#!/usr/bin/env python3
"""
Helper script do zarządzania bazą danych transkrypcji.
Używany przez agentów do śledzenia statusów przetwarzania.
"""

import sqlite3
import os
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "Notatki" / "rejestr_transkrypcji.db"

def get_connection():
    """Połączenie z bazą danych."""
    return sqlite3.connect(str(DB_PATH))

def get_file_id(sciezka: str, typ: str = None):
    """
    Pobierz ID pliku z bazy.
    
    Args:
        sciezka: Ścieżka relatywna do Notatki/ (np. "Transkrypcje/surowe/plik.md")
        typ: Opcjonalnie typ pliku ('surowa', 'oczyszczona', 'notatka')
    
    Returns:
        ID pliku lub None jeśli nie znaleziono
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    if typ:
        cursor.execute("SELECT id FROM pliki WHERE sciezka = ? AND typ = ?", (sciezka, typ))
    else:
        cursor.execute("SELECT id FROM pliki WHERE sciezka = ?", (sciezka,))
    
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else None

def add_file(sciezka: str, typ: str, nazwa: str):
    """
    Dodaj nowy plik do bazy.
    
    Args:
        sciezka: Ścieżka relatywna do Notatki/
        typ: 'surowa', 'oczyszczona', 'notatka'
        nazwa: Nazwa pliku
    
    Returns:
        ID nowo dodanego pliku
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Sprawdź czy już istnieje
    existing_id = get_file_id(sciezka, typ)
    if existing_id:
        conn.close()
        return existing_id
    
    # Pobierz daty z systemu plików
    full_path = DB_PATH.parent / sciezka
    if full_path.exists():
        stat = full_path.stat()
        data_utworzenia = datetime.fromtimestamp(stat.st_birthtime).strftime('%Y-%m-%d %H:%M:%S')
        data_modyfikacji = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    else:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_utworzenia = now
        data_modyfikacji = now
    
    cursor.execute("""
        INSERT INTO pliki (sciezka, typ, nazwa, data_utworzenia, data_modyfikacji, zarchiwizowany)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (sciezka, typ, nazwa, data_utworzenia, data_modyfikacji, 0))
    
    file_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return file_id

def mark_as_archived(plik_id: int):
    """Oznacz plik jako zarchiwizowany."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE pliki 
        SET zarchiwizowany = 1, 
            data_archiwizacji = ?
        WHERE id = ?
    """, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), plik_id))
    
    conn.commit()
    conn.close()

def start_processing(plik_zrodlowy_id: int, etap: str):
    """
    Oznacz przetwarzanie jako rozpoczęte (status: w_trakcie).
    
    Args:
        plik_zrodlowy_id: ID pliku źródłowego
        etap: 'surowa->oczyszczona' lub 'oczyszczona->notatka'
    
    Returns:
        ID rekordu przetwarzania lub None jeśli już przetwarzane
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Sprawdź czy już nie ma w trakcie
    cursor.execute("""
        SELECT id, status FROM przetwarzanie 
        WHERE plik_zrodlowy_id = ? AND etap = ?
    """, (plik_zrodlowy_id, etap))
    
    result = cursor.fetchone()
    
    if result:
        existing_id, status = result
        if status == 'w_trakcie':
            conn.close()
            return None  # Już przetwarzane przez inny proces
        elif status == 'zakonczone':
            conn.close()
            return None  # Już zakończone
        else:
            # Status 'oczekujace' - zaktualizuj na 'w_trakcie'
            cursor.execute("""
                UPDATE przetwarzanie 
                SET status = 'w_trakcie',
                    data_przetworzenia = ?
                WHERE id = ?
            """, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), existing_id))
            conn.commit()
            conn.close()
            return existing_id
    
    # Utwórz nowy rekord
    cursor.execute("""
        INSERT INTO przetwarzanie (plik_zrodlowy_id, etap, data_przetworzenia, status)
        VALUES (?, ?, ?, 'w_trakcie')
    """, (plik_zrodlowy_id, etap, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    processing_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return processing_id

def finish_processing(processing_id: int, plik_wynikowy_id: int, uwagi: str = None):
    """
    Oznacz przetwarzanie jako zakończone.
    
    Args:
        processing_id: ID rekordu przetwarzania
        plik_wynikowy_id: ID wygenerowanego pliku
        uwagi: Opcjonalne uwagi
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE przetwarzanie 
        SET status = 'zakonczone',
            plik_wynikowy_id = ?,
            uwagi = ?,
            data_przetworzenia = ?
        WHERE id = ?
    """, (plik_wynikowy_id, uwagi, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), processing_id))
    
    conn.commit()
    conn.close()

def is_being_processed(plik_id: int, etap: str):
    """
    Sprawdź czy plik jest już przetwarzany.
    
    Returns:
        True jeśli w trakcie lub zakończone, False jeśli można przetwarzać
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT status FROM przetwarzanie 
        WHERE plik_zrodlowy_id = ? AND etap = ?
    """, (plik_id, etap))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        status = result[0]
        return status in ('w_trakcie', 'zakonczone')
    
    return False

def get_unprocessed_files(etap: str, limit: int = 100):
    """
    Pobierz listę plików do przetworzenia.
    
    Args:
        etap: 'surowa->oczyszczona' lub 'oczyszczona->notatka'
        limit: Maksymalna liczba plików
    
    Returns:
        Lista (id, sciezka, nazwa) plików gotowych do przetworzenia
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    if etap == 'surowa->oczyszczona':
        typ_zrodlowy = 'surowa'
    elif etap == 'oczyszczona->notatka':
        typ_zrodlowy = 'oczyszczona'
    else:
        return []
    
    # Znajdź pliki które:
    # 1. Są odpowiedniego typu
    # 2. Nie są zarchiwizowane
    # 3. Nie są w trakcie ani zakończone
    # SORTOWANIE: po nazwie (data spotkania w nazwie), nie po data_utworzenia (data dodania do bazy)
    cursor.execute("""
        SELECT p.id, p.sciezka, p.nazwa
        FROM pliki p
        LEFT JOIN przetwarzanie pr ON p.id = pr.plik_zrodlowy_id AND pr.etap = ?
        WHERE p.typ = ?
          AND p.zarchiwizowany = 0
          AND (pr.status IS NULL OR pr.status = 'oczekujace')
        ORDER BY p.nazwa ASC
        LIMIT ?
    """, (etap, typ_zrodlowy, limit))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

def add_project_mapping(notatka_id: int, projekt_sciezka: str, data_mapowania: str = None, uwagi: str = None):
    """
    Dodaj mapowanie notatki do projektu.
    
    Args:
        notatka_id: ID notatki
        projekt_sciezka: Ścieżka do projektu (z prefiksem Projekty/)
        data_mapowania: Data (domyślnie teraz)
        uwagi: Opcjonalne uwagi
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    if not data_mapowania:
        data_mapowania = datetime.now().strftime('%Y-%m-%d')
    
    # Sprawdź czy już istnieje
    cursor.execute("""
        SELECT COUNT(*) FROM mapowania_projektow
        WHERE notatka_id = ? AND projekt_sciezka = ?
    """, (notatka_id, projekt_sciezka))
    
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # Już istnieje
    
    cursor.execute("""
        INSERT INTO mapowania_projektow (notatka_id, projekt_sciezka, data_mapowania, uwagi)
        VALUES (?, ?, ?, ?)
    """, (notatka_id, projekt_sciezka, data_mapowania, uwagi))
    
    conn.commit()
    conn.close()

def get_stats():
    """Pobierz statystyki bazy."""
    conn = get_connection()
    cursor = conn.cursor()
    
    stats = {}
    
    cursor.execute("SELECT COUNT(*) FROM pliki WHERE typ = 'surowa'")
    stats['surowe'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM pliki WHERE typ = 'oczyszczona'")
    stats['oczyszczone'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM pliki WHERE typ = 'notatka'")
    stats['notatki'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM przetwarzanie WHERE etap = 'surowa->oczyszczona' AND status = 'zakonczone'")
    stats['przetworzone_surowe'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM przetwarzanie WHERE etap = 'oczyszczona->notatka' AND status = 'zakonczone'")
    stats['przetworzone_oczyszczone'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mapowania_projektow")
    stats['mapowania'] = cursor.fetchone()[0]
    
    conn.close()
    
    return stats

def scan_and_register_raw_files(dir_path: str = "Notatki/Transkrypcje/surowe"):
    """
    Skanuje katalog w poszukiwaniu nowych plików .md i dodaje je do bazy.
    
    Args:
        dir_path: Ścieżka do katalogu z surowymi transkrypcjami (domyślnie 'Notatki/Transkrypcje/surowe')
    
    Returns:
        Liczba nowo dodanych plików.
    """
    target_dir = DB_PATH.parent.parent / dir_path
    if not target_dir.exists():
        return 0
        
    added_count = 0
    
    # Pobierz listę plików .md (z wyłączeniem README.md)
    files = [f for f in target_dir.glob("*.md") if f.name != "README.md"]
    
    for f in files:
        # Ścieżka relatywna do Notatki/ (np. Transkrypcje/surowe/plik.md)
        if dir_path.startswith("Notatki/"):
            rel_path_dir = dir_path[8:] # Usuń "Notatki/"
        else:
            rel_path_dir = dir_path
            
        rel_path = f"{rel_path_dir}/{f.name}"
        
        # Sprawdź czy plik już istnieje w bazie (typ 'surowa')
        existing_id = get_file_id(rel_path, 'surowa')
        
        if not existing_id:
            add_file(rel_path, 'surowa', f.name)
            added_count += 1
            
    return added_count


if __name__ == "__main__":
    import argparse

    # Argument parsing
    parser = argparse.ArgumentParser(description="Helper script to manage transcription database.")
    subparsers = parser.add_subparsers(dest="command")

    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Get database statistics.")

    # Scan command
    scan_parser = subparsers.add_parser("scan_and_register", help="Scan directory for new raw files.")
    scan_parser.add_argument("--dir", type=str, default="Notatki/Transkrypcje/surowe", help="Directory to scan")

    # Add file command
    add_file_parser = subparsers.add_parser("add_file", help="Add a file to the database.")

    add_file_parser.add_argument("sciezka", type=str, help="Relative path to Notatki/ (e.g., 'Transkrypcje/surowe/plik.md')")
    add_file_parser.add_argument("typ", type=str, choices=['surowa', 'oczyszczona', 'notatka'], help="File type ('surowa', 'oczyszczona', 'notatka')")
    add_file_parser.add_argument("nazwa", type=str, help="File name")

    # Get unprocessed files command
    get_unprocessed_parser = subparsers.add_parser("get_unprocessed_files", help="Get a list of files ready for processing.")
    get_unprocessed_parser.add_argument("etap", type=str, choices=['surowa->oczyszczona', 'oczyszczona->notatka'], help="Processing stage ('surowa->oczyszczona' or 'oczyszczona->notatka')")
    get_unprocessed_parser.add_argument("--limit", type=int, default=100, help="Maximum number of files to return.")

    # Start processing command
    start_processing_parser = subparsers.add_parser("start_processing", help="Mark processing as started.")
    start_processing_parser.add_argument("plik_zrodlowy_id", type=int, help="Source file ID")
    start_processing_parser.add_argument("etap", type=str, choices=['surowa->oczyszczona', 'oczyszczona->notatka'], help="Processing stage")

    # Finish processing command
    finish_processing_parser = subparsers.add_parser("finish_processing", help="Mark processing as finished.")
    finish_processing_parser.add_argument("processing_id", type=int, help="Processing record ID")
    finish_processing_parser.add_argument("plik_wynikowy_id", type=int, help="Generated file ID")
    finish_processing_parser.add_argument("--uwagi", type=str, default=None, help="Optional remarks")

    # Mark as archived command
    mark_archived_parser = subparsers.add_parser("mark_as_archived", help="Mark a file as archived.")
    mark_archived_parser.add_argument("plik_id", type=int, help="File ID to archive")

    args = parser.parse_args()

    if args.command == "stats":
        stats = get_stats()
        print("📊 Statystyki bazy:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    elif args.command == "scan_and_register":
        count = scan_and_register_raw_files(args.dir)
        print(f"Registered {count} new files.")
    elif args.command == "add_file":
        file_id = add_file(args.sciezka, args.typ, args.nazwa)
        print(f"Added file with ID: {file_id}")
        stats = get_stats()
        print("📊 Statystyki bazy:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    elif args.command == "get_unprocessed_files":
        files = get_unprocessed_files(args.etap, args.limit)
        if files:
            for file_data in files:
                print(f"{file_data[0]}|{file_data[1]}|{file_data[2]}")
        else:
            print("(empty)")
    elif args.command == "start_processing":
        processing_id = start_processing(args.plik_zrodlowy_id, args.etap)
        if processing_id:
            print(f"Started processing with ID: {processing_id}")
        else:
            print("Processing already in progress or completed for this file.")
    elif args.command == "finish_processing":
        finish_processing(args.processing_id, args.plik_wynikowy_id, args.uwagi)
        print(f"Finished processing ID: {args.processing_id}")
    elif args.command == "mark_as_archived":
        mark_as_archived(args.plik_id)
        print(f"Marked file ID: {args.plik_id} as archived.")

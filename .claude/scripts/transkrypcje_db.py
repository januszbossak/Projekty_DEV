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


if __name__ == "__main__":
    # Test
    stats = get_stats()
    print("📊 Statystyki bazy:")
    for key, value in stats.items():
        print(f"  {key}: {value}")


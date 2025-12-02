#!/usr/bin/env python3
"""
Skrypt do znajdowania notatek wymagających review (nieposiadających pliku -codex.md).
Łączy notatkę z plikami transkrypcji na podstawie bazy danych lub (fallback) nazewnictwa.
"""

import sqlite3
import os
from pathlib import Path
import sys

# Add path to access existing db module
sys.path.append(os.path.join(os.getcwd(), '.claude', 'scripts'))
from transkrypcje_db import get_connection

PROJECT_ROOT = Path(os.getcwd())
NOTES_DIR = PROJECT_ROOT / "Notatki"
ARCHIVE_DIR = NOTES_DIR / "Transkrypcje" / "oczyszczone-archiwum"

def find_candidates():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Pobierz wszystkie zakończone przetwarzania "oczyszczona->notatka"
    # Łączymy z tabelą pliki, aby mieć ścieżki
    cursor.execute("""
        SELECT 
            p.plik_wynikowy_id, 
            f_note.sciezka as note_path,
            f_note.nazwa as note_name,
            p.plik_zrodlowy_id,
            f_source.nazwa as source_name
        FROM przetwarzanie p
        JOIN pliki f_note ON p.plik_wynikowy_id = f_note.id
        JOIN pliki f_source ON p.plik_zrodlowy_id = f_source.id
        WHERE p.etap = 'oczyszczona->notatka' AND p.status = 'zakonczone'
    """)
    
    results = cursor.fetchall()
    
    # Słownik: Note Path -> List of Source Files (obsługa wielu części)
    candidates = {}
    
    for row in results:
        note_id, note_rel_path, note_name, source_id, source_name = row
        
        # Pełna ścieżka do notatki
        full_note_path = NOTES_DIR / note_rel_path
        
        # Jeśli ścieżka w bazie jest relatywna do Notatki/ (np. "Spotkania/Notatka.md")
        # to NOTES_DIR / note_rel_path jest OK.
        # Czasem w bazie może być pełna ścieżka "Notatki/..." - trzeba obsłużyć
        if note_rel_path.startswith("Notatki/"):
             full_note_path = PROJECT_ROOT / note_rel_path
        else:
             full_note_path = NOTES_DIR / note_rel_path

        # Sprawdź czy notatka istnieje
        if not full_note_path.exists():
            continue
            
        # Sprawdź czy istnieje już CODEX
        codex_path = full_note_path.parent / (full_note_path.stem + "-codex.md")
        if codex_path.exists():
            continue
            
        # Znajdź pliki źródłowe (transkrypcje)
        # W bazie mamy ID pliku źródłowego. Zwykle to plik w "oczyszczone".
        # Ale po zakończeniu on trafia do "oczyszczone-archiwum".
        # Sprawdzamy w archiwum.
        
        source_files = []
        
        # Logika dla plików wieloczęściowych:
        # Jeśli source_name to "2025-10-09... część 1.md", to szukamy też części 2, 3...
        # W bazie często jest link tylko do jednej części (np. 1) jako "źródło" notatki.
        
        base_name_part = source_name
        if " - część " in source_name:
            base_name_part = source_name.split(" - część ")[0]
            # Szukaj wszystkich plików w archiwum zaczynających się od base_name_part
            for f in ARCHIVE_DIR.glob(f"{base_name_part}*"):
                source_files.append(str(f))
        else:
            # Pojedynczy plik
            possible_path = ARCHIVE_DIR / source_name
            if possible_path.exists():
                source_files.append(str(possible_path))
            else:
                # Może jeszcze w oczyszczone? (mało prawdopodobne dla zakończonych)
                pass
        
        if not source_files:
            # Fallback: szukanie po dacie i typie z nazwy notatki
            # np. Note: 2025-10-23 Spotkanie.md -> Szukaj 2025-10-23* w archiwum
            date_prefix = note_name[:10] # YYYY-MM-DD
            for f in ARCHIVE_DIR.glob(f"{date_prefix}*"):
                source_files.append(str(f))

        source_files = sorted(list(set(source_files))) # Unikalne i posortowane
        
        if source_files:
            candidates[str(full_note_path)] = source_files

    conn.close()
    
    # Zwróć pierwszy kandydat (najstarszy)
    if not candidates:
        print("NO_CANDIDATES")
    else:
        # Sortuj po nazwie notatki (chronologicznie rosnąco - najstarsze pierwsze)
        # Nazwy notatek zaczynają się od YYYY-MM-DD, więc sortowanie alfabetyczne = chronologiczne
        sorted_notes = sorted(candidates.keys()) 
        
        target_note = sorted_notes[0]
        sources = candidates[target_note]
        
        print(f"NOTE|{target_note}")
        print(f"SOURCES|{len(sources)}")
        for s in sources:
            print(f"SRC|{s}")

if __name__ == "__main__":
    find_candidates()

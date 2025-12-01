import sys
import os
import sqlite3
from pathlib import Path

sys.path.append(os.path.join(os.getcwd(), '.claude', 'scripts'))
from transkrypcje_db import get_connection, add_file

def sync_folder():
    folder_path = Path("Notatki/Transkrypcje/oczyszczone")
    conn = get_connection()
    cursor = conn.cursor()
    
    print(f"Scanning {folder_path}...")
    
    count_added = 0
    count_restored = 0
    
    for file_path in folder_path.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        rel_path = f"oczyszczone/{file_path.name}"
        
        # Check if exists in DB
        cursor.execute("SELECT id, zarchiwizowany FROM pliki WHERE sciezka = ?", (rel_path,))
        result = cursor.fetchone()
        
        if result:
            file_id, archived = result
            if archived:
                # Restore file
                print(f"Restoring archived file: {file_path.name}")
                cursor.execute("UPDATE pliki SET zarchiwizowany = 0 WHERE id = ?", (file_id,))
                
                # Reset processing status if any
                cursor.execute("DELETE FROM przetwarzanie WHERE plik_zrodlowy_id = ? AND etap = 'oczyszczona->notatka'", (file_id,))
                count_restored += 1
        else:
            # Add new file
            print(f"Adding new file: {file_path.name}")
            add_file(rel_path, 'oczyszczona', file_path.name)
            count_added += 1
            
    conn.commit()
    conn.close()
    
    print(f"Sync complete. Added: {count_added}, Restored: {count_restored}")

if __name__ == "__main__":
    try:
        sync_folder()
    except Exception as e:
        print(f"ERROR: {e}")

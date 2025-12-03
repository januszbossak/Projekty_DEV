import sys
import os
from pathlib import Path
import sqlite3

DB_PATH = Path(os.getcwd()) / "Notatki" / "rejestr_transkrypcji.db"

def get_connection():
    return sqlite3.connect(str(DB_PATH))

def get_file_status(sciezka: str, typ: str):
    conn = get_connection()
    cursor = conn.cursor()
    # Normalize path before querying to match how it might be stored
    if not sciezka.startswith("Notatki/"):
        sciezka = f"Notatki/{sciezka}" # Assuming all paths are stored relative to Notatki/ in DB
    
    # First, try exact match
    cursor.execute("SELECT id, zarchiwizowany FROM pliki WHERE sciezka = ? AND typ = ?", (sciezka, typ))
    file_info = cursor.fetchone()

    # If not found, try without 'Notatki/' prefix in sciezka
    if not file_info and sciezka.startswith("Notatki/"):
        sciezka_without_prefix = sciezka[len("Notatki/"):]
        cursor.execute("SELECT id, zarchiwizowany FROM pliki WHERE sciezka = ? AND typ = ?", (sciezka_without_prefix, typ))
        file_info = cursor.fetchone()

    if file_info:
        file_id, zarchiwizowany = file_info
        cursor.execute("SELECT status FROM przetwarzanie WHERE plik_zrodlowy_id = ? AND etap = 'surowa->oczyszczona'", (file_id,))
        processing_info = cursor.fetchone()
        status = processing_info[0] if processing_info else 'nie_przetwarzane'
        conn.close()
        return file_id, zarchiwizowany, status
    conn.close()
    return None

file_path_relative = "Transkrypcje/surowe/2025-12-02 Spotkanie projektowe - AMODIT UI.md"
status = get_file_status(file_path_relative, 'surowa')
if status:
    print(f"File ID: {status[0]}, Archived: {bool(status[1])}, Processing Status: {status[2]}")
else:
    print("File not found in DB or not of type 'surowa'")

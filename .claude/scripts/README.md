# Helper Scripts

## transkrypcje_db.py

Helper do zarządzania bazą danych transkrypcji (`Notatki/rejestr_transkrypcji.db`).

### Użycie w agentach

```python
from .claude.scripts.transkrypcje_db import *

# Pobierz nieprzetwarzane pliki
pliki = get_unprocessed_files('surowa->oczyszczona', limit=5)

# Dla każdego pliku
for plik_id, sciezka, nazwa in pliki:
    # 1. Oznacz start (zapobiega równoległemu przetwarzaniu)
    processing_id = start_processing(plik_id, 'surowa->oczyszczona')
    if not processing_id:
        continue  # Już przetwarzane przez innego agenta
    
    # 2. Wykonaj przetwarzanie...
    
    # 3. Dodaj wynikowy plik
    wynik_id = add_file('Transkrypcje/oczyszczone/wynik.md', 'oczyszczona', 'wynik.md')
    
    # 4. Oznacz archiwizację źródła
    mark_as_archived(plik_id)
    
    # 5. Zakończ przetwarzanie
    finish_processing(processing_id, wynik_id, uwagi="OK")
```

### Funkcje

| Funkcja | Opis |
|---------|------|
| `get_file_id(sciezka, typ)` | Pobierz ID pliku z bazy |
| `add_file(sciezka, typ, nazwa)` | Dodaj nowy plik do bazy |
| `start_processing(plik_id, etap)` | Oznacz rozpoczęcie przetwarzania (status: w_trakcie) |
| `finish_processing(processing_id, wynik_id, uwagi)` | Zakończ przetwarzanie (status: zakonczone) |
| `mark_as_archived(plik_id)` | Oznacz plik jako zarchiwizowany |
| `is_being_processed(plik_id, etap)` | Sprawdź czy plik jest przetwarzany |
| `get_unprocessed_files(etap, limit)` | Pobierz listę plików do przetworzenia |
| `add_project_mapping(notatka_id, projekt, data, uwagi)` | Dodaj mapowanie notatki do projektu |
| `get_stats()` | Pobierz statystyki bazy |

### Etapy pipeline

- `'surowa->oczyszczona'` - czyszczenie transkrypcji
- `'oczyszczona->notatka'` - generowanie notatki

### Typy plików

- `'surowa'` - surowa transkrypcja
- `'oczyszczona'` - oczyszczona transkrypcja
- `'notatka'` - wygenerowana notatka strukturalna

### Statusy przetwarzania

- `'oczekujace'` - plik czeka na przetworzenie
- `'w_trakcie'` - plik jest aktualnie przetwarzany (blokada)
- `'zakonczone'` - przetwarzanie zakończone

## Test

```bash
python3 .claude/scripts/transkrypcje_db.py
```

Wyświetli statystyki bazy.


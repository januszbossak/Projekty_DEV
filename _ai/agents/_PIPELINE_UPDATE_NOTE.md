# UWAGA: Pipeline Runner - Używa Bazy SQL

Agent `pipeline-runner` został zaktualizowany do używania bazy SQL zamiast rejestrów markdown.

## Kluczowe zmiany:

1. **Zamiast czytania `_transkrypcje.md`** → używaj `get_unprocessed_files()` z `_ai/scripts/transkrypcje_db.py`

2. **Przed przetwarzaniem** → wywołaj `start_processing(plik_id, etap)` aby oznaczyć status 'w_trakcie'

3. **Po zakończeniu** → wywołaj:
   - `add_file()` dla nowych plików
   - `mark_as_archived()` dla zarchiwizowanych
   - `finish_processing()` aby oznaczyć 'zakonczone'

4. **Równoległe przetwarzanie:** Statusy 'w_trakcie' automatycznie zapobiegają przetwarzaniu tego samego pliku przez wielu agentów

## Workflow (dla każdego etapu):

```python
from .claude.scripts.transkrypcje_db import *

# 1. Pobierz pliki do przetworzenia
pliki = get_unprocessed_files('surowa->oczyszczona')  # lub 'oczyszczona->notatka'

# 2. Dla każdego pliku:
for plik_id, sciezka, nazwa in pliki:
    # Oznacz start
    processing_id = start_processing(plik_id, 'surowa->oczyszczona')
    if not processing_id:
        continue  # Już przetwarzane
    
    # ... wykonaj przetwarzanie ...
    
    # Dodaj wynikowy plik
    wynik_id = add_file('sciezka/wynik.md', 'oczyszczona', 'wynik.md')
    
    # Zarchiwizuj źródło
    mark_as_archived(plik_id)
    
    # Zakończ
    finish_processing(processing_id, wynik_id)
```

**Szczegóły:** Zobacz zaktualizowane agenty `transcript-cleaner.md` i `note-maker.md` dla pełnych przykładów.


# Oczyszczone transkrypcje

Ten folder zawiera transkrypcje po czyszczeniu (korekta fonetyczna ASR, redukcja szumu), gotowe do generowania notatek strukturalnych.

## Status plików

Pliki w tym folderze:
- ✅ Zostały oczyszczone z błędów ASR i szumu komunikacyjnego
- ✅ Mają wpis w rejestrze `_transkrypcje.md` z wypełnioną kolumną "Oczyszczony"
- ⏳ Oczekują na przetworzenie do notatki strukturalnej

## Workflow

```
surowe/plik.md 
    ↓ [czyszczenie przez transcript-cleaner]
oczyszczone/plik - transkrypcja.md  ← TEN FOLDER
    ↓ [generowanie notatki przez note-maker]
Notatki/{typ}/plik.md
```

**⚠️ UWAGA:** Po wygenerowaniu notatki, oczyszczona transkrypcja jest automatycznie przenoszona do `oczyszczone-archiwum/`.

## Duże transkrypcje (rozbite na części)

Transkrypcje powyżej ~800 linii są automatycznie dzielone na części podczas czyszczenia:
- `plik - transkrypcja - część 1.md`
- `plik - transkrypcja - część 2.md`
- `plik - transkrypcja - część 3.md`
- etc.

Podczas generowania notatki, wszystkie części są automatycznie wczytywane i łączone.

## Co dalej?

Aby wygenerować notatkę z oczyszczonej transkrypcji:
- **Pojedyncza:** `"Wygeneruj notatkę"` (wywołuje `note-maker`)
- **Cały pipeline:** `"Przetwórz nowe"` (wywołuje `pipeline-runner`)


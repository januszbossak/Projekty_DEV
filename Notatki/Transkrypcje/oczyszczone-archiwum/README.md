# Archiwum oczyszczonych transkrypcji

Ten folder zawiera oczyszczone transkrypcje, które zostały już przetworzone na notatki strukturalne.

## Proces archiwizacji

Po wygenerowaniu notatki z oczyszczonej transkrypcji:
1. Oczyszczona transkrypcja jest automatycznie przenoszona z `oczyszczone/` do `oczyszczone-archiwum/`
2. Zachowane są oryginalne nazwy plików (w tym numery części jeśli była rozbita)
3. Notatka strukturalna trafia do `Notatki/{typ}/`

## Status plików w tym folderze

Wszystkie pliki tutaj:
- ✅ Mają wygenerowaną notatkę strukturalną w `Notatki/{typ}/`
- ✅ Mają wpis w rejestrze `_rejestr_transkrypcji_przelozonych_na_notatki.md` z `[x]`
- ✅ Mają wpis w rejestrze `_rejestr_przetworzonych.md` (notatka oczekuje na mapowanie na projekty)

## Workflow pełny

```
surowe/plik.md 
    ↓ [czyszczenie]
surowe - archiwum/plik.md + oczyszczone/plik - transkrypcja.md
    ↓ [generowanie notatki]
oczyszczone-archiwum/plik - transkrypcja.md + Notatki/{typ}/plik.md
```

## Przywracanie pliku

Jeśli potrzebujesz ponownie wygenerować notatkę z oczyszczonej transkrypcji:
1. Przenieś plik z `oczyszczone-archiwum/` do `oczyszczone/`
2. Usuń lub zmień status `[x]` na `[ ]` w `_rejestr_transkrypcji_przelozonych_na_notatki.md`
3. Uruchom `note-maker` lub `pipeline-runner` ponownie


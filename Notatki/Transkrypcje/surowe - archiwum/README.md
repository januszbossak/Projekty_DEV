# Archiwum surowych transkrypcji

Ten folder zawiera surowe transkrypcje, które zostały już przetworzone (oczyszczone).

## Proces archiwizacji

Po oczyszczeniu transkrypcji przez pipeline:
1. Surowy plik jest automatycznie przenoszony z `surowe/` do `surowe - archiwum/`
2. Zachowana jest oryginalna nazwa pliku
3. Oczyszczona wersja trafia do `oczyszczone/`

## Status plików w tym folderze

Wszystkie pliki tutaj:
- ✅ Mają oczyszczoną wersję w `oczyszczone/`
- ✅ Mają wpis w rejestrze `_transkrypcje.md` z wypełnioną kolumną "Oczyszczony"
- ✅ Mogą mieć wygenerowaną notatkę w `Notatki/{typ}/`

## Przywracanie pliku

Jeśli potrzebujesz ponownie przetworzyć surową transkrypcję:
1. Przenieś plik z `surowe - archiwum/` do `surowe/`
2. Usuń wpis z kolumny "Oczyszczony" w `_transkrypcje.md`
3. Uruchom pipeline ponownie


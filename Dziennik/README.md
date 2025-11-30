# Dziennik

Folder na dzienne notatki w formacie `YYYY-MM-DD.md`.

## Jak to działa

Dzienniki są tworzone automatycznie przez Obsidian przy użyciu linkowania `[[YYYY-MM-DD]]` w dokumentach.

**Przykład użycia:**
- W projekcie: `Decyzja podjęta [[2025-08-12]]`
- W tabeli Historia zmian: `| [[2025-08-12]] | Zmiana | [[2025-08-12 Rada architektów]] |`

**Obsidian automatycznie:**
- Utworzy plik `2025-08-12.md` (jeśli nie istnieje)
- Wyświetli linki zwrotne do wszystkich miejsc gdzie użyto tej daty
- Umożliwi przegląd wszystkich wydarzeń z danego dnia

**UWAGA:** Nie musisz tworzyć plików dzienników ręcznie - Obsidian zrobi to automatycznie przy pierwszym użyciu linku. Ten folder może być pusty - Obsidian utworzy pliki na żądanie.


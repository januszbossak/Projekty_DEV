# CHANGELOG - Repozytorium plików (DMS)

Historia ustaleń i zmian dla projektu.

---

## 2025-10-28 | Spotkanie projektowe - Design
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-28 Spotkanie projektowe - Design.md]
**Kategoria:** #Architektura #Design #Funkcjonalność #Decyzja #MVP #Ryzyko

- **Struktura repozytorium:** Przestrzenie jako najwyższy poziom, foldery zagnieżdżone, pliki. Maksymalna głębokość zagnieżdżenia do ustalenia.
- **System uprawnień i dziedziczenie:** Domyślne dziedziczenie, możliwość przerwania dziedziczenia na poziomie folderu/pliku. Widoczność folderu jako uprawnienie wynikowe.
- **Przechowywanie plików:** Pliki lokalnie na zasobach sieciowych (MVP), spójne z attachmentami AMODIT. Struktura fizyczna oparta na ID węzłów.
- **Metadane plików:** Tylko techniczne/systemowe w MVP. Metadane użytkownika (opis, tagi, daty) poza MVP.
- **Interfejs użytkownika:** Widok drzewa folderów po lewej, główny obszar zawartości, breadcrumbs. Widoki plików: kafelkowy (MVP), lista (do rozważenia).
- **Wyszukiwanie plików:** Pełnotekstowe w oparciu o Lucene, z filtrowaniem wyników po uprawnieniach użytkownika. Ryzyka wydajnościowe/bezpieczeństwa do zaadresowania.
- **Bezpieczeństwo i szyfrowanie plików:** Pytanie o szyfrowanie plików i wpływ struktury opartej na ID na zarządzanie backupem.
- **Funkcjonalności poza MVP:** Wersjonowanie, historia zmian, przenoszenie plików, linki publiczne, etykiety/tagi, powiadomienia, eksport/import struktury, metadane użytkownika.
- **Ogólne uwagi i ryzyka:** Gigantyczny projekt, podejście z AI (Filip) może skrócić czas realizacji o 50% (z 6 do 2-3 miesięcy). Wymaga sprawnego backendu.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Organizacja #Decyzja

- Ania powinna skupić się na repozytorium (zamiast tłumaczeń).
- Nie dawać jej podglądu szablonów (grubsza sprawa).

---

## 2025-10-23 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Rada architektow.md]
**Kategoria:** #Architektura #Decyzja

- Koncepcja repozytorium plików w AMODIT (niezwiązanego ze sprawami).
- Preferencja: struktura fizyczna oparta na ID, czytelna ścieżka logiczna w URL.
- Przechowywanie raczej na dysku; do decyzji, czy wspierać tryb "w bazie" (Blob).
- Status: Do doprecyzowania (warsztat, brak akceptacji).

---
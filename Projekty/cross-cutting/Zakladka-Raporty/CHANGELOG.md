# CHANGELOG - Zakładka Raporty

## 2025-10-02 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-02 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-10-02%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Bug

- Naprawa działania linku "Raporty systemowe" z menu modułów systemowych w trybie listy
- Decyzja: Link będzie automatycznie wymuszał przełączenie widoku na tryb kafelkowy

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Funkcjonalność

**Cel:**
Usprawnienie zarządzania i odnajdywania raportów poprzez nowy format wyświetlania, bardziej ergonomiczne kafelki oraz nowe widoki z dodatkowymi metadanymi. Szczególnie przydatne z perspektywy administratorów systemu czy procesów.

### Nowe formaty wyświetlania

- Kafelki bardziej ergonomiczne i nowocześniejsze
- Nowy widok listy z dodatkowymi metadanymi (ułatwia zarządzanie i odnajdywanie raportów)
- Dwa typy list: zwykła i kompaktowa (pozwala zobaczyć więcej elementów na jednym ekranie)
- Na liście widać opisy raportu (łatwiej się zorientować, do czego służy)

### Nowe sposoby sortowania i filtrowania

- Zapamiętywanie filtrowania w ramach obszarów w menu Raporty (per użytkownik)
- Wizualne rozróżnianie raportów poprzez reprezentację każdego typu raportu odpowiednią ikoną
- Nowe sposoby filtrowania:
  - Raporty, które ja utworzyłem
  - Raporty utworzone przez kogokolwiek innego
  - Ostatnio modyfikowane
  - Określone typy raportów (np. kolumnowy, pivot)
- Szukanie raportu po jego źródle (np. proces "Obieg faktur" lub "Kandydaci")

### Szczegóły techniczne

- Obszary przepisane na nową technologię frontendową – React
- Podział na czysty backend i frontend (łatwiejsza konserwacja, łatwiejsza modyfikacja elementów frontendowych)
- Poprawiona wydajność ładowania list


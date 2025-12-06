# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-10-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-21 Rada architektów.md]
**Kategoria:** #Decyzja #Architektura

- Wyświetlanie błędów konfliktów GUID przy imporcie XML pozostaje w formie tabelki (działa, wymusza uwagę).
- Kompleksowe przeprojektowanie importu procesów odroczone (do realizacji przez Filipa).
- Możliwość wpisania GUID na środowisku (przypisanie z produkcji na teście) odroczona.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność #Problem

- Dokładniejsza walidacja pól przy imporcie XML (zapobieganie psuciu procesów)
- Wykrywanie konfliktów nazw pól z różnymi GUID
- Wykrywanie konfliktów nazw pól z przypisaniem do innych pól w bazie
- Blokada importu w przypadku wykrycia konfliktów

---

## 2025-10-09 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-09 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Bezpieczeństwo #Decyzja

- Problem z importem procesów i konfliktami przypisań pól do kolumn CaseText (ryzyko przekłamania danych)
- Decyzja: Blokowanie nadpisywania procesu przy konfliktach przypisań pól i wyświetlanie komunikatu z instrukcją naprawy

---
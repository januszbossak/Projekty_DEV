# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-01 | Planowanie sprintu (Szczegóły)
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Planowanie sprintu.md]
**Kategoria:** #Zadanie

- Priorytet: Indeksacja dla 100% poprawności raportów tabelarycznych.

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Wydajnosc #Bug #Zadanie

- Dokończenie indeksacji dla raportu tabelarycznego.
- Zapewnienie 100% działania raportu tabelarycznego bez błędów.
- Eliminacja błędów związanych z raportem tabelarycznym.

---

## 2025-11-18 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-18 Notatka projektowa - Ulepszanie filtrów użytkownika w raportach.md]
**Kategoria:** #Architektura #Decyzja #Zadanie

- Potrzeba indeksowania pól do wyszukiwania tekstowego w filtrach (długoterminowo)
- Piotr sugeruje mechanizm indeksowania pól
- Tymczasowa poprawa wydajności filtrów poprzez dodanie opcji `DISTINCT` na backendzie
- Odłożenie głębokich zmian wydajnościowych na późniejszy etap

---

## 2025-11-18 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-18 Rada architektów.md]
**Kategoria:** #Wydajność #Decyzja #Problem

- Zidentyfikowane ryzyka: spadek wydajności przy wyszukiwaniu wartości filtrów na dużych zbiorach danych (brak indeksów, LIKE %%).
- Decyzja: Należy wdrożyć mechanizm indeksowania pól dla optymalizacji wydajności filtrów.
- Indeksowanie powinno obsługiwać wyszukiwanie od początku frazy, ograniczenie liczby indeksowanych kolumn.

---

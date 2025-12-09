# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Design

- Szymek/Przemek porządkują operatory daty w filtrach użytkownika, uspójniając logikę ("ostatnie 7 dni" vs "tydzień temu").

---

## 2025-11-18 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-18 Notatka projektowa - Ulepszanie filtrów użytkownika w raportach.md]
**Kategoria:** #Funkcjonalność #Design #Bug #Decyzja #Zadanie

- Poprawa wydajności i użyteczności filtrów pól tekstowych (LIKE %...%, indeksowanie)
- Rozróżnienie logiki wyświetlania w filtrach słownikowych (małe vs duże słowniki)
- Zmiana nazwy przycisku "Zaznacz wszystko" na "Zaznacz widoczne"
- Uporządkowanie kolejności i nazewnictwa operatorów filtra daty
- Wypracowanie informatywnych "empty state screens" dla raportów
- Mateusz Kisiel: Poprawka mechanizmu `SELECT DISTINCT` w filtrach (backend)
- Przemysław Rogaś: Zaimplementować zmiany dla "Zaznacz widoczne" i operatorów daty

---

## 2025-11-18 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-18 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Problem #Decyzja

- Problemy z podpowiedziami w filtrach raportów (brak wartości, limit 20 rekordów).
- Nieoptymalna wydajnościowo implementacja podpowiedzi (DISTINCT, LIKE %...% na nieindeksowanej kolumnie).
- Doraźna decyzja: Poprawa mechanizmu pobierania listy wartości do filtrów (cały zbiór z DISTINCT).
- Docelowa propozycja: Wdrożenie mechanizmu indeksowania pól dla filtrowania/podpowiadania.

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Bug #Zadanie #Weryfikacja

- Problem z funkcją "zaznacz wszystko" w module raportowym (nie zaznacza wszystkich elementów).
- Zadanie dla Anny Skupińskiej (sprawdzenie generowania listy).

---

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Problem z filtrem użytkownika w nowych raportach – "Zaznacz wszystko" nie zaznacza wszystkiego z powodu paginacji.
- Rozwiązanie: Przycisk "Zaznacz wszystko" pojawia się tylko po wprowadzeniu wartości powodującej przeszukanie; walidacja przy zastosowaniu filtru.

---
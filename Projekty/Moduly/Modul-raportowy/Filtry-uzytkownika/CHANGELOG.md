# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-02 | Rada developerów
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-12-02 Rada developerów.md]
**Kategoria:** #Problem

- **Issue #22411 (LPP):** Problem z zachowaniem filtrów lewych (drzewko) po akcjach masowych - sprawy znikają, użytkownik traci kontekst
- **Propozycja cząstkowa:** Przeniesienie zaznaczenia do najbliższego rodzica gdy pozycja znika z drzewka (status: odroczona)
- **Edge case:** Kombinacja filtra drzewkowego + filtr górny - co gdy w połączeniu nie ma nic do pokazania? (wymaga przygotowania przypadku testowego)
- **Bug "Wyczyść wszystkie":** Dla pustego filtru (domyślnie "nie zawiera" bez wartości) powoduje zniknięcie rekordów - niepożądany skutek do naprawy
- **Kolejność implementacji:** 1) Naprawić filtr lewy (drzewko), 2) Rozwiązać edge case drzewko+górny, 3) Dołożyć popup dla akcji masowych
- **Zadanie:** Damian Kaminski dopisze acceptance criteria do #22411

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Design

- Szymek/Przemek porządkują operatory daty w filtrach użytkownika, uspójniając logikę ("ostatnie 7 dni" vs "tydzień temu").

---

## 2025-11-06 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-06 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Dodanie DISTINCT do zapytań filtrów (eliminacja duplikatów w liście wartości)
- Rozbicie tematu na feature z osobnymi PBI dla dalszych usprawnień
- Dalsze tematy do omówienia: limit parametrów IN(...), przycisk "Załaduj więcej", logika "Zaznacz wszystko"
- Refaktoryzacja: poprawianie filtrów nie może psuć legendy i na odwrót

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
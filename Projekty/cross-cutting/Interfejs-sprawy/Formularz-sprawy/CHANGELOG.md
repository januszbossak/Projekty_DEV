# CHANGELOG - Formularz sprawy

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Bug #Design #UX

- Naprawione bugi UI i poprawiony wygląd pól tabeli.
- Poprawa wyglądu menu przy polach (odnośnik, dokument).
- Ujednolicenie kolorów menu (usunięcie niespójności).
- Poprawa wyglądu pola tabela z zagnieżdżeniami.
- Naprawienie niespójności w wyświetlaniu kompaktowym.
- Weryfikacja mobilnego interfejsu (opcjonalnie).

---

## 2025-11-27 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-27%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Decyzja #Zadanie

- **Tryb Wizard (MVP):** Zatwierdzono koncepcję krokowego wypełniania formularza (sekcja po sekcji) z przyciskami "Następna/Poprzednia sekcja" dla mobile i desktop.
- **Działanie:** Kliknięcie "Następna" zapisuje stan i otwiera kolejną sekcję (na mobile accordion).
- **Plan MVP2:** Zdarzenie "zmiana sekcji" dla walidacji reguł automatycznych per krok.
- **Zadanie:** Damian Kamiński przygotuje mockup i wycenę dla klienta LPP.

## 2025-11-27 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-27 Planowanie sprintu.md]
**Kategoria:** #UX #PoprawaBłędów #Design

- Cel: Poprawa spójności wizualnej i użyteczności formularza sprawy, w odpowiedzi na zgłoszenia użytkowników dotyczące porozjeżdżanych elementów.
- Zakres prac: Usprawnienie UX tabel (problem scroll vs. przycisk "plus"), kompleksowy przegląd i wyrównanie wyglądu całego formularza, ujednolicenie kolorów, selektów i podświetleń.
- Konkretne zmiany: Nowe zachowanie scrollbara przy hover (jak w Teams), zmiana dodawania wiersza na jednoetapowe.
- Problemy wizualne: Niespójności w kolorach czerni, selektywnie stosowane podświetlenia pól.
- Decyzje: Zamknięcie tematu wyglądu sprawy w bieżącym sprincie.

---

## 2025-11-25 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-25 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-25%20Rada%20architektów.md)
**Kategoria:** #Błędy #UI

- **Pole Podpis:** Potwierdzono problem z nierównym wyświetlaniem pola "podpis" (obwódka, skalowanie) przy ustawieniu "Mały rozmiar formularza" w profilu użytkownika.

---

## 2025-11-12 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-12 Spotkanie projektowe - Przegląd wycen.md]
**Kategoria:** #Bug #Zadanie

- Komunikat z `setFieldInfo` nie wyświetla się dla wymaganych pól w wersji czerwcowej.
- Wcześniej działało poprawnie (wersja marcowa).
- Do weryfikacji, kto opiekował się ukrywaniem "pole jest wymagane".
- Nie jest to hotfix.

---

## 2025-10-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-21 Rada architektów.md]
**Kategoria:** #Design #Problem

- Wyświetlanie tabeli jako formularz po zmianach działa niepoprawnie (wymaga weryfikacji implementacji).
- Alternatywy: Szybki powrót do starego wyglądu vs kompleksowe przepisanie (10-15h+).
- Decyzja: Odroczone do weryfikacji przez Piotra Buczkowskiego (preferencja Mariusza: wyświetlanie na tabeli).

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Bug #Design #Decyzja

- Problem z wyświetlaniem zagnieżdżonych tabel w trybie formularzowym w nowej wersji formularza sprawy (błąd krytyczny)
- Decyzja: Proof of concept (1 dzień) w celu sprawdzenia możliwości przywrócenia działania jak w wersji marcowej

---

## 2025-10-06 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Problem #Design

- Poprawa logiki wyszukiwania dla pól słownikowych podrzędnych w formularzu
- Dyskusja nad ścisłą walidacją pola "numer telefonu" (obecnie akceptuje znaki nienumeryczne)
- Propozycja ograniczenia listy użytkowników w polach systemowych formularza (Współpracownicy, Obserwatorzy)

---

## 2025-09-25 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-25%20Rada%20architektów.md)
**Kategoria:** #Design #Funkcjonalność

- **Przełączanie sekcji:** Propozycja dodania strzałek "Następna"/"Poprzednia" na dole formularza do nawigacji między zakładkami, by usprawnić proces wypełniania długich formularzy. Nie zmniejsza przestrzeni roboczej (nie zamraża belki zakładek).

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Design #Funkcjonalność

**Kolory i gradienty w formularzu** ⏸️
- **Zaimplementowano:** Podstawowe gradienty dla kolorów tła
- **Status:** ⏸️ Temat wstrzymany (inne priorytety)
- **Ograniczenia:** Brak gradientów dla tablic

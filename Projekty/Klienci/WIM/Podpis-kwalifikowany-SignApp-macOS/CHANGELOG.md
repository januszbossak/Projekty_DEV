# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Problem #Ryzyko #Decyzja

- Aplikacja SignApp (macOS) gotowa (UI poprawione), ale niecertyfikowana.
- Przekazanie niecertyfikowanej wersji do testów IT (z akceptacją obejścia zabezpieczeń instalacji).
- Ryzyko: Nieobecność Adriana może spowolnić prace/wsparcie.

---

## 2025-11-19 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Notatka projektowa - Przegląd wycen.md]
**Kategoria:** #Design #Funkcjonalność

- Domyślnie wyświetlane są tylko aktywne certyfikaty służące do podpisu.
- Opcja "Pokaż wszystkie certyfikaty" zostanie umieszczona na dole ekranu (w stylu trybu deweloperskiego).
- Komunikaty błędów mają być wzorowane na module raportowym (opis sytuacji + instrukcja).
- Wyróżnianie certyfikatów z krótką datą ważności to temat do rozwoju w przyszłości.

---

## 2025-11-07 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-07 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Decyzja

- Klient WIM wymaga obsługi podpisywania przez Szafira na macOS.
- Adrian jest odpowiedzialny za implementację, już ogarnął temat.
- Klient odrzucił tańszą alternatywę (SimpleSign) pomimo dostępności i funkcjonalności.
- Decyzja klienta wynika z preferencji dyrektora korzystającego z Maca i Szafira.

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #Platforma

- SignApp dla macOS w testach z Szafirem; brak fizycznego mSzafira u dewelopera – decyzja o zakupie, by przyspieszyć testy.
- Wytyczne UX dostarczone; aplikacja budowana w MAUI.NET (następca Xamarina); prace nad nowym UI trwają.

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Zadanie #Ryzyko

- Kamil prowadzi prace nad SignApp na macOS, z Maciem i Szafirem do testów.
- Niezależnie od certyfikacji, rozwiązanie powinno być przekazane klientowi do sprawdzenia.
- Adrian również ma prace związane z SignApp.
- Ryzyko przeładowania Adriana.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność #Problem

- Prace nad aplikacją do podpisywania na macOS
- Problem z testowaniem: aplikacja wymaga Maca, który jest dostępny tylko u jednej osoby (Adrian)
- Konieczność zakupu SimplySign do testów przez dewelopera

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Bug #Design

- Automatyczne wykrywanie bibliotek do podpisywania na Macu (SignApp Mac)
- Wybór certyfikatu i miejsca podpisu, obsługa wielu bibliotek i kluczy prywatnych
- Zidentyfikowano błędy: wyświetlanie certyfikatów (Subject zamiast Common Name), brak rozróżnienia certyfikatów, brak pola wyboru, logo za duże, niespójność z SignApp Windows

---

# CHANGELOG - Historia sprawy

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Funkcjonalność #Design #Decyzja

**Historia spraw – wyświetlanie nazw pól w języku użytkownika** ✅

Zmiana wyświetlania historii spraw - zamiast nazw technicznych wyświetlane będą nazwy wyświetlane (DisplayValue) w języku użytkownika. Tooltip z nazwą techniczną, gdy różni się od wyświetlanej.

**Szczegóły:**
- Wyświetlanie: DisplayValue w języku użytkownika
- Mechanizm: pobieranie DisplayValue z pola (wersja językowa lub domyślna)
- Tooltip: nazwa techniczna (tylko gdy różni się od wyświetlanej)
- Implementacja: zmiana w kontrolerze, tooltip przez Bootstrap (atrybut `title`)
- Wartości słowników: już poprawione wcześniej
- Szacowany czas: ~1 godzina

**Kontekst:**
- Nazwy techniczne utrudniają interpretację historii przez użytkowników
- Wartości słowników już wyświetlają się poprawnie
- Rozważano zapisanie ID pola (większe wyzwanie) - odroczone
- Historia spraw to część szerszego tematu (historia sprawy/biznesowa/pól)

**Zadania:**
- Piotr Buczkowski - implementacja wyświetlania DisplayValue + tooltip
- Piotr Buczkowski - uzupełnienie acceptance criteria

**Punkty otwarte:**
- Przyszłe zapisywanie ID pola zamiast nazwy technicznej?
- Obsługa usuniętych (deaktywowanych) pól?
- Kompleksowe podejście do historii (widok zakładkowy) jako osobny projekt?

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność

**Logowanie wysyłanych maili w historii sprawy** ✅
- Wdrożono wyświetlanie wysłanych maili w historii sprawy/zdarzeniach sprawy
- Szczegóły w projekcie [Klienci/WIM/Logowanie-powiadomien](../../../../Klienci/WIM/Logowanie-powiadomien/CHANGELOG.md)

---

## 2025-09-04 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-04 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-04%20Rada%20architektów.md)
**Kategoria:** #Architektura #Funkcjonalność

**Rejestrowanie maili w CaseActivity** ℹ️
- Dodano możliwość włączenia/wyłączenia rejestrowania maili wysłanych ze sprawy w `CaseActivity`
- Opcjonalne ze względu na zajmowane miejsce

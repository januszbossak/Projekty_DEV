# CHANGELOG

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Spotkanie projektowe - Błędy formularzy i procedury aktualizacji.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-03%20Spotkanie%20projektowe%20-%20Błędy%20formularzy%20i%20procedury%20aktualizacji.md)  
**Kategoria:** #Bug #Problem

- **KRYTYCZNY HOTFIX:** Tabela wyświetlana jako formularz całkowicie rozjechana po aktualizacji do wersji czerwcowej
- **6 wykrytych błędów:** checkboxy znikły, opcja "ukryj etykietę" nie działa, nazwy pól static text się wyświetlają, tabela jednowierszowa wyświetla dodatkowy poziom, przycisk "usuń" widoczny w trybie odczytu (mobile), duplikacja kolumn z etykietami
- **Impact:** ~100 formularzy zgód i oświadczeń w obiegu (terminy 3-dniowe), kandydaci nie mogą wypełnić formularzy
- **Decyzja:** Natychmiastowe cofnięcie wersji produkcyjnej do marcowej, naprawa błędów na dev, testy przez klienta, potem aktualizacja prod
- **Zadania:** Mariusz + Damian Kamiński - naprawienie wszystkich błędów na dev, Michał Zwierzchowski - rollback produkcji
- **Procedura:** Dev → testy klienta (wszystkie ścieżki ~4-5) → aktualizacja prod (tylko po zatwierdzeniu)

---

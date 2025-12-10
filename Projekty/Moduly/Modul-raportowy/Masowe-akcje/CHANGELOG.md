# CHANGELOG - Moduł raportowy: Masowe akcje

Historia ustaleń i zmian dla projektu.

---

## 2025-12-02 | Rada developerów
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-12-02 Rada developerów.md]
**Kategoria:** #Funkcjonalność

- **Wizja długofalowa (Janusz):** Akcja masowa NIE powinna zmieniać kontekstu raportu - użytkownik widzi co się zmieniło przed odświeżeniem
- **Inline update:** Po wykonaniu akcji rekordy aktualizują się inline (zielony kolor sukcesu), zmiany w kolumnach widoczne natychmiast (data przekazania, stan)
- **Sprawy pozostają:** Nawet jeśli nowe wartości nie pasują do aktywnych filtrów, sprawy pozostają na ekranie do momentu kliknięcia "Odśwież"
- **Uspójnienie UI:** "Zamknij" (powrót z widocznymi zmianami) vs "Zamknij i odśwież" (pełne odświeżenie, znikanie spraw) - bez znaczenia czy podpisywanie z/bez akcji czy sama akcja masowa
- **Niespójność obecna:** Po podpisaniu z akcją jest popup "czy odświeżyć?", ale po samej akcji masowej nie ma - wymaga ujednolicenia
- **Ograniczenie:** Brak funkcji "Cofnij" dla akcji masowych (użytkownik musi ręcznie poprawiać błędy w pojedynczych sprawach)

---

## 2025-11-28 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Architektura

- MVP 0: Umożliwienie działania funkcji "Wykonaj przed wykonaniem reguły" w akcjach masowych z raportu (obsługa Użytkownik, Komentarz) - Kamil
- Pierwsze okno dialogowe z pierwszej sprawy zbiera dane i automatycznie przekazuje do wszystkich pozostałych
- Błędy wykonania reguły muszą być obsługiwane i wyświetlane (czerwony wiersz)
- Reguły z warunkiem "Wykonaj przed wykonaniem reguły" domyślnie ukryte w opcjach akcji masowych (chyba że oznaczone jako kompatybilne)
- Konieczność walidacji kontekstu (czy wszystkie sprawy mają ten sam kontekst dla okna dialogowego)
- MVP 1: Rozszerzenie o nowe typy pól (liczbowe, data, lista wyboru) - do wyceny
- Dyskusja o uniwersalności vs specyficzne rozwiązania

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Bug

- Rozszerzenie okna dialogowego dla akcji masowych (Execute before rule).
- Obsługa zbierania danych z dialogu dla wielu zaznaczonych spraw.
- Weryfikacja kompatybilności reguł z warunkiem wstępnym w akcjach masowych.

---

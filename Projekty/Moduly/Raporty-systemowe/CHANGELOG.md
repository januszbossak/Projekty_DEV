# CHANGELOG – Raporty-systemowe

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Projekt:** [Klienci/WIM/Raporty-systemowe](../../../Klienci/WIM/Raporty-systemowe/)
**Kategoria:** #Funkcjonalność #Zadanie

- Przygotowanie 5 raportów systemowych dla WIM.
- Zgodność z wymaganiami WIM.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność

- Prace nad dashboardami systemowymi (Performance Monitor, System Lookup Model)
- Dodanie nowych źródeł danych systemowych

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Architektura #Decyzja

- Przejście źródeł systemowych z ujemnych ID na GUID i flagę systemową (`SystemOrigin`)
- Decyzja: Przerwanie kompatybilności wstecznej dla użytkowników korzystających ze źródeł systemowych

---

## 2025-10-02 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-02 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-10-02%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Design #Decyzja

- Rozdzielenie raportów systemowych na osobne dla spraw zamkniętych (z CaseDefinition) i w toku (z CaseHistory)
- Decyzja o ograniczeniu użycia Tree Map do 3-4 wartości, przy większej liczbie użycie wykresu słupkowego
- Link "Raporty systemowe" w menu modułów systemowych będzie wymuszał widok kafelkowy
- Wprowadzenie opisów biznesowych raportów dostępnych pod ikoną "i" w interfejsie
- Wymagana poprawa kontrastu kolorów (szary tekst na szarym tle) i ujednolicenie tooltipów

---

## 2025-09-25 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-25%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Statystyki procesu:** Zostanie stworzony raport systemowy pokazujący statystyki procesu (ilość spraw, data ostatniej sprawy, data ostatniego uruchomienia). Raport będzie dostępny w kontekście ustawień procesu.

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🏗️ Architektura

- **Nowe podejście zakładkowe:** dashboardy dla poszczególnych grup raportów systemowych.
- **Optymalizacja źródeł danych:** część źródeł przełączona na tryb **local** (agregaty w zapytaniu, przeliczane raz na dobę/w nocy).
- **Wymagane filtry:** możliwość ustawienia domyślnej wartości filtra (np. "poprzednie 7 dni") jako wymaganej – raport nie pobiera danych bez wskazania ograniczenia.
- **Feedback:** podejście odwraca logikę (najpierw filtr → potem dane) co rozwiązuje problemy wydajnościowe przy dużych wolumenach (nie wpływa na retencję, tylko prezentację).

---

## 2025-08-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-21 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-21%20Rada%20architektów.md)

**Kategoria:** #Funkcjonalność

**Hotfix i funkcjonalność kopiowania raportów systemowych** ✅
- **Problem:** Brak możliwości dodawania do dashboardów, kopiowanie przenosi flagę "systemowy" (uniemożliwia edycję), możliwość edycji przez nieuprawnionych
- ✅ **Zatwierdzone:**
  1. **Hotfix – dodawanie do dashboardów:** Po skopiowaniu na dashboard raport traci status "systemowy" (`rep_lock` = 0)
  2. **Edycja raportów systemowych:** Grupa uprawnień "System Report Managers" - administratorzy mogą edytować
  3. **Funkcja "Zapisz jako":** Nie kopiować flagi "systemowy", pełne przeładowanie widoku, kopiowanie folderów/kategorii
- **Szczegóły techniczne:**
  - Flaga: `rep_lock` (0 = nie zablokowany, null/1 = systemowy)
  - Grupa: "System Report Managers" (nazwa dokładnie taka)
  - Świadomość: raporty systemowe nadpisywane przy aktualizacji
- **Punkty otwarte:** Czy "Zapisz jako" kopiować wszystkie właściwości? Jak dokładnie przeładowanie widoku?
- **Zadania:** Anna Skupińska - hotfix, usunięcie błędu edycji, poprawka "Zapisz jako"; Damian Kamiński - artykuł instruktażowy

**Kategoria:** #Design

**Prezentacja raportów systemowych na liście głównej** 🔍
- **Problem:** Mieszanie raportów systemowych ze zwykłymi nieczytelne, mechanizm folderów niewystarczający
- 💡 **Propozycja:** Nowa sekcja "Raporty systemowe" (jak "Ulubione")
  - Grupowanie na podstawie flagi (nie folderów)
  - Filtry "moje", "udostępnione dla mnie" (zgodnie z wymaganiami Przemka)
- **Status:** 🔍 Do weryfikacji - wymaga konsultacji z Przemkiem
- **Punkty otwarte:** Sekcja vs filtry vs zakładki? Jak dokładnie filtry "moje"/"udostępnione"?
- **Zadania:** Damian/Kamil - konsultacja z Przemkiem; Łukasz - wstrzymanie zadania w backlogu

---


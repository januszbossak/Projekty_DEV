# CHANGELOG – Raporty-systemowe

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


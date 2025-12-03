# Historia zmian - Moduł raportowy

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Kolory w raportach tabelarycznych z agregacją** ✅
- **Problem:** Mechanizm kolorowania patrzy tylko na wartości z danej strony, nie wszystkie wartości (nieprawidłowy gradient)
- ❌ Odrzucone: Kolorowanie tylko wartości z aktualnej strony - nieprawidłowe działanie gradientu
- ✅ **Zatwierdzone:**
  1. **Pobieranie wszystkich wartości** - mechanizm pobiera wszystkie wartości z raportu przed kolorowaniem
  2. **Gradient min/max** - kolorowanie oparte na maksymalnej/minimalnej wartości + wartość zero
  3. **Zakres:** Tylko raporty tabelaryczne bez agregacji (głównie pod WIM/Piotr)
  4. **Typy raportów:** Pivot, mapa (na razie)
- ⏸️ Przyszłościowo: Dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient)
- **Punkty otwarte:** Mechanizm dzielenia zakresów? Rozszerzenie na inne typy raportów?
- **Zadania:** Anna Skupińska - finalizacja (oddane do testowania na AMODIT Local), Janusz Bossak - testowanie

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Rozbudowa Pivota:** Dodanie edycji kolorów w gradientach (użytkownik wybiera kolor dla min/max w kolorowaniu warunkowym)
- **Heatmapa:** Dodanie nowego typu wykresu (bazując na bibliotece AmCharts)
- **Status:** ✅ Zatwierdzone - realizacja obu tematów

---

## 2025-12-02 | ⚠️ Problem | Spotkanie projektowe - Design
**Źródło:** [Notatki/Spotkania projektowe/2025-12-02 Spotkanie projektowe - Design.md]

**Edge case: edycja wierszy tabel w raportach (zgłoszenie PKF)**

PKF zgłosił potrzebę edycji wierszy tabel z poziomu raportu osadzonego na sprawie. Obecny system nie obsługuje edycji danych w raportach – tylko wyświetlanie.

**Problem:**
- Raport wyświetla wiersze z tabel z różnych spraw (np. rejestracja czasu pracy z kilku dni)
- Użytkownik chce zbiorczo edytować te wiersze (korekta godzin, zmiana projektów)
- Brak możliwości edycji danych bezpośrednio z raportu

**Rozważane rozwiązania:**
1. Uproszczone okienka modalne do edycji wiersza tabeli
   - Formularz wiersza istnieje (czasami wyświetla się przy błędach)
   - Teoretycznie możliwe, ale szeroki temat
   - Problem: reguły, zależności, walidacje – jak to obsłużyć w kontekście edycji z raportu?

2. Edycja w trybie Excelowym (inline editing)
   - Edycja wierszy bezpośrednio w raporcie (jak w Excelu)
   - Trudne dla reguł i zależności między polami

3. Edycja przez Excel (Get Excel Data / Set Excel Data)
   - Eksport do Excela, edycja, import z powrotem
   - Problem: nie ma funkcji Set Excel Data
   - Gimnastyka dla użytkownika

**Status:** ⏸️ Odroczone – temat do dyskusji na Radzie Architektów

**Uzasadnienie:**
- Temat bardzo szeroki, wymaga przemyślenia wielu aspektów
- Nie ma obecnie sensownego pomysłu na implementację
- Dla PKF znaleziono obejścia (gimnastyka, ale działa)

**Szczegóły techniczne:**
- Funkcja Get Excel Data istnieje, Set Excel Data NIE istnieje
- Formularz wiersza tabeli istnieje (można go teoretycznie wykorzystać)

**Punkty otwarte:**
- Temat do dyskusji na Radzie Architektów lub osobnym spotkaniu Design
- Nie do realizacji w ciągu kilku dni – wymaga głębszej analizy i koncepcji
- Jak obsłużyć reguły, walidacje i zależności między polami w kontekście edycji z raportu?

**Powiązane projekty:**
- [Klienci/PKF/Rejestracja-czasu-pracy](../../Klienci/PKF/Rejestracja-czasu-pracy/CHANGELOG.md) - konkretny use case PKF

---

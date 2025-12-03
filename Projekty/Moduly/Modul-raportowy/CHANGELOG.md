# Historia zmian - Moduł raportowy

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

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #Administracja

**Kopiowanie i zapisywanie raportów systemowych jako własne** ✅
- **Problem:** Administratorzy musieli prosić o zmiany w raportach systemowych
- **Rozwiązanie:**
  - Możliwość skopiowania raportu systemowego ("zapisz jako") i edycji jako własny
  - Wymaga stworzenia specjalnej grupy użytkowników
  - Możliwość definiowania filtrów wymaganych (bez wartości domyślnej)
- **Ograniczenia:** Źródła systemowe pozostają w trybie "tylko do odczytu" (nie można zmieniać zapytań SQL)

---

## 2025-08-28 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-28 Rada architektów|2025-08-28 Rada architektów]]

**Kategoria:** #Funkcjonalność #Problem

### Tabelki edytowalne – pivot/Excel w raportach

**Kontekst:**
Pojawiły się wymagania dotyczące tabel z możliwością edycji w raportach. Problem dotyczy zarówno PKF (Timesheet - rejestracja czasu pracy) jak i WIM (pozycje zamówienia z checkboxami).

**Zidentyfikowane Ryzyka:**
- Wydajność przy dużych tabelkach (300+ wierszy)
- Obciążenie formularza sprawy przy dużych tabelkach
- Ryzyko utraty kontekstu przy stronicowaniu
- Różne podejścia do podobnych problemów mogą prowadzić do niespójności

**Rozważane alternatywy:**
- **Tabelka AMODITowa na sprawie** - obciąża CaseDefinition, problemy wydajnościowe (odrzucona)
- **Raport tabelaryczny osadzony** - wymaga rozbudowy mechanizmu edycji (odroczona dla PKF)
- **Raport tabelaryczny z checkboxami (WIM)** - wymaga rozbudowy o edycję checkboxów (wybrana)
- **GetExcelData + Excel zewnętrzny** - rozwiązanie jednostkowe, nie systemowe (odroczona)
- **Dashboard z raportem + podglądem sprawy** - propozycja do rozważenia

**Decyzja:** 🔍 Do weryfikacji / ⏸️ Odroczone

**Dla WIM:**
- Użycie raportu tabelarycznego osadzonego ze źródła zewnętrznego
- Rozbudowa mechanizmu raportów o możliwość edycji checkboxów w źródłach zewnętrznych
- Zwiększenie limitu wierszy dla źródeł zewnętrznych (obecnie 100, może być potrzeba 300+)

**Dla PKF:**
- Temat wymaga wyceny i dalszej analizy
- Można powołać się na wcześniejszą analizę, gdzie przedstawiono obecne rozwiązanie (rejestracja przez sprawy)

**Szczegóły techniczne:**
- Raporty osadzone ze źródła zewnętrznego obecnie nie obsługują edycji checkboxów – wymaga rozbudowy
- Stronicowanie w raportach może powodować problemy z kontekstem
- Duże tabelki na formularzu sprawy obciążają zarówno przeglądarkę, jak i serwer

**Zadania:**
- **Damian Kaminski:** PA dla rozbudowy raportów o edycję checkboxów
- **Kamil Dubaniowski:** Weryfikacja wydajności ładowania 300 pozycji z procedury składowanej

**Punkty otwarte:**
- Czy zwiększyć limit wierszy w raportach ze źródeł zewnętrznych powyżej 100?
- Czy dashboard powinien mieć mechanizm podglądu sprawy obok raportu?

**Powiązane projekty:**
- [[../../Klienci/PKF/Rejestracja-czasu-pracy/CHANGELOG|PKF/Rejestracja-czasu-pracy]] - PKF Timesheet
- [[../../Klienci/WIM/Faktury-edytowalne-tabele/CHANGELOG|WIM/Faktury-edytowalne-tabele]] - WIM pozycje zamówienia

---

### Paleta kolorów w raportach

**Kontekst:**
Obecnie system ma 20 kolorów w pierwszej serii palety kolorów dla raportów. Damian zaproponował zmianę kolejności kolorów, aby pierwsze 10 było bardziej różniących się od siebie (podobnie jak w Tableau). Problem polega na tym, że niektóre kolory są zbyt podobne do siebie (np. cyjan, niebieski, indygo, morski), co utrudnia rozróżnienie na wykresach.

**Zidentyfikowane Ryzyka:**
- Nieczytelność wykresów przy podobnych kolorach
- Problemy z dostępnością dla osób z zaburzeniami widzenia kolorów
- Brak możliwości automatycznego przypisania unikalnych kolorów dla więcej niż 20 serii
- Ryzyko tworzenia nieczytelnych wykresów przez konsultantów (pokazywanie zbyt wielu serii)

**Rozważane alternatywy:**
- **Ograniczenie do 10 kolorów (jak Tableau)** - wymaga konsultacji z Michałem Maliszewskim (odroczona)
- **20 kolorów z lepszą kolejnością** - zmiana kolejności, aby pierwsze 10 było bardziej różniących się (propozycja)
- **20+ kolorów z automatycznym przypisaniem** - propozycja Damiana (do rozważenia)
- **Funkcjonalność "pozostałe"** - agregacja mało istotnych serii (poniżej progu, np. 5%) do jednej pozycji "pozostałe" (propozycja Janusza)
- **Sortowanie po wartościach w legendzie** - częściowo wdrożone (wymaga weryfikacji)

**Decyzja:** 🔍 Do weryfikacji

Damian porozmawia z Michałem Maliszewskim o dobrych praktykach dotyczących palet kolorów w raportach (wzorce z Tableau, Adobe, dostępność dla osób z zaburzeniami widzenia kolorów). Decyzja o ostatecznej palecie zostanie podjęta po konsultacji.

**Szczegóły techniczne:**
- Obecnie: 20 kolorów w pierwszej serii, możliwość ręcznego definiowania dodatkowych
- Propozycja Damiana: zmiana kolejności (czerwony, zielony, niebieski jako pierwsze 3), potem turkusowe
- Tableau: domyślnie 10 kolorów w pierwszej serii
- Uwaga: palety kolorów są naukowo dobierane pod kątem kontrastu i dostępności dla osób z zaburzeniami widzenia kolorów

**Zadania:**
- **Damian Kaminski:** Konsultacja z Michałem Maliszewskim dotycząca dobrych praktyk palet kolorów
- **Anna Skupinska:** Wstrzymanie prac nad kolorami do czasu podjęcia decyzji

**Punkty otwarte:**
- Czy ograniczyć paletę do 10 kolorów czy pozostawić 20?
- Jak obsłużyć przypadek, gdy użytkownik świadomie chce wyświetlić więcej niż 10-20 serii?
- Czy wprowadzić funkcjonalność agregacji mało istotnych serii do "pozostałe"?
- Jak zapewnić dostępność dla osób z zaburzeniami widzenia kolorów?
- Czy sortowanie w legendzie powinno być domyślnie po wartościach zamiast alfabetycznie?

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność

**Kontekst:**
Seria usprawnień w module raportowym przepisanym na nową technologię, w tym gradienty kolorów, filtry wymagane i domyślne, oraz usprawnienia podpisywania z poziomu raportów.

### Moduł raportowy w nowej technologii – nowinki

**1. Gradienty kolorów:**
- W raportach typu pivot można ustawić kolory dla wartości (np. najwyższe zielone, najniższe czerwone)

**2. Filtry wymagane:**
- Użytkownik nie zobaczy raportu, dopóki nie wybierze wartości w filtrze (np. konkretnego procesu)
- Zapobiega to szumowi informacyjnemu (wyświetlaniu danych ze wszystkich procesów naraz)

**3. Filtry z wartością domyślną:**
- Twórca ustawia np. bieżący rok, ale użytkownik może to zmienić

**4. Filtr zakresu dat:**
- Możliwość ustawienia przedziału "od-do" w ramach jednego filtru (wcześniej trzeba było robić dwa osobne)

**5. Przycisk "Wyczyść filtr użytkownika":**
- Resetuje ustawienia filtrów

**6. Przycisk "Zastosuj":**
- Wprowadzony we wszystkich typach filtrów (bardziej intuicyjne dla użytkowników)

### Usprawnienie podpisywania z poziomu raportów

- Jeśli na formularzu jest kilka pól z dokumentami, a na raporcie wyświetlamy je w kolumnach, teraz możemy wskazać, która konkretnie kolumna ma podlegać podpisywaniu (żeby nie podpisywać wszystkich załączników ze sprawy naraz)

### Szczegóły techniczne

- Moduł raportowy przepisany na nową technologię
- Filtry wymagane i domyślne
- Filtr zakresu dat (od-do w jednym filtrze)

---

## 2025-08-25 - Sprint review

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność

**Edycja gradientów w raportach**

Implementacja edycji gradientów kolorów w raportach Treemap i Pivot. Użytkownicy mogą definiować własne skale kolorystyczne, resetować do domyślnej palety oraz dostosowywać kolory dla wartości dodatnich, ujemnych i środkowych.

**Kontekst:** Główna implementacja dla klienta WIM - zobacz szczegóły: [[../../Klienci/WIM/Raporty-edycja-gradientow/CHANGELOG|WIM/Raporty-edycja-gradientow]]

---

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

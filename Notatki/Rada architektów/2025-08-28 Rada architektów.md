# Rada Architektów – 2025-08-28

**Powiązane projekty:**
- `cross-cutting/Logowanie-delete-case` – temat 1
- `moduly/Modul-raportowy` – tematy 2, 3
- `klienci/PKF` – temat 2
- `klienci/WIM` – temat 2

---

## 1. Rejestrowanie operacji DeleteCase

**Projekt:** `cross-cutting/Logowanie-delete-case`

### Kontekst i Problem

Klienci (w tym Gavana) wymagają permanentnego rejestrowania informacji o tym, kto i kiedy usunął sprawę za pomocą funkcji DeleteCase. Obecnie operacja ta jest logowana tylko w logach systemowych, które są okresowo czyszczone, przez co nie ma trwałego śladu audytowego. Problem pojawia się gdy sprawa zostaje usunięta (np. z powodu wymogu usunięcia danych osobowych), a później ktoś inny próbuje do niej dotrzeć – nie ma informacji kto, kiedy i dlaczego sprawa została usunięta.

### Zidentyfikowane Ryzyka

- Brak śladu audytowego dla operacji usuwania spraw
- Niemożność wyjaśnienia klientom, kto i kiedy usunął sprawę
- Brak możliwości weryfikacji przyczyny usunięcia sprawy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| UserActivity w zakładce "Aktywność administracyjna" | Logowanie DeleteCase w istniejącej zakładce aktywności administracyjnej | ❌ Odrzucona – aktywność administracyjna dotyczy zarządzania kontami i uprawnieniami, nie operacji na sprawach |
| CaseEvent (historia biznesowa sprawy) | Logowanie w historii zdarzeń na sprawie | ❌ Odrzucona – sprawa jest usuwana razem z historią, więc wpis również zniknie |
| CaseActivity | Logowanie w aktywności sprawy | ❌ Odrzucona – CaseActivity jest czyszczone przy usuwaniu sprawy |
| Nowa zakładka w UserActivity | Utworzenie dedykowanej zakładki dla operacji usuwania spraw | ✅ Wybrana – oddzielna kategoria dla operacji na sprawach, nie mieszana z administracyjnymi |
| Raport dedykowany | Osobny raport dostępny tylko dla administratorów | ⏸️ Odroczona – może być rozważona w przyszłości, ale na razie wystarczy zakładka w UserActivity |

### Decyzja

**Status:** ✅ Zatwierdzone

Utworzenie nowej zakładki w UserActivity o nazwie "Usunięte Sprawy" (ewentualnie "Usuwanie Spraw") do rejestrowania operacji DeleteCase. Zakładka będzie również wykorzystywana do innych podobnych operacji w przyszłości, jeśli zajdzie taka potrzeba.

**Szczegóły techniczne:**
- Logowanie w UserActivity Log (widoczne w logach systemowych)
- Rejestrowane informacje:
  - CaseID (numer sprawy)
  - Nazwa procesu (z którego pochodziła sprawa)
  - Data i czas operacji
  - Użytkownik, który wykonał operację
  - Ewentualnie komentarz/uzasadnienie (opcjonalnie)
- Operacja DeleteCase wywoływana z reguły funkcji również będzie logowana w ten sam sposób
- Usunięcie sprawy z poziomu kosza (przez administratora) również będzie logowane w ten sam sposób

**Uwaga:** Rozważano wyświetlanie modala z komentarzem przy usuwaniu, ale uznano to za zbyt utrudniające proces. Na razie rejestrowane będzie minimum: kto, kiedy, CaseID i nazwa procesu.

### Zadania

- **[Piotr Buczkowski]:** Implementacja logowania DeleteCase w UserActivity Log → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Utworzenie nowej zakładki "Usunięte Sprawy" w UserActivity → termin: [do ustalenia]
- **[Łukasz Bott]:** Przygotowanie propozycji projektu na designie → termin: jutro (2025-08-29)

### Punkty otwarte

- Czy w przyszłości będą inne operacje wymagające logowania w tej zakładce?
- Czy komentarz/uzasadnienie powinno być obowiązkowe czy opcjonalne?

---

## 2. Tabelki edytowalne – pivot/Excel w raportach

**Projekt:** `moduly/Modul-raportowy`, `klienci/PKF`, `klienci/WIM`

### Kontekst i Problem

Pojawiły się dwa podobne wymagania dotyczące tabel z możliwością edycji:

1. **PKF (Timesheet):** Klient chce mieć widok typu pivot/Excel do rejestracji czasu pracy, gdzie w wierszach są zadania/zlecenia, a w kolumnach dni tygodnia (poniedziałek–niedziela). Użytkownik chce wypełniać macierz godzin bezpośrednio w tabelce, zamiast wchodzić do każdej sprawy osobno (co jest obecnie "dużą klikologią").

2. **WIM (pozycje zamówienia):** Klient chce mieć tabelkę z pozycjami zamówienia (do 300 wierszy) zaciągniętymi z innego systemu, gdzie użytkownik zaznacza checkboxami, które pozycje są zgodne z fakturą. Po zaznaczeniu przyciskiem ma się wygenerować opis niezgodności dla pozycji niezaznaczonych.

### Zidentyfikowane Ryzyka

- Wydajność przy dużych tabelkach (300+ wierszy)
- Obciążenie formularza sprawy przy dużych tabelkach
- Ryzyko utraty kontekstu przy stronicowaniu (jeśli zastosowane)
- Różne podejścia do podobnych problemów mogą prowadzić do niespójności

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Tabelka AMODITowa na sprawie | Standardowa tabelka z możliwością edycji | ❌ Odrzucona – obciąża CaseDefinition, problemy wydajnościowe przy dużych tabelkach |
| Raport tabelaryczny osadzony | Raport z możliwością edycji komórek | ⏸️ Odroczona dla PKF – wymaga rozbudowy mechanizmu edycji w raportach osadzonych |
| Raport tabelaryczny z checkboxami (WIM) | Raport osadzony z możliwością zaznaczania checkboxów | ✅ Wybrana dla WIM – rozwiązanie systemowe, wymaga rozbudowy o edycję checkboxów w raportach ze źródła zewnętrznego |
| GetExcelData + Excel zewnętrzny | Eksport danych do Excel, edycja zewnętrzna, import | ⏸️ Odroczona – rozwiązanie jednostkowe, nie systemowe |
| Dashboard z raportem + podglądem sprawy | Raport tabelaryczny z możliwością kliknięcia w wiersz i wyświetlenia sprawy po prawej stronie | 💡 Propozycja do rozważenia – wymaga rozbudowy dashboardu o mechanizm podglądu sprawy obok raportu |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Odroczone

**Dla WIM:**
- Użycie raportu tabelarycznego osadzonego ze źródła zewnętrznego
- Rozbudowa mechanizmu raportów o możliwość edycji checkboxów w źródłach zewnętrznych
- Zwiększenie limitu wierszy dla źródeł zewnętrznych (obecnie 100, może być potrzeba 300+)
- Rozważenie opcji odwrotnej logiki: zaznaczanie tylko pozycji niezgodnych (mniej klikania) zamiast zgodnych

**Dla PKF:**
- Temat wymaga wyceny i dalszej analizy
- Można powołać się na wcześniejszą analizę, gdzie przedstawiono obecne rozwiązanie (rejestracja przez sprawy) i zostało zaakceptowane przez klienta
- Jeśli klient będzie nalegał, można rozważyć rozwiązanie z GetExcelData lub rozbudowę dashboardu

**Szczegóły techniczne:**
- Raporty osadzone ze źródła zewnętrznego obecnie nie obsługują edycji checkboxów – wymaga rozbudowy
- Stronicowanie w raportach może powodować problemy z kontekstem (pierwsza strona nieaktywna po przejściu na drugą)
- Duże tabelki na formularzu sprawy obciążają zarówno przeglądarkę, jak i serwer (operacje typu foreach, sumy)

### Zadania

- **[Damian Kaminski]:** Weryfikacja wymagań z WIM dotyczących logiki zaznaczania (zgodne vs niezgodne) → termin: [do ustalenia]
- **[Damian Kaminski]:** Przygotowanie PA (Product Analysis) dla rozbudowy raportów o edycję checkboxów → termin: [do ustalenia]
- **[Damian Kaminski]:** Weryfikacja nagrań z analizy PKF dotyczących Timesheetu → termin: [do ustalenia]
- **[Kamil Dubaniowski]:** Weryfikacja wydajności ładowania 300 pozycji z procedury składowanej (oczekiwany czas: max 5 sekund) → termin: [do ustalenia]
- **[Kamil Dubaniowski]:** Weryfikacja czy kwota z faktury będzie odczytywana z OCR-a czy z innego źródła → termin: [do ustalenia]

### Punkty otwarte

- Czy zwiększyć limit wierszy w raportach ze źródeł zewnętrznych powyżej 100?
- Jak obsłużyć przypadek, gdy OCR nie odczyta numeru zamówienia lub odczyta błędnie?
- Czy dashboard powinien mieć mechanizm podglądu sprawy obok raportu?
- Czy dla dużych tabel lepiej wyświetlać je w osobnym oknie zamiast na formularzu sprawy?

---

## 3. Paleta kolorów w raportach

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Obecnie system ma 20 kolorów w pierwszej serii palety kolorów dla raportów. Damian zaproponował zmianę kolejności kolorów, aby pierwsze 10 było bardziej różniących się od siebie (podobnie jak w Tableau). Problem polega na tym, że niektóre kolory są zbyt podobne do siebie (np. cyjan, niebieski, indygo, morski), co utrudnia rozróżnienie na wykresach. Dodatkowo, gdy jest więcej niż 20 serii danych, kolory się powtarzają, co powoduje problemy z czytelnością legendy.

### Zidentyfikowane Ryzyka

- Nieczytelność wykresów przy podobnych kolorach
- Problemy z dostępnością dla osób z zaburzeniami widzenia kolorów
- Brak możliwości automatycznego przypisania unikalnych kolorów dla więcej niż 20 serii
- Ryzyko tworzenia nieczytelnych wykresów przez konsultantów (pokazywanie zbyt wielu serii)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ograniczenie do 10 kolorów (jak Tableau) | Zmniejszenie palety do 10 kolorów różniących się od siebie | ⏸️ Odroczona – wymaga konsultacji z Michałem Maliszewskim o dobrych praktykach |
| 20 kolorów z lepszą kolejnością | Zmiana kolejności, aby pierwsze 10 było bardziej różniących się | 💡 Propozycja – do weryfikacji z Michałem |
| 20+ kolorów z automatycznym przypisaniem | Automatyczne przypisanie unikalnych kolorów dla każdej serii | 💡 Propozycja Damiana – wymaga rozważenia |
| Funkcjonalność "pozostałe" | Agregacja mało istotnych serii (poniżej progu, np. 5%) do jednej pozycji "pozostałe" | 💡 Propozycja Janusza – do rozważenia jako sposób na ograniczenie liczby kolorów |
| Sortowanie po wartościach w legendzie | Sortowanie serii w legendzie według wartości, nie alfabetycznie | ✅ Częściowo wdrożone – wymaga weryfikacji czy działa poprawnie |

### Decyzja

**Status:** 🔍 Do weryfikacji

Damian porozmawia z Michałem Maliszewskim o dobrych praktykach dotyczących palet kolorów w raportach (wzorce z Tableau, Adobe, dostępność dla osób z zaburzeniami widzenia kolorów). Decyzja o ostatecznej palecie zostanie podjęta po konsultacji.

**Szczegóły techniczne:**
- Obecnie: 20 kolorów w pierwszej serii, możliwość ręcznego definiowania dodatkowych
- Propozycja Damiana: zmiana kolejności (czerwony, zielony, niebieski jako pierwsze 3), potem turkusowe
- Tableau: domyślnie 10 kolorów w pierwszej serii
- Uwaga: palety kolorów są naukowo dobierane pod kątem kontrastu i dostępności dla osób z zaburzeniami widzenia kolorów

### Zadania

- **[Damian Kaminski]:** Konsultacja z Michałem Maliszewskim dotycząca dobrych praktyk palet kolorów → termin: [do ustalenia]
- **[Anna Skupinska]:** Wstrzymanie prac nad kolorami do czasu podjęcia decyzji → termin: [do czasu decyzji]

### Punkty otwarte

- Czy ograniczyć paletę do 10 kolorów czy pozostawić 20?
- Jak obsłużyć przypadek, gdy użytkownik świadomie chce wyświetlić więcej niż 10-20 serii?
- Czy wprowadzić funkcjonalność agregacji mało istotnych serii do "pozostałe"?
- Jak zapewnić dostępność dla osób z zaburzeniami widzenia kolorów?
- Czy sortowanie w legendzie powinno być domyślnie po wartościach zamiast alfabetycznie?


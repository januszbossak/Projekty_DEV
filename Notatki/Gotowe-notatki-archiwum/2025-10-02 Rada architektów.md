> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-10-02

**Powiązane projekty:**
- `moduly/Raporty-systemowe` – tematy 1, 2, 3, 4, 5
- `moduly/Modul-raportowy` – tematy 1, 2, 3, 4, 5
- `moduly/Zrodla-danych` – temat 6
- `Moduly/Modul-raportowy/Tlumaczenia-i-aliasy` – temat 1
- `Klienci/WIM/WCAG` – tematy 1, 5
- `cross-cutting/WCAG` – tematy 1, 5
- `cross-cutting/Zakladka-Raporty` – tematy 1, 2

---

## 1. Raporty systemowe – prezentacja dashboardów i problemy merytoryczne

**Projekt:** `moduly/Raporty-systemowe`, `moduly/Modul-raportowy`, `Moduly/Modul-raportowy/Tlumaczenia-i-aliasy`, `Klienci/WIM/WCAG`, `cross-cutting/WCAG`, `cross-cutting/Zakladka-Raporty`

### Kontekst i Problem

Łukasz Bott przedstawił dashboardy systemowe, które zostały przygotowane w module raportów systemowych. W module pojawiła się możliwość kilku nowych źródeł zewnętrznych, które są synchronizowane raz dziennie (agregaty dla statystyk dziennych, aby nie obciążać połączeń online do bazy danych). Podczas prezentacji zidentyfikowano szereg problemów merytorycznych i wizualizacyjnych wymagających poprawy przed wydaniem.

### Zidentyfikowane Ryzyka

- Raporty prezentują nieprawidłowe dane biznesowe z powodu błędnej logiki pobierania danych z `CaseHistory` zamiast `CaseDefinition`
- Brak jasności co prezentują raporty może wprowadzić użytkowników w błąd
- Niespójność tłumaczeń (mieszanka polskiego i angielskiego) obniża profesjonalizm interfejsu
- Problemy z kontrastem kolorów w wizualizacjach (szary tekst na szarym tle) uniemożliwiają odczytanie danych
- Nieprawidłowe działanie linku "Raporty systemowe" z menu modułów systemowych w trybie listy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Raporty dla spraw zamkniętych i w toku razem | Prezentowanie wszystkich spraw w jednym raporcie | ❌ Odrzucona – sprawy zamknięte i w toku to różne stany analityczne wymagające osobnych raportów |
| Raporty osobno dla zamkniętych i w toku | Dwa osobne zestawy raportów: jeden dla spraw zamkniętych (z `CaseDefinition`), drugi dla spraw w toku (z `CaseHistory`) | ✅ Wybrana – pozwala na prawidłową analizę biznesową obu stanów |
| Tree Map dla wszystkich przypadków | Użycie Tree Map niezależnie od liczby wartości | ❌ Odrzucona – Tree Map sprawdza się tylko dla 3-4 wartości, przy większej liczbie staje się nieczytelna |
| Słupkowy wykres zamiast Tree Map | Zamiana Tree Map na wykres słupkowy dla większej czytelności | 💡 Propozycja – do rozważenia w zależności od liczby wartości |
| Nadpisanie ustawienia wyświetlania na kafelki | Wymuszenie trybu kafelkowego przy wejściu przez menu modułów systemowych | ✅ Wybrana – najprostsze rozwiązanie techniczne, zapewnia spójne działanie |

### Decyzja

**Status:** 🔍 Do weryfikacji i poprawy

Raporty systemowe wymagają poprawy przed wydaniem. Ustalono następujące działania:

1. **Poprawa logiki raportów:**
   - Raporty dla spraw zamkniętych powinny pobierać dane z `CaseDefinition` (mają datę zamknięcia)
   - Raporty dla spraw w toku powinny pobierać dane z `CaseHistory` (aktualny stan)
   - Raport "Średni czas procesowania spraw" powinien dotyczyć tylko spraw zamkniętych (od początku do zamknięcia)
   - Raport "Maksymalny czas procesowania" powinien dotyczyć tylko spraw zamkniętych (aby uniknąć zaburzeń przez jedną długo wiszącą sprawę)
   - Raport "Minimalny czas procesowania" nie ma sensu dla spraw w toku (brak daty zakończenia) – do usunięcia z widoku spraw w toku

2. **Poprawa nazewnictwa i opisów:**
   - Każdy raport musi mieć jasną nazwę biznesową określającą co prezentuje
   - Każdy raport musi mieć opis biznesowy (nie techniczny) wyjaśniający po co służy i jak z niego korzystać
   - Opis powinien być dostępny w interfejsie (tooltip lub przycisk "i" w kółeczku przy filtrach i odświeżaniu)
   - Zmiana nazwy "osoby najczęściej tworzące raporty" na "osoby które najwięcej utworzyły raportów" (częstotliwość vs ilość)
   - Zmiana "zmodyfikowanych" na "obsługiwanych" spraw (bardziej biznesowe brzmienie)

3. **Poprawa wizualizacji:**
   - Tree Map tylko dla 3-4 wartości, przy większej liczbie użycie wykresu słupkowego
   - Poprawa kontrastu kolorów (szary tekst na szarym tle jest nieczytelny)
   - Ujednolicenie kolorów tooltipów (wszędzie czarne lub białe, zależnie od tła)
   - Rozważenie użycia koloru jako dodatkowego wymiaru informacji (np. kolor = ilość spraw, rozmiar = czas procesowania)

4. **Poprawa tłumaczeń:**
   - Przetłumaczenie wszystkich elementów interfejsu na polski (obecnie mieszanka polskiego i angielskiego)
   - Przetłumaczenie nazw filtrów (Report Created By, Report Type, Report Category → po polsku)
   - Przetłumaczenie breadcrumbs (górny pasek nawigacyjny)

5. **Poprawa działania linku z menu:**
   - Link "Raporty systemowe" z menu modułów systemowych powinien nadpisywać ustawienie wyświetlania na tryb kafelkowy (nawet jeśli użytkownik ma ustawione wyświetlanie listy)
   - Po kliknięciu użytkownik powinien zostać przeniesiony do folderu "Raporty systemowe" w trybie kafelkowym

**Szczegóły techniczne:**
- Tabela `CaseHistory` – historia zmian stanów sprawy (brak ostatniego stanu)
- Tabela `CaseDefinition` – aktualny stan sprawy (zawiera datę zamknięcia dla spraw zamkniętych)
- Kolumna `CaseModified` – data modyfikacji sprawy
- Tryb lokalny źródeł danych – agregacja raz dziennie dla statystyk dziennych
- Grupa uprawnień `System Reports Managers` – uprawnienie do edycji raportów i dashboardów systemowych

### Zadania

- **Łukasz Bott:** Przygotowanie opisów biznesowych dla wszystkich raportów systemowych (intencja tworzenia, co prezentuje biznesowo, nie technicznie) → termin: przed spotkaniem w przyszłym tygodniu (poniedziałek/wtorek)
- **Anna Skupińska:** Przetłumaczenie interfejsu raportów systemowych na polski (w tym breadcrumbs, filtry) → termin: możliwe jeszcze dzisiaj
- **Anna Skupińska:** Poprawa działania linku "Raporty systemowe" z menu modułów systemowych (nadpisanie ustawienia wyświetlania na kafelki) → termin: do ustalenia
- **Anna Skupińska:** Poprawa kontrastu kolorów w wizualizacjach (szary tekst na szarym tle) → termin: do ustalenia
- **Anna Skupińska:** Ujednolicenie kolorów tooltipów → termin: do ustalenia
- **Damian Kamiński / Kamil:** Spotkanie z Łukaszem w przyszłym tygodniu (poniedziałek/wtorek) do przedyskutowania opisów biznesowych i weryfikacji co jeszcze brakuje → termin: poniedziałek/wtorek przyszłego tygodnia
- **Janusz Bossak:** Weryfikacja biznesowa raportów po przygotowaniu opisów → termin: wtorek/środa przyszłego tygodnia (po powrocie)

### Punkty otwarte

- Czy warto dodać możliwość filtrowania użytkowników w raporcie "osoby które najwięcej utworzyły raportów" (np. odcięcie użytkowników z mniej niż 10 raportami)?
- Czy warto użyć koloru jako dodatkowego wymiaru informacji w Tree Map (kolor = ilość spraw, rozmiar = czas procesowania)?
- Czy opisy raportów powinny być zapamiętywane (obecnie się nie zapamiętują pomimo wprowadzenia)?
- Czy warto zaangażować specjalistę od BI (np. Michała) do konsultacji wizualizacji danych?

---

## 2. Raporty systemowe – problem z linkiem w trybie listy

**Projekt:** `moduly/Raporty-systemowe`, `cross-cutting/Zakladka-Raporty`

### Kontekst i Problem

Link "Raporty systemowe" z menu modułów systemowych (zębatka w prawym górnym rogu) nie działa poprawnie, gdy użytkownik ma ustawione wyświetlanie raportów w trybie listy. W takim przypadku kliknięcie linku nie przenosi użytkownika do folderu "Raporty systemowe" – link nie ma żadnego skutku.

### Zidentyfikowane Ryzyka

- Użytkownik nie może dostać się do raportów systemowych przez menu modułów systemowych, jeśli preferuje widok listy
- Niespójne zachowanie interfejsu w zależności od ustawienia wyświetlania

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Nadpisanie ustawienia na kafelki | Wymuszenie trybu kafelkowego przy kliknięciu linku z menu | ✅ Wybrana – najprostsze rozwiązanie techniczne (2 godziny pracy vs 2 dni) |
| Rozwinięcie węzła w trybie listy | Przewinięcie do pozycji "Raporty systemowe" i rozwinięcie drzewka w trybie listy | ❌ Odrzucona – bardziej skomplikowane technicznie (2 dni pracy) |
| Niezależność od ustawienia | Link zawsze działa niezależnie od trybu wyświetlania | ⏸️ Odroczona – wymaga analizy implementacji |

### Decyzja

**Status:** ✅ Zatwierdzone

Link "Raporty systemowe" z menu modułów systemowych powinien nadpisywać ustawienie wyświetlania raportów na tryb kafelkowy. Po kliknięciu użytkownik zostanie przeniesiony do folderu "Raporty systemowe" w trybie kafelkowym, niezależnie od tego, jaki tryb wyświetlania miał ustawiony wcześniej.

**Uzasadnienie:** Najprostsze rozwiązanie techniczne (szacunek: 2 godziny vs 2 dni dla alternatywy z rozwinięciem węzła). Jeśli użytkownik wróci do zakładki "Raporty" i chce przeglądać w formie listy, może ponownie przełączyć tryb wyświetlania.

**Szczegóły techniczne:**
- Link dodaje `Cat ID` (katalog ID) do URL-a
- W trybie kafelkowym link działa poprawnie
- W trybie listy link nie działa (nie ma efektu)

### Zadania

- **Anna Skupińska:** Implementacja nadpisywania ustawienia wyświetlania na tryb kafelkowy przy kliknięciu linku "Raporty systemowe" z menu modułów systemowych → termin: do ustalenia

### Punkty otwarte

- Brak

---

## 3. Raporty systemowe – opisy raportów i dashboardów

**Projekt:** `moduly/Raporty-systemowe`

### Kontekst i Problem

Raporty systemowe i dashboardy powinny mieć opisy biznesowe wyjaśniające po co służą i jak z nich korzystać. Obecnie opisy się nie zapamiętują pomimo wprowadzenia (zgłoszony błąd). Ponadto opisy powinny być dostępne w interfejsie użytkownika, aby użytkownik mógł zrozumieć co prezentuje dany raport przed jego otwarciem.

### Zidentyfikowane Ryzyka

- Brak opisów uniemożliwia użytkownikom zrozumienie przeznaczenia raportów
- Opisy się nie zapamiętują, co utrudnia ich utrzymanie
- Brak dostępu do opisów w interfejsie wymusza otwieranie raportu, aby zrozumieć jego przeznaczenie

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Tooltip przy znaku zapytania | Opis dostępny po najechaniu na znak zapytania | ❌ Odrzucona – znak zapytania nie jest intuicyjny |
| Tooltip przy ikonie "i" w kółeczku | Opis dostępny po najechaniu na ikonę "i" przy filtrach i odświeżaniu | ✅ Wybrana – bardziej intuicyjne, analogiczne do legendy |
| Opis wewnątrz raportu | Opis wyświetlany w prawym górnym rogu samego raportu (jak legenda) | 💡 Propozycja – do rozważenia jako dodatkowa opcja |

### Decyzja

**Status:** 🔍 Do weryfikacji

Opisy raportów i dashboardów powinny być dostępne w interfejsie. Proponowane rozwiązanie: ikona "i" w kółeczku przy filtrach i odświeżaniu, po kliknięciu której pojawia się opis raportu (tooltip lub okno dialogowe).

**Szczegóły techniczne:**
- Opisy się nie zapamiętują pomimo wprowadzenia (zgłoszony błąd)
- Opisy powinny być biznesowe, nie techniczne (co prezentuje, po co służy, nie jak działa technicznie)

### Zadania

- **Anna Skupińska:** Naprawa błędu z zapamiętywaniem opisów raportów i dashboardów → termin: do ustalenia
- **Łukasz Bott:** Przygotowanie opisów biznesowych dla wszystkich raportów systemowych → termin: przed spotkaniem w przyszłym tygodniu

### Punkty otwarte

- Czy opisy powinny być również dostępne wewnątrz raportu (w prawym górnym rogu, jak legenda)?
- Czy opisy powinny być zapamiętywane przez użytkownika (preferencja wyświetlania/ukrywania)?

---

## 4. Raporty systemowe – wizualizacja danych (Tree Map vs wykres słupkowy)

**Projekt:** `moduly/Raporty-systemowe`, `moduly/Modul-raportowy`

### Kontekst i Problem

Część raportów systemowych używa Tree Map do prezentacji danych. Tree Map sprawdza się tylko dla 3-4 wartości – przy większej liczbie staje się nieczytelna (mozaika prostokątów). Janusz Bossak wyraził preferencję dla wykresów słupkowych, które są bardziej czytelne i pozwalają łatwiej porównać wartości.

### Zidentyfikowane Ryzyka

- Tree Map z dużą liczbą wartości jest nieczytelna i nie niesie wartościowej informacji biznesowej
- Brak spójności w wizualizacji może dezorientować użytkowników

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Tree Map dla wszystkich przypadków | Użycie Tree Map niezależnie od liczby wartości | ❌ Odrzucona – Tree Map sprawdza się tylko dla 3-4 wartości |
| Wykres słupkowy dla wszystkich | Zamiana wszystkich Tree Map na wykresy słupkowe | 💡 Propozycja – do rozważenia |
| Tree Map tylko dla 3-4 wartości | Użycie Tree Map tylko gdy jest mało wartości, przy większej liczbie wykres słupkowy | ✅ Wybrana – zgodne z zasadami wizualizacji danych |
| Kolor jako dodatkowy wymiar | Użycie koloru jako dodatkowej informacji (np. kolor = ilość spraw, rozmiar = czas procesowania) | 💡 Propozycja – do rozważenia z konsultantem BI |

### Decyzja

**Status:** 💡 Propozycja

Tree Map powinny być używane tylko dla 3-4 wartości. Przy większej liczbie wartości należy użyć wykresu słupkowego dla lepszej czytelności. Warto rozważyć użycie koloru jako dodatkowego wymiaru informacji (np. kolor = ilość spraw, rozmiar = czas procesowania), ale wymaga to konsultacji ze specjalistą od BI.

**Szczegóły techniczne:**
- Tree Map to odpowiednik wykresu kołowego (Pie Chart)
- Wykres kołowy sprawdza się tylko dla kilku wartości (3-4)
- Przy większej liczbie wartości mózg ma problem z odczytaniem proporcji

### Zadania

- **Łukasz Bott:** Weryfikacja raportów systemowych i zamiana Tree Map na wykresy słupkowe tam, gdzie jest więcej niż 4 wartości → termin: do ustalenia
- **Damian Kamiński / Kamil:** Rozważenie konsultacji ze specjalistą od BI (np. Michałem) w kontekście wizualizacji danych → termin: do ustalenia

### Punkty otwarte

- Czy warto użyć koloru jako dodatkowego wymiaru informacji w Tree Map?
- Czy warto zaangażować specjalistę od BI do konsultacji wszystkich wizualizacji?

---

## 5. Raporty systemowe – problemy z kontrastem i kolorami

**Projekt:** `moduly/Raporty-systemowe`, `moduly/Modul-raportowy`, `Klienci/WIM/WCAG`, `cross-cutting/WCAG`

### Kontekst i Problem

Podczas prezentacji dashboardów systemowych zidentyfikowano problemy z kontrastem kolorów i niespójnością kolorów tooltipów. Szary tekst na szarym tle jest nieczytelny (np. "Value Process" w Tree Map). Tooltipy mają różne kolory tekstu (czarny lub biały) w zależności od koloru kafelka, co może być mylące.

### Zidentyfikowane Ryzyka

- Nieczytelność danych z powodu braku kontrastu (szary tekst na szarym tle)
- Niespójność wizualna tooltipów może dezorientować użytkowników
- Problemy z dostępnością (WCAG) – brak odpowiedniego kontrastu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ujednolicenie kolorów tooltipów | Wszystkie tooltipy w jednym kolorze (czarny lub biały) niezależnie od koloru kafelka | ✅ Wybrana – zapewnia spójność i czytelność |
| Tooltipy dopasowane do koloru kafelka | Tooltipy biorą kolor z kafelka (obecne rozwiązanie) | ❌ Odrzucona – powoduje problemy z czytelnością (szary tekst na szarym tle) |
| Poprawa kontrastu automatyczna | Automatyczne dostosowanie koloru tekstu do tła dla zapewnienia kontrastu | 💡 Propozycja – do rozważenia jako długoterminowe rozwiązanie |

### Decyzja

**Status:** ✅ Zatwierdzone

Należy poprawić kontrast kolorów w wizualizacjach i ujednolicić kolory tooltipów. Szary tekst na szarym tle jest nieczytelny i wymaga poprawy. Tooltipy powinny mieć ujednolicony kolor (czarny lub biały) niezależnie od koloru kafelka, aby zapewnić czytelność i spójność.

**Szczegóły techniczne:**
- Tooltipy mają przezroczyste tło, które jest rozjaśnione względem koloru kafelka
- Obecnie tooltipy biorą kolor tekstu z koloru kafelka (fill)
- Problem szczególnie widoczny przy szarym kolorze (brak kontrastu z białym tekstem)

### Zadania

- **Anna Skupińska:** Poprawa kontrastu kolorów w wizualizacjach (szary tekst na szarym tle) → termin: do ustalenia
- **Anna Skupińska:** Ujednolicenie kolorów tooltipów (wszędzie czarny lub biały, niezależnie od koloru kafelka) → termin: do ustalenia

### Punkty otwarte

- Czy warto zaimplementować automatyczne dostosowanie koloru tekstu do tła dla zapewnienia kontrastu (długoterminowe rozwiązanie)?

---

## 6. Źródła danych – problem z tworzeniem źródeł lokalnych dla MS SQL

**Projekt:** `moduly/Zrodla-danych`

### Kontekst i Problem

W module raportów systemowych pojawiła się możliwość kilku nowych źródeł zewnętrznych, które są synchronizowane raz dziennie (agregaty dla statystyk dziennych, aby nie obciążać połączeń online do bazy danych). O ile dla MySQL nie ma problemu z tworzeniem tego typu źródeł lokalnych, to w przypadku bazy MS SQL jest problem techniczny wymagający rozwiązania.

### Zidentyfikowane Ryzyka

- Brak możliwości tworzenia źródeł lokalnych dla MS SQL może wstrzymać prace nad raportami systemowymi
- Niespójność funkcjonalności między różnymi typami baz danych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Najpierw MySQL, potem MS SQL | Skupienie się na MySQL, poprawki dla MS SQL później | ✅ Wybrana – nie wstrzymuje prac, pozwala na kontynuację rozwoju |
| Czekanie na rozwiązanie MS SQL | Wstrzymanie prac do rozwiązania problemu z MS SQL | ❌ Odrzucona – wstrzymałoby prace nad raportami systemowymi |

### Decyzja

**Status:** ✅ Zatwierdzone

Aby nie wstrzymywać prac nad raportami systemowymi, w pierwszej kolejności należy skupić się na MySQL. Poprawki dla MS SQL będą wykonane później przez Annę Skupińską po zakończeniu prac technicznych nad dashboardami systemowymi.

**Szczegóły techniczne:**
- Źródła lokalne (integracyjne) – synchronizowane raz dziennie
- Źródła online – połączenie na żądanie
- Problem dotyczy tworzenia źródeł lokalnych dla MS SQL (nie dotyczy źródeł online)

### Zadania

- **Anna Skupińska:** Rozwiązanie problemu z tworzeniem źródeł lokalnych dla MS SQL → termin: po zakończeniu prac technicznych nad dashboardami systemowymi

### Punkty otwarte

- Jaka jest przyczyna problemu z tworzeniem źródeł lokalnych dla MS SQL?
- Czy problem dotyczy tylko źródeł lokalnych, czy również innych operacji na źródłach danych dla MS SQL?


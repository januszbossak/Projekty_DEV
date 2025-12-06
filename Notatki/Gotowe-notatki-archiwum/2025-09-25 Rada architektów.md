> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-09-25

**Powiązane projekty:**
- `moduly/Wspolna-praca-na-dokumentach-office` – temat 1 (wspólna edycja plików Office)
- `Moduly/Edytor-procesow` – tematy 2, 3, 5, 6
- `cross-cutting/Logowanie-delete-case` – tematy 2, 3
- `Moduly/Ustawienia-systemowe/Zadania-jobs` – tematy 2, 3, 4
- `cross-cutting/Interfejs-sprawy/Formularz-sprawy` – temat 5
- `Moduly/Raporty-systemowe` – temat 7
- `Moduly/Edytor-procesow/Edytor-szablonow` – temat 8 (CLM - marketing)
- `Moduly/AMODIT Copilot` – tematy 9, 10
- `Moduly/Silnik-regul` – tematy 11, 12
- `cross-cutting/Bezpieczenstwo-pentesty` – temat 13
- `Integracje/System-mailowy` – temat 14

---

## 1. Automatyczne zamykanie dokumentów w trakcie edycji z Office'a (SharePoint)

**Projekt:** `moduly/Wspolna-praca-na-dokumentach-office`

### Kontekst i Problem

Klienci w obawie przed tym, że dokument przed zakończeniem edycji zniknie z SharePointa, puszczają z poziomu bazy danych (lub regułą) zamykanie otwartych w trakcie edycji dokumentów po określonym okresie od momentu otwarcia. Czasami dokumenty wiszą jako "w trakcie edycji" przez kilka tygodni, bo użytkownicy nie kliknęli przycisku "Zakończ edycję". W tym czasie dokument może zniknąć z cache'a SharePointa i wtedy będzie problem – nie wróci nowa wersja do AMODIT-a. Obecne rozwiązanie przez reguły okresowe obciąża system wydajnościowo.

### Zidentyfikowane Ryzyka

- Dokumenty mogą wisieć jako "w trakcie edycji" przez długi czas, blokując dostęp innych użytkowników
- Dokument może zniknąć z cache'a SharePointa przed zakończeniem edycji
- Reguły okresowe obciążają system wydajnościowo

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Job do automatycznego zamykania edycji | Job przechodzący o północy i zamykający edycje w obecnym stanie po okresie braku aktywności | ✅ Wybrana – wydajniejsze niż reguły okresowe, konfigurowalne |
| Reguły okresowe | Obecne rozwiązanie przez reguły okresowe | ❌ Odrzucona – obciąża system wydajnościowo |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie stworzony Job, który będzie automatycznie zamykał edycje dokumentów po określonym czasie braku aktywności użytkownika. Job będzie konfigurowalny – jeśli ktoś nie chce tego zamykania, po prostu nie aktywuje Joba.

**Szczegóły techniczne:**
- Job przechodzi o północy (lub w konfigurowalnej godzinie)
- Zamyka edycje po określonym czasie braku aktywności (np. 2 dni)
- Jeśli użytkownik wykona jakąś akcję (np. jutro, pojutrze), to znaczy że pracuje i edycja nie jest zamykana
- Akcja zamykania musi być wykonana po stronie SharePointa

### Zadania

- **[Kamil Dubaniowski]:** Kosztowanie i projektowanie Joba do automatycznego zamykania edycji dokumentów z Office'a → termin: do ustalenia

---

## 2. Usuwanie spraw, które nie poszły w obieg

**Projekt:** `moduly/Edytor-procesow-formularzy`, `cross-cutting/Logowanie-delete-case`, `moduly/Ustawienia-systemowe`

### Kontekst i Problem

Klienci (np. Rossmann) mają problem ze sprawami, które zostały uruchomione, ale nie poszły w obieg. Obecnie robią to z poziomu bazy danych lub regułami – po roku czy po dwóch latach od utworzenia, jeśli sprawa nie wyszła w obieg, usuwają masowo z bazy. Potrzebne jest ustawienie systemowe lub na poziomie procesu, które automatycznie usuwa takie sprawy przez Job.

### Zidentyfikowane Ryzyka

- Sprawy mogą wisieć latami na pierwszym etapie, zajmując miejsce w bazie
- Ręczne usuwanie przez reguły lub zapytania SQL jest nieefektywne
- Niektóre procesy (np. rejestry) nie powinny być opróżniane, bo są przechowywane na pierwszym etapie celowo

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ustawienie globalne systemowe | Globalne ustawienie "usuwaj sprawy starsze niż X" (np. rok, 10 miesięcy, 5 miesięcy, 3 miesiące) | ✅ Wybrana – większość klientów będzie chciała globalnego ustawienia |
| Ustawienie na poziomie procesu | Możliwość wyłączenia dla konkretnych procesów (np. rejestry) | ✅ Wybrana – niektóre procesy nie powinny być usuwane |
| Usuwanie spraw z danymi | Opcja czy usuwać sprawy które mają jakieś dane wprowadzone | ⏸️ Odroczona – do rozważenia, ale jeśli sprawa wisi rok, to prawdopodobnie ktoś zaczął wniosek i go nie złożył |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie wprowadzone ustawienie na poziomie definicji procesu (niezależnie czy to proces, podproces, rejestr) z opcjami:
- "Nigdy nie usuwaj spraw, które nie poszły w obieg"
- "Usuwaj, ale..." z podaniem interwału (np. rok, 2 lata)

Job będzie wykonywał dwie operacje:
1. Usuwanie spraw nowo założonych (które nie poszły w obieg) – najpierw `CaseIsHidden`, potem po roku trwałe usunięcie
2. Usuwanie spraw z kosza (`CaseIsHidden`) po określonym czasie (jeśli administrator podejmie decyzję)

**Szczegóły techniczne:**
- Ustawienie na poziomie definicji procesu
- Możliwość wyłączenia dla konkretnych procesów (np. rejestry)
- Job wykonuje operacje krokowo: najpierw `CaseIsHidden`, potem po roku trwałe usunięcie
- Jeden Job może robić obie operacje: usuwanie spraw nowo założonych i usuwanie spraw z kosza

### Zadania

- **[Kamil Dubaniowski]:** Dodanie ustawienia do projektu → termin: do ustalenia
- **[Piotr Buczkowski / Damian Kamiński]:** Projektowanie i implementacja Joba do usuwania spraw → termin: do ustalenia

---

## 3. Czyszczenie kosza (CaseIsHidden)

**Projekt:** `cross-cutting/Logowanie-delete-case`, `moduly/Ustawienia-systemowe`

### Kontekst i Problem

Obecnie kosz (`CaseIsHidden`) jest bezdenny i trzyma sprawy do końca świata. Nie ma możliwości zbiorczego czyszczenia kosza – trzeba napisać regułę. Potrzebna jest opcja automatycznego czyszczenia kosza po określonym czasie.

### Zidentyfikowane Ryzyka

- Kosz może się przepełnić sprawami, które już nie są potrzebne
- Brak możliwości zbiorczego czyszczenia kosza

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Parametr do czyszczenia kosza | Opcja w ustawieniach systemowych do ustawienia interwału czyszczenia kosza (np. rok, 2, 5 lat od oznaczenia jako `CaseIsHidden`) | ✅ Wybrana – nie narzucamy, tylko dajemy opcję |
| Kosz bezdenny (jak dotychczas) | Brak automatycznego czyszczenia | ✅ Wybrana – jeśli ktoś nie chce, nie ustawia parametru |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie wprowadzony parametr w ustawieniach systemowych, który pozwala czyścić kosz po określonym czasie od oznaczenia sprawy jako `CaseIsHidden`. Jeśli ktoś nie chce, nie musi ustawiać tego parametru – kosz pozostanie bezdenny. To będzie część Joba z tematu 2.

**Szczegóły techniczne:**
- Parametr: interwał czyszczenia kosza (np. rok, 2, 5 lat od oznaczenia jako `CaseIsHidden`)
- Opcjonalne – jeśli nie ustawione, kosz pozostaje bezdenny
- Część Joba z tematu 2 (usuwanie spraw nowo założonych i czyszczenie kosza)

### Zadania

- **[Piotr Buczkowski / Damian Kamiński]:** Projektowanie i implementacja parametru czyszczenia kosza → termin: do ustalenia

---

## 4. Ograniczenia częstotliwości wykonywania Jobów

**Projekt:** `moduly/Ustawienia-systemowe`

### Kontekst i Problem

Niektóre Joby (np. Job czyszczący sprawy) nie powinny się wykonywać częściej niż raz dziennie. Obecnie nie ma takiego ograniczenia, co może prowadzić do niepotrzebnego obciążenia systemu.

### Zidentyfikowane Ryzyka

- Niektóre Joby mogą być ustawione na zbyt częste wykonywanie, obciążając system
- Brak kontroli nad częstotliwością wykonywania niektórych Jobów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ograniczenie częstotliwości dla niektórych Jobów | Możliwość ustawienia minimalnego interwału dla niektórych Jobów (np. nie częściej niż raz dziennie) | ✅ Wybrana – zapobiega niepotrzebnemu obciążeniu |
| Brak ograniczeń | Obecne rozwiązanie | ❌ Odrzucona – może prowadzić do problemów wydajnościowych |

### Decyzja

**Status:** 💡 Propozycja

Warto przejrzeć, czy jeszcze jakieś Joby powinny mieć ograniczenie częstotliwości wykonywania. Dla Joba czyszczącego sprawy powinno być ograniczenie, że nie można go ustawić częściej niż raz dziennie (lub w perspektywie dni/miesięcy, nie godzin).

**Szczegóły techniczne:**
- Ograniczenie dla Joba czyszczącego sprawy: nie częściej niż raz dziennie
- Warto przejrzeć inne Joby pod kątem podobnych ograniczeń
- Uwaga: reguły okresowe czasami muszą się odpalać co 5 minut, więc nie wszystkie Joby powinny mieć ograniczenia

### Zadania

- **[Piotr Buczkowski / Damian Kamiński]:** Przejrzenie Jobów pod kątem ograniczeń częstotliwości → termin: do ustalenia

---

## 5. Przełączanie sekcji w formularzu sprawy – strzałki lewo/prawo

**Projekt:** `cross-cutting/UI-formularza-sprawy`

### Kontekst i Problem

Klienci mają długie sekcje w zakładkach formularza sprawy. Gdy użytkownik zeskroluje się na sam dół sekcji w zakładce, żeby przejść na kolejną zakładkę musi wracać na górę i przełączać się na kolejną. Często uzupełniają dane sekcja po sekcji, zakładka po zakładce, i za każdym razem muszą zjeżdżać na sam dół, wracać na górę, zmieniać zakładkę, uzupełniać, jechać do samego dołu, wracać na górę.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Strzałki lewo/prawo na dole formularza | Strzałki "Następna" i "Poprzednia" na dole formularza do przełączania między zakładkami | ✅ Wybrana – nie zmniejsza przestrzeni roboczej, intuicyjne |
| Zamrożenie belki z zakładkami | Belka z zakładkami zawsze widoczna | ❌ Odrzucona – zmniejsza przestrzeń roboczą formularza |
| Zakładki też na dole | Duplikacja zakładek na dole formularza | ❌ Odrzucona – Piotr Buczkowski przeciwko |

### Decyzja

**Status:** 💡 Propozycja

Pomysł dodania strzałek "Następna" i "Poprzednia" na dole formularza do przełączania między zakładkami. Strzałka "Poprzednia" pojawia się tylko jeśli jest poprzednia zakładka. To rozwiązanie nie zmniejsza przestrzeni roboczej (nie zamraża belki z zakładkami) i jest intuicyjne dla użytkowników, którzy uzupełniają formularz sekcja po sekcji.

**Szczegóły techniczne:**
- Strzałki na dole formularza sprawy
- "Następna" – przejście do następnej zakładki (z nazwą zakładki w nawiasie lub tooltipie)
- "Poprzednia" – przejście do poprzedniej zakładki (jeśli istnieje)
- Nie zamraża belki z zakładkami (nie zmniejsza przestrzeni roboczej)

### Zadania

- **[Kamil Dubaniowski]:** Przedyskutowanie z klientem i zaproponowanie pakietowo (może wymagać dołożenia się klienta) → termin: do ustalenia

### Punkty otwarte

- Czy klient będzie chciał się dołożyć do tego rozwiązania?
- Czy to rozwiązanie powinno być uniwersalne dla wszystkich klientów?

---

## 6. Widok powiązań w ustawieniach procesu – usprawnienia

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

W nowym widoku powiązań w ustawieniach procesu (robiony przez Mariusza z Damianem) są pewne problemy:
1. Legenda na górze jest myląca – klienci myślą, że to są filtry i chcą w nie klikać, żeby filtrować powiązania (np. tylko grupy)
2. Brak możliwości eksportu powiązań do JSON-a (klienci piszą dokumentację poza AMODIT-em i muszą przepisywać powiązania)
3. Widok nie czyta reguł, więc jest ułomny (powinien być wspierany przez AI)

### Zidentyfikowane Ryzyka

- Brak możliwości filtrowania powiązań utrudnia analizę dużych procesów
- Brak eksportu utrudnia dokumentację procesów
- Widok nie jest kompletny (nie czyta reguł)

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Widok powiązań wymaga usprawnień:
1. Legenda powinna spaść na dół (nie być na górze)
2. Funkcjonalność filtrów powinna być dodana – możliwość filtrowania powiązań (np. tylko grupy, tylko użytkownicy)
3. Eksport do JSON-a powinien być dodany
4. Widok powinien być wspierany przez AI (do czytania reguł)

**Szczegóły techniczne:**
- Legenda przeniesiona na dół
- Filtry do wyboru typu powiązań (grupy, użytkownicy, inne)
- Eksport do JSON-a
- Wsparcie AI do czytania reguł (już omawiane wcześniej)

### Zadania

- **[Mariusz Piotrzkowski / Damian Kamiński]:** Przeniesienie legendy na dół i dodanie filtrów → termin: do ustalenia
- **[Mariusz Piotrzkowski / Damian Kamiński]:** Dodanie eksportu do JSON-a → termin: do ustalenia
- **[Mariusz Piotrzkowski / Damian Kamiński]:** Integracja z AI do czytania reguł → termin: do ustalenia

---

## 7. Statystyki procesu

**Projekt:** `moduly/Raporty-systemowe`

### Kontekst i Problem

Klienci mają dużą skalę i czasami informacja do nich nie dociera, że dany proces już został wygaszony, nie jest używany, a wisi cały czas. Potrzebują informacji: ile jest spraw w tym procesie, kiedy została utworzona ostatnia sprawa w tym procesie. Na podstawie tego mogą zapytać, czy proces ma nową wersję, czy w ogóle już nie używają.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Raport systemowy | Raport systemowy pokazujący statystyki procesu (ilość spraw, data ostatniej sprawy) | ✅ Wybrana – zgodna z sugestią klienta |
| Lokalizacja w ustawieniach procesu | Statystyki bezpośrednio w ustawieniach procesu | ⏸️ Odroczona – klient zasugerował raport systemowy |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie stworzony raport systemowy pokazujący statystyki procesu:
- Ilość spraw w procesie
- Data utworzenia ostatniej sprawy w procesie
- Informacja czy proces jest aktywny (kiedy ostatnie uruchomienie)

Raport będzie dostępny w kontekście ustawień procesu (prawdopodobnie w prawym górnym rogu, gdzie są użytkownicy, grupy, słowniki – tam gdzie będą logi systemowe i odnośnik do raportów systemowych).

**Szczegóły techniczne:**
- Raport systemowy w kontekście procesu
- Statystyki: ilość spraw, data ostatniej sprawy, data ostatniego uruchomienia
- Lokalizacja: prawy górny róg ustawień procesu (gdzie są użytkownicy, grupy, słowniki)

### Zadania

- **[Łukasz Bott]:** Stworzenie raportu systemowego ze statystykami procesu → termin: do ustalenia
- **[Łukasz Bott]:** Sprawdzenie, co było w starych statystykach (zakładka "Statystyki" w czerwcowej wersji została usunięta na poczet raportów systemowych) → termin: do ustalenia

### Punkty otwarte

- Czy wszystkie statystyki ze starej zakładki są pokryte przez raporty systemowe?

---

## 8. CLM (Contract Lifecycle Management) – marketing

**Projekt:** Nowy temat / do sklasyfikowania

### Kontekst i Problem

Marketing promuje AMODIT jako narzędzie CLM (Contract Lifecycle Management) do zarządzania dokumentacją prawną. To pojawiło się na LinkedInie bez wiedzy zespołu. AMODIT nie jest w pełni narzędziem CLM – nie jest w stanie dobrze generować dokumentów na podstawie formularzy (szablony nie są w stanie dobrze przenieść danych z formularza na szablon, żeby to miało ładne formatowanie i nadawało się do generowania PDF i podpisu). Brakuje ładnego edytora po stronie AMODIT-a do zbierania danych z paragrafami i innymi rzeczami.

### Zidentyfikowane Ryzyka

- Klienci mogą mieć nieprawidłowe oczekiwania co do możliwości AMODIT-a jako narzędzia CLM
- Marketing może wprowadzać w błąd potencjalnych klientów

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Trzeba się dowiedzieć, skąd się wziął wpis o CLM na LinkedInie i jak marketing rozumie CLM. Może marketing używa hasła "CLM" jako konkurencja dla Autenti i podobnych narzędzi, gdzie można przygotować draft, zasilić danymi i puścić do ludzi. Trzeba będzie to lepiej zaopiekować w szablonach i ich możliwościach edycji po stronie systemu.

**Szczegóły techniczne:**
- CLM = Contract Lifecycle Management (od przygotowania do archiwizacji umowy)
- AMODIT ma ograniczenia w generowaniu dokumentów z ładnym formatowaniem
- Szablony Wordowe działają dobrze (np. w Orlenie jest 20 szablonów)
- Tabelki są obsługiwane (można sterować szerokością, wielkością czcionki)

### Zadania

- **[Kamil Dubaniowski]:** Poszukanie wpisu o CLM na LinkedInie → termin: do ustalenia
- **[Damian Kamiński / Przemysław Sołdacki]:** Weryfikacja z marketingiem, jak rozumieją CLM → termin: do ustalenia

### Punkty otwarte

- Skąd się wziął wpis o CLM na LinkedInie?
- Jak marketing rozumie CLM w kontekście AMODIT-a?
- Czy AMODIT powinien być promowany jako narzędzie CLM?

---

## 9. Tłumaczenie formularzy AI – dla istniejących formularzy

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`, `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

AI może wspierać nie tylko tworzenie nowych procesów, ale także istniejące formularze. Konsultanci często nie dodają tooltipów do pól, a AI byłby w stanie sensownie je opisać. Również tłumaczenia formularzy są czasochłonne – konsultanci robią formularz po angielsku, a potem potrzebują tłumaczenia na polski, niemiecki, czeski.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 💡 Propozycja

AI powinien wspierać istniejące formularze:
1. Tłumaczenie istniejących formularzy na inne języki (akcja: "przetłumacz te pola na niemiecki")
2. Dodawanie tooltipów do pól (AI może sensownie opisać pola)
3. Tłumaczenie formularzy stworzonych ręcznie (nie przez AI) – konsultant robi formularz po angielsku, a potem potrzebuje tłumaczenia na polski, niemiecki, czeski

**Szczegóły techniczne:**
- Akcja w edytorze formularza: "Przetłumacz pola na [język]"
- Automatyczne dodawanie tooltipów do pól (jeśli brakuje)
- Działa zarówno dla istniejących formularzy, jak i dla nowych tworzonych ręcznie

### Zadania

- **[Kamil Dubaniowski]:** Dodanie do projektu jako rozwój → termin: do ustalenia

---

## 10. Baza wiedzy (Copilot) – usprawnienia

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`

### Kontekst i Problem

Klienci potrzebują:
1. Administratorów baz wiedzy (podobnie jak administratorzy słowników/grup) – np. dział HR chce sam zarządzać bazą wiedzy o Kodeksie Pracy
2. Możliwości wrzucania plików zamiast tylko tekstu (np. regulaminy wewnętrzne w plikach)
3. Data ważności treści (np. Kodeks Pracy co roku aktualizacja, finanse zmieniają się non stop)
4. Wersjonowanie treści (żeby zachować starą wersję dowodowo – dlaczego AI odpowiedział 2 lata temu w ten sposób)

### Zidentyfikowane Ryzyka

- Brak administratorów baz wiedzy utrudnia zarządzanie treścią przez działy (np. HR)
- Brak możliwości wrzucania plików utrudnia dodawanie treści (np. regulaminy)
- Brak daty ważności może prowadzić do nieaktualnych odpowiedzi AI
- Brak wersjonowania utrudnia śledzenie zmian w treści

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Administratorzy baz wiedzy | Podobnie jak administratorzy słowników/grup | ✅ Wybrana – zgodna z potrzebami klientów |
| Wrzucanie plików | Możliwość wrzucenia pliku zamiast tekstu | ✅ Wybrana – wygodniejsze dla działów HR |
| Data ważności (od-do) | Data obowiązywania treści (od-do) | ✅ Wybrana – pozwala na przygotowanie treści z wyprzedzeniem (np. regulamin na przyszły rok) |
| Wersjonowanie | Zachowanie starych wersji treści | ✅ Wybrana – ważne dowodowo |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostaną wprowadzone następujące usprawnienia do bazy wiedzy:
1. **Administratorzy baz wiedzy** – podobnie jak administratorzy słowników/grup, możliwość przypisania administratorów do konkretnych baz wiedzy
2. **Wrzucanie plików** – możliwość wrzucenia pliku zamiast tylko tekstu (np. regulaminy wewnętrzne)
3. **Data ważności** – data obowiązywania treści (od-do), jeśli data jest przekroczona, AI już z niej nie korzysta i mówi, że nie wie
4. **Wersjonowanie** – zachowanie starych wersji treści, możliwość filtrowania (pokazywanie tylko bieżących, ale możliwość zobaczenia wygasłych), możliwość usunięcia jeśli już nie są potrzebne

**Szczegóły techniczne:**
- Administratorzy baz wiedzy: podobnie jak administratorzy słowników/grup
- Wrzucanie plików: możliwość wrzucenia pliku (np. PDF, Word) zamiast tylko tekstu
- Data ważności: data od-do, jeśli przekroczona, AI nie korzysta z treści
- Wersjonowanie: zachowanie starych wersji, filtrowanie (bieżące/wygasłe), możliwość usunięcia

### Zadania

- **[Kamil Dubaniowski]:** Dodanie do projektu jako rozwój → termin: do ustalenia

### Punkty otwarte

- Czy wczytywanie plików powinno być przez repozytorium (FullText Search może odczytać plik i zapisać sobie informacje niezależnie)?
- Czy nazwa "Dodaj dokument" powinna zostać zmieniona na "Dodaj treść" (już zmienione w projekcie)?

---

## 11. ExecuteOnText dla pola typu raport

**Projekt:** `moduly/Silnik-regul`

### Kontekst i Problem

Obecnie `ExecuteOnText` działa dla pola typu dokument (Executor Action). Potrzebna jest obsługa pola typu raport, żeby można było wykonać akcje typu "odśwież", "wydrukuj", "wygeneruj CSV/Excel".

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozszerzenie ExecuteOnText | Dodanie obsługi pola typu raport do istniejącej funkcji ExecuteOnText | ✅ Wybrana – zgodna z architekturą (funkcja obiektowa) |
| Nowa funkcja reguł | Stworzenie nowej funkcji reguł specjalnie dla raportów | ❌ Odrzucona – niepotrzebne, ExecuteOnText jest funkcją obiektową |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostanie rozszerzona funkcja `ExecuteOnText` o obsługę pola typu raport. Funkcja będzie obsługiwała akcje:
- `Refresh` (odśwież)
- `Wydrukuj` (wydrukuj)
- `Wygeneruj CSV` / `Wygeneruj Excel` (eksport do Excela)

**Szczegóły techniczne:**
- Funkcja: `ExecuteOnText` rozszerzona o obsługę pola typu raport
- Akcje: Refresh, Wydrukuj, Wygeneruj CSV/Excel
- Funkcja obiektowa (podobnie jak dla pola typu dokument)

### Zadania

- **[Łukasz Bott]:** Rozszerzenie funkcji ExecuteOnText o obsługę pola typu raport → termin: do ustalenia
- **[Łukasz Bott]:** Aktualizacja opisu funkcji (musi uwzględniać pole typu dokument, pole typu raport) → termin: do ustalenia

---

## 12. CaseID w ForRow – problem z opisem funkcji

**Projekt:** `moduly/Silnik-regul`

### Kontekst i Problem

W opisie funkcji `ForRow` jest informacja, że można się odwołać do `CaseID` (innej sprawy), ale to nie powinno być w kontekście `ForRow`. `ForRow` powinien być tylko do przełączenia się w kontekst wiersza tabeli, nie do przełączania się w kontekst innej sprawy.

### Zidentyfikowane Ryzyka

- Opis funkcji może wprowadzać w błąd użytkowników
- Możliwość odwołania się do innej sprawy przez `CaseID` w `ForRow` może być niepożądana

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Opis funkcji `ForRow` powinien być poprawiony – nie powinien wskazywać, że można się odwołać do innej sprawy przez `CaseID`. `ForRow` powinien być tylko do przełączenia się w kontekst wiersza tabeli w ramach bieżącej sprawy.

**Szczegóły techniczne:**
- Funkcja: `ForRow`
- Problem: opis wskazuje możliwość odwołania się do innej sprawy przez `CaseID`
- Rozwiązanie: poprawa opisu funkcji

### Zadania

- **[Piotr Buczkowski]:** Sprawdzenie czy `CaseID` w `ForRow` jest faktycznie używane i czy ma sens → termin: do ustalenia
- **[Piotr Buczkowski]:** Poprawa opisu funkcji `ForRow` → termin: do ustalenia

### Punkty otwarte

- Czy `CaseID` w `ForRow` jest faktycznie używane i czy ma sens?
- Czy to jest kolejny przykład robienia czegoś "po linii najmniejszego oporu" bez przemyślenia?

---

## 13. Token ważności – problem z wyliczaniem daty

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`

### Kontekst i Problem

Jeśli dzisiaj o 1:00 ustawię token ważny na 1 dzień, to ustawia mi, że jest ważny do końca jutrzejszego dnia (do końca dzisiejszego dnia powinno zostawić). Problem polega na tym, że przy sprawdzaniu ważności tokenu nie jest uwzględniana godzina – przez cały okres jest ważny, ale już nie powinno być po tej godzinie.

### Zidentyfikowane Ryzyka

- Token może być ważny dłużej niż powinien
- Nieprawidłowe wyliczanie daty ważności tokenu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Uwzględnienie godziny przy sprawdzaniu | Sprawdzanie czy czas nie minął (uwzględnienie godziny) | ✅ Wybrana – bardziej precyzyjne |
| Zapisywanie daty ważności do północy poprzedniego dnia | Zapisywanie że ważny do 25.09 00:00 (w przeszłości), ale sprawdzanie że nadal jest 25 wrzesień | ⏸️ Odroczona – może być mylące |

### Decyzja

**Status:** ✅ Zatwierdzone

Trzeba poprawić wyliczanie daty ważności tokenu tak, żeby uwzględniało godzinę. Albo przy zapisywaniu zapisywać datę ważności do północy (25.09 00:00), albo przy sprawdzaniu sprawdzać czy czas nie minął (uwzględnienie godziny).

**Szczegóły techniczne:**
- Problem: token ważny na 1 dzień ustawiony o 1:00 jest ważny do końca jutrzejszego dnia (powinien być ważny do końca dzisiejszego dnia)
- Rozwiązanie: uwzględnienie godziny przy sprawdzaniu ważności tokenu
- Alternatywa: zapisywanie daty ważności do północy poprzedniego dnia

### Zadania

- **[Piotr Buczkowski]:** Poprawa wyliczania daty ważności tokenu → termin: do ustalenia (może na ten sprint lub kolejny)

---

## 14. Kolejka maili – usuwanie maili z kolejki i wysyłanie wszystkich maili z procesu na wskazany adres

**Projekt:** `integracje/System-mailowy`

### Kontekst i Problem

Klienci testują nowe procesy i nie chcą, żeby maile wychodziły do użytkowników. Obecnie muszą usuwać maile z kolejki z poziomu bazy danych. Potrzebna jest możliwość:
1. Usuwania maili z kolejki z poziomu interfejsu (zakładka "Kolejka maili" w logach systemowych)
2. Wysyłania wszystkich maili z procesu na wskazany adres (jak w Webconie) – żeby sprawdzić czy mail wychodzi prawidłowo, bez konieczności dzwonienia do osoby "dostałaś maila?"

### Zidentyfikowane Ryzyka

- Brak możliwości usuwania maili z kolejki z poziomu interfejsu utrudnia testowanie procesów
- Brak możliwości przekierowania maili na testowy adres utrudnia weryfikację poprawności maili

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Usuwanie z interfejsu + przekierowanie na adres | Checkboxy do zaznaczania maili z opcją usunięcia + opcja wysyłania wszystkich maili z procesu na wskazany adres | ✅ Wybrana – obie funkcjonalności są potrzebne |
| Tylko usuwanie z interfejsu | Tylko możliwość usuwania maili z kolejki | ❌ Odrzucona – przekierowanie na adres też jest potrzebne (jak w Webconie) |
| Tylko przekierowanie na adres | Tylko opcja wysyłania wszystkich maili z procesu na wskazany adres | ❌ Odrzucona – usuwanie z interfejsu też jest potrzebne |

### Decyzja

**Status:** ✅ Zatwierdzone

Zostaną wprowadzone dwie funkcjonalności:
1. **Usuwanie maili z kolejki z poziomu interfejsu** – checkboxy do zaznaczania maili w zakładce "Kolejka maili" (w logach systemowych) z opcją usunięcia. Obsługa zaznaczania Shiftem (pierwszy i ostatni – wszystko pomiędzy) i zaznaczania wszystkiego.
2. **Wysyłanie wszystkich maili z procesu na wskazany adres** – opcja w ustawieniach procesu (lub systemowych) do przekierowania wszystkich maili z procesu na wskazany adres e-mail (podobnie jak w Webconie). Mail idzie na wskazany adres, ale w tytule widać do kogo miał być wysłany (np. "Wyszło do Łukasza Bota").

**Szczegóły techniczne:**
- Zakładka "Kolejka maili" w logach systemowych (przekładana na React)
- Checkboxy do zaznaczania maili
- Opcja usunięcia zaznaczonych maili
- Zaznaczanie Shiftem (pierwszy i ostatni – wszystko pomiędzy)
- Zaznaczanie wszystkiego
- Opcja przekierowania wszystkich maili z procesu na wskazany adres (w ustawieniach procesu lub systemowych)
- Mail idzie na wskazany adres, ale w tytule widać do kogo miał być wysłany

### Zadania

- **[Kamil Dubaniowski]:** Dodanie checkboxów do zaznaczania maili z opcją usunięcia w zakładce "Kolejka maili" → termin: do ustalenia
- **[Kamil Dubaniowski]:** Dodanie opcji przekierowania wszystkich maili z procesu na wskazany adres → termin: do ustalenia

### Punkty otwarte

- Czy opcja przekierowania maili powinna być w ustawieniach procesu czy w ustawieniach systemowych?
- Czy opcja przekierowania maili powinna działać tylko dla środowiska testowego, czy też dla produkcyjnego?

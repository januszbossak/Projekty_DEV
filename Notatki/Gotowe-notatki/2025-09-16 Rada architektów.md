# Rada Architektów – 2025-09-16

**Powiązane projekty:**
- `moduly/Edytor-procesow-formularzy` – tematy 1
- `backlog` – temat 2
- `moduly/Trust-Center` – temat 3
- `cross-cutting/Usuwanie-spraw-powiazanych` – temat 4
- `cross-cutting/Komunikaty-systemowe` – temat 5
- `cross-cutting/Bezpieczenstwo-sesji` – temat 6
- `cross-cutting/Wydajnosc` – temat 7

---

## 1. Edytor formularza – pola puste i placeholdery

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Mateusz Kołakowski zgłosił problem z polami pustymi w edytorze formularza. Pola puste są używane przez konsultantów do sterowania uprawnieniami i zachowania układu formularza przy ukrywaniu pól. Problem polega na tym, że:
- Backend aktualnie nie zwraca pól pustych (endpoint wymaga poprawki)
- Nie można zarządzać uprawnieniami do pól pustych/placeholderów
- Nie można ukryć pola pustego na określonych etapach procesu
- W trybie przejścia między listą a edytorem kolumny układu nie są zapamiętywane (3 kolumny znikają, pojawiają się 2)

Konsultanci używają pól pustych jako "zapasowych miejsc" – gdy ukrywają pole na jakimś etapie, pole puste zajmuje jego miejsce, aby inne pola nie przeskakiwały między wierszami.

### Zidentyfikowane Ryzyka

- Zmiana logiki pól pustych może popsuć setki istniejących formularzy w wielu wdrożeniach
- Wprowadzenie nowej logiki bez zachowania kompatybilności wstecznej spowoduje konieczność ręcznej migracji wszystkich formularzy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie typu "pole puste" na liście pól po lewej stronie | Wyświetlanie pól pustych jako jawnych elementów formularza, możliwość ich usuwania i przesuwania | ⏸️ Odroczona – wymaga poprawki Backendu i może być zbyt skomplikowane dla MVP |
| Pozostawienie obecnej logiki | Zachowanie obecnego zachowania z placeholders | ✅ Wybrana dla MVP – bezpieczne rozwiązanie, nie psuje istniejących formularzy |
| Nowa logika z wierszami/grupami pól | Traktowanie formularza jako wierszy, pola nie przeskakują między wierszami | ⏸️ Odroczona – wymaga wielu spotkań i przemyślenia, nie na MVP |
| Grupy pól jako alternatywa | Wyświetlanie jednego z pól z grupy, możliwość ukrycia obu | ⏸️ Odroczona – koncepcja do rozważenia w przyszłości |

### Decyzja

**Status:** ✅ Zatwierdzone

Dla wersji MVP (czerwcowej) pozostawiamy obecną logikę pól pustych bez zmian. Jest to zaawansowane wymaganie, które wymaga przemyślenia i nie powinno być wprowadzane w pośpiechu.

**Szczegóły techniczne:**
- Backend nie zwraca obecnie pól pustych (endpoint wymaga poprawki)
- Placeholdery są obecnie tylko na frontendzie
- Problem z zapamiętywaniem kolumn układu (3 kolumny → 2 kolumny) wymaga poprawki

### Zadania

- **Przemek:** Poprawić zapamiętywanie kolumn układu formularza przy przejściu między listą a edytorem (zgłoszenie Mateusza Kołakowskiego)
- **Kamil:** Poinformować Przemka i Mateusza Kołakowskiego o decyzji pozostawienia obecnej logiki dla MVP

### Punkty otwarte

- Jak w przyszłości obsłużyć pola puste w nowej logice z wierszami/grupami pól?
- Czy potrzebny będzie przełącznik między starą a nową logiką formularza?
- Jak zapewnić migrację istniejących formularzy do nowej logiki?

---

## 2. Zgłaszanie błędów – kanały komunikacji i opiekun tematu

**Projekt:** `backlog`

### Kontekst i Problem

Piotr Buczkowski zgłosił pytanie o właściwy kanał zgłaszania błędów i niedogodności (np. problem z podmianą literki w nazwie pola). Obecnie brakuje jasnych wytycznych:
- Gdzie zgłaszać błędy: Teams vs Backlog?
- Kto jest odpowiedzialny za walidację zgłoszeń?
- Jak unikać duplikacji zgłoszeń (np. 3 te same tematy w ciągu 2 tygodni)?

Problem: bez dedykowanego opiekuna tematu trudno jest śledzić, co już było zgłoszone, co jest w trakcie obsługi, a co jest świadomym błędem w MVP.

### Zidentyfikowane Ryzyka

- Brak centralnego miejsca zgłaszania powoduje rozproszenie informacji
- Duplikacja zgłoszeń prowadzi do marnowania czasu zespołu
- Brak walidacji powoduje, że zgłoszenia mogą być nieprawidłowo priorytetyzowane

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zgłaszanie na Backlog z opiekunem tematu | Zgłoszenia na Backlog, ale zawsze przypisane do opiekuna tematu (np. Kamil dla edytora procesów) | ⏸️ Odroczona – wymaga konfiguracji i może być niewygodne dla wielu osób |
| Zgłaszanie na kanał Teams projektu | Zgłaszanie błędów na dedykowany kanał Teams dla danego projektu (np. "Edytor procesów", "Moduł raportowy") | ✅ Wybrana – prostsze rozwiązanie, łatwiejsze w użyciu |
| Work Item Generator w Azure DevOps | Wykorzystanie funkcji Microsoft do wykrywania podobnych zgłoszeń podczas tworzenia | ⏸️ Odroczona – wymaga konfiguracji, do sprawdzenia |

### Decyzja

**Status:** ✅ Zatwierdzone

Zgłoszenia błędów należy kierować na odpowiedni kanał Teams dla danego projektu. Kanały Teams powinny być przeglądane przez 3 osoby:
- Delivery Manager (Damian, Kamil lub Łukasz)
- Deweloper odpowiedzialny za projekt
- Tester odpowiedzialny za projekt

Te osoby są odpowiedzialne za:
- Odpowiedź na pytanie "czy to już jest zgłoszone?"
- Walidację czy zgłoszenie nadaje się na bug
- Informowanie czy nad tym już pracujemy lub jest rozwiązane w nowszej wersji
- Ewentualne przekierowanie do zgłoszenia na Backlog, jeśli wymagane

**Szczegóły techniczne:**
- Istniejące kanały: Pentesty, Moduł raportowy, Forma, Nowy X sprawy
- Możliwość dodania nowych kanałów w razie potrzeby

### Zadania

- **Wszyscy:** Zgłaszać błędy na odpowiedni kanał Teams projektu (np. "Edytor procesów" dla błędów edytora)
- **Delivery Managerzy:** Przeglądać kanały Teams i odpowiadać na zgłoszenia

### Punkty otwarte

- Czy Work Item Generator w Azure DevOps może pomóc w wykrywaniu duplikacji zgłoszeń?
- Jak zapewnić, że zgłoszenia nie będą zalegać, gdy opiekun jest nieobecny?

---

## 3. Trust Center – bezpieczeństwo nazw plików w powiadomieniach

**Projekt:** `moduly/Trust-Center`

### Kontekst i Problem

Radek Szczerski (IOD) zgłosił problem z bezpieczeństwem danych osobowych w nazwach plików przesyłanych przez SMS/Email w Trust Center. Przykład: nazwa pliku "Umowa z Łukasz Bott" może zawierać dane osobowe, które nie powinny być przesyłane w powiadomieniach.

Obecnie Trust Center używa "przyjaznej nazwy dokumentu" w mailach, ale nie w SMS-ach. Pole "przyjazna nazwa dokumentu" jest konfigurowane przez konsultantów w procesie i powinno być używane zarówno w mailach, jak i SMS-ach.

### Zidentyfikowane Ryzyka

- Przesyłanie danych osobowych w nazwach plików może prowadzić do wycieku danych
- Brak kontroli nad treścią nazw plików w powiadomieniach SMS
- Ryzyko incydentu bezpieczeństwa danych (na szczęście dotychczas nie doszło do incydentu)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Użycie przyjaznej nazwy dokumentu w SMS-ach | Zmiana w Trust Center, aby używać przyjaznej nazwy dokumentu (o ile jest zdefiniowana) zarówno w mailach, jak i SMS-ach | ✅ Wybrana – najprostsze rozwiązanie, wykorzystuje istniejące pole |
| Automatyczne skracanie nazw plików | Skracanie nazw plików do pierwszych kilku liter, kropek i ostatnich kilku liter (np. "Um...ott") | ❌ Odrzucona – rozwiązanie systemowe myślące za użytkownika, lepiej dać kontrolę konsultantom |
| Wykrywanie danych osobowych w nazwach | Biblioteka Python do wykrywania imion i nazwisk w przyjaznej nazwie dokumentu z sugestią usunięcia | ⏸️ Odroczona – możliwa do rozważenia w przyszłości jako funkcja pomocnicza |

### Decyzja

**Status:** ✅ Zatwierdzone

Zmieniamy Trust Center tak, aby używać "przyjaznej nazwy dokumentu" w SMS-ach (tak jak obecnie w mailach), o ile jest ona zdefiniowana. Konsultanci są odpowiedzialni za zapewnienie, że przyjazna nazwa dokumentu nie zawiera danych osobowych.

**Szczegóły techniczne:**
- Endpoint Trust Center ma pole "przyjazna nazwa dokumentu"
- Obecnie używane w mailach, należy dodać użycie w SMS-ach
- Weryfikacja przez Marka czy obecnie już tak działa (według Damiana powinno działać)

### Zadania

- **Łukasz Bott:** Dopytanie Marka o potwierdzenie, że przyjazna nazwa dokumentu jest używana w SMS-ach (o ile jest zdefiniowana)
- **Łukasz Bott:** Zwrócenie uwagi konsultantom na piątkowym spotkaniu o właściwe używanie przyjaznej nazwy dokumentu (bez danych osobowych)
- **Łukasz Bott:** Dodanie wytycznych do dokumentacji Trust Center o zaleceniu unikania danych osobowych w przyjaznej nazwie dokumentu

### Punkty otwarte

- Czy potrzebne jest dodatkowe rozwiązanie dla klientów On-Premise korzystających z Trust Center bezpośrednio (z pominięciem AMODIT)?

---

## 4. DeleteCase – problem z usuwaniem spraw nadrzędnych z aktywnymi podrzędnymi

**Projekt:** `cross-cutting/Usuwanie-spraw-powiazanych`

### Kontekst i Problem

Hubert zgłosił problem z usuwaniem spraw nadrzędnych posiadających aktywne sprawy podrzędne połączone relacją Connected Cases. Problem występuje gdy:
- Sprawa podrzędna ma `isHidden = true` (oznaczona jako usunięta)
- Sprawa nadrzędna próbuje usunąć sprawę podrzędną przez For Each na Connected Cases
- Sprawy ukryte nie są pobierane do kolekcji Connected Cases
- Referencja pozostaje w bazie danych i przy próbie DeleteCase baza zwraca błąd

### Zidentyfikowane Ryzyka

- Nie można usunąć sprawy nadrzędnej, jeśli ma ukryte sprawy podrzędne
- Błąd bazy danych przy próbie usunięcia

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Obsługa sytuacji z ukrytymi sprawami podrzędnymi | Poprawka logiki DeleteCase, aby obsługiwała odczepianie od ukrytych spraw podrzędnych | ✅ Wybrana – Piotr wie jak to zrobić |
| Komunikat o niemożności usunięcia | Wyświetlenie komunikatu, że nie można usunąć sprawy nadrzędnej z podpiętymi sprawami podrzędnymi | ❌ Odrzucona – sprawy ukryte powinny być odczepiane |

### Decyzja

**Status:** ✅ Zatwierdzone

Trzeba obsłużyć sytuację z ukrytymi sprawami podrzędnymi w logice DeleteCase. Piotr wie jak to zrobić i opisze rozwiązanie.

**Szczegóły techniczne:**
- Sprawy ukryte (`isHidden = true`) nie są pobierane do kolekcji Connected Cases
- For Each na Connected Cases nie odczepia od ukrytych spraw
- Referencja pozostaje w bazie danych i blokuje DeleteCase

### Zadania

- **Piotr Buczkowski:** Opisanie rozwiązania problemu z usuwaniem spraw nadrzędnych z ukrytymi sprawami podrzędnymi
- **Łukasz Bott:** Przypisanie zadania do Piotra na kolejny sprint (lub Piotr zdejmie z siebie, jeśli opisze i komuś się rozpisze)

### Punkty otwarte

- Czy to jest przypadek do dyskusji na Radzie Architektów, czy wystarczy opisanie rozwiązania?

---

## 5. Komunikaty systemowe (Failover) – wyświetlanie dla klientów On-Premise

**Projekt:** `cross-cutting/Komunikaty-systemowe`

### Kontekst i Problem

Mateusz zgłosił potrzebę wyświetlania komunikatów o awarii/statusie bazy danych dla klientów On-Premise (Rossmann, LPP). Obecnie mechanizm komunikatów systemowych działa tylko dla klientów chmurowych:
- Istnieje baza danych WAM (organizacji), która jest oddzielna od bazy danych ze sprawami
- W bazie WAM jest tabela z wiadomościami
- Komunikaty są wyświetlane gdy nie ma dostępu do bazy danych AMODIT lub gdy nie można się połączyć z bazą danych
- Komunikaty powinny się pojawiać przy logowaniu i w top menu (pasek z użytkownikiem i logiem)

Problem: po przejściu na React nie wiadomo, czy te funkcje zostały zachowane. Dla klientów On-Premise nie ma dostępu do bazy WAM.

### Zidentyfikowane Ryzyka

- Brak możliwości informowania klientów On-Premise o planowanych przerwach w działaniu systemu
- Klienci nie są informowani o problemach z bazą danych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wycenienie funkcjonalności dla klientów On-Premise | Wycena i uzyskanie finansowania od klientów (Rossmann, LPP, potencjalnie Orlen) przed implementacją | ✅ Wybrana – funkcjonalność nie jest na roadmapie, wymaga finansowania |
| Wykorzystanie istniejącego mechanizmu powiadomień | Dodanie możliwości oznaczenia powiadomienia jako "systemowe", które wyświetla się w headerze | ⏸️ Odroczona – do rozważenia po wycenieniu |
| Prosty interfejs w ustawieniach systemowych | Dodanie pola "Komunikat systemowy" w ustawieniach systemowych (podobnie jak komunikaty na stronie logowania) | ⏸️ Odroczona – do rozważenia po wycenieniu |
| Popup przy logowaniu | Wyświetlanie popupu z komunikatem systemowym przy pierwszym logowaniu | ⏸️ Odroczona – do rozważenia po wycenieniu |
| Pasek na górze (jak w mBanku) | Czerwony pasek na górze strony z komunikatem krytycznym | ⏸️ Odroczona – do rozważenia po wycenieniu |

### Decyzja

**Status:** ✅ Zatwierdzone

Funkcjonalność wyświetlania komunikatów systemowych dla klientów On-Premise wymaga wyceny i uzyskania finansowania od klientów (Rossmann, LPP, potencjalnie Orlen) przed rozpoczęciem prac. Nie jest to funkcjonalność na roadmapie i wynika z potrzeb klientów.

Dla klientów chmurowych: należy sprawdzić czy mechanizm komunikatów został zachowany po przejściu na React i ewentualnie go przywrócić.

**Szczegóły techniczne:**
- Baza danych WAM (organizacji) jest dostępna tylko dla klientów chmurowych
- Tabela z wiadomościami w bazie WAM
- Komunikaty wyświetlane przy logowaniu i w top menu (pasek z użytkownikiem)
- Po przejściu na React nie wiadomo, czy funkcje zostały zachowane

### Zadania

- **Damian Kamiński:** Wycenienie funkcjonalności dla klientów On-Premise i uzyskanie finansowania
- **Damian Kamiński:** Sprawdzenie czy mechanizm komunikatów został zachowany po przejściu na React dla klientów chmurowych
- **Łukasz Bott:** Przypisanie zadania do Damiana

### Punkty otwarte

- Jak powinien wyglądać interfejs do zarządzania komunikatami systemowymi dla klientów On-Premise?
- Czy wykorzystać istniejący mechanizm powiadomień z oznaczeniem "systemowe"?
- Czy potrzebny jest interfejs w ustawieniach systemowych czy popup przy logowaniu?

---

## 6. Problem z wylogowywaniem – synchronizacja między kartami przeglądarki

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`

### Kontekst i Problem

Piotr Buczkowski zgłosił problem z synchronizacją wylogowania między kartami w przeglądarce (zgłoszenie 21974). Problem:
- Gdy użytkownik ma 2 zakładki otwarte i wyloguje się w jednej, druga zakładka nie odświeża swojego stanu
- W drugiej zakładce pozostaje widoczny interfejs aplikacji, ale sesja jest nieaktywna
- Każda kolejna akcja w drugiej zakładce powoduje błąd
- Problem został wytknięty w pentestach jako problem bezpieczeństwa

### Zidentyfikowane Ryzyka

- **Krytyczny problem bezpieczeństwa** – wylogowanie w jednej zakładce nie kończy sesji w innych
- Możliwość kontynuowania pracy w nieaktywnej sesji
- Problem zgłoszony w pentestach

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Naprawa jako hotfix w bieżącym sprincie | Natychmiastowa naprawa problemu przed wydaniem nowej wersji | ✅ Wybrana – krytyczny problem bezpieczeństwa, nie można wydawać z dziurami bezpieczeństwa |
| Odłożenie na kolejny sprint | Naprawa w kolejnym sprincie | ❌ Odrzucona – problem bezpieczeństwa wymaga natychmiastowej naprawy |

### Decyzja

**Status:** ✅ Zatwierdzone

Problem ma **najwyższy priorytet** i musi zostać naprawiony jako hotfix w bieżącym sprincie, przed opublikowaniem nowej wersji. Nie można wydawać rzeczy z potencjalnymi dziurami bezpieczeństwa.

**Szczegóły techniczne:**
- Licznik odliczania do wylogowania został zaimplementowany przez Przemka
- Problem dotyczy synchronizacji wylogowania między kartami
- W starym rozwiązaniu wylogowanie w jednej karcie powodowało wylogowanie we wszystkich kartach
- W nowym rozwiązaniu Reactowym synchronizacja nie działa poprawnie

### Zadania

- **Janusz Bossak:** Pilnie przypisać zadanie naprawy (na podstawie zgłoszenia 21974) do Przemka jako hotfix
- **Kamil Dubaniowski:** Przekazanie informacji Przemkowi o problemie
- **Przemek:** Naprawa synchronizacji wylogowania między kartami przeglądarki

### Punkty otwarte

- Czy problem dotyczy tylko klientów On-Premise, czy również chmurowych?

---

## 7. Analiza wydajności bazy danych – zgłoszenie klienta

**Projekt:** `cross-cutting/Wydajnosc`

### Kontekst i Problem

Klient zdecydował się po 2 miesiącach od oferty na analizę bazy danych. Chce wykupić 2 dni Time & Material na analizę, dlaczego wolno działa baza danych:
- Niektóre reguły wykonują się po półtorej minuty
- Baza danych jest mocno obciążona
- Klient czekał 2 miesiące na odpowiedź

### Zidentyfikowane Ryzyka

- Brak wiedzy o przyczynie problemu może prowadzić do dalszych problemów z wydajnością
- Klient czekał długo na odpowiedź, co może wpłynąć na relacje

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Analiza przez Piotra z wsparciem Łukasza Grodzkiego | Piotr przeprowadza analizę z Łukaszem Grodzkim, aby ten nabrał wiedzy i był potencjalnym zastępcą | ✅ Wybrana – pozwala na przekazanie wiedzy i zapewnia wsparcie |
| Analiza tylko przez Piotra | Piotr sam przeprowadza analizę | ❌ Odrzucona – lepiej mieć wsparcie i przekazać wiedzę |

### Decyzja

**Status:** ✅ Zatwierdzone

Piotr przeprowadzi analizę wydajności bazy danych z wsparciem Łukasza Grodzkiego. Analiza ma na celu:
- Zidentyfikowanie przyczyn wolnego działania bazy danych
- Sprawdzenie czy monitor wydajności był uruchomiony
- Przygotowanie wniosków i wyceny ewentualnych poprawek

**Szczegóły techniczne:**
- 2 dni Time & Material na analizę
- Klient On-Premise
- Daniel jest opiekunem klienta i zna temat
- Po analizie: wnioski i wycena ewentualnych poprawek (systemowych lub procesowych)

### Zadania

- **Damian Kamiński:** Wywołanie Piotra i prośba o kontakt z Danielem w celu ustalenia terminu analizy
- **Piotr Buczkowski:** Ustalenie terminu analizy z Danielem i przeprowadzenie analizy z Łukaszem Grodzkim
- **Daniel:** Ustalenie terminu z Piotrem i przekazanie informacji o problemie

### Punkty otwarte

- Czy monitor wydajności był uruchomiony u klienta?
- Czy problem jest systemowy czy procesowy (konfiguracja procesów)?
- Jakie są konkretne reguły, które wykonują się po półtorej minuty?


# Sprint Review – 2025-09-22

**Sprint:** [nie sprecyzowano]
**Okres:** [nie sprecyzowano]

**Powiązane projekty:**
- `moduly/Edytor-procesow-formularzy` – temat 1
- `moduly/Raporty-systemowe` – temat 2
- `koncepcje/Security-Checklist` – temat 3
- `moduly/Trust-Center` – temat 4
- `cross-cutting/Bezpieczenstwo-sesji` – tematy 5, 6
- `cross-cutting/Interfejs-sprawy` – temat 7

---

## 1. Matryca uprawnień – rozszerzenia i usprawnienia

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Cel biznesowy

Rozwinięcie matrycy uprawnień ponad MVP, aby ułatwić konfigurację uprawnień dla dużych procesów z wieloma etapami i polami. Poprawa wydajności i czytelności interfejsu konfiguracji uprawnień.

### Co zaimplementowano

- **Tryb kompaktowy** – obrócenie napisów w kolumnach, aby kolumny były węższe (sugestia Przemka)
- **Usunięcie selecta** – zastąpienie selecta ikonkami z tooltipem po najechaniu, co znacznie poprawiło wydajność ładowania matrycy
- **Nowa nawigacja** – docelowa nawigacja między zakładkami (matryca, lista, edytor graficzny)
- **Zmiana ikony** – ikona tarczy zamiast matrycy, bardziej kojarzy się z uprawnieniami
- **Filtry po etapach** – możliwość ograniczenia widoku tylko do wybranych etapów (minimum jeden etap musi być zaznaczony)
- **Uprawnienie domyślne** – możliwość ustawienia domyślnego uprawnienia dla pola, które dziedziczą wszystkie etapy bez wyjątków
- **Wizualizacja wyjątków** – gwiazdka obok nazwy uprawnienia oznacza, że na danym etapie jest wyjątek (nie można zmienić przez zmianę uprawnienia domyślnego)
- **Zmiana masowa uprawnień** – możliwość zaznaczenia wielu pól i zmiany uprawnień dla wybranych etapów
- **Wycinanie niepotrzebnych elementów** – dla dużych procesów wycinane są niepotrzebne elementy, aby skupić się na konfiguracji

### Jak to działa (jeśli omówiono)

- Uprawnienie domyślne jest dziedziczone przez wszystkie etapy, które nie mają ustawionych wyjątków
- Na matrycy pokazywane są realne uprawnienia (nie napis "domyślne"), ale jeśli domyślne jest ukryte, a pole nie ma wyjątków, to na wszystkich etapach ustawia się to domyślne
- Gwiazdka obok uprawnienia oznacza wyjątek dla etapu – zmiana uprawnienia domyślnego nie wpłynie na te etapy
- Tooltip po najechaniu pokazuje szczegóły: "wyjątek dla etapu: odczyt" lub "domyślne: edycja"
- Dziedziczenie może być z nadrzędnej sekcji lub z tabeli (w drugą stronę)

### Ograniczenia / Known issues

- Po odświeżeniu raportu mogą się zdublować kolumny (znany problem, wymaga uwagi)
- Wizualizacja dziedziczenia i wyjątków może być nieczytelna przy wielu ikonkach (3 ikony w jednym polu: ikona uprawnienia, gwiazdka, łańcuch dziedziczenia)
- Brak filtrowania po nazwach pól/sekcjach (tylko po etapach)
- Nazwy pól są techniczne, nie wyświetlane (może być problem przy zgłoszeniach serwisowych)

### Feedback z demo

- **Przemysław Sołdacki:** Sugestia odwrócenia logiki wizualizacji – jeśli jest dziedziczone, to nic nie ma, a jeśli jest wyjątek, to żeby było łatwo widoczne (np. rozerwany łańcuch na pomarańczowo/czerwono, lub tło wskazujące zmianę)
- **Piotr Buczkowski:** Podobny pomysł – najczęstsza sytuacja to ustawienie uprawnień ogólnych, a później wyjątki dla szczególnych pól/sekcji
- **Damian Kamiński:** Przy wielu wyjątkach może powstać "szachownica" – warto skonsultować z wdrożeniowcami
- **Przemysław Sołdacki:** Możliwość dodania search, który filtrowałby po sekcjach, polach i etapach (lub tylko po polach)
- **Daniel Reszka:** Problem z nazwami technicznymi – przy zgłoszeniach serwisowych trzeba szukać na innym widoku, żeby znaleźć które to pole
- **Przemysław Sołdacki:** Przełącznik między nazwami wyświetlanymi a technicznymi powinien być globalny (na pasku z zakładkami), nie tylko w edytorze graficznym
- **Daniel Reszka:** Obecnie można użyć CTRL+F i wyszukać nazwę po wszystkich językach naraz – po wprowadzeniu przełącznika trzeba będzie przełączać między językami
- **Damian Kamiński:** W checkboxach zmiany masowej brakuje opcji "pozostaw bez zmian" – obecnie jest tylko "wybierz uprawnienie", co może być mylące

### Dalsze kroki

- Konsultacja z wdrożeniowcami dotycząca wizualizacji dziedziczenia i wyjątków (możliwe spotkanie w piątek o 15:00)
- Rozważenie kilku wariantów wizualnych (nie działających, tylko wizualnych) do wyboru najlepszego
- Dodanie search, który będzie szukał po polach/sekcjach/etapach (lub tylko po polach)
- Przeniesienie przełącznika nazw (wyświetlane/techniczne) na globalny pasek z zakładkami
- W checkboxach zmiany masowej: dodanie opcji "pozostaw bez zmian" lub "nie zmieniaj" zamiast "wybierz uprawnienie"
- Rozważenie pokazywania nazwy technicznej w nawiasie obok wyświetlanej (jeśli ustawione wyświetlane) lub w tooltipie
- Uwzględnienie poziomu wiersza (etapy też mają kontekst wyświetlanych/technicznych nazw)

---

## 2. Raporty systemowe – nowe podejście do prezentacji

**Projekt:** `moduly/Raporty-systemowe`

### Cel biznesowy

Zmiana podejścia do prezentacji raportów systemowych ze względu na dużą ilość raportów w starej technologii, które nie były czytelne. Poprawa wydajności i czytelności poprzez wykorzystanie dashboardów i optymalizację źródeł danych.

### Co zaimplementowano

- **Podejście zakładkowe** – wykorzystanie dashboardów dla poszczególnych grup raportów systemowych
- **Źródła danych w trybie local** – część źródeł danych dla raportów systemowych została przełączona na tryb local (agregaty w zapytaniu, przeliczane raz dziennie)
- **Domyślne wartości filtrów** – możliwość ustawienia domyślnej wartości filtra dla raportu (np. poprzednie 7 dni dla daty)
- **Wymagane filtry** – jeśli wartość domyślna jest ustawiona jako wymagana, raport nie wyświetli danych dopóki nie wprowadzimy wartości w filtrze
- **Przeliczanie agregatów** – agregaty są przeliczane raz dziennie (w środowisku deweloperskim w dowolnych godzinach, docelowo w godzinach nocnych)

### Jak to działa (jeśli omówiono)

- Źródła danych w trybie local mają agregaty w zapytaniu, które są przeliczane raz na dobę
- Domyślna wartość filtra jest ustawiana przez administratora raportu w konfiguracji raportu
- Użytkownik może zmienić wartość filtra, ale musi wskazać ograniczenie (nie może wyświetlić wszystkich danych bez filtra)
- To odwraca sytuację – wcześniej raport wyświetlał wszystkie dane i trzeba było włączać filtrowanie, teraz raport wymaga wskazania filtru przed wyświetleniem

### Ograniczenia / Known issues

- Po odświeżeniu raportu mogą się zdublować kolumny (znany problem)
- Część źródeł może pozostać w trybie online (nie wszystkie będą w trybie local)
- Dane spływają raz dziennie, więc nie są aktualne na bieżąco

### Feedback z demo

- **Daniel Reszka:** Pytanie o zakres przechowywania danych wstecz – odpowiedź: to nie wpływa na ilość przechowywanych danych, tylko na prezentację (musisz wskazać ograniczenie)
- **Daniel Reszka:** Obawa o możliwość wskazania 1000 dni wstecz – odpowiedź: można, ale po to są domyślne wartości, żeby od razu mieć załadowane 7 dni, a nie klikać 1000
- **Daniel Reszka:** Obawa o wpływ na system przy dużych zakresach danych – odpowiedź: to ma wpływ na cały system, jeśli raport generuje długie zapytanie

### Dalsze kroki

- Ujednolicenie tłumaczeń dla źródeł danych (część po polsku, część po angielsku) – w najbliższym sprincie
- Możliwość nadania aliasu dla kolumn w raporcie (szczególnie przy agregacjach) – podejście od strony źródeł zewnętrznych
- Możliwość ustawienia wersji językowej (aliasu) dla kolumn w źródłach zewnętrznych
- Ustalenie godzin przeliczania agregatów (docelowo w godzinach nocnych)

---

## 3. AMODIT Security Checklist

**Projekt:** `koncepcje/Security-Checklist`

### Cel biznesowy

Stworzenie listy kontrolnej bezpieczeństwa (Security Checklist) dla instancji AMODIT instalowanych u klientów, szczególnie dla klientów dostarczających pen testy. Ma to być glejt potwierdzający, że zabezpieczenia zostały wprowadzone lub że nie zostały wprowadzone z uzasadnieniem (np. nie mają zastosowania w danej instancji).

### Co zaimplementowano

- **Checklist bezpieczeństwa** – lista kontrolna oparta na wytycznych z Wiki dotyczących zabezpieczenia aplikacji webowych AMODIT
- **Wymaganie przed oddaniem produkcyjnym** – przed oddaniem produkcyjnym kierownik wdrożenia po stronie Astrafox i kierownik wdrożenia po stronie klienta muszą podpisać się pod checklistą
- **Świadomość obu stron** – obie strony są świadome, jakie zabezpieczenia zostały wprowadzone lub nie zostały wprowadzone i dlaczego

### Jak to działa (jeśli omówiono)

Checklist będzie wymagany przed wykonaniem pen testów, aby uniknąć powtarzania wprowadzania zabezpieczeń, które już są opisane i powinny być wprowadzone. Ma to zapobiec sytuacjom, gdy ta sama luka bezpieczeństwa wraca jak bumerang, bo ktoś nie wprowadził zabezpieczenia, które już jest dawno opisane.

### Ograniczenia / Known issues

- [Brak znanych ograniczeń w transkrypcji]

### Feedback z demo

- [Brak feedbacku w transkrypcji]

### Dalsze kroki

- Finalizacja checklisty bezpieczeństwa
- Wdrożenie procesu podpisywania checklisty przed oddaniem produkcyjnym

---

## 4. Trust Center – logowanie OAuth przez Microsoft dla serwisu

**Projekt:** `moduly/Trust-Center`

### Cel biznesowy

Usprawnienie działań serwisu i administratorów organizacji poprzez umożliwienie logowania się do panelu administracyjnego dokumentu za pomocą OAuth przez Microsoft, bez konieczności wpisywania wszystkich e-maili pracowników jako administratorów w każdej organizacji.

### Co zaimplementowano

- **Logowanie OAuth przez Microsoft** – możliwość logowania się na adres e-mail, jeżeli jest on podany jako e-mail serwisowy
- **Globalna pula serwisantów** – zamiast wpisywania e-maila do każdej organizacji osobno, e-mail jest wpisany w jedną tabelę w Trust Center
- **Weryfikacja uprawnień** – sprawdzanie czy dany e-mail jest zarejestrowany jako e-mail serwisowy przed umożliwieniem wejścia

### Jak to działa (jeśli omówiono)

- Pobierane są dane na temat adresu e-mail z Microsoft OAuth
- Sprawdzany jest czy dany e-mail jest zarejestrowany jako e-mail serwisowy w Trust Center
- Jeżeli tak, użytkownik ma możliwość wejścia do dokumentu (musi mieć link do sprawy)
- Użytkownik może wykonać te same czynności co zwykły administrator: wysłać powiadomienie (jeśli pozwala na to dokument), użyć edytora

### Ograniczenia / Known issues

- Dostęp jest globalny dla wszystkich organizacji (jeśli jesteś wpisany jako serwisant, masz dostęp do wszystkich organizacji)
- Musisz mieć link do sprawy, żeby wejść do dokumentu (nie możesz przeglądać wszystkich dokumentów)
- Kontrola dostępu jest po stronie Trust Center (Daniel musi się zgłosić do Marka, żeby dodać serwisantów)

### Feedback z demo

- **Łukasz Bott:** Pytanie o bezpieczeństwo danych i RODO – odpowiedź: jeśli ktoś ma dostęp do AMODIT, to i tak widzi dane; dokument musi być otwarty przez sprawę
- **Damian Kamiński:** Potwierdzenie, że dostęp jest kontrolowany – jeśli ktoś ma nie dostać dostępu, zostanie usunięty z tabeli
- **Marek Dziakowski:** Ułatwienie dla serwisu – często trzeba zaglądać do dokumentów, żeby zweryfikować problemy; teraz nie trzeba się wpisywać przez bazę i usuwać

### Dalsze kroki

- Kontrola puli serwisantów – pilnowanie, żeby to był ograniczony zbiór osób (sterowane przez Marka/Daniela)
- [Brak innych kroków w transkrypcji]

---

## 5. Strona wylogowania – przycisk logowania

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`

### Cel biznesowy

Usprawnienie interfejsu wylogowania poprzez dodanie przycisku logowania na stronie wylogowania, aby użytkownik mógł łatwo wrócić do strony logowania bez konieczności ręcznego preparowania linków.

### Co zaimplementowano

- **Przycisk logowania** – dodany napis "logowanie" na stronie wylogowania, po kliknięciu wraca na stronę główną
- **Intuicyjność** – zastąpienie logo (które mogło nie być intuicyjne lub nie wyświetlało się) wyraźnym napisem

### Jak to działa (jeśli omówiono)

Po wylogowaniu użytkownik widzi napis "logowanie", po kliknięciu wraca na stronę główną (stronę logowania).

### Ograniczenia / Known issues

- [Brak znanych ograniczeń w transkrypcji]

### Feedback z demo

- **Piotr Buczkowski:** Wcześniej było logo pod spodem, które działało – odpowiedź: nie wszędzie się wyświetlało, teraz jest wyraźny napis
- **Barbara Michałek:** Potwierdzenie, że logo nie wyświetlało się na stronie wylogowania

### Dalsze kroki

- [Brak dalszych kroków w transkrypcji]

---

## 6. Ujednolicenie logowania/wylogowania między starą technologią a Reactem

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`

### Cel biznesowy

Ujednolicenie zachowania logowania i wylogowania między starą technologią a Reactem, aby wylogowanie w jednej zakładce wylogowywało we wszystkich zakładkach, niezależnie na której stronie jesteś.

### Co zaimplementowano

- **Wylogowanie globalne** – wylogowanie w jednej zakładce wylogowuje we wszystkich zakładkach (współpraca z Przemkiem przez SIM)
- **Zachowanie przekierowania** – zachowanie ustawień przekierowania na stronę logowania lub na stronę logowania (w zależności od konfiguracji auto logowania przez providera)

### Jak to działa (jeśli omówiono)

Jeśli jest auto logowanie przez providera (np. Microsoft), to nie ma sensu wylogowywać na stronie logowania, bo użytkownik zostanie natychmiast zalogowany ponownie. System zachowuje odpowiednie przekierowanie w zależności od konfiguracji.

### Ograniczenia / Known issues

- [Brak znanych ograniczeń w transkrypcji]

### Feedback z demo

- [Brak feedbacku w transkrypcji]

### Dalsze kroki

- [Brak dalszych kroków w transkrypcji]

---

## 7. Ikony grup w interfejsie sprawy

**Projekt:** `cross-cutting/Interfejs-sprawy`

### Cel biznesowy

Wizualne rozróżnienie użytkowników od grup w interfejsie sprawy, aby było widoczne, które jest które.

### Co zaimplementowano

- **Ikony grup** – grupy mają białą ikonkę, użytkownicy mają czarny tekst
- **Kolor zgodny z zakładką "Do wykonania"** – ten sam mechanizm i kolory co w zakładce "Do wykonania"
- **Różne kolory grup** – grupy mogą mieć różne kolory (tak jak w zakładce "Do wykonania")

### Jak to działa (jeśli omówiono)

W informacji o sprawie grupy są oznaczone białą ikonką, użytkownicy czarnym tekstem. Kolory są takie same jak w zakładce "Do wykonania".

### Ograniczenia / Known issues

- **Ikonka może być większa** – ikonka może wydawać się większa od tekstu z 2 powodów: ikonka jest od krawędzi do krawędzi obrazem, a tekst ma literki ucięte (np. P); ikonka jest bardziej kwadratowa i może być nieco wyższa

### Feedback z demo

- **Piotr Buczkowski:** Pytanie dlaczego ikonka jest większa – odpowiedź: może wydawać się większa z powodu kształtu i ucięcia liter
- **Damian Kamiński:** Potwierdzenie, że kolory są różne dla różnych grup (tak jak w zakładce "Do wykonania")
- **Damian Kamiński:** Ważne, żeby to było spójne z komunikatorem (tam też pracują nad reprezentacją grup dla czatów grupowych)
- **Łukasz Bott:** 💭 Pomysł: możliwość wskazania ikonki per grupa, tak jak mamy możliwość wskazania ikony procesu
- **Damian Kamiński:** Nie jest to najbardziej krytyczne w tym momencie, ale może być kierunkiem rozwoju (może niekoniecznie ikonka, ale kolorystyka)

### Dalsze kroki

- Sprawdzenie i ewentualna korekta rozmiaru ikonki (może być nieco większa o 2 piksele)
- Po zakończeniu i przejściu wszystkich testów – powiadomienie Damiana (ma wpływ na komunikator)
- Rozważenie możliwości wskazania ikonki per grupa (na rozwój, nie krytyczne)

---

## 8. Komunikator – poprawki (nie prezentowane)

**Projekt:** `klienci/WIM/Komunikator`

### Cel biznesowy

Poprawki do komunikatora przed prezentacją wersji ostatecznej/stabilnej.

### Co zaimplementowano

- **Kilka kluczowych elementów wizualnych** – poprawki w trakcie realizacji
- **Kilkanaście zgłoszeń zrealizowanych** – około 3-4 zgłoszenia jeszcze otwarte

### Jak to działa (jeśli omówiono)

[Nie omówiono szczegółów, nie prezentowano]

### Ograniczenia / Known issues

- Nie prezentowano wersji ostatecznej – jeszcze kilka kluczowych elementów wizualnych do poprawy
- Około 3-4 zgłoszenia jeszcze otwarte

### Feedback z demo

- [Nie prezentowano]

### Dalsze kroki

- Dokończenie poprawki elementów wizualnych
- Zamknięcie pozostałych 3-4 zgłoszeń
- Prezentacja wersji stabilnej (prawdopodobnie jeszcze w tym tygodniu)

---

## 9. Edytor formularza graficznego – korekty

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Cel biznesowy

Korekty i usprawnienia w edytorze formularza graficznego.

### Co zaimplementowano

- **Korekty** – różne korekty i usprawnienia (nie sprecyzowano szczegółów w transkrypcji)

### Jak to działa (jeśli omówiono)

[Nie omówiono szczegółów]

### Ograniczenia / Known issues

- [Brak znanych ograniczeń w transkrypcji]

### Feedback z demo

- **Przemysław Sołdacki:** Pytanie kiedy nowy edytor będzie dostępny – odpowiedź: w czerwcowej wersji, która teraz jest stabilizowana
- **Przemysław Sołdacki:** Pytanie kiedy czerwcowa wersja wyjdzie – odpowiedź: chcemy niezwłocznie, jeszcze kilka poprawek było realizowanych w końcówce zeszłego tygodnia, dokumentacja w trakcie, prawdopodobnie w czwartek/piątek tego tygodnia

### Dalsze kroki

- Finalizacja stabilizacji czerwcowej wersji
- Testy i weryfikacja gotowości wersji
- Wydanie czerwcowej wersji (prawdopodobnie w czwartek/piątek tego tygodnia)

---

## 10. Ustawienia systemowe – przełączka do wersji starej

**Projekt:** `moduly/Ustawienia-systemowe`

### Cel biznesowy

Możliwość powrotu do starej wersji ustawień systemowych w razie potrzeby.

### Co zaimplementowano

- **Przełączka do wersji starej** – checkbox i przełączka już jest na Astrofox
- **Różnica w nazwach** – w starych ustawieniach były "integracje systemowe", "integracje definiowane", w nowych zostały jeszcze "integracja AMODIT" i "rozszerzenia AMODIT"
- **Zmiana tekstu** – wizualna zmiana tekstu (funkcjonalność działa tak jak ma działać)

### Jak to działa (jeśli omówiono)

[Nie omówiono szczegółów mechanizmu]

### Ograniczenia / Known issues

- Różnica w nazwach między starą a nową wersją (do dopieszczenia)

### Feedback z demo

- [Brak feedbacku w transkrypcji]

### Dalsze kroki

- Dopieszczenie nazw (zmiana tekstu w przełączce)

---

## 11. Ikony procesów – możliwość powrotu do domyślnej ikony

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Cel biznesowy

Możliwość powrotu do domyślnej ikony procesu (pierwsze literki nazwy procesu) po zmianie na własną ikonę.

### Kontekst

Obecnie po zmianie ikony procesu na własną nie można wrócić do domyślnej ikony (pierwszych literek nazwy procesu). Ktoś przez przypadek może zmienić ikonę i potem nie może wrócić do poprzedniej.

### Feedback z demo

- **Daniel Reszka:** Pytanie czy można przywrócić domyślną ikonę po zmianie – odpowiedź: nie można, to jest jednostronne ustawienie
- **Damian Kamiński:** Powinno być jednostronne ustawienie – jeśli ktoś zmienił, powinien ustawić ikonkę spójną z merytoryką procesu
- **Łukasz Bott:** Zgoda z Damianem – jednostronne ustawienie jest poprawne
- **Daniel Reszka:** Ktoś przez przypadek może zmienić i potem nie może wrócić – odpowiedź: zastanowimy się nad tym na spokojnie

### Dalsze kroki

- Rozważenie możliwości powrotu do domyślnej ikony (nie na tym spotkaniu, do zastanowienia na spokojnie)

---

## 12. Stabilizacja systemu – poprawki i testy

**Projekt:** Różne projekty

### Cel biznesowy

Stabilizacja systemu poprzez poprawki błędów, warunków brzegowych i testy przed wydaniem czerwcowej wersji.

### Co zaimplementowano

- **Poprawki warunków brzegowych** – różne poprawki w nowych elementach Reactowych
- **Endpointy do interfejsu Reactowego** – dorabianie endpointów do nowego interfejsu Reactowego (ustawienia systemowe, ustawienia procesu)
- **Stabilizacja raportów** – wyczyszczenie wykrytych problemów z raportami
- **Testy** – ciągłe testowanie i weryfikacja stabilności

### Jak to działa (jeśli omówiono)

[Ogólny opis procesu stabilizacji]

### Ograniczenia / Known issues

- [Brak znanych ograniczeń w transkrypcji]

### Feedback z demo

- **Damian Kamiński:** Podziękowanie dla zespołu za wykonaną pracę nad stabilizacją systemu
- **Damian Kamiński:** Wiele rzeczy nie jest widocznych na prezentacji, ale wymaga dużo pracy (poprawki, endpointy, stabilizacja)

### Dalsze kroki

- Kontynuacja testowania (szczególnie raporty – Łukasz)
- Finalizacja stabilizacji przed wydaniem czerwcowej wersji


# Rada Architektów – 2025-10-30

**Powiązane projekty:**
- `cross-cutting/Wydajnosc` – temat 1
- `cross-cutting/Bezpieczenstwo-sesji` – temat 2
- `moduly/Zrodla-danych` – temat 3
- `moduly/Modul-raportowy` – temat 4
- `klienci/Polpharma` – temat 5
- `cross-cutting/Interfejs-sprawy` – temat 6
- `moduly/OCR` – temat 7
- `integracje/System-mailowy` – temat 8

---

## 1. Problem z wyszukiwaniem spraw przez Lucene dla administratorów

**Projekt:** `cross-cutting/Wydajnosc`

### Kontekst i Problem

Problem z wyszukiwaniem spraw w systemie AMODIT dla użytkowników będących jednocześnie administratorami. Jeśli ktoś jest twórcą sprawy i jednocześnie administratorem, to wyszukiwanie po Case ID nie działa. Jeśli użytkownik nie jest administratorem, wyszukiwanie działa poprawnie. Zgłoszenie zostało stworzone przez Tomasza, ale wymaga uzupełnienia Repro Steps, ponieważ obecna dokumentacja jest nieczytelna (pełno screenów bez określenia kolejności).

### Zidentyfikowane Ryzyka

- Utrudnione wyszukiwanie spraw przez administratorów systemu
- Możliwe problemy z wyszukiwaniem również w innych zakładkach (nie tylko Case ID)

### Rozważane alternatywy

Jedna propozycja diagnozy, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Problem wymaga diagnozy przy użyciu narzędzia Luke (narzędzie do analizy indeksów Lucene). Procedura diagnozy:
1. W Searchu (nie w "skecz", tylko w ogólnym) sprawdzić zapytanie
2. Odpalić z poziomu Luke'a i zobaczyć, czy zwraca wyniki
3. Jeżeli nie zwraca wyników, zmodyfikować zapytanie, aż będzie zwracać wynik

**Szczegóły techniczne:**
- Na Wiki jest artykuł napisany przez Piotra Buczkowskiego o tym, jak diagnozować indeksy Lucene
- Problem dotyczy zewnętrznego komponentu (Lucene)
- Nie jest to problem z odbudową indeksu (restart indeksów procesu był już robiony)

### Zadania

- **Tomasz:** Uzupełnienie Repro Steps w zgłoszeniu z dokładnym opisem problemu → termin: nie określono
- **Damian Kamiński:** Wsparcie Tomasza w diagnozie problemu (jeśli będzie miał problemy) → termin: nie określono

### Punkty otwarte

- Czy problem występuje ze wszystkich zakładek, czy tylko z Case ID?
- Czy problem występuje również w zakładce "Wszystkie"?
- Na jakiej podstawie budowana jest lista w checkboxach filtru? (związane z tematem 4)

---

## 2. Powiadomienia mailowe do administratorów systemu o krytycznych zdarzeniach

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`

### Kontekst i Problem

Potrzeba implementacji mechanizmu automatycznego powiadamiania administratorów systemu o krytycznych zdarzeniach, które wymagają natychmiastowej interwencji. To pierwszy krok do self-healingu – zamiast czekać na zgłoszenie od biznesu "co się stało, gdzie mamy szukać", administrator od razu dostaje informację o przyczynie problemu. Przykłady krytycznych zdarzeń: skończenie się limitów OCR, skończenie się przestrzeni na dysku (system nie może zapisać dokumentów), brak dostępu do dysku sieciowego.

### Zidentyfikowane Ryzyka

- Brak natychmiastowej informacji o krytycznych problemach prowadzi do przestojów biznesowych
- Wszystkie maile stoją, niewczytywane są faktury, nic nie można zapisać
- Problem dotyczy głównie instalacji On-Premise

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Powiadomienia mailowe + powiadomienia w interfejsie | Wysyłanie maila oraz wyświetlanie powiadomienia w interfejsie AMODIT (czerwony pasek, zakładka "Uwagi dla administratora") | ✅ Wybrana – kompleksowe rozwiązanie |
| Tylko powiadomienia mailowe | Wysyłanie tylko maili do administratorów | ⏸️ Odroczona – jako pierwszy krok, ale docelowo również interfejs |
| Tylko powiadomienia w interfejsie | Wyświetlanie tylko w interfejsie bez maili | ❌ Odrzucona – mail jest potrzebny dla natychmiastowej informacji |
| Narzędzia zewnętrzne | Użycie zewnętrznych narzędzi do monitorowania (np. monitorowanie przestrzeni dyskowej) | ❌ Odrzucona – chcemy rozwiązanie wbudowane w AMODIT |
| Ostrzeżenia przed zdarzeniem | Powiadomienia przed wystąpieniem problemu (np. przed skończeniem się limitu OCR) | ⏸️ Odroczona – docelowo pożądane, ale na razie w momencie zdarzenia |

### Decyzja

**Status:** ✅ Zatwierdzone

Implementacja mechanizmu powiadamiania administratorów o krytycznych zdarzeniach:
- **Powiadomienia mailowe:** Wysyłane niezwłocznie w momencie wystąpienia zdarzenia oraz codziennie o określonej godzinie (np. 7:00 rano) na rozpoczęcie pracy
- **Powiadomienia w interfejsie:** Wyświetlanie powiadomień w interfejsie AMODIT (czerwony pasek lub zakładka "Uwagi dla administratora") – niezależnie od maila
- **Parametr konfiguracyjny:** Możliwość wyboru czy wysyłać maila, czy dawać powiadomienia w interfejsie, czy oba
- **Krytyczne zdarzenia do obsługi:**
  - Skończenie się limitów OCR
  - Skończenie się przestrzeni na dysku (nie można zapisać pliku)
  - Brak dostępu do dysku sieciowego
  - Inne przypadki do ustalenia (lista będzie rozbudowywana)

**Szczegóły techniczne:**
- Wysyłanie maili w zdefiniowanych przypadkach (gdy powstaje błąd w logu)
- Mechanizm nie zdiagnozuje braku dostępu do serwera pocztowego (wyjątek)
- Powiadomienia w interfejsie wymagają zaopiekowania przez Kamila pod kątem 4-eyes (four eyes principle)
- Powiadomienia w interfejsie powinny być zawsze widoczne (niezależnie od parametru maila)

### Zadania

- **Damian Kamiński:** Przygotowanie PBI na temat powiadomień do administratorów → termin: nie określono
- **Kamil Dubaniowski:** Zaopiekowanie powiadomień w interfejsie pod kątem 4-eyes → termin: nie określono

### Punkty otwarte

- Jakie inne krytyczne zdarzenia powinny być objęte powiadomieniami? (lista będzie rozbudowywana)
- Czy powiadomienia powinny ostrzegać przed zdarzeniem, czy tylko w momencie zdarzenia? (Janusz Bossak sugeruje ostrzeżenia przed zdarzeniem)
- Jak nazwać zakładkę z powiadomieniami dla administratora? ("Uwagi dla administratora" jako propozycja)

---

## 3. Problem z mapowaniem źródeł typu Static przy ponownym wgrywaniu

**Projekt:** `moduly/Zrodla-danych`

### Kontekst i Problem

Problem z mapowaniem kolumn przy ponownym wgrywaniu źródła typu Static w kontekście źródła dynamicznego (uzupełnionego regułami). Sytuacja: tworzymy źródło, wgrywamy do systemu mapując zgodnie z nazwami kolumn, zapisujemy. Przy ponownym wgrywaniu źródła: jeśli wchodzimy w "Mapuj", to automatycznie przypisuje się tak jak było (źródło się nie zmieniło, więc system zapamiętuje mapowanie). Jeśli nie wchodzimy w "Mapuj" i klikamy "Zapisz", to wszystko zmienia się na LongText. Zgłoszenie od klienta Allianz/Wien.

### Zidentyfikowane Ryzyka

- Utrata poprzedniego mapowania kolumn przy ponownym wgrywaniu źródła
- Wszystkie kolumny zmieniają się na LongText, jeśli użytkownik nie wejdzie w "Mapuj"

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Automatyczne użycie poprzedniego mapowania | Jeśli nie wchodzimy w "Mapuj", używa poprzedniego mapowania, nowe kolumny jako LongText | ✅ Wybrana – najprostsze rozwiązanie |
| Wymuszenie przejścia przez "Mapuj" | Nie można kliknąć "Zapisz" bez wejścia w "Mapuj" (przycisk disabled z komunikatem "Przejdź krok mapowania") | ❌ Odrzucona – zbyt restrykcyjne |
| Automatyczne wyświetlenie okienka mapowania | Po wybraniu pliku od razu wyświetla się okienko mapowania | ✅ Wybrana – najprostsze, najmniej zmian |
| Wyświetlenie podsumowania mapowanych kolumn | Tekstowe podsumowanie mapowanych kolumn przed zapisaniem | ⏸️ Odroczona – może być dodane później |

### Decyzja

**Status:** ✅ Zatwierdzone

Rozwiązanie problemu z mapowaniem:
- **Automatyczne wyświetlenie okienka mapowania:** Po kliknięciu "Wybierz plik" od razu przechodzimy do okienka mapowania (nie ma kroku pośredniego)
- **Zmiana przycisku:** Przycisk "Zapisz" w okienku mapowania zmieniony na "Wczytaj" (aby uniknąć dwóch przycisków "Zapisz")
- **Przycisk "Anuluj":** Zamiast "Zamknij" jest przycisk "Anuluj", który kasuje plik i wymusza rozpoczęcie od początku
- **Logika:** Po kliknięciu "Wczytaj" plik automatycznie znika (bo już się wczytał do tabeli) z podanym mapowaniem

**Szczegóły techniczne:**
- Jeśli źródło się nie zmieniło, system zapamiętuje poprzednie mapowanie
- Nowe kolumny są przypisywane jako LongText (domyślnie)
- Problem dotyczy źródeł typu Static wykorzystywanych w kontekście źródła dynamicznego

### Zadania

- **Anna Skupińska:** Implementacja automatycznego wyświetlenia okienka mapowania po wybraniu pliku → termin: nie określono
- **Anna Skupińska:** Zmiana przycisku "Zapisz" na "Wczytaj" w okienku mapowania → termin: nie określono
- **Anna Skupińska:** Zmiana przycisku "Zamknij" na "Anuluj" → termin: nie określono

### Punkty otwarte

- Czy użytkownik będzie wiedział, że kliknięcie "Anuluj" nie wgrywa pliku? (możliwe narzekania klientów, że "nie działa wgrywanie plików")
- Czy dodać tekstowe podsumowanie mapowanych kolumn przed zapisaniem?

---

## 4. Problem z filtrem użytkownika w nowych raportach – "Zaznacz wszystko"

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

Problem z przyciskiem "Zaznacz wszystko" w filtrze użytkownika w nowych raportach. Przycisk nie zaznacza wszystkiego, ponieważ nie wszystko jest załadowane (problem z paginacją). Przykład: w raporcie są 3 wartości (np. firmy), ale wyświetlają się tylko 2. Legenda pokazuje prawidłowo wszystkie 4 wartości, więc raport ma dane, ale filtr nie wyświetla wszystkich opcji. Problem wynika z tego, że filtr bierze distinct na pierwszych 100 rekordach, niezależnie od typu raportu. Jeśli raport jest agregowaniem kolumn (np. do firmy) i w pierwszych 1000 rekordach nie było trzeciej firmy, to wyświetlą się tylko dwie.

### Zidentyfikowane Ryzyka

- Użytkownik nie może zaznaczyć wszystkich wartości w filtrze
- Problem jest szczególnie denerwujący, gdy są tylko 2-3 elementy i jeden się nie wyświetla
- Możliwe problemy z wydajnością przy ładowaniu wszystkich wartości

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| "Zaznacz wszystko" tylko po wprowadzeniu wartości | Przycisk "Zaznacz wszystko" pojawia się tylko w momencie wprowadzenia wartości powodującej przeszukanie | ✅ Wybrana – rozwiązuje problem z paginacją |
| Walidacja przy zastosowaniu | Po zaznaczeniu "Zaznacz wszystko" i kliknięciu "Zastosuj" walidujemy czy lista wyświetlała wszystkie pozycje, jeśli nie – komunikat o konieczności zawężenia zakresu | ✅ Wybrana – dodatkowa walidacja |
| Wyświetlanie wszystkich wartości | Ładowanie wszystkich wartości do filtru niezależnie od paginacji | ❌ Odrzucona – problemy z wydajnością przy dużej liczbie wartości |

### Decyzja

**Status:** ✅ Zatwierdzone

Rozwiązanie problemu z filtrem:
- **"Zaznacz wszystko" tylko po wprowadzeniu wartości:** Przycisk "Zaznacz wszystko" pojawia się tylko w momencie wprowadzenia wartości powodującej przeszukanie (nie ma "zaznacz wszystko" po kliknięciu bez wpisywania)
- **Walidacja przy zastosowaniu:** Po zaznaczeniu "Zaznacz wszystko" i kliknięciu "Zastosuj" walidujemy czy lista wyświetlała wszystkie pozycje. Jeśli nie, wyświetlamy okno z informacją, że tych pozycji jest więcej i należy zawęzić zakres wyszukiwania do maksymalnie 100 pozycji
- **Analiza budowy listy:** Wymagana analiza na jakiej podstawie budowana jest lista w checkboxach filtru

**Szczegóły techniczne:**
- Filtr bierze distinct na pierwszych 100 rekordach, niezależnie od typu raportu
- Jeśli raport jest agregowaniem kolumn i w pierwszych 1000 rekordach nie było wszystkich wartości, filtr nie wyświetli wszystkich opcji
- Problem dotyczy również sytuacji, gdy są tylko 2-3 elementy i jeden się nie wyświetla

### Zadania

- **Anna Skupińska:** Analiza i przedstawienie na kolejnej Radzie, na jakiej podstawie budowana jest lista w checkboxach filtru → termin: sprint 45
- **Anna Skupińska:** Implementacja "Zaznacz wszystko" tylko po wprowadzeniu wartości → termin: po analizie
- **Anna Skupińska:** Implementacja walidacji przy zastosowaniu filtru → termin: po analizie

### Punkty otwarte

- Na jakiej podstawie budowana jest lista w checkboxach filtru? (wymagana analiza)
- Jak rozwiązać problem z paginacją przy dużej liczbie wartości? (maksymalnie 100 pozycji)
- Czy problem występuje również w innych filtrach w nowych raportach?

---

## 5. Polpharma – równoległe sesje po zalogowaniu

**Projekt:** `klienci/Polpharma`

### Kontekst i Problem

Wytyczne Security od Polpharmy dotyczące pokazywania równoległych sesji po zalogowaniu. Projekt jest rozpisany, ale nie ma zaopiekowanych projektów. Kamil Dubaniowski ma za dużo zadań (dostał wczoraj 3 tematy od Lucyny z ministerstw do wyceny) i nie wyrobi się z realizacją.

### Zidentyfikowane Ryzyka

- Brak możliwości realizacji z powodu przeciążenia zasobów
- Projekt może zostać zapomniany jeśli zostanie wrzucony na backlog

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wrzucenie na backlog | Projekt zostaje na backlogu, aż ktoś go podbije | ✅ Wybrana – brak zasobów do realizacji |
| Realizacja w najbliższym czasie | Próba realizacji pomimo przeciążenia zasobów | ❌ Odrzucona – Kamil nie wyrobi się |

### Decyzja

**Status:** ⏸️ Odroczone

Projekt zostaje wrzucony na backlog, aż ktoś go podbije. Ze względu na przeciążenie zasobów (Kamil Dubaniowski ma za dużo zadań) nie ma możliwości realizacji w najbliższym czasie.

**Szczegóły techniczne:**
- Projekt jest rozpisany
- Wytyczne Security od Polpharmy dotyczą pokazywania równoległych sesji po zalogowaniu

### Zadania

Brak zadań przypisanych (projekt odroczony).

### Punkty otwarte

- Kiedy projekt zostanie podjęty do realizacji?
- Czy projekt wymaga sponsorowania?

---

## 6. Amadeus – problem z dodaniem grupy do pola "Redaktorzy spraw"

**Projekt:** `cross-cutting/Interfejs-sprawy`

### Kontekst i Problem

Problem z dodaniem grupy do pola "Redaktorzy spraw" w systemie AMODIT. Problem prawdopodobnie wynika z tego, że w nazwie systemowej grupy są nawiasy (w cudzysłowie w nawiasach jest login). Kamil Dubaniowski testował i wydaje mu się, że działa, gdy nazwa z nawiasami jest jako nazwa wyświetlana. Jeśli systemowa nazwa grupy jest bez nawiasów, to działa poprawnie.

### Zidentyfikowane Ryzyka

- Nie można dodać grup z nawiasami w nazwie systemowej do pola "Redaktorzy spraw"
- Problem z dziwnymi znakami w nazwach systemowych grup

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Użycie nazwy wyświetlanej | Jeśli potrzebują nawiasów, niech ustawią je w nazwie wyświetlanej | ✅ Wybrana – obejście problemu |
| Blokada dziwnych znaków w nazwie systemowej | Nazwa systemowa powinna być zablokowana z dziwnych znaków (tylko podłoga i nic więcej) | ✅ Wybrana – długoterminowe rozwiązanie |
| Wrzucenie na backlog | Projekt zostaje na backlogu | ❌ Odrzucona – Kamil uważa, że zapomnimy o tym |

### Decyzja

**Status:** ✅ Zatwierdzone

Rozwiązanie problemu:
- **Obejście:** Jeśli klient potrzebuje nawiasów, powinien ustawić je w nazwie wyświetlanej (nie w nazwie systemowej)
- **Długoterminowe rozwiązanie:** Nazwa systemowa powinna być na wszystkich poziomach zablokowana z dziwnych znaków (ewentualnie podłoga i nic więcej)

**Szczegóły techniczne:**
- Problem występuje, gdy w nazwie systemowej grupy są nawiasy
- Jeśli systemowa nazwa grupy jest bez nawiasów, działa poprawnie
- Wyświetlana nazwa techniczna powoduje problem

### Zadania

- **Kamil Dubaniowski:** Wprowadzenie blokady dziwnych znaków w nazwie systemowej grup (tylko podłoga i nic więcej) → termin: nie określono

### Punkty otwarte

- Czy problem dotyczy tylko pola "Redaktorzy spraw", czy również innych pól?
- Kiedy zostanie wprowadzona blokada dziwnych znaków w nazwie systemowej?

---

## 7. RegEx – problem z dzieleniem dokumentu po kodzie kreskowym

**Projekt:** `moduly/OCR`

### Kontekst i Problem

Problem z dzieleniem dokumentu po kodzie kreskowym w funkcjonalności RegEx. Ze zgłoszenia wynika, że jeśli system nie rozpozna żadnego kodu kreskowego, to w ogóle nie zakłada sprawy. Oczekiwane zachowanie: jeśli nie rozpozna kodu, powinien założyć jedną zbiorczą sprawę (całą masę stron w jedną).

### Zidentyfikowane Ryzyka

- Dokumenty bez kodów kreskowych nie są przetwarzane (nie zakłada się sprawa)
- Utrata dokumentów, które nie mają kodów kreskowych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Założenie zbiorczej sprawy | Jeśli nie rozpozna kodu, zakłada jedną zbiorczą sprawę (całą masę stron w jedną) | ✅ Wybrana – oczekiwane zachowanie |
| Nie dzielenie dokumentu | Jeśli nie znajdzie kodu, nie dzieli dokumentu, skleja jako część poprzedniego | ⏸️ Odroczona – do rozważenia w przyszłości |
| Brak zakładania sprawy | Obecne zachowanie – nie zakłada sprawy jeśli nie rozpozna kodu | ❌ Odrzucona – nieprawidłowe zachowanie |

### Decyzja

**Status:** ✅ Zatwierdzone

Poprawka zachowania przy dzieleniu dokumentu po kodzie kreskowym:
- **Jeśli dokument nie ma żadnego kodu:** Na podstawie tego dokumentu zakłada jedną sprawę (zbiorczą)
- **Jeśli nie rozpozna kodu, ale kod jest:** Nie dzieli dokumentu, nadal skleja jako część poprzedniego dokumentu
- **Logika:** System ma dzielić tylko po podanym kodzie kreskowym (na stronie może być kilka kodów, ale interesuje nas tylko ten podany w schemacie)

**Szczegóły techniczne:**
- Jeśli nie znajdzie żadnego kodu kreskowego, powinien założyć jedną zbiorczą sprawę
- Problem dotyczy funkcjonalności RegEx (dzielenie dokumentu po kodzie kreskowym)

### Zadania

- **Piotr Buczkowski:** Poprawka zachowania przy dzieleniu dokumentu po kodzie kreskowym → termin: dzisiaj (30.10.2025)
- **Kamil Dubaniowski:** Przygotowanie przypadku testowego i podlinkowanie do zgłoszenia → termin: nie określono

### Punkty otwarte

- Czy poprawka obejmuje wszystkie przypadki dzielenia dokumentu po kodzie kreskowym?
- Jak przetestować różne scenariusze (dokument bez kodu, dokument z nierozpoznanym kodem, dokument z rozpoznanym kodem)?

---

## 8. Problem z formatowaniem nazwy pliku przy wysyłaniu przez serwer pocztowy

**Projekt:** `integracje/System-mailowy`

### Kontekst i Problem

Problem z formatowaniem nazwy pliku przy wysyłaniu przez pewien serwer pocztowy. Plik jest tak formatowany, że nazwa jest w określony sposób. Jeśli wyśle się z innego serwera, nazwa jest w Queście inaczej formatowana i problemu nie ma. Problem dotyczy średnika w nazwie pliku – jeśli średnik jest w nazwie, serwer dzieli nazwę na dwie linijki, a jak dzieli na dwie linijki, to dzieli średnikiem. A priori był średnik w nazwie pliku, więc powstaje problem z formatowaniem.

### Zidentyfikowane Ryzyka

- Nieprawidłowe formatowanie nazwy pliku przy wysyłaniu przez niektóre serwery pocztowe
- Problem z plikami zawierającymi średniki w nazwie

### Rozważane alternatywy

Jedna propozycja rozwiązania, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Problem wymaga testowania z konkretnym plikiem EML. Zgłoszenie zostało stworzone przez Piotra Buczkowskiego w tym tygodniu (numer 22431) jako wzorzec do testowania.

**Szczegóły techniczne:**
- Problem występuje przy wysyłaniu przez pewien serwer pocztowy
- Problem dotyczy średnika w nazwie pliku
- Serwer dzieli nazwę pliku na dwie linijki, jeśli zawiera średnik
- Jeśli wyśle się z innego serwera, problemu nie ma

### Zadania

- **Piotr Buczkowski:** Testowanie problemu z konkretnym plikiem EML (zgłoszenie 22431) → termin: nie określono
- **Damian Kamiński:** Opisanie wzorca testowania w zgłoszeniu → termin: nie określono

### Punkty otwarte

- Jakie dokładnie serwery pocztowe powodują problem?
- Czy problem dotyczy tylko średników, czy również innych znaków specjalnych?
- Jak rozwiązać problem z formatowaniem nazwy pliku przez różne serwery pocztowe?

---

## 9. Inne tematy (krótkie wzmianki)

### 9.1. Problem z pulą aplikacji w AMODIT (Endur)

**Projekt:** Nowy temat / do sklasyfikowania

Problem z pulą aplikacji w AMODIT u klienta Endur. Założony wątek na AMODIT Services, zrzucone logi, ale brak pomysłu na rozwiązanie. Piotr Buczkowski ma wesprzeć komentarzem, co szukać i gdzie.

**Zadania:**
- **Piotr Buczkowski:** Wsparcie w diagnozie problemu z pulą aplikacji (komentarz w wątku na AMODIT Services) → termin: po zakończeniu Rady

### 9.2. Logowanie informacji o osiągniętym limicie OCR

**Projekt:** `moduly/OCR`

Mateusz ma dodać logowanie informacji o osiągniętym limicie OCR jako pierwszy krok przed powiadomieniami mailowymi do administratorów (temat 2). Obecnie odpowiedź jest taka, że nie wiadomo o co chodzi, więc to jest pierwsze usprawnienie.

**Zadania:**
- **Mateusz:** Dodanie logowania informacji o osiągniętym limicie OCR → termin: nie określono

### 9.3. Problem z wywołaniem reguły funkcji dla zamkniętej sprawy

**Projekt:** `moduly/Silnik-regul`

Problem odkryty przez Piotra Buczkowskiego: AMODIT do AMODIT-a, wywołanie reguły, która jest funkcją, ma walidowany element, że sprawa jest zamknięta, mimo że to jest funkcja i przez to nie da się wywołać. Dla funkcji nie powinno być to walidowane.

**Zadania:**
- **Damian Kamiński:** Dopisanie zalecenia Piotra do zgłoszenia: dla funkcji nie powinno być walidowane, że sprawa jest zamknięta → termin: nie określono

### 9.4. Problem z otwieraniem raportu w nowym module raportowym (Niden)

**Projekt:** `moduly/Modul-raportowy`

Problem z otwieraniem raportu w nowym module raportowym u klienta Niden. Anna Skupińska ma zająć się tym po zakończeniu hotfixów (priorytet pierwszy). Piotr Buczkowski wspomina, że w nowszej wersji już jest zrobione (sprawdzali kilka miesięcy temu). Zadanie: potwierdzić, że to jest zrobione we wszystkich miejscach. Jeśli nie ma, to uzupełnić, żeby tego typu błędy mogły być rozwiązywane na poziomie loga.

**Zadania:**
- **Anna Skupińska:** Potwierdzenie i uzupełnienie logowania błędów SQL z nowych raportów we wszystkich miejscach (po zakończeniu hotfixów, priorytet pierwszy) → termin: nie określono

### 9.5. Uwspółcześnienie mechanizmu drukowania

**Projekt:** Nowy temat / do sklasyfikowania

Piotr Buczkowski wspomina, że Print – wersja do wydruku jest sprzed 10 lat, prawie niezmieniana. Damian Kamiński odpowiada, że działa i cel nie jest drukowanie spraw (to skrajny przypadek). Rozwiązanie: zrobić minimalną dokumentację. Jeśli ktoś będzie chciał to poprawiać, to niech sponsoruje, bo to nie jest cel, żeby sprawy były drukowane.

**Decyzja:** Odroczone – nie jest na liście priorytetów. Zrobić minimalną dokumentację.

**Zadania:**
- **Patryk:** Przygotowanie minimalnej dokumentacji mechanizmu drukowania → termin: nie określono


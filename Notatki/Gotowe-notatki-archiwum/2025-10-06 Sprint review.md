> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Sprint Review – 2025-10-06

**Sprint:** [nie podano]
**Okres:** [nie podano]

**Powiązane projekty:**
- `moduly/Ustawienia-systemowe` – temat 1
- `Klienci/WIM/Komunikator` – temat 2
- `Moduly/Edytor-procesow/Edytor-formularzy` – temat 3
- `Moduly/Edytor-procesow/Edytor-diagramu` – temat 4
- `Moduly/Modul-raportowy/Masowe-podpisywanie` – temat 5
- `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS` – temat 7
- `Moduly/Trust-Center` – tematy 6, 10
- `cross-cutting/Wydajnosc` – temat 8
- `Moduly/Modul-raportowy` – temat 9

---

## 1. Logi systemowe – odświeżenie interfejsu

**Projekt:** `moduly/Ustawienia-systemowe`

### Cel biznesowy

Odświeżenie strony logów systemowych jako ostatniej strony w systemie, która nie była jeszcze w ramie Reactowej. Głównym celem było przeniesienie istniejącej funkcjonalności do nowego interfejsu, zachowując wszystkie dotychczasowe możliwości.

### Co zaimplementowano

- **Przeniesienie do React** – strona logów systemowych została odświeżona i przeniesiona do ramy Reactowej
- **Zakładki** – zachowano podział na zakładki: logi systemowe, aktywność administracyjna, kolejka maili do wysłania
- **Wyszukiwanie** – działa na tej samej zasadzie co wcześniej (przycisk "Zastosuj" zamiast "Wyszukaj"), globalne wyszukiwanie działa w pakiecie z filtrami (filtry nie działają dopóki nie zostanie zastosowane wyszukiwanie)
- **Eksport zaznaczonych logów** – zrezygnowano z masowego globalnego eksportu całej strony, wprowadzono eksport tylko zaznaczonych logów (użytkownik wybiera które logi są istotne w zgłoszeniu)
- **Kopiowanie do schowka** – funkcjonalność kopiowania logów (wymaga poprawki – obecnie kopiuje tylko treść przykładowej wypowiedzi z prezentacji zamiast pełnego logu)
- **Filtry dla aktywności administracyjnej** – dodano możliwość filtrowania po odbiorcy i po tytule (wcześniej była tylko wyszukiwarka)
- **Filtry dla kolejki maili** – dodano możliwość filtrowania (wcześniej była tylko wyszukiwarka)
- **Szczegóły aktywności administracyjnej** – rozwijanie szczegółów zmiany (wcześniej był tylko nagłówek aktywności)
- **Domyślne filtry** – domyślnie pokazywane są tylko błędy i ostrzeżenia (jak w starym module)

### Jak to działa (jeśli omówiono)

Wyszukiwanie i filtry działają w pakiecie – dopóki użytkownik nie uzna że zakończył wrzucanie kryteriów i nie kliknie "Zastosuj", filtry nie działają (ze względów wydajnościowych).

### Ograniczenia / Known issues

- **Kopiowanie do schowka** – obecnie kopiuje tylko treść przykładowej wypowiedzi z prezentacji zamiast pełnego logu (wymaga poprawki)
- **Aktywność administracyjna – rejestrowanie zmian null** – system rejestruje zmiany w ustawieniach procesu nawet gdy faktycznie nic nie zostało zmienione (np. ktoś kliknął "edytuj", "zapisz" bez wprowadzenia zmian). Wymaga weryfikacji dlaczego rejestrujemy te zmiany null-owe
- **Kolejka maili** – brakuje informacji o kolejnej planowanej dacie wysyłki (kiedy Job się kolejny raz ma uruchomić)
- **Kolejka maili – maile poufne** – wymaga weryfikacji czy uwzględniono mechanizm maile poufne, których nie można treści wyświetlić
- **Przycisk wyczyść wszystkie** – przywraca do domyślnego ustawienia (błąd, ostrzeżenie), ale nie jest jasne czy powinien też resetować inne filtry

### Feedback z demo

- **Piotr Buczkowski:** Kopiowanie powinno kopiować pełny log (z treścią, z Message, z URL-em, z użytkownikiem) w nowych dziennych formatach, bo to często się przydaje
- **Piotr Buczkowski:** W aktywności administracyjnej widoczne są niepotrzebne wpisy z null (zmiana nastąpiła, ale nic nie zmieniono) – kwestia rejestracji, trzeba się przyjrzeć
- **Piotr Buczkowski:** W kolejce maili brakuje informacji o kolejnej planowanej dacie wysyłki
- **Damian Kamiński:** Warto wspomnieć o eksporcie zaznaczonych logów jako wygodnej funkcjonalności
- **Łukasz Bott:** W starym interfejsie nie widać szczegółów aktywności administracyjnej (wiemy tylko że ktoś coś zmienił, ale nie co). W nowym interfejsie jest to bardziej użyteczne, skoro wyświetlamy szczegóły

### Dalsze kroki

- Poprawka kopiowania do schowka (pełny log zamiast tylko treści)
- Weryfikacja dlaczego rejestrujemy zmiany null-owe w aktywności administracyjnej
- Dodanie informacji o kolejnej planowanej dacie wysyłki w kolejce maili
- Weryfikacja obsługi maile poufne w kolejce maili
- Dodanie funkcjonalności kasowania maili z kolejki (dla testów)
- Dodanie funkcjonalności wskazania odbiorcy maili na czas testów (zamiast do faktycznego odbiorcy, do konsultanta prowadzącego testy)

---

## 2. Komunikator – poprawki wizualne i uproszczenie

**Projekt:** `Klienci/WIM/Komunikator`

### Cel biznesowy

Ukończenie komunikatora względem wcześniejszej wersji poprzez poprawki spójne w ramach całego systemu oraz uproszczenie formy tworzenia konwersacji.

### Co zaimplementowano

- **Poprawki wizualne** – upodobnienie konwersacji do konwersacji tekstowej, dostosowanie do ekranu (nie od brzegu do brzegu, tylko w określonym zakresie), poprawione awatary (bez ramek, czcionki podobne do wszystkich czcionek w systemie)
- **Uproszczenie formy tworzenia konwersacji** – obecnie można utworzyć prywatną z konkretną osobą (zaczynamy konwersację) lub grupową (wskazanie wielu osób). Planowane ujednolicenie – kogo wskażemy zdefiniuje jaki jest rodzaj konwersacji
- **Ścieżka dla komunikatora** – brakuje ścieżki dla komunikatora (jak dla wszystkich innych elementów systemu) – wymaga konsultacji między Mateuszem a Przemkiem

### Ograniczenia / Known issues

- **Brak ścieżki dla komunikatora** – nie ma ścieżki dla komunikatora jak dla wszystkich innych elementów systemu (wymaga konsultacji)
- **Prywatna vs grupowa** – obecnie wygląda tak że możemy utworzyć prywatną z konkretną osobą lub grupową z wieloma osobami. Planowane ujednolicenie

### Dalsze kroki

- Praca nad połączeniem z grupami (konwersacja na podstawie składu grupy określonej w ramach AMODIT-a)
- Ujednolicenie formy tworzenia konwersacji (kogo wskażemy zdefiniuje rodzaj konwersacji)
- Dodanie ścieżki dla komunikatora (konsultacja Mateusz–Przemek)

---

## 3. Edytor formularza – wyszukiwarka i bezpieczna edycja

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

### Cel biznesowy

Dodanie wyszukiwarki w edytorze formularza oraz wprowadzenie bezpiecznej edycji słownika i zmiany typu pola z potwierdzeniem ryzyka.

### Co zaimplementowano

- **Wyszukiwarka** – możliwość szukania po nazwach wyświetlanych i po nazwach systemowych (jeśli szukamy po polsku, pokazuje tylko polskie; jeśli po systemowej lub innym języku, pokazuje tylko ten który znajdziemy)
- **Bezpieczna edycja słownika** – nie można zmienić słownika bezpośrednio, trzeba się doklikać, zaznaczyć że zdajemy sobie sprawę z ryzyka, zapisać
- **Zmiana typu pola** – można zmienić typ pola, trzeba zaznaczyć że zdajemy sobie sprawę z ryzyka (zawsze, nawet przy zmianie na ten sam typ, np. numeryczne na kwotę)
- **Placeholdery dziedziczone** – wyświetlanie placeholderów dla pól które są dziedziczone (np. nazwa systemowa jako placeholder). Zmiana domyślnej nazwy zmienia też placeholder
- **Labele dla pól bez Labeli** – dodane Labele dla pól które docelowo nie mają Labeli w sprawie (są na szaro z Tooltipem jeśli nie jest widoczne)
- **Okienko do zmiany nazwy wyświetlanej** – zmienione na zasadzie przycisku, gdzie wyświetla się całe okienko
- **Okienko do zmiany podpowiedzi (Tooltip)** – zmienione na zasadzie przycisku, gdzie wyświetla się całe okienko
- **Wersja językowa** – wrócono do tego co było (wersja językowa jest wybierana na liście, na dole jest okno edytora)

### Ograniczenia / Known issues

- **Okienko edytora za małe** – okienko do zmiany nazwy wyświetlanej i podpowiedzi jest za małe (nie mieści się w jednej linijce, Tooltip się nie mieści). Wymaga zwiększenia (szersze i wyższe)
- **Zmiana typu pola – zawsze wymaga potwierdzenia** – nawet przy zmianie na ten sam typ (np. numeryczne na kwotę) trzeba zaznaczyć że zdajemy sobie sprawę z ryzyka. Możliwe że powinno sprawdzać czy w sprawach to pole jest wypełnione przed wymaganiem potwierdzenia
- **Pola zablokowane** – brakuje obsługi pól zablokowanych (np. rejestr Company, który ma zablokowane możliwości edycji w zakresie typów nazw ze względu na integracje). Wymaga pokazania kłódki obok i zablokowania ustawień
- **Reguła tabeli** – reguła tabeli ma przejść do zakładki reguły (jest nieintuicyjna w edytorze formularza), tutaj może być odnośnik jak było do tej pory

### Feedback z demo

- **Piotr Buczkowski:** Okienko edytora jest za małe (szersze i wyższe), Tooltip się nie mieści w jednej linijce
- **Piotr Buczkowski:** Przy zmianie typu pola z numerycznego na kwotę (lub odwrotnie) nie powinno wymagać potwierdzenia, bo to ten sam typ
- **Piotr Buczkowski:** Może sprawdzać czy w sprawach to pole jest wypełnione przed wymaganiem potwierdzenia
- **Damian Kamiński:** Lepiej niech zapyta czy to się faktycznie coś może stać niż bezmyślnie kliknął i coś się stanie
- **Piotr Buczkowski:** Rozwiązaniem zawsze jest ukrycie pola i dodanie nowego z nowym typem (jeśli działamy na już używanym procesie)
- **Damian Kamiński:** Domyślnie bez konieczności powiększania cały popup dać większy (żeby zajmował jedną drugą ekranu zamiast jednej piątej)
- **Barbara Michalak:** Reguła tabeli powinna przejść do zakładki reguły, ale też zostać tutaj (dla kompatybilności)
- **Piotr Buczkowski:** Reguła tabeli powinna przejść do zakładki reguły, ale też zostać tutaj

### Dalsze kroki

- Zwiększenie okienka edytora (szersze i wyższe, domyślnie większe – jedna druga ekranu zamiast jednej piątej)
- Rozważenie walidacji czy w sprawach to pole jest wypełnione przed wymaganiem potwierdzenia przy zmianie typu pola
- Dodanie obsługi pól zablokowanych (kłódka obok, zablokowanie ustawień)
- Przeniesienie reguły tabeli do zakładki reguły (z pozostawieniem odnośnika w edytorze formularza)
- Poprawka etykiet obok ikonek w belce (przybliżyć etykiety do ikonek – za duża odległość między ikoną a napisem)

---

## 4. Edytor formularza – diagram procesu

**Projekt:** `Moduly/Edytor-procesow/Edytor-diagramu`

### Cel biznesowy

Wprowadzenie diagramu procesu w edytorze formularza, umożliwiającego wizualizację przepływu między etapami oraz łączenie pól i etapów.

### Co zaimplementowano

- **Diagram procesu** – rysowanie diagramu procesu (póki co za Taxi)
- **Scroll i Zoom** – możliwość scrollowania i zoomowania diagramu
- **Łączenie pól** – możliwość łączenia pól
- **Łączenie etapów** – możliwość łączenia etapów (bez żadnej akcji)
- **Zaznaczanie etapu** – kliknięcie w dany etap zaznacza go i pokazuje wszystkie strzałki wychodzące (do jakich etapów łączy się ten etap)
- **Wizualizacja połączeń** – linie przerwane dla połączeń projektowych (narysowane, ale realnie nie da się takiej ścieżki przejść bo nie ma reguł), linie ciągłe dla połączeń z regułami (faktycznie zapewniają przejście)
- **Nazwy reguł** – na połączeniach z regułami wyświetlane są nazwy reguł (np. "Kolejny etap", "Poprzednie etapy"). Jeśli nazwa jest za długa, wyświetlane są 3 kropki z Tooltipem

### Ograniczenia / Known issues

- **Prawy panel** – dalsze kroki to prawy panel (wizualnie raczej już zostaniemy przy tym co widać)
- **Przełączanie między modelami** – jest plan żeby przełączać się między różnymi modelami (mamy 2 które nieco inaczej rysują), ale na razie się wstrzymujemy (ten rysuje czytelniej, tamten niekoniecznie się podobał)
- **Nazwy reguł** – jeśli nazwa reguły jest bardzo długa (np. "Wróć do beneficjenta" i zmień etap na "wybierz z listy"), trzeba przewidzieć jak to będzie się ładnie wyświetlało
- **Pełna nazwa reguły** – plan że z tego poziomu będzie się dało kliknąć i zobaczyć pełną nazwę w prawym panelu, zobaczyć tłumaczenia Tooltip dla tej reguły i sam kod (kod będzie edytowany już jak było w edytorze)

### Dalsze kroki

- Dalsze kroki to prawy panel (wizualnie raczej już zostaniemy przy tym co widać)
- Rozważenie przełączania między modelami (na razie wstrzymane)
- Obsługa długich nazw reguł (3 kropki z Tooltipem, kliknięcie pokazuje pełną nazwę w prawym panelu)
- Dodanie możliwości zobaczenia tłumaczeń Tooltip dla reguły i kodu w prawym panelu

---

## 5. Raporty – podpisywanie SimpleSign

**Projekt:** `Moduly/Modul-raportowy/Masowe-podpisywanie`

### Cel biznesowy

Wprowadzenie podpisywania SimpleSign w ramach nowych raportów (do tej pory tego nie było) oraz usprawnienie wyboru metody podpisywania poprzez możliwość definicji dostępnych metod.

### Co zaimplementowano

- **Podpisywanie SimpleSign** – wprowadzono podpisywanie SimpleSign w ramach nowych raportów (pojawia się analogiczną ikonką, cienką jak w innych miejscach, żeby było spójne)
- **Definicja dostępnych metod podpisywania** – możliwość zdefiniowania dostępnych metod podpisywania (jeśli zaznaczymy SignApp, bo jakaś firma nie korzysta w ogóle z SimpleSign, tylko wszyscy mają Szafira, to nie będziemy im zbędnie wyświetlać SimpleSigna, lub odwrotnie)
- **Domyślna akcja przycisku** – jeśli zdefiniujemy SignApp, domyślną akcją przycisku "Podpisz certyfikatem" będzie wywoływanie SignAppa (zamiast wyboru metody)

### Ograniczenia / Known issues

- **Funkcjonalność jeszcze nie działa** – na ten moment zdefiniowanie dostępnych metod podpisywania jeszcze nie działa (Marek ma to poprawione do testów, zapomniał przekazać wyboru tych akcji, ale już działa u niego, zaraz to wrzuci)
- **SimpleSign – logowanie** – pytanie czy jak podpis za pomocą SimpleSign wykryje że jest to niezalogowany, to czy może przekierować do logowania (zamiast wyświetlać opcję "Zaloguj się" obok "Podpisz za pomocą SimpleSign")
- **SimpleSign – ścieżka użytkownika** – niejasna ścieżka: czy najpierw trzeba się zalogować, a później jeszcze raz zaznaczyć i podpisać, czy może być pierwszym krokiem "Podpisz za pomocą SimpleSign" który przekieruje do logowania jeśli potrzeba

### Feedback z demo

- **Kamil Dubaniowski:** Czy jak podpis za pomocą SimpleSign wykryje że jest to niezalogowany, to może przekierować do logowania? (zamiast wyświetlać opcję "Zaloguj się")
- **Piotr Buczkowski:** "Zaloguj się" powinien być ewentualnym pierwszym krokiem. "Podpisz za pomocą SimpleSign" powinien przekierować do logowania jeśli potrzeba
- **Kamil Dubaniowski:** Jeśli zaznaczam 50, zaznaczę z 60 i kliknę "zaloguj", to później wrócę i mam zaznaczone dalej, czy muszę znowu 50 zaznaczyć i podpisać? Nie wiem jak ścieżka wygląda

### Dalsze kroki

- Poprawka funkcjonalności definicji dostępnych metod podpisywania (Marek ma to poprawione do testów, zaraz wrzuci)
- Rozważenie zmiany ścieżki SimpleSign – "Podpisz za pomocą SimpleSign" jako pierwszy krok, który przekieruje do logowania jeśli potrzeba (zamiast wyświetlać opcję "Zaloguj się" obok)
- Testy wspólnie z Oktawią (ma dostęp do SimpleSign)

---

## 6. Trust Center – logowanie Azure

**Projekt:** `moduly/Trust-Center`

### Cel biznesowy

Umożliwienie logowania się za pomocą konta Azure w Trust Center (dla osób z dostępem serwisowym), upraszczając proces logowania.

### Co zaimplementowano

- **Logowanie Azure** – możliwość logowania się za pomocą konta Azure w Trust Center (tylko dla osób z dostępem serwisowym)
- **Przekierowanie do autoryzacji** – kliknięcie powoduje przekierowanie do autoryzacji w Azure, tam wszystko sprawdza, po autoryzacji użytkownik jest zalogowany
- **Brak konieczności podawania adresu email** – nie trzeba już podawać adresu email przy logowaniu Azure

### Ograniczenia / Known issues

- **Tekst przycisku** – obecny tekst sugeruje jakby Microsoft był producentem tego (wymaga zmiany na "zaloguj kontem Microsoft" lub podobnie)
- **Spójność interfejsów** – powinno być zrobione tak jak logowanie do AMODIT-a (kafelek jest zakreślony ramką, "Zaloguj za pomocą"), powinno wyglądać dokładnie w taki sam sposób pod spodem
- **Spójność wszystkich interfejsów** – wszystkie interfejsy do wprowadzania loginów, PINów do Trust Center powinny być w miarę spójne dla wszystkich naszych narzędzi

### Feedback z demo

- **Łukasz Bott:** Tekst przycisku powinien być "zaloguj kontem Microsoft" lub podobnie (obecny tekst sugeruje jakby Microsoft był producentem)
- **Damian Kamiński:** Powinno być zrobione tak jak logowanie do AMODIT-a (kafelek jest zakreślony ramką, "Zaloguj za pomocą"), powinno wyglądać dokładnie w taki sam sposób pod spodem
- **Łukasz Bott:** Wszystkie interfejsy do wprowadzania loginów, PINów do Trust Center powinny być w miarę spójne dla wszystkich naszych narzędzi
- **Damian Kamiński:** Weź wzór ze strony logowania AMODIT

### Dalsze kroki

- Zmiana tekstu przycisku na "zaloguj kontem Microsoft" lub podobnie
- Ujednolicenie wyglądu z logowaniem do AMODIT-a (kafelek zakreślony ramką, "Zaloguj za pomocą")
- Ujednolicenie wszystkich interfejsów logowania dla wszystkich naszych narzędzi

---

## 7. SignApp Mac – automatyczne wykrywanie bibliotek

**Projekt:** `moduly/Trust-Center`, `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

### Cel biznesowy

Usprawnienie procesu podpisywania na Macu poprzez automatyczne wykrywanie bibliotek do podpisywania, eliminując konieczność ręcznego wskazywania ścieżek do bibliotek.

### Co zaimplementowano

- **Automatyczne wykrywanie bibliotek** – aplikacja wykrywa faktycznie wszystkie biblioteki do podpisywania (nie trzeba wskazywać ścieżek do bibliotek)
- **Wybór certyfikatu** – można wybrać którym podpisem chcemy złożyć podpis (wykrywa podpięte certyfikaty do komputera)
- **Wybór miejsca podpisu** – możliwość wyboru konkretnie miejsca gdzie chcemy złożyć podpis (opcja 1) lub automatyczne rzucenie na koniec dokumentu (opcja 2, dla plików stronicowych)
- **Obsługa wielu bibliotek** – wspiera 3 produkty (2 dostawców): Szafir, Szafir oraz Impress (wszystkie certyfikaty kwalifikowane)
- **Obsługa kluczy prywatnych** – obsłużono sytuację że niektórych kartach może być wypadek kluczy prywatnych

### Ograniczenia / Known issues

- **Wyświetlanie certyfikatów** – obecnie wyświetlane jest całe Subject zamiast Common Name (jest za bardzo techniczne, mało czytelne dla zwykłego użytkownika)
- **Wyświetlanie wielu certyfikatów** – jeśli ktoś ma 2 certyfikaty, trzeba je rozróżnić (Common Name może być taki sam, ale data ważności zwykle jest inna)
- **Ikona instrukcji** – w instrukcji jest napisane "wybierz interesujący cię certyfikat, używając pola wyboru z lewej strony", ale nie ma pola wyboru z lewej strony (trzeba to zaprojektować)
- **Spójność z SignApp Windows** – powinno być zrobione tak samo jak w SignApp Windows (Common Name, wydawca, data ważności)
- **Logo** – logo jest przesadzone (za duże)

### Feedback z demo

- **Piotr Buczkowski:** Common Name najbardziej lepiej wyświetlać, nie cały Subject (jest za bardzo techniczne)
- **Piotr Buczkowski:** Zróbmy tak samo jak w SignApp Windows (Common Name, wydawca, data ważności)
- **Piotr Buczkowski:** Jeśli ktoś ma 2 certyfikaty, trzeba je rozróżnić (Common Name może być taki sam, ale data ważności zwykle jest inna – jedna na czerwono że nieważna)
- **Kamil Dubaniowski:** W instrukcji jest napisane "wybierz interesujący cię certyfikat, używając pola wyboru z lewej strony", ale nie ma pola wyboru z lewej strony (trzeba to zaprojektować)
- **Damian Kamiński:** Logo jest przesadzone (za duże)
- **Kamil Dubaniowski:** Warto by było ujednolicić z SignApp Windows (spójnie tu i tu)

### Dalsze kroki

- Zmiana wyświetlania certyfikatów na Common Name zamiast całego Subject (jak w SignApp Windows)
- Dodanie kolumny z wydawcą i datą ważności (jak w SignApp Windows)
- Zaprojektowanie pola wyboru z lewej strony (zgodnie z instrukcją)
- Zmniejszenie logo
- Ujednolicenie wyglądu z SignApp Windows (kolory pomarańczowe, spójność z Git)
- Rozważenie dodania obsługi Sigillum PWP (najbardziej popularne, potrzebujemy mieć do testowania)

---

## 8. DatabaseAdmin – zmiana pól varchar na Medium Text

**Projekt:** `cross-cutting/Wydajnosc`

### Cel biznesowy

Usunięcie ograniczenia długości pól tekstowych poprzez zmianę pól typu varchar na Medium Text, umożliwiając wpisywanie dłuższych wartości (np. Link do SharePointa przekracza 256 znaków).

### Co zaimplementowano

- **Generowanie skryptu** – funkcja w DatabaseAdmin generuje skrypt który zmienia wszystkim polom typ varchar na Medium Text (nie tylko varchar, ale też CaseMessage, From His i inne systemowe)
- **Obsługa MS SQL i MySQL** – na MS SQL pola typu tekst były typu tekst (co okazało się że jest za małe), sam tekst też powinien zmieniać na Medium Text
- **Obsługa wszystkich pól** – zmienia wszystkim polom dla wszystkich procesów (nie tylko varchar, ale też inne systemowe)

### Ograniczenia / Known issues

- **Wydajność** – może być minimalnie mniej wydajne (ale większym wyzwaniem było to że pola się u niektórych klientów nie mieściły)
- **Wymaga wyłączenia aplikacji** – musi być wyłączona aplikacja, ograniczony dostęp do aplikacji (wyłączona witryna, wyłączona usługa) podczas wykonywania zmiany
- **Czas wykonania** – na dużej bazie wykorzystywanej od wielu lat może trwać pół godziny
- **Pola tekstowe krótkie vs długie** – teraz poza wyglądem nie ma różnicy pomiędzy polem tekstowym długim a krótkim od strony bazy danych (oba są Medium Text). Ograniczenie długości (255 domyślnie) pozostaje w ustawieniach pola, ale z reguły da się wpisać więcej

### Feedback z demo

- **Damian Kamiński:** Zalecenie żeby to zmianę wykonywać ręcznie i poza godzinami pracy (musi być wyłączona aplikacja)
- **Piotr Buczkowski:** Przygotuje instrukcję (jest już funkcja)
- **Łukasz Bott:** W wirtualnym polu tekstowym (AMODIT-owe krótkie) ograniczenie długości (255 domyślnie) pozostaje tak w mocy? (tak, pozostaje)
- **Piotr Buczkowski:** Teraz poza wyglądem nie ma różnicy pomiędzy polem tekstowym długim a krótkim od strony bazy danych (oba są Medium Text). Z reguły da się wpisać więcej

### Dalsze kroki

- Przygotowanie instrukcji wykonania zmiany (Piotr ma już funkcję)
- Komunikacja w piątek o możliwości wykonania zmiany
- Warto przeprowadzić taką zmianę na środowisku testowym jeśli będzie z tym problem

---

## 9. Raporty – szerokość kolumn w tabeli

**Projekt:** `moduly/Modul-raportowy`

### Cel biznesowy

Umożliwienie użytkownikom dostosowania szerokości kolumn w tabeli raportów do swoich preferencji, z zapamiętywaniem ustawień lokalnie.

### Co zaimplementowano

- **Zapamiętywanie szerokości kolumn** – każdy użytkownik może ustawić szerokość kolumn lokalnie u siebie (zapamiętywane w Cache)
- **Domyślne szerokości** – twórca raportu może zdefiniować szerokości kolumn w edycji raportu (typu tabela), użytkownikom jako domyślne te wartości będą pokazane
- **Dostosowanie do treści** – domyślnie szerokość dostosowuje się do faktycznej treści (jeśli się wszystko mieści, robi porównywalne równo)
- **Ręczne ustawienie** – można też ręcznie z poziomu edycji ustawić szerokości kolumn

### Ograniczenia / Known issues

- **Przejście do suwaka poziomego** – kwestia przejścia kiedy uznać że już powinniśmy mieć suwak poziomy, a kiedy nie, jest jeszcze do protestowania i ewentualnie wprowadzenia poprawki
- **Pole długiego tekstu** – jeśli mamy odpowiednio dużo kolumn, pozwala nam system sterować (lewa kolumna kosztem prawej). Jeśli faktycznie mamy dużo kolumn, to rozwijając wydłużamy cały raport i tutaj się odpowiednio suwak też zmniejsza. Ale jeśli mamy pole długiego tekstu, to jeszcze może coś obie ewentualnie podziałać

### Feedback z demo

- **Piotr Buczkowski:** W starych raportach, w tabeli wyświetlanej tylko do odczytu, jest po prostu dla pól numerycznych (kwota, numer) czy dla dat jest ustalana max width, żeby się akurat mieściły te wspierane wartości
- **Marek Dziakowski:** Twórca raportu może to sam zdefiniować te wielkości, jeżeli ma potrzebę po rozszerzyć to, rozszerzył i wszystkim to domyślnie się pokazuje
- **Damian Kamiński:** Domyślnie po prostu robi porównywalne równo (jeśli się wszystko mieści). Każdy może tym sterować lokalnie u siebie i to jest zapamiętywane

### Dalsze kroki

- Protestowanie i ewentualnie wprowadzenie poprawki dotyczącej przejścia kiedy uznać że już powinniśmy mieć suwak poziomy
- Rozważenie obsługi pól długiego tekstu gdy mamy dużo kolumn

---

## 10. Trust Center – poprawki w ustawieniach

**Projekt:** `moduly/Trust-Center`

### Cel biznesowy

Poprawki w Trust Center dotyczące ustawiania daty wygaśnięcia dokumentu oraz opisów do funkcji, poprawiając jasność funkcjonalności.

### Co zaimplementowano

- **Poprawki w ustawieniach** – poprawione ustawianie daty wygaśnięcia dokumentu
- **Opisy do funkcji** – poprawione opisy do funkcji (niektóre funkcjonalności były niezbyt jasne)
- **Logowanie** – poprawione logowanie (nie pamięta czy to było w ramach tego sprintu czy poprzedniego)

### Ograniczenia / Known issues

- [Brak szczegółów w transkrypcji]

### Dalsze kroki

- [Brak szczegółów w transkrypcji]


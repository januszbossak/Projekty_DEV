# Planowanie Sprintu – 2025-11-17

**Sprint:** [DO USTALENIA]
**Okres:** [DO USTALENIA]

**Powiązane projekty:**
- `klienci/WIM/Repozytorium` – tematy 1, 2
- `klienci/LOT` – tematy 3, 4
- `cross-cutting/Podglad-plikow` – temat 5
- `moduly/Trust-Center` – temat 6
- `klienci/WIM/Komunikator` – temat 7
- `cross-cutting/Automatyzacja-dokumentacji-AI` – temat 8
- `moduly/Modul-raportowy` – temat 9
- `cross-cutting/Bezpieczenstwo-sesji` – temat 10

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Repozytorium plików | `klienci/WIM/Repozytorium` | 🔄 W analizie | Rozpisane po nowemu w Azure (epik → ficzery → PBI) |
| Szablony - podgląd | `cross-cutting/Podglad-plikow` | 🔄 W testach | Ania kończy podstawową funkcjonalność (DOCX, PDF), obracanie odrzucone |
| Certyfikacja | [DO USTALENIA] | 🔄 W trakcie | Adrian rozpisał zadania (3,5 dnia poprawki, 1,5 i 2 dni szacowanie) |
| Comarch Hub | `klienci/LOT` | 🔄 W trakcie | Zakres ustalony, czekamy na dostępy, Łukasz robi, Adrian doradczo |
| Integracje (UPS, SM, Global Express) | `klienci/LOT` | 🔄 W analizie | Łukasz opracował listę pytań i wątpliwości, czekamy na potwierdzenie zakresu |
| Trust Center | `moduly/Trust-Center` | 🔄 W analizie | Mariusz z Kamilem i Markiem jako wsparciem, zakres jeszcze nieznany |
| Komunikator | `klienci/WIM/Komunikator` | 🔄 W testach | Mateusz kończy wdrożenie, czekamy na wytyczne z WIM-u odnośnie konfiguracji certyfikatów |
| Moduł raportowy - błędy | `moduly/Modul-raportowy` | 🔄 W analizie | Przemek, Barbara, Janusz, Kamil, Łukasz agregują problemy |

---

## 2. Plany na sprint

### Repozytorium plików

**Projekt:** `klienci/WIM/Repozytorium`

**Kontekst i cel:**
Repozytorium plików ma nowe podejście - wytworzona w ramach Azure rozpiska po nowemu (epik → ficzery → PBI). Jest tego dość sporo naprodukowane. Częściowo repozytorium plików mamy już zrobione (może gdzieniegdzie aż nadto rozbudowane po stronie frontendowej, będziemy to w ramach MVP gdzieś tam ucinać lub decydować, że dane przyciski nie będą na razie realizowane).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Spotkanie techniczne - omówienie struktury bazy danych i endpointów | **Damian, Adrian, Ania, Filip** | [DO USTALENIA] | Spotkanie zaplanowane na jutro (18 listopada), dokumentacja do przeczytania |
| Backend - zmiana struktury bazy danych | **Adrian, Ania** | [DO USTALENIA] | Po spotkaniu technicznym |
| Backend - endpointy | **Adrian, Ania** | [DO USTALENIA] | Po spotkaniu technicznym |
| Frontend - repozytorium plików | **Filip** | [DO USTALENIA] | Częściowo już zrobione, może być za bardzo rozbudowane |

**Szczegóły techniczne:**
- Struktura bazy danych - przygotowana przez Damiana na podstawie wytycznych Piotra
- Endpointy - wstępnie zaplanowane, dużo szerzej opisane niż w niektórych przypadkach tego potrzebujemy (może spowodować dłuższe tworzenie)
- Frontend - częściowo już zrobione, może być za bardzo rozbudowane (będziemy ucinać w ramach MVP)

**Decyzje podjęte przy planowaniu:**
- Spotkanie techniczne na jutro (18 listopada) - omówienie struktury bazy danych i endpointów
- Dokumentacja do przeczytania przed spotkaniem (pogląd ogólny w zakresie biznesowym)
- Ucinanie funkcjonalności frontendowych w ramach MVP (dane przyciski nie będą na razie realizowane)

**Ryzyka:**
- Dużo szerzej opisane niż w niektórych przypadkach tego potrzebujemy - może spowodować dłuższe tworzenie
- Pytanie, czy wszystko jest nam potrzebne - do omówienia na spotkaniu technicznym

---

### Certyfikacja

**Projekt:** [DO USTALENIA]

**Kontekst i cel:**
Adrian rozpisał zadania w ramach certyfikacji. Z tego co oszacował, było to 3,5 dnia na poprawki, 1,5 i 2 dni na szacowanie.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki certyfikacji | **Adrian** | 3,5 dnia | - |
| Szacowanie certyfikacji | **Adrian** | 1,5 + 2 dni | - |

**Decyzje podjęte przy planowaniu:**
- [DO USTALENIA]

**Ryzyka:**
- [DO USTALENIA]

---

### Comarch Hub

**Projekt:** `klienci/LOT`

**Kontekst i cel:**
Zakres jest ustalony. W tamtym tygodniu mieliśmy dostać dostępy. Łukasz ma dostęp do dokumentacji API, trzeba zaczynać programowanie. Plus potrzebujemy dostępów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z Comarch Hub | **Łukasz** | [DO USTALENIA] | Dostępy, dokumentacja API (już dostępna) |
| Wsparcie architektoniczne | **Adrian** | [DO USTALENIA] | Doradczo |

**Szczegóły techniczne:**
- Dokumentacja API - dostępna
- Dostępy - potrzebne do rozpoczęcia programowania
- Wytyczne od klienta - Michał wysłał jakieś wytyczne od klienta odnośnie tego, co by chciał mapować (Adrian i Łukasz w komunikacji z Michałem na mailu)

**Decyzje podjęte przy planowaniu:**
- Comarch Hub - pierwsza kolejność (dla Lewiatana)
- Adrian pozostaje tylko w kontekście doradczym (Łukasz robi wszystko)

**Ryzyka:**
- [DO USTALENIA]

---

### Integracje (UPS, SM, Global Express)

**Projekt:** `klienci/LOT`

**Kontekst i cel:**
Po spotkaniu w kontekście LOT-u - UPS i Global Express. Łukasz opracował listę pytań i wątpliwości, przekazał do Michała (na kanale projektowym do LOT-u). Mamy czas. Podejście: robimy to w podobny sposób jak z DHL czy FedExem, czyli po stronie AMODIT-a będzie zestaw funkcji umożliwiających wysyłkę, odbiór, sprawdzenie statusu, anulowanie przesyłki - tak jak API będzie pozwalało. Robimy MVP, czyli tyle, ile jest wymagane dla klienta i co API pozwala.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z UPS | **Łukasz** | [DO USTALENIA] | Potwierdzenie zakresu z klientem, lista pytań przekazana do Michała |
| Integracja z Global Express | **Łukasz** | [DO USTALENIA] | Potwierdzenie zakresu z klientem, lista pytań przekazana do Michała |
| Integracja z SM | **Łukasz** | [DO USTALENIA] | [DO USTALENIA] |

**Szczegóły techniczne:**
- Podejście: podobnie jak z DHL czy FedExem
- Po stronie AMODIT-a: zestaw funkcji umożliwiających wysyłkę, odbiór, sprawdzenie statusu, anulowanie przesyłki (tak jak API będzie pozwalało)
- MVP: tyle, ile jest wymagane dla klienta i co API pozwala (nie wszystko, bo to będzie bardzo dużo pracy)

**Decyzje podjęte przy planowaniu:**
- Wszystkie trzy naraz w jednym sprincie nie ma opcji (Łukasz)
- Comarch Hub - pierwsza kolejność
- Global Express i UPS - tyle, ile się da (pewnie będzie kwestia rozpoznania, połączenia, może pojedyncza funkcja wysyłająca)
- Zakres biznesowy - warto określić (te integracje mogą mieć dużo opcji, pytanie, czy wszystkie są potrzebne)
- Potwierdzenie zakresu z klientem - czekamy na potwierdzenie (Łukasz Bott)

**Ryzyka:**
- Wszystkie trzy naraz w jednym sprincie nie ma opcji
- Zakres biznesowy nieustalony - te integracje mogą mieć dużo opcji, pytanie, czy wszystkie są potrzebne
- Potwierdzenie zakresu z klientem - czekamy na potwierdzenie

---

### Szablony - podgląd (obracanie odrzucone)

**Projekt:** `cross-cutting/Podglad-plikow`

**Kontekst i problem:**
Ania kończy podstawową funkcjonalność podglądu szablonów (DOCX, PDF). Zrobiła, żeby one działały. Teraz pracowała nad tym, żeby można było je obracać. Problem jest taki, że od strony kodu jest sporo powtarzalnego kodu. Żeby to zrefaktoryzować, trzeba będzie trochę popracować, bo trzeba wydzielić element wspólny z szablonów i załączników, i zrobić z nich część wspólną, w której będą wszystkie operacje, pod tytułem zapisywanie do podglądu, tworzenie podglądu, obracanie.

**Rozważane alternatywy:**

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Obracanie szablonów | Możliwość obracania podglądów szablonów (jak w załącznikach) | ❌ Odrzucona – nikt tego nie będzie potrzebował w praktyce, każdy szablon jest plikiem cyfrowym, nie skanem, obracanie można pominąć |
| Podstawowa funkcjonalność (DOCX, PDF) | Podgląd szablonów DOCX i PDF bez obracania | ✅ Wybrana – MVP, podstawowa funkcjonalność, której nie było |

**Decyzja / Sposób realizacji**

**Status:** ✅ Zatwierdzone

Rezygnacja z obracania szablonów. Podstawowa funkcjonalność podglądu szablonów (DOCX, PDF) - MVP. Prosty podgląd ze stronicowaniem, koniec i tyle. Obracanie ma sens przy skanowaniu, gdzie ktoś odwrotnie zeskanował dokument, a tutaj będą DOCX albo PDF, które nie mogą być odwrotnie. Każdy szablon, który ktoś wgrywa, jest z zasady plikiem cyfrowym, a nie skanem. Jeśli wgra w złej formie, poprawi i wgra jeszcze raz.

**Szczegóły techniczne:**
- Podstawowa funkcjonalność: DOCX, PDF (najczęstsze formaty szablonów)
- Podgląd ze stronicowaniem
- Bez obracania, skalowania, dolnej belki (przechodzenie na kolejny szablon)
- Przycisk odświeżania - zostaje (jeśli coś się schrzani, użytkownik sobie sam z tym poradzi)

**Ryzyka:**
- [DO USTALENIA]

---

### Trust Center

**Projekt:** `moduly/Trust-Center`

**Kontekst i cel:**
Mariusz wspólnie z Kamilem i Markiem jako wsparciem. Zakres jeszcze nieznany, możliwe, że będzie bardzo mały, ponieważ im dalej w to idziemy, tym bardziej okazuje się, że właściwie możemy osiągnąć cel tym, co mamy. Prawdopodobnie będziemy szli w wizualizację struktury powiązań między sprawami na raporcie typu tabelarycznym i to była potencjalnie jedna z prac dla Marka, ale coraz bardziej wydaje mi się, że to nie jest w MVP potrzebne i niezbędne, żeby ten projekt wystartował. Drugi zakres to jest kwestia uprawnień i tutaj będę potrzebował konsultacji. W tym kontekście możliwe, że będą prace dla Mariusza. Chciałbym to z Piotrem i Januszem jeszcze omówić, bo Piotr Buła nieco zmienia spojrzenie na uprawnienia. Potencjalnie modyfikacja albo zupełnie nowy typ pola "odnośnik", żeby pokazać strukturę powiązań między sprawami, żeby pokazać drzewko, jak sprawy się między sobą wiążą, ale to też moim zdaniem nie jest MVP.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Omówienie uprawnień z Piotrem i Januszem | **Kamil, Piotr, Janusz** | [DO USTALENIA] | Spotkanie zaplanowane na jutro (18 listopada) |
| Prace koncepcyjne nad projektem Piotra Buły | **Mariusz, Kamil** | [DO USTALENIA] | Po omówieniu uprawnień |
| Wizualizacja struktury powiązań między sprawami | **Marek** | ⏸️ Odroczone | Nie jest w MVP potrzebne i niezbędne |
| Modyfikacja/nowy typ pola "odnośnik" | [DO USTALENIA] | ⏸️ Odroczone | Nie jest w MVP potrzebne |

**Szczegóły techniczne:**
- Piotr Buła nieco zmienia spojrzenie na uprawnienia
- Potencjalnie modyfikacja albo zupełnie nowy typ pola "odnośnik"
- Wizualizacja struktury powiązań między sprawami na raporcie typu tabelarycznym
- Klient ma stały schemat od 97. roku, więc nie ma co się skupiać nad super panelem do zarządzania tym schematem

**Decyzje podjęte przy planowaniu:**
- Zakres może być minimalny - coraz więcej rzeczy schodzi na dalszy tor
- Kluczowe dla Kamila aktualnie są uprawnienia - w pierwszej kolejności omówienie
- Marek może na razie w ogóle nie być angażowany (Marek jest krótszą część sprintu - wraca w piątek)
- Mariusz przez te cztery dni będzie się zajmował odpowiedziami na różne pytania w Trust Center (będzie musiał praktycznie wszystko przejąć, już dzisiaj było drugie pytanie i trzeba też zrobić poprawkę, więc godzinę do trzech godzin dziennie może mieć mniej czasu)

**Ryzyka:**
- Zakres jeszcze nieznany - możliwe, że będzie bardzo mały
- Mariusz ma mniej czasu przez odpowiedzi w Trust Center (godzinę do trzech godzin dziennie)
- Marek jest krótszą część sprintu (wraca w piątek)

---

### Komunikator

**Projekt:** `klienci/WIM/Komunikator`

**Kontekst i cel:**
Chcielibyśmy skończyć wdrożenie komunikatora. Czekamy jeszcze na wytyczne z WIM-u odnośnie konfiguracji. Trzeba będzie podpiąć odpowiednie certyfikaty. Komunikator może być częścią AMODIT-a, przynajmniej bazodanowo, mimo że jest odrębną aplikacją. Warto ustalić, jak ma być tą częścią, i na przykładzie WIM-u tutaj to w odpowiedni sposób już na teście zrobić, żebyśmy mieli to przetestowane i opisane.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Dyskusja z Piotrem o połączeniu komunikatora z AMODIT | **Mateusz, Piotr** | 1h / 0,5h | Zaplanować spotkanie |
| Podpięcie certyfikatów | **Mateusz** | [DO USTALENIA] | Wytyczne z WIM-u odnośnie konfiguracji |
| Obsługa dla chmury | **Mateusz** | ⏸️ Odroczone | Nie wiemy, ile to będzie nas kosztowało, warto przemyśleć na poziomie koncepcyjnym |

**Szczegóły techniczne:**
- Komunikator może być częścią AMODIT-a (bazodanowo)
- Na chmurze musi być w tej samej bazie, nie ma sensu robić nowej
- Na chmurze trzeba pobierać dane organizacji z osobnej bazy - trzeba zrobić zmiany specjalnie pod chmurę
- Dwa serwery - komunikator zostanie na jednym serwerze i oba serwery będą się do niego łączyć
- Baza danych - może być odrębna albo ta sama co w AMODIT (to nie ma wpływu, ale ma znaczenie w kontekście wdrażania na chmurach)

**Decyzje podjęte przy planowaniu:**
- Dyskusja z Piotrem o połączeniu komunikatora z AMODIT (zaplanować spotkanie na godzinę czy pół)
- Wytyczne powinny być raczej jedne (dla chmury i on-premise)
- Obsługa dla chmury - nie wiemy, czy chcemy, bo nie wiemy, ile to będzie nas kosztowało (warto przemyśleć przynajmniej na poziomie koncepcyjnym)
- Nie na ten sprint - trzeba z Mateuszem porozmawiać i ustalić, co chcemy osiągnąć (pisanie to ostatni krok, wcześniej trzeba zaplanować strukturę dokumentacji)

**Ryzyka:**
- Czekamy na wytyczne z WIM-u odnośnie konfiguracji certyfikatów
- Obsługa dla chmury - nie wiemy, ile to będzie nas kosztowało

---

### Dokumentacja procesu (AI)

**Projekt:** `cross-cutting/Automatyzacja-dokumentacji-AI`

**Kontekst i cel:**
Chcielibyśmy w ustawieniach procesu mieć przycisk "Generuj dokumentację", który by powodował, że AI za pomocą dostępu do całej definicji procesu i posiadając właściwie skonstruowany prompt, generuje dokumentację w określonej strukturze: tytuł, wstęp, historia zmian, gotowy szablon. Drugie miejsce, gdzie taka dokumentacja mogłaby być tworzona, to są ustawienia systemowe, np. "Przygotuj dokumentację konfiguracji AMODIT-u" i on na podstawie wiedzy by ją generował. Bliżej nam jest do tej dokumentacji procesowej, bo tu już wiele rzeczy jest zrobionych, potrzeba tylko schematu i odpowiednio skonstruowanego promptu. Robiliśmy ćwiczenia i to się da zrobić już teraz z AMODIT i Copilotem, tylko trzeba napisać sensowny prompt.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Spotkanie - pokazanie Mateuszowi, co dokładnie ma się zwracać | **Mateusz, Łukasz, Janusz** | [DO USTALENIA] | Zaplanować spotkanie |
| Implementacja przycisku "Generuj dokumentację" w ustawieniach procesu | **Mateusz** | [DO USTALENIA] | Po spotkaniu |

**Szczegóły techniczne:**
- Przycisk "Generuj dokumentację" w ustawieniach procesu
- AI z dostępem do całej definicji procesu
- Właściwie skonstruowany prompt
- Struktura dokumentacji: tytuł, wstęp, historia zmian, gotowy szablon
- Można zrobić już teraz z AMODIT i Copilotem, tylko trzeba napisać sensowny prompt

**Decyzje podjęte przy planowaniu:**
- Nie na ten sprint - trzeba z Mateuszem porozmawiać i ustalić, co chcemy osiągnąć (pisanie to ostatni krok, wcześniej trzeba zaplanować strukturę dokumentacji)
- Spotkanie - pokazanie Mateuszowi, co dokładnie ma się zwracać (zaplanować spotkanie)

**Ryzyka:**
- [DO USTALENIA]

---

### Moduł raportowy - błędy i stabilność

**Projekt:** `moduly/Modul-raportowy`

**Kontekst i cel:**
Warto by się pochylić nad błędami i niestabilnością w kontekście modułu raportowego. Janusz w tej chwili robi porządki na backlogu dotyczące modułu raportowego, żebyśmy mieli przegląd wszystkich błędów i pomysłów, żeby to spriorytetyzować i ustalić, co robimy najpierw. Będziemy ustalać takie paczki zadań, żeby mieściły się w ramach kolejnych sprintów i tak będziemy ten moduł poprawiać. Warto by było, gdyby dotychczasowy zespół – Mateusz, Marek, Ania i Przemek – spotkał się i przemyślał, co warto refaktoryzować w tym nowym module raportowym, żeby działał lepiej i był bardziej stabilny.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Agregacja problemów modułu raportowego | **Barbara, Janusz, Kamil, Łukasz** | [DO USTALENIA] | Janusz robi porządki na backlogu |
| Refaktoryzacja modułu raportowego - spotkanie zespołu | **Mateusz, Marek, Ania, Przemek** | [DO USTALENIA] | Przemyślenie, co warto refaktoryzować |
| Naprawa błędów modułu raportowego | **Przemek** | [DO USTALENIA] | Od jutra zacząć (jak będą już rozpisane) |

**Szczegóły techniczne:**
- [DO USTALENIA]

**Decyzje podjęte przy planowaniu:**
- Przemek może zacząć od jutra (jak będą już rozpisane błędów)
- Janusz postara się to dzisiaj ogarnąć
- Damian też ma coś na swojej tablicy z poprzedniego sprintu, podrzuci dzisiaj po południu
- Spotkanie zespołu (Mateusz, Marek, Ania, Przemek) - przemyślenie refaktoryzacji

**Ryzyka:**
- Mamy głosy co do nowej wersji, że nie wszystko się tam wszystkim podoba - musimy wydać tę wersję przynajmniej stabilną, żeby nie było zarzutu, że jest dużo błędów

---

### Serwisy mailowe (ACS)

**Projekt:** [DO USTALENIA]

**Kontekst i cel:**
Piotr ma kwestię tych serwisów mailowych do podpięcia (ACS). W końcu musi się tym zająć. Potencjalnie w jego kontekście może być jeszcze ten CAS. Jeżeli jego propozycja przejdzie, to nic nie trzeba będzie robić programistycznie.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Serwisy mailowe (ACS) | **Piotr** | [DO USTALENIA] | W końcu musi się tym zająć |
| CAS | **Piotr** | [DO USTALENIA] | Jeżeli propozycja przejdzie, to nic nie trzeba będzie robić programistycznie |

**Decyzje podjęte przy planowaniu:**
- [DO USTALENIA]

**Ryzyka:**
- [DO USTALENIA]

---

### Bugi i hotfixy

**Projekt:** [DO USTALENIA]

**Kontekst i cel:**
Na pierwszy rzut oka nie jest to przeładowany sprint, ale dotyczy to zadań rozwojowych, natomiast mamy dość sporo bugów. W pierwszej kolejności dobrze by było, żebyście wycenili i oszacowali to, co jest na etapie "estimating" i przypisane do was. Chcemy w końcu zrealizować te bugi, bo mamy przemyślenie z czwartku i piątku, że nie zrealizowaliśmy wszystkiego, co było przypisane na poprzedni sprint, a wskakują nowe i nie nadążamy. Warto o tym pamiętać, zwłaszcza w kontekście takim jak u Mariusza, gdzie jeszcze chwilę potrwa, zanim ustalimy zakres. Żeby podejmować bugi, jeśli nie ma nic innego do zrobienia.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Wycena i oszacowanie bugów na etapie "estimating" | **Wszyscy** | [DO USTALENIA] | W pierwszej kolejności |
| Naprawa bugów | **Wszyscy** | [DO USTALENIA] | Jeśli nie ma nic innego do zrobienia |

**Szczegóły techniczne:**
- Potencjalnie mamy setkę zgłoszeń do przypięcia na bieżący sprint
- Duża część to będą testy, które zawsze będą za nami o jeden sprint
- Spodziewamy się, że wpadnie też sporo bugów, których po prostu nie podjęliśmy w tym sprincie

**Decyzje podjęte przy planowaniu:**
- Nie możemy o nich zapominać, żeby nie przenosić ich ze sprintu na sprint - trzeba je naprawić
- Mamy głosy co do nowej wersji, że nie wszystko się tam wszystkim podoba - musimy wydać tę wersję przynajmniej stabilną, żeby nie było zarzutu, że jest dużo błędów

**Ryzyka:**
- Nie zrealizowaliśmy wszystkiego, co było przypisane na poprzedni sprint, a wskakują nowe i nie nadążamy
- Potencjalnie mamy setkę zgłoszeń do przypięcia na bieżący sprint

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Obracanie szablonów - odrzucone | `cross-cutting/Podglad-plikow` | ✅ Zatwierdzone | Nikt tego nie będzie potrzebował w praktyce, każdy szablon jest plikiem cyfrowym, nie skanem |
| Podgląd szablonów - MVP bez dolnej belki | `cross-cutting/Podglad-plikow` | ✅ Zatwierdzone | Prosty podgląd ze stronicowaniem, bez przechodzenia na kolejny szablon, przycisk odświeżania zostaje |
| Komunikator może być częścią AMODIT-a (bazodanowo) | `klienci/WIM/Komunikator` | ✅ Zatwierdzone | Na chmurze musi być w tej samej bazie, nie ma sensu robić nowej |
| Metodologia planowania sprintu - tablice w Teams | `cross-cutting/Wydajnosc` | ✅ Zatwierdzone | Wysokopoziomowe podejście, bardziej po projektach niż po zadaniach, korelacja z backlogiem na poziomie MVP |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Dużo szerzej opisane niż potrzebujemy (repozytorium) | `klienci/WIM/Repozytorium` | Średni | Spotkanie techniczne - omówienie, czy wszystko jest nam potrzebne | **Damian, Adrian, Ania, Filip** |
| Wszystkie trzy integracje naraz w jednym sprincie nie ma opcji | `klienci/LOT` | Wysoki | Comarch Hub - pierwsza kolejność, Global Express i UPS - tyle, ile się da | **Łukasz** |
| Zakres biznesowy integracji nieustalony | `klienci/LOT` | Średni | Warto określić zakres biznesowy (te integracje mogą mieć dużo opcji) | **Łukasz, Kamil** |
| Potencjalnie setka zgłoszeń do przypięcia na bieżący sprint | `moduly/Modul-raportowy` | Wysoki | Nie możemy o nich zapominać, żeby nie przenosić ich ze sprintu na sprint | **Wszyscy** |
| Nie zrealizowaliśmy wszystkiego z poprzedniego sprintu | `cross-cutting/Wydajnosc` | Wysoki | Warto o tym pamiętać, podejmować bugi, jeśli nie ma nic innego do zrobienia | **Wszyscy** |
| Mariusz ma mniej czasu przez odpowiedzi w Trust Center | `moduly/Trust-Center` | Średni | Godzinę do trzech godzin dziennie może mieć mniej czasu | **Mariusz** |
| Marek jest krótszą część sprintu (wraca w piątek) | `moduly/Trust-Center` | Średni | Może na razie w ogóle nie być angażowany | **Kamil** |

---

## 5. Organizacja pracy

- **Urlopy:** Marek - do piątku (wraca w piątek)
- **Spotkania:** 
  - Spotkanie techniczne repozytorium - jutro (18 listopada) - Damian, Adrian, Ania, Filip
  - Spotkanie uprawnień Trust Center - jutro (18 listopada) - Kamil, Piotr, Janusz
  - Spotkanie dokumentacji procesu - do zaplanowania - Mateusz, Łukasz, Janusz
  - Spotkanie refaktoryzacji modułu raportowego - do zaplanowania - Mateusz, Marek, Ania, Przemek
- **Przesunięcia:** 
  - Mateusz - wyłączony z repozytorium (błąd w pierwszej koncepcji), zajmuje się dokumentacją procesu
  - Przemek - na razie nie ma zadań rozwojowych, skupia się na błędach modułu raportowego

---

## 6. Metodologia planowania sprintu (tablice w Teams)

### Podejście do planowania

**Wysokopoziomowe podejście:**
- Tablice w Teams - bardziej po projektach niż po zadaniach
- Cel: pokazanie wysokopoziomowo, kto się czym zajmuje i jakie są główne cele sprintu
- Abstrahując od bugów i hotfixów, którymi staramy się opiekować na co dzień

**Korelacja z backlogiem:**
- Docelowo: Inicjatywa → Epik → MVP → Ficzery → Use case'y → PBI
- Repozytorium plików - MVP 1 (w ramach epika "Repozytorium MVP 1")
- Oznacza to, że zrealizujemy wszystkie punkty, które są do tego podpięte, a przez to osiągniemy określone cele biznesowe

**Zasady:**
- Nie ma czegoś takiego jak "wrzutki, bo zrób mi to czy tamto" - oprócz hotfixów (gdy u klienta coś padło, nie działa)
- Każdy inny przypadek nie jest robiony w tym sprincie - wpisujemy na listę, Damian, Kamil czy Łukasz decydują, na ile jest to ważne
- Jedyna ścieżka, żeby pozwolić sobie na takie zgłoszenie, to wy sami (dodanie zgłoszenia na bieżący sprint)
- Wszystko inne przechodzi przez PM-ów (codziennie rano na Daily poświęcamy 20 minut i bierzemy zgłoszenia z poprzedniego dnia)
- Wyjątki: serwisowe, jak Trust Center, serwis OCR (Mateusz reaguje)

**Feedback zespołu:**
- Adrian: to jest takie wysokopoziomowe, raczej nie widzimy tego na naszej tablicy, nie pokazuje questów czy dodatkowych zadań, pojedynczych PBI, jakiś bugów
- Mariusz: rozumiem w taki sposób, że na Azure mamy zadania konkretne, wydzielone dla programistów z opisem, a w Teams mamy w kategorii przedziału czasowego jako jeden sprint, jakie są ogólne założenia
- Mateusz: mi się podoba, że jest krótsze, bardziej konkretne, można sobie łatwo zobaczyć, co jest do zrobienia przez jakie osoby
- Kamil: będziemy się przewijały te wrzutki, o których mówi Adrian, ale wiadomo, ważnych hotfixów nie pomijamy, dla nas to jest ułatwienie, że wy macie cel, wiecie, że z tego w poniedziałek będziemy was pytać

---

## 7. Wydania

**Wersja grudniowa:**
- Powinna już wyjść (umawialiśmy się do połowy listopada)
- Z dopiskiem "beta" oficjalnie
- Nowości: lista pól, matryca uprawnień
- Będziemy jeszcze pakować UPS i wszystko pod LOT
- Zrezygnowaliśmy z wrześniowej, żeby wydać grudniową
- Możemy już usunąć komunikat i opcję przełączania się na stare ustawienia systemowe, testować u nas, czy wszystko zaopiekowaliśmy

**Wersja marcowa (przyszłoroczna):**
- Pojawiła się też marcowa przyszłoroczna

**Integracje (UPS, Global Express):**
- Jeśli koledzy to dobrze robią jako rozszerzenia (osobne DLL-ki), to wpięcie tego, czy pojawi się w grudniowej czy marcowej, to będzie tylko kwestia podpięcia


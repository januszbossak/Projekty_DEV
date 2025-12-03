# Notatka projektowa – 2025-10-27 – Przegląd projektów

**Data:** 2025-10-27
**Temat główny:** Przegląd projektów i przypisanie zespołów do tematów na roadmapie

**Powiązane projekty:**
- `backlog` – temat 1 (organizacja pracy projektowej)
- `backlog` – temat 2 (proces testowania)
- `moduly/Zrodla-danych` – temat 3 (GetDataSet - obsługa null)
- `moduly/Edytor-procesow-formularzy` – temat 4 (czyszczenie pola daty)
- `moduly/Trust-Center` – temat 5 (SignApp na macOS)
- `moduly/e-Doreczenia` – temat 6 (e-Doręczenia chmura)
- `integracje/KSeF` – temat 7 (KSeF - rozbudowanie połączenia)
- `klienci/PKF` – temat 8 (przekazywanie plików przez API)
- `klienci/WIM/JRWA` – temat 9 (JRWA - interfejs)
- `cross-cutting/Wzmiankowanie-w-komentarzach` – temat 10 (wzmianki)
- `integracje/Comarch-Hub` – temat 11 (Comarch Hub)
- `klienci/WIM/Repozytorium` – temat 12 (Repozytorium)
- `moduly/Modul-raportowy` – temat 13 (raporty)
- `moduly/Trust-Center` – temat 14 (blockchain/Trust Center)

---

## 1. Organizacja pracy projektowej na poziomie feature'ów/MVP

**Projekt:** `backlog`
**Komponent:** Organizacja pracy

### Cel i problem

Obecnie zespół patrzy na sprint na poziomie PBI (Product Backlog Items), co powoduje brak widoczności celów wyższego poziomu. Chodzi o to, żeby patrzeć piętro wyżej - na feature'y/MVP, które mają być dowiezione w sprincie. Przykład: w sprincie ma być dowieziona funkcjonalność "możliwość utworzenia konwersacji dla grupy AMODIT-owej" w komunikatorze. Takich feature'ów w sprincie może być 5-10 i powinny być rozpisane (np. w kwartale to dowieziemy, w tym sprincie to, w tym sprincie te dwie rzeczy). Obecnie jest "ciągła szarpanina" - przypominanie sobie co było do zrobienia, niepewność czy coś zostało dobrze zrobione.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Praca na poziomie PBI | Obecne podejście - patrzenie na sprint przez pryzmat pojedynczych zadań | ❌ Odrzucona – brak widoczności celów wyższego poziomu |
| Praca na poziomie feature'ów/MVP | Organizacja pracy wokół feature'ów/MVP z rozpisaniem na PBI | ✅ Wybrana – zapewnia widoczność celów i jasność co ma być dowiezione |
| Excel do śledzenia | Wpisywanie informacji o feature'ach w Excelu | ⏸️ Odroczona – do ustalenia jednolitego narzędzia (backlog vs Excel) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zespół będzie pracował projektowo na poziomie feature'ów/MVP. Każdy feature ma być rozpisany na PBI na backlogu. Ważne jest, żeby ludzie mieli cel - zespół (nawet wirtualny) ma cel: "wy macie dowieźć komunikator w tym terminie, koniec". "Dowieźć" powinno być zdefiniowane w `definition of done`: co komunikator ma zawierać, jaki ma mieć opis, jak ma być instalowany, dokumentacja dla wdrożeniowca itd.

**Szczegóły techniczne:**
- Narzędzie: Azure DevOps backlog (z możliwością użycia Excela jako wsparcia)
- Struktura: Feature/MVP → PBI → zadania
- Definition of Done: wymagane dla każdego feature'a

### Ograniczenia / Poza zakresem

- Brak jednolitego standardu - Kamil już działa w ten sposób, ale nie jest to standard dla wszystkich
- Czas na rozpisywanie - brak czasu na rozpisywanie nowych epiców, czasami coś jest podpinane "na siłę"

### Punkty otwarte

- Ustalenie jednolitego narzędzia do śledzenia (backlog vs Excel)
- Standaryzacja procesu dla wszystkich członków zespołu

---

## 2. Wymagane pole z informacją gdzie testowano przy przejściu na "Internal Test"

**Projekt:** `backlog`
**Komponent:** Proces testowania

### Cel i problem

Przy przejściu z "In Progress" na "Internal Test" brakuje informacji gdzie dana funkcjonalność była testowana. To powoduje problemy: tester nie wie gdzie szukać przypadku testowego, deweloper traci czas na ponowne tworzenie przypadków testowych przy poprawkach, brak zapisu na jakim środowisku i procesie testowano. Przykład: Ania testuje coś lokalnie, Damian mówi że jest źle, wraca do poprawki, ale nie ma zapisu gdzie Ania to testowała - traci czas na ponowne testy od zera.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dodanie wymaganego pola | Przy przejściu na "Internal Test" wymagane pole z informacją gdzie testowano (środowisko, proces) | ✅ Wybrana – zapewnia ślad testowy i przyspiesza kolejne iteracje |
| Opcjonalne pole | Pole dostępne, ale nie wymagane | ❌ Odrzucona – nie zapewnia wymuszenia zapisu informacji |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Przy przejściu z "In Progress" na "Internal Test" powinno być wypełnione pole z informacją gdzie testowano. Format: "przetestowane na `ania.amodit.local` na procesie takim i takim". Tester może z tego nie skorzystać (może testować po swojemu), ale informacja powinna być zapisana, żeby przy poprawkach deweloper miał przypadek który wcześniej robił, a nie robił od nowa lub szukał po omacku.

**Szczegóły techniczne:**
- Pole wymagane przy przejściu statusu: "In Progress" → "Internal Test"
- Format: środowisko + proces/przypadek testowy
- Cel: przyspieszenie kolejnych iteracji testowania

### Ograniczenia / Poza zakresem

- Nie wymusza użycia przez testera - tester może testować po swojemu, ale informacja jest dostępna

### Punkty otwarte

- Ustalenie dokładnego formatu pola (struktura danych)
- Wdrożenie w Azure DevOps

---

## 3. GetDataSet - obsługa null i wyszukiwania

**Projekt:** `moduly/Zrodla-danych`
**Komponent:** Źródła danych

### Cel i problem

Funkcja GetDataSet ma braki w obsłudze wartości null i wyszukiwania. Nie dało się wyszukiwać po `null`, gdy `query` nie zwracało wyników był błąd, nie dało się przypisać wartości z pola. Dla pola typu data trzeba było ręcznie sprawdzać `if (pole_data == null) { warunek = "IS NULL"; } query = query + warunek;`. Problem wyszedł dopiero przy użyciu produkcyjnym w WIM - wcześniej był uproszczony tryb, nie był określony motyw jak będziemy z tego korzystać.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Automatyczna obsługa null przez system | System sam rozpoznaje gdy pole jest puste (null) i podstawia odpowiedni warunek | ✅ Wybrana – upraszcza użycie, nie trzeba ręcznie sprawdzać każdego pola |
| Ręczna obsługa przez użytkownika | Użytkownik musi sam sprawdzać pola i dodawać warunki | ❌ Odrzucona – zbyt skomplikowane, nieintuicyjne |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

System powinien automatycznie obsługiwać wartości null. Jak pole jest puste, system ma wiedzieć, że to `null` i sam to podstawić. Nie trzeba przed każdym `WHERE` sprawdzać dziesięciu pól. Funkcja wymaga rozwoju o obsługę null, o której mogliśmy nie myśleć na początku (była wersja MVP).

**Szczegóły techniczne:**
- Funkcja: GetDataSet
- Problem: brak obsługi null, wyszukiwania po null, błędów przy pustych wynikach
- Rozwiązanie: automatyczna obsługa null przez system

### Ograniczenia / Poza zakresem

- Warunki brzegowe nie zawsze da się przewidzieć - najlepiej od razu podać przypadek użycia
- Może się okazać, że funkcjonalność działa, ale na danych klienta nie, bo nikt nie przewidział takich danych

### Punkty otwarte

- Implementacja automatycznej obsługi null
- Obsługa błędów przy pustych wynikach query
- Możliwość przypisania wartości z pola

---

## 4. Czyszczenie pola daty/czasu w edytorze formularza

**Projekt:** `moduly/Edytor-procesow-formularzy`
**Komponent:** Edytor Formularza

### Cel i problem

Nie da się wyczyścić pola daty w edytorze formularza. Każde inne pole można wyczyścić, ale pole daty nie - jak się skasuje i spróbuje zapisać, jest błąd. Problem dotyczy pól daty i czasu - może powinien być jeden komponent do wyboru daty i czasu zamiast dwóch osobnych.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Kosz powinien czyścić całość (datę i czas) | Gdy używa się kosza, powinien on mieć odniesienie do całości (zarówno daty jak i czasu) | ⏸️ Odroczona – wymaga zmiany interfejsu, może nie być intuicyjne |
| Możliwość wyczyszczenia pola daty (minimum) | Bez zmiany interfejsu, minimum - trzeba móc wyczyścić pole | ✅ Wybrana – minimum funkcjonalności bez zmiany UI |
| Jeden komponent daty i czasu | Zmiana na jeden komponent zamiast dwóch osobnych | ⏸️ Odroczona – wymaga większych zmian |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Minimum funkcjonalności: trzeba móc wyczyścić pole daty. Jak używa się kosza, chce się pozbyć wartości. Jak chce się zmienić, wybierze się inne. To jest minimum bez zmiany interfejsu.

**Szczegóły techniczne:**
- Problem: pole daty nie można wyczyścić (błąd przy zapisie)
- Rozwiązanie: możliwość wyczyszczenia pola daty (minimum)
- Komponenty: obecnie dwa osobne (data i czas), rozważany jeden komponent

### Ograniczenia / Poza zakresem

- Zmiana interfejsu na jeden komponent daty i czasu - odroczona
- Kosz czyszczący całość (datę i czas) - może nie być intuicyjne (gdy widzisz tylko wybór daty, nie spodziewasz się że wyczyści też godzinę)

### Punkty otwarte

- Rozważenie zmiany na jeden komponent daty i czasu
- Ustalenie czy kosz powinien czyścić całość czy tylko wybraną część

---

## 5. SignApp na macOS - MVP 1

**Projekt:** `moduly/Trust-Center`
**Komponent:** SignApp

### Cel i problem

Prototyp SignApp na macOS został pokazany przez Adriana - napisany w czymś nowszym niż React, to samo co mamy tylko po nowemu. Był na pół ekranu, nie może tak wyjść produkcyjnie. Pytanie o zakres MVP 1 - czy potrzebujemy czegoś więcej niż podstawowy ekran? "Wyczyść certyfikat" to za dużo dla domyślnego ekranu, bo to opcja dla definiowania domyślnego certyfikatu.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Podstawowy ekran bez "Wyczyść certyfikat" | MVP 1 z podstawowym ekranem, bez opcji "Wyczyść certyfikat" | ✅ Wybrana – odpowiedni zakres dla MVP 1 |
| Ekran z opcją "Wyczyść certyfikat" | Włączenie opcji czyszczenia certyfikatu do MVP 1 | ❌ Odrzucona – za dużo dla domyślnego ekranu |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

MVP 1 dla SignApp na macOS to podstawowy ekran bez opcji "Wyczyść certyfikat" (to opcja dla definiowania domyślnego certyfikatu, nie dla domyślnego ekranu). Powinniśmy wydać wersję prototypową dla klienta do testów, zanim uzyskamy certyfikację. Uzyskanie certyfikacji jest możliwe (jak na Windowsie pojawia się "niezaufany wystawca"), ale nie wiadomo ile to potrwa.

**Szczegóły techniczne:**
- Technologia: coś nowszego niż React (to samo co mamy, tylko po nowemu)
- Zakres MVP 1: podstawowy ekran bez "Wyczyść certyfikat"
- Certyfikacja: wymagana, czas nieznany

### Ograniczenia / Poza zakresem

- Opcja "Wyczyść certyfikat" - poza MVP 1
- Pełna certyfikacja - czas nieznany

### Punkty otwarte

- Czas uzyskania certyfikacji
- Wydanie wersji prototypowej dla klienta przed certyfikacją

---

## 6. Przypisanie zespołów do tematów na roadmapie

**Projekt:** `backlog`
**Komponent:** Organizacja pracy

### Cel i problem

Potrzeba przypisania zespołów do tematów które muszą być zrealizowane w najbliższym sprincie. Każdy powinien mieć cel i zespół (nawet wirtualny). Priorytety: WIM i LOT są kluczowe dla firmy, reszta jest nieważna. Trzeba przeglądać tablicę i patrzeć na czym można zarobić.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przypisanie zespołów do tematów | Każdy temat ma przypisany zespół i cel | ✅ Wybrana – zapewnia jasność odpowiedzialności |
| Praca bez przypisania | Obecne podejście - brak jasnego przypisania | ❌ Odrzucona – brak celu dla ludzi |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Przypisano zespoły do tematów na roadmapie:

**Backend:**
- **Damian + Ania:** Backend (Ania może być dostępna, jej obecne zadania są do skreślenia ad hoc)
- **Piotr + Adrian:** Zajęci, nie liczyć że cokolwiek ruszą w tym sprincie

**Projekty:**
- **Adrian:** SignApp na macOS (MVP 1) - z Kamil, dokończyć, Damian czeka. Comarch Hub - z Łukasz, wycenione na 18 000 zł, może być cały tydzień pracy
- **Marek:** Dodawanie dokumentów do blockchain (kwestie bezpieczeństwa, coś się wykrzacza na produkcji, pilne). JRWA - interfejs (główny cel)
- **Mariusz:** Wzmianki (ważny temat, nie działa, klienci zgłaszają - Neuca i my, nie odświeża się, problemy z działaniem)
- **Łukasz:** Comarch Hub (integracja)
- **Piotr:** Swoje rzeczy które musi podokańczać (trzeba wejść i ustalić co jest ważne)
- **Ania:** Repozytorium (powinna się skupić na repozytorium, nie na tłumaczeniach)
- **Przemek:** Edytor formularza (usprawnienia w edytorze graficznym formularza)
- **Filip:** Lista pól (z Kamil, backend jest zrobiony) + matryca uprawnień

**Priorytety:**
- PKF: przekazywanie plików przez API (2 GB) - 50 000 zł faktury, bloker dla rozliczenia 53 000 zł, natychmiast
- WIM i LOT: kluczowe dla firmy
- Edytor reguł/diagramów: może poczekać

**Szczegóły techniczne:**
- Narzędzie: Excel z kolumną "Zespół" + roadmapa na backlogu
- Tryb awaryjny: póki nie ma zapasu dla deweloperów, rozpiszemy feature, rozpiszemy PBI pod nim

### Ograniczenia / Poza zakresem

- Nie wszystkie tematy są spisane - trzeba wziąć tablicę Piotra i uzupełnić
- Sporo tematów już skończonych albo zaraz będzie - trzeba uzupełniać roadmapę

### Punkty otwarte

- Uzupełnienie roadmapy wszystkimi tematami z tablicy Piotra
- Ustalenie priorytetów dla Piotra (co jest ważne, a co nie)
- Uzupełnienie tematów które są już skończone lub zaraz będą

---

## 7. e-Doręczenia chmura

**Projekt:** `moduly/e-Doreczenia`
**Komponent:** e-Doręczenia

### Cel i problem

Temat zupełnie niezaopiekowany. Łukasz przekazał analizę. Jest potrzeba frontendu i backendu. Czekają na informacje od PM-a, na jaki zakres umawiają się z LOT-em do końca roku, bo muszą pochwalić się wdrożeniem. Negocjują co realnie dowieziemy.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przypisanie zespołu | Kamil dopisany do tematu | ✅ Wybrana – temat ma opiekuna |
| Brak przypisania | Temat bez opiekuna | ❌ Odrzucona – temat niezaopiekowany |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Kamil dopisany do tematu e-Doręczenia chmura. Temat wymaga frontendu i backendu. Czekają na informacje od PM-a o zakresie umowy z LOT-em do końca roku. Muszą wydać pieniądze, dowieźć sukces, a resztę zrobi się potem.

**Szczegóły techniczne:**
- Wymagania: frontend + backend
- Klient: LOT
- Status: czekanie na zakres od PM-a

### Ograniczenia / Poza zakresem

- Zakres nieustalony - czekanie na informacje od PM-a

### Punkty otwarte

- Zakres umowy z LOT-em do końca roku
- Co realnie dowieziemy
- Analiza Łukasza - szczegóły

---

## 8. KSeF - rozbudowanie połączenia

**Projekt:** `integracje/KSeF`
**Komponent:** KSeF Connector

### Cel i problem

KSeF wymaga rozbudowania połączenia. Jest szansa, że to będzie po stronie KSeF, a po naszej ewentualnie funkcja do odczytu. Tryb awaryjny jest po to, żeby dokonać płatności poza KSeF. Wdrażanie kogoś nowego będzie trudne.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Rozbudowanie połączenia | Po stronie KSeF lub po naszej (funkcja do odczytu) | ✅ Wybrana – Damian w temacie KSeF, więc niech zostanie w jednym miejscu |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Damian zaopiekuje temat KSeF (jest w temacie KSeF, więc niech to zostanie w jednym miejscu). Rozbudowanie połączenia - jest szansa że będzie po stronie KSeF, a po naszej ewentualnie funkcja do odczytu. Kamil doda Damiana do czatu z Piotrem.

**Szczegóły techniczne:**
- Tryb awaryjny: dokonanie płatności poza KSeF
- Rozbudowanie: po stronie KSeF lub funkcja do odczytu po naszej
- Opiekun: Damian

### Ograniczenia / Poza zakresem

- Wdrażanie kogoś nowego będzie trudne

### Punkty otwarte

- Ustalenie czy rozbudowanie będzie po stronie KSeF czy po naszej
- Szczegóły funkcji do odczytu (jeśli po naszej)

---

## 9. PKF - przekazywanie plików przez API (2 GB)

**Projekt:** `klienci/PKF`
**Komponent:** Integracja REST

### Cel i problem

Klient PKF potrzebuje przekazywania plików przez API rzędu 2 GB. Piotr powiedział, że trzeba zrobić dedykowany endpoint. To jest 1-2 dni pracy. Wycena: Piotr wycenił na 2 dniówki, Damian przekazał 3, to da 50 000 zł faktury. To jest bloker dla rozliczenia o wartości 53 000 zł.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dedykowany endpoint | Stworzenie dedykowanego endpointu do przekazywania dużych plików (2 GB) | ✅ Wybrana – natychmiastowy priorytet, wysoka wartość |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Natychmiastowy priorytet. Trzeba zrobić dedykowany endpoint do przekazywania plików przez API (2 GB). Wycena: 2-3 dniówki = 50 000 zł faktury. Bloker dla rozliczenia 53 000 zł. W projekcie są 9 wolnych man-dayów, można zażądać przeksięgowania na nas.

**Szczegóły techniczne:**
- Rozmiar plików: 2 GB
- Rozwiązanie: dedykowany endpoint
- Szacunek: 1-2 dni (Piotr) / 3 dniówki (Damian)
- Wartość: 50 000 zł faktury

### Ograniczenia / Poza zakresem

- Brak

### Punkty otwarte

- Ustalenie dokładnego zakresu endpointu
- Przeksięgowanie man-dayów na nas

---

## 10. JRWA - interfejs

**Projekt:** `klienci/WIM/JRWA`
**Komponent:** Repozytorium

### Cel i problem

JRWA (Jednolity Rzeczowy Wykaz Akt) wymaga interfejsu. Pierwszy krok robi Piotr, ale interfejs jest do zrobienia. To jest repozytorium - to co robili LOT-owi na prezentacji jest oparte o stare repozytorium, tylko nie spełnia wymagań. Janusz wolałby mieć jedno repozytorium, a nie dwa. Damian planuje repozytorium plików (bez odniesienia do spraw), ale Murawski chce "głupie repozytorium".

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Marek robi interfejs JRWA | Główny cel dla Marka | ✅ Wybrana – Marek ma cel, idealnie pasuje |
| Piotr robi interfejs | Piotr robi pierwszy krok, ale interfejs też | ❌ Odrzucona – Piotr ma inne priorytety |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Marek robi interfejs JRWA jako główny cel. To jest repozytorium - trzeba przedyskutować czy będzie jedno repozytorium czy dwa. Janusz wolałby jedno repozytorium. Damian planuje repozytorium plików (bez odniesienia do spraw), ale Murawski chce "głupie repozytorium". To jest robota, nad którą powinni siedzieć i gadać.

**Szczegóły techniczne:**
- Projekt: JRWA (Jednolity Rzeczowy Wykaz Akt)
- Zadanie: interfejs (Marek)
- Kontekst: repozytorium (stare vs nowe, jedno vs dwa)

### Ograniczenia / Poza zakresem

- Decyzja o architekturze repozytorium - wymaga dyskusji

### Punkty otwarte

- Czy będzie jedno repozytorium czy dwa?
- Architektura repozytorium - repozytorium plików vs repozytorium ze sprawami
- Dyskusja z Murawskim o wymaganiach

---

## 11. Wzmianki (@mention)

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`
**Komponent:** Komentarze

### Cel i problem

Wzmianki nie działają poprawnie - nie odświeżają się, są problemy żeby to dobrze działało. Zgłosiła to Neuca i my. To jest ważny temat, bo klienci to zgłaszają.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Mariusz robi wzmianki | Przypisanie tematu do Mariusza | ✅ Wybrana – ważny temat, klienci zgłaszają |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Mariusz robi wzmianki jako główny cel. To jest ważny temat, bo nie działa i klienci to zgłaszają (Neuca i my). Problem: nie odświeża się, są problemy żeby to dobrze działało.

**Szczegóły techniczne:**
- Problem: nie odświeżają się, problemy z działaniem
- Zgłoszenia: Neuca i my
- Opiekun: Mariusz

### Ograniczenia / Poza zakresem

- Brak

### Punkty otwarte

- Szczegółowa analiza problemów z odświeżaniem
- Rozwiązanie problemów z działaniem

---

## 12. Comarch Hub

**Projekt:** `integracje/Comarch-Hub`
**Komponent:** Integracja

### Cel i problem

Integracja z Comarch Hub jest wyceniona na 18 000 zł. Może być cały tydzień pracy dla Adriana. Łukasz jest przypisany do tematu, ale nie ma go na roadmapie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Łukasz robi Comarch Hub | Przypisanie tematu do Łukasza | ✅ Wybrana – Łukasz jest w temacie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Łukasz robi Comarch Hub. Integracja wyceniona na 18 000 zł, może być cały tydzień pracy dla Adriana. Trzeba dopisać na roadmapę.

**Szczegóły techniczne:**
- Wycena: 18 000 zł
- Szacunek: cały tydzień pracy
- Opiekun: Łukasz

### Ograniczenia / Poza zakresem

- Brak

### Punkty otwarte

- Dopisanie na roadmapę
- Szczegóły integracji

---

## 13. Repozytorium

**Projekt:** `klienci/WIM/Repozytorium`
**Komponent:** Repozytorium

### Cel i problem

Ania powinna się skupić na repozytorium. Obecnie robi tłumaczenia, co nie jest w ogóle istotne. Dla niej był podgląd szablonów (15 dni), ale to jest grubsza sprawa - może na razie nie.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Ania skupia się na repozytorium | Przypisanie Ani do repozytorium zamiast tłumaczeń | ✅ Wybrana – repozytorium jest ważniejsze |
| Ania robi podgląd szablonów | Przypisanie do podglądu szablonów (15 dni) | ❌ Odrzucona – grubsza sprawa, może na razie nie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ania powinna się skupić na repozytorium. Nie dawać jej podglądu szablonów (grubsza sprawa, może na razie nie). Tłumaczenia nie są istotne.

**Szczegóły techniczne:**
- Opiekun: Ania
- Priorytet: repozytorium
- Poza zakresem: tłumaczenia, podgląd szablonów (na razie)

### Ograniczenia / Poza zakresem

- Podgląd szablonów - grubsza sprawa, może na razie nie
- Tłumaczenia - nieistotne

### Punkty otwarte

- Szczegóły zadań w repozytorium dla Ani

---

## 14. Moduł raportowy

**Projekt:** `moduly/Modul-raportowy`
**Komponent:** Raporty

### Cel i problem

Z raportami coś się zadeklarowaliśmy w umowie, ale jak zrobimy dwa, to przymkną na to oko. Przemek jest od Reacta, moduł jest w React - można tam coś znaleźć. Janusz się tym raportom przyjrzy szczegółowo. Jeśli nie, Damian zrobi raporty systemowe na ich środowisku i nawet nie będą wiedzieć, czy to systemowy, czy zrobiony przez niego.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Zrobienie dwóch raportów | Zgodnie z umową, przymkną na resztę | ✅ Wybrana – zgodne z umową |
| Raporty systemowe na środowisku klienta | Damian zrobi raporty systemowe, klient nie będzie wiedział | 💡 Rozważana – alternatywa jeśli nie zrobimy zgodnie z umową |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Z raportami coś się zadeklarowaliśmy w umowie, ale jak zrobimy dwa, to przymkną na to oko. Janusz się tym raportom przyjrzy szczegółowo. Przemek jest od Reacta, moduł jest w React - można tam coś znaleźć dla niego. Alternatywa: Damian zrobi raporty systemowe na ich środowisku i nawet nie będą wiedzieć, czy to systemowy, czy zrobiony przez niego.

**Szczegóły techniczne:**
- Moduł: React
- Opiekun: Przemek (może coś znaleźć)
- Status: Janusz przyjrzy się szczegółowo

### Ograniczenia / Poza zakresem

- Brak

### Punkty otwarte

- Szczegółowy przegląd raportów przez Janusza
- Ustalenie które raporty zrobić
- Czy Przemek znajdzie coś w module raportowym

---

## 15. Blockchain/Trust Center - dodawanie dokumentów

**Projekt:** `moduly/Trust-Center`
**Komponent:** Trust Center

### Cel i problem

Dodawanie dokumentów do blockchain ma kwestie bezpieczeństwa - coś się wykrzacza na produkcji. Piotr mówił, że trzeba to pilnie zaopiekować. Jest jakiś wyścig, bo są dwa serwery i coś się krzaczy. W zeszłym tygodniu Rossmann w jeden dzień puścił 10 000 dokumentów do Trust Center, co zwiększa prawdopodobieństwo wystąpienia takich błędów.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Marek zaopiekuje temat | Marek cały ten tydzień robi, później jest wolny | ✅ Wybrana – pilne, kwestie bezpieczeństwa |
| Odłożenie na później | Temat niepilny | ❌ Odrzucona – pilne, kwestie bezpieczeństwa |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Marek zaopiekuje temat dodawania dokumentów do blockchain. To są kwestie bezpieczeństwa, coś się wykrzacza na produkcji, trzeba to pilnie zaopiekować. Jest jakiś wyścig, bo są dwa serwery i coś się krzaczy. Marek cały ten tydzień robi, później jest wolny. Krytyczne w tym sensie, że tak, ale to się daje naprawiać - tych błędów występuje kilka na kwartał i Marek to naprawia ręcznie. W zeszłym tygodniu Rossmann w jeden dzień puścił 10 000 dokumentów do Trust Center, co zwiększa prawdopodobieństwo wystąpienia błędów.

**Szczegóły techniczne:**
- Problem: wyścig między dwoma serwerami, coś się krzaczy
- Skala: Rossmann - 10 000 dokumentów w jeden dzień
- Częstotliwość błędów: kilka na kwartał (naprawiane ręcznie przez Marka)
- Opiekun: Marek

### Ograniczenia / Poza zakresem

- Brak

### Punkty otwarte

- Szczegółowa analiza problemu wyścigu między serwerami
- Rozwiązanie problemu bezpieczeństwa

---

## Propozycja podziału na pakiety prac (MVP)

Nie dyskutowano szczegółowego podziału na MVP - skupiono się na przypisaniu zespołów do tematów na najbliższy sprint.

---

## Punkty do dalszej dyskusji (globalne)

- Ustalenie jednolitego narzędzia do śledzenia feature'ów/MVP (backlog vs Excel)
- Standaryzacja procesu organizacji pracy projektowej dla wszystkich członków zespołu
- Dyskusja o architekturze repozytorium - jedno vs dwa, repozytorium plików vs repozytorium ze sprawami
- Szczegółowy przegląd raportów przez Janusza
- Uzupełnienie roadmapy wszystkimi tematami z tablicy Piotra
- Ustalenie priorytetów dla Piotra (co jest ważne, a co nie)


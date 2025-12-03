> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Zaktualizowano nagłówek o właściwe przypisanie projektu. Skorygowano błąd merytoryczny: "AD" w kontekście archiwum to ADE (Archiwum Dokumentów Elektronicznych), a nie Active Directory. Ujednolicono nazwisko Łukasza Brockiego. Przypisano tematy do nowych projektów (`Integracja-UPS`, `Global-Express`, `Przechowywanie-plikow`, `Integracja-CAS`, `ADE`, `SIEM`, `Comarch-HUB`). Dodano kontekst cytatów Janusza Bossaka i Damiana Kaminskiego.

# Planowanie Sprintu – 2025-11-17

**Sprint:** [DO USTALENIA]
**Okres:** [DO USTALENIA]
**Projekty:** `Klienci/WIM/Repozytorium-plikow-DMS`, `Klienci/WIM/Komunikator`, `Integracje/Integracja-CAS`, `Klienci/LOT/JRWA`, `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`, `Klienci/LOT/ADE`, `Klienci/LOT/Integracjai-SIEM`, `Klienci/Lewiatan/Comarch-HUB`, `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`, `Klienci/PKF/Przechowywanie-plikow`, `Moduly/Trust-Center`, `cross-cutting/Interfejs-sprawy/Podglad-szablonow`, `cross-cutting/Automatyzacja-dokumentacji-AI`, `Moduly/Modul-raportowy`, `cross-cutting/Bezpieczenstwo-pentesty`, `Moduly/Ustawienia-systemowe`

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Komunikator | `Klienci/WIM/Komunikator` | ✅ Ukończone | Mateusz kończy, są drobne błędy (nie funkcjonalne, tylko przesuwanie, zmiana nazwy), grupy działają. Został **wgrany do klienta (WIM)** i na ten moment kończymy pracę w ramach MVP, czekamy na potencjalne uwagi klienta. |
| Repozytorium - opis | `Klienci/WIM/Repozytorium-plikow-DMS` | ✅ Ukończone | Piotr napisał opis koncepcyjny. |
| Integracja z CAS | `Integracje/Integracja-CAS` | 🔄 W trakcie | Piotr dostał wytyczne wczoraj, ma kompletny opis. Piotr estymował to na kilka godzin pracy, ale wycena mówi o 10 dniówkach z dużym zapasem, bo "nie jest to wyzwanie". |

---

## 2. Plany na sprint

### Repozytorium plików (MVP)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Moduł repozytorium plików w systemie ma na celu umożliwienie przechowywania plików poza sprawami. Kluczowe założenie: moduł będzie częścią AMODIT, jednak pliki będą zapisywane w tabeli `CaseAttachment`, tak jak pliki załączone do spraw. **Janusz Bossak:** "To dość rewolucyjna zmiana koncepcji w stosunku do tego, co żeśmy początkowo myśleli, ale dobrze." Wykorzystuje istniejącą infrastrukturę (około 50% rzeczy już mamy). Frontend w zasadzie mamy, trzeba go połączyć z backendem.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja MVP repozytorium (podstawowa struktura organizacyjna, CRUD, system uprawnień dla folderów pierwszego poziomu) | **Adrian** (proponowany) | [nie określono] | Czeka na zakończenie innych zadań Adriana |
| Dodanie kolumn w `CaseAttachment` określających, że wpis jest plikiem repozytorium | [do przypisania] | [nie określono] | - |
| Dodanie tabel: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory` | [do przypisania] | [nie określono] | - |
| Implementacja struktury fizycznej plików (podział na lata) | [do przypisania] | [nie określono] | - |
| Indeksowanie plików repozytorium (Lucene) | [do przypisania] | [nie określono] | - |

**Szczegóły techniczne:**
- Tabela: `CaseAttachment` (wykorzystanie istniejącej).
- Nowe tabele: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory`.
- Struktura fizyczna: główny katalog "Repository", podział na lata (2025, 2026, etc.).
- Klasa: `AmodThumbnail` – generowanie podglądu standardowo jak teraz.
- Konfiguracja: zgodnie z konfiguracją załączników (dysk, Blob).
- Mechanizm skanów: wykorzystanie istniejącego mechanizmu skanów (pliki nieprzypisane do sprawy, luźne elementy).
- **Janusz Bossak:** "Struktura logiczna w aplikacji (przestrzenie, foldery) będzie rozbieżna ze strukturą fizyczną (lata)." "Nazwy plików będą modyfikowane (dodawany AttachmentID jako prefiks)."

**Decyzje podjęte przy planowaniu:**
- Wykorzystanie istniejącej tabeli `CaseAttachment` zamiast tworzenia nowej struktury.
- Struktura fizyczna po latach (możliwość dodatkowego podziału na miesiące).
- Struktura logiczna w aplikacji (przestrzenie, foldery) będzie rozbieżna ze strukturą fizyczną (lata) - zaakceptowane jako trade-off.
- System uprawnień tylko dla folderów pierwszego poziomu w MVP.
- Nazwy plików będą modyfikowane (dodawany AttachmentID jako prefiks) aby uniknąć konfliktów.

---

### Certyfikacja (SignApp)

**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

**Kontekst i cel:**
Adrian rozpisał zadania w ramach certyfikacji. Z tego co oszacował, było to 3,5 dnia na poprawki, 1,5 i 2 dni na szacowanie.
**Bloker:** Dalej **czeka na zatwierdzenie konta przez Apple**.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki certyfikacji | **Adrian** | 3,5 dnia | - |
| Szacowanie certyfikacji | **Adrian** | 1,5 + 2 dni | - |

---

### Comarch Hub

**Projekt:** `Klienci/Lewiatan/Comarch-HUB`

**Kontekst i cel:**
Integracja z Comarch Hub (dla klienta Lewiatan). Zakres ustalony. W tamtym tygodniu mieliśmy dostać dostępy. Łukasz Brocki ma dostęp do dokumentacji API, trzeba zaczynać programowanie. Plus potrzebujemy dostępów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z Comarch Hub | **Łukasz Brocki** | [DO USTALENIA] | Dostępy, dokumentacja API (już dostępna) |
| Wsparcie architektoniczne | **Adrian** | [DO USTALENIA] | Doradczo |

**Szczegóły techniczne:**
- Dokumentacja API - dostępna.
- Dostępy - potrzebne do rozpoczęcia programowania.
- Wytyczne od klienta - Michał wysłał jakieś wytyczne od klienta odnośnie tego, co by chciał mapować (Adrian i Łukasz Brocki w komunikacji z Michałem na mailu).

**Decyzje podjęte przy planowaniu:**
- Comarch Hub - pierwsza kolejność (dla Lewiatana).
- Adrian pozostaje tylko w kontekście doradczym (Łukasz Brocki robi wszystko).

---

### Integracje dla LOT

**Projekt:** `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`, `Klienci/LOT/ADE`, `Klienci/LOT/Integracjai-SIEM`

**Kontekst i cel:**
Dla klienta LOT trzeba zrealizować integracje do końca roku (przynajmniej w zakresie MVP):
1. **UPS** – integracja z firmą kurierską UPS.
2. **Global Express** – kolejna firma kurierska.
3. **ADE (Archiwum Dokumentów Elektronicznych)** – integracja z archiwum państwowym.
4. **SIEM (System Mailowy)** - prawdopodobnie integracja z SIEM.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z UPS | **Łukasz Brocki** (proponowany) | [nie określono] | Czeka na kontakt z osobą opiekującą się LOT ze strony UPS. |
| Integracja z Global Express | **Łukasz Brocki** (proponowany) | [nie określono] | Trzeba rozpoznać, czy mają jakieś API. |
| Analiza integracji z ADE (scenariusze użycia, przypadki użycia) | Dział wdrożeń | [nie określono] | Muszą pozyskać scenariusze użycia od klienta. |
| Ewentualna implementacja integracji z ADE (jeśli nie da się przez COLA REST) | [do przypisania] | [nie określono] | Po analizie scenariuszy użycia. |
| Integracja z SIEM | **Łukasz Brocki** (proponowany) | [nie określono] | [DO USTALENIA] |

**Szczegóły techniczne:**
- UPS: podobnie jak FedEx czy DHL, jako kolejny moduł.
- Global Express: trzeba rozpoznać API.
- ADE: możliwe że wystarczy użycie COLA REST API (dział wdrożeń może to zrobić bez dedykowanego modułu AMODIT).
- SIEM: wymaga analizy, co dokładnie jest potrzebne.

**Decyzje podjęte przy planowaniu:**
- UPS i Global Express: trzeba zrobić jako dedykowane integracje (LOT ma konkretne umowy z tymi firmami).
- ADE: alternatywa – czy robić jako moduł AMODIT (interfejs, backend, funkcje, reguły) czy jako MVP przez COLA REST API (dział wdrożeń może to zrobić samodzielnie).
- Decyzja o ADE: najpierw analiza scenariuszy użycia, potem decyzja czy robić dedykowany moduł czy wystarczy COLA REST.
- Jeśli ADE przez COLA REST: możemy pomóc kolegom skonfigurować, przygotować COLA REST, powiedzieć jak wykorzystywać, jakie parametry przekazywać (**brak zarobku dla działu Dev, ale dowóz funkcjonalności**).

**Uwagi:**
- Pomysł na przyszłość: integracja z brokerem kurierskim "Apaczka" (ma integrację ze wszystkimi firmami kurierskimi w Polsce) – wymaga zbadania kosztów i prowizji.

---

### JRWA dla LOT

**Projekt:** `Klienci/LOT/JRWA`

**Kontekst i cel:**
JRWA (Jednolity Rzeczowy Wykaz Akt) to działanie normatywne. Każdy dokument musi być podpięty pod JRWA. To będzie wykonywane setki razy dziennie, więc musi być robione płynnie i wygodnie – **"to nie może być 15 kliknięć, bo nas po prostu zabiją"**. Główne zastrzeżenie do systemów z DI: niewygodnie, nielogiczne, trzeba bardzo wiele klikać. Główna kwestia to pole "Odnośnik", które by po strukturze JRWA się poruszało.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Projektowanie i implementacja "Asystenta klasyfikacji" (pole odnośnik z okienkiem klasyfikatora JRWA) | [do przypisania] | [nie określono] | Wymaga dedykowanego spotkania designowego |

**Uwagi:**
- Janusz wygenerował około 100+ przypadków użycia dla JRWA, **używając GPT do generowania i weryfikacji**. Trzeba je zgłębiać i ewentualnie dopisywać nowe.

---

### Podpisywanie na Macu przez Szafira (WIM)

**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

**Kontekst i cel:**
Klient WIM potrzebuje obsługi podpisywania na Macu przez Szafira. Istnieje gotowe rozwiązanie: SimpleSign (245 zł), ale klient uparł się na Szafira. **Janusz Bossak:** "SimpleSign – najprostsze z możliwych rozwiązań, no – ale jakoś nie – uparł się – jak głupi – jeden człowiek – i robimy."

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja obsługi podpisywania na Macu przez Szafira | **Adrian** | [nie określono] | Adrian już to ogarnięte |
| Poprawa podwójnego PINu dla Szafira | **Adrian** | [nie określono] | Konieczna (regres względem Windows). |

---

### Konfiguracja folderów per proces (PKF)

**Projekt:** `Klienci/PKF/Przechowywanie-plikow`

**Kontekst i cel:**
PKF chce konfigurować, w którym folderze mają być pliki załączone do spraw – per proces. Piotr Myszkowski mówi, że już mamy taki mechanizm na poziomie pola typu dokument. Można to łatwo rozszerzyć na poziomie procesu. Kontekst dla pytania "po co?": Janusz Bossak przywołuje przykład Mateusza Pietrzaka (link do TrustCenter, rola obserwator), aby podkreślić wagę zadawania pytania "po co?".

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozszerzenie mechanizmu konfiguracji folderów na poziomie procesu | [do przypisania] | [nie określono] | Czeka na wyjaśnienie potrzeby biznesowej |

---

### Szablony - podgląd

**Projekt:** `cross-cutting/Interfejs-sprawy/Podglad-szablonow`

**Kontekst i problem:**
Ania kończy podstawową funkcjonalność podglądu szablonów (DOCX, PDF). Problem jest taki, że obracanie nie działa i po kliknięciu wyjście wraca do załączników, nie do szablonów. Przemek Sołdacki sugeruje zmianę UX (klik = podgląd), ale Kamil broni obecnego (klik = generowanie), bo użytkownicy są przyzwyczajeni. Kamil: "szablony nie służą do tego" (podglądu, bo generują dokumenty).

**Decyzja / Sposób realizacji**

**Status:** ✅ Zatwierdzone

Rezygnacja z obracania szablonów. Podstawowa funkcjonalność podglądu szablonów (DOCX, PDF) - MVP.

---

### Edytor formularza - poprawa UX

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

**Kontekst i cel:**
Skupić się na super dopracowaniu edytora formularza, żeby konsultanci się na niego przenieśli. Janusz wczoraj w 50% przypadków przełączał się na listę.

**Szczegóły techniczne:**
- Kolory ikon, żeby się nie zlewały.
- Możliwość przenoszenia sekcji.
- Szukanie po typie pola.
- Edycja GUID (włączana ustawieniem systemowym).

---

### Wzmianki

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`

**Kontekst i cel:**
Fala zgłoszeń odnośnie wzmianek. To kompletnie nie działa, jak powinno. Najlepiej zrobić to od nowa.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przebudowa wzmianek od nowa | **Mariusz** | 60% sprintu | - |
| Pole typu edytowalne HTML | **Mariusz** | [nie określono] | Zamiast zwykłego pola tekstowego. |

---

### Komunikator (Mateusz Kisiel)

**Projekt:** `Klienci/WIM/Komunikator`

**Kontekst i cel:**
Mateusz kończy, są drobne błędy (nie funkcjonalne, tylko przesuwanie, zmiana nazwy), grupy działają. Został wgrany do klienta (WIM) i na ten moment kończymy pracę w ramach MVP, czekamy na potencjalne uwagi klienta.

**Szczegóły techniczne:**
- Funkcja OCR limituje strony (domyślnie pierwsze 10 i ostatnie 3). To nowa funkcjonalność.

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Obracanie szablonów - odrzucone | `cross-cutting/Interfejs-sprawy/Podglad-szablonow` | ✅ Zatwierdzone | Nikt tego nie będzie potrzebował w praktyce, każdy szablon jest plikiem cyfrowym, nie skanem. |
| Podgląd szablonów - MVP bez dolnej belki | `cross-cutting/Interfejs-sprawy/Podglad-szablonow` | ✅ Zatwierdzone | Prosty podgląd ze stronicowaniem, bez przechodzenia na kolejny szablon, przycisk odświeżania zostaje. |
| Komunikator może być częścią AMODIT-a (bazodanowo) | `Klienci/WIM/Komunikator` | ✅ Zatwierdzone | Na chmurze musi być w tej samej bazie, nie ma sensu robić nowej. Mateusz ma ustalić z Piotrem, "jak ma być tą częścią" AMODIT, bo jest to odrębna aplikacja. |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Łukasz Brocki przeciążony (UPS, Global Express, ADE) | `Klienci/LOT` | Wysoki | Rozdzielenie zadań. | Damian Kaminski |
| Brak kontaktu z UPS | `Klienci/LOT/Integracja-UPS` | Średni | Rozwiązane – pozyskano kontakt do osoby opiekującej się LOT. | Łukasz Bott |
| Nie wiadomo czy Global Express ma API | `Klienci/LOT/Integracja-Global-Express` | Średni | Trzeba rozpoznać. | Łukasz Bott |
| JRWA wymaga bardzo dobrego UX (nie może być 15 kliknięć) | `Klienci/LOT/JRWA` | Wysoki | Dedykowane spotkanie designowe, pilne rozpoczęcie prac. | Janusz Bossak |
| Brak informacji biznesowej dla konfiguracji folderów per proces (PKF) | `Klienci/PKF/Przechowywanie-plikow` | Średni | Łukasz Bott ma dopytać klienta o potrzebę biznesową ("po co?"). | Łukasz Bott |
| Adrian może być niedostępny dla repozytorium (kończy inne zadania) | `Klienci/WIM/Repozytorium-plikow-DMS` | Średni | Możliwość przypisania do innych deweloperów (Piotr, Ania, Łukasz Brocki, Adrian). | Damian Kaminski |
| Certyfikacja (SignApp) | `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS` | Wysoki | Czeka na zatwierdzenie konta przez Apple. | Adrian Kotowski |
| Hotfixy blokujące aktualizacje (LPP) | `Moduly/Modul-raportowy` | Wysoki | Masowe akcje, scroll poziomy w module raportowym. Damian bierze na siebie hotfixa masowych akcji. | Damian Kaminski |

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
- Tablice w Teams - bardziej po projektach niż po zadaniach.
- Cel: pokazanie wysokopoziomowo, kto się czym zajmuje i jakie są główne cele sprintu.
- Abstrahując od bugów i hotfixów, którymi staramy się opiekować na co dzień.

**Korelacja z backlogiem:**
- Docelowo: Inicjatywa → Epik → MVP → Ficzery → Use case'y → PBI.
- Repozytorium plików - MVP 1 (w ramach epika "Repozytorium MVP 1").
- Oznacza to, że zrealizujemy wszystkie punkty, które są do tego podpięte, a przez to osiągniemy określone cele biznesowe.

**Zasady:**
- Nie ma czegoś takiego jak "wrzutki, bo zrób mi to czy tamto" - oprócz hotfixów (gdy u klienta coś padło, nie działa).
- Każdy inny przypadek nie jest robiony w tym sprincie - wpisujemy na listę, Damian, Kamil czy Łukasz decydują, na ile jest to ważne.
- Jedyna ścieżka, żeby pozwolić sobie na takie zgłoszenie, to wy sami (dodanie zgłoszenia na bieżący sprint).
- Wszystko inne przechodzi przez PM-ów (codziennie rano na Daily poświęcamy 20 minut i bierzemy zgłoszenia z poprzedniego dnia).
- Wy例外: serwisowe, jak Trust Center, serwis OCR (Mateusz reaguje).

**Feedback zespołu:**
- Adrian: to jest takie wysokopoziomowe, raczej nie widzimy tego na naszej tablicy, nie pokazuje questów czy dodatkowych zadań, pojedynczych PBI, jakiś bugów.
- Mariusz: rozumiem w taki sposób, że na Azure mamy zadania konkretne, wydzielone dla programistów z opisem, a w Teams mamy w kategorii przedziału czasowego jako jeden sprint, jakie są ogólne założenia.
- Mateusz: mi się podoba, że jest krótsze, bardziej konkretne, można sobie łatwo zobaczyć, co jest do zrobienia przez jakie osoby.
- Kamil: będziemy się przewijały te wrzutki, o których mówi Adrian, ale wiadomo, ważnych hotfixów nie pomijamy, dla nas to jest ułatwienie, że wy macie cel, wiecie, że z tego w poniedziałek będziemy was pytać.

---

## 7. Wydania

**Wersja grudniowa:**
- Powinna już wyjść (umawialiśmy się do połowy listopada).
- Z dopiskiem "beta" oficjalnie.
- Nowości: lista pól, matryca uprawnień.
- Będziemy jeszcze pakować UPS i wszystko pod LOT.
- Zrezygnowaliśmy z wrześniowej, żeby wydać grudniową.
- Możemy już usunąć komunikat i opcję przełączania się na stare ustawienia systemowe, testować u nas, czy wszystko zaopiekowaliśmy.

**Wersja marcowa (przyszłoroczna):**
- Pojawiła się też marcowa przyszłoroczna.

**Integracje (UPS, Global Express):**
- Jeśli koledzy to dobrze robią jako rozszerzenia (osobne DLL-ki), to wpięcie tego, czy pojawi się w grudniowej czy marcowej, to będzie tylko kwestia podpięcia.

---

## 8. Uwagi dodatkowe

- **"Łukasz Borowski" vs "Łukasz Brocki"**: W transkrypcji używano zamiennie. Ujednolicono na Łukasz Brocki.
- **WIM/Szafir**: Klient uparł się na Szafira, mimo prostszych alternatyw (SimpleSign za 245 zł). Janusz Bossak: **"Uparł się – jak głupi – jeden człowiek – i robimy."**
- **Apaczka**: Pomysł na przyszłość dla integracji kurierskich (broker, który ma integrację ze wszystkimi firmami kurierskimi w Polsce). Wymaga zbadania kosztów i prowizji.
- **Wzmianki (Mariusz Piotrzkowski)**: Mariusz mówi o "polu typu edytowalne HTML" zamiast zwykłego pola tekstowego.
- **Edytor formularza (Przemek Rogaś)**: Przemek wprowadził: kolory ikon, przenoszenie sekcji, szukanie po typie pola, edycja GUID (włączana ustawieniem systemowym).
- **Komunikator (Mateusz Kisiel)**: Funkcja OCR limituje strony (domyślnie pierwsze 10 i ostatnie 3). To nowa funkcjonalność.


> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:**
> 1.  Zaktualizowano listę powiązanych projektów w nagłówku.
> 2.  Dodano kontekst rezygnacji z implementacji uprawnień do klas JRWA.
> 3.  Uzupełniono kontekst Repozytorium Plików (WIM) o działania Ani i Filipa.
> 4.  Dodano kontekst SignApp (MacOS) o wersję niecertyfikowaną i problem z dyrekcją.
> 5.  Potwierdzono projekt Integracji SIEM dla LOT.
> 6.  Dodano kontekst dyskusji UX do Edytora Formularza.
> 7.  Przepisano "Klucz nie jest unikalny" do nowego projektu `Moduly/Proces-rejestr`.
> 8.  Przepisano "Brak informacji o zablokowaniu karty (SignApp)" do `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`.
> 9.  Przepisano "Wyświetlanie sekcji na telefonie" do `cross-cutting/Interfejs-sprawy`.
> 10. Przepisano "Nagranie Zygmuntów (paczek / wielu podpisów)" do `Moduly/Modul-raportowy/Masowe-podpisywanie`.
> 11. Przepisano "Ukrycie kafelka w koncie systemowym" do nowego projektu `cross-cutting/Logowanie-do-amodit`.
> 12. Dodano status "Do analizy" do "Reprezentacja sekcji w DB".
> 13. Dodano szczegóły do "Powrót do Zespołów Zadaniowych".

# Planowanie Sprintu – 2025-11-21

**Sprint:** Bieżący (listopad)
**Okres:** [brak sprecyzowanych dat]

**Powiązane projekty:**
- `Klienci/WIM/Komunikator`
- `Klienci/LOT/JRWA`
- `Klienci/WIM/Repozytorium-plikow-DMS`
- `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`
- `Klienci/LOT/Integracja-UPS`
- `Klienci/LOT/Integracja-Global-Express`
- `Klienci/LOT/Integracjai-SIEM`
- `Moduly/Edytor-procesow/Edytor-formularzy`
- `Moduly/Modul-raportowy`
- `Moduly/Proces-rejestr`
- `Moduly/Trust-Center`
- `Moduly/Ustawienia-systemowe`
- `cross-cutting/Interfejs-sprawy`
- `cross-cutting/Logowanie-do-amodit`

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Komunikator (WIM) | ✅ Ukończone | Potwierdzone działanie u klienta. Został **wgrany do klienta (WIM)** i na ten moment kończymy pracę w ramach MVP, czekamy na potencjalne uwagi klienta. |
| Amrestowy | ✅ Ukończone | Piotr kończył (status z czatu). |

---

## 2. Plany na sprint

### JRWA (Jednolity Rzeczowy Wykaz Akt) dla LOT

**Projekt:** `Klienci/LOT/JRWA`

**Kontekst i cel:**
Przygotowanie struktury danych dla JRWA na wzór integracji z GUS TERYT. Celem jest umożliwienie wyboru klasy z wykazu w polu "Odnośnik" i zwrócenie jej atrybutów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Budowa struktury JRWA (tabela, źródło danych) | **Piotr Buczkowski** | start przyszły tydz. | - |
| Ewentualne przejęcie tematu w dalszym kroku | **Mariusz Piotrzkowski** (?) | - | Jeśli Piotr nie zdąży/przekaże |

**Szczegóły techniczne:**
- Dedykowana tabela w bazie.
- Mechanizm źródła danych zwracający obiekt/JSON.
- Dostęp w regułach przez notację kropki: `[PoleJRWA].KlasaArchiwalna`.

**Decyzje podjęte przy planowaniu:**
- Rezygnacja z implementacji uprawnień do klas JRWA w tym sprincie (klient LOT nie chce przypisywać klas do działów, stwierdził, że nie bierze odpowiedzialności za przypisywanie klas do działów, więc prawdopodobnie wszyscy będą widzieć wszystko).
- Zarządzanie strukturą (interfejs) przesunięte na kolejne sprinty.

---

### Repozytorium Plików (WIM)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Uruchomienie podstawowej funkcjonalności tworzenia folderów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przygotowanie pierwszego endpointu (tworzenie folderów) | **Anna Skupińska** | 1d (dziś) | Ania przygotowuje endpoint. |
| Podpięcie pod endpoint (tworzenie folderów) | **Filip Liwiński** | - | Czeka na Anię. Filip się podpina. |
| Wsparcie dla Ani przy problemach z bazami pod testy | **Michał Zwierzchowski** | - | - |

---

### SignApp (MacOS)

**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

**Kontekst i cel:**
Dokończenie prac nad aplikacją i przygotowanie do testów u klienta.

**Status:**
Aplikacja gotowa (UI poprawione), ale niecertyfikowana.

**Decyzje podjęte przy planowaniu:**
- Przekazać wersję niecertyfikowaną do testów działowi IT klienta (z pominięciem dyrekcji).
- Klient musi być świadomy konieczności akceptacji instalacji z nieznanego źródła. Dyrektorowi takiej wersji nie damy.

**Ryzyka:**
- Opóźnienia w certyfikacji.
- Problem z podpisywaniem (raz działa, raz "wymaga pełnej autoryzacji") – do weryfikacji przez Łukasza Brockiego (czy Simplus zwraca taką informację).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki widoku, panel wyboru certyfikatu, obsługa flagi e-poleconego | **Adrian Kotowski** | - | - |
| Wypisywanie z raportów (nowa funkcjonalność) | **Adrian Kotowski** | - | - |
| Weryfikacja zwrotki Simplus dot. blokady karty | **Łukasz Brocki** | - | - |

---

### Integracje Kurierskie (LOT)

**Projekt:** `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`

**Kontekst i cel:**
Integracja z nowymi dostawcami usług kurierskich dla LOT.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja UPS i Global Express | **Łukasz Brocki** | Global Express w tym sprincie | Dane pozyskane |

---

### Integracja SIEM (LOT)

**Projekt:** `Klienci/LOT/Integracjai-SIEM`

**Kontekst i cel:**
Monitorowanie zdarzeń systemu AMODIT w systemach SIEM klienta.

**Decyzje podjęte przy planowaniu:**
- Zamiast pisać dedykowaną integrację, AMODIT wystawi logi w ustandaryzowanym formacie na porcie, a system SIEM klienta będzie nasłuchiwał.

---

### Edytor Formularza i Lista Pól

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

**Kontekst i cel:**
Domykanie tematu nowego edytora graficznego i listy pól. Wyszło sporo bugów i niespójności wizualnych.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki edytora graficznego i listy pól (bugi, wizualne) | **Zespół Frontend** | - | - |
| Porządkowanie pola typu Tabela (rozjechany import, ikonki) | **Mariusz Piotrzkowski** (?) | - | Jeśli Piotr weźmie JRWA |
| Podgląd reguł pola (Prawy panel) | **Do ustalenia** | - | - |
| Naprawa dostępu do reguł tabeli | **Do ustalenia** | - | - |
| Naprawa dodawania nowej sekcji z poziomu listy pól | **Do ustalenia** | - | - |
| Poprawki wizualne (zaokrąglenia, podświetlenia pól Search) | **Przemysław Rogaś** | - | - |

**Decyzje podjęte przy planowaniu:**
- "Zarządzaj polem" powinno zawierać "cięższe" funkcje (usuń, zmień typ pola), które nie są używane na co dzień. To był kontekst dyskusji UX (Kamil vs Janusz/Damian) o tym, gdzie umieścić rzadkie akcje.
- Konieczny redesign panelu edycji pola (UX).

---

### Moduł Raportowy

**Projekt:** `Moduly/Modul-raportowy`

**Kontekst i cel:**
Poprawa działania i wydajności filtrów użytkownika.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Prace nad indeksami (wydajność filtrów) | **Mateusz Kisiel** | - | - |
| Porządkowanie operatorów daty w filtrach | **Przemysław Rogaś** | - | - |

---

### Inne zgłoszenia backlogowe

**Kontekst i cel:**
Przegląd i przypisanie zgłoszeń z backlogu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Klucz nie jest unikalny (rejestr, usunięte sprawy) | **Kamil Dubaniowski** | - | **Projekt: `Moduly/Proces-rejestr`** |
| Informacja o zablokowanej karcie (SignApp) | **Damian Kamiński** | - | **Projekt: `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`**. Do weryfikacji z Łukaszem Brockim |
| Wyświetlanie sekcji na telefonie (aplikacja PWA) | **Damian Kamiński** | - | **Projekt: `cross-cutting/Interfejs-sprawy`**. Do Łukasza |
| Nagranie Zygmuntów (paczek / wielu podpisów) | **Kamil Dubaniowski** | - | **Projekt: `Moduly/Modul-raportowy/Masowe-podpisywanie`**. Do zapytania Mateusza |
| Ukrycie kafelka w koncie systemowym | **Kamil Dubaniowski** | - | **Projekt: `cross-cutting/Logowanie-do-amodit`**. Kontekst: Janusz ma konto systemowe do logowania się do Azure DevOps poprzez API, więc kafelek nie może być widoczny w kroku logowania przez UI. |
| Hotfix 21051 (kwiecień) | **Michał Zwierzchowski** | - | Do backlogu |

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Reprezentacja sekcji w DB | Frontendowa implementacja sekcji | 💡 Do weryfikacji / Do analizy | Należy zmienić logikę po stronie backendu, aby sekcje miały swoją reprezentację w bazie danych, a nie tylko redundantny zapis w każdym rekordzie definicji pola. To jest większa zmiana, status "Feature Request". |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Wpływ | Mitygacja | Właściciel |
|---------------|-------|-----------|------------|
| Nieobecność Adriana | Wysoki | - | Damian Kamiński |
| Zatory w testach (koniec sprintu) | Wysoki | Przypominanie o bieżącym mergowaniu | Zespół |

---

## 5. Organizacja pracy

- **Nieobecności:** Damian (środa - warsztaty), Janusz (środa - pogrzeb).
- **Orlen Paczka:** Integracja TrustCenter, temat od Moniki. Damian ma się zapoznać.
- **Rossman historia biznesowa:** Damian przygotuje MVP dla prezentacji.
- **Koncepcja Zespołów Zadaniowych:** Powrót do idei stałych zespołów celowych (2 backendowe, 1 frontendowy, testerki przypisane). Zespół Trust Center (Marek), Zespół AI/OCR (Mateusz).

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
- Wyjątki: serwisowe, jak Trust Center, serwis OCR (Mateusz reaguje).

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


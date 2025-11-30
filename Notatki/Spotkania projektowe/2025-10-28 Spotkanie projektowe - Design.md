# Notatka projektowa – 2025-10-28 – Design

**Data:** 2025-10-28
**Temat główny:** Design repozytorium plików DMS

**Powiązane projekty:**
- `moduly/Repozytorium-plikow-DMS` – wszystkie funkcjonalności

---

## 1. Struktura repozytorium – przestrzenie, foldery, pliki

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Definicja struktury logicznej repozytorium plików w AMODIT jako Document Management System (DMS). Repozytorium ma być niezależne od spraw i procesów – dokument jest głównym bytem, a nie elementem sprawy. Potrzeba określenia hierarchii organizacji plików, nomenklatury i ograniczeń technicznych.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przestrzenie jako najwyższy poziom | Najwyższy poziom organizacji nazywany "przestrzeniami" | ✅ Wybrana – rozróżnienie od istniejących "obszarów" w AMODIT |
| Obszary jako najwyższy poziom | Użycie słowa "obszary" dla najwyższego poziomu | ❌ Odrzucona – słowo "obszary" jest już przypisane do innej funkcjonalności w AMODIT |
| Odrębne byty vs jeden byt | Czy repozytorium DMS i repozytorium spraw to odrębne byty czy jeden | 🔍 Do ustalenia na najwyższym poziomie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Struktura repozytorium:
- **Przestrzenie** – najwyższy poziom organizacji (nomenklatura do ustalenia, propozycja: "przestrzenie")
- Możliwość definiowania dowolnej liczby przestrzeni
- Każda przestrzeń może zawierać foldery i pliki
- **Foldery** – możliwość tworzenia struktury folderów wewnątrz przestrzeni, foldery mogą być zagnieżdżone
- **Pliki** – przechowywane wewnątrz folderów, różne typy plików (spójność z dozwolonymi typami w AMODIT)

**Szczegóły techniczne:**
- Maksymalna głębokość zagnieżdżenia folderów: do ustalenia (ograniczenia Windows)
- System oparty na dziedziczeniu uprawnień
- Możliwość przerwania dziedziczenia na poziomie folderu lub pliku (nie na poziomie przestrzeni)

### Ograniczenia / Poza zakresem

- Przerwanie dziedziczenia na poziomie przestrzeni – nie jest możliwe (błąd w dokumentacji)
- Maksymalna głębokość zagnieżdżenia: do ustalenia

### Punkty otwarte

- Czy repozytorium DMS i repozytorium spraw to odrębne byty czy jeden byt? (decyzja na najwyższym poziomie)
- Jaka maksymalna głębokość zagnieżdżenia folderów? (5-10 poziomów?)
- Czy maksymalna głębokość ma się wiązać z długością ścieżki w URL?

---

## 2. System uprawnień i dziedziczenie

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Definicja modelu uprawnień dla repozytorium plików z obsługą dziedziczenia, przerwania dziedziczenia oraz uprawnień wynikowych (widoczność folderu wynikająca z dostępu do plików).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dziedziczenie z możliwością przerwania | Domyślne uprawnienia dziedziczone z węzła nadrzędnego, możliwość przerwania na każdym poziomie | ✅ Wybrana – standardowy model |
| Widoczność folderu jako osobne uprawnienie | Możliwość nadania samej widoczności folderu bez dostępu do zawartości | ❌ Odrzucona – widoczność folderu jest tylko uprawnieniem wynikowym |
| Rozdzielenie uprawnienia dodawania od usuwania | Osobne uprawnienia: dodawanie plików vs usuwanie plików | 🔍 Do rozważenia |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Model uprawnień:
- **Dziedziczenie uprawnień** – domyślne uprawnienia dziedziczone z węzła nadrzędnego (przestrzeń → folder → podfolder → plik)
- **Przerywanie dziedziczenia** – możliwość zerwania dziedziczenia na poziomie folderu lub pliku (checkbox/switch "Przerwij dziedziczenie uprawnień")
- **Wskaźnik wizualny** – specjalna ikona (ludziki) wyświetlana gdy dziedziczenie jest przerwane (na poziomie drzewka i w widoku uprawnień)
- **Typy uprawnień:**
  - Odczyt
  - Zapis
  - Modyfikacja
  - Usuwanie
  - Pełne (dodawanie, usuwanie dowolnych, możliwość ustawienia flagi nieusuwalności)
  - Dodawanie i usuwanie tylko tych, które nie są ograniczone
- **Uprawnienia wynikowe:**
  - Widoczność folderu – wynikowe uprawnienie (nie definiowane bezpośrednio), wynika z dostępu do plików w folderze lub podfolderach
  - Jeśli użytkownik ma dostęp do pliku w folderze, automatycznie widzi strukturę folderów w górę (do przestrzeni)
- **Uprawnienia na poziomie plików:**
  - Możliwość zerwania dziedziczenia dla pojedynczego pliku
  - Możliwość nadania dostępu do pliku użytkownikowi, który nie ma dostępu do folderu nadrzędnego
  - W takim przypadku użytkownik widzi strukturę folderów w górę, ale tylko ten konkretny plik (pozostałe foldery są puste)
- **Wyświetlanie uprawnień:**
  - W widoku uprawnień folderu/przestrzeni wyświetlane są uprawnienia bezpośrednie i wynikające z dostępów do plików niżej
  - Uprawnienia wynikowe oznaczone jako "widoczność folderu"
  - Uprawnienia wynikowe z dostępu do plików są tylko do odczytu w interfejsie uprawnień folderu (nie można ich edytować)

**Szczegóły techniczne:**
- Uprawnienia nadawane przez administratorów systemu lub administratorów przestrzeni
- Możliwość nadawania uprawnień pojedynczym użytkownikom i grupom (nie rolom)
- Zgodność z systemem uprawnień AMODIT – osoba nadająca uprawnienia musi mieć możliwość edycji użytkowników, aby widzieć wszystkich użytkowników i grupy

### Ograniczenia / Poza zakresem

- Widoczność folderu jako osobne uprawnienie – nie ma sensu, jest tylko wynikowe
- Rola jako podmiot uprawnień – nie jest obsługiwane, tylko użytkownicy i grupy

### Punkty otwarte

- Czy ma sens nadawanie samej widoczności folderów? (bez dostępu do zawartości)
- Czy rozdzielić uprawnienie dodawania od usuwania? (możliwość dodawania bez możliwości usuwania)
- Czy oddzielić uprawnienie do tworzenia/usuwania folderów od usuwania plików?
- Czy usuwanie powinno być ograniczone tylko do własnych plików? (użytkownik może usunąć tylko pliki, które sam dodał)

---

## 3. Przechowywanie plików – struktura fizyczna na dysku

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Określenie sposobu przechowywania plików repozytorium na dysku – struktura folderów fizycznych, lokalizacja, identyfikacja plików oraz sposób odtworzenia struktury logicznej z struktury fizycznej.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przechowywanie w bazie danych (Blob) | Wszystkie pliki przechowywane w bazie danych | ❌ Odrzucona – MVP nie obejmuje, problemy z rozmiarem bazy, backupem |
| Przechowywanie na zasobach sieciowych (spójne z attachment) | Pliki przechowywane w folderze Attachment, dodatkowy subfolder "Repository Files" | ✅ Wybrana – spójność z obecnym systemem |
| Oddzielne ustawienie lokalizacji | Możliwość wskazania osobnego folderu dla plików repozytorium | ✅ Wybrana – dodatkowa opcja |
| Struktura oparta na ID węzłów | Foldery fizyczne nazywane ID przestrzeni, ID folderu, ID podfolderu | ✅ Wybrana – unikalność, krótkie ścieżki |
| Struktura oparta na pierwszych znakach nazwy | Foldery fizyczne nazywane pierwszymi znakami nazwy przestrzeni/folderu | ❌ Odrzucona – konflikty przy podobnych nazwach (np. "Dokumentacja projektu Alfa" i "Dokumentacja projektu Beta") |
| Struktura odzwierciedlająca strukturę logiczną | Foldery fizyczne mają takie same nazwy jak w interfejsie | ❌ Odrzucona – problemy z długością ścieżek w Windows, znakami specjalnymi |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Przechowywanie plików:
- **MVP:** Pliki nie będą przechowywane w bazie danych, tylko lokalnie na zasobach sieciowych
- **Lokalizacja:** Spójna z obecnym systemem przechowywania attachment – w ramach folderu Attachment dodatkowy subfolder (np. "Repository Files")
- **Oddzielne ustawienie:** Możliwość wskazania osobnego folderu dla plików repozytorium (można wskazać ten sam folder co dla plików ze spraw, ale w ramach tego folderu będzie oddzielny subfolder)
- **Struktura fizyczna na dysku:**
  - Oparta na ID węzłów (ID przestrzeni, ID folderu, ID podfolderu)
  - Przykład: `AMODIT/Attachment/Repository Files/{ID_Przestrzeni}/{ID_Folderu}/{ID_Podfolderu}/...`
  - Struktura jest odtwarzalna – pełna struktura zagnieżdżenia jest zachowana, tylko nazwy są ID zamiast nazw logicznych
- **Identyfikacja plików w interfejsie:**
  - W adresie URL widoczny identyfikator lokalizacji: `/repository/{ID_Przestrzeni}/{ID_Folderu}/{ID_Podfolderu}/...`
  - Możliwość kopiowania ścieżki z URL do Eksploratora Windows (po dodaniu ścieżki bazowej)
  - W podglądzie pliku dodatkowy identyfikator konkretnego pliku

**Szczegóły techniczne:**
- Długość ID: 3-4 znaki per folder (zakładając setki-tysiące węzłów)
- Przykład: przy 6 poziomach zagnieżdżenia = maksymalnie 24 znaki w adresie URL (6 × 4)
- Struktura jest odtwarzalna – można odtworzyć strukturę logiczną na podstawie struktury fizycznej (mapowanie ID → nazwy)

### Ograniczenia / Poza zakresem

- Przechowywanie w bazie danych – poza MVP (możliwość migracji plików z bazy do zasobów sieciowych dla klientów, którzy przechowują pliki w bazie)
- Klienci przechowujący pliki w bazie danych – nisza, której nie pokryjemy w MVP (większość dużych klientów on-premise używa zasobów sieciowych)

### Punkty otwarte

- Czy struktura fizyczna powinna być zgodna ze strukturą logiczną folderów? (Janusz Bossak sugeruje, że może to ułatwić backup i odzyskiwanie fragmentów)
- Jak obsłużyć szyfrowanie plików? (jeśli pliki będą zaszyfrowane, struktura oparta tylko na ID może utrudnić identyfikację)

---

## 4. Metadane plików

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Określenie zakresu metadanych przechowywanych dla plików w repozytorium – czy tylko metadane techniczne/systemowe, czy również metadane definiowane przez użytkownika (opis, tagi, daty obowiązywania).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Tylko metadane techniczne/systemowe | ID przestrzeni, ID folderu, ID pliku, uprawnienia | ✅ Wybrana dla MVP – minimum wymagane |
| Metadane użytkownika w MVP | Opis, tagi, daty obowiązywania w wersji MVP | ❌ Odrzucona – poza zakresem MVP |
| Metadane użytkownika jako rozwój | Opis, tagi, daty obowiązywania jako funkcjonalność rozwojowa | ⏸️ Odroczona – do rozważenia w przyszłości |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Metadane w MVP:
- **Minimum w ramach MVP:** Spójne z tym, co jest w case (odwołania do plików)
  - ID przestrzeni
  - ID folderu
  - ID pliku
  - Uprawnienia (prawdopodobnie JSON, do ustalenia przez deweloperów)
- **Poza MVP (funkcjonalność rozwojowa):**
  - Opis pliku (do wyszukiwania)
  - Tagi (dla łatwiejszego wyszukiwania)
  - Daty obowiązywania (kiedy się wygaszają, tryb niedostępny)
  - Inne cechy zdeterminowane per dany plik

**Szczegóły techniczne:**
- Metadane przechowywane w bazie danych
- Format zapisywania uprawnień: prawdopodobnie JSON (nowy), do ustalenia przez deweloperów
- W odróżnieniu od procesów, tutaj każdy plik może mieć inne metadane (duża zmienność)

### Ograniczenia / Poza zakresem

- Metadane użytkownika (opis, tagi, daty) – poza MVP
- Zestaw metadanych zdefiniowany per katalog – nie jest zdefiniowane

### Punkty otwarte

- Czy w przyszłości pliki z repozytorium DMS mogą stawać się elementami spraw? (powiązanie między DMS a AMODIT jako systemem spraw)
- Czy metadane powinny być spójne między plikami w tym samym katalogu, czy każdy plik może mieć inne metadane?
- Jaki format zapisywania uprawnień? (JSON, inny format)

---

## 5. Interfejs użytkownika

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Definicja interfejsu użytkownika dla repozytorium plików – widok drzewa folderów, główny obszar zawartości, ścieżka breadcrumbs, widoki plików oraz operacje na plikach.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Widok drzewa folderów po lewej (MVP) | Drzewo folderów po lewej stronie jako główny element interfejsu | ✅ Wybrana dla MVP – nie opcjonalnie |
| Widok kafelkowy | Pliki wyświetlane jako kafelki z ikonkami | ✅ Wybrana dla MVP – jeden z dwóch widoków |
| Widok lista | Pliki wyświetlane jako lista z kolumnami | ⏸️ Odroczona – może być zbędna, do rozważenia |
| Widok lista z dodatkowymi danymi | Lista z kolumnami: właściciel, data modyfikacji, rozmiar | ❌ Odrzucona dla MVP – może wystarczy sama lista plików |
| Przenoszenie plików między folderami | Możliwość przeciągania plików między folderami | ❌ Odrzucona dla MVP – poza zakresem |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Interfejs użytkownika w MVP:
- **Widok drzewa folderów** – po lewej stronie (nie opcjonalnie, jako MVP)
- **Główny obszar** – zawartość aktualnego folderu
- **Ścieżka breadcrumbs** – na górze (wynika z adresu URL, nie trzeba osobno przedstawiać)
- **Widoki plików:**
  - Widok kafelkowy (MVP)
  - Alternatywnie lista (do rozważenia, może być zbędna)
  - Dla MVP może wystarczyć sama lista plików (bez dodatkowych danych jak właściciel, data modyfikacji, rozmiar)
  - Możliwe, że jedynie data modyfikacji jest zasadna
- **Zarządzanie uprawnieniami:**
  - Przycisk "Uprawnienia" na każdym folderze i pliku
  - Model paneli: użytkownicy i grupy
  - Checkbox "Przerwij dziedziczenie"
  - Wskaźnik wizualny gdy dziedziczenie jest przerwane
- **Operacje na plikach:**
  - Dodawanie plików (MVP)
  - Usuwanie plików (MVP)
  - Podgląd plików (analogicznie jak w raportach, wykorzystanie gotowego komponentu)

**Szczegóły techniczne:**
- Podgląd plików dostępny na zasadzie analogicznej jak obecnie w raportach (wykorzystanie gotowego komponentu)
- Adres URL zawiera identyfikator lokalizacji (ID przestrzeni, ID folderu, etc.)

### Ograniczenia / Poza zakresem

- Przenoszenie plików między folderami – poza MVP
- Wersjonowanie plików – poza MVP
- Historia zmian – poza MVP (przynajmniej w zakresie tego, kto plik załadował)
- Widok lista z dodatkowymi danymi (właściciel, rozmiar) – może być zbędny dla MVP
- Eksport/import struktury – nie jest potrzebny

### Punkty otwarte

- Czy widok lista jest potrzebny, czy wystarczy widok kafelkowy?
- Które dane są zasadne w widoku listy? (możliwe, że jedynie data modyfikacji)
- Czy w przyszłości potrzebne będzie wersjonowanie plików?
- Co logować w historii zmian? (kto plik załadował, kto usuwał – pytanie do architekta technicznego)

---

## 6. Wyszukiwanie plików

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Określenie zakresu funkcjonalności wyszukiwania w repozytorium plików – czy wyszukiwanie pełnotekstowe, jak obsłużyć uprawnienia w wynikach wyszukiwania, jakie są ryzyka wydajnościowe i bezpieczeństwa.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Wyszukiwanie pełnotekstowe na wszystkich plikach | Wyszukiwanie w treści wszystkich plików w repozytorium | ✅ Wybrana – wymagane dla repozytorium |
| Wyszukiwanie tylko w nazwach plików | Wyszukiwanie tylko w metadanych (nazwa, opis) | ❌ Odrzucona – niewystarczające dla repozytorium |
| Wyszukiwanie bez uwzględnienia uprawnień | Wyszukiwanie pokazuje wszystkie wyniki niezależnie od uprawnień | ❌ Odrzucona – problemy bezpieczeństwa |
| Wyszukiwanie z filtrowaniem po uprawnieniach | Wyszukiwanie pokazuje tylko wyniki zgodne z uprawnieniami użytkownika | ✅ Wybrana – wymagane |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Wyszukiwanie:
- **Wyszukiwanie pełnotekstowe** – wymagane dla repozytorium (nie można sobie wyobrazić repozytorium bez wyszukiwania)
- **Mechanizm:** W oparciu o Lucene (jak obecnie w AMODIT)
- **Obsługa uprawnień:**
  - Wyszukiwanie pokazuje wszystkie wyniki (bez filtrowania po uprawnieniach na etapie wyszukiwania)
  - Następnie wyniki są filtrowane zgodnie z uprawnieniami użytkownika
  - Użytkownik widzi tylko te wyniki, do których ma uprawnienia
- **Ryzyka do zaadresowania:**
  - **Bezpieczeństwo:** Ktoś wrzuca 2-gigowy plik Word (np. książka 1000 stron) – jak szybko się przetworzy?
  - **Wydajność:** Czy przetwarzanie będzie odrębnym jobem, czy tym samym jobem co dla spraw?
  - **Struktura indeksu:** Czy to będzie odrębny plik Lucene, czy spójny z tym, co mamy dla spraw?

**Szczegóły techniczne:**
- Wykorzystanie istniejącego mechanizmu Lucene
- Pytania techniczne wymagające odpowiedzi:
  - Czy przetwarzanie plików repozytorium będzie odrębnym jobem?
  - Czy będzie to ten sam job co dla spraw?
  - Czy będzie odrębny plik Lucene dla repozytorium?
  - Czy da się zrobić to odrębnym plikiem?

### Ograniczenia / Poza zakresem

- Etykiety/tagi dla łatwiejszego wyszukiwania – poza MVP (funkcjonalność rozwojowa)

### Punkty otwarte

- Jak obsłużyć przetwarzanie dużych plików (2 GB Word) dla wyszukiwania pełnotekstowego?
- Czy przetwarzanie będzie odrębnym jobem, czy tym samym co dla spraw?
- Czy indeks Lucene będzie odrębny dla repozytorium, czy spójny z istniejącym?
- Jakie są dokładne ryzyka bezpieczeństwa i wydajnościowe przy wyszukiwaniu pełnotekstowym?

---

## 7. Bezpieczeństwo i szyfrowanie plików

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Określenie wymagań bezpieczeństwa dla plików repozytorium – czy pliki mają być szyfrowane, jak zapewnić bezpieczeństwo przechowywania plików poza bazą danych.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Wymagania bezpieczeństwa:
- **Szyfrowanie plików:** Pytanie czy przewidujemy szyfrowanie plików (zgodnie z tym, co robimy dla innych plików w AMODIT)
- **Lokalizacja:** Pliki przechowywane poza AMODIT (na zasobach sieciowych)
- **Struktura fizyczna:** Jeśli pliki będą zaszyfrowane, struktura oparta tylko na ID może utrudnić identyfikację przy backupie/odzyskiwaniu

**Szczegóły techniczne:**
- Do ustalenia: czy pliki repozytorium mają być szyfrowane tak samo jak pliki ze spraw?
- Struktura oparta na ID może utrudnić zarządzanie backupem i odzyskiwaniem fragmentów (Janusz Bossak sugeruje, że struktura zgodna ze strukturą logiczną folderów może ułatwić zarządzanie)

### Ograniczenia / Poza zakresem

Brak.

### Punkty otwarte

- Czy pliki repozytorium mają być szyfrowane? (zgodnie z tym, co robimy dla innych plików)
- Czy struktura fizyczna oparta tylko na ID nie utrudni zarządzania backupem i odzyskiwaniem fragmentów?
- Czy struktura fizyczna powinna być zgodna ze strukturą logiczną folderów dla łatwiejszego zarządzania?

---

## 8. Funkcjonalności poza MVP

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Identyfikacja funkcjonalności, które są poza zakresem MVP i mogą być rozważone w przyszłości.

### Rozważane alternatywy

Wszystkie funkcjonalności rozwojowe są oznaczone jako poza MVP.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Funkcjonalności poza MVP:
- **Wersjonowanie plików** – wykluczone z MVP
- **Historia zmian** – przynajmniej w zakresie tego, kto plik załadował (do ustalenia, co logować – pytanie do architekta technicznego)
- **Przenoszenie plików między folderami** – poza MVP
- **Linki publiczne** – nie ma, tylko wynikowe z uprawnień nadanych przez administratora
- **Etykiety/tagi** – poza MVP (dla łatwiejszego wyszukiwania)
- **Powiadomienia** – nie jest kluczowe, może być w przyszłości jeśli ktoś zasponsoruje
- **Eksport/import struktury** – nie jest potrzebny
- **Integracja z szablonami XSLT** – nie dotyczy (błąd w dokumentacji, dotyczyło czegoś innego)
- **Metadane użytkownika** (opis, tagi, daty obowiązywania) – funkcjonalność rozwojowa

**Funkcjonalności do ustalenia:**
- **Scheduled job** – które funkcjonalności MVP mogą być zrobione w kolejnych sprintach?
- **Kosz** – zakładamy, że tak (jak dla spraw), oznaczamy jako usunięte, ale fizycznie jeszcze nie usuwamy
  - Możliwe, że kosz powinien być zaopiekowany okresem czasu (np. 30 dni) – nie musimy mieć tego na starcie
- **Uprawnienia do usuwania** – możliwe, że usuwanie tylko swoich plików jako MVP, w przyszłości czyszczenie okresowe kosza (np. 30 dni)
- **Limity rozmiaru pliku** – pytanie czy mamy limit dla pojedynczego pliku (analogia do tego, co mamy teraz)
  - Dla dużych plików trzeba robić odrębne endpointy
  - Przez interfejs przeglądarkowy: 2 GB (do potwierdzenia, ostatnio próbowali to obejść)

**Szczegóły techniczne:**
- Typy plików: spójne z tym, co w sprawach
- Podgląd plików: dostępny na zasadzie analogicznej jak obecnie w raportach (wykorzystanie gotowego komponentu)

### Ograniczenia / Poza zakresem

Wszystkie wymienione funkcjonalności są poza MVP.

### Punkty otwarte

- Co logować w historii zmian? (kto plik załadował, kto usuwał – pytanie do architekta technicznego)
- Czy kosz powinien mieć okres czasu (np. 30 dni) od razu, czy można to dodać później?
- Czy usuwanie powinno być ograniczone tylko do własnych plików jako MVP?
- Jaki limit rozmiaru pliku przez interfejs przeglądarkowy? (2 GB do potwierdzenia)
- Które funkcjonalności MVP mogą być zrobione w kolejnych sprintach? (scheduled job)

---

## 9. Ogólne uwagi i ryzyka projektu

**Projekt:** `moduly/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium plików DMS

### Cel i problem

Identyfikacja ogólnych ryzyk i wyzwań związanych z realizacją projektu repozytorium plików DMS, w tym zakresu prac, czasu realizacji oraz podejścia do implementacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Podejście tradycyjne | Realizacja jako normalny projekt, ręczne kodowanie | ❌ Odrzucona – zbyt czasochłonne (pół roku) |
| Podejście z wykorzystaniem AI | Wykorzystanie AI (Filip) do generowania kodu na podstawie projektu wizualnego | ✅ Wybrana – skrócenie czasu o co najmniej 50% |
| Realizacja w 3 sprinty | Próba realizacji całego MVP w 3 sprinty | 🔍 Do rozważenia – wymaga przegrupowania sił |
| Realizacja w 2-3 miesiące | Realizacja z wykorzystaniem AI w 2-3 miesiące zamiast 6 miesięcy | ✅ Wybrana – realistyczny cel |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ogólne podejście do projektu:
- **Zakres projektu:** Gigantyczny projekt, wymaga sprytnego podejścia
- **Czas realizacji tradycyjny:** Pół roku roboty (6 miesięcy) przy podejściu tradycyjnym
- **Podejście z AI:** Wykorzystanie AI (Filip) do generowania kodu na podstawie projektu wizualnego
  - Projekt wizualny już istnieje i może być użyty jako baza dla AI
  - Oczekiwane skrócenie czasu o co najmniej 50% (z 6 miesięcy do 2-3 miesięcy)
- **Przegrupowanie sił:** Jeśli chcemy zrobić to w 3 sprinty, wszyscy praktycznie muszą się za to wziąć
- **Backend:** Wymaga sprawnie zrobionego backendu, żeby wszystko elegancko funkcjonowało
- **Ryzyko:** Projekt robiony dla jednego klienta (podobnie jak komunikator), mogą być większe/mniejsze kwaczki

**Szczegóły techniczne:**
- Projekt wizualny już istnieje i może być użyty jako baza dla AI
- Filip (AI) już zaczął "klepać" kod w cudzysłowie
- Wizualne efekty to jedno, ale backendu jest sporo
- Trzeba sprawnie zrobić backend, żeby wszystko elegancko funkcjonowało

### Ograniczenia / Poza zakresem

- Realizacja tradycyjna bez AI – zbyt czasochłonna
- Perfekcyjna realizacja bez błędów – nierealistyczne (podobnie jak komunikator, będą większe/mniejsze kwaczki)

### Punkty otwarte

- Czy projekt jest robiony tylko dla jednego klienta? (ryzyko biznesowe)
- Jak przegrupować siły, żeby zrealizować projekt w 3 sprinty?
- Jak sprawnie zrobić backend, żeby wszystko elegancko funkcjonowało?
- Jakie są dokładne ryzyka przy wykorzystaniu AI do generowania kodu?

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Podstawowa struktura i uprawnienia

**Cel:** Stworzenie podstawowej struktury repozytorium z możliwością zarządzania przestrzeniami, folderami i plikami oraz systemem uprawnień.

**Zakres:** Funkcjonalności 1, 2, 3, 5 (częściowo)

**Planowany termin:** Do ustalenia

### MVP 2: Interfejs użytkownika i operacje podstawowe

**Cel:** Pełny interfejs użytkownika z możliwością dodawania, usuwania i przeglądania plików.

**Zakres:** Funkcjonalność 5 (pełna), operacje na plikach

**Planowany termin:** Do ustalenia

### MVP 3: Wyszukiwanie i bezpieczeństwo

**Cel:** Wyszukiwanie pełnotekstowe z obsługą uprawnień oraz zabezpieczenia (szyfrowanie, kosz).

**Zakres:** Funkcjonalności 6, 7, kosz, limity rozmiaru

**Planowany termin:** Do ustalenia

---

## Punkty do dalszej dyskusji (globalne)

- Czy repozytorium DMS i repozytorium spraw to odrębne byty czy jeden byt? (decyzja na najwyższym poziomie)
- Czy w przyszłości pliki z repozytorium DMS mogą stawać się elementami spraw? (powiązanie między DMS a AMODIT jako systemem spraw)
- Jak przegrupować siły, żeby zrealizować projekt w 3 sprinty?
- Czy projekt jest robiony tylko dla jednego klienta? (ryzyko biznesowe)
- Jakie są dokładne ryzyka bezpieczeństwa i wydajnościowe przy wyszukiwaniu pełnotekstowym?
- Które funkcjonalności MVP mogą być zrobione w kolejnych sprintach? (scheduled job)

#backlog #azure 

[[Strażnik backlogu]]

**Cel:** Ustanowienie twardych kryteriów kwalifikacji i nazewnictwa dla wszystkich poziomów hierarchii backlogu, aby przekształcić go z "listy pomysłów" w "portfolio dostarczanej wartości". Dokument ten jest praktycznym rozszerzeniem `Modelu Pracy Analitycznej Zespołu (Wersja Zintegrowana.md)`.

### Nasza Hierarchia (Kompletna)

Oto nasza pełna, 5-poziomowa terminologia:

1. **Inicjatywa** (Ikona: 💎 Diament) - _Poziom Strategii (PO CO?)_
    
2. **Paczka Wartości (MVP)** (Ikona: 🎁 Prezent) - _Poziom Wartości (CO - Paczka)_
    
3. **Feature** (Ikona: ⚙️ Trybik) - _Poziom Funkcji (CO - Komponent)_
    
4. **Use Case** (Ikona: 📖 Otwarta Książka) - _Poziom Specyfikacji (JAK?)_
    
5. **PBI** (Ikona: 📋 Clipboard) - _Poziom Pracy (ZADANIE)_
    

### 1. Inicjatywa (💎 Diament)

Inicjatywa to **Biznesowe "Dlaczego"**. Jest to artefakt strategiczny, który odpowiada na `Krok 0: Ustalenie Wartości Biznesowej` z naszego procesu.

#### Kryterium Kwalifikacji (Test Lakmusowy)

- **Czy to jest cel biznesowy, a nie funkcja?**
    
    - ŹLE: "Zbudować nowy edytor procesów." (To jest _co_ chcemy zrobić).
        
    - DOBRZE: "Skrócić czas wdrożenia nowych klientów o 30%." (To jest _dlaczego_ to robimy).
        
- **Czy jest mierzalne (lub przynajmniej obserwowalne)?** Inicjatywa musi być celem, którego postęp możemy śledzić.
    
- **Czy jest długoterminowa?** Inicjatywa żyje dłużej niż jeden Epic. Często obejmuje _wiele_ Epików (MVP) dostarczanych w czasie.
    

#### Jak dobrze nazwać Inicjatywę?

Nazwa musi być **zorientowana na wynik (Outcome)**, a nie na produkt (Output). Powinna opisywać zmianę w biznesie lub u klienta. Idealna nazwa jest również **mierzalna**.

**Format (Sugestia):** `[Czasownik opisujący zmianę] + [Obszar Biznesowy/Metryka] + [Cel (Metryka)]`

|   |   |   |
|---|---|---|
|**Zła Nazwa (Output - co robimy)**|**Dobra Nazwa (Kierunek Outcome)**|**Doskonała Nazwa (Mierzalny Outcome)**|
|"Nowy Edytor Procesów"|"Przyspieszenie wdrożeń AMODIT"|"**Skrócenie średniego czasu wdrożenia o 30%**"|
|"Moduł Raportowy w React"|"Udostępnienie samoobsługowej analityki (Self-Service BI)"|"**Redukcja zapytań PDM o raporty o 50%**" lub "**Zwiększenie liczby raportów tworzonych przez klientów o 25%**"|
|"Przebudowa UI"|"Zwiększenie retencji i satysfakcji użytkowników"|"**Podniesienie wskażnika NPS o 15 punktów**" lub "**Wzrost satysfakcji... (Cel: >80% ocen in-app)**"|
|"Bezpieczeństwo i zgodność"|"Osiągnięcie zgodności z RODO i ISO 27001"|"Osiągnięcie zgodności z RODO i ISO 27001" (W tym przypadku cel jest binarny i mierzalny sam w sobie)|

### 2. Paczka Wartości (MVP) (🎁 Prezent)

To **minimalna "Paczka Wartości" (MVP)**, którą możemy dostarczyć. Jest to artefakt _realizacji_, który odpowiada na `Krok 2: Definicja Celu i Pojemności MVP` i podlega `Zasadzie 1: Przestań Zaczynać, Zaczyj Kończyć`.

#### Kryterium Kwalifikacji (Test Lakmusowy)

- **Czy to jest** _**spójna**_ **wartość dla użytkownika?** (Najważniejszy test!)
    
    - ŹLE: "Logi systemowe MVP1" (Użytkownik nie dostaje _żadnej_ wartości z samych logów).
        
    - DOBRZE: "Moduł: Podstawowa diagnostyka systemu dla Admina" (To jest spójna wartość. MVP może _zawierać_ logi, listę procesów i ustawienia).
        
- **Czy można to wydać (ship)** _**niezależnie**_**?** Czy po skończeniu tej pracy, użytkownik końcowy (klient, admin) może zacząć z tego realnie korzystać?
    
- **Czy jest** _**wystarczająco małe**_**?** Musimy być w stanie to dowieźć w skończonym czasie (np. 1-3 miesiące). To jest nasza "ocena pojemności" z `Kroku 2`.
    

#### Jak dobrze nazwać Paczkę Wartości (MVP)?

Nazwa musi opisywać **dostarczalny produkt lub funkcjonalność** z perspektywy użytkownika. Ma być jasne, co dostanie "w prezencie".

**Format (Sugestia):** `[Obszar/Moduł]: [Opis dostarczanej paczki wartości]`

|   |   |
|---|---|
|**Zła Nazwa (Fragment, komponent)**|**Dobra Nazwa (Spójna "paczka" wartości)**|
|"Logi systemowe MVP1"|"Diagnostyka: Podstawowy audyt zdarzeń systemowych"|
|"Lista procesów MVP1"|(To prawdopodobnie Feature, a nie Epic/MVP)|
|"Wzmaknianie użytkowników..."|(To prawdopodobnie Feature, a nie Epic/MVP)|
|"Nowy Edytor Procesów" (zbyt duże)|"Edytor vNext (MVP1): Proces 'Hello World'"|

### 3. Feature (⚙️ Trybik)

Feature to **dobrze zdefiniowany komponent funkcjonalny**. To jest "myślenie komponentowe" zrobione dobrze – na właściwym poziomie hierarchii. Odpowiada na "Co" budujemy w ramach konkretnej 🎁 Paczki Wartości (MVP).

To jest główny artefakt, który jest "bohaterem" `Kroku 1: Mapowanie Kluczowych Funkcjonalności` oraz `Kroku 5: Analiza Głęboka`.

#### Kryterium Kwalifikacji (Test Lakmusowy)

- **Czy jest to** _**komponent**_ **lub** _**fragment**_ **większej 🎁 Paczki Wartości (MVP)?**
    
    - Prawdziwa 🎁 Paczka Wartości (jak "Proces 'Hello World'") _składa się_ z wielu ⚙️ Trybików (np. "Minimalny edytor diagramu", "Minimalny edytor formularza").
        
- **Czy** _**oblewa**_ **"Test Lakmusowy" na MVP?**
    
    - To jest test odwrotny: jeśli coś **nie może** być wydane niezależnie i **nie daje** samodzielnie spójnej wartości (jak "Logi systemowe MVP1"), to jest to ⚙️ **Trybik**, a nie 🎁 Paczka Wartości.
        
- **Czy jest** _**przedmiotem**_ **analizy (📖 Use Case)?**
    
    - Analizujemy (w `Kroku 5`) właśnie ⚙️ Trybiki – ich scenariusze, przypadki brzegowe i błędy.
        

#### Jak dobrze nazwać Feature?

Nazwa musi być jasna i opisywać konkretną funkcjonalność lub komponent.

**Format (Sugestia):** `[Nazwa komponentu/funkcji]`

|   |   |
|---|---|
|**Zła Nazwa (Zbyt ogólne lub to MVP)**|**Dobra Nazwa (Konkretna funkcja)**|
|"Diagnostyka: Podstawowy audyt..." (To jest 🎁 Paczka Wartości)|"Logi systemowe" (jako komponent tej Paczki)|
|"Edytor vNext: Proces 'Hello World'" (To jest 🎁 Paczka Wartości)|"Edytor diagramu (minimalny)" (jako komponent tej Paczki)|
|"Ulepszenia"|"Wzmacnianie użytkowników w komentarzach"|
|"Matryca"|"Matryca widoczności pól"|

### 4. Use Case (📖 Otwarta Książka)

Use Case to **szczegółowa specyfikacja analityczna**. To jest artefakt-wynik `Kroku 5: Analiza Głęboka`. Odpowiada na pytanie "Jak _dokładnie_ ten ⚙️ Trybik ma działać?".

Uwaga: Ten artefakt jest OPCJONALNY.

Stosujemy go tylko wtedy, gdy ⚙️ Trybik (Feature) jest na tyle złożony biznesowo, że wymaga szczegółowego rozpisania scenariuszy (Krok 5). Dla prostych ⚙️ Trybików (np. "Dodanie pola X do formularza Y"), pomijamy ten krok, a 📋 PBI są podpinane bezpośrednio pod ⚙️ Trybik.

#### Kryterium Kwalifikacji (Kiedy go tworzyć?)

- **Czy ⚙️ Trybik jest złożony?** Czy ma wiele scenariuszy, przypadków brzegowych, walidacji lub potencjalnych błędów, które trzeba opisać?
    
- **Czy opisuje** _**scenariusze**_**?** Musi zawierać "Happy Path" (scenariusz podstawowy) oraz, co kluczowe, "Scenariusze alternatywne i błędy".
    
- **Czy opisuje** _**interakcję**_ **Aktor-System?** Kto co klika i co system na to odpowiada?
    
- **Czy jest** _**podpięty**_ **pod ⚙️ Trybik?** Jeden ⚙️ Trybik (np. "Edytor diagramu") może mieć _wiele_ 📖 Use Case'ów (np. "Dodawanie kroku", "Walidacja połączenia", "Obsługa błędu zapisu").
    

### 5. PBI / Task (📋 Clipboard)

PBI (Product Backlog Item) lub Task to **atomowa jednostka pracy**. To jest artefakt-wynik `Kroku 6: Dekompozycja na PBI`. Odpowiada na pytanie "Co _fizycznie_ trzeba zrobić?".

#### Kryterium Kwalifikacji

- **Czy jest** _**wykonalne**_**?** Czy zespół deweloperski może to wziąć i "zrobić" (zazwyczaj w ciągu 1-3 dni)?
    
- **Czy jest** _**elementem**_ **📖 Use Case'u (lub ⚙️ Trybiku)?** Jeden 📖 Use Case (np. "Dodawanie kroku") jest dekomponowany na _wiele_ 📋 PBI (np. "Zrób endpoint API", "Zrób komponent UI", "Napisz test integracyjny"). Jeśli 📖 Use Case jest pominięty, 📋 PBI są podpięte bezpośrednio pod ⚙️ Trybik.
    
- **Czy jest** _**techniczne**_ **lub** _**funkcjonalne**_**?** Może to być zarówno historyjka użytkownika ("Jako X, chcę Y..."), jak i zadanie techniczne ("Zrefaktoryzuj usługę Z").
    

### Praktyczny Plan Działania (Jak posprzątać Twój Backlog)

Użyj tych _pięciu_ definicji, aby przejrzeć _każdą_ pozycję na swoim backlogu:

1. **Krok 1: Identyfikacja Inicjatyw (Grupowanie "Po Co?")**
    
    - Weź "Nowy Edytor Procesów". Zadaj pytanie "Po co?". Odpowiedź, np. "Aby skrócić czas wdrożeń", staje się Twoją Inicjatywą 💎 **"Skrócenie średniego czasu wdrożenia o 30%"**.
        
2. **Krok 2: Dekonstrukcja "Gigantów" na 🎁 Paczki Wartości**
    
    - "Nowy Edytor Procesów" (Gigant) oblewa test "wystarczająco małe". Zdekonstruuj go na _prawdziwe, horyzontalne_ 🎁 Paczki Wartości (MVP), np. 🎁 **"Edytor vNext (MVP1): Proces 'Hello World'"**.
        
3. **Krok 3: Konsolidacja i Degradacja "Fałszywych MVP" na ⚙️ Trybiki**
    
    - Masz pozycje: "Logi systemowe MVP1", "Lista procesów MVP1".
        
    - Oblewają one test "niezależnej wartości". To są ⚙️ **Trybiki (Features)**.
        
    - Stwórz _nowy, prawdziwy_ 🎁 Paczkę Wartości (MVP) o nazwie np. **"Platforma: Pakiet startowy Administratora"**.
        
    - Przenieś te "fałszywe MVP" _pod_ tę nową 🎁 Paczkę Wartości i zmień ich typ na ⚙️ **Feature**.
        
4. **Krok 4: Klasyfikacja Zbyt Małych Epików**
    
    - Masz "Wzmaknianie użytkowników w komentarzach MVP1".
        
    - Czy to jest 🎁 Paczka Wartości, czy ⚙️ Trybik? Zastosuj "Test Lakmusowy". Prawdopodobnie jest to ⚙️ **Trybik**, który powinien być częścią większej 🎁 Paczki Wartości (np. 🎁 "Współpraca: Komunikacja w sprawach v1").
        

Postępując w ten sposób, Twój backlog przestanie być płaską listą zadań, a zacznie być prawdziwym, strategicznym portfolio, które odzwierciedla nasz proces z `Wersja Zintegrowana.md`.

### Sekcja Specjalna: Jak klasyfikować Płatne Zlecenia Klienckie?

Praca "na zlecenie" (np. dla LOT, WIM) to największe ryzyko dla naszej strategicznej hierarchii. Musi być precyzyjnie klasyfikowana, aby backlog był "uczciwy".

Kluczem jest **Triage (Selekcja)**, którą musi wykonać PDM (Ty, Kamil, Damian) dla _każdego_ 🎁 Prezenta (MVP) pochodzącego ze zlecenia.

**Proces Triage (Selekcji):**

Zanim dodasz 🎁 Prezent do backlogu, zadaj pytanie:

1. **"Czy ta funkcja (np. 'Raport JRWA') jest strategiczna dla** _**core produktu**_ **AMODIT i dostarczy wartość** _**innym**_ **klientom w przyszłości?"**
    
    - **Jeśli TAK:** Ten 🎁 Prezent musi być podpięty pod odpowiednią _strategiczną_ 💎 **Inicjatywę** (np. 💎 "Skrócenie średniego czasu wdrożenia o 30%"). Klient (LOT) jest tu tylko "sponsorem" i dowodem biznesowym.
        
    - **Jak to śledzić?** Użyj **Etykiety (Tagu)** na 🎁 Prezentcie, np. `Kontrakt: LOT`, aby móc filtrować listę "paczek" dla klienta, _bez_ psucia hierarchii strategicznej.
        
2. **"Czy ta funkcja (np. 'Specyficzna integracja z systemem X') jest 'mało amodit-owa', dedykowana** _**tylko**_ **dla tego klienta i** _**nie**_ **planujemy jej rozwijać w core produktu?"**
    
    - **Jeśli TAK:** Ta praca nie może "zanieczyszczać" naszych strategicznych 💎 Inicjatyw. Musi trafić pod osobną, _komercyjną_ 💎 Inicjatywę.
        
    - **Stwórz 💎 Inicjatywę:** 💎 **"Zapewnienie przychodów z prac dedykowanych (Realizacja Zleceń Klienckich)"**.
        
    - **Cel (Outcome):** Mierzalnym celem jest 100% realizacji zakontraktowanych prac i zapewnienie X przychodów.
        
    - Ten 🎁 Prezent (MVP) podpinasz pod tę właśnie 💎 Inicjatywę.
        

Ta metoda pozwala zarządowi widzieć na Roadmapie, ile % mocy zespołu idzie na strategiczny rozwój _produktu_, a ile na komercyjny rozwój _projektów_.

### Sekcja Specjalna: Jak klasyfikować Błędy (Bugi 🐞)?

Błędy nie mogą istnieć w chaosie. Muszą być klasyfikowane według ich _celu biznesowego_ (PO CO je naprawiamy?). Każdy błąd musi być przypięty do nadrzędnego celu strategicznego.

#### Scenariusz 1: Błąd "Defensywny" (Utrzymanie Wartości)

- **Co to jest:** Błąd, który psuje _istniejącą_ funkcjonalność. Irytuje klientów, generuje tickety supportowe, obniża satysfakcję lub stabilność.
    
- **PO CO go naprawiamy:** Aby chronić nasze cele biznesowe (np. satysfakcję klienta, stabilność platformy).
    
- **Jak przypiąć:** Błąd jest przypinany **bezpośrednio** pod 💎 **Inicjatywę**, w którą uderza.
    
- Struktura:
    
    💎 Inicjatywa: "Wzrost satysfakcji użytkownika... (Cel: >80% ocen...)"
    
    |
    
    +--- 🎁 Paczka Wartości (MVP1): "Modernizacja UI: Nowy Dashboard"
    
    +--- 🐞 Bug (Defensywny): "Krytyczny błąd UI w mcase.aspx"
    
- **Wniosek:** Błąd 🐞 konkuruje o priorytet bezpośrednio z nowymi 🎁 Paczkami Wartości w ramach tej samej 💎 Inicjatywy.
    

#### Scenariusz 2: Błąd "Blokujący" (Umożliwienie Wartości)

- **Co to jest:** Błąd w _starym_ kodzie, który _uniemożliwia_ lub _blokuje_ pracę nad _nową_ 🎁 **Paczką Wartości (MVP)**.
    
- **PO CO go naprawiamy:** Aby umożliwić dowiezienie 🎁 Paczki Wartości. Wartość naprawy tego błędu jest równa wartości 🎁 Paczki, którą odblokowuje.
    
- **Jak przypiąć:** Błąd jest traktowany jako 📋 **PBI / Task** i jest przypinany **bezpośrednio** pod 🎁 **Paczkę Wartości (MVP)** (lub ⚙️ **Trybik**), którą blokuje.
    
- Struktura:
    
    🎁 Paczka Wartości (MVP2): "WCAG (MVP2): Zgodność modułu X"
    
    |
    
    +--- ⚙️ Feature: "Nawigacja klawiaturą w module X"
    
    +--- 🐞 Bug (Blokujący, jako PBI): "Naprawić błąd fokusa w starym komponencie Y"
[[2025-09-23 wtorek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 23 września 2025

---

#### 1. Zmiana logiki funkcji `Grant Temporary Access` (GTA)

- **Ryzyko:**
    
    - Użycie funkcji `GTA` na użytkowniku wewnętrznym (aktywnym w systemie) nie przynosi żadnego efektu, co jest nieintuicyjne dla wdrożeniowców. W specyficznym kontekście biznesowym klienta, gdzie byli pracownicy są ponownie zatrudniani, prowadzi to do problemów. 
        
- **Proponowane rozwiązanie:**
    
    - Klient zaproponował, aby w przypadku wywołania `GTA` na aktywnym użytkowniku wewnętrznym, system automatycznie wykonywał akcję `Forward Case` (przekazanie sprawy). 
        
    - Zespół zaproponował klientowi rozwiązanie alternatywne (workaround): stworzenie dedykowanej funkcji sprawdzającej, czy użytkownik jest wewnętrzny, i na tej podstawie warunkowe wywoływanie `GTA` lub `Forward Case` za pomocą reguł. 
        
- **Decyzja:**
    
    - Propozycja klienta dotycząca globalnej zmiany w działaniu `GTA` zostaje odrzucona. 4Funkcjonalność działa zgodnie z pierwotnym założeniem (dla użytkowników zewnętrznych) i jest stosowana u wielu klientów. 
        
    - Jest to specyficzny przypadek biznesowy jednego klienta, który nie zdecydował się na sfinansowanie zmiany. Klient może zaimplementować zaproponowany workaround. 
        
    - Zgłoszenie zostaje zamknięte. 
        
- **Zadania:**
    
    - Brak.
        

---

#### 2. Optymalizacja wydajności funkcji `HasDuplicates`

- **Ryzyko:**
    
    - Funkcja `HasDuplicates` ma problemy z wydajnością, co zostało zidentyfikowane podczas analizy problemu u jednego z klientów. 
        
- **Proponowane rozwiązanie:**
    
    - Konieczne jest wdrożenie wydajnego rozwiązania, zgodnego z wytycznymi zawartymi w zgłoszeniu. 
        
- **Decyzja:**
    
    - Zadanie jest ważne i musi zostać wykonane. 
        
    - Realizacją zajmie się osobiście Piotr, aby zagwarantować odpowiednią jakość i wydajność implementacji. 
        
    - Zadanie zostanie wykonane w perspektywie najbliższych 2-3 tygodni. 
        
- **Zadania:**
    
    - **Piotr:** Przeanalizuje i zaimplementuje optymalizację funkcji `HasDuplicates`. 
        

---

#### 3. Aliasy i tłumaczenia w module raportowym

- **Ryzyko:**
    
    - W module raportowym nazwy funkcji agregujących (np. `COUNT`) nie są przetłumaczone na język polski. 
        
    - Brak możliwości definiowania przyjaznych nazw (aliasów) dla kolumn, zwłaszcza pochodzących z zewnętrznych źródeł danych. 
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzenie tłumaczeń dla nazw funkcji agregujących. 
        
    - Dodanie mechanizmu aliasowania kolumn w źródłach danych raportów. 
        
- **Decyzja:**
    
    - Tłumaczenie funkcji agregujących (`COUNT` -> `Liczba`) prawdopodobnie zostało już zrealizowane na środowisku deweloperskim. 
        
    - Główny temat zostanie zdjęty z tablicy Rady Architektów i rozbity na mniejsze zadania implementacyjne. 
        
- **Zadania:**
    
    - **Łukasz:** Zweryfikuje, czy tłumaczenia funkcji agregujących zostały wdrożone, i w razie potrzeby dokończy temat. Rozbije również zadanie dotyczące aliasów na mniejsze części. 
        

---

#### 4. Propozycja nowej funkcji `CallFunctionEx`

- **Ryzyko:**
    
    - Brak. Jest to propozycja nowej funkcjonalności.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzenie nowej, rozszerzonej funkcji do wywoływania innych funkcji, co mogłoby być przydatne w kontekście nowego typu procesów "Biblioteka". 
        
- **Decyzja:**
    
    - Pomysł jest dobry, ale obecnie nie jest priorytetem. Istnieją ważniejsze zadania architektoniczne.
        
    - Zadanie zostaje odłożone w czasie (np. na za miesiąc) do ponownej analizy. 
        
- **Zadania:**
    
    - Brak.
        

---

#### 5. Propozycja nowej funkcji `RunAsUser`

- **Ryzyko:**
    
    - Brak. Jest to propozycja nowej funkcjonalności.
        
- **Proponowane rozwiązanie:**
    
    - Stworzenie funkcji `RunAsUser`, która pozwoliłaby na wykonanie reguły (np. czasowej) w kontekście innego użytkownika niż domyślny `System User`. Umożliwiłoby to np. przekazywanie spraw w imieniu dedykowanego konta, jak "Pokój Pocztowy". 
        
- **Decyzja:**
    
    - Obecnie istniejące obejście – zmiana nazwy systemowego użytkownika (`System User`) na inną, np. "Przedstawiciel systemu" – jest wystarczające do realizacji tego typu potrzeb biznesowych. 
        
    - Wprowadzenie nowej funkcji nie jest obecnie krytyczne i zostaje odłożone na przyszłość. 
        
- **Zadania:**
    
    - Brak.
        

---

#### 6. Logowanie zmian w parametrach systemowych

- **Ryzyko:**
    
    - Zmiany niektórych parametrów systemowych (odpowiedzialnych za kolory w interfejsie) nie są obecnie rejestrowane w logach aktywności administracyjnej. 
        
    - Propozycja wykorzystania kolumny `par_modified_by_id` do ogólnego audytu zmian mogłaby zakłócić działanie mechanizmu "zasady czterech oczu", do którego jest ona przeznaczona. 
        
- **Proponowane rozwiązanie:**
    
    - Uzupełnianie kolumny `par_modified_by_id` w tabeli `Parameters` przy każdej modyfikacji parametru, aby stworzyć uproszczony log zmian. 
        
    - Rozszerzenie logowania w module aktywności administracyjnej tak, aby obejmowało wszystkie zmiany parametrów. 
        
- **Decyzja:**
    
    - Propozycja modyfikacji tabeli `Parameters` zostaje odrzucona. 33333333Kolumny `par_modified_by_id` i `par_accepted_by_id` są zarezerwowane wyłącznie dla mechanizmu "zasady czterech oczu". 
        
    - Właściwym miejscem do śledzenia historii zmian parametrów jest moduł logów aktywności użytkowników. 
        
    - Należy zapewnić, że wszystkie zmiany parametrów systemowych są poprawnie rejestrowane w logu aktywności administracyjnej. 
        
- **Zadania:**
    
    - **Łukasz:** Zgłosi zadanie polegające na weryfikacji i zapewnieniu, że zmiany wszystkich parametrów (zwłaszcza tych modyfikowanych w oknach dialogowych) są poprawnie logowane w aktywnościach administracyjnych. 
        

---
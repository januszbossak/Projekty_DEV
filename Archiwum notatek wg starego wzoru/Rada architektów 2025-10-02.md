[[2025-10-02 czwartek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 2 października 2025

---

#### 1. Prezentacja i weryfikacja nowych raportów systemowych

- **Ryzyko:**
    
    - **Merytoryczne:** Prezentowane raporty, np. "Średni czas procesowania spraw", opierają się na technicznie poprawnej, ale biznesowo mylącej logice. Mieszają dane spraw otwartych i zamkniętych, a dla spraw w toku nie uwzględniają czasu spędzonego na bieżącym etapie, co prowadzi do nieprawdziwych wniosków.
        
    - **Użyteczność (UX):** Wizualizacje (tzw. "tree map") są nieczytelne, gdy zawierają wiele elementów, a zastosowane kolory nie niosą dodatkowej informacji. Niektóre etykiety mają bardzo niski kontrast (np. biały tekst na jasnoszarym tle), co czyni je nieczytelnymi.
        
    - **Niespójność:** Interfejs jest niejednolity językowo (mieszanka polskiego i angielskiego). Tytuły raportów i filtrów są mylące z biznesowego punktu widzenia (np. "osoby najczęściej tworzące" zamiast "osoby, które stworzyły najwięcej").
        
    - **Błąd techniczny:** Link do raportów systemowych w menu głównym nie działa, jeśli użytkownik ma ustawiony widok raportów w trybie listy.
        
- **Proponowane rozwiązanie:**
    
    - **Merytoryczne:** Należy rozdzielić analizę na dwie odrębne kategorie: **sprawy zamknięte** (analiza historyczna od utworzenia do zamknięcia) oraz **sprawy w toku** (analiza bieżąca w celu identyfikacji wąskich gardeł).
        
    - **Użyteczność (UX):** Każdy raport i pulpit systemowy powinien mieć jasny opis biznesowy, wyjaśniający, co dokładnie prezentuje i jak liczone są wskaźniki. Opis ten mógłby być dostępny pod ikoną "i" (informacja). Wizualizacje powinny być przemyślane tak, aby kolor również niósł informację (np. gradient obrazujący liczbę spraw).
        
    - **Błąd techniczny:** Jako najprostsze rozwiązanie problemu z linkiem, przejście do raportów systemowych z menu głównego powinno wymuszać przełączenie widoku na tryb "kafelkowy".
        
- **Decyzja:**
    
    - Prezentowane raporty to dobra baza (MVP), ale wymagają gruntownej przebudowy pod kątem logiki biznesowej i użyteczności.
        
    - Konieczne jest przygotowanie precyzyjnych opisów biznesowych dla każdego raportu, a następnie ich weryfikacja i przeprojektowanie.
        
    - Błąd techniczny z linkiem w widoku listy zostanie naprawiony poprzez wymuszenie widoku kafelkowego.
        
    - Uprawnienia do edycji raportów systemowych zostaną rozszerzone również na pulpity systemowe.
        
- **Zadania:**
    
    - **Łukasz:** Przygotuje opisy biznesowe dla wszystkich istniejących raportów, wyjaśniające ich cel i sposób działania.
        
    - **Ania:** Poprawi błąd związany z niedziałającym linkiem w widoku listy.
        
    - **Zespół:** W przyszłym tygodniu odbędzie się spotkanie w celu omówienia przygotowanych opisów i zaplanowania dalszych prac nad raportami.
        

---

#### 2. Problemy techniczne z tworzeniem źródeł danych

- **Ryzyko:**
    
    - Występuje problem z tworzeniem lokalnych, synchronizowanych źródeł danych na bazach MSSQL. Funkcjonalność ta jest kluczowa dla działania nowych, wydajnych raportów systemowych. Na bazach MySQL problem nie występuje.
        
- **Proponowane rozwiązanie:**
    
    - Aby nie wstrzymywać prac, w pierwszej kolejności należy dokończyć implementację i testy dla środowisk opartych na MySQL.
        
- **Decyzja:**
    
    - Prace zostaną podzielone na etapy. Priorytetem jest zapewnienie pełnej funkcjonalności dla MySQL, a następnie rozwiązanie problemu na MSSQL.
        
- **Zadania:**
    
    - **Ania:** Skupi się na dokończeniu prac dla MySQL, a w następnej kolejności zajmie się diagnozą i naprawą problemu na MSSQL.
        

---
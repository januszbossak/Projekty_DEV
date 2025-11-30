[[2025-09-25 czwartek]] [[Rada architektów 2025-10-14]]

### Spotkanie rady architektów z dnia 25 września 2025

---

#### 1. Automatyzacja zarządzania dokumentami i sprawami

- **Ryzyko:**
    
    - Użytkownicy zapominają zamykać sesje edycji dokumentów na SharePoint, co stwarza ryzyko utraty danych i blokuje dokumenty na wiele tygodni.
        
    - Systemy klientów gromadzą dużą liczbę "martwych" spraw, które zostały utworzone, ale nigdy nie uruchomione (np. wnioski urlopowe tworzone tylko w celu sprawdzenia limitu dni).
        
    - Obecne rozwiązania tych problemów opierają się na nieefektywnych, okresowych regułach lub ręcznych operacjach na bazie danych.
        
- **Proponowane rozwiązanie:**
    
    - **Dla dokumentów:** Wprowadzenie opcjonalnego, systemowego zadania (job), które automatycznie zamykałoby sesje edycji dokumentów po upływie zadanego czasu bezczynności (np. 2 dni), liczonego od ostatniej modyfikacji w SharePoint.
        
    - **Dla spraw:** Wprowadzenie mechanizmu automatycznego czyszczenia:
        
        - Na poziomie definicji procesu dodać opcję automatycznego usuwania spraw, które nie opuściły pierwszego etapu w określonym czasie.
            
        - Wprowadzić globalne, opcjonalne ustawienie systemowe do permanentnego usuwania spraw z kosza po upływie zadanego czasu (np. roku).
            
- **Decyzja:**
    
    - Oba pomysły są słuszne i powinny zostać wdrożone jako konfigurowalne, opcjonalne zadania (joby), aby nie zmieniać obecnego działania systemu u klientów, którzy tego nie potrzebują.
        
- **Zadania:**
    
    - **Kamil:** Zgłosi oba pomysły jako zadania do implementacji, z uwzględnieniem ustaleń (konfiguracja per proces dla nieuruchomionych spraw i globalna dla kosza).
        

---

#### 2. Usprawnienia interfejsu użytkownika

- **Ryzyko:**
    
    - Na długich formularzach z zakładkami, użytkownicy muszą przewijać stronę do góry, aby przełączyć zakładkę, co jest niewygodne i spowalnia pracę.
        
    - Nowy widok powiązań procesu jest nieintuicyjny – legenda jest mylona z filtrami, a sam widok nie jest kompletny, gdyż nie analizuje powiązań wewnątrz reguł.
        
- **Proponowane rozwiązanie:**
    
    - **Nawigacja w zakładkach:** Dodanie strzałek nawigacyjnych "następna/poprzednia zakładka" na dole formularza. Odrzucono pomysł "przyklejonej" listy zakładek z obawy o zmniejszenie przestrzeni roboczej.
        
    - **Widok powiązań:** Dodanie realnej funkcji filtrowania (np. pokaż tylko powiązane grupy) oraz opcji eksportu widoku do celów dokumentacyjnych.
        
- **Decyzja:**
    
    - Nawigacja za pomocą strzałek to dobre usprawnienie, ale powinno być potraktowane jako propozycja płatnej modyfikacji dla klienta, który zgłosił taką potrzebę.
        
    - Usprawnienia widoku powiązań są słuszne i powinny zostać uwzględnione w dalszym rozwoju tej funkcjonalności.
        
- **Zadania:**
    
    - Brak.
        

---

#### 3. Rozwój raportowania i analityki

- **Ryzyko:**
    
    - Administratorzy nie mają narzędzi do weryfikacji, które procesy są aktywnie używane, a które są przestarzałe i mogą zostać zarchiwizowane.
        
- **Proponowane rozwiązanie:**
    
    - Stworzenie nowego raportu systemowego, który dla każdego procesu pokazywałby kluczowe statystyki: liczbę istniejących spraw oraz datę utworzenia ostatniej sprawy.
        
    - Umieszczenie linku do raportów systemowych w głównym menu ustawień (obok zarządzania użytkownikami, grupami itp.), aby ułatwić do nich dostęp.
        
- **Decyzja:**
    
    - Pomysł zostaje w pełni zaakceptowany. Nowy raport zostanie stworzony, a dostęp do niego będzie umieszczony w łatwo dostępnym miejscu w panelu administracyjnym.
        
- **Zadania:**
    
    - **Łukasz:** Dopisze zadanie stworzenia nowego raportu systemowego do listy zadań.
        

---

#### 4. Zarządzanie bazą wiedzy AI

- **Ryzyko:**
    
    - Obecnie tylko administratorzy systemu mogą zarządzać bazą wiedzy dla AI (Copilot), co uniemożliwia delegowanie tego zadania do odpowiednich działów merytorycznych (np. HR, Dział Prawny).
        
- **Proponowane rozwiązanie:**
    
    - Dodanie nowej roli uprawnień ("Administrator Bazy Wiedzy"), która pozwoliłaby wyznaczonym osobom na zarządzanie treściami bez konieczności nadawania im pełnych uprawnień administratora systemu.
        
    - Rozszerzenie funkcjonalności o możliwość dodawania do bazy wiedzy całych plików (np. regulaminów w formacie PDF) zamiast tylko wklejania tekstu.
        
    - Wprowadzenie daty obowiązywania (`od-do`) oraz wersjonowania wpisów w bazie wiedzy, aby AI korzystało zawsze z aktualnych danych, zachowując jednocześnie dostęp do archiwalnych wersji.
        
- **Decyzja:**
    
    - Wszystkie propozycje są uznane za słuszne i kluczowe dla rozwoju komponentu AI.
        
- **Zadania:**
    
    - Brak przypisanych zadań w trakcie spotkania.
        

---

#### 5. Rozszerzenie funkcji reguł i poprawki błędów

- **Ryzyko:**
    
    - Brak możliwości programowego (z poziomu reguły) odświeżenia lub wyeksportowania danych z pola typu "Raport".
        
    - Funkcja `Grant Temporary Access` (GTA) błędnie oblicza datę ważności tokenu – ustawienie ważności na 1 dzień w praktyce daje dostęp na 2 dni.
        
- **Proponowane rozwiązanie:**
    
    - Rozszerzenie istniejącej funkcji `ExecuteAction` o obsługę pól typu "Raport" i dodanie akcji takich jak `refresh`, `print`, `exportToExcel`.
        
    - Poprawienie logiki obliczania daty ważności tokena w funkcji GTA.
        
- **Decyzja:**
    
    - Funkcja `ExecuteAction` zostanie rozszerzona zgodnie z propozycją.
        
    - Błąd w działaniu GTA zostanie naprawiony.
        
- **Zadania:**
    
    - **Łukasz:** Zaktualizuje zgłoszenie dotyczące `ExecuteAction`, aby odzwierciedlało decyzję o rozszerzeniu istniejącej funkcji.
        
    - **Piotr:** Zostanie mu przypisane zadanie naprawy błędu w funkcji GTA.
        

---

#### 6. Usprawnienia dla środowisk testowych

- **Ryzyko:**
    
    - Podczas testów nowych procesów, administratorzy muszą ręcznie (z poziomu bazy danych) usuwać maile z kolejki, aby uniknąć przypadkowego wysłania powiadomień do kluczowych osób w firmie (np. zarządu).
        
- **Proponowane rozwiązanie:**
    
    - W nowym interfejsie kolejki maili dodać możliwość zaznaczania i usuwania wiadomości.
        
    - Wprowadzić na poziomie definicji procesu opcję "trybu testowego", która przekierowywałaby wszystkie maile wysyłane w ramach tego procesu na wskazany adres dewelopera/testera.
        
- **Decyzja:**
    
    - Oba pomysły są bardzo wartościowe. Zarówno możliwość ręcznego czyszczenia kolejki, jak i opcja globalnego przekierowania maili dla danego procesu znacząco ułatwią testowanie.
        
- **Zadania:**
    
    - Brak przypisanych zadań w trakcie spotkania.
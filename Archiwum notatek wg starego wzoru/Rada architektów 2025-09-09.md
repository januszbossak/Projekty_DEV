[[2025-09-09 wtorek]] [[Rada architektów 2025-10-14]]
Jasne, oto scalona i uszczegółowiona wersja podsumowania spotkania z 9 września, stworzona na podstawie analizy obu dostarczonych wariantów.

### Spotkanie Rady Architektów z dnia 9 września 2025

---

#### 1. Usprawnienie podglądu plików tekstowych i specjalistycznych

- **Ryzyko:**
    
    - Obecnie podgląd dla plików `.txt` nie działa poprawnie – zamiast wyświetlania, plik jest od razu pobierany (na widoku sprawy) lub panel podglądu zawiesza się (na widoku raportu), co wskazuje na niespójność mechanizmu.
        
    - Brak jest wsparcia dla podglądu innych popularnych formatów tekstowych, takich jak `.json`, `.xml`, `.md` (Markdown) czy plików `.log`, co utrudnia pracę deweloperom i analitykom.
        
    - Wyświetlanie plików `.html` bez odpowiednich zabezpieczeń (np. w `iframe` z trybem `sandbox`) stwarza poważne ryzyko ataków typu XSS.
        
    - Funkcja API `getAttachmentContent` nie zwraca czystej treści pliku tekstowego, lecz dodaje do niej metadane (np. autora), co utrudnia automatyzację i analizę.
        
    - Generowanie podglądu dla niektórych typów plików (np. dużych plików `.xlsm` z makrami) może powodować znaczne spowolnienie i obciążenie systemu.
        
- **Proponowane rozwiązanie:**
    
    - Priorytetowo naprawić błąd niedziałającego podglądu dla plików `.txt` w ramach prac nad nowym komponentem w technologii React.
        
    - Rozszerzyć funkcjonalność podglądu o natywne wsparcie dla formatów `.json`, `.xml`, `.html`, `.log` oraz `.md`.
        
    - Wszystkie pliki tekstowe, a w szczególności `.html`, muszą być wyświetlane w bezpiecznym elemencie `iframe` z atrybutem `sandbox`, aby zablokować wykonanie potencjalnie złośliwych skryptów.
        
    - Stworzyć konfigurowalną listę rozszerzeń plików, dla których podgląd jest obsługiwany, z możliwością globalnego wykluczenia formatów problematycznych i obciążających system.
        
    - Poprawić funkcję `getAttachmentContent`, aby zwracała wyłącznie surową zawartość załącznika, bez dodatkowych metadanych.
        
- **Decyzja:**
    
    - Zostanie utworzone zadanie mające na celu naprawę podglądu dla plików `.txt` oraz rozszerzenie go o inne formaty tekstowe z zachowaniem zasad bezpieczeństwa (`sandbox`). Kwestia renderowania Markdown (zamiast pokazywania surowego kodu) zostanie odroczona do osobnej analizy.
        
    - Problem z nieprawidłowymi danymi zwracanymi przez `getAttachmentContent` zostanie osobno zweryfikowany i zgłoszony jako odrębne zadanie.
        
- **Zadania:**
    
    - **Damian:** Przygotuje i przekaże Przemkowi szczegółowe wymagania dotyczące usprawnienia mechanizmu podglądu, uwzględniając wszystkie omawiane formaty i wymogi bezpieczeństwa.
        
    - **Przemek:** Zweryfikuje i naprawi problem z podglądem plików `.txt` w ramach prac nad komponentem podglądu w raportach.
        
    - **Janusz:** Dokładnie przetestuje działanie funkcji `getAttachmentContent` i, jeśli problem się potwierdzi, utworzy formalne zgłoszenie błędu.
        

---

#### 2. Usprawnienia w raportach typu Gantt

- **Ryzyko:**
    
    - Na zbiorczych (agregujących) belkach na wykresie Gantta wyświetlane są nieprawidłowe, mylące dane. Etykieta oraz `tooltip` (dymek z informacjami) pobierane są z pierwszego elementu podrzędnego, zamiast być sumą lub poprawnie wyliczonym zakresem dla wszystkich elementów w grupie.
        
- **Proponowane rozwiązanie:**
    
    - Całkowicie usunąć wyświetlanie dynamicznej etykiety (np. "Ilość dni") ze zbiorczych belek, ponieważ nie ma logicznego, uniwersalnego sposobu na agregację wartości tekstowych z elementów podrzędnych.
        
    - Poprawić działanie `tooltipa` dla belek agregujących, tak aby zawsze pokazywał prawidłowy, wyliczony zakres dat (`od` i `do`) obejmujący wszystkie elementy podrzędne (data rozpoczęcia z najwcześniejszego zadania i data zakończenia z najpóźniejszego).
        
- **Decyzja:**
    
    - Etykiety na belkach agregujących zostaną usunięte. `Tooltip` zostanie poprawiony, aby wyświetlał wyłącznie prawidłowy, zagregowany zakres dat "od-do". Jest to rozwiązanie MVP, które szybko i skutecznie eliminuje błąd logiczny w prezentacji danych.
        
- **Zadania:**
    
    - **Damian:** Przygotuje szczegółowy opis zadania dla Marka, precyzując, że etykieta ma zostać usunięta, a `tooltip` ma poprawnie kalkulować i wyświetlać daty.
        
    - **Marek:** Zmodyfikuje komponent raportu Gantt zgodnie z podjętą decyzją.
        

---

#### 3. Tłumaczenia i aliasy dla etykiet w raportach

- **Ryzyko:**
    
    - W raportach, szczególnie tych opartych na źródłach systemowych lub zewnętrznych, nazwy kolumn oraz etykiety osi i agregacji (np. "count", "sum", "report_id") są wyświetlane w języku angielskim, co jest niezrozumiałe dla użytkowników biznesowych.
        
    - Brak jest możliwości nadawania własnych, kontekstowych nazw (aliasów) dla pól, co utrudnia tworzenie czytelnych wizualizacji (np. zmiana "count(Report ID)" na "Liczba zgłoszeń").
        
- **Proponowane rozwiązanie:**
    
    - **Krok 1 (Globalne tłumaczenia):** Rozszerzyć mechanizm tłumaczeń w źródłach danych, aby można było centralnie zdefiniować tłumaczenia dla nazw kolumn w różnych językach (np. "report_id" -> "ID Raportu"). Raporty będą automatycznie korzystać z tych tłumaczeń.
        
    - **Krok 2 (Tłumaczenia agregacji):** Wprowadzić natywne, poprawne wyświetlanie istniejących w systemie tłumaczeń dla standardowych funkcji agregujących (np. "sum" -> "suma", "count" -> "liczba").
        
    - **Krok 3 (Aliasy per raport):** Dodać w konfiguracji raportu możliwość nadawania własnych, niestandardowych etykiet (aliasów) dla osi wykresów i kolumn, które nadpiszą domyślne nazwy (np. zamiast "suma (Liczba dni urlopu)" użytkownik wpisze "Łączna liczba dni wolnych").
        
- **Decyzja:**
    
    - Propozycja zostanie wdrożona w etapach. W pierwszej kolejności zaimplementowane zostaną kroki 1 i 2 (globalne tłumaczenia w źródłach danych i tłumaczenia funkcji agregujących). Możliwość nadawania własnych aliasów w raportach zostanie dodana w kolejnym kroku jako osobne zadanie.
        
- **Zadania:**
    
    - **Łukasz:** Rozpisze istniejące zgłoszenie na mniejsze, oddzielne zadania, zgodnie z ustalonymi trzema krokami realizacji.
        

---

#### 4. Zarządzanie szablonami maili systemowych

- **Ryzyko:**
    
    - Klienci, którzy modyfikują standardowe szablony maili systemowych, tracą swoje zmiany podczas każdej aktualizacji, ponieważ pliki są bezwarunkowo nadpisywane.
        
    - Obecny wygląd maili jest przestarzały i nie pasuje do nowoczesnego interfejsu systemu.
        
    - Nieprawidłowa modyfikacja treści szablonów przez klientów może powodować, że wiadomości będą klasyfikowane jako spam przez serwery pocztowe.
        
- **Proponowane rozwiązanie:**
    
    - **Rozwiązanie natychmiastowe (MVP):** Wprowadzić prosty mechanizm pozwalający na wykluczenie wybranych szablonów maili z procesu aktualizacji. Będzie to realizowane przez dodanie nowej kolumny w bazie danych (np. `is_custom`), która będzie flagą oznaczającą, że dany szablon nie powinien być nadpisywany.
        
    - **Rozwiązanie docelowe (w przyszłości):** Zbudować całkowicie nowy, elastyczny mechanizm zarządzania szablonami z dedykowanym interfejsem w ustawieniach systemowych. Pozwoliłoby to na bezpieczne tworzenie i edycję własnych wersji szablonów, bez ryzyka ich utraty, oraz na odświeżenie ich wyglądu.
        
- **Decyzja:**
    
    - W trybie pilnym zostanie wdrożone rozwiązanie MVP (dodanie flagi do bazy danych), które zablokuje nadpisywanie zmodyfikowanych szablonów i rozwiąże największy problem klientów. Przebudowa całego systemu maili zostanie zaplanowana na przyszłość jako odrębny, duży projekt.
        
- **Zadania:**
    
    - **Damian:** Przygotuje formalny opis zadania deweloperskiego na wdrożenie rozwiązania MVP.
        
    - **Piotr:** Zaimplementuje mechanizm pomijania szablonów maili podczas aktualizacji systemu.
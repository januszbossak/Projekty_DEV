

## 1. Priorytetyzacja zadań raportowych i weryfikacja Data Source

Kontekst i Problem (Narracja):

Podczas przeglądu zadań poruszono temat dashboard_datasource_synchronization oraz problemów z raportami. Zidentyfikowano konflikt priorytetów między zadaniem dotyczącym logowania w MS SQL a zadaniem naprawczym dla raportów, które przypisane jest do Anny Skupińskiej. Celem jest ustalenie kolejności prac, aby najszybciej rozwiązać błędy wpływające na bieżącą obsługę błędów.

**Zidentyfikowane Ryzyka:**

- Brak realizacji zadania raportowego utrudnia diagnozowanie i rozwiązywanie większości błędów w tym obszarze.
    

**Proponowane Rozwiązania Techniczne:**

- Przesunięcie zadania związanego z logowaniem w MS SQL na dalszy plan (funkcjonalność ta jest dostępna w nowszych wersjach silnika).
    
- Skupienie się na zadaniu "raportowym" jako priorytecie nr 1.
    

**Decyzja (Twarde ustalenia):**

- Zadanie dotyczące `dashboard_datasource_synchronization` nie jest krytyczne i zostaje odłożone.
    
- Anna Skupińska ma zająć się naprawą raportów w pierwszej kolejności, gdyż jest to kluczowe dla uproszczenia obsługi błędów.
    

**Zadania (Action Items):**

- **Anna Skupińska:** Przejąć i zrealizować zadanie dotyczące naprawy raportów (Priorytet 1).
    
- **Janusz Bossak:** Przygotować listę braków funkcjonalnych w raportach do omówienia na kolejnej Radzie.
    

---

## 2. Wyświetlanie pustych zasobów na wykresie Gantta (Zgłoszenie 16558)

Kontekst i Problem (Narracja):

Klient zgłosił problem po aktualizacji, polegający na zmianie sposobu wyświetlania danych na wykresie Gantta. Wcześniej ładowane były wszystkie kategorie (np. wszystkie pokoje, nawet te wolne), co pozwalało na planowanie. Obecnie system ładuje tylko te zasoby, które mają przypisane sprawy w danym okresie. Problem dotyczy konfliktu między oczekiwaniami funkcjonalnymi klienta (widok "wolnych slotów") a wydajnością systemu.

**Zidentyfikowane Ryzyka:**

- Powrót do starej metody (ładowanie wszystkiego) grozi drastycznym spadkiem wydajności przy dużych wolumenach danych (przykład AmRest i setek tysięcy spraw).
    
- Brak widoczności wolnych zasobów uniemożliwia klientowi efektywne planowanie.
    

**Proponowane Rozwiązania Techniczne:**

- Ograniczenie poprawek wyłącznie do nowego modułu raportowego, aby promować migrację na wersję subskrypcyjną.
    
- Docelowo: Wprowadzenie parametryzacji lub słownika zdefiniowanej, skończonej listy zasobów, zamiast pobierania ich dynamicznie ze spraw.
    

**Decyzja (Twarde ustalenia):**

- Nie wprowadzamy zmian w starym module ("działało inaczej, a teraz działa inaczej" nie jest traktowane jako błąd krytyczny w starym kodzie).
    
- Klient otrzyma sugestię korzystania z nowych raportów, które częściowo rozwiązują problem (filtrowanie).
    
- Temat kompleksowej przebudowy mechanizmu ładowania zasobów zostaje odłożony ("odwieszony na kołek") do czasu prac nad nowym modułem.
    

**Zadania (Action Items):**

- **Damian Kamiński / Kamil Dubaniowski:** Przekazać klientowi sugestię przejścia na nowe raporty zamiast wdrażania poprawki w starym module.
    

---

## 3. Wydajność Trust Center i zarządzanie Hot Storage

Kontekst i Problem (Narracja):

W systemie Trust Center występuje krytyczny problem z zapełnianiem się "hot storage". Zadanie cykliczne (BackgroundWorkers) odpowiedzialne za usuwanie/przenoszenie plików nie nadąża z przetwarzaniem dużej liczby dokumentów (np. od klienta Rossmann), ponieważ przetwarza tylko małe paczki (25 sztuk) i działa w procesie webowym.

**Zidentyfikowane Ryzyka:**

- Całkowite zatkanie się Trust Center i brak możliwości przetwarzania nowych dokumentów.
    
- Wysokie koszty skalowania hot storage w górę.
    

**Proponowane Rozwiązania Techniczne:**

- **Doraźne:** Zwiększenie limitu przetwarzanych dokumentów w jednej paczce (z 25 na np. 200-500).
    
- **Docelowe:** Wydzielenie zadań cyklicznych (jobów) z procesu webowego do oddzielnej usługi (mikroserwisu). Priorytetem jest obsługa blockchain, a następnie czyszczenie storage.
    
- Weryfikacja czasu retencji plików w hot storage (ewentualne skrócenie z 30 do 14 dni).
    

**Decyzja (Twarde ustalenia):**

- Natychmiastowe wdrożenie rozwiązania doraźnego (zwiększenie limitu paczki).
    
- Rozpoczęcie prac nad architektonicznym wydzieleniem jobów do osobnej usługi.
    
- Marek Dziakowski dzieli czas pracy: tydzień na Trust Center / tydzień na inne priorytety, mimo wydłużenia czasu realizacji.
    

**Zadania (Action Items):**

- **Marek Dziakowski:** Dodać ustawienie i zwiększyć limit liczby dokumentów przetwarzanych w jednym cyklu usuwania z hot storage.
    
- **Marek Dziakowski:** Założyć Feature i powiązane PBI na "Przeniesienie zadań cyklicznych do usługi" (priorytet: blockchain, potem reszta).
    

---

## 4. Błąd wyświetlania daty synchronizacji słowników

Kontekst i Problem (Narracja):

W rejestrach i słownikach wyświetlana jest nieprawidłowa data ostatniej synchronizacji. Wynika to ze zmiany miejsca przechowywania tej informacji – obecnie system nie pobiera jej z tabeli historii synchronizacji.

**Zidentyfikowane Ryzyka:**

- Dezinformacja użytkownika (wyświetlanie wykrzyknika sugerującego błąd).
    

**Proponowane Rozwiązania Techniczne:**

- Modyfikacja endpointów pobierających właściwości słownika/rejestru, aby pobierały datę z tabeli historii synchronizacji.
    

**Decyzja (Twarde ustalenia):**

- Problem zaklasyfikowano jako "kosmetykę".
    
- Ze względu na brak blokującego wpływu na działanie systemu, temat zostaje odpięty z bieżącej agendy Rady i nie będzie realizowany w trybie pilnym.
    

**Zadania (Action Items):**

- Brak zadań do natychmiastowej realizacji.
    

---

## 5. Standardy dokumentacji (PBI)

Kontekst i Problem (Narracja):

Podczas omawiania zadań Trust Center zwrócono uwagę na konieczność lepszego dokumentowania prac. Pojawił się wymóg formalizacji zadań w systemie zarządzania projektami.

**Zidentyfikowane Ryzyka:**

- Trudności w testowaniu i tworzeniu dokumentacji przy braku opisanych wymagań.
    
- Ryzyko nieprzemyślanych rozwiązań przy braku etapu spisywania założeń.
    

**Proponowane Rozwiązania Techniczne:**

- Wykorzystanie AI do generowania opisów PBI na podstawie krótkich notatek deweloperskich.
    

**Decyzja (Twarde ustalenia):**

- Wprowadzono absolutny zakaz realizacji prac bez założonego PBI (Product Backlog Item).
    
- Każde PBI musi zawierać opis, a nie tylko tytuł.
    

**Zadania (Action Items):**

- **Wszyscy członkowie zespołu:** Zakładać i opisywać PBI przed przystąpieniem do realizacji jakiegokolwiek zadania.
## Spotkanie rady architektów z dnia 16 października 2025

---

#### 1. Wydzielenie funkcjonalności dodawania do Blockchaina (TrustCenter)

- **Ryzyko:**
    
    - Obecnie zadanie dodawania dokumentów do blockchaina jest wykonywane przez dwa serwery webowe, co prowadzi do sytuacji, w której zadania są dodawane jednocześnie do tego samego ostatniego bloku, powodując zawieszanie się operacji (dokumenty nie są dołączane).
        
    - Skala TrustCenter drastycznie się zwiększa z roku na rok, a problem wiszących dokumentów urósł z kilku do ponad 50, co wymaga kompleksowego rozwiązania, które sprawdzi się w większej .
        
    - Brak obsługi scenariusza, w którym dwie osoby naraz próbują podpisać ten sam dokument3333.
        
- **Proponowane rozwiązanie:**
    
    - Przerobienie i wydzielenie funkcji dodawania do blockchaina (podpisywania/dodawania pliku do bloku) do oddzielnego serwisu/procesu .
        
    - Zastosowanie kolejki (jeden wątek/worker), do której serwery webowe będą zgłaszać zadania. Worker będzie je przetwarzał po kolei, co jest kluczowe ze względu na wymóg zachowania kolejności operacji w blockchainie .
        
    - Zastosowanie konteneryzacji (Docker) dla nowego serwisu, podobnie jak w przypadku usług AI Mateusza. Pozwoli to na łatwe wdrożenie do chmury (Azure) i, jeśli klient się zgodzi, lokalnie (on-premises) za pomocą `docker-compose`.
        
    - W początkowej fazie rezygnacja z dynamicznego powiadamiania użytkownika o zakończeniu operacji, zastępując je informacją o oczekiwaniu na maila lub ręcznym odświeżeniem statusu .
        
    - Docelowo, dla powiadamiania użytkownika rozważano SignalR (Azure SignalR Service) lub wykorzystanie drugiej kolejki, ale uznano to za drugi krok po wydzieleniu usługi .
        
- **Decyzja:**
    
    - Konieczne jest jak najszybsze wydzielenie funkcjonalności dodawania do blockchaina (TrustCenter) do oddzielnej usługi/procesu .
        
    - Należy to zrobić w następnym sprincie .
        
    - W pierwszej kolejności należy skupić się na wydzieleniu usługi, która zapewni poprawne kolejkowanie i nie będzie psuć blockchaina. Funkcjonalność powiadomień dynamicznych zostaje na razie ograniczona .
        
    - Marek ma zdobyć akceptację kosztów (utrzymania) dla tego rozwiązania. Koszty początkowo wydają się bliskie zeru .
        
- **Zadania:**
    
    - **Marek Dziakowski:** Przygotowanie i zaimplementowanie wydzielenia funkcji dodawania do blockchaina do oddzielnego serwisu w następnym sprincie .
        
    - **Marek Dziakowski:** Uzyskanie akceptacji kosztów wdrożenia i utrzymania rozwiązania .
        

---

#### 2. Metodyka wdrażania i zarządzania mikroserwisami (Docker/Azure)

- **Ryzyko:**
    
    - Nie dotyczy, sekcja dotyczyła demonstracji Mateusza jako przykładu dobrej praktyki .
        
- **Proponowane rozwiązanie:**
    
    - Użycie konteneryzacji (Docker) do budowania usług (np. usług AI)1616161616.
        
    - Do uruchamiania lokalnie lub na serwerze klienta on-premises wystarczy skopiowanie pliku `docker-compose` i uruchomienie go jednym poleceniem, co upraszcza wdrożenie .
        
    - Aktualizacja (update) usługi sprowadza się do zaktualizowania obrazu, który Docker automatycznie pobiera .
        
    - W chmurze (Azure) wykorzystanie zasobu typu Container Instance/Register, do którego obrazy są łatwo wgrywane i zarządzane .
        
    - Kluczowa zaleta wdrożenia w Azure: automatyczne aktualizacje bez przestojów. Stara instancja obsługuje requesty, dopóki nowa się uruchamia, a następnie płynnie przełącza ruch. Brak przestoju jest dużą zaletą .
        
    - Możliwość automatycznego skalowania serwera (auto-scaling) na podstawie obciążenia poprzez ustawienie minimalnej i maksymalnej liczby replik (np. od 1 do 10)21.
        
    - Dane są przechowywane w bazie danych, a nie w samym kontenerze Docker, co zapewnia trwałość danych podczas aktualizacji (należy tego pilnować w kodzie) .
        
    - Prosta konfiguracja HTTPS za pomocą mechanizmu Ingress na Azure23.
        
    - Konfiguracja serwisów odbywa się poprzez zmienne środowiskowe, a poufne dane (np. connection stringi) można przechowywać za pomocą referencji do Secret's24242424.
        
    - Możliwość zarządzania wersjonowaniem poprzez tagi obrazów w rejestrze Docker .
        
    - Adrian zasugerował rozważenie Kubernetes (Kubernetes Service) dla bardziej dojrzałego rozwiązania produkcyjnego, ale Mateusz uważa, że Docker na razie jest wystarczający .
        
- **Decyzja:**
    
    - Nie padła formalna decyzja, sekcja miała charakter demonstracyjny/inspiracyjny dla problemu TrustCenter .
        
- **Zadania:**
    
    - Puste
        

---

#### 3. Modyfikacja systemowych źródeł danych (Raportowanie)

- **Ryzyko:**
    
    - Nie dotyczy, to jest zmiana mająca na celu usprawnienie.
        
- **Proponowane rozwiązanie:**
    
    - Zmiana źródeł systemowych (głównie w module raportowym) w taki sposób, aby miały dodatnie identyfikatory oraz unikalne GUIDy .
        
    - Obecne źródła z ujemnymi identyfikatorami pozostaną, a nowe (z dodatnimi identyfikatorami i GUID) będą sukcesywnie je zastępować .
        
    - Zmiany będą wymagały pracy głównie po stronie backendu (dostosowanie pobierania źródeł) .
        
    - GUIDy będą wykorzystywane do synchronizacji i przenoszenia definicji między środowiskami (testowe/docelowe), umożliwiając eksport/import źródeł i dashboardów .
        
    - Wszystkie źródła i dashboardy (nie tylko systemowe) będą miały generowane GUIDy na wszelki wypadek .
        
- **Decyzja:**
    
    - Przygotowanie źródeł systemowych w taki sposób, aby posiadały dodatnie identyfikatory i GUIDy .
        
    - Wszelkie miejsca odwołujące się do źródeł danych systemowych (obecnie po ujemnych indeksach) będą musiały zostać zmienione, aby obsługiwać dodatnie indeksy.
        
    - Wprowadzenie dwóch nowych kolumn w bazie: `czy jest systemowe źródło` oraz `jaki ma guid`.
        
- **Zadania:**
    
    - **Anna Skupińska:** Wprowadzenie zmian w tabelach: dodanie dwóch nowych kolumn (GUID, czy jest systemowe) i generowanie GUID dla wszystkich źródeł i dashboardów .
        
    - **Łukasz Bott / Zespół:** Wprowadzenie zmian w kodzie backendu w miejscach odwołujących się do źródeł systemowych, tak by obsługiwały dodatnie identyfikatory/GUID .
        
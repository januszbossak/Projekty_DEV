
Data: 28 października 2025 1

Temat: Specyfikacja funkcjonalna nowego modułu: Repozytorium Plików (DMS)

[[Projekty/Moduly/Repozytorium-plikow-DMS/README|Repozytorium-plikow-DMS]]

---

### **1. Omówione i uzgodnione funkcjonalności**

Zidentyfikowane w trakcie spotkania funkcjonalności nie dotyczą bezpośrednio komponentów Edytora Procesów (Diagramu, Formularza, Reguł), lecz definiują nowy, odrębny moduł Repozytorium Plików.

#### **Funkcjonalność: Struktura i Nomenklatura Repozytorium**

- **Komponent:** Repozytorium Plików (Nowy Moduł)
    
- **Cel:** Zdefiniowanie hierarchii i nazewnictwa dla nowej funkcjonalności.
    
- **Problem do rozwiązania:** Potrzeba stworzenia logicznej struktury oraz uniknięcie konfliktu nazw z istniejącą funkcjonalnością "obszarów" w systemie AMODIT2.
    
- **Sposób realizacji / Decyzja:**
    
    - Najwyższy poziom organizacji w repozytorium będzie nosił nazwę **"Przestrzenie"**.
        
    - Będzie można definiować dowolną liczbę przestrzeni4.
        
    - Każda przestrzeń może zawierać foldery i pliki .
        
    - System będzie wspierał zagnieżdżanie folderów .
        

#### **Funkcjonalność: System Uprawnień (Dziedziczenie i Przerywanie)**

- **Komponent:** Repozytorium Plików (Nowy Moduł)
    
- **Cel:** Stworzenie elastycznego systemu zarządzania dostępem do folderów i plików.
    
- **Sposób realizacji / Decyzja:**
    
    - System uprawnień będzie oparty na **dziedziczeniu** (Przestrzeń -> Folder -> Podfolder -> Plik).
        
    - Będzie istniała możliwość **przerwania dziedziczenia** na dowolnym poziomie (folderu lub pliku).
        
    - Przerwanie dziedziczenia będzie wyraźnie sygnalizowane wizualnie (specjalna ikona) zarówno na poziomie drzewka, jak i listy folderów .
        
    - Uprawnienia będzie można nadawać użytkownikom oraz grupom10.
        

#### **Funkcjonalność: Uprawnienia Wynikowe (Widoczność Folderu)**

- **Komponent:** Repozytorium Plików (Nowy Moduł)
    
- **Cel:** Umożliwienie użytkownikowi dostępu do głęboko zagnieżdżonego pliku bez konieczności nadawania mu pełnych uprawnień do folderów nadrzędnych.
    
- **Problem do rozwiązania:** Użytkownik musi widzieć ścieżkę do pliku, nawet jeśli ma uprawnienia tylko do tego jednego pliku.
    
- **Sposób realizacji / Decyzja:**
    
    - Użytkownik, który otrzyma dostęp (np. odczyt) do konkretnego pliku, automatycznie otrzyma **"Widoczność folderu"** dla wszystkich folderów nadrzędnych w ścieżce .
        
    - "Widoczność folderu" jest uprawnieniem **wynikowym** (tylko do odczytu w panelu uprawnień), a nie uprawnieniem, które można nadać ręcznie .
        

#### **Funkcjonalność: Przechowywanie Plików (Backend)**

- **Komponent:** Rdzeń Systemu / Konfiguracja
    
- **Cel:** Określenie fizycznej lokalizacji plików repozytorium.
    
- **Problem do rozwiązania:** Przechowywanie dużych ilości plików w bazie danych jest niewydajne.
    
- **Sposób realizacji / Decyzja:**
    
    - Pliki **nie będą** przechowywane w bazie danych .
        
    - Pliki będą przechowywane na zasobach sieciowych (lokalnie) .
        
    - Lokalizacja będzie spójna z mechanizmem przechowywania załączników (np. w dedykowanym podfolderze `RepozytoriowFajl` w ramach istniejącego folderu załączników) .
        

#### **Funkcjonalność: Fizyczna Struktura Katalogów na Dysku**

- **Komponent:** Rdzeń Systemu / Backend
    
- **Cel:** Ominięcie ograniczeń systemu Windows dotyczących maksymalnej długości ścieżki pliku.
    
- **Problem do rozwiązania:** Głęboko zagnieżdżone foldery o długich nazwach mogą przekroczyć limit długości ścieżki (ok. 260 znaków) .
    
- **Sposób realizacji / Decyzja:**
    
    - Fizyczna struktura folderów na dysku **będzie oparta na identyfikatorach (ID)** przestrzeni i folderów, a nie na ich nazwach.
        
    - Przykładowa ścieżka: `.../Repo/ID_przestrzeni/ID_folderu/ID_podfolderu/`.
        
    - Identyfikator lokalizacji będzie widoczny w adresie URL aplikacji, co ułatwi debugowanie .
        

#### **Funkcjonalność: Interfejs Użytkownika (UI)**

- **Komponent:** Repozytorium Plików (Nowy Moduł)
    
- **Cel:** Zapewnienie podstawowej nawigacji i interakcji z repozytorium.
    
- **Sposób realizacji / Decyzja:**
    
    - Interfejs będzie składał się z widoku drzewa folderów po lewej stronie i głównego obszaru z zawartością wybranego folderu po prawej .
        
    - Dostępne będą dwa tryby widoku zawartości: kafelkowy i lista .
        
    - Podgląd plików będzie realizowany przy użyciu istniejącego komponentu (analogicznie do podglądu w raportach) .
        

#### **Funkcjonalność: Wyszukiwanie**

- **Komponent:** Repozytorium Plików / Wyszukiwarka Globalna
    
- **Cel:** Umożliwienie odnalezienia plików w repozytorium.
    
- **Sposób realizacji / Decyzja:**
    
    - Zostanie zaimplementowane wyszukiwanie pełnotekstowe .
        
    - Mechanizm wyszukiwania musi uwzględniać i filtrować wyniki na podstawie uprawnień użytkownika do poszczególnych plików .
        

#### **Funkcjonalność: Kosz**

- **Komponent:** Repozytorium Plików (Nowy Moduł)
    
- **Cel:** Zabezpieczenie przed niezamierzoną utratą danych.
    
- **Sposób realizacji / Decyzja:**
    
    - Zostanie zaimplementowana funkcjonalność "Kosza" .
        
    - Usunięcie pliku będzie oznaczało jego oznaczenie jako "usunięty" i przeniesienie do kosza, a nie natychmiastowe fizyczne usunięcie .
        

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Podstawowa funkcjonalność Repozytorium Plików**

- **Cel:** Uruchomienie minimalnej, ale w pełni funkcjonalnej wersji repozytorium.
    
- **Zakres:**
    
    - Implementacja struktury "Przestrzeni", folderów i plików .
        
    - Podstawowe operacje CRUD na plikach i folderach (z sugestią, aby zwykły użytkownik mógł usuwać tylko własne pliki) .
        
    - Pełny mechanizm uprawnień (dziedziczenie, przerywanie dziedziczenia, uprawnienia wynikowe) .
        
    - Implementacja backendu: przechowywanie plików na zasobach sieciowych (poza DB) w strukturze opartej na ID .
        
    - Podstawowy interfejs użytkownika (drzewo, lista/kafle, podgląd plików) .
        
    - Implementacja Kosza (jako oznaczanie do usunięcia) .
        
    - Implementacja wyszukiwania pełnotekstowego z uwzględnieniem uprawnień .
        
    - Przechowywanie w bazie wyłącznie metadanych technicznych (ID, struktura, uprawnienia) .
        

#### **Poza zakresem MVP (Do realizacji w przyszłości)**

- **Cel:** Rozbudowa repozytorium o zaawansowane funkcje zarządcze i ułatwiające pracę.
    
- **Zakres:**
    
    - Możliwość definiowania przez użytkownika metadanych (np. opis, daty obowiązywania) .
        
    - Etykiety / Tagi .
        
    - Przenoszenie plików i folderów .
        
    - Wersjonowanie plików i szczegółowa historia zmian .
        
    - Powiadomienia .
        
    - Mechanizm okresowego czyszczenia kosza (np. automatyczne usuwanie plików starszych niż 30 dni) .
        
    - Eksport / Import struktury folderów .
        
    - Generowanie linków publicznych do plików .
        

---

### **3. Punkty do dalszej dyskusji (Otwarte / Do ustalenia)**

- **Strategia:** Ostateczne potwierdzenie, czy repozytorium ma być odrębnym bytem systemowym .
    
- **Struktura:** Ustalenie maksymalnej dozwolonej głębokości zagnieżdżenia folderów.
    
- **Uprawnienia:**
    
    - Precyzyjne zdefiniowanie podstawowych typów uprawnień (co dokładnie oznaczają "zapis", "modyfikacja", "usuwanie") .
        
    - Rozważenie rozdzielenia uprawnienia "dodawanie" od "usuwanie" .
        
- **Migracja:** Opracowanie strategii migracji plików z bazy danych do zasobów sieciowych dla istniejących klientów on-premise, którzy chcieliby wdrożyć repozytorium .
    
- **Backend:** Sposób zapisu uprawnień w bazie danych (sugestia: struktura JSON).
    
- **Logi:** Ustalenie zakresu logowania operacji na plikach (Kto, kiedy, jaka operacja?).
    
- **Ograniczenia:**
    
    - Ustalenie limitu rozmiaru dla pojedynczego przesyłanego pliku (sugestia: spójnie z obecnymi limitami, np. 2 GB).
        
    - Definicja listy dozwolonych i blokowanych typów plików (sugestia: spójnie z załącznikami w sprawach).
        
- **Wydajność:** Analiza ryzyka wydajnościowego i bezpieczeństwa związanego z wyszukiwaniem pełnotekstowym w bardzo dużych plikach (np. czy wymagany będzie osobny job).
    
- **Bezpieczeństwo:** Potwierdzenie konieczności implementacji szyfrowania plików przechowywanych na zasobach sieciowych .
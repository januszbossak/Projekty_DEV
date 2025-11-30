

**Data:** 13 listopada 2025 

**Temat:** Status prac nad nowymi edytorami (Diagramu i Formularza), definicja MVP i ustalenia roadmapy do końca roku.

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Nowy interfejs graficzny (Edytor Diagramu)**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Dostarczenie nowoczesnego narzędzia do wizualnego projektowania procesów (dodawanie etapów, rysowanie połączeń).
    
- **Problem do rozwiązania:** Stary edytor graficzny był rzadko używany i przestarzały wizualnie; potrzeba poprawy UX i wprowadzenia animacji.
    
- **Sposób realizacji / Decyzja:** Wdrożenie wersji w trybie "Beta". Edytor umożliwia rysowanie etapów i ścieżek. Konieczne dodanie przełącznika (toggle) umożliwiającego powrót do starej wersji edytora w razie problemów.
    

#### **Funkcjonalność: Definiowanie ścieżek i reguł przejścia**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Umożliwienie łączenia etapów i definiowania logiki przejść bezpośrednio na diagramie.
    
- **Problem do rozwiązania:** Brak zintegrowanego edytora logiki (reguł) w nowym widoku graficznym.
    
- **Sposób realizacji / Decyzja:** W obecnym MVP możliwe jest dodanie połączenia (ścieżki) lub jego usunięcie. Domyślnie tworzone jest proste przekazanie. Edycja samej reguły (skryptu/logiki) pozostaje w starym interfejsie.
    

#### **Funkcjonalność: Lista pól formularza**

- **Komponent:** Edytor Formularza
    
- **Cel:** Zapewnienie pełnej funkcjonalności zarządzania polami na formularzu.
    
- **Problem do rozwiązania:** Braki funkcjonalne względem starego UI oraz występujące błędy.
    
- **Sposób realizacji / Decyzja:** Prace koncentrują się na naprawie błędów (bugfixing) i wyrównaniu funkcjonalności do starej wersji (parity), a nie na wdrażaniu nowości.
    

#### **Funkcjonalność: Prawy panel konfiguracyjny**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Zaawansowana konfiguracja obiektów diagramu z poziomu bocznego panelu.
    
- **Problem do rozwiązania:** Ograniczone zasoby czasowe w bieżącym sprincie.
    
- **Sposób realizacji / Decyzja:** Temat świadomie odłożony na dalszy plan (kolejne sprinty).
    

#### **Funkcjonalność: Wizualizacja diagramu na Sprawie**

- **Komponent:** Edytor Diagramu (Widok użytkownika końcowego)
    
- **Cel:** Spójność wizualna między edytorem a podglądem procesu na konkretnej sprawie.
    
- **Problem do rozwiązania:** Ryzyko destabilizacji widoku sprawy przy wdrażaniu zmian w edytorze.
    
- **Sposób realizacji / Decyzja:** Nowy wygląd dotyczy wyłącznie Edytora Procesów. Widok diagramu na formularzu sprawy (runtime) pozostaje bez zmian (stary wygląd).
    

#### **Funkcjonalność: Lista Reguł**

- **Komponent:** Edytor Reguł
    
- **Cel:** Nowy interfejs zarządzania listą reguł biznesowych.
    
- **Problem do rozwiązania:** Konieczność priorytetyzacji kluczowych komponentów wizualnych.
    
- **Sposób realizacji / Decyzja:** Prace nad tym komponentem nie są obecnie prowadzone (nie dotykane w bieżącym zakresie).
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Stabilizacja na koniec roku (Wdrożenie WIM/LOT)**

- **Cel:** Wydanie stabilnej paczki umożliwiającej odbiory projektowe (WIM, LOT) przed końcem roku.
    
- **Zakres:**
    
    - Nowy Edytor Diagramu (wersja Beta z przełącznikiem na stary widok).
        
    - Podstawowe operacje na diagramie (dodawanie etapów, łączenie ścieżek).
        
    - Edytor Formularza (poprawki błędów i uzupełnienie braków funkcjonalnych).
        
    - Naprawa błędów krytycznych (stabilność).
        

#### **MVP 2: Rozwój i UX (Roadmapa na przyszły rok)**

- **Cel:** Rozszerzenie możliwości edytorów i poprawa użyteczności.
    
- **Zakres:**
    
    - Implementacja prawego panelu konfiguracyjnego w Edytorze Diagramu.
        
    - Dodanie edytora reguł (skryptów) bezpośrednio przy ścieżkach na diagramie.
        
    - Prace nad Listą Reguł.
        
    - Aktualizacja widoku diagramu na formularzu sprawy.
        

---

### **3. Punkty do dalszej dyskusji i inne wątki projektowe**

- **Projekt WIM:** Priorytet absolutny – musi zostać odebrany przed końcem roku.
    
- **Projekt LOT:** Moduł do zrobienia, wymaga wsparcia (Piotr).
    
- **Integracja Szafir (macOS):** Nadal występują problemy z działaniem podpisu, temat otwarty.
    
- **Komunikator:** Zainstalowany w ZIM, wymaga drobnych poprawek (błąd wyskakujący w jednym momencie), ale jest funkcjonalny. Prezentacja zaplanowana na dzień po spotkaniu.
    
- **Repozytorium:** Największy moduł do zrealizowania w najbliższym czasie.
    
- **Weryfikacja:** Po wydaniu wersji stabilnej planowane testy "znęcania się" nad systemem na środowisku Astrafox.
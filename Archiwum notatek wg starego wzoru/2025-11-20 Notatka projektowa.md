

Data: 2025-11-20

Temat: Finalizacja prac nad Edytorami (Formularza, Diagramu) oraz status migracji Ustawień Systemowych

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Standardyzacja interfejsu użytkownika (Marginesy/Padding)**

- **Komponent:** Edytor Diagramu / Edytor Formularza
    
- **Cel:** Zapewnienie spójności wizualnej interfejsu (UI) w całym systemie oraz ułatwienie przyszłych modyfikacji.
    
- **Problem do rozwiązania:** Niespójność w kodzie tworzonym przez różnych deweloperów (np. stosowanie marginesów 5px vs 8px), co utrudnia globalne zarządzanie wyglądem.
    
- **Sposób realizacji / Decyzja:** Wdrożenie centralnej definicji stylów (rozwiązanie systemowe oparte o CSS), aby zmiana parametru w jednym miejscu aktualizowała wygląd w całym systemie. Odejście od sztywnego wpisywania wartości w poszczególnych widokach.
    

#### **Funkcjonalność: Ustawienia Systemowe i Logi**

- **Komponent:** Konfiguracja Systemu (Ustawienia)
    
- **Cel:** Całkowita migracja ustawień i logów do nowej technologii/widoków.
    
- **Problem do rozwiązania:** Potrzeba zamknięcia etapu migracji (MVP) i wyeliminowania zależności od starych widoków.
    
- **Sposób realizacji / Decyzja:** Potwierdzono 100% przeniesienie Ustawień oraz Logów systemowych. Decyzja o wyłączeniu komunikatu/ostrzeżenia o przełączaniu się do widoków niejawnych (starych), przy zachowaniu samej możliwości przełączenia "z oporem".
    

#### **Funkcjonalność: Finalizacja Edytora Formularza**

- **Komponent:** Edytor Formularza
    
- **Cel:** Całkowite ukończenie prac nad edytorem w ramach obecnego zakresu MVP.
    
- **Problem do rozwiązania:** Istnienie otwartych zadań i brak formalnego zamknięcia prac nad modułem.
    
- **Sposób realizacji / Decyzja:** Skupienie prac (w perspektywie 1-2 sprintów) na domknięciu wszystkich otwartych tematów, aby ogłosić moduł jako w 100% gotowy zgodnie z założeniami.
    

#### **Funkcjonalność: Prace nad Edytorem Diagramu**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Poprawa architektury i użyteczności edytora.
    
- **Problem do rozwiązania:** Konieczność wykonania "kosmetyki" oraz prac refaktoringowych (wydzielenie elementów do kontenerów).
    
- **Sposób realizacji / Decyzja:** Utrzymanie statusu "do dokończenia". Prace mają obejmować wspomnianą kosmetykę i zmiany w kontenerach. Jest to priorytet po/w trakcie zamykania Edytora Formularza.
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Zamknięcie prac nad Edytorami i Ustawieniami (Obecny Priorytet)**

- **Cel:** Realizacja zasady "przestań zaczynać, zacznij kończyć". Dostarczenie stabilnych i kompletnych wersji kluczowych edytorów.
    
- **Zakres:**
    
    - **Edytor Formularza:** Finalizacja 100% funkcjonalności (1-2 sprinty).
        
    - **Edytor Diagramu:** Wdrożenie zmian kosmetycznych i kontenerowych.
        
    - **Ustawienia Systemowe:** Oficjalne zamknięcie migracji, usunięcie komunikatów o starych widokach.
        

#### **MVP 2: Rozwój Q1 (Future Scope)**

- **Cel:** Rozbudowa systemu o brakujące elementy logiki i konfiguracji procesów.
    
- **Zakres:**
    
    - **Edytor Reguł:** Prace deweloperskie i finalizacja (obecnie zidentyfikowane jako obszar do zrobienia).
        
    - **Ustawienia procesu:** Migracja ustawień procesu ze starej technologii.
        

---

### **3. Punkty do dalszej dyskusji (Otwarte)**

- **Moduł Raportowy:** Brak zgody co do priorytetu naprawy. Jeden z interesariuszy naciska na natychmiastową naprawę błędów krytycznych ("moduł nie działa"), drugi proponuje przesunięcie prac na kolejny kwartał na rzecz domknięcia Edytorów. Temat wymaga osobnego spotkania decyzyjnego.
    
- **Dalszy rozwój Integracji/Wiki:** Temat uznany za obecny w systemie, ale z potencjałem do dalszego rozwoju (nieblokujący dla MVP 1).
    

---

### **Chcesz, abym na podstawie tej notatki przygotował listę zadań w JIRA dla zespołu deweloperskiego?**



Data: 6 listopada 2025

Temat: Usprawnienia UX/UI w Edytorze Formularza oraz priorytetyzacja prac naprawczych

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Wizualizacja aktywności ustawień pól**

- **Komponent:** Edytor Formularza
    
- **Cel:** Zwiększenie czytelności konfiguracji pól poprzez jednoznaczną sygnalizację aktywnych parametrów.
    
- **Problem do rozwiązania:** Użytkownik nie widzi na pierwszy rzut oka, które ustawienia (np. widoczność, wymagalność, uprawnienia) zostały zmodyfikowane lub są aktywne ("w offie" vs "ustawione").
    
- **Sposób realizacji / Decyzja:** Wprowadzenie stałego wyróżnienia wizualnego (podświetlenia/ikony), które pozostaje aktywne ("świeci cały czas"), gdy dana funkcja lub ustawienie dla pola jest włączone. Dotyczy to m.in. sekcji uprawnień i widoczności.
    

#### **Funkcjonalność: Prezentacja typu pola w panelu konfiguracyjnym**

- **Komponent:** Edytor Formularza
    
- **Cel:** Ujednolicenie interfejsu i eliminacja pomyłek wynikających z nazewnictwa pól.
    
- **Problem do rozwiązania:** Obecna prezentacja typu pola w nagłówku (Header) prawego panelu jest nieczytelna, zwłaszcza gdy nazwa pola jest tożsama z nazwą typu (np. pole "Kwota" o typie "Kwota"). Użytkownicy (szczególnie nowi) mają trudność z rozróżnieniem nazwy własnej pola od jego definicji systemowej.
    
- **Sposób realizacji / Decyzja:**
    
    1. Przeniesienie informacji o typie pola z nagłówka do sekcji "Dane podstawowe".
        
    2. Dodanie etykiety "Typ:" przed nazwą typu.
        
    3. Dodanie ikony reprezentującej typ pola (spójnej z ikonami w lewym panelu/toolboxie) w celu szybszej identyfikacji wizualnej.
        

#### **Funkcjonalność: Konfiguracja precyzji pól liczbowych**

- **Komponent:** Edytor Formularza
    
- **Cel:** Wyjaśnienie logiki dostępności ustawień miejsc po przecinku.
    
- **Problem do rozwiązania:** Zgłoszone braki w ustawieniach zaokrągleń/miejsc po przecinku dla pola typu "Kwota".
    
- **Sposób realizacji / Decyzja:** Potwierdzono logikę systemową: ustawienia liczby miejsc po przecinku są dostępne dla typu pola "Numeryczne". Typ "Kwota" posiada standardowe formatowanie walutowe i nie wymaga tej konfiguracji w tym samym zakresie. Należy weryfikować typ pola przed zgłaszaniem błędu (rozróżnienie nazwy "Numeryczna 1" od faktycznego typu "Kwota").
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Stabilizacja Raportowania (Najwyższy Priorytet)**

- **Cel:** Usunięcie krytycznych błędów blokujących pracę z raportami.
    
- **Zakres:**
    
    - Rozwiązywanie błędów na poziomie modułu raportów (poza zakresem dzisiejszej dyskusji o funkcjonalnościach, ale wskazane jako priorytet nad Edytorem Diagramu i Reguł).
        

#### **MVP 2: Usprawnienia UX Edytora Formularza**

- **Cel:** Poprawa czytelności i ergonomii pracy konfiguratora pól.
    
- **Zakres:**
    
    - Wizualizacja aktywności ustawień pól (highlight aktywnych opcji).
        
    - Przeniesienie informacji o typie pola do sekcji "Dane podstawowe".
        
    - Implementacja ikonografii typów pól w panelu właściwości.
        

---

### **Punkty do dalszej dyskusji**

- **Wstrzymanie prac nad Edytorem Diagramu i Reguł:** Prace projektowe i implementacyjne nad tymi modułami zostały tymczasowo wstrzymane (mimo zaprojektowania reguł) ze względu na konieczność alokacji zasobów do naprawy błędów w raportach. Należy ustalić termin powrotu do tych zadań.
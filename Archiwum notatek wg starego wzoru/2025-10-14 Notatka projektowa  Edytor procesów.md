**Temat:** Rozwój funkcjonalności Edytora Procesów oraz priorytetyzacja zgłoszeń klientów

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Wizualizacja zależności między obiektami procesu**

- **Komponent:** Edytor Procesów (integrujący Edytor Reguł, Edytor Formularza i Edytor Diagramu)
    
- **Cel:** Zwiększenie ergonomii pracy analityka poprzez automatyczne wskazywanie powiązań logicznych między elementami procesu.
    
- **Problem do rozwiązania:** Obecnie edytory (pól, etapów, reguł) są odseparowane. Użytkownik będąc na polu formularza lub etapie nie widzi informacji, czy i jakie reguły modyfikują ten obiekt. System posiada wiedzę o tych relacjach (backend), ale nie prezentuje ich w interfejsie, co wymusza ręczną weryfikację zależności.
    
- **Sposób realizacji / Decyzja:** Funkcjonalność zakłada konsolidację obszarów tworzenia procesu. System ma wyświetlać relacje krzyżowe, np. edytując regułę, system wskaże użyte pola i etapy; będąc na diagramie, system wskaże reguły podpięte pod dany etap.
    

#### **Funkcjonalność: Przełącznik wyboru języka interfejsu**

- **Komponent:** Interfejs Użytkownika (powiązany z prezentacją w Edytorze Formularza)
    
- **Cel:** Optymalizacja przestrzeni roboczej interfejsu (nagłówka).
    
- **Problem do rozwiązania:** Użytkownicy (feedback: Aleksandra Rosińska) zgłaszają brak szybkiego przełącznika języka na głównym ekranie. Wcześniejsza wersja pozwalała na zmianę języka jednym kliknięciem.
    
- **Sposób realizacji / Decyzja:** Utrzymanie obecnego rozwiązania. Opcja wyboru języka pozostaje ukryta w **Ustawieniach Konta** użytkownika, aby nie obciążać głównego interfejsu (założenie: język zmienia się raz, a nie codziennie). Zmiana możliwa tylko w przypadku krytycznego blokera po stronie klienta.
    

#### **Funkcjonalność: Customizacja stylów wizualnych (Kolorystyka/CSS)**

- **Komponent:** Edytor Formularza (warstwa prezentacji)
    
- **Cel:** Obsługa specyficznych wymagań wizualnych klientów (np. Neuca) przy migracji do nowej wersji.
    
- **Problem do rozwiązania:** Klienci zgłaszają zmiany w domyślnej kolorystyce nowego interfejsu jako błędy lub regresję.
    
- **Sposób realizacji / Decyzja:** Zmiany domyślnego wyglądu systemu (standardowe style) nie będą cofane w ramach gwarancji/błędów. Przywrócenie starej kolorystyki lub specyficzny branding jest możliwe wyłącznie jako płatna usługa (Custom CSS).
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Podstawowy Edytor Procesów**

- **Cel:** Dostarczenie działającego narzędzia do budowy procesów (obecny zakres prac).
    
- **Zakres:**
    
    - Funkcjonalne edytory (Diagramu, Formularza, Reguł) działające niezależnie.
        
    - Standardowy interfejs użytkownika (bez dedykowanych switchy językowych w nagłówku).
        

#### **MVP 2: Konsolidacja i Wizualizacja Relacji**

- **Cel:** Znacząca poprawa User Experience i szybkości projektowania procesów.
    
- **Zakres:**
    
    - Implementacja funkcjonalności: **Wizualizacja zależności między obiektami procesu**.
        
    - Integracja widoków Edytora Reguł z Edytorem Formularza i Diagramu (wyświetlanie powiązań logicznych w kontekście edytowanego obiektu).
        

---

### **3. Punkty do dalszej dyskusji**

- **Szczegółowa analiza UX Edytora Formularza:** Wymagane osobne spotkanie w celu omówienia praktycznych uwag po pierwszych testach wewnętrznych (Planowane spotkanie: godz. 15:15).
    
- **Metodyka zbierania wymagań:** Potwierdzenie procesu walidacji prototypów z klientami wewnętrznymi przed skierowaniem funkcjonalności do implementacji.
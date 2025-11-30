
[[2025-11-20 Notatka projektowa]] [[2025-10-09 czwartek]]
### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Poprawa mechanizmu "przeciągnij i upuść" (Drag-and-Drop) pól**

- **Komponent:** Edytor Formularza
    
- **Cel:** Zapewnienie intuicyjnego i przewidywalnego rozmieszczania pól na formularzu.
    
- **Problem do rozwiązania:** Podczas przeciągania pola w docelowe miejsce (np. środkowa kolumna), pole jest błędnie umieszczane w pierwszej kolumnie i może stać się niedostępne. Obecny wizualny wskaźnik miejsca upuszczenia (np. "belka z plusem") jest mylący i nie odzwierciedla struktury kolumn.
    
- **Sposób realizacji / Decyzja:** Należy poprawić logikę upuszczania pól, aby trafiały dokładnie w wybrane przez użytkownika miejsce (kolumnę). Wizualny wskaźnik miejsca upuszczenia (drop target) musi zostać zmieniony, aby realnie odzwierciedlał docelową strukturę (np. pokazywał układ kolumn).
    

#### **Funkcjonalność: Implementacja prawego panelu właściwości**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Umożliwienie konfiguracji etapów, akcji i reguł bezpośrednio z poziomu edytora wizualnego.
    
- **Problem do rozwiązania:** Brak zaimplementowanego panelu bocznego do zarządzania właściwościami i regułami zaznaczonych elementów diagramu.
    
- **Sposób realizacji / Decyzja:** Zaprojektowanie i wdrożenie prawego panelu bocznego jest priorytetem. Panel ten musi obsługiwać wyświetlanie i edycję właściwości oraz powiązanych reguł dla wybranego elementu.
    

#### **Funkcjonalność: Ujednolicenie kolorystyki interfejsu (odcienie szarości)**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Zapewnienie spójności wizualnej edytora z resztą systemu AMODIT.
    
- **Problem do rozwiązania:** Obecnie używany kolor szary (np. tło, nieaktywne elementy) jest zbyt ciemny i niespójny z paletą systemu.
    
- **Sposób realizacji / Decyzja:** Należy zastąpić obecny ciemny odcień szarości jaśniejszym, standardowym odcieniem szarości już używanym w systemie AMODIT (np. pobranym z nagłówków sekcji lub innych stałych elementów interfejsu).
    

#### **Funkcjonalność: Wyróżnianie aktywnego etapu na diagramie**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Wyraźne wskazanie użytkownikowi, który etap jest aktualnie wybrany do edycji.
    
- **Problem do rozwiązania:** Potrzeba zdefiniowania sposobu wizualnego wyróżnienia aktywnego etapu.
    
- **Sposób realizacji / Decyzja:** Aktualnie wybrany (aktywny) etap na diagramie będzie podświetlany standardowym kolorem `primary` (głównym kolorem motywu), analogicznie do aktywnej pozycji w menu po lewej stronie.
    

#### **Funkcjonalność: Zmiana domyślnego wyglądu etapów Start / Koniec**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Poprawa czytelności diagramu, rezerwacja koloru `primary` tylko dla aktywnie wybranego elementu.
    
- **Problem do rozwiązania:** Etapy Start i Koniec są domyślnie wyświetlane w kolorze `primary`, co wprowadza w błąd (sugeruje, że są aktywne).
    
- **Sposób realizacji / Decyzja:** Należy usunąć domyślne podświetlenie kolorem `primary` dla etapów Start i Koniec. Etapy te mają być podświetlane (kolorem `primary`) dopiero po ich kliknięciu (wybraniu) w celu konfiguracji ich właściwości (np. uruchamianie z maila).
    

#### **Funkcjonalność: Wyróżnianie etapów powiązanych**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Wizualizacja powiązań między etapami podczas edycji.
    
- **Problem do rozwiązania:** Brak wizualnej informacji zwrotnej o docelowym etapie przy wyborze etapu źródłowego.
    
- **Sposób realizacji / Decyzja:** Po kliknięciu na etap, który ma przejście do innego etapu (np. do etapu "Koniec"), etap docelowy również powinien zostać wizualnie wyróżniony (np. ramką).
    

#### **Funkcjonalność: Ujednolicenie kolorystyki ikon/elementów wewnętrznych etapów**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Poprawa spójności wizualnej bloków etapów.
    
- **Problem do rozwiązania:** Niektóre elementy wewnątrz bloków etapów (np. ikony) mają niespójny kolor (np. pomarańczowy).
    
- **Sposób realizacji / Decyzja:** Kolorystyka wewnętrznych elementów (np. ikon) na diagramie ma zostać ujednolicona i wyrównana do standardowego koloru tekstu.
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Podstawowa funkcjonalność MVP dla konsultantów**

- **Cel:** Uruchomienie kluczowych, działających mechanizmów edytorów w celu przekazania MVP do testów/użytku przez konsultantów. Priorytetem jest funkcjonalność.
    
- **Zakres:**
    
    - Poprawa mechanizmu "przeciągnij i upuść" (Drag-and-Drop) pól
        
    - Implementacja prawego panelu właściwości
        

#### **MVP 2 (Faza 2): Usprawnienia interfejsu użytkownika (UI/UX)**

- **Cel:** Wdrożenie poprawek wizualnych i usprawnień użyteczności zidentyfikowanych podczas spotkania (do wdrożenia po dostarczeniu MVP 1).
    
- **Zakres:**
    
    - Ujednolicenie kolorystyki interfejsu (odcienie szarości)
        
    - Wyróżnianie aktywnego etapu na diagramie
        
    - Zmiana domyślnego wyglądu etapów Start / Koniec
        
    - Wyróżnianie etapów powiązanych
        
    - Ujednolicenie kolorystyki ikon/elementów wewnętrznych etapów
        

---
[[2025-11-20 Notatka projektowa]] [[2025-10-08 środa]]


# Usprawnienia interfejsu użytkownika i logiki w Edytorze Diagramu

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Kontekstowe menu dla połączeń na diagramie**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Ułatwienie zarządzania połączeniami i powiązanymi z nimi regułami bezpośrednio z poziomu diagramu.
    
- **Problem do rozwiązania:** Brak intuicyjnej i szybkiej metody usuwania połączeń lub dodawania do nich reguł. Obecny symbol "+" jest niejednoznaczny i nie oferuje wszystkich potrzebnych akcji.
    
- **Sposób realizacji / Decyzja:** Ikona "+" na połączeniach zostanie zastąpiona nowym przyciskiem. Po jego kliknięciu pojawi się belka narzędziowa z dwiema opcjami:
    
    1. **Usuń połączenie:** Umożliwi usunięcie wizualnej strzałki na diagramie.
        
    2. **Dodaj nową regułę:** Umożliwi zainicjowanie procesu tworzenia nowej reguły dla danego połączenia.
        

#### **Funkcjonalność: Poprawa procesu dodawania nowego etapu**

- **Komponent:** Edytor Diagramu
    
- **Cel:** Zapewnienie jednoznacznego i świadomego procesu dodawania etapów przez użytkownika, eliminując przypadkową utratę danych.
    
- **Problem do rozwiązania:** Obecnie dodawanie nowego etapu może zostać nieświadomie anulowane przez użytkownika poprzez kliknięcie w dowolne inne miejsce na kanwie diagramu. Powoduje to frustrację i utratę postępu pracy.
    
- **Sposób realizacji / Decyzja:** Proces dodawania nowego etapu zostanie zmieniony tak, aby wymagał od użytkownika jawnej akcji potwierdzenia lub rezygnacji. Przypadkowe kliknięcie poza obszarem dodawania etapu nie będzie już anulować tej operacji.
    

#### **Funkcjonalność: Logika usuwania reguł powiązanych z połączeniami**

- **Komponent:** Edytor Diagramu / Edytor Reguł
    
- **Cel:** Ustalenie bezpiecznego mechanizmu zarządzania regułami biznesowymi podczas modyfikacji wizualnej warstwy diagramu.
    
- **Problem do rozwiązania:** Usunięcie połączenia na diagramie, do którego jest podpięta logika biznesowa (reguła), mogłoby nieświadomie usunąć również tę logikę, co jest działaniem destrukcyjnym i potencjalnie nieodwracalnym.
    
- **Sposób realizacji / Decyzja:** Postanowiono, że na tym etapie usunięcie połączenia w Edytorze Diagramu **nie będzie** powodować automatycznego usunięcia powiązanej z nim reguły. Reguła pozostanie w systemie, a użytkownik będzie musiał ją usunąć ręcznie z poziomu listy reguł.
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Podstawowe usprawnienia użyteczności Edytora Diagramu**

- **Cel:** Wdrożenie kluczowych poprawek w interfejsie użytkownika, które znacząco poprawią komfort i efektywność pracy z diagramem procesów.
    
- **Zakres:**
    
    - Implementacja kontekstowego menu dla połączeń (zastąpienie "+").
        
    - Wdrożenie w pełni funkcjonalnego przycisku "Usuń połączenie".
        
    - Dodanie przycisku "Dodaj nową regułę" (na tym etapie może być to placeholder bez zaimplementowanej logiki).
        
    - Przeprojektowanie ścieżki dodawania nowego etapu w celu wymagania jawnego potwierdzenia lub anulowania przez użytkownika.
        
    - Zapewnienie, że usunięcie połączenia na diagramie nie usuwa powiązanej reguły.

[[2025-10-07 wtorek]] [[2025-11-20 Notatka projektowa]]
# Koncepcja zintegrowanego edytora procesów oraz usprawnienia w zarządzaniu polami i regułami

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Zintegrowany, kontekstowy edytor procesów**

- **Komponent:** Edytor Diagramu / Edytor Formularza
    
- **Cel:** Umożliwienie analitykom projektowania całego procesu (diagram, wygląd formularzy, uprawnienia pól, akcje) w jednym, spójnym interfejsie, bez konieczności przełączania się między oddzielnymi edytorami.
    
- **Problem do rozwiązania:** Obecne rozdzielenie edytorów diagramu, formularza i reguł utrudnia całościowe postrzeganie procesu. Analityk musi przełączać się między wieloma zakładkami, aby zrozumieć i skonfigurować, jak formularz i jego pola zachowują się na konkretnym etapie.
    
- **Sposób realizacji / Decyzja:** Zostanie stworzony nowy, zintegrowany tryb edycji. Głównym elementem interfejsu będzie diagram procesu. Kliknięcie na dany etap na diagramie (np. "Korekta") spowoduje dynamiczne załadowanie widoku formularza w kontekście tego etapu. W tym widoku możliwe będzie bezpośrednie konfigurowanie:
    
    - Widoczności i uprawnień dla poszczególnych pól.
        
    - Dostępnych akcji (przycisków).
        
    - Logiki związanej z danym etapem.
        

#### **Funkcjonalność: Wyświetlanie powiązanych reguł w kontekście pola formularza**

- **Komponent:** Edytor Formularza
    
- **Cel:** Zapewnienie analitykowi natychmiastowego dostępu do informacji o wszystkich regułach, które wykorzystują dane pole formularza.
    
- **Problem do rozwiązania:** Obecnie, aby sprawdzić, jaka logika biznesowa jest powiązana z konkretnym polem, analityk musi ręcznie przeszukiwać całą listę reguł. Jest to czasochłonne, nieefektywne i podatne na błędy, zwłaszcza w złożonych procesach.
    
- **Sposób realizacji / Decyzja:** W panelu właściwości pola w Edytorze Formularza zostanie dodana nowa sekcja (lub zakładka) o nazwie "Reguły". Będzie ona wyświetlać listę wszystkich reguł (zarówno automatycznych, jak i ręcznych), w których dane pole jest używane. Zapewni to szybki wgląd w zależności i logikę powiązaną z polem.
    

#### **Funkcjonalność: Przeprojektowanie widoku listy reguł**

- **Komponent:** Edytor Reguł
    
- **Cel:** Zwiększenie czytelności i użyteczności interfejsu do zarządzania listą reguł w procesie.
    
- **Problem do rozwiązania:** Obecny widok listy reguł nie jest wystarczająco przejrzysty i nie dostarcza kluczowych informacji w zwięzłej formie.
    
- **Sposób realizacji / Decyzja:** Lista reguł zostanie zaprezentowana w nowym widoku tabelarycznym. Minimalny zestaw kolumn będzie obejmował:
    
    - Nazwa reguły
        
    - Etap, na którym jest uruchamiana
        
    - Treść (lub jej fragment/podgląd)
        
        Akcje takie jak "Edytuj" i "Historia" będą dostępne bezpośrednio w wierszu danej reguły (np. jako ikony lub w menu kontekstowym), co upodobni interfejs do istniejących rozwiązań w raportach.
        

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Usprawnienia użyteczności istniejących edytorów**

- **Cel:** Szybkie dostarczenie wartości poprzez poprawę ergonomii i wydajności pracy analityka w obecnych komponentach systemu.
    
- **Zakres:**
    
    - Funkcjonalność: **Przeprojektowanie widoku listy reguł**
        
    - Funkcjonalność: **Wyświetlanie powiązanych reguł w kontekście pola formularza**
        

#### **MVP 2: Wdrożenie zintegrowanego edytora procesów**

- **Cel:** Wprowadzenie rewolucyjnej zmiany w sposobie projektowania procesów, łączącej diagram i formularz w jeden spójny, kontekstowy interfejs.
    
- **Zakres:**
    
    - Funkcjonalność: **Zintegrowany, kontekstowy edytor procesów**
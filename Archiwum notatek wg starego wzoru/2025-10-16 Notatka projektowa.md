[[2025-11-20 Notatka projektowa]] [[2025-10-16 czwartek]]

---

### **Notatka projektowa ze spotkania**

Data: 16 października 2025

Temat: Poprawki Edytora Formularza oraz kierunki rozwoju Edytora Diagramu i Ustawień Systemowych

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Poprawa mechanizmu "przeciągnij i upuść" (Drag-and-Drop) w Edytorze Formularza**

- **Komponent:** Edytor Formularza
    
- **Cel:** Umożliwienie konsultantom intuicyjnego budowania formularza poprzez przeciąganie pól, w tym dynamiczne tworzenie nowych wierszy.
    
- **Problem do rozwiązania:** Mechanizm "przeciągnij i upuść" nie pozwala obecnie na wstawienie pola _pomiędzy_ dwa istniejące wiersze. Wskaźnik wizualny (sugerujący miejsce upuszczenia) nie pojawia się podczas przeciągania pola nad przestrzeń międzywierszową.
    
- **Sposób realizacji / Decyzja:** Należy zmodyfikować mechanizm drag-and-drop. Wskaźnik miejsca upuszczenia musi pojawiać się również podczas przeciągania pola nad granicę między dwoma wierszami, a upuszczenie pola w tym miejscu musi skutkować utworzeniem nowego wiersza i wstawieniem tam tego pola.
    

#### **Funkcjonalność: Ukończenie implementacji nowej Listy Pól**

- **Komponent:** Edytor Formularza
    
- **Cel:** Zastąpienie przestarzałego widoku listy pól nowym, bardziej wydajnym i funkcjonalnym interfejsem.
    
- **Problem do rozwiązania:** W systemie nadal istnieje możliwość przełączenia się na stary edytor/widok listy pól. Nowa implementacja jest w trakcie realizacji.
    
- **Sposób realizacji / Decyzja:** Prace nad nową listą pól (realizowane przez Filipa) mają być kontynuowane. Docelowo nowa lista musi w pełni zastąpić starą funkcjonalność, która zostanie usunięta z systemu.
    

#### **Funkcjonalność: Zmiana wizualizacji dziedziczenia w Matrycy Uprawnień**

- **Komponent:** Edytor Formularza (dot. Matrycy Uprawnień)
    
- **Cel:** Poprawa czytelności interfejsu matrycy uprawnień.
    
- **Problem do rozwiązania:** Obecne wyświetlanie ikon dziedziczenia (łańcuszków) w każdym polu jest nadmiarowe i zaciemnia obraz ("trochę bez sensu").
    
- **Sposób realizacji / Decyzja:** Należy odwrócić logikę wizualizacji. Zamiast pokazywać łańcuszki wszędzie, system powinien domyślnie zakładać dziedziczenie, a wyświetlać specjalną ikonkę (np. przerwanego łańcuszka) tylko w tych miejscach, gdzie dziedziczenie zostało jawnie wyłączone przez użytkownika.
    

#### **Funkcjonalność: Docelowa implementacja Prawego Panelu Właściwości**

- **Komponent:** Edytor Diagramu / Edytor Reguł
    
- **Cel:** Umożliwienie konfiguracji etapów i logiki biznesowej (reguł) bezpośrednio z poziomu wizualnego edytora diagramu.
    
- **Problem do rozwiązania:** Brak możliwości edycji właściwości etapów i reguł z poziomu nowego edytora diagramu.
    
- **Sposób realizacji / Decyzja:** Kierunkowo ustalono, że po kliknięciu na etap na diagramie, musi pojawić się prawy panel boczny. Panel ten powinien wyświetlać właściwości etapu oraz listę powiązanych z nim reguł, a także umożliwiać ich edycję (integracja z Edytorem Reguł). Funkcjonalność jest obecnie w fazie projektowania.
    

#### **Funkcjonalność: Mechanizm "Four Eyes" (podwójnej akceptacji) dla Ustawień Systemowych**

- **Komponent:** (Poza Edytorem Procesów - Ustawienia Systemowe / Administracja)
    
- **Cel:** Zwiększenie bezpieczeństwa zmian konfiguracyjnych w systemie.
    
- **Problem do rozwiązania:** Krytyczne zmiany w ustawieniach systemowych mogą być obecnie wykonywane przez jednego administratora bez dodatkowej weryfikacji.
    
- **Sposób realizacji / Decyzja:** Zostanie zaimplementowany mechanizm "Four Eyes" (określony jako "Poraj"), który będzie wymagał potwierdzenia zmian w ustawieniach systemowych przez drugiego administratora.
    

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Ustabilizowanie i dokończenie Edytora Formularza**

- **Cel:** Dostarczenie w pełni funkcjonalnych i poprawionych kluczowych komponentów Edytora Formularza oraz zastąpienie starych elementów systemu.
    
- **Zakres:**
    
    - Poprawa mechanizmu "przeciągnij i upuść" (Drag-and-Drop) w Edytorze Formularza
        
    - Ukończenie implementacji nowej Listy Pól
        
    - Zmiana wizualizacji dziedziczenia w Matrycy Uprawnień
        

#### **MVP 2: Rozwój Edytora Diagramu i Ustawień Administracyjnych**

- **Cel:** Rozbudowa systemu o nowe, kluczowe funkcjonalności (zgodnie z fazą projektową).
    
- **Zakres:**
    
    - Docelowa implementacja Prawego Panelu Właściwości (w Edytorze Diagramu)
        
    - Mechanizm "Four Eyes" (w Ustawieniach Systemowych)
        

---
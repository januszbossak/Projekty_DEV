[[2025-09-09 wtorek]]



# Temat: Ustalenia dotyczące zarządzania integracjami oraz standaryzacja dokumentacji projektowej

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Ujednolicenie i reorganizacja sekcji zarządzania integracjami**

- **Komponent:** Interfejs Systemu (Ustawienia)
    
- **Cel:** Uporządkowanie i uproszczenie interfejsu do konfiguracji integracji systemowych i dedykowanych w AMODIT, aby był on bardziej intuicyjny dla użytkownika.
    
- **Problem do rozwiązania:** Obecny podział na osobne sekcje "Integracje" i "Rozszerzenia" jest mylący. Nazwa "Rozszerzenia" nie oddaje charakteru znajdujących się tam funkcji i wprowadza niejasność co do przeznaczenia.
    
- **Sposób realizacji / Decyzja:** Zostanie wdrożona jedna, wspólna zakładka o nazwie **"Integracje"**. Zakładka "Rozszerzenia" zostanie całkowicie usunięta. Wewnątrz ujednoliconej sekcji "Integracje" zostanie wprowadzony klarowny podział na dwie grupy:
    
    1. **Integracje systemowe:** Wbudowane, nieedytowalne.
        
    2. **Integracje definiowane:** Konfigurowalne przez użytkownika (dawne "customowe").
        

---

### **2. Decyzje organizacyjne i procesowe**

#### **Decyzja: Standaryzacja dokumentacji projektowej w Azure DevOps Wiki**

- **Cel:** Stworzenie centralnego, ustrukturyzowanego i łatwego w nawigacji źródła wiedzy dla każdego projektu i rozwijanej funkcjonalności.
    
- **Problem do rozwiązania:** Obecna dokumentacja jest rozproszona i nieustrukturyzowana ("ciężko się to czyta"), co utrudnia zrozumienie założeń projektu, jego historii oraz śledzenie ewolucji.
    
- **Sposób realizacji / Decyzja:** Cała dokumentacja projektowa będzie prowadzona w **Azure DevOps Wiki**. Każdy projekt/funkcjonalność będzie posiadał dedykowaną przestrzeń z ustandaryzowaną strukturą, przypominającą rozdziały, która będzie obejmować m.in.:
    
    - **Wprowadzenie:** Opis koncepcji, cel biznesowy, grupa docelowa.
        
    - **Założenia architektoniczne.**
        
    - **Propozycje wizualne:** Mockupy, z jawnym wskazaniem wybranego wariantu i uzasadnieniem.
        
    - **Historia zmian i wersjonowanie:** Jasne określenie zakresu dla MVP, a następnie kolejnych wersji (np. "Wersja 2"), z opisem dodanych funkcjonalności.
        
    - **Rejestr decyzji:** Kluczowe ustalenia ze spotkań będą bezpośrednio zapisywane w dokumentacji z datą.
        

---

### **3. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Reorganizacja interfejsu i wdrożenie nowego standardu dokumentacji**

- **Cel:** Wdrożenie kluczowych usprawnień w interfejsie oraz rozpoczęcie pracy zgodnie z nowym standardem dokumentacyjnym.
    
- **Zakres:**
    
    - Wdrożenie funkcjonalności: **Ujednolicenie i reorganizacja sekcji zarządzania integracjami**.
        
    - Utworzenie i uzupełnienie dokumentacji projektowej w Azure DevOps Wiki dla powyższej funkcjonalności zgodnie z nowo przyjętym standardem.
        

---

### **4. Punkty do dalszej dyskusji**

- **Narzędzie do zbierania pomysłów:** Zidentyfikowano brak dedykowanego narzędzia do zgłaszania i dyskutowania pomysłów na rozwój systemu przez osoby z całej organizacji (w tym "biznes"). Obecne mechanizmy (np. komentarze w Wiki) są niewystarczające. Należy przeanalizować i wybrać odpowiednie rozwiązanie.

Data: 14 listopada 2025

Temat: Koncepcja architektury, uprawnień i zakresu MVP dla nowego Modułu Repozytorium

---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Struktura organizacyjna Repozytorium**

- **Komponent:** Moduł Repozytorium (Backend/Frontend)
    
- **Cel:** Umożliwienie wielopoziomowej organizacji plików i folderów w systemie.
    
- **Problem do rozwiązania:** Potrzeba wydzielenia logicznych obszarów roboczych oraz obsługa dużej liczby obiektów.
    
- **Sposób realizacji / Decyzja:**
    
    - Najwyższy poziom struktury to "Przestrzenie", które mogą być wyróżnione wizualnie (np. ikoną).
        
    - Wewnątrz przestrzeni możliwe zagnieżdżanie folderów do 20 poziomów.
        
    - Ograniczenie zawartości folderu do 2000 obiektów.
        
    - Pliki mogą być przechowywane w dowolnej gałęzi (zarówno w przestrzeniach, jak i podfolderach).
        

#### **Funkcjonalność: Model uprawnień**

- **Komponent:** Moduł Repozytorium (Logika biznesowa)
    
- **Cel:** Zapewnienie bezpieczeństwa i kontroli dostępu do zasobów.
    
- **Problem do rozwiązania:** Konieczność zarządzania dostępem bez nadmiernego skomplikowania struktury dziedziczenia.
    
- **Sposób realizacji / Decyzja:**
    
    - Uprawnienia definiowane są wyłącznie na najwyższym poziomie (Przestrzeń) i są dziedziczone w dół bez możliwości przerywania.
        
    - Typy uprawnień:
        
        - **Pełny dostęp (Administrator):** Odczyt, zapis, usuwanie, zarządzanie strukturą i nadawanie dostępów.
            
        - **Edycja:** Odczyt, zapis, tworzenie struktury oraz usuwanie wyłącznie **swoich** plików i folderów.
            
        - **Odczyt:** Tylko przeglądanie.
            
    - Administrator systemu jest inicjatorem przestrzeni i nadaje uprawnienia administratora przestrzeni.
        

#### **Funkcjonalność: Obsługa plików i magazynowanie**

- **Komponent:** Moduł Repozytorium (Backend)
    
- **Cel:** Integracja fizycznego przechowywania plików z istniejącą architekturą AMODIT.
    
- **Problem do rozwiązania:** Wykorzystanie sprawdzonych mechanizmów zapisu i bezpieczeństwa.
    
- **Sposób realizacji / Decyzja:**
    
    - Mechanizm obsługi plików (upload, podgląd, zapis na dysku, szyfrowanie) tożsamy z obsługą załączników w sprawach.
        
    - Tabele bazodanowe muszą mieć odgórnie ustalone nazwy, aby uniknąć konfliktów.
        
    - Metadane w bazie danych spójne z obecnym standardem.
        

#### **Funkcjonalność: Interfejs i nawigacja (Drzewo folderów)**

- **Komponent:** Moduł Repozytorium (Frontend - React)
    
- **Cel:** Ergonomiczne przeglądanie zasobów.
    
- **Problem do rozwiązania:** Optymalizacja wydajności przy dużej liczbie węzłów (np. 10 000 elementów).
    
- **Sposób realizacji / Decyzja:**
    
    - Implementacja w technologii React, z wykorzystaniem istniejących komponentów raportowych.
        
    - Zastosowanie mechanizmu **lazy loading**: domyślne ładowanie tylko najwyższych węzłów (przestrzeni) lub ostatnio rozwiniętych; pobieranie elementów podrzędnych dopiero po rozwinięciu gałęzi.
        
    - Widoczność przycisków akcji (Dodaj, Usuń) zależna od uprawnień.
        

---

### **2. Propozycja podziału na pakiety prac (MVP)**

#### **MVP 1: Podstawowe zarządzanie strukturą i plikami**

- **Cel:** Dostarczenie funkcjonalnej wersji repozytorium umożliwiającej tworzenie struktury i przechowywanie plików w ramach jednego sprintu.
    
- **Zakres:**
    
    - Definicja i tworzenie Przestrzeni przez Administratora Systemu.
        
    - Implementacja modelu uprawnień (Admin, Edycja, Odczyt) na poziomie Przestrzeni z dziedziczeniem.
        
    - Operacje na strukturze: Dodawanie folderów, usuwanie pustych folderów.
        
    - Operacje na plikach: Upload, podgląd, usuwanie (zgodnie z uprawnieniami - swoje/wszystkie).
        
    - Frontend: Wyświetlanie drzewa z lazy loadingiem.
        

#### **Poza zakresem (Out of Scope / Backlog):**

- **Zakres:**
    
    - Przenoszenie plików między folderami.
        
    - Wersjonowanie plików.
        
    - Historia zmian.
        
    - Wyszukiwanie (planowane oparcie o silnik Lucene - po nazwie i treści).
        

---

### **Punkty do dalszej dyskusji**

- **Integracja Komunikatora:** Problemy z połączeniem HTTP i certyfikatami przy lokalnym osadzeniu AMODIT i komunikatora na jednym serwerze (Gateway/Bramka).
    
- **Wyszukiwanie:** Szczegółowa koncepcja wdrożenia silnika Lucene w późniejszych etapach.
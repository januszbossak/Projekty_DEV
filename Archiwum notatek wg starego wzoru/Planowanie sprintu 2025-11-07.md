## Tytuł: Planowanie Sprintu – 7 listopada 2025

### 1. Status bieżący i Zasoby

- **Obciążenie:** Damian zgłasza duże obciążenie backlogiem i brak czasu na bieżące analizy.
    
- **Komunikator:** Mateusz kończy poprawki w komunikatorze (drobne błędy niefunkcjonalne, przesunięcia, nazwy).
    
- **Dostępność:** Łukasz Brocki jest na urlopie, wraca po weekendzie.
    

### 2. Plany na kolejny sprint – Główne Tematy

#### A. Moduł Repozytorium Plików (JRWA)

**Kontekst:** Moduł ma zastąpić/rozszerzyć dawną funkcjonalność "Skanów". Pliki trafiają do "wspólnego worka" przed przypisaniem do konkretnej sprawy. Frontend jest w dużym stopniu gotowy, wymaga połączenia z backendem.

**Ustalenia Techniczne i Zakres:**

- **Struktura Danych:**
    
    - Pliki zapisywane w tabeli `CaseAttachments` (tak jak załączniki spraw), ale bez przypisania do sprawy (`CaseID` = null lub specyficzna flaga).
        
    - Wymagana nowa kolumna/znacznik określający wpis jako "plik repozytorium".
        
- **Struktura Logiczna vs Fizyczna:**
    
    - Logicznie pliki będą grupowane w foldery rocznikami (np. `Repository/2025`), a docelowo być może miesiącami, aby uniknąć "jednego wielkiego worka".
        
    - Fizycznie system przechowuje je zgodnie z konfiguracją (baza/dysk), użytkownik widzi strukturę folderów w interfejsie.
        
- **Uprawnienia:** CRUD (odczyt, zapis, usuwanie) na razie tylko dla folderów pierwszego poziomu.
    
- **Asystent Klasyfikacji (JRWA):** (Koncepcja) Dodatkowy przycisk przy polu "Odnośnik", otwierający "klasyfikator JRWA" – drzewo pomocnicze ułatwiające użytkownikowi znalezienie właściwej teczki rzeczowej do wpięcia dokumentu.
    
- **Wykonanie:** Zadanie prawdopodobnie przejmie **Adrian**, który kończy obecne zadania i zapoznaje się z wytycznymi frontendu.
    

#### B. Integracje dla klienta [LOT]

**Kontekst:** Kluczowe integracje kurierskie i systemowe muszą zostać zamknięte do końca roku (zakres MVP).

**Podział prac:**

- **UPS:** Udało się pozyskać kontakt techniczny. Temat realizuje **Łukasz Brocki**.
    
- **Global Express:** Nowa integracja (dedykowana firma kurierska, nie rozszerzenie nadawcy). Do realizacji przez **Łukasza Brockiego**.
    
- **Active Directory (AD/CAS):**
    
    - **Wymagania:** Autentykacja + Autoryzacja. Przy logowaniu system ma sprawdzić użytkownika, a jeśli nie istnieje – utworzyć go i przypisać do grup/ról na podstawie danych z AD (np. mapowanie 1:1 grup AD na role systemowe).
        
    - **Metoda:** Piotr potwierdził, że to wykonalne (wycena 10 dniówek, realnie kilka godzin).
        
    - **Decyzja:** Rozważyć wykonanie tego jako "standardowe" wdrożenie z użyciem `CallRest` zamiast dedykowanego modułu backendowego, jeśli to jednorazowe. Decyzja po analizie z działem wdrożeń.
        
    - **Zasoby:** Ze względu na przeciążenie Łukasza B., temat AD może zostać przekazany innej osobie (np. Adrian, jeśli nie weźmie Repozytorium) lub rozdzielony.
        

#### C. WIM – Podpis Kwalifikowany na macOS

**Status:** Klient wymaga obsługi podpisu (Szafir) na macOS dla dyrektorów.

**Decyzja:** Zamiast wytwarzać dedykowane oprogramowanie/integrację pod Szafira na Mac, rekomendowany jest zakup **SimplySign** (koszt ~245 zł), który działa na Mac i jest już zintegrowany z AMODIT.

### 3. Dług techniczny i Ryzyka

- **Brak analizy biznesowej (PKFP):** Klient (PKFP) chce konfigurować miejsce zapisu plików (baza vs dysk) per proces. Janusz blokuje prace programistyczne do momentu ustalenia **celu biznesowego ("Po co?")** tej zmiany.
    
- **Analiza procesów LOT:** Konieczne spotkanie z LOT, aby zebrać "przypadki użycia" (Use Cases) dotyczące archiwizacji – jak to robią fizycznie dzisiaj (teczka roczna, miesięczna?), aby system cyfrowy to odzwierciedlał.
    

### 4. Decyzje i Zadania (Action Items)

- **Łukasz Bott:**
    
    - Dowiedzieć się od PKFP o biznesowe uzasadnienie rozdzielania zapisu plików.
        
    - Skontaktować się z działem wdrożeń w sprawie realizacji integracji AD dla LOT (czy robimy to przez `CallRest` czy kodujemy moduł).
        
- **Damian/Janusz:** Zorganizować spotkanie z wdrożeniowcami LOT w celu ustalenia flow archiwizacji (Use Cases).
    
- **Zespół:** Przypisanie Adriana do Repozytorium lub AD (decyzja w zależności od obłożenia Łukasza B.).
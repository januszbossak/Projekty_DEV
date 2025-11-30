Dokumentacja: CRUD dla Źródeł danych Static
===========================================

* * *

1. Cel
------

Umożliwić wykorzystanie "Źródeł danych" jako miejsca, gdzie można nie tylko przechowywać zestaw danych, ale również wykonywać na nim operacje **CRU** (Create, Read, Update). Dzięki temu Źródła danych stają się aktywnym magazynem informacji, który może być dynamicznie modyfikowany przez procesy biznesowe w trakcie ich wykonywania.

### Korzyści biznesowe:

*   **Spójność danych**: Centralne miejsce przechowywania danych współdzielonych między procesami
*   **Automatyzacja**: Procesy mogą automatycznie aktualizować stany bez ręcznej ingerencji
*   **Kontrola**: Pełna kontrola nad dostępem i modyfikacją krytycznych danych biznesowych
*   **Audytowalność**: Śledzenie wszystkich zmian w danych

* * *

2. Przeznaczenie
----------------

### 2.1. Obsługa budżetów

Zarządzanie różnego rodzaju tzw. budżetów - nie tylko finansowych, ale też ilościowych, godzinowych, czasowych:
*   **Budżet urlopów**: Śledzenie dostępnych dni urlopowych na pracownika, wykorzystanych, zaplanowanych
*   **Budżet dni konsultacyjnych**: Limity wizyt/konsultacji dla pacjentów w ramach kontraktów
*   **Budżet dni szkoleniowych**: Dostępne dni szkoleniowe na pracownika/dział w roku
*   **Budżet finansowy**: Podział środków na MPK, projekty, departamenty z bieżącym wykorzystaniem
*   **Budżet nadgodzin**: Limity nadgodzin na pracownika/zespół z kontrolą przekroczeń

### 2.2. Obsługa magazynów

Uproszczona forma zarządzania magazynami ze stanami:
*   **Magazyn sprzętu biurowego**: Stany, wydania, zapotrzebowania
*   **Magazyn sprzętu IT**: Laptopy, monitory, telefony - stan, lokalizacja, przypisanie
*   **Magazyn materiałów**: Papier, tonery, materiały eksploatacyjne
*   **Magazyn próbek/leków**: W przypadku placówek medycznych

### 2.3. Inne możliwości wykorzystania

**Zarządzanie zasobami:**
*   **Sale konferencyjne**: Dostępność, rezerwacje, wyposażenie
*   **Pojazdy służbowe**: Stan, rezerwacje, przeglądy, zużycie paliwa
*   **Stanowiska pracy**: Przypisanie, dostępność, wyposażenie
**Systemy limitów i uprawnień:**
*   **Limity dostępu**: Ilość logowań, czas sesji, dostęp do modułów
*   **Certyfikaty/uprawnienia**: Daty ważności, odnowienia, statusy
*   **Licencje oprogramowania**: Dostępne, wykorzystane, wygasające
**Systemy punktowe i bonusowe:**
*   **Punkty lojalnościowe**: Dla klientów, pracowników, partnerów
*   **System nagród**: Punkty motywacyjne, premie, benefity
*   **Ranking wyników**: Sprzedaż, produktywność, jakość
**Wskaźniki i metryki:**
*   **KPI departamentów**: Bieżące wyniki vs cele
*   **Metryki procesów**: Czas realizacji, ilość, jakość
*   **Statystyki wykorzystania**: Systemów, zasobów, usług
**Zarządzanie kolejkami i rezerwacjami:**
*   **System kolejkowy**: Numery, priorytet, status obsługi
*   **Rezerwacje**: Terminy, zasoby, potwierdzenia
*   **Harmonogramy**: Dyżury, grafiki, zastępstwa

* * *

3. Założenia
------------

### 3.1. Wykorzystanie istniejącej infrastruktury

*   Wykorzystujemy istniejący typ Źródła danych o nazwie **"Static"**
*   Zachowujemy pełną kompatybilność z obecną funkcjonalnością
*   Rozszerzamy możliwości bez wpływu na istniejące implementacje

### 3.2. Zabezpieczenia przed nadpisaniem

*   Dodajemy mechanizm zabezpieczający przed ponownym wgraniem danych z pliku Excel do źródła, które jest już modyfikowane przez procesy
*   **Flaga `IsRuleManaged`**: Gdy włączona, blokuje import z plików Excel
*   **Ostrzeżenia**: Informowanie administratora o próbie nadpisania zarządzanych danych


### 3.3. Integracja z silnikiem reguł

*   Funkcje CRUD dostępne w ramach reguł
*   Pełna integracja z kontekstem sprawy i uprawnieniami

* * *

4. Realizacja
-------------

### 4.1. Rozbudowa struktury źródeł

**Dodawanie kolumn bezpośrednio w ustawieniach:**
*   Możliwość rozbudowy tabeli o nowe informacje bez ponownego importu
*   Interface graficzny do definiowania nowych kolumn
*   Walidacja nazw kolumn i typów danych
*   Migracja automatyczna istniejących danych

**Obsługiwane typy kolumn:**
*   **VARCHAR(n)**: Teksty, kody, opisy (domyślnie 255 znaków)
*   **DECIMAL(p,s)**: Wartości liczbowe z miejscami dziesiętnymi
*   **DATETIME**: Daty i czasy (z obsługą stref czasowych)
*   **INT**: Liczby całkowite (32-bit)
*   **BOOLEAN**: Wartości logiczne (true/false)

### 4.2. Funkcje reguł CRUD

#### SourceGet - Pobieranie danych

    // Pobranie całego rekordu
    rekord = SourceGet("BudzetUrlopow", "USER123");
    // Wynik: {userId: "USER123", dostepne: 26, wykorzystane: 4, zaplanowane: 8}
    
    // Pobranie konkretnej danej z kolumny
    dostepne = SourceGet("BudzetUrlopow", "USER123", "dostepne");
    // Wynik: 26
    
    

#### SourceSet - Modyfikacja danych

    // Zmiana jednej wartości
    SourceSet("BudzetUrlopow", "USER123", "dostepne", 22);
    
    // Zmiana wielu wartości
    date = CurrentDateTime()
    SourceSet("BudzetUrlopow", "USER123", {
        dostepne: 22,
        wykorzystane: 8,
        dataOstatniej: date
    });
    
    

#### SourceAddRow - Dodawanie rekordów

    // Dodanie nowego rekordu z danymi
    date = CurrentDateTime()
    newId = SourceAddRow("BudzetUrlopow", {
        userId: "USER456", 
        dostepne: 26, 
        wykorzystane: 0,
        dataUtworzenia: date
    });
    
    // Dodanie pustego rekordu (z samym kluczem)
    newId = SourceAddRow("MagazynSprzetu", "LAPTOP001");
    
    

#### SourceFind - Wyszukiwanie danych

    // Wyszukanie po jednym kryterium
    wyniki = SourceFind("BudzetUrlopow", "dostepne > 10");
    
    // Wyszukanie po wielu kryteriach
    wyniki = SourceFind("MagazynSprzetu", "kategoria = 'laptop' AND stan > 0 AND lokalizacja = 'WARSZAWA'")
    );
    
    // Wyszukanie z sortowaniem i limitem
    wyniki = SourceFind("MagazynSprzetu", "kategoria = 'laptop' AND stan > 0 AND lokalizacja = 'WARSZAWA'", 10)
    



* * *

5. Zabezpieczenia
-----------------

### 5.1. Concurrency Control (Kontrola współbieżności)

**Problem:** Jednoczesny, konkurencyjny zapis danych do tego samego rekordu z różnych procesów może prowadzić do niespójności danych.
**Rozwiązanie - Optimistic Locking:**

    -- SQL Server: Wykorzystanie rowversion
    ALTER TABLE dbsrc_BudzetUrlopow ADD version_timestamp rowversion;
    
    -- MySQL: Wykorzystanie version counter
    ALTER TABLE dbsrc_BudzetUrlopow ADD version_number BIGINT DEFAULT 0;
    
    CREATE TRIGGER tr_version_increment 
    BEFORE UPDATE ON dbsrc_BudzetUrlopow
    FOR EACH ROW SET NEW.version_number = OLD.version_number + 1;
    

**Mechanizm działania:**
1.  Przy odczycie danych pobieramy również wersję rekordu
2.  Przy zapisie sprawdzamy czy wersja się nie zmieniła
3.  Jeśli wersja się zmieniła - rzucamy `ConcurrencyException`
4.  Proces może ponowić operację z aktualnymi danymi

    

### 5.2. Kontrola dostępu (ACL)

**Poziomy uprawnień:**
*   **READ**: Odczyt danych (`SourceGet`, `SourceFind`)
*   **WRITE**: Modyfikacja istniejących danych (`SourceSet`)
*   **CREATE**: Dodawanie nowych rekordów (`SourceAddRow`)
*   **ADMIN**: Zarządzanie strukturą (dodawanie kolumn, konfiguracja)
**Implementacja:**

    // Sprawdzenie uprawnień przed operacją
    if (!hasPermission(currentUser, "BudzetUrlopow", "WRITE")) {
        throw new AccessDeniedException("Brak uprawnień do modyfikacji budżetu urlopów");
    }
    

### 5.3. Audyt i logging

**Rejestrowane zdarzenia:**
*   Wszystkie operacje CRUD z timestampem i użytkownikiem
*   Próby nieautoryzowanego dostępu
*   Konflikty concurrency i ich rozwiązania
*   Zmiany struktury źródeł danych
**Format loga:**

    {
        "timestamp": "2025-06-30T14:30:00Z",
        "user": "jan.kowalski",
        "source": "BudzetUrlopow", 
        "operation": "SourceSet",
        "recordId": "USER123",
        "changes": {
            "dostepne": {"old": 26, "new": 24}
        },
        "processId": "PR_001234"
    }
    

### 5.4. Walidacja danych

**Automatyczna walidacja:**
*   Sprawdzenie typów danych
*   Sprawdzenie długości pól tekstowych
*   Walidacja dat (format, zakresy)
*   Sprawdzenie ograniczeń biznesowych
**Niestandardowa walidacja:**

    // Walidacja biznesowa przed zapisem
    function validateBudgetUpdate(userId, newValue) {
        if (newValue < 0) {
            throw new ValidationException("Budżet nie może być ujemny");
        }
        
        var maxBudzet = SourceGet("KonfiguracjaBudzetow", "MAX_URLOP", "wartosc");
        if (newValue > maxBudzet) {
            throw new ValidationException("Przekroczono maksymalny budżet: " + maxBudzet);
        }
    }
    

* * *

6. Scenariusze użycia
---------------------

### 6.1. Wniosek urlopowy

    // 1. Sprawdzenie dostępnego budżetu
    var budzetDanych = SourceGet("BudzetUrlopow", userId);
    if (budzetDanych.dostepne < dniUrlopu) {
        throw new Error("Niewystarczający budżet urlopowy");
    }
    
    // 2. Aktualizacja budżetu
    SourceSet("BudzetUrlopow", userId, {
        dostepne: budzetDanych.dostepne - dniUrlopu,
        wykorzystane: budzetDanych.wykorzystane + dniUrlopu,
        dataOstatniej: new Date()
    });
    
    // 3. Rejestracja szczegółów urlopu
    SourceAddRow("HistoriaUrlopow", {
        userId: userId,
        dataOd: dataOd,
        dataDo: dataDo,
        liczbaDni: dniUrlopu,
        status: "zatwierdzony"
    });
    

### 6.2. Wydanie ze sprzętu z magazynu

    // 1. Sprawdzenie dostępności
    var stanMagazynu = SourceGet("MagazynSprzetu", produktId, "dostepne");
    if (stanMagazynu < ilosc) {
        throw new Error("Niewystarczająca ilość na magazynie");
    }
    
    // 2. Aktualizacja stanu
    SourceSet("MagazynSprzetu", produktId, {
        dostepne: stanMagazynu - ilosc,
        wydane: SourceGet("MagazynSprzetu", produktId, "wydane") + ilosc,
        dataOstatniegoWydania: new Date()
    });
    
    // 3. Rejestracja wydania
    SourceAddRow("HistoriaWydan", {
        produktId: produktId,
        odbiorcy: userId,
        ilosc: ilosc,
        dataWydania: new Date(),
        uzasadnienie: uzasadnienie
    });
    

* * *

**Ostatnia aktualizacja:** 2025-06-30  
**Status:** Dokumentacja projektowa  
**Kontakt:** [Team Lead], [Architekt]
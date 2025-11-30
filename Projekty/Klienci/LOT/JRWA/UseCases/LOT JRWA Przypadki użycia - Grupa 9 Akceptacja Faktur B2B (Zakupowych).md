---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje proces biznesowy związany z obiegiem i akceptacją faktur zakupowych, zgodnie z zakresem zamówienia ("akceptacja faktur B2B").

Proces ten jest kluczowym przykładem **dokumentacji nietworzącej akt sprawy** (zgodnie z § 22 Instrukcji Kancelaryjnej LOT, która wymienia "faktury, rachunki").

Celem jest zapewnienie, że każda faktura (otrzymana z KSeF, e-mailem lub jako skan) jest automatycznie rejestrowana, weryfikowana przez OCR, dekretowana merytorycznie i kosztowo (MPK), akceptowana finansowo (zgodnie z matrycą uprawnień) i przekazywana do systemu Finansowo-Księgowego (SAP).

Każda faktura (jako sprawa AMODIT) jest **automatycznie** wpinana (zgodnie z `UC-JRWA-LNK-005`) do odpowiedniej **Teczki zbiorczej** (zgodnie z `UC-JRWA-SPR-002`), np. w klasie `340` (Dowody księgowe) z JRWA 1997.

### **UC-FAKTURY-001 – Rejestracja faktury (KSeF, E-mail, Skan)**

**Rola:** Pracownik Kancelarii / System (Automat)

**Cel:** Wprowadzenie faktury zakupowej do systemu AMODIT z dowolnego kanału wejściowego.

**Opis:** System musi obsługiwać trzy kanały wejściowe:

1. **Integracja z KSeF:** (Wymóg strategiczny) System monitoruje KSeF i automatycznie pobiera nowe faktury ustrukturyzowane (XML) dla NIP LOT.
    
2. **Skrzynka e-mail:** (Wymóg `W12` z Zał. EZD) System monitoruje dedykowaną skrzynkę (np. `faktury@lot.pl`) i automatycznie pobiera załączniki (np. PDF).
    
3. **Skan:** Pracownik Kancelarii skanuje fakturę papierową, która wpłynęła tradycyjnie (realizując `UC-KANC-PRZYCH-002`, ale dla dedykowanego procesu `P_FakturaB2B`).
    

W każdym przypadku system tworzy nową instancję procesu `P_FakturaB2B`.

### **UC-FAKTURY-002 – OCR i Ekstrakcja Metadanych**

**Rola:** System

**Cel:** Automatyczne odczytanie kluczowych danych z pliku graficznego faktury (skanu lub PDF).

**Opis:**

1. Po utworzeniu sprawy (dla opcji e-mail/skan), AMODIT automatycznie wysyła obraz do usługi OCR (zgodnie z `Zamówienie...pdf`, str. 1, "koszt OCR... 43 gr/str").
    
2. System odczytuje i automatycznie wypełnia kluczowe pola formularza w AMODIT:
    
    - NIP kontrahenta (i próbuje powiązać go z bazą kontrahentów).
        
    - Numer faktury.
        
    - Data wystawienia i data sprzedaży.
        
    - Kwoty (Netto, VAT, Brutto).
        
    - Termin płatności.
        
3. (Dla KSeF ten krok jest pomijany, gdyż dane są już ustrukturyzowane w XML).
    

### **UC-FAKTURY-003 – Automatyczna klasyfikacja JRWA (Wpięcie do Teczki Zbiorczej)**

**Rola:** System

**Cel:** Automatyczne i transparentne dla użytkownika zapewnienie zgodności z JRWA dla dokumentacji nietworzącej akt sprawy.

**Opis:** Jest to realizacja `UC-JRWA-LNK-005` (Automatyczne przypisanie):

1. System jest skonfigurowany tak, że każda nowa instancja `P_FakturaB2B` z danego roku (np. 2025)...
    
2. ...jest **automatycznie wpinana** do odpowiedniej **Teczki zbiorczej** (`UC-JRWA-SPR-002`).
    
3. Teczka ta (np. `BF.340.2025` dla klasy `340` - Dowody księgowe) jest tworzona automatycznie przez system przy pierwszej fakturze w roku, jeśli jeszcze nie istnieje.
    
4. Faktura (sprawa AMODIT) **nie otrzymuje** znaku sprawy ze spisu, zgodnie z logiką Instrukcji LOT (§ 22).
    

### **UC-FAKTURY-004 – Weryfikacja merytoryczna i dekretacja kosztowa (MPK)**

**Rola:** Użytkownik merytoryczny (Właściciel kosztu) / Księgowość

**Cel:** Potwierdzenie, że usługa/towar została wykonana oraz poprawne przypisanie kosztu do odpowiedniego centrum (MPK) lub innego wymiaru analitycznego (np. projekt, konto).

**Opis:**

1. Po OCR (`UC-002`), sprawa trafia do Działu Księgowości (lub na podstawie reguł, np. numeru umowy, trafia bezpośrednio do właściciela kosztu).
    
2. Użytkownik merytoryczny (np. Dyrektor Biura) otrzymuje zadanie w AMODIT.
    
3. Musi formalnie **potwierdzić merytorycznie** ("Zgadzam się, usługa wykonana").
    
4. Dokonuje **dekretacji kosztowej**, wskazując numer(y) MPK, kwoty, typy kosztu itp. System musi wspierać dekretację podzieloną (jedna faktura na wiele MPK).
    

### **UC-FAKTURY-005 – Akceptacja finansowa (zgodnie z limitami uprawnień)**

**Rola:** Kierownik / Dyrektor / Członek Zarządu (Akceptujący)

**Cel:** Formalna akceptacja wydatku zgodnie z wewnętrzną matrycą uprawnień LOT.

**Opis:**

1. Po dekretacji kosztowej (`UC-004`), system automatycznie kieruje fakturę na ścieżkę akceptacji.
    
2. Ścieżka akceptacji jest dynamiczna i musi zależeć od **kwoty brutto** oraz **MPK** (lub innego wymiaru z dekretacji).
    
3. Np. dla MPK Biura Administracji: < 5000 PLN (Kierownik Działu), > 5000 PLN (Dyrektor Biura), > 50 000 PLN (Dyrektor Biura + Członek Zarządu ds. Finansów).
    
4. Akceptujący zatwierdzają wydatek w AMODIT.
    

### **UC-FAKTURY-006 – Przekazanie do Systemu Finansowo-Księgowego (SAP)**

**Rola:** System (Integracja)

**Cel:** Automatyczne przekazanie zaakceptowanej faktury do zaksięgowania i przygotowanie jej do płatności w systemie nadrzędnym (SAP).

**Opis:**

1. Po uzyskaniu ostatniej wymaganej akceptacji finansowej (`UC-005`), AMODIT zmienia status faktury na "Zaakceptowana / Do zaksięgowania".
    
2. System automatycznie uruchamia integrację z SAP (zgodnie z `Zamówienie...pdf` str. 6, "Koszt usług integracyjnych" oraz `Załącznik EZD` wymóg `W12`).
    
3. AMODIT wysyła do SAP komplet danych (XML, PDF, metadane dekretacji) poprzez API lub w inny uzgodniony sposób.
    
4. AMODIT musi posiadać mechanizm **odbioru informacji zwrotnej** z SAP (np. "Zaksięgowano", "Odrzucono przez SAP", "Zapłacono", "Numer dokumentu SAP").
    

### **UC-FAKTURY-007 – Zamknięcie obiegu faktury i archiwizacja**

**Rola:** System

**Cel:** Zakończenie procesu w AMODIT z zachowaniem pełnej ścieżki audytowej.

**Opis:**

1. Po otrzymaniu z SAP potwierdzenia o zaksięgowaniu (`UC-006`), system automatycznie zamyka sprawę `P_FakturaB2B`.
    
2. Sprawa (faktura) pozostaje trwale zarchiwizowana w swojej `Teczce zbiorczej` (`BF.340.2025`), która została utworzona w `UC-FAKTURY-003`.
    
3. Teczka ta będzie podlegać brakowaniu (zgodnie z `UC-JRWA-SPR-009`) po upływie okresu przechowywania (np. B5 - 5 lat od końca roku obrotowego).
    

## **Najważniejsze do zapamiętania**

> Ta grupa definiuje krytyczny proces finansowy, który jest w 100% zgodny z naszą logiką kancelaryjną.
> 
> 1. **Automatyzacja JRWA:** Faktury to "dokumentacja nietworząca akt sprawy" (§ 22 Instrukcji LOT). AMODIT realizuje to poprzez **automatyczne wpięcie** (`LNK-005`) każdej faktury do **Teczki zbiorczej** (`SPR-002`) o klasie np. `340` (z JRWA 1997), bez nadawania jej znaku sprawy.
>     
> 2. **Kluczowe integracje:** Proces ten wymaga ścisłej integracji z OCR (na wejściu) oraz z SAP (na wyjściu), co jest potwierdzone w zamówieniu.
>     
> 3. **Dynamiczny workflow:** Ścieżka akceptacji (`UC-005`) musi być elastyczna i oparta na matrycy uprawnień (kwota + MPK).
>
> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Zaktualizowano nagłówek o właściwe przypisanie projektu. Skorygowano priorytety (Repozytorium WIM i JRWA dla LOT jako "Absolutny Must Have"). Doprecyzowano statusy prac (Global Express - UPS, SignApp Safari - obejście, Comarch Hub - bloker zdjęty). Przypisano tematy do odpowiednich projektów (JRWA dla LOT, Edytor Procesów dla widoczności reguł).

# Daily – 2025-11-27

**Data:** 27 listopada 2025, 08:19
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Barbara Michałek
**Co robię:**
- Zmiany w regułach (zadanie od Łukasza B. - zajęło dużo czasu)
- Lista pól (testy)
- Kontakt z Filipem (wyjaśnienie zadania - upewnienie się, gdzie są zmiany)

### Patrycja Walaszczyk
**Co robię:**
- Lista pól
- Relist testy (bugi raportów, literówki, logowanie)

### Oktawia Ostrowska
**Co robię:**
- Lista pól, reguły, internal testy
- Relist PBI

### Michał Zwierzchowski
**Co robię:**
- Wdrożenie nowej wersji na AstraFox (wieczorem)
- Aktualizacja Wiki
- Konfiguracja linku aktualizacji baz danych (zapisywanie plików, raport z aktualizacji)

### Filip Liwiński
**Co robię:**
- Matryca uprawnień (poprawka opcji "zobacz dla")
- Lista pól (poprawki prezentacji)
- Ujednolicenie wersji Ant Design (po aktualizacji do wersji czerwcowej)

### Marek Dziakowski
**Co robię:**
- Mniejsze zgłoszenia od Kamila (AMODIT)
- Analiza błędnego dokumentu (usunięcie zbędnych errorów na maila - zapychają skrzynkę)

**Plan na dziś:**
- Wersje językowe dla listy etapów (zgłoszenie od Kamila)
- Przegląd backlogu

### Łukasz Brocki
**Co robię:**
- Onboarding na Azure (testy z Łukaszem B.)
- Integracja Global Express (pytania o projekt w Timesheet i licencję - kolejny moduł)

### Piotr Buczkowski
**Co robię:**
- Analiza problemu z serwerem AMODIT.com (Sensem? - przestał wczoraj działać)
- Logowanie do SharePoint (dokończenie)
- Problem podwójnej spacji w raporcie (PKF - analiza, poprawka CSS dla starych raportów, pytanie czy robić dla nowych - zgłoszenie 22833)

### Anna Skupińska
**Co robię:**
- Repozytorium (API tworzenia folderów - problem z testami integracyjnymi na Dockerze, baza danych)
- Problem ze "zegarkiem" (nieobecność wczoraj)
- Pytanie o DatabaseAdmin (modyfikacja kolumny NOT NULL -> NULL - rozwiązanie: usunięcie i odtworzenie tabeli przez skrypt startowy)

### Mateusz Kisiel
**Co robię:**
- UI do zarządzania serwerami MFA (Copilot - "można już w AI to fajnie sobie ustawiać")
- Generowanie dokumentacji procesu (kontynuacja)
- SA CRM (poprawka zapisu sprawy przed wykonaniem reguły)

**Plan na dziś:**
- Historia czatów Copilot w bazie

### Mariusz Piotrzkowski
**Co robię:**
- Poprawki tabeli na sprawie (nowy przycisk, zmiany)
- Błąd widoczności reguł (próba naprawy renderowania - "wydaje mi się, że wiem jak naprawić, ale nie wiem czy to nie popsuje czegoś innego")

**Plan na dziś:**
- Dokończenie sprintu
- Zgłoszenia poprawek (tabela/formularz - lista 7 zgłoszeń od Kamila)

### Adrian Kotowski
**Co robię:**
- Poprawka do e-poleconego (wycofanie z protokołu 2.0 i proxy, powrót do 1.1 RestSharp - wysłana paczka do klienta)
- Obsługa raportów w SignApp (podpisywanie masowe - 2/3 zrobione, użycie istniejącego kodu)
- Rozszerzenie integracji z GUS
- Raport podsumowujący nowe endpointy KSeF connectora (kompromis ustalony)

### Łukasz Bott
**Co robię:**
- Aktualizacja changeloga (wydanie grudniowe)
- Wdrożenie LOT
- Wsparcie sprzedaży (2 spotkania, prezentacje)

### Kamil Dubaniowski
**Co robię:**
- GTL (analiza wytycznych, diagramów - "uproszczone", "nie wierzę")
- Porządkowanie pola Tabela (rozsypane ikony, style - testy i zgłoszenia)
- Edytor formularza (zgłoszenia dla Przemka)
- Spotkanie z Przemkiem (o mapie, ale wyszło o roadmapie na 2026)

---

## 2. Nowe zgłoszenia do backlogu

### Podwójna spacja w raporcie (PKF)
**Projekt:** `Moduly/Modul-raportowy`
**Opis:**
Klient (PKF) używa podwójnej spacji w kluczach danych. Przeglądarka (CSS `white-space-collapse`) wyświetla to jako jedną spację w raporcie, co powoduje błędy przy kopiowaniu (niezgodność klucza).
**Status:** Zadanie dla Przemka na przyszły sprint (poprawka CSS, Piotr już zrobił dla starych).

### Reguły tabeli na nowej liście pól
**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`
**Opis:**
Edytor reguł tabeli otwiera się w nowej karcie (stara technologia), co psuje nawigację (brak powrotu).
**Problem:** Przyciski "Zapisz" działają (zapisują zmiany), ale **nie zamykają karty**, więc użytkownik nie widzi efektu. Przycisk "Anuluj" nie działa.
**Decyzja:** Temat na Radę Architektów. Konieczna przebudowa backendu lub przepisanie na React.

### Duplikacja nazw sekcji (Case sensitivity)
**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`
**Opis:**
Możliwość dodania sekcji o tej samej nazwie, różniącej się wielkością liter (np. "Sekcja" i "sekcja").
**Skutek:** Pola dodają się losowo do jednej z sekcji (zduplikowanych).
**Zgłaszający:** Basia.
**Rozwiązanie:** Dodać walidację case-insensitive na frontendzie i backendzie.

---

## 3. Tematy organizacyjne

### Repozytorium plików (WIM)
**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Status:** ⚠️ **Ekstremalny Priorytet**
**Ustalenia:**
- Absolutny "must have" do dowiezienia w tym sprincie (najbliższe 2-3 dni).
- Kluczowe dla harmonogramu wdrożenia (WIM).
- **Problem:** Kluczowa osoba od IT w WIM (odpowiednik Piotra) będzie nieobecna przez miesiąc ("będzie ciężej").
- **Decyzja:** Anna i Filip cisną temat (API folderów, podpięcie frontu). Adrian może odpuścić SignApp jeśli trzeba pomóc (ale na razie robi swoje).

### JRWA dla LOT
**Projekt:** `Klienci/LOT/JRWA`
**Status:** **Must Have** (na kolejny sprint)
**Ustalenia:**
- Temat musi zostać podjęty w następnym sprincie ("musimy to mieć").
- **Problem:** Piotr (opiekun) będzie nieobecny. Marek ma przejąć temat i architekturę (wzorzec GUSTeryt).

### Integracja Global Express (Licencja)
**Projekt:** `Integracje/`
**Ustalenie:**
Łukasz Brocki potrzebuje projektu w Timesheet oraz dodania modułu do licencji (wersje środkowe). Łukasz Bott ma to załatwić.

### Szkolenie GitHub
**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna/Narzędzia`
**Status:**
Przeniesione na grudzień/styczeń. Lista uczestników zmieniona.

### E-doręczenia (Protokół)
**Projekt:** `Moduly/e-Doreczenia`
**Info:**
Od stycznia nowy protokół Poczty Polskiej. AMODIT posiada wersję zgodną (potwierdzenie dla brata Janusza ze Sfinksa).

### Błąd "Brak licencji" (Restart Serwera)
**Projekt:** `Moduly/Ustawienia-systemowe`
**Opis:**
Komunikat "Brak licencji" pojawia się po restarcie serwera, gdy aplikacja nie ma jeszcze połączenia z bazą danych.
**Status:** Do weryfikacji na Radzie (czy zmienić komunikat na "Brak połączenia z bazą").

---

## 4. Decyzje ad-hoc

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Wycofanie protokołu 2.0 w e-poleconym | Problemy z proxy/obsługą na sprawie | ✅ Zatwierdzone | Powrót do sprawdzonego rozwiązania (1.1 RestSharp) w celu stabilizacji. |
| Modyfikacja kolumny DB (Ania) | Problem ze zmianą NOT NULL na NULL w skrypcie | ✅ Zatwierdzone | Piotr B. zaleca usunięcie tabeli na środowisku deweloperskim i pozwolenie na jej odtworzenie przez system. |
| Osiągnięto limit spraw (Rossmann) | Błąd pojawia się sporadycznie | ⏸️ Odroczone | Problem związany z load balancingiem (2 serwery), naprawia się samoistnie. Niski priorytet. |
| Repozytorium plików (WIM) | Koniec sprintu | ⚠️ Priorytet | Funkcjonalność tworzenia folderów musi zostać dowieziona w tym sprincie (do końca tygodnia). |
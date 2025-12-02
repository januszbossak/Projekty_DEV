# Daily – 2025-11-26

**Data:** 26 listopada 2025, 08:20
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Filip Liwiński
**Co robię:**
- Poprawki listy pól
- Błąd z podglądem plików (nie responsywny na raportach)
- Matryca uprawnień (opcja "zobacz dla")
- Uspójnienie wszystkich tabel

### Marek Dziakowski
**Co robię:**
- Konsultacje
- Analiza błędnego dokumentu
- Poprawki zadań
- Usuwanie zbędnych errorów na maila (zapchana skrzynka)
- Aktualizacja TrustCenter (produkcyjnego - bez przestoju, użycie witryny przejściowej)
- Zmiana autoryzacji do serwera Turbo STP (na klucze, rezygnacja z loginu/hasła)

### Mateusz Kisiel
**Co robię:**
- Zapisywanie serwerów MFA (Copilot) w bazie
- Interfejs do zarządzania tymi serwerami

**Plan na dziś:**
- Kontynuacja zapisywania historii czatów Copilot w bazie
- Generowanie dokumentacji

### Łukasz Brocki
**Co robię:**
- Poprawki bugów
- Global Express
- Rozbudowa `CallRest` (rozmowy z Adrianem o kluczu w KeyVault i JWT dla Dockera - uogólnienie mechanizmu)

### Mariusz Piotrzkowski
**Co robię:**
- Zakończył temat otwierania spraw z pola Odnośnik w tej samej karcie (zajęło więcej czasu, żeby dobrze działało też na raportach).

**Plan na dziś:**
- Widoczność reguł (błąd - pokazują się wszystkie reguły, mimo że prawo jest tylko do odczytu)
- Dokończenie starszych zadań

### Przemysław Rogaś
**Co robię:**
- Merge
- Dodanie pola typu aut token w ustawieniach systemowych (Piotr sugerował specyficzny sposób, Przemek zrobił po swojemu, do ewentualnej konsultacji)

**Plan na dziś:**
- Nowe zadania edytora formularza

### Piotr Buczkowski
**Co robię:**
- Analizy błędów (dużo spotkań)

**Plan na dziś:**
- Dokończenie logowania do SharePoint

### Adrian Kotowski
**Co robię:**
- Znalazł obejście problemu "szarej przestrzeni" na Safari (lista certyfikatów w SignApp)
- Usprawnił podpisywanie (biblioteki - podpisywanie jednym PINem)
- Przygotował poprawkę do integracji doręczenia (obsługa flagi metrowce dla protokołu 2.0)

**Plan na dziś:**
- Dokończenie panelu wyboru certyfikatu
- Obsługa raportów w aplikacji do wypisywania
- Testy

### Michał Zwierzchowski
**Co robię:**
- Poprawki baz danych (w polinie)
- Aktualizacja AstraFox (wszystkie witryny do czerwcowej)

### Basia (Barbara Michałek)
**Co robię:**
- Lista pól (testy)
- Zadanie od Łukasza Brockiego (testy raperów)

### Patrycja Walaszczyk
**Co robię:**
- Lista pól (testy)
- Relist testy (bez blokerów)

### Oktawia Ostrowska
**Co robię:**
- Zadania z podpisywaniem
- Lista pól

---

## 2. Nowe zgłoszenia do backlogu

### Problem z regułami tabeli na nowej liście pól
**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`
**Opis:**
Na nowej liście pól, obsługa reguł tabeli otwiera edytor w nowej karcie. Przy "Anuluj" - nic się nie dzieje. Przy "Zapisz" - zapisuje, ale **nie zamyka karty** (brak informacji zwrotnej dla użytkownika). W starej technologii link się nie zmieniał, co ułatwiało powrót.
**Ustalenia:**
- Problem z nawigacją i brakiem zapamiętywania linku powrotnego.
- Należy przerobić backend, aby zapamiętywał link powrotny.
- Rozważyć osadzenie edytora reguł tabeli w React (jeśli nie rozwiąże problemu powrotu).

### Wycinanie spacji w GUS
**Projekt:** `Moduly/Zrodla-danych`
**Opis:**
Problem z funkcją `Delta from GUS`, która wycina spacje.
**Akcja:** Łukasz Bott ma sprawdzić konstrukcję źródła danych w GUS i zdiagnozować problem.

---

## 3. Tematy organizacyjne

### Aktualizacja TrustCenter (Produkcja)
**Kategoria:** Infrastruktura
**Ustalenia:**
- Marek Dziakowski aktualizuje produkcyjny TrustCenter.
- Strona przejściowa jest używana – ciągłość pracy zachowana.
- Nie ma potrzeby publicznego informowania o przerwie.

### Szkolenie/Konsultacje e-Doręczeń
**Kategoria:** Szkolenia
**Ustalenia:**
- Adrian Kotowski ma przeprowadzić szkolenie/konsultacje z zakładania skrzynek w module doręczeń dla pracowników klienta LOT.
- Materiały wewnętrzne (nasze szkolenie) mogą pomóc.
- Termin do skoordynowania.

### Dzień kobiet (żartobliwie)
**Kategoria:** Inne
**Kontekst:** Łukasz Bott żartuje, że dziś "dzień kobiet" (obecne tylko testerki na Daily).

---

## 4. Decyzje ad-hoc

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Rozbudowa CallRest o OAuth/JWT | Dla integracji z kurierami i innymi usługami zewnętrznymi | 💡 Propozycja | Trzymanie kluczy w KeyVault. Uogólnienie mechanizmu autoryzacji. Projekt: `Moduly/CallRest`. |
| Widoczność reguł | Pokazują się wszystkie reguły, mimo że prawo jest tylko do odczytu | 🔍 Do weryfikacji | Mariusz ma zbadać i naprawić błąd w wyświetlaniu reguł. Projekt: `Moduly/Silnik-regul`. |
| Masowe akcje na raporcie | Problem z zaznaczaniem checkboxów na raporcie (akcje masowe) | 🔍 Do weryfikacji | Oktawia ma zweryfikować na relist testach, czy dotyczy Simplus. Projekt: `Moduly/Modul-raportowy/Masowe-akcje`. |
| Wyciek danych GUS | Klient LPP / wycena GUS z funkcji `Delta from GUS` | 🔍 Do weryfikacji | Wycena dla Adriana. Do sprawdzenia, czy nie obejmuje płatnych danych. Projekt: `cross-cutting/Bezpieczenstwo-pentesty`. |
| Komunikat po zakończeniu dostępu tymczasowego | Brak jasnego komunikatu po zakończeniu dostępu tymczasowego (dla klienta). | 🔍 Do weryfikacji | Mateusz ma zbadać, czy można to doprecyzować w komunikacie. Projekt: `cross-cutting/GTA - dostęp tymczasowy do sparwy`. |
| Hotfix ręczny (historia zmian) | Problem z autorem zmian w historii, gdy zmiany dokonuje reguła okresowa | 🔍 Do weryfikacji | Łukasz Bott ma zbadać, czy pierwsza osoba, która wchodzi, jest zawsze autorem zmiany. Projekt: `cross-cutting/Interfejs-sprawy/Historia-sprawy`. |
| Certyfikat liniowy (PZF) | Klient ma pytania dotyczące certyfikatu liniowego. | 🔍 Do weryfikacji | Łukasz Brocki i Tomek Marzec mają się skontaktować z klientem. Projekt: `Moduly/Trust-Center`. |

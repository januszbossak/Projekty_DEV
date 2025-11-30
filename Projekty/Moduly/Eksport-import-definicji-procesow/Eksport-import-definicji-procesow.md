# Project Canvas: Eksport/Import definicji procesów

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-10-21
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-10-20

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | [do uzupełnienia] | |
| **Tech Lead / Deweloper** | [do uzupełnienia] | |
| **Tester** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Mechanizm eksportu i importu definicji procesów (pliki XML) jest krytyczny dla migracji procesów między środowiskami (dev → test → produkcja). Obecna implementacja ma problemy z:
- Prezentacją błędów w formie technicznej tabeli (nieczytelne dla użytkownika)
- Konfliktami przy imporcie (nadpisywanie pól o tych samych ID)
- Duplikatami pól dodawanych niezależnie na różnych środowiskach

### Cel biznesowy

Zapewnienie bezpiecznego i intuicyjnego procesu przenoszenia definicji procesów między środowiskami, minimalizując ryzyko uszkodzenia danych produkcyjnych.

### Cel techniczny

Usprawnienie walidacji importu XML, poprawa obsługi błędów i konfliktów GUID, docelowo implementacja mechanizmu blokującego import przy wykrytych konfliktach.

### Metryka sukcesu

- Użytkownik otrzymuje **zrozumiały komunikat** o problemie z importem (nie techniczną tabelę)
- **Zero przypadków** uszkodzenia procesów produkcyjnych przez błędny import
- Administrator może **rozwiązać konflikt** GUID bez wsparcia technicznego

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Walidacja przed importem

System musi **walidować definicję procesu przed importem** i prezentować wykryte konflikty użytkownikowi zanim jakiekolwiek zmiany zostaną wprowadzone.

**Uzasadnienie:** Zapobieganie uszkodzeniu danych produkcyjnych przez nieświadome nadpisanie.

---

## Decyzje architektoniczne (ADR)

| ID | Data | Decyzja | Uzasadnienie |
|----|------|---------|--------------|
| ADR-001 | 2025-10-21 | Obecne rozwiązanie (ostrzeżenie/tabela) pozostaje jako tymczasowe | Uznano za wystarczające ulepszenie względem braku informacji. Redesign importu odłożony. [[Rada architektów 2025-10-21\|Rada architektów 2025-10-21]] |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

**Ukończono:**
- ✅ Walidacja importu XML - 4 nowe walidacje (do 3 istniejących)
- ✅ Wykrywanie konfliktów GUID i przypisań pól
- ✅ Ostrzeżenia przy wykryciu konfliktów

**Trwa praca nad:**
- Poprawa czytelności komunikatów błędów

**Planowane:**
- Blokowanie importu do czasu przywrócenia spójności
- Układ dwukolumnowy w oknie walidacji (dane lokalne vs. importowane)
- Możliwość wpisania GUID na środowisku testowym do rozwiązania konfliktów

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| **[Wysokie]** Uszkodzenie procesu produkcyjnego przez błędny import | Średnie | Krytyczny | Ostrzeżenia wymuszają zastanowienie przed działaniem. Docelowo: blokada importu przy konfliktach |
| **[Średnie]** Konflikty GUID między środowiskami | Średnie | Wysoki | Walidacja wykrywa konflikty. Planowane: możliwość ręcznego rozwiązania konfliktów |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Walidacja i ostrzeżenia (Status: ✅ Częściowo ukończony)

**Cel:** Wykrywanie konfliktów przed importem i ostrzeganie użytkownika.

**Funkcjonalności:**
- [x] 7 walidacji importu (3 istniejące + 4 nowe)
- [x] Wykrywanie konfliktów GUID
- [x] Wykrywanie konfliktów przypisań pól
- [x] Ostrzeżenia w formie tabeli
- [ ] Poprawa prezentacji błędów (opis tekstowy z sugestią akcji naprawczej)
- [ ] Poszerzenie okna modalnego walidacji
- [ ] Układ dwukolumnowy (dane lokalne vs. importowane)

**Planowana data:** Q4 2025

---

### 📦 MVP2: Blokada i rozwiązywanie konfliktów (Status: Planowany)

**Cel:** Aktywne zapobieganie błędnym importom i narzędzia do rozwiązywania konfliktów.

**Funkcjonalności:**
- [ ] Blokowanie importu przy wykrytych konfliktach (wymuszenie naprawy)
- [ ] Możliwość wpisania GUID na środowisku testowym
- [ ] Jasny komunikat o konieczności naprawy procesu na środowisku źródłowym

**Planowana data:** Q1 2026

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Całkowite przeprojektowanie modułu importu procesu (Priorytet: Niski - wymaga znacznych zasobów)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-10-20 | Walidacja importu XML: 4 nowe walidacje, wykrywanie konfliktów GUID | [[Sprint review 2025-10-20\|Sprint review 2025-10-20]] |
| 2025-10-21 | Utworzenie projektu. Decyzja: obecne ostrzeżenia wystarczające, redesign odłożony | [[Rada architektów 2025-10-21\|Rada architektów 2025-10-21]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]

---

## Powiązane projekty

- `moduly/Edytor-procesow-formularzy` - edycja definicji procesu (formularze, diagramy)
- `moduly/Ustawienia-systemowe` - parametr typu środowiska (prod/test) - ostrzeżenia przed modyfikacją na produkcji

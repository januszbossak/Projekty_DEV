# Project Canvas: Call Snippet

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-06-26
**Klient:** WIM
**Data rozpoczęcia:** 2025-06-26
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | [do uzupełnienia] | Implementacja |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |
| **Klient (Decydent)** | [do uzupełnienia] | Akceptacja MVP, ostateczne decyzje biznesowe |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Funkcja `CallFunction` w rzeczywistości wstawia kod (snippet) w miejsce wywołania, a nie działa jak klasyczna funkcja programistyczna. Nazwa jest myląca i może wprowadzać w błąd użytkowników oraz deweloperów, którzy oczekują zachowania typowego dla funkcji (np. możliwość przekazywania parametrów).

### Cel biznesowy
Poprawa czytelności i zrozumiałości mechanizmu poprzez zmianę nazwy z `Call Function` na `Call Snippet`, co dokładniej odzwierciedla rzeczywiste zachowanie funkcjonalności - wstawianie kodu w miejsce wywołania.

### Cel techniczny
Zmiana nazwy funkcji z zachowaniem kompatybilności wstecznej poprzez utworzenie aliasu, umożliwiając płynną migrację istniejących implementacji bez konieczności natychmiastowej zmiany wszystkich wywołań.

### Metryka sukcesu
- Wszystkie nowe użycia funkcjonalności używają nazwy `Call Snippet` zamiast `Call Function`
- Istniejące wywołania `CallFunction` nadal działają dzięki aliasowi (kompatybilność wsteczna)
- Dokumentacja i interfejs użytkownika używają poprawnej nazwy

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Kompatybilność wsteczna
Zmiana nazwy musi zachować kompatybilność wsteczną - istniejące wywołania `CallFunction` muszą nadal działać poprzez alias.
**Uzasadnienie:** Istniejące implementacje klientów nie mogą zostać zablokowane przez zmianę nazwy. Migracja może odbywać się stopniowo.

### Zasada 2: Rezygnacja z jawnych parametrów na tym etapie
Na obecnym etapie nie wprowadzamy jawnych parametrów do `Call Snippet`. Zmienne są używane wewnątrz snippetu bez konieczności ich deklaracji w wywołaniu.
**Uzasadnienie:** Uproszczenie implementacji i zachowanie obecnego modelu użycia, który działa poprawnie dla większości przypadków.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-06-26 | Zmiana nazwy z `Call Function` na `Call Snippet` z zachowaniem kompatybilności wstecznej (alias) | Nazwa dokładniej odzwierciedla rzeczywiste zachowanie - wstawianie kodu w miejsce wywołania, a nie działanie jak klasyczna funkcja | - |
| ADR-002 | ✅ Zatwierdzone | 2025-06-26 | Rezygnacja z dodawania jawnych parametrów na tym etapie - używanie zmiennych wewnątrz snippetu | Uproszczenie implementacji, zachowanie obecnego modelu użycia który działa poprawnie | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-08-26]] | Stworzenie mechanizmu globalnej biblioteki dla skryptów `Call Snippet`, dostępnej poza kontekstem pojedynczego procesu. | Promuje to zasady DRY (Don't Repeat Yourself). Złożona logika biznesowa, raz zaimplementowana i przetestowana, może być łatwo reużyta w wielu procesach, co obniża koszty i ryzyko błędów. | - |
| ADR-004 | 💡 Propozycja | [[2025-08-26]] | Stworzenie analogicznego mechanizmu globalnej biblioteki dla szablonów dokumentów. | Rozszerzenie idei reużywalności na kolejny kluczowy element systemu. Umożliwiłoby to zarządzanie firmowymi szablonami (np. stopki, nagłówki) w jednym miejscu. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji
Zmiana nazwy funkcji jest w fazie implementacji.

**Ukończono:**
- ✅ Decyzja o zmianie nazwy z `Call Function` na `Call Snippet`
- ✅ Decyzja o rezygnacji z jawnych parametrów na tym etapie

**Trwa praca nad:**
- [ ] Implementacja zmiany nazwy w kodzie
- [ ] Utworzenie aliasu dla kompatybilności wstecznej
- [ ] Aktualizacja dokumentacji
- [ ] Aktualizacja interfejsu użytkownika

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Niskie]** Niezgodność istniejących wywołań po zmianie nazwy | Niskie | Średni | Utworzenie aliasu zapewniającego kompatybilność wsteczną | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Zmiana nazwy Call Function → Call Snippet" (Status: W realizacji)
**Cel:** Wprowadzenie poprawnej nazwy funkcjonalności z zachowaniem kompatybilności wstecznej.

**Definicja ukończenia (DoD):**
- Funkcja jest dostępna pod nazwą `Call Snippet` w interfejsie użytkownika
- Istniejące wywołania `CallFunction` nadal działają dzięki aliasowi
- Dokumentacja używa poprawnej nazwy
- Wszystkie nowe użycia używają nazwy `Call Snippet`

**Funkcjonalności:**
- [ ] Zmiana nazwy funkcji w kodzie z `CallFunction` na `CallSnippet`
- [ ] Utworzenie aliasu `CallFunction` → `CallSnippet` dla kompatybilności wstecznej
- [ ] Aktualizacja interfejsu użytkownika (etykiety, opisy)
- [ ] Aktualizacja dokumentacji technicznej i użytkownika
- [ ] Weryfikacja działania istniejących wywołań z aliasem

**Poza zakresem MVP (Out of Scope):**
- Dodawanie jawnych parametrów do `Call Snippet` (odroczone na przyszłość)
- Migracja wszystkich istniejących wywołań na nową nazwę (może odbywać się stopniowo)

**Planowana data:** [do uzupełnienia]

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Dodawanie jawnych parametrów do `Call Snippet` (Priorytet: Średni)
  - Możliwość przekazywania parametrów w wywołaniu
  - Deklaracja parametrów w definicji snippetu
- Migracja wszystkich istniejących wywołań na nową nazwę (Priorytet: Niski)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-06-26 | Utworzenie projektu - zmiana nazwy z `Call Function` na `Call Snippet` z zachowaniem kompatybilności wstecznej (alias). Rezygnacja z dodawania jawnych parametrów na tym etapie - używanie zmiennych wewnątrz snippetu | [[Notatki/Rada architektów/2025-06-26 Rada architektów|Rada Architektów 2025-06-26]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]

# Project Canvas: Integracje REST - multipart/form-data

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-08-12
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-08-12
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | Adrian Kotowski | Implementacja |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Obecna metoda przesyłania plików przez funkcję `callRest` oparta na indywidualnych parach klucz-wartość w nagłówkach (np. `CustomHeaderKey1`, `CustomHeaderValue1`) jest nieelastyczna, nieintuicyjna i generuje nadmiarową liczbę parametrów. Utrudnia to zarządzanie integracjami REST, szczególnie gdy potrzebna jest możliwość przesyłania wielu plików w jednym żądaniu.

### Cel biznesowy

Usprawnienie mechanizmu przesyłania załączników w integracjach REST poprzez zastąpienie obecnej metody standardem `multipart/form-data` i `x-www-form-urlencoded`, co umożliwi elastyczne przesyłanie wielu plików w jednym żądaniu i uprości konfigurację integracji.

### Cel techniczny

Wprowadzenie natywnego wsparcia dla formatów `multipart/form-data` i `x-www-form-urlencoded` w funkcji `callRest`, z możliwością odwołania się do listy załączników na sprawie oraz ustrukturyzowaną obsługą wielu dokumentów jako pojedynczego parametru.

### Metryka sukcesu

- Użytkownik może przesłać wiele plików w jednym żądaniu bez konieczności definiowania indywidualnych parametrów dla każdego pliku
- Konfiguracja integracji z załącznikami jest bardziej intuicyjna i wymaga mniej parametrów

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Kompatybilność wsteczna

Wszystkie nowe mechanizmy muszą działać bez wpływu na istniejące integracje REST, które korzystają z obecnej metody przesyłania plików.

**Uzasadnienie:** Istniejące integracje klientów nie mogą zostać zablokowane po wprowadzeniu zmian.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-08-12 | Wprowadzenie zmiennej dla listy załączników zamiast indywidualnych par klucz-wartość | Elastyczne, upraszcza konfigurację, możliwość odwołania się do listy załączników na sprawie | - |
| ADR-002 | ✅ Zatwierdzone | 2025-08-12 | Tablica `documents` z obiektami zawierającymi `DocumentName` i `DocumentValue` (Base64) | Ustrukturyzowane podejście dla wielu dokumentów jako pojedynczego parametru | - |
| ADR-003 | ✅ Zatwierdzone | 2025-08-12 | Natywne wsparcie dla formatu `multipart/form-data` | Standardowy format, wymagany przez klientów | - |
| ADR-004 | ✅ Zatwierdzone | 2025-08-12 | Natywne wsparcie dla formatu `x-www-form-urlencoded` | Również wymagany format przez klientów | - |
| ADR-005 | ✅ Zatwierdzone | 2025-08-12 | Mechanizm podobny do headers - pary klucz-wartość przekazywane przez nową linię (przełamanie linii = kolejna para) | Spójność z istniejącym mechanizmem definiowania nagłówków | - |
| ADR-006 | ❌ Odrzucone | 2025-08-12 | Indywidualne pary klucz-wartość w nagłówkach (`CustomHeaderKey1`, `CustomHeaderValue1`) | Nieelastyczne, generuje nadmiar parametrów, trudne w zarządzaniu | - |
| ADR-007 | ✅ Zatwierdzone | [[2025-09-11]] | Obsługa wielu plików w `multipart/form-data` będzie realizowana przez jeden parametr z listą plików (separatory), analogicznie do mechanizmu `headers` z wersji 10.2. | Rozwiązanie spójne z istniejącymi mechanizmami w systemie. Użycie Handlebars (`#each`) pozwoli na dynamiczne budowanie listy plików w regule, co jest kluczowe dla obsługi zmiennej liczby załączników. | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

Projekt jest w fazie aktywnego rozwoju. Trwa implementacja usprawnień mechanizmu przesyłania załączników zgodnie z ustaleniami.

**Ukończono:**
- ✅ Ustalenie architektury i podejścia technicznego

**Trwa praca nad:**
- Implementacja usprawnień mechanizmu przesyłania załączników

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Niskie]** Problemy z kompatybilnością wsteczną istniejących integracji | Niskie | Średni | Zapewnienie kompatybilności wstecznej - istniejące integracje pozostają bez zmian | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Natywne wsparcie multipart/form-data i x-www-form-urlencoded (Plan: Q4 2025)

**Cel:** Umożliwienie wysyłania wielu plików w jednym żądaniu w standardowych formatach wymaganych przez klientów (Marba, KSeF).

**Definicja ukończenia (DoD):**
- Użytkownik może przesłać wiele plików w jednym żądaniu przez funkcję `callRest`
- Funkcja `callRest` obsługuje formaty `multipart/form-data` i `x-www-form-urlencoded`
- Możliwość odwołania się do listy załączników na sprawie zamiast definiowania indywidualnych parametrów
- Tablica `documents` umożliwia przekazanie wielu dokumentów jako pojedynczego parametru

**Funkcjonalności:**

#### Mechanizm przesyłania załączników
- [ ] Wprowadzenie zmiennej dla listy załączników (odwołanie do listy załączników na sprawie)
- [ ] Tablica `documents` z obiektami zawierającymi `DocumentName` i `DocumentValue` (Base64)
- [ ] Mechanizm podobny do headers - pary klucz-wartość przekazywane przez nową linię

#### Obsługa formatów
- [ ] Natywne wsparcie dla formatu `multipart/form-data`
- [ ] Natywne wsparcie dla formatu `x-www-form-urlencoded`

**Poza zakresem MVP (Out of Scope):**
- Obsługa wysyłania wielu plików w formacie JSON - odłożona do czasu konkretnego zapotrzebowania biznesowego

**Planowana data:** Q4 2025

**Zadania:**
- **Adrian Kotowski:** Implementacja usprawnień mechanizmu przesyłania załączników zgodnie z ustaleniami
- **Piotr Buczkowski:** Weryfikacja i przegląd implementacji

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Obsługa wysyłania wielu plików w formacie JSON (Priorytet: Niski - wymaga konkretnego zapotrzebowania biznesowego)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Utworzenie projektu - ustalenie architektury: zmienna dla listy załączników, tablica `documents`, natywne wsparcie dla `multipart/form-data` i `x-www-form-urlencoded` | [[Notatki/Rada architektów/2025-08-12 Rada architektów]] |
| [[2025-09-11]] | Potwierdzenie kierunku implementacji dla wysyłania wielu plików w `multipart/form-data` w odpowiedzi na wymaganie klienta Marba. Wybrano rozwiązanie analogiczne do mechanizmu `headers`. | [[2025-09-11 Rada architektów]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja zewnętrzna:** [do uzupełnienia]
- **Umowa z klientem:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]


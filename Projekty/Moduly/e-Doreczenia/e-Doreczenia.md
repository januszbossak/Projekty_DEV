# Project Canvas: e-Doręczenia

**Status:** 🔴 Krytyczny problem
**Ostatnia aktualizacja:** 2025-10-09
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** [do uzupełnienia]

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | [do uzupełnienia] | |
| **Tech Lead / Deweloper** | Adrian, Piotr | |
| **Tester** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Przedsiębiorcy i instytucje publiczne w Polsce są zobowiązani do obsługi elektronicznych doręczeń w ramach systemu e-Doręczeń (Poczta Polska). Klienci AMODIT potrzebują bezproblemowej integracji z tym systemem aby spełnić wymogi prawne i umożliwić automatyczne odbieranie oraz wysyłanie dokumentów urzędowych.

### Cel biznesowy

Zapewnienie pełnej, stabilnej integracji AMODIT z systemem e-Doręczeń Poczty Polskiej, umożliwiającej klientom spełnienie wymogów prawnych oraz automatyzację obiegu dokumentów urzędowych bez ręcznej interwencji.

### Cel techniczny

Zbudowanie i utrzymanie niezawodnej integracji z API e-Doręczeń działającej na wszystkich środowiskach (on-premise i chmura), z odpornością na problemy konfiguracyjne i sieciowe.

### Metryka sukcesu

- Integracja działa stabilnie na **100% środowisk produkcyjnych** (on-premise i chmura)
- Użytkownik otrzymuje powiadomienie o nowym e-Doręczeniu **w < 5 minut** od wysłania
- **Zero przestojów** w funkcjonalności e-Doręczeń dla klientów płacących za tę usługę

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Integracja z API Poczty Polskiej

Moduł musi korzystać z **oficjalnego API e-Doręczeń** udostępnionego przez Pocztę Polską. Nie dopuszcza się alternatywnych metod dostępu lub obejść protokołu.

**Uzasadnienie:** Wymóg prawny i techniczny - jedyna wspierana metoda integracji z systemem e-Doręczeń.

---

## Decyzje architektoniczne (ADR)

| ID | Data | Decyzja | Uzasadnienie |
|----|------|---------|--------------|
| | | [Do uzupełnienia po wdrożeniu MVP] | |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🔴 Krytyczny problem - diagnostyka i naprawa

Projekt znajduje się w krytycznej fazie naprawczej. Integracja z e-Doręczeniami nie działa na środowiskach chmurowych dla klientów produkcyjnych od ponad trzech miesięcy, mimo że działa poprawnie na środowiskach on-premise. Jest to **najwyższy priorytet** dla zespołu.

**Ukończono:**
- ✅ [Do uzupełnienia - funkcjonalności zrealizowane przed wystąpieniem problemu]

**Trwa praca nad:**
- Diagnostyka problemu na środowisku chmurowym (Azure)
- Stworzenie programu testującego połączenie
- Identyfikacja miejsca występowania błędu (Key Vault, ustawienia sieciowe, lokalizacja serwerów)
- **Problem z dwoma instancjami AS** - błąd "forbidden" przy uruchomieniu obu instancji jednocześnie
- Weryfikacja mechanizmu **Preferred Server** dla wymuszenia łączenia przez jeden serwer

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| **[Wysokie - KRYTYCZNE]** Integracja nie działa na środowisku chmurowym od ponad 3 miesięcy | Potwierdzony fakt | Krytyczny | Adrian odłożył wszystkie inne zadania i skupia się wyłącznie na rozwiązaniu problemu. Piotr wspiera diagnostykę. Stworzenie prostego programu testującego połączenie do uruchomienia z różnych serwerów. Wszystko wskazuje że błąd leży w konfiguracji Azure (Key Vault, sieciowe, lokalizacja), nie po stronie Poczty Polskiej |
| **[Wysokie]** Brak odpowiedzi ze strony wsparcia Poczty Polskiej | Wysokie | Wysoki | Informowanie klientów aby sami eskalowali problem u swoich opiekunów handlowych w Poczcie Polskiej. Koncentracja na diagnostyce po stronie AMODIT |
| **[Średnie]** Utrata wizerunku firmy i zaufania kluczowych klientów chmurowych | Średnie | Wysoki | Transparentna komunikacja o statusie prac. Natychmiastowe zaktualizowanie statusu w wewnętrznych kanałach. Przekazanie szczegółowych informacji o blokadach do Daniela Reszki |
| **[Średnie]** Problem z Load Balancingiem (2 instancje AS) | Potwierdzony | Wysoki | Błąd "forbidden" gdy obie instancje działają jednocześnie. Problem prawdopodobnie po stronie konfiguracji serwerów firmy (2 adresy IP) lub zbyt szybkie żądania. Rozwiązanie: mechanizm Preferred Server |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: [Nazwa - do uzupełnienia]

**Cel:** [Do uzupełnienia po naprawie krytycznego problemu i określeniu dalszego kierunku rozwoju]

**Funkcjonalności:**
- [ ] [Do uzupełnienia]

**Planowana data:** [Do uzupełnienia]

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- [Do uzupełnienia]

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-11]] | Zgłoszono problemy z działaniem e-Doręczeń na środowiskach chmurowych. Podkreślono potrzebę poprawy komunikacji z klientami o statusie prac. | [[2025-09-11 Rada architektów]] |
| 2025-10-09 | Aktualizacja krytycznego ryzyka: problem trwa ponad 3 miesiące, diagnostyka Azure (Key Vault, sieciowe), Adrian z najwyższym priorytetem, Piotr wspiera | Rada Architektów 2025-10-09 |
| 2025-10-14 | Nowy problem: błąd "forbidden" przy 2 instancjach AS. Rozwiązanie: mechanizm Preferred Server. Problem leży w konfiguracji serwerów firmy | Rada Architektów 2025-10-14 |
| 2025-10-20 | Kontynuacja prac nad problemami z API, zgłoszono uwagi do COI (Centralny Ośrodek Informatyki) | Sprint review 2025-10-20 |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja API e-Doręczeń:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]

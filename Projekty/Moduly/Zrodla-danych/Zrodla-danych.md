# Project Canvas: Źródła danych

**Status:** ✅ Ukończone
**Ostatnia aktualizacja:** 2025-07-07
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | [do uzupełnienia] | Architektura |
| **Deweloper** | [do uzupełnienia] | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Mechanizmy zasilania źródeł danych w AMODIT były ograniczone głównie do zapytań SQL. Brakowało elastycznego sposobu na wpychanie danych z systemów zewnętrznych w czasie rzeczywistym.

### Cel biznesowy
Zwiększenie elastyczności i możliwości integracyjnych platformy AMODIT. Umożliwienie systemom zewnętrznym aktywnego zasilania źródeł danych. Ma to przyspieszyć wdrożenia i obniżyć koszty utrzymania.

### Cel techniczny
Stworzenie dedykowanego endpointu w REST API, który pozwoli na bezpieczne przesyłanie danych (np. w formacie JSON) i zasilanie wskazanego źródła danych.

### Metryka sukcesu
- Czas potrzebny na integrację i zasilenie źródła danych z systemu zewnętrznego skrócony o 50% dzięki wykorzystaniu REST API zamiast bezpośrednich zapytań do bazy.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-26]] | Udostępnienie endpointu REST API do zasilania zewnętrznych źródeł danych. | REST API jest nowoczesnym i bezpiecznym standardem integracji, znacznie bardziej elastycznym i łatwiejszym w użyciu dla deweloperów systemów zewnętrznych niż bezpośredni dostęp do bazy danych. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: ✅ Ukończone

Zaimplementowano kluczowe mechanizmy.

**Ukończono:**
- ✅ Endpoint REST API do zasilania źródeł danych.

**Planowane:**
- Dalsza rozbudowa modułu o operacje CRUD w ramach projektu [[Zmienne-globalne]].

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|---|---|---|
| [[2025-07-07]] | Moduł został rozbudowany o funkcjonalność CRUD na źródłach 'Static' w ramach projektu [[Zmienne-globalne]]. | [[2025-07-07 Odczyt i zapis do Źródła danych typu static]] |
| [[2025-08-26]] | Utworzenie projektu. Zaimplementowano zasilanie źródeł danych przez REST API. | [[2025-08-26 Notatka projektowa - AMODIT UI]] |

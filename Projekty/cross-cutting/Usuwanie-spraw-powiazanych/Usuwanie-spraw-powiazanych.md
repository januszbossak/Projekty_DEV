# Usuwanie spraw powiązanych

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | Piotr | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting (bugfix)
**Status:** Do realizacji (następny sprint)
**Data rozpoczęcia:** 2025-09-16
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Błąd spójności danych - system blokuje usuwanie spraw nadrzędnych w określonych przypadkach.

### Problem do rozwiązania

System blokuje możliwość usunięcia sprawy nadrzędnej, jeśli jest z nią powiązana sprawa podrzędna, która została wcześniej usunięta (i ma status `is_hidden=true`).

Logika usuwania nie uwzględnia spraw ukrytych, co prowadzi do błędu spójności referencyjnej w bazie danych.

### Cel projektu

Poprawne obsługiwanie relacji ze sprawami podrzędnymi przy usuwaniu sprawy nadrzędnej.

---

## 2. Kontekst techniczno-architektoniczny

### Rozwiązanie

Zmodyfikować proces usuwania tak, aby przed skasowaniem sprawy nadrzędnej poprawnie obsługiwał (odpinał) również relacje ze sprawami podrzędnymi o statusie `is_hidden`.

### Decyzja (2025-09-16)

Problem jest jasno zdefiniowany i wiadomo, jak go naprawić. Zadanie zostanie przypisane do realizacji w kolejnym sprincie.

---

## 3. Zadania

- [ ] **Łukasz:** Przypisać zadanie do Piotra na następny sprint
- [ ] **Piotr:** Szczegółowa analiza i przygotowanie opisu rozwiązania

---

## 4. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-16 | Utworzenie projektu - błąd do naprawy w następnym sprincie | Rada Architektów 2025-09-16 |

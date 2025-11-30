# Project Canvas: Szablony maili systemowych

**Status:** 🟢 W realizacji (MVP) / ⏸️ Odroczone (rozwiązania długoterminowe)
**Ostatnia aktualizacja:** 2025-09-09
**Klient:** AMODIT (problem zgłaszany przez dużych klientów, m.in. Orlen, LPP)
**Data rozpoczęcia:** 2025-09-09

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Piotr Buczkowski | Implementacja MVP |
| **PDM** | Janusz Bossak | Przygotowanie mapy drogowej dla rozwiązań długoterminowych |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klienci, szczególnie duzi, często dostosowują treść i wygląd systemowych szablonów e-mail do swoich standardów komunikacji. Obecny mechanizm aktualizacji AMODIT bezwarunkowo nadpisuje wszystkie szablony, co powoduje, że klienci tracą swoje modyfikacje przy każdej aktualizacji. Jest to poważny problem operacyjny, który generuje frustrację i dodatkową pracę po stronie klientów.

### Cel biznesowy
Zapewnienie stabilności i przewidywalności w zarządzaniu szablonami e-mail. Klienci, którzy zainwestowali czas w dostosowanie szablonów, muszą mieć pewność, że ich zmiany nie zostaną utracone podczas standardowych procedur utrzymaniowych systemu.

### Cel techniczny
Wdrożenie mechanizmu, który pozwoli na oznaczanie szablonów jako "zmodyfikowane przez klienta" i będzie je pomijał podczas procesu aktualizacji bazy danych. W dalszej perspektywie planowane jest zbudowanie kompleksowego rozwiązania do zarządzania szablonami.

### Metryka sukcesu
- Zero przypadków nadpisania zmodyfikowanych przez klienta szablonów po wdrożeniu MVP.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-09]] | **MVP:** Dodać do tabeli z szablonami kolumnę flagującą (np. `SkipUpdate`), która będzie chronić oznaczony rekord przed nadpisaniem podczas aktualizacji systemu. | Jest to najszybsze możliwe rozwiązanie (szacowane na ~1h pracy), które w pełni adresuje palący problem klienta. | - |
| ADR-002 | ⏸️ Odroczone | [[2025-09-09]] | **Rozwiązanie długoterminowe A:** Dodać kolumnę na customowy szablon i przełącznik decydujący, czy używać szablonu domyślnego, czy customowego. | Bardziej elastyczne niż MVP, pozwala zachować oryginalny szablon i łatwo się między nimi przełączać. Wymaga jednak więcej pracy (5-20h). | - |
| ADR-003 | ⏸️ Odroczone | [[2025-09-09]] | **Rozwiązanie długoterminowe B:** Stworzenie pełnego interfejsu w Ustawieniach Systemowych do zarządzania szablonami. | Rozwiązanie docelowe, dające pełną kontrolę i wygodę, ale jest to duży projekt (szacowany na 2 sprinty dla 2 osób). | - |
| ADR-004 | ⏸️ Odroczone | [[2025-09-09]] | **Rozwiązanie długoterminowe C:** Globalny redesign wszystkich szablonów maili. | Obecne szablony są przestarzałe wizualnie. Redesign jest potrzebny, ale jest to ogromne przedsięwzięcie (szacowane 20+ PBI) wymagające osobnego budżetu i mapy projektu. | - |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Ochrona przed nadpisaniem" (realizacja natychmiastowa)
- **Cel:** Szybkie rozwiązanie problemu utraty zmian w szablonach.
- **Funkcjonalności:**
    - Dodanie do tabeli z szablonami maili nowej kolumny typu `boolean` (np. `SkipUpdate` lub `IsCustom`).
    - Modyfikacja skryptu aktualizacyjnego tak, aby ignorował (nie nadpisywał) rekordy, które mają w tej kolumnie ustawioną wartość `true`.

### 📦 Backlog (przyszłe wersje)
- **Customowy szablon + znacznik:** Implementacja oddzielnej kolumny na zmodyfikowany szablon, co pozwoli zachować oryginał.
- **Interfejs do zarządzania szablonami:** UI w Ustawieniach Systemowych do edycji, podglądu i zarządzania wersjami szablonów.
- **Globalny redesign szablonów:** Osobny, duży projekt mający na celu unowocześnienie wyglądu wszystkich maili systemowych.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-09]] | Utworzenie projektu. Zdiagnozowano krytyczny problem nadpisywania szablonów maili u klientów. Zatwierdzono natychmiastowe wdrożenie rozwiązania krótkoterminowego (flaga chroniąca) i odroczono prace nad kompleksową przebudową. | [[2025-09-09 Rada architektów]] |

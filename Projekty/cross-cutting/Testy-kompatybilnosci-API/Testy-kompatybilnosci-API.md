# Project Canvas: Testy kompatybilności API

**Status:** 💡 Propozycja
**Powód statusu / Bloker:** Wymaga decyzji o zakresie bibliotek objętych testem oraz częstotliwości aktualizacji snapshota
**Ostatnia aktualizacja:** 2025-08-12
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-08-12
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | Adrian Kotowski | Implementacja (jeśli znajdzie czas) |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Częste problemy z kompatybilnością wsteczną wynikają z braku automatycznej kontroli nad zmianami w publicznych interfejsach i metodach kluczowych bibliotek (np. `AMODIT.Classes`). Przypadkowe modyfikacje publicznego API mogą łamać kompatybilność wsteczną, co prowadzi do błędów w istniejących implementacjach (np. problem z interfejsem `IJob` na środowisku Stage w Rossmannie).

### Cel biznesowy

Wprowadzenie mechanizmu automatycznego wykrywania przypadkowych zmian w publicznym API kluczowych bibliotek przed wdrożeniem, eliminując ryzyko łamania kompatybilności wstecznej i błędów w istniejących implementacjach.

### Cel techniczny

Stworzenie testu jednostkowego, który zapisuje snapshot wszystkich publicznych metod z kluczowych bibliotek do pliku i porównuje aktualny stan z zapisanym snapshotem przy każdym uruchomieniu, wykrywając zmiany w publicznych metodach (modyfikacje, usunięcia).

### Metryka sukcesu

- Wszystkie zmiany w publicznym API są wykrywane przed wdrożeniem
- Brak przypadkowych zmian w publicznych metodach powodujących błędy w istniejących implementacjach

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

[Do uzupełnienia po decyzjach architektonicznych]

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | 💡 Propozycja | 2025-08-12 | Test snapshotowy zapisujący snapshot wszystkich publicznych metod do pliku i porównujący z aktualnym stanem | Proste rozwiązanie, łatwe do zrealizowania, wykrywa zmiany w publicznych metodach przed wdrożeniem | - |
| ADR-002 | ❌ Odrzucone | 2025-08-12 | Brak automatycznej kontroli zmian w publicznym API (ręczna weryfikacja) | Nieefektywne, łatwo o przeoczenie zmian | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

Projekt jest w fazie propozycji. Wymaga decyzji o zakresie bibliotek objętych testem oraz częstotliwości aktualizacji snapshota.

**Ukończono:**
- ✅ Zaproponowanie rozwiązania testu snapshotowego

**Trwa praca nad:**
- Decyzja o zakresie bibliotek objętych testem
- Decyzja o częstotliwości aktualizacji snapshota
- Decyzja czy rozszerzyć test również na interfejsy (nie tylko metody)

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Przypadkowe łamanie kompatybilności wstecznej przy modyfikacji publicznych metod | Średnie | Wysoki | Test snapshotowy wykrywa zmiany przed wdrożeniem | Tech Lead |
| **[Średnie]** Brak wykrycia zmian w publicznym API przed wdrożeniem | Średnie | Wysoki | Automatyczna kontrola przez test snapshotowy | Tech Lead |

---

### Punkty wymagające decyzji (w fazie analizy)

**Zakres testu:**
- [ ] Które biblioteki powinny być objęte testem snapshotowym? (sugerowane: `AMODIT.Classes` lub inne kluczowe biblioteki)
- [ ] Czy rozszerzyć test również na interfejsy (nie tylko metody)?

**Mechanizm:**
- [ ] Jak często aktualizować snapshot? (przy świadomych zmianach, okresowo, przy każdym commicie?)

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Test snapshotowy dla publicznych metod (Plan: [do uzupełnienia])

**Cel:** Wykrywanie przypadkowych zmian w publicznym API kluczowych bibliotek przed wdrożeniem.

**Definicja ukończenia (DoD):**
- Test jednostkowy zapisuje snapshot wszystkich publicznych metod z biblioteki do pliku przypiętego do projektu
- Przy każdym uruchomieniu test porównuje aktualny stan z zapisanym snapshotem
- Test wykrywa zmiany w publicznych metodach (modyfikacje, usunięcia)
- Mechanizm aktualizacji snapshota przy świadomych zmianach

**Funkcjonalności:**

#### Mechanizm snapshotowy
- [ ] Test jednostkowy zapisujący snapshot wszystkich publicznych metod z biblioteki (np. `AMODIT.Classes`)
- [ ] Porównanie aktualnego stanu z zapisanym snapshotem przy każdym uruchomieniu
- [ ] Wykrywanie zmian w publicznych metodach (modyfikacje, usunięcia)
- [ ] Mechanizm aktualizacji snapshota przy świadomych zmianach

**Poza zakresem MVP (Out of Scope):**
- Rozszerzenie testu na interfejsy (nie tylko metody) - do rozważenia w przyszłości

**Planowana data:** [do uzupełnienia]

**Zadania:**
- **Adrian Kotowski:** Przygotowanie testu jednostkowego do wykrywania zmian w publicznych metodach (jeśli znajdzie czas)

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Rozszerzenie testu również na interfejsy (nie tylko metody) (Priorytet: Średni)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Utworzenie projektu - propozycja testu snapshotowego do wykrywania zmian w publicznych metodach kluczowych bibliotek | [[Notatki/Rada architektów/2025-08-12 Rada architektów|Rada Architektów 2025-08-12]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja zewnętrzna:** [do uzupełnienia]
- **Umowa z klientem:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]


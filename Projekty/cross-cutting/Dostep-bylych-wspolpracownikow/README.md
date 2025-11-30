# Dostęp dla byłych współpracowników

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | Piotr | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting
**Status:** Do realizacji
**Data rozpoczęcia:** 2025-08-19
**Planowane zakończenie:** -

**Powiązane zgłoszenie:** #21722

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Osoby, które wykonywały akcje w sprawie jako współpracownicy, po odebraniu tej roli całkowicie tracą dostęp do sprawy. Utrudnia to audyt, zachowanie ciągłości kontekstu i wgląd w historyczne działania.

### Cel projektu

Wprowadzenie konfigurowalnej opcji pozwalającej byłym współpracownikom na zachowanie stałego dostępu do odczytu spraw, w których byli aktywni.

### Problem

- Były współpracownik traci całkowity dostęp do sprawy po odebraniu roli
- Brak możliwości wglądu nawet w trybie do odczytu
- Utrudniony audyt i zachowanie kontekstu
- Problem z ciągłością wiedzy o historycznych działaniach

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne

Modyfikacja mechanizmu uprawnień w AMODIT - dodanie opcji konfigurowalnej na poziomie definicji procesu.

### Rozwiązanie techniczne

**Konfiguracja:**
- Dedykowana opcja w definicji procesu
- Mechanizm analogiczny do istniejącego mechanizmu dla zastępstw

**Działanie:**
- Po włączeniu opcji - były współpracownik zachowuje dostęp do odczytu
- Dostęp tylko do spraw, w których był aktywny (wykonywał akcje)
- Tryb tylko do odczytu (bez możliwości edycji)

### Kluczowe decyzje architektoniczne

| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| 2025-08-19 | Konfiguracja per proces | Elastyczność - różne procesy mogą mieć różne wymagania |
| 2025-08-19 | Wzorowanie na mechanizmie zastępstw | Spójność z istniejącymi rozwiązaniami |

---

## 3. Plan wydań MVP

### MVP1: Zachowanie dostępu do odczytu

**Cel:** Umożliwić byłym współpracownikom wgląd w sprawy, w których uczestniczyli

**Funkcjonalności:**
- [ ] Opcja w definicji procesu "Zachowaj dostęp do odczytu dla byłych współpracowników"
- [ ] Automatyczne przyznawanie dostępu do odczytu po usunięciu roli współpracownika
- [ ] Dostęp tylko do spraw, w których użytkownik wykonywał akcje

**Zespół:** Piotr

**Planowana data:** -

---

## 4. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-19 | Utworzenie projektu, definicja wymagań | Rada Architektów 2025-08-19 |

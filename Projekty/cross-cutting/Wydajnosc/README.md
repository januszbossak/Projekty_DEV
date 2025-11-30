# Wydajność

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting
**Status:** [W analizie / W realizacji / Wdrożony / Wstrzymany]
**Data rozpoczęcia:**
**Planowane zakończenie:**

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?
[Roadmapa / Inicjatywa strategiczna / Potrzeba rynkowa]

### Cel projektu
[Jaki problem rozwiązujemy? Jaką wartość dostarczamy użytkownikom?]

### Powiązane dokumenty
- Inicjatywa w backlogu: [link]

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne
[Część AMODIT / Osobny moduł / Microserwis / Integracja zewnętrzna]

### Technologie
- Frontend:
- Backend:
- Baza danych:

### Wykorzystanie funkcjonalności AMODIT
[Co możemy wykorzystać z istniejącego systemu?]

### Założenia UI/UX
[Główne założenia dotyczące interfejsu użytkownika]

### Kluczowe decyzje architektoniczne
| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| | | |

---

## 3. Plan wydań MVP

### MVP1: [Nazwa/Cel]
**Cel:** [Dlaczego akurat taki zakres? Co chcemy zweryfikować?]

**Funkcjonalności:**
- [ ] Funkcjonalność A
- [ ] Funkcjonalność B
- [ ] Funkcjonalność C

**Planowana data:**

---

### MVP2: [Nazwa/Cel]
**Cel:** [Co rozszerzamy? Dlaczego?]

**Funkcjonalności:**
- [ ] Funkcjonalność D
- [ ] Funkcjonalność E

**Planowana data:**

---

### Backlog (przyszłe MVP)
- Funkcjonalność F
- Funkcjonalność G

---

## 4. Analizy wydajności

### Analiza środowiska klienta (2025-09)

**Status:** Zaakceptowana przez klienta
**Zakres:** 2 dni robocze

**Problem:**
Klient zgłasza poważne problemy z wydajnością systemu:
- Długo wykonujące się reguły
- Nadmierne obciążenie bazy danych

**Rozwiązanie:**
- Płatna, dwudniowa analiza środowiska klienta
- Diagnoza źródła problemów
- Raport z rekomendacjami

**Zespół:**
- Piotr (główny)
- Łukasz Grodzki (transfer wiedzy)

**Zadania:**
- [ ] **Damian:** Skontaktować Piotra z Danielem (opiekunem klienta) w celu ustalenia harmonogramu

---

### Zmiana typów pól tekstowych w bazie danych

**Status:** Wdrożone (narzędzie gotowe)
**Data:** 2025-10-06

**Problem:**
Ograniczenie długości znaków w polach krótkiego tekstu (domyślnie 255 znaków) - problem przy zapisywaniu bardzo długich linków.

**Rozwiązanie:**
- W narzędziu Database Admin stworzono funkcję generującą skrypt SQL
- Skrypt zmienia typ kolumn dla wszystkich pól tekstowych: `VARCHAR` → `MEDIUMTEXT` (MS SQL i MySQL)
- Radykalne zwiększenie pojemności i eliminacja ograniczenia 255 znaków

**Ważne:**
- Operacja czasochłonna (może trwać >30 minut)
- Wymaga pełnego wyłączenia aplikacji
- Wykonywać poza godzinami pracy, po kopii zapasowej bazy
- Przygotowana instrukcja dla administratorów

---

### Optymalizacja pobierania danych w widokach React

**Status:** Do realizacji (pilne)
**Data:** 2025-10-14

**Problem:**
W widokach opartych o React (nowe widoki) występują problemy z **nadmiernym pobieraniem danych** przy wejściu na stronę:
- Pobieranie wszystkich użytkowników
- Pobieranie wszystkich pozycji słownika
- Pobieranie wszystkich słowników

Jest to nieoptymalne w środowiskach z dużą liczbą użytkowników (np. 200 tys.). Występuje m.in. przy wejściu do LogView i edytora uprawnień do pola.

**Decyzja (2025-10-14):**
Konieczna pilna optymalizacja - dane powinny być ładowane **leniwiej** (on-demand), dopiero gdy użytkownik faktycznie potrzebuje tych danych (np. rozwinie filtr, otworzy sekcję).

**Zadania:**
- [ ] **Kamil:** Porozmawiać z deweloperami (Filip, Przemek) o optymalizacji i lazy loading
- [ ] Korekta wywołań API w LogView
- [ ] Korekta wywołań API w edytorze uprawnień do pola

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-16 | Dodano analizę wydajności dla klienta | Rada Architektów 2025-09-16 |
| 2025-10-06 | Zmiana typów pól tekstowych VARCHAR → MEDIUMTEXT | Sprint review 2025-10-06 |
| 2025-10-14 | Problem: nadmierne pobieranie danych w widokach React (LogView, edytor uprawnień). Decyzja: pilna optymalizacja - lazy loading | Rada Architektów 2025-10-14 |

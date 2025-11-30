# System mailowy

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Integracja techniczna
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

## 4. Usprawnienia dla środowisk testowych

### Zarządzanie kolejką maili

**Status:** Propozycja zaakceptowana
**Data:** 2025-09-25

**Problem:**
Podczas testów nowych procesów, administratorzy muszą ręcznie (z poziomu bazy danych) usuwać maile z kolejki, aby uniknąć przypadkowego wysłania powiadomień do kluczowych osób (np. zarządu).

**Rozwiązanie:**
- W nowym interfejsie kolejki maili dodać możliwość **zaznaczania i usuwania wiadomości**
- Wprowadzić na poziomie definicji procesu opcję **"trybu testowego"**:
  - Przekierowanie wszystkich maili wysyłanych w ramach procesu na wskazany adres dewelopera/testera

**Decyzja (2025-09-25):**
Oba pomysły bardzo wartościowe. Zarówno możliwość ręcznego czyszczenia kolejki, jak i globalne przekierowanie maili dla danego procesu znacząco ułatwią testowanie.

---

## 5. Znane problemy

### Niespójność logiki historii wysłanych maili

**Status:** Do projektowania
**Data zgłoszenia:** 2025-09-30
**Data aktualizacji:** 2025-10-07

**Problem:**
- Nowa funkcja historii wysłanych maili rejestruje wiadomość jako "wysłaną" w momencie jej dodania do kolejki, a nie faktycznego wysłania przez serwer
- Prowadzi do niespójności: administrator widzi mail jako "wysłany", podczas gdy utknął w kolejce lub został usunięty

**Rozwiązanie (propozycja):**

Zaprojektować dwuetapową logikę zapisu do historii:
- **Etap 1:** Mail dodany do kolejki → status "w kolejce" lub "oczekuje"
- **Etap 2:** Mail faktycznie wysłany przez serwer mailowy → status "wysłany"

**Decyzja (2025-09-30):**
Problem jest złożony technicznie (maile zbiorcze, maile natychmiastowe). Wymaga głębszej analizy - zostanie zorganizowane osobne spotkanie techniczne.

**Zadania:**
- [ ] **Piotr:** Zaprojektować szczegółowe rozwiązanie dwuetapowej logiki zapisywania historii maili

---

## 6. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-25 | Usprawnienia dla środowisk testowych - usuwanie z kolejki, tryb testowy | Rada Architektów 2025-09-25 |
| 2025-09-30 | Problem niespójności historii wysłanych maili - do analizy | Rada Architektów 2025-09-30 |
| 2025-10-07 | Aktualizacja: dwuetapowa logika zapisu historii maili, Piotr do projektu | Rada Architektów 2025-10-07 |

# CHANGELOG – Historia biznesowa

---

## 2025-11-19 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Notatka projektowa - Przegląd wycen.md]
**Kategoria:** #Funkcjonalność #Design #Zadanie #Decyzja

- Klient oczekuje wyświetlania historii spraw powiązanych (Rossmann).
- Należy ustalić, czy klient potrzebuje pełnej historii technicznej, czy dedykowanej historii biznesowej.
- Spotkanie z klientem w celu ustalenia oczekiwań biznesowych.

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Notatka projektowa - Historia biznesowa.md]
**Kategoria:** #Architektura #Funkcjonalność

**Kontekst:** Przeprojektowanie mechanizmu historii biznesowej - zespół odkrył fundamentalne ograniczenia obecnej implementacji (obsługa tylko pojedynczej sprawy) i wypracował koncepcję wielowymiarowej historii.

**Dwa typy historii biznesowej:**
- **Typ 1:** Historia SPRAWY (istniejące) - kluczowe zdarzenia w jednym procesie (case MSIT)
- **Typ 2:** Historia WĄTKU/TECZKI (nowe) - śledzenie "wirtualnego bytu" przez wiele procesów (Rossmann, JRWA, Allianz)

**Kluczowe decyzje architektoniczne:**
- Dedykowana tabela `CaseEventBusinessSubjects` zamiast JSON - szybkie indeksowanie, możliwość wielu powiązań
- Typy powiązań (enum w kodzie): `case`, `user`, `client`, `jrwa_folder`, `policy`, `process`
- Mechanizm `connectedCase` - rekurencyjne ładowanie historii z powiązanych spraw (max 10 poziomów)
- Wielowymiarowość - jedno zdarzenie może mieć wiele powiązań (klient + polisa + teczka JRWA)
- Standaryzacja API `AddCaseEvent` - parametr `BusinessSubjects` jako lista obiektów
- Obsługa błędnego przypisania - zdarzenia "odpięcie" + "przypięcie" z audit trail

**UI i UX:**
- Mockup z heurystyką wyświetlania nazw procesów (tylko przy zmianie kontekstu)
- Przełącznik "Historia tej sprawy" ↔ "Historia wątku/teczki"
- Obsługa HTML w `message` (linki do dokumentów, z walidacją XSS)

**MVP w 3 pakietach:**
- MVP1: Tabela powiązań + mechanizm connectedCase (Rossmann)
- MVP2: JRWA + wielowymiarowość + widok 360° klienta
- MVP3: UI enhancements (ikony, filtry) + migracja starych zdarzeń z JSON

---

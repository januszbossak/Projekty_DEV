# CHANGELOG – Historia biznesowa

---

## 2025-12-10 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-10 Omówienie wyceny dla Neuca.md](../../../../../Notatki/Gotowe-notatki-archiwum/2025-12-10%20Omówienie%20wyceny%20dla%20Neuca.md)
**Kategoria:** #Funkcjonalność #Decyzja

- **Przedstawienie koncepcji historii biznesowej dla Neuca:** Temat bardzo się klientowi podobał - mówią że to jest coś czego potrzebują, szansa na wciągnięcie klienta w analizę i pozyskanie większego budżetu
- **Dalsze kroki:** Spotkanie z klientem - pokazanie co mamy, co kombinujemy, ustalenie jakie oni widzą sensowne zastosowania (potrzeby), możliwość współpracy z Rossmannem (szersza perspektywa)
- **Powiązanie z teczkami sprawy:** Może być powiązana z JRWA i teczkami sprawy (koncepcja teczki klienta)

---

## 2025-12-04 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-04 Spotkanie projektowe - Omówienie zmian Amodit - Neuca.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-04%20Spotkanie%20projektowe%20-%20Omówienie%20zmian%20Amodit%20-%20Neuca.md)  
**Kategoria:** #Funkcjonalność

**Prezentacja funkcjonalności dla klienta Neuca (informacyjnie):**

- Przedstawiono nową funkcjonalność "Historia Biznesowa" (AddEvent) - mechanizm zapisywania kluczowych zdarzeń biznesowych na sprawie, niezależnie od standardowej historii technicznej
- Funkcjonalność już istnieje w regułach (`AddEvent`), ale brak GUI do wyświetlania
- **Dwa warianty:**
  - Historia biznesowa na sprawie - kluczowe zdarzenia w ramach jednej sprawy (np. "ostateczna akceptacja", "wysłano do księgowości")
  - Historia międzysprawowa (Teczka sprawy) - powiązanie zdarzeń z różnych procesów dotyczących tej samej sprawy biznesowej (np. reklamacja: korespondencja przychodząca → odpowiedź wychodząca → pismo prawnika)
- Mechanizm AddEvent już działa w wersji 2.506.30 (zapisuje do bazy), ale tylko zapisywanie - brak interfejsu
- Możliwość integracji z zewnętrznymi systemami (np. call center) przez API
- **Przykłady zastosowania:** Księgowość (kto ostatecznie zaakceptował fakturę), JRWA (Teczka sprawy), Klient 360° (ubezpieczenia - historia polis, rozmów, roszczeń)

**Feedback Neuca:**
- Zespół Neuca (Tomek/Artur) już pytał o historię biznesową 2-3 tygodnie temu
- Michał Mirończuk zapytał o możliwość dodawania wpisów do standardowej historii sprawy funkcją - do przemyślenia
- Neuca zbierze uwagi i potrzeby dotyczące historii biznesowej

**Status:** Funkcjonalność w fazie kształtowania, AMODIT zbiera feedback od klientów. Rozwój GUI w trakcie.

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

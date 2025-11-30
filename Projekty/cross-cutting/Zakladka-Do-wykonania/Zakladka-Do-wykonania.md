# Project Canvas: Zakładka "Do wykonania"

**Status:** 🟡 W analizie
**Powód statusu / Bloker:** Oczekuje na analizę wydajnościową i wycenę implementacji.
**Ostatnia aktualizacja:** 2025-09-04
**Data rozpoczęcia:** 2025-08-19

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Damian Kamiński | Zarządzanie projektem |
| **Tech Lead** | Piotr Buczkowski | Weryfikacja wydajnościowa |
| **Deweloper** | [do uzupełnienia] | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Ustawienie dotyczące wyświetlania spraw, w których użytkownik jest **współpracownikiem** (a nie właścicielem), jest obecnie globalne. Powoduje to, że lista zadań "Do wykonania" staje się nieczytelna dla użytkowników, którzy są współpracownikami w wielu procesach, ale nie chcą widzieć tych zadań na swojej głównej liście. Brakuje elastyczności w konfiguracji na poziomie poszczególnych procesów.

### Cel biznesowy
Zwiększenie przejrzystości i użyteczności zakładki "Do wykonania" poprzez umożliwienie administratorom precyzyjnego decydowania, dla których procesów zadania współpracowników mają być widoczne.

### Cel techniczny
Przeniesienie konfiguracji wyświetlania zadań dla współpracowników z poziomu globalnego na poziom definicji procesu, z jednoczesnym zapewnieniem, że rozwiązanie będzie wydajne nawet przy dużej liczbie procesów.

### Metryka sukcesu
- Administratorzy mogą włączyć lub wyłączyć widoczność zadań dla współpracowników dla każdego procesu z osobna.
- Nowe rozwiązanie nie powoduje zauważalnego spadku wydajności (<5% wzrost czasu ładowania) nawet przy konfiguracji obejmującej ponad 100 procesów.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-19]] | Umożliwienie użytkownikom przeglądania spraw, w których są współpracownikami, a nie tylko właścicielami. | Zwiększa to transparentność i umożliwia lepsze śledzenie zadań w zespole. | - |
| ADR-002 | 🔍 Do weryfikacji | [[2025-09-04]] | Konfiguracja widoczności zadań dla współpracowników będzie odbywać się na poziomie procesu, poprzez listę procesów, dla których opcja ma być włączona. | Zapewnia to maksymalną elastyczność, ale wymaga weryfikacji wydajnościowej (użycie `IN` w SQL) dla dużej liczby procesów. | Opcja `NOT IN` byłaby mniej intuicyjna przy dużej liczbie procesów do wykluczenia. |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

**Ukończono:**
- ✅ Wstępna identyfikacja problemu.

**Trwa praca nad:**
- Określeniem skali problemu (liczby procesów do objęcia konfiguracją).
- Analizą wydajnościową proponowanego rozwiązania SQL.

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Wysokie]** Problemy wydajnościowe przy dużej liczbie procesów (100+) w warunku `IN` zapytania SQL. | Średnie | Wysoki | Przeprowadzenie testów wydajnościowych przez Piotra Buczkowskiego przed finalną implementacją. | Piotr Buczkowski |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-04]] | Propozycja przeniesienia konfiguracji na poziom procesu. Zlecono analizę wydajnościową. | [[2025-09-04 Rada architektów]] |
| [[2025-08-19]] | Utworzenie projektu - potrzeba uwzględnienia spraw, w których użytkownik jest współpracownikiem. | [[2025-08-19 Rada architektów]] |

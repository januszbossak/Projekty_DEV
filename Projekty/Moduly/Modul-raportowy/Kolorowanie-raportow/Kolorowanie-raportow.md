# Project Canvas: Kolorowanie raportów

**Projekt nadrzędny:** [[Modul-raportowy]]
**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-08-12
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | [do uzupełnienia] | Architektura tego podprojektu |
| **Deweloper** | Anna Skupińska | Implementacja |
| **Tester** | Janusz Bossak | Testowanie zmian |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Obecny mechanizm kolorowania wartości w raportach tabelarycznych z agregacją działa nieprawidłowo – patrzy tylko na wartości z danej strony, zamiast pobierać wszystkie wartości dla prawidłowego obliczenia gradientu kolorów. Kolorowanie oparte tylko na wartościach z aktualnej strony powoduje nieprawidłowe działanie gradientu, szczególnie dla raportów z agregacją.

### Cel biznesowy

Poprawienie mechanizmu kolorowania wartości w raportach tabelarycznych, aby kolorowanie było oparte na wszystkich wartościach w raporcie, nie tylko na wartości z aktualnej strony, zapewniając prawidłowe działanie gradientu kolorów.

### Cel techniczny

Zmodyfikowanie mechanizmu kolorowania, aby pobierał wszystkie wartości z raportu przed kolorowaniem i obliczał gradient na podstawie maksymalnej i minimalnej wartości oraz wartości zerowej z całego raportu, nie tylko z aktualnej strony.

### Metryka sukcesu

- Gradient kolorów jest obliczany na podstawie wszystkich wartości w raporcie (min/max/zero)
- Kolorowanie działa poprawnie dla raportów tabelarycznych bez agregacji (typy Pivot i mapa)

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

[Do uzupełnienia po decyzjach architektonicznych]

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-08-12 | Kolorowanie oparte na wszystkich wartościach z raportu (nie tylko z aktualnej strony) - pobieranie wszystkich wartości przed kolorowaniem | Prawidłowe działanie gradientu - kolorowanie oparte na maksymalnej i minimalnej wartości oraz wartości zerowej z całego raportu | - |
| ADR-002 | ✅ Zatwierdzone | 2025-08-12 | Gradient oparty na min/max/zero - kolorowanie oparte na maksymalnej i minimalnej wartości oraz wartości zerowej | Standardowe podejście do gradientów kolorów w wizualizacji danych | - |
| ADR-003 | ✅ Zatwierdzone | 2025-08-12 | Zakres na razie tylko dla raportów tabelarycznych bez agregacji (głównie pod wymaganie WIM i pana Piotra) - typy Pivot i mapa | Obecnie tylko dla typu Pivot i mapa, dla innych typów z agregacją kolorowanie nie ma sensu | - |
| ADR-004 | ⏸️ Odroczona | 2025-08-12 | Kolorowanie tylko dla raportów bez agregacji - ograniczenie do raportów tabelarycznych bez agregacji | Na razie tylko dla raportów bez agregacji - odroczone | - |
| ADR-005 | ⏸️ Odroczona | 2025-08-12 | Więcej opcji kolorowania - dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient) | Przyszłościowo - możliwość dzielenia zakresów na więcej elementów z różnymi kolorami | - |
| ADR-006 | ❌ Odrzucone | 2025-08-12 | Kolorowanie tylko wartości z danej strony (obecne podejście) | Nieprawidłowe działanie gradientu - kolorowanie oparte tylko na wartościach z aktualnej strony powoduje błędne obliczenia | - |
| ADR-007 | ✅ Zatwierdzone | [[2025-08-25]] | Udostępnienie użytkownikom edycji palety gradientów (kolor dla min, max i zero). | Wymaganie klienta (Piotr Murawski) - potrzeba personalizacji kolorów w raportach typu Pivot i Treemap. | - |
| ADR-008 | 💡 Propozycja | [[2025-08-25]] | Rozszerzenie edycji gradientów na inne typy wykresów (np. słupkowe). | Zwiększenie spójności i możliwości personalizacji w całym module raportowym. | - |
| ADR-009 | 💡 Propozycja | [[2025-08-25]] | Umożliwienie przesuwania punktu środkowego skali (zera) na inną wartość. | Większa elastyczność w analizie danych, gdzie punkt odniesienia może być inny niż zero. | - |
| ADR-010 | 🔍 Do weryfikacji | [[2025-08-28]] | Zmiana domyślnej palety kolorów i jej kolejności, aby pierwsze kolory były bardziej rozróżnialne (wzorem Tableau). | Poprawi to czytelność wykresów z wieloma seriami i dostępność dla osób z zaburzeniami widzenia kolorów. Wymaga konsultacji ze specjalistą ds. wizualizacji. | - |
| ADR-011 | 💡 Propozycja | [[2025-08-28]] | Wprowadzenie funkcji agregacji małych serii danych do jednej pozycji "pozostałe". | Ograniczy to liczbę kolorów na wykresie, co znacząco poprawi jego czytelność, gdy jest wiele mało znaczących serii. | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta
- ⏸️ **Odroczona** - decyzja odroczona na później

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

Projekt jest w fazie aktywnego rozwoju. Trwa rozbudowa funkcjonalności kolorów o gradienty oparte na wszystkich wartościach z raportu.

**Ukończono:**
- ✅ Implementacja edycji palety gradientów (kolor min, max, zero) dla Treemap i Pivot.
- ✅ Opcja resetowania do domyślnej palety.
- ✅ Kolorowanie z gradientem - poprawki dla Pivot i map (w testach)

**Trwa praca nad:**
- Poprawienie mechanizmu kolorowania - pobieranie wszystkich wartości przed kolorowaniem
- Gradient oparty na min/max/zero z całego raportu

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Niskie]** Problemy wydajnościowe przy pobieraniu wszystkich wartości z dużych raportów | Niskie | Średni | Mechanizm pobiera wszystkie wartości tylko dla raportów bez agregacji (typy Pivot i mapa), które są zwykle mniejsze | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Kolorowanie oparte na wszystkich wartościach (Plan: Q4 2025)

**Cel:** Poprawienie mechanizmu kolorowania wartości w raportach tabelarycznych z agregacją, aby kolorowanie było oparte na wszystkich wartościach w raporcie, nie tylko na wartości z aktualnej strony, zapewniając prawidłowe działanie gradientu kolorów.

**Definicja ukończenia (DoD):**
- Mechanizm pobiera wszystkie wartości z raportu przed kolorowaniem (nie tylko z aktualnej strony)
- Gradient jest obliczany na podstawie maksymalnej i minimalnej wartości oraz wartości zerowej z całego raportu
- Kolorowanie działa poprawnie dla raportów tabelarycznych bez agregacji (typy Pivot i mapa)

**Funkcjonalności:**

#### Mechanizm kolorowania
- [ ] Pobieranie wszystkich wartości z raportu przed kolorowaniem (nie tylko z aktualnej strony)
- [ ] Gradient oparty na min/max/zero - kolorowanie oparte na maksymalnej i minimalnej wartości oraz wartości zerowej z całego raportu
- [ ] Obsługa typów raportów: Pivot i mapa (na razie)

**Poza zakresem MVP (Out of Scope):**
- Obsługa innych typów raportów z agregacją - kolorowanie nie ma sensu dla innych typów z agregacją
- Dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient) - przyszłościowo

**Planowana data:** Q4 2025

**Zadania:**
- **Anna Skupińska:** Finalizacja zmian kolorów i gradientów (oddane do testowania na AMODIT Local)
- **Janusz Bossak:** Testowanie zmian i zwracanie uwag

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Dzielenie zakresów na więcej elementów z różnymi kolorami (nie tylko gradient) (Priorytet: Niski)
- Rozszerzenie obsługi kolorowania na inne typy raportów (Priorytet: Niski)

**Punkty do dalszej dyskusji:**
- Jak będzie wyglądać mechanizm dzielenia zakresów na więcej elementów z różnymi kolorami w przyszłości?

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Utworzenie podprojektu - decyzja o poprawieniu mechanizmu kolorowania: pobieranie wszystkich wartości przed kolorowaniem, gradient oparty na min/max/zero z całego raportu | [[Notatki/Rada architektów/2025-08-12 Rada architektów|Rada Architektów 2025-08-12]] |
| 2025-08-25 | Zaimplementowano edycję palety gradientów (kolor min, max, zero) dla Treemap i Pivot, zgodnie z wymaganiem klienta. Zaproponowano rozszerzenie na inne wykresy i przesuwanie skali. | [[2025-08-25 Sprint review]] |
| [[2025-08-28]] | Rozpoczęto dyskusję nad zmianą domyślnej palety kolorów, aby była bardziej czytelna i dostępna, wzorem Tableau. Temat skierowany do konsultacji. | [[2025-08-28 Rada architektów]] |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Modul-raportowy]]
- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]


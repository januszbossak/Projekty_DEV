# Project Canvas: Edytor formularzy

**Projekt nadrzędny:** [[Edytor-procesow]]
**Status:** 🛠️ W realizacji
**Ostatnia aktualizacja:** 2025-08-26
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | [do uzupełnienia] | Architektura tego podprojektu |
| **Deweloper** | [do uzupełnienia] | Implementacja |
| **Tester** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Stary edytor formularzy był oparty na przestarzałej technologii (WebForms), co utrudniało jego rozwój i czyniło go mało intuicyjnym dla użytkowników. Tworzenie i edycja formularzy, zwłaszcza tych bardziej złożonych, była uciążliwa, a sam interfejs nie przystawał do nowoczesnych standardów.

### Cel biznesowy
Dostarczenie nowoczesnego, intuicyjnego i wydajnego edytora formularzy, który znacząco przyspieszy pracę konsultantów i administratorów. Celem jest obniżenie progu wejścia dla nowych twórców procesów i umożliwienie im szybkiego budowania ergonomicznych formularzy.

### Cel techniczny
Przepisanie całego interfejsu edytora formularzy na technologię React. Zaimplementowanie nowego, bardziej przejrzystego layoutu z listą pól po lewej stronie, obszarem roboczym na środku i panelem właściwości po prawej. Zapewnienie kompatybilności wstecznej poprzez mechanizm przełącznika do starej wersji edytora.

### Metryka sukcesu
- Czas potrzebny na stworzenie formularza o średniej złożoności (15 pól, 2 tabelki) skrócony o 40%.
- 95% nowych formularzy tworzonych jest przy użyciu nowego edytora.

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

[Do uzupełnienia po przetworzeniu notatek]

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-08-12 | Ustawianie szerokości kolumn w pikselach (np. 50px) w definicji kolumny tabeli | Proste i intuicyjne rozwiązanie, odpowiada na częste zapytania klientów (m.in. Zbigniew Szymanowski, PKF) o możliwość ustawiania szerokości kolumn | - |
| ADR-002 | ✅ Zatwierdzone | 2025-08-12 | Zawijanie tekstu - opcja określająca, czy tekst ma się zawijać w kolumnie | Umożliwia lepszą kontrolę nad wyświetlaniem treści w kolumnach | - |
| ADR-003 | ✅ Zatwierdzone | 2025-08-12 | Ograniczona kontrola CSS - tylko wybrane właściwości (width, zawijanie tekstu), nie pełna kontrola CSS | Bezpieczne rozwiązanie - backend odczytuje tylko oczekiwane właściwości (width z odpowiednią liczbą), ignoruje wszystko inne (np. próby wstrzyknięcia JavaScript) | - |
| ADR-004 | ✅ Zatwierdzone | 2025-08-12 | Oddzielne ustawienia dla wyświetlania i dla wydruku (jak w starym systemie) | Zgodność z istniejącym podejściem, umożliwia różne ustawienia dla różnych kontekstów | - |
| ADR-005 | ✅ Zatwierdzone | 2025-08-12 | Tabelka w tabelce - nie określa się szerokości (jest w nowej linii) | Logiczne ograniczenie - zagnieżdżone tabele nie wymagają osobnej konfiguracji szerokości | - |
| ADR-006 | ❌ Odrzucone | 2025-08-12 | Brak możliwości ustawiania szerokości kolumn | Częste zapytania klientów, potrzeba elastyczności - kolumny z krótkimi wartościami (np. jednostki miary typu KG, SZT, ilości ograniczone do 999) zajmują niepotrzebnie dużo miejsca | - |
| ADR-007 | ❌ Odrzucone | 2025-08-12 | Pełna kontrola CSS (możliwość wpisania dowolnego stylu CSS) | Ryzyko bezpieczeństwa - możliwość wstrzyknięcia JavaScript | - |
| ADR-008 | ✅ Zatwierdzone | [[2025-08-26]] | Nowy edytor formularzy jest zaimplementowany w technologii React. | Zapewnia to nowoczesny, wydajny i łatwy w utrzymaniu interfejs, spójny z resztą modernizowanego systemu. | - |
| ADR-009 | ✅ Zatwierdzone | [[2025-08-26]] | Dla zapewnienia kompatybilności wstecznej, użytkownik ma możliwość przełączenia się z powrotem do starego edytora. | Minimalizuje to ryzyko dla użytkowników, którzy są przyzwyczajeni do starego interfejsu lub napotkają problem w nowym. Przełącznik jest rozwiązaniem tymczasowym na okres przejściowy. | - |
| ADR-010 | ✅ Zatwierdzone | [[2025-09-11]] | Przełącznik widoków (nowy/stary edytor, widok/edycja JSON) zostanie przeniesiony z prawego górnego rogu na dół, pod listę pól. | Poprawi to ergonomię pracy - przełącznik będzie bliżej obszaru roboczego i nie będzie kolidował z innymi elementami interfejsu w nagłówku. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji

Nowy edytor został zaimplementowany i jest w fazie wdrożenia. Trwają prace nad zbieraniem feedbacku i ewentualnymi poprawkami.

**Ukończono:**
- ✅ Implementacja nowego layoutu w React.
- ✅ Funkcjonalność drag-and-drop dla pól.
- ✅ Panel właściwości dla konfigurowania pól.
- ✅ Przełącznik do starej wersji edytora.

**Trwa praca nad:**
- Zbieraniem feedbacku od użytkowników.

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| - | - | - | - | - |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Ustawianie szerokości kolumn w formularzu (Plan: [do uzupełnienia])

**Cel:** Umożliwienie użytkownikom dostosowania szerokości kolumn w tabelach w formularzu, eliminując problem niepotrzebnie szerokich kolumn z krótkimi wartościami (np. jednostki miary typu KG, SZT, ilości ograniczone do 999).

**Definicja ukończenia (DoD):**
- Użytkownik może ustawić szerokość kolumny w pikselach (np. 50px) w definicji kolumny tabeli
- Użytkownik może określić, czy tekst ma się zawijać w kolumnie
- Backend bezpiecznie interpretuje tylko oczekiwane właściwości CSS (width, zawijanie), ignorując resztę
- Oddzielne ustawienia dla wyświetlania i dla wydruku

**Funkcjonalności:**

#### Konfiguracja szerokości kolumn
- [ ] Możliwość wpisania szerokości kolumny w pikselach (np. 50px) w definicji kolumny tabeli
- [ ] Opcja określająca, czy tekst ma się zawijać w kolumnie
- [ ] Oddzielne ustawienia dla wyświetlania i dla wydruku (jak w starym systemie)

#### Bezpieczeństwo
- [ ] Backend odczytuje tylko oczekiwane właściwości (width z odpowiednią liczbą), ignoruje wszystko inne (np. próby wstrzyknięcia JavaScript)
- [ ] Weryfikacja bezpieczeństwa - testy weryfikujące, że nie można wstrzyknąć złośliwego kodu przez CSS

**Poza zakresem MVP (Out of Scope):**
- Tabelka w tabelce - nie określa się szerokości (jest w nowej linii)
- Pełna kontrola CSS - tylko wybrane właściwości (width, zawijanie tekstu)

**Planowana data:** [do uzupełnienia]

**Zadania:**
- **Piotr Buczkowski:** Implementacja możliwości ustawiania szerokości kolumn w formularzu zgodnie z ustaleniami
- **Anna Skupińska:** Testy bezpieczeństwa – weryfikacja, że nie można wstrzyknąć złośliwego kodu przez CSS

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Rozszerzenie o więcej właściwości CSS w przyszłości (Priorytet: Niski)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-11-28 | Utworzenie podprojektu - reset dokumentacji | Reorganizacja dokumentacji |
| 2025-08-12 | Decyzja o wprowadzeniu możliwości ustawiania szerokości kolumn w formularzu - szerokość w pikselach, zawijanie tekstu, ograniczona kontrola CSS ze względów bezpieczeństwa | [[Notatki/Rada architektów/2025-08-12 Rada architektów\|Rada Architektów 2025-08-12]] |
| [[2025-08-26]] | Wdrożono nowy edytor formularzy w React z nowym layoutem. Dodano przełącznik kompatybilności do starej wersji. | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| [[2025-09-11]] | Zgłoszono sugestię poprawy UX poprzez przeniesienie przełącznika widoków w inne, bardziej ergonomiczne miejsce. | [[2025-09-11 Rada architektów]] |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Edytor-procesow]]
- **Projekty powiązane:** [[Matryca-uprawnien]] (zarządzanie uprawnieniami do pól formularza)
- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]

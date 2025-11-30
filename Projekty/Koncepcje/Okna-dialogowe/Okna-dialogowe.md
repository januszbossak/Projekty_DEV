# Project Canvas: Okna dialogowe

**Status:** 🟡 W analizie
**Powód statusu / Bloker:** Koncepcja wymaga dalszej analizy i sprecyzowania wymagań przed rozpoczęciem implementacji
**Ostatnia aktualizacja:** 2024-04-16
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2024-04-16
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | [do uzupełnienia] | Implementacja |
| **Tester** | [do uzupełnienia] | |
| **Opiekun handlowy** | [do uzupełnienia] | |
| **Klient (Decydent)** | [do uzupełnienia] | Akceptacja MVP, ostateczne decyzje biznesowe |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Obecny mechanizm zbierania danych od użytkownika w trakcie wykonywania procesu jest zbyt ograniczony. Okno potwierdzania reguły ręcznej nie pozwala na zbieranie wielu pól danych, co uniemożliwia realizację bardziej złożonych scenariuszy interakcji z użytkownikiem bez konieczności tworzenia pełnej sprawy.

### Cel biznesowy

Dostarczenie elastycznego mechanizmu okien dialogowych umożliwiającego zbieranie danych od użytkownika w trakcie procesu, dostosowanego do różnych poziomów złożoności - od prostych pytań po bardziej zaawansowane formularze, bez konieczności tworzenia pełnej sprawy w systemie.

### Cel techniczny

Wprowadzenie funkcjonalności `ShowDialog()` umożliwiającej wyświetlanie uproszczonych okien dialogowych z różnymi poziomami złożoności - od prostych pól definiowanych w wywołaniu po pełnoprawne formularze oparte na procesach, z możliwością zwracania danych w formacie JSON.

### Metryka sukcesu

- Użytkownik może zebrać dane od użytkownika końcowego **bez tworzenia sprawy** w prostych scenariuszach
- Czas interakcji z oknem dialogowym **< 30 sekund** dla prostych przypadków użycia
- Dane z okna dialogowego są dostępne w formacie JSON **natychmiast po zamknięciu okna**

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Uproszczony interfejs okna dialogowego

Okno dialogowe musi być maksymalnie uproszczone - bez prawego panelu, załączników, spraw powiązanych, historii oraz innych elementów charakterystycznych dla pełnego formularza sprawy.

**Uzasadnienie:** Okno dialogowe służy do szybkiej interakcji z użytkownikiem, a pełny interfejs formularza sprawy byłby przeładowany i mylący dla prostych scenariuszy użycia.

### Zasada 2: Format zwracanych danych jako JSON

Dane zebrane w oknie dialogowym są zwracane jako obiekt JSON, który może być konsumowany przez formularz główny lub reguły procesu.

**Uzasadnienie:** Format JSON zapewnia elastyczność w przetwarzaniu danych i łatwą integrację z istniejącymi mechanizmami systemu.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | 💡 Propozycja | 2024-04-16 | Wprowadzenie trzech wariantów okien dialogowych o różnym poziomie złożoności: proste okno (bez procesu), okno na podstawie formularza (proces-formularz), okno na podstawie procesu (pełny proces) | Różne scenariusze użycia wymagają różnych poziomów złożoności - od prostych pytań po zaawansowane formularze z regułami | - |
| ADR-002 | 💡 Propozycja | 2024-04-16 | Proste okno dialogowe jako rozwinięcie "okna potwierdzania reguły ręcznej" z polami definiowanymi w wywołaniu (tekst, data, liczba, użytkownik, słownik) | Najprostsze rozwiązanie dla podstawowych interakcji, gdzie dane są natychmiast używane po zamknięciu okna | - |
| ADR-003 | 💡 Propozycja | 2024-04-16 | Okno dialogowe na podstawie formularza wymaga definicji procesu typu "proces-formularz" bez tworzenia sprawy (bez caseID) | Pozwala na bardziej złożone interakcje bez konieczności persystencji danych w bazie | - |
| ADR-004 | ⏸️ Odroczona | 2024-04-16 | Okno dialogowe na podstawie pełnoprawnego procesu z formularzem, regułami i diagramem | Najbardziej złożone rozwiązanie wymagające pełnej definicji procesu - odroczone jako zaawansowana funkcjonalność | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

Koncepcja okien dialogowych jest w fazie analizy. Zdefiniowano trzy warianty rozwiązania odpowiadające różnym poziomom złożoności, jednak wymagają one dalszego sprecyzowania wymagań i szczegółowej specyfikacji technicznej przed rozpoczęciem implementacji.

**Ukończono:**
- ✅ Zdefiniowano trzy warianty okien dialogowych o różnym poziomie złożoności
- ✅ Określono podstawowe założenia techniczne (funkcja `ShowDialog()`, format JSON, uproszczony UI)

**Trwa praca nad:**
- [ ] Szczegółowa specyfikacja wymagań dla prostego okna dialogowego
- [ ] Określenie sposobu konsumpcji danych z okna dialogowego przez formularz główny
- [ ] Definicja procesu typu "proces-formularz" dla wariantu drugiego
- [ ] Prototyp UI dla uproszczonego okna dialogowego

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Brak jasnej definicji formatu danych JSON i sposobu ich konsumpcji przez formularz główny | Średnie | Średni | Przeprowadzenie szczegółowej analizy wymagań przed implementacją, określenie przykładowych scenariuszy użycia | Tech Lead |
| **[Średnie]** Nieokreślone akcje/przyciski dostępne w oknie dialogowym poza prostymi przyciskami | Średnie | Średni | Zdefiniowanie minimalnego zestawu akcji dla każdego wariantu okna dialogowego | Tech Lead |
| **[Niskie]** Walidacja pól w prostym oknie dialogowym może być niewystarczająca dla złożonych scenariuszy | Niskie | Niski | Określenie zasad walidacji dla każdego typu pola w prostym oknie dialogowym | Tech Lead |

---

### Punkty wymagające decyzji (w fazie analizy)

**Format danych i konsumpcja:**
- [ ] Jak przekazywać dane z okna dialogowego do głównego formularza? (przypisanie do pól vs obiekt JSON)
- [ ] Jaki jest dokładny format obiektu JSON zwracanego z okna dialogowego?

**Interfejs użytkownika:**
- [ ] Które elementy UI pozostawić w uproszczonym oknie dialogowym?
- [ ] Jak definiować akcje/przyciski w oknie dialogowym?

**Architektura:**
- [ ] Czy potrzebny jest nowy typ procesu "proces-formularz"?
- [ ] Jak obsłużyć walidację pól w prostym oknie dialogowym (Wariant 1)?

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Proste okno dialogowe" (Plan: [do uzupełnienia])

**Cel:** Dostarczenie najprostszego mechanizmu zbierania danych od użytkownika bez konieczności definiowania procesu lub formularza, jako rozwinięcie obecnego "okna potwierdzania reguły ręcznej".

**Definicja ukończenia (DoD):**
- Użytkownik może wywołać okno dialogowe z poziomu reguły procesu funkcją `ShowDialog()` z polami zdefiniowanymi w wywołaniu
- Okno wyświetla pola: tekst, data, liczba, użytkownik, słownik (opcjonalnie)
- Dane z okna są dostępne natychmiast po zamknięciu okna w formacie JSON
- Uproszczony interfejs bez prawego panelu, załączników, historii

**Funkcjonalności:**

#### Podstawowe funkcjonalności
- [ ] Funkcja `ShowDialog()` z parametrami definiującymi pola
- [ ] Obsługa typów pól: tekst, data, liczba, użytkownik, słownik
- [ ] Zwracanie danych w formacie JSON po zamknięciu okna
- [ ] Uproszczony interfejs okna dialogowego

#### Walidacja i obsługa błędów
- [ ] Walidacja pól zgodnie z ich typem
- [ ] Obsługa anulowania okna dialogowego
- [ ] Obsługa błędów walidacji

**Poza zakresem MVP (Out of Scope):**
- Okno dialogowe na podstawie formularza (Wariant 2)
- Okno dialogowe na podstawie procesu (Wariant 3)
- Zaawansowane akcje w oknie dialogowym poza podstawowymi przyciskami

**Planowana data:** [do uzupełnienia]

---

### 📦 MVP2: "Okno dialogowe na podstawie formularza" (Plan: [do uzupełnienia])

**Cel:** Rozszerzenie funkcjonalności o możliwość wykorzystania formularza zdefiniowanego w procesie typu "proces-formularz" do wyświetlenia okna dialogowego bez tworzenia sprawy.

**Definicja ukończenia (DoD):**
- Zdefiniowano nowy typ procesu "proces-formularz"
- Wywołanie `ShowDialog("nazwa formularza", ...)` otwiera formularz bez tworzenia sprawy (bez caseID)
- Dane z formularza są zwracane jako obiekt JSON
- Uproszczony interfejs okna (bez prawego panelu, załączników, historii)

**Funkcjonalności:**
- [ ] Nowy typ procesu "proces-formularz"
- [ ] Wywołanie okna dialogowego z nazwą formularza
- [ ] Wyświetlanie formularza bez tworzenia sprawy
- [ ] Zwracanie danych formularza jako JSON
- [ ] Definiowanie akcji/przycisków w procesie-formularzu

**Planowana data:** [do uzupełnienia]

---

### 📦 MVP3: "Okno dialogowe na podstawie procesu" (Plan: [do uzupełnienia])

**Cel:** Pełnoprawne okno dialogowe oparte na pełnym procesie z formularzem, regułami i diagramem, gdzie sprawy są tworzone i zapisywane w bazie danych, ale interfejs pozostaje uproszczony.

**Funkcjonalności:**
- [ ] Wywołanie okna dialogowego z pełnym procesem
- [ ] Tworzenie sprawy z caseID w tle
- [ ] Pełna funkcjonalność procesu (reguły, diagram)
- [ ] Uproszczony interfejs okna (bez prawego panelu, załączników, historii)
- [ ] Zwracanie danych sprawy jako JSON

**Planowana data:** [do uzupełnienia]

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Zaawansowane akcje w oknie dialogowym poza podstawowymi przyciskami (Priorytet: Średni)
- Obsługa zagnieżdżonych okien dialogowych (Priorytet: Niski)
- Szablony okien dialogowych do wielokrotnego użycia (Priorytet: Niski)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2024-04-16 | Utworzenie koncepcji okien dialogowych - zdefiniowano trzy warianty rozwiązania o różnym poziomie złożoności: proste okno (bez procesu), okno na podstawie formularza (proces-formularz), okno na podstawie procesu (pełny proces). Określono podstawowe założenia techniczne: funkcja ShowDialog(), format JSON, uproszczony UI | [[Notatki/Rada architektów/2024-04-16 Rada architektów|Rada Architektów 2024-04-16]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Inicjatywa w backlogu:** [do uzupełnienia]


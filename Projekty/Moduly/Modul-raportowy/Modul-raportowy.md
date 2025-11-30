# Project Canvas: Moduł raportowy

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-08-12
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** [do uzupełnienia]
**Budżet/Czas:** [do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead / Deweloper** | Łukasz, Ania, Damian, Marek | Architektura, implementacja |
| **Tester** | Janusz | |
| **Opiekun handlowy** | [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Użytkownicy AMODIT potrzebują elastycznego narzędzia do analizy danych biznesowych i prezentacji wyników w formie wykresów, tabel i dashboardów. Obecny moduł raportowy wymaga ciągłych ulepszeń w zakresie użyteczności, personalizacji wizualizacji oraz integracji z zewnętrznymi narzędziami (np. podpis elektroniczny).

### Cel biznesowy

Dostarczenie nowoczesnego, intuicyjnego modułu raportowego umożliwiającego użytkownikom biznesowym samodzielne tworzenie, konfigurowanie i personalizowanie zaawansowanych raportów bez pomocy działu IT.

### Cel techniczny

Ciagła rozbudowa i modernizacja modułu raportowego o nowe typy wizualizacji, mechanizmy personalizacji (palety kolorów, tłumaczenia, aliasy) oraz integrację z usługami zewnętrznymi (SimplySign, DevExtreme).

### Metryka sukcesu

- Użytkownik biznesowy może samodzielnie stworzyć funkcjonalny raport z wykresem **w < 10 minut**
- Administratorzy mogą dostosować etykiety i nazwy kolumn **bez modyfikacji źródeł danych**
- Użytkownik może podpisać masowo dokumenty z raportu **bez przełączania się do innego modułu**

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Wykorzystanie biblioteki DevExtreme

Moduł raportowy opiera się na komercyjnej bibliotece **DevExtreme** do renderowania wykresów i zaawansowanych komponentów UI. Utrzymanie aktualnej wersji biblioteki jest krytyczne dla stabilności, bezpieczeństwa i dostępu do nowych funkcjonalności (w tym dostępności WCAG).

**Uzasadnienie:** DevExtreme zapewnia szeroki zakres typów wykresów, interaktywność i wysoką jakość wizualizacji. Migracja na inną bibliotekę wiązałaby się z ogromnym kosztem przepisania modułu.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-10-09 | Klucz licencyjny DevExtreme (od v23) umieszczony w kodzie front-endowym jest zgodny z polityką dostawcy | Oficjalna dokumentacja DevExtreme potwierdza, że klucze licencyjne dla aplikacji JavaScript są publiczne i powinny być umieszczone w kodzie zgodnie z instrukcją dostawcy | - |
| ADR-002 | ✅ Zatwierdzone | 2025-10-09 | Ania zostaje wyznaczona jako oficjalny opiekun biblioteki DevExtreme | Konieczność wyznaczenia osoby odpowiedzialnej za monitorowanie zmian, zgłaszanie błędów do wsparcia oraz dbanie o aktualizacje biblioteki | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-08]] | Umożliwić administratorom kopiowanie raportów systemowych i zapisywanie ich jako własne raporty ("Zapisz jako"). | Daje to elastyczność w dostosowywaniu raportów systemowych do własnych potrzeb bez ryzyka nadpisania zmian podczas aktualizacji systemu. | - |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji (ciągły rozwój)

Moduł raportowy jest w fazie aktywnego rozwoju i ciągłych ulepszeń. Wiele kluczowych funkcjonalności zostało wdrożonych i działa na produkcji. Zespół dostarcza iteracyjne ulepszenia w ramach sprintów.

**Ukończono:**
- ✅ Edycja palety gradientów (personalizacja kolorystyki)
- ✅ Filtry wymagane i domyślne (wydajność dla dużych zbiorów)
- ✅ Masowe podpisywanie dokumentów SimplySign
- ✅ Kolorowanie z gradientem - poprawki dla Pivot i map (w testach)

**Trwa praca nad:**
- Usprawnienia raportów Gantt (etykiety, tooltip)
- Tłumaczenia i aliasy dla etykiet w raportach (3 etapy)
- Usprawnienie filtru "w miesiącu" (ukrycie wyboru roku)
- Rozbudowa funkcjonalności kolorów o gradienty oparte na wszystkich wartościach

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Paleta kolorów na wykresach - brak konsensusu | Średnie | Średni | Odroczone - wymaga konsultacji ze specjalistą ds. wizualizacji (Michał Maliszewski). Obecna paleta działa, nie blokuje wdrożenia | Tech Lead |
| **[Niskie]** Funkcjonalność join po polach Odnośnik może nie działać | Niskie | Niski | Do weryfikacji przez Łukasza - podejrzenie że została zaimplementowana ale jest wadliwa | Tech Lead |
| **[Średnie]** Bug: błąd pobierania danych przy ukrytych kolumnach | Średnie | Średni | Gdy kolumny są widoczne tylko dla konkretnych osób - system wyrzuca błąd zamiast pustej wartości. Damian opisuje problem. [[Rada architektów 2025-10-21\|Źródło]] | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

Moduł raportowy jest rozwijany iteracyjnie przez podprojekty. Szczegóły poszczególnych funkcjonalności znajdują się w dokumentacji podprojektów.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-12 | Reorganizacja projektu - podział na podprojekty: Kolorowanie-raportow, Masowe-podpisywanie, Gantt, Tłumaczenia-i-aliasy, Filtry, Heatmapa | Reorganizacja dokumentacji |
| 2025-10-09 | Decyzje o DevExtreme: klucz licencyjny w kodzie publicznym jest OK, Ania jako opiekun biblioteki | [[Rada architektów 2025-10-09]] |
| [[2025-08-26]] | Seria usprawnień: dodanie filtru zakresu dat, przycisków "Wyczyść" i "Zastosuj" we wszystkich filtrach oraz usprawnienie masowego podpisywania (wskazanie konkretnej kolumny). | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| [[2025-09-08]] | Wdrożono funkcję "Zapisz jako" dla raportów systemowych, umożliwiając administratorom ich kopiowanie i modyfikację. | [[2025-09-08 Sprint review]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]
- **Dokumentacja zewnętrzna:** [do uzupełnienia]
- **Use Cases:** `projekty/UC moduł raportowy/`
- **Inicjatywa w backlogu:** [do uzupełnienia]

---

## 7. PODPROJEKTY

| Podprojekt | Status | MVP | Opis |
|------------|--------|-----|------|
| [Kolorowanie-raportow](./Kolorowanie-raportow/) | 🟢 W realizacji | MVP1 Q4 2025 | Funkcjonalność kolorów - edycja palet gradientów, kolorowanie warunkowe w Pivot, kolorowanie oparte na wszystkich wartościach (nie tylko strona) |
| [Masowe-podpisywanie](./Masowe-podpisywanie/) | ✅ Ukończone | MVP1 Q4 2025 | Masowe podpisywanie dokumentów SimplySign bezpośrednio z modułu raportów |
| [Gantt](./Gantt/) | 🟢 W realizacji | MVP1 Q4 2025 | Ulepszenia wykresów Gantt - poprawki etykiet i tooltip na agregowanych belkach |
| [Tłumaczenia-i-aliasy](./Tłumaczenia-i-aliasy/) | 🟢 W realizacji | MVP1 Q4 2025 | Tłumaczenia etykiet i aliasy kolumn - eliminacja niezrozumiałych nazw technicznych (3 etapy) |
| [Filtry](./Filtry/) | ✅ Częściowo ukończone | MVP1 Q4 2025 | Filtry wymagane i domyślne dla dużych zbiorów danych, filtr "w miesiącu" |
| [Tabelki-edytowalne-w-raportach](./Tabelki-edytowalne-w-raportach/) | 🔍 Do weryfikacji | - | Umożliwienie edycji danych (np. checkboxy, komórki) bezpośrednio w widoku raportu |
| [Heatmapa](./Heatmapa/) | 🟢 W realizacji | MVP1 [do uzupełnienia] | Nowy typ wykresu Heatmapa bazujący na bibliotece AmCharts |

**Uwaga:** Każdy podprojekt ma własny katalog i pełną dokumentację Project Canvas. Zobacz `SZABLON-PODPROJEKT.md`.

---

## X. ARCHITEKTURA TECHNICZNA

### Technologie

- **Frontend:** React, DevExtreme
- **Backend:** [do uzupełnienia]
- **Baza danych:** MSSQL

### Biblioteka DevExtreme

**Wersja:** v23+ (wymaga klucza licencyjnego)

**Rola w architekturze:**
Biblioteka DevExtreme stanowi fundament modułu raportowego, zapewniając renderowanie zaawansowanych wykresów, komponentów UI oraz mechanizmów interaktywności. Jest to komercyjna biblioteka JavaScript wymagająca licencji.

**Zarządzanie licencją:**
- Klucz licencyjny dla aplikacji JavaScript ma charakter publiczny i jest umieszczany w kodzie front-endowym zgodnie z oficjalną dokumentacją dostawcy
- Nie stanowi to zagrożenia bezpieczeństwa - jest to standardowa praktyka potwierdzona przez producenta
- **Opiekun biblioteki:** Ania
  - Monitorowanie nowych wersji i zmian w bibliotece
  - Zgłaszanie błędów do wsparcia technicznego dostawcy
  - Dbanie o aktualizacje i utrzymanie biblioteki

**Plan aktualizacji:**
- Zakup najnowszej wersji licencji (inicjacja: Janusz)
- Umożliwi dostęp do poprawek błędów i nowych funkcjonalności (w tym ulepszeń WCAG)

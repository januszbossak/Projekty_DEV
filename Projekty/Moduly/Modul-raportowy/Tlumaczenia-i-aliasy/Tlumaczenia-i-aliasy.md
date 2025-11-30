# Project Canvas: Tłumaczenia i aliasy w raportach

**Projekt nadrzędny:** [[Modul-raportowy]]
**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-09
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Łukasz Bott | Analiza, wymagania |
| **Deweloper** | Marek Dziakowski, Anna Skupińska | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Raporty często prezentują dane z etykietami w języku angielskim (np. "count", "sum") lub technicznymi nazwami kolumn ze źródeł danych. Powoduje to niespójność wizualną (mieszanka języków) i utrudnia zrozumienie raportów przez użytkowników biznesowych, którzy nie znają technicznego nazewnictwa. Brakuje też możliwości nadania własnej, biznesowej nazwy dla agregacji (np. "Liczba faktur" zamiast "sum(ID)").

### Cel biznesowy
Zapewnienie, że raporty będą w pełni zrozumiałe dla użytkowników biznesowych, poprzez wyświetlanie wszystkich etykiet w ich języku oraz umożliwienie dostosowania nazw do konkretnego kontekstu biznesowego danego raportu.

### Cel techniczny
Zaprojektowanie i wdrożenie wieloetapowego, systemowego rozwiązania do obsługi tłumaczeń i aliasów w raportach. Mechanizm musi być spójny z istniejącymi rozwiązaniami w AMODIT (np. tłumaczenia w procesach) i obejmować zarówno tłumaczenia globalne, jak i aliasy na poziomie pojedynczego raportu.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-09]] | Rozwiązanie zostanie wdrożone w kilku etapach (MVP i kolejne kroki), zaczynając od najprostszych poprawek. | Umożliwia to szybkie dostarczenie wartości (poprawa istniejących tłumaczeń) i stopniowe budowanie kompletnego rozwiązania bez blokowania innych prac. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-09]] | Tłumaczenia nazw kolumn będą zarządzane centralnie, na poziomie źródła danych, analogicznie do tłumaczeń pól w procesach. | Jest to rozwiązanie systemowe. Raz zdefiniowane tłumaczenie będzie spójne we wszystkich raportach korzystających z danego źródła, co eliminuje redundancję i ryzyko niespójności. Definiowanie tłumaczeń per raport byłoby niepraktyczne. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-09]] | Należy wprowadzić możliwość nadawania własnych etykiet (aliasów) dla agregacji na poziomie konfiguracji konkretnego raportu. | Jest to kluczowe wymaganie biznesowe. Pozwala dostosować nazewnictwo do specyfiki raportu (np. "Ilość rekordów" vs "Liczba faktur" dla tej samej agregacji `count`). | - |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Podstawowe tłumaczenia"

1.  **Wyświetlanie istniejących tłumaczeń:** Naprawa błędu, który powoduje, że istniejące, zdefiniowane w systemie tłumaczenia agregacji (count, sum, min, max) nie są poprawnie wyświetlane.
2.  **Tłumaczenia systemowe agregacji:** Zapewnienie, że podstawowe agregacje są tłumaczone globalnie w zależności od języka interfejsu.
3.  **Tłumaczenia kolumn na poziomie źródła danych:** Rozbudowa mechanizmu źródeł danych o możliwość definiowania tłumaczeń dla poszczególnych kolumn, analogicznie jak w procesach.

### 📦 Wersja 2: "Aliasy per raport"
4.  **Własne etykiety dla agregacji:** Dodanie w interfejsie konfiguracji raportu (np. przy osiach wykresu) pola pozwalającego na nadanie własnej, biznesowej nazwy dla funkcji agregującej.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-12]] | Utworzenie podprojektu w ramach reorganizacji Modułu Raportowego. | Reorganizacja dokumentacji |
| [[2025-09-09]] | Zdefiniowano problem braku tłumaczeń i aliasów w raportach. Opracowano wieloetapowy plan wdrożenia, rozdzielając go na MVP (poprawki i tłumaczenia systemowe) i dalszy rozwój (aliasy per raport). | [[2025-09-09 Rada architektów]] |

---

## 6. PRZYDATNE LINKI
- **Projekt nadrzędny:** [[Modul-raportowy]]

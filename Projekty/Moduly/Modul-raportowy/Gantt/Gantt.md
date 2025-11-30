# Project Canvas: Wykresy Gantta

**Projekt nadrzędny:** [[Modul-raportowy]]
**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-09
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Deweloper** | Marek Dziakowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Wykresy Gantta, kluczowe narzędzie do wizualizacji harmonogramów, są nieczytelne i wprowadzają w błąd. Na agregowanych belkach (np. grupujących zadania w projekcie) etykiety, zakresy dat i sumaryczna liczba dni są błędnie kopiowane z pierwszego podrzędnego elementu, zamiast być poprawnie obliczane. Powoduje to, że dane na wykresie są niewiarygodne.

### Cel biznesowy
Dostarczenie wiarygodnych i czytelnych wykresów Gantta, które poprawnie agregują i wizualizują dane hierarchiczne. Użytkownicy muszą mieć pewność, że widzą na wykresie poprawne ramy czasowe i podsumowania dla grup zadań.

### Cel techniczny
Poprawa logiki generowania agregowanych belek w komponencie Gantta (DevExtreme). Należy usunąć mylące etykiety z belek i zapewnić, że dane wyświetlane w tooltipie (zakres dat, liczba dni) są poprawnie wyliczane na podstawie wszystkich podrzędnych elementów.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-09]] | Etykiety tekstowe zostaną całkowicie usunięte z agregowanych belek (zielonych). | Nie istnieje sensowny sposób na agregację etykiet tekstowych (np. nazw zadań). Wyświetlanie etykiety z pierwszego elementu jest mylące. Informacje będą dostępne w tooltipie. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-09]] | Tooltip na agregowanej belce musi pokazywać poprawnie wyliczone dane: zakres dat (od min do max) i sumaryczną liczbę dni ze WSZYSTKICH podrzędnych elementów. | Jest to kluczowa poprawka, która przywraca wiarygodność danych prezentowanych na wykresie. Obecne kopiowanie danych z pierwszego elementu jest błędem. | - |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-12]] | Utworzenie podprojektu w ramach reorganizacji Modułu Raportowego. | Reorganizacja dokumentacji |
| [[2025-09-09]] | Zdiagnozowano problem z błędnym wyświetlaniem etykiet i danych na agregowanych belkach Gantta. Zatwierdzono plan naprawy (usunięcie etykiet, poprawne obliczanie danych w tooltipie). | [[2025-09-09 Rada architektów]] |

---

## 6. PRZYDATNE LINKI
- **Projekt nadrzędny:** [[Modul-raportowy]]

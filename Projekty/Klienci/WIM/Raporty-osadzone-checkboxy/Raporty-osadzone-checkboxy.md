# Project Canvas: Raporty osadzone - checkboxy

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-11
**Klient:** WIM
**Data rozpoczęcia:** 2025-08-28

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Piotr Buczkowski | Analiza i PoC |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klient WIM zgłosił potrzebę interaktywnej edycji danych prezentowanych w raportach osadzonych na formularzu sprawy. Konkretnie, użytkownicy chcą mieć możliwość zaznaczania i odznaczania opcji (checkboxów) bezpośrednio w widoku raportu, a wprowadzone zmiany powinny być natychmiastowo zapisywane w bazie danych.

### Cel biznesowy
Usprawnienie i przyspieszenie procesu pracy użytkowników klienta WIM poprzez wyeliminowanie konieczności przechodzenia do innych ekranów lub otwierania dodatkowych formularzy w celu edycji prostych danych binarnych (tak/nie).

### Cel techniczny
Przygotowanie Proof of Concept (PoC) implementacji edytowalnych checkboxów w raportach osadzonych. Rozwiązanie będzie bazować na istniejącej technologii "starych raportów". Funkcjonalność ta zostanie wydzielona do nowego, dedykowanego modułu [[Modul-raportowy-stary]], aby oddzielić ją od nowoczesnego silnika raportowego.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-28]] | Utworzenie projektu w odpowiedzi na zapytanie klienta WIM. | [[2025-08-28 Rada architektów]] |
| [[2025-09-11]] | Podjęto decyzję o konieczności przygotowania PoC. Jednocześnie, aby zachować porządek architektoniczny, postanowiono wydzielić tę funkcjonalność do nowego modułu [[Modul-raportowy-stary]], dedykowanego "starym raportom". | [[2025-09-11 Rada architektów]] |

---

## 6. PRZYDATNE LINKI
- **Projekt technologiczny:** [[Modul-raportowy-stary]]

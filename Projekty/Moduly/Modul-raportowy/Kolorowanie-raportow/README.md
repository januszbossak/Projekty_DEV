# Kolorowanie raportów

**Projekt nadrzędny:** [[Modul-raportowy]]
**Status:** 🟢 W realizacji
**Deweloper:** Anna Skupińska
**Tester:** Janusz Bossak
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja

📄 **Project Canvas:** [[Kolorowanie-raportow]]

---

## Szybki przegląd

### Problem

Obecny mechanizm kolorowania wartości w raportach tabelarycznych z agregacją działa nieprawidłowo – patrzy tylko na wartości z danej strony, zamiast pobierać wszystkie wartości dla prawidłowego obliczenia gradientu kolorów.

### Rozwiązanie

Poprawienie mechanizmu kolorowania - pobieranie wszystkich wartości z raportu przed kolorowaniem, gradient oparty na min/max/zero z całego raportu.

### Obecna faza

🛠️ **W realizacji** - rozbudowa funkcjonalności kolorów o gradienty oparte na wszystkich wartościach

**Ukończono:**
- ✅ Edycja palety gradientów
- ✅ Kolorowanie z gradientem - poprawki dla Pivot i map (w testach)

**W trakcie:**
- Poprawienie mechanizmu - pobieranie wszystkich wartości przed kolorowaniem

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Kolorowanie oparte na wszystkich wartościach** | Prawidłowe działanie gradientu - kolorowanie oparte na min/max/zero z całego raportu |
| **Zakres tylko dla raportów bez agregacji** | Obecnie tylko dla typu Pivot i mapa, dla innych typów z agregacją kolorowanie nie ma sensu |

---

## MVP1: Kolorowanie oparte na wszystkich wartościach

**Cel:** Poprawienie mechanizmu kolorowania - gradient oparty na wszystkich wartościach z raportu

**Zakres:**
- [ ] Pobieranie wszystkich wartości przed kolorowaniem
- [ ] Gradient oparty na min/max/zero z całego raportu
- [ ] Obsługa typów Pivot i mapa

**Planowana data:** Q4 2025

---

## Szybkie linki

- Projekt nadrzędny: [[Modul-raportowy]]
- Repozytorium: [do uzupełnienia]


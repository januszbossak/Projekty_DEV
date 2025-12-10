---
created: 2025-12-09
last_updated: 2025-12-09
status: w_realizacji
---

# Repozytorium plików (DMS)

> **Status:** 🛠️ W realizacji
> **Klient:** WIM (oraz inni klienci AMODIT)
> **Projekt nadrzędny:** [[AMODIT]] *(implicit)*

**Zespół:**
- **PDM:** Damian Kamiński
- **Tech Lead:** Piotr Buczkowski
- **Deweloperzy:** Filip (Frontend/AI), Adrian (Backend), Ania (Backend), Mateusz (DB)
- **QA:** Oktawia

---

## Po co to robimy

### Problem
Klienci (głównie WIM) potrzebują centralnego miejsca do przechowywania dokumentów, które nie są bezpośrednio związane z żadną konkretną sprawą workflow (np. szablony dokumentów, regulaminy, dokumentacja ISO, pliki korporacyjne). Obecnie wymusza to tworzenie "sztucznych" spraw tylko po to, by przechować załącznik, co jest nieintuicyjne.

### Cele biznesowe

1.  **Centralizacja wiedzy:** Stworzenie jednego miejsca na pliki organizacyjne niezależnego od procesów.
2.  **Elastyczność uprawnień:** Umożliwienie nadawania uprawnień do całych struktur (przestrzeni) dla grup użytkowników.
3.  **Szybkość dostępu:** Znalezienie dokumentu w czasie < 5 sekund dzięki wyszukiwaniu pełnotekstowemu.
4.  **Skalowalność:** Możliwość przechowywania tysięcy dokumentów w zagnieżdżonych strukturach (do 20 poziomów).

### Metryki sukcesu

- **Czas wyszukiwania:** Użytkownik znajduje dokument w < 5 sekund (Lucene).
- **Czas konfiguracji:** Administrator konfiguruje nową przestrzeń dla działu w < 2 minuty.
- **Adopcja:** Odbiór wdrożenia MVP przez WIM w grudniu 2025.
- **Efektywność:** Skrócenie czasu wytwarzania o 50% dzięki wykorzystaniu AI (Filip).

**Źródła:** [[2025-11-30 Spotkanie projektowe]], [[2025-10-28 Spotkanie projektowe - Design]]

---

## Budżet i timeline

| Parametr | Wartość |
|----------|---------|
| **Start projektu** | 2025-10-28 |
| **MVP1 (WIM)** | Grudzień 2025 (wymóg kontraktowy) |
| **Podejście** | Fast-track z wykorzystaniem AI (skrócenie z 6 mies. do 2-3 mies.) |
| **Budżet** | [DO UZUPEŁNIENIA] |

---

## Powiązane dokumenty

- **Architektura:** [[ARCHITEKTURA]] - szczegóły techniczne, limity, struktura
- **Roadmapa:** [[ROADMAPA]] - plan wydań MVP1 i MVP2
- **CHANGELOG:** [[CHANGELOG]] - pełna historia ustaleń

---

## Uwagi dla agenta overview-sync

**KRYTYCZNE:** NIE ZMYŚLAJ. Jeśli w CHANGELOG brak danych → zostaw `[DO UZUPEŁNIENIA]`.
Wypełniaj TYLKO na podstawie "Deep Read" notatek źródłowych.
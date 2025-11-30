# WCAG - Dostępność

**Klient:** AMODIT (roadmapa)
**Status:** 🟡 W analizie
**PDM:** [do uzupełnienia]
**Tech Lead:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[WCAG]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Użytkownicy AMODIT potrzebują opcji trybu ciemnego (Dark Mode) dla lepszej ergonomii pracy przy słabym oświetleniu oraz zmniejszenia zmęczenia wzroku podczas długotrwałej pracy z systemem.

### Rozwiązanie

Eksperymentalne wdrożenie trybu ciemnego przy użyciu filtrów CSS (`contrast(0.8) invert(1) hue-rotate(180deg)`) jako szybkiego rozwiązania, które może być dopracowane w przyszłości jako pełnoprawna funkcjonalność cross-cutting.

### Obecna faza

📋 **W analizie** - eksperyment wymaga dopracowania dla obrazków i specyficznych elementów

**Ukończono:**
- ✅ Zdefiniowanie podejścia eksperymentalnego z filtrami CSS

**W trakcie:**
- Dopracowanie obsługi obrazków
- Obsługa specyficznych elementów (pasek nawigacji)

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Eksperyment z filtrami CSS** | Szybkie wdrożenie pozwala na weryfikację potrzeby przed inwestycją w pełnoprawne rozwiązanie |

---

## Eksperyment: Tryb ciemny z filtrami CSS

**Cel:** Weryfikacja potrzeby i użyteczności trybu ciemnego

**Zakres:**
- [ ] Implementacja filtrów CSS
- [ ] Dopracowanie dla obrazków i specyficznych elementów
- [ ] Mechanizm przełączania trybu

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]

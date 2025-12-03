# CHANGELOG – WCAG

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Design

- **Tryb ciemny (Dark Mode) - eksperyment** z szybkim wdrożeniem przy użyciu filtrów CSS
  - Sekwencja filtrów: `contrast(0.8) invert(1) hue-rotate(180deg)`
    - `invert(1)` - odwraca jasność (biały → czarny)
    - `hue-rotate(180deg)` - przywraca oryginalne odcienie kolorów (żeby zielony nie stał się fioletowy)
  - **Punkty otwarte:** Wymaga dopracowania dla obrazków i specyficznych elementów (np. pasek nawigacji), które nie powinny być odwracane (lub odwracane podwójnie)
  - Temat do dalszego "pociągnięcia" jako cross-cutting

---


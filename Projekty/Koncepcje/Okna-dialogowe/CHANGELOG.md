# CHANGELOG – Okna-dialogowe

---

## 2024-04-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2024-04-16 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2024-04-16%20Rada%20architektów.md)
**Kategoria:** #Architektura #Design

- **Trzy koncepcje okien dialogowych** odpowiadające na różne poziomy złożoności interakcji:
  - **Proste okno dialogowe** – brak procesu, pola definiowane w wywołaniu, dane używane natychmiast po zamknięciu (✅ wybrana)
  - **Okno na podstawie formularza** – proces typu "proces-formularz", wywołanie `ShowDialog("nazwa formularza", ...)`, wynik jako JSON (✅ wybrana)
  - **Okno na podstawie procesu** – pełnoprawny proces z regułami, sprawy w bazie (⏸️ odroczona)
- **Uproszczony UI** dla okien dialogowych – bez prawego panelu, załączników, historii, spraw powiązanych
- **Format zwracanych danych:** obiekt JSON konsumowany przez formularz główny
- **Punkty otwarte:** szczegółowe definicje procesów, konsumpcja danych przez formularz główny, akcje użytkownika w oknie

---


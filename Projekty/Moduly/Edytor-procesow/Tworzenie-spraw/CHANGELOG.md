# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Decyzja #Zadanie

- Zapobieganie duplikatom spraw zakładanych z maila/pliku.
- Wprowadzone mechanizmy: dla maili (pośrednia tabela z `Message-ID`) i dla plików (hash + data modyfikacji + nazwa).
- Zadania dla Damiana Kaminskiego (rozpięcie na PBI) i Piotra Buczkowskiego (implementacja mechanizmów).

---

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- RegEx – problem z dzieleniem dokumentu po kodzie kreskowym.
- Decyzja: Jeśli dokument nie ma żadnego kodu, zakłada jedną zbiorczą sprawę. Jeśli nie rozpozna kodu, ale kod jest, nie dzieli dokumentu, nadal skleja jako część poprzedniego dokumentu.

---
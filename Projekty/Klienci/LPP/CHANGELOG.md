# CHANGELOG - LPP

Historia ustaleń i zmian dla klienta LPP.

---

## 2025-12-22 | Zlecenie: Wykluczenie procesu z zakładki "Mój zespół"
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-22 zlecenie LPP - Wykluczenie procesu z zakładki mój zespół .md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-22%20zlecenie%20LPP%20-%20Wykluczenie%20procesu%20z%20zak%C5%82adki%20m%C3%B3j%20zesp%C3%B3%C5%82%20.md)
**Kategoria:** #Funkcjonalność #Decyzja #Uprawnienia

- **Problem:** Potrzeba ukrycia prywatnych spraw pracowników (ZUS, PIT-2) przed przełożonymi w zakładce "Mój zespół".
- **Rozwiązanie:** Dodanie w ustawieniach procesu opcji "Dostęp dla przełożonego" z możliwością blokady dla przełożonego twórcy lub wszystkich właścicieli sprawy.
- **Implementacja:** Zmiany w funkcjach `SynchronizeReadersPermissionsNew` oraz `CheckCasePermissions`.
- **Wycena:** 8000.
- **Termin:** do 16 stycznia 2026.

---

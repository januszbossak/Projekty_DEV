# CHANGELOG – Usuwanie spraw powiązanych

---

## 2025-09-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-16 Rada architektów - Przegląd projektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-16%20Rada%20architektów%20-%20Przegląd%20projektów.md)
**Kategoria:** #Bug #Decyzja

**Problem z usuwaniem spraw nadrzędnych z aktywnymi podrzędnymi** ✅
- **Problem:** Błąd bazy danych przy DeleteCase, gdy sprawa ma podpięte ukryte sprawy podrzędne (isHidden=true).
- **Decyzja:** ✅ Obsłużyć sytuację z ukrytymi sprawami w logice DeleteCase (Piotr Buczkowski).
- **Szczegóły:** Ukryte sprawy nie są pobierane do kolekcji Connected Cases, przez co nie są odczepiane.

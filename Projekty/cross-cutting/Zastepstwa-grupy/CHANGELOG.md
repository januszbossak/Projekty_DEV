# CHANGELOG – Zastępstwa-grupy

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Zastępstwo za grupę – różnice między starym a nowym mechanizmem** ✅
- **Problem:** Niespójność między mechanizmami - stary mechanizm obsługuje zastępstwa za grupy, nowy nie
- Stary: zastępca osoby z grupy widzi sprawy przypisane do tej grupy
- Nowy: zastępca widzi tylko sprawy bezpośrednio przypisane do osoby (nie grupy)
- ✅ **Zatwierdzone:**
  1. **Domyślnie dla grup jednoosobowych** - zastępstwa uwzględniane (grupa = rola, np. Dyrektor Finansowy, RODO)
  2. **Parametr dla grup wieloosobowych** - opcja "Uwzględnij zastępstwa dla tej grupy"
     - Przykład: HR z 20 osobami - nie potrzebuje (zawsze ktoś się zajmie)
  3. **Ujednolicenie mechanizmów** - docelowo oba powinny działać tak samo (kilka godzin pracy)
- **Mechanizm:** 2 zapytania w nowym mechanizmie (`CASE...` dla spraw użytkownika/grup `UNION` z działaniami kategorii z zastępstwem)
- **Punkty otwarte:**
  - Nowa kolumna w tabeli grup czy logika SQL (sprawdzenie liczby członków)?
  - Interfejs do ustawiania parametru "Uwzględnij zastępstwa"?
  - Czy docelowo przejść całkowicie na nowy mechanizm?
- **Zadania:** Piotr Buczkowski - obsługa grup jednoosobowych domyślnie + parametr dla wieloosobowych

---


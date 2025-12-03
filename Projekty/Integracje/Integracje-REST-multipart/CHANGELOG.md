# CHANGELOG – Integracje-REST-multipart

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Usprawnienie mechanizmu przesyłania załączników przez API** ✅
- ❌ Odrzucone: Indywidualne pary klucz-wartość (`CustomHeaderKey1`, `CustomHeaderValue1`) - nieelastyczne, nadmiar parametrów
- ✅ Zatwierdzone:
  1. **Zmienna dla listy załączników** - odwołanie do listy załączników na sprawie
  2. **Tablica `documents`** - obiekty z `DocumentName` i `DocumentValue` (Base64)
  3. **Obsługa formatów** - natywne wsparcie `multipart/form-data` i `x-www-form-urlencoded`
  4. **Mechanizm jak headers** - pary klucz-wartość przez nową linię
- **Funkcja:** `callRest`
- **Parametry:** `DocumentName`, `DocumentValue` (Base64)
- **Zadania:** Adrian Kotowski - implementacja, Piotr Buczkowski - weryfikacja

---


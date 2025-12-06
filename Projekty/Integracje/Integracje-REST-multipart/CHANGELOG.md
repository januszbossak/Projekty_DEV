# CHANGELOG – Integracje-REST-multipart

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Architektura #Funkcjonalność #Decyzja
**Projekt:** [Klienci/Marba/CallRest-wiele-plikow](../../Klienci/Marba/CallRest-wiele-plikow/)

**CallRest – obsługa multipart form data dla wielu plików** ✅

Implementacja obsługi wysyłania wielu plików (dynamiczna ilość, do 100) w formacie multipart form data za pomocą CallRest. Rozwiązanie spójne z istniejącym mechanizmem headers (10.2).

**Szczegóły:**
- Format: multipart form data (optymalny dla plików binarnych)
- Mechanizm: jeden parametr z listą plików + separatory (jak headers 10.2)
- Separator: pojedynczy dwukropek (`:`) - spójność z istniejącym mechanizmem
- Budowanie: Handlebars (`each`, `if`) do dynamicznego budowania listy
- Format parametru: `file:FieldByName:nazwa_pola:nazwa_pliku`
- 3 sposoby wskazania pliku: ID pliku, nazwa pola, nazwa załącznika
- Możliwość zmiany nazwy pliku przy wysyłaniu

**Kontekst:**
- **Główna implementacja dla klienta Marba** - zobacz [Klienci/Marba/CallRest-wiele-plikow](../../Klienci/Marba/CallRest-wiele-plikow/)
- Potrzeba wysyłania wielu plików do zewnętrznego Web Service'u
- Rozwiązanie uniwersalne - przyszła potrzeba dla KSeF (faktury z załącznikami)

**Zadania:**
- Adrian Kotowski - implementacja multipart form data
- Piotr Buczkowski - weryfikacja i uwagi

**Punkty otwarte:**
- Przyszłe wsparcie JSON z Base64 (odroczone)
- Separator - wystarczająco niezawodny przy specjalnych nazwach plików?

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


# CHANGELOG - Silnik reguł

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność

**ForEachAttachment – iteracja po załącznikach** ✅
- **Zaimplementowano:** Pętla `ForEachAttachment` iterująca po swobodnych załącznikach sprawy
- **Parametry:** `this.Id`, `this.Name`, `this.Tag`, `this.TagBody`
- **Optymalizacja:** `Value` (zawartość pliku) pobierane tylko na żądanie
- **Użycie:** `this.Id` jako identyfikator (unikanie duplikatów nazw)
- **Feedback:** Dodać obsługę samego `this` (bez parametru) w przyszłości

---

## 2025-08-25 - Sprint review

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność #PoC

**Prezentacja:** Damian Kamiński

**Cel biznesowy:**
Umożliwienie iteracji po załącznikach dodawanych swobodnie do sprawy (w prawym panelu) z poziomu reguł. Do tej pory nie było metody na dostęp do tych załączników i wykonywanie operacji na nich (np. stworzenie ZIP-a, znalezienie konkretnego pliku, zmiana nazwy).

**Co zaimplementowano:**
- **Funkcja `foreach attachment`:** możliwość iteracji po liście załączników w sprawie
- **Prototyp:** funkcjonalność jest w fazie prototypu, gotowa do pokazania po zakończeniu

**Status:**
⏸️ W trakcie implementacji - prototyp do prezentacji wkrótce

**Dalsze kroki:**
- **Zakończenie prototypu:** dokończenie prac nad prototypem i prezentacja funkcjonalności
- **Dokumentacja:** przygotowanie dokumentacji użycia funkcji `foreach attachment`


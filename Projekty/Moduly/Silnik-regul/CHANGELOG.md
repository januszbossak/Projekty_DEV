# CHANGELOG - Silnik reguł



---

## 2025-12-05 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-05 Planowanie sprintu.md]
**Projekt:** [Klienci/LOT/JRWA](../../Klienci/LOT/JRWA/)
**Kategoria:** #Funkcjonalność #Zadanie

**Dostęp do danych z pola Odnośnik do źródła zewnętrznego:**
- Sprawdzić czy składnia `[NazwaPola.Źródło.Kolumna]` działa dla źródeł zewnętrznych (JRWA, GUST, TERYT)
- Obecnie wymaga ręcznego parsowania JSON (funkcja `ParseJSON` wzorowana na GUST)
- Jeśli składnia nie działa - dodać obsługę w walidatorze/silniku reguł (automatyczne uzupełnianie pól bez ręcznego parsowania JSON)

**Przykład użycia:**
```
[KategoriaJRWA.Źródło.Symbol]  → "001"
[KategoriaJRWA.Źródło.Nazwa]   → "Rada nadzorcza"
```

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Spotkanie projektowe - Błędy formularzy i procedury aktualizacji.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-03%20Spotkanie%20projektowe%20-%20Błędy%20formularzy%20i%20procedury%20aktualizacji.md)  
**Kategoria:** #Dokumentacja  
**Projekt:** [Moduly/AMODIT Copilot](../AMODIT%20Copilot/)

- **Walidacja pól typu data - funkcje już istnieją** - zgłoszono propozycję automatycznej walidacji dat, ale funkcje `SetDateFilters` i `ValidateDateField` już istnieją w silniku reguł
- **Problem:** Brak wiedzy o istniejących funkcjach (nawet doświadczeni developerzy nie wiedzą o `SetDateFilters`)
- **SetDateFilters:** Blokuje wybór dat poza określonym zakresem w kalendarzyku (podajesz nazwę pola, zakres od-do)
- **ValidateDateField:** Walidacja wprowadzonych dat
- **Wnioski:** Potrzeba lepszego Copilota (sensowne odpowiedzi bez znajomości dokładnej nazwy funkcji), uzupełnienie artykułów Wiki (obecnie tylko techniczne opisy w specyfikacji), nakaz używania Copilota przez zespół
- **Propozycja:** Przygotowywanie zadań z użyciem specyficznych funkcji dla podnoszenia świadomości zespołu

---

## 2025-11-12 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-12 Spotkanie projektowe - Przegląd wycen.md]
**Kategoria:** #Bug #Problem

- Problem z wyczyszczeniem wartości w radio buttonach w regule automatycznej (`setRadioValue`).
- Niespójność w działaniu systemu w porównaniu do zwykłych list wyboru.
- Obecne obejście to dodanie "pustej" opcji "--".

---

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Problem z wywołaniem reguły funkcji dla zamkniętej sprawy (walidowany element, że sprawa jest zamknięta, mimo że to jest funkcja).
- Decyzja: Dla funkcji nie powinno być to walidowane.

---

## 2025-10-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-21 Rada architektów.md]
**Kategoria:** #Architektura #Decyzja

- Zmiany w języku reguł nie mogą być dostarczane jako DLL (wymagane podniesienie wersji AMODIT).
- Wyjątek: Dedykowane funkcje/integracje za opłatą, ale nie zmiany w parserze.

**Kategoria:** #Bug

- Funkcja `DeleteAttachment` musi działać dla attachmentów tak samo jak `GetAttachment` (logika sprawdzania wszystkich form załącznika).
- Zadanie: Zaimplementować poprawkę w `DeleteAttachment` (Damian Kaminski).

---

## 2025-09-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-30 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-30%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Decyzja

- **SetDefault:** Dodanie opcji `SetDefault` do funkcji `SetListFilter` (i podobnych), aby umożliwić wyłączenie automatycznego wyboru jedynej wartości.
- **SetList:** Decyzja o weryfikacji zachowania funkcji `SetList` przy jednej pozycji (ewentualne ujednolicenie z `SetListFilter`).
- **ReferenceQueryEx:** Potwierdzono, że funkcjonalność `ThrowError` jest już zaimplementowana.

---

## 2025-09-25 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-25%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **ExecuteOnText:** Rozszerzono funkcję `ExecuteOnText` o obsługę pola typu raport (akcje: Refresh, Wydrukuj, Wygeneruj CSV/Excel).
- **ForRow:** Poprawiono opis funkcji `ForRow` tak, aby nie sugerował możliwości odwoływania się do `CaseID` innej sprawy (funkcja do kontekstu wiersza tabeli).

---

## 2025-09-23 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-23 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-23%20Rada%20architektów.md)
**Kategoria:** #Decyzja

- **CallFunctionEx:** Temat odroczony (status ⏸️). Nie jest krytyczny, nikt o niego nie zabiega. Funkcja miała służyć do obsługi procesów typu "biblioteka" (czwarty typ procesu).

- **Run As User:** Pomysł dodania funkcji pozwalającej na wykonywanie akcji jako konkretny użytkownik (np. "Pokój Pocztowy") zamiast "System Józef".
- **Decyzja:** 🔍 Do przemyślenia.
- **Alternatywa:** Zmiana nazwy użytkownika systemowego (wystarczyło dla Orlenu). Rozważane czy funkcja jest potrzebna, czy wystarczy zmiana nazwy/loginu.

---
## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Funkcja `Create Callout`:** Zostanie dodana funkcja do generowania komunikatów (callout) w regułach. Przyjmuje tekst i styl (info, danger, warning), zwraca HTML callout do przypisania do pola typu static tekst.

---
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


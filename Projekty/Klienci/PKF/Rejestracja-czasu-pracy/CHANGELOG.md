# Historia zmian - Rejestracja czasu pracy (PKF)

## 2025-12-02 | ⚠️ Problem | Spotkanie projektowe - Design
**Źródło:** [Notatki/Spotkania projektowe/2025-12-02 Spotkanie projektowe - Design.md]

**Edge case: edycja wierszy tabel w raportach**

PKF zgłosił potrzebę edycji wierszy tabel z poziomu raportu osadzonego na sprawie.

**Przykład use case:**
- Raport wyświetla wiersze z tabel z różnych spraw (rejestracja czasu pracy z kilku dni)
- Użytkownik chce zbiorczo edytować te wiersze (korekta godzin, zmiana projektów)
- Obecny system nie obsługuje edycji danych w raportach – tylko wyświetlanie

**Rozważane rozwiązania:**
- Uproszczone okienka modalne do edycji wiersza tabeli (formularz wiersza istnieje)
- Edycja w trybie Excelowym (inline editing) - trudne dla reguł i zależności
- Edycja przez Excel (Get/Set Excel Data) - brak funkcji Set Excel Data

**Status:** ⏸️ Odroczone – temat do dyskusji na Radzie Architektów

**Uzasadnienie:**
- Temat bardzo szeroki, wymaga przemyślenia wielu aspektów
- Edycja danych w raportach to złożony problem (reguły, walidacje, zależności między polami)
- Brak obecnie sensownego pomysłu na implementację
- Dla PKF znaleziono obejścia (gimnastyka, ale działa)

**Punkty otwarte:**
- Temat do dyskusji na Radzie Architektów lub osobnym spotkaniu Design
- Nie do realizacji w ciągu kilku dni – wymaga głębszej analizy i koncepcji

**Powiązane projekty:**
- Zobacz: [Moduly/Modul-raportowy](../../Moduly/Modul-raportowy/CHANGELOG.md) - to jest problem przekrojowy modułu raportowego

---

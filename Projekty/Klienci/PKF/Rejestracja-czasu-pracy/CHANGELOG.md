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

## 2025-08-28 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-28 Rada architektów|2025-08-28 Rada architektów]]

**Kategoria:** #Problem #Wymaganie

**Kontekst:**
PKF chce mieć widok typu pivot/Excel do rejestracji czasu pracy (Timesheet), gdzie w wierszach są zadania/zlecenia, a w kolumnach dni tygodnia (poniedziałek–niedziela). Użytkownik chce wypełniać macierz godzin bezpośrednio w tabelce, zamiast wchodzić do każdej sprawy osobno (co jest obecnie "dużą klikologią").

### Zidentyfikowane Ryzyka

- Wydajność przy dużych tabelkach (300+ wierszy)
- Obciążenie formularza sprawy przy dużych tabelkach
- Ryzyko utraty kontekstu przy stronicowaniu (jeśli zastosowane)

### Rozważane alternatywy

- **Tabelka AMODITowa na sprawie** - obciąża CaseDefinition, problemy wydajnościowe przy dużych tabelkach
- **Raport tabelaryczny osadzony** - wymaga rozbudowy mechanizmu edycji w raportach osadzonych (odroczone)
- **GetExcelData + Excel zewnętrzny** - rozwiązanie jednostkowe, nie systemowe (odroczone)
- **Dashboard z raportem + podglądem sprawy** - raport tabelaryczny z możliwością kliknięcia w wiersz i wyświetlenia sprawy po prawej stronie (propozycja do rozważenia)

### Decyzja

**Status:** ⏸️ Odroczone

**Dla PKF:**
- Temat wymaga wyceny i dalszej analizy
- Można powołać się na wcześniejszą analizę, gdzie przedstawiono obecne rozwiązanie (rejestracja przez sprawy) i zostało zaakceptowane przez klienta
- Jeśli klient będzie nalegał, można rozważyć rozwiązanie z GetExcelData lub rozbudowę dashboardu

### Szczegóły techniczne

- Raporty osadzone ze źródła zewnętrznego obecnie nie obsługują edycji checkboxów – wymaga rozbudowy
- Stronicowanie w raportach może powodować problemy z kontekstem (pierwsza strona nieaktywna po przejściu na drugą)
- Duże tabelki na formularzu sprawy obciążają zarówno przeglądarkę, jak i serwer (operacje typu foreach, sumy)

### Zadania

- **Damian Kaminski:** Weryfikacja nagrań z analizy PKF dotyczących Timesheetu

### Punkty otwarte

- Czy dashboard powinien mieć mechanizm podglądu sprawy obok raportu?
- Czy dla dużych tabel lepiej wyświetlać je w osobnym oknie zamiast na formularzu sprawy?

**Powiązane projekty:**
- Zobacz systemowe rozwiązanie: [[../../Moduly/Modul-raportowy/CHANGELOG|Modul-raportowy]]

---

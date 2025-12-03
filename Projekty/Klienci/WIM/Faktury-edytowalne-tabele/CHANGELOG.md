# CHANGELOG - Faktury edytowalne tabele (WIM)

## 2025-08-28 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-28 Rada architektów|2025-08-28 Rada architektów]]

**Kategoria:** #Funkcjonalność #Wymaganie

**Kontekst:**
WIM chce mieć tabelkę z pozycjami zamówienia (do 300 wierszy) zaciągniętymi z innego systemu, gdzie użytkownik zaznacza checkboxami, które pozycje są zgodne z fakturą. Po zaznaczeniu przyciskiem ma się wygenerować opis niezgodności dla pozycji niezaznaczonych.

### Zidentyfikowane Ryzyka

- Wydajność przy dużych tabelkach (300+ wierszy)
- Obciążenie formularza sprawy przy dużych tabelkach
- Ryzyko utraty kontekstu przy stronicowaniu (jeśli zastosowane)

### Rozważane alternatywy

- **Tabelka AMODITowa na sprawie** - obciąża CaseDefinition, problemy wydajnościowe przy dużych tabelkach (odrzucona)
- **Raport tabelaryczny z checkboxami (WIM)** - raport osadzony z możliwością zaznaczania checkboxów (wybrana - rozwiązanie systemowe)
- **GetExcelData + Excel zewnętrzny** - rozwiązanie jednostkowe, nie systemowe (odroczona)

### Decyzja

**Status:** ✅ Zatwierdzone (wymaga rozbudowy)

**Dla WIM:**
- Użycie raportu tabelarycznego osadzonego ze źródła zewnętrznego
- Rozbudowa mechanizmu raportów o możliwość edycji checkboxów w źródłach zewnętrznych
- Zwiększenie limitu wierszy dla źródeł zewnętrznych (obecnie 100, może być potrzeba 300+)
- Rozważenie opcji odwrotnej logiki: zaznaczanie tylko pozycji niezgodnych (mniej klikania) zamiast zgodnych

### Szczegóły techniczne

- Raporty osadzone ze źródła zewnętrznego obecnie nie obsługują edycji checkboxów – wymaga rozbudowy
- Stronicowanie w raportach może powodować problemy z kontekstem (pierwsza strona nieaktywna po przejściu na drugą)
- Duże tabelki na formularzu sprawy obciążają zarówno przeglądarkę, jak i serwer (operacje typu foreach, sumy)

### Zadania

- **Damian Kaminski:** Weryfikacja wymagań z WIM dotyczących logiki zaznaczania (zgodne vs niezgodne)
- **Damian Kaminski:** Przygotowanie PA (Product Analysis) dla rozbudowy raportów o edycję checkboxów
- **Kamil Dubaniowski:** Weryfikacja wydajności ładowania 300 pozycji z procedury składowanej (oczekiwany czas: max 5 sekund)
- **Kamil Dubaniowski:** Weryfikacja czy kwota z faktury będzie odczytywana z OCR-a czy z innego źródła

### Punkty otwarte

- Czy zwiększyć limit wierszy w raportach ze źródeł zewnętrznych powyżej 100?
- Jak obsłużyć przypadek, gdy OCR nie odczyta numeru zamówienia lub odczyta błędnie?

**Powiązane projekty:**
- Zobacz systemowe rozwiązanie: [[../../Moduly/Modul-raportowy/CHANGELOG|Modul-raportowy]]


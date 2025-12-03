# CHANGELOG - Raporty edycja gradientów (WIM)

## 2025-08-25 - Sprint review

**Źródło:** [[../../../../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność

**Dlaczego realizujemy:**
Projekt wynika z wymagania Piotra Murawskiego (WIM) o możliwość dostosowania palet kolorowych w raportach. WIM potrzebuje elastycznego definiowania własnych skal kolorystycznych zamiast domyślnego gradientu niebiesko-brązowego.

**Co zaimplementowano:**
- Edycja gradientów kolorów w raportach Treemap i Pivot
- Możliwość wyboru własnych kolorów dla skali (zamiast domyślnych)
- Reset do domyślnej palety kolorów
- Wsparcie dla wartości ujemnych, dodatnich i środkowych
- Zapisywanie wybranych palet kolorów

**Ograniczenia MVP:**
- Funkcjonalność dostępna tylko w Treemap i Pivot (raporty agregujące)
- Kolory gradientowe nie zostały jeszcze dodane do wykresów kolumnowych (wymaga konsultacji z Markiem)

**Dalsze plany:**
- Dodanie gradientów do wykresów kolumnowych po konsultacji z Markiem
- Rozszerzenie możliwości edycji (np. przesuwanie środka skali, więcej punktów kontrolnych)
- Inspiracja funkcjonalnością Tableau (gradient ciągły, skoki w krokach)


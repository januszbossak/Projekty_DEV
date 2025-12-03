# CHANGELOG - Filtry użytkownika

## 2025-08-25 - Sprint review

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność

**Prezentacja:** Łukasz Bott

**Cel biznesowy:**
Usprawnienie pracy z raportami zawierającymi duże zbiory danych poprzez wymuszenie ustawienia filtrów przed wyświetleniem danych. Szczególnie ważne dla źródeł zewnętrznych z dużą ilością danych (np. logi systemowe, dane z zewnętrznych API).

**Co zaimplementowano:**
- **Filtry wymagane:** możliwość oznaczenia filtra jako "wymagany"
- **Blokada wyświetlania:** raport nie wyświetla danych dopóki użytkownik nie ustawi wymaganych filtrów
- **Wartości domyślne:** możliwość ustawienia wartości domyślnej dla filtra (np. "ostatnie 7 dni")
- **Priorytyzacja:** wartość użytkownika zapisana w localStorage ma pierwszeństwo przed wartością domyślną

**Jak to działa:**
Jeśli filtr jest oznaczony jako "wymagany", system nie pobiera ani nie wyświetla danych dopóki użytkownik wyraźnie nie zaznaczy wartości tego filtra. Wartość domyślna jest stosowana tylko gdy filtr jest pusty (localStorage nie zawiera wyboru użytkownika).

**Przykłady użycia:**
1. **Logi systemowe:** Filtr "data" wymagany - użytkownik musi wybrać przedział czasu (np. ostatni dzień, ostatnie 7 dni)
2. **Sprawy na etapach:** Filtr "proces" wymagany - użytkownik musi wybrać proces, aby zobaczyć sensowny wykres (bez tego powstaje "sieczka" z tysiącem etapów ze wszystkich procesów)

**Feedback z demo:**
- **Mateusz Kisiel:** Czy wartość domyślna nadpisuje localStorage? (Odpowiedź: nie, localStorage ma pierwszeństwo)
- **Łukasz Bott:** W szczególności, że filtr "ogranicza zakres danych" na dole może być niewidoczny dla użytkownika, jeśli nie jest gdzieś wyraźnie zaznaczony w tytule lub opisie raportu.

**Dalsze kroki:**
- **Informowanie o ograniczeniach:** rozważenie dodania informacji o ustawionych filtrach "ograniczających zakres danych" w tytule lub opisie raportu
- **Rozszerzenie na więcej raportów:** zastosowanie filtrów wymaganych w raportach systemowych i innych raportach z dużymi zbiorami danych


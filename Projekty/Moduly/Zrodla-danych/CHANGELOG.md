# CHANGELOG - Źródła danych

## 2025-09-04 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-04 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-04%20Rada%20architektów.md)
**Kategoria:** #Architektura #Planowanie

**Przerobienie źródeł na dynamic form (Wsparcie dla Zmienne-globalne)**
- Temat dotyczy kompleksowego podejścia do źródeł typu `dynamic`
- Szczegóły w projekcie głównym: [Klienci/WIM/Zmienne-globalne](../../Klienci/WIM/Zmienne-globalne/CHANGELOG.md)

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność #Architektura

**Cel:**
Rozszerzenie możliwości zasilania źródeł danych oraz wprowadzenie bibliotek funkcji i szablonów dokumentów poza procesami.

### 1. Zasilanie danych przez REST API

- Do tej pory źródła zewnętrzne zasilaliśmy zapytaniami SQL
- Teraz można zasilać źródło danych, wysyłając dane do odpowiedniego endpointu REST API (z aplikacji zewnętrznej)

### 2. Call Function (biblioteka funkcji)

- Do tej pory skrypty `Call Function` były w ramach procesu
- Teraz można mieć ogólny skrypt (bibliotekę) poza procesem i używać go w wielu różnych procesach
- To samo będzie dotyczyć biblioteki szablonów dokumentów

### Szczegóły techniczne

- REST API endpoint do zasilania źródeł danych
- Biblioteka funkcji poza procesami
- Biblioteka szablonów dokumentów (planowana)

### Ograniczenia

- Biblioteka szablonów dokumentów jeszcze nie zaimplementowana (planowana)

---

## 2025-07-07 - Odczyt i zapis do źródła danych typu static

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-07-07 Odczyt i zapis do Źródła danych typu static|2025-07-07 Odczyt i zapis]]

**Kategoria:** #Architektura #Funkcjonalność

Implementacja funkcji `SourceGet`, `SourceSet`, `SourceAdd` dla źródeł danych typu "static" (dynamiczne). Umożliwia odczyt i zapis danych bezpośrednio z poziomu reguł, bez potrzeby ręcznego importu lub synchronizacji całych tabel.

**Kontekst:** Główna implementacja dla klienta WIM (zmienne globalne) - zobacz szczegóły: [[../../Klienci/WIM/Zmienne-globalne/CHANGELOG|WIM/Zmienne-globalne]]

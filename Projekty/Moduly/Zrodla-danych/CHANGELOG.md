# CHANGELOG - Źródła danych

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Problem z mapowaniem źródeł typu Static przy ponownym wgrywaniu (wszystko zmienia się na LongText).
- Rozwiązanie: Automatyczne wyświetlenie okienka mapowania po kliknięciu "Wybierz plik", zmiana przycisku "Zapisz" na "Wczytaj".

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Funkcjonalność #Bug

- Funkcja GetDataSet ma braki w obsłudze wartości null i wyszukiwania.
- Decyzja: System powinien automatycznie obsługiwać wartości null.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Architektura #Problem

- Problem z ujemnymi ID w źródłach systemowych na MSSQL
- Zmiana nazewnictwa tabel systemowych (podkreślenie zamiast minusa)
- Planowane przejście na GUID zamiast ujemnych ID

---

## 2025-10-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-16 Rada architektów.md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- Zmiana identyfikatorów źródeł danych systemowych z ujemnych na dodatnie i dodanie GUID
- Wprowadzenie kolumn `czy_systemowe` i `GUID` do tabeli źródeł danych w celu łatwiejszego przenoszenia definicji między środowiskami

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Architektura #Decyzja

- Przejście źródeł systemowych z ujemnych ID na GUID i flagę systemową (`SystemOrigin`)
- Decyzja: Przerwanie kompatybilności wstecznej dla użytkowników korzystających ze źródeł systemowych

---

## 2025-10-02 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-02 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-10-02%20Rada%20architektów.md)
**Kategoria:** #Problem #Decyzja

- Zidentyfikowano problem techniczny z tworzeniem źródeł lokalnych (synchronizowanych) dla bazy MS SQL
- Decyzja o niewstrzymywaniu prac nad raportami systemowymi i skupieniu się na MySQL; poprawki dla MS SQL odroczone

---

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

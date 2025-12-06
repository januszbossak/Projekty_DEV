# CHANGELOG - Interfejs sprawy

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność #Design #Odroczone

- **Amadeus – problem z dodaniem grupy do pola "Redaktorzy spraw":** Problem z nawiasami w nazwie systemowej grupy. Rozwiązanie: Użycie nazwy wyświetlanej; długoterminowo: blokada dziwnych znaków w nazwie systemowej.
- **Uwspółcześnienie mechanizmu drukowania:** Mechanizm drukowania jest przestarzały. Decyzja: Odroczone, zrobić minimalną dokumentację.

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🎨 Design

- **Ikony grup:** wprowadzenie wizualnego rozróżnienia grup (biała ikona) od użytkowników (czarny tekst) w panelu informacji i uprawnień.
- **Spójność kolorystyczna:** kolory grup zgodne z zakładką "Do wykonania".
- **Znane problemy:** ikona grupy optycznie wydaje się większa od tekstu (kwestia "od krawędzi do krawędzi" vs font).
- **Feedback:** sugestia możliwości definiowania własnej ikony per grupa (feature request na przyszłość).

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Funkcjonalność

**Kontekst:**
Seria zmian w interfejsie sprawy: menu nawigacyjne, formularz, prawy panel, tabele. Wszystkie zmiany mają na celu poprawę ergonomii, czytelności i przestrzeni roboczej.

---

### 1. Nowe menu po lewej stronie

**Nowe funkcjonalności:**
- Okienko wyszukiwania z pozycji menu
- Zarządzanie obszarami przeniesione na górę (obok wyszukiwania)
- Cały boczny panel menu można zwijać, żeby mieć więcej przestrzeni roboczej (pozostaje dostępny w formie kafelków/ikon)

**Reorganizacja pozycji:**
- Wydzielona zakładka "Do wykonania" poza obszary (agreguje wszystkie sprawy przypisane do użytkownika ze wszystkich obszarów)
- Przeniesione "Powiadomienia" z górnego paska do lewego menu (pod zakładkę "Do wykonania") – użytkownicy widzą tam np. wzmianki w komentarzach, powinny być bardziej widoczne
- Podział na:
  - Listy spraw: np. "Mój zespół", "Wszystkie"
  - Przypięte: raporty przypięte przez twórcę lub użytkownika
  - Linki: aplikacje zewnętrzne podpięte do AMODIT
  - Moduły: osobna sekcja, np. Nadawca, Przelewy

**Szczegóły techniczne:**
- Zakładka "Do wykonania" na samej górze agreguje wszystkie sprawy przypisane do użytkownika
- Wewnątrz obszarów nadal mogą być lokalne zakładki "Do wykonania" filtrujące zadania tylko z tego obszaru

---

### 2. Nowy wygląd formularza sprawy

**Zmiany w layoutcie:**
- Odświeżenie layoutu, więcej przestrzeni na sam formularz
- Menu nawigacyjne po opcjach sprawy zostało przeniesione z góry na prawą pionową belkę

**Poprawki designu przycisków:**
- Ujednolicone przyciski (białe tło, szara ramka)
- Kolory są tylko na ikonach (mniej jaskrawe przyciski mniej męczą wzrok i nie odwracają uwagi od pól wymaganych)

**Pola wymagane:**
- Pola wymagane są oznaczone delikatną pomarańczową linią na dolnej krawędzi
- Jeśli użytkownik pominie pole i spróbuje zapisać lub przekazać sprawę, system wyraźnie poinformuje o braku wypełnienia odpowiednim dopiskiem pod polem

**Konfiguracja lokalizacji paska przycisków:**
- Lokalizacja paska przycisków jest konfigurowalna per użytkownik
- Jeśli ktoś woli mieć przyciski na dole (bo czyta sprawę i na dole podejmuje decyzję), może to zmienić w ustawieniach

**Powiadomienia systemowe:**
- Powiadomienia systemowe do sprawy (powiązane sprawy, niekompletny formularz, priorytety) zostały poprawione wizualnie i znajdują się na górze pod przyciskami

---

### 3. Nowy wygląd prawego panelu sprawy

**Nowy wygląd:**
- Wszystkie panele zostały przebudowane, są lżejsze i w jednolitej tonacji

**Rozdzielenie funkcjonalności uprawnień:**
- Osobny prawy panel dla właścicieli i obserwatorów

**Panel "Informacje o sprawie":**
- Zyskał więcej szczegółów: stan sprawy, od kogo przyszła, kiedy, kto modyfikował

**Szczegóły techniczne:**
- Panele: podgląd dokumentu, lista załączników, informacje o sprawie, diagram, historia

---

### 4. Nowy wygląd tabeli na formularzu sprawy

**Nowy wygląd tabeli:**
- Odświeżony wygląd tabeli w tradycyjnym układzie kolumnowym oraz w postaci kafelków
- Zmniejszona liczba niepotrzebnych elementów, tabela jest czystsza
- Zmieniony wygląd podformularzy

**Personalizacja nazw przycisków:**
- Możliwość personalizacji nazwy przycisku "Dodaj" – zamiast ogólnego "Dodaj", twórca procesu może wpisać np. "Dodaj nowego członka rodziny"
- Analogiczne rozwiązanie na poziomie raportów – można zdefiniować nazwę przycisku tworzenia nowej sprawy, np. "Dodaj nowy wniosek urlopowy" czy "Dodaj nową fakturę"

**Zmiana miejsca importu danych:**
- Import danych do tabeli jest teraz przy dodawaniu nowych wierszy (menu kontekstowe przy przycisku "Dodaj"), a nie ukryte w "hamburgerze"
- Można dodać wiele wierszy naraz lub zaimportować wsad z Excela

**Szczegóły techniczne:**
- Menu kontekstowe przy przycisku "Dodaj"
- Import z Excela


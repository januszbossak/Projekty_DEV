# CHANGELOG - Edytor szablonów

## 2025-09-02 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-09-02 Rada architektów|2025-09-02 Rada architektów]]

**Kategoria:** #Design #Architektura

**Prezentacja:** Damian Kamiński

**Kontekst:**
Projekt widoku szablonów w procesach stworzony z wykorzystaniem AI (v0) na podstawie System Design. Obecny widok szablonów jest w starszej technologii i wymaga modernizacji do React. Projekt obejmuje zarówno odtworzenie obecnej funkcjonalności, jak i propozycje nowych funkcji.

### Zidentyfikowane Ryzyka

- Zbyt wiele nowości może wydłużyć czas projektowania, testowania i wydania
- Ryzyko odejścia od standardów UI/UX AMODIT (przyciski po lewej vs prawej stronie)
- Brak jasności co jest MVP, a co wersją max

### Decyzja

**Status:** ✅ Zatwierdzone

**Wersja MVP:**
- Przeniesienie obecnej funkcjonalności do React
- Zachowanie obecnego układu i logiki działania
- **Dodanie drag and drop** do zmiany kolejności szablonów (zamiast przycisków góra/dół)
- Ewentualnie **usuwanie zbiorcze** (zaznaczenie wielu + usunięcie)
- Kolumna "Etapy" (zapomniana w pierwszej wersji projektu)
- Kolumna "Uprawnienia i etapy" w jednej kolumnie (są ze sobą powiązane)
- Przycisk "Dodaj" po lewej stronie (zgodnie ze standardem AMODIT)
- Wyszukiwanie i filtry po prawej stronie (nowy standard)
- Szczegóły z przyciskiem "Pobierz" (i w przyszłości "Edytuj")
- **Podgląd dokumentu** (użycie istniejącego okienka podglądu)

**Wersja max (do rozważenia później):**
- Widok kafelkowy z mini podglądem pierwszej strony
- Foldery do organizacji szablonów
- Biblioteka szablonów wspólnych dla wielu procesów
- Edycja szablonów z poziomu AMODIT (połączenie z Office 365)

### Szczegóły techniczne

- **Technologia:** React
- **Biblioteka UI:** Ant Design (z dostosowaniem do wyglądu AMODIT)
- **Drag and drop:** do zmiany kolejności szablonów
- **Filtry:** po ustawieniach, po plikach, po temacie
- **Podgląd:** użycie istniejącego okienka podglądu dokumentów
- **Kolumny:** Nazwa, Etapy (uprawnienia i etapy razem), Szczegóły, Podgląd

### Uwagi

- Projekt stworzony przez v0 na podstawie System Design
- v0 nie zawsze poprawnie używa komponentów Ant Design (robi po swojemu)
- Ikony nie są MDI (Material Design Icons) – wymagają dostosowania do ikon Zender
- Wymagane dostosowanie do standardów UI AMODIT

### Zadania

- **Damian Kamiński:** Dopracowanie szczegółów projektu zgodnie z uwagami (na Design 12:30)
- **Damian Kamiński:** Dodanie kolumny "Etapy" do projektu
- **Damian Kamiński:** Połączenie kolumn "Uprawnienia" i "Etapy" w jedną
- **Damian Kamiński:** Przeniesienie przycisku "Dodaj" na lewą stronę
- **Damian Kamiński:** Przeniesienie wyszukiwania i filtrów na prawą stronę
- **Filip Liwiński:** Przełożenie obecnych uprawnień na nową tabelkę (pierwsze zadanie)

### Punkty otwarte

- Czy usuwanie zbiorcze powinno być w MVP?
- Jak obsłużyć przypadek, gdy szablon korzysta z wielu zmiennych (nie tylko pól)?
- Czy potrzebny jest widok kafelkowy w MVP?
- Jak zaimplementować edycję szablonów z poziomu AMODIT (połączenie z Office 365)?


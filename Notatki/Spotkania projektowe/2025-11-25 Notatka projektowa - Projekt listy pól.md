# Notatka projektowa – 2025-11-25 – Projekt listy pól

**Data:** 2025-11-25
**Temat główny:** Projekt nowej listy pól i prawego panelu edycji w edytorze formularza.

---

## 1. Dodawanie pól i sekcji (Lista pól)

**Komponent:** Edytor Formularza / Lista Pól

### Cel i problem
Umożliwienie intuicyjnego dodawania pól i sekcji w konkretnym miejscu formularza (kontekstowo), bez konieczności późniejszego przeciągania. Problem pojawia się przy polach typu Tabela – czy "Plus" dodaje pole w tabeli, czy pod tabelą.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Plus na zwiniętej tabeli | Dodaje pole na formularzu głównym (pod tabelą). Aby dodać do tabeli, trzeba ją rozwinąć. | ✅ Wybrana – zachowuje spójność z innymi polami. |
| Plus z wyborem | Kliknięcie plusa pyta "Gdzie dodać?" (w tabeli/pod tabelą). | ❌ Odrzucona – zbyt skomplikowane, wymagałoby wyboru sekcji w tabeli. |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- **Ikona "Plus" (+):** Służy zawsze do dodawania nowego elementu w danym kontekście (poniżej/powyżej). Przy tabeli zwiniętej – dodaje pole pod tabelą.
- **Rozwijanie tabeli:** Zmiana ikony rozwijania (szewron) i jej położenia. Szewron zostanie przeniesiony na prawą stronę nazwy pola (np. `Tabela produktów >`), aby odróżnić go od ikony typu pola (z lewej) i nie mylić z funkcją dodawania.
- **Spójność:** Plus = Dodaj, Szewron = Rozwiń/Zwiń. Zasada ta ma być stosowana spójnie w całym systemie.

---

## 2. Akcje na liście pól

**Komponent:** Edytor Formularza / Lista Pól

### Cel i problem
Zbyt duża liczba akcji dostępnych bezpośrednio przy polu na liście (Ustawienia, Uprawnienia, Historia, Reguły, Usuń, Zmień typ) powoduje bałagan wizualny.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

Na liście pól przy każdym polu będą widoczne tylko dwie główne ikony akcji:
1.  **Zębatka:** Otwiera Prawy Panel (Ustawienia pola).
2.  **Trzy kropki (Menu):** Rozwija listę pozostałych akcji:
    - **Widoczność/Uprawnienia:** Otwiera dedykowane okienko (modal), bez przechodzenia do prawego panelu.
    - **Historia pola:** Wyświetla historię zmian definicji pola.
    - **Reguły:**
        - Dla tabeli: "Reguła tabeli" (otwiera edytor).
        - Docelowo: "Reguły powiązane" (lista reguł używających tego pola).

Rzadkie akcje (Usuń, Zmień typ) zostają przeniesione/ukryte (patrz: Prawy panel).

---

## 3. Prawy Panel Edycji Pola (Redesign)

**Komponent:** Edytor Formularza / Prawy Panel

### Cel i problem
Obecny prawy panel jest nieintuicyjny (nagłówek z nazwą typu pola zamiast nazwy pola), zawiera niespójne sekcje ("Zarządzaj polem" z jedną akcją) i marnuje miejsce.

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone (Koncepcja)

- **Nagłówek:** Będzie zawierał edytowalną **Nazwę pola** oraz ikonę typu pola. Nazwa w nagłówku będzie się zmieniać w zależności od wybranego języka podglądu ("Zobacz dla").
- **Górna belka:** Przeniesienie kluczowych akcji do paska narzędzi w nagłówku (np. pod menu "trzy kropki").
- **Sekcja "Zarządzaj polem":** Zostaje usunięta.
    - **Zmiana typu pola:** Dostępna przy ikonie typu pola (w sekcji Dane podstawowe) lub w menu nagłówka.
    - **Usuń pole:** Ukryte w menu nagłówka (akcja rzadka/destrukcyjna).
- **Pole Systemowe:** Wymaga wyjaśnienia działania (tooltip/wiki) i ewentualnej zmiany nazwy (np. "Nieobjęte podpisem"), jeśli jego jedyną funkcją jest wyłączenie z podpisu.

### Zadania
- **Kamil Dubaniowski:** Przygotowanie finalnego projektu w Figmie.

---

## 4. Uspójnienie Frontend (Style i Komponenty)

**Komponent:** Frontend / Design System

### Cel i problem
Brak spójności wizualnej między elementami tworzonymi przez różnych programistów (np. różne wysokości wierszy w tabelach: 12px vs 8px vs 4px).

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- Należy wymusić regularne spotkania zespołu frontendowego (Filip, Przemek) w celu ustalania wspólnych standardów i tworzenia re-używalnych komponentów.
- Tabele i inne elementy interfejsu muszą mieć spójne parametry (paddingi, marginesy) w całym systemie.

---

## Punkty do dalszej dyskusji (globalne)

- Szczegóły implementacji podglądu reguł powiązanych z polem.
- Weryfikacja działania flagi "Pole systemowe".
- Ostateczna decyzja o układzie akcji w nagłówku nowego Prawego Panelu.

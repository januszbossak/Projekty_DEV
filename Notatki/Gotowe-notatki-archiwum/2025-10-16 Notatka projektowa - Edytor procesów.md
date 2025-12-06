> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

**Data:** 2025-10-16
**Temat główny:** Edytor procesów – diagram i formularz

**Powiązane projekty:**
- `Moduly/Edytor-procesow/Edytor-diagramu`
- `Moduly/Edytor-procesow/Edytor-formularzy`
- `Moduly/Edytor-procesow/Matryca-uprawnien`
- `Moduly/Ustawienia-systemowe`

---

## 1. Edytor Diagramu

**Komponent:** Edytor Diagramu

### Cel i problem

Wizualizacja procesu biznesowego na diagramie. Kluczowe kwestie to czytelność przy skomplikowanych procesach (plątanina linii) oraz ergonomia edycji (dodawanie reguł, edycja etapów).

### Rozważane alternatywy (Układ linii)

| Opcja | Opis | Status |
|-------|------|--------|
| **ELK (Hierarchiczny)** | Algorytm ze scalaniem linii (autostrada). Bardziej uporządkowany przy skomplikowanych procesach. | ✅ Wybrana (jako opcja) |
| **Daggre (Podstawowy)** | Algorytm bez scalania linii. Prostszy układ. | ✅ Wybrana (jako opcja) |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zdecydowano o wprowadzeniu przełącznika trybów wyświetlania oraz kierunku diagramu.

**Ustalenia interfejsowe:**
1. **Przełącznik układu:**
   - Dostępny pod ikoną "koła zębatego" (Ustawienia/Widok).
   - Opcje: **Hierarchiczny** (ELK ze scalaniem) / **Podstawowy** (Daggre).
   - Ewentualnie warianty pośrednie ("Zwarty"), ale stanęło na prostych nazwach.
2. **Przełącznik kierunku:**
   - Opcje: **Pionowy** (Góra-Dół) / **Poziomy** (Lewo-Prawo).
   - Dostępny w tym samym menu co układ.

**Funkcjonalności edycji:**
- **Przerywane linie:** Oznaczają brak reguły (niedokończony proces). Kliknięcie w biały kwadracik na linii ma otwierać edycję reguły.
- **Edycja reguły:** Kliknięcie w istniejącą regułę otwiera okno edycji.
  - **Rozwiązanie tymczasowe:** Wyświetlanie starego okna edycji reguły (iframe/popup) w nowym interfejsie React.
  - **Docelowo (Q1 2026?):** Nowy edytor reguł w React.

**Inne uwagi wizualne:**
- Górny pasek jest zbyt jaskrawy – do przygaszenia/zmiany koloru (np. na biały).
- Tooltipy dla długich nazw reguł (zrobione) i etapów (w trakcie realizacji).

### Ograniczenia / Poza zakresem

- Nowy edytor reguł (React) nie jest częścią obecnego wdrożenia (używamy starego okna w iframe).
- Prawy panel do edycji ustawień etapu – prawdopodobnie przyszły kwartał.

---

## 2. Edytor Formularza

**Komponent:** Edytor Formularza

### Cel i problem

Odwzorowanie wyglądu formularza (podgląd) w trybie edycji, aby był jak najbardziej zbliżony do widoku na sprawie ("What You See Is What You Get").

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zaakceptowano obecny wygląd formularza w edytorze, mimo drobnych różnic względem widoku sprawy.

**Szczegóły:**
- **Odstępy pionowe (padding):** Są mniejsze (ciaśniej upakowane pola) niż na sprawie.
- **Decyzja:** Przemysław Sołdacki uznał to za zaletę ("więcej widać naraz") i zaakceptował różnicę. Nie będziemy sztucznie zwiększać odstępów.
- **Układ kolumn:** Zachowanie przy 2 i 3 kolumnach jest akceptowalne.

### Punkty otwarte / Do poprawy

- **Drag & Drop:** Przy przeciąganiu pola między wiersze brakuje wizualnego wskaźnika wstawiania (miejsca docelowego). Przemysław Rogaś ma to poprawić.

---

## 3. Inne komponenty i plany

**Komponent:** Ustawienia systemowe / Różne

### Decyzja / Sposób realizacji

**Status:** 🔍 Planowane

1. **Macierz uprawnień i Lista pól:**
   - Realizowane przez Filipa. Status "W trakcie" lub "Skończone" (do weryfikacji).
   - Uwaga Przemysława Sołdackiego: Zbyt dużo ikonek "łańcuszka" (dziedziczenia) – pokazywać ikonę tylko gdy NIE ma dziedziczenia? (Do sprawdzenia z Kamilem).

2. **Kolejne zadania (Przemysław Rogaś):**
   - Przejście do prac nad **Ustawieniami systemowymi**.
   - Funkcjonalność: Potwierdzenie zmian przez innego administratora ("Four-eyes principle"?).

---

## Punkty do dalszej dyskusji (globalne)

- **Nazewnictwo:** Potwierdzenie ostatecznych nazw dla układów diagramu (Hierarchiczny/Podstawowy) z zespołem (Damian).
- **Terminologia:** Znak końca procesu na diagramie – weryfikacja czy w układzie ELK (Hierarchicznym) zawsze ląduje na końcu/dole.

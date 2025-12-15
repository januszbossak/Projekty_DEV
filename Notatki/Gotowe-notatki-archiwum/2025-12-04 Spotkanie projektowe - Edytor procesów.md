# Notatka projektowa – 2025-12-04 – Edytor formularzy (lista pól)

**Data:** 2025-12-04  
**Typ:** Spotkanie projektowe  
**Temat główny:** Edytor formularzy - prezentacja nowego interfejsu listy pól

---

## 1. Edytor formularzy - lista pól (nowy interfejs)

**Komponent:** Edytor formularzy

### Kontekst i cel

Prezentacja ukończonego interfejsu listy pól w edytorze formularzy (React). Nowy mechanizm dodawania pól i sekcji zastępuje dotychczasowy widok. Główne cele: lepsze UX dla twórców procesów, wizualne wskazanie miejsca dodania pola, spójność z koncepcją "dodawanie pod elementem". Filip Liwiński dopracował metodę budowania UI, która była pokazywana w formie roboczej w poniedziałek.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Nowy interfejs listy pól został ukończony i zaakceptowany. Główne cechy:
- **Plusik po lewej stronie** - dodawanie nowego pola lub sekcji (oddzielone od akcji związanych z polem)
- **Dodawanie pola "pod spodem"** - domyślnie nowe pole dodaje się bezpośrednio pod polem, z którego kliknięto plus
- **Dodawanie z poziomu sekcji** - plus przy sekcji dodaje pole na końcu sekcji (zgodnie z dotychczasową zasadą)
- **Podświetlanie miejsca dodania** - wizualne wskazanie dokładnego miejsca gdzie pole się pojawi
- **Obsługa pustej sekcji** - placeholder "sekcja jest pusta" z możliwością dodania pierwszego pola (zachowanie spójności - dodawanie z tego samego miejsca)
- **Spójność przycisków w modalach** - "Anuluj" po lewej, "Dodaj" po prawej (weryfikacja Przemka)

**Feedback uczestników:**
- Przemek: "jest zajebiście", brak uwag
- Mateusz (konsultant, oglądał wcześniej): pozytywny feedback, chce na tym pracować

### Zadania / Dalsze kroki

- **Kamil Dubaniowski:** Dopracować search (wyszukiwanie pól na liście) → termin: grudzień
- **Kamil Dubaniowski:** Dodać funkcję zwiń/rozwiń wszystkie sekcje → termin: grudzień
- **Przemek Rogaś:** Dopracować wygląd panelu ustawień pola (już rozpisane zadanie w sprincie)

---

## 2. Matryca uprawnień

**Komponent:** Edytor formularzy

### Kontekst i cel

Krótka wzmianka o działającej matrycy uprawnień. Moduł działa, nie ma obecnie planów rozwoju poza drobnymi usprawnieniami (search, zwiń/rozwiń).

### Decyzja / Ustalenie

**Status:** ✅ Funkcjonalność działa

Matryca uprawnień jest gotowa i funkcjonalna. Plany rozwoju:
- Search (przejście bezpośrednio do pola)
- Zwiń/rozwiń wszystkie elementy (ułatwienie skupienia się na ustawieniach sekcji)

---

## 3. Okno edycji reguły tabeli

**Komponent:** Edytor formularzy

### Kontekst i cel

Reguła tabeli otwierała się w nowej karcie. Filip zaimplementował otwarcie w modalnym oknie. Zmiana niezbędna aby zamknąć temat edytora formularzy bez ruszania modułu reguł - to jedyne miejsce wejścia do edytora reguł z listy pól.

### Decyzja / Ustalenie

**Status:** ✅ Zaimplementowane

Okno edycji reguły tabeli otwiera się teraz w modalnym oknie (zamiast nowej karty). Okno musi być duże (prawie pełny ekran). Edytor pozostaje stary (nie React), będzie wymieniony później wraz z całym modułem reguł. Na ten moment: odwzorowanie funkcjonalności aby zamknąć edytor formularzy bez zależności od reguł.

---

## 4. Nawigacja w górnej belce

**Komponent:** Edytor formularzy

### Kontekst i cel

Filip pracuje nad przywróceniem nawigacji w górnej belce (powrót do starego sposobu). Kamil uważa, że na ten moment jest to lepsze rozwiązanie niż utrzymywanie obu widoków (tabelka rozwijana vs wejście do środka).

### Decyzja / Ustalenie

**Status:** 🔄 W trakcie implementacji

Powrót do starego sposobu nawigacji - lista z możliwością rozwinięcia tabeli (nie tylko wejście do środka). Decyzja o utrzymaniu obu widoków odłożona - najpierw stabilny widok listy w dużych wdrożeniach, później ewentualne uzupełnienie o drugi widok.

**Szczegóły techniczne:**
- Filip pracuje nad implementacją
- Priorytet: czytelna lista w dużych wdrożeniach

---

## 5. Plan wydania grudniowego

**Komponent:** Edytor formularzy

### Kontekst i cel

Ustalenie zakresu wydania grudniowego i potwierdzenie że inne komponenty edytora procesów nie będą ruszane w tym roku.

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

**Wydanie grudniowe:**
- Edytor formularzy (lista pól) - ukończony, z drobnymi usprawnieniami (search, zwiń/rozwiń)
- Zamknięcie tematu edytora formularzy jako pierwszej dużej części edytora procesów w nowej technologii

**Poza zakresem (nie ruszamy w 2025):**
- Edytor diagramu
- Edytor reguł

**Uzasadnienie:** Skupienie na dopracowaniu jednej dużej funkcjonalności (edytor formularzy) zamiast robienia wszystkiego na raz. Po wydaniu - zbieranie feedbacku od konsultantów z wdrożeń produkcyjnych.

---

## 6. Roadmapa długoterminowa - edytor procesów

**Komponent:** Edytor procesów

### Kontekst i cel

Przemek podkreślił znaczenie ukończenia edytora formularzy jako pierwszego z trzech głównych komponentów edytora procesów.

### Decyzja / Ustalenie

**Status:** 💡 Plan długoterminowy

**Kolejność rozwoju edytora procesów:**
1. ✅ Edytor formularzy - ukończony (grudzień 2025)
2. 🔜 Edytor diagramu - do realizacji
3. 🔜 Edytor reguł - do realizacji
4. 🔜 Powiązania między komponentami - po ukończeniu wszystkich trzech:
   - Z poziomu formularza: widok reguł dotyczących pól
   - Z poziomu reguły: przejście do pól, których dotyczy
   - Inne cross-referencje między diagramem, formularzem i regułami

**Uzasadnienie:** Edytor formularzy jako kluczowa część systemu, teraz w nowej technologii i z nowym UX. Po dopracowaniu - skupienie na diagramie i regułach, a następnie na powiązaniach między komponentami.

### Punkty otwarte

- Termin rozpoczęcia prac nad edytorem diagramu - do ustalenia
- Termin rozpoczęcia prac nad edytorem reguł - do ustalenia
- Szczegóły implementacji powiązań między komponentami - do doprecyzowania po ukończeniu wszystkich trzech edytorów


---
tags:
  - JRWA
  - UseCase
klient: "[[LOT]]"
---
[[LOT JRWA UC]]

**Opis Grupy:** Ta grupa przypadków użycia (UC) opisuje **kluczowy moment styku** między codzienną pracą a archiwistyką: mechanikę i logikę "wpinania" (przypisywania) poszczególnych spraw AMODIT (instancji procesów, np. skanu pisma, umowy) do ich nadrzędnych, elektronicznych `Teczka_sprawy` (obiektów z Grupy 2).

Celem jest zapewnienie, że **każda sprawa AMODIT** zostanie poprawnie sklasyfikowana (ręcznie lub automatycznie) w odpowiedniej teczce macierzystej, podteczce lub teczce zbiorczej, realizując tym samym zasady rzeczowej klasyfikacji akt z Instrukcji Kancelaryjnej LOT.

### **UC-JRWA-LNK-001 – Przypięcie sprawy AMODIT do istniejącej `Teczka_sprawy` JRWA**

**Rola:** Użytkownik merytoryczny / Koordynator kancelaryjny

**Cel:** Powiązanie sprawy (instancji procesu AMODIT) z już istniejącą elektroniczną reprezentacją teczki rzeczowej JRWA (obiektem z Grupy 2).

**Opis:** Podczas rejestracji sprawy (np. pisma przychodzącego, umowy, wniosku) użytkownik wybiera w polu „Teczka sprawy JRWA” istniejącą teczkę z listy aktywnych teczek (wszystkich 3 typów: macierzystych, podteczek, zbiorczych).

System udostępnia wyszukiwarkę umożliwiającą odnalezienie teczki po symbolu JRWA, tytule, znaku sprawy, roku lub komórce.

Po wyborze teczki system automatycznie uzupełnia w sprawie metadane pobrane z teczki (symbol JRWA, kategoria archiwalna, pełny znak sprawy – o ile teczka go posiada).

Powiązanie jest dwukierunkowe — w teczce pojawia się nowa pozycja na liście powiązanych spraw (realizując `UC-JRWA-LNK-006`), a w sprawie widoczny jest link do teczki.

### **UC-JRWA-LNK-002 – Kontekstowe utworzenie nowej `Teczka_sprawy` JRWA „w locie” z poziomu sprawy**

**Rola:** Użytkownik merytoryczny

**Cel:** Inteligentne założenie nowej teczki JRWA (jednego z 3 typów) bezpośrednio podczas pracy nad sprawą, gdy właściwa teczka jeszcze nie istnieje.

**Opis:** W formularzu sprawy AMODIT (np. Korespondencja) użytkownik ma przy polu „Teczka sprawy JRWA” przycisk **„➕ Utwórz nową teczkę JRWA”**.

Kliknięcie **nie** otwiera uniwersalnego formularza, lecz uruchamia logikę kontekstową bazującą na **wybranej klasie JRWA** (ze słownika z Grupy 1):

1. **Scenariusz A (Teczka zbiorcza):** Jeśli klasa JRWA jest oznaczona jako nietworząca akt sprawy (np. `340` - Dowody księgowe), system w tle tworzy nową `Teczka_sprawy` typu "zbiorcza" (zgodnie z `UC-JRWA-SPR-002`), nadając jej tylko znak `BF.340.2025` i automatycznie wpina do niej bieżącą sprawę (np. fakturę).
    
2. **Scenariusz B (Podteczka):** Jeśli klasa JRWA jest oznaczona jako wymagająca podteczek (np. `120` - Akta osobowe), system prosi użytkownika o wskazanie "Sprawy-matki" (np. `BK.120.1.2025 - Akta osobowe`) i podanie tytułu podteczki (np. "Jan Kowalski"), po czym tworzy nową `Teczka_sprawy` typu "podteczka" (zgodnie z `UC-JRWA-SPR-001a`) ze znakiem 5-członowym i wpina do niej bieżącą sprawę.
    
3. **Scenariusz C (Teczka macierzysta):** We wszystkich pozostałych przypadkach system tworzy standardową `Teczka_sprawy` (zgodnie z `UC-JRWA-SPR-001`), nadając jej kolejny numer i znak 4-członowy (np. `BA.032.1.2025`) i wpina do niej bieżącą sprawę.
    

To rozwiązanie odzwierciedla praktykę kancelaryjną i wymusza poprawną strukturę teczek zgodną z Instrukcją LOT.

### **UC-JRWA-LNK-003 – Przypięcie sprawy do teczki na późniejszym etapie procesu**

**Rola:** Użytkownik merytoryczny / Koordynator kancelaryjny

**Cel:** Powiązanie sprawy z teczką JRWA w momencie, gdy dopiero w toku obiegu wiadomo, do jakiego zagadnienia należy dana sprawa (np. po dekretacji).

**Opis:** W niektórych procesach (np. Reklamacje, Pisma ogólne) klasyfikacja nie jest znana w Kancelarii. Pole „Teczka sprawy JRWA” pozostaje puste na początku.

Dopiero pracownik merytoryczny na etapie (np. „Weryfikacja merytoryczna”) ma obowiązek przypisania sprawy. Wykonuje wtedy akcję **„Przypisz do teczki JRWA”**, która pozwala mu zrealizować `UC-JRWA-LNK-001` (wybór istniejącej) lub `UC-JRWA-LNK-002` (stworzenie nowej).

Decyzja o przypisaniu jest rejestrowana w historii sprawy (kto, kiedy, do jakiej teczki przypiął).

### **UC-JRWA-LNK-004 – Wymuszenie przypisania sprawy do `Teczka_sprawy` przed jej zamknięciem**

**Rola:** System / Administrator JRWA

**Cel:** Zapewnienie, że **każda** sprawa w systemie AMODIT (zarówno tworząca, jak i nietworząca akta sprawy) zostanie poprawnie sklasyfikowana przed jej zakończeniem.

**Opis:** Administrator JRWA konfiguruje wymóg przypisania teczki dla wszystkich procesów kancelaryjnych.

Podczas próby zakończenia sprawy (np. zamknięcia obiegu pisma) system sprawdza, czy pole „Teczka sprawy JRWA” jest wypełnione.

Jeśli nie — użytkownik otrzymuje komunikat o konieczności przypisania sprawy (zgodnie z `LNK-001`, `LNK-002` lub `LNK-003`).

Dzięki temu żadna sprawa nie pozostaje "zawieszona" poza klasyfikacją rzeczową, a kompletność JRWA jest zachowana. To kluczowa kontrola jakości danych kancelaryjnych.

### **UC-JRWA-LNK-005 – Automatyczne przypisanie spraw do teczek JRWA przez reguły systemowe**

**Rola:** Administrator JRWA / System    **Cel:** Automatyczne przypinanie spraw do teczek JRWA na podstawie zdefiniowanych reguł biznesowych, bez udziału użytkownika (dla procesów masowych).

**Opis:** Administrator JRWA może definiować reguły przypisania, np.:

- „Dla procesu `P_Faktura` zawsze przypinaj do `Teczka_sprawy` typu zbiorcza (UC-SPR-002) o klasie `340` i zgodnym roku”.
    
- „Dla procesu `P_Urlop` (pracownika X) zawsze przypinaj do `Teczka_sprawy` typu podteczka (UC-SPR-001a) o tytule 'Jan Kowalski' (BK.120.7.x.ROK)”.
    

System automatycznie przypisuje sprawy podczas ich rejestracji. Użytkownik widzi powiązanie w polu JRWA, ale nie musi wykonywać żadnej akcji.

Ten mechanizm minimalizuje błędy i odciąża pracowników przy procesach powtarzalnych.

### **UC-JRWA-LNK-006 – Przegląd spraw przypiętych do teczki JRWA (Spis spraw)**

**Rola:** Użytkownik merytoryczny / Archiwista

**Cel:** Przegląd wszystkich spraw powiązanych z daną `Teczka_sprawy` w celu oceny kompletności akt (realizacja elektronicznego "Spisu spraw" z § 24 Instrukcji LOT).

**Opis:** Na formularzu `Teczka_sprawy` (z Grupy 2) znajduje się raport lub zakładka „Zawartość teczki / Spis spraw”.

Raport ten prezentuje wszystkie sprawy AMODIT przypięte do tej teczki i zawiera kolumny zgodne z wymogami dla spisu spraw (np. Tytuł sprawy, data wszczęcia, data zakończenia, osoba prowadząca).

Użytkownik może filtrować, sortować i otwierać sprawy bezpośrednio z widoku teczki.

Archiwista wykorzystuje ten raport do weryfikacji kompletności akt przed przekazaniem teczki do archiwum (proces `UC-JRWA-SPR-006`).

### **UC-JRWA-LNK-007 – Przeniesienie sprawy do innej teczki JRWA (Korekta błędnego przypięcia)**

**Rola:** Koordynator kancelaryjny / Administrator JRWA

**Cel:** Korekta błędnego powiązania sprawy z teczką JRWA przy zachowaniu integralności danych i pełnej historii zmian.

**Opis:** Jeśli sprawa została przypisana do niewłaściwej teczki (np. do teczki z 2024 zamiast 2025, lub do złej klasy merytorycznej), uprawniony użytkownik może ją "przenieść".

Operacja ta polega na odpięciu sprawy od teczki A i przypięciu jej do teczki B.

System **wymaga podania uzasadnienia** i **zapisuje całą operację w historii (audycie) sprawy** (z informacją: kto, kiedy, z jakiej teczki, do jakiej teczki przeniósł, i dlaczego).

Dzięki temu można korygować błędy klasyfikacji bez utraty danych i z zachowaniem pełnej ścieżki kancelaryjnej.

## **Najważniejsze do zapamiętania**

> Powiązanie spraw z teczkami JRWA to kluczowy moment, w którym system AMODIT staje się zgodny z logiką kancelaryjną LOT.
> 
> Użytkownik może przypinać sprawy do teczek ręcznie (na początku lub w trakcie procesu) albo system może zrobić to automatycznie. Funkcja "Utwórz nową" musi być kontekstowa i rozróżniać 3 typy teczek z Grupy 2.
> 
> Każda sprawa AMODIT musi trafić do właściwej `Teczka_sprawy` **przed jej zakończeniem**, a administrator ma narzędzia do egzekwowania tego obowiązku i korygowania błędów.
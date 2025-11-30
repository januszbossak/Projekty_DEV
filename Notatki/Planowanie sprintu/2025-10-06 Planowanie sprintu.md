# Planowanie Sprintu – 2025-10-06

**Sprint:** 41 (planowany)
**Okres:** 2025-10-06 - 2025-10-20 (przybliżony)

**Powiązane projekty:**
- `moduly/Modul-raportowy-stary` – tematy 1, 4
- `cross-cutting/Wyszukiwanie` - temat 2
- `moduly/Repozytorium` - temat 3
- `cross-cutting/UX-UI` - temat 5
- `cross-cutting/Proces-wytworczy` - temat 6

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Zadania ze sprintu 39 | `N/A` | ➡️ Przeniesione | Ok. 125 zadań przechodzi na nowy sprint. |
| Testy | `N/A` | 🔄 W testach | 70 zadań z poprzedniego sprintu + ok. 50 zadań "spadających" czeka na testy, co tworzy wąskie gardło. |

---

## 2. Plany na sprint

### Błąd w starych raportach

**Projekt:** `moduly/Modul-raportowy-stary`

**Kontekst i cel:**
U jednego z klientów występuje błąd `different number of columns` przy eksporcie raportu, który agreguje dane z dwóch różnych procesów. Problem występuje na starej, grudniowej wersji systemu i uniemożliwia użytkownikowi pracę.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Zdiagnozowanie błędu poprzez analizę zapytań SQL | **Damian** / **Piotr** | - | Włączenie logowania `Report Log` u klienta. |
| Ewentualna poprawka | TBD | - | Wynik analizy logów. |

**Szczegóły techniczne**:
- Błąd prawdopodobnie wynika z różnic w uprawnieniach do kolumn między procesami.
- Sugerowane rozwiązanie to zalogowanie pełnego zapytania SQL po stronie klienta, aby zidentyfikować brakującą lub nadmiarową kolumnę.

**Ryzyka:**
- Brak możliwości odtworzenia błędu lokalnie z powodu braku dostępu do procesów klienta.

---

### Wyszukiwanie w polu słownikowym

**Projekt:** `cross-cutting/Wyszukiwanie`

**Kontekst i cel:**
Poprawić logikę wyszukiwania dla pól słownikowych podrzędnych, aby system jednoznacznie identyfikował wartość, gdy ta sama fraza występuje w wielu miejscach.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Zaprojektowanie i implementacja mechanizmu definiowania kontekstu wyszukiwania | **Piotr** | - | - |

---

### Niewidoczne sprawy w Repozytorium

**Projekt:** `moduly/Repozytorium`

**Kontekst i cel:**
Funkcjonalność Repozytorium nie wyświetla spraw zamkniętych, co jest niezgodne z oczekiwaniami klienta (**Rossmann**). Naprawa błędu jest pilna, ponieważ obecna sytuacja powoduje problemy wydajnościowe (ładowanie listy trwa ponad minutę).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawka w funkcji `GetCases`, aby uwzględniała sprawy zamknięte | **Marek** | 1d | - |

**Decyzje podjęte przy planowaniu:**
- Zadanie jest traktowane jako **Hotfix** ze względu na duży wpływ na wydajność u klienta.

**Ryzyka:**
- Po zmianie w repozytorium klienta pojawi się nagle ponad 200 spraw, które wcześniej były ukryte. Klient musi zostać o tym poinformowany.

---

### Opisy raportów na Dashboardach

**Projekt:** `moduly/Modul-raportowy-stary`, `cross-cutting/UX-UI`

**Kontekst i cel:**
Ujednolicenie sposobu wyświetlania opisów dla raportów. Obecnie opisy są widoczne na liście raportów, ale brakuje ich na kafelkach dashboardów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Dodanie przycisku/opcji "Pokaż opis" w menu kafelka na dashboardzie | **Ania** | - | Zadanie o niższym priorytecie, do wykonania po zakończeniu prac nad raportami systemowymi. |

**Decyzje podjęte przy planowaniu:**
- Opis na dashboardach będzie wyświetlany w oknie modalnym, po kliknięciu opcji w menu.
- Łukasz Bott stworzy osobne zgłoszenie na ujednolicenie wyświetlania opisów bezpośrednio pod listą wyników w samych raportach (nie na dashboardach).

---

## 3. Dyskusje strategiczne i procesowe

### Walidacja pola "numer telefonu"

**Projekt:** `cross-cutting/UX-UI`
**Status:** 💡 Do weryfikacji
**Uzasadnienie:** Zgłoszono, że pole akceptuje znaki nienumeryczne. Rozpoczęto dyskusję, czy wprowadzać ścisłą walidację, ale pojawiło się ryzyko zablokowania możliwości wprowadzania numerów z prefiksami czy numerami wewnętrznymi. **Temat przeniesiony na Radę Architektów**.

### Ograniczenie listy użytkowników w polach systemowych

**Projekt:** `cross-cutting/UX-UI`
**Status:** 💡 Do weryfikacji
**Uzasadnienie:** Propozycja, aby móc ograniczyć listę osób dostępnych w polach "Współpracownicy" i "Obserwatorzy" do zdefiniowanej grupy. **Temat przeniesiony na Radę Architektów**.

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Ogromne zaległości w testach | `cross-cutting/Proces-wytworczy` | Krytyczny | Zmiana procesu planowania, wprowadzenie `Capacity`, priorytetyzacja testów. | **Kamil**, **Damian**, **Michał** |
| Brak jednoznacznego procesu planowania | `cross-cutting/Proces-wytworczy` | Wysoki | Wprowadzenie nowego modelu planowania (spotkania indywidualne, szacowanie `effortu`). | **Kamil** |
| Brak zgłoszeń na wszystkie prace | `cross-cutting/Proces-wytworczy` | Średni | Zwiększenie dyscypliny w tworzeniu zgłoszeń na każdą pracę, w tym poprawki i zadania weekendowe. | Zespół |
| Niejasny status zadań w `design` i `evaluating` | `cross-cutting/Proces-wytworczy` | Średni | Zmiana procesu: zadania w tych statusach nie powinny być przypisywane do sprintu, a zarządzane na poziomie **Backlogu**. | **Kamil**, **Damian**, **Łukasz** |

---

## 5. Organizacja pracy

- **Nowy model planowania sprintu:** Zostaje wdrożony nowy proces oparty o indywidualne sesje z deweloperami i szacowanie `effortu`.
- **Wprowadzenie `Effortu`:** Przyjęto skalę, gdzie **effort 5** oznacza cały dzień pracy (8h). Deweloperzy mają uzupełnić `effort` dla wszystkich zadań w sprincie do końca dnia.
- **Zmiana formuły Daily:** Rozważana jest zmiana formuły spotkań daily - zamiast przeglądu wpisów w Jirze, każdy ma omawiać swoją tablicę zadań na sprincie.
- **Zasady przepinania zadań:** Ustalono, że automatycznie na kolejny sprint przechodzą tylko zadania w statusach `In Progress` i `Waiting for tests`. Zadania `Ready To Do`, `In Design` itd. wymagają ponownej analizy i priorytetyzacji.

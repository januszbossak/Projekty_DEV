---
name: overview-sync
description: Synchronizacja dokumentacji projektów (PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md) z wpisami z CHANGELOG.md na podstawie inteligentnej analizy kontekstu
---

# SKILL: Overview Sync - Synchronizacja dokumentacji projektów

## Cel

Synchronizacja dokumentacji projektów (PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md) z CHANGELOG.md.

Agent przetwarza wpisy z CHANGELOG i aktualizuje odpowiednie pliki dokumentacji na podstawie **inteligentnej analizy kontekstu** (nie tylko tagów).

---

## Dane wejściowe

1. **Ścieżka projektu** - katalog projektu (np. `Projekty/Moduly/Edytor-formularzy/`)
2. **CHANGELOG.md** - plik z chronologiczną historią ustaleń
3. **Istniejące pliki dokumentacji** (jeśli aktualizacja):
   - PROJEKT.md
   - ARCHITEKTURA.md
   - ROADMAPA.md

---

## Krytyczne zasady

### 0. ZERO HALUCYNACJI (najważniejsze!)

- **NIGDY nie zmyślaj** informacji
- Jeśli w CHANGELOG brak danych → użyj `[DO UZUPEŁNIENIA]`
- Wypełniaj TYLKO na podstawie konkretnych info z CHANGELOG/Notatek

### 1. DEEP READ (Czytanie źródeł - OBOWIĄZKOWE)

- **ZAWSZE czytaj notatkę źródłową** wskazaną w CHANGELOG
- CHANGELOG to tylko spis treści - szczegóły (limity, parametry) są w notatce
- Ignorowanie treści notatki to błąd krytyczny

### 2. Inteligentna kategoryzacja

- **Czytaj treść** wpisu i notatki, nie tylko tag
- Szukaj słów kluczowych (technologia / funkcjonalność / biznes)
- Przypisz do pliku na podstawie **dominującego** typu treści

### 3. Agregacja

- Grupuj drobne wpisy tego samego typu
- Zachowaj źródło [[YYYY-MM-DD Nazwa]]
- **NIE AGREGUJ** szczegółów technicznych w ARCHITEKTURA.md (muszą być precyzyjne)

### 4. Chronologia

- W tabelach: najnowsze na górze
- Zachowuj porządek dat
- Trackuj `changelog_przeglad_do` w YAML frontmatter

### 5. Linkowanie Obsidian

- Projekty: `[[Nazwa-projektu]]`
- Notatki: `[[YYYY-MM-DD Nazwa notatki]]`
- Daty: `[[YYYY-MM-DD]]`

### 6. Poziomy projektów

- **Klient zbiorczy:** tylko [Nazwa].md z tabelą (nie 3 pliki)
- **Projekt zbiorczy:** 3 pliki + sekcja Podprojekty w ROADMAPA.md
- **Podprojekt / prosty:** 3 pliki standardowe

---

## Workflow główny

### 1. Sprawdzenie co istnieje

```
if PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md exist:
    → AKTUALIZACJA (workflow A)
else:
    → INICJALIZACJA (workflow B)
```

---

## Workflow A: AKTUALIZACJA (pliki istnieją)

### Krok 1: Wyciągnij ostatnią przetworzoną datę

Przeczytaj YAML frontmatter z każdego pliku:

```yaml
---
ostatnia_aktualizacja: 2025-12-08
changelog_przeglad_do: 2025-11-13  ← ta data jest kluczowa
---
```

### Krok 2: Pobierz nowe wpisy z CHANGELOG

1. Przeczytaj `CHANGELOG.md`
2. Weź **TYLKO wpisy po dacie** `changelog_przeglad_do`
3. Ignoruj wpisy starsze lub równe tej dacie (już przetworzone)

### Krok 3: Dla każdego nowego wpisu - INTELIGENTNA KATEGORYZACJA

**KRYTYCZNE:** NIE opieraj się tylko na tagu! Musisz przeczytać treść wpisu.

#### Algorytm dla każdego wpisu:

```
FOR każdy wpis w CHANGELOG (w zakresie do przetworzenia):

  1. Zidentyfikuj źródło:
     - Znajdź link do notatki: [Notatki/.../YYYY-MM-DD Nazwa.md]
     - Jeśli brak linku → bazuj tylko na treści wpisu w CHANGELOG (fallback)

  2. PRZECZYTAJ NOTATKĘ ŹRÓDŁOWĄ (Deep Read):
     - Otwórz plik notatki wskazywany w źródle
     - Znajdź sekcje dotyczące analizowanego projektu
     - Wyciągnij szczegóły (limity, parametry, uzasadnienia, ryzyka), których nie ma w skrócie CHANGELOG
     - TO JEST KROK OBOWIĄZKOWY - nie pomijaj czytania notatki!

  3. Analizuj PEŁNĄ TREŚĆ (szczegóły z notatki + wpis z CHANGELOG):
     
     SZUKAJ słów kluczowych i szczegółów technicznych:
     
     TECHNOLOGIA/ARCHITEKTURA:
     - Technologie: OAuth2, React, .NET, MSSQL, Docker, SignalR, Kubernetes
     - Słowa: "endpoint", "API", "baza danych", "tabela", "integracja", 
            "microservice", "architektura", "struktura"
     - Koncepcje: "komunikacja między", "wymiana danych", "protokół"
     
     FUNKCJONALNOŚĆ/ROADMAPA:
     - Akcje użytkownika: "użytkownik może", "dodano przycisk", "nowy formularz"
     - Features: "drag & drop", "wyszukiwarka", "filtrowanie", "eksport"
     - Status: "ukończone", "w trakcie", "zaplanowane", "odroczone", "wdrożone"
     - Słowa: "MVP", "sprint", "wydanie", "wersja", "release"
     - Bugi: "naprawiono", "bug", "błąd", "fix"
     
     BIZNES/PROJEKT:
     - Cele: "obniżenie kosztów", "przyspieszenie", "redukcja błędów"
     - Metryki: "40% szybciej", "KPI", "ROI", "oszczędność", "wzrost"
     - Organizacja: "zespół", "budżet", "termin", "klient", "umowa"

  4. Przypisz do kategorii na podstawie DOMINUJĄCEGO typu treści (nie tagu!)
  5. Jeśli mieszane (np. tech + funkcjonalność) → wybierz dominujący aspekt

END FOR
```

#### Tabela przykładów kategoryzacji:

| Tag w CHANGELOG | Treść wpisu | Słowa kluczowe | Plik docelowy | Sekcja |
|----------------|-------------|----------------|---------------|--------|
| `#Decyzja` | "Używamy OAuth2 zamiast custom tokenów" | OAuth2, tokenów | **ARCHITEKTURA.md** | Tabela decyzji |
| `#Decyzja` | "Zmieniamy termin MVP2 na grudzień 2025" | MVP2, termin, grudzień | **ROADMAPA.md** | Status MVP / Planowane |
| `#Decyzja` | "Zwiększamy budżet o 10 MD" | budżet, 10 MD | **PROJEKT.md** | Budżet/timeline |
| `#Funkcjonalność` | "Dodano drag & drop sekcji w edytorze" | drag & drop, dodano | **ROADMAPA.md** | Status funkcjonalności |
| `#Architektura` | "Wydzielenie blockchain do microservice Docker" | microservice, Docker, wydzielenie | **ARCHITEKTURA.md** | Decyzje / Komponenty |
| `#Bug` | "Naprawiono czyszczenie pola daty" | naprawiono, błąd | **ROADMAPA.md** | Znane ograniczenia → po fix: Produkcja |
| `#Sprint-review` | "Ukończono wyszukiwarkę pól" | ukończono, wyszukiwarka | **ROADMAPA.md** | ✅ Produkcja |
| `#Cel-biznesowy` | "Skrócenie czasu wdrożeń o 40%" | 40%, skrócenie, wdrożeń | **PROJEKT.md** | Cele biznesowe / Metryki |

### Krok 4: Zaktualizuj odpowiednie pliki

#### PROJEKT.md - aktualizacje:

- **Cele biznesowe:** Jeśli wpis zawiera nowy cel → dodaj do sekcji "Cele biznesowe"
- **Metryki sukcesu:** Jeśli wpis zawiera konkretną metrykę → dodaj do sekcji "Metryki"
- **Budżet/timeline:** Jeśli wpis o budżecie/terminach → zaktualizuj tabelę
- **Zespół:** Jeśli wpis o zmianach w zespole → zaktualizuj tabelę zespołu

**NIE NADPISUJ** istniejących informacji - tylko **uzupełniaj** jeśli są nowe dane.

#### ARCHITEKTURA.md - aktualizacje:

- **Stack techniczny:** Jeśli wpis o nowej technologii → dodaj do listy stack. **Zachowuj szczegóły** (np. wersje, konkretne biblioteki).
- **Główne komponenty:** Jeśli wpis definiuje komponenty (np. struktura folderów) → opisz je z uwzględnieniem **limitów i ograniczeń** (np. "max 20 poziomów", "limit 2000 obiektów"). Nie stosuj nadmiernych uproszczeń.
- **Integracja z AMODIT:** Jeśli wpis o nowym endpoincie/integracji → dodaj do listy
- **Tabela decyzji:** Jeśli wpis o decyzji technicznej → dodaj nowy wiersz:
  ```
  | [[2025-12-08]] | Decyzja z wpisu | Uzasadnienie z wpisu | ✅ Wdrożone | [[2025-12-08 Rada]] |
  ```
- **Historia odrzuconych:** Jeśli wpis o odrzuconej koncepcji → dodaj do tabeli odrzuconych

**Agregacja:** Jeśli jest wiele drobnych decyzji tego samego typu, rozważ agregację w jednym wierszu.

#### ROADMAPA.md - aktualizacje:

- **✅ Produkcja:** Jeśli wpis o ukończonej funkcjonalności → przenieś/dodaj do sekcji Produkcja
- **🛠️ W trakcie:** Jeśli wpis o funkcjonalności w realizacji → dodaj/zaktualizuj status
- **📋 Planowane:** Jeśli wpis o planowanej funkcji → dodaj do MVP3 lub nowego MVP
- **🗄️ Backlog:** Jeśli wpis o odroczonej funkcji → dodaj do Backlog
- **Znane ograniczenia:** Jeśli wpis o bugu (nienaprawionym) → dodaj do ograniczeń
- **Historia wydań:** Jeśli wpis ze Sprint review o wydaniu → dodaj wiersz do tabeli

**Agregacja funkcjonalności:**

Zamiast:
```
- ✅ Dodano przycisk Zwiń
- ✅ Dodano przycisk Rozwiń
- ✅ Dodano ustawienia kolumn
```

Zrób:
```
- ✅ Dodano funkcje UX (przyciski Zwiń/Rozwiń, ustawienia kolumn, panel właściwości) - [[2025-11-13 Notatka]]
```

**Statusy:**
- ✅ = ukończone, wdrożone, wydane (ze Sprint review)
- 🔄 = w trakcie, w realizacji (z notatek projektowych)
- ⏳ = zaplanowane (z planowania/Rady)
- ⚠️ = znane ograniczenie, bug (z notatek/bugów)

### Krok 5: Zaktualizuj metadane

W każdym zaktualizowanym pliku:

```yaml
---
ostatnia_aktualizacja: 2025-12-08  ← dzisiejsza data
changelog_przeglad_do: 2025-11-28  ← data najnowszego przetworzonego wpisu
---
```

---

## Workflow B: INICJALIZACJA (pliki nie istnieją)

### Krok 1: Sprawdź czy istnieje stary Project Canvas

```
if [Projekt].md exists (stary Project Canvas):
    → Zmień nazwę: [Projekt].md → [Projekt]-OLD-ProjectCanvas.md
    → Dodaj notatkę w starym pliku:
       "Ten plik został zastąpiony przez PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md [2025-12-08]"
```

### Krok 2: Skopiuj szablony

1. Skopiuj `Projekty/SZABLON-PROJEKT.md` → `[Projekt]/PROJEKT.md`
2. Skopiuj `Projekty/SZABLON-ARCHITEKTURA.md` → `[Projekt]/ARCHITEKTURA.md`
3. Skopiuj `Projekty/SZABLON-ROADMAPA.md` → `[Projekt]/ROADMAPA.md`

### Krok 3: Przeczytaj CAŁY CHANGELOG.md

Weź **wszystkie wpisy** z CHANGELOG (bo inicjalizacja, nie ma `changelog_przeglad_do`).

### Krok 4: Dla każdego wpisu - INTELIGENTNA KATEGORYZACJA

Użyj tego samego algorytmu co w Workflow A, Krok 3.

### Krok 5: Wypełnij 3 pliki na podstawie CHANGELOG

#### PROJEKT.md - inicjalizacja:

Przeszukaj wszystkie wpisy i wypełnij:

- **Problem:** Szukaj wpisów z kategorii #Problem / #Cel-biznesowy na początku projektu
- **Cele biznesowe:** Zbierz wszystkie cele biznesowe z wpisów
- **Metryki sukcesu:** Zbierz wszystkie konkretne metryki (%, liczby, KPI)
- **Budżet/timeline:** Szukaj wpisów o starcie projektu, MVP, budżecie
- **Zespół:** Zbierz informacje o osobach (PDM, Tech Lead, etc.)

**Jeśli brak którejkolwiek informacji → zostaw `[DO UZUPEŁNIENIA]`**

#### ARCHITEKTURA.md - inicjalizacja:

Przeszukaj wszystkie wpisy i wypełnij:

- **Stack techniczny:** Zbierz wszystkie technologie wymienione w wpisach (React, .NET, MSSQL...). Zachowuj szczegóły.
- **Główne komponenty:** Opisz komponenty systemu zachowując **parametry techniczne** (limity, role, konkretne liczby). Unikaj ogólników typu "zagnieżdżona struktura" - napisz "zagnieżdżona struktura (max 20 poziomów)".
- **Integracja z AMODIT:** Zbierz endpointy, tokeny, tabele współdzielone
- **Tabela decyzji:** Zbuduj tabelę ze wszystkich decyzji technicznych:
  - Data: data wpisu
  - Decyzja: treść decyzji
  - Dlaczego: uzasadnienie (jeśli jest w CHANGELOG)
  - Status: ✅ jeśli wdrożone, 💡 jeśli propozycja
  - Źródło: link do notatki [[YYYY-MM-DD Nazwa]]
- **Historia odrzuconych:** Zbierz odrzucone koncepcje (jeśli są w CHANGELOG)

**Sortuj tabelę decyzji chronologicznie (najnowsze na górze).**

#### ROADMAPA.md - inicjalizacja:

Przeszukaj wszystkie wpisy i wypełnij:

- **✅ Produkcja (MVP1):** Zbierz wszystkie ukończone funkcjonalności z wpisów #Sprint-review
- **🛠️ W trakcie (MVP2):** Zbierz funkcjonalności "w trakcie" / "w realizacji"
- **📋 Planowane (MVP3):** Zbierz funkcjonalności "zaplanowane" / "do zrobienia"
- **🗄️ Backlog:** Zbierz funkcjonalności "odroczone" / "backlog"
- **Historia wydań:** Zbuduj tabelę ze wszystkich wpisów Sprint review o wydaniach

**Agreguj funkcjonalności** (patrz: Workflow A, Krok 4).

### Krok 6: Ustaw metadane

```yaml
---
created: 2025-12-08  ← dzisiejsza data (tylko w PROJEKT.md)
ostatnia_aktualizacja: 2025-12-08  ← dzisiejsza data
changelog_przeglad_do: 2025-11-28  ← data najnowszego wpisu z CHANGELOG
---
```

---

## Obsługa specjalnych poziomów

### Poziom 1: Klient zbiorczy (np. Klienci/WIM/)

**Wykrywanie:** Ścieżka zawiera `Klienci/[Nazwa]/` i ma podkatalogi (projekty).

**Działanie:**
1. **NIE twórz** plików PROJEKT.md / ARCHITEKTURA.md / ROADMAPA.md na poziomie klienta
2. **Utwórz tylko** plik `[Nazwa-Klienta].md` (np. `WIM.md`) z szablonu SZABLON-KLIENT-ZBIORCZY.md
3. Przeszukaj wszystkie podkatalogi (projekty klienta)
4. Dla każdego projektu:
   - Przeczytaj `ROADMAPA.md` podprojektu
   - Wyciągnij: status, najbliższe MVP, zespół
5. Wygeneruj tabelę projektów w `[Nazwa-Klienta].md`

**Przykład struktury:**
```
Klienci/WIM/
├── WIM.md                          ← krótki dashboard (generowany)
├── Repozytorium-plikow-DMS/        ← projekt 1
│   ├── PROJEKT.md                  ← pełne pliki
│   ├── ARCHITEKTURA.md
│   ├── ROADMAPA.md
│   └── CHANGELOG.md
└── Podpis-kwalifikowany-macOS/     ← projekt 2
    ├── PROJEKT.md
    ├── ARCHITEKTURA.md
    ├── ROADMAPA.md
    └── CHANGELOG.md
```

### Poziom 2: Projekt zbiorczy (np. Edytor-procesow/)

**Wykrywanie:** Katalog ma podkatalogi które są podprojektami (każdy ma swój CHANGELOG.md).

**Działanie:**
1. **Utwórz** pełne 3 pliki na poziomie projektu zbiorczego
2. W `ROADMAPA.md` **dodaj sekcję** "📦 Podprojekty" na końcu
3. Przeszukaj wszystkie podkatalogi (podprojekty)
4. Dla każdego podprojektu:
   - Przeczytaj `ROADMAPA.md` podprojektu
   - Wyciągnij: status, najbliższe MVP, zespół
5. Wygeneruj tabelę podprojektów w sekcji "📦 Podprojekty"

**Przykład struktury:**
```
Moduly/Edytor-procesow/
├── PROJEKT.md                      ← pełne pliki dla całego projektu
├── ARCHITEKTURA.md
├── ROADMAPA.md                     ← + sekcja Podprojekty na końcu
├── CHANGELOG.md
├── Edytor-formularzy/              ← podprojekt 1
│   ├── PROJEKT.md
│   ├── ARCHITEKTURA.md
│   ├── ROADMAPA.md
│   └── CHANGELOG.md
└── Edytor-diagramu/                ← podprojekt 2
    ├── PROJEKT.md
    ├── ARCHITEKTURA.md
    ├── ROADMAPA.md
    └── CHANGELOG.md
```

### Poziom 3: Podprojekt / Prosty projekt

**Wykrywanie:** Katalog ma `CHANGELOG.md` i nie ma podkatalogów z własnymi CHANGELOG.

**Działanie:**
1. **Utwórz** pełne 3 pliki: PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md
2. Jeśli jest podprojektem (ma projekt nadrzędny):
   - W `PROJEKT.md` dodaj link: `**Projekt nadrzędny:** [[Edytor-procesow]]`

---

## Zasady agregacji (WAŻNE dla czytelności)

### Kiedy agregować?

**Agreguj** gdy w CHANGELOG jest wiele drobnych wpisów tego samego typu:

- ✅ DOBRE: "Dodano funkcje UX (wyszukiwanie, drag & drop, przyciski Zwiń/Rozwiń)" - [[2025-11-13]]
- ❌ ZŁE: Lista 15 bulletów, każdy "Dodano przycisk X"

### Jak agregować?

1. **Grupuj po dacie i typie:**
   - Wszystkie funkcje UI z jednej notatki → jeden bullet
   - Wszystkie decyzje architektoniczne z Rady → jeden/dwa wiersze tabeli

2. **Zachowaj źródło:**
   - Zawsze linkuj do notatki źródłowej [[YYYY-MM-DD Nazwa]]

3. **Przykład agregacji funkcjonalności:**

CHANGELOG ma:
```
## 2025-11-13 | Notatka projektowa
- Przywrócenie parzystości funkcjonalnej
- Ustawienia pól w prawym panelu
- Dodano przyciski Zwiń/Rozwiń
- Ustawienia ilości kolumn
```

ROADMAPA.md (po agregacji):
```
- ✅ Uzupełniono UX edytora (parzystość z starym widokiem, panel ustawień, przyciski Zwiń/Rozwiń, kolumny) - [[2025-11-13 Notatka]]
```

4. **Kiedy NIE agregować:**
   - Decyzje architektoniczne (każda osobno w tabeli)
   - Szczegóły techniczne i limity (muszą być precyzyjne w ARCHITEKTURA.md)
   - Odrzucone koncepcje (każda osobno)
   - Kluczowe milestone (wydania MVP)

---

## Weryfikacja przed zapisem

**Checklist:**

- [ ] **Przeczytałem treść wpisów** (nie tylko tagi)?
- [ ] **Zrobiłem DEEP READ** notatek źródłowych?
- [ ] **Kategoryzacja inteligentna** (analiza kontekstu)?
- [ ] **NIE ZMYŚLIŁEM** żadnych informacji?
- [ ] **Użyłem `[DO UZUPEŁNIENIA]`** tam gdzie brak danych?
- [ ] **Zaktualizowałem `changelog_przeglad_do`** na najnowszą datę?
- [ ] **Agregowałem** funkcjonalności gdzie sensowne?
- [ ] **Linkuję źródła** [[YYYY-MM-DD Nazwa notatki]]?
- [ ] **Zachowuję chronologię** (najnowsze na górze w tabelach)?
- [ ] **Projekt zbiorczy:** dodałem sekcję Podprojekty w ROADMAPA.md?
- [ ] **Klient zbiorczy:** utworzyłem tylko [Nazwa].md (nie pełne 3 pliki)?

---

## Przykłady wpisów CHANGELOG → kategoryzacja

### Przykład 1: Decyzja techniczna

**CHANGELOG:**
```markdown
## 2025-10-16 | Rada architektów
**Kategoria:** #Architektura #Optymalizacja #Decyzja #Blockchain

- Wydzielenie funkcjonalności dodawania dokumentów do blockchaina do osobnego microservice w Dockerze (Azure Container Instances)
- Rozwiązanie problemu rosnącej liczby wiszących dokumentów poprzez sekwencyjne przetwarzanie zadań przez worker
```

**Analiza:**
- Słowa kluczowe: "microservice", "Docker", "Azure", "worker", "architektura"
- Typ: TECHNOLOGIA/ARCHITEKTURA
- Plik docelowy: **ARCHITEKTURA.md**

**ARCHITEKTURA.md (dodaj do tabeli decyzji):**
```markdown
| [[2025-10-16]] | Wydzielenie blockchain do microservice Docker (Azure Container Instances) z workerem sekwencyjnym | Rozwiązanie problemu wiszących dokumentów, sekwencyjne przetwarzanie | ✅ Wdrożone | [[2025-10-16 Rada]] |
```

### Przykład 2: Funkcjonalność użytkownika

**CHANGELOG:**
```markdown
## 2025-11-03 | Sprint review
**Kategoria:** #Funkcjonalność #UI

- Drag & drop sekcji w edytorze graficznym (zwijanie sekcji na czas przenoszenia, rozwijanie po upuszczeniu)
```

**Analiza:**
- Słowa kluczowe: "drag & drop", "edytorze graficznym", "użytkownik może"
- Typ: FUNKCJONALNOŚĆ/ROADMAPA
- Plik docelowy: **ROADMAPA.md**

**ROADMAPA.md (dodaj do sekcji Produkcja):**
```markdown
- ✅ Drag & drop sekcji w edytorze (zwijanie podczas przenoszenia) - [[2025-11-03 Sprint review]]
```

### Przykład 3: Decyzja o planie (nie tech!)

**CHANGELOG:**
```markdown
## 2025-10-23 | Notatka projektowa
**Kategoria:** #Funkcjonalność #Decyzja

- Decyzja: Nie dodawanie już nowych funkcji, tylko stabilizacja obecnego rozwiązania na wersję grudniową.
```

**Analiza:**
- Tag: #Decyzja
- ALE treść: "nie dodawanie funkcji", "stabilizacja", "wersję grudniową"
- Typ: ROADMAPA (decyzja o planie, nie o technologii!)
- Plik docelowy: **ROADMAPA.md**

**ROADMAPA.md (zaktualizuj MVP2):**
```markdown
## 🛠️ W TRAKCIE - MVP2 "Stabilizacja"

**Planowane wydanie:** Grudzień 2025

**Out of Scope (NIE robimy w tym MVP):**
- Nowe funkcje - focus na stabilizacji istniejącego rozwiązania - [[2025-10-23 Notatka]]
```

### Przykład 4: Cel biznesowy

**CHANGELOG:**
```markdown
## 2025-08-26 | Notatka projektowa - AMODIT UI
**Kategoria:** #Design #Architektura

**Cel:**
Przebudowa całego obszaru definiowania procesu na "ramę Reactową", rozpoczęcie od Edytora Formularza jako pierwszego elementu w tej wersji.

Zupełnie nowy projekt oparty na feedbacku klientów
```

**Analiza:**
- Słowa kluczowe: "Cel:", "feedbacku klientów", "nowy projekt"
- Typ: BIZNES/PROJEKT (mimo tagu #Design)
- Plik docelowy: **PROJEKT.md**

**PROJEKT.md (dodaj do celów):**
```markdown
### Cele biznesowe

**Modernizacja UI na podstawie feedbacku:** Przebudowa obszaru definiowania procesu na React, zaczynając od Edytora Formularza - [[2025-08-26 Notatka]]
```

---

## Edge cases

### Co jeśli wpis pasuje do 2 plików?

**Przykład:** Wpis o technologii która wpływa na funkcjonalność.

**Zasada:** Wybierz **dominujący aspekt**:
- Jeśli głównie o technologii → ARCHITEKTURA.md
- Jeśli głównie o funkcjonalności → ROADMAPA.md

**Alternatywnie:** Dodaj do obu (krótko):
- ARCHITEKTURA.md: pełny opis decyzji technicznej
- ROADMAPA.md: krótka wzmianka o wpływie na funkcjonalność

### Co jeśli CHANGELOG nie ma żadnych wpisów?

**Odpowiedź:** Utwórz 3 pliki z szablonów z `[DO UZUPEŁNIENIA]` w większości sekcji.

### Co jeśli projekt ma tylko CHANGELOG, bez starego Project Canvas?

**Odpowiedź:** Normalna inicjalizacja - utwórz 3 pliki na podstawie CHANGELOG.

---

## Zakończenie

Agent zakończył pracę gdy:
1. ✅ Przeczytał wszystkie nowe wpisy z CHANGELOG
2. ✅ Zakategoryzował każdy wpis inteligentnie (kontekst + tagi)
3. ✅ Zaktualizował odpowiednie pliki (PROJEKT/ARCHITEKTURA/ROADMAPA)
4. ✅ Zaktualizował metadane (`changelog_przeglad_do`)
5. ✅ NIE zmyślił żadnych informacji (użył `[DO UZUPEŁNIENIA]`)

**Raport końcowy:**
```
✓ Synchronizacja zakończona

Projekt: [Nazwa]
Przetworzono wpisów z CHANGELOG: X
- PROJEKT.md: zaktualizowano [sekcje]
- ARCHITEKTURA.md: dodano Y decyzji
- ROADMAPA.md: zaktualizowano Z funkcjonalności

Najnowszy przetworzony wpis: [[2025-11-28 Rada architektów]]
changelog_przeglad_do: 2025-11-28
```


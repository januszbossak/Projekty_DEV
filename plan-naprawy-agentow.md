# Plan uporządkowania agentów do przetwarzania notatek

 

**Data utworzenia:** 2025-12-05

**Status:** W realizacji

 

---

 

## 🎯 Cel główny

 

Uporządkowanie agentów do przetwarzania notatek z priorytetem na naprawę `note-reviewer` do obsługi ~60 starych notatek czekających w `Gotowe-notatki/`.

 

---

 

## 📋 Przypadki użycia (docelowe)

 

### 1. **Przetwarzanie starych gotowych notatek** (PRIORYTET)

- **Źródło:** `Gotowe-notatki/` (~60 notatek)

- **Agent:** `note-reviewer` (do naprawy)

- **Cel:** Weryfikacja jakości + mapowanie na projekty + archiwizacja

 

### 2. **Przetwarzanie nowych surowych transkrypcji** (później)

- **Źródło:** `surowe/`

- **Agenci:** `transcript-cleaner` → `note-maker` (lub nowy)

- **Cel:** Czyszczenie → generowanie notatki → mapowanie

 

### 3. **Przetwarzanie gotowych dokumentów** (później)

- **Źródło:** `surowe/notatki/` (np. artykuły z wiki)

- **Agent:** TBD (pomija czyszczenie)

- **Cel:** Bezpośrednio notatka → mapowanie

 

**UWAGA:** Punkty 2 i 3 pozostawiamy na później. Teraz skupiamy się na punkcie 1.

 

---

 

## 🔧 Zmiany w `note-reviewer` (PRIORYTET)

 

### Obecne problemy:

1. ❌ Baza SQLite - już nie używamy, tylko foldery

2. ❌ Mapowanie na projekty nieprecyzyjne (agent wymyśla projekty, zamiast używać słownika)

3. ❌ Dwa momenty mapowania (wstępne w notatce → finalne w CHANGELOG) - zbędne

4. ❌ Format pytań do użytkownika nieczytelny

5. ❌ Workflow zbyt skomplikowany

 

### Zmiany do wprowadzenia:

 

#### 1. **Usunięcie SQLite**

- ✅ Tylko przenoszenie plików między folderami

- ✅ Struktura folderów jako blokada:

  ```

  Gotowe-notatki/           ← kolejka

  Gotowe-notatki-w-trakcie/ ← blokada (agent pracuje)

  Gotowe-notatki-archiwum/  ← zakończone

  ```

 

#### 2. **Mapowanie na projekty - TYLKO ze słownika**

- ✅ Agent **ZAWSZE** używa `.claude/skills/_SLOWNIK_PROJEKTOW.md`

- ✅ Agent **NIGDY** nie czyta `/projekty/README.md` ani innych plików z listami

- ✅ Agent **NIGDY** nie wymyśla projektów - tylko te ze słownika

- ✅ Agent **IGNORUJE** projekty wpisane w starej notatce (sekcja "Powiązane projekty")

- ✅ Agent **SAMODZIELNIE** analizuje treść notatki i mapuje na projekty ze słownika

- ✅ Jeśli projekt ze słownika vs projekt w notatce się różnią → pokazuje: "Było X, Powinienem Y"

 

#### 3. **Przejrzysty format pytań**

Format numerowanej listy:

 

```markdown

## 📋 Propozycja zmian do notatki

 

Przeanalizowałem notatkę i znalazłem X kwestii do weryfikacji:

 

---
### 1. [Tytuł kwestii - np. "Status decyzji w sekcji 'Wybór Lucene'"]
**JEST:** [Co jest teraz w notatce]
**PROPOZYCJA:** [Co proponuję zmienić]
**KONTEKST:** [Uzasadnienie + fragmenty z transkrypcji dowodzące mojej sugestii]
---
### 2. [Kolejna kwestia]
...
---


**Jak odpowiedzieć?**
Wpisz numer i swoją decyzję, np:
- "1 tak, 2 nie, 3 tak ale dodaj XYZ"
- "Wszystkie tak"
```

 

**Po odpowiedzi użytkownika:**

- ✅ Uwzględnij zmiany

- ✅ Przedstaw **ponownie całą listę ze zmianami**

- ✅ W KONTEKST dodaj: "Użytkownik: [co zaproponował]"

- ✅ Poproś o potwierdzenie końcowe: "Czy zatwierdzasz te zmiany?"

 

#### 4. **Workflow docelowy (rozdzielenie odpowiedzialności)**

 

```

┌─────────────────────────────────────────────────────────┐

│ NOTE-REVIEWER                                           │

├─────────────────────────────────────────────────────────┤

│ 1. Znajdź najstarszą notatkę w Gotowe-notatki/         │

│ 2. PRZENIEŚ do Gotowe-notatki-w-trakcie/ (blokada)     │

│ 3. Wczytaj notatkę + transkrypcję źródłową             │

│ 4. Wczytaj _SLOWNIK_PROJEKTOW.md                       │

│ 5. ANALIZA:                                             │

│    - Porównaj notatkę z transkrypcją                   │

│    - Wykryj niezgodności, braki, błędy                 │

│    - Zidentyfikuj projekty ZE SŁOWNIKA (nie z notatki) │

│    - Porównaj: projekty w notatce vs słownik           │

│ 6. Przedstaw listę zmian (format numerowany)           │

│ 7. Czekaj na odpowiedź użytkownika                     │

│ 8. Uwzględnij zmiany + przedstaw ponownie              │

│ 9. Czekaj na potwierdzenie końcowe                     │

│ 10. Wprowadź zmiany do notatki                         │

│ 11. Wywołaj PROJECT-MAPPER (delegacja)                 │

└─────────────────────────────────────────────────────────┘

                         ↓

┌─────────────────────────────────────────────────────────┐

│ PROJECT-MAPPER (wywołany przez note-reviewer)           │

├─────────────────────────────────────────────────────────┤

│ 1. Otrzymaj: ścieżka do notatki + lista projektów      │

│ 2. Dla każdego projektu:                                │

│    - Otwórz Projekty/{kategoria}/{projekt}/CHANGELOG.md│

│    - Wyciągnij kluczowe ustalenia z notatki            │

│    - Zindentyfikuj Datę notatki
     
      - Dodaj wpis "NA GÓRZE" (odwrotna chronologia) ale w odpowiednim miejscy cahngelog.md aby zachowac w nim chronologie wpisow        │

│    - Automatycznie dobierz kategorie (#Architektura...)│

│ 3. PRZENIEŚ notatkę:                                    │

│    Gotowe-notatki-w-trakcie/ → Gotowe-notatki-archiwum/│

│ 4. Raport: co zmapowano                                │

└─────────────────────────────────────────────────────────┘

```

 

#### 5. **Kluczowe zasady mapowania na projekty**

 

**HIERARCHIA PROJEKTÓW (klient vs ogólny):**

- ✅ **TYLKO gdy notatka WYRAŹNIE wspomina klienta** ("dla WIM", "u LOT", "projekt PKF")

  - **PRIORYTET 1:** Projekt kliencki (pełny wpis)

  - **DODATKOWO:** Projekt ogólny (krótszy wpis z linkiem do klienckiego)

- ✅ **Jeśli BRAK wzmianki o kliencie:** TYLKO ogólny projekt

- ✅ **NIE zgaduj** że coś jest dla klienta

 

**KATEGORIE (tagi Obsidian):**

Automatyczne dobieranie na podstawie treści:

- `#Funkcjonalność` - nowe features

- `#Architektura` - techniczne, struktura bazy, komunikacja (SignalR), biblioteki

- `#Design` - UI/UX, wizualne

- `#Problem` - blokada (nie bug)

- `#Bug` - naprawa błędów

- `#Decyzja` - zatwierdzone ustalenia

- `#Zadanie` - task

- `#Wydanie` - deployment, release

- `#Dokumentacja` - tworzenie/aktualizacja docs

 

**CHRONOLOGIA:**

- ✅ **ZAWSZE** dodawaj wpis WE WŁAŚCIWYM MIEJSCY W  w CHANGELOG.md (WG DAT NOTATEK U GORY NAJNOWSZE )

- ✅ Odwrotna chronologia: 2025-12-03 → 2025-09-09 → 2025-08-26


 

---

 

## 📝 Kroki realizacji

 

### ✅ KROK 1: Zapisanie planu

- [x] Stworzenie `plan-zmiany-agentow.md`

- [x] Omówienie z użytkownikiem

 

### ⏳ KROK 2: Aktualizacja `note-reviewer`

- [ ] Usunięcie referencji do SQLite

- [ ] Dodanie wczytywania `_SLOWNIK_PROJEKTOW.md`

- [ ] Implementacja ignorowania projektów z notatki

- [ ] Implementacja samodzielnej analizy projektów ze słownika

- [ ] Implementacja nowego formatu pytań (lista numerowana)

- [ ] Implementacja powtórnego przedstawiania listy po zmianach użytkownika

- [ ] Dodanie delegacji do `project-mapper` na końcu

- [ ] Testowanie na jednej notatce

 

### ⏳ KROK 3: Weryfikacja `project-mapper`

- [ ] Sprawdzenie czy `project-mapper` istnieje i działa

- [ ] Jeśli nie - stworzenie od zera

- [ ] Testowanie integracji `note-reviewer` → `project-mapper`

 

### ⏳ KROK 4: Przetworzenie ~60 notatek

- [ ] Uruchomianie przez użytkownika  `note-reviewer` dla kolejnych notatek

- [ ] Weryfikacja jakości mapowania

- [ ] Archiwizacja przetworzonych

 

### ⏸️ KROK 5: Inne agenci (NA PÓŹNIEJ)

- [ ] Analiza `note-maker` (przetwarzanie nowych transkrypcji)

- [ ] Analiza `transcript-cleaner` (czyszczenie)

- [ ] Decyzja co z `pipeline-runner` i `batch-note-maker`

- [ ] Obsługa gotowych dokumentów z `surowe/notatki/`

 

---

 

## 🎯 Metryki sukcesu

 

### Dla KROKU 2-4 (priorytet):

- ✅ `note-reviewer` działa bez SQLite

- ✅ `note-reviewer` używa TYLKO `_SLOWNIK_PROJEKTOW.md`

- ✅ Format pytań czytelny i numerowany

- ✅ Użytkownik może edytować propozycje i widzieć je ponownie

- ✅ ~60 notatek poprawnie przetworzonych i zmapowanych

- ✅ Wszystkie notatki w `Gotowe-notatki-archiwum/`

- ✅ Wszystkie CHANGELOG.md zaktualizowane zgodnie z zasadami

 

---

 

## 📚 Zasoby

 

### Pliki do edycji:

- `.claude/agents/note-reviewer.md`

- `.claude/agents/project-mapper.md` (może wymagać stworzenia/aktualizacji)

 

### Pliki referencyjne (do wczytywania):

- `.claude/skills/_SLOWNIK_PROJEKTOW.md` (źródło projektów)

- `Notatki/Transkrypcje/Słownik Domenowy/` (korekta terminów)

- `projekty/ZASADY.md` (struktura Project Canvas)

- `projekty/STYL.md` (styl pisania)

 

### Foldery:

- `Notatki/Gotowe-notatki/` - kolejka (~60 notatek)

- `Notatki/Gotowe-notatki-w-trakcie/` - agent pracuje (blokada)

- `Notatki/Gotowe-notatki-archiwum/` - zakończone

- `Notatki/Transkrypcje/oczyszczone-archiwum/` - transkrypcje źródłowe

- `projekty/` - docelowe CHANGELOG.md

 

---

 

## ❓ Pytania otwarte

 

1. ~~Czy `project-mapper` już istnieje i działa?~~ → Sprawdzimy w KROKU 3

2. ~~Czy format pytań jest OK?~~ ✅ Zatwierdzony przez użytkownika

3. ~~Czy workflow `note-reviewer` → `project-mapper` jest OK?~~ ✅ Zatwierdzony (opcja B)

 

---

 

## 📅 Historia zmian

 

- **2025-12-05:** Plan utworzony, omówiony z użytkownikiem, zatwierdzony

 
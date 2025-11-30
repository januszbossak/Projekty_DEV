# Przewodnik: Praca z bazą wiedzy R&D AMODIT

Przewodnik po przypadkach użycia - jak pracować z bazą wiedzy, jakie agenty wywoływać i jakie workflow stosować.

---

## Przypadki użycia

### UC-001: Dodawanie nowej transkrypcji spotkania

**Scenariusz:** Użytkownik dodaje surową transkrypcję ze spotkania w postaci pliku `.md`, zawierającą znaczniki czasu i nieoczyszczoną.

**Lokalizacja:** `Notatki/Transkrypcje/surowe/`

**Format pliku:** `YYYY-MM-DD [Typ spotkania].md` (np. `2025-11-28 Rada architektów.md`)

**Opcje przetwarzania:**

**a) Oczyszczenie pojedynczej transkrypcji:**
```
Wywołaj: "Oczyść [nazwa pliku]"
Agent: transcript-cleaner
Rezultat: Plik w `oczyszczone/` gotowy do generowania notatki
```

**b) Pipeline dzienny (zalecane):**
```
Wywołaj: "Przetwórz dzisiejsze" lub "Przetwórz nowe"
Agent: pipeline-runner
Rezultat: Automatyczne czyszczenie + generowanie notatki w jednej sesji
```

**c) Pipeline dla konkretnej daty:**
```
Wywołaj: "Przetwórz z 2025-11-28"
Agent: pipeline-runner
Rezultat: Wszystkie transkrypcje z danej daty przetworzone
```

---

### UC-002: Dodawanie gotowego dokumentu/opracowania

**Scenariusz:** Użytkownik dodaje gotowy dokument (np. artykuł z wiki technicznego, opracowanie, dokumentację), który **NIE wymaga czyszczenia**.

**Lokalizacja:** `Notatki/Transkrypcje/surowe/notatki/`

**Format pliku:** 
- `YYYY-MM-DD [Tytuł] - dokument.md` lub
- `YYYY-MM-DD [Tytuł] - notatka.md` lub
- `YYYY-MM-DD [Tytuł] - opracowanie.md`

**Przykłady:**
- `2025-11-28 Opis e-doręczeń - dokument.md` (artykuł z wiki DevOps)
- `2025-11-28 Standardy code review - opracowanie.md`
- `2025-11-28 Proces onboarding - dokument.md`

**Wyciąganie daty:**
1. Z nazwy pliku: `YYYY-MM-DD` na początku
2. Z zawartości: szukaj wzorca `YYYY-MM-DD` lub `RRRR-MM-DD`
3. Z metadanych: `**Data:** YYYY-MM-DD`
4. **Jeśli brak → użyj dzisiejszej daty**

**Przetwarzanie:**
```
Wywołaj: "Przetwórz nowe" lub "Przetwórz dzisiejsze"
Agent: pipeline-runner
Rezultat: Pomija czyszczenie, od razu generuje notatkę strukturalną
```

**Uwaga:** Pipeline automatycznie rozpozna że to gotowa notatka (folder `notatki/` lub oznaczenie w nazwie) i pominie etap czyszczenia.

---

### UC-003: Dodawanie swobodnej wypowiedzi/monologu

**Scenariusz:** Użytkownik dodaje swoją swobodną wypowiedź, wyjaśnienie, doprecyzowanie w formie monologu.

**Lokalizacja:** `Notatki/Transkrypcje/surowe/` (NIE w folderze `notatki/`)

**Format pliku:** `YYYY-MM-DD [Temat] - wypowiedź.md` lub po prostu `YYYY-MM-DD [Temat].md`

**Przykłady:**
- `2025-11-28 Wyjaśnienie Daily.md`
- `2025-11-28 Doprecyzowanie procesu.md`
- `2025-11-28 Uwagi do backlogu.md`

**Przetwarzanie:**
```
Wywołaj: "Przetwórz nowe" lub "Oczyść [nazwa pliku]"
Agent: pipeline-runner lub transcript-cleaner
Rezultat: Podlega czyszczeniu (jak transkrypcja), potem generowanie notatki
```

**Uwaga:** Swobodne wypowiedzi traktujemy jak transkrypcje - podlegają czyszczeniu, bo mogą zawierać błędy, niejasności, wymagają formatowania.

---

### UC-004: Przetwarzanie oczyszczonych transkrypcji na notatki

**Scenariusz:** Masz już oczyszczone transkrypcje w `oczyszczone/` i chcesz wygenerować z nich notatki strukturalne.

**Opcje:**

**a) Pojedyncza notatka:**
```
Wywołaj: "Wygeneruj kolejną notatkę"
Agent: note-maker
Rezultat: Jedna notatka strukturalna, czeka na potwierdzenie przed następną
```

**b) Batch 4 notatek:**
```
Wywołaj: "Wygeneruj notatki z pozostałych transkrypcji"
Agent: batch-note-maker
Rezultat: 4 notatki sekwencyjnie, automatyczna kontynuacja
```

**c) Pipeline (czyszczenie + notatka):**
```
Wywołaj: "Przetwórz nowe"
Agent: pipeline-runner
Rezultat: Pełny pipeline dla wszystkich nowych plików
```

---

### UC-005: Mapowanie notatek na projekty

**Scenariusz:** Masz gotowe notatki strukturalne i chcesz zaktualizować dokumentację projektów.

**Lokalizacja notatek:** `Notatki/[Typ]/` (np. `Notatki/Rada architektów/`)

**Przetwarzanie:**
```
Wywołaj: "Przetwórz następną notatkę"
Agent: project-mapper
Rezultat: 
1. Analiza notatki i identyfikacja projektów
2. Propozycja planu zmian (do zatwierdzenia)
3. Aktualizacja Project Canvas zgodnie z planem
4. Aktualizacja rejestru przetworzonych
```

**Workflow:**
1. Agent identyfikuje najstarszą nieprzetworzoną notatkę z `_rejestr_przetworzonych.md`
2. Analizuje tematy i mapuje na projekty/podprojekty
3. Przedstawia plan zmian do zatwierdzenia
4. Po zatwierdzeniu aktualizuje Project Canvas
5. Oznacza notatkę jako przetworzoną

**Dokumentacja:** `Notatki/PROMPT.md`

---

### UC-006: Wyłapywanie tematów organizacyjnych z notatek

**Scenariusz:** W notatce ze spotkania pojawiły się tematy organizacyjne (np. zmiana procesu Daily, nowe narzędzie, ustalenia o code review).

**Workflow:**

**1. Podczas mapowania notatki na projekty:**
```
Agent: project-mapper
Akcja: Rozpoznaje tematy organizacyjne i wyodrębnia je
Rezultat: Utworzenie/aktualizacja pliku w `Notatki/Organizacja działu DEV/[Kategoria]/`
```

**2. Ręczne wyodrębnienie:**
```
Wywołaj: "Wyodrębnij tematy organizacyjne z [nazwa notatki]"
Agent: project-mapper (tryb organizacyjny)
Rezultat: Utworzenie notatki organizacyjnej z linkiem do źródła
```

**Struktura tematów organizacyjnych:**
- `Procesy/` - jak pracujemy (Daily, code review, planowanie)
- `Narzędzia/` - czego używamy (Azure DevOps, Git, środowiska)
- `Zespół/` - struktura, komunikacja, spotkania
- `Standardy/` - konwencje, nazewnictwo, dokumentacja
- `HR/` - urlopy, onboarding, szkolenia

**Format:** Każdy temat ma własny plik (np. `Procesy/Daily.md`) z historią zmian.

**Dokumentacja:** `Notatki/Organizacja działu DEV/STRUKTURA.md`

---

### UC-007: Synchronizacja rejestru notatek

**Scenariusz:** Chcesz upewnić się, że wszystkie pliki w katalogach notatek są uwzględnione w rejestrze.

**Wywołanie:**
```
Wywołaj: "Synchronizuj rejestr notatek" lub "Sync notes"
Agent: project-mapper (tryb sync-notes)
Rezultat: 
1. Skanuje katalogi: Planowanie sprintu/, Rada architektów/, Spotkania projektowe/, Sprint review/, Daily/
2. Porównuje z rejestrem _rejestr_przetworzonych.md
3. Dodaje brakujące notatki do kolejki "Notatki oczekujące"
4. Raportuje ile notatek dodano
```

**Uwaga:** To zadanie **nie czyta treści notatek**, jedynie listuje pliki i porównuje z rejestrem.

---

### UC-008: Reprocesing od zera

**Scenariusz:** Zmieniono szablon Project Canvas lub chcesz "czystą" historię projektów.

**Wywołanie:**
```
Wywołaj: "Reprocesing od zera" lub "Reset dokumentacji projektów"
Agent: project-mapper (tryb reprocess-all)
Rezultat:
1. Reset rejestru (wszystkie notatki → nieprzetworzone)
2. Przetwarzanie chronologicznie od najstarszej
3. Budowanie historii projektów od początku
```

**Uwaga:** Przy reprocesingu treść sekcji 1-4 Project Canvas jest nadpisywana. Historia (sekcja 5) rośnie chronologicznie.

---

## Szybka referencja: Agenty i ich zastosowanie

| Agent | Kiedy użyć | Co robi |
|-------|------------|--------|
| `pipeline-runner` | Codzienna praca, przetwarzanie nowych plików | Pełny pipeline: surowe → oczyszczone → notatka |
| `transcript-cleaner` | Tylko czyszczenie pojedynczej transkrypcji | Korekta ASR, redukcja szumu, formatowanie |
| `note-maker` | Generowanie jednej notatki z oczyszczonej transkrypcji | Strukturalna notatka, czeka na potwierdzenie |
| `batch-note-maker` | Generowanie wielu notatek naraz | 4 notatki sekwencyjnie, automatyczna kontynuacja |
| `project-mapper` | Aktualizacja dokumentacji projektów | Mapowanie notatek na Project Canvas |

---

## Typy plików i ich lokalizacja

| Typ | Lokalizacja | Wymaga czyszczenia? | Przykład |
|-----|-------------|---------------------|----------|
| Transkrypcja spotkania | `surowe/` | ✅ Tak | `2025-11-28 Rada architektów.md` |
| Swobodna wypowiedź | `surowe/` | ✅ Tak | `2025-11-28 Wyjaśnienie Daily.md` |
| Gotowy dokument | `surowe/notatki/` | ❌ Nie | `2025-11-28 Opis e-doręczeń - dokument.md` |
| Oczyszczona transkrypcja | `oczyszczone/` | - | `2025-11-28 Rada architektów - transkrypcja.md` |
| Notatka strukturalna | `Notatki/[Typ]/` | - | `Notatki/Rada architektów/2025-11-28 Rada architektów.md` |

---

## Workflow: Od surowego pliku do projektu

```
1. Dodaj plik do surowe/ lub surowe/notatki/
   ↓
2. Wywołaj: "Przetwórz nowe" (pipeline-runner)
   ↓
3. [Jeśli transkrypcja] Czyszczenie → oczyszczone/
   [Jeśli gotowa notatka] Pomija czyszczenie
   ↓
4. Generowanie notatki strukturalnej → Notatki/[Typ]/
   ↓
5. Wywołaj: "Przetwórz następną notatkę" (project-mapper)
   ↓
6. Analiza i propozycja planu zmian
   ↓
7. Zatwierdzenie → Aktualizacja Project Canvas
   ↓
8. Notatka oznaczona jako przetworzona
```

---

## Linkowanie Obsidian

**WAŻNE:** Wszystkie dokumenty używają linkowania Obsidian (`[[nazwa]]`) dla tworzenia grafu powiązań.

**Formaty:**
- **Projekty:** `[[Nazwa-projektu]]` (nazwa bez ścieżki)
- **Notatki:** `[[2025-11-28 Rada architektów]]` (nazwa pliku bez ścieżki)
- **Dzienniki dat:** `[[2025-11-28]]` (format YYYY-MM-DD)

**Obsidian automatycznie:**
- Utworzy plik `Dziennik/2025-11-28.md` przy pierwszym użyciu linku
- Wyświetli linki zwrotne do wszystkich miejsc gdzie użyto daty/notatki/projektu
- Umożliwi przegląd powiązań w grafie

---

## Dokumentacja szczegółowa

- **Struktura repozytorium:** `CLAUDE.md` lub `GEMINI.md`
- **Workflow przetwarzania notatek:** `Notatki/PROMPT.md`
- **Struktura Project Canvas:** `Projekty/ZASADY.md`
- **Styl pisania:** `Projekty/STYL.md`
- **Agenty i Skills:** `.claude/agents/README.md`
- **Struktura organizacyjna:** `Notatki/Organizacja działu DEV/STRUKTURA.md`

---

## Najczęstsze scenariusze

### Scenariusz 1: Codzienna praca
```
1. Dodaj transkrypcje do surowe/
2. Wywołaj: "Przetwórz dzisiejsze"
3. Sprawdź wygenerowane notatki
4. Wywołaj: "Przetwórz następną notatkę" (kilka razy)
```

### Scenariusz 2: Dodanie gotowego dokumentu
```
1. Dodaj dokument do surowe/notatki/
2. Wywołaj: "Przetwórz nowe"
3. Notatka wygenerowana bez czyszczenia
4. Wywołaj: "Przetwórz następną notatkę"
```

### Scenariusz 3: Wyłapanie tematu organizacyjnego
```
1. Podczas mapowania notatki project-mapper rozpoznaje temat organizacyjny
2. Automatycznie tworzy/aktualizuje plik w Organizacja działu DEV/[Kategoria]/
3. Dodaje link zwrotny do źródłowej notatki
```

---

## Uwagi

- **Chronologia:** Notatki przetwarzane są chronologicznie (najstarsze najpierw)
- **Zatwierdzenie:** Zawsze przedstawiam plan zmian przed aktualizacją projektów
- **Linkowanie:** Wszystkie linki przez Obsidian `[[nazwa]]`, nie przez ścieżki
- **Dzienniki:** Daty jako linki `[[YYYY-MM-DD]]` - Obsidian tworzy dzienniki automatycznie


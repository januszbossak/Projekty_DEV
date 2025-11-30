# Agenty Claude dla Projekty DEV

Ten katalog zawiera definicje agentów Claude do automatyzacji przepływu pracy w projekcie.

---

## Dostępne agenty

### 1. `transcript-cleaner` 🧹
**Kolor:** Niebieski
**Model:** Sonnet

**Cel:** Batchowe przetwarzanie surowych transkrypcji ze spotkań R&D AMODIT.

**Aktywacja:**
- "Oczyść transkrypcje"
- "Przetwórz transkrypcję"
- "Oczyść oczekujące"
- References to files in `Notatki/Transkrypcje/surowe/`

**Workflow:**
```
surowe/ → [korekta fonetyczna, redukcja szumu] → oczyszczone/
```

**Funkcje:**
- Korekta błędów ASR (Automatic Speech Recognition)
- Redukcja szumu transkrypcji
- Formatowanie według standardu
- Aktualizacja bazy SQLite (statusy przetwarzania)
- Tryb batch (max 5 plików) lub pojedynczy plik

**Zasoby:**
- Skill: `.claude/skills/transcript-cleaning/SKILL.md`
- Słownik: `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite)
- Helper: `.claude/scripts/transkrypcje_db.py`

---

### 2. `note-maker` 📝
**Kolor:** Zielony
**Model:** Sonnet

**Cel:** Generowanie strukturalnych notatek ze spotkań na podstawie oczyszczonych transkrypcji (pojedyncza notatka).

**Aktywacja:**
- "Wygeneruj kolejną notatkę"
- "Wygeneruj notatkę"
- "Zrób notatkę"
- "Przetwórz następną transkrypcję na notatkę"

**Workflow:**
```
oczyszczone/ → [wyspecjalizowane skills] → Notatki/{typ spotkania}/
```

**Funkcje:**
- Automatyczne rozpoznanie typu spotkania
- Wybór odpowiedniego skilla (5 typów spotkań)
- **Automatyczne wykrywanie i wczytywanie części transkrypcji** (jeśli rozbite na część 1, 2, ... N)
- Generowanie strukturalnych notatek z pełną szczegółowością
- Identyfikacja powiązanych projektów
- Zachowanie niuansów i alternatyw decyzyjnych
- Aktualizacja bazy SQLite (statusy przetwarzania, archiwizacja)
- Przetwarzanie chronologiczne (najstarsze najpierw)
- **Tryb pojedynczy** - jedna notatka na sesję, czeka na potwierdzenie przed następną
- **Blokada współbieżna** - SQLite zapobiega duplikatom przy wielu agentach

**Typy spotkań i skills:**
- Rada architektów → `rada-architektow`
- Sprint review → `sprint-review`
- Planowanie sprintu → `planowanie-sprintu`
- Spotkania projektowe → `spotkanie-projektowe`
- Tematy organizacyjne → `organizacyjne`

**Zasoby:**
- Skills: `.claude/skills/note-types/*/SKILL.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite)
- Helper: `.claude/scripts/transkrypcje_db.py`

---

### 3. `batch-note-maker` 📝📝📝📝
**Kolor:** Fioletowy
**Model:** Sonnet

**Cel:** Batch processing - generowanie 4 strukturalnych notatek sekwencyjnie w jednej sesji.

**Aktywacja:**
- "Wygeneruj notatki z pozostałych transkrypcji"
- "Przetwórz 4 kolejne transkrypcje na notatki"
- "Batch generowanie notatek"

**Workflow:**
```
oczyszczone/ → [wyspecjalizowane skills] → Notatki/{typ spotkania}/
(4 transkrypcje sekwencyjnie w jednej sesji)
```

**Funkcje:**
- Automatyczne rozpoznanie typu spotkania (dla każdej z 4 transkrypcji)
- Wybór odpowiedniego skilla (5 typów spotkań)
- **Automatyczne wykrywanie i wczytywanie części transkrypcji** (jeśli rozbite na część 1, 2, ... N)
- Generowanie strukturalnych notatek z pełną szczegółowością
- Identyfikacja powiązanych projektów
- Zachowanie niuansów i alternatyw decyzyjnych
- Aktualizacja bazy SQLite (statusy przetwarzania, archiwizacja)
- Przetwarzanie chronologiczne (najstarsze najpierw)
- **Tryb batch** - 4 notatki sekwencyjnie, automatyczna kontynuacja bez czekania na potwierdzenie
- **Blokada współbieżna** - SQLite zapobiega duplikatom przy wielu agentach
- Raportowanie postępu po każdej notatce
- Podsumowanie batcha po zakończeniu

**Typy spotkań i skills:**
- Rada architektów → `rada-architektow`
- Sprint review → `sprint-review`
- Planowanie sprintu → `planowanie-sprintu`
- Spotkania projektowe → `spotkanie-projektowe`
- Tematy organizacyjne → `organizacyjne`

**Zasoby:**
- Skills: `.claude/skills/note-types/*/SKILL.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite)
- Helper: `.claude/scripts/transkrypcje_db.py`

**Różnica vs `note-maker`:**
- `note-maker`: 1 notatka na sesję, czeka na potwierdzenie
- `batch-note-maker`: 4 notatki sekwencyjnie, automatyczna kontynuacja

---

### 4. `pipeline-runner` 🚀
**Kolor:** Fioletowy
**Model:** Sonnet

**Cel:** Automatyczny pipeline end-to-end: surowe transkrypcje → oczyszczone → notatki strukturalne.

**Aktywacja:**
- "Przetwórz nowe", "Przetwórz nowe transkrypcje"
- "Przetwórz dzisiejsze", "Przetwórz z dzisiaj"
- "Przetwórz z [data]", "Przetwórz wczorajsze"

**Workflow:**
```
surowe/ → [czyszczenie + generowanie notatki] → Notatki/{typ}/
(pełny pipeline dla każdej transkrypcji)
```

**Funkcje:**
- Wykrywanie nowych surowych transkrypcji
- Filtrowanie po dacie (dzisiejsze, wczorajsze, konkretna data)
- Automatyczne czyszczenie (skill transcript-cleaning)
- Automatyczne generowanie notatek (skills note-types)
- Aktualizacja wszystkich rejestrów
- Raportowanie postępu i wyników
- **NIE** wykonuje mapowania na projekty (to osobny krok)

**Dokumentacja:** `.claude/agents/pipeline-runner.md`

---

### 5. `project-mapper` 🗺️
**Kolor:** Pomarańczowy
**Model:** Sonnet

**Cel:** Mapowanie notatek ze spotkań na dokumentację projektów (Project Canvas).

**Aktywacja:**
- "Przetwórz następną notatkę"
- "Synchronizuj rejestr notatek", "Sync notes"
- "Reprocesing od zera", "Reset dokumentacji projektów"

**Workflow:**
```
Notatki/{typ}/ → [analiza + mapowanie] → Projekty/*/{Projekt}.md
```

**Funkcje:**
- Automatyczna identyfikacja projektów/podprojektów z notatki
- Propozycja planu zmian do zatwierdzenia
- Aktualizacja Project Canvas (wszystkie sekcje)
- **Obsługa podprojektów** (np. Edytor-procesow → Edytor-formularzy)
- **Dokumentowanie odrzuconych koncepcji** (ADR ze statusem ❌ + "Powód odrzucenia")
- Synchronizacja rejestru notatek
- Workflow reprocesingu od zera

**Tryby pracy:**
- `process-note` - przetwarza jedną najstarszą nieprzetworzoną notatkę (z bazy SQLite)
- `sync-notes` - synchronizuje bazę z plikami notatek (dodaje brakujące do bazy)
- `reprocess-all` - usuwa mapowania z bazy i przetwarza chronologicznie od zera

**Zasoby:**
- Szablony: `Projekty/SZABLON.md`, `Projekty/SZABLON-PODPROJEKT.md`
- Zasady: `Projekty/ZASADY.md`, `Projekty/STYL.md`
- Workflow: `Notatki/PROMPT.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite - mapowania notatek na projekty)
- Helper: `.claude/scripts/transkrypcje_db.py`

---

## Przepływ pracy (pipeline)

### Wariant A: Automatyczny pipeline (zalecany dla codziennej pracy)

```
┌─────────────────────────────────────────────────────────────────┐
│ PIPELINE-RUNNER (Etapy 1+2 automatycznie)                      │
│ Trigger: "Przetwórz nowe" / "Przetwórz dzisiejsze"             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ surowe/                                                         │
│   └─ 2025-11-28 Rada developerów.md                            │
│        ↓ [czyszczenie: korekta + redukcja szumu]               │
│ oczyszczone/                                                    │
│   └─ 2025-11-28 Rada architektów - transkrypcja.md             │
│        ↓ [generowanie: rozpoznanie typu + skill]               │
│ Notatki/Rada architektów/                                       │
│   └─ 2025-11-28 Rada architektów.md                            │
│                                                                 │
│ (powtórz dla każdej transkrypcji)                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ PROJECT-MAPPER (Etap 3 - osobno, z kontrolą)                   │
│ Trigger: "Przetwórz następną notatkę"                          │
├─────────────────────────────────────────────────────────────────┤
│ Notatki/Rada architektów/                                       │
│   └─ 2025-11-28 Rada architektów.md                            │
│        ↓ [analiza tematów + plan zmian + zatwierdzenie]        │
│ Projekty/moduly/Trust-Center/                                   │
│   └─ Trust-Center.md (Project Canvas)                          │
└─────────────────────────────────────────────────────────────────┘
```

### Wariant B: Manualne agenty (dla kontroli krok po kroku)

```
┌─────────────────────────────────────────────────────────────┐
│ Etap 1: Czyszczenie transkrypcji                           │
│ Agent: transcript-cleaner                                   │
├─────────────────────────────────────────────────────────────┤
│ surowe/ → [korekta fonetyczna + redukcja szumu] → oczyszczone/ │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Etap 2: Generowanie notatek strukturalnych                 │
│ Agent: note-maker / batch-note-maker                       │
├─────────────────────────────────────────────────────────────┤
│ oczyszczone/ → [rozpoznanie typu + skill] → Notatki/{typ}/ │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Etap 3: Mapowanie na projekty                              │
│ Agent: project-mapper                                       │
├─────────────────────────────────────────────────────────────┤
│ Notatki/{typ}/ → [analiza + plan + zatwierdzenie] → Projekty/ │
└─────────────────────────────────────────────────────────────┘
```

---

## Jak używać

### Automatyczny pipeline (zalecany)

**Codzienne użycie:**
```
User: Przetwórz nowe
```
Agent przetworzy wszystkie nowe surowe transkrypcje przez cały pipeline (czyszczenie + notatka).

**Po spotkaniu:**
```
User: Przetwórz dzisiejsze
```
Agent przetworzy tylko transkrypcje z dzisiejszą datą.

**Nadrabianie:**
```
User: Przetwórz wczorajsze
User: Przetwórz z 2025-11-27
```
Agent przetworzy transkrypcje z konkretnej daty.

---

### Czyszczenie transkrypcji (Etap 1)

**Tryb batch (zalecany):**
```
User: Oczyść oczekujące transkrypcje
```
Agent przetworzy maksymalnie 5 plików i zapyta czy kontynuować.

**Tryb pojedynczy:**
```
User: Oczyść 2025-11-25 Design.md
```

### Generowanie notatek (Etap 2)

**Pojedyncza notatka (kontrolowany postęp):**
```
User: Wygeneruj kolejną notatkę
```
Agent automatycznie wybierze najstarszą nieprzetworzoną transkrypcję i wygeneruje notatkę.

**Kontynuacja:**
Po każdej notatce agent poinformuje o postępie. Aby kontynuować:
```
User: Wygeneruj kolejną notatkę
```

**Batch processing (4 notatki sekwencyjnie):**
```
User: Wygeneruj notatki z pozostałych transkrypcji
```
Agent automatycznie wybierze 4 najstarsze nieprzetworzone transkrypcje i przetworzy je sekwencyjnie w jednej sesji. Raportuje postęp po każdej notatce i podsumowuje batch po zakończeniu.

### Mapowanie na projekty (Etap 3)

**Pojedyncza notatka (z zatwierdzeniem planu):**
```
User: Przetwórz następną notatkę
```
Agent przedstawi plan zmian do zatwierdzenia, po akceptacji zaktualizuje Project Canvas.

**Synchronizacja rejestru:**
```
User: Sync notes
```
Agent zsynchronizuje rejestr notatek z plikami w katalogach.

**Reprocesing od zera:**
```
User: Reprocesing od zera
```
Agent zresetuje rejestr i przetworzy wszystkie notatki chronologicznie od najstarszej.

---

## Baza danych SQLite i śledzenie postępu

### `Notatki/rejestr_transkrypcji.db`

Centralna baza SQLite śledzi statusy przetwarzania:

**Tabele:**
- `pliki` - wszystkie pliki (surowe, oczyszczone, notatki)
- `przetwarzanie` - statusy transformacji (surowa→oczyszczona, oczyszczona→notatka)
- `mapowania_projektow` - powiązania notatek z projektami

**Funkcje** (`.claude/scripts/transkrypcje_db.py`):
- `get_unprocessed_files(etap)` - pobiera pliki do przetworzenia
- `start_processing(plik_id, etap)` - oznacza jako 'w_trakcie' (blokada)
- `finish_processing(processing_id, plik_wynikowy_id)` - oznacza jako 'zakonczone'
- `mark_as_archived(plik_id)` - archiwizacja pliku
- `add_project_mapping(notatka_id, projekt_sciezka)` - mapowanie na projekt
- `get_stats()` - statystyki

**Zalety:**
- Automatyczna blokada współbieżna (wiele agentów jednocześnie)
- Sortowanie chronologiczne (po nazwie pliku, nie dacie dodania)
- Pełna historia transformacji (surowa → oczyszczona → notatka → projekt)
- Szybkie zapytania SQL

---

## Standardy jakości

### Transcript Cleaner
- Wierność oryginałowi (brak halucynacji)
- Korekta tylko potwierdzonymi mapowaniami ze słownika
- Redukcja szumu bez utraty kontekstu

### Note Maker
- 100% zgodność struktury ze skillem
- **Automatyczne wczytywanie wszystkich części transkrypcji** (jeśli rozbite)
- Zachowanie niuansów i szczegółów technicznych
- Dokumentowanie odrzuconych alternatyw
- Brak halucynacji (użycie `[DO USTALENIA]` jeśli brak info)
- Pełna identyfikacja powiązanych projektów

---

## Rozwój

Planowane przyszłe agenty:
- `changelog-generator` - generowanie changelogów z notatek
- `meeting-summarizer` - quick summaries dla management

---

## Struktura katalogów

```
.claude/
├── agents/
│   ├── README.md                    ← ten plik
│   ├── transcript-cleaner.md
│   ├── note-maker.md
│   ├── batch-note-maker.md
│   └── project-mapper.md            ← NOWY
├── skills/
│   ├── transcript-cleaning/
│   │   └── SKILL.md
│   └── note-types/
│       ├── rada-architektow/
│       ├── sprint-review/
│       ├── planowanie-sprintu/
│       ├── spotkanie-projektowe/
│       └── organizacyjne/
└── settings.local.json
```

---

## Troubleshooting

### Transcript Cleaner nie znajduje plików
→ Sprawdź czy pliki są w `Notatki/Transkrypcje/surowe/`

### Note Maker nie generuje notatki
→ Sprawdź czy transkrypcja jest w `oczyszczone/` i czy ma wpis w bazie SQLite:
```python
python3 .claude/scripts/transkrypcje_db.py  # Pokaż statystyki
```

### Nieprawidłowy typ spotkania
→ Sprawdź nazwę pliku transkrypcji w bazie (kolumna `nazwa` w tabeli `pliki`) lub w systemie plików

### Brak identyfikacji projektów w notatce
→ Skill może wymagać aktualizacji lub transkrypcja nie zawiera wystarczających informacji

### Notatka niepełna - brakuje części transkrypcji
→ Sprawdź czy wszystkie części transkrypcji zostały wczytane (część 1, 2, ... N). Agent powinien automatycznie wykrywać i wczytywać wszystkie części.

### Project Mapper nie rozpoznaje podprojektu
→ Sprawdź mapowanie w `project-mapper.md` i czy projekt nadrzędny ma sekcję "7. PODPROJEKTY"

### Project Mapper nie dokumentuje odrzuconych koncepcji
→ Upewnij się że w notatce jest wyraźnie zaznaczone że koncepcja została odrzucona i dlaczego

---

**Dokumentacja:** Wersja 1.1 - 2025-11-28

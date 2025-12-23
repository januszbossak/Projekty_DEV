# Agenty Claude dla Projekty DEV

Ten katalog zawiera definicje agentów Claude do automatyzacji przepływu pracy w projekcie.

---

## Dostępne agenty

### 1. `transcript-cleaner` 🧹
**Kolor:** Niebieski
**Model:** Sonnet

**Cel:** Batchowe przetwarzanie surowych transkrypcji ze spotkań R&D AMODIT.

**Aktywacja:**
- "Oczyść transkrypcję"
- "Czyszczenie transkrypcji"
- "Oczyść [nazwa pliku]"

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
- Skill: `_ai/skills/transcript-cleaning/SKILL.md`
- Słownik: `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite)
- Helper: `_ai/scripts/transkrypcje_db.py`

---

### 2. `note-maker` 📝
**Kolor:** Zielony
**Model:** Sonnet

**Cel:** Generowanie strukturalnych notatek ze spotkań na podstawie oczyszczonych transkrypcji (pojedyncza notatka).

**Aktywacja:**
- "Wygeneruj notatkę"
- "Utwórz notatkę"
- "Zrób notatkę"

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
- Skills: `_ai/skills/note-types/*/SKILL.md`
- Baza danych: `Notatki/rejestr_transkrypcji.db` (SQLite)
- Helper: `_ai/scripts/transkrypcje_db.py`

---

### 3. `pipeline-runner` 🚀
**Kolor:** Fioletowy
**Model:** Sonnet

**Cel:** Automatyczny pipeline end-to-end: surowe transkrypcje → oczyszczone → notatki strukturalne.

**Aktywacja:**
- "Przetwórz nowe", "Przetwórz nowe transkrypcje"
- "Przetwórz dzisiejsze", "Przetwórz z dzisiaj"
- "Przetwórz z [data]", "Przetwórz wczorajsze"
- "Pipeline [nazwa pliku]"

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

**Dokumentacja:** `_ai/agents/pipeline-runner.md`

---

### 4. `project-mapper` 🗺️
**Kolor:** Pomarańczowy
**Model:** Sonnet

**Cel:** Dodawanie wpisów do CHANGELOG.md projektów na podstawie notatek ze spotkań.

**Aktywacja:**
- Automatycznie wywołany przez note-reviewer po zatwierdzeniu zmian
- Ręcznie: "Dodaj do changelog projektu X"

**Workflow:**
```
Notatki/{typ}/ → [ekstrakcja ustaleń] → Projekty/*/CHANGELOG.md
```

**Funkcje:**
- Automatyczna identyfikacja projektów/podprojektów z notatki
- Ekstrakcja kluczowych ustaleń (max 5-7 bulletów)
- **Automatyczne dobieranie kategorii** (#Funkcjonalność, #Decyzja, #Architektura, etc.)
- Dodawanie wpisów do CHANGELOG.md (chronologicznie)
- Archiwizacja notatki do `Gotowe-notatki-archiwum/`

**Zasoby:**
- Słownik projektów: `_ai/skills/_SLOWNIK_PROJEKTOW.md`
- Zasady: `Projekty/ZASADY.md`, `Projekty/STYL.md`

---

### 5. `overview-sync` 📊
**Kolor:** Zielony
**Model:** Sonnet

**Cel:** Synchronizacja dokumentacji projektów (PROJEKT.md, ARCHITEKTURA.md, ROADMAPA.md) z CHANGELOG.md

**Aktywacja:**
- "Synchronizuj overview projektu X"
- "Zaktualizuj dokumentację projektu X"
- "@overview-sync [nazwa-projektu]"

**Workflow:**
```
CHANGELOG.md → [analiza kontekstu + inteligentna kategoryzacja] → PROJEKT.md + ARCHITEKTURA.md + ROADMAPA.md
```

**Funkcje:**
- Automatyczna synchronizacja z CHANGELOG
- **Inteligentna kategoryzacja** (analiza treści, nie tylko tagów!)
  - `#Decyzja` + "OAuth2" → ARCHITEKTURA.md (tech)
  - `#Decyzja` + "MVP2 grudzień" → ROADMAPA.md (plan)
  - `#Decyzja` + "budżet 10 MD" → PROJEKT.md (biznes)
- Trackowanie ostatniego przetworzonego wpisu (YAML frontmatter: `changelog_przeglad_do`)
- Obsługa 3 poziomów projektów:
  - Klient zbiorczy (np. WIM/) → tylko krótki dashboard
  - Projekt zbiorczy (np. Edytor-procesow/) → 3 pliki + sekcja Podprojekty
  - Podprojekt / prosty → standardowe 3 pliki
- Inicjalizacja nowych projektów (3 pliki z szablonów)
- Migracja z Project Canvas (rename → -OLD-ProjectCanvas.md)
- **ZERO HALUCYNACJI** - używa `[DO UZUPEŁNIENIA]` gdy brak danych

**Zasoby:**
- Skill: `_ai/skills/overview-sync/SKILL.md`
- Szablony: `Projekty/SZABLON-PROJEKT.md`, `SZABLON-ARCHITEKTURA.md`, `SZABLON-ROADMAPA.md`, `SZABLON-KLIENT-ZBIORCZY.md`
- Zasady: `Projekty/ZASADY.md`
- Styl: `Projekty/STYL.md`

---

### 6. `note-reviewer` 🔍
**Kolor:** Fioletowy
**Model:** Sonnet

**Cel:** Audytor jakości dla starych/gotowych notatek. Weryfikuje treść, formatowanie i przypisanie projektów.

**Aktywacja:**
- "Zrób review"
- "Review notatki"
- "Zweryfikuj notatkę [nazwa]"

**Workflow:**
```
Gotowe-notatki/ → [weryfikacja + korekta] → Gotowe-notatki-w-trakcie/ → [przekazanie do project-mapper]
```

**Funkcje:**
- Przenosi plik z `Gotowe-notatki/` do `Gotowe-notatki-w-trakcie/` (blokada)
- Weryfikuje zgodność z transkrypcją źródłową (jeśli dostępna)
- Mapowanie projektów wyłącznie ze słownika `_SLOWNIK_PROJEKTOW.md`
- Ignoruje projekty wpisane w starej notatce jeśli nie ma ich w słowniku
- Przekazuje zweryfikowaną notatkę do `project-mapper`

**Zasoby:**
- Słownik projektów: `_ai/skills/_SLOWNIK_PROJEKTOW.md`
- Zasady: `Projekty/ZASADY.md`, `Projekty/STYL.md`

---

### 7. `roadmap-mapper` 🗓️
**Kolor:** Niebieski
**Model:** Sonnet

**Cel:** Specjalistyczny mapper do aktualizacji Roadmapy AMODIT na podstawie notatek z planowania.

**Aktywacja:**
- Wywoływany automatycznie przez `note-maker` dla notatek typu 'Roadmapa'

**Workflow:**
```
Notatki/Roadmapa/ → [ekstrakcja ustaleń strategicznych] → Projekty/Roadmapa-AMODIT/CHANGELOG.md
```

**Funkcje:**
- Przenoszenie ustaleń strategicznych z notatek do CHANGELOG Roadmapy
- Zachowanie kontekstu kwartałów i MVP
- Dedykowany dla notatek typu 'Roadmapa' / 'Strategia'

**Zasoby:**
- Folder: `Projekty/Roadmapa-AMODIT/`

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
│ NOTE-REVIEWER + PROJECT-MAPPER (Etap 3 - stare notatki)        │
│ Trigger: "Zrób review notatki"                                 │
├─────────────────────────────────────────────────────────────────┤
│ Gotowe-notatki/                                                 │
│   └─ 2025-11-28 Rada architektów.md                            │
│        ↓ [weryfikacja + mapowanie projektów]                   │
│ Projekty/moduly/Trust-Center/                                   │
│   └─ CHANGELOG.md (surowa historia)                            │
│        ↓                                                        │
│ Gotowe-notatki-archiwum/                                        │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ OVERVIEW-SYNC (Etap 4 - na żądanie)                            │
│ Trigger: "Synchronizuj overview projektu Trust-Center"         │
├─────────────────────────────────────────────────────────────────┤
│ Projekty/moduly/Trust-Center/                                   │
│   └─ CHANGELOG.md                                              │
│        ↓ [inteligentna kategoryzacja + synteza]                │
│   ├─ PROJEKT.md (biznes)                                       │
│   ├─ ARCHITEKTURA.md (tech)                                    │
│   └─ ROADMAPA.md (plan)                                        │
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
│ Agent: note-maker                                          │
├─────────────────────────────────────────────────────────────┤
│ oczyszczone/ → [rozpoznanie typu + skill] → Notatki/{typ}/ │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Etap 3: Mapowanie na projekty (CHANGELOG)                  │
│ Agent: project-mapper                                       │
├─────────────────────────────────────────────────────────────┤
│ Notatki/{typ}/ → [ekstrakcja + kategoryzacja] → CHANGELOG.md │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Etap 4: Synchronizacja dokumentacji (na żądanie)           │
│ Agent: overview-sync                                        │
├─────────────────────────────────────────────────────────────┤
│ CHANGELOG.md → [synteza] → PROJEKT + ARCHITEKTURA + ROADMAPA │
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

**Konkretny plik:**
```
User: Pipeline 2025-12-12 Rada architektów.md
```
Agent przetworzy wskazany plik przez cały pipeline.

---

### Czyszczenie transkrypcji (Etap 1)

**Automatyczny wybór z kolejki (zalecany):**
```
User: Oczyść transkrypcję
```
lub
```
User: Czyszczenie transkrypcji
```
Agent automatycznie wybierze najstarszy plik z kolejki.

**Konkretny plik:**
```
User: Oczyść 2025-11-25 Design.md
```

### Generowanie notatek (Etap 2)

**Automatyczny wybór z kolejki:**
```
User: Wygeneruj notatkę
```
lub
```
User: Utwórz notatkę
```
Agent automatycznie wybierze najstarszą nieprzetworzoną transkrypcję i wygeneruje notatkę.

**Kontynuacja:**
Po każdej notatce agent poinformuje o postępie. Aby kontynuować, użyj tej samej komendy ponownie.

### Przetwarzanie starych notatek (note-reviewer)

**Automatyczny wybór z kolejki:**
```
User: Zrób review
```
lub
```
User: Review notatki
```
Agent pobierze kolejną notatkę z `Gotowe-notatki/`, zweryfikuje ją i przekaże do `project-mapper`.

**Konkretna notatka:**
```
User: Zweryfikuj notatkę 2025-12-04 Spotkanie projektowe.md
```

### Ręczne mapowanie na projekty (project-mapper)

**Dodanie notatki do changelog konkretnego projektu:**
```
User: Dodaj notatkę z 2025-12-01 do changelog Repozytorium
```
Agent wyekstrahuje ustalenia z notatki i doda je do CHANGELOG.md wskazanego projektu.

**Uwaga:** Zazwyczaj `project-mapper` jest wywoływany automatycznie przez `note-reviewer` lub `note-maker`.

---

## Baza danych SQLite i śledzenie postępu

### `Notatki/rejestr_transkrypcji.db`

Centralna baza SQLite śledzi statusy przetwarzania:

**Tabele:**
- `pliki` - wszystkie pliki (surowe, oczyszczone, notatki)
- `przetwarzanie` - statusy transformacji (surowa→oczyszczona, oczyszczona→notatka)
- `mapowania_projektow` - powiązania notatek z projektami

**Funkcje** (`_ai/scripts/transkrypcje_db.py`):
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
_ai/
├── agents/
│   ├── README.md                    ← ten plik
│   ├── transcript-cleaner.md
│   ├── note-maker.md
│   ├── project-mapper.md
│   ├── note-reviewer.md
│   ├── overview-sync.md
│   ├── pipeline-runner.md
│   └── roadmap-mapper.md
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
python3 _ai/scripts/transkrypcje_db.py  # Pokaż statystyki
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

---
name: pipeline-runner
description: |
  Automatyczny pipeline: surowe transkrypcje → oczyszczone → notatki strukturalne.
  
  Activation triggers:
  1. "Przetwórz nowe", "Przetwórz nowe transkrypcje"
  2. "Przetwórz dzisiejsze", "Przetwórz z dzisiaj"
  3. "Przetwórz z [data]", "Przetwórz wczorajsze"
  4. "Pipeline" + nazwa pliku
  
  Examples:
  - "Przetwórz nowe" → wszystkie nowe surowe transkrypcje
  - "Przetwórz dzisiejsze" → tylko transkrypcje z dzisiejszą datą
  - "Przetwórz z 2025-11-27" → transkrypcje z konkretnej daty
  - "Przetwórz wczorajsze" → transkrypcje z wczoraj
model: sonnet
color: purple
---

# Pipeline Runner Agent

Agent do automatycznego przetwarzania surowych transkrypcji przez cały pipeline:

```
surowe/ → [czyszczenie] → oczyszczone/ → [generowanie] → Notatki/{typ}/
```

**Zakres:** Agent **NIE** wykonuje mapowania na projekty. To pozostaje jako osobny, kontrolowany krok (wywołaj `project-mapper`).

---

## Tryby pracy

### 1. "Przetwórz nowe" (domyślny)

Przetwarza **wszystkie** nowe surowe transkrypcje (te bez statusu `zakonczone` dla etapu `surowa->oczyszczona` w bazie).

### 2. "Przetwórz dzisiejsze" / "Przetwórz z dzisiaj"

Przetwarza tylko transkrypcje z **dzisiejszą datą** w nazwie pliku.

### 3. "Przetwórz z [data]" / "Przetwórz wczorajsze"

Przetwarza transkrypcje z **konkretnej daty**:
- "Przetwórz z 2025-11-27" → data explicite
- "Przetwórz wczorajsze" → data = dzisiaj - 1 dzień

### 4. "Pipeline [nazwa pliku]"

Przetwarza **konkretny plik** przez cały pipeline.

---

## Typy plików wejściowych

Pipeline obsługuje **dwa typy plików**:

### 1. Transkrypcje (wymagają czyszczenia)
- **Lokalizacja:** `Notatki/Transkrypcje/surowe/`
- **Format:** Surowa transkrypcja z błędami ASR, znacznikami czasu, dialogiem wielu osób
- **Przetwarzanie:** Czyszczenie → Generowanie notatki
- **Rozpoznawanie:** Format dialogu, znaczniki czasu, błędy ASR

### 2. Gotowe notatki (pomijają czyszczenie)
- **Lokalizacja:** `Notatki/Transkrypcje/surowe/notatki/` lub `Notatki/Transkrypcje/surowe/` (z oznaczeniem)
- **Format:** Gotowa notatka, dokument, opracowanie (np. artykuł z wiki)
- **Przetwarzanie:** Tylko generowanie notatki (pomija czyszczenie)
- **Rozpoznawanie:** 
  - Plik w folderze `surowe/notatki/`
  - Lub nazwa zawiera `- notatka.md` / `- dokument.md` / `- opracowanie.md`
  - Lub zawartość nie ma formatu transkrypcji (brak dialogu, znaczników czasu)

**Uwaga:** Swobodne wypowiedzi/monologi traktujemy jak transkrypcje (podlegają czyszczeniu).

---

## Workflow

### Krok 1: Identyfikacja plików do przetworzenia

1. **Wylistuj pliki w `Notatki/Transkrypcje/surowe/`** (w tym `surowe/notatki/`)
2. **Pobierz nieprzetwarzane pliki z bazy SQLite:**
   ```python
   from .claude.scripts.transkrypcje_db import *
   # Dla nowych surowych transkrypcji (bez czyszczenia w bazie)
   pliki = get_unprocessed_files('surowa->oczyszczona', limit=100)
   ```
3. **Rozpoznaj typ pliku** (transkrypcja vs gotowa notatka)
4. **Filtruj według trybu:**

   | Tryb | Filtr |
   |------|-------|
   | "Przetwórz nowe" | Wszystkie pliki z `get_unprocessed_files()` |
   | "Przetwórz dzisiejsze" | + filtruj po dacie w nazwie = dzisiaj |
   | "Przetwórz z [data]" | + filtruj po dacie w nazwie = podana data |
   | "Pipeline [plik]" | Tylko wskazany plik |

5. **Lista jest już posortowana chronologicznie** (najstarsze najpierw - sortowanie po nazwie w bazie)
5. **Przedstaw listę użytkownikowi:**

```markdown
## 📋 Transkrypcje do przetworzenia

Znaleziono: X plików

| # | Data | Typ spotkania | Plik |
|---|------|---------------|------|
| 1 | 2025-11-28 | Rada architektów | `2025-11-28 Rada developerów.md` |
| 2 | 2025-11-28 | Planowanie sprintu | `2025-11-28 Planowanie sprintu.md` |

**Kontynuować? (tak/nie)**
```

### Krok 2: Wczytanie zasobów (raz na sesję)

**Przed pierwszym przetwarzaniem wczytaj:**

1. **Skill czyszczenia:** `_ai/skills/transcript-cleaning/SKILL.md`
2. **Słownik domenowy:** `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`

**Cache te zasoby mentalnie** – nie wczytuj ponownie dla każdego pliku.

### Krok 3: Rozpoznawanie typu pliku

Dla każdego pliku określ typ:

**Kryteria rozpoznawania gotowej notatki:**
- Plik w folderze `surowe/notatki/`
- Nazwa zawiera: `- notatka.md`, `- dokument.md`, `- opracowanie.md`
- Zawartość nie ma formatu transkrypcji:
  - Brak dialogu (format `**[Imię]:**`)
  - Brak znaczników czasu (`[14:23]`)
  - Brak błędów ASR typowych dla transkrypcji
  - Jest już sformatowany jako dokument/notatka

**Jeśli nie spełnia kryteriów → traktuj jako transkrypcję**

### Krok 4: Pętla przetwarzania (dla każdego pliku)

```
FOR EACH plik IN lista:

    IF typ == "gotowa_notatka":
        ┌─────────────────────────────────────────────────────┐
        │ ETAP: Generowanie notatki (pomija czyszczenie)      │
        ├─────────────────────────────────────────────────────┤
        │ 1. DODAJ plik do bazy (jeśli jeszcze nie ma)        │
        │    plik_id = add_file(sciezka, 'surowa', nazwa)     │
        │ 2. Wyciągnij datę z nazwy pliku lub użyj dzisiejszej│
        │ 3. Rozpoznaj typ spotkania (z nazwy lub zawartości) │
        │ 4. OZNACZ rozpoczęcie w bazie                       │
        │    proc_id = start_processing(plik_id,              │
        │                    'surowa->notatka_bezposrednia')  │
        │ 5. Wczytaj odpowiedni skill note-types              │
        │ 6. Wczytaj gotową notatkę (bez czyszczenia)        │
        │ 7. Wygeneruj notatkę strukturalną                  │
        │ 8. Zapisz do Notatki/{typ}/                         │
        │ 9. DODAJ notatkę do bazy                            │
        │    notatka_id = add_file(sciezka, 'notatka', nazwa) │
        │ 10. ZAKOŃCZ przetwarzanie w bazie                   │
        │     finish_processing(proc_id, notatka_id)          │
        │ 11. ARCHIWIZUJ surowy plik                          │
        │     mark_as_archived(plik_id)                       │
        └─────────────────────────────────────────────────────┘

    ELSE (typ == "transkrypcja"):
        ┌─────────────────────────────────────────────────────┐
        │ ETAP A: Czyszczenie (transcript-cleaning)           │
        ├─────────────────────────────────────────────────────┤
        │ 1. DODAJ plik do bazy (jeśli jeszcze nie ma)        │
        │    plik_id = add_file(sciezka, 'surowa', nazwa)     │
        │ 2. OZNACZ rozpoczęcie czyszczenia w bazie           │
        │    proc_a_id = start_processing(plik_id,            │
        │                        'surowa->oczyszczona')       │
        │    jeśli None → pomiń (już w trakcie)               │
        │ 3. Przeczytaj surowy plik                           │
        │ 4. Sprawdź rozmiar (wc -l)                          │
        │    - > 800 linii → podziel na części               │
        │    - ≤ 800 linii → przetwórz całość               │
        │ 5. Zastosuj reguły ze skilla:                       │
        │    - Korekta fonetyczna wg słownika                 │
        │    - Redukcja szumu                                 │
        │    - Formatowanie                                   │
        │ 6. Zapisz do oczyszczone/:                          │
        │    - Format: `{data} {typ} - transkrypcja.md`       │
        │    - Lub części: `... - część 1.md`, etc.          │
        │ 7. DODAJ oczyszczoną do bazy                        │
        │    oczyszczona_id = add_file(sciezka, 'oczyszczona',│
        │                              nazwa)                 │
        │ 8. PRZENIEŚ surowy plik do surowe - archiwum/       │
        │ 9. OZNACZ archiwizację w bazie                      │
        │    mark_as_archived(plik_id)                        │
        │ 10. ZAKOŃCZ czyszczenie w bazie                     │
        │     finish_processing(proc_a_id, oczyszczona_id)    │
        └─────────────────────────────────────────────────────┘
                         ↓
        ┌─────────────────────────────────────────────────────┐
        │ ETAP B: Generowanie notatki (note-maker)            │
        ├─────────────────────────────────────────────────────┤
        │ 1. OZNACZ rozpoczęcie generowania w bazie           │
        │    proc_b_id = start_processing(oczyszczona_id,     │
        │                        'oczyszczona->notatka')      │
        │ 2. Rozpoznaj typ spotkania (z nazwy)                │
        │ 3. Wczytaj odpowiedni skill note-types              │
        │ 4. Wczytaj oczyszczoną transkrypcję                 │
        │    - Jeśli części → wczytaj wszystkie i połącz      │
        │ 5. Wygeneruj strukturalną notatkę                   │
        │ 6. Zapisz do Notatki/{typ}/                         │
        │ 7. DODAJ notatkę do bazy                            │
        │    notatka_id = add_file(sciezka, 'notatka', nazwa) │
        │ 8. PRZENIEŚ oczyszczoną do oczyszczone-archiwum/    │
        │ 9. OZNACZ archiwizację w bazie                      │
        │    mark_as_archived(oczyszczona_id)                 │
        │ 10. ZAKOŃCZ generowanie w bazie                     │
        │     finish_processing(proc_b_id, notatka_id)        │
        └─────────────────────────────────────────────────────┘
                         ↓
    ┌─────────────────────────────────────────────────────┐
    │ Raport cząstkowy                                    │
    ├─────────────────────────────────────────────────────┤
    │ ✓ [1/3] 2025-11-28 Rada architektów                │
    │   → Oczyszczone: 2025-11-28 Rada architektów - ...  │
    │   → Notatka: Notatki/Rada architektów/2025-11-28... │
    │   → Powiązane projekty: Trust-Center, Moduł-rapor.. │
    └─────────────────────────────────────────────────────┘

END FOR
```

### Krok 4: Raport końcowy

```markdown
## ✓ Pipeline zakończony

### Przetworzone transkrypcje

| # | Źródło | Oczyszczone | Notatka | Projekty |
|---|--------|-------------|---------|----------|
| 1 | 2025-11-28 Rada dev... | ✓ (3 części) | Rada architektów/... | Trust-Center, ... |
| 2 | 2025-11-28 Planowanie... | ✓ | Planowanie sprintu/... | - |

### Nowe błędy ASR (do dodania do słownika)

- "xyz" → "ABC" (kontekst: ...)

### Statystyki

- **Przetworzone:** 2 transkrypcje
- **Notatki wygenerowane:** 2
- **Notatki oczekujące na mapowanie:** 51 (w tym 2 nowe)

---

**Następny krok:** Aby zmapować notatki na projekty:
> "Zrób review" (wywołuje `note-reviewer` → `project-mapper`)
```

---

## Wyciąganie daty z pliku

**Dla transkrypcji:**
- Data z nazwy pliku: `YYYY-MM-DD` na początku
- Nazwa pliku jest dostępna w bazie (kolumna `nazwa` w tabeli `pliki`)

**Dla gotowych notatek:**
- Data z nazwy pliku: `YYYY-MM-DD` na początku
- Lub z zawartości pliku (szukaj wzorca `YYYY-MM-DD` lub `RRRR-MM-DD`)
- Lub z metadanych na początku pliku (`**Data:** YYYY-MM-DD`)
- **Jeśli brak → użyj dzisiejszej daty**

---

## Rozpoznawanie typu spotkania

Z nazwy pliku lub zawartości (nazwa pliku dostępna w bazie w kolumnie `nazwa`):

| Wzorzec w nazwie | Typ | Skill | Folder docelowy |
|------------------|-----|-------|-----------------|
| `Rada developerów`, `Rada architektów` | Rada architektów | `rada-architektow` | `Notatki/Rada architektów/` |
| `Sprint review` | Sprint review | `sprint-review` | `Notatki/Sprint review/` |
| `Planowanie sprintu` | Planowanie sprintu | `planowanie-sprintu` | `Notatki/Planowanie sprintu/` |
| `Daily` | Daily | `daily` | `Notatki/Daily/` |
| `Design`, `Spotkanie projektowe`, `Przegląd`, `Repozytorium` | Spotkanie projektowe | `spotkanie-projektowe` | `Notatki/Spotkania projektowe/` |
| Inne | Organizacyjne | `organizacyjne` | `Notatki/Organizacja działu DEV/` |

---

## Nazewnictwo plików

### Oczyszczone transkrypcje

```
{YYYY-MM-DD} {Typ spotkania} - transkrypcja.md
```

Przykłady:
- `2025-11-28 Rada architektów - transkrypcja.md`
- `2025-11-28 Planowanie sprintu - transkrypcja.md`
- `2025-11-28 Design - transkrypcja - część 1.md` (dla dużych plików)

### Notatki

```
{YYYY-MM-DD} {Typ czytelny}[ - {dodatkowe info}].md
```

Przykłady:
- `2025-11-28 Rada architektów.md`
- `2025-11-28 Planowanie sprintu.md`
- `2025-11-28 Spotkanie projektowe - Design.md`

---

## Zarządzanie statusami w bazie SQLite

Wszystkie statusy przetwarzania są śledzone w bazie `Notatki/rejestr_transkrypcji.db`:

### Funkcje bazy danych (`transkrypcje_db.py`)

```python
# Dodanie pliku do bazy (jeśli jeszcze nie ma)
plik_id = add_file(sciezka, typ, nazwa)
# typ: 'surowa', 'oczyszczona', 'notatka'

# Rozpoczęcie przetwarzania (oznacz jako 'w_trakcie')
processing_id = start_processing(plik_zrodlowy_id, etap)
# etap: 'surowa->oczyszczona', 'oczyszczona->notatka'
# Zwraca None jeśli już przetwarzane

# Zakończenie przetwarzania (oznacz jako 'zakonczone')
finish_processing(processing_id, plik_wynikowy_id, uwagi)

# Archiwizacja pliku
mark_as_archived(plik_id)

# Pobranie statystyk
stats = get_stats()
```

**Baza automatycznie:**
- Śledzi statusy: `oczekujace` → `w_trakcie` → `zakonczone`
- Zapobiega duplikatom (blokada przez status `w_trakcie`)
- Sortuje chronologicznie (po nazwie pliku, nie dacie dodania)
- Przechowuje powiązania: surowa → oczyszczona → notatka

---

## Obsługa błędów

### Plik już oczyszczony (status 'zakonczone' dla 'surowa->oczyszczona')

→ Pomiń etap A (czyszczenie), wykonaj tylko etap B (generowanie notatki)

### Plik już w trakcie przetwarzania (start_processing zwróciło None)

→ Pomiń plik (inny agent go przetwarza), przejdź do następnego

### Plik surowy nie istnieje

→ Pomiń, zgłoś w raporcie

### Nieznany typ spotkania

→ Użyj skilla `organizacyjne`, zapisz do `Organizacja działu DEV/`

### Błąd podczas przetwarzania

→ Zanotuj błąd, kontynuuj z następnym plikiem, zgłoś w raporcie końcowym

---

## Krytyczne zasady

### 1. Kolejność przetwarzania

**Zawsze chronologicznie** – najstarsze najpierw. To zapewnia spójność historii.

### 2. Wierność treści

- **Etap A (czyszczenie):** Brak halucynacji, tylko korekta i formatowanie
- **Etap B (notatka):** Zachowaj niuanse, użyj `[DO USTALENIA]` przy brakach

### 3. Pełne przetworzenie

Każda transkrypcja przechodzi przez **oba etapy** w jednej sesji. Nie zostawiaj w stanie pośrednim.

### 4. Archiwizacja

**Po oczyszczeniu transkrypcji:**
- **ZAWSZE** przenoś surowy plik do `surowe - archiwum/`
- Zachowaj oryginalną nazwę

**Po wygenerowaniu notatki:**
- **ZAWSZE** przenoś oczyszczoną transkrypcję (wszystkie części jeśli rozbita) do `oczyszczone-archiwum/`
- Zachowaj oryginalne nazwy plików

### 5. Aktualizacja bazy danych

**ZAWSZE** aktualizuj bazę SQLite po każdym etapie:
- `start_processing()` na początku etapu
- `finish_processing()` po zakończeniu etapu
- `mark_as_archived()` po przeniesieniu do archiwum
- `add_file()` dla nowo utworzonych plików

### 6. Raportowanie

Po każdej transkrypcji pokaż cząstkowy postęp. Na końcu – pełny raport.

---

## Skills używane przez agenta

| Etap | Skill | Ścieżka |
|------|-------|---------|
| Czyszczenie | transcript-cleaning | `_ai/skills/transcript-cleaning/SKILL.md` |
| Rada architektów | rada-architektow | `_ai/skills/note-types/rada-architektow/SKILL.md` |
| Sprint review | sprint-review | `_ai/skills/note-types/sprint-review/SKILL.md` |
| Planowanie sprintu | planowanie-sprintu | `_ai/skills/note-types/planowanie-sprintu/SKILL.md` |
| Daily | daily | `_ai/skills/note-types/daily/SKILL.md` |
| Spotkanie projektowe | spotkanie-projektowe | `_ai/skills/note-types/spotkanie-projektowe/SKILL.md` |
| Organizacyjne | organizacyjne | `_ai/skills/note-types/organizacyjne/SKILL.md` |

---

## Powiązane zasoby

- **Baza danych:** `Notatki/rejestr_transkrypcji.db` (SQLite)
- **Helper script:** `_ai/scripts/transkrypcje_db.py`
- **Słownik ASR:** `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`
- **Surowe:** `Notatki/Transkrypcje/surowe/`
- **Gotowe notatki:** `Notatki/Transkrypcje/surowe/notatki/`
- **Oczyszczone:** `Notatki/Transkrypcje/oczyszczone/`
- **Archiwa:** `Notatki/Transkrypcje/surowe - archiwum/` i `Notatki/Transkrypcje/oczyszczone-archiwum/`
- **Notatki:** `Notatki/{Rada architektów|Sprint review|Planowanie sprintu|Spotkania projektowe|Organizacja działu DEV}/`

---

## Przykładowa sesja

```
User: Przetwórz dzisiejsze

Agent:
🔍 Szukam transkrypcji z 2025-11-28...

## 📋 Transkrypcje do przetworzenia

Znaleziono: 2 plików

| # | Data | Typ spotkania | Plik |
|---|------|---------------|------|
| 1 | 2025-11-28 | Rada architektów | `2025-11-28 Rada developerów.md` |
| 2 | 2025-11-28 | Planowanie sprintu | `2025-11-28 Planowanie sprintu.md` |

**Kontynuować? (tak/nie)**

User: tak

Agent:
📖 Wczytuję zasoby (skill czyszczenia, słownik)...
✓ Zasoby wczytane

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1/2] 2025-11-28 Rada developerów.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧹 Etap A: Czyszczenie...
   Rozmiar: 650 linii (bez podziału)
   ✓ Oczyszczone → `2025-11-28 Rada architektów - transkrypcja.md`
   ✓ Zarchiwizowane → `surowe - archiwum/2025-11-28 Rada developerów.md`

📝 Etap B: Generowanie notatki...
   Typ: Rada architektów
   Skill: rada-architektow
   ✓ Notatka → `Notatki/Rada architektów/2025-11-28 Rada architektów.md`
   ✓ Zarchiwizowane → `oczyszczone-archiwum/2025-11-28 Rada architektów - transkrypcja.md`
   
   Powiązane projekty:
   - `moduly/Trust-Center` - tematy 1, 3
   - `moduly/Modul-raportowy` - temat 2

✓ Baza danych zaktualizowana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[2/2] 2025-11-28 Planowanie sprintu.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧹 Etap A: Czyszczenie...
   Rozmiar: 420 linii (bez podziału)
   ✓ Oczyszczone → `2025-11-28 Planowanie sprintu - transkrypcja.md`
   ✓ Zarchiwizowane → `surowe - archiwum/2025-11-28 Planowanie sprintu.md`

📝 Etap B: Generowanie notatki...
   Typ: Planowanie sprintu
   Skill: planowanie-sprintu
   ✓ Notatka → `Notatki/Planowanie sprintu/2025-11-28 Planowanie sprintu.md`
   ✓ Zarchiwizowane → `oczyszczone-archiwum/2025-11-28 Planowanie sprintu - transkrypcja.md`

✓ Baza danych zaktualizowana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✓ Pipeline zakończony

### Przetworzone transkrypcje

| # | Źródło | Oczyszczone | Notatka |
|---|--------|-------------|---------|
| 1 | Rada developerów | ✓ | Rada architektów/2025-11-28... |
| 2 | Planowanie sprintu | ✓ | Planowanie sprintu/2025-11-28... |

### Statystyki

- **Przetworzone:** 2 transkrypcje
- **Notatki wygenerowane:** 2
- **Notatki oczekujące na mapowanie:** 51 (w tym 2 nowe)

---

**Następny krok:** Aby zmapować notatki na projekty:
> "Zrób review" (wywołuje `note-reviewer` → `project-mapper`)
```


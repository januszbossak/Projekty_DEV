# AI.md - Uniwersalne Instrukcje dla Modeli AI

> [!IMPORTANT]
> Ten plik to **JEDYNY** punkt wejścia dla każdego modelu AI pracującego z tym repozytorium.
> Nie ma znaczenia czy jesteś Claude, Gemini, GPT czy innym modelem - postępuj według tych samych instrukcji.

---

## Zasada #1: Jedno źródło prawdy

**Hierarchia dokumentów:**
1. **Agent (`_ai/agents/*.md`)** - zawsze nadrzędny, szczegółowe instrukcje wykonawcze
2. Ten plik (`AI.md`) - ogólny kontekst i mapa nawigacyjna
3. `README.md` - dla ludzi, przypadki użycia

**Ignoruj:**
- `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` - to tylko przekierowania do tego pliku

---

## Ścieżka poznawcza

### Krok 1: Zrozum repozytorium
- To **repozytorium wiedzy dokumentacyjnej** R&D AMODIT
- **Język:** Polski (cała dokumentacja i metodyka)
- **Narzędzia:** Markdown, Obsidian
- **Charakter:** Projekt dokumentacyjny - brak kompilacji, testów, buildów

### Krok 2: Poznaj strukturę agentów
**Przeczytaj:** `_ai/agents/README.md`

Agenty to zdefiniowane przepływy pracy dla konkretnych zadań (czyszczenie transkrypcji, generowanie notatek, mapowanie na projekty).

### Krok 3: Zidentyfikuj intencję użytkownika
Na podstawie polecenia użytkownika określ który agent aktywować.

### Krok 4: Aktywuj odpowiedniego agenta
Wczytaj plik agenta z `_ai/agents/[nazwa-agenta].md` i postępuj według jego instrukcji.

### Krok 5: Wczytaj wymagane zasoby
Agent wskaże które skills i zasoby wczytać (słowniki, szablony, etc.).

---

## Agenty - Quick Reference

| Trigger użytkownika | Agent | Lokalizacja |
|---------------------|-------|-------------|
| "Wygeneruj notatkę", "Utwórz notatkę" | `note-maker` | `_ai/agents/note-maker.md` |
| "Oczyść transkrypcję", "Czyszczenie" | `transcript-cleaner` | `_ai/agents/transcript-cleaner.md` |
| "Przetwórz nowe", "Przetwórz dzisiejsze" | `pipeline-runner` | `_ai/agents/pipeline-runner.md` |
| "Zrób review", "Review notatki" | `note-reviewer` | `_ai/agents/note-reviewer.md` |
| Automatycznie przez `note-maker` | `project-mapper` | `_ai/agents/project-mapper.md` |
| "Synchronizuj overview projektu X" | `overview-sync` | `_ai/agents/overview-sync.md` |

**Pełna lista:** `_ai/agents/README.md`

---

## Kluczowe zasady

### 1. Wierność źródłom
- **NIE halucynuj** - jeśli czegoś nie ma w źródle, użyj `[DO USTALENIA]`
- **NIE interpretuj** - dokumentuj co zostało powiedziane, nie własne wnioski
- Zachowuj niuanse i szczegóły techniczne

### 2. Struktura folderów (NIE SQLite)
- **WAŻNE:** Używamy struktury folderów do śledzenia statusu przetwarzania
- Foldery: `surowe/`, `oczyszczone/`, `oczyszczone-w-trakcie/`, `oczyszczone-archiwum/`
- **NIE używamy bazy SQLite** dla agentów (to była nieaktualna informacja)

### 3. Język i terminologia
- **Tylko polski** w dokumentacji
- **Terminologia techniczna** po angielsku (jak w słowniku domenowym)

### 4. Linkowanie Obsidian
- Wszystkie linki przez format Obsidian: `[[nazwa-pliku]]`
- Daty jako linki: `[[YYYY-MM-DD]]`
- Projekty: `[[Nazwa-projektu]]`

---

## Struktura repozytorium

### 📝 Notatki/
Główne źródło informacji o postępach, decyzjach i ustaleniach projektowych.

**Workflow przetwarzania:** `Notatki/PROMPT.md`

**Podkatalogi:**
- `Transkrypcje/surowe/` - surowe transkrypcje ze spotkań
- `Transkrypcje/oczyszczone/` - po czyszczeniu, gotowe do generowania notatek
- `Daily/` - notatki z Daily (nie mapowane na projekty)
- `Gotowe-notatki/` - notatki projektowe i organizacyjne
- `Rada architektów/`, `Sprint review/`, etc. - notatki wg typu

### 📂 Projekty/
Dokumentacja wszystkich projektów R&D i klienckich.

**Struktura:** `Projekty/ZASADY.md`
**Styl pisania:** `Projekty/STYL.md`

**Kategorie:**
- `Moduly/` - główne moduły systemu AMODIT
- `Klienci/` - prace dedykowane dla klientów
- `Integracje/` - integracje z systemami zewnętrznymi
- `cross-cutting/` - funkcjonalności przekrojowe

### 🤖 _ai/
Definicje agentów, skills i workflows dla AI.

**Dokumentacja:** `_ai/agents/README.md`

---

## Najczęstsze scenariusze

### Codzienna praca
```
User: "Przetwórz dzisiejsze"
→ Agent: pipeline-runner
→ Rezultat: Automatyczne czyszczenie + generowanie notatek
```

### Pojedyncza notatka (kontrolowany postęp)
```
User: "Wygeneruj notatkę"
→ Agent: note-maker
→ Rezultat: Jedna notatka, czeka na potwierdzenie przed następną
```

### Przetwarzanie starych notatek
```
User: "Zrób review"
→ Agent: note-reviewer
→ Rezultat: Weryfikacja + mapowanie na projekty
```

---

## Dokumentacja szczegółowa

- **Agenty i workflow:** `_ai/agents/README.md`
- **Przypadki użycia:** `README.md`
- **Workflow notatek:** `Notatki/PROMPT.md`
- **Struktura projektów:** `Projekty/ZASADY.md`
- **Styl pisania:** `Projekty/STYL.md`

---

**Wersja:** 1.0 - 2025-12-23
**Status:** Aktywny punkt wejścia dla wszystkich modeli AI

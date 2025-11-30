# GEMINI.md

Wytyczne dla Gemini podczas pracy z tym repozytorium.

Przeczytaj dokladnie i traktuj jak swoje, wytyczne zawarte w pliku Claude.md

======
To co jest poniej ignoruj

---

## Przegląd

To **repozytorium wiedzy nie-kodowej** – centralne repozytorium dokumentacji, metodyki i zarządzania wiedzą projektową działu R&D AMODIT.

**Charakter:** Projekt dokumentacyjny - brak kompilacji, testów, buildów. Narzędzia: Markdown, Azure CLI, Obsidian.

**Język:** Polski (cała dokumentacja i metodyka)

---

## Nawigacja: Hierarchia dokumentów

Ten plik to **MAPA** - punkt wyjścia wskazujący gdzie szukać szczegółowych informacji.

### Poziomy dokumentacji:

1. **MAPA** (`GEMINI.md` - ten plik) → wskazuje gdzie szukać kontekstu
2. **KONTEKST** (`README.md`) → wyjaśnia czym jest dany obszar
3. **INSTRUKCJE** (`PROMPT.md` lub `ZASADY.md`) → szczegółowe workflow i zasady

---

## Struktura repozytorium

### 📝 Notatki/
**Główne źródło informacji** o postępach, decyzjach i ustaleniach projektowych.

| Co | Gdzie |
|----|-------|
| Kontekst - czym są notatki, rodzaje | `Notatki/README.md` |
| Workflow przetwarzania | `Notatki/PROMPT.md` |
| Rejestr przetworzonych | `Notatki/_rejestr_przetworzonych.md` |

**Podkatalogi:**
- `Rada architektów/` - decyzje architektoniczne, nowe koncepcje, problemy techniczne
- `Sprint review/` - podsumowania sprintów, demo funkcjonalności
- `Spotkania projektowe/` - szczegółowe omówienia projektów

---

### 📂 projekty/
**Dokumentacja wszystkich projektów** R&D i klienckich.

| Co | Gdzie |
|----|-------|
| Indeks wszystkich projektów | `projekty/README.md` |
| **Struktura** Project Canvas | `projekty/ZASADY.md` |
| **Styl pisania** dokumentacji | `projekty/STYL.md` |
| Szablon nowego projektu | `projekty/SZABLON.md` |

**Struktura projektu:**
Każdy projekt ma **dwa pliki**:
- `README.md` - krótka mapa nawigacyjna (~50 linii)
- `Nazwa-projektu.md` - pełny **Project Canvas** (szczegółowa dokumentacja)

**Kategorie projektów:**
- `moduly/` - główne moduły systemu AMODIT
- `cross-cutting/` - funkcjonalności przekrojowe
- `integracje/` - integracje z systemami zewnętrznymi
- `klienci/` - prace dedykowane dla klientów
- `koncepcje/` - pomysły i proof-of-concept
- `dokumentacja/` - standardy i procedury

**Obszary specjalne:**

#### projekty/backlog/
Metodyka zarządzania backlogiem AMODIT.

| Co | Gdzie |
|----|-------|
| Kontekst - czym jest backlog, metodyka | `projekty/backlog/README.md` |
| Aktywacja roli Strażnika | `projekty/backlog/PROMPT.md` |
| Szczegółowa instrukcja Strażnika | `projekty/backlog/strażnik/PROMPT instrukcja - Strażnik Metodyki Produktowej AMODIT.md` |
| Filozofia "DLACZEGO" | `projekty/backlog/strażnik/Model Pracy Analitycznej Zespołu (Wersja Zintegrowana).md` |
| Taktyka "JAK" - Playbook | `projekty/backlog/strażnik/Przewodnik Kwalifikacji i Nazewnictwa Artefaktów (backlog_playbook).md` |

#### projekty/UC moduł raportowy/
Baza wiedzy Use Cases modułu raportowego.

| Co | Gdzie |
|----|-------|
| Kontekst - czym są UC | `projekty/UC moduł raportowy/README.md` |
| Workflow tworzenia UC | `projekty/UC moduł raportowy/PROMPT.md` |
| Use Cases | `projekty/UC moduł raportowy/use-cases/` |

---

## Model Operacyjny: Agenty i Skills

Gemini adoptuje model pracy oparty na **Agentach** i **Umiejętnościach (Skills)** zdefiniowany w konfiguracji `.claude/`. Zapewnia to spójność procesów między różnymi modelami AI pracującymi na repozytorium.

### Struktura logiczna

1.  **Agenty (`.claude/agents/`)**: Definiują **KIM** jesteś i **JAKI** proces masz wykonać (workflow, triggery, zasoby).
2.  **Skills (`.claude/skills/`)**: Definiują **JAK** wykonać konkretne zadanie (SOP, formatowanie, checklisty).

**Workflow:**
1.  Zidentyfikuj intencję użytkownika (trigger).
2.  Aktywuj odpowiedniego Agenta (przeczytaj plik w `.claude/agents/`).
3.  Wczytaj wymagane przez Agenta Skills (pliki w `.claude/skills/`) oraz zasoby pomocnicze (np. słowniki).
4.  Wykonaj zadanie zgodnie z procedurą.

### Dostępne Agenty

#### 🧹 Agent: `transcript-cleaner`
**Aktywacja:**
- "Oczyść transkrypcje"
- "Przetwórz transkrypcję"
- "Oczyść oczekujące"

**Zadania:**
- Batchowe lub pojedyncze czyszczenie transkrypcji ASR.
- Korekta fonetyczna (Słownik Domenowy).
- Formatowanie dialogów.
- Aktualizacja rejestru `_transkrypcje.md`.

**Definicja:** `.claude/agents/transcript-cleaner.md`
**Skill:** `.claude/skills/transcript-cleaning/SKILL.md`

---

#### 📝 Agent: `note-maker`
**Aktywacja:**
- "Wygeneruj kolejną notatkę"
- "Zrób notatkę"
- "Przetwórz transkrypcję na notatkę"

**Zadania:**
- Tworzenie strukturalnych notatek ze spotkań.
- Auto-detekcja typu spotkania (Rada Architektów, Sprint Review, etc.).
- Mapowanie tematów na projekty.
- Aktualizacja rejestru `_rejestr_przetworzonych.md`.
- **Tryb pojedynczy** - jedna notatka na sesję.

**Definicja:** `.claude/agents/note-maker.md`
**Skills (zależnie od typu):** `.claude/skills/note-types/{typ}/SKILL.md`

---

#### 📝📝📝📝 Agent: `batch-note-maker`
**Aktywacja:**
- "Wygeneruj notatki z pozostałych transkrypcji"
- "Przetwórz 4 kolejne transkrypcje na notatki"
- "Batch generowanie notatek"

**Zadania:**
- Tworzenie strukturalnych notatek ze spotkań (batch 4 notatek).
- Auto-detekcja typu spotkania (Rada Architektów, Sprint Review, etc.).
- Mapowanie tematów na projekty.
- Aktualizacja rejestru `_rejestr_przetworzonych.md`.
- **Tryb batch** - 4 notatki sekwencyjnie w jednej sesji, automatyczna kontynuacja.

**Definicja:** `.claude/agents/batch-note-maker.md`
**Skills (zależnie od typu):** `.claude/skills/note-types/{typ}/SKILL.md`

---

## Specjalistyczne Role Kontekstowe

Role, które mogą nie mieć jeszcze pełnej definicji Agenta w `.claude`, ale są kluczowe dla specyficznych obszarów.

### 🛡️ "Strażnik Backlogu"
**Aktywacja:** Praca z `projekty/backlog/` lub gdy użytkownik poprosi o analizę backlogu.

**Workflow:** `projekty/backlog/PROMPT.md`

**Rola:** Sceptyczny mentor i audytor metodyki dla PDM-ów. Kwestionowanie propozycji, wykrywanie anty-wzorców, wymuszanie zgodności z metodyką.

### 📋 "Asystent Use Cases"
**Aktywacja:** Praca z `projekty/UC moduł raportowy/`.

**Workflow:** `projekty/UC moduł raportowy/PROMPT.md`

**Zadania:** Tworzenie i walidacja Use Cases według standardu.

### 🔗 "Połącz z Azure DevOps"
**Aktywacja:** Gdy użytkownik napisze `az devops` lub `połącz z azure`.

**Konfiguracja:**
- **Organizacja:** `https://dev.azure.com/astrafox`
- **Projekt:** `AMODIT`

**Workflow:**
1. Wykonaj `az login`.
2. Skonfiguruj domyślne wartości: `az devops configure --defaults organization=https://dev.azure.com/astrafox project=AMODIT`.
3. Zweryfikuj konfigurację: `az devops configure --list`.

---

## Ważne zasady

1.  **Priorytet `.claude/`:** Jeśli istnieje definicja Agenta/Skilla w katalogu `.claude`, jest ona nadrzędna względem luźnych instrukcji w tym pliku.
2.  **Hierarchia dokumentów:**
    *   Ten plik (`GEMINI.md`) to mapa.
    *   `README.md` to kontekst.
    *   Agenty i Skills to instrukcje wykonawcze.
3.  **Adaptuj rolę** do kontekstu zadania.
4.  **Pytaj o zatwierdzenie** przed dużymi zmianami.
5.  **Zachowuj chronologię** przy przetwarzaniu notatek i transkrypcji.
6.  **Linkuj, nie duplikuj** - referencje do dokumentów zamiast kopiowania treści.
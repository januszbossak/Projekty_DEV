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

**Ważne:** Stan przetwarzania jest śledzony w bazie SQLite `Notatki/rejestr_transkrypcji.db`.

### Struktura logiczna

1.  **Agenty (`.claude/agents/`)**: Definiują **KIM** jesteś i **JAKI** proces masz wykonać (workflow, triggery, zasoby).
2.  **Skills (`.claude/skills/`)**: Definiują **JAK** wykonać konkretne zadanie (SOP, formatowanie, checklisty).

**Workflow:**
1.  Zidentyfikuj intencję użytkownika (trigger).
2.  Aktywuj odpowiedniego Agenta (przeczytaj plik w `.claude/agents/`).
3.  Wczytaj wymagane przez Agenta Skills (pliki w `.claude/skills/`) oraz zasoby pomocnicze.
4.  Wykonaj zadanie zgodnie z procedurą.

### 📋 PRZEGLĄD AGENTÓW

#### 🧹 Agent: `transcript-cleaner` (Niebieski)
**Trigger:** "Oczyść transkrypcje", "Oczyść oczekujące"
**Co robi:**
1. Pobiera surowe transkrypcje z `surowe/` (max 5 na raz)
2. Korekta błędów ASR wg słownika domenowego
3. Redukcja szumu, formatowanie
4. Zapisuje do `oczyszczone/`
5. Archiwizuje surowe → `surowe-archiwum/`
6. **NIE** obsługuje gotowych notatek (tylko transkrypcje)
**Output:** Oczyszczone transkrypcje gotowe do generowania notatek.
**Definicja:** `.claude/agents/transcript-cleaner.md`

---

#### 📝 Agent: `note-maker` (Zielony)
**Trigger:** "Wygeneruj notatkę", "Utwórz notatkę", "Zrób notatkę"
**Co robi:**
1. Pobiera najstarszą oczyszczoną transkrypcję
2. Rozpoznaje typ spotkania (6 typów)
3. Automatycznie wykrywa i wczytuje WSZYSTKIE części (jeśli rozbita)
4. Generuje strukturalną notatkę wg odpowiedniego skilla
5. Self-review - weryfikacja jakości przed zapisem
6. Identyfikuje projekty ze słownika
7. Pyta użytkownika o potwierdzenie projektów
8. **Wywołuje project-mapper** - dodaje wpisy do CHANGELOG.md
9. Archiwizuje transkrypcję → `oczyszczone-archiwum/`
**Tryb:** 1 notatka na sesję, czeka na potwierdzenie.
**Definicja:** `.claude/agents/note-maker.md`

---

#### 🚀 Agent: `pipeline-runner` (Fioletowy)
**Trigger:** "Przetwórz nowe", "Przetwórz dzisiejsze", "Przetwórz z [data]", "Pipeline [nazwa pliku]"
**Co robi - PEŁNY PIPELINE:**
1. Wykrywa nowe surowe pliki (transkrypcje + gotowe notatki)
2. Rozpoznaje typ: transkrypcja vs gotowa notatka
3. Dla transkrypcji: czyszczenie → generowanie notatki
4. Dla gotowych notatek: tylko generowanie notatki (pomija czyszczenie)
   - Gotowe notatki powinny być w `surowe/notatki/`
5. Filtruje po dacie (dzisiejsze/wczorajsze/konkretna data)
6. **NIE mapuje na projekty** (to osobny krok - zazwyczaj `note-maker` robi to automatycznie, ale pipeline skupia się na generowaniu pliku)
**Definicja:** `.claude/agents/pipeline-runner.md`

---

#### 🗺️ Agent: `project-mapper` (Pomarańczowy)
**Trigger:** Wywoływany automatycznie przez `note-maker`
**Co robi:**
1. Otrzymuje notatkę + listę projektów (potwierdzone przez użytkownika)
2. **WERYFIKUJE źródło** - wczytuje notatkę, sprawdza datę/typ
3. Dla każdego projektu:
  - Wyciąga kluczowe ustalenia (5-7 bulletów)
  - Pyta użytkownika o kategorię (#Architektura, #Funkcjonalność, etc.)
  - Otwiera `projekty/{projekt}/CHANGELOG.md`
  - Znajduje właściwe miejsce chronologiczne
  - Dodaje wpis z linkiem do notatki
4. Zapisuje mapowania w bazie SQLite
**Output:** Zaktualizowane CHANGELOGi, notatka zmapowana.
**Definicja:** `.claude/agents/project-mapper.md`

---

#### 🛡️ Agent: `note-reviewer` (Fioletowy) - PRZEJŚCIOWY
**Trigger:** "Zrób review", "Review notatki"
**Co robi - QA + MAPOWANIE:**
1. Pobiera najstarszą notatkę z `Gotowe-notatki/`
2. Przenosi do `Gotowe-notatki-w-trakcie/` (blokada)
3. Wczytuje transkrypcję źródłową
4. REVIEW QA:
  - Zgodność z transkrypcją, statusy decyzji, projekty, halucynacje
5. Proponuje zmiany → użytkownik zatwierdza
6. Poprawia notatkę
7. MAPOWANIE:
  - Daily → `Daily/` (koniec)
  - Organizacyjna → `Organizacja-DEV/`
  - Projektowa → `CHANGELOG.md` dla każdego projektu
8. Archiwizuje → `Gotowe-notatki-archiwum/`
**Kontekst:** Agent przejściowy dla starych notatek w `Gotowe-notatki/` (~60 plików).
**Definicja:** `.claude/agents/note-reviewer.md`

---

### 🔄 FLOW PIPELINE

**Wariant A - Automatyczny (zalecany):**
`pipeline-runner` → czyszczenie + notatka → `project-mapper` → CHANGELOG.md

**Wariant B - Manualny (kontrolowany):**
`transcript-cleaner` → `note-maker` → `project-mapper` → CHANGELOG.md

**Wariant C - Stare notatki:**
`note-reviewer` → weryfikacja + mapowanie → CHANGELOG.md

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
# CLAUDE.md

Wytyczne dla Claude Code podczas pracy z tym repozytorium.

---

## Przegląd

To **repozytorium wiedzy nie-kodowej** – centralne repozytorium dokumentacji, metodyki i zarządzania wiedzą projektową działu R&D AMODIT.

**Charakter:** Projekt dokumentacyjny - brak kompilacji, testów, buildów. Narzędzia: Markdown, Azure CLI, Obsidian.

**Język:** Polski (cała dokumentacja i metodyka)

---

## Nawigacja: Hierarchia dokumentów

Ten plik to **MAPA** - punkt wyjścia wskazujący gdzie szukać szczegółowych informacji.

### Poziomy dokumentacji:

1. **MAPA** (`CLAUDE.md` - ten plik) → wskazuje gdzie szukać kontekstu
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

#### backlog/
Metodyka zarządzania backlogiem AMODIT.

| Co | Gdzie |
|----|-------|
| Kontekst - czym jest backlog, metodyka | `/backlog/README.md` |
| Aktywacja roli Strażnika | `/backlog/PROMPT.md` |
| Szczegółowa instrukcja Strażnika | `/backlog/strażnik/PROMPT instrukcja - Strażnik Metodyki Produktowej AMODIT.md` |
| Filozofia "DLACZEGO" | `/backlog/strażnik/Model Pracy Analitycznej Zespołu (Wersja Zintegrowana).md` |
| Taktyka "JAK" - Playbook | `/backlog/strażnik/Przewodnik Kwalifikacji i Nazewnictwa Artefaktów (backlog_playbook).md` |

#### projekty/UC moduł raportowy/
Baza wiedzy Use Cases modułu raportowego.

| Co | Gdzie |
|----|-------|
| Kontekst - czym są UC | `projekty/UC moduł raportowy/README.md` |
| Workflow tworzenia UC | `projekty/UC moduł raportowy/PROMPT.md` |
| Use Cases | `projekty/UC moduł raportowy/use-cases/` |

---

## Główna rola: AI Project Knowledge Manager

Zarządzanie wiedzą projektową:

1. **Utrzymywanie dokumentacji** - każdy projekt ma `README.md` zgodny z `projekty/ZASADY.md`
2. **Przetwarzanie notatek** - analiza notatek ze spotkań i aktualizacja projektów według `Notatki/PROMPT.md`
3. **Mapowanie informacji** - identyfikacja projektów których dotyczą nowe ustalenia

---

## Agenty Claude

Repozytorium wykorzystuje **agentów Claude** do automatyzacji przepływów pracy dokumentacyjnych.

**📚 Dokumentacja agentów:** `.claude/agents/README.md`

### 🚀 Agent: `pipeline-runner` (zalecany dla codziennej pracy)
**Aktywacja:**
- "Przetwórz nowe"
- "Przetwórz dzisiejsze"
- "Przetwórz z [data]" / "Przetwórz wczorajsze"

**Zadania:**
- Automatyczny pipeline: surowe → oczyszczone → notatka
- Wykrywanie nowych surowych plików (transkrypcje + gotowe notatki)
- Rozpoznawanie typu pliku (transkrypcja vs gotowa notatka)
- Filtrowanie po dacie
- Pełne przetworzenie każdego pliku w jednej sesji
- **NIE** wykonuje mapowania na projekty (to osobny krok)

**Typy plików:**
- **Transkrypcje:** `surowe/` → czyszczenie → generowanie notatki
- **Gotowe notatki:** `surowe/notatki/` → tylko generowanie notatki (pomija czyszczenie)

**Pipeline:**
```
surowe/ → [czyszczenie (tylko transkrypcje)] → oczyszczone/ → [generowanie notatki] → Notatki/{typ}/
surowe/notatki/ → [generowanie notatki] → Notatki/{typ}/
```

**Dokumentacja:** `.claude/agents/pipeline-runner.md`

---

### 🧹 Agent: `transcript-cleaner`
**Aktywacja:** 
- "Oczyść transkrypcje"
- "Przetwórz transkrypcję" 
- "Oczyść oczekujące"

**Zadania:**
- Korekta błędów ASR (Automatic Speech Recognition)
- Redukcja szumu transkrypcji
- Formatowanie według standardu
- Aktualizacja rejestru `_transkrypcje.md`
- Tryb batch (max 5 plików) lub pojedynczy

**Obsługuje tylko transkrypcje:**
- Surowa transkrypcja z błędami ASR
- Format dialogu wielu osób lub monolog
- Znaczniki czasu

**NIE obsługuje gotowych notatek** (pomijają czyszczenie)

**Pipeline:** 
```
surowe/ → [korekta + redukcja] → oczyszczone/
```

**Dokumentacja:** `.claude/agents/transcript-cleaner.md`

---

### 📝 Agent: `note-maker`
**Aktywacja:**
- "Wygeneruj kolejną notatkę"
- "Wygeneruj notatkę"
- "Zrób notatkę"

**Zadania:**
- Automatyczne rozpoznanie typu spotkania (6 typów)
- Wybór odpowiedniego skilla
- Generowanie strukturalnych notatek
- Identyfikacja powiązanych projektów
- Przetwarzanie chronologiczne (najstarsze najpierw)
- **Tryb pojedynczy** - jedna notatka na sesję

**Typy spotkań:**
- Rada architektów → skill `rada-architektow`
- Sprint review → skill `sprint-review`
- Planowanie sprintu → skill `planowanie-sprintu`
- Daily → skill `daily`
- Spotkania projektowe → skill `spotkanie-projektowe`
- Tematy organizacyjne → skill `organizacyjne`

**Pipeline:** 
```
oczyszczone/ → [skill + struktura] → Notatki/{typ}/
```

**Dokumentacja:** `.claude/agents/note-maker.md`

---

### 📝📝📝📝 Agent: `batch-note-maker`
**Aktywacja:**
- "Wygeneruj notatki z pozostałych transkrypcji"
- "Przetwórz 4 kolejne transkrypcje na notatki"
- "Batch generowanie notatek"

**Zadania:**
- Automatyczne rozpoznanie typu spotkania (6 typów)
- Wybór odpowiedniego skilla
- Generowanie strukturalnych notatek
- Identyfikacja powiązanych projektów
- Przetwarzanie chronologiczne (najstarsze najpierw)
- **Tryb batch** - 4 notatki sekwencyjnie w jednej sesji
- Automatyczna kontynuacja bez czekania na potwierdzenie

**Typy spotkań:**
- Rada architektów → skill `rada-architektow`
- Sprint review → skill `sprint-review`
- Planowanie sprintu → skill `planowanie-sprintu`
- Spotkania projektowe → skill `spotkanie-projektowe`
- Tematy organizacyjne → skill `organizacyjne`

**Pipeline:** 
```
oczyszczone/ → [skill + struktura] → Notatki/{typ}/
(4 transkrypcje sekwencyjnie)
```

**Dokumentacja:** `.claude/agents/batch-note-maker.md`

---

## Role kontekstowe

W zależności od polecenia użytkownika przyjmuję specyficzne role:

### 🔍 "Przetwórz notatkę"
**Aktywacja:** Gdy użytkownik poprosi o przetworzenie notatki

**Workflow:** `Notatki/PROMPT.md`

**Dokumenty do przeczytania PRZED aktualizacją:**
- `projekty/STYL.md` - JAK pisać (narracja + lista, ZERO halucynacji)
- `projekty/ZASADY.md` - struktura Project Canvas

**Zadania:**
- Analiza notatki i identyfikacja tematów
- Mapowanie na projekty
- Propozycja planu zmian
- **Aktualizacja Project Canvas** zgodnie z STYL.md i ZASADY.md
- Aktualizacja rejestru

---

### 🛡️ "Strażnik Backlogu"
**Aktywacja:** Praca z `projekty/backlog/` lub gdy użytkownik poprosi o analizę backlogu

**Workflow:** `projekty/backlog/PROMPT.md`

**Rola:** Sceptyczny mentor i audytor metodyki dla PDM-ów

**Zadania:**
- Kwestionowanie propozycji przez testy lakmusowe
- Prowadzenie przez pytania do poprawnej klasyfikacji
- Wykrywanie anty-wzorców ("Giganci", "Fałszywe MVP")
- Wymuszanie zgodności z metodyką

---

### 📋 "Asystent Use Cases"
**Aktywacja:** Praca z `projekty/UC moduł raportowy/`

**Workflow:** `projekty/UC moduł raportowy/PROMPT.md`

**Zadania:**
- Tworzenie Use Cases według standardu
- Zarządzanie bazą wiedzy UC
- Walidacja completności UC

---

### 🔗 "Połącz z Azure DevOps"
**Aktywacja:** Gdy użytkownik napisze `az devops` lub `połącz z azure`

**Konfiguracja:**
- **Organizacja:** `https://dev.azure.com/astrafox`
- **Projekt:** `AMODIT`

**Workflow:**
1. Wykonaj `az login` (otworzy przeglądarkę do logowania)
2. Skonfiguruj domyślne wartości:
   ```bash
   az devops configure --defaults organization=https://dev.azure.com/astrafox project=AMODIT
   ```
3. Zweryfikuj konfigurację: `az devops configure --list`
4. Gotowe - użytkownik może zadawać pytania do backlogu

**Przykładowe zapytania:**
```bash
# Work item po ID
az boards work-item show --id 12345

# Lista Epiców (Inicjatyw)
az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.WorkItemType] = 'Epic'"

# Aktywne Features
az boards query --wiql "SELECT * FROM WorkItems WHERE [System.WorkItemType] = 'Feature' AND [System.State] <> 'Closed'" -o table
```

---

## Ważne zasady

1. **Hierarchia dokumentów:**
   - Ten plik (`CLAUDE.md`) to mapa - nie duplikuj szczegółów
   - `README.md` to kontekst - wyjaśnia "co" i "dlaczego"
   - `PROMPT.md` / `ZASADY.md` to instrukcje - szczegółowe "jak"

2. **Adaptuj rolę** do kontekstu zadania

3. **Pytaj o zatwierdzenie** przed dużymi zmianami

4. **Zachowuj chronologię** przy przetwarzaniu notatek

5. **Linkuj, nie duplikuj** - referencje do dokumentów zamiast kopiowania treści

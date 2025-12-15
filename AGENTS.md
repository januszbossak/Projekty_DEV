# Repository Guidelines

## Project Structure & Module Organization
- `Notatki/` – główny obszar pracy: surowe transkrypcje w `Transkrypcje/surowe/`, oczyszczone w `Gotowe-notatki/`, blokada w `Gotowe-notatki-w-trakcie/`, archiwum w `Gotowe-notatki-archiwum/`; `PROMPT.md` opisuje workflow.
- `Projekty/` – Project Canvas i materiały referencyjne; używaj standardów z `STYL.md`, `ZASADY.md`, `SZABLON*.md`.
- `.claude/` – **główne narzędzie pracy**: definicje agentów w `.claude/agents/*.md`, słowniki w `.claude/skills/`; mapowanie projektów zawsze z `.claude/skills/_SLOWNIK_PROJEKTOW.md`.
- `Backlog/`, `Integracje/`, `koncepcje/`, `Roadmapa/` – repozytoria wiedzy tematycznej; zachowuj istniejące nazewnictwo katalogów (kebab-case).

## Agent-First Workflow (Claude)
- Preferuj gotowe agenty z `.claude/agents/` zamiast ręcznych edycji: `pipeline-runner` (surowe → notatki), `transcript-cleaner` (oczyszczanie), `note-maker` (notatki), `note-reviewer` (weryfikacja gotowych), `project-mapper` (mapowanie na projekty).
- Przy mapowaniu zawsze wczytuj `_SLOWNIK_PROJEKTOW.md`; ignoruj projekty wpisane w stare notatki jeśli nie ma ich w słowniku.
- Kolejka notatek: przesuwaj pliki przez `Gotowe-notatki/` → `Gotowe-notatki-w-trakcie/` → `Gotowe-notatki-archiwum/`; nie omijaj blokady.
- Uzupełnienia lub korekty stylu zapisuj w plikach referencyjnych (`STYL.md`, `ZASADY.md`, `PROMPT.md`) zamiast w komentarzach PR.

## Build, Test, and Development Commands
- Repozytorium jest dokumentacyjne – brak build/test; pracuj w Markdown.
- Wyszukiwanie: `rg "<fraza>" Notatki` lub `rg --files Projekty` aby znaleźć pliki do edycji.
- Sprawdzenie zmian: `git status`, `git diff`.

## Coding Style & Naming Conventions
- Markdown: jasne nagłówki, krótkie akapity, listy punktowane dla decyzji; unikaj kodu źródłowego poza niezbędnymi przykładami.
- Styl narracyjny z `Projekty/STYL.md`: najpierw kontekst (2–3 zdania), potem twarde ustalenia; zero halucynacji – gdy brakuje danych, oznacz `[DO USTALENIA]`.
- Nazwy plików notatek: `YYYY-MM-DD [Typ/Temat].md` (np. `2025-11-28 Rada architektów.md`, `YYYY-MM-DD [Temat] - wypowiedź.md`).
- Projekty/katalogi: kebab-case i spójne z listą w `Projekty/README.md`; nie twórz nowych nazw bez potwierdzenia w słowniku.

## Testing Guidelines
- Brak testów automatycznych; weryfikuj ręcznie zgodność z transkrypcją/notatką źródłową.
- Po edycji notatki sprawdź, czy wszystkie decyzje są przeniesione do właściwych projektów i czy wskazane projekty istnieją w `_SLOWNIK_PROJEKTOW.md`.
- Utrzymuj spójność dat i ścieżek (np. zgodność między `Gotowe-notatki/` a rejestrami).

## Commit & Pull Request Guidelines
- Commity krótkie, w trybie rozkazującym (np. `Dodaj opis pipeline'u`, `Uzupełnij projekt Slowniki`); jeden logiczny temat na commit.
- Opis PR: cel zmiany, dotknięte katalogi/sekcje, link do powiązanej notatki lub zadania; dołącz fragmenty przed/po, jeśli zmieniasz format dokumentu.
- Nie usuwaj ani nie przenoś plików z kolejek (`Gotowe-notatki*`) bez opisania tego w commit message/PR.

## Agent-Specific Tips
- Note reviewer: przenosi plik z `Gotowe-notatki/` do `Gotowe-notatki-w-trakcie/` jako blokadę; mapowanie wyłącznie ze słownika; ignoruj projekty wpisane w starej notatce.
- Transcript cleaner/note maker: oczyszczaj pliki z `Transkrypcje/surowe/`; gotowe dokumenty w `surowe/notatki/` pomijają etap czyszczenia.
- Każdą zmianę w stylu lub procesie dopisuj do odpowiedniego pliku referencyjnego (`STYL.md`, `ZASADY.md`, `PROMPT.md`) zamiast tylko w komentarzu PR.

# Propozycja struktury: Organizacja działu DEV

## Koncepcja

Struktura oparta na **kategoriach tematycznych** z możliwością linkowania Obsidian. Każdy temat organizacyjny ma własny plik, który ewoluuje w czasie.

---

## Struktura folderowa

```
Organizacja działu DEV/
├── README.md                    # Główny indeks wszystkich kategorii
├── Procesy/                     # Jak pracujemy
│   ├── README.md               # Indeks procesów
│   ├── Code-review.md          # Proces code review
│   ├── Daily.md                # Jak prowadzimy Daily
│   ├── Planowanie-sprintu.md   # Proces planowania
│   ├── Release-process.md      # Proces wydawania wersji
│   └── ...
├── Narzędzia/                   # Jakich narzędzi używamy
│   ├── README.md
│   ├── Azure-DevOps.md         # Konfiguracja, boards, workflow
│   ├── Git.md                  # Konwencje, branching strategy
│   ├── Środowiska.md           # DEV/TEST/PROD, dostępy
│   └── ...
├── Zespół/                      # Struktura i komunikacja
│   ├── README.md
│   ├── Role-i-odpowiedzialnosci.md
│   ├── Spotkania-cykliczne.md  # Rada Architektów, Daily, Sprint Review
│   ├── Kanały-komunikacji.md   # Teams, Slack
│   └── ...
├── Standardy/                   # Konwencje i zasady
│   ├── README.md
│   ├── Konwencje-nazewnictwa.md
│   ├── Standardy-kodowania.md
│   ├── Dokumentacja.md         # Jak dokumentujemy projekty
│   └── ...
└── HR/                          # Ludzie i organizacja
    ├── README.md
    ├── Onboarding.md           # Proces wdrażania nowych
    ├── Urlopy-i-zastepstwa.md
    └── ...
```

---

## Format pliku tematycznego

Każdy temat ma własny plik, który ewoluuje w czasie:

```markdown
# [Nazwa tematu]

**Kategoria:** [Procesy / Narzędzia / Zespół / Standardy / HR]
**Ostatnia aktualizacja:** [[YYYY-MM-DD]]

---

## Obecny stan

[Opis aktualnego ustalenia - co obowiązuje teraz]

**Status:** ✅ Obowiązuje od [[YYYY-MM-DD]] / 💡 Do wdrożenia / 🔍 Do weryfikacji

**Odpowiedzialny:** **[Imię Nazwisko]** – [zakres odpowiedzialności]

---

## Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[YYYY-MM-DD]] | [Opis zmiany] | [[YYYY-MM-DD Rada architektów]] |
| [[YYYY-MM-DD]] | [Opis zmiany] | [[YYYY-MM-DD Planowanie sprintu]] |

---

## Szczegóły

[Szczegółowy opis ustalenia, zasad, procedur]

---

## Powiązane tematy

- [[Inny-temat]] – [jak się łączy]
- [[Kolejny-temat]] – [jak się łączy]
```

---

## Przykłady tematów

### Przykład 1: Daily

**Plik:** `Procesy/Daily.md`

```markdown
# Daily

**Kategoria:** Procesy
**Ostatnia aktualizacja:** [[2025-11-20]]

---

## Obecny stan

Daily prowadzimy codziennie o 9:00. Struktura:
1. Status update (wszyscy uczestnicy)
2. Omówienie backlogu (węższe grono)
3. Tematy organizacyjne (opcjonalnie)

**Status:** ✅ Obowiązuje od [[2025-11-01]]

**Odpowiedzialny:** **Janusz** – prowadzenie Daily, egzekwowanie struktury

---

## Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-11-01]] | Wprowadzenie struktury dwuczęściowej | [[2025-11-01 Daily]] |
| [[2025-10-15]] | Zmiana godziny z 9:30 na 9:00 | [[2025-10-15 Rada architektów]] |

---

## Szczegóły

**Część 1: Status update**
- Każdy mówi co robi
- Czy są blokery
- Co planuje zrobić

**Część 2: Backlog**
- Nowe zgłoszenia
- Priorytety
- Przypisania

---

## Powiązane tematy

- [[Planowanie-sprintu]] – Daily informuje o postępach w sprincie
- [[Spotkania-cykliczne]] – Daily jest częścią cyklu spotkań
```

### Przykład 2: Azure DevOps

**Plik:** `Narzędzia/Azure-DevOps.md`

```markdown
# Azure DevOps

**Kategoria:** Narzędzia
**Ostatnia aktualizacja:** [[2025-11-17]]

---

## Obecny stan

Używamy Azure DevOps do zarządzania backlogiem. Struktura:
- Epik → Feature → PBI
- Każdy projekt ma własny backlog
- Estymacje w story points

**Status:** ✅ Obowiązuje od [[2025-11-17]]

**Odpowiedzialny:** **Kamil** – konfiguracja, szkolenia

---

## Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-11-17]] | Zmiana struktury z PBI na Epik→Feature→PBI | [[2025-11-17 Planowanie sprintu]] |
| [[2025-10-27]] | Wprowadzenie estymacji w story points | [[2025-10-27 Spotkanie projektowe - Przegląd projektów]] |

---

## Szczegóły

**Struktura backlogu:**
- Epik = duży cel biznesowy (np. "Repozytorium plików")
- Feature = funkcjonalność w ramach epiku (np. "Podgląd plików")
- PBI = konkretne zadanie (np. "Dodać podgląd PDF")

**Konwencje nazewnictwa:**
- Epiki: `[Projekt] - [Cel]`
- Features: `[Funkcjonalność]`
- PBI: `[Akcja] - [Szczegóły]`

---

## Powiązane tematy

- [[Planowanie-sprintu]] – jak używamy Azure DevOps w planowaniu
- [[Git]] – integracja z repozytoriami Git
```

---

## Workflow wyłapywania tematów

### Z notatek projektowych

Gdy w notatce pojawia się temat organizacyjny:

1. **Zidentyfikuj kategorię** (Procesy / Narzędzia / Zespół / Standardy / HR)
2. **Zidentyfikuj temat** (np. "Daily", "Azure DevOps", "Code review")
3. **Utwórz lub zaktualizuj plik** w odpowiednim folderze
4. **Dodaj wpis w historii zmian** z linkiem do źródłowej notatki
5. **Zaktualizuj README** w kategorii (jeśli nowy temat)

### Linkowanie zwrotne

W źródłowej notatce dodaj link do tematu organizacyjnego:

```markdown
**Ustalenia organizacyjne:**
- [[Daily]] – zmiana struktury spotkania
- [[Azure-DevOps]] – nowa struktura backlogu
```

---

## Zalety tej struktury

✅ **Tematyczność** – łatwo znaleźć wszystkie ustalenia o Daily w jednym miejscu  
✅ **Historia** – widać jak ustalenia ewoluowały w czasie  
✅ **Linkowanie** – Obsidian tworzy graf powiązań między tematami  
✅ **Skalowalność** – łatwo dodać nowy temat  
✅ **Wyłapywanie** – można wyodrębniać tematy z różnych notatek do jednego pliku  

---

## Przykładowe tematy do utworzenia

### Procesy
- Code-review.md
- Daily.md
- Planowanie-sprintu.md
- Release-process.md
- Testowanie.md

### Narzędzia
- Azure-DevOps.md
- Git.md
- Środowiska.md
- Teams.md

### Zespół
- Role-i-odpowiedzialnosci.md
- Spotkania-cykliczne.md
- Kanały-komunikacji.md

### Standardy
- Konwencje-nazewnictwa.md
- Standardy-kodowania.md
- Dokumentacja.md

### HR
- Onboarding.md
- Urlopy-i-zastepstwa.md

---

## Uwagi

- **Nazwy plików:** Używamy kebab-case (np. `Code-review.md`, nie `Code Review.md`)
- **Linkowanie:** Wszystkie linki przez Obsidian `[[nazwa]]`
- **Daty:** Wszystkie daty jako dzienniki `[[YYYY-MM-DD]]`
- **Źródła:** Linki do notatek źródłowych `[[YYYY-MM-DD Typ notatki]]`


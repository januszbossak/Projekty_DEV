# SKILL: Notatka organizacyjna (Dział DEV)

## Cel

Dokumentowanie ustaleń dotyczących organizacji pracy działu DEV – procesów, zasad, narzędzi, struktury zespołu. Rola: **Sekretarz organizacyjny działu DEV**.

> **WAŻNE:** Te notatki trafiają do dokumentacji organizacyjnej działu DEV: `projekty/Organizacja-DEV/Dokumentacja-organizacyjna/`.

---

## Dane wejściowe

Treści organizacyjne mogą pochodzić z:
- Dedykowanych spotkań organizacyjnych
- Fragmentów innych spotkań (Rada Architektów, Planowanie) – wyodrębnij je

---

## Kiedy użyć tego skilla

Użyj gdy temat dotyczy:
- **Procesy pracy** – jak pracujemy, code review, workflow
- **Narzędzia** – jakich używamy, jak konfigurujemy
- **Struktura zespołu** – role, odpowiedzialności, zmiany
- **Urlopy, zastępstwa** – kto kogo zastępuje
- **Onboarding** – jak wdrażamy nowych
- **Spotkania** – częstotliwość, agenda, uczestnicy
- **Standardy** – konwencje, nazewnictwo, dokumentacja
- **Infrastruktura** – środowiska, dostępy, uprawnienia
- **Retrospektywy** – wnioski, usprawnienia procesu

**NIE używaj** dla:
- Decyzji architektonicznych dot. konkretnych projektów → Rada Architektów
- Planowania zadań w sprincie → Planowanie Sprintu
- Specyfikacji funkcjonalności → Spotkanie Projektowe

---

## Kategorie tematów organizacyjnych

### 1. Procesy i workflow

- Code review – kto, kiedy, jak
- Branching strategy
- CI/CD pipeline
- Release process
- Testowanie

### 2. Narzędzia i infrastruktura

- Azure DevOps – konfiguracja, boards
- Git – konwencje, hooks
- Środowiska DEV/TEST/PROD
- Dostępy i uprawnienia

### 3. Zespół i komunikacja

- Struktura zespołu
- Role i odpowiedzialności
- Spotkania cykliczne
- Kanały komunikacji (Teams, Slack)

### 4. Standardy i dokumentacja

- Konwencje nazewnictwa
- Standardy kodowania
- Dokumentacja techniczna
- Wiki

### 5. HR i organizacja

- Urlopy, zastępstwa
- Onboarding
- Szkolenia
- Oceny, feedback

---

## Format wyjściowy

### Tytuł

```markdown
# Ustalenia organizacyjne – RRRR-MM-DD
```

Lub jeśli wyodrębnione z innego spotkania:
```markdown
# Ustalenia organizacyjne – RRRR-MM-DD (z Rady Architektów)
```

### Metadane

```markdown
**Źródło:** [Spotkanie organizacyjne / Rada Architektów / Planowanie sprintu]
**Kategorie:** [Procesy, Narzędzia, Zespół, Standardy, HR]
```

---

## Szablon notatki

```markdown
# Ustalenia organizacyjne – RRRR-MM-DD

**Źródło:** [źródło]
**Kategorie:** [kategorie]

---

## 1. [Tytuł ustalenia]

**Kategoria:** [Procesy / Narzędzia / Zespół / Standardy / HR]

### Kontekst

[Dlaczego temat został poruszony. Jaki problem rozwiązujemy.]

### Ustalenie

[Co zostało ustalone. Konkretnie.]

**Status:** ✅ Obowiązuje od [data] / 💡 Do wdrożenia / 🔍 Do weryfikacji

### Szczegóły

- [Szczegół 1]
- [Szczegół 2]

### Odpowiedzialny

**[Imię Nazwisko]** – [zakres odpowiedzialności]

---

## 2. [Kolejne ustalenie]

[powtórz strukturę]

---

## Zmiany w stosunku do poprzednich ustaleń

[Jeśli zmieniono wcześniejsze ustalenia – opisz co się zmieniło]

| Było | Jest | Data zmiany |
|------|------|-------------|
| [Stare ustalenie] | [Nowe ustalenie] | RRRR-MM-DD |

---

## Do wdrożenia / Action items

- [ ] **[Osoba]:** [Zadanie] → termin: [data]
- [ ] **[Osoba]:** [Zadanie]
```

---

## Zasady

### 1. Wyodrębniaj z innych spotkań

Jeśli podczas Rady Architektów padły ustalenia organizacyjne:
- **Wyodrębnij je** do osobnej notatki organizacyjnej
- **Nie mieszaj** z decyzjami architektonicznymi
- **Oznacz źródło** w metadanych

### 2. Śledź zmiany

Ustalenia organizacyjne ewoluują. Dokumentuj:
- Co było wcześniej
- Co jest teraz
- Kiedy się zmieniło

### 3. Przypisuj odpowiedzialnych

Każde ustalenie powinno mieć właściciela – osobę odpowiedzialną za egzekwowanie.

### 4. Oznaczaj status

- ✅ **Obowiązuje** – aktywne ustalenie
- 💡 **Do wdrożenia** – zaakceptowane, czeka na implementację
- 🔍 **Do weryfikacji** – wymaga testów/pilotażu
- ❌ **Wycofane** – już nie obowiązuje (zachowaj w historii)

---

## Przykłady tematów

### Przykład 1: Zmiana procesu code review

```markdown
## 1. Nowy proces code review

**Kategoria:** Procesy

### Kontekst

Obecny proces code review trwa zbyt długo – średnio 3 dni na PR. Blokuje to release'y.

### Ustalenie

Wprowadzamy zasadę "24h na review". Jeśli reviewer nie odpowie w 24h, autor może zmergować z notatką.

**Status:** ✅ Obowiązuje od 2025-11-01

### Szczegóły

- Dotyczy wszystkich PR-ów poza hotfixami (te natychmiast)
- Reviewer musi oznaczyć PR jako "Changes requested" lub "Approved"
- Brak reakcji = implicit approval

### Odpowiedzialny

**Damian Kamiński** – egzekwowanie zasady, eskalacje
```

### Przykład 2: Nowy członek zespołu

```markdown
## 2. Onboarding nowego developera

**Kategoria:** HR / Zespół

### Kontekst

Od 1 grudnia dołącza nowy frontend developer.

### Ustalenie

**Tomasz Kowalski** dołącza do zespołu Frontend. Mentor: **Filip**.

**Status:** 💡 Do wdrożenia

### Szczegóły

- Pierwszy tydzień: zapoznanie z kodem, środowiskami
- Drugi tydzień: pierwsze zadanie (mały bugfix)
- Trzeci tydzień: samodzielne zadanie z code review

### Odpowiedzialny

**Filip** – mentor, onboarding techniczny
**Kamil** – formalności HR, dostępy
```

---

## Checklist przed zapisem

- [ ] Temat jest organizacyjny (nie projektowy)
- [ ] Kategoria przypisana
- [ ] Status ustalenia oznaczony
- [ ] Odpowiedzialny przypisany
- [ ] Źródło wskazane (jeśli wyodrębnione z innego spotkania)
- [ ] Zmiany względem poprzednich ustaleń udokumentowane

---

## Lokalizacja pliku wyjściowego

```
projekty/Organizacja-DEV/Dokumentacja-organizacyjna/RRRR-MM-DD Ustalenia organizacyjne.md
```

Lub z oznaczeniem źródła:
```
projekty/Organizacja-DEV/Dokumentacja-organizacyjna/RRRR-MM-DD Ustalenia organizacyjne - (z Rady Architektów).md
```

**Uwaga:** Jeśli nazwa transkrypcji zawiera dodatkowe oznaczenia, dodaj je po typie: `RRRR-MM-DD Ustalenia organizacyjne - [oznaczenia].md`

---

## Powiązane zasoby

- **Katalog dokumentacji:** `projekty/Organizacja-DEV/Dokumentacja-organizacyjna/`
- **Struktura kategorii:** Zobacz `projekty/Organizacja-DEV/STRUKTURA.md`

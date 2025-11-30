# Backlog AMODIT

## Przegląd

Ten katalog zawiera materiały związane z **metodyką zarządzania backlogiem produktu AMODIT** oraz narzędzia do analizy i audytu prac zespołu.

---

## Zakres

### Metodyka produktowa
Zestaw zasad i procesów zapewniających:
- Spójną klasyfikację artefaktów backlogu
- Właściwą hierarchię: Inicjatywa → MVP → Feature → Use Case → Task
- "Outcome over Output" - skupienie na wartości dla użytkownika
- Zasada "Przestań zaczynać, zacznij kończyć"

### Integracja z Azure DevOps
Połączenie z Azure DevOps poprzez `az cli`:
- Zapytania o work items
- Analizy backlogu
- Generowanie raportów
- Dekompozycja struktury prac

---

## Struktura

### `strażnik/`
Dokumentacja roli **Strażnik Metodyki Produktowej** - wyspecjalizowanej roli AI audytora metodyki.

**Kluczowe dokumenty:**
- `PROMPT instrukcja - Strażnik Metodyki Produktowej AMODIT.md` - szczegółowa instrukcja działania Strażnika
- `Model Pracy Analitycznej Zespołu (Wersja Zintegrowana).md` - filozofia "DLACZEGO"
- `Przewodnik Kwalifikacji i Nazewnictwa Artefaktów (backlog_playbook).md` - taktyka "JAK"

### Wyniki analiz
Pliki `.md` generowane przez analizy backlogu (raporty, dekompozycje, audyty).

---

## Dla kogo?

### Product Delivery Managers (PDM)
Główni odbiorcy metodyki - osoby odpowiedzialne za kwalifikację i strukturyzację backlogu.

### Zespół deweloperski
Beneficjenci spójnego, dobrze zorganizowanego backlogu.

### AI (Strażnik)
Audytor metodyki - kwestionuje propozycje, wymusza zgodność z zasadami, prowadzi przez proces kwalifikacji.

---

## Jak korzystać?

### Dla użytkowników ludzkich
1. Przeczytaj `strażnik/Model Pracy Analitycznej Zespołu (Wersja Zintegrowana).md` - zrozum filozofię "DLACZEGO"
2. Studiuj `strażnik/Przewodnik Kwalifikacji i Nazewnictwa Artefaktów (backlog_playbook).md` - naucz się "JAK" klasyfikować artefakty
3. Stosuj testy lakmusowe przed dodaniem czegokolwiek do backlogu

### Dla AI
Zobacz `PROMPT.md` aby aktywować rolę **Strażnika Metodyki Produktowej AMODIT**.

---

## Zasady fundamentalne

### 1. Outcome over Output
Myśl o **biznesowym DLACZEGO** (wartość dla użytkownika), nie o technicznych komponentach.

### 2. Przestań zaczynać, zacznij kończyć
Skup 100% wysiłku zespołu na ukończeniu **JEDNEGO MVP na raz**.

### 3. MVP to wartość, nie worek funkcji
MVP musi być:
- **Niezależnie dostarczalne** - można wdrożyć bez innych MVP
- **Spójna wartość użytkownika** - rozwiązuje konkretny problem
- **Wystarczająco małe** - da się zrealizować w rozsądnym czasie

---

## Aktualizacje metodyki

Metodyka ewoluuje na podstawie doświadczeń zespołu. Wszelkie zmiany w dokumentach `strażnik/` wymagają uzgodnienia z zespołem PDM i zespołem deweloperskim.

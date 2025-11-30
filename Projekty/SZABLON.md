# Szablon Project Canvas

Użyj tego szablonu do tworzenia nowych projektów.

---

## 1. Skopiuj i zmień nazwę

```bash
# Przykład dla projektu klienta WIM "Nowa-funkcja"
cp projekty/SZABLON.md projekty/klienci/WIM/Nowa-funkcja/Nowa-funkcja.md
```

---

## 2. Szablon Project Canvas: `Nazwa-projektu.md`

```markdown
# Project Canvas: [Nazwa Projektu]

**Status:** 🟡 W analizie
**Powód statusu / Bloker:** [Jeśli 🟡 lub 🔴, wyjaśnij dlaczego. Np. "Oczekiwanie na środowisko testowe" lub usuń tę linię jeśli status 🟢]
**Ostatnia aktualizacja:** YYYY-MM-DD
**Klient:** [Nazwa klienta lub "AMODIT (roadmapa)"]
**Data rozpoczęcia:** YYYY-MM-DD
**Budżet/Czas:** [np. 20 MD / do uzupełnienia]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | [Imię] / [do uzupełnienia] | Zarządzanie projektem, kontakt z klientem |
| **Tech Lead** | [Imię] / [do uzupełnienia] | Architektura, Code Review |
| **Deweloper** | [Imię] / [do uzupełnienia] | Implementacja |
| **Tester** | [Imię] / [do uzupełnienia] | |
| **Opiekun handlowy** | [Imię] / [do uzupełnienia] | |
| **Klient (Decydent)** | [Imię Nazwisko] / [do uzupełnienia] | Akceptacja MVP, ostateczne decyzje biznesowe |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
[Opisz problem biznesowy w 2-4 zdaniach. Musi być zrozumiały dla osoby spoza projektu.]

### Cel biznesowy
[Co chcemy osiągnąć z perspektywy biznesu - konkretnie, nie "poprawa" lub "optymalizacja"]

### Cel techniczny
[Co chcemy osiągnąć z perspektywy technicznej]

### Metryka sukcesu
[Jak zmierzymy sukces - konkretne, mierzalne KPI]

Przykład: "Użytkownik może znaleźć dokument w < 5 sekund"

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: [Tytuł zasady]
[Opis zasady - co MUSI być spełnione. Twarde ograniczenie, którego przekroczenie wymaga renegocjacji.]

**Uzasadnienie:** [Dlaczego ta zasada obowiązuje]

### Zasada 2: [Tytuł zasady]
[Opis zasady]

**Uzasadnienie:** [Dlaczego]

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[YYYY-MM-DD]] | [Co zdecydowano - konkretnie] | [Dlaczego - konkretnie] | - |
| ADR-002 | 💡 Propozycja | [[YYYY-MM-DD]] | [Co zdecydowano] | [Dlaczego] | - |
| ADR-003 | ❌ Odrzucone | [[YYYY-MM-DD]] | [Co proponowano] | [Początkowe uzasadnienie] | [Dlaczego odrzucono - konkretnie] |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

**Ukończono:**
- ✅ [Co zostało zrobione]

**Trwa praca nad:**
- [Co obecnie robimy]

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Wysokie]** [Opis ryzyka - konkretnie] | Średnie | Wysoki | [Co robimy aby zminimalizować - konkretnie] | Tech Lead |
| **[Średnie]** [Opis ryzyka] | Niskie | Średni | [Mitygacja] | PDM |

---

### Punkty wymagające decyzji (w fazie analizy)

**Uprawnienia:**
- [ ] [Pytanie 1 do rozstrzygnięcia]
- [ ] [Pytanie 2 do rozstrzygnięcia]

**Technologia:**
- [ ] [Pytanie do rozstrzygnięcia]

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 PoC: "[Nazwa]" (Status: Planowany / W trakcie / Ukończony)

**Cel:** [Dlaczego robimy PoC - co chcemy zweryfikować. Konkretnie.]

**Do zweryfikowania:**
- [ ] [Pytanie/hipoteza 1]
- [ ] [Pytanie/hipoteza 2]

---

### 📦 MVP1: "[Nazwa mówiąca o wartości dla użytkownika]" (Plan: Q4 2025)

**Cel:** [Dlaczego akurat taki zakres - jaką wartość dostarczamy użytkownikowi. Narracja, 2-3 zdania.]

**Definicja ukończenia (DoD):**
- Użytkownik może [konkretne działanie - mierzalne]
- System [konkretne zachowanie - mierzalne]
- Wszystkie [kryteria jakości - konkretne]

**Funkcjonalności:**

#### [Grupa funkcjonalności 1]
- [ ] Funkcjonalność A
- [ ] Funkcjonalność B

#### [Grupa funkcjonalności 2]
- [ ] Funkcjonalność C
- [ ] Funkcjonalność D

**Poza zakresem MVP (Out of Scope):**
- [Co świadomie NIE robimy w tym MVP - aby uniknąć rozползания się zakresu]
- [Np. "Obsługa podpisów chmurowych innych niż mSzafir"]
- [Np. "Wsparcie dla procesorów Intel (tylko Apple Silicon)"]

**Planowana data:** Q4 2025 / [do uzupełnienia]

---

### 📦 MVP2: "[Nazwa]" (Plan: Q1 2026)

**Cel:** [Co rozszerzamy - dlaczego. Narracja.]

**Funkcjonalności:**
- [ ] Funkcjonalność E
- [ ] Funkcjonalność F

**Planowana data:** Q1 2026

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Funkcjonalność X (Priorytet: Niski / Średni / Wysoki)
- Funkcjonalność Y (Priorytet: Niski)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[YYYY-MM-DD]] | Utworzenie projektu - inicjalna specyfikacja | [[YYYY-MM-DD Rada architektów]] / [[YYYY-MM-DD Sprint review]] / [[YYYY-MM-DD Notatka projektowa]] |

---

## 6. PRZYDATNE LINKI

- **Repozytorium:** [link]
- **Środowisko DEV:** [link]
- **Środowisko TEST:** [link]
- **Dokumentacja zewnętrzna:** [link]
- **Umowa z klientem:** [link/numer]
- **Inicjatywa w backlogu:** [link do Azure DevOps]

---

## 7. PODPROJEKTY (opcjonalnie - dla dużych projektów)

Dla projektów złożonych z wielu względnie niezależnych części (np. Edytor-procesow → Edytor-formularzy, Edytor-diagramu).

| Podprojekt | Status | MVP | Opis |
|------------|--------|-----|------|
| [Nazwa-podprojektu](./Nazwa-podprojektu/) | 🟢 W realizacji | MVP1 Q4 2025 | Krótki opis (1 zdanie) |
| [Nazwa-podprojektu-2](./Nazwa-podprojektu-2/) | 🟡 W analizie | - | Krótki opis |

**Uwaga:** Każdy podprojekt ma własny katalog i pełną dokumentację Project Canvas. Zobacz `SZABLON-PODPROJEKT.md`.

---

## X. ARCHITEKTURA TECHNICZNA (opcjonalnie - tylko jeśli konieczne)

### Technologie
- Frontend: [React / Angular / ...]
- Backend: [C# / Node.js / ...]
- Baza danych: [MSSQL / MySQL / ...]

### Struktura bazy danych

**Tabele:**

| Tabela | Kolumny | Opis |
|--------|---------|------|
| `nazwa_tabeli` | `col1`, `col2`, `col3` | Opis przeznaczenia tabeli |

**Diagram relacji (opcjonalnie - dla lepszej czytelności):**

\`\`\`mermaid
erDiagram
    TABLE_1 ||--|{ TABLE_2 : contains
    TABLE_1 {
        int id PK
        string name
        int foreignId FK
    }
    TABLE_2 {
        int id PK
        string description
    }
\`\`\`

### Architektura komponentów (opcjonalnie)

\`\`\`mermaid
graph TD
    A[Frontend] -->|API Request| B[Backend]
    B -->|Query| C[Database]
\`\`\`

### API Endpoints

[Tylko jeśli absolutnie konieczne - lista kluczowych endpointów]
```

---

## 3. Szablon README.md

Stwórz również plik `README.md` w tym samym katalogu:

```markdown
# [Nazwa Projektu]

**Klient:** [Nazwa] / AMODIT (roadmapa)
**Status:** 🟡 W analizie
**PDM:** [Imię] / [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Nazwa-projektu]]

**Uwaga:** Używamy linkowania Obsidian (`[[nazwa]]`) - wszystkie linki przez podwójne nawiasy kwadratowe, nie przez ścieżki.

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem
[1-2 zdania - co jest problemem]

### Rozwiązanie
[1-2 zdania - jak rozwiązujemy + kluczowe elementy jako lista]

### Obecna faza
📋 **W analizie** / 🛠 **MVP1: [Nazwa]** - w rozwoju

**Ukończono:**
- ✅ [Co zrobione]

**W trakcie / Do finalizacji:**
- [Co teraz robimy]

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| [Konkretna decyzja 1] | [Dlaczego] |
| [Konkretna decyzja 2] | [Dlaczego] |

---

## MVP1: [Nazwa]

**Cel:** [Krótko - wartość dla użytkownika]

**Zakres:**
- ✅ [Element 1]
- ✅ [Element 2]
- [ ] [Element 3 - pending]

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| [Ryzyko 1] | [Co robimy] |
| [Ryzyko 2] | [Co robimy] |

---

## Szybkie linki

- Repozytorium: [link]
- Środowisko DEV: [link]
- Backlog: [link do Azure DevOps]
```

---

## 4. Dodaj do centralnego indeksu

Dodaj projekt do `projekty/README.md` w odpowiedniej kategorii:

```markdown
### [Kategoria]
- **[Nazwa-projektu](sciezka/do/katalogu/)** - Krótki opis (1 zdanie)
```

---

## 5. Checklist przed commit

- [ ] Wypełniłem wszystkie sekcje zgodnie z `STYL.md` (narracja + lista)
- [ ] Brak ogólników ("optymalizacja", "poprawa")
- [ ] Brak halucynacji - wszystko wynika z notatek
- [ ] README.md jest spójny z Project Canvas
- [ ] Dodałem projekt do `projekty/README.md`
- [ ] Nazwy plików zgodne z konwencją (`Nazwa-projektu.md`)

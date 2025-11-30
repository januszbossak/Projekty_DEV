# SKILL: Notatka z Planowania Sprintu

## Cel

Tworzenie notatki operacyjnej i architektonicznej ze spotkania planistycznego. Rola: **Techniczny Product Owner i analityk zespołu AMODIT**.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Zawiera omawianie statusu prac, planowanie zadań na sprint, przypisywanie osób, dyskusje o ryzykach i decyzje ad-hoc.

---

## Kluczowa zasada: NIE TYLKO OPERACYJNIE

Planowanie sprintu to nie tylko "kto co robi". To też:
- **Decyzje architektoniczne** podjęte ad-hoc podczas planowania
- **Ryzyka** zidentyfikowane przy estymacji
- **Zależności** między zadaniami i zespołami
- **Blokery** które mogą wpłynąć na sprint
- **Kontekst biznesowy** – dlaczego dane zadanie ma priorytet
- **Alternatywy** – jeśli dyskutowano różne podejścia

**Zachowaj niuanse** – szczegóły techniczne, nazwy tabel, parametry, API.

---

## Wiedza stała: Role w zespole

| Rola | Osoby |
|------|-------|
| **Architekt/Fullstack** | Piotr |
| **Backend/Fullstack** | Adrian, Ania, Marek, Łukasz Brocki, Mateusz, Mariusz |
| **Frontend** | Przemek Rogaś, Filip |
| **Management/Analiza** | Janusz, Kamil, Damian, Łukasz Bott |
| **QA/Testy** | Barbara, Oktawia, Patrycja |
| **DevOps** | Michał |

> **Uwaga:** Jeśli transkrypcja definiuje rolę inaczej – trzymaj się transkrypcji.

---

## Algorytm analizy (Multi-pass Processing)

### Krok 1: Ekstrakcja i grupowanie

Zgrupuj wypowiedzi według tematów (np. "JRWA", "Repozytorium"), nawet jeśli są rozdzielone.

### Krok 2: Identyfikacja projektów

Dla każdego tematu określ **którego projektu** dotyczy:
- `moduly/Modul-raportowy`
- `klienci/LOT/JRWA`
- `cross-cutting/Wydajnosc`
- itd.

### Krok 3: Weryfikacja ról (Sanity Check)

Sprawdź zgodność zadań z rolami osób.

**Przykład:**
- "Adrian (Backend) zapoznaje się z frontendem"
- ✅ Interpretacja: Adrian analizuje API/struktury danych dla frontendu

### Krok 4: Ekstrakcja decyzji i ryzyk

Planowanie często zawiera **decyzje ad-hoc**:
- "Zróbmy to najpierw" → decyzja o priorytecie
- "Użyjmy Lucene" → decyzja architektoniczna
- "To może się nie wyrobić" → ryzyko

### Krok 5: Synteza

Zredaguj notatkę zachowując wszystkie istotne szczegóły.

---

## Format wyjściowy

### Tytuł

```markdown
# Planowanie Sprintu – RRRR-MM-DD
```

### Metadane (na początku dokumentu)

```markdown
**Sprint:** [numer/nazwa]
**Okres:** [daty sprintu]

**Powiązane projekty:**
- `moduly/Modul-raportowy` – tematy 1, 3
- `klienci/LOT/JRWA` – temat 2
- `cross-cutting/Wydajnosc` – temat 4
```

---

## Szablon notatki

```markdown
# Planowanie Sprintu – RRRR-MM-DD

**Sprint:** [numer]
**Okres:** [daty]

**Powiązane projekty:**
- [lista]

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| [Temat A] | `projekt/ścieżka` | ✅ Ukończone | |
| [Temat B] | `projekt/ścieżka` | 🔄 W testach | Czeka na QA |
| [Temat C] | `projekt/ścieżka` | ➡️ Przeniesione | Brak czasu |

---

## 2. Plany na sprint

### [Nazwa tematu/projektu]

**Projekt:** `[ścieżka/do/projektu]`

**Kontekst i cel:**
[2-3 zdania wyjaśniające DLACZEGO to robimy, ograniczenia biznesowe, terminy klienta. Pomiń dla trywialnych bugfixów.]

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| [Zadanie 1 – konkretnie] | **Adrian** | 2d | - |
| [Zadanie 2] | **Filip** | 3d | Czeka na API od Adriana |
| [Zadanie 3] | **Ania** | 1d | - |

**Szczegóły techniczne** (jeśli istotne):
- Tabela: `CaseDefinition`
- Endpoint: `POST /api/v2/filters`
- Parametr: `indexEnabled=true`

**Decyzje podjęte przy planowaniu:**
- [Decyzja 1 – np. "Użyjemy Lucene zamiast LIKE"]
- [Decyzja 2]
- [Jeśli brak – pomiń sekcję]

**Ryzyka:**
- [Ryzyko 1 – np. "Brak środowiska testowego"]
- [Ryzyko 2]
- [Jeśli brak – pomiń sekcję]

---

### [Kolejny temat]

[powtórz strukturę]

---

## 3. Decyzje architektoniczne (ad-hoc)

[Sekcja dla decyzji które padły podczas planowania, ale dotyczą architektury/technologii]

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| [Decyzja 1] | `projekt/ścieżka` | ✅ Zatwierdzone | [Dlaczego] |
| [Decyzja 2] | `projekt/ścieżka` | 💡 Do weryfikacji | [Dlaczego] |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| [Opis] | `projekt` | Wysoki/Średni/Niski | [Co robimy] | [Osoba] |

---

## 5. Organizacja pracy

- **Urlopy:** [Kto, kiedy]
- **Spotkania:** [Istotne spotkania w sprincie]
- **Przesunięcia:** [Zmiany przypisań między projektami]
```

---

## Zasady formatowania

| Element | Format |
|---------|--------|
| Nazwy systemów | **Bold** (np. **AMODIT**, **Trust Center**) |
| Zmienne, kod, nazwy tabel | `Inline Code` (np. `CaseDefinition`) |
| Osoby | **Pogrubione** w tabelach |
| Projekty | `ścieżka/do/projektu` |

---

## Zasady krytyczne

### 1. Precyzja czasu

- "Zrobiliśmy" → sekcja Status bieżący
- "Będziemy robić" → sekcja Plany na sprint

### 2. Zachowaj szczegóły

Nie streszczaj zbyt mocno. Zachowaj:
- Nazwy tabel, API, parametry
- Estymacje czasowe
- Zależności między zadaniami
- Decyzje podjęte ad-hoc

### 3. Weryfikacja ról

Backendowiec "robi frontend" → opisz jako "przygotowanie API/danych dla frontendu".

### 4. Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

**Zasady oznaczania:**

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia → użyj oznaczenia **"💭 Pomysł Przemka"**
   - W sekcji "Plany na sprint" lub "Uwagi" dodaj: **"💭 Pomysł Przemka - wymaga rozważenia"**

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka → możesz zapisać jako zadanie/plan
   - W takim przypadku dodaj informację: "Pomysł Przemka, potwierdzony przez uczestników"

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne potwierdzenia: "zgadzam się", "dobry pomysł", "tak zrobimy"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia

---

## Checklist przed zapisem

- [ ] Każdy temat ma przypisany projekt
- [ ] Metadane "Powiązane projekty" na początku
- [ ] Status poprzedniego sprintu udokumentowany
- [ ] Zadania z estymacjami i przypisaniami
- [ ] Zależności między zadaniami oznaczone
- [ ] Decyzje ad-hoc zapisane
- [ ] Ryzyka i blokery wyodrębnione
- [ ] Szczegóły techniczne zachowane

---

## Lokalizacja pliku wyjściowego

```
Notatki/Planowanie sprintu/RRRR-MM-DD Planowanie sprintu.md
```

**Uwaga:** Jeśli nazwa transkrypcji zawiera dodatkowe oznaczenia, dodaj je po typie: `RRRR-MM-DD Planowanie sprintu - [oznaczenia].md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Planowanie sprintu/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`

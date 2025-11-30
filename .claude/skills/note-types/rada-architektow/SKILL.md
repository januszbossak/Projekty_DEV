# SKILL: Notatka z Rady Architektów

## Cel

Synteza chaotycznych transkrypcji ze spotkań technicznych w ustrukturyzowane, decyzyjne notatki biznesowe. Rola: **Sekretarz Rady Architektów**.

> **Uwaga:** "Rada Architektów" i "Rada Developerów" to to samo spotkanie.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Tekst zawiera dialog wielu osób, wtrącenia, dygresje i może być nieuporządkowany chronologicznie względem tematów.

---

## Kluczowa zasada: ZACHOWAJ NIUANSE

Notatki służą jako źródło wiedzy do aktualizacji dokumentacji projektowej. **Nie streszczaj zbyt agresywnie.**

Zachowaj:
- **Rozważane alternatywy** – co było dyskutowane, ale odrzucone (i dlaczego)
- **Niuanse techniczne** – konkretne nazwy tabel, API, parametry, flagi
- **Kontrowersje** – jeśli były różne opinie, zapisz je
- **Otwarte pytania** – co nie zostało rozstrzygnięte
- **Zależności** – co od czego zależy

---

## Algorytm analizy (Chain of Thought)

Zanim wygenerujesz notatkę, wykonaj wewnętrznie następujące kroki:

### 1. Grupowanie tematyczne

Zidentyfikuj główne wątki. Pamiętaj, że dyskusja o jednym temacie (np. "Repozytorium") może być przerwana innym wątkiem i wznowiona później. **Scal te fragmenty.**

### 2. Filtracja szumu

Odsiej dygresje, żarty i kwestie organizacyjne (np. "czy mnie słychać", "poczekajmy na Piotra").

**ALE zachowaj** wszystko co może być istotne dla dokumentacji projektu.

### 4. Weryfikacja ról (Sanity Check)

Analizując zadania, sprawdzaj ich sensowność względem roli osoby.

**Zasada:** Jeśli Backendowiec "zajmuje się frontendem", sprawdź czy nie chodzi o przygotowanie API pod frontend. Jeśli nie masz pewności, opisz czynność jako "analizę" lub "wsparcie".

### 5. Ekstrakcja decyzji i alternatyw

Odróżnij:
- **Twarde ustalenia** → sekcja "Decyzja"
- **Propozycje do weryfikacji** → sekcja "Decyzja" z oznaczeniem statusu
- **Odrzucone opcje** → sekcja "Rozważane alternatywy"
- **Nierozstrzygnięte** → sekcja "Punkty otwarte"

---

## Format wyjściowy

### Tytuł

```markdown
# Rada Architektów – RRRR-MM-DD
```

### Metadane (na początku dokumentu)

```markdown
**Tematy:**
- Temat 1
- Temat 2
```

---

## Szablon sekcji (dla każdego wątku)

```markdown
---

## [Numer]. [Tytuł Zagadnienia]

### Kontekst i Problem

[2-4 zdania wyjaśniające DLACZEGO temat został poruszony i jaki problem rozwiązujemy. Tło biznesowe/techniczne. Zachowaj konkretne nazwy, liczby, parametry.]

### Zidentyfikowane Ryzyka

- [Konkretne zagrożenie 1]
- [Konkretne zagrożenie 2]
- [Jeśli brak – wpisz "Nie zidentyfikowano."]

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Opcja A | [Krótki opis] | ✅ Wybrana – [powód] |
| Opcja B | [Krótki opis] | ❌ Odrzucona – [powód] |
| Opcja C | [Krótki opis] | ⏸️ Odroczona – [powód] |

[Jeśli nie było alternatyw – pomiń tabelę, napisz "Jedna propozycja, bez alternatyw."]

### Decyzja

**Status:** ✅ Zatwierdzone / 💡 Propozycja / 🔍 Do weryfikacji / ⏸️ Odroczone

[Co ostatecznie postanowiono. Jeśli decyzja odroczona – napisz dlaczego i co jest potrzebne do podjęcia decyzji.]

**Szczegóły techniczne** (jeśli istotne):
- Nazwa tabeli: `CaseDefinition`
- Parametr: `force=true`
- API: `POST /api/v2/documents`

### Zadania

- **[Imię Nazwisko]:** [Zadanie - bezokolicznik] → termin: [jeśli padł]
- **[Imię Nazwisko]:** [Kolejne zadanie]

### Punkty otwarte

- [Pytanie które nie zostało rozstrzygnięte]
- [Kwestia wymagająca dalszej analizy]
- [Jeśli brak – pomiń sekcję]
```

---

## Zasady (Strict Output Rules)

### Zakazy absolutne

| Zakaz | Przykład błędu |
|-------|----------------|
| **Cytowanie** | ~~"jak powiedział Piotr o 14:23"~~ |
| **Znaczniki czasu** | ~~"[14:23]"~~ |
| **Ściana tekstu** | ~~Jeden długi akapit bez struktury~~ |
| **Pomijanie tematów trudnych** | ~~(pominięcie nierozwiązanego problemu)~~ |
| **Ocenianie pomysłów** | ~~"świetny pomysł Piotra"~~ |
| **Nadmierne streszczanie** | ~~Utrata niuansów technicznych~~ |

### Nakazy

- Każdy temat = osobna sekcja wg szablonu
- Każdy temat ma przypisany projekt
- Narracja przed listą (Kontekst → Ryzyka → Alternatywy → Decyzja → Zadania)
- Zachowaj szczegóły techniczne (nazwy tabel, parametry, API)
- Jeśli decyzja odroczona – napisz dlaczego
- Jeśli były alternatywy – zapisz je z powodami odrzucenia
- **Pomysły Przemysława Sołdackiego** – oznaczaj wyraźnie jako pomysły, chyba że są potwierdzone przez uczestników (patrz sekcja poniżej)

---

## Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

### Zasady oznaczania

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia od innych uczestników → użyj statusu **💡 Propozycja** lub dodaj oznaczenie **"💭 Pomysł Przemka"**
   - W sekcji "Decyzja" napisz: **"💭 Pomysł Przemka - wymaga rozważenia"** lub podobnie
   - W sekcji "Rozważane alternatywy" możesz dodać pomysł Przemka jako opcję do rozważenia

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka (np. "dobry pomysł", "zgadzam się", "tak zrobimy") → możesz użyć statusu **✅ Zatwierdzone**
   - W takim przypadku **nie oznaczaj** jako pomysł, tylko jako decyzję
   - W sekcji "Decyzja" możesz dodać informację: "Pomysł Przemka, potwierdzony przez uczestników"

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne potwierdzenia: "zgadzam się", "dobry pomysł", "tak zrobimy", "właśnie o to chodzi"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia
   - Pytania i dyskusja = pomysł wymagający rozważenia, nie decyzja

4. **Format w sekcji "Decyzja":**
   ```markdown
   **Status:** 💡 Propozycja
   
   💭 Pomysł Przemka: [opis koncepcji] - wymaga rozważenia przez zespół.
   ```
   
   Lub jeśli potwierdzony:
   ```markdown
   **Status:** ✅ Zatwierdzone
   
   [Opis decyzji]. Pomysł Przemka, potwierdzony przez uczestników spotkania.
   ```

**Przykłady:**
- ❌ Błędne: "Ustalono, że..." (gdy Przemek tylko zaproponował)
- ✅ Poprawne: "💭 Pomysł Przemka: wprowadzenie parametru X - wymaga rozważenia"
- ✅ Poprawne: "✅ Zatwierdzone (pomysł Przemka, potwierdzony przez uczestników)"

---

## Checklist przed zapisem

- [ ] Każdy wątek ma osobną sekcję
- [ ] Każdy wątek ma przypisany projekt (lub "do sklasyfikowania")
- [ ] Tytuł zawiera datę w formacie RRRR-MM-DD
- [ ] Metadane "Powiązane projekty" na początku dokumentu
- [ ] Brak cytowań i znaczników czasu
- [ ] Narracja kontekstu przed listami
- [ ] Rozważane alternatywy zapisane (jeśli były)
- [ ] Szczegóły techniczne zachowane (nazwy, parametry)
- [ ] Wszystkie zadania mają przypisaną osobę
- [ ] Tematy nierozwiązane w sekcji "Punkty otwarte"
- [ ] Status decyzji oznaczony (✅/💡/🔍/⏸️)
- [ ] **Pomysły Przemka** - jeśli Przemysław Sołdacki uczestniczył, czy jego pomysły są wyraźnie oznaczone jako pomysły (💭), chyba że są potwierdzone?

---

## Lokalizacja pliku wyjściowego

```
Notatki/Rada architektów/RRRR-MM-DD Rada architektów.md
```

**Uwaga:** Jeśli nazwa transkrypcji zawiera dodatkowe oznaczenia (np. temat, klient), dodaj je po typie: `RRRR-MM-DD Rada architektów - [oznaczenia].md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Rada architektów/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`

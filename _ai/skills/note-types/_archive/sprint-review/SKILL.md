---
name: sprint-review
description: Notatki ze Sprint Review - dostarczone funkcjonalności, feedback, ograniczenia, plany, kontekst biznesowy (ARCHIWUM - używaj spotkanie-projektowe)
---

# SKILL: Notatka ze Sprint Review

## Cel

Przekształcenie surowej transkrypcji ze Sprint Review w klarowną, ustrukturyzowaną notatkę dokumentującą dostarczone funkcjonalności i ich kontekst. Rola: **Asystent dokumentacji sprintów**.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Zawiera prezentacje wielu osób, demo funkcjonalności, dyskusje i feedback.

---

## Kluczowa zasada: ZACHOWAJ NIUANSE

Sprint Review to nie tylko "co zrobiono" – to też:
- **Feedback** od uczestników (uwagi, sugestie)
- **Ograniczenia** obecnego rozwiązania (co NIE działa, co jest workaroundem)
- **Plany na przyszłość** (co będzie rozwijane)
- **Kontekst biznesowy** (dlaczego to było ważne)
- **Szczegóły techniczne** (jak to działa pod spodem)

**Nie pisz "Nie sprecyzowano w transkrypcji"** – zamiast tego wyciągnij informacje z kontekstu dyskusji.

---

## Algorytm analizy

### 1. Identyfikacja funkcjonalności

**Kluczowa zasada:** Traktuj każdą odrębną funkcjonalność jako **osobny temat**, nawet jeśli prezentowane są przez tę samą osobę.

- ❌ Źle: "Prezentacja Piotra" (grupowanie po osobie)
- ✅ Dobrze: "Copilot", "Komunikator", "E-Doręczenia" (osobne tematy)

### 2. Ekstrakcja pełnego kontekstu

Dla każdej funkcjonalności wyodrębnij:
- **Cel biznesowy** – dlaczego to zrobiono
- **Co zaimplementowano** – konkretnie, ze szczegółami
- **Jak to działa** – mechanizm, architektura (jeśli omówiono)
- **Ograniczenia / Known issues** – co nie działa, co jest workaroundem
- **Feedback** – uwagi uczestników
- **Dalsze kroki** – co będzie robione dalej

### 3. Samoocena przed finalizacją

Przed finalizacją porównaj notatkę z transkrypcją – upewnij się, że **żadna istotna informacja nie została pominięta**.

---

## Format wyjściowy

### Tytuł

```markdown
# Sprint Review – RRRR-MM-DD
```

### Metadane (na początku dokumentu)

```markdown
**Sprint:** [numer/nazwa sprintu jeśli padła]
**Okres:** [daty sprintu jeśli padły]
```

---

## Szablon sekcji (dla każdej funkcjonalności)

```markdown
---

## [Numer]. [Nazwa Funkcjonalności/Tematu]

### Cel biznesowy

[Dlaczego ta funkcjonalność była potrzebna. Jaki problem rozwiązuje. 2-3 zdania.]

### Co zaimplementowano

- [Konkretny element 1 – ze szczegółami technicznymi jeśli padły]
- [Konkretny element 2 – np. "endpoint `POST /api/documents` z parametrem `force`"]
- [Konkretny element 3]

### Jak to działa (jeśli omówiono)

[Opis mechanizmu, architektury, przepływu danych. Zachowaj szczegóły techniczne.]

### Ograniczenia / Known issues

- [Co nie działa w tej wersji]
- [Workaroundy które trzeba stosować]
- [Jeśli brak – pomiń sekcję]

### Feedback z demo

- [Uwaga/sugestia uczestnika 1]
- [Uwaga/sugestia uczestnika 2]
- [Jeśli brak – pomiń sekcję]

### Dalsze kroki

- [Co będzie robione w następnym sprincie]
- [Co wymaga dalszych prac]
- [Jeśli brak – pomiń sekcję]
```

---

## Zasady (Strict Output Rules)

### Zakazy absolutne

| Zakaz | Przykład błędu |
|-------|----------------|
| **Cytowanie** | ~~"jak pokazał Piotr"~~ |
| **Grupowanie po osobie** | ~~"Prezentacja Anny"~~ |
| **"Nie sprecyzowano"** | ~~Leniwe pomijanie kontekstu~~ |
| **Nadmierne streszczanie** | ~~Utrata szczegółów technicznych~~ |
| **Halucynacje** | ~~Wymyślanie informacji~~ |

### Nakazy

- Każda funkcjonalność = osobna sekcja
- Zachowaj szczegóły techniczne (nazwy, parametry, API)
- Zachowaj feedback i uwagi uczestników
- Zachowaj ograniczenia i known issues
- Wyciągaj kontekst z dyskusji, nie pisz "nie sprecyzowano"
- **Pomysły Przemysława Sołdackiego** – oznaczaj wyraźnie jako pomysły, chyba że są potwierdzone przez uczestników (patrz sekcja poniżej)

---

## Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

### Zasady oznaczania

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia → użyj oznaczenia **"💭 Pomysł Przemka"**
   - W sekcji "Dalsze kroki" lub "Uwagi" dodaj: **"💭 Pomysł Przemka - wymaga rozważenia"**

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka → możesz zapisać jako decyzję/plan
   - W takim przypadku dodaj informację: "Pomysł Przemka, potwierdzony przez uczestników"

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne potwierdzenia: "zgadzam się", "dobry pomysł", "tak zrobimy"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia

---

## Obsługa niejasności

Jeśli transkrypcja zawiera niejasne nazwy:

1. **Nie zgaduj** nazw własnych
2. **Opisz funkcjonalność** – co robi, jak działa
3. **Oznacz do wyjaśnienia:** "[nazwa do weryfikacji]"

---

## Checklist przed zapisem

- [ ] Każda funkcjonalność ma osobną sekcję
- [ ] Cel biznesowy opisany (nie "nie sprecyzowano")
- [ ] Szczegóły techniczne zachowane
- [ ] Ograniczenia/known issues zapisane (jeśli były)
- [ ] Feedback z demo zapisany (jeśli był)
- [ ] Dalsze kroki określone (jeśli padły)
- [ ] Brak cytowań i znaczników czasowych

---

## Lokalizacja pliku wyjściowego

```
Notatki/Sprint review/RRRR-MM-DD Sprint review.md
```

**Uwaga:** Jeśli nazwa transkrypcji zawiera dodatkowe oznaczenia, dodaj je po typie: `RRRR-MM-DD Sprint review - [oznaczenia].md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Sprint review/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`

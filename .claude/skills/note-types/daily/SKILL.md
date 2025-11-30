# SKILL: Notatka z Daily

## Cel

Tworzenie zwięzłej, operacyjnej notatki ze spotkań Daily, dokumentującej status prac, nowe zgłoszenia do backlogu i tematy organizacyjne. Rola: **Sekretarz operacyjny Daily**.

**WAŻNE:** Ten skill służy **TYLKO** do generowania notatki z transkrypcji. **NIE przypisuj projektów** - to jest osobny krok wykonywany przez workflow "Przetwórz notatkę" lub agenta `project-mapper`. Twoja rola: zachować wszystkie informacje z transkrypcji, szczególnie szczegóły techniczne które pomogą w późniejszym mapowaniu.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Zawiera krótkie statusy od uczestników, omówienie nowych zgłoszeń i czasami tematy organizacyjne.

---

## Kluczowa zasada: ZWIĘZŁOŚĆ I OPERACYJNOŚĆ

Daily to codzienne, krótkie spotkania operacyjne. **Nie rozwijaj zbyt szczegółowo** – skup się na:
- **Statusie prac** – co kto robi, czy są blokery
- **Nowych zgłoszeniach** – co napłynęło do backlogu, jak zostało omówione
- **Tematach organizacyjnych** – jeśli były (urlopy, zastępstwa, spotkania)

**Zachowaj:**
- Krótkie, konkretne informacje
- Blokery i ryzyka (jeśli padły)
- Decyzje ad-hoc (jeśli były – rzadko)
- Szczegóły techniczne tylko jeśli istotne dla backlogu

---

## Struktura Daily

Daily ma często **dwie części**:

### Część 1: Status update (wszyscy uczestnicy)
- Każdy mówi co robi
- Czy są blokery
- Co planuje zrobić

### Część 2: Omówienie backlogu (węższe grono)
- Nowe zgłoszenia napływające do backlogu
- Omówienie priorytetów
- Decyzje o przypisaniu

### Część 3: Tematy organizacyjne (opcjonalnie)
- Urlopy, zastępstwa
- Spotkania, zmiany w harmonogramie
- Inne kwestie organizacyjne

---

## Algorytm analizy

### Krok 1: Identyfikacja części

Rozpoznaj w transkrypcji:
- **Część 1:** Status update od uczestników
- **Część 2:** Omówienie nowych zgłoszeń do backlogu
- **Część 3:** Tematy organizacyjne (jeśli były)

### Krok 2: Ekstrakcja informacji

**Dla statusów:**
- Co robi osoba
- Czy są blokery
- Co planuje zrobić dalej

**Dla nowych zgłoszeń:**
- Opis zgłoszenia
- Priorytet (jeśli padł)
- Przypisanie (jeśli padło)
- Kontekst biznesowy (jeśli padł)
- Techniczne szczegóły (jeśli padły)

**Dla tematów organizacyjnych:**
- Co zostało ustalone
- Kogo dotyczy
- Terminy (jeśli padły)

---

## Format wyjściowy

### Tytuł

```markdown
# Daily – RRRR-MM-DD
```

---

## Szablon notatki

```markdown
# Daily – RRRR-MM-DD

## 1. Status update

### [Imię Nazwisko]

**Co robię:**
- [Zadanie 1 – konkretnie]
- [Zadanie 2 – konkretnie]

**Blokery:**
- [Bloker 1 – jeśli jest]
- [Jeśli brak – pomiń sekcję]

**Plan na dziś/jutro:**
- [Co planuje zrobić]

---

### [Kolejna osoba]

[powtórz strukturę]

---

## 2. Nowe zgłoszenia do backlogu

### [Numer]. [Tytuł zgłoszenia]

**Opis:**
[Krótki opis zgłoszenia – co jest potrzebne, jaki problem rozwiązuje]

**Kontekst biznesowy** (jeśli padł):
[Dlaczego to jest ważne, termin klienta, priorytet biznesowy]

**Priorytet:** [Wysoki / Średni / Niski] lub [do ustalenia]

**Przypisanie:** [Osoba] lub [do przypisania]

**Uwagi:**
- [Uwaga 1]
- [Uwaga 2]
- [Jeśli brak – pomiń sekcję]

---

### [Kolejne zgłoszenie]

[powtórz strukturę]

---

## 3. Tematy organizacyjne

### [Tytuł tematu]

**Kategoria:** [Urlopy / Zastępstwa / Spotkania / Inne]

**Ustalenie:**
[Co zostało ustalone]

**Kogo dotyczy:**
- [Osoba 1] – [szczegóły]
- [Osoba 2] – [szczegóły]

**Termin:** [data] lub [do ustalenia]

[Jeśli brak tematów organizacyjnych – pomiń sekcję]

---

## 4. Decyzje ad-hoc (jeśli były)

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| [Decyzja 1] | [1-2 zdania] | ✅ Zatwierdzone | [Dlaczego] |
| [Decyzja 2] | [1-2 zdania] | 💡 Do weryfikacji | [Dlaczego] |

[Jeśli brak decyzji – pomiń sekcję]
```

---

## Zasady (Strict Output Rules)

### Zakazy absolutne

| Zakaz | Przykład błędu |
|-------|----------------|
| **Cytowanie** | ~~"jak powiedział Piotr"~~ |
| **Nadmierne rozwijanie** | ~~Długie opisy dla prostych statusów~~ |
| **Halucynacje** | ~~Wymyślanie szczegółów których nie ma~~ |
| **Mieszanie części** | ~~Status update z omówieniem backlogu~~ |

### Nakazy

- Każda osoba w status update = osobna sekcja
- Każde zgłoszenie = osobna sekcja ze wszystkimi szczegółami
- Zachowaj zwięzłość – Daily to nie Rada Architektów
- Zachowaj blokery i ryzyka (jeśli padły)
- **Zachowaj wszystkie szczegóły techniczne** - nazwy modułów, funkcji, komponentów, API, tabel - pomogą w późniejszym mapowaniu na projekty
- Tematy organizacyjne wyodrębnij osobno

---

## Wiedza stała: Role w zespole

| Rola | Osoby |
|------|-------|
| **Architekt/Fullstack** | Piotr |
| **Backend/Fullstack** | Adrian, Ania, Marek, Łukasz Brocki, Mateusz, Mariusz |
| **Frontend** | Przemek Rogaś, Filip |
| **Management/Analiza** | Janusz, Kamil, Damian, Łukasz Bott |
| **QA/Testy** | Barbara, Oktawia, Patrycja |
| **DevOps** | Michał Zwierzchowski |

> **Uwaga:** Jeśli transkrypcja definiuje rolę inaczej – trzymaj się transkrypcji.

---

## Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

### Zasady oznaczania

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia → użyj oznaczenia **"💭 Pomysł Przemka"**
   - W sekcji "Uwagi" lub "Decyzje ad-hoc" dodaj: **"💭 Pomysł Przemka - wymaga rozważenia"**

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka → możesz zapisać jako decyzję/plan
   - W takim przypadku dodaj informację: "Pomysł Przemka, potwierdzony przez uczestników"

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne potwierdzenia: "zgadzam się", "dobry pomysł", "tak zrobimy"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia

---

## Checklist przed zapisem

- [ ] Status update od każdego uczestnika (jeśli był)
- [ ] Wszystkie zgłoszenia zapisane z pełnymi szczegółami
- [ ] Blokery zapisane (jeśli były)
- [ ] Tematy organizacyjne wyodrębnione (jeśli były)
- [ ] Decyzje ad-hoc zapisane (jeśli były)
- [ ] Zwięzłość zachowana – nie rozwijaj zbyt szczegółowo
- [ ] Brak cytowań i znaczników czasowych
- [ ] **Pomysły Przemka** - jeśli Przemysław Sołdacki uczestniczył, czy jego pomysły są wyraźnie oznaczone jako pomysły (💭), chyba że są potwierdzone?
- [ ] **Zachowanie szczegółów technicznych** - nazwy modułów, funkcji, tabel, API - wszystko co może pomóc w późniejszym mapowaniu na projekty

---

## Lokalizacja pliku wyjściowego

```
Notatki/Daily/RRRR-MM-DD Daily.md
```

**Uwaga:** Jeśli nazwa transkrypcji zawiera dodatkowe oznaczenia, dodaj je po typie: `RRRR-MM-DD Daily - [oznaczenia].md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Daily/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`


# SKILL: Czyszczenie transkrypcji ASR

## Cel

Transformacja surowego outputu ASR (Automatic Speech Recognition) w czysty, czytelny zapis dialogu. Zachowujemy 100% treści merytorycznej, usuwamy szum komunikacyjny i błędy rozpoznawania mowy.

---

## Zasoby obowiązkowe

**ZAWSZE przeczytaj PRZED przetwarzaniem:**

1. **Słownik domenowy:** `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`
   - Mapowania błędnych zapisów ASR → poprawne terminy
   - Nazwy produktów, technologii, akronimów

---

## Kluczowa umiejętność: Korekta fonetyczna

ASR często zapisuje słowa brzmiące podobnie, ale bezsensowne w kontekście. Musisz działać jak "inteligentny dekoder":

### Algorytm korekty

1. **Zidentyfikuj domenę** – szybki skan tekstu (IT, HR, biznes, technologia AMODIT)
2. **Wykryj halucynacje ASR** – gramatycznie poprawne, ale semantycznie absurdalne frazy
3. **Zastosuj korektę** – zamień na termin techniczny/branżowy o podobnym brzmieniu
4. **Test kontekstu** – czy poprawiona wersja ma sens w kontekście R&D AMODIT?

### Przykłady korekt

| ASR (błędnie) | Poprawnie | Kontekst |
|---------------|-----------|----------|
| kopalnie lot | Copilot | Asystent AI |
| modlicie, a modlit | AMODIT | Nazwa systemu |
| re aktywne | Reactowe | Framework frontendowy |
| bekendu | backendu | Warstwa serwerowa |
| i o r wa, jura | JRWA | Jednolity Rzeczowy Wykaz Akt |
| em wi pi | MVP | Minimum Viable Product |
| komar hab | Comarch Hub | Integracja z systemem |
| krzew, ksyw | KSeF | Krajowy System e-Faktur |

### Zasada niepewności

Jeśli nie możesz jednoznacznie określić poprawnej formy:
- **NIE zgaduj** – zostaw oryginalny tekst
- **Oznacz do weryfikacji** – dodaj komentarz `[?]` po fragmencie
- **Zgłoś do słownika** – zanotuj nowy błąd ASR do dodania

---

## Reguły redukcji szumu

### Usuń całkowicie

**Wypełniacze (fillers):**
- "yyyy", "eee", "eeee"
- "słuchajcie", "że tak powiem", "w zasadzie"
- "jakby", "no", "generalnie", "w sumie"
- "znaczy", "wiesz", "rozumiesz"

**Powtórzenia:**
- "to jest, to jest system" → "to jest system"
- "musimy, musimy to zrobić" → "musimy to zrobić"

**Technikalia spotkania:**
- "czy mnie słychać?", "słychać mnie?"
- "włączam nagrywanie", "poczekajmy na..."
- "możesz udostępnić ekran?", "widzicie?"
- "sorry, miałem mute"

**Znaczniki czasowe w wypowiedziach:**
- Usuń timestampy typu "0:03", "1:14" z linii mówców
- Zachowaj tylko datę spotkania na początku dokumentu

### Zachowaj bezwzględnie (100%)

- Każdy fakt, liczbę, nazwę
- Każdy argument i opinię
- Każdą decyzję i ustalenie
- Każde zadanie i przypisanie osoby
- Chronologię wypowiedzi

---

## Wykrywanie luk w transkrypcji

Jeśli znaczniki czasowe skaczą znacząco (np. 5:00 → 12:00 bez treści), oznacz:

```markdown
[BRAKUJĄCY FRAGMENT TRANSKRYPCJI: 5:00 - 12:00]
```

---

## Format wyjściowy

```markdown
**Data spotkania:** DD miesiąc RRRR, GG:MM

---

**[Imię Nazwisko]:** Treść wypowiedzi w poprawnych, pełnych zdaniach. Zachowana interpunkcja i gramatyka.

**[Imię Nazwisko]:** Kolejna wypowiedź. Może zawierać wiele zdań jeśli mówca kontynuuje myśl.

**[Imię Nazwisko]:** Odpowiedź lub nowy wątek.
```

### Zasady formatowania

- **Mówca** zawsze pogrubiony: `**[Imię Nazwisko]:**`
- **Jeden akapit** = jedna ciągła wypowiedź mówcy
- **Nowa linia** = zmiana mówcy lub wyraźna pauza
- **Brak numeracji** wypowiedzi
- **Brak timestampów** przy wypowiedziach

---

## Gramatyka i interpunkcja

Surowa transkrypcja to "strumień słów". Twoje zadanie:

1. **Podziel na zdania** – dodaj kropki, przecinki, znaki zapytania
2. **Popraw gramatykę** – bez zmiany sensu
3. **Zachowaj styl mówiony** – nie przekształcaj w formalny tekst pisany
4. **Nie dodawaj treści** – tylko formatuj to co jest

### Przykład transformacji

**Przed (surowe):**
```
no i teraz patrzcie mamy ten problem z tym filtrem że on nie działa jak powinien znaczy działa ale nie tak jak użytkownik by chciał
```

**Po (oczyszczone):**
```
Mamy problem z tym filtrem – nie działa jak powinien. Znaczy, działa, ale nie tak jak użytkownik by chciał.
```

---

## Czego NIE robić

1. **NIE streszczaj** – czyść, nie kondensuj
2. **NIE interpretuj** – edytuj, nie komentuj
3. **NIE dodawaj** – żadnych własnych treści
4. **NIE oceniaj** – neutralny zapis
5. **NIE zmieniaj kolejności** – chronologia jest święta
6. **NIE usuwaj kontrowersji** – nawet jeśli ktoś się myli, zapisz co powiedział

---

## Strategia dla dużych plików (>800 linii)

Jeśli surowa transkrypcja ma powyżej ~800 linii, **NIE przetwarzaj całego pliku na raz**. Wielokrotne próby zapisu dużego pliku marnują tokeny i mogą kończyć się błędami.

### Podejście: Podział na części

**Algorytm:**

1. **Sprawdź rozmiar** pliku surowego (polecenie `wc -l`)
2. **Jeśli > 800 linii**, podziel na części po ~400 linii
3. **Ważne:** Nie urywaj w połowie wypowiedzi – cała wypowiedź mówcy musi być w jednej części
4. **Zapisz każdą część osobno** z dopiskiem w nazwie:
   - `{data} {typ} - transkrypcja - część 1.md`
   - `{data} {typ} - transkrypcja - część 2.md`
   - `{data} {typ} - transkrypcja - część 3.md`
   - itd.

**Przykład:**

```markdown
Plik surowy: 2025-10-09 Rada developerów.md (1131 linii)

Część 1: linie 1-400 (zakończ na pełnej wypowiedzi)
Część 2: linie 401-800 (zakończ na pełnej wypowiedzi)
Część 3: linie 801-1131 (reszta)
```

**W nagłówku każdej części oprócz pierwszej dodaj:** `część 2`, `część 3`, etc.

```markdown
**Data spotkania:** 9 października 2025, 08:00 - część 2
```

**W rejestrze zaktualizuj:**
```markdown
| 2025-10-09 | Rada architektów | `2025-10-09 Rada developerów.md` | `2025-10-09 Rada developerów - transkrypcja - część 1-4.md` |
```

### Zalety tego podejścia:

✅ Unika wielokrotnego przetwarzania tego samego materiału  
✅ Oszczędza tokeny (jedno przetworzenie zamiast 5+ prób)  
✅ Każda część zapisuje się niezawodnie  
✅ Łatwo znaleźć konkretny fragment w odpowiedniej części  
✅ Można równolegle przetwarzać różne części w przyszłości

### Kiedy NIE dzielić:

- Pliki < 800 linii – przetwarzaj normalnie jednym plikiem
- Bardzo krótkie spotkania (< 500 linii) – bez podziału

---

## Checklist przed zapisem

- [ ] Słownik domenowy został przeczytany
- [ ] Żadna informacja merytoryczna nie została utracona
- [ ] Nazwy produktów pisane poprawnie (AMODIT, SignApp, KSeF, React, etc.)
- [ ] Chronologia mówców zachowana
- [ ] Format wyjściowy zgodny ze standardem
- [ ] Luki w transkrypcji oznaczone (jeśli występują)
- [ ] Nowe błędy ASR zanotowane do aktualizacji słownika

## Checklist po zapisie

- [ ] Oczyszczony plik zapisany w `Notatki/Transkrypcje/oczyszczone/`
- [ ] Surowy plik przeniesiony do `Notatki/Transkrypcje/surowe - archiwum/` (zachowano oryginalną nazwę)


---

## Aktualizacja słownika

Jeśli podczas przetwarzania znajdziesz nowy, powtarzający się błąd ASR:

1. Zanotuj parę: `błędny zapis → poprawna forma`
2. Po zakończeniu przetwarzania, dodaj do słownika domenowego
3. Uwzględnij kontekst użycia

---

## Powiązane zasoby

- **Słownik domenowy:** `Notatki/Transkrypcje/Słownik Domenowy/Słownik Domenowy i Korekta Fonetyczna.md`
- **Katalog surowych:** `Notatki/Transkrypcje/surowe/`
- **Katalog oczyszczonych:** `Notatki/Transkrypcje/oczyszczone/`

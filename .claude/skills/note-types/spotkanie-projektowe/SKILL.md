# SKILL: Notatka ze Spotkania Projektowego

## Cel

Tworzenie kompletnej notatki projektowej ze spotkań zespołu, dokumentującej funkcjonalności, decyzje, alternatywy i otwarte kwestie. Rola: **Analityk projektowy specjalizujący się w systemie AMODIT**.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Zawiera dyskusje o funkcjonalnościach, decyzje projektowe, problemy do rozwiązania.

---

## Kluczowa zasada: ZACHOWAJ PEŁNY KONTEKST

Spotkania projektowe to główne źródło wiedzy o funkcjonalnościach. **Nie streszczaj zbyt agresywnie.**

Zachowaj:
- **Rozważane alternatywy** – co dyskutowano, co odrzucono i dlaczego
- **Niuanse techniczne** – nazwy tabel, parametry, formaty danych
- **Kontrowersje** – różne opinie, argumenty za i przeciw
- **Otwarte pytania** – co nie zostało rozstrzygnięte
- **Zależności** – co od czego zależy
- **Ograniczenia** – co NIE będzie robione i dlaczego

---

## Wiedza stała: Nomenklatura systemu AMODIT

Precyzyjnie kategoryzuj zagadnienia:

### Edytor Procesów

| Komponent | Opis |
|-----------|------|
| **Edytor Diagramu** | Wizualne tworzenie diagramów procesów, etapy, akcje, połączenia |
| **Edytor Formularza** | Projektowanie formularzy, pola, walidacje |
| **Edytor Reguł** | Skrypty, logika biznesowa, reguły |

### Inne moduły

- **Moduł raportowy** – raporty, filtry, dashboardy
- **Repozytorium** – zarządzanie plikami (DMS)
- **Trust Center** – podpisy elektroniczne
- **Ustawienia systemowe** – konfiguracja, joby, integracje
- **Copilot / AI** – funkcje AI, baza wiedzy

---

## Algorytm analizy

### Krok 1: Identyfikacja wątków

Przeskanuj transkrypcję i zgrupuj wypowiedzi według funkcjonalności/tematów.

### Krok 2: Kategoryzacja komponentu

Przyporządkuj do właściwego komponentu systemu AMODIT.

> **Uwaga:** Jeśli nie wiesz o czym mowa – oznacz "[do wyjaśnienia]". Lepiej zapytać niż błędnie sklasyfikować.

### Krok 3: Ekstrakcja pełnego kontekstu

Dla każdej funkcjonalności wyodrębnij:
- Cel biznesowy i techniczny
- Problem do rozwiązania
- Rozważane alternatywy (z powodami odrzucenia/wyboru)
- Podjętą decyzję i jej status
- Szczegóły techniczne (nazwy, parametry, formaty)
- Punkty otwarte

### Krok 4: Podział na MVP

Jeśli dyskutowano priorytetyzację – zaproponuj podział na pakiety prac.

### Krok 5: Weryfikacja końcowa

**WAŻNE:** Przed finalizacją dokonaj powtórnego przeglądu transkrypcji. Upewnij się, że wszystkie wątki zostały prawidłowo przedstawione.

---

## Format wyjściowy

### Tytuł

```markdown
# Notatka projektowa – RRRR-MM-DD – [Temat główny]
```

### Metadane (na początku dokumentu)

```markdown
**Data:** RRRR-MM-DD
**Temat główny:** [np. "Edytor Diagramu – połączenia i etapy"]
```

---

## Szablon sekcji (dla każdej funkcjonalności)

```markdown
---

## [Numer]. [Nazwa Funkcjonalności]

**Komponent:** [Edytor Diagramu / Edytor Formularza / Edytor Reguł / inny]

### Cel i problem

[2-3 zdania: Jaki problem rozwiązujemy? Dlaczego to ważne? Kontekst biznesowy.]

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A | [Opis podejścia] | ✅ Wybrana – [powód] |
| Opcja B | [Opis podejścia] | ❌ Odrzucona – [powód] |
| Opcja C | [Opis podejścia] | ⏸️ Odroczona – [powód] |

[Jeśli była jedna propozycja – napisz "Jedna propozycja, bez alternatyw."]

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone / 💡 Propozycja / 🔍 Do weryfikacji / ⏸️ Odroczone

[Opis podjętej decyzji. Kluczowe aspekty techniczne i projektowe.]

**Szczegóły techniczne:**
- Format danych: [np. "XML z atrybutem `waypoints`"]
- Tabela: [np. `ProcessDefinition`]
- API: [np. `PUT /api/diagram/connections`]

### Ograniczenia / Poza zakresem

- [Co świadomie NIE będzie robione]
- [Ograniczenia techniczne]
- [Jeśli brak – pomiń sekcję]

### Punkty otwarte

- [Pytanie do rozstrzygnięcia]
- [Kwestia wymagająca analizy]
- [Jeśli brak – pomiń sekcję]
```

---

## Sekcje końcowe

```markdown
---

## Propozycja podziału na pakiety prac (MVP)

[Jeśli dyskutowano priorytetyzację]

### MVP 1: [Nazwa pakietu]

**Cel:** [Cel tego MVP]
**Zakres:** Funkcjonalności [1, 2, 3]
**Planowany termin:** [jeśli padł]

### MVP 2: [Nazwa pakietu]

**Cel:** [Cel tego MVP]
**Zakres:** Funkcjonalności [4, 5]

---

## Punkty do dalszej dyskusji (globalne)

- [Temat wymagający osobnego spotkania]
- [Kwestia wymagająca decyzji zarządu/klienta]
```

---

## Zasady krytyczne

### 1. Ignoruj autorów wypowiedzi

Skup się na **ustaleniach, problemach i decyzjach**, nie na tym kto co powiedział. Notatka jest bezosobowa.

### 2. Zachowaj alternatywy

Każda dyskutowana opcja ma wartość – nawet odrzucona. Zapisz CO odrzucono i DLACZEGO.

### 3. Zachowaj szczegóły techniczne

Nie streszczaj nazw tabel, parametrów, formatów danych. To kluczowe dla implementacji.

### 4. Oznaczaj status decyzji

- ✅ **Zatwierdzone** – decyzja ostateczna
- 💡 **Propozycja** – do dalszej dyskusji
- 🔍 **Do weryfikacji** – wymaga testów/analizy
- ⏸️ **Odroczone** – odłożone na później

### 5. Kategoryzuj precyzyjnie

Każdy temat musi być przyporządkowany do projektu i komponentu systemu.

### 6. Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

**Zasady oznaczania:**

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia od innych uczestników → użyj statusu **💡 Propozycja** lub dodaj oznaczenie **"💭 Pomysł Przemka"**
   - W sekcji "Decyzja / Sposób realizacji" napisz: **"💭 Pomysł Przemka - wymaga rozważenia"** lub podobnie
   - W sekcji "Rozważane alternatywy" możesz dodać pomysł Przemka jako opcję do rozważenia

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka (np. "dobry pomysł", "zgadzam się", "tak zrobimy") → możesz użyć statusu **✅ Zatwierdzone**
   - W takim przypadku **nie oznaczaj** jako pomysł, tylko jako decyzję
   - W sekcji "Decyzja / Sposób realizacji" możesz dodać informację: "Pomysł Przemka, potwierdzony przez uczestników"

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne potwierdzenia: "zgadzam się", "dobry pomysł", "tak zrobimy", "właśnie o to chodzi"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia
   - Pytania i dyskusja = pomysł wymagający rozważenia, nie decyzja

4. **Format w sekcji "Decyzja / Sposób realizacji":**
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
- ✅ Poprawne: "💭 Pomysł Przemka: wprowadzenie funkcjonalności X - wymaga rozważenia"
- ✅ Poprawne: "✅ Zatwierdzone (pomysł Przemka, potwierdzony przez uczestników)"

---

## Checklist przed zapisem

- [ ] Każda funkcjonalność ma osobną sekcję
- [ ] Każda funkcjonalność ma przypisany projekt i komponent
- [ ] Metadane "Powiązane projekty" na początku dokumentu
- [ ] Rozważane alternatywy zapisane (jeśli były)
- [ ] Szczegóły techniczne zachowane (nazwy, parametry, formaty)
- [ ] Status decyzji oznaczony (✅/💡/🔍/⏸️)
- [ ] Punkty otwarte wyodrębnione
- [ ] MVP zaproponowane (jeśli dyskutowano priorytetyzację)
- [ ] Powtórna weryfikacja z transkrypcją wykonana
- [ ] **Pomysły Przemka** - jeśli Przemysław Sołdacki uczestniczył, czy jego pomysły są wyraźnie oznaczone jako pomysły (💭), chyba że są potwierdzone?

---

## Lokalizacja pliku wyjściowego

```
Notatki/Spotkania projektowe/RRRR-MM-DD Notatka projektowa - [temat].md
```

**Wyciąganie tematu:**
- Jeśli nazwa transkrypcji zawiera dodatkowe informacje (np. "Komunikator (AMODIT Talk)", "Edytor procesów", "Repozytorium", "Design"), użyj ich jako tematu
- Usuń z tematu: "- transkrypcja", "- część 1-4", "-gemini" i podobne sufixy techniczne
- Jeśli typ spotkania to "Design", użyj nazwy "Spotkanie projektowe" z tematem "Design"

Przykłady:
- Transkrypcja: `2025-10-14 Design - transkrypcja - część 1-4.md` → Notatka: `2025-10-14 Spotkanie projektowe - Design.md`
- Transkrypcja: `2025-08-12 Komunikator (AMODIT Talk) - transkrypcja.md` → Notatka: `2025-08-12 Notatka projektowa - Komunikator (AMODIT Talk).md`
- Transkrypcja: `2025-07-30 Repozytorium.md` → Notatka: `2025-07-30 Notatka projektowa - Repozytorium.md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Spotkania projektowe/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`
- **Struktura Project Canvas:** `projekty/ZASADY.md`

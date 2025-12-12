# SKILL: Notatka ze Spotkania (Zunifikowany)

## Cel

Tworzenie kompletnej notatki ze spotkań zespołu, dokumentującej funkcjonalności, decyzje, alternatywy i otwarte kwestie. Rola: **Analityk projektowy specjalizujący się w systemie AMODIT**.

**Ten skill obsługuje wszystkie typy spotkań "substantywnych":**
- Rada Architektów / Rada Developerów
- Design / Spotkania projektowe
- Sprint Review
- Planowanie Sprintu
- Przegląd projektów / wycen
- Inne spotkania projektowe

> **Wyjątki:** Daily → osobny skill `daily`. Organizacyjne → osobny skill `organizacyjne`.

---

## Dane wejściowe

Oczyszczona transkrypcja z Microsoft Teams (output z `transcript-cleaning` skill). Zawiera dyskusje o funkcjonalnościach, decyzje projektowe, problemy do rozwiązania, demo, planowanie.

---

## Kluczowa zasada: ZACHOWAJ PEŁNY KONTEKST

Spotkania to główne źródło wiedzy o projektach. **Nie streszczaj zbyt agresywnie.**

Zachowaj:
- **Rozważane alternatywy** – co dyskutowano, co odrzucono i dlaczego
- **Niuanse techniczne** – nazwy tabel, parametry, formaty danych, API
- **Kontrowersje** – różne opinie, argumenty za i przeciw
- **Otwarte pytania** – co nie zostało rozstrzygnięte
- **Zależności** – co od czego zależy
- **Ograniczenia** – co NIE będzie robione i dlaczego
- **Feedback** – uwagi uczestników (szczególnie przy Sprint Review)
- **Ryzyka** – zidentyfikowane zagrożenia (szczególnie przy Planowaniu)

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

- **Moduł raportowy** – raporty, filtry, dashboardy, Gantt, Kanban, Pivot
- **Repozytorium** – zarządzanie plikami (DMS)
- **Trust Center** – podpisy elektroniczne, blockchain
- **Ustawienia systemowe** – konfiguracja, joby, integracje
- **Copilot / AI** – funkcje AI, baza wiedzy, OCR
- **Silnik reguł** – logika biznesowa, funkcje

---

## Algorytm analizy

### Krok 1: Identyfikacja wątków

Przeskanuj transkrypcję i zgrupuj wypowiedzi według funkcjonalności/tematów.
Pamiętaj, że dyskusja o jednym temacie może być przerwana i wznowiona później – **scal te fragmenty**.

### Krok 2: Kategoryzacja komponentu

Przyporządkuj do właściwego komponentu systemu AMODIT.

> **Uwaga:** Jeśli nie wiesz o czym mowa – oznacz "[do wyjaśnienia]". Lepiej zapytać niż błędnie sklasyfikować.

### Krok 3: Ekstrakcja pełnego kontekstu

Dla każdej funkcjonalności/tematu wyodrębnij:
- Cel biznesowy i techniczny
- Problem do rozwiązania
- Rozważane alternatywy (z powodami odrzucenia/wyboru)
- Podjętą decyzję i jej status
- Szczegóły techniczne (nazwy, parametry, formaty)
- Ryzyka i ograniczenia
- Punkty otwarte

### Krok 4: Weryfikacja końcowa

**WAŻNE:** Przed finalizacją dokonaj powtórnego przeglądu transkrypcji. Upewnij się, że wszystkie wątki zostały prawidłowo przedstawione.

---

## Format wyjściowy

### Tytuł

Format zależny od typu spotkania (rozpoznanego z nazwy transkrypcji):

```markdown
# Rada Architektów – RRRR-MM-DD
# Sprint Review – RRRR-MM-DD
# Planowanie Sprintu – RRRR-MM-DD
# Notatka projektowa – RRRR-MM-DD – [Temat główny]
```

### Metadane (na początku dokumentu)

```markdown
**Data:** RRRR-MM-DD
**Typ:** [Rada Architektów / Sprint Review / Planowanie / Spotkanie projektowe]
**Temat główny:** [np. "Repozytorium plików", "Moduł raportowy"]
```

---

## Szablon sekcji (dla każdego wątku/funkcjonalności)

```markdown
---

## [Numer]. [Nazwa Tematu/Funkcjonalności]

**Komponent:** [np. Edytor Diagramu / Moduł raportowy / Trust Center / inny]

### Kontekst i cel

[2-4 zdania: Jaki problem rozwiązujemy? Dlaczego to ważne? Kontekst biznesowy/techniczny. Zachowaj konkretne nazwy, liczby, parametry.]

### Zidentyfikowane ryzyka

- [Konkretne zagrożenie 1]
- [Konkretne zagrożenie 2]
- [Jeśli brak – pomiń sekcję]

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A | [Opis podejścia] | ✅ Wybrana – [powód] |
| Opcja B | [Opis podejścia] | ❌ Odrzucona – [powód] |
| Opcja C | [Opis podejścia] | ⏸️ Odroczona – [powód] |

[Jeśli była jedna propozycja – napisz "Jedna propozycja, bez alternatyw."]
[Jeśli nie było dyskusji o alternatywach – pomiń sekcję]

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone / 💡 Propozycja / 🔍 Do weryfikacji / ⏸️ Odroczone

[Co ostatecznie postanowiono. Kluczowe aspekty techniczne i projektowe.]

**Szczegóły techniczne** (jeśli istotne):
- Format danych: [np. "XML z atrybutem `waypoints`"]
- Tabela: [np. `CaseDefinition`]
- API: [np. `PUT /api/diagram/connections`]
- Parametr: [np. `force=true`, `limit=500`]

### Ograniczenia / Poza zakresem

- [Co świadomie NIE będzie robione]
- [Ograniczenia techniczne]
- [Jeśli brak – pomiń sekcję]

### Feedback / Uwagi uczestników

- [Uwaga/sugestia uczestnika 1]
- [Uwaga/sugestia uczestnika 2]
- [Szczególnie istotne przy Sprint Review - jeśli brak, pomiń sekcję]

### Zadania / Dalsze kroki

- **[Imię Nazwisko]:** [Zadanie - bezokolicznik] → termin: [jeśli padł]
- **[Imię Nazwisko]:** [Kolejne zadanie]
- [Jeśli brak – pomiń sekcję]

### Punkty otwarte

- [Pytanie które nie zostało rozstrzygnięte]
- [Kwestia wymagająca dalszej analizy]
- [Jeśli brak – pomiń sekcję]
```

---

## Sekcje dodatkowe (używaj jeśli potrzebne)

### Dla Planowania Sprintu - Status poprzedniego sprintu

```markdown
## Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| [Temat A] | ✅ Ukończone | |
| [Temat B] | 🔄 W testach | Czeka na QA |
| [Temat C] | ➡️ Przeniesione | Brak czasu |
```

### Dla Sprint Review - Podsumowanie demo

```markdown
## Podsumowanie demo

| Funkcjonalność | Prezentował | Status |
|----------------|-------------|--------|
| [Feature 1] | [Osoba] | ✅ Gotowe |
| [Feature 2] | [Osoba] | 🔄 W trakcie |
```

---

## Zasady (Strict Output Rules)

### Zakazy absolutne

| Zakaz | Przykład błędu |
|-------|----------------|
| **Cytowanie** | ~~"jak powiedział Piotr o 14:23"~~ |
| **Znaczniki czasu** | ~~"[14:23]"~~ |
| **Ściana tekstu** | ~~Jeden długi akapit bez struktury~~ |
| **Pomijanie tematów** | ~~(pominięcie nierozwiązanego problemu)~~ |
| **Ocenianie pomysłów** | ~~"świetny pomysł Piotra"~~ |
| **Nadmierne streszczanie** | ~~Utrata niuansów technicznych~~ |
| **Halucynacje** | ~~Wymyślanie szczegółów których nie było~~ |
| **"Nie sprecyzowano"** | ~~Leniwe pomijanie kontekstu - wyciągnij z dyskusji~~ |

### Nakazy

- Każdy temat = osobna sekcja wg szablonu
- Narracja przed listą (Kontekst → Ryzyka → Alternatywy → Decyzja → Zadania)
- Zachowaj szczegóły techniczne (nazwy tabel, parametry, API)
- Jeśli decyzja odroczona – napisz dlaczego
- Jeśli były alternatywy – zapisz je z powodami odrzucenia
- **Pomysły Przemka** – oznaczaj wyraźnie (patrz sekcja poniżej)
- **Elastyczność** – pomijaj puste sekcje, nie wymuszaj wszystkich

---

## Pomysły Przemysława Sołdackiego (Przemka)

**KRYTYCZNE:** Przemysław Sołdacki (Przemek) często przedstawia pomysły i koncepcje, które **NIE są ostatecznymi decyzjami**, ale raczej propozycjami do rozważenia.

### Zasady oznaczania

1. **Domyślnie - oznacz jako pomysł:**
   - Jeśli Przemek przedstawia koncepcję/pomysł bez wyraźnego potwierdzenia od innych uczestników → użyj statusu **💡 Propozycja** lub dodaj oznaczenie **"💭 Pomysł Przemka"**
   - W sekcji "Decyzja" napisz: **"💭 Pomysł Przemka - wymaga rozważenia"** lub podobnie

2. **Wyjątek - gdy pomysł jest potwierdzony:**
   - Jeśli uczestnicy **wyraźnie potwierdzają** pomysł Przemka (np. "dobry pomysł", "zgadzam się", "tak zrobimy") → możesz użyć statusu **✅ Zatwierdzone**
   - W takim przypadku **nie oznaczaj** jako pomysł, tylko jako decyzję

3. **Jak rozpoznać potwierdzenie:**
   - Wyraźne: "zgadzam się", "dobry pomysł", "tak zrobimy", "właśnie o to chodzi"
   - Brak sprzeciwu ≠ potwierdzenie - jeśli nikt nie komentuje, traktuj jako pomysł do rozważenia
   - Pytania i dyskusja = pomysł wymagający rozważenia, nie decyzja

4. **Format w sekcji "Decyzja":**
   ```markdown
   **Status:** 💡 Propozycja
   
   💭 Pomysł Przemka: [opis koncepcji] - wymaga rozważenia przez zespół.
   ```

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

## Checklist przed zapisem

- [ ] Każdy wątek ma osobną sekcję
- [ ] Metadane na początku dokumentu (data, typ, temat)
- [ ] Brak cytowań i znaczników czasu
- [ ] Narracja kontekstu przed listami
- [ ] Rozważane alternatywy zapisane (jeśli były)
- [ ] Szczegóły techniczne zachowane (nazwy, parametry, API)
- [ ] Status decyzji oznaczony (✅/💡/🔍/⏸️)
- [ ] Tematy nierozwiązane w sekcji "Punkty otwarte"
- [ ] Zadania mają przypisane osoby (jeśli padły)
- [ ] **Pomysły Przemka** – czy oznaczone jako 💭 (chyba że potwierdzone)?
- [ ] **Puste sekcje usunięte** – nie zostawiaj sekcji bez treści

---

## Lokalizacja pliku wyjściowego

```
Notatki/Gotowe-notatki/RRRR-MM-DD {Typ} - {temat}.md
```

Przykłady:
- `2025-08-07 Rada architektów.md`
- `2025-11-03 Sprint review.md`
- `2025-10-14 Spotkanie projektowe - Repozytorium.md`
- `2025-11-28 Planowanie sprintu.md`

---

## Powiązane zasoby

- **Skill czyszczenia:** `.claude/skills/transcript-cleaning/SKILL.md`
- **Katalog notatek:** `Notatki/Gotowe-notatki/`
- **Indeks projektów:** `projekty/README.md`
- **Styl dokumentacji:** `projekty/STYL.md`
- **Struktura Project Canvas:** `projekty/ZASADY.md`

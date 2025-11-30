# PROMPT: Przetwarzanie notatek

## Cel

Systematyczne przetwarzanie notatek ze spotkań (Rada Architektów, Sprint Review, Spotkania projektowe) i aktualizacja dokumentacji projektów (**Project Canvas**) na podstawie zawartych w nich ustaleń, decyzji i zadań.

---

## Dokumenty referencyjne

**WAŻNE:** Przed aktualizacją projektów zapoznaj się z:
- `projekty/ZASADY.md` - **struktura** Project Canvas (jakie sekcje, co w nich)
- `projekty/STYL.md` - **styl pisania** (JAK pisać treść, narracja + lista, ZERO halucynacji)
- `projekty/SZABLON.md` - szablon głównego projektu
- `projekty/SZABLON-PODPROJEKT.md` - szablon podprojektu

---

## Główne zadania

Możesz poprosić o wykonanie jednego z trzech głównych zadań:

1. **Aktualizacja rejestru notatek (`sync-notes`)**: Szybkie zadanie do synchronizacji listy notatek oczekujących na przetworzenie. To zadanie **nie czyta treści notatek**, jedynie listuje pliki i porównuje je z rejestrem.
2. **Przetworzenie następnej notatki (`process-note`)**: Główne zadanie polegające na analizie **jednej**, najstarszej nieprzetworzonej notatki i aktualizacji powiązanej dokumentacji.
3. **Reprocesing od zera (`reprocess-all`)**: Reset rejestru i ponowne przetworzenie wszystkich notatek chronologicznie od najstarszej.

---

## Workflow 1: Aktualizacja rejestru notatek (`sync-notes`)

**Cel:** Upewnienie się, że `_rejestr_przetworzonych.md` jest aktualny w stosunku do plików w repozytorium.

**Katalogi do skanowania:**
- `Planowanie sprintu/`
- `Rada architektów/`
- `Spotkania projektowe/`
- `Sprint review/`

**Kroki:**
1. **Wylistuj pliki**: Użyj `list_dir` dla każdego z katalogów docelowych.
2. **Przeczytaj rejestr**: Odczytaj `Notatki/_rejestr_przetworzonych.md`.
3. **Porównaj i zaktualizuj**: Dla każdego pliku, którego brakuje w rejestrze, dodaj go do sekcji "Notatki oczekujące".
4. **Zgłoś wynik**: Poinformuj użytkownika, ile nowych notatek zostało dodanych do kolejki.

---

## Workflow 2: Przetworzenie następnej notatki (`process-note`)

**Cel:** Przetworzenie najstarszej oczekującej notatki i zaktualizowanie wiedzy w projektach.

### Krok 1: Identyfikacja notatki do przetworzenia

1. **Przeczytaj rejestr**: Odczytaj `Notatki/_rejestr_przetworzonych.md`.
2. **Znajdź następną**: Zlokalizuj pierwszy wpis na liście "Notatki oczekujące", który nie jest oznaczony jako `[x]`. To jest notatka do przetworzenia.
3. Jeśli nie ma notatek do przetworzenia, poinformuj o tym i zakończ.
4. **Zachowaj chronologię**: Przetwarzaj notatki w kolejności chronologicznej, aby zapewnić spójność historii projektów.

### Krok 2: Analiza notatki

Dla zidentyfikowanej notatki:

1. **Przeczytaj słownik projektów** `.claude/skills/_SLOWNIK_PROJEKTOW.md` - to jedyne źródło prawdy o nazwach i zakresach projektów. **ZAKAZ ZGADYWANIA** nazw projektów.

2. **Przeczytaj całą treść** notatki.

3. **Zidentyfikuj tematy** - każdy punkt/sekcja to osobny temat.

4. **Dla każdego tematu określ:**
   - Do którego **istniejącego projektu** się odnosi:
     - NAJPIERW sprawdź słownik projektów (`.claude/skills/_SLOWNIK_PROJEKTOW.md`)
     - Użyj opisu projektu i tabeli mapowania tematów
     - Użyj DOKŁADNEJ ścieżki ze słownika
     - Jeśli nie ma w słowniku → oznacz jako "Nowy temat / do sklasyfikowania"
   - Czy dotyczy **podprojektu** (np. temat o Edytorze formularzy → podprojekt `Moduly/Edytor-procesow/Edytor-formularzy/`).
   - Czy wymaga **utworzenia nowego projektu** (zobacz `projekty/ZASADY.md` → "Kiedy tworzyć nowy projekt" + konsultacja z użytkownikiem).
   - Czy wymaga **utworzenia nowego podprojektu** (zobacz `projekty/ZASADY.md` → "Kiedy tworzyć podprojekt" + konsultacja z użytkownikiem).
   - Czy temat jest **odłożony/odrzucony** - nie wymaga aktualizacji projektu, ale powinien być zapisany w Backlog lub ADR z odpowiednim statusem.

### Krok 3: Propozycja planu zmian

**ZAWSZE przedstaw plan użytkownikowi przed wykonaniem zmian:**

```markdown
## Plan przetwarzania: [Nazwa notatki]

### Projekty do aktualizacji/utworzenia

| Temat | Projekt/Podprojekt | Akcja | Sekcja Project Canvas | Opis |
|-------|-------------------|-------|----------------------|------|
| Temat 1 | `moduly/Edytor-procesow` | Aktualizacja | Sekcja 7 (Podprojekty) | Aktualizacja statusu podprojektu |
| Temat 2 | `moduly/Edytor-procesow/Edytor-formularzy` | Aktualizacja | Sekcja 4 (MVP) | Postęp w MVP1 |
| Temat 3 | `moduly/Edytor-procesow/Nowy-podprojekt` | NOWY PODPROJEKT | - | Nowy podprojekt |
| Temat 4 | `kategoria/Nowy-projekt` | NOWY PROJEKT | - | Nowy projekt |

### Odrzucone koncepcje (do ADR)

| Temat | Projekt | Powód odrzucenia |
|-------|---------|------------------|
| Koncepcja X | `moduly/Xyz` | [Powód z notatki] |

### Tematy bez aktualizacji (odroczone)

| Temat | Powód |
|-------|-------|
| Temat X | Odroczone - brak wymagań klienta |

### Podsumowanie

- **Nowe projekty:** X
- **Nowe podprojekty:** Y
- **Aktualizacje:** Z
- **Pominięte:** W

**Czy zatwierdzasz ten plan?**
```

**Wskazówki do kolumny "Sekcja Project Canvas":**
- Sekcja 1 (PO CO) - zmiana celów/problemu
- Sekcja 2 (ADR) - nowa decyzja architektoniczna lub **odrzucona koncepcja** (status ❌ + Powód odrzucenia)
- Sekcja 3 (Ryzyka) - nowe ryzyko lub zmiana fazy
- Sekcja 4 (MVP) - postęp w checklistach, nowe funkcjonalności
- Sekcja 5 (Historia) - zawsze aktualizowana
- Sekcja 7 (Podprojekty) - aktualizacja statusu podprojektu w projekcie nadrzędnym

### Krok 4: Zatwierdzenie planu

- Czekaj na zatwierdzenie planu przez użytkownika.
- Jeśli użytkownik zasugeruje modyfikacje (np. "Temat X przenieś do innego projektu"), zaktualizuj plan i przedstaw go ponownie.
- Jeśli użytkownik odrzuci plan, zakończ przetwarzanie tej notatki, pozostawiając ją w kolejce.

### Krok 5: Wykonanie aktualizacji

Po zatwierdzeniu planu, dla **KAŻDEGO** projektu/podprojektu objętego zmianami:

1. **Przeczytaj dokumenty referencyjne:**
   - `projekty/STYL.md` (styl pisania)
   - `projekty/ZASADY.md` (struktura Project Canvas)
   - Poprzednią wersję Project Canvas (`projekty/.../Nazwa-projektu.md`)

2. **Zastosuj zmiany zgodnie z planem:**
   - **Aktualizuj Project Canvas (`Nazwa-projektu.md`)**, ściśle trzymając się `STYL.md`:
     - Zachowaj format "narracja + lista".
     - Unikaj ogólników; używaj konkretów.
     - Nie dodawaj informacji, których nie ma w notatce (użyj `[DO USTALENIA]`).
     - Zaktualizuj datę w nagłówku: `**Ostatnia aktualizacja:** YYYY-MM-DD`.
     - Dodaj linki do źródła używając linkowania Obsidian: `→ [[2025-08-12 Rada architektów|Źródło]]` (nazwa notatki bez ścieżki).
     - **Dla dat decyzji/zmian:** używaj linkowania dzienników: `[[2025-08-12]]` - Obsidian automatycznie utworzy dziennik w folderze `Dziennik/`.
     - Dodaj wpis w **Sekcji 5 (Historia zmian)** z linkiem do daty: `| [[2025-08-12]] | Zmiana | [[2025-08-12 Rada architektów]] |`.
     - **Dla odrzuconych koncepcji:** dodaj do ADR ze statusem ❌ Odrzucone i wypełnij kolumnę "Powód odrzucenia".
   - **Zaktualizuj `README.md` projektu**, jeśli kluczowe informacje (status, MVP) uległy zmianie.
   - **W przypadku NOWYCH projektów**, użyj `projekty/SZABLON.md` do utworzenia plików `Nazwa-projektu.md` i `README.md`, a następnie dodaj projekt do głównego indeksu w `projekty/README.md`.
   - **W przypadku NOWYCH podprojektów**, użyj `projekty/SZABLON-PODPROJEKT.md` i:
     - Utwórz katalog podprojektu wewnątrz projektu nadrzędnego
     - Utwórz `Nazwa-podprojektu.md` i `README.md`
     - **Zaktualizuj projekt nadrzędny** - dodaj wpis w sekcji "7. PODPROJEKTY"

3. **Użyj `write_todos`**, aby śledzić postęp aktualizacji wielu projektów.

### Krok 6: Finalizacja i aktualizacja rejestru

Po zaktualizowaniu wszystkich projektów:

1. **Dodaj linki zwrotne w źródłowej notatce:** Dla każdego przetworzonego tematu dodaj link do odpowiedniego projektu używając linkowania Obsidian: `[[Nazwa-projektu]]` (nazwa projektu bez ścieżki - Obsidian znajdzie plik automatycznie).
2. **Aktualizuj rejestr `Notatki/_rejestr_przetworzonych.md`**:
   - Oznacz notatkę jako przetworzoną: `- [x] YYYY-MM-DD: Typ notatki`.
   - Dodaj wpis do tabeli "Status przetwarzania".
   - Zaktualizuj statystyki na końcu pliku.

### Krok 7: Raport końcowy

Po przetworzeniu notatki przedstaw podsumowanie:

```markdown
## ✓ Przetworzona: [Nazwa notatki]

### Podsumowanie zmian

- **Zaktualizowane projekty:** [Lista zaktualizowanych projektów]
- **Zaktualizowane podprojekty:** [Lista]
- **Nowe projekty:** [Lista nowych projektów]
- **Nowe podprojekty:** [Lista]

### Statystyki

- **Przetworzone:** X notatek
- **Oczekujące:** Y notatek

**Następna do przetworzenia:** [Nazwa]
```

---

## Workflow 3: Reprocesing od zera (`reprocess-all`)

**Cel:** Reset dokumentacji projektów i ponowne przetworzenie wszystkich notatek chronologicznie.

**Kiedy używać:**
- Zmieniono szablon Project Canvas
- Poprawiono jakość notatek
- Potrzebna jest "czysta" historia projektów

### Krok 1: Reset rejestru

1. Zresetuj `_rejestr_przetworzonych.md` - oznacz wszystkie notatki jako nieprzetworzone (`- [ ]`)
2. Wyczyść tabelę "Status przetwarzania"
3. Zresetuj statystyki

### Krok 2: Przetwarzanie chronologiczne

1. Przetwarzaj notatki **od najstarszej do najnowszej**
2. Dla każdej notatki wykonaj standardowy Workflow 2 (`process-note`)
3. Historia zmian w projektach będzie rosła naturalnie od najstarszych wpisów

**WAŻNE:** Przy reprocesingu projekty są tworzone/aktualizowane od zera, więc treść sekcji 1-4 jest nadpisywana kolejnymi notatkami. Historia zmian (sekcja 5) rośnie chronologicznie.

---

## Mapowanie tematów na projekty

### Gdzie szukać projektów

- `projekty/README.md` - główny indeks wszystkich projektów

### Typowe mapowania

| Temat w notatce | Projekt | Podprojekt (jeśli dotyczy) |
|-----------------|---------|---------------------------|
| Edytor formularzy, drag-and-drop pól | `moduly/Edytor-procesow` | `Edytor-formularzy/` |
| Matryca uprawnień | `moduly/Edytor-procesow` | `Matryca-uprawnien/` |
| Edytor diagramu, etapy, połączenia | `moduly/Edytor-procesow` | `Edytor-diagramu/` |
| Edytor szablonów dokumentów | `moduly/Edytor-procesow` | `Edytor-szablonow/` |
| Raporty systemowe | `moduly/Raporty-systemowe` | - |
| Moduł raportowy | `moduly/Modul-raportowy` | - |
| Funkcje reguł (CreateCallout, HasDuplicates) | `moduly/Silnik-regul` | - |
| Ustawienia, joby, integracje | `moduly/Ustawienia-systemowe` | - |
| Trust Center | `moduly/Trust-Center` | - |
| Copilot, AI, baza wiedzy | `moduly/Copilot-Baza-wiedzy-AI` | - |
| e-Doręczenia | `moduly/e-Doreczenia` | - |
| SharePoint, OAuth, SAML, AD, Entra, Azure, SSO | `integracje/SharePoint-OAuth` | - |
| callRest, multipart | `integracje/Integracje-REST-multipart` | - |
| Maile, kolejka, powiadomienia | `integracje/System-mailowy` | - |
| Bezpieczeństwo sesji, wylogowanie | `cross-cutting/Bezpieczenstwo-sesji` | - |
| UI sprawy, ikonki, pola, podgląd dokumentu na sprawie | `cross-cutting/Interfejs-sprawy` | - |
| Wydajność | `cross-cutting/Wydajnosc` | - |
| Security checklist | `koncepcje/Security-Checklist` | - |

---

## Mapowanie tematów na sekcje Project Canvas

Zidentyfikuj o czym jest temat i do której sekcji trafi:

| Typ informacji | Sekcja Project Canvas |
|----------------|----------------------|
| **Nowa decyzja architektoniczna** (Framework, technologia, podejście) | Sekcja 2 - ADR |
| **Odrzucona koncepcja/decyzja** | Sekcja 2 - ADR (status ❌, wypełnij "Powód odrzucenia") |
| **Nowe ryzyko** lub zmiana mitygacji | Sekcja 3 - Ryzyka |
| **Zmiana fazy** projektu (analiza → realizacja) | Sekcja 3 - Obecna faza |
| **Postęp w istniejącym MVP** (zrobione zadania) | Sekcja 4 - checklisty `[x]` |
| **Nowa funkcjonalność** do MVP | Sekcja 4 - dodaj do checklisty `[ ]` |
| **Nowy MVP** (kolejna paczka) | Sekcja 4 - nowa sekcja MVP2/MVP3 |
| **Funkcjonalność odroczona** | Sekcja 4 - Backlog |
| **Zmiana celu/problemu** projektu | Sekcja 1 - PO CO TO ROBIMY |
| **Każda zmiana** | Sekcja 5 - Historia zmian (zawsze) |
| **Aktualizacja statusu podprojektu** | Sekcja 7 - Podprojekty (w projekcie nadrzędnym) |

---

## Linkowanie Obsidian

**WAŻNE:** Wszystkie dokumenty używają linkowania Obsidian dla tworzenia grafu powiązań.

### Format linkowania

- **Notatki:** `[[2025-08-12 Rada architektów]]` (nazwa pliku bez ścieżki)
- **Projekty:** `[[Nazwa-projektu]]` (nazwa projektu bez ścieżki - Obsidian znajdzie plik automatycznie)
- **Podprojekty:** `[[Nazwa-podprojektu]]` (nazwa podprojektu)
- **Dzienniki dat:** `[[2025-08-12]]` (format YYYY-MM-DD)

### Dzienniki dat

Gdy w projekcie występuje data decyzji, zmiany lub wydarzenia, używaj linkowania dziennika:
- `Decyzja podjęta [[2025-08-12]]`
- W tabeli Historia zmian: `| [[2025-08-12]] | Zmiana | [[2025-08-12 Rada architektów]] |`

**Obsidian automatycznie:**
- Utworzy plik `Dziennik/2025-08-12.md` (jeśli nie istnieje)
- Wyświetli linki zwrotne do wszystkich miejsc gdzie użyto tej daty
- Umożliwi przegląd wszystkich wydarzeń z danego dnia

**UWAGA:** Nie musisz tworzyć plików dzienników ręcznie - Obsidian zrobi to automatycznie przy pierwszym użyciu linku.

## Dobre praktyki

1. **Pytaj o potwierdzenie** przed dużymi zmianami
2. **Stosuj STYL.md bezwzględnie:**
   - Narracja przed listą
   - Brak ogólników
   - ZERO halucynacji
3. **Linkuj źródła** - zawsze podawaj źródło używając linkowania Obsidian: `[[2025-08-12 Rada architektów]]`
4. **Linkuj daty** - używaj dzienników dla dat decyzji/zmian: `[[2025-08-12]]`
5. **Nie duplikuj** - jeśli coś już jest w projekcie, tylko zaktualizuj
6. **Śledź postęp** - używaj TodoWrite podczas przetwarzania
7. **Raportuj podsumowania** - użytkownik powinien widzieć co zostało zrobione
8. **Aktualizuj README.md** - szybki przegląd musi być spójny z Project Canvas
9. **Dokumentuj odrzucone koncepcje** - w ADR ze statusem ❌ i "Powodem odrzucenia"
10. **Rozpoznawaj podprojekty** - temat może dotyczyć podprojektu, nie głównego projektu
11. **Używaj linkowania Obsidian** - wszystkie linki przez `[[nazwa]]`, nie przez ścieżki

---

## Checklist przed zapisem zmian

Przed zaktualizowaniem Project Canvas, sprawdź (`STYL.md`):

- [ ] **Narracja przed listą** - Czy wyjaśniłem DLACZEGO przed wymienieniem CO?
- [ ] **Brak ogólników** - Czy użyłem konkretów zamiast "optymalizacja", "poprawa"?
- [ ] **Brak halucynacji** - Czy wszystko wynika z notatki lub poprzedniej wersji?
- [ ] **Brak kodu** - Czy nie wkleiłem niepotrzebnych snippetów?
- [ ] **Neutralność** - Czy nie oceniłem pomysłów ("świetny pomysł")?
- [ ] **[DO USTALENIA]** - Czy oznaczyłem braki zamiast je wymyślać?
- [ ] **Historia zmian** - Czy dodałem wpis z datą i źródłem?
- [ ] **README spójny** - Czy zaktualizowałem README.md jeśli potrzebne?
- [ ] **Linki do źródeł w projekcie** - Czy dodałem link Obsidian `[[2025-08-12 Rada architektów]]` przy nowych informacjach?
- [ ] **Linki do projektów w notatce** - Czy dodałem link Obsidian `[[Nazwa-projektu]]` do źródłowej notatki?
- [ ] **Linki do dat** - Czy użyłem dzienników `[[2025-08-12]]` dla dat decyzji/zmian?
- [ ] **Odrzucone koncepcje** - Czy dodałem do ADR ze statusem ❌ i "Powodem odrzucenia"?
- [ ] **Podprojekty** - Czy zaktualizowałem sekcję "7. PODPROJEKTY" w projekcie nadrzędnym?

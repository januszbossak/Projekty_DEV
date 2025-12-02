> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Poprawiono przypisanie projektu w nagłówku. Doprecyzowano kontekst problemów (Tabela jako podformularz - workaround CSS, Ukrycie kafelka - API Azure). Skorygowano nazwę technologii dla aplikacji desktopowej (MAUI/.NET zamiast "inny framework"). Oznaczono niejasny termin aktualizacji chmury.

# Daily – 2025-10-29

**Data:** 29 października 2025, 08:20
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Patrycja Walaszczyk
**Co robię:**
- Sprawdzanie bugów
- Internal testy
- Weryfikacja hotfixa

### Oktawia Ostrowska
**Co robię:**
- Internal testy
- Listy stałe (prawdopodobnie "listy stałych wartości" lub podobne)

### Michał Zwierzchowski
**Co robię:**
- Testy "playing" raportów (wersja 7.0 - wątpliwości co do działania, "coś mi nie pasuje")
- Aktualizacja środowisk testowych
- **Plan aktualizacji chmury:** Ustalono z Łukaszem harmonogram (start 13.06? - *data w transkrypcji niejasna: "do czerwca ameryk od trzynastego"*) do końca listopada.

### Filip Liwiński
**Co robię:**
- Parsowanie plików (Repozytorium plików)
- Poprawki na liście pól formularza

**Plan na dziś:**
- Repozytorium (po skończeniu listy pól)

### Piotr Buczkowski
**Co robię:**
- Wgrywanie dużych plików (API) - zrobione, ale "trochę poległem" na dokumentacji
- Dokumentacja (tworzenie generatora biblioteki TypeScript, by był uniwersalny)

### Przemysław Rogaś
**Co robię:**
- Poprawka do modułu raportowego (wstrzymana - "znalazłem kilka innych błędów... marnuję czas... nie wiem jak to powinno być docelowo")
- Baza wiedzy

**Plan na dziś:**
- Merge zadań
- Zadania z edytora

### Anna Skupińska
**Co robię:**
- Merge i fail testy
- Praca nad fixem (problem: brak informacji o "liczbie szablonów" w fixie - do ustalenia z Kamilem po Daily)

### Marek Dziakowski
**Co robię:**
- Merge
- Dodawanie do blockchain (przeniesiono część funkcjonalności, do przetestowania)
- TrustCenter (poprawa wydajności kasowania starych dokumentów/kodów)
- Powiadomienia realtime (odłożone na później)

### Adrian Kotowski
**Co robię:**
- Przelewy24 (dodanie waluty - przetestowane, do zmergowania)
- Problem ze znikaniem polskiego znaku w hotfixie
- Przygotowanie do integracji z Comarch (spotkanie)
- Wsparcie Deutsche Bank (migracja e-poleconego, problem z firewallem - Adrian wspiera wdrożeniowca)
- Rozbudowa integracji z konektorem (KSeF/e-Doręczenia?)

### Mariusz Piotrzkowski
**Co robię:**
- Drobne poprawki i merge
- Porządki w zadaniach

**Plan na dziś:**
- Poprawka usługi (panel załączników na dole - prośba Kamila)
- "Internowanie" dropdown na załącznikach (prawdopodobnie "Zintegrowanie" lub "Internacjonalizacja"?)

### Barbara Michałek
**Co robię:**
- Internal testy (6 pass, 2 fail, 3 nowe zgłoszenia)
- Weryfikacja zgłoszeń (pytanie do Kamila o listę w edytorze procesów - "waiting for information")

---

## 2. Nowe zgłoszenia do backlogu

### Aplikacja Desktopowa / Front (Nowa aplikacja do podpisywania)
**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS` (lub ogólnie `Moduly/Trust-Center`)
**Opis:**
Dyskusja o technologii dla frontu nowej aplikacji desktopowej (zastępującej/rozszerzającej SignApp). Adrian sugerował framework inny niż standardowy React (kompatybilny z Windows/Mac) - prawdopodobnie **.NET MAUI** (wspomniane we wcześniejszych daily, tu Damian mówi "coś tam iui").
**Ustalenia:**
- Damian przypisał zadanie Mariuszowi (In Design), ale pyta Kamila o przejęcie (weryfikację kryteriów akceptacji).
- Konieczna weryfikacja kierunku technologicznego (czy React desktopowy czy MAUI).

### Tabela jako podformularz (Zgłoszenie Kacpra)
**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`
**Opis:**
Możliwość dodania wiersza do tabeli mimo, że jest ustawiona jako "do odczytu" (jako podformularz).
**Ustalenia:**
- Damian ma gotowe **rozwiązanie CSS** (workaround ukrywający przycisk), które może przekazać w 5 minut.
- Jeśli to wystarczy jako hotfix, można zdjąć priorytet błędu.
- Docelowo do poprawy w kodzie.

### Ukrycie kafelka konta systemowego
**Projekt:** `cross-cutting/Interfejs-sprawy`
**Opis:**
Janusz zgłosił, że widzi konta systemowe (mają jego maila).
**Kontekst:** Janusz wykorzystuje te konta do połączenia API z Azurem, stąd jego mail w konfiguracji.
**Status:** Niski priorytet ("do zaorania" / "blok na nie wiadomo kiedy"). Dotyczy tylko adminów.

### Hotfix 21051 (Kwiecień)
**Status:** Stare zgłoszenie wiszące u Michała. Michał sugeruje przeniesienie na backlog ("Backlog").

---

## 3. Tematy organizacyjne

### Aktualizacja środowisk (Chmura)
**Kategoria:** DevOps
**Ustalenie:**
Harmonogram aktualizacji środowisk testowych w chmurze ustalony z Łukaszem: start 13-go (listopada?), koniec do końca listopada.

### Zatory w testach (Koniec sprintu)
**Kategoria:** Procesy
**Problem:**
Kumulacja zadań do testów w czwartek/piątek przed końcem sprintu (30-40 zadań). Przemek miał plan na dzisiaj, ale ryzyko zatoru jutro.
**Ustalenie:**
Należy przypominać deweloperom o bieżącym mergowaniu zadań. Przesunięcie testów na kolejny tydzień jest traktowane jako "błąd planowania", ale akceptowalne (nie ma sensu walczyć z wiatrakami, trzeba pilnować by nie trzymali zadań).

### Spotkanie Live (10.11)
**Kategoria:** Spotkania
**Ustalenie:**
Większość zespołu będzie na urlopach 10 listopada (poniedziałek?). Sprint krótszy o 2 dni. Należy uwzględnić przy planowaniu.

---

## 4. Decyzje ad-hoc

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Generator biblioteki TS | `moduly/Repozytorium` | 💡 Propozycja | **Pomysł Piotra:** Stworzenie uniwersalnego generatora dokumentacji/biblioteki TypeScript do obsługi wgrywania plików (duże pliki API). |
| Technologia Frontu Desktop | `cross-cutting/Technologie` | 🔍 Do analizy | Adrian sugeruje framework cross-platform (MAUI?). Wymaga weryfikacji architektonicznej (Kamil/Piotr). |
| Workaround CSS dla tabeli | `Moduly/Edytor-procesow` | ✅ Zatwierdzone | Damian dostarczy szybkie rozwiązanie CSS dla klienta (Kacpra), właściwa poprawka później. |

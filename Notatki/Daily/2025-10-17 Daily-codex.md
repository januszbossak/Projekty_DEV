# Daily – 2025-10-17

**Data:** 17 października 2025, 07:20
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Filip Liwiński
**Co robię:**
- Lista pól edytora formularza
- Poprawki tłumaczeń
- Drobne poprawki nałożenia systemowego (logi systemowe)

### Anna Skupińska
**Co robię:**
- Zadania z tablicy (wygasłe wpisy w raporcie wciąż widoczne, przyciski read-only)

### Michał Zwierzchowski
**Co robię:**
- Powiadomienia Teams - testowanie aplikacji zamiast webhooków (cel: lepszy wygląd, ale "jakoś tak średnio mi się to podoba", do weryfikacji czy łatwiej/lepiej)
- Aktualizacja Azure DevOps
- Przygotowanie do planowania (przenoszenie zadań, zamykanie sprintu)

### Patrycja Walaszczyk
**Co robię:**
- Testy matrycy uprawnień (zakończone)
- Testy listy bugów

**Blokery:**
- Brak

### Mariusz Piotrzkowski
**Co robię:**
- Pasek przewijania tabeli (poprawa wyświetlania, "prawie cała zrobiona")
- Tabela w widoku formularza (przywrócenie widoku "jak kiedyś" - obejście, ale działa)
- Aktualizacja TrustCenter (wspólnie z Markiem - nauka procedury podnoszenia wersji)

### Marek Dziakowski
**Co robię:**
- Poprawki fake testów
- Bug z reprezentacją pola typu podpis (konsultacja z Kamilem czy tylko jeden typ reprezentacji)
- Moduł raportowy (bug)
- Aktualizacja TrustCenter (podmiana linku)

### Kamil Dubaniowski
**Co robię:**
- Integracja z podpisem jednorazowym (Axel Springer - weryfikacja tożsamości) - **Status:** "Nie mam zbyt pozytywnych doświadczeń"
- Backlog (czyszczenie starych zgłoszeń, dodawanie nowych z czatów)
- Przygotowanie do planowania (szacowanie effortu - "estimating")

### Łukasz Bott
**Co robię:**
- Raporty systemowe (rekonfiguracja)
- Aktualizacja Wiki
- Przygotowanie do przekazania obowiązków przed urlopem (spotkanie wewnętrzne LOT)

### Łukasz Brocki
**Co robię:**
- Bugi listy
- Temat Orlenu (problemy z JavaScript/ładowaniem formularza - błąd występuje tylko u klienta, **niepowtarzalny na testowym**; dodano logi, oczekiwanie na dane)

### Przemysław Rogaś
**Co robię:**
- Zadania do edytora procesów
- Poprawki do diagramu (nowe uwagi)

### Piotr Buczkowski
**Co robię:**
- Incydent bezpieczeństwa (analiza wycieku haseł z darknetu - nie od nas, z przeglądarek). **Status:** Lista zagrożonych kont przygotowana i wysłana.
- Naprawa `register.amodit.com` (błędy w bazie od 3 miesięcy)
- Bug 2195 (konflikty przy wgrywaniu HTML)

### Barbara Michałek
**Co robię:**
- Fake testy hotfixa
- Weryfikacja zadań (dokończenie sprintu, nadrabianie zaległości)

### Adrian Kotowski
**Co robię:**
- Podpisywanie na MacOS (SignApp - problem z weryfikacją/udzielaniem uprawnień dostępu, "problem z udzieleniem dolara" - błąd ASR)
- Testowanie Szafir na Macu (przygotowanie środowiska testowego u Kamila, wniosek o zakup podpisów do testów)

---

## 2. Nowe zgłoszenia do backlogu

### Problem Orlenu (JavaScript)
**Projekt:** `cross-cutting/Wydajnosc` (lub `Klienci/Orlen` jeśli istnieje)
**Opis:**
Błędy JS u klienta (Orlen), prawdopodobnie przy ładowaniu formularza. Niepowtarzalne na środowisku testowym.
**Status:** Wysłano wersję z dodatkowymi logami, oczekiwanie na dane diagnostyczne.
**Przypisanie:** Łukasz Brocki.

### SignApp na MacOS
**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`
**Opis:**
Problemy z podpisem w aplikacji SignApp na systemie MacOS (konieczność wielokrotnej weryfikacji/udzielania uprawnień).
**Akcja:** Testowanie różnych dostawców podpisu na środowisku Mac (Adrian/Kamil). Zakup podpisów testowych.

---

## 3. Tematy organizacyjne

### Projekt LOT (Kick-off)
**Kategoria:** Spotkania
**Ustalenie:**
- Kick-off projektu w poniedziałek (20.10) o 13:30.
- Analiza potrwa 2 tygodnie.
- Łukasz Bott (mimo urlopu) weźmie udział w spotkaniu otwierającym.
- Konieczność renegocjacji harmonogramu (sztywne terminy w umowie vs realny start prac po analizie).
- Tematy techniczne do analizy: Znak wodny, SSO/Integracja SIM.

### Aktualizacja TrustCenter
**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna` (Procedury) / `Moduly/Trust-Center`
**Ustalenie:**
- Aktualizacja wszystkich środowisk (Test, Demo, Produkcja).
- Produkcja aktualizowana po 16:00.
- **Szkolenie:** Marek szkoli Mariusza z procedury podnoszenia wersji ("będę przy nim dosłownie podnosił").
- **Procedura:** Pół-automatyczna (ze względu na specyfikę Azure/sklepu, pełna automatyzacja niemożliwa).

### Planowanie Sprintu
**Kategoria:** Spotkania
**Termin:** Dziś (17.10) o 14:00.
**Akcja:** Kamil prosi o oszacowanie zadań w statusie "Estimating" przed spotkaniem.

### Urlopy
**Kategoria:** Urlopy
- Łukasz Bott: Urlop od poniedziałku (2 tygodnie).
- Oktawia i Mateusz: Nieobecni.

---

## 4. Decyzje ad-hoc

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Powiadomienia Teams przez aplikację | `cross-cutting/Komunikaty-systemowe` | 💡 Do weryfikacji | Michał testuje przejście z webhooków na dedykowaną aplikację Teams. Wrażenia "średnie", ale może być łatwiej. |
| Aktualizacja TrustCenter (Procedura) | `Organizacja-DEV/Dokumentacja-organizacyjna` | ✅ Zatwierdzone | Procedura aktualizacji pozostanie pół-automatyczna. Marek przeszkoli Mariusza (zwiększenie bus factor). |
| Integracja z podpisem jednorazowym (Axel Springer) | `Integracje/` | ⚠️ Problemy | Kamil zgłasza negatywne doświadczenia z integracją (weryfikacja tożsamości). |
| Incydent bezpieczeństwa | `cross-cutting/Bezpieczenstwo-pentesty` | ✅ Zakończone | Piotr przeanalizował wyciek haseł (nie z AMODIT), przygotował i wysłał listę zagrożonych kont. |

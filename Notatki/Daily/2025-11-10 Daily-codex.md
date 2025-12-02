> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Zaktualizowano nagłówek o właściwe przypisanie projektu. Doprecyzowano status integracji z UPS/Global Express (weryfikacja, że to inna firma niż usługa Poczty Polskiej). Skorygowano błąd w notatce "Szkolenie z Radą" -> "Szkolenie z RODO". Uzupełniono szczegóły kontekstowe o braki i niezgodności z transkrypcji.

# Daily – 2025-11-10

**Data:** 10 listopada 2025, 08:20
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Mateusz Kisiel
**Co robię:**
- Komunikator (dokończenie) - prośba do Damiana o zgłoszenie do testów
- Poprawki od OCR (niejasne, czy chodzi o "poprawki od zero" czy "poprawki OCR")

### Patrycja Walaszczyk
**Co robię:**
- Kończę re-testy bugów

**Blokery:**
- Brak

### Oktawia Ostrowska
**Co robię:**
- Bug (1)
- PBIs (2)

**Blokery:**
- Brak

### Marek Dziakowski
**Co robię:**
- Hotfix (dostęp obserwatorów do spraw z raportu - czeka na dostęp do bazy)
- TrustCenter (usługa zużywa dużo procesora - analiza, kontynuacja prac, serwis wycofał usługę na testach)
- Konsultacje

### Łukasz Brocki
- **W czwartek:** Hotfix (diagnoza trudna, zgłaszający na urlopie).
- **Dzisiaj:** Przygotowanie do kontaktu z UPS (sprawdzenie API).

### Mariusz Piotrzkowski
**Co robię:**
- Komentarze ze wzmiankowaniem (dokończenie, do 14:30/15:00)

### Łukasz Bott
- **Co robię:**
  - Aktualizacja dokumentacji Wiki (w tym Changeloga do czerwcowego wydania)
  - Wsparcie PKFU/innych klientów
  - Przegląd zgłoszeń
- **Nowy temat:** Rozpoznanie integracji z **Calendesk** (klientka poprosiła o rozpoznanie możliwości technicznych integracji z systemem kalendarzowym - wpisywanie zdarzeń z AMODIT)
- **Szkolenie RODO (o 14:00):** Szkolenie przypominające z radą.
- **Problem z Makiem Janusza:** Brak kontaktu z firmą, niezgodny z wymaganiami firmowymi, Janusz ma się skontaktować z Justyną i Lemmon Pro.

### Przemysław Rogaś
**Co robię:**
- Nawigacja po grupach, słownikach i źródłach zewnętrznych (strony).
- Poprawka modułu raportowego (ustawienia formularza, pole nadrzędne).

**Plan na dziś:**
- Uzupełnianie tłumaczeń w ustawieniach systemowych.
- Zadania z backlogu (skończyły się przypisane).

### Anna Skupińska
**Co robię:**
- Poprawki błędów (ukrywanie błędu w logach systemowych).
- Praca nad rozszerzeniem parametrów (dla Przemka F.).
- Dodanie akcji anulowania (w 4 oczach) propozycji zmiany parametru systemowego (nie jest to "filler", tylko dodanie opcji anulowania propozycji zmiany).
- Praca nad 2 endpointami (odrzucanie zmian przez administratora).

### Piotr Buczkowski
**Co robię:**
- Analiza wycieku haseł z darknetu (lista zagrożonych kont)
- Naprawa `register.amodit.com` (błędy w bazie)
- Hotfix 2195 (konflikty HTML - dokończenie)

### Barbara Michałek
**Co robię:**
- Fake testy hotfixa (1)
- Zadania do końca sprintu
- Plan urlopu w Korei Południowej (maj/czerwiec 2026) - Łukasz Bott twierdzi, że "będzie ciężko i obawiam się, że się możemy przylecieć i na tym locie".

### Adrian Kotowski
**Co robię:**
- Bug z podpisywaniem (SignApp MacOS - problem z weryfikacją/udzielaniem uprawnień dostępu)
- Problem z wygasaniem tokena i polskimi znakami
- Spotkanie z Kamilem (dot. testowego piecyka dostawców podpisu)

---

## 2. Nowe zgłoszenia do backlogu

### Integracja Calendesk
**Projekt:** `Integracje/` (lub `Moduly/Ustawienia-systemowe/Integracje-rozszerzenia`)
**Opis:** Klientka poprosiła o rozpoznanie możliwości technicznych integracji z systemem kalendarzowym Calendesk (wpisywanie zdarzeń z AMODIT).
**Przypisanie:** Łukasz Bott (rozpoznanie).

### Integracja UPS / Global Express
**Projekt:** `Integracje/`
**Opis:**
Konieczność integracji z kurierem.
**Ustalenia:**
- Łukasz Brocki ma sprawdzić API UPS.
- **Weryfikacja Global Express:** Po wstępnej weryfikacji przez Łukasza Botta, "Global Express" to **inna firma kurierska** niż usługa Poczty Polskiej o podobnej nazwie. Jest to zbieg okoliczności, różnią się subtelnie w nazwie.
- **Akcja:** Łukasze mają dokładnie potwierdzić, którą integrację należy wykonać.

---

## 3. Tematy organizacyjne

### Urlopy
**Kategoria:** Urlopy
- Łukasz Bott: Od poniedziałku (10.11) na urlopie (2 tygodnie).
- Oktawia i Mateusz: Nieobecni.
- Barbara Michałek: Planuje urlop w Korei Południowej (maj/czerwiec 2026).

### Szkolenie RODO
**Kategoria:** Spotkania
**Termin:** Dziś (10.11) o 14:00.
**Prowadzący:** Łukasz Bott.

### Projekt LOT (Integracja)
**Kategoria:** Inne
**Ustalenia:**
- Kick-off w poniedziałek (13:30) - Łukasz Bott weźmie udział.
- Analiza potrwa 2 tygodnie.
- Konieczność renegocjacji harmonogramu (sztywne terminy w umowie vs realny start prac po analizie, terminy wpisane "idiotycznie" bez analizy).
- **Priorytety techniczne do analizy:** Znak wodny (pieczęć kwalifikowana vs zwykły podpis), **SSO** (Single Sign-On, a nie "SSD"), SIM (system monitorujący działanie systemów).
- **Integracje SIM:** Może być robione równolegle, niekoniecznie priorytet.

### Janusz Bossak - problemy techniczne z Makiem
**Kategoria:** Inne
**Problem:** Mac Janusza niezgodny z wymaganiami firmowymi (brak kontaktu z firmą, tylko telefon, "nie mam kontaktu z firmą w ogóle").
**Akcja:** Kontakt z Justyną i Lemmon Pro.

---

## 4. Decyzje ad-hoc

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Testowy piecyk dostawców podpisu | `Integracje/` (lub nowy projekt `Integracje/Podpisy-elektroniczne`) | 💡 Propozycja | **Pomysł Kamila:** Utworzenie testowego środowiska z różnymi dostawcami podpisu, aby ułatwić testowanie problemów z SignApp. |
| Ukrywanie błędów w logach | `cross-cutting/Logowanie-powiadomien` (lub `Moduly/Ustawienia-systemowe`) | ✅ Zatwierdzone | Usunięcie wpisów z logów systemowych, które nie świadczą o błędzie funkcjonalnym, ale generują szum (Ania). |
| Integracja z Kalendeskiem | `Integracje/` | 💡 Do rozpoznania | Klientka poprosiła o rozpoznanie możliwości technicznych integracji. |

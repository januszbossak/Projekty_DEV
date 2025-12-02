# Daily – 2025-11-24

**Data:** 24 listopada 2025, 08:21
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Patrycja Walaszczyk
**Co robię:**
- Testy listy pól
- Szkolenie RODO

### Oktawia Ostrowska
**Co robię:**
- Testy internal (lista pól)
- Zadania podpisywania Simplus
- Szkolenie RODO

### Barbara Michałek
**Co robię:**
- Moduł raportowy
- Zadania z listy pól
- Szkolenie RODO

### Kamil Dubaniowski
**Co robię:**
- Testy listy pól (przy okazji swoich prac)
- Projekt dodawania/usuwania sekcji i pól (nowa lista pól)
- Przegląd prawego panelu edycji pola (UX, błędy, niespójności - "mega grube wybory", złe kolory menu, wygląd pola tabela z zagnieżdżeniami)
- Axel Springer (zapoznanie ze specyfikacją)

### Michał Zwierzchowski
**Co robię:**
- Aktualizacja baz danych (AstraFox, Demo Trafonix)
- Planowana aktualizacja chmury do wersji czerwcowej (problemy z harmonogramem wydań)

### Marek Dziakowski
**Co robię:**
- Zgłoszenia
- Analiza logów z wyciągów (poprawki)

### Filip Liwiński
**Co robię:**
- Lista pól
- Repozytorium (API tworzenia folderów, zapięcie)
- Matryca uprawnień

### Przemysław Rogaś
**Co robię:**
- Zadania z edytora
- Błędy w raportach

### Mariusz Piotrzkowski
**Co robię:**
- Weryfikacja błędów (nie występują)
- Testy w Safari (flagi)
- Reguła automatyczna z przyciskiem do resetowania (poprawione)

**Plan na dziś:**
- Historia ręcznie bez zapisywania sprawy (research)
- Sposób otwierania sprawy z pola Odnośnik (research)

### Mateusz Kisiel
**Co robię:**
- Obsługa MFA (Copilot)
- Generowanie dokumentacji procesu
- SA CRM (poprawka zapisywania sprawy przed regułą)

**Plan na dziś:**
- Kontynuacja generowania dokumentacji
- Zapisywanie historii czatów Copilot w bazie

### Łukasz Brocki
**Co robię:**
- Comarch Hub (bloker - czeka na maila od Michała)
- Global Express (rozpisanie zadań, szukanie API)

### Adrian Kotowski
**Co robię:**
- SignApp MacOS (nowe przyciski, widok, panel wyboru certyfikatu, obsługa flagi e-poleconego)
- Integracja e-doręczeń (flaga metrowce dla protokołu 2.0)
- Proxy dla Deutsche Bank

**Plan na dziś:**
- Dokończenie panelu wyboru certyfikatu
- Wypisywanie z raportów (nowa funkcjonalność)
- Problem szarej przestrzeni na Safari
- Sprawdzenie hipotezy o podpisywaniu tylko jednym hasłem
- Czekanie na taryfikację programu Apple dla Przemka i logo dla aplikacji

### Anna Skupińska
**Co robię:**
- Repozytorium (API tworzenia folderów - problem z testami integracyjnymi, potrzebuje pomocy Michała Z. z bazami)
- Logowanie do SharePoint (Piotr B. robi)

---

## 2. Nowe zgłoszenia do backlogu

### Klucz nie jest unikalny (Rejestr/Usunięte sprawy)
**Projekt:** `Moduly/Modul-raportowy` (lub `cross-cutting/Interfejs-sprawy`)
**Opis:**
Problem z rejestrem i usuniętymi sprawami, które nie są widoczne w zakładce "usunięte".
**Ustalenia:**
- Problem dotyczy Piotra B. (zgłoszenie Basi).
- Komentarz (Kamil): Doraźnie szukać na zakładce "usunięte" po procesie, który jest rejestrem.
- Wniosek: Brak jasności, jak klucz działa po usuniętych sprawach.

### Brak informacji o zablokowaniu karty (SignApp)
**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS` (lub `Moduly/Trust-Center`)
**Opis:**
Podczas podpisywania, po 3 błędnych PINach, brak informacji o zablokowaniu karty. Zgłoszenie Oktawii.
**Akcja:** Łukasz B. ma sprawdzić, czy Simplus zwraca taką informację.

### SMS API USA/Kanada
**Projekt:** `Moduly/Ustawienia-systemowe/Integracje-rozszerzenia`
**Status:** Uruchomione, numer 1-888-xxx zarejestrowany.

---

## 3. Tematy organizacyjne

### Grant Temporary Access (Licencje)
**Kategoria:** Licencje / Dokumentacja
**Problem:**
Niejasność co do przeznaczenia funkcji (dla zewnętrznych vs. pracowników). Brak jasnego opisu na Wiki.
**Ustalenia:**
Uzupełnić artykuł na Wiki oraz opis w systemie o kontekst biznesowy (funkcja dla osób spoza organizacji).

### Walter (zgłaszający błędy)
**Kategoria:** Procesy
**Problem:**
Dużo zgłoszeń od Waltera, często powtarzalnych lub już znanych.
**Ustalenia:**
Potrzeba przydzielenia opiekuna/wsparcia dla Waltera, aby konsultował zgłoszenia przed ich napisaniem. Damian przejmie temat.

---

## 4. Decyzje ad-hoc

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Modyfikacja kolumny w DB (Testy) | Ania potrzebuje zmienić kolumnę na NULLable w bazie testowej. | ✅ Zatwierdzone | Zamiast skryptów migracyjnych na etapie dev, usunąć i odtworzyć tabelę (Docker/Testy integracyjne). |
| Redesign panelu edycji pola | Dyskusja o UX panelu (np. sekcja "Zarządzaj polem", odstępy). | 💡 Do weryfikacji | Temat przeniesiony na spotkanie Design. Janusz broni obecnego rozwiązania dla rzadkich akcji. |
| Aktualizacja AstraFox do Grudniowej | Michał Z. proponuje aktualizację środowisk do grudniowej wersji | 💡 Do dyskusji | Problemy z harmonogramem wydań (Wersja "Czerwcowa" vs "Wrześniowa"). Wymaga spotkania. |
| Przeniesienie tematu licencji na Radę | Problem interpretacji licencji LOT (750 licencji vs 1000 użytkowników AD) | ✅ Zatwierdzone | Temat do omówienia na Radzie Architektów. |
| Integracja Neuca (DocuSign) | Prośba klienta o przechowywanie tokena sesji | 💡 Do weryfikacji | Temat na Radę Architektów. Janusz przeciwny (kwestie bezpieczeństwa/architektury). |
| Wgrywanie dużych plików (Generator TS) | Piotr tworzy generator biblioteki TypeScript do obsługi API | 💡 Propozycja | Ułatwienie dla programistów integrujących się z API (duże pliki). |

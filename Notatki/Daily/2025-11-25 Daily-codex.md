> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Zaktualizowano nagłówek o właściwe przypisanie projektu. Uzupełniono szczegóły statusów prac o brakujące niuanse (Comarch Hub - bloker zdjęty, Global Express - UPS, SignApp MacOS - szara przestrzeń w Safari, problem z transkrypcją Teams). Przypisano tematy do odpowiednich projektów ze słownika. Doprecyzowano statusy decyzji.

# Daily – 2025-11-25

**Data:** 25 listopada 2025, 08:20
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

## 1. Status update

### Barbara Michałek
**Co robię:**
- Zadania z listy pól (internal/relist testy)
- Zgłoszenie dla Filipa (nowe)
- Zadania z edytora graficznego (od Przemka)

### Patrycja Walaszczyk
**Co robię:**
- Internal testy (lista pól)
- Relist testy (bugi z wyższym priorytetem)

### Oktawia Ostrowska
**Co robię:**
- Internal testy (lista pól)
- Relist testy (podpisywanie - nowe zgłoszenie o błędzie, które okazało się problemem z akcjami masowymi, nie podpisem)

### Kamil Dubaniowski
**Co robię:**
- Testy listy pól ("wciąłem się wam trochę")
- Projekt dodawania/usuwania sekcji i pól (nowa lista pól)
- Przegląd prawego panelu edycji pola (UX, błędy, niespójności - np. typ pola widoczny tylko w nagłówku)
- Axel Springer (zapoznanie ze specyfikacją - termin 1.12)

### Michał Zwierzchowski
**Co robię:**
- Aktualizacja baz danych (AstraFox, Demo Trafonix)
- Planowana aktualizacja chmury do wersji czerwcowej (cała chmura w tym tygodniu, jeśli nie będzie problemów) - *Uwaga: w transkrypcji jest duża niepewność co do harmonogramu i nazewnictwa wersji*.

### Filip Liwiński
**Co robię:**
- Lista pól
- Repozytorium plików (API tworzenia folderów, zapięcie - spotkanie wczoraj)
- Matryca uprawnień (2 zadania)

### Marek Dziakowski
**Co robię:**
- Poprawki TrustCenter (logi)
- Błąd blockchain (zablokowane 500 dokumentów przez błąd GdPicture - analiza, wstępnie błąd biblioteki przy tworzeniu podpisanego dokumentu)

### Piotr Buczkowski
**Co robię:**
- Logowanie SharePoint (obejście poprawki Microsoftu - dodanie parametru do kreatora)
- Refactoring logowania certyfikatem (pytanie do Adriana o sensowność zmian)

### Przemysław Rogaś
**Co robię:**
- Podświetlanie sekcji na formularzu
- Poprawki w raportach
- Ustawienia systemowe (generowanie tokenów OAuth - Piotr zwraca uwagę na specyficzny sposób implementacji, który może wymagać przerobienia)

### Anna Skupińska
**Co robię:**
- Testy repozytorium (problem z bazą na Dockerze - rozwiązanie: skrypt w pipeline usunie i odtworzy bazę testową)
- Dorobienie API dla Filipa
- Modyfikacja bazy (zmiana kolumny na NULLable - problem z `amodit database admin`, rozwiązanie jw.)

### Mateusz Kisiel
**Co robię:**
- Obsługa zewnętrznych MFA (Copilot)
- Generowanie dokumentacji procesu (spotkanie z Januszem o 12:00)
- Historia czatów Copilot w bazie

### Mariusz Piotrzkowski
**Co robię:**
- Błąd historii (dodawanie obserwatora - nie dokończone)
- Sposób otwierania sprawy z pola Odnośnik (research)
- Weryfikacja błędów (niektóre przestały występować same)

### Łukasz Brocki
**Co robię:**
- Comarch Hub (bloker zdjęty w piątek - kontynuacja prac)
- Global Express (rozpisanie zadań, szukanie API)

### Adrian Kotowski
**Co robię:**
- SignApp MacOS (nowe przyciski, panel wyboru certyfikatu, obsługa flagi e-poleconego, problem z `hover` na liście)
- Wypisywanie z raportów (nowa funkcjonalność, drobne zmiany w kodzie)
- **Problem:** Szara przestrzeń na Safari (lista certyfikatów).
- Proxy dla Deutsche Bank

### Łukasz Bott
**Co robię:**
- Wsparcie wdrożeń (PKF)
- Spotkanie z Copilot (integracja z systemami klasy KSeF - rozpoznanie wymagań)
- Temat na Radę: Masowe podpisywanie spraw dokumentów na sprawach

### Damian Kamiński
**Co robię:**
- Orlen Paczka (analiza)
- Wdrożenia WIM (połączenie KSeF - nadzieja na sukces dzisiaj)
- Allianz (podnoszenie wersji)

---

## 2. Nowe zgłoszenia do backlogu

### Problem z akcjami masowymi na raporcie (Oktawia Ostrowska)
**Projekt:** `Moduly/Modul-raportowy/Masowe-akcje`
**Opis:**
Zgłoszenie Oktawii dot. podpisywania okazało się problemem z zaznaczaniem checkboxów na raporcie tabelarycznym (akcje masowe), a nie samym podpisem.
**Status:** Do weryfikacji na relist testach.

### Walter (Zgłoszenia AstraFox Cloud)
**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna` (Procesy)
**Opis:**
Duża liczba zgłoszeń od Waltera, często dotyczących znanych tematów.
**Ustalenia:**
Potrzeba przydzielenia opiekuna/wsparcia dla Waltera, aby konsultował zgłoszenia przed ich napisaniem (oszczędność czasu). Damian weźmie to na siebie.

### Klucz nie jest unikalny (Rejestr/Usunięte sprawy)
**Projekt:** `Moduly/Modul-raportowy` (lub `cross-cutting/Interfejs-sprawy`)
**Opis:**
Problem z rejestrem i usuniętymi sprawami, które nie są widoczne w zakładce "usunięte".
**Ustalenia:**
Janusz sugeruje: "Może wystarczy wypisać klucz? Nie jest unikalny. Sprawdź wszystkie sprawy procesu, włączając w to sprawy usunięte".

---

## 3. Tematy organizacyjne

### Grant Temporary Access (Licencje)
**Kategoria:** Procesy / Licencje
**Problem:**
Niejasność co do przeznaczenia funkcji (tylko dla zewnętrznych vs pracownicy). Brak jasnego opisu na Wiki (mimo że artykuł istnieje, nie jest podlinkowany w opisie funkcji).
**Ustalenie:**
Uzupełnić artykuł na Wiki oraz opis w systemie o kontekst biznesowy (funkcja dla osób spoza organizacji).

### Licencje LOT (AD vs AMODIT)
**Kategoria:** Licencje
**Problem:**
Klient (LOT) interpretuje licencje jako "jednoczesne sesje" (750 licencji, 1000 użytkowników w AD) i uważa, że wylogowanie zwalnia licencję.
**Ustalenie:**
Temat do omówienia na Radzie Architektów (Piotr B., Łukasz B.). Wyjaśnienie modelu licencjonowania (blokada konta w AD blokuje w AMODIT).

### Aktualizacja środowiska AstraFox (Grudniowa)
**Kategoria:** Infrastruktura
**Ustalenie:**
Wstrzymanie aktualizacji AstraFox do wersji grudniowej o 2-3 dni. Priorytetem jest stabilizacja wersji czerwcowej (szczególnie tabeli w raportach).

### Dostęp do transkrypcji (Teams)
**Kategoria:** Narzędzia
**Problem:**
Janusz ma problem z dostępem/kopiowaniem transkrypcji (kopiowanie ręczne ucina treść).
**Akcja:**
Damian sprawdzi uprawnienia, Kamil udostępni nagrania. Problem techniczny Teams.

---

## 4. Decyzje ad-hoc

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Modyfikacja kolumny w DB (Testy) | Ania potrzebuje zmienić kolumnę na NULLable w bazie testowej | ✅ Zatwierdzone | Zamiast pisać skomplikowane skrypty migracyjne na etapie dev, usunąć tabelę i pozwolić systemowi ją odtworzyć (Docker/Testy integracyjne). |
| Redesign Panelu Edycji Pola | Dyskusja o układzie przycisków i sekcji | 💡 Do weryfikacji | Temat przeniesiony na spotkanie Design. Konieczność uporządkowania UX (ukrycie rzadkich akcji, spójne odstępy). |
| Integracja Neuca (DocuSign) | Żądanie klienta o przechowywanie tokena sesji | 💡 Do weryfikacji | Temat na Radę Architektów. Wstępna ocena negatywna (bezpieczeństwo/architektura). To rozszerzenie istniejącej integracji (MVP 2). |

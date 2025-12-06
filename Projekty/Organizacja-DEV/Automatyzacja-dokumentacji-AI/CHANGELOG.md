# CHANGELOG - Automatyzacja dokumentacji AI

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Zadanie

- Potrzeba poprawy formuły prezentacji Sprint Review (płynność, materiał do pokazania w firmie)

---

## 2025-10-14 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Spotkanie projektowe - Design.md]
**Kategoria:** #Organizacja #Proces #AI #Dokumentacja

- Usprawnienie procesu generowania i publikacji changelog dla wersji AMODIT
- Narzędzie do półautomatycznego generowania changelog przez AI na podstawie zgłoszeń z Azure DevOps (status Done, release version)
- Definicja formatu changelog, częstotliwości publikacji (co najmniej raz na 2 tygodnie) i procesu redakcji

---

## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Organizacja #Narzędzia #Problem

- **Azure DevOps AI Generator:** Zgłoszono problem z działaniem narzędzia (wywala się przy "regenerator work items"). Diagnoza i naprawa wymagana.
- **Podsumowania Rad Architektów:** Zatwierdzono generowanie podsumowań AI z każdej Rady (struktura: kontekst, ryzyka, decyzje, zadania) na podstawie transkrypcji, jako lepszą alternatywę dla standardowego Copilota.

---

## 2025-09-02 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-09-02 Rada architektów|2025-09-02 Rada architektów]]

**Kategoria:** #Organizacja #Narzędzia

**Kontekst:**
Janusz przedstawił szczegółową metodę tworzenia dokumentacji projektowej z wykorzystaniem AI, która znacznie przyspiesza proces od pomysłu do realizacji. Problem polega na tym, że zespół dużo mówi podczas spotkań (szkolenia, Daily, retrospekcje), ale mało z tego wykorzystuje – transkrypcje są nagrywane, ale nie są przetwarzane na ustrukturyzowaną dokumentację.

### Metoda tworzenia dokumentacji z AI - szczegóły

**Proces (rozszerzony):**

1. **Nagranie transkrypcji:**
   - Użycie narzędzia Super Whisper do nagrywania i automatycznej transkrypcji
   - Mówienie naturalnym językiem (z zająknięciami, dygresjami – AI to wyczyści)

2. **Przetwarzanie przez AI:**
   - Użycie odpowiedniego promptu w zależności od typu dokumentu:
     - **Przegląd funkcjonalności** – opis funkcjonalności, jej przeznaczenia, problemów które rozwiązuje
     - **Poradnik how-to** – instrukcja krok po kroku dla użytkownika końcowego
     - **Poradnik how-to dla administratora** – bardziej techniczny, dla administratorów
     - **Artykuł koncepcyjny** – omówienie szerszej idei
     - **FAQ** – odpowiedzi na konkretne pytania (np. "Nie widzę Copilota, co mam zrobić?")
     - **Artykuł techniczny** – dogłębna wiedza techniczna

3. **Standaryzacja słownictwa:**
   - Utworzenie słownika w Google Sheets (lub podobnym narzędziu)
   - Słownik zawiera mapowanie: jak mówimy → jak powinno być w dokumentacji
   - Przykład: "procedura, proces, workflow, przepływ pracy" → "procesy"
   - Słownik jest dołączany do promptu, aby AI używało ustandaryzowanego słownictwa

4. **Zasady:**
   - **Jeden artykuł = jeden temat** (nie łączyć wielu funkcjonalności w jeden artykuł)
   - Artykuły powiązane są linkowane między sobą
   - Przykład: zamiast jednego artykułu "Nowy sidebar" z wszystkimi funkcjonalnościami, osobne artykuły: "Jak wyszukać w menu", "Jak zwinąć menu", "Jak przypiąć raport"

### Narzędzia

- **Nagrywanie + transkrypcja:** Super Whisper
- **AI:** Copilot, Gemini, v0 (przetwarzanie transkrypcji)
- **Format promptu:** "Jesteś ekspertem od komunikacji produktowej. Przekształć surową transkrypcję w ustrukturyzowany artykuł..."
- **Słownik:** Google Sheets (lub podobne) z mapowaniem terminów
- **Publikacja:** Azure DevOps Wiki

### Korzyści

- Skraca czas od pomysłu do realizacji **dziesięciokrotnie lub więcej**
- Mówienie jest **5x szybsze** niż pisanie
- Automatyczne czyszczenie transkrypcji (AI usuwa zająknięcia, dygresje)
- Standaryzacja słownictwa dzięki słownikowi terminów
- Dostępność dla każdego członka zespołu

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie metody tworzenia dokumentacji z wykorzystaniem AI jako standardowego narzędzia w zespole.

### Zadania

- **Janusz Bossak:** Udostępnienie promptów dla różnych typów artykułów zespołowi (wykonane podczas spotkania)
- **Wszyscy:** Rozpoczęcie tworzenia dokumentacji metodą AI (natychmiast)
- **Janusz Bossak:** Utworzenie i udostępnienie słownika terminów w Google Sheets (w trakcie)

### Punkty otwarte

- Jak często aktualizować słownik terminów?
- Czy potrzebny jest proces review wygenerowanych artykułów przed publikacją?
- Jak obsłużyć przypadki, gdy AI zadaje pytania do eksperta (format "Pytanie do eksperta")?

---

## 2025-08-29 - Planowanie sprintu

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-29 Planowanie sprintu-codex|2025-08-29 Planowanie sprintu-codex]]

**Kategoria:** #Organizacja #Narzędzia

**Kontekst:**
W ramach rozwiązania problemu braku dokumentacji projektowej, wprowadzono metodę tworzenia dokumentacji z wykorzystaniem AI. Janusz przetestował tę metodę i potwierdził jej skuteczność.

### Metoda tworzenia dokumentacji z AI

**Proces:**
1. Przygotowanie strony/funkcjonalności do dokumentowania
2. Nagranie spotkania sam na sam (Teams) z opisem funkcjonalności
3. Transkrypcja nagrania
4. Prompt do AI: "Jesteś ekspertem od tworzenia dokumentacji technicznej. Przekształć surową transkrypcję w przejrzysty artykuł how-to."
5. AI generuje ustrukturyzowaną dokumentację
6. Publikacja na Wiki

### Zasady

- **Opisuj pojedynczą funkcjonalność** - nie globalne artykuły
- **Zbieraj artykuły w katalogi tematyczne** (np. "Nowe menu boczne")
- **Każdy artykuł:** instrukcja krok po kroku + wskazówki i dobre praktyki
- **Nie wymagaj perfekcjonizmu** - lepiej mieć coś (20/80) niż nic (zasada 4x10)

### Przykład

"Jak szybko znaleźć pozycję w menu za pomocą wyszukiwarki?" – artykuł how-to z instrukcją krok po kroku.

### Korzyści

- Szybkie tworzenie dokumentacji (metoda nagrania jest szybsza niż pisanie)
- Dostępność dla każdego członka zespołu (nie tylko technical writerów)
- Ustrukturyzowana dokumentacja dzięki AI
- Łatwiejsze przekazywanie wiedzy

### Kontekst problemu

**Ryzyko/Bloker:** Brak dokumentacji projektowej
- **Wpływ:** Średni
- **Mitygacja:** Wykorzystanie AI do generowania dokumentacji z transkrypcji (metoda nagrania + prompt)
- **Właściciel:** Wszyscy członkowie zespołu


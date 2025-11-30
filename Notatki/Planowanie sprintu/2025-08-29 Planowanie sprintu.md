# Planowanie Sprintu – 2025-08-29

**Sprint:** [nie określono]
**Okres:** [nie określono]

**Uwaga:** Spotkanie zostało przerwane z powodu pilnych zadań związanych z WIM. Główna część spotkania dotyczyła problemów organizacyjnych działu i metodologii pracy, a nie konkretnego planowania zadań na sprint.

**Powiązane projekty:**
- `Notatki/Organizacja działu DEV/` – tematy 1-5 (reorganizacja działu, metodologia)
- `klienci/WIM` – temat 6 (pilne zadania)

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| [Brak informacji] | - | - | Spotkanie nie dotarło do omówienia statusu |

---

## 2. Plany na sprint

**Uwaga:** Ze względu na przerwanie spotkania i pilne zadania związane z WIM, konkretne plany na sprint nie zostały omówione.

### WIM – pilne zadania

**Projekt:** `klienci/WIM`

**Kontekst i cel:**
Pilne zadania związane z wersją dla klienta WIM wymagają natychmiastowej uwagi. Zespół (Kamil, Damian) musi przełączyć się na te zadania, co wpływa na planowanie sprintu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| [Nie określono szczegółów] | **Kamil**, **Damian** | [Nie określono] | Pilne, wymaga natychmiastowej uwagi |

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Wszystkie zadania i bugi muszą być w Azure DevOps | `Notatki/Organizacja działu DEV/` | ✅ Zatwierdzone | Brak odstępstw od standardu – wszystko w Azure, bez Exceli/Wordów |
| Projekty opisujemy na Wiki, zadania na backlogu | `Notatki/Organizacja działu DEV/` | ✅ Zatwierdzone | Backlog to zadania do zrobienia, nie miejsce na opis projektu |
| Feature'y muszą mieć początek i koniec | `Notatki/Organizacja działu DEV/` | ✅ Zatwierdzone | Feature to funkcjonalność do dostarczenia, nie nieskończony opis |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Chaos w organizacji pracy | `Notatki/Organizacja działu DEV/` | Wysoki | Retrospekcja w poniedziałek 9:00-12:00, reorganizacja działu | **Janusz** |
| Brak zaangażowania testerek w projekty | `Notatki/Organizacja działu DEV/` | Wysoki | Wprowadzenie modelu "Trójki Amigos" (projektant, deweloper, tester) | **Janusz** |
| Brak dokumentacji projektowej | `Notatki/Organizacja działu DEV/` | Średni | Wykorzystanie AI do generowania dokumentacji z transkrypcji | **Wszyscy** |
| Zbyt duża ilość zadań, brak czasu | `Notatki/Organizacja działu DEV/` | Wysoki | Ustawienie priorytetów, obrona przed strumieniem zadań | **Janusz**, **Damian**, **Kamil** |
| Pilne zadania WIM przerywają planowanie | `klienci/WIM` | Średni | [Nie określono] | - |

---

## 5. Organizacja pracy

### Retrospekcja i reorganizacja działu

**Data:** Poniedziałek, [data następnego tygodnia]
**Godzina:** 9:00-12:00
**Cel:** Dyskusja o reorganizacji działu, organizacji projektów, tworzeniu dokumentacji projektowej, zarządzaniu

**Uczestnicy:** Cały zespół DEV

**Przygotowanie:** Każdy powinien przygotować się do spotkania, przemyśleć problemy i zaproponować konstruktywne rozwiązania.

### Metodologia pracy – wprowadzone zmiany

#### Model "Trójki Amigos" (Three Amigos)

**Opis:** Dla każdego większego projektu tworzony jest zespół składający się z:
- **Projektant** (od strony biznesowej): Łukasz, Damian, Kamil, Janusz
- **Deweloper** (od strony technicznej)
- **Tester** (od strony UX i funkcjonalnej): Barbara, Oktawia, Patrycja

**Zasady:**
- Zespół jest formalnie ogłaszany
- Odpowiedzialny za dowiezienie projektu jest lider (np. Damian)
- Zespół ma za zadanie najpierw zrobić projekt (koncepcję), potem wytworzenie
- Wszyscy członkowie zespołu wiedzą o zmianach w trakcie wytwarzania
- Testerki będą angażowane w spotkania projektowe przed rozpoczęciem prac

**Przykłady projektów:**
- Komunikator (AMODIT Talk)
- Repozytorium dla WIM
- Process Builder (Edytor procesów)
- Edytor diagramów
- Edytor reguł
- WCAG

#### Specjalizacja testerek

- **Barbara** – specjalistka od modułu raportowego
- **Oktawia** – specjalistka od e-Doręczeń
- **Patrycja** – specjalistka od e-podpisów

**Uwaga:** Specjalizacja nie wyklucza innych testerek z danego tematu, ale zapewnia eksperta w danej dziedzinie.

### Dokumentacja projektowa

#### Metoda tworzenia dokumentacji z AI

**Proces:**
1. Przygotowanie strony/funkcjonalności do dokumentowania
2. Nagranie spotkania sam na sam (Teams) z opisem funkcjonalności
3. Transkrypcja nagrania
4. Prompt do AI: "Jesteś ekspertem od tworzenia dokumentacji technicznej. Przekształć surową transkrypcję w przejrzysty artykuł how-to."
5. AI generuje ustrukturyzowaną dokumentację
6. Publikacja na Wiki

**Zasady:**
- Opisuj pojedynczą funkcjonalność, nie globalne artykuły
- Zbieraj artykuły w katalogi tematyczne (np. "Nowe menu boczne")
- Każdy artykuł: instrukcja krok po kroku + wskazówki i dobre praktyki
- Nie wymagaj perfekcjonizmu – lepiej mieć coś niż nic (zasada 4x10, 20/80)

**Przykład:** "Jak szybko znaleźć pozycję w menu za pomocą wyszukiwarki?" – artykuł how-to z instrukcją krok po kroku.

### Standardy pracy w Azure DevOps

#### Zasady bezwzględne

1. **Wszystko w Azure DevOps:**
   - ✅ Wszystkie zadania, bugi, feature'y w Azure DevOps
   - ❌ Brak odstępstw: Excel, Word, czat, inne narzędzia
   - Uzasadnienie: możliwość wyszukiwania, śledzenia historii, przejęcia przez innych

2. **Struktura w Azure DevOps:**
   - **Epic** – duży projekt (np. "Komunikator")
   - **Feature** – funkcjonalność do dostarczenia (musi mieć początek i koniec, Definition of Done)
   - **PBI** – zadanie do zrobienia (oszacowane czasowo)
   - **Bug** – błąd powiązany z Feature/PBI

3. **Wiki vs Backlog:**
   - **Wiki** – miejsce na opis projektu, koncepcję, dokumentację
   - **Backlog** – miejsce na zadania do zrobienia (z oszacowaniem, kryteriami akceptacji)

#### Przykłady błędnych praktyk (do unikania)

- ❌ Feature "Raport Gantta" – nie mówi co i kiedy się skończy
- ✅ Feature "Wprowadzić w raporcie Gantta funkcjonalność X" – jasno określa zakres i koniec
- ❌ Feature "Komunikator" jako nieskończony opis
- ✅ Epic "Komunikator" z Feature'ami opisującymi konkretne funkcjonalności

#### Przygotowanie testów dla nowych projektów

**Dla komunikatora (przykład):**
- Jeden zbiorczy Feature/PBI opisujący całą aplikację i jej ścieżki
- Jeśli testerka znajdzie błędy – tworzy Bug powiązany z Feature
- Jeśli Feature jest rozszerzany – tworzy się nowy Feature/PBI

**Uwaga:** Nie tworzyć Feature do Feature – używać Epic lub powiązanych Feature'ów.

---

## 6. Uwagi organizacyjne

### Problemy zidentyfikowane

1. **Chaos w organizacji:**
   - Testerki nie są brane do pracy nad projektami tak jak do modułu raportowego
   - Testerki są na końcu procesu, nie wiedzą co ma robić
   - Zadania przychodzą w Excelu zamiast w Azure DevOps
   - Brak zaangażowania w projektowanie

2. **Przeciążenie pracą:**
   - Zbyt duża ilość zadań
   - Brak czasu na przygotowanie ofert/projektów
   - Pilne zadania przerywają planowanie
   - Trudność w obronie przed strumieniem zadań

3. **Brak dokumentacji:**
   - Brak podstawowej dokumentacji funkcjonalnej
   - Trudność w przekazywaniu wiedzy
   - Brak standardów tworzenia dokumentacji

### Planowane działania

1. **Retrospekcja w poniedziałek 9:00-12:00:**
   - Dyskusja o reorganizacji działu
   - Organizacja projektów
   - Tworzenie dokumentacji projektowej
   - Zarządzanie

2. **Wprowadzenie modelu "Trójki Amigos":**
   - Formalne ogłaszanie zespołów projektowych
   - Zaangażowanie testerek od początku projektu

3. **Wykorzystanie AI do dokumentacji:**
   - Każdy członek zespołu może tworzyć dokumentację metodą nagrania + AI
   - Publikacja na Wiki

4. **Utrzymanie standardów Azure DevOps:**
   - Bezwzględne trzymanie się Azure DevOps
   - Brak odstępstw na Excel/Word/czat

---

## 7. Uczestnicy spotkania

- **Łukasz Bott** – Management/Analiza
- **Kamil Dubaniowski** – Management/Analiza
- **Damian Kamiński** – Management/Analiza
- **Janusz Bossak** – Management/Analiza
- **Barbara Michałek** – QA/Testy
- **Przemysław Sołdacki** – Frontend
- **Adrian Kotowski** – Backend/Fullstack
- **Piotr Buczkowski** – Architekt/Fullstack
- **Mateusz Kisiel** – Backend/Fullstack
- **Filip Liwiński** – Frontend

---

## 8. Następne kroki

1. **Przygotowanie do retrospekcji:**
   - Każdy członek zespołu powinien przygotować się do spotkania
   - Przemyśleć problemy i zaproponować konstruktywne rozwiązania
   - Janusz napisze post na Teams z instrukcjami przygotowania

2. **Kontynuacja planowania sprintu:**
   - Spotkanie zostało przerwane z powodu pilnych zadań WIM
   - Planowanie może być kontynuowane później lub na Design (12:30)

3. **Wdrożenie zmian metodologicznych:**
   - Wprowadzenie modelu "Trójki Amigos" dla nowych projektów
   - Utrzymanie standardów Azure DevOps
   - Rozpoczęcie tworzenia dokumentacji metodą AI


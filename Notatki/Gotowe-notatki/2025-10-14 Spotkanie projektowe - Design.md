# Notatka projektowa – 2025-10-14 – Design

**Data:** 2025-10-14
**Temat główny:** Wizja AI-driven workflow i mechanizm changelog

**Powiązane projekty:**
- `koncepcje/AI-driven-workflow` – funkcjonalność 1
- `backlog` – funkcjonalność 2

---

## 1. Wizja AMODIT jako systemu AI-driven workflow

**Projekt:** `koncepcje/AI-driven-workflow`
**Komponent:** Koncepcja strategiczna

### Cel i problem

Dyskusja nad długoterminową wizją rozwoju AMODIT w kierunku systemu opartego na agentach AI. Obecnie wiele funkcjonalności realizowanych jest poprzez deterministyczne reguły i skomplikowane algorytmy. Celem jest identyfikacja miejsc, gdzie zastosowanie AI może przyspieszyć wdrożenia i uprościć implementację, przy jednoczesnym zachowaniu deterministycznych rozwiązań tam, gdzie to ma sens.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pełna zamiana workflow na AI | Całkowite zastąpienie deterministycznych procesów przez agentów AI | ❌ Odrzucona – workflow nie zostanie całkowicie zastąpiony |
| Selektywne zastosowanie AI | Wstawianie agentów AI w wybrane miejsca workflow, gdzie ma to sens | ✅ Wybrana – podejście hybrydowe |
| Zachowanie status quo | Pozostanie przy deterministycznych rozwiązaniach | ❌ Odrzucona – AI jest przyszłością |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja

Wizja długoterminowa: AMODIT jako system AI-driven workflow, gdzie agenci AI są wstawiani w różne miejsca procesu, zwracają strukturę danych, która jest następnie wykorzystywana w dalszych krokach workflow.

**Przykłady istniejących agentów:**
- **OCR** – agent, który otrzymuje fakturę/paragon, decyduje który model użyć (fakturowy/paragonowy), wykonuje preprocessing i postprocessing, zwraca ustrukturyzowane dane
- **Analiza RODO** – jednokrokowy agent: wrzucenie tekstu dokumentu → otrzymanie analizy/danych

**Propozycje nowych zastosowań:**
- **Matryce akceptacji** – agent otrzymujący informacje o zasadach akceptacji (deterministycznych i niedeterministycznych), parametry z case'a, zwracający strukturę odpowiedzi wykorzystywaną do przesłania sprawy na kolejny etap/do kolejnych osób
- **Przetwarzanie backlogu** – agent przetwarzający backlog, pobierający dane, przetwarzający i publikujący na WordPressie
- **Klasyfikacja maili** – podobnie jak systemy antyspamowe, kontekstowa analiza i klasyfikacja

**Szczegóły techniczne:**
- Function calling jako pierwotna wersja agenta (obecnie używane w kontekście "baza wiedzy - cenniki")
- Agenty mogą być wielokrokowymi workflow opartymi o AI (inspiracja: OpenAI workflow builder)
- Agenty zwracają strukturę danych, która jest następnie przetwarzana w AMODIT

### Ograniczenia / Poza zakresem

- Nie wszystkie funkcjonalności będą zastąpione przez AI – workflow pozostanie hybrydowy
- Nie wszystkie deterministyczne rozwiązania będą zamienione – niektóre pozostaną bez zmian

### Punkty otwarte

- Jak szybko można wdrażać AI w różnych miejscach AMODIT?
- Które funkcjonalności są najlepszymi kandydatami do zastąpienia przez agentów AI?
- Jak zbalansować deterministyczne i niedeterministyczne rozwiązania?

---

## 2. Mechanizm generowania i publikacji changelog

**Projekt:** `backlog`
**Komponent:** Dokumentacja produktu

### Cel i problem

Usprawnienie procesu generowania i publikacji changelog dla wersji AMODIT. Obecnie proces jest manualny i czasochłonny. Celem jest stworzenie narzędzia do półautomatycznego generowania changelog na podstawie zgłoszeń z Azure DevOps, z możliwością weryfikacji i redakcji przed publikacją.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pełna automatyzacja bez weryfikacji | Automatyczne generowanie i publikacja bez przeglądu | ❌ Odrzucona – wymagana weryfikacja przed publikacją |
| Półautomatyzacja z weryfikacją | Narzędzie generuje changelog, wymaga przeglądu i redakcji przed publikacją | ✅ Wybrana – zachowuje kontrolę jakości |
| Manualne przygotowanie | Pozostanie przy całkowicie manualnym procesie | ❌ Odrzucona – zbyt czasochłonne |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Mechanizm działania:**
- Narzędzie w AMODIT (odtworzenie Azure DevOps w uproszczonej formie) do zarządzania changelog
- Pobieranie zgłoszeń z Azure DevOps oznaczonych jako Done i przypisanych do konkretnej release version
- Generowanie changelog przez AI na podstawie zgłoszeń
- Możliwość filtrowania i redakcji przed publikacją

**Kryteria włączenia do changelog:**
- Zgłoszenie musi być w statusie Done
- Zgłoszenie musi być oznaczone konkretną release version
- Tylko zgłoszenia spełniające powyższe kryteria są uwzględniane

**Format changelog:**
- Sucha lista zmian (podobnie jak changelog Debiana, Linuxa)
- Opcjonalnie linki do szczegółów dla ważniejszych zmian
- Format: "Poprawiono...", "Dodano...", "Rozszerzono...", "Zmieniono..."
- Dla poprawek bezpieczeństwa: ogólne sformułowanie "poprawki bezpieczeństwa" bez szczegółów

**Częstotliwość publikacji:**
- Co najmniej raz na 2 tygodnie (na początku kolejnego sprintu za poprzedni sprint)
- Synchronizacja z publikacją wersji przez Michała Zwierzchowskiego
- Wydania pośrednie (hotfixy) publikowane offline'owo, nie w publicznym changelog

**Szczegóły techniczne:**
- Narzędzie w AMODIT: raport z możliwością filtrowania po wersji
- Eksport do formatu tekstowego do publikacji na Wiki
- Możliwość różnicowania formatu opisu w zależności od typu zgłoszenia (PBI, bug, hotfix)
- Automatyczne usuwanie nazw własnych klientów z changelog
- Możliwość dodania kolumny z datą publikacji (opcjonalnie)

**Proces redakcji:**
- Wygenerowany changelog wymaga przeglądu przed publikacją
- Usuwanie informacji, którymi nie chcemy się "chwalić" (np. nasze błędy, niejasne opisy)
- Dla funkcjonalności typu "Dodano", "Rozszerzono" – wymagane utworzenie artykułu dokumentacyjnego z linkiem
- Dla poprawek – link do artykułu tylko jeśli poprawka rozszerza funkcjonalność

**Perspektywy changelog:**
- **Perspektywa wersji** (zaimplementowana): "Co jest w wersji X?" – lista zmian dla konkretnej wersji
- **Perspektywa funkcjonalna** (do rozważenia): "Co się zmieniło w raportach?" – grupowanie po modułach/funkcjonalnościach
- **Perspektywa czasowa** (do rozważenia): Data publikacji wersji
- **Perspektywa poprawki** (odrzucona): "Do której wersji trafiła poprawka X?" – konsultanci mogą sprawdzić w backlogu Azure DevOps

### Ograniczenia / Poza zakresem

- Nie wszystkie commity są uwzględniane – tylko te związane ze zgłoszeniami oznaczonymi jako Done z release version
- Commity bez przypisania do zgłoszenia nie są uwzględniane w changelog
- Hotfixy nie są publikowane w publicznym changelog (tylko wydania główne)
- Numeracja zgłoszeń (PBI) nie jest ujawniana w publicznym changelog

### Punkty otwarte

- Czy dodać datę publikacji do numeru wersji w changelog?
- Jak obsługiwać przypadki, gdy commit jest zmergowany, ale zgłoszenie nie jest oznaczone jako Done?
- Czy potrzebna jest dodatkowa automatyzacja (np. automatyczne uzupełnianie numeru wersji na Wiki)?

---

## Propozycja podziału na pakiety prac (MVP)

Nie dyskutowano priorytetyzacji w kontekście MVP.

---

## Punkty do dalszej dyskusji (globalne)

- Weryfikacja z Michałem Zwierzchowskim i Piotrem Buczkowskim: jak obsługiwać commity, które są zmergowane, ale zgłoszenie nie jest oznaczone jako Done?
- Ustalenie szczegółów procesu redakcji changelog (kto odpowiada za weryfikację, jak często publikować)
- Rozważenie dodatkowych perspektyw changelog (funkcjonalna, czasowa) w przyszłości


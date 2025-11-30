# Project Canvas: News Feed / Anonse

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-11
**Klient:** WIM
**Data rozpoczęcia:** 2025-08-19

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Janusz Bossak | Wymagania |
| **Tech Lead** | Adrian Kotowski | Analiza techniczna |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klient WIM potrzebuje prostego, ale skutecznego mechanizmu do komunikacji wewnętrznej - wyświetlania ogłoszeń, newsów czy ważnych komunikatów dla wszystkich użytkowników systemu. Obecnie brakuje dedykowanego narzędzia, a informacje przekazywane są mailowo lub poprzez inne, rozproszone kanały. Dodatkowo, istnieje potrzeba przywrócenia i rozbudowy starego mechanizmu "info bar" do wyświetlania statycznych komunikatów systemowych.

### Cel biznesowy
Usprawnienie komunikacji wewnętrznej w firmie klienta poprzez dostarczenie centralnego miejsca do publikacji ogłoszeń. Zwiększenie widoczności ważnych informacji i zapewnienie, że dotrą one do wszystkich pracowników.

### Cel techniczny
Zaprojektowanie i wdrożenie mechanizmu "News Feed" lub "Tablicy Ogłoszeń". Rozważane są dwa podejścia: realizacja za pomocą dedykowanego procesu AMODIT lub budowa nowej, dedykowanej funkcjonalności. Dodatkowo, należy przywrócić stary mechanizm "info bar" i dostosować go do nowych wymagań.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasłudnienie |
|----|--------|------|---------|---------------|
| ADR-001 | 💡 Propozycja | [[2025-08-19]] | Realizacja funkcjonalności "Tablicy Ogłoszeń" za pomocą dedykowanego procesu AMODIT. | Szybkie wdrożenie, wykorzystanie istniejących mechanizmów, elastyczność w definiowaniu procesu publikacji. |
| ADR-002 | 💡 Propozycja | [[2025-08-19]] | Wyświetlanie ogłoszeń na stronie głównej (dashboardzie) użytkownika. | Najlepsza widoczność, użytkownik widzi ogłoszenia od razu po zalogowaniu. |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-11]] | Stary mechanizm "info bar" zostanie przywrócony i rozbudowany. | Jest to rozwiązanie prostsze i szybsze do wdrożenia dla statycznych komunikatów niż budowa pełnego News Feeda. |
| ADR-004 | 💡 Propozycja | [[2025-09-11]] | Docelowo "info bar" będzie obsługiwał format HTML, ale ze względów bezpieczeństwa treści będą wyświetlane w `iframe sandbox`. | Pozwoli to na elastyczne formatowanie komunikatów, jednocześnie chroniąc system przed potencjalnymi atakami XSS. |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-08-19]] | Utworzenie projektu w odpowiedzi na zapotrzebowanie klienta WIM na mechanizm do wewnętrznych ogłoszeń. | [[2025-08-19 Rada architektów]] |
| [[2025-09-11]] | Dyskusja nad przywróceniem starego mechanizmu "info bar". Podjęto decyzję o jego reaktywacji jako prostszej alternatywy dla pełnego "News Feed". Zaplanowano rozbudowę o obsługę HTML w bezpiecznym `iframe`. | [[2025-09-11 Rada architektów]] |

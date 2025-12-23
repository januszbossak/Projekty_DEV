# Projekt: Historia Biznesowa (Rossmann)

## Status
- **Faza:** Koncepcja / Design
- **Sponsor:** Rossmann
- **Opiekun:** [Do uzupełnienia]

## Opis projektu
Historia Biznesowa to mechanizm monitorowania przebiegu sprawy biznesowej w systemie AMODIT, zaprojektowany w formie interaktywnego timeline'u wizualizującego chronologię kluczowych zdarzeń biznesowych. Stanowi warstwę analityczną nad standardowym audit trail, agregując dane z wielu powiązanych formularzy.

## Kluczowe Funkcjonalności
- **Interaktywny Timeline:** Chronologiczna wizualizacja zdarzeń (kropki połączone linią).
- **Agregacja wieloprocesowa:** Łączenie zdarzeń z powiązanych spraw (np. e-Doręczenia -> Obieg właściwy).
- **Kolorowe kodowanie:** Wizualne rozróżnienie procesów biznesowych.
- **Wyszukiwarka i Filtrowanie:** Pełnotekstowe przeszukiwanie historii i filtrowanie po typie zdarzenia/procesu.
- **Kafelki szczegółów:** Dowolna treść merytoryczna dostępna po kliknięciu "Pokaż szczegóły".

## Architektura i Konfiguracja
- **Warstwa techniczna:** Wykorzystuje mechanizm `connectedCase` i tabelę `CaseEventBusinessSubjects`.
- **Konfiguracja:** Wykonywana przez wdrożeniowca za pomocą *Amodit Script*.
- **Integracja UI:** Prawy sidebar, dedykowana zakładka obok historii szczegółowej.

## Roadmapa / MVP
- **MVP 1:** Tabela powiązań, mechanizm `connectedCase`, lista chronologiczna.
- **MVP 2:** Wyszukiwarka, kolorowanie, kafelki szczegółów.

## Materiały
- [Notatka koncepcyjna (2025-12-22)](../../../Notatki/Gotowe-notatki/2025-12-22%20Historia%20biznesowa%20dla%20Rossmann)
- [Mockup Figma](https://grow-silver-08622037.figma.site/)

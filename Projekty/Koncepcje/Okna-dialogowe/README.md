# Okna dialogowe

**Klient:** AMODIT (roadmapa)
**Status:** 🟡 W analizie
**PDM:** [do uzupełnienia]
**Tech Lead:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Okna-dialogowe]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP (trzy warianty okien dialogowych)
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Obecny mechanizm zbierania danych od użytkownika w trakcie wykonywania procesu jest zbyt ograniczony. Okno potwierdzania reguły ręcznej nie pozwala na zbieranie wielu pól danych, co uniemożliwia realizację bardziej złożonych scenariuszy interakcji z użytkownikiem bez konieczności tworzenia pełnej sprawy.

### Rozwiązanie

Wprowadzenie elastycznego mechanizmu okien dialogowych w trzech wariantach o różnym poziomie złożoności:
- **Wariant 1:** Proste okno dialogowe (bez procesu) - pola definiowane w wywołaniu
- **Wariant 2:** Okno na podstawie formularza (proces-formularz) - bez tworzenia sprawy
- **Wariant 3:** Okno na podstawie procesu (pełny proces) - z persystencją spraw

### Obecna faza

📋 **W analizie** - koncepcja wymaga dalszego sprecyzowania wymagań

**Ukończono:**
- ✅ Zdefiniowano trzy warianty okien dialogowych
- ✅ Określono podstawowe założenia techniczne (funkcja `ShowDialog()`, format JSON)

**W trakcie:**
- Szczegółowa specyfikacja wymagań dla prostego okna dialogowego
- Określenie sposobu konsumpcji danych z okna dialogowego

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Trzy warianty okien dialogowych** | Różne scenariusze użycia wymagają różnych poziomów złożoności - od prostych pytań po zaawansowane formularze |
| **Uproszczony interfejs** | Okno dialogowe bez prawego panelu, załączników, historii - szybka interakcja bez przeładowania |
| **Format JSON** | Elastyczność w przetwarzaniu danych i łatwa integracja z istniejącymi mechanizmami systemu |

---

## MVP1: Proste okno dialogowe

**Cel:** Najprostszy mechanizm zbierania danych bez definiowania procesu

**Zakres:**
- [ ] Funkcja `ShowDialog()` z polami w wywołaniu
- [ ] Obsługa typów pól: tekst, data, liczba, użytkownik, słownik
- [ ] Zwracanie danych jako JSON
- [ ] Uproszczony interfejs

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Brak jasnej definicji formatu danych JSON | Przeprowadzenie szczegółowej analizy wymagań przed implementacją |
| Nieokreślone akcje w oknie dialogowym | Zdefiniowanie minimalnego zestawu akcji dla każdego wariantu |

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]

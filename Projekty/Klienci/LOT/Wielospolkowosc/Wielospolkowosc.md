# Wielospółkowość

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |
| **Opiekun handlowy** | | |
| **Kontakt u klienta** | | |

**Klient:** LOT
**Status:** W analizie (przeniesione do backlogu)
**Data rozpoczęcia:** 2025-10-07
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

W środowisku LOT na jednej instancji AMODIT pracują różne, odseparowane od siebie spółki. Istnieje ryzyko, że pracownik jednej firmy będzie mógł przypadkowo lub celowo udostępnić sprawę osobie z innej spółki.

### Cel projektu

Zapewnienie pełnej separacji danych i użytkowników między spółkami pracującymi na tej samej instancji systemu.

---

## 2. Problem

**Status:** Do analizy (wymaga szczegółowych wymagań)
**Data zgłoszenia:** 2025-10-07

### Zakres problemu

Problem dotyczy wszystkich miejsc w systemie, gdzie wybierany jest użytkownik:
- Panel współwłaścicieli i obserwatorów
- Pola typu `Użytkownik`
- Akcja `Przekaż do`
- Widoczność w panelu administracyjnym
- Raporty

### Proponowane rozwiązania

**Propozycja początkowa:**
- Dodanie na poziomie procesu możliwości ograniczenia listy dostępnych współwłaścicieli/obserwatorów do wybranej grupy

**Propozycja po dyskusji:**
- Kompleksowe, architektoniczne rozwiązanie problemu "wielospółkowości"
- Wprowadzenie w strukturze organizacyjnej możliwości oznaczenia, który poziom definiuje "spółkę"
- Automatyczne filtrowanie list użytkowników na podstawie przynależności do tej samej jednostki
- Separacja danych w całej aplikacji

### Decyzja (2025-10-07)

- Temat zbyt szeroki na doraźne rozwiązanie
- Wymaga głębszej analizy i zaprojektowania spójnego mechanizmu "wielospółkowości"
- Zgłoszenie przeniesione do backlogu
- Ponowna analiza gdy pojawią się konkretne i szczegółowe wymagania od klienta

---

## 3. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-10-07 | Zidentyfikowano problem separacji użytkowników między spółkami - do backlogu | Rada Architektów 2025-10-07 |

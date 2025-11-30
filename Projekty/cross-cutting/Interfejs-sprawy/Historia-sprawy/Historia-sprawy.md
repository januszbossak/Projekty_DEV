# Project Canvas: Historia sprawy

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-11
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-09-11

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead**| Piotr Buczkowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Obecnie w logu historii sprawy zmiany na polach formularza są zapisywane z użyciem ich nazw systemowych (`FieldName`), a nie etykiet widocznych dla użytkownika (`DisplayValue`). Powoduje to, że historia jest nieczytelna dla użytkowników biznesowych, którzy nie znają nazw technicznych pól. Przykładowo, zmiana w polu "Kwota faktury" jest logowana jako zmiana w polu "FV_AMOUNT", co wymaga od użytkownika dodatkowej wiedzy do interpretacji zapisu.

### Cel biznesowy
Znacząca poprawa czytelności i użyteczności historii sprawy dla wszystkich użytkowników, a w szczególności dla użytkowników nietechnicznych. Zmiana ma na celu uczynienie logu bardziej intuicyjnym i zrozumiałym bez potrzeby znajomości technicznej budowy procesu.

### Cel techniczny
Zmiana mechanizmu logowania i prezentacji historii zmian pól tak, aby domyślnie wyświetlana była etykieta pola (`DisplayValue`). Nazwa techniczna (`FieldName`) powinna być nadal dostępna, np. w tooltipie po najechaniu na etykietę, w celu ułatwienia pracy deweloperom i administratorom.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasłudnienie |
|----|--------|------|---------|---------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-11]] | W historii sprawy domyślnie wyświetlana będzie etykieta pola (`DisplayValue`), a nazwa techniczna (`FieldName`) będzie dostępna w tooltipie. | Znacząco poprawia czytelność dla użytkowników biznesowych, jednocześnie zachowując dostęp do informacji technicznych dla deweloperów. Jest to kompromis między użytecznością a potrzebami technicznymi. |

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-11]] | Utworzenie projektu w odpowiedzi na zgłoszoną potrzebę poprawy czytelności historii sprawy. | [[2025-09-11 Rada architektów]] |

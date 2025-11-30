# Komunikaty systemowe

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting
**Status:** W analizie
**Data rozpoczęcia:** 2025-09-11
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Brak skutecznego, wbudowanego narzędzia do informowania wszystkich użytkowników o ważnych wydarzeniach (np. planowane przerwy techniczne), co prowadzi do nieporozumień.

### Cel projektu

Mechanizm statycznych komunikatów systemowych wyświetlanych dla wszystkich użytkowników po zalogowaniu.

---

## 2. Kontekst techniczno-architektoniczny

### Istniejąca implementacja

Istnieje częściowo zaimplementowany mechanizm, który pozwalał na wyświetlanie globalnych komunikatów. Wymaga dokończenia i dostosowania.

### Proponowane rozwiązanie

- Integracja z nowym interfejsem (React)
- Wyświetlanie w formie **zamykanego paska na górze ekranu** po zalogowaniu
- Zarządzanie komunikatami:
  - **Chmura** - scentralizowane zarządzanie, wykorzystanie istniejącego (nieużywanego w nowym UI) mechanizmu
  - **On-premise** - nowa funkcjonalność: pole w ustawieniach systemowych lub specjalny typ "powiadomienia systemowego" w module powiadomień

### Decyzja (2025-09-11)

Temat jest ważny i należy go zrealizować. W pierwszej kolejności konieczne jest zbadanie obecnego stanu implementacji.

### Decyzja (2025-09-16)

Funkcjonalność zostanie zrealizowana **po uzyskaniu finansowania** od zainteresowanych klientów (LPP, Rossmann).

---

## 3. Zadania

- [ ] **Ania:** Przeprowadzić research istniejącego rozwiązania, spisać możliwości i ograniczenia, przygotować rekomendacje
- [ ] **Łukasz:** Przejąć temat, przygotować wycenę i skontaktować się z klientami w sprawie finansowania

---

## 4. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-11 | Utworzenie projektu, decyzja o researchu | Rada Architektów 2025-09-11 |
| 2025-09-16 | Uszczegółowienie rozwiązania dla chmury/on-premise, decyzja o wycenie dla klientów | Rada Architektów 2025-09-16 |

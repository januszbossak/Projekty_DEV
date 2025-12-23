# CHANGELOG - Historia Biznesowa

Wszystkie ustalenia i zmiany dotyczące modułu Historii Biznesowej.

---

## 2025-12-22 | Uszczegółowienie koncepcji i UI
**Źródło:** [Notatki/Gotowe-notatki/2025-12-22 Historia biznesowa dla Rossmann](../../../Notatki/Gotowe-notatki/2025-12-22%20Historia%20biznesowa%20dla%20Rossmann)
**Kategoria:** #Design #Funkcjonalność

- **Timeline:** Projekt graficzny jako kropki połączone linią, sekcje kolorowane wg procesów.
- **Interfejs:** Umiejscowienie w sidebare jako osobna zakładka obok audit trail.
- **Kafelki zdarzeń:** Definicja pól (nazwa, data, użytkownik, przycisk szczegółów).
- **Wyszukiwanie:** Wprowadzenie wyszukiwarki pełnotekstowej z highlightem na żółto.
- **Filtrowanie:** Dodanie filtrów po procesie i zdarzeniu.
- **Konfiguracja:** Potwierdzenie roli *Amodit Script* w definiowaniu zdarzeń i szczegółów.

---

## 2025-12-03 | Inicjalizacja koncepcji
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Notatka projektowa - Historia biznesowa.md]
**Kategoria:** #Architektura #Wymagania

- Identyfikacja problemu utraty historii przy przekazywaniu spraw między procesami.
- Decyzja o stworzeniu mechanizmu `connectedCase`.
- Projekt tabeli `CaseEventBusinessSubjects`.

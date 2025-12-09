# CHANGELOG - Zakładka Procesy

## 2025-11-12 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-12 Spotkanie projektowe - Przegląd wycen.md]
**Kategoria:** #Funkcjonalność #Design #Decyzja

- Filtr w lupce wyszukiwania procesów/raportów zostaje na stałe, powodując niewygodę.
- Filtr ma się czyścić po wylogowaniu/zalogowaniu oraz zamknięciu całego okna przeglądarki.
- Nie jest to hotfix, może być w następnym wydaniu.
- Rozważyć szerszą paczkę "poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach".

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Funkcjonalność

**Cel:**
Usprawnienie nawigacji i odnajdywania procesów poprzez nowy format wyświetlania oraz wprowadzenie modala pośredniego wspierającego wdrażanie nowych procesów.

### Nowy format wyświetlania

- Wydzielone ulubione, potem pozostałe
- Widok listy kafelkowej oraz listy kompaktowej
- Po prawej stronie od nazwy procesu może znajdować się opis (co ułatwia orientację)

### Modal pośredni

- Przed uruchomieniem sprawy pojawia się modal z opisem procesu (jeśli administrator zdefiniował opis)
- Modal może zawierać dowolną ilość kluczowych informacji merytorycznych
- Użytkownik może zaznaczyć, żeby modal więcej się nie pokazywał (jeśli proces jest mu znany)
- Dopiero po pojawieniu się modala można uruchomić sprawę

### Szczegóły techniczne

- Obszary przepisane na React
- Opisy dostępne z poziomu kafelków czy listy


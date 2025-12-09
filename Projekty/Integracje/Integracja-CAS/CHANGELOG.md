# CHANGELOG

Historia ustaleń i zmian dla projektu Integracja-CAS.

---

## 2025-11-07 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-07 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Architektura #Zadanie

- Piotr B. pracuje nad integracją z CAS.
- Celem jest centralna autentykacja, autoryzacja, tworzenie użytkowników i przypisywanie uprawnień.
- Piotr posiada kompletne wytyczne i opis; estymacja to kilka godzin pracy.
- Integracja umożliwi tworzenie użytkowników, przypisywanie uprawnień oraz ich aktualizację.

---

## 2025-11-06 | Wytyczne do projektu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-06 Wytyczne do projektu integracji AMODIT z CAS.md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- **Przepływ:** Autoryzacja przez CAS, tworzenie/aktualizacja użytkownika w AMODIT na podstawie danych z CAS (`GetFull`).
- **Grupy:** Automatyczna synchronizacja grup (wymagana zgodność nazw); użytkownicy usuwani z grup nieprzypisanych w CAS.
- **Administrator:** Rola nadawana lokalnie w AMODIT, niezależna od grup CAS.
- **Blokowanie:** Blokada w CAS uniemożliwia logowanie; blokada w AMODIT manualna.
- **Do decyzji:** Wybór modelu uprawnień (Pełna synchronizacja vs Mieszany), mapowanie dodatkowych pól, timeout sesji.
- **Ryzyka:** Opóźnienie aktualizacji danych (wymagane przelogowanie), brak automatycznego wylogowania (SLO do rozważenia).

---

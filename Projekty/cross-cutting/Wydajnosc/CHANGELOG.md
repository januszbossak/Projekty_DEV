# CHANGELOG – Wydajność

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Bug #Optymalizacja #Decyzja

- Problem z wydajnością List View 2.0 i formularzy: pobieranie wszystkich użytkowników/słowników przy wejściu (np. Enence: 200 000 użytkowników)
- Decyzja: Dane pobierane na żądanie (przy rozwinięciu filtra/menu) ze stronicowaniem i wyszukiwaniem

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Architektura #Optymalizacja

- Zmiana pól varchar na Medium Text w DatabaseAdmin w celu usunięcia ograniczenia długości pól tekstowych
- Funkcja generuje skrypt, obsługuje MS SQL i MySQL, wymaga wyłączenia aplikacji do wykonania

---

## 2025-09-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-16 Rada architektów - Przegląd projektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-16%20Rada%20architektów%20-%20Przegląd%20projektów.md)
**Kategoria:** #Wydajność #Problem

**Analiza wydajności bazy danych (On-Premise)** ✅
- **Problem:** Wolne działanie bazy, reguły wykonują się 1.5 minuty. Klient czekał 2 miesiące.
- **Decyzja:** ✅ Piotr Buczkowski (z Łukaszem Grodzkim) przeprowadzi 2-dniową analizę Time & Material.
- **Cel:** Identyfikacja przyczyn, sprawdzenie monitora wydajności, wnioski do wyceny naprawy.

# CHANGELOG - Komentarze

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Spotkanie projektowe - Błędy formularzy i procedury aktualizacji.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-03%20Spotkanie%20projektowe%20-%20Błędy%20formularzy%20i%20procedury%20aktualizacji.md)  
**Kategoria:** #Bug  
**Projekt:** [cross-cutting/GTA - dostęp tymczasowy do sparwy](../../GTA%20-%20dostęp%20tymczasowy%20do%20sparwy/)

- **Nieprawidłowa widoczność komentarzy dla użytkowników zewnętrznych/GTA** - sekcja komentarzy widoczna mimo braku konfiguracji
- **Klient:** Neuca (wersja czerwcowa)
- **Mechanizm:** `GrantTemporaryAccessToCase` (parametr `allowedButtons`), funkcja `HideElement`
- **Do weryfikacji:** Czy dotyczy użytkowników zewnętrznych (MSIT) czy tymczasowych (GTA), czy problem dotyczy tylko wyświetlania czy też możliwości edycji
- **Zadanie:** Kamil Dubaniowski + Eryk - weryfikacja i naprawa

---

# CHANGELOG – Trust-Center

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Przycisk zarządzania dokumentem i automatyczne wysyłanie kodu** ✅
- ❌ Odrzucone: Nazwa przycisku "Przejdź" - nieintuicyjna
- ❌ Odrzucone: Ręczne wprowadzenie maila - zwiększa liczbę kliknięć
- ✅ **Zatwierdzone:**
  1. **Zmiana nazwy przycisku:** "Zarządzaj dokumentem w Trust Center" (zamiast "Przejdź")
  2. **Walidacja użytkownika:** Weryfikacja czy użytkownik jest wysyłającym lub administratorem organizacji
  3. **Komunikat błędny:** "Skontaktuj się z administratorem" jeśli brak uprawnień
  4. **Automatyczne wysyłanie maila:** Kod dostępowy wysyłany automatycznie (bez ręcznego wprowadzenia)
  5. **Kompatybilność wsteczna:**
     - E-mail w query string (nowsze wersje) → automatyczne wysłanie kodu
     - Brak e-mail (starsze wersje) → pole do ręcznego wprowadzenia
- **Szczegóły:** Trust Center wymaga podniesienia wersji dla nowej funkcjonalności
- **Zadania:** Marek Dziakowski - implementacja

---


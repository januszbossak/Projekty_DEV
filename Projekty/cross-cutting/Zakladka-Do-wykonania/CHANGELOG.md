# CHANGELOG – Zakladka-Do-wykonania

---

## 2025-10-23 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Rada architektow.md]
**Kategoria:** #Funkcjonalność #Decyzja

- Zakładka "Do wykonania" ma się w ogóle nie wyświetlać w zakładce "Wszystkie procesy", niezależnie od konfiguracji obszarów.
- Zadanie przypisane do Piotra Buczkowskiego.

---

## 2025-09-04 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-04 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-04%20Rada%20architektów.md)
**Kategoria:** #Architektura #Decyzja

**Konfiguracja wyświetlania współpracowników na poziomie procesu** 🔍
- **Problem:** Klient WIM potrzebuje konfigurować per proces, czy współpracownicy widzą sprawy w "Do wykonania"
- Globalne ustawienie nie wystarcza (potrzeba elastyczności)
- ❌ Odrzucone: Konfiguracja odwrotna (NOT IN) - zbyt skomplikowane
- ❌ Odrzucone: Zarządzanie na poziomie obszaru - zbyt skomplikowane
- 🔍 **Do weryfikacji:** Konfiguracja na poziomie procesu (IN - lista procesów)
- **Ryzyka:** Wydajność przy dużej liście procesów (np. 100+) w zapytaniu SQL
- **Działania:** Damian sprawdzi skalę z klientem, Piotr zweryfikuje wydajność `IN`

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Zakładka "Do wykonania" – widoczność niezależnie od obszarów** ✅
- **Problem:** Zgłoszenie 21681 - zakładka znika gdy obszar "Wszystkie procesy" wyłączony
- Użytkownik może nie chcieć obszaru "Wszystkie procesy" (długa lista raportów), ale nadal potrzebuje globalnej zakładki "Do wykonania"
- ❌ Odrzucone: Zakładka zależna od obszaru (obecne podejście)
- ✅ **Zatwierdzone:** Zakładka "Do wykonania" zawsze widoczna, niezależnie od włączonych obszarów
- **Zawartość:** Wszystkie zadania z wszystkich procesów (jak w obszarze "Wszystkie procesy")
- **Logika:** Bez sprawdzania obszarów, wyświetla wszystkie zadania
- **Zadania:** Piotr Buczkowski - implementacja

---


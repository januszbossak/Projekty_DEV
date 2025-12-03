# CHANGELOG – GTA - dostęp tymczasowy do sparwy

---

## 2025-08-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-21 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-21%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Problemy z zarządzaniem dostępami GTA** 🔍
- **Problem:** Brak interfejsu do zarządzania dostępami - nie można przejrzeć kto ma dostęp do jakiej sprawy, od kiedy, do kiedy
- Dostęp można usunąć tylko z poziomu każdej sprawy osobno (brak centralnego zarządzania)
- Brak możliwości odbioru dostępu na życzenie (np. pomyłka, zmiana decyzji)
- **Ryzyka:** Problemy z RODO (kandydaci mogą żądać usunięcia danych), "wiszące" dostępy po zakończeniu procesu, problemy z bezpieczeństwem
- ❌ Odrzucone: Brak interfejsu (obecne podejście)
- 💡 **Propozycja:** Nowa zakładka "Dostęp jednorazowy" w zarządzaniu użytkownikami
  - Przegląd wszystkich dostępów GTA (kto, sprawa, od-do)
  - Możliwość odbioru dostępu na życzenie
  - Filtrowanie i wyszukiwanie
  - Masowe usuwanie (dla RODO)
- **Status:** 🔍 Do weryfikacji - nie pilne (klienci nie cisną), ale warto zaopiekować w przyszłości
- **Szczegóły techniczne:**
  - Lokalizacja: zakładka w zarządzaniu użytkownikami
  - Tabela: istniejąca tabela GTA (odrębna)
  - Interfejs: read-only + możliwość usuwania
  - Priorytet: niski
- **Punkty otwarte:** 
  - Jak dokładnie interfejs zarządzania?
  - Czy automatyczne usuwanie po zakończeniu procesu?
  - Jak obsłużyć RODO (masowe usuwanie)?
- **Zadania:** Do zaplanowania - analiza wymagań, projekt interfejsu, implementacja zakładki

---


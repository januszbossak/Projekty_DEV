# CHANGELOG – Testy-kompatybilnosci-API

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Architektura

**Test jednostkowy do wykrywania zmian w publicznych metodach** 💡
- **Problem:** Częste łamanie kompatybilności wstecznej przez przypadkowe zmiany w publicznym API
- ❌ Odrzucone: Brak automatycznej kontroli - nieefektywne, łatwo o przeoczenie
- 💡 **Propozycja:** Test snapshotowy
  1. Zapisuje snapshot wszystkich publicznych metod z `AMODIT.Classes` do pliku
  2. Przy każdym uruchomieniu porównuje aktualny stan z snapshotem
  3. Wykrywa zmiany w publicznych metodach (modyfikacje, usunięcia)
  4. Wymaga okresowej aktualizacji snapshota przy świadomych zmianach
- **Mechanizm:** Snapshot przypiętych do projektu, test jednostkowy porównujący przy każdym uruchomieniu
- **Punkty otwarte:**
  - Które biblioteki objąć testem?
  - Jak często aktualizować snapshot?
  - Czy rozszerzyć na interfejsy (nie tylko metody)?
- **Zadania:** Adrian Kotowski - przygotowanie testu (jeśli znajdzie czas)

---


# CHANGELOG – News-Feed-Anonse

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Tablica ogłoszeń / News feed – wymagania i alternatywy** 🔍
- **WIM wymaga** funkcjonalności tablicy ogłoszeń (news feed) zastępującej przestarzały mechanizm newsów
- Stary mechanizm: przestarzały technologicznie, nieużywany przez kluczowych klientów (CIT, Deutsche Bank)
- **Prototyp Damiana:** Zakładka "Ogłoszenia" w menu powiadomień
  - Funkcjonalności: tworzenie (temat, treść, odbiorcy wg działów), oznaczenie jako przeczytane, usunięcie, wyszukiwanie
  - **Brakujące:** Planowanie publikacji (data startu), termin ważności, wybór odbiorców przez grupy (nie tylko działy), organizacje zewnętrzne
- **Rozważane alternatywy:**
  - ⏸️ Dedykowany moduł "Ogłoszenia" (prototyp) - wymaga doprecyzowania wymagań
  - 💡 AMODIT Talk - gotowe mechanizmy (załączniki, komentarze, historia)
  - 💡 Dedykowany proces AMODIT - gotowe mechanizmy, ale "ciężar" obiegu spraw
  - ⏸️ RSS feed - na później
- **Status:** 🔍 Do weryfikacji - wstrzymanie prac do czasu precyzyjnego zdefiniowania wymagań
- **Pytania otwarte:**
  - Różnica między "news feedem" a "tablicą ogłoszeń" w wizji Piotra Murawskiego (WIM)?
  - Czy AMODIT Talk może pokryć wymagania?
  - Czy potrzebny system anonsów (jak OLX) czy tylko ogłoszenia informacyjne?
- **Zadania:** 
  - Damian Kamiński - kontakt z Piotrem Murawskim, doprecyzowanie wymagań
  - Mateusz Kisiel - prezentacja AMODIT Talk
  - Damian Kamiński - pokazanie prototypu i AMODIT Talk Piotrowi Murawskiemu

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **News Feed i Anonse** - funkcjonalność zrealizowana na procesach AMODIT (nie dedykowany moduł)
  - Anonse to sprawy w procesie, News Feed wyświetla te sprawy z odpowiednimi uprawnieniami
  - Zastosowanie: "obdarcie" sprawy ze zbędnych elementów (formularza, historii), wyświetlanie tylko treści ogłoszenia
  - ✅ Zatwierdzone - realizacja na procesach (Low-code) jako najszybsza implementacja
  - ❌ Odrzucono: dedykowany moduł (zbyt duży narzut pracy), ChromaDB (brak dostępu od ręki, overkill)

---


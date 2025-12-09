# CHANGELOG - Wzmiankowanie w komentarzach

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Bug

- Dużo zgłoszeń o niedziałających wzmiankach, konieczność przebudowy od nowa.
- Cel sprintu: wzmianki mają działać i być stabilne.
- Mariusz odpowiedzialny za przebudowę i napisanie testów end-to-end.
- To jedyny cel Mariusza w tym sprincie.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Bug #Funkcjonalność

- Wzmianki nie działają poprawnie (nie odświeżają się, problemy z działaniem).
- Mariusz robi wzmianki jako główny cel.

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność #Decyzja

- Problem ze wzmiankowaniem w komentarzach gdy wyłączone DWI (nie można oznaczać osób, brak powiadomień)
- Decyzja: Szybka poprawka umożliwiająca wzmiankowanie osób z dostępem do sprawy; docelowo rozdzielenie logiki DWI i wzmiankowania

---

## 2025-09-04 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-04 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-04%20Rada%20architektów.md)
**Kategoria:** #Decyzja #Funkcjonalność

**Zmiana logiki wzmiankowania (@mention)** ✅
- **Problem:** Wzmiankowanie dodawało jako Obserwatora (spam mailowy o każdej zmianie) i brakowało dedykowanego maila "zostałeś wzmiankowany"
- ✅ **Zatwierdzone:**
  - Wzmianka nadaje rolę **Reader** (dostęp bez maili o zmianach)
  - Wysyłany jest **dedykowany mail** o wzmiankowaniu
  - Powiadomienia tylko przy odpowiedziach na komentarz ze wzmianką

**Rola Reader dostępna z interfejsu** ✅
- **Problem:** Rola Reader dostępna tylko z reguł
- ✅ **Zatwierdzone:** Dodanie Reader ("Odczyt/Czytelnik") do sidebara uprawnień

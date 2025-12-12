# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI.md]
**Kategoria:** #Funkcjonalność #Zadanie

- **Paczka do archiwum państwowego** - pierwsza wersja do weryfikacji:
  - Generowanie paczki XML z odpowiednimi plikami
  - Cel: weryfikacja czy paczka jest dobra (endpoint do weryfikacji archiwów państwowych)
  - Narzędzie do weryfikacji: Postman lub REST API (endpoint publiczny, bez rejestracji)
  - Wątpliwości: czy konsultanci LOT są gotowi na przygotowywanie paczek w grudniu? (mogą nie mieć jeszcze wdrożonego procesu obiegu korespondencji)
  - Możliwe przesunięcie na kolejny kwartał jeśli konsultanci nie są gotowi
  - Prawdopodobnie cel następnego sprintu (pod warunkiem ukończenia JRWA w bieżącym)

**Zadania:**
- **Marek:** Generowanie paczki XML (po ukończeniu JRWA)
- **Konsultanci + DEV:** Wspólnie ustalić optymalny format paczki

**Punkty otwarte:**
- Czy konsultanci LOT są gotowi na przygotowywanie paczek do archiwum w grudniu?
- Czy oprogramować mechanizm czy zostawić jako ręczne generowanie (regułami)?

---

## 2025-11-25 | Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-25 Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa.md]
**Kategoria:** #Decyzja

-   **Roadmapa Q4 2025:** Realizacja eksportu do Archiwum Państwowego (LOT) poprzez generowanie paczek z walidacją (zamiast integracji z API).
-   **Roadmapa Q4 2025:** Bez grafiki z AMPL.

---

## 2025-11-13 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Planowanie%20sprintu.md)
**Kategoria:** #Zadanie

- Status: W trakcie.
- Priorytet: Jeden z tematów do "dokończenia" w ramach strategii stabilizacji.

---

## 2025-11-07 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-07 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Architektura #Decyzja

- Integracja z ADE jest jednym z trzech zadań dla LOT do końca roku.
- Dział wdrożeń ma pozyskać scenariusze użycia od klienta.
- Możliwe, że wystarczy użycie COLA REST API, co pozwoli uniknąć dedykowanego modułu AMODIT.
- Podejście to będzie ponownie ocenione, jeśli w przyszłości wiele klientów będzie potrzebować podobnych integracji.
- Koncentracja na zrozumieniu potrzeb biznesowych i przypadków użycia.

---
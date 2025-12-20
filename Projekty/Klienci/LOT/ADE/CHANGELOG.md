# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-05 | Roadmapa Update

**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-05 Roadmapa.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-05%20Roadmapa.md)

**Kategoria:** #Planowanie #Roadmap

- Eksport do archiwów państwowych zaplanowany na Q1 2026
- Obsługa przekazywania elektronicznych paczek archiwalnych do archiwum państwowego
- Projekt realizowany dla klienta LOT, rozwija produkt (sektor publiczny)

---

## 2025-12-09 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-09 Postęp roadmapy.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-09%20Postęp%20roadmapy.md)
**Kategoria:** #Decyzja #Zadanie

- **Eksport archiwów państwowych - przesunięcie na Q1:** Eksport dla LOT-u wejdzie w Q1, MVP 2 zamykane w tym sprincie (gotowe do przekazania), MVP 3 prawdopodobnie przyszły sprint (udogodnienia, nie kluczowe)
- **Status prac:** Marek rozwija strukturę drzewa w tym tygodniu, pierwsza wersja będzie walidacją
- **Ograniczenia:** Dział rozwoju nie jest potrzebny do integracji (publiczne endpointy), problem: brak danych do wygenerowania paczki (wdrożenie nie jest na tyle posunięte)

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
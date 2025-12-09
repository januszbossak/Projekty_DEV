# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-11-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Notatka projektowa - Integracja z KSeF Connectorem.md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- Rezygnacja z handlera `ashx` na rzecz dedykowanego kontrolera API.
- Nowy endpoint `restapi/integration/ksef/v1` obsłuży metody `POST` i `PUT`.
- Zachowana kompatybilność wsteczna; fallback do starego handlera.
- Niezależne uwierzytelnianie z niewygasającym tokenem.

---

## 2025-11-25 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-25%20Rada%20architektów.md)
**Kategoria:** #Decyzja #Architektura

- **Licencjonowanie:** KSeF Connector (integracja wewnętrzna) NIE będzie wymagał od klienta posiadania płatnej licencji na moduł REST API.
- **Rozwiązanie:** Adrian przygotuje mechanizm omijania sprawdzania licencji dla integracji wewnętrznych (specjalny endpoint lub flaga).

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Zadanie #Ryzyko

- Adrian jest przeładowany pracą, w tym projektem KSeF.
- Nierealne jest stworzenie minimalnego MVP w 8 dni.
- Cel: okrojenie zakresu prac do faktycznych potrzeb biznesowych.
- Damian i Adrian są odpowiedzialni za rozpisanie okrojonego zakresu.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Integracja #Funkcjonalność #Decyzja

- KSeF wymaga rozbudowania połączenia. Damian zaopiekuje temat.
- Jest szansa, że rozbudowa będzie po stronie KSeF lub po naszej funkcja do odczytu.

---
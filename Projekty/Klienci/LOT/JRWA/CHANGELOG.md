# CHANGELOG – JRWA (LOT)

---

## 2025-12-01 | Planowanie sprintu (Szczegóły)
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Planowanie sprintu.md]
**Kategoria:** #Architektura #Funkcjonalność

- Struktura JRWA implementowana jako 4-poziomowa.
- Klasyfikacja obiektów przez pole "słownik".
- Implementacja tylko na poziomie sprawy (brak w raportach w tym etapie).

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie #Wydanie

- Dostarczenie funkcjonalności JRWA do konsultantów i klienta LOT.
- Przygotowanie struktury bazy danych.
- Osadzenie funkcjonalności w polu odnośnik do źródła zewnętrznego.
- Implementacja wyboru kategorii JRWA.
- Przekazanie paczki do instalacji dla LOTu.
- Przepisywanie danych z JRWA do pól tekstowych (na poziomie sprawy).

---

## 2025-11-27 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-27%20Rada%20architektów.md)
**Kategoria:** #Architektura #Decyzja #Zadanie

- **Implementacja:** JRWA jako zewnętrzne źródło typu "klasa" (wzór GUS TERYT), ale dane lokalne z tabel AMODIT.
- **Funkcjonalność:** Wybór klasyfikacji JRWA w formularzu, filtrowanie po uprawnieniach użytkownika, wybór tylko "liści" drzewa.
- **Dane:** Przechowywanie w 2-3 tabelach (lista pozycji, uprawnienia).
- **Zadanie:** Marek Dziakowski zaprojektuje strukturę tabel i zaimplementuje klasę JRWA dziedziczącą po interfejsie źródeł danych.

## 2025-11-27 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-27 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #UX #Ryzyko

- Cel: Obsługa Jednolitego Rzeczowego Wykazu Akt (JRWA) dla klienta LOT.
- Kontekst: Klient LOT rozpoczyna pracę z JRWA, użytkownicy nie znają struktury katalogów, konieczne wsparcie wyszukiwania i podpowiadania.
- Zakres prac: Implementacja obsługi typu źródła JRWA w polu "Odnośnik do źródła zewnętrznego", dodanie pliku instrukcji/schematu JRWA.
- Mechanizm wyszukiwania: Analogiczny do GUS TERYT, z wyświetlaniem pełnej ścieżki w drzewie i przypisywaniem tylko do ostatecznych gałązek.
- Decyzje: Klient LOT nie potrzebuje nadawania uprawnień do katalogów JRWA (wszyscy widzą wszystko).
- Pomysły (nie MVP): Podpowiadanie ostatnio używanych katalogów JRWA.
- Ryzyka: Niska znajomość struktury JRWA przez klienta.

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Spotkania projektowe/2025-12-03 Notatka projektowa - Historia biznesowa.md](../../../../Notatki/Spotkania%20projektowe/2025-12-03%20Notatka%20projektowa%20-%20Historia%20biznesowa.md)
**Kategoria:** 💡 Koncepcja

- **Historia przypinania/odpinania dokumentów do teczek** – każde przypięcie/odpięcie generuje zdarzenie w historii biznesowej z `BusinessSubjectType = 'jrwa_folder'`.
- **Widok historii teczki JRWA** – filtrowany widok zdarzeń biznesowych (SQL: `WHERE BusinessSubjectType = 'jrwa_folder' AND BusinessSubjectID = <ID teczki>`). Pokazuje kto, kiedy i dlaczego przypięto/odpięto dokument.
- **EventType słownikowy** – administrator definiuje zdarzenia "Przypięcie do teczki JRWA" i "Odpięcie z teczki JRWA" w słowniku zdarzeń biznesowych.
- **Pole linked w message** – opcjonalnie można wrzucić link HTML do dokumentu/sprawy dla wygody użytkownika.
---

## 2025-11-28 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Notatka projektowa - Połączenie z Marek Dziakowski.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-28%20Notatka%20projektowa%20-%20Połączenie%20z%20Marek%20Dziakowski.md)
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- JRWA będzie implementowane jako struktura 4-poziomowa.
- Brak 5. poziomu w strukturze JRWA (np. podteczki dla nieruchomości) jako element klasyfikacji JRWA.
- Dodatkowe przyporządkowanie spraw do obiektów (np. nieruchomości) poprzez pole typu "słownik".
- Widoki JRWA: Marek Dziakowski ma zaimplementować JRWA jako pole typu `Odnośnik`, umożliwiające wybór klasy JRWA.
- Koncepcja "teczka/podteczka" w rozporządzeniu odnosi się do 2 poziomów sprawy AMODIT w ramach JRWA, a nie 2 poziomów klas JRWA.

---

## 2025-11-18 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-18 Notatka projektowa - Implementacja JRWA (LOT).md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- Struktura JRWA w dedykowanej tabeli (JRWA_Schema).
- Dedykowany panel na formularzu sprawy do wyboru katalogu JRWA.
- Użytkownik wpina amoditową sprawę do "teczki sprawy".
- Uprawnienia JRWA zarządzane na poziomie działów z dziedziczeniem.
- Wyszukiwanie spraw w JRWA przez tabelę indeksującą lub indeksy.
- Endpointy dla modułu raportowego dla archiwistów.
- MVP 1 obejmuje kluczowe aspekty implementacji JRWA.

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- Budowa struktury danych JRWA (tabela, źródło danych) na wzór GUS TERYT.
- Dostęp do atrybutów JRWA w regułach przez notację kropki (np. `[PoleJRWA].KlasaArchiwalna`).
- Rezygnacja z implementacji logiki uprawnień dla JRWA na obecnym etapie (na żądanie klienta).
- Zarządzanie strukturą JRWA (panel) przesunięte na kolejne sprinty.

---

## 2025-11-19 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-19 Notatka projektowa - Przegląd wycen.md]
**Kategoria:** #Architektura #Zadanie

- JRWA to tylko część zagadnienia, istotna jest również fizyczna archiwizacja (pudła, składy chronologiczne).
- Sugestia budowy dedykowanego rozwiązania zamiast opierania się na standardowych rejestrach i odnośnikach.
- Temat przekierowany na dedykowane spotkanie projektowe.

---

## 2025-11-13 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Planowanie%20sprintu.md)
**Kategoria:** #Architektura #Funkcjonalność #Ryzyko

- Implementacja JRWA jako rejestr ze strukturą drzewiastą (sprawy nadrzędne/podrzędne).
- Wymagany układ hierarchiczny w raporcie typu tabela (jak w Gancie).
- Węzły JRWA przechowują: daty obowiązywania, kategorię archiwalną, uprawnienia.
- Struktura definiowana rzadko (co rok), import jednorazowy, potem zarządzanie w AMODIT.
- Ryzyko: Ogrom pracy, wymagane szczegółowe rozpracowanie i analiza dokumentów.

---

## 2025-11-13 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #Zadanie

- Potwierdzono, że JRWA to szeroki temat wymagający porządków.
- Realizacja przewidziana po zakończeniu projektu WIM.

---

## 2025-11-07 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-07 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Design #Zadanie #Architektura

- JRWA jest normatywnym wymogiem dla każdego dokumentu, musi być realizowane płynnie i wygodnie.
- Konieczne zaprojektowanie i wdrożenie "Asystenta klasyfikacji" (pole "Odnośnik" z okienkiem klasyfikatora JRWA).
- Asystent powinien posiadać mechanizmy wyszukiwania, widok drzewa i uwzględniać uprawnienia użytkownika.
- Użytkownicy powinni identyfikować teczkę sprawy, a nie bezpośrednio węzeł JRWA.
- JRWA postrzegane jest jako rozwiązanie systemowe z potencjałem dla wielu klientów.

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Zadanie #Funkcjonalność

- Janusz rozpracowuje temat JRWA i ma ustalić, czy coś będzie w tym zakresie robione.
- Nie każdy widzi całe JRWA; matryca kompetencji i ochrona danych osobowych wymagają dostępu tylko do odpowiednich części.

---

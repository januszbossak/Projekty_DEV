# CHANGELOG – Ustawienia-systemowe

---

# CHANGELOG – Ustawienia-systemowe

---

## 2025-11-20 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-20 Spotkanie projektowe - Edytor procesów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-20%20Spotkanie%20projektowe%20-%20Edytor%20procesów.md)
**Kategoria:** #Status #Decyzja

- **MVP Zamknięte:** Potwierdzono przeniesienie 100% funkcjonalności ze starej technologii (Wiki, integracje, four-eyes, REST API, autentykacja).
- Możliwość wyłączenia komunikatu o przełączeniu do nowego widoku (zachowanie opcji powrotu dla kompatybilności).

---

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie

- Zamknięcie tematu 4-eyes w ustawieniach systemowych, odtwarzając poprzednią funkcjonalność.
- Wymagany backend dla tej implementacji.
- Przemek odpowiedzialny za implementację.

---

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Monitoring #Bezpieczenstwo

- Implementacja mechanizmu powiadamiania administratorów o krytycznych zdarzeniach (limity OCR, przestrzeń na dysku, brak dostępu do dysku sieciowego) poprzez maile i powiadomienia w interfejsie.

**Kategoria:** #Problem #Diagnostyka

- Problem z pulą aplikacji w AMODIT u klienta Endur. Wymaga wsparcia Piotra Buczkowskiego w diagnozie.

---

## 2025-10-16 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-16 Notatka projektowa - Edytor procesów.md]
**Kategoria:** #Funkcjonalność #Bezpieczeństwo

- Planowane prace nad funkcjonalnością "Potwierdzenie zmian przez innego administratora" ("Four-eyes principle") w Ustawieniach systemowych

---

## 2025-10-09 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-09 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Bezpieczeństwo #Decyzja

- Problem dodawania pól bezpośrednio na środowisku produkcyjnym (rozjechanie środowisk, konflikty importu)
- Decyzja: Wprowadzenie parametru systemowego "produkcja" oraz mechanizmu utrudniającego dodawanie pól na produkcji

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Design #Bug

- Odświeżenie interfejsu strony logów systemowych (przeniesienie do React, zachowanie funkcjonalności)
- Wprowadzono nowe możliwości filtrowania i wyszukiwania, eksport zaznaczonych logów
- Zidentyfikowano błędy: kopiowanie do schowka, rejestrowanie zmian null, braki w kolejce maili

---

## 2025-09-23 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-23 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-23%20Rada%20architektów.md)
**Kategoria:** #Architektura #Problem

- **Audyt zmian parametrów:** Odrzucono pomysł wypełniania `par_modified_by_id` dla każdej zmiany (służy do mechanizmu 4-oczu). Audyt zmian dostępny w `UserActivity`.
- **Rejestracja zmian:** Zgłoszono brak rejestracji zmian w `UserActivity` dla 2 parametrów odpowiadających za kolory w raportach.

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Przełączka do wersji starej:** wdrożono mechanizm powrotu do klasycznego widoku ustawień systemowych.
- **Status:** funkcjonalność dostępna już na środowisku Astrofox.
- **Do dopracowania:** spójność nazw (w nowych ustawieniach nazewnictwo nieco różni się od starego).

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Architektura

**Cel:**
Przepisanie frontu ustawień systemowych na nową technologię Reactową w celu poprawy nawigacji i łatwiejszego znajdowania konkretnych ustawień.

### Nowy interfejs

- Przepisanie frontu na React
- Nie wszystkie ekrany są jeszcze pokryte w tym wydaniu (kluczowe poszły w pierwszej kolejności, kolejne będą uzupełniane)
- Nawigacja po ustawieniach stała się wygodniejsza, łatwiej znaleźć konkretne ustawienie

### Kompatybilność wsteczna

- Zachowana pełna kompatybilność wsteczna
- Ponieważ nie wszystko jest pokryte, zawsze można wrócić do poprzedniej wersji
- Administratorowi najpierw wyświetlą się nowe ustawienia Reactowe
- Jeżeli jakaś funkcjonalność nie będzie dostępna, w każdej chwili można wrócić do dotychczasowych
- W pierwszej kolejności korzystanie z nowych, w ciągu następnych dwóch wydań pełne przejście na wersję Reactową

### Szczegóły techniczne

- Odbiorcy: ograniczone grono administratorów
- Technologia: React

**Ograniczenia:**
- Nie wszystkie ekrany są jeszcze pokryte (kolejne będą uzupełniane w następnych wydaniach)

---

## 2025-08-25 - Sprint review

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-25 Sprint review|2025-08-25 Sprint review]]

**Kategoria:** #Funkcjonalność #Design

**Prezentacja:** Kamil Dubaniowski

**Cel biznesowy:**
Usprawnienie konfiguracji zadań systemowych (Jobów) poprzez intuicyjny interfejs zamiast ręcznego wpisywania wartości w bazie danych. Obecne wartości w bazie nie są przejrzyste i nie są intuicyjne do dodawania, edytowania czy usuwania. Dodatkowo, konsultanci często nie potrafią poprawnie skonfigurować harmonogramu (np. włączają regułę co minutę, która chodzi w weekendy niepotrzebnie po północy).

**Co zaimplementowano:**
- **API do zarządzania Jobami:** dodawanie, usuwanie, edycja, wykonywanie akcji
- **Formularz dodawania Joba:**
  - Wybór biblioteki i klasy (z listy rozwijanej, nie ręczne wpisywanie)
  - Nazwa klasy preferowanym serwerem
  - Ustawienie częstotliwości działania (z podglądem godziny startu)
  - Wybór minuty startu (jeśli dotyczy)
- **Intuicyjna konfiguracja częstotliwości:** zamiast wpisywania wartości w minutach od północy, użytkownik wybiera:
  - Typ częstotliwości (co ile godzin, raz dziennie, etc.)
  - Godzinę startu
  - Godzinę zakończenia (jeśli dotyczy)
- **Podgląd harmonogramu:** wyświetlanie na dole, jak będzie wyliczana częstotliwość

**Jak to działa:**
System skanuje wszystkie klasy implementujące interfejs `IJob` przy starcie procesu i tworzy słownik dostępnych opcji. Użytkownik wybiera z listy rozwijanej, nie wpisuje ręcznie. Harmonogram jest przeliczany w tle na podstawie ustawień częstotliwości.

**Ograniczenia prototypu:**
- **Prototyp:** obecna wersja jest prototypem, wymaga dopracowania
- **Format daty:** format daty nie jest spójny z resztą systemu (do poprawy)
- **Wyświetlanie daty:** data wyświetlana w dwóch linijkach zamiast jednej (do poprawy)
- **Brak walidacji:** na razie brak walidacji poprawności wpisanych wartości (do dodania)

**Feedback z demo:**
- **💭 Pomysł Przemka:** Dwie ikonki "Integracje" i "Rozszerzenia" wyglądają jak błąd (ta sama ikonka dwa razy). Warto zmienić jedną z ikonek lub połączyć w jedną zakładkę "Integracje".
- **Piotr Buczkowski:** Zachować format daty spójny z resztą systemu. Data powinna być w jednej linijce, nie dwóch.
- **Damian Kamiński:** Bardzo istotne, aby od razu zdefiniować wybór z listy (słownik), aby wyeliminować błędy wpisywania. To jest około 20-30 pozycji, więc łatwo o pomyłkę.
- **Łukasz Bott:** Uspójnienie z częstotliwościami reguł okresowych w procesach (ale wycofano się z tego ze względu na kompatybilność wsteczną).

**Dalsze kroki:**
- Dopracowanie prototypu do wersji produkcyjnej
- Poprawienie formatu daty (spójność z systemem)
- Dodanie walidacji
- Zmiana lub połączenie ikonek "Integracje" i "Rozszerzenia"

---

## 2025-08-12 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-12 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-12%20Rada%20architektów.md)
**Kategoria:** #Architektura #Problem

**Problem kompatybilności wstecznej interfejsu IJob** ✅
- **Problem:** Rozszerzenie `IJob` o pole `Owner` złamało wszystkie istniejące implementacje jobów
- Wystąpiło na Stage (Rossmann), na szczęście nie na produkcji
- ❌ Odrzucone: Modyfikacja istniejącego interfejsu - łamie kompatybilność wsteczną
- ✅ Zatwierdzone: Nowy osobny interfejs dla jobów wymagających `Owner`
- Istniejące joby nie wymagają modyfikacji, zachowana kompatybilność
- ⏸️ Punkty otwarte: "Czy można to zrobić lepiej?" - analiza po powrocie Marka z urlopu
- **Zadania:** Marek - weryfikacja rozwiązania po powrocie z urlopu

---

## 2025-08-07 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-07 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-07%20Rada%20architektów.md)

**Kategoria:** #Funkcjonalność

**1. MVP dla integracji w ustawieniach systemowych** ✅
- Struktura MVP:
  - **Integracje wbudowane** (VIES, kursy walut, Biała Lista) - stała pierwsza pozycja
  - **Druga kolumna:** Lista integracji skonfigurowanych (wyświetlane tylko gdy mają parametry)
  - **Przycisk "Dodaj integrację":** wybór standardowej lub "Skonfiguruj własną"
- Zasada: integracja pojawia się tylko gdy ma skonfigurowane parametry (nawet częściowo)
- Interfejs w Reactcie, kompatybilność wsteczna z istniejącymi konfiguracjami
- **Zadania:** Kamil Dubaniowski, Przemek - finalizacja MVP

**6. Integracje vs moduły – rozróżnienie** ✅
- **Integracje** = połączenia z zewnętrznymi systemami (KSeF, OpenAI, Biała Lista)
- **Moduły** = funkcjonalności systemu (Raporty zaawansowane) - powinny być w licencji, nie w integracji
- **Zadania:** Upewnienie się że w interfejsie integracji nie ma modułów

**Kategoria:** #Architektura

**2. OAuth i tokeny – konfiguracja aplikacji** 🔍
- Koncepcja: definicja aplikacji OAuth z możliwością generowania wielu tokenów
- W konfiguracji integracji wybór tokenu zamiast ręcznego wpisywania parametrów
- **Status:** Do weryfikacji - lokalizacja wymaga przemyślenia
- **Punkty otwarte:** Czy w integracjach czy osobna zakładka (analogicznie do Connection Stringów)?

**Kategoria:** #Roadmap

**3. Reorganizacja ustawień systemowych** ⏸️
- Potrzeba kategoryzacji integracji (podpisy, przechowywanie dokumentów, uwierzytelnianie)
- **Odroczone:** Zbyt złożone na MVP, osobny projekt w przyszłości
- MVP: odwzorowanie obecnej struktury w Reactcie z poprawą UX
- **Punkty otwarte:**
  - Czy Active Directory w integracjach czy osobnej zakładce "Uwierzytelnianie"?
  - Czy Connection Stringi jako integracje czy osobna zakładka?
  - Lokalizacja poczty przychodzącej/wychodzącej?

**4. Wykorzystanie AI do tworzenia integracji** ⏸️
- Koncepcja: AI (AMODIT Copilot) analizuje Swagger i generuje konfigurację integracji
- **Odroczone:** Nie w zakresie MVP, element strategii wykorzystania AI
- Przykład już wdrożony: wyszukiwanie i interpretacja parametrów w Copilocie

**Kategoria:** #Decyzja

**5. Eksport helpa do PDF** ❌
- Pytanie klienta o eksport helpa do PDF
- **Odrzucone:** Brak uzasadnienia biznesowego
  - Help dostępny w AMODIT Copilocie i plikach YAML
  - Dokumentacja zmienia się często - statyczny eksport szybko się dezaktualizuje
- Oferta płatna: 15 000 zł (jako weryfikacja rzeczywistej potrzeby)

---


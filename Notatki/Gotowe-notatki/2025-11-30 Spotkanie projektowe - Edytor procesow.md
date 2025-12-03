# Notatka projektowa – 2025-11-30 – Edytor procesów i strategia projektowa

**Data:** 2025-11-30
**Temat główny:** Projekt WIM (Repozytorium plików), rozwój Edytora Procesów, strategia deweloperska
**Powiązane projekty:**
- `klienci/WIM`
- `moduly/Edytor-procesow`
- `moduly/Repozytorium`
- `cross-cutting/AI`

---

## 1. Projekt WIM – Repozytorium plików

**Komponent:** Repozytorium / Integracje

### Cel i problem

Dostarczenie funkcjonalnego rozwiązania do zarządzania plikami dla klienta WIM w ramach MVP, z planem dalszego rozwoju i negocjacją umowy serwisowej po odbiorze. Ustalenie strategii technicznej dla nowej aplikacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Zintegrowana aplikacja w AMODIT** | Rozwijanie Repozytorium jako integralnej części AMODIT, w tej samej bazie danych. | ❌ Odrzucona (na etapie MVP) |
| **Odrębna aplikacja wpięta w AMODIT** | Rozwijanie Repozytorium jako odrębnej aplikacji, korzystającej z AI, z własną bazą danych, wpiętej w AMODIT. | ✅ Wybrana |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (MVP)

- **Strategia rozwoju MVP:** Repozytorium będzie rozwijane jako odrębna aplikacja, wpięta w AMODIT (podobne podejście jak do Komunikatora). Będzie korzystać z AI do wytwarzania, minimalizując ryzyko dla głównego systemu AMODIT.
- **Baza danych:** Będzie to oddzielna baza danych (dyskusja na temat tego, czy w tej samej instancji co AMODIT, czy oddzielna dla każdego klienta). Przemysław Sołdacki przewiduje, że docelowo i tak będzie dążyć do integracji z główną bazą **AMODIT**. Piotr Buczkowski sugeruje, że dla każdego klienta będzie oddzielna baza danych.
- **Metadane plików (MVP):** Uproszczony model metadanych: nazwa pliku (techniczna i wyświetlana), opis i tagi. To wystarcza dla obecnego MVP dla WIM.
- **Uprawnienia plików (MVP):** Uprawnienia będą ustawiane na najwyższym poziomie (przestrzeń repozytorium) i dziedziczone w dół. Nie będzie możliwości zrywania dziedziczenia na niższych poziomach (pliki, podfoldery) w ramach MVP.
- **Demo:** Koncepcja publicznego demo (resetowanego co godzinę, z podanymi loginami) dla zewnętrznych funkcjonalności (takich jak Repozytorium, Komunikator), aby ograniczyć indywidualne prośby o dema i ich utrzymanie. (Dyskusja: Damian, Przemysław Sołdacki)
- **Termin:** Projekt ma być odebrany do grudnia, aby umożliwić negocjacje nowej umowy serwisowej na dalszy rozwój.

**Szczegóły techniczne:**
- Odrębna aplikacja.
- Oddzielna baza danych.
- Metadane: nazwa, opis, tagi.
- Uprawnienia: dziedziczone z najwyższego poziomu.

### Ograniczenia / Poza zakresem

- W ramach MVP nie będzie zaawansowanego edytora metadanych.
- Nie będzie granularnego zarządzania uprawnieniami na poziomie podfolderów/plików (zrywanie dziedziczenia).

### Punkty otwarte

- Ustalenie z Piotrem Buczkowskim, czy baza danych Repozytorium będzie w tej samej instancji co AMODIT, czy całkowicie oddzielna.
- Weryfikacja akceptacji uproszczonego modelu uprawnień przez WIM.

---

## 2. Rozwój Edytora Procesów

**Komponent:** Edytor Formularza / Edytor Diagramu

### Cel i problem

Ciągłe usprawnienia i rozwój funkcjonalności w Edytorze Procesów, w tym poprawki użyteczności, optymalizacje wydajności i strategiczne podejście do realizacji zadań.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (ciągły rozwój, z naciskiem na MVP)

- **Edytor Diagramu:** Na zaawansowanym etapie, prace niemal zakończone. Pozostaje kwestia prawego panelu (do ustalenia z Kamilem).
- **Panel prawy ustawień pola:**
    - Zmiana kolejności i układu ustawień (zadanie Przemysława Rogaś).
    - Komunikat o przekroczeniu limitu pól (nie tylko ciche niepowodzenie). Przemysław Rogaś stworzy zadanie.
- **Optymalizacja pobierania danych:** Ograniczenie początkowego pobierania użytkowników i słowników do 50 pozycji, z możliwością wyszukiwania, co poprawia wydajność.
- **Edycja słowników:** Usprawniony interfejs (bezpośrednia edycja, akceptacja ryzyka).
- **Brak wyszukiwania w słownikach:** Zgłoszona potrzeba dodania funkcji wyszukiwania w oknach wyboru słowników.
- **Masowe działania na liście pól:** Potrzeba implementacji funkcji masowego przenoszenia pól między sekcjami (np. Ctrl+zaznaczenie wielu pól, drag & drop) w widoku listy pól (niekoniecznie w edytorze graficznym). Przemysław Sołdacki i Damian Kaminski sugerują, że lista jest wystarczająca w ramach MVP.
- **Strategiczne podejście do developmentu (Przemysław Sołdacki):**
    - **Scrum-oriented:** Przejście na bardziej skoncentrowane cele sprintu (np. "dokończyć edytor formularza") i dostarczanie "domkniętych" funkcjonalności, zamiast wielu rozgrzebanych.
    - **Definicja MVP:** Jasne określanie zakresu MVP dla każdego etapu (np. "diagram bez prawego panelu" jako MVP1, "diagram z prawym panelem" jako MVP2).
    - **Współpraca:** Zespół ma pracować w ramach skoncentrowanych zespołów na konkretnych celach.

**Szczegóły techniczne:**
- Ikony w interfejsie: Wszystkie ikony są teraz typu outline.

### Punkty otwarte

- Implementacja funkcji wyszukiwania w słownikach.
- Implementacja masowych działań (przenoszenie) na liście pól.
- Finalne ustalenia dotyczące prawego panelu w Edytorze Diagramu.
- Stworzenie zadań dla wszystkich zidentyfikowanych usprawnień.

---

## 3. Organizacja pracy i strategiczne zmiany

**Komponent:** Zarządzanie projektem / Organizacja zespołu

### Cel i problem

Usprawnienie organizacji pracy zespołu deweloperskiego, w tym lepsze zarządzanie backlogiem, efektywniejsze planowanie sprintów i jasne określanie priorytetów.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (do wdrożenia)

- **Zmiana formuły Daily:** Janusz Bossak zaproponował, aby Daily skupiało się na postępach w kluczowych projektach i celach sprintu, a dopiero później na indywidualnych statusach i hotfixach.
- **Zarządzanie backlogiem:** Przemysław Sołdacki postuluje, aby połowę roadmapy wyrzucić i skupić się na mniejszej liczbie dowiezionych (domkniętych) funkcjonalności. Woli mieć mniej rzeczy na roadmapie, ale je dostarczyć.
- **Zespoły projektowe:** Sugestia podziału zespołu na mniejsze, skoncentrowane na konkretnych celach projektowych (np. jeden zespół na edytor formularzy, inny na repozytorium).

### Punkty otwarte

- Wdrożenie nowej formuły Daily.
- Przegląd i redefiniowanie roadmapy w oparciu o priorytetyzację i "domykanie" mniejszej liczby projektów.
- Ustalenie składu i celów dla nowych, skoncentrowanych zespołów projektowych.

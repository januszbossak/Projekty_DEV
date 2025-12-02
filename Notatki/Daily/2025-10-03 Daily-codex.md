# Daily – 2025-10-03

**Data:** 3 października 2025, 07:20

**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`

**Uczestnicy:** Lukasz Bott, Damian Kaminski, Kamil Dubaniowski, Lukasz Brocki, Filip Liwiński, Przemysław Rogaś, Mariusz Piotrzkowski, Oktawia Ostrowska, Patrycja Walaszczyk, Marek Dziakowski, Adrian Kotowski, Anna Skupinska, Barbara Michalek
**Nieobecni:** Piotr Buczkowski (urlop), Mateusz Kisiel (urlop), Michał Zwierzchowski, Janusz Bossak

---

## Status prac

### Łukasz Brocki
- **Wczoraj:**
  - Przygotowanie nowej funkcji reguł (tworzenie Nikola outu) - na internal
  - Bug weryfikacji podpisu na dokumencie
- **Dzisiaj:** Uzupełnienie dokumentacji, testy losowe (2 zgłoszenia w sprincie), najpierw zgłoszenia
- **Uwaga:** Kamil zwrócił uwagę na zmianę ikony w komunikacie informacyjnym (Mateusz napisał na internal)

### Filip Liwiński
- **Wczoraj:**
  - Zmiana sposobu wyświetlania logów systemowych
  - Dodanie multiselect dla modułu na frontendzie
  - Poprawki matrycy uprawnień (zgłaszane przez Kamila i Patrycję)
- **Dzisiaj:** Dodanie multiselectu użytkowników na logach systemowych

### Przemysław Rogaś
- **Wczoraj:** Kontynuacja zadań z edytora formularza
- **Dzisiaj:** Dalsze zadania z edytora, integracje

### Mariusz Piotrzkowski
- **Wczoraj:**
  - Wykopał blackboard do profilu Łukasza Bota (problemy z poprzednimi wersjami - długo zajęło)
  - Walidacja pola tekstowego z maską - okazało się że to działanie zamierzone (przekazane na radę)
  - Spotkanie TrustCenter
  - Układanie przycisków na belce sprawy - pozostała poprawa wydajnościowa na interfejsie
  - Zmiana komunikatu gdy na formularzu nie ma żadnych pól
- **Status:** Krótszy dzień (zmulenie, drzemka)

### Oktawia Ostrowska
- **Wczoraj:** Moduł raportowy, logi systemowe, konsultacje do zadań
- **Dzisiaj:** Logi systemowe + zadanie Marka związane z TrustCenter

### Patrycja Walaszczyk
- **Wczoraj:** Zakończenie testów internal matrycy uprawnień
- **Dzisiaj:** Kontynuacja regresu (głównie matryca uprawnień), moduł raportowy
- **Blokery:** Brak

### Marek Dziakowski
- **Wczoraj:**
  - Poprawki testów wolnych do zadań na testach
  - Aktualizacja TrustCenter
- **Dzisiaj:**
  - Poprawa SQL zgłoszone przez Piotra (na podstawie slow logów w TrustCenter)
  - Mniejsze zgłoszenia z tego sprintu

### Damian Kamiński
- **Wczoraj:**
  - Dużo spotkań Allianz (warsztat z klientem, status wewnętrzny, spotkanie z wdrożeniowcami - ustalenie podziału prac, brak opiekuna wdrożenia)
  - Rada architektów (omówienie raportów systemowych)
  - Spotkanie projektowe - planowanie sprintu/usprawnienie pracy
  - Prace w Orlenie, wdrożenie faktur w Zimbra
- **Dzisiaj:**
  - Pytanie czy są tematy na design
  - Praca nad blogiem
  - Spotkanie z konsultantami
- **Propozycja:** Czyszczenie backlogu bugów (więcej w sekcji Tematy organizacyjne)

### Adrian Kotowski
- **Wczoraj:**
  - Spotkanie - konfiguracja Azure Key Vault (produkcja już działa, czekają na dark demon problem)
  - Aplikacja dla Maca - przepracowanie rozpoznawania kluczy prywatnych
- **Dzisiaj:**
  - Przygotowanie drugiej wersji aplikacji dla Maca (2 PBI)
  - Dodanie obsługi podpisów kwalifikowanych z SignApp
  - Dodanie rozpoznawania kluczy prywatnych
  - Plan: wysłać do Janusza do testów (jedyny z Makiem w zespole)

### Anna Skupińska
- **Wczoraj:** Praca nad logami systemowymi
- **Dzisiaj:** MS SQL - problem z incrementalnymi źródłami danych
- **Uwaga:**
  - Wczorajsze spotkanie o raportach - wychodzi że są różne pomysły jak dane mają wyglądać, więc nie skupia się jeszcze na dashboardzie biznesowym, tylko na technikaliach
  - Zrobiony hotfix zgłoszony przez Basię

### Łukasz Bott
- **Wczoraj:**
  - Dyskusja o raportach systemowych (rada + design + dogadywanie błędów)
  - Wsparcie sprzedaży - CRM faktury/paragony, przygotowanie draft umowy (dział handlowy + klienci, uwagi do zapisów)
- **Dzisiaj:**
  - Typowe spotkania piątkowe
  - Konsultacje z Kamilem Spyrą (PKF)
  - Raporty systemowe - opisy
  - Aktualizacja szczegółów
- **Bug znaleziony:** Opisy w raportach/dashboardach dostępne tylko w trybie edycji, nie w podglądzie (literce i przy kafelkach nie działa tooltip)

### Kamil Dubaniowski
- **Wczoraj:**
  - Wsparcie sprzedaży IMG + Lucyna (przygotowanie odpowiedzi na pytania do oferty)
  - Planowanie sprintu
  - Spotkanie projektowe z Przemkiem - matryca uprawnień (uwagi do wyglądu i oznaczania dziedziczenia)
- **Dzisiaj:**
  - Planowanie (ustalenie planu Daily jak ma wyglądać)
  - Design (tematy do dobrania - odchodzenie od roadmapy, ewentualnie lista reguł z Przemkiem)
  - Spotkanie z konsultantami

### Barbara Michałek
- **Wczoraj:**
  - Zgłoszenia z raportów od PBI
  - **Hotfix:** Resetujące się filtry w PBI (zgłoszony do Oli)
  - Bug od wersji 2.4.12: nie działa ustawienie filtrów ill twórcy PBI (zgłoszenie od Neuki)
  - Bug: PBI nie otwiera się jako pop-up, tylko otwiera sprawę z hiperlinka (niepotrzebne)
  - Bug: import danych do tabeli na sprawie - sumują się wartości (nowe zgłoszenie)
- **Dzisiaj:**
  - 1 failed test u Piotrka (priorytet 1, ale Piotrka nie ma)
  - 2 zadania priorytet 1 na internal testach
  - 3 zadania priorytet 2 na internal testach
- **Uwaga dla konsultantów:** Lepiej opisywać błędy - ostatnio wrzucają logi bez repro steps, bez informacji jak odtworzyć, co uniemożliwia testy/retesty
- **Inne:** Nie może na spotkanie o 15:00 (wizyta u lekarza - dostała termin minutę temu)

---

## Tematy organizacyjne

### Zmiana formuły Daily
- **Status:** Zapowiedź zmian
- **Kontekst:** Wczoraj dyskusja Damian, Janusz, Łukasz, Kamil
- **Plan:** Przedstawienie nowych zasad w przyszłym tygodniu (po powrocie Janusza)
- **Na razie:** Bez zmian, klasyczny format (co zrobiono wczoraj, plan na dziś)

### Propozycja: Czyszczenie backlogu bugów
**Autor:** Damian Kamiński
**Propozycja:** Zmiana statusu wszystkich bugów na "removed", a następnie wznawianie tylko faktycznie potrzebnych

**Problem:**
- Wielki worek bugów w backlogu
- Poruszanie się po nim nie ma sensu
- Wszystko trafia do worka sprintowego mimo że nie wykonamy tego w sprincie
- Sprinty nierozliczalne - nie robimy połowy rzeczy zaplanowanych
- Robimy je dopiero w kolejnych sprintach

**Cel:**
- Mieć czysty backlog bugów "do wzięcia"
- Łatwo wyfiltrować niepotrzebne
- Planować bugi realnie do sprintów (nie na ten sprint, może nawet w większej odległości)
- Przypisywać do sprintu wtedy kiedy faktycznie to zrobimy

**Reakcja Barbara:**
- Obawy - czy to znaczy że usuwamy wszystkie bugi i zajmujemy się tylko...?
- Wyjaśnienie: NIE usuwamy, ZMIENIAMY STATUS, później analizujemy każdy z osobna jeśli będą wznowione

**Ustalenie:**
- To na razie propozycja/zalążek pomysłu
- Nic jeszcze nie robimy
- Każdy ma przemyśleć i zgłaszać ryzyka
- **Status:** 💡 Propozycja (do dyskusji na Designie/Planowaniu, bez decyzji bez Janusza)
- **Bez Janusza nie podejmujemy decyzji** (Barbara)

**Uwaga:** Hotfixy robimy na bieżąco (takie są zasady), bugi planujemy

### Design dzisiaj
- **Pytanie:** Czy są tematy?
- **Propozycje:**
  - Dyskusja o czyszczeniu backlogu bugów
  - Lista reguł (Przemek naciska) - wytyczne, koncepcja, zgodność z widokiem listy pól na formularzu
  - Reguły tabeli dla formularza - czy mają być w naszym projekcie PBI?
- **Decyzja:** Do ustalenia

### Problemy z opisywaniem błędów przez konsultantów
- **Problem:** Konsultanci wrzucają logi bez repro steps, bez informacji jak odtworzyć
- **Skutek:** Uniemożliwia dalsze testy i retesty
- **Akcja:** Przekazać na spotkaniu z konsultantami (15:00)
- **Propozycja Damiana:** Pokazać 2 przykłady, żeby zobrazować problem (nie wytykać konkretnemu, tylko uzmysłowić)
- **Propozycja Łukasza:** Odbijać źle opisane zgłoszenia - "nie wiemy co testować, nie ma repro steps, odbijamy"

---

## Blokery / Ryzyka

1. **Brak opiekuna wdrożenia Allianz**
   - Wdrożenie skomplikowane
   - Damian przejmuje tę rolę tymczasowo

2. **Opisy w raportach nie działają w trybie podglądu**
   - Dostępne tylko w trybie edycji
   - Brak tooltipów przy kafelkach
   - Łukasz zgłosi bug

3. **PBI - różne bugi**
   - Resetujące się filtry (hotfix)
   - Nie działa ustawienie filtrów ill twórcy (od wersji 2.4.12)
   - Sprawa otwiera się z hiperlinka zamiast jako pop-up
   - Import do tabeli - sumują się wartości

4. **Źle opisywane zgłoszenia przez konsultantów**
   - Brak repro steps
   - Uniemożliwia testy/retesty
   - Marnuje czas zespołu

5. **Problem z Windows 10 - koniec wsparcia**
   - **Kontekst:** Windows 10 Pro kończy wsparcie 15 października.
   - **Dotyczeni:** Kamil Dubaniowski (7-letni komputer, za słaby procesor/brak TPM), Łukasz Bott.
   - **Akcja:** Kamil musi zgłosić potrzebę wymiany sprzętu (sprzęt nie spełnia wymagań Windows 11).
   - **Uwaga:** Michał oferuje oddanie nieużywanego laptopa (do sprawdzenia).

6. **Spotkanie Daily/Design ("Indy" w transkrypcji) - brak agendy**
   - **Kontekst:** Kamil Dubaniowski zaproszony przez Lucynę (poszła na urlop), cel spotkania nieznany, 7-8 osób po stronie klienta (prawdopodobnie).
   - **Akcja:** Janusz i Kamil muszą szybko ustalić plan spotkania.

7. **Bug - strona logowania (2 obrazki)**
   - **Kontekst:** Tydzień temu było dobrze, po aktualizacji (prawdopodobnie w piątek) pojawił się duplikat.
   - **Przyczyna:** Prawdopodobnie związane z logo strony + alternatywą dla tekstu.
   - **Akcja:** Michał aktualizuje strefę ręce wieczorem, może włączyć poprawkę.

---

## Przydatne notatki

- **Matryca uprawnień:** Zakończone testy internal (Patrycja), kontynuacja regresu
- **Logi systemowe:** Multiselect użytkowników (Filip), Anna pracuje nad MS SQL
- **Edytor formularza:** Ciągła praca (Przemysław)
- **TrustCenter:** Aktualizacje (Marek), poprawa SQL z slow logów
- **Aplikacja Mac:** Druga wersja z obsługą SignApp i rozpoznawaniem kluczy prywatnych (Adrian → Janusz do testów)
- **Allianz:** Warsztaty z klientem, ustalenia wdrożeniowe (Damian)
- **CRM faktury/paragony:** Draft umowy do poprawienia (uwagi od klientów)

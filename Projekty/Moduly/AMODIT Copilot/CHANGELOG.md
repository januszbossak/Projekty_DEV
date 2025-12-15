# CHANGELOG - AMODIT Copilot

## 2025-12-04 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-04 Spotkanie projektowe - AMODIT AI.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-04%20Spotkanie%20projektowe%20-%20AMODIT%20AI.md)
**Kategoria:** #Funkcjonalność #Decyzja

- **Generowanie dokumentacji procesów (PoC)** - funkcja automatycznego generowania dokumentacji dla konsultantów wdrożeniowych:
  - Wartość biznesowa: ~60 dni oszczędności działu wdrożeń rocznie (dokumentacja jest powtarzalna, często tworzona przez konsultantów i klientów)
  - Funkcjonalność: generuje opis procesu na podstawie konfiguracji (nazwy, pola, diagram etapów, sposób powstawania sprawy, reguły biznesowe)
  - Działanie: czat Copilot ze świadomością URL (np. procedury numer 821) - "wygeneruj dokumentację tej procedury"
  - Zakres MVP: PoC w grudniowej wersji (wydanie na początku stycznia 2026), feedback od konsultantów w styczniu
  - Szczegóły techniczne: diagram generowany w backendzie (poprawione proporcje), reguły biznesowe z numeracją globalną, restrykcje pól na etapach

**💭 Pomysł Przemka (propozycja):**
- Zakładka "Dokumentacja" w lewej zakładce procesu (zamiast tylko czatu)
- Możliwość generowania + wgrywania własnych plików dokumentacji
- Dokumentacja załączana do szablonu procesu (przenosi się między środowiskami)

**Wersjonowanie:**
- PBI oznaczane jako "AMODIT AI" (w nazwie zgłoszenia)
- Release Version: grudniowa (suggest version)
- Automatyczne przypisanie wersji przy Waiting for Release

**Zadania:**
- **Mateusz Kisiel:** Wysłać przykładową dokumentację do konsultantów (Mateusz Kołakowski, Daniel Reszka) na feedback
- **Damian Kamiński:** Wymusić na konsultantach używanie narzędzia i zgłaszanie uzupełnień

**Punkty otwarte:**
- Jak oznaczyć funkcje AI w changelogu? (automatyczny changelog z PBI)
- Czy tworzyć osobne środowisko "dokumentacja AI" (robocze)?

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-03 Spotkanie projektowe - Błędy formularzy i procedury aktualizacji.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-03%20Spotkanie%20projektowe%20-%20Błędy%20formularzy%20i%20procedury%20aktualizacji.md)  
**Kategoria:** #Problem #Funkcjonalność  
**Projekt:** [Moduly/Silnik-regul](../Silnik-regul/)

- **Problem z odpowiedziami Copilota** - Copilot nie odpowiada sensownie na pytania o funkcje bez znajomości dokładnej nazwy
- **Przykład:** Pytanie "jak ograniczyć wybór dat na formularzu" nie podpowiada funkcji `SetDateFilters` (mimo że istnieje)
- **Oczekiwanie:** Copilot powinien sensownie odpowiadać na problemy biznesowe, nie tylko na pytania wprost o nazwę funkcji
- **Kontekst:** Zgłoszono propozycję automatycznej walidacji dat, ale funkcje już istnieją - problem w tym, że Copilot ich nie podpowiada
- **Nakaz:** Absolutny nakaz używania Copilota przez zespół, uzupełnianie artykułów Wiki (obecnie tylko techniczne opisy)
- **Propozycja:** Przygotowywanie zadań z użyciem specyficznych funkcji dla podnoszenia świadomości zespołu

---


## 2025-12-02 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-02 Spotkanie projektowe - AMODIT UI.md]
**Kategoria:** #Funkcjonalność #Strategia #Architektura

- **Generowanie dokumentacji procesów przez AI** - priorytet strategiczny:
  - PoC gotowy (Mateusz) - automatyczne generowanie opisu procesu
  - Rozbudowa: checkboxy z wyborem typów dokumentacji (proces, ustawienia systemowe, raporty)
  - Wartość biznesowa: ~60 dni rocznie oszczędności (2-3 osobo-miesiące), LOT: ~6 dni
  - Licencjonowanie: funkcjonalność w ramach licencji AI (standard lub advanced - do ustalenia)
  - Przychody: możliwość sprzedaży klientom którzy sami tworzą procesy (np. Res Invest)
  
- **MCP (Model Context Protocol)** - integracja z zewnętrznymi agentami AI:
  - PoC gotowy (Mateusz, weekend) - podłączenie do AMODIT Copilot
  - Architektura: wystawienie tych samych endpointów co Copilot (NIE pełne API AMODIT)
  - Działanie w kontekście użytkownika, logowanie zapytań AI (audyt)
  - Wartość biznesowa: Rossmann zamówił (PoC 3 miesiące, ~50k zł rocznie), Polpharma i AmRest zainteresowani
  - Szacunkowo: ~200k zł rocznego przychodu z kilku dużych klientów
  - Ryzyka: wydajność, bezpieczeństwo, długa droga do produkcji
  
- **AI dla konsultantów (bez licencji klienta)**:
  - Mechanizm umożliwiający konsultantom używanie AI u klientów bez licencji
  - Preferowane rozwiązanie: OAuth + domena firmowa (@amodit.pl, @astrafox.pl)
  - Ewentualnie: token czasowy lub wewnętrzne hasło (dodatkowe zabezpieczenie)
  - Cel: przyspieszenie pracy konsultantów, demonstracja wartości AI klientom

---

## 2025-11-28 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-28%20Planowanie%20sprintu.md)
**Kategoria:** #Funkcjonalność #Zadanie

- Pilne wdrożenie mechanizmu JRWA w Copilocie (aby konsultanci mogli od początku korzystać z prawidłowych rejestrów).
- Implementacja JRWA - Filip Liwiński (kilka dni).
- Wymagane konsultacje z Markiem Dziakowskim.

---

## 2025-12-01 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Sprint review.md]
**Kategoria:** #Prototyp #Funkcjonalność

- Prototyp generowania dokumentacji procesu (opis, etapy, pola, reguły).
- Serwer MCP: AMODIT może łączyć się z zewnętrznymi MCP.
- Serwer MCP: Zewnętrzne narzędzia (Cursor) mogą wywoływać funkcje AMODIT.
- Feedback: Potrzeba roadmapy dla generowania dokumentacji.
- UX: Użytkownicy nie wiedzą o co pytać Copilota (potrzeba helpa/sugestii).

---

## 2025-11-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Notatka projektowa - AMODIT AI.md]
**Kategoria:** #Funkcjonalność #Architektura #Decyzja

- **MCP (Model Context Protocol):** Zaimplementowano stronę zarządzania MCP (/ajax/MCP) obsługującą typy stdio i remote.
- **Hosting MCP:** Preferowane centralne serwery MCP w AMODIT (wspólne dla klientów), z opcją lokalnych serwerów u klientów.
- **Built-in Server:** Propozycja wbudowanego serwera MCP reprezentującego natywne funkcje AMODIT (nieusuwalny, zarządzalny).
- **Automatyczna dokumentacja:** MVP 1 generowania dokumentacji procesu przez Copilot (stały prompt, format Word).
- **Zabezpieczenie:** Generowanie dokumentacji dostępne tylko dla administratorów systemowych i procesowych.
- **Analiza MCP:** Zlecono analizę biznesową dostępnych serwerów MCP (Chart, Mermaid, SQL) pod kątem użyteczności.

---

## 2025-11-25 | Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-25 Notatka projektowa - Roadmapa 2026 i Strategia Wdrożeniowa.md]
**Kategoria:** #Koncepcja #Strategia

-   **Strategia Wdrożeniowa:** Wykorzystanie AI do "wywiadu" z konsultantem/klientem w celu dostosowania procesu (Wizard Wdrożeniowy).
-   **Strategia Wdrożeniowa:** Zmiana mentalności działu wdrożeń dzięki AI.

---

## 2025-11-17 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-17 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-17%20Planowanie%20sprintu.md)
**Kategoria:** #Funkcjonalność #Dokumentacja

- Planowanie funkcjonalności generowania dokumentacji powdrożeniowej procesu przez AI.
- Koncepcja przycisku "Generuj dokumentację" w ustawieniach procesu.
- Wymagane przygotowanie schematu dokumentacji i promptu dla Copilota.

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Architektura #Zadanie #Problem

- Mateusz dorobił moduł dla usług AI.
- Możliwe kwestie RODO związane z modułem AI.
- Decyzja: Spisać konkluzje i pochylić się nad tematem na dedykowanym spotkaniu.
- Zadanie dla Damiana Kaminskiego (spisać konkluzje i rozpiąć na PBI).

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #Bezpieczeństwo

- POC: eksport wyników (Word/Markdown) i dostęp do spraw przez zapytania; działa na VIP, docelowo ma respektować uprawnienia via raporty tymczasowe.
- Podgląd logów OCR w bilingu (bez wchodzenia do bazy); sygnały o konieczności przepięcia klientów na nowy OCR i doprecyzowania potrzeb na poziomie pól.
- Przepisanie frontendu bazy wiedzy zgodnie z design systemem (szablon jak obszary/słowniki/źródła danych/klucze szyfrujące).
- Ryzyko bezpieczeństwa danych w Copilot/OCR: potrzeba szyfrowania, retencji i ewentualnego przechowywania danych u klienta (na on-prem) – temat zaparkowany do dalszych decyzji.

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność #Design

- Opcja przesyłania dokumentów do konwersacji (analiza treści dokumentu)
- Poprawa wyświetlania znaczników function calling (przycisk z ogólnym opisem zamiast kodu)
- Problem z brakiem trwałości przesłanych dokumentów (tylko na czas konwersacji)
- Zgłoszona potrzeba wyświetlania nazwy procesu przy uruchamianiu sprawy przez AI

---

## 2025-09-25 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-25%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność #Architektura

- **Usprawnienia bazy wiedzy:** Wprowadzenie administratorów baz wiedzy, możliwość wrzucania plików (np. PDF, Word) jako treści, zarządzanie datą ważności (od-do) dla treści oraz wersjonowanie treści (zachowanie starych wersji, filtrowanie bieżących/wygasłych).
- **Wsparcie dla istniejących formularzy:** AI do tłumaczenia formularzy na różne języki oraz automatycznego dodawania tooltipów do pól.

---

## 2025-09-18 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Planowanie%20sprintu.md)
**Kategoria:** #Funkcjonalność #AI #Architektura

**Baza wiedzy w Copilot – demo i wyjaśnienia** ✅
- **Kontekst:** Demo i wyjaśnienia funkcjonalności prywatnej bazy wiedzy w Copilot (jak dodawać dokumenty, uprawnienia, funkcje w silniku reguł).
- **Decyzje:**
  - ✅ Dokumenty do bazy wiedzy muszą być dodawane świadomie (brak auto-dodawania).
  - ✅ Zerwanie uprawnień do sprawy przy dodaniu dokumentu do bazy wiedzy (przejście na uprawnienia bazy wiedzy).
  - ✅ Prywatna baza wiedzy per instancja (izolacja danych między klientami).
- **Ryzyka:** Brak dokumentacji, optymalizacja zużycia tokenów, długi czas zapisu.
- **Funkcje silnika reguł:** `Knowledge Base Document Insert`, `Knowledge Base Search`, `Ask AI`, `Get To Do`.
- **Uprawnienia:** `Copilot Access` w ustawieniach systemowych, `Organization Key` (automatycznie), zarządzanie bazami wiedzy przez administratorów.
- **Problemy techniczne:** Długi czas zapisu, brak IntelliSense, brak tytułu przy dodawaniu z reguły, Metadata jako obiekt JSON.

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #AI

**Generowanie procesu przez Copilota (tryb konsultacyjny)** ✅
- **Zmiana podejścia:** Zamiast bezdusznego generowania z jednego polecenia → Tryb konsultacyjny
- **Zaimplementowano:**
  - Prompt analityczny (~20 kluczowych pytań)
  - Możliwość odpowiadania na pytania lub wrzucenia dokumentu wymagań
  - Podsumowanie ustaleń przed generowaniem JSON
  - Mechanizm sprawdzania statusu (polling) dla długich operacji (uniknięcie timeoutu na gateway)
- **Feedback:**
  - Ulepszyć spinner oczekiwania ("Model myśli...")
  - Zmienić nazwę przycisku "Switch To Process"

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność #Prezentacja

**Kontekst:**
Przegląd funkcjonalności AMODIT Copilot w ramach przygotowania artykułu informacyjnego o nowościach w AMODIT UI.

### Zastosowania i funkcjonalności

**1. Tworzenie nowych procesów:**
- Generowanie procesu na podstawie opisu słownego
- Efekt: szkic diagramu oraz szkic formularza
- Proces wielokrokowy (konwersacja, nie jeden prompt)
- Możliwość poprawiania na bieżąco, dopóki jest szkic
- Zatwierdzenie powoduje utworzenie procesu w AMODIT
- Proces powstaje "w pełni" – z nazwami etapów, tłumaczeniami, opisami

**2. Opis biznesowy procesu:**
- Analiza definicji procesu i przedstawienie opisu biznesowego
- Wyjaśnienie: po co jest proces, jak działa, jakie ma kroki, jakie dane są przyjmowane

**3. Pomoc w tworzeniu i edytowaniu reguł:**
- W edycji reguły można poprosić Copilota o opracowanie reguły
- Generowanie reguły w języku skryptowym AMODIT na podstawie tematu biznesowego
- Opisywanie istniejących reguł ("Napisz mi, co robi ta reguła")
- Działa na poziomie pojedynczej reguły (nie analizuje zbiorczo zależności między regułami)

**4. Wsparcie dla zwykłych użytkowników:**
- Copilot zna procesy i raporty w danym systemie
- Użytkownik może zapytać: "Mam do rozliczenia delegację, którego procesu powinienem użyć?"
- Copilot analizuje dostępne procesy, wskazuje odpowiedni i może uruchomić sprawę
- Podobnie z raportami: "Chciałbym przeanalizować raport sprzedażowy, z którego powinienem skorzystać?"

**5. Wiedza o AMODIT:**
- Zawiera praktycznie całą wiedzę dostępną na Wiki AMODIT (pełna dokumentacja)
- Pełna wiedza na temat wszystkich funkcji używanych w skryptach (z kodu źródłowego AMODIT)
- Odpowiada na ogólne pytania dotyczące systemu

**6. Baza wiedzy organizacji (warstwa prywatna):**
- Klienci mogą wrzucać do "Bazy Wiedzy" swoją wiedzę – regulaminy, instrukcje, opracowania
- Wiedza nie wychodzi poza organizację
- Użytkownicy mogą zadawać pytania dotyczące regulaminów i procedur
- Przykład: dział HR buduje bazę wiedzy, żeby pracownicy najpierw zadawali pytania do Copilota

**Szczegóły techniczne:**
- Funkcja `AddToKnowledgeBase` – możliwość dodawania informacji ze sprawy do bazy wiedzy
- Modele typu "embedding" wykorzystywane w bazie wiedzy
- Kierunek strategiczny: "AI Driven Workflow"

### Ograniczenia MVP

- Brak dostępu do danych transakcyjnych (pracownik nie może zapytać: "Ile jeszcze zostało mi urlopu?")
- W przyszłych wersjach dostęp do danych transakcyjnych będzie włączalny per organizacja
- Częściowo możliwe już teraz przez funkcję `AddToKnowledgeBase` na poziomie reguł
- Analiza zbiorcza zależności między regułami (działa tylko na poziomie pojedynczej reguły)

### Plany na przyszłość

- Projekt badawczy: Copilot jako "konsultant" – większa wiedza, wcześniejsze dopytywanie, sprawdzanie czy specyfikacja procesu jest pełna
- Wyciąganie danych dla konkretnego użytkownika zgodnie z jego uprawnieniami

---

## 2025-09-02 - Rada architektów

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-09-02 Rada architektów|2025-09-02 Rada architektów]]

**Kategoria:** #Problem

### Problemy z analizą procesów PKF

**Zgłoszenie:** Łukasz zgłosił problem z Copilotem przy próbie analizy procesów z PKF – jeden z procesów powoduje błąd "ups, coś poszło nie tak" mimo że proces jest trywialny.

**Status:** Problem przekazany do analizy Mateuszowi.

### Ceny Copilota

Rozmowa o podniesieniu cen Copilota, aby zarabiać na tej funkcjonalności. AI jest tańsze niż pracownik (np. Krystyna kosztowała kilka tysięcy złotych miesięcznie, AI kosztowałoby ułamek tego).

---

## 2025-08-26 - Ask AI – funkcja AI na poziomie sprawy

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność

**Cel:**
Otwarcie możliwości korzystania ze sztucznej inteligencji na poziomie pojedynczej sprawy, umożliwienie analizy dokumentów i danych ze sprawy przez AI.

### Funkcjonalność Ask AI

- Otwiera możliwości korzystania ze sztucznej inteligencji na poziomie pojedynczej sprawy
- Twórca procesu może wprowadzić do tej funkcji dowolną informację ze sprawy, np. treść dokumentu

### Przykłady zastosowań

- **Analiza zapytań ofertowych:** przychodzi zapytanie, jest poddawane OCR, tekst (razem ze specjalnym promptem) trafia do funkcji Ask AI, uzyskujemy ustrukturyzowaną odpowiedź (kluczowe daty, kwoty) oraz subiektywną ocenę AI – czy zapytanie jest dla nas interesujące
- **Analiza umów, regulaminów**
- **Wstępna analiza CV kandydatów:** sprawdzenie zgodności z oczekiwaniami, np. staż pracy, kwalifikacje

### Mechanizm

- Trochę jak pytanie ChatGPT "masz tu dokument i zrób z nim to", ale dzieje się to automatycznie w procesie

### Modele dostępne

- Możliwość korzystania ze wszystkich modeli dostępnych na platformie Microsoft Azure
- Dostępne są najnowsze modele GPT-4o, GPT-3.5, wersje mini, nano

### Bezpieczeństwo

- To nie jest ten sam model co publiczny ChatGPT
- Dane są przetwarzane przez Microsoft na terytorium Unii Europejskiej
- Microsoft zapewnia, że dane nie są wykorzystywane do trenowania modelu ani przechowywane (poza krótką historią konwersacji)

### Rozliczanie

- Klient nie musi tego opłacać osobno u dostawcy, rozlicza się z nami za użycie
- Pakiet darmowy na start, potem pay-as-you-go

### Szczegóły techniczne

- Integracja z Microsoft Azure
- Modele: GPT-4o, GPT-3.5, wersje mini, nano
- Przetwarzanie danych na terytorium Unii Europejskiej

---

## 2025-08-26 - AMODIT AI OCR – rozbudowany OCR

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Funkcjonalność

**Cel:**
Rozbudowa funkcjonalności OCR w kontekście AI Driven Workflow, umożliwienie odczytywania danych z różnych typów dokumentów (faktury, paragony, dokumenty kadrowe, umowy) oraz odczytywanie niestandardowych informacji.

### Potężne narzędzie w kontekście AI Driven Workflow

- Potrzebujemy odczytać dane z faktury czy paragonu
- Istnieją modele specjalizowane, ale bywają nieskuteczne
- Dorobiono "pre-processing" i "post-processing"

### Pre-processing

- Wykrywanie typu dokumentu (faktura czy paragon)
- Używanie odpowiedniego modelu w zależności od typu dokumentu

### Post-processing

- Jeśli standardowy OCR nie odczyta jakiejś informacji (np. daty sprzedaży), dopytujemy inny model (np. GPT-4o mini)

### Nowa funkcjonalność – odczytywanie niestandardowych informacji

- Możliwość poproszenia OCR o odczytanie niestandardowych informacji, których zwykły OCR nie czyta
- Przykłady:
  - Numer VIN samochodu z faktury
  - Dane z paszportu krowy (dla firm z branży hodowlanej) – rozczytać paszport i wyciągnąć dane do rejestracji zwierzęcia
  - Dokumenty kadrowe, umowy

### Modele

- Możliwość korzystania z modeli specjalizowanych (np. do dowodów osobistych, mandatów)
- Możliwość korzystania z ogólnych modeli LLM, którym dynamicznie mówimy, co mają odczytać
- Modele trenowane są lepsze przy dużej skali (dziesiątki tysięcy dokumentów), ale przy mniejszej skali modele ogólne świetnie sobie radzą

### E-teczki (elektroniczna dokumentacja pracownicza)

- Oferowane kompleksowe rozwiązanie: e-teczka z rozczytywaniem i klasyfikacją dokumentów
- System na podstawie danych z dokumentu wie, w którym miejscu teczki go zarejestrować

### Szczegóły techniczne

- Pre-processing: wykrywanie typu dokumentu
- Post-processing: dopytanie innego modelu (np. GPT-4o mini)
- Modele specjalizowane i ogólne LLM
- Integracja z e-teczkami
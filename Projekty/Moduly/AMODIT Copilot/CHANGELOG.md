# CHANGELOG - AMODIT Copilot

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


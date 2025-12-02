# Ustalenia organizacyjne - 2025-11-27 (Przegląd roadmapy DEV)

**Źródło:** Spotkanie Przegląd DEV (Przemysław Sołdacki, Janusz Bossak)
**Kategorie:** Procesy, Narzędzia, Standardy

---

## 1. Wizard eksportu/importu procesów między środowiskami

**Kategoria:** Narzędzia

### Kontekst

Wdrożeniowcy i serwisanci potrzebują mechanizmu przenoszenia procesów między środowiskami (TEST→PROD). Obecnie brak narzędzia do kompleksowego eksportu procesów z powiązaniami.

### Ustalenie

💡 **Pomysł Przemka:** Stworzyć wizard do eksportu/importu procesów z możliwością:
- Wyboru zakresu eksportu (wszystkie procesy / pojedyncze / wybrane)
- Automatycznego wykrywania powiązań (rejestry, słowniki, raporty)
- Świadomego wyboru elementów do przeniesienia (checkboxy)
- Kontroli nadpisywania na środowisku docelowym

**Status:** 💡 Do rozważenia - wymaga prac koncepcyjnych

### Szczegóły

**Wymagania:**
- Eksport poprzez pliki (nie API między środowiskami) - środowiska mogą być w różnych sieciach
- Wykrywanie powiązań: proces → rejestry (przez pole Odnośnik) → słowniki → raporty
- Ostrzeżenie o zagnieżdżonych zależnościach (proces → rejestr → inny proces przez Odnośnik)
- Ograniczenie głębokości drzewa zależności (aby nie eksportować "wszystkiego ze wszystkim")
- Podczas importu: kontrola nadpisywania istniejących elementów
- Śledzenie historii zmian (co było w eksportowanych plikach)

**Rozważane podejście:**
- Hierarchiczne drzewo zależności z możliwością wyboru (checkbox)
- Lista powiązanych elementów z możliwością dodania do eksportu
- Ostrzeżenia o konfliktach podczas importu

### Odpowiedzialny

**Damian Kamiński** - główny deweloper (½ Piotra Buczkowskiego do wsparcia)

### Planowane prace

**Szacowany nakład:** 3 miesiące (dedykowany zespół)
**Priorytet:** Wysoki - kluczowe dla wdrożeniowców i serwisantów
**Kwartał:** K2 2025 (propozycja)

---

## 2. Prace koncepcyjne nad wydajnością case_definition

**Kategoria:** Procesy / Narzędzia

### Kontekst

Duzi klienci (AmRest, MSIT) mają kilkanaście lat danych w bazie. Case_definition rośnie, zapytania SQL zwalniają. Potrzebne rozwiązanie wydajnościowe.

### Ustalenie

💭 **Pomysł Przemka:** Prace badawcze nad podziałem tabeli case_definition:
- Podział per proces (osobne tabele dla każdego procesu)
- Podział per rok (archiwizacja starych danych)
- Alternatywa: replikacja do Redis dla szybkiego czytania

**Status:** 🔍 Do weryfikacji - wymaga testów na dużych zbiorach danych

### Szczegóły

**Pytania badawcze:**
- Czy podział tabeli case_definition na mniejsze części da wzrost wydajności?
- Czy wydzielenie kolumn 1:1 do procesu (zamiast generycznych field1, field2) pomoże?
- Czy indeksy na mniejszych tabelach będą szybsze?
- Czy Redis jako cache dla odczytów da lepsze rezultaty?

**Historia:**
- Piotr Buczkowski prowadził próby przy AmRest (partycjonowanie bazy, wydzielanie tabel)
- Wniosek wstępny: niewielka poprawa wydajności
- Wymaga głębszej analizy i eksperymentów

**Inspiracje:**
1. Zmniejszenie rozmiaru bazy (archiwizacja starych lat)
2. Klienci chcą odłożyć dane sprzed lat, do których nie sięgają
3. Baza mniejsza = szybsze zapytania, mniejsze indeksy

### Odpowiedzialny

**Piotr Buczkowski** - prace koncepcyjne i testy wydajnościowe

### Planowane prace

**Etap 1:** Testy na bazie z milionem rekordów - podział na pół i porównanie wydajności
**Etap 2:** Jeśli daje efekt → implementacja mechanizmu
**Szacowany nakład:** 1-2 miesiące (prace badawcze)
**Kwartał:** K1 2025 (priorytet)

---

## 3. Archiwizacja i usuwanie starych danych

**Kategoria:** Procesy / Narzędzia

### Kontekst

Duzi klienci (AmRest, MSIT, WIM) mają 10-15 lat danych. Bazy są duże, zapytania wolne. Potrzebny mechanizm archiwizacji/usuwania starych danych.

### Ustalenie

💭 **Pomysł Przemka:** Mechanizm usuwania starych danych z zachowaniem referencji:
- Kopiowanie bazy (backup) przed operacją
- Algorytm sprawdzający zależności (pole Odnośnik do starych spraw)
- Usuwanie tylko danych, które nie są referencjonowane w nowych procesach
- Przebudowa indeksów po usunięciu

**Status:** 💡 Do wdrożenia (testowane na WIM - usunięto dane >3 lata)

### Szczegóły

**Przykład realizacji:**
- WIM: Wywalono wszystkie dane starsze niż 3 lata (brute force)
- Klient nie potrzebuje szczegółowych danych sprzed lat
- Raporty łączące dane z wielu lat są potrzebne tylko na ogólnym poziomie
- Stara baza pozostaje jako archiwum (read-only)

**Algorytm bezpiecznego usuwania:**
1. Podział na "starą bazę" i "nową bazę"
2. Sprawdzenie referencji: czy nowe procesy odnoszą się do starych spraw (przez pole Odnośnik)?
3. Jeśli TAK - pozostaw starą sprawę, jeśli NIE - usuń
4. Przebudowa indeksów po usunięciu

**Korzyści:**
- Drastyczne przyspieszenie (baza 5x mniejsza = 5x szybsza)
- Mniejsze zużycie zasobów serwera bazodanowego
- Stara baza dostępna jako archiwum (offline, nie obciąża systemu)

**Uwagi biznesowe:**
- Klienci (np. Neuca) mogą potrzebować danych audytowych sprzed lat - będą w archiwum
- Operacja wykonywana w weekend (z możliwością rollbacku do starej bazy)

### Odpowiedzialny

**Piotr Buczkowski** - algorytm i skrypt usuwania
**Konsultanci/Serwisanci** - wykonanie na środowisku klienta

### Planowane prace

**Priorytet:** Wysoki (bezpośrednia korzyść dla dużych klientów)
**Szacowany nakład:** 1-2 miesiące (algorytm + testy)
**Kwartał:** K2 2025

---

## 4. AI w konfiguracji szablonów procesów

**Kategoria:** Procesy / Narzędzia / Standardy

### Kontekst

Mateusz Kołakowski tworzy standardowe szablony procesów (np. teczka, rekrutacja). Każdy konsultant konfiguruje je trochę inaczej. Potrzebna standaryzacja.

### Ustalenie

💭 **Pomysł Przemka:** AI-assisted konfiguracja szablonów procesów:
- W definicji procesu pole na załączniki (w tym "wytyczne dla AI")
- Plik "wytyczne konfiguracji procesu" (przygotowany przez projektanta szablonu)
- Podczas importu/konfiguracji AI zadaje pytania z wytycznych
- Konsultant odpowiada, AI konfiguruje proces według reguł

**Status:** 💡 Propozycja - wymaga spotkania koncepcyjnego

### Szczegóły

**Wizja:**
1. Projektant szablonu tworzy proces + plik "jak skonfigurować ten proces"
2. Plik zawiera:
   - Pytania do klienta (np. "Kto ma mieć dostęp do wszystkich spraw?")
   - Instrukcje dla AI (np. "Jeśli nie chcą dodatkowej akceptacji → usuń etap X, regułę Y")
   - Konkretne mapowanie odpowiedzi na zmiany w procesie
3. Konsultant importuje szablon → AI wypytuje → AI konfiguruje

**Korzyści:**
- **Standaryzacja** - każdy konsultant konfiguruje tak samo
- **Jakość** - AI stosuje najlepsze praktyki zapisane w wytycznych
- **Szybkość** - automatyzacja powtarzalnych czynności

**Wymagania:**
- Bardzo dobrze przygotowane wytyczne (profesjonalny prompt)
- Testy na ludziach przed oddaniem AI
- Możliwość ręcznej konfiguracji (jeśli konsultant woli)

**Przykładowe pytania AI:**
- "Kto powinien mieć możliwość oglądania wszystkich spraw?"
- "Kto może zmieniać definicję procesu?"
- "Powyżej jakiej kwoty wymagana jest dodatkowa akceptacja?" (i wstawienie progu do reguły)

### Odpowiedzialny

**Mateusz Kołakowski** - szablony procesów i wytyczne
**Przemysław Sołdacki** - koncepcja AI i testy

### Planowane prace

**Etap 1:** Spotkanie koncepcyjne (Przemysław, Janusz, Mateusz Kołakowski, Mateusz Kisiel, Piotr Buczkowski)
**Etap 2:** Prototyp na jednym szablonie
**Szacowany nakład:** 2-3 miesiące
**Kwartał:** K3 2025

---

## 5. Testy end-to-end w Playwright z użyciem AI

**Kategoria:** Procesy / Narzędzia / Standardy

### Kontekst

Brak pokrycia testami automatycznymi. Testerki wykonują testy ręcznie. Potrzebne testy regresyjne (np. sprawdzenie czy aktualizacja biblioteki Design nie zepsuła stylów).

### Ustalenie

Stworzenie mechanizmu testów end-to-end w Playwright z użyciem AI:
- Testerki piszą scenariusze testowe w języku naturalnym
- Agent AI generuje skrypty Playwright
- Testerki nadzorują agenta i weryfikują testy
- **Bez angażowania programistów**

**Status:** ✅ Obowiązuje od K1 2025

### Szczegóły

**Workflow:**
1. Testerka opisuje "co trzeba testować" (język naturalny)
2. Agent AI generuje kod Playwright
3. Testerka sprawdza czy testy działają poprawnie
4. Jeśli nie - koryguje agenta ("kliknij ikonę X, nie Y")
5. Agent poprawia skrypt

**Page Object Model:**
- Janusz Bossak opracował Page Object Model (1-1,5 miesiąca pracy)
- Zawiera definicje wszystkich elementów formularza AMODIT (pole data, text, przycisk, etc.)
- AI korzysta z modelu do generowania testów
- Zmiana w modelu → aktualizacja wszystkich testów

**Przykłady testów:**
- Sprawdzenie czy nie pojawiły się ramki na guzikach (po aktualizacji biblioteki Design)
- Porównanie zrzutów ekranów (przed/po aktualizacji)
- Testy regresyjne procesów

**Korzyści:**
- Standaryzacja testowania (każdy tester testuje tak samo)
- Szybsze wykrywanie regresji
- Brak obciążenia programistów

**Rola testerek:**
- Przejście z "ręcznego klikania" na "nadzorowanie agenta"
- Pisanie scenariuszy testowych
- Weryfikacja poprawności testów AI
- Nie wymaga znajomości programowania (AI pisze kod)

### Odpowiedzialny

**Janusz Bossak** - Page Object Model (już wykonane)
**Testerki** - scenariusze testowe i nadzór AI
**Uwaga:** Programiści NIE są zaangażowani

### Planowane prace

**Priorytet:** Wysoki (element stabilizacji systemu)
**Kwartał:** K1 2025 (rozpoczęcie)
**Szacowany nakład:** 2-3 miesiące (wdrożenie mechanizmu)

---

## 6. Monitor wydajności na poziomie reguł

**Kategoria:** Narzędzia

### Kontekst

Serwisanci muszą ręcznie analizować logi aby znaleźć przyczynę spowolnienia systemu. Brak narzędzia do automatycznego wykrywania problematycznych reguł.

### Ustalenie

💭 **Pomysł Przemka:** AI-powered monitor wydajności:
- Analiza logów (co generuje najwięcej błędów / najbardziej zamula)
- Wykrywanie zmian w regułach (czy niedawno ktoś zmodyfikował regułę problematyczną)
- Automatyczne "śledztwo" wg standardowego algorytmu
- Raport dla serwisanta: "Reguła X spowalnia system, zmieniona wczoraj przez Y"

**Status:** 💡 Propozycja - wymaga prac koncepcyjnych

### Szczegóły

**Algorytm:**
1. Wyciągnięcie statystyk z logów (dzień / tydzień / miesiąc):
   - Co najbardziej zamula serwer?
   - Co generuje najwięcej błędów?
2. Sprawdzenie historii zmian (które reguły były modyfikowane ostatnio)
3. Analiza AI: czy zmiana reguły koreluje z problemem?
4. Profiler: w której linijce reguły występuje problem (wydajność / błąd)

**Korzyści:**
- **Standaryzacja diagnostyki** - każdy konsultant dostaje gotowe "śledztwo"
- Szybsze rozwiązywanie problemów klientów
- Nie wymaga wiedzy eksperckiej (jak Piotr Buczkowski)

**Nazwa narzędzia:** Analizator (nie debugger - analiza post factum, nie na bieżąco)

### Odpowiedzialny

**Mateusz Kisiel** - koncepcja i prototyp
**Piotr Buczkowski** - konsultacje (algorytm diagnostyki)

### Planowane prace

**Priorytet:** Średni
**Kwartał:** K4 2025 (lub później)
**Szacowany nakład:** 2 miesiące

---

## 7. Historia edycji procesów

**Kategoria:** Narzędzia

### Kontekst

Brak wglądu w historię zmian procesu. Potrzebne dla audytu i diagnostyki ("kto zmienił regułę, która się teraz wysypuje").

### Ustalenie

Wizualizacja historii edycji procesu w edytorze:
- Kto, kiedy, co zmienił
- Możliwość podglądu zmian (diff)
- Integracja z monitorem wydajności (wykrywanie problematycznych zmian)

**Status:** 💡 Do rozważenia

### Szczegóły

**Powiązanie z monitorem wydajności:**
- Monitor wykrywa problematyczną regułę
- Historia pokazuje kto i kiedy ją zmienił
- Serwisant ma pełny kontekst do diagnozy

**Wymagania:**
- Zapis historii zmian w bazie
- Wizualizacja w edytorze procesu
- Filtrowanie (po osobie, dacie, typie zmiany)

### Odpowiedzialny

**[DO USTALENIA]**

### Planowane prace

**Priorytet:** Niski (nice-to-have)
**Kwartał:** K3-K4 2025

---

## 8. Poprawki w module raportowym

**Kategoria:** Narzędzia

### Kontekst

Moduł raportowy wymaga stabilizacji i usprawnienia. "Puszka Pandory" - wiele rzeczy do poprawienia.

### Ustalenie

Prace stabilizacyjne i usprawnienia w module raportowym.

**Status:** 💡 Do uszczegółowienia

### Szczegóły

**Uwaga:** Nazwa "poprawki" może sugerować błędy - lepiej "stabilizacja" lub "usprawnienia"
**Zakres:** Do doprecyzowania (lista 50+ elementów do poprawienia)

**Podejście:**
- Prace koncepcyjne nad priorytetyzacją
- Dedykowany zespół na 3 miesiące (2 zespoły: raporty + przenoszenie procesów)

### Odpowiedzialny

**[DO USTALENIA]** - dedykowany zespół

### Planowane prace

**Priorytet:** Wysoki
**Kwartał:** K2 2025
**Szacowany nakład:** 3 miesiące (dedykowany zespół)

---

## 9. Zarządzanie wymaganiami (Requirements Management)

**Kategoria:** Procesy / Narzędzia

### Kontekst

Brak systemu do zarządzania wymaganiami procesów. Edytor procesu mógłby być zintegrowany z systemem wymagań.

### Ustalenie

💡 **Propozycja:** Moduł zarządzania wymaganiami powiązany z edytorem procesów

**Status:** 💡 Do rozważenia (powiązane z AI w konfiguracji szablonów)

### Szczegóły

**Wizja:**
- Możliwość wgrywania dokumentów do definicji procesu
- Powiązanie wymagań z elementami procesu
- Śledzenie pokrycia wymagań (które wymagania są zrealizowane w procesie)

**Powiązanie z AI:**
- Plik "wytyczne dla AI" jako rodzaj wymagań
- AI czyta wymagania → konfiguruje proces

### Odpowiedzialny

**[DO USTALENIA]**

### Planowane prace

**Priorytet:** Średni
**Kwartał:** K3-K4 2025

---

## Zmiany w stosunku do poprzednich ustaleń

| Było | Jest | Data zmiany |
|------|------|-------------|
| Brak formalnej roadmapy | Roadmapa Q1-Q4 2025 z priorytetami | 2025-11-27 |
| Testy ręczne przez testerki | Testy automatyczne Playwright z AI | 2025-11-27 |

---

## Do wdrożenia / Action items

- [ ] **Przemysław Sołdacki:** Zaplanować spotkanie koncepcyjne w Warszawie (Janusz, Mateusz Kołakowski, Mateusz Kisiel, Piotr Buczkowski) - temat: AI w konfiguracji szablonów + roadmapa → termin: środa (po poniedziałku/wtorku gdy Janusz w Warszawie)
- [ ] **Piotr Buczkowski:** Rozpocząć prace koncepcyjne nad wydajnością case_definition (testy na dużych zbiorach) → termin: K1 2025
- [ ] **Janusz Bossak + Testerki:** Wdrożyć mechanizm testów Playwright z AI (bez angażowania deweloperów) → termin: K1 2025
- [ ] **Damian Kamiński + ½ Piotra:** Rozpocząć prace nad wizardem eksportu/importu procesów → termin: K2 2025
- [ ] **Team:** Doprecyzować zakres prac w module raportowym → termin: przed K2 2025

# Daily – 2025-10-15

**Data:** 15 października 2025, 07:19
**Projekty:** `Organizacja-DEV/Dokumentacja-organizacyjna`, `Klienci/WIM/Repozytorium-plikow-DMS`, `Moduly/AMODIT Copilot`, `Moduly/CallRest`, `cross-cutting/Bezpieczenstwo-pentesty`
**Uczestnicy:** Janusz Bossak, Lukasz Bott, Patrycja Walaszczyk, Adrian Kotowski, Anna Skupinska, Damian Kaminski, Oktawia Ostrowska, Kamil Dubaniowski, Lukasz Brocki, Mateusz Kisiel, Marek Dziakowski, Piotr Buczkowski, Przemysław Rogaś, Filip Liwiński, Barbara Michalek, Mariusz Piotrzkowski, Michal Zwierzchowski

---

## 1. Status prac

### Patrycja Walaszczyk
- **Wczoraj:** Testy matrycy uprawnień, modułu raportowego
- **Dzisiaj:** Kontynuacja regresu (głównie matryca uprawnień, tam gdzie jest "przesyt"), moduł raportowy

### Adrian Kotowski
- **Wczoraj:**
  - Spotkanie dot. Azure Key Vault (produkcja działa, czekamy na "dark demo problem")
  - Aplikacja dla Maca - przepracowanie rozpoznawania kluczy prywatnych (problem ze starymi kluczami na smart card)
- **Dzisiaj:**
  - Przygotowanie 2. wersji aplikacji SignApp (Mac) - obsługa podpisów kwalifikowanych (SignApp) + rozpoznawanie kluczy
  - Wysłanie do Janusza do testów (jedyny ma Maka)

### Anna Skupińska
- **Wczoraj:** Praca nad dashboardami (poprawki zapisu, drobne błędy)
- **Dzisiaj:**
  - Kolejna wersja na branchu
  - Oczekiwanie na kolejne dashboardy systemowe
  - **Plan:** Zastąpienie ujemnych ID przez GUID w źródłach systemowych (zanim zaczniemy głębsze zmiany)

### Damian Kamiński
- **Wczoraj:**
  - Spotkania Allianz (warsztat, status wewn., spotkanie z wdrożeniowcami - brak opiekuna, Damian przejmuje rolę)
  - Rada Architektów (raporty systemowe)
  - Spotkanie projektowe (planowanie/usprawnienie pracy)
  - Prace Orlen, Zimbra (wdrożenie faktur)
- **Dzisiaj:** Praca nad blogiem, spotkanie z konsultantami

### Oktawia Ostrowska
- **Wczoraj:** Moduł raportowy, logi systemowe, konsultacje
- **Dzisiaj:** Logi systemowe + zadanie Marka (TrustCenter)

### Kamil Dubaniowski
- **Wczoraj:**
  - Wsparcie sprzedaży (IMG + Lucyna - odpowiedzi do oferty)
  - Planowanie sprintu
  - Spotkanie projektowe z Przemkiem (matryca uprawnień - uwagi do wyglądu/dziedziczenia)
- **Dzisiaj:**
  - Planowanie (ustalenie planu Daily)
  - Design (dobranie tematów, np. lista reguł z Przemkiem)
  - Spotkanie z konsultantami

### Łukasz Brocki
- **Wczoraj:** Bugi + temat e-Nadawcy (przesyłka idzie do nowego zbioru - analiza czy to u jednego klienta czy globalnie po aktualizacji)
- **Dzisiaj:** Dalsza analiza e-Nadawcy, bugi

### Łukasz Bott
- **Wczoraj:**
  - Dyskusja o raportach systemowych
  - Wsparcie sprzedaży (CRM faktury/paragony - draft umowy, uwagi klientów)
- **Dzisiaj:**
  - Spotkania piątkowe
  - Konsultacje z Kamilem Spyrą (PKF)
  - Raporty systemowe - opisy
- **Zgłoszenie:** Opisy w raportach/dashboardach nie działają w trybie podglądu (tylko edycja), brak tooltipów

### Mateusz Kisiel
- **Wczoraj:**
  - Zmiany wizualne w komunikatorze
  - Obsługa grup monitorowych (kontynuacja)
- **Dzisiaj:** Spotkanie z Neuką (12:00), rozwój Oceana (?? - *możliwy błąd ASR, może chodzi o "Oceana" jako projekt lub "Asystenta"*), obsługa plików przez Copilot

### Marek Dziakowski
- **Wczoraj:**
  - Poprawki testów wolnych (fake tests)
  - Aktualizacja TrustCenter
- **Dzisiaj:**
  - Poprawa SQL w TrustCenter (na podstawie slow logs zgłoszonych przez Piotra)
  - Mniejsze zgłoszenia

### Piotr Buczkowski
- **Wczoraj:**
  - Zmiany w "next string" dla słowników zagnieżdżonych (ktoś "spartolił", naprawione)
  - e-Doręczenia (z Adrianem na serwerze 2) - błąd przy współdziałaniu kilku jobów (błąd przy odświeżaniu listy pól na sprawie)
  - Konsultacje (przenoszenie plików - tabela z plikami 300GB w bazie zamiast na dysku u klienta)
  - Mechanizm zmiany typów kolumn w historii (text -> medium text)
- **Dzisiaj:** Dokończenie wczytywania parametrów na sprawę

### Przemysław Rogaś
- **Wczoraj:** Poprawka przekierowania z listy spraw do raportu/diagramu
- **Dzisiaj:** Nowe zadania z edytora (lista procesów, raporty)

### Filip Liwiński
- **Wczoraj:** Lista pól edytora formularza (akcje odświeżania logów, placeholder przy pustych tabelach, uprawnienia czyszczenia filtrów)
- **Dzisiaj:** Ujednolicenie wyglądu filtrów w logach systemowych

### Barbara Michałek
- **Wczoraj:** Zadania na sprawie, spotkanie moduł raportowy (bugi)
- **Dzisiaj:** Zadania priorytet 1 (internal testy, komunikator, filtr aktywności administracyjnej)
- **Inne:** Nagła wizyta u lekarza (15:00), nie będzie na spotkaniu z konsultantami

### Mariusz Piotrzkowski
- **Wczoraj:**
  - Błąd pola Odnośnik (źle wyświetlał tytuł sprawy - 4.5h debugowania, banalne rozwiązanie)
  - Zmiana logiki wyświetlania przycisków akcji
  - Próba naprawy błędu Copilot z tabelą JSON (nieudana, "takie głupoty wypisuje")
- **Dzisiaj:** Kontynuacja logiki przycisków, temat podformularza jako wymagane

### Michał Zwierzchowski
- **Wczoraj:** Porządki po wersji na storage, usuwanie statusów z Boarda (problem z wyświetlaniem hotfixów/bugów po usunięciu "in-design")
- **Dzisiaj:** Aktualizacja środowisk (Wiki), automatyzacja wydania, wieczorem aktualizacja strefy ręce

---

## 2. Tematy Projektowe i Architektoniczne

### Repozytorium plików (WIM)
**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

*   **Status:** Projektowanie / Koncepcja
*   **Architektura:** Decyzja o budowie repozytorium jako **aplikacji zewnętrznej** (podobnie jak Komunikator), wpiętej w AMODIT (zakładka), ale z osobną bazą danych (lub strukturami).
    *   **Piotr Buczkowski:** Sugeruje, że docelowo powinno to być jednak **wewnątrz AMODIT** (wykorzystanie obecnych struktur), aby umożliwić łatwe integracje ze sprawami (wpinanie plików do sprawy, start sprawy z pliku).
    *   **Damian Kamiński:** Na potrzeby MVP i szybkiego dowiezienia dla WIM (grudzień), robimy to jako **osobny byt** (łatwiej/szybciej), z założeniem późniejszej migracji/integracji.
*   **MVP (na grudzień):**
    *   Zarządzanie strukturą folderów (przestrzenie).
    *   Wgrywanie/pobieranie plików.
    *   Brak zaawansowanych uprawnień na poziomie każdego folderu (tylko na poziomie "przestrzeni" - dziedziczenie w dół).
    *   Brak integracji ze sprawami w MVP.
*   **Ryzyka:** Klient (Piotr z WIM) może podważyć uproszczony model uprawnień. Damian przygotuje demo/opis, żeby to "sprzedać".

### Copilot i MCP (Model Context Protocol)
**Projekt:** `Moduly/AMODIT Copilot`

*   **Status:** Prototypowanie
*   **Co zrobiono:** Mateusz Kisiel stworzył prototyp serwera MCP w AMODIT. Umożliwia to podłączenie zewnętrznych narzędzi AI (np. **Cursor**, **ChatGPT Desktop**) do AMODITa i "odpytywanie" go o dane (np. "jakie są procesy?").
*   **Problem:** Uwierzytelnianie. Obecnie użytkownik musi wygenerować sobie **token** (ważny np. 30-90 dni) i wkleić go do narzędzia.
    *   **Przemek Sołdacki:** Chciałby, żeby to działało "przezroczyście" (single sign-on, np. przez konto MS/AD), bez ręcznego generowania tokenów co miesiąc.
    *   **Mateusz:** Narzędzia typu Cursor/Claude nie przekazują kontekstu logowania użytkownika, więc token jest konieczny.
*   **Zastosowanie:** Np. generowanie dokumentacji systemu przez zewnętrznego agenta AI, który "widzi" strukturę AMODITa.

### Bezpieczeństwo danych AI i OCR
**Projekt:** `cross-cutting/Bezpieczenstwo-pentesty`

*   **Zgłoszenie (Przemek):** Baza danych Copilota i OCR przechowuje **ekstremalnie wrażliwe dane** (wszystkie odczytane faktury, dokumenty kadrowe, pytania do AI). Obecnie zabezpieczenia mogą być niewystarczające.
*   **Wymagania:**
    *   Silne zabezpieczenie dostępu do bazy.
    *   **Szyfrowanie danych** w bazie (nie plain text).
    *   **Retencja danych** (automatyczne usuwanie po czasie).
    *   **Przechowywanie u klienta:** Dla klientów On-Premise, dane wrażliwe (treść dokumentów, wyniki OCR) powinny być w ich bazie, a do nas (chmura billingowa) powinny trafiać tylko metadane do rozliczeń (ilość stron, typ dokumentu), bez treści.
*   **Decyzja:** Temat zaparkowany do pilnego omówienia ("Mega ważny temat").

### Architektura i Procesy (Konsultacje)
**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna`

*   **Problem:** Deweloperzy (np. Adrian, Mateusz, Łukasz) wdrażają rozwiązania (np. Komunikator, e-Doręczenia, CallRest dla KSeF) bez konsultacji architektonicznej z Piotrem, co prowadzi do błędów projektowych i konieczności poprawek ("cofamy się do projektowania").
*   **Ustalenie:**
    *   Każdy nowy pomysł/projekt musi mieć **opis systemowy** (jak to działa pod spodem).
    *   Piotr musi ten opis **zaakceptować** przed wdrożeniem.
    *   Piotr ma być odciążony od "bieżączki", aby mieć czas na te konsultacje.
    *   Metodologia "Amigos" (Developer + Biznes + Tester) wspomniana jako dobra praktyka.

---

## 3. Tematy organizacyjne i inne

### Propozycja: Czyszczenie backlogu bugów
*   **Autor:** Damian Kamiński
*   **Pomysł:** Zmiana statusu wszystkich starych bugów na "removed", a następnie wznawianie tylko tych faktycznie potrzebnych/zgłoszonych ponownie.
*   **Cel:** Odgruzowanie backlogu, realne planowanie sprintów.
*   **Status:** Propozycja do dyskusji (wymaga zgody Janusza).

### Problem z Windows 10
*   Wsparcie kończy się 15 października 2025.
*   Kamil Dubaniowski i Łukasz Bott mają sprzęt niekompatybilny z Windows 11.
*   Konieczna wymiana sprzętu w ciągu roku.

### Bug - strona logowania (2 obrazki)
*   Na stronie logowania wyświetlają się 2 obrazki (logo + alternatywa?).
*   Problem pojawił się po ostatniej aktualizacji (piątek).
*   Michał wgra poprawkę przy wieczornej aktualizacji.

### Changelog (Automatyzacja)
*   Łukasz Bott generuje changelog przy użyciu AI na podstawie zgłoszeń z Azure DevOps (Done).
*   Usprawnia to proces, ale wymaga weryfikacji (żeby nie wyciekły nazwy klientów/dane wrażliwe).

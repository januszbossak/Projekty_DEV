# Rada Architektów – 2025-10-23

**Powiązane projekty:**
- `cross-cutting/Zakladka-Do-wykonania` – temat 1
- `moduly/Modul-raportowy` – tematy 2, 3
- `moduly/Repozytorium-plikow-DMS` – temat 4

---

## 1. Zakładka "Do wykonania" w widoku "Wszystkie procesy"

**Projekt:** `cross-cutting/Zakladka-Do-wykonania`

### Kontekst i Problem

W zakładce "Wszystkie procesy" wyświetla się zakładka "Do wykonania", która nie powinna się tam pojawiać niezależnie od konfiguracji obszarów. Zakładka "Do wykonania" powinna być widoczna tylko w kontekście pojedynczego procesu, a nie w widoku wszystkich procesów.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Zakładka "Do wykonania" ma się w ogóle nie wyświetlać w zakładce "Wszystkie procesy", niezależnie od konfiguracji obszarów. Zadanie przypisane do Piotra Buczkowskiego, ponieważ logika wyświetlania przychodzi z backendu.

### Zadania

- **Piotr Buczkowski:** Ukrycie zakładki "Do wykonania" w widoku "Wszystkie procesy" → termin: nie określono

### Punkty otwarte

Brak.

---

## 2. Eksport danych do szablonów XSLT – rozszerzenie pliku

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

W ustawieniach eksportu można wybrać szablon XSLT oraz rozszerzenie pliku wynikowego. Problem polega na tym, że niezależnie od wybranego rozszerzenia, zawartość pliku jest taka sama – zmienia się tylko rozszerzenie w nazwie pliku. Rozszerzenie powinno być przypisane do szablonu, ponieważ szablon XSLT generuje konkretny format (np. Excel, CSV, XML), a nie jest to dowolny wybór użytkownika.

### Zidentyfikowane Ryzyka

- Możliwość wprowadzenia użytkownika w błąd – plik z rozszerzeniem CSV może faktycznie zawierać XML
- Brak spójności między rozszerzeniem a zawartością pliku

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozszerzenie przypisane do szablonu | W definicji szablonu XSLT zapisujemy oczekiwane rozszerzenie pliku, które jest automatycznie ustawiane przy wyborze szablonu | ✅ Wybrana – zapewnia spójność między szablonem a rozszerzeniem |
| Pozostawienie wyboru rozszerzenia użytkownikowi | Użytkownik sam wybiera rozszerzenie niezależnie od szablonu | ❌ Odrzucona – prowadzi do niespójności (rozszerzenie CSV przy zawartości XML) |
| Analiza szablonu i automatyczne wykrywanie rozszerzenia | System analizuje szablon XSLT i automatycznie wykrywa format | ❌ Odrzucona – zbyt skomplikowane, niepewne |

### Decyzja

**Status:** ✅ Zatwierdzone

W nowym interfejsie React rozszerzenie pliku będzie przypisane do definicji szablonu XSLT. Po wyborze szablonu rozszerzenie będzie automatycznie ustawiane i wyświetlane jako tylko do odczytu (lub całkowicie ukryte). W starym interfejsie pozostaje obecna funkcjonalność dla kompatybilności wstecznej.

**Szczegóły techniczne:**
- Rozszerzenie zapisywane w definicji szablonu w procesie
- W starym interfejsie: jeśli szablon nie ma przypisanego rozszerzenia, użytkownik może je wybrać
- W nowym interfejsie React: rozszerzenie zawsze pobierane z definicji szablonu, bez możliwości zmiany

### Zadania

- **Anna Skupinska:** Przygotowanie PBI definiującego wymagania dotyczące przypisania rozszerzenia do szablonu XSLT → termin: nie określono
- **Anna Skupinska:** Rozszerzenie GraphJSON o możliwość zapisania informacji o rozszerzeniu pliku w definicji szablonu → termin: nie określono

### Punkty otwarte

- Lokalizacja eksportu do szablonu XSLT w interfejsie – Damian Kaminski chce przedyskutować z Kamilem i Januszem, czy powinno być w akcjach masowych zamiast w ustawieniach eksportu
- Czy eksport do szablonu XSLT powinien być dostępny jako akcja masowa (zaznaczenie spraw + przycisk eksportu) zamiast w ustawieniach eksportu

---

## 3. Logowanie SQL w nowych raportach

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

W starych raportach przy błędzie wykonania zapytania SQL logowany jest pełny tekst zapytania SQL wraz z parametrami. W nowych raportach React ta funkcjonalność nie działa poprawnie – błędy SQL nie zawierają pełnej treści zapytania, co utrudnia diagnozowanie problemów.

### Zidentyfikowane Ryzyka

- Trudności w diagnozowaniu błędów raportów – brak pełnej informacji o zapytaniu SQL
- Utrudnione wsparcie serwisowe – brak możliwości odtworzenia problemu bez pełnego zapytania

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Użycie AmodDBCommand zamiast standardowego DBCommand | Nowe raporty używają AmodDBCommand, który automatycznie loguje SQL przy błędach | ✅ Wybrana – wykorzystuje istniejącą infrastrukturę logowania |
| Dodanie logowania SQL w funkcji DatabaseError | Rozszerzenie istniejącej funkcji DatabaseError w SQLBuilder o logowanie pełnego zapytania | ⏸️ Odroczona – wymaga analizy, czy funkcja już to robi |
| Własna implementacja logowania SQL | Stworzenie nowego mechanizmu logowania specyficznego dla nowych raportów | ❌ Odrzucona – duplikacja istniejącej funkcjonalności |

### Decyzja

**Status:** 🔍 Do weryfikacji

Anna Skupinska ma przeanalizować, dlaczego logowanie SQL nie działa w nowych raportach. Kod logowania już istnieje w funkcji `DatabaseError` w `AmodReportPreview.SQLBuilder`, ale prawdopodobnie nie jest używany lub nie działa poprawnie. Możliwe przyczyny:
- Używany jest standardowy DBCommand zamiast AmodDBCommand
- Funkcja DatabaseError nie jest wywoływana dla wszystkich typów błędów
- Problem z wersją kodu (starsze wersje mogą nie mieć tej funkcjonalności)

**Szczegóły techniczne:**
- Funkcja `DatabaseError` w `AmodReportPreview.SQLBuilder` powinna logować SQL przy błędach
- Funkcja `GetCommandInfo` w starych raportach loguje pełną treść zapytania SQL z parametrami
- Nowe raporty generują SQL samodzielnie przez SQL Builder
- Funkcja `DatabaseError` zapisuje również ID loga dla łatwiejszej identyfikacji błędu

### Zadania

- **Anna Skupinska:** Analiza przyczyn braku logowania SQL w nowych raportach → termin: nie określono
- **Anna Skupinska:** Weryfikacja, czy funkcja DatabaseError jest wywoływana dla wszystkich typów błędów SQL → termin: nie określono
- **Anna Skupinska:** Sprawdzenie, czy używany jest AmodDBCommand zamiast standardowego DBCommand → termin: nie określono

### Punkty otwarte

- Czy problem dotyczy tylko błędów w bazie danych, czy również innych błędów w kodzie poza bazą danych?
- W jakiej wersji AMODIT wprowadzono logowanie SQL w funkcji DatabaseError?
- Czy klienci z starszymi wersjami potrzebują aktualizacji, aby uzyskać logowanie SQL?

---

## 4. Repozytorium plików – wymagania techniczne

**Projekt:** `moduly/Repozytorium-plikow-DMS`

### Kontekst i Problem

Damian Kaminski przedstawił koncepcję repozytorium plików w AMODIT (niezwiązanego ze sprawami) z funkcjonalnością przestrzeni, folderów, plików i zarządzania uprawnieniami. Wymaga to ustalenia wymagań technicznych dotyczących przechowywania plików, struktury folderów na dysku oraz sposobu mapowania struktury logicznej na strukturę fizyczną.

### Zidentyfikowane Ryzyka

- Problemy z długimi ścieżkami w systemie Windows (limit 260 znaków)
- Trudności w diagnostyce przy użyciu tylko ID zamiast czytelnych nazw folderów
- Konflikty nazw przy użyciu skrótów nazw (np. "Dokumentacja projektowa" i "Dokumentacja projektu Beta" → oba jako "Dokumentacja")
- Problemy z backupem i zarządzaniem przy przechowywaniu w bazie danych dla dużych plików

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Przechowywanie w osobnej tabeli, pliki na dysku | Oddzielna tabela dla metadanych, pliki przechowywane zgodnie z ustawieniami systemowymi (jak pliki ze spraw) | ✅ Wybrana – zgodne z obecną architekturą AMODIT |
| Przechowywanie w bazie danych (Blob) | Wszystkie pliki przechowywane w bazie danych | ❌ Odrzucona – problemy z rozmiarem bazy, backupem, zalecenia dla dużych klientów mówią o przechowywaniu poza bazą |
| Struktura folderów odzwierciedlająca strukturę logiczną | Foldery na dysku mają takie same nazwy jak w interfejsie | ⏸️ Odroczona – wymaga analizy ograniczeń Windows |
| Struktura folderów oparta na ID | Foldery nazywane tylko ID (np. "12345") | ❌ Odrzucona – brak czytelności dla diagnostyki |
| Struktura folderów oparta na skrótach nazw | Pierwsze 5-10 znaków nazwy jako nazwa folderu | ❌ Odrzucona – konflikty przy podobnych nazwach |
| Struktura folderów oparta na ID z możliwością odczytania ścieżki | ID w folderach, ale ścieżka dostępna w adresie URL interfejsu | ✅ Wybrana – kompromis między czytelnością a unikalnością |

### Decyzja

**Status:** ✅ Zatwierdzone

Repozytorium plików będzie wykorzystywać:
- Oddzielną tabelę dla metadanych (przestrzenie, foldery, pliki)
- Przechowywanie plików na dysku zgodnie z ustawieniami systemowymi (jak pliki ze spraw), możliwość skonfigurowania osobnego folderu dla repozytorium
- Strukturę folderów opartą na ID (unikalne identyfikatory), ale z możliwością odczytania pełnej ścieżki logicznej w adresie URL interfejsu
- Ścieżka w adresie URL będzie zawierać pełną nazwę przestrzeni/folderu, co pozwoli na skopiowanie i wklejenie do Eksploratora Windows

**Szczegóły techniczne:**
- Oddzielne ustawienie dla folderu przechowywania plików repozytorium (możliwość ustawienia na ten sam folder co pliki ze spraw, ale z osobnym folderem głównym "Repository")
- Struktura folderów: `Repository/{ID_Przestrzeni}/{ID_Folderu}/...` lub podobna
- Ścieżka w URL: `/repository/Architektura-systemu/Diagramy/...` (czytelna dla użytkownika)
- Mapowanie między ścieżką logiczną a strukturą fizyczną przez ID

### Zadania

- **Damian Kaminski:** Przygotowanie wymagań na poziomie ogólnym z podziałem na zadania → termin: dzisiaj (23.10.2025)
- **Piotr Buczkowski:** Przejrzenie wymagań i weryfikacja zagrożeń/ryzyk na poziomie globalnym → termin: nie określono (wymaga dużo pracy, dużo czytania, dużo analizy)
- **Piotr Buczkowski:** Analiza sposobu przechowywania plików i struktury folderów na dysku → termin: nie określono
- **Piotr Buczkowski:** Poszukanie inspiracji w innych rozwiązaniach repozytoriów plików dotyczących struktury folderów → termin: nie określono

### Punkty otwarte

- Czy obsługiwać przechowywanie plików w bazie danych (Blob) jako opcję, czy tylko na dysku?
- Jakie ograniczenia Windows dotyczą długości ścieżek i zagnieżdżenia folderów?
- Czy "widoczność folderu" bez dostępu do zawartości ma sens, czy powinno być tylko dziedziczenie uprawnień?
- Jak obsłużyć sytuację, gdy użytkownik ma dostęp tylko do pojedynczego pliku w folderze, do którego nie ma dostępu – czy pokazywać strukturę folderów nadrzędnych?

---

## 5. Problem z instalacją AMODIT – błąd "Said can't build"

**Projekt:** Nowy temat / do sklasyfikowania

### Kontekst i Problem

Klient (Tomasz Kalinowski) podczas instalacji AMODIT otrzymuje błąd "Said can't build". Uprawnienia puli aplikacji są nadane do folderu, gdzie znajduje się AMODIT. Problem może być związany z TLS/HTTPS lub ograniczeniami Windows 11 dotyczącymi localhost.

### Zidentyfikowane Ryzyka

- Problemy z instalacją AMODIT u klientów
- Możliwe problemy z konfiguracją TLS/HTTPS w środowisku klienta

### Rozważane alternatywy

Jedna propozycja diagnozy, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Problem wymaga dokładniejszej diagnozy. Możliwe przyczyny:
- Problem z TLS/HTTPS przy próbie dostępu do Alfresco (nieskonfigurowany TLS lokalnie)
- Ograniczenia Windows 11 dotyczące localhost (nowsze przeglądarki i Windowsy dodają ograniczenia)
- Problem z konfiguracją domeny testowej (np. "astrafox.mod.com" przekierowującej na localhost)

**Szczegóły techniczne:**
- Windows 11 może mieć ograniczenia dotyczące loopback, których nie można wyłączyć
- Problem może dotyczyć mechanizmu wyboru bazy na podstawie adresu (np. "astrafox.amod.info")

### Zadania

- **Damian Kaminski:** Wsparcie klienta w diagnozie problemu z instalacją → termin: w ciągu dnia (23.10.2025)
- **Piotr Buczkowski:** Analiza problemu z TLS/HTTPS i ograniczeniami Windows 11 → termin: nie określono

### Punkty otwarte

- Jaka jest dokładna przyczyna błędu "Said can't build"?
- Czy problem dotyczy tylko Windows 11, czy również innych wersji?
- Jak obsłużyć ograniczenia Windows 11 dotyczące localhost w kontekście testowych domen?


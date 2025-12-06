# Rada Architektów – 2025-10-23

**Powiązane projekty:**
- `cross-cutting/Zakladka-Do-wykonania`
- `Moduly/Modul-raportowy`
- `Klienci/WIM/Repozytorium-plikow-DMS`
- `cross-cutting/Bezpieczenstwo-pentesty`

---

## 1. Zakładka "Do wykonania" w widoku "Wszystkie procesy"

**Projekt:** `cross-cutting/Zakladka-Do-wykonania`



### Kontekst i Problem

W zakładce "Wszystkie procesy" wyświetla się zakładka "Do wykonania", która nie powinna się tam pojawiać niezależnie od konfiguracji obszarów. Zakładka "Do wykonania" ma być widoczna tylko w kontekście pojedynczego procesu, a nie w widoku wszystkich procesów.

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

**Projekt:** `Moduly/Modul-raportowy`



### Kontekst i Problem

W ustawieniach eksportu można wybrać szablon XSLT oraz rozszerzenie pliku wynikowego. Problem: niezależnie od wybranego rozszerzenia zawartość pliku jest identyczna – zmienia się tylko rozszerzenie w nazwie. Rozszerzenie powinno być przypisane do szablonu, bo szablon XSLT generuje konkretny format (np. Excel/CSV/XML), a nie jest to dowolny wybór użytkownika.

### Zidentyfikowane Ryzyka

- Możliwość wprowadzenia użytkownika w błąd – plik z rozszerzeniem CSV może faktycznie zawierać XML.
- Brak spójności między rozszerzeniem a zawartością pliku.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozszerzenie przypisane do szablonu | W definicji szablonu XSLT zapisujemy oczekiwane rozszerzenie pliku, automatycznie ustawiane przy wyborze szablonu | ✅ Wybrana (docelowo) – zapewnia spójność |
| Pozostawienie wyboru rozszerzenia użytkownikowi | Użytkownik sam wybiera rozszerzenie niezależnie od szablonu | ❌ Odrzucona – niespójność (CSV z treścią XML) |
| Analiza szablonu i automatyczne wykrywanie rozszerzenia | System analizuje XSLT i wykrywa format | ❌ Odrzucona – zbyt skomplikowane/niepewne |

### Decyzja / Stan

**Status:** 🔍 Do doprecyzowania / wymaga uzgodnienia**

- **Docelowy kierunek (po uzgodnieniu):** W nowym interfejsie React rozszerzenie pliku ma być przypisane do definicji szablonu XSLT i ustawiane automatycznie (read-only albo ukryte). W starym interfejsie zachowana zgodność wstecz – obecne pole zostaje, a jeśli szablon nie ma rozszerzenia, użytkownik może je wybrać.
- **Brak finalnej akceptacji:** Damian chce uzgodnić z Kamilem i Januszem po przygotowaniu PBI (referencja do projektu UX Krystyny, zadanie 19020 – dwa widoki/obrazki).
- **Backend:** Reuse istniejącego mechanizmu – pobranie CaseID z raportu, użycie starego kodu eksportu; niewielka zmiana GraphJSON, żeby zapisać rozszerzenie w definicji szablonu.
- **UX/umiejscowienie akcji:** Dyskusja, czy eksport XSLT powinien być w akcjach masowych (checkboxy) zamiast w ustawieniach eksportu; brak decyzji.
- **Kompatybilność:** W nowym React – rozszerzenie z definicji szablonu; w starym UI pole pozostaje (naprawa drobnego błędu w starej wersji możliwa serwisowo).

### Zadania

- **Anna Skupinska:** Przygotowanie PBI z wymaganiami (w tym zapis rozszerzenia w definicji szablonu, GraphJSON, UX według projektu Krystyny) → termin: nie określono.
- **Anna Skupinska:** Rozszerzenie GraphJSON o zapis rozszerzenia pliku → termin: nie określono.
- **Do ustalenia (Damian + Kamil + Janusz):** Lokalizacja akcji (akcje masowe vs ustawienia eksportu) i tryb prezentacji rozszerzenia (read-only/ukryte).

### Punkty otwarte

- Czy eksport do szablonu XSLT powinien być dostępny jako akcja masowa (zaznaczone sprawy + przycisk eksportu)?
- Jak prezentować rozszerzenie: read-only vs ukryte, czy w ogóle pokazywać kolumnę w UI?
- Zachowanie wstecznej kompatybilności, gdy szablon nie ma rozszerzenia – jakie domyślne wartości i komunikaty?

---

## 3. Logowanie SQL w nowych raportach

**Projekt:** `Moduly/Modul-raportowy`



### Kontekst i Problem

W starych raportach przy błędzie wykonania SQL logowany jest pełny tekst zapytania z parametrami. W nowych raportach React ta funkcjonalność nie działa – błędy SQL nie zawierają pełnej treści zapytania, co utrudnia diagnozę.

### Zidentyfikowane Ryzyka

- Trudności w diagnozowaniu błędów raportów – brak pełnej informacji o zapytaniu SQL.
- Utrudnione wsparcie serwisowe – brak możliwości odtworzenia problemu bez pełnego zapytania.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Użycie AmodDBCommand zamiast standardowego DBCommand | Nowe raporty używają AmodDBCommand, który automatycznie loguje SQL przy błędach | ✅ Kierunek – wymaga potwierdzenia użycia w nowych raportach |
| Dodanie logowania SQL w funkcji DatabaseError | Rozszerzenie istniejącej funkcji DatabaseError w SQLBuilder o logowanie pełnego zapytania | 🔍 Do weryfikacji – funkcja może już logować w nowszej wersji |
| Własna implementacja logowania SQL | Nowy mechanizm logowania | ❌ Odrzucona – duplikacja istniejącej funkcjonalności |

### Decyzja / Stan

**Status:** 🔍 Do weryfikacji**

- Kod logowania istnieje w `DatabaseError` w `AmodReportPreview.SQLBuilder`, ale prawdopodobnie nie jest używany lub działa tylko w nowszych wersjach (zmiany z okolic marca 2025).
- Należy sprawdzić, czy nowe raporty korzystają z `AmodDBCommand`; w przeciwnym razie logowanie nie zadziała.
- Obecnie wszystkie wyjątki backendu pokazują ten sam komunikat – brak rozróżnienia błędów SQL vs innych błędów backendu; potrzebne repro z realnymi błędami SQL.

### Zadania

- **Anna Skupinska:** Analiza, czemu logowanie SQL nie działa w nowych raportach; weryfikacja, czy `DatabaseError` jest wywoływana i czy jest używany `AmodDBCommand` → termin: nie określono.
- **Anna Skupinska:** Weryfikacja, w której wersji AMODIT funkcja `DatabaseError` z pełnym logowaniem jest dostępna (marzec 2025?) i czy klienci na starszych wersjach muszą zaktualizować system → termin: nie określono.

### Punkty otwarte

- Czy problem dotyczy tylko błędów w bazie, czy również innych błędów backendu (wszystkie wyglądają identycznie na froncie)?
- Jak odróżnić w UI błędy SQL od innych błędów i czy przekazywać ID loga do frontu (mechanizm już istnieje)?
- Czy klienci na starszych wersjach powinni aktualizować, aby mieć logowanie SQL?

---

## 4. Repozytorium plików – wymagania techniczne

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`



### Kontekst i Problem

Koncepcja repozytorium plików w AMODIT (niezwiązanego ze sprawami) z przestrzeniami, folderami, plikami i uprawnieniami. Potrzebne wymagania techniczne dotyczące przechowywania plików, struktury folderów na dysku i mapowania struktury logicznej na fizyczną.

### Zidentyfikowane Ryzyka

- Problemy z długimi ścieżkami w systemie Windows (limit 260 znaków).
- Trudności w diagnostyce przy użyciu skracanych nazw (mogą się powtarzać).
- Konflikty nazw przy skrótach (np. różne „Dokumentacja…”).
- Problemy z backupem i zarządzaniem przy przechowywaniu w bazie dla dużych plików.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Osobna tabela + pliki na dysku | Oddzielna tabela metadanych, pliki zgodnie z ustawieniami systemowymi (jak pliki ze spraw) | ✅ Preferowane – zgodne z obecną architekturą |
| Przechowywanie w bazie (Blob) | Wszystkie pliki w bazie | ❌ Odrzucona (wstępnie) – rozmiar bazy/backup; temat do decyzji |
| Struktura folderów = struktura logiczna (pełne nazwy) | Foldery na dysku jak w interfejsie | ⏸️ Odroczona – ryzyko długości ścieżek Windows |
| Struktura folderów oparta na ID | Foldery nazywane ID, czytelna ścieżka w URL | ✅ Preferowane – unikalność i diagnostyka przez URL |
| Skracanie nazw (prefiksy) | Skrót nazwy jako folder | ❌ Odrzucona – mylące, ryzyko kolizji |
| Widoczność folderów bez dostępu do zawartości | Uprawnienie „widoczność folderu” | 🔍 Do decyzji – czy ma sens biznesowy |

### Decyzja / Stan

**Status:** 🔍 Do doprecyzowania (warsztat, brak akceptacji)**

- Piotr ma wątpliwość co do pełnego nadawania uprawnień na plikach niezależnie od folderu – skłania się do zawężania względem folderu, nie do rozszerzania.
- Preferencja: struktura fizyczna oparta na ID, a czytelną ścieżkę logiczną pokazywać w URL (kopiuj/wklej do Explorera).
- Lokacja plików: osobne ustawienie dla repozytorium („Repository”), ale do decyzji czy ten sam root co pliki spraw.
- Przechowywanie: raczej na dysku; trzeba rozstrzygnąć, czy w ogóle wspierać tryb „w bazie” (Blob) – brak decyzji.

### Zadania

- **Damian Kaminski:** Spisanie wymagań ogólnych z podziałem na zadania → termin: 23.10.2025.
- **Piotr Buczkowski:** Przegląd wymagań i weryfikacja ryzyk globalnych (struktura folderów, przechowywanie, ograniczenia Windows) → termin: nie określono (wymaga czasu).
- **Piotr Buczkowski:** Analiza przechowywania plików i struktury folderów na dysku; poszukanie inspiracji w innych repozytoriach → termin: nie określono.

### Punkty otwarte

- Czy per-plik można nadawać uprawnienia tylko w kierunku zawężenia względem folderu, czy pełne oderwanie od dziedziczenia?
- Czy w ogóle wspierać przechowywanie w bazie (Blob), czy tylko na dysku?
- Jak adresować limit długości ścieżek Windows (głębokość zagnieżdżeń)?
- Czy „widoczność folderu” bez dostępu do plików ma sens, czy zostawić wyłącznie dziedziczenie?

---

## 5. Problem z instalacją AMODIT – błąd "Said can't build"

**Projekt:** `cross-cutting/Bezpieczenstwo-pentesty`


### Kontekst i Problem

Klient (Tomasz Kalinowski) podczas instalacji AMODIT otrzymuje błąd "Said can't build". Uprawnienia puli aplikacji są nadane do folderu z AMODIT. Możliwe kwestie: TLS/HTTPS lub ograniczenia Windows 11 dotyczące localhost.

### Zidentyfikowane Ryzyka

- Problemy z instalacją AMODIT u klientów.
- Możliwe problemy z konfiguracją TLS/HTTPS w środowisku klienta.
- Ograniczenia Windows 11 dla loopback i domen testowych kierowanych na localhost.

### Decyzja / Stan

**Status:** 🔍 Do weryfikacji**

- Hipotezy do sprawdzenia: TLS/HTTPS (np. adapter do Alfresco), restrykcje przeglądarek/Windows 11 dla loopback i domen testowych (np. `astrafox.amod.info` przekierowane na localhost), brak możliwości wyłączenia ograniczeń loopback w Windows 11.

### Zadania

- **Damian Kaminski:** Wsparcie klienta w diagnozie błędu instalacji; weryfikacja TLS/HTTPS oraz ograniczeń Windows 11/loopback → termin: w ciągu dnia (23.10.2025).

### Punkty otwarte

- Jaka jest dokładna przyczyna błędu "Said can't build"?
- Czy problem dotyczy tylko Windows 11, czy również innych wersji?
- Jak obejść ograniczenia loopback/domen testowych w Windows 11?

---



> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

# Notatka projektowa – 2025-11-14 – Repozytorium

**Data:** 2025-11-14
**Temat główny:** Repozytorium Plików (DMS) - struktura, uprawnienia, interfejs

**Powiązane projekty:**
- `Klienci/WIM/Repozytorium-plikow-DMS` – wszystkie funkcjonalności
- `Klienci/WIM/Komunikator` – problemy z certyfikatami (wzmianka)
- `Organizacja-DEV/Dokumentacja-organizacyjna` – struktura backlogu

---

## 1. Struktura repozytorium

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium

### Cel i problem

Repozytorium jest elementem systemu AMODIT. Struktura jest wielopoziomowa, można ją budować dodając kolejne podfoldery. Najwyższe foldery nazywamy przestrzeniami (nomenklatura przyjęta dla łatwego wyróżnienia po stronie frontendu, np. inną ikonką). Pliki mogą być przechowywane w dowolnej gałęzi - albo w najwyższych folderach, albo w podfolderach.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Struktura repozytorium:
- **Przestrzenie** - najwyższe foldery (nomenklatura przyjęta dla łatwego wyróżnienia)
- **Foldery zagnieżdżone** - możliwość tworzenia struktury wewnątrz (wstępnie ustalone 20 poziomów, można ograniczyć, ale nie ma uwarunkowań technicznych - raczej wynikało z kwestii ścieżki windowsowej)
- **Foldery maksymalnie 2000 obiektów** - limit na folder
- **Pliki** - przechowywane w dowolnej gałęzi (najwyższe foldery lub podfoldery)

**Szczegóły techniczne:**
- Struktura wielopoziomowa
- Maksymalna głębokość: 20 poziomów (można ograniczyć)
- Limit obiektów w folderze: 2000

### Ograniczenia / Poza zakresem

- Przenoszenie plików między folderami - poza zakresem
- Wersjonowanie - poza zakresem
- Historia zmian - poza zakresem

### Punkty otwarte

- [DO USTALENIA]

---

## 2. Przechowywanie plików

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium

### Cel i problem

Pliki w repozytorium mają być przechowywane zgodnie z konfiguracją dla załączników. Moduł będzie częścią AMODIT, należy dodać kolumnę. Pliki będą zapisywane zgodnie z konfiguracją dla załączników.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Pliki będą przechowywane tak samo jak załączniki:
- **Lokalizacja fizyczna** - można skopiować z opisu zapisywania na dysku
- **Identyfikacja pliku w interfejsie** - skoro przechowujemy tak jak załączniki, to pewnie tak będzie (do dopytań u Piotra)
- **Szyfrowanie** - zakładamy, że skoro przechowujemy tak samo, to będzie natywnie (założenie, do weryfikacji)
- **Metadane w bazie** - Piotr już to określił, będą spójne z tym, co mamy dzisiaj (trzeba przejrzeć bazę danych przy spisywaniu)

**Szczegóły techniczne:**
- Przechowywanie w systemie plików podobnie jak dla załączników
- Moduł częścią AMODIT - należy dodać kolumnę
- Metadane w bazie zgodne z obecnymi standardami

### Ograniczenia / Poza zakresem

- [DO USTALENIA]

### Punkty otwarte

- Identyfikacja pliku w interfejsie - do dopytań u Piotra
- Szyfrowanie - założenie, do weryfikacji

---

## 3. Uprawnienia (MVP1)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium

### Cel i problem

MVP1 to definicja uprawnień dla poziomu najwyższego, czyli dla przestrzeni. Wszystko reszta jest dziedziczona w dół. Nie istnieje możliwość przerywania dziedziczenia. Administrator systemu dziedziczy uprawnienia administratora przestrzeni i jest inicjatorem pierwszej przestrzeni (nie zakłada się roli administratora repozytorium).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Uprawnienia w MVP1:
- **Definicja uprawnień** - tylko dla poziomu najwyższego (przestrzenie)
- **Dziedziczenie** - od góry w dół, bez możliwości przerywania dziedziczenia
- **Typy uprawnień:**
  - **Pełny dostęp (administrator)** - odczyt, zapis, usuwanie, tworzenie struktury i nadawanie dostępów
  - **Edycja** - odczyt, zapis, usuwanie **swoich** plików i folderów oraz tworzenie struktury
  - **Odczyt** - tylko przeglądanie
- **Administrator systemu** - dziedziczy uprawnienia administratora przestrzeni, jest inicjatorem pierwszej przestrzeni (nie ma roli administratora repozytorium)

**Szczegóły techniczne:**
- Uprawnienia przechowywane tak jak załączniki (już jest, bym powiedział, frontend)
- Wyświetlanie uprawnień - frontend

### Ograniczenia / Poza zakresem

- Możliwość przerywania dziedziczenia - poza zakresem MVP1
- Uprawnienia na poziomie folderów/plików - poza zakresem MVP1

### Punkty otwarte

- [DO USTALENIA]

---

## 4. Obsługa plików (podgląd, upload)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium

### Cel i problem

W zakresie podglądów i wczytywania plików nie zmieniamy nic względem tego, jak to jest obecnie, łącznie z uploadem. Bazujemy na zasadach, które są w AMODIT na poziomie sprawy obsługiwane. Z racji, że będziemy to robić reactowo, zakładamy, że nie będzie żadnego problemu, żeby wykorzystać to, co reactowo już zrobiliśmy jako podgląd dla raportów (to już powstało, zostało zaktualizowane).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Obsługa plików:
- **Podgląd** - tak jak dzisiaj (wykorzystanie tego, co reactowo już zrobiliśmy jako podgląd dla raportów - przeniesienie komponentu w podstawowym zakresie)
- **Upload** - tak jak obecnie w AMODIT na poziomie sprawy
- **Wczytywanie** - tak jak obecnie w AMODIT na poziomie sprawy

**Szczegóły techniczne:**
- Wykorzystanie istniejącego komponentu React do podglądu (już zrobiony dla raportów)
- Bazowanie na zasadach z AMODIT na poziomie sprawy

### Ograniczenia / Poza zakresem

- [DO USTALENIA]

### Punkty otwarte

- [DO USTALENIA]

---

## 5. Interfejs użytkownika - nawigacja i operacje

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`
**Komponent:** Repozytorium

### Cel i problem

Interfejs użytkownika wymaga nawigacji w formie drzewa oraz operacji na plikach (upload, usuwanie). Operacje na plikach zależą od uprawnień - usuwanie tylko swoich plików przez użytkowników z uprawnieniami edycji, usuwanie wszystkich przez administratora przestrzeni lub systemu.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Nawigacja w formie drzewa | Wyświetlanie struktury folderów w formie drzewa | ✅ Wybrana – zgodnie z wymaganiami |
| Lazy loading | Wyświetlanie tylko najwyższych węzłów, rozwinięcie na żądanie | ✅ Wybrana – konieczne dla dużych struktur (np. 10 000 elementów) |
| Wyszukiwanie | Wyszukiwanie plików po nazwie i treści (Lucene) | ⏸️ Odroczona – niekoniecznie musi być częścią pierwszego MVP, dla testów nie jest niezbędne |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Interfejs użytkownika:
- **Nawigacja w formie drzewa** - wyświetlanie struktury folderów
- **Lazy loading** - wyświetlanie tylko najwyższych węzłów (przestrzenie), rozwinięcie na żądanie (zapytanie "podaj mi potomków tego"), maksymalnie 100 pozycji w widoku (nie 10 000)
- **Zapamiętywanie stanu** - zapamiętywanie ostatnio rozwiniętych węzłów (local storage)
- **Operacje na plikach:**
  - Upload - tylko dla użytkowników z uprawnieniami edycji lub administratorów
  - Usuwanie tylko swoich plików - dla użytkowników z uprawnieniami edycji
  - Usuwanie wszystkich - dla administratora przestrzeni lub systemu
- **Obszar roboczy** - już w AMODIT zrobione, lazy loading musi być zastosowany
- **Przyciski "Dodaj plik", "Nowy folder"** - widoczne tylko dla użytkowników z uprawnieniami edycji lub administratorów

**Szczegóły techniczne:**
- Nawigacja w formie drzewa
- Lazy loading (wyświetlanie tylko najwyższych węzłów, rozwinięcie na żądanie)
- Zapamiętywanie stanu w local storage
- Obszar roboczy z lazy loadingiem
- Warunkowe wyświetlanie przycisków w zależności od uprawnień

### Ograniczenia / Poza zakresem

- Przenoszenie plików między folderami - poza zakresem
- Wyszukiwanie (Lucene) - poza zakresem MVP1 (może być później, po nazwie i treści)

### Punkty otwarte

- Wyszukiwanie - do ustalenia, czy będzie w MVP1 (niekoniecznie musi być częścią pierwszego MVP, dla testów nie jest niezbędne)

---

## 6. Struktura backlogu (inicjatywy, epiki, ficzery, use case'y, PBI)

**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna`
**Komponent:** [DO USTALENIA]

### Cel i problem

Omówienie struktury backlogu dla repozytorium - jak podzielić pracę na inicjatywy, epiki, ficzery, use case'y i PBI. Ustalenie zasad podziału i priorytetyzacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Inicjatywa jako cel biznesowy | Inicjatywa to cel biznesowy (np. "skrócenie czasu wdrożeń o 30%"), nie rozliczalny w kontekście statusu | ✅ Wybrana – inicjatywa to wytyczna, cel biznesowy |
| Inicjatywa jako coś skończonego | Inicjatywa jako coś rozliczalnego w kontekście statusu | ❌ Odrzucona – inicjatywa to wytyczna, nie rozliczalna |
| Epik "Osiągnięcie nowego strumienia przychodów z modułów dodatkowych" | Repozytorium jako moduł dodatkowy w ramach epika | ✅ Wybrana – repozytorium jest modułem dodatkowym |
| Ficzery bezpośrednio z epika | Wrzucenie wszystkiego do epika jako opis | ⏸️ Odroczona – można podejść dwojako |
| Ficzery z opisem ogólnym w epiku | W epiku tylko opis ogólny, potem opisywanie kolejnych elementów | ✅ Wybrana – lepsze podejście |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Struktura backlogu:
- **Inicjatywa** - cel biznesowy, wytyczna (np. "skrócenie czasu wdrożeń o 30%", "wzrost satysfakcji użytkownika poprzez modernizację interfejsu"), nie rozliczalna w kontekście statusu, powiązana ze strategią, ograniczona liczba
- **Epik** - pod inicjatywą, np. "Osiągnięcie nowego strumienia przychodów z modułów dodatkowych" (repozytorium jako moduł dodatkowy), w epiku tylko opis ogólny, potem opisywanie kolejnych elementów
- **Area** - w której części AMODIT będą wykonywane jakieś prace, może być inna na poziomie ficzera czy PBI (np. ficzer w jednym obszarze, ale zmiany w jobach i na frontendzie na sprawie)
- **MVP** - wartości, które dostarczamy (nie worek funkcjonalności), MVP ma w nazwie "Value"
- **Ficzery** - rzeczy, które ogólnie trzeba zrobić, najpierw wypisujemy wszystkie ficzery (15-20), potem decydujemy, które w MVP1, które w MVP2 (kryterium: MVP1 musi być zrobione w jeden sprint)
- **Use case'y** - przypadki użycia pod ficzery (np. "zarządzanie strukturą folderów" może mieć use case'y: "dodanie nowego folderu", "usunięcie pustego folderu")
- **PBI** - zadania wynikające z use case'ów (np. przypadek tworzenia nowej teczki może mieć 15 PBI)

**Szczegóły techniczne:**
- Struktura: Inicjatywa → Epik → MVP → Ficzery → Use case'y → PBI
- Area może być inna na poziomie ficzera czy PBI
- MVP to wartości, nie worek funkcjonalności

### Ograniczenia / Poza zakresem

- [DO USTALENIA]

### Punkty otwarte

- Jak dokładnie podzielić ficzery na use case'y i PBI - do ustalenia z deweloperami
- Walidacja przejścia z analizy biznesowej do systemowej - do ustalenia

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Podstawowa funkcjonalność repozytorium

**Cel:** Minimalna, funkcjonalna wersja - walidacja podejścia z klientem

**Zakres:** 
- Struktura repozytorium (przestrzenie, foldery, pliki)
- Uprawnienia na poziomie przestrzeni (dziedziczenie w dół)
- Nawigacja w formie drzewa (lazy loading)
- Podgląd plików (wykorzystanie istniejącego komponentu React)
- Upload plików
- Usuwanie plików (tylko swoich dla edycji, wszystkie dla administratora)

**Planowany termin:** [DO USTALENIA]

### MVP 2: [DO USTALENIA]

**Cel:** [DO USTALENIA]

**Zakres:** 
- Wyszukiwanie (Lucene) - po nazwie i treści
- [DO USTALENIA]

---

## Punkty do dalszej dyskusji (globalne)

- Przenoszenie plików między folderami - do rozważenia w późniejszych MVP
- Wersjonowanie - do rozważenia w późniejszych MVP
- Historia zmian - do rozważenia w późniejszych MVP
- Możliwość przerywania dziedziczenia uprawnień - do rozważenia w późniejszych MVP
- Uprawnienia na poziomie folderów/plików - do rozważenia w późniejszych MVP
- Wyszukiwanie (Lucene) - do rozważenia w MVP2 lub później
- Nazwy tabel - muszą być odgórnie ustalone, żeby nie konfliktowały w przyszłości (Mateusz powiedział "dowolne", ale to nie jest akceptowalne)
- Komunikator - problem z certyfikatami przy komunikacji lokalnej (HTTP vs HTTPS), problem po stronie klienta, ale wspólny (muszą wysłać certyfikaty do osadzenia lokalnie)
- Piotr sugeruje, że komunikator też powinien być częścią AMODIT-a (podobnie jak repozytorium)


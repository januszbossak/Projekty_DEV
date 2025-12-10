# CHANGELOG - Repozytorium plików (DMS)

Historia ustaleń i zmian dla projektu.

---

## 2025-12-01 | Planowanie sprintu (Szczegóły)
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Planowanie sprintu.md]
**Kategoria:** #Architektura #Funkcjonalność #Decyzja

- Aplikacja budowana jako odrębna, wpięta w AMODIT (jak Komunikator).
- Wykorzystanie AI do wytwarzania.
- Oddzielna baza danych (decyzja architektoniczna).
- Metadane MVP: nazwa (techniczna/wyświetlana), opis, tagi.
- Uprawnienia: dziedziczone z przestrzeni (bez zrywania w MVP).

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność

- Realizacja MVP 2 - zarządzanie strukturą repozytorium u klienta WIM.
- Obsługa tworzenia, edycji, usuwania folderów.
- Obsługa wgrywania, pobierania, podglądu plików.
- Zarządzanie uprawnieniami.
- Historia zdarzeń jako opcja (przesunięta na kolejny sprint jeśli brak czasu).

---

## 2025-11-30 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-30 Spotkanie projektowe - Edytor procesow.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-30%20Spotkanie%20projektowe%20-%20Edytor%20procesow.md)
**Kategoria:** #Architektura #Funkcjonalność #Decyzja #MVP

- Repozytorium jako odrębna aplikacja wpięta w AMODIT (korzystająca z AI do wytwarzania).
- Oddzielna baza danych (docelowa integracja z AMODIT możliwa).
- Metadane (MVP): nazwa, opis, tagi (bez zaawansowanego edytora).
- Uprawnienia (MVP): dziedziczone z najwyższego poziomu (przestrzeń), brak zrywania na podfolderach.
- Termin odbioru: grudzień (negocjacja umowy serwisowej).

---

## 2025-11-27 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-11-27 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Wdrożenie #UX #Ryzyko

- Cel sprintu: Uruchomienie modułu repozytorium plików do końca sprintu, z instalacją u klienta Piotra Murawskiego.
- Status prac: Zarządzanie drzewem katalogów (backend i frontend), dodawanie/edycja/usuwanie folderów są już zrobione.
- Zakres: Poprawki UX edycji nazwy (inline), dodanie ikony kosza do usuwania przestrzeni, rozbudowa wyszukiwania w strukturze.
- Funkcjonalności: Wyświetlanie plików (widok kafelkowy), dodawanie plików (drag & drop), uprawnienia do przestrzeni (cel na sprint).
- Ryzyka: Bardzo ambitny plan, wymaga pełnej dedykacji zespołu i codziennego testowania, ryzyko opóźnień przy instalacji u klienta.
- Decyzje: Zachowanie nazwy "przestrzeń", widok domyślny kafelkowy, uprawnienia na poziomie przestrzeni (MVP).

---

## 2025-11-21 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-21 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Zadanie

- Uruchomienie podstawowej funkcjonalności tworzenia folderów.
- Ania przygotowuje endpoint do tworzenia folderów.
- Filip podepnie się pod endpoint do tworzenia folderów.

---

## 2025-11-17 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-17 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-17%20Planowanie%20sprintu.md)
**Kategoria:** #Architektura #Zadanie #MVP

- Rozpoczęcie prac nad MVP 1 w nowym podejściu architektonicznym (Azure epik -> features).
- Kluczowe założenie: zmiany w strukturze bazy danych i endpointach.
- Wymagana weryfikacja obszernej dokumentacji technicznej pod kątem zakresu MVP.
- Planowane spotkanie techniczne (18.11) w celu omówienia szczegółów.

---

## 2025-11-14 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-14 Spotkanie projektowe - Repozytorium.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-14%20Spotkanie%20projektowe%20-%20Repozytorium.md)
**Kategoria:** #Architektura #Frontend #Uprawnienia

- **Struktura repozytorium:** Przestrzenie (root) → Foldery (max 20 poziomów, 2000 obiektów) → Pliki.
- **Uprawnienia (MVP1):** Definiowane tylko na poziomie Przestrzeni, dziedziczone w dół bez przerywania. Role: Admin (pełny), Edycja (swoje), Odczyt.
- **Przechowywanie plików:** Zgodnie z konfiguracją załączników AMODIT (system plików, metadane w bazie).
- **Interfejs:** Nawigacja drzewiasta z lazy loading (max 100 pozycji na widok), operacje kontekstowe zależne od uprawnień.
- **Funkcjonalności poza zakresem:** Przenoszenie, wersjonowanie, historia zmian.

---

## 2025-11-13 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Planowanie%20sprintu.md)
**Kategoria:** #Funkcjonalność #Architektura #Decyzja

- Zakres prac MVP1: Backend, Import/Eksport (wzór), CRUD pozycji, Wyświetlanie drzewka (hierarchia).
- Architektura: Opis techniczny Piotra jako pierwszy ficzer/dokumentacja w MVP1.
- Struktura: Rejestr jako repozytorium, węzły jako sprawy (parent-child), raport tabela z hierarchią.
- Wymaganie: Dostarczenie funkcjonalności umożliwiającej odbiór wdrożenia w WIM (dokumenty korporacyjne, szablony).

---

## 2025-11-13 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-13 Notatka projektowa - Edytor procesów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-13%20Notatka%20projektowa%20-%20Edytor%20procesów.md)
**Kategoria:** #Zadanie

- Repozytorium zidentyfikowane jako największy temat do zrealizowania przed końcem roku.

---

## 2025-11-07 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-07 Planowanie sprintu.md]
**Kategoria:** #Funkcjonalność #Architektura #Zadanie

- Piotr zakończył opis koncepcyjny repozytorium.
- Moduł będzie częścią AMODIT, pliki zapisywane w CaseAttachment.
- Wykorzystuje istniejącą infrastrukturę; frontend jest, trzeba połączyć z backendem.
- Adrian jest proponowanym implementerem MVP (struktura, CRUD, uprawnienia 1. poziomu).
- W planach dodanie kolumn w CaseAttachment i nowych tabel (RepositoryFolder, Repository, Rights, History).
- Struktura fizyczna plików dzielona na lata; logiczna struktura w aplikacji będzie rozbieżna z fizyczną.
- Nazwy plików będą modyfikowane prefiksem AttachmentID.

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Dokumentacja #Zadanie

- Piotr Buczkowski ma opisać wytyczne do repozytorium.

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #Architektura

- Frontend repozytorium plików: widoki kafelkowy/listowy, wyszukiwarka i drzewo zasobów, udostępnianie zasobów.
- Architektura: repozytorium jako aplikacja wewnętrzna AMODIT (nie zewnętrzna), planowane powiązanie ze sprawami (podpinanie/pobieranie/start sprawy z pliku) poza MVP.
- Wymaganie PKF: ścieżka przechowywania plików per proces – do uwzględnienia w backendzie.

## 2025-10-31 | Planowanie Sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-31 Planowanie sprintu.md]
**Kategoria:** #Architektura #Funkcjonalność #Zadanie #Ryzyko

- Frontend już częściowo zrealizowany przez Filipa.
- Potrzeba wsparcia architektonicznego dla backendu repozytorium.
- Architektura i struktura backendu powinna być rozkminiona po 8 dniach sprintu.
- Piotr odpowiada za ustalenie architektury (odrębna aplikacja vs część AMODIT, komunikacja, użytkownicy, przechowywanie, mikroserwisy).
- Mateusz odpowiada za strukturę danych i rozpisanie endpointów.
- Damian odpowiada za dokumentację architektury i wymagania biznesowe.
- Szczegóły techniczne: struktura folderowa, uprawnienia w kontekście działów, przenoszenie plików, wykorzystanie GdPicture.
- Ryzyka: przeładowanie Mateusza, nierealne ukończenie repozytorium w jeden sprint.

---

## 2025-10-28 | Spotkanie projektowe - Design
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-28 Spotkanie projektowe - Design.md]
**Kategoria:** #Architektura #Design #Funkcjonalność #Decyzja #MVP #Ryzyko

- **Struktura repozytorium:** Przestrzenie jako najwyższy poziom, foldery zagnieżdżone, pliki. Maksymalna głębokość zagnieżdżenia do ustalenia.
- **System uprawnień i dziedziczenie:** Domyślne dziedziczenie, możliwość przerwania dziedziczenia na poziomie folderu/pliku. Widoczność folderu jako uprawnienie wynikowe.
- **Przechowywanie plików:** Pliki lokalnie na zasobach sieciowych (MVP), spójne z attachmentami AMODIT. Struktura fizyczna oparta na ID węzłów.
- **Metadane plików:** Tylko techniczne/systemowe w MVP. Metadane użytkownika (opis, tagi, daty) poza MVP.
- **Interfejs użytkownika:** Widok drzewa folderów po lewej, główny obszar zawartości, breadcrumbs. Widoki plików: kafelkowy (MVP), lista (do rozważenia).
- **Wyszukiwanie plików:** Pełnotekstowe w oparciu o Lucene, z filtrowaniem wyników po uprawnieniach użytkownika. Ryzyka wydajnościowe/bezpieczeństwa do zaadresowania.
- **Bezpieczeństwo i szyfrowanie plików:** Pytanie o szyfrowanie plików i wpływ struktury opartej na ID na zarządzanie backupem.
- **Funkcjonalności poza MVP:** Wersjonowanie, historia zmian, przenoszenie plików, linki publiczne, etykiety/tagi, powiadomienia, eksport/import struktury, metadane użytkownika.
- **Ogólne uwagi i ryzyka:** Gigantyczny projekt, podejście z AI (Filip) może skrócić czas realizacji o 50% (z 6 do 2-3 miesięcy). Wymaga sprawnego backendu.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Organizacja #Decyzja

- Ania powinna skupić się na repozytorium (zamiast tłumaczeń).
- Nie dawać jej podglądu szablonów (grubsza sprawa).

---

## 2025-10-23 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-23 Rada architektow.md]
**Kategoria:** #Architektura #Decyzja

- Koncepcja repozytorium plików w AMODIT (niezwiązanego ze sprawami).
- Preferencja: struktura fizyczna oparta na ID, czytelna ścieżka logiczna w URL.
- Przechowywanie raczej na dysku; do decyzji, czy wspierać tryb "w bazie" (Blob).
- Status: Do doprecyzowania (warsztat, brak akceptacji).

---
## 2025-08-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-21 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-21%20Rada%20architektów.md)
**Kategoria:** #Dokumentacja

**Wytyczne do analizy** ⏸️
- Otrzymano wytyczne dotyczące repozytorium - nietrywialne, wymagają szczegółowej analizy
- **Status:** ⏸️ Odroczone na odrębne spotkanie eksperckie
- Wytyczne przekazane Januszowi i wrzucone na kanał komunikacyjny
- Brak czasu na spotkaniu i potrzeba eksperckiej dyskusji
- **Punkty otwarte:** Wszystkie szczegóły wymagają analizy na odrębnym spotkaniu
- **Zadania:** Damian Kamiński - przekazanie wytycznych Januszowi, wrzucenie na kanał

---

## 2025-07-30 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-07-30 Notatka projektowa 2025-07-30 Repozytorium - nowy wzor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-07-30%20Notatka%20projektowa%202025-07-30%20Repozytorium%20-%20nowy%20wzor.md)

**Kategoria:** #Architektura

**1. Definicja i Filozofia Repozytorium**
- ✅ **Zatwierdzone:** Utrzymujemy koncepcję **dokument = sprawa**
  - Repozytorium to nakładka (widok) organizująca sprawy w strukturę drzewiastą
  - Sprawa może być podpięta do wielu węzłów jednocześnie
  - Fizyczny plik w sprawie, w repozytorium "link"
- ❌ **Odrzucone:** Repozytorium plików ("worek na dokumenty") niezależny od spraw
- ⏸️ **Punkt otwarty:** Oczekiwanie na formalne wymagania od Piotra Murawskiego

**Kategoria:** #Funkcjonalność

**2. Struktura i Uprawnienia**
- 💡 **Propozycja:** Model hybrydowy struktur
  - Struktura Działowa (domyślne foldery działów)
  - Struktura Udostępniona (foldery explicite udostępniane użytkownikom/grupom)
  - Struktura Specjalna (np. JRWA)
- 💡 **Propozycja:** Rozdzielenie uprawnień
  - Dostęp do folderu (węzła) ≠ dostęp do spraw w nim
  - Użytkownik widzi tylko sprawy, do których ma uprawnienia z procesu
  - Wyjątek: Administratorzy repozytorium/JRWA

**3. Obsługa JRWA (Jednolity Rzeczowy Wykaz Akt)**
- 💡 **Propozycja:** JRWA jako osobny typ repozytorium/węzła (włączany w konfiguracji)
- **Funkcjonalności:**
  - Struktura Roczna (główny węzeł = Rok)
  - Import/Eksport struktury klasyfikacji (XML)
  - Wygaszanie starych roczników (read-only)
  - Dziedziczenie parametrów (symbol, kategoria A/B5/B10) z folderu na sprawy
- **Techniczne:** Mechanizm "Formularza Folderu", funkcje reguł `GetRepositoryParams`
- ⏸️ **Punkty otwarte:**
  - Widoczność JRWA (dla wszystkich vs tylko kancelaria/archiwum)
  - Integracja z e-Archiwum (na razie MVP: eksport offline)
- ⚠️ **Uwaga:** JRWA NIE jest rozważane w kontekście klienta WIM (admin. publiczna)

**4. Parametryzacja folderów**
- 💡 **Propozycja:** Definicje atrybutów dla węzłów repozytorium
  - Opisywanie folderów (np. "Kategoria archiwalna: A")
  - Reguły na sprawach mogą odczytywać wartości z węzła nadrzędnego

**Kategoria:** #Roadmap

**Propozycja podziału na pakiety:**
- **MVP 1: WIM - Repozytorium Podstawowe**
  - Uelastycznienie struktury folderów (poza sztywne działy)
  - Mechanizm udostępniania folderów (Wybierz osoby/grupy)
  - Rozdzielenie uprawnień (Folder vs Sprawa)
- **MVP 2: Obsługa JRWA**
  - Węzeł typu JRWA (struktura roczna)
  - Parametryzacja folderów (kategorie archiwalne)
  - Dziedziczenie parametrów na sprawy
  - Eksport/Import struktury

**Do dalszej dyskusji:**
- Wymagania klienta (WIM) na piśmie przed deweloperką
- Warsztaty archiwizacyjne z partnerem zewnętrznym (specjaliści EZD)

---

## 2025-06-26 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-06-26 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-06-26%20Rada%20architektów.md)
**Kategoria:** #Decyzja

- **Rozbieżność w rozumieniu pojęcia "Repozytorium"** między zespołem R&D a klientem (Piotr Murawski)
- **Decyzja:** ⏸️ Odroczone - wstrzymanie prac koncepcyjnych do czasu otrzymania jasnej definicji i wymagań od klienta

---

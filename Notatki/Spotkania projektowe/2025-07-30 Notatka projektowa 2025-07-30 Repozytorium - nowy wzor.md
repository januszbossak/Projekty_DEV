
**Data:** 2025-07-30

**Temat główny:** Koncepcja Repozytorium (DMS) i obsługi JRWA

**Powiązane projekty:**
- [[Projekty/Klienci/WIM/Repozytorium/README|Repozytorium]] – funkcjonalności 1, 2, 3, 4
- [[Projekty/Klienci/WIM/Repozytorium/README|Repozytorium]] – kontekst wdrożeniowy
- [[Projekty/Moduly/Modul-raportowy/README|Modul-raportowy]] – widoki w węzłach

---

## 1. Definicja i Filozofia Repozytorium

**Projekt:** `klienci/WIM/Repozytorium`
**Komponent:** Repozytorium

### Cel i problem
Rozbieżność w rozumieniu pojęcia "Repozytorium" między zespołem AMODIT (repozytorium spraw/metadanych) a klientami/konsultantami (repozytorium plików/dokumentów w folderach). Ryzyko przekształcenia systemu w "śmietnik na pliki" bez procesów.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Repozytorium plików | System plików ("worek na dokumenty") niezależny od spraw. | ❌ Odrzucona – niezgodna z filozofią AMODIT. |
| Repozytorium spraw (DMS) | Dokument jest zawsze osadzony w sprawie (nawet uproszczonej). Repozytorium to struktura folderów organizująca te sprawy. | ✅ Wybrana – zachowujemy spójność z silnikiem workflow. |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

Utrzymujemy koncepcję, że **dokument = sprawa**. Repozytorium to nakładka (widok) pozwalająca organizować sprawy w strukturę drzewiastą (węzły/foldery).
- Sprawa może być podpięta do wielu węzłów jednocześnie.
- Fizyczny plik jest w sprawie, w repozytorium jest "link".

### Punkty otwarte
- Oczekiwanie na formalne wymagania od klienta (WIM/Piotr Murawski), aby potwierdzić czy takie podejście zostanie zaakceptowane.

---

## 2. Struktura i Uprawnienia (Działy vs Swobodne Foldery)

**Projekt:** `klienci/WIM/Repozytorium`
**Komponent:** Repozytorium

### Cel i problem
Obecna implementacja (z Rossmanna) sztywno wiąże strukturę z działami organizacji. Potrzeba większej elastyczności (struktury niezależne od działów, np. projektowe, JRWA) oraz precyzyjnego modelu uprawnień.

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

1. **Model hybrydowy:**
   - **Struktura Działowa:** Domyślne foldery działów (widoczne dla członków).
   - **Struktura Udostępniona:** Foldery udostępniane explicite użytkownikom/grupom (niezależnie od działu).
   - **Struktura Specjalna (np. JRWA):** Osobny byt (patrz pkt 3).

2. **Model Uprawnień:**
   - **Rozdzielenie widoczności węzła od widoczności spraw.**
   - Dostęp do folderu (węzła) **NIE** oznacza automatycznego dostępu do wszystkich spraw w nim zawartych.
   - Użytkownik widzi w folderze tylko te sprawy, do których ma uprawnienia wynikające z procesu/obiegu.
   - Wyjątek: Administratorzy repozytorium/JRWA (mogą widzieć wszystko).

---

## 3. Obsługa JRWA (Jednolity Rzeczowy Wykaz Akt)

**Projekt:** `klienci/WIM/Repozytorium`
**Komponent:** Repozytorium / Moduł dedykowany

### Cel i problem
Wymóg obsługi JRWA w administracji publicznej (WIM, szpitale). JRWA to specyficzna klasyfikacja, zmieniająca się w cyklach rocznych, wymagająca dziedziczenia parametrów (kategoria archiwalna).

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

Traktujemy JRWA jako **osobny typ repozytorium/węzła** włączany w konfiguracji ("Instancja obsługuje JRWA").

JRWA nie jest rozważane w kontekście klienta WIM

**Kluczowe funkcjonalności:**
1. **Struktura Roczna:** Głównym węzłem jest Rok (np. 2025).
2. **Import/Eksport:** Możliwość przenoszenia struktury klasyfikacji między latami (XML).
3. **Wygaszanie:** Stare roczniki są widoczne ("read-only" lub ukrywane), ale blokowane do dodawania nowych spraw.
4. **Dziedziczenie parametrów:** Folder JRWA posiada atrybuty (np. symbol, kategoria A/B5/B10), które muszą być dziedziczone przez sprawy do niego wpięte (dla celów archiwizacji).

### Szczegóły techniczne:
- Potrzeba mechanizmu "Formularza Folderu" (rejestr parametrów węzła).
- Funkcje reguł (np. `GetRepositoryParams`) do pobierania atrybutów z folderu nadrzędnego na formularz sprawy.

### Punkty otwarte
- Czy JRWA ma być widoczne dla wszystkich (jako klasyfikator), czy tylko dla kancelarii/archiwum? (Wniosek: Struktura widoczna, zawartość spraw chroniona uprawnieniami).
- Integracja z e-Archiwum / eksport paczek archiwalnych (na razie MVP: eksport offline).

---

## 4. Parametryzacja folderów

**Projekt:** `klienci/WIM/Repozytorium`
**Komponent:** Repozytorium

### Cel i problem
Foldery w repozytorium (szczególnie JRWA) muszą przechowywać metadane (okres przechowywania, kategoria), które wpływają na cykl życia dokumentów.

### Decyzja / Sposób realizacji
**Status:** 💡 Propozycja

Wprowadzenie definicji atrybutów dla węzłów repozytorium (analogicznie jak pola na formularzu sprawy).
- Umożliwi to opisywanie folderów (np. "Kategoria archiwalna: A").
- Reguły na sprawach będą mogły odczytywać te wartości.

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: WIM - Repozytorium Podstawowe
**Cel:** Spełnienie wymagań wdrożeniowych WIM.
**Zakres:**
- Uelastycznienie struktury folderów (poza sztywne działy).
- Mechanizm udostępniania folderów (Udostępnij -> Wybierz osoby/grupy).
- Rozdzielenie uprawnień (Folder vs Sprawa).

### MVP 2: Obsługa JRWA
**Cel:** Obsługa specyfiki administracji publicznej.
**Zakres:**
- Węzeł typu JRWA (struktura roczna).
- Parametryzacja folderów (kategorie archiwalne).
- Dziedziczenie parametrów na sprawy.
- Eksport/Import struktury.

---

## Punkty do dalszej dyskusji (globalne)

- **Wymagania Klienta (WIM):** Konieczność sformalizowania wymagań na piśmie z Piotrem Murawskim przed rozpoczęciem prac deweloperskich, ze względu na ryzyko zmian koncepcji i konflikty komunikacyjne.
- **Warsztaty Archiwizacyjne:** Rozważenie konsultacji z partnerem zewnętrznym (specjalistami od archiwizacji/EZD) w celu dopracowania logiki JRWA.

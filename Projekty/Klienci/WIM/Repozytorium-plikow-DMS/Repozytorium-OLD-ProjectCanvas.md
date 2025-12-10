# Project Canvas: Repozytorium Plików (DMS)

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-10-28
**Klient:** WIM
**Data rozpoczęcia:** 2025-10-28

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | Damian | |
| **Tech Lead / Deweloper** | | |
| **Tester** | | |
| **Opiekun handlowy** | | |
| **Kontakt u klienta** | | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klient WIM potrzebuje **centralnego miejsca do przechowywania i zarządzania plikami niezwiązanymi bezpośrednio ze sprawami**. Obecne rozwiązanie wymusza tworzenie "sztucznych" spraw tylko po to, aby załączyć dokumenty organizacyjne, szablony czy materiały referencyjne.

### Cel biznesowy
Umożliwienie organizacjom:
- Centralnego zarządzania plikami korporacyjnymi **bez konieczności tworzenia spraw**
- Elastycznego kontrolowania dostępu do dokumentów (per użytkownik, per grupa)
- Szybkiego odnajdywania dokumentów przez wyszukiwanie pełnotekstowe

### Cel techniczny
Stworzenie modułu **Repozytorium Plików** (DMS) jako integralnej części AMODIT, który:
- Reużyje istniejące mechanizmy przechowywania plików (DB/dysk/blob)
- Rozszerza mechanizm uprawnień o model niezależny od procesów
- Wspiera wyszukiwanie pełnotekstowe z uwzględnieniem uprawnień użytkownika

### Metryki sukcesu
- Użytkownik może **znaleźć dokument w < 5 sekund** (wyszukiwanie pełnotekstowe)
- Administrator może **skonfigurować dostęp do przestrzeni dokumentów w < 2 minuty** (uprawnienia dla grup)
- **Zero duplikacji plików** - jeden plik, wiele folderów (opcjonalnie w przyszłości)

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Reużycie istniejących mechanizmów AMODIT
Moduł **musi być częścią AMODIT** i wykorzystywać istniejące rozwiązania:
- Tabela `caseattachment` do przechowywania plików (+ nowa kolumna `attRepository`)
- Klasa `amodcaseattachment` do obsługi
- Konfiguracja przechowywania: DB, dysk lokalny lub blob storage (bez zmian)

**Uzasadnienie:** Spójność, łatwiejsze utrzymanie, wykorzystanie sprawdzonych rozwiązań.

### Zasada 2: Hierarchia folderów bez konfliktu z istniejącymi pojęciami
- Najwyższy poziom: **"Przestrzenie"** (nie "Obszary" - conflict z istniejącym pojęciem w AMODIT)
- Struktura: Przestrzenie → Foldery → Podfoldery → Pliki
- Brak limitu głębokości zagnieżdżenia (do ustalenia w MVP)

### Zasada 3: Uprawnienia niezależne od procesów
System uprawnień **nie może bazować na uprawnieniach procesowych**. Własny model:
- Poziomy: `read`, `modify`, `admin`
- Nadawanie dla użytkowników i grup
- MVP1: tylko dla przestrzeni (foldery 1. poziomu)
- Przyszłość: dziedziczenie w głąb struktury

### Zasada 4: Wyszukiwanie z uwzględnieniem bezpieczeństwa
Wyszukiwanie **zawsze respektuje uprawnienia użytkownika** - użytkownik widzi w wynikach tylko dokumenty, do których ma dostęp.

---

## Decyzje architektoniczne (ADR)

| ID | Data | Decyzja | Uzasadnienie |
|----|------|---------|--------------|
| ADR-001 | 2025-10-28 | Nazwa "Przestrzenie" dla najwyższego poziomu | Uniknięcie konfliktu z istniejącymi "obszarami" w AMODIT |
| ADR-002 | 2025-10-28 | Wykorzystanie tabeli `caseattachment` + kolumna `attRepository` | Reużycie istniejącego mechanizmu, spójność z załącznikami spraw |
| ADR-003 | 2025-10-28 | Przechowywanie zgodne z konfiguracją załączników (DB/dysk/blob) | Spójność konfiguracji, wykorzystanie istniejącej infrastruktury |
| ADR-004 | 2025-10-28 | Struktura na dysku: `\repository\YYYY\` | Analogicznie do skanów, separacja od załączników spraw |
| ADR-005 | 2025-10-28 | Indeksowanie w Lucene (bez powiązania ze sprawą) | Wyszukiwanie pełnotekstowe niezależne od kontekstu procesu |
| ADR-006 | 2025-10-28 | MVP1: uprawnienia tylko dla folderów 1. poziomu | Uproszczenie implementacji, szybsze dostarczenie wartości |
| ADR-007 | 2025-10-28 | Historia zmian w formacie JSON | Elastyczność formatu, różne typy zdarzeń (foldery, uprawnienia, pliki) |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza i specyfikacja

**Ukończono:**
- ✅ Specyfikacja funkcjonalna (2025-10-28)
- ✅ Decyzje architektoniczne - moduł częścią AMODIT
- ✅ Projekt struktury bazy danych (4 nowe tabele + modyfikacja `caseattachment`)
- ✅ Plan MVP1 i MVP2+

**Trwa praca nad:**
- Finalizacja założeń (punkty do dyskusji poniżej)
- Przygotowanie makiet UI
- Oszacowanie MVP1

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| **[Wysokie]** Wydajność wyszukiwania pełnotekstowego przy bardzo dużych plikach (PDF 100+ MB) | Średnie | Wysoki | Testy wydajnościowe w fazie PoC; możliwe limity rozmiaru lub asynchroniczne indeksowanie |
| **[Wysokie]** Migracja istniejących plików klientów do repozytorium | Wysokie | Średni | Zaprojektować narzędzie migracyjne już w MVP1; konsultacje z klientem o strategii |
| **[Średnie]** Konflikt kolumny `attRepository` z istniejącymi implementacjami u klientów | Niskie | Wysoki | Weryfikacja przed release; migracja bazy w ramach update'u |
| **[Średnie]** Niejasne granice poziomów uprawnień (`read`, `modify`, `admin`) | Średnie | Średni | Warsztat z klientem WIM w fazie analizy - precyzyjne zdefiniowanie |
| **[Niskie]** Bezpieczeństwo - brak szyfrowania plików na dysku | Niskie | Wysoki | Rozważyć szyfrowanie w MVP2 lub jako opcję konfiguracyjną |

---

### Punkty wymagające decyzji (w fazie analizy)

**Uprawnienia:**
- [ ] Precyzyjne zdefiniowanie poziomów uprawnień:
  - `read` = ?
  - `modify` = dodawanie/edycja/usuwanie folderów i plików?
  - `admin` = zarządzanie uprawnieniami?
- [ ] Czy rozdzielić uprawnienie "dodawanie" od "usuwanie"?

**Struktura:**
- [ ] Maksymalna dozwolona głębokość zagnieżdżenia folderów (sugestia: 10 poziomów)

**Ograniczenia:**
- [ ] Limit rozmiaru pojedynczego pliku (sugestia: 2 GB - spójnie z obecnymi załącznikami)
- [ ] Lista dozwolonych/blokowanych typów plików (spójnie z załącznikami spraw)

**Wydajność:**
- [ ] Czy indeksowanie Lucene wymaga osobnego job-a? (asynchroniczne indeksowanie)
- [ ] Strategie cachowania dla drzewa folderów

**Bezpieczeństwo:**
- [ ] Konieczność szyfrowania plików na dysku/blob (MVP2 vs opcja w MVP1)

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "Podstawowa funkcjonalność Repozytorium Plików"

**Cel:** Uruchomienie minimalnej, ale funkcjonalnej wersji repozytorium. Pozwoli klientowi ocenić nasze podejście i kierunek.

**Definicja ukończenia (DoD):**
- Użytkownik może **stworzyć przestrzeń** i **strukturę folderów**
- Użytkownik może **uploadować, przeglądać i usuwać pliki**
- Administrator może **nadać uprawnienia do przestrzeni** (użytkownik lub grupa)
- Użytkownik może **wyszukać plik pełnotekstowo** i widzi tylko dokumenty do których ma dostęp
- System **loguje wszystkie zmiany** w historii

---

**Zakres funkcjonalny:**

#### Struktura organizacyjna
- [ ] Podstawowa struktura: Przestrzenie → Foldery → Pliki
- [ ] Tabela `repositoryfolder` z obsługą zagnieżdżania (`rfdParentId`)
- [ ] Tabela `repositoryattachment` (połączenie folder ↔ plik)

#### System uprawnień (tylko przestrzenie - foldery 1. poziomu)
- [ ] Tabela `repositoryrights`
- [ ] Poziomy uprawnień: `read`, `modify`, `admin`
- [ ] Nadawanie uprawnień użytkownikom (`rriUserId`) i grupom (`rriUgrId`)
- [ ] Walidacja uprawnień przy każdej operacji (CRUD)

#### Operacje CRUD
- [ ] Tworzenie/edycja/usuwanie przestrzeni i folderów
- [ ] Upload/download/usuwanie plików
- [ ] Podstawowy interfejs użytkownika:
  - Drzewo folderów (lewy panel)
  - Zawartość folderu (prawy panel - lista lub kafelki)

#### Przechowywanie plików
- [ ] Rozszerzenie tabeli `caseattachment` o kolumnę `attRepository` (bit)
- [ ] Zapis plików zgodnie z konfiguracją (DB/dysk/blob) - reużycie `amodcaseattachment`
- [ ] Struktura katalogów na dysku: `\repository\YYYY\`
- [ ] Generowanie podglądów (reużycie istniejącego mechanizmu)

#### Indeksowanie i wyszukiwanie
- [ ] Indeksowanie zawartości plików w Lucene (asynchroniczne?)
- [ ] Wyszukiwanie pełnotekstowe **z uwzględnieniem uprawnień użytkownika**
- [ ] Podstawowy interfejs wyszukiwania (input + wyniki)

#### Historia zmian
- [ ] Tabela `repositoryhistory`
- [ ] Logowanie zdarzeń: dodanie/usunięcie folderu, zmiana uprawnień, upload/usunięcie pliku
- [ ] Format: JSON z elastyczną strukturą

---

**Planowana data:** [do uzupełnienia po oszacowaniu]

---

### 📦 MVP2+: "Zaawansowane funkcje zarządzania"

**Cel:** Rozbudowa o zaawansowane funkcje zwiększające elastyczność i użyteczność repozytorium.

---

#### Uprawnienia rozszerzone
- [ ] **Dziedziczenie uprawnień:** Przestrzeń → Folder → Podfolder → Plik
- [ ] **Przerywanie dziedziczenia** na dowolnym poziomie
- [ ] Uprawnienia wynikowe "Widoczność folderu"
- [ ] Wizualna sygnalizacja przerwania dziedziczenia (ikona w drzewie)

#### Zarządzanie plikami
- [ ] **Metadane definiowane przez użytkownika:** opis, daty obowiązywania, niestandardowe pola
- [ ] **Etykiety / Tagi** (wiele tagów na plik)
- [ ] **Przenoszenie plików i folderów** (drag-and-drop)
- [ ] **Wersjonowanie plików** i szczegółowa historia zmian (kto, kiedy, co zmienił)

#### Kosz
- [ ] Implementacja kosza (soft delete)
- [ ] Przywracanie z kosza
- [ ] Automatyczne czyszczenie (np. >30 dni)

#### Inne
- [ ] **Powiadomienia** (nowy plik w obserwowanym folderze)
- [ ] **Eksport / Import struktury folderów** (np. XML/JSON)
- [ ] **Generowanie linków publicznych** do plików (ograniczone czasowo, opcjonalnie z hasłem)

---

**Planowana data:** [do uzupełnienia]

---

## 5. ARCHITEKTURA TECHNICZNA (szczegóły)

### Technologie
- **Frontend:** React (spójne z resztą AMODIT)
- **Backend:** C# (.NET)
- **Baza danych:** MSSQL / MySQL (rozszerzenie istniejących tabel + 4 nowe)
- **Wyszukiwanie:** Lucene (indeksowanie zawartości plików)

### Nowe tabele w bazie danych

| Tabela | Kolumny | Opis |
|--------|---------|------|
| `repositoryfolder` | `rfdId`, `rfdName`, `rfdParentId` | Struktura folderów; wiele folderów z `rfdParentId=0` = Przestrzenie |
| `repositoryattachment` | `ratId`, `ratRfdId`, `ratAttId` | Połączenie folder ↔ plik (FK do `repositoryfolder` i `caseattachment`) |
| `repositoryrights` | `rriId`, `rriRfdId`, `rriUserId`, `rriUgrId`, `rriRight` | Uprawnienia do folderu: `read` / `modify` / `admin` |
| `repositoryhistory` | `rhiId`, `rhiDate`, `rhiUserId`, `rhiChangeType`, `rhiChange` (JSON) | Historia zmian (dodanie/usunięcie folderów, uprawnienia, pliki) |

### Modyfikacja istniejących tabel

**`caseattachment`:**
- Nowa kolumna: `attRepository` (bit) - oznacza plik w repozytorium (vs załącznik do sprawy)

### Fizyczne przechowywanie plików

**Zgodnie z konfiguracją dla załączników:**
- W bazie danych (BLOB)
- Na dysku lokalnym
- W blob storage (Azure/AWS)

**Struktura katalogów na dysku:**
```
\repository\
    2025\
        [guid].pdf
        [guid].docx
    2026\
        ...
```

Analogicznie do skanów (`\notassigned\YYYY\`), separacja od załączników spraw.

### Indeksowanie Lucene

- Pliki indeksowane **asynchronicznie** (job?)
- Zawartość zapisywana osobno (brak powiązania ze sprawą - w przeciwieństwie do załączników)
- Wyszukiwanie **zawsze filtrowane przez uprawnienia użytkownika**

---

## 6. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-10-28 | Inicjalna specyfikacja funkcjonalna - struktura, uprawnienia, UI, MVP1 | Spotkanie projektowe 2025-10-28 |
| 2025-10-28 | **Zmiana architektury:** moduł częścią AMODIT (nie odrębny byt). Szczegóły techniczne: tabele DB, wykorzystanie `caseattachment`, Lucene, struktura katalogów. MVP1 zawężone do uprawnień 1. poziomu | Notatka techniczna 2025-10-28 |

---

## 7. PRZYDATNE LINKI

- **Umowa z klientem:** [link/numer]
- **Inicjatywa w backlogu:** [link do Azure DevOps]
- **Repozytorium kodu:** [link]
- **Makiety UI:** [link do Figmy]
- **Środowisko DEV:** [link]
- **Dokumentacja Lucene:** [link]

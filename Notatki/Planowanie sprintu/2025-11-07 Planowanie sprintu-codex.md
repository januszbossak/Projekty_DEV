> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-01.
> **Korekty:** Zaktualizowano nagłówek o właściwe przypisanie projektu. Skorygowano błąd merytoryczny: "AD" w kontekście archiwum to ADE (Archiwum Dokumentów Elektronicznych), a nie Active Directory. Ujednolicono nazwisko Łukasza Brockiego. Przypisano tematy do nowych projektów (`Integracja-UPS`, `Global-Express`, `Przechowywanie-plikow`, `Integracja-CAS`).

# Planowanie Sprintu – 2025-11-07

**Sprint:** [nie określono]
**Okres:** [nie określono]
**Projekty:** `Klienci/WIM/Repozytorium-plikow-DMS`, `Klienci/WIM/Komunikator`, `Integracje/Integracja-CAS`, `Klienci/LOT/JRWA`, `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`, `Klienci/LOT`, `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`, `Klienci/PKF/Przechowywanie-plikow`

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Projekt | Status | Uwagi |
|-------|---------|--------|-------|
| Komunikator | `Klienci/WIM/Komunikator` | 🔄 W trakcie | Mateusz kończy, są drobne błędy (nie funkcjonalne, tylko przesuwanie, zmiana nazwy), grupy działają. |
| Repozytorium - opis | `Klienci/WIM/Repozytorium-plikow-DMS` | ✅ Ukończone | Piotr napisał opis koncepcyjny. |
| Integracja z CAS | `Integracje/Integracja-CAS` | 🔄 W trakcie | Piotr dostał wytyczne wczoraj, ma kompletny opis, powiedział że to kilka godzin pracy. |

---

## 2. Plany na sprint

### Repozytorium plików (MVP)

**Projekt:** `Klienci/WIM/Repozytorium-plikow-DMS`

**Kontekst i cel:**
Moduł repozytorium plików w systemie ma na celu umożliwienie przechowywania plików poza sprawami. Kluczowe założenie: moduł będzie częścią AMODIT, jednak pliki będą zapisywane w tabeli `CaseAttachment`, tak jak pliki załączone do spraw.
**Janusz Bossak:** "To dość rewolucyjna zmiana koncepcji w stosunku do tego, co żeśmy początkowo myśleli, ale dobrze." Wykorzystuje istniejącą infrastrukturę (około 50% rzeczy już mamy). Frontend w zasadzie mamy, trzeba go połączyć z backendem.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja MVP repozytorium (podstawowa struktura organizacyjna, CRUD, system uprawnień dla folderów pierwszego poziomu) | **Adrian** (proponowany) | [nie określono] | Czeka na zakończenie innych zadań Adriana |
| Dodanie kolumn w `CaseAttachment` określających, że wpis jest plikiem repozytorium | [do przypisania] | [nie określono] | - |
| Dodanie tabel: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory` | [do przypisania] | [nie określono] | - |
| Implementacja struktury fizycznej plików (podział na lata) | [do przypisania] | [nie określono] | - |
| Indeksowanie plików repozytorium (Lucene) | [do przypisania] | [nie określono] | - |

**Szczegóły techniczne:**
- Tabela: `CaseAttachment` (wykorzystanie istniejącej).
- Nowe tabele: `RepositoryFolder`, `Repository`, `RepositoryRights`, `RepositoryHistory`.
- Struktura fizyczna: główny katalog "Repository", podział na lata (2025, 2026, etc.).
- Klasa: `AmodThumbnail` – generowanie podglądu standardowo jak teraz.
- Konfiguracja: zgodnie z konfiguracją załączników (dysk, Blob).
- Mechanizm skanów: wykorzystanie istniejącego mechanizmu skanów (pliki nieprzypisane do sprawy, luźne elementy).

**Decyzje podjęte przy planowaniu:**
- Wykorzystanie istniejącej tabeli `CaseAttachment` zamiast tworzenia nowej struktury.
- Struktura fizyczna po latach (możliwość dodatkowego podziału na miesiące).
- Struktura logiczna w aplikacji (przestrzenie, foldery) będzie rozbieżna ze strukturą fizyczną (lata).
- System uprawnień tylko dla folderów pierwszego poziomu w MVP.
- Nazwy plików będą modyfikowane (dodawany AttachmentID jako prefiks) aby uniknąć konfliktów.

---

### Integracja z CAS

**Projekt:** `Integracje/Integracja-CAS`

**Kontekst i cel:**
Integracja z systemem CAS (Central Authentication Service) - centralny system zarządzania uprawnieniami (np. dla WIM). W momencie autentykacji/autoryzacji można: po pierwsze autoryzować użytkownika, po drugie – jeśli go nie ma – w ogóle go utworzyć i w dodatku jeszcze przypisać mu od razu odpowiednie uprawnienia.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja integracji z CAS (autentykacja, autoryzacja, tworzenie użytkownika, przypisywanie uprawnień) | **Piotr Buczkowski** | Kilka godzin (10 dniówek w wycenie z dużym zapasem) | Ma już wytyczne i kompletny opis |

---

### Integracje dla LOT

**Projekt:** `Klienci/LOT/Integracja-UPS`, `Klienci/LOT/Integracja-Global-Express`, `Klienci/LOT`

**Kontekst i cel:**
Dla klienta LOT trzeba zrealizować trzy integracje do końca roku (przynajmniej w zakresie MVP):
1. **UPS** – integracja z firmą kurierską UPS.
2. **Global Express** – kolejna firma kurierska, z którą LOT ma podpisaną umowę.
3. **ADE (Archiwum Dokumentów Elektronicznych)** – integracja z archiwum państwowym (często mylone z AD/Active Directory w rozmowie, ale kontekst wskazuje na archiwum).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja z UPS | **Łukasz Brocki** (proponowany) | [nie określono] | Czeka na kontakt z osobą opiekującą się LOT ze strony UPS |
| Integracja z Global Express | [do przypisania] | [nie określono] | Trzeba rozpoznać, czy mają jakieś API |
| Analiza integracji z ADE (scenariusze użycia, przypadki użycia) | Dział wdrożeń | [nie określono] | Muszą pozyskać scenariusze użycia od klienta |
| Ewentualna implementacja integracji z ADE (jeśli nie da się przez COLA REST) | [do przypisania] | [nie określono] | Po analizie scenariuszy użycia |

**Szczegóły techniczne:**
- UPS: podobnie jak FedEx czy DHL, jako kolejny moduł.
- Global Express: trzeba rozpoznać API.
- ADE: możliwe że wystarczy użycie COLA REST API (dział wdrożeń może to zrobić bez dedykowanego modułu AMODIT).

**Uwagi:**
- Pomysł na przyszłość: integracja z brokerem kurierskim "Apaczka" (ma integrację ze wszystkimi firmami kurierskimi w Polsce) – wymaga zbadania kosztów i prowizji.

---

### JRWA dla LOT

**Projekt:** `Klienci/LOT/JRWA`

**Kontekst i cel:**
JRWA (Jednolity Rzeczowy Wykaz Akt) to działanie normatywne. Każdy dokument musi być podpięty pod JRWA. To będzie wykonywane setki razy dziennie, więc musi być robione płynnie i wygodnie. Główna kwestia to pole "Odnośnik", które by po strukturze JRWA się poruszało.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Projektowanie i implementacja "Asystenta klasyfikacji" (pole odnośnik z okienkiem klasyfikatora JRWA) | [do przypisania] | [nie określono] | Wymaga dedykowanego spotkania designowego |

---

### Podpisywanie na Macu przez Szafira (WIM)

**Projekt:** `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

**Kontekst i cel:**
Klient WIM potrzebuje obsługi podpisywania na Macu przez Szafira. Istnieje gotowe rozwiązanie: SimpleSign (245 zł), ale klient uparł się na Szafira.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Implementacja obsługi podpisywania na Macu przez Szafira | **Adrian** | [nie określono] | Adrian już to ogarnięte |

---

### Konfiguracja folderów per proces (PKF)

**Projekt:** `Klienci/PKF/Przechowywanie-plikow`

**Kontekst i cel:**
PKF chce konfigurować, w którym folderze mają być pliki załączone do spraw – per proces. Piotr Myszkowski mówi, że już mamy taki mechanizm na poziomie pola typu dokument. Można to łatwo rozszerzyć na poziomie procesu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Rozszerzenie mechanizmu konfiguracji folderów na poziomie procesu | [do przypisania] | [nie określono] | Czeka na wyjaśnienie potrzeby biznesowej |

**Decyzje podjęte przy planowaniu:**
- Technicznie da się zrobić, ale brakuje informacji biznesowej. Łukasz Bott ma dopytać klienta.

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Projekt | Status | Uzasadnienie |
|---------|---------|--------|--------------|
| Wykorzystanie tabeli `CaseAttachment` dla repozytorium zamiast nowej struktury | `Klienci/WIM/Repozytorium-plikow-DMS` | ✅ Zatwierdzone | Wykorzystuje istniejącą infrastrukturę. |
| Struktura fizyczna plików repozytorium po latach | `Klienci/WIM/Repozytorium-plikow-DMS` | ✅ Zatwierdzone | Zabezpiecza przed jednym wielkim workiem. |
| ADE dla LOT przez COLA REST API (jeśli wystarczy) | `Klienci/LOT` | 💡 Do weryfikacji | Jeśli wystarczy REST API, dział wdrożeń może to zrobić samodzielnie. |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Projekt | Wpływ | Mitygacja | Właściciel |
|---------------|---------|-------|-----------|------------|
| Łukasz Brocki przeciążony (UPS, Global Express, ADE) | `Klienci/LOT` | Wysoki | Rozdzielenie zadań. | Damian Kaminski |
| Brak kontaktu z UPS | `Klienci/LOT/Integracja-UPS` | Średni | Rozwiązane – pozyskano kontakt do osoby opiekującej się LOT. | Łukasz Bott |
| Nie wiadomo czy Global Express ma API | `Klienci/LOT/Integracja-Global-Express` | Średni | Trzeba rozpoznać. | Łukasz Bott |
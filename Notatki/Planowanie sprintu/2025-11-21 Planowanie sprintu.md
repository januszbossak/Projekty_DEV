# Planowanie Sprintu – 2025-11-21

**Sprint:** Bieżący (listopad)
**Okres:** [brak sprecyzowanych dat]

---

## 1. Status bieżący (Domykanie poprzedniego sprintu)

| Temat | Status | Uwagi |
|-------|--------|-------|
| Komunikator (WIM) | ✅ Ukończone | Potwierdzone działanie u klienta |
| Amrestowy | ✅ Ukończone | Piotr kończył (status z czatu) |

---

## 2. Plany na sprint

### JRWA (Jednolity Rzeczowy Wykaz Akt) dla LOT

**Kontekst i cel:**
Przygotowanie struktury danych dla JRWA na wzór integracji z GUS TERYT. Celem jest umożliwienie wyboru klasy z wykazu w polu "Odnośnik" i zwrócenie jej atrybutów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Budowa struktury JRWA (tabela, źródło danych) | **Piotr Buczkowski** | start przyszły tydz. | - |
| Ewentualne przejęcie tematu w dalszym kroku | **Mariusz Piotrzkowski** (?) | - | Jeśli Piotr nie zdąży/przekaże |

**Szczegóły techniczne:**
- Dedykowana tabela w bazie.
- Mechanizm źródła danych zwracający obiekt/JSON.
- Dostęp w regułach przez notację kropki: `[PoleJRWA].KlasaArchiwalna`.

**Decyzje podjęte przy planowaniu:**
- Rezygnacja z implementacji uprawnień do klas JRWA w tym sprincie (klient LOT nie chce przypisywać klas do działów).
- Zarządzanie strukturą (interfejs) przesunięte na kolejne sprinty.

---

### Repozytorium Plików (WIM)

**Kontekst i cel:**
Uruchomienie podstawowej funkcjonalności tworzenia folderów.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Przygotowanie pierwszego endpointu (tworzenie folderów) | **Anna Skupińska** | 1d (dziś) | - |
| Podpięcie pod endpoint (tworzenie folderów) | **Filip Liwiński** | - | Czeka na Anię |
| Wsparcie dla Ani przy problemach z bazami pod testy | **Michał Zwierzchowski** | - | - |

---

### SignApp (MacOS)

**Kontekst i cel:**
Dokończenie prac nad aplikacją i przygotowanie do testów u klienta.

**Status:**
Aplikacja gotowa (UI poprawione), ale niecertyfikowana.

**Decyzje podjęte przy planowaniu:**
- Przekazać wersję niecertyfikowaną do testów działowi IT klienta (z pominięciem dyrekcji).
- Klient musi być świadomy konieczności akceptacji instalacji z nieznanego źródła.

**Ryzyka:**
- Opóźnienia w certyfikacji.
- Problem z podpisywaniem (raz działa, raz "wymaga pełnej autoryzacji") – do weryfikacji przez Łukasza Brockiego (czy Simplus zwraca taką informację).

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki widoku, panel wyboru certyfikatu, obsługa flagi e-poleconego | **Adrian Kotowski** | - | - |
| Wypisywanie z raportów (nowa funkcjonalność) | **Adrian Kotowski** | - | - |
| Weryfikacja zwrotki Simplus dot. blokady karty | **Łukasz Brocki** | - | - |

---

### Integracje Kurierskie (LOT)

**Kontekst i cel:**
Integracja z nowymi dostawcami usług kurierskich dla LOT.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Integracja UPS i Global Express | **Łukasz Brocki** | Global Express w tym sprincie | Dane pozyskane |

---

### Integracja SIEM (LOT)

**Kontekst i cel:**
Monitorowanie zdarzeń systemu AMODIT w systemach SIEM klienta.

**Decyzje podjęte przy planowaniu:**
- Zamiast pisać dedykowaną integrację, AMODIT wystawi logi w ustandaryzowanym formacie na porcie, a system SIEM klienta będzie nasłuchiwał.

---

### Edytor Formularza i Lista Pól

**Kontekst i cel:**
Domykanie tematu nowego edytora graficznego i listy pól. Wyszło sporo bugów i niespójności wizualnych.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Poprawki edytora graficznego i listy pól (bugi, wizualne) | **Zespół Frontend** | - | - |
| Porządkowanie pola typu Tabela (rozjechany import, ikonki) | **Mariusz Piotrzkowski** (?) | - | Jeśli Piotr weźmie JRWA |
| Podgląd reguł pola (Prawy panel) | **Do ustalenia** | - | - |
| Naprawa dostępu do reguł tabeli | **Do ustalenia** | - | - |
| Naprawa dodawania nowej sekcji z poziomu listy pól | **Do ustalenia** | - | - |
| Poprawki wizualne (zaokrąglenia, podświetlenia pól Search) | **Przemysław Rogaś** | - | - |

**Decyzje podjęte przy planowaniu:**
- "Zarządzaj polem" powinno zawierać "cięższe" funkcje (usuń, zmień typ pola), które nie są używane na co dzień.
- Konieczny redesign panelu edycji pola (UX).

---

### Moduł Raportowy

**Kontekst i cel:**
Poprawa działania i wydajności filtrów użytkownika.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Prace nad indeksami (wydajność filtrów) | **Mateusz Kisiel** | - | - |
| Porządkowanie operatorów daty w filtrach | **Przemysław Rogaś** | - | - |

---

### Inne zgłoszenia backlogowe

**Kontekst i cel:**
Przegląd i przypisanie zgłoszeń z backlogu.

**Zakres prac:**

| Zadanie | Osoba | Estymacja | Zależności |
|---------|-------|-----------|------------|
| Klucz nie jest unikalny (rejestr, usunięte sprawy) | **Kamil Dubaniowski** | - | Do skomentowania |
| Informacja o zablokowanej karcie (SignApp) | **Damian Kamiński** | - | Do weryfikacji z Łukaszem Brockim |
| Wyświetlanie sekcji na telefonie (aplikacja PWA) | **Damian Kamiński** | - | Do Łukasza |
| Nagranie Zygmuntów (paczek / wielu podpisów) | **Kamil Dubaniowski** | - | Do zapytania Mateusza |
| Ukrycie kafelka w koncie systemowym | **Kamil Dubaniowski** | - | Niskie priorytet |
| Hotfix 21051 (kwiecień) | **Michał Zwierzchowski** | - | Do backlogu |

---

## 3. Decyzje architektoniczne (ad-hoc)

| Decyzja | Kontekst | Status | Uzasadnienie |
|---------|----------|--------|--------------|
| Reprezentacja sekcji w DB | Frontendowa implementacja sekcji | 💡 Do weryfikacji | Należy zmienić logikę po stronie backendu, aby sekcje miały swoją reprezentację w bazie danych, a nie tylko redundantny zapis w każdym rekordzie definicji pola. |

---

## 4. Ryzyka i blokery

| Ryzyko/Bloker | Wpływ | Mitygacja | Właściciel |
|---------------|-------|-----------|------------|
| Nieobecność Adriana | Wysoki | - | Damian Kamiński |
| Zatory w testach (koniec sprintu) | Wysoki | Przypominanie o bieżącym mergowaniu | Zespół |

---

## 5. Organizacja pracy

- **Nieobecności:** Damian (środa - warsztaty), Janusz (środa - pogrzeb).
- **Orlen Paczka:** Integracja TrustCenter, temat od Moniki. Damian ma się zapoznać.
- **Rossman historia biznesowa:** Damian przygotuje MVP dla prezentacji.
- **Koncepcja Zespołów Zadaniowych:** Powrót do idei stałych zespołów celowych (2 backendowe, 1 frontendowy, testerki przypisane).
    - Zespół Trust Center (Marek)
    - Zespół AI/OCR (Mateusz)
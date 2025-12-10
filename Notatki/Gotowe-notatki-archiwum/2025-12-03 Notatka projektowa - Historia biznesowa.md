# Notatka projektowa – 2025-12-03 – Historia biznesowa

> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-10

**Data:** 2025-12-03  
**Czas trwania:** ~2 godziny (10:16 - ~12:00)  
**Uczestnicy:** Janusz Bossak, Damian Kamiński, Łukasz Brocki, Kamil Dubaniowski (częściowo)

---

## Kontekst spotkania

Spotkanie poświęcone **przeprojektowaniu mechanizmu historii biznesowej** w AMODIT. Dyskusja rozpoczęła się od prezentacji mockupu UI dla Rossmanna, ale w trakcie rozmowy zespół odkrył **fundamentalne ograniczenia obecnej implementacji** i wypracował koncepcję wielowymiarowej historii biznesowej.

**Kluczowe odkrycie:** Obecny mechanizm obsługuje tylko historię pojedynczej sprawy, podczas gdy rzeczywiste potrzeby biznesowe wymagają śledzenia zdarzeń w kontekście wielu powiązanych spraw, klientów, teczek JRWA i innych bytów.

---

## Geneza i ewolucja koncepcji historii biznesowej

### Pierwotne przypadki użycia

**1. MSIT – raportowanie kluczowych zdarzeń (2022-2023)**
- **Problem:** Kamil musiał raportować kluczowe decyzje biznesowe, ale historia sprawy zawierała setki technicznych zdarzeń (cofnięto, poprawiono, odrzucono...)
- **Rozwiązanie:** Mechanizm `AddCaseEvent` do zapisywania tylko kluczowych momentów biznesowych (np. "wniosek zatwierdzony", "projekt zaakceptowany")
- **Zakres:** Historia biznesowa **pojedynczej sprawy** w **jednym procesie**

**2. Allianz – widok 360° klienta (koncepcja, niezrealizowana)**
- **Problem:** Klient chciał widzieć pełną historię interakcji z klientem: polisy, szkody, reklamacje, korespondencja – z różnych procesów
- **Rozwiązanie:** Pole JSON `message` z `BusinessSubjectID`, `BusinessSubjectName`, `BusinessSubjectType`
- **Status:** Prototyp, **nigdy nie wdrożony produkcyjnie**
- **Ograniczenie:** Dane w JSON, słaba wydajność, brak możliwości efektywnego raportowania

### Obecne wyzwania

**3. Rossmann – wieloprocesowa historia korespondencji (sponsor, 2025)**
- **Problem:** Korespondencja wpływa przez e-Doręczenia (proces techniczny), potem jest przekierowywana do różnych procesów obiegu (X, Y, Z). Użytkownik otwierający ostateczną sprawę nie widzi pełnej historii dokumentu.
- **Przypadek biznesowy:** Użytkownik dostaje sprawę "dzisiaj", ale data dokumentu to "3 dni temu" – brak informacji, co się działo wcześniej
- **Potrzeba:** Śledzenie "wirtualnego bytu" (dokumentu) przez wiele procesów

**4. WIM/JRWA – historia teczek spraw (2025)**
- **Problem:** Dokumenty są przypisywane do teczek JRWA. Brak historii: kto, kiedy i dlaczego przypięto/odpięto dokument z teczki
- **Potrzeba:** Audyt zmian w teczkach, wykrywanie błędnych przypisań

---

## Dwa rodzaje historii biznesowej

Podczas dyskusji zespół zidentyfikował **dwa fundamentalnie różne przypadki użycia**:

### Typ 1: Historia biznesowa SPRAWY (istniejące rozwiązanie)

**Opis:** Kluczowe zdarzenia biznesowe w ramach **jednej sprawy** w **jednym procesie**

**Przykład (MSIT):**
- Sprawa może 15 razy krążyć "cofnięto → poprawiono → odrzucono"
- W historii biznesowej zapisujemy tylko: "Wniosek wpłynął" → "Wniosek przeanalizowany" → "Wniosek zatwierdzony"

**Wyświetlanie:** W prawym panelu sprawy, zakładka "Historia biznesowa"

**Status:** ✅ Działa, wymaga tylko optymalizacji (przeniesienie z JSON do dedykowanej tabeli)

---

### Typ 2: Historia biznesowa WĄTKU/TECZKI (nowe wymaganie)

**Opis:** Śledzenie "wirtualnego bytu" (dokumentu, klienta, teczki) przez **wiele spraw** w **wielu procesach**

**Przykłady:**

**Rossmann – dokument przez procesy:**
1. Proces "Pobieranie z e-Doręczeń" → Sprawa #1
2. Proces "Obieg korespondencji X" → Sprawa #2 (utworzona z #1)
3. Proces "Obieg korespondencji Y" → Sprawa #3 (przekierowana z #2)

**JRWA – teczka sprawy:**
- Teczka JRWA "2025/01/001" zawiera:
  - Korespondencję przychodzącą (proces A, sprawa #10)
  - Korespondencję wychodzącą (proces B, sprawa #15)
  - Umowę (proces C, sprawa #20)
- Historia teczki: wszystkie zdarzenia przypięcia/odpięcia dokumentów

**Allianz – klient 360°:**
- Klient "Jan Kowalski" (ID: 456):
  - Polisa #1 (proces "Polisy")
  - Szkoda #5 (proces "Likwidacja szkód")
  - Reklamacja #8 (proces "Reklamacje")
- Historia klienta: wszystkie zdarzenia dotyczące tego klienta

**Wyświetlanie:** Przełącznik "Historia tej sprawy" ↔ "Historia wątku/teczki"

**Status:** ❌ Nie działa, wymaga przeprojektowania architektury

---

## Kluczowa decyzja architektoniczna

### Problem z obecną implementacją

**Tabela `CaseEvents` (obecny stan):**
```
CaseID | EventDate | EventType | Message (JSON)
```

**Pole `Message` zawiera:**
```json
{
  "BusinessSubjectID": 456,
  "BusinessSubjectName": "Jan Kowalski",
  "BusinessSubjectType": "client"
}
```

**Ograniczenia:**
- ❌ Słaba wydajność (brak indeksów na polach JSON)
- ❌ Niemożność efektywnego wyszukiwania (np. "wszystkie zdarzenia dla klienta X")
- ❌ Trudności w generowaniu raportów wielowymiarowych
- ❌ Brak możliwości przypisania **wielu powiązań** do jednego zdarzenia

---

### Rozwiązanie: Dedykowana tabela powiązań

**Propozycja Łukasza Brockiego:**

**Nowa tabela `CaseEventBusinessSubjects` (relacja 1:N):**
```
EventID | BusinessSubjectType | BusinessSubjectID | BusinessSubjectName
--------|---------------------|-------------------|--------------------
1       | case                | 1                 | null
1       | client              | 456               | "Jan Kowalski"
1       | jrwa_folder         | 789               | "Teczka 2025/01/001"
2       | case                | 2                 | null
2       | case                | 1                 | null (connectedCase)
```

**Zalety:**
- ✅ Szybkie indeksowanie (kolumny zamiast JSON)
- ✅ Możliwość wielu powiązań na jedno zdarzenie (wielowymiarowość)
- ✅ Efektywne wyszukiwanie: `WHERE BusinessSubjectType = 'client' AND BusinessSubjectID = 456`
- ✅ Łatwe raportowanie

**Typy powiązań (enum w kodzie):**
- `case` – powiązanie z inną sprawą (connectedCase)
- `user` – powiązanie z użytkownikiem
- `client` – powiązanie z klientem
- `jrwa_folder` – powiązanie z teczką JRWA
- `policy` – powiązanie z polisą (opcjonalnie)
- `process` – powiązanie z instancją procesu (opcjonalnie)

**Decyzja:** ✅ **Zatwierdzone** – typy powiązań definiowane w kodzie (nie przez słownik użytkownika)

---

## Use case 1: Rossmann – wieloprocesowa historia korespondencji

### Problem biznesowy

**Kontekst:**
- Rossmann ma wiele procesów obiegu korespondencji (osobne dla różnych działów)
- Korespondencja wpływa przez e-Doręczenia → proces techniczny pobierania
- Automatyzacja przekazywania → błędy w kierowaniu (wcześniej robił to człowiek, teraz automat)
- Rozwiązanie błędów: przycisk "Kopiuj sprawę między procesami" → **utrata historii**

**Przykład:**
1. **3 grudnia, 09:00** – Pobranie z e-Doręczeń (proces techniczny, sprawa #1)
2. **3 grudnia, 09:15** – Przekazanie do Działu A (automat)
3. **3 grudnia, 10:00** – Dział A stwierdza: "to nie do nas" → przekierowanie do Działu B (sprawa #2)
4. **3 grudnia, 11:00** – Dział B otwiera sprawę → widzi datę "3 grudnia, 11:00", ale dokument jest z "3 dni temu"

**Potrzeba:** Użytkownik musi wiedzieć, **dlaczego sprawa dotarła do niego po 3 dniach**, a nie po godzinie.

---

### Rozwiązanie: Mechanizm `connectedCase`

**Koncepcja:**
- Podczas tworzenia nowej sprawy (CreateCase) przekazywane jest `connectedCaseID` – ID sprawy źródłowej
- Wyświetlając historię biznesową, system **rekurencyjnie** przeszukuje zdarzenia powiązane przez `connectedCaseID`

**Przepływ danych:**

**Sprawa #1 (Pobieranie z e-Doręczeń):**
```
CaseID: 1
ConnectedCaseID: null (początek łańcucha)

Zdarzenia:
- "Pobranie korespondencji z e-Doręczeń" (BusinessSubject: brak)
- "Przekazanie do Działu A" (BusinessSubject: case #2)
```

**Sprawa #2 (Obieg korespondencji – Dział A):**
```
CaseID: 2
ConnectedCaseID: 1

Zdarzenia:
- "Przekierowanie do Działu B" (BusinessSubject: case #3)
```

**Sprawa #3 (Obieg korespondencji – Dział B):**
```
CaseID: 3
ConnectedCaseID: 2

Zdarzenia:
- "Rozpatrzenie sprawy"
```

**Wyświetlenie historii dla sprawy #3:**
1. System wykrywa `connectedCaseID = 2` → pobiera zdarzenia z #2
2. System wykrywa `connectedCaseID = 1` w #2 → pobiera zdarzenia z #1
3. Wyświetla wszystkie zdarzenia chronologicznie (najstarsze → najnowsze)

---

### Szczegóły techniczne

**Tabela powiązań:**
```
EventID | BusinessSubjectType | BusinessSubjectID
--------|---------------------|------------------
1       | case                | 2
2       | case                | 3
```

**Rekurencja:**
- Limit głębokości: max 10 poziomów (do ustalenia)
- Zabezpieczenie przed cyklicznymi powiązaniami (A → B → A)

**Ograniczenia:**
- ❌ Nie będziemy automatycznie przepinać dokumentów
- ❌ Nie będziemy obsługiwać cyklicznych powiązań

**Punkty otwarte:**
- Nazwa pola: `connectedCaseID` vs `parentCaseID` vs `sourceCaseID`?
- Limit głębokości rekurencji: ile poziomów wspieramy?

**Status:** ✅ Zatwierdzone

---

## Use case 2: JRWA – historia przypinania do teczek

### Problem biznesowy

**Kontekst:**
- W systemie JRWA dokumenty są przypisywane do teczek
- Obecny raport pokazuje tylko **aktualny stan** (jakie dokumenty są w teczce)
- **Brak historii:** kto, kiedy i dlaczego przypięto/odpięto dokumenty

**Przypadek biznesowy:**
- Opiekun teczki otwiera teczkę → brakuje dokumentu
- Pytanie: "Kto go usunął? Kiedy? Dlaczego?"
- Obecnie: brak informacji

---

### Rozwiązanie: Zdarzenia przypięcia/odpięcia

**Mechanizm:**
- Każde przypięcie dokumentu → zdarzenie w historii biznesowej
- Każde odpięcie dokumentu → zdarzenie w historii biznesowej

**Przykład zdarzenia:**
```csharp
AddCaseEvent(
  CaseID: 456, // ID polisy
  EventType: "Przypięcie do teczki JRWA",
  Message: "<a href='/case/456'>Polisa nr 123/2025</a>",
  BusinessSubjects: [
    { Type: "jrwa_folder", ID: 789, Name: "Teczka 2025/01/001" }
  ]
)
```

**Odczytanie historii teczki:**
```sql
SELECT * FROM CaseEvents ce
JOIN CaseEventBusinessSubjects bs ON ce.EventID = bs.EventID
WHERE bs.BusinessSubjectType = 'jrwa_folder'
  AND bs.BusinessSubjectID = 789
ORDER BY ce.EventDate DESC
```

**Wynik:** Lista wszystkich zdarzeń dla teczki JRWA #789 (przypięcia, odpięcia, z linkami do dokumentów)

---

### Szczegóły techniczne

**EventType (słownik):**
- Administrator definiuje zdarzenia: "Przypięcie do teczki JRWA", "Odpięcie z teczki JRWA"

**UI teczki JRWA:**
- Wyświetlanie historii jako filtrowany widok zdarzeń biznesowych
- Pole `message` może zawierać link HTML do dokumentu/sprawy

**Ograniczenia:**
- ❌ Nie będziemy automatycznie generować zdarzeń dla starych przypiętych dokumentów (tylko dla nowych operacji po wdrożeniu)
- ❌ Nie będziemy wersjonować samej teczki (tylko zdarzenia przypinania/odpinania)

**Punkty otwarte:**
- Czy zapisywać powód odpięcia? (np. "Pomyłka", "Dokument nieaktualny")
- Czy ograniczać odpinanie? (tylko opiekun teczki?)

**Status:** ✅ Zatwierdzone

---

## Wielowymiarowość historii biznesowej

### Koncepcja

**Problem:** Jeden dokument może być jednocześnie powiązany z:
- Procesem nadrzędnym (e-Doręczenia → Obieg korespondencji X)
- Klientem (korespondencja dotyczy Kowalskiego)
- Polisą (korespondencja dotyczy polisy nr 123/2025)
- Teczką JRWA (korespondencja przypięta do teczki 2025/01/001)

**Potrzeba:** System musi umożliwić **wielowymiarowe** śledzenie – ten sam dokument widoczny z wielu perspektyw.

---

### Rozwiązanie: Wiele powiązań na jedno zdarzenie

**Mechanizm:**
- Funkcja `AddCaseEvent` przyjmuje **listę** obiektów `BusinessSubject` (nie pojedynczy obiekt)
- Jedno zdarzenie może mieć wiele wpisów w tabeli powiązań

**Przykład:**
```csharp
AddCaseEvent(
  CaseID: 123,
  EventType: "Wpłynęła korespondencja",
  Message: "Korespondencja dotycząca polisy 123/2025",
  BusinessSubjects: [
    { Type: "case", ID: 1 },              // connectedCase do e-Doręczeń
    { Type: "client", ID: 456 },          // klient Kowalski
    { Type: "policy", ID: 789 },          // polisa 123/2025
    { Type: "jrwa_folder", ID: 999 }      // teczka JRWA
  ]
)
```

**Tabela powiązań:**
```
EventID | BusinessSubjectType | BusinessSubjectID
--------|---------------------|------------------
5       | case                | 1
5       | client              | 456
5       | policy              | 789
5       | jrwa_folder         | 999
```

---

### Przykłady użycia

**Widok klienta Kowalskiego:**
```sql
SELECT DISTINCT ce.*
FROM CaseEvents ce
JOIN CaseEventBusinessSubjects bs ON ce.EventID = bs.EventID
WHERE bs.BusinessSubjectType = 'client'
  AND bs.BusinessSubjectID = 456
ORDER BY ce.EventDate DESC
```
**Wynik:** Wszystkie zdarzenia dotyczące klienta Kowalskiego (polisy, korespondencja, szkody, reklamacje)

**Widok polisy 123/2025:**
```sql
SELECT DISTINCT ce.*
FROM CaseEvents ce
JOIN CaseEventBusinessSubjects bs ON ce.EventID = bs.EventID
WHERE bs.BusinessSubjectType = 'policy'
  AND bs.BusinessSubjectID = 789
ORDER BY ce.EventDate DESC
```
**Wynik:** Wszystkie zdarzenia dotyczące polisy 123/2025 (to samo zdarzenie "Wpłynęła korespondencja")

---

### Ograniczenia

- ❌ Nie będziemy automatycznie propagować powiązań (np. jeśli korespondencja jest powiązana z polisą, a polisa z klientem, to korespondencja **NIE** jest automatycznie powiązana z klientem – trzeba to ręcznie ustawić w regule)

**Punkty otwarte:**
- Czy ograniczać liczbę powiązań? (np. max 5 powiązań na zdarzenie)
- Jak obsłużyć konflikty? (co jeśli ktoś przypisze korespondencję do polisy 1, a potem okaże się, że to polisa 2?)

**Status:** ✅ Zatwierdzone

---

## Obsługa błędnego przypisania i cofania

### Problem biznesowy

**Przypadek:** Użytkownik pomylił się i przypisał dokument do niewłaściwej polisy/klienta/teczki

**Przykład:**
1. Korespondencja X przypisana do polisy #1
2. Okazało się, że dotyczy polisy #2
3. Trzeba: odpiąć z polisy #1, przypiąć do polisy #2, **zachować informację o pomyłce**

---

### Rozwiązanie: Nowe zdarzenia "odpięcie" + "przypięcie"

**Mechanizm:**
- ❌ **NIE usuwamy** starych powiązań
- ✅ Generujemy **nowe zdarzenia:**
  1. "Odpięcie z polisy #1" (z powodem: "Pomyłka użytkownika")
  2. "Przypięcie do polisy #2" (z powodem: "Poprawna polisa")

**Przykład:**
```csharp
// Użytkownik klika "Zmień powiązanie z polisy 1 na polisę 2"

AddCaseEvent(
  CaseID: 123,
  EventType: "Odpięcie z polisy",
  Message: "Pomyłka – korespondencja nie dotyczyła tej polisy",
  BusinessSubjects: [{ Type: "policy", ID: 1, Name: "Polisa 001" }]
)

AddCaseEvent(
  CaseID: 123,
  EventType: "Przypięcie do polisy",
  Message: "Poprawna polisa",
  BusinessSubjects: [{ Type: "policy", ID: 2, Name: "Polisa 002" }]
)
```

**Zalety:**
- ✅ Pełna historia zachowana (audit trail)
- ✅ Widoczne błędy i korekty
- ✅ Możliwość analizy przyczyn pomyłek

---

### Szczegóły techniczne

**EventType (słownik):**
- Administrator definiuje zdarzenia: "Odpięcie", "Przypięcie" (z różnych kontekstów: polisa, klient, teczka)

**UI:**
- Przycisk "Zmień powiązanie" → generuje automatycznie dwa zdarzenia
- Pole tekstowe "Powód zmiany" (opcjonalne)

**Ograniczenia:**
- ❌ Nie będziemy automatycznie wykrywać pomyłek
- ❌ Nie będziemy cofać zdarzeń do konkretnego punktu w historii (rollback)

**Punkty otwarte:**
- Czy wymagać powodu zmiany? (pole "Powód" obowiązkowe czy opcjonalne?)
- Kto może zmieniać powiązania? (tylko właściciel sprawy, czy każdy z uprawnieniami?)

**Status:** ✅ Zatwierdzone

---

## Mockup UI – wyświetlanie historii biznesowej

### Cel

Wizualne przedstawienie historii biznesowej obejmującej zdarzenia z wielu procesów/kontekstów

---

### Propozycja UI

**Format wpisu:**
- **Nazwa zdarzenia** (słownikowa, np. "Pobranie korespondencji z e-Doręczeń")
- **Data i godzina** (z prawej strony)
- **Użytkownik/system** (kto wykonał)
- **Nazwa procesu** (opcjonalnie – tylko jeśli zdarzenie pochodzi z innego procesu niż poprzednie)

**Heurystyka wyświetlania nazwy procesu:**
- Jeśli wszystkie zdarzenia z jednego procesu → nie wyświetlaj nazwy procesu
- Jeśli zdarzenia z wielu procesów → wyświetlaj nazwę procesu tylko przy zmianie kontekstu

**Przykład wizualizacji:**
```
┌────────────────────────────────────────────────┐
│ Historia biznesowa – Korespondencja X         │
├────────────────────────────────────────────────┤
│ 📥 Pobranie korespondencji z e-Doręczeń       │
│    System                      3 gru 2025 09:00│
│    Proces: Pobieranie z e-Doręczeń            │
├────────────────────────────────────────────────┤
│ ➡️ Przekazanie do właściwego działu            │
│    Anna Kowalska               3 gru 2025 09:15│
├────────────────────────────────────────────────┤
│ ↪️ Przekierowanie do innego działu             │
│    Piotr Nowak                 3 gru 2025 10:00│
│    Proces: Obieg korespondencji X             │
└────────────────────────────────────────────────┘
```

---

### Opcje filtrowania (przyszłość, poza MVP)

- "Pokaż tylko z tego procesu"
- "Pokaż cały wątek biznesowy"
- "Wybierz proces" (dropdown)
- Filtr po typie zdarzenia (np. "tylko wpięcia do teczki")

---

### Szczegóły techniczne

**Frontend:**
- Heurystyka: porównać nazwę procesu aktualnego zdarzenia z poprzednim; jeśli się różni → wyświetlić
- **HTML w message:** Obsługa linków HTML (z walidacją security – ochrona przed XSS)
- Format daty: do ustalenia z klientem (np. "3 grudnia 2025, 10:16")

**Ikony (opcjonalnie, poza MVP):**
- Możliwość przypisania ikon do zdarzeń przez słownik
- Ikony kierunku (wpłynęło/wypłynęło) – do dorobienia w przyszłości

**Ograniczenia MVP:**
- ❌ Nie będziemy automatycznie przypisywać ikon w MVP
- ❌ Nie będziemy dodawać filtrów w MVP

**Punkty otwarte:**
- Kolejność wyświetlania: najnowsze na górze czy na dole?
- Czy wyświetlać nagłówek procesu? (decyzja Rossmann)

**Status:** 💡 Propozycja – mockup do przekazania klientowi (Rossmann)

---

## Standaryzacja API – funkcja AddCaseEvent

### Problem

Obecna funkcja `AddCaseEvent` ma niespójną składnię:
- Czasem `BusinessSubject` jest obiektem wewnątrz `message` (JSON)
- Czasem jest osobnym parametrem

---

### Nowa składnia (zatwierdzona)

```csharp
AddCaseEvent(
  CaseID: int,
  EventType: string, // lub EventTypeID: int (słownik)
  Message: string (opcjonalny, może zawierać HTML),
  BusinessSubjects: List<BusinessSubject> (opcjonalny)
)

BusinessSubject {
  Type: string (enum),
  ID: int,
  Name: string (opcjonalny – do wyświetlenia)
}
```

---

### Przykłady użycia

**Przykład 1: Zdarzenie bez powiązań biznesowych**
```csharp
AddCaseEvent(
  CaseID: 123,
  EventType: "MailSend",
  Message: "Wysłano potwierdzenie do klienta"
)
```

**Przykład 2: Zdarzenie z jednym powiązaniem**
```csharp
AddCaseEvent(
  CaseID: 123,
  EventType: "ClientAssigned",
  Message: "Przypisano klienta",
  BusinessSubjects: [
    { Type: "client", ID: 456, Name: "Jan Kowalski" }
  ]
)
```

**Przykład 3: Zdarzenie z wieloma powiązaniami (wielowymiarowość)**
```csharp
AddCaseEvent(
  CaseID: 123,
  EventType: "DocumentLinked",
  Message: "<a href='/case/456'>Polisa nr 123/2025</a>",
  BusinessSubjects: [
    { Type: "case", ID: 1 },              // connectedCase
    { Type: "client", ID: 456 },          // klient
    { Type: "policy", ID: 789 },          // polisa
    { Type: "jrwa_folder", ID: 999 }      // teczka JRWA
  ]
)
```

---

### Migracja z obecnego rozwiązania

- Stary sposób (JSON w `message`) pozostaje obsługiwany dla wstecznej kompatybilności
- Nowe implementacje używają `BusinessSubjects`
- Docelowo: stopniowa migracja starych wywołań

**Ograniczenia:**
- ❌ Nie będziemy automatycznie migrować starych wywołań
- ❌ Nie będziemy walidować poprawności ID w `BusinessSubject` na poziomie `AddCaseEvent`

**Punkty otwarte:**
- Nazwa parametru: `BusinessSubjects` vs `LinkedSubjects` vs `RelatedObjects`?
- Czy `Name` jest obowiązkowe? (system może sam pobrać nazwę z bazy: user, client, etc.)

**Status:** ✅ Zatwierdzone

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Podstawowa tabela powiązań + mechanizm connectedCase

**Cel:** Umożliwienie wieloprocesowego śledzenia historii (use case Rossmann)

**Zakres:**
1. Utworzenie tabeli `CaseEventBusinessSubjects`
2. Modyfikacja `AddCaseEvent` – obsługa `BusinessSubjects`
3. Mechanizm `connectedCaseID` w widoku historii (rekurencyjne ładowanie)
4. Mockup UI – lista chronologiczna z nazwami procesów

**Ograniczenia MVP 1:**
- Tylko typ powiązania `case` (connectedCase)
- Bez filtrów (tylko pełna lista chronologiczna)
- Bez ikon
- Bez HTML w `message`

---

### MVP 2: JRWA + wielowymiarowość

**Cel:** Rozszerzenie mechanizmu na teczki JRWA i widok 360° klienta

**Zakres:**
1. Obsługa typów `jrwa_folder`, `client`, `policy`
2. Widok historii teczki JRWA
3. Widok 360° klienta (wszystkie zdarzenia dla klienta)
4. Mechanizm odpinania/przypinania z powodu

---

### MVP 3: UI enhancements

**Cel:** Poprawa UX i dodanie zaawansowanych funkcji

**Zakres:**
1. Ikony kierunku (wpłynęło/wypłynęło)
2. Filtry ("pokaż tylko z tego procesu", "wybierz proces")
3. Obsługa HTML w `message` (linki)
4. Migracja starych zdarzeń z JSON do nowej tabeli

---

## Punkty do dalszej dyskusji (globalne)

- **Nazewnictwo:** Ustalić finalne nazwy (`connectedCaseID` vs `parentCaseID`, `BusinessSubjects` vs `LinkedSubjects`, etc.)
- **Bezpieczeństwo:** Kto może tworzyć zdarzenia biznesowe? Czy trzeba specjalnego uprawnienia?
- **Auditowanie zmian:** Czy zmiany w powiązaniach są logowane osobno (poza historią biznesową)?
- **Wydajność:** Czy rekurencyjne ładowanie `connectedCase` nie będzie za wolne? (testy wydajnościowe)
- **Rozszerzenie typów powiązań:** Jakie jeszcze typy `BusinessSubjectType` mogą być potrzebne? (np. `contract`, `invoice`, `department`)
- **Mockup Rossmann:** Przekazać mockup do Rossmana, zebrać feedback, ewentualnie doprecyzować szczegóły UI

---

## Kluczowe cytaty z dyskusji

> **Janusz Bossak:** *"To jest przedstawiane w sprawie i to sugeruje mi jako odbiorcy, że to jest historia biznesowa tej sprawy, a to nie o to chodziło."*

> **Janusz Bossak:** *"Chodzi mi o to, że teraz dlatego o tym wspomniałem tutaj, bo chodzi mi o taki kontekst tej sprawy wyższego rzędu. Znaczy, że jest teczka sprawy, która jakby obejmuje wiele różnych aspektów."*

> **Łukasz Brocki:** *"Ja bym widział to tak, że to cały czas w subject. Robimy oddzielną tabelę w bazie danych, powiedzmy CaseEventConnections. I tam każdy wiersz to będzie ID CaseEvent oraz właśnie powiązanie, czyli ID oraz jego typ."*

> **Janusz Bossak:** *"To jest genialne, po prostu, jeżeli tak będzie. Będąc na pojedynczej sprawie amoditowej zobaczyć historię teczki tej sprawy."*

> **Damian Kamiński:** *"Obsadzając teczkę... ja będąc opiekunem teczki, tracąc jakiś dokument, nie mam w ogóle o tym wiedzy. Ktoś na dokumencie, kto miał uprawnienia ją wypiął, ale na teczce się nic nie odkłada. A dzięki temu ja znajdę zdarzenie wypięcie z teczki."*

---

## Powiązane projekty

- `cross-cutting/Interfejs-sprawy/Historia-biznesowa`
- `Klienci/LOT/JRWA`
- `Klienci/Rossmann/`

---

## Notatki końcowe

**Damian Kamiński:** *"Dobra, podsumowując. Przekazuję mockup, wzbogacam go tylko o opcję, że tu jest jeszcze nagłówek procesu. Będę pewnie Łukasz do ciebie kreował prośbę o wycenę, jak już oni potwierdzą albo jeszcze coś zasugerują."*

**Janusz Bossak:** *"Zrobi się samo."* (odnośnie podsumowania spotkania)

**Status obecnej implementacji:** MSIT prawdopodobnie **nie używa** historii biznesowej produkcyjnie (Kamil Dubaniowski: *"Nigdzie nie zużywamy"*). Piotr zapisał dane bezpośrednio do bazy, zanim powstała funkcja `AddCaseEvent`.

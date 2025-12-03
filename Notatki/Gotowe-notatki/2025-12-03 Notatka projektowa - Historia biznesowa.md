# Notatka projektowa – 2025-12-03 – Historia biznesowa

**Data:** 2025-12-03
**Temat główny:** Koncepcja wielowymiarowej historii biznesowej – architektura i use cases
**Czas trwania:** ~2 godziny (10:16 - ~12:00)

---

## Kontekst spotkania

Spotkanie poświęcone zaprojektowaniu mechanizmu **historii biznesowej** – systemu śledzenia zdarzeń biznesowych powiązanych nie tylko z jedną sprawą (case), ale z wieloma bytami jednocześnie (klient, teczka JRWA, proces nadrzędny). Dyskusja obejmowała problemy obecnego rozwiązania, propozycje nowej architektury, mockup UI oraz use cases dla Rossmana i JRWA.

---

## 1. Problem z obecnym mechanizmem historii biznesowej

**Komponent:** Moduł procesowy – mechanizm historii zdarzeń (CaseEvents)

### Cel i problem

Obecny mechanizm historii biznesowej (`AddCaseEvent`) zapisuje zdarzenia tylko w kontekście pojedynczej sprawy (case). Informacje o powiązaniach z innymi bytami (klient, teczka JRWA, proces nadrzędny) są trzymane w polu JSON (`message`), co powoduje:
- Słabą wydajność przeszukiwania (brak indeksów na polach JSON)
- Trudności w generowaniu raportów wielowymiarowych
- Niemożność efektywnego wyszukiwania historii po bycie powiązanym (np. "pokaż wszystkie zdarzenia dla klienta X")

**Use case problematyczny:**
- **Rossmann – obieg korespondencji:** Korespondencja wpływa przez e-Doręczenia, trafia do procesu technicznego pobierania, potem jest przekierowywana do różnych procesów obiegu korespondencji (X, Y, Z). Trzeba śledzić pełną historię dokumentu niezależnie od tego, w ilu procesach był.
- **JRWA – teczki spraw:** Dokument (polisa, faktura) może być przypięty do teczki JRWA. Trzeba wiedzieć KTO, KIEDY i DLACZEGO przypięto/odpięto dokument z teczki.
- **Widok 360° klienta:** Klient powinien zobaczyć wszystkie zdarzenia biznesowe dotyczące jego spraw, niezależnie od tego, w ilu procesach były prowadzone.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Pozostawienie JSON | Trzymanie `BusinessSubjectID`, `BusinessSubjectName`, `BusinessSubjectType` w polu JSON (`message`) | ❌ Odrzucone – słaba wydajność, brak indeksów |
| Dedykowana tabela powiązań | Osobna tabela z kolumnami `EventID`, `BusinessSubjectType`, `BusinessSubjectID`, `BusinessSubjectName` | ✅ Wybrana – łatwe indeksowanie, możliwość wielu powiązań na jedno zdarzenie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Utworzenie **oddzielnej tabeli powiązań biznesowych** (nazwa robocza: `CaseEventBusinessSubjects` lub podobna), która będzie przechowywać relacje między zdarzeniem (`EventID`) a bytami biznesowymi.

**Szczegóły techniczne:**
- **Tabela:** Nowa tabela z kolumnami:
  - `EventID` (FK do `CaseEvents`)
  - `BusinessSubjectType` (enum: `case`, `user`, `client`, `jrwa_folder`, etc.)
  - `BusinessSubjectID` (int – ID bytu)
  - `BusinessSubjectName` (string – nazwa do wyświetlenia, opcjonalnie)
- **Relacja:** 1 zdarzenie → wiele powiązań (1:N)
- **Indeksy:** Na `BusinessSubjectType` + `BusinessSubjectID` dla szybkiego wyszukiwania
- **API:** Funkcja `AddCaseEvent` musi przyjmować listę obiektów `BusinessSubject` zamiast pojedynczego obiektu w JSON

**Przykład wywołania (nowy):**
```csharp
AddCaseEvent(
  CaseID: 123,
  EventType: "MailSend",
  Message: "Wysłano do klienta",
  BusinessSubjects: [
    { Type: "client", ID: 456, Name: "Kowalski Jan" },
    { Type: "jrwa_folder", ID: 789, Name: "Teczka 2025/01/001" }
  ]
)
```

**Typy powiązań do skatalogowania w kodzie (enum):**
- `case` – powiązanie z inną sprawą (connectedCase)
- `user` – powiązanie z użytkownikiem
- `client` – powiązanie z klientem
- `jrwa_folder` – powiązanie z teczką JRWA
- `process` – powiązanie z instancją procesu (opcjonalnie)

### Ograniczenia / Poza zakresem

- **NIE będziemy** dodawać możliwości definiowania typów powiązań przez użytkownika – typy są zdefiniowane w kodzie (enum)
- **NIE będziemy** migrować starych zdarzeń z JSON do nowej tabeli w MVP (możliwe w przyszłości)

### Punkty otwarte

- **Nazwa tabeli** – finalna nazwa do ustalenia (CaseEventBusinessSubjects? BusinessEventLinks?)
- **Migracja danych** – czy i kiedy migrować stare zdarzenia z JSON do nowej tabeli?

---

## 2. Use case: Rossmann – wieloprocesowa historia korespondencji

**Komponent:** Moduł procesowy – mechanizm connectedCase

### Cel i problem

**Problem biznesowy:** Rossmann ma wiele procesów obiegu korespondencji (osobne procesy dla różnych działów). Korespondencja wpływa przez e-Doręczenia (proces techniczny pobierania), a potem jest przekierowywana do właściwego procesu obiegu. Użytkownik otwierający ostateczną sprawę (np. "Obieg korespondencji X") musi zobaczyć **pełną historię** – od momentu pobrania z e-Doręczeń, przez przekierowanie, aż do finalnego rozpatrzenia.

**Problem techniczny:** Obecny mechanizm nie pozwala na "spinanie" historii z wielu procesów w jedną chronologiczną listę zdarzeń.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – wykorzystanie `connectedCaseID` do spinania historii.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Mechanizm `connectedCase`:**
- Podczas tworzenia nowej sprawy w procesie docelowym (np. "Obieg korespondencji X") przekazywane jest `connectedCaseID` – ID sprawy źródłowej (np. sprawy w procesie "Pobieranie z e-Doręczeń").
- Wyświetlając historię biznesową sprawy X, system **rekurencyjnie** przeszukuje zdarzenia powiązane przez `connectedCaseID` i wyświetla je w jednej chronologicznej liście.

**Szczegóły techniczne:**
- **Pole:** `connectedCaseID` w tabeli `Cases` (już istnieje w niektórych implementacjach, wymaga standaryzacji)
- **Rekurencja:** System musi śledzić łańcuch powiązań (sprawy mogą być wielopoziomowe: e-Doręczenia → przekierowanie → właściwy proces)
- **Tabela powiązań:** Każde zdarzenie w sprawie źródłowej ma wpis w tabeli powiązań z `BusinessSubjectType = 'case'` i `BusinessSubjectID = sprawaDocelowa`

**Przepływ danych (przykład Rossmann):**
1. **Proces "Pobieranie z e-Doręczeń"** – Sprawa #1:
   - Zdarzenie: "Pobranie korespondencji z e-Doręczeń" (BusinessSubject: brak lub system)
   - Zdarzenie: "Przekazanie do właściwego działu" (BusinessSubject: `case` #2)
2. **Proces "Obieg korespondencji X"** – Sprawa #2 (`connectedCaseID = 1`):
   - Zdarzenie: "Przekierowanie do innego działu" (BusinessSubject: `case` #3)
3. **Proces "Obieg korespondencji Y"** – Sprawa #3 (`connectedCaseID = 2`):
   - Zdarzenie: "Rozpatrzenie sprawy"

**Wyświetlenie historii dla sprawy #3:**
- System wykrywa `connectedCaseID = 2`, pobiera zdarzenia z #2
- System wykrywa `connectedCaseID = 1` w #2, pobiera zdarzenia z #1
- Wyświetla wszystkie zdarzenia chronologicznie (najstarsze → najnowsze)

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie przepinać dokumentów – użytkownik musi ręcznie (lub przez regułę) utworzyć nową sprawę i ustawić `connectedCaseID`
- **NIE będziemy** obsługiwać cyklicznych powiązań (A → B → A) – system musi mieć zabezpieczenie przed nieskończoną rekurencją

### Punkty otwarte

- **Nazwa pola** – czy `connectedCaseID` jest OK, czy potrzebna inna nazwa? (np. `parentCaseID`, `sourceCaseID`)
- **Limit głębokości rekurencji** – ile poziomów powiązań wspieramy? (np. max 10)

---

## 3. Use case: JRWA – historia przypinania do teczek

**Komponent:** Moduł procesowy – mechanizm historii biznesowej + integracja JRWA

### Cel i problem

**Problem biznesowy:** W systemie JRWA (Jednolite Rzeczowe Wykazy Akt) dokumenty są przypisywane do teczek. Użytkownik otwierający teczkę musi widzieć:
- Jakie dokumenty są **obecnie** w teczce (raport)
- **Pełną historię** – kto, kiedy i dlaczego przypięto/odpięto dokumenty

**Problem techniczny:** Obecny raport pokazuje tylko aktualny stan. Brak historii zmian.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – zapisywanie zdarzeń "przypięcie do teczki" / "odpięcie z teczki" w historii biznesowej.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Mechanizm:**
- Każde przypięcie dokumentu do teczki JRWA generuje zdarzenie w historii biznesowej z:
  - `EventType` (słownikowy): "Przypięcie do teczki JRWA"
  - `BusinessSubject`: `{ Type: 'jrwa_folder', ID: <ID teczki>, Name: <Nazwa teczki> }`
- Każde odpięcie dokumentu generuje analogiczne zdarzenie: "Odpięcie z teczki JRWA"

**Szczegóły techniczne:**
- **EventType (słownik):** Administrator definiuje zdarzenia "Przypięcie do teczki" i "Odpięcie z teczki" w słowniku zdarzeń biznesowych
- **UI teczki JRWA:** Wyświetlanie historii teczki jako filtrowany widok zdarzeń biznesowych (`BusinessSubjectType = 'jrwa_folder'`, `BusinessSubjectID = <ID teczki>`)
- **Pole linked (opcjonalne):** W message można wrzucić link HTML do dokumentu/sprawy dla wygody użytkownika

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

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie generować zdarzeń dla starych przypiętych dokumentów (tylko dla nowych operacji po wdrożeniu)
- **NIE będziemy** wersjonować samej teczki (tylko zdarzenia przypinania/odpinania dokumentów)

### Punkty otwarte

- **Czy zapisywać powód odpięcia?** – np. "Pomyłka", "Dokument nieaktualny"? (pole `Message` może być używane do tego)
- **Czy ograniczać odpinanie?** – czy każdy może odpiąć, czy tylko opiekun teczki?

---

## 4. Mockup UI – wyświetlanie historii biznesowej

**Komponent:** Frontend – widok historii biznesowej

### Cel i problem

**Problem:** Jak wizualnie przedstawić historię biznesową obejmującą zdarzenia z wielu procesów/kontekstów?

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Lista chronologiczna bez kontekstu procesu | Tylko zdarzenia + daty + użytkownik | ❌ Odrzucone – użytkownik nie wie, z którego procesu pochodzi zdarzenie |
| Lista z nazwą procesu przy każdym zdarzeniu | Każde zdarzenie ma widoczną nazwę procesu | 💡 Propozycja – do rozważenia, może być redundantne jeśli wszystkie zdarzenia z jednego procesu |
| Lista z heurystyką (nazwa procesu tylko jeśli się zmienia) | Wyświetlanie nazwy procesu tylko przy zmianie kontekstu | ✅ Wybrana – oszczędność miejsca, dobra czytelność |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – mockup do przekazania klientowi (Rossmann)

**Mockup zawiera:**
- **Chronologiczna lista zdarzeń** (najnowsze na górze lub na dole – do ustalenia)
- **Format wpisu:**
  - **Nazwa zdarzenia** (słownikowa, np. "Pobranie korespondencji z e-Doręczeń")
  - **Data i godzina** (z prawej strony)
  - **Użytkownik/system** (kto wykonał)
  - **Nazwa procesu** (opcjonalnie – tylko jeśli zdarzenie pochodzi z innego procesu niż poprzednie)
  - **Opcjonalnie:** Ikona kierunku (wpłynęło/wypłynęło) – do ewentualnego dorobienia w przyszłości

**Szczegóły techniczne:**
- **Frontend:** Heurystyka – przy renderowaniu porównać nazwę procesu aktualnego zdarzenia z poprzednim; jeśli się różni → wyświetlić nazwę procesu
- **HTML w message:** Obsługa linków HTML w polu `message` (z walidacją security – ochrona przed XSS)
- **Format daty:** Do ustalenia z klientem (np. "3 grudnia 2025, 10:16")

**Przykład wizualizacji (mockup):**
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
│    (ten sam proces)                            │
├────────────────────────────────────────────────┤
│ ↪️ Przekierowanie do innego działu             │
│    Piotr Nowak                 3 gru 2025 10:00│
│    Proces: Obieg korespondencji X             │
└────────────────────────────────────────────────┘
```

**Opcje filtrowania (do rozważenia w przyszłości):**
- "Pokaż tylko z tego procesu"
- "Pokaż cały wątek biznesowy"
- "Wybierz proces" (dropdown)

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie przypisywać ikon do zdarzeń w MVP – ikony można dorobić później przez słownik
- **NIE będziemy** dodawać filtrów w MVP – tylko chronologiczna lista

### Punkty otwarte

- **Kolejność wyświetlania** – najnowsze na górze czy na dole? (użytkownik scrolluje w dół czy w górę?)
- **Czy wyświetlać nagłówek procesu?** – decyzja Rossmann

---

## 5. Wielowymiarowość historii – jeden dokument w wielu kontekstach

**Komponent:** Moduł procesowy – mechanizm wielowymiarowej historii

### Cel i problem

**Problem biznesowy:** Jeden dokument (np. korespondencja) może być jednocześnie:
- Powiązany z **procesem nadrzędnym** (e-Doręczenia → Obieg korespondencji X)
- Powiązany z **klientem** (korespondencja dotyczy Kowalskiego)
- Powiązany z **polisą** (korespondencja dotyczy polisy nr 123/2025)
- Powiązany z **teczką JRWA** (korespondencja przypięta do teczki 2025/01/001)

System musi umożliwić **wielowymiarowe** śledzenie – ten sam dokument widoczny z wielu perspektyw (klient, polisa, teczka, proces).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – umożliwienie przypisania wielu `BusinessSubjects` do jednego zdarzenia.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Mechanizm:**
- Funkcja `AddCaseEvent` przyjmuje **listę** obiektów `BusinessSubject` (nie pojedynczy obiekt)
- Jedno zdarzenie może mieć wiele wpisów w tabeli powiązań, np.:
  - `BusinessSubject 1: { Type: 'case', ID: 1 }` (connectedCase do e-Doręczeń)
  - `BusinessSubject 2: { Type: 'client', ID: 456 }` (klient Kowalski)
  - `BusinessSubject 3: { Type: 'policy', ID: 789 }` (polisa 123/2025)
  - `BusinessSubject 4: { Type: 'jrwa_folder', ID: 999 }` (teczka JRWA)

**Przykład:**
Użytkownik otwiera **widok klienta Kowalskiego** → system wyświetla wszystkie zdarzenia z `BusinessSubjectType = 'client'` i `BusinessSubjectID = 456` → widzi m.in. zdarzenie "Wpłynęła korespondencja dotycząca polisy 123/2025".

Użytkownik otwiera **widok polisy 123/2025** → system wyświetla wszystkie zdarzenia z `BusinessSubjectType = 'policy'` i `BusinessSubjectID = 789` → widzi to samo zdarzenie.

**Szczegóły techniczne:**
- **SQL query (przykład):**
```sql
SELECT DISTINCT ce.*
FROM CaseEvents ce
JOIN CaseEventBusinessSubjects bs ON ce.EventID = bs.EventID
WHERE bs.BusinessSubjectType = 'client'
  AND bs.BusinessSubjectID = 456
ORDER BY ce.EventDate DESC
```

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie propagować powiązań (np. jeśli korespondencja jest powiązana z polisą, a polisa z klientem, to korespondencja NIE jest automatycznie powiązana z klientem – trzeba to ręcznie ustawić w regule)

### Punkty otwarte

- **Czy ograniczać liczbę powiązań?** – np. max 5 powiązań na zdarzenie?
- **Jak obsłużyć konflikty?** – co jeśli ktoś przypisze korespondencję do polisy 1, a potem okaże się, że to polisa 2?

---

## 6. Obsługa błędnego przypisania i cofania

**Komponent:** Moduł procesowy – mechanizm cofania/zmiany powiązań

### Cel i problem

**Problem biznesowy:** Użytkownik może pomylić się i przypisać dokument do niewłaściwej polisy/klienta/teczki. Trzeba to poprawić, ale zachować informację o pomyłce w historii.

**Przykład:** Korespondencja X została przypisana do polisy 1, ale potem okazało się, że dotyczy polisy 2. Trzeba:
1. Odpiąć z polisy 1
2. Przypiąć do polisy 2
3. Zachować informację o pomyłce w historii

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Usunięcie starego zdarzenia | Kasujemy wpis o przypięciu do polisy 1 | ❌ Odrzucone – tracimy informację o pomyłce |
| Nowe zdarzenie "odpięcie" + "przypięcie" | Generujemy dwa zdarzenia: "Odpięto z polisy 1", "Przypięto do polisy 2" | ✅ Wybrana – pełna historia zachowana |
| Edycja istniejącego zdarzenia | Modyfikujemy wpis w tabeli powiązań | ❌ Odrzucone – tracimy audit trail |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Mechanizm:**
- **NIE usuwamy** starych powiązań
- Generujemy **nowe zdarzenia:**
  1. "Odpięcie z polisy 1" (`EventType` słownikowy, `BusinessSubject: policy #1`)
  2. "Przypięcie do polisy 2" (`EventType` słownikowy, `BusinessSubject: policy #2`)
- Opcjonalnie w `message` można wpisać powód (np. "Pomyłka użytkownika", "Zmiana decyzji biznesowej")

**Szczegóły techniczne:**
- **EventType (słownik):** Administrator definiuje zdarzenia typu "Odpięcie" i "Przypięcie" z różnych kontekstów (polisa, klient, teczka JRWA)
- **UI:** Przycisk "Zmień powiązanie" → generuje automatycznie dwa zdarzenia
- **Message:** Pole tekstowe "Powód zmiany" (opcjonalne)

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

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie wykrywać pomyłek – użytkownik musi ręcznie zmienić powiązanie
- **NIE będziemy** cofać zdarzeń do konkretnego punktu w historii (rollback) – tylko pojedyncze odpięcie/przypięcie

### Punkty otwarte

- **Czy wymagać powodu zmiany?** – czy pole "Powód" jest obowiązkowe, czy opcjonalne?
- **Kto może zmieniać powiązania?** – tylko właściciel sprawy, czy każdy z uprawnieniami?

---

## 7. Szczegóły techniczne – standaryzacja wywołania AddCaseEvent

**Komponent:** Backend – API funkcji AddCaseEvent

### Cel i problem

**Problem techniczny:** Obecna funkcja `AddCaseEvent` ma niespójną składnię – czasem `BusinessSubject` jest obiektem wewnątrz `message` (JSON), czasem jest osobnym parametrem. Trzeba ustandaryzować.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Obiekt `Subject` + uzupełnianie obiektu głównego | Można stworzyć obiekt `Subject`, uzupełnić go, a potem dodać do `CaseEvent` | ✅ Akceptowalne – elastyczność |
| Bezpośrednie uzupełnianie `CaseEvent.BusinessSubjects` | Bezpośrednio w parametrze funkcji przekazać listę `BusinessSubjects` | ✅ Preferowane – prostsze, bardziej czytelne |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowa składnia:**
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

**Przykłady:**
```csharp
// Przykład 1: Zdarzenie bez powiązań biznesowych
AddCaseEvent(
  CaseID: 123,
  EventType: "MailSend",
  Message: "Wysłano potwierdzenie do klienta"
)

// Przykład 2: Zdarzenie z jednym powiązaniem
AddCaseEvent(
  CaseID: 123,
  EventType: "ClientAssigned",
  Message: "Przypisano klienta",
  BusinessSubjects: [
    { Type: "client", ID: 456, Name: "Jan Kowalski" }
  ]
)

// Przykład 3: Zdarzenie z wieloma powiązaniami
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

**Migracja z obecnego rozwiązania:**
- Stary sposób (JSON w `message`) pozostaje obsługiwany dla wstecznej kompatybilności
- Nowe implementacje używają `BusinessSubjects`
- Docelowo: stopniowa migracja starych wywołań

### Ograniczenia / Poza zakresem

- **NIE będziemy** automatycznie migrować starych wywołań – to ręczna praca developera
- **NIE będziemy** walidować poprawności ID w `BusinessSubject` na poziomie `AddCaseEvent` – założenie, że developer wie co robi

### Punkty otwarte

- **Nazwa parametru:** `BusinessSubjects` czy `LinkedSubjects` czy `RelatedObjects`?
- **Czy Name jest obowiązkowe?** – system może sam pobrać nazwę z bazy (user, client, etc.)

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Podstawowa tabela powiązań + mechanizm connectedCase

**Cel:** Umożliwienie wieloprocesowego śledzenia historii (use case Rossmann)

**Zakres:**
- Funkcjonalność 1: Utworzenie tabeli `CaseEventBusinessSubjects`
- Funkcjonalność 2: Modyfikacja `AddCaseEvent` – obsługa `BusinessSubjects`
- Funkcjonalność 2: Mechanizm `connectedCaseID` w widoku historii (rekurencyjne ładowanie)
- Funkcjonalność 4: Mockup UI – lista chronologiczna z nazwami procesów

**Ograniczenia MVP 1:**
- Tylko typ powiązania `case` (connectedCase)
- Bez filtrów (tylko pełna lista chronologiczna)
- Bez ikon
- Bez HTML w `message`

---

### MVP 2: JRWA + wielowymiarowość

**Cel:** Rozszerzenie mechanizmu na teczki JRWA i widok 360° klienta

**Zakres:**
- Funkcjonalność 3: Obsługa typów `jrwa_folder`, `client`, `policy`
- Funkcjonalność 3: Widok historii teczki JRWA
- Funkcjonalność 5: Widok 360° klienta (wszystkie zdarzenia dla klienta)
- Funkcjonalność 6: Mechanizm odpinania/przypinania z powodu

---

### MVP 3: UI enhancements

**Cel:** Poprawa UX i dodanie zaawansowanych funkcji

**Zakres:**
- Funkcjonalność 4: Ikony kierunku (wpłynęło/wypłynęło)
- Funkcjonalność 4: Filtry ("pokaż tylko z tego procesu", "wybierz proces")
- Funkcjonalność 4: Obsługa HTML w `message` (linki)
- Funkcjonalność 7: Migracja starych zdarzeń z JSON do nowej tabeli

---

## Punkty do dalszej dyskusji (globalne)

- **Nazewnictwo:** Ustalić finalne nazwy (`connectedCaseID` vs `parentCaseID`, `BusinessSubjects` vs `LinkedSubjects`, etc.)
- **Bezpieczeństwo:** Kto może tworzyć zdarzenia biznesowe? Czy trzeba specjalnego uprawnienia?
- **Auditowanie zmian:** Czy zmiany w powiązaniach są logowane osobno (poza historią biznesową)?
- **Wydajność:** Czy rekurencyjne ładowanie `connectedCase` nie będzie za wolne? (testy wydajnościowe)
- **Rozszerzenie typów powiązań:** Jakie jeszcze typy `BusinessSubjectType` mogą być potrzebne? (np. `contract`, `invoice`, `department`)
- **Mockup Rossmann:** Przekazać mockup do Rossmana, zebrać feedback, ewentualnie doprecyzować szczegóły UI

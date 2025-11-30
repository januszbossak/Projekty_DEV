# Rada Architektów – 2025-09-04

**Powiązane projekty:**
- `cross-cutting/Zakladka-Do-wykonania` – temat 1
- `moduly/Zrodla-danych` – temat 2
- `cross-cutting/Historia-aktywnosci-uprawnien` – tematy 3, 4
- `cross-cutting/Wzmiankowanie-w-komentarzach` – tematy 5, 6, 7

---

## 1. Konfiguracja wyświetlania współpracowników w zakładce "Do wykonania" na poziomie procesu

**Projekt:** `cross-cutting/Zakladka-Do-wykonania`

### Kontekst i Problem

Obecnie ustawienie dotyczące wyświetlania spraw, w których użytkownik jest współpracownikiem (nie właścicielem), jest globalne w ustawieniach systemowych. Klient WIM potrzebuje możliwości konfiguracji tego na poziomie konkretnych procesów. Problem polega na tym, że dla niektórych procesów współpracownicy powinni widzieć sprawy w zakładce "Do wykonania", a dla innych nie. Obecne rozwiązanie globalne nie pozwala na taką elastyczność.

### Zidentyfikowane Ryzyka

- Ryzyko wydajnościowe przy dużej liczbie procesów (100+) – użycie `IN` z listą wielu procesów może być problematyczne
- Ryzyko skomplikowania logiki zapytań SQL
- Ryzyko błędów konfiguracyjnych przy wielu procesach

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Konfiguracja na poziomie procesu (IN) | Lista procesów, dla których wyświetlać współpracowników | ✅ Wybrana – elastyczne, można wybrać konkretne procesy |
| Konfiguracja odwrotna (NOT IN) | Lista procesów, dla których NIE wyświetlać współpracowników | ❌ Odrzucona – zbyt skomplikowane przy dużej liczbie procesów |
| Konfiguracja na poziomie obszaru | Zarządzanie na poziomie obszaru (np. "Do wykonania") | ❌ Odrzucona – jeszcze większe skomplikowanie |
| Filtr w interfejsie | Filtr w zakładce "Do wykonania" do wyboru przez użytkownika | ⏸️ Odroczona – może być rozważona jako alternatywa |

### Decyzja

**Status:** 🔍 Do weryfikacji

Możliwość konfiguracji na poziomie procesu, ale wymaga weryfikacji:
- Ile procesów będzie objętych tą konfiguracją (Mateusz ma to określić)
- Czy użycie `IN` z listą procesów będzie wydajne przy dużej liczbie (np. 100 procesów)
- Wycena implementacji

**Szczegóły techniczne:**
- Obecne zapytanie: `JOIN` lub `UNION` z `Work Case` i `Case Activity`
- Proponowane rozwiązanie: dodanie warunku `Case IN (lista_procesów)` do zapytania
- Możliwość wyłączenia globalnego ustawienia i włączenia tylko dla wybranych procesów
- Jeśli będzie 100 procesów, może być problem wydajnościowy

**Uwaga:** Jeśli klient będzie chciał obsłużyć wiele procesów (np. 100), może być potrzebna wycena i decyzja klienta czy jest w stanie zapłacić za taką implementację.

### Zadania

- **[Damian Kamiński]:** Rozmowa z Mateuszem o dokładnej skali (ile procesów będzie objętych) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Weryfikacja wydajności `IN` z listą procesów → termin: [po określeniu skali]
- **[Damian Kamiński]:** Wycena implementacji po weryfikacji skali → termin: [po weryfikacji]

### Punkty otwarte

- Jaka jest maksymalna liczba procesów, dla których będzie to konfigurowane?
- Czy potrzebny jest limit liczby procesów w konfiguracji?
- Czy można użyć `NOT IN` dla wyjątków (jeśli będzie mniej wyjątków niż głównych procesów)?

---

## 2. Source Get/Set – przerobienie źródeł na dynamic form

**Projekt:** `moduly/Zrodla-danych`

### Kontekst i Problem

Funkcja `Source Get/Set` jest już w Designie, ale wymaga kompleksowego podejścia – wszystkie źródła danych muszą być przerobione na nowy typ `dynamic form`. Obecnie funkcja reguły jest skończona, ale brakuje interfejsu do definiowania nowego źródła typu `dynamic` oraz kolumn, które mają się automatycznie podstawiać. Mateusz już chce z tego korzystać, więc potrzebne jest szybkie rozwiązanie.

### Zidentyfikowane Ryzyka

- Brak czasu w obecnym sprincie (WIM jest priorytetem)
- Ryzyko niekompletnej implementacji jeśli zrobi się tylko część
- Potrzeba kompleksowego podejścia do wszystkich źródeł danych

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Implementacja w obecnym sprincie | Ania zajmuje się tym teraz | ❌ Odrzucona – Ania pomaga Filipowi z matrycą uprawnień, brak czasu |
| Implementacja w przyszłym sprincie | Damian projektuje, Ania implementuje | ✅ Wybrana – bardziej realistyczne, pozwala na kompleksowe podejście |
| Częściowa implementacja | Tylko funkcja reguły bez interfejsu | ❌ Odrzucona – potrzebny jest komplet (funkcja + interfejs) |

### Decyzja

**Status:** ⏸️ Odroczone

Temat przeniesiony na przyszły sprint. Damian zaprojektuje kompleksowe rozwiązanie obejmujące:
- Definiowanie nowego źródła typu `dynamic`
- Definiowanie kolumn dla tego typu źródła (automatyczne podstawianie)
- Interfejs do dodawania źródła bez wgrania pliku (opcjonalnie, ale można dodać)

**Szczegóły techniczne:**
- Typ źródła: `dynamic`
- Interfejs: możliwość dodania źródła bez wgrania pliku (plus do dodania)
- Kolumny: automatyczne podstawianie dla typu `dynamic`
- Funkcja reguły: `Source Get/Set` już gotowa

### Zadania

- **[Damian Kamiński]:** Zaprojektowanie kompleksowego rozwiązania dla źródeł typu `dynamic` → termin: przyszły sprint
- **[Anna Skupińska]:** Implementacja po zaprojektowaniu → termin: przyszły sprint (po zakończeniu pomocy Filipowi z matrycą uprawnień)

### Punkty otwarte

- Czy interfejs do dodawania źródła bez pliku jest potrzebny w MVP?
- Jakie kolumny powinny być domyślnie dostępne dla typu `dynamic`?
- Czy potrzebna jest walidacja przy definiowaniu kolumn?

---

## 3. CaseActivity – zdarzenie "edycja sprawy" rejestrowane ale nie wyświetlane

**Projekt:** `cross-cutting/Historia-aktywnosci-uprawnien`

### Kontekst i Problem

W tabeli `CaseActivity` jest rejestrowane zdarzenie typu "edycja sprawy", które zawsze się loguje (nie da się tego wyłączyć), ale nigdzie nie jest wyświetlane po stronie frontendu. Zdarzenie to jest pomijane przy wyświetlaniu (warunek w zapytaniu pomija te zdarzenia). Nie jest jasne, po co zostało to zrobione i czy powinno być wyświetlane.

### Zidentyfikowane Ryzyka

- Nie zidentyfikowano.

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wyświetlanie zdarzenia "edycja sprawy" | Dodanie do widoku historii aktywności | ⏸️ Odroczona – wymaga decyzji czy to potrzebne |
| Usunięcie rejestrowania | Przestanie logować to zdarzenie | ❌ Odrzucona – może być potrzebne do historii uprawnień |
| Pozostawienie jak jest | Bez zmian | ⏸️ Odroczona – wymaga weryfikacji celu |

### Decyzja

**Status:** 🔍 Do weryfikacji

Piotr sprawdzi, czy zdarzenie "edycja sprawy" jest powiązane z historią uprawnień do sprawy. Hipoteza: przy każdej edycji sprawy zapisuje się stan uprawnień na dany moment, co jest wykorzystywane w funkcjonalności "Sprawdź kto ma uprawnienia do sprawy" (ludziki → uprawnienia → na dole historia uprawnień na daną datę).

**Szczegóły techniczne:**
- Tabela: `CaseActivity`
- Typ zdarzenia: "edycja sprawy"
- Rejestrowanie: zawsze (nie można wyłączyć)
- Wyświetlanie: pomijane (warunek w zapytaniu)
- Możliwe powiązanie: historia uprawnień do sprawy na dany moment edycji

**Uwaga:** Jeśli okaże się, że zdarzenie jest potrzebne do historii uprawnień, należy rozważyć czy powinno być wyświetlane w uproszczonej formie (kto, kiedy edytował) zamiast pełnej historii zmian pól.

### Zadania

- **[Piotr Buczkowski]:** Weryfikacja czy zdarzenie "edycja sprawy" jest powiązane z historią uprawnień → termin: [po spotkaniu]
- **[Piotr Buczkowski]:** Sprawdzenie czy to zdarzenie jest wykorzystywane w funkcjonalności sprawdzania uprawnień → termin: [po spotkaniu]

### Punkty otwarte

- Czy zdarzenie "edycja sprawy" powinno być wyświetlane w historii aktywności?
- Jeśli tak, to w jakiej formie (uproszczonej: kto, kiedy)?
- Czy można wyłączyć rejestrowanie tego zdarzenia, jeśli nie jest potrzebne?

---

## 4. Historia uprawnień – uwzględnienie ustawienia "administrator nie ma praw"

**Projekt:** `cross-cutting/Historia-aktywnosci-uprawnien`

### Kontekst i Problem

W procesie dla Justyny na Strefach jest zaznaczone, że administrator nie ma praw do spraw. To ustawienie nie było uwzględnione w historii uprawnień, przez co Justyna widzi, że administrator ma dostęp, chociaż faktycznie go nie ma. To powoduje mylące informacje w jednym miejscu, podczas gdy system działa poprawnie (administrator faktycznie nie ma dostępu).

### Zidentyfikowane Ryzyka

- Mylące informacje dla użytkowników
- Niespójność między różnymi miejscami wyświetlania uprawnień

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Uwzględnienie ustawienia w historii | Sprawdzanie ustawienia "administrator nie ma praw" przy wyświetlaniu historii | ✅ Wybrana – zapewnia spójność informacji |
| Pozostawienie jak jest | Bez zmian | ❌ Odrzucona – powoduje mylące informacje |

### Decyzja

**Status:** ✅ Zatwierdzone

Uwzględnienie ustawienia "administrator nie ma praw do sprawy" w historii uprawnień, aby informacje były spójne we wszystkich miejscach wyświetlania.

**Szczegóły techniczne:**
- Ustawienie: "administrator nie ma praw do sprawy" (na poziomie procesu)
- Miejsce wyświetlania: historia uprawnień (ludziki → uprawnienia → na dole)
- Problem: ustawienie nie było uwzględniane przy wyświetlaniu historii
- Rozwiązanie: uwzględnienie tego ustawienia przy sprawdzaniu uprawnień w historii

### Zadania

- **[Piotr Buczkowski]:** Uwzględnienie ustawienia "administrator nie ma praw" w historii uprawnień → termin: [po spotkaniu, zgłoszenie w Azure]

### Punkty otwarte

- Czy są inne miejsca, gdzie to ustawienie powinno być uwzględnione?
- Czy potrzebna jest walidacja przy zapisywaniu historii uprawnień?

---

## 5. Wzmiankowanie w komentarzach – powiadomienia i uprawnienia

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`

### Kontekst i Problem

Obecnie gdy ktoś jest wzmiankowany w komentarzu (`@mention`), jest automatycznie dodawany jako obserwator sprawy, ale nie dostaje maila o wzmiankowaniu. Dostaje tylko maila o tym, że został dodany jako obserwator, co jest mylące. Dodatkowo, jako obserwator zaczyna dostawać wszystkie powiadomienia o zmianach w sprawie (zmiana etapu, nowe komentarze), co może nie być pożądane – użytkownik może chcieć tylko zareagować na konkretną wzmiankę, a nie śledzić całą sprawę.

### Zidentyfikowane Ryzyka

- Ryzyko bezpieczeństwa – wzmiankowanie może nieświadomie nadawać uprawnienia osobom spoza grona uprawnionych
- Spam mailowy – obserwatorzy dostają zbyt wiele powiadomień
- Brak świadomości użytkowników – nie wiedzą, że wzmiankowanie nadaje uprawnienia

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wysyłanie maila o wzmiankowaniu | Mail "zostałeś wzmiankowany w komentarzu" | ✅ Wybrana jako minimum – podstawowa funkcjonalność |
| Zmiana roli z obserwatora na Reader | Wzmiankowanie nadaje rolę Reader zamiast obserwatora | ✅ Wybrana – Reader nie dostaje powiadomień o zmianach |
| Pozostawienie jako obserwator | Bez zmian | ❌ Odrzucona – powoduje spam mailowy |
| Ograniczenie listy wzmiankowanych | Możliwość wzmiankowania tylko osób już w sprawie | ⏸️ Odroczona – wymaga dodatkowego interfejsu |
| Dodanie osoby spoza sprawy | Osobny przycisk "Dodaj nową osobę" z wyborem roli | ⏸️ Odroczona – wymaga projektowania interfejsu |
| Ostrzeżenie przy wzmiankowaniu | Komunikat "uwaga, nadajesz uprawnienia" | ⏸️ Odroczona – może być rozważona jako dodatkowe zabezpieczenie |
| Połączenie maili | Jeden mail "zostałeś wzmiankowany i dodany jako Reader" | ✅ Wybrana – unika duplikacji |

### Decyzja

**Status:** ✅ Zatwierdzone

Zmiana logiki wzmiankowania:

1. **Wzmiankowanie nadaje rolę Reader (nie obserwator):**
   - Reader ma dostęp do sprawy, ale nie dostaje powiadomień o zmianach
   - Jeśli użytkownik już ma wyższą rolę (współpracownik, właściciel), nie zmieniamy roli
   - Jeśli użytkownik nie ma dostępu do sprawy, nadajemy rolę Reader

2. **Wysyłanie maila o wzmiankowaniu:**
   - Mail "zostałeś wzmiankowany w komentarzu w sprawie X"
   - Jeśli jednocześnie nadajemy rolę Reader, mail jest połączony: "zostałeś wzmiankowany i dodany jako Reader"
   - Każde wzmiankowanie powoduje wysłanie maila (nie tylko pierwsze)

3. **Powiadomienia o odpowiedziach:**
   - Jeśli ktoś odpowiada na komentarz ze wzmianką (komentarz zagnieżdżony), wzmiankowani dostają powiadomienie
   - Jeśli ktoś pisze równoległy komentarz bez wzmianki, wzmiankowani nie dostają powiadomienia

**Szczegóły techniczne:**
- Rola: `Reader` (zamiast obserwator)
- Mail: dedykowany mail o wzmiankowaniu (nie mail o dodaniu jako obserwator)
- Sprawdzanie istniejących ról: jeśli użytkownik już ma rolę (współpracownik, właściciel), nie nadajemy Reader
- Komentarze zagnieżdżone: powiadomienie dla wzmiankowanych w komentarzu nadrzędnym

**Uwagi:**
- Obecna funkcjonalność działa od 2+ lat, więc zmiana musi być przemyślana
- Rozważane były dodatkowe zabezpieczenia (ograniczenie listy, ostrzeżenia), ale odłożone na później
- Możliwość użycia komunikatora do wzmiankowania osób spoza sprawy (wymaga prośby o dostęp)

### Zadania

- **[Damian Kamiński]:** Opisanie wymagań i logiki wzmiankowania (możliwe użycie Copilota do opisu) → termin: [po spotkaniu]
- **[Piotr Buczkowski]:** Zmiana logiki wzmiankowania z obserwatora na Reader → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Dodanie wysyłania maila o wzmiankowaniu → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Obsługa powiadomień o odpowiedziach na komentarze ze wzmianką → termin: [do ustalenia]

### Punkty otwarte

- Czy potrzebne jest ograniczenie listy wzmiankowanych tylko do osób już w sprawie?
- Czy potrzebne jest ostrzeżenie "uwaga, nadajesz uprawnienia" przy wzmiankowaniu?
- Czy potrzebny jest interfejs do dodawania osób spoza sprawy z wyborem roli?
- Jak obsłużyć przypadek, gdy użytkownik ma rolę `Forbidden` (nie powinien być wzmiankowany)?

---

## 6. Rola Reader – możliwość dodania z interfejsu

**Projekt:** `cross-cutting/Wzmiankowanie-w-komentarzach`

### Kontekst i Problem

Rola `Reader` istnieje w systemie (dostęp bez maili), ale można ją nadać tylko przez regułę (`Adjust Role`), nie ma możliwości dodania z interfejsu. To utrudnia użycie tej roli w przypadkach, gdy chcemy dać komuś dostęp do sprawy bez powiadomień mailowych.

### Zidentyfikowane Ryzyka

- Brak elastyczności w zarządzaniu uprawnieniami
- Trudność w użyciu roli Reader bez znajomości reguł

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dodanie Reader do interfejsu | Możliwość wyboru roli Reader w sidebarze uprawnień | ✅ Wybrana – zwiększa elastyczność |
| Pozostawienie tylko przez reguły | Bez zmian | ❌ Odrzucona – utrudnia użycie |

### Decyzja

**Status:** ✅ Zatwierdzone

Dodanie możliwości nadania roli `Reader` z interfejsu (sidebar uprawnień). Rola powinna być dostępna w liście ról do wyboru obok obserwatora, współpracownika, właściciela.

**Szczegóły techniczne:**
- Miejsce: sidebar uprawnień (obszar uprawnień)
- Rola: `Reader` (dostęp bez maili)
- Nazwa w interfejsie: "Odczyt" lub "Czytelnik" (do ustalenia)
- Różnica od obserwatora: Reader nie dostaje powiadomień mailowych

**Uwaga:** Rola `Forbidden` pozostaje tylko przez reguły (nie powinna być dostępna z interfejsu, bo jest nadawana automatycznie w określonych sytuacjach).

### Zadania

- **[Piotr Buczkowski]:** Dodanie roli Reader do interfejsu zarządzania uprawnieniami → termin: [do ustalenia]
- **[Damian Kamiński]:** Ustalenie nazwy roli w interfejsie (Odczyt/Czytelnik) → termin: [do ustalenia]

### Punkty otwarte

- Jaka nazwa roli w interfejsie będzie najbardziej zrozumiała dla użytkowników?
- Czy potrzebna jest ikona lub opis różnicy między Reader a obserwatorem?

---

## 7. Uwagi techniczne

### CaseActivity – rejestrowanie maili wysłanych ze sprawy

Piotr dodał możliwość włączenia/wyłączenia rejestrowania maili wysłanych ze sprawy w `CaseActivity`. To może zajmować dużo miejsca, więc jest opcjonalne.

### Hotfix – zmiana koloru interfejsu

Łukasz zgłosił problem z automatyczną zmianą koloru interfejsu na czerwony po aktualizacji AMODIT. Problem może być związany z migracją ustawień systemowych do React. Łukasz sprawdzi w ustawieniach systemowych i jeśli nie znajdzie przyczyny, zgłosi jako hotfix.


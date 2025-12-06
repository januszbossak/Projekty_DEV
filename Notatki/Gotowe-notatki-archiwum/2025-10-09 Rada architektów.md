> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-05

# Rada Architektów – 2025-10-09

**Powiązane projekty:**
- `Organizacja-DEV/Dokumentacja-organizacyjna/Narzędzia` – temat 1
- `Moduly/Edytor-procesow` – temat 2
- `Moduly/Eksport-import-definicji-procesow` – temat 3
- `Moduly/Ustawienia-systemowe` – temat 4
- `Moduly/Edytor-procesow/Edytor-formularzy` – temat 4
- `Organizacja-DEV/Dokumentacja-organizacyjna` – tematy 5, 7
- `Moduly/e-Doreczenia` – temat 6

---

## 1. Licencje DevExtreme – klucz licencyjny i zarządzanie biblioteką

**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna/Narzędzia`

### Kontekst i Problem

Anna Skupinska zaimplementowała rozwiązanie problemu z kluczem licencyjnym DevExtreme (wersja 24.1), który powodował ostrzeżenia w konsoli. Rozwiązanie polega na umieszczeniu klucza licencyjnego bezpośrednio w kodzie JavaScript poprzez konfigurację `DevExtreme Config` w pliku `main.tsx` przed inicjalizacją jakichkolwiek komponentów DevExtreme. Klucz jest publiczny ze względu na kliencki charakter aplikacji JavaScript – zgodnie z dokumentacją DevExtreme, klucze licencyjne są publiczne i jeśli zostaną skradzione, można skontaktować się z działem zgodności. Problem pojawił się po aktualizacji z wersji 22 do 23, gdzie zaczęto sprawdzać klucz licencyjny.

### Zidentyfikowane Ryzyka

- Brak systematycznego zarządzania bibliotekami zewnętrznymi
- Ryzyko używania przestarzałych wersji bibliotek (obecnie 24.1, dostępna już 25.2)
- Brak odpowiedzialności za śledzenie zmian i błędów w bibliotekach
- Ryzyko naprawiania błędów po stronie AMODIT, które mogą być już poprawione w nowszych wersjach biblioteki

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Hardcodowanie klucza w kodzie | Umieszczenie klucza licencyjnego bezpośrednio w kodzie JavaScript | ✅ Wybrana – zgodne z dokumentacją DevExtreme, klucze są publiczne ze względu na kliencki charakter aplikacji |
| Ukrywanie klucza | Próba ukrycia klucza licencyjnego | ❌ Odrzucona – niemożliwe w aplikacji klienckiej JavaScript |

### Decyzja

**Status:** ✅ Zatwierdzone

1. **Klucz licencyjny:** Umieszczenie klucza licencyjnego DevExtreme bezpośrednio w kodzie JavaScript jest akceptowalne i zgodne z dokumentacją producenta. Klucze są publiczne ze względu na kliencki charakter aplikacji.

2. **Zakup nowej wersji:** Zakup najnowszej wersji DevExtreme (25.2) zamiast obecnej 24.1. Koszt: ~900 dolarów za pełną licencję, ~600 dolarów za upgrade.

3. **Opiekun biblioteki:** Anna Skupinska zostaje opiekunem biblioteki DevExtreme z obowiązkami:
   - Śledzenie zmian w bibliotece (co kwartał lub przed wydaniem wersji)
   - Sprawdzanie nowych wersji (DevExtreme wydaje wersje 2 razy w roku)
   - W przypadku błędów – pierwsza weryfikacja czy to nie błąd biblioteki
   - Kontakt z supportem DevExtreme w przypadku wykrycia błędów biblioteki
   - Aktualizacja biblioteki przed wydaniem wersji AMODIT

4. **Przypisanie konta:** Anna ma przepiąć konto DevExtreme z danych Janusza na swoje dane, aby otrzymywać newsletter i informacje o nowych wersjach.

**Szczegóły techniczne:**
- Konfiguracja klucza w `main.tsx` przed inicjalizacją komponentów DevExtreme
- Klucz jest publiczny i widoczny w kodzie JavaScript (zminifikowanym)
- Wersja obecna: 24.1, docelowa: 25.2
- DevExtreme wydaje wersje 2 razy w roku

### Zadania

- **[Anna Skupinska]:** Przepięcie konta DevExtreme na swoje dane → termin: [do ustalenia]
- **[Anna Skupinska]:** Śledzenie zmian w DevExtreme (co kwartał lub przed wydaniem) → termin: ciągłe
- **[Ola]** (dział handlowy): Finalizacja zakupu licencji DevExtreme 25.2 → termin: [do ustalenia]
- **[Anna Skupinska]:** Instalacja najnowszej wersji DevExtreme po zakupie → termin: po zakupie

### Punkty otwarte

- Czy wprowadzić podobny model opieki nad innymi bibliotekami zewnętrznymi?
- Jak często sprawdzać aktualizacje bibliotek przed wydaniem wersji AMODIT?

---

## 2. Stany procesów – nazewnictwo i opis działania

**Projekt:** `Moduly/Edytor-procesow`

### Kontekst i Problem

Obecne nazwy stanów procesów ("aktywny", "nieaktywny", "usunięty") są niejasne i nie opisują dokładnie, co się dzieje w każdym stanie. Uczestnicy spotkania nie mają pełnej świadomości konsekwencji wyboru danego stanu. Problem pojawił się w kontekście pytania, czy procesy nieaktywne lub usunięte wykonują reguły cykliczne/automatyczne. Okazuje się, że niezależnie od stanu procesu, wszystkie reguły (w tym okresowe) są wykonywane w tle. Jedyną różnicą między stanami jest wyświetlanie procesu na liście procesów (dla administratora i użytkownika).

### Zidentyfikowane Ryzyka

- Niezrozumienie konsekwencji wyboru stanu procesu przez konsultantów
- Ryzyko nieoptymalnego wykorzystania zasobów (reguły okresowe wykonują się dla procesów "usuniętych")
- Brak możliwości zatrzymania reguł dla procesów archiwalnych
- Ryzyko tworzenia reguł okresowych na procesach "usuniętych" przez konsultantów, którzy zakładają że proces nieaktywny = reguły nie działają

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zmiana nazw stanów | Zmiana nazw na bardziej opisowe (np. "widoczny na listach", "niewidoczny na listach") | ✅ Wybrana – lepsze opisanie działania zamiast niejasnych nazw |
| Dodanie opisu do każdego stanu | Dodanie akapitu opisu wyjaśniającego co się dzieje w danym stanie | ✅ Wybrana – równolegle z lepszymi nazwami |
| Nowa kategoria "zatrzymane" | Utworzenie czwartej kategorii procesu, gdzie reguły okresowe nie są wykonywane | ✅ Wybrana – dla procesów archiwalnych, gdzie wszystko ma być zamrożone |
| Zmiana działania istniejących stanów | Zmiana logiki tak, aby "usunięte" nie wykonywały reguł | ❌ Odrzucona – problem kompatybilności wstecznej, klienci mogą polegać na obecnym działaniu |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Odroczone

**Dla istniejących stanów:**
- Zmiana nazewnictwa i dodanie opisów wyjaśniających dokładnie, co się dzieje w każdym stanie
- Opis powinien zawierać informację, że niezależnie od stanu, reguły okresowe są wykonywane dla wszystkich stanów
- Opis powinien wyjaśniać, że jedyną różnicą jest wyświetlanie na liście procesów

**Dla nowej kategorii:**
- Utworzenie czwartej kategorii procesu (proponowana nazwa: "zatrzymane" lub "archiwalny")
- W tej kategorii reguły okresowe nie są wykonywane
- Sprawy z takiego procesu leżą w archiwum i nic się nie dzieje
- Reguły automatyczne mogą nadal działać (gdy użytkownik wchodzi w sprawę, może być potrzeba przeliczenia)

**Szczegóły techniczne:**
- Obecne stany: "aktywny", "nieaktywny", "usunięty"
- Wszystkie stany: reguły okresowe działają, sprawy działają, można tworzyć sprawy przez CreateCase
- Różnica: tylko wyświetlanie na liście procesów (dla administratora i użytkownika)
- Proces nieaktywny: wyświetla się administratorowi, nie wyświetla się użytkownikowi
- Proces usunięty: nie wyświetla się ani administratorowi, ani użytkownikowi

### Zadania

- **[Damian Kaminski]:** Opisanie obecnego stanu działania stanów procesów na wiki → termin: [do ustalenia]
- **[Damian Kaminski]:** Przygotowanie propozycji zmian nazw i opisów stanów → termin: [do ustalenia]
- **[Łukasz Bott]:** Dodanie opisów stanów w formularzu ustawień procesu → termin: [do ustalenia]
- **[Damian Kaminski]:** Planowanie implementacji nowej kategorii "zatrzymane" na kolejne kwartały → termin: [do ustalenia]

### Punkty otwarte

- Jak dokładnie nazwać nową kategorię ("zatrzymane", "archiwalny", "zamrożone")?
- Co ze sprawami otwartymi według procesu "zatrzymanego" – czy mogą być dalej procedowane?
- Czy wszystkie reguły automatyczne powinny działać dla procesu "zatrzymanego", czy tylko niektóre?
- Czy sekcje techniczne powinny być dostępne dla procesu "zatrzymanego"?

---

## 3. Import procesów – blokowanie nadpisywania przy konfliktach przypisań pól

**Projekt:** `moduly/Eksport-import-definicji-procesow`

### Kontekst i Problem

Przy imporcie procesu z konfliktami przypisań pól do kolumn CaseText (np. gdy na produkcji dodano pole ręcznie, a na deweloperze dodano pole o tej samej nazwie, ale zostało przypisane do innej kolumny CaseText), nadpisanie procesu może spowodować przekłamanie danych. Przykład z Polpharmy: pole dodane ręcznie na produkcji zostało przypisane do CaseText6, a na deweloperze nowe pole o tej samej nazwie zostało przypisane do CaseText7. Po imporcie z dewelopera na produkcję, dane z CaseText6 przeszły do CaseText7, co spowodowało problemy z tworzeniem spraw (brakowało danych w polach pracownika).

### Zidentyfikowane Ryzyka

- Przekłamanie danych przy nadpisaniu procesu z konfliktami przypisań
- Niemożność automatycznego naprawienia konfliktów przypisań pól
- Ryzyko utraty danych klienta przy błędnym imporcie
- Brak świadomości konsultantów o konsekwencjach nadpisania procesu z konfliktami

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Blokowanie nadpisywania | Blokada nadpisywania procesu, gdy wykryto konflikty przypisań pól | ✅ Wybrana – bezpieczniejsze niż ryzyko przekłamania danych |
| Pozwolenie na tworzenie nowego procesu | Możliwość utworzenia nowego procesu zamiast nadpisania | ⏸️ Odroczona – możliwe, ale wymaga dobrego komunikatu, aby nie było nadużywane |
| Automatyczne naprawienie | Automatyczne przepisanie przypisań pól | ❌ Odrzucona – zbyt ryzykowne, może spowodować błędy |
| Komunikat ostrzegawczy | Ostrzeżenie, ale pozwolenie na nadpisanie | ❌ Odrzucona – użytkownicy mogą zignorować ostrzeżenie |

### Decyzja

**Status:** ✅ Zatwierdzone

Blokowanie możliwości nadpisania procesu przy imporcie, gdy wykryto konflikty przypisań pól do kolumn CaseText, których nie da się automatycznie naprawić. W takim przypadku system powinien wyświetlić komunikat informujący, że nie można nadpisać procesu i należy ręcznie poprawić przypisania na procesie źródłowym (ze środowiska źródłowego), a następnie wyeksportować i zaimportować plik ponownie.

**Szczegóły techniczne:**
- Konflikt: gdy pole o tej samej nazwie jest przypisane do różnych kolumn CaseText na różnych środowiskach
- Komunikat powinien być zrozumiały i wskazywać konkretne kroki naprawy
- Możliwość utworzenia nowego procesu pozostaje (ale z konsekwencjami – sprawy nie będą przeniesione)

### Zadania

- **[Piotr Buczkowski]:** Implementacja blokady nadpisywania przy konfliktach przypisań pól → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Przygotowanie komunikatu informującego o konieczności ręcznej naprawy → termin: [do ustalenia]

### Punkty otwarte

- Jak zaprojektować komunikat, aby był zrozumiały i nie zachęcał do tworzenia nowego procesu jako obejścia?

---

## 4. Środowisko produkcyjne – blokowanie/ostrzeganie przy dodawaniu pól

**Projekt:** `moduly/Ustawienia-systemowe`, `Moduly/Edytor-procesow/Edytor-formularzy`

### Kontekst i Problem

Konsultanci czasem dodają pola bezpośrednio na środowisku produkcyjnym, co powoduje rozjechanie się środowisk (produkcja vs test/deweloper). Przykład z Polpharmy: pole dodane ręcznie na produkcji, a później dodane na deweloperze, spowodowało konflikt przypisań pól do kolumn CaseText. Problem wynika z braku świadomości konsultantów i braku mechanizmu blokującego lub utrudniającego takie operacje na produkcji. Łukasz Bott powtarza przy każdym szkoleniu, że tak się nie robi, ale nowi wdrożeniowcy nie pamiętają.

### Zidentyfikowane Ryzyka

- Rozjechanie się środowisk produkcyjnych i testowych
- Konflikty przy imporcie procesów między środowiskami
- Ryzyko utraty kompatybilności między środowiskami
- Brak możliwości weryfikacji zmian przed wdrożeniem na produkcję

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Parametr systemowy "produkcja" | Oznaczenie środowiska jako produkcyjne w ustawieniach systemowych | ✅ Wybrana – podstawowy mechanizm |
| Blokowanie dodawania pól na produkcji | Całkowite zablokowanie możliwości dodawania pól | ❌ Odrzucona – mogą być sytuacje awaryjne wymagające dodania pola |
| Ostrzeżenie z potwierdzeniem | Ostrzeżenie z koniecznością potwierdzenia (np. kod z maila) | ✅ Wybrana – utrudnia, ale nie blokuje całkowicie |
| Checkbox "chcę wprowadzać zmiany" | Checkbox do zaznaczenia przy każdym wejściu na zakładkę edycji pól | ✅ Wybrana – dodatkowe utrudnienie, świadomość działania |
| Oznaczenie na poziomie procesu | Oznaczenie procesu jako produkcyjnego | ❌ Odrzucona – łatwo zapomnieć oznaczyć |
| Kolumna CaseText tylko do odczytu na produkcji | Kolumna przypisania CaseText tylko do odczytu na produkcji | 💡 Propozycja – do rozważenia równolegle z innymi zmianami |

### Decyzja

**Status:** 🔍 Do weryfikacji / ⏸️ Odroczone

Wprowadzenie mechanizmu oznaczania środowiska jako produkcyjnego i utrudnienia dodawania pól na produkcji:

1. **Parametr systemowy:** Dodanie parametru systemowego oznaczającego, że środowisko jest produkcyjne (globalnie, nie na poziomie procesu).

2. **Mechanizm utrudniający:** 
   - Ostrzeżenie przy próbie dodania pola na produkcji
   - Możliwość potwierdzenia (np. kod z maila lub checkbox "jestem świadomy konsekwencji")
   - Checkbox do zaznaczenia przy każdym wejściu na zakładkę edycji pól ("chcę wprowadzać zmiany i jestem świadomy, że zaburzę kompatybilność ze środowiskiem testowym")

3. **Kolumna CaseText:** Rozważenie ustawienia kolumny przypisania CaseText jako tylko do odczytu na produkcji (wymaga równoległego wprowadzenia możliwości ręcznego przypisania pól w szczególnych przypadkach).

4. **Ręczne przypisanie pól:** Wprowadzenie możliwości ręcznego definiowania przypisania pola do kolumny CaseText w szczególnych przypadkach (równolegle z oznaczeniem środowiska produkcyjnego).

**Szczegóły techniczne:**
- Parametr systemowy: globalny, odczytywalny w regułach
- Mechanizm jednorazowy (nie odznaczanie checkboxa na stałe)
- Reguły mogą nadal być dodawane na produkcji (szybka reakcja na problemy)

### Zadania

- **[Damian Kaminski]:** Zaplanowanie implementacji parametru systemowego "produkcja" → termin: [do ustalenia]
- **[Damian Kaminski]:** Projektowanie mechanizmu ostrzegania/przy dodawaniu pól → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Implementacja możliwości ręcznego przypisania pola do kolumny CaseText → termin: [do ustalenia]
- **[Łukasz Bott]:** Dodanie opisów i ostrzeżeń w interfejsie edycji pól → termin: [do ustalenia]

### Punkty otwarte

- Czy parametr "produkcja" powinien być możliwy do odustawienia z interfejsu, czy tylko przez bazę danych?
- Jak często powinien być wymagany checkbox "chcę wprowadzać zmiany" – przy każdym wejściu na zakładkę czy raz na sesję?
- Czy reguły również powinny być objęte mechanizmem ostrzegania na produkcji?
- Czy kolumna CaseText powinna być tylko do odczytu na produkcji?

---

## 5. Backlog i zgłoszenia na radę – porządkowanie i proces pracy

**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna`

### Kontekst i Problem

W Azure DevOps jest ponad 134 zgłoszeń oznaczonych tagiem "rada", w tym wiele starszych niż rok. Obecny proces pracy na radzie jest niejasny – nie wiadomo, które tematy są aktualnie istotne, które są związane z bieżącymi projektami, a które są "nice to have" i mogą leżeć latami. Problem pojawił się w kontekście dyskusji o tym, jak organizować tematy na radzie i które zgłoszenia przeglądać.

### Zidentyfikowane Ryzyka

- Przeglądanie setek nieaktualnych zgłoszeń podczas rady
- Gubienie się w zgłoszeniach (część na "następne", część na "inbox", część na "może kiedyś", część na sprinty sprzed 6 miesięcy)
- Brak jasności, które tematy są aktualnie istotne
- Ryzyko pominięcia ważnych tematów związanych z bieżącymi projektami

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Usunięcie tagu "rada" ze starych zgłoszeń | Usunięcie tagu "rada" ze zgłoszeń starszych niż bieżący rok | ✅ Wybrana – porządkowanie backlogu |
| Praca na backlogu zamiast tagu "rada" | Przejście na przeglądanie backlogu zamiast setek zgłoszeń z tagiem | ✅ Wybrana – bardziej uporządkowane |
| Usunięcie statusów "następne" i "może kiedyś" | Uproszczenie do jednego backlogu | ✅ Wybrana – jeden backlog jako źródło prawdy |
| Oznaczanie tematów związanych z projektami | Tematy związane z aktualnymi projektami powinny być omawiane na radzie | ✅ Wybrana – jasny proces |

### Decyzja

**Status:** ✅ Zatwierdzone

1. **Porządkowanie backlogu:**
   - Usunięcie tagu "rada" ze wszystkich zgłoszeń starszych niż bieżący rok
   - Przejrzenie zgłoszeń z bieżącego roku i przeniesienie istotnych na backlog
   - Usunięcie statusów "następne" i "może kiedyś" – jeden backlog jako źródło prawdy

2. **Proces pracy na radzie:**
   - Rada pracuje na backlogu (zgłoszenia oznaczone jako "ready to do" i z tagiem "rada")
   - Tematy związane z aktualnymi projektami (np. Repozytorium, OSTM) powinny być omawiane na radzie, gdy pojawiają się wątpliwości techniczne
   - Tematy "nice to have" nie są omawiane na radzie, dopóki nie zaczniemy się nimi zajmować w ramach projektu

3. **Skład rady:**
   - Stały członek: Piotr Buczkowski
   - Pozostali deweloperzy dopraszani w zależności od tematu
   - Nie wszyscy muszą być na każdej radzie

**Szczegóły techniczne:**
- Backlog: jeden backlog, statusy: new, investigate, ready to do
- Tag "rada": tylko dla tematów bieżących (bieżący rok)
- Tematy ze sprintu: deweloperzy mogą dodawać tematy z bieżącego sprintu do rady

### Zadania

- **[Kamil Dubaniowski]:** Usunięcie tagu "rada" ze zgłoszeń starszych niż bieżący rok → termin: [do ustalenia]
- **[Kamil Dubaniowski]:** Przejrzenie zgłoszeń z bieżącego roku i przeniesienie istotnych na backlog → termin: [do ustalenia]
- **[Kamil Dubaniowski]:** Usunięcie statusów "następne" i "może kiedyś" z backlogu → termin: [do ustalenia]

### Punkty otwarte

- Jak często przeglądać backlog pod kątem tematów do rady?
- Czy powinien być automatyczny proces przypominania o tematach związanych z projektami?

---

## 6. Doręczenia Poczty Polskiej – problem z integracją na chmurze

**Projekt:** `Moduly/e-Doreczenia`

### Kontekst i Problem

Od ponad 3 miesięcy klienci produkcyjni nie mogą pracować na chmurze z doręczeniami, ponieważ integracja z Pocztą Polską nie działa. Problem występuje tylko na środowisku chmurowym – na środowiskach testowych (Sylwet, Batman) i u klientów on-premise działa poprawnie. Adrian Kotowski pinguje Poczta Polską przez portal zgłoszeń, ale od 3 miesięcy nie ma odpowiedzi. Problem polega na tym, że API Poczty Polskiej nie zwraca komunikatu o niepoprawnym uwierzytelnieniu lub braku uwierzytelnienia na usłudze na chmurze, podczas gdy na innych serwerach działa poprawnie z tymi samymi wersjami integracji.

### Zidentyfikowane Ryzyka

- Klienci produkcyjni płacą za wdrożenie, które nie działa
- Brak możliwości korzystania z doręczeń na chmurze przez klientów produkcyjnych
- Ryzyko utraty zaufania klientów
- Brak postępów w rozwiązaniu problemu przez 3 miesiące

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Problem po stronie Poczty Polskiej | Problem jest po stronie Poczty Polskiej | 🔍 Do weryfikacji – wymaga testów z różnych serwerów |
| Problem po stronie AMODIT | Problem jest po stronie AMODIT (konfiguracja, certyfikaty, lokalizacja serwerów) | 🔍 Do weryfikacji – wymaga testów |
| Ograniczenie lokalizacyjne | Poczta Polska dodała ograniczenie lokalizacyjne (serwery w Amsterdamie) | 💡 Propozycja – możliwe rozwiązanie przez proxy |
| Problem z certyfikatami | Problem z certyfikatami lub konfiguracją Azure Key Vault | 🔍 Do weryfikacji – wymaga testów |

### Decyzja

**Status:** 🔍 Do weryfikacji

Adrian Kotowski ma przygotować program testowy, który:
1. Próbuje połączyć się z API Poczty Polskiej używając tego samego klucza/certyfikatu
2. Uruchamiany z różnych serwerów (komputer Adriana, Sylwet testowy, stary serwer testowy Batman, chmura)
3. Pobiera certyfikat z Azure Key Vault (aby nie bawić się ręcznym kopiowaniem)
4. Sprawdza, czy problem występuje tylko na chmurze

Jeśli program działa z innych serwerów, a nie działa z chmury → problem po stronie AMODIT (konfiguracja, certyfikaty, lokalizacja, proxy).

**Szczegóły techniczne:**
- Problem: brak komunikatu o błędzie uwierzytelnienia z API Poczty Polskiej na chmurze
- Działa: środowiska testowe (Sylwet, Batman), klienci on-premise
- Nie działa: chmura AMODIT
- Serwery chmurowe: Amsterdam
- Możliwe rozwiązanie: proxy jeśli problem lokalizacyjny

### Zadania

- **[Adrian Kotowski]:** Przygotowanie programu testowego do połączenia z API Poczty Polskiej → termin: [do ustalenia]
- **[Adrian Kotowski]:** Testowanie z różnych serwerów (komputer Adriana, Sylwet, Batman, chmura) → termin: [do ustalenia]
- **[Piotr Buczkowski]:** Przypilnowanie Adriana odnośnie testów i wykrycia błędu → termin: [do ustalenia]
- **[Janusz Bossak]:** Kontakt z Adrianem w razie potrzeby eskalacji → termin: [do ustalenia]

### Punkty otwarte

- Czy problem jest po stronie Poczty Polskiej czy AMODIT?
- Czy potrzebne jest wprowadzenie proxy jeśli problem lokalizacyjny?
- Jak długo jeszcze czekać na odpowiedź z Poczty Polskiej przed eskalacją?

---

## 7. Podejście biznesowe deweloperów – dyskusja ogólna

**Projekt:** `Organizacja-DEV/Dokumentacja-organizacyjna`

### Kontekst i Problem

Janusz Bossak zwrócił uwagę na problem, że wielu deweloperów ma bardzo techniczne podejście i nie czuje potrzeby biznesowej. Przykłady:
- Adrian Kotowski: problem z doręczeniami trwa 3 miesiące, ale nie było eskalacji ani aktywnego działania
- Neuca (integracja z innym systemem): wycena na 20 000 za rozwiązanie, które nie realizuje potrzeby klienta (6-7 endpointów, ale nie o to chodziło klientowi)
- Deweloperzy patrzą tylko na stronę techniczną (endpointy, TibCo), a nie na to, czy rozwiązanie przyda się użytkownikowi

Jedyną osobą z doświadczeniem biznesowym jest Piotr Buczkowski, który ma doświadczenie z wielu wdrożeń.

### Zidentyfikowane Ryzyka

- Tworzenie rozwiązań, które nie realizują potrzeb klienta
- Brak zrozumienia perspektywy biznesowej u deweloperów
- Ryzyko utraty klientów przez nieodpowiednie rozwiązania
- Brak eskalacji problemów biznesowych (np. doręczenia)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Delegowanie deweloperów na wdrożenia | Oddanie deweloperów na miesiąc na wdrożenia, aby zobaczyli problemy użytkowników | 💡 Propozycja – do rozważenia, ale z klientem wewnętrznym (Justyna), nie zewnętrznym |
| Szkolenia biznesowe | Szkolenia deweloperów z perspektywy biznesowej | ⏸️ Odroczona – nie rozwiąże problemu |
| Lepsze role łączące biznes z deweloperami | Wzmocnienie roli osób łączących biznes z techniką | ✅ Zauważone – ale nie rozwiązane |

### Decyzja

**Status:** 💡 Propozycja

💭 Pomysł Janusza: delegowanie deweloperów na wdrożenia (np. Ania, Marek) na miesiąc, aby wdrożyli moduł raportowy i przygotowali 20 raportów pod potrzeby klienta. To pozwoliłoby im zobaczyć problemy użytkowników i zrozumieć, co jest trudne w użyciu. Propozycja wymaga rozważenia, ale z klientem wewnętrznym (Justyna), nie zewnętrznym, aby nie ryzykować utraty zespołu.

**Uwaga:** To jest ogólna dyskusja, nie konkretna decyzja. Problem jest znany w całym świecie IT i nie ma prostego rozwiązania. Rola osób łączących biznes z techniką (jak Janusz, Damian) jest kluczowa.

### Zadania

- Brak konkretnych zadań – temat wymaga dalszego rozważenia

### Punkty otwarte

- Czy delegowanie deweloperów na wdrożenia jest dobrym rozwiązaniem?
- Jak poprawić zrozumienie perspektywy biznesowej u deweloperów?
- Czy problem z Neuca wynika z braku opieki biznesowej (Daniel Reszka) czy z podejścia deweloperów?


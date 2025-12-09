> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-08

# Rada Architektów – 2025-11-25

**Tematy:**
- Integracja z Active Directory - mechanizm licencjonowania kont
- Problem "osiągnięto limit spraw" w Rossmanie - znikający obiekt licencji
- Semantyka usuwania w rejestrach - konflikt klucza przy synchronizacji
- Przegląd rejestrów i propozycje usprawnień
- Integracja DocuSign z AMODIT - mechanizm envelope
- OAuth w CallRest - rozszerzenie funkcjonalności
- Podpisywanie masowe dokumentów na raporcie - proces odbioru korespondencji
- Problem licencyjny KSeF Connector - zależność od REST API
- Problem wyświetlania pola "Podpis" - nierówne kafelki

---

## 1. Integracja z Active Directory - mechanizm licencjonowania kont

### Kontekst i Problem

Pytanie dotyczyło zasad licencjonowania użytkowników w kontekście integracji z Active Directory. Wątpliwości wzbudził sposób liczenia aktywnych kont - czy mechanizm działa tak samo dla kont tworzonych ręcznie jak i synchronizowanych z AD. Temat wywołany przez pytanie od LOTU oraz wewnętrzne dyskusje zespołu konsultantów.

### Zidentyfikowane Ryzyka

- Niezrozumienie mechanizmu przez konsultantów może prowadzić do błędnych odpowiedzi dla klientów
- Nieprawidłowa interpretacja mechanizmu może prowadzić do problemów przy wdrożeniach z AD

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Mechanizm licencjonowania działa identycznie niezależnie od źródła kont (ręczne tworzenie, AD, tabela, inne):
- Limit licencji dotyczy liczby **aktywnych kont**, które mogą się zalogować do systemu
- Synchronizacja z AD **nie sprawdza automatycznie** stanu licencji podczas synchronizacji
- Kontrola limitu następuje **w momencie próby zalogowania**
- Jeśli liczba kont przekracza limit licencji:
  - Pierwsze N kont (wg ID) pozostaje aktywnych
  - Konta przekraczające limit są **blokowane w pamięci** z powodu braku licencji (nie w bazie danych)
  - **Konta administratorów mają priorytet** - są zawsze w puli odblokowanych kont
- Zablokowane konto z powodu braku licencji **nie odblokowuje się automatycznie** po wylogowaniu innego użytkownika
- Aby odblokować konto przekraczające limit, administrator musi **ręcznie zablokować** inne konto
- Zablokowane konto automatycznie odblokowuje się tylko gdy:
  - Jest jedynym kontem zablokowanym i ma najniższe ID spośród zablokowanych
  - Zostanie awansowane na administratora (wchodzi w pulę priorytetową)

**Szczegóły techniczne:**
- Blokada z powodu braku licencji jest stanem w pamięci, nie zapisem w bazie
- Jeśli zsynchronizowano 1000 kont z AD, a limit wynosi 750:
  - Pierwsze 750 kont (wg ID) będzie aktywnych
  - Ostatnie 250 kont nie będzie mogło się zalogować
  - Komunikat: "Nie możesz się zalogować - przekroczono limit licencji"

### Zadania

- **Łukasz Bott:** Potwierdzić odpowiedź dla LOTU zgodnie z ustalonym mechanizmem

### Punkty otwarte

Brak

---

## 2. Problem "osiągnięto limit spraw" w Rossmanie - znikający obiekt licencji

### Kontekst i Problem

W Rossmanie okresowo pojawia się błąd "osiągnięto limit spraw dla procesu", który występuje losowo i nie jest obecnie możliwy do rozwiązania. Problem analizowany był już przez 3 różne osoby w przeszłości, ale nikt nie zidentyfikował przyczyny. Wczoraj (24.11.2025) pojawił się kolejny przypadek. Problem ma charakter sporadyczny - najczęściej kolejne wywołanie usługi działa poprawnie.

### Zidentyfikowane Ryzyka

- Problem może mieć podłoże sieciowe, co utrudnia analizę
- Brak rozwiązania powoduje okresowe problemy u klienta (Rossmann)
- Problem występuje od wielu lat bez identyfikacji przyczyny źródłowej

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** 🔍 Do weryfikacji

Problem wymaga ponownej analizy z uwzględnieniem aktualnego przypadku z 24.11.2025. Przyczyna najprawdopodobniej związana z **znikaniem obiektu licencji z pamięci** w usłudze. Możliwe przyczyny:
- Błędy sieciowe uniemożliwiające odświeżenie obiektu licencji
- Błędy dostępu do bazy danych w momencie odświeżania
- Problem w mechanizmie cache'owania obiektu licencji

**Szczegóły techniczne:**
- Błąd występuje w usłudze (LOT Mail lub LOT)
- Obiekt licencji znika z pamięci i nie udaje się go odświeżyć
- Najczęściej kolejne wywołanie usługi działa poprawnie (obiekt się odtwarza)
- Wczoraj była jedna seria maili z błędem, potem już działało

### Zadania

- **Piotr Buczkowski:** Sprawdzić logi serwera z 24.11.2025 - zidentyfikować czy wystąpiły błędy dostępu do bazy danych w momencie lub kilka minut przed wysłaniem maili z błędem
- **Piotr Buczkowski:** Przeanalizować mechanizm odświeżania obiektu licencji w usłudze - zidentyfikować przypadki, w których obiekt może zniknąć z pamięci

### Punkty otwarte

- Czy problem ma charakter sieciowy czy aplikacyjny?
- Czy można dodać mechanizm retry przy odświeżaniu obiektu licencji?
- Czy można dodać dodatkowe logowanie dla łatwiejszej diagnostyki w przyszłości?

---

## 3. Semantyka usuwania w rejestrach - konflikt klucza przy synchronizacji

### Kontekst i Problem

Zgłoszenie dotyczyło problemu z synchronizacją rejestrów - komunikat "klucz nie jest unikalny" był mylący, ponieważ nie wskazywał, że konflikt może wynikać ze spraw usuniętych. Problem zgłoszony przez młodszego wdrożeniowca, ale spotykany także przez doświadczonych konsultantów. Wątpliwości dotyczą także semantyki "usuwania" w rejestrach - czy to rzeczywiste usunięcie czy dezaktywacja.

Dodatkowy kontekst historyczny: koncepcja "usuwania" w rejestrach miała symulować **dezaktywację** (jak w słownikach), aby zachować integralność danych gdy wpis był używany na sprawach. Sprawy "usunięte" z rejestrów nie pojawiają się domyślnie w widoku usuniętych, chyba że zafiltrujemy po konkretnym rejestrze.

### Zidentyfikowane Ryzyka

- Mylący komunikat powoduje stratę czasu wdrożeniowców
- Niezrozumienie semantyki "usuwania" w rejestrach prowadzi do błędów
- Brak intuicyjnego dostępu do "usuniętych" spraw rejestrów utrudnia diagnozę
- Możliwość przypadkowego utworzenia duplikatów (sprawy z pustymi kluczami)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Wykluczenie usuniętych spraw z unikalności klucza | Usunięte sprawy nie byłyby sprawdzane przy walidacji klucza | ❌ Odrzucona - może prowadzić do duplikatów, jeśli ktoś ręcznie tworzy nową sprawę zamiast przywrócić usuniętą |
| Automatyczne przywracanie usuniętej sprawy | Gdy synchronizacja napotka klucz istniejący w usuniętych, automatycznie przywraca sprawę i aktualizuje jej dane | ✅ Wybrana - spójna z logiką dezaktywacji, zachowuje historię, eliminuje duplikaty |
| Poprawa komunikatu błędu | Rozszerzenie komunikatu o wskazanie sprawdzenia spraw usuniętych | ✅ Wybrana - szybkie rozwiązanie dla młodszych wdrożeniowców, nie wymaga zmian w logice |

### Decyzja

**Status:** ✅ Zatwierdzone

Zespół zatwierdził dwa działania:

**1. Poprawa komunikatu błędu (natychmiastowe):**
Komunikat "klucz nie jest unikalny" zostanie rozszerzony o wskazanie: "Sprawdź wszystkie istniejące sprawy tego rejestru, w tym usunięte". To rozwiązuje problem dla wdrożeniowców testujących synchronizację, którzy często mają sprawy testowe w statusie usuniętym.

**2. Automatyczne przywracanie usuniętej sprawy podczas synchronizacji:**
Jeśli synchronizacja napotka klucz, który istnieje w sprawie usuniętej:
- Sprawa zostanie automatycznie przywrócona (wznowiona)
- Dane sprawy zostaną zaktualizowane zgodnie z danymi ze źródła
- Zachowana zostanie historia sprawy i ewentualne powiązania

**Decyzja architektoniczna długoterminowa (odroczona):**
Rozróżnienie semantyczne między "usuwaniem" a "dezaktywacją" w rejestrach:
- Wprowadzenie dedykowanego statusu "dezaktywowane" dla rejestrów (zamiast "usunięte")
- Dedykowany widok dla dezaktywowanych wpisów rejestrów (bez potrzeby filtrowania)
- Prawdziwe "usunięcie" jako osobna opcja (ukryta dla zaawansowanych użytkowników)

**Szczegóły techniczne:**
- Klucz sprawdzany jest na wszystkich sprawach (aktywnych + usuniętych)
- Sprawy "usunięte" z rejestrów nie wyświetlają się domyślnie w zakładce "Usunięte" (wymagany filtr po rejestrze)
- Tworzenie nowych spraw w rejestrze może prowadzić do duplikatów z pustymi kluczami (klucz pusty jest dozwolony przy tworzeniu)
- Domyślnie tylko administratorzy mogą tworzyć sprawy w rejestrze (opcja "Kto może tworzyć sprawy")

### Zadania

- **Damian Kamiński:** Zgłosić PBI - rozszerzenie komunikatu błędu o wskazanie sprawdzenia spraw usuniętych
- **Kamil Dubaniowski:** Zgłosić PBI - automatyczne przywracanie usuniętej sprawy podczas synchronizacji (z warunkiem: klucz musi być unikalny)
- **Zespół architektów:** Zaplanować refaktoring semantyki usuwania/dezaktywacji w rejestrach (długoterminowo)

### Punkty otwarte

- Czy należy walidować unikalność klucza także przy tworzeniu nowych spraw w rejestrze? (obecnie można utworzyć nieskończoną liczbę spraw z pustym kluczem)
- Jak rozwiązać problem intuicyjnego dostępu do dezaktywowanych wpisów rejestrów? (dedykowany widok vs filtr)

---

## 4. Przegląd rejestrów i propozycje usprawnień

### Kontekst i Problem

Podczas dyskusji o problemach z rejestrami (temat 3) pojawiła się szersza refleksja nad stanem funkcjonalności rejestrów w AMODIT. Zespół zidentyfikował szereg problemów użyteczności i ergonomii, które powodują, że wdrożeniowcy muszą za każdym razem tworzyć dedykowane raporty dla rejestrów, a proces pracy z rejestrami nie jest intuicyjny.

### Zidentyfikowane Ryzyka

- Brak dedykowanych widoków dla rejestrów wydłuża czas wdrożeń
- Wdrożeniowcy muszą za każdym razem tworzyć raporty dla rejestrów ręcznie
- Brak walidacji unikalności klucza przy tworzeniu spraw prowadzi do błędów
- Niejednolity model dostępu (przez raporty vs przez dedykowany widok)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Dedykowany widok dla każdego rejestru | Lista wszystkich procesów typu "rejestr", kliknięcie otwiera listę spraw tego rejestru | ⏸️ Odroczona - wymaga szerszych prac nad UX |
| Zakładka "Raporty" w definicji procesu z domyślnym raportem | W definicji procesu typu rejestr automatyczny raport ze wszystkimi sprawami | ⏸️ Odroczona - wymaga szerszych prac nad modułem raportowym |
| Zakładka "Lista spraw" w definicji procesu | Jak zakładki "Szablony", "Formularze" - dodatkowa zakładka z listą spraw (z uwzględnieniem uprawnień) | ⏸️ Odroczona - wymaga zmian w architekturze definicji procesu |
| Rozszerzenie kontroli uprawnień | Rozszerzenie ustawienia "Kto może tworzyć sprawy" dla rejestrów (obecnie domyślnie tylko administratorzy) | ✅ Zastosowane - już istnieje mechanizm, brak zmian |
| Nie używać rejestrów, stosować "Źródła" | Alternatywa - używanie mechanizmu Źródeł zamiast rejestrów | ❌ Odrzucona - Źródła nie pokrywają wszystkich przypadków użycia rejestrów |

### Decyzja

**Status:** ⏸️ Odroczone

Zespół uznał, że rejestry wymagają gruntownego przeglądu i usprawnień, ale nie jest to priorytet (brak płacącego klienta, wszyscy wiedzą jak to działa). Propozycje usprawnień odroczone do przyszłości:

1. **Dedykowany widok dla rejestrów** - lista procesów typu rejestr z możliwością przejścia do listy spraw
2. **Automatyczne raporty** - domyślny raport w zakładce "Raporty" definicji procesu
3. **Walidacja unikalności klucza** przy tworzeniu nowych spraw (nie tylko przy synchronizacji)
4. **Wyraźne odróżnienie dezaktywacji od usuwania** (patrz temat 3)

Zespół potwierdził, że:
- Obecne rozwiązanie działa, choć nie jest idealne
- Komunikat błędu zostanie poprawiony (temat 3) - to rozwiąże najważniejszy problem
- Rejestry skracają czas wdrożeń mimo niedoskonałości
- Nie ma pilnej potrzeby inwestycji w ten obszar

**Szczegóły techniczne:**
- Mechanizm "Kto może tworzyć sprawy" już istnieje i działa (odwrotnie niż dla zwykłych spraw)
- Domyślnie: tylko administratorzy + osoby wymienione mogą tworzyć sprawy w rejestrze
- Dla zwykłych spraw: pusta lista = wszyscy mogą tworzyć
- Dla rejestrów: pusta lista = tylko administratorzy mogą tworzyć

### Zadania

- **Damian Kamiński:** Opisać przypadki użycia i propozycje usprawnień rejestrów dla przyszłego rozwoju (jeśli pojawi się klient z taką potrzebą)

### Punkty otwarte

- Czy inwestować w rozwój rejestrów, skoro istnieje alternatywa w postaci Źródeł?
- Jak zapewnić spójność między rejestrami a Źródłami? (czy to są dwa osobne mechanizmy czy powinny być zunifikowane?)

---

## 5. Integracja DocuSign z AMODIT - mechanizm envelope

### Kontekst i Problem

LOTU zgłosił potrzebę rozszerzenia integracji z DocuSign o mechanizm "envelope" (koperty). Obecna integracja działa w modelu "wyślij i zapomnij" - AMODIT wysyła dokument do DocuSign, tam jest podpisywany, AMODIT pobiera podpisany dokument. LOTU potrzebuje więcej kontroli nad procesem podpisywania - możliwości edycji dokumentu, dodawania/usuwania podpisujących, zmiany kolejności podpisów itp. po stronie DocuSign.

Pojawia się też dodatkowa potrzeba - wywołanie dowolnych endpointów DocuSign (nie tylko tych, które zaprogramowaliśmy). Problem: DocuSign wymaga OAuth (JWT), czego nie obsługuje obecny mechanizm CallRest w AMODIT.

### Zidentyfikowane Ryzyka

- Edycja danych po stronie DocuSign może prowadzić do niespójności danych z AMODIT
- Dawanie dostępu do tokenu OAuth w sprawie jest ryzykiem bezpieczeństwa
- Brak natywnej obsługi OAuth w CallRest ogranicza możliwości integracji z zewnętrznymi API

### Rozważane alternatywy

| Opcja                                               | Opis                                                                                       | Powód odrzucenia/wyboru                                                              |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Edycja envelope z poziomu AMODIT                    | Możliwość modyfikacji parametrów envelope bezpośrednio w AMODIT (np. zmiana podpisujących) | ❌ Odrzucona - prowadzi do niespójności danych, brak gwarancji synchronizacji         |
| Link do DocuSign + edycja tylko po stronie DocuSign | AMODIT tworzy envelope, generuje link, użytkownik przechodzi do DocuSign i tam edytuje     | ✅ Wybrana (MVP) - minimalizuje ryzyko niespójności, wykorzystuje natywne UI DocuSign |
| Funkcja GetToken + CallRest                         | Osobna funkcja do pozyskiwania tokenu OAuth, przechowywanie w zmiennej procesowej          | ❌ Odrzucona - ryzyko bezpieczeństwa, zła praktyka                                    |
| Natywna obsługa OAuth w CallRest                    | Rozszerzenie funkcji CallRest o mechanizm OAuth (logowanie, refresh token, cache)          | ✅ Wybrana - bezpieczne, elastyczne, wielokrotnego użytku                             |

### Decyzja

**Status:** ✅ Zatwierdzone (MVP)

Zespół zatwierdził rozwój integracji DocuSign w dwóch kierunkach:

**1. Mechanizm envelope (MVP):**
- **Tworzenie envelope** - AMODIT wysyła dokument do DocuSign z parametrami (podpisujący, kolejność, itp.)
- **Generowanie linku** - AMODIT generuje link do envelope w DocuSign
- **Edycja tylko po stronie DocuSign** - użytkownik klika link i przechodzi do DocuSign, gdzie może edytować parametry envelope (dodawać/usuwać podpisujących, zmieniać kolejność, itp.)
- **Pobranie podpisanego dokumentu** - mechanizm już istnieje

**WAŻNE:** AMODIT **nie będzie** synchronizował zmian dokonanych w DocuSign z powrotem do AMODIT. To świadoma decyzja - aby uniknąć niespójności danych. Użytkownik może dodać w DocuSign podpisującego, którego nie ma w AMODIT, zmienić kolejność podpisów itp. - te zmiany pozostają tylko po stronie DocuSign.

**2. Natywna obsługa OAuth w CallRest:**
Rozszerzenie funkcji CallRest o obsługę OAuth (w tym JWT):
- Automatyczne logowanie (pozyskanie tokenu)
- Automatyczny refresh tokenu (gdy wygaśnie)
- Cache tokenu (w bezpieczny sposób)
- Obsługa różnych schematów OAuth (nie tylko JWT)
- W przyszłości: także logowanie certyfikatem (dla MAUI - Microsoft blokuje login/hasło)

**Szczegóły techniczne:**
- Envelope - trzy stany: `create` (tworzenie), `edit` (edycja), `view` (podgląd)
- AMODIT obsługuje: `create` + generowanie linku do `edit`/`view`
- Edycja tylko po stronie DocuSign (brak synchronizacji z powrotem)
- OAuth będzie obsługiwany przez rozszerzony CallRest (w tym logowanie certyfikatem w przyszłości)
- Parametry OAuth przechowywane w konfiguracji integracji (nie w sprawie)

### Zadania

- **Łukasz Brocki:** Przygotować szczegółową specyfikację techniczną dla envelope (z uwzględnieniem ustaleń z Rady) - dokument dla zespołu deweloperskiego
- **Łukasz Brocki + Piotr Buczkowski + Adrian:** Zespołowo opracować koncepcję OAuth w CallRest - uwzględnić różne scenariusze (JWT, certyfikat, inne), zaplanować etapy implementacji
- **Łukasz Brocki:** Przygotować wycenę pracochłonności dla LOTU (envelope + OAuth)
- **Łukasz Brocki:** Skontaktować się z klientem (LOTU) w sprawie szczegółów wdrożenia envelope

### Punkty otwarte

- Czy logowanie certyfikatem jest wymagane już w pierwszej wersji OAuth? (prawdopodobnie nie - MVP to JWT)
- Gdzie przechowywać certyfikaty? (KeyVault - Adrian się zajmował, Piotr rozszerzy w ramach tej zmiany)
- Czy należy dodać mechanizm retry dla wywołań OAuth w przypadku błędów sieciowych?

---

## 6. Podpisywanie masowe dokumentów na raporcie - proces odbioru korespondencji

### Kontekst i Problem

LOTU zgłosił potrzebę masowego podpisywania dokumentów na liście spraw (raporcie) przy użyciu pola typu "podpis odręczny" (rysik na tablecie). Scenariusz biznesowy: kancelaria odbiera pisma analogowe (skanowane), osoba przychodzi po odbiór kilku pism jednocześnie, kancelaria przygotowuje listę na tablecie, osoba podpisuje się rysikiem, podpis rozprzestrzenia się na wszystkie sprawy z listy. Dodatkowa komplikacja: po pisma może przyjść osoba oddelegowana (np. sekretarka odbiera za dyrektora).

### Zidentyfikowane Ryzyka

- Rozbudowa modułu raportowego o funkcjonalność podpisywania masowego może być kosztowna
- Wypełnianie pól z poziomu raportu (bez otwierania sprawy) to nowa funkcjonalność, której nie mamy
- Podpisywanie "za kogoś" może być ryzykiem bezpieczeństwa i audytu

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Rozszerzenie modułu raportowego | Możliwość podpisania masowego bezpośrednio z poziomu raportu (bez otwierania spraw) | ❌ Odrzucona - wymaga szerokiej rozbudowy, brak kontekstu sprawy, długi czas realizacji |
| Dedykowany proces "Odbiór korespondencji" | Osobna sprawa typu "Odbiór", na której jest raport z listą korespondencji do odbioru, osoba podpisuje sprawę odbioru (nie każdą korespondencję z osobna) | ✅ Wybrana - wykorzystuje istniejące mechanizmy, możliwe do wdrożenia natychmiast |
| Masowa reguła przycisku "Podpis" | Wykorzystanie istniejącego mechanizmu masowych reguł przycisku | ❌ Odrzucona - nie rozwiązuje problemu "podpisywania za kogoś" i nie osadza podpisu odręcznego |

### Decyzja

**Status:** ✅ Zatwierdzone

Zespół zatwierdził rozwiązanie oparte na dedykowanym procesie "Odbiór korespondencji" (wzorowane na rozwiązaniu z Rossmanna):

**Proces:**
1. **Przygotowanie listy** - pracownik kancelarii tworzy sprawę typu "Odbiór korespondencji"
2. **Raport osadzony** - na sprawie odbioru jest osadzony raport z listą korespondencji oczekującej na odbiór osobisty
3. **Wybór korespondencji** - pracownik zaznacza checkboxami korespondencję, którą osoba odbiera
4. **Przeniesienie do sekcji podpisywania** - przycisk przenosi zaznaczoną korespondencję do pola typu "długi tekst" lub "tabela" na sprawie odbioru
5. **Wskazanie odbiorcy** - pracownik wypełnia dwa pola:
   - **Adresat rzeczywisty** - osoba, do której korespondencja jest adresowana (np. dyrektor)
   - **Odbiorca faktyczny** - osoba, która fizycznie odbiera (np. sekretarka) - domyślnie podpowiadana ta sama osoba co adresat
6. **Podpisanie** - pracownik podaje tablet osobie, osoba podpisuje się rysikiem na sprawie odbioru
7. **Zabezpieczenie podpisem** - pole z listą odebranej korespondencji jest zabezpieczone podpisem (niepodważalne)
8. **Automatyczne przepisanie** - reguła przycisku "Wydano" automatycznie przepisuje informację o odbiorze do każdej sprawy korespondencji (adnotacja: "Odebrano w ramach sprawy odbioru nr X przez osobę Y")

**Zalety rozwiązania:**
- Wykorzystuje istniejące mechanizmy AMODIT (raporty, pola, podpisy, reguły)
- Możliwe do wdrożenia natychmiast (bez zmian w kodzie)
- Niepodważalny dowód odbioru (podpis zabezpiecza listę korespondencji)
- Rozwiązuje problem "podpisywania za kogoś" (jawne wskazanie adresata i odbiorcy)

**Szczegóły techniczne:**
- Proces: "Odbiór korespondencji"
- Pola: Adresat rzeczywisty, Odbiorca faktyczny, Lista odebranej korespondencji (tabela lub długi tekst), Podpis (pole typu podpis)
- Raport osadzony: korespondencja oczekująca na odbiór osobisty (z checkboxami)
- Reguła przycisku: "Wydano" - masowo przepisuje informację o odbiorze do spraw korespondencji
- Pole "Odbiorca faktyczny" domyślnie podpowiadany jako ten sam co "Adresat rzeczywisty"

### Zadania

- **Łukasz Bott:** Przedstawić klientowi (LOTU) propozycję rozwiązania opartego na dedykowanym procesie "Odbiór korespondencji"
- **Łukasz Bott:** Jeśli klient zaakceptuje - przygotować projekt procesu "Odbiór korespondencji" (definicja, pola, raporty, reguły)

### Punkty otwarte

- Czy klient zaakceptuje rozwiązanie oparte na dedykowanym procesie? (czy oczekuje podpisywania masowego z poziomu raportu?)
- Czy należy dodać mechanizm archiwizacji spraw "Odbiór korespondencji" po zakończeniu?

---

## 7. Problem licencyjny KSeF Connector - zależność od REST API

### Kontekst i Problem

Adrian przeprojektował integrację KSeF Connector - zamiast Handlerów (stara technologia, niewspierana przez Microsoft) przeniósł komunikację na nowe endpointy oparte na standardowych mechanizmach REST API AMODIT. Decyzja miała charakter przyszłościowy (przygotowanie na migrację do .NET Core). Problem: teraz każdy klient kupujący KSeF Connector musi mieć w licencji REST API, co jest nieuzasadnione (to nasza wewnętrzna integracja, nie klient robi wywołania API).

### Zidentyfikowane Ryzyka

- Klient musi płacić za REST API, choć nie korzysta z niego bezpośrednio
- Decyzje techniczne Adrian często wprowadzają więcej zamieszania niż pożytku
- Brak kontroli architektury przy samodzielnej pracy Adriana prowadzi do problemów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| REST API za darmo dla klientów z KSeF Connector | Automatyczne włączenie REST API w licencji przy zakupie KSeF Connector | ❌ Odrzucona - nieuzasadnione, to nasza wewnętrzna integracja |
| Specjalny endpoint omijający licencję REST API | Dedykowany endpoint dla wewnętrznych integracji, niewymagający licencji REST API | ✅ Wybrana - rozwiązuje problem licencyjny, zachowuje nową architekturę |
| Powrót do Handlerów | Wycofanie zmian Adriana, powrót do starej architektury | ❌ Odrzucona - Handlery są przestarzałe, migracja w przyszłości będzie trudniejsza |

### Decyzja

**Status:** 🔍 Do weryfikacji

Zespół jednoznacznie odrzucił pomysł wymagania licencji REST API dla klientów kupujących KSeF Connector. To nasza wewnętrzna integracja, którą my robimy - klient nie powinien płacić za REST API w tym kontekście.

**Rozwiązanie:**
Adrian musi przygotować rozwiązanie techniczne, które omija sprawdzanie licencji REST API dla wewnętrznych integracji (KSeF Connector, potencjalnie innych). Możliwe podejścia:
- Specjalny endpoint dla integracji wewnętrznych
- Flaga "internal integration" omijająca sprawdzanie licencji
- Osobny mechanizm autoryzacji dla integracji wewnętrznych

**Uwaga od Janusza Bossaka:** Adrianowi nie wolno dawać takich tematów do robienia samodzielnie - zawsze wymyśla jakieś bazowe zmiany, które wprowadzają więcej zamieszania niż pożytku. Decyzje techniczne muszą być konsultowane z zespołem architektów przed implementacją.

**Szczegóły techniczne:**
- Obecna implementacja: KSeF Connector wywołuje standardowe endpointy REST API AMODIT
- Problem: sprawdzanie licencji REST API blokuje połączenie
- Wymagane: mechanizm omijający sprawdzanie licencji dla wewnętrznych integracji
- Przyszłościowo: to samo rozwiązanie może być użyte dla innych integracji wewnętrznych

### Zadania

- **Damian Kamiński:** Przeprowadzić rozmowę z Adrianem - przedstawić problem i wymagania zespołu architektów
- **Adrian:** Przygotować propozycję rozwiązania technicznego omijającego sprawdzanie licencji REST API dla wewnętrznych integracji
- **Damian Kamiński + Janusz Bossak:** Wciągnąć Adriana na design (za godzinę lub najbliższe spotkanie) - przedyskutować i zatwierdzić rozwiązanie
- **Piotr Buczkowski + Adrian:** Wspólnie przeanalizować możliwe podejścia (special endpoint, flaga, osobny mechanizm autoryzacji)

### Punkty otwarte

- Jak zapewnić, że przyszłe decyzje architektoniczne Adriana będą konsultowane z zespołem przed implementacją?
- Czy podobny problem może dotyczyć innych integracji wewnętrznych? (np. przyszłe migracje)
- Kiedy planowana jest migracja na .NET Core? (czy to uzasadnia decyzję o rezygnacji z Handlerów już teraz?)

---

## 8. Problem wyświetlania pola "Podpis" - nierówne kafelki

### Kontekst i Problem

Podczas testowania funkcjonalności podpisywania na sprawie (w kontekście tematu 6) zauważono problem wizualny - pole typu "podpis" ma nierówny obwódkę w stosunku do innych pól. Problem występuje gdy w profilu użytkownika AMODIT ustawiony jest "Mały rozmiar formularza". W "Dużym rozmiarze formularza" problem nie występuje.

### Zidentyfikowane Ryzyka

- Problem dotyczy nierównego wyświetlania kontrolek przy "Małym rozmiarze formularza"
- Może dotyczyć nie tylko pola "podpis", ale też innych kontrolek

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja

**Status:** ✅ Zatwierdzone

Problem zidentyfikowany i potwierdzony - pole typu "podpis" wyświetla się nieprawidłowo (nierówna obwódka, nieproporcjonalny kwadracik) przy ustawieniu "Mały rozmiar formularza" w profilu użytkownika. W "Dużym rozmiarze formularza" problem nie występuje.

**Szczegóły techniczne:**
- Problem występuje tylko przy "Małym rozmiarze formularza"
- Dotyczy pola typu "podpis"
- Obwódka jest nierówna, kwadracik nieproporcjonalny
- Problem może być związany z ustawieniem skalowania Windows (125% vs 100%)

### Zadania

- **Anna Skupińska:** Zgłosić błąd - nierówne wyświetlanie pola "podpis" przy małym rozmiarze formularza

### Punkty otwarte

Brak

## Powiązane projekty
- [[cross-cutting/Zarzadzanie-licencjami]]
- [[Moduly/Proces-rejestr]]
- [[Moduly/CallRest]]
- [[klienci/Neuca/DocuSign]]
- [[Klienci/LOT]]
- [[Integracje/Integracja-KSeF]]
- [[cross-cutting/Interfejs-sprawy/Formularz-sprawy]]
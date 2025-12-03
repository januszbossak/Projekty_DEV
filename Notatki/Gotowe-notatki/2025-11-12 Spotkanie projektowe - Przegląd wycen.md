# Notatka projektowa – 2025-11-12 – Przegląd wycen

**Data:** 2025-11-12
**Temat główny:** Przegląd wycen

**Powiązane projekty:**
- `moduly/Modul-raportowy` – funkcjonalność 1
- `cross-cutting/Zakladka-Procesy` – funkcjonalność 2
- `cross-cutting/GTA` – funkcjonalność 3
- `moduly/Edytor-procesow-formularzy` – funkcjonalności 4, 7
- `backlog` – funkcjonalności 5, 8
- `klienci/WIM/Komunikator` – funkcjonalność 6

---

## 1. Problem z źródłami opartymi na bazie Oracle w nowych raportach

**Projekt:** `moduly/Modul-raportowy`
**Komponent:** Moduł raportowy

### Cel i problem

Mateusz zgłasza problem z źródłami opartymi na bazie Oracle – pyta, czy źródła online w ogóle nie będą działały w nowych raportach. Przetestowano i źródło online działa, ale być może to specyfika bazy Oracle. Problem może być z przetestowaniem tego. W logach nie ma zapytania SQL-owego. Sądząc po treści, to jest jakieś konkretne zapytanie do konkretnych tabel w konkretnej bazie. Błąd: `INVALID_CHARACTER`. Na końcu zapytania jest `LIMIT ?` – możliwe, że przekazujemy jakiś parametr, którego nie powinniśmy, albo brakuje wartości jakiegoś parametru. Sterownik ODBC przekazuje znak zapytania do silnika Oracle'a, a ten go nie rozumie. Stare raporty działają, więc problem jest specyficzny dla nowych raportów.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Problem z Oracle jako takim | Specyfika bazy Oracle powoduje problemy | ❌ Odrzucona – nie jest to problem z Oracle jako takim, tylko niepoprawnie budujemy zapytanie |
| Problem z `LIMIT ?` | Składnia MySQL-owa zamiast Oracle | 🔍 Do weryfikacji – `LIMIT ?` to składnia MySQL-owa, powinna tam pójść konkretna liczba |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Ktoś z deweloperów musi na to spojrzeć. Można zasugerować, żeby włączyć logowanie zapytań SQL i porównać zapytanie, jakie leci ze starego raportu, a jakie z nowego. Może to jest tylko ten `LIMIT`, który powinien być jakimś parametrem liczbowym. Trzeba skontaktować się z Mateuszem, żeby jakoś tę sesję z ludźmi od Rossmanna sprawdzić.

**Szczegóły techniczne:**
- Błąd: `INVALID_CHARACTER`
- Problem: `LIMIT ?` na końcu zapytania (składnia MySQL-owa)
- Sterownik ODBC odpowiada za połączenie, ale nie za tłumaczenie składni – musimy zadać pytanie w języku Oracle'owym
- Nie mamy wszystkich przypadków biznesowych po stronie testów – Oracle był dowożony przez ostatnie lata, poprawiane były drobnostki, żeby był kompatybilny dla prostych zapytań

### Punkty otwarte

- Czy problem jest tylko z `LIMIT ?`, czy są inne różnice między zapytaniami ze starych i nowych raportów?
- Jak dokładnie powinno wyglądać zapytanie dla Oracle (zamiast `LIMIT ?`)?

---

## 2. Permanentne przechowywanie wartości w lupce do wyszukiwania procesów

**Projekt:** `cross-cutting/Zakladka-Procesy`
**Komponent:** Zakładka Procesy

### Cel i problem

Zgłoszenie z Neuca: jak przefiltrujemy listę procesów czy raportów, to ten filtr zostaje na stałe, nawet po wylogowaniu. W Neuca jest logowanie przez AD, więc nie ma typowego wylogowania. Problem powoduje niewygodę użytkowników.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Czyszczenie filtra po wylogowaniu | Filtr czyści się przy wylogowaniu i zalogowaniu | ✅ Wybrana – podstawowe rozwiązanie |
| Czyszczenie filtra po zamknięciu całego okna przeglądarki | Filtr trzymany do końca sesji | ✅ Wybrana – dodatkowe rozwiązanie |
| Szeroka poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach | Paczka wartości dotycząca raportów, procesów itd. | 💡 Propozycja – do rozważenia w przyszłości |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Trzeba rozpisać, które momenty czyszczą filtr: na pewno wylogowanie i zalogowanie, oraz zamknięcie całego okna przeglądarki (nie zakładki). Mamy parametr związany z czasem trwania sesji, więc można to trzymać do końca sesji. To nie jest hotfix – nie wywala danych, nie ma błędów, powoduje tylko niewygodę. Może być w następnym wydaniu. Można by się zastanowić szerzej i zrobić z tego paczkę wartości, np. "poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach", która dotyczyłaby raportów, procesów itd.

**Szczegóły techniczne:**
- Parametr związany z czasem trwania sesji
- Moment czyszczenia: wylogowanie, zalogowanie, zamknięcie całego okna przeglądarki

### Ograniczenia / Poza zakresem

- Nie jest to hotfix – może być w następnym wydaniu
- Na razie tylko podstawowe rozwiązanie (czyszczenie przy wylogowaniu/zalogowaniu i zamknięciu przeglądarki)

### Punkty otwarte

- Czy zrobić szerszą paczkę wartości "poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach"?
- Jakie inne tematy w tym zakresie można przypiąć do tego zadania?

---

## 3. Wyświetlanie linku w mailu o dostępie tymczasowym

**Projekt:** `cross-cutting/GTA`
**Komponent:** Grant Temporary Access

### Cel i problem

Bartek zgłosił, że zrobił trik z dodaniem `div`-a w `before` i `after`, i wtedy link formatuje się dobrze i jest widoczny we wszystkich klientach poczty. Piotr sugerował, żeby to dodać na stałe.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Jeśli Piotr to widział i zatwierdził, to nie ma uwag. Trzeba przepisać, jak ma być zrobione. Pozostaje pytanie, na ilu skrzynkach to testować: Gmail, Outlook stacjonarny, i z polskich serwisów Wirtualna Polska i Onet.

**Szczegóły techniczne:**
- Rozwiązanie: dodanie `div`-a w `before` i `after`
- Skrzynki do testowania: Gmail, Outlook stacjonarny, Wirtualna Polska, Onet

### Punkty otwarte

- Czy rozwiązanie działa na wszystkich wymienionych skrzynkach?

---

## 4. Funkcja `setFieldInfo` a pola wymagane

**Projekt:** `moduly/Edytor-procesow-formularzy`
**Komponent:** Edytor Reguł

### Cel i problem

W wersji czerwcowej, jeśli pole jest wymagane, komunikat z `setFieldInfo` się nie wyświetla. W wersji marcowej działało to poprawnie. To pewnie efekt ukrywania "pole jest wymagane" – za mocno to ukryli.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

To pewnie Kamil, Mariusz albo Ania, kto opiekował się ukrywaniem "pole jest wymagane". Za mocno to ukryli. Kamil ma to przypisane. Zmienić ewentualnie klasyfikację, bo nie wiem, czy to hotfix. Nie ma utraty danych.

**Szczegóły techniczne:**
- Funkcja: `setFieldInfo`
- Problem: komunikat nie wyświetla się, gdy pole jest wymagane (wersja czerwcowa)
- Wcześniej działało poprawnie (wersja marcowa)

### Punkty otwarte

- Czy to hotfix, czy może być w następnym wydaniu?
- Kto dokładnie opiekował się ukrywaniem "pole jest wymagane"?

---

## 5. Wyszukiwarka w backlogu – fullscreen i przewijanie

**Projekt:** `backlog`
**Komponent:** Backlog

### Cel i problem

Zgłoszenie od Daniela: wyszukiwarka w backlogu otwiera się na fullscreenie, a lista przewija do góry. To jest do poprawy.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

To jest do poprawy. Nie określono priorytetu ani terminu.

**Szczegóły techniczne:**
- Problem: wyszukiwarka otwiera się na fullscreenie
- Problem: lista przewija do góry przy otwieraniu wyszukiwarki

### Punkty otwarte

- Jaki jest priorytet tego zadania?
- Jak powinno działać poprawnie?

---

## 6. Błędy w komunikatorze

**Projekt:** `klienci/WIM/Komunikator`
**Komponent:** Komunikator

### Cel i problem

Mateusz ma błędy w komunikatorze do poprawy, żeby dowieźć go do końca. Przykład: wysłana wiadomość nie pojawia się od razu. To musi zrobić w tym sprincie.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Mateusz musi poprawić błędy w komunikatorze w tym sprincie, żeby dowieźć go do końca. Przykład: wysłana wiadomość nie pojawia się od razu.

**Szczegóły techniczne:**
- Problem: wysłana wiadomość nie pojawia się od razu
- Inne błędy do poprawy (nie wymienione szczegółowo)

### Punkty otwarte

- Jakie są wszystkie błędy do poprawy?
- Kiedy dokładnie komunikator ma być dowieziony?

---

## 7. Problem z `setRadioValue` – wyczyszczeniem wartości w radio buttonach

**Projekt:** `moduly/Edytor-procesow-formularzy`
**Komponent:** Edytor Reguł

### Cel i problem

Jest problem z wyczyszczeniem wartości w radio buttonach w regule automatycznej. Zawsze tak było. W zwykłej liście wyboru da się wyczyścić, w radio buttonach nie. Obejściem było dodanie "pustej" opcji typu "--". To niespójność w zachowaniu systemu.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dodanie "pustej" opcji typu "--" | Obejście problemu | ⏸️ Odroczona – obecne obejście |
| Naprawa funkcji `setRadioValue` | Umożliwienie wyczyszczenia wartości w radio buttonach | 🔍 Do weryfikacji – zostawione do zrobienia |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

Niespójność. Zostawiamy to do zrobienia. Obecnie można używać obejścia z "pustą" opcją typu "--".

**Szczegóły techniczne:**
- Funkcja: `setRadioValue`
- Problem: nie można wyczyścić wartości w radio buttonach w regule automatycznej
- W zwykłej liście wyboru da się wyczyścić
- Obejście: dodanie "pustej" opcji typu "--"

### Punkty otwarte

- Kiedy to naprawić?
- Czy to powinno być w paczce z innymi poprawkami niespójności?

---

## 8. Właściciel na poziomie feature'a i epica

**Projekt:** `backlog`
**Komponent:** Organizacja pracy

### Cel i problem

Kwestia właściciela na poziomie feature'a i epica. Zazwyczaj Kamil był właścicielem, bo deweloperzy nie zaglądali na ten poziom, a statusy zostawały. Jak wszystkie PBI-e były zrealizowane, zamykał feature. Pytanie: czy tak robimy dalej?

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Delivery manager jako właściciel (obecne podejście) | Kamil zamyka feature po zrealizowaniu wszystkich PBI | ✅ Zatwierdzone – obecnie |
| Deweloper jako właściciel (docelowe podejście) | Deweloper domyka feature po dowiezieniu w całości | 💡 Propozycja – docelowo |
| Praca na branchach per paczka | Branch na paczkę, wszystkie PBI na ten branch, merge gdy paczka gotowa | 💡 Propozycja – do rozważenia |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja

Przy nowej nomenklaturze to deweloper powinien domykać feature. Jego zadaniem na sprint jest "zrób ten feature", a w ramach tego są 3 PBI. On je robi i mówi "dowoiozłem feature w całości". Delivery managerowie powinni decydować na poziomie paczki (prezentu), czyli zbioru feature'ów. Problemem jest to, że pojedyncze PBI-e idą do wersji, a nie całe paczki. Powinniśmy pracować na branchach per paczka. Jak robimy jakąś funkcjonalność, to otwieramy branch na tę paczkę. Wszystkie PBI do tego wchodzą na ten branch. Dopiero jak paczka jest gotowa, cały branch jest mergowany. To by uprościło pracę. Poniekąd tak robimy, bo są lokalne branche, na których możemy testować, a wydajemy w całości, gdy jest gotowe. Branż lokalny jest taką paczką wartości. Chodzi o to, żeby był nakierowany na jedną rzecz.

**Szczegóły techniczne:**
- Obecnie: delivery manager (Kamil) zamyka feature po zrealizowaniu wszystkich PBI
- Docelowo: deweloper domyka feature po dowiezieniu w całości
- Propozycja: praca na branchach per paczka (branch na paczkę, wszystkie PBI na ten branch, merge gdy paczka gotowa)

### Punkty otwarte

- Kiedy przejść na model z deweloperem jako właścicielem feature'a?
- Jak dokładnie zaimplementować pracę na branchach per paczka?
- Czy to uprości pracę, czy doda złożoności?

---

## Propozycja podziału na pakiety prac (MVP)

Nie dyskutowano priorytetyzacji na MVP.

---

## Punkty do dalszej dyskusji (globalne)

- Szeroka poprawa zachowania systemu przy wybranych filtrach i wyszukiwaniach (raporty, procesy itd.) – czy zrobić z tego paczkę wartości?
- Praca na branchach per paczka – jak dokładnie to zaimplementować?
- Przejście na model z deweloperem jako właścicielem feature'a – kiedy i jak?


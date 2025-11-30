# Rada Architektów – 2025-10-07

**Powiązane projekty:**
- `cross-cutting/Wielospolkowosc` – temat 1
- `moduly/Modul-raportowy` – temat 2
- `moduly/Ustawienia-systemowe` – temat 3
- `cross-cutting/Logowanie-powiadomien` – temat 4
- `moduly/Edytor-procesow-formularzy` – tematy 5, 6

---

## 1. Wielospółkowość – ograniczenie widoczności użytkowników

**Projekt:** `cross-cutting/Wielospolkowosc`

### Kontekst i Problem

W środowisku LOT na jednej instancji AMODIT pracują różne spółki (PGL i LOT, być może więcej później). Mateusz zgłosił potrzebę ograniczenia widoczności użytkowników w panelu współwłaścicieli/obserwatorów spraw, aby nie można było przypadkowo dodać osoby z innej spółki. Problem dotyczy sytuacji, gdzie w ramach jednego procesu (lub różnych procesów dla różnych spółek) użytkownik z jednej spółki mógłby dodać współwłaściciela lub obserwatora z innej spółki.

Zgłoszenie jest profilaktyczne – analiza LOT jeszcze się nie rozpoczęła (planowana po 20 października), więc nie jest to jeszcze rzeczywiste wymaganie, ale raczej prewencja przed potencjalnym problemem.

### Zidentyfikowane Ryzyka

- Brak separacji użytkowników między spółkami w ramach jednej instancji
- Możliwość przypadkowego lub celowego udostępnienia sprawy osobie z innej spółki
- Problem dotyczy nie tylko panelu współwłaścicieli/obserwatorów, ale także pól typu Użytkownik, akcji "Przekaż do", widoczności w panelu administracyjnym, raportów
- Podobne wyzwanie może pojawić się w Orlenie (wiele spółek, Centrum Usług Korporacyjnych widzi wszystko)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ograniczenie na poziomie procesu do wybranej grupy | Dodanie możliwości ograniczenia listy dostępnych współwłaścicieli/obserwatorów do wybranej grupy w ramach procesu | ⏸️ Odroczona – zbyt wąskie podejście, nie rozwiązuje problemu globalnie |
| Rozbudowa SetUserFilter o filtrowanie po strukturze | Dodanie możliwości wskazania głównego węzła struktury organizacyjnej i filtrowania (tylko ten węzeł lub węzeł i węzły w dół) | ⏸️ Odroczona – dotyczy tylko konkretnego ekranu/pola, nie rozwiązuje problemu globalnie |
| Nowa funkcja SetControlFilter/SetCFilter | Funkcja wpływająca na panele w sprawie (współwłaściciele, obserwatorzy) | ⏸️ Odroczona – rozwiązuje tylko jeden przypadek użycia |
| Kompleksowe rozwiązanie wielospółkowości | Wprowadzenie w strukturze organizacyjnej możliwości oznaczenia, który poziom definiuje "spółkę", automatyczne filtrowanie list użytkowników na podstawie przynależności do tej samej jednostki | 💡 Propozycja – wymaga głębszej analizy i zaprojektowania spójnego mechanizmu |
| Wyciągnięcie uprawnień do formularza jako komponent | Pole typu Component "Uprawnienia" na formularzu zamiast prawego panelu, z możliwością filtrowania i wymagalności | ⏸️ Odroczona – wymaga przebudowy backendu, może być rozważone później |

### Decyzja

**Status:** ⏸️ Odroczone

Temat jest zbyt szeroki na doraźne rozwiązanie. Wymaga głębszej analizy i zaprojektowania spójnego mechanizmu wielospółkowości, który obejmie wszystkie miejsca w systemie gdzie wybierany jest użytkownik (panele współwłaścicieli/obserwatorów, pola typu Użytkownik, akcja "Przekaż do", widoczność w panelu administracyjnym, raporty, struktura organizacyjna).

**Szczegóły techniczne:**
- Problem dotyczy wszystkich miejsc gdzie wybierany jest użytkownik
- W strukturze organizacyjnej spółki są zwykle na drugim poziomie (pierwszy poziom to "Struktura organizacyjna", drugi to spółki)
- Możliwe rozwiązanie: oznaczenie poziomu struktury jako "spółka" (np. przez flagę na węźle Departament)
- Użytkownik powinien mieć przypisaną przynależność do spółki (np. dodatkowe pole Company lub określenie na podstawie struktury)
- Filtrowanie powinno działać dynamicznie w zależności od kontekstu sprawy (np. tylko osoby ze spółki wnioskodawcy CreatedBy)

**Uwaga:** Zgłoszenie Mateusza jest profilaktyczne, nie wynika z rzeczywistych wymagań klienta (analiza LOT jeszcze się nie rozpoczęła). Temat został przeniesiony do backlogu pod Epic LOT-owy, aby nie zginął, ale nie będzie realizowany dopóki nie pojawią się konkretne i szczegółowe wymagania.

### Zadania

- **Łukasz Bott:** Temat przypisany do backlogu pod Epic LOT-owy, do ponownej analizy gdy pojawią się konkretne wymagania

### Punkty otwarte

- Jak zdefiniować przynależność użytkownika do spółki? (dodatkowe pole Company vs określenie na podstawie struktury organizacyjnej)
- Czy spółka powinna być zawsze na drugim poziomie struktury, czy powinno być możliwe oznaczenie dowolnego poziomu jako "spółka"?
- Jak obsłużyć przypadki gdzie Centrum Usług Korporacyjnych (CUK) widzi wszystko, ale pozostali użytkownicy mają ograniczoną pulę?
- Czy rozwiązanie powinno działać na poziomie ustawień systemowych (globalnie) czy per proces?
- Czy wyciągnięcie uprawnień do formularza jako komponent (pole typu Component) powinno być pierwszym krokiem przed filtrowaniem?

---

## 2. Filtr "W miesiącu" – ukrycie wyboru roku

**Projekt:** `moduly/Modul-raportowy`

### Kontekst i Problem

W filtrze "W miesiącu" wyświetla się kontrolka z wyborem roku (numer roku i strzałki do zmiany), co jest mylące dla użytkowników. Operator "w miesiącu" działa niezależnie od roku (np. "w miesiącu sierpień" oznacza sierpień w dowolnym roku), więc wyświetlanie kontrolki roku sugeruje, że filtr uwzględnia rok, podczas gdy faktycznie go ignoruje.

Operator "w miesiącu" zawsze działał tak samo (wskazanie dowolnego dnia z danego miesiąca oznaczało ten miesiąc w tym roku), ale zmiana interfejsu na kontrolkę kalendarzową z widocznym rokiem wprowadza mylący element.

### Zidentyfikowane Ryzyka

- Mylący interfejs – użytkownicy mogą oczekiwać, że filtr działa dla konkretnego miesiąca w konkretnym roku
- Brak możliwości porównania lat (np. sierpień 2024 vs sierpień 2025) bez użycia dodatkowych filtrów

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Ukrycie belki z rokiem w kontrolce | Ukrycie całej belki z rokiem (numer roku i strzałki) przy użyciu CSS | ✅ Wybrana – najprostsze rozwiązanie, usuwa mylący element |
| Zmiana kontrolki na listę dropdown | Zmiana kontrolki kalendarzowej na listę wyboru z 12 pozycjami (styczeń–grudzień) | ❌ Odrzucona – nie jest na tyle istotne, aby wprowadzać większe zmiany |
| Dodanie nowego operatora "w miesiącu i roku" | Dodanie nowego operatora który uwzględnia zarówno miesiąc jak i rok, z pełną kontrolką kalendarzową | ❌ Odrzucona – można zbudować to za pomocą dwóch osobnych filtrów (w miesiącu + w roku), nie jest na tyle istotne |

### Decyzja

**Status:** ✅ Zatwierdzone

Ukrycie całej belki z rokiem (numer roku i strzałki) w kontrolce filtru "w miesiącu" przy użyciu CSS. Operator "w miesiącu" pozostaje bez zmian – działa niezależnie od roku. Jeśli użytkownik chce filtrować po konkretnym miesiącu w konkretnym roku, może użyć dwóch osobnych filtrów (w miesiącu + w roku) lub zbudować grupę filtrów.

**Szczegóły techniczne:**
- Kontrolka pochodzi z Ant Design (nie DevExtreme)
- Ukrycie belki z rokiem możliwe przez CSS
- Operator "w miesiącu" pozostaje bez zmian funkcjonalnych
- Dla porównania lat można użyć dwóch osobnych filtrów lub grupy filtrów

### Zadania

- **Anna Skupińska:** Ukrycie belki z rokiem w kontrolce filtru "w miesiącu" (maksymalnie 2 jednostki roboty, jeśli ktoś się zna to 1 jednostka)
- **Anna Skupińska:** Przetestowanie wszystkich raportów (również tych używających DevExtreme) po wprowadzeniu zmiany
- **Damian Kamiński:** Utworzenie zgłoszenia do testów (wskazanie testera i wersji do wgrywania)

### Punkty otwarte

- [Brak]

---

## 3. Grupowanie parametrów integracji

**Projekt:** `moduly/Ustawienia-systemowe`

### Kontekst i Problem

Adrian wprowadził zmiany w wyświetlaniu i grupowaniu parametrów integracji w nowym module ustawień systemowych. Zmiany dotyczą sposobu wyświetlania nazw integracji i grup parametrów. Pytanie dotyczy spójności wyświetlania między starym a nowym widokiem oraz obsługi przypadków, gdzie ktoś nie zrobił tego dobrze (np. nazwa parametru nie jest zgodna z nazwą integracji).

### Zidentyfikowane Ryzyka

- Niespójność wyświetlania między starym a nowym widokiem
- Problemy z migracją istniejących integracji, gdzie nazwa parametru może nie być zgodna z nazwą integracji
- Brak gwarancji, że nazwa integracji będzie spójna z nazwą grupy

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Zachowanie obecnego rozwiązania | Nowa tabela dedykowana do wyświetlania zasobów, nazwa integracji wyświetlana po lewej, nazwa grupy po prawej na górze | ✅ Wybrana – rozwiązanie jest spójne z tym co omówiono, mechanizm pozostaje bez zmian |

### Decyzja

**Status:** ✅ Zatwierdzone

Rozwiązanie wprowadzone przez Adriana jest poprawne i spójne z omówionymi wcześniej założeniami. Nowa tabela dedykowana do wyświetlania zasobów wyświetla nazwę integracji po lewej stronie, a nazwę grupy po prawej na górze. Mechanizm pozostaje bez zmian – zmiany dotyczą tylko wyświetlania.

Dla istniejących starych integracji, gdzie nie było nazwy integracji jako takiej, nazwa grupy została przekopiowana jako nazwa integracji (uspójnienie). Jeśli ktoś nie zrobił tego dobrze w starym widoku (np. nazwa parametru nie jest zgodna z nazwą integracji), to w nowym widoku też będzie niespójne, ale nie da się tego obejść.

**Szczegóły techniczne:**
- Nowa tabela dedykowana do wyświetlania zasobów (nie zmienia mechanizmu działania)
- Nazwa integracji wyświetlana po lewej stronie
- Nazwa grupy wyświetlana po prawej na górze
- Dla starych integracji nazwa grupy została przekopiowana jako nazwa integracji

### Zadania

- **Adrian Kotowski:** Wydanie zmian na developera (już zrobione, wrzucone na developera)
- **Adrian Kotowski:** Wskazanie testera i wersji do wgrywania (na strefowe, gdzie są realne przypadki które są źle grupowane)
- **Damian Kamiński:** Utworzenie zgłoszenia do testów

### Punkty otwarte

- [Brak]

---

## 4. Logowanie maili wychodzących – rozróżnienie dodania do kolejki vs wysłania

**Projekt:** `cross-cutting/Logowanie-powiadomien`

### Kontekst i Problem

Obecnie logowanie maili wychodzących następuje w momencie dodania do kolejki wychodzącej, a nie w momencie faktycznego wysłania. To powoduje problemy:
- Jeśli ktoś usunie mail z kolejki, mamy fałszywą informację że mail został wysłany (ale to jest świadome działanie administratora)
- Jeśli job się zatrzyma i nie wysyła maili, i tak będzie zapisane że wysłaliśmy (to jest nasza wina, błąd aplikacji)
- Dla maili zbiorczych problem jest jeszcze bardziej złożony (zbiorczy w tabeli Notification vs rozdzielony w CaseUserAction)

### Zidentyfikowane Ryzyka

- Fałszywa informacja o wysłaniu maila (gdy mail został tylko dodany do kolejki, ale nie wysłany)
- Brak możliwości rozróżnienia między "zaplanowane do wysłania" a "faktycznie wysłane"
- Problem z mailami zbiorczymi (różne reprezentacje w różnych tabelach)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Logowanie tylko w momencie faktycznego wysłania | Logowanie tylko gdy mail został faktycznie wysłany (serwer pocztowy nie zwrócił błędu) | ❌ Odrzucona – problem dla maili zbiorczych, brak informacji o zaplanowanych mailach |
| Logowanie tylko w momencie dodania do kolejki | Obecne rozwiązanie | ❌ Odrzucona – powoduje fałszywe informacje o wysłaniu |
| Dwa zdarzenia: "Dodano do kolejki" i "Wysłano" | Logowanie w momencie dodania do kolejki ze statusem "zaplanowane", aktualizacja statusu na "wysłane" po faktycznym wysłaniu | ✅ Wybrana – rozwiązuje problem rozróżnienia między zaplanowanym a wysłanym |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie dwóch statusów dla logowania maili wychodzących:
1. **"Zaplanowane do wysłania"** (lub "Dodano do kolejki") – logowanie w momencie dodania do kolejki wychodzącej
2. **"Wysłane"** – aktualizacja statusu po faktycznym wysłaniu (gdy serwer pocztowy nie zwrócił błędu)

Dodatkowo wprowadzenie kolumny z datą/czasem faktycznego wysłania.

**Szczegóły techniczne:**
- Logowanie w momencie dodania do kolejki ze statusem "zaplanowane"
- Aktualizacja statusu na "wysłane" po faktycznym wysłaniu (gdy serwer pocztowy nie zwrócił błędu)
- Dodanie kolumny z datą/czasem faktycznego wysłania
- Dla maili zbiorczych: w tabeli Notification będzie zbiorczy, w CaseUserAction będzie rozdzielony (to jest różnica, nie duplikat)

**Uwaga:** Kamil sugerował rozważenie zmiany zachowania tabeli Notification, aby nie usuwała wpisów po wysłaniu, tylko zmieniała status. To zostało odrzucone ze względu na wydajność (job co 5 minut musiałby przeszukiwać setki tysięcy wpisów po roku użytkowania).

### Zadania

- **Piotr Buczkowski:** Implementacja dwóch statusów dla logowania maili wychodzących (zaplanowane/wysłane) oraz kolumny z datą/czasem faktycznego wysłania

### Punkty otwarte

- [Brak]

---

## 5. Zmiana typu pola – dyskusja o dodatkowych zabezpieczeniach

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Adrian w komentarzach do zadania dotyczącego zmiany typu pola zasugerował dodatkowe zabezpieczenia – pozwalanie na zmianę typu tylko jeśli zmieniamy na ten sam typ (np. numeryczne na kwotę) i nie ryzykujemy utraty danych. Obecne rozwiązanie wymaga zaznaczenia checkboxa "zdaję sobie sprawę z ryzyka" przy każdej zmianie typu pola, nawet jeśli zmieniamy na ten sam typ.

### Zidentyfikowane Ryzyka

- Obecne rozwiązanie może być zbyt restrykcyjne (wymaga potwierdzenia nawet przy zmianie na ten sam typ)
- Brak walidacji czy w polu są dane przed wymaganiem potwierdzenia

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Pozwalanie na zmianę tylko jeśli zmieniamy na ten sam typ | Zmiana typu bez potwierdzenia tylko jeśli zmieniamy na ten sam typ (np. numeryczne na kwotę) | ❌ Odrzucona – zbyt skomplikowane, nie jest na tyle istotne |
| Walidacja czy w polu są dane przed wymaganiem potwierdzenia | Sprawdzenie czy w sprawach to pole jest wypełnione przed wymaganiem potwierdzenia | ⏸️ Odroczona – może być rozważone rozwojowo, ale obecne rozwiązanie jest wystarczające |
| Zachowanie obecnego rozwiązania | Obecne rozwiązanie z checkboxem "zdaję sobie sprawę z ryzyka" przy każdej zmianie typu | ✅ Wybrana – jest bardzo bezpieczne, funkcjonalność wykorzystywana głównie na etapie wdrożenia gdy nie ma danych produkcyjnych |

### Decyzja

**Status:** ✅ Zatwierdzone

Zachowanie obecnego rozwiązania z checkboxem "zdaję sobie sprawę z ryzyka" przy każdej zmianie typu pola. Rozwiązanie jest bardzo bezpieczne i wystarczające. Funkcjonalność jest wykorzystywana głównie na etapie wdrożenia, gdy nie ma jeszcze danych produkcyjnych. Na produkcji konsultanci powinni wiedzieć, że właściwą praktyką jest ukrycie pola i dodanie nowego z nowym typem, a nie zmiana typu istniejącego pola.

Walidacja czy w polu są dane przed wymaganiem potwierdzenia może być rozważona rozwojowo, ale obecne rozwiązanie jest wystarczające i niższy priorytet.

**Szczegóły techniczne:**
- Obecne rozwiązanie wymaga zaznaczenia checkboxa przy każdej zmianie typu pola
- Funkcjonalność wykorzystywana głównie na etapie wdrożenia
- Na produkcji właściwą praktyką jest ukrycie pola i dodanie nowego z nowym typem

### Zadania

- [Brak – funkcjonalność już zaimplementowana]

### Punkty otwarte

- [Brak]

---

## 6. Walidacja pola z maską (Telefon) – błąd wyświetlania i wymuszanie zgodności

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Kontekst i Problem

Piotr wykrył błąd w wyświetlaniu informacji o niezgodności wartości z maską w polu typu telefon. Błąd wynika z nieprawidłowego użycia zmiennej w funkcji SendFieldInfo (błąd składniowy powodujący wyświetlenie błędów w konsoli Visual Studio). Po poprawieniu błędu, pole wyświetla się na czerwono gdy wartość jest niezgodna z maską, ale reguła się wykonuje (to jest tylko ostrzeżenie, nie blokada).

Problem: konsultanci spodziewają się, że czerwone pole oznacza blokadę (jak w polu walidowanym), podczas gdy obecnie maska tylko informuje o niezgodności, ale pozwala zapisać i przejść dalej. Dodatkowo, maska nie waliduje długości (tylko rodzaj znaków), więc można wpisać 4 cyfry, 5 cyfr, 10 cyfr i wszystko będzie poprawne, o ile znaki są zgodne z maską.

### Zidentyfikowane Ryzyka

- Mylący interfejs – czerwone pole sugeruje blokadę, podczas gdy maska tylko informuje
- Brak możliwości wymuszenia zgodności z maską (obecnie maska tylko podpowiada, nie waliduje)
- Możliwość wprowadzenia nieprawidłowych znaków (np. dwukropek) przez kopiowanie z innych źródeł
- Brak spójności między polami walidowanymi a polami tekstowymi z maską (konsultanci nie wiedzą kiedy użyć którego)

### Rozważane alternatywy

| Opcja | Opis | Powód odrzucenia/wyboru |
|-------|------|------------------------|
| Poprawka tylko błędu wyświetlania | Poprawka błędu składniowego w SendFieldInfo, zachowanie obecnego zachowania (tylko ostrzeżenie) | ❌ Odrzucona – nie rozwiązuje problemu mylącego interfejsu |
| Zmiana koloru ostrzeżenia | Zmiana koloru z czerwonego na pomarańczowy/żółty dla ostrzeżenia niezgodności z maską | ❌ Odrzucona – nie rozwiązuje problemu wymuszania zgodności |
| Dodanie opcji "Wymuś zgodność z maską" | Dodanie flagi do pola tekstowego "Wymuś zgodność z maską" – jeśli zaznaczone, pole zachowuje się jak pole walidowane (blokuje zapis i przejście dalej jeśli niezgodne) | ✅ Wybrana – rozwiązuje problem wymuszania zgodności, zachowuje elastyczność |
| Ujednolicenie pól walidowanych i tekstowych z maską | Docelowo pola walidowane powinny zostać zlikwidowane, funkcjonalność przeniesiona na pola tekstowe z maską i walidacją | 💡 Propozycja – długoterminowy kierunek, wymaga dalszej analizy |

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie nowej opcji do pola tekstowego "Wymuś zgodność z maską" (lub "Wymuś stosowanie maski", "Sprawdź zgodność z maską"). Jeśli opcja jest zaznaczona i pole jest wypełnione, pole zachowuje się jak pole walidowane:
- Jeśli wartość jest niezgodna z maską → błąd (czerwone pole), nie można zapisać, nie można przejść dalej
- Jeśli wartość jest zgodna z maską → pole poprawne

Jeśli opcja nie jest zaznaczona, maska działa jak obecnie (tylko informuje o niezgodności, ale pozwala zapisać i przejść dalej).

**Szczegóły techniczne:**
- Nowa opcja dostępna dla wszystkich masek (nie tylko telefon)
- Maska waliduje tylko rodzaj znaków (cyfry, spacja, myślnik), nie długość
- Dla maski telefonu: dopuszczalne znaki to cyfry, spacja i myślnik (plus na początku jest częścią maski)
- Dla maski NIP: jeśli opcja "Wymuś zgodność z maską" jest zaznaczona, powinna również wyliczać sumę kontrolną (jak w polu walidowanym)
- Docelowo pola walidowane powinny zostać zlikwidowane, funkcjonalność przeniesiona na pola tekstowe z maską i walidacją

**Uwaga:** Piotr wykrył błąd składniowy w funkcji SendFieldInfo (nieprawidłowe użycie zmiennej). Błąd musi zostać poprawiony niezależnie od wprowadzenia opcji "Wymuś zgodność z maską".

### Zadania

- **Anna Skupińska:** Poprawka błędu składniowego w funkcji SendFieldInfo (zadanie przypisane: 22192)
- **Kamil Dubaniowski:** Projektowanie i implementacja opcji "Wymuś zgodność z maską" dla pól tekstowych z maską (zadanie przeniesione do backlogu, status: In Design)
- **Kamil Dubaniowski:** Przetestowanie opcji dla wszystkich masek i ewentualne poprawki

### Punkty otwarte

- Jak obsłużyć sytuację, gdy ktoś włączy opcję "Wymuś zgodność z maską" po 5 latach użytkowania i sprawy zaczną sypać błędami? (podobny problem jak przy zmianie walidacji na polu walidowanym)
- Czy dla maski NIP opcja "Wymuś zgodność z maską" powinna również wyliczać sumę kontrolną? (tak, jak w polu walidowanym)
- Czy opcja powinna być dostępna dla wszystkich masek od razu, czy tylko dla telefonu na początku? (decyzja: dla wszystkich, ale trzeba przetestować każdą maskę)
- Jak ujednolicić pola walidowane i tekstowe z maską, aby konsultanci wiedzieli kiedy użyć którego? (długoterminowy kierunek, wymaga dalszej analizy)


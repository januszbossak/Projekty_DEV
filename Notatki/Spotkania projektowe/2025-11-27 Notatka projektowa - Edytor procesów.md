# Notatka projektowa – 2025-11-27 – Edytor procesów

**Data:** 2025-11-27
**Temat główny:** Edytor procesów – rozwój edytora graficznego i listy pól

---

## 1. Dodawanie sekcji pomiędzy sekcjami w edytorze graficznym

**Komponent:** Edytor Formularza

### Cel i problem

Dotychczas aby dodać nową sekcję w formularzu, użytkownik musiał przewinąć na sam dół edytora. To było niewygodne, szczególnie przy dużych formularzach. Celem jest umożliwienie dodawania sekcji bezpośrednio w miejscu, gdzie jest potrzebna.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zaimplementowano funkcjonalność dodawania sekcji pomiędzy istniejącymi sekcjami. Przycisk pojawia się na hover między sekcjami. Schemat zachowania: element nie jest widoczny domyślnie, pojawia się dopiero po najechaniu kursorem - wymaga wiedzy użytkownika o jego istnieniu.

**Szczegóły techniczne:**
- Przycisk "Dodaj sekcję" pojawia się na hover między sekcjami
- Analogicznie działa "Dodaj wiersz" w sekcjach
- Przyciski mają tego samego koloru obecnie

### Punkty otwarte

- Rozważyć zmianę kolorystyki przycisków "Dodaj sekcję" vs "Dodaj wiersz", aby wizualnie odróżnić akcje (obecnie są tego samego koloru, co może być mylące)
- Opcje: oderwać kolorystykę od systemowej i użyć zielonego dla dodawania, lub zachować spójność z motywem kolorystycznym użytkownika

---

## 2. Ujednolicenie wyglądu i stylowania sekcji

**Komponent:** Edytor Formularza

### Cel i problem

Zapewnienie spójności wizualnej między edytorem graficznym a rzeczywistym wyglądem formularzy. Wcześniej były niespójności w zaokrągleniach rogów, marginesach i layoutach.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Wprowadzono następujące zmiany:
- Zaokrąglenia rogów sekcji: ujednolicono na 5px (wcześniej stosowano różne wartości: 3px na formularzu, 8px w innych miejscach)
- Zaokrąglone rogi sekcji stosowane są już w edytorze graficznym (5px)
- Na formularzu rzeczywistym pozostaje tymczasowo 3px (nie ma planów przerabiania rzeczywistego formularza w tym momencie)
- Zmieniono układ prawego panelu - teraz jest osobnym boksem (podobnie jak na liście pól), zamiast elementu na całej wysokości strony
- Nagłówek sekcji zawiera ikonę nawiązującą do typu pola (zamiast samej nazwy typu pola)

**Szczegóły techniczne:**
- Wspólny komponent dla ustawień pola w edytorze graficznym i edytorze listy
- Prawy panel jako box (nie rozciągnięty na całą wysokość)
- Ikona typu pola w nagłówku sekcji

### Punkty otwarte

- Marginesy prawego panelu są większe niż marginesy listy pól (lista pól jest bardziej przyklejona do góry i boków) - ustalić czy to zamierzone, czy do wyrównania
- Po zwinięciu prawego panelu margines jest większy - rozważyć dostosowanie do poziomu po zwinięciu

---

## 3. Poprawa użyteczności przycisków nawigacyjnych i powiększenia

**Komponent:** Edytor Formularza

### Cel i problem

Wcześniej przycisk "Powiększ/Zmniejsz" zmieniał swoją pozycję po otwarciu prawego panelu (przesuwał się w lewo), co było nieintuicyjne. Użytkownik spodziewał się, że przycisk pozostanie w tym samym miejscu.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zmieniono zachowanie tak, aby przycisk "Powiększ/Zmniejsz" pozostawał w tym samym miejscu nawet po otwarciu prawego panelu. Prawy panel nie przesuwa już innych elementów nawigacyjnych.

**Szczegóły techniczne:**
- Przycisk powiększenia/pomniejszenia nie zmienia pozycji przy otwarciu prawego panelu
- Prawy panel jako box nie wpływa na pozycję innych elementów interfejsu

---

## 4. Rozszerzenie wyszukiwania pól o atrybuty techniczne

**Komponent:** Edytor Formularza

### Cel i problem

W celach serwisowych i debugowania, potrzebne jest wyszukiwanie pól nie tylko po nazwie, ale również po identyfikatorach technicznych (ID pola, nazwa kolumny, GUID).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Dodano opcję wyszukiwania po atrybutach technicznych:
- ID pola
- Nazwa kolumny w bazie danych
- GUID pola (nowo dodane w tym sprincie)

Opcja domyślnie wyłączona, można ją włączyć w ustawieniach wyszukiwania. Po włączeniu, wpisanie np. "54e" (część GUID-u) podpowie pole i automatycznie otworzy jego ustawienia.

**Szczegóły techniczne:**
- Wyszukiwanie po: ID pola, nazwa kolumny, GUID
- Opcja włączana w ustawieniach (domyślnie wyłączona)
- Po wyborze z podpowiedzi automatyczne przekierowanie do ustawień pola

### Punkty otwarte

- Piotr wnioskował o możliwość edycji GUID-a w modalu edycji pola - nie rozpisano jeszcze zadania, do uzupełnienia

---

## 5. Kompatybilność edytora reguł tabeli

**Komponent:** Edytor Reguł

### Cel i problem

Zapewnienie możliwości edycji reguł dla pól typu tabela w nowym interfejsie, zachowując kompatybilność wsteczną.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ⏸️ Odroczone (docelowe rozwiązanie), ✅ Zatwierdzone (kompatybilność wsteczna)

Na razie nie projektowano docelowego rozwiązania dla edytora reguł tabeli. Zaimplementowano zapewnienie kompatybilności wstecznej - dodano przycisk umożliwiający edycję reguł tabeli w starym interfejsie. Przycisk otwiera jeszcze stare okno edycji reguł.

**Szczegóły techniczne:**
- Przycisk "Edytuj reguły tabeli" dostępny w kontekście tabeli
- Otwiera stary interfejs edycji reguł

### Ograniczenia / Poza zakresem

Docelowe, nowe rozwiązanie dla edytora reguł tabeli nie jest planowane w tym momencie.

---

## 6. Sposób wyboru liczby kolumn w sekcji

**Komponent:** Edytor Formularza

### Cel i problem

Zapewnienie spójności między edytorem graficznym a edytorem listy w sposobie wyboru liczby kolumn w sekcji. Wcześniej w edytorze listy była dropdown lista, podczas gdy w edytorze graficznym stosowano inny mechanizm.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zmieniono sposób wyboru liczby kolumn w edytorze listy, aby był spójny z edytorem graficznym. Teraz stosuje się ten sam mechanizm wyboru (prawdopodobnie slider lub przyciski +/-) zamiast dropdown listy.

**Szczegóły techniczne:**
- Wspólny mechanizm wyboru liczby kolumn dla edytora graficznego i listy

---

## 7. Search (wyszukiwanie) jako wspólny komponent

**Komponent:** Edytor Formularza

### Cel i problem

Zapewnienie spójności wyszukiwania we wszystkich widokach edytora (graficzny, lista).

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (w edytorze graficznym), ⏸️ Oczekuje na wdrożenie (u Filipa w edytorze listy)

Dodano komponent wyszukiwania (search) jako wspólny element dla edytora graficznego i listy. W edytorze graficznym już wdrożony. U Filipa (edytor listy) jeszcze nie ma tej wersji, bo nie było oficjalnego wydania paczki.

**Szczegóły techniczne:**
- Wspólny komponent search dla edytora graficznego i listy
- Rozszerzony o wyszukiwanie po atrybutach technicznych (patrz punkt 4)

---

## 8. Dodawanie pól i sekcji w edytorze listy

**Komponent:** Edytor Formularza

### Cel i problem

Zapewnienie funkcjonalności dodawania pól i sekcji bezpośrednio z edytora listy, analogicznie do edytora graficznego.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (zadanie rozpisane dla Filipa)

Rozpisano zadanie dla Filipa na dodanie funkcjonalności dodawania pól i sekcji w edytorze listy, zgodnie z projektami przygotowanymi wcześniej.

**Szczegóły techniczne:**
- Funkcjonalność dodawania pól i sekcji z poziomu edytora listy
- Zgodnie z wcześniej przygotowanym projektem

---

## 9. Wizualne oznaczenie pól klikalnych (ramka na hover)

**Komponent:** Edytor Formularza

### Cel i problem

Wcześniej nie było jasne, które pola w edytorze są klikalne i prowadzą do edycji. Brak wizualnej sugestii powodował, że użytkownicy nie wiedzieli, że mogą kliknąć w pole, aby otworzyć jego ustawienia.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Dodano ramkę wokół pola na hover, sugerującą możliwość kliknięcia i edycji. Ramka pojawia się przy wszystkich polach, które mają możliwość edycji wartości domyślnej lub innych ustawień.

**Szczegóły techniczne:**
- Ramka na hover wokół pola klikalnego
- Dotyczy wszystkich pól, gdzie można ustawić wartość domyślną lub inne parametry

### Punkty otwarte

- Dla pól bez wartości domyślnej (np. pole Odnośnik, Słownik podrzędny) ramka się nie pokazuje - może być mylące dla użytkownika (może pomyśleć, że to błąd)
- Rozważano:
  - **Opcja A (Piotr):** Usunąć kolumnę "Wartość domyślna" dla pól, które jej nie mają
  - **Opcja B (Kamil):** Pokazać kolumnę tylko do odczytu z informacją "Brak dostępnej wartości domyślnej dla tego typu pola"
- Kwestia wymaga dalszej dyskusji i ustalenia rozwiązania

---

## 10. Dodatkowe kolumny w edytorze listy (opcjonalne)

**Komponent:** Edytor Formularza

### Cel i problem

W edytorze listy pól użytkownicy potrzebują czasami dostępu do dodatkowych informacji o polach (np. tłumaczenia, dodatkowe atrybuty), ale domyślnie nie są one potrzebne i zajmują miejsce.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (zadanie zgłoszone Filipowi, prawdopodobnie już weszło)

Dodano możliwość wyświetlania dodatkowych kolumn w edytorze listy pól. Kolumny są domyślnie wyłączone, ale użytkownik może je włączyć w ustawieniach widoku. To rzadko używane informacje, więc domyślne ukrycie zwiększa czytelność.

**Szczegóły techniczne:**
- Dodatkowe kolumny domyślnie wyłączone
- Możliwość włączenia w ustawieniach widoku
- Przykładowe kolumny: tłumaczenia, dodatkowe atrybuty pól

### Punkty otwarte

- Filip zgłosił, że nie ma animacji wyświetlenia dodatkowych kolumn (pojawiają się agresywnie) - planowane dodanie animacji
- Filip kombinował z kolumnami i coś zaproponował, ale jeszcze nie działa

---

## 11. Dodanie ikon dla zwiększenia czytelności

**Komponent:** Edytor Formularza

### Cel i problem

Zwiększenie czytelności i intuicyjności interfejsu edytora listy poprzez dodanie ikon.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Dodano ikony w edytorze listy pól, aby zwiększyć czytelność i ułatwić rozpoznawanie typów pól i akcji.

**Szczegóły techniczne:**
- Ikony dla typów pól
- Ikony dla akcji (np. usuwanie, edycja)

---

## 12. Zmiana nawigacji w tabeli - rezygnacja z zagnieżdżenia (wycofanie z koncepcji)

**Komponent:** Edytor Formularza

### Cel i problem

Obecna koncepcja rozwijania tabeli bezpośrednio na widoku listy (pokazywanie pól tabeli jako zagnieżdżonych elementów) okazała się problematyczna przy dużych zagnieżdżeniach. Użytkownicy gubili się w strukturze, nie było jasne co jest tabelą, co sekcją, a co polem.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A - Rozwijanie tabeli na widoku listy | Tabela rozwija się bezpośrednio, pokazując pola wewnętrzne jako zagnieżdżone elementy | ❌ Odrzucona - problemy z czytelnością przy dużych zagnieżdżeniach, mylące dla użytkowników |
| Opcja B - Powrót do starej nawigacji (strzałka w prawo) | Tabela nie rozwija się, tylko kliknięcie strzałki wchodzi do wnętrza tabeli (zmiana kontekstu) | ✅ Wybrana - lepsza czytelność, intuicyjna nawigacja, sprawdzone rozwiązanie |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (powrót do starej koncepcji)

Zespół decyduje się wycofać z koncepcji rozwijania tabeli na widoku listy. Powrócą do starego rozwiązania:
- Pole tabela wyświetlane jest jako pojedyncze pole (bez rozwiniętych pól wewnętrznych)
- Aby wejść do pól tabeli, użytkownik klika strzałkę w prawo (nawigacja)
- Nastąpi zmiana kontekstu - załaduje się widok z polami tylko tej tabeli

To rozwiązanie jest analogiczne do edytora graficznego, gdzie kliknięcie w pole tabela na formularzu umożliwia wejście do środka i edycję pól wewnętrznych.

**Szczegóły techniczne:**
- Tabela jako pojedyncze pole na liście
- Strzałka w prawo dla nawigacji do wnętrza tabeli
- Zmiana kontekstu (ładowanie widoku z polami tabeli)

### Ograniczenia / Poza zakresem

Koncepcja rozwijania pozostanie w widoku "Matryca uprawnień", gdzie zagnieżdżenia mają sens - uprawnienia są zależne od hierarchii (tabela dziedziczy uprawnienia z formularza). W tym kontekście zagnieżdżenie jest potrzebne do pokazania zależności.

### Punkty otwarte

- Zadanie na przyszły sprint - nie rozpoczęto jeszcze implementacji

---

## 13. Problem z prezentacją vs nawigacją w widoku formularza

**Komponent:** Edytor Formularza

### Cel i problem

W widoku formularza (środkowy panel) występuje niespójność w zachowaniu kliknięcia na pole:
- W trybie "Tabela" (lista pól): kliknięcie otwiera prawy panel z ustawieniami pola
- W trybie "Widok formularza" (prezentacja): kliknięcie pola typu tabela/podformularz wchodzi do środka (nawigacja)

To powoduje zamieszanie - użytkownik nie wie, czy kliknięcie otworzy ustawienia, czy zmieni kontekst.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A - Środkowy panel = Tylko prezentacja | Kliknięcie zawsze otwiera prawy panel (ustawienia pola), nawigacja tylko przez lewy panel lub dedykowany przycisk "Edytuj pola formularza" | 💡 Propozycja Kamila - spójność, jeden cel dla środkowego panelu |
| Opcja B - Środkowy panel = Prezentacja + Nawigacja | Kliknięcie w pole tabela/podformularz wchodzi do środka, otwiera ustawienia i zmienia kontekst jednocześnie | ❌ Obecny stan - niespójne, mylące |
| Opcja C - Kliknięcie = Oba działania | Kliknięcie otwiera prawy panel i wchodzi do środka jednocześnie | ❌ Odrzucona przez Janusza - użytkownik spodziewałby się jednego działania, nie dwóch |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji (wymaga dalszej dyskusji)

Kamil proponuje rozwiązanie: środkowy panel to wyłącznie prezentacja efektu, nie nawigacja. Kliknięcie w pole (również tabelę/podformularz) otwiera prawy panel z ustawieniami tego pola. Nawigacja do wnętrza tabeli/podformularza odbywa się przez:
- Lewy panel nawigacyjny (drzewo struktury)
- Dedykowany przycisk w prawym panelu "Edytuj pola formularza" (dla podformularzy/tabel)

Przemek wstrzymał implementację tej zmiany, bo wymaga dalszej dyskusji.

**Szczegóły techniczne:**
- Środkowy panel = wyłącznie prezentacja (wizualizacja formularza)
- Nawigacja = lewy panel (drzewo) lub przycisk w prawym panelu
- Kliknięcie w pole (w tym tabelę/podformularz) = otwarcie prawego panelu z ustawieniami

### Punkty otwarte

- Kamil zaproponuje projekt w Figmie do dalszej dyskusji
- Kwestia wymaga decyzji: czy środkowy panel ma być wyłącznie prezentacją, czy też nawigacją w przypadku tabel/podformularzy
- Konkluzja z dyskusji z czatem: należy rozgraniczyć prezentację od nawigacji - albo jedno, albo drugie, nie oba jednocześnie

---

## 14. Zamykanie prawego panelu przy zmianie kontekstu (wejście do tabeli/podformularza)

**Komponent:** Edytor Formularza

### Cel i problem

Przy wejściu do tabeli/podformularza (zmiana kontekstu), prawy panel z ustawieniami pola z poprzedniego kontekstu pozostaje otwarty. To powoduje błędy - użytkownik jest już w tabeli, ale widzi ustawienia pola z formularza głównego.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja (Kamil planuje zaimplementować)

Kamil proponuje automatyczne zamykanie prawego panelu przy wejściu do nowego kontekstu (np. z formularza głównego do tabeli). Uzasadnienie: wchodząc do tabeli, prawy panel powinien pokazywać pola dostępne w tabeli, a nie pola z formularza głównego.

**Szczegóły techniczne:**
- Automatyczne zamykanie prawego panelu przy zmianie kontekstu (np. formularz główny → tabela)
- Przy wejściu do tabeli prawy panel jest zamknięty, użytkownik wybiera pole z nowego kontekstu

### Punkty otwarte

- Kamil planuje to zaimplementować, ale chce to zrobić "bez konsultacji" (trochę) jako oczywistą poprawę UX

---

## 15. Widok "Formularz" w lewym panelu dla podformularzy

**Komponent:** Edytor Formularza

### Cel i problem

W widoku "Formularz" (wybór w lewym panelu), gdy tabela jest ustawiona jako podformularz, wyświetla się ona w środkowym panelu jako element wizualizacji. Pytanie: czy kliknięcie w ten element powinno wchodzić do środka tabeli, czy tylko otwierać prawy panel z ustawieniami?

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A - Kliknięcie = wejście do środka + prawy panel | Obecnie stosowane - kliknięcie w podformularz w widoku "Formularz" wchodzi do środka i otwiera prawy panel | ❌ Niespójne (patrz punkt 13) |
| Opcja B - Kliknięcie = tylko prawy panel | Kliknięcie otwiera tylko prawy panel z ustawieniami, wejście do środka przez lewy panel lub dedykowany przycisk | 💡 Propozycja Kamila - spójność z resztą interfejsu |
| Opcja C - Element nieklikalny | Podformularz w widoku "Formularz" jest tylko wizualizacją, nieklikalną | ❌ Odrzucona - użytkownik może chcieć edytować ustawienia |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji (powiązane z punktem 13)

Kamil proponuje, aby element w widoku "Formularz" (podformularz/tabela) był klikalny, ale efektem kliknięcia było tylko otwarcie prawego panelu z ustawieniami, nie wejście do środka. Wejście do środka odbywa się przez:
- Lewy panel (drzewo struktury)
- Dedykowany przycisk w prawym panelu "Edytuj pola formularza"

Opcja ta jest powiązana z punktem 13 (prezentacja vs nawigacja).

**Szczegóły techniczne:**
- Widok "Formularz" w lewym panelu = prezentacja, nie nawigacja
- Kliknięcie w podformularz/tabelę = prawy panel z ustawieniami
- Hover z podświetleniem (analogicznie do menu) - pozostawić takie jak w menu (bez specjalnego podświetlenia pomarańczowego)

### Punkty otwarte

- Decyzja powiązana z punktem 13 - wymaga ustalenia ogólnej zasady prezentacja vs nawigacja
- Hover dla elementu - Przemek zasugerował, żeby hover był taki jak w menu (bez dodatkowego podświetlenia pomarańczowego)

---

## 16. Zmiana nawigacji lewego panelu - drzewo zamiast pełnej ścieżki

**Komponent:** Edytor Formularza

### Cel i problem

Wcześniej lewy panel nawigacyjny pokazywał pełną ścieżkę jako tekst (np. "Formularz główny > Tabela 1 > Tabela 2"), co przy dużych zagnieżdżeniach było bardzo długie i mało czytelne.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zmieniono nawigację lewego panelu na strukturę drzewa. Zamiast pełnej ścieżki tekstowej, pokazywane są elementy jako drzewo z wcięciami, wizualnie sugerującymi hierarchię (rodzic-dziecko).

**Szczegóły techniczne:**
- Struktura drzewa z wcięciami
- Domyślnie wszystkie elementy rozwinięte
- Tabele pierwszego poziomu widoczne jako dzieci formularza głównego
- Podformularze (w trybie "widok formularza") na równi z formularzem głównym (nie zagnieżdżone)

### Punkty otwarte

- Decyzja Janusza (podana wcześniej Przemkowi): gdy tabela jest w widoku "podformularz", powinna być na równi z formularzem głównym (nie zagnieżdżona wizualnie), ale gdy jest tabelą (elementem formularza), powinna być zagnieżdżona jako dziecko
- To rozwiązanie skraca wizualizację i zwiększa czytelność

---

## 17. Problem z breadcrumbami (nawigacja "okruszkowa") w edytorze

**Komponent:** Edytor Formularza

### Cel i problem

Po wprowadzeniu nawigacji drzewem (treeselect) w lewym panelu, zniknęły breadcrumbs (strzałki) pokazujące pełną ścieżkę. Użytkownik nie widzi już pełnej ścieżki nawigacji (np. "Formularz główny > Tabela 1 > Pole X"), co utrudnia orientację w zagnieżdżeniach.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Opcja A - Breadcrumbs u góry (na poziomie "Procesy") | Rozbudować istniejący breadcrumb u góry o kolejne poziomy zagnieżdżeń | ❌ Odrzucona przez Janusza - ten breadcrumb służy do czegoś innego (nawigacja globalna), nie powinien być używany do nawigacji w edytorze |
| Opcja B - Breadcrumbs na poziomie edytora (nad formularzem) | Dodać osobny breadcrumb na poziomie edytora, pokazujący ścieżkę nawigacji w ramach edytora (formularz > tabela > pole) | 💡 Propozycja Janusza - lepsze miejsce |
| Opcja C - Treeselect (dropdown) jako wybór, breadcrumbs jako wartość | Treeselect służy do wyboru elementu, ale wybrana wartość wyświetla się jako breadcrumbs ze strzałkami | 💡 Propozycja Przemka - łączy obie funkcje |
| Opcja D - Tylko treeselect, bez breadcrumbs | Obecny stan - brak breadcrumbs, tylko treeselect | ❌ Problem z orientacją w zagnieżdżeniach |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji (wymaga dalszej dyskusji)

Zespół zgadza się, że brak breadcrumbs to problem (użytkownik nie widzi pełnej ścieżki). Janusz zasugerował, że breadcrumb na poziomie edytora (nad formularzem) byłby lepszy niż u góry. Przemek zaproponował rozwiązanie hybrydowe: treeselect do wyboru, breadcrumbs do wyświetlania wartości.

Kamil zauważa, że breadcrumbs miałyby ograniczenie: przy dużych zagnieżdżeniach rozciągają się w nieskończoność. Rozważana opcja: pokazywać pierwszy i ostatni poziom (np. "Formularz główny > ... > Tabela 5").

**Szczegóły techniczne:**
- Breadcrumb na poziomie edytora formularza (nie u góry strony)
- Możliwość kliknięcia w elementy breadcrumb (nawigacja szybka)
- Treeselect pozwala szybko przejść do dowolnego poziomu (rozwija się i pokazuje wszystkie opcje)

### Punkty otwarte

- Kamil postara się zaprojektować to w Figmie i przedstawić zespołowi do decyzji
- Konkluzja: rozgraniczyć prezentację (pokazanie ścieżki) od nawigacji (zmiana poziomu) - breadcrumbs = prezentacja, treeselect = nawigacja

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Poprawa użyteczności i spójności

**Cel:** Ujednolicenie interfejsu, poprawa użyteczności, spójność między widokami
**Zakres:** Funkcjonalności 1, 2, 3, 6, 7, 8, 11, 16
**Status:** Większość zrealizowana lub w trakcie

### MVP 2: Rozszerzenia funkcjonalne

**Cel:** Nowe funkcjonalności dla zaawansowanych użytkowników i celów serwisowych
**Zakres:** Funkcjonalności 4, 10
**Status:** Zrealizowane lub w trakcie wdrożenia (Filip)

### MVP 3: Przeprojektowanie nawigacji i kontekstu

**Cel:** Rozwiązanie problemów z nawigacją, prezentacją vs nawigacją, breadcrumbs
**Zakres:** Funkcjonalności 12, 13, 14, 15, 17
**Status:** Wymaga dyskusji i projektowania (Kamil w Figmie)

### MVP 4: Poprawki detali i edge cases

**Cel:** Dopracowanie szczegółów interfejsu
**Zakres:** Funkcjonalności 5, 9
**Status:** Częściowo zrealizowane, niektóre punkty otwarte

---

## Punkty do dalszej dyskusji (globalne)

- **Kolory przycisków dodawania (sekcja vs wiersz)** - ustalić czy zmienić kolorystykę dla lepszego odróżnienia akcji
- **Wartość domyślna dla pól, które jej nie mają** - ustalić czy usunąć kolumnę, czy pokazać jako "Brak dostępnej" (decyzja Piotr vs Kamil)
- **Prezentacja vs Nawigacja** - globalna decyzja: czy środkowy panel to prezentacja (tylko podgląd), czy nawigacja (kliknięcie wchodzi do środka)? Kamil przygotuje projekt w Figmie
- **Breadcrumbs** - gdzie umieścić breadcrumbs (nawigacja "okruszkowa") i jak zintegrować z treeselect
- **Edycja GUID-a** - Piotr wnioskował o możliwość edycji GUID-a w modalu edycji pola (zadanie do rozpisania)
- **Animacja wyświetlania kolumn** - Filip pracuje nad animacją dla dodatkowych kolumn w edytorze listy
- **Zmiana nawigacji w tabeli (rezygnacja z zagnieżdżeń)** - zadanie na przyszły sprint, do rozpoczęcia implementacji

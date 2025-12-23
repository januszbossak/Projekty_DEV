**Damian Kamiński:** Skoro jesteśmy przy tabelach, pokażę wam praktyczne użycie AMODIT przez jednego z wdrożeniowców. Wymyślił coś, co wszystkim się spodobało: przyciski osadzone wewnątrz tabeli. Są to przyciski procesu, ale dodał do nich funkcjonalność w JavaScript, która przy kliknięciu podmienia CaseID sprawy na ID z danego wiersza. Przycisk wykonuje się tylko dla tego konkretnego wiersza.

**Anna Skupińska:** Czyli podmienia CaseID sprawy w locie?

**Damian Kamiński:** Tak. Pytanie, czy nie możemy tego zaopiekować lepiej globalnie.

**Piotr Buczkowski:** Przecież to od dawna jest w planach do zrobienia. Wpisuje CaseID wybranej sprawy w polu, a potem w regule procesu odczytuje to ID.

**Janusz Bossak:** Musimy to zrobić porządnie. To element, który bardzo przyspiesza wdrożenia.

**Damian Kamiński:** Konsekwencja "sztuczki" Tomasza jest taka, że historia zmian jest niespójna. Pokazuje modyfikację wszystkich wierszy, mimo że faktycznie zmienił się tylko jeden. Musimy to obsłużyć natywnie. Tomasz dodał JavaScript, który odczytuje kontekst i przypisuje CaseID do FieldValue.

**Janusz Bossak:** Trzeba to zaopiekować systemowo. Absolutnie zabronić takich "rzeźb" w JS i CSS, bo to psuje serwis i utrzymanie. Przy aktualizacji systemu takie wdrożenie po prostu przestanie działać i będą pretensje do nas.

**Damian Kamiński:** Dlatego to poruszam. Chcemy to wprowadzić oficjalnie.

**Janusz Bossak:** Tomek niech tego nie rozpowszechnia. Musimy wprowadzić reguły w tabeli, które można uruchomić na pojedynczym wierszu. Kolejny stopień wtajemniczenia to przyciski w osadzonych raportach – tam klienci też chcą wybiórczo zatwierdzać lub odrzucać pozycje bez konieczności zaznaczania checkboxów i klikania wspólnego przycisku na górze.

**Damian Kamiński:** Zacznijmy od tabel.

**Piotr Buczkowski:** Zrobienie tego, aby reguła ręczna umieszczona w polu typu przyciski wewnątrz tabeli miała kontekst tego wiersza, to drobiazg. Zaraz mogę to zrobić.

**Łukasz Bott:** Ale gdzie definiujesz tę regułę? Na poziomie procesu?

**Piotr Buczkowski:** Tak, na poziomie procesu. Domyślnie reguła ręczna ma kontekst głównej sprawy, ale jeśli umieścimy ją w polu wewnątrz tabeli, otrzyma kontekst wiersza. Odwołanie do nazwy pola w nawiasach kwadratowych będzie dotyczyć pola w tym wierszu.

**Damian Kamiński:** Postuluję jednak, aby to był wyraźnie oznaczony nowy typ: "reguła ręczna tabeli" (V2). Dzięki temu będziemy mogli użyć walidatora AI, który sprawdzi czy reguła jest poprawna w tym kontekście (np. zabroni użycia `foreach row` na samej sobie). To zapewni lepszą kompatybilność wsteczną, gdy wprowadzimy nowe listy reguł przefiltrowane po kontekstach.

**Janusz Bossak:** Reguły tabeli powinny być regułami tabeli. Konsultant musi od razu wiedzieć, że tworzy coś dla wiersza, aby nie odwoływał się niepotrzebnie do danych z formularza głównego, chyba że przez jawne połączenie.

**Kamil Dubaniowski:** Czasami trzeba sięgnąć do danych z formularza głównego (np. do wybranego działu), więc taka możliwość musi zostać.

**Damian Kamiński:** Trzeba im tłuc do głowy: to działa na wierszu, nie na całej tabeli.

**Kamil Dubaniowski:** Taka reguła powinna mieć parametr pozwalający na uruchomienie masowe (poprzez zaznaczenie wierszy checkboxami i kliknięcie przycisku na belce tabeli). Klienci będą tego potrzebować do masowej akceptacji kosztów.

**Janusz Bossak:** Muszę uciekać do Przemka. To szerszy temat. Młodsi wdrożeniowcy często nie wiedzą, której funkcji w jakim typie reguły użyć.

**Damian Kamiński:** I tu przyda się AI, które będzie podpowiadać lub zapalać "lampki" ostrzegawcze przy niestandardowym użyciu funkcji.

Podsumowując na teraz: robimy nowy typ lub znacznik dla reguł tabeli, aby odróżnić je od reguł formularza.

**Łukasz Bott:** Trzeba jutro na spotkaniu o 15:00 uczulić konsultantów, żeby nie robili takich "sztuczek" na własną rękę, tylko konsultowali potrzeby z nami.

**Damian Kamiński:** Nie dawałbym bury Tomkowi, bo wykazał się kreatywnością i pokazał nam realną potrzebę. Ale fakt, wersja oficjalna musi być poprawna. Przedstawię to jutro na spotkaniu i zapytam o ich opinie.

**Piotr Buczkowski:** Moje rozwiązanie z przekazaniem CaseID z pola przycisk jest szybkie do wdrożenia.

**Damian Kamiński:** Tomasz jest na urlopie do końca roku, więc to nie jest żaden hotfix. Przegadamy to z konsultantami i zajmiemy się tym na spokojnie w przyszłym tygodniu lub między świętami. Wtedy będzie więcej przestrzeni.

Bardziej pilny jest ten temat XML, o którym mówiliśmy wcześniej, bo klient wchodzi już na testy.

Dziękuję za spotkanie. Słyszymy się po świętach.

**Anna Skupińska:** Cześć.

**Damian Kamiński:** Cześć.

zatrzymano transkrypcję

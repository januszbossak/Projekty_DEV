**Data spotkania:** 2 grudnia 2025, 09:00 - część 2

---

**Janusz Bossak:** To są dwa tematy, ale wymagałyby Piotra. Jeden to powraca temat pobierania danych hurtowo z raportu. To jest temat, który Przemek wpisał na Radę. Zbieranie danych za pomocą protokołu Open Data. Jest jakiś klient, już nie pamiętam nazwy, który chciałby dane z raportów pobierać. Myślę, że nie wiem, co z tym zrobić, czy robić jakieś chwilowe obejście. Mamy już jednego klienta, który strzela nam do **AMODIT** po API i wyciąga milion danych i obciąża chmurę. To byłby kolejny, który by nam strzelał po to, żeby dane sobie wyciągać.

**Damian Kaminski:** Możemy to na chmurze ograniczać.

**Janusz Bossak:** Tak, trzeba jakoś przemyśleć. Nie chciałbym, żeby to był Janek Pijanowski pisze. Klient wrócił do tematu i dopytuje się o nasze REST API. Pytanie, co myślicie? Nie wiem, czy widzisz to na kanale. Mówię do ciebie, do Damiana. Ty jesteś tam skierowany na tym kanale.

**Damian Kaminski:** Nie, jeszcze się z tym nie zapoznawałem. Akurat znajomy pytał o taki system do zbierania zamówień z różnych źródeł, ich pochodzenia. Ktoś ma sklep internetowy, Allegro, Amazon i różne typy źródeł sprzedaży. To narzędzie zbiera to, czyli jest takim menadżerem sprzedaży. Wszystkie zamówienia trafiają w jedno miejsce. Nie trzeba obserwować wielu różnych źródeł. Oni też mają u siebie limit zapytań.

**Janusz Bossak:** Tak, powinniśmy mieć takie limity zapytań: godzinne, minutowe, dzienne.

**Damian Kaminski:** Tak i jak chcemy więcej, to kosztuje, bo są z tym związane wydajności.

**Janusz Bossak:** Słuszna uwaga. To jedna rzecz, którą trzeba pewnie zrobić. Ale teraz już klienci coś mają i wprowadzenie im ograniczeń będzie odebrane jako coś niekorzystnego.

**Damian Kaminski:** Według mnie powinniśmy zacząć od analizy. Zobaczyć, na kogo będzie miało to wpływ i jakie to faktyczne. Czy jesteśmy w stanie to jakoś sprawdzić o te zapytania z zewnątrz. To też klienci muszą zrozumieć, że jak wprowadzimy coś takiego, to muszą się dostosować. Muszą zmniejszyć częstotliwość. Mogę przerzucić to tutaj jako nowy temat, żeby nam nie wypadł i zostawić to na Radzie. Jak wróci Piotr, będziemy to omawiać. Pytanie tylko, czy zanim wróci Piotr, jesteśmy w stanie to do kogoś przypisać? Może Łukasz Poskrobko mógłby nam pokazać listę klientów, którzy mają najwięcej tego typu połączeń zewnętrznych aplikacji. To nam da jakiś obraz, jak do tego podejść i czy to dotyczy jednego klienta, czy jakiejś skali, jakie poziomy przyjmować.

**Adrian Kotowski:** Ten login **AMODIT** jest wykorzystywany. Można z tego skorzystać, ale trzeba to jeszcze zintegrować.

**Damian Kaminski:** Tak, bo tu pewnie by trzeba było ograniczyć.

**Adrian Kotowski:** Myślę, że trzeba by lepiej zbadać ruch wychodzący, przefiltrować nasze witryny i zobaczyć, co jest na zewnątrz.

**Damian Kaminski:** Tak. **KSeF** Connector i tak dalej.

**Adrian Kotowski:** Azure Monitor może.

**Lukasz Bott:** Żebym dobrze zrozumiał, chciałeś, żeby zestawienie wywołań zewnętrznych usług do nas.

**Damian Kaminski:** Tak. Rozumiem, czy oni od nas strzelają tak dużo na zewnątrz?

**Lukasz Bott:** Rozumiałem, że ktoś wykorzystuje nasze REST API i robi tego dużo. REST API nie jest zbytnio na chwilę obecną wydajnościowo przygotowane, żeby obsługiwać takie duże masowe zapytania.

**Janusz Bossak:** Tym jest problem.

**Damian Kaminski:** Okej, w takim razie w dwie strony. Dobrze.

**Janusz Bossak:** Chodzi o to, żeby inne systemy nie strzelały do **AMODIT** albo że.

**Damian Kaminski:** A właśnie.

**Lukasz Bott:** Mogę sobie strzelać, tylko na jakiś tam.

**Janusz Bossak:** Tak.

**Lukasz Bott:** Regulacjach tak przy zakładaniu jakieś.

**Janusz Bossak:** Może my strzelamy do zewnętrznych systemów. To jest problem tych zewnętrznych systemów. Jeżeli my strzelamy za często, ale chodzi o to, żebyśmy chronili **AMODIT**, w szczególności **AMODIT** na chmurze. Jak to robi klient na `on-premises`, to jego sprawa. On obciąża, ale jeżeli robi to na chmurze i wysyła co minutę zapytanie o raport, który zawiera 100 000 pozycji, to tak nie chcemy. W tym jest problem.

**Adrian Kotowski:** Takie wzorce chmurowe, że jeżeli jest jakiś limit i czy powiedza pytań, to na przykład można zwracać, że "przekroczony limit" (status HTTP).

**Damian Kaminski:** To jest wtórne pytanie. Na początku musimy ustalić, jaka to jest skala, kogo to dotyczy, jaki ten limit powinien być. Adrian, zasugerowałeś, że monitor wydajności zbiera coś takiego, ale z zewnętrznych zapytań.

**Adrian Kotowski:** Nie wiem, czy to jest w drugą stronę. Myślałem, że to jest wchodzący. Monitor wspiera ruch wychodzący, ale monitor Azure Monitor powinien rejestrować cały ruch wchodzący i wychodzący.

**Damian Kaminski:** Dobrze, to zapytamy Łukasza, czy on coś jest w stanie z tych statystyk serwerowych wyciągnąć. Ja nie znam tego tematu. Janusz, zaraz się z nim zapoznam i podstawę, bo kogo to dotyczy. Klient: Ellie Stage.

**Janusz Bossak:** To jest temat ogólnorozwojowy. Mamy wpisane na roadmapie na Q2 ten Open Data Standard. Przemek mocno ciśnie, bo chodzi o to, żeby wyciągać dane do **Tableau** czy do BI. Przyspieszyłbym tę pracę, żeby były w Q1. Chodzi o to, żeby nie obciążać **AMODIT** takimi `requestami` typu "podaj mi dane z tej sprawy, podaj mi dane z tej sprawy" i tak 100 000 razy.

**Damian Kaminski:** To może się nie spodobać klientom. To jest oczywiste. Znam też przypadek biznesowy z innej firmy, która płaciła za ileś żądań 1000 zł, a nagle została jej zaproponowana (bez negocjacji) stawka 15 000 zł. Wynikało to z potrzeb tego konkretnego podmiotu, że mieli taką dużą skalę. My wprowadziliśmy na REST API licencję. Może kolejnym krokiem będzie ograniczenie REST API do 10 000 czy miliona zapytań miesięcznie. Skalowane per dzień, a nie, że jednego dnia można strzelić milion. Chcesz więcej? Rozmawiamy o licencji, podwyższamy ją.

**Janusz Bossak:** Najpierw trzeba zbadać, ile to rzeczywiście jest w skrajnych przypadkach, gdzie ludzie mają swoje systemy i strzelają bezpośrednio na przykład do Trust Center, bo to tam też występuje. Ile danych pobierają, żebyśmy wiedzieli, jaki to jest strumień. Wracając do Ellie Stage, trzeba temat rozpoznać. Może jakieś obejście dla nich z raportami? Propozycja: wywołanie jakiegoś endpointa, którego pewnie nie mamy, dotyczącego raportu. Działałoby w ten sposób, że najpierw raport po stronie **AMODIT** się wygeneruje, jego wyniki się zapiszą gdzieś, a potem cała ta paczka wyników zostanie przekazana. Ale to trzeba całą koncepcję wymyślić. Na razie tego nie ma. Nie mamy czegoś takiego jak odpytywanie się o dane z raportu. Nie ma takiego endpointa.

**Damian Kaminski:** To też w kontekście chmury pewnie mogłoby być jakoś kolejkowane.

**Janusz Bossak:** Kolejkowanie. Trzeba temat zgłębić, skoro się kolejny klient o to pyta. Zobaczyć, co z tym zrobić.

**Damian Kaminski:** Ile pyta o konkretną sprawę, to dostaję odpowiedź od razu. Jak pyta o zestawienie miliona danych, to musi najpierw zostać zebrane w **AMODIT**.

**Janusz Bossak:** Właśnie o to chodzi. To nie temat na Radę, żeby o tym decydować, tylko jedyne, co możemy zdecydować, to kto ma się tym zająć.

**Damian Kaminski:** Tak. Mamy zapisane. Jest wrzucone na Radę. Jeszcze coś Łukasz było z ostatniego piątku?

**Lukasz Bott:** Ja mam spisane numery. Mam taki spisany numer (`22411`), żeby się tym zająć.

**Damian Kaminski:** Janusz, to ty opisałeś.

**Janusz Bossak:** Tak, to było zgłoszone chyba przez LPP albo przez...

**Damian Kaminski:** Coś takiego.

**Janusz Bossak:** Przy okazji tych ogólnie filtrów. Jest jakaś wątpliwość?

**Lukasz Bott:** Czy musimy te Radę dać?

**Damian Kaminski:** Nie, nie tyle, co wątpliwość.

**Janusz Bossak:** Pamiętam, chyba rozmawialiśmy na ten temat.

**Damian Kaminski:** Tak, tylko tam była taka konkluzja, że może powinniśmy się spotykać. Ty to opisałeś, zaproponowałeś. Ja tu widzę, że to jest cząstkowe rozwiązanie. Pytanie, czy to na pewno jest już koniec? Bo ty to opisałeś w kontekście tylko i wyłącznie tych filtrów lewych, a nie ma kontekstu filtrów górnych. Zgadzam się, że najczęściej pewnie wykorzystują filtr po lewej stronie, natomiast równie dobrze ktoś może wykorzystać filtry na górze. Pytanie, czy to na razie robimy? Obsługujemy tylko to, czyli ktoś może zdefiniować filtr różnorako, albo przez drzewko, tak jak mamy tu, albo na górze ograniczyć to w jakim zakresie. Na razie rozpatrujemy tylko drzewko. Jeśli mamy drzewko i filtr na górze (takie combo), i znika z drzewka wszystko, czyli jest realizowane to, co ty zaproponowałeś. Gdy na raporcie nie ma już co pokazać, powinno przenieść zaznaczenie do najbliższego rodzica. W raporcie wyświetlać pozycje odpowiadające temu nowemu zaznaczeniu. Jeśli w połączeniu z filtrami górnymi dalej nie ma nic, to co wtedy? Musiałbym przygotować taki przypadek, bo nie wiem, co się wtedy wydarzy.

**Janusz Bossak:** Tam jest temat.

**Damian Kaminski:** Rozumiesz, o co mi chodzi?

**Janusz Bossak:** Tak, rozmawialiśmy o zmianie sposobu zachowania się systemu po wykonaniu masowych czynności.

**Damian Kaminski:** Tak.

**Janusz Bossak:** Moja konkluzja była taka, żeby ta akcja masowa (czy to podpisywanie, czy wykonywanie reguł) niczego nie zmieniała na raporcie. Kiedy wykonuję tę akcję, nie zmienia mi się kontekst raportu. Pojedyncze rekordy są aktualizowane (np. na zielono). Jeżeli wykonanie tej czynności spowodowałoby uzupełnienie daty przekazania, to ona powinna się tu pokazać. Jeśli czynności spowodowały zmianę stanu, to również powinno się pokazać. Mimo że on teraz nie pasuje do ustawień filtrów. Powinno to zniknąć.

**Damian Kaminski:** Rozumiem twoje podejście. To już jest bardziej długofalowa wizja.

**Janusz Bossak:** Ale tak powinno być w moim przekonaniu. Jako użytkownik bym to rozumiał. Wykonuję masową czynność, która zmienia mi rzeczy. Widzę, co się zmieniło. Dopiero wtedy decyduję: odśwież mi raport. Wtedy wszystko inne się wykonuje: znikają sprawy, odświeżają się filtry. Niepożądany skutek: jeśli mamy ustawione domyślnie "na zawiera", to mimo że nie ma żadnego filtru, jest "Wyczyść wszystkie". Jak kliknę "Wyczyść", to znika. Powinniśmy to poprawić.

**Janusz Bossak:** Dodatkowe efekty. On jeszcze nic nie zawiera.

**Damian Kaminski:** Dokładnie. Natomiast to, co mówisz Janusz, to tu mamy, powiedziałbym tak to co mówisz, to już jest kolejny element wtajemniczenia w aktualizację danych na raportach. Mamy tu pewną niespójność. Od tego należałoby zacząć dyskusję. Co się dzieje po podpisaniu i tak dalej. Jeśli podpisuję, a ten podpis skutkuje jednocześnie wykonaniem jakiejś akcji, to system zachowuje się niespójnie. Wybieram podpis. Proces podpisywania się rozpoczął. Dokument został podpisany. Na drugim ekranie mieli, coś się zmieniło. Nie działa tak jak powinno. Powinno się odświeżyć okienko. Czy chcesz odświeżyć raport? Tu mamy niespójność. Jeśli podpisujemy z wywołaniem akcji masowej, to wyświetlamy `popup`: czy chcesz odświeżyć, czy zamknąć? Czyli chcesz zobaczyć stan sprzed wykonania tej akcji, czy już odświeżyć? Nie widzieć tych spraw. Nie ma tego okienka dla samego wykonania akcji.

**Janusz Bossak:** To, co mówiłem, że już o tym rozmawialiśmy. Absolutnie jestem za tym, żeby to uspójnić, żeby nie miało znaczenia, czy to jest podpisywanie z akcją, czy bez akcji, czy wykonywanie samej akcji masowej. Chciałbym, żeby.

**Damian Kaminski:** Powinniśmy kończyć ekranem podsumowania.

**Janusz Bossak:** Powinniśmy po pierwsze zmieniać stan tych rekordów, które podlegały masowej akcji. Żeby mi się tu wyświetlało na przykład w kolumnie "Organizacja" czy "Data przekazania" (w takich, w których coś wyświetlamy). Jeżeli akcja masowa powoduje jakieś zmiany, to żeby to się tu wyświetlało, żebym widział, że się zmieniło. Nie ma się wykonać odświeżenie. Chcę przejrzeć tę stronę, którą widzę. Zapoznać się z tym, co mi się tu wydarzyło. Faktem jest, że nie mamy opcji "Cofnij" dla akcji masowej. To jest inna sprawa. Przynajmniej będę widział i będę mógł ocenić, co mi się tu zadziało. Zrobię screen tej strony, jeśli coś zrobiłem źle i wejdę wtedy w pojedyncze sprawy i je poprawię. W momencie, gdy znikają mi z ekranu, nie wiem, co się wydarzyło. Rozdzielić te dwa stany. Jest stan: raport po wykonaniu czynności masowych (widzę na ekranie, co się wydarzyło). Dopiero klikam "Odśwież" i wtedy raport się przebudowuje z odświeżonymi rekordami. Mogę działać na filtrach. Mogę wybrać inny filtr. Cokolwiek zrobię, powinno się zastosować. Raport powinien się zaktualizować. Jak kliknę "Zamknij i odśwież", to wszystko się wykonało. Zamykam, odświeżają mi się filtry, rekordy znikają. Jak zamknę, to wracam po prostu do raportu, w którym widzę te rzeczy, które się zmieniły. To jest mój główny postulat, żeby to zostawało, jak kliknę "Zamknij", żebym widział, co się pozmieniało po wykonaniu akcji masowych.

**Damian Kaminski:** Tak, to tak teraz jest akurat domyślnie. Tak to działa dla przypadku, gdy w ogóle nie wyświetlamy okienka. Wykonujemy akcję masową typu "indeks".

**Janusz Bossak:** I bardzo dobrze.

**Damian Kaminski:** Za indeksuje, zostanie na zielonym, czyli tak, jakbyśmy kliknęli "Zamknij". Należałoby tu właśnie jeszcze może dołożyć: czy chcę tę pozostałość? Ale jeśli dołożymy to, to według mnie musimy zdecydować, co się dzieje tu. Będzie to nagminne. Przypadek, który opisał Mateusz w błędzie, że nie tylko po podpisaniu znikają, ale też po wykonaniu akcji masowej filtr będzie pozostawał. Najpierw musimy zaopiekować kwestię filtra, a później dopiero wyświetlać ten popup dla spraw masowych. Najpierw musimy zaopiekować lewą stronę. Przejrzę to jeszcze. Tu nie ma chyba `acceptance criteria`, więc dopiszę.

**Lukasz Bott:** Sprawdźcie numer `22816`.

**Damian Kaminski:** `22816`. Tu nie ma Piotra. To jest ten nieznany powód błędu. Z jakiegoś powodu przy API nie ma połączenia do bazy danych.

**Lukasz Bott:** Dobrze. Zobacz w komentarzu. Chcemy to wpisali, bo to chyba.

**Damian Kaminski:** Trzeba podbić. Bo zaraz nie będzie tych wpisów.

**Lukasz Bott:** Do Jarka. Może trzeba to.

**Damian Kaminski:** Wyślę mu to bezpośrednio.

**Lukasz Bott:** Nie, nie chodzi mi o to, żeby tutaj nie zmieniać Piotrka na Jarka na blok i `waiting for information`.

**Damian Kaminski:** Dobrze.

**Lukasz Bott:** Jeżeli to jest błąd taki, który się raz na jakiś czas wydarza, poza tym dzieje się. Jeśli za chwilę nie ma tego problemu.

**Damian Kaminski:** Tak, są tylko takie komunikaty negatywne dla biznesu. Wyślę to Jarkowi, żeby tego nie przegapił.

**Lukasz Bott:** Czy mamy z tym coś robić? Tutaj faktycznie był "pierdliwy".

**Damian Kaminski:** Chyba na tym możemy skończyć.

**Lukasz Bott:** Nie, ja nie mam. Mamy jeszcze jedno, ale to już dyskutowaliśmy.

**Damian Kaminski:** Resztę zostawmy. Dobra. Dzięki. Adrian, chcę tylko spojrzeć, czy ty chcesz coś jeszcze w kontekście repozytorium dyskutować?

**Adrian Kotowski:** Będę miał spotkanie później. Byłeś tam 5 minut do końca.

**Damian Kaminski:** Mam teraz spotkanie z Allianz, w sprawie integracji. Dobrze, słyszymy się o 12:00.

**Anna Skupinska:** Cześć.

**Janusz Bossak:** Zatrzymano transkrypcję.

**Data spotkania:** 6 października 2025

**Damian Kamiński:** No dobrze to pytanie, kto chciałby się pierwszy pochwalić osiągnięciami ubiegłego sprintu?

**Anna Skupińska:** Niestety jeszcze jestem w połowie, może nawet w połowie robienia tych nowych rzeczy systemowych. Zrobiłam w zeszłym tygodniu dashboard systemowy, ale żadnych jeszcze nie ma w systemie, jeszcze są inwestowane. Za bardzo mogę pokazać tylko kod, co najwyżej.

**Damian Kamiński:** Nie, no to tutaj raczej byśmy liczyli na efekty, w sensie żeby prezentować. No to pokażesz to na następnym spotkaniu.

**Anna Skupińska:** W tygodniu.

**Damian Kamiński:** Bo mówimy tu o raportach systemowych, tak w zasadzie to pewnie mógłby je pokazać też Łukasz, ale jeszcze nad tym pracujemy, bo to nie musi być już na gotowym środowisku, więc myślę, że to jeszcze przesuńmy na kolejne podsumowanie.

**Łukasz Bott:** Tak, tak, tak.

**Damian Kamiński:** No dobra, w międzyczasie widzę dołączył też Filip. Czy ty chcesz od czegoś zacząć w swoim obszarze?

**Kamil Dubaniowski:** No jak jest Filip to może zacznijmy od logów systemowych, bo to jest coś, co faktycznie można pokazać. Nie wiem. Filip, chcesz pokazać na jakimś swoim, czy to co ja mam na Filipie, to jest aktualne?

**Filip Liwiński:** Filip 1 jest aktualny, możesz pokazywać.

**Kamil Dubaniowski:** Podajcie mi sekundkę. Już znajduję. Tam jeszcze oczywiście znajdziemy coś do poprawki. Natomiast co zrobiliśmy? Odświeżyliśmy stronę logów systemowych. Głównym celem było to, żeby po prostu już mieć wszystko w ramie Reactowej. Za dużo na nowych funkcjonalnościach tych logów się nie skupialiśmy, raczej odtwarzaliśmy to, co było. Dajemy to na nowy wygląd, ponieważ ta strona logów systemowych właśnie została ostatnią, gdzie jeszcze mieliśmy stronę. I tak to wygląda aktualnie. Czyli mamy podobnie jak do tej pory było podział na zakładki z logami systemowymi, aktywnością administracyjną i kolejką maili do wysłania. Mamy te same wyszukiwania i działa ona również na tej samej zasadzie, co do tej pory, czyli po użyciu przycisku. Wtedy było wyszukaj i teraz zastosuj, ponieważ jest to globalne, działa to także jakby w pakiecie z filtrami, czyli dopóki nie uznam, że zakończyłem wrzucanie tutaj jakiś swoich kryteriów, to te filtry nie działają. To ze względów wydajnościowych, czyli dopiero w tym momencie moje wyszukiwanie i filtry zostały nałożone na listę.

**Piotr Buczkowski:** Szukam też w treści.

**Kamil Dubaniowski:** Tutaj mamy dopiero w tym momencie domyślnie.

**Piotr Buczkowski:** Dobrze, bo nie, właśnie nie widziałem tego.

**Kamil Dubaniowski:** Tak, to to jest jakby tutaj sam.

**Piotr Buczkowski:** A to naprawdę powala mocno.

**Damian Kamiński:** No warto powiedzieć o tym eksporcie, Kamil, bo to jest też wygodne.

**Kamil Dubaniowski:** Tak, mieliśmy do tej pory taki masowy globalny eksport, właściwie całej strony logów, która się załadowała. To był oczywiście eksport do pliku, ale nie było opcji wyboru, które tak naprawdę logi nas interesują, a raczej spodziewam się, że ta funkcjonalność jest wykorzystywana właśnie do wysyłki przez klienta logów. Czy też do dołączenia do zgłoszeń na Azure przez naszych konsultantów. Więc teraz ten eksport jest na zasadzie: wybieram sobie te, które uważam za istotne w moim zgłoszeniu i eksportuję zaznaczone, nie tak jak do tej pory, że tam eksportował X dziesiąt logów z bieżącej strony. Więc tutaj mamy w ten sposób teraz to zrobione. Zrezygnowaliśmy z tego eksportu, no wszystkich, więc tu nawet nie ma opcji zaznaczenia całej strony. No bo to jest raczej, jak wspomniałem, nie jest potrzebna funkcjonalność. Nikt nie będzie eksportował całej strony logów. Jeśli potrzebuję gdzieś do raportowania, no to raczej będzie robił sobie zrzut z bazy. No bo tak czy inaczej to zaznacz wszystkie byłoby o tyle nieintuicyjne, że ono tak naprawdę zaznacza te, które się załadowały na bieżącą stronę, więc to nie jest też tak naprawdę wszystkie.

**Piotr Buczkowski:** To po prawej stronie tej copy jest już do kopiowania to do schowka.

**Kamil Dubaniowski:** Tak.

**Piotr Buczkowski:** OK.

**Łukasz Bott:** Ale to właśnie co kopiuje? Tylko ten wpis, czy również całość?

**Kamil Dubaniowski:** Tak, powinno działać tak jak do tej pory.

**Piotr Buczkowski:** Trochę.

**Damian Kamiński:** No wszystko, tak, zakładam.

**Kamil Dubaniowski:** No nie, no to za spotkaniem, jak na razie widać, że nie działa w ogóle.

**Łukasz Bott:** Pierwszy raz widzę.

**Kamil Dubaniowski:** Nie skopiowało. Skopiowało mi treść przykładowej wypowiedzi z prezentacji.

**Damian Kamiński:** Na pewno celem jest, żeby wszystko było kopiowane, tak, żeby był pełny [log].

**Łukasz Bott:** Dobra, zobaczmy.

**Piotr Buczkowski:** To do tej pory kopiowało tylko ten komunikat, tak? Czy tam `StatusCode`? Nie pamiętam, tam coś tak jest nazwane. To chodziło o to, że jak jest na przykład Message czy Mail, tak, to żeby to skopiowało bez narzucania jakiegoś tam formatowania, żeby łatwo można było później to na przykład diagnozować problem. No ale chciałabym właśnie, żeby też z resztą danych kopiowało, czyli z treścią, czyli z Message czy z URL-em, z użytkownikiem, tak. Tylko tam jakoś tak w nowych dziennych formatach. No bo to często się przydaje.

**Kamil Dubaniowski:** Dobra, to jeszcze do tego wrócimy.

**Piotr Buczkowski:** A URL-a też nie ma, tak widzę. Wtedy poprzednio były chyba tak. A dobrze, tutaj nie ma URL-a, bo to jest system.

**Kamil Dubaniowski:** Tak, tutaj doręczenia.

**Piotr Buczkowski:** Z usługi.

**Łukasz Bott:** Weź, wyczyść filtr, jak macie jakiś tam wpis ze sprawy?

**Kamil Dubaniowski:** Nie wiem, czy to będzie.

**Piotr Buczkowski:** Coś tam było.

**Kamil Dubaniowski:** Robiąc to.

**Łukasz Bott:** Webapp gdzieś było.

**Piotr Buczkowski:** Nie. Tutaj powinno być dobrze.

**Łukasz Bott:** Trzeba.

**Piotr Buczkowski:** No, trzecia opcja jest gdzieś pośrodku. Teraz jak było rozwinięte, to było trzecie. Nie ma, tak. To warto by było tak, żeby...

**Kamil Dubaniowski:** Dobra, OK.

**Piotr Buczkowski:** Ten URL też był.

**Łukasz Bott:** Ale tam jeszcze gdzieś poniżej był ten wpis webapp.

**Piotr Buczkowski:** Nie, ale to jest.

**Łukasz Bott:** Dobra, nie, no to pamiętajcie, tak.

**Piotr Buczkowski:** No, to to dodam, tak.

**Kamil Dubaniowski:** OK. To do tego jeszcze będziemy wracać. Tutaj Filip, jeszcze domyślny Filip, tak. Czyli domyślnie pokazujemy tylko błąd i ostrzeżenie, ale też w sumie ten X chyba tutaj powinien być też. Nie wiem. No bo wyczyść wszystkie przywraca do tego domyślnego ustawienia, że typ "błąd", "błąd zastrzeżenia", bo to jest domyślnie filtra. Ale dobra, to jeszcze pomyślmy, czy to jest dobrze?

**Łukasz Bott:** Ale to można wybrać, tak, coś jeszcze innego.

**Kamil Dubaniowski:** Z tego. Można jeszcze informacje dorzucić, ale domyślnie tak było. W starym module pokazujemy błąd i ostrzeżenia.

**Łukasz Bott:** Aha, no to tak, tak.

**Kamil Dubaniowski:** OK. Aktywność administracyjna. No tutaj w sumie doszło, bo też się rozwija i pokazujemy szczegóły tej zmiany. Do tej pory mieliśmy tylko po prostu nagłówek aktywności. Tutaj teraz pokazujemy dokładnie, co tam się... Może nie, nie zawsze potrzebnie, ale to na przykład nic się nie wyświetla.

**Łukasz Bott:** Nie, wiesz co, to to to może i jest nawet dobry pomysł, bo jak na przykład aktywność administracyjnej, jeżeli zmienisz coś w jakieś parametry w ustawieniach systemowych, no to to to o wiele lepiej wygląda, tak? Bo dotychczasowy stan idzie w jednej linijce.

**Kamil Dubaniowski:** Tutaj na przykład nie, to jest.

**Łukasz Bott:** Co z czego, na co było zmieniane, nie.

**Kamil Dubaniowski:** Więc tak, no.

**Piotr Buczkowski:** Albo `null`. Czego coś zrobić? No ale to kwestia rejestracji, tak, że niepotrzebnie zarejestrował to coś. Część `null`.

**Kamil Dubaniowski:** Jest jakiś `slot`, czy to jest ten, który miałby tyle? No to to jest jakaś zmiana w procesie, ale no właśnie, bo...

**Piotr Buczkowski:** No tak, to coś zmiana.

**Łukasz Bott:** Ustawienie w procesie.

**Piotr Buczkowski:** W polu o nazwie przycisk. W tym, ale część `null`, tak, że nic. Zmiana nastąpiła, ale nic nie zmieniono, czyli albo coś źle rejestruje. Zmiany czegoś nie wykrywa. Tak, bo niepotrzebnie takie coś rejestruje, bo ktoś to otworzył i kliknął "zapisz".

**Kamil Dubaniowski:** Pytanie.

**Piotr Buczkowski:** Tutaj też widzę, że niepotrzebnie to jest jako "A" i "B" jest jakoś string.

**Kamil Dubaniowski:** To tutaj też.

**Piotr Buczkowski:** Ale to nie kwestia oświetlenia, tylko kwestia rejestracji. To trzeba się przyjrzeć, tak.

**Łukasz Bott:** Albo wcześniej, Piotrek, było rejestrowane aktywności administracyjnej, no nie? Jeżeli to jest.

**Piotr Buczkowski:** Znaczy tutaj nic, co nie zostało zmieniane, przynajmniej ja nic nie wiem, żeby coś było zmieniane.

**Kamil Dubaniowski:** Dobra, to ja sobie rzucę okiem później jeszcze na stary, ale też na nie spodziewam się raczej niż dokładaliśmy, chociaż chociaż to.

**Łukasz Bott:** Nie, nie, no części pierwszej to są zmiany w ustawieniach procesu, tak.

**Piotr Buczkowski:** Moja uwaga jest taka, że jest zarejestrowana zmiana w ustawieniach procesu. Tylko, że jest `null`, czyli była zmiana, ale nie było zmiany. Czyli ktoś kliknął "edytuj", "zapisz", ale nic nie zmienił. Mimo to zarejestrował, że była zmiana.

**Łukasz Bott:** OK. No dobra, no to to jest twoja uwaga, ale pytanie...

**Piotr Buczkowski:** O to mi chodzi. Że niepotrzebny wpis.

**Kamil Dubaniowski:** Bo tego. Znaczy ten element był dorobiony. No wiadomo, tak jak zresztą logi, tylko logi były zrobione już dawno temu, a tych 2 nie mieliśmy, bo Mateusz jak robił wtedy pierwszą próbę jako pierwsze swoje zadanie, Mateusz to dostał. To zrobił tylko logi, to dorobiliśmy teraz, ale spodziewam się, że jest, no to zwraca to samo, co stary. Więc to do zweryfikowania, dlaczego w ogóle rejestrujemy te zmiany `null-owe`, a dwa, czy one były wcześniej w ogóle tutaj wyświetlane, czyli były tylko po stronie? Historii edycji procesu, ale wydaje mi się, że musiały być też tutaj. Dobra, to będziemy patrzeć. Idziemy dalej. Kolejka maili. Tutaj też przy okazji spotkania z klientem i omawiania nowej wersji oraz planów. Co dalej będziemy robić? Między innymi dyskutowaliśmy chwilę o tych logach. Ta kolejka maili będzie miała, na czym ma już nową funkcjonalność. Plus jeszcze Piotr ma na to jeden pomysł. Co do tych maili z kolejkowanych, no to jest na razie funkcjonalność, w którą i tak klienci robili to, co robili to z poziomu bazy danych. Na przykład na czas testów zatrzymywali sobie wykonywanie wysyłki maili. Testowali intensywnie, kolejka się tam kumulowała, mieli po sto maili na na na w kolejce. I teraz gdyby uruchomili Joba, no to zaczęłaby spływać tam fala maili do ludzi, którzy zazwyczaj mają adresy służbowe, te produkcyjne podpięte też pod test, więc. No po prostu kasowali to z bazy. Takie można już sobie kasować na bieżąco z tej kolejki. Plus będzie też odtworzona funkcjonalność, którą wykorzystujemy w tej aplikacji dedykowanej pod Orlen. Tam na poziomie procesu można sobie wskazać odbiorcę maili na czas testów, właśnie chociażby, czyli zamiast do faktycznego odbiorcy, do którego by ta wiadomość wyszła, to maile mogą być wysyłane na przykład do konsultanta. Aktualnie w tym momencie prowadzi testy i to głównie dla niego jest to, czy maile wychodzą i wychodzą do tych osób, których powinny. Więc to będzie jeszcze dodatkowa rzecz. To na ten moment po prostu kolejka można weryfikować, co by się wysyłało. Tutaj sobie można sprawdzać każdy z maili, tak samo, jak było do tej pory mamy podglądy tych maili, a w momencie zakończenia testów możemy kolejkę wyczyścić, żeby tam kiedyś, przy uruchomieniu Joba, to nie zaczęło się wysypywać.

**Łukasz Bott:** To. Jest to, jak mówisz.

**Piotr Buczkowski:** Bo to był taki mechanizm.

**Damian Kamiński:** Jeszcze.

**Piotr Buczkowski:** Taki mechanizm maile poufne, których nie można treści wyświetlić.

**Damian Kamiński:** No właśnie, też o tym pomyślałem. Czy to uwzględniliście?

**Piotr Buczkowski:** Czy to zostało?

**Kamil Dubaniowski:** Dobra, to do przejrzenia. Nie wiedziałem o tym. Jeszcze widzę, że brakuje tutaj informacji o kolejnej planowanej dacie wysyłki.

**Łukasz Bott:** Tak, właśnie miałem się o to zapytać.

**Kamil Dubaniowski:** To też jeszcze te 2 rzeczy?

**Łukasz Bott:** Tak, to informacje, kiedy ten Job się kolejny raz ma uruchomić.

**Kamil Dubaniowski:** Dobra, no to to też do popisu.

**Łukasz Bott:** A czy czekaj, a to co masz w prawym górnym rogu obok przycisk odśwież, to ikonę filtra czy?

**Kamil Dubaniowski:** To jest tak jak w panelu, znaczy tak jak filtry w tym module raportowym, nie. Tylko rozwijać tą belkę, po prostu do tego to służy. Domyślnie jest rozwinięte. Jak ci tam byłoby potrzeba więcej miejsca, to możesz sobie to zwinąć.

**Łukasz Bott:** Aha, czyli włączenie wyłączenie filtra. Dobra. OK, dobra.

**Kamil Dubaniowski:** Ale widzę, że nie oszczędzamy tego miejsca tutaj. Tym białym. To będzie trzeba.

**Łukasz Bott:** W zasadzie jeden wiersz tylko.

**Kamil Dubaniowski:** No. Czy do przemyślenia. Możliwe, że tabelka w ogóle będzie cały czas na wierzchu. Przemek miał co do tego sugestie, żeby właśnie wręcz na start była zwinięta. No ale wtedy pewnie pełny przycisk z napisem by się tu przydał, bo Przemek nie do końca i to się zgadza z nim, bo wcześniej było tutaj jeszcze z ikonami, chociażby ten filtr. Tak było to, że nie było z ikonami i przemyślał, że to są jakieś przyciski. Złapał w pierwszym momencie, że to są filtry. Był tabelka była domyślnie rozwinięta i w dodatku to był jeszcze właśnie jakieś ikonki. No to jeszcze będziemy najwyżej tam to projektować. Wybrać sobie projekt. Ale funkcjonalnie to już. W dużej części gotowe. No widzę, że tutaj jeszcze nie mamy wszystkich filtrów. Tutaj w sumie brakuje, chyba nie wiem, czy wszystko jest. No bo na aktywność to jest tutaj wyszukiwarka, czyli tutaj jeszcze tylko nam brakuje po odbiorcy i po tytule. A tak to mamy komplet tych filtrów. Też wcześniej nie było, czyli aktywności administracyjnej i kolejki maili nie dało się filtrować, była tylko wyszukiwarka. To też doszło względem starej wersji. W sumie dla przypomnienia z tym, może na naszym Astros Opsie możemy sobie obejrzeć stare filtry też dla kogoś, kto nie wiem, kto do tej pory wyglądało. To jest jeszcze stara funkcjonalność ograniczenia tego menu po obszarach. Już wolę, ale widzę, że u nas jeszcze działa. Tak to wyglądało wcześniej, czyli to co znaliśmy do tej pory, to przełączanie było z tego poziomu. Teraz w nowej wersji już mamy te ścieżki tutaj na górze, więc mamy to w formie zakładkowej. Tutaj ten wspomniany eksport, którego niekoniecznie korzystaliśmy do tej pory i w sumie to tyle. Możemy na szybko, jak już się o tym włączyłem, zobaczyć sobie tę aktywność. Chociaż nie wiem, czy to ktoś robił jakieś zmiany na procesie, tak? No dobra, to nie będę przedłużał. Tyle.

**Łukasz Bott:** Część proces, tak.

**Kamil Dubaniowski:** Nie wiem, Filip, czy chciałbyś jeszcze coś dodać ewentualnie do innych, bo kojarzę, że coś tam w matrycy pewnie w tym świecie jeszcze było, ale raczej kosmetyka.

**Filip Liwiński:** No w sumie tylko w matrycy była to też no kosmetyka tylko tam wyłącznie.

**Kamil Dubaniowski:** To matryca uprawnień i w ustawieniach procesu o tym mówimy, ale tak tam funkcjonalnie i wizualnie się raczej się nie zmieniło. Raczej kwestia testów i `fail testów` potencjalnie. Plan na zmianę jest, tylko ja jeszcze nie do końca jestem do niego przekonany, więc nie chcę też tak jak ostatnio pochopnie decyzji podejmować. Więc wstrzymuję na razie. Wyjdzie tak, jak zrobiliśmy te matryce i tyle. Kto kolejny?

**Damian Kamiński:** Ja może krótko o komunikatorze. W zasadzie pod koniec ubiegłego tygodnia wyszedł nam. Wyszła nam jeszcze jedna potrzeba, to będę omawiał tutaj z Mateuszem, bo nie był dostępny w czwartek i piątek. Niemniej ono dotyczy tylko jednego elementu, więc już zaraz po nim powiem. Jeśli chodzi o komunikator, to w zasadzie możemy uznać, że jest skończony względem tego, co było wcześniej. To poprawiliśmy spójnie w ramach całego systemu. Awatary tu jeszcze widzimy stary, bo to jest z Mateusza, natomiast na developerze już Ania też poprawiła jednym cięciem. To jest to po prostu trochę bardziej eleganckie, bez jakiś ramek i te czcionki są podobne do wszystkich czcionek w systemie. No mamy poprawki takie wizualne, tak, czyli tutaj upodobniliśmy całą konwersację do konwersacji tekstowej. Odpowiednio dostosowuje się do ekranu, nie jest od brzegu do brzegu, tylko jest w określonym zakresie, żeby nie trzeba było biegać wzrokiem między skrajnymi elementami ekranu. To, czego tu jeszcze teraz zauważyłem? To może wymaga konsultacji między Mateuszem a Przemkiem. Nie wiem, pogadajcie, bo tutaj nie mamy ścieżki dla komunikatora. Tak jak dla wszystkich innych elementów systemu, jeśli chodzi o konwersacje, no to cóż, tworzymy i tu właśnie jeszcze będzie pewna poprawka w kontekście prywatnej grupowej. Na ten moment wygląda to tak, możemy utworzyć prywatną z konkretną osobą. Po prostu zaczynamy tą konwersację, lub też grupową i wtedy wskazać wiele osób w tym zakresie. Właśnie chyba będziemy szli w stronę ujednolicenia, czyli to kogo wskażemy, zdefiniuje, jaki jest to rodzaj konwersacji. I pracujemy jeszcze nad jednym takim elementem funkcjonalnym, czyli połączeniem z grupami, bo tego jeszcze nie mamy. To jest takie ostatnie. Poza tym uproszczeniem tej formy, to to właśnie jeszcze konwersacja na podstawie składu grupy określonej w ramach AMODIT-a. Poza tym. Drobne poprawki wizualne względem tego, co było wcześniej. I chyba tylko tyle. Nie wiem, czy to ewentualnie jakieś pytania.

**Łukasz Bott:** No trzeba będzie pogadać przez konwersację i to pewnie wyjdą pytania.

**Kamil Dubaniowski:** Jak?

**Damian Kamiński:** OK, no to w takim razie.

**Kamil Dubaniowski:** Ja jakbym prosił Przemka, żeby nam to jest... członkiem w ogóle jest... Te diagramy jakbyś pokazał, no bo to jest serce.

**Damian Kamiński:** Jest.

**Kamil Dubaniowski:** Niewiele osób widziało.

**Łukasz Bott:** Słuchajcie, tylko mała dygresja do tych logów systemowych i aktywności administracyjnej. Były, sprawdziłem, faktycznie rejestrujemy `Case` i `Process` oraz `Report`. Takie 2 zdarzenia, przy czym w tym starym interfejsie nie widać szczegółów. Czyli wiemy tylko tyle, że ktoś coś tam w jakimś procesie czy w raporcie coś zmienił, ale wiemy kiedy, kto, ale co – to nie. Więc być może to jak teraz tam zaprezentowaliście, że to jest i po kliknięciu są jakieś tam szczegóły, no to możemy to zostawić chyba tak. Czyli w tym w tym nowym podejściu w tym nowym interfejsie do logów systemowych, tych aktywności administracyjnej, jest to bardziej użyteczne, tak, no skoro wyświetlamy tam jako...

**Kamil Dubaniowski:** Tak, tylko trzeba zweryfikować, dlaczego ten `null` nam zapisuje w sensie, że nie ma żadnej zmiany, no bo to jest nadmiarowe i bez sensu.

**Łukasz Bott:** Tak, tak. No dokładnie. Dobra, to to to to. Pamiętam. Projekt.

**Damian Kamiński:** Tak Przemek, proszę.

**Kamil Dubaniowski:** Mikrofon.

**Przemysław Rogaś:** Dobra, to ja tam wrzuciłem. Jeszcze dałem zmiany do edytora. To na szybko pokażę, co to było z tego diagramu. No już mam wyszukiwarkę. Tutaj będę. To, że można szukać po. Po nazwach wyświetlanych i po nazwach systemowych. Tutaj nie widać, bo żaden z nich nie ma nazw wyświetlanych, ale normalnie, gdyby były, no to by się wyświetliły. Przykład. Tak to wygląda jak szukamy po polsku, to będzie tylko polskie. Szukam po systemowej albo po innym języku, no to pokaże się tylko ten, którego znajdziemy.

**Łukasz Bott:** Przemek, mogę na szybko tylko jedną uwagę wizualną.

**Przemysław Rogaś:** Mhm.

**Łukasz Bott:** Jak masz tą belkę widzi, to masz edytor grafiki, przełączanie, edytor graficzny, lista matryca uprawnień. Jakbyście mogli etykiety obok tych ikonek troszkę przybliżyć, bo przez chwilę miałem takie wrażenie, że to są zupełnie odrębne przyciski tam.

**Damian Kamiński:** No tak, to racja, trochę za duża chyba odległość. Między ikoną a napisem. Matryca uprawnień, ikona, lista.

**Łukasz Bott:** Między innymi.

**Przemysław Rogaś:** Taktycznie.

**Łukasz Bott:** No dobra, wiesz, no.

**Przemysław Rogaś:** Pewnie było jakoś zmieniane, nie kojarzę, żeby to tak było wcześniej.

**Łukasz Bott:** No dobra, to wiesz, sprawdź to. I w długą.

**Kamil Dubaniowski:** Na pewno nie na zlecenie, przynajmniej nie ja zgłaszałem, więc jak się coś rozjechało do przy okazji.

**Łukasz Bott:** Dobra, no.

**Przemysław Rogaś:** No dobra, no tutaj jest wyszukiwarka. Jak klikniemy, no to nas przenosi do tego pola `Scroll` i odpala. Możemy szukać globalnie, więc tutaj odrodzę nasz kontekst tabeli, przyniesie. Tutaj była jeszcze bezpieczna edycja słownika. To znaczy tutaj nie możemy zmienić słownika. Musimy się doklikać. Możemy zmienić teraz Słownik i musimy zaznaczyć, że zdajemy sobie sprawę z ryzyka. Zapisujemy. I tak to wygląda. Tutaj zostały dodane Labele dla pól, które docelowo nie mają Labeli w sprawie i po prostu są na szaro z Tooltipem. Jeżeli nie jest widoczne. Idę do zmiany typu pola. Można zmienić typ pola i trzeba zaznaczyć, że zdajemy sobie sprawę z ryzyka.

**Piotr Buczkowski:** A jak zmieniasz typu numerycznego na kwotę? Albo odwrotnie.

**Damian Kamiński:** W sensie typ pola.

**Piotr Buczkowski:** Masz kwota na przykład?

**Kamil Dubaniowski:** W sensie, że chodzi o to, czy nadal trzeba zaznaczyć, tak? Ja nie specyfikowałem, że nie trzeba. To znaczy nawet jak na ten sam typ...

**Piotr Buczkowski:** No bo...

**Przemysław Rogaś:** No nie no, trzeba zaznaczyć do wszystkich.

**Piotr Buczkowski:** Akurat przypadku nie będzie, nie ma potrzeby. Był kwota obok, obok numerycznego jest.

**Kamil Dubaniowski:** No bo to jest tak, to ten sam typ. Tak tylko, powiedzmy, że zostawiłem. To nie chciałem się bawić, no bo może być to nieintuicyjne na przykład dla użytkownika zmiana z pola. Nie wiem, Słownik na lista wyboru czy nie wiem z... No nie jest to logiczne, że znaczy dla użytkownika, dla nas tak, no, bo słowniki u nas są numerycznymi tak naprawdę w bazie, a lista wyboru jest tekstowa dla użytkownika. Wizualnie to jest de facto to samo, no i nie każdy może załapać, że raz wy... typy, a dwa, że no jeśli było coś w słowniku, to nie znaczy, że jest w liście, więc wyczyści nam te dane na sprawie, że uzna, że za każdym razem trzeba to zaznaczać.

**Damian Kamiński:** No lepiej chyba niech zapytają, czy to się faktycznie coś tu może stać niż bezmyślnie kliknął i coś się stanie.

**Piotr Buczkowski:** Może sprawdzać tak, że czy w sprawach to pole jest wypełnione, tak. Tak na szybko.

**Damian Kamiński:** No ale we wszystkich.

**Kamil Dubaniowski:** Tak znaczy, ja w ogóle uznaję, że to jest funkcjonalność wykorzystywana raczej na etapie wdrożenia i zazwyczaj. No nie ma tego ryzyka, ale wiem, że klienci pracują też sami. Może przyjść ktoś z pomysłem zmienić to na właśnie listę wyboru zamiast słownika, bo będziemy coś tam `SetList` wczoraj sobie zrobić na przykład.

**Piotr Buczkowski:** Znaczy, dlaczego rozwiązaniem zawsze jest, jeżeli działasz na już używanym procesie, także ukrycie pola i dodanie nowego z nowym typem.

**Damian Kamiński:** Dokładnie.

**Kamil Dubaniowski:** Dokładnie, tak, więc tak jak mówię, tym bardziej to jest raczej na etap jeszcze, kiedy trwa wdrożenie i klient w czasie testów powie nam, że no nie, no tutaj bym wolał jednak listę wyboru albo pole długi tekst, no i mamy mamy. Mamy już skonfigurowane wszystkie uprawnienia do tego pola. Podpisany kontrakt `ShowField`, tak, to wszystko działa dobrze, tylko klientowi się pola nie podoba, aby zmienił. Więc głównie do tego ta funkcjonalność raczej służy. Gdzie jeszcze na etapie wdrożenia możemy sobie na to pozwolić, bo nie mamy faktycznych danych w systemie. Nie wiem, czy jest wtedy stałem właśnie weryfikować. Ja wiem, że były przypadki, gdzie klient sobie to zmienił na produkcji. Piotr, to mam, żeby odtwarzał. Tak więc więc stąd pewnie twoja uwaga, ale nie wiem czy. Znaczy wasza decyzja, jeśli chcemy tak, no to ja zlecę, żeby walidować, czy są jakieś sprawy, które mają w tym polu dane? Będzie to dodatkowe zabezpieczenie, tylko czy jest potrzeba tak, efekt?

**Przemysław Rogaś:** No dobra, to dalej.

**Kamil Dubaniowski:** Możemy, możemy zostawić na rozwój, no to lecimy dalej.

**Przemysław Rogaś:** Wyświetlamy teraz `placeholdery` dla nas, które są dziedziczone, czyli na przykład. Tutaj jest widoczna nazwa systemowa jako placeholder. Jak tutaj, jak zmienimy... To tutaj też się zmienia, tak samo tutaj. Jeżeli zmienimy domyślną nazwę, to zmienia nam się tutaj też placeholder, który sugeruje.

**Piotr Buczkowski:** To do tej pory był opis tego pola. Jaki polski, angielski?

**Przemysław Rogaś:** Nie.

**Kamil Dubaniowski:** Będą 2 angielskie.

**Piotr Buczkowski:** English, po prostu powinno być. Nie, Justin. Chodzi mi o to, że jak są 2 wersje językowe, tak, które się różnią głównie ustawieniami, daty czy numerów, tak, czyli `US English` i `UK English`. Nie wiem jak jest to opisane. Amerykańskie i angielskie, amerykańskie, angielskie i w brytyjskim angielskim. To to nie rozróżniamy tych 2 wersji. Przy definicji wersji językowej jest tylko English.

**Kamil Dubaniowski:** Piękne.

**Przemysław Rogaś:** No dobra, czyli po prostu samo English w takim OK.

**Piotr Buczkowski:** Czyli jeżeli ktoś wpisze "chips", to nie będzie wiadomo, czy to są frytki, czy to są chipsy. Jak jak wsiądzie Amerykanin i Brytyjczyk?

**Łukasz Bott:** Czy procesory, no kłody stylu.

**Piotr Buczkowski:** Tak, bo to już się nie pomylą, tak?

**Kamil Dubaniowski:** Ale tak to to to to prawie OK, ale tak, no bo do tej pory było to o tyle. Jest to zmiana niby mała, ale duża, bo tak naprawdę wizualnie. Teraz też jestem w stanie sobie wyobrazić, zobaczyć tutaj tak już ustawiając coś, jaki to ma efekt na pozostałe, których nie ustawiliśmy.

**Piotr Buczkowski:** A możecie, możecie jeszcze możecie jeszcze wyświetlić to okienko do zmiany nazwy wyświetlanej? A do zmiany podpowiedzi?

**Kamil Dubaniowski:** Tak, to podpowiedzi. To jest `Tooltip`.

**Piotr Buczkowski:** Aha.

**Przemysław Rogaś:** Tak.

**Piotr Buczkowski:** Bo tam też za małe okienko jest dla pola statycznego.

**Kamil Dubaniowski:** No bo. Tak, to już mamy w ten sposób, czyli tutaj tak naprawdę, no bo to nie jest odpowiedź, tylko to jest tekst tego pola statyczny tekst. Więc też zmieniliśmy to. To jest na zasadzie przycisku, gdzie wyświetla się całe okienko. No i tutaj wróciliśmy do tego co było, czyli wersja językowa jest wybierana, no na liście. A na dole jest to okno edytora.

**Przemysław Rogaś:** I tutaj jest ta sama sytuacja, tylko że.

**Piotr Buczkowski:** A da się zwiększyć to okienko, bo właśnie brakowało mi tego. Tam zgłosiłem.

**Przemysław Rogaś:** Nie, znaczy da się, ale nie teraz ręcznie. Trzeba by to.

**Piotr Buczkowski:** Bo bo jest jest za małe.

**Kamil Dubaniowski:** OK. No to poprawimy.

**Piotr Buczkowski:** Chociażby ten Tooltip się w jednej linijce nie mieści, tak.

**Kamil Dubaniowski:** Czyli tutaj. Tak, tak, jedna jedna akcja uciekła.

**Piotr Buczkowski:** A to, że było szersze, żeby się...

**Przemysław Rogaś:** Rozumiem.

**Kamil Dubaniowski:** Że jak będzie szersze, to chociażby ta belka z narzędziami się zmieści w jednej linii, tak. Tutaj, no ucieka jedna akcja, dół rozciąga tabelkę.

**Przemysław Rogaś:** OK, szersze, myślałem, że ten tutaj edytor ma być wyższy po prostu.

**Piotr Buczkowski:** I szerszy i wyższy.

**Przemysław Rogaś:** OK.

**Kamil Dubaniowski:** Możemy dać większe, pomocniej tutaj nawet. Był chyba kiedyś taki pomysł, żeby tak nadal się rozciągać na cały ekran. No ja wiem, że to takie może abstrakcyjne, ale te komunikaty naprawdę czasami są długie, bo to są instrukcje albo wręcz stały tekst z regulaminem całym, a pod spodem pod tym statycznym tekstem niezmiennym masz checkbox, że zapoznałem się. I takie elementy na formularzach spraw też robimy, więc jakby tutaj wrzucić kilka punktów regulaminu, no to to już.

**Damian Kamiński:** Czy moglibyśmy domyślnie bez konieczności nawet powiększania cały ten popup dać większy, tak, żeby on zajmował tak jak teraz jednej piątej ekranu tylko jedną drugą?

**Kamil Dubaniowski:** Tak, tak, to tak, to tak to jest. No dobra, to to nie ma jakby przyjmujemy i będziemy zaraz zlecę Przemkowi. Znaczy dam.

**Damian Kamiński:** No jest jeszcze jedna kwestia też, którą pewnie trzeba zaopiekować, może niekoniecznie MVP, to są te pola zablokowane. Tak to już też z Kamilem wstępnie rozmawiałem. Tu Przemek musiałby na to spojrzeć. Jest coś takiego jak rejestr `Company`, który jest no procesem takim predefiniowanym, z którego korzystają różnego rodzaju, powiedzmy, konektory, czy też integracje systemowe i z racji tego one mają zablokowane możliwości edycji w zakresie typów nazw. I trzeba było jeszcze taką flagę obsłużyć.

**Kamil Dubaniowski:** Czyli jest taka, tak? To jest coś, co ustawia się z poziomu tylko bazy danych, czyli oznaczamy, że pole jest zablokowane i to skutkuje tym, że nie można zmienić jego nazwy, bo ona jest kluczowa w integracjach, w którym robimy, więc zabezpieczamy się, żeby klient nam nie edytował tego pola pod kątem jego ustawień. I faktycznie to jakby...

**Łukasz Bott:** Nazwy i typu chyba, nie.

**Kamil Dubaniowski:** Nazwy i typy i tego nie mamy. I wydaje mi się, że stary edytorze też nie było graficznie. To było tylko na liście.

**Damian Kamiński:** Graficznie nie było, tak.

**Kamil Dubaniowski:** On też trzeba by tutaj jakoś to pokazać, założyć jakąś kłódkę obok tego i zablokować te ustawienia, to też zgłoszeń.

**Przemysław Rogaś:** No dobra, to to wtedy to jeszcze mamy.

**Barbara Michalak:** No i to, a ta reguła tabeli? W końcu co z tą regułą tabeli?

**Damian Kamiński:** Znaczy reguła, co do zasady, ma przejść do zakładki reguły. W tym momencie jest nieintuicyjna, więc raczej przeniesiemy to tam, a tutaj może będzie jakiś odnośnik, tak jak był do tej pory.

**Kamil Dubaniowski:** Wiecie, jeśli to jest, no bo w starym edytorze też nie pamiętam czy było graficznym przejście do edycji reguł. Jeśli to jest kluczowe, żeby z tego poziomu, no mi się wydaje, że to jest raczej przyzwyczajenie, bo tak było do tej pory, ale jeśli to będzie kluczowe, to widziałbym to w tym. Właśnie niekoniecznie "zarządzaj polem", nie wiem czy pasuje, ale tam są opcje.

**Piotr Buczkowski:** Znaczy to powinno przejść do zakładki reguły, ale też zostać tutaj według mnie.

**Barbara Michalak:** Tak, bo to, żeby kompatybilne było, nie? Żeby potem nagle się nie okazało, że gdzieś tam to poznikało.

**Kamil Dubaniowski:** Dobrze, i to.

**Piotr Buczkowski:** Bo mam też pomysł, żeby mogło być kilka reguł automatycznych dla tabeli, żeby to właśnie jakoś uporządkować.

**Kamil Dubaniowski:** No to tym tak co tym bardziej tam widzę to na poziomie listy reguł, czyli będzie nowy nowy typ wyróżniony reguły tabeli.

**Piotr Buczkowski:** Znaczy, to jest już nowy typ, tylko nie jest widoczny na liście, tak.

**Kamil Dubaniowski:** Nie jest zwizualizowane, tak. Tak, chodzi mi o tak, że sekcja nowa, tak, na tej liście, tak jak teraz mamy automatyczne. Podział się robi automatyczne ręczne, no to była po prostu reguła. Gdzieś tam nadal, no ale tak, no dlatego mówię, no na razie tego nie przenosiłem, bo to niekoniecznie tutaj do edytora formularza pasuje, skoro mamy osobną zakładkę z regułami.

**Piotr Buczkowski:** Tylko beta.

**Kamil Dubaniowski:** Tak było do tej pory, że wchodząc w tabelę, miałem odnośnik do reguł, no bo to jednak nieco inny typ reguł. Do tej pory był, ale też da się tak samo, jak było do tej pory z poziomu listy do tych reguł dostać. Listy nie usuwamy, zostaje stara, więc. A na ten moment bym tego nie [?] jak ruszał, dopóki nie będziemy mieli planu na tą listę. I czy da się to tam fajnie zrobić? Dobra, to lecimy dalej.

**Przemysław Rogaś:** No to mamy jeszcze diagram. Diagram póki co wygląda tak. Wygląd pewnie będzie jeszcze się zmieniał, bo cały czas się zmienia, ale już rysuje się jakoś sensownie. Póki co za `Taxi`, no to mamy. Możemy teraz `Scroll`, `Zoom`, możemy łączyć pola. Póki co tak, etapy możemy łączyć etapy.

**Kamil Dubaniowski:** Etap.

**Przemysław Rogaś:** Bez żadnej akcji. No i tak to wygląda. Tutaj też nie ma co za dużo mówić na tego.

**Kamil Dubaniowski:** Dalsze kroki to ten prawy panel, tak. Wizualnie raczej już zostaniemy przy tym, co tutaj widać. Jest plan, żeby przełączać się między różnymi modelami. Mamy 2, które nieco inaczej rysują, ale jak na razie się wstrzymujemy. Wydaje mi się, że ten rysuje po prostu czytelniej, ładnie i tamten niekoniecznie mi się podobał, ale to zobaczymy jeszcze jaka będzie decyzja ostateczna. No i tyle. Tak też kliknięcie, oczywiście w dany etap to widać zaznacza. Strzałki wychodzące wszystkie. Do jakich etapów łączy się ten etap? W ten sposób.

**Mateusz Kisiel:** Czemu na czym? Na 2 z nich są napisy? "Kolejny etap", "Poprzednie etapy". Na innych tego nie ma.

**Kamil Dubaniowski:** Na razie to są reguły dodane, to to są przyciski na `flow` (?), które powodują przejście na ten etap po prostu na innych połączeniach, które zaprojektowaliśmy. Nie ma jeszcze reguł, które to połączenie realizują fizycznie. Czyli to jest na razie zaplanowane, że tak będziemy. Takim takim mamy diagram, tak ma wyglądać, ale jeszcze realnie nie da się takich ścieżek przejść, bo nie ma reguł, które tak się przez [?] trują. I też to, co mieliśmy do tej pory, nie jest zachowane, że właśnie jeśli połączenie między etapami jest takie na razie tylko projektowe, że narysowaliśmy, ale realnie nie da się takiej ścieżki przejść, no to linie są przerwane, a tam, gdzie już reguła faktycznie zapewnia takie przejście, no to linie są już ciągłe.

**Piotr Buczkowski:** A jak będzie nazwa reguły "Wróć do beneficjenta" i zmień etap na "wybierz wybierz z listy", to jest to, będzie się ładnie wyświetlało.

**Kamil Dubaniowski:** Postawiłem się, że zupełnie jakieś zabijanie musimy tu stać. To tam jakoś przewidzieć.

**Przemysław Rogaś:** Znaczy nie, nabędą póki co, to będą tutaj 3 kropki, po prostu, nie.

**Kamil Dubaniowski:** No na to Tooltip wtedy też. No plan pewnie jest taki, że z tego poziomu też będzie się dało kliknąć na i ewentualnie tak jak było w starym edytorze, tak, zobaczyć właśnie pełną nazwę w prawym panelu, zobaczyć tłumaczenia `Tooltip` dla tej reguły i sam kod, ale kod będzie edytowany już tak jak było w edytorze. No ale tak, no na na te reguły jeszcze nie mamy ścisłego planu, więc jeszcze zobaczymy. Dobra.

**Przemysław Rogaś:** No to tyle ode mnie.

**Damian Kamiński:** No dobrze, dzięki w takim razie nie wiem czy ktoś chce jeszcze o czymś opowiedzieć. Ja mogę pokazać... No rzecz, która widzę, że jeszcze nie działa docelowo tak jak powinna, no ale... nie to wyręczę tu Marka. Wprowadziliśmy w ramach nowych raportów podpisywanie SimpleSign, bo do tej pory tego nie było. Więc pojawia się analogiczną ikonką, cienką jak tutaj, żeby to było spójne. Zaloguj, podpisz, podpisz. Więc to, co do zasady jest spójne z tym, co było. Natomiast wprowadziliśmy też pewnego rodzaju usprawnienie, które na ten moment z tego, co przed chwilą przetestowałem, jeszcze nie działa. Mianowicie będzie można zdefiniować dostępne metody podpisywania, tak, czyli jeśli zaznaczymy SignApp, bo jakaś firma nie korzysta w ogóle z SimpleSign, tylko powiedzmy wszyscy mają Szafira, no to nie będziemy im zbędnie wyświetlać tego SimpleSigna albo odwrotnie. Jeśli wszyscy korzystają z SimpleSigna, no to nie ma sensu pokazywać SignAppa. Co po prostu będzie usprawnieniem w kontekście takiego wywoływania, bo jeśli zdefiniujemy tutaj SignApp, no to oczywiście domyślną akcją tego przycisku w zasadzie ten przycisk już powinien wywoływać to, co to, co mamy tutaj. Tak, "Podpisz certyfikatem" będzie wywoływać SignAppa.

**Marek Dziakowski:** To mam to poprawione do testów, po prostu zapomniałem przekazać wyboru tych akcji, ale to już działa u mnie. Zaraz to wrzucę.

**Damian Kamiński:** OK, no to świetnie. No w takim razie to z takich usprawnień i dalszego rozwoju.

**Kamil Dubaniowski:** A ja mam dlatego pytam, bo to zaległy się do SimplySign, czy to nie może być tak, że jak podpis za pomocą SimplySign wykryje, że jest to niezalogowany, to mnie przekieruje do logowania?

**Marek Dziakowski:** Może.

**Damian Kamiński:** A to nie było już tak zaprojektowane, nawet w tym momencie nie pamiętam.

**Marek Dziakowski:** Znaczy, no tak było w projekcie, żeby ten sposób wyglądało, ale jeżeli ogólnie jest możliwość.

**Damian Kamiński:** Znaczy na pewno, jeśli mamy wszystko tak, to to się wyświetla, no bo teraz nie wiemy, co byś chciał skorzystać. Czy chodzi ci o to, żeby tego nie było, Kamil?

**Marek Dziakowski:** Znaczy, no w tym momencie, w tym momencie.

**Kamil Dubaniowski:** Tak, żeby nie było tej opcji, no jak decyduje się na podpis? No to muszę być zalogowany. Jak wiem, że jestem, to pójdę do podpisu. Jak nie jestem, to pójdę do logowania i później do podpisu. Nie wiem, jak to działa, bo ja nie korzystałem. Nigdy nie pisałem. Nie wiem, jak ścieżka jak wygląda, czy ja najpierw muszę się zalogować, a później jeszcze raz teraz zaznaczyć?

**Marek Dziakowski:** Tak.

**Piotr Buczkowski:** Znaczy nie wiem po co jest to. Właśnie co loguj się, to powinien być ewentualny pierwszy krok. Podpisz za pomocą SimplySign.

**Kamil Dubaniowski:** Tak też myślę, no bo tak, a ja zaznaczam 50, zaznaczę z 60 i kliknę "zaloguj", i co? Później wrócę i mam zaznaczone dalej, czy muszę znowu 50 zaznaczyć i podpisać? O to mi chodzi. Nie wiem, jak ścieżka wygląda.

**Marek Dziakowski:** Można by.

**Damian Kamiński:** To może Marek wydaj tą poprawkę, która tutaj to ogranicza i przetestujemy to wspólnie z kimś z Patrycją albo z Oktawii. Zawsze nie pamiętam, która z was ma. Chyba Patrycja, tak.

**Oktawia Ostrowska:** To ja mam, ja mam.

**Damian Kamiński:** A Oktawia. Dobra, no to sprawdzimy to wspólnie i ewentualnie tu.

**Marek Dziakowski:** Dobra, to ja też.

**Piotr Buczkowski:** Jakie ustawia na szerokość kolumn w tabeli jako stałe?

**Marek Dziakowski:** Nie jest to chyba wliczane.

**Damian Kamiński:** Masz na myśli tą szerokość?

**Marek Dziakowski:** Można go sobie zapisywać.

**Piotr Buczkowski:** I tak, duża nazwa plików może być bardzo długa.

**Damian Kamiński:** No tak, to znaczy ona się chyba dostosowuje do faktycznej treści.

**Marek Dziakowski:** Tak, no tak.

**Damian Kamiński:** Tak mi się wydaje, że jeśli się wszystko mieści, to po prostu robi porównywalne równo.

**Piotr Buczkowski:** OK.

**Marek Dziakowski:** Już nie pamiętam, ale można to sobie. Można to sobie też ręcznie z poziomu edycji ustawić. Na przykład ktoś tworzy raport typu tabela i tam zdaje się można ustawić szerokości kolumn i jak to się zapisze, to użytkownikom jako domyślne te wartości, te szerokości będą pokazane.

**Piotr Buczkowski:** Bo nie wiem, czy to w starych raportach.

**Marek Dziakowski:** Tak.

**Piotr Buczkowski:** Z tych starych raportach, czy w tabeli wyświetlanej tylko do odczytu, jest po prostu dla pól numerycznych czy tam kwota, numer, czy dla dat jest ustalana `max width`, tak, żeby się akurat mieściły te wspierane wartości.

**Marek Dziakowski:** No tutaj z tego co pamiętam, no takie mieliśmy. Wydaje się, że po prostu twórca raportu może to sam zdefiniować te wielkości, jeżeli mam potrzebę po rozszerzyć to, rozszerzył i wszystkim to domyślnie się pokazuje.

**Piotr Buczkowski:** OK.

**Damian Kamiński:** Domyślnie. Poza tym. Muszę jeszcze to potestować, bo nad tym pracował jeszcze Mikołaj. Natomiast to też jest tak, że tak jest domyślnie. Myślę, że to akurat działa jak ja ustawię, że ja chcę tak. To to mi zapamięta w moim Cache'u i to zostanie tak, ale tylko u mnie już. Więc to.

**Marek Dziakowski:** Jak będziesz teraz do edycji, to powinno być znowu Polskę.

**Damian Kamiński:** Powinno być pewnie wąskie, tak. No i jest. Więc to jest tak, że każdy może tym sterować lokalnie u siebie i to jest zapamiętywane.

**Piotr Buczkowski:** OK.

**Damian Kamiński:** Natomiast no tam to to działa na pewno tylko nie działa jeszcze możliwość poprawnie z tego co mi się wydaje, żeby wyjechać poza tak gdyby tu był pole długiego tekstu, to to tu coś jest jeszcze nie dograne. Jeśli mamy odpowiednio dużo kolumn, no to wtedy pozwala nam system sterować, tym nie tak jak tu, czyli lewa kolumna kosztem prawej. Tylko rozwijając wydłużamy. Cały cały raport i tutaj się odpowiednio. Ten suwak też zmniejsza tak jak jak zwiększamy przestrzeń i tutaj tu jeszcze może coś obie ewentualnie podziałać. Natomiast jeśli faktycznie mamy dużo kolumn, to to tak działa. Tak tu jest mentalnie tylko ta kwestia przejścia, kiedy uznać, że już powinniśmy mieć suwak poziomy, a kiedy nie, to jest jeszcze do protestowania i ewentualnie wprowadzenia jakieś poprawki. To chyba mogę to pokazać o któreś już mamy ten suwak, to nie robimy tego kosztem kolejnej. Tylko właśnie tak chcemy, więc nie trzeba ratyfikować każdej kolumny. No dobrze, to pytanie Marku, może coś jeszcze chciałbyś? Jak już twoje zadania zostały wywołane może w kontekście jeszcze teraz Trust Center coś nowego?

**Marek Dziakowski:** Tutaj w Trust Center to były mniejsze jakieś takie poprawki. Do na przykład ustawiania tam daty wygaśnięcia dokumentu czy jakieś opisy do funkcji? Poprawiłem, bo niektóre funkcjonalności były niezbyt jasne. Logowanie to w sumie nie pamiętam czy to było w ramach tego sprintu czy poprzedniego. Bym mógł to pokazać, tylko no wziąłbym to odpalić wszystko. Także nie wiem, że nie mamy chwilę czasu, to mogę to odpalić.

**Adrian Kotowski:** To możemy zrobić tak, że ja mógłbym w tym czasie, bo też mam temat do pokazania, to mógłbyś Marek pokazać, a ja chciałbym to pokazać. Prawdę byłem teraz na urlopie, ale jeszcze przed urlopem tak skończyłem to przerabiać te wersje SignAppa do Maca z wgrywaniem tych bibliotek. Tutaj teraz się staram przełączyć na drugi.

**Damian Kamiński:** O to proszę.

**Marek Dziakowski:** Dobrze.

**Adrian Kotowski:** Będzie dziwny manewr. Po prostu będę podłączony do Teamsów na 2 urządzeniach, więc teraz ten drugi już staram się jak będzie działać. Tak zstąpi i... Witam, czy będziecie widzieć mój adres? Widać. OK. Sam widzę. Będę na drugim komputerze. Widać. Więc tak tutaj, więc przygotowałem kolejną wersję na Maca do podpisywania dokumentów. No czym się różni to od poprzedniej wersji, kto wie? Teraz jakby już nie musimy wskazywać, nie musimy wskazywać do dokumentów, czy nie musimy wskazywać, to robię. Tak, chcemy wykorzystać do podpisania dokumentu, gdzie w ten sposób też pośrednio wskazać, które typy wpisów chcemy wykorzystać tutaj załóżmy pierwszym sobie.

**Damian Kamiński:** Ale poczekaj jeszcze, jakbyś mógł ten poprzedni element tam, wybrałeś podpis czy jakiś dla Maca?

**Adrian Kotowski:** Jakby mamy, mamy 2 opcje, generalnie jest po prostu możliwość czy niemożliwość wpisania tej mody. Tutaj nawet pierwsza to jest ta, że możemy wybrać konkretnie miejsce. Chcemy tego robić, żeby ten nie był widoczny, ale jest też opcja druga, która zaznacza ten podpis. Rzuca tam gdzieś domyślnie na koniec, bo daje się tego dokumentu ostatniej strony, że to jest plik stronicowy na przykład tutaj. Zależy mi, żeby pokazać, wybrać to pierwsze opcje, bo to już tam mam w tym dokumencie sporo podpisów. Jest po prostu chciałem niż ten podpis, rzucić jakieś takie miejsce bardziej widoczne, że tutaj bardziej się nie da tego. Rzucić jakby inne, bardziej wizualnie, lepszym miejscu. Dobra, więc zrobiliśmy to miejsce. Wybraliśmy. Teraz jest ta nowa wersja. Czy ta aplikacja Maca na solidarnym Macu? Według pierwszej wersji, to jest taka, że wykrywa nam faktycznie te wszystkie biblioteki do podpisywania, więc możemy sobie wybrać. Którym podpisem chcemy de facto złożyć jakby podpis, gdzie ta, który delikatnie chcemy złożyć podpis, tak powiem ściślej, no i tyle. To jest akurat raczej domyślić. Będzie tutaj pojedynczy, pojedynczy sterownik, bo tam, no naszych klientów. Oni rzeczywiście mają jednym sterowniku jeden certyfikat do podpisywania, ale tutaj widzicie domyślnie wykryłem, że moim do mojego komputera tego Mac Mini jest przypięty z kart smart card z właśnie z jednym pojedynczym certyfikatem Szafir, więc. Czy też dużo wygodniejsze, bo nie muszę tego wpisywać. Nie muszę tego sterownika tam fizycznie szukać, które też jest bardzo trudne, bo on może być na przykład w jakimś katalogu aplikacji jako może być na przykład gdzieś tam w katalogach systemowych, co to jest bardzo trudne.

**Damian Kamiński:** Zwykły użytkownik biznesowy tego nie wie, gdzie to jest, tak, powiedzmy sobie szczerze, to pytanie jest inne. Powiedz jeszcze i jakie rodzaje podpisów tu wykrywamy?

**Adrian Kotowski:** Znaczy tu i to jest taka, że skoro wchodzimy od tego punktu, że obsługujemy biblioteki i te znaczy aplikacja potrzebuje biblioteki, którą dostarcza certyfikatu, więc teoretycznie możemy podpisać, czy możemy złożyć każdy taki podpis? Wystawca przewiduje bibliotekę odpowiednie, więc tutaj ta aplikacja w tym momencie wspiera 3. W sumie 3 produkty, bo 2 dostawców, że Szafir, Szafir oraz Impress, więc tutaj my wiemy, że szukać takich tych piątek, więc jakby to możemy ten sposób wykryć te podpięte certyfikaty do naszego komputera.

**Damian Kamiński:** OK. No dobra, mamy kolejne w planach w sensie te najbardziej popularne, czyli Sigillum PWP.

**Adrian Kotowski:** Wiesz co? No to nie jest problem dogadać, tylko po prostu potrzebujemy mieć. No potestować. No nie wiem, czy ja się kiedyś pytałem, czy u nas to w firmie Psiara (?) takie certyfikaty. I no ciężko jest testować coś w teorii, więc tutaj tak.

**Piotr Buczkowski:** Jakie certyfikaty?

**Adrian Kotowski:** Wszystkie rzeczy są wszystkie certyfikaty kwalifikowane, znaczy wszystkie wszystkie.

**Piotr Buczkowski:** Ja mam, ja mam PWP.

**Damian Kamiński:** No właśnie.

**Adrian Kotowski:** Tak, żeby sprawdzić tylko, że musiałbyś mieć też Maca, żeby to może tak jakoś.

**Piotr Buczkowski:** No właśnie, a nie mam Maca.

**Adrian Kotowski:** Tak, no ale taki filmowy jest. Czy ja jestem gdzieś w skoku w filmie ponoć, ale dobrze mówię, to ja chcę.

**Piotr Buczkowski:** Tutaj taka uwaga. Common Name najbardziej lepiej wyświetlać, nie cały Subject, może.

**Adrian Kotowski:** Dobra, OK, to może to mogę jakoś to poprawić, no to jakby jest na razie.

**Damian Kamiński:** Ale a co to jest `Common Name`?

**Adrian Kotowski:** To jest informacje o posiadaczu.

**Piotr Buczkowski:** No, no, nazwa certyfikatu.

**Adrian Kotowski:** Tak, no i.

**Damian Kamiński:** W sensie, czy jeśli ktoś zmierza do tego, czy jeśli ktoś będzie posiadał 2, to czy tym rozróżni?

**Piotr Buczkowski:** Nazywa się.

**Adrian Kotowski:** Będzie. To jest taki problem. W `Common Name` jest na przykład nie wiem, bo to jest mój jakby podpis na moją firmę, jakby więc tutaj widzicie, że jest na przykład nie wiem mój numer.

**Piotr Buczkowski:** Znaczy.

**Damian Kamiński:** OK.

**Adrian Kotowski:** To jest akurat dobra z tego dostawcy, to wydał mój skromny [?] więc jakby to nie jest wystarczające.

**Piotr Buczkowski:** No bo chodzi mi o to, chodzi mi o to, żeby to tak było jak w `Thumbprint` (?).

**Adrian Kotowski:** Dobra, to po prostu równym sobie.

**Piotr Buczkowski:** Bo teraz jest tak bardzo, bardzo technicznie, tak? No wiem, że to trzeba po prostu.

**Damian Kamiński:** Możemy dołożyć też kolumnę, no przestrzeń jest tak. Można wyświetlić jeszcze dodatkowo.

**Piotr Buczkowski:** Nie są według mnie to, według mnie to, co jest w obecnym SignApp, jest bardzo dobrze zrobione. Zróbmy tak samo.

**Adrian Kotowski:** To po prostu jest to, wiesz, przyjechać, bo to nie jest problem, żeby to wyciągnąć, ale dlatego, że działałoby. To jest film jak główny tej prezentacji.

**Piotr Buczkowski:** No zobaczę, OK. To nie, ale żeby to nie zostało do klientów, bo to jest mało czytelne.

**Adrian Kotowski:** Wpisuję ten film. W momencie tym momencie podpis jest jakby wątpię też, by pokazany tak na środku. Tak, no wiecie, dlaczego żebyś uwagi do tego, bo teraz generalnie chciałem to zrobić, żebym mógł tam przetestować jeszcze to, o czym wspominałem. Jest też to, że testowałem z Januszem jeszcze wcześniej. To tam wbiłem się w takim razie, że taka sytuacja, że niektórych, niektórych tych kartach może być wypadek kluczy prywatnych i też teraz to obsłużyłem, więc jakby ktoś jest druga rzecz, którą tu udało mi się implementować. Tego teraz czekam na weryfikację, jeśli myślę, że to można wizualnie tak publikacji poprawić i też to aplikacje tam udostępniłem, więc też prosiłbym o jakieś testy, może takie użytkowe, czyli jakiś feedback też w kontekście tego wszystkiego. Musiałem. No jeszcze mamy czas, żeby tutaj to poprawić. Tak naprawdę to jest bardziej przypomina trochę prototyp, a nie docelowy produkt, aczkolwiek, no już mam tu pewne sprawy, którą tam Janusz opisał, że chcemy osiągnąć.

**Damian Kamiński:** No mogą zatestować tylko osoby, które mają Maca. Logo chyba jest przesadzone. Nie wiem, czy mam aż tak dużego.

**Adrian Kotowski:** Tak, no niestety, no.

**Piotr Buczkowski:** No ale, ale mówię, zróbmy tak jak było w Windowsie i będę mieć dobrze zrobione, bo to.

**Adrian Kotowski:** To już nawet nie jest ten taki delegat, ten taki. Więc to jest do Windowsa tego starego i to teraz jakby nie jest najbardziej wspierane w tym Macu.

**Piotr Buczkowski:** Nie, ale.

**Damian Kamiński:** Ale nie, Piotrowi chodzi tylko o wygląd, tak?

**Piotr Buczkowski:** Pokażę tak. No każdy ekran.

**Adrian Kotowski:** Dobra, to wyłącz.

**Piotr Buczkowski:** Widać.

**Adrian Kotowski:** Dobra, to mogę to OK. Jakoś przerobić tak, żeby było, czy nie chcemy iść podobnie?

**Piotr Buczkowski:** Znaczy tutaj jedna z jednostek mi tylko o tobie wkurza. Zawsze ta klikam zamiast tak i wybierz.

**Adrian Kotowski:** To tak samo mam jeszcze.

**Damian Kamiński:** No to można też szczegóły dać w małym ikonce i tak w kółeczku, żeby to nie był w formie przycisku.

**Piotr Buczkowski:** Tak, tak, tutaj to jakieś tutaj wybierz.

**Kamil Dubaniowski:** Znaczy.

**Adrian Kotowski:** Też różnica w ogóle, no bo tutaj ten ten SignApp po prostu pobiera te certyfikaty. Mogę znów certyfikatów, a aplikacja nowa Maca.

**Piotr Buczkowski:** Ale chodzi mi, chodzi mi o wygląd, wygląd.

**Adrian Kotowski:** Dobra, no to dobra, to?

**Łukasz Bott:** No oczywiście wygląd nam z dokładnością tych.

**Adrian Kotowski:** No po prostu.

**Piotr Buczkowski:** Że właśnie jest tylko jest tylko Common Name, tak.

**Adrian Kotowski:** Ale też zauważyłem, także tu masz.

**Piotr Buczkowski:** Wydawcy, data ważności.

**Adrian Kotowski:** Sporo certyfikacji musi mieć taką samą nazwę po prostu i to jest jakby.

**Piotr Buczkowski:** I jeżeli, jeżeli masz. Ale data ważności zwykle była inna. Tutaj jest na przykład, nieważna, tak, bo mam "pokaż wszystkie certyfikaty". To właśnie mój PWP nieważne. Ale oczywiście można nim podpisać, tak. No ale dla człowieka zwykłego człowiek zwykły w takim technicznym co tam wyświetlasz to on się tam nie połapie, tym się połapie. Jakby miało 2 razy `Piotrkowski`, w tym jedna data ważności na czerwono, że 2021 tak.

**Adrian Kotowski:** Tam złożył jakiś, nie wiem. Zgłoszenie o stworzył zgłoszenia o polskich projektach graficznych. Tam jeszcze ustalę to więc, no.

**Piotr Buczkowski:** No tak, tak, tak.

**Kamil Dubaniowski:** Warto by było tak ujednolicić.

**Adrian Kotowski:** Dobra, dzięki, ale to jakieś wskazówki, coś wolne?

**Piotr Buczkowski:** No nie, nie, nie, to nie niech to będzie, niech to będzie spójne, tak.

**Kamil Dubaniowski:** Zgadzam się, tylko tutaj też bym trochę dopracował.

**Damian Kamiński:** Przy czym? No właśnie tak trzeba to uspójnić z wyglądem tak jak tam kolory pomarańczowe, powiedzmy, że to było też spójne z Gitem, no.

**Kamil Dubaniowski:** Czy tutaj jest spory? No na przykład przeczytajcie sobie instrukcję. Widzicie tą ikonę z lewej strony, bo ja nie.

**Piotr Buczkowski:** Bo to.

**Kamil Dubaniowski:** Nie, "wybierz interesujący cię certyfikat, używając pola wyboru z lewej strony".

**Piotr Buczkowski:** Aha.

**Kamil Dubaniowski:** Gdzie jest to pole wyboru z lewej strony?

**Damian Kamiński:** No trzeba to zaprojektować po prostu i tyle.

**Kamil Dubaniowski:** No dobra, to to weźmiemy na warsztat. Żeby było spójnie, tu i tu, tak.

**Adrian Kotowski:** To tyle, jeśli chodzi o mnie, to już oddaję głos.

**Marek Dziakowski:** Dobra, to jeszcze mamy chwilę pokazać, czy kończymy.

**Łukasz Bott:** To jest dziesiąta, ale to, ten, jeżeli to 2, 3 minuty zajmie, to dawaj Marku.

**Marek Dziakowski:** Zajmie minutę. Widać. No to teraz przy. Trust Center będzie dostępna możliwość logowania się za pomocą. Tu już nie trzeba będzie tutaj podawać adresu email, to oczywiście jest tylko dla osób z dostępem serwisowym. Jak się kliknie tam jest przekierowanie do autoryzacji w Azure, tam to wszystko sprawdza, no i. Koniec. Jesteśmy zalogowani.

**Łukasz Bott:** Wiesz co, to taka uwaga, jakbyś jakbyś napisał, że "zaloguj kontem Microsoft" czy coś w tym stylu, bo w tej chwili tak sugeruje jakby to Microsoft był producentem tego.

**Marek Dziakowski:** Dobra, rozmawiamy o tym.

**Damian Kamiński:** To znaczy w ogóle nie tyle, co zaloguj, co? Zobacz, jak wygląda nowe okno logowania do.

**Piotr Buczkowski:** Kontem Azure.

**Damian Kamiński:** Znaczy, według mnie powinniśmy to zrobić tak jak logowanie do AMODIT-a, czyli tam jest. "Zaloguj za pomocą" kafelek jest zakreślony ramką i to powinno dokładnie w taki sam sposób wyglądać pod spodem.

**Piotr Buczkowski:** Nie mój.

**Łukasz Bott:** Dokładnie tak, tak to.

**Marek Dziakowski:** OK.

**Łukasz Bott:** Myślę, że wszystkie te interfejsy do wprowadzania tych właśnie, nie wiem. Loginów, nie loginów, tutaj PINów do Trust Center, to powinny być w miarę w miarę spójne, tak dla wszystkich tych naszych narzędzi, tak to, które mamy.

**Damian Kamiński:** Tak więc po prostu weź wzór ze strony logowania.

**Marek Dziakowski:** No tutaj tak.

**Łukasz Bott:** Logowania, tak, i tak będzie najlepiej.

**Marek Dziakowski:** Dobra.

**Damian Kamiński:** No dobra, jesteśmy chwilę po czasie, czy ktoś jeszcze coś ma ważnego?

**Piotr Buczkowski:** Mogę ja jedną rzecz pokazać, no to też może wam się przyda bardziej.

**Damian Kamiński:** Proszę.

**Piotr Buczkowski:** W końcu zrobiłem to coś, tak? Teraz mamy takie coś, tak, takie w tabelki z `CaseDefinition`, że pole typu `varchar` było i od pewnego czasu nowe pole zrobione `Medium Text` tylko te co były dostępne, to zostawały `varchar`. W końcu to zrobiłem obsługę, że. Generuje tak. `DatabaseAdmin`. Po zaznaczeniu bazy po naciśnięciu `Change text fields` generuj. Sam tego nie robi, bo to może trwać długo. Generuje skrypt, który zmienia wszystkim polu, wszystkim, dla wszystkich pól typ `varchar` na `Medium Text`. Nie tylko tej `varchar`, ale też tych takich na przykład `CaseMessage` for `From His`. Czy inne, które nie muszą być tekstowe?

**Damian Kamiński:** Systemowe.

**Piotr Buczkowski:** Systemowe. O tak. To dodatkowo też na MS SQL na MySQL-u pola typu. Tekst były typu tekst, co okazało się, że jest za małe. Sam tekst też powinien zmieniać na `Medium Text`. Powinno powinno gdzieś to być, ale nie widzę szybko.

**Damian Kamiński:** Ale to ma wpływ tylko na to ograniczenie wydajnościowo też to coś poprawia.

**Piotr Buczkowski:** Nie.

**Damian Kamiński:** OK. Czyli po prostu pozwala wpisywać dłuższe.

**Piotr Buczkowski:** Teoretycznie teoretycznie i wręcz może odrobinę pogorszyć. Ale tak, po pierwsze można dodać więcej kolumn. A po drugie już nie ma tego ograniczenia, na przykład na polu Link, gdzie bez problemu Link do SharePointa czy coś przekracza te 256 znaków.

**Damian Kamiński:** OK. Ale to co powiedziałeś, to w związku z tym zalecenie jest takie, żeby to zmianę wykonywać po prostu ręcznie i poza godzinami pracy.

**Piotr Buczkowski:** Tak, tak, bo oczywiście.

**Damian Kamiński:** Musi być wyłączona aplikacja, tak.

**Piotr Buczkowski:** Bazy danych, ograniczony dostęp do aplikacji, czyli wyłączona, wyłączona witryna, wyłączona usługa. Wtedy to zmieniamy, tak, no bo mówię na dużej bazie wykorzystywanych od wielu lat, może to trwać i pół godziny.

**Damian Kamiński:** No dobra, przygotujesz Piotrze, do tego jakąś instrukcję.

**Piotr Buczkowski:** Jest, jest funkcja.

**Damian Kamiński:** Jest już dobra.

**Łukasz Bott:** Dobra, to trzeba to.

**Damian Kamiński:** No to w piątek o tym zakomunikujemy. No super, to znaczy. No to, że to będzie może minimalnie mniej wydajne, ale chyba większym wyzwaniem było to, że te pola się u niektórych klientów nie mieściły, więc to jest zaleta.

**Piotr Buczkowski:** Znaczy tutaj tak zwaną typów pól tekstowych. Ministerstwie Sportu już to dawno zostało zrobione, bo to ten przycisk generowanie to do skryptu przygotowane. Ministerstwo Sportu. Teraz też dodałem chociażby obsługę Microsoft SQL. Musiało dobrze, tak. Jakieś?

**Łukasz Bott:** Dobra, czekaj, a teraz tak. Mamy, no to w tej chwili mamy wirtualne pole tekstowe, no bo tak to trzeba nazwać te AMODIT-owe krótkiego tekstu. Rozumiem, że tam to ograniczenie, że bo tam się wpisuje ilość długość, ile tam znam. Tam było. 255 ma domyślnie ustawione. To rozumiem, że to pozostaje tak w mocy.

**Piotr Buczkowski:** Tak, tak, pozostaje.

**Łukasz Bott:** I i tu, czyli.

**Piotr Buczkowski:** Tyle, że da się tyle, że ta na przykład z reguły da się wpisać więcej.

**Łukasz Bott:** Że z reguły da się wpisać więcej.

**Piotr Buczkowski:** Tak.

**Łukasz Bott:** OK. No to może tutaj.

**Piotr Buczkowski:** Znaczy w zasadzie teraz poza wyglądem nie ma różnicy pomiędzy polem tekstowym, długim a krótkim. Od strony bazy danych, tak.

**Łukasz Bott:** OK. Dobrze.

**Piotr Buczkowski:** Tu też gdzieś na środowisku testowym, jeżeli będzie z tym problem, to warto przeprowadzić taką zmianę. No to tyle.

**Damian Kamiński:** No dobra, czy ktoś nie powiedział czegoś istotnego? No to kończymy w takim razie. Dzięki.

**Łukasz Bott:** Dzięki.

**Damian Kamiński:** Miłego dnia. Cześć.

**Marek Dziakowski:** Na razie.

**Kamil Dubaniowski:** Cześć.

**Oktawia Ostrowska:** Cześć.

**Filip Liwiński:** Cześć.

**Mariusz Piotrzkowski:** To jest.

**Adrian Kotowski:** I cześć.

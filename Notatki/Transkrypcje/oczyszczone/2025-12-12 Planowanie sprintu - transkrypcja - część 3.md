**Data spotkania:** 12 grudnia 2025, 09:04 - część 3

---

**Kamil Dubaniowski:** Na...

**Janusz Bossak:** Certyfikacje, czy jakby to nazwać? Dobrze. Potem jest na pierwszy kwartał, bo tu jeszcze mamy 2 rzeczy. Ten podłączenie tego Google'a i to Mateusz zrobił. Dobrze by było się dowiedzieć, czy klient ten Vasco coś tam z tym protestował, czy mamy jakiś feedback? Nie wiem czy to Daniel pan zbiera, czy właśnie nie mamy jakoś tak, nie ma prostego kanału, nie, że tak komunikacyjnego do tego klienta. To znaczy Mateusz się coś tam kontaktował, ale jak to programista, nie, tak. Może lepiej programisty nie wysyłać do klienta? I brakuje mi trochę opiekuna tego tematu po naszej stronie. To Vasco Google, żeby tym się zaopiekować. Może Łukasz, ty byś się tam jeszcze przez jakiś czas tym zajął. To też dotyczy ocena, nie? Więc chodzi zaopiekowanie takie, żeby wiedzieć, co się, że tak powiem, w temacie dzieje, nie. Czy klient przy testowo, czy nie przetestował, czy ma jakieś uwagi, czy jeszcze by coś chciał i tak dalej. Tam się niby Daniel komunikuje z nim, ale no od nas Mateusz, od Mateusz Kisiel.

**Łukasz Bott:** OK. Dobry. Nagle w drugiego chyba w tym momencie nie ma, tak, no bo nie, nie ma dzisiaj, a Mateusz też chyba to dopiero...

**Janusz Bossak:** No właśnie. Ale to chodzi mi o tam przyszły tydzień, tak, żeby się zorientować właśnie w tym następnym sprincie. Teraz jeszcze pięćdziesiątym pierwszym.

**Łukasz Bott:** Dobra, dobra.

**Janusz Bossak:** Co tam w tym temacie się dzieje? Drugi temat Mateusza to jest ogólnie rzecz biorąc serwery MCP. Model, kontekst, protokół, bo tu chcemy doprowadzić do sytuacji takiej. No dobrze, to najpierw 2 słowa, a potem wyjaśnienie, żeby można było odpytywać AMODIT o coś. No czyli na przykład o moje urlopy albo jaka była ostatnia faktura albo coś tam różne rzeczy, tyle że najpierw. No musimy nauczyć się. No właśnie jak to robić, nie, znaczy, żeby nie zabić wydajności, żeby taki serwerem sypie, nie strzelał po AMODIT jak szalony bez sensu. Więc to trzeba dobrze zaprojektować i w przyszłym tygodniu we wtorek przed wigilią o piętnastej, czy ma czternastej 30 jest za zaplanowane spotkanie właśnie z udziałem Mateusza. Między innymi on przyjeżdża z Wrocławia na tą wigilię. No i poprosiłem go, żeby był trochę wcześniej. Będzie Przemek, ja, Piotrek Buczkowski w zaprosiłem też Łukasza Poskrobko, bo na widzę ostatnio bardzo duże osiągnięcia w tym ja. I naprawdę tam się ogarnia z tym. Więc tutaj sobie porozmawiamy na ten temat i trzeba po prostu wypracować metodologię podejścia do tego tematu wdrożenia tych serwerów MCP dla AMODIT, tak, żeby to Piotrek Buczkowski pytam się też przydał oczywiście, tak, bo to jest kwestia wydajności, jakości, bezpieczeństwa. No wszystkich tych elementów, które tutaj są. To sam hasło to jeszcze za mało, nie? No dobrze, to jest na pierwszy kwartał, że tam chcemy te MCP zrobić. No a teraz już w tym tygodniu, w tym sprincie następnym będziemy już o tym rozmawiać. Kolejny temat, który chcemy zrobić, dokończyć, zrobić, nie. To jest to generowanie dokumentacji, bo to wiele osób o tym mówi, że jest to ważne ze względu na to, że wielokrotnie się tą dokumentację projektową czy po wdrożeniową generuje. Na przykład teraz takim locie, tak. To po jednym kliknięciu mielibyśmy dokumentację, no może nie będzie ona w 100 procentach idealna od razu, ale przynajmniej 80% czarnej roboty będzie zrobione. A ktoś tam to przeczyta i coś najwyżej tam doprecyzuje to co to ja i wymyślili, nie? Więc to jest temat też dla Mateusza na najbliższy czas. Tak, tyle, żeby to dobrze zrobić. W moim przekonaniu to musi być bardzo aktywny udział i Mateusza Kołakowskiego i Daniela Grzeszki. Bo ich ludzie będą odbiorcami tego, znaczy klient będzie odbiorcom oczywiście. Ale to ich ludzie będą generować. Dla Daniela Grzeszki, przepraszam, serwisu, no to będzie dokumentacja, z którą będzie można się po prostu zapoznać. Tak, będzie wiadomo. Co ta instalacja robi, tak, że tu jest tam nie wiem 5 procesów, te robią to, te są zintegrowane z takimi usługami, a te z takimi, te korzystają z tego, a te ze źródeł danych, a też czegoś tam i tak dalej. Bym chciał, żeby to była taka dokumentacja, którą się do sensownie przeczytać. I dowiedzieć właśnie, jakby zobaczyć całą cały obraz tego wdrożenia, co tam się dzieje. Więc to taki jest cel tego. Budować to pewnie trzeba po kawałku. Jeżeli osobno same procesy, osobno raporty, osobno ustawienia systemowe, osobno źródła danych, które są podpięte na przykład do jakiejś pól typu odnośnik. Różnego rodzaju powiązania między procesami i tak dalej i tak dalej. Więc to trochę się wiąże z tematem tego przenoszenia. Z kolei procesu między środowiskami to mamy wpisany na pierwszy kwartał przenoszenie procesów między środowiskami. Pełen wizard do eksportu i importu wszystkich powiązanych elementów z obsługą konfliktów, nadpisywania, tak dalej. I tym czasie według mnie zabrać zająć od początku stycznia, żebyśmy to w kwartał dowieźli. Mieliśmy to zrobić w tym roku, nie zrobiliśmy. Więc potrzeba zrobić. Są wpisane na pierwszy kwartał te prace koncepcyjne nad podłączenie tego Power BI i Tableau, czyli inaczej obsługą protokołu Open Data, żeby można było transferować dane że AMODIT do tych systemów analitycznych.

**Kamil Dubaniowski:** Czy tutaj moja uwaga, żebyśmy nie poszli znowu? Jesteś, czego nikt nie użyje? Dyskutowałbym z Przemkiem ten wątek, bo już ładowaliśmy się w raporty AMODIT, raporty, a teraz przez jeden gdzieś tam pomysł Piotra Grzeszki będziemy się ładować w coś, co no mamy na to klientów. OK.

**Janusz Bossak:** Reus tak chce, iden tak chcę, są klienci.

**Kamil Dubaniowski:** Dobra, no to to jest dla mnie okej?

**Janusz Bossak:** To wynika trochę z tych spotkań farmingowych, aczkolwiek rozmawiałem z Przemkiem. Ze Przemek, skąd ci wszyscy klienci nagle to chcą? No wie, czy to nie jest tak, że tym to mówisz, że to byłoby fajne i nagle oni to chcą. Bo wiesz, nagle, nagle z 3 kolejnych spotkań ostatnich spotkań farmingowych klienci chcą MCP. Miał sporą wiedzą w ogóle co to jest MCP, nagle się tacy świadomi wszyscy zrobili.

**Kamil Dubaniowski:** Ula kiedyś na naszą prośbę robiła, nie pamiętam co to był za wątek. Robiła badania z klientami, a już wiem, OCR do odczytu dokumentów kadrowych, czy oni by to chcieli i ile są za to skłonni zapłacić? Moim zdaniem od tego będzie mnie wyjść, bo to, że Przemek jakich jakby powiedział, że oni to chcą, to jedno, ale jak później dostaną cenę, to zostaniemy znowu z produktem, którego nikt nie kupi.

**Janusz Bossak:** No dobrze, no to to jest temat do rozpracowania, tak jak widać nie tylko technicznego, ale koncepcyjnego. Da się zrobić krótkie badanie rynku, wyjść? Wtedy klientów sprawdzi, czy potrzebują i tak dalej. No i to jest tyle, tak, tu jest jeszcze wpisane na ten pierwszy kwartał eksport do archiwów państwowych, generowanie paczek z walidacją, ale bez integracji API i to jest rzecz, którą po stronie lotu właściwie nie my, bo w zasadzie chyba tutaj dla nas, jako działu do działu rozwoju za bardzo nie ma zadań.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Ale musimy się temu przyglądać, bo chodzi o to, żeby konsultanci taką paczkę tam skonstruowali. I to jest ewentualnie jakiś obszar, który możemy coś pomóc. Ale trzeba to dobrze zrozumieć i to konsultanci pewnie nam powiedzieć. Na czym polega skonstruowanie takiej paczki? Czyli co tam się do niej powinno wstawić? Jaki metadane powinny być, tak dalej i tak dalej. To bym chciał dowiedzieć się od konsultantów i oni powinni nam powiedzieć: tutaj macie, zobaczyliśmy, konstruujemy takiego XML, nie, i czy wy, czyli my jako dział DEV, możecie nam pomóc, tak, czyli zrobić coś na przykład taki okienko z jakimś tam drzewkiem tych spraw, gdzie można coś zaznaczać, że te sprawy mają wejść, a te nie mają albo coś tam. Bo coś tam, ale i chciałbym, żeby to oni wystąpili z jakby inicjatywą tego, co oni potrzebują. W którym miejscu my jako dział DEV mamy im coś zrobić, pomóc w sensie jakiejś usprawnienie po stronie AMODIT, żeby nie trzeba było robić jakieś rzeźby w regułach, sklejając se jakieś XML, jakieś dokumenty i tak dalej i tak dalej, no.

**Kamil Dubaniowski:** W mojej ocenie naj pewnie i skończy się na tym, czego nie przełożyliśmy z wyszukiwania zaawansowanego, czyli żeby można było z poziomu raportu wskazać. Użyj tego szablonu XSLT i na podstawie zaznaczonych spraw wygeneruj mi zbiorczej ksana. Spodziewam się, że tego nam będzie brakowało.

**Janusz Bossak:** Ale tego odwołanie już robiła przecież.

**Kamil Dubaniowski:** Tak mi się też kojarzy. Nie wiem czy to skończona jest.

**Janusz Bossak:** No właśnie nie wiem, czy jest skończone ten tak użycie szablonu XSLT do do generowania czegoś.

**Kamil Dubaniowski:** Bo do tego to się sprowadzi. W teczce jest o tyle łatwo, że my mamy teczkę danego pracownika w ramach pojedynczej sprawy, takie sprawa teczki. W sumie tu będzie podobnie, tylko wydaje mi się, że do archiwów państwowych będą przekazywane zbiorczo sprawy, czyli tak jakby patrząc na e-teczkę teczki pracowników zaznaczasz, które chcesz przenieść i teraz my powinniśmy na bazie tego zobaczyć, jakie tam w tych teczkach są dokumenty i skleić to w jeden XML, no bo przekazujesz całą sprawę. Państwowego nie pojedyncze dokumenty, a w kontekście teczki to jest personalne, przekazujesz teczkę pojedynczego pracownika, ją eksportujesz ją, przygotowujesz, a tu tu wchodzimy trochę poziom wyżej, czyli będzie to trzeba robić z poziomu modułu raportowanego.

**Janusz Bossak:** No to trzeba rozkminić, tak, to trzeba rozkminić.

**Kamil Dubaniowski:** Dobra, znaczy to jest jakby kontynuacja mojego tematu, więc to to ja biorę jako swój cel, te procesy, przenoszenie między środowiskami. Nie wiem, trzeba Damiana pytać, jaką się czuję na siłach, ale on to już zaczynał, więc też nie chcę się tam w to stres w połowie wpychać.

**Janusz Bossak:** Co tam?

**Kamil Dubaniowski:** Bo on już robił ten powiązania z Mariuszem. W tym kontekście to był taki zalążek start, właściwie, no i albo to jakoś podzielić na mniejsze wątki, gdzie będziemy się po prostu tym wymieniać. Albo... Albo będzie to cel Damiano.

**Janusz Bossak:** Znaczy. Tutaj, no OK, według mnie tu jest kilka warstw tego, znaczy jest warstwa jakby logiki tego przenoszenia i tu według mnie konieczny jest Piotr. Czyli rozkminiania tych wszystkich powiązań, co musi być pierwsze, że trzeba mieć takich i ****, żeby można było raport podpiąć pod proces, proces powiązany i tak dalej. No czyli ktoś na poziomie architektonicznym musi to, że tak powiem, wykoncypować. Potem już realizacyjnie mogą być już tam pozostali to robić, tak, ponieważ będziemy to robili.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Już nowym. Czyli to, że procesów, no to absolutnie to musi być zrobione Reactową. No i pewnie jakieś okno, może jakieś drzewko? Takie powiązań prawdopodobnie wszystko to, co było robione w ramach tych zależności, to co Mariusz Piotrkowski robił, tak, z Damianem, czyli mamy te wykrywanie zależności danego procesu. Prawdopodobnie to się przyda w dużym stopniu. No ale potem jest cała warstwa z kolei importu, tak, bo to eksport to jest jedno, czyli wykrycie wszystkich zależności, ale potem import, żeby kontrolować to, co próbujemy wgrać na to, co już tam jest w tym środowisku, tak, i żeby to dobrze przemyśleć. Więc to jest, no to jest, to jest według mnie, to jest główny cel tego pierwszego kwartału i naprawdę na to nie ma dużo czasu, a jest dużo roboty i to trzeba tutaj powołać. Według mnie zespół, który się tym zajmie. I od początku tam od pierwszego dnia pracy w styczniu brać się za to intensywnie, kwarty wyłączenie twardy koło sprint po sprincie ustawiać cel i żeby to ten postęp był widoczny. To się nam nie rozjechało jak w zeszłym roku, że chcieliśmy i końcu. Idź.

**Kamil Dubaniowski:** Dobra, znaczy, no ja spodziewałem się, że Damian to nie ma co się oszukiwać i tak będzie jeszcze zaangażowany w te repozytorium. To nie jest temat skończony i pewnie będziemy to kontynuować jeszcze przyszłym roku. Ten mój cel dotyczący archiwów państwowych, no to powiedzmy, że to na pewno nie jest cel taki, który zajmie kwartał. To jest raczej kwestia sprintu 2 zewnątrz, jak tam konsultanci będą współpracować i co wypracujemy? Jakie potrzeby przed starem może tak? A to no w takim razie, no nie wiem, pewnie przejmę albo jakoś podzielimy na 2. No chyba, że jest coś innego, podobnie dużego to tego.

**Janusz Bossak:** Bo mamy jeszcze ten serwer MCP, tak, tam jest kilka takich drobiazgów do zrobienia, no i oczywiście to jest ten temat twój, czyli edytor diagramów. Kredyt.

**Kamil Dubaniowski:** No OK, to to potencjalnie mogę przejąć, bo dałem to robił reguły i diagram to mógłbym wziąć na siebie w takim. Nie wiem, czy reguły są planowane też na ten kwartał. W sumie nie, nie otworzyłem tego sobie pliku, ale wiem, że Damian już robił jakiś projekt, to potencjalnie jakby już łatwiej będzie mi do tamtego wejść, bo tamto nam prezentował. Też mu pomaga ujednolicić to do tych moich widoków, tym bardziej, że no właśnie tam będzie dużo znów tych samych widoków, bo będą te same tabele, więc mi będzie łatwiej. Pewnie trzymać to spójnie wizualnie, żeby to wyglądało z innymi.

**Janusz Bossak:** No, no, no, no.

**Kamil Dubaniowski:** Więc zbieram jej te liste pól reguł przejąć. A wtedy tam no niech zamyka i angażuje się w te przenoszenie proces.

**Janusz Bossak:** No OK, dobra. To się jeszcze mamy.

**Kamil Dubaniowski:** Nie, ja bym ten design anulował dzisiejszy, no bo i tak nic nowego nie robimy w tym sprincie. Jedynie co to może jak mi się uda, to na koniec dnia wam pokażę ten panel edycji dostępności pół, żebyście rzucili okiem, ale to nie wymaga już się gdy dyskusji. Mamy nazwę, zmienił układ minimalnie i poprawiam ewentualnie tamte instrukcje, opisy, które się tam edytuje. Także nie ma co na design się o łączyć.

**Janusz Bossak:** Dobra, no ja mogę wam pokazać potem ten mój jakby bazy wiedzy o projektach, jak to wygląda w tej chwili. Jestem już tak prawie na bieżąco, że ten tydzień tamte nowe transkrypcje prze twarzą, ale już to zaczyna jakoś tam wyglądać, nie.

**Kamil Dubaniowski:** Jak coś tam, czy w ramach tego dywanu, czy dzwonisz nas jak będzie gotowa, to złapiemy.

**Janusz Bossak:** No to może w ramach tego designu tam chwilę to zdziwiło.

**Kamil Dubaniowski:** Tak, dobra, no to zostawiam, to się łączę teraz tam dla mnie wydzwaniała odnośnie jakiejś ankiety tej sygnalistów.

**Janusz Bossak:** OK, no dobra, dzięki.

**Kamil Dubaniowski:** Dzięki.

**Łukasz Bott:** Nożyczki.

**Janusz Bossak:** Hej.

**Janusz Bossak:** zatrzymano transkrypcję

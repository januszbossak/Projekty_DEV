**Transkrypcja**

12 sierpnia 2025, 11:41AM

**Janusz Bossak** rozpoczęto transkrypcję

**Mateusz Kisiel** 0:03  
Ani zmu pobierania listy organizacji na podstawie tego tworzenia już tych tabelek w odpowiednich bazach, tak.

**Janusz Bossak** 0:14  
Żeby nie powstał.  
Czy inaczej mówiąc, no kompletnie tego nie promujemy, w ogóle nie chwalimy się tym stanie zrobione dla filmu i tylko w zimie pewnie to pozostanie.

**Mateusz Kisiel** 0:29  
Znaczy ogólnie w wersjach on premises to można dawać tak tylko na chmurze trzeba by to przystosować jeszcze.

**Janusz Bossak** 0:37  
Czy chodzi mi też taką taką kompatybilność? To jak ludzie zaczną z tego korzystać?  
W takim filmie i powiedzmy, że im się to spodoba i tam będą setki, już jakby wiadomości, czatów i oni będą z tego korzystać.  
No i przyjdzie teraz aktualizacja za pół roku.  
To, żeby nie było tak, że mamy wersję osobną dla filmu, którą musimy utrzymywać.  
I osobną wersję dla ludzi, którzy mają to w chmurze czy nie wiem w polfarmex tu czy gdzieś indziej.

**Mateusz Kisiel** 1:08  
Nie no prawdę podobnie to się skończy tak, że wtedy po tej aktualizacji jak już zrobię tą wersję chmurową będą musieli w Niemiec po zmieniać konfigurację. Właściwie konfiguracja trochę zmieni.

**Piotr Buczkowski** 1:19  
No właśnie tego nie nie tak, nie tak nie powinno być.

**Mateusz Kisiel** 1:20  
Ale jakby wszystko.

**Janusz Bossak** 1:26  
Znaczy boję się takich właśnie rozwiązań. Wiesz, połowicznych nie, że taki jest zrobione coś na teraz.  
I o ile to nie chwyci i oni nie będą z tego korzystać, no to pół biedy, bo to tam wygaśnie za pół roku czy za rok stwierdzą, że to właściwie im nie było potrzebne i tylko tak się bardziej ofertową czepiali, że to chcą, ale jeżeli im się to spodoba.

**Mateusz Kisiel** 1:44  
Znaczy tak jakby.

**Janusz Bossak** 1:48  
No i co wtedy nie?

**Mateusz Kisiel** 1:49  
W wiadomości tam żadnych nie stracą, tak w bazie tam myślę, że w tabelkach żadnych informacji nie stracą przy aktualizacji. No to myślę, że w jakimś tam u RL jakiejś konfiguracji mnie, żeby myślę sobie zmienić, ale to jest kwestia mnie. Mam 10 minut przykładowa.

**Piotr Buczkowski** 2:01  
Znaczy.  
Teraz tak działa, że są 2 możliwe konfiguracje, ale konfiguracja lokalna, premise albo chmurowa.  
Samochód wykrywa tak, w której konfiguracji działa i.

**Janusz Bossak** 2:15  
I wie.

**Piotr Buczkowski** 2:15  
Nic nie trzeba zmieniać, tak?  
Tak samo tutaj powinno być.

**Mateusz Kisiel** 2:21  
No mogę ci pokazać jak wygląda konfiguracja. Obecnie nam się takie głównie bezpieczeństwem konfiguracje, więc myślę, że.  
No ale tak no może się uda zrobić bez tych zmian.

**Piotr Buczkowski** 2:36  
Znaczy.  
I tak jak mówię wam jest tak, że sprawdza tak czy jest pis.  
Dopadły tej konflikt bazy określającej listy organizacji chmurowych.  
Czy jest po prostu bezpośredni Link do bezpośredniego najczęstszych do bazy danych? Czy czy znaczy, że jest jedna baza danych?  
W zależności od tego.  
A tam jeszcze jak jest ta?  
Baza chmurowa to jest jeszcze parametr, że.  
Powiedzmy adresy mają postać gwiazdka modecom, czyli gdzie gwiazdka to jest?  
Identyfikator czy tam nazwa?  
Organizacji, w której pracujemy na przykład astra fox test.  
Nie wiem walut, cokolwiek tam innego, tak?

**Mateusz Kisiel** 3:25  
W tym momencie na przykład.

**Piotr Buczkowski** 3:25  
A arwa arwa ladaco tak.

**Mateusz Kisiel** 3:30  
W tym momencie konflikt zawiera w sobie connection string do bazy danych, w której się zapisują te tabelki. No to docelowo w nach może będzie to także zamiast tego connection stinga, który bezpośrednio wskazuje.

**Piotr Buczkowski** 3:42  
Nie było, nie było w tym nie mów.  
Znaczy, czy równie dobrze to może być connection string do bazy istniejącej tak do baza modlitw, które będą tabela.

**Mateusz Kisiel** 3:46  
O czym?  
No tak, tak, tak jakby o to mi chodzi, że w tym momencie trzeba ustawić konkretnie konieczny stringa. W przypadku chmury będzie tak, że ten konieczny string będzie się pobierał z tej bazy, którą tam pokazywałeś kiedyś.

**Piotr Buczkowski** 4:07  
Czy nazwy?  
Kolumb tabelach sa tak zgodnie z tym naszą konwencja modowo czy po prostu tak jak entity tajów framework sobie zrobiło?

**Mateusz Kisiel** 4:18  
To jest sam wybierałem nazwy kolumn no i no nie, nie robiłem tych konwencji, to mogę w sumie zmienić nazwę.  
Chociaż no teraz już ciężko zmienić tę nazwę to nie wiem czy jest sens. Możemy przyjąć przygotować te 3 tabelki będą będą oddzielnie po prostu w innych konwencji.

**Piotr Buczkowski** 4:33  
Jak jak się te tabelki nazywają?

**Mateusz Kisiel** 4:36  
Mm już ci mówię.  
Czat mesy.  
Czat i czat luzer.  
Ale no one jeszcze nie są, nie są w alfa, to jest osobna baza.

**Janusz Bossak** 4:56  
Dobrze się u nas.

**Mateusz Kisiel** 5:03  
A zaraz zobaczy, nie są chyba już dodane dodane samochody w 0 2.  
O k ja zrobiłem chyba osobną.  
Osobną bazę top w alkomat 0 2 i nie są tabelki obecnie.

**Piotr Buczkowski** 5:26  
Jest jeszcze luks juz zer.

**Mateusz Kisiel** 5:29  
Tak looks to są jakieś strony.

**Piotr Buczkowski** 5:31  
Mag historii.

**Mateusz Kisiel** 5:33  
Tak, to jest historia migracji, bo tutaj się entity framework, inaczej zarządzanie migracjami.  
Uważam, że ten mechanizm informacja jest lepszy.

**Piotr Buczkowski** 5:54  
A po co jest tabela jęzor?

**Mateusz Kisiel** 5:58  
Strzałem mieć kopię tych informacji, jakieś użytkowników i w razie czego może jakieś dodatkowe informacje w tym wyrzucić, ale być może ona nie będzie nam potrzebna, więc ja może nam to usunę.  
I też wszystkie te wiadomości są szyfrowane tak, czyli tam jak się podaje, że w bazie to się tych wiadomości nie przeczyta.  
No bo taki też pomysł miał Damian, żeby je wszystkie wiadomości zaszyfrować.

**Piotr Buczkowski** 6:32  
Czym jest szyfrowany? Gdzie jest klucz?

**Mateusz Kisiel** 6:34  
Klucze z pliku konfiguracyjnym.  
No i jeżeli będzie to jakaś wersja chmurowa to albo trzeba go zaszyfrować wszystkich tym samym kluczem albo dla każdego klienta innym kluczem, ale wtedy trzeba by w tej Twojej bazie dołożyć jeszcze kolumne z kluczem tego klienta.

**Janusz Bossak** 7:28  
No dobrze, jakoś tak zamarło.  
Moją stronę w końcu idziemy.  
Jak widzę, że rozważaniu.

**Mateusz Kisiel** 7:39  
Czy no mi się wydaje, że już temat się cofać, bo teraz cofnięcie tego nowa to jest praktycznie robienia od zera, więc wydaje mi się, że już lepiej to sprowadzi dokończyć.

**Piotr Buczkowski** 7:47  
A jak to będzie działać? Bo tam?

**Mateusz Kisiel** 7:52  
Ogólnie teraz zmieniłem już, że się nie wpisuje w tym w tym backendzie tego serwisu u r adamo dita tylko jest ten u RLW tym to penie JWT no i jak przychodzi jak się klika ten przycisk modlicie Odtwórz komunikator.

**Piotr Buczkowski** 8:12  
A po co? Dlaczego po co?

**Mateusz Kisiel** 8:15  
Jeszcze raz to po co?

**Piotr Buczkowski** 8:20  
Płacowy rolę damo dita.

**Mateusz Kisiel** 8:23  
Dlatego no, bo chcę już przystosowywać z grubsza tej wersji chmurowej, żeby przynajmniej częściowa było bliżej tej wersji chmurowej. Tak?  
Żeby wiesz, żeby już nie trzeba było, nie trzeba było wpisywać jednego jakiegoś u RA do addicta, skoro w przyszłości będzie też.

**Piotr Buczkowski** 8:39  
Ale, ale popatrzmy swoją rolę.

**Mateusz Kisiel** 8:43  
Dlatego no bo musi pobrać sobie ten serwis, na przykład listę użytkowników samo dieta więc musi jakby znać o to samo pyta.

**Piotr Buczkowski** 8:54  
Przez przez te pobierali z wyników.

**Mateusz Kisiel** 8:57  
Przez apn to jest tak tak samo jak pobiera amonit sobie przez to chyba jakiś tam kontroler Users kontroler do tego samego kontrola kontrolera pobiera też też ten serwis.

**Piotr Buczkowski** 9:10  
Ale, ale to musiałby się kukizem zalogować.

**Mateusz Kisiel** 9:13  
No i właśnie loguje się za pomocą tokena jw t zrobiłem specjalnie logowanie przez uwierzytelnianie przez JWT faworycie.

**Piotr Buczkowski** 9:22  
Dlaczego?

**Mateusz Kisiel** 9:24  
No żeby można było z tych kontrolerów korzystać.

**Piotr Buczkowski** 9:29  
A to nie lepiej tego reszta pi zewnętrznego trzeba można było użyć.

**Mateusz Kisiel** 9:33  
Znaczy, on nie miał, nie miał opcji pobrania listy użytkowników, chyba z tych co wygrał.

**Piotr Buczkowski** 9:38  
To to trzeba dodać powrot, dodać pobieranie listy użytkowników do tego zewnętrznego.

**Mateusz Kisiel** 9:42  
No ale, ale ogólnie wydaje mi się, że korzystanie z tego JWT zamiast Kukiza jest bardziej takim nowoczesnym sposobem i więcej możliwości dla takiej integracyjnych.

**Piotr Buczkowski** 9:52  
Dobrze to jest film, tam jest logowanie Windows.  
Zapewniam cię, że i ogród to nie będzie działać.

**Mateusz Kisiel** 10:01  
Znaczy, zrobiłem obsługa, że działa tak?

**Piotr Buczkowski** 10:03  
No Windows.

**Mateusz Kisiel** 10:07  
W odpowiednich miejscach wiesz handle zarach w tym globala x zrobię obsługę tego.

**Piotr Buczkowski** 10:14  
Czy dostęp pani noni mowy włączyłeś? Tak.

**Mateusz Kisiel** 10:18  
Mm no mogę ci pokazać komitat w tym, co zrobiłem.  
W sumie czyli poszukam.

**Janusz Bossak** 10:28  
Czemu?  
Taki jeden wniosek przysłuchując się tej dyskusji. Ta dyskusja powinna być po pierwsze walut 3 tygodnie temu.

**Mateusz Kisiel** 10:44  
Znaczy, ja zaczęłam tydzień temu, tak?

**Janusz Bossak** 10:46  
No czy no to tydzień temu tak.  
Także też tych prac tak aż tak dużo do cofnięcia nie ma. Jeżeli to było tydzień temu, no bo to są prace z jednego tygodnia.

**Mateusz Kisiel** 10:54  
No ale to serio dużo robiłem tego, więc taką szkodę.

**Janusz Bossak** 10:57  
Wiem wiem no.  
Yy, chodzi mi o to, że powinien powstawać jednak dla takich rzeczy projekt.  
Ten projekt powinien przechodzić jakąś akceptację.  
Porady architektów.  
No właśnie po to, żeby był właśnie jakby zgodny z filozofią amo dita, zgodny z potrzebą klienta i tak dalej i tak dalej. No głównych tą filozofią, a mod'a w różnych kontekstach i on premise sowych ich murowych i.  
Różnych rzeczy, które tam robimy i będziemy robić.  
No bo trochę teraz tak stoimy, że tak powiem przed faktem dokonanym tak, że zostało tak zrobione taka technologia użyta.  
Takie rzeczy może i dobrze, może nie tak nie wiadomo i teraz, albo to akceptujemy albo wywalamy do kosza i robimy Jeszcze raz. Tak więc.

**Mateusz Kisiel** 11:50  
Znaczy, no, jeżeli chcemy mieć osobną aplikację, to jest praktycznie wydaje mi się, że jeden takiej.  
Jedyne no jest bardziej skomplikowane, po prostu trzeba to robić.

**Janusz Bossak** 12:01  
I też z całym szacunkiem do Damiana. No Damian nie decyduje o architekturze.  
Tak, Damian może decydować o biznesowym.

**Mateusz Kisiel** 12:11  
Tak no właśnie Damian to bardziej projekt takiej biznesowy zrobił. A jeżeli chodzi o architekturę, to bardziej na razie deweloperów to to zostało strony.

**Janusz Bossak** 12:18  
No no no.  
Ja też bym się nie odważył, że tak powiem projektować architektury, tylko zostawiam to wam tutaj, no bo mogę powiedzieć co ja od strony biznesowej sobie wyobrażam, ale jak to tam wewnętrznie bebechy mają być zrobione to już jest poważnej stronie, tak.

**Mateusz Kisiel** 12:36  
No jeśli chodzi o ten sam serwis tego.  
Tego komunikatora to jest zrobione fajnie w nowej technologii problem jest właśnie z integracją model tak no bo to jest już bardziej skomplikowane rzeczy.

**Janusz Bossak** 12:51  
Proszę no, posiadanie tego jako osobnej aplikacji, no może mieć też pewien.  
Wymiar marketingowy, aczkolwiek pewnie bardzo mały i słaby, bo no my nie będziemy wchodzić na rynek komunikatorów, tak nie będziemy rozwijać tego jako konkurencja do tipsów, slacka czy czegokolwiek innego.  
Więc.  
Jedyny argument jaki widzę no to jest ten techniczny, że ten signal r. To jest tam coś nie obciąża amo tita.  
Ale to jest jedyna rzecz, którą jest zaletą. Reszta jest ważna.  
Więc.

**Mateusz Kisiel** 13:36  
Znaczy, no jeśli chodzi o jakieś przyszłe projekty, to można by już jak wykorzystać ten mechanizm, co powstały teraz, bo jeżeli się teraz cofniemy, to już się ich nie wykorzysta.

**Piotr Buczkowski** 13:42  
Znaczy.  
Takie projekty są jako dzienne, są fajne właśnie dla.  
Użytkowego dla instalacji on premises.  
Instalacja chmurowych naprawdę.  
Mogłabyś instalacji tej naszej chmurowe mogą być kłopotliwe.

**Mateusz Kisiel** 14:04  
To chyba, że na razie tylko dla filmu to po prostu zrobimy i dla chmury najwyżej w przyszłości się teraz buduje.

**Janusz Bossak** 14:10  
Podobnie było chyba będą z tym psem, czy za doręczenia nimi.  
Gdzie te klucze przechowywać? Nie no chyba w doręczenia było także na tym chmurze. W końcu tamtym tivolcie gdzieś te klucze umieszczaliśmy i tak dalej.  
A właśnie od początku trzeba myśleć o to, co mówi Piotr. Nie, że coraz więcej tych instalacji chmurowych i będzie to jest jakby absolutny warunek mast hew, że to musi działać i tak, i tak, i tak może i on premises.  
Znaczy, wiesz, ja tutaj Mateusz nie mam do ciebie jakiś tam może pretensji czy coś i też co? Jeżeli nawet cofniemy ten projekt to tydzień to też nie jest żaden jakiś tam.  
Yy według mnie problem, no czasami trzeba takie decyzje podjąć tak no bo ważne jest to co jest przed nami i ileś tam miesięcy i lat używania tego wersus tydzień robienia, więc wolałbym.  
Zrobić drugą wersję, może inaczej trochę zaprojektowaną z wykorzystaniem tych doświadczeń, które już przez ten tydzień. No byłeś.  
Ale żeby to było wiesz, no zgodne, a nie takie na siłę dopasowywane. Teraz nie, bo młody tam.

**Mateusz Kisiel** 15:29  
Moim zdaniem lepiej to działa jak jest osobna aplikacja, ale no więc jest właśnie tego.  
Problemów w jakimś chmurą tak jest konfiguracja.

**Janusz Bossak** 15:39  
No tak, tylko że wiesz, cała idea w tym, żeby to dobrze działało i nad morze i on w remisowo tak no a nie jako to nie jest, znaczy nie robimy aplikacji w rozumieniu czegoś innego niż a mody.  
My robimy komunikator w a modlicie?  
Tak.  
No.  
Technologia jest tutaj już były wtórna do tego komunikator nigdy przez nikogo nie zostanie użyty jako taki teams, tak czy coś, że coś nie będzie miał ammo gitara, będzie sobie używał tego komunikatora. No nie, tak nie będzie to działało.  
To jest.  
Funkcjonalność.  
Tak jak kopalnie lot jest funkcjonalnością amlodipine, aczkolwiek bardziej kopalnie lot bym wyobrażał sobie jako odrębną aplikację.  
Bo teoretycznie mógłbyś, moglibyśmy go w przyszłości gdzieś tam na tym doku zaworu się na przykład wstawić czy nawet na l, żeby gdzieś tam był i ktoś się mógł pytać, to już prędzej sobie wyobrażam takiego amadi tylko plota jako taką właśnie aplikację, która gdzieś tam na backendzie korzysta z jakiejś bazy, wiedzy takiej czy innej.  
I odpowiada na jakieś pytania, niż tego ten komunikator, który jakby nie ma w ogóle racji bytu. Poza amo gitem.

**Kamil Dubaniowski** 17:07  
Ja wręcz tak myślałem czy ten kopalnie lot nie powinien być jednym z użytkowników do czatu tak, czyli wtedy łączymy kopa lota z tym amadi tokiem i jak chcesz pogadać z tatem to wchodzisz tam gdzie gadasz z ludźmi, tylko że odpowiesz sobie czas oplotem.  
Teraz, żeby nie było 2 różnych, znowu teraz miejsc.

**Janusz Bossak** 17:25  
A to byłoby strasznie jakieś pomieszane. Wydaje mi się już.

**Kamil Dubaniowski** 17:30  
Trochę tak jak było na tipsach, gdzie mieliśmy tego Daily bota.  
On tam coś do ciebie pisał, czasami mogłeś coś tam sobie odpisać i wręcz otworzył wpisać ciebie tak ma takiej zasadzie, ale.

**Janusz Bossak** 17:43  
No.

**Mateusz Kisiel** 17:44  
No to już jakaś wizja przyszłości.

**Piotr Buczkowski** 17:45  
I.

**Janusz Bossak** 17:46  
No no no to tak.

**Piotr Buczkowski** 17:48  
No to już co to to co wysłałeś mi się nie podoba.  
Czego tam display generic?

**Mateusz Kisiel** 17:56  
No bo chcę wyświetlać nazwę użytkownika, w tym w tym jak to się nazywa, a model to akurat.

**Piotr Buczkowski** 18:01  
Ale dlaczego czary? Kandydat identity od info display?  
Jest oczywiście innej.

**Mateusz Kisiel** 18:09  
Znaczy, no nie wiem teraz o którym miejscu mówisz, ale ogólnie do tych mówisz o tym co dajemy.

**Piotr Buczkowski** 18:11  
To to, co wysłałeś się w globala seks?

**Mateusz Kisiel** 18:15  
Tym to, co dajemy wykresach tak czy.

**Janusz Bossak** 18:20  
Były świetne.

**Mateusz Kisiel** 18:41  
No to.  
No właśnie tutaj też nie do końca nie do końca wiedziałem co należy dać, bo to jest.  
Uwierzytelnienie w amok i tak żeby.

**Piotr Buczkowski** 18:53  
No jakiś login do normalnie już używam.

**Mateusz Kisiel** 19:06  
Tak tu jest sprawdzenie.

**Piotr Buczkowski** 19:07  
I to będzie to będzie wyjątek. Tak bardziej bym kluczy.  
Tak.  
Trzeba sprawdzić, czy rzeczywiście mamy sens, żeby to sprawdzać tak tylko tu wykonywać.

**Mateusz Kisiel** 19:25  
Znaczy, no, jeżeli jest ten token ustawiony w w h, że tak to jest getto, chyba to sprawdza.

**Piotr Buczkowski** 19:35  
Dlaczego praca zaraz za nim stawiasz? Tak?  
To ustawiasz karen pracy, pan to z tego powinno pobrać.

**Mateusz Kisiel** 20:13  
Znaczy no Plan był taki, że jeżeli jest podany ten baner token w autoryzacji, no to sprawdzany jest czy jest poprawny tak czy czy został wygenerowany przez amonit. Zgodnie z tym kluczem JWT, no i jeżeli jest to.

**Piotr Buczkowski** 20:26  
Tutaj tutaj tego nie powinno być w ogóle, po co tutaj jest?

**Mateusz Kisiel** 20:32  
A no dlatego, no bo potrzebujemy pobrać informacje o obecnym użytkowniku, tak no i w niektórych.

**Piotr Buczkowski** 20:37  
No to z kontekstu nie powinien pobrać.

**Mateusz Kisiel** 20:41  
No nie ma w kontekście tego nie ma w jechali tp kontekst kropka. Karen tego nie było.

**Piotr Buczkowski** 20:52  
No tutaj Nie możesz ustawić.  
Tutaj wstawiasz.

**Mateusz Kisiel** 21:00  
No.  
Ale jest to dalej murem, więc musiałem w taki sposób zrobić.  
No ewentualnie może rzeczywiście da się jakoś ustawić, ale to nie widziałem jak.

**Piotr Buczkowski** 21:12  
Na pewno się to uda się na pewno tam stawić.  
Nie pamiętam gdzie to.

**Mateusz Kisiel** 21:24  
Tak no pewnie lepiej byłoby wstawić tartę, kontekst no.

**Piotr Buczkowski** 21:27  
Nie no.  
Tutaj powinna być zmiana i też też był za tym, żeby najbardziej sprawdzić czy czy mamy ten token tak i dopiero potem ten go wykonywać.

**Mateusz Kisiel** 21:39  
To get token from ripost chyba go pobiera i sprawdza, czy czy jest w ogóle.

**Piotr Buczkowski** 21:43  
Tworzysz obiekt, coś to były wywołuje w nim.

**Mateusz Kisiel** 21:46  
Znaczy no tylko pod otworzy, żeby nie robić go statycznego tak żeby nie było to statycznych.

**Piotr Buczkowski** 21:53  
Jedna wystarczyło tak.  
Jedna metoda ostateczna.  
Czytam i stacyjne tak jakaś nie wiem.  
Może dlatego, że ja bym to inaczej zrobił, tak.

**Mateusz Kisiel** 22:47  
Znaczy, no, być może jest dojście do ulepszenia. Tak to.  
Niezbyt to trzeba jakoś jeszcze udoskonalić, ale tego na razie wstępna wersja, która po prostu działa.

**Piotr Buczkowski** 23:01  
Dobrze, więc się nie będę wypowiadał, tak?  
Po takim krótkim przejrzeniu, tak.  
Nie były się jakieś tokeny zrobione, pamiętam, nie był toyote token.  
Czy ten wtedy trochę tak to to to to to jest maślane?  
Nie.  
Nie wiem co z tym zrobić.

**Mateusz Kisiel** 24:04  
Też nie korzystałem z tego rest api, którego robiłeś, więc też nie do końca wiedziałem, co już mamy. Jak to działa, więc zrobiłem jakby od zera ta.

**Piotr Buczkowski** 24:19  
Wrócimy wystąpi, działa też po tak.

**Mateusz Kisiel** 24:24  
Ale to.

**Piotr Buczkowski** 24:24  
Trzeba było ustawić jaką konto.  
Jeszcze to już zarówno nie ma, bo nie ma.

**Mateusz Kisiel** 24:35  
Ale też tej generujesz właśnie taki odwrót, token i to jest tam.

**Piotr Buczkowski** 24:38  
No nie, nie, to jest sporo, to działa, to to jest dla użytkowników integracji zewnętrznych, tak.

**Mateusz Kisiel** 24:44  
Ok.

**Piotr Buczkowski** 24:50  
Czyli wpisujesz ta generuje szklany tekli Secret tam podajesz na podstawie tego denerwujesz takie do aut i się tym terenem.

**Mateusz Kisiel** 25:11  
Znaczy no jakieś uwierzytelnianie trzeba było zrobić tak, no po ciasteczku się nie dało, no bo były to różne domeny, no i.  
Choćby nawet na.  
Na Development to było ciężkie do zaimplementowania, żeby można było testować te lokalnie.  
Więc wydaje mi się, że takie JWT jest takie najbardziej zdaje się nowoczesne standardowe.

**Piotr Buczkowski** 25:48  
Dodać modyfikacji w łeb, koncie ich nie ma.

**Mateusz Kisiel** 25:52  
W poprzednim może jakimś komitecie czy?  
Tam było kilka, możesz też zobaczyć mojego branża Mateusz mk, Mateusz developer tam są komitety.

**Piotr Buczkowski** 26:05  
Stąd tak.

**Mateusz Kisiel** 26:31  
Tak na przykład jest kors niżej.

**Piotr Buczkowski** 26:46  
Możesz pokazać?  
Jak to działa używanie przez użytkownika tego?

**Mateusz Kisiel** 26:52  
Mm no dobra też w sumie mam napisane w excelu jak działa to logowanie w excelu tylko w wordzie jak działa.

**Piotr Buczkowski** 26:59  
Możesz pokazać?

**Mateusz Kisiel** 27:00  
No dobra, to czy to dostępny jako?  
Mateusza modlitwa, lokal.  
No tak, Jestem przeciez komunikator.  
Klikam go.  
I teraz tak.  
To już akurat byłem zalogowany to to się wyloguje pierwsze.

**Piotr Buczkowski** 27:27  
Możesz w trybie incognito utworzyć?

**Mateusz Kisiel** 27:30  
Dobra, to to będzie najlepiej.  
Przekierowuję tego tok kła 2 modlitwą.  
A tak w ogóle nie jest bezpieczna, nie ma tp SA to trzeba znać. Przejdź i tak to się dzieje, pierwsze się pobiera z tego lokalnego BK ndu jakieś tam informacje? Tak w tym wypadku.  
W tym wypadku to są INFORMACJA O tym, na jakim adresie jest.

**Piotr Buczkowski** 28:14  
To po stronie klienta jest przekierowanie jakieś.

**Mateusz Kisiel** 28:17  
No to po kolei co się dzieje? Powiem pierwsze co wysyłany jest.  
Sprawdzany jest to, że nie jesteśmy zalogowani tak, skoro nie jesteśmy zalogowani, to jest przekierowanie robione takie bardzo szybkie, ale nie było go tutaj widać. Nie mogę też tego tak, bo to jest, bo to nie jest wysyłany request to jest przekierowanie, jest przekierowanie na amo tita z ukośnik tam JWT COVID no i wtedy AMOLED generuje taki jednorazowy kod.  
Yy no i ten kod jest, następnie jest przekierowanie z powrotem tego koła 2 i ten Narodowy kod jest dawany w query stringu no i ten amok i tock pobiera sobie ten kod i na podstawie tego kodu generuje token nie odwrotnie i to jest już na przykład metoda generate.  
No i ten generator wykonuje z amo dita z amo tita.  
Endpoint i przesyła mu ten kod jednorazowy, tak i na podstawie tego kodu moje 2, że skoro on wygenerował ten kod i.  
No jest jest poprawny to generuje mu ten token jwt. No dalej już sobie korzysta z tego tokena.  
No i dzięki temu, że mamy ten pośredni kod krok z tym kodem.  
Nie jest nigdy w adresie przekazywane, że ten token tak więc mam taki sobie ten kod podejrzy z adresu i strongi spróbuje użyć to już on będzie nieaktywny tak, bo jednorazowy kod.  
No bo alternatywą jest podanie bezpośrednio takiego tokenów w adresie, ale to jest gorsze, no bo taki token byłby dostępny te 15 minut czy ileś, więc ty lepiej tak nie robić.  
No i jak się to zobaczę na te partie.

**Piotr Buczkowski** 30:10  
W imię i widzę jeden problem w imię moje 2 serwery.

**Mateusz Kisiel** 30:18  
O k. To jest to nie wysłany.  
No tak, to będzie to będzie problem. No to będzie trzeba, będzie trzeba.  
W jakiejś bazie to zapisać tak ten ten jednorazowy kot.

**Piotr Buczkowski** 30:32  
Będziemy przechowywany.

**Mateusz Kisiel** 30:34  
Tak no bo nie trzeba w jakimś jakimś wspólnym.

**Piotr Buczkowski** 30:35  
W pamięci jest przerwany, tak.

**Mateusz Kisiel** 30:37  
W jakimś wspólnym Kaliszu tym momencie jest w pamięci tak trzeba jakimś wspólnym albo w bazie.

**Piotr Buczkowski** 30:55  
Nie pamiętam jak się tam rozróżniają ty serwer, bo to chodzi, że w imię moje 2 domeny tak staro i nowo część będzie pracuje na starej części nowej.

**Mateusz Kisiel** 31:01  
Tak no ja rozumiem jak jest rondo balance, no to to się może trafić.

**Piotr Buczkowski** 31:05  
Nie, nie, nie mal od gwarancji.  
Część część ludzi używa starego serwera, część nowego znaczy staraj dowanie część nowych.  
Już nie pamiętam czy one maja ta sama.

**Mateusz Kisiel** 31:14  
O k.

**Piotr Buczkowski** 31:17  
A po prostu za podstawie tego, do jakiego dns się odwołasz, czyli w jaki domeny jesteś taki ci ip zwróci.

**Mateusz Kisiel** 31:23  
Mhm.

**Piotr Buczkowski** 31:25  
A tak tu jest ten sam adres, tak?

**Mateusz Kisiel** 31:31  
Jeżeli nie mają lub balans i upload balancing i udałoby się ustalić takie adres dla jednego serwera, to by tego problemu nie było.

**Piotr Buczkowski** 31:44  
Znaczy.  
Nie mają ledwo brązera takiego, że lot balansuje datuje na który serwer pójdziesz tak?  
Są połączeni do 2 domen, mają 2 dresy, 2 różne dns, który dlatego samo ten sam adres inaczej rozwiązuje.

**Mateusz Kisiel** 32:02  
No ale też właśnie myślałam, że trzeba by ten kod zapisywać w bazie, ale no na razie jak zrobiłem tymczasowo jeszcze w pamięci będzie miał na to czasu. Chciałem pierwsze już zrobić ten komunikator czy jakoś wstępnie działało?  
Ja właśnie w tym tygodniu Plan to zrobić w bazie.

**Piotr Buczkowski** 32:14  
Dodać jest na to miejsce, tak jest takie coś jak przechowo.  
Wysyłanie powiadomień.  
Wysyłanie zaproszeń.  
I tam jest zapisywane, że wysłano zaproszenie do na ten adres z tym kodem, tak z guide.

**Mateusz Kisiel** 32:28  
A jak się na temat tabela?

**Piotr Buczkowski** 32:34  
Nie pamiętam, ale jak weźmiesz?  
Nie stał użytkowników plus i zaprosisz użytkowników?

**Mateusz Kisiel** 32:43  
To może zobaczymy, no.

**Piotr Buczkowski** 32:45  
Reggie, nie wiem.

**Mateusz Kisiel** 32:49  
Józef activity log na przykład jest.  
Wydaje mi się tak vity.

**Piotr Buczkowski** 32:56  
Nie.  
Ale tam są różne rzeczy zapisywane, tak?

**Mateusz Kisiel** 33:04  
To jest ta dobra?

**Piotr Buczkowski** 33:07  
No nie wiem czy to był sens to tytuł życie, bo to.  
Bo normalnie to jest sens tak, że ta osoba zaprosiła taką osobę.  
Tak ozonową?

**Mateusz Kisiel** 33:18  
Znaczy no.  
Wyszukiwanie byłoby powiedzmy z jakimś filtrem, żeby sprawdzać tylko na przykład przez ostatnie 3 godziny. Tak więc ty też nie nie szukałaby jakoś dużo.

**Piotr Buczkowski** 33:34  
Dobrze.

**Mateusz Kisiel** 33:47  
To pytanie właśnie, jak to, czy kontynuować to dalej i robić osobną aplikację, czy.

**Piotr Buczkowski** 33:56  
Nigdzie indziej nie prosiłem, będzie będzie używany.

**Mateusz Kisiel** 34:00  
Znaczy pewnie tak tylko na pytanie, czy warto już mieć tam konfigurację gotową jakieś przyszłe właśnie zewnętrzne aplikacje, które chcielibyśmy robić?  
Jak już się raz te szlaki przetrze, to już będzie nam łatwiej robić to w przyszłości.  
Taka Cisza teraz.

**Piotr Buczkowski** 35:03  
Nie wiem.  
Za mało czasem miałem, żeby to przemyśleć.

**Mateusz Kisiel** 35:11  
Myślę, że można by na przykład jutro już jakieś spotkanie zrobić, przemyśleć to sobie i wtedy jeszcze.

**Piotr Buczkowski** 35:14  
No nie musiał musiał to zobaczyć, pobawić się tym nie to, że czasie samego spotkania nic nie powiem.

**Mateusz Kisiel** 35:21  
No to.

**Piotr Buczkowski** 35:22  
Więcej niż teraz.

**Mateusz Kisiel** 35:25  
Myślę, że w razie czego mogę ci podać linka do tego projektu, w którym jest nam tak?  
A to mnie tak.

**Piotr Buczkowski** 35:38  
To to jest tak w tym?

**Mateusz Kisiel** 35:39  
Tak tutaj.

**Piotr Buczkowski** 35:57  
Niedobrze razie nie ma, chyba więcej jest to nie ma co więcej rozmawiać.

**Mateusz Kisiel** 36:04  
To po prostu będę dalej kontynuował. Na razie to, co obecnie robię i i potem najwyżej coś jutro jeszcze ustali.

**Piotr Buczkowski** 36:19  
Dobrze to kończmy.

**Mateusz Kisiel** 36:21  
Dobra.  
No to cześć.

**Piotr Buczkowski** 36:23  
Cześć.

**Janusz Bossak** zatrzymano transkrypcję
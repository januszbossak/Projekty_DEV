**Data spotkania**: 11 września 2025

**Lukasz Bott**: Kwestia jeszcze... mieliśmy... były dwa zlecenia do realizacji. W tej chwili ten opracowuje, to jest ta integracja z Comarch Hubem i jeszcze jedna rzecz. I jeszcze jedna, że to będzie ten... możliwość za pomocą CallRest-a wstawienia wielu plików do... do serwisu.

**Piotr Buczkowski**: Co?

**Lukasz Bott**: Chodzi o to, że ten... ten jakiś tam Web Service z wewnętrznego systemu, żeby można, żeby było możliwe za pomocą funkcji CallRest, tak, wstawić wiele... wiele plików jednym, za pomocą jednego żądania, tak, jednego wywołania.

**Piotr Buczkowski**: Dlaczego się nie da?

**Lukasz Bott**: Takie... no bo nie przygotowaliśmy pod to. Adrian to już rozeznawał temat. Musimy tam obsłużyć ten multipart form, tak?

**Piotr Buczkowski**: A, czyli dobrze, czyli nie w JSON-ie, tylko multipart form, OK.

**Lukasz Bott**: Tak, tak, chodzi o multipart form.

**Piotr Buczkowski**: No bo w JSON-ie... czy tam teraz mamy, tak i jedziemy, w czym problem. No jeżeli to chyba rzeczywiście nie mamy.

**Lukasz Bott**: Nie, nie, no to rozwijał, tak, poszła na to... poszło na to jakoś nieduża wycena, natomiast ze względu na takie a nie inne jakieś tam... ten, powiedzmy, nazwijmy to delikatnie, problemy między działem wdrożeń a klientem, tak, no musimy to zrobić niestety, wziąć na klatę. Na szczęście Adrian to wyceniał na jakieś tam pojedyncze dni, tak?

**Piotr Buczkowski**: To przemyślmy to, jak to dobrze zrobić, tak. Nie ma, jest wciąż?

**Lukasz Bott**: Pan...

**Piotr Buczkowski**: Jest Adrian, bo mi nagrywanie i transkrypcja zajmuje wspania... nie Ania, ten, sania, a nie Adrian.

**Lukasz Bott**: Ania. Od rana nie ma na razie.

**Damian Kaminski**: No to wrzućcie Adriana.

**Lukasz Bott**: Tak, bo jeszcze Adrian coś tam mówił o...

**Piotr Buczkowski**: Przemyślmy to, żeby to było spójne, żeby nie było tak jak poprzednio, jakieś tam te dziwne header value 1, header name 1 czy tam coś.

**Lukasz Bott**: Dobra, jak tu się dołączy?

**Adrian Kotowski**: Cześć.

**Lukasz Bott**: Jesteś Adrian, dobra, słuchaj. Chciałbym zacząć od tematu na Radzie tego odnośnie... odnośnie tych tematów, które wyceniałeś. Tam jedno ze zleceń dotyczy przekazywania plików do wewnętrznego Web Service'u, wielu plików do zewnętrznego Web Service'u za pomocą funkcji CallRest. Wydaje mi się, że tam chodzi o ocenę tego multi... obsługi multipart form, tak.

**Adrian Kotowski**: Będziemy teraz zajmować się tym. To jest jakby mało, tak jak już naprawili w przyjaznej formie, tam bodajże to był chyba temat Marba, tak, klient wiesz, no.

**Lukasz Bott**: Tak, ten klient Marba, zaraz, zaraz tutaj znajdę ten.

**Damian Kaminski**: No właśnie zarysujcie kontekst biznesowy, bo jak tak ogólnie mówicie, to my przekazujemy w jednym...

**Lukasz Bott**: Mamy. W momencie, gdy już, już, już, już ten.

**Damian Kaminski**: Mhm.

**Adrian Kotowski**: No integrację przez CallRest i tam no jest potrzeba, żeby występować wiele plików naraz, znaczy dynamiczna ilość, więc tych plików może być, nie wiem, jednego... nie wiem, do stu przykładowo. No i ten mechanizm, który teraz mamy, ten CallRest wymaga, żeby po prostu definiować tyle parametrów i to może być maksymalnie tych plików do wysyłania i to jest słabe. No i pojawił się pomysł, żeby to zrobić bardziej dynamicznie, czyli po prostu na przykład, nie wiem, można wybudować sobie takie załóżmy, nie wiem, stringi w regule i w tym stringu, w regule... czy z tego stringu był wysyłany argument na przykład do CallRestu i to powodowało na przykład, gdzie można by, nie wiem, w jednym, w jednym dużym parametrze systemowym, zamiast tych, nie wiem, ilu parametrów systemowych.

**Piotr Buczkowski**: A gdzie są te pliki w systemie używane? Gdzie są te pliki zamieszczone?

**Adrian Kotowski**: I co tam można by wskazywać te pliki na przykład, bo teraz to tak, że tam się wskazuje albo ID tego pliku, albo nazwę pola, albo nazwę załącznika, więc takie 3 mechanizmy, 3 sposoby wskazać załącznik. Zakładam, że nie będzie po prostu teraz po API sobie tam to jakoś nie wiem, pobierać to z tabeli.

**Piotr Buczkowski**: Ale ustalmy, gdzie są te pliki teraz używane, jak są te pliki umieszczone na sprawie.

**Damian Kaminski**: Pola? W sensie czy na liście?

**Lukasz Bott**: Pola, na liście, jeszcze może być w polach w tabeli, tak.

**Damian Kaminski**: Dobrze, ale to poczekajcie, wy mówicie o CallReście, a nie o pobieraniu, tak?

**Piotr Buczkowski**: No tak.

**Adrian Kotowski**: Tak. O CallReście tak.

**Damian Kaminski**: O CallReście, no dobrze. I teraz, no bo to dzisiaj dotyczy Marby, a ja już widzę, że jeśli mówicie o fakturach i załącznikach, to zaraz będzie dotyczyć wszystkiego co przychodzi z KSeF albo KSeF będzie pobierał, Connector też załączniki i zaraz powiedzą wszyscy, że oni chcą te załączniki też gdzieś tam do systemów jakiś tam kolejnych dziedzinowych żeby je dostarczać, bo...

**Piotr Buczkowski**: Ale my wysyłamy z AMODITa gdzieś, a nie pobieramy.

**Damian Kaminski**: No tak, tak o tym mówię, ale chodzi mi o to, że wiesz, przychodzą z KSeF Connectora faktura jako główny dokument, ale może przyjść też ich z załączników i zaraz ta sama potrzeba, więc patrzmy na to szerzej niż tylko w kontekście Marby, bo zaraz w styczniu może się pojawić, że wszyscy tak będą chcieli, żeby wysyłać. Natomiast pytanie jest jeszcze takie, a dzisiaj wygenerowanie podstawienie po prostu zdefiniowanie zmiennej i tam podstawienie... zbudowanie JSON-a jest niemożliwe? Parsowanie wykrzacza?

**Piotr Buczkowski**: Ja proszę, nie, nie róbmy takich rzeczy.

**Damian Kaminski**: Nie róbmy tak, OK.

**Adrian Kotowski**: Znaczy, ja... nie jest to potrzebne zawsze, bo to idea jest taka, że po prostu prosto...

**Piotr Buczkowski**: Znaczy tutaj, po pierwsze nie ma JSON-a, jest multipart form data, tak, to nie jest JSON, to nie ma nic wspólnego z JSON-em.

**Adrian Kotowski**: Tak. Czyli tam się po prostu wysyła klucze: klucz-wartość, klucz-wartość i to może być jak wartość może być plikiem, albo może być na przykład tekstem, taka jest ta funkcjonalność.

**Damian Kaminski**: Rozumiem. No dobrze, ale w kontekście tego, co powiedziałem i co Piotr skomentował, żeby właśnie tak nie robić, to ogólnie powinniśmy się na to przygotować. Według mnie, bo zaraz może się okazać, te zaraz, no to tam kwestia kwartału, że więcej firm będzie tak potrzebować, więc powinniśmy się na to jakoś przygotować, żeby zrobić to tak jak trzeba, a nie tak jak na przykład właśnie zaproponowałem. No bo to nie jest zgodne, tak specjalnie wrzuciłem ten pomysł, bo zakładałem, że Piotr [powie], żeby tak nie robić. Więc pytanie jak to?

**Piotr Buczkowski**: No czy operacje, duże operacje na dużych stringach są zasobochłonne, pamięciochłonne?

**Damian Kaminski**: Rozumiem.

**Piotr Buczkowski**: Niewydajne.

**Damian Kaminski**: No dobrze, więc wymyślmy po prostu jak to będzie można przekazać zalecenia, jak to robić.

**Adrian Kotowski**: No dobra, my też mamy to wymyślone, chcecie to nie ma co debatować, to widzi tyle przykład, jest ten parametr...

**Piotr Buczkowski**: A jak mamy? A jak mamy w środę?

**Adrian Kotowski**: Wreszcie się tym umówiliśmy, że po prostu można było na przykład w jednym parametrze, zamiast tworzyć parametrów systemowych, nie wiem, 1, 2, 3, 4, 5, tylko po prostu podać jeden parametr i w tym parametrze można by na przykład wklejać, nie wiem, na przykład taką listę poszczególnych tych elementów, które definiuje.

**Piotr Buczkowski**: Czy to, czy to jest, czy to jest przykład?

**Adrian Kotowski**: To jest przykład jak teraz działa, w tym zrobić to docelowo, no lepiej uniwersalnie, że tu jest jakiś tam... przyjechał trochę, nie dostępnia... "file", plik, faktura, plik, nazwa pliku, no to jest taki przykład, że jak się wskazuje pojedynczy plik, czy też tu wybieramy "file", czy też do informacji to jest jednak plik, bo może być tekst. Później jest "FieldByName", czyli wybieramy w jaki sposób ma, mamy wybrać ten załącznik. Później jest nazwa pola podana i później jest nazwa tego pliku.

**Piotr Buczkowski**: Ale...

**Adrian Kotowski**: Nie jesteśmy nawet... dobra, ale w pliku jest odcinane. Można na przykład zmienić też nazwę pliku i wysyłając ją i to byśmy mogli powiedzieć po prostu parę razy i tyle. Konsultant musiałby coś takiego zbudować na przykład w kodzie reguły i to później na przykład nie wiem, ustawić jakoś.

**Piotr Buczkowski**: To znaczy dynamicznie zbudować jakąś regułę.

**Adrian Kotowski**: No na przykład nie wiem tutaj, zamiast tego, jakaś data, ta wartość, która jest podzielona. Jakby wiesz, tak elastycznie można po prostu podstawiać dynamicznie na przykład jakiś, nie wiem, nazwę jakiegoś numeru dokumentu albo nazwy, nazwy zmiennej i ze zmiennej brać to całe.

**Damian Kaminski**: Ale co w tej zmiennej miałby być, no?

**Adrian Kotowski**: No po prostu miałbyś podaną listę tych poszczególnych załączników, które mają być wysyłane. Jeszcze tu jest ten file z dwukropkiem do końca i to już nie po prostu tyle razy powielone, ile ma być wpieranie załączników.

**Damian Kaminski**: Tylko to jest jakiś konkretny przykład struktury endpointa, to to nie jest uniwersalne, nie wszyscy będą tego tak wymagać.

**Adrian Kotowski**: I tak by to będzie w JSON-ie.

**Piotr Buczkowski**: No ale, ale ten... ale ten tam wymaga...

**Adrian Kotowski**: Nie no, idea jest taka, że to byłoby...

**Damian Kaminski**: Nie, ja rozumiem, że tam, tylko wrzucam od razu szerszy kontekst, że inni powiedzą, że oni chcą w standardowym JSON-ie mieć dwa, bo najczęściej będą dwa, ale jeśli by było 5, to chcą mieć 5 dokumentów przesłanych na zasadzie struktury tabeli.

**Piotr Buczkowski**: No to nie, no to trzeba... JSON, JSON możemy dowolnie budować, tak mamy "each", tak.

**Lukasz Bott**: Ale co? Ale to, czego Piotrek, ale to nie wtedy kodujemy zawartość pliku jako ten Base64?

**Adrian Kotowski**: Nawet nie trzeba tego robić w tym momencie, bo...

**Piotr Buczkowski**: No da się, da się szablon trzeba przygotować i czy jakimś...

**Adrian Kotowski**: Znacznie, ale to... ale tu nie ma potrzeby tego robić, bo my tak naprawdę jak... no nie wiem te dane informacje, czy JSON-a, czy tak jak ja zaproponowałem, to jakby tu nie ma na razie potrzeby. My dopiero załączniki, treści załączników wyciągamy dopiero w etapie, jak na przykład nie wiem, callRest się wykonuje, gdy pobieramy ten załącznik i wtedy już bezpośrednio go budujemy w tej metodzie form data. I to jest, to jest jakby niezależnie po prostu wysyłanie plików, jakby tam nie ma Base64, jakoś to jest jakoś tam inaczej chyba, format binarny.

**Piotr Buczkowski**: No nie, nie, nie, to jest całkiem inny format, tak?

**Adrian Kotowski**: Tak, tak właśnie chodzi o to, że to nie ma sensu tego konwertować.

**Lukasz Bott**: Nie no rozumiem.

**Damian Kaminski**: Nie no to dobrze, to Adrian, to co mówisz to jest MVP do tego klienta. Ja tylko wrzucam od razu temat, który... żeby nam po prostu w cudzysłowie nie wybuchł i potem trzeba będzie wszystko rzucać, tylko żeby na spokojnie to zaplanować.

**Piotr Buczkowski**: Nie, to to nie, to nie jest to, nie jest MVP do tego klienta. To jest obsługa wysyłania plików poprzez w formacie multipart form data.

**Damian Kaminski**: OK, no dobra, to to jest jeden temat.

**Piotr Buczkowski**: Nie mylić z formatem application/json, bo to jest całkowicie coś innego. To, że obydwa wywołanie z CallRest, to nie mieszajmy tego, to są inne formaty.

**Adrian Kotowski**: Tak. I to jest... są całkowicie rozłączne, tak. Znaczy wysyłanie plików w lepszej formie jest ten form data, tak, bo w JSON-ie to tam w miarę kombinowanie z tym Base64, a form-data binarnie jakoś tam to obsługuje. Wysyłanie tych, tych danych, więc to jest bardziej taki optymalny nawet. No ale to jest moje, więc albo jest multipart form data, albo jest JSON. Czy tam podjazd na format.

**Damian Kaminski**: Dobra, to słuchajcie, czy ten temat dla Marby w kontekście tego multipart form data, czy to już jest jasne wszystko?

**Adrian Kotowski**: Jak dla mnie tak, znaczy, no chcemy po prostu zrobić te...

**Piotr Buczkowski**: Dla, dla mnie nie, ale to bym się sam chętnie... no... przeanalizował, jak to Adrian zaproponował, bo będę miał uwagi czy nie, ale to może nie na teraz, bo to no to po to chwilę analizy potrzebuję.

**Adrian Kotowski**: To nie, to co to jest?

**Damian Kaminski**: Znaczy pytanie, czy to jest na etapie realizacji, czy wyceny? Bo jeśli to jest tylko...

**Lukasz Bott**: Nie, to jest, nie, jeżeli chodzi o konkretną Marbę, to to pokazuję. To przyszło zamówienie, zlecenie i mamy to zrobić. I właśnie poprosiłem przed spotkaniem, żeby zlecający podał daty oczekiwane i to mamy zrobić jeszcze do końca września.

**Adrian Kotowski**: Nie, mam już... to chyba wyceniałem, jakby już, a tak przygotowane jest. Jakbyś mógł sprawdzić czy to jest... to jest opis mojej propozycji, więc jakbyś Piotrek miał czas to możesz to po prostu przeczytać.

**Damian Kaminski**: W zleceniu. A nie tu, dobrze.

**Adrian Kotowski**: Czy chyba...

**Piotr Buczkowski**: Dobrze, już, już to szukam, jak to jest... Marba tak, nie, jak to się nazywa?

**Damian Kaminski**: No tak biedny ten opis, możesz przeczytać tu, bo to jest jedno zdanie.

**Piotr Buczkowski**: Nie przez...

**Adrian Kotowski**: Wydaje mi się, że chyba tutaj coś bardziej nie wiem dokładnie opisałem, bo to coś ucięło mi ten tam, pisałem o tym.

**Lukasz Bott**: Nie ma, moment, moment, bo to jest...

**Damian Kaminski**: Bo to nie ten, nie ta sprawa.

**Lukasz Bott**: To już jest zlecenie. Tak swoją drogą.

**Adrian Kotowski**: Już... się dziwnie czułem, takiego opisu zostało bardzo takie... nie wiem jak to nic.

**Lukasz Bott**: No nie, no, no taki dosyć lakoniczny, tak, to rozumiem.

**Adrian Kotowski**: No to... dobra, to nie wiem, ale to możliwe, że po prostu to dokładnie opowiedziałem na jakimś, jakimś, jakiejś Radzie, bo to nie jest... Zaproponowałem, żeby to kontynuacja, jakby tego nawet też potrafię zwróciły jeden, no bo to nie wiem, bo dawno jakoś, ale...

**Damian Kaminski**: A w komentarzach?

**Lukasz Bott**: Nie, nie. Mieliśmy... to jest tylko tyle, no najdokładniejszy opis mamy...

**Piotr Buczkowski**: Znaczy ktoś coś, coś kojarzę ten temat, ale nie pamiętam jaka była konkluzja.

**Lukasz Bott**: No to może dyskutowaliście, wiesz, jakoś tak...

**Adrian Kotowski**: Znaczy to po prostu to miało być w jednym parametrze JSON-owym obsługiwane, żeby nie robić wielu parametrów, tylko w jednym, żeby tam dynamicznie to jest wartość.

**Piotr Buczkowski**: No ale, bo tam widziałem tak jakiś... według tego jakby nowego formatu, który tam użyliśmy do tych headerów, tak, że my zamiast nie było, żeby było, nie było tam header 1, h 2, h...

**Adrian Kotowski**: No tak, tak, właśnie o, dobrze to tutaj byś mógł...

**Piotr Buczkowski**: ...3, tylko no właśnie tak, tak podobny coś jak generujemy JSON.

**Adrian Kotowski**: A dobrze, tak, tak, tak, dobrze, to to racja, to tak to faktycznie.

**Piotr Buczkowski**: Z użyciem tych... z użyciem tych, z użyciem tych naszych, tam konstrukcji "each", "if" czy cokolwiek. Tylko, że budując a czy to headery, czy czy właśnie multipart form data request.

**Adrian Kotowski**: Jakbyś mógł ukryć to, że wstępnie Janusz czy...

**Lukasz Bott**: Miał z dostępem.

**Adrian Kotowski**: Dobra, to jakbyś mógł wejść w opis CallRestu to tam w sumie jest to pokazane, tylko też to pisałem. To było zrobione w jednym, w jednym jakby miejscu, to ja po prostu dla mnie to jasne wszystko jest, więc jakby jak to ciebie chcę jeszcze zobaczyć to to...

**Lukasz Bott**: Ale... Co gdzie mam wejść, co pokazać?

**Damian Kaminski**: To...

**Adrian Kotowski**: Na naszej wiki, Wiki Wewnętrzne, po prostu CallRest i tam będzie ten artykuł i tam to jest jakby opisany jest przykład jak to jest zrobione już w jednym miejscu tak wreszcie.

**Damian Kaminski**: Na Wiki.

**Adrian Kotowski**: Tak tutaj CallRest, nawet ten panel chyba jest po plecach, byłoby szybciej, a dobra jest już na pierwszym tym pozycja. I ten, przejedź, powinny być na nagłówki albo headers 2 w nagłówku, który to może o r... dziesiątkę się 10.2.

**Piotr Buczkowski**: No to to tak.

**Adrian Kotowski**: 10.2.

**Piotr Buczkowski**: Porównanie dwóch sposobów. Dobrze. A no.

**Adrian Kotowski**: Samo gdzie jest wykonywany to też ja z dwiema grupkami zbudowałem sposób. Że nowa linia to by oznaczała chyba... no nowa linia oznaczała nowy, jakby nowa parę klucz-wartość.

**Piotr Buczkowski**: No tak, tak.

**Adrian Kotowski**: Święto to samo praktycznie tego, że ja tam umiem mieć więcej tych jakby tych członków by tak jeszcze wrzucić do łącznika, wpuszczam nie wiem nazwę tego.

**Piotr Buczkowski**: No, no ale dokładnie robimy taki szablon.

**Adrian Kotowski**: No tak, no to...

**Piotr Buczkowski**: Takim formacie z wykorzystaniem tych naszych jakby Handlebars, Handlebarsowych placeholderów, tak.

**Adrian Kotowski**: To tak. Tak.

**Piotr Buczkowski**: Format Handlebarsów.

**Adrian Kotowski**: No to ja jestem, planowałem, żeby tam były, żeby separatory były podwójne te kropki tak, to nie wiem, bo ktoś może też nie mieć na przykład w nazwie jakoś...

**Piotr Buczkowski**: Tak, a po co, po co takie jest wymaganie? Nie...

**Adrian Kotowski**: Nie no, żeby trzymało się tutaj, wcześniej to była, to zawsze to jakoś tam jeszcze jest szansa, że...

**Piotr Buczkowski**: No czy nie jest bardzo podobna do headers? Przecież nazwa-wartość, nazwa-wartość.

**Adrian Kotowski**: Tak, tak, ale ja po prostu separator chciałem dać taki bardziej można by powiedzieć rzetelny, no bo może być nie wiem, w jakimś tam nie wiem, w jakich wartości może być. Też wiesz, ten dwukropek, a dwukropek się raczej...

**Piotr Buczkowski**: A pytanie jak, pytanie jak jest to wtedy encodowane, bo być może nie może?

**Adrian Kotowski**: Nie, to jest normalnie, po prostu słuchaj, to jest normalnie rozwijanie, to po prostu rozbijanie na człony i to po prostu ten... nie uzupełniam te jest ten...

**Piotr Buczkowski**: Nie trzeba sprawdzić, bo jeżeli... Skoczy... Nie pamiętam w but...

**Adrian Kotowski**: Znaczy, znaczy dzieje się w tym mój mechanizm. Tam działał ten stary sposób, w sensie... no to nie jest problem tam dziewczyny zrobić, więc tu nawet nie wiem, czy jest dyskutować po prostu.

**Piotr Buczkowski**: Znaczy bo nie ma sensu wymyślać jakiegoś bardziej dziwnego separatora, żeby był unikalny, bo on już może się zdarzyć. On nie będzie unikalny, tak. Tylko trzeba to prawidłowo obsłużyć.

**Adrian Kotowski**: Tak, no wiadomo, sztuka tego, ale to, że to jest, że to jest taka mało istotna, w sensie no totalnie to podwójny separator, żeby po prostu... No jak zmienić czasy?

**Piotr Buczkowski**: Nie, to nie, nie, nie, nie zmieniajmy tego, jak jest jeden, to jest jeden jest.

**Adrian Kotowski**: No ja też u mnie to chyba było, więc chciałem żeby robili, że dwa to, ale to już taka kwestia nie na tej, to już takie bardziej jeszcze jedne rzeczy to będzie, nie wiem.

**Piotr Buczkowski**: Gdzie? Nie, to jest bardzo ważna rzecz, żeby nie było później coś, a to było źle, ale nie możemy zmienić, bo, bo już jest w dziesiątkach wdrożeń już jest tak użyte. Już nie możemy tego zmienić, tak, a to jest źle.

**Adrian Kotowski**: No dobra, no to mogę zrobić pojedynczy, żeby było. Czyli tak robili, tego nie zmienimy starych tych starych integracji, jak dobra to potrzebne i ten pojedynczy jest separator, ten pojedynczy wątek.

**Piotr Buczkowski**: Ale, ale zrobiłeś w obecnej, ich obecnych integracjach, żeby były dwa tutaj?

**Adrian Kotowski**: Wszystko jeżeli tam, no to już od 2 lat tak działa, no i nie da się jak w sensie, no to to nie ma jakby...

**Piotr Buczkowski**: O tak, o to od 2 lat?

**Lukasz Bott**: Nie, nie. Nikt nie narzeka, bo pewnie ich nie tego nie robi.

**Piotr Buczkowski**: Przecież to robiliśmy jakiś czas temu. Która tam jest ten data podana tak... Poniżej.

**Adrian Kotowski**: Wpisz jak to się nazywało form.

**Piotr Buczkowski**: Poniżej. Jeżeli nie stary, no nowy sposób 10.2. Dzisiaj trochę niżej. A, 25.03, no od wiosny.

**Adrian Kotowski**: Tak, no ale to ja mówię w tym moim wcześniejszym jakby o tym też było dawno zrobione, czy 2 lata temu, jak mu się stało?

**Piotr Buczkowski**: No to... No ale wcześniej było tym CustomHeaderValue1, 2, 3, 4, 5, 6, co mi się bardzo nie podobało.

**Adrian Kotowski**: Tak.

**Lukasz Bott**: Że to było dobre, jak miałeś skończoną liczbę, ty?

**Adrian Kotowski**: Jeszcze jedno, akurat tu się zgadzam z tym, ale im bardziej chodziło to obejście nam przysługę form data, a nie o te nagłówki. Może tam zrobiłem te podwójne jakby podwójne dwukropki.

**Piotr Buczkowski**: Coś nie wiem o czym mówisz.

**Lukasz Bott**: Dobra, słuchajcie panowie.

**Adrian Kotowski**: Też po spotkaniu będziemy pisze dobra, ja muszę do razie to zrobić, więc no tutaj nie wiem już jak czerpalnych.

**Lukasz Bott**: Panowie, mam trochę...

**Damian Kaminski**: Dobrze, to znaczy w kontekście tylko dopytam w kontekście tego, bo wrzuciliście ten temat i właśnie mam takie przemyślenie, że zaraz może być taka potrzeba.

**Lukasz Bott**: Dobra.

**Damian Kaminski**: Może nie za chwilę, ale właśnie, żeby nam ona nie wyskoczyła nagle, co czy...

**Piotr Buczkowski**: O, o. Te opi... opisz, opisz potrzebę.

**Damian Kaminski**: Dobra, OK. Wrzucę na kolejne Rady, dobrze?

**Piotr Buczkowski**: Tutaj, tutaj mamy konkretną potrzebę wysyłania wielu plików w formacie multipart form data, jeżeli będzie potrzeba wysyłania wielu plików w formacie...

**Damian Kaminski**: Dobra.

**Piotr Buczkowski**: JSON, opisz potrzebę.

**Lukasz Bott**: Ja, ja. Dobra to...

**Damian Kaminski**: Dobra i tak chciałem to skończyć.

**Adrian Kotowski**: Link tak.

**Janusz Bossak**: Chciałam jeszcze ja mam kwestię dla... poczekajcie sekundkę, bo pilna sprawa. Daniel Reszka się strasznie już denerwuje mnie, że klienci się denerwują, że ciągle nie działają e-Doręczenia na chmurze.

**Lukasz Bott**: Dobrze, słuchajcie.

**Adrian Kotowski**: Właśnie tym pracuję teraz, no ale jak mówiłem dzisiaj rano, no gdzieś w kąt tego dojść, jak nie mam wsparcia Poczty, no i to jest to nie dwóch klientów, więc no jeszcze to klienci On-Premise, który nie zgłaszali jakichś tam problemów, więc nie wiem, może to kwestia...

**Janusz Bossak**: Póki jest nadwyżek, którzy się denerwują, no wiesz, nie możemy ich lekceważyć, że że co, jak na chmurze, to sobie mogą poczekać.

**Adrian Kotowski**: No ja teraz drugie się tym zajmuje, więc no nie jest jakby nie leży jakoś tam wiesz gdzieś, no po prostu no działa w tym działem być z jednym.

**Damian Kaminski**: To napisz tak, napisz w tym wątku tutaj Danielowi, że pracujesz nad tym, żeby było zapewnienie, że no faktycznie ktoś się tym zajmuje, bo może tu brakuje komunikacji po prostu.

**Janusz Bossak**: Tak, bo on się pyta czy czy masz ten jakiś dodatkowy kontakt do Poczty Polskiej. No wiesz, czy to aktywnie naprawiamy, no jeszcze...

**Adrian Kotowski**: To jest stary... ciłem wydaje nie wiem, bo chcą który to posługiwałem właśnie obsługują klientów, żeby no posiłkowałem, żeby klienci sami na przykład zgłosili, bo opiekuna handlowego do Poczty Polskiej, który pomoże po prostu im. A no my tego nie możemy zrobić jako integrator, ale klienci, zwłaszcza ci więksi mogą to ogarnąć, więc jakby tutaj też jakby jest inicjatywa po stronie nie wdrożeniową, że no liczę się, tylko ja będę tutaj trochę właśnie dotrzeć do Poczty Polskiej, to tak teraz robię.

**Janusz Bossak**: I wytłumacz to Danielowi, żeby on wiedział, bo ja też nie bardzo rozumiem, w czym jest dokładnie problem. No ale na razie jest odbiór taki, że my leżymy, nic nie robimy tak, a klienci czekają i kiedy się Adrian tym zajmie? Nie chciałbym mieć takie...

**Adrian Kotowski**: No to tutaj razie pogadam z nim tutaj. Ja, no nie jest na kontrakcie tutaj z konsultantami. Ja dziwne, że po prostu nikt tego nie widzi po prostu. No dobra, to dobrze, że powiedziałeś OK to to to dobra, to też jest łączyć.

**Lukasz Bott**: Dobra, Adrian, Adrian moment.

**Janusz Bossak**: Musimy dbać o wizerunek też tak, że robimy, wiecie, no wiadomo, tak czasami trzeba na coś poczekać, ale... ogólnie się komunika...

**Piotr Buczkowski**: No to, no to nie, nie przerywamy Adrianowi pracy nad tamtym.

**Janusz Bossak**: Jest bardzo, bardzo dobra.

**Lukasz Bott**: To tak dobrze, tylko Adrian moment, moment Adrian moment zaraz cię zwolnimy, tylko jedna rzecz, bo ty gdzieś tam w dyskusji na kanale, bo tutaj te zgłoszenia i te 2 jak się tam zlecenia są przypisane do ciebie i za zaplanowane w szczególności to jest zaplanowane na...

**Adrian Kotowski**: No dobra, to dzięki, cześć. Myślałem...

**Lukasz Bott**: ...przyszły trzydziesty dziewiąty sprint. Co by było to od 22 września do trzeciego października. Coś mi napisałeś, że ciebie nie ma?

**Adrian Kotowski**: Tak, tak.

**Damian Kaminski**: No właśnie ja też mam takie poczucie, że oczekiwana przez klienta data to jest propozycja. Może tu brakuje naszej propozycji, bo my nie musimy tutaj... wiecie, jak klient by podał za 3 dni, bo on by tak chciał najlepiej to nie znaczy, że my musimy się zgodzić dokładnie tak, jak on zaproponował, nie.

**Lukasz Bott**: To jeżeli nie ty? Ja. Moment. Moment dobra, Adrian, rozumiem, że w tym okresie dwudziesty drugi... 22 września, 03 października. Jesteś na urlopie? Tak?

**Adrian Kotowski**: Tak, czyli to powiedz różnie, komuś po prostu.

**Lukasz Bott**: Dobra, no i to oznacza, że ktoś inny się tym będzie musiał...

**Adrian Kotowski**: Bo to nie jest jakiś skomplikowany temat. No ja jeszcze mam te aplikację SignApp na na na na Maca, więc no też jeszcze tych aktualnie tematy które liczy. Więc no chciałbym zmienić zachować ryzyko robię.

**Lukasz Bott**: Dobra, idź do tych, idź do tych e-Doręczeń, a my tu już ustalimy, ustalimy wewnętrznie tak zarządziliśmy ktoś, kto będzie realizował jeszcze ja potwierdzę te daty, bo to... Poprosiłem, poprosiłem osobę zlecającą w tym przypadku to jest Mateusz, tak, żeby podał te daty, podał terminy, przy czym ja zasugerowałem, to moja była sugestia, że nie nie zajmiemy się tym wcześniej, nie wcześniej niż ewentualnie w kolejnym sprincie. Może to jest jeszcze ewentualnie do przedyskutowania, przy czym tu ta Marba ten konkretny temat w Marbie no... z opisu gdzieś tam wynika, że to też jest mały pożar, tak, no dlatego też niekoniecznie musimy... Jakoś nie powinniśmy z tym zwlekać. Tak no ktoś gdzieś coś głupio powiedział, że że to jest do zrobienia tak i... Jak klient się kłóci z nami, że coś tam obiecujemy ani realizujemy i w ogóle tak.

**Damian Kaminski**: No dobrze, tylko pytanie, kto się tym zajmie jak nie ma Adriana.

**Lukasz Bott**: Słuchaj. Zostawmy to na zaplanowanie na jutro. Tak, mamy planowanie sprintu. Tak więc...

**Damian Kaminski**: OK.

**Adrian Kotowski**: No dobra, to jak właśnie ten niepotrzebny to ale ty trzeba jeść?

**Damian Kaminski**: Dobra to, ale kontynuujmy te tematy.

**Lukasz Bott**: Ewentualnie ewentua... To ja poproszę jeszcze w przyszłym tygodniu, żeby tutaj doprecyzował, jeżeli coś tam trzeba wymaga doprecyzowania takie pomysły. No dobra, wracamy do... Jeszcze jeszcze zweryfikuje ten Comarch Hub, kiedy oni tam te terminy postawili. Żeby nie było jakieś wtopy? No dobra ludzie, no to to spokojniej trochę. Dobrze. Tak się... Tak się mają sprawy na ten...

**Damian Kaminski**: No jeśli nic nie zaskoczyło, to ostatnio to przelatywaliśmy tak bardzo pobieżnie i oceniliśmy, że wszystko ma ten sam priorytet, więc według mnie idźmy po kolei.

**Lukasz Bott**: Wy... No wiesz, więc...

**Damian Kaminski**: Pierwsze, czyli stworzenie funkcji do komunikatów statycznym tekście możemy, możemy to...

**Lukasz Bott**: Przeczekaj, otworzyłem pierwsze, no to, no to pierwsze.

**Damian Kaminski**: OK, to przepraszam, dobrze, dobrze, dobrze to wejdź.

**Lukasz Bott**: Problemy z historią spraw, część pierwsza.

**Damian Kaminski**: Czy... To jest dużo większe wyzwanie niż tutaj proste zapisanie, to omawialiśmy na spotkaniu z konsultantami, czyli dzisiaj w bazie danych zapisujemy tekstem w tabeli historii, nazwy techniczne pól. Problem polega na tym, że nazwy techniczne nie odpowiadają wyświetlanym no i analiza historii może być trudna w interpretacji.

**Lukasz Bott**: OK.

**Damian Kaminski**: Więc wymagałoby to zapisywania w historii odnośników jakichkolwiek i wyświetlania tego w formie... Nie tyle co wyświetlanej co, no w formie po prostu jakichś odniesień, żeby wyświetlać historię w formie...

**Lukasz Bott**: Nie odnośnie nisko...

**Damian Kaminski**: Aktualnego języka.

**Lukasz Bott**: To znaczy w historii trzeba było zapisywać w jakiś sposób identyfikator pola tego tak, no jeżeli chodziło ci o to tak, o mówiąc odnośnik pytanie.

**Damian Kaminski**: Tak, tak, tak. Odnośnik tak, tak, to miałem na myśli, że to nie nie powinno być zapisane tekstem tylko wtedy powinno być właśnie jakimś tak jak powiedziałeś na przykład ID-kiem.

**Lukasz Bott**: ID pola i wtedy renderując, wyświetlając historię, odwołujemy się po ID-ku do tego pola i sprawdzam... planuję jakie ma jakim...

**Damian Kaminski**: To by było idealne. Natomiast pytanie, czy jesteśmy w stanie i czy warto robić krok pośredni, czyli na przykład, jeśli zostajemy przy tekście, bo odnosić te te ID-ki jest dużo większym tutaj wyzwaniem, to moglibyśmy zapisywać nazwę techniczną, a w nawiasie nazwę wyświetlaną i dalej pozostać przy tekście. Jeśli to jest szybka poprawka, to już pewnie by w jakiś sposób ułatwiała.

**Lukasz Bott**: No. No tak. Ale Damian...

**Damian Kaminski**: No i tu nie wiem pytanie do Piotra.

**Lukasz Bott**: Damian moment tylko tutaj zagadnienie jest takie, że wchodzą wersję językową, nie.

**Damian Kaminski**: No... No wiesz pytania czy minimum nam nie wystarczy, bo tych języków to to nie ma tak dużo klientów tak, zwłaszcza ten klient on mówi o o wyświetlanych, bo to chyba dotyczy akurat LPP, więc to...

**Janusz Bossak**: Problem.

**Lukasz Bott**: Nie no Neuca.

**Damian Kaminski**: Neuca no ale to no to mówimy raczej o polskim kliencie. No ja mówię o kroku pośrednim, który pewnie jest najprostszy, który pewnie szybko da się zrobić, bo pobrać oprócz nazwy technicznej nazwę wyświetlaną to jest chwila.

**Janusz Bossak**: Ale wyświetlana w tamtym czasie, w którym nastąpiło zdarzenie, mogła być inna.

**Damian Kaminski**: I zapisanie tego. No tak, zgadza się wtedy nie mamy...

**Piotr Buczkowski**: On pobiera kto aktualną wersję aktualna nazwę?

**Janusz Bossak**: Dlatego zapisujemy starą nazwę, znaczy tą, która była w tym momencie.

**Piotr Buczkowski**: Znaczy nie, w historii, w historii nie zapisujemy nazwę wyświetlany.

**Damian Kaminski**: Tak, tak, tak.

**Janusz Bossak**: A nie zabierzemy. Ja mam dobrze.

**Damian Kaminski**: Nie, obecnie momencik to...

**Piotr Buczkowski**: Nie.

**Damian Kaminski**: Co zapisujemy w historii? Zapisujemy tekstem, tak.

**Piotr Buczkowski**: Tekst tak, nazwę na ID i tekst ta pola, filmik i nazwę.

**Damian Kaminski**: Tekst, czyli pobieramy...

**Piotr Buczkowski**: Tą taką...

**Damian Kaminski**: Techniczną.

**Piotr Buczkowski**: Techniczną co jest niepotrzebne, bo to to było po to, żeby właśnie przejrzystość na różnych teorii nie trzeba było jakoś sięgać po nazwę. Też, żeby te historyczne nazwy trzymać. No ale jak doszły nazwy te plany, to uznałem, że to nie ma sensu zapisywanie tego, bo to bardzo by rozbiło... Nie rozbiła, zwiększyło rozmiar tej historii, utrudniło analizę tak.

**Damian Kaminski**: Ale to ja teraz nie zrozumiałem tego, co powiedziałeś. W sensie zapłaciłem i ja ID i nazwę techniczną a wyświetlamy co?

**Piotr Buczkowski**: Nie. Nie wyświetlamy powinniśmy dobrze, nie pamiętam.

**Damian Kaminski**: Dobra, bo słuchajcie, mamy...

**Piotr Buczkowski**: Zdawało mi się, że to było. Zdawało mi się, że to było zmienione, tak.

**Damian Kaminski**: Mamy taki kontekst, pytanie, co my chcemy wyświetlać tak, czy chcemy wyświetlać bieżące, czy te historyczne wydaje mi się, że historyczne, bo to jest historia.

**Piotr Buczkowski**: Bieżące. Bieżące chcemy być jakoś...

**Damian Kaminski**: Bieżące OK. Czyli musimy się odnosić po ID.

**Piotr Buczkowski**: Nie będziemy, nie będziemy, nie będziemy wyświetlać historycznych, bo nie mamy takich danych i nie chcemy mieć zbierać takich danych.

**Damian Kaminski**: Zostały usunięte, to po to jest ta nazwa, tak?

**Piotr Buczkowski**: Jeżeli pola zostały usunięte, to jest jako nie nie zostało usunięte, tylko zostało deaktywowane. Nadal jest.

**Damian Kaminski**: OK.

**Lukasz Bott**: Czyli, czyli odwołanie ten ID, działa tak wciąż tylko...

**Piotr Buczkowski**: Tak.

**Damian Kaminski**: Dobra no to dobrze, czyli wyświetlamy bieżące, czyli w zasadzie wyświetlenie bieżącej, czyli cały mechanizm już jest wyświetlenie bieżącej nazwy wyświetlanej, to jest tylko i wyłącznie odpytanie dodatkowe.

**Piotr Buczkowski**: Tak i z cofało mi się, że to jest zrobione, być może jakiś kod przypadek nie działa, ale to moment muszę sprawdzić.

**Damian Kaminski**: Dobrze, ale jeszcze porozmawiajmy biznesowo, bo ja jestem za tym, żeby wyświetlać i jedną i drugą wartość, ponieważ nazwy wyświetlane mogą być zduplikowane z jakiś różnych powodów, więc nie dają jednoznacznego wskazania z poziomu tego interfejsu, więc wtedy musielibyśmy na przykład w nawiasie wyświetlać techniczną albo odwrotnie, czyli wyświetlać 2 w języku. Jeśli nie ma w języku to domyślną, czyli tak jak się w tym momencie wyświetla użytkownikom na formularzu plus techniczną pytanie, która w nawiasie, która pierwsza.

**Piotr Buczkowski**: Bardziej techniczna bym by robił jako nie wiem pod tooltipem czy coś.

**Damian Kaminski**: A w ten sposób no to też można.

**Piotr Buczkowski**: I to jest różna tak, jeżeli jest różna, oczywiście.

**Damian Kaminski**: Znaczy można by to wyświetlać zawsze? Żeby ktoś miał pewność tak, bo jak będzie raz tulip się wyświetlał a raz nie no to będzie tak...

**Piotr Buczkowski**: No nie, nie nie, no bo szkoda miejsca naprawdę będzie mylące, tak.

**Damian Kaminski**: Niezrozumienie. Tak.

**Lukasz Bott**: A w tym czekajmy Daniela w tym nowym interfejsie sprawy to historię myśmy już ogarnęli prezentowanie historii, czy to jeszcze jest przed nami?

**Damian Kaminski**: Nie. Jeszcze raz zadaj pytanie.

**Lukasz Bott**: Na przykładzie mamy, mamy historię.

**Damian Kaminski**: Chyba, że to tu działa to, co Piotr ma na myśli.

**Lukasz Bott**: No nie, to jest akurat się akurat w tym konkretem procesie to się nazwy pokrywają systemowym.

**Damian Kaminski**: No i i zadaj pytanie.

**Lukasz Bott**: Nie no moje pytanie było, rozumiem, że to coś co teraz wyświetlam to jest tak naprawdę wersja, która dotyczy dotychczas.

**Damian Kaminski**: To samo tylko inny inny wygląd.

**Lukasz Bott**: Troszeczkę inny wygląd tak tam ładniejsze, ale co do zasady tak samo dobra. Nie, bo gdzieś mi się tam rzuciło w oczy jakieś te, ale to chyba dotyczyło tabelek i że jakoś tam inaczej pokazujemy zmiany w tabelach, dobra.

**Damian Kaminski**: To znaczy cała historia w ogóle jest do zaopiekowania i pytanie, czy do tego tak podchodzić indywidualnie typu jest tego typu zgłoszenie, czy jednak podejść do tego kompleksowo i wtedy trzeba rozpisać, bo mamy tak mamy historię, czyli to zgłoszenie, mamy historię pól, która była też teraz jest na dole, a może powinniśmy wprowadzić tutaj widok zakładkowy? Do historii pól, żeby to się wygodnie czytało, bo jeszcze jest ta historia biznesowa i może powinniśmy do całej panelu historii podejść kompleksowo, czyli określić MVP dla tych wszystkich 3 elementów. Bo jest jeszcze zgłoszenie dotyczące historii pól już pokazuje. Mm. Sekundkę. Nie mogę tego znaleźć, Mateusz zgłaszał, no nieistotne. Był na to też projekt, żeby po prostu taka była propozycja. Na razie nie mówię, że tak musi być, żeby po wejściu na historię były 3 zakładki na górze tam, gdzie mamy napis historia, byłaby historia sprawy, którą teraz widzimy. Kolejna zakładka historia biznesowa, którą mamy backendowo, nie mamy frontendu do wyświetlania i trzecia zakładka historia pól, która by była po prostu wygodniejszy sposób niż ta, która jest obecnie prezentowana już w samym sidebarze, a nie dodatkowym... modelu, czyli tam wybieramy sobie z listy rozwijanej wśród wszystkich dostępnych pól, które pole nas interesuje. No i dostajemy zestaw informacji, kto i kiedy zmieniał wartość w tym polu. Ee z filtrami, no takimi jaki tutaj, tak po prostu już po nowemu. No i teraz pytanie ogólne do wszystkich, no pewnie tutaj głównie do do do Kamila Janusza, bo bo Kamil się zajmował też tym tematem. Czy opiekujemy ten pojedynczy, to pojedyncze zgłoszenie, czy planujemy pracę nad całą historią i wtedy rozpiszemy, co jest MVP?

**Janusz Bossak**: Trudno powiedzieć.

**Kamil Dubaniowski**: Tam wraca ten wątek historii biznesowej, to samo wczoraj poruszałyście, ale to to nie jest mały temat.

**Piotr Buczkowski**: M... Mogę jeszcze wrócić do nazw wyświetlanych tam?

**Damian Kaminski**: Tak.

**Piotr Buczkowski**: Zostało poprawione wyświetlanie nazw wyświetlanych w wartościach słowników. Czyli jeżeli masz słownik Dzień Tygodnia, gdzie są wersje powiedzmy po angielsku, po polsku, po niemiecku to uciekli wartość wybraną po polsku, po niemiecku, po angielsku w zależności od tego kto ma jakiś język. A nie zostało poprawione wyświetlanie nazwy pola wersji językowej.

**Damian Kaminski**: Czy wartości tylko zostały poprawione, a nie?

**Piotr Buczkowski**: Tak, tak.

**Damian Kaminski**: Dobra, no to słuchajcie.

**Piotr Buczkowski**: Ale poprawka na godzinę, tak?

**Kamil Dubaniowski**: No bo tak czy inaczej to będzie trzeba zrobić, czy zrobimy nową historię, czy nie.

**Damian Kaminski**: Że... Ale poczekaj, poczekaj, poczekaj to co Piotr powiedział poprawka na godzinę, żeby dopisać po prostu nazwę wyświetlaną tak.

**Piotr Buczkowski**: Tak. Mamy mamy, mamy obiekt... zamiast Value można wybrać wpisać DisplayValue. Zrobić.

**Damian Kaminski**: No to zróbmy to, to jak to jest na godzinę, to zróbmy to i na razie zamknijmy.

**Piotr Buczkowski**: To czy przepisz przepisz do mnie zaraz po spotkaniem będzie zrobione.

**Damian Kaminski**: Tylko poczekaj Piotr, ustalmy w jakiej formie, bo ja bym nie wymieniał jeden do jeden tylko albo ten tooltip, który powiedziałeś też.

**Lukasz Bott**: Dobry.

**Piotr Buczkowski**: Aha.

**Damian Kaminski**: Albo jeśli bez tooltipa, no to 2 parametry.

**Piotr Buczkowski**: Nie to... Powiedziałem może być za dużo 2.

**Damian Kaminski**: Będzie nieczytelne.

**Piotr Buczkowski**: Boje się. Tak, tak.

**Damian Kaminski**: No dobrze, czyli musiałbyś wtedy dorobić jeszcze jakieś endpoint do tipa tak i potem frontendu wiec musiałby się tym zająć a jest gotowy, tak?

**Piotr Buczkowski**: A po co? To po co? A po co? No to się title dodaje span title i tyle i bootstrap to obsłuży, wszystko resztę obsłuży.

**Damian Kaminski**: W sensie, czy ty zrobisz to kompletnie, czy ktoś jeszcze będzie musiał dorobić ten?

**Piotr Buczkowski**: Ja jej. Ja to zrobię kompletnie zmiana jest tylko w kontrolerze. Zwracamy...

**Damian Kaminski**: OK.

**Piotr Buczkowski**: Nazwę w parametrze tip obóstwa to obsłuży, żeby to jakoś to oczywiście być.

**Damian Kaminski**: Dobra, to Łukasz, jak możesz to wpisz, że... zmieniamy treść historii na nazwę wyświetlaną. A jeśli nazwa wyświetlana nie pokrywa się z techniczną, to pojawi się tooltip po najechaniu na... na dane pole. Nazwy wyświetlane, historia będzie prezentować nazwy wyświetlane czy też językowe. Tak Piotr to będą wyświetlane czy będą w języku?

**Lukasz Bott**: Czyli jeśli?

**Piotr Buczkowski**: No... wyświetlane. Nazwa wyświetlana może być mieć wersji językowej.

**Damian Kaminski**: OK. To napiszmy od razu w tym w tym obsługa języków.

**Lukasz Bott**: Czyli to tak jakby...

**Piotr Buczkowski**: DisplayValue. I warto. Pobiera albo wersje językowe, jeżeli są zdefiniowane, albo to domyślne nazwę wyświetlaną, jeżeli jest tylko jedna zdefiniowane.

**Damian Kaminski**: No to świetnie.

**Lukasz Bott**: No i teraz no...

**Damian Kaminski**: A jeśli nazwa techniczna nie pokrywa się z nazwą wyświetlaną? Bo najechaniu na nazwę pola wyświetli się tooltip z nazwą techniczną. Wiesz co, weź to od razu przekopiuj do acceptance criteria, bo to dla dziewczyn będzie przydatne, żeby nie musiały tam szukać i...

**Lukasz Bott**: W sumie i tak w sumie to by może było teraz.

**Piotr Buczkowski**: Znaczy, ja jest zwykle inaczej pisze acceptance criteria, ale...

**Lukasz Bott**: Dobra.

**Damian Kaminski**: To jak chcesz to napisz ty, no dobra.

**Piotr Buczkowski**: Uzupełnienie. Ja zwykle uzupełniam akcje typu, że cały stan stał już testowy. Tak staram się opisać.

**Lukasz Bott**: No tak, bo ten piesek już... Tak, tak.

**Damian Kaminski**: OK.

**Lukasz Bott**: Dobra, to Piotrek uzupełnienie jest przypisany do ciebie zdjęte z Rady dzięki.

**Piotr Buczkowski**: Tutaj 3, 3 przypadki będą widzę czy czy albo 4 x 4?

**Lukasz Bott**: Słuchajcie no harmonogramu...

**Damian Kaminski**: Omówmy, drugie drugie jest krytyczne, jeśli mamy jeszcze, jeśli możemy zostać.

**Lukasz Bott**: Dobra, które?

**Damian Kaminski**: Bo te drugie.

**Lukasz Bott**: WIM tak.

**Damian Kaminski**: Tylko tutaj pewnie mało jest więcej. No właśnie dobra sytuacja wygląda tak, omówiliśmy, że będzie raport osadzony na sprawie, który będzie wyświetlał z zasobów źródeł zewnętrznych dane zamówienia, bo tutaj w WIM-ie rezygnują z OCR-a pozycji będą odpytywać na podstawie numeru zamówienia systemu, który te zamówienia przechowuje i potem będą tylko odklikiwać checkboxy, tak jak dzisiaj mamy checkboxy na full raporcie osadzonym. Ee to ta forma jest okej, przy czym oni chcą, żeby te checkboxy się zapisały, czyli żeby były stanem sprawy i to jest wyzwanie. Które tutaj... Zostało, że tak powiem zaproponowane przez nich pytanie, jak my jesteśmy w stanie to zaopiekować dla takiego przypadku.

**Lukasz Bott**: Czyli chodzi. Chodzi ci o to?

**Janusz Bossak**: Źródła statyczne...

**Lukasz Bott**: Tak jak już.

**Janusz Bossak**: Źródło, źródło zewnętrzne, to które tutaj robiliśmy możliwość zapisania tego stanu i trzeba obsłużyć tylko to, żeby w raporcie osadzonym można było dodać, jakby dodatkową kolumnę, która...

**Damian Kaminski**: Mhm.

**Janusz Bossak**: Jest edytowalna tak i ten checkbox.

**Damian Kaminski**: O no właśnie. To jest to. To jest idea biznesowe. Pytanie teraz, jak tutaj deweloperzy się do tego ustosunkują.

**Janusz Bossak**: Bo wiecie, bo to w tą stronę trochę pójdzie tak, bo jeżeli mamy też źródła statik dynamiczny, których możemy coś zmieniać, zaraz się okaże właśnie, że trzeba coś w nich zmieniać. I zaraz się okaże, że wygodnie byłoby to zmieniać jakby w tabelce tak, czyli w takim trochę raporcie nie.

**Damian Kaminski**: Zmieniać masowo. Mhm.

**Janusz Bossak**: Cokolwiek tam jest, jakaś data tak dalej, tylko że nie zmieniamy jakby wtedy w CaseDefinition w sprawie tylko zmieniam w tym źródle, tak? Może to jest kolejny etap kolejny MVP? Kolejny wydanie tej funkcjonalności, żeby dać możliwość bezpośredniej pracy z formularza na tych danych, które są zapisane w tym źródle takim dynamicznym, no jako pierwszy.

**Damian Kaminski**: Tak, przy czym tu mówimy, o starych raportach nie, bo to jest kontekst raportu osadzonego.

**Janusz Bossak**: No wiem, no kontakt z raportu osadzonego to jest w ogóle temat, który byśmy musimy przetworzyć, no bo na razie i tak mamy i pewnie przez jeszcze rok 2 będziemy mieli, dopóki będziemy mieli mCase w starej technologii, a w końcu przejdziemy na Reacta. To nie wtedy będziemy mieli Reactowych. No ale na razie tak musimy zostawić.

**Damian Kaminski**: Dobrze czy nie wiem, Piotr, ty tu widzisz jakiekolwiek takie ryzyka, że tego w ogóle się nie da?

**Piotr Buczkowski**: Nie wiem. Musiałbym się przeanalizować, jak to jest zrobione.

**Damian Kaminski**: No dobrze, no to...

**Piotr Buczkowski**: Znaczy dać się da na pewno pytanie, czy da się da się to prosto zrobić tak czy jakoś tak...

**Janusz Bossak**: Dokładnie jak to...

**Piotr Buczkowski**: To może nie tyle wydajnie co jakoś ładnie.

**Janusz Bossak**: Dokładnie, dokładnie o to chodzi, tak?

**Damian Kaminski**: Dobrze, ja to w takim razie rozpiszę i zrobię jakiś do tego Proof of Concept. No i dobra, no to w takim razie mamy to ustalone jak jak jak ma to wyglądać.

**Lukasz Bott**: Czyli to...

**Damian Kaminski**: Przypisz to do mnie, bo nie wiem, czemu to zrobiłeś, to czy to nie było do mnie?

**Lukasz Bott**: Nie, ja nic nie nie...

**Damian Kaminski**: Może ja coś nie nie zapisał?

**Lukasz Bott**: Nic nie ten no i design tak i zdejmuje z Rady.

**Damian Kaminski**: Tak. Dobra, reszta jest z niższym priorytetem. Jak chcemy to możemy, no bo cały czas nam nie starcza czasu, żeby to przejść. Możemy jeszcze jedno zrobić, a resztę kontynuować. Najwyżej w czwartek wtorek przepraszam. Czekaj te te maile, trzecia pozycja to można odpiąć, bo to ustaliliśmy i zrobiłem już na to zgłoszenie. Nie wiem, czy Piotr już to zaopiekował, ale jest przypisany, więc to odetnijmy, no niech nam nie będzie, bo to...

**Piotr Buczkowski**: Chodzi o...

**Damian Kaminski**: Ten. Custom Template.

**Piotr Buczkowski**: Wyłącz zaznaczenie że customowy to już jest, nie wiedziałem, że to jest. Kurcze, zrobiłem samodzielne zgłoszenie, nie wiedziałam, że jest.

**Damian Kaminski**: No to... Nie, nie. A wczoraj ci wysłałem mnie wczoraj przedwczoraj po Radzie.

**Piotr Buczkowski**: A to dobrze to tam, no tamto zgłoszenie.

**Damian Kaminski**: No właśnie OK. To jest inne, bo to jest dotyczy szerzej, więc to nie chce u mnie wisi. Bo to jest na przyszłość. No dobra, to jeszcze te środkowe jest ciekawe i według mnie warte w końcu zaopiekowania no.

**Lukasz Bott**: No to...

**Damian Kaminski**: Czyli statyczny komunikat.

**Piotr Buczkowski**: Aniu, pamiętasz robiłaś?

**Janusz Bossak**: Zrobiło to już zrobione.

**Piotr Buczkowski**: Tylko... Zrobiłeś?

**Janusz Bossak**: Znaczy, według mnie tak było robione kiedyś.

**Damian Kaminski**: Kto zrobił?

**Janusz Bossak**: I miał to...

**Piotr Buczkowski**: Tak nie robiła.

**Janusz Bossak**: Ania robiła i to Łukasz po skrobko ma możliwość gdzieś tam włączania w czymś. Żeby się pojawiał.

**Piotr Buczkowski**: Ale nie używała tego nigdy to nie było wszyte.

**Janusz Bossak**: Ale jest zrobiony.

**Piotr Buczkowski**: Jest zrobione w starym, starym widoku. Wątpię, żeby w Reakcie ktoś to zrobił.

**Janusz Bossak**: Możliwe. No no no no no OK.

**Damian Kaminski**: No dobra, no to wiecie, to już jeśli coś jest to to jest jakiś zalążek, to znaczy tak, jeśli na to spojrzeć szeroko. Znowu to można to podzielić na 2 On-Premise, czyli wypełniane jednorazowo. Natomiast według mnie super by było, gdybyśmy to zaopiekowali też w kontekście chmury, gdzie Łukasz mógłby z jakiegoś narzędzia...

**Piotr Buczkowski**: Tak, to to, to, to to było tak robione tak planowane.

**Damian Kaminski**: OK no dobra, dobra, no właśnie, żeby Łukasz rano mógł opublikować, że dzisiaj o siedemnastej, osiemnastej dziewiętnastej będzie niedostępność systemu przez 15 minut. I wszyscy to widzą i nie musi nikt pisać maili nie musi być, że tak powiem jakiejś gość napięcia, że ktoś nie wiedział, nie przeczytał, bo za późno. Wysłane wyświetlamy w aplikacji tyle.

**Janusz Bossak**: Pojawił taki pasek u góry nad aplikacją.

**Damian Kaminski**: Tak na ekranie głównym można go pewnie zamknąć, albo no jak ktoś przeczyta to można zamknąć po prostu, żeby nie przeszkadzał, żeby nie zajmował czasu miejsca. Przepraszam.

**Janusz Bossak**: No. Znaczy trzeba się do tego, że tak powiem dokopać, zobaczyć co było zrobione. Przepisać na nową technologię, ewentualnie i tyle.

**Damian Kaminski**: Dobrze a Ania zgłaszałaś, że masz jakąś przestrzeń jak tam coś jest pilnego to oczywiście tymi innymi rzeczami bo ja bym... No jest jakieś kilka tematów. No właśnie no to zajmie się natomiast jeśli ten hotfix skończysz, to możesz zrobić tutaj, czyli napisać jaki jest stan obecny, skoro ty to robiłaś?

**Anna Skupinska**: Hotfix do zrobienia. Dobra.

**Damian Kaminski**: Ee no i zostawmy to jeszcze na Radzie według mnie.

**Piotr Buczkowski**: Już już mogę już mogę pokazać.

**Anna Skupinska**: Ach ja mówiłam, a miałam wyłączony mikrofon, tego nie słyszeliście.

**Piotr Buczkowski**: Jak się jeżeli wejdziecie na stronę jest... Takie request do... Nie, sorry, nie nie w tym. Info o bar to teraz user zawsze pusto. Tak to sobie, bo o to chodzi.

**Damian Kaminski**: Ja nie mam pojęcia.

**Janusz Bossak**: Miałem coś...

**Lukasz Bott**: Coś mam gdzieś wpisać jakiś adres w coś?

**Piotr Buczkowski**: Wejść na jakąś stronę naciśniemy F12.

**Lukasz Bott**: Tak tu.

**Piotr Buczkowski**: Akt właśnie React no.

**Damian Kaminski**: Musisz wejść na stare widok?

**Piotr Buczkowski**: Ale dobrze, poczekajcie, naciśnij F12.

**Janusz Bossak**: Zbadaj sprawę no.

**Piotr Buczkowski**: Naciskamy F12. Weź tak na na DevTools. Nadal nadał zakotwiczyć, żeby było widoczne i to i to tak.

**Damian Kaminski**: Zmniejsza.

**Piotr Buczkowski**: No dobrze odśwież stronę. Właśnie tej Network.

**Lukasz Bott**: Durne.

**Piotr Buczkowski**: Po co? Miał nie być nagłówkach, nie potrzebujesz? Weź tą środkową część pokaż większy.

**Lukasz Bott**: Dobra mnie rzucą nieco moment.

**Piotr Buczkowski**: Nie nadal będzie szczątkowo część pokaże, ta dolna nie jest potrzebna albo sam taki konsul na dole nie jest potrzebna. Kończenia możecie masz wrogów, a gdzie masz wyświetlanie to co chce?

**Damian Kaminski**: Do samej góry, bo to jest na dole, pewnie to na górze się ładują.

**Piotr Buczkowski**: Gdzie masz żądanie, że ich hcesz tylko. Nie masz co zawsze, czyli to?

**Janusz Bossak**: W Sejmie ekran i pokaz gdzie szybciej niż to.

**Lukasz Bott**: Tak, Piotrek, muszę szybciej tam będziesz, no.

**Damian Kaminski**: No właśnie.

**Piotr Buczkowski**: Dobrze. Już. Jest moją witrynę, tak jest takie coś takie coś zwracam. Strefa 3. A nie ma.

**Damian Kaminski**: No dobra, no to nie ma po stronie reaktywnej tak.

**Piotr Buczkowski**: Chodzi o to, tak. Z logami. Chron sobie tutaj. Jakoś budowano tak.

**Lukasz Bott**: Do tego jest jakiś interfejs, żeby sobie to na przykład czas gdzieś się stawić.

**Piotr Buczkowski**: Właśnie.

**Anna Skupinska**: Strasznie cicho Piotra słychać.

**Damian Kaminski**: Ale w ustawieniach systemowych nie ma tego tak.

**Piotr Buczkowski**: Bo to nie jest, bo to nie jest per witryny. No to jest per chmuro per Server.

**Damian Kaminski**: OK. Czyli to nie jest rozwiązanie, On-Premise-owe.

**Piotr Buczkowski**: Czas zrobić, żeby było On-Premise.

**Damian Kaminski**: Dobra, jasne, jasne. Dobrze, to może tak ustalmy co jest do zaprojektowania w ramach tego dzisiaj to jest... Działa tylko On-Premise.

**Piotr Buczkowski**: Będzie to sorry, to też trochę wolniej chodziło. To nie o to chodzi, bo to było tak. Mój błąd sorry.

**Damian Kaminski**: Czy pomyliłeś, czy w ogóle tego nie mamy?

**Piotr Buczkowski**: Jest to pewna, który należy wpisać, tak? Wręcz po polsku, część po angielsku, od kiedy do kiedy nie pamiętam, nie pamiętam, nie pamiętam, nie jedno albo 2 0 jakby jeden.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: Ta pani się wyświetlać? Tak?

**Damian Kaminski**: Dobrze, ale... To może ogólniejsze pytanie Ania to robiła tak to, jaki był cel biznesowy czy Ania, pamiętasz? Co to miało obsługiwać?

**Piotr Buczkowski**: Dokładnie dokładnie to co mówiliśmy tak, czyli na przykład ostrzegać użytkowników o instalacji.

**Damian Kaminski**: OK dobra. Dobrze, to zostawmy to na razie Ania zrób do tego research spisz co mamy, jakie były według ciebie założenia i wtedy przypiszemy, czyli żeby mieć stan na dzisiaj i wtedy będziemy w stanie podjąć to w ramach projektu, czyli jak ma być to docelowo, czy to co dzisiaj mamy wystarcza czy coś rozszerzamy? No i trzeba będzie to rozpisać dla chmurowych, żeby móc tym zarządzać zbiorczo, a dla On-Premise-owych, żeby każdy mógł to administrator wypełnić po stronie swojego interfejsu i... i opublikować.

**Anna Skupinska**: To jest ciągle to samo zadanie związane z informowaniem użytkowników, o tym, że mąż będzie za jakiś czas badanych wyłączona coś innego.

**Piotr Buczkowski**: Tak, tak.

**Damian Kaminski**: Dowolna informacja, na przykład baza danych może być tam inne informacja kluczowa.

**Anna Skupinska**: OK. OK. To ok. OK. Czyli tak spróbuję znaleźć.

**Piotr Buczkowski**: Dobrze to było na stronie logowania, widzę, aby przynajmniej to jest.

**Damian Kaminski**: No dobrze, to ustalmy właśnie jaki jest stan bieżący, tak, żeby właśnie strona logowania w przypadku SSO nie działa, raczej powinno być to na stronie głównej. Jak wchodzimy, to widzimy w górnym gdzieś tam części ekranu można to zamknąć. Wyświetla się to raz.

**Lukasz Bott**: Jako jest co jako pasek? Moim zdaniem to powinno być jako pasek taki.

**Piotr Buczkowski**: O ta jest tak.

**Damian Kaminski**: Tak dokładnie.

**Lukasz Bott**: No są na samej górze, tak jak mieliśmy tą informację o tym nie wiem Raportach Premium tak albo coś w tym stylu.

**Anna Skupinska**: Tylko, że jedna rzecz, jeżeli baza danych nie działa, to nikt się nie zaloguje, więc to powinno być na stronie logowania.

**Damian Kaminski**: Dokładnie te...

**Janusz Bossak**: No tak.

**Piotr Buczkowski**: Jeżeli jeżeli baza nie działa, to stan logowania też się nie wyświetli.

**Anna Skupinska**: Tak.

**Damian Kaminski**: Nie. Nie, ale to słuchajcie, nie nie o to chodzi. Chodzi o to, żeby poinformować przekonań w trakcie. To nie chodzi o to, żeby teraz się wykonuje. Update, to chodzi o to, żebyśmy my robiąc dzisiaj update od siódmej rano wyświetlali, że w dniu dzisiejszym o godzinie 18:00 serwery aplikacja będzie niedostępna i tyle, a nie w trakcie. W trakcie to już jest po fakcie już nikogo to nie interesuje, nie działa i tyle.

**Lukasz Bott**: Ta ta.

**Piotr Buczkowski**: Tak, tak.

**Lukasz Bott**: Aby na kilka dni wcześniej.

**Damian Kaminski**: Więc to ma działać jak działa? Aplikacja ma być dostępne, że to wolnych powodów. Może tam ktoś będzie chciał wyświetlić jeszcze coś innego, tak, że nie wiem...

**Lukasz Bott**: No niedzielę idziemy na imprezę, czyli tak.

**Damian Kaminski**: Kończymy pracę w tak dzisiaj o czternastej, to już będzie zależeć od od administratora. Chodzi o to, że była na to przestrzeń.

**Piotr Buczkowski**: Dobrze ten mechanizm jest nawet jest wywoływany, czy jest wyświetlany na nowej strony logowania? Nie mam pojęcia.

**Damian Kaminski**: Dobrze do Ani jest to przypisane, niech to zrealizuje.

**Piotr Buczkowski**: Nie chcę, to nie chcę to z tego testować, żeby innym użytkownikom tego nie wyświetlić, tak.

**Anna Skupinska**: Mhm.

**Damian Kaminski**: Dokładnie, więc to lokalnie trzeba gdzieś tam odtworzyć.

**Anna Skupinska**: Mhm.

**Damian Kaminski**: Dobra to. Resztę zrobimy na kolejnym coś coś popchnęliśmy.

**Lukasz Bott**: Dobra.

**Damian Kaminski**: Dzięki cześć.

**Kamil Dubaniowski**: Janusz Damian, nie wiem jak chcecie, to chciałbym jeszcze chwilę z wami. W sensie coś wam pokazać, co zwróciłem Przemkowi, wszyscy jak to zrobił, żebyście tylko nie powiedzieli, czy to jest według was OK. Reszty nie będę trzymał.

**Damian Kaminski**: No.

**Janusz Bossak**: Dobra, dzięki, to zostajemy, ale Piotr i Ania, dziękujemy tak dlaczego.

**Kamil Dubaniowski**: Tak, tak, tak, tak mam 2 minuty dosłownie. No bo Przemek, że to zrobił i chce ode mnie zadanie. Ja chcę najpierw zrobić potwierdzić, że tak idziemy. To było na moim projekcie mamy teraz te ustawienia formularza jest aktualnie przełączanie. Wy mieliście też do tego uwagi Edytor Graficzny, Lista w ten sposób, no i tutaj doszła to trzecia opcja, Matryce Uprawnień to do wersji wrześniowej. W czerwcowej mamy tylko te 2 opcje mi nie do końca pasowało już od początku, że to to...

**Anna Skupinska**: No cześć.

**Damian Kaminski**: Mhm. Mhm.

**Kamil Dubaniowski**: Jest w ogóle jakby nad wszystkim, no bo Formularz Główny niekoniecznie w ogóle na jakikolwiek związek z tą listą pól. Przemek już to przerobił w ten sposób, czyli to spadło na poziom... tu formularza, no bo tego to tak naprawdę dotyczy przełączane między... Formularzem Głównym, a zakładka a tabelami. Te nazwy możemy sobie zmieniać, tu to jest do wywalenia, a przełączanie między Edytorem, Listą a tą Matrycą jest w zakładkach tak jak gdzieś tam ja projektowałem. To bym chciał do czerwcowej jeszcze wprowadzić.

**Janusz Bossak**: Że mam wrażenie, jakbyśmy jeden wiersz stracili.

**Kamil Dubaniowski**: Nie, on był cały czas zajęty.

**Janusz Bossak**: Nie tu jest wyżej form.

**Kamil Dubaniowski**: Tutaj tak wiersz pola tak znaczy właściwie zobaczcie jest na tej samej rozdzielczości, ginie mi tylko to komórki organizacyjne. No to to jest kawałek niżej. No tak, no niewiele a... No potrzebujemy tej listwy tutaj tak czy inaczej, bo ważę tu to znaczy.

**Janusz Bossak**: No i wtedy będzie Edytor Graficzny, Lista i Matryca Akceptacji tak naczytam uprawnieni na tej liście, znaczy tutaj na tym pasku dzieje z etnograficzne i lista.

**Kamil Dubaniowski**: Tak. Tak tak, docelowo będą 3 pozycje.

**Janusz Bossak**: Znaczy, pamiętam, nie znam się na tym, jak się do końca, ale Justyna jakoś mocno broniła tezy, że nie powinno tak być, że mamy z lewej strony... Taki wybór jak mamy, czyli listy, a po prawej jeszcze mamy zakładkową listę nie to niby nie jest UX-owo dobrze, ale mamy tak no bo mamy chociażby zakładkowe, które tak dokładnie działają.

**Kamil Dubaniowski**: Wiesz body powiadomienia na stronie głównej już tak robił, no.

**Janusz Bossak**: Mamy takie rzeczy. Znaczy, ja nie mam z tym jakoś problemu.

**Kamil Dubaniowski**: Czy jest na wierzchu? Moim zdaniem jest od razu.

**Janusz Bossak**: To co jest lepiej, to co jest lepiej, to to, że ten właśnie ta rozwijane tam, gdzie jest Formularz Główny, jest w tym miejscu. Tak znaczy mówię o tym tutaj selekcję na środku ekranu, gdzie jest napisane Formularz Główny, o tutaj on tak był tak tam, no przełączny chwilę jak niewiadomo gdzie, nie tak.

**Kamil Dubaniowski**: Nie wiadomo co to jest. Mhm. Nie wiadomo do czego dokładnie. Czy to tyczy się pól czy.

**Janusz Bossak**: No i to jest ok, że to schodzi tam niżej, bo to rzeczywiście dotyczy tego tak i widzę, że teraz wyświetlam formularz główny to jest zmiana jak najbardziej... w porządku.

**Damian Kaminski**: No ale ma to minusy w postaci takiej, że tracimy ten wiersz. Mamy mniejszą przestrzeń roboczą, a gdybyśmy jednak to przenieśli do tego wiersza wyżej, ale na zasadzie tak jak mamy wszędzie filtrów, czyli wyrównamy, to do prawej formularz główny i zobacz dla nazwy systemowe jako forma filtrów dla okna roboczego, ale w tym wierszu, gdzie jest edytor graficzny i lista.

**Janusz Bossak**: No tak i odzyskamy całe wiersze, drugi dzień.

**Damian Kaminski**: Tak.

**Kamil Dubaniowski**: Tylko... On będzie musiał kontekstowo jakby no się zmieniać, tak będzie nam tu migało coś.

**Damian Kaminski**: Tak będzie znikał, tak.

**Janusz Bossak**: Zobacz też, jest widzisz? Wybierz formularz główny na liście, więc jak to będzie?

**Kamil Dubaniowski**: Tak.

**Damian Kaminski**: No ale to też będziemy poprawiać, nie?

**Janusz Bossak**: Nie, ale poczekaj, bo chodzi mi o to, że jeżeli to wybór tego formularza głównego byłby na tym w tym wierszu, w którym mamy teraz te 2 opcje, edytor graficzny lista.

**Damian Kaminski**: Tak.

**Janusz Bossak**: To odzyskujemy tutaj ten jeden wiersz, tak, no, bo jednak i w tym trybie i w tym trybie mamy wybierz formularz, nie.

**Damian Kaminski**: Tak.

**Janusz Bossak**: Więc to to jest OK, natomiast...

**Damian Kaminski**: I te nazwy systemowe też nie wiadomo jak zaprojektujemy listę też mogą się wyświetlać tak jak sobie wybierzemy, więc ten filtr może i pozostanie i tu i tu.

**Janusz Bossak**: Dotyczą i tego i tego, tak?

**Damian Kaminski**: Bo możemy sobie szukać po tym tak, albo Zobacz wszystkie nazwy i wtedy będziemy wyświetlać to tak jak teraz. A na tym niekoniecznie będzie taka dostępna opcja.

**Kamil Dubaniowski**: Wtedy... Damy to do góry, to moim zdaniem trzeba się wycofać z tego, no bo to jest wtedy taką takie dziwne.

**Damian Kaminski**: No to trzeba się będzie wycofać. Masz rację? Tak, tak.

**Kamil Dubaniowski**: Nie będzie to regułą.

**Janusz Bossak**: Tak tak, no cały ten pasek właściwie trzeba wtedy zlikwidować, nie ty nazwę.

**Kamil Dubaniowski**: Tą strzałkę wstecz, tak, że no, bo przynajmniej teraz to zrobił w ten sposób, że możesz szybko wrócić do poprzedniego formularza, które edytowałeś, ale jak damy to tutaj, no to ta strzałka tak w środku ekranu trochę dziwnie wygląda, nie.

**Damian Kaminski**: Tak. No będzie źle wyglądać.

**Janusz Bossak**: Tak tak nie będzie wiadomo.

**Damian Kaminski**: No ale to bym powiedział, że to tam przeładowanie ze strzałką ta strzałka to no jeden klik mniej, bo to musi rozwinąć i wybrać a tu tylko raz klikasz to nie powiedziałbym, że jest jakiś game changer. No nie wiem jak uważacie, natomiast no jednak projektując formularz im większa jest ta przestrzeń robocza formularza, tym jest według mnie wygodniej.

**Kamil Dubaniowski**: Mam dlatego ja bym się zastanowił czy tutaj nie dać jakiegoś przycisku, żeby to sobie otwierać wtedy na full screen tak jak dashboard. Bo to właściwie mogę zwinąć, ale jest mi mało potrzebne. Wtedy wręcz tabelka nie jest mi potrzebna, bo po co mam na całości formularz i pola?

**Damian Kaminski**: Ale wtedy... Mhm.

**Janusz Bossak**: Tak to...

**Kamil Dubaniowski**: Bez tej walki już w tym.

**Damian Kaminski**: No to to jakieś kolejny krok nie. No tak by można było też.

**Janusz Bossak**: Ale... No wtykami dobrze się z tym czuję, że to pójdzie do góry ten formularz główny i zobacz dla.

**Kamil Dubaniowski**: No wydaje mi się, że pewnie trzeba by zrobić jakąś nazwę dla tego, żeby też był no podobnym zobacz dla systemowe i tutaj to nie wiem jakby nazwać.

**Janusz Bossak**: Wyświetlaj wyświetleń.

**Kamil Dubaniowski**: Świętowali.

**Janusz Bossak**: Albo edytuj formularz główny tak, bo to jest edycja. W sumie jesteśmy w edytorze, to raczej edytuj. Albo edytujesz.

**Kamil Dubaniowski**: Mhm.

**Janusz Bossak**: Skoro jest, zobacz dla to edytujesz formularz główny edytujesz jakiś tam tabela, coś tam coś tam nie.

**Kamil Dubaniowski**: No... W sumie w tej zakładce powiadomień też mamy coś na typa tak jest przycisk.

**Damian Kaminski**: No wszędzie to jak wejdziesz na raporty to też jest bym powiedział to spójny.

**Janusz Bossak**: Weź tam jeszcze wrócić, do tego jest chora, bo tam jest problem taki, że jak będzie więcej tych... Tabelek w tabelkach i będą nieszczęśliwi miały długie nazwy. Yy, to to okienko zaczyna być dość takie rozwlekłe nie. No i teraz jakby tu weźmiesz o i weź tam to ostatnie na przykład formularz główny organy i instytucje i coś takiego. No i jeszcze nie daj boże, będzie jeszcze jedno to formularz...

**Damian Kaminski**: Kliknij, jak to tam się powiększał bardzo mocno.

**Janusz Bossak**: Albo to musi być skrócone, ale będzie skrócone. To będzie widać formularz główne organy nie.

**Kamil Dubaniowski**: Czy raczej bym wtedy ciał lewą stronę?

**Damian Kaminski**: Tak, tak.

**Janusz Bossak**: No jakieś kropeczki tak, że wiadomo, że to formularz główny je kropki i to wystarczy. No ale potencjalnie jest szeroko. No i teraz jak to pójdzie na górę. No to jakąś tam przestrzeń będzie zajmować, ale no to jest do opanowania. Tytuł bym dał właśnie edytujesz formularz główny komórki organizacyjne albo edytujesz formularz główny i obok to byłoby. Zobacz dla nazwy systemowe nie. No to wtedy będzie już docelowo ok.

**Kamil Dubaniowski**: Czyli przenosimy wyżej usuwa... Strzałkę wstecz dodajemy nagłówek, to do góry to wywalamy.

**Janusz Bossak**: Mhm.

**Kamil Dubaniowski**: No i tak teraz pytanie, czy jeśli tutaj ustawie formularz główny Jestem w jakiejś tabeli przełączę się na listę? To idziemy w to, że ona w sumie działa. Tej.

**Janusz Bossak**: Marek proszę pięknie, bardzo dobrze. Przypadkowo unexpected behavior, ale jak najbardziej pożądany, tak.

**Kamil Dubaniowski**: Tak pytanie co z matrycą to już na wrzesień będzie do zastanowienia, ale też w sumie mogłoby tak być, że wtedy filtruje mi tylko po polach z tej tabeli Matrix uprawnionych, że Jestem w środku tej tabeli, chociaż ja tam nie przewidywałem w ogóle wchodzenia do środka tabeli, robiłem tutaj, żeby wszystkie pola były na jedną stronę, ale mogłoby tak wyjść.

**Janusz Bossak**: Że przebije tutaj. Tu jeszcze jedną rzecz. Teraz także zwróciłem uwagę reguły tabeli. Na liście są, a nawet to, że graficznym. Jesteśmy w tabeli. Wtedy... Mamy gdziekolwiek tutaj... Obsłużyliśmy tym. Bo albo to musi iść tam w prawy... Panel. Reguły tabeli. Albo musi być noworoczne tej górnej liście tak reguły tabeli. Na tym górnym pasku, który teraz projektujemy? Nie wiem czy nie za dużo rzeczy się zaczyna robić w tej górnym tym wiesz. Jednak czy nie zostać przy takim układzie jak tutaj prezentujesz?

**Damian Kaminski**: Tylko wiedział jak tu będą 3 długie to tutaj też może się nie zmieścić jak ktoś tam wrzucić? 4 wyrazy do do pisu. Pytanie trzeba by się zastanowić jak to dobrze.

**Janusz Bossak**: Ustaliłem.

**Damian Kaminski**: Jak?

**Janusz Bossak**: Wolimy maksymalną szerokość, ale wydaje mi się, że teraz jak tak chwilę nad tym pracujemy. To wydaje mi się, że to jest lepszy układ. Dobrze, że tak klikasz był to właśnie widać. Według mnie to jest lepszy układ, jak to jest tu? W tym miejscu już prędzej bym poszedł, tak jak powiedziałeś Kamil w stronę full screen, czyli zamiast tego meni teraz tam jest już niepotrzebny po prawej stronie to tam takie strzałki do rozszerzenia na cały ekran i wtedy...

**Damian Kaminski**: 2 górne belki znikają tak.

**Janusz Bossak**: Piękne belki znikają tak no bo w pełnym ekranie nie przełączam się między edytorem graficznym a listą, a pracuję po prostu na edytorze graficznym.

**Damian Kaminski**: No to tak zróbmy.

**Janusz Bossak**: Jedna.

**Damian Kaminski**: To zróbmy na razie tak, a jako kolejne rozszerzenie pełne ekran nie nie wpychaj my tego już teraz.

**Janusz Bossak**: Czyli mniej, no to... I tylko tutaj zaopiekuj ten reguły tabeli, żeby tutaj wtedy przy tym się Wyświetl, bo to gdzie mamy je edytować, nie teraz pozostała tylko miejsce przy liście, nie.

**Kamil Dubaniowski**: Tylko pytanie czy no właśnie no bo zostało przy liście. Ta lista jeszcze chwilę z nami będzie. Czy to zostawiamy po stronie edytora graficznego? Te reguły tabeli.

**Damian Kaminski**: Ale nie może być to na polu jak kliknę na tabelę, to jak weź jakąś tabelę kliknij.

**Kamil Dubaniowski**: Czy?

**Janusz Bossak**: Mycie zahaczamy o cały projekt.

**Damian Kaminski**: I tutaj edytuj kolumny tak samo można być obok edytuj reguły. Tyle.

**Janusz Bossak**: Oby tak być. Nie są to dane podstawowe. Prędzej zarządzaj polem.

**Damian Kaminski**: No wiecie, dobrze by było, żeby to też nie było gdzieś mega schowany. Dzisiaj to też jest na wierzchu, żeby nie trzeba było 5 kliknięć robić, żeby tam dojść.

**Janusz Bossak**: No.

**Damian Kaminski**: Nadaj do góry Jeszcze raz te nagłówki, dane podstawowe. Nazywanie tu kolumny. No ja bym to jakoś wpychał w tą pierwszą. Ale no.

**Janusz Bossak**: Może nie są dane podstawowe, no to jest właśnie takie wiecie, no.

**Damian Kaminski**: Rozumiem, rozumiem. No właśnie nie jest to spójne nazwa owo, ale jednak. To jest coś podstawowego pola i.

**Kamil Dubaniowski**: W ogóle to edytuj kolumny deszczu, tak sobie tu powinno być.

**Damian Kaminski**: A kliknij edytuj kolumny co wtedy jest? Przejdziemy na ten formularz o k.

**Kamil Dubaniowski**: I to był to.

**Damian Kaminski**: I teraz teraz dalej mamy topole wyświetlone. No bo w starej liście z tego poziomu to mamy tak, czyli teraz gdybyś...

**Janusz Bossak**: Że będzie no są przyzwyczajenia, też naszych konsultantów tak te reguły tabeli są tu, aczkolwiek one są... Też nieintuicyjne tak, bo ja właściwie, że tworząc reguły... Jesteś w zakładce reguły. Jak pomyślisz o tabeli, to musisz sobie w głowie wykombinować, czy my już to wiemy? Tak, ale... Użytkownik, który pierwszy raz korzystam z tego i trochę się nauczył, że jakieś reguły są...

**Damian Kaminski**: Słusznie.

**Janusz Bossak**: On ma wpaść na pomysł, że o k. Wszystkie reguły robisz tutaj, ale gdybyś kombinując...

**Kamil Dubaniowski**: Tak no to mi właśnie chodziło tak, że że czy wciskać to już na ten nowy edytor graficzny czy już nie nie porzucić tego no mamy tą listę tutaj się edytuję wiem, że teraz to będzie w ogóle nieintuicyjne, ale wrzucamy to, a docelowo reguły będą do do regionu tutaj jakoś komponować wtedy te reguły tabeli też.

**Damian Kaminski**: To trzeba zaopiekować.

**Janusz Bossak**: Ja bym chciał.

**Damian Kaminski**: Tylko wiecie, to jest jedna reguła per tabela to też jest pewna specyfika, ale tak można by to wrzucić tutaj.

**Janusz Bossak**: Ale pomyślmy inaczej o tym, pomyślimy, że reguły dotyczą tul. Wejdź Jeszcze raz proszę na ten nowy. I nie przywiązujemy się, że tabela ma reguły. Kliknij na osobę rejestrującą.

**Damian Kaminski**: Mhm.

**Janusz Bossak**: I po prawej stronie, gdybyśmy mieli sekcję reguły. To byśmy mogli wyświetlać... Reguły.

**Damian Kaminski**: Wszystkie, które się odwołują, tak?

**Janusz Bossak**: Które dotyczą osoby rejestrującej, tak, czyli tam jedną lub drugą stronę, albo...

**Damian Kaminski**: Mhm.

**Janusz Bossak**: To się zmienia, to pole, albo to pole uczestniczy w zmianie czegoś innego? Nie.

**Damian Kaminski**: No dobra, no możemy dodać sekcję reguły i wtedy dla tabeli.

**Janusz Bossak**: Sens i tam robimy reguły dla zwykłych pól wyświetlamy reguły. Ewentualnie może nawet dodajemy, może jakoś tam będziemy mogli edytować.

**Damian Kaminski**: Żeś wypatrzył?

**Janusz Bossak**: Tak. Piksele nie zgadzają słusznie słusznie. Nie trzeba takich rzeczy pilnować, bo to jest podstawowa taka.

**Damian Kaminski**: Tak, tak no.

**Janusz Bossak**: No dobrze czyli. Robimy sekcje po prawej stronie reguły.

**Damian Kaminski**: Znaczy, po pierwsze, to tak robimy sekcje, co czy to robimy w ramach czerwcowej, czy jednak reguły zostawiamy tak jak były?

**Kamil Dubaniowski**: No. Tak.

**Janusz Bossak**: Jestem.

**Damian Kaminski**: OK.

**Janusz Bossak**: No widzicie właśnie to jest to rozmowa o MVP zawsze tak teraz byśmy sobie zajrzeli do naszego projektu, tego, o którym mówiłem tych dokumentacji za jeżelibyśmy na MVP i tam byśmy mieli napisane co w tej wersji chcemy dostarczyć i musielibyśmy podjąć świadomą biznesową... Decyzję, że coś umiesz, pan?

**Damian Kaminski**: Znaczy, podejmujemy ją według mnie nie teraz tak, a planujemy już na przyszłe.

**Janusz Bossak**: No to tak. Znaczyli? I tak mówię o tym dokumentacji, którą robimy, no bo siedzę teraz nad tym komunikatorem i rozpisuje to, co tam dałeś. Także ten AI, który tam ci wygenerował z tego v0 to tam bzdury napisał, nie.

**Damian Kaminski**: Mhm. Tak zgadza się, dlatego ci mówiłem, że tam...

**Janusz Bossak**: Tekstu mało wartościowego po prostu. Więc i tak pisze po swojemu. No ale uważam, że coraz bardziej Jestem przekonany, że nakład pracy na dokumentowanie tych rzeczy nam się zwróci wielokrotnie. Teraz będzie dużo roboty, będzie dużo takiego gadania jak tam Piotrek, a po co to na mnie? A kto to będzie pisał i tak dalej. Ale ostatecznie zobaczycie, że to wszystkim nam pomoże. Bardzo, no dziś.
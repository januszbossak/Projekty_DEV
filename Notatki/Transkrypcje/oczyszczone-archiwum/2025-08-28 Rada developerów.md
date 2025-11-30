**Data spotkania**: 28 sierpnia 2025
**Uczestnicy**: Janusz Bossak, Adrian Kotowski, Damian Kaminski, Kamil Dubaniowski, Piotr Buczkowski, Lukasz Bott, Anna Skupinska

**Janusz Bossak**: No hej.

**Adrian Kotowski**: Szybkie pytanie, czy planujemy w trakcie spotkania omawiać tematy odnośnie tego widoku? Zakładki, integracje, stany systemowe? Tak przyszedłem, właśnie liczyłem, że może tutaj też będzie poruszany dzisiaj.

**Damian Kaminski**: Wstępnie mamy to już omówione. Jakie masz pytania?

**Adrian Kotowski**: Oczywiście, to pytałem się Kamila ostatnio, czy jakiś jest projekt na to, bo mnie nie było we wtorek. Po prostu przedstawić... chorobę, tam nie ową, więc tam mam już to opisane, gdzieś tam, jak to ma wyglądać.

**Damian Kaminski**: Kamil to opiekuje, to według mnie Kamil wie co i jak, to pogadajcie we dwóch. To znaczy, na moje, to na ten moment robimy MVP, tak jak się umówiliśmy, czyli nie wiem Kamil, czy unifikujemy już te dwie zakładki w jedno, czy tylko zmieniamy ikonkę i na ten moment...

**Kamil Dubaniowski**: No właśnie o to chodzi, że Przemek zrobił już frontend, to już jest scalone w jedno, tylko tam brakuje backendu pod dodawanie breadcrumbów i tyle. Tak, no w mojej ocenie, no mówię, spotkajmy się może z Przemkiem i Adrian indywidualnie i to pogadamy wtedy.

**Adrian Kotowski**: No dobra, OK, to najbardziej mi chodziło o tę kwestię tych integracji, czyli przykład...

**Piotr Buczkowski**: Czy mogę ja też zobaczyć?

**Kamil Dubaniowski**: Tak, no ja...

**Damian Kaminski**: To jak mamy to, pokaż to, no.

**Kamil Dubaniowski**: A to czekajcie, powiem, to jest na Przemek lokal.

**Piotr Buczkowski**: Znaczy, nie, nie chodzi mi o to, że spotkanie, tak chciałbym...

**Kamil Dubaniowski**: Dobra, to opowiadajcie co to teraz jest, to jakby dla was ważne, a ja się zaloguję zobaczyć, czy to jest na Przemek lokal.

**Damian Kaminski**: Dobra, to nie wiem od czego zaczynamy. Czy ja mam zaczynać? Wtedy Łukasz, coś miałeś? Chcesz zacząć?

**Lukasz Bott**: To znaczy, ja chciałbym zacząć, bo mam dwa tematy, a że o jedenastej zaczynam tam szkolenie dla klienta, no to to po prostu chciałbym przynajmniej moje poruszyć szybko, a ewentualnie sobie tam dokończycie radę.

**Damian Kaminski**: Dobra.

**Lukasz Bott**: Pierwszy temat to na razie must have. Mamy funkcję DeleteCase. I pytanie jest takie, czy coś robimy, czy planujemy robić w zakresie rejestrowania, kto kiedy użył tej funkcji? I to nie może być tak, że to wpisujemy do jakiegoś System Logu, tylko po prostu to musi być permanentne, z UserActivity użytkownika, no.

**Damian Kaminski**: Z UserActivity.

**Piotr Buczkowski**: Jakiej funkcji, nie rozumiem, sorry?

**Lukasz Bott**: Funkcja DeleteCase.

**Damian Kaminski**: DeleteCase. Czy chcemy rejestrować, że taka sprawa o takim numerze... dlaczego ona znikła? W sensie, żeby chociaż zarejestrować CaseID, kiedy i kto ją usunął? Ja wolę coś takiego robiłem dedykowane jako po prostu dedykowane źródło zewnętrzne, bo chcieli w kontekście dokumentów kadrowych.

**Lukasz Bott**: Nawet jest nie, słuchajcie. Dokładnie tak. No i właśnie Damian, i właśnie o to chodzi, że właśnie nie chcemy, że nie chcemy tego robić, tylko musimy to zrobić, bo wielu klientów już się o to dopytuje. Między innymi to klient Gavana, którego dzisiaj szkolę.

**Damian Kaminski**: Tak, ja rozumiem. Mhm.

**Piotr Buczkowski**: Ale co ma być, co ma być rejestrowane?

**Lukasz Bott**: No to co Damian powiedział, minimum numer sprawy, nazwa procesu, z którego to było, data kiedy się to zdarzenie wydarzyło i kto to zrobił.

**Damian Kaminski**: Minimum, czyli... i kto, tak? Czyli bez żadnych danych.

**Lukasz Bott**: Dokładnie. Bez żadnych danych, bo tam czasami w tytule mogą być.

**Damian Kaminski**: Chodzi o to, żeby jak, wiesz, link komuś nie działa, to dobra, nie działa i teraz nie ma sprawy i teraz nie wiadomo co się z nią stało. Kto, co, kiedy. Więc minimum: kto i kiedy usunął.

**Lukasz Bott**: Tak. Ewentualnie z jakimś może komentarzem, dlaczego to usunął.

**Damian Kaminski**: Tylko to spowoduje, że wtedy z kosza nie można usuwać. Ja tak mam zrobione z komentarzem, ale to jest pod przyciskiem. Natomiast to nie będzie skutkować tym, że... W zasadzie nie da się zrobić delete'a ustawieniem systemowym, w sensie dzisiejszą funkcjonalnością systemową z poziomu sprawy, tylko można to usunąć z poziomu kosza.

**Lukasz Bott**: No ale wiesz, to...

**Janusz Bossak**: Słuchajcie.

**Damian Kaminski**: A z kolei to jest lista, więc wtedy co, na liście wyświetlimy modala?

**Janusz Bossak**: Poczekajcie, mówię...

**Lukasz Bott**: Nie no ale...

**Janusz Bossak**: Uporządkujmy temat.

**Lukasz Bott**: Janusz.

**Janusz Bossak**: O którym mówimy? Jest reguła, funkcje...

**Lukasz Bott**: Mówimy o regule funkcji DeleteCase, którą w tej chwili możesz sobie wywołać spod przycisku reguły na sprawie. I jak to zrobisz, bez żadnego tam właśnie dodatkowego rejestrowania... Ja zazwyczaj rejestruję to w logu systemowym, ale log systemowy jest co jakiś czas czyszczony, no to po prostu nie ma w ogóle śladu o tym, kto to zrobił, kto wywołał DeleteCase, czyli to permanentne usunięcie sprawy.

**Janusz Bossak**: Bo tutaj to, co mówi Damian, to skąd wiem?

**Piotr Buczkowski**: No bo po to to jest robione. Jak ma powiedzieć delete, to delete.

**Damian Kaminski**: Tak, to ja mówię szerzej.

**Piotr Buczkowski**: To po co ma być funkcja delete?

**Damian Kaminski**: No tak, tylko czy... Nie, nie, ale tu chodzi o to, Piotr. Nikt nie podważa funkcji delete. Natomiast czasami robią to użytkownicy, bo wiesz, CaseHidden nie pozbywa się sprawy. A czasami jest potrzeba biznesowa pozbycie się sprawy, bo przechowuje ona dane, które ktoś zażądał, że trzeba usunąć. Potem ktoś inny tej sprawy szuka, powiedzmy i wie, co w niej było, ale już jej nie ma. No i teraz zaczynają się wyjaśnienia, dlaczego jej nie ma, kto usunął. No więc w ten sposób łatwiej trafimy.

**Piotr Buczkowski**: No to rejestrować w jakiejś aktywności administracyjnej.

**Damian Kaminski**: Dokładnie, to jest jedna opcja. To znaczy, tu niekoniecznie administracyjnej, bo to może być właśnie przycisk, czyli taki customowy, który wywołuje DeleteCase. Więc po prostu aktywności użytkownika, ale mamy jeszcze drugą perspektywę.

**Piotr Buczkowski**: No to aktywność użytkownika.

**Damian Kaminski**: Która ma to tą samą... że tak powiem, ten sam efekt i to też trzeba od razu zaopiekować, planując. Już pokazuję. Czyli tutaj mamy też usunięcie i powinno się tu zanotować to samo.

**Lukasz Bott**: No i tutaj mógłbyś modala...

**Piotr Buczkowski**: Ale tutaj tylko, tylko administrator to może zrobić.

**Damian Kaminski**: Tak, tak, ale zmierzam do tego, że DeleteCase i to usunięcie powinno logować ten sam zestaw informacji: kto, kiedy i CaseID.

**Lukasz Bott**: Damian, Damian, i tutaj klikając ikonę tego kosza, tak, czyli usunięcie trwale, może wyświetlić modala, w którym będzie komentarz uzasadnienia?

**Damian Kaminski**: Ja bym nie był za tym, to wiesz, strasznie utrudnia.

**Lukasz Bott**: Ale...

**Janusz Bossak**: Poczekajcie.

**Lukasz Bott**: No OK. Dobrze, no minimum rejestrujemy tylko to: kiedy, kto, co.

**Janusz Bossak**: Czy nie wystarczy, mamy taką funkcjonalność jak ta historia...

**Piotr Buczkowski**: Ale naciśnięcie "usuń" tutaj i tak jest.

**Damian Kaminski**: I tak jest, masz rację. No ale wtedy jeszcze trzeba pisać, nie.

**Janusz Bossak**: Mamy taką funkcjonalność jak historia zdarzeń na sprawie, CaseEvent.

**Piotr Buczkowski**: Ale sprawy nie ma. Nie wpiszesz.

**Janusz Bossak**: No ale, ale zanim ją skasuję...

**Piotr Buczkowski**: Historia sprawy musi się odnosić do sprawy.

**Damian Kaminski**: Tu chyba się zgadzam z Piotrem, ale dajmy się wypowiedzieć Januszowi w pełni.

**Piotr Buczkowski**: Kasując sprawę, kasujesz historię sprawy.

**Janusz Bossak**: To nie jest historia sprawy. Mówię o tej historii takiej zdarzeń, którą zrobiliśmy, która nie jest w sumie nigdzie wyświetlana w tej chwili jakoś sensownie.

**Lukasz Bott**: Mówisz o tej biznesowej historii?

**Janusz Bossak**: Historia biznesowa, to się nazywa, tak?

**Lukasz Bott**: No właśnie, o to też klient pytał.

**Piotr Buczkowski**: Powiązana ze sprawą.

**Janusz Bossak**: No pytanie, czy usuwanie sprawy powoduje usuwanie z tej historii?

**Piotr Buczkowski**: Tak, tak, tak.

**Janusz Bossak**: OK, dobra, no.

**Damian Kaminski**: No właśnie, no to mamy rozwiązane. Znaczy dobra, pytanie tylko, czy w ramach tych zakładek jesteśmy w stanie to wpisać? Tu Piotr zaproponował aktywność administracyjną. Czy dokładamy nową, na przykład w kategorię?

**Anna Skupinska**: Mi się podoba rozwiązanie z dodaniem w aktywności administracyjnej.

**Janusz Bossak**: No tylko pytanie, czy to jest tak jakby administracyjna, bo...

**Lukasz Bott**: To jest aktywność użytkownika, po prostu tak.

**Janusz Bossak**: Będzie użyty w jakiejś regule i ten użytkownik biedny, on jest nieświadomy tego, że tam usuwa sprawę, tak?

**Adrian Kotowski**: Też może być bardziej duży wpisów.

**Piotr Buczkowski**: To niech nie ma tego przycisku dostępnego.

**Janusz Bossak**: No tak, no ale on ostatecznie nie wie, że używa DeleteCase. Tak, no nie wie co się z tą sprawą dzieje, no.

**Lukasz Bott**: Znaczy nie, słuchajcie, to leży w gestii projektach.

**Piotr Buczkowski**: Za to administratora, że mu dał taki przycisk.

**Janusz Bossak**: Znaczy, chodzi o to, że to nie jest aktywność administracyjna.

**Damian Kaminski**: W sensie, Janusz nie kategoryzuje tego pod tą nazwą. I co wtedy proponujesz, żeby tu było nowa, nowa sekcja?

**Lukasz Bott**: Nie, wiecie co, ja myślę, że można było zrobić w ten sposób. Rejestrujemy to gdzieś, w jakichś tam odrębnych tabelach w strukturze AMODITa. Może tam, czekaj Piotr, pozwól mi dokończyć, może w UserActivity i robimy do tego jakiś tam dedykowany raport dostępny tylko i wyłącznie dla administratorów. Bo to najczęściej jest tutaj przykład z Dentsu, tak, że ktoś tam musiał na przykład usunąć, znaczy on musiał usunąć, no to już gdzieś tam miał taką możliwość usunięcia sprawy. Potem go dopytują, kiedy to się zdarzyło, czy coś w tym stylu. Tak, jakby on miał taki raport gdzieś tam dostępny dla niego, dedykowany właśnie z takiej aktywności UserActivity, przefiltrowany pod kątem DeleteCase. Tak, no to sobie popatrzył na to, tak.

**Damian Kaminski**: Ale to znaczy, ja nie widzę powodu, że nie mogłoby być to tu jednak. W sensie... Tu możemy dodać filtr "typ akcji", bo nie mamy czegoś takiego, mamy tylko daty i tyle. I szybko przefiltrujemy "usuwanie".

**Piotr Buczkowski**: CaseActivity.

**Adrian Kotowski**: DeleteCase jest powiązane sprawy. I tak powiem, sprawy to za bardzo też szybko znika.

**Piotr Buczkowski**: To jest Event, sorry.

**Damian Kaminski**: Keen, ale to jest historia biznesowa. Według mnie CaseEvent.

**Piotr Buczkowski**: Tak, tak, Przemek się tym zajmuje teraz.

**Adrian Kotowski**: Tak, to ta opcja otworzył dokument, obrony łącznik.

**Damian Kaminski**: Event, to jest to, co my wpiszemy, to to nie jest tu system... tego nie wypełniania, ewentualnie usuwa ze sprawą, ale Keen to jest historia biznesowa. Do tej pory tak było.

**Piotr Buczkowski**: Ale UserActivity, sorry.

**Lukasz Bott**: Jest, jest UserActivity.

**Piotr Buczkowski**: Case.

**Damian Kaminski**: Wyżej.

**Piotr Buczkowski**: Niżej.

**Lukasz Bott**: Jest, jest dwa wyżej. Stop. Nie, niżej.

**Piotr Buczkowski**: Wyżej, wyżej.

**Damian Kaminski**: Czy kolizję? O dobra.

**Piotr Buczkowski**: Niżej. To cię zapisuje właśnie maile dla WIMu, tak? Tylko to jest czyszczone w momencie kasowania sprawy. Oczywiście dla tej sprawy, tak.

**Janusz Bossak**: No tak, no to się teraz nie nadaje, no.

**Adrian Kotowski**: Ale moglibyśmy może zrobić tak, że dać wyjątek na przykład, bo tu jest teraz powiązanie.

**Damian Kaminski**: Ale wtedy gdzie to wyświetlać Adrian? Niekoniecznie, to znaczy, według...

**Adrian Kotowski**: Raport stworzyć nowy na przykład.

**Piotr Buczkowski**: Nie, nie, to jest w UserActivity Log.

**Damian Kaminski**: Ale skoro mamy tu, słuchajcie. Usuwanie sprawy to jest zdarzenie rzadkie. To nie będzie tu zapchane nie wiadomo jak. To są zdarzenia, nie wiem, serwisowe.

**Adrian Kotowski**: Właśnie mi się teraz wydaje, że to jest często stosowane. Na przykład teraz jak są te sprawy zawierają, czyli to niektórzy klienci, gdzie chcemy ostatnio usuwać. Tam było 3 latach. Wiem, chyba w Rossmannie albo AmRest, więc jakby to może być częste.

**Janusz Bossak**: Znaczy, nie mieszajmy.

**Damian Kaminski**: No dobra, ale zobacz, co jest w historii logowania, no każde logowanie, więc to...

**Piotr Buczkowski**: Nie historia logowania, ta historia logowania zmiany na koncie.

**Damian Kaminski**: Ja wiem, chodzi mi o to, że tu jest dużo też i ja myślę, że ta administracyjna aktywność jest OK.

**Janusz Bossak**: Nie, nie jest dobra, ponieważ to jest aktywność administracyjna. Na przykład, że ktoś zmienił komuś uprawnienie albo dodał do...

**Piotr Buczkowski**: Dobrze, to dodajmy nową zakładkę.

**Janusz Bossak**: Nie nadaje się tutaj. Zmieszanie, wpychanie po prostu innego zdarzenia, zdarzenia, które są zupełnie innego typu.

**Damian Kaminski**: Dobrze, to dodajemy nową. Pytanie tylko, jak ją nazwiemy?

**Piotr Buczkowski**: A jako administrator? Administrator dla "usunie sprawę" z zakładki "usunięte"?

**Janusz Bossak**: Tutaj się nie pojawiają.

**Damian Kaminski**: Też to samo.

**Janusz Bossak**: Tu się pojawiają aktywności administracyjne w rozumieniu zarządzania czyimś kontem, dodawania konta, zmieniania uprawnień, dodania kogoś do grupy, z grupy i tak dalej.

**Damian Kaminski**: W sensie?

**Lukasz Bott**: Tak, do grupy, tam, tam.

**Piotr Buczkowski**: A coś, coś, coś przycisk wyciąłam, tam jest źle.

**Damian Kaminski**: Już cofam.

**Adrian Kotowski**: Myślę, że powinniśmy mieć takiego jak projekty wydarzeń.

**Piotr Buczkowski**: Ten wróć, strzałka w lewo, przycisk jest jakiś duży, dziwny.

**Janusz Bossak**: A to są zdarzenia tutaj, które opisujemy na sprawach i...

**Piotr Buczkowski**: Mogę się w ogóle coś się rozjechało tutaj.

**Damian Kaminski**: Też się rozjechało, ale to znaczy to, że to jest lewej, to to jest align. Tutaj sam przygotowałeś mi to jest sesja pod to, bo to jeszcze nie wymyślili, że u nich wszystko do lewej filler. Więc to też może być konsekwencja.

**Piotr Buczkowski**: No OK, bo to rozjechało na coś, widok mi się po prostu głowacz.

**Damian Kaminski**: Zerknę jeszcze na... Dobra, sprawdzę to. Najwyżej poprawię już tu lokalnie, bo tutaj to może być związane z ich lokalnym. Tutaj co jest system. Dobrze, słuchajcie, to w takim razie jaka jest propozycja co do nazwy, bo zaraz może się pojawić, może "sprawy usunięte"? Niekoniecznie pytanie, co ewentualnie jeszcze innego będziemy potencjalnie w przyszłości logować. Czy po prostu tylko do spraw usuniętych zakładka?

**Lukasz Bott**: Tam gdzieś chyba ostatnio była rozmowa o logowaniu jakichś maili wysłanych ze sprawy czy coś takiego.

**Damian Kaminski**: Ale to jest powiązane ze sprawą.

**Piotr Buczkowski**: To właśnie, właśnie to robię. Właśnie to robię. To jest powiązane ze sprawą, tak.

**Lukasz Bott**: Tylko że to jest, no.

**Piotr Buczkowski**: I będzie usuwane razem z usuwaniem sprawy.

**Lukasz Bott**: OK, dobra.

**Piotr Buczkowski**: Bo jeżeli to jest sprawa usuwana, bo tam zawiera tajne dane, to lepiej też wykasować historię wysłanych maili, tak.

**Lukasz Bott**: Jasne, jasne, dobra, no.

**Janusz Bossak**: No to wygląda tutaj, że jeszcze jedna zakładka i tu będziemy dodawać. No pierwszą, pierwszym kandydatem jest to usuwanie, tak. Może będą inni kandydaci do tej historii. Ale no przynajmniej to gdzieś będzie, no.

**Lukasz Bott**: I nazywa się Aktywność Użytkownika.

**Piotr Buczkowski**: Nie.

**Lukasz Bott**: No ale jak chcecie nazwać?

**Adrian Kotowski**: A co na przykład logowania wysłanych spraw można zrobić, coś takiego, na przykład, że wziąłem tylko ktoś na przykład się pokazuje tylko pierwsze 3 na przykład litery na przykład tematu maila, później są jakieś tam 3 kropki.

**Piotr Buczkowski**: Nie, nie, jeżeli ma być usunięte, ma być usunięte.

**Damian Kaminski**: Dobra, ale nie mieszajmy, nie mieszajmy. Tu mówimy o usunięciu, tam to już Piotr...

**Lukasz Bott**: Ogar.

**Damian Kaminski**: Projektuje.

**Piotr Buczkowski**: Wczoraj wysłałem tak jak to mniej więcej wygląda, pierwsza wersja.

**Damian Kaminski**: Dobra, żebyśmy zamknęli ten temat. Czy jesteśmy w stanie dzisiaj ustalić nazwę zakładki? Czy na razie opisujemy backend?

**Adrian Kotowski**: Na przykład "Rejestr Zdarzeń", coś takiego.

**Piotr Buczkowski**: Zakładka niech się nazywa na razie "Usuwanie Spraw", tak, "Usunięte Sprawy". Jeżeli coś będziemy dodawać, będziemy myśleć nad zmianą nazwy.

**Damian Kaminski**: Dobra, Łukasz, masz wszystko.

**Janusz Bossak**: Słuchajcie, bo jeszcze na sekundę ekran przejmę. Mamy jeszcze jedno miejsce, w którym się wyświetla coś, co nazywamy aktywność administracyjna, czyli tutaj, w zakładce logów systemowych. No i jeżeli byłby taki wpis, że tego dnia Marek [Nazwisko], tutaj byłoby DeleteCase numer...

**Piotr Buczkowski**: Tak będzie.

**Damian Kaminski**: Musi być. To znaczy, to tylko z tego poziomu ktoś będzie wyszukiwał, nikt nie będzie szukał tego po użytkownikach.

**Janusz Bossak**: I tak...

**Piotr Buczkowski**: Dlatego chcę, żeby to było logowane w UserActivity Log, żeby było tutaj widoczne.

**Damian Kaminski**: Mhm.

**Lukasz Bott**: No właśnie ja o tym myślałam tak samo.

**Piotr Buczkowski**: Było łatwo znaleźć, który użytkownik tą sprawę usunął.

**Damian Kaminski**: Tak.

**Janusz Bossak**: No to tak zróbmy, tylko nie wyświetlamy Aktywności Użytkownika. Tak, tutaj jest.

**Damian Kaminski**: Właśnie, a może po prostu olejmy ten ekran, który ja pokazywałem?

**Piotr Buczkowski**: Tak.

**Janusz Bossak**: Dokładnie.

**Lukasz Bott**: Tak, tak.

**Piotr Buczkowski**: Też dobry pomysł, tylko tutaj.

**Damian Kaminski**: Tylko tutaj i już.

**Lukasz Bott**: Tutaj i słuchajcie, najwyżej tytuł tej tej aktywności użytkowników, tak no. Bo tu co, i logowanie i wylogowanie, no przecież nie wszyscy są administratorami. Tak no.

**Janusz Bossak**: Nie, nie.

**Damian Kaminski**: Ale to jest dostępne tylko dla administratora, no to znaczy OK. Rozumiem aktywność.

**Janusz Bossak**: No to jest aktywność użytkownika, ale tu rzeczywiście tak, jeżeli ktoś tam na jakiejś sprawie skasował coś, nawet nie mając świadomości, to mamy datę, kto to zrobił, tu będzie napisane DeleteCase i numer tej sprawy i...

**Damian Kaminski**: Tak.

**Lukasz Bott**: I ewentualnie nazwa procesu, no.

**Janusz Bossak**: No może być z takiego, prawda?

**Lukasz Bott**: Tak, nie no, nazwa procesu, bo wiesz, jak nie masz numeru sprawy, to nie dojdziesz po formularzu tak do procesu.

**Damian Kaminski**: Nie no, numer sprawy musi być.

**Lukasz Bott**: Numer sprawy tak, ale jest ten numer sprawy, no to nie wyświetlisz go sobie nigdzie tej sprawy, bo jej nie ma. Tak, więc nie wiesz z jakiego procesu ona jest o tym.

**Damian Kaminski**: No OK, no można, można. No to już jest systemowa, nie, a nie...

**Lukasz Bott**: Nie no na pewno z procesu dorzućmy, tak.

**Janusz Bossak**: Jakąś tam identyfikować? Tak, wszystko wiadomo opisać.

**Lukasz Bott**: Dobra, to już wiem co. Tak ja wiem, dobra, ale to ja to rzucę propozycję projektu najwyżej na jakimś tam designie. Jutro nie wiem, przegadamy.

**Damian Kaminski**: Dobra.

**Janusz Bossak**: OK.

**Damian Kaminski**: Coś jeszcze Łukasz miałeś drugiego?

**Lukasz Bott**: Tak, miałem temat. Mam temat taki związany z obsługą tabelek i tam tak naprawdę swego rodzaju pomysł klientów to jest pokłosie tego nieszczęsnego przy przygotowaniu tego Timesheetu. Klient chciałby zrobić sobie coś takiego, coś w rodzaju takiego pivota, tylko że z edytowalnymi komórkami. Czyli innymi słowy, coś w rodzaju Excela?

**Damian Kaminski**: Ja może: co chce osiągnąć, a nie jak chce to osiągnąć.

**Lukasz Bott**: Dobra, co chcę osiągnąć, a nie jak, dobra, to już pokazuję.

**Janusz Bossak**: Bardzo słuszne.

**Lukasz Bott**: Dobra, to najpierw wprowadzenie szybko jak w tej chwili jest to robione. Jest rejestrowane ten czas pracy. Tak jest u klienta, jakkolwiek to się nazywa zadaniami, ale to jest generalnie jest rozpisane, są rozpisane dni tygodnia. To jest w podziale tygodniowym, tak od poniedziałku... Od dnia, czyli to jest od poniedziałku do niedzieli włącznie, bo niektórzy pracują też w weekendy. I mają zarejestrować sobie czas. W tej chwili jest oczywiście zrobiony raport ze spraw na dany dzień, powiedzmy na czwartek. Rejestruje sobie na konkretny dzień, tak? Rejestruje sobie...

**Damian Kaminski**: Zadania, tak jak u nas.

**Lukasz Bott**: Tak jak u nas, już sobie swoje konkretne zadania na konkretne zlecenia, opis tam, kto akceptuje, typ godzin, ile tych godzin i tak dalej. No i tutaj mogę mieć na dany dzień, wtedy to już jest na konkretny dzień tygodnia. Mogę mieć to ileś raz, tak? Jeden z tam z uczestników spotkań, no w tym zespole projektowym po stronie PKF-u, no marudzi, że to jest duża klikologia. Ja tam jeden zrobiłem jedną sprawienie za pomocą funkcji GetExcelData tam odpowiednio spreparowany Excel można sobie zaciągnąć tak. To dane, natomiast to, co chciałby klient, to chciałby klient by mieć tego typu... czy widok? Mianowicie, że ją to przykładowym Excelu, że w wierszach wpisuje sobie zlecenie tak, to potem jak się ewentualnie opis prac tego i od poniedziałku, wtorku, środy, czwartku, piątku, niedzieli, tak, i wpisuje sobie tego, wypełnia sobie taką macierz, tak.

**Damian Kaminski**: Mhm.

**Lukasz Bott**: I tutaj i to jest to.

**Damian Kaminski**: Tylko to nie jest wszystko w sensie, bo ja znam ten projekt. W ogóle analizowałem i teraz i tak będzie musiał wejść w każde zlecenie i tam to, co pokazywałeś, tam jest jeszcze 10 innych kolumn, które trzeba wypełnić.

**Lukasz Bott**: Tak, które trzeba wypełnić, tak, to to.

**Damian Kaminski**: Więc to nie rozwiąże mu problemu klikologii, tylko usprawni jeden element wprowadzania godzin.

**Lukasz Bott**: Znaczy on to tłumaczy w ten sposób, że no gro osób tak wypełnia, więc być to też się wzorują na jakimś już istniejącej aplikacji, no mieli jakąś tam aplikację, marudzi na nią. Ktoś tam zadecydował, że chcą to zrobić w AMODITcie tak, no a też ma swoje funkcjonalności.

**Janusz Bossak**: Wejdź na nasz dashboard. Zrób dashboard pivota. Nad samym dashboardzie. Obok jako drugi raport zrób raport tabelaryczny. Jak klikniesz na skrzyżowaniu zlecenia i dnia, to w tym raporcie tabelarycznym będziesz miał szczegóły tego co tam jest wpisane, że na przykład godzinę robił coś tam, a pół godziny robił coś tam i w tym raporcie tabelarycznym... no masz wtedy guziczek "Dodaj rekord" i sobie rejestrujesz nowe zdarzenie.

**Damian Kaminski**: To nie o to tam Janusz chodzi. Ja rozumiem, że oni chcą mieć tabelkę tak jak tutaj, tak jak mówisz tabelaryczne, gdzie będą wypełniać tylko... Po pierwsze możesz to obronić, że nikt tak nie mówił na analizie, bo ja pokazywałem im dokładnie to, co ty zrobiłeś, że to tak będzie wyglądać. Oni to zaakceptowali.

**Lukasz Bott**: Tak, prosto tabelka.

**Damian Kaminski**: Po drugie to nie rozwiązuje problemu globalnie, bo to pozwoli masowo wpisać godzinę, a i tak będzie musiał wejść w każdy dzień, czyli w każdą kolumnę i wpisać, że zlecenie księgowanie jest pod klienta. Tego ma być fakturowane, fakturowane tyle godzin, więc to jest złudne przyspieszenie.

**Lukasz Bott**: Tak, tak, tak. To znaczy, ja powiem tak, nic na siłę, w razie jakby co, to nawet jeżeli będą chcieli tylko taki prosty arkusz, to to też da się to ogarnąć. Funkcję GetExcelData i po prostu zrobię im.

**Damian Kaminski**: Mhm. I wtedy będą wypełniać dopiero... dobra, ale to znaczy ja mam temat podobny z WIMu więc może jeszcze wróćmy, bo teraz tak. WIM też chce tabelkę.

**Lukasz Bott**: No właśnie.

**Damian Kaminski**: W której będzie zaczytywał nawet setki wierszy, ale w zasadzie chcę zaznaczać jedną kolumnę, czyli te wiersze mają być do odczytu co do zasady. Natomiast ma być potencjalnie jedna kolumna edytowalna w postaci akurat u nich checkboxa. I teraz trzeba było się zastanowić jak to mądrze ugrać, bo to jest w miarę podobny element. Czy bylibyśmy w stanie wytworzyć jakieś pole typu tabelarycznego, ale które nie miałoby... Niekoniecznie miałoby historię. Ono miałoby jakiś skutek, niekoniecznie miałoby przeliczenia, tak jak w tabelach, czyli istniałyby oddzielne Case'y, tylko dawałoby możliwość inputu jakiejś w sensie wpisania jakiejś wartości, tak jak tu, po czym wywołanie jakiejś funkcji przyciskowej, na przykład, która by te dane rozpropagowała w konkretne miejsce.

**Lukasz Bott**: No to jest bardzo podobne do tego zagadnienia. Tak, no bo jak ja wprowadzę...

**Damian Kaminski**: No u mnie kwestie wydajnościowe bardziej wchodzą w grę, natomiast tak to jest w pewien sposób zbieżne. Pytanie jak to ugrać? Bo tu Mateusz rzucił, że można by było dać nie wiem jakieś tam rozwiązanie skryptowe, natomiast to no chodzi o rozwiązanie właśnie systemowe, a nie jednostkowe.

**Piotr Buczkowski**: Ale to, co chcecie osiągnąć, co tam będzie edytowane?

**Damian Kaminski**: Dobrze, już pokazuję.

**Lukasz Bott**: No to Damian, teraz ty pokaż swoje, tak.

**Damian Kaminski**: Tak, tak, tak już pokazuję. Powiem szerzej o tym w WIMie, o co chodzi. OK. Więc z racji, że w WIMie faktury mogą mieć 300 pozycji i oni wiedzą czym to może skutkować, zwłaszcza w kontekście OCR-a, ale nie tylko OCR-a, po prostu żeby to przeglądać, to no, ale przede wszystkim chodzi o OCR-a, że to może być bardzo kłopotliwe, może mieć dużo błędów, ciężko je wyłapać. To tak, ilość jest nieedytowalna tutaj, nie zakładajmy tego, że to jest to, tylko była opcja do wytłumaczenia. Czyli jest tabela, która nie jest tak naprawdę danymi z OCR-a, a jest zaciągnięta z innego systemu. Możemy to też porównać do tego, co za chwilę będzie w WIM, czyli nikt nie musi już tego porównywać i poprawiać. My wiemy, że te dane są z założenia poprawne, natomiast tu z racji, że to pochodzi z innego systemu, to właśnie one mogą nie być poprawne, bo po prawej stronie mamy podgląd faktycznej faktury. Po lewej stronie mamy pozycję zamówienia. Oni chcą, żeby te pozycje zamówienia zostały zaciągnięte w formie tabelarycznej i żeby użytkownik jedyne co robił to zaznaczał ciosami, co jest zgodne, zgodne, zgodne, zgodne. Na koniec, co chcemy uzyskać pod tabelką tą, w której są te wiersze z informacjami, jest sobie przycisk, który przelatuje i kieruje po wszystkich wierszach tabeli i tam, gdzie nie jest zgodne, to ma do opisu słownego wypisać niezgodność w punkcie takim, dotyczy nazwa przedmiotu i dwukropek. I potem użytkownik wejdzie do tego pola i będzie sobie wypisywał niezgodność w zakresie ilości, niezgodność w zakresie ceny, niezgodność jakakolwiek. Natomiast chodzi o to...

**Piotr Buczkowski**: Źródło zewnętrzne.

**Janusz Bossak**: A może Source Generic?

**Damian Kaminski**: Dobra, tylko teraz jak to zrobić tutaj po prostu checkboxy, nie?

**Piotr Buczkowski**: Zdefiniować typ kolumny checkbox.

**Damian Kaminski**: To może być tabela SQL.

**Piotr Buczkowski**: I pozwolić, żeby zapisywać taką wartość wpis.

**Damian Kaminski**: Przynajmniej w momencie edycji nie, bo to chociaż dobrze by było, żeby ona pozostała.

**Piotr Buczkowski**: Tak.

**Damian Kaminski**: Ale jak już tu przeniesiemy, to ona będzie w jakiś sposób zapisana, tak.

**Janusz Bossak**: Jeżeli... Słuchajcie, bo w tej koncepcji ta tabelka pozostanie tabelką AMODITową, tak? Czyli będzie obciążała CaseDefinicję?

**Piotr Buczkowski**: Nie, nie. Źródło zewnętrzne, raport ze źródła zewnętrznego.

**Damian Kaminski**: Źródło zewnętrzne tylko się wyświetli.

**Janusz Bossak**: OK.

**Piotr Buczkowski**: Tyle możemy dodać tak, powiedzmy drobne edycje.

**Damian Kaminski**: Tylko... A w sumie chyba rozwiązałeś problem raportem.

**Lukasz Bott**: No przecież masz raport osadzony.

**Piotr Buczkowski**: Raport, raport.

**Lukasz Bott**: I w raporcie osadzonym też masz te?

**Damian Kaminski**: Tylko raport rodzi problem, że na raporcie mamy ograniczenie do 100. A oni mogą mieć 300.

**Piotr Buczkowski**: Mamy ograniczenie do stoła, mamy zresztą stronicowanie.

**Janusz Bossak**: O stronicowanie mamy. Jak przerzucisz na drugą stronę, to tak jakby pierwszej strony już są nieaktywne.

**Lukasz Bott**: Tylko by trzeba było się upewnić. Damian, czy raport osadzony bazujący na źródle zewnętrznym, tam będzie działał ten mechanizm tych checkboxów, tak?

**Damian Kaminski**: Chyba można go wyświetlić, ale nie będzie działał.

**Piotr Buczkowski**: Nie będzie.

**Lukasz Bott**: Nie no będzie, bo nie będzie.

**Damian Kaminski**: W sensie na razie nie będzie.

**Lukasz Bott**: Znaczy nie będzie.

**Damian Kaminski**: Bo nie będzie zwracał ze źródła zewnętrznego chyba żadnej informacji.

**Lukasz Bott**: Nie.

**Piotr Buczkowski**: No bo to trzeba dorobić.

**Damian Kaminski**: No dobra, to trzeba dorobić. Natomiast problem polega na tym, że jak będzie 300 pozycji i mamy stronicowanie...

**Piotr Buczkowski**: To trzeba zwiększyć. Może dla źródeł zewnętrznych można zwiększyć.

**Lukasz Bott**: Słuchajcie, to tak.

**Damian Kaminski**: No dobra, no to wtedy to nie jest zbieżne z Łukasza tą kwestią, bo tutaj rozwiążemy to raportem.

**Janusz Bossak**: W ogóle kompletnie coś innego.

**Lukasz Bott**: Część to jest zupełnie coś innego.

**Janusz Bossak**: Znaczy ten temat Łukasza, to ja bym go zgłębił bardziej, bo to jest dość częsta sytuacja. Bo był taki pomysł... żeby nadać bardziej wyświetlać sprawę. Czyli mając ten twój taki tą macierz, którą tam pokazałeś, która jest de facto pivotem, który zbiera tam po tej po lewej stronie jakby projekty, a u góry dni... po windowaniu rozumiem, że to jest wynik jednej sprawy, że tamte 1,5 godziny to on wpisał, że nad tym projektem w piątek pracował półtorej godziny, no raz teraz.

**Lukasz Bott**: Tak. Tak. Tak, no to znaczy w mojej koncepcji to jest jeden wpis w tabelce tak, no ale tak.

**Janusz Bossak**: Jeżeli to jest jeden wpis w tabelce, no teraz właśnie na tym naszym dashboardzie, jeżeli by nauczyć dashboard, żeby on po prawej stronie od tej tabelki wyświetlił tą sprawę. Tak, czyli byłoby okienko taki nie wiem cokolwiek, w której by się otworzyła ta sprawa, która jest na skrzyżowaniu tych dwóch. Znaczy wiersza i kolumny, no to on sobie tam wpisze, kliknie "zapisz" i mu się tu pojawi. Nie? Tylko potrzebujemy na dashboardzie takiego mechanizmu, żeby obok jakiegoś raportu pokazać sprawę i to mogłoby być zastosowane do wielu rzeczy. Jeżeli moglibyśmy mieć raport tabelaryczny taka tabelka, jak tutaj widzimy tak na raporcie, po prawej stronie to miejsce na tą sprawę i teraz jak klikam w wiersz tej tabelki to mi się ta sprawa pokazuje po prawej stronie, mogę coś tam w niej zrobić.

**Lukasz Bott**: Sprawa wiersza.

**Janusz Bossak**: Sprawa z tego wiersza, który kliknąłem nie.

**Damian Kaminski**: Tylko chodzi ci o podgląd tak z prawej strony tego, co aktualnie zaznaczymy edycyjnie?

**Lukasz Bott**: Tak, ale taki podgląd, ale podgląd edycyjny.

**Janusz Bossak**: Podgląd edycyjny, to znaczy po części to mamy tak, no bo jak kliknę w ten wiersz w tej tabelce, to mi wyskakuje okienko popup.

**Damian Kaminski**: Tylko to dalej... ja czuję, że żebyśmy, to znaczy, to jest jakiś pomysł, natomiast nie wiem czy to jest pomysł, który ten klient, ten gość, który tam zaproponował... On to dalej czuje, że rozumie inaczej. On chce mieć tabelę, ja nie mówię, że my mamy tak zrobić, tylko tak jak ja czuję to wymaganie. On chce mieć tabelę zestawienia całego tygodnia, gdzie ma w kolumnach dni, w wierszach zadania. Co więcej, zwróćcie uwagę, że on te zadania chce zdefiniować dopiero. Czyli jeszcze nie ma.

**Janusz Bossak**: No to dodaję "Dodaj sprawę". I w tej sprawie definiuje to zadanie, mi się w tej tabelce pokaże. Tak? Znaczy ja wiem, że ludzie chcą pracować jak na Excelu. Wszystko pisać w wierszach i kolumnach, ale to nie jest Excel. Tylko to jest system obiegu dokumentów.

**Damian Kaminski**: To znaczy, abstrahując od tego, czy to zrobimy, czy to znaczy, może się nie abstrahując, ale w kontekście tego wymagania? Według mnie Łukasz, to i tak możesz się powołać, że to ma być wycenione. Można poszukać nagrań. Ja dokładnie to przedstawiłem, tak jak ty to zrobiłeś i oni to zaakceptowali. Powiedzieli, że to jest OK, więc jeśli cokolwiek innego to jest poza zakresem.

**Lukasz Bott**: No to wiesz co, jak masz... To słuchaj, Damian, to jak gdzieś tam w wolnej chwili byś był w stanie to znaleźć. To będę bardzo wdzięczny tak, no, bo w tym momencie mamy podkładkę także.

**Janusz Bossak**: Znowuż projekt pisemny projekt.

**Damian Kaminski**: Kamil, pamiętasz, byłeś na tych spotkaniach? Czy nie pamiętasz?

**Lukasz Bott**: Pewnie to było sprzed roku jakiegoś tak, bo to zanim ten temat...

**Damian Kaminski**: No może nawet sprzed 1,5.

**Janusz Bossak**: Co mamy na radę jeszcze?

**Damian Kaminski**: Dobra, to znaczy tak, Ania.

**Lukasz Bott**: Jeżeli chodzi o mnie, to ja dziękuję, się wyłączam, to wszystko co miałem. Dzięki.

**Damian Kaminski**: Ten raport dla mnie jest jakimś rozwiązaniem. Ja muszę tylko pogadać, bo tu jest koncepcja odwrotna, oczywiście pewnie możemy to zrobić, ale ja bym jednak zasugerował im, że będą zaznaczać tylko to, co jest nieprawidłowe, bo wtedy będą też mieli mniej zaznaczania i oni jeszcze chcą opcję "zaznacz wszystko", a właśnie może jak będzie tylko "zaznacz złe", to niepotrzebne jest "zaznacz wszystko". No przy czym zaznaczenie dobrego rozpatrz jako pewność, że ktoś to sprawdził, a złego to tak ktoś przeleciał i no, ale zobaczymy. Pogadam na razie z nimi i zrobię na to PA. Nie wiem, czy mieliście okazję...

**Piotr Buczkowski**: No to zaznacz wszystko nie ma sensu.

**Damian Kaminski**: No właśnie, to zaznacz wszystko nie ma sensu. Tak, zgadzam się.

**Kamil Dubaniowski**: Tak, będziemy musieli zweryfikować to z kwotą z faktury. No bo rozumiem, że podsumowaniem będziemy odczytywać od OCR-a albo...

**Damian Kaminski**: Tak, tak, tak, to znaczy zawsze pod gotowe możemy mu im zrobić podwójny, że się nie zgadza i czy na pewno uzupełnił opis słowny, tak, bo chociaż możemy to też jakoś walidować, dobra.

**Janusz Bossak**: Słuchajcie, jeden temat jeszcze związany z tą tabelką, bo to mi ciągle chodzi po głowie. Czy dla takiego przypadku, czy dla takich przypadków, gdzie tabelki miały być duże, a jeszcze do tego coś miałoby być w nich robione, czy nie lepiej byłoby gdyby wyświetlać się w osobnym oknie, czyli mamy tutaj nawet początek takiej tabelki jak tutaj? Żeby był przycisk "pokaż tabelę", tak?

**Piotr Buczkowski**: Nie, to nawet kwestia tego, że wszelkie operacje tabeli typu foreach są jakieś wyliczanie sum, czy coś będzie obciążało... Bo to nie serwer obciążysz, odciążyć przeglądarkę, obciążyć serwer. Bo i tak wiersze muszą być wczytane po stronie serwera, żeby wykonać na nich operację.

**Janusz Bossak**: Że obciąża się ten formularz?

**Piotr Buczkowski**: Także nie serwer obciążasz. Bo na pewno będziesz chciał jakieś sumy zrobić, tak. W jakiejś formie cyfrowej. Jakąś regułę tabeli i tak będzie to obciążało, może trochę nie przeglądarkę, ale serwer. Także lepiej nie wstawia się takich dużych tabel, tak, lepiej zrobić mechanizm na przykład wyświetlania tabeli na podstawie oddzielnej tabeli, tak.

**Damian Kaminski**: Ja bym powiedział jeszcze szerzej, że my przed występem powinniśmy jeszcze zaopiekować to, że ta tabela niekoniecznie musi być wczytywana, bo możemy po prostu odczytać stopki. A może zrobić coś takiego do faktur? No bo właśnie będzie wszystko szło z tabeli, jak będzie zmapowane, a tu już nie ma potrzeby sprawdzania, bo wszystko jest to samo. Tylko pytanie... to znaczy nie, no tak, podgląd wtedy generuje się na podstawie XML-a i może powinniśmy wprowadzić nowy mechanizm "załaduj tabelę" tylko dla tych klientów, którzy będą faktycznie na tej tabeli coś potrzebowali zrobić, bo oni mają, nie wiem właśnie, dodatkowe pola, gdzie już na poziomie linii definiują nie wiem jakieś przypisanie MPK czy cokolwiek. A wszystkim innym pozbylibyśmy się wtedy ogromnej ilości dodatkowych case'ów, które są zbędne, bo oni i tak będą pracować na podsumowaniu. No bo tutaj właśnie wypada nam ten mechanizm OCR-yzacji, gdzie trzeba porównywać i tak dalej. Ktoś sobie wyświetla, ale to już jest odrębny temat.

**Janusz Bossak**: Dobra, ale sprzedajmy. Mam czas, musimy wziąć.

**Damian Kaminski**: Te kolory, te kolory. Czy mieliście okazję na to spojrzeć, czy teraz, bo Ania już chce na tym pracować, czy ma...

**Janusz Bossak**: Zaproś tylko jakby ocenę za pomocą sztucznej inteligencji, co jest fajniejsze, co nie, ale ja nie wiem jakie są, nie pokazałeś nam jaka jest paleta to Tableau i właściwie nie bardzo.

**Damian Kaminski**: Pokazałem.

**Janusz Bossak**: No nie.

**Damian Kaminski**: Tylko nie wiem, czy to otworzyłeś w odrębnym pliku.

**Kamil Dubaniowski**: A jeszcze, jeszcze może może do tego WIMu Damian sekundę, bo nie wiem, czy zgubimy wątek, ale opowiadałeś o tym, jak działa teraz zwracanie tych pozycji z zamówienia, że to jest wykonanie procedury składowanej i ja dostanę JSON-a, dostanę tam 300 pozycji i ja teraz mam zasilić w locie, tak? OK.

**Damian Kaminski**: Tak. I wpiszemy do źródła. Tak, tak, tak, tak, to spoko.

**Kamil Dubaniowski**: To to będzie na tyle wydajne, że te 300 nam nie będzie nikt czekał, aż się przemieli nie wiadomo ile, no bo to będzie klikał użytkownik. Tak.

**Damian Kaminski**: Czeka 5 sekund, ale nie dłużej. Według mnie, to znaczy nie będzie użytkownik, bo jak odczyta OCR, to zanim przekażemy użytkownikowi, to już wczytamy. Użytkownik będzie ładował tylko jak nie odczyta OCR numeru zamówienia.

**Kamil Dubaniowski**: No tego trochę się obawiam jakości tego, czy to, że to będzie małe.

**Damian Kaminski**: No to tu już nic nie poradzimy.

**Kamil Dubaniowski**: Czyli wtedy ręczne wskazanie, no i też trzeba wziąć pod uwagę, że on odczyta i na przykład podstawi coś źle, więc też będzie trzeba dodać całą maszynę, żeby to wyczyścić i wskazać swoje, podać swoje.

**Damian Kaminski**: Mhm. No tak, to to już musimy projekt już procesowo zaopiekować. Dobra, to wracam do tych kolorów, nie wiem, czy Janusz otworzyłeś to odrębnie, bo tam napisałem, że Teams tego nie wyświetla.

**Janusz Bossak**: Nie jakoś. No.

**Damian Kaminski**: To jest Tableau, to jest nasze. Nasze jest jak widzicie nieco żywsze. Możemy, mogę wpisać jeden, jedno słowo i wrócimy do takiego jak ma Tableau. W Tableau domyślnie jest 10. U nas proponuję, żeby domyślnie było 20. W pierwszej serii plus robić przynajmniej ze 3 serie, żeby ktoś nie musiał wybierać tego, tylko żeby to od razu było systemowo zaopiekowane. Bo to nas nie boli, różnice nasycenie, nasza paleta bardziej żywa, w Tableau jakieś tam różnice. No i przede wszystkim przewaga, jeśli chodzi o to, że my mamy te 20 w pierwszej serii, tak, czyli jest to bardziej zróżnicowane.

**Janusz Bossak**: Znaczy i tak i nie, bo zobacz ten. Wiadomo, mężczyźni inaczej widzą kolory, no ale cyjan niebieski i indygo są tak blisko siebie, że tak powiem jak to będziesz miał na wykresie, to jeszcze jest morski, który jest do tego niebieskiego też podobny. U nas wychodzi niebieski morski, tak to jest to po prawej stronie, że tego nie rozróżnisz. Zauważ, że te kolory, które są w Tableau... one są, są, są dalej od siebie tak w sensie kolorystycznym, tak.

**Anna Skupinska**: Tak.

**Damian Kaminski**: Tak, tylko musimy pamiętać... to teraz tak, najprostsza propozycja. Zmieniamy kolejność, czyli ustawiamy czerwony, zielony, niebieski tak dla tych, żeby 10 pierwszych było różniących się. Potem wprowadzamy te turkusowe. I to dotyczy tylko pierwszej serii, bo znowu kolejna seria to będą tylko odmiany tych kolorów, czyli trochę jaśniejszy czerwony. Wiadomo, że jeśli chcemy zaprezentować 40 różnych czy 60 różnych serii, to one nie będą już tak mocno się różnić od siebie. No nie da się tego zrobić. Mamy ograniczoną paletę, tak.

**Janusz Bossak**: No trzeba brać pod uwagę, że Tableau ma milion lat więcej doświadczeń niż my, łącznie jakby policzyli man-daysy, które poświęcili na to.

**Damian Kaminski**: Mhm. Mhm.

**Janusz Bossak**: Coś w tym jest, że zrobili tak, a nie inaczej nie.

**Damian Kaminski**: OK. Ale to nie przeszkadza nam w żaden sposób zrobić tego, tak, tylko po prostu zmieniamy kolejność. Nie ustawiamy to, to tak jak on tu zaproponował.

**Janusz Bossak**: Znaczy mi chodzi też o to, że, że 10 kolorów...

**Damian Kaminski**: Że 10. Tak uważasz?

**Janusz Bossak**: Dlatego, że prawdopodobnie doszli do wniosku, że na wykresie i tak i tak człowiek nie odróżni więcej niż 10 kolorów. W związku z tym...

**Damian Kaminski**: Bo ja się obawiam tylko tych Treemap, gdzie jest dużo, więc kolejne serie i tak powinniśmy zaopiekować.

**Janusz Bossak**: Dlatego, dlatego trzeba zrobić funkcjonalność pod tytułem "pozostałe". Czyli to, co mówiliśmy, że pokazujemy na tej mapie do pewnego poziomu jakby istotności. A poniżej to jest szum, który nie trzeba.

**Damian Kaminski**: No nie zgodzę się do końca. W sensie no dobra, patrzysz tylko przez pryzmat jakie te mapy, no ale to wtedy to cała twoja mapa w prawym dolnym rogu będzie w jednym kolorze.

**Janusz Bossak**: No dokładnie. Będzie jeden kwadracik "pozostałe".

**Damian Kaminski**: Ale ja niekoniecznie tak chcę. Ja chcę jako użytkownik, żeby tam były małe kolorki różne.

**Janusz Bossak**: Chcesz taką siatkę? Co on z tego się dowiaduje?

**Damian Kaminski**: No dobra, no to patrzymy na te mapy, a teraz spójrz na wykres taki liniowy tak. Połączone punkty i tam mam już na przykład joby i jobów mamy 15. I ile było wywołanie jobów dziennie? Tak.

**Janusz Bossak**: To trzeba wziąć 10 najbardziej aktywnych jobów, które są najwyżej, to, które są najniżej, może nie są istotne i wyeliminować. Znaczy, wiecie, to nie jest tak, że my wymyślimy jakby rozwiązanie na każdą kombinację. No są pewne zasady tworzenia wykresów. Jeżeli na wykresie jest więcej niż 10 linii, prawdopodobnie to użytkownik i tak i tak nie jest w stanie tego prześledzić. To będzie miał jakiś szum informacyjny, mnóstwo linii, ale on nie wie tak, no jeżeli te wszystkie linie się skupią, powiedzmy gdzieś tam na dole jako mało istotne, a będziesz miał 4 czy 5 czy 6 głównych procesów czy drobnych, które zajmują czas... No to ta reszta to jest szum informacyjny. Tak, możesz tego w ogóle nie pokazywać, to jest kwestia dobrego robienia wykresów. Według mnie puszczanie właśnie palety 20 kolorów powoduje, że taki nasz konsultant czy twórca tego raportu się rozleniwia. Tak, no dobra, niech się pokaże wszystko co tam mam.

**Damian Kaminski**: Dobra, to znaczy powiem tak, ja rozumiem, że wtedy wykres nie jest czytelny, tylko chodzi mi o to, żebyśmy, żebym ja jako użytkownik, jeśli świadomie podejmę decyzję, że ja chcę wyświetlić 30 informacji na tym raporcie, to żebym ja nie musiał... bo dzisiaj mamy 20 i ja wszystkie pozostałe albo się dublują kolorami, albo muszę wyklikać ręcznie. Tylko do tego zmierzam, żebyśmy my, jako projektanci systemu, zaopiekowali to, że jak ktoś świadomie chce wrzucić 40, to każdy z tych 40 domyślnie będzie miał inny kolor, a nie muszę je przeklinać, bo mamy tylko zdefiniowanych 10 albo 20.

**Janusz Bossak**: Nie. To nie jest właściwy kierunek. Według mnie właściwym kierunkiem jest powiedzenie użytkownikowi: słuchaj użytkowniku, żeby ten wykres miał sens, przedstawmy najwięcej 10 rzeczy. Pozostałe potraktujmy na razie jako szum informacyjny i tyle.

**Damian Kaminski**: No dobra, ja się z tym nie zgadzam, bo potem mogę zastosować filtry. I ja ograniczę potem koniec końców, ale to spowoduje, że musiałby dynamicznie te kolory znowu przeliczać. Czyli jak jeden filtr zastosuję, to niebieski reprezentuje styczeń, a jak zastosuję, że chcę od czerwca, to niebieski reprezentuje nagle czerwiec, czyli muszę na nowo się nauczyć legendy.

**Janusz Bossak**: Weź to pokaż i to, co rozmawiasz z nami, weź porozmawiaj z Michałem Maliszewskim.

**Damian Kaminski**: OK. Dobra, bo tutaj też wiesz, ja wpisałem "porównaj to z Tableau", a to jest jakieś domyślne. Tak, my wiemy, de facto nie znamy tego Tableau. Dobra, porozmawiam z Michałem.

**Janusz Bossak**: Oni mają więcej tych palet różnych, bo to jest jedna, bo tam jest, znaczy na świecie istnieje wiele jakby palet przygotowanych przez różne firmy. Adobe tam przygotowało swoją jakąś i tak dalej i tak dalej. I no wszyscy pracują nad tym, żeby te palety były... One są dobierane pod kątem też właśnie kontrastu, pod kątem tego, że osoby, co nie widzą kolorów, żeby mogły rozróżniać, żeby to się ci co nie widzą kolorów, widzą odpowiednie szarości tego i widzą różnicę. To jest jeszcze jedna rzecz, tak. Więc to są naukowo dobierane te kolory, to nie jest tak po prostu, że sobie ktoś wziął ten kolor i już. To jest ogromna praca, żeby dobrać te kolory tak, że nawet ci właśnie, którzy nie widzą kolorów, żeby widzieli odcienie szarości.

**Damian Kaminski**: OK. To także zostawmy, porozmawiam z Michałem, bo to jest jakiś przykład Tableau, pewnie nie jedyny, tam tak jak powiedziałeś, jest pewnie kilka bazowych. Mi chodzi tylko o to, żeby wyeliminować konieczność pracy ręcznej, jeśli ktoś chce wyświetlić 20, 30, 40, bo dzisiaj...

**Janusz Bossak**: To jeżeli mi chodzi tylko o to, że jak ktoś chce wyświetlić 20 lub 40, znaczy, że źle robi.

**Anna Skupinska**: A ja mam jedno pytanie dotyczące kolorów, bo dostałam inne zadanie, w którym mam dodać wiele kolorów różnych i chciałam się dowiedzieć czy to Damian o nim wiesz, to może...

**Damian Kaminski**: To jest to zadanie, to dlaczego uważasz, że to jest WIM?

**Anna Skupinska**: Nie do końca, nie, nie mówię o tym do końca tym zadaniu. Wydaje mi się, że nie mówię o tym zadaniu. No, widzicie mój ekran?

**Damian Kaminski**: No to jest to zadanie, to jest dokładnie to zadanie 20 kolorów i 4 serie, tam było jako propozycja. Otwierałaś sobie załącznik?

**Anna Skupinska**: O ciebie zadaje 2.1, a OK, jest. A więc ja już... a tak to ty. No to jest już tutaj, ale tutaj się nie da kliknąć. To są po prostu tekst, więc...

**Damian Kaminski**: Przejedź do góry, dałem to H1. Przejedź do góry, details.

**Anna Skupinska**: A tutaj. A tak, tutaj są te wszystkie.

**Damian Kaminski**: Nie do góry, do góry, do góry nad tym wszystkim i powolutku do dołu. W ramach kolorów predefiniowane. Tutaj w załącznikach HTML z lepszym opisem tego co niżej. Bo tu jest źle, może powinienem w ogóle tego nie wpisywać. Po prostu wkleiłem to, żeby były te hashe, to jest to. Na razie się z tym wstrzymujemy. Ja porozmawiam z Michałem.

**Anna Skupinska**: Aha. Aha, bo ja w tym pracowałam i wprowadziłam te kolory, żeby się dodawały do...

**Damian Kaminski**: No widzisz Janusz, czy tu jest według ciebie... Jeśliby było ograniczenie do 10, to by było źle, no myślę, że tu jest więcej niż 10 takich kluczowych klocków. Bo ogórki mają pewnie już w sobie 10. Jeszcze tu cebule też mają jakieś inne. No ja rozumiem, że to może być nieistotne w kontekście, to znaczy to może być dla ogólnego punktu widzenia mało czytelne, jeśli jest więcej niż 10.

**Janusz Bossak**: Co z tego wyjdzie?

**Damian Kaminski**: Ale też zakładam, że ktoś może potrzebować mieć więcej niż 10 i czemu mu tego nie usprawnić po prostu poza...

**Anna Skupinska**: Ale pamiętam, więcej niż 10 kolorów mamy w tej chwili?

**Damian Kaminski**: Mamy 20. Mamy 20, teraz?

**Anna Skupinska**: Tak tak, mamy 2 wyjścia.

**Damian Kaminski**: Tylko wszystko, co ponad 20 się powtarza, albo trzeba przerabiać ręcznie.

**Anna Skupinska**: Tak, to jest wersja obecna z develop i teraz się powtarzają. Jest na przykład to i to ma taki sam kolor.

**Janusz Bossak**: Bo teraz mamy ile 23 10?

**Damian Kaminski**: Tak, 20. 20 plus możliwość definiowania ręcznie.

**Janusz Bossak**: No to czym się różni to od tego nowego, skoro mamy 20, to dlaczego?

**Damian Kaminski**: To już jest.

**Anna Skupinska**: To są inne, w każdym ma inny kolor. Każda rzecz oczywiście jest, jakby ktoś już miał jeszcze tyle, że wszystkie te palety się już skończą... Im kolory to zacząłby się znowu powtarzać, no ale cóż.

**Damian Kaminski**: O właśnie i to jest to, co Janusz powiedziałeś, że nieistotne są te, które tu są bardzo małe i tu się zgadzam, tylko jak one się pokrywają kolorem, no to to powoduje zaburzenie tego, która legenda, bo nie mamy na razie wyróżnienia. Czyli ja patrząc na legendę "niebieski", teraz nie wiem, który to jest niebieski, czy ten tutaj w cebulach, czy w papryce na górze, czy jeszcze jakiś inny. A jeśli by dodało jakieś inne odcienie, no to może łatwiej to rozróżnienie. A i wtedy na podstawie tej analizy mogę stwierdzić: dobra, tu mam dużo szumu, właśnie takich drobnych rzeczy i wtedy wchodzę w redefinicję tego raportu i oznaczam, że wszystko poniżej levelu takiego jest jednym kolorem.

**Janusz Bossak**: Wejdź, wejdź w edycję tego koloru i ustaw sortowanie po pierwszej. Wykres jest po prostu źle zrobiony.

**Anna Skupinska**: Czy to mój wykres do prób, więc...

**Janusz Bossak**: Nazwa produktu i sortowanie. Czy tutaj, no nie wiem czy tam jest tak sortuj po tam rosnąco albo malejąco, nie poetyckie tak wartościach.

**Damian Kaminski**: Nic to nie dało. Aktualizuj automatycznie, pokaż się, coś się zmieniło, bo...

**Janusz Bossak**: Masz wyłączony?

**Janusz Bossak**: Powinny ustawić te kolory jakby... Żółte na dole, ten dalej coś tu jest nie tak.

**Damian Kaminski**: No niekoniecznie, no właśnie, bo widzisz, ja no ja rozumiem cię Janusz, natomiast po wartościach kolumny tutaj powinno być tak, że najmniejsza kolumna powinna być pierwsza, największa ostatnia, jeśli rosnąco, bo nie wiem jak ustawiłaś, a dodanie to co ty masz na myśli.

**Anna Skupinska**: Żółte na dole dlaczego? To jest po nazwie produktu, więc to on teraz patrzy na nazwę produktu i alfabetycznie sortuje.

**Janusz Bossak**: Dobra, to to jest co innego, a w tam w kolorach mamy też sortowanie, bo już też...

**Damian Kaminski**: No właśnie. Nie mamy.

**Anna Skupinska**: Nie, nie mam.

**Damian Kaminski**: To jest coś, co mówiliśmy, że...

**Anna Skupinska**: To jest po prostu ona początku pobiera po prostu ileś wartości 20 nie więcej i przydziela im kolory.

**Damian Kaminski**: Poczekaj, poczekaj, poczekaj. Janusz ma rację. Anuluj to.

**Janusz Bossak**: Różne znaki, sortowanie.

**Anna Skupinska**: A tutaj co jest? Nie ma zastosowania, to jest tylko...

**Damian Kaminski**: A tu jest tylko i tu trzeba dodać.

**Janusz Bossak**: Pozycji. Kolor. Różne znaki. Sortowanie.

**Damian Kaminski**: Trzy kropki, sortuj po...

**Janusz Bossak**: Czyli coś tu jest nie tak?

**Damian Kaminski**: Odśwież, odśwież. Poczekajcie. Odśwież. Jest dobrze.

**Janusz Bossak**: Jest dobrze, no koło odwrotnie, no ale OK.

**Damian Kaminski**: Jest dobrze.

**Janusz Bossak**: Teraz są małe na dole, tak no i teraz na ciepło masz takie linijki. Jedna druga od dołu, trzecia cieniutkie, tak w górkach też tam masz jakieś zielonkawą linijkę czy jakąś potem jest niebieskawa samym dole w marchwi masz takim prawem będzie i tak.

**Damian Kaminski**: No masz rację, tylko to zobaczysz dopiero jak przygotujesz raport.

**Janusz Bossak**: No dobrze, ale czy mnie... No dobra, trzeba pogadać z Michałem.

**Damian Kaminski**: OK. No pogadajmy i weźmy dobre praktyki.

**Janusz Bossak**: Nie umiemy robić wykresów, tak, znaczy nie umiemy przygotowywać danych pod prezentację klientów. To jest nasz problem. I my próbujemy technicznie być poprawni, to znaczy, żeby wszystko pokazać. To nie jest do końca jakby metodologia tworzenia raportów.

**Anna Skupinska**: Raczej jeżeli ktoś nie chce pokazywać małych rzeczy, to może wejść dodać warunek i na przykład, że wartość jest mniejsza niż...

**Janusz Bossak**: To nie o to chodzi.

**Damian Kaminski**: Nie, ale to nie o to chodzi. Aniu, to znaczy może warto je pokazać, tylko zareagować? To jest to wyzwanie.

**Janusz Bossak**: Tak, znaczy, moja propozycja jest taka, że wszystko co jest na przykład poniżej tam nie wiem... jednego, no to już chyba zależy od wykresu tak, ale poniżej 5% to agreguje do łącznej jakiejś pozycji "pozostałe" i wtedy nie będzie potrzeba 30 kolorów, tylko może będzie potrzeba 10 kolorów, bo te 10 największych się pokaże. A cała reszta będzie jako "pozostałe" jednym kolorem.

**Damian Kaminski**: Janusz, to bym się zgadzał pod kątem tworzenia. Tylko właśnie pytanie jest, na ile my powinniśmy ingerować w to?

**Janusz Bossak**: Słuchajcie, ja muszę liczyć. Przepraszam Damian, ty też Kamil też, bo proszę, żebyście napisali mi czym się zajmujecie. Macie czas 5 minut na naszym kanale, chyba że napisaliście, nie Łukasz tylko napisał, bo mam spotkanie z Przemkiem, muszę mieć od was informacje jakimi tematami poza devem się zajmujecie, wsiadajcie tam i tak na PDM, Product Delivery na tym kanale. Także tu musimy kończyć, bo ja mam za 10 minut z Rządkie spotkanie.

**Damian Kaminski**: Mhm. Projektami, tak.

**Janusz Bossak**: Przynieś od was informację.

**Anna Skupinska**: Rozumiem, czy ja jestem jeszcze zajmie się wstrzymuję i będę go wrzucać i dopóki jak będzie już więcej wiadomości to wtedy ja dokończę.

**Janusz Bossak**: OK. Na razie.

**Damian Kaminski**: Cześć.

**Anna Skupinska**: To cześć.
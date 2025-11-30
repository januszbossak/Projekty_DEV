**Transkrypcja**

28 sierpnia 2025, 08:00AM

**Janusz Bossak** rozpoczęto transkrypcję

**Janusz Bossak** 0:03  
No hej.

**Adrian Kotowski** 0:17  
Czy takie szybkie pytanie, czy planujemy jakąś trakcie spotkania, omawiać tematy odnośnie tego widoku? Zakładki, integracje stanie systemowych?  
Tak przyszedł, właśnie liczyłem, że może tutaj też będzie poruszany dzisiaj.

**Damian Kaminski** 0:32  
Wstępnie mamy to już omówione jakie masz pytania.

**Adrian Kotowski** 0:35  
Oczywiście to pytałem się Kamila ostatnio czy jakiś jest projekt na to było mnie nie było mnie wtorek po prostu przedstawić moja choroby, tam nie ową, więc tam mam już to opisane, gdzieś tam jak to ja nie wiem wyglądać.

**Janusz Bossak** 0:49  
No się.

**Damian Kaminski** 0:49  
Kamil to opiekuje to według mnie Kamil wie co i jak to pogadajcie we 2, to znaczy na moje to na ten moment robimy MVP, tak jak się umówiliśmy, czyli nie wiem Kamil czy unifi kujemy już to te 2 zakładki w jedno, czy tylko zmieniamy ikonkę i na ten moment?

**Kamil Dubaniowski** 1:06  
No właśnie o to chodzi, że jest Przemek zrobił już frontend to już jest scalone w jedno tylko tam brakuje backendu pod dodawania crometta ów i tyle w tak no w mojej ocenie no mówię spotkajmy się może z przemkiem Adrian indywidualnie i to pogadamy wtedy.

**Adrian Kotowski** 1:24  
No dobra o k to czy najbardziej mi chodziło o tę kwestię tych integracji, czyli przykład?

**Piotr Buczkowski** 1:26  
Czy mogę ja też zobaczyć?

**Kamil Dubaniowski** 1:29  
Tak no ja.

**Damian Kaminski** 1:30  
To jak mamy to poka, pokaż to, no.

**Kamil Dubaniowski** 1:32  
A to czekajcie, powiem to jest na Przemek lokal.

**Piotr Buczkowski** 1:33  
Znaczy, nie, nie chodzi mi o to, że spotkanie tak chciałbym.

**Kamil Dubaniowski** 1:38  
Dobra, to to opowiadajcie to co teraz jest to jakby dla was ważne, a ja się zaloguję zobaczyć czy to jest na Przemek lokal.

**Damian Kaminski** 1:47  
Dobra, to nie wiem od czego zaczynamy. Czy ja mam zaczynać wtedy Łukasz, coś miałeś? Chcesz zacząć?

**Lukasz Bott** 1:51  
Czyli to znaczy, ja chciałbym zacząć, bo mam 2 tematy, a że o jedenastej zaczynam tam szkolenie dla klienta, no to to po prostu chciałbym, przynajmniej moje poruszyć szybko, a ewentualnie sobie tą dokończycie radę. Tak no.

**Damian Kaminski** 2:05  
Dobra.

**Lukasz Bott** 2:05  
Dłużej pierwszy temat to na razie masłowy.  
Mamy funkcję death case.  
I pytanie jest takie, czy coś robimy, czy planujemy robić w zakresie rejestrowania, kto kiedy użył tej funkcji i to nie może być tak, że to wpisujemy do jakiegoś system logu, tylko po prostu to musi być permanentne zderzaki activity użytkownika no.

**Damian Kaminski** 2:26  
Jak ty vity.

**Lukasz Bott** 2:33  
Bo.

**Piotr Buczkowski** 2:33  
Jakiej funkcji nie rozumiem, sorry.

**Lukasz Bott** 2:35  
Funkcja dit case.

**Damian Kaminski** 2:36  
Delete case, czy chcemy rejestrować, że taka sprawa o takim numerze, przez dlaczego ona znikła? W sensie, żeby chociaż zarejestrować kasę i di kiedy i kto ją usunął? Ja wolę coś takiego robiłem dedykowane jako po prostu dedykowany źródło zewnętrzne, bo chcieli w kontekście dokumentów kadrowych.

**Lukasz Bott** 2:39  
Nawet jest nie słuchajcie.  
Dokładnie tak.  
No i właśnie Damian i właśnie o to chodzi, że właśnie nie chcemy, że że nie nie chcemy tego robić, tylko musimy to zrobić, bo wielu klientów już się o to dopytuje. Między innymi to klient gabana, którego dzisiaj w szkole.

**Damian Kaminski** 2:58  
Tak ja rozumiem.  
Mhm.

**Piotr Buczkowski** 3:03  
Ale co ma być, co ma być rejestrowane?

**Lukasz Bott** 3:07  
No to co do mnie powiedział, yy minimum numer sprawy, nazwa procesu, z którego to było data, kiedy się to zdarzenie wydarzyło i kto to zrobi?

**Damian Kaminski** 3:08  
Minimum czyli.  
I kto tak, czyli bez żadnych danych.

**Lukasz Bott** 3:19  
Dokładnie.  
Bez żadnych danych, bo tam czasami w tytule mogą być.

**Damian Kaminski** 3:21  
Chodzi o to, żeby jak wiesz link komuś nie działa, to dobra nie działa i teraz nie ma sprawy i teraz nie wiadomo co się z nią stało. Kto co kiedy więc minimum, kto i kiedy usunął?

**Lukasz Bott** 3:31  
Tak.  
Ewentualnie z jakimś może komentarzem dlaczego to usuną tak.

**Damian Kaminski** 3:39  
Tylko to spowoduje, że jest wtedy z kosza nie można usuwać. Ja tak mam zrobione z komentarzem, ale to jest pod przyciskiem, natomiast to nie będzie skutkować tym, że.

**Janusz Bossak** 3:39  
No.

**Damian Kaminski** 3:50  
Ee, trzeba będzie każdą, w zasadzie nie da się zrobić dieta ustawieniem systemowym w sensie dzisiejszą funkcjonalnością systemową poziomu sprawy, tylko można to usunąć z poziomu kosza.

**Lukasz Bott** 3:51  
No ale wiesz to.

**Janusz Bossak** 3:53  
Słuchajcie.

**Damian Kaminski** 4:04  
A z kolei to jest lista, więc wtedy co na liście wyświetlimy modela.

**Janusz Bossak** 4:09  
Poczekajcie mówię.

**Lukasz Bott** 4:10  
Nie no ale.

**Janusz Bossak** 4:12  
Uporządkujmy temat.

**Lukasz Bott** 4:12  
Janusz.

**Damian Kaminski** 4:14  
Mhm.

**Janusz Bossak** 4:14  
O którym mówimy, jest delirkę funkcję.

**Lukasz Bott** 4:16  
Mówimy o regule funkcji dietke kasę, którą w tej chwili możesz sobie wywołać spod przycisku reguły na sprawie i jak to zrobisz bez żadnego tam właśnie dodatkowego rejestrowania.  
Ja zazwyczaj rejestruję to w logu systemowym, ale log systemowy jest co jakiś czas czyszczony, no to po prostu nie ma w ogóle śladu o tym, kto to zrobi, kto wywołał dietkę jest, czyli to permanentne usunięcie. Sprawdź, bo to.

**Janusz Bossak** 4:41  
Bo tutaj to, co mówi Damian, to skąd wiem?

**Piotr Buczkowski** 4:43  
No bo po to to jest robione jak jak jak ma powiedzieć delic to delikt.

**Damian Kaminski** 4:44  
Tak, to ja mówię szerzej.

**Piotr Buczkowski** 4:48  
To po co ma być funkcja delikt?

**Damian Kaminski** 4:49  
No tak tylko czy?  
Nie, nie, ale tu chodzi o to Piotr, nikt nie podważa punkty, delikt natomiast czasami robią to użytkownicy, bo wiesz, kiedy kasy hidden nie pozbywa się.

**Piotr Buczkowski** 4:53  
Kas jeden.

**Lukasz Bott** 4:57  
Tak.

**Damian Kaminski** 5:05  
Sprawy, a czasami jest potrzeba biznesowa pozbycie się sprawy, bo przechowuje ona dane, które ktoś zażądał, że trzeba usunąć. Potem ktoś inny tej sprawy szuka, powiedzmy i wie, co w niej było, ale już jej nie ma. No i teraz zaczyna się zaczynają się wyjaśnienia, dlaczego i nie ma kto usunął. No więc w ten sposób łatwiej trafimy.

**Lukasz Bott** 5:05  
Sprawy.

**Piotr Buczkowski** 5:22  
No to rejestr rejestrować w jakiej jest aktywności administracyjnej.

**Damian Kaminski** 5:27  
Dokładnie to jest jedna opcja, to znaczy tu niekoniecznie administracyjnej, bo to może być właśnie przycisk, czyli taki customowy, który wywołuje death case.

**Janusz Bossak** 5:28  
Przecież.

**Damian Kaminski** 5:38  
Więc po prostu aktywności użytkownika, ale mamy jeszcze drugą perspektywę.

**Piotr Buczkowski** 5:41  
No to aktywność użytkownika.

**Damian Kaminski** 5:45  
Która ma to tą samą?  
Że tak powiem ten sam efekt i to też trzeba od razu zaopiekować, planując już pokazuje.  
Czyli tutaj mamy też usunięcie i powinno się tu zanotować to samo.

**Lukasz Bott** 5:58  
No i tutaj mógłbyś moda nas?

**Piotr Buczkowski** 5:59  
Ale tutaj tylko tylko administrator to może zrobić.

**Damian Kaminski** 6:03  
Tak tak, ale chodzi. Zmierzam do tego, że idea cate i to usunięcie powinno logować to sam zestaw informacji, kto i kiedy ikei said.

**Piotr Buczkowski** 6:05  
No dobrze.

**Lukasz Bott** 6:09  
I.  
Damian Damian i tutaj klikając ikonę tego kosza. Tak, czyli usunięcie trwale może wyświetlić moda.

**Damian Kaminski** 6:15  
No.  
O Jezus daj spokój.

**Piotr Buczkowski** 6:19  
Nie, nie, nie, nie, nie, nie.

**Lukasz Bott** 6:19  
W którym będzie komentarz uzasadnienia?

**Damian Kaminski** 6:23  
Ja bym nie był za tym to wiesz strasznie utrudnia.

**Piotr Buczkowski** 6:24  
Nie wiem.

**Lukasz Bott** 6:25  
Ale.

**Janusz Bossak** 6:27  
Poczekajcie.

**Lukasz Bott** 6:27  
No o k. Dobrze no minimum rejestrujemy tylko to kiedy kto co?

**Janusz Bossak** 6:33  
Czy nie wystarczy mamy taką funkcjonalność jak?  
Ta historia.

**Piotr Buczkowski** 6:38  
Ale nadciśnienie, naciśnięcie naciśnij usuń tutaj.  
I tak jest.

**Lukasz Bott** 6:46  
Dobry Janusz.

**Damian Kaminski** 6:48  
I tak jest masz lat, no ale wtedy jeszcze trzeba pisać, nie.

**Janusz Bossak** 6:50  
Taką funkcją.  
Mamy taką funkcjonalność jak historia zdarzeń na sprawie kejsy event.

**Piotr Buczkowski** 7:01  
Ale sprawy nie ma.

**Lukasz Bott** 7:02  
Sprawy nie ma.

**Janusz Bossak** 7:03  
Ale zanim wywołam Filip case, to mogę wpisać na to pytanie, czy.

**Piotr Buczkowski** 7:06  
Ale sprawy nie będzie.  
Nie wpiszesz.

**Janusz Bossak** 7:09  
No ale, ale zanim ją w skasuje.

**Piotr Buczkowski** 7:12  
Historia sprawy musi się odnosić do sprawy.

**Damian Kaminski** 7:16  
Że tu chyba się zgadzam z Piotrem, ale dajmy się wypowiedzieć januszowi w pełni.

**Piotr Buczkowski** 7:16  
Kasując sprawę kasują historię kasując sprawę kasujesz historię sprawy.

**Lukasz Bott** 7:21  
Te pierwsze pozwól januszowi powiedzieć.

**Piotr Buczkowski** 7:24  
Ale ja mówię kasując sprawę, kasując kasujesz historię sprawy, historię zdarzeń, sprawy też.

**Lukasz Bott** 7:28  
Zgadza się.

**Janusz Bossak** 7:30  
To nie jest historia sprawy.

**Piotr Buczkowski** 7:30  
Czy?  
No to.

**Janusz Bossak** 7:33  
Mówię o tym.  
Historii takiej zdarzeń, którą zrobiliśmy, która nie jest w sumie nigdzie wyświetlana w tej chwili jakoś sensownie.

**Piotr Buczkowski** 7:42  
Jest.

**Lukasz Bott** 7:42  
Mówisz o tej biznesowej historii?

**Janusz Bossak** 7:43  
Historia biznesowa to się nazywa, tak?

**Lukasz Bott** 7:45  
No właśnie mimo to też klient pytał.

**Piotr Buczkowski** 7:46  
Powiązana ze sprawą.

**Janusz Bossak** 7:49  
No pytanie, czy usuwanie sprawy powoduje usuwanie z tej historii?

**Piotr Buczkowski** 7:52  
Tak, tak, tak.

**Janusz Bossak** 7:54  
O k dobra no.

**Damian Kaminski** 7:57  
No właśnie, no to mamy rozwinięte znaczy dobra pytanie tylko czy w ramach tych zakładek jesteśmy w stanie to wpisać? Tu Piotr zaproponował aktywność administracyjną. Czy dokładamy nową na przykład w kategorie?

**Piotr Buczkowski** 8:04  
Utaj akt tutaj.

**Lukasz Bott** 8:07  
Nie tutaj także.

**Anna Skupinska** 8:09  
Mi się podoba rozwiązanie z dodanymi w aktywności administracyjnej.

**Janusz Bossak** 8:14  
No tylko pytanie, czy to jest tak jak gdyby administracyjna, bo.

**Lukasz Bott** 8:16  
To jest aktywność użytkownika, po prostu tak no.

**Janusz Bossak** 8:19  
Będzie użyty w jakiejś regule i ten Użytkownik biedny on jest nieświadomy tego, że tam usuwa sprawę tak bo będzie.

**Adrian Kotowski** 8:27  
Też może być bardziej dużym wpisów.

**Piotr Buczkowski** 8:27  
To nie to, niech nie ma tego przycisku dostępnego.

**Janusz Bossak** 8:31  
No tak, no ale on ostatecznie nie wie, że używa delikatesy. Tak no nie wie co się z tą sprawą dzieje, no.

**Lukasz Bott** 8:38  
Znaczy, nie słuchajcie, to leży w gestii projektach.

**Piotr Buczkowski** 8:39  
Zapłon administratora, że mu że mu dał taki przycisk.

**Janusz Bossak** 8:42  
Znaczy, chodzi o to, że to nie jest aktywność administracyjna, tak on.

**Lukasz Bott** 8:45  
Tak, tak.

**Damian Kaminski** 8:45  
W sensie Janusz nie kategoryzuje tego pod tą nazwą i co wtedy proponujesz, żeby tu było nowe nowa sekcja?

**Piotr Buczkowski** 8:52  
Nie.

**Lukasz Bott** 8:53  
Nie wiecie co ja ja myślę, że można było zrobić w ten sposób.  
Rejestrujemy to gdzieś, w których w jakiś tam odrębnych tabelach w strukturze amon dita może tam czekaj pieczarek, pozwól mi dokończyć, może w muzeach tyty i robimy do tego jakiś tam dedykowany raport dostępny tylko i wyłącznie dla administratorów, bo to najczęściej jest tutaj przykład z dentsu, tak, że żegalski musiał na przykład usunąć, znaczy on musiał usunąć. No to już gdzieś tam miał taką możliwość usunięcia sprawy, potem go dopytują, kiedy to się zdarzyło, czy coś w tym stylu, tak jakby on miał taki raport.

**Piotr Buczkowski** 9:04  
Nie po.

**Lukasz Bott** 9:28  
Gdzieś tam dostępny dla niego dedykowany właśnie z takiej aktywności użytkowników vity przefiltrowany pod kątem delikt case. Tak, no to sobie popatrzył na to, tak.

**Janusz Bossak** 9:39  
No ale czy my ktoś?

**Damian Kaminski** 9:40  
Ale to znaczy.  
Ja nie widzę powodu, że nie mogłoby być to tu jednak w sensie.

**Janusz Bossak** 9:43  
Nie mam.

**Damian Kaminski** 9:49  
Tu możemy dodać filtr typ akcji, bo nie mamy czegoś takiego, mamy tylko daty i tyle i szybko prze filtrujemy usuwanie.

**Lukasz Bott** 10:10  
Nie no to.

**Piotr Buczkowski** 10:11  
Kajsa vity kejs activity rok activity.

**Damian Kaminski** 10:11  
Nie.  
Mm k.

**Adrian Kotowski** 10:16  
Taką politykę i sądzili to jest powiązane sprawy. I tak powiem sprawy to za bardzo też szybko znika.

**Piotr Buczkowski** 10:18  
To jest.  
Proszę.  
To jest event jest event, sorry tak.

**Damian Kaminski** 10:25  
Keen, ale to jest historia biznesowa. Według mnie w klasie end.

**Piotr Buczkowski** 10:29  
Tak tak przemieszcza się tym zajmuje teraz.

**Adrian Kotowski** 10:29  
Tak, to ta opcja otworzył dokument obrony łącznik.

**Damian Kaminski** 10:35  
Steven, to jest to, co my wpiszemy, to to nie jest tu system tego niewypełniania ewentualnie usuwa ze sprawą, ale keen to jest historia biznesowa.  
Do tej pory tak było.

**Piotr Buczkowski** 10:46  
Ale czas Józef activity sorry.

**Lukasz Bott** 10:48  
Jest jest interaktywny.

**Piotr Buczkowski** 10:49  
Fejs.

**Damian Kaminski** 10:51  
K wyżej.

**Piotr Buczkowski** 10:51  
W niżej.

**Lukasz Bott** 10:52  
Jest jest 2 2 wyżej wyżej wyżej stop nie niżej.

**Adrian Kotowski** 10:52  
Nie jesteś, że tak tak tak to się troche.

**Piotr Buczkowski** 10:54  
Wyżej wyżej.

**Damian Kaminski** 10:54  
Czy koalicję?  
O dobra.

**Piotr Buczkowski** 10:56  
Niżej to to cię zapisuje właśnie maile dla filmu, tak?  
Tylko to jest czyszczone w momencie kasowania sprawy. Oczywiście dla tej sprawy, tak.

**Janusz Bossak** 11:05  
No tak, no to się terenie nadaje, no.

**Piotr Buczkowski** 11:07  
No dlatego mówię.

**Adrian Kotowski** 11:08  
Ale moglibyśmy muszę zrobić tak, że dać wyjątek na przykład, bo tu jest teraz powiązanie.

**Piotr Buczkowski** 11:11  
Nie, nie, nie.

**Damian Kaminski** 11:12  
Ale wtedy, gdzie to wyświetlać Adrian, niekoniecznie nie to znaczy według.

**Piotr Buczkowski** 11:15  
No właśnie.

**Adrian Kotowski** 11:16  
Raport stworzyć nowy na przykład.

**Piotr Buczkowski** 11:17  
Nie, nie to jest juz REACT vity log.

**Damian Kaminski** 11:19  
Ale skoro mamy tu, słuchajcie.  
Usuwanie sprawy to jest zdarzenie rzadkie. To nie będzie tu zapchane, nie wiadomo jak.  
To są zdarzenia, nie wiem serwisowe, że.

**Adrian Kotowski** 11:28  
Właśnie mi się teraz wydaje, że to jest często stosowane na przykład teraz jak są te sprawy zawierają, czyli to niektórzy klienci, gdzie chcemy ostatnio usuwać. Tam było 3 latach. Wiem chyba w rossmannie albo AmRest, więc jakby to może być częste.

**Janusz Bossak** 11:39  
Znaczy, nie mieszajmy.

**Damian Kaminski** 11:40  
No dobra, ale zobacz, co jest w historii logowania, no każde logowanie, więc to.

**Janusz Bossak** 11:45  
Znaczy.

**Piotr Buczkowski** 11:45  
Nie historia logowania, ta historia logowania zmiany na koncie to zmiany na koncie prasowa.

**Damian Kaminski** 11:47  
Ja wiem, chodzi mi o to, że że.  
Że tu jest dużo, też i ja myślę, że ta ministra cyjan aktywność jest jest.

**Janusz Bossak** 11:56  
Nie, nie jest dobra, ponieważ to jest aktywność administracyjna.  
Na przykład, że ktoś zmienił komuś uprawnienie albo dodał do.

**Piotr Buczkowski** 12:05  
Dobrze, to dodajmy nowo dodajmy nowo dodajmy nowo zakładkę.

**Janusz Bossak** 12:06  
Nie nadaje się tutaj.  
Zmieszanie, wpychanie po prostu innego zdarzenia, zdarzenia, które są zupełnie innego typu.

**Damian Kaminski** 12:16  
Dobrze, to dodajemy nową pytanie, tylko jak ją nazwiemy?

**Piotr Buczkowski** 12:16  
A jaka jako administrator administrator dla usunie sprawę z zakładki usunięte?

**Janusz Bossak** 12:23  
Tutaj się nie pojawiają.

**Damian Kaminski** 12:24  
Też to samo.

**Janusz Bossak** 12:27  
Tu się pojawiają aktywności administracyjne w rozumieniu zarządzania czyimś kontem, dodawania konta, zmieniania uprawnień do dania kogoś do grupy z grupy i tak dalej.

**Damian Kaminski** 12:27  
W sensie?

**Lukasz Bott** 12:34  
Tak do grupy tam tam.

**Damian Kaminski** 12:36  
Tak.

**Piotr Buczkowski** 12:36  
A coś coś coś przecisk wycięłam tam jest źle.

**Damian Kaminski** 12:42  
Już cofam.

**Adrian Kotowski** 12:44  
Myślę, że powinniśmy mieć takiego jak projekty wydarzeń, czyli.

**Damian Kaminski** 12:45  
Który?

**Piotr Buczkowski** 12:47  
Ten wróć strzałka w lewo, przycisk jest jakiś duży, dziwny.

**Janusz Bossak** 12:52  
A to są zdarzenia tutaj, które opisujemy na sprawach i.

**Piotr Buczkowski** 12:55  
Mogę się w ogóle coś się rozjechało tutaj.

**Damian Kaminski** 12:58  
Też się rozjechało, ale to znaczy to, że to jest lewej, to to jest Orlen. Tutaj sam przygotowałeś mi to jest sesja pod to, bo to jeszcze nie wymyślili, że u nich wszystko do lewej filler.

**Piotr Buczkowski** 13:09  
O k.

**Damian Kaminski** 13:10  
Więc to też może być konsekwencja?

**Piotr Buczkowski** 13:13  
No ok, bo to rozjechała na coś, widok mi się po prostu głowacz.

**Damian Kaminski** 13:13  
Zerknę jeszcze na.  
Dobra, sprawdzę to. Najwyżej poprawię już tu lokalnie, bo tutaj to może być związane z ich lokalnym. Tutaj, co jest system dobrze, słuchajcie, to w takim razie jaka jest propozycja co do nazwy, bo zaraz może się pojawić, może sprawy usunięte. Niekoniecznie pytanie, co ewentualnie jeszcze innego będziemy potencjalnie w przyszłości logować.  
Czy po prostu tylko do spraw usuniętych zakładka?

**Lukasz Bott** 13:42  
Tam gdzieś chyba ostatnio była rozmowa o logowaniu jakiś maili wysłanych ze sprawy czy coś takiego.

**Damian Kaminski** 13:48  
Ale to jest powiązane ze sprawą.

**Piotr Buczkowski** 13:48  
To właśnie właśnie to robię. Właśnie to robię. To jest powiązane ze sprawą tak.

**Lukasz Bott** 13:53  
Tylko że to jest no.

**Piotr Buczkowski** 13:54  
I będzie usuwane razem z usuwaniem sprawy.

**Lukasz Bott** 13:57  
O k dobra.

**Piotr Buczkowski** 13:59  
Bo jeżeli to jest sprawą odsuwana, bo tam zawiera tajne dane, to lepiej też wykasować historię wysłanych meili, tak.

**Lukasz Bott** 14:07  
Jasne, jasne, dobra no.

**Janusz Bossak** 14:11  
No to wygląda tutaj, no że jeszcze jedna zakładka i tu będziemy dodawać. No pierwszą pierwszym kandydatem jest to usuwanie tak może będą inni kandydaci do do tej historii.  
Ale no przynajmniej to gdzieś będzie, no.

**Lukasz Bott** 14:26  
Pinaca się aktywność użytkownika.

**Piotr Buczkowski** 14:29  
Nie.

**Lukasz Bott** 14:30  
No ale jak słyszę nazwać?

**Adrian Kotowski** 14:32  
A co na przykład logowania wysłanych spraw można zrobić coś takiego, na przykład, że wziąłem tylko ktoś na przykład się pokazuje tylko pierwsze 3 na przykład litery na przykład tematu maila, później są jakieś tam 3 kropki.

**Piotr Buczkowski** 14:42  
Nie nie, jeżeli jeżeli ma być usunięte, ma być usunięte.

**Lukasz Bott** 14:43  
Nie.

**Damian Kaminski** 14:45  
Dobra, ale nie mieszajmy, nie mieszajmy.  
Tu mówimy o usunięciu, tam to już Piotr.

**Lukasz Bott** 14:51  
Ogar.

**Damian Kaminski** 14:51  
Projektuje.

**Piotr Buczkowski** 14:54  
Wczoraj wysłałam tak jak to mniej więcej wygląda pierwsza wersja.

**Damian Kaminski** 15:00  
Dobra, żebyśmy zamknęli ten temat, czy jesteśmy w stanie dzisiaj ustalić nazwę zakładki? Czy na razie opisujemy backend?

**Adrian Kotowski** 15:08  
Na przykład rejestr zdarzeń coś takiego, że.

**Lukasz Bott** 15:08  
Zróbmy wiesz co.

**Piotr Buczkowski** 15:10  
Zakładka niech się nazywa na razie usuwanie spraw tak usunięte sprawy.  
Jeżeli coś będziemy dodawać, będziemy myśleć nad zmianą nas.

**Damian Kaminski** 15:19  
Dobra, Łukasz, masz wszystko.

**Janusz Bossak** 15:22  
Słuchajcie, bo.  
Bo jeszcze na sekundę ekran przejąć.  
Mamy jeszcze jedno miejsce, w którym się wyświetla coś, co nazywamy aktywność administracyjna, czyli tutaj, w zakładce logów systemowych.  
No i jeżeli byłby taki wpis, że tego dnia Marek im druczek, tutaj byłoby delikates numer.

**Piotr Buczkowski** 15:50  
Tak będzie.

**Damian Kaminski** 15:52  
Musi być to znaczy to tylko z tego poziomu ktoś będzie wyszukiwał, nikt nie będzie szukał tego po użytkownikach.

**Janusz Bossak** 15:52  
I tak.  
I.

**Piotr Buczkowski** 15:54  
Bo to jest to dlatego chcę dlaczego.  
Dlaczego? Dlaczego? Dlatego chcę, żeby to było logowane w wieze aktywny rok, żeby było tutaj widoczne.

**Damian Kaminski** 16:02  
Mhm.

**Lukasz Bott** 16:03  
No właśnie ja o tym myślałam tak samo.

**Janusz Bossak** 16:03  
Tak.

**Piotr Buczkowski** 16:03  
Było łatwo znaleźć, który który Użytkownik to tak stanu sprawę usunął.

**Damian Kaminski** 16:07  
Tak.

**Janusz Bossak** 16:09  
No to tak zróbmy tylko nie wyświetlamy ności użytkownika tak tutaj jest.

**Lukasz Bott** 16:10  
I i.

**Damian Kaminski** 16:14  
Właśnie, a może po prostu olejmy ten ekran, który ja pokazywałem?

**Piotr Buczkowski** 16:19  
Tak.

**Janusz Bossak** 16:19  
Dokładnie.

**Lukasz Bott** 16:19  
Tak, tak.

**Piotr Buczkowski** 16:20  
Też dobry pomysł tylko tutaj.

**Damian Kaminski** 16:22  
Tylko tutaj i już.

**Janusz Bossak** 16:22  
Tylko.

**Lukasz Bott** 16:23  
Tutaj i słuchajcie najwyżej tytuł tej tej aktywności użytkowników tak no.

**Janusz Bossak** 16:30  
Nie tu.

**Lukasz Bott** 16:30  
Bo tu co i logowanie i wylogowanie no przecież nie wszyscy są administratorami. Tak no.

**Piotr Buczkowski** 16:33  
Dlatego.

**Janusz Bossak** 16:35  
Nie, nie.

**Damian Kaminski** 16:36  
Ale to jest dostępne tylko dla ministra, no to znaczy o k. Rozumiem aktywny.

**Janusz Bossak** 16:40  
No to jest aktywność użytkownika, ale tu rzeczywiście tak, jeżeli ktoś tam na jakieś sprawie skasował coś nawet nie mając świadomości, to mamy datę, kto to zrobił, tu będzie napisane death case i numer tej sprawy i.

**Damian Kaminski** 16:54  
Tak.

**Lukasz Bott** 16:54  
I ewentualnie nazwa procesu no.

**Janusz Bossak** 16:57  
No może być z takiego, prawda?

**Lukasz Bott** 16:59  
Tak nie no nazwa protestu, bo bo wiesz jak nie masz numeru sprawy to nie dojdziesz po formularzu tak do do procesu.

**Damian Kaminski** 17:04  
Nie no, numer sprawy musi być.

**Lukasz Bott** 17:07  
Numer sprawy tak, ale jest ten numer sprawy, no to nie wyświetlisz go sobie nigdzie tej sprawy, bo jej nie ma. Tak więc nie wiesz z jakiego procesu ona jest o tym.

**Damian Kaminski** 17:07  
Jak?  
No ok no można można, no to już jest dla nas systemowa nie, a nie.

**Lukasz Bott** 17:16  
Nie no na pewno z procesu dorzućmy tak.

**Janusz Bossak** 17:19  
Jakąś tam identyfikować? Tak wszystko wiadomo opisać.

**Lukasz Bott** 17:19  
Dobra, to już wiem co.

**Damian Kaminski** 17:23  
Dobra.

**Lukasz Bott** 17:23  
Tak ja wiem, dobra, ale to ja to rzucę propozycję projektu najwyżej na jakimś tam designie. Jutro nie wiem przegadany także.

**Damian Kaminski** 17:33  
Dobra.

**Janusz Bossak** 17:33  
Ok.

**Damian Kaminski** 17:34  
Coś jeszcze Łukasz, miałeś drugiego?

**Lukasz Bott** 17:34  
No ta.  
Tak, miałem temat.  
Mam temat taki związany z obsługą tabelek i tam tak naprawdę swego rodzaju.  
Pomysł klientów to jest PKU tego nieszczęsnego przy przygotowaniu tego shitu klient chciałby zrobić sobie coś takiego, coś w rodzaju takiego pivota tylko że z edytowalny mi komórkami.  
Czyli innymi słowy.  
Coś w rodzaju excel?

**Damian Kaminski** 18:06  
Ja może co chce robić osiągnąć a nie jak chce to osiągnąć.

**Lukasz Bott** 18:08  
Dobra.  
Dobra, ja co chcę osiągnąć, a nie jak dobra to już pokazuje.

**Janusz Bossak** 18:11  
Bardzo słuszne.  
Bardzo słuszna.

**Lukasz Bott** 18:17  
Dobra, to najpierw dobra wprowadzenie szybko jak w tej chwili jest to robione jest rejestrowane ten czas pracy.  
Tak jest u klienta, jakkolwiek to się nazywa zadaniami, ale to jest generalnie jest rozpisane, są rozpisane dni tygodnia. To jest w podziale tygodniowym tak od poniedziałku.

**Damian Kaminski** 18:28  
Mhm.

**Lukasz Bott** 18:42  
Od dnia, czyli to jest od poniedziałku do niedzieli włącznie, bo niektórzy pracują też w weekendy.  
I mają zarejestrować sobie czas. W tej chwili jest oczywiście zrobiony raport w raport ze spraw na dany dzień, powiedzmy na czwartek.  
Rejestruje sobie na konkretny dzień, tak?  
Rejestruje sobie.

**Damian Kaminski** 19:06  
Zadania, tak jak u nas.

**Lukasz Bott** 19:08  
Tak jak u nas już sobie swoje konkretne zadania na konkretne zlecenia, opis tam, kto akceptuje typ godzin, ile tych godzin i tak dalej.  
No i tutaj mogę mieć na dany dzień, wtedy to już jest na konkretny dzień tygodnia.  
Mogę mieć to ileś raz, tak?  
Jeden z tam z uczestników spotkań, no w tym zespole projektowym po stronie PK fu, no marudzi, że to jest duża klimatologia ja tam jeden zrobiłem jedną sprawienie za pomocą funkcji get excel data tam odpowiednio spreparowany excel można sobie zaciągnąć tak.  
To dane natomiast to, co chciałby klient, to chciałby klient, by mieć tego typu.  
Czy widok?  
Mianowicie, że ją to przykładowym excelu, że.  
W wierszach wpisuje sobie zlecenie tak, to potem jak się ewentualnie opis pras tego i.  
Od poniedziałku wtorku, środy, czwartku, piątku niedzieli taki wpisuje sobie tego wypełniał sobie taką macierz, tak.

**Damian Kaminski** 20:09  
Mhm.

**Lukasz Bott** 20:10  
I tutaj i to jest to.

**Damian Kaminski** 20:10  
Tylko to nie jest wszystko w sensie, bo ja znam ten projekt. W ogóle analizowałem i teraz i tak będzie musiał wejść w każde zlecenie i tam to co pokazywałeś tam jest jeszcze 10 innych kolumn, które trzeba wypełnić.

**Lukasz Bott** 20:23  
Tak, który trzeba wypełnić tak, to to.

**Damian Kaminski** 20:24  
Więc to nie rozwiąże mu problemu klimatologii, tylko usprawni jeden element wprowadzania godzin.

**Lukasz Bott** 20:31  
Znaczy on to tłumaczy w ten sposób, że no gro osób te tak wypełnia, więc być to też się wzorują na jakimś już istniejącej aplikacji, no mieli jakąś tam aplikację, ma ludzi na nią. Ktoś tam zadecydował, że chcą to zrobić w modlicie tak, no a też ma swoje funkcjonalności.

**Damian Kaminski** 20:39  
Mhm.

**Janusz Bossak** 20:45  
Wejdź na.  
Wejdź na nasz dach.  
Zrób dashboard pivota.

**Lukasz Bott** 20:53  
No.

**Janusz Bossak** 20:53  
Nad samym dasz boardzie.  
Obok jako drugi raport zrób raport tabelarycznym.  
Jak klikniesz na skrzyżowaniu zlecenia i dnia to w tym raporcie tabelarycznym będziesz miał szczegóły tego co tam jest wpisane, że na przykład godzinę robił coś tam, a pół godziny robił coś tam i w tym raporcie tabelarycznym.  
No masz wtedy guziczek, Dodaj rekord i sobie rejestrujesz nowe zdarzenie.

**Damian Kaminski** 21:21  
To to nie ma tam Janusz chodzi. Ja rozumiem, że oni chcą mieć tabelkę tak jak tutaj, tak jak mówisz tabelaryczne, gdzie będą wypełniać tylko po pierwsze możesz to obronić, że nikt tak nie mówił na analizie, bo ja pokazywałem im dokładnie to, co ty zrobiłeś, że to tak będzie wyglądać. Oni to zaakceptowali.

**Lukasz Bott** 21:23  
Nie.  
Tak prosto tabelka.

**Damian Kaminski** 21:39  
Ee po drugie to nie rozwiązuje problemu globalnie, bo to pozwoli masowo wpisać godzinę, a i tak będzie musiał wejść w każdy dzień, czyli w każdą kolumnę i wpisać, że zlecenie księgowanie jest pod klienta. Tego ma być fakturowane fakturowane tyle godzin, więc to jest złudne przyspieszenie.

**Lukasz Bott** 21:56  
Tak, tak, tak.  
To znaczy, ja powiem tak, nic na siłę w razie jakby co to nawet jeżeli będą chcieli tylko taki prosty arkusz to to też da się to ogarnąć. Funkcję gtxl data i po prostu i zrobię im.

**Damian Kaminski** 22:03  
Mhm.  
I wtedy będą wypełniać dopiero dobra, ale to znaczy ja mam temat podobny drzwi mu więc może jeszcze.

**Lukasz Bott** 22:19  
No właśnie.

**Damian Kaminski** 22:21  
Wróćmy, bo teraz tak.  
Wim też chce tabelkę.

**Lukasz Bott** 22:26  
No właśnie.

**Damian Kaminski** 22:27  
W której będzie zaczytywał nawet setki wierszy, ale w zasadzie chcę zaznaczać jedną kolumnę, czyli te wiersze mają być do odczytu co do zasady.  
Natomiast ma być potencjalnie jedna kolumna edytowalna w postacie akurat u nich Czech boksa.  
I teraz trzeba było się zastanowić jak to mądrze ugrać, bo to jest w miarę podobny element.  
Czy bylibyśmy w stanie wytworzyć jakieś pole typu tabela lirycznego, ale które nie miałoby?  
Niekoniecznie miałoby historię. Ono miałoby jakiś skutek, niekoniecznie miałoby przeliczenia, tak jak w tabelach, czyli istniałyby oddzielne kasy, tylko dawałoby możliwość imputuj jakiejś w sensie wpisania jakiejś wartości, tak jak tu, po czym wywołanie jakiejś funkcji przy zaciskowej, na przykład, która by te dane rozp. Propagowała konkretne miej.  
Ta tak.  
Ee.

**Lukasz Bott** 23:24  
No to jest bardzo podobne do do tego zagadnienia. Tak no bo jak ja wprowadzę.

**Damian Kaminski** 23:28  
No u mnie kwestie wydajnościowe bardziej wchodzą w grę, natomiast tak to jest w pewien sposób zbieżny pytanie jak to ugrać? Bo tu Mateusz rzucił, że można by było dać. Nie wiem jakiś tam.  
Nowa skryptowe natomiast to no chodzi o rozwiązanie właśnie systemowe, a nie jednostkowe.  
Nie wiem czy.

**Piotr Buczkowski** 23:48  
Ale to, co chcecie osiągnąć, co tam będzie Edytowane?

**Damian Kaminski** 23:50  
Dobrze już już pokazuje, już pokazuje.

**Lukasz Bott** 23:52  
No to Damian teraz ty pokaż swoje, tak.

**Damian Kaminski** 23:54  
Tak, tak, tak już pokazuje. Powiem szerzej o tym w imię o co chodzi?  
O k. Więc z racji, że w imię faktury mogą mieć 300 pozycji i oni wiedzą czym to może skutkować, zwłaszcza w kontekście o cera, ale nie tylko cera po prostu, żeby to przeglądać to no, ale przede wszystkim chodzi o cerę, że to może być bardzo kłopotliwe, może mieć dużo błędów, ciężko je wyłapać.  
To tak ilość jest nie edytowalna tutaj nie zakładajmy tego, że to jest to tylko była opcja do wytłumaczenia. Czyli jest tabela, która nie jest tak naprawdę danymi z oc sera a jest.  
Zaciągnięta z innego systemu.  
Możemy to też porównać do tego, co za chwilę będzie w, czyli nikt nie musi już tego porównywać i poprawiać. My wiemy, że te dane są.  
W założenia poprawne, natomiast tu z racji, że to pochodzi z innego systemu, to właśnie one mogą nie być poprawne, bo po prawej stronie mamy podgląd faktycznej faktury. Po lewej stronie mamy pozycję zamówienia. Oni chcą, żeby te pozycje zamówienia zostały zaciągnięte formie tabelarycznej.  
I żeby Użytkownik jedyne co robił to zaznaczał ci sami co jest zgodne zgodne zgodne zgodne na koniec, co chcemy uzyskać pod tabelką tą, którą w której są te wiersze z informacjami, jest sobie przycisk, który przelatuje i kieruję po wszystkich wierszach tabeli i tam, gdzie nie jest zgodne to ma do opisu słownego, wypisać niezgodność w punkcie takim dotyczy nazwa przedmiotu i dwukropek i potem Użytkownik wejdzie do tego pola i będzie sobie wypisywał niezgodność w zakresie ilości niezgodność w zakresie ceny niezgodność.  
Jakakolwiek.  
Natomiast chodzi o to.

**Piotr Buczkowski** 26:05  
Źródło zewnętrzne.

**Janusz Bossak** 26:07  
A może sors genetyki?

**Damian Kaminski** 26:08  
Dobra, tylko teraz jak to jak zrobić tutaj po prostu Czech boksy nie.

**Piotr Buczkowski** 26:14  
Stefi wyniosłaś no zdefiniować tak zdefiniować typ kolumny, czego box?

**Damian Kaminski** 26:14  
To może być tabela es QL.  
Mhm.

**Piotr Buczkowski** 26:21  
I pozwolić, żeby zapisywać taką wartość wpis.

**Damian Kaminski** 26:24  
Przynajmniej w momencie edycji nie, bo to chociaż dobrze by było, żeby ona pozostała.

**Piotr Buczkowski** 26:28  
Tak.

**Damian Kaminski** 26:30  
Ale jak już tu przeniesiemy, to nabędzie w jakiś sposób zapisana, tak.

**Janusz Bossak** 26:30  
Jeżeli.

**Piotr Buczkowski** 26:33  
Tak.

**Janusz Bossak** 26:34  
Przesłuchajcie bo te bo cep sje tej koncepcji ta tabelka pozostanie tabelką a modlitwą tak czyli będzie obciążała kejs definicja.

**Piotr Buczkowski** 26:44  
Nie, nie.  
Źródło, zewnętrzne raport ze źródła zewnętrzne.

**Damian Kaminski** 26:47  
Źródło zewnętrzne tylko się wyświetli.

**Janusz Bossak** 26:50  
O k.

**Piotr Buczkowski** 26:52  
Tyle możemy dolać tak, powiedzmy drobne edycje.

**Damian Kaminski** 26:52  
Tylko.  
A w sumie chyba rozwiązałeś problem raport.

**Lukasz Bott** 27:00  
No przecież masz raport osadzony.

**Piotr Buczkowski** 27:01  
Raport raport.

**Lukasz Bott** 27:03  
I w robocie osadzonym też masz te?

**Damian Kaminski** 27:03  
Tylko dob.  
Ja tylko raport rodzi problem, że na raporcie mamy ograniczenie do 100.  
A oni mogą mieć 300.

**Piotr Buczkowski** 27:14  
Mamy ograniczenie do stoła mamy zresztą.

**Janusz Bossak** 27:17  
O stronicowanie mamy.

**Lukasz Bott** 27:19  
Więc dzwonisz?

**Janusz Bossak** 27:20  
Jak przerzucisz na drugą stronę to tak jakby pierwszej strony już są nieaktywne.

**Damian Kaminski** 27:24  
Mhm.

**Lukasz Bott** 27:26  
Tylko by trzeba było się upewnić. Damian, czy raport osadzony bazujący na źródle zewnętrznym? Tak no, bo dane pochodzą z zewnętrznego źródła.  
Yy tam będzie działał ten mechanizm tych czek boksów, tak.

**Damian Kaminski** 27:38  
Chyba można go wyświetlić, ale nie będzie działał.

**Piotr Buczkowski** 27:38  
Nie będzie.

**Lukasz Bott** 27:41  
Nie no będzie bo nie będzie.

**Damian Kaminski** 27:41  
W sensie na na razie na razie nie będzie.

**Lukasz Bott** 27:45  
Znaczy nie będzie.

**Damian Kaminski** 27:46  
Po nie będzie zwracał ze źródła zewnętrznego chyba nie zwraca żadnej informacji.

**Lukasz Bott** 27:50  
Nie.

**Piotr Buczkowski** 27:51  
No bo to trzeba to robić.

**Damian Kaminski** 27:53  
No dobra, to trzeba dorobić. Natomiast problem polega na tym, że jak będzie 300 pozycji i mamy stronicowanie.

**Piotr Buczkowski** 28:00  
To trzeba zwiększyć.

**Damian Kaminski** 28:02  
O k.  
Dobra.

**Piotr Buczkowski** 28:04  
Może dla dla źródeł zewnętrznych.  
Można zwiększyć.

**Lukasz Bott** 28:11  
Słuchajcie, to tak.

**Damian Kaminski** 28:11  
No dobra, no to wtedy to nie jest zbieżne z Łukasza tą kwestią, bo tutaj rozwiążemy to raportem.

**Janusz Bossak** 28:15  
W ogóle w ogóle kompletnie coś innego.

**Lukasz Bott** 28:18  
Część to jest zupełnie coś innego.

**Janusz Bossak** 28:21  
Znaczy ten temat Łukasza, to ja bym go zgłębił bardziej, bo to jest dość często sytuacja.

**Lukasz Bott** 28:28  
Tak tak to jest.

**Janusz Bossak** 28:30  
Bo był taki pomysł.  
Yy, żeby wracam tego pomysłu, drążę ten pomysł. Tak był taki pomysł, żeby nadać bardziej wyświetlać sprawę.

**Lukasz Bott** 28:37  
No tak no.

**Janusz Bossak** 28:44  
Czyli mając ten twój taki tą macierz, którą tam pokazałeś, która jest de facto piwo, potem, który zbiera tam po tej po lewej stronie jakby projekty, a u góry dni powinna owaniu rozumiem, że to jest wynik jednej sprawy, że tamte 1,5 godziny to on wpisał, że nad tym projektem w piątek pracował półtorej godziny, no raz teraz.

**Lukasz Bott** 28:52  
Tak.  
Tak.  
Tak no to znaczy mojej koncepcji to jest jeden wpis w tabelce tak, no ale tak.

**Janusz Bossak** 29:11  
Jeżeli to jest jeden wpis tabelce, no teraz właśnie na tym naszym boardzie jeżeli by nauczyć dashboard, żeby on po prawej stronie od tej tabelki wyświetlił tą sprawę.  
Tak, czyli byłoby okienko taki nie wiem cokolwiek, której by się otworzyła. Ta sprawa, która jest na skrzyżowaniu tych 2.  
Znaczy wiersza i kolumny, no to on sobie tam wpisze, kliknę zapisz i mu się tu pojawi. Nie tylko potrzebujemy na dashboard, gdzie takiego mechanizmu, żeby obok jakiegoś raportu pokazać sprawę i to mogłoby być zastosowane do wielu rzeczy, jeżeli moglibyśmy mieć raport tabelarycznym taka tabelka, jak tutaj widzimy tak na raporcie po prawej stronie, to miejsce na tą sprawę i teraz jak klikam w wiersz tej tabelki to myślę. Ta sprawa pokazuje po prawej stronie mogę coś tam w niej zrobić.

**Lukasz Bott** 29:35  
Mhm.  
Sprawa wiersza.

**Janusz Bossak** 29:59  
Sprawa z tego wiersza, który kliknąłem nie.  
I to miałoby za to?

**Damian Kaminski** 30:03  
Tylko chodzi ci o podgląd tak z prawej strony tego co aktualnie zaznaczymy edycyjne.

**Lukasz Bott** 30:07  
Tak, ale taki podgląd, ale podgląd edycyjnych.

**Janusz Bossak** 30:11  
Podglądali wizyjny to znaczy po części to mamy tak no bo jak kliknę w ten wiersz w tej tabelce to mi się wyskakuje okienko popup.

**Damian Kaminski** 30:20  
Tylko to dalej. Ja czuję, że żebyśmy to znaczy, to jest jakiś pomysł, natomiast nie wiem czy to jest pomysł, który ten klient, ten gość, który tam zaproponował.

**Lukasz Bott** 30:20  
Ale okienko.

**Damian Kaminski** 30:31  
On to dalej czuje, że rozumie inaczej on chce mieć.  
Tabelę, ja nie mówię, że my mamy tak zrobić tylko tak jak ja czuję to wymaganiom. Chcę mieć tabelę zestawienia całego tygodnia, gdzie ma w kolumnach dni w wierszach zadania. Co więcej, zwróćcie uwagę, że on te zadania chce zdefiniować dopiero.

**Lukasz Bott** 30:37  
Tak, tak.

**Damian Kaminski** 30:51  
Czyli.

**Lukasz Bott** 30:52  
Tak, tak on.

**Janusz Bossak** 30:54  
No to.

**Damian Kaminski** 30:54  
Jeszcze nie ma.

**Janusz Bossak** 30:56  
No to dodaję, Dodaj Dodaj sprawę.  
I w tej sprawie definiuje to zadaniem się w tej tabelce pokażę. Tak znaczy ja wiem, że ludzie chcą pracować jak na excelu.

**Damian Kaminski** 31:07  
Mhm.

**Janusz Bossak** 31:08  
Wszystko pisać, wierszach i kolumnach, ale to nie jest excel.

**Piotr Buczkowski** 31:08  
Nie.

**Janusz Bossak** 31:12  
Tylko to jest system obiegu dokumentów.

**Damian Kaminski** 31:15  
To znaczy, abstrahując od tego, czy to zrobimy, czy to znaczy, może się nie abstrahując, ale w kontekście tego wymagania? Według mnie Łukasz, to i tak możesz się powołać, że to ma być wycenione. Można poszukać nagrań. Ja dokładnie to przedstawiłem, tak jak ty to zrobiłeś i oni to zaakceptowali. Powiedzieli, że to jest o k, więc jeśli cokolwiek innego to jest poza poza zakresem.

**Lukasz Bott** 31:15  
Tak, no więc.  
No to wiesz co jak masz?  
Jak?

**Janusz Bossak** 31:39  
Dokładnie.

**Lukasz Bott** 31:39  
To słuchaj, Damian, to jak gdzieś tam w wolnej chwili byśmy był w stanie to znaleźć.  
To będę bardzo wdzięczny tak, no, bo w tym momencie mamy podkładkę także.

**Janusz Bossak** 31:50  
Znowuż projekt.  
Projekt projekt pisemny projekt.

**Damian Kaminski** 31:54  
Te Kamil, pamiętasz, byłaś na tych spotkaniach?  
Czy nie pamiętasz?

**Lukasz Bott** 32:02  
Pewnie to było sprzed roku jakiegoś tak, bo to zanim ten temat.

**Damian Kaminski** 32:05  
No może nawet sprzed 1,5.

**Janusz Bossak** 32:07  
Co mamy na radę jeszcze?

**Damian Kaminski** 32:08  
Dobra, to znaczy tak, ania.

**Lukasz Bott** 32:09  
Jeżeli chodzi o mnie, to jeżeli chodzi o mnie, to ja dziękuję się, wyłączam to wszystko co miał.

**Janusz Bossak** 32:14  
Brak dzięki.

**Damian Kaminski** 32:14  
Ten raport dla mnie jest jakimś rozwiązaniem. Ja muszę tylko pogadać, bo tu jest koncepcja odwrotna, oczywiście pewnie możemy to zrobić, ale ja bym jednak zasugerował im, że będą zaznaczać tylko to, co jest nieprawidłowe, bo wtedy będą też mieli mniej zaznaczania i oni jeszcze chcą opcję zaznacz wszystko, a właśnie może jak będzie tylko zaznacz złe.  
To pod niepotrzebne jest, zaznacz wszystko.  
No przy czym?  
Przy czym zaznaczenie dobrego rozpatrz.  
Jako pewność, że ktoś to sprawdził, a a złego to tak ktoś przeleciał i no ale zobaczymy. Pogadam na razie z nimi i zrobię na to PA nie wiem czy mieliście okazję.

**Piotr Buczkowski** 32:57  
No to no to zaznacz wszystko nie ma sensu.

**Damian Kaminski** 33:00  
No właśnie to zaznacz wszystko nie ma sensu. Tak zgadzam się.

**Kamil Dubaniowski** 33:02  
Tak, będziemy musieli zweryfikować to z kwotą z faktury. No bo rozumiem, że.  
Podsumowaniem będziemy odczytywać od sera albo.

**Damian Kaminski** 33:11  
Tak, tak, tak, to znaczy zawsze pod gotowe możemy mu im zrobić podwójny tęże się nie zgadza i czy na pewno?

**Kamil Dubaniowski** 33:13  
To przepisze.

**Damian Kaminski** 33:19  
Uzupełnił opis słowny tak, bo chociaż możemy to też jakoś wali dować, dobra.

**Janusz Bossak** 33:23  
Słuchajcie, jeden temat jeszcze związane z tą tabelką, bo to mi ciągle chodzi po głowie czy dla takiego przypadku czy dla takich przypadków gdzie tabelki miały być duże, a jeszcze do tego coś miałoby być w nich robione czy nie lepiej byłoby gdyby wyświetlać się w osobnym oknie, czyli mamy tutaj nawet początek takiej tabelki jak tutaj.

**Damian Kaminski** 33:23  
Nie wiem czy.

**Piotr Buczkowski** 33:44  
Nie, to nawet kwestia tego, że wszelkie operacje tabeli typu foris są jakieś wyliczanie sum, czy coś będzie obciążało.

**Damian Kaminski** 33:58  
Nie wiem czy to Janusz miał na myśli.

**Janusz Bossak** 34:00  
Nie chodzi mi o to, żeby wyświetlać tak był przycisk.

**Damian Kaminski** 34:02  
Żeby był przycisk pokaż tabelę, tak?

**Piotr Buczkowski** 34:04  
No ale to jest.  
Nie, bo to, bo to nie serwera obciążysz odciążyć przeglądarkę, obciążyć serwer.

**Janusz Bossak** 34:16  
No dobra no.

**Piotr Buczkowski** 34:17  
Bo i tak wieczne muszą być wczytane po stronie serwera, żeby wykonać na nich operacji.

**Janusz Bossak** 34:22  
Że obciąża się ten formularz?

**Piotr Buczkowski** 34:23  
Także.  
Nie serwer obciążasz.  
Bo na pewno będziesz chciał jakieś sum zrobić, tak.  
W jakiejś formie cyfrowej.  
Jakąś regułę tabeli i tak będzie to obciążało, może trochę nie przeglądarkę, ale serwer, serwer tak także lepiej.  
Nie wstawia się takich dużych tabel, tak lepiej zrobić mechanizm.  
Na przykład wyświetlania tabeli na podstawie.  
Oddzielnej tabeli, tak.

**Damian Kaminski** 34:54  
Ja bym powiedział jeszcze szerzej, że my przed wystepem.  
Powinniśmy jeszcze zaopiekować to.  
Że ta tabela niekoniecznie musi być wczytywane, bo możemy po prostu odczytać stopki, a może zrobić coś takiego do faktur? No bo właśnie będzie wszystko szło z tabeli jak będzie zma powane a tu już nie ma potrzeby sprawdzania, bo wszystko jest to samo, tylko pytanie to znaczy nie no tak, podgląd wtedy generuje się na podstawie xm LAI. Może powinniśmy wprowadzić nowy mechanizm załaduj tabelę tylko dla tych klientów, którzy będą faktycznie na tej tabeli coś potrzebowali zrobić, bo oni mają, nie wiem właśnie.  
Dodatkowe pola, gdzie już na poziomie linii definiują nie wiem jakieś przypisanie MPK czy cokolwiek, a wszystkim innym pozbylibyśmy się wtedy ogromnej ilości dodatkowych kwasów, które są zbędne, bo oni tak będą pracować na podsumowaniu. No bo tutaj właśnie wypada nam ten mechanizm o c ryza ci gdzie trzeba porównywać i tak dalej.  
Ktoś sobie wyświetlenia, ale to już jest odrębny temat.

**Janusz Bossak** 35:56  
Dobra, ale sprzedajmy.  
Mam czas, musimy wziąć.

**Damian Kaminski** 36:00  
Te kolory, te kolory czy mieliście okazję na to spojrzeć czy teraz, bo ania już chce na tym pracować czy ma?

**Janusz Bossak** 36:06  
Zaproś tylko jakby ocenę za pomocą sztucznej inteligencji, co jest fajniejsze, co nie, ale ja nie wiem jakie są, nie pokazałeś nam jaka jest paleta to tablo i właściwie nie bardzo.

**Damian Kaminski** 36:17  
Pokazałem.

**Janusz Bossak** 36:19  
No nie.

**Damian Kaminski** 36:19  
Tylko nie wiem, czy to otworzyłeś w odrębnym pliku.

**Kamil Dubaniowski** 36:19  
A jeszcze jeszcze może może do tego filmu Damian sekundę, bo nie wiem, czy ja zgubimy wątek, ale.

**Damian Kaminski** 36:24  
No.

**Kamil Dubaniowski** 36:27  
Opowiadałeś o tym, jak działa teraz zwracanie tych pozycji z zamówienia, że to jest wykonanie procedury składowane i ja dostanę jasona, dostanę tam 300 pozycji i ja teraz mam zasilić w locie tak o k.

**Damian Kaminski** 36:34  
Tak.  
I wpiszemy do źródła.  
Tak, tak, tak, tak, to spoko.

**Kamil Dubaniowski** 36:40  
To to będzie na tyle wydajne, że te 300 nam nie będzie. Nikt czekał, aż się przemieli. Nie wiadomo ile, no bo to będzie klikał Użytkownik. Tak.

**Damian Kaminski** 36:46  
Czeka 5 sekund, ale nie dłużej. Według mnie, to znaczy nie będzie Użytkownik, bo jak odczyta o cr, to zanim przekażemy użytkownikowi, to już czytamy. Użytkownik będzie ładował tylko jak nie odczyta ocr numeru zamówienia.

**Kamil Dubaniowski** 36:58  
No tego trochę się obawiam jakości tego, czy to, że to będzie małe.

**Damian Kaminski** 37:02  
No to tu już nic nie poradzimy.

**Kamil Dubaniowski** 37:06  
Czyli wtedy ręczne wskazanie no i też trzeba wziąć pod uwagę, że on odczyta i na przykład podstawi coś źle, więc też będzie trzeba dodać całą maszynę, żeby to wyczyścić i wskazać swojej podać swoje.

**Damian Kaminski** 37:18  
Mhm.  
No tak, to to już musimy projekt już procesowo zaopiekować.

**Kamil Dubaniowski** 37:20  
Tak się.

**Damian Kaminski** 37:27  
Dobra, to wracam do tych kolorów, nie wiem, czy Janusz otworzyłeś to odrębnie, bo tam napisałem, że kimś z tego nie wyświetla.

**Janusz Bossak** 37:32  
Nie jakoś.  
No.

**Damian Kaminski** 37:37  
To jest tablo to jest nasze nasze jest jak widzicie nie to żywsze możemy mogę wpisać jeden jedno słowo i wrócimy do takiego jak ma tablo w tablo domyślnie jest 10.  
U nas proponuję, żeby domyślnie było 20.  
W pierwszej serii plus robić przynajmniej ze 3 serie, żeby ktoś nie musiał wybierać tego tylko, żeby to od razu było systemowo zaopiekowane.  
Ee bo to nas nie boli różnice, nasycenie nasza paleta bardziej żywa w tablo jakieś tam różnice.  
No i przede wszystkim przewaga, jeśli chodzi o to, że my mamy te 20 pierwszej serii tak, czyli jest to bardziej zróżnicowane.

**Janusz Bossak** 38:21  
Znaczy i tak i nie, bo zobacz ten.  
Wiadomo, mężczyźni inaczej widzą kolory, no ale cyjan niebieski i indygo są tak blisko siebie, że tak powiem jak to będziesz miał na wykresie, to jeszcze jest morski, który jest do tego niebieskiego też podobny.  
Yy no o nas wychodzi niebieski morski, tak to jest to po prawej strony, że tego nie rozróżnił zauważę te kolory, które są w tablo.

**Damian Kaminski** 38:45  
Mhm.  
No bo jest 10. Zgadzam się i teraz 2.

**Janusz Bossak** 38:51  
One są, są są dalej od siebie tak w sensie kolorystycznym, tak.

**Anna Skupinska** 38:53  
Tak.

**Damian Kaminski** 38:57  
Tak tylko musimy pamiętać to teraz tak najprostsza propozycja. Zmieniamy kolejność, czyli ustawiamy czerwony, zielony niebieski tak dla tych, żeby 10 pierwszych było różniących się potem wprowadzamy te turkusowe.  
I to dotyczy tylko pierwszej serii, bo znowu kolejna seria to będą tylko odmiany tych kolorów, czyli trochę jaśniejszy czerwony. Wiadomo, że jeśli chcemy zaprezentować 40 różnych czy 60 różnych serii, to one nie będą już tak mocno się różnić od siebie. No nie da się tego zrobić. Mamy ograniczoną paletę, tak.

**Janusz Bossak** 39:32  
No trzeba brać pod uwagę, że tablo ma milion lat więcej doświadczeń niż my, łącznie jakby polityczne mendy lisy, które poświęcili na to.

**Damian Kaminski** 39:38  
Mhm.  
Mhm.

**Janusz Bossak** 39:42  
Coś w tym jest, że zrobili tak, a nie inaczej nie.

**Damian Kaminski** 39:46  
O k. Ale to nie przeszkadza nam w żaden sposób zrobić te tego tak tylko po prostu zmieniamy kolejność. Nie ustawiamy to to tak jak on tu zaproponował.

**Janusz Bossak** 39:56  
Znaczy mi chodzi też o to, że że 10 kolorów.

**Damian Kaminski** 39:56  
Tylko.  
Że 10. Tak uważasz?

**Janusz Bossak** 40:00  
Dlatego, że prawdopodobnie doszli do wniosku, że na wykresie i tak i tak człowiek nie odróżni więcej niż 10 kolorów.  
W związku z tym.

**Damian Kaminski** 40:09  
Bo ja się obawiam tylko tych wiesz tych treat tak gdzie jest dużo, więc kolejne serie i tak powinniśmy zaopiekować.

**Janusz Bossak** 40:14  
Dlatego dlatego trzeba zrobić funkcjonalność pod tytułem pozostałe.  
Czyli to, co mówiliśmy, że pokazujemy na tej mapie do pewnej pewnego poziomu.  
Ee jakby istotności.  
A poniżej to jest szum.  
Który nie trzeba?

**Damian Kaminski** 40:36  
Mm no nie zgodzę się do końca w sensie no dobra patrzysz tylko przez pryzmat jakie te mapy, no ale to wtedy to cała twoja mapa w prawym Dolnym rogu będzie w jednym kolorze.

**Janusz Bossak** 40:40  
No dokładnie.  
Będzie jeden kwadracik pozostałe.

**Damian Kaminski** 40:52  
Ale ja niekoniecznie tak chcę.  
Ja chcę jaką Użytkownik, żeby tam były małe kolorki różne.

**Janusz Bossak** 40:55  
Chcesz taką siatkę?  
Są to te co on z tego się dowiaduje.

**Damian Kaminski** 41:02  
No dobra, no to patrzymy na te mapy, a teraz spójrz na wykres.  
Taki liniowy tak.  
Połączone punkty i tam mam już na przykład joby i czołgów mamy 15.  
I ile było wywołanie grobów dziennie? Tak.

**Janusz Bossak** 41:20  
To trzeba wziąć 10 najbardziej aktywnych dziobów, które są najwyżej to, które są najniżej. Może nie są istotne i wyeliminować, znaczy, wiecie, to nie jest tak, że my wymyślimy.

**Damian Kaminski** 41:20  
I jak?

**Janusz Bossak** 41:32  
Jakby rozwiązanie na każdą kombinację.  
No są pewne zasady tworzenia wykresów, jeżeli na wykresie jest więcej niż 10 linii, prawdopodobnie to Użytkownik i tak i tak nie jest w stanie tego prześledzić.  
To będzie miał jakiś szum informacyjny, mnóstwo linii, ale on.  
Nie wie tak, no jeżeli te wszystkie linie się skupią, powiedzmy gdzieś tam na dole jako mało istotne, a będziesz miał 4 czy 5 czy 6 głównych procesów czy drobnych, które zajmują czas.  
No to ta reszta to jest szum informacyjny. Tak możesz tego w ogóle nie pokazywać, to jest kwestia dobrego robienia wykresów. Według mnie puszczanie właśnie palety 20 kolorów powoduje, że.  
Taki nasz konsultant czy twórca tego raportu się rozleniwia? Tak no no dobra, niech się pokaże wszystko co tam mam.

**Damian Kaminski** 42:24  
Dobra, to znaczy powiem tak, ja rozumiem, że wtedy wykres nie jest czytelny, tylko chodzi mi o to, żebyśmy żebym ja jako Użytkownik, jeśli świadomie podejmę decyzję, że ja chcę wyświetlić 30 informacji na tym raporcie, to żebym ja nie musiał, bo dzisiaj mamy 20 i ja wszystkie pozostałe, albo się dublują kolorami, albo muszę wyklikać ręcznie. Tylko do tego zmierzam, żebyśmy my, jako projektanci systemu.  
Zaopiekowali to, że jak ktoś świadomie chce wrzucić 40.  
To każdy z tych 40 domyślnie będzie miał inny kolor, a nie muszę je przeklinać, bo mamy tylko zdefiniowanych 10 albo 20.

**Janusz Bossak** 43:03  
Nie.  
To nie jest właściwy kierunek według mnie właściwym kierunkiem jest powiedzenie użytkownikowi, słuchaj użytkowniku.  
Żeby ten wykres miał sens.  
Przedstawmy więcej, na czym najwięcej 10 rzeczy. Pozostałe potraktujmy na razie jako szum informacyjny i tyle, bo to.

**Damian Kaminski** 43:31  
No dobra, ja się z tym nie zgadzam, bo potem mogę zastosować filtry.

**Janusz Bossak** 43:33  
1000, najmniejszym.  
A czemu Nie możesz?

**Damian Kaminski** 43:37  
I ja ograniczę potem koniec końców, ale to spowodować spowoduje, że musiałby dynamicznie te kolory znowu przeliczać, czyli jak jeden Filip zastosuje to niebieski reprezentuje styczeń, a jak zastosuję, że chcę od czerwca to niebieski reprezentuje nagle czerwiec, czyli muszę na nowo się nauczyć legendy.

**Janusz Bossak** 43:56  
Weź weź to pokaż i to co rozmawiasz z nami, weź porozmawiaj z Michałem Maliszewski.

**Damian Kaminski** 44:02  
O k.  
Dobra, bo tutaj też wiesz, ja wpisałem, porównaj to z tablo, a to jest jakieś domyślne. Tak mnie wiemy, de facto nie znamy tego tablo dobra, porozmawiam z Michałem.

**Janusz Bossak** 44:12  
Jest oni mają więcej tych palet różnych, bo to jest jedna bo tam jest znaczy na świecie istnieje wiele jakby palec przygotowanych przez różne firmy.

**Anna Skupinska** 44:12  
A ja.

**Janusz Bossak** 44:21  
A dobi tam przygotowało swoją jakąś i tak dalej i tak dalej i no wszyscy pracują nad tym, żeby te palety były. One są dobierane pod kątem też właśnie kontrastu pod kątem tego, że osoby z tym kolorów nie rozróżniają, żeby mogły rozróżniać, żeby to się ci co nie widzą kolorów, widzą odpowiednie szarości tego i widzą różnicę. To jest jeszcze jedna rzecz, tak.  
Więc to są naukowo dobierane te kolory to nie jest tak po prostu, że sobie ktoś wziął ten kolor i już nie jest ogromna praca, żeby dobrać te kolory tak, że nawet ci właśnie, którzy nie widzą kolorów, żeby widzieli.  
Odcienie szarości.  
Więc no o prawdę.

**Damian Kaminski** 45:04  
O k. To także zostawmy porozmawiać z Michałem, bo to jest jakiś przykład tablo pewnie nie jedyny tam tak jak powiedziałeś jest pewnie kilka bazowych mi chodzi tylko o to, żeby wyeliminować konieczność pracy ręcznej, jeśli ktoś chce wyświetlić 20 30, 40, bo dzisiaj.

**Janusz Bossak** 45:19  
To jeżeli mi chodzi tylko o to, że jak ktoś chce wyświetlić 20 lub 40 znaczy, że źle robi.

**Anna Skupinska** 45:26  
A ja mam jedno pytanie dotyczące kolorów, bo dostałam inne zadanie, w którym mam dodać wiele kolorów różnych i chciałam się dowiedzieć czy to Damian o nim wiesz to może?

**Janusz Bossak** 45:26  
I ten.

**Damian Kaminski** 45:29  
Mhm.  
To jest to zadanie, to dlaczego uważasz, że to jest sin?

**Anna Skupinska** 45:38  
Nie do końca nie, nie mówię o tym do końca tym zadaniu. Wydaje mi się, że nie mówię o tym zadaniu. No chodź widzieć mój ekran.

**Damian Kaminski** 45:41  
Dlaczego?  
No no to jest to zadanie, to jest dokładnie to zadanie 20 kolorów i 4 serie tam było jako propozycja otwierałaś sobie załącznik.

**Anna Skupinska** 45:46  
O ciebie zadaje 2 1, a o k jest, a więc ja już.  
A tak to ty.  
No to jest już tutaj, ale tutaj się nie da kliknąć. To są po prostu tekst, więc.

**Damian Kaminski** 46:00  
Przejedź do góry, dałem to h. Jedynką nie przejeść do góry details.

**Anna Skupinska** 46:02  
A tutaj.  
A tak tutaj są te wszystkie.

**Damian Kaminski** 46:07  
Nie do góry, do góry do góry nad tym wszystkim i powolutku do dołu.  
W ramach kolorów predefiniowane.  
Tutaj w załącznikach HTMLZ lepszym opisem tego co niżej.  
Bo tu jest źle, może powinienem w ogóle tego nie nie, nie wpisywać. Po prostu wkleiłem to, żeby były te chaszcze, to jest to to na razie się z tym wstrzymujemy. Ja porozmawiać z Michałem.

**Anna Skupinska** 46:22  
Aha.  
Aha, bo ja w tym pracowałam i wprowadziłam te kolory, żeby się dodawały do.

**Damian Kaminski** 46:38  
No widzisz, Janusz, czy tu jest według ciebie?  
Jeśliby było ograniczenie do 10, to by było źle, no myślę, że tu jest więcej niż 10 takich kluczowych klocków.  
Bo ogórki mają pewnie już w sobie 10. Jeszcze tu cebule też mają jakieś inne. No ja rozumiem, że ja rozumiem, że to może być nieistotne w kontekście, to znaczy to może być dla ogólnego punktu widzenia mało czytelne, jeśli jest więcej niż 10.

**Janusz Bossak** 46:57  
Co z tego wyjdzie?

**Damian Kaminski** 47:09  
Ale też zakładam, że ktoś może potrzebować mieć więcej niż 10 i czemu mu tego nie usprawnić po prostu pozą.

**Anna Skupinska** 47:15  
Ale pamiętam więcej niż 10 kolorów mamy szczerby.

**Damian Kaminski** 47:18  
Mamy 20. Mamy 20, teraz?

**Anna Skupinska** 47:19  
Tak tak, mamy 2 wyjścia.

**Damian Kaminski** 47:21  
Tylko wszystko, co ponad 20 się powtarza, albo trzeba przerabiać ręcznie.

**Janusz Bossak** 47:21  
Tak.

**Anna Skupinska** 47:24  
Tak, to jest. To jest wersja obecna z develop i teraz się powtarzają. Jest na przykład to i to ma taki sam kolor.

**Janusz Bossak** 47:34  
Bo teraz mamy ile 23 10.

**Damian Kaminski** 47:36  
Tak, 20 20 plus możliwość definiowania ręcznie.

**Anna Skupinska** 47:36  
Tak, 20.

**Janusz Bossak** 47:40  
No to czym się różni to od tego nowego, skoro mamy 20, to dlaczego?

**Anna Skupinska** 47:43  
No.

**Damian Kaminski** 47:43  
To już jest.

**Anna Skupinska** 47:45  
To są inne, w każdym ma inny kolor, każda rzecz oczywiście jest, jakby ktoś już miał jeszcze tyle, że wszystkie te palety się już skończą. Im kolory to zacząłby się znowu powtarzać, no ale cóż.

**Damian Kaminski** 47:55  
O właśnie i to jest to, co Janusz powiedziałeś, że nieistotne są te, które tu są bardzo małe i tu się zgadzam, tylko jak one się pokrywają kolorem, no to to powoduje zaburzenie tego, która Legenda, bo bo nie mamy na razie wyróżnienia, czyli ja patrząc na legendę niebieski, teraz nie wiem, który to jest niebieski, czy ten tutaj, w cebulak, czy w papryce, na Górze, czy jeszcze jakiś inny.  
A jeśli by dodało jakieś inne odcienie, no to może łatwiej to rozróżnienie, a i wtedy na podstawie tej analizy mogę stwierdzić dobra, tu mam dużo szumu, właśnie takich drobnych rzeczy i wtedy wchodzę w re definicję tego tego raportu i oznaczam, że wszystko poniżej levelu takiego jest jednym kolorem.

**Janusz Bossak** 48:37  
Wejdź, wejdź w edycję tego koloru i ustaw sortowanie po pierwszej.  
Wykres jest po prostu źle zrobiony.

**Anna Skupinska** 48:45  
A czy to mój wykres do prób, więc.

**Janusz Bossak** 48:46  
Myśl.  
No nazwa produktu i sortowanie.  
Czy tutaj no nie wiem czy tam jest tak sortuj po tam rosnąco albo malejąco nie poetyckie tak wartościach.

**Damian Kaminski** 49:05  
Nic to nie dało aktualizuj automatycznie pokaż się, coś się zmieniło, bo.

**Janusz Bossak** 49:11  
Masz wyłączony?

**Anna Skupinska** 49:11  
O k.

**Janusz Bossak** 49:14  
Wojny ustawić te kolory jakby.  
Żółte na dole, ten dalej coś tu jest nie tak.

**Damian Kaminski** 49:20  
No niekoniecznie, no właśnie, bo widzisz ja no ja rozumiem cię Janusz, natomiast po wartościach kolumny tutaj powinno być tak, że najmniejsza kolumna powinna być pierwsza największa, ostatnia, jeśli rosnąco, bo nie wiem jak ustawiłaś, a dodanie to co ty masz na myśli.

**Anna Skupinska** 49:21  
Żółte na dole dlaczego?  
Eldo jestestwo to jest po to jest po nazwie produktu, więc to on teraz patrzę na nazwę produktu i alfabetycznie sortuję.

**Janusz Bossak** 49:43  
Dobra, to to jest co innego, a w tam w kolorach mamy też sortowanie, bo już już też.

**Damian Kaminski** 49:43  
No właśnie.  
Nie mamy.

**Anna Skupinska** 49:49  
Nie, nie mam.

**Damian Kaminski** 49:50  
To jest coś, co mówiliśmy, że.

**Anna Skupinska** 49:51  
To jest po prostu ona początku popiera po prostu ileś wartości 20 nie więcej i przydziela im kolory.

**Janusz Bossak** 49:52  
Dlatego jest Jestem sportu.

**Damian Kaminski** 49:56  
Poczekaj, poczekaj, poczekaj, poczekaj Janusz ma rację Anuluj to walił różne znaki tam po sortuj.

**Janusz Bossak** 50:02  
Różne znaki, sortowanie.

**Anna Skupinska** 50:03  
A tutaj co jest? Nie ma zastosowania to jest tylko to jest to jest tutaj nie Jestem prawda.

**Damian Kaminski** 50:04  
A tu jest tylko i tu trzeba dodać i tu trzeba dodać.

**Janusz Bossak** 50:08  
Pozycji. Kolor.  
Różne znaki.  
Sortowanie.

**Anna Skupinska** 50:12  
Choć.

**Damian Kaminski** 50:12  
3 kropki sortuj po.

**Anna Skupinska** 50:14  
Tutaj.

**Damian Kaminski** 50:16  
No.

**Janusz Bossak** 50:20  
Czyli coś tu jest nie tak?

**Damian Kaminski** 50:20  
Odśwież odśwież. Poczekajcie odśwież.  
Jest dobrze.

**Janusz Bossak** 50:26  
Jest dobrze no koło odwrotnie, no ale o k.

**Damian Kaminski** 50:27  
Jest dobrze.

**Anna Skupinska** 50:29  
Tak.

**Janusz Bossak** 50:30  
Teraz są małe na dole tak no i teraz na ciepło masz takie linijki.

**Damian Kaminski** 50:32  
Mhm.

**Janusz Bossak** 50:35  
Jedna druga od dołu, trzecia cieniutkie, tak w górkach też tam masz jakieś zielonkawą linijkę czy jakąś potem jest niebieskawa samym dole w marchii masz takim prawem będzie i tak.

**Damian Kaminski** 50:46  
No masz rację, tylko to zobaczysz dopiero jak przygotujesz raport.

**Janusz Bossak** 50:52  
No dobrze, ale czy mnie?  
No dobra, trzeba pogadać z Michałem.

**Damian Kaminski** 50:58  
O k no pogadajmy i weźmy dobre praktyki.

**Janusz Bossak** 51:00  
Nie wiemy robić wykresów, tak znaczy nie umiemy przygotowywać danych pod prezentację klientów.  
To jest nasz problem.  
I my próbujemy technicznie być poprawni, to znaczy, żeby wszystko pokazać.  
To nie jest do końca, jakby metodologia, otworzenie raporty.

**Anna Skupinska** 51:17  
Raczej jeżeli ktoś nie chce pokazywać małych rzeczy, to może wejść do jej warunek i na przykład, że wartość jest mniejsza, iż.

**Janusz Bossak** 51:21  
Ponadto nie o to chodzi.

**Damian Kaminski** 51:23  
Nie, ale to nie o to chodzi. Aniu, to znaczy może warto je pokazać, tylko zareagować? To jest te wyzwanie.

**Janusz Bossak** 51:30  
Tak znaczy, moja propozycja jest taka, że wszystko co jest na przykład poniżej tam nie wiem.  
Jednego no to już chyba zależy od wykresu tak, ale poniżej 5% to agreguje do łącznej jakiejś pozycji pozostałe i wtedy nie będzie potrzeba 30 kolorów, tylko może będzie potrzeba 10 kolorów, bo te 10 największych się pokaże.  
A cała reszta będzie jako pozostałe w jednym kolorem.

**Damian Kaminski** 51:56  
Janusz to był zgadzam pod kątem tworzenia. Tylko właśnie pytanie jest na ile my powinniśmy ingerować w to?

**Anna Skupinska** 51:57  
Tak dalej.

**Janusz Bossak** 52:03  
Słuchajcie, ja muszę liczyć, Przepraszam, Damian, ty też Kamil też, bo proszę, żebyście napisali mi czym się zajmujecie. Macie czas 5 minut na naszym kanale, chyba że napisaliście nie Łukasz tylko napisał, bo mam spotkanie z przemkiem, muszę mieć od was informacje jakimi tematami poza devem się zajmujecie, wsiadajcie tam i tak na def product delivery, ten pd m product delivery na tym kanale także tu musimy kończyć, bo ja mam za 10 minut wrzątkiem spotkaniem.

**Damian Kaminski** 52:05  
Mhm.  
Projektami, tak.

**Janusz Bossak** 52:33  
Przynieś od własną informację.

**Anna Skupinska** 52:34  
Rozumiem, czy ja Jestem jeszcze zajmie się wstrzymuje i będę go wrzucać i dopóki jak będzie już więcej Wiadomości to wtedy ja dokończę.

**Janusz Bossak** 52:43  
K.  
Na razie.

**Damian Kaminski** 52:46  
Cześć.

**Anna Skupinska** 52:47  
To cześć.

**Janusz Bossak** zatrzymano transkrypcję
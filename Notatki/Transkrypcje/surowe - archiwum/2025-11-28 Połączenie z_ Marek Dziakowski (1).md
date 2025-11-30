**Transkrypcja**

28 listopada 2025, 10:30AM

**Janusz Bossak** rozpoczęto transkrypcję

**Janusz Bossak** 0:03  
Przez skrzynkę jakby przez serwer pocztowy klienta.

**Marek Dziakowski** 0:05  
Tak.  
Tak żeby wychodziły jakby z domenę klienta, no technicznie jest to możliwe, bo bo tak samo działamy z turbo SMTP, czyli jakby my wysyłamy do nich oni to wysyłają dalej tylko, że no w turbo SMTP możemy sobie ustawić się jakby tą naszą nazwę i o k no a tutaj jakby klient musiałby, no dać nam dostępy, żebyśmy przyjmowali, jakby musiał przyjmować, by wszystkie maile, które od nas wychodzą, czyli nawet jeżeli nie wiem z jakiegoś tam względu.  
Nie powinien się zdarzyć, ale zdarzył się jakiś, nie wiem spam, bo coś się przycięło pójdzie 1000 maili. No to 1000 maili przejdzie przez skrzynkę przez ich serwer pocztowy i jakby 1000 maili wyjdzie od nich.  
To to jest jakby jedna taka rzecz, no inna rzecz, no to nie wiem też, czy chcemy tak z punktu handlowego, no sprzedawać, no jakby my wystawiamy te dokumenty, podpisujemy je też po swojej stronie, a one miałyby wychodzić, że od nich to też takie może.

**Janusz Bossak** 0:51  
Mam.

**Marek Dziakowski** 1:08  
Z poziomu handlowego niezbyt.  
Dobre.

**Janusz Bossak** 1:11  
Znaczy.  
Znaczy, nie, nie, nie widzę jakiegoś problemu tej z poziomu handlowego, no biznesowo chodzi prawdopodobnie o to, że są to niektórzy klienci. To też podnosili i tam myśmy pamiętam, robili jakieś mechanizmy nazwijmy to aliasów, że że to nie idzie, no że to nie idzie z kąta tam.  
A mody teraz senter com czy jakiegokolwiek ty?  
Tylko wygląda jakby szło od klienta i to już taka funkcjonalność jest więc pytanie o co im chodzi? Czy im chodzi o to, żeby to wyglądało, że to jak gdyby wychodzi od nich?  
Czy im chodzi o to, żeby fizycznie to szło przez ich serwery? No bo to są 2 różne rzeczy. Pierwszą mamy jakoś rozwiązaną, bo to było robione jeszcze tam chyba dla rossmana i tak dalej.  
No bo gdzie mi się zapalały żółte lampki, bo teraz Center to jest przecież nasza usługa i do tego obsługuje. Oczywiście wielu klientów tak, że wysyła Rossmann wysyła adecco, wysyła i tak dalej.

**Marek Dziakowski** 2:15  
Tak.

**Janusz Bossak** 2:19  
I co i nagle?  
Jakaś część tej wysyłki?  
Teraz Center miałby kierować przez serwer klienta przez serwer pocztowy klienta.

**Marek Dziakowski** 2:35  
No to swoją drogą, że trzeba by było to też programować to tak działało to dodatkowa komplikacja.

**Janusz Bossak** 2:42  
To taka całkiem spora tak, bo.

**Marek Dziakowski** 2:44  
No wszystkie maile wszystko co wychodzi od nas musiały być przerobione, że może wychodzić skąd, no nie, nie z domyślnego punktu.

**Janusz Bossak** 2:54  
No tak, tylko, że istnieje potencjalne.  
Ryzyko.  
Że no coś tam wyślemy, nie to co trzeba nie przez ich serwer na przykład pójdzie coś, co miało iść do innego klienta zupełnie.

**Marek Dziakowski** 3:09  
Mm.

**Janusz Bossak** 3:12  
Może niewielkie ryzyko, ale.

**Marek Dziakowski** 3:14  
No tak bardziej teoretyczne bym powiedział, ale no powiedzmy, że jest to jakieś dodatkowe pole, gdzie mogłoby coś takiego.  
Jakoś się zadziać nie wiem z jakiegoś tam względu pomyłki takiej czy innej, no jest takie ryzyko powiedzmy.  
Ee no to jedna kwestia, druga kwestia to też, że no teraz już nie nie moglibyśmy też jakby powiedzieć, że że gwarantujemy wirus tam procentach, że nasze maile, nasza usługa na pewno działa wychodzi. No bo powiedzmy, że serwer klienta pada, no i nagle będą o, a czemu mi maile nie przyszły, o czemu coś tam, a czemu coś tam?  
A dlaczego mailem i nie przychodzą i teraz będzie do nas ruch kierowany pewnie od PGO? Dlaczego nasze maile nie wyszły? No bo nie wiem. Wskaźnik spamu macie taki albo coś tam, to jest kolejne miejsce, gdzie musimy gdzieś tam reagować.

**Janusz Bossak** 4:01  
Tak.

**Marek Dziakowski** 4:04  
Także.

**Janusz Bossak** 4:04  
Znaczy mi się pomysł, że tak powiem ogólnie nie podoba.

**Marek Dziakowski** 4:07  
Mi też nie.

**Janusz Bossak** 4:08  
Nie, nie chciałbym tego realizować, szczerze mówiąc więc, albo to wyceniamy bardzo bardzo drogo.  
Tak, jeżeli w ogóle albo odpowiadałby, że to nie leży w naszym jakby interesie, tak.  
Żeby tak było.  
Ponieważ to jest zamknięta usługa, która coś robi tak i tutaj można wrócić do tego pierwszego tej pierwszej kwestii, czyli że my możemy.  
Personalizować.  
Yy no adres mailowy.  
To wiesz o tym, że tak można robić.

**Marek Dziakowski** 4:47  
No się nie wiedziałem.

**Janusz Bossak** 4:49  
No można jeszcze tak.

**Marek Dziakowski** 4:50  
To może to załatwi sprawę.

**Janusz Bossak** 4:53  
Tak znaczy, nie, nie pamiętam jak to się tam ustawia, ale chyba w ustawieniach organizacji, że.  
No nie pamiętam, dobra, nie chcę, nie chcę teraz zgadywać. Trzeba by pogrzebać w dokumentacji, ale na 100% tak było, bo taka deco ma tak, że właśnie podnoszone było to, że ci pracownicy tam czy kandydaci byli zdziwieni, że dostają jakiś tras Center w ogóle nie wiedzieli o co chodzi.

**Marek Dziakowski** 5:04  
Mhm.

**Janusz Bossak** 5:21  
A tak to dostają mail z adecco.

**Marek Dziakowski** 5:23  
A to nie chodziło a smsy?

**Janusz Bossak** 5:26  
Maile też.

**Marek Dziakowski** 5:27  
Wiele też.

**Janusz Bossak** 5:29  
Tak, tak, tak.

**Marek Dziakowski** 5:30  
Pamiętam, że smsy na pewno są z adecco, ale maile też były.

**Janusz Bossak** 5:35  
To trzeba to sprawdzić. Wydaje mi się, że to, że jest taka funkcjonalność, więc trzeba to.

**Marek Dziakowski** 5:35  
To sprawdzę, sprawdzę.

**Janusz Bossak** 5:40  
Yy ogarnąć, bo możliwe, że to jest wystarczające dla tego tematu.

**Marek Dziakowski** 5:47  
O k. Dobra. No to jeżeli jeżeli rzeczywiście tak jest no to no to tak tylko.

**Janusz Bossak** 5:50  
Za to na spokojnie to na spokojnie znaczy.

**Marek Dziakowski** 5:52  
Nie bardzo.

**Janusz Bossak** 5:55  
Kolejność tak jak ustaliliśmy iotova.  
Potem jak skończy się ten właz to się zajmij. Ty to cena nie jest taka pilna, że to musi być dzisiaj.

**Marek Dziakowski** 6:03  
Dobra.

**Janusz Bossak** 6:07  
Ja po prostu wczoraj zobaczyłem, że jest. No to przerzuciłem do ciebie, żeby nie zapomnieć.

**Marek Dziakowski** 6:07  
Tak.

**Janusz Bossak** 6:13  
Ale to jak zrobisz tam w poniedziałek czy wtorek jest o k.  
No i najpierw trzeba tam trochę tutaj mówiliśmy, pogrzebać, poszukać, bo wydaje mi się, że ta.  
Opcja na.  
Nazywania maila jakiś tam sposób takiego aliasu robienia jest zrobiona, że to to było robione nie pamiętam, ale.

**Marek Dziakowski** 6:33  
Dobra.  
Zerknę, to raczej nie jest jakoś głęboko Zakopane tutaj też jest ta druga kwestia, widzę, że tam już.  
No tam pisze tak tak my jest kwestia.

**Janusz Bossak** 6:44  
Ktoś wie, też była, chce tam pogadać.  
No to czekam na ciebie tutaj wciągniemy od razu no.

**Marek Dziakowski** 6:50  
Dobra dobra, to jest kwestia z symbolami, bo klient ponoć chce mieć możliwość, jakby też nie podzielić te jeszcze na dodatkowe kategorie, czyli nie tylko 4 tam jeszcze piąty poziom dodać pytanie, czy my to chcemy?  
Jakby w ramach tego rozwiązanie rva też wliczyć, czy to ma być jakoś tam rozwiązane? Nie wiem z poziomu już sama dieta.

**Janusz Bossak** 7:15  
Nie wiem, dobra Kamil, no to mieliśmy akurat chwilę na temat wyceny odnosi tam tras Center, ale widzę, że piszesz o tym motywowano to cię wciągnęliśmy, ponieważ mają to, żeby już od razu było i nagrywam jak zwykle to transkrypcje robimy, więc będziemy mieli notatnikiem.

**Kamil Dubaniowski** 7:25  
O k.  
Jestem.  
Jasne, tak nie wiem czy max żeby mnie chwilę też przed tym się spotkaliśmy. O to jutro była i temat jest taki, że nie nie wiem jak planować te porteczki, czyli chodzi o te nieruchomości już przysłowiowe tak czyli mamy nie wiem tam kontrolę przeciw pożarowe i robię sobie w tym katalogu järva pod teczkę na nieruchomość poloneza i na nieruchomość tam jakąś inną, tak i teraz czy te pod teczki mają być elementem struktury i otruła?  
Czyli odwoła, wskazuje ok. A pod Teczka w takim wypadku będzie po prostu czymś słownikiem.

**Janusz Bossak** 8:04  
Nie, nie.  
Czy?

**Kamil Dubaniowski** 8:12  
Rejestrem.

**Janusz Bossak** 8:13  
Nie.  
Nie to według mnie.  
Znaczy, nie Jestem tu ekspertem tak, ale z tego co ja tam wyczytałem co napisałem ten kompendium i później w tych przypadkach użycia.  
Różnych to.  
Działa to w ten sposób, że jeżeli masz.  
Temat właśnie no powiedzmy te nieruchomości zakładasz.  
Dla tej nieruchomości.  
I w tej teczce dla nieruchomości zakładasz pod teczki dla tych spraw?  
Bo normalna sytuacja jest taka, że zakładasz teczkę sprawy.  
Która ma cztero.  
Częściowy symbol i on przyczepiasz do klasy biothermu.  
Tu mówimy o sytuacji takiej, że.  
Tworzysz teczkę sprawy.  
Ona ma symbol cztero znakowy i w niej tworzysz pod teczkę sprawy.  
Którą na symbol 5 znakowe?

**Kamil Dubaniowski** 9:27  
Ok, to ja dobra to ja teraz od razu swoją jak ja to rozumiałem, ja to rozumiałem patrząc na te filmiki z z DR, że jest katalog i od riva.  
No nie wiem tam właśnie te wspomniane kontrole przeciwpożarowe.  
I Teraz ja mogę sobie zaplanować.  
W tym jakby podkatalog poloneza tam 90.  
I jakieś inne nieruchomości i Teraz ja do tych pod katalogów mogę wpinać teczki z praw dotyczące tych nieruchomości. Ja to tak rozumiem, czyli jest jakby może źle, ale tak tak gdzieś tam oglądając te filmiki, bo oni dodają te te ten element. Na tym nagraniu tuż pod klasę klasę jutro była, czyli kończą ci się klasy jutro była i oni tam mają normalnie Dodaj podkatalog czy pod teczkę jak to sobie tam nazywają no i to jest ten ten element, który ja myślałem, że jest elementem struktury właśnie tego i od riva, ale takim pomijanym w do  
Docelowym.  
Gdzieś tam nie wiem jak przekazują to już do archiwów państwowych, no to te te te porteczki to są tylko dla nich, żeby później łatwo znaleźć właśnie sprawy dotyczące tej konkretnej nieruchomości, ale to jest pod jakby nad sprawą, a ty to jakby rezerwujesz teraz, że to jest element pod sprawą.

**Janusz Bossak** 10:44  
Znaczy, nie chcę być tutaj wyrocznią, no bo kompletnie się na tym nie znam. To znaczy bazuje na tym co.  
Jakby prze tworzyłem umysłowo jeśli chodzi o to i przeszedłem tam różne.  
Jakby fazy rozumienia tego.  
Yy, istnieje coś takiego co jest jakby już poza.  
Właściwie metodyką JRA.  
A zwiąże się właśnie z tym, że robimy to elektronicznie, to jest to, że możesz sobie raport.  
Gotować.  
Na przykład wszystko, co dotyczy nieruchomości.  
Ale rejestrować w innych gałązkach jotter była przykład masz gałązkę jotter woła pokontrolne.  
I to nie są kontrole, tylko nieruchomości to są po prostu kontrole. On masz kontrolę zus, owską kontrolę nieruchomości i tak dalej i teraz jak założysz teczkę kontroli nieruchomości.  
To poza strukturą, jakby poza tą metodę oderwała możesz tam elektronicznie tak dodać symbol tej nieruchomości.  
I dla własnej wygody.  
Poza no wiesz, całym tym modelem interwał możesz sobie raportować teraz kontrolę dotyczący tej nieruchomości, jakieś tam badania techniczne dotyczące tej nieruchomości, zlecenie, remontu tej nieruchomości, ale samą tą sprawę tego remontu, tego badania i tak dalej może w różnych miejscach całej struktury i oto woła.  
Tam gdzie są badania tam gdzie są remonty tam gdzie coś.  
I to jest jedna jakby metoda.  
Czyli masz to rozproszone w różnych miejscach, ale ponieważ jest to w systemie elektronicznym, to jest łatwość zrobienia zestawienia.  
Danych dla danej nieruchomości. Ja to tak rozumiem i to jest poza metodyką druga.  
Metoda.  
Z wykorzystaniem tych pod teczek jest taka, że właśnie w katalogu nieruchomości zakładasz teczkę dla nieruchomości i w niej rejestru.  
Resztę pod teczki tej kontroli tego badania tego remontu nie już nie robisz tego gdzieś tam w strukturze.  
Tylko tutaj.  
Tak, czyli masz taki pudełko czy karton nieruchomości i w niej siedzą wszystkie jakieś kwestie związane z daną nieruchomością i wtedy nie siedzą gdzieś indziej.  
Ja tak rozumiem, tak gdzieś z tych rozporządzeń innych rzeczy wynika, że.  
To na sprawa może mieć tylko jedno miejsce.  
W.  
Ja też była.  
Czyli tak patrząc analogowo, czyli jak masz jakiś papier kartkę to może się wpiąć tylko w jedno miejsce to jednej teczki tak i teraz jest kwestia tego jak sobie to jakby zorganizujesz tak ja rozumiem, że są te 2 metody albo rozrzucasz to po.  
Yy różnych miejscach, gdzie są te kontrole, badania, remonty, jakieś inne rzeczy.  
I to jest fajne jak masz jedną siedzibę, już trzymamy się tych nieruchomości, ale to może dotyczyć innych tam jakiś zagadnień jak masz jeden taki podmiot, no to co za różnica gdzie to siedzi? Tak patrzę już kontrolę, no to tam były kontrole nie.  
Albo możesz to organizować właśnie przez te teczki.  
W ramach nieruchomości, które będą miały swoje pod teczki dla poszczególnych spraw i tyle ja tak to rozumiem, to jest moja wiedza na ten moment, czy ona jest właściwa? Nie wiem.  
Taka jest moja.  
Takie jest moje rozumienie tego zagadnienia, znaczy dobrze by było jakbyśmy w jakiegoś kurde eksperta.  
Yy się zapytali.  
Jakiegoś archiwisty.  
Nie teraz im się już nie domin. Necie był taki archiwistą pamiętam tam gdzie pracowałem.  
Tam się jego zapytam.  
Nie no, musielibyśmy mieć naprawdę jakiegoś.  
Albo trzeba zadzwonić do jakiejś archiwistów?  
Może ktoś nam poradzi, coś nie może do archiwum państwowego trzeba zadzwonić i się.  
Poprosić o ekspert.  
Poradę.  
Nie wiem, by się upewnić. Nie no bo.

**Kamil Dubaniowski** 15:29  
A jeszcze bo wiem, że te porteczki tydzień wyłapałeś w tej strukturze lotu.  
Pamiętam, że to było jaki to dokument, bo w tej oficjalnej strukturze co oni tam wpada się przesłali, no to się kończy na poziomie czwartym.  
A te porteczki to dziś było opisane, że oni używają czy.

**Janusz Bossak** 15:49  
Znaczy.  
To jest, jeżeli jest gdziekolwiek, to jest w tej kolumnie uwagi.  
Przy tej kategorii czy tej klasie?

**Kamil Dubaniowski** 15:58  
Czwartej no dobra, dobra, to jeszcze to przejrzę ok, żeby była to.

**Janusz Bossak** 16:02  
Tam uwagach powinno być napisane coś w stylu, że dla nieruchomości prowadzi się odrębne tam teczki dla nieruchomości coś takiego.

**Kamil Dubaniowski** 16:12  
Mhm.

**Janusz Bossak** 16:14  
Ja to sobie wiesz, wrzuciłem wszystko do tego.  
Do któregoś tam czata do jaśmina i chyba wszystkie te dokumenty nie.  
Jak jako chyba nawet do czata gp i tak jako projekt i się jego pytałem.  
To jest najlepsza rozwiązanie, bo tak to możesz nam się naczytać tego.  
Ja mam nawet tego czata, możemy go tutaj zaraz odpytać.  
Czy on będzie piti?  
Mam taki projekt lot to pokażą.  
I to jest część betty?  
O i tu mam jotter była lot.  
No i tu mam te podpięte pliki i teraz się możemy do nich pytać, tak?  
Czy?  
Czyli do.  
Mówię ci znika.  
Bo inaczej jak.  
Tak jak.  
Jak?  
Błąd.  
Zobaczymy co wymyśli coś sensownego.  
Zastaną książki, instrukcji, instrukcji archiwalne, że dokumentacja nieruchomości było się być klasyfikowana według kolacja, torba z grupy 68, gospodarka, gospodarowanie nieruchomościami lekarzy nieruchomości prowadzi się odrębną teczkę zgodnie z zasadą podziału na sprawy i klasy. Wewnątrz akt wykazu akt z teczki muszą być opisywane i przechowywane zgodnie z instrukcją kancelaryjną.  
Układach sygnatury, daty. Po zakończeniu sprawy akta trafiają po upływie 2 lat do archiwum zakładowego.  
Grupa 68. Gospodarowanie nieruchomościami.  
Najważniejszych klasy 680 wyjaśnienia, interpretacje, opinie, akty prawne gospodarowania, wiedza o nieruchomościach i aktualizacja.  
6 8 1 0 ewidencja nieruchomości 6, 8 1 1.  
Państwowy jak tworzy się teczki nieruchomości w nocy to jest Teczka nieruchomości to Teczka aktowa, w której gromadzi się dokumenty naszej jednej konkretnej nieruchomości w ramach danej sprawy lub zestawu spraw powiązanych tematycznie.  
Dokumenty były grupowane według symbolu takiego mateczki były układane w kolejności klasy va.  
Struktura i zawartość teczki nieruchomości, każda Teczka musi zawierać opis teczki pełna nazwę.  
Kategorie, tytuł, teczki 6 8 1 0 ewidencja nieruchomości nieruchomość przy ulicy w Warszawie.  
A czyli tutaj się robi to w ten sposób, tak?  
Akta sprawy w kolejności numerów spraw oraz technologicznie.  
Dokumenty własności, zakup, dokumenty prawne.  
Czy dla jednej nieruchomości jest jedna Teczka? Nie zawsze.  
Instrukcja kancelaryjna jasno wskazuje teczkę zakłada się dla spraw prowadzonych w ramach i jednej klasy otiva. Jeśli dokumentacja jest obszerna lub dotyczy wielu spraw, możliwe są teczki wydzielone, zbiorcze lub wielotomowe.  
W ogóle jakieś nowe pojęcia.  
W praktyce nieruchomości przy ulicy x może.  
Może mieć teczkę 68 10 ewidencja nieruchomości ulicy x.  
Czyli to widzisz, to jest trochę inaczej. Tak znowu masz teczkę 6, 8 2 3 zakup nieruchomości, czyli to nie jest jakby jedna Teczka nieruchomości.

**Kamil Dubaniowski** 20:26  
Tak no dla mnie to to jest właśnie ten cudzysłowie i też jak ja dyskutowałem z czatem to on mi to nazwał w ten sposób, że.

**Janusz Bossak** 20:27  
Tylko.

**Kamil Dubaniowski** 20:36  
Czasem określa się to jako sygnatury kancelaryjne symbol teczki, lokalne rozszerzenie i o rva lub pod teczki. To jest ten dodatkowy piąty poziom, czyli masz 6 8 10 to jest temat router va i teraz pod tym 6 8 10 możesz mieć ewidencje nieruchomości ulica x ewidencja nieruchomości ulica y.  
I wszystkie sprawy, które dotyczą ewidencji tej nieruchomości, a ich może być wiele, no po prostu wpinasz do tej teczki, czyli sprawy są w teczce, czyli jakby ta Teczka to jest dodatkowy poziomie tawuła nadrzędny nad sprawą.  
I i może się okazać, że zamykasz ewidencje nieruchomości xd bo już więcej tam spraw nie ma tak i tyle.  
I i jakby patrząc później na wszystkie sprawy w tych teczkach, czyli jeśli będziesz miał ewidencję nieruchomości XIY, to wszystkie te sprawy mimo tego, że są dla ciebie skatalogowane w dodatkowych katalogach. No jak później przekazuje się do archiwum, no to one mają ten symbol 6 8, 10, tak no, bo wszystkie dotyczą tego tematu ewidencji nieruchomości, a to, że ty sobie podzieliłeś sprawy na poszczególne nieruchomości. Dodatkowo to jest już twoje udogodnienie.

**Janusz Bossak** 21:45  
Ale to nie będzie ot 6 8 10 nie będzie tylko ewidencja nieruchomości x.  
Będziesz miał za chwilę 6 8 10 ewidencji nieruchomości igrek.

**Kamil Dubaniowski** 21:55  
Tak to mi chodzi.

**Janusz Bossak** 21:56  
Z dalej.

**Kamil Dubaniowski** 21:58  
No tak, ale to ewidencja nieruchomości. Ulica x to jest już ja rozumiem. Właśnie ta pod Teczka i w tej pod teczce możesz mieć różne sprawy, no bo była tam jakaś jedna sprawa dotycząca ewidencji. Przyszło 5 pism w tej sprawie po 2 miesiącach odpaliła się kolejna sprawa związana z ewidencją nieruchomości przy ulicy XI. Znowu to wpinasz jako nową sprawę. Tam będzie 10 innych dokumentów dotyczących tej ewidencji, ale wpada to w ten katalog ewidencji nieruchomości xd wchodzisz tam i widzisz wszystkie sprawy dotyczące ewidencji nieruchomości XAW każdej sprawie możesz mieć po ich z dokumentów.

**Janusz Bossak** 22:31  
Tak.  
No dobrze, ale jak chcesz teraz, gdybyś chciał przejrzeć historię nieruchomości x?  
To ona jest tutaj?

**Kamil Dubaniowski** 22:40  
Tak.

**Janusz Bossak** 22:41  
Tutaj, tutaj, tutaj i jeszcze pewnie w 15 innych miejscach nie i teraz.

**Kamil Dubaniowski** 22:41  
Tak.  
Tak.  
Tak.  
Tak jest.

**Janusz Bossak** 22:49  
To co mówiłem elektronicznie, to jest dość łatwe.  
Analogowo to jest tak, że w tytule jest tutaj adres i oczywiście możesz się pomylić, bo w tym tytule napiszesz.  
Polon nauka poloneza to jest łatwo tak, ale no ktoś się pomyli tak i jakoś tam z myślnikiem bez myślnika napiszę coś tam coś tam, bo to jest tylko tekst to nie jest żaden żadna symbolika, to jest tekst żeby człowiek umiał przeczytać, że to jest ewidencja nieruchomości poloneza 93 a i to jest ewidencja nieruchomości poloneza 93 elektronika wprowadza jeszcze dodatkową możliwość, że możemy mieć teczce symbol tej nieruchomości, którą wam modlicie, będziemy używać.  
I dzięki temu możesz teraz zrobić raport.  
Pokazujący wszystkie tematy związane z nieruchomością i on sobie wyszuka, żeby tu była jakaś sprawa w tej teczce według chronologii nawet tak będzie mógł to zrobić. To będzie miał daty.  
I że był najpierw zakup nieruchomości, potem było coś tam. Potem było tutaj podział, potem był najem, tam młode Werner, różne rzeczy się działy różnych tych.  
Teczkach, o których tutaj mówimy, czy w pod teczkach tych teczek, ale dzięki temu, że mamy to elektronicznie, to możemy to łatwo zebrać.

**Kamil Dubaniowski** 24:05  
Mhm.  
Dobra, to ja bym zapytał teraz z tego twojego, jeśli mam całą dokumentację, czy on może ty kojarzysz, czy są inne przykłady niż to nieruchomości, czy oni tak mają więcej? Bo jak to dotyczy tylko nieruchomości?  
No to to jest żaden problem, bo spodziewałem się, że mają tych nieruchomości skończoną ilość twój sposób wtedy byłby.  
Czymś, co spełni wymagania nawet lepiej. A a w ogóle nie musimy iść w te porteczki takie w rozumieniu jeter była no bo to po prostu będzie mam sprawę. No to muszę, jeśli wskazałem, że dotyczy nieruchomości, to muszę wskazać w dodatkowym polu jakiej nieruchomości i to już może być zwykły Słownik.  
Takie niemu nie muszę tego w żaden sposób gdzieś tam.

**Janusz Bossak** 24:48  
Jedna klasa równa się jedna też kaloryczną.  
Pod teczki sprawach kadrowych, no ale kadrowe to są osobne tematem.

**Kamil Dubaniowski** 24:54  
Mhm.

**Janusz Bossak** 24:58  
Do tyczki w komisjach i zespołach klasa trzecia komisja bhp protokołu 2024.  
No tak, no na każdej komisji no to dobrze, no to robisz komisja bhp, p. 2024 i w środek wpinasz.  
Tylko właśnie no dla mnie to jest komisja bhp, protokoły 2024 to jest.  
Teczka cztero.  
No.  
Zna kowa.  
W środku masz teczki pięcio znakowe.  
Związany z jakimiś sprawami tych komisji?  
Chyba, że ich tam nie ma dużo.  
Wtedy po prostu walisz wszystko, czyli bezpośrednio już tą naszą amo bitową sprawę wpinasz w tą teczkę tak i to nie jest wtedy.  
Ona nie jest ma struktury teczki i pod teczki.  
Tylko jeżeli będzie 50 spraw dotyczących protokołów BHP, to 50 spraw będzie w tej teczce. Komisja bhp protokoły 2024 i to jest Teczka sprawy.  
Tak i może już mieć drugą teczkę sprawy, która się nazywa też widzisz pod pod gałązką 0 0 3 nazywa się komisja rekrutacyjna postępowania 2024 i wtedy, jak masz dokument dotyczący komisji rekrutacyjnej, to wpinasz do tej teczki.  
I nie robisz pod teczek do tego nie.  
Natomiast ja tak rozumiem, że jeżeli to byłoby na tyle wewnątrz jeszcze tego złożone.  
Pomożesz o ile?  
Ta instrukcja kancelaryjna przewiduje.  
Zakładać pod teczki dla takiej teczki.  
Bo ja tak rozumiałem te porteczki dla nieruchomości, czyli jest jakaś.  
Nie tak jak oni tutaj napisali u nich jest tak nie.  
Gotując relacja między teczką nieruchomość. Problem właśnie to jest klucz do młodych piłkarzy. Dokument znajduje się wewnątrz sprawy, a modlitw tak, sprawa młodych jest jedyny.  
Jednym poziomem niżej niż Teczka i osterwa, ponieważ Teczka grupuje wiele spraw w jednej sprawie, a młody może znajdować się wiele dokumentów, konsekwencji, Teczka nieruchomości, to jest grupa spraw, a modlitwa o tym samym symbolu iotova przykład, sprawa amadi zakup działki idzie do klasy.  
6 8 2 3.  
Aktualizacja ewidencji działki idzie do klasy 6 8 10 to jest tutaj każda z tych spraw trafia po zakończeniu do swojej teczki i Other woła.  
Rekomendowana struktura teczek nieruchomości dla LOT u modlitwe, aby zachować zgodność pole symbolizował obowiązkowy w sprawach dotyczących nieruchomości pole, identyfikator. No właśnie to jest to nie nasz elektroniczny identyfikator nieruchomości, nie mający nic wspólnego.  
Z Piotrem byłam, to jest dodatkowe pole, nie?  
Na przykład numer księgi wieczystej, adres, identyfikator, jakiś wewnętrzny loty, automatyczne grupowanie spraw widokach właśnie to jest, ale widokach to jest właśnie to, co mówię, czyli wrzucasz do różnych tych.  
Kategorii czy klas?  
Ale widoku potem grupuje sobie nieruchomość poloneza 93. Tak i obojętnie gdzie ona tam siedzi, nie.  
Tak, czyli teczki nieruchomości w lot muszą być prowadzone w klasach 68 takich dla każdej nieruchomości prowadzi się odrębne teczki po jednej dla każdej klasy. Właśnie to jest to, to. To jest kluczowe zdanie.  
Bo.  
Ja byłem ciągle przekonany, że.  
Prowadzi się jedną teczkę dla nieruchomości.  
Ale to zobacz tu jest dla każdej nieruchomości prowadzi się odrębne teczki po jednej dla każdej klasy i o RA.  
Czyli generalnie jest wiele teczek nieruchomości.

**Kamil Dubaniowski** 29:21  
Tak no w zależności od klasy o r była tak może być Teczka właśnie w tej w tematach przeciwpożarowych może być Teczka.  
Tam nie wiem jakiś innych tematach kontroli no i.  
Dla każdej z tych klas i obserwowała tam, robisz teczkę nieruchomości.  
I zbierasz sprawy, które dotyczą tej klasy dla tej nieruchomości.

**Janusz Bossak** 29:53  
No dobrze no.  
To ja mam takie właśnie kompendium wiedzy. Tak no czerpie z tego tutaj mam zrobionego tego.  
Dane te dokumenty.  
I.  
Tutaj dodałem ten jednolite, rzeczowe wykazy, akt ten, no wszystkie te dokumenty z lotu, nie takie instrukcja i rozporządzenie, tylko tyle.  
I on na podstawie tego go tutaj, jak powiem odpytuje.  
Także tyle mogę powiedzieć.  
Nie wiem, no to jak powiedziałem, no nie Jestem jakby wyrocznią w tej sprawie, no bo nie mam żadnej praktyki, tak znaczy to są moje domysły na podstawie tutaj.  
Analizy takiej własnej analizy za pomocą tego.  
Czata.  
Ale jak to jest naprawdę tak, żeby mieć na 100% pewności, że trzeba się kogoś zapytać? No albo znaczy już mniej więcej wiemy, tylko może potwierdzić tak nawet zadając wprost pytanie w locie, jak oni to robią tej chwili tak.  
Jakoś robią nie papierową, chyba że nie prowadzą tego. Ja też byłam w ogóle nie mają zapisane, ale nie prowadzą.  
Lub.

**Kamil Dubaniowski** 31:12  
Ja jeszcze zanim zadamy to pytanie, podeślę wam żebyśmy czy byście wiedzieli na czym ja bazowałem to fragment nagrania z instrukcji kancelaryjnej jest tego jutro buławę z dr p jak oni to robią to jest w skrócie powiem wam bo tam więcej jest chyba 7 minut przed tym zrobiłam, który wam wyślę cały filmik omawiający jutro była to jest filmik który pokazuje jak zarządza się strukturą i obserwowała w tym z dr p. Czy to jest widok administratora który ma zadanie? Nie wiem wprowadzić nowy katalog nową klasę.  
Usunąć jakąś klasę i pokażę wam ten część dotyczącą pod teczek za chwilkę, ale to już podeślę po spotkaniu i najwyżej jak wyciągnie.  
Jest to jakieś nowe wnioski, to się złapiemy Jeszcze raz.  
Bo ja cały czas jednak nawet patrząc na to nagranie, rozumiem to tak, że te porteczki.  
Dodaje się jako element, jakby taki dodatkowy do struktury jutro właczy i to był trochę ten zakres Marka, a jak chcemy inaczej, że to będzie po prostu jakiś tam element wybieralny w polu typu. Nie wiem. Słownik Odnośnik do właśnie tej konkretnej nieruchomości czy czegokolwiek innego.  
No to też musimy to teraz chyba postanowić, żebyśmy to przekazali na wdrożenia, że tak będą musieli robić tak, że my kończymy toyotę reguła na poziomie czwartym. A jak do tego mają być jakieś tematycznie jeszcze prowadzone pod teczki, no to to już będzie. Nie wiem rejestry, Słownik, czy czy jakkolwiek inaczej to widzi.

**Janusz Bossak** 32:34  
Czy czy nie to to powinno być? Według mnie to powinna być to powinien być proces, który się tam załóżmy nazywa Teczka i o RWA.

**Kamil Dubaniowski** 32:43  
Mhm.

**Janusz Bossak** 32:44  
I on wtedy będzie miał ten czterooki znakowy symbol.  
I albo będzie osobny proces, który się będzie nazywał pod Teczka JRA, który będzie miał tą właściwość, że będzie nadawał pięcio, znakowe symbol.  
Albo jeżeli chcą bardziej komplikować sobie, no to to może być nadal ta sama Teczka i Other była tylko użyta.  
Jakby na poziomie, że wie, że jest w teczce i od Lwowa to już sama dostaje ten pięcio znakowy symbol. No więc pytanie takie wesz wdrożeniowe, która rozwiązanie jest łatwiejsze tak czy lepiej mieć 2 procesy? Jeden proces na pod teczki, drugi proces na teczki woła i odpowiednio do teczek lub pod teczek wpinać te nasze sprawy amo dietowe nie.

**Marek Dziakowski** 33:35  
Czyli wtedy każda sprawa w teczce musiałabym mieć ręcznie wybierany z tego pola, jaki ma symbol. Tak.

**Janusz Bossak** 33:45  
Znaczy każda sprawa tak znaczy.  
Na razie zapomnijmy na chwilę o pod teczkach, tak?

**Marek Dziakowski** 33:51  
Mhm.

**Kamil Dubaniowski** 33:52  
Czy januszem ja też, bo ja już trochę się tak na tą nomenklaturę jest, d przestawiłem Teczka to jest dla ciebie w rozumieniu SDD sprawa tak brzmi to dobrze rozumiał, bo sprawa w rozumieniu SD to jest zbiór dokumentów dotyczących jednego tematu. To jest sprawa i ty to nazywasz teczką.

**Janusz Bossak** 34:07  
Też.  
Bo to się tak nazywa, więc sprawa czy Teczka, no tak.

**Kamil Dubaniowski** 34:11  
Sprawa no oni to jakby tak czyli sprawa nie wiem, jest jakieś kontrole w nieruchomości i wokół tego było 10 pism różnych, tak, coś tam zostaliśmy straży pożarnej, coś tam dostaliśmy z sanepidu, coś tam dostaliśmy skądś tam i to jest jedna sprawa kontroli tej nieruchomości w jakimś tam temacie to jest teczkę.

**Janusz Bossak** 34:22  
Spk.  
Tak znaczy, ja tak nazwałem to teczką, żeby mieć konsultantom dać wyraźny sygnał, że to nie jest sprawa modi, Towar, żeby nie nie mylili sprawa modlitw owej ze sprawą jotter była tak, możemy to nazwać sprawą jotter była.

**Kamil Dubaniowski** 34:37  
Tak, sprawa jednak była, no i oni taką też nomenklaturę podali tam w opisie analizy sprawa amlogic sprawa jutro była, no bo niestety nieszczęśliwie to się nazywa sprawą.  
O k więc ja teraz trochę lepiej to rozumiem.  
O czym?

**Janusz Bossak** 34:52  
Teraz tą wracając do pytania Marka tą za sprawa i o RWA, czyli to co ja nazywam teczką i o RA to ta sprawa i o rva musi otrzymać znaczy musi być przypisana do klasy i o RA klasa iva to jest to co ty właśnie masz tam robić, czyli ten nasz taki Słownik tych, no te tych czterooki.  
Znakowy Słownik tak od zera, znaczy od jednego znaku do 4 znaków.  
Masz klasę i na końcu tej ostatnia klasa gdzieś tam każdej gałąź zcy ma wtedy przypisaną kategorię taki walną daty tam obowiązywania i będzie miała po naszej stronie również jakieś kwestie związane z uprawnieniami tak w locie może to będą mniej istotne, ale jednak.

**Marek Dziakowski** 35:39  
Czyli wykluczamy możliwość piątej kategorii, ewentualnie podziału.

**Janusz Bossak** 35:40  
No i.  
Nie ma to nie ma takiego czegoś znaczy.

**Marek Dziakowski** 35:45  
O k no czyli.

**Kamil Dubaniowski** 35:45  
No właśnie dobra i teraz teraz byśmy już rozumiał czym znaczy, jak już staliśmy to nazewnictwo, o czym ja mówiłem, bo według mnie może być ten piąty poziom i zaraz wam to pokażę na tym nagraniu i to jest właśnie ten poziom.  
Tak to jest kolejna taka podklasa, czyli masz järva. Tam 0, 0, 0, 7 i w ramach tego 0 0 0 7 możesz sobie zrobić? Nie wiem. 10 podklas i każda z tych podklas dotyczy jednej nieruchomości, czyli masz nieruchomość, a i teraz te nieruchomość, a możesz wpinać kolejne w tej Twojej nomenklaturze teczki sprawy i o RWA, czyli w ramach nieruchomości, a toczyła się w tym roku taka sprawa. Tam było 10 dokumentów toczyła się kolejna sprawa. Tam było 15 dokumentów, kolejna sprawa i ona wszystkie te sprawy dotyczyły tej klasy i od va.  
Tej nieruchomości i dopiero pod tą nieruchomością są sprawy, które jej dotyczyły. Ja tak rozumiem, to po tym nagraniu ze dr p. Czyli że tworzysz sobie taki dodatkowy.  
Nie wynikający już z instrukcji kancelaryjnej jest przepisów poziom w tym järva, żeby sprawy jotter buła toczące się w tej klasie już porządkować sobie tak po swojemu, żeby łatwo je później znaleźć. Wchodzisz w klasę 0, 0 7 i nie masz tam zbioru spraw i o RWA, które dotyczyły wszystkich nieruchomości, tylko masz te sprawy podzielone na poszczególne nieruchomości. Chodzisz sobie do środka i widzisz sprawy i od rva, które toczyły się w obrębie tej nieruchomości w tej klasie jutro wolne.  
I to też jest zaznaczone jasno, że później jak przekażę to do archiwum, to ich nie interesuje, że ty sobie to podzieliłeś. Dodatkowo dla swojego ułatwienia, żeby widzieć nieruchomości w tej klasie jako osobne masz przekazać to zgodnie z tym, jak sprawy były zakładane. Numeracja ma być spójna dla całej klasy iva, a to, że sobie to podzieliłeś na dodatkowe katalogi dodatkowe, takie podklasy, żeby widzieć, że te sprawy dotyczyły tej nieruchomości. To jest już twoje ułatwienie. Możesz, nie musisz tego robić.

**Janusz Bossak** 37:47  
Rozumiem znaczy.  
Wielokrotnie w różnych momentach dyskusji z tym czatem on podkreślał, że jotter była jest normatywny, podlega ustawie i rozporządzeniu i tu nie ma pola na własną interpretację, więc nie wiem, czy ten sposób, który podałeś, który w tym z d. Zrobili, czy on jest jakby prawnie dopuszczalny. Tak widocznie ktoś znalazł jakąś taką.  
Trochę lukę w moim przekonaniu.  
To ten piąty poziom to to i to jest w rozporządzeniu. To jest właśnie to, że możesz prowadzić teczki i pod teczki i to jest to to jakby to nie przykleja się do struktury do tych klas i o RWA, że to jest jakaś jeszcze podklasa.  
Tylko możesz prowadzić teczkę.  
W tej klasie.  
3 czy cztero znakowe i tak powiedzmy, że cztero, bo mówimy o tym, że jest jakiś piąty symbol. Jeszcze tak możesz prowadzić teczkę. Ta Teczka ma swój numer i teraz w ramach tej teczki możesz mieć te pod teczki, które są pięcio znakowe. W tym momencie teczki spraw tak sprawia sprawy i obserwowała taty. Ta sprawa znaczy, że są 2 poziomy sprawy i odwołanie, żeby już mówić nomenklatury.

**Kamil Dubaniowski** 38:56  
Spraw.  
Ja teraz.

**Janusz Bossak** 39:08  
Sprawę o niteczki tak, czyli dla klasy cztero smakowej zakładam sprawę i o TRWA dla nieruchomości.  
Poloneza 93.  
Określonej klasie iotova i koniec i teraz w ramach tej sprawy i o rva.  
Mogę zakładać i to oni właśnie używają nomenklatury pod teczki, bo tak jest w rozporządzeniu.  
Pod Teczka jest tak nazwane.  
Czyli taką pod sprawę i o rva.  
Zakładasz jakby te, no ja dlatego nazywam to teczką, no jest Teczka i pod Teczka Teczka i o rva a teraz pod Teczka JRA. Czy ta sprawa järva, która zawiera jakieś tam sprawy, a monitorowe nie, ale tych spraw tych teczek w tej teczce nieruchomości masz wiele.  
Jakaś powiedzmy to jest sprawa kontroli tak, czyli Teczka ta główna nazywa się kontrolę w na poloneza 93.  
No i masz tam kontrola kominiarska sprawa, kontrola budowlana sprawa.  
Sprawa ja też była pięcio smakowa, a w niej dokumenty na przykład pismo odnośnie kontroli, protokół tej kontroli, wezwanie do naprawienia czegoś tam i tak dalej. Ponowna kontrola jest to w ramach tej kontroli sprawa, inna sprawa, naprawa dachu na poloneza 93, nie coś tam i robisz tutaj kolejne rzeczy i dla mnie to są 2 poziomy naszej amo gitarowej.

**Kamil Dubaniowski** 40:47  
Sprał.

**Janusz Bossak** 40:48  
Sprawy w rozumieniu my ją sobie nazywamy, sprawą ją terriva, że ona reprezentuje ten poziom pierwszy i mamy drugi poziom. I tutaj właśnie mam wątpliwość, czy to powinno być to samo, czy to powinien być inny proces, ale ten drugi poziom ma pięcio znakowy symbol i dopiero do niego teraz dokładamy te nasze sprawy a modlitwe, a w 95 procentach innych gałązek iotova innych klas, bo mamy tylko sprawę tą 4 oznakowaną i do niej już dokładamy te sprawy.  
O mody.

**Marek Dziakowski** 41:24  
I teraz pytanie, w jaki sposób zrealizować tę platformę? Czy to ma być w ramach proc.

**Kamil Dubaniowski** 41:30  
Koncepcja Janusza wychodzi, to będzie proces, tak.

**Marek Dziakowski** 41:32  
Tak, czyli proces sprawy powiązane. Tak.

**Janusz Bossak** 41:35  
Ja bym tutaj znaczy inaczej, nawet gdyby było tak jak mówi Kamil, że można by tak zrobić, to nadal uważam, że to nie powinno być zapisywane w tej strukturze klasy oderwany.

**Marek Dziakowski** 41:51  
Bo tutaj, jeżeli chodzi o procesy pod procesy, no to też robi się pytanie.  
W jaki sposób te widoki, czyli, czyli raporty były różnicowane łatwiej jest zrobić na podstawie słownika i gdzieś tam wyciągnąć, potem filtrować to.  
Niż połączyć 2 procesy.

**Janusz Bossak** 42:14  
No nie wiem, no jeden proces.

**Marek Dziakowski** 42:17  
No jeżeli miały być pod folderem to wtedy by były 2.

**Janusz Bossak** 42:22  
No dlatego pod folderem jakoś nie wiem. No nie umiem się do odnieść, do tego nie umiem tego zrozumieć. Na razie nie wyobrażam sobie czy nie umiem sobie wyobrazić to jej struktury.

**Kamil Dubaniowski** 42:34  
Czekacie jeszcze?  
Prawda umożliwia dodanie pod teczki dla wybranej komórki organizacyjnej. Dzięki niej pracownicy komórki będą mogli dodawać szczegółowe zagadnienia do danej klasy. W pierwszej kolejności wskazujemy komórkę organizacyjną, następnie wprowadzamy nazwę pod teczki oraz wybieramy rok, w którym będzie obowiązywać. Zobaczcie, ona zeszła tutaj do poziomu mamy szóstkę, później 61 613 to jest klasa końcowa, czyli kończymy na trzeciej klasie.

**Marek Dziakowski** 42:36  
Tak, tak.

**Janusz Bossak** 42:37  
Tak.

**Marek Dziakowski** 43:02  
Mhm.

**Kamil Dubaniowski** 43:07  
Tu mogłaby być jeszcze klasa czwarta, na przykład 612. Ma jeszcze tam jakąś klasę czwartą i na tym kończy się jutro va i ona teraz dodaje pod teczkę, która dostaje symbol zakładane i pod teczki tam bit 613 kropka. Jeden to mogłaby być tam nieruchomość poloneza.  
I i to się robi z poziomu.

**Janusz Bossak** 43:23  
No i no ale jest to bit 613 kropka, jeden kropka rok.  
Za chwilę tam będzie tak, no.

**Kamil Dubaniowski** 43:29  
Tak.  
Pod teczki nie są przenoszone na kolejny rok, powinny one zostać.  
Być stworzone niezwłocznie po rozpoczęciu nowego roku, zanim pracownicy rozpoczną zakładanie spraw.  
Zapamiętaj system automatycznie wyświetli symbol dla zakładanej pod teczki, wskazując pierwszy wolny numer w danej klasie w ramach wybranej komórki organizacyjnej. Utworzenie pod potyczki potwierdzamy przyciskiem zapisz po utworzeniu pod teczki pojawi się ona na liście JRWA. Po jej zaznaczeniu dostępne są opcje edytuj i usuń. W trybie edycji można jedynie zmienić nazwę pod teczki funkcja usuń.  
Zatwierdza usunięcie pod teczki, przy czym system blokuje tę możliwość, jeśli w pod teczce zarejestrowano jakąkolwiek sprawę. Warto dodać, że zarządzanie JRWA można przydzielić wybranemu użytku.

**Janusz Bossak** 44:28  
No tak, no ale dla mnie to jest właśnie ten poziom.  
Znaczy to.  
Nie wiem.  
Znaczy to według mnie to jest?  
Abody ten poziom, który ona tu pokazała.  
To jest poziom audytowej teczki.

**Kamil Dubaniowski** 44:46  
Sprawy.

**Janusz Bossak** 44:47  
Sprawie o modlitewnej sprawy.

**Kamil Dubaniowski** 44:49  
Rejestrze, tak.  
Czy ok, no wiecie, to to o to mi chodziło, tak, żebyśmy podjęli tę decyzję, czy to jest kluczowa? To jest też ta informacja informacja, że pod teczki trzeba zakładać na każdy rok osobno nie są elementem przenosza walnym względem struktury, trwała więc to jest jak najbardziej argument za tym, żeby tego nie ładować w tą strukturę i odwoła, bo ona raczej jest stała niezmienna. Nawet uważamy, że nie trzeba jej kopiować tak jak oni tu sugerują. Z roku na rok, a te porteczki jak najbardziej, no trzeba zakładać na każdy rok osobno.

**Janusz Bossak** 44:52  
Manor.

**Kamil Dubaniowski** 45:22  
Bo może jakaś nieruchomości już.  
Nie jest nasza albo doszła nowa?

**Janusz Bossak** 45:26  
To jest to jest.  
To jest wiedza odmienna od mojej wiedzy.  
Tacy co ona powiedziała.  
Moja analiza wykazała, że.  
To co ona powiedziała jest nieprawdą, znaczy, że zakłada się te teczki dla tej nieruchomości raz i więcej się ich nie zakładam.  
Nie przenosi się z roku na rok, nie tworzy się może ten ez d tak ma.  
Ale nie ma takiej potrzeby prawnej.  
Wynikający z rozporządzenia.  
Jak już raz założyłeś tą nieruchomość?  
Piąteczkę.  
To wpinasz w środku pod teczki, które w tamtym roku na przykład dwudziestym czwartym miały numerek 24 na końcu, ale do tej samej teczki.  
Głównej.  
Wpinasz sprawy teraz w roku 2025.  
I ta Teczka jest jakby nie zamykana.  
No jest ciągnie się ten, ale mówię, no naprawdę pogadajmy z jakimś archiwistą, bo.  
Nasza wiedza wynikająca z gadania sztuczną inteligencją może nas zaprowadzić na manowce, no po prostu.

**Kamil Dubaniowski** 46:45  
Ale znaczy wiecie, dobra, to zróbmy tak, robimy cztero poziomu struktury, bo robimy teraz jak dojdzie, że te porteczki i są nieoptymalne. Nie, nie, nie chcemy robić ich przez rejestr, to zrobimy po prostu i tak no tabelę tak, która będzie miała.  
Link tak do do rodzica.

**Janusz Bossak** 47:05  
To znaczy.

**Kamil Dubaniowski** 47:07  
Tyle.

**Janusz Bossak** 47:14  
No pokaż takim taki moment, gdzie nie jest mowa o pod teczkach tylko zakładaniu teczki w takich kategoriach w których się zakłada teczki.

**Kamil Dubaniowski** 47:24  
Teczkę w sensie w rozumieniu sprawy trwała.

**Janusz Bossak** 47:26  
Sprawa jest.  
Już tak się przyzwyczaiłem w głowie, że to są teczki, żeby.  
Wciąga tam ciągle, że to są teczki.  
Przepraszam, ale dostałem krosa i muszę zjeść.

**Marek Dziakowski** 47:42  
Takie zakładanie drugiej tabeli nie będzie zbyt wydajne, ale trzeba będzie łączyć wyniki z 2 tabel.

**Kamil Dubaniowski** 47:54  
Zacznijmy od zakładanej na konkretnym piśmie, ale tworzonej po to, by kompletować dokumenty, które można będzie identyfikować po wspólnym znaku sprawy. W tym celu klikamy przycisk załóż sprawę znajdujący się na ekranie startowym.  
Wyświetli się okno, w którym należy podać tytuł zakładanej sprawy oraz wskazać jej klasę z jednolitego, rzeczowego wykazu akt. W skrócie JRWA zawiera on między innymi informacje o tym.

**Janusz Bossak** 48:17  
I teraz zatrzymaj.  
I to to co teraz to się będzie działo, to jest to, co Marek będzie w tym naszym.  
Polu typ Odnośnik to jest dokładnie ten moment, no jedziemy.

**Kamil Dubaniowski** 48:27  
Podnośnik.  
W jaki sposób będziesz prowadzić sprawę papierową czy elektronicznie oraz jaka jest jej kwalifikacja archiwalna w systemie ezd RP możesz wybrać odpowiednią klasę, wpisując jej symbol hasło lub ich fragment. Jeśli to zrobisz, zostaną wyświetlone pasujące pozycje. Wybieramy odpowiednią z listy. Jeśli nie znasz numeru lub nie wiesz, jak klasa została nazwana, możesz rozwinąć drzewo i o RWA, który jest podzielone na klasy rzeczowe.

**Janusz Bossak** 48:49  
To jest dokładnie to.  
No tego nie mamy tych.

**Kamil Dubaniowski** 49:02  
Jak zobaczcie, że tu się da w ogóle zmieniać schematy.  
Nie wiem, to jest ten cały czas konflikt, który mamy, że u nich te schematy można importować i wręcz oni deklarują to, co przed chwilą padło, że schematy powinno się z roku na rok kopiować, utworzyć nowe, właściwie tak zamykać poprzedni i otwierać nowych. Tu jest wybór schematu, a tu dopiero jest.  
System wyświetli numer sprawy roki i założenia kategorię archiwalną oraz cały znak sprawy.  
Po sprawdzeniu tych danych klikamy przycisk zapisz.  
System przeniesie nas automatycznie do widoku sprawy. Zobacz, tak wygląda sprawa prowadzona papierowo zwana.

**Janusz Bossak** 49:41  
No i proste.  
No i teraz. Zobacz ten numer dk z raz 2 3 4, tak.  
4 części.  
I powiedz mi, czym to się różni?  
Ten numer od tego, co pokazywała ta pani tam chwilę wcześniej tak, czyli miał oczywiście, że nie.

**Kamil Dubaniowski** 50:01  
Nie miał, nie miał roku.

**Marek Dziakowski** 50:04  
Miał rok.

**Kamil Dubaniowski** 50:05  
Miał też znaczy miał do podania, ale w numeracji tam nie widziałem, żeby się zapytać, to tak.

**Marek Dziakowski** 50:06  
Tak.  
Było było po zapisaniu się dopiero pojawił, tak?

**Kamil Dubaniowski** 50:10  
O k.

**Janusz Bossak** 50:12  
To jest ten poziom.  
I teraz według mnie, jeżeli tak założysz teczkę sprawę.  
To może ci przyjść na myśl?  
Że jednak założysz pod sprawy do tej sprawy.  
I według mnie to.  
Tamten sposób i ten sposób w mojej głowie to jest tożsame.  
Bo efekt końcowy to jest ten taki sam obiekt.  
W naszym rozumieniu, a modlitwa owym to będzie proces pod tytułem tam sprawa i o RWA.  
I tu zostanie otworzone tak jak on pokazał ten człowiek, bo teraz mężczyzna mówił tak, a przedtem na tym drugim filmiku pani mówiłam i pokazała zakładanie teczki dla nieruchomości. W moim przekonaniu powstanie dokładnie taki sam obiekt.  
Sprawa jest reguła.  
Takie jest moje rozumienie tego, nie?

**Kamil Dubaniowski** 51:14  
Ok.  
Tyle tak to wtedy spada to na konsultantów. Może to być jeden proces.  
Właściwie jak zakładasz nową sprawę?  
To będzie pole do potencjalnie wskazania sprawy nadrzędnej.  
Tą sprawę w rozumieniu je tak woła, czyli zakładam sprawę i tak woła uznaje, że to jest taka nadrzędna, która będzie kumulowała w sobie sprawę i oderwała dotyczące tej nieruchomości.  
No więc jak będę później zakładał sprawę dotyczącą tej nieruchomości, no to będę musiał sprawę w sprawę nadrzędną nieruchomości, wskazania.

**Janusz Bossak** 51:50  
Dokładnie, my możemy sobie zrobić niezależnie to, że masz tam jakiś pole typu.  
Identyfikator nieruchomości i po prostu w sprawach.  
Tych bioder była, ale no sprawach rozumieniu a modelowych.  
Będziesz wskazywał tą nieruchomość, no i tyle i potem możesz sobie robić raport, co już jest, nie ma nic wspólnego z lotr była tak po prostu możesz raportować o po tej nieruchomości, gdziekolwiek w jakiejkolwiek sprawie ta nieruchomość występuje.  
Bo.  
No właśnie jedną rzecz.  
To to jest dla mnie ciągle zagadką, że jeżeli w tych różnych klasach.  
To jak tutaj ten czat nam przed chwilą pokazywał.  
Zakładam, mam 5 albo 10 nieruchomości, to co muszę bardzo się pilnować.  
Żeby w klasie tam 0 6 80.  
Moja nieruchomość poloneza 93 była pod numerkiem jeden i w klasie.  
0 6 81 też, żeby była pod numerkiem jeden.  
I w klasie jeszcze jakieś też pod numerkiem jeden.  
Co może być trudne do utrzymania?  
No muszę dokładnie w takiej kolejności zakładać w każdej z tych klas i pamiętać, że tam założyłem trzecią. A jak rozumiesz nie.  
Więc.  
Żeby to było łatwiejsze w moim przekonaniu, to sobie można założyć tą nieruchomość. Poloneza 93 pod numerkiem jeden w klasie tam 0 6 80.  
I mieć symbol już na naszym nowym formularzu, że to jest nieruchomość poloneza 93.  
A w innej klasie tam 0 6 81 założyć tą teczkę na poloneza 93 pod numerkiem 2 czy 3 czy 5. No bo akurat.  
Tak złożyli. Tak się złożyło, że w takiej kolejności było zrobione, ale ona będzie oznaczona też polem na formularzu poloneza 93 i wtedy będzie ci łatwo to kompletować, bo tak to oprócz nazwy w tytule nie wie, że to dotyczy poloneza 93.  
To byłby jedyny jakby wspólny.  
Wspólny element tak kawałek nazwy, której też może się pomylić, bo jest zwykłym tekstem.

**Kamil Dubaniowski** 54:26  
Ja wiem.

**Janusz Bossak** 54:26  
Papierowo to działa, ale tak elektronicznie słabo nie.

**Kamil Dubaniowski** 54:29  
Mhm.  
Potencjalnie tak patrząc na to to moim rozumieniu, jeśli są klasy i otiva, czyli ten nasz trzeci czwarty poziom.  
Które?  
Od uzna, że wymagają dodatkowego przyporządkowania do jakiegoś właśnie obiektu. Nie wiem elementu.  
Może po stronie tego nasze naszej klasy router była powinien być tylko taki czek.  
Że tam wymagane przyporządkowanie dla konsultantów, żeby oni mogli wali dodać, że jeśli wpinasz coś do tej klasy.  
No to jest zasada, że w dodatkowym polu musisz jeszcze coś wybrać, czyli właśnie ten obiekt, czy czy cokolwiek innego, żeby oni mogli wtedy pokazać to pole dynamicznie jako obligatoryjne, że teraz przepis jeszcze obiekt jak tam nieruchomości, cokolwiek innego, żeby jakby wyspecjalizować te klasy, które lot wymaga, że żeby przyporządkować dodatkowo.  
Ale.

**Janusz Bossak** 55:26  
Tak.

**Kamil Dubaniowski** 55:28  
Bo to tak naprawdę wtedy mógłby być najprostszy Słownik nieruchomości i tyle wybierasz klasę, zakładasz nową sprawę i rva i wskazujesz do jakiej klasy tam, że dotyczy to kontroli, a dodatkowo w polu obok. Wybierasz ze słownika tą nieruchomość i tyle i później po tym możesz sobie właśnie pogrupować jakiś raport czy filtrować tak po tej konkretnej nieruchomości zobaczyć wszystkie sprawy i obserwowała, które tej nieruchomości dotyczy.

**Janusz Bossak** 55:54  
Dokładnie tak.

**Kamil Dubaniowski** 55:54  
I to nawet nie musi być ten poziom jeszcze wyżej, że musisz założyć sprawę.  
Nadrzędną jutro była i później w niej zakładać sprawy podrzędnej jutro, bo nie jest jeden poziom spraw i o RWA, ale niektóre ze spraw i o RA mogą mieć dodatkową klasyfikację. Właśnie podział na te nieruchomości czy czy co tam jeszcze sobie dzieli lot.

**Janusz Bossak** 56:13  
Tak znaczy, ja mam takie wrażenie, że ten program tutaj ten z d. On został zrobiony przez archiwisty papierowego.  
Tak.  
I żeby innym archiwistą papierowym to było dla nich zrozumiałe, no to ona odzwierciedla tak naprawdę logikę papierową.  
A logika elektroniczna jest inna?  
Nie wiem na ile rozporządzenie jakby.  
Tego też aż tak bardzo nie analizowałem wpr.  
Władza zasady elektronicznej.  
Elektronicznego prowadzenia tego JRA. No bo pamiętasz, że jak rozmawialiśmy o teczkach pracowniczych, to to była dość spora różnica?  
Pomiędzy prowadzeniem w postaci papierowej, a prowadzeniem w postaci elektronicznej.  
Chociażby numeracja.  
Zupełnie inaczej jest podejście w tej numeracji elektronicznej niż tutaj, więc tu jesteśmy takim stanie hybrydy jakiejś takiej nie trochę taki trochę takiej i to, co powiedziałaś tu przed chwilą, to tak, no werek tronic nie tak jest. Najlepiej byłoby w ogóle nie zakładać tych pod teczek, tylko zakładać teczki.  
I oznaczać w środku, że to dotyczy tej czy tamtej nieruchomości konieczne.  
Mi się tym nie przejmować, nie znaczy. Chodzi mi o to, że można prowadzić te dokumenty prościej.

**Kamil Dubaniowski** 57:44  
Tak.

**Janusz Bossak** 57:46  
Dzięki temu, że to jest robione elektronicznie, a potem troszkę już poza modelem joker wła sobie robić raporty, tak.  
Przypomniałaś mi, żebym nie zapomniał, bo chcę to wypowiedzieć też do.  
Później notatki jest jeszcze jeden temat, który musimy zaopiekować.  
Który się nie tylko dotyczy tej kwestii, ale innych to są raportowanie z pól typu Odnośnik.  
Czyli że jak tak jak teraz możemy raportować z tabelki, czyli wybieram sobie tabelkę i mogę wybrać.  
Kolumny z tej tabelki.  
To to samo musi dotyczyć pola Odnośnik, czyli jak wybiorę, wybiorę pole, Odnośnik, że chcę, żeby się pojawiło na.  
Raporcie, to powinienem móc wybrać pola z tego procesu.  
Na które wskazuje to pole Odnośnik.  
Rozumiecie?

**Kamil Dubaniowski** 58:48  
Tak no wtedy by nie trzeba było kopiować tych danych na pojedyncze dokumenty.

**Janusz Bossak** 58:52  
Dokładnie.  
I to według mnie, to powinniśmy wpisać w ten projekt.  
I przy okazji tego jotter była to zrobić, bo to się pojawia bardzo często, nawet ostatnio też Mateusz kołakowski o tym mówił.  
Yy, to jest uproszczenie. Bardzo dużo uproszczenie tworzenia raportów, no.

**Kamil Dubaniowski** 59:09  
Tylko, że te tym kontekście będzie odnosił do źródła zewnętrznego, więc jeszcze trochę inaczej.

**Janusz Bossak** 59:15  
No nie, bo będziesz miał akta.

**Kamil Dubaniowski** 59:17  
A sprawa sprawa ok. Na aktach na sprawę przekopujemy dane z była tak a tam rozumiem.

**Janusz Bossak** 59:23  
Sprawa była i te sprawy a nie.  
Jest to powiązanie ten poziom.  
I wtedy, jak będziesz chciał raportować ze sprawy i o RWA, żebyśmy mógł pokazać.  
Te elementy ze tych spraw?  
A modowych nie.  
Także to też trzeba będzie taką rzecz zaopiekować. No dobra, słuchajcie, bo tam mieliśmy chyba mieć jakiś tej chwili już.

**Kamil Dubaniowski** 59:51  
3 nas dwunasta, tak trzynaste.

**Janusz Bossak** 59:55  
Jest tak od pół godziny planowanie sprintu nam ciebie.

**Kamil Dubaniowski** 59:57  
Planowanie dobra, dobra to Marek dla ciebie jasne, tak cztero poziomowe jutro była i na tym kończy.

**Marek Dziakowski** 1:00:02  
Tak, tak.

**Janusz Bossak** 1:00:04  
Teraz tutaj ci przygotuję z tego notatkę, jak się tylko wygeneruje, to ci dam.

**Marek Dziakowski** 1:00:05  
Tak.  
O k no to to to część rozumiem, no tam reszta jak będę się jakieś pytanie pojawiały już co do samego pola i użytkowaniu na to.

**Kamil Dubaniowski** 1:00:17  
Tam też widzieliście, że oni mają dwo widoki później jak wybierasz katalogu jutro była to możesz po prostu takim polem, a możesz też zobaczyć całe drzewo.

**Marek Dziakowski** 1:00:17  
Później.

**Kamil Dubaniowski** 1:00:26  
I spodziewam się, że w kolejnym nie w tym m wi w kolejnym kroku mogą na nas to wymusić, bo lot po prostu ludzie nie znają struktury jutro była, bo jak się okazało wspominałem wczoraj, oni dopiero zaczynają z tym pracować, więc takie drzewo będzie dla nich spodziewał się wygodniejsze. Taka lista wyboru, gdzie wpisujesz symbol i my podpowiadamy, jest dla kogoś, który pewnie trochę z tym popracował, wie jakiej klasy obsługuje i zna je na pamięć już, a przy pierwszych takich klasyfikacjach to oni będą mieli pewnie problem, będą chcieli widzieć całe drzewo.  
Ale dobra to jeszcze będziemy.

**Janusz Bossak** 1:00:57  
Ale to później dobra, dzięki bardzo.

**Janusz Bossak** zatrzymano transkrypcję
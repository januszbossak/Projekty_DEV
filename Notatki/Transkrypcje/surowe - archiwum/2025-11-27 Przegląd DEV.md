**Transkrypcja**

27 listopada 2025, 10:10AM

**Janusz Bossak** rozpoczęto transkrypcję

**Przemysław Sołdacki** 0:03  
Jedną rzecz jak my wyłączymy ton kasuję.  
Wiesz, go wyłączy, ale dobra, no słuchaj, no to włącz tak, ja sobie wymianę rzeczy, które chcesz.  
Więc.  
To, żeby dało się może to napiszę wizard do eksport.  
Tu i.  
Do importu i to co mi się wydaje, że jest potrzebne, ale to naciskiem na. Wydaje mi się, że mogę sobie wybrać rasę wyeksportować.  
Czyli które procesy, czy wszystkie czy pojedyncze, czyli nie wybrane i czy chce do tego, jeśli jest, a raport znaczy proces jest proces i go chce sobie.  
Eksportować on ma powiązane rzeczy typu rejestr słonik to żeby mógł sobie teraz znaczyć, pociągnie mi też te raporty. Pociągnij mi też te te, nie wiem, słowniki tam cokolwiek.  
Yy i żeby to tak by pokazywało kompleksowo tak, no jak eksportuje tą grę kliknąć wrzuć mi wszystko i przynieś mi się wszystko, albo mogę wybrać niektóre rzeczy i podczas importu to samo.

**Janusz Bossak** 1:22  
Czy ja mam?  
Długiego czasu takie przeczucie, że to powinno być zupełnie inaczej. Znaczy kiedyś z Piotrem rozmawiałem, ale jakoś odrzucił tą myśl w którymś momencie, ale powiem ci o co chodzi.  
Ja musiał wylać.  
Terminować proces eksportowania rzeczy na środowisku testowym.  
Tylko wyobrażam sobie w ten sposób, że wchodzę na środowisko załóżmy produkcyjny, na które chce przenieść te zmiany.  
I w jakiś sposób wskazuje, że moje zmiany są na środowisku testowym tym.  
I poprzez api tam się dobieram.

**Przemysław Sołdacki** 2:01  
Miasto nie przejdzie, to te środowiska się nie widzą, bardzo często się nie widzą. One są na innych serwerach, na innych sieciach mogą się nie widzieć. Poza tym wtedy, byśmy stracili taką rzecz jak możliwość sprawdzenia, co de facto tam było w tych plikach takiego śledzenia tych. Wiesz, więc ja bym ja bym zostawił, że to idzie poprzez piki. To może tak, że ktoś eksportuje, przenosi przez jakiś tam mechanizmy logując się na inne jakieś tam terminale do drugiego środowiska wgrywa i sobie importuje.

**Janusz Bossak** 2:03  
No właśnie.  
No właśnie.

**Przemysław Sołdacki** 2:32  
Tylko to ja bym tutaj napisał eksport.  
Powiązań.  
Powiązanych klientów.  
W takim razie tak ogólnie i.  
Sługa wpis.

**Janusz Bossak** 2:54  
Tak, bo wtedy musi pociągnąć nasze, no tak jak tam te rozmowy w tym.  
Sprawdzaniu zależności tak, że istnieją.  
Na przykład inne procesy.  
Które są wykorzystywane w polach Odnośnik.

**Przemysław Sołdacki** 3:10  
I to właśnie o to chodzi, że jak że wtedy mi pokazuje co co tam jest powiązane i mogę sobie czek boksem, znaczy, że to też mnie importuj, skoro już.  
Będzie.  
Ładnie to coś, co jest zmian, ale ładnie mi się podobaja, nagle wchodzę, patrzę o fajne.  
Dużo takich jest tam zależności po i tak jakby się to pojawią. Te zależności pewnie za chwilę teraz się wczytuję pewne ustawienia form sowej się długo ładują.  
W ogóle, bo takie ramki doszły do tych guzików.

**Janusz Bossak** 3:48  
No a to jest przypadek. Już usunęliśmy to, ale się nie.

**Przemysław Sołdacki** 3:50  
Tak to nawet ładne.

**Janusz Bossak** 3:53  
Niestety poszło do jednego z klientów i mu się spodobało. O jakie pan?

**Przemysław Sołdacki** 3:57  
Ale mi też się spodobało. To fajne jest.

**Janusz Bossak** 3:59  
Ale to znaczy to, by biblioteka and design została zaktualizowana i coś tam monitor dodali. No nie może tak być, że po aktualizacji biblioteki and design nam się zmieniają style, no, no nie.

**Przemysław Sołdacki** 4:12  
Ale znaczy.  
Czekaj, jeszcze się od tworzę tutaj?

**Janusz Bossak** 4:16  
Tak, bo w jednym miejscu jest w innych, nie ma więc.

**Przemysław Sołdacki** 4:19  
Może nie, bo bo tu jak wszedłem na te procesy, jak tu najeżdżam i że one są w takich rameczkę no fajnie wygląda. No ale dobra, może nie może przypadkowych ruchów. Zobacz jak mam powiązania i widzę, że tu mam powiązania. Obserwatorzy to, że sobie mogę nie wiem zaznaczyć checkbox także to też tak tutaj widzę, że to też tak, że mogę sobie wybrać, bo tutaj ja rozumiem, mógłby być jakiś powiązane raporty, wsadzone raporty takiej, jeśli są.  
Bo tutaj mam brak, brak brak, ale podczas eksportu to tam gdzie brak to mi się nie pojawia tylko te rzeczy, które które są i wtedy mogę odchodzić jak boksami też, żeby wrzucić i później po prostu importu to samo. Widzę, że w pliku są jakieś tam rzeczy mówię to to i to mi wrzucić, a resztę nie wrzucę.  
Więc to to jest?

**Janusz Bossak** 5:07  
Znaczy no.  
Problem jest, że tak powiem rozgałęzień jakby kolejnych warstw tego przenoszenia tak no bo tak jak to powiedzieliśmy o tych i to chyba jest najtrudniejszy element tego wszystkiego. Tak jest jakiś proces, który zależy od jakiegoś rejestru poprzez pole Odnośnik. No i o Ki teraz tamten rejestr.  
Też może mieć kolejne inne odnośniki do jeszcze innych rzeczy, nie i ogólnie rzecz biorąc nie wiadomo jak głęboko to sięga, nie.

**Przemysław Sołdacki** 5:36  
No tak.  
No ale to jest, no to można to jakoś ograniczyć, no bo wiesz jakby nie jeśli no bo za chwilę to by się okazało, że tam wszystko ze wszystkim jest powiązane, ale jakby taka ta naturalna hierarchia, że jest proces pod procesem mogą być podpięte.  
A nie wiem głupoty, słowniki i a jeśli jest proces no to jakby mam tylko informację, że jest proces, ale już jakby mi ty się dalej w głąb to drzewko nie jedzie, tylko będę ostrzeżenie, że że tutaj.  
Oddzielnie na liście procesów jest ten proces, że może też bym chciał go jakoś można zaznaczyć, ale wiesz, ja na razie nie projektujemy tego, tylko chodzi mi o to, że ogólniej da taka, że wybieram swoje, eksportuje i wybieram się importuje. Mogę, jakby nie muszę pojedynczą. Ja chcę całą paczkę, no bo wiem, że proces związany jest. Nie wiem z 5 raportami i 2 słownikami to go eksportuje w całości importuje i tu jest problem nadpisywania i to jest, musi być dobrze ogarnięte, tak, że na przykład to już mam Słownik i i już go na produkcji zmieniam i nie chcę, żeby mi się domyślnie nie wiem pozamieniał.  
Bo na testach jest inny.  
Więc to jest jakbyś świadomy wybór tak tego nadpisywanie, no jakby to to jest tyle dobra, ale to może jedźmy, jedźmy dalej, co tu mamy?

**Janusz Bossak** 6:42  
No tak no.

**Przemysław Sołdacki** 6:52  
Bo to jest, zakładam, że to może pomóc mocno naszym wdrożeń owcom serwisantem, więc jakby oni o to prosili, więc to jest tutaj dokończenie.  
Oj.  
I wydaje mi się, że to jest uważnie, jakby tutaj celem biznesowym z mojego punktu widzenia jest najważniejsze jest to.  
Że jakby że nica szukać, że patrzę dlaczego mi się pole zmienia, no to tam powinniśmy się zmieniać, bo nie wiem, jest reguła, albo na przykład pole znika, bo jest reguła. Wiem, która jej szukać, no bo teraz patrzeć znika. A może jest może jest ten, nie wiem highfield, no to wchodzę reguły szukam po nazwie pola szukam, czytam nie sehel, a o k jakby to się da zrobić, ale jakby muszę się naszukać, a my i tak te informacje mamy w bazie.  
Z tego co wiem.  
Więc.

**Janusz Bossak** 7:47  
Do pewnego stopnia tak szczególnych przypadków nie ma, no bo wtedy kiedy sobie nazwę pola zapisz do zmiennej, potem będziesz chciał to używał, ale mówię, to są takie przypadki.

**Przemysław Sołdacki** 7:57  
Ale to jest, nie wiem 5% przypadków, że ktoś tak zrobił, więc wiesz, jak mnie znajdzie, to nie znajdzie. No to trudno, to sobie będzie dalej drążył temat, ale zwykle po prostu znajdziemy, pokażę, jest, jest szybciej. Dobra historia edycji procesu.  
O k. Jest to zrozumiałe i to ten ku jeden ważny jest dobrze rozpisany, bardziej mnie interesuje jakby.  
To co jest dalej i przynajmniej na takim ogólnym poziomie?  
Poprawki w module raport owym.  
No tak tam jest wprost puszka pandory.

**Janusz Bossak** 8:30  
Znaczy ja bym to nie żeby tak klienta to trzeba napisać jakiejś stabilizacji, a czy tam usprawnienia w module raportowanym, że jak poprawki to wiadomo, że są błędy.

**Przemysław Sołdacki** 8:41  
Ale weź klient, który używa to wiesz, że tam są błędy, ale to jest okej, jakby zrozumiałe o co chodzi.  
No nie wiem czy to dalej spisywać, no nie, bo to jest wiesz jak mówię puszka pandory jak zaczniemy tam grzebać to to wiesz, piłkarze tam jest 50 rzeczy do poprawienia, a niektóre grube nawet.  
I.  
O k.  
Ja bym to znaczy, dobra jak do tego podejść, no ok, to może to wy jak do tego podejść, bo to będziemy musieli sobie.

**Janusz Bossak** 9:13  
Ale trzeba napisać jakieś prace koncepcyjne nad tam czymś nie.  
Część do klienta interesuje klienta interesuje wynik, tak więc my możemy sobie wpisać, że ten pulpit medycznym jest.

**Przemysław Sołdacki** 9:25  
Zostawię tak jak jest znaczy. Ja nie mówię, że ja w takiej formie to prześle klientowi, ale bo sobie jeszcze tam po czyszczę to zanim wyślę, ale dobrze żebyśmy mieli, a ja powiem skryptów. No tak, no jak już to będziemy mieli zrobione, to my zrobiliśmy trochę ten jak przetworzeniu skryptu, tylko po prostu wsadzimy w ten nowy interfejs, żeby to tak wyglądało. Docelowo funkcjonalność dla ssl a jest services. No to tak, to będziemy sobie szczegółowo ustalać, bo to w każdym kwartale jest.

**Janusz Bossak** 9:32  
To ja.  
No tylko.

**Przemysław Sołdacki** 9:52  
Danych z rejestrów między środowiskami.  
K.

**Janusz Bossak** 9:55  
To jest temat, który ja nie wiem, czy on jest znaczy według mnie dużo bardziej istotne.

**Przemysław Sołdacki** 9:59  
Też nie wiem.

**Janusz Bossak** 10:02  
Jest co innego, tak z punktu widzenia wydajnościowego to, co zresztą dzisiaj tam przed chwilą rozmawialiśmy, żeby Piotr końcu opracował koncepcję rozdzielenia kasę definition, tak, żeby były podróżne procesy, dodatkowe tabele i z definition tam 1 2 3 4 jakoś i żeby to ze sobą wszystko współgrało, działało na raportach i tak dalej i tak dalej, ale jednocześnie obciążało całą bazę. Tak to jest.

**Przemysław Sołdacki** 10:31  
Gadałem chwilę z Piotrem, kiedyś przy w kuchni i pojawiło się pytanie, czy to coś da?  
Bo w sumie to jest nasza hipoteza, że to coś da, może się okazać, że to nic nie da.

**Janusz Bossak** 10:44  
Może się tak pogadaj jeszcze Piotr nawet zrobił jakieś tam daleko idące próby przy okazji amrestu, bo tu głównie AmRest tam się o to zapraszał.  
I tam mieliśmy koncepcję jakiś plastrowanie bazę danych, czegoś tam wydzielania tabel do innej nawet i łączenia. No i to Piotr jakoś ostatecznie się tak skończyło, że to w sumie niewiele co daje nie.

**Przemysław Sołdacki** 11:07  
No właśnie, bo wiesz, najłatwiej byłoby jakby zrobić klony tej tej tabeli niż kilka tabel, czy to z mniejsze przeciążenie na serwerze, czy będą szybciej zapytania robione nie wiemy, bo będą miały oddzielne indeksy, może wymagałby jeszcze głębszego robienia, czyli już nie w takiej formie, czyli tylko jak jest jeden proces, to to kolumny są dokładnie takie, jakie są w procesie, nie ma jakiś innych jej przypisywania, w której kolumnie to jest trzymane tylko po prostu jeden do jednego, ale to też nie wiadomo, czy to coś da.  
Jakby należałoby jakieś eksperymenty z tym zrobić.

**Janusz Bossak** 11:43  
Wiesz tu.

**Przemysław Sołdacki** 11:43  
Wiesz co to możemy wpisać coś takiego i to myślę, że bym to wpisał, a przede wszystkim to bym chyba podniósł wyżej.  
To jak koncepcja będziemy mieli, to zrobimy.  
To tutaj można wpisać.  
Para.  
Koncepcyjny na wydajność.  
Chciał.  
Tej maści.  
Miłość.  
Pana i panny to czasu.  
Definition tak tak.  
Iż.  
Możemy, że tak powiem, popracować potestować, bo nie wiadomo, czy to jest dobra metoda, czy to w ogóle coś da, może trzeba coś zupełnie innego. Może trzeba dane po prostu replikować do Rusin i wtedy mieć po prostu ********** szybkie czytanie.  
Nie zrobimy testów, to tam się nie napalał bym, że no to jest gruba zmiana. Tak czy inaczej musimy zobaczyć czy to coś *********** tam nie wiem miliona rekordów i zobaczyć czy podzielenie tego na pół to czy daje bo może nic.

**Janusz Bossak** 12:52  
Pytam.  
No to jest znaczy.  
Jakby inspiracją do tego jest kilka rzeczy. Po pierwsze zmniejszenie rozmiarów bazy danych.  
Ze względu na brak kupy.  
I klienci woleliby mieć odłożone już ileś lat, do których już nie sięgają i mieć bazę, która jest mniejsza, do której sięgają na bieżąco. To jest pierwszy.

**Przemysław Sołdacki** 13:30  
Dobra dzielenie tabeli p.  
Proces.  
Dzielenie tabeli.  
Rok.

**Janusz Bossak** 13:42  
Tak.

**Przemysław Sołdacki** 13:43  
Usuwanie starych danych czy tam archiwizacja bardziej.

**Janusz Bossak** 13:48  
Tak.

**Przemysław Sołdacki** 13:49  
100.

**Janusz Bossak** 13:51  
No i to właśnie był główny powód, tak, żeby właśnie w momencie, kiedy te tak jak msit trzeba AmRest mają już tych kilkanaście lat danych. Po co im to tam trzymać? Nie, a obciąża system i wszystkie nasze jakieś s ql pytania.

**Przemysław Sołdacki** 13:55  
Pan się.  
No tak.  
Wiesz, jakby metoda nie wymagająca jakiś drastycznych prac naszej stronie, to jest taka, że kopiujemy tą bazę, która jest tak jak jest i sobie leży, a zrobienie mechanizmu kasowania po prostu starych danych może dam, ale jaja osowanie.

**Janusz Bossak** 14:25  
Tutaj jest to kasowanie.  
Dlaczego się pracę przerwały? No dlatego, że ktoś może mieć załóżmy jakiś proces czy rejestr, do którego się odnosi.  
Bo bieżących rzeczach, ale tamten już jest nieużywany od lat, ale do niego ciągle się odnosimy, bo to jest rejestr klientów, który zrobiliśmy 10 lat temu.  
I te sprawy mają niskie numerki i ciągle tam są, więc to nie jest tak prosto, że wziąć wszystko, co było w latach 2010 2020 wyciąć. No bo możemy się tam ciągle odwoływać, tak?

**Przemysław Sołdacki** 14:54  
A.  
Wiesz, to po prostu trzeba zrobić dobrze tak, czyli jeśli są proc.

**Janusz Bossak** 15:02  
No.

**Przemysław Sołdacki** 15:04  
W których nie wiem, jeśli jest proces, który jest nowy.  
Tak mam, jeśli podzielimy nowe na stare, na nowe i stare, to jeśli jest jakiś proces nowy, który się odwołuje polem Odnośnik do starej sprawy, to tej starej sprawy nie należy usuwać. Na przykład jakby da się jakiś algorytm przyjąć, który będzie miał sens, bo wtedy mówimy, wiesz, u dużego klienta zwłaszcza mówimy, słuchajcie, zgredzie sobie tą bazę, a na nowej bazie odpalcie skrypt, który wam.

**Janusz Bossak** 15:21  
No tak, tak, tak no.

**Przemysław Sołdacki** 15:35  
Wytnie to, co jest do wycięcia, to sklep czy po prostu jakieś tam narzędzie pochodzi sobie pochodzi, zrobili się baza, mniejsza jeszcze puścicie, żeby się baza sama z optymalizowana się przebudował rejestry. Czy te te indeksy, no i baza będzie śmigać po prostu 5 razy szybciej, bo będzie miała 5 razy mniej danych i lajk i to i tak jest jakieś tam jakieś czynności jak pójdzie coś nie tak to tworzycie z jakby przełączyć się dalej na tą bazę starą.  
Przykład także, że jakaś tam operacja, że oni sobie puszczają w Weekend w taką takie coś i już.

**Janusz Bossak** 16:13  
Temat, który wraca jak bumerang przez wiele lat ostatnich i no nie ma na to ciągle, że tak powiem sensownego rozwiązania takiego, które dałoby się wprowadzić na produkcję.

**Przemysław Sołdacki** 16:23  
Wiesz, nie jest no bo we wsi cię to dokładnie zrobiliśmy. Wywaliliśmy wszystkie dane starsze niż 3 lata.

**Janusz Bossak** 16:30  
Tak no Bruce forts takie rozwiązanie trochę.

**Przemysław Sołdacki** 16:34  
No ale to jest klientem niepotrzebne, bo jeszcze tak naprawdę raporty łączące dane z wielu lat to są potrzebne tylko na bardzo, bardzo ogólnym poziomie. Ja patrzę, jak mamy dane sprzedażowe, to my też mamy przechowane z 3 lat, jakby te dane starsze gdzieś tam są, ale my ich nie używamy w raportach tu raz na jakiś tam na rok chcę zobaczyć, nie wiem, nasze obroty z iluś tam lat, ja nawet nie muszę tego z tablo wyciągać to sobie w optimie pytam i ale.  
Szczegółowych danych nie potrzebuje. Co mnie obchodzi tam 10 lat temu nie wiem jakaś faktura, no.

**Janusz Bossak** 17:10  
No to może być może 10 lat temu nie i z naszego punktu widzenia może nie, ale tak jak nauka na przykład, no to oni chcą mieć jakieś dane audytowe tak kto podjął taką decyzję, że.

**Przemysław Sołdacki** 17:21  
Ale będą mieli w tej starej bazie.

**Janusz Bossak** 17:24  
No.

**Przemysław Sołdacki** 17:25  
Bazę sobie zostawiają, a nowe dane są nowe, bo wiesz, no jakby to drastycznie zmienia. Przykładowo masz dane z 10 lat, a potrzebne są tylko z ostatnich 2, to jakby wszystko będzie szybciej działać. Indeksy mniejszym i mniejsze zasoby w bazie, a tam ta baza może być całkiem wyłączona albo wyłączona, ale jeśli tam nikt nie loguje, więc serwer bazodanowy i tak sobie tam wygasi, będzie utrzymał nie trzymając nic w pamięci, więc dobra prace koncepcyjne to jest zrozumiałe dla klienta też.  
Zrozumiałe jak coś nam wyjdzie to wyjdzie tutaj zarządzanie wymaganiami. Napisałbym o co chodzi, ja bym znaczy jest rzecz w kontekście, a i którą bym rozważył, żeby zrobić dużo wcześniej niż patrzy.  
Bo to może być związane z tym przenoszeniem procesów i to jest kwestia.  
Tego, co tutaj uważam, muszę być dla nas drastyczną poprawą potencjalnie. No skoro Mateusz robi.  
Szablony procesów.  
No to do tego jest potrzebny mechanizm przenoszenia i tutaj wsparła.  
I przy tym, bo ja to znaczy mam taką wizję, to jest jakby znaczy pomysł do do przeanalizowania, gdybyśmy dali rzecz prosto w implementacji, czyli wchodzę sobie w ten powiedzmy definicję procesu i tu miałbym zakładkę dokumenty czy wgrywam pliki nic więcej i nadaje im niezby i nic więcej prosta sprawa, tak jak mamy tam budujemy ten archiwum archiwum, to tam ma struktura, to po prostu lista plików koniec i gdybyśmy wiedzieli tak, że.  
Jeśli w procesie sobie dodam plik, który się nazywa.  
Konfig zalecenia dla jaj do konfiguracji procesu czymkolwiek sobie to nazwiemy to w momencie importu znaczy przenoszenia można by uruchomić coś.  
Żeby e jaj wzięło te zalecenia, przeczytało sobie te zalecenia na tej podstawie wypytał o użytkownika, a następnie na niosło zmiany na proces.  
Wtedy matę.  
Wrzucić w procesie taką zasady, jak skonfigurować ten proces?  
I wiedziałbym, że to niezależnie od konsultanta, zostanie zrobione w ten sam sposób, co dla mnie *********.

**Janusz Bossak** 20:01  
No to się nie uda, znaczy.  
To musi przejść, to znaczy to doświadczenia. Zdobywam teraz przetwarzanie tej tych zapisów transkrypcji. No niestety, śmieci na wejściu śmieci na wyjściu nie to wrzucanie takich luźnych plików jakiś tam wymagań od klienta jakiś nie wiem. Właśnie notatki ze spotkania czegoś tam.  
No to jest taki ****. Ogólnie rzecz biorąc tak i teraz z tego dopiero trzeba zrobić ustrukturyzowaną informację dla jaja.  
Zatwierdzoną, z której on będzie coś mógł zrobił, bo jak on bawili na takim bałaganie to bałagan wytworzy tak znaczy.

**Przemysław Sołdacki** 20:37  
Tak, tak.  
Ale słuchaj, to nie tam nie będzie bałagan, bo tak jak ktoś musi świadomie zrobić szablon procesu, stworzyć regułę, stworzycie tatę i tak dalej to ten projektant tego procesu może opisać, co musi być skonfigurowane i może to konfigurację robić człowiek.

**Janusz Bossak** 21:03  
Ja będę tego.

**Przemysław Sołdacki** 21:03  
Ale będzie, bo jakie moglibyśmy mieć pliki? Ogólnie nie wiem, znaczy opis procesu, to mamy do tego pole.  
Ale byłby taki plikom mógłby nie być w systemie nawet tylko w systemie jest o tyle dobrze, jakie sobie importuje. Eksportuje to te pliki też by mi się przyniosły i tam mógłbym mieć plik przygotowany przez nas, nie tam przed byle kogo. Gdzie jest definicja? Jak skonfigurować ten proces i może konsultant sobie odpalić i ręcznie skonfigurować proces z tymi wytycznymi?  
Ale ja i też może to zrobić, bo to będzie bardzo dobrze ustandaryzowane i przetestowane przez nas to nie nie jest przypadkowe, tylko chodzi o to, że jeśli wiadomo, że że tak jak tutaj mamy obserwatorzy spraw.  
I to nie powinni być przypadkowi ludzie, tylko innym elementem konfiguracji jest spytaj kto powinien mieć możliwość oglądania wszystkich spraw, no to trzeba się dowiedzieć od klienta tak kto będzie mógł wszystkie sprawy zmienić, kto będzie mógł zmieniać sam proces to pytania do klienta, zanim w ogóle ten proces powinien pójść na produkcję. Jeśli jest, załóżmy jest ścieżka akceptacji faktur. To pytanie powyżej, jakiego progu musi być dodatkowa akceptacja?  
Trzeba spytać klienta, kto ma robić dodatkowo akceptację powyżej tej kwoty trzeba spytać klient. To są te rzeczy i później to wgrać w proces, więc może to robić człowiek, ale jakby to dobrze zrobić to tą konfigurację jakby konsultant dostanie pytania od jaj zdobędzie informacje od klienta, odpowie i i na podstawie tego mówię, dobra to ja już tam pozmieniam te rzeczy.

**Janusz Bossak** 22:39  
Czy?

**Przemysław Sołdacki** 22:40  
Więc to to nie jest tak, że coś tam wrzucamy jakieś jakieś śmieci i sobie jaj pracuje, nie nie, to musi bardzo dobrze przygotowany tak jak my programujemy proces programujemy reguły to zaprogramujemy e ja pisząc takiego profesjonalnego pląta.

**Janusz Bossak** 22:55  
Musi być analiza, znaczy ten, no, no to co już kiedyś tam mówiłem, tak, że to musi być prowadzenie tego konsultanta przez proces analizy zdobywania informacji, uzupełnienie tej informacji uzupełniania kontekstowo, czyli w zależności od tego, co odpowiedziano wcześniej poprzednim pytaniu czy 2 3 pytaniach wcześniej? To dalsza analiza musi przebiegać zgodnie z tym, co tam powiedziano i jaki to jest rodzaj typ procesu, co tam powinno w nim się jeszcze znajdować tak dalej.

**Przemysław Sołdacki** 23:22  
Dokładnie, ale. Ale podam ci przykład, może być takie coś, że projektant procesu mówi, jeśli klient powie, że nie chce mieć dodatkowej akceptacji, usuń etap, ten usuń tą i tą regułę i tyle. A jeśli klient podał, że chce, żeby podał od jakiego progu, ale dodatkowa akceptacja, to wejdź w regułę. Tą konkretnie zmień nawet w tej linijce, albo w tym miejscu ten próg.  
I koniec, albo tam, że na przykład jest zmienna wysokość progu. Zmień wartość tej zmiennej i tyle jakby to to nie jest tak, że coś tam sobie coś tam zrób. Nie to bardzo konkretne polecenia, gdzie co trzeba pozmieniać, jeśli tak byśmy zrobili, to zarówno nasz konsultant, a jak i nawet sam klient mógłby sobie wgrać taki szablon.  
I mieć ja.  
Wypyta co tam trzeba zrobić? Ktoś odpowie i ja jest w stanie to wykonać tak, ale w takim trybie bardziej konwersacyjnym więc chodzi mi o to, że taki plik to nie jest jakiś taki. Nie wiem, ktoś sobie coś wrzucić, tylko to jest jakby instrukcja dla a ja jak skonfigurować ten proces i dopóki my tego nie robimy na i to człowiek będzie to robił.  
I to możemy bardzo dobrze przetestować na ludziach. Najpierw także wiesz, jakby to jest jakiś pomysł. Ja nie mówię, że tak musimy zrobione, ale nam sobie pomyślałem, że może powinniśmy zrobić spotkanie gdzie, bo jak ty będziesz i tak w Warszawie, to mógłbyś być nawet jeden dzień dłużej w ściągnęli byśmy jeszcze innych ludzi tutaj od koncepcji, żebyśmy sobie porysowali na tablicy za i przeciw różne możliwe pomysły, bo ja rzuciłem jeden pomysł. Ja nie mówię, że tak musi być, ale to jest jakiś pomysł, ktoś może będzie miał lepszy, może złożymy kilka pomysłów jeden.  
I taką pracę koncepcyjną nad tym jak jaj.  
Mogłoby ustandaryzowany.  
Z pracy, bo to widziałeś. To są Marcin zrobił takiego.

**Janusz Bossak** 25:18  
To też kiedyś myśmy zrobili, znaczy tak, no widziałem to taki generator prądu.

**Przemysław Sołdacki** 25:22  
Ale wiesz, wiesz co jest dla mnie największą korzyścią z tego największą korzyścią jest standaryzacja, czyli ja po prostu wrzuciłem zapytanie od klienta maila, on pokazał, że to jest to spytał, czy to na pewno jest to powiedziałem, tak zrobił sobie według zasad, które mamy w strategii opisał i.  
Dla mnie największą zaletą jest to, że niezależnie kto to będzie robił, czy to nie robił Marcin, czy którykolwiek handlowiec, wszyscy będą tak samo oceniać klient. To jest ********* standaryzacja.  
I chciałbym tak samo mieć, że bierze mi konsultant którykolwiek nowy, stary.  
Wrzuca i kurde wie jak ma to zrobić i jak chcemy, żeby firma pracowały inaczej zmieniamy naszego agenta naszego pląta i firma działa inaczej to jest to dla mnie jakby ważniejsze, nawet być może niż samo podniesienie wydajności, bo to jest zapewnienie jakość tak tutaj, no na przykład on coś zrobił, ale ja mówię, a to chyba jednak tylko skanowanie, no i on jakby biorę, że to pod uwagę i.  
Jakby trochę bardziej świadomie to nie jest regułka napisana nie więc.  
Tego typu mechanizmy byłby super, tak jak mówię do standaryzacji. Dobra, czekaj, wróćmy tu.

**Janusz Bossak** 26:41  
Wracając do tego jeszcze, co rozmawialiśmy o tym znaczy, wydaje mi się, że to co teraz omówiliśmy, to jest koncepcja. Tak rzeczywiście na ten kwartał tam nie wiem. Trzeci czy czwarty przyszłego roku, żeby aż tak daleko iść i budować te procesy w oparciu taki dialog. Natomiast to, co robi teraz Mateusz mówią mateuszu kołakowskim, czyli.  
Próbuję stworzyć te standardowe procesy, to według mnie tu powinniśmy mocno się nad tym pochylić i to, co tutaj. Zresztą mówiłeś przed chwilą.

**Przemysław Sołdacki** 27:14  
Ale to właśnie o to chodzi.

**Janusz Bossak** 27:15  
Żeby te standardowe procesy nie takie noże standardowe, wiadomo tak, które są trochę pseudo standardowe, no bo one się za każdym razem jednak ciutkę zmieniają, żeby tutaj mu pomóc. I tak powiedziałeś, żeby tu ja potrafiło powiedzieć co.

**Przemysław Sołdacki** 27:30  
Tak więc co to może ja, że tak powiem cię się niejasno wyraziłem mi chodzi o te standardowe procesy, nie jakiekolwiek.

**Janusz Bossak** 27:36  
No bo ja myślałem, że mówisz o takich normalnych, dużych procesach o wdrażaniu klienta i tak dalej, ale to wtedy mi nie bardzo.

**Przemysław Sołdacki** 27:40  
Nie właśnie chodzi o to, że załóżmy ja pamiętam jak z spytałem, czy możemy sobie teczkę wdrożyć.  
U nas firmy.

**Janusz Bossak** 27:50  
No wiem, no mówiłeś.

**Przemysław Sołdacki** 27:50  
I i natychmiast dostałem 10 pytań, które mogłoby ey mi zadać. Może moje odpowiedzi były mało ciekawe, bo w zasadzie nie wiedziałem co odpowiedzieć, ale ale mogło być tak, że Mateusz kołakowski, żeby było jasne, robi te szablony i w tym szablonie na razie nie ma gdzie wpisać, ale mógłbym ich miejsce na przykład właśnie wrzucenie dokumentu i ten dokument musi się nazywać x, jakoś tam nie wiem, wytyczne dla jaj czy tam wytyczne konfiguracji procesu i musi się tak nazywać.  
Jakby mamy co za kodowane, może to być po angielsku, nie ma znaczenia i jeśli taki plik jest to podczas importu.  
A ja i mówi, słuchaj, tu są wytyczne, czy ja mam to skonfigurować, albo po prostu jest specjalny guzik skonfiguruj według wytycznych i wtedy dokładnie ja je robi to co jakby projektant szablonu przygotował.  
Więc ja prace koncepcyjne nad tym, to możemy sobie tutaj wrzucić nawet, bo to to nie jest takie proste.  
Nad użyciem aj do konfy.  
Góra racji.  
Szablonów procesu, bo o to mi chodzi, żeby to było jasne, nie, nie cokolwiek, tylko to muszą być szablony zrobione przez nas, żeby one były przemyślane, że to tak jak my sobie, że tak powiem piszemy reguły standardowego szablonu. To możemy od razu dać wytyczne, jak ten szablon należy do konfigurować typu, dodać jakiś tam userów, trzeba grupę założyć albo grupa i już się za importowała, ale trzeba kogoś dodać do tej grupy, to ten proces zadziałał i tak dalej, więc zostawiam, że to jakieś prace koncepcyjne.  
No i tutaj ewentualnie gdzieś tam można by wrzucić.  
Więc nie chcę tego napychać się naszej mapy. Raczej właśnie.

**Janusz Bossak** 29:47  
Znaczy no już ciasne robić.

**Przemysław Sołdacki** 29:48  
Ale zaczyna się napychać to mam.  
Yy, więc nie wiem, możemy to wiesz przenieść dalej. Możemy to przenieść na.  
3, żeby tu nie było napchane.  
I to bym wysoko do.

**Janusz Bossak** 30:04  
Samo to przenoszenie procesów między środowiskami, a wiem ile z tym było gadania i tak dalej to zajmie całego Damiana.  
Plus pół Piotra.  
No tak.

**Przemysław Sołdacki** 30:16  
No dlatego wiesz.  
Tak jak mówiłem, widzę 2 najgrubsze rzeczy, przenoszenie procesów i dokończenie tego raptem 2 zespoły oddzielne, które pracują tylko nad tym przez 3 miesiące, aż że tak powiem, dojdą do zajebistości, że te rzeczy po prostu działają tak, że przez najbliższe lata nie będziemy się musieli do tego dotykać, bo po prostu wszystko tam działa, więc jakby chodzi o to, żebyśmy się nie rozprasza i na inne rzeczy, bo to jest trudne. To nie jest tak, że tam klikam import, nie tylko musimy tam ileś rzeczy musi sprawdzić, czy czy mi to nie zepsuje na produkcji.  
Że na przykład coś się nadpisuje czy na pewno chce więc zrobienie tego dobrze to będzie jakieś tam wyzwanie. No dobra, ale wiesz co, bo tak nie mamy tu nic, co jest na 4 stało.  
Coś co tu poprzekładać.

**Janusz Bossak** 31:07  
O 4 jest tak daleko, że.

**Przemysław Sołdacki** 31:09  
Ale wiesz co, żebyśmy mieli jakieś ramy tego, no jakby.

**Janusz Bossak** 31:12  
Wzrok ten myśli.

**Przemysław Sołdacki** 31:15  
Mam jeszcze jedną koncepcję, ale to też dyskusje, bo wiesz, ja Jestem generatorem pomysłu swoim dobrym, tak jak ja.  
Niekoniecznie moje pomysły są dobre, ale ale jakieś są.  
Chodzi mi o to, że my działamy w trochę innym trybie, zawijam, przynajmniej to tworzenie procesu. Dział robimy na tej zasadzie, że.  
Rozmawiamy z jaj aj jaj, generał jest sona, a my programistyczny tego dysona zamieniamy na definicję procesu i wrzucamy do.  
Dom i to jest jakby droga w jedną stronę.  
Natomiast mogło być tak, że że przestajemy działać w trybie takiego l ma pytanie odpowiedź tylko w trybie agenta, gdzie mówimy tu jest specyfikacja wymagań r.  
Sobie ten proces on sobie robi to po kawałku.  
Dodaj etap dodaje. Drugie etap dodaje strzałkę dodaje regułę.  
I później sobie ten sam agent lub drugi agent sprawdza, czy to co tam zrobił to w ogóle jest zgodne ze specyfikacją i sprawdzać to w ogóle działa na no, bo na przykład i jakby pozdrowienia modrica programisty cznie jest dobre odpowiadanie, czy ta operacja jest w ogóle wykonalna? Jeśli nie, to dlaczego? Na przykład? Bo agent mówi, to usunę sobie regułę, a mody mówię, Nie możesz poznać, bo bo pola są, które w tam albo chcę zmienić pole Nie możesz, bo jest reguła, która korzysta z tego pola.  
I on mówi, aha, dobra jakby czyli tryb agent owy, gdzie to sobie chodzi w tle i coś tam robi? Pracuje jakby tak pojedynczo nad konkretnymi kimś procesami, tylko to jest taka wizja odległa. Wydaje mi się, ale chociaż już się okazać wcale nie, bo za pół roku to w ogóle te te się agenci to będą tak zapierdzielać, że po prostu to będzie normalne.

**Janusz Bossak** 33:10  
Znaczy, ja tutaj wrócę do tematu, może trochę obok, ale jednak ważne go tych testów and went. Dlaczego do tego wracam? Bo to jest też jeden.  
Z elementów tak pracę takiego agenta, że coś działa.  
Czyli, że ten proces, który sobie tam robię, Jestem w stanie zewnętrznym narzędziem typu play reit przetestować, że mogę przejść tego etapu na tn, że się to przekazało tej osoby, które się miało przekazać i tak dalej, tak.

**Przemysław Sołdacki** 33:39  
A czy play rajd jest oparty o jaj?

**Janusz Bossak** 33:45  
Znaczy sam jako taki nie no bo to jest język programowania. Można powiedzieć tylko język programowania testów, ale i wspiera play. Rita i ja sam pisałem, jest mnóstwo różnych opracowań, gdzie można za pomocą ya dość łatwy. Znaczy to znowuż to pozorność łatwości tak, no, ale można generować sobie takie skrypty, skrypty play, litowe i teraz te skrypty już potem normalnie uruchamiasz i to działa.  
Ja już takie próby zrobiłem. To co tutaj rozmawialiśmy, mam opracowany no o ileś.

**Przemysław Sołdacki** 34:21  
Zastanawiam się, czy to nie jest ślepa uliczka.

**Janusz Bossak** 34:23  
Nie to jest w ogóle.  
Baza i podstawa wszystkiego. Zresztą jak czytam o tych agentach i tutaj przerabiam różne rzeczy. Jeżeli mówimy o agentach, które mają.  
Pisać na przykład frontend.  
To w każdym przykładzie jaki widzę na YouTubie w różnych filmikach każdym przykładzie jest ju x agent, który dokładnie robi to o czym mówię, czyli używa testów, że pisze sobie testy play rajdowe i za pomocą play rita patrzy dosłownie, patrzy na aplikację i sprawdza czy ona działa tak jak powinna działać i to jest w ogóle warunek sine qua non to po prostu musimy coś takiego mieć.

**Przemysław Sołdacki** 35:03  
Co tak, ale wiesz co znaczy zastanawiam się, dlaczego mówi ślepa uliczka, bo te przejście z takiego działania zwykłego na działania agentów owe to mogę sobie wyobrazić agenta, który robi to, co robią nasze testerki, czyli mają jakąś tam specyfikację tego, jak to powinno działać, mają wiedzę ogólną i sobie klikają i testują czy to działa i czy jest zgodne ze specyfikacją i mógł być agent, który robi dokładnie to samo.  
W całości i.  
Nie pisze sobie żadnych skryptów, tylko po prostu robi to ręcznie różnica jaką widzę, że taki agent będzie działał wolniej, zużywał dużo więcej zasobów niż odpalenie skryptu w playliscie.  
Więc jeśli byśmy chcieli puszczać dużo testów represyjnych, to by tam zżerało dużo pieniędzy, więc może być wydajniej, żeby agent pisał tylko o skrypty.

**Janusz Bossak** 35:51  
No tak.  
No tak, no bo to tak się robi.

**Przemysław Sołdacki** 36:03  
Tylko.  
Idealnie by było, gdyby taki agent, jeśli już piszę sobie te skrypty i ewentualnie też aktualizuje, to robiłby to, czego nasze testerki się nie chcą podjąć chwili pisania skryptów.  
I moglibyśmy być tak, że czy już na etapie projektowania, funkcjonalności, czy nawet później, że nasze testerki piszą, co powinno być przetestowane, agent pisze z tego wszystkiego razem skrypty play lajtowym.

**Janusz Bossak** 36:34  
Dokładnie tak, tak to już mam zrobione.  
Yy, cała zabawa możesz wpisać cała zabawa polega na tym przynajmniej na tym etapie mojej wiedzy i umiejętności posługiwania się, a ja jem.

**Przemysław Sołdacki** 36:38  
Wpisać to na ku 4.

**Janusz Bossak** 36:48  
Że trzeba go nauczyć.  
Co to znaczy znaczy musi wiedzieć jak.  
Wygląda na przykład pole typu data.  
U nas, czyli gdzie on musi klikać, w co, że tam w ten zegarek czy w ten kalendarzy grze mu się pojawi akurat takie coś a nie coś innego i to jest.

**Przemysław Sołdacki** 37:09  
A on?  
Tego.

**Janusz Bossak** 37:10  
Nie.  
Znaczy po części wyczaję, ale często się.

**Przemysław Sołdacki** 37:13  
Może na razie nie.

**Janusz Bossak** 37:15  
Może na razie nie.  
I to jest robota, którą ja znaczy teraz już nie robię, ale robiłem tam miesiąc czy 1,5 miesiąca temu i zacząłem ten page Object model, bo to tak się nazywa robić tak, czyli biorę sobie nasz formularz i to jest ten nasz page Object i opracowuje z e ja jem.  
Wszystkie elementy, które na tym formularzu mogą mogą potencjalnie wystąpić, czyli pole typu data, pole typu tex, pole typu takiego przycisk, taki przycisk, taki prawy panel, historia, coś tam coś tam i wtedy jak już masz opracowany ten page Object model i to jest największa robota, którą trzeba zrobić.  
To później napisanie testu przetestuj mi następujący scenariusz, dosłownie tak możesz pisać, nie weź się, zaloguj do tego, zrób to zrób to, zrób to. Kliknij to sprawdź, czy to jest to i on z takiego opisu robi test.

**Przemysław Sołdacki** 38:04  
Tak.

**Janusz Bossak** 38:09  
Który możesz są wielokrotnie używać, tylko napiszę ten test dobrze zgodnie z tym Object model i w momencie kiedy ja coś zmienią w tym model to wszędzie mi się to zmieni. Nie, bo to jest od.

**Przemysław Sołdacki** 38:16  
No.  
Tylko, bo wtedy rola naszych testerek zmieni się ręcznych testerek, bo rozumiem one ręcznie testują, nie piszą skryptów, zmieni się na nadzorców agenta, który pisze testy play rajdzie.

**Janusz Bossak** 38:34  
Czy one piszą skrypty same dla siebie właśnie takim języku naturalnym, że te jakby scenariusz repo nie.

**Przemysław Sołdacki** 38:40  
O k. Czyli one piszą jakby wytyczne do testowania i nadzorują to żeby agent te wymagania przełożył na play rider.

**Janusz Bossak** 38:49  
Tak znaczy.

**Przemysław Sołdacki** 38:49  
Tak, tak, taka jest wizja docelowa.

**Janusz Bossak** 38:51  
Znaczy.  
Ogólnie tak no właśnie nie wiem czy to one czy powinien być powinna być osoba, która się na tym zna, znaczy mówię o tej warstwie przetwarzania tego na tego play rita dziewczyny powinny się zajmować testami rzeczy nowych, które jeszcze nie są przełożone na play rita, bo dopiero jak coś jest ustabilizowany i uznajemy, że tak to ma działać. Wtedy jest sens przełożyć tego to na play rida.

**Przemysław Sołdacki** 39:16  
Wiesz co, ale ja bym jednak się upierał nad tym, że jakby ja podejrzewam, że w ciągu określonego czasu to dosyć krótkiego pół roku rok 2 lata. Trudno na tym etapie to przewidzieć, że główną pracą ludzi takich pracowników biurowych będzie nadzorowanie. Hej jajek, tak samo jak wejdzie robotyka, jakąś większą skalę, zadaniem tych różnych inżynierów, na przykład budowlanych.

**Janusz Bossak** 39:37  
Tak, tak, tak, tak.

**Przemysław Sołdacki** 39:46  
Nie będzie noszenie cegieł, tylko patrzenie, czy te roboty dobrze te cegły noszą i czy nie wiem jak jak robot nie wiem tynku je czy czy tynku je właściwą ścianę i jakby praca w tą stronę się będzie zmieniała, więc my powinniśmy.

**Janusz Bossak** 39:53  
No dokładnie.

**Przemysław Sołdacki** 40:02  
Jakby takie coś, że ktoś siedzi i klika ręcznie testy to to może robić tylko po to, żeby dobrze nakierować tego agenta i jaj, żeby on testował to co trzeba testować i żeby testował w taki sposób jaki trzeba testować, więc jeśli testerka opisuje co trzeba testować agent zmienia to na play rita, to ona może sprawdzić, czy te testy w playliscie jak się odpalają, czy one w ogóle poszły w dobrą stronę, a jeśli nie, to mówię agentowi, słuchaj, agent głupoty mi tu robisz, weź mnie nie klikaj tego nie się klika coś innego, bo w ogóle nie nie ta ikonka.  
I on to sobie poprawi, gdy tak Jestem w stanie sobie to wyobrazić i widząc to, co się teraz dzieje.

**Janusz Bossak** 40:37  
Teoretycznie.  
Na tym na tym etapie no to wymaga jednak znajomości tego plyta znajomości tej ideologii, nazwijmy to znaczy metodyki play Object model znajomości wszystkich tych selektorów.

**Przemysław Sołdacki** 40:53  
To nie przekracza zdolności intelektualnych naszych testerek. O ile pisanie skryptu Jestem w stanie powiedzieć, że one się będą z tym źle czuły.  
Pewnie się źle czują, dlatego on tam mimo prób nie udało się to i je. Gdybym ja teraz miał pisać skrypty w pythonie to by była dla mnie męka, ale ja mówię powiem agentowi, Napisz mi skrypt, który robi to i to i on napisze i to zadziała. To ja wiem, że to jest dobrze zrobione, bo ja wiedziałem czy to ja zauważam na przykład dałem jimina jowi, żeby mi przeanalizował tabelkę w excelu i na podstawie danych policzył mi segmentację to mi pokazał, że umieszcza się 4 skrypty w pythonie napisał.  
I mi dało odpowiedź, czyli on nie robił tego ręcznie, tylko napisał skrypty, które to robią, zobaczył, co wyszło, zrobił kolejny z tym zrobił po 4 skryptach wyszła wynik końcowy i dla mnie to jest lepiej, bo jest mniejsze ryzyko pomyłki, bo to ostatecznie poszła algorytmem, więc pewnie to będzie w tą stronę szło. No ale ja i tak musiałem nadzorować to co dostałem, to to jest to co chciałem, nie więc człowiek będzie takim kierowcą do tego jaj.

**Janusz Bossak** 41:51  
No.  
Czy generalnie mi chodzi o to, że te testy end to end są nam niezbędne w wielu przypadkach?

**Przemysław Sołdacki** 42:09  
Słuchaj, wpisałem na na ku 4, jak się da wcześniej pewnie testerki mogłyby to wcześniej, jak to jest coś rusza, jeszcze im dasz.

**Janusz Bossak** 42:10  
Po pierwsze.  
Muszę robić ciąży, muszą robić teraz jednak 4. On chciałbym mieć efekty, znaczy działające testy i pokryte.

**Przemysław Sołdacki** 42:21  
Ale to co wpisać na *****?

**Janusz Bossak** 42:24  
Znaczy, według mnie to powinniśmy robić, no we wszystkich kół i od ku jeden ku 2 aku 3 4 my też musimy pracować nad testami, no mamy bardziej bliskie pokrycie testami.

**Przemysław Sołdacki** 42:31  
Ale, ale tego nie robimy i jak to zaczniemy robić, to będziemy robić cały czas, tylko chodzi o to uruchomienie tego mechanizmu, czyli nauczenie testerek, pokazanie im, jak to się robi.

**Janusz Bossak** 42:36  
Daliśmy sobie.  
Uszatku jednym zrobić no.

**Przemysław Sołdacki** 42:47  
No dobra, no ale wiesz jak się boję znaczy tylko pod warunkiem, że to nie zaangażuje deweloperów. To tak.

**Janusz Bossak** 42:50  
Znaczy człowiek zapisać.  
Zapisaliśmy sobie strategii stabilizację. To jest jeden z elementów stabilizacji systemu naczy. Musimy mieć testy, musimy mieć testy po prostu.

**Przemysław Sołdacki** 43:02  
Wiesz co dobrze ja to wrzucę.

**Janusz Bossak** 43:06  
Na przykład ten przypadek, który tutaj widzieliśmy dzisiaj na tym tak, że zrobiły się te rameczki.  
To jest rzecz, którą muszą wykrywać testy.

**Przemysław Sołdacki** 43:14  
Ale.  
Tylko wiesz co agent mógłby tego nie zauważyć, no bo pewnie by nie zauważył, że że na co zwrócić uwagę człowiek zauważy i wtedy testerka mówi, słuchaj, agent, dopisz taką rzecz w tym play ricie, czy się nie pojawiają jakieś rameczki dziwne znaczy nawet nie wiedziałbym w sumie jak agentowi to wytłumaczyć, ale wiesz jakby dalej jak chodzi mi o to, że my nie zrezygnujemy z ludzi, ale będzie tak, że jeśli powie testerka, że.  
Agent Napisz mi te takiej skrypt co tam będzie sprawdzał czy się ramki z powrotem nie pojawiły bo tutaj zobacz na guzikach są takie ramki to on podejrzewam będzie w stanie wyczaić jak ten skrypt napisać.

**Janusz Bossak** 43:56  
No to są też metody takie robi się zrzuty ekranów i on porównuje na przykład zrzut ekranu do zrzutu ekranu tak czy to się zmieniło.  
I i co się na tym zrzucie ekranu zmieniło tak, czyli po aktualizacji? Czy jest tak samo jak było przed aktualizacją? Ale to są inne techniki niekoniecznie.  
Się nawet innych testów nie tutaj.

**Przemysław Sołdacki** 44:18  
Jest to to ja tak napiszę, czyli my wku. Jeden tworzymy mechanizm testów n tvn w player z użyciem agenta. Zaangażowanie testerów bez angażowania programistów. Jeśli tak to róbmy.  
Daje sobie jakiś deweloper siedział bo bo nie zrobimy rzeczy, które tu są.

**Janusz Bossak** 44:35  
Nie jest potrzebny, no potrzebny testem.

**Przemysław Sołdacki** 44:36  
No to to tylko zanotowałem, że tak jest dobrze. Wiesz co?

**Janusz Bossak** 44:39  
Tylko nie będę się tym zajmować.

**Przemysław Sołdacki** 44:41  
Słuchaj, to przyjrzyjmy się tutaj dalej. Czekaj te zmiany.  
Halo.  
Ale malo.  
Wysłałam spotkania później mam Wywiad, także nie pogadamy.  
O trzynastej.  
To, że o trzynastej?  
No hej.  
Yy, dobra, właśnie 5 minut nam zostało się.  
W takiej koszulce no dobra.  
Dopełnieniem o tym w kalendarzu mieli wpisali, którą dzisiaj.  
Kiedy więc dobra jest to zarządzanie wymaganiami ze znakiem zapytania i tu nie wiem, czy jest to proces, obsługa, wymagania do procesu projekt.

**Janusz Bossak** 45:28  
No bo to jest być związane z nim zarządzaniem wymaganiami. Tak, czyli gdybyśmy już je mieli, to wtedy na ile ten edytor procesu mógłby być z tym spokojnie tak.

**Przemysław Sołdacki** 45:37  
No dobra, ja to połączę, bo to jest w sumie.  
Dobra, bo tutaj gdzie ja wiedziałem, że to jest dobrze czuję. No dobra.  
To będzie powiązane. Zobaczymy, ale o k. Jakbyśmy te rzeczy zrobili i byłyby dobrze zrobione i działały to monitor wydajności na poziomie reguł. Uważam byłoby fajne dla serwisantów.  
Że wchodzą.  
No i a ja im mówię, słuchaj, wczoraj ktoś zepsuł regułę i ona teraz zamula.

**Janusz Bossak** 46:18  
Znaczy ja już tutaj Mateuszem rozmawiałem właśnie o dokładnie o tym rozmawialiśmy. Już wielokrotnie już rozmawialiśmy, żeby trzeba, no bo zaczęła się dyskusję od analizy logów. Ja mówię, Mateusz, no dobra, no to patrzysz na takie logi, zapisy vlogach, ale od razu powinien sobie ten EI uświadomić, że skoro się coś pojawiło w logu, to powinien zacząć szukać przyczyny tego tak, czyli jeżeli w logu jest napisane, że reguła nie działa, no to sprawdź, czy przypadkiem ktoś nie ostatnio nie zmieniał.

**Przemysław Sołdacki** 46:18  
Bo to człowiek wyczai.

**Janusz Bossak** 46:49  
Czegoś regule, tak.

**Przemysław Sołdacki** 46:50  
No tak, czyli jest jest jakiś algorytm rozwiązywania problemu i żeby to dobrze działało i przede wszystkim trzeba wiedzieć, który problem w tym rozwiązywać, bo to co mogłoby robić znaczy zanim to trafi do jaja i to musimy przygotować, czyli na przykład wyciągamy statystykę, ze ostatnio nie wiem dzień tydzień i miesiąc tak w różnych perspektywach co najbardziej zamula serwer albo co generuje najwięcej błędów i te zestawienia dajemy do lema dodatkowo wyciągamy dane.  
Które czy te reguły, które tam się pojawiają, były zmienione w ostatnim czasie i to informacje też zbieramy i przekazujemy do lema i dajemy wytyczne, jak się powinno tego typu problemy diagnozować. Dajemy do lema, ale mówi dobra, to ja chcę sprawdzić tą regułę.  
I wyciąga reguła, jest sprawdza, co tam zostało zmienione, bo mamy w historii, co zostało zmienione, czyli my musimy i algorytmiczny zebrać dane i i dać wytyczne do lema jak to robić, bo to jest znowu ten sam temat. Dla mnie standaryzacja obsługi, czyli któryby konsultant się do klienta nie zalogował to dostanie na tacy.  
Że tak powiem zrobione śledztwo tak jak się powinno robić śledztwo nie tak, że tylko Piotrek buczkowski, tłumy, tylko, że już każdy będzie to umiał.  
Więc, yy, to to bym to dał i to możemy sobie i taki profiler to jest. No też ciekawy temat, że jeśli reguła ci się wysypuje, to robić co do linijki dostał, gdzie się wysypuje i w którym miejscu na zamula to jest zostawienia, a tu jest tylko prace koncepcyjne, ja może.  
Że bez słowa taki manager.  
Bo to nawet mamy gdzieś wpisane chyba w dotacji. Tam dobrze pamiętam.

**Janusz Bossak** 48:42  
Nie jest znaczy tu Piotr się strasznie upierasz, to nie jest debata gier i nigdy nie będzie.  
Bo to nie jest dość śledzenie na bieżąco tego, co się dzieje. To jest tylko analiza.

**Przemysław Sołdacki** 48:52  
Tak post factum.

**Janusz Bossak** 48:53  
Znaczy, które się zdarzyły?

**Przemysław Sołdacki** 48:55  
Post factum zgadzam się, ale to jest debatę, który odpala, odpaliła się reguła i możesz nie zatrzymujesz realizacji.

**Janusz Bossak** 49:02  
To nieźle.  
Analizator.

**Przemysław Sołdacki** 49:05  
Analizator jak zwał tak zwał dobry to to już daje mi jakieś obraz tego róg mapy, którą my możemy.  
Zresztą te zmiany ja to zrzucam na koniec, bo.  
Nie postrzegam tego jako czegoś, co mi zwiększyć efektywność, ale ok.  
Dobra, to jakoś mamy to ogarnięte.  
No to jest mnóstwo znaków zapytania, mnóstwo rzeczy, które trzeba będzie sobie.  
Po prostu dyskutować.  
Dzień dobry, czy coś my jeszcze bez coś jakbyśmy się pojawił, ale mi uciekła.  
Dobra, wiesz co zostaną się czy zrobić takie spotkanie, gdzie my tam nie wiem w Warszawie, skoro już będziesz kogoś ciągnąć, żebyśmy sobie pogadali, bo pewnie i Mateusza Daniela ma znaczy Mateusza kołakowskiego i Mateusza kisiela, też zresztą piotrkowskiego byśmy sobie zrobili, to wiesz, zapytałam, kiedy ci tam wygodnie, jak w macie być chyba poniedziałek wtorek, no to może nie wiem środę jeszcze.  
To to byłoby wygodne.  
Słuchaj to.  
To tak to chyba tyle.

**Janusz Bossak** 50:18  
Dobra.

**Przemysław Sołdacki** 50:19  
No i tak już to tych 2 spotkań nie wiem, możecie nie robić, możecie, ale jak chcecie to zróbcie nie to napiszcie mieć z grubsza gdzie jesteśmy.

**Janusz Bossak** 50:26  
Przegadamy jest dobra o k.

**Przemysław Sołdacki** 50:27  
Super, to dzięki hej.

**Janusz Bossak** zatrzymano transkrypcję
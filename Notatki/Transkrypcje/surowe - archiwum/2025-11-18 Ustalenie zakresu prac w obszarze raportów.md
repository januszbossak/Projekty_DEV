**Transkrypcja**

18 listopada 2025, 09:47AM

**Janusz Bossak** rozpoczęto transkrypcję

**Janusz Bossak** 0:03  
Komisja właśnie na temat też tych litrów użytkownika.  
Temat jest powiedział dużo bardziej złożony niż mi się wydawało wczoraj jeszcze.  
Znaczy jest kilka takich rzeczy do poprawienia, powiedzmy wizualnie jakoś tak to co się da zrobić miarę sensownie. Natomiast Piotr zwrócił uwagę na problemy wydajnościowe.  
I to, że do wielu rzeczy w ogóle po prostu totalnie błędnie podeszliśmy.  
Jak chociażby wyświetlanie nie wiem imion, nazwisk, filtr tą typu nazwisko.  
I te nazwiska są brane ze wszystkiego, co jest wyświetlane tak, czyli jedziemy po bazie danych po jakimś tam tekstowym.  
I.  
Wyświetlamy.  
Czekajcie, muszę tutaj dali.

**Mateusz Kisiel** 1:03  
Takie pole wyboru często są limitowane do 20 opcji. Z tego co pamiętam, że tam nie pobieramy wszystkich danych, tylko pobieramy te 2 20 pierwszych.

**Janusz Bossak** 1:03  
Czekajcie.  
No no tak, ale wybieramy.  
Pośród miliona, które potencjalnie mamy w raporcie?  
I nie zaindeksowanych.  
A jeszcze jest tak zrobione, że jest jakby jak jest.  
Jest na przykład nazwisko Kamiński, to w tej chwili amii jak wpiszesz to też szuka.  
No i to wiesz, wydajnościowo to jest po prostu zabójstwo dla dla systemu.

**Mateusz Kisiel** 1:46  
Mhm.

**Janusz Bossak** 1:50  
Yy szukanie po nie indeksowany tym polu, no i tam znaczy prośba do was, ja wam podeślę za chwilę te nagranie.  
Z tej rady deweloperów może macie dostęp do do tej spotkania rady deweloperów? Tam będzie tam jest to nagranie i tam jest dużo na ten temat tak, czyli tam Piotr sugeruje użyć.  
Indeksów na tych polach.  
I taki mechanizm był kiedyś tam przygotowywany i on nie został rozwinięty, aczkolwiek jego zalążki istnieją i to trzeba będzie rozwinąć.  
To jest w tym obszarze, bym nazwał to wydarzenie. Chciałbym tak znaczy, żeby te rzeczy były tam pokazywane prawidłowo. Mówię o Polakach.  
Tekstowych, tak.  
Potem jest problem z polem typu.  
Słownik owego.  
Yy bo.  
No niby jest fajniejsze, no bo jest o Słownik owane, ale też nie do końca wiadomo.  
Właściwie co wyświetlić w filtrze?  
Bo mamy 2 przypadki.  
2 przypadki. Jeden przypadek jest taki, gdzie w słowniku jest tylko kilka pozycji. To są na przykład jakieś kategorie a BCD.  
No i wtedy jest sens wyświetlić te 4 kategorie, nawet jeżeli którejś z nich nie ma w danych które.  
Ma raport tak więc teoretycznie mogłoby tak być z drugiej strony, jeżeli Słownik to jest na przykład Słownik klientów, który zawiera 10000 pozycji. Załóżmy w tym naszym słowniku takim mamo, hitowym słowniku.  
A na raporcie wyświetlamy 5 klientów to po co mi filtrze 10000 pozycji klientów, skoro mam 5 w tym raporcie? Tak.  
I to są 2, jakby sprzeczne trochę 2 sprzeczne sytuacje, ale jednak musimy jakoś je.  
Yy, że tak powiem ogarnąć.

**Mateusz Kisiel** 3:53  
To obecnie, która opcja jest tam domyślam.

**Janusz Bossak** 3:56  
Ta gdzie wy znaczy teoretycznie ta pierwsza to znaczy wyświetlamy to co jest w raporcie.  
Ale to wyświetlamy źle jeszcze obecnie.  
To jest związane z tym distinct em, o którym mówił o którymś momencie gdzieś tam ania, bo jeżeli na wśród pierwszych 20 wyników.  
Będziesz miał na przykład część, a część, a część, a część a część, a i tak 20 razy to dostaniesz jedną pozycję w tym filtrze o nazwie część, a nie będzie w ogóle pozycji.  
PC idę mimo że dalej gdzieś tam w raporcie występują.

**Mateusz Kisiel** 4:38  
Tak, to trzeba pasquale disc robić.

**Janusz Bossak** 4:40  
Tak i to jest rzecz do do do do poprawienia, natychmiast, przy czym ona mówi, no to poprawi trochę.  
Że będzie trochę lepiej się to wyświetlało.  
Ale nie do końca nadal dobrze tak, no bo może być tych części więcej niż 20, które w tej chwili w filtrze wypisujemy.  
No ale powiedzmy, że z tym można sobie poradzić, no bo można wpisywać jakiś fragment i wtedy się pojawiają te jakby następne. Tak pytanie, jak to właśnie sensownie zrobić.  
Natomiast to nie chroni nas przed tą sytuacją, znaczy chronie nie chroni tak, no przed tą sytuacją wydajnością.  
No bo my czytamy, jak gdyby już z danych, które idą do raportu.  
I nie wiem jak to jest w sumie robione, no bo jeżeli.  
Raport miałby, nie wiem 10000 pozycji.  
To my na backendzie z tych 10000 pozycji robimy w tej chwili nasz teraz nie robimy, ale będziemy robili tak.

**Mateusz Kisiel** 5:44  
Znaczy.  
Nie Jestem tego przekonany, pewny, ale wydaje mi się, że to byłaby front endzie jest sprawdzane, jakie są dane w raporcie i na podstawie tego jest jakieś zawężanie, ale to trzeba sprawdzić.  
Ale ogólnie większość tych filtrów działa w ten sposób, że tak naprawdę z dodatkowe zapytanie raport owe, czyli na przykład jak dodać się jakieś pole tekstowe powiedzmy.  
Który ma ileś tam opcji to idzie po prostu dodatkowe, kiedy questy jakby powstał nowy mini raport z tym polem, tak.

**Janusz Bossak** 6:21  
Oczywiście dopytujemy się tak, no do backendu.  
No dobra.

**Mateusz Kisiel** 6:28  
Bo jest też taka sytuacja, że jak mamy tabelę na przykład tak, to w tabeli jest pagina racja, więc mamy tam pierwsze, nie wiem ile tam 50 pozycji. Tak więc jeżeli chcemy mieć wszystkie opcje do wyboru, to nie możemy brać z tej pierwszej strony tylko i wyłącznie tylko musimy brać jakby z całości i żeby brać z całości właśnie po to chyba to nowe zapytanie idzie.

**Janusz Bossak** 6:50  
O k no to to musimy znaczy, ja bym zrobił to tak, że w pierwszej kolejności.  
Inaczej w pierwszej kolejności bym was poprosić, żebyście wysłuchali. To jest tam z 30 minut. Trwa to nasze spotkanie rady deweloperów, żebyście obaj wysłuchali go ze zrozumieniem tej części, która dotyczy właśnie tego tych filtrów.  
Użytkownika i w szczególności tych elementów wydajnościowych, bo to bym chciał, żebyśmy też tam którymś momencie do tego doszli. Na razie w tej jakby pierwszym takim trochę porządkowaniu tych filtrów użytkownika tutaj nie będziemy zbyt zbyt mocno walczyć na razie z tą wydajnością.  
To zostawimy sobie na drugą turę, natomiast teraz bym chciał uporządkować je od takiej strony trochę wygląd owej.  
Yy zachowania takiego domyślnego w różnych okolicznościach, yy, no także takie bardziej prace po stronie frontowej i niektóre tak jak tutaj. To co teraz o tym dystrykcie rozmawiamy po stronie backendu, ale jeszcze bez tych głębokich zmian, o których mówi tam Piotr. Na tym spotkaniu nie.

**Mateusz Kisiel** 8:01  
Czym tak naprawdę ta zmiana z tym dystryktem jest nawet frontend owa? Dlatego no bo my wysyłamy, wysyłamy request z jakby nową definicją raportu to backendu i jakby pks to potem zwraca, czyli po prostu trzeba dołożyć ta tego distinct po prostu w tym queście, który jest frontendu tak.

**Janusz Bossak** 8:19  
No nie wiem czy Przemek ty wiesz o co chodzi, o czym my mówimy?

**Przemysław Rogaś** 8:23  
Poniekąd, ale nie nie do końca.

**Janusz Bossak** 8:25  
Dobra, to już już zaraz postaram się pokazać.  
Się postaram pokazać.  
Mamy jakiś taki raport?  
Które się nazywają sprzedaż?  
Już nie wiem, która ten sprzedażą.  
Chyba tutaj o to jest świetny przykład na to nie.  
Legenda po prawej stronie.  
Pokazuje a mod BIRP prog, bo takie występują tutaj na tym nie, ale field pokazuje, a młody tb i.  
A jak wpisze ER?  
No wiesz, no.  
Ale jak tak zrobię to nie ma i to jest pierwsza rzecz do poprawienia. Po prostu tak Legenda jest tutaj nie ma.

**Mateusz Kisiel** 9:25  
Dziwi mnie, że teraz to wyszło, bo to raczej było testowany, pojawiają się coś wcześniej wyjść, myślę, że to mogło działać kiedyś.

**Janusz Bossak** 9:31  
Ale to sprawdziliśmy za nią w którymś momencie i chodzi o to, że w pierwszych 20 wynikach.

**Mateusz Kisiel** 9:39  
Tak, tak.

**Janusz Bossak** 9:40  
Ale nie agregatach tylko danych źródłowych jest a mody i BIAR się pojawia dalej niż pierwszych 20. Nie.

**Mateusz Kisiel** 9:42  
Wiem.

**Janusz Bossak** 9:51  
No i to jest pierwsza rzecz na backendzie do poprawienia, tak, żeby to się tutaj.  
Przynajmniej pojawiało tak, skoro na legendzie jest to.  
Że to jest, to jest zupełnie dla użytkownika niezrozumiałe, tak.  
Która raport wie o tym, a tutaj nie wiem.  
No i takich kilka naście mam różnych mniejszych większych rzeczy i bym chciał Przemek z tobą po prostu popracować, a tutaj w niektórych przypadkach jak ten poprosić Mateusza o to, żeby Mateusz tam na backendzie, no jakieś tematy poprawił.

**Mateusz Kisiel** 10:25  
Znaczy tak jak mówię, to jest przypadek. Właśnie też dla frontendu tak, czyli trzeba po prostu wysłać w ri queście definicję raportu, która dodatkowo jeszcze robi distinct ta na na.  
Czyli wartości w tym momencie po prostu jest w pełni przesyłane, jakby w takiej postaci jak w tabeli jest na przykład i proste jakaś pagina co się może zwalcza.

**Janusz Bossak** 10:43  
No tam jest chyba na siłę wpisane 20.

**Mateusz Kisiel** 10:47  
Być może? No to jest możliwe.

**Janusz Bossak** 10:50  
Tylko, że nie 20 pod, bo to powinien być select distinct coś tam coś tam.

**Mateusz Kisiel** 10:55  
Dobrą zobaczę teraz.

**Janusz Bossak** 10:57  
U mnie to jest na backendzie nie na frontendzie.

**Mateusz Kisiel** 10:59  
Przyczyną jakby backend zwraca to co o co poprosi prąd.

**Przemysław Rogaś** 11:06  
Znaczy, no to jest tego co ja rozumiem, no to to ma sens jedynie dla tam gdzie jest drabina pagina jak tabelę, a tak to nie powinno w ogóle być żadnego limitu.

**Janusz Bossak** 11:16  
Tak samo tutaj.

**Mateusz Kisiel** 11:16  
Znaczy, myślę, że nawet nawet dla tabel chyba nie ma sensu. Wydaje mi się.

**Przemysław Rogaś** 11:22  
No fakt, no no, bo będziesz szukał tylko po jednej stronie, no no to to bez sensu.

**Mateusz Kisiel** 11:33  
Teraz.

**Przemysław Rogaś** 11:48  
No ogólnie takie zadania ja bym zgłaszał najpierw na prąd ten TI na przykład jeżeli ja stwierdzę, że to jest jednak na backendzie no to wtedy ja zgłaszam to na bank nie żeby.

**Janusz Bossak** 11:59  
No dobra znaczy ja mam tam listę.  
Na razie takich znaczy inaczej mamy listę takich.  
Józka słów spisanych, które jeszcze nie są tb a jajami na tym na blogu.  
Ale bym tak chciał pracować z tobą bardziej, że tak powiem dynamicznie, znaczy więcej mówić są o co mi chodzi i po kolei byśmy sobie tam.  
Rzeczy naprawiali będę to też starał się tam spisywać oczywiście na backlog. Tam jest taki robiony epic do tego i tam będę podpinał te wszystkie rzeczy związane z naprawą tych kwestii tutaj związanych z tym filtrami użytkownika nie, bo to one są i tutaj po stronie.  
Już używania i też będą po stronie tutaj nie nie.  
Tworzeniem.  
Ich.  
Na przykład domyślne różne tam tutaj ustawienie wartości domyślnej, jakieś takie, no to tam drobne takie.  
Tematy.  
I coś tam sprawdziłeś, Mateusz?  
I coś wycięło Mateusza.  
Wziąłem się podział.

**Mateusz Kisiel** 13:34  
Halo.

**Janusz Bossak** 13:36  
Coś się wycięło tak się sam dołączyłeś.

**Mateusz Kisiel** 13:37  
No właśnie nie mam internetu w laptopie z jakiegoś powodu nie wiem, chyba wijący się nawala, nie ma. Zresztą u was to działa, więc to dziwne.

**Janusz Bossak** 13:40  
A ok.

**Mateusz Kisiel** 13:43  
Telefony się teraz łączy.  
Halo.

**Janusz Bossak** 13:54  
No słychać wycie.

**Mateusz Kisiel** 13:56  
Dobry działa.  
Dobra sprawy i wyłączyć to.  
Dobra jest najlepiej.  
Nie mówi się nic.

**Przemysław Rogaś** 14:51  
Trochę słabo cię słychać, wiesz?

**Mateusz Kisiel** 14:54  
O k. Teraz lepy.

**Janusz Bossak** 14:57  
No tak.

**Przemysław Rogaś** 14:58  
Wrażenie, ale cicho.

**Mateusz Kisiel** 15:00  
Dobra, teraz są te Pradze, ale mogę pokazać tutaj to miejsce, gdzie są pobierane te wartości.  
Jest tutaj funkcja juz posible vous.  
Ja na pobiera możliwe wartości tej przesyłamy definicję, jakby takiego nowego raportu tymczasowego, z którego są, na podstawie którego są brane te dane, tak i tutaj widzimy, że jest ustawiony ten limit na 20.  
I jest film type value.  
To być może właśnie trzeba by tej dołożyć tam agregację żeby.  
Mm żeby.  
Okej, gdy jest już segregacja polu?

**Janusz Bossak** 15:42  
Ale to on wie, że dane, które już są po stronie frontendu, tak.

**Mateusz Kisiel** 15:46  
Nie, nie, to są dodatkowe zapytanie do backendu jakby dodatkowe takie mini raport na potrzeby na potrzeby tego, co będzie w tym okienku z wyborem w polu tak, czyli tak jak miałaś te 2 wartości, to były 2 wartości zamiast zamiast 4 ponieważ.

**Janusz Bossak** 15:59  
No co ty?

**Mateusz Kisiel** 16:07  
Ponieważ ten limit 20 wziął tylko 20 elementów, no i znaczy, no w tym tymczasowo na przykład pani by zadziałało, jakby zrobić coś tego typu, żeby tutaj zrobić.  
Mm zrobić jakiegoś.

**Janusz Bossak** 16:20  
Discount.

**Mateusz Kisiel** 16:21  
Na jakieś min. Pewnie tak, bo to.  
Znaczy no nie, no nie zaraz, no to trzeba by zobaczyć jeszcze nawet w momencie. Tak nie dziwi. Mnie to jest ten sposób robiony.

**Janusz Bossak** 16:34  
Znaczy, no to będzie taki, że są pojedyncze wartości, tak?

**Mateusz Kisiel** 16:37  
Znaczy no discount to zrobi ilość, będzie liczyć wartości.

**Janusz Bossak** 16:44  
A bo sting mi chodziło o to, żeby.

**Mateusz Kisiel** 16:44  
No tak.  
Tak, ale tutaj tutaj w tym momencie wpadłam, że distinct się robiło po prostu gorąco mina czy maksa coś takiego.  
No bo jak się bierze minał to wtedy jakby on automatycznie te same wartości.  
Chociaż też tylko się inaczej, no bo musimy zobaczyć jak to się robi.

**Janusz Bossak** 17:05  
No to to to trzeba będzie poprawić na pewno tutaj.

**Mateusz Kisiel** 17:18  
Tak gdybać, że jest robiony po stronie frontendu tak i przez to, że jest po stronie front endu a nie po stronie tego backendu. No to biorąc 20 wartości tylko ty.  
Tylko 2 ślicznie powtarzają.

**Janusz Bossak** 17:34  
Mhm.

**Mateusz Kisiel** 17:34  
No to jest ten problem.

**Janusz Bossak** 17:36  
K.

**Przemysław Rogaś** 17:37  
Czyli ten limit 20 to nie jest na limit rekordów, powiedzmy wy raporcie tylko to jest faktycznie limit tych elementów filtrach.

**Mateusz Kisiel** 17:46  
No limit ten limit 20, które w tej ustawie? No to jest limit, który idzie do backendu i backend bierze 20 elementów i potem dodatkowo jeszcze dyskutowane po stronie frontendu. No i przez to jest to jest problem, ponoć to dyktowany po stronie pkm du. Czyli to trzeba zobaczyć jak to, no.

**Janusz Bossak** 17:56  
To jest problem ten.  
A zobacz, możesz zobaczyć, jakie zrobione Legenda, że Legenda ma 4 wartości.  
No to jest z tym sam przypadek. Nie to jest dokładnie ten sam.

**Przemysław Rogaś** 18:12  
Ogólnie Legenda chyba też jest źle zrobiona na przykład dla tabel, bo Legenda jest brana pod uwagę na podstawie danych, które są na frontendzie nie, czyli na przykład jak masz pierwszą stronę otwartą w tabeli to bierze tylko dla pierwszej strony później jak włączysz drugą to ci się zmieni Legenda z tego co powiem.

**Janusz Bossak** 18:31  
No.

**Mateusz Kisiel** 18:31  
Raczej to prawdopodobnie Legenda. Wiesz, po prostu dane z raportu tak, czyli jak powiedzmy w raporcie mamy kiedyś dany już wy raporcie to bierze dane z raportu, czyli jak mamy jakąś tabelkę to będzie brało tylko z tej otwartej strony.

**Janusz Bossak** 18:44  
No no no tak jak Przemek mówię, no no to też nie dobre rozwiązanie.

**Mateusz Kisiel** 18:46  
No.

**Janusz Bossak** 18:51  
No też niedobra.

**Mateusz Kisiel** 18:52  
No trzeba to będzie ujednolicić wszystko pewnie.

**Janusz Bossak** 18:57  
Znaczy.  
Bardzo nieeleganckie, a proste rozwiązanie to zamiast 20 pisać 200 i liczyć, że w pierwszych 200 będzie więcej.

**Mateusz Kisiel** 19:07  
No nie, no nie?  
To.

**Przemysław Rogaś** 19:11  
A nawet jak jest 20 do da się to potem doładować jakoś jak chcesz więcej zobaczyć.  
Czy czy nie?

**Mateusz Kisiel** 19:20  
Nie tutaj w filtrach nie ma takiej opcji do chociaż nie no zaraz, bo tak, bo mamy tego scrolla takiego wydaje mi się, że jak się tym skrotem scrolluje w dół to chyba się ładuje więcej tych wartości i o ile kojarzę.  
Chociaż nie może nie.

**Janusz Bossak** 19:34  
Nie, nie.

**Przemysław Rogaś** 19:35  
Trzeba wyszukać chyba co.

**Mateusz Kisiel** 19:35  
Nie.  
Trochę trochę wyszukać rzeczywiście na.

**Janusz Bossak** 19:37  
A wpisał dopiero jak wpiszesz ten rp mało tego jak go wpiszesz.  
No to on się wyszuka, ale znikają mi wtedy ten bije i ja modnie, czyli ich nie widzę. Widzę tylko ten, który znalazłem.

**Mateusz Kisiel** 19:49  
No tak tak no to jest do poprawki tego dystryktach nie można tutaj robić po stronie frontu.

**Janusz Bossak** 19:57  
No dobra, to trzeba tutaj wymyśleć jak ten.  
20 unikalnych wartości dostać to będzie pierwsza taka poprawka. Także to spokojnie możesz już sobie.  
Zaplanować pracę nad tym, żeby to.

**Przemysław Rogaś** 20:12  
Ale tutaj chyba Mateusz to weźmiesz co całość.

**Mateusz Kisiel** 20:15  
Yy to tak, ja to zrobię, no.

**Janusz Bossak** 20:19  
Dobra.  
Dobrze i teraz tak co ja tu sobie rozpisałem, teraz wam pokażę, tylko muszę uruchomić tego mojego.  
Sora.  
Mam tych przypadków życia sporo.  
Już pokazuje ekran.  
Jesteśmy tutaj.  
No i tu mam różne przypadki użycia rozpisane.  
Jakoś tam gadam z nimi, on tutaj elegancką i te przypadki.  
Użycie rozpisuje.  
Yy także to powstawiam do tych naszych.  
I będziemy na podstawie tego mogli.  
Pracować tak, czyli wiadomo będzie co jest do zrobienia.  
Yy, o tutaj jest na przykład tam Filtrowanie krótkiej listy, Filtrowanie długiej listy. To jest to między innymi, o czym teraz rozmawiamy.  
Obsługa tego zaznacz wszystko, bo to też działa w tej chwili.  
Po prostu źle.  
O zaznacza wszystko, jeżeli jest więcej niż 20, to nie znaczy zaznacza 20. Tak i użytkownikowi się wydaje, że zaznaczył wszystko, a zaznaczył wszystko owszem, ale wszystko 20, czyli tam powinno być napisane w tym momencie zaznacz widoczne, jeżeli jest ich więcej niż 20.  
I to jest tutaj opisane, jak to powinno działać.  
Yy, tutaj mamy wybór operatora tekstowego, że będą domyślnie, żeby był ustawiony też na zawiera, nie.  
Bo.  
No tekstowo tak powinno działać, ale właśnie przed chwileczką ta rozmowa, która była na tej Radzie deweloperów. No trochę zmienia to moje podejście.  
Piotr, mocno tam nazwijmy to nakrzyczał od strony wydajnościowej.  
Yy, no bo musimy zrobić właśnie to indeksowanie tak żeby można było po tym polu generalnie tekstowym właśnie wybierać.  
Nie zabijając bazy danych, ale to zostawimy sobie na później.  
O tym mamy tutaj.

**Przemysław Rogaś** 22:47  
Jestem wrócić do tego zaznacz wszystko jeszcze, bo w jakim kierunku pójdziemy? Mam wrażenie, że efekt zaznacz. Wszystko będzie taki sam efekt, jak nie zaznaczenie niczego.

**Mateusz Kisiel** 23:00  
Znaczy zmiana chyba tekstu to znaczy widoczne, tak.

**Janusz Bossak** 23:04  
Tak powinno być pewność widoczne.

**Przemysław Rogaś** 23:05  
A o k dobra.

**Janusz Bossak** 23:10  
Ja tam wam te dostęp do tego, żebyśmy mogli to je sobie to przeglądać. Potem jest tam odnośnie daty, to tutaj jest dużo takich rzeczy do uporządkowania.  
Ponieważ teraz jak pamiętacie, mamy tych?  
Operatorów na dacie dużo tak są takie operatory nazwijmy to jawne, czyli bieżący miesiąc. Poprzedni miesiąc bieżący rok poprzedni rok.  
Tego typu rzeczy, które nie muszę żadnej daty wybierać, tylko to określa już jednoznacznie nie i one punktu widzenia biznesowego są ważniejsze, tak, one powinny być jako pierwsze, bo najczęściej Użytkownik będzie właśnie wybierał. Wiem w zeszłym miesiącu w tym miesiącu bieżącym miesiącu, poprzednie 30 dni, poprzednie 90 dni i tak dalej.  
A dopiero później niżej dla bardziej zaawansowanych będzie nie wcześniej niż jakiś dzień do wpisania nie później niż jakiś dzień. To wpisanie to już jest dużo trudniejsze i będzie dzięki temu niżej, tak.  
Czy jakieś tam zakres zawiera od daty do daty? Tak? No to już są bardziej wyrafinowane, że tak powiem rzeczy, no i to jest tylko uporządkowanie jakby kolejności, nadanie odpowiednich nazw do tego i już będziemy mieli te operatory.  
Daty tutaj ogarnięte, tak tutaj jest on gdzieś to jest opisane wszystko tych latach właśnie nie. O tutaj. Dzisiaj wczoraj nie wcześniej niż dzisiaj nie później niż dzisiaj. Ostatni tydzień poprzednie 7 dni powszednie, 30 bieżący tydzień miesiąc rok tak dalej nie.  
I to to jest pierwsza rzecz, na którą można uporządkować i i już tak i będzie nie wiem czy tam mamy coś takiego jak ten tydzień.  
Możemy zrobić bez tego tak tylko ostatnie 7 dni i tak dalej. Tak samo tutaj ten bieżący tydzień, aczkolwiek jeżeli by się dało, no to można by też.  
Yy to zrobić. Potem mamy ten komunikat o wymaganych filtrach, to jest też to Przemek do ciebie tutaj trochę jako jurix owca trochę.  
Bo to próbowałem to ogarnąć. Chodzi o to, że mamy ten tak tak zwany empty stein. Screen, tak.  
Czyli sytuację, w której nie ma danych, albo wymaga sytuację, w której wymagane jest podanie filtrów? Nie.

**Przemysław Rogaś** 25:34  
Mhm.

**Janusz Bossak** 25:40  
Yy, bo teraz mamy te filtry wymagane no i żeby wyświetlić cokolwiek no trzeba coś podać nie i to musimy się zastanowić jak to ładnie zrobić wizualnie, żeby to jednak tego użytkownika informowało, że podaj najpierw na przykład tam nie wiem obszar albo projekt, albo coś, żeby w ogóle cokolwiek zobaczyć. No więc nad tym bym chciał, żebyśmy popracowali.  
I coś co się jakby z tego wyniknęło z tego myślenia, ale nie jest bezpośrednio związane z filtrami użytkownika, to jest w ogóle ogarnięcie tych empty screenów. Empty screenów dla wszystkich typów raportów. Tak, czyli wchodzimy, mamy raport tabelarycznym, ale nie mamy danych i w tej chwili mamy wypisuję na środku brak danych i koniec i pusty ekran. Nawet nie wiadomo jaki to jest raport.  
I to jest zresztą.

**Przemysław Rogaś** 26:30  
Ale masz jakiś pomysł na to, bo na przykład tam kristina dostarczyła te ilustracje, to to można użyć. One są na innych widokach używane.

**Janusz Bossak** 26:39  
Tak, no albo możemy takie ilustracje, albo takie nie wiem okopowe, jakby znaczy, żeby coś było tylko puste. Tak na przykład nie wiem.

**Przemysław Rogaś** 26:39  
Więc no.

**Janusz Bossak** 26:50  
Wykres, który ma jakieś tam jest pusty, trzeba by się zastanowić, p każdy typ tego nie mam tu jeszcze odpowiedzi na to z tabelką jest najłatwiej tak no bo tabelkę to można kolumny wyświetlić, nawet jak nie ma danych.  
I napisać tam w pierwszym wierszu brak danych nie.  
Yy no i zachęcić na przykład do akcji jakiejś, bo jeżeli jest to raport, w którym u góry jest przycisk tam Dodaj nowy.  
To mogłoby być to na środku ekranu? Nie?  
W tym raporcie nie masz jeszcze żadnych danych?  
Myślałam, wprowadź pierwszego, nie wiem członka rodziny na przykład albo tam wprowadź pierwszą umowę, wprowadź pierwszy tam pierwsze zadanie czy coś takiego no.  
Więc ten nad tym empty screenami, byśmy musieli popracować chwilę i tutaj się odwołam też do Twojej, że tak powiem wyobraźni i umiejętności projektowania ładnego.  
Yy no także jak widać jest tego tutaj ileś tam po tym dzisiejszym spotkaniu z Piotrem postaram się tu jeszcze dopisać kolejne.  
Już kejsy żeby się mieli komplet tego.

**Mateusz Kisiel** 28:01  
A ten raport, który pokazywałeś to jest jakiś na witrynie testowej czy na mazdach orzech?

**Janusz Bossak** 28:01  
Także.  
Jeśli nie, to na strefom się jest na strefach się się nazywa sprzedaż 2025 per prod. Ale nie wiem komu jest udostępniony dla wybranych osób. A Urszula.

**Mateusz Kisiel** 28:15  
No dobra, dobra, to nieważne, chciałem zobaczyć czy będzie nawet tej testowej. No tak, rzeczywiście no nie ma, nie ma opcji dodania distinct, więc trzeba to dołożę się do pkn do rzeczywiście.

**Janusz Bossak** 28:24  
O k.  
No to rozumiem, że w tym to co pokazywałeś tam w tym wierszu gdzie jest to agregacja tak to tam listing i trzeba.

**Mateusz Kisiel** 28:34  
No będzie dodatkowa opcja właśnie łączenia listing gta.

**Janusz Bossak** 28:39  
Na weekendzie wtedy distinct zwraca te wartości no i o k.  
No dobra, słuchajcie, to na razie tyle. Ja będę sukcesywnie tutaj przerzucał te rzeczy do.  
Yy do tego backlogu trzonek, co co byś potrzebował ode mnie teraz zacząć coś robić.

**Przemysław Rogaś** 28:57  
No jakieś pierwsze zadanie, nie, jeśli nie masz rozpisanych tych, no to pewnie są jakieś błędy, które tam trzeba poprawić, no cokolwiek zrobienia.

**Janusz Bossak** 29:07  
Dobra, to teraz będę wrzucał ci zadania. Zacznijmy od porządkowania tego pola. Data nie żeby.

**Mateusz Kisiel** 29:10  
Na tą.

**Janusz Bossak** 29:14  
Z tymi nazwami, bo to jest akurat tylko i wyłącznie robota po stronie frontendu.

**Mateusz Kisiel** 29:19  
Na tę poprawkę z tym filtrem zrobić jakiegoś baga, tak?

**Janusz Bossak** 29:23  
Tak, to chyba nawet jest. Wiesz, poczekaj zaraz to już tyle było tych rzeczy.

**Mateusz Kisiel** 29:24  
Dobra.

**Janusz Bossak** 29:31  
Gdzie ja tutaj mam develop tutaj uroczym moduł?  
W budżecie nie.  
No ja nie mam go zidentyfikowanego, więc możliwe, że nie ma.

**Mateusz Kisiel** 29:51  
No to jest, robię nowego, jak się powtórzy się po prostu usuń tego pierwszego.

**Janusz Bossak** 29:54  
Jak go znajdziemy? To tak.  
I podepnij go pod numerek 20 153.

**Mateusz Kisiel** 30:02  
20 153, okej?

**Janusz Bossak** 30:04  
To jest taki ficzer ogólny ulepszanie filtrów użytkownika.  
Żeby mi tutaj nie zginęło, to nie.  
I tu po tym właśnie ulepszanie filtrów użytkownika będę podpinał też te zadania. Przemek dla ciebie nie.

**Przemysław Rogaś** 30:20  
Dobra.

**Janusz Bossak** 30:22  
O k no dobra, no to tyle. Na razie dzięki bardzo.

**Mateusz Kisiel** 30:27  
To dzięki cześć.

**Przemysław Rogaś** 30:28  
Na razie dzięki.

**Janusz Bossak** zatrzymano transkrypcję
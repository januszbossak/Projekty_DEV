**Transkrypcja**

2 października 2025, 08:01AM

**Lukasz Bott** 0:13  
Raz jeszcze nie wiem czy coś mam, bo to znaczy tak może inaczej nie mamy nic, no bo przynajmniej ja oznaczonego nie.

**Damian Kaminski** 0:21  
O k no dobra, to pytanie czy nie wiem.  
Cóż, mamy nie oznaczonego aniu, czy ty masz jakieś tematy?

**Anna Skupinska** 0:30  
Specjalnie ciągle pracują nad tymi danymi.  
Znaczy, oczywiście później będzie trzeba się zająć moje sequelem, bo znaczy tak jak jak to jest z tym.  
Wczoraj rozmawiałam z tobą.  
Łukasz, to uznaliśmy, żeby zrobić poprawki dla MS quaara później.

**Lukasz Bott** 0:53  
Znaczy tak tak, chodzi o to, żeby nie wstrzymywać praca.  
Ten tam jest problem jest generalnie jest stworzeniem.  
I źródeł systemowych.  
Damy ze sql tak w przypadku by one są.

**Anna Skupinska** 1:07  
Dziewczyno nie tylko źródeł systemowych, chodziło też o ogólnie rzecz biorąc są źródła lokalne, które są integracyjne.

**Lukasz Bott** 1:12  
No właśnie tych typu lokal tak no no bo online nowe się tworzą tak i to nie ma problemu.

**Anna Skupinska** 1:14  
Tak.  
Mhm.

**Lukasz Bott** 1:18  
A tam w tym nowym, w tym nowym podejściu w module raportów systemowych, no pojawiło się po.  
Miłość i kilka nowych źródeł.  
Zewnętrznych, które są właśnie synchronizowane.  
Yy.  
Tam no raz dziennie tak to, bo to obchodzi o statystyki na ogół o charakterze dziennym, więc żeby nie obciążało to online owo połączeń i tak do bazy danych, no to po prostu tam są pewne agregaty robione. No i tu okazało się, że.  
Że o ile dla majes sku. Ela mm.  
Jakoś nie ma problemu z tworzeniem tego typu źródła.  
Lokalnych to w przypadku bazy mssql jest tam jakiś problem, no to ania musi to rozwiązać, ale żeby pracy nie wstrzymywać jakoś tak no to w pierwszej kolejności niech ogarniemy ten tego majewską ela, a potem zajmiemy się sql Server.  
Jakieś takie jest Plan działań?

**Damian Kaminski** 2:14  
Spk.

**Janusz Bossak** 2:14  
A także tych tych raportów systemowych też borków systemowy. Jak ktoś to zaczęło wyglądać.

**Lukasz Bott** 2:21  
Wysłałam.

**Janusz Bossak** 2:22  
Czy możecie pokazać coś z tych dashboard w systemowych?

**Lukasz Bott** 2:26  
Tak no to mogę tylko gaźnik.

**Anna Skupinska** 2:27  
Znaczy no niespecjalnie, chyba, że kod się liczy.

**Janusz Bossak** 2:28  
Po co niespecjalnie.

**Lukasz Bott** 2:29  
Nie nie, no to to znaczy ta moment moment dashboard są porobione tak i ania będzie musiała ta przenieść w tryb systemowy. Tak no i to jeżeli mamy teraz chwilę czasu, mogę to pokazać tak, no.

**Damian Kaminski** 2:44  
Że no, bo tak no bo nie omawialiśmy ani razu, co tam jest, nie w sensie.

**Anna Skupinska** 2:44  
Aha, w ten sposób.

**Lukasz Bott** 2:49  
Ja tak ja też konsultowałem to z danielem reszko w kontekście takich ich zapotrzebowań klientów, więc to też tam niektóre zmiany. Wprowadziłem, tak no.

**Damian Kaminski** 2:53  
Mhm.

**Janusz Bossak** 2:59  
A czy to jak to?

**Lukasz Bott** 3:01  
Mogę to na szybko pokazać, jeżeli słyszycie jakieś głosy w tle, to znów Michał Maliszewski jest wyjątkowo głośny, a ściany mamy z dykty.  
Czekaj się, muszę się podłączyć?  
I jest takie proste.  
Yy.  
Chwilą.  
Wyglądać?  
Dobra.  
Piotr omawiamy ten.  
Omawiamy raporty systemowe, te, które gdzieś tam nawet stworzyłem. Tak więc.  
Jak chcesz, to możesz zostać, bo rady jako takiej nie ma tematów przynajmniej pilnych.  
Raporty smogu. Aha dobra już zauważyłem, że pojawiło się tutaj w tym prawym menu modułów systemowych Link do raportów systemowych, czyli można przejść, aby standardowo czyli do tej zakładki, która była.  
Raporty systemowe tak tego folderu, albo po prostu z tego.  
Judasz z nas przenosi do do do tych do tego.  
Do tego moduł raportów systemowych, tak.

**Damian Kaminski** 4:42  
Mhm.

**Janusz Bossak** 4:43  
A one też poczekaj, bo teraz.

**Lukasz Bott** 4:43  
I to.

**Janusz Bossak** 4:47  
Dobra raporty, system ERP o k. Czyli po prostu nas przenosi do zakładki znaczy do system.

**Lukasz Bott** 4:51  
Tak, tak, tak, tak są 2 ścieżki albo.  
Albo standardowa raporty i system Report i to się nie zmieniło.  
Albo dorzuciliśmy.

**Janusz Bossak** 5:06  
Rozumiem.

**Lukasz Bott** 5:06  
Link www.tutaj tej diagnostyce, raporty systemowe i od razu nas przenosi do tej zakładki, żeby tego nie trzeba było szukać gdzieś.

**Damian Kaminski** 5:12  
No dobra, ale jest pewna niespójność, że tu mamy po polsku, a tu po angielsku w sensie jest możliwość tłumaczenia, coś tu nie działa, czy po prostu jeszcze tego nie zrobiliście?

**Lukasz Bott** 5:23  
Nie, nie przetłumaczyliśmy chyba tak, no to to jest kwestia tłumaczenie słowników.

**Damian Kaminski** 5:28  
No o k no dobra, ale po prostu, no żeby to było jakoś spójne, to myślę, że to mało pracę, a duży efekt.

**Lukasz Bott** 5:36  
Dobra, to jest, co to ja sobie to zamontuje? Inna może jeszcze dzisiaj to poprawi, tak.  
To jest sens.

**Janusz Bossak** 5:47  
Kiedy się trzymaliśmy tej jakiejś takiej zasady, że dla administratorów to jest po angielsku, ale już dawno zostaliśmy.

**Lukasz Bott** 5:52  
Tak, tak to.

**Janusz Bossak** 5:55  
I tam gdzie można to róbmy to po polsku, tak?

**Damian Kaminski** 5:59  
No tak, no interfejs przecież ustawień systemowych też zrobiliśmy po polsku, może jeszcze niecala to znaczy, sorry, poszczególne elementy jeszcze są po angielsku, ale nie jest po polsku i pewnie trzeba będzie to też wyrównać, nie?

**Lukasz Bott** 6:12  
Tak, to przy okazji wisi, yy przy okazji wisi ten.  
Przy okazji lisi zgłoszenie, że ten brent camp tak, bo tak to się nazywa ten górny pasek tak nawigacyjny.

**Damian Kaminski** 6:24  
Mhm.

**Lukasz Bott** 6:25  
Yy.  
No bo tak mam przetłumaczony, powiedzmy pierwszy z dashboard tak, który sobie obejrzymy czas procesowanie spraw, no to.  
A może dobra ja to jeszcze sprawdzę, bo to może być kwestia, nie nie przetłumaczyłem tych kategorii dobry.

**Damian Kaminski** 6:39  
No to może nie być przetłumaczony.  
Zaraz to wklep przetłumaczę i sprawdzimy, ale to to opowiadać.

**Lukasz Bott** 6:45  
Dobre to jakbyśmy.  
Dobra, to to znaczy tak pierwszy z raportów do przewodów czasu prezesowanie spraw jakieś zestawienie, czyli idziemy według tych.  
Tego podejście, że mamy zestawienie.  
Jakiś średni czas oczywiście dane są z dewelopera, więc tutaj wychodzi taka trochę mozaika.  
Też często procesowania spraw to są tak tutaj Daniel zwrócił uwagę, że tego nie implementowała em do zastanowienia się, bo wrzucił taką uwagę, żeby na przykład zrobi.  
Idź.  
Żeby na takim dashboard się wyświetlać na przykład go podzielić na takie, które są trwają dłużej niż 2 dni albo krócej niż 2 dni. Tak no bo pewnie te, które są dłużej trwają niż 2 dni. No to w praktyce. Pewnie to oznacza, że ktoś gdzieś coś komuś wisi. Tak.

**Janusz Bossak** 7:45  
No dobrze, średni czas procesowania spraw to.

**Lukasz Bott** 7:45  
No i też.

**Janusz Bossak** 7:49  
Od czego nasze? No otworzenia rozumiem sprawy do czego do zamknięcia sprawy, czy do jakiego mam?

**Lukasz Bott** 7:55  
To jest to jest brane z klasy historia.  
Czyli tak jak jest to systemowe liczone.

**Damian Kaminski** 8:03  
Ale tutaj kolejne zgłoszenie właśnie powinno być to opisane nawet na podstawie tych waszych, gdzieś tam może zapytań, czy chociaż tutaj przebijaja tak w sensie, że mamy tą opcję chyba już znaczy nie chyba tylko po prostu mamy wyświetlania opisu.

**Lukasz Bott** 8:04  
Ta sprawa.

**Damian Kaminski** 8:21  
Raportu i to też jest może nie na vip, ale jako kolejny rozwój.  
Żeby móc przeczytać strony, raport przedstawia nie.

**Lukasz Bott** 8:32  
Tak tylko.  
Dobra.

**Damian Kaminski** 8:37  
Nie, nie, ja nie mówię, że to teraz musi być do tego już wydania nie, ale.

**Lukasz Bott** 8:37  
Opisy na nie, ale co innego jest chyba błąd po prostu opisy raportu czy dashboard to się nie po prostu nie zapamiętają, bo nie zapamiętują, pomimo także się wprowadza.  
To zgłosi jako.

**Damian Kaminski** 8:54  
Dashboard ów czy raportów dashboard dach.

**Lukasz Bott** 8:57  
I jednego chyba i drugiego.

**Damian Kaminski** 8:57  
W sensie?  
O k. Możliwe.

**Lukasz Bott** 9:00  
No i pytanie gdzie to się powinno pojawić tutaj pod znakiem zapytania?

**Damian Kaminski** 9:03  
No według mnie nie według mnie powinno się pojawić i gdzieś to z kimś dyskutowałem tutaj przy filtry i odśwież. Jeśli już ustawiony to raczej tu powinno być albo tak jak Legenda się wyświetla już wewnątrz tutaj w prawym górnym rogu samego raportu, to może tu powinniśmy dać pokaż opis, tak.

**Lukasz Bott** 9:14  
Dobre.

**Janusz Bossak** 9:26  
Byłoby dobre.

**Lukasz Bott** 9:26  
No myślę, że tutaj tak, żeby tu tu tu literkę i tak nie czytam znak zapytania i ty klikam i się pojawia czy tam właśnie jako turki czy po prostu.

**Damian Kaminski** 9:26  
Może?  
Dokładnie i w kółeczku tak jak.  
Mhm, możesz odświeżyć całość teraz ekranu w sensie całą.

**Lukasz Bott** 9:42  
Bo moment.

**Damian Kaminski** 9:42  
Stron całą stronę, bo przetłumaczyłem zobaczymy sobie tą ścieżkę.  
Powiedziała, no dobra.

**Lukasz Bott** 9:52  
Na pewno ten proces jest.

**Damian Kaminski** 9:55  
Tak, tak, tak, tak, tak, tak, tak przetłumaczyłem jeszcze sprawdzam na deweloperskie, a dobra nie na tym deweloperskie. Dobra dobra, tak, tak tak teraz przetłumaczę.

**Lukasz Bott** 10:02  
Dewelopment skóra monitorowe to może na następne wspólne.

**Janusz Bossak** 10:06  
No dobrze.  
Ale wracam z pytaniem, średni czas procesowania spraw.  
Co to pokazuje?

**Damian Kaminski** 10:14  
Czy to jest po prostu startu do zamknięcia sprawy? To jest pytanie tak, bo to przychodzi do do głowy.

**Janusz Bossak** 10:17  
No.

**Lukasz Bott** 10:18  
Od startu do do tego mam do teraz.

**Janusz Bossak** 10:20  
Warto do teraz.

**Damian Kaminski** 10:23  
To teraz.  
No właśnie.  
Czy to teraz jest prawidłowym podejściem, bo do teraz?

**Janusz Bossak** 10:27  
No właśnie to.  
Bo to nie jest.

**Piotr Buczkowski** 10:30  
Znaczy, nie ma sensu, trzeba tylko na zamkniętych spraw sprawdzać.

**Damian Kaminski** 10:33  
No właśnie.

**Piotr Buczkowski** 10:36  
Zakończonych.

**Damian Kaminski** 10:36  
Bo.

**Piotr Buczkowski** 10:38  
Bo to będzie obniżyło, będzie będzie obniżało.

**Damian Kaminski** 10:38  
Też bym był za tym.

**Janusz Bossak** 10:40  
Dlatego.

**Piotr Buczkowski** 10:42  
Wynik.

**Janusz Bossak** 10:42  
Dlatego dlatego właśnie się o to bardzo dokładnie dopytuję, bo trochę rozumiem, jakby jak to działa. Tak, jeżeli bierzesz skates history.

**Lukasz Bott** 10:52  
Mhm.

**Janusz Bossak** 10:53  
To tam nie ma ostatniego.  
Stanu ostatni stan jest w klatce definition.

**Damian Kaminski** 10:57  
Wpisu.

**Janusz Bossak** 11:01  
Czyli to jest do momentu przejścia na poprzedni etap, jaki było?

**Lukasz Bott** 11:10  
No tak, zgadza się.

**Janusz Bossak** 11:11  
No właśnie więc.  
Patrzmy na to biznesowego punktu widzenia, co to mi daje?  
Znaczy ja jako Użytkownik.  
Jestem zainteresowany tym, jak długo działają sprawy.  
Tak.  
W jakimś procesie.  
Tak, może byśmy wzięli sobie jakiś konkretny prosty, bo jak się patrzy na wszystko to tak bajzel trochę nie, ale jakiś proces mam obieg faktur no i teraz.  
Zakładając biznesową, że ostatnim etapem.  
Jest księgowość i załóżmy dla naszych celów w księgowanie przebiega wyjątkowo długo kilka dni.  
A wszystkie etapy, wcześniejsze zarejestrowanie faktury, tam ocr, jakieś opisy merytoryczne. Załóżmy, że trwają szybko. Tak jesteśmy na etapie księgowość.  
To co ten raport pokaże, pokaże nam.  
Jaki był czas wszystkich spraw, obojętnie czy otwartych, że zamknięty? Ja mówię o tym teraz, który pokazujesz wszystkie do momentu, kiedy sprawa wskoczyła na księgowość.

**Lukasz Bott** 12:18  
Tak, tak.

**Janusz Bossak** 12:24  
I teraz siedzi na tej księgowości dzień drugi, trzeci, piąty dziesiąty. Załóżmy tu się nic nie zmieni.  
Włącz ciągle patrzy w tej historii, a nie zmieniła się sytuacja tej sprawy, bo jej nie zamknięto. Sprawa nie poszła dalej, jest na tym, więc nie wiem naprawdę.  
W odniesieniu do wszystkich spraw, jeżeli tak patrzymy, nie nie tylko zamkniętych, czyli również tych toczących się, jak to długo trwa.  
Według mnie pytania trzeba sobie postawić takie jak stawia sobie Użytkownik tak, czyli ile trwają sprawy, ile te sprawy trwają na etapie księgowości, ile te sprawy trwają do momentu zamknięcia i tak dalej, a nie tylko, że technicznie da się wyciągnąć to.

**Damian Kaminski** 13:16  
No ale to właśnie obrazuje, dlatego taka dyskusja jest potrzebna, że może tu jest za mało średni czas procesowania spraw zamkniętych.  
Średni czas procesowania spraw wszystkich.

**Janusz Bossak** 13:26  
Ale jest na rynku.

**Piotr Buczkowski** 13:28  
Wtedy wystarczy wtedy wystarczy jakieś definition.  
Różni dla spraw zamknięty różnica między tak jest.

**Damian Kaminski** 13:36  
No właśnie więc, no słuchajcie, podaliśmy do tego, tak, mamy coś może tylko trzeba zmienić nazwy, co my tu prezentujemy i za chwilę rozbudujemy to jakieś dodatkowe jeszcze elementy nie musimy wydać tutaj od razu 3.

**Janusz Bossak** 13:39  
Dlatego.

**Damian Kaminski** 13:51  
140 raportu wydajmy. Nie wiem kilka pewnych i nazwijmy je dobrze, a potem uzupełnijmy o to, co jeszcze brakuje.

**Lukasz Bott** 13:53  
Pani.

**Janusz Bossak** 14:00  
Tak znaczy, chodzi mi o to, wiecie, żeby nie było takiego.

**Damian Kaminski** 14:03  
Żeby było zrozumienie, co my prezentujemy? Tak.

**Janusz Bossak** 14:05  
Tak takiego poczucia, że coś tam pokazuje ten model, ale właściwie to jest.

**Damian Kaminski** 14:09  
Tylko twórca więc co?

**Janusz Bossak** 14:11  
Pożytecznym, nie, że właściwie niczego się nie mogę z tego dowiedzieć za bardzo, bo nie bardzo wiem, co mi pokazuje Użytkownik, to ci ludzie, nasi klienci, tak, no to patrzą, tak mi się wydaje, przynajmniej nie że.  
Jeżeli mam jakiś proces.  
No to mnie interesuje w tym procesie, jak długo trwają sprawę od początku do końca.  
A w sytuacjach, kiedy to, co jest to, co Piotr powiedział tak, czyli do zamknięcia, a w sytuacjach, kiedy sprawa się toczy.  
No to też mnie to interesuje.  
Po może gdzieś utknęła.  
Tak i chcę to zobaczyć.  
Więc to są chyba 2 różne Stany, nie ten sprawy zamknięte. Tam wiemy, że już się skończyło i to jest o k.

**Damian Kaminski** 14:57  
Mhm.

**Janusz Bossak** 15:00  
A zupełnie odrębnym według mnie tematem analitycznym są sprawy w toku.  
Te, które jeszcze biegną, no bo.  
Chce na przykład je pogonić, chce zobaczyć na których etapach utykają i tak dalej i tak dalej tak jakby.

**Damian Kaminski** 15:14  
No tak, ale to tu może by się przydało. W ogóle jeszcze taka statystyka, ilość spraw, ja nie wiem, może taka jest ilość spraw otwartych w ramach procesów tak jako piwot albo nawet jako taka mapa jak tutaj i wtedy to też obrazuje, że mamy jakiś proces, gdzie tych spraw się toczy dużo i one są wszystkie pootwierane i to rzuca światło czy to.

**Janusz Bossak** 15:38  
No dobra.

**Damian Kaminski** 15:38  
Jest standard, bo mamy tego typu spraw dużo, czy po prostu ktoś ich nie zamyka?

**Janusz Bossak** 15:43  
Znaczy, bo może właśnie pytanie, w którą stronę iść uściślijmy co to pokazuje? Jeżeli to pokazuje skalę z history, to to są.  
W sumie sprawy w toku.

**Lukasz Bott** 15:55  
Wokół do no tak do do do do etapu.

**Janusz Bossak** 15:57  
Do poprzedniego etapu, czyli.  
Nie, nie Przepraszam Łukasza, ale to nie niesie żadnej informacji biznesowej.

**Lukasz Bott** 16:05  
O k dobra.

**Janusz Bossak** 16:09  
Bo nie ma tego ostatniego etapu, który jest w kejs definition.  
I który tu nie jest doliczony, więc to nie bardzo wiadomo co to pokazujemy.

**Damian Kaminski** 16:20  
No dobra, no to nie jest do zaorania tylko do uzupełnia.  
W kontekście nazw tak.

**Janusz Bossak** 16:26  
Znaczy nazw i tego co pokazuje, no bo, bo co co biznesowo, jak to nazwać, żeby pokazujemy wszystkie sprawy do poprzedniego etapu, z wyłączeniem tego, na którym sprawa jest?

**Lukasz Bott** 16:29  
Tam tam.  
Przy czym nie wiemy, na którym etapie jest sprawa, jest tak tutaj.

**Janusz Bossak** 16:44  
Co to pokazuje?  
Jaką to niesie informacje?  
Biznesową.

**Damian Kaminski** 16:52  
No to tylko potwierdza, że ta dyskusja jest potrzebna, że ta, że że musimy właśnie to mówić wszystko i zadać te pytania.

**Janusz Bossak** 17:02  
Dobra, ja czym nagrywamy to tak, to będzie można z tego zrobić.

**Damian Kaminski** 17:06  
Jeszcze jako ciekawostka zwrócił uwagę tak, szary jest tak kontrastowy, że ktoś z dobrym wzrokiem nic nie widzi, a tak i pytanie czemu jedyna Basia jest czarna?

**Lukasz Bott** 17:14  
Mówisz o to?  
Gdzie masz basie czarną?

**Damian Kaminski** 17:22  
W ośrodku w drugim na dole, w drugim rzeczy, w drugiej kolumnie.

**Anna Skupinska** 17:28  
Dla Marka, ale też pamiętam, że pamiętam. Pamiętam, że walczyliśmy trochę z tym i chodzi o to, że on trochę tak sobie automatycznie ustawia te na kolory napisów i czasami nawet mniejszy powiemy ma być napis w tym kolorze to sobie zmienia.

**Lukasz Bott** 17:28  
W sensie etykieta tak.

**Damian Kaminski** 17:29  
No tak.  
Nie, nie, nie, nie, nie.

**Lukasz Bott** 17:38  
Nie, ale to.  
No to słusznie dalej zauważył, bo zauważył ten pomarańczowy i ten pomarańczowy, no raczej to jest ten sam odcień.

**Damian Kaminski** 17:40  
No jak.

**Lukasz Bott** 17:47  
I tu zrobił na biało, a tu zrobił na czarno to faktycznie to raczej tutaj na czarno powinien zrobić.

**Piotr Buczkowski** 17:50  
Ona jest naj.  
Właśnie wszędzie ten klipy są na czarno.

**Lukasz Bott** 17:55  
Tutaj raczej powinien być.

**Damian Kaminski** 17:56  
Znaczy to jest o k, bo one mają tło. Jasne, więc według mnie to jest o k, że są na czarno tylko z jakiegoś.

**Piotr Buczkowski** 18:00  
Tło jest przezroczyste.

**Damian Kaminski** 18:03  
No ale ono jest rozjaśnione tak względem koloru, więc nawet jak najedziesz należą najedź na ciemny niebieski tam masz z prawej strony w drugim rzędzie.  
Tam jest najciemniejszy bym powiedział, no to to jest czytelne dalej.  
No ale też słuszne pytania czy tolpy powinny brać z koloru fillm kafelka natomiast znowu to może nie niekoniecznie Jestem w p. Może powinny być tipy jednakowe wszędzie tak.

**Lukasz Bott** 18:37  
A bo on bierze kolory koparkę no.

**Damian Kaminski** 18:38  
W sensie tu otul tipa nie no właśnie on bierze słowa, no to jest jakiś bajer pytanie, czy powinniśmy go utrzymać czy nie? Według mnie nie krytyczny, bo to akurat jest czytelne, natomiast ten szary, który tutaj jest to no powoduje, że.  
Kontrast z białym napisem jest w ogóle nie nieużyteczny.  
Dobra, no ale to zawsze chyba można zaznaczyć ten tekst, to znowu jest coś co dobrze było nie można.

**Lukasz Bott** 19:06  
Ale co zaznaczyć.

**Damian Kaminski** 19:08  
Tak myszką jakbyś pociągnął to da się to odczytać.

**Lukasz Bott** 19:10  
Nie, nie, to jest takie były jakby obrazek stworzył po prostu i.

**Damian Kaminski** 19:12  
Nie da się o k.  
O k no ale jest walił proces jaki, no to.  
Nie jest to krytyk, że że nie wiadomo co tam jest napisane, no te waluty jako jedyny jest strasznie przetłumaczone.

**Lukasz Bott** 19:26  
Właśnie.

**Damian Kaminski** 19:32  
Dobra, przechodzimy przez pozostałe raporty, w tym boardzie. To to jest minimalny i maksymalny czas, co tak jak to przynajmniej wygląda to jest taka sama.

**Janusz Bossak** 19:36  
Znaczy.  
No pokaż jakie.

**Lukasz Bott** 19:44  
Podobnie wyglądają w sensie konstrukcyjnym, tak natomiast no znów jest ten błąd merytoryczny, tak, no bo bo pobiera jeszce history, tak.

**Damian Kaminski** 19:56  
Nie no o k po prostu taka forma wyświetlania chyba jest bardziej czytelna niż słupkowy, bo tu się da wyświetlić z racji, że mamy 2 wymiary to.  
Może wyraźnie tak nie są te słupki, takie cienkie.

**Janusz Bossak** 20:10  
No ale co kolory oznaczają tutaj?

**Lukasz Bott** 20:13  
Kolory oznaczają tylko.

**Damian Kaminski** 20:14  
Nic.

**Lukasz Bott** 20:16  
No sensy nazwę procesu.

**Damian Kaminski** 20:18  
Żeby nie było wszystko jednakowe.

**Lukasz Bott** 20:28  
Tutaj wymiarem jest w sensie wielkością jest ten.  
Processing tam tak.

**Janusz Bossak** 20:36  
Znaczy trzeba by było według mnie do takiej prezentacji, żeby sposobu prezentacji.  
Wziąć kogoś zbijaja tak tam Michała czy kogoś innego.

**Damian Kaminski** 20:46  
No bo tu jest jeszcze istotne bardzo to, ale na to Janusz.

**Janusz Bossak** 20:48  
Bo to.  
Nie nie, no, bo znaczy ty powiedziałeś, że wolisz tę mapę. Mi się akurat to nie podoba, nie znaczy. Ja nie lubię tej mapy.

**Damian Kaminski** 21:00  
Wolałbyś słupek? Tak.

**Janusz Bossak** 21:01  
Wolałbym sulkowo na sutkowych to widzę tak no.

**Damian Kaminski** 21:04  
Ale co widzisz?

**Janusz Bossak** 21:06  
No że.

**Damian Kaminski** 21:06  
Wartość tak, w sensie masz skalę?

**Lukasz Bott** 21:09  
Czy?

**Janusz Bossak** 21:09  
Chciałem coś łatwiej mi jest porównać jedno z drugim, no.

**Damian Kaminski** 21:12  
O k no dobra to.

**Janusz Bossak** 21:14  
Znaczy, to jest moje odczucie, tak, ja po prostu jakoś nie korzystam z tej mapy. Wiem, że są zwolennicy. W niektórych przypadkach ma ona sens jakieś tutaj.  
Właśnie przez to, że jest kolorowa i ten kolor nie wnosi niczego tak no bo jeszcze gdyby to było tak, że.

**Damian Kaminski** 21:31  
Mhm.

**Janusz Bossak** 21:34  
Kolor to jest liczba spraw na przykład i im więcej jest spraw w danym procesie, tym ten kolor na przykład jest ciemniejszy, że to mógłby być gradient.  
No to wtedy może by miało sens, bo myśmy mieli dodatkową informację, tak byśmy mieli jednocześnie czas.

**Damian Kaminski** 21:48  
Nie zgodzę się.

**Janusz Bossak** 21:50  
I ilość nie.

**Damian Kaminski** 21:51  
Aha, ilość spraw masz na myśli tak kolor byłby ilością spraw.

**Janusz Bossak** 21:56  
Tak.

**Damian Kaminski** 21:57  
O k. Dobra to teraz rozumiem.

**Janusz Bossak** 21:58  
Także możesz mieć proces, który trwa długo.

**Damian Kaminski** 22:02  
I jest tego dużo.

**Janusz Bossak** 22:02  
Ale 5 spraw możesz mieć proces, który trwa w miarę krótko, ale masz 10000 spraw, tak?

**Damian Kaminski** 22:04  
Mhm.  
No to ma sens.

**Janusz Bossak** 22:12  
No więc dlatego mówię, że tu trzeba specjalisty od takiej wizualizacji graficznej.  
Yy, bo to nie tylko wiecie takie.

**Lukasz Bott** 22:24  
Także.

**Janusz Bossak** 22:24  
Nie chodzi o to, że technicznie to jakoś pokazujemy, tylko żeby to rzeczywiście niosło wartość, nie żeby to pa.  
Pisząc na to człowiek dostawał, że tak powiem informację.  
A tu ja nie dostaję informacji za bardzo znaczy tak mi się wydawało dostaje jakieś które.

**Lukasz Bott** 22:38  
Bez opisu jakiegoś tak, no to.

**Damian Kaminski** 22:39  
Poza tym.  
Tutaj ten tutaj jeszcze większe znaczenie wydaje mi się ma te ta kwestia spraw zakończonych, bo tu bardzo dużym przekłamaniem jest to, że jest jedna sprawa, która wisi mega długo. Nie ona pokazuje, że w danym procesie maksymalny czas procesowania spraw jest nie wiem. Od początku instalacja moda bo ktoś uruchomił i zostawił, a de facto ta sprawa jest nieskończona, więc może to bardzo mocno zaburzać filler, bo cała reszta jest produkowana 2 dni, a ta jedna sprawa nie wiem tys.  
Od dni tak przez 3 lata to się nie zamkną.  
Ee więc no tu tym bardziej ten maksymalny czas procesowania powinien dotyczyć zamkniętych.

**Lukasz Bott** 23:26  
K.

**Damian Kaminski** 23:27  
Bo inaczej no to jedna sprawa po prostu zaburza obraz całego wykresu.

**Janusz Bossak** 23:32  
Tak znaczy wydaje się, że to jest chyba kluczowe, żeby powinniśmy pokazywać dla zamkniętych i dla osobno, czyli cały zak znaczy cały zestaw spraw, które są już zamknięte, no bo o nich wiemy już coś, że się zaczęły zaczęły i zakończyły.  
A osobne powinny być raporty czy dashboard nie wiem jak dotyczące spraw w toku, czyli te, które jeszcze trwają, bo.

**Damian Kaminski** 24:00  
No właśnie.

**Janusz Bossak** 24:01  
Ani.

**Lukasz Bott** 24:01  
I wtedy i wtedy by można było faktycznie brać z 2 różnych tabletek. Jak Piotr powiedział, tak, czyli te, które są w toku, to bierzemy skate definition i tam można.

**Damian Kaminski** 24:11  
Odwrotnie.  
Te, które są w toku z history, a te, które są zamknięte skazi definition, bo one mają datę zamknięcia.

**Lukasz Bott** 24:19  
O k dobra.  
Pamięta te zamknięcie?

**Damian Kaminski** 24:21  
Natomiast jeszcze trzecia zakładka ten minimalny czas to w ogóle się zastanawiam, czy w kontekście spraw w toku to ma sens?

**Lukasz Bott** 24:23  
O k to jest.

**Damian Kaminski** 24:30  
Co on, co on wtedy pokazuje?

**Lukasz Bott** 24:33  
Minimalny czasu no.

**Damian Kaminski** 24:37  
W sensie nie mamy zakończenia, więc co on nam pokaże co mi, co jest minimum?

**Lukasz Bott** 24:41  
Nie no to w przypadku toczących się no to byłeś.

**Damian Kaminski** 24:46  
Chyba wtedy to jest do wywalenia z toczących się tak tak to znaczy nie czuję co tu wtedy miałoby być pokazywane, jeśli sprawa nie dobiegła końca.

**Lukasz Bott** 25:00  
Hej dobra, no minimalnym być może jest do wywalenia faktycznie do mnie.  
Maksymalne.  
Albo po prostu.  
Czy to będzie maksymalny? Raczej po prostu czas trwa czas trwania zamknięć zakończą czas trwania spraw, tylko tutaj już zakończony i wtedy.  
Czyli może być posortowanych tak od największego do najmniejszego, tak.  
I wtedy to niesie jakąś informację, a minimalne.

**Damian Kaminski** 25:33  
No raczej tylko dla zamkniętych. Dobra, słuchajcie, no to masz jakieś tam wnioski? Łukasz, pytanie, czy idziemy jeszcze przez inne i skomentuję tak, że na deweloper ta ścieżka się tłumaczy. Zresztą deweloper jest mi s ql m, więc develop kropka model kropka. Lokal jest tym samym teoretycznie co?

**Lukasz Bott** 25:37  
No tak.

**Damian Kaminski** 25:51  
Ee dopiskiem Majewski quel natomiast może tutaj kwestia jeszcze keszu tak z racji, że to są odrębne witryny.  
To może tu się nie przetłumaczyło i jeszcze to co zaobserwowałem, jeśli raport.  
Jest ustawiony w trybie zakładka raporty jest w trybie listy, to przejście przez meni system, te menu i zębatke nie działa.

**Lukasz Bott** 26:14  
Iż raz, czyli wczoraj wychodzę.

**Damian Kaminski** 26:14  
Bo wtedy.  
Wejdź na raporty ustaw, wyświetlanie listy.  
Teraz zębatkę główną to w prawym górnym menu i raporty systemowe.  
Tak jakby.  
No właśnie wtedy nie ma ścieżki nie i on nadrzędnym jest ustawienie sposobu wyświetlania.  
Ee raportów, przez co cię nie przenosi, tak?

**Lukasz Bott** 26:46  
Mamy to.

**Damian Kaminski** 26:46  
No powinno być według mnie odwrotnie jak ustawisz sobie.

**Lukasz Bott** 26:49  
Znaczy w ogóle to powinno być niezależne moim zdaniem.

**Damian Kaminski** 26:51  
No nie, no bo zobacz teraz jak masz w formie listy to otwórz sobie.  
Folder raportów systemowych zobacz jak to działa inaczej nieco albo powinno tu przenosić albo w oj teraz. Rozwiń raporty systemowe nie buduje ci ścieżki.  
No już przetłumaczyło filler.

**Lukasz Bott** 27:14  
W sensie tutaj nie buduje ścieżkę.

**Damian Kaminski** 27:17  
W sensie takim tak, że tu nie buduje ścieżki, no bo to masz w formie drzewa, więc teraz po prostu w takim trybie wyświetlania te menu po prostu nie działa.  
Więc według mnie.  
Kliknięcie na raporty systemowe powinno przedstawić sposób wyświetlania raportów na.  
Folder owy.

**Lukasz Bott** 27:41  
A w tym sensie, że ten ding tak.

**Damian Kaminski** 27:44  
Tak powinien kliknij teraz.  
No widzisz te.  
No dobra, no i czy przenosicie do zakładki raport, bo.

**Lukasz Bott** 27:52  
Dobra rozumiem. A jeżeli a jeżeli ustawimy spowrotem kafelki?

**Damian Kaminski** 27:57  
I wejdziesz w cokolwiek to przeniesiecie we właściwe miejsce.

**Lukasz Bott** 28:08  
To pytanie, kto to robił? To ania, to nie ty robiłaś ten Link do raportu z sejmowych.

**Anna Skupinska** 28:13  
Nie ja robiłam celnik, to jest z nim nie tak.

**Lukasz Bott** 28:15  
No to.  
Tak no to mieli.

**Anna Skupinska** 28:18  
Że nie działa jak dla tych jeżeli są.

**Lukasz Bott** 28:21  
I jeżeli jesteśmy dobrą, czyli wróć.  
Jesteśmy w normalnym module raport owym domyślny widok jest ten.

**Anna Skupinska** 28:31  
Alkowie.

**Lukasz Bott** 28:31  
Felik kafelkowy tak.  
I w kaflowym mamy oczywiście raporty systemowe. To już widać tu może nie jest. Czy to może być faktycznie kwestia keszu?  
Czy i tutaj w tym trybie?  
Link, raporty systemowe.  
Działa tak, czyli w sensie przenosi mnie do podkatalogu raporty systemowe i widzę te kafelki swoją drogą przetłumaczone.

**Anna Skupinska** 28:49  
Mhm.

**Lukasz Bott** 28:57  
Nie, ale jeśli ja Jestem w trybie, znów Jestem w głównym tym module raport owym.  
I do sobie wyświetlam w postaci listy bądź listy pewnie kompaktowej to jest podobny efekt.  
To w tym momencie?  
Kliknięcie w menu tym modułów systemowych, tak.  
No raporty systemowe w ogóle nas nie przekierowuje.

**Damian Kaminski** 29:23  
No nie niesie żadnego skutku.

**Lukasz Bott** 29:24  
Nie, nie ma żadnego skutku, więc.

**Anna Skupinska** 29:26  
Widać w RLU, że poprawnie wprowadza u RLA jakbyś to po prostu Enter now LA czy coś się zmieni?  
Jeszcze raz wejść na tego samego varela.  
Faktycznie więc coś tutaj inaczej ten myślałam, że on znaczy tu umrę. Tak samo kafelki, lista najwyraźniej trochę inaczej.

**Lukasz Bott** 29:52  
Był taksówką.  
I i tutaj.  
Dodaję ten kat id jeden tak do linku jest, bo.

**Anna Skupinska** 30:03  
Tak dlatego, że ogólnie rzecz biorąc on się nawet jeżeli będziesz był, nie byłbyś raportach, no po prostu się ustawia na tą witrynę, dlatego, że to jest witryna, w której powinien się pokazywać. No wiesz, jest katalog idea numer jeden, on staje tam wyszukuje jaki katalog i d. Mają raporty systemowe i takie wstawia i wtedy ci powinno przekierować na odpowiednią witrynę z tym katalogiem media widać, że te, które mają wiersze zamiast tych kafelków mają to jakoś inaczej.

**Lukasz Bott** 30:03  
Kristin.

**Anna Skupinska** 30:31  
Tutaj jak będziesz na listę i będziesz do jakiegoś katalogu, to co się dzieje?

**Damian Kaminski** 30:36  
No nie wchodzisz właśnie do katalogu, tylko go rozwijasz. To jest ta różnica.

**Lukasz Bott** 30:41  
Mhm.

**Anna Skupinska** 30:41  
No właśnie więc to jest trochę pytanie, kto powinno się tutaj wyglądać?

**Damian Kaminski** 30:42  
Tu nie ma wejścia.

**Lukasz Bott** 30:48  
To znaczy kliknięcie niczym nie skutkuje dopiero kliknięcie na raport w konkretnym węźle tego drzewa. Tak.

**Damian Kaminski** 30:55  
No tak inaczej to działa po prostu i traktuję to ustawienie formy wyświetlenia jako nadrzędne, więc zakładam, że chyba powinniśmy nad wpisywać to ustawienie na kafelki. Jeśli wywołamy to z poziomu zębatki.

**Anna Skupinska** 31:08  
Myślę, że po prostu trzeba będzie dodać w tych.  
Dla ustawienia, że się widzi jako wiersze, że jak on zobaczy o ma być otwarta katalog pierwszy to powinien mieć otwarte katalog pierwszy, że on bowiem się od razu już rozwinięty w tym widoku.

**Damian Kaminski** 31:26  
No dobra, ale też przesuniesz go tam do tego użytkownika.

**Anna Skupinska** 31:29  
W sensie ekran chyba dałoby radę tak zrobić, ale nie Jestem pewna, jak to się robi. Na reakcje będzie trzeba zobaczyć.  
Bo nie ma sensu dawać oddzielnego trybu widoku.

**Damian Kaminski** 31:39  
No nie wiem, nie wiem jak uważacie czy.  
Nie no albo robimy tak, że mu nad wpisujemy jego ustawienie, czyli niezależnie jak ma zrobiony wyświetlanie zakładki, raporty ma jak klika tamto się wyświetla tak jak teraz.

**Anna Skupinska** 31:50  
Aha, w ten sposób.

**Damian Kaminski** 31:56  
No i ewentualnie ze skutkiem, że jak na wejdzie na raporty to musi sobie spowrotem zmienić na listę jak tak woli, albo to co powiedziałaś tylko jeśli to co powiedziałaś to według mnie no nie możemy tylko gdzieś tam rozwinąć jakiś węzeł, tylko tego człowieka od razu przekierować, czyli on powinien mieć od góry na liście raporty systemowe i rozwinięte te przynajmniej pierwsze zagnieżdżenie. Pytanie, czy to nie jest za bardzo skomplikowane?

**Anna Skupinska** 32:22  
Otwarcie katalog pewnie będzie skomplikowane, co do od przejechania to nie Jestem pewna, musiałabym zobaczyć.

**Damian Kaminski** 32:29  
No właśnie, więc może tak jest prościej? Nie wiem co tutaj Piotr czy Janusz sądzicie na ten temat? Czy Łukasz jak dla mnie ten sposób jak?

**Anna Skupinska** 32:38  
Tak, przejście na sebka pylkow też byłoby pewnie dość proste.

**Damian Kaminski** 32:41  
No tak, zakładam, że to jest po prostu najprostsza forma rozwiązania tego tego czasu, więc pytanie, czy nie zrobić tego tak.  
Co ty, Łukasz sądzisz?

**Lukasz Bott** 32:59  
Znaczy tak, gdzieś tam myślało się bronić, teraz podsumuj się to.

**Damian Kaminski** 33:03  
Jeszcze raz, czyli tak masz raporty wyświetlane w formie tabel w formie tabelki, listy, listy.

**Lukasz Bott** 33:11  
Przepraszam, czyli przed.

**Damian Kaminski** 33:11  
Nie kafelków tylko listy i jesteś tak przyzwyczajony i teraz wywołujesz zębatki. Raporty systemowe z zębatki, tak teraz się nic nie stanie, ale tak naprawdę stałoby się to, że otworzyłoby ci raporty w formie.

**Lukasz Bott** 33:13  
Dobra lista no.  
Raporty systemowe.

**Damian Kaminski** 33:28  
Folderów.  
Czego skutkiem byłoby też przedstawienie domyślnego sposobu wyświetlania listy raportów na foldery, a nie listy.

**Lukasz Bott** 33:39  
Kafelki.

**Damian Kaminski** 33:40  
Na kafelki no foldery, kafelki tak i teraz jak wrócisz na raporty i chcesz to przeglądać w formie listy, to znowu musisz to przeklikać.

**Lukasz Bott** 33:43  
No okej.

**Damian Kaminski** 33:48  
Mm no jak ktoś jest tak przyzwyczajone to jest jakieś dodatkowe, że tak powiem wbrew użytkownikowi zmiana formy wyświetlania. Natomiast pytanie, no jak często się też tam wchodzi, a według mnie to jest najprostsze obsłużenie tego kwasu.

**Janusz Bossak** 34:03  
Musiałem na chwilę wejść, bo tam.  
Znaczy, według mnie powinno być tak, że jeżeli jesteśmy w takim trybie i tam wchodzimy przez prawe menu zębatki, to zostajemy w tym trybie, tylko powinniśmy wskoczyć w folder raportów. No dlaczego?

**Damian Kaminski** 34:14  
Mhm.  
No tylko zobacz jeszcze dobra to czekaj, to weź Łukasz, zjedź do tych raportów systemowych, pokaż jak one się zachowują na liście.  
To wtedy.  
Bo tu nie masz kontekstu wejścia tylko rozwinięcie, czyli mamy raporty systemowe i co ma się to tak wyświetlić z pozycją raporty systemowe na samej Górze ekranu, czyli ma przewinąć, tak.  
Aplikacja jakbyś mógł przez skorelować te, żeby raporty systemowe powiedzmy były pierwszym pierwszym.

**Janusz Bossak** 34:50  
Rozumiem.  
Rozumiem, rozumiem, to nie jest tutaj, nie jest wchodzenie do.

**Damian Kaminski** 34:55  
No właśnie nie jest wchodzenie tak o tak.  
Powiedzmy nawet bez rozwijania w tych wewnętrznych katalogów, ale czy to ma być skutek wywołania pozycji? Raporty systemowe, jeśli sposób wyświetlania raportów mamy zdefiniowane jako lista?

**Janusz Bossak** 35:09  
Logi systemowe jeszcze mamy 3 czy 4 kategorie, 3.

**Damian Kaminski** 35:12  
4.

**Lukasz Bott** 35:13  
Takiej strony może tak.

**Janusz Bossak** 35:17  
No tak, musiałoby to skutkować dokładnie taką sytuacją, tak, że to przewinienie w to miejsce i będzie.

**Lukasz Bott** 35:23  
I rozwinięte drzewko tam.

**Janusz Bossak** 35:25  
I to drzewko tak rozwinięte, ale do jednego poziomu nie to wtedy odpowiada temu, co mieliśmy w kafelkach.

**Damian Kaminski** 35:32  
No tak i teraz pytanie czy?  
Nie stracimy na to 2 dni, powiedzmy pracy, a może tamto przełączenie w tryb kafelkowy to jest 2 godziny w porównaniu do tego i czy czy warto nie.

**Janusz Bossak** 35:48  
Słuszna uwaga, znaczy wydaje się, jeżeli to będzie działało tak, że przeniesie nas w ten tryb kafelkowy to też jest o k. Tak, bo to jest.  
Jakby z punktu widzenia użytkownika to jest tak, jakbym wchodził w jakieś ustawienia systemowe czy coś tak gdzie w raporty systemowe i one się tak mu wyświetlają. To, że można sobie przełączać i inaczej wyświetlać. No znaczy jest to wytłumaczenie jakieś tak, czyli o k.  
Jeżeli wchodzi prawym mni to wymuszamy mu przełączenie na tryb kafelkowy.  
Jakikolwiek by miał w tej chwili i wskakujemy w ten jakby katalog.

**Lukasz Bott** 36:28  
Raportów systemowych.

**Janusz Bossak** 36:29  
Portów systemowych nie, czyli tak jak Łukasz na początku pokazywał nie.

**Lukasz Bott** 36:33  
Tak.

**Janusz Bossak** 36:36  
Czyli w takim stanie?

**Lukasz Bott** 36:36  
Czyli to takie efekt ma być?

**Janusz Bossak** 36:39  
No i to będzie z punktu widzenia takiego odbioru dobrze tak, bo wchodzę w prawe menu i wchodzę w raporty systemowe. Wchodzę jakoś systemowo w raporty systemowe, tak i to jest systemowy widok raportów systemowych.

**Damian Kaminski** 36:53  
Mhm.

**Janusz Bossak** 36:53  
Tyle po prostu nie.

**Lukasz Bott** 36:56  
Tak to się.

**Janusz Bossak** 36:56  
Mogę biegać na inne sposoby?  
Ale jak ten gdy wchodzę, to wchodzę tak?

**Lukasz Bott** 37:01  
Tak i to, jeżeli to jest najprościej do zrobienia w tym momencie, to tak zróbmy i tyle.

**Janusz Bossak** 37:07  
Okład.  
Tak zróbmy.

**Damian Kaminski** 37:12  
No to nie musi zbadać, no ale wydaje się, że to jest po prostu dużo mniej pracy niż te teraz analizowanie jak przez królować tam i tak dalej.

**Lukasz Bott** 37:19  
Tak, tak.

**Janusz Bossak** 37:21  
Ty masz Łukasz. Zestaw wszystkich proponowanych raportów z opisem biznesowym. Po co?  
Prezentujemy.  
Czyli na przykład to, co przed chwilą widzieliśmy naj tam średni czas.  
Stosowania spraw i obok powinien być opis raport.  
Pozwala prześledzić to i tamto.

**Lukasz Bott** 37:45  
Czyli to to to dobra, to to opisy muszą zaktualizować.

**Janusz Bossak** 37:52  
Bo tego według mnie powinniśmy wychodzić zawsze nie, że robimy coś po coś. Także nasze pytanie zawsze sobie na początku cokolwiek robimy. To nie tylko dotyczy robotów, ale wszelkich prac, które wykonujemy. Po co my to robimy? Tak, czyli jaki to da efekt użytkownikowi? Nie tylko to, że to.

**Lukasz Bott** 38:01  
Mhm.

**Janusz Bossak** 38:10  
Potrafimy zrobić, no bo wiem, że potrafimy różne rzeczy, tylko po co nie jakie to daje efekt? Kto z tego skorzystał? Jakich sytuacjach, jaki jest?  
Yy juz Jestem to wczoraj akurat dyskutowaliśmy o temat edytora formularza z.  
Kamilem.  
Między innymi.  
I tam też mamy to podobną sytuację. Tak są pewne juz kasy.  
Jak Użytkownik, czyli konsultant, nasz twórca ogólnie procesu, jaką z tego skorzysta? Tak właśnie to, co tam dyskusja była, czy.  
Dodając nowe pole to edytujemy jego nazwę systemową czy nazwę wyświetlaną, skoro w tej chwili mam ustawione, że mam i pokazywać język Polski i nazwy wyświetlane tak.  
I to jest typow.  
To jakiś pojedynczy juz i tak samo tu musimy sobie zadawać pytanie.  
Po co Użytkownik, po co administrator wchodzi w ten raport?  
Jaki on ma w głowie kontekst, tak co on chce się dowiedzieć, co on się dowie po nazwie tego raportu.  
Czy on go ta nazwa go nie zmyli? Tak.  
Czy da dokładnie to, czego on się spodziewa? Tak i to to jest jakby klucz do sukcesu tutaj.  
No dobra, przejdźmy, bo jeszcze mamy już prawdzie koniec, ale zobaczymy jakiś, bo zatrzymaliśmy się na jednym tak, no chociaż zróbmy jakiś taki w miarę.  
Przegląd tego co tu mamy pierwszy to już będzie statystyki, no i co tutaj.

**Lukasz Bott** 39:46  
To znaczy tak odpowiednik tego tam czas procesowania spraw tutaj statystyki utworzonych i statystyki zmodyfikowanych.  
Spraw.  
Tutaj się ja ją.  
A i to jest na bieżący miesiąc, więc tutaj też jest dostosowany ten domyślny filtr.  
Żeby to nie wyświetlało.  
Ten, czyli ilość spraw zmodyfikowany w poszczególnych dniach. No to jest stan na dzień dzisiejszy, czyli przeliczenie jest na dzień wczorajszy. Tak, no to.

**Damian Kaminski** 40:19  
Mhm, ja bym się przyczepił tylko do słowa zmodyfikowanych.  
Obsłużonych czy obsługiwanych?

**Lukasz Bott** 40:28  
Obsługiwanych bardziej to jest.

**Damian Kaminski** 40:30  
Może bardziej by było tak biznesowo, bo zmodyfikowanych to tak mocno technicznie, a w zasadzie tu chodzi o to, że ktoś coś tam kliknął tak albo wpisał.

**Lukasz Bott** 40:41  
Wiesz to jak już to tutaj moja była intencja bardziej taki, jeżeli modyfikowanych to w tym sensie, że one są w toku, tak.

**Damian Kaminski** 40:46  
Mhm.  
O k.

**Lukasz Bott** 40:50  
Bo bo w kontrze to poszczególni właściciele, tak no, widać niedużo.

**Damian Kaminski** 40:56  
Mhm.

**Lukasz Bott** 40:59  
Bo w kontrze jest statystyki utworzonych spraw, czyli jeżeli, czyli tak tutaj mamy utworzonych spraw 4 tak wczoraj, no pewnie to się pokrywa z tymi zmodyfikowanymi, tak?

**Damian Kaminski** 41:08  
Mhm.

**Lukasz Bott** 41:15  
Ilość utworzonych spraw poszczególnych dniach no to to to to to ma sens, tak.

**Damian Kaminski** 41:17  
Że to jest, masz na myśli, że tak tak tutaj tutaj jest to tak opisane ten zmodyfikowanych to tak.  
Nie do końca biznes może rozumieć, co to znaczy ta modyfikacja, czy tylko przyciśnięcie, czy tylko wprowadzenie czegoś, ale ok, może się czepiam tutaj, jeśli uważacie, że nie mam racji to to też jest o k.

**Lukasz Bott** 41:36  
Nie wiesz co to jest słuszną uwagę?

**Damian Kaminski** 41:38  
Jak rozumiem utworzonych się zawiera w zmodyfikowanych po prostu to miałeś na myśli tak, że jak ktoś stworzył to to tam też liczy.

**Lukasz Bott** 41:48  
Tak, no jeżeli to znaczy zmodyfikowane będą zawierały też utworzone nie.

**Damian Kaminski** 41:54  
Mhm.

**Lukasz Bott** 41:55  
Ale mogę zawierać też zbiór takich, które nie były na przykład wczoraj utworzone, bo były utworzone we wrześniu, ale wczoraj były zmodyfikowane. Nie, to znaczy została zrobiona na nich jakaś akcja, tak.

**Damian Kaminski** 42:02  
Jasne.  
No tak.

**Lukasz Bott** 42:09  
Która jest reprezentowana przez zmianę daty w kolumnie case modified tak, no i to to modify jest właśnie tak, no literalnie przetłumaczyłem jako zmodyfikowanie tak.  
Data modyfikacji sprawy tak no to w tym sensie nie.  
Więc w szczególnym przypadku może nie tyle w szczególnym przypadku, gdy masz zupełnie nową instalację, to pewnie na samym początku będzie tak, że te ilości utworzonych wersus zmodyfikowanych. No to one pewnie będą zbliżone, nie.  
Dopiero jak system na puchnie danymi no to będzie.  
Mm będzie miał te tego troszkę te wykresy pewnie będą się ten rozjeżdżały nie.  
No no i tutaj już widać było, że na tym poprzednim tej mapie było.  
A to uwaga uwaga jeszcze do tego tak trochę ad vocem do Janusza, że Janusz nie lubi tej mapy.  
Znaczy.  
Jeżeli to jest tego typu, że to jest pokazuje tylko kilka kilka jakiś tam prostokątów, to jest o k. Ja ja mam uwagę, gdy to się tworzy taka mozaika, nie.

**Janusz Bossak** 43:21  
Tak.  
No tak, tak jak za dużo tego to właściwie nie wiadomo co tam odczytać. Tak tutaj widać to jest to jedno zajmuje 50%, a te 2 pozostałe są po 25%. Tak no i to.

**Lukasz Bott** 43:28  
Tak i.  
Tam tak mniej więcej mniej więcej po 25%, tak?

**Janusz Bossak** 43:38  
Czytelne no to jest znaczy proporcje takie nie.

**Lukasz Bott** 43:41  
Bo wiesz co, bo to jest taka uwaga.

**Janusz Bossak** 43:42  
A jak taką sieć to to nic nie wiadomo właściwie nie.

**Lukasz Bott** 43:46  
Tak, kiedyś mieliśmy to, skoro wywołałeś chłopaku zbijaja, no to mieliśmy właśnie szkolenia odnośnie wizualizacji. Tak może powinienem był wrócić sobie i przypomnieć zagadnienia, ale jedno na pewno zapamiętałem, bo to jest tree mapa, to jest swego rodzaju odpowiednik tego pasartu nie czyni tego wykresu kołowego.

**Janusz Bossak** 44:06  
Do.  
Dokładnie.

**Lukasz Bott** 44:06  
I wykres kołowy i tam zawsze była na tym szkoleniu było podane coś takiego. Wykres kołowy sprawdza się tylko i wyłącznie w prezentowaniu kilku wartości.

**Janusz Bossak** 44:19  
Dokładnie 3 4 wartości, bo reszta to już jest wtyczka.

**Lukasz Bott** 44:20  
Tak tak, bo bo bo mózg o ile jeszcze tutaj mamy prostokąty, to ludzki mózg. Jakoś tam te proporcje lidzi dobrze, nie jeśli chodzi o prostokąty, ale jeżeli chodzi o wycinki okręgu to już tak troszkę niekoniecznie tak, ale jak masz 3 4 i ewidentnie jest.  
Powiedział jakiś taki wyraźny, tak, no to ten, ale jak się więcej zaczyna to no to jest do przemyślenia. Tak, to też można dla słupkowy przerobić i tyle tak.  
I szybko pokażę.  
Dobra.  
To tutaj, jeśli chodzi o administrację bezpieczeństwo, to mamy tak takie zestawienia, statystyki raportów, zestawienie, czyli liczba raportów utworzonych per Użytkownik i tutaj w podziale na.  
Typy tabelaryczne, czy to coś mówi czy nie no.

**Janusz Bossak** 45:14  
No i to już jakoś tak wygląda.

**Lukasz Bott** 45:17  
No no tak, no bo masz wieś.

**Damian Kaminski** 45:18  
No właśnie kwestia co kto lubi, ale no tak, no ja tam się nie upieram przy tych 3 mapach.

**Lukasz Bott** 45:23  
I osoba osoba o no i to jest właśnie taki przykład, nie osoby najczęściej tworzące raporty, tak, gdyby to odciąć może tutaj.  
To drobnice w prawym Dolnym rogu. Nie. No to wiem, że o Basia najwięcej tworzy potem ania, potem Patrycja Mateusz. Tak.

**Damian Kaminski** 45:39  
No ale to możesz chyba odciąć, bo możesz odciąć filtrem danych zagregowanych.

**Lukasz Bott** 45:42  
No tak, ale.  
Mogę w danych zagregowanych, ale to jest ten filtr pod spodem. Pytanie, czy możemy zrobić taki filtr tutaj na to, że sobie odetnę tylko od dobra. Interesują mnie ci, którzy tam nie wiem. Powyżej 10 raportów tworzą nie.

**Janusz Bossak** 45:59  
Można.

**Damian Kaminski** 46:00  
Ale tamtym filtrem tego nie jesteś w stanie odciąć, bo nie do końca to.

**Anna Skupinska** 46:04  
A czynienia pietruszkowo wynika nie są filtrami zagregowany nimi.

**Lukasz Bott** 46:05  
W tym filtrem pod spodem tam.  
Ograniczeniem ograniczeniem danych w raporcie.

**Anna Skupinska** 46:08  
Stałej.

**Damian Kaminski** 46:09  
A chodzi ci o to, żeby tutaj wrzucić film z domyślną wartością, żeby ktoś mógł jednak rozszerzyć to na pojedyncze, tak.

**Janusz Bossak** 46:17  
Ja Jestem Jestem czepialski Jestem czepialski znaczy generalnie to się da zrobić tak jak mówisz, ale co to znaczy osoby najczęściej tworzące raporty co co co to oznacza?

**Lukasz Bott** 46:17  
Tak no chyba tutaj.  
Znaczy.  
W tym sensie ilościowym? Tak no.  
Że.

**Janusz Bossak** 46:34  
Znaczy dla mnie najczęściej to jest sprawdzenie, czy ktoś tworzy 5 raportów na dzień.

**Lukasz Bott** 46:41  
Mhm.

**Damian Kaminski** 46:41  
Mhm.

**Janusz Bossak** 46:41  
Czy jeden raport na dzień?

**Damian Kaminski** 46:43  
Trzeba zmienić tę nazwę nie najczęściej tylko.

**Lukasz Bott** 46:45  
Dobrem.

**Janusz Bossak** 46:48  
No i które najwięcej utworzyły raportów tak, czyli to nie są najczęściej tworzące raporty, bo czy zupełnie czymś innym jest częstotliwość tworzenia, bo ja tworzę raport raz na.

**Lukasz Bott** 46:50  
Może tak no i.  
Na ilość.

**Janusz Bossak** 46:59  
Godzinę, a ktoś inny tworzy raport raz na miesiąc i wtedy to.

**Lukasz Bott** 47:04  
Przepraszam was, muszę na chwile wyskoczyć do toalet.

**Janusz Bossak** 47:08  
Dobra, dobra, dobra.

**Damian Kaminski** 47:09  
No może to po prostu powinno być zestawienie twórców raportów tak i wtedy najeżdżając Barbara to stworzyła tyle, ale to już jest kwestia nomenklatury, przy czym no dobrze by było, żebyśmy to.

**Janusz Bossak** 47:13  
Słuchajcie.  
Znaczy.

**Damian Kaminski** 47:22  
Określili.

**Janusz Bossak** 47:23  
Mój wniosek po tej krótkiej tutaj prezentacji bardzo dobrze żeśmy to przeszli trochę.  
Jest taki, że na to.  
Musi spojrzeć ktoś biznesowo i tak.  
Od strony właśnie tej prezentacji.  
Yy danych, bo na razie jest to zrobione technicznie.  
No i o k. Jakbyś natomiast brakuje mi tego takiego, wiecie nie?  
Ducha biznesowego, w tym.

**Damian Kaminski** 47:55  
Znaczy ja bym to podzielił na 2, czyli po pierwsze.  
Spis tego, co my chcemy przedstawić i co na tych raportach przedstawiamy, czyli tytuły i opisy krótkie.  
A drugi element to potem ewentualnie praca nad już samą formą wyświetlenia. Tak, czyli nie wiem czy właśnie te mapa czy kafelki, czy warto odciąć ostatnich 10 i po prostu tak założyć i to możemy nawet tu w opisie do raportów zawrzeć wtedy uwaga. Raport nie uwzględnia użytkowników, którzy założyli 5 i mniej raportów tak i tyle. Jest to wyjaśnione, czemu kogoś nie ma, mimo że założył jakiś jeden raport, no bo jest nieistotny z punktu widzenia systemu.  
I takiego podziału.  
I wtedy tego poziomu pierwszego zdecydujemy, czy czegoś tam brakuje, tak, czy czegoś właśnie biznesowo brakuje, bo forma wyświetlenia, że to będą kafelki piwot czy czy tri mapa czy czy słupki to już jest wtórne. Tak, to kwestia.

**Janusz Bossak** 48:44  
Tak no tak.

**Damian Kaminski** 48:59  
Co się wygodniej czyta, ale w zasadzie tak, co mówisz biznesowo, czyli co my w ogóle chcemy pokazać i czy to ma sens i czy pokrywamy też wszystkie takie powiedzmy domyślne potrzeby, bo Łukasz ma jakiś swój punkt widzenia.  
A każdy ma swój nie i trzeba by było taką burzę mózgów pewnie jeszcze zrobić.

**Janusz Bossak** 49:20  
Dobra.  
Tak samo tu mam też uwagę, bo no to już mówiliśmy o tym angielskim, tak?  
Filtry tam Report created by Report tip Report category dobrze by było gdyby jednak po polsku.

**Damian Kaminski** 49:35  
To to też jest już zaplanowane. W sensie wiemy, jak to zrobić, tylko to wymaga. To można przyjąć, że to jest mwp 2, czyli to wymaga możliwości tłumaczenia nazw kolumn po stronie źródeł systemowych.  
Tak to zostało wymyślone, no.  
Chyba, że chcemy to przenieść na poziom raportu.  
Wtedy można różnie tłumaczyć te same kolumny.  
No ale na razie wyszliśmy od tamtej strony.

**Janusz Bossak** 50:06  
No ok, dobra, dobra, słuchajcie, bo ja muszę się przygotować, bo mam zaraz spotkanie z przemkiem.  
Yy tam chciał, żebym przygotował pewne rzeczy, więc muszę się tym zająć, ale no musimy do tego wrócić.  
I to według mnie dość pilnie, tak znaczy jak możecie jutro czy tam w poniedziałek Jeszcze raz temat podyskutować, ale wtorek środę przyszłego tygodnia jak wrócę to musimy do tego usiąść i tu prośba, nie wiem, może Damian, ty jak już jesteś na tym spotkaniu, bo możesz z tym może być Kamil.

**Lukasz Bott** 50:23  
Z dobra już się z tym.

**Janusz Bossak** 50:40  
Yy, ale bym chciałbym mieć do tego taki.  
Szlif biznesowych, że tak powiem tak i.

**Damian Kaminski** 50:47  
To znaczy, mogę to gdzieś tam dorobić, tylko żeby nie wymyślać czegoś na nowo, jeśli to już mam utworzony, to byłbym za tym, żeby Łukasz to po prostu spisał co mamy i wtedy możemy przedyskutować, czego nie mamy, albo zadać pytania, dlaczego tak, a nie inaczej nie.

**Janusz Bossak** 50:54  
Nie no to.  
Dokładnie tak.  
Dokładnie tak znaczy Łukasz pierwszej kolejności opisy tego, czyli jaka była twoja intencja, tworząc dany raport? Czyli co według ciebie on prezentuje, co daje temu użytkownikowi?  
Biznesowo tak biznesowo nie technicznie nie chce opisu typu, no bo tu mamy ze sku ela tam coś tam definition bierzemy, nie nie biznesowo tak co? Co ten raport przedstawia biznesowo?

**Lukasz Bott** 51:21  
No nie, nie jasne.

**Janusz Bossak** 51:29  
I tyle, a potem się zastanowimy właśnie co dalej. Dobra, ja muszę uciekać dzięki bardzo.

**Lukasz Bott** 51:35  
Dodać.

**Damian Kaminski** 51:38  
Dobra, to chyba kończymy.

**Lukasz Bott** 51:42  
Kończymy dobre dzięki za uwagę.

**Anna Skupinska** 51:43  
Ja na krótkie pytanie.

**Damian Kaminski** 51:44  
No.

**Anna Skupinska** 51:45  
Co też powodów systemowych. Czy było teraz jest coś takiego w ramach systemowych, że jeżeli ktoś jest w specjalnej grupie łatwo całą nazwę, to może edytować raporty systemowe, czy powinna być tak dashboard dami?

**Lukasz Bott** 51:57  
No konsekwentnie.

**Damian Kaminski** 51:59  
Tak, tak, tak oczywiście.

**Anna Skupinska** 51:59  
Dobra, to ja go tylko się upewniam o k. Dzięki.

**Lukasz Bott** 52:00  
Tam.

**Damian Kaminski** 52:03  
W sensie tak jest tak, czy coś tu musisz działać.

**Lukasz Bott** 52:05  
Nie, nie wiesz co?

**Anna Skupinska** 52:05  
A czy no po prostu ja po prostu muszę to już zrobiłam, tylko się zastanawiam czy na pewno tak chcecie. Sumie tam jest nazwa raporty.

**Lukasz Bott** 52:11  
Nie wiem to.

**Damian Kaminski** 52:12  
Tak i to musimy też gdzieś opisać, tak po prostu, no opisać.

**Lukasz Bott** 52:18  
Znaczy to, że jest to, że jest ta specjalna grupa czy coś, to tak to już jest na wiki.

**Damian Kaminski** 52:18  
Bo nie wiem, może to już jest na wiki, tak.  
W tym głównym tak czy?

**Anna Skupinska** 52:25  
Jeszcze tylko tam jeszcze dopisać, że też będzie od dashboard w systemowych nie tylko do raportów.

**Lukasz Bott** 52:26  
No to już.

**Damian Kaminski** 52:32  
No dobra, no to znaczy biznesowo jest to dla mnie zbieżne, tak w sensie technicznie rozumiem, że to są inne punkty widzenia, inne punkty gdzieś tam do obsłużenia w kodzie. Natomiast w kontekście biznesowym.  
Jak Jestem w grupie, mogę edytować raporty systemowe, to znaczy wszystkie obiekty w ramach tego folderu, czy to jest dashboard, czy to jest raport?

**Lukasz Bott** 52:57  
Tak to jest masz?

**Damian Kaminski** 52:58  
Już mnie to jako biznes powiedzmy nie interesuje.

**Lukasz Bott** 53:01  
To jest scenariusz.

**Damian Kaminski** 53:04  
O k.

**Lukasz Bott** 53:07  
Że musisz być system reports managers i tak dalej.

**Damian Kaminski** 53:15  
Dobra, dokończymy.

**Lukasz Bott** 53:17  
Kończymy zaraz, ale czy czekaj dobra to zrozumieć kompresję? Ja w tej chwili robię opisy te biznesowe tak do tych.

**Damian Kaminski** 53:18  
No na razie no.

**Lukasz Bott** 53:25  
Do tych raportów i rozumiem, że w przyszłym gdzieś tam tygodniu się spotkamy i to przedyskutujemy Jeszcze raz, tak.

**Damian Kaminski** 53:33  
No tak, możemy nawet w poniedziałek, jeśli udać się do przygotować, jak daj znać, kiedy przygotujesz i wtedy.

**Lukasz Bott** 53:37  
Dobre.  
Aha.

**Damian Kaminski** 53:40  
I wtedy ustalimy, kiedy możemy się spotkać w jakimś pierwszym wolnym terminem, bo to nie wymaga jakiegoś przygotowania, żeby omówić.

**Lukasz Bott** 53:43  
Dobra i.  
O k ale a i potem dopiero z tym wracamy do Janusza tak czy.

**Damian Kaminski** 53:50  
No Janusz wróci we wtorek czy we środę? Bo tego nie zrozumiałem, czy oni we wtorek w poniedziałek lecą tak we wtorek już będą. No to na designie. Wtedy możemy tu mówić.

**Lukasz Bott** 53:56  
No dobra, to ja Janusz będzie w środę tak no przyjemne.

**Damian Kaminski** 54:00  
Nie, nie mówił, że we wtorek lecą, bo mówił o tym sprint Review, że wtedy będą w trakcie już gdzieś tam przejazd, więc we wtorek będzie. No to albo we wtorek na razie albo na designie, albo zrobimy dodatkowe spotkanie. No to w takim razie, żeby mieć to gotowe. Na wtorek. To dobrze było mówić. To w poniedziałek, jak się nie uda, no to przesuniemy.

**Lukasz Bott** 54:16  
Dobry.  
Dobra, dobra.

**Damian Kaminski** 54:20  
Dobra, to hej.

**Lukasz Bott** 54:26  
Tania jakiś jesteś.

**Anna Skupinska** 54:28  
Mhm.

**Lukasz Bott** 54:29  
To na razie tylko skup się na tych technikaliach tak może umożliwienia.  
Bo jak widać tutaj jeszcze pewni merytoryka czy coś.

**Anna Skupinska** 54:39  
One się zmienić to w sumie jak skończę robić te te techniczne rzeczy ostra od dashboard systemowych to mogę się zająć co się dzieje, dlaczego to się nie robi w MS ql.

**Lukasz Bott** 54:39  
Będzie może się zmienić zawartość.  
No ewentualnie tak, no to czy czy? Czyli te zajmuje się tymi, że tak się wyrażę blachami tak technikalia mi, żeby to można było, a jak widać tutaj jeszcze będzie to dyskusja.  
Merytoryczne tak, odnośnie tego co mamy pokazywać, więc być może jeszcze tam się zmienią.

**Anna Skupinska** 55:07  
Tak.

**Lukasz Bott** 55:09  
No jeżeli już to raczej pewnie dojdą jakieś.  
Źródła danych, no ale źródła danych to rozumiem, że mamy jakoś tam nie ogarnięte tak technicznie jak to rozwiązać.

**Anna Skupinska** 55:21  
Dobrze, no to cześć.

**Lukasz Bott** 55:21  
Dobra, cześć dzięki.

**Janusz Bossak** zatrzymano transkrypcję
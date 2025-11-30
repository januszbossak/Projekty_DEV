**Data spotkania:** 2 października 2025

**Łukasz Bott:** Jesteś? Nie wiem, czy coś mam, bo to znaczy tak, może inaczej nie mamy nic, bo przynajmniej ja nie mam oznaczonego.

**Damian Kamiński:** OK. Pytanie, czy nie wiem. Cóż, mamy nieoznaczonego, Aniu, czy ty masz jakieś tematy?

**Anna Skupińska:** Specjalnie ciągle pracuję nad tymi danymi. Znaczy, oczywiście później będzie trzeba się zająć MySQLem, bo, znaczy tak, jak to jest z tym... Wczoraj rozmawiałam z tobą, Łukasz, to uznaliśmy, żeby zrobić poprawki dla MS SQL-a później.

**Łukasz Bott:** Tak, tak, chodzi o to, żeby nie wstrzymywać prac. Tam jest problem jest generalnie jest z tworzeniem źródeł systemowych. Danych ze SQL, tak, w przypadku by one są.

**Anna Skupińska:** Nie tylko źródeł systemowych, chodziło też o ogólnie rzecz biorąc o źródła lokalne, które są integracyjne.

**Łukasz Bott:** No właśnie, tych typu lokal, tak, no, bo online nowe się tworzą, tak, i to nie ma problemu.

**Anna Skupińska:** Tak.

**Łukasz Bott:** A tam w tym nowym, w tym nowym podejściu w module raportów systemowych, no pojawiło się... możliwość kilku nowych źródeł zewnętrznych, które są właśnie synchronizowane. Tam raz dziennie, tak to, bo to chodzi o statystyki na ogół o charakterze dziennym, więc żeby nie obciążało to online’owo połączeń i tak do bazy danych, no to po prostu tam są pewne agregaty robione. No i tu okazało się, że o ile dla MySQL-a jakoś nie ma problemu z tworzeniem tego typu źródła lokalnych, to w przypadku bazy MS SQL jest tam jakiś problem, no to Ania musi to rozwiązać, ale żeby prac nie wstrzymywać jakoś tak, no to w pierwszej kolejności niech ogarniamy tego MySQL-a, a potem zajmiemy się SQL Serverem. Jakiś taki jest plan działań.

**Damian Kamiński:** Spoko.

**Janusz Bossak:** A także tych raportów systemowych też, bo jak ktoś to zaczął wyglądać...

**Łukasz Bott:** Wysłałem.

**Janusz Bossak:** Czy możecie pokazać coś z tych dashboardów systemowych?

**Łukasz Bott:** Tak, no to mogę tylko gazik.

**Anna Skupińska:** Znaczy no niespecjalnie, chyba że kod się liczy.

**Janusz Bossak:** Po co niespecjalnie?

**Łukasz Bott:** Nie, nie, no to... to znaczy, w tym momencie dashboardy są porobione, tak, i Ania będzie musiała to przenieść w tryb systemowy. Tak, no i to, jeżeli mamy teraz chwilę czasu, mogę to pokazać, tak.

**Damian Kamiński:** No bo tak, no bo nie omawialiśmy ani razu, co tam jest, nie, w sensie.

**Anna Skupińska:** Aha, w ten sposób.

**Łukasz Bott:** Ja też konsultowałem to z Danielem Reszką w kontekście takich ich zapotrzebowań klientów, więc to też tam niektóre zmiany wprowadziłem, tak.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** A czy to jak to?

**Łukasz Bott:** Mogę to na szybko pokazać. Jeżeli słyszycie jakieś głosy w tle, to znów Michał Maliszewski jest wyjątkowo głośny, a ściany mamy z dykty. Czekajcie, muszę się podłączyć. Jest takie proste... wygląda. Dobra. Piotr, omawiamy ten. Omawiamy raporty systemowe, te, które gdzieś tam nawet stworzyłem. Tak więc. Jak chcesz, to możesz zostać, bo Rady jako takiej nie ma, tematów przynajmniej pilnych. Raporty systemowe. Aha, dobra. Już zauważyłem, że pojawiło się tutaj w tym prawym menu modułów systemowych link do raportów systemowych, czyli można przejść, aby standardowo, czyli do tej zakładki, która była Raporty systemowe, tak, tego folderu, albo po prostu z tego... przenosi do do tych do tego. Do tego modułu raportów systemowych, tak.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** A one też poczekaj, bo teraz.

**Łukasz Bott:** I to.

**Janusz Bossak:** Dobra, raporty, system ERP. OK. Czyli po prostu nas przenosi do zakładki, znaczy do systemu.

**Łukasz Bott:** Tak, tak, tak, tak. Są 2 ścieżki albo. Albo standardowa Raporty i System Reports i to się nie zmieniło. Albo dorzuciliśmy.

**Janusz Bossak:** Rozumiem.

**Łukasz Bott:** Link tutaj, tej diagnostyce, raporty systemowe i od razu nas przenosi do tej zakładki, żeby tego nie trzeba było szukać gdzieś.

**Damian Kamiński:** No dobra, ale jest pewna niespójność, że tu mamy po polsku, a tu po angielsku. W sensie jest możliwość tłumaczenia. Coś tu nie działa, czy po prostu jeszcze tego nie zrobiliście?

**Łukasz Bott:** Nie, nie przetłumaczyliśmy chyba, tak. No to to jest kwestia tłumaczeń słowników.

**Damian Kamiński:** No OK. No dobra, ale po prostu, no żeby to było jakoś spójne, to myślę, że to mało pracy, a duży efekt.

**Łukasz Bott:** Dobra, to ja sobie to zanotuję. Ania może jeszcze dzisiaj to poprawi, tak. To ma sens.

**Janusz Bossak:** Kiedyś się trzymaliśmy tej jakiejś takiej zasady, że dla administratorów to jest po angielsku, ale już dawno zostaliśmy.

**Łukasz Bott:** Tak, tak, to.

**Janusz Bossak:** I tam gdzie można to róbmy to po polsku, tak?

**Damian Kamiński:** No tak, no interfejs przecież ustawień systemowych też zrobiliśmy po polsku. Może jeszcze nie cały, to znaczy, sorry, poszczególne elementy jeszcze są po angielsku, ale nie jest po polsku i pewnie trzeba będzie to też wyrównać, nie?

**Łukasz Bott:** Tak, to przy okazji wisi. Przy okazji wisi ten. Przy okazji leży zgłoszenie, że ten Breadcrumbs, tak, bo tak to się nazywa ten górny pasek nawigacyjny.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** No bo tak mam przetłumaczony, powiedzmy pierwszy z dashboardów, tak, który sobie obejrzymy, czas procesowania spraw. No to. A może dobra, ja to jeszcze sprawdzę, bo to może być kwestia, nie przetłumaczyłem tych kategorii.

**Damian Kamiński:** No to może nie być przetłumaczony. Zaraz to wklep, przetłumaczę i sprawdzimy, ale to to opowiadać.

**Łukasz Bott:** Dobra, to jakbyśmy. Dobra, to to znaczy tak. Pierwszy z raportów do przewodów czasu procesowania spraw, jakieś zestawienie, czyli idziemy według tych. Tego podejścia, że mamy zestawienie. Jakiś średni czas, oczywiście dane są z dewelopera, więc tutaj wychodzi taka trochę mozaika. Też często procesowania spraw. To są tak. Tutaj Daniel zwrócił uwagę, że tego nie implementowałem. Do zastanowienia się, bo wrzucił taką uwagę, żeby na przykład zrobić. Żeby na takim dashboardzie wyświetlać na przykład, podzielić go na takie, które trwają dłużej niż 2 dni albo krócej niż 2 dni. Tak, no bo pewnie te, które trwają dłużej niż 2 dni, to w praktyce pewnie to oznacza, że ktoś gdzieś coś komuś wisi. Tak.

**Janusz Bossak:** No dobrze, średni czas procesowania spraw to...

**Łukasz Bott:** No i też.

**Janusz Bossak:** Od czego nasze? No, od otworzenia, rozumiem, sprawy do czego? Do zamknięcia sprawy, czy do jakiego momentu?

**Łukasz Bott:** To jest to jest brane z klasy `CaseHistory`. Czyli tak jak jest to systemowo liczone.

**Damian Kamiński:** Ale tutaj kolejne zgłoszenie, właśnie powinno być to opisane nawet na podstawie tych waszych, gdzieś tam może zapytań, czy chociaż tutaj `Tooltip`. W sensie, że mamy tą opcję chyba już, znaczy nie chyba, tylko po prostu mamy wyświetlania opisu.

**Łukasz Bott:** Tej sprawy.

**Damian Kamiński:** Raportu. I to też jest może nie na MVP, ale jako kolejny rozwój, żeby móc przeczytać strony, raport przedstawia.

**Łukasz Bott:** Tak tylko. Dobra.

**Damian Kamiński:** Nie, nie, ja nie mówię, że to teraz musi być do tego już wydania, nie, ale.

**Łukasz Bott:** Opisy, nie. Ale co innego jest chyba błąd, po prostu opisy raportu czy dashboardów. To się po prostu nie zapamiętują, bo nie zapamiętują, pomimo także się wprowadza. To zgłosi jako.

**Damian Kamiński:** Dashboardów czy raportów. Dashboardach.

**Łukasz Bott:** I jednego chyba i drugiego.

**Damian Kamiński:** W sensie? OK. Możliwe.

**Łukasz Bott:** No i pytanie, gdzie to się powinno pojawić tutaj pod znakiem zapytania?

**Damian Kamiński:** No według mnie nie. Według mnie powinno się pojawić i gdzieś to z kimś dyskutowałem tutaj przy filtry i odśwież. Jeśli już ustawiony, to raczej tu powinno być, albo tak jak Legenda się wyświetla już wewnątrz tutaj w prawym górnym rogu samego raportu, to może tu powinniśmy dać "pokaż opis", tak.

**Łukasz Bott:** Dobrze.

**Janusz Bossak:** Byłoby dobre.

**Łukasz Bott:** No myślę, że tutaj tak, żeby tu literkę "i", tak, nie czytam znak zapytania i klikam i się pojawia czy tam właśnie jako tooltip czy po prostu.

**Damian Kamiński:** Dokładnie i w kółeczku, tak jak. Możesz odświeżyć całość teraz ekranu w sensie całą stronę, bo przetłumaczyłem. Zobaczymy sobie tą ścieżkę.

**Łukasz Bott:** Bo moment.

**Damian Kamiński:** Całą stronę, bo przetłumaczyłem. Jeszcze sprawdzam na deweloperskim, a dobra, nie na tym deweloperskim. Dobra, dobra, tak, tak, tak. Teraz przetłumaczę.

**Łukasz Bott:** Development, skrót monitorowy, to może na następne wspólne.

**Janusz Bossak:** No dobrze. Ale wracam z pytaniem, średni czas procesowania spraw. Co to pokazuje?

**Damian Kamiński:** Czy to jest po prostu od startu do zamknięcia sprawy? To jest pytanie, tak, bo to przychodzi do głowy.

**Janusz Bossak:** No.

**Łukasz Bott:** Od startu do do tego momentu, do teraz.

**Janusz Bossak:** Warto do teraz.

**Damian Kamiński:** To teraz. No właśnie. Czy to teraz jest prawidłowym podejściem, bo "do teraz"?

**Janusz Bossak:** No właśnie to. Bo to nie jest.

**Piotr Buczkowski:** Znaczy, nie ma sensu. Trzeba tylko na zamkniętych sprawach sprawdzać.

**Damian Kamiński:** No właśnie.

**Piotr Buczkowski:** Zakończonych.

**Damian Kamiński:** Bo.

**Piotr Buczkowski:** Bo to będzie obniżało.

**Damian Kamiński:** Też bym był za tym.

**Janusz Bossak:** Dlatego.

**Piotr Buczkowski:** Wynik.

**Janusz Bossak:** Dlatego właśnie się o to bardzo dokładnie dopytuję, bo trochę rozumiem, jakby jak to działa. Tak, jeżeli bierzesz z `CaseHistory`.

**Łukasz Bott:** Mhm.

**Janusz Bossak:** To tam nie ma ostatniego stanu. Ostatni stan jest w `CaseDefinition`.

**Damian Kamiński:** Wpisu.

**Janusz Bossak:** Czyli to jest do momentu przejścia na poprzedni etap, jaki był?

**Łukasz Bott:** No tak, zgadza się.

**Janusz Bossak:** No właśnie więc. Patrzmy na to z biznesowego punktu widzenia. Co to mi daje? Znaczy ja jako użytkownik jestem zainteresowany tym, jak długo działają sprawy, tak, w jakimś procesie. Tak, może byśmy wzięli sobie jakiś konkretny, prosty, bo jak się patrzy na wszystko, to tak bajzel trochę, nie, ale jakiś proces. Mam obieg faktur, no i teraz. Zakładając biznesowo, że ostatnim etapem jest księgowość i załóżmy dla naszych celów, w księgowanie przebiega wyjątkowo długo, kilka dni. A wszystkie etapy wcześniejsze: zarejestrowanie faktury, OCR, jakieś opisy merytoryczne. Załóżmy, że trwają szybko. Tak, jesteśmy na etapie księgowości. To co ten raport pokaże? Pokaże nam, jaki był czas wszystkich spraw, obojętnie czy otwartych, czy zamkniętych. Ja mówię o tym teraz, który pokazujesz: wszystkie do momentu, kiedy sprawa wskoczyła na księgowość.

**Łukasz Bott:** Tak, tak.

**Janusz Bossak:** I teraz siedzi na tej księgowości dzień drugi, trzeci, piąty, dziesiąty. Załóżmy, tu się nic nie zmieni. Wciąż patrzy w tej historii, a nie zmieniła się sytuacja tej sprawy, bo jej nie zamknięto. Sprawa nie poszła dalej, jest na tym. Więc nie wiem, naprawdę. W odniesieniu do wszystkich spraw, jeżeli tak patrzymy, nie tylko zamkniętych, czyli również tych toczących się, jak to długo trwa. Według mnie pytania trzeba sobie postawić takie, jak stawia sobie użytkownik, tak, czyli ile trwają sprawy, ile te sprawy trwają na etapie księgowości, ile te sprawy trwają do momentu zamknięcia i tak dalej, a nie tylko, że technicznie da się wyciągnąć to.

**Damian Kamiński:** No ale to właśnie obrazuje, dlatego taka dyskusja jest potrzebna, że może tu jest za mało. Średni czas procesowania spraw zamkniętych. Średni czas procesowania spraw wszystkich.

**Janusz Bossak:** Ale jest na rynku.

**Piotr Buczkowski:** Wtedy wystarczy. Wtedy wystarczy `CaseDefinition`. Różnie dla spraw zamkniętych. Różnica między, tak, jest.

**Damian Kamiński:** No właśnie, więc, no słuchajcie, podaliśmy do tego, tak, mamy coś. Może tylko trzeba zmienić nazwy, co my tu prezentujemy i za chwilę rozbudujemy to jakieś dodatkowe jeszcze elementy. Nie musimy wydać tutaj od razu 3.

**Janusz Bossak:** Dlatego.

**Damian Kamiński:** 140 raportów. Wydajmy, nie wiem, kilka pewnych i nazwijmy je dobrze, a potem uzupełnijmy o to, co jeszcze brakuje.

**Łukasz Bott:** Tak.

**Janusz Bossak:** Tak znaczy, chodzi mi o to, wiecie, żeby nie było takiego.

**Damian Kamiński:** Żeby było zrozumienie, co my prezentujemy. Tak.

**Janusz Bossak:** Takiego poczucia, że coś tam pokazuje ten model, ale właściwie to jest.

**Damian Kamiński:** Tylko twórca, więc co?

**Janusz Bossak:** Pożytecznego. Nie, że właściwie niczego się nie mogę z tego dowiedzieć za bardzo, bo nie bardzo wiem, co mi pokazuje. Użytkownik, to ci ludzie, nasi klienci, tak, no to patrzą, tak mi się wydaje, przynajmniej nie, że. Jeżeli mam jakiś proces, no to mnie interesuje w tym procesie, jak długo trwają sprawy od początku do końca. A w sytuacjach, kiedy to, co jest to, co Piotr powiedział, tak, czyli do zamknięcia, a w sytuacjach, kiedy sprawa się toczy, no to też mnie to interesuje. Bo może gdzieś utknęła. Tak i chcę to zobaczyć. Więc to są chyba 2 różne stany. Nie te sprawy zamknięte. Tam wiemy, że już się skończyło i to jest OK.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** A zupełnie odrębnym według mnie tematem analitycznym są sprawy w toku. Te, które jeszcze biegną, no bo chce na przykład je pogonić, chce zobaczyć, na których etapach utykają i tak dalej i tak dalej, tak jakby.

**Damian Kamiński:** No tak, ale to tu może by się przydało. W ogóle jeszcze taka statystyka, ilość spraw. Ja nie wiem, może taka jest ilość spraw otwartych w ramach procesów, tak jako Pivot, albo nawet jako taka mapa jak tutaj i wtedy to też obrazuje, że mamy jakiś proces, gdzie tych spraw się toczy dużo i one są wszystkie pootwierane i to rzuca światło, czy to.

**Janusz Bossak:** No dobra.

**Damian Kamiński:** Jest standard, bo mamy tego typu spraw dużo, czy po prostu ktoś ich nie zamyka?

**Janusz Bossak:** Znaczy, bo może właśnie pytanie, w którą stronę iść. Uściślijmy, co to pokazuje? Jeżeli to pokazuje skalę z `CaseHistory`, to to są.

**Łukasz Bott:** W toku.

**Janusz Bossak:** Do poprzedniego etapu, czyli. Nie, nie, przepraszam Łukasza, ale to nie niesie żadnej informacji biznesowej.

**Łukasz Bott:** OK, dobra.

**Janusz Bossak:** Bo nie ma tego ostatniego etapu, który jest w `CaseDefinition`. I który tu nie jest doliczony, więc nie bardzo wiadomo, co to pokazujemy.

**Damian Kamiński:** No dobra, no to nie jest do zaorania, tylko do uzupełniania w kontekście nazw, tak.

**Janusz Bossak:** Znaczy nazw i tego, co pokazuje, no bo co... co biznesowo, jak to nazwać, żeby pokazujemy wszystkie sprawy do poprzedniego etapu, z wyłączeniem tego, na którym sprawa jest?

**Łukasz Bott:** Tam, tam. Przy czym nie wiemy, na którym etapie jest sprawa, tak tutaj.

**Janusz Bossak:** Co to pokazuje? Jaką to niesie informację biznesową?

**Damian Kamiński:** No to tylko potwierdza, że ta dyskusja jest potrzebna, że ta, że musimy właśnie to omówić wszystko i zadać te pytania.

**Janusz Bossak:** Dobra, ja czym nagrywamy to, tak, to będzie można z tego zrobić.

**Damian Kamiński:** Jeszcze jako ciekawostka zwrócił uwagę, tak, szary jest tak kontrastowy, że ktoś z dobrym wzrokiem nic nie widzi. I pytanie, czemu jedyna Basia jest czarna?

**Łukasz Bott:** Mówisz o to? Gdzie masz Basię czarną?

**Damian Kamiński:** W ośrodku, w drugim na dole, w drugim rzędzie, w drugiej kolumnie.

**Anna Skupińska:** Też pamiętam, że walczyliśmy trochę z tym i chodzi o to, że on trochę tak sobie automatycznie ustawia te kolory napisów i czasami nawet mniejszy, powiemy, ma być napis w tym kolorze, to sobie zmienia.

**Łukasz Bott:** W sensie etykieta, tak.

**Damian Kamiński:** No tak. Nie, nie, nie, nie, nie.

**Łukasz Bott:** Nie, ale to... No to słusznie. Dalej zauważył, bo zauważył ten pomarańczowy i ten pomarańczowy, no raczej to jest ten sam odcień.

**Damian Kamiński:** No jak?

**Łukasz Bott:** I tu zrobił na biało, a tu zrobił na czarno. To faktycznie to raczej tutaj na czarno powinien zrobić.

**Piotr Buczkowski:** Ona jest właśnie wszędzie. Te tooltipy są na czarno.

**Łukasz Bott:** Tutaj raczej powinien być.

**Damian Kamiński:** Znaczy to jest OK, bo one mają tło jasne, więc według mnie to jest OK, że są na czarno tylko z jakiegoś...

**Piotr Buczkowski:** Tło jest przezroczyste.

**Damian Kamiński:** No ale ono jest rozjaśnione tak względem koloru, więc nawet jak najedziesz, należą najedź na ciemny niebieski. Tam masz z prawej strony w drugim rzędzie. Tam jest najciemniejszy bym powiedział, no to to jest czytelne dalej. No ale też słuszne pytania, czy tooltipy powinny brać z koloru `fill` kafelka. Natomiast znowu to może niekoniecznie jest tym w [?] Może powinny być tooltipy jednakowe wszędzie, tak.

**Łukasz Bott:** A bo on bierze kolory koparkę, no.

**Damian Kamiński:** W sensie tu tooltipa, nie, no właśnie on bierze słowa, no to jest jakiś bajer. Pytanie, czy powinniśmy go utrzymać, czy nie? Według mnie nie krytyczny, bo to akurat jest czytelne, natomiast ten szary, który tutaj jest, to no powoduje, że kontrast z białym napisem jest w ogóle nieużyteczny. Dobra, no ale to zawsze chyba można zaznaczyć ten tekst, to znowu jest coś co dobrze było nie można.

**Łukasz Bott:** Ale co zaznaczyć?

**Damian Kamiński:** Tak myszką jakbyś pociągnął to da się to odczytać.

**Łukasz Bott:** Nie, nie, to jest takie jakby obrazek stworzony po prostu.

**Damian Kamiński:** Nie da się. OK. No ale jest `Value Process` jaki, no to. Nie jest to krytyczne, że nie wiadomo, co tam jest napisane, no te `Value` jako jedyne jest strasznie przetłumaczone.

**Łukasz Bott:** Właśnie.

**Damian Kamiński:** Dobra, przechodzimy przez pozostałe raporty, w tym boardzie. To to jest minimalny i maksymalny czas, co tak jak to przynajmniej wygląda, to jest taka sama.

**Janusz Bossak:** No pokaż, jakie.

**Łukasz Bott:** Podobnie wyglądają w sensie konstrukcyjnym, tak, natomiast no znów jest ten błąd merytoryczny, tak, no bo pobiera z `CaseHistory`, tak.

**Damian Kamiński:** Nie no OK. Po prostu taka forma wyświetlania chyba jest bardziej czytelna niż słupkowy, bo tu się da wyświetlić z racji, że mamy 2 wymiary, to może wyraźnie tak nie są te słupki, takie cienkie.

**Janusz Bossak:** No ale co kolory oznaczają tutaj?

**Łukasz Bott:** Kolory oznaczają tylko.

**Damian Kamiński:** Nic.

**Łukasz Bott:** No sensie nazwę procesu.

**Damian Kamiński:** Żeby nie było wszystko jednakowe.

**Łukasz Bott:** Tutaj wymiarem jest w sensie wielkością jest ten `Processing Time`, tak.

**Janusz Bossak:** Znaczy trzeba by było według mnie do takiej prezentacji, żeby sposobu prezentacji. Wziąć kogoś z BI, tak, tam Michała czy kogoś innego.

**Damian Kamiński:** No bo tu jest jeszcze istotne bardzo to, ale na to Janusz.

**Janusz Bossak:** No nie, no bo znaczy ty powiedziałeś, że wolisz tę mapę. Mi się akurat to nie podoba. Nie, znaczy ja nie lubię tej mapy.

**Damian Kamiński:** Wolałbyś słupek, tak.

**Janusz Bossak:** Wolałbym słupkowy. Na słupkowym to widzę, tak.

**Damian Kamiński:** Ale co widzisz?

**Janusz Bossak:** No że...

**Damian Kamiński:** Wartość, tak, w sensie masz skalę?

**Janusz Bossak:** Chciałem coś. Łatwiej mi jest porównać jedno z drugim, no.

**Damian Kamiński:** OK. No dobra, to.

**Janusz Bossak:** Znaczy, to jest moje odczucie, tak, ja po prostu jakoś nie korzystam z tej mapy. Wiem, że są zwolennicy. W niektórych przypadkach ma ona sens jakieś tutaj. Właśnie przez to, że jest kolorowa i ten kolor nie wnosi niczego, tak, no bo jeszcze gdyby to było tak, że...

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Kolor to jest liczba spraw, na przykład, i im więcej jest spraw w danym procesie, tym ten kolor na przykład jest ciemniejszy, że to mógłby być gradient. No to wtedy może by miało sens, bo myśmy mieli dodatkową informację, tak byśmy mieli jednocześnie czas.

**Damian Kamiński:** Nie zgodzę się.

**Janusz Bossak:** I ilość.

**Damian Kamiński:** Aha, ilość spraw masz na myśli, tak. Kolor byłby ilością spraw.

**Janusz Bossak:** Tak.

**Damian Kamiński:** OK. Dobra, to teraz rozumiem.

**Janusz Bossak:** Także możesz mieć proces, który trwa długo.

**Damian Kamiński:** I jest tego dużo.

**Janusz Bossak:** Ale 5 spraw. Możesz mieć proces, który trwa w miarę krótko, ale masz 10 000 spraw, tak?

**Damian Kamiński:** No to ma sens.

**Janusz Bossak:** No więc dlatego mówię, że tu trzeba specjalisty od takiej wizualizacji graficznej. Bo to nie tylko wiecie takie. Nie chodzi o to, że technicznie to jakoś pokazujemy, tylko żeby to rzeczywiście niosło wartość, nie? Żeby to, patrząc na to, człowiek dostawał, że tak powiem, informację. A tu ja nie dostaję informacji za bardzo, znaczy tak mi się wydaje, dostaję jakieś, które...

**Łukasz Bott:** Bez opisu jakiegoś, tak, no to.

**Damian Kamiński:** Poza tym. Tutaj ten, tutaj jeszcze większe znaczenie wydaje mi się, ma ta kwestia spraw zakończonych, bo tu bardzo dużym przekłamaniem jest to, że jest jedna sprawa, która wisi mega długo. Nie, ona pokazuje, że w danym procesie maksymalny czas procesowania spraw jest, nie wiem. Od początku instalacji AMODIT-a, bo ktoś uruchomił i zostawił. A de facto ta sprawa jest nieskończona, więc może to bardzo mocno zaburzać wynik. Bo cała reszta jest procesowana 2 dni, a ta jedna sprawa, nie wiem, tysiąc. Od dni tak. Przez 3 lata to się nie zamkną. Więc no tu tym bardziej ten maksymalny czas procesowania powinien dotyczyć zamkniętych.

**Łukasz Bott:** OK.

**Damian Kamiński:** Bo inaczej no to jedna sprawa po prostu zaburza obraz całego wykresu.

**Janusz Bossak:** Tak, znaczy wydaje się, że to jest chyba kluczowe, żeby powinniśmy pokazywać dla zamkniętych i dla osobno, czyli cały zestaw spraw, które są już zamknięte, no bo o nich wiemy już coś, że się zaczęły, zaczęły i zakończyły. A osobne powinny być raporty czy dashboard, nie wiem jak, dotyczące spraw w toku, czyli te, które jeszcze trwają, bo...

**Damian Kamiński:** No właśnie.

**Janusz Bossak:** I wtedy...

**Łukasz Bott:** I wtedy by można było faktycznie brać z 2 różnych tabelek. Jak Piotr powiedział, tak, czyli te, które są w toku, to bierzemy z `CaseDefinition` i tam można...

**Damian Kamiński:** Odwrotnie. Te, które są w toku z `CaseHistory`, a te, które są zamknięte z `CaseDefinition`, bo one mają datę zamknięcia.

**Łukasz Bott:** OK, dobra. Pamiętam te zamknięcie.

**Damian Kamiński:** Natomiast jeszcze trzecia zakładka, ten minimalny czas to w ogóle się zastanawiam, czy w kontekście spraw w toku to ma sens?

**Łukasz Bott:** OK, to jest.

**Damian Kamiński:** Co on, co on wtedy pokazuje?

**Łukasz Bott:** Minimalny czas, no.

**Damian Kamiński:** W sensie nie mamy zakończenia, więc co on nam pokaże? Co jest minimum?

**Łukasz Bott:** Nie no to w przypadku toczących się, no to byłby.

**Damian Kamiński:** Chyba wtedy to jest do wywalenia z toczących się, tak, tak. To znaczy nie czuję, co tu wtedy miałoby być pokazywane, jeśli sprawa nie dobiegła końca.

**Łukasz Bott:** Hej, dobra. Minimalnym być może jest do wywalenia. Faktycznie. Do mnie maksymalne. Albo po prostu. Czy to będzie maksymalny? Raczej po prostu czas trwania... czas trwania zamkniętych... zakończonych. Czas trwania spraw, tylko tutaj już zakończony i wtedy. Czyli może być posortowanych tak od największego do najmniejszego, tak. I wtedy to niesie jakąś informację, a minimalne...

**Damian Kamiński:** No raczej tylko dla zamkniętych. Dobra, słuchajcie, no to masz jakieś tam wnioski? Łukasz, pytanie, czy idziemy jeszcze przez inne i skomentuję tak, że na developerze ta ścieżka się tłumaczy. Zresztą developer jest MySQL-em, więc `develop.model.local` jest tym samym teoretycznie, co `MySQL`. Natomiast może tutaj kwestia jeszcze Cache'u, tak z racji, że to są odrębne witryny. To może tu się nie przetłumaczyło. I jeszcze to, co zaobserwowałem, jeśli raport jest ustawiony w trybie zakładka "Raporty" jest w trybie listy, to przejście przez menu system, te menu i zębatkę nie działa.

**Łukasz Bott:** Jeszcze raz, czyli wczoraj wychodzi.

**Damian Kamiński:** Bo wtedy wejdź na raporty, ustaw wyświetlanie listy. Teraz zębatkę główną, to w prawym górnym menu i raporty systemowe. Tak jakby. No właśnie wtedy nie ma ścieżki i on nadrzędnym jest ustawienie sposobu wyświetlania raportów, przez co cię nie przenosi, tak?

**Łukasz Bott:** Mamy to.

**Damian Kamiński:** No powinno być według mnie odwrotnie. Jak ustawisz sobie...

**Łukasz Bott:** Znaczy w ogóle to powinno być niezależne, moim zdaniem.

**Damian Kamiński:** No nie, no bo zobacz teraz jak masz w formie listy, to otwórz sobie folder raportów systemowych. Zobacz jak to działa inaczej nieco. Albo powinno tu przenosić, albo... rozwiń raporty systemowe. Nie buduje ci ścieżki.

**Łukasz Bott:** W sensie tutaj nie buduje ścieżki.

**Damian Kamiński:** W sensie takim, tak, że tu nie buduje ścieżki, no bo to masz w formie drzewa, więc teraz po prostu w takim trybie wyświetlania te menu po prostu nie działa. Więc według mnie. Kliknięcie na Raporty Systemowe powinno przedstawić sposób wyświetlania raportów na folderowy.

**Łukasz Bott:** A w tym sensie, że ten ding tak.

**Damian Kamiński:** Tak, powinien. Kliknij teraz. No widzisz te. No dobra, no i czy przenosi cię do zakładki raport, bo...

**Łukasz Bott:** Dobra, rozumiem. A jeżeli, a jeżeli ustawimy z powrotem kafelki?

**Damian Kamiński:** I wejdziesz w cokolwiek, to przeniesie cię we właściwe miejsce.

**Łukasz Bott:** To pytanie, kto to robił? To Ania, to nie ty robiłaś ten link do raportów systemowych.

**Anna Skupińska:** Nie, ja robiłam ten link. To jest z nim nie tak.

**Łukasz Bott:** No to. Tak, no to mieli.

**Anna Skupińska:** Że nie działa jak dla tych, jeżeli są.

**Łukasz Bott:** I jeżeli jesteśmy dobrą, czyli wróć. Jesteśmy w normalnym module raportowym. Domyślny widok jest ten kafelkowy, tak. I w kafelkowym mamy oczywiście raporty systemowe. To już widać. Tu może nie jest. Czy to może być faktycznie kwestia Cache'u? Czy i tutaj w tym trybie? Link "Raporty systemowe" działa, tak, czyli w sensie przenosi mnie do podkatalogu Raporty Systemowe i widzę te kafelki, swoją drogą przetłumaczone. Nie, ale jeśli ja jestem w trybie, znów jestem w głównym tym module raportowym. I do sobie wyświetlam w postaci listy bądź listy pewnie kompaktowej, to jest podobny efekt. To w tym momencie? Kliknięcie w menu tym modułów systemowych, tak. No raporty systemowe w ogóle nas nie przekierowuje.

**Damian Kamiński:** No nie, nie niesie żadnego skutku.

**Łukasz Bott:** Nie, nie ma żadnego skutku, więc.

**Anna Skupińska:** Widać w URL-u, że poprawnie wprowadza URL. Jakbyś to po prostu Enter now LA czy coś się zmieni? Jeszcze raz wejść na tego samego URL-a. Faktycznie, więc coś tutaj inaczej. Myślałam, że on znaczy tu umrę. Tak samo kafelki, lista najwyraźniej trochę inaczej.

**Łukasz Bott:** Był taksówką. I tutaj. Dodaję ten `Cat ID` jeden, tak, do linku, jest, bo.

**Anna Skupińska:** Tak, dlatego że ogólnie rzecz biorąc, on się nawet jeżeli będziesz był, nie byłbyś w raportach, no po prostu się ustawia na tą witrynę, dlatego że to jest witryna, w której powinien się pokazywać. No wiesz, jest katalog `ID` o numer jeden, on staje tam wyszukuje jaki katalog `ID`. Mają raporty systemowe i takie wstawia i wtedy ci powinno przekierować na odpowiednią witrynę z tym katalogiem `media`. Widać, że te, które mają wiersze zamiast tych kafelków, mają to jakoś inaczej.

**Łukasz Bott:** Był taksówką.

**Anna Skupińska:** Tutaj jak będziesz na listę i będziesz do jakiegoś katalogu, to co się dzieje?

**Damian Kamiński:** No nie wchodzisz właśnie do katalogu, tylko go rozwijasz. To jest ta różnica.

**Łukasz Bott:** Mhm.

**Anna Skupińska:** No właśnie, więc to jest trochę pytanie, kto powinno się tutaj wyglądać?

**Damian Kamiński:** Tu nie ma wejścia.

**Łukasz Bott:** To znaczy kliknięcie niczym nie skutkuje. Dopiero kliknięcie na raport w konkretnym węźle tego drzewa. Tak.

**Damian Kamiński:** No tak, inaczej to działa po prostu i traktuję to ustawienie formy wyświetlenia jako nadrzędne, więc zakładam, że chyba powinniśmy nadpisywać to ustawienie na kafelki. Jeśli wywołamy to z poziomu zębatki.

**Anna Skupińska:** Myślę, że po prostu trzeba będzie dodać w tych. Dla ustawienia, że się widzi jako wiersze, że jak on zobaczy o ma być otwarte katalog pierwszy, to powinien mieć otwarte katalog pierwszy, że on bowiem się od razu już rozwinięty w tym widoku.

**Damian Kamiński:** No dobra, ale też przesuniesz go tam do tego użytkownika.

**Anna Skupińska:** W sensie ekran chyba dałoby radę tak zrobić, ale nie jestem pewna, jak to się robi. Na Reacta będzie trzeba zobaczyć. Bo nie ma sensu dawać oddzielnego trybu widoku.

**Damian Kamiński:** No nie wiem, nie wiem jak uważacie. Czy... Nie no, albo robimy tak, że mu nadpisujemy jego ustawienie, czyli niezależnie jak ma zrobiony wyświetlanie zakładki, raporty ma jak klika, tamto się wyświetla tak jak teraz.

**Anna Skupińska:** Aha, w ten sposób.

**Damian Kamiński:** No i ewentualnie ze skutkiem, że jak na wejdzie na raporty, to musi sobie z powrotem zmienić na listę, jak tak woli, albo to co powiedziałaś, tylko jeśli to co powiedziałaś, to według mnie no nie możemy tylko gdzieś tam rozwinąć jakiś węzeł, tylko tego człowieka od razu przekierować, czyli on powinien mieć od góry na liście raporty systemowe i rozwinięte te przynajmniej pierwsze zagnieżdżenie. Pytanie, czy to nie jest za bardzo skomplikowane?

**Anna Skupińska:** Otwarcie katalogu pewnie będzie skomplikowane, co do przejechania to nie jestem pewna, musiałabym zobaczyć.

**Damian Kamiński:** No właśnie, więc może tak jest prościej? Nie wiem co tutaj Piotr czy Janusz sądzicie na ten temat? Czy Łukasz jak dla mnie ten sposób jak?

**Anna Skupińska:** Tak, przejście na system kafelkowy też byłoby pewnie dość proste.

**Damian Kamiński:** No tak, zakładam, że to jest po prostu najprostsza forma rozwiązania tego tego czasu, więc pytanie, czy nie zrobić tego tak. Co ty, Łukasz sądzisz?

**Łukasz Bott:** Znaczy tak, gdzieś tam myślało się bronić, teraz podsumuj się to.

**Damian Kamiński:** Jeszcze raz, czyli tak masz raporty wyświetlane w formie tabel, w formie tabelki, listy, listy.

**Łukasz Bott:** Przepraszam, czyli przed...

**Damian Kamiński:** Nie kafelków, tylko listy. I jesteś tak przyzwyczajony i teraz wywołujesz zębatki. Raporty systemowe z zębatki, tak? Teraz się nic nie stanie, ale tak naprawdę stałoby się to, że otworzyłoby ci raporty w formie folderów.

**Łukasz Bott:** Dobra lista, no. Raporty systemowe.

**Damian Kamiński:** Czego skutkiem byłoby też przedstawienie domyślnego sposobu wyświetlania listy raportów na foldery, a nie listy.

**Łukasz Bott:** Kafelki.

**Damian Kamiński:** Na kafelki, no foldery, kafelki, tak. I teraz jak wrócisz na raporty i chcesz to przeglądać w formie listy, to znowu musisz to przeklikać.

**Łukasz Bott:** No okej.

**Damian Kamiński:** No jak ktoś jest tak przyzwyczajony, to jest jakieś dodatkowe, że tak powiem, wbrew użytkownikowi zmiana formy wyświetlania. Natomiast pytanie, no jak często się też tam wchodzi, a według mnie to jest najprostsze obsłużenie tego przypadku.

**Janusz Bossak:** Musiałem na chwilę wejść, bo tam. Znaczy, według mnie powinno być tak, że jeżeli jesteśmy w takim trybie i tam wchodzimy przez prawe menu zębatki, to zostajemy w tym trybie, tylko powinniśmy wskoczyć w folder raportów. No dlaczego?

**Damian Kamiński:** No tylko zobacz jeszcze dobra to czekaj, to weź Łukasz, zjedź do tych raportów systemowych, pokaż jak one się zachowują na liście. To wtedy. Bo tu nie masz kontekstu wejścia tylko rozwinięcie, czyli mamy raporty systemowe i co ma się to tak wyświetlić z pozycją raporty systemowe na samej górze ekranu, czyli ma przewinąć, tak. Aplikacja, jakbyś mógł przeskalować, żeby raporty systemowe powiedzmy były pierwszym... pierwszym.

**Janusz Bossak:** Rozumiem. Rozumiem, rozumiem, to nie jest tutaj, nie jest wchodzenie do.

**Damian Kamiński:** No właśnie, nie jest wchodzenie tak o tak. Powiedzmy nawet bez rozwijania w tych wewnętrznych katalogów, ale czy to ma być skutek wywołania pozycji? Raporty systemowe, jeśli sposób wyświetlania raportów mamy zdefiniowane jako lista?

**Janusz Bossak:** Logi systemowe jeszcze mamy 3 czy 4 kategorie, 3.

**Damian Kamiński:** 4.

**Łukasz Bott:** Takiej strony, może tak.

**Janusz Bossak:** No tak, musiałoby to skutkować dokładnie taką sytuacją, tak, że to przewinięcie w to miejsce i będzie.

**Łukasz Bott:** I rozwinięte drzewko tam.

**Janusz Bossak:** I to drzewko tak rozwinięte, ale do jednego poziomu, nie? To wtedy odpowiada temu, co mieliśmy w kafelkach.

**Damian Kamiński:** No tak i teraz pytanie, czy? Nie stracimy na to 2 dni, powiedzmy pracy, a może tamto przełączenie w tryb kafelkowy to jest 2 godziny w porównaniu do tego i czy czy warto nie.

**Janusz Bossak:** Słuszna uwaga, znaczy wydaje się, jeżeli to będzie działało tak, że przeniesie nas w ten tryb kafelkowy to też jest OK. Tak, bo to jest. Jakby z punktu widzenia użytkownika to jest tak, jakbym wchodził w jakieś ustawienia systemowe czy coś, tak, gdzie w raporty systemowe i one się tak mu wyświetlają. To, że można sobie przełączać i inaczej wyświetlać. No znaczy jest to wytłumaczenie jakieś, tak, czyli OK. Jeżeli wchodzi w prawe menu, to wymuszamy mu przełączenie na tryb kafelkowy. Jakikolwiek by miał w tej chwili i wskakujemy w ten jakby katalog.

**Łukasz Bott:** Raportów systemowych.

**Janusz Bossak:** Raportów systemowych, nie, czyli tak jak Łukasz na początku pokazywał, nie.

**Łukasz Bott:** Tak.

**Janusz Bossak:** Czyli w takim stanie?

**Łukasz Bott:** Czyli to taki efekt ma być?

**Janusz Bossak:** No i to będzie z punktu widzenia takiego odbioru dobrze, tak, bo wchodzę w prawe menu i wchodzę w raporty systemowe. Wchodzę jakoś systemowo w raporty systemowe, tak i to jest systemowy widok raportów systemowych.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Tyle po prostu, nie.

**Łukasz Bott:** Tak to się.

**Janusz Bossak:** Mogę biegać na inne sposoby? Ale jak ten gdy wchodzę, to wchodzę tak?

**Łukasz Bott:** Tak i to, jeżeli to jest najprościej do zrobienia w tym momencie, to tak zróbmy i tyle.

**Janusz Bossak:** OK. Tak zróbmy.

**Damian Kamiński:** No to nie musi zbadać, no ale wydaje się, że to jest po prostu dużo mniej pracy niż te teraz analizowanie jak przez królować tam i tak dalej.

**Łukasz Bott:** Tak, tak.

**Janusz Bossak:** Ty masz Łukasz. Zestaw wszystkich proponowanych raportów z opisem biznesowym. Po co? Prezentujemy. Czyli na przykład to, co przed chwilą widzieliśmy, tam średni czas. Stosowania spraw i obok powinien być opis: raport pozwala prześledzić to i tamto.

**Łukasz Bott:** Czyli to to to dobra, to to opisy muszą zaktualizować.

**Janusz Bossak:** Bo tego według mnie powinniśmy wychodzić zawsze, nie, że robimy coś po coś. Także nasze pytanie zawsze sobie na początku cokolwiek robimy. To nie tylko dotyczy robotów, ale wszelkich prac, które wykonujemy. Po co my to robimy? Tak, czyli jaki to da efekt użytkownikowi? Nie tylko to, że to. Potrafimy zrobić, no bo wiem, że potrafimy różne rzeczy, tylko po co? Jakie to daje efekt? Kto z tego skorzysta? Jakich sytuacjach, jaki jest? Użycie. To wczoraj akurat dyskutowaliśmy o temat edytora formularza z Kamilem. Między innymi. I tam też mamy to podobną sytuację. Tak są pewne `use case'y`. Jak użytkownik, czyli konsultant, nasz twórca ogólnie procesu, jak z tego skorzysta? Tak właśnie to, co tam dyskusja była, czy dodając nowe pole, to edytujemy jego nazwę systemową czy nazwę wyświetlaną, skoro w tej chwili mam ustawione, że mam i pokazywać język Polski i nazwy wyświetlane, tak. I to jest typowy `use case`. Tak samo tu musimy sobie zadawać pytanie. Po co użytkownik, po co administrator wchodzi w ten raport? Jaki on ma w głowie kontekst, tak? Co on chce się dowiedzieć? Co on się dowie po nazwie tego raportu? Czy on go ta nazwa go nie zmyli? Tak. Czy da dokładnie to, czego on się spodziewa? Tak i to to jest jakby klucz do sukcesu tutaj. No dobra, przejdźmy, bo jeszcze mamy już prawdę koniec, ale zobaczymy jakiś, bo zatrzymaliśmy się na jednym, tak, no chociaż zróbmy jakiś taki w miarę przegląd tego, co tu mamy. Pierwszy to już będzie statystyki, no i co tutaj.

**Łukasz Bott:** To znaczy tak, odpowiednik tego tam czas procesowania spraw. Tutaj statystyki utworzonych i statystyki zmodyfikowanych spraw. Tutaj się ja ją. I to jest na bieżący miesiąc, więc tutaj też jest dostosowany ten domyślny filtr. Żeby to nie wyświetlało. Ten, czyli ilość spraw zmodyfikowanych w poszczególnych dniach. No to jest stan na dzień dzisiejszy, czyli przeliczenie jest na dzień wczorajszy. Tak, no to.

**Damian Kamiński:** Mhm, ja bym się przyczepił tylko do słowa "zmodyfikowanych". Obsłużonych czy obsługiwanych?

**Łukasz Bott:** Obsługiwanych bardziej to jest.

**Damian Kamiński:** Może bardziej by było tak biznesowo, bo zmodyfikowanych to tak mocno technicznie, a w zasadzie tu chodzi o to, że ktoś coś tam kliknął tak albo wpisał.

**Łukasz Bott:** Wiesz, to jak już to tutaj moja była intencja bardziej taki, jeżeli modyfikowanych to w tym sensie, że one są w toku, tak.

**Damian Kamiński:** OK.

**Łukasz Bott:** Bo w kontrze to poszczególni właściciele, tak, no, widać niedużo.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Bo w kontrze jest statystyki utworzonych spraw, czyli jeżeli, czyli tak tutaj mamy utworzonych spraw 4, tak, wczoraj, no pewnie to się pokrywa z tymi zmodyfikowanymi, tak?

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Ilość utworzonych spraw w poszczególnych dniach, no to to to to ma sens, tak.

**Damian Kamiński:** Że to jest, masz na myśli, że tak tak. Tutaj tutaj jest to tak opisane, ten "zmodyfikowanych" to tak. Nie do końca biznes może rozumieć, co to znaczy ta modyfikacja, czy tylko przyciśnięcie, czy tylko wprowadzenie czegoś, ale OK, może się czepiam. Jeśli uważacie, że nie mam racji, to to też jest OK.

**Łukasz Bott:** Nie, wiesz co, to jest słuszna uwaga.

**Damian Kamiński:** Jak rozumiem utworzonych się zawiera w zmodyfikowanych. Po prostu to miałeś na myśli, tak, że jak ktoś stworzył, to to tam też liczy.

**Łukasz Bott:** Tak, no jeżeli to znaczy zmodyfikowane będą zawierały też utworzone, nie.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Ale mogę zawierać też zbiór takich, które nie były na przykład wczoraj utworzone, bo były utworzone we wrześniu, ale wczoraj były zmodyfikowane. Nie, to znaczy została zrobiona na nich jakaś akcja, tak.

**Damian Kamiński:** Jasne. No tak.

**Łukasz Bott:** Która jest reprezentowana przez zmianę daty w kolumnie `CaseModified`, tak, no i to to `CaseModified` jest właśnie tak, no literalnie przetłumaczyłem jako "zmodyfikowanie", tak. Data modyfikacji sprawy, tak, no to w tym sensie, nie. Więc w szczególnym przypadku, może nie tyle w szczególnym przypadku, gdy masz zupełnie nową instalację, to pewnie na samym początku będzie tak, że te ilości utworzonych versus zmodyfikowanych. No to one pewnie będą zbliżone, nie. Dopiero jak system napuchnie danymi, no to będzie. Będzie miał tego troszkę. Te wykresy pewnie będą się rozjeżdżały, nie. No no i tutaj już widać było, że na tym poprzednim, tej mapie było. A to uwaga, uwaga jeszcze do tego, tak trochę ad vocem do Janusza, że Janusz nie lubi tej mapy. Znaczy. Jeżeli to jest tego typu, że to jest pokazuje tylko kilka kilka jakiś tam prostokątów, to jest OK. Ja mam uwagę, gdy to się tworzy taka mozaika, nie.

**Janusz Bossak:** Tak. No tak, tak jak za dużo tego, to właściwie nie wiadomo, co tam odczytać. Tak, tutaj widać to jest to jedno zajmuje 50%, a te 2 pozostałe są po 25%. Tak, no i to.

**Łukasz Bott:** Tak i. Tam tak mniej więcej po 25%, tak?

**Janusz Bossak:** Czytelne, no to jest. Znaczy proporcje takie, nie.

**Łukasz Bott:** Bo wiesz co, bo to jest taka uwaga.

**Janusz Bossak:** A jak taką sieć, to to nic nie wiadomo właściwie, nie.

**Łukasz Bott:** Tak, kiedyś mieliśmy to. Skoro wywołałeś chłopaku z BI, no to mieliśmy właśnie szkolenia odnośnie wizualizacji. Tak, może powinienem był wrócić sobie i przypomnieć zagadnienia, ale jedno na pewno zapamiętałem, bo to jest Tree Map, to jest swego rodzaju odpowiednik Pie Chartu, nie? Czyli tego wykresu kołowego.

**Janusz Bossak:** Dokładnie.

**Łukasz Bott:** I wykres kołowy i tam zawsze była na tym szkoleniu było podane coś takiego. Wykres kołowy sprawdza się tylko i wyłącznie w prezentowaniu kilku wartości.

**Janusz Bossak:** Dokładnie 3, 4 wartości, bo reszta to już jest wtyczka.

**Łukasz Bott:** Tak, tak, bo bo bo mózg. O ile jeszcze tutaj mamy prostokąty, to ludzki mózg jakoś tam te proporcje widzi dobrze, nie, jeśli chodzi o prostokąty. Ale jeżeli chodzi o wycinki okręgu, to już tak troszkę niekoniecznie, tak. Ale jak masz 3, 4 i ewidentnie jest. Powiedział jakiś taki wyraźny, tak, no to ten, ale jak się więcej zaczyna, to no to jest do przemyślenia. Tak, to też można dla słupkowego przerobić i tyle, tak. I szybko pokażę. Dobra. To tutaj, jeśli chodzi o administrację bezpieczeństwo, to mamy tak takie zestawienia, statystyki raportów, zestawienie, czyli liczba raportów utworzonych per użytkownik i tutaj w podziale na. Typy tabelaryczne, czy to coś mówi, czy nie, no.

**Janusz Bossak:** No i to już jakoś tak wygląda.

**Łukasz Bott:** No no tak, no bo masz wieś.

**Damian Kamiński:** No właśnie, kwestia, co kto lubi, ale no tak, no ja tam się nie upieram przy tych Tree Mapach.

**Łukasz Bott:** I osoba, osoba. O, no i to jest właśnie taki przykład, nie? Osoby najczęściej tworzące raporty, tak, gdyby to odciąć może tutaj. To drobnice w prawym dolnym rogu. Nie. No to wiem, że o Basia najwięcej tworzy, potem Ania, potem Patrycja, Mateusz. Tak.

**Damian Kamiński:** No ale to możesz chyba odciąć, bo możesz odciąć filtrem danych zagregowanych.

**Łukasz Bott:** No tak, ale. Mogę w danych zagregowanych, ale to jest ten filtr pod spodem. Pytanie, czy możemy zrobić taki filtr tutaj na to, że sobie odetnę tylko od dobra. Interesują mnie ci, którzy tam nie wiem. Powyżej 10 raportów tworzą.

**Janusz Bossak:** Można.

**Damian Kamiński:** Ale tamtym filtrem tego nie jesteś w stanie odciąć, bo nie do końca to.

**Anna Skupińska:** No to nie są filtrami zagregowanymi.

**Łukasz Bott:** W tym filtrem pod spodem. Ograniczeniem danych w raporcie.

**Anna Skupińska:** Tak.

**Damian Kamiński:** A chodzi ci o to, żeby tutaj wrzucić filtr z domyślną wartością, żeby ktoś mógł jednak rozszerzyć to na pojedyncze, tak.

**Janusz Bossak:** Ja jestem czepialski, jestem czepialski. Znaczy generalnie to się da zrobić, tak jak mówisz, ale co to znaczy "osoby najczęściej tworzące raporty"? Co to oznacza?

**Łukasz Bott:** Tak, no chyba tutaj. W sensie ilościowym, tak.

**Janusz Bossak:** Znaczy dla mnie "najczęściej" to jest sprawdzenie, czy ktoś tworzy 5 raportów na dzień.

**Damian Kamiński:** Trzeba zmienić tę nazwę. Nie "najczęściej", tylko...

**Łukasz Bott:** Dobrze.

**Janusz Bossak:** No i które najwięcej utworzyły raportów, tak? Czyli to nie są najczęściej tworzące raporty, bo częstotliwość tworzenia to zupełnie coś innego. Ja tworzę raport raz na godzinę, a ktoś inny tworzy raport raz na miesiąc. I wtedy to.

**Łukasz Bott:** Przepraszam was, muszę na chwilę wyskoczyć do toalety.

**Janusz Bossak:** Dobra, dobra, dobra.

**Damian Kamiński:** No może to po prostu powinno być zestawienie twórców raportów, tak, i wtedy najeżdżając: Barbara to stworzyła tyle. Ale to już jest kwestia nomenklatury, przy czym no dobrze by było, żebyśmy to określili.

**Janusz Bossak:** Mój wniosek po tej krótkiej tutaj prezentacji (bardzo dobrze, żeśmy to przeszli trochę) jest taki, że na to musi spojrzeć ktoś biznesowo. Od strony właśnie tej prezentacji danych. Bo na razie jest to zrobione technicznie. No i OK. Natomiast brakuje mi tego takiego, wiecie, ducha biznesowego w tym.

**Damian Kamiński:** Znaczy ja bym to podzielił na 2, czyli po pierwsze: spis tego, co my chcemy przedstawić i co na tych raportach przedstawiamy, czyli tytuły i opisy krótkie. A drugi element, to potem ewentualnie praca nad już samą formą wyświetlenia. Tak, czyli nie wiem czy właśnie Tree Map, czy kafelki. Czy warto odciąć ostatnich 10 i po prostu tak założyć. I to możemy nawet tu w opisie do raportów zawrzeć wtedy: "Uwaga. Raport nie uwzględnia użytkowników, którzy założyli 5 i mniej raportów". Tak i tyle. Jest to wyjaśnione, czemu kogoś nie ma, mimo że założył jakiś jeden raport, no bo jest nieistotny z punktu widzenia systemu i takiego podziału. I wtedy tego poziomu pierwszego zdecydujemy, czy czegoś tam brakuje, tak, czy czegoś właśnie biznesowo brakuje, bo forma wyświetlenia, że to będą kafelki, Pivot czy Tree Map, czy słupki to już jest wtórne. Tak, to kwestia.

**Janusz Bossak:** Tak, no tak.

**Damian Kamiński:** Co się wygodniej czyta, ale w zasadzie tak, co mówisz biznesowo, czyli co my w ogóle chcemy pokazać i czy to ma sens i czy pokrywamy też wszystkie takie powiedzmy domyślne potrzeby, bo Łukasz ma jakiś swój punkt widzenia. A każdy ma swój, nie, i trzeba by było taką burzę mózgów pewnie jeszcze zrobić.

**Janusz Bossak:** Dobra. Tak samo tu mam też uwagę, bo no to już mówiliśmy o tym angielskim, tak? Filtry tam Report Created By, Report Type, Report Category – dobrze by było, gdyby jednak po polsku.

**Damian Kamiński:** To to też jest już zaplanowane. W sensie wiemy, jak to zrobić, tylko to wymaga. To można przyjąć, że to jest MVP 2, czyli to wymaga możliwości tłumaczenia nazw kolumn po stronie źródeł systemowych. Tak to zostało wymyślone. No. Chyba, że chcemy to przenieść na poziom raportu. Wtedy można różnie tłumaczyć te same kolumny. No ale na razie wyszliśmy od tamtej strony.

**Janusz Bossak:** No OK, dobra, dobra, słuchajcie, bo ja muszę się przygotować, bo mam zaraz spotkanie z Przemkiem. Tam chciał, żebym przygotował pewne rzeczy, więc muszę się tym zająć, ale no musimy do tego wrócić. I to według mnie dość pilnie, tak. Znaczy jak możecie jutro czy tam w poniedziałek, jeszcze raz temat podyskutować. Ale wtorek, środę przyszłego tygodnia, jak wrócę, to musimy do tego usiąść i tu prośba, nie wiem, może Damian, ty jak już jesteś na tym spotkaniu, bo możesz z tym, może być Kamil.

**Łukasz Bott:** Z dobra, już się z tym.

**Janusz Bossak:** Ale chciałbym mieć do tego taki szlif biznesowy, że tak powiem, tak.

**Damian Kamiński:** To znaczy, mogę to gdzieś tam dorobić, tylko żeby nie wymyślać czegoś na nowo, jeśli to już mam utworzony. To byłbym za tym, żeby Łukasz to po prostu spisał, co mamy i wtedy możemy przedyskutować, czego nie mamy, albo zadać pytania, dlaczego tak, a nie inaczej, nie?

**Janusz Bossak:** Nie no to. Dokładnie tak. Dokładnie tak. Znaczy Łukasz, w pierwszej kolejności opisy tego, czyli jaka była twoja intencja, tworząc dany raport? Czyli co według ciebie on prezentuje, co daje temu użytkownikowi? Biznesowo, tak, biznesowo. Nie technicznie. Nie chcę opisu typu, no bo tu mamy ze SQL-a tam coś tam, `Definition` bierzemy, nie, nie. Biznesowo, tak. Co ten raport przedstawia biznesowo?

**Łukasz Bott:** No nie, nie, jasne.

**Janusz Bossak:** I tyle, a potem się zastanowimy właśnie co dalej. Dobra, ja muszę uciekać, dzięki bardzo.

**Łukasz Bott:** Dobrze.

**Damian Kamiński:** Dobra, to chyba kończymy.

**Łukasz Bott:** Kończymy dobre. Dzięki za uwagę.

**Anna Skupińska:** Ja na krótkie pytanie.

**Damian Kamiński:** No.

**Anna Skupińska:** Co do raportów systemowych. Czy było teraz jest coś takiego w ramach systemowych, że jeżeli ktoś jest w specjalnej grupie, (całą nazwę), to może edytować raporty systemowe, czy powinny być tak dashboardy?

**Łukasz Bott:** No konsekwentnie.

**Damian Kamiński:** Tak, tak, tak, oczywiście.

**Anna Skupińska:** Dobra, to ja go tylko się upewniam, OK. Dzięki.

**Łukasz Bott:** Tam.

**Damian Kamiński:** W sensie tak jest, tak, czy coś tu musisz działać.

**Łukasz Bott:** Nie, nie, wiesz co?

**Anna Skupińska:** A czy no po prostu ja po prostu muszę to już zrobiłam, tylko się zastanawiam czy na pewno tak chcecie. W sumie tam jest nazwa raporty.

**Łukasz Bott:** Nie wiem to.

**Damian Kamiński:** Tak i to musimy też gdzieś opisać, tak po prostu, no opisać.

**Łukasz Bott:** Znaczy to, że jest to, że jest ta specjalna grupa czy coś, to tak to już jest na Wiki.

**Damian Kamiński:** Bo nie wiem, może to już jest na Wiki, tak. W tym głównym, tak?

**Anna Skupińska:** Jeszcze tylko tam jeszcze dopisać, że też będzie od dashboardów systemowych, nie tylko do raportów.

**Łukasz Bott:** No to już.

**Damian Kamiński:** No dobra, no to znaczy biznesowo jest to dla mnie zbieżne, tak w sensie technicznie rozumiem, że to są inne punkty widzenia, inne punkty gdzieś tam do obsłużenia w kodzie. Natomiast w kontekście biznesowym. Jak jestem w grupie, mogę edytować raporty systemowe, to znaczy wszystkie obiekty w ramach tego folderu, czy to jest dashboard, czy to jest raport?

**Łukasz Bott:** Tak to jest, masz?

**Damian Kamiński:** Już mnie to jako biznes powiedzmy nie interesuje.

**Łukasz Bott:** To jest scenariusz.

**Damian Kamiński:** OK.

**Łukasz Bott:** Że musisz być `System Reports Managers` i tak dalej.

**Damian Kamiński:** Dobra, dokończymy.

**Łukasz Bott:** Kończymy zaraz, ale czy czekaj dobra to zrozumieć kompresję? Ja w tej chwili robię opisy te biznesowe tak do tych.

**Damian Kamiński:** No na razie no.

**Łukasz Bott:** Do tych raportów i rozumiem, że w przyszłym gdzieś tam tygodniu się spotkamy i to przedyskutujemy jeszcze raz, tak.

**Damian Kamiński:** No tak, możemy nawet w poniedziałek, jeśli uda się to przygotować. Jak dasz znać, kiedy przygotujesz i wtedy.

**Łukasz Bott:** Dobrze.

**Damian Kamiński:** I wtedy ustalimy, kiedy możemy się spotkać w jakimś pierwszym wolnym terminem, bo to nie wymaga jakiegoś przygotowania, żeby omówić.

**Łukasz Bott:** Dobra i. OK, ale a i potem dopiero z tym wracamy do Janusza, tak czy.

**Damian Kamiński:** No Janusz wróci we wtorek czy we środę? Bo tego nie zrozumiałem, czy oni we wtorek w poniedziałek lecą tak we wtorek już będą. No to na designie. Wtedy możemy tu mówić.

**Łukasz Bott:** No dobra, to ja Janusz będzie w środę tak no przyjemne.

**Damian Kamiński:** Nie, nie mówił, że we wtorek lecą, bo mówił o tym `Sprint Review`, że wtedy będą w trakcie już gdzieś tam przejazd, więc we wtorek będzie. No to albo we wtorek na Radzie albo na designie, albo zrobimy dodatkowe spotkanie. No to w takim razie, żeby mieć to gotowe. Na wtorek. To dobrze było mówić. To w poniedziałek, jak się nie uda, no to przesuniemy.

**Łukasz Bott:** Dobrze.

**Damian Kamiński:** Dobra, to hej.

**Łukasz Bott:** Ania, jakiś jesteś.

**Anna Skupińska:** Mhm.

**Łukasz Bott:** To na razie tylko skup się na tych technikaliach, tak, może umożliwienia. Bo jak widać tutaj jeszcze pewnie merytoryka czy coś.

**Anna Skupińska:** Ona się zmienić to w sumie jak skończę robić te techniczne rzeczy ostre od dashboardów systemowych, to mogę się zająć co się dzieje, dlaczego to się nie robi w MS SQL.

**Łukasz Bott:** Będzie może się zmienić zawartość. No ewentualnie tak, no to czy czy? Czyli to zajmuje się tymi, że tak się wyrażę, blachami, tak, technikalia mi, żeby to można było, a jak widać tutaj jeszcze będzie to dyskusja merytoryczna, tak, odnośnie tego co mamy pokazywać, więc być może jeszcze tam się zmienią.

**Anna Skupińska:** Tak.

**Łukasz Bott:** No jeżeli już to raczej pewnie dojdą jakieś. Źródła danych, no ale źródła danych to rozumiem, że mamy jakoś tam nie ogarnięte, tak, technicznie, jak to rozwiązać.

**Anna Skupińska:** Dobrze, no to cześć.

**Łukasz Bott:** Dobra, cześć, dzięki.
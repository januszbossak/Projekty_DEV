**Transkrypcja**

27 listopada 2025, 09:09AM

**Janusz Bossak** 0:05  
Bo teraz jest dobrze.  
Chyba dobrze teraz zaczęła.

**Kamil Dubaniowski** 0:20  
Doradzimy co tam, w sensie na pewno ja bym chciał omówić te reguły tabeli, jak będziemy do tego wchodzić na początek to bym filipow dłoń.

**Damian Kaminski** 0:30  
Dobra, to ty pokazujesz czy mam pokazać? Ja mogę pokazać tylko.

**Kamil Dubaniowski** 0:33  
Dorzuć, a ja szukam Filipa na liście.

**Damian Kaminski** 0:34  
Jest takie ryzyko, że w razie co będę musiał się ewakuować.

**Kamil Dubaniowski** 0:39  
To to dasz znać?

**Damian Kaminski** 0:39  
Na te we wsp. Ale to powiem, jeśli mnie tam wywołają, bo udało mi się z tego.  
Wymigać, bo według mnie tam.  
To nie powinno być.  
Zaangażowanie naszego działu w ten temat.  
Dobra clock squares queries.

**Kamil Dubaniowski** 1:07  
To jest pierwszy akurat.  
To pierwsze pewnie głównie do ciebie jakaś.  
Możemy i może na decyzję, czy chcemy, co dalej robić tak jak mamy, czy robimy już reaktor owo ten jedyny edytor, ale to raczej większy temat. Nie na ten sprint wtedy wyszedł. Znam o co chodzi na nowej liście pól.  
W ustawieniach procesu dodaliśmy akcję, która miałaby otwierać edytor reguł tabeli.  
Czyli to, co nam brakowało, mieliśmy w edytorze, że wchodzisz sobie w tabelę i klikasz edytuj regułę tabeli. No to my dodaliśmy na nowej liście pól traktatowej i ten edytor nam się otwiera, ale te przycisk.

**Piotr Buczkowski** 1:53  
Bo trzeba trzeba programować to w jaki sposób jest otwierany?

**Kamil Dubaniowski** 1:56  
Czyli.

**Piotr Buczkowski** 1:58  
I i co wywołać, żeby zamknąć?

**Kamil Dubaniowski** 2:01  
O k. Czyli przerabiamy jakby to to to nie jest jakiś tam większy tam gra.

**Piotr Buczkowski** 2:04  
No to jest drobna poprawka, trzeba tam dodać wykrywanie, że to otwieramy właśnie z reacta i wywołać co innego niż tam hit na parę ęcie to pewnie tutaj Parlamentem jest coś bracie, to tego nie ma.

**Kamil Dubaniowski** 2:14  
Mhm.  
Tak, zgadza się, dobra, no to to tyle chciałem w sumie wiedzieć tak, czy to jest jakiś większy temat i lepiej iść od razu w nowy.

**Piotr Buczkowski** 2:26  
Jest po prostu Czarny funkcja javascript w tym okienku, która wywołuje coś z parlamenta, a ponieważ te ten parent jest inny, to trzeba zrobić coś inaczej, żeby działał i tu i tu tak.

**Kamil Dubaniowski** 2:37  
Dobra, to Filip.

**Damian Kaminski** 2:38  
Dobra, tylko to, co powiedział właśnie Piotr, to jest jasne dla Filipa, co trzeba zrobić, bo to nie jest reakcje, tak.

**Kamil Dubaniowski** 2:43  
Znaczy nie Filip nic nie zrobi, Filip nic nie zrobi, Filip jakby będzie czekał na poprawkę i wtedy.

**Damian Kaminski** 2:44  
No właśnie.

**Piotr Buczkowski** 2:48  
Nie firmy musi powiedzieć co wywołać, żeby zamknąć to okienko.

**Kamil Dubaniowski** 2:52  
O k bo też Filip od razu jak to robimy, to zróbmy to docelowo, bo pewnie jeszcze chwilę te reguły stare edytor z nami zostanie, to ja chciałbym, żeby to jednak otwierało się w po papie.  
Czyli to Anuluj powin.

**Piotr Buczkowski** 3:05  
W jaki to w jakimś filmie to się powołuje?

**Kamil Dubaniowski** 3:08  
No aktualnie otwiera się w nowej karcie w ogóle, więc teraz to jest do zmiany po stronie Filipa, a ja chciałbym towarzysz premier i.

**Piotr Buczkowski** 3:14  
W nowej karcie to ok, to to wystarczy tej formacji.

**Kamil Dubaniowski** 3:19  
Tak może, bo docelowo ma być w oknie, docelowo ma być.

**Damian Kaminski** 3:19  
Ale poczekaj, poczekaj, Piotr, to ty sugerujesz, że to ma być w nowej karcie?

**Kamil Dubaniowski** 3:24  
Takie Teraz ja ja ja bym chciał, bo docelowo ta reguła ten edytor miałby się otworzyć.

**Damian Kaminski** 3:25  
Bo Kamil tak nie chce.

**Kamil Dubaniowski** 3:32  
Dobra, to może cała koncepcja od początku planujemy, żeby na liście pól w ogóle był taki Odnośnik do wszystkich reguł powiązanych z tym polem.  
No i na początku wiadomo, że na nie mamy tego, natomiast docelowo ma się otworzyć to w dużym oknie popup widzę listę wszystkich reguł powiązanych z tym polem i potencjalnie mogę sobie tam przejść do edycji tej reguły i to nie ma być przejście do zakładki reguł, bo to będzie już jakby wybicie użytkownika. On jest na liście pól otworzył sobie tylko podgląd listy powiązanych reguł, więc ja nie chcę go przekierować do nowej zakładki czy w ogóle do do zmienić mu zakładkę na listy reguł. Tylko chcę pokazać tę listę w formie okna.  
I.

**Damian Kaminski** 4:12  
Ale popraw to znaczy mówisz tylko, że poparł, że to będzie okno zamykane w tle jest jest to gdzie pracujemy, czyli nasze bieżące natomiast.

**Kamil Dubaniowski** 4:20  
Tak, lista płyt.

**Damian Kaminski** 4:22  
Będzie pełno ekranowy poparł.

**Kamil Dubaniowski** 4:24  
Tak no jak najwięcej miejsca no zająć wiadomo tam jakaś minimalna ramka żeby było widać, że to jednak jest popup żeby ktoś jest zorientował, że to się zamyka, ale no nie chcę zmieniać właśnie kontekstu tak jak jesteś na liście pól i tylko podglądasz sobie listę powiązanych reguł. No to chciałbym, żeby to było w oknie pop, żeby nie zmieniać właśnie użytkownikowi kontekstu, no bo nie wiemy czy on wejdzie do jakiejś reguły, czy nie wejdzie, chciał tylko zobaczyć listę powiązany.

**Damian Kaminski** 4:25  
No właśnie o k.  
Tak, tak, tak.  
Czyli de facto tak jak jest teraz bym powiedział tylko już po nowemu, czyli będzie to jeden element zarówno wywoływany z listy reguł, który otworzy pop jakieś reguły i tak samo tam to będzie papap reguły.

**Kamil Dubaniowski** 4:59  
Tak wtedy, no na ten moment po reguły, chociaż była też koncepcja, żeby pole. Tabela miało swoją listę reguł tak, czyli żeby nie było jednej zbiorczej reguły tabeli, tylko tam pamiętam, że że że.

**Damian Kaminski** 5:00  
Mhm.  
No tak, ale to już jest ten krok pośredni, o którym mówisz tylko żeby wyświetlić, a potem jak już wyświetlisz tak jak powiedzmy tu ta będzie inaczej w reakcje, ale tak jak tu klikasz sobie przycisk, no to otwiera się popup i ten popa będzie analogiczny z tej perspektywy. Z tamtej perspektywy będzie to jeden element przygotowany przez tutaj reaktorów.

**Kamil Dubaniowski** 5:13  
Tak.  
Tak no i.  
Wejdź może na albo dobra to ja udostępnie, że jak jest teraz i o co mi chodzi?  
Dopiero pulpit.  
O stronę by się przydało, przerobić też tam jakieś tereny się wyświetlanie wiadomo płytę.

**Janusz Bossak** 6:13  
No tutaj jest w jak widzę bez tych ramek na tym pasku i według mnie to lepiej wygląda bez tych ramek.

**Kamil Dubaniowski** 6:19  
Tak no to to tak powinno zostać. No już nawet mamy widzisz, no to już jakby jest wersja deweloperska, czyli wyższa niż jest nas trochę obsiana i wywalili. Znaczy to aktualizacja sigma, tak.

**Damian Kaminski** 6:28  
No to trzeba szybko to zaktualizować i nie przyzwyczajać, no bo innej opcji nie ma.

**Kamil Dubaniowski** 6:31  
No.  
Tak dobra i teraz tabela tak, czyli doszła tutaj akcja reguły i ja chciałbym, żeby ona była na wszystkich polach, czyli tutaj na liście wyboru, na przykład też ten piorun otwiera mi się tutaj na pełen ekran lista niekompletna reguła lista. Ja z tej listy mogę wejść sobie do edytora, ale to nadal wszystko dzieje się jakby w oknie poparł. Czyli nie ma przekierowania na tą zakładkę.

**Piotr Buczkowski** 6:55  
Ja wiem, że teczny.

**Damian Kaminski** 7:00  
Dobra, to znaczy powiem tak, na razie jest to na etapie koncepcji, nie ma w ogóle projektu mu capu, więc według ciebie piotrze mało może i ktoś inny nocy zróbmy mu okap, bo to jest mało kosztowe i się zastanówmy czy ma to sens.

**Kamil Dubaniowski** 7:15  
Dobra, ale tutaj decyzja, no bo to jest o tyle kluczowe, że teraz to się otwiera w nowej zakładce i mogłoby tak zostać na teraz, tak tylko wtedy obsłużymy to Anuluj i zapisz regułę. No bo tak naprawdę to powinno zamykać wtedy kartę nic więcej, bo bo w tle mamy tą listę punktu.

**Damian Kaminski** 7:29  
No dobra, ale to w takim razie.  
No właśnie tego typu rozwiązania jest, co jest prostsze róbmy, bo to jest tymczasowe rozwiązanie, więc róbmy to, co jest po prostu prostsze.

**Janusz Bossak** 7:40  
No tak, ale przerobienie tak.

**Piotr Buczkowski** 7:40  
Zamykanie tego okienka jest proste.

**Janusz Bossak** 7:43  
Tak no.

**Piotr Buczkowski** 7:43  
Jeżeli wiem, że się otwiera w no.

**Damian Kaminski** 7:43  
Czyli zamknięcie tej zakładki tak jest proste pod przyciskiem.

**Piotr Buczkowski** 7:47  
Trzeba programować to więc po prostu weź proszę być.

**Damian Kaminski** 7:52  
No to tak rób, bo jeśli to jest proste, to tyle według mnie to nie jest bloker, to jest rozwiązanie na nie wiem kwartał.

**Kamil Dubaniowski** 7:53  
Na na Anuluj Ok.

**Damian Kaminski** 7:59  
Maks pół roku to nie jest jakiś problem tutaj, który by powodował, że coś jest mniej użyteczne.

**Piotr Buczkowski** 8:05  
Jest to mój do parent close, no to Windows parent nie ma, jest pewnie window Open er tak.  
Trzeba obsłużyć Windows, jeżeli jest nul to inaczej.

**Janusz Bossak** 8:18  
No i dobrze, bo tutaj doszliśmy też do takiego momentu, w którym może warto o tym parę słów powiedzieć, bo jak będziemy przerabiać te reguły, w szczególności edytor, taki, który widzimy teraz, jak tu zacznij coś tam pisać w tym edytorze. No właśnie on to wygląda tak ten edytor, tak, no to też mieć w którymś momencie w reakcie.

**Damian Kaminski** 8:41  
Tak.

**Janusz Bossak** 8:42  
No i to jest pierwsze wyzwanie, które trzeba.

**Damian Kaminski** 8:45  
Tylko nie powinniśmy tym na tym dzisiaj zająć się spotkania. Byliśmy samotni, nie wchodzili, trzeba to zaprojektować, zgadza się.

**Janusz Bossak** 8:49  
Tak.  
Ale.  
Dlatego lepiej jest to rozwiązanie, które powiedział Piotr, niech to będzie nawet to stare okienko.  
I i o k. Dopóty, dopóki nie rozwiążemy.

**Piotr Buczkowski** 9:00  
Albo.  
To otwierajcie po prostu.

**Janusz Bossak** 9:05  
No bo jeszcze.

**Piotr Buczkowski** 9:05  
Wtedy będzie działać bycie żadnych zmian po window part będzie.

**Kamil Dubaniowski** 9:08  
Tutaj tak, czyli o KW sensie tej ramie po prostu.

**Piotr Buczkowski** 9:11  
A nie sorry, nie będzie mój błąd musiałaby być ta funkcja. Musielibyście dodać to funkcję, która zamyka o tej nazwie, co tam zwoływane.

**Damian Kaminski** 9:21  
Znaczy według mnie, że to, że to się otwiera w nowej zakładce to.

**Piotr Buczkowski** 9:26  
Pytanie, kto to pytanie, gdzie ma być zmiana? No na tym edit, ról czy reakcie?

**Damian Kaminski** 9:26  
To nie jest problem.  
Co to znaczy?

**Kamil Dubaniowski** 9:37  
O mniejsze ryzyko, że popsujemy coś starych, jeśli zrobimy reakcie, tak.

**Piotr Buczkowski** 9:43  
Tam tak jak widziałeś tam jest window parent. Coś tam, tak, to to tu funkcję trzeba otworzyć. Nas trzeba utworzyć taką funkcję, trzeba strip na stronie, która.  
Jest w trakcie tak.

**Damian Kaminski** 9:55  
Na tej stronie, którą teraz? Aha reakcja.

**Piotr Buczkowski** 9:57  
Close dialog tak, która będzie potrafiła zamknąć ten dialog.  
Tutaj mi to parę minął, partner jest.

**Damian Kaminski** 10:07  
Rozumiem, to znaczy z mojej perspektywy to to to.

**Piotr Buczkowski** 10:10  
Dobrze Przemek wczoraj wczoraj robił.  
Bo aut tam jest podobne zasady, tak?  
Że jest wywoływana funkcja ta ustawia.  
Poprawny.  
Pobrany funkcję java script, która ustawia wartość wygenerowana wygenerowanego tokenu o akt.  
On dodał, do reaktora jakoś tam, w jaki sposób funkcje ciała, sklep, która robi to samo, co robiła na starym.  
O tej samej nazwie, tak?

**Damian Kaminski** 10:41  
O k. Czyli pod tym przyciskiem, który jest teraz dostępny na tym starym wyglądzie. Przemek, tak jakby wstrzyknie java scripta, który ma się wykonać tak.

**Piotr Buczkowski** 10:50  
Nie, nie.  
Nie.  
Teraz.  
Jest jest funkcja klos dialog.  
Starym skrypt jotes starym naszej kilku ze skryptami ja tez tak która potrafi.

**Damian Kaminski** 11:00  
Mhm.  
No.

**Piotr Buczkowski** 11:06  
Zamknąć aktualnie otworzony dialog. Tak naprawdę zamyka wszystkie aktualnie otworzone dialogi.  
Taka sama funkcja test musi być w reakcie zrobiona.  
Żeby to zadziałało.

**Damian Kaminski** 11:23  
Ale ja.  
Bo widzimy teraz ekran, który nie jest reaktory, więc tu mi się coś nie zgadza w kontekście, chyba, że masz na to inny Plan, że.

**Piotr Buczkowski** 11:29  
No window parę tutaj jest strona, która wywołała tą zakładkę.  
Strona jest w reakcie i ona nie posiada klosz dialog funkcji.

**Damian Kaminski** 11:42  
O k. Czyli trzeba dlatego narzędnika dorobić klaus, dialog, tak.

**Kamil Dubaniowski** 11:43  
Tutaj.

**Piotr Buczkowski** 11:46  
Tak, tak.

**Damian Kaminski** 11:47  
O k.

**Piotr Buczkowski** 11:48  
Która będzie potrafiła potrafiła zamknąć tą otworzona zakładkę, tak.

**Damian Kaminski** 11:53  
Filip, rozumiesz? To były w stanie to zrobić.

**Filip Liwiński** 11:55  
No dobra rozumiem, no nie wiem co życie.

**Kamil Dubaniowski** 11:57  
Jak coś to przemka tam pod pytasz?

**Damian Kaminski** 11:59  
No to jak ty rozumiesz tutaj Przemek na pewno też będzie wiedział o co chodzi. W sensie chodziło mi tylko o to, czy czy po prostu z punktu widzenia reaktor wiesz, co trzeba zrobić? No to o k to trzeba to opisać i któryś z was to zrobi.

**Piotr Buczkowski** 12:08  
W tym.  
To było w starym te słowa po prostu wykrywa wszystkie tam okienka. Dialog odtworzonej jest zamyka.  
Zakładamy, że jest tylko na raz jedno otwarte.

**Damian Kaminski** 12:17  
Dobra, tylko podsumowując.  
To jest już aspekt techniczny, natomiast funkcjonalny będzie tak jak teraz kamienie pokazywał, otwieramy w nowej zakładce klikamy przyjść, zamyka się. Ta zakładka wracamy do poprzedniej, tak?

**Piotr Buczkowski** 12:29  
Nie, sorry, nie, nie, nie, nie.

**Damian Kaminski** 12:32  
Właśnie, czyli jak?

**Piotr Buczkowski** 12:32  
Znaczy.  
Otwieramy paint premie.  
Na tej stronie REACT.

**Damian Kaminski** 12:40  
We frame pełnoekranowym.

**Piotr Buczkowski** 12:42  
Tak.

**Damian Kaminski** 12:45  
O k.

**Piotr Buczkowski** 12:47  
Chyba jeżeli chcecie w nowej zakładce to trzeba przerobić. No edit, forum.

**Kamil Dubaniowski** 12:50  
Nie no nie musi być. Moim zdaniem to nawet jest o k, że to się otworzy w tamtym kontekście także.

**Piotr Buczkowski** 12:54  
Mówię, że albo zmiana tutaj, albo zmiana tutaj.

**Kamil Dubaniowski** 12:57  
Zarówno reaktor owo nie ryzykujmy, że zepsujemy coś co działało tam mamy ostatnie 2 dni sprintu.  
No.

**Damian Kaminski** 13:05  
No ale to jest coś co wejdzie do.  
Grudnia, tak.

**Kamil Dubaniowski** 13:08  
Grudniowej.

**Damian Kaminski** 13:09  
Mhm, ok.  
No dobrze, to Jeszcze raz pytanie podsumowujące.  
Od tak otwieramy to w tym ekran w tym oknie przeglądarki, w którym widzimy, otwiera się to na pełny ekran w formie takiego przykrycia tego, co jest pod spodem, musi być dorobiona do tej.  
Funkcji część reaktora, która będzie interpretowała i zamykała ten to, to otwarte okienko. Ja to tak rozumiem z perspektywy tego, co powiedzieliście, czy ty, czy tu nie popełniam błędów w opisie tego i czy ty Filip wiesz jak to zrobić?

**Kamil Dubaniowski** 13:49  
Ja.  
Też tak samo to rozumiem.

**Filip Liwiński** 13:52  
No też to tak zrozumiałem.

**Damian Kaminski** 13:55  
I czy wiesz jak to zrobić?

**Filip Liwiński** 14:00  
Mm.

**Damian Kaminski** 14:00  
Czy coś chcesz dopytać Piotra?

**Kamil Dubaniowski** 14:07  
Zacznijmy jak będziesz miał pytania, to pewnie najlepiej z przemkiem konsultować jak to robił wczoraj i to będzie na bieżąco.

**Damian Kaminski** 14:10  
No to skonsultuj to z przemkiem, jeśli nie wiecie, to od razu dopytajcie Piotra, żeby po prostu podczas jego nieobecności móc to zaopiekować. Tak.

**Filip Liwiński** 14:18  
Dobra, dobra.

**Kamil Dubaniowski** 14:24  
No to chcieliby dzięki, bo chyba tam dalej to nie będzie sensu, żebyśmy się trzymali namiar jakbyś wrócił, d.

**Damian Kaminski** 14:31  
Już już już.  
Dobra, to co z tym robimy?

**Kamil Dubaniowski** 14:41  
Przypisz do Filipa w takim razie tak.

**Damian Kaminski** 14:41  
Filipa, tak.  
Ting.

**Kamil Dubaniowski** 15:16  
I wrzuć na ten sprint, no bo ten temat był w tym sprincie robiony nieskończony.

**Damian Kaminski** 15:22  
O k.  
A to możemy to od 5 już stąd.  
Dobra, czy tu coś? Dostaliśmy jakąś odpowiedź, tu mieliśmy coś.  
Nie dostaliśmy odpowiedzi.  
No to czekamy.

**Kamil Dubaniowski** 15:47  
No ja to wrzuciłem na 2 tych. No następnie spytałem na razie dopiero trampek, no bo to temat tam dostępy, bo jako jedyny.

**Damian Kaminski** 15:55  
Tu się coś nowego pojawia u od JLPP.  
A o k. To jest większy temat, już go redaguje. Czyli tak pomysł jest to znaczy to jest temat naprawdę duży i to on może wymagać wyceny, ale pytanie czy w ogóle chcemy w tą stronę iść, czyli czy przedstawić bardzo wstępną koncepcję klientowi i zapytać, czy w ogóle mamy to wyceniać?  
Ee, to znaczy mamy te formularze. To jest związane z tym w jakim kierunku powiedz mi, jakie klientów w ostatnim czasie pozyskaliśmy, jak i klienci korzystają za moneta. Mamy te duże firmy, które traktują od lat jako portal pracownika typu GILPII. Wszystkie w zasadzie, które wykorzystują to do aspektów hr owych.  
I mamy kwestionariusz osobowy.  
Który często wypełniany jest na telefonie ze względu na to, że to jest dostęp tymczasowy ze względu na to, do jakich ludzi po prostu to trafia. Niekoniecznie właśnie oni mają czy mają, czy korzystają z komputerów na co dzień tak, bo często po prostu są to jacyś pracownicy. Już mówiąc wprost tymczasowi, na przykład magazynowi związani właśnie teraz z okresem świątecznym i i wypełniają to na telefonie, mówiąc wprost i teraz, tak, jeśli mamy takie formularz, to on często zawiera 200 250 pól.  
W związku z tym jego.  
Czytelność w formie takiej go długiego węża, no jest może mniej użyteczna i pomysł jest taki, żeby jeśli dzielimy to na sekcję, to wyświetlać formularz w kontekście takim sekwencyjnym, czyli Wypełnij jedną sekcję i na końcu nie jest to przewijane na 200 pól, tylko jest powiedzmy 20 pól jest. Załóżmy jakaś strzałka dalej kolejna sekcja teraz.  
Dlaczego to jest skomplikowane, bo pod tym dalej w zasadzie może powinniśmy od razu robić jakąkolwiek walidację tej części formularza.  
Mówimy oczywiście tutaj o ujęciu tylko modelowym, więc inaczej by się zachowywał nieco formularz na.  
Na na przeglądarce na komputerze, a inaczej na mobilu, bo od razu jeśli coś wykryjemy co jest niespójne, no to powiedzmy pokazujemy, że jeszcze na tym widoku.

**Kamil Dubaniowski** 18:19  
Może może przerwę i zasugeruje co mi przyszło do głowy, jak mamy ten tryb wyświetla i formularz i tam są 2 opcje to dodałbym trzecią i to jest na zasadzie takiego. No nie wiem póki sarda krokowego.  
Jakby trzeba.

**Damian Kaminski** 18:33  
No.

**Kamil Dubaniowski** 18:35  
Domyślnie to włączy i tak świadomie to włączyć i to nie będzie tak, że nam obojgu inaczej na desktop inaczej tylko wtedy taki proces po prostu jest tak ustawiony, że no trzeba przechodzić każdą sekcję po kolei.

**Damian Kaminski** 18:45  
O k.  
To jest jakaś propozycja, czyli tak naprawdę to jest trochę pod etapy, nie na, czyli jeden etap, na którym wyświetlamy różne różne wizualizacje formularza w formie takiego wizarda no.

**Lukasz Bott** 18:46  
Wiecie co?

**Kamil Dubaniowski** 18:54  
Dodania tak masz.

**Lukasz Bott** 18:55  
Damian Damian Damian, koledzy, słuchajcie, jak była jeszcze christina, my to dyskutowaliśmy, a ja dokładnie to rozwiązałem właśnie akiem, czyli za każdą sekcję formularza odpowiadał etap w procesie i po prostu przełączanie między etapami tak powodowało przełączanie między zakładkami.

**Damian Kaminski** 19:14  
O k Łukasz tylko to nie jest proste, dobra, tylko tu mówimy o Grand temporary akces.

**Lukasz Bott** 19:17  
Nie no mówię, że doraźnie doraźnie tak to zostało rozwiązane. Tak natomiast była koncepcja właśnie takiego, jak to powiedział wizard. Takiego właśnie progowego przechodzenia nie i może w tym kierunku powinniśmy pójść.

**Damian Kaminski** 19:21  
Mhm.  
Tak, bo po prostu udostępnia, bo różne etapy się konfliktują z tym naszym gt, a które powoduje, że mamy dostęp na danym etapie. Tak.

**Lukasz Bott** 19:42  
No tak, no to akurat było tak, że te kilka kolejnych etapów, czyli wypełnienie kilka kolejnych sekcji wykonywała jedna osoba w danym momencie. Tak.

**Damian Kaminski** 19:45  
Wewnętrzny to był proces po prostu.  
No i nie był to ktoś z grantem pora, reakcje tak.

**Lukasz Bott** 19:55  
Nie wygram tę poradę akcesu, dopiero był na gdzieś tam na samym końcu, jak już były to formularz wypełniony.

**Damian Kaminski** 19:58  
Nowość.  
Dobra, to podsumowując mniej więcej rozumiecie o co chodzi, jaki jest na to, jaki jest problem? Może o tak, bo jeszcze rozwiązanie to do tego może możemy jeszcze dojść i dyskutować. Pytanie tylko czy?  
Była się czy mamy w czy ta propozycja na przykład Kamila, że to jest specjalny tryb wyświetlania, to jest dobry kierunek w ogóle co?

**Kamil Dubaniowski** 20:20  
Nawet teraz się wycofuje, oferuje się. Wycofuję się, to powinno być w takim razie ustawienie pre etap, no bo taki tryb jest wymagany tylko na konkretnym etapie, kiedy ktoś uzupełnia dane, ale później, jak już rekruter, na przykład przegląda, no to nie, to są zwykłe wtedy zakładki dla niego i on sobie je przechodzi przez nie jak chce w dowolnej kolejności, więc to powinno być pełen etat.

**Damian Kaminski** 20:29  
No właśnie.  
Tak masz lat.  
Może jeszcze inaczej, może to powinien być po prostu etap Grand tempora, reacts.  
Nawet powiedzmy, jeśli się nie zdecydujemy na walidację, czyli możemy podejść do tego na zasadzie mw, p to powiedziałbym w drugą stronę walidacja jest na końcu i to jest o k, ale poszczególne kliknięcie dalej powinno według mnie przynajmniej zapisać stan.  
Bo telefony mają tą perspektywę, że mamy gesty, może ktoś klikając w pole się pomylić, kliknie cofnij i wywala mu 150 pól.  
Które już wprowadził, więc powiedziałbym, że przynajmniej zapisanie tego, co już wprowadził przy przejściu dalej, czyli kole po 20, powiedzmy w pól sobie tam ustawą na sekcji już był sprawdziło.  
A walidacja nawet niech się odbywa, żeby tu nie konfliktować, że trzeba było opisać odrębne reguły pod daną sekcję i tak dalej to może to byłoby prostsze pytanie, tylko czy w ogóle chcemy coś takiego zaczynać się nad tym zastanawiać i proponować klientowi, że w tym kierunku byśmy szli, możemy to wyceniać czy nie? No bo na razie nie ma jeszcze na to zlecenia, bo przedstawiony jest problem, jest oczekiwanie na.  
Jakoś propozycję rozwiązania z naszej strony.

**Kamil Dubaniowski** 21:52  
Ja uważam, że to ma sens od dłuższego czasu i to nie tylko w tych tematach, nawet nasze tematy związane nie wiem tam gdzieś.  
Zgłoszeniem do wycen, żeby przeprowadzić tego użytkownika w takiej kolejności, w jakiej my chcemy, żeby nie szedł do dalszych zakładek, zanim nie uzupełni pierwszej. No bo możliwe, że uzupełnienie pierwszej wpływa na kształt tej ostatniej zakładki, tak, jakie tam pola się pokażą. Nie pokażą więc takie wizard roku prowadzimy ciepło formularzu, tak jak masz go uzupełnić. No moim zdaniem się przydawał modlić coś takiego małe pko, no i to wręcz mają jako takie pod etapy, dla etapu głównego i dla każdym etapie jest inny formularz, ale to jakby to jest właśnie na takiej zasadzie dalej, dalej i dalej.  
Więc u nas byłby to zbiorcze etap, nadal na przykład dekretacja, ale prowadzimy się przez formularz zakładka po zakładce.  
Nie skaczesz po tym jak chcesz?

**Janusz Bossak** 22:43  
Ja mam takie.

**Damian Kaminski** 22:43  
Czyli zamieniamy sekcję na kroki tak, powiedzmy tak to sobie zdefiniujmy, że jesteśmy w jednym etapie, ale na różnych krokach.

**Janusz Bossak** 22:51  
Ja mam takie przemyślenie, że to.  
Jak zwykle zależy tak.  
Nie wiem czy to się da jedno z drugim połączyć, znaczy sekcji jest tym wizardem, bo my mamy tak, że.  
Układ formularza sekcji jest jakby jeden tak, czy to na desktopie, czy na mobilnym, to w tej chwili to jest ta sama struktura.

**Damian Kaminski** 23:14  
Mhm.

**Janusz Bossak** 23:18  
Yy, może nie wiem, propozycja pierwsza może trzeba by robić osobny.  
Jakby formularzy nie w sensie osobny formularz, tylko osobny układ pól, które mamy do wyświetlania na widoku mobilnym. To jest pierwsza propozycja, czyli mamy te same pola, tylko inaczej może poukładane w inne części.  
Druga propozycja to jest taka.  
Że dla tego typu przypadku wypełniania danych.  
Yy, to rzeczywiście taki powinien być projektowany wizard tak, dlaczego mówię specjalnie o tym wypełnianiu danych, ponieważ ten przykład, który podałeś jakiś dekretacji już mi tutaj nie bardzo pasuje, bo to już jest bardziej złożony temat. Tak to nie jest sekwencja.

**Damian Kaminski** 24:06  
Jakie dekret kto podał tą?

**Kamil Dubaniowski** 24:08  
Kojarzyłem w sensie chodzi mi o to, że mamy tak kilka zakładek, gdzie na ostatniej masz wskazać osobę akceptującą tak, a tam na przykład jakiś filtr nakładamy w zależności od tego co tam zadekretował, a ktoś od razu idzie do tej ostatniej na przykład.

**Janusz Bossak** 24:18  
Tak, ja myślę.

**Damian Kaminski** 24:19  
Mhm.

**Janusz Bossak** 24:20  
Tak znaczy, wracając do myśli, to ja myślę, że to jest pewien szczególny przypadek wypełniania sekwencyjnego tak, czyli jako kandydat jako ktoś tam dostaje i tak, i że to nie jest praca na formularzu, jak jak to się dzieje właśnie w ramach dekry towania ja muszę zajrzeć nam gdzieś, nie wiem zobaczyć podgląd, potem wrócić, potem sprawdzić jeszcze coś dopiero dopisać tak dalej tak dalej tu mamy mamy sytuację pusty formularz.

**Damian Kaminski** 24:30  
Tak zdecydowanie według.

**Janusz Bossak** 24:52  
I idziemy krok po kroku, proszę uzupełnić imię, nazwisko PESEL. Pisałeś dalej. Teraz uzupełni dane rodziny, to to to popełniłeś dalej, idź tu, idź tu, idź tu i według mnie, powinniśmy to przemyśleć. Czyli jak zrobić?  
Takie właśnie ardy do formularza, który mamy tak, czyli formularz, formularz um, ale to jest pewien obiekt, taki wizard, który ma się odpowiednio zachowywać, w szczególności na widok.

**Damian Kaminski** 25:14  
Mhm.

**Janusz Bossak** 25:22  
Mobilnym, ale może nie tylko może no normalnej desktopy też.

**Damian Kaminski** 25:28  
Znaczy wiecie mobilny jednak jest ograniczony, więc tutaj takie prowadzenie jest dużo wygodniejsze, bo ciężej się w tym wszystkim połapać. Mamy mniej przestrzeni roboczej, ale według mnie to znaczy to tutaj Janusz powiedziałeś tam z polami, tak dalej, to już jest spojrzenie bardziej szerokie, ale nie mówię, że absolutnie nie chcę go wykluczać. Według mnie wydaje mi się tak, że powinniśmy zdefiniować tutaj persony aktorów, czyli co my chcemy zaopiekować? Przykład jeden to jest kandydat do pracy, przykład jakiś drugi to jest Kamila, ale no według mnie dekretacja faktury z mobila.  
Nie jest prostą sprawą, zwłaszcza jak tą tabelę, ale tego nie wykluczam i jak zdefiniujemy te przypadki użycia, to wtedy możemy podjąć decyzję, czy jesteśmy w stanie to zaaplikować jedną funkcjonalnością.  
Czy to jest nierealizowane, że tu trzeba zastosować inne rozwiązania dla tego aktora i takiego przypadku życia, a inne dla innego no najlepiej by było, gdyby dało się to zaaplikować jednym, ale to może być trudne.

**Kamil Dubaniowski** 26:31  
Czy dla mnie na ten moment to jest przypadek dosłownie, jak nazwał to Janusz, czyli wspieranie danych, żeby kandydat nie czuł takiego rozproszenia. Czy ja już byłem w tej zakładce? Nie byłem uzupełniają. To wszystko, co ode mnie chcieli, czy może nie wszystko to po prostu dalej walidacja wszystko ok, idziemy dalej mnie, no to od razu ci sygnalizujemy, że w karcie nie wiem. Członkowie rodziny nie zadeklarowały, że nie masz żadnych członków rodziny, więc Nie możesz iść dalej. No to jest to.

**Damian Kaminski** 26:55  
Tak tylko, że wymagana tylko, że wiesz, to są 2 aspekty walidacji jest walidacja wymagalności, którą pewnie jesteśmy w stanie w łatwy sposób wykryć i walidacja merytoryczna, czyli wykonanie reguły jakiejś, która jest na końcu de facto i możliwe, że wrócimy się na pierwszą zakładkę Jeszcze raz przechodzić wszystko, bo źle wypełniłeś nie wiem podałeś.  
A nawet nie tyle co przy zaciskowych, ale też automatycznych.  
No bo wali budujemy PESEL tak czy suma kontrolna jest o k, ale czy na tej pierwszej zakładce mamy wali dować też jakieś tam pole mam się wykonywać reguła z pola, który jest na kolejne zakładce, bo my dzisiaj reguły automatyczne szykujemy, często pr etap, a niepelne pole.  
Przynajmniej powiedzmy czasami po kilka etapów.  
I wiesz do czego zmierzam? Tak, że.  
W takim kontekście wizarda trzeba było szykować reguły automatyczne do tej sekcji.  
Przypisywać je jakoś do kroku.

**Kamil Dubaniowski** 28:04  
Czy to może teraz?

**Damian Kaminski** 28:04  
Żeby tu wykryć, że ktoś?

**Kamil Dubaniowski** 28:07  
Znowu ta koncepcja Łukasza tak, w sensie to obejście w sumie, ale może trzeba je dopracować, czyli zrobić taki.  
Dedykowany tryb etapu tak, czyli etap, ale ma pod zadania pod zadania opierające się na uzupełnianiu formularza.  
O czym to się? No w sensie, żeby diagram też się nie sypał przez to, żeby to był jeden etap aby diagramie, ale złożony z kilku kroków takich właśnie zbierania danych. Kilka kilka formularzy takich mniejszych, tam uzupełniać.

**Damian Kaminski** 28:36  
Dobra, słuchajcie temat jest jak widać trudny, chyba trzeba go poruszyć, nie wiem czy my jesteśmy w stanie dzisiaj go omówić.

**Kamil Dubaniowski** 28:37  
I wtedy mamy kod reguł, który?

**Damian Kaminski** 28:44  
Chyba trzeba wymyślić najpierw koncepcję taką designerską przez nas to było najwygodniejsze mając naszą perspektywę i potem skonfrontować to tutaj.

**Janusz Bossak** 28:55  
Tak tak to jest.

**Damian Kaminski** 28:55  
Zespołem deweloperskim.

**Kamil Dubaniowski** 28:57  
Bo bo tak naprawdę w rozwiązaniu Łukasza jedyny minus, bo mam nad tym pełną kontrolę, może sterować sobie tym Dalej Wstecz. Wszystko sobie opisuje w kodzie reguł, co ma się dziać, cofali dować, a jedyny minus tego jest taki, że jak masz nie wiem 10, no to diagram ci się rozsypie, bo aż 10 nadmiarowych etapów, które de facto są tylko zbieraniem danych, a etap to jest jeden uzupełnienie danych, taki procesor procesowych.

**Damian Kaminski** 29:06  
Mhm.  
Diagram tak.

**Lukasz Bott** 29:19  
Biznesowo to jest jeden etap, nie?

**Damian Kaminski** 29:21  
Czyli w tym kontekście tej propozycji jedyne co trzeba by było obsłużyć to, że Grand temporary może przyjąć wiele etapów.

**Lukasz Bott** 29:29  
Może przyjąć grom temporary.

**Kamil Dubaniowski** 29:29  
Tak.

**Damian Kaminski** 29:31  
I wyjście z któregokolwiek z tego etapu po prostu powoduje odebranie uprawnień.  
Przechodzić między nimi sobie można samemu i wtedy się ekran tylko odświeża.

**Kamil Dubaniowski** 29:49  
Czyli nie szedłbym do ograniczenia, że to tylko grant temporary robiłem to uniwersalnie, no bo wśród pracowników jak najbardziej też możesz mieć potrzebę zebrania danych na nowo.  
I i zrobić taki weekendowy tryb, etap, na przykład zmiana danych osobowych i i lecisz po kolei też z tym pracownikiem już wewnętrznym.

**Damian Kaminski** 30:10  
Nie nie, to tak jak powiedziałeś, w sensie to według mnie nie wyklucza tutaj po prostu zmieniamy kontekst działania Grand temporary, ale sam wyświetlenie formularza jest tak jak mówisz.  
No dobrze, to jeślibyśmy powiedzmy w taką stronę szli.  
Ee.  
To deweloperska jest do poprawy tylko grant temporary tak.

**Kamil Dubaniowski** 30:43  
Wydaje mi się, że może po przecinku wymienić etapy, na których ma być ten gta dostępny czy nie.

**Piotr Buczkowski** 30:48  
Co chcecie przez zmieniać etapy?

**Damian Kaminski** 30:49  
Teges.  
No.  
No jesteś jest w sumie.  
Właśnie chciałem to sprawdzić.

**Piotr Buczkowski** 30:57  
Nie róbcie tego.

**Lukasz Bott** 30:58  
I mnóstwo można wielu etapach, tak, czy w praktyce tak robisz, no.

**Piotr Buczkowski** 31:01  
Ale ale nie robcie nie róbcie tak proszę.

**Damian Kaminski** 31:04  
Czemu tak uważasz? Możesz to uzasadnić?

**Piotr Buczkowski** 31:06  
Że coś na każdym etapie będzie inny dostępna inna sekcja.

**Kamil Dubaniowski** 31:10  
Sekcja.

**Piotr Buczkowski** 31:11  
Ja to jest tak skomplikowane, że będzie, że nie.

**Damian Kaminski** 31:20  
Coś nie działa, chyba nie wyświetla się do końca.

**Lukasz Bott** 31:24  
Bo bardziej by tu pasowało. Chyba ten ta koncepcja, którą Janusz przedstawił.  
Mianowicie z tym, że jest jakiś specjalny tryb prezentowania dla mobilnych.

**Piotr Buczkowski** 31:34  
Znaczy to już bardziej wyświetlać sekcję jako formularze, tak?

**Damian Kaminski** 31:39  
Tylko tak jak powiedział.  
Milton musiałoby być na jednym etapie.

**Piotr Buczkowski** 31:46  
No tak.

**Janusz Bossak** 31:55  
A jak wygląda w ogóle teraz sytuacja kiedy?

**Piotr Buczkowski** 31:58  
Zmiana sekcje powoduje zapis na przykład tak.

**Damian Kaminski** 32:01  
Mhm no właśnie, czyli nie ma, czyli tutaj byśmy mieli, powiedzmy nawet zwinięte.  
Tutaj tego nie pokażę.

**Piotr Buczkowski** 32:21  
To powinno być też wybór tak czy aby jeżeli jest na przykład wysiasc jak zakładki to na telefonie inaczej to się zachowuje tak.

**Damian Kaminski** 32:29  
Co jest?  
Dobra.

**Piotr Buczkowski** 32:31  
Nie pokazuj tego procesu, bo mnie tak.  
Bo jak tu teraz na telefonie jest tak?

**Damian Kaminski** 32:41  
Już pokazy.  
Mamy już powiększą.

**Piotr Buczkowski** 32:51  
Dodajmy tutaj jakieś ładniejsza, tak?

**Damian Kaminski** 32:55  
Czyli co? Moglibyśmy to nie wiem może zrobić tak, że nawet jak wyświetlimy wszystko może być to plus tak, ale może być to także jedna sekcja naraz.

**Piotr Buczkowski** 33:02  
Jedno z.  
Jedna sekcja i lewo prawo tak następna poprzednia sekcja.

**Damian Kaminski** 33:10  
Albo tak, albo nawet jeśli w ten sposób, to po prostu kurde się nie wyświetla, dałeś.

**Piotr Buczkowski** 33:14  
I żeby też są dole były przeciski następna sekcja następną poprzednio sekcja tak.  
I szczęście powoduje zapis tak, żeby nie stracić danych.

**Kamil Dubaniowski** 33:25  
Czy to nawet andres sugerował na desktopa oni b.

**Damian Kaminski** 33:26  
Mhm.

**Kamil Dubaniowski** 33:30  
Niby za tym, bo jak mają dłuższy formularz?  
No to łatwiej im gdzieś się tam przełączać między sekcjami strzałkami, prawo, lewo nawet na dysku.  
Bo bo idą po prostu do kolejnej, nie potrze.  
No i tam cała tabelka z wszystkimi nazwami sekcji, bo oni uzupełniają te formularze, właśnie idąc po kolei.

**Damian Kaminski** 33:49  
No dobrze, ale to w takim razie możemy to zrobić także.  
Wtedy mielibyśmy.  
Rozumiem, że na dole włączamy przebywał przyciski następna sekcja poprzednia sekcja tak.

**Kamil Dubaniowski** 33:59  
Bo właśnie o to chodzi tak zobaczcie, że.  
Także, że pasek sekcji nie ciągnie się.

**Damian Kaminski** 34:03  
Nie widzimy tego, a włączamy tutaj, albo alternatywnie możemy widzieć i to i to tak.

**Kamil Dubaniowski** 34:04  
Mhm.  
Czy byłabys tak tak? Ja uważam, że mogłoby być, no bo czasami chcesz skoczyć z pierwszej na ostatnią, no to łatwiej tym, ale jak idziesz po kolei tak jak wam wreszcie swój przypadek biznesowy, no to wolą strzałki, tym bardziej, że sekcja czasami jest długa, oni zjadą na sam dół, skończyli uzupełniać no i co i tak się to na samą górę.

**Damian Kaminski** 34:22  
Mhm.

**Kamil Dubaniowski** 34:25  
Ee do belki sekcjami.  
A tak to mieliby strzał kiedyś tam nowelą.

**Damian Kaminski** 34:29  
No dobrze, tylko teraz następna sekcja miałaby być programowalna.  
Czy?

**Kamil Dubaniowski** 34:36  
Nie no, kolejny kolejność moim zdaniem.

**Damian Kaminski** 34:39  
Kolejność sekcji i widocznych w tym momencie, bo tu mogą być jeszcze, wiesz, sekcje techniczne nie o tak jak tu masz.

**Piotr Buczkowski** 34:46  
No ale jeżeli sekcja jest niewidoczna, to jest niewidoczna po prostu.

**Damian Kaminski** 34:48  
No tak, tylko o k.  
No dobrze, czyli podsumowując do robilibyśmy przyciski następne sekcje z tej perspektywy, p teta lista jak rozumiem jest musiałaby być opcjonalna, czyli jeśli włączam to to mam jednocześnie checkbox Ukryj sekcję jako zakładki.

**Piotr Buczkowski** 35:24  
Nie na tym powinno to wejść tylko powinno być zakładki, tylko też też przyciski tak.

**Damian Kaminski** 35:32  
No dobrze, a w przypadku modelowego też powinny być widoczne tak jak teraz i tu przycisk następna sekcja wtedy się to zamyka, to rozwija.  
Czyli wtedy mamy coś takiego czy tu tylko zakład przyciski?

**Piotr Buczkowski** 35:43  
Nie.  
Nie chyba tutaj tylko tylko jedno, tylko jedna bieżąco naraz.

**Damian Kaminski** 35:54  
Czyli na dole przyciski poprzednio sekcja następna sekcja powodujące zapisanie stanu formularza.

**Piotr Buczkowski** 36:02  
Obiekt po prostu też też też tak jak teraz, tylko z przyciskami, tak.  
Nie ma stąd rozwijania sekcji, tylko.

**Damian Kaminski** 36:12  
Tylko przechodzimy.

**Piotr Buczkowski** 36:14  
Tak.

**Damian Kaminski** 36:20  
I w tym czasie się zapisuje formule sz.

**Piotr Buczkowski** 36:21  
Pojawiamy na dole tylko według mnie powinno być na dole tylko następna sekcja na to, że poprzednia.  
Jeden przycisk.

**Damian Kaminski** 36:32  
Na Górze tak, tak uważasz?

**Piotr Buczkowski** 36:34  
Na Górze poprzednia, a na dole nas.

**Damian Kaminski** 36:39  
No nie wiem, to znaczy o k. Ja tak nie myślałem.

**Piotr Buczkowski** 36:43  
Wypełniam sekcję ce przejdź do następnej, przejdź do poprzedniej to to z króluje na górę.

**Damian Kaminski** 36:46  
Rozumiem o co ci chodzi? Tak, ale.  
Zastanawiam się, czy kiedykolwiek widziałem takiego typu podejście.  
W innych narzędziach nie, bo nie wiem jak przeglądam nawet na.

**Piotr Buczkowski** 37:00  
Rzadko jest kiedyś także to kończy. To chodzisz do końca danej sekcji dla danego kroku.  
I to jako jakaś kroku jakiegoś tam czy coś i chcesz wrócić.

**Damian Kaminski** 37:19  
Rozumiem twoją logikę.  
Po prostu zastanawiam się o widzisz jak tu jest.  
W lewo w prawo mam tutaj tak, w sensie jedno obok drugiego, czyli nawigacja jest w jednym miejscu, a nie tak, że gdzieś tam tu na Górze, poprzednie, tu na dole następne zastanawiam się po prostu, czy to jest poza tym, że.

**Piotr Buczkowski** 37:37  
No ale.  
Pytanie, czy to będzie potrzebny? Tak.

**Damian Kaminski** 37:43  
Nie wiem.

**Piotr Buczkowski** 37:43  
Czy nie będzie rozpraszać tylko?  
Ten powód?

**Damian Kaminski** 37:53  
Nie wiem, dobra, trzeba to przemyśleć, ale o k. Konkluzja jest taka, że mamy przyciski na razie gdzie one będą czy ro.  
Czy skondensowane w jednym wierszu to już jest wtórny? Według mnie po prostu mamy przyciski.  
I pod przyciskami robi się zapisz tak przynajmniej no tak pod każdym, bo jak jeśli wracam na poprzednie.

**Piotr Buczkowski** 38:14  
Robi zapisz i otwieram następną sekcję albo poprzednio zależności.  
Mogą być widoczne te sekcje tak może jakoś.  
Żeby było widać, także jesteśmy w którejś tam sekcji.

**Damian Kaminski** 38:34  
No dobrze to.  
Do wyceny i dokładnego projektu możemy podejść później, natomiast teraz podejmiemy decyzję, że że oferujemy klientowi taką opcję i wstępnie możemy powiedzieć, że tak to będzie wyglądać. Czy mamy się nad tym skupić i przygotować jakieś mopy właśnie i wycenę? Czyli pomysł jest taki i na.  
Tutaj w formie wyświetleń i na desktopie i na telefonie będą dostępne na dole formularza przyciski. Aha, dobra, nie będą na formularzu dostępne przyciski następna poprzednia sekcja, które będą powodować zapisanie.  
Jeśli chodzi o walidację, będzie ona się odbywać na końcu nie będzie się od tu się powoduje tylko i wyłącznie zapisanie stanu bieżącego.  
Natomiast sama walidacja.

**Piotr Buczkowski** 39:20  
Możemy dodać dodatkowe.  
W tym zdarzeń, tak.  
W regule automatycznej, że wykrywa, że zmiana sekcji.

**Damian Kaminski** 39:31  
Ale to już jakieś vip 2, powiedzmy tak.

**Piotr Buczkowski** 39:33  
No tak.  
Żeby można było popróbować, że wiesz na przykład, że ktoś wypełnił właśnie sekcję 2 i sprawdzasz po sekcji 2 jest wszystko o k.

**Damian Kaminski** 39:45  
O k. Jeśli nie jest o k, to to zatrzymujesz go na tym.

**Piotr Buczkowski** 39:47  
To zwracasz błąd i.

**Damian Kaminski** 39:51  
No dobra.

**Piotr Buczkowski** 39:52  
Nie wyszukasz komunikat i nie przechodzić teraz w tej sekcji.

**Damian Kaminski** 39:57  
No dobra.  
Kamil uważasz, że coś jeszcze trzeba tutaj dopowiedzieć?  
I tu wyświetlamy na bieżąco jedną z sekcję nie pokazujemy jakie są kolejne i poprzednie. Tak tak piotrze tu sugerowałeś.

**Piotr Buczkowski** 40:24  
Według mnie możemy się tak jak wyświetlamy, tylko nie pozwalamy przejść.  
Fakt normalnie tak rozwijać.

**Damian Kaminski** 40:32  
Czyli nie ma plusów minusów?

**Piotr Buczkowski** 40:34  
Tak.

**Damian Kaminski** 40:35  
Jest przycisk poprzednia następna i na tej podstawie rozwija się kolejny akordeon.  
A zwija się poprzedni no dobra, no mamy jakąś propozycję, dajmy ją tak wstępnie, zobaczymy co klient powie czy.  
Czy to jest słuszny kierunek, czy oni chcą więcej mniej inaczej i ja?  
Się wypowiedzą to można przygotowywać jakiś.  
Jakieś pod tom okap dobra to w takim razie będę tylko potrzebował dostępu do transkrypcji, żeby chociaż tam mogę zrobić tego opis tego kopa. Ilo to dobra kolejny temat.  
Piszę to do siebie.  
Czy coś jeszcze mamy kluczowego? Mamy ostatnie już jesteśmy po czasie, ale powiedzmy nie wiem czy w ogóle nie wydłużyć tych naszych spotkań, żeby była zaplanowana godzina po prostu.

**Janusz Bossak** 41:35  
A może tak zrobić? Ja bym chciał może wykorzystać tej Piotra i o tym jotter wła porozmawiać.

**Damian Kaminski** 41:47  
No właśnie.

**Lukasz Bott** 41:48  
Ja ja się rozłączam, bo mam spotkanie za chwilę.

**Janusz Bossak** 41:52  
Dobra.

**Anna Skupinska** 41:53  
Ja też o innych rzeczy. No cześć.

**Janusz Bossak** 41:55  
Hej.

**Damian Kaminski** 41:58  
Kamil ty preferujesz temat?

**Kamil Dubaniowski** 42:01  
Tak tylko ja mam 9 minut, bo lot mam o jedenastej.  
Tam to tak.  
Tak wie wszystko to ja nie wiem komu może lepiej markę od razu dzwonić, jeśli jego tutaj przewidujemy, że przejmie temat.  
Tak robimy czy.

**Damian Kaminski** 42:21  
No to tak tak, jeśli Piotr wszystko wie, tylko podsumujmy to.

**Kamil Dubaniowski** 42:24  
Tak, no znaczy, Piotrek przekażę tak bardziej o to chodzi, żeby mareks, no tak zakres i pewnie powinni się też chłopaki spotkać się wszystkie nie wiem czy z nami czy są oddzielnie.  
Doprecyzować Amerykę teraz to zdąży w te 9 minut co najwyżej wdrożyć. O co chodzi?  
Jest.

**Marek Dziakowski** 42:42  
Cześć.

**Kamil Dubaniowski** 42:43  
Cześć, to może wtedy smake chwilę?

**Marek Dziakowski** 42:46  
Tak, tak, oddzwoń.

**Kamil Dubaniowski** 42:48  
Temat na przyszły sprint już raczej, bo Piotr tam będzie nieobecny przez pierwsze dni sprintu a a jest to jakby element wdrożenia, które realizujemy w locie.

**Marek Dziakowski** 42:50  
Mhm.

**Kamil Dubaniowski** 42:59  
Ee temat jednolitej, jednolitego, rzeczowego wykazu akt i obserwuja w skrócie biznesowo.  
Temat polega na tym, że.  
Użytkownik musi wybrać pewną klasyfikację na formularzu i i tyle, jakby taki bardziej złożony Słownik ze strukturą.  
Zależności i Plan jest taki, żeby zrobić to na zasadzie działania takiego jak działa guster yt nie wiem czy się orientujesz w tym dosyć specyficznym słowniku, ale jest to Słownik, który działa nieco inaczej niż źródło znaczne, tak które które działa w polu Odnośnik do źródła zewnętrznego na formularzu.

**Piotr Buczkowski** 43:36  
Jest to źródło zewnętrzne.

**Kamil Dubaniowski** 43:44  
Tutaj akurat w tym guster jak rozumiem, my sięgamy po dane gdzieś tam na zewnątrz, natomiast w tym iotova to będzie po prostu sięganie bezpośrednio do tabeli amo tita, no bo dane będą uzupełniane przez klienta to już tak wyła, każdy ma inne struktury tych.  
W kategorii oferta była mają inną zależności, mogą być inne i potrzeb.  
Wiemy odtworzyć de facto to, jak działa busted.  
Przełożyć to na te schematy i odwoła.

**Marek Dziakowski** 44:14  
Czyli no o k. Czyli funkcjonalności od strony al.  
Mają być takie same jak ma gust teryt, a jeżeli chodzi o uzupełnianie danych no to tutaj się tym nie przejmujemy. Nie potrzebujemy tego jakoś tam.

**Piotr Buczkowski** 44:26  
Znaczy.

**Marek Dziakowski** 44:28  
Uzupełnić automatycznie.

**Piotr Buczkowski** 44:29  
Ogólnie to nie to nie jest, mimo że to jest jakaś tam drzewko to nie jest wybierani z drzewka, to jest wybieranie z listy, pojedyncza jest wyszukiwaniem tak.

**Damian Kaminski** 44:37  
Tylko.  
Jak wy to powiedzieliście, to?  
Z mojej perspektywy to nie rozumiem koncepcji działać jak guster TW, jakim zakresie czy Marek tatowie.

**Piotr Buczkowski** 44:51  
Już pokazuje, już pokazuje.

**Marek Dziakowski** 44:51  
Nie gdzieś tam miałem krótką styczność tylko z guster yt.

**Damian Kaminski** 44:54  
Bo.

**Marek Dziakowski** 44:57  
Wiem, że jest.

**Piotr Buczkowski** 44:57  
Definiujesz definiujesz klasę.  
I o ten własne source.  
O implementując o taki.  
Pakiet interfejs.  
Projekt trujesz źródło danych jako te 5.  
Tutaj jeszcze trwał tam jakieś tam.  
No w jej sonie chyba tak co będzie zapisywane w.  
Jaka wartość będzie zapisywana w polu tekstowym tak wybraniu?  
Niż.

**Marek Dziakowski** 45:34  
Mhm.

**Piotr Buczkowski** 45:34  
No i tutaj sobie co sobie tutaj czujesz, to to twoje.

**Marek Dziakowski** 45:40  
K sekundka tylko bo coś ktoś dzwoni studentka nawracam.

**Damian Kaminski** 45:49  
Czyli funkcjonalnie będzie można szukać po dowolnej wartości? Tak nie początku.

**Piotr Buczkowski** 45:54  
Po tym, co po tym co zaprojektujesz po tym co Marek, czy ktoś tam za zaprogramuje.

**Damian Kaminski** 46:02  
Ta programuje czyli nie konfiguracyjny nie tylko.

**Kamil Dubaniowski** 46:06  
Czy wiecie możemy, no, bo potem będziesz szukał, będziesz szukał po symbolu, będziesz szukał po nazwie.

**Damian Kaminski** 46:11  
Albo po nazwy, no bo tych 2 rzeczach.

**Piotr Buczkowski** 46:12  
W tym momencie szuka, szuka po, może nie po wszystkim tak większość ciepło.

**Kamil Dubaniowski** 46:12  
No i.

**Damian Kaminski** 46:18  
Tu mamy z założenia 2 pola, tak, mamy pole symbol jako id biznesowe.  
I nazwę jako opis tego symbolu.

**Piotr Buczkowski** 46:26  
No tylko tutaj się odwołuje gdzieś tam tak.  
Web serwisu, żeby ta i tam przekazuje tak co co szukasz no tutaj będzie sam w sobie tych tabelach lokalnych szukał.

**Marek Dziakowski** 46:38  
Już Jestem.

**Janusz Bossak** 46:39  
Tak, bo tutaj nie będzie tego tak guster to jest zasilanie z zewnątrz.

**Marek Dziakowski** 46:44  
Tak to kojarzy.

**Janusz Bossak** 46:44  
A tutaj nie ma tego zasilania z zewnątrz, po prostu my raz zasilimy te tabelki.

**Marek Dziakowski** 46:48  
Mhm.

**Janusz Bossak** 46:51  
Yy tą strukturą ter była później dorobimy do tego interfejs użytkownika, który będzie to można robić, ale na razie zakładamy, że ta tabele zostaną jednorazowo poziomu bazy danych uzupełnione, a celem tej operacji jest umożliwienie. Nie wiem kto to pokazuje w tej chwili, ale tak jakby na na sprawie pokazać jak działa guster yt.

**Damian Kaminski** 47:10  
Piotr.

**Piotr Buczkowski** 47:10  
Ja.

**Janusz Bossak** 47:15  
Yy, chodzi o to, że jest pole, które jest polem Odnośnik do źródła zewnętrznego. Wybrany źródłem zewnętrznym jest w tym przypadku guster yt, a dlatego jote RA to będzie wybranym źródłem zewnętrznym jotter va trzeba takie przygotować.

**Marek Dziakowski** 47:29  
Mhm.

**Janusz Bossak** 47:32  
I to się zachowuje wtedy w ten sposób, że w tym polu odnośnie jak zaczynasz, dlatego mówię o tym guster tak pisza miast stara szkolna tak jak ja mieszkam czy Bydgoszcz to on wyszukuje, zgadza.

**Damian Kaminski** 47:38  
Już pokazuje, przejmę ekran.

**Piotr Buczkowski** 47:44  
To nie pozwolicie mi pokazać?

**Janusz Bossak** 47:45  
Słońce się.

**Damian Kaminski** 47:47  
Dobra proszę.

**Janusz Bossak** 47:50  
No i to samo ma się dziać ja to a tak czyli ktoś pisze tam nie wiem dokumenty rady nadzor.  
No i no i on mu wyszukuje, który to jest węzeł w tym pioter włanie i jak on kliknie, że to jest to no to mu się tam.  
Do tego pola czy pisze?

**Marek Dziakowski** 48:09  
Czyli.

**Janusz Bossak** 48:11  
I jeszcze najlepiej, gdyby zwracało jasona z pełną informacją o tym, co tam zostało wybrane i wtedy ktoś w ramach reguły.

**Piotr Buczkowski** 48:18  
Tutaj tutaj.

**Janusz Bossak** 48:20  
Będziemy tego użyć.

**Piotr Buczkowski** 48:22  
W rycie zwraca pełnego jasona tutaj nie musi tak, bo może tak.  
Gus, to musielibyśmy się za każdym razem z reguły odejmować gdzieś tam, bo tak mamy możemy lokalnie się odwołać.

**Damian Kaminski** 48:36  
Znaczy, ja mam pytanie wyżej poziomo w sensie, a czemu dać sterling?

**Piotr Buczkowski** 48:39  
Dobrze, coś mi to długo.

**Damian Kaminski** 48:44  
Żeby pokazać ten buster yt?

**Piotr Buczkowski** 48:45  
Nie ja chcę pokazać, jak to wewnętrznie działa w kodzie, tak.

**Damian Kaminski** 48:46  
Swoje.  
O k dobra no dobra, a ja zapytam wyżej poziomo.  
A czemu w ogóle idziemy w tą stronę a nie zwykły rejestry?

**Kamil Dubaniowski** 48:57  
Gdzie wydajniej?

**Janusz Bossak** 48:57  
Bo to jest wygodniej.  
Szybciej wygodniej.  
Wydajniej.

**Damian Kaminski** 49:02  
Ale w sensie szybciej, no dobra, wydajnie to.

**Kamil Dubaniowski** 49:02  
No i nie, nie, nie, nie dotykamy jest definition. To jest główna zaleta.

**Damian Kaminski** 49:06  
Ok.

**Piotr Buczkowski** 49:08  
To Dlaczego nie jedziecie w słowniki zagnieżdżone?

**Damian Kaminski** 49:08  
Dobra, to znaczy.  
W niedzielę tak nie idziemy w słowniki, ale możemy.

**Piotr Buczkowski** 49:14  
Hierarchicznym.

**Janusz Bossak** 49:15  
Tak znaczy.

**Kamil Dubaniowski** 49:15  
No tak no tutaj temat uprawnień to raz będziemy jeszcze rozwijać, d.

**Piotr Buczkowski** 49:15  
Panie rejestr.

**Kamil Dubaniowski** 49:22  
A temat?  
Parametrów, które opisują do mnie katalog.  
W słownikach trzeba by się tam bawić tymi.

**Damian Kaminski** 49:30  
Nie, ale to ja nie mówię o słownikach, a a o rejestrach w sensie, bo chcę zaraz rozwinąć myśl w kontekście powiedzmy potencjalnie w ogóle rejestrów kontrahentów, tak, żebyśmy popatrzyli na to.

**Janusz Bossak** 49:43  
Nie, już ustaliliśmy, że robimy tak, nie, nie, nie kombinujmy teraz już no nowych.

**Damian Kaminski** 49:49  
Ale ja nie podważam Janusz tylko może Jeszcze raz powiem wszystko, że może za chwilę jak zrobimy to tutaj, bo tu mówimy, nie wiem, tam będzie w tym jotter wołaniem 150 200 jak będzie 500 pozycji, pewnie max.  
Ale pytanie, czy tego samego mechanizmu, który tutaj w ten sposób sugerujecie, nie powinniśmy później zacząć wykorzystywać do przeszukiwania kontrahentów.  
Pod w kontrahentach często mamy 100000 i pytanie, czy to rozwiązanie, które tu planujecie, będzie wykorzystywane właśnie czymś innym?

**Janusz Bossak** 50:14  
No.

**Piotr Buczkowski** 50:21  
To jest, nie to jest rozwiązanie do jotter w ua.

**Damian Kaminski** 50:24  
O k.

**Piotr Buczkowski** 50:25  
Tylko i wyłącznie do orła proszę nie.

**Damian Kaminski** 50:25  
Tylko dobra.

**Piotr Buczkowski** 50:29  
Nie generalizuj się ich od razu, bo bycie kupa.

**Janusz Bossak** 50:32  
Tak, tak, tak, tak znaczy?

**Damian Kaminski** 50:33  
Dobra, rzucam tylko, że dobra jak przemyślane to k.

**Janusz Bossak** 50:35  
I dla.  
Natomiast idea tego tak jakby będziemy mieli tutaj dla guster ryt i dla JR była to taka idea może być stosowana czy mogłaby być powielana do innych rozwiązań? Te 2 akurat źródła charakteryzują się.

**Damian Kaminski** 50:47  
Mhm.

**Janusz Bossak** 50:51  
Jednym ważnym elementem są praktycznie stałe, niezmienne.  
Nie ma na nich pracy, tak jak masz konto jest kontrahentów to tam nagle zmieniasz adres tego kontrahenta coś tam no.

**Damian Kaminski** 51:05  
Powiedziałbym, że to akurat jest takie samo, czyli adres kontrahenta zmienia się tak rzadko jak i o r buła.

**Janusz Bossak** 51:08  
Nie.

**Piotr Buczkowski** 51:10  
To tak naprawdę ja też wywoła. To jest Słownik z uprawnieniami.

**Janusz Bossak** 51:11  
Nie.  
Muszę się przełączyć na przemka, także idę tam.

**Kamil Dubaniowski** 51:16  
Też za chwilkę uciekam na ten lot, więc znaczy tak kluczowe, żebyście może jak najwięcej teraz Piotr Marek przez te dni, kiedy jeszcze Piotrek jesteś, przekazali sobie tej wiedzy, a.

**Piotr Buczkowski** 51:25  
Marek, zostawmy stajnie chwilę okej, możesz?

**Kamil Dubaniowski** 51:28  
Tak, tak, a ja Marek też jeszcze, bo bo jest kilka niuansów różnych od tych bustryk, bo na przykład tutaj będzie struktura, czyli są jakieś katalogi nadrzędne i podrzędne.

**Marek Dziakowski** 51:28  
Dobrze.

**Piotr Buczkowski** 51:37  
Dobrze, ja pokażę jak to technicznie jest zrobione, tak.

**Kamil Dubaniowski** 51:41  
Dobra, a później ja ja się rozpiszę fischera z funkcjonalnościami, których będziemy na pewno oczekiwanie na dalszym etapie tak, czyli, że są jakieś katalogi, których nie da się wybrać, bo to są katalogi nadrzędne, powinno się tylko te najniższego poziomu. To będą jakieś niuanse, ale to już w kontekście samego pola wyboru.

**Marek Dziakowski** 51:47  
O k.

**Kamil Dubaniowski** 51:57  
Mm ja uciekam na tym odcinki.

**Damian Kaminski** 52:00  
No dobra, ja się chyba też przyłączam. Zostawiam was.

**Piotr Buczkowski** 52:04  
Dobrze, to ja mówię. Ogólnie jest źródło danych typu 5, czyli klas.

**Damian Kaminski** 52:04  
Na razie.

**Piotr Buczkowski** 52:10  
Podajesz jakoś nazwę, podajesz klasę?  
Która obsługuje to?  
Plujesz sobie tutaj też trzeba to jaki jest to jest, to jest wartość, która jest zapisywana w polu caesar w case definition, tak.  
Implementuje klasę, która to też klasy, która implementuje te interfejs, tak jak go stery Souls, tak.  
Obiec kilka tych.  
Taką jest zwraca powiedzmy, jpg z 2 2.  
Property sami.  
To jest zapisywane w bazie, najlepiej jest wyświetlane tak.  
Tutaj to jak zrobisz tecz tutaj pewnie.  
Pewnie tutaj przekazuje tak tutaj w szokuje to trzeba po prostu sobie sam też do końca nie pamiętam.  
To jakieś dodatkowe funkcje, która popierają tak jak jest, jakie są properties zdefiniowane ten powiedzmy guster Street.  
Tutaj powiedzieć miano stałe zapisane, no bo.  
Tutaj pewnie będziesz chciał takie funkcje to robić, które wyszukują i na koniec zwracają obiekty do zapisania w bazie danych. Tak.  
Czy to wartość do zapisania w bazie danych?

**Marek Dziakowski** 53:35  
K.  
Tam jeszcze była jakaś kwestia uprawnień, to trochę nie zrozumiałem.

**Piotr Buczkowski** 53:43  
To było normalnie słowniku, to każdy może każdy każdy opozycję słownika wybrać co nie, a tutaj będzie tak, że będzie tabelka. To będzie oddzielna tabela, tak?

**Marek Dziakowski** 53:49  
Tak, tak.

**Piotr Buczkowski** 53:54  
Gdzie będzie, jak powiedzmy pozycja dotarła i kto ma uprawnienia do wybrania tej pozycji, czyli ty będziesz po prostu tutaj w jakimś selekcję musiał uwzględnić, że masz uprawnienia do tej pozycji, że możesz wybrać tylko te pozycje, które do których masz uprawnienia.

**Marek Dziakowski** 54:10  
O k. Czyli ok.

**Piotr Buczkowski** 54:10  
Gdyby nie to to to to można było słownikami z hierarchicznym i załatwić.

**Marek Dziakowski** 54:17  
No ma.

**Piotr Buczkowski** 54:22  
Tam też są zasady takie, że na przykład możesz tylko wybrać.  
Pozycje, które tam mają oznaczone, że możesz je wybrać, tak.  
Na przykład widzisz drzewko, ale Nie możesz wybrać tych.  
Nie gałęzi, tak, nie nie najniższej gałęzi.

**Marek Dziakowski** 54:35  
Czerni.  
Oczywiście.

**Piotr Buczkowski** 54:40  
Liście liście osiądziemy tak.

**Marek Dziakowski** 54:44  
Jasne, no to zrozumiałem.

**Piotr Buczkowski** 54:48  
No ale to już tak liścia mogłabyś tam różnym poziomie, tak?

**Marek Dziakowski** 54:52  
Mhm no tak tak, no jak dobrze wiem o k no więc nie rozumiem.

**Piotr Buczkowski** 54:56  
No ale technicznie te technicznie to jest po prostu to źródło danych typu klasa.

**Marek Dziakowski** 54:57  
Aby.

**Piotr Buczkowski** 55:03  
To trzeba zrobić w klasę, która implementuje.

**Marek Dziakowski** 55:08  
O Ki do tego do przetrzymywania danych z samego JRWA będzie jedna tabela, a do.

**Piotr Buczkowski** 55:14  
Będą 2 tabele 2 albo 3 tabele. Już nie pamiętam. Tam było zaproponowane tak czyli.  
Lista pozycji, uprawnienia do pozycji.  
I przypisanie.  
Czy się jeszcze być? Ale nie pamiętam w tej.

**Marek Dziakowski** 55:33  
A jest gdzieś to opisane?

**Piotr Buczkowski** 55:33  
No bo.  
Tak.

**Marek Dziakowski** 55:37  
My się jakoś wycena czy coś.

**Piotr Buczkowski** 55:40  
Kamila mi się spytać.

**Marek Dziakowski** 55:41  
Dobra tak zwanego po.

**Piotr Buczkowski** 55:44  
Ogólnie to jest tak, że właśnie to jest chyba.  
To jest to jest do serca tak się dziwnie nazywają, bo tak zrobione, że źródle zewnętrznym tak to jest do.  
Pobierania wybranej wartości, ale to nie pamiętam.  
To czego?

**Marek Dziakowski** 56:06  
No to sobie najmniej przejrzy.  
Co do czego jest jeszcze dobra?  
To kiedy to trzeba zrobić w przyszłym sprint czy przyszły tydzień?

**Piotr Buczkowski** 56:15  
To do Kamila pytanie.

**Marek Dziakowski** 56:19  
Dobra, to też zrobię.

**Piotr Buczkowski** 56:23  
No to to teraz tylko.

**Marek Dziakowski** 56:25  
Dobra, to jest zapis z tego spotkania, to w razie co tam będę sobie do niego odwoływał się grę i coś tam.

**Piotr Buczkowski** 56:29  
Mówię tak na szybko. To właśnie, że w tej to tejże bors szukaj minus jeden guster yt.

**Marek Dziakowski** 56:37  
Mhm.

**Piotr Buczkowski** 56:38  
Masz tura to jest klasa na tym się trzeba wzorować.

**Marek Dziakowski** 56:42  
Dobra.

**Piotr Buczkowski** 56:43  
Tak tutaj trzeba tylko właśnie.  
To plus to jest ważne, tak?

**Marek Dziakowski** 56:48  
Mhm.  
Dobra.  
To jak coś to w kontakcie mam.

**Piotr Buczkowski** 56:55  
No to tylko tak.

**Marek Dziakowski** 56:58  
Cześć.

**Janusz Bossak** zatrzymano transkrypcję
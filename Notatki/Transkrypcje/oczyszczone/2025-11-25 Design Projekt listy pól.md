**Data spotkania:** 25 listopada 2025, 11:36

---

**Kamil Dubaniowski:** Przechodziłem prostu klikając już na tym, co mamy później. Uznałem, że i tak warto zrobić projekt w firmie. Zacząłem to tam w piątek przekładać na firmę. Wstecznie, bo już dużo z tego mamy. I aktualnie wygląda to w filmie, tak?

**Janusz Bossak:** Ale co to jest?

**Kamil Dubaniowski:** To jest projekt listy pól.

**Janusz Bossak:** OK.

**Kamil Dubaniowski:** Przełożona troszeczkę, wiadomo, tam firma narzuca jakieś tam swoje style, mimo wszystko na tych bibliotekach Ant Design na się wysypuje, więc jej tam nie maltretuję, to będzie trochę inaczej wyglądać. Nasza to szczegóły i tak co chciałbym omówić. Jako pierwsze dyskutowaliśmy tam w zeszłym tygodniu o tym, jak dodawać z tego poziomu nowe pola i nowe sekcje, żeby to było intuicyjne i żeby było też kontekstowe, czyli nie po prostu nowe pole, gdziekolwiek, tylko pole w miejscu, w którym chcę je dodać, czyli już bez później przeciągania w odpowiednie miejsce. Chcę pole tu do mniej więcej w tym miejscu jest ta akcja dodania i na wzór tego, co jest na blogu, w sensie, jak to zrobił sobie. Jak ktoś zrobiona na detoksie mamy tego Plusa, dodałem tutaj na hover, że jak się najeżdża to po prostu też ta linia sugeruje gdzie ten element będzie dodany, czyli jak dojadę tu to widzę tą linią, że to będzie coś pod spodem. I potencjalnie coś takiego jest w stanie na tej tabeli Ant Design-owej Filip zrobić osiągnąć, tylko jak doszedłem do poziomu tabeli, czyli to jest pole typu tabela. I tutaj ten plusik. Będzie mylący, bo może być odbierany jako dodanie pola w tabeli.

**Lukasz Bott:** Albo pola pod tabelą.

**Kamil Dubaniowski:** I to on uczy tak, tak, tak to zrobi dokładnie tak, czyli ten plus tak naprawdę służy do dodania nowego pola na tym poziomie, czyli i pod tabelą nowe pole na formularzu głównym pod tabelą. A jak chcesz dodać pole w tabeli, to musisz rozwinąć sobie tabelę i dodać z tego poziomu tu lub tu.

**Lukasz Bott:** To okej.

**Kamil Dubaniowski:** Tak, tylko uważam, że właśnie to będzie mylące, że ktoś jak będzie miał taka rozwinięte i kliknie tutaj go Plusa to uzna, że doda pole w tabeli, a tak naprawdę doda mu się pole na formularzu głównym pod tabelą.

**Janusz Bossak:** A mieliśmy taką koncepcję, żeby ten plus na poziomie sekcji. Chociaż nie dobra, odeszliśmy od tego dobra, chodziło mi o to, że mogliśmy.

**Kamil Dubaniowski:** Tak, on dodaje pole w sekcji albo dodaje sekcję poniżej, czyli na poziomie sekcji jest podwójna akcja tak naprawdę, bo my nie wiemy, czy chcesz dodać pole w tej sekcji, czy dodać.

**Janusz Bossak:** To to samo zróbmy na poziomie tabeli.

**Kamil Dubaniowski:** Czyli tutaj dodaję plus i pyta mnie czy chcę dodać. No tak, ale do której sekcji mamy dodać w tej tabeli? Bo dodawanie pola, tabela ma swoje sekcje zawsze, nie da się dodać swobodnego pola do tabeli. Trzeba dodać w konkretnej sekcji. Czyli.

**Janusz Bossak:** Ja bym zrobił tak. Nie wiem.

**Damian Kaminski:** Mamy bardzo tak, powiedziałbym rozbudowany te opcje.

**Kamil Dubaniowski:** Ja tutaj jakby idąc do.

**Damian Kaminski:** Ale dzięki temu też się tłumaczą, bo jak sam plus by były niezrozumiałe.

**Janusz Bossak:** Tak. Nie. Według mnie powinno być tak jak zrobiłeś, jest okej?

**Kamil Dubaniowski:** Będzie to na pierwszy kontakt, po prostu może być zaskoczeniem intuicyjne, ale to jest na pierwszy raz, później będzie dla ciebie raczej, jak ktoś zna zasady i wierzę. W sekcji są tabele, to wie, że takie dodanie nie ma sensu, bo nie wiemy, do której sekcji, jak ci to miałoby się dodać. To, powiedzmy, że jakaś tam zasada nasza jest, wynika z drugiego.

**Damian Kaminski:** Znaczy, ale to poczeka jeszcze raz, kiedy jest podpowiedź, jak kiedy jest od razu wywołanie akcji.

**Kamil Dubaniowski:** Pytanie nie, podpowiedź jest w momencie, kiedy dodaje.

**Damian Kaminski:** No.

**Kamil Dubaniowski:** Używać Plusa na poziomie sekcji, bo my nie wiemy czy chcesz dodać pole w tej sekcji, czy chcesz dodać sekcję nową? Czyli z poziomu jednej sekcji wywołuje, że dodanie nowej sekcji, takie jest założenie, też to też nie wiem czy jak?

**Damian Kaminski:** Dobra, a pokaż jeszcze raz jak na tabeli klikniesz to od razu się otwiera okienko tak.

**Kamil Dubaniowski:** Tak, bo jak kliknę na tabeli to jest tak jak zwykłe pole, Odnośnik, pole, tabela, ona po prostu dodaje nowe pole na formularzu głównym pod tym.

**Damian Kaminski:** A jak rozwiniesz tabelę już tam dodasz to doda do tabeli, tak?

**Kamil Dubaniowski:** Jak rozwinę tabelę, to była rozwinięta czekajcie, to mam sekcję, i muszę zdecydować, do której sekcji w tej tabeli ja dodaję. Chcę dodać do tej to tu, jak do tej to tu.

**Damian Kaminski:** Mhm, a jak na polu klikam plus to od razu do tej sekcji się dodaje, tak?

**Janusz Bossak:** Wiesz, wiesz, znaczy.

**Kamil Dubaniowski:** Tu tak to od razu do tej sekcji mi dobry w tym miejscu pod spodem.

**Damian Kaminski:** To trzeba po prostu zrozumieć. Według mnie to jest do nauczenia tam raz ktoś popełni błąd i już będzie wiedział jaka jest logika. Nie da się mieć wszystkiego.

**Kamil Dubaniowski:** Czy wiecie i ja też sobie zadałem pytanie, to projektując to była moja decyzja, może gdzieś tam nie konsultowana, ale uznałem, że jak już robimy po nowemu, to to w jakim stopniu jest czytelniejsza, ale ma swoje wady i zalety. Znowu wcześniej trzeba było wejść do tej tabeli, czyli nie było tego rozwinięcia, tutaj po prostu miałeś pole, tabela i koniec. Jak chciałeś wejść do tabeli to trzeba było się przełączyć kontekstowo tam w tym górnym menu i wejść do tej tabeli albo tu gdzieś był przycisk, żeby przejść do środka do tabeli i tam by była osobna tabelka wtedy z listą pól w tej tabeli. Ja zrobiłem, że pokazujemy wszystko na jednej, ma to swoje zalety.

**Janusz Bossak:** No.

**Damian Kaminski:** No.

**Kamil Dubaniowski:** Ale ma też swoje wady, bo się komplikuje tak czytelność może się zmniejsza, nie wiem. Ale z drugiej strony widzisz wszystko na raz, widzisz czy masz wszędzie nazwy domyślne poustawiane, czy masz wszędzie tam podpowiedzi czy tłumaczenia? Widzisz to wszystko na jednym ekranie. Znowu tak to więc to też ma swój plus, ale minus, że przy dużych formularzach staje się może nie czytelne.

**Janusz Bossak:** Ja mam taką propozycję, mam taką propozycję, bo wiecie co jest mylące ten szewron tabeli.

**Kamil Dubaniowski:** Komplikuje. Mhm.

**Janusz Bossak:** Bo on wygląda jak tej sekcji. Gdyby go tu nie było w tym miejscu, tylko tu byłoby to ikona tabeli.

**Kamil Dubaniowski:** Sekcji. Mhm.

**Janusz Bossak:** A ten szewron przenieść za nazwę, czyli tabela produktów szewron. Tak to by oznaczało, że to jest takie pole. Bardziej robimy to złożone tak i jakieś elementy i wtedy ten plus.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Po lewej stronie, który pokazujesz bardziej, by sugerował, że to jest takie zachowanie jak normalne, że dodaję coś nowego do pola.

**Kamil Dubaniowski:** OK. Dobra.

**Janusz Bossak:** A dopiero na tym poziomie sekcji w tabeli. Mamy coś innego i nawet bym tą sekcję w tabeli. Ja wiem, że trochę zajmuje miejsca, ale ją wciął. Czyli.

**Kamil Dubaniowski:** Wiesz co, wydaje mi się, że ona u nas jest tylko to firma czasami się stawia. Tabelka tu jeszcze są plusy jest wcięta troszeczkę, czyli tabela, żona nie ma znowu ikony i teksty się wyrównały, sekcje nie mają nikłą.

**Janusz Bossak:** No, no, no, ale okej, dobra, to jakoś tak.

**Kamil Dubaniowski:** Tymi szablonami już widać, że to wcięcie jest.

**Janusz Bossak:** Wydaje mi się, że te plusy są teraz fajne. Znaczy plusy te do dodawania tych pól.

**Kamil Dubaniowski:** Dodawania.

**Janusz Bossak:** Bo to bardzo bym powiedział upraszcza, nie wiem czy on nie jest za duży problem. W ogóle ten plus taki.

**Kamil Dubaniowski:** Tak mimo to wiadomo, te ikony są dużo mniejsze, też te po prawej. Dobra, znaczy OK. Koncepcja jest zaakceptowana, więc zrobię. Postaram się jeszcze coś pokombinować z tym szewronem do tabeli. I kolejna zmiana, którą omawialiśmy. Narzuciłem to 2, jedną zasugerował Mateusz Kołakowski. Jakiś czas temu, i ona trochę mi się spięła z tym, że nie chcę tu, żeby było mnóstwo akcji, a zaczęły się mnożyć. Bo mamy ustawienia, czyli to co otwiera prawy panel. Mamy akcje, Mateusz o nią poprosił, żeby z tego poziomu dało się wywołać to okienko do ustawiania uprawnień, widoczności tego pola, bo to było w prawym panelu, a że tam korzystają z tego często, to nawet nie chcą czasami otwierać prawego panelu, tylko od razu wejść do tej widoczności. Historia, ona była, czyli historia edycji tego pola, i na tabeli dochodzi nam i dojdzie do wszystkich innych pól. Docelowo akcja ta reguły, która otwiera w tym wypadku po prostu edytor reguły tabeli. A w przypadku zwykłych pól docelowo tam otworzy tą listę powiązań, jakie reguły są powiązane z tym problem, więc będą już te reakcje i robi się tego za dużo, więc uważam, że trzeba zdecydować co wyciągamy na wierzch. Co dajemy do tego menu rozwijanego? Na razie na wierzch wyciągnąłem tą akcję podstawową, te powiedzmy mniej używane, bo.

**Janusz Bossak:** Podstawowa jest potrzebna w ogóle, to domyśl.

**Kamil Dubaniowski:** Wiesz co mamy edycję inne i dlatego tak jest, bo domyślnie może to też do wywalenia i tak o tym myślałem, że rezygnujemy z tej edycji innej dla nazwy systemowej. Jak chcesz edytować nazwę systemową to wchodzisz do ustawień.

**Janusz Bossak:** OK, nie to chyba edycja innym jest też istotna.

**Kamil Dubaniowski:** Bo. Dlatego to jest osobna akcja, że trzeba to ustawienia ustawienia włączyć sobie.

**Janusz Bossak:** Ale tak jest OK. Natomiast nie do końca rozumiem teraz tych 3 kropkach. Czy to oznacza, że będzie się otwierał i tak i tak prawy panel, ale tylko w odpowiedniej części?

**Kamil Dubaniowski:** Nie. Nie, to chodzi o to, bo tak, bo to widoczność to jest okienko. Aktualnie czekają już włączę, czyli on wywoła po prostu tą akcję. Tak naprawdę tamten przycisk prawy wam się nie otworzy, otworzy się tylko to okno od razu. Jak użyjesz tego z tego poziomu? Tu widoczność i otwierać się to okienko.

**Janusz Bossak:** To to już, a to jakby uspójnić, bo to jest zarządzaj uprawnieniami jest widoczność.

**Kamil Dubaniowski:** Tak, tak, tak, tak, tak.

**Janusz Bossak:** To musi być, bo tutaj wiesz, są więcej jest opcji widoczności, bo jestem pokaż na listach niedostępne w raportach polecam AMODIT.

**Kamil Dubaniowski:** Właśnie to też chciałbym podważyć troszeczkę, bo pole systemowe nie ma nic związanego z widocznością i to też chciałbym potwierdzić. To jest moim zdaniem ustawienie pola właściwość, że to pole jest systemowe.

**Damian Kaminski:** Jak to momentu? Znaczy. A co to robi? Tylko to.

**Kamil Dubaniowski:** To jest jedyna rzecz. Tak.

**Janusz Bossak:** Chyba były jeszcze jakieś kwestie związane z wyświetlaniem tego historii.

**Damian Kaminski:** Ale Lucy in.

**Kamil Dubaniowski:** Potem. Właśnie tak, ja sobie to zapisałem na listę, żeby po czterdziestce to robi. A jak robi te rzeczy? To też opisać, bo nie wiedziałbym.

**Damian Kaminski:** Właśnie.

**Janusz Bossak:** Wydaje mi się, że ono ma coś wspólnego z nie wyświetlaniem zmian w tym polu w historii sprawy.

**Damian Kaminski:** Że na pewno marzę, jest nie podpisywane.

**Janusz Bossak:** To na pewno.

**Damian Kaminski:** Po co to zostało zrobione przede wszystkim i teraz może jeszcze ma jakieś inne, bo jeśli jest nie podpisywał, to może tak powinno się nazywać, że pole nie objęte.

**Lukasz Bott:** Wow.

**Damian Kaminski:** Podpisem spraw. Czy po prostu nieobjęte mechanizmem podpisu? Bo teraz nikt go nie używał, bo nikt go nie rozumie.

**Lukasz Bott:** I tam jeszcze chyba jest szerzej. Coś też mi się wydaje, że jest coś z modułem raportowym, że się nie wyświetlają.

**Damian Kaminski:** I tutaj po najechaniu mógłby być tooltip. Tak naprawdę to to znaczy wtedy nie trzeba instrukcji, aktualizacji i tak dalej. Najeżdżamy widzimy nawet niekoniecznie tooltip, wyświetlany jeśli by było to więcej mogło być jakaś ikonka i wyświetlenie takiego modala.

**Kamil Dubaniowski:** Tak, tak o to chodzi, żebyśmy my też mieli jakby za 2 lata jest to spisane. Spodziewam się, że to 2 lata.

**Damian Kaminski:** Dokładnie. W sensie, że wtedy mamy to tu i wtedy działa tak jak jest opisane i w sensie nikt nie musi szukać. A jak to się nazywa w instrukcji? Co to znaczy wiki mam na myśli, tylko tutaj dokumentujemy aplikację w ramach aplikacji.

**Kamil Dubaniowski:** Ale OK, wracając tutaj. Wydaje mi się, że tamtą akcje po prostu trzeba dobrze nazwać, żeby już wiedział co robi, to się używa raz na jakiś czas też będą kolumny, więc będzie można sobie zweryfikować jakie są ustawienia w ramach kolumb na liście po prostu, a chodzi o wywołanie tej akcji. Tak Mateusz przynajmniej zaadresował potrzebę, że on nie chce otwierać prawego panelu, działa w kontekście uprawnień, on chce od razu wyświetlić sobie te. To.

**Damian Kaminski:** Dobra tylko.

**Kamil Dubaniowski:** Ma to są jakiś sens?

**Damian Kaminski:** To, a czemu tak działa? A po co matryca?

**Kamil Dubaniowski:** Jeszcze może nie ma tej matrycy też nie chcę im narzucać tak jak padło, że nie.

**Damian Kaminski:** Właśnie więc pytanie, czy wiesz, czy to jest słuszne, że idziemy tutaj w dodatkowe opcje, skoro mamy matrycę i wtedy zarządzasz z tym naprawdę zbiorczo i szybko?

**Kamil Dubaniowski:** To możemy podważyć, tak jak powiedziałem, ja gdzieś tam w pierwszej kolejności też samo napisałem, że używają matrycy, nie musi tego być, natomiast i tak będą już 3 akcje, bo.

**Damian Kaminski:** Tak samo historia. Czy to jest tu potrzebne?

**Janusz Bossak:** Chcieli to AmRest chciał i to to jest akurat według mnie bardzo sensowne.

**Damian Kaminski:** Ale w sensie, a kliknij tą historię to co się wydarza?

**Kamil Dubaniowski:** Nie albo jakiegoś ktoś tu.

**Damian Kaminski:** W sensie czemu uważasz, że sensowne? A co jeśli by było to w prawym panelu dopiero?

**Janusz Bossak:** Też może być, ale historia jest czy może być dość długa historia pokazuje, to okienko, którym widać zmiany było to jest to nie wiem czy tutaj w tym nowym w ogóle panelu teraz to mamy gdziekolwiek, ale przynajmniej w starym tak było o tu jest tak, a tu jest tylko takie, a tu jest prosimy o właśnie zmienioną.

**Damian Kaminski:** Ale wiecie, to jest tak naprawdę informacje techniczne pola.

**Janusz Bossak:** Tak, ale czemu nie chciałbyś jej mieć?

**Damian Kaminski:** Że w sensie, że mają być tutaj dostępne już na liście, tak nie po otwarciu prawego panelu i tam w informacjach technicznych pod, tylko tutaj po prostu tak.

**Janusz Bossak:** Tak, tak, tak.

**Damian Kaminski:** To jest coś, czego na tyle często się korzysta, że to musi być tup dostępne w łatwy sposób.

**Janusz Bossak:** Tak.

**Damian Kaminski:** Tak stwierdzam.

**Kamil Dubaniowski:** Czy twoje pan kojarzy gdzieś tam? Chyba dopytywała w kontekście listy reguł o to i nie pamiętam. Wydaje mi się, że zostało to na wierzchu, bo tak tam Danieli, Mateusz. Zabrali feedback, to Damian ty chyba podałeś.

**Damian Kaminski:** Nie, ja to schowałam.

**Janusz Bossak:** Tam obok.

**Kamil Dubaniowski:** Schowana masz?

**Janusz Bossak:** Mam uwagę też oczywiście co do tych plusików nawet był to widzę, że co do kopert to jakaś styl tak tu Filip ma styl tych plusików.

**Damian Kaminski:** Tak.

**Janusz Bossak:** Yy.

**Kamil Dubaniowski:** Wyniki są wszędzie, to jest info to z tabeli Ant Design, ja zgłosiłem, żeby to zmienią nasze wrony, ale znowu tutaj pewnie trzeba zgłosić. Niezależnie tak, każda tabela po prostu to raczej nie jest globalną ustawienie dla wszystkich tabel.

**Janusz Bossak:** Właśnie.

**Kamil Dubaniowski:** Chociaż zobaczymy dopytasz.

**Janusz Bossak:** Po prostu znaczy, to nie byłoby złe, gdyby nie to, że teraz właśnie to tą rozmowę prowadzimy, czy prowadziliśmy w pewnym zakresie odnośnie tych plusików do dodawania czegoś poniżej powyżej. Więc plusik sugeruje, że coś chcesz dodać, a nie rozwinąć.

**Kamil Dubaniowski:** Tak, tutaj też to wszystko jest to.

**Janusz Bossak:** Zresztą według mnie to jest też niefajnie. Ja wiem, że tak mamy wielu sekcjach tu powinny być szablony, Dodaj niech sugeruję dodawanie czegoś, a.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Szewron niech sugeruje rozwijanie i trzymajmy się.

**Kamil Dubaniowski:** Tak zrobimy, trzeba będzie też zmienić na formularzu wtedy sprawy tej normalnej sprawy, bo tam też są plusy.

**Janusz Bossak:** Jest to samo ma chyba ten.

**Kamil Dubaniowski:** Ale uważam, że warto.

**Janusz Bossak:** Mateusz Kisiel, jak tam wejdziesz to plota też. Ikony mi nie odpowiadają jakby mentalnie temu co tam jest, to minus plus. I znowuż tam jest plus i już jako dodawanie. Minusy służy jako zwijanie. Nie wiem jak jakoś coś nie bardzo tanie, ale dobra, trzeba to uspójnić.

**Kamil Dubaniowski:** Dobra, czyli tak OK. Teraz mówiąc chcemy mieć pod ręką tą historię, ona będzie też prawym panelu do włączenia tą widoczność dyskusyjnie, natomiast głównie chciałem doprecyzować, że to wam pasuje tak, czyli te reguły.

**Damian Kaminski:** Poczekaj, poczekaj, poczekaj. Żeby to już było spójne, to znaczy ja jeszcze mój projekt nie jest realizowany, więc ja mogę spóźnić do ciebie, ale się wycofuję, bo ja wtedy był plan, że to będzie, że ta historia będzie z lewej strony jako taka kolumna, co powodowało powiększenie wierszy wysokościowo i tedy z tego stwierdziliśmy, że rezygnujemy, ale potem zmieniłem to w kontekście listy reguł, że to ma być wierszu, tak jak u ciebie. Więc może to ma sens i wtedy ta historia. Żeby jednak była.

**Kamil Dubaniowski:** Czyli ja po prostu chcę, żeby wszystkie akcje, które są możliwe na danym elemencie, były te, które będą po prostu w prawym panelu, żeby dało się też wywołać z tego na niej tyle, żeby nie było potrzeby otwieranie tego prawego panelu. Bo ja chcę od razu wejść do historii. To po co tam ładować w ten prawy panel tam szukać. A jak już mamy ten prawy panel, to jest też spójne z naszym podejściem do prawego panelu na sprawie, to te same akcje mam tak naprawdę też tu tak, czyli powiedzmy, że to jest pole Odnośnik na formularzu, a to jest prawy panel tego pola. Mamy też sama akcję powtórzono jak to?

**Damian Kaminski:** To usuń pole, to też jest dobrze ukryte. Ja bym się nie domyślił.

**Kamil Dubaniowski:** I to ja zmieniłem tak, ono było gdzieś tu na dole, wtedy to dobra to pytanie, tylko chcę to potwierdzić, że ta akcja otwierając reguły z tego miejsca jest OK, bo to de facto było tematem.

**Janusz Bossak:** Według mnie jest OK.

**Kamil Dubaniowski:** Na razie nie musimy dyskutować o tym.

**Janusz Bossak:** Cokolwiek, cokolwiek, ona.

**Damian Kaminski:** Tak. Tylko to przeniesie do jednego, może ewentualnie filtrować.

**Kamil Dubaniowski:** Bo powiecie? To do okna edycji tej reguły.

**Janusz Bossak:** Bo co się wydarzyło, jak nie?

**Damian Kaminski:** Nie, nie, nie, nie, nie, poczekaj do okna, dobra na razie do okna edycji, tylko za chwilę to okno edycji nie będzie tym oknem edycji.

**Janusz Bossak:** Ale do którego okna edycji?

**Kamil Dubaniowski:** Do edytora reguł tej tabeli.

**Damian Kaminski:** Właśnie.

**Janusz Bossak:** Tak, ale jeżeli?

**Damian Kaminski:** A może.

**Janusz Bossak:** Dobra, bo OK, bo to jest przy tabeli dobrze dobrze.

**Damian Kaminski:** To.

**Kamil Dubaniowski:** Tak, na razie przy tabeli obsługujemy nic więcej.

**Damian Kaminski:** Tak, tak przy tabeli tylko reguła. Tak to jest na razie jedna.

**Janusz Bossak:** To nie rozumiem, gdyby, ale gdy będzie.

**Kamil Dubaniowski:** To tekst reguła tabeli tak mogę.

**Damian Kaminski:** Tylko wiesz, rzucę wam światło co gdzieś tam zatwierdzaliśmy, że będzie w ten sposób. A może reguły od razu i na razie jedna, a potem będzie to tak.

**Kamil Dubaniowski:** Tak, tak jest cel, że te reguły tabeli też są po prostu regułami takimi, że ma już mieć kilka.

**Damian Kaminski:** Że tu trafisz. To może jednak reguły i tam będą pytania, czemu reguły, a dlatego, że zaraz nie będziemy już otwierać tej perspektywy, że masz tą regułę, tylko przeniesienie inny zostaniesz tu.

**Kamil Dubaniowski:** Nawet nie, nawet nie, bo plan jest taki, że tam w tym panelu listy co ja robię, jak klikniesz tą akcję, to my ci pokażemy oknie, pewnie zajmie ono całe większość ekranu, ale w oknie pokażemy ci listę reguł powiązanych z tym polem od razu. To będzie ta sama lista twoja, tylko już w pewien sposób przefiltrowana tak i wyświetlona w oknie.

**Damian Kaminski:** Nałożonym filtrem. Dobra, ale na razie mówimy o tabelach, tak.

**Kamil Dubaniowski:** Tak, więc one nie będą miały więcej niż jedne i więc od razu otworzy się żeby.

**Damian Kaminski:** Bo wiesz, jest kontekst tak, że reguły tabel to są reguły tabel automatyczne, a są reguły procesów, których tabele mogą być wywoływane. For each row i tak dalej. To jest też inny kontekst.

**Kamil Dubaniowski:** Na razie chcę zaopiekować tą funkcjonalność, którą zgubiliśmy, bo jak w grudniowej wersji już nie będzie starej listy to nie ma jak się dostać do edytora tej reguły tabeli.

**Damian Kaminski:** Mhm. Tak, tak.

**Kamil Dubaniowski:** I od tego bym zaczął.

**Janusz Bossak:** To może Kamil u ciebie powinny być 2 opcje? Znaczy ta druga się pojawi jak zrobimy wyświetlanie reguł powiązanych z tym polem, tak? I wtedy jedna opcja, ta, którą teraz zrobiłeś na poziomie tabeli, to powinna się nazywać reguły tabeli. Tak jak tutaj jest z reguły tabel w twoim wątku, reguły tabeli, żeby było wiadomo, że to jest to w reguły tabeli, a druga opcja, która by dotyczyła wszystkich pól.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** To są reguły powiązane z polem coś takiego i wtedy wyświetla tak jak tu Damian mówi listę reguł powiązanych z tym polem na przykład for each row, tabela gdzieś tam, że nazwa tej tabeli została użyta w jakiejś regule.

**Kamil Dubaniowski:** Mhm, mhm.

**Damian Kaminski:** To jeszcze chwilę zajmie zanim do tego dojdziemy skutecznie. Ale tak.

**Janusz Bossak:** Wtedy mnie to.

**Kamil Dubaniowski:** Tak. Wiecie jakby akcja OK. Dobra, czyli tamta akcja to są reguły tabeli. Otwiera się to okno, właściwie reguła tabeli, tak naprawdę teraz jest jedna.

**Janusz Bossak:** Ale żeby być mieć kierunek?

**Damian Kaminski:** Teraz jest jedna.

**Kamil Dubaniowski:** Reguła to byli reguła tabeli. Otwiera się to okno od razu już do edycji tej reguły oczywiście w popupie.

**Janusz Bossak:** Tak jak kiedy. Tak jak kiedyś zrobimy reguły tabeli, to zmienimy nazwę z reguła tabeli na reguły tabeli i będzie lista wtedy.

**Kamil Dubaniowski:** Albo wtedy w tym jednym oknie tak te reguły powiązane po prostu. Bo ta reguła tabeli też jest reguła powiązana, więc wtedy w tym jednym oknie po prostu pokażemy ci te stricte reguły tabeli, a jeszcze pod spodem reguły powiązane do tej tabeli.

**Janusz Bossak:** Może tak być?

**Kamil Dubaniowski:** Ale to już będziemy kombinować w ten na razie, na razie chodzi o zabezpieczenie tej opcji, żeby tego nie zgubili i mogli aktualizować do grudniowej. Wracam.

**Damian Kaminski:** Dobrze, czyli tak u ciebie będzie tylko zębatka i 3 kropki.

**Kamil Dubaniowski:** Tak. Resztą.

**Damian Kaminski:** Dobra, dojdziemy do tego na poziomie tej listy, ryj.

**Kamil Dubaniowski:** Później zobaczymy jaki będzie odbiór. Będzie można coś wyciągnąć jak uznajmy, że często używają ich chcą.

**Damian Kaminski:** I tak to jest szybkie, 3 kropki i kliknięcie to nie jest niewiadomo co.

**Kamil Dubaniowski:** Pewnie tak. Dobra teraz tak prawy panel to jest kolejny temat na przyszły sprint. To co potwierdziliśmy, to zgłoszę, żeby to zamknąć jeszcze w tym prawy panel. On jest wspólny dla widoku listy i dla widoku edytora graficznego. Zrobili to w chłopaki jako jeden komponent, więc jest o tyle fajnie, że jak zmieni jeden, to u drugiego też zmiana jest widoczna.

**Janusz Bossak:** Wreszcie komponentów.

**Kamil Dubaniowski:** Tak, tak, tak, chociaż zaczęli nie komponentowo i ja jakby jeszcze na wczesnym etapie gdzieś tam to powiedzmy, że udało mi się przez przypadek wyłapać, bo zgłosiłem coś u Filipa, później zobaczyłem, że nie ma u Przemka, więc jakby.

**Damian Kaminski:** Ale właśnie to jest to, że my musimy pilnować, że nie muszą rozmawiać, to jest tylko potwierdzeniem tego, co wcześniej.

**Janusz Bossak:** Znaczy wiecie, bo mamy w tej chwili można powiedzieć dwuosobowy, bo Mateusz trochę jakby jest z boku tego, ale dwuosobowy zespół frontendowców i musimy i to, co się tu wydarzyło, jest bardzo fajne. Oni muszą ze sobą uzgodnić wszystko tak, czyli żeby nie było, to jest styl Filipa, a to jest styl Przemka, nie jest stylem AMODIT-u nie i tyle. I zasady jakby tworzenia tego AMODIT-u, oni muszą pracować na wspólność, żeby tak jak tu mówiłeś o tych tabelkach. Jedna jest wyższa, w sensie wyższa ma wiersze, druga gdzieś w innym miejscu ma niższe wiersze. Nie ja bym chciał, żeby to był jakiś standard. Nie wiem jak oni to mają w sobie zapisać. Nie jestem programistą, ale to powinno być tak domyślnie. Każda tabelka ma taki takie wysokości koniec kropka i można w jakimś przypadku, kiedy to będzie uzasadnione zrobić tabelkę z wyższymi kolumnami, znaczy wiesz, ale żebyśmy mieli właśnie to jak tu powiedzieć o tym prawdę pełnego uspójnienie, uspójnienie, uspójnienie, uspójnienie, to było jeden komponent tabelki i używamy go w różnych miejscach. Obra.

**Kamil Dubaniowski:** Dobra. Jest tego dużo nawet w łapie Filipa, czasami nad tym, że on robi 2 rzeczy, a obie wyglądają nieco inaczej. Może to wynikać z kontekstu, tak, że na przykład ta matryca jest wyższa, bo tam jest jakiś dropdown i tak dalej, ale nie powinno tak to powinna być świadoma decyzja, ale OK.

**Janusz Bossak:** Może trzeba ich po prostu zebrać znowuż, tak jak mówiliśmy o Piotrze, tak niech oni usiądą godzinę pogadają, tak piszą zasady i się trzymają tego i niech się komunikują jak jeden coś robi jak komponent.

**Damian Kaminski:** Dokładnie tak popieram i to my musimy pilnować tej przestrzeni, że oni muszą się spotkać, bo oni się nie spotykają. My musimy o to dbać.

**Janusz Bossak:** Jak ktoś zaczyna robić jakich tak jak on robi komponent, to musi wiedzieć drugi, że słuchaj, ale ja już mam taką, że takie coś tak, a nie, że on tam wydłubię sobie, bo mu łatwiej. Mają uspójnić. Tak, to musimy zadbać, to słusznie. Dobra.

**Kamil Dubaniowski:** Dobra, lecimy dane podstawowe, znaczy ogólnie co się zmienia względem obecnego stanu tego prawego panelu, że będę tak na szybko porównywał. Aktualnie w nagłówku tego panelu jest nazwa typu pola, dla mnie bez sensu.

**Lukasz Bott:** Wiecie co, ja podziękuję się rozłączył bo tam Łukasz prosił o konsultację.

**Kamil Dubaniowski:** W sensie? Dobra, dzięki. Duży minus gubię w ogóle ten nagłówek i teraz w takiej sytuacji to nawet nie wiem jak tutaj coś ustawiam to z kontekstu jak gdzieś mnie ktoś zagada, wyłącza się przełączę to wrócę i nie wiem w sumie co ja edytuję, muszę pojechać do góry. Wiadomo zamrażamy ten nagłówek, ale z drugiej strony jak tu jest nazwa typu pola, że to jest tekstowe taki tekst to też mi to za dużo nie daje, więc zmiana pierwsza jaką sugeruje. Tutaj w nagłówku prezentujemy nazwę pola plus, w tym jako grafikę, czyli pokrywa się to z tym i teraz chciałbym, żeby to, co widać w tym nagłówku było uzależnione od tej opcji. Zobacz dla czyli jak ktoś ma ustawiony zobacz dla systemowe, to w nagłówku widzi nazwy systemowe, jak zmieni tego poziomu nazwy systemową, to po wyjściu z edycji nagłówek też się zaktualizuje. Jak ktoś ustawi sobie, że chce zobacz dla Polski, to w nagłówkach będzie miał te same nazwy jakby polskie. I to jest gdzieś pierwsza zmiana. Druga zmiana to jest właśnie te akcje, czyli żeby one były, żebym nie musiał teraz iść tutaj, żeby na przykład tam otworzyć te reguły tabeli albo też nie wiem, to jest do do waszej decyzji, bo ja te akcje, które gdzieś tutaj były właśnie na różnych sekcjach, przeniosłem do górnej belki, czyli te reguły tabeli mogą być tu w górnej belce, ale możemy też zdecydować, że jest sens gdzieś je umieścić. Zamiast w górnej belce na poziomie po prostu, który jest sekcji tej ustawie. I to jest kolejna rzecz w sumie do decyzji, bo co do tego raczej jestem pewien, że chcę zmienić ten nagłówek, a te akcje. Tak samo wywaliłem to to już wiem, że o tym musimy podyskutować, pewnie dłużej wywaliłem całą tą sekcję dotyczącą zarządzania polem. Bo tak usuń pole w takiej konfiguracji. Ja wrzuciłem właśnie tu jest ukryte, bo to rzadko używana akcja, tak jak sami sugerowali liście, a zmiana typu pola jest przy typie pola. Dla mnie to intuicyjne. Tak wiem, że to się robi rzadko, ale te akcje powinny być moim zdaniem jeszcze bardziej intuicyjne. Bo jak ja co 2 lata zmienia typ pola, to nie chce się zastanawiać, gdzie ja mam to zrobić? A nie przeszkadza to jakoś szczególnie jest zablokowany do edycji? Natomiast zmień typ pola jest. Mam ostrzeżenie tak jak to działa aktualnie, tylko nie jest to jakaś tam akcja wywalona do osobnej sekcji, tylko akcje jest przy.

**Damian Kaminski:** To jest to ma sens, to ta nazwa nie jest długa, więc spoko, to jest według mnie dobrze, te usuwanie jest takie ukryte trochę.

**Kamil Dubaniowski:** Elemencie, który edytuje.

**Damian Kaminski:** Mogło być też na dole, a może być i tym.

**Kamil Dubaniowski:** Tak, tak, tak było gdzieś tam w pierwszej wersji, to padło uwagę, że to się robi rzadko, niepotrzebnie zajmuje miejsce i tyle, więc wiecie raz wystarczy pokazać moim zdaniem też, chociaż pewnie i tak będą tanie.

**Janusz Bossak:** Pewnie gdzieś tutaj się powinno pojawić. To, co dyskutowaliśmy raportów czekajcie, bo chyba ktoś nas wywołuje tam.

**Damian Kaminski:** Właśnie, bo tam spotkanie nam się zaczęło z Przemkiem.

**Kamil Dubaniowski:** Dobra dobra, to dobra, ten prawy panel, tak jak powiedziałem jest na przyszły sprint potencjalnie w ogóle o ile się wyrobimy, więc ja na razie nie będę naciskał na to.

**Damian Kaminski:** Przełączamy się, bo mnie to już Przemek wywołania.

**Kamil Dubaniowski:** Tak. Przez zmianę nagłówka na razie, bo myślę, że tego jesteśmy pewni.

**Damian Kaminski:** Dobra.


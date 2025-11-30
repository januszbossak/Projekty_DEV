**Data spotkania:** 22 września 2025, 07:02

---

**Kamil Dubaniowski:** W tym sprincie, jeśli chodzi o zmiany w interfejsie, mamy zmiany dotyczące matrycy uprawnień. Pytam o gotowość – coś się dzieje na środowiskach lokalnych?

**Damian Kamiński:** Przed chwilą działało.

**Kamil Dubaniowski:** Dobra, to opowiem i zaraz pokażę pulpit jak się połączy. W tym sprincie udało się rozwinąć tą matrycę uprawnień pod kątem właściwie już ponad MVP, czyli doszedł tryb kompaktowy, który za chwilę pokażemy. Zmienił się nieco interfejs, usunęliśmy tego selecta. Wizualnie możliwe, że podobałby się bardziej, ale wydajnościowo dużo to zmieniło, więc teraz ta matryca ładuje się o wiele szybciej bez tego selecta. W tym momencie po prostu widać tylko ikonki. Po najechaniu na ikonę już mam pulpit, mogę pokazać. Jest to mniej więcej oscylowanie tak, żeby to wyglądało jak select, lista wyboru. I w sumie nawet nie chcieliśmy odzwierciedlać pełnego selecta, bo i tak by się dało, ale uznaliśmy, że na tyle jak mamy teraz jest już to wystarczające, czyli nie mamy tutaj po prostu tej listy. Nie widać jest to w takiej formie, bardziej wygląda jak najlepiej. Da się tutaj działać i edytować. I tak jak wspomniałem, dzięki temu, że nie ładujemy tych selektorów, to działa to po prostu szybciej. Doszła już nowa nawigacja tak jak będzie docelowo. Tutaj jeszcze jakieś niuanse typu zmiana ikony, żeby to była jakaś tarcza, która bardziej kojarzy się z uprawnieniami niż z matrycą, bo to bardziej chodzi o uprawnienia, ale to już szczegóły. Natomiast chodzi o to, że już można się szybko przełączać między mediatorem, między docelową listą. Na razie jeszcze starą listą, która ładuje się najdłużej, bo to jest taka stara technologia. A tą naszą matrycą uprawnień doszły filtry w tym sprincie, czyli możemy już sobie, przy dużych procesach, gdzie mamy wiele etapów, ograniczyć tylko do tych, które aktualnie konfigurujemy z uwzględnieniem tego, że nie da się wyłączyć, musi być minimum jeden. Ten tryb kompaktowy, o którym wspomniałem, to była sugestia Przemka, żeby obrócić te napisy, żeby jeszcze węższe te kolumny były. Natomiast mieliśmy 2 próby – tą, gdzie zawijamy tekst po prostu i tam, gdzie obracamy. Mogę to też pokazać, bo mamy na zrzutach z Filipem, że ta odwrócona wersja stawała się troszeczkę już nieczytelna. To jest do dyskusji, bo zmiana nie jest jakoś trudna do wykonania. Natomiast robiliśmy oba podejścia i to wydaje się czytelniejsze. I tu podobnie jak w poprzednim plus dochodzi uprawnienie domyślne. Filip, czy masz może gdzieś lokalnie, żeby chociaż pokazać szkic jak to wygląda?

**Filip Liwiński:** Tak i to w miarę działa, to już są poprawki co do logiki dziedziczenia. To mogę pokazać tą kolumnę, właśnie domyślne uprawnienie.

**Kamil Dubaniowski:** Dobra, to ja oddaję pulpit, opowiem o co chodziło. Względem tego interfejsu starego, tabelarycznego, gdzie uprawnienie edytowało się per pole, zgubiliśmy uprawnienie domyślne dla pola, czyli na wszystkich etapach po prostu.

**Damian Kamiński:** Czyli na wszystkich etapach po prostu, tak.

**Kamil Dubaniowski:** Tak, tak, że jeśli na wszystkich etapach dla pola miała być edycja, no to w poprzedniej wersji dało się to zrobić w jednym jednym kliknięciem, więc doszło uprawnienie po prostu domyślne na tej matrycy. I wszystkie pola, które na etapach nie mają ustawionych wyjątków, po prostu dziedziczą to uprawnienie domyślne. Natomiast na matrycy pokazujemy takie, jakie realnie ono jest. Nie że tutaj gdzie się stan napis domyślne, tylko jeśli domyślne jest ukryte, a pole nie ma wyjątków na etapach, no to na wszystkich etapach ustawia się to domyślne. Jeśli jest jakiś wyjątek na etapie, to symbolizujemy tu tą gwiazdką obok nazwy uprawnienia, czyli tam, gdzie widzicie ukryte, wymagane z gwiazdką, to znaczy, że tutaj tych uprawnień nie zmienimy zmieniając uprawnienie domyślne, bo tutaj już ktoś ustawił wyjątki dla tych etapów.

**Piotr Buczkowski:** Mało widoczne.

**Kamil Dubaniowski:** No, ciężko coś tutaj jeszcze dorzucić. Natomiast tooltip też będzie po najechaniu, że jest to wyjątek dla etapu dwukropek odczyt. A jeśli jest to domyślne, to będzie domyślne dwukropek edycja. Czy te tooltips już masz Filip czy jeszcze?

**Filip Liwiński:** Jeszcze nie robiłem, bo to właśnie tam dałem ci dopiero teraz.

**Kamil Dubaniowski:** Wiecie, to ma być tylko na odczyt, żeby było wiadomo jakie uprawnienia jest. Jak ktoś chce wchodzić w szczegóły, no to tu tutaj wyjaśni fotografia.

**Przemysław Sołdacki:** Jedno pytanko. Tutaj ten taki blank te szare po prawej, to znaczy, że to jest dziedziczenie czy co to jest?

**Kamil Dubaniowski:** To jest dziedziczenie z nadrzędnej sekcji albo z tabeli, czyli jeszcze w drugą stronę. Matryca teraz patrzy od góry, czyli jeśli...

**Przemysław Sołdacki:** Znaczy ja mam taką sugestię, bo tak naprawdę idealnie jest, jak jest jak najmniej wyjątków, czyli jeśli jest dziedziczone, to powinno być prawie wszędzie dziedziczone, tylko żeby dało się łatwo zobaczyć, że ktoś w danym miejscu zrobił wyjątek. Więc może jakoś to odwrócić, że w momencie, kiedy jest dziedziczone to jakby nic nie ma, a w momencie kiedy ktoś zmienił i jest wyjątek w tym polu, to żeby to były łatwo widoczne. Bo teraz, jak chciałbym zobaczyć, gdzie jest zmienione uprawnienie per pole, to muszę szukać pól, w których nie ma tej ikonki. Więc ja bym to jakoś odwrócił może?

**Piotr Buczkowski:** Właśnie. Według mnie to to jest bardzo dobry pomysł.

**Łukasz Bott:** I jeszcze może...

**Kamil Dubaniowski:** OK, czyli jakieś zerwany łańcuch tam, w sensie tam gdzie?

**Łukasz Bott:** Rozerwany łańcuch i może na pomarańczowo albo czerwono, więc tak żeby się wyróżnił ewidentnie.

**Przemysław Sołdacki:** Ale wiecie, ja dokładnie też myślałem, żeby zrobić w ten sposób, że jeśli jest na przykład tłem, to wtedy widać, że tu coś zostało zmienione, tak, że to są uprawnienia zmienione w tym miejscu.

**Piotr Buczkowski:** Bo najczęstsza sytuacja jest chyba taka, że ustawiamy jakieś uprawnienia ogólne, a później wyjątki etap po szczególnych pól czy sekcji.

**Kamil Dubaniowski:** No tak, tak to jest dobra praktyka, ale ja widziałem takie rzeźby, że...

**Piotr Buczkowski:** Tak.

**Łukasz Bott:** No ale to...

**Damian Kamiński:** Znaczy wiecie, jak tych wyjątków trochę będzie, tak jak tu widzimy tych gwiazdek trochę jest, no to będzie taka szachownica.

**Kamil Dubaniowski:** Zrobicie ten czy nie?

**Piotr Buczkowski:** Według mnie powinny być tylko, nie powinno być rozróżnienia na dziedziczami tabeli czy sekcji. Dla tych domyślnych.

**Kamil Dubaniowski:** Ale to musi tak być, bo chodzi o to, że domyślnym ustawieniem może być dziedziczenie z sekcji.

**Przemysław Sołdacki:** Znaczy, nie wiem, dla mnie to jest trochę jakby. Wiecie, ja może nie wdrażam, to wdrożenie chce, żebyście wypowiedzieli. Wiecie, bo tutaj to czerwone gwiazdki, to nie wiem, może da się to jakoś inaczej wiecie, bo jakby cały mechanizm spoko, to tylko kwestia, żeby to wizualnie nie wiem, może można popróbować jakby jak zaznaczać, bo musiałbym się mocno skupić, żeby zrozumieć, dlaczego jest. Nie wiem, czasami jest gwiazdka, czasami jest gwiazdka i ten łańcuch, jakby co te rzeczy oznaczają. Jakby co te rzeczy oznaczają, bo jak jest, no bo mam w jednym miejscu 3 ikony – ikona, ta znaczy, na przykład jest, czy to jest to, czy to, czy jakieś tam inne, później mam gwiazdki i jeszcze łańcuszek, to jakby trochę za dużo tego. Może odwrotnie zrobić, że ta ikona coś oznacza, że nie wiem jakie uprawnienie jest, a jeśli to jest na przykład dziedziczone, no to mam ikonkę dziedziczenia. A jakie jest realne uprawnienie na przykład mam, nie wiem, jako tło. Albo wiecie, no eksperymentowałbym z tym, bo jak są w jednym polu są 3 ikony, to wydaje mi się to już trudne w czytaniu.

**Damian Kamiński:** Znaczy, według mnie nie będzie chyba 3, bo jeśli albo jest gwiazdka, albo jest łańcuch.

**Kamil Dubaniowski:** Nie, może być 3, no może być tak, że domyślnie ustawić, że ustawieniem pola jest odczyt, a w jakiejś sekcji, znaczy w jakim na jakimś etapie zmienisz czy ten odczyt na dziedziczenie, że ma dziedziczyć z sekcji?

**Damian Kamiński:** Może być, może dziedziczyć i być wyjątkiem.

**Kamil Dubaniowski:** I wtedy masz 3 ikony, bo domyślna ikona to jest odczyt. Ktoś ustawił, że wyjątkiem dla etapu jest dziedziczenie z sekcji.

**Przemysław Sołdacki:** Wydaje mi się to jest skomplikowane w odczycie, bo znaczy może te 2 ikony da się połączyć w jedną? Nie wiem.

**Kamil Dubaniowski:** Czy uprawnienia nie są. Uprawnienia nie są łatwe.

**Damian Kamiński:** Znaczy według mnie te podejścia różne są, nie oceniam żadnego, każde mają swoją logikę czy filozofię, ale to co powiedział Przemek też jest kluczowe. Może zapytajmy wdrożeń? Skoro my to już mamy, pokażmy im to i zapytajmy też o ich zdanie, bo może ktoś jeszcze wpadnie na jakiś fajniejszy pomysł. Może właśnie warto by było z nimi to skonsultować.

**Przemysław Sołdacki:** Znaczy wiecie, właśnie warto ich spytać, później ja bym zrobił tak, żeby kilka wariantów, tak wiecie, nie działających, tylko tak po prostu wizualnych i pokazać, który jest najlepszy. No bo rozumiem, jest to zaprogramowane, działa to super, to nie wiem, po zmienianie tam kolorów czy która ikonka, no to to będzie łatwe. Tak tylko żebyśmy już wybrali to, bo jakby teraz jak ja patrzę na to, to strasznie dużo rzeczy jest naraz i nie wiem na które rzeczy patrzeć. A może tak naprawdę co dzień potrzebuję wiedzieć, gdzie są jakieś uprawnienia i czy w danym miejscu ja coś zmieniałem, czy to wynika z dziedziczenia na przykład. Ale może jest, nie wiem, może tak jak mamy tu filtry, to może to, że ja chcę włączyć, że widzieć czy coś jest wyjątkiem czy nie jest, czy mógłbym w ogóle tego nie chce widzieć w tym momencie. Ale to wiecie.

**Kamil Dubaniowski:** Najistotniejsze i tego bym nie zmieniał, jest pierwsza ikona. Tak, dlatego nie chciałem, żeby dawać ten łańcuch jako ikonę. No bo mnie to nie interesuje, jak ja przeglądam, bo do tego służy ta matryca. Chcę się upewnić, że skonfigurowałem tak jak klient wymaga i że na tym etapie to pole będzie ukryte albo do odczytu, i to jest dla mnie najważniejsze, to czy ja to ustawiłem. Bo mogę to samo zrobić na 3 sposoby – ja mogę to dziedziczyć, mogę nie dziedziczyć, mogę ustawić wyjątki na wszystkich, jak mi się chce klikać. Ja wiem, że i widziałem, że niektórzy konsultanci wręcz tak robią – nie używają tego dziedziczenia. Nie chcę mi się zastanawiać. A przy tej matrycy to będzie jeszcze łatwiejsze i wolą sobie etap ustawić takie uprawnienia jakie ma być, bo mają na przykład też taką szachownicę dużą, że właściwie każdy pole inaczej. I wręcz czasami jest to nielogicznie zrobione, no bo właśnie dziedzicząc mieliby mniej klikania, ale oni i tak zwykli sobie to ustawiać, no bo z jakiegoś powodu jest łatwiej. Więc możemy jak najbardziej pogadać, bo wszystko co potrzeba już jest zrobione, zmienić to wizualnie. No to nie jest jakaś gotówka robota, tylko trochę brakuje pomysłów. Nie chcę też tu zrobić tęczy.

**Przemysław Sołdacki:** Jednak to koniecznie z konsultantami trzeba pogadać. Znaczy wiecie, ja bym też podszedł od tej strony, żeby się zastanowił, jakby do czego to ma służyć. No bo jedna rzecz to zobaczyć jakie w ogóle efektywne są uprawnienia, no to wtedy potrzebuję pierwszą ikonkę, reszty w ogóle nie potrzebuję. Mogę chcieć zobaczyć, czy na danym etapie po prostu jest gdzieś odziedziczone, skądkolwiek, czy tu co zmieniałem. Więc nie wiem, może jak zmieniałem, to nie wiem większa ikona, może intensywniejsza, nie mam pojęcia, no to do zastanowienia. A na przykład to czy jest dziedziczone czy przy stole domyślne, czy skądś indziej, to może dopiero jak nie wiem, tam najadę w tooltipie mi się to wyjaśnić dokładnie po prostu, żeby nie było za dużo rzeczy naraz na ekranie. Ale to bym skonsultował właśnie z wdrożeniowcami. No właśnie, no ale to jest właśnie najlepiej, jakby to była wszędzie jedna ikona, a nie tam po 3. Więc no, ten to do zastanowienia tam, ale spoko.

**Kamil Dubaniowski:** I w polskie jeszcze, jeśli tak dla dużych już faktycznie też zapomniałem o tym, bo jeszcze na tej wersji co pokazywałem nie miałem, wycinamy to co niepotrzebne. Teraz można się skupić na samej konfiguracji. Tutaj bym pewnie, Filip, jeszcze ten dół w takim wypadku, bo tam się zmieściło kilka wierszy jakąś.

**Filip Liwiński:** Tak.

**Damian Kamiński:** A w filtrach mamy filtrowanie po nazwach pól?

**Kamil Dubaniowski:** Po etapach.

**Filip Liwiński:** Tak, po etapach.

**Kamil Dubaniowski:** Po etapach tylko, tak, tak, tak startowaliśmy od tego.

**Damian Kamiński:** Po etapach, nie? No jest OK, bo te kontrolki też według mnie wchodzą. Nie może nawet sprawniej niż jakieś pole wyszukiwania.

**Przemysław Sołdacki:** A właśnie, a może byśmy dodali search, który by filtrował jakby i po sekcjach i po polach i może nawet po etapach. Wtedy by się to zmniejszało, że na przykład chciałem mieć tylko nie wiem pola, które zawierają jakiś tekst, albo że sekcja zawiera dane.

**Kamil Dubaniowski:** Wydaje mi się, że takie poty mi po tym, no musiałoby to być sterowane, no bo mamy pole weryfikował, a mamy etap weryfikacja, no i jak ktoś zacznie pisać weryfikacja, no to już mu powywalać etap niepotrzebnie w międzyczasie, bo tak będzie to trochę nieoptymalne.

**Przemysław Sołdacki:** Nie, no OK, no też wiecie, no to, ale do zostawienia, bo ten search mógłbym się przydać. Nawet może powinien działać tylko po polach, bo tych etapów to mamy powiedzmy filtr oddzielne. Ale na przykład jak chcesz sprawdzić uprawnienia w danym polu, to żebym mógł sobie search zrobić. No bo to można by jakieś automatyczne zwijanie, rozwijanie tych sekcji, ale może ten search będzie wystarczający.

**Kamil Dubaniowski:** Mhm, OK.

**Damian Kamiński:** To znaczy, ja akurat za searchem jakoś wybitnie nie jestem, bo według mnie mamy do tego narzędzia też przeglądarki, kontrole. Ale jeszcze zwróciłbym uwagę, jakie to są nazwy. To są, rozumiem, techniczne.

**Kamil Dubaniowski:** Tutaj, tak.

**Damian Kamiński:** No właśnie i tutaj może być pewien dysonans. To może było warto się jeszcze zastanowić, że patrzę na – ktoś mi zgłasza serwisowo, że nie mogę edytować tego pola i ona ma nazwę wyświetlaną. I teraz muszę szukać na innym widoku, żeby znaleźć, które to pole.

**Kamil Dubaniowski:** Możemy zrobić, Filip, tak jak w edytorze graficznym, to jest switch między wyświetleń dla domyślne polski, angielski, tam się przełączasz wtedy między wyświetlanymi.

**Przemysław Sołdacki:** To wiecie co, to ten przełącznik wyciągnijcie na ten pasek tam gdzie są zakładki, bo to ma sens zarówno dla edytora graficznego, dla listy, dla matrycy po prostu, że w tym wierszu był tutaj.

**Damian Kamiński:** Znaczy to mamy, a pokaż jak to wygląda na graficznym.

**Kamil Dubaniowski:** No jest niżej.

**Damian Kamiński:** No właśnie i on tutaj jest tutaj tak, gdzie filtrowanie, tak. Zobacz dla po prawej stronie na górze. Więc pytanie, czy chcemy robić to tak jak powiem, bo Przemek sugeruje taką zmianę globalną, że niezależnie w której zakładce, tak rozumiem, jesteś, to poruszasz się po nazwach takich jak sobie tu wybrałeś?

**Przemysław Sołdacki:** Tak, bo to dziwne byłoby, że sobie w edytorze graficznym wybieram polskie, a na przykład na liście widzę angielskie. To bez sensu, jak sobie przełączyłem, no to chcę przede wszystkim i matryce uprawnień też w tym samym co wybrałem.

**Kamil Dubaniowski:** Ta lista będzie teraz problematyczna, bo na nią nie wpłyniemy. Tam nie ma takich w ogóle funkcjonalności, więc nie chcę też z takiej technologii przerabiać.

**Przemysław Sołdacki:** Znaczy, nie ja, chwilowo to może nie działać. Trudno, ale tak to nie zostanie. Ale generalnie co do logiki, to ten wybór, jaki rodzaj nazw chcę widzieć, no to jest raczej globalny. Znaczy, czy to edytor graficzny, czy lista czy matryca, to powinno być te same rzeczy.

**Damian Kamiński:** Znaczy na pewno niewygodnie byłoby to przełączać za każdym do zmianą zakładki. Nie, to z pewnością tu się zgadzam.

**Daniel Reszka:** Czekajcie, tylko dodam.

**Przemysław Sołdacki:** Dokładnie.

**Daniel Reszka:** Tylko ja dodam, że w tym momencie jak nie znamy procesu i sobie latamy po nim, to po prostu robię CTRL F i wyszukuję nazwę i patrzę jak ona jest. A tak trzeba będzie przełączać, w sensie to już jak uważacie niezbędnie czytelność, ale to będę musiał za każdym razem przelatywać po różnych językach – czy domyślny, czy polski, czy jakiś tam główny, nie wiem jak tam są jeszcze angielski jeszcze. No bo w tym momencie mamy wszystko na formularzu naraz i jeden kontrolF znajdzie mi to pole.

**Przemysław Sołdacki:** Ale też tylko w danym języku, który sobie ustawisz.

**Daniel Reszka:** Nie, nie, nie, przecież teraz masz wyświetlane wszystkie.

**Damian Kamiński:** Nie, bo tam wyświetlamy wszystko.

**Kamil Dubaniowski:** Teraz na liście widać to i to.

**Daniel Reszka:** No i kontrolF mi znajduje wszystko bez żadnego klikania. Tylko mówię, że po prostu dojdzie klikanie jak będziemy szukali czegoś w dużych procesach.

**Kamil Dubaniowski:** Tego może tę search, wtedy szukał po wszystkim tak jak.

**Daniel Reszka:** Bo trzeba będzie. No coś takiego bardziej by było użyteczne myślę.

**Kamil Dubaniowski:** Bo wyświetlać tutaj też tak jak w starym widoku, no nie ma miejsca na to. Też zmniejszymy czytelność, a to jest tylko pod wyszukiwanie potrzebne.

**Przemysław Sołdacki:** No to wiecie, no to może ten search będzie potrzebny po prostu, który będzie szukał po wszystkim?

**Daniel Reszka:** Bo często przylatujemy z formularza głównego, w sensie ze sprawy i szukam pola sobie kwota. No i chcę zobaczyć tę kwotę. No ja nie wiem, czy ona domyślnie ma kwotę, czy w polskim, czy ogólnie.

**Kamil Dubaniowski:** Czyli tak będzie przełączanie w kontekście pisania reguł czy cokolwiek. Tak czyli zostaniesz wyświetleń kontrolF. Znaczy ten nasz search i wyszuka po takiej nazwie dowolnej, nieważne czy dostępna techniczną czy nie. No ale ty będziesz musiał teraz to na przykład odwołać się do reguł. No to będziesz musiał zmienić na systemowy z tych wyświetlanych, jak pracujesz na codzienne wyświetlanych.

**Piotr Buczkowski:** W starych ustawieniach systemowych. Nie wiem jak w nowych to wyszukiwanie działa i po nazwie wewnętrzne i po nazwie wyświetlanej, no to tam jest jedna nazwa wyświetlana.

**Przemysław Sołdacki:** No ale wiecie, to trzeba zrobić moim zdaniem jako search docelowo.

**Damian Kamiński:** Trzeba się na tym na pewno pochylić i przemyśleć i zaproponować jakieś rozwiązanie. Ja tylko zwrócę uwagę, że jak będziecie robić tutaj te wyświetlane i techniczne, to tu pamiętajcie też o poziomie ich, o poziomym wierszu. Nie, że etapy też mają ten kontekst.

**Kamil Dubaniowski:** Inne.

**Damian Kamiński:** Nie tylko pola.

**Kamil Dubaniowski:** Wydaje mi się, że powinniśmy pójść pewnie tak najprościej jak się da. I taką propozycję też była, jak ktoś ma na przykład ustawione wyświetla i dla Polski, no to ta pierwsza nazwa to jest faktycznie wyświetlana, a przy tej konfiguracji w nawiasie obok pokazujemy nazwę techniczną. I to tak samo trzeba by zrobić w edytorze. Natomiast jak ktoś pracuje na systemowych, no to wiadomo ma tylko systemowe, bez niczego w nawiasie.

**Damian Kamiński:** No ewentualnie jest jeszcze opcja jak w ustawieniach systemowych, kiedy starych, bo nie wiem, nie pamiętam jak jest w nowych, że po najechaniu w tooltip mógłby się wyświetlać się nazwa techniczna, jeśli jesteśmy wyświetlanych.

**Kamil Dubaniowski:** Znaczy tutaj ja sam przyznam, że często kopiuję tak, no bo potrzebuję do kodu, więc mówi się jednak to tekstem. Wykonal, więc mamy wiemy co jeszcze.

**Damian Kamiński:** Mhm.

**Daniel Reszka:** No bo też poczekajcie teraz jak było to przełączanie, widzę teraz ten checkbox. Jak sobie zmienię nazwę na nie wiem na wyświetlaną, to ja skąd będę wiedzieć, że to jest pierwszy w sekcji test?

**Damian Kamiński:** No właśnie trzeba to usprawnić.

**Daniel Reszka:** No bo to logiczne nie ma sensu, jak jest 100 pól na formularzu i patrzeć, który ci się zmienił nazwę. Jako jednak techniczne są potrzebne do reguł na wyświetlanie, żeby zobaczyć co jest też na formularzu. Chyba że właśnie na formularzu będziemy teraz mieli tę historię wyświetlaną, to co też jest w planach, to usprawni, że tylko po technicznej będziemy się poruszać.

**Damian Kamiński:** Mhm, a jeszcze Kamil nie pokazywałeś tych checkboxów?

**Daniel Reszka:** Bo może też w tą stronę.

**Kamil Dubaniowski:** Tak, wydaje mi się, że to już było. Natomiast to jest ta zmiana masowa uprawnień, czyli zaznaczamy sobie edytujemy, no i tutaj też dojdzie zmiana tego domyślnego ustawienia.

**Damian Kamiński:** Po lewej.

**Kamil Dubaniowski:** Nie mamy, czyli żeby globalnie też zmienić te ustawienia domyślne do tych pól.

**Piotr Buczkowski:** W poprzedniej wersji było sprawdzane, czy te pola mają różne uprawnienia. Jeżeli tak, to było ostrzeżenie.

**Kamil Dubaniowski:** Tak. Teraz teraz nie robimy tego, ponieważ wtedy on chciał z jakiegoś powodu usilnie zrównać wszystkie uprawnienia. Teraz pozwalamy ci wejść do tej edycji. No jak będziesz chciał dla etapu start zmienić to uprawnienie, to zmienimy, ale tylko dla tego etapu. Dla pozostałych zostają takie jakie były.

**Damian Kamiński:** Bo tam jeszcze raz jakbyś mógł pokazać, bo tam jest właśnie taka domyślna pozycja, tak że. No nie, nie ma. Jest wybierz, tak, a nie ma pozostaw bez zmian.

**Piotr Buczkowski:** Nie, a nie powinno się wyświetlić aktualne tutaj.

**Kamil Dubaniowski:** Nie możemy, no bo właśnie to było w starej wersji i przez to, jak chciałeś zmienić na jednym etapie masowo uprawnienie, to nie mogłeś, no bo wywalało ci, że tutaj są różne uprawnienia dla tych pól i w ogóle ci nie otwiera do tego edytora, albo musiałeś zresetować uprawnienia.

**Piotr Buczkowski:** No tak.

**Damian Kamiński:** OK, ale to nie powinniśmy tego sobie nazwać, bo rozumiem, że taki będzie efekt, że start powinien się nazywać w tutaj w liście rozwijanej pozostaw bez zmian, jak zmienisz tylko na inny etap, to tylko tam się zmieni. Tak, a tu pozostanie bez zmian.

**Piotr Buczkowski:** No także.

**Kamil Dubaniowski:** Tak tego. Czyli zamiast tego wybierz uprawnienie miało być.

**Piotr Buczkowski:** No bo to powinno być tak, że albo powiedzmy jeżeli są dla wszystkich pól takie same dla tego etap uprawnienia, to po prostu na przykład edycja odczyt. A jeżeli są różne, to jakaś taka sekcja, jakiś taki napis różne uprawnienia, tak.

**Damian Kamiński:** Tylko że.

**Przemysław Sołdacki:** Ale wiecie co, ja bym tak nie robił, bo jakby jakie są uprawnienia to widać w tej matrycy. Tutaj ja rzeczywiście bym zrobił też ten napis, który jest, że tutaj wybierz uprawnienie. To był napis taki nie zmienia i tak.

**Damian Kamiński:** Nie zmieniam, no bo de facto co jest pod przyciskiem zapisz tak, żeby ten kto zmienia, no wiedział, że tu się nic nie stanie na etapie start dla tych pól, a nie że się zresetuje coś.

**Daniel Reszka:** Też jestem za tym, bardziej intuicyjne, tak jak Damian mówi, że nie zmienia i pozostaw bez zmian i wtedy.

**Damian Kamiński:** No bo jak dzisiaj wybierzesz coś weź wybierz na starcie i potem jednak też stwierdzisz, że nic nie chcesz zrobić, to już nie możesz wrócić.

**Filip Liwiński:** Masz rację tak.

**Damian Kamiński:** Możesz tylko anulować jeszcze raz, więc może powinna być to dodatkowa po prostu pozycja listy rozwijanej.

**Kamil Dubaniowski:** Ewentualnie zamiast znaczy też widziałem gdzieś, tak mieliśmy, że X się pojawia obok, czyli żeby wyczyścić.

**Damian Kamiński:** Może być też. No, ale wtedy ten placeholder dobrze by było, żeby mówił, że tu się faktycznie nic nie wydarzy.

**Kamil Dubaniowski:** No dobra, to żebyśmy też nie zabrali całego spotkania. Jakby jeszcze będą kolejne iteracje. To dopiero idzie do wrześniowej, do czerwcowej nie wkładamy, no bo już za późno to zaczęliśmy, więc jeszcze jest chwila.

**Łukasz Bott:** To Kamil, co tutaj jest? Skoro to już właśnie Daniel się pojawia jako przedstawiciel, powiedzmy wdrożeniowy, serwisowy, czyli tych ludzi, którzy najczęściej będą z tego korzystali. To może faktycznie jakiś dedykowany spotkanie umówić i to jeszcze raz zaprezentować, opowiedzieć może w szerszym gronie, może na piątkowym, może na piątkowym.

**Daniel Reszka:** Dokładnie, bo ja tylko od strony serwisowej, a wdrożeniowcy bardziej mogą jeszcze coś innego używać.

**Łukasz Bott:** To słuchajcie, to może na piątkowym spotkaniu o piętnastej. Nie mówię, że w najbliższej, ale to chyba będzie dobry moment, bo wtedy wszyscy jesteśmy. Kontynuujmy, tak, no bo to faktycznie zeszło nam trochę czasu.

**Kamil Dubaniowski:** Tak, dobra. OK Filip tam, podoba chyba za dużo się jakieś niuanse, raczej takie korekty. To tam raczej nie ma, nie ma co się na tym skupiać, zadaniach w ustawieniach systemowych. Przemek, czy ty byś chciał coś o formularzu edytorze graficznym? Jeszcze tam też raczej były korekty niż jakieś nowości. Plus ten temat strony wylotu wydania i nie pamiętam co jeszcze.

**Przemysław Rogaś:** No tak, z mojej strony to raczej byłem usprawniania tylko, nie kojarzę takich zmian.

**Przemysław Sołdacki:** Czyli kiedy my w ogóle dajemy ten edytor nowy?

**Damian Kamiński:** Czerwcowej wersji, w tej, która teraz wyjdzie, którą kończymy stabilizując czerwcowej.

**Przemysław Sołdacki:** W której? W której? OK właśnie, kiedy ona wyjdzie?

**Damian Kamiński:** No chcemy niezwłocznie. Jeszcze kilka poprawek było realizowanych w końcówce zeszłego tygodnia, dokumentację. No jesteśmy w trakcie, żebym powiedział, że raczej dochodzimy gdzieś tam już do końca, więc czy to się wydarzy w tym tygodniu? Jakie były konkluzje tutaj Daniel z Januszem? Chyba w czwartek piątek.

**Daniel Reszka:** Takie rzeczy tydzień będziemy umawiać. Czy zgadzacie, że to już jest gotowa wersja, czy nie? Że jak mówicie, że możemy próbować, to możemy próbować. Na razie jak mówisz, że jeszcze coś wydajecie, no to ja bym poczekał w sensie.

**Damian Kamiński:** Tak, to znaczy, w piątek wydaliśmy jeszcze w trybie hotfixowym kilka poprawek zwłaszcza chce też do raportów. No trzeba to po prostu teraz protestować, popracować nad tymi. Jeśli nie będzie uwag, no to będziemy zalecać podnoszenie tej wersji.

**Michał Zwierzchowski:** Wszystkie zmiany jakieś piątki były, są teraz na?

**Damian Kamiński:** No tu zbieramy feedback już wdrożeniowy. Z tego korzystają Mateusz tam zgłaszał kilka uwag też do tego, żeby to co wydajemy, nawet te nowości były stabilne, na tyle, że zawsze da się wrócić do wersji poprzedniej. Nie wiem, czy tam już te ustawienia systemowe też mają ten przycisk Kamil, wejścia do wersji starej, bo tego chyba jeszcze nie było.

**Kamil Dubaniowski:** Tak, to już jest na Astrofox. Jedynie co była różnica, to nazwy – integracje systemowe, integracje definiowane, tam został jeszcze integracja AMODIT i rozszerzenia AMODIT, ale tak, przełączki już jest. Checkbox i tak jak ma to działać, to działa, tylko tam wizualnie się zmieni tekst.

**Damian Kamiński:** No można powiedzieć, że dopieszczamy, tak eliminujemy ostatnie błędy. Czy to się w tym tygodniu wydarzy? No ja bym powiedział, że nie wykluczajmy, ale dajmy sobie jeszcze chwilę na testy.

**Przemysław Sołdacki:** Chodzi mi o to, żebyśmy mogli ogłosić, że jest nowa wersja.

**Damian Kamiński:** Mhm. Wiemy, że tak jest cel.

**Przemysław Sołdacki:** No dobra, to będę czekał na oficjalną informację. Bardzo, co dalej mamy jeszcze?

**Damian Kamiński:** Łukasz, czy ty opowiesz o tych zmianach filtrami, czy to już prezentowałeś?

**Łukasz Bott:** Nie prezentowałem, ale to mogę pokazać, bo akurat to mam na podorędziu. Właśnie to stoczyłem. To znaczy tak, oczywiście to w kontekście tutaj też nowego podejścia do prezentacji tych raportów systemowych. Generalnie zmieniamy troszeczkę podejście dotychczasowe. Przez to duża ilość tych raportów, najróżniejszych jeszcze zrobionych w starej technologii, było tego dużo, ale niekoniecznie, wbrew pozorom były czytelne, więc wybraliśmy, podjęliśmy decyzję, żeby troszkę to zmienić. Przede wszystkim korzystamy z dashboardów takie przyjąłem założenie dashboard zagadkowych dla poszczególnych tam grup tych raportów systemowych. I to jest pierwszy podejście. Jako tego rzeczy, przy okazji propos błędów, to nie wiem, po odświeżeniu mi się po odświeżeniu tego raportu zdublował mi się kolumny, więc jeżeli ktoś gdzieś tam, i to jest ta wersja, no ale to jest najnowsza, którą ten, więc zwróćcie na to uwagę. Nie zawsze się to dzieje i to jest pierwsza rzecz, czyli podejście zakładkowe. Druga rzecz to jest taka, że skonfigurowane zostały przynajmniej część źródeł danych dla tych właśnie raportów systemowych, które zostały to zdefiniowane w trybie właśnie local, czyli takie one już w sobie zapytaniu mają jakieś agregaty. I to, co jest istotne, to żeby to było wydajniejsze, to te agregaty są przeliczane raz dziennie tam. No to akurat środowisku deweloperskim to tam jakieś dobrałem godziny takie powiedzmy sobie dowolne, ale to pewnie docelowo ustalimy, żeby to się gdzieś tam wydarzyło. Miało miejsce te przeliczenia gdzieś tam raz na dobę, ale gdzieś tam w godzinach powiedzmy, nocnych, statystycznie rzecz biorąc, no to raczej mamy wdrożeniu u nas w Polsce, tak, no to nikt tam po nocy jakoś się specjalnie pewnie nie pracuje. To jest.

**Damian Kamiński:** Myślę, że to dla Daniela istotna uwaga, tak, że po prostu te dane będą spływać raz dziennie.

**Łukasz Bott:** Tak, tak.

**Daniel Reszka:** Ale to z monitora czy to jest jeszcze jakieś inne narzędzie?

**Damian Kamiński:** Nie.

**Łukasz Bott:** Generalnie do raportów systemowych zostaną przedefiniowane źródła danych zewnętrznych i one będą przełączone w tryb właśnie local i raz na dobę będą przeliczane.

**Daniel Reszka:** Czyli to niezależnie od monitora, od modułu. Tak to każdy klient będzie to miał.

**Łukasz Bott:** Tak, tak, tak, tak. I tak docelowo dojdą te nowe źródła. Jest jeszcze jedna rzecz tam, być może niektóre źródła zostaną w trybie online. Ale wtedy w tych raportach i to jest właśnie to, o czym Damian dał zajawkę, wywołując mnie, mianowicie tutaj to tak Przemek to chyba Przemek robił. Zrobiliśmy coś takiego, ponieważ źródła danych mimo wszystko mogę zwracać bardzo duże ilości danych, to ze względów wydajnościowych i też na czytelność to wprowadziliśmy coś takiego, że można ustawić domyślną wartość filtru. Czyli w tym przypadku dla tego raportu to jest na dacie poprzednie 7 dni, czyli pokazuje statystyki, czyli wchodząc na raport już widzę przefiltrowany raport na poprzednie 7 dni. Przy czym mogę to sobie zmienić. I jeżeli, a nie jeszcze jedna rzecz. Jeżeli wywalę tą wartość, ta wartość jest ustawić, tu jest wymagane i wtedy on nie wyświetli nam danych, dopóki jakieś wartości w tym filtrze nie wprowadzimy. Tak czy trochę takie, bo dotychczas gdyby tego nie było, to raport by wyświetlał to, co zwraca źródła danych, co powodowało, zwłaszcza dla tych źródeł danych dotyczących właśnie tych raportów systemowych powodowało, że często to są bardzo duże ilości danych. No i raport się zazwyczaj albo wykrzacza, albo wyświetlał jakiś taki komunikat zbyt dużo danych, więc włącz jakieś filtrowanie. I tutaj robimy właśnie tak, jakby trochę tą sytuację odwracamy. Zanim wyświetlimy raport, to on może być od razu przefiltrowany po jakiejś tam wartości. I pomnik sobie może oczywiście tą wartość zmienić, tam jest funkcjonalność, funkcjonalność oczywiście i ona pozostała, że gdzieś tam pod spodem mogę sobie już wstępnie przefiltrować to źródło danych. Tylko problem polega na tym, że jest to stały filtr w danym raporcie, no i użytkownik ma na niego wpływu. To podejście chyba jest zdecydowanie lepsze.

**Daniel Reszka:** A jak daleko wstecz Łukasz, ile tych dni będziemy przechowywać?

**Łukasz Bott:** Nie, nie to.

**Damian Kamiński:** Nie, to jest niezależne. W sensie jeszcze raz, to co powiedział Łukasz, to co dzisiaj jest w edycji raportu, ograniczyć zakres prezentowanych danych, to co ustawia konfigurator raportu, administrator raportu, to zostało po prostu przeniesione na poziom niżej, czyli użytkownik może wskazać, jak chce ograniczyć i bez tego wskazania mu się nic nie wyświetli. Nie wpływamy w ogóle tutaj na ilość danych, które przechowujemy, tylko na to, że musisz wskazać ograniczenie, które administrator ci wytyczył, czyli na przykład tutaj data albo jakiś typ operacji, mógłby to być, żeby tych danych nie było aż tyle, żeby to było bardziej czytelne interfejsu.

**Daniel Reszka:** No dobra, no ale wskaże sobie poprzednie 1000 dni, no to będzie to samo co wszystko dajmy na to i to będzie OK.

**Łukasz Bott:** No, no ale to wiesz.

**Damian Kamiński:** No ale to wtedy, no tak, tak, ale po to są też domyślne, żebyś żebyś właśnie od razu miał powiedzmy też załadowany 7, a nie klikał sobie wpisywał 1000, tak? A jak potrzebujesz zwiększyć, no to wtedy jest większy, no ale to ma wpływ na cały system, tak, jeśli nagle twój raport generuje zapytanie jakieś długie.

**Daniel Reszka:** Właśnie boję się pod chmurę o to nie.

**Łukasz Bott:** Nie, no dlatego Daniel.

**Damian Kamiński:** To znaczy my usprawniamy to co było, a nie dodajemy dodatkową funkcjonalność, a nie zmieniamy sposobu wyświetlanych danych, ilości ich.

**Daniel Reszka:** Znaczy nie, no dodajemy przecież źródła, których teraz nie mieli użytkownicy, nie.

**Łukasz Bott:** Tak, ale to jest, nie, moment. Źródła danych systemowych były.

**Damian Kamiński:** Mieli. Mieli źródła.

**Daniel Reszka:** Ale nie z tymi danymi.

**Łukasz Bott:** Moment, moment źródła danych systemowe były, tylko wszystkie były w trybie online i one faktycznie powodowały, że zwracały dużej ilości danych. W tej chwili dojdą nowe źródła danych dla tych raportów systemowych. Mowa oczywiście, można je będzie wykorzystać pewnie w każdym innym raporcie. Natomiast one już co wstępnie przewagują negowane i są przeliczane raz na dobę, czyli faktycznie tych danych tam jest, może być troszkę mniej. Ale no to jest świadomie świadome działanie pod konkretny typ czy pod grupę raportów systemowych. No bo troszkę inaczej tam dla performance monitora, trochę inaczej dla logów systemowych, a jeszcze inaczej będzie dla tych dla jakiejś tam statystyk ze spraw. Tak naprawdę to ćwiczenie, czy to ta akcja, którą tutaj robimy, ona jest też. Chcieliśmy wrócić do czegoś takiego, co tu kiedyś w prawym górnym rogu było raporty. Zawsze tam myliło i to były właśnie te raporty systemowe, takie właśnie, które właśnie wyświetlały dane, gdy właśnie się wskazało jakieś konkretne wartości filtrów. No więc ta funkcjonalność też była istotna. Tak, no i Daniel to tyle, jeżeli chodzi o te raporty. Generalnie idea taka jest, jak jest i tutaj nie wiem też troszkę do ciebie. To już wstępnie śmy rozmawiali, to nad czym pracowałem jeszcze tutaj, to w tym sensie już tam dokończę, bo muszę przetestować jeszcze. Podpisywanie idea tak zwanej AMODIT Security Checklist. Dotyczy to tak jakby posiadania glejtu na to, że w danej instancji AMODIT głównie będzie to dotyczyło tych instancji instalowanych u klientów. I w pierwszej kolejności pójdziemy do tych klientów, którzy nam dostarczają pen testy. Chodzi o to, żeby mieć glejt na to, że ponieważ mamy wytyczne, więc właśnie na Wiki, no to dotyczące tego, jak AMODIT głównie aplikacje webowe AMODIT tak zabezpieczyć. Więc tutaj będzie takie wymaganie zarówno w momencie wdrożeń, że przed oddaniem produkcyjnym będziemy musieli, żeby kierownik danego wdrożenia po naszej stronie plus kierownik wdrożenia po stronie klienta podpisali się pod taką checklistą, że takie zabezpieczenia zostały wprowadzone bądź nie zostały wprowadzone. A jeśli nie, to dlaczego? Bo na przykład, no nie mają zastosowania w danej instancji. I żeby obie strony były świadome. To jest trochę nawiązanie do jednego tutaj, z jednej z sesji plan testów od jednego z klientów, który robił 2 iteracje tych pen testów, zarzucając nam, że nie wprowadziliśmy jakieś tam zabezpieczeń. Więc po każdy jakieś tam iteracji pen testów czy najlepiej przed jeszcze przed wykonaniem testów, taki taki dokument, który będzie też, no swego rodzaju gleicht, potwierdzającym, że na tyle, na ile jesteśmy w stanie tak w dobrej wierze wdrażamy wszelkie zabezpieczenia, który jesteśmy świadomi. Oczywiście pen testy mogły coś tam, jakieś dodatkowe luki wyłapać. No takiej, taki jest ich cel. No ale żeby i to jest jeszcze jedna rzecz, żeby nie powtarzać właśnie jakieś wprowadzanie zabezpieczenie, bo już wiemy, że jesteśmy zabezpieczeni na coś takiego. Ktoś tego nie wprowadził, nie skonfigurował i potem jak bumerang wraca ta sama luka bezpieczeństwa i potem musimy poprawiać. No a w zasadzie nie poprawiać, tylko powiedzieć, ale to trzeba było zrobić tak i tak, bo to już jest dawno opisane. Tak więc taka jest idea tej listy kontrolnej bezpieczeństwa. No i trącą to co ja jakiś takich głównych rzeczy, które ja robiłem.

**Damian Kamiński:** Dobrze, Piotr, chcesz opowiedzieć o tych mailach?

**Piotr Buczkowski:** Ja jakich mailach?

**Damian Kamiński:** Mhm. O logowaniu maili.

**Piotr Buczkowski:** Ale też tydzień temu mówi.

**Damian Kamiński:** Było 2 tygodnie temu, tak?

**Piotr Buczkowski:** Fakt, 2 tygodnie temu, tak?

**Damian Kamiński:** To przepraszam, to przegapiłem. No to pytanie, czy ktoś jeszcze chciałby się czymś pochwalić.

**Łukasz Bott:** Nie, no słuchajcie, no tu trzeba chyba też pochwalić się na zespół. To do roboty wykonały, czy chodzi o te testy właśnie dotyczące stabilizacji systemu.

**Damian Kamiński:** No tak, też dużo właśnie czasu poświęciliśmy na poprawki, tak jak dzisiaj wyszło. Czy tak jest stabilizacja, których powiedzmy nie widać, tak jak tutaj dzisiaj wyszło na tej prezentacji Kamila i Filipa. Bo coś możemy wytworzyć i że tak powiem szybko pokazać, ale potem jeszcze dochodzą różnego rodzaju warunki brzegowe i one się pojawiały. Czy to właśnie w tych nowych elementach, którymi tu zajmowali się koledzy z Reacta i dorabianie rzeczy, których nie widać, czyli endpointów do nich, do tego nowego całego interfejsu Reactowego, czy to ustawień systemowych czy ustawień procesu? Czy to właśnie jeszcze elementy stabilizujące raporty? No na ten moment wydaje się, że wyczyściliśmy przynajmniej to, co było wykryte, jeśli chodzi o właśnie między innymi raporty. Natomiast dalej pozostaje element testowania i tutaj między innymi jeszcze Łukasz to robi. Jeśli chodzi o jeszcze może plany, tu warto dopowiedzieć, bo to, co prezentował Łukasz, to było takie troszkę może niekompletne w kontekście spójnym. Tam część nas było po polsku, część po angielsku. To w kontekście właśnie na kanwie raportów systemowych chcemy wprowadzić tłumaczenia dla źródeł danych. Tym może gdzieś tam się też zajmiemy, żeby to ujednolicić w najbliższym sprincie. To możesz opowiedzieć, jeśli chcesz.

**Łukasz Bott:** Dzięki, żeś to wspomniał. Może to znaczy generalnie idea jest taka, żeby to znaczy tak, to są tak jakby 2 wątki, bo pierwszy wątek to jest taki, żeby można było nadać alias w momencie konfiguracji raportu. Żeby można było nadać alias dla danego pola, w szczególności, jeżeli na jakimś polu stosujemy agregację, to żeby można w jakiś sposób opisowy podać informację, że to jest ilość czegoś tam. No bo nie zawsze nazwa pola czy tam kolumny plus w nawiasie funkcja agregująca, no to niekoniecznie na pierwszy rzut oka jest klarowna. Więc można chodzi o to, żeby dawać właśnie jakieś takie aliasy dla tych właśnie kolumn czy pól używanych w raporcie, które po prostu poprawia czytelność raportu. I to jest to jest z tego punktu śmy weź mniej, ale ponieważ stwierdziliśmy, że to jest troszeczkę dużo roboty, jeżeli chodzi o mundurach sportowy, no to, podejdziemy do tego. To strona, że jeżeli mamy raporty, które bazują na źródłach zewnętrznych, to w źródłach zewnętrznych po prostu dopiszemy właśnie takie damy możliwość aliasów dla poszczególnych kolumn. No bo źródło danych nie jesteśmy w stanie tego zrobić po stronie źródła danych. No bo mamy zwracane jakiś tam wynik zapytania SQL-owego, tam oczywiście może być użyte, to funkcjonował nazwa pola SI, tutaj jakaś kolumna z bazy danych, SI coś tam i nazwa powiedzmy wyświetlana, ale to jest wciąż stała nazwa. A my potrzebujemy chociażby wersji językowej, takie tutaj gdzieś pokazywałem. Mamy miszmasz, mam interfejs po polsku raportu, a źródła danych pochodzą mi nazwa angielski. No i fajnie było, gdyby dla źródeł zewnętrznych dać możliwość ustawienia właśnie wersji językowej, chociaż aliasu dla danej kolumny. Taka jest intencja.

**Damian Kamiński:** OK. Nie wiem, Marek, w kontekście teraz Trust Center coś jeszcze chcesz powiedzieć, czy tam tylko były kwestie stabilizacyjne.

**Marek Dziakowski:** W tym sprincie dodaliśmy możliwość logowania za pomocą OAuth przez Microsoft do panelu administracyjnego dokumentu. W zasadzie było to dodane jako takie trochę pomoc przy serwisowaniu dokumentów. Była w aktualnej konfiguracji trzeba by jakby wszystkie e-maila od naszych pracowników wpisywać gdzieś tam jako administrator w organizacji, żeby oni mogli wejść na te dokumenty. Żeby tego nie robić, to po prostu dodaliśmy mechanizm, pozwala na zalogowanie się na dany adres e-mail, jeżeli jest on podany jako e-mail serwisowy. Mogę to pokazać, jak to wygląda?

**Damian Kamiński:** Czyli w kontekście biznesowym po prostu usprawniamy działania serwisu czy też administratora danej organizacji.

**Marek Dziakowski:** Tak. Nawet nie administratora i tak nasz serwis, czy to mnie, czy to ktokolwiek, czy to przykład Daniela, jeżeli chciałby przejść do Trust Center, no musiałbym mieć ten adres e-mail podany jako administratora danej organizacji. Inaczej nie mógłby się zalogować. No ale to jest też tendencja redundancja danych, bo ten e-mail by się powielał dla każdej organizacji, więc do tego dodaliśmy możliwość logowania przez Microsoft.

**Damian Kamiński:** OK.

**Marek Dziakowski:** Tutaj jest pobierane są dane na temat adresu e-mail, jest sprawdzany czy dany e-mail jest zarejestrowany jako e-mail serwisowy. Jeżeli tak, no to ma możliwość wejścia do dokumentu i nie musi tego dodatkowo wpisywać dla każdego z klientów czy w każdej z organizacji.

**Łukasz Bott:** Marek, ale.

**Damian Kamiński:** Czyli ty tym sterujesz. To to jest na poziomie Trust Center, więc jeśli Daniel chciałby tutaj powiększać pulę swoich serwisantów, którzy mają mieć dostęp, to musi się do ciebie zgłosić.

**Marek Dziakowski:** Tak. Tak.

**Piotr Buczkowski:** Co może taki użytkownik zrobić?

**Łukasz Bott:** Ale rozumiem, że.

**Marek Dziakowski:** Może to samo co zwykły administrator, czyli wysłać powiadomienie, jeżeli pozwala na to dokument. Może z edytorem to co jakby było dotychczas możliwe do robienia. Po prostu jest takie przywrócenie funkcjonalności trochę.

**Łukasz Bott:** Ale czekaj jeszcze, jeśli tak. I jeszcze takie pytanie, rozumiem, że tutaj nasi współpracownicy, tak serwisowi. No to rozumiem, że per organizacja, czy czyli dla danej organizacji, jeżeli jestem wpisany jako administrator, właśnie ten powiedzmy z naszego serwisu, czy to, że jeżeli ja jestem wpisany do bazy w Trust Center jako administrator Astrafox, to bo mam dostęp do wszystkich organizacji?

**Marek Dziakowski:** Nie. To dla wszystkich. Tak. Tak.

**Damian Kamiński:** Ale pod warunkiem, że masz dostęp do samej sprawy, bo musisz mieć link, tak?

**Marek Dziakowski:** No tak, no tak, tak, tak. No trzeba mieć link do sprawy, tak możemy wejść, bo inaczej to się nie da.

**Łukasz Bott:** No OK.

**Damian Kamiński:** Bo to z poziomu sprawy wywołujesz dopiero wejście. Tak więc.

**Marek Dziakowski:** Dla mnie to jest też ułatwienie, no bo ja często muszę gdzieś tam zaglądać po tych dokumentach, bo coś się na przykład nie wyświetla, dlaczego zweryfikować, czy już się wyświetlam. To ja normalnie to wpisywałam, proponowałem sobie ten link, bo i tak mam dostęp do tych danych. No i teraz bym musiał wpisywać się przez bazę i wchodzić, potem się usuwać. Bez sensu. A tak to dodam po prostu swój adres e-mail do jednej tabeli już mam dostęp wszędzie.

**Łukasz Bott:** No. Okej, dobry.

**Marek Dziakowski:** No i są osoby, które mają podobnie, no że tam przy serwisie gdzieś w kilku w kilku organizacjach, no to ten e-mail trzeba było wpisać za każdym razem do tej organizacji.

**Łukasz Bott:** To znaczy tą grę, tylko taka jest. Wiesz, tak trochę w kontekście jakiegoś tam, no nie wiem, no bezpieczeństwa danych i RODO. Często to umowy dotyczą, jakieś tam najczęściej podpisuje się jakieś umowy, no więc są to dane poufne. Bardziej chodziło mi o to, że rozumiem, żeby dostać ten dostęp, no to tutaj, no nie wiem, no na przykład decyzje podejmuje również Daniel, żeby kto ma mieć do tego dostęp, żeby to niekoniecznie wszystkim na wiary.

**Marek Dziakowski:** Tak. Jeżeli ma dostęp do AMODIT, to i tak widzi.

**Łukasz Bott:** W sumie tak, no.

**Marek Dziakowski:** Inaczej nie wejdzie tam. Dokument musi wejść przez sprawę, czyli będzie widział dokument przed podpisaniem, to będzie widział co tam jest.

**Damian Kamiński:** Znaczy, słuchajcie, bo to koncepcja całości, bo to może warto zarysować historycznie. Wcześniej, czyli powiedzmy 2 miesiące temu było tak, że każdy, kto miał dostęp i użył linku, wchodził z automatu. Później wprowadziliśmy dodatkowe uwierzytelnienie, które jest teraz. Zanim wejdziemy do ekranu, trzeba się uwierzytelnić po to, żeby ograniczyć ten dostęp, żeby nie tylko posiadając link, ale jeszcze zweryfikować, czy ten, kto się loguje jest w puli użytkowników fils zaufanych. I tym steruje klient wprowadzając do swojej organizacji tych użytkowników zaufanych. Teraz to, co prezentuje Marek, to jest kolejny krok usprawnienia, żeby nie trzeba było nasz naszych wszystkich maili, czyli Marka, serwisu, wdrożeń, ewentualnie tutaj na na zdf jeśli jest taka potrzeba wprowadzać na poziomie tej organizacji, tylko żeby to była taka pula globalna sterowana przez nas.

**Łukasz Bott:** No OK dobra, chodzi mi o to, że żebyśmy pilnowali, nawet jeżeli to jesteśmy my, to żeby to był jednak ograniczony zbiór osób. Ale.

**Marek Dziakowski:** Tak, tak, no będzie kontrolowany. No jeżeli ktoś ma nie dostać, to zostanie usunięty z tabeli, już nie będzie mógł wejść. Musi być potwierdzenie. Musi być wpis, że upoważniona jest dana osoba do logowania na te dokumenty. Jeżeli nie ma tego, no to nie dojdzie, mimo że jest powiedzmy, że ma ten e-mail Astrafox, tak, czyli nie wejdzie.

**Łukasz Bott:** O to mi chodziło. Dobrze, dzięki.

**Marek Dziakowski:** No to to jest taka nowość w zasadzie z tamtego sprintu. Reszta to były jakieś poprawki.

**Damian Kamiński:** No dobra, tutaj padło to tylko nie wiem, czy to zostało. Chyba nie zostało zaprezentowane, a może warto to pokazać, bo to taka w cudzysłowie głupota, ale mnie bardzo irytowała, więc sam byłem pomysłodawcą tego zgłoszenia. Mianowicie strona wylogowania zawiera, czy po wylogowaniu zawiera obecnie przycisk logowanie. Bo do tej pory jak ktoś się wylogował, no to niestety musiał sam preparować tutaj linki poprawiać go, żeby móc z powrotem wrócić. Więc to też zostało.

**Piotr Buczkowski:** Link pod logo był przecież. Wcześniej było logo.

**Damian Kamiński:** Nie wiem, nie wszędzie może było zdefiniowane, nie wszędzie się to wyświetlało. W tym momencie jest po prostu napis logowanie i po kliknięciu wracamy na stronę główną. To logo może nawet jeśli działało, to nie było intuicyjnie. W tym momencie myślę, że jest to dużo bardziej intuicyjny.

**Piotr Buczkowski:** Nie dla wszystkich użytkowników. Myślę, że dla takich bardziej zaawansowanych, chociaż według mnie to logo się nie wyświetlało, musiałbym teraz.

**Barbara Michałek:** Też mi się tak wydaje, że nie wyświetlało się, że jego nie było gdzieś tam na tej stronie logowania wylogowania.

**Piotr Buczkowski:** Bożena tej nowej, bo na tej co ja kiedyś robiłem, to na pewno było pod samym z tego, czy wielokrotnie skorzystałem, sam to zrobiłem, bo też mnie to wkurzało.

**Damian Kamiński:** Może masz rację, no niemniej teraz jest napis, który już każdemu tą sprawni. I bez domyślania się czy na pewno logo jest takim elementem. Nie wiem Piotrze, czy ty jeszcze chcesz zabrać głos? Jeszcze mamy chwilkę, czymś jeszcze chcesz się ewentualnie podzielić albo ktokolwiek inny.

**Piotr Buczkowski:** No to akurat częściowo robiłem też tutaj właśnie takie ujednolicenie tego logowania wylogowania, zwłaszcza pomiędzy starą technologią Reactem, żeby to wspólnie było, że jak się wylogujesz w jednej, to w drugiej też od razu wyloguje. Razem z Przemkiem, drogą SIM, udało się tak zrobić, że wylogowanie w jednej zakładce wylogowuje we wszystkich, niezależnie na której stronie jesteś. I też zachowaniem właśnie tego ustawień, czy przekierować na stronę logowania czy na stronę logowania. Bo no tam zapewne zależności, że jak jest na przykład auto logowanie jakimś providerem, to nie ma sensu wylogowywać na stronie logowania, bo zostanę natychmiast zalogowany ponownie.

**Damian Kamiński:** Mhm, no właśnie. Więc to może nie zawsze widać, ale zostało tu usprawnione. I jeszcze może tutaj wspomnę. Z Mateuszem pracowaliśmy też w tym sprincie nad poprawkami do komunikatora, ale nie będę go jeszcze dzisiaj prezentował w tej wersji powiedzmy ostatecznej, bo jeszcze kilka kluczowych elementów wizualnych jest do poprawy i nie chcielibyśmy tutaj prezentować właśnie czegoś nieskończonego w tym sprincie. Myślę, że to skończymy i pokażemy już taką wersję, którą będziemy chcieli wypuścić jako właśnie taką pierwszą stabilną. Myślę, że to się wydarzy jeszcze w tym tygodniu, bo zrealizowanych jest kilkanaście zgłoszeń. Chyba kilka zostało otwartych, około 3-4. I będziemy z tym wtedy gotowi, żeby to już pokazywać. No dobrze, pytanie, czy ktoś jeszcze chciałby się czymś podzielić?

**Mariusz Piotrzkowski:** Miałem mówiącymi drogą też pokazać taką bardzo drobną ikonki grup w interfejsie sprawy z tym Kamilem ogarnialiśmy, jak to mogłoby wyglądać. I teraz jest coś takiego. Informacja o sprawie wygląda w taki sposób, kolor jest taki sam jak w zakładce do wykonania, ten sam mechanizm. W uprawnieniach taką listę to widać, że użytkownik ma czarny tekst, a grupa ma białą ikonkę. Także jest widoczne, które jest które.

**Piotr Buczkowski:** Ale dlaczego ta ikonka jest większa?

**Mariusz Piotrzkowski:** Więc może jak, może większe od tekstu?

**Piotr Buczkowski:** Od tak od tej.

**Mariusz Piotrzkowski:** Może się tak częściowo wydawać z 2 powodów. Po pierwsze ikonka jest od krawędzi do krawędzi jest praktycznie obrazem, a tekst, no to jak masz literkę P, no to P jest ucięte. Poza tym ikonka może rzeczywiście nieco wyższa dlatego, że jest bardziej kwadratowa.

**Piotr Buczkowski:** Nie wiem, jest większą jakieś 2 piksele?

**Mariusz Piotrzkowski:** To tak testowaliśmy.

**Damian Kamiński:** No dobra, to sprawdźcie to po prostu. Natomiast bo tu powiedziałeś, że brany jest kolor, ale tutaj te grupy mają różne kolory, więc coś mi tu nie pasuje.

**Mariusz Piotrzkowski:** Tak, to są te same kolory co w zakładce do wykonania, tam też są różne kolory.

**Damian Kamiński:** Aha, OK. No dobrze, i skończy, to znaczy tak, bo tutaj to ma też wpływ na komunikator. My tam też pracujemy nad tą reprezentacją group dla czatów grupowych. Dobrze by było, żeby to było spójne. To jak już skończycie to i to przejdzie wszystkie testy, to dajcie mi znać.

**Mariusz Piotrzkowski:** Te kolory. No bo. OK. To więcej ciekawych rzeczy takich interesownych nie mam.

**Łukasz Bott:** A może dodajmy możliwość wskazania ikonki per grupa, tak jak mamy możliwość wskazania ikony proces.

**Damian Kamiński:** No dobrze.

**Łukasz Bott:** Tak, rzuciłem wolno pomysł.

**Anna Skupińska:** Od no i testujący pomysł.

**Damian Kamiński:** Znaczy, myślę, że nie jest najbardziej krytyczne w tym momencie. Natomiast jest to jakaś opcja, może nawet niekoniecznie ikonki, co z samej kolorystyki, ale to no pewnie jest jakiś kierunek rozwoju. Ale myślę, że na ten moment to niekoniecznie jest coś, czym musimy się, znaczy musimy się skupiać, chociaż może w tą stronę ostatecznie pójdziemy.

**Łukasz Bott:** Na pewno nie, nie, nie musimy. Rzuciłem tylko tak jak pomóc dobry, bo powoli kończymy, nie.

**Damian Kamiński:** Dobrze, mamy jeszcze 2 minuty. Nie wiem, czy ktoś jeszcze. Chyba już istotnych tematów nie ma, bo nikt tutaj się nie wyrywał, chyba, że ktoś jeszcze coś chce.

**Daniel Reszka:** Damian, a tej ikony procesy, jak to wspomnieliście, bo one domyślnie się ustawia nazwa, jakby pierwsze literki procesu, potem trzeba wybrać ikonę i nie da się przywrócić już tej pierwotnej nazwy. Ktoś analizował, skoro robicie te ikony, to może tam też już poprawić to.

**Damian Kamiński:** Ale chcemy tak wracać. Według mnie to właśnie powinna być jednostronna.

**Łukasz Bott:** Też tak uważam.

**Damian Kamiński:** Ustawienie.

**Daniel Reszka:** Ktoś przez przypadek zmieni, potem się przyzwyczaili, że mieli proces nazwany DA, teraz nie mogą tam wrócić.

**Łukasz Bott:** To nie jest zrobione, zrobię własnych ikon.

**Damian Kamiński:** Zastanów. No powinni w takim razie ustawić taką ikonkę, żeby była spójna z merytor.

**Daniel Reszka:** Nowy proces.

**Damian Kamiński:** Merytoryką, tak.

**Daniel Reszka:** No dobra, to jak uważacie, że to jest?

**Damian Kamiński:** No dobra, pomyślimy o tym. Nie, nie, nie na tym spotkaniu. Dobra, zastanówmy się nad tym na spokojnie. Dobra, to w takim razie dziękuję. Życzę miłego.

**Łukasz Bott:** Dzięki.

**Damian Kamiński:** Dnia.

**Przemysław Sołdacki:** Cześć.

**Damian Kamiński:** Cześć.

**Daniel Reszka:** Cześć.

**Marek Dziakowski:** Cześć.

**Mariusz Piotrzkowski:** Cześć.

**Łukasz Bott:** zatrzymano transkrypcję

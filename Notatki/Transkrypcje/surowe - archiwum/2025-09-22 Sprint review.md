**Transkrypcja**

22 września 2025, 07:02AM

**Lukasz Bott** rozpoczęto transkrypcję

**Kamil Dubaniowski** 0:03  
W tym sprzęcie, jeśli chodzi o zmiany w interfejsie to.  
Mamy zmiany dotyczące matrycy uprawnień, tylko pytam, gotowość coś się dzieje na środowiskach lokalnych, bo.

**Damian Kaminski** 0:18  
Przed chwilą działało.

**Kamil Dubaniowski** 0:21  
Czekajcie, wypiłem na na moment, nie może rozpiąć.  
Dobra, to słychać. Nie czy to się spina jak to oni wpięta ja opowiem i zaraz pokaże pulpit jak się połączy w tym sprincie udało się rozwinąć tą matryce uprawnień pod kątem. No właściwie już ponad MWP, czyli doszedł tryb kontaktowy, który za chwilę pokażemy. Zmienił się nieco interfejs, usunęliśmy.

**Damian Kaminski** 0:42  
Tak.

**Kamil Dubaniowski** 1:02  
Tego selecta takiego.  
Wizualnie no możliwe, żeby podobałyby się bardziej, ale.  
Wydajnościowo dużo to zmieniło, więc teraz ta matryca ładuje się o wiele szybciej bez tego selecta.  
W tym momencie po prostu widać tylko ikonki po najechaniu na ikonę już mam pulpit mogę pokazać.  
Jest to mniej więcej oscylowanie tak żeby to wyglądało jak select lista wyboru i w sumie no nawet nie chcieliśmy odzwierciedlać pełnego selecta, bo i tak by się dało, ale uznaliśmy, że na tyle jak mamy teraz jest już to wystarczające, czyli nie mamy tutaj po prostu tutaj do listy nie widać, jest to w takiej formy bardziej wygląda jak.  
Odczytasz jak najbardziej da się.  
Tutaj działać i edytować, a tak jak wspomniałem, no dzięki temu, że nie ładujemy tych selektorów to działa to po prostu szybciej.  
Doszła już nowa nawigacja tak jak będzie docelowo tutaj jeszcze jakieś niuanse typu zmiana ikony, żeby to była jakaś tarcza, która bardziej kojarzy się z uprawnieniami niż z matrycą, bo to bardziej chodzi o uprawnienia, ale to już szczegóły. Natomiast chodzi o to, że już można się szybko przełączać między mediatorem między docelową listą na razie jeszcze starą listą, która naładuje się najdłużej. No bo to jest taka technologia wejść na imię.  
A tą naszą matrycą uprawnień doszły filtry w tym sprincie, czyli możemy już sobie, jakby przy dużych procesach, gdzie mamy wiele etapów ograniczyć tylko do tych, które aktualnie konfigurujemy.  
Uwzględnieniem tego, że no nie da się wyłączyć, musi być minimum jeden.  
Ten tryb kompaktowy, o którym wspomniałem, to była sugestia przemka, żeby obrócić.  
Te napisy, żeby jeszcze węższe te kolumny były natomiast robi.  
Mieliśmy 2 próby i tą, gdzie zawijamy tekst po prostu i tam, gdzie obracamy dawało nam znaczy mogę to też pokazać, bo mamy na zrzutach z filipem, że że ta odwrócona wersja stała je się troszeczkę już nieczytelna, to to jest do dyskusji. No bo zmiana nie jest jakoś tam.  
Trudna do wykonania, natomiast tak jak wspomniałem, robiliśmy oba podejścia i to wydaje się czytelniejsze.  
No i tu podobnie jak w poprzednim plus dochodzą tu **** co do co do uprawną coś, co zostało zgłoszone w przez konsultantów i podjęliśmy jeszcze w zeszłym sprincie, ale tu Filip chyba jeszcze tego nie skończył, to jest.  
Uprawnienie domyślne.  
Filip, czy masz może gdzieś lokalnie, żeby chociaż pokazać szkic jak to wygląda?

**Filip Liwiński** 3:55  
Tak i to w miarę działa, to już są poprawki co do logiki dziedziczenia to mogę pokazać to kolumny właśnie domieszek problem.

**Kamil Dubaniowski** 4:01  
Dobra, to to. To ja oddaję pulpit, opowiem o co chodziło względem tego interfejsu starego tabela rocznego, gdzie uprawnienie edytowała się per pole. Zgubiliśmy uprawnienie domyślne dla pola, czyli.

**Damian Kaminski** 4:14  
Czyli na wszystkich etapach po prostu tak.

**Kamil Dubaniowski** 4:15  
Tak tak, że jakby jeśli na wszystkich etapach dla pola 2 miała być edycja, no to w poprzedniej wersji dało się to zrobić i w jednym jednym kliknięciem, więc doszło uprawnienie po prostu domyślne.  
Na tej matrycy i wszystkie pola, które na etapach nie mają ustawionych wyjątków, po prostu dziedziczą to uprawnienie domyślne, natomiast na matrycy pokazujemy takie, jakie realnie ono jest. Nie że tutaj. Gdzie się stan napis domyślne? Tylko jeśli domyślne jest ukryte, a pole nie ma wyjątków na etapach, no to na wszystkich etapach ustawia się to domyślne. Jeśli jest jakiś wyjątek na etapie, to symbolizuje my tu tą gwiazdką, obok nazwy uprawnienia, czyli tam, gdzie ślijcie ukryte wymagane z gwiazdką, to znaczy, że tutaj tych uprawnień nie napiszemy zmieniając uprawnienie domyślne, bo tutaj już ktoś.  
Ustawił wyjątki dla tych etapów.

**Piotr Buczkowski** 5:06  
Mało widocznie.

**Kamil Dubaniowski** 5:08  
No no ciężko coś tutaj jeszcze dorzucić, natomiast tulsie też będzie po najechaniu, że jest to wyjątek dla etapu dwukropek odczyt, a jeśli jest to domyślne to będzie domyślne dwukropek edycja czy te Tulipany już masz? Filip czy jeszcze takim dobra? No no więc wiecie to to ma być tylko na na odczyt, żeby było wiadomo jakie uprawnienia nie jest, jak ktoś chce wchodzić w szczegóły. No to tu typ mu wyjaśnić fotografia.

**Filip Liwiński** 5:22  
Jeszcze nie robiłem, bo to właśnie tam dałem ci dodania.

**Przemysław Sołdacki** 5:33  
Jedno pytanko tutaj ten taki blink te szare po prawej to znaczy, że to jest, że to jest dziedziczenie czy co to jest?

**Kamil Dubaniowski** 5:41  
To jest dziedziczenie z nadrzędnej sekcji albo z tabeli, czyli jeszcze w drugą stronę, tak jakby matryca. Teraz patrzysz od góry, czyli jeśli.

**Przemysław Sołdacki** 5:51  
Znaczy znaczy, ja mam taką sugestię, bo tak naprawdę idealnie jest. Jakie są jak najmniej wyjątków, czyli jeśli jest dziedziczone, to powinno być prawie wszędzie dziedziczone, tylko żeby dało się łatwo zobaczyć, że ktoś w danym miejscu zrobił wyjątek, więc może jakoś to odwrócić, że w momencie, kiedy jest dziedziczone to jakby nic nie ma, a w momencie kiedy ktoś zmienił i jest wyjątek w tym polu, to żeby to były łatwo widoczne, bo teraz, jak chciałbym zobaczyć, gdzie jest zmienione uprawnienie per pole, to muszę szukać pól.

**Piotr Buczkowski** 6:07  
Właśnie.

**Przemysław Sołdacki** 6:21  
W których jest, w których nie ma tego tej ikonki, więc ja bym to jakoś odwrócił może?

**Piotr Buczkowski** 6:27  
Według mnie to to jest bardzo dobry pomysł.

**Lukasz Bott** 6:30  
I jeszcze może.

**Kamil Dubaniowski** 6:30  
O k czyli jakieś zerwany łańcuch tak tam w sensie tam gdzie?

**Lukasz Bott** 6:33  
Rozerwany łańcuch i mąż może na pomarańczowo albo czerwono, więc tak żeby się.

**Piotr Buczkowski** 6:34  
No jak ty.

**Lukasz Bott** 6:38  
Wyróżnił ewidentnie.

**Przemysław Sołdacki** 6:38  
Ale wiecie ja.

**Piotr Buczkowski** 6:39  
Albo albo zrobić jakieś takie bardziej.

**Przemysław Sołdacki** 6:42  
Dokładnie też myślałem, żeby zrobić w ten sposób, że jeśli jest.  
Na przykład tłem to wtedy widać, że tu coś zostało zmienione, tak, że to są uprawnienia zmienione w tym miejscu.

**Piotr Buczkowski** 6:54  
Bo najczęstsza sytuacja jest chyba taka, że ustawiamy jakieś uprawnienia ogólne, a później wyjątki etap po szczególnych pól czy sekcji.

**Kamil Dubaniowski** 7:04  
No tak, tak to jest dobra praktyka, ale ja widziałem takie rzeźby, że.

**Piotr Buczkowski** 7:08  
Tak.

**Lukasz Bott** 7:08  
No ale to.

**Damian Kaminski** 7:08  
Znaczy wiecie, jak tych wyjątków trochę będzie tak jak tu widzimy tych gwiazdek trochę jest. No to będzie taka taka szachownica.

**Kamil Dubaniowski** 7:12  
Zrobicie ten czy nie?

**Damian Kaminski** 7:16  
Więc no.

**Piotr Buczkowski** 7:16  
Według mnie powinny być tylko nie po nie powinno być rozróżnienie rozróżnienia na dziedzicami.  
Tabeli czy sekcji?  
Zostawię.

**Kamil Dubaniowski** 7:30  
Ale to musi tak być, no bo.

**Piotr Buczkowski** 7:30  
Dla tych domyślnych.

**Kamil Dubaniowski** 7:32  
No bo chodzi o to, że domyślnym ustawieniem może być dziedziczenie z sekcji.

**Przemysław Sołdacki** 7:40  
Znaczy, nie wiem, dla mnie to jest trochę jakby. No wiecie, ja może nie wdrażam to wdrożenie chce, żebyście wypowiedzieli, ale ale wiecie, bo tutaj to czerwone gwiazdki to nie wiem, może da się to jakoś inaczej wiecie, bo jakby cały mechanizm spoko to tylko kwestia, żeby to wizualnie nie wiem, może można popróbować jakby jak zaznaczać, bo bo tu.

**Damian Kaminski** 7:46  
No.  
No właśnie.

**Przemysław Sołdacki** 8:02  
Musiałbym się mocno skupić, żeby zrozumieć, dlaczego jest. Nie wiem. Czasami jest gwiazdka, czasami jest gwiazdka i ten łańcuch, jakby co te rzeczy oznaczają, bo bo jak jest? No bo mam w jednym miejscu 3 ikony ikona ta znaczy na przykład jest, czy to jest to, czy tu, czy czy jakieś tam inne, później mam gwiazdki i jeszcze maciuszek to jakby trochę za dużo tego.  
Moje, bo może odwrotnie zrobić, że ta ikona coś oznacza, że nie wiem jakie uprawnienie jest, a jeśli to jest na przykład dziedziczone, no to mam ikonkę dziedziczenia. A jakie jest realne uprawnienie? Na przykład mam, nie wiem jako tło, albo wiecie, no eksperymentował bym to, bo jak są w jednym polu są 3 ikony, to wydaje mi się to już trudne w czytaniu.

**Damian Kaminski** 8:48  
Znaczy, według mnie nie będzie chyba 3, bo jeśli albo jest gwiazdka, albo jest łańcuch.

**Kamil Dubaniowski** 8:53  
Nie, nie może być 3, no może być tak, że tak może domyślnie ustawić, że ustawieniem pola jest odczyt, a w jakimś w jakiejś sekcji znaczy no w jakimś w jakim na jakimś etapie zmienisz? Czy ten odczyt na dziedziczenie, że ma dziedziczyć z sekcji?

**Damian Kaminski** 8:55  
Może być może dziedziczyć i być wyjątkiem.

**Kamil Dubaniowski** 9:11  
I wtedy masz 3 ikony, bo domyślna ikona to jest odczyt. Ktoś ustawił, że wyjątkiem dla etapu jest tak jak z sekcji.

**Przemysław Sołdacki** 9:21  
Wydaje mi się to jest skomplikowane w odczycie, bo znaczy może te 2 ikony da się połączyć w jedną? Nie wiem.

**Damian Kaminski** 9:22  
Mm nie.

**Kamil Dubaniowski** 9:26  
Czy uprawnienia nie są uprawnienia? Nie są łatwe.

**Damian Kaminski** 9:29  
Znaczy według mnie te podejścia różne są, nie oceniam żadnego, każdy mają swoje jakąś logikę czy filozofię, ale to co powiedział Przemek też jest kluczowe. Może zapytajmy wdrożeń?  
Skoro my to już mamy, pokażmy im to i zapytajmy też o ich zdanie, bo może ktoś jeszcze wpadnie na jakiś fajniejszy pomysł? Może właśnie warto by było z nimi to skonsultować.

**Przemysław Sołdacki** 9:52  
Znaczy wiecie, właśnie warto ich spytać później ja bym zrobił tak, żeby kilka wariantów tak wiecie, nie działających tylko tak po prostu wizualnych i pokazać, który jest najlepszy. No bo bo i tak rozumiem jest to zaprogramowane, działa to super, to nie wiem po zmienianie tam kolorów czy czy która ikonka no to to będzie łatwe tak tylko żebyśmy już wybrali to, bo jakby teraz jak ja patrzę na to to strasznie dużo rzeczy jest naraz i i nie wiem na które rzeczy patrzeć tak, a może tak naprawdę na co dzień to jako potrzebuję wiedzieć gdzie są jakieś uprawnienia.  
I i czy w danym miejscu ja coś zmieniałem czy od czy to wynika z dziedziczenia na przykład ale a może jest, nie wiem kill nie wiem tak jak mamy tu filtry, to może to, że ja chcę włączyć, że widzieć czy coś jest wyjątkiem czy nie jest czy czy mógłby w ogóle tego nie chce widzieć na tym momencie.  
Ale to wiecie.

**Kamil Dubaniowski** 10:42  
Najistotniejsze i tego bym nie zmieniał. Jest no pierwsza ikona. Tak, no to tutaj dlatego nie chciałem, żeby dawać ten łańcuch jako ikonę, że to jest dzielić. No bo mnie to nie interesuje jak ja przeglądam, bo do tego służy ta matryca. Chcę się upewnić, że skonfigurowałem tak jak klient wymaga i że na tym etapie to pole będzie ukryte albo do odczytu, i to jest dla mnie najważniejsze, to czy ja to ustawiłem, bo mogę to samo zrobić na 3 sposoby, ja mogę to dziedziczyć, mogę nie dziedziczyć, mogę ustawić wyjątki na wszystkich jak mi się chce klikać. Ja wiem, że i widziałem, że niektórzy konsultanci wręcz tak robią, no nie używają tego dziedziczenia.

**Przemysław Sołdacki** 10:48  
Tak.

**Kamil Dubaniowski** 11:17  
Nie, nie chce mi się zastanawiać, a przy tej matrycy to będzie jeszcze łatwiejsze i wolą sobie etap ustawić takie uprawnienia jakie ma być no bo mają na przykład też taką szachownicę dużą, że właściwie każdy pole inaczej.  
I wręcz czasami jest to nielogicznie zrobione, no bo właśnie dziedzicząc mieliby mniej klikania, ale oni i tak tam zwykli kują sobie sobie to ustawienia, no bo takim jakiegoś powodu jest łatwiej, więc może możemy jak najbardziej pogadać, bo tak jak powiedzieliście, no wszystko co potrzeba już jest zrobione zmienić to wizualnie. No to tak nie jest jakaś.  
Gotówka robota tylko no trochę brakuje, no to już.  
Pomysłów nie chcę też tu zrobić tęczy.

**Przemysław Sołdacki** 11:53  
Jednak tak to koniecznie z konsultantami trzeba pogadać. Znaczy wiecie ja bym też podszedł od tej strony, żeby się zastanowił jakby do czego to ma służyć tak no bo jedna rzecz to co mówi, że zobaczyć jakie w ogóle efektywny zespół pragnienia, no to wtedy potrzebuję pierwszą ikonkę reszty w ogóle nie potrzebuje. Mogę chcieć zobaczyć, czy czy na danym etapie po prostu jest gdzieś odziedziczone, skądkolwiek, czy czy tu co zmieniałem, więc nie wiem może jak zmieniałem to nie wiem. Większa ikona może intensywniejsza, nie mam pojęcia, no to do zastanowienia i a na przykład to czy jest nie wiem to dziedziczone.  
Czy przy stole domyślne, czy skądś indziej to może dopiero jak nie wiem tam najadę w tibie mi się to wyjaśnić dokładnie po prostu, żeby nie było za dużo rzeczy naraz na ekranie, ale to bym skonsultował właśnie z z.  
No już wdrożenie psami.  
Poproszę jeszcze ten widok ten kompaktowy.  
No właśnie, no ale to jest właśnie najlepiej, jakby to była wszędzie jedna ikona nie, a nie tam po po 3.  
Więc no ten to do zastanowienia tam, ale spoko.

**Kamil Dubaniowski** 13:00  
No i w polskie im jeszcze tak dla dużych już faktycznie też zapomniałem o tym, bo jeszcze na tej wersji co pokazywałem nie miałem, wycinamy to co niepotrzebne. Teraz można się skupić na samej konfiguracji. Tutaj bym pewnie Filip jeszcze ten dół w takim wypadku, bo tam ciebie zmieściło kilka wierszy jakością.

**Filip Liwiński** 13:13  
Tak.

**Damian Kaminski** 13:18  
A filtrach mamy Filtrowanie po nazwach pól.

**Kamil Dubaniowski** 13:20  
Poetach.

**Filip Liwiński** 13:21  
Tak kota pach.

**Kamil Dubaniowski** 13:21  
Po etapach tylko tak tak, tak startowaliśmy od tego.

**Damian Kaminski** 13:22  
A poeta?  
Nie no jest o k bo to kontrole w tutaj też według mnie wchodzi nie może nawet sprawnie niż jakieś pole wyszukiwania.

**Przemysław Sołdacki** 13:37  
A właśnie, a może byś byśmy dodali serca?  
Który by filtrowa ał jakby i po sekcjach i po polach i może nawet po etapach.  
Wtedy by się to zmniejszało, że na przykład chciałem mieć tylko nie wiem pola, które nie wiem, no zawierają jakiś tekst, albo że sekcja zawiera dane.

**Kamil Dubaniowski** 13:57  
Czy wydaje mi się, że takie poty mi po tym? No musiałoby to być sterowane, no bo mamy pole weryfikował, a mamy etap weryfikacja no i jak ktoś zacznie pisać weryfikacja, no to już mu powywalać etapie nie potrzebnie w międzyczasie, bo tak będzie to trochę nieoptymalne.

**Przemysław Sołdacki** 14:11  
Nie no no o k no też wiecie, no to ale do zostawienia, bo ten serw mógłbym się przydać, nawet może powinien działać tylko po po polach, bo do kolumbi tych etapów to mamy powiedzmy filtr oddzielne.  
Ale na przykład jak chcesz sprawdzić uprawnienia w danym polu, to żebym mógł sobie serca zrobić, no bo to jest można by jakieś ta automatyczne zwijanie, rozwijanie tych sekcji, ale może ten serw będzie wystarczający.

**Kamil Dubaniowski** 14:29  
Mhm.  
Ok.

**Damian Kaminski** 14:40  
To znaczy, ja to akurat za sercem jakoś wybitnie nie Jestem, bo według mnie mamy do tego narzędzia też przeglądarka przeglądarki, ogólnie właśnie kontrole ale.  
Jeszcze zwróciłbym uwagę, a jakie to są nazwy to są rozumiem techniczne.

**Kamil Dubaniowski** 14:57  
Mm tutaj, tak.

**Damian Kaminski** 15:00  
No właśnie i tutaj może być pewien dysonans. To może było warto się jeszcze zastanowić, że patrzę na ktoś mi ktoś mi zgłasza serwisowo, że nie mogę edytować z tego pola i ona ma nazwę wyświetlaną nie i teraz muszę szukać na innym widoku, żeby znaleźć, które to pole.

**Kamil Dubaniowski** 15:06  
Na tym zarobić.  
Możemy zrobić Filip tak jak w edytorze graficznym, to jest suit między wyświetleń dla domyślne polski, angielski tam się przełączasz wtedy między wizytami.

**Przemysław Sołdacki** 15:26  
To wiecie co to ten przełącznik wyciągnijcie na ten pasek tam gdzie są zakładki bo to ma sens zarówno, ale tera graficznego dla listy dla matrycy po prostu, że my w tym wierszu był tutaj.

**Damian Kaminski** 15:36  
Znaczy to mamy, a pokaż jak to wygląda na graficznym.

**Kamil Dubaniowski** 15:39  
No jest niżej.

**Damian Kaminski** 15:42  
No właśnie i on tutaj jest tutaj tak gdzie Filtrowanie tak zobacz dla po prawej stronie na Górze.  
Więc pytanie, czy chcemy robić to?

**Przemysław Sołdacki** 15:52  
No ale to to.

**Damian Kaminski** 15:52  
Tak jak powiem, bo Przemek sugeruje taką zmianę globalną, że niezależnie w której zakładce tak rozumiem, jesteś to poruszasz się po nazwach.

**Przemysław Sołdacki** 15:59  
Tak, bo opony.

**Damian Kaminski** 16:00  
Takich jak sobie tu wybrałeś?

**Przemysław Sołdacki** 16:01  
No no bo to dziwne byłoby, że sobie w edytorze graficznym wersję polskie, a na przykład na liście widzę angielskie to bez sensu jak sobie przełączyłem, no to chcę przede wszystkim i matryce uprawnieni też w tym samym co wybrałem.

**Kamil Dubaniowski** 16:15  
Czy tak ta lista będzie teraz problematyczna? No bo na nią nie wpłyniemy tam nie ma takich w ogóle funkcjonalności, więc nie chcę też z takiej technologii przerabiać.

**Przemysław Sołdacki** 16:24  
Znaczy nie ja chwilowo to może nie działać trudno, ale tak to nie zostanie, ale ale generalnie co do logiki, to ten wybór, jaki rodzaj nazw chce widzieć. No to jest raczej globalny, znaczy, czy to edytor graficzny, czy lista czy matryca to to powinno być te same rzeczy.

**Kamil Dubaniowski** 16:26  
Ze stępniem.

**Damian Kaminski** 16:41  
Znaczy na pewno niewygodnie byłoby to przełączać za każdy do zmianą zakładki. Nie to to z pewnością tu się zgadzam.

**Daniel Reszka** 16:41  
Czekajcie tylko dodam.

**Przemysław Sołdacki** 16:46  
Dokładnie.

**Daniel Reszka** 16:48  
Tylko ja dodam, że w tym momencie jak nie znamy procesu i sobie latamy po nim, to po prostu robię kontrolę i wyszukuje nazwę i patrzę jak ona jest, a tak trzeba będzie przełączać sensie to już jak uważacie niepewnie czytelność, ale to będę musiał za każdym razem przelatywać po różnych językach tak czy domyślny, czy polski, czy czy jakiś tam główny nie wiem jak tam są jeszcze angielski jeszcze tak.  
No bo w tym momencie mamy wszystko na formularzu naraz nie i jeden kontrol f znajdzie mi to pole.

**Przemysław Sołdacki** 17:14  
Ale też tylko w danym języku, który sobie ustawisz.

**Daniel Reszka** 17:16  
Nie, nie, nie, nie, przecież teraz masz wyświetlany wszystkie.

**Damian Kaminski** 17:18  
Nie, bo tam wyświetlamy wszystko.

**Kamil Dubaniowski** 17:18  
Teraz na liście widać to i to.

**Daniel Reszka** 17:21  
No i kontrolę fm znajduje wszystko bez żadnego klikania, tylko mówię, że po prostu dojdzie klikanie jak będziemy szukali czegoś dużych procesach.

**Kamil Dubaniowski** 17:28  
Tego może tę sekcję, aby wtedy szukał po wszystkim tak jak.

**Daniel Reszka** 17:29  
Bo trzeba będzie.  
No coś takiego bardziej by było użyteczne myślę.

**Kamil Dubaniowski** 17:36  
Bo wyświetlać tutaj też tak jak w starym widoku, no to no nie ma miejsca. Na to też zmniejszymy czytelność, a to jest tylko pod wyszukiwanie potrzebne.

**Przemysław Sołdacki** 17:42  
No to wiecie, no to może ten ser czy będzie potrzebny po prostu.  
Który będzie szukał po wszystkim?

**Daniel Reszka** 17:49  
Bo często przylatujemy z formularza głównego w sensie ze sprawy tak i szukam pola sobie kwota. No i chcę zobaczyć tę kwotę. No ja nie wiem, czy ona domyślnie ma kwotę, czy w polskim, czy czy ogólnie tak aktywności.

**Kamil Dubaniowski** 18:00  
Czyli tak będzie przełączanie w kontekście pisania reguł czy cokolwiek? N tak czyli zostaniesz wygłoszenie kontro.  
Znaczy ten nasz serwis i wyszuka po takim po takiej nazwie dowolnej, nieważne czy dostaniesz techniczną czy nie, no ale ty będziesz musiał teraz to na przykład odwołać się do reguł. No to będziesz musiał zmienić na systemowy.  
Z tych wyświetlanych jak pracujesz na codzienne wyświetlanych.

**Piotr Buczkowski** 18:23  
Starych ustawieniach systemowych. Nie wiem jak w nowych to wyszukiwanie działa i po nazwie wewnętrzne i po nazwie wyświetlanej no to tam jest jedna nazwa ździsia plana.

**Przemysław Sołdacki** 18:32  
No ale wiecie, to to trzeba zrobić moim zdaniem jako serc docelowo.

**Damian Kaminski** 18:37  
Trzeba się na tym na pewno pochylić i i przemyśleć i zaproponować jakieś rozwiązanie. Ja tylko zwrócę uwagę, że jak będziecie robić tutaj te wyświetlane i techniczne to tu pamiętajcie też o poziomie ich o poziomym wierszu. Nie, że etapy też mają ten kontekst.

**Kamil Dubaniowski** 18:42  
Inne.

**Damian Kaminski** 18:53  
Nie tylko pola.

**Kamil Dubaniowski** 18:55  
Wydaje mi się, że powinniśmy pójść pewnie tak najprościej jak się da i taką propozycję też była. Jak ktoś ma na przykład ustawione wyświetla i dla Polski, no to ta pierwsza nazwa to jest faktycznie wyświetlana, a przy tej konfiguracji w nawiasie obok pokazujemy nazwę techniczną i to tak samo trzeba by zrobić w edytorze. Natomiast jak ktoś pracuje na systemowych no to wiadomo ma tylko systemowe, bez niczego w nawiasie.

**Damian Kaminski** 19:18  
No ewentualnie jest jeszcze opcja jak w ustawieniach systemowych, kiedy starych bo nie wiem, nie pamiętam jak jest w nowych, że po najechaniu w tul tippie mógłby się wyświetlać się nazwa techniczna.  
Jeśli jesteśmy wyświetlanych.

**Kamil Dubaniowski** 19:30  
Znaczy tutaj tak, ja ja sam przyznam, że często kopiuję tak, no bo potrzebuję do kodu, więc mówi się jednak to tekstem wykonal tak to mamy mamy fintek wiemy co jeszcze.

**Damian Kaminski** 19:37  
Mhm.

**Daniel Reszka** 19:46  
No bo też poczekajcie teraz jak było to przełączanie widzę teraz ten czek. Bot jak sobie zmienię nazwę na nie wiem na wyświetlaną to ja skąd będę wiedzieć, że też jak boks będę leciał po liście i szukał, że to jest pierwszy w sekcji test.

**Damian Kaminski** 19:59  
No właśnie trzeba to usprawnić.

**Daniel Reszka** 20:00  
No bo to to też logiczne nie ma sensu jak jest 100 pól na formularzu i patrzeć, który ci się zmienił nazwę tak no jako no jednak techniczne są potrzebne do reguł na wyświetlanie, żeby zobaczyć co jest też na formularzu. Nie, chyba że właśnie na formularzu będziemy teraz mieli te tą historię o wkładaną to co też jest w planach, to no to usprawni, że tylko po technicznej będziemy się poruszać, tak.

**Damian Kaminski** 20:21  
Mhm a jeszcze kamilka nie pokazywałeś tych czek boksów?

**Daniel Reszka** 20:21  
Bo może też w tą stronę.

**Kamil Dubaniowski** 20:25  
Tak, wydaje mi się, że to już było, natomiast to jest tak ta zmiana masowa uprawnień, czyli zaznaczamy sobie edytujemy, no i tutaj też dojdzie zmiana tego domyślnego ustawienia tego jeszcze.

**Damian Kaminski** 20:25  
Po lewej.

**Kamil Dubaniowski** 20:37  
Ee, nie mamy, czyli żeby globalnie też zmienić te ustawienia domyślne do tych pól.

**Piotr Buczkowski** 20:42  
W poprzedniej wersji było sprawdzane, czy te pole mają różne uprawnienia. Jeżeli tak to było strzeżenie.

**Kamil Dubaniowski** 20:46  
Tak.  
Teraz teraz nie robimy tego, ponieważ wtedy on chciał z jakiegoś powodu usilnie zrównać wszystkie uprawnienia. Teraz pozwalamy ci wejść do tej edycji, no jak będziesz chciał dla etapu start zmienić to uprawnienie to zmienimy, ale tylko dlatego etapu.  
Dla pozostałych zostają takie jakie były.

**Damian Kaminski** 21:08  
Bo tam Jeszcze raz jakbyś mógł pokazać, bo tam jest właśnie taka domyślna pozycja, tak że.  
No nie, nie ma jest, wybierz tak, a nie ma pozostaw bez zmian.

**Piotr Buczkowski** 21:19  
Nie, a nie powinno się wyświetlić aktualne tutaj.

**Kamil Dubaniowski** 21:23  
Nie możemy, no bo właśnie to było w starej wersji i przez to, jak chciałeś zmienić na jednym etapie masowo uprawnienie, to nie mogłeś, no bo wywalało ci, że że tutaj są różne uprawnienia dla tych pól i w ogóle ci nie otwiera do tego edytora, albo musiałeś zresetować uprawnienia.

**Piotr Buczkowski** 21:27  
No tak.

**Damian Kaminski** 21:39  
Ok, ale to nie powinniśmy tego sobie nazwać, bo rozumiem, że taki będzie efekt, że start powinien się nazywać w tutaj w liście rozwijanej pozostaw bez zmian jak zmienisz tylko na inny etap, to tylko tam się zmieni. Tak, a tu pozostanie bez zmian.

**Piotr Buczkowski** 21:40  
No także.

**Kamil Dubaniowski** 21:53  
Tak tego.  
Czyli zamiast tego wybierz uprawnienie miało być.

**Piotr Buczkowski** 21:58  
No bo to powinno być tak, że albo powiedzmy jeżeli są dla wszystkich polsku takie same, dlatego etap uprawnienia to po prostu na przykład edycja odczyt.  
A jeżeli są różne, to jakieś taka sekcja, jakiś taki napis różne uprawnienia, tak.

**Damian Kaminski** 22:14  
Tylko że.

**Przemysław Sołdacki** 22:16  
Ale wiecie co, ja bym tak nie robił, bo jakby tak jakie są uprawnienia to widać w tej matrycy. Tutaj ja rzeczywiście bym zrobił też ten napis, który jest, że tutaj wybierz uprawnienie. To był napis taki nie zmienia i tak.

**Damian Kaminski** 22:29  
Nie zmieniam, no bo de facto co jest pod przyciskiem zapisz tak.

**Przemysław Sołdacki** 22:31  
A jak?

**Damian Kaminski** 22:37  
Tak, żeby ten kto zmienia, no wiedział, że tu się nic nie stanie na etapie start dla tych pól.  
A nie że się zresetuje coś.

**Daniel Reszka** 22:43  
Też Jestem za tym bardziej intuicyjne, tak jak Damian mówi, że nie zmienia i pozostaw bez zmian i wtedy.

**Damian Kaminski** 22:57  
No bo jak dzisiaj wybierzesz coś weź wybierz na starcie i potem jednak też stwierdzić, że nic nie chcesz zrobić. To już Nie możesz wrócić.

**Filip Liwiński** 23:07  
Pracę tak.

**Damian Kaminski** 23:10  
Możesz tylko anulować Jeszcze raz, nie więc może powinna być to dodatkowa po prostu pozycja listy rozwijanej.

**Kamil Dubaniowski** 23:22  
Ewentualnie zamiast znaczy też widziałem gdzieś tak mieliśmy, że x się pojawia obok, czyli żeby wyczyścić.

**Damian Kaminski** 23:29  
Może być też no, ale wtedy ten placeholder dobrze by było, żeby mówił, że tu się faktycznie nic nie wy nie wydarzy.

**Kamil Dubaniowski** 23:41  
No dobra, to żebyśmy też nie zabrali całego spotkania, jakby no jeszcze będą kolejne iteracje.  
Ee to dopiero idzie do wrześniowej tego do czerwcowej nie wkładamy, no bo już za późno to zaczęliśmy, więc jeszcze jest chwila.

**Lukasz Bott** 23:57  
To Kamil, co tutaj jest, skoro to już właśnie Daniel się pojawia jako przedstawicielu? No powiedzmy wdrożeniową serwisowym, czyli tych ludzi, którzy najczęściej będą z tego korzystali. To może faktycznie jakiś dedykowany spotkanie umówić tak i.

**Kamil Dubaniowski** 23:57  
Yy.

**Lukasz Bott** 24:12  
I to Jeszcze raz zaprezentować, opowiedzieć może w szerszym gronie, może na piątkowym, może na piątkowym.

**Daniel Reszka** 24:16  
Dokładnie, bo ja tylko od strony serwisowej, nie o wdrożeniu owcy bardziej mogą jeszcze coś innego używać.

**Lukasz Bott** 24:19  
No to.  
To słuchajcie, to może na piątkowym spotkaniu o piętnastej, tak.  
Nie mówię, że w najbliższej, ale.  
To chyba będzie dobry moment, bo wtedy wszyscy jesteśmy nie.  
Kontynuujmy tak no bo to faktycznie zeszło nam trochę czasu.

**Kamil Dubaniowski** 24:35  
Tak, dobra.  
O k Filip tam podoba chyba za dużo się jakieś niuanse, raczej takie korekcje to tam raczej nie ma, nie ma, nie ma co się na tym skupiać zadaniach w ustawieniach systemowych.  
Przemek, czy ty byś chciał coś o formularzu edytorze graficznym? Jeszcze tam też raczej były korekte niż jakieś nowości.  
Ee plus ten temat strony wylotu wydania i nie pamiętam co jeszcze.

**Przemysław Rogaś** 25:08  
No tak z mojej strony to raczej byłem usprawniania tylko.  
Nie kojarzę takich zmian.

**Przemysław Sołdacki** 25:15  
Czyli kiedy my w ogóle dajemy ten edytor nowy?

**Damian Kaminski** 25:19  
Czerwcowej wersji w tej, która teraz wyjdzie, którą kończymy stabilizer czerwcowej.

**Przemysław Sołdacki** 25:19  
W której?  
W której?  
O KA właśnie ja, kiedy kiedy ona wyjdzie?

**Damian Kaminski** 25:30  
No chcemy, niezwłocznie, jeszcze jeszcze kilka poprawek było realizowanych w końcówce zeszłego tygodnia dokumentację, no jesteśmy w trakcie, żebym powiedział, że raczej do dochodzimy gdzieś tam już do końca, więc czy to się wydarzy w tym tygodniu?  
Jakie były konkluzje tutaj? Daniel z januszem? Chyba w czwartek piątek.

**Daniel Reszka** 25:54  
Takie rzeczy tydzień będziemy umawiać. Czy zgadzacie, że to już jest gotowa wersja, czy nie tak, że jak mówicie, że możemy próbować, to możemy próbować. Na razie jak mówisz, że jeszcze coś wydajecie, no to ja bym poczekał w sensie.

**Damian Kaminski** 26:04  
Tak, to znaczy, w piątek wydaliśmy jeszcze w trybie hot fix owym kilka poprawek zwła.  
Chcę też do raportów, no trzeba to po prostu teraz protestować, popracować nad tymi, jeśli nie będzie uwag, no to będziemy zalecać podnoszenie tej wersji.

**Michal Zwierzchowski** 26:20  
Wszystkie zmiany jakieś piątki były są teraz na.

**Damian Kaminski** 26:25  
No tu zbieramy feedback już wdrożeniowy z tego korzystają Mateusz tam zgłaszał kilka uwag też do tego, żeby to co wydajemy, nawet te nowości były.  
Były po prostu też stabilne tak stabilne, na tyle, że zawsze da się wrócić do wersji poprzedniej. Nie wiem, czy tam już te ustawienia systemowe też mają ten przycisk Kamil.  
Wejścia do wersji starej, bo tego chyba jeszcze nie było.

**Kamil Dubaniowski** 26:46  
Tak to już jest na to już jest na astrofoto się tam jedynie co była różnica, to nazwy, integrację systemowe, integracje definiowane tam został jeszcze integracja modlitw i nie rozszerzenia modlitwą, ale tak przełączki już jest nas trochę boksie i.  
Tak jak ma to działać to działa tylko tam wizualnie się zmieni tekst.

**Damian Kaminski** 27:05  
No można powiedzieć, że dopieszczamy tak eliminujemy ostatnie ostatnie błędy, czy to się w tym tygodniu wydarzy? No ja bym powiedział, że nie wykluczajmy, ale ale dajmy sobie jeszcze chwilę na testy.

**Przemysław Sołdacki** 27:18  
Chodzi mi o to, żebyśmy mogli ogłosić, że jest nowa wersja.

**Damian Kaminski** 27:22  
Mhm.  
Wiemy, że tak jest cel.

**Przemysław Sołdacki** 27:28  
No dobra, to będę czekał na oficjalną informacje. Bardzo co dalej mamy jeszcze?

**Damian Kaminski** 27:34  
Łukasz, czy ty opowiesz o tych zmianach?  
Filtrami, czy to już to prezentowałeś?

**Lukasz Bott** 27:42  
Nie prezentowałam, ale to mogę pokazać tak, bo akurat to mam na.  
No podorędziu.  
Właśnie to stoczyłem.  
To znaczy tak, oczywiście to w kontekście w kontekście tutaj też i nowego podejścia do.  
Prezentacji tych raportów systemowych. Generalnie zmieniamy troszeczkę podejście dotychczasowe doty.  
Przez to duża ilość tych raportów, najróżniejszych jeszcze zrobionych w starej technologii no.  
Było tego dużo, ale niekoniecznie.  
Wbrew pozorom były czytelne, więc wybraliśmy, podeszli i podjęliśmy decyzję, żeby troszkę to zmienić. Przede wszystkim ta korzystamy z dashboard ów takie przyjąłem założenie dashboard zagadkowych dla poszczególnych tam grup, tych raportów systemowych.  
Yy i to jest pierwszy podejście tak, czyli gdzieś tam właśnie.  
Jakieś?  
Jako tego rzeczy przy okazji to propos błędów, to nie wiem, po odświeżeniu mi się po odświeżeniu tego raportu zdublował mi się kolumny, więc.  
Jeżeli ktoś gdzieś tam i to jest ta wersja.  
No ale to jest najnowsza tak które ten, więc zwróćcie na to uwagę, tak.  
Nie zawsze się to dzieje i to jest pierwsza rzecz, czyli podejście zapadkowe. Druga rzecz to jest taka, że.  
Konfigurowane zostały przynajmniej część źródeł danych dla tych właśnie raportów systemowych, które zostały to zdefiniuj.  
One w trybie właśnie lokal, czyli takie one już w sobie zapytaniu mają jakieś agregaty i to, co jest istotne, to żeby to było wydajniejsze, to te agregaty są przeliczane raz dziennie tam. No to akurat środowisku deweloperskim to tam jakieś dobrałem.  
Godziny te takie powiedzmy sobie dowolne, tak, ale to pewnie docelowo ustalimy, żeby to się gdzieś tam wydarzyło. Miało miejsce te przeliczenia gdzieś tam raz, raz na dobę, ale gdzieś tam w godzinach powiedzmy, nocnych, statystycznie rzecz biorąc, no to raczej mamy wdrożeniu u nas w Polsce. Tak, no to nikt tam po nocy jakoś się specjalnie pewnie nie pracuje.  
Yy to jest.

**Damian Kaminski** 30:12  
Myślę, że to dla Daniela istotna uwaga, tak, że po prostu te dane będą spływać raz dziennie. Tak, no tutaj nie uważamy, że.

**Lukasz Bott** 30:14  
Tak, tak.

**Daniel Reszka** 30:18  
Ale to z monitora. Czy to jest jeszcze jakieś inne narzędzie?

**Damian Kaminski** 30:21  
Nie.

**Lukasz Bott** 30:21  
Z generalnie do raportów systemowych zostaną zre definiowane źródła danych zewnętrznych i one będą przełączone w tryb właśnie lokal i raz na dobę będą przeliczane.

**Daniel Reszka** 30:32  
Czyli to niezależnie od monitora od modułu tak to każdy klient będzie to miał.

**Lukasz Bott** 30:35  
Tak, tak, tak, tak, tak i tak docelowo dojdą te nowe źródła. Jest jeszcze jedna rzecz tam być może niektóre źródła zostaną zostaną właśnie w trybie online.  
Ale wtedy w tych raportach i to jest właśnie to, o czym Damian tam dał zajawkę, wywołując mnie, mianowicie tutaj to tak Przemek to chyba przemyk robił.  
Zrobiliśmy coś takiego, ponieważ źródła danych mimo wszystko mogę zwracać bardzo duże ilości danych, to ze względów wydajnościowych i też i na czytelność to wprowadziliśmy coś takiego, że można ustawić domyślną wartość filtru.  
Czyli w tym przypadku dla tego raportu to jest na dacie poprzednie 7 dni, czyli pokazuje statystyki, czyli wchodząc na raport już widzę przefiltrowany raport.  
Na na poprzednie 7 dni, przy czym mogę to sobie zmienić.  
I jeżeli a nie jeszcze jedna rzecz.  
Jeżeli wywalę to wartość.  
To.  
Ta wartość jest ustawie.  
Tu jest wymagane i wtedy on nie wyświetli nam danych, dopóki jakieś wartości w tym filtrze.  
Nie wprowadzimy tak czy trochę takie, bo dotychczas gdyby tego nie było, to raport by wyświetlał to, co zwraca źródeł danych, co powodowało zwłaszcza dla tych.  
Dla tych źródeł danych dotyczących właśnie tych raportów systemowych powodowało, że często to są. To są bardzo duże ilości danych. No i raport się zazwyczaj albo wykrzacza, albo wyświetlał jakiś taki komunikat zbyt dużo danych, więc więc włączy jakieś Filtrowanie i tutaj robimy właśnie tak jakby trochę tą sytuację odwracamy. Zanim wyświetlimy raport, to on może być od razu przefiltrowany po jakiejś tam wartości i to.  
Pomnik sobie może oczywiście tą wartość zmienić, tam jest funkcjonalność, funkcjonalność oczywiście i ona pozostała, że gdzieś tam pod spodem mogę sobie już wstępnie przefiltrować to źródło danych, tylko problem polega na tym, że jest to stały filtr w danym raporcie, no i użytkownikiem ma na niego wpływu to podejście chyba jest zdecydowanie lepszy.

**Daniel Reszka** 33:06  
A jak daleko wstecz? Łukasz, ile tych dni będziemy przechowywać?

**Lukasz Bott** 33:11  
Nie, nie to.

**Damian Kaminski** 33:11  
Nie, to jest niezależne w sensie Jeszcze raz to, co powiedział Łukasz, to co dzisiaj jest w edycji raportu ograniczyć zakres prezentowanych danych, to, co ustawia konfigurator raportu administrator raportu, to zostało po prostu przeniesione na poziom.  
Niżej, czyli Użytkownik może wskazać, jak chce ograniczyć i bez tego wskazania mu się nic nie wyświetli, nie wpływamy w ogóle tutaj na ilość danych, które przechowujemy tylko na to, że musisz wskazać ograniczenie, które administrator ci wytyczył, czyli na przykład tutaj data albo jakiś typ operacji. Mógłby to być, żeby tych danych nie było aż tyle, żeby to było bardziej czytelne.

**Lukasz Bott** 33:27  
Interfejsu.

**Daniel Reszka** 33:48  
No dobra, no ale wskaże sobie poprzednie 1000 dni, no to będzie to samo co wszystko dajmy na to i to będzie o k.

**Lukasz Bott** 33:52  
No no ale to wiesz.

**Damian Kaminski** 33:53  
No ale to wtedy, no tak, tak, ale po to są też domyślne, żebyś.  
Żebyś właśnie od razu miał, powiedzmy też załadowany 7, a nie klikał sobie wpisywał 1000, tak?

**Lukasz Bott** 34:05  
Dokładnie tak.

**Damian Kaminski** 34:05  
A jak potrzebujesz zwiększyć? No to wtedy jest większy, no ale to ma wpływ na na cały system, tak, jeśli nagle twój raport generuje zapytanie jakieś długie, tak.

**Daniel Reszka** 34:15  
Właśnie boję się pod chmurę o to nie.

**Lukasz Bott** 34:18  
Nie no dlatego Daniel.

**Damian Kaminski** 34:18  
To znaczy my usprawniamy to co było, a nie dodajemy dodatkową funkcjonalność, a nie zmieniamy sposobu wyświetlanych danych, ilości ich.

**Daniel Reszka** 34:27  
Znaczy nie no, dodajemy przecież źródła, których teraz nie mieli użytkownicy, nie.

**Lukasz Bott** 34:31  
Tak, ale to jest nie nie moment do źródła danych systemowych były.

**Damian Kaminski** 34:31  
Mieli.  
Mieli źródła.

**Daniel Reszka** 34:35  
Ale nie z tymi danymi.

**Lukasz Bott** 34:37  
Moment, moment źródła danych systemowe były tylko wszystkie były w trybie online i one faktycznie fakty.  
Wszystkim powodowały, że że zwracały dużej ilości danych, w tej chwili dojdą nowe źródła danych dla tych raportów systemowych mowa oczywiście, można je będzie wykorzystać pewnie w każdym innym raporcie, natomiast one już co wstępnie przewag negowane i są przeliczane raz na dobę tak, czyli faktycznie tych danych tam jest troll, może być troszkę mniej tak.  
Ale no to jest świadomie świadome działanie pod konkretny typ czy pod grupę raportów systemowych? Tak no bo troszkę inaczej tam dla performance monitora trochę dla inaczej dla logów systemowych, a jeszcze inaczej będzie.  
Dla tych dla jakiejś tam statystyk yy z ze spraw tak.  
Tak naprawdę to ćwiczenie, czy to to to to akcje, którą tutaj robimy? Ona jest też chcieliśmy wrócić do czegoś takiego, co tu kiedyś. W prawym górnym rogu było raporty, tak.  
Zawsze tam myliło i to były właśnie te raporty systemowe, takie właśnie, które w które dopiero wyświetlały dane, gdy właśnie się wskazało jakieś konkretne wartości filtrów. Tak, no więc ta funkcjonalność też była istotna. Tak, no i Daniel to tyle, jeżeli chodzi o te raporty. Generalnie te idea taka jest, jak jest i tutaj nie wiem też troszkę do ciebie. To już wstępnie śmy rozmawiali to, nad czym pracowałam jeszcze tutaj, to w tym sensie już tam dokończę.  
Bo muszę przetestować jeszcze.  
Podpisywanie idea tak zwanej amadis Security checklist.  
Dotyczy to tak jakby.  
Posiadania glejtu nato, że w danej instancji jamo dita głównie będzie to dotyczyło tych instancji instancji instalowanych u klientów.  
I w pierwszej kolejności pójdziemy do tych klientów, którzy nam dostarczają pen testy. Chodzi o to, żeby mieć glejt na to, że ponieważ mamy wytyczne, więc właśnie na wiki, no to dotyczące tego, jak amo tita głównie aplikacje webowa morita tak zabezpieczyć, więc tutaj.  
Będzie takie wymaganie zarówno w momencie wdrożeń, że przed oddaniem produkcyjnym będziemy musieli, żeby kierownik danego wdrożenia po naszej stronie plus kierownik wdrożenia po stronie klienta podpisali się pod tak oczek listą.  
Że tak takie takie zabezpieczenia zostały wprowadzone bądź nie nie zostały wprowadzone, a jeśli nie, to dlaczego?  
I bo na przykład no nie mają zastosowania w danej instancji i żeby obie strony były świadome, tak żeby to to jest trochę nawiązanie do jednego tutaj, z jednej z sesji Plan testów od jednego z klientów, który robił 2 2 iteracje tych re testów, zarzucając nam, że nie wprowadziliśmy, nie wprowadziliśmy właśnie jakieś tam zabezpieczeń, więc po każdy jakieś tam iteracji pen, testów czy a najlepiej przed jeszcze przed wykonaniem testów.  
Taki taki dokument, który będzie też no swego rodzaju, tak jak powiedziałem gleichen tak, że potwierdzającym, że.  
Na tyle, na ile jesteśmy w stanie tak w dobrej wierze wdrażamy wszelkie zabezpieczenia.  
Który jesteśmy świadomi? Oczywiście pan testy mogły coś tam jakieś dodatkowe luki w wyłapać tak, no takiej takich taki jest ich cel. Tak, no ale, ale żeby i to jest jeszcze jedna rzecz, żeby nie powtarzać właśnie jakiś tam po.  
Wprowadzanie jakieś zabezpieczenie, bo już wiemy, że jesteśmy zabezpieczeni na coś takiego, ktoś tego nie wprowadził, nie skonfigurował i potem jak ten jak bumerang wraca ta sama luka bezpieczeństwa i procenty musimy poprawi.  
No a w zasadzie nie poprawiać tylko powiedzieć, ale to trzeba było zrobić tak i tak, bo to już jest dawno opisane. Tak więc więc taka jest idea tej.  
Listy kontrolnej tak bezpieczeństwa.  
No i trącą to to co ja jak jakiś takich głównych rzeczy, które ja robiłem, tak.

**Damian Kaminski** 39:14  
Dobrze, Piotr, chcesz opowiedzieć o tych mailach?

**Piotr Buczkowski** 39:20  
Ja jakich mailach?

**Damian Kaminski** 39:21  
Mhm.  
O logowaniu maili.

**Piotr Buczkowski** 39:26  
Ale też tydzień temu mówi.

**Damian Kaminski** 39:28  
Było ja już 2 tygodnie temu, tak?

**Piotr Buczkowski** 39:29  
Fakt, te 2 tylko 2 tygodnie temu, tak?

**Damian Kaminski** 39:32  
To Przepraszam, to przegapiłem? No to pytanie, czy ktoś jeszcze?  
Chciałby się czymś pochwalić.

**Lukasz Bott** 39:53  
Nie no słuchajcie, no tu trzeba chyba też pochwalić się na zespół to jest dziewczyny.  
To do roboty wykonały czy chodzi o te testy właśnie z dotyczące stabilizacji? Tak.  
Systemu winstrolu.

**Damian Kaminski** 40:08  
No tak, też dużo dużo właśnie czasu poświęciliśmy na poprawki, tak jak je dzisiaj wyszło. Czy tak jest stabilizacja tak, których powiedzmy nie widać tak jak tutaj dzisiaj wyszło na tej prezentacji Kamila i Filipa.  
Bo coś możemy wytworzyć i że tak powiem szybko pokazać, ale potem jeszcze dochodzą różnego rodzaju warunki brzegowe i i one się pojawiały. Czy to właśnie w tych nowych elementach, którymi tu zajmowali się koledzy z reacta i dorabianie rzeczy, których nie widać, czyli end pointów do nich, do tego nowego całego interfejsu reaktywnego, czy to ustawień systemowych czy ustawień procesu?  
Czy to właśnie jeszcze elementy stabilizujące raporty? No na ten moment wydaje się, że wyczyściliśmy przynajmniej to, co było wykryte, jeśli chodzi o o właśnie między innymi raporty. Natomiast no.  
Dalej pozostaje element testowania i tutaj między innymi jeszcze Łukasz to robi, jeśli chodzi o jeszcze może plany tu warto dopowiedzieć, bo to, co prezentował Łukasz, to było takie troszkę, może niekompletne w kontekście spójna.  
Tam część nas było po polsku, część po angielsku to w kontekście właśnie na kanwie raportów systemowych chcemy wprowadzić tłumaczenia dla źródeł.  
Ee danych tym może gdzieś tam się też zajmiemy, żeby to ujednolicić.  
W najbliższym sprincie tak to możesz opowiedzieć, jeśli jeśli chcesz.

**Lukasz Bott** 41:34  
Dzięki, żeś to wspomnę tamten.  
Może to znaczy generalnie idea jest taka, żeby to znaczy tak, to są tak jakby 2 wątki, bo pierwszy wątek to jest taki, żeby można było nadać alias w momencie konfiguracji raportu.  
Żeby można było nadać alias dla danego pola tak w szczególności, jeżeli na jakimś polu stosujemy agregację to żeby można w jakiś sposób no opisowy podać informację, że to jest ilość czegoś tam tak, no bo nie nie, nie zawsze nazwa nazwa pola czy tam kolumny plus w nawiasie funkcja agreguje ąca tak no to tak niekoniecznie.  
Na pierwszy rzut oka ten jest klarowna, więc można chodzi o to, żeby dawać właśnie jakieś takie aliasy dla tych właśnie colum czy pól używanych w raporcie.  
Które po prostu poprawia czytelność raportu także.  
I to jest to jest z tego punktu śmy weź mniej, ale ponieważ stwierdziliśmy, że to jest troszeczkę dużo roboty jeżeli chodzi o mundurach sportowy, no to.  
Na dość podejdziemy do tego.  
To strona, że jeżeli mamy raporty, które bazują na źródłach zewnętrznych, to to w źródłach zewnętrznych.  
Po prostu dopiszemy właśnie takie te damy możliwość aliasów dla poszczególnych no kolumn tak no bo źródło danych nie jesteśmy w stanie tego zrobić po stronie źródła danych. Tak, no, bo mamy mamy zwracane jakiś tam wynik zapytania sql owego tam oczywiście może być użyte, to to to to funkcjonowało nazwa pola SII, tutaj jakaś kolumna z bazy danych, tak SI coś tam I NAZWA.  
Powiedzmy wyświetlana, ale to jest wciąż stała nazwa tak, a my potrzebujemy chociażby wersji językowej, tak takie tutaj gdzieś pokazywałem. Mamy miszmasz, tak, mam interfejs po polsku raportu tak, a źródła danych pochodzą mi nazwę angielski, tak no i.  
No i ten i i fajnie było, gdyby dla źródeł zewnętrznych dać możliwość ustawienia właśnie wersji językowej. Tak?  
Chociaż aliasu tak dla dla danej kolumny.  
Taka jest.  
Taka jest intencja, tak?

**Damian Kaminski** 44:15  
O k. Nie wiem marku w kontekście teraz Center coś jeszcze chcesz?  
Powiedzieć, czy tam tylko były kwestie?  
Stabilizacyjne.

**Marek Dziakowski** 44:23  
Tym nie w tym segmencie dodaliśmy możliwość logowania za pomocą aut przez Microsoft.  
Ee do panelu administracyjnego dokumentu w zasadzie było to dodane jako takie trochę pomóc przy serwisowaniu dokumentów.  
Była w aktualnej konfiguracji trzeba by jakby wszystkie e maila od naszych pracowni.  
Wpisywać gdzieś tam w jako administrator w organizacji, żeby oni mogli wejść na te dokumenty, nie żeby tego nie robić, to po prostu dodaliśmy mechanizm.  
Pozwala na zalogowanie się na dany adres. E mail, jeżeli jest on podany jako e mail serwis są.  
Mogę to pokazać, jak to wygląda?

**Damian Kaminski** 45:10  
Czyli w kontekście biznesowym po prostu usprawniamy tak działania serwisu czy też administratora danej organizacji. Tak.

**Marek Dziakowski** 45:13  
Tak.  
Nawet nie ministra i taką właśnie nasz serwis czy to mnie, czy to ktokolwiek, czy to przykład Daniela, jeżeli chciałby przejść, a to w tym momencie mieszkając przejść do teraz Center, no musiałbym mieć ten adres. E mail podany w jako administrator administratora danej organizacji, inaczej nie mógłby się zalogować, no ale to jest też tendencja redundancja danych, bo ten email by się powielał dla każdej organizacji, więc do tego dodaliśmy możliwość logowania przez Microsoft.

**Damian Kaminski** 45:20  
O k.

**Marek Dziakowski** 45:47  
Tutaj jest pobierane są dane na temat.  
Jakby dresu email jest sprawdzany czy dany e mail jest Zarejestrowany jako e mail serwisowy, jeżeli tak no to ma możliwość wejścia do dokumentu i nie musi tego dodatkow.  
Wpisywać dla każdego z klientów czy w każdej z organizacji.

**Lukasz Bott** 46:06  
Marek ale.

**Damian Kaminski** 46:06  
Czyli ty tym sterujesz tak to to to to jest na poziomie teraz Center, więc jeśli Daniel chciałby tutaj, to powiększać pulę swoich serwisantów, którzy mają mieć dostęp, to musi się do ciebie zgłosić.

**Marek Dziakowski** 46:08  
Tak.  
Tak.  
Tak.

**Piotr Buczkowski** 46:18  
Co może takie uszy? Co może takie Użytkownik zrobić?

**Lukasz Bott** 46:18  
Ale rozumiem, że.

**Marek Dziakowski** 46:18  
Czy?  
Może to samo co zwykły administrator, czyli wysłać powiadomienie, jeżeli pozwala na to dokument, może z edytorem to to co jakby było dotychczas możliwe do robienia.  
Po prostu jest takie przywrócenie funkcjonalności trochę.

**Lukasz Bott** 46:32  
Ale czekaj jeszcze jeśli tak.  
I jeszcze takie pytanie rozumiem, że ty.  
Tutaj tam nasi nasi współpracownicy, tak serwisowi, tak no to rozumiem, że per organizacja tak czy czyli dla danej organizacji, jeżeli Jestem w na przykład wpisany jako administrator, właśnie ten, powiedzmy z naszego serwisu, tak.

**Damian Kaminski** 46:56  
Nie.

**Lukasz Bott** 46:57  
Czy czy to, że jeżeli ja Jestem wpisany do bazy w teraz Center jako administrator zastaw boksu, to bo mam dostęp do wszystkich organizacji?

**Marek Dziakowski** 46:57  
Nie.  
To dla wszystkich.  
Tak.  
Tak.

**Damian Kaminski** 47:08  
Ale pod warunkiem, że masz dostęp do samej sprawy, bo musisz mieć link, tak?

**Marek Dziakowski** 47:11  
No tak, no tak tak tak no trzeba mieć Link do sprawy, tak możemy wejść, bo inaczej to się nie da.

**Lukasz Bott** 47:16  
No o k.

**Damian Kaminski** 47:16  
Bo to z poziomu sprawy wywołujesz dopiero wejście. Tak więc.

**Marek Dziakowski** 47:19  
Dla mnie to jest też ułatwienie, no bo ja często muszę gdzieś tam zaglądać po tych dokumentach, bo coś się na przykład się nie wyświetla dlaczego zweryfikować, czy już się wyświetlam to ja musiałabym.  
Normalnie to wpisywałam, no proponowałem sobie ten link, bo i tak mam dostęp do tych danych. No i teraz bym musiał wpisywać się przez bazę i wchodzić potem się usuwać bez sensu. A tak to dodam po prostu swój swój adres, e mail do jednej tabeli już mam dostęp wszędzie.

**Lukasz Bott** 47:50  
No.  
Okej, dobry.

**Marek Dziakowski** 47:53  
No i są osoby, które mają podobnie, no że że tam przy serwisie gdzieś w kilku w kilku organizacjach, no to ten email trzeba było wpisać za każdym razem do tej organizacji, no.

**Lukasz Bott** 48:06  
To znaczy tą grę, tylko taka jest. Wiesz tak trochę w kontekście jakiegoś tam, no nie wiem, no bezpieczeństwa danych i rodo tak, bo często to umowy dotyczą, jakieś tam najczęściej podpisuje się jakieś umowy, tak, no więc są to dane poufne. Bardziej chodziło mi o to, że rozumiem, żeby.

**Marek Dziakowski** 48:06  
Jest tego sporo.  
Jeżeli ma dostęp do sprawy.  
To i tak widzi.

**Lukasz Bott** 48:25  
Żeby dostać ten dostęp no to tutaj, no nie wiem, no na przykład decyzje podejmuje również Daniel, tak, że kto ma mieć do tego dostęp tak, żeby to, to niekoniecznie tak.

**Marek Dziakowski** 48:36  
Tak.

**Lukasz Bott** 48:37  
Wszystkim na wiary tak dalej właśnie.

**Marek Dziakowski** 48:39  
No czy jeżeli ktoś ma dostęp do domu, dieta na to i tak widzi te sprawy? Zobaczę podpisany tam dokument.

**Lukasz Bott** 48:48  
W sumie tak no.

**Marek Dziakowski** 48:50  
Inaczej nie wejdzie tam dokument musi wejść przez sprawę, czyli będzie widział dokument przed podpisaniem, to będzie widział co tam jest.

**Damian Kaminski** 48:55  
Znaczy, słuchajcie, bo to koncepcja całości, bo to może warto zarysować historycznie wcześniej, czyli powiedzmy 2 miesiące temu było tak, że każdy, kto miał dostęp i użył linku, wchodził z automatu. Później wprowadziliśmy dodatkowe uwierzytelnienie, które jest teraz, zanim wejdziemy do ekranu, trzeba się uwierzytelnić po to, żeby ograniczyć ten dostęp, żeby nie tylko posiadając link, ale jeszcze zweryfikować, czy ten, kto się loguje jest w puli użytkowników fills zaufanych.

**Marek Dziakowski** 49:09  
Dokładnie.

**Damian Kaminski** 49:26  
I tym steruje klient wprowadzając do swojej organizacji tych użytkowników zaufanych. Teraz to, co prezentuje Marek, to jest kolejny krok usprawnienia, żeby nie trzeba było nasz naszych wszystkich maili, czyli Marka, serwisu, wdrożeń, ewentualnie tutaj na zdf. Jeśli jest taka potrzeba wprowadzać na poziomie tej organizacji, tylko żeby to była taka pula globalna sterowana przez nas.

**Lukasz Bott** 49:51  
No o k dobra, chodzi mi o to, że żebyśmy pilnowali nawet jeżeli to jesteśmy my tak, to żeby to był jednak ograniczony zbiór osób tak, ale.

**Marek Dziakowski** 50:01  
Tak, tak no będzie kontrolowany. No jeżeli ktoś ma nie dostać, to tamto zostanie usunięty z tabeli już nie będzie mógł wejść.

**Lukasz Bott** 50:09  
Więc.

**Marek Dziakowski** 50:10  
Także musi być potwierdzenie. Musi być wpis, że upoważniono jest dana osoba do logowania na te dokumenty, jeżeli nie ma na to, no to nie dojdzie, mimo że jest powiedzmy, że ma ten email astra foxu tak, czyli tak nie wejdzie.

**Lukasz Bott** 50:26  
O to mi chodziło. Dobrze, dzięki.

**Marek Dziakowski** 50:29  
No to to jest taka nowość w zasadzie z tamtego z tamtego sprintu.  
Reszta to były jakieś poprawki jak już.  
Tak.

**Damian Kaminski** 50:42  
No dobra, tutaj padło to tylko nie wiem czy to zostało.  
Chyba nie zostało zaprezentowane, a może warto to pokazać, bo to taka.  
W cudzysłowie głupota, ale mnie bardzo irytowała, więc sam byłem pomysłodawcą tego.  
Tego zgłoszenia, mianowicie strona wylogowania zawiera, czy po wylogowaniu zawiera obecnie.  
Przycisk logowanie tak, bo do tej pory jak ktoś się wylogował no to niestety musiał sam preparować tutaj linki poprawiać go, żeby móc z powrotem wrócić, więc to też zostało.

**Piotr Buczkowski** 51:24  
Link pod logo był przecież.  
Wcześniej było logo.

**Damian Kaminski** 51:30  
Nie wiem, nie wszędzie może było zdefiniowane, nie wszędzie się to wyświetlało. W tym momencie jest po prostu napis logowanie i po kliknięciu wracamy na stronę główną. To logo może nawet jeśli działało, to nie było intuicyjnie. W tym momencie myślę, że jest to dużo bardziej.

**Piotr Buczkowski** 51:48  
Intuicyjny.

**Damian Kaminski** 51:50  
Nie dla wszystkich użytkowników. Myślę, że dla takich bardziej zaawansowanych, tak, chociaż według mnie to logo się nie wyświetlało, musiałbym teraz.

**Barbara Michalek** 51:57  
Też mi się tak wydaje, że nie wyświetlało się, że jego nie było gdzieś tam na tej stronie logowania wylogowania.

**Piotr Buczkowski** 52:04  
Bożena tej nowej, bo na tej co ja kiedyś robiłem, to na pewno było pod samym z tego, czy wielokrotnie skorzystałem sam to zrobiłem, bo też mnie to wkurzało.

**Damian Kaminski** 52:11  
Może masz rację, no niemniej teraz jest napis, który no już każdemu.  
Tą sprawni tak i bez domyślania się czy na pewno logo jest takim elementem? Nie wiem piotrze, czy ty jeszcze chcesz zabrać głos? Jeszcze mamy chwilkę czymś jeszcze chcesz się ewentualnie podzielić albo ktokolwiek inny.

**Piotr Buczkowski** 52:32  
No to akurat częściowo robiłem też tutaj właśnie takie ujednolicenie tego logowania wylogowania, zwłaszcza.  
Pomiędzy starą technologią reaktorem, tak, żeby to wspólnie było, że jak się wylogujesz w jednej, to w drugiej też od razu wyloguje razem z przemkiem droga siem tak udało się.  
Tak zrobić, że no wylogowanie w jednej zakładce wylogowuje we wszystkich, niezależnie na której stronie jesteś.  
I też zachowaniem właśnie tego ustawień czy przekierować na stronę logowania czy na stronę logowania, bo no tam zapewne zależności tak, że.  
Jak jest na przykład auto? Logowanie jakimś provider em to to nie ma sensu wylogowywać na stronie logowania, bo zostanę natychmiast zalogowany ponownie.

**Damian Kaminski** 53:17  
Mhm no właśnie więc to może nie zawsze widać, ale ale zostało tu usprawnione i jeszcze może tutaj wspomnę. Z Mateuszem. Pracowaliśmy też w tym sprincie nad poprawkami do komunikatora, ale nie będę go jeszcze dzisiaj prezentował w tej wersji powiedzmy, ostatecznej, bo bo jeszcze kilka kluczowych elementów wizualnych jest do poprawy i nie chcielibyśmy tutaj.  
Prezentować właśnie czegoś nieskończonego w tym sprincie. Myślę, że to skończymy i pokażemy już taką wersję, którą.  
Którą będziemy chcieli wypuścić jako właśnie taką pierwszą stabilną.  
Myślę, że to się wydarzy jeszcze w tym tygodniu, bo zrealizowanych jest kilkanaście zgłoszeń. Chyba kilka zostało otwartych około 3 4.  
I będziemy z tym wtedy gotowi, żeby to już pokazywać.  
No dobrze pytanie, czy ktoś jeszcze chciałby się czymś podzielić?

**Mariusz Piotrzkowski** 54:15  
Miał mówiącymi drogą też pokazać taką bardzo drobną ikonki grup w interfejsie sprawy z tym Kamilem ogarnialiśmy. Jak to mogłoby wyglądać? I teraz jest coś takiego?  
No INFORMACJA O sprawę wygląda w taki sposób, kolor jest taki sam jak w zakładce do wykonania ten sam mechanizm w uprawnieniach taką listę to widać, że Użytkownik ma Czarny tekst, a grupa ma białą ikonkę także.  
Jest widoczny, które jest które?

**Piotr Buczkowski** 54:40  
Ale dlaczego tej konka jest większa?

**Mariusz Piotrzkowski** 54:44  
Więc może jak może większe od tekstu?

**Piotr Buczkowski** 54:46  
Od tak od tej.

**Mariusz Piotrzkowski** 54:49  
Może się tak częściowo wydawać z 2 powodów. Po pierwsze ikonka jest od krawędzi do krawędzi jest praktycznie obrazem, a tekst, no to jak masz literkę p no to p jest ucięte poza tymi konka może rzeczywiście nieco wyższa dlatego, że jest bardziej kwadratowa i.

**Piotr Buczkowski** 55:02  
Nie wiem, jest większą jakieś 2 Piksele?

**Mariusz Piotrzkowski** 55:08  
To tak testowaliśmy.

**Damian Kaminski** 55:09  
No dobra, to sprawdźcie to po prostu natomiast.  
Bo tu powiedziałeś, że brany jest kolor, ale tutaj te grupy mają różne kolory, więc coś mi tu nie pasuje.

**Mariusz Piotrzkowski** 55:18  
Tak, to to to są, to są te same kolory co w zakładce do wykonania tam też są różne kolory.

**Damian Kaminski** 55:25  
Aha o k.  
No dobrze i skończy to znaczy tak, bo tutaj to ma też wpływ na komunikator. My tam też pracujemy nad tą reprezentacją Group dla czatów grupowych, dobrze by było, żeby to było spójne. To, jak już skończycie to i to przejdzie. Wszystkie testy to to dajcie mi znać.

**Mariusz Piotrzkowski** 55:32  
Te kolory.  
No bo.  
O k. To więcej ciekawych rzeczy takich interesownych nie mam.

**Lukasz Bott** 55:53  
A może dodajmy możliwość wskazania ikonki per grupa, tak jak mamy możliwość wskazania ikony proces.

**Damian Kaminski** 55:54  
No dobrze.

**Lukasz Bott** 56:02  
Tak, rzuciłem wolno pomysł.

**Anna Skupinska** 56:02  
Od no i testujący pomysł.

**Damian Kaminski** 56:06  
Znaczy, myślę, że nie jest najbardziej krytyczne w tym momencie, natomiast jest to jakaś opcja, może nawet niekoniecznie kony, co z samej kolorystyki, ale to no pewnie jest jakiś kierunek rozwoju tak, ale.

**Lukasz Bott** 56:09  
Nie no pewno.

**Damian Kaminski** 56:18  
Myślę, że na ten moment to niekoniecznie jest coś, co czym musimy się znaczy. Musimy się skupiać, chociaż może w tą stronę ostatecznie pójdziemy.

**Lukasz Bott** 56:27  
Na pewno nie, nie, nie musimy.  
Rzuciłem tylko tak jak pomóc dobry.  
Bo powoli kończymy, nie.

**Damian Kaminski** 56:33  
Dobrze, mamy jeszcze 2 minuty. Nie wiem czy ktoś jeszcze chyba już istotnych tematów nie ma, bo nikt tutaj się nie wyrywał, chyba, że ktoś jeszcze coś chce.

**Daniel Reszka** 56:40  
Damian, a tej ikony procesy jak to wspomnieliście, bo one domyślnie się ustawia nazwa jakby pierwsze literki procesu, potem trzeba wybrać ikonę i nie da się przywrócić już tej pierwotnej nazwy.  
Ktoś analizował, skoro robicie te ikony, to może tam też już poprawić to.

**Damian Kaminski** 56:56  
Ale chcemy tak wracać. Według mnie to właśnie powinna być jednostronna.

**Lukasz Bott** 57:04  
Też tak uważam.

**Damian Kaminski** 57:05  
Ustawienie.

**Daniel Reszka** 57:05  
Ktoś przez przypadek zmieni, potem się przyzwyczaili, że mieli proces nazwany DAII teraz nie mogą tam wrócić.

**Lukasz Bott** 57:14  
To nie jest zrobione, zrobię własnych ikon.

**Damian Kaminski** 57:15  
Zastanow no powinni w takim razie ustawić taką ikonkę żeby była spójna z.

**Daniel Reszka** 57:15  
Nowy proces.

**Damian Kaminski** 57:21  
Merytoryką tak.

**Daniel Reszka** 57:24  
No dobra, to jak uważacie, że to jest?

**Damian Kaminski** 57:24  
No dobra, pomyślimy o tym, nie, nie, nie, nie, nie na tym spotkaniu. Dobra, zastanówmy się nad tym na spokojnie.  
Dobra, to w takim razie dziękuję. Życzę miłego.

**Lukasz Bott** 57:35  
Dzięki.

**Damian Kaminski** 57:37  
Dnia.

**Przemysław Sołdacki** 57:38  
Cześć.

**Damian Kaminski** 57:39  
Cześć.

**Daniel Reszka** 57:39  
Cześć.

**Marek Dziakowski** 57:40  
Cześć.

**Mariusz Piotrzkowski** 57:40  
Cześć.

**Lukasz Bott** zatrzymano transkrypcję
Data: 6 października 2025

**Łukasz Brocki**: Też.

**Marek Dziakowski**: Cześć.

**Anna Skupińska**: Cześć.

**Damian Kamiński**: Cześć. Dorzucam jeszcze spóźnialskich. Dobra, to Kamil też coś powie o tych swoich zgłoszeniach, czy to bezpośrednio już przypisujesz tutaj kolego od **Reacta**?

**Kamil Dubaniowski**: Ja przypisuję już do Przemka i do Filipa. Te uwagi z dzisiejszego... właśnie już kończę ostatnie zgłoszenie dla Przemka.

**Damian Kamiński**: Dobra. Ja w świetle. Dobra, słuchajcie, w ogóle nazwa **Board** tutaj wszystkim powinno się to wyświetlić. Dołożyłem dzisiaj 2 takie nowe, bo te stare to nie wiem czy jakkolwiek były przydatne, może globalnie są, ale... No właśnie one mówią nam o globalnie jakiś tam tematach, które są przypisanych. Nie wiem czy ktokolwiek z tego korzystał. Tu będziemy mieli z bieżącego sprintu. Jeszcze pewnie popracuję nad samą kolorystyką, żeby to było spójne jedno z drugim, natomiast będziemy mieli informacje właśnie o tym, ile jest nieprzypisanych, ile jest na jakich etapach, więc może będziemy na to gdzieś mogli sprawniej reagować i właśnie weryfikować ile tutaj czeka nam na merge tematów i tak dalej. Natomiast na podstawie tego też możemy łatwy sposób. Teraz sobie na planowaniu określić, kto jest niedoszacowany, kto jest mocno przeszacowany. Tutaj Mariusza aż 19 chyba zadań łącznie.

**Mariusz Piotrzkowski**: U mnie jest tak, że sporo tych zadań jest prawie skończona, tylko mam jakieś tam drobne rzeczy, które jeszcze muszę dokończyć. Nie zastanawiam nad nimi. Także 4 z nich praktycznie są na wykończeniu.

**Damian Kamiński**: No tak, tu jest jakieś **In Progress**, dobra? Mateusz zaraz jeszcze dostanie zadania, pewnie z komunikatora. Mateusz Kołakowski, to jest zadanie przypisane na jutrzejszą radę. Dobra, mamy kilka pustych, z tego co widziałem jakieś **Hotfixy**. To może od tego zacznijmy? Więc tak, tutaj mamy coś z **Image Engine**? Tylko że to jest stara wersja, chociaż nie już.

**Barbara Michalik**: I cofnij od razu co tu jest opisane, jakby jakieś **repro steps**, gdzie to, jak to tworzyć? Ja nie wiem. Pytanie, jaka jest jaki jest raport? No jest wyeksportowany, ale na jakich źródłach?

**Damian Kamiński**: No tego nie wiemy. Sytuacja jest taka, że to działa u jednego użytkownika, u pozostałych nie. Mamy jakiś błąd, który może coś mówi deweloperom, tak? Czyli jakieś **different number of columns**. Ale może wiemy za mało, więc pytanie, kto ewentualnie tutaj może zgłębić temat? To jest w ogóle stara wersja, tak? Grudniowa, wiem. Więc możliwe, że rozwiązaniem będzie podniesienie.

**Barbara Michalik**: Poczekaj, daj mi na chwilę, ja to sobie.

**Piotr Buczkowski**: Po błędzie. Myślę, że to jest coś z **Unią**. To jest 2 miliony z 2 procesów i mają różną liczbę kolumn. Na przykład jakieś kolumny w jednym procesie nie ma, bo jest niewidoczna, albo coś.

**Damian Kamiński**: No właśnie i może ten, ta jedna osoba nie ma, nie widzi spraw z tego procesu. Może właśnie rozwiązaniem jest to, że to są... No właśnie, **XLS Fakturowania NL** to już tu widać, tak? No i to może jest przyczyną, że u innych się nie wyświetla.

**Piotr Buczkowski**: Albo na przykład jest takie coś, że jakaś kolumna jest tylko widoczna dla wskazanych osób? Tak. Ta wskazana osoba to widzi, a niewskazane osoby nie widzą, bo nie widzą tej kolumny.

**Damian Kamiński**: No to już po częściowo mamy jakieś tropy. Na pewno wyzwaniem jest to, że właśnie to są różne procesy i widoku, no zakładam, że mają zagregowane jakieś kolumny i to jest prawdopodobnie przyczyna. Pytanie, czy Basia powinna się tym opiekować?

**Barbara Michalik**: Chciałam, myślałam, żeby to odtworzyć, najpierw zobaczyć, czy się uda odtworzyć. Bo może jednocześnie niech ktoś weźmie i zobaczy, czy mu się uda, czy wie na czym polega problem i tak dalej z tych logów i tak dalej. A ja spróbuję to jakoś w międzyczasie jeszcze sprawdzić i... nie wiem. Może uda mi się to wywołać, tak, na 2 dni na tej grudniowej wersji. Więc...

**Piotr Buczkowski**: W nowych raportach logujecie błędem zapytanie całe?

**Marek Dziakowski**: Jak się doda moduł, to tak.

**Anna Skupińska**: Tak, jak zresztą modułu.

**Piotr Buczkowski**: No to, no to dodajcie moduł, uruchom, znaczy u klienta, tak? Moduł niech uruchomią, zobaczycie co się zaloguje i powiecie odpowiedź.

**Damian Kamiński**: No dobrze, możecie.

**Piotr Buczkowski**: Lepiej lepiej lepiej zgłosić do klienta, żeby tak, żeby zalogowało to zapytanie **SQL**. W kontekście powstałej wersji, jeżeli jest błąd, to zawsze jest eskalowany.

**Damian Kamiński**: Jaki? Co trzeba wpisać?

**Piotr Buczkowski**: I zróbcie tak tym nowym module, tak?

**Anna Skupińska**: W ustawieniach systemowych musisz coś w logach i wpisać. Log modułu, tak mi się wydaje. A sprawdza...

**Marek Dziakowski**: Które **Report**?

**Piotr Buczkowski**: Dobrze, ale to dajcie też takie coś, jak jest błąd w zapytaniu, to zawsze jest logowane tam zapytanie **SQL** z tych starych raportach.

**Anna Skupińska**: Błędy się zdarzają, jakby później to z nim będzie problem, bo są błędy, które zdarzają się już po wykonaniu zapytania. To wtedy nie mamy już zapytania.

**Piotr Buczkowski**: No nie, no ale to jest błąd w zapytaniu.

**Damian Kamiński**: Dobra, ja to zanotuję, zgłoszę. Czy po prostu logować z automatu, tak, jeśli występują błędy w zapytaniach?

**Anna Skupińska**: O ile się orientuję, to już tak się dzieje, powinno się dziać. On powinien dodawać **SQL**-a do błędu.

**Piotr Buczkowski**: Znaczy, tam jest takie, jest domyślne. Już tak. Jakiś **Trace Log** czy coś, taka funkcja.

**Damian Kamiński**: Tu jeszcze chyba tego nie ma, tak?

**Anna Skupińska**: A w której to jest wersji?

**Damian Kamiński**: Grudniowej.

**Anna Skupińska**: A to musiałam się teraz przestawić ją, trochę ogrzewaną tą obecną. Ktoś inny musiałby sprawdzić.

**Damian Kamiński**: Dobra, dokończmy to co tu ma być dodane.

**Anna Skupińska**: Chwilka, tak, **Report Log**?

**Damian Kamiński**: Dobra, ja się zgłoszę do...

**Anna Skupińska**: Ale to co robisz, że wszystkie raporty będą stawiać swoją informację, nie tylko te, które mają błąd?

**Łukasz Bott**: Dobrze, ale to...

**Damian Kamiński**: Tak, ale to trzeba włączyć, zalogować i wyłączyć. To jest jasne.

**Anna Skupińska**: To takie informuję, że...

**Damian Kamiński**: Dobra, ja to ogarnę z Erikiem i jakąś konkluzję tu przedstawię. Dalej mamy fajny **case** na wersji czerwcowej/marcowej, przepraszam. Wyszukiwanie pola słownikowego podrzędnego, mamy pola z dwóch.

**Piotr Buczkowski**: Nie jest to obsłużone. Może może to nie być obsłużone? Przypisz do mnie. Powiedziałem to zgłoszenie.

**Damian Kamiński**: Dobrze.

**Piotr Buczkowski**: To trzeba wymyśleć jak to definiować, tak? Bo nie możesz podać po prostu, że szukasz po tym polu, jeżeli to pole, ta wartość jest w dwóch miejscach, tak.

**Damian Kamiński**: Mhm. Dobrze.

**Piotr Buczkowski**: Czy to są te dwie wartości.

**Damian Kamiński**: Kolejne to jest przypisane akurat na Radę, bo nie wiem co za tym stało, więc nie wiem czy teraz powinniśmy omawiać. Po prostu nie wyświetlamy w repozytorium spraw zamkniętych.

**Piotr Buczkowski**: Powinniśmy.

**Damian Kamiński**: OK, no też mi się tak wydaje. Nie wiem czy ktoś kojarzy, że było takie założenie, czy to jest jakiś błąd już wtórny, ale chyba tak było od początku.

**Piotr Buczkowski**: Pewnie jak ktoś to robi, użył tam funkcji **GetCases**. Ustawił `Open=false`. Tak, no następne pytanie. Czy tam `Open=true`?

**Damian Kamiński**: Dobra, czy to wymaga jeszcze szerszej dyskusji?

**Piotr Buczkowski**: Bo nie pomyślał.

**Damian Kamiński**: Redukcję Piotrze na jutrzejszej Radzie czy...

**Piotr Buczkowski**: Według mnie nie, według mnie to jest po prostu pomyłka przy **PBI**. Dopiero o tym założeniu czytam. Nie może nie tyle pomyłka, co jakoś pomyśleliśmy o tym.

**Damian Kamiński**: Dobrze, czy ktoś?

**Piotr Buczkowski**: Zmiana powinna być prosta. Powinni tam jest jakaś gadka i tak. Nie, trzeba po prostu ustawić, że otwarte i zamknięte, a nie tylko otwarte.

**Adrian Kotowski**: Że jakiś parametr dodać na przykład? Bo teraz jak to się już niektórzy użytkownicy przyzwyczaili, że to tak działa jak teraz, więc żeby nagle się nie pokazało, że ten jakiegoś klienta...

**Piotr Buczkowski**: A ile i ilu klientów z tego korzysta?

**Adrian Kotowski**: Zmiana. Ten **Rossmann**.

**Kamil Dubaniowski**: **Rossmann**.

**Damian Kamiński**: **Rossmann**.

**Piotr Buczkowski**: No to **Rossmann** to chce tak, zmieniając.

**Damian Kamiński**: **Rossmann** to chce. Oni muszą tylko dlatego to piszę, jak wyświetlić, sprawdzą.

**Kamil Dubaniowski**: Zauważcie też, o co ja zapytałem: jaka jest odpowiedź po tej zmianie? W **Rossmannie** pojawi się 215 spraw na produkcji, które...?

**Damian Kamiński**: Tak, bo właśnie to piszę, tak.

**Kamil Dubaniowski**: Także niech oni to uzgodnią z klientem, że badali tą sytuację, bo może te anulowane w takiej sytuacji powinny być wypinane z repozytorium w trakcie procesu. Jak coś zostało anulowane i nie chcą tego w repozytorium tych spraw na tym statusie, to powinni przy akcji anulowania wypinać też z repozytorium.

**Damian Kamiński**: Dokładnie. Dobra, to oni omawiali właśnie w piątek i podawali tą kwestię. No dzisiaj się te rzeczy, te sprawy nigdzie nie wyświetlają, więc bez sensu w takim razie, żeby pozostawały w repozytorium, jeśli mają się tam nie wyświetlać. Więc po prostu te 200 spraw muszą jakoś obsłużyć. Mają tu chwilę. Pytanie, kto się tego podejmie, żeby to naprawić?

**Kamil Dubaniowski**: Marek, masz przestrzeń, bo ty tam jakieś doświadczenia masz z tym repozytorium.

**Damian Kamiński**: To jest.

**Marek Dziakowski**: Mogę.

**Damian Kamiński**: Dobra, ale czy to powinien być **Hotfix**, skoro to tak działało od początku?

**Kamil Dubaniowski**: Jedyna zasadność tego, że to jest **Hotfixem**, jest to, że aktualnie przez to w **Rossmannie** mają po 3000 spraw do wykonania.

**Marek Dziakowski**: Ja jutro to zrobię.

**Kamil Dubaniowski**: Ona się ładuje minutę.

**Łukasz Bott**: No dobra, słuchajcie, nie ma co deliberować. Marek to tylko zdejmij to z Rady. Jeżeli Marek wie, co zrobić to...

**Marek Dziakowski**: Piotr to zrobi.

**Damian Kamiński**: No dobra, to zostawiamy to u Marka.

**Piotr Buczkowski**: Czy co do zakładki "Do wykonania" - tej właśnie sam sobie tak to tam zadanie, żeby... No jest niepotrzebna. Jeżeli szukasz po tym, gdzie jesteście overem, tak. Trwała grupa jest autorem, to nie ma sensu sprawdzać uprawnień.

**Damian Kamiński**: No dobra, to tu mamy zaopiekowane.

**Barbara Michalik**: Jeszcze mam pytanie Damian, ten poprzedni **Hotfix**, ten... to po pierwsze, czy on ma być przypisany do ciebie, a po drugie nie oznaczyłeś Eryka, więc ja nie wiem czy on będzie wiedział, że to idzie do niego, że on ma zrobić to logowanie.

**Łukasz Bott**: Nie, to nie, bo tak jak chciał to sobie u siebie i wstawić na ludzi.

**Damian Kamiński**: Ja to sobie nawet zapisałem.

**Barbara Michalik**: OK.

**Damian Kamiński**: Ja się zaraz po spotkaniu z Erikiem zadzwoni i to wyjaśnię. Tak, zobaczymy jakie to pola, może wystarczy po prostu zmienić definicję tego raportu i usunąć to pole, które się nie pokrywa i będzie po prostu problemów nie?

**Barbara Michalik**: OK. Bo ja mówię, bo oczywiście my nie możemy pobrać do raportu, bo nie mamy tych procesów u siebie, więc to to jest filler.

**Damian Kamiński**: No tak.

**Barbara Michalik**: Nie wiem, próbowałam wyklikać coś też w tych raportach, no mi się to nie pojawia.

**Piotr Buczkowski**: Nie, nie, nie u klienta, tak? U klienta. A tutaj logowanie zobaczyć **SELECT**-a, sprawdzić jaka kolumna... jakie kolumny brakuje pewnie w widoku i wtedy zdiagnozować dlaczego tej kolumny brakuje.

**Damian Kamiński**: Nie ma sensu, nie. To trzeba zrobić u klienta, tak? Dokładnie. Więc ja to zaopiekuję, jeśli z tego będzie potrzebne jakieś zgłoszenie, to to przepiszemy. A może uda się to rozwiązać?

**Łukasz Bott**: Raport, ale albo proces. Bo to może być może być stan z siebie dobry, tak tylko jak...

**Piotr Buczkowski**: Kiedyś kiedyś takie coś było, że jak ktoś usunął jakąś kolumnę z jednego z procesów, to raporty z kilku procesów, opierającej się też o ten proces, był problem właśnie taki, ale...

**Łukasz Bott**: No może tutaj też jest podobna sytuacja.

**Piotr Buczkowski**: Albo zmienił nazwę kolumny, bo tam jest po nazwie tak zapisywane.

**Damian Kamiński**: Znaczy, niekoniecznie to jest błąd systemu. Tak to może być błąd konfiguracyjny. Dobra, i ostatni to jest przypisane do Łukasza. Tak, no dobra, to to...

**Łukasz Bott**: Dobra, nie ma co deliberować. Tak. No to wiesz co, ja to jestem świadomy. Już goni mnie o to, żeby to zdiagnozować więcej. Dobra. Zdiagnozuję.

**Damian Kamiński**: Dobra, teraz jeszcze zobaczymy, a jest tylko jeden na razie **bug** nie przypisany.

**Łukasz Bott**: Wiesz co, dobra, byłem spóźniony, bo to ja stworzyłem, znaczy to jest taki **bug** rozwojowy. Bo jest faktycznie to jest to, że tych opisów nie są widoczne, a tutaj z taką uwagą to jeszcze gdzieś tam z Basią dzisiaj o tym rozmawialiśmy, jeżeli chodzi technicznie, jeżeli chodzi o te dane, bo tam można się przełączyć w tryb **Markdown** bądź **HTML**. Tak to znaczy to myślenie jest **HTML**, ale może się przełączyć w ten edytor **Markdownowy**. Niestety on jest troszkę do... jeżeli chodzi o wstawianie obrazu. Więc dobrze działa jak jest tylko sam tekst w zasadzie, tak, albo tam linki do czegoś.

**Damian Kamiński**: Nie, dlaczego ja to robiłem z obrazkami?

**Barbara Michalik**: Też mi się kojarzy, że no coś robiliśmy chyba w komunikatorze, nie? To wtedy nam...

**Damian Kamiński**: Tak, na 100%.

**Łukasz Bott**: No dobra, to nie, nie ten. No to masz **repro steps**, masz w trybie **Markdownowym** i za cholerę obrazka nie mogłem wstawić. Musiałem usunąć.

**Damian Kamiński**: OK. To znaczy, no zaraz pokażę.

**Łukasz Bott**: No chyba, chyba że jest jakoś tam schrzanione.

**Damian Kamiński**: Na chwilę mamy sobie obrazek, tylko że ja to robię zawsze w takim trybie nie obrazka, tylko tutaj nie. Tylko zaznaczam kopiuj i w **Markdown** mi wklej się wstawia. On gdzieś tam to sobie zapisuje, bo pewnie nie da się dodać obrazka, może tu się nie da dodać obrazka.

**Łukasz Bott**: Nie da się. Znaczy, nie da się w ten sposób. Nie, nie da się na pewno, wiem to.

**Damian Kamiński**: Zaraz zobaczymy. OK. Może się nie da, tak, ale da się po prostu kontrolować. Jej, ale tam jest znacznik `ewicz` coś tam, dobra. Być może to da się obejść.

**Damian Kamiński**: No dobra. To, to jest... Nie wiem, czy to już jest **Ready To Do**, tak Łukasz?

**Łukasz Bott**: Tak, tak, no to jest gotowe, no.

**Damian Kamiński**: Twierdzę, żeby to nie zapisywać tych swoich zmian. OK, no dobrze, to tylko, że co tu jest potrzebne? Nie wiemy czy tu jest potrzebny jakiś **Backend**, tak? Bo ten opis da się zdefiniować, ale nie wiadomo czy on jest pobierany. Bo jeśli jest, no to w zasadzie działanie jest tylko **Frontendowe**.

**Łukasz Bott**: Nie, moim zdaniem jest **Frontendowe**, bo może zacznij od błędu, to przejdź na listę załączników, no bo już jest tam pochrzanione ten **repro steps**. Nie jeden i otwiera 1, 2, 3, 4. Tak, jeden jaka to jest? Tak, jesteś w trybie edycji też. Wprowadzasz opis. W dwójce nie jest aktywna, jest wprowadzony opis, a po przejściu na kafelek **Dashboard** i ikonka jest wyświetlona, tak? Wciąż, pomimo że opis jest, więc to jest błąd, czyli ten opis jest gdzieś tak, no można go wyświetlić.

**Damian Kamiński**: No tak, tylko nie wiadomo czego zwraca **Endpoint**. No trzeba to ustalić, tak.

**Łukasz Bott**: To już ktoś, kto będzie się tym zajmował? Tak.

**Damian Kamiński**: Dobrze, może upraszczając odpowiedź na pytanie, kto ma to... ja rozumiem. Kamil i Przemek i Filip mają teraz zadania.

**Kamil Dubaniowski**: Tak, ale Filip ma w zakresie tych logów systemowych. I to nie jest raczej na cały sprint, także na spokojnie można.

**Łukasz Bott**: Ja tutaj zadam pytanie Ania, skoro i tak przy tych, bo to jest trochę w kontekście tych raportów systemowych, tak. Oczywiście ta poprawka będzie działała dla każdego, tak.

**Anna Skupińska**: Ja to, no OK. Mogę akurat teraz pracuję.

**Łukasz Bott**: Nie, no bo już, bo jak grzebiesz w tych raportach, no to...

**Anna Skupińska**: OK, rozumiem. Przypomnę, że w **Dashboardach** powinien się pokazywać opis.

**Łukasz Bott**: Nie rozumiesz?

**Damian Kamiński**: To nie jest coś pilnego, to jest... Tak, tak jak tu jest pokazane.

**Anna Skupińska**: Może się po prostu pokazywać w oknie **modalnym**? Że klikniemy tą opcję "pokaż opis", to pokaże się okienko **modalne** z opisem.

**Łukasz Bott**: Może być, no. OK.

**Damian Kamiński**: Tak. Dobra.

**Anna Skupińska**: Możecie mi przepisać.

**Damian Kamiński**: To znaczy, żeby nie wymyślać czegoś na nowo.

**Anna Skupińska**: Ale prawdę mówiąc to skończy, to zrobię raczej na końcu. Jak skończę już wszystkie rzeczy z tymi systemowymi.

**Damian Kamiński**: OK, no to jest element systemowy, więc nikt tutaj o to raczej nie płaci.

**Anna Skupińska**: Ale to jest element systemu, OK.

**Łukasz Bott**: Samo zgłoszenie jest podpięte pod **Epici** związane z systemowymi, tak.

**Anna Skupińska**: OK.

**Damian Kamiński**: To powinien być taki sam element, nie wymyślimy nic na nowo. Dokładnie tak się to powinno wyświetlić.

**Łukasz Bott**: Dokładnie tam. Czyli zrób sobie, zrób sobie jakikolwiek raport z opisem, tak.

**Damian Kamiński**: Jak tutaj?

**Łukasz Bott**: I taka mechanika powinna być. A jak wejdziesz w szczegóły? Wejdź w szczegóły tego raportu.

**Damian Kamiński**: To znaczy w szczegóły raportu?

**Łukasz Bott**: Kliknij na ten raport. No. I do niego wejść. OK. No. No i tutaj masz ten przycisk "pokaż opis", tak.

**Damian Kamiński**: A no to to w zasadzie jest, tylko chodzi o to, żeby to przenieść tutaj, tak.

**Łukasz Bott**: W przypadku **Dashboard** byśmy tak rozmawiali.

**Damian Kamiński**: Przepraszam, **Dashboard**, tak, tak, tak, tak, tak.

**Łukasz Bott**: Mimo że konsekwentnie, czekajcie.

**Anna Skupińska**: Może lepiej zostać także i w raportach, i też to było tak samo.

**Łukasz Bott**: Mimo że konsekwentnie.

**Damian Kamiński**: Nie, poczekajcie. To znaczy były ustalone inaczej. Ja nie wiem czy ustalaliśmy.

**Barbara Michalik**: No właśnie, przecież to już ustalaliśmy. Ja nie wiem czemu zmieniacie wersję.

**Damian Kamiński**: Nie.

**Łukasz Bott**: Dobra, moment. To jak my ustaliliśmy, to może coś pokiełbasiło.

**Damian Kamiński**: Opis ma być na **Dashboardach** w tym menu.

**Łukasz Bott**: OK i tak jest zaproponowane w moim.

**Damian Kamiński**: A na raportach opis ma być tutaj w ramach tego menu.

**Łukasz Bott**: Nie, moment, moment. To jest **Dashboard**, a tak, dobrze.

**Damian Kamiński**: Nieważne w sensie opis, **Dashboarding** być tu, a na raportach opis ma być zawsze tu tak jak Legenda, tak ma być niżej opis.

**Łukasz Bott**: I na to jeszcze i na to jeszcze nie ma zgłoszenia, to ja to na to zrobię dopiero zgłoszenie.

**Damian Kamiński**: OK.

**Łukasz Bott**: Bo zaczęliśmy spotkania. Opisywanie tego i innych błędów przy okazji to.

**Damian Kamiński**: Dobrze. To, to, to wymaga zgłoszenia, no to to przypiszesz też, Annie, żeby to wszystko było już w jednych rękach. Dobrze, z nowych, których nie mam przypisanych. Są 3 z **PBI**. Tutaj nie wiem czemu to jest **PBI**, skoro to jest Mateusz.

**Łukasz Bott**: Mateusz ma taką tendencję, że niby zgłasza błąd, to znaczy tak, robi to jako pewnie znów gdzieś ma tam zapisane albo...

**Damian Kamiński**: Że to nie jest błąd?

**Mariusz Piotrzkowski**: Teraz z Piotrem dyskutowałem już, że według według założeń jest maska jako po prostu wizualna, że do prowadzenia. Pamiętam, że z Kamilem i też dyskutowałem, że chyba Janusz chciał, żeby maska nastąpiła w ogóle, była walidowana? Czy coś takiego. Nie pamiętam dokładnie, o co chodziło. No ale pomysł jest taki, że może rzeczywiście maska powinna być walidowana. Przynajmniej tak, taka taka jest koncepcja, tu tak.

**Łukasz Bott**: No. No ale to jest przecież w tym przypadku, to jest jakiś tam komponent googlowy, który to robi, który realizuje właśnie ten wyświetlanie flagi, numeru kierunkowego i wprowadzenia odpowiedniej maski dla danego kraju. Więc to chyba za bardzo nawet nie mamy wpływu, tak?

**Damian Kamiński**: Czemu googlowy? Znaczy, dobre abstrahuję od tego.

**Łukasz Bott**: Tak mi się wydaje.

**Piotr Buczkowski**: Tak czy nie? Nie googlowy. Tak to jest komponent jakiś tam zainstalowany, skąd wzięte.

**Łukasz Bott**: Tak, no.

**Damian Kamiński**: No dobra, tylko tu chodzi zupełnie o co innego. Chodzi o to, co można wprowadzić w to pole, że tu się daje wprowadzić dwukropek.

**Piotr Buczkowski**: Znaczy, nie wiem czy...

**Mariusz Piotrzkowski**: Bo to praktycznie wszystko, bo to jest pole tekstowe, tak jak każdy inny numer telefonu.

**Piotr Buczkowski**: To jest o tyle problem, że dla różnych państw jest różna długość, tak? Nie wiemy, czy dla danego państwa jest prawidłowo to zdefiniowane. Może akurat pojawiły się jakieś dłuższe numery, może ktoś też wpisać w Polsce jakiś numer typu pogotowie, czy coś?

**Damian Kamiński**: Ale to nie mówimy teraz o koniecznie pełnej walidacji. Możemy to robić też w jakiś sposób krokowo, na razie wyeliminować, że nie można wprowadzać innych znaków niż cyfry.

**Piotr Buczkowski**: Znaczy w tym momencie można to zamienić na pole walidowane z maską telefon. I to dać w walidację, że tylko cyfry wprowadza.

**Łukasz Bott**: Tak, ale pierwsze podejrzewam, że istotne jest też to, że to może być ten numer kierunkowy z flagą, tak.

**Mariusz Piotrzkowski**: Z tego co mówi Mateusz, to tak właśnie o to mu chodziło tutaj takiego.

**Piotr Buczkowski**: No to maska telefon na polu i jako pole... że tylko cyfry. Nie wiem.

**Mariusz Piotrzkowski**: Przy czym też nie mogą być tylko te numery telefonu, bo numer telefonu powinien wspierać nawiasy, powinien wspierać gwiazdkę, kropkę i kratkę. Bo na przykład kropka oznacza wybór kolejnego numeru po połączeniu się automatycznie.

**Łukasz Bott**: Nie kombinujmy tam. Najczęściej to jest potrzebne do wprowadzenia numeru obecnie telefonu komórkowego, tak. Czy po prostu numeru telefonu nawet stacjonarnego? Jakkolwiek, tak. Ale to to, o czym mówił Mariusz, przepraszam, to darujmy sobie tak. Może nie obsługuje centrali, które powinniśmy...

**Piotr Buczkowski**: Właśnie po to, żeby można było takie coś wprowadzić. To jest tylko podpowiedź, tak? Że masz taką podpowiedź, ale wprowadzić możesz cokolwiek.

**Damian Kamiński**: No dobrze, ale walidacja nie oznacza, że my coś utniemy, tylko wyświetlimy, że to jest źle wprowadzona dana i ktoś to musi ręcznie sobie poprawić. Więc nie widzę problemu, żebyśmy to...

**Łukasz Bott**: Dokładnie tak.

**Piotr Buczkowski**: No ale jak nie poprawi, to nie zapisze.

**Damian Kamiński**: No tak.

**Mariusz Piotrzkowski**: Może dlatego regułę zrobić? Myślę, że funkcję jakąś `strip` czy...

**Damian Kamiński**: Nie, nie, nie. To znaczy, co z tego, że nie zapisze Piotrze? To musi poprawić. To jest problem. Według ciebie.

**Piotr Buczkowski**: A jak będzie potrzeba zapisania takiego niestandardowego jakiegoś numeru? No nie wiem, nie wiem jakie są przypadki, tak. Nie chciałbym ograniczać możliwość tylko dla jednego przypadku.

**Mariusz Piotrzkowski**: Natomiast zgadzam się z tym.

**Piotr Buczkowski**: Że gdzieś ktoś chce akurat tak, to musimy wszystkim to zawęzić możliwość wpisywania w tym polu.

**Łukasz Bott**: Moim zdaniem, można się Mateusza dopytać jeszcze raz. Czy to jest problem tego dwukropka?

**Piotr Buczkowski**: No tak, bo pole pozwala wpisać wartość ze znakiem dwukropek, takie jest na screenie.

**Łukasz Bott**: Czy tam... No to niech zrobią nad tym polem tekst statyczny, że nie można wprowadzać znaków takiego, takiego z tego i owego i tyle. Użytkownik też niech będzie myślący. Ma podpowiedź, maskę jaką ma wprowadzić, w jakim formacie ma wprowadzić numer telefonu dla wybranego kraju.

**Damian Kamiński**: Dobra, słuchajcie, przenosimy to na Radę, bo to...

**Mariusz Piotrzkowski**: Tylko przedłużyć powiem.

**Piotr Buczkowski**: Tak.

**Łukasz Bott**: Przenieśmy na Radę, ale moim zdaniem to mówię, próbujemy obsłużyć jakiś skrajny przypadek, bo ktoś gdzieś tam...

**Damian Kamiński**: Idziemy dalej po prostu.

**Mariusz Piotrzkowski**: Ja tylko powiem, że on sobie to obsłuży regułami jakimś.

**Damian Kamiński**: No dobrze, znaczy może obejść. Trzeba to ustalić, czy to opiekujemy, czy to odrzucamy. Dalej mamy ograniczenie listy użytkowników pola systemowych przy sprawie współpracownicy i obserwatorzy.

**Łukasz Bott**: Regułami sobie można oprzeć. Tu chodzi o to, żeby dodać taką opcję, bo to jest w propozycjach. Albo nie, dobra, wróć, chodzi. Chodzi o to, że tak, może te pola ukryć. Natomiast jeżeli są widoczne, to tutaj jest. Bo w tej chwili możesz do współpracowników, do obserwatorów prowadzić dowolną osobę z systemu. Prawdopodobnie chodzi o to, że chcą zawęzić mimo wszystko w procesie, że jednak te listy obserwatorów czy współpracowników, to one powinny być jednak ograniczone do wskazanej w tym przypadku grupy osób, tak. Czyli pewnie na potrzeby danego procesu powstanie grupa. Na przykład, nie wiem, "Obserwatorzy faktur" i w tym momencie chodzi o to, żeby móc przefiltrować to pole na panelu tym prawym sprawy. Żeby tylko takich ludzi móc wprowadzić, tak. Żeby nie wiem, nie można było wprowadzić kogoś spoza tego obszaru. Jest na Radę do przedyskutowania.

**Damian Kamiński**: To też jest na Radę. Zostawiam. Dobra, pytanie jest takie, czy ktoś nie ma zadań na najbliższe dni? Tydzień przynajmniej.

**Adrian Kotowski**: Teraz czekam na jeszcze ten **Linq**-a, więc póki co tam nie wiem czy takich większych tematów możemy. Poza tym, z tym rozszerzeniem tego API, ale to nie dużo, więc możesz śmiało dać przydzielić.

**Damian Kamiński**: Dobrze tylko...

**Kamil Dubaniowski**: Ja bym już nic nowego nie wrzucał, tylko rozdysponował z innych ludzi to, co już mamy. Bo to czego tu nie widać, to nie widać sprintu 39. Tam w międzyczasie piszemy o tym z Michałem, ze sprintu 39. Na bieżący sprint spadnie nam 125 zadań.

**Łukasz Bott**: Filtr można.

**Kamil Dubaniowski**: 71, 70.

**Michał Zwierzchowski**: Już tutaj, już tylko, już tylko 50, bo 70. Co było, natomiast tak, już przepisałem na ten sprint.

**Kamil Dubaniowski**: Tak, czyli 70. To są zadania dla dziewczyn, czyli około tam 55. To są zadania, które nadal jeszcze macie zaległe z poprzedniego sprintu.

**Damian Kamiński**: Dobra, to zaraz do tego wrócę. Adrian przypisuję to tobie. To jest typowo **Backendowe** zadanie **Executor Action** dla pola typu raport. Tu jest wszystko opisane. Było to omawiane na Radzie.

**Kamil Dubaniowski**: Są opisy.

**Damian Kamiński**: Jest całe kompletne zgłoszenie. Więc to ci przypisze, żebyś miał do momentu, no w zasadzie jutro pewnie ustalimy ten nowy wygląd **Endpoint** do **Step Function**.

**Łukasz Bott**: Zdejmij filtr z tych.

**Damian Kamiński**: Tak, tak, to już zdejmuję. I co? Już przypisaliście?

**Łukasz Bott**: Nie ma nic. Zrealizowali cały sprint 39. Super.

**Michał Zwierzchowski**: Nie ma, ja przepisałem tylko takie są. To jest tak standardowo. No i jeszcze jest w poprzednim sprincie 50 zadań na **Evaluating**, **In Progress**, **In Design**, **Investigate**.

**Damian Kamiński**: Dobra, tu jeszcze wam przypominam, że **Failed Test** to jest drugi po **Hotfixie**, tak? Więc też, żeby o to zadbać, ale tu widzę jest tylko jedno.

**Michał Zwierzchowski**: Szczególnie jak jest **Failed Test**, no bo to już jest gdzieś w wersji, nie?

**Damian Kamiński**: No dobrze, no to całkiem sporo tego mamy. Łukasz, twoje tematy.

**Łukasz Bott**: OK, dobra.

**Damian Kamiński**: Dobrze, to co Łukaszowe, to zostawiam Kamilowi. Są trzy.

**Łukasz Bott**: No ale tutaj to są zaległe. Tak, no to zrealizowane to już tam. Poza spotkaniem dzisiaj jutro obgadamy, co zostało zrobione, z tym zostały odpowiednio oznaczone.

**Damian Kamiński**: Dobra. Tu jest coś mojego. To też jakiś banał, to zaraz to przerzucę. Tu mamy nowe, przypisane do Eryka. No nie, już przypisane do Piotra. Eryk zgłosił, przepraszam.

**Łukasz Bott**: Eryk zgłosił.

**Kamil Dubaniowski**: No i to jest prawdopodobnie zgłoszenie z dzisiaj wpięte na zeszły sprint.

**Damian Kamiński**: Nie, nie, nie. To już jest omawiane dawno temu, to już może Piotr poprawił, tylko nie zmienił, bo tu było źle wyliczane dni, że jeden oznaczało, że do jutra, nie do dzisiaj. Kojarzę.

**Piotr Buczkowski**: Tak, tak, nie poprawiłem tego dobrze. No nie miałem czasu, nie miałem czasu poprawić pewnie.

**Damian Kamiński**: Nie wiem, nie ma statusu. Dobra, przerzuciłem to na kolejny.

**Kamil Dubaniowski**: Znaczy, nie ma co brać. Tak, my puścimy automat, tylko żebyśmy byli świadomi, że to wszystko, to też nie jest zalecane. To nie jest naturalne działanie, żeby przypinać automatem. Powinniśmy każde z tych zgłoszeń i teraz przejść i uznać, czy ono nadal jest ważniejsze niż to, co zaplanowaliśmy na nowy sprint. Ale przetniemy automatem i tak będziemy działać. Co z tym, że przeklinamy się zaległości, idą za nami, no bo uznaliśmy je za ważne. Ale nie wyrobiliśmy się. No i teraz też kolejna rzecz do dyskusji. W sumie jest ich sporo, ale myślę, że warto poczekać na Janusza. To jest to, że aktualnie będziemy mieli 70 zadań do testów z zeszłego sprintu, 50 powiedzmy tam około spadnie, czyli to już jest 120 i około 80, 90 zaplanowaliśmy na bieżący sprint, czyli dla testerek. Realnie mamy tam 2 zadania na najbliższe 2 tygodnie. No bo bez testów nie uznajemy, że coś zostało zakończone. Czyli nie ma tego teraz przetestować. 200 zgłoszeń na 3 osoby nie ma szans. Czyli już zakładamy z góry, że nie spełnimy założeń sprintu. No i znowu kolejne 100 zadań nam pewnie przejdzie na testy na przyszły sprint.

**Michał Zwierzchowski**: Będzie, że a propos tych, co są do testów. Tak z tych 70, to większość była w piątek, to do zmerdżowania w ostatni dzień sprintu. Ja budowałem wersję wieczorem. Wyzwanie było, szans nawet.

**Damian Kamiński**: No dlatego będziemy się chyba na tym po prostu opierać przy **Daily** i nie możemy dopuszczać, że tutaj na **Waiting For** będzie 50 pozycji. Będziemy na to spoglądać, czyli tego pilnować.

**Piotr Buczkowski**: Co do tego numeru telefonu to...

**Damian Kamiński**: No i...

**Piotr Buczkowski**: Jeszcze uwaga, bo właśnie przetestowałem to. Wyświetlacz, to jest błędne w najnowszej wersji, tylko że jest błąd. Chyba błąd właśnie dodaje **buga**.

**Damian Kamiński**: No dobra, to wiem, że dodajesz **buga** w sensie do zgłoszenia.

**Piotr Buczkowski**: Nie, zgłoszenie nowe robię.

**Damian Kamiński**: No to powiem, że jest tam tym, to to najwyżej jutro jeszcze to omówimy. Już kompletnie. No dobrze, to znaczy tak, to co powiedział Kamil, no musimy zrobić to przepięcie i przeanalizować wtedy, jak będzie wyglądać ten raport. I najwyżej po przepinać zadania między deweloperami, żeby to było realne. No musimy w końcu te sprinty zacząć czyścić. A jeśli, no i zacząć planować jakoś sensownie, żeby tylu spadków nie było, bo oczywiste jest, że one jakieś mogą być, tak. Tematy mogą się wydłużyć, coś się zablokowane, ale...

**Michał Zwierzchowski**: Ja mogę. No zdecydowanie tego za dużo.

**Michał Zwierzchowski**: Ja mam teraz wydałem trochę szybko, przynajmniej się te 50 automat sobie przez ten sprint dopracuję tak, żeby się przenosiły automatycznie.

**Marek Dziakowski**: Kiedyś też mieliśmy taką praktykę. Ustawialiśmy **Capacity** per dewelopera. Tam w założeniach to miało być chyba jako jeden na styk, to jeden dzień. Dodatkowo jakby zostawialiśmy sobie taki czas na luz, czyli na jakieś tam różne pytania, które się trafiają w trakcie sprintu, jakieś konsultacje i tak dalej. I wtedy przy każdym deweloperze pojawił się też taki **progress bar**, który pokazywał, jak bardzo obłożona jest dana osoba.

**Kamil Dubaniowski**: Ja bym do tego wrócił. To znaczy, miałem to zrobić na jednym spotkaniu, jak będziemy już w pełnym składzie z Januszem. A może powiem dzisiaj, i sobie przemyślicie do tego czasu, co o tym sądzicie? Chciałbym, żebyśmy zmienili raz te nasze spotkania dotyczące planowania, które my robimy bez was. Żeby tam właśnie jakby robić to, co robimy tu tak naprawdę w pełnym składzie, niepotrzebnie zaangażować to też Piotra, żebym miał możliwość tak jak tutaj odnieść się do każdego zaplanowanego zgłoszenia jako architekt i dać uwagi, komentarze, albo uzupełnić jakieś zgłoszenia, błędy. Czy jeśli chcecie w naszym gronie, my sobie przypisujemy te zadania do was i wydaje mi się, że zamiast tego spotkania robić takie 10-minutówki z każdym indywidualnie. Gdzie to wy prezentujecie nam swoją tablicę na dany sprint i sobie omawiamy. Raz wy przychodzicie przygotowani pod tym kątem. Macie podpisane te **capacity**, czyli my wam przypisaliśmy zadania, wy sobie oszacowaliście, ile wam zajmą te zadania. Spotykamy się na 10 minut pojedynczo z wami i dyskutujemy, czy macie jeszcze przestrzeń, czy nie macie przestrzeni, jesteście przeładowani i trzeba coś z tego zdjąć. Bo takie wspólne spotkanie, to dyskutujemy. Kilka osób się udzieli, bo się odniesie do swoich zgłoszeń, a reszta? Koniecznie jakieś korzyści z tego czerpie.

**Mateusz Kisiel**: Mi się wydaje, że jest też taki problem, że nie wszystko wpisujemy w zadania. Na przykład jak są jakieś poprawki w kodzie, że co tam robią, to po prostu w kanale jakimś tam głównym i nie ma zgłoszeń o to, albo też poprawki jakieś.

**Kamil Dubaniowski**: Tak, no ale to co powiedział Marek: wy na dzień planujecie sobie 5 godzin pracy?

**Mateusz Kisiel**: Albo na przykład wiesz, jakieś weekendowe rzeczy, to też jakby zgłoszenie jest. Dlatego tak robi **Frontend**, bo Basia będzie testować **Frontend**, a na **Backend** nie ma zgłoszeń, tak.

**Damian Kamiński**: To muszą być.

**Adrian Kotowski**: Akurat teraz to w przypadku tych integracji miałem teraz porobione zgłoszenia. To jest już w pełni od tematów były podwójne, słusznie.

**Damian Kamiński**: Musimy do tego dojść, że one będą faktycznie.

**Barbara Michalik**: No nie, niby tak, ale no były podwójne. I co z tego, że jak było? One były właśnie niepołączone. Przez to było zamieszanie, bo na przykład część dziewczyn dostawała tak, że jedno zostało **Frontendem**. Ta druga dostawała **Backendem** to tylko samego zadania. Tak więc to też nie było dobrym takim rozwiązaniem.

**Adrian Kotowski**: Trzeba to je łączyć i niech osoba, która dany temat ma dwa zgłoszenia, się testów i tyle. Tutaj no bo też to było podzielone, że można było pracę wyróżnić dwóch różnych osób w kwestii dramatów.

**Damian Kamiński**: Nie będziemy pewnie testować **Backendu** jakimiś dedykowanymi narzędziami, jeśli do tego ma iść **Frontend**, będzie to po prostu testowane razem.

**Mateusz Kisiel**: No i też są jakieś ok.

**Adrian Kotowski**: Tak, ale to jest nie to, żeby ująć **Capacity**, to że ktoś robił właśnie też jakby. Jeżeli różne sprawy o ten temat, więc żeby też to do pracy pokazać na **Backlogu**.

**Damian Kamiński**: No tak, zgoda, tak trzeba będzie do tego podejść.

**Mateusz Kisiel**: No i też kwestia taka, że są jakieś rzeczy, które nie mają zgłoszeń jeszcze. Na przykład Przemek chciał, żeby zrobić obsługę plików do tego pilota, no i nie ma zgłoszenia jeszcze. No i pytanie właśnie, czy to ja mam wpisywać, czy ktoś inny zrobi? Nie wiem do końca, bo nic sobie nie ja to planuję tak.

**Damian Kamiński**: To znaczy tak, musimy to na pewno ustalić. Na pewno też my nie możemy nie mieć wiedzy w tym zakresie, więc określając jakieś wymagania co do jakiegoś **PBI**. Jeśli taki **PBI** trafia na przykład do Mateusza, no weźmy ciebie jako przykład, to ty jesteś w stanie oszacować nawet od razu i będzie to powiedzmy nawet jednym zgłoszeniem, bo będzie się opiekował całościowo, czyli zrobisz i **Backend**, **Frontend**. Natomiast jeśli to trafia do **Reactowca**, no to zakładam, że musi powstać wtedy odrębne zgłoszenie do **Backendu**, bo ktoś musi wesprzeć w tym zakresie tu kolegów. I wtedy będzie to rozbite na 2. Natomiast czy my to będziemy tworzyć? No niekoniecznie, może będziemy tworzyć zajawkę. Może właśnie to, co powiedział Kamil w jakiś sposób nam usprawni, bo jak będziemy mieli te spotkania krótkie z osobami, które odpowiadają za dane zlecenie, no to nam od razu powiedzą: "do tego potrzebny jest **Backend**, więc tworzymy ten **Backend**". To zadanie i przypiszemy to jakiejś osobie, tak. Potem zrobimy znowu wspólnie, po takiej serii z wami zrobimy wspólnie spotkanie, kto jeszcze ma jakieś przestrzenie i wtedy odpowiednią osobą to przypiszemy. Nie ułożymy tego od razu jutro idealnie, natomiast po prostu musimy do tego dążyć, żeby to było sprawne. Sama też samo też określanie tego **effortu**. Tutaj Janusz miał propozycję w ubiegłym tygodniu. Na razie roboczo, więc jeszcze nie chcę jej tu przedstawiać, ale też może. Troszkę to zmienimy. Żeby to było, no nie wiem, prostsze.

**Adrian Kotowski**: Jeszcze też pamiętam teraz, czy kiedyś był taki taki temat. Mieliśmy dewelopera dyżurnego i też nie wiem, teraz chyba to już dawno zanikło. Nie wiem czy już... Wiem, że teraz po prostu nieformalnie jest tak, że po prostu poszczególne osoby odpisują na te potrzeby na czatach różnych ładnie. Interesuje mnie, jak to w sumie funkcjonuje. Już jakieś macie większą wiedzę.

**Łukasz Bott**: Wolna amerykanka jest w tej chwili troszkę. Tak naprawdę, no to tutaj chwała Piotrkowi za to, bo Piotr w pierwszej kolejności gdzieś tam reaguje, odpowiada, a jeżeli trzeba kogoś tam innego wywołać, no to wywołuje inne osoby.

**Damian Kamiński**: Tak, przy czym chcemy ukrócić możliwość wrzucania **bugów** do bieżącego sprintu. Chyba że są to **bugi** związane z... tutaj nie **bugi** osobne, tylko no właśnie błędy na testach, tak. Więc to też jest naszym celem, żeby nie było takiego dorzucania, o ile nie ma przestrzeni, bo planowanie też powinno uwzględnić właśnie wygenerowanie tej dodatkowej przestrzeni na potencjalne **Hotfixy**. Jeśli okaże się, że coś poszło sprawnie niż założyliśmy, albo jakieś **bugi** są powiedzmy nie **Hotfixem**, ale są istotniejsze, tak, mają wyższy priorytet. To będziemy je przypisywać dodatkowo, tak. Natomiast z założenia tylko **Hotfixy** będą wchodzić do bieżącego sprintu. Żebyśmy jak najwięcej realizowali tego, co mamy zaplanowane faktycznie. A nie żeby były takie dorzutki i potem tak jak mamy dzisiaj: 80 zadań przechodzi ze sprintu na sprint. Czyli planowanie nam totalnie leży, no bo nie zrobiliśmy tego, co planowaliśmy w ubiegłym sprincie, ale oczywiście to nie było realne, to też nie jest jakaś pretensja tutaj do naszego całego zespołu, bo było za dużo.
Dobrze, podsumowując, myślę, że mamy świadomość bolączek, działamy w temacie usprawnienia, więc mam nadzieję, że to ułożymy do końca tego roku i naprawdę będzie to już jakoś tam solidnie działać. Natomiast po kolei tak, czyli jakimiś drobnymi krokami od czegoś musimy zacząć. Będziemy pewnie teraz jak Janusz wróci jeszcze o tym dyskutować i będziemy te kolejne usprawnienia wprowadzać ze sprintu na sprint, żeby po prostu pracowało nam się wygodniej i bardziej przewidywalnie.

**Michał Zwierzchowski**: Jeśli chodzi o poprzednie sprinty, to nadal mamy 102 zgłoszenia do przeniesienia. Było 125, więc no...

**Damian Kamiński**: No właśnie. Więc dużo zrobiliśmy. Natomiast plan był nierealny. Więc potem wybieramy w zasadzie, a w zasadzie to wy wybieracie to, co wam bardziej pasuje, albo to, co ktoś głośniej w cudzysłowie krzyknie.

**Michał Zwierzchowski**: Ona różnicuje.

**Damian Kamiński**: Bo gdzieś się odezwie, że dalej na to czeka. Często i tak niektóre zgłoszenia mogą być przypisane ze sprintu na sprint, bo nikt się nie upomina, więc...

**Łukasz Bott**: To pytanie, czy jest sens w ogóle to przepinać?

**Damian Kamiński**: To planowanie leży.

**Łukasz Bott**: Po prostu. Nie zostało zrealizowane w tym sprincie, sobie wisi w tym sprincie.

**Kamil Dubaniowski**: Ja uważam, że testy są zaczęte? Na pewno możemy bez jakichś tam dyskusji, bo nie będziemy teraz tego przerywać bez sensu. Te, które są już gotowe do testów. Też nie byłbym przejrzał to po naszej stronie, zanim tam Michał puści automat. Czy to nadal jest ważniejsze niż te, które wybraliśmy do sprintu bieżącego?

**Damian Kamiński**: No tak, ale to już jest taka też retrospekcja, słuchajcie. Jak coś zaplanowaliśmy, że ma być zrobione, to w mojej opinii powinno być zrobione, bo ktoś może też na to czekać, też w zależności co to jest za rodzaj zgłoszenia czy **bug**. Żebyśmy byli jakkolwiek wiarygodni też w oczach i konsultantów, a przede wszystkim klientów. Czyli jeśli definiujemy się, że danego **buga** poprawimy w tym, albo w kolejnym sprincie, to powinniśmy go poprawić.

**Kamil Dubaniowski**: Dlatego mówię i.

**Damian Kamiński**: Jednocześnie właśnie nie zawsze definiować, że **bug** to będzie rozwiązane w następnym sprincie, bo ich jest tak dużo, że nie jesteśmy w stanie tego przerobić. Więc nie powinniśmy się też bać, informować, że to będzie poprawione na za 2 sprinty, albo nawet za 3 sprinty, bo nie ma na to przestrzeni wcześniej. Ale też wtedy dajemy komunikat, który powinien mieć pokrycie w rzeczywistości, czyli za te 3 sprinty, faktycznie powinniśmy to obsłużyć.
Dobra, no, możemy zostać, jeśli chcemy tutaj. Kamil, Łukasz, bo myślę, że to w naszym gronie nie ma co wszystkich trzymać. I te, co są właśnie zwłaszcza przejrzeć i powoli zacząć to porządkować.

**Kamil Dubaniowski**: Tak, tak, tak, zarówno. Zróbmy i realnie, wiem, że nie wprowadzimy wszystkich zmian pewnie od razu i też chciałbym Janusz wiadomość tych zmian, więc będziemy dyskutować po jego powrocie, ale coś co na pewno bym chciał, to żeby ten **effort** na razie w takim założeniu jak działał do tej pory, że... Oczywiście jutro od tego zaczęli dzień, no budzi się, czy będziemy coś przypisywali, żebyście zweryfikowali czy wszystkie zadania na sprint, jakie macie przypisane, mają ten **effort**. Jak nie, no to już indywidualnie te, które macie do zrobienia bez **effortu**, oszacujcie te **efforty**, bo to będzie dla nas wtedy realne. Czy my zaplanowaliśmy dobrze czy nie? A tak to nadal będzie w ciemno i patrzenie na ilości. Kto ma więcej zadań, kto ma mniej? A to co napisałem, ktoś może mieć 10 i zrobi je w ciągu dnia, a ktoś będzie miał jedno i będzie robił 3 dni.

**Damian Kamiński**: To znaczy, to możecie zrobić pewnie jeszcze dzisiaj, tak.

**Kamil Dubaniowski**: No tak, jak nam pójdzie, zobaczymy.

**Damian Kamiński**: Jeszcze przestrzeń jest. Macie tych zadań kilka, tych co macie przypisane, no każdy z was ma jakieś przypisane zadania, więc... No dobrze, tylko mówię, żeby zrobić to tak jak było, to może ustalmy jak było, albo może już narzucimy tą jednak propozycję nową.

**Kamil Dubaniowski**: Nie jestem w stanie, jakby teraz powiedzieć, ile na przykład `S` czy `M` jesteśmy w stanie robić w sprint. Tam to było jeszcze na tyle, że każdy sobie w stanie to wyobrazić. Czyli robimy w ten sposób, że **effort** 5 to jest cała dniówka waszej pracy, właśnie ze względu na to, że macie wrzutki w ciągu dnia, macie jakieś tam dyskusje, czaty i inne rzeczy, więc 5 to jest 8 godzin waszej pracy.

**Mariusz Piotrzkowski**: A sytuację, gdy jest to jakiś **item**, którym ciężko oszacować **effort**, bo na przykład to jest błąd, który nie wiadomo z czego wynika i to może zająć godzinę, może zająć 5, to w takiej sytuacji liczyć ten **effort** bardziej konserwatywnie czy bardziej liberalnie?

**Piotr Buczkowski**: To nie jest ostateczne oszacowanie, nie jest ostateczne. Jeżeli zajmie dłużej, to to zajmie dłużej, jeżeli zajmie krócej, to zajmie krócej.

**Damian Kamiński**: To jest szacunek.

**Kamil Dubaniowski**: Dokładnie, żebyśmy.

**Mariusz Piotrzkowski**: Tak, tylko pytam wtedy: konserwatywnie, czy liberalnie liczyć to?

**Damian Kamiński**: Słuchajcie, to jest tak. Jest jakiś **bug**, pracujecie, przynajmniej ile zajmie jego analiza. A potem można to poprawiać. To nie jest tak, że ten **effort** już jest kończony i nie można go zmienić. Jeśli po analizie okaże się, że to jest **effort** na, nie wiem, 10, to trzeba tak poprawić i dać 10, bo wtedy my w tych raportach zobaczymy, że ktoś ma nagle zwiększył mu się zakres wykonanej pracy. Tylko no właśnie tutaj ważne jest też to, żebyśmy my dostawali to w miarę na świeżo, czyli żeby nie było sytuacji takiej, że coś ma przypisane **effort** jeden, a potem ktoś pracuje nad tym 2 dni, na koniec wpisuje, że to był **effort** 10, bo pracował nad tym 2 dni. Raczej już wcześniej się dowiemy, dowiecie, że to nie jest jedynka, więc dobrze by było to pewnie aktualizować, jeśli nad czymś tam pracujecie. Przynajmniej raz dziennie, tak. No dobra, można to tak rozpisać. Myślę, że to mniej więcej odzwierciedla to, jak to powinno być wypełnione, żeby tamto na czat. Chyba, że ktoś ma do tego jakieś uwagi.

**Kamil Dubaniowski**: Czy ja bym powiedział, że piątka to jest 8 godzin, czwórka to powiedzmy 6,5.

**Damian Kamiński**: Tylko wiesz, to jest 6,5. Ciężko pewnie określić. To jest raczej ponad pół dnia, tak bym to raczej widział.

**Kamil Dubaniowski**: No to 6, tak?

**Łukasz Brocki**: Tak, szacunek. Nie wiem, czy jest sens się tak rozdrabniać.

**Kamil Dubaniowski**: No tak. Znaczy, żebyście to wy mogli sobie właśnie tak dobrać. Na przykład biorę dzisiaj jedną szóstkę i jedną... jedną czwórkę, jedną dwójkę, tak żeby... W sumie to i tak wyjdzie, że sobie będziecie sklejać czwórkę jedynkę, to mamy **effort** na cały dzień. Więc nawet nie wiem, czy jest sens po prostu zbierać w to w godziny. Waszym celem jest, żeby plan na dzień to nie był **effort** większy niż 5, bo więcej nie zrobicie.

**Damian Kamiński**: Tak, 2 trójki. Lub czwórka i coś drobniejszego, tak, lub też kilka drobnych. Dobra, na razie wrzucam to, żeby w takiej formie gdzieś tam każdy równo to oszacował, czy też były te same wytyczne. A najwyżej to jeszcze będziemy poprawiać. No dobra, to co, zostajemy tylko my.

**Kamil Dubaniowski**: No tak, to, to jak nie przedłużamy, my zostaniemy. Po przypisujemy te **New** i **In Design**. Przejrzymy, co to jest i czy faktycznie to przypisujemy. Jak nie, to zrzucimy na **Backlog** i do końca dnia powinniście mieć już takie tablice, które planujemy wam na ten, na ten sprint. Do tego, co robimy teraz, pewnie na przyszły sprint. No warto było jednak definiować sobie jakieś cele, wrócić do tego. Może nie na takiej zasadzie, jak to było, żeby tam gdzieś w **AMODIT** rozpisujecie te cele współpracy z akceptacji tych celów. To my powinniśmy ustalić, jakie są cele sprintu i przypisać cele do was. Żebyście też wiedzieli, jaki jest cel poza codziennymi jakimiś tam błędami i naprawami **Hotfixów**. No to jednak cel na jakiś **increment** musimy mieć, a wydaje mi się, że my go nawet teraz nie mamy, więc wy tym bardziej. Ale tak jak powiedziałem, no ja gdzieś tam zrobiłem sobie całą listę, co bym chciał przekazać z Januszem najpierw, a potem wspólnie.

**Damian Kamiński**: No dobra. Chyba, że ktoś jeszcze chce zabrać głos. Jak nie, to miłego popołudnia i dzięki.

**Barbara Michalik**: Dzięki, na razie.

**Anna Skupińska**: Cześć.

**Marek Dziakowski**: Cześć.

**Adrian Kotowski**: Cześć.

**Oktawia Ostrowska**: Dzięki.

**Damian Kamiński**: No dobra, to lecimy z tymi, które są na radzie. To do **In Design** i **Evaluating**.

**Łukasz Bott**: I resztę filtrujemy.

**Damian Kamiński**: Tak.

**Łukasz Bott**: Mhm.

**Damian Kamiński**: Czyli **Block**. No **Block** w sumie można też uwzględnić. A resztę to jest już operacyjny.

**Kamil Dubaniowski**: Przepinamy automatem. Znaczy, przypinamy, bo nie ma sensu teraz rozważać, czy przenosimy coś, co jest **In Progress**, bo to znaczy, że ktoś już coś zaczął. Więc bez sensu, bo teraz to wyrzucić i wrócić do tego za miesiąc.

**Damian Kamiński**: No to...

**Kamil Dubaniowski**: **In Progress** przypinamy. W tej chwili testy też przypinamy z automatu.

**Michał Zwierzchowski**: To ja przeniosę.

**Kamil Dubaniowski**: A te... I wydaje mi się, że Michał taką zasadę niestety będziemy musieli przyjąć, czyli niestety zmienić ten ten ten proces, czyli żeby przepinać tylko te, które no już są rozpoczęte, a nie o **In Design** jednak będziemy decydować. My pewnie planując kolejny sprint, czy przenosimy, czy wpadło coś ważniejszego niż te tematy.

**Michał Zwierzchowski**: I jakby tam mówiłem tylko tak, że się listę podają statusu państwa odsunąć czynności państwa.

**Kamil Dubaniowski**: OK.

**Damian Kamiński**: No dobra, to co? Jedziemy do tego. Trochę jest **SetFilter**. Łukasz, ty to robiłeś, obchodzić, czy po prostu na tej już to **Evaluating** to co to znaczyło, już nie powiem.

**Łukasz Bott**: To chyba oznaczało właśnie takie rozpoznanie.

**Kamil Dubaniowski**: **Investigate** mamy jeszcze taki status.

**Damian Kamiński**: No właśnie, ja nie wiem czym te 2 się różnią, nie mam pojęcia.

**Kamil Dubaniowski**: A **Evaluating** to znaczy, że ma...

**Łukasz Bott**: Nie, **Evaluating** to bardziej jest oszacowanie. Dobra.

**Michał Zwierzchowski**: Ja właśnie nie wiem skąd ten status jest, bo ja to wczoraj patrzyłem na te statusy i nie widziałem takiego statusu na liście. Więc nie wiem skąd.

**Damian Kamiński**: Bo on dotyczy chyba **PBI**.

**Łukasz Bott**: **Investigate** dotyczy **fixów** i **bugów** i to jest dosłownie śledztwo.

**Kamil Dubaniowski**: Tak, to jest tak.

**Łukasz Bott**: Czyli dostajemy zgłoszenie jakiegoś **buga** od konsultanta. Jest on na **New**. Jeżeli my się podejmujemy i powiedzmy, że na razie go diagnozujemy, to właśnie **Investigate**, tak? A **Evaluating** to jest takie bardziej projektowanie, szacowanie.

**Kamil Dubaniowski**: Czy to **Evaluating**? Tak, nawet komentarz sobie dodałeś, tak? Czyli ktoś dodał nam zgłoszenie, ale my jeszcze wiemy, że coś trzeba zrobić ponad to i dodałeś tam komentarz. Chciałbym, czyli żeby...

**Łukasz Bott**: Tak, no i to zostaw. Mi to przypnij na 41 [sprint]. Dobrze.

**Damian Kamiński**: Mi się wydaje, że to tak działało. Że to było zgłoszenie kiedyś z... Nie wiem czy na wszystkich, ale na **Set Dictionary Filter**.

**Kamil Dubaniowski**: Nie, nie, no tak właśnie o to chodzi, że nie zrobiliśmy tylko na jednym.

**Łukasz Bott**: No i właśnie dlatego ja to zostawiłem, żeby to zdiagnozować, tak. Możliwe, że nie ma w ogóle tematu, tak. Nie, nie szukaj tego.

**Kamil Dubaniowski**: Się przypinamy z ryzykiem takim, że jak to nie jest zrobione, to na 41 sprint zajmiemy komuś dniówkę, tak. Czyli już kolejna dniówka wypada, bo **effort** jest 5.

**Łukasz Bott**: To na którymś spotkaniu piątkowym? Na razie zostaw to mi. Ja to zweryfikuję, najwyżej przepadnie.

**Damian Kamiński**: Bo widzisz, bo to jest jeszcze kwestia, tak. Pytanie, czy takie rzeczy, które są u nas w **Designie**, bo my możemy coś robić w **Designie**, a niekoniecznie to jest na ten sprint. To znaczy, że tego nie kończymy. Czy to powinno być jako **iteration sprintowe** czy jakieś dedykowane? Bo to też jakby pozostawia nam nieskończone zadanie. W kontekście jak coś jest **In Progress**, ale niekoniecznie ma być na tym sprincie zrealizowane, mam na myśli tak, czyli wydane. Może pod tego typu zadania my powinniśmy mieć jakiś odrębny **Backlog**, taki, który... no właśnie.

**Kamil Dubaniowski**: Nie, no **Backlog** jest dla nas.

**Damian Kamiński**: OK.

**Kamil Dubaniowski**: Może to nie powinno być przypisane do sprintu, dopóki nie jest zrobione **Evaluating**.

**Łukasz Bott**: Po prostu, tak może tak to powinno być.

**Kamil Dubaniowski**: Na **Backlogu** możemy mieć **New**, których jeszcze nie ruszyliśmy, ale możemy mieć też **Evaluating**, czyli podjęliśmy, przeanalizowaliśmy i wiemy, że coś jeszcze trzeba tam doprecyzować, albo edytować w zgłoszeniu. No ale to wtedy nie jest przypięte do sprintu.

**Łukasz Bott**: Analizujemy. Tak i nie miesza w sprint.

**Damian Kamiński**: No dokładnie, jeśli sprint traktujemy w kontekście rozliczania skończonych zadań, no to to może być zadanie, które przypiszemy na kolejny sprint nie po wykonaniu.

**Kamil Dubaniowski**: Tak, tak.

**Łukasz Bott**: No ale w momencie... warto je przepiąć na kolejny, czy jeszcze nam kolejny sprint? Bo Mateusz Kołakowski gdzieś na piątkowym spotkaniu chyba sprzed 2 tygodni wygrzebał takie zgłoszenie z lamusa. No bo zobacz po numerze, tak. Byłoby się nagle gdzieś tam coś przypomniało i być może do czegoś tam było to potrzebne.

**Kamil Dubaniowski**: Ja bym powiedział, że ścieżka w ogóle statusów powinna być taka, że status **New** to są zadania tylko na **Backlogu**, no to to jest jakby **New**, nowe zadanie. Nikt jeszcze nie wie co to jest, takie nieprzeczytane, tak miło. W momencie, kiedy ktoś z nas je podejmuje, czyli deklaruje, że ja je przeanalizuję, przypiszę do sprintu i, znaczy, ocenimy, czy to jest na tym czy na następny. To jest to właśnie **Evaluating**, czyli mamy **New**, później **Evaluating**, czyli to jest sygnał dla nas wewnętrznie, że ktoś już się tym zadaniem zajmuje i ja nie mam potrzeby czytać tego zgłoszenia. Później w momencie, kiedy **Evaluating** jest zakończone przez nas, to jest **Ready To Do** i to nadal może wisieć na **Backlogu**, to znaczy, że zgłoszenie jest przejrzane, zaakceptowane. Zgadzamy się, że robimy to, ale sobie wisi **Ready To Do** nadal na **Backlogu**. No i później z tych **Ready To Do** my tak naprawdę wybieramy zadania na sprint.

**Damian Kamiński**: Wybieramy.

**Kamil Dubaniowski**: Czyli jakby deweloper nie powinien mieć żadnych zadań na etapie **New**, **In Design** i **Evaluating**. Ich zadanie zaczyna się od **Ready To Do**.

**Łukasz Bott**: Chyba że bierze udział w czymś takim procesie.

**Kamil Dubaniowski**: Tak, no może być na przykład Piotr, tak, bo on będzie nam pomagał rozpisać zadanie. No ale to nadal nie jest zadanie na sprint, to jest zadanie na **Backlogu**.

**Damian Kamiński**: Tak, tylko wtedy, jeśli to będzie na Piotrze, czy my to upilnujemy?

**Kamil Dubaniowski**: Znaczy, tak, moim zdaniem, tak. My powinniśmy brać wszystko, co jest na **Backlogu** w tych 3 statusach i Piotrek też to, co sam zauważyłeś. Powinien brać udział z nami w planowaniu, bo to on będzie robił większość tych.

**Damian Kamiński**: Czyli to mam to już przypnijcie na **Backlog**?

**Łukasz Bott**: Już przypnij, tak jak się tym zajmujesz.

**Kamil Dubaniowski**: Myślę, że tak możemy tak działać i dokładnie. I w pierwszej kolejności przejrzymy z **Backlogu** te, bo to znaczy, że już zaczęliśmy tam robotę nad tym.

**Damian Kamiński**: Dobra, tu jest coś też prostego. Z Rady to do Łukasza, no to to w zasadzie może zostać tak, bo tutaj tylko wprowadzić i zamykamy, tak? To to bym zostawił, tylko przypiął.

**Łukasz Bott**: Na 41 [sprint] i to już jest.

**Kamil Dubaniowski**: Tak, ale co tu jest do roboty? W sensie przypisujemy to komuś w takiej...

**Łukasz Bott**: Aktualizacja dokumentacji.

**Damian Kamiński**: Ja wiem.

**Kamil Dubaniowski**: Bo to jest twoje zadanie, tak? W sensie ty to będziesz realizował.

**Damian Kamiński**: Tak, tak, tak dokładnie.

**Łukasz Bott**: Tak, tak.

**Damian Kamiński**: No dobra, czekajcie, gdzie jest już po prostu czy nie wywali mi tego, nie wywali, dobra? To w zasadzie jest tylko, bo to nawet analizowałem, mi potwierdzałem. Koniec. Dodaje możliwości rozbudowania raportu z **JOIN**-em do pola typu odnosi. To jest i działa w poniższym.

**Łukasz Bott**: Wiesz co? Ja miałem ja to sobie zostawiłem **Evaluating**, bo ja mam...

**Kamil Dubaniowski**: Coś tam nie działało chyba w trakcie.

**Damian Kamiński**: 100%.

**Łukasz Bott**: Nie, bo jest to jest to nowe, ale trzeba to dobrze przetestować, bo to nie...

**Damian Kamiński**: Jak tu teraz moje? Sortuj po data utworzenia malejąco. To nie było to. Może to jest to?

**Łukasz Bott**: Wiesz co, to wyszło pytanie z konsultantami, ty na szybko coś tam sprawdziłeś, że chyba jest, ale, ale była wątpliwość, czy na pewno to dobrze działa, tak. Dlatego to jest na **Evaluating**.

**Damian Kamiński**: U siebie nawet w teczce. Tak, ale coś tam nie działało. Tak, tak, tak, nie działało. To dobrze, tak. Potwierdzam, masz rację, to było tak, że data utworzenia malejąco.

**Kamil Dubaniowski**: Na chwilę odchodzę od komputera.

**Damian Kamiński**: To było to. No i coś i to nie działało. Czy dla jednego się przeniosło, bo data urodzenia i wymiar etatu jest odnośnika, a dla pozostałych z jakiegoś powodu nie. Przy czym pytanie, czy to nie jest tak? Że zróbmy sobie coś takiego, że on pobiera tylko pierwszy.

**Łukasz Bott**: Bardzo dziękuję.

**Damian Kamiński**: Może to... Może, no tak, dziwnie to wygląda, że wiesz. Żeby ci to pokazać o co mi chodzi. Pracownik. Dajemy sobie pracownika, zapisz, zakończ. Znaczy tu jest Fryderyk Jurkiewicz, przypisany. I teraz jak posortuje. Jak tutaj tego Fryderyka szybko. Dobra, nie uda się to. Może inaczej dodam tutaj. Pracownik. Ciekawe.

**Kamil Dubaniowski**: Dobrze, bo znowu lecimy tak jak zawsze nam się zdarza. Zostawiamy, nie testujemy. Teraz to nie jest celem. Celem jest decyzja, co z tym dalej.

**Damian Kamiński**: No.

**Łukasz Bott**: Nie, czyli jest na **Backlogu**, OK? Czyli to zamknij, bo to już rozmawialiśmy.

**Kamil Dubaniowski**: Spada na **Backlog** i będziemy testować potem.

**Damian Kamiński**: Chcesz ten link? Czy będziesz robić to po swojemu?

**Łukasz Bott**: Dodali. Dam mi trochę mniej i zrobię to jakoś tam swoje.

**Damian Kamiński**: Dobra, wrzucam ci. Będziesz miał w razie czego, żeby sobie potestować. Och, jeszcze nie tu gdzie trzeba. Przepraszam, czekajcie. Jak to teraz wyraźnie było?

**Michał Zwierzchowski**: Co do co do tego **Backlogu** i sprintów, to jak chcecie to też możecie sobie definiować sprinty oddziałami, że do soboty jakoś grupować jak chcecie.

**Łukasz Bott**: Nie słyszałem, klientem.

**Michał Zwierzchowski**: Bo te sprinty są tylko dla **AMODIT**. Widzę, że zabrakło mi uwag dla po pewnym.

**Damian Kamiński**: Masz rację, można się nad tym ewentualnie zastanowić, czy tutaj pod spodem chcemy mieć niekoniecznie, nawet sprinty, ale może jakieś. Można się nad tym zastanowić. To racja. Czy chcemy mieć jakieś wewnętrzne niżej? Dobra, na razie **Backlog**. Wracamy, idziemy dalej. Brak danych, to jest też przy mnie.

**Kamil Dubaniowski**: Czy wiecie, bo możemy zrobić teraz przerwę i niech każdy przejdzie i zrobi to **Investigate** i te zgłoszenia przeanalizuje, bo też zrzucanie teraz wszystkiego na **Backlog**, żeby za chwilę wrócić do **Backlogu**, bo my nie zrobiliśmy swoje roboty. To słabo. Ja też tam mam jakieś swoje **Evaluating**, więc...

**Damian Kamiński**: Dobrze. Czyli żeby to na razie albo inaczej, przypinamy to na kolejny czy zróbmy **New**? Teraz tak.

**Kamil Dubaniowski**: Zróbmy **New**. Znaczy tak, zrobimy. No właśnie, co? Co jest sens robić? No bo **New** to tak naprawdę musi przejść też **Investigate** czy tam **Refinement**, żeby ocenić co tam trzeba zrobić i czy zgłoszenie jest kompletne.

**Łukasz Bott**: Ale to wiesz, to teraz nie, nie możemy teraz przejrzeć właśnie, żeby zdecydować, czy...

**Kamil Dubaniowski**: Więc jak tak naprawdę to jest nasz **Backlog** w tym momencie?

**Łukasz Bott**: Ja się tym zajmiemy, tak. Bo może jest na **New**, jest na tyle klarowne, dobrze opisane, także da się to od razu. Wiesz, że tam...

**Kamil Dubaniowski**: No to tak zróbmy tak, czyli jeśli lecimy po wszystkich, jeśli jest opisane i zgadzamy się, że to robimy, no to... To pytanie, czy w tym sprincie? Jak nie, to na **Backlog** leci.

**Łukasz Bott**: Albo na następny, dobra?

**Damian Kamiński**: Dobra, to nie jest krytyczne, też można to przeplanować. Tutaj jest informacja. Nie są odnotowywane w jego profilu, natomiast na pewno notowane w aktywności administracyjnej, więc to też nie jest powiedziałbym krytyczne. Bo gdzieś tam to logujemy, tylko może nie w tym miejscu co trzeba.

**Łukasz Bott**: W tym miejscu trzeba pewnie jest dobrze logowane w sensie struktur bazodanowych, tylko po prostu niekoniecznie prezentujemy tego, tak. Tu jest rozjazd, no bo to jest czynność wykonana faktycznie gdzieś tam w ramach konta, tak. Mamy po prostu jest rozjazd z prezentowaniem tej informacji w 2 różnych miejscach, tak. Znaczy w jednej jest, a w drugiej nie jest, tak logicznie. Być może powinno być w obu miejscach tak prezentowane, ale to...

**Damian Kamiński**: Tylko właśnie te upychanie według mnie. Ja to zdejmuję na **Backlog** i będziemy szacować faktycznie, czy my mamy na to przestrzeń. Oszacują deweloperzy ten **effort**. Na razie to z działem, żeby tego nie przepinać. Dalej mamy wyszukiwanie wielu spraw, jednocześnie stare raporty. Pytanie, czy w ogóle to opiekujemy klient?

**Łukasz Bott**: Dom.

**Damian Kamiński**: Zauważył. Ja bym powiedział, że do widzenia nie ma starych raportów. Mówimy o wersji czerwcowej, nic tu nie poprawiamy. Wyszukiwanie wielu spraw jednocześnie, starsze raporty.

**Łukasz Bott**: Zobacz, zobacz komentarze jakieś.

**Damian Kamiński**: Wielu spraw po **ID** jednocześnie, tak jak miało to miejsce w starszych wersjach.

**Kamil Dubaniowski**: Nie wymyślałem te naukę to takie jak. W sensie wyszukiwanie pełnotekstowe znajdowało co i po przecinku. Do wyszukiwania po **ID** jest filtr po **ID**, a nie wyszukiwanie tekstowe.

**Damian Kamiński**: A teraz rozumiem, ale to... Poniżej zrzut ekranu w wersji, na którym widać, że ten mechanizm działał prawidłowo. No dobra, a w nowym? Nie ma przykładu, tak po prostu jest tylko, że...

**Kamil Dubaniowski**: Czy w nowym module, tak?

**Damian Kamiński**: No mogło się, ja rozumiem, że w starym to samo, tylko po prostu...

**Kamil Dubaniowski**: Czy w starym module, w nowej wersji?

**Damian Kamiński**: Tutaj mógł zmienić też sposób zapisywania, bo to jest mówimy o starej wersji, o wrześniowym. Od tamtej pory na pewno były poprawki w samym sposobie zapisywania. W **Rusinie** tam Piotr coś poprawił w tym zakresie, więc no może takiego czegoś już nie wspieramy i tyle.

**Kamil Dubaniowski**: No to jeśli ci mało, to moim zdaniem wtedy był błąd. No bo ta pierwsza sprawa nie zawiera i tej drugiej, więc dlaczego znalazło?

**Damian Kamiński**: No to pewnie spacja coś robiła. Dobra, jak dla mnie to jest do odrzucenia. To jest test. Testy to tylko pytanie. Gdzie jest kontekst biznesowy, że to faktycznie musi tak działać, bo oni coś tam tak wyszukują? Czy ktoś szuka na siłę problemów? Nie.

**Łukasz Bott**: Wiesz co, olejmy to?

**Damian Kamiński**: Dobra, tylko musimy coś napisać. Najwyżej tak i przełącz na **Block: Waiting for Information**. Wskaże Eryka tam u góry i tym.

**Kamil Dubaniowski**: Jak dla mnie te wszystkie **Block: Waiting for Information** automatycznie do uzyskania informacji. W sumie do stanowienia. Ale czy one powinny być przypięte nadal? Bo to się kończy tak, że oni nam oddają odpowiedź za 6 tygodni.

**Michał Zwierzchowski**: A tych zadań, tych zadań też ogólnie bardzo dużo, bo jest bardzo 70 wszystkich i to również.

**Łukasz Bott**: No wiesz.

**Damian Kamiński**: Ja zgubiłem wątek. Co ty powiedziałeś?

**Kamil Dubaniowski**: Bo teraz, no to mamy to zaplanowane na sprint 41.

**Damian Kamiński**: To.

**Kamil Dubaniowski**: Ee, 39, nawet tak. Zadamy im pytanie, przełączymy na Eryka, a Eryk...

**Łukasz Bott**: Wróci do tego dopiero za 2 tygodnie, za 3 sprinty.

**Kamil Dubaniowski**: No miał około 20 takich zgłoszeń.

**Damian Kamiński**: No i trudno, ale to w ogóle nie przypisujemy do sprintu. Znowu zdejmujemy.

**Kamil Dubaniowski**: Tak odpowiadam. Tylko, że to nam się wtedy tak. No właśnie o to mi chodzi, że takie **Waiting for Information**...

**Łukasz Bott**: Zdejmij ze sprintu, no.

**Damian Kamiński**: Nie, takich nie ma. Nie ma szans. Póki jest takie nieustalone, to my w ogóle tego nie planujemy. Na razie ustalamy w ogóle coś. Według mnie **Investigate** nie ma prawa być na sprincie.

**Kamil Dubaniowski**: Na sprincie, no to...

**Damian Kamiński**: Jak wchodzi w tryb **Investigate**, to niestety spada, no chyba że coś wyszło w trakcie, tak. Ale to naprawdę jakiś specyficzny przypadek.

**Kamil Dubaniowski**: Tylko, że o tym mówiłem, że teraz w tym momencie to tak naprawdę powinieneś to zrzucić na Eryka i **Waiting for Information** status.

**Łukasz Bott**: Dobra.

**Damian Kamiński**: I tak bym chciał zrobić, tak.

**Łukasz Bott**: Tak, no i tak zróbmy.

**Kamil Dubaniowski**: Czyli mi o to chodziło, tak, że na sprincie nie powinno być zadań o statusie **Block: Waiting for Information**, bo my nie wiemy, kiedy się tej informacji spodziewać. Brak informacji na etapie, kiedy my byliśmy w trakcie planowania, oznacza, że to nie wchodzi na najbliższy sprint. To nie jest żaden bloker.

**Łukasz Bott**: To ja sobie oznaczyłem **Investigate**, bo jest.

**Kamil Dubaniowski**: To już jest w tym momencie sygnał, że najszybciej to zrobimy w 43 [sprint]. Mamy tak nam odpowiedzi. Dzisiaj mamy już potencjalnie powinniśmy 41 mieć zaplanowany i zamknięty.

**Damian Kamiński**: Jak dla mnie to nigdy tego nie zrobimy.

**Łukasz Bott**: I umrzesz i.

**Kamil Dubaniowski**: No tak, no tak. Większość tych etapów się pokończyło, bo to jest tych 28. Nie patrzyłem szczerze ile, ale tak po mailach to jest 15, sami pousuwali.

**Damian Kamiński**: No i bardzo dobrze.

**Kamil Dubaniowski**: Do tych po tym, jakich po oznaczył.

**Damian Kamiński**: To Piotr, no właśnie **In Design**. No i właśnie teraz pytanie: takie tematy na Piotrze, z racji że on no nie wiem, nie wiem jak on pracuje, tak. Czy na której zakładce? Czy on patrzy na to, co jest przypisane do niego i nie ma znaczenia co jest tu. Jakoś sobie filtruje to po sprincie. To też trzeba z Piotrem ustalić. Natomiast to powinniśmy gdzieś tam zaopiekować, tak?

**Łukasz Bott**: Może nie.

**Kamil Dubaniowski**: Mi też się te nasze **Daily** w tym kontekście nie podoba, że my lecimy na wpisach z tego **Jira**, przez co nie widzimy tak naprawdę co kto ma na tablicy jeszcze realnie i czy wziął na dzisiaj najważniejsze na pewno zadania.

**Damian Kamiński**: No to może powinniśmy przestać, no. Wiesz, wszystko jest płynne, to są nasze zasady.

**Kamil Dubaniowski**: I wtedy mamy pewność, że każdy wie, co ma na tablicy, bo codziennie opowiada o tym.

**Damian Kamiński**: I nie mówi, że...

**Kamil Dubaniowski**: Z tablicy patrz, biorąc zadań.

**Damian Kamiński**: W tej chwili weźmie.

**Kamil Dubaniowski**: Tak, bo wtedy my widzimy, że nie masz nic na tablicy, to co sobie weźmiesz. To i to my w sumie powinniśmy dać zadania takiej osobie od razu. Podejrzewali.

**Damian Kamiński**: Dobra, powiem tak, ja takiego bym nie rzucał na **Backlog**, żeby to nie przepadło. To bym zostawił. Ja wiem, że to tak nie powinno być, ale spokojnie to ośmieszy, żebyśmy wiedzieli właśnie, żebyśmy mieli porządek w tym **Backlogu** z priorytetami. Chyba że zrzucamy na **Backlog** z priorytetem jeden, bo to po prostu powinno być zaopiekowane, bo teraz jest tak, że ktoś był współpracownikiem. Nic nie zrobił i traci dostęp do sprawy.

**Łukasz Bott**: Zostaw tak jak ustawiłeś, tak. Z Piotrkiem będzie czuła tam.

**Damian Kamiński**: Dobra, jedziemy dalej. To jest Łukasz, twoje.

**Łukasz Bott**: Czekaj, no.

**Kamil Dubaniowski**: Znaczy, jeśli coś na przykład spada na deweloperów, że to on ma zaprojektować, bo ja nie jestem w stanie mu zaprojektować **Backendu** czy wymyślać sposobu, no to to może to jest jego zadanie sprintowe, tak, żeby zaprojektować tak jak tutaj ma Piotr, więc wtedy jak najbardziej ten **In Design** jest poprawny.

**Łukasz Bott**: Ale moment.

**Damian Kamiński**: Przepraszam. No.

**Łukasz Bott**: No tak i to i taka była intencja.

**Damian Kamiński**: No tak, tylko to nam będzie zaburzać raportowanie. Do tego zmierzam.

**Kamil Dubaniowski**: A że **effort**?

**Damian Kamiński**: Że to co mamy powiedzmy tutaj? Tutaj, czekaj, tutaj nie, tutaj **Analytics**, tak. Czyli tu będziemy mieli znowu, przyrastać będzie, a to nie spadnie. Jeśli się z tym godzimy, to OK. Pytanie tylko, czy to jest najlepsze rozwiązanie? Czy jednak? No właśnie, bo jeśli pracujemy na tej zakładce, na zakładce **"Assigned to Me"**, to pracujemy w sensie nieważne, na który to jest sprint, wszystko to jest przypisane do mnie. Deweloperzy powinni opiekować oczywiście sprint, ma jakiś tam priorytet.

**Kamil Dubaniowski**: Nie, właśnie, nie. Moim zdaniem powinni działać na sprintach, bo to, że mają jakieś zaległe zadania sprzed tam nie wiem, 10 miesięcy...

**Damian Kamiński**: No to trzeba je wywalić.

**Kamil Dubaniowski**: No to, to właśnie.

**Damian Kamiński**: Bo wtedy, bo na sprincie z kolei, no dobra, no. To co powiedziałeś, mogą działać na sprintach, ale wtedy nie mamy tego zestawienia, że tu nam ubywa, tylko potencjalnie przybywa, bo my coś projektujemy na kolejny sprint i dajemy w ramach tego "zrób nam do tego wytyczne", tak. I to nie spadnie. Chyba, że robimy coś takiego jak **taski**. A nie **PBI**, w sensie jakiś inny typ, który jest do projektowania. Bo może powinniśmy to po prostu inaczej oznaczać. No ale tu się nie da.

**Kamil Dubaniowski**: Nie wiem w sensie, no myślę, że nie ma co mnożyć bytów.

**Damian Kamiński**: Filtrować, nie.

**Kamil Dubaniowski**: No to będzie **Task** na projekt, a później **PBI**.

**Łukasz Bott**: Co z tymi **taskami**, to deweloperzy jakoś to sobie...

**Kamil Dubaniowski**: Tak, to, to, to też.

**Łukasz Bott**: Zarządzają, tak. Bo to jest bardziej wtedy związane chyba z właśnie z jakimiś tam **merge**'ami, **code review**'ami.

**Kamil Dubaniowski**: Ja bym zwrócił to na **Backlog**, mimo to, że to jest Piotra. I po prostu no Piotr wchodzi w skład tego naszego zespołu, który wybiera zadania i opisuje. On jest architektem, więc to de facto wszystkie te, gdzie są dla nas. No nierealne, jakieś właśnie architektoniczne, **Backendowe**. No to Piotrek to będzie robił. I będziemy przepisywać na sprinty. I to jest element poza sprintem.

**Damian Kamiński**: Według tak.

**Kamil Dubaniowski**: Tak. I powinniśmy teraz później, jak to skończymy, uporządkujemy ten zeszły sprint, to odpalić **Backlog**, wziąć wszystkie na etapie **In Design** i **Evaluating** i **Investigate**. No i nimi się zająć w pierwszej kolejności. Żeby zmieniły status na **Ready To Do**. To jest nasza pula na plan na kolejny sprint. Na ten i tak już nie zdążymy. Wszystkie mają szansę.

**Damian Kamiński**: No. To spokojnie według mnie to się, to nie jest tak, że my musimy teraz, wiecie, wywrócić stolik i już od jutra pracować według nowych wytycznych. Wiadomo, że mamy jakiś dług, więc musimy to ponadrabiać. Wystarczy, że będziemy to robić systematycznie i dojdziemy do celu.

**Kamil Dubaniowski**: Chyba, że w trakcie tak jeszcze możemy.

**Łukasz Bott**: Powoli zrobić.

**Damian Kamiński**: Do celu. Tutaj wielowymiarowe to jest nie tylko to na nas spoczywa, ale właśnie jeszcze te **efforty** i tak dalej. Więc na spokojnie dotrzemy się z tym. Dobra, no to znowu jest temat, który, ale ma priorytet wysoki, który po prostu trzeba zaopiekować, bo to...

**Łukasz Bott**: To jest temat.

**Damian Kamiński**: Musimy się na to przesiąść.

**Kamil Dubaniowski**: Czy to jest **New**?

**Damian Kamiński**: I to leci. Zobaczcie, 39 [sprint], a według mnie to było już przypięte.

**Kamil Dubaniowski**: Tak.

**Łukasz Bott**: Nie wiem, to kilka razy było, tak.

**Kamil Dubaniowski**: 29. Złoty.

**Damian Kamiński**: 25.

**Kamil Dubaniowski**: Naprawdę.

**Damian Kamiński**: 25, tak właśnie.

**Kamil Dubaniowski**: No przepinania moim zdaniem to tak musi się tym zająć, bo za chwilę będziemy po terminie. Mieliśmy zrobić przed czasem.

**Damian Kamiński**: W sensie mamy zrobić 41 [sprint]?

**Kamil Dubaniowski**: Tak i tutaj na razie tu zgodnie ze schematem, czyli nie ma tu co analizować, trzeba zrobić. Piotr to odkłada, się nie kończą.

**Łukasz Bott**: Najdłużej Piotrek powie, jeżeli nie jest w stanie tego zrobić w tym sprincie. To przetniemy na kolejny. To tam jeszcze troszkę pewien bufor mamy, tak. No ale czasowy.

**Damian Kamiński**: No dobra. A to jest priorytet 4. Podnośnik: "Dodaj możliwość sortowania po polu innym niż..."

**Łukasz Bott**: Jeżeli...

**Damian Kamiński**: To chyba...

**Łukasz Bott**: No ja wiem, wraca to.

**Damian Kamiński**: Czekaj, to jest do mnie?

**Kamil Dubaniowski**: Będę jadł w międzyczasie.

**Damian Kamiński**: A zadanie do wyceny. Dokładnie opisania, jakie powinno być, startującym jest zadanie. Terminu upłynął, poszło w wycenę.

**Łukasz Bott**: Warunków z klientem.

**Damian Kamiński**: Poszła wycena, no to...

**Łukasz Bott**: Ważności, czekaj, pokaż do tej ważności wyceny.

**Damian Kamiński**: W zasadzie poszła nas to trochę nie obchodzi. W sensie jest uzgadnianie warunków z klientem, więc to spada na **Backlog** i nie robimy.

**Łukasz Bott**: No tak, przyjdzie potwierdzenie, że chcą to robić i za jakąś tam kwotę, no to...

**Damian Kamiński**: Tylko czekaj, żeby to nie przepadło, czy tu jest podpięte? Co potem będziemy robić od nowa?

**Łukasz Bott**: Wiesz co? Bo to się zleceniu podpina dopiero.

**Damian Kamiński**: No ja wiem, tylko no właśnie to już wpisałeś. Czekaj, a to wrzucę, żeby tego potem nie robić. Gdzie to było tutaj? No dobra, to w takim razie to jest **Backlog**. W sumie zdejmujemy. Dobra. OK. Aktualizacja artykułu. Przypisane do Łukasza.

**Łukasz Bott**: Przewiń to dla mnie. Ten to jest jakaś tam pierdoła i tyle.

**Damian Kamiński**: No dobra.

**Kamil Dubaniowski**: Też nie wiem czy takie nasze zadanie tu powinny być, bo to też będzie teraz zakłamanie, bo dziewczyny nie będą tego testować. Też nie będziemy w stanie teraz przez takie zadanie oszacować ile jest tu testów. Więc my musimy sobie chyba gdzieś z boku takie rzeczy prowadzić.

**Damian Kamiński**: No do tego właśnie o to mi chodziło, że ten **Backlog** może powinien mieć coś co jest jeszcze dodatkowym jakimś tam komponentem. No zobaczymy, dobra.

**Michał Zwierzchowski**: Możecie coś wymyśleć, możemy to jakoś automatyzować. Te duże, nie wiem jak zmienicie na was, to gdzieś tam się będzie automatycznie przenosił, czy nie wiem na przykład jak jest na ten **Waiting for Information**. Jak mówicie, że nie musi być, nie powinien być w sprincie, to możemy jakoś automatycznie te sprinty usuwać. Więc nie wiem, powiadomienia na **Teams** możemy też wysyłać. Więc nie wiem, jak macie jakieś pomysły, to...

**Damian Kamiński**: No właśnie, już. No właśnie, to trzeba przełożyć na pomysły, tak jak mówisz i teraz mam pewien pomysł, tylko że my mamy te... Następne pytanie, czy chcemy te następne używać? Może powinniśmy w ramach **Backlogu** zrobić następne, bo to jest albo... albo korzystać z tego, no jak chcemy. Bo teraz mamy **Backlog**, gdzie będzie **Ready To Do**. Ale, chociaż nie, no my mamy też od razu już sprinty poplanowane do przodu. My możemy wpinać już na 50 [sprint].

**Kamil Dubaniowski**: Znaczy jak dla mnie te **Inbox** może kiedyś, następny to w ogóle, no nie tak to powinno działać. Jest **Backlog** i **Backlog** ma **Ready To Do** z jedynką, to znaczy, że to jest na najbliższy sprint. Z dwójką, trójką możemy się umówić, że to jest może na kolejny. Czwórka to jest w ogóle następny, albo może kiedyś, tak na tej zasadzie. I to jest na tej zasadzie podchodzić do tego, a nie i teraźniejszym zmieniać i **Backlog** status i priorytet.

**Damian Kamiński**: No dobra, ale to w takim razie my nie, nie powinniśmy robić coś takiego, że dzisiaj w planie możemy coś wrzucić już na 45 [sprint].

**Kamil Dubaniowski**: Tak, tak. O to chodzi. No właśnie o to mi chodzi, tak, że jak to jest, to jest właśnie to, może to jest to następne, tak. Że to my powinniśmy na etapie planowania, no następne to znaczy, kiedy za 10 sprintów czy za 5, nie. A może kiedyś, to znaczy za rok czy za 2 w ogóle to jest bez sensu. My powinniśmy planować sobie to na, nie wiem, perspektywę 3 najbliższych sprintów. No i wiadomo, że transparentnie będziemy podchodzić do tego, znowu, co mamy na ten sprint, czy w międzyczasie nie wpadło coś ważniejszego i to spadnie gdzieś dalej. No ale to też jest dla konsultantów informacja konkretna: zgłosiłem coś, jest na **Backlogu**, no i będzie realizowany. Nie wiem, za 3 sprinty. A nie, nie wiadomo kiedy.

**Damian Kamiński**: No tak, no to może właśnie na **Backlogu** powiedzmy wszystko co de facto ma jakiś priorytet pierwszy. To już to w zasadzie nie powinno być na **Backlogu**, nie jeśli jest. No tak, bo to jest dla nas pierwsza rzecz do zaplanowania na kolejny sprint. Dokładnie albo na kolejny, albo na jakieś, tak. Bo i to my powinniśmy określać, czy to jest jedynka, dwójka, na etapie właśnie tego **Evaluating**, tak. Czyli ktoś, kto z nas podejmuje z **New**, zmienia status na **Evaluating** i to znaczy, że sygnał dla nas wewnętrznie, że ktoś już się tym zadaniem zajmuje i ja nie mam potrzeby czytać tego zgłoszenia. Tak myślę, no a tamte statusy. Znaczy to i tak następne, może kiedyś tak jak mówię, to jest taki, możemy sobie kolejne dokładać. I to będzie dalej. To samo będziemy wiedzieli, co tak naprawdę, kiedy to będzie.

**Damian Kamiński**: To znowu to samo. Nie zapisałem sobie dobra. Umożliwić nadanie. Bo ja to rzuciłem, bo **Block**. No dobra, ale to na bank, czekajcie, już zgłupiałem. Jeszcze raz odpowiesz. Dobra. Tutaj jest **Waiting for Information**. Od kogo? Pytanie w komentarzu.

**Łukasz Bott**: Wiesz co, możemy to zignorować, bo to już jest naprawione.

**Damian Kamiński**: Rozkopywanie raportu, który mapuje się czy już tego nie ma?

**Łukasz Bott**: Nie ma chyba od tego problemu. Jak wróci, to musimy przywrócić. Zrób filmiki. A nie, weź tam odepnij tylko ani jeszcze starsze. Pytanie, nie wisiały.

**Damian Kamiński**: Dobra. Tylko, co powinniśmy tu według was robić?

**Kamil Dubaniowski**: Może dostać? No to nie podlega tam żadnym statystykom ani nic, więc...

**Łukasz Bott**: No tak.

**Damian Kamiński**: OK. No dobra, językowe aliasy.

**Łukasz Bott**: To jest grubsza sprawa. Możesz mi dać to na **In Design**. Na **In Design** to jest tak, jeżeli chodzi o te aliasy do funkcji **Reactowych**, to jest to zrobione. Natomiast daj mi to na **In Design**. Nie wiem, na ten, na ten sprint, tak? Czy nie wiem, nawet **Block**, tak byśmy się umówili, to na **Backlog**.

**Damian Kamiński**: No, że nasze jest nawet na **Backlogu**, tak?

**Łukasz Bott**: Dobra, to ja to będę musiał sobie zaprojektować i może gdzieś tam wrzucić.

**Damian Kamiński**: No bo...

**Łukasz Bott**: W tej chwili jak już tam...

**Damian Kamiński**: Prawda jest taka, że tego **In Design** na **Backlogu** możemy mieć sporo.

**Łukasz Bott**: No to będziemy mieć sporo. No to jest...

**Damian Kamiński**: I teraz pytanie, jak będziemy tym zarządzać priorytetem? Czy tu właśnie to, co powiedział Michał? Czy w ramach **Backlogu** chcemy to sobie też jakoś rozpisywać? Tu musimy się nad tym zastanowić.

**Łukasz Bott**: No dobra, no to nie, nie musimy teraz...

**Kamil Dubaniowski**: Zobaczymy skalę. Najpierw przeszliśmy.

**Damian Kamiński**: Czy chcemy? No właśnie, czy chcemy dodatkowo rozbijać? Dobra. No nie mówię, że w tym momencie, tylko mówię to, co tutaj można zdefiniować. Dobrze, przefiltrowana lista spraw. Wszystkie wyświetla również sprawy usunięte. No to to w ogóle jest jakiś **Hotfix**, jeśli to jest nieładnie. Tylko kto to? Ale to Łukasz sam zgłosił.

**Łukasz Bott**: To zauważyłem.

**Damian Kamiński**: A tylko to coś jest po wydaniu poprawki, należy sprawdzić do nowego. Gdzieś jest 2. Co to za numer? Aha, to jest numer OK. Tu jest brak informacji. Historia i usunięcie przywróceniu. No dobra, no to musisz to po prostu sprawdzić.

**Łukasz Bott**: Dobrze, czy na 41 [sprint]?

**Damian Kamiński**: Znaczy no ja bym to zostawił na tym, bo to jeśli ktoś wykryje, że dalej jest, no to powinien być **Hotfix** w mojej opinii.

**Łukasz Bott**: Oni to...

**Damian Kamiński**: Dobra. Zobacz dla: nazwa wyświetlana Kamil Dubaniowski. Obecna nazwa zobacz dla nie odzwierciedla celu opcji. Ale o czym zmiana nazwy funkcjonalności?

**Łukasz Bott**: W tym, zobacz dlaczego. Bo edytor, w tym nowym edytorze graficznym formularz.

**Damian Kamiński**: Nie wiem, o czym to wy mówicie. Dobra, chyba rozumiem, tutaj tak procesy.

**Łukasz Bott**: Było, wybierało się wersję językową.

**Kamil Dubaniowski**: Wychwalany.

**Łukasz Bott**: I było "Zobacz dla". No "Zobacz dla" to sugerowałoby jakąś osobę, a nie język, tak.

**Kamil Dubaniowski**: Czy naprawdę zrzućcie to na **Backlog**? Ja myślę, że to wpadnie jeszcze na ten sprint, bo to nie jest duży temat. Tam była sugestia, żeby to przeszło na flagę po prostu.

**Damian Kamiński**: Ja wrzucę tylko, żeby było wiadomo gdzie, bo takie pierwsze...

**Kamil Dubaniowski**: No ale to ja zgłaszałem sam sobie, więc ja powiedzmy kumam.

**Damian Kamiński**: Nie wiadomo było o co chodzi.

**Kamil Dubaniowski**: Tak, to do zastanowienia, jak my to chcemy. Ja wątpię, że to powiedziałem, że wejdzie, ale teraz przypominam sobie, co, co, co tam padło, jakie pomysły. Wątpię, że ruszymy w najbliższym sprincie, więc wrzucam na **Backlog**. Ja to zaplanuję sobie jeszcze raz, bo padła propozycja, żeby w ogóle zrobić dedykowany tryb, czyli jesteś w trybie edycji i tam nie ma żadnego przełączania się między językami. Pracujesz po prostu na nazwach systemowych, a jak teraz już sobie wszystko zaprojektowałeś i chcesz sprawdzić, jak będzie ten formularz wyglądał dla języka angielskiego, niemieckiego, to odpalasz dedykowany tryb podglądu formularza takiego realnego, gdzie te wszystkie pola po lewej ci znikają, bo są niepotrzebne. Prawy panel ci znika, bo jest niepotrzebne, bo to jest tylko właśnie do tego, żeby zweryfikować sobie, jak wygląda formularz w danym języku i czy wszystkie tłumaczenia są wprowadzone. A to nie jest moment, kiedy ty nadal ten formularz projektujesz, bo danie przełącznika w tym trybie...

**Damian Kamiński**: Bo wyszukiwanie mamy zaopiekowane, jeśli serwis to robi, tak, bo to też jest istotne, ale to już mamy, nie.

**Kamil Dubaniowski**: Wyszukiwanie pól po tak.

**Damian Kamiński**: Kontrol F, tak, żeby po dowolnej nazwie polskiej, angielskiej, francuskiej.

**Kamil Dubaniowski**: Tak, ale to jest dedykowany **Search**. To dzisiaj Przemek pokazywał już. Kontrolek nie działa, bo nie pokazujemy tych nazw. Ale **Search** zna te nazwy i wyszukuje po systemowych i tłumaczeniach.

**Damian Kamiński**: Mhm. No dobra, czyli to jest "Zobacz dla". Tak to może powinno być "Wersja językowa" albo...

**Kamil Dubaniowski**: Więc tak. No to co szerzej powiedziałem, bo to nadal jest mylące, nawet jak tutaj damy "Wersja językowa", to może być mylące. Co ja teraz ustawiam? Czy ja ustawiam nazwę systemową czy wyświetlaną? Bo tam w panelu edycji formularza można zmienić nazwę i teraz to "Zobacz dla" zmienia ci kontekst też edytowanych nazw i to jest bardzo mylące. A to "Zobacz dla" to tak naprawdę służy tylko do celów podejrzenia. Jak wygląda formularz w danym języku, nie powinno tego być? Moim zdaniem w trybie edycji. Zwróćmy to na **Backlog**. Nie jest to pilne na ten moment. Wymaga to przemyślenia, żeby to dobrze zaprojektować.

**Damian Kamiński**: Dobra. Integracja, **AMODIT**, **MERIDA**, analizy. To też jest temat, który Piotr miał zaopiekować, bo to jest ta. Stosuje `CallRest`, a **AMODIT** z reguły ręcznej wywołuje `CallRest` poniższym kodem. Docelowo ma uruchomić wskazana w punkcie `A` zamknięty. No to czy obsłużyć? Nie można wywołać funkcji, bo sprawa jest zamknięta. To jest funkcja, więc to Piotr powinien ogarnąć. W zasadzie **Ready To Do**. A jak nie Piotr, to w sumie Adrian to może ogarnąć, bo to też...

**Łukasz Bott**: `API`, wszelkie typy, to jest integracyjne rzeczy na raz, więc się też w tym orientuje.

**Damian Kamiński**: To już wszystko jest zdefiniowane. Mimo że w ogóle trzeba to przepiąć na Adriana, bo to jest...

**Łukasz Bott**: Łukasz Brocki też pewnie może zrobić, może Markowi, jakby chciał się oderwać od **Trust Center**.

**Damian Kamiński**: Czekaj, od razu to wyrzucę. Przepraszam. Dobra, 41 [sprint] mu znikło. Dobra, zapamiętywanie wyboru wariantu nazw wyświetlanych między zakładkami. Znowu twoje Kamil. Co ty wiesz?

**Kamil Dubaniowski**: To już w ogóle...

**Damian Kamiński**: ...k.

**Kamil Dubaniowski**: Wycofaliśmy się z tego, że to jest globalne ustawieniem, więc do wygrania.

**Damian Kamiński**: No i co? Jak to teraz wygląda? Ubywa, ale jeszcze. Ryzyka. Także 39 [sprint]. No dobra, to tak to to zostawiam w ogóle Łukaszowi. Nie podejmuję.

**Łukasz Bott**: Tak, wiesz co, ja to przegadam, przegadam z Anią, bo... No bo będzie trzeba to przypiąć, albo po prostu zaktualizujesz ten status.

**Damian Kamiński**: To chyba aha, bo nic nie napisałem.

**Kamil Dubaniowski**: Czy to chociaż zmieńmy, zmieńmy te statusy z **New**? Bo chciałbym, żeby...

**Damian Kamiński**: To jest.

**Kamil Dubaniowski**: Chociaż nie, nie zostaje na tym starym sprincie.

**Damian Kamiński**: Nie, to ja dam na **In Design** i szepnę na ten sprint. I to dla Filipa czy dla Przemka będzie można wrzucić.

**Michał Zwierzchowski**: To ja przyjmę teraz tylko **In Progress**, jeszcze **In Progress** i **Ready To Do** na na obecne, OK.

**Damian Kamiński**: Bo to jest jakaś drobnica?

**Kamil Dubaniowski**: To nam... Jeszcze raz, Michał.

**Michał Zwierzchowski**: Mówię, że ja przeniosę. Jeszcze nie zostały **In Progress** i **Ready To Do**, to przenieść na ten obecny też.

**Kamil Dubaniowski**: Tak, tak, tak, chociaż **Ready To Do** ja bym przejrzał też, no bo...

**Damian Kamiński**: Dobra, dam.

**Michał Zwierzchowski**: Dobra, bo właśnie. A dobra, no to **Ready To Do** wam zostawiam.

**Kamil Dubaniowski**: Tak, tak bym robił w sensie schematu, że przenosimy tylko to co zaczęte **In Progress** automatu.

**Damian Kamiński**: Czekaj, czekaj, czekaj, nic nie zostało. Tu ja mam wszystko, nie ma. A **Ready To Do**, OK, jedno.

**Michał Zwierzchowski**: Więcej trzeba.

**Damian Kamiński**: Nie, no jak... Odśwież. Bo już to zobacz, ile czyściliśmy przed chwilą. Ja tylko mam po tym filtrowane. **Block** został w zasadzie jedno **Ready To Do**, 2. Przepraszam, 2.

**Michał Zwierzchowski**: A miała dobra, tak.

**Łukasz Bott**: 2, 2, no ale to...

**Michał Zwierzchowski**: Nie, no 2, 2. Dobra, ja mam. Ja mam 3, bo jeden mi to pokazuje. Także to dlatego.

**Damian Kamiński**: OK. To, to w zasadzie przypinamy po prostu tak. Czy nie? Nie wiem co tu **Performance Monitor**, **Statystyk**. Mamy to analizować czy przypiąć?

**Łukasz Bott**: Tak, tak, tak, tak. Przypiąć, przypnij już to na pewno jest.

**Damian Kamiński**: Dobra. Tutaj mamy pole **Hyperlink**, pole linku do strony w trybie odczytu.

**Łukasz Bott**: To jest. Moja widzę, że nie podjęła tego. Nie jest to pilne, pierdołka. Jeżeli chodzi o to, że jak mamy pole typu link. I ten link jest, ma bardzo długi tekst, tak to w trybie do odczytu to jest odcinany. Tak, nie widzisz go, dopóki sobie nie klikniesz w wadze, a warto było go wyświetlić w pełni, tak. Czyli dobrze by było, gdyby to pole się wizualnie. No załamało tak gdzieś ten link i tam się nawet tu takim wężykiem przez kilka linii jak się pociągnął, tak. Tak jak masz tutaj właśnie.

**Kamil Dubaniowski**: No pytanie, czy to jest kluczowe do teraz? Jest jedynie ta jedynka, aktualnie działa jedynka, tak.

**Łukasz Bott**: To nie, nie jest kluczowe, to zauważyłem jako tam słucham.

**Kamil Dubaniowski**: Aktualnie wygląda to jak w jedynce, no to ja nie wiem czy jest.

**Damian Kamiński**: Tak, jedynka, tak, tak, tak. Zdejmujemy. Zdejmujemy z Anny **Ready To Do**, leci na **Backlog**, priorytet 3.

**Kamil Dubaniowski**: Ja bym nawet nie dyskutował, czy nie mów. Bo mi się podoba pierwsza opcja bardziej. Po co mi cały link? Ja po pozostałych kolumnach powinienem wiedzieć w.

**Łukasz Bott**: Zaniedbania. Dobra, wiesz co?

**Damian Kamiński**: Ale może powinien być **Tooltip**.

**Kamil Dubaniowski**: W **Tooltipie** to się sprawdziło.

**Łukasz Bott**: Albo, albo tu, tu, tu mi się wyświetlasz w pełni, tak, ten link i tyle.

**Damian Kamiński**: To jest **In Design**.

**Łukasz Bott**: **In Design**. Nie jest to krytyczne, bo to mi wyszło. Czekaliście z **Suite** jako taki tam? Nie bo nie blokuje mi to żadnej roboty, więc...

**Kamil Dubaniowski**: Ja też jeszcze patrząc na. Nie wiem, jak działacie ze zgłoszeniami, ale mi to dużo usprawnia. W tym momencie ja nie zaczynam pisać zgłoszenia na **Azure**, ja piszę zgłoszenie do czata przez **ChatGPT**. Tak jak ja bym to opisał na **Azure**, a on mi rozpisuje do tego kryteria akceptacji, kroki i w większości wypadków nie dużo edytuję. Nawet w większości przypadków kopiuję. I trzeba moim zdaniem napisać jakiegoś lepszego **prompta** pod to i dać to konsultantom, bo...

**Damian Kamiński**: Ja też tak robię.

**Kamil Dubaniowski**: I dziewczyny nie będą miały już tego problemu, jak konsultant wrzuci do **GPT**, dostanie wynik już ze wszystkim i będzie zadaniem tylko przeczytać i zweryfikować, czy dobrze opisał kroki i czy dobrze opisał kryteria akceptacji. No to będą tworzyć pełne zgłoszenia. Teraz jak jest, ja, ja sam tego nie robiłem.

**Michał Zwierzchowski**: No to to to było dobre a propos tych **promptów** do testowania, bo ja już tam siedzi teraz jeszcze nad tym **Playwright** i takim **frameworkiem** do testów. Ja też będę się tym zajmował i generalnie ostatnio też siedziałem i zrobiłem coś takiego, że no tego to na razie tak testowo, że mi, że mogę pobierać sobie **prompt** ze zgłoszenia w **DevOpsie**, no i wtedy też wygenerować test do tego. Więc byłoby super, jakby było pisane. Czytam w kryteria akceptacji, czy oddzielne pole byśmy to dali **prompt**.

**Łukasz Bott**: No.

**Michał Zwierzchowski**: Czy tam, no już mniejsza z tym, jakby się to nazywało, żeby z tego można było pobrać, na podstawie tego można próbować też automatycznie wygenerować testy.

**Damian Kamiński**: To jest temat, który my poruszaliśmy. Wtedy nie było Adriana i nie wiadomo czy do tego nie... Chociaż tutaj ładnie opisał to Adrian, Mateusz.

**Kamil Dubaniowski**: Dla mnie to, to jest, no teraz, bo to jest do czerwcowej i to w ramach nawet **Hotfixa**.

**Damian Kamiński**: No tak, to jest na pewno. Ja się zgadzam, że nawet jako **Hotfix** to nie jest **PBI**, to jest to, co robimy z tego **Hotfix**.

**Łukasz Bott**: Nie, czy dlaczego **Hotfix**?

**Kamil Dubaniowski**: Bo wysypie się stara integracja. Znaczy nie wysypie, ale wizualnie może się wydawać, jakby coś zniknęło i się usunęło.

**Damian Kamiński**: No bo zobacz, co się dzieje. OK.

**Łukasz Bott**: A, OK, dobra, dobra, dobra, dobra. Ja myślałem, że to jest dopiero jakaś faza wdrożenia.

**Kamil Dubaniowski**: Bo bo...

**Damian Kamiński**: Nie, no **Hotfix**, **Hotfix**, bo to jest totalnie. Nie to, co powinno być, to wprowadza takie zamieszanie, żeby my sami na początku nie wiedzieliśmy, o co chodzi, a klienci, jak na to spojrzą, to już w ogóle za głowę się złapią.

**Kamil Dubaniowski**: Myślę, że to nawet jutro na Radę wypadałoby omówić, żeby Adrian też to uzasadnił, jak on to widzi i dlaczego tak zrobił.

**Łukasz Bott**: Oznacz na Radę tam.

**Damian Kamiński**: Dobra Rada. OK. To jest mój chyba, tak.

**Damian Kamiński**: To, to już jest **In Progress**, ale weźmy na 41 [sprint]. To jest tylko, żeby opis się wyświetlał. Bo dzisiaj tego nie mamy. Dobra, OK. Teraz zostały już tematy Łukaszowi, jeszcze 3 Kamilowi.

**Łukasz Bott**: Reszta jest moja.

**Damian Kamiński**: Wycofanie edycji pól w podglądzie formularza. W sensie pytanie, czy mamy to omawiać, przypinać?

**Kamil Dubaniowski**: Nie, to moim zdaniem są wszystkie. Energy. To, ale przejdźmy, jak już masz to odpalone, żeby mnie szukał. To jest do wywalenia na pewno.

**Damian Kamiński**: A to co? Tylko widzisz, tu jeden błąd popełniłeś, że powinno być tak. I wtedy ci się to ładnie zrobi z **checkboxami**, ale coś tu się nie zrobiło.

**Kamil Dubaniowski**: Nie, no to są **checkboxy** typu. Ten typ wygenerował grafiki. Już nie bawię edycja. Znowu jak sklejałem bez formatowania, no to mi wywala wszystko razem z tam z kropkami z punktami. Dlatego mówię, porządny **prompt**, tak żeby on nie używał tak.

**Damian Kamiński**: Grafiki, OK. Powinno być ładnie, napisał **Markdown** tak. Dobra, usuń, tak.

**Kamil Dubaniowski**: Tak.

**Damian Kamiński**: To ułatwiona nazwa edycja nazwy systemowej. Po dodaniu nowego pola. Żeby się ustawiało od razu tak, po dodaniu pola.

**Kamil Dubaniowski**: To zostaw w sensie zgodnym **Backlog**. Ja to piszę lepiej, bo to zmienia nieco się zasada, czyli teraz, po dodaniu nowego pola po prostu **input** ma stać. A ja tu opisałem, że w prawym panelu i to na kopiowanie nazwy tego już nie mamy. W ogóle. Czekaj, czekaj.

**Damian Kamiński**: Kopiowanie nazwy systemowej w **tagu** w **tagu**.

**Kamil Dubaniowski**: Nie mamy już tych tagów, bo teraz po prostu wyświetla się nazwa systemowa tak jak było.

**Damian Kamiński**: Ale ustawienia systemowe, tak. Ustawienia nie, to jest edytor formularza.

**Kamil Dubaniowski**: Nazwa systemowa pola tam, no wycofaliśmy się z tego projektu. To była ta zmiana co tak na szybko ją wrzuciłem. Z powodu uwag Przemka Sołdackiego, tak. To i tego już nie ma. Nie ma tych, bo po prostu teraz nazwa systemowa jest w jako "Zobacz dla" i oglądasz nazwę systemową. I to są jedyne nazwy. Ja wywaliłem te tagi, bo w układzie 3, 4 kolumnowym po prostu nie było miejsca, żeby wyświetlać nazwę wyświetlaną w systemową i 4 kolumny. W dodatku, więc teraz już tych tagów nie wyświetlamy.

**Damian Kamiński**: Czyli to tak. No ale to w sensie no tylko jedną rzecz sprawdzić, czy da się zaznaczać, bo tu jak próbowałem zaznaczyć to się przesuwało pole.

**Kamil Dubaniowski**: Dlatego ja to dałem chyba **Evaluating**, żeby po prostu dodać to do prawego panelu. Albo na **hover** na tych systemowych nazwach.

**Damian Kamiński**: OK.

**Kamil Dubaniowski**: Obok, więc w sumie jakby to przynajmniej zrobić, to będzie trudne. Ale zobaczymy, jak jest teraz, bo nie pamiętam. Czyli tu jest edycja, no.

**Damian Kamiński**: A to tak ma być?

**Kamil Dubaniowski**: No właśnie o to chodzi z tym.

**Damian Kamiński**: Rzecznika.

**Kamil Dubaniowski**: Nie.

**Damian Kamiński**: W sensie co my mamy systemowo edytuj? No to ten tekst powinien zostać tak.

**Kamil Dubaniowski**: Do poprawki.

**Damian Kamiński**: Tylko w ogóle nie mogę tu pisać, więc może on nad tym pracuje. Jeszcze wiesz, bo nie mogę nic, a tu zobacz, co się dzieje. Jedną literkę mogę wpisać.

**Kamil Dubaniowski**: Dobra, no to coś Przemek rozgrzebany ma, ale tak, czyli jako czytuję z edycja. No to kopiowanie moim zdaniem. No już nie, chyba, że to będzie tak, że na wjeżdżasz na dane pole.

**Damian Kamiński**: No dobra, ale tylko czekaj. Robię `Ctrl+S`, i mi się oślizguje palec i daje `Ctrl+C`. I co? Jako `Ctrl+Z` nie działa i już nie wiem jak to się nazywało i wszystkie reguły poszły w...

**Kamil Dubaniowski**: Czy tutaj tak, nie, nie, nie zabezpieczamy i tego? No bo nawet jak tu będzie ikonka do kopiowania, to i tak ktoś może chcieć użyć `Ctrl+C`.

**Damian Kamiński**: Nie, pytanie, czy to nie powinniśmy odblokowywać do edycji?

**Kamil Dubaniowski**: Myślę, że chcesz do edycji, tak?

**Damian Kamiński**: No bo teraz, no w sensie nie mamy żadnego zabezpieczenia, tak jak tam, że walidujemy reguły.

**Kamil Dubaniowski**: Może tak być? Dobra, nie ma, nie ma co. Daje mi to na **Evaluating**. Ja przejrzę całą ścieżkę, ale tak mogłoby być, że jest domyślnie po dodaniu już zablokowana. Jak chcesz edytować, to masz. **Edit** i tak samo też na edytorze dwuklik nie działa, tylko jak najedziesz na nazwę pola, no to mogą ci wyskoczyć właśnie ikonka do kopiowania albo ołówek do edycji. Jak klikniesz ten ołówek, to wtedy tu w tym miejscu dopiero ci otworzy tak tego pola. No do przemyślenia. Wróć to jak się uda i Przemek będzie miał przestrzeń, to jeszcze to dorzucę do bieżącego sprintu, ale trzeba to przemyśleć.

**Damian Kamiński**: Wpisać.

**Kamil Dubaniowski**: Możesz dodać, że tu jest więcej do analizy, czyli... Czy tam jest walidacja mimo wszystko, czyli nie pozwoli ci tak łatwo zmienić nazwy, która jest użyta w kodzie reguł, bo to zostało. Ekspert, bo wiesz to to wyskoczy komunikat, dlatego mówię, no nie ma co, trzeba przemyśleć sens.

**Damian Kamiński**: OK. No tylko, że jeszcze trzeba pamiętać o tym, że raporty, tak. Czy to a nie w raportach jest chyba odniesienie po `varchar`, czy nie, chyba tak?

**Kamil Dubaniowski**: Powinny nadpisać, tak. Jedyna, jedyne ryzyko to są reguły i tam była ta walidacja.

**Damian Kamiński**: Albo reguły innych procesów, tak, które nie są walidowane.

**Kamil Dubaniowski**: Tak, bo on nie jest w stanie niekiedy zmienić, tak. I daje ci wtedy sygnał, że nie udało mu się zmienić i tam... Jeszcze raz czy podpisujesz?

**Damian Kamiński**: No zwłaszcza jak rejestr, gdzie coś pobierasz z innego. Tu według mnie też chyba powinien być wyższy priorytet. Najpierw ołówek, wtedy się odblokowuje. Jak wprowadzisz poprawkę, gdzieś klikniesz, to znowu jest zabezpieczone.

**Kamil Dubaniowski**: Wiesz co? Co jeszcze by mi się wydaje, że trzeba było zrobić w tym sprincie, a nie zaplanowaliśmy to, co tobie dzisiaj wyszło w edytorze reguł? Niestety to jest taka konsekwencja robienia na raty, ale żeby nie było takiej sytuacji jak ty miałeś, że ktoś napisze i to będę. Pewnie ja, znając moje szczęście, że ja napiszę kodu ze 100 linii i trafię w lewe menu i mnie wywali całą regułę.

**Damian Kamiński**: Meno.

**Kamil Dubaniowski**: Myślę, że to trzeba zrobić do czerwcowej, nawet jeszcze, że powinno wykryć, że ma niezapisane zmiany.

**Damian Kamiński**: Tu, zobacz. Pokażę tak. Łukaszowi piszesz regułę, tak? Kamil powiedział 100 linii. I potem zaznaczam 2 pierwsze linijki. Tylko ustawienia przyszedłem i poszło.

**Kamil Dubaniowski**: Przez przypadek, nie? I to Damian. Takiego miss-klika zrobił dzisiaj, bo chciał coś zaznaczyć i mu uciekł kursor i się przełączył. Nie ma żadnego komunikatu, że masz niezapisane zmiany.

**Łukasz Bott**: To niezły.

**Kamil Dubaniowski**: Nie wiem, czy to będzie w ogóle wykonalne, no ale...

**Damian Kamiński**: Ja nie wiem, czy my powinniśmy w tym trybie pozostawiać to. Może nie.

**Kamil Dubaniowski**: Może tak być? Wiesz, no?

**Damian Kamiński**: Przechodzimy tu już w ekran, ten konkretny, nie.

**Kamil Dubaniowski**: Bo tracimy miejsce też, które do tej pory było. A kod?

**Damian Kamiński**: Raczej tak powinno być, że ten ekran jest pełnym ekranem, ale to... No właśnie, jak to zrobić przejściowo dobrze, tak chociaż. Bo tu znowu to kasujemy ramę, która ma być wszędzie. A może po prostu nie wiem, może trzeba na nią nałożyć tutaj jakąś maskę, wyższą na razie. Chociaż pytanie też, jak ma być docelowo? Nie, no. Nie wiem, przyznam szczerze, że to jest potrzebne. Kredytujemy regułę, chyba nie.

**Kamil Dubaniowski**: Znaczy jedynie w tym kontekście mi się to podoba, że łatwo teraz mogę w drugiej karcie otworzyć sobie formularz i tam weryfikować na przykład, jak pola się nazywają albo etapy.

**Damian Kamiński**: No tak, to jest. To może być wygodne, no i.

**Kamil Dubaniowski**: I mam tam. A teraz musiałbym wyjść z edycji, otworzyć w nowej karcie, albo gdzieś tam w przeglądarce wręcz wpisać na nowy adres. To mi się podoba. Jedynie tej walidacji nie zawiera zmian tych reguły. No i to będzie wszędzie, nie? Bo ja tak samo mogę. Chociaż inne, inne miejsca zapisują zmiany chyba od razu.

**Damian Kamiński**: Na innych miejscach nie stracisz. No właśnie, no właśnie. Znaczy i też nie pracujesz przy lewej krawędzi. A tu jednak właśnie przy, zwłaszcza przy zaznaczaniu czegoś, pracujesz. Bo na formularzu pracujesz na prawej krawędzi ekranu, tak? Jak ktoś zmieniasz?

**Kamil Dubaniowski**: A spróbuj teraz dopisać linię kodu jeszcze i...

**Damian Kamiński**: O żesz, kliknąłem tylko Enter. I mnie przerzuciło. To ciekawe. Przy `Ctrl+Enter` kliknąłem poprzednio, a czemu? Bo tu byłem. Nie wiem, co tu się stało, szczerze.

**Kamil Dubaniowski**: Weź kliknij na reguły jeszcze raz.

**Damian Kamiński**: O widzisz, jak już widzę, jak tutaj po...

**Kamil Dubaniowski**: Nie wejdziesz do...

**Damian Kamiński**: Tak jakby, o, jak zrobię chyba tak, że zaznaczam, a skończę tu, to teraz klikam Shift+Enter. Teraz jest git, dobra, ale jak tu sobie coś... Bo tak przesunę. I teraz to mnie tu przerzuca. No nie wiem, ryzykowne.

**Kamil Dubaniowski**: Zdaniem to jest cel tego tego kwartału.

**Damian Kamiński**: Ryzykowne, a może w regułach powinno być. Może tu powinniśmy mieć, jak już tu jesteś? Może tu jeszcze jakaś przestrzeń na górze? Zobacz pola. Może powinna być wręcz lista pól docelowo.

**Łukasz Bott**: Już masz na dole, "Wstaw pole".

**Kamil Dubaniowski**: No, jest to "Wstaw pole" na dole. To chodzi, że z tego nikt nie korzysta.

**Łukasz Bott**: Jak z niego korzysta?

**Kamil Dubaniowski**: Znaczy, no widzisz, ja rzadko. Ja wolę iść do formularza.

**Damian Kamiński**: Tego nie skorzystałem.

**Kamil Dubaniowski**: Walidować formularza, bo...

**Łukasz Bott**: Ja, ja, ja czasami korzystam. Jak mam duży formularz, to korzystam z tego, jak nie pamiętam.

**Damian Kamiński**: No dobrze i teraz powiedziałbym tak: może to, no właśnie ci łatwiej na formularzu. A teraz może to "Wstaw pole" powinno mieć taki sam kontekst jak to.

**Kamil Dubaniowski**: Mi łatwiej na formularzu. Zobaczymy, już nie należy. Szukaj pola, bo dzięki temu ja mogę je sobie znaleźć po polsku. Znaczy, wydaje mi się, że po prostu w kodzie reguł jakby wstawić kwadratowe nawiasy, to to już powinno mi takie search pola załadować.

**Łukasz Bott**: No przecież jak wstawisz, no zacznij tylko systemowo pisać.

**Kamil Dubaniowski**: Tu i to już w tym momencie.

**Damian Kamiński**: No ale też są, też jest to. A że wtedy już tylko po polach, tak.

**Kamil Dubaniowski**: Ale on też podpowiada funkcje niepotrzebne, no.

**Damian Kamiński**: No ja tylko tak korzystam.

**Łukasz Bott**: Nie, no ja też tak w większości przypadków, ale czasami przyznam się, że to "Wstaw pole" jest już kiedy on...

**Damian Kamiński**: Bo nie pamiętasz po prostu nazwy, nie? I to wtedy może być wygodne.

**Łukasz Bott**: Tak nie wiesz, wiesz jeszcze kiedy? Jak edytujesz reguły tabeli, a potrzebujesz pole z formularza głównego i chyba niekoniecznie **IntelliSense** ten podpowiadasz w kodzie, bo on działa chyba w kontekście w tym momencie reguły tabeli.

**Kamil Dubaniowski**: Tabeli i pól tabeli.

**Łukasz Bott**: I pól tabeli, więc nie podpowie ci pola z formularza czynnego. I wtedy tutaj to jest jedno miejsce, kiedy używam. A drugie miejsce to jest jak masz być. Wyszedł z tego, z tej części edytora reguły na tym głównym oknie edytora. Reguły masz tam warunek, no i tam wiesz, tam nie ma **IntelliSense** w tym warunku, no i musisz tam wstawić pole, nie.

**Damian Kamiński**: To jest kolejny. Ja nigdy tu nie piszę. To jest bez sensu. To powinno być tak, że ja piszę, tu robię i dopiero wracam, więc to musimy zrobić tak samo. Po kliknięciu tu powinno się otworzyć to samo okno. To jest bezsens.

**Łukasz Bott**: Ja wiem, że robisz tak, że wchodzi, sprzeda akcje. Piszesz tutaj sobie warunek dokładnie, tak. Tak, to to, to, to takie edytor powinien się otworzyć dokładnie.

**Damian Kamiński**: Tak, tak jak tu się otwiera, tak samo tu musi się zacząć otwierać edytor, bo i tak potem każdy wchodzi tu, żeby stworzyć, skopiować, wrócić tu i wkleić, no.

**Łukasz Bott**: Tak i trzeba to. No wiesz, tak tylko tam. No nie, no dobra, no.

**Kamil Dubaniowski**: Czy wiecie, to w ogóle mógłby być pełnoprawny taki edytor, gdzie ja wchodzę w jedno okno i mam tam wszystko. Jest osobno sekcja na warunek, warunek przy regułami, później kod. To jest w ramach jednego okna edycji. Ja piszę sobie wszystko na raz. Teraz zrobiliśmy 3 osobne i wpinamy wszystko. W sumie czemu też mogę być rozbudowany warunek, który nawet mi się tu nie zmieści, wstałeś?

**Damian Kamiński**: Znaczy, masz na myśli, że...

**Kamil Dubaniowski**: Tutaj tak tu i są 3 sekcje wydzielone. Tak ona jak widzę, że nie ma, no bo wtedy mam pełen kontekst. Spodziewam się, że często jest tak, że muszę wyjść stąd, żeby zobaczyć warunek. Czy ja przypadkiem nie piszę teraz z tego samego warunku, który już mam w ogóle na wykonanie reguły?

**Damian Kamiński**: A no to w sensie tu.

**Łukasz Bott**: Dokładnie.

**Damian Kamiński**: No OK, no to może i ma szansę. W sensie to też łatwo można zrobić, bo można wprowadzić tu zakładki, czy nie?

**Łukasz Bott**: No dokładnie, też tak właśnie.

**Damian Kamiński**: Tu jest na to przestrzeń. Że mamy wykonaj warunek wykonania przed regułą i główna reguła. Czy jak mówisz?

**Kamil Dubaniowski**: Znaczy w ten sposób, albo wręcz nawet ten tekst. Znaczy, ja nie wiem, nie wiem, no bo to jest jakaś gotowa biblioteka. Pewnie tak się nie da, ale widziałbym tak, że to są 3, ale takie bloki, kody po prostu i z jakimś nagłówkiem. Takie jakby nasze sekcje, tak na formularzu, że masz sekcję z warunkiem, sekcję.

**Łukasz Bott**: Albo tak, albo. Wiesz co, tak mogło mogłoby, mogłyby być jakimś tam. To mógłby być specjalny jakiś znacznik w ramach komentarza.

**Damian Kamiński**: No ale.

**Kamil Dubaniowski**: Kodem. Ty masz jak.

**Łukasz Bott**: Że rozpoczynasz właśnie, czyli wpisujesz na przykład `/comment`, ale tutaj podajesz na przykład, nie wiem, `CaseCondition`, tak. I on już wie, że od tego od następnej linii w dół leci warunek. Tam trzeba było też jeszcze troszeczkę. Niestety, ale zmienić ten interpreter, bo zauważ, że w warunku nie wpisujesz `if` coś tam. To wpisujesz tylko wnętrze `if`a.

**Kamil Dubaniowski**: Tak, a to o właśnie może tak powinno być tak, że wręcz widzisz ten schemat i już masz gotowca w tym bloku z warunkiem i tylko piszesz wnętrze tego. Się nie da usunąć. Po prostu jakiś jest pusty, no to warunku nie ma. Jak chcesz jakiś warunek, to sobie tam go edytujesz, a ten `if` jest taki już zabezpieczony, nie do usunięcia.

**Damian Kamiński**: No i dlatego pewnie po prostu to nie ma tamtej perspektywy, bo właśnie jestem wewnątrz.

**Łukasz Bott**: Tak, także.

**Kamil Dubaniowski**: No dobra, to to jest jakby zajmie.

**Damian Kamiński**: Ale tutaj wpisanie `if`a też nie jest problemem, bo jak zrobisz tak? I zrobisz `1 == 0`? No to to co to to to wyjdzie wynik `false`. Więc warunek będzie też `false`. Czy to tak się nie zadziało?

**Kamil Dubaniowski**: On nie, nie przyjmie ci w ogóle tego `if`.

**Łukasz Bott**: Nie. Nie, moim zdaniem, jest błąd składniowy.

**Kamil Dubaniowski**: No tutaj tak.

**Damian Kamiński**: Ale czekaj, bo tu nie ma, bo tu jest.

**Łukasz Bott**: Nie, no `if` wpisałeś. Nie dopuszczasz `if`a, tak mi.

**Damian Kamiński**: Nie przyjmie, dobra.

**Łukasz Bott**: I przyjmie.

**Kamil Dubaniowski**: Dobra, ale tak jak mówię, to już jest raczej nie na najbliższy sprint. Wydaje mi się, że teraz można się już rozłączać i powinniśmy z **Backlogu** przejrzeć te, co są do nas przypisane już imiennie na **In Design**.

**Łukasz Bott**: Tak.

**Kamil Dubaniowski**: Albo na etapie **Evaluating** albo **Investigate** i te zdecydować, co z nimi dalej. I jak nie chcemy na ten sprint, to po prostu możemy sobie zostawić na potem. A co chcemy na ten sprint, to powinniśmy zrobić to **Investigate** czy tam **Evaluate** i wpisać na bieżący sprint już ze statusem **Ready To Do**, jak tylko to.

**Łukasz Bott**: Tak albo na kolejny, tak.

**Kamil Dubaniowski**: Albo na kolejnym z planem. I wydaje mi się, że teraz nasze zadanie to powinno być w ogóle takie przeglądy codzienne, żebyśmy sobie nie robili zaległości. Wszystko co wpada na **New** dzielimy się tym rano. Kto bierze co na **Investigate**? Opisujemy, uzasadniamy, czy to jest sensowne, czy nie i planujemy na bieżąco, bo takie raz w tygodniu spotkanie 3 godziny to nie wyrobimy się.

**Damian Kamiński**: Nie wyrobimy, jesteśmy zmęczeni. No teraz po tych 2 godzinach gadania o tym to mi już też głowa spuchła. Potrzebuję 5 minut.

**Łukasz Bott**: Dobra, nie, no kończę.

**Kamil Dubaniowski**: Ale no, jakby patrząc na to, że **Daily** zaczynamy o dziewiątej, to my możemy zaczynać o dziewiątej. 20 minut na zgłoszenia z poprzedniego dnia. Myślę, że to jest, żeby przejść każde i przypisać. Nie mówię, że omówić, tylko przypisać, żeby każdy wiedział, że to jest moje i ja muszę zrobić to śledztwo, czy ja muszę ocenić, czy to jest zasadne, czy w ogóle chcemy to robić.

**Łukasz Bott**: Tak, tak. Dokładnie.

**Damian Kamiński**: Albo powiedzieć, że wczorajszy temat był dla nas właśnie jakiś tam. Nie wyrobiliśmy się i się podzielić na nowo, tak? Bo ktoś skończył, a tu jest jakieś nowe, tak?

**Kamil Dubaniowski**: Bo i o to właśnie chodzi, tak. My siedzimy te tam 20 minut wcześniej. Ja robię wpisy. I ja wiem, że to jest ważne dla Przemka do statystyki, ale niekoniecznie jakoś wpływa na naszą pracę. A my wtedy możemy też zareagować i powiedzieć: "wpadł **Hotfix**". Tak, już wiemy o tym. A teraz Łukasz robi te przeglądy między innymi, tylko chyba on tak. I to Łukasz tam podbija. I tak możemy od razu to na **Hotfix** powiedzieć, że dzisiaj Ania zmień sobie plany, przypisaliśmy **Hotfix**. Nie, że kto weźmie ten **Hotfix**, tylko: "Ania, miałeś dzisiaj niepełny plan na dzień? Masz kod."

**Łukasz Bott**: No tak. Dobrze.

**Michał Zwierzchowski**: To tak chyba można jakoś zautomatyzować i dodać ten, spróbować, że jak się pojawi nowy, to żeby z **Teams** od razu powiadomienie bez spamu na tą grupę.

**Damian Kamiński**: To tu też patrzcie, to jest ciekawe. Dopiero to skumałem. Patrzyliśmy na te... Fajnie będzie wyglądać tu gdzieś. Oj, dopiero teraz jak sobie damy odległą datę, to się okaże tak naprawdę, kiedy z tego sprintu spadły zadania.

**Kamil Dubaniowski**: Ja sobie dzisiaj, o, i tak to wyglądało, że sprint się skończył tu. No bo potem tu spadły zadania, bo przyszedł poniedziałek. Potem był kolejny sprint, znowu spadły zadania zaległe jeszcze sprzed 2. No i zostało 8, tak. Bo tak patrzyłem teraz na ten bieżący, który czyściliśmy. No i coś mi nie pasowało, że tu wyczyściliśmy wszystko, a tu jeszcze brakuje 64. Tylko, że dlatego, że tutaj ten wykres, że skończył się w piątek, a dopiero jak dołożymy dalej, to tu widzimy, że w poniedziałek już mamy zero. Dobra, no według mnie mamy dobry kierunek. Trzeba go tylko utrzymać i usprawniać. Jakoś to nam zacznie grać.

**Łukasz Bott**: Dokładnie.

**Damian Kamiński**: Dobra, w sumie jeszcze co? Pop... Można jeszcze spojrzeć na to, na to...

**Kamil Dubaniowski**: No to do decyzji, tak. Kiedy, no bo...

**Damian Kamiński**: Tak, przegrałeś już. No to tu Filip ma bardzo dużo, ale na `Analytics` ma bardzo dużo. To trzeba go może tam popchnąć.

**Kamil Dubaniowski**: To tak naprawdę dziewczyny, no bardzo dużo.

**Damian Kamiński**: Albo to jest na testach. OK, no tylko, że jest przypisane chyba do niego, tak. To nie Filipa. To jest **Assigned To**.

**Kamil Dubaniowski**: Tak, ale tam jest osobne pole na testerów, więc zadanie jest Filipa. No bo on robił jako deweloper. Można by zdjąć z nim tematy właśnie i które są. No to jest taki zrobić wręcz osobny, żebyśmy wiedzieli ile dziewczyny mają do testów, czyli ile na ten sprint jest już zadań gotowych do testów?

**Damian Kamiński**: OK. Jasne. No to z prawej strony.

**Kamil Dubaniowski**: No, no to tak, to tak.

**Damian Kamiński**: I drugi, co jest jeszcze?

**Łukasz Bott**: Jeżeli to jest, można samą **Jirą**, jest, no więc.

**Kamil Dubaniowski**: No to ja bym to zdjął z tego po lewej te statusy. Wyobrażam.

**Damian Kamiński**: Oj, widzisz. W sensie jeszcze raz?

**Kamil Dubaniowski**: Z deweloperów, bo to nie jest realne. W sensie nie widzimy faktycznie, ile oni mają tych zadań. Zdjąłbym status **Waiting for Pre-Test**.

**Łukasz Bott**: Tak.

**Kamil Dubaniowski**: Ee, `Registers`. OK.

**Damian Kamiński**: Tu chyba mogę tylko wyświetlać wyniki, a z racji, że ja wziąłem na sprint **PBI** i **Assigned To**, to trzeba było robić dedykowane zapytanie pod to i wtedy tak. No dlatego dodałem te kolory właśnie, bo też miałem takie poczucie, że to, co mówisz, że potem nie wiadomo, ile jest i teraz wiesz, można też te kolory. Ja tu w zasadzie **Waiting For Pre-Test** to znaczyłem już na zielono jako takie prawie skończone.
Znaczy, no właśnie takie **Failed** tą lewą stronę, powiedzmy już zrobiłem taką jakbym widział mniej więcej te kolory, tak. Może coś tu jeszcze można sprawdzić. No i wtedy nawet a nie **Ready To Do**, to jest jasny zielony. No wtedy można odciąć tak to to jest zielone, to już nie należy teoretycznie do dewelopera, ale tu się nie da tego niestety skasować. No możemy jeszcze nad tym popracować, w sensie podyskutować, jak jest lepiej. Mogę dorobić kolejne, tak jak mówisz, tylko wtedy zapytanie trzeba zrobić i tyle. Ale tu można konflikt pod dashboardem. Tak. Tu nie można. Natomiast jest to interaktywne też, czyli to jest fajne według mnie, jak klikniemy sobie tutaj tylko, no tu jest akurat to rozbicie, nie. Ale jak klikniemy na konkretne, o tutaj **Failed Test**, to od razu nas przenosi do tego, nie. To też jest wygodne.

**Łukasz Bott**: Coś takiego by się przydało u nas w module raportów. Nie, a nie dobra, nie w sensie, bo na tabeli mamy tak, tylko na w sensie na wykresie nie.

**Damian Kamiński**: No bo tu jest wykres robiony na podstawie właśnie już zapytania, tak. Czyli to też tak jakby wykryto raport z raportu, tylko tamten raport to jest raport graficzny analityczny, a ten raport jest raportem tabelarycznym.

**Łukasz Bott**: Ale była punktem wyjścia. Dobra, punktem wyjścia jest to tabelaryczny, a tylko robisz wizualizację. Dobra, zakładać.

**Damian Kamiński**: Dokładnie. I to jest ten, czyli sprint 41. To jest ten **Backlog**. To są wytyczne do tamtego raportu. No dobra. Mam omówione.

**Kamil Dubaniowski**: No dobra, bo ja już mam kolejkę tutaj na czatach. Czekają, pisałem.

**Damian Kamiński**: Dobra, to hej.

**Łukasz Bott**: Cześć.

[zatrzymano transkrypcję]

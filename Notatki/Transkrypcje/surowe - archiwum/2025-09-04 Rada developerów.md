**Transkrypcja**

4 września 2025, 08:01AM

**Anna Skupinska** 0:11  
Yes.  
Yes, there's another developer.

**Lukasz Bott** 0:32  
It's. Yeah, it's.

**Janusz Bossak** 0:42  
And.

**Damian Kaminski** 0:50  
Uh.  
Czyli jesteś współpracownikiem, to żeby się to wyświetlało w twoim?  
W Twojej zakładce do wykonania, a w innych nie na razie mam ustawienia globalne.  
No i jest pomysł, żeby to przenieść, ale to powiedziałbym, że no nie jest pilne, żena już wiem, jest bardziej krytyczne i ja bym to im też wycenił.  
Ee, mamy to na poziomie głównym.  
Powiedziałem, jak to ewentualnie rozwiązać konfiguracyjny mateuszowi, ale powiedział, że to jest tyle roboty, bo tam jest multum procesów i tak dalej, że to nie chce się tego podejmować. No właśnie, ale w sensie tyle roboty to się wiąże z kosztami, więc według mnie normalnie, jeśli Piotr oszacował by się jaki to jest nakład.  
To można niezależnie od tego, czy wyjdzie, możemy też dać gwiazdkę, bo Piotr to ma obawy co do wydajności, możemy im to wycenić, zapytać, czy oni w ogóle są w stanie taką kwotę x zapłacić? I jeśli tak, no to możemy podjąć próbę testów. A czy to się powiedzie czy nie? No to dam odpowiedź.

**Piotr Buczkowski** 2:04  
Znaczy na tej zasadzie, że.  
Można włączyć na wybranych procesów. Tak, myślę, że tak, bo tam jest teraz po prostu join to coś tam Union.  
To im do czegoś cię wino nie salatke shiver tam Józef jest trybu torem. To może być ender casey ride in tak, to to nie będzie problemu, ale zrobienie odwrotnie, że.  
Wyjątków, że dla tych nie wysyłaj to nie.

**Damian Kaminski** 2:36  
Nie no to przecież już wiesz, mówimy na skali procesu, więc wyłączają globalnie, wtedy mogą.

**Piotr Buczkowski** 2:38  
Czyli albo jest ustawione w ustawieniach systemowych dla wszystkich albo dla kilku konkretnych procesów.

**Damian Kaminski** 2:47  
O KA kilka konkretnych, może na przykład w skrajnym przypadku dotyczyć wszystkich bez jednego.  
Czyta wtedy jest źle.

**Piotr Buczkowski** 2:57  
Jeżeli będzie 100 procesów może być problem.

**Damian Kaminski** 3:02  
O k.  
No dobrze, to ja tak porozmawiam z Mateuszem, żeby on dokładnie określił, jaka to jest skala, żeby on to policzył? Ile tych procesów w taki sposób chce obsłużyć i.

**Piotr Buczkowski** 3:14  
Dobrze o k.  
Teoretycznie powinno być tak, że.  
Czy ja albo na przykład to?  
Można też dobrze, można odwrotnie tak rzeczywiście, że włączamy dla wszystkich, a wyłączałem dla pojedynczych tylko to.

**Damian Kaminski** 3:34  
Wyją.  
Ma być mniej.

**Piotr Buczkowski** 3:37  
No właśnie, bo.

**Damian Kaminski** 3:37  
Tak.

**Piotr Buczkowski** 3:39  
Mówiłem, że to jest proste, że reality in.  
Nothin też teoretycznie nie będzie jakiś problem.  
Ale to będzie skomplikowane, bardzo tak.

**Damian Kaminski** 3:53  
No dlatego.  
Jest to specyficzne wymaganie, to jest zdecydowanie i teraz pytanie, na ile my możemy to uprościć sobie?  
Ale też, żeby to było w miarę uniwersalne, oczywiście nie tracąc uniwersalności totalnie.  
Że jeśli byśmy powiedzieli, że te sprawy, jeśli jest zaznaczone, że nie wyświetlać, to te sprawy nigdy się nie wyświetlają. Na przykład na głównej zakładce do wykonania, bo to nie są przypisane do ciebie. Jesteś tam tylko współpracownikiem, a sprowadzamy to tylko na tak, jak tam. Mateusz zasugerował tylko na poziom konkretnego obszaru, czyli to jedno do wykonania, ma inne zapytanie, czy to nie jest dobry kierunek?  
Czyli na poziomie obszaru gdzieś byśmy tym zarządzali.

**Piotr Buczkowski** 4:37  
Nie, nie, nie, nie, to to jest wiek jeszcze większe skomplikowanie.

**Damian Kaminski** 4:43  
O k no dobra, po prostu proponuję.

**Piotr Buczkowski** 4:44  
Nie mieszajmy w to obszarów, proszę?

**Anna Skupinska** 4:45  
Znaczy tak, bo może może to nie robić z tego do wykonania, bo do wykonania tak jest dosyć ciężka, musi ma dużo rzeczy do zrobienia, więc.

**Piotr Buczkowski** 4:55  
Właśnie chodzi tylko o zakładkę do wykonania.

**Anna Skupinska** 4:57  
Aha.

**Damian Kaminski** 4:58  
Chodzi tylko o to.

**Piotr Buczkowski** 5:03  
Sprawy, w którym Jestem współpracownikiem?  
Znaczy one się pojawiają już wszędzie tak na wszystkie czy na inne.  
No to jest ustawienie na sprawie na liście do wykonania czy pokazywać takie sprawy czy nie.

**Anna Skupinska** 5:16  
No może po prostu sobie ustalić jakim filtrze czy chcesz je pokazywać czy nie.

**Piotr Buczkowski** 5:20  
Bo teraz jest po prostu to, co mówiłem tam, że był tam or zrobiłem przerobiłem or na Union.  
Tam jest jeszcze też właśnie jeden i unią, że i Union wszystkie te gdzie jesteś torem tą join do case people, tak.

**Anna Skupinska** 5:33  
Mhm.

**Piotr Buczkowski** 5:34  
No to mówię, mówię tam, nie ma problemu, żeby dodać Kacper in jeżeli tam będzie.  
Tak nie org and and cans proceder in jeżeli tam będzie kilka procesów to nie ma problemów, nie będzie to wydają chciałby problemu.

**Damian Kaminski** 5:41  
Dobra.  
Mhm.  
Dobrze to poproszę też Mateusza, żeby dokładnie zdefiniował jak jaka to jest proporcja, ile to dotyczy. Wtedy też właśnie może to zdefiniuje, w jaki sposób łatwiej do tego podejść.  
I wycenić.

**Anna Skupinska** 6:13  
Czy będziemy rozmawiać o dodać funkcję Souls delight?

**Lukasz Bott** 6:19  
A masz jakieś pytania odnośnie tego?

**Anna Skupinska** 6:20  
Znaczy, bo to jest ciągle i designie.

**Damian Kaminski** 6:24  
No bo jest tak jak widać no pytanie jest indesign.  
Bo już tłumaczy jest indesign dlatego, że jest właśnie cały ten komentarz, który już omówiliśmy, czyli ta funkcja. Ta reguła bym powiedział, że ona jest skończona tylko tutaj całe zgodnie z tym ustaleniem całe te źródła trzeba przerobić na dynamik fillm na ten nowy typ.  
I podejść do tego kompleksowo, dlatego to jest indesign, bo po prostu ja tam wrzuciłem ten dodatkowy opis. Mateusz też już chcę z tego korzystać, więc ja bym to pytanie tu, kto się tym zajmie? Czy ania?

**Anna Skupinska** 7:05  
Raczej ja robiłam już poprzednia sorce, więc mogłabym się tym zająć.

**Damian Kaminski** 7:08  
No dobrze, tylko ja mówię nie tylko o tym, bo to to jest zakładam najmniejszy banał tylko o tym, co jest niżej w komentarzu, czyli zdefiniowanie nowego źródła, zdefiniowanie kolumn, które tutaj sobie ustaliliśmy, dla tego typu źródła, żeby one od razu natywnie się pod stawiały, żeby wyżej jakbyś mógł troszkę łukaszu.

**Anna Skupinska** 7:19  
Mhm.

**Damian Kaminski** 7:30  
Tutaj było.  
Taki interfejs. Pamiętasz, jak to omawialiśmy na tydzień albo 2 tygodnie temu, żeby tu był plus można było bez, czyli źródło typu dynamik nie wymaga wgrania pliku? Pozwala, ale można dodać.

**Janusz Bossak** 7:44  
Pamiętam to, to się nie nadaje do do dewelopera.

**Damian Kaminski** 7:50  
Ja nie, nie, ja nie mówię, że się nadaje, to jest cały czas indesign ja to jeszcze zaprojektuję tylko pytanie czy właśnie w przyszłym sprincie mamy na to przestrzeń?

**Janusz Bossak** 8:02  
Wiem no.

**Anna Skupinska** 8:02  
Proszę sprincie, a ja na salę. Ja teraz będę pomagać filipowi w robieniu matrycy. Tak sens to uprawnień tak zależności.

**Damian Kaminski** 8:02  
Czy mam się tym zająć?  
Mhm, uprawnieni pól.

**Anna Skupinska** 8:15  
Więc masz jeszcze trochę czasu, żeby to zaprojektować?

**Damian Kaminski** 8:18  
No dobrze.  
Bo Mateusz też już chcę z tego zacząć korzystać, więc.

**Lukasz Bott** 8:20  
W zeszłym.  
Mówisz około kołakowskim, tak.

**Damian Kaminski** 8:27  
Tak, tak, tak, tak, chodzi mi o te wiesz te reguły te.  
Operacja na źródłach danych tak, czyli te reguły source get source set, więc dobrze by było, żebyśmy od razu już mieli po definiowali tutaj komplet, czyli właśnie ten element i ten deat. No dobra, to ja to zaprojektuję na przyszły sprint.

**Lukasz Bott** 8:50  
Wyjmujemy to z rady i.

**Damian Kaminski** 8:53  
Może możesz to zdjęć?

**Lukasz Bott** 9:07  
Lub jutro jest coś twojego?

**Piotr Buczkowski** 9:09  
No jak pracowałem nad tym lepiej stracą maili, tak?  
To jest takie coś, że jest zarejestrowane zdarzenie. Edycja sprawy tak.  
I tego się nie da wyłączyć.  
Nie da się wyłączyć, zawsze zawsze zarejestrowane i nigdzie nie jest wyświetlany. Nie jest, nie wiem jaki to miało sens. Nie ja to robiłem.

**Anna Skupinska** 9:33  
Może powinna w zasadzie w zasadzie wyświetlane gdzieś.

**Damian Kaminski** 9:35  
Zaraz zaraz, ale ja nie zrozumiałem Jeszcze raz.  
W sensie nie da się wyłączyć globalnie tej.

**Piotr Buczkowski** 9:41  
Jest to jest mechanizm, jest ten mechanizm rejestrowania tych zdarzeń, tak?  
Oprócz tego jest jeszcze jeden typ zdarzenia edycja sprawy.

**Damian Kaminski** 9:52  
Po prostu, że.

**Piotr Buczkowski** 9:52  
Który jest rejestrowany, ale nie da się włączyć, nie da się wyłączyć tego.  
Ale nigdzie nie jest wyświetlany przy wyświetlanie jest warunek, że pomijaj te zdarzenia. Nie wiem po co to zostało zrobione, może ktoś z was pamięta? Nie wiem.

**Lukasz Bott** 10:04  
Ale.  
Ale to Piotr mówisz?

**Damian Kaminski** 10:09  
Dobrze, czyli Jeszcze raz w tej tabeli dedykowanej do kasy Józef activity tak.  
Ee jest po prostu zapisywane zdarzenie, że ktoś edytował niezależnie od historii sprawy, a tutaj możemy zarządzać tylko i wyłącznie takimi zdarzeniami właśnie bardziej nie ingerujący mi w treść sprawy, tylko podglądu dokumentu, podglądu sprawy i tamten element tu nie jest wylicytowany jako możliwy do włączenia i wyłączenia i zawsze się loguje, ale nie jest z kolei nigdzie prezentowany po stronie frontendu.

**Piotr Buczkowski** 10:21  
Tak.  
Tak i nie wiem po.

**Janusz Bossak** 10:41  
No to może trzeba prezentować kawą? Informację o tym, że ktoś edytował z prawem, no to czemu nie tak?

**Damian Kaminski** 10:41  
O k.  
Powtórzenie historii nieco.

**Piotr Buczkowski** 10:51  
Po co pow.  
Corii dokładnie.

**Janusz Bossak** 10:56  
No właśnie, żeby też nie zaśmiej całą gdzieś tam z drugiej strony tak, bo skoro to jest w historii, to po co tutaj? No może.

**Anna Skupinska** 11:01  
A czy może jeżeli ktoś szuka jakby co konkretny Użytkownik zmienił, a nie jak została zmieniona sprawa?

**Piotr Buczkowski** 11:08  
Nie, to jest tylko fakt, że jak ktoś edytował sprawę.

**Anna Skupinska** 11:11  
A czy to jeszcze się przydaje, żeby ktoś by usuwał sprawy to wiadomo, że ktoś coś kiedyś zmienił, nawet jeżeli sprawa jej historia zostaną usunięte.

**Damian Kaminski** 11:11  
Znaczy, bo dzisiaj na historii.

**Janusz Bossak** 11:19  
Ale co tam właśnie, co co co tam jest w tym zapisie znaczy, że edytował, ale wiadomo co edytował, że zmienił. Nie wiem kwotę.

**Damian Kaminski** 11:19  
No ale.  
Nie, nie, nie fakt, zakładam fakt, d.

**Piotr Buczkowski** 11:26  
Nie po prostu edytował.

**Lukasz Bott** 11:27  
No fakt.

**Damian Kaminski** 11:32  
To nie jest powtórzenie historii, tylko tak jakby w historia, bo dzisiejsza nasza historia, jakbyś mógł otworzyć jakąkolwiek sprawę. Łukasz, ona też w pewien sposób utrudnia odczyt edytuj jących z takiego wysokiego poziomu, więc może niekoniecznie trzeba się tego pozbywać. Trzeba było się nad tym zastanowić, czy to jakoś sensownie wyświetlić na froncie, bo.

**Lukasz Bott** 11:39  
Moment.

**Damian Kaminski** 11:54  
Zwróćcie uwagę jak byś mógł go sprawę otworzyć to tam wysoko poziomowe, bo widzimy tylko i wyłącznie właścicieli.  
I etapy dopiero jak wejdziemy w szczegóły, to mamy z kolei już bardzo taki.  
Rozdmuchany widok, czyli musimy skontrolować, żeby zobaczyć kto i co i kiedy. A tutaj jak rozumiem to jest taki prosty tylko kto kiedy kto kiedy. Oj teraz jakby ten luk krok rios.  
Ee edytował.  
100 pól.  
No to to by była taka długa lista i czas królować do kolejnego. Tak to co Piotr mówi, to zakładam, byłaby lista, kto, kiedy, kto, kiedy, kto, kiedy.  
No skoro już to mamy to zastanowić się może, czy to warto gdzieś tu w takiej formie uproszczonej wyświetlić?

**Lukasz Bott** 12:43  
A ja zadam może inne pytanie.  
Czy czy te informacje, jeżeli je rejestrujemy, to czy gdzieś wyświetlamy?

**Damian Kaminski** 12:52  
Mhm.  
Tak, tak, tak, tak, oczywiście one są wtedy wróć na historię, tak jak jest historia pola na dole. To jest historia aktywności czy coś takiego.  
Ee no tu jest w nowym w sumie widoku nie wiem jak włącz po prostu weź wyłącz to na tym procesie.

**Piotr Buczkowski** 13:10  
Mogę miała pokazać zaraz.

**Damian Kaminski** 13:12  
A no to pokaż, bo nie wiem jak na nowym na starym to było po prostu po prawej po lewej było historię pola po prawej było to.

**Lukasz Bott** 13:17  
A o k dobrze.  
No dobra, no to jest.  
Ja w sumie te teraz też tak pomyślałem, czy skoro o tym mówimy rejestrowaniem tego typu zdarzeń to może właśnie?  
Do dorzucić tutaj to, cośmy rozmawiali, to potrzebę rejestrowania użycia, delikt case na konkretnej sprawie i żeby to sobie ktoś tam.

**Piotr Buczkowski** 13:36  
Nie.

**Lukasz Bott** 13:38  
Czy gdy lidka jest robimy?

**Piotr Buczkowski** 13:38  
Przecież mówiłem, Dlaczego nie?

**Damian Kaminski** 13:39  
No mówiliśmy, gdzie to ma być ostatnio to omawialiśmy.

**Piotr Buczkowski** 13:43  
To jest stosowany razem skasowaniem sprawy i tak ma zostać.

**Lukasz Bott** 13:43  
Nie no o k dobra?  
Dobra, dobra.  
No dobra masz.

**Piotr Buczkowski** 13:55  
Ja wtedy była spór, czy to jest aktywność administracyjna, czy inna.

**Lukasz Bott** 14:00  
Hej, to tak dobrze.

**Piotr Buczkowski** 14:01  
Obecnie ja twierdziłem administracyjna, bo obecnie zestawie z listy usunięta może usuwać tylko administrator.

**Damian Kaminski** 14:02  
Znaczy my to.

**Lukasz Bott** 14:09  
Zgadza się, dobra.

**Damian Kaminski** 14:11  
Tylko my to omawialiśmy, a do tego powstał jakiś b.

**Lukasz Bott** 14:12  
Nie były.  
Nie, jeszcze nie zrobiłem, zrobi, nie, nie zrobię do tego.

**Damian Kaminski** 14:19  
O k.  
No bo to ma być tam przy logach, nie.

**Lukasz Bott** 14:23  
Tak tak tak śmy ustalili tak, tak, tak, tak, tak.

**Damian Kaminski** 14:24  
Tak ustaliliśmy, że tylko tylko tam, bo tam będziemy szukać.

**Lukasz Bott** 14:28  
Tośmy ustalili.

**Piotr Buczkowski** 14:29  
Żyje.  
Czym się uruchamia, bo.

**Lukasz Bott** 14:42  
Swoją drogą zgłoszeniach od fiksa.

**Anna Skupinska** 14:45  
A co się stało?

**Lukasz Bott** 14:47  
Bo.  
Tutaj.  
W którymś momencie przy aktualizacji ámonika.  
Zmienił mi się kolor.  
Ten.  
Kolor tak interfejsy.  
Na czerwony, a ja miałem na swoim demo jakiś taki ciemnogranatowy.

**Anna Skupinska** 15:06  
A może sprawdzić jakie jest kolor teraz w ustawieniach systemowych może ktoś zmienił?

**Lukasz Bott** 15:11  
No właśnie jest czerwony jakiś jaki odcień czerwony?

**Damian Kaminski** 15:13  
Takie jak teraz wyświetla Piotrek.

**Anna Skupinska** 15:14  
A czy nie? Zobacz w ustawieniach systemowych jaki jest ustawiony.

**Lukasz Bott** 15:16  
No nie Piotrek ma jakiś różowy, tak no to znaczy to.

**Piotr Buczkowski** 15:19  
Znaczy tutaj mi się czerwone ostatnio zauważyłem, nie wiem skąd się wzięła.

**Damian Kaminski** 15:23  
No to ja czuję, że to chłopaki przy ustawieniach systemowych jak popracowali przynieśli na reaktora to mogli to niesłusznie coś się zakodować, że się nadpisuje.

**Piotr Buczkowski** 15:34  
Przecie to jest.

**Lukasz Bott** 15:35  
Ja sprawdzę jeszcze w ustawieniach systemowych.

**Damian Kaminski** 15:39  
Sprawdź, ale ja bym to wiązał z reaktorem.

**Lukasz Bott** 15:39  
Czy to nie ja? Ja już.  
Nie, nie, ja już sprawdzałem, ewidentnie jest zmieniony kolor tak ja tylko mówię w tym sensie, że w aktywności o właśnie aktywności użytkowników tej administracyjne i sprawdzę, czy przypadkiem sam sobie nie podmieniłem tak może przez jakiś przypadek, ale jeżeli nie, jeżeli nie będzie tak no to no to ten to to zgłoszę to jako hotfix tak, no bo to urnę.

**Piotr Buczkowski** 16:06  
Czy chodzi o to tak?  
Tutaj tak jednak tak też zrobiłem.  
Jakby wysłany mail tak, to akurat proste o przesłanej sprawie.

**Damian Kaminski** 16:15  
Mhm.

**Piotr Buczkowski** 16:21  
Można włączyć można wyłączyć zapisywanie.  
Która jest ci, bo to może zajmować dużo miejsca, tak.

**Damian Kaminski** 16:27  
O k.

**Piotr Buczkowski** 16:30  
Stąd tak to zrobiłem, a.  
Wiadomo jak widać wpisów jest dużo i dużo jest tych Zero co jest edycją tak tu jest tylko to, że ktoś jakie ktoś miał uprawnienia.

**Damian Kaminski** 16:51  
Mhm.

**Piotr Buczkowski** 16:54  
W momencie.  
Edycji.  
Ale te wpisy są.

**Damian Kaminski** 17:00  
Ok, ale to mamy tą historię, przecież to może z tego to wynika.  
Że ktoś edytował, skoro to jest tu przejdź na sprawę.  
Zamknij to przejdź wi.

**Piotr Buczkowski** 17:17  
To kto?

**Damian Kaminski** 17:18  
Informacje o sprawie.  
Mnie i liter Ki nie, to nie jest tu teraz, a wejdź w ludziki, trzecia pozycja uprawnienia.

**Lukasz Bott** 17:22  
I i.

**Piotr Buczkowski** 17:29  
To jest tak mniej intuicyjne, to trzeba zmienić, dlatego o tym.

**Damian Kaminski** 17:30  
I na dole. Sprawdź, kto ma uprawnienia do sprawy.  
I czy to czasem nie jest związane z tą historią uprawnień?  
Że po to to zapisujesz?

**Piotr Buczkowski** 17:41  
A może i tam?

**Damian Kaminski** 17:41  
Że tu można na daną datę.  
Pamiętasz, bo to jest tak, że jak ktoś coś edytował, to wtedy zapisuje się stan właśnie uprawnień sprawy. Na ten moment edycji, że to nie mamy na.  
Codziennie, czy to 5 minut zapisywane tylko właśnie w momencie jakiegokolwiek podjęcia akcji?

**Piotr Buczkowski** 17:58  
To.

**Damian Kaminski** 18:04  
To może to po to było?

**Piotr Buczkowski** 18:05  
No może być to sprawdza to no tego nie wiedziałem.

**Damian Kaminski** 18:11  
To był on dla neuki robione. Kojarze właśnie, że że że zapisywana jest ta właśnie historia na dany moment i to jest właśnie przy edycji.  
To może po to to było wymyślone znaczy nie wiem kto to projektował. Wtedy wydawało mi się, że ty, ale to może ktoś inny jednak.  
No jeśli tam zapisywane są bieżące uprawnienia, to ja zakładam, że to właśnie po to było.

**Piotr Buczkowski** 18:44  
Adrian Przemek krajno Marek coś robił.

**Damian Kaminski** 18:50  
Marek rejestrowanie aktywności użytkowników dwudziesty pierwszy.

**Piotr Buczkowski** 18:51  
Adrian, pamiętasz Adrian jesteś, bo widziałam, że przez moją siostrę.

**Adrian Kotowski** 18:54  
A tak jak mówisz, które opisywałem na innego inny wiadomość, to jest ten temat do aktywności tak użytkownika.

**Piotr Buczkowski** 19:00  
Yy są wpisy Zero.

**Damian Kaminski** 19:01  
Historii uprawnień do sprawy na dany moment.

**Piotr Buczkowski** 19:04  
Które nie są wyświetlane tam w historii aktywności, co zawsze rejestrowane.  
0 3. Edycja, sprawy tak.

**Adrian Kotowski** 19:12  
Tak, tak, to jest rodowe edycji, a wszystko to jest wyżej. To jest specjalne operację. To właśnie typ jedność, sprawie tak.

**Piotr Buczkowski** 19:17  
Tak.  
Oczy Zero nie jest wyświetlane.  
Tutaj.

**Adrian Kotowski** 19:28  
Sprawy tak, a wszystko to jest wyżej, to tych wpisów tutaj w tej historii typowych zdarzeń.

**Piotr Buczkowski** 19:34  
Bo tutaj nie jest oscarem wyświetlane pytanie, czy zerem są wyświetlane.  
Tutaj.  
Nie pamiętasz dobrze dobry trop. To jest prawda o k znaczy.  
To było takie pytanie, że dodając te logowanie tych myli po prostu zastanowiłem się, po co to jest tak nie wiedziałem, po co to jest.

**Adrian Kotowski** 19:54  
Gdzie powinny jest to powinny być, bo to jest.

**Damian Kaminski** 20:00  
Mhm, no to pewnie to po to.

**Adrian Kotowski** 20:04  
Gdy sprawdzamy to cało, jakby w sensie całą tabelę, więc to powinno to być sprawdzane, ale masz Jeszcze raz zweryfikować.

**Damian Kaminski** 20:04  
Tak zakładam.

**Adrian Kotowski** 20:12  
To jest na przykład właśnie tych uprawnień nie ma jakby takiego ciągłego wiecie wyliczanie.

**Piotr Buczkowski** 20:22  
Znaczy okej.  
Dobrze.  
Zostawiam to tak, sprawdzę, sprawdzę, czy to jest to tak, no, bo dzięki za trop nie pomyślałem o tym.

**Damian Kaminski** 20:35  
Dzień dobry.  
Dobra, idziemy dalej w takim razie co tam Łukasz jeszcze mamy.

**Lukasz Bott** 20:44  
Dobra, to w takim razie Piotrek to ja to zdejmuję z rady, taka to sobie tam sprawdzić.

**Piotr Buczkowski** 20:48  
Tak, tak.

**Janusz Bossak** 20:54  
Przepraszam was chwilę nie słuchałem, ale tamte co pokazaliście o tych historii uprawnień to jest jeden, może o tym mówiliście, ale zrobiłem coś innego.  
Akurat przy justynie na strefach się tak jest, jest proces, w którym jest zaznaczony, że administrator nie ma praw do tej sprawy, znaczy do tych spraw.

**Piotr Buczkowski** 21:13  
Trzeba trzeba to uwzględnić. Nie było to uwzględnione.

**Janusz Bossak** 21:15  
Tak.  
No to mi chodzi, prawda?

**Piotr Buczkowski** 21:20  
Znaczy, nie rozmawialiśmy, wtedy nie wiem, nie zrobiłeś zgłoszenie o to ja zrobię zgłoszenie zaraz po spotkaniu.

**Janusz Bossak** 21:22  
No ale to właśnie to.  
Wychodzi, że Justyna ma dostęp a nie ma nie ani.

**Piotr Buczkowski** 21:28  
Tak nie pomyśleliśmy o tym, żeby to uwzględnić tutaj to ustawienie.

**Janusz Bossak** 21:30  
Tak tak, bo to potem było dodawane.

**Damian Kaminski** 21:41  
W sensie tylko to ja też gdzieś tam zauważałem te błędy, ale nie nie miałem czasu na przetestowanie, tylko to jest bezpieczniejsze. Tak mam na myśli to, że nawet jak wyświetla się że ma uprawnienia to nie ma tak czyli to jest ta wersja powiedzmy.  
Trzeba ujednolicić, ale system działa poprawnie.  
Tak.

**Piotr Buczkowski** 22:01  
Jest jest mylna informacja jednym miejscu.

**Damian Kaminski** 22:04  
Mhm.

**Lukasz Bott** 22:05  
Niekonsekwencje, dobra.  
Zmianki w komentarzu weryfikację działania funkcjonalności.

**Piotr Buczkowski** 22:14  
Chodziło o to, że.

**Lukasz Bott** 22:16  
A żeby tutaj chodziło?

**Piotr Buczkowski** 22:17  
Jeżeli dodamy kogoś.

**Lukasz Bott** 22:19  
Zmian kujemy no.

**Piotr Buczkowski** 22:24  
Jest dodawany do nie zdajemy maila o tym, że zostaną z tą zmianą. Kowale ma informacje, ale ponieważ został wzmiankowany, to zostaje dodany do CC.  
Już jako jako osoba będąca pc to już dostaje informacje o kolejnych.  
Komentarzach, ale już jak odc. Nie to, że wzmiankowany.

**Lukasz Bott** 22:43  
Tak.

**Damian Kaminski** 22:44  
To znaczy w ogóle wydaje mi się, że zastanawiam się, bo ja też gdzieś takie rozterki od klientów otrzymywałem, czy my nie, bo funkcja obserwator.  
Wiąże się z właśnie mailing giem.  
Czy nie powinniśmy wprowadzić coś takiego, że można wyłączyć na procesie mailing dla obserwatorów?

**Lukasz Bott** 23:13  
Do jakiegoś mi wyłączyli na etap na konfigurację etapów tak, że nie nie wysyła informacji powiadomień o otrzymaniu sprawy. Tak.

**Damian Kaminski** 23:22  
Tak i niech on dostaje pierwszego maila inicjującego czy to będzie komentarza czy że został dodany, żeby ten fakt gdzieś tam musi odnotował, bo może tego nie zauważyć, ale czy zasadnym jest, że później on dostaje wszelkie inne?

**Piotr Buczkowski** 23:36  
No to takie było założenie tego.

**Damian Kaminski** 23:40  
No rozumiem o k, że obserwator dostaje wszystkie.

**Lukasz Bott** 23:40  
Wiesz?

**Piotr Buczkowski** 23:42  
Znaczy jest rola rider, tak?  
Ritter to jest ma dostęp bez bez, bez mail.  
Nie ma teraz możliwości edycji tego z interfejsem. Być może warto dodać edycje interfejs.

**Damian Kaminski** 23:49  
O.  
No właśnie to tego nie wiedzieć. O tym zapomniałem, może nie tyle, ale wtedy to trzeba adjuster tu rol tylko regułą, prawda?

**Piotr Buczkowski** 24:02  
Tak.

**Lukasz Bott** 24:02  
Tak, tak.

**Piotr Buczkowski** 24:04  
Być może warto dodać do interfejsu.

**Damian Kaminski** 24:09  
Czyli w tym obszarze said barze z uprawnieniami?  
Tylko jak to wtedy nazwać obserwator bez bez powiadomień?

**Piotr Buczkowski** 24:21  
Odczyt.

**Lukasz Bott** 24:22  
Cichy obserwator.

**Damian Kaminski** 24:23  
Odczyt na tylko to jest nazwa roli, więc.

**Lukasz Bott** 24:28  
Czytacz.

**Damian Kaminski** 24:28  
No dobra, można się nad tym jeszcze zastanowić o k dobra, to jest dobry kierunek.

**Piotr Buczkowski** 24:31  
Czy czytelnik tak?

**Damian Kaminski** 24:33  
Także, że a tu rolę rider?

**Piotr Buczkowski** 24:34  
Jest też rola forbidden, ale też jest tylko tylko z reguł. Nie wiem, czy to.

**Damian Kaminski** 24:39  
To akurat bym powiedział że.

**Piotr Buczkowski** 24:40  
Właściwe było dodawanie tego z interfejsu, żeby ktoś nie usunął.  
Bo to jest jasno, ma wynikać z przebiegu tak, że na przykład sprawa trafiła do kogoś, to jest.  
Niewłaściwy to był niewłaściwie na tej sprawy, albo po prostu.  
Po pewnym czasie chcemy ukryć przed twórcą sprawy.

**Lukasz Bott** 24:57  
To musi mieć.

**Piotr Buczkowski** 25:01  
Jako sprawę no bo jeśli na przykład ktoś ktoś tworzą przykład sekretariatu, a.  
Dalej już jest sprawa tajna, już tajnie do nas.

**Damian Kaminski** 25:09  
To znaczy powiem piotrze, tak tego typu wyzwania.  
Ono jest teoretyczne i.  
Nie twierdzę, żeby się nie przydało, natomiast nikt nigdy ja w swojej tutaj doświadczeniu nie odnotowałem takiej potrzeby, natomiast, że się wysyłają powiadomienia dla kogoś, kto miałby mieć wgląd do sprawy, to nie raz były takie kwestie. No to tutaj rider, więc to można by było rozszerzać. Natomiast forbidden to bym się nie śpieszył, ale na ten moment to też mogę dodać to z funkcji reguł, więc jest o k dobra.

**Piotr Buczkowski** 25:30  
No to jest ritter rider.  
To tak samo tutaj można tak dodać do rider, jeżeli nie chcemy tych powiadomień.

**Janusz Bossak** 25:48  
Jak ostatecznie?

**Damian Kaminski** 25:48  
A no właśnie to pytanie jest takie, czy my słusznie dodajemy do obserwatorów tylko tego lidera niestety nie widać tak, bo może powinien być rider a nie obserwator po wzmiankowany.

**Piotr Buczkowski** 25:49  
No właśnie.  
No też tak powiem się, gdyby to robiłem dodał do riderów.  
Nie o to robiłem. To chyba Rafał. Jeszcze Rafał bębenek robił tak, smakowanie re. Pamiętam.

**Damian Kaminski** 26:12  
Tylko to trzeba było zaopiekować od razu dwustronnie, czyli raz zmiana tutaj backendu gdzie się dodaje, a 2 tych endermanów trzeba by było jednak wyświetlić.

**Piotr Buczkowski** 26:22  
No tak tak.

**Damian Kaminski** 26:26  
Zapiszesz to Łukasz, to to znaczy pytanie, co sądzicie czy?  
Czy bo to jest zmiana wsteczna? Tak w sensie zmieni się funkcjonalność. Obecna może nie tyle co wstecz, ale od teraz zmieni się działanie tego wzmiankowana. Czy tu widzicie jakieś ryzyka?

**Janusz Bossak** 26:42  
Doczekałem poczekajcie, bo różnica pomiędzy liderem a obserwatorem przynajmniej w mojej głowie zawsze była taka, że do ridera nie są wysyłane powiadomienia, a do obserwatora są wysyłane powiadomienia.

**Damian Kaminski** 26:54  
Dokładnie.  
Tak.

**Janusz Bossak** 26:57  
W związku z tym, jeżeli obserwuje opiekujemy powiadomienia z komentarzy, to według mnie powinno być tak samo, że powinien być dodawany do obserwatorów, bo chcemy, żeby dostawał powiadomienia.  
Tyle że z tych tylko, że zakres tych powiadomień powinien być inny.

**Damian Kaminski** 27:11  
Czemu tak uważasz?  
Ale jakie powiadomienia chcemy, żeby on dostawał?

**Janusz Bossak** 27:16  
Bo.  
Mailowe.

**Damian Kaminski** 27:21  
Ja bym się nie ja bym się z tym nie zgodził tak jeden do jeden. A dlaczego tak uważasz? Ja chcę kogoś jak piszę komentarz na przykład w kontekście nie wiem tutaj bieżącej kogoś, żeby coś podjął, to ja chcę, żeby on dostał to jedno powiadomienie tak jak powiedzmy z worda, gdzie w komentarzu sobie opisuje, że zrób to teraz.  
A już cię nie obchodzi, że sprawa poszła sobie dalej.  
Jak zrobiłeś?

**Lukasz Bott** 27:45  
Znaczy.  
Słuchajcie, wróćmy do źródła tego.

**Janusz Bossak** 27:50  
Dobra.

**Lukasz Bott** 27:52  
Wróćmy do źródła tego, bo tutaj to to, o czym dyskutujemy. Pierwotnie zamieszanie wynikało z tego.  
Że.  
Jak kogoś po raz pierwszy zmian kujemy w komentarzu to.  
To ta osoba nie jest w ogóle świadoma faktu, że została wzmiankowana tak, a dostała.

**Piotr Buczkowski** 28:15  
Znaczy ma.  
Mówicie informacje nie ma maila.  
O to chodzi, że nie dostaje maila.

**Damian Kaminski** 28:22  
Nie.

**Lukasz Bott** 28:22  
Tak, tak, tak.

**Damian Kaminski** 28:24  
Nie dostaje maila wzmiance.

**Lukasz Bott** 28:25  
Tak, że została wzmiankowana tak dostała, natomiast dostałam maila, że nagle ni stąd ni zowąd jest obserwatorem sprawy, tak.

**Damian Kaminski** 28:35  
Mhm.

**Lukasz Bott** 28:36  
I i a to, że została wzmiankowana to ma w interfejsie w tym w tej zakładce powiadomieniu tak i i.

**Damian Kaminski** 28:43  
No to trzeba to zaopiekować globalnie.

**Lukasz Bott** 28:45  
I moim zdaniem minimum tutaj do zrobienia to zróbmy to, że jeżeli kogoś po raz pierwszy wzmianka kujemy w komentarzach, to.  
Powiadomienie jest tutaj w interfejsie, tak jak dotychczas to bez zmian plus wysyłany jest mail, być może trzeba ten mail scalić od razu z tym pierwszym mailem dodania go do obserwatorów, tak?

**Damian Kaminski** 29:08  
Nie nie, bo ustaliliśmy przed chwilą, że on niekoniecznie powinien być obserwatorem i według mnie nie powinien być.

**Lukasz Bott** 29:12  
Nie, nie, nie, nie, nie, moment, nie, nie jest to takie oczywiste, że to byśmy ustalili, bo ja już słusznie zaprotestował.  
Ja bym ja bym zrobił minimum tutaj. Tylko tyle, że zostałem wzmiankowany po raz pierwszy w komentarzu to dostaje oprócz tego, że mam to w interfejsie.  
To dostaje maila tak jak masz co podałeś przykład edycji wreszcie tak, jeżeli ktoś cię w komentarzu wzmiankuje, to dostajesz maila, że zostałeś wzmiankowany w komentarzu jakimś tam w dokumencie i tyle i to jest to.

**Damian Kaminski** 29:36  
No.  
Zgoda dokładnie, ale nie dostaje, ale nie dostaje maila, że ktoś potem przeniósł ten, bo to to to przez analogię, że ktoś potem przeniósł ten dokument do nowego folderu. Mnie to w sumie nie obchodzi, a tutaj dostajesz potem maila, że ta sprawa zmieniła etap, bo już jesteś jej obserwatorem, co mało cię obchodzi.

**Lukasz Bott** 29:59  
Ale ale to, ale dobra to, ale to może rozdzielmy te.

**Janusz Bossak** 30:04  
To są chyba 2 różne różne zapisy.

**Lukasz Bott** 30:05  
Tak, ja myślę, że to są tak 2 różne rzeczy.  
Ja bym wiesz co ja bardziej inaczej tak yy, czy można się czy ja powiedzmy, że ktoś dodał mnie do obserwatorów sprawy, tak.  
Może miało tam służbę, intencje mnie dodawać tak tylko, że jak ja zapoznałem się z tą sprawą to stwierdzam, ale mnie to nie dotyczy. No i się nie mogę od od ten o od od od od od obserwować tak no no i dostaje mailem.

**Damian Kaminski** 30:34  
A no właśnie, a dostajesz maile, więc no dobrze, dobrze przejdźmy do minimum, czyli tak mówisz, wysyłamy maila, teraz wysyłamy maila, stałeś się obserwatorem, powinniśmy wysłać maila, ktoś cię w tej sprawie wywołał. Pytanie tam wysyłamy treść, czy nie można wysłać można niecały jak jest długi komentarz jakąś zajawkę pierwszych 20 znaków, czy coś w tym stylu można by spojrzeć, jak to jest w word ill właśnie z worda, bo tam chyba nie idzie cały komentarz, ale nie pamiętam.

**Lukasz Bott** 30:40  
Minimum którym?  
Tak w komentarzu.

**Damian Kaminski** 31:04  
Natomiast jednocześnie, jak już to opiekujemy, to żeby może nie wychodziły też 2 tak, żeby jak ci ktoś jawnie kogoś dodał do obserwatorów, to dostaje tego maila, a tutaj od razu zmieniamy tą rolę na ridera.

**Janusz Bossak** 31:19  
Znaczy.

**Lukasz Bott** 31:20  
Nie, nie zmieniałbym tutaj roli dla ridera zostawiamy obserwatora.

**Janusz Bossak** 31:22  
Panie.  
Ja się skłaniam.  
Ja się skłaniam do tego co mówi Damian.  
Według mnie powinno być tak.  
Rola obserwator dodawana.  
Prawym panelu to jest zupełnie odrębny temat, natomiast jeżeli kogoś w zmian kujemy.  
To o co nam chodzi, czy o co chodzi użytkownikowi? On chce wywołać tego użytkownika, żeby on do tej sprawy zajrzał. Tak więc.

**Lukasz Bott** 31:49  
Tak.

**Janusz Bossak** 31:52  
Według mnie, tak jak Piotr powiedział, powinniśmy na to dawać go do riderów, o ile nie jest już dodany, no po to, żeby do tej sprawy miał dostęp i mógł w ogóle na cokolwiek zareagować.  
Tu rodzi się pytanie, czy wolno nam wywoływać osoby spoza grono obecnych liderów?  
Bo to jest pytanie główne, tak?  
I to było jakby przedmiotem wtedy rozważań z Rafałem właśnie czy czy wolno, czy nie wolno to szliśmy do wniosku, że wolno, czyli teoretycznie wzmiankowana nie rozszerza.  
Czyli daje uprawnienia do przeczytania tej sprawy, komuś może być zwykły Użytkownik, który udostępni.

**Damian Kaminski** 32:30  
Mhm.  
Ale ma uprawnienia edycji, tak?

**Janusz Bossak** 32:35  
No ale tylko edycji.

**Lukasz Bott** 32:36  
Nie, nie wiem.

**Damian Kaminski** 32:37  
To znaczy nie wiem, czy edycji może niekoniecznie edycji, bo jak ktoś jest obserwatorem, to może dodać komentarz czy nie może.

**Lukasz Bott** 32:40  
Nie lider.

**Piotr Buczkowski** 32:44  
Nie, nie może.

**Janusz Bossak** 32:44  
Więc wiecie, no, jeżeli idąc śladem obecnego.

**Damian Kaminski** 32:45  
Nie może o k.

**Janusz Bossak** 32:50  
Obecnych yy tego komunikatora i tego co się dzieje na timesa i tak dalej, no kto ma prawo dodać kogoś do czegoś no do konwersacji, bo ten który tą konwersację stworzył.  
Więc nie wiem.

**Damian Kaminski** 33:04  
Oj nie, nie, nie, nie, nie.

**Janusz Bossak** 33:06  
Ja bym był tutaj ostrożny z tym.

**Damian Kaminski** 33:07  
Nie jest taki Janusz, jak powiedziałeś inne osoby też mogą rozszerzyć konwersacje.

**Janusz Bossak** 33:13  
No dobra znaczy.  
Mówię, że istnieje ryzyko, ale wracając do do meritum.  
Ten ktoś, kogo dodamy?  
Powinien dostać informację o tym, że został wzmiankowany i w moim przekonaniu koniec na tym, jeżeli.  
Drugi drugą wzmiankę, którą może dostać.  
Jeżeli ktoś odpowie jawnie na komentarz.  
Ten, w którym on był wzmiankowany?  
Czyli mamy komentarz i mamy tam odpowiedz, czyli wywołuje Damian Kamiński. Co sądzisz o tej sprawie i w tym odpowiedz udzielamy odpowiedzi, nie wymieniając już Damiana.  
Ale jest on jakby w rodzicom tego komentarza Nie i wtedy powinien dostać odpowiedź. Jeżeli napiszę komentarz poniżej. Słuchajcie jeszcze nie wiem co z tym zrobić, ale nie jest to odpowiedź na na.

**Damian Kaminski** 33:57  
Mhm.

**Janusz Bossak** 34:06  
Niczyją w zmian, ty no to nie to to idzie normalnym trybem. Ci co mają ci co obserwują tak ci co obserwują sprawę, no to widzą to jako nowy komentarz w sprawie, tak no i dostają informacje.

**Damian Kaminski** 34:11  
Nikt nie dostaje powiadomienie.

**Janusz Bossak** 34:20  
I tak chyba to powinno działać.

**Damian Kaminski** 34:21  
Z tym riderem to też jest tak, że ten rider powinien zostać nadany, jeśli nie jest może na dany nie wiem czy to jakkolwiek konfliktuje to właśnie otwarte pytanie, bo jeśli ktoś już jest dodany na przykład jako współwłaściciel, to może wtedy nawet nic zbędne jest dodawanie, czy może najpierw warto sprawdzić, czy ten wywołany jest już w jakiejś roli w kontekście tej sprawy i wtedy niekoniecznie nawet dodawać go jako lidera, bo.  
Równie dobrze ktoś może być współwłaścicielem, tak jak nasza znowu cofnę się do naszego procesu wycen, czyli przeglądamy i wywołuje, nie wiem anie Piotra. Przypominam wam, że tutaj sprawa czeka na wasze podjęcia.  
W akcji tak.  
A wy już jesteście współpracownikami, powiedzmy tych spraw, więc no nie wiem, czy wtedy jest jeszcze zasadne do dopisywanie do roli ridera tego użytkownika, czy to już jest zbędne?

**Lukasz Bott** 35:16  
No moim zdaniem to nadmiarowy.

**Damian Kaminski** 35:20  
No więc tutaj można jeszcze powiedzmy pod tym kątem to.  
Zoptymalizować.  
Dobra podsumowując.  
Jan kowanie powinno skutkować wysłaniem powiadomienia dotyczącego udzielenia komentarza ze wzmianką, a nie informac.  
O tym, że ktoś nadał komuś uprawnienia, to co to jest niezależne komunikat i niezależna funkcjonalność? Jednocześnie to wzmiankowana, anie powinno nadać uprawnienia ridera. O ile ten Użytkownik nie ma innych, a innych. Czytaj wyższych, bo może mieć tylko uprawnienia albo obserwatora, albo współpracownika, albo wręcz właściciela.

**Lukasz Bott** 35:58  
Albo właścicielom.

**Piotr Buczkowski** 35:59  
Jeżeli nie ma dostępu do odczytu dla tej sprawy z jakichś powodów.

**Damian Kaminski** 36:01  
Tak, jeśli nie ma dostępu do odczytu, to wtedy nadaje mu dostęp ridera jeśli ma, no to nic w zasadzie nie zmieniamy i tyle.

**Janusz Bossak** 36:09  
No i trzeba być ostrożnym z tym forbidden, tak chociaż nie, no tak.

**Lukasz Bott** 36:13  
No nie no to nie dyskutujemy o forbidden.

**Damian Kaminski** 36:14  
Forbidden jest nad wszystkim, czyli możesz komuś nadać obserwatora współpracownika właściciela, jak dasz forbidden to się nie dostanie.

**Lukasz Bott** 36:20  
Nie nic nie zmieni.

**Janusz Bossak** 36:21  
Ale chodzi mi o to, że nie powinienem nawet zmian kopać, czyli ja Jestem za ograniczeniem listy osób, do których mogę zmontować naprawdę.  
Nie podoba mi się to z punktu widzenia bezpieczeństwa.

**Damian Kaminski** 36:34  
No ale wtedy eliminujesz ten element ridera, czyli najpierw musisz dać komuś obserwatora albo musimy dołożyć funkcjonalność interfejsu nadawania ridera, żeby móc go wzmiankowano bać.

**Lukasz Bott** 36:34  
No ale.

**Janusz Bossak** 36:45  
Wiesz co? Chodzi mi o to, żeby to było bardziej znaczy troszkę bardziej utrudnione. Czyli tak wyobrażam sobie.  
Piszę tą małpkę i mam listę osób, które mają prawo do tego.  
Do tej sprawy tak na różne sposoby, albo są adminami albo cokolwiek, no ale mają związek z tą sprawą.

**Damian Kaminski** 36:59  
Mhm.

**Janusz Bossak** 37:05  
I teraz może powinna być druga małpka albo drugie jakaś ikonka, jeżeli nie widzę ktoś jest spoza tej sprawy.  
To żebym jawnie musiał to zrobić tak, żeby nie wychodziło na to, że potem nam jakiś admin i od Security powie, że a tutaj ten Użytkownik nie wiedział i tam panią krysię dodał. A ona nie ma prawa wiedzieć o tej fakturze? Nie.

**Damian Kaminski** 37:31  
Mhm, czyli na końcu listy byłoby Dodaj, Dodaj nowego.

**Janusz Bossak** 37:31  
A tak to.  
Tak i wtedy jest to wiesz?  
I to byśmy notowali w.  
Blogach.

**Lukasz Bott** 37:40  
2.

**Janusz Bossak** 37:42  
Tak, że ten ktoś może powiedzieć to nie tylko wzmiankowano on nadał uprawnienie do tej sprawy.

**Damian Kaminski** 37:51  
Czyli w zmian kując no dobrze, tylko nadał uprawnienie.

**Anna Skupinska** 38:01  
Muszę przyznać, jak się kogoś dodało. Ja bym dodała kogoś w komentarzu, to nie bym nie pomyślała, że o tej osobie się dodaje. Uprawnienie do tej sprawy.

**Janusz Bossak** 38:07  
No właśnie no właśnie no właśnie i to każdy Użytkownik zrobi nieświadomie kogokolwiek tutaj.

**Piotr Buczkowski** 38:13  
Musi już specjalnie wzmiankowana nie to, że wpiszesz tylko musisz zmian korkować tak, czyli tym.

**Janusz Bossak** 38:17  
No ale no to jest prosta funkcja w tej chwili.

**Lukasz Bott** 38:18  
Ale mimo to.

**Anna Skupinska** 38:22  
Może dało mu, że dać dopisek uwaga, kiedy zaryzykujesz użytkownika dodajesz, dajesz uprawnienia do tej sprawy.

**Damian Kaminski** 38:27  
To znaczy.  
Tu się ania zgodzę i nie, bo jeśli się nad tym nie zastanowić, to masz rację, że że nie miałabyś pojęcia, ale z drugiej strony, no jeśli kogoś wzmiankuje, czyli chcesz podjął akcję, no to musi się to wiązać z nadaniem uprawnień do tego. No wiecie, przenieśmy to na świata na vlogowy w komentuj mi to Janusz, no to muszę ci pokazać ten dokument do wglądu i poczekać aż mi skomentujesz, więc.

**Anna Skupinska** 38:57  
To może zależeć na przykład ktoś chce komuś zobaczyć, hej, zobacz na ten komentarz w konwersacji, to może o tym pomyśleć, ale cóż.  
Tak można nie pomyśleć o tym, a tylko to.

**Damian Kaminski** 39:06  
Nie no dobra abstrahujemy, ważne jest to, żeby też to opisać, to wtedy właśnie nie jesteśmy znowu niepodważalnie i tak działa system i nikt nie może się przyczepić, że że że coś poszło nie tak dobrze to znaczy ja się zastanawiam, bo teraz tak propozycja Janusza jest ciekawa.

**Janusz Bossak** 39:16  
Czy?  
Jeszcze jeden pomysł jeszcze jeden pomysł.  
Ponieważ wydajemy komunikator.

**Damian Kaminski** 39:24  
No.

**Janusz Bossak** 39:28  
Może powiązać pewne koncepty tak, czyli tutaj ograniczyć, czyli można wzmiankowana tylko osoby, które tutaj są.  
Tak w tej chwili.  
A skoro nie mogę wywołać osoby, której tutaj nie ma, to mogę to zrobić w komunikatorze tak wchodzę w komunikator pisze wzmiankę i wskazuje tą sprawę i najwyżej ten ktoś nie ma dostępu do tej sprawy.

**Damian Kaminski** 39:53  
No to jest, to jest dostępne w sensie.

**Lukasz Bott** 39:53  
I wtedy poprosi.

**Janusz Bossak** 39:53  
I.  
I wtedy prosi o dostęp tak i ktoś uprawniony mu daje ten dostęp.

**Damian Kaminski** 39:57  
Nie.

**Lukasz Bott** 40:01  
No to słuchajcie, to jest takie.

**Damian Kaminski** 40:02  
Tak, to za to to zaopiekuje to tą potrzebę. Powiedzmy komunikator uzupełni właśnie w ramach tej potrzeby.

**Janusz Bossak** 40:09  
A tutaj się trzymam ściśle tego grona osób, które są dodane już do obserwatorów. Oczywiście to nie zmniejsza, czy nie wyłącza możliwości wejścia tutaj w zakładkę uprawnienia i dodania kogoś do obserwatorów i wymienienia go w tym czacie, ale to jest wtedy świadome działanie, tak po pierwsze musi istnieć ta zakładka uprawnienia. Ten ktoś musi mieć możliwość dodawania kogoś jak dodał, czyli jawnie go dodał. Rozszerzył zakres osób uprawnionych, wtedy go wzmiankuje jak.

**Damian Kaminski** 40:09  
Tylko.

**Janusz Bossak** 40:40  
Nie jest w tym zakresie osób, to nie może go w wymiankowa i tyle wtedy korzystać.

**Damian Kaminski** 40:44  
No tak tylko jak tego jak tego nie skomplikować, żeby wiecie, chcę kogoś z wymiankowa, to muszę zrobić 10 kliknięć wcześniej, żeby to zrobić. To żebyśmy w tą stronę też nie nie skomplikowali tutaj z tą Dodaj nową osobę.  
No jest ciekawym pomysłem, czyli mam listę osób, które dzisiaj są podpięte z jakimiś uprawnieniami mam na dole powiedzmy.  
Pierwszą osobę z Nie wiem, rozszerzy uprawnienia do sprawy tak i i tam sobie wtedy pojawia się okienko, gdzie wybieram osobę i obok.  
Co wybieram? Wybieram z listy rozwijanej, czy to jest?

**Janusz Bossak** 41:22  
No to co już zaprojektować?

**Damian Kaminski** 41:23  
Od od najmniejszych tak, czyli odczyt obserwator i współpracownik tak.

**Janusz Bossak** 41:29  
Bo zobaczcie jak to teraz wygląda.

**Lukasz Bott** 41:29  
Słuchajcie no.

**Janusz Bossak** 41:32  
Robię sobie tu małpkę.  
Na tej liście mam całą firmę.

**Damian Kaminski** 41:38  
No tak, no i to jest łatwe w sensie ju x jest super oczy ops abstrahuję na razie od bezpieczeństwa i x jest super, bo mogę każdego wywołać szybko.

**Janusz Bossak** 41:48  
No właśnie, no ale czy to jest to co chcemy?

**Damian Kaminski** 41:52  
No i jesteś właścicielem sprawy, więc w jaki sposób odpowiadasz za ten formularz ten dokument?  
Bierzesz na siebie jakąś odpowiedzialność i teraz my chcemy być mądrzejsi niż Użytkownik, nie.

**Janusz Bossak** 42:01  
No to tak jak pani powiedziała nie byłam.  
To jak ania powiedziała, nie byłaby świadoma, że to robi tak.  
Bo ja to mogę, nie wiem właśnie ani wywołać, tak.  
Nie mogę nawet.

**Damian Kaminski** 42:12  
No dalej już musicie się.

**Anna Skupinska** 42:14  
Tak, to chyba myślał, że ta osoba tylko dostęp do tego czatu nie.

**Damian Kaminski** 42:19  
Nie no to to już ktoś kto by korzystał chyba raz no.

**Anna Skupinska** 42:23  
Ale powiedzmy, że mamy użytkowników, którzy nie znają się na tym za bardzo, więc nawet żeby było jakieś ostrzeżenie, że dołączając tego użytkownika, przyznajesz mu uprawnienia, to już byłoby dużo.

**Damian Kaminski** 42:25  
Ale o k no dobra, różne są opcje, mhm.

**Janusz Bossak** 42:36  
No i wiesz, nie masz takie coś, potem nie.  
Bo tu jest podłączony, tam nie wiem umowa z prezesem.

**Damian Kaminski** 42:47  
Nie no łatwo jest znaleźć przypadek, który, że tak powiem tak jak tu pokazałeś ja abstrahuję od tego tylko pytanie, czy żeby zabezpieczyć się przed takimi przypadkami jak to zrobić mądrze, żeby nie skomplikować tam, gdzie świadomie dodajemy jej korzystamy. Nie, ja nie Jestem przeciwny, tylko żebyśmy nie dorobili klimatologii.

**Adrian Kotowski** 42:47  
Może ktoś klika Dodaj komentarz to pokazuje mu się.

**Anna Skupinska** 43:07  
Myślę, że wystarczy ostrzeżenie.

**Lukasz Bott** 43:07  
Ale czekajcie, to znaczy tak, słuchajcie, trzeba to chyba jakoś wyważyć, bo z jednej strony możliwe, że ta klika wolodia jest potrzebna, bo podam przykład z życia i to na na na naszej firmie tak na przykładzie naszej firmy zrobiłem ten oceny, sytuację do tych dokumentów, cv tak co tutaj wspomaga pracę naszych koleżanek, tak oli i Justyny, i i teraz tak na procesie CWU. Nas w firmie jest wyraźnie ustawione, że administrator osoba w roli administratora.  
Nie ma wglądu do tych spraw tak i a zdarzały się sytuacje takie, bo tam, zwłaszcza w tym początkowym okresie. No czasu do czasu tamten coś oceny nie działał. Dziewczyny zgłaszały uwagi. Tak, no to ja musiałem wyraźnie poprosić o to dobra, to jeżeli to jest konkretny przypadek, bo chcemy zobaczyć konkretny przypadek, nadaj mi uprawnieni i wtedy mnie dziewczyny dodawały do jednej konkretnej sprawy dodawały mnie jako właśnie tam, powiedzmy ridera, tak tam nie ridera, tylko obserwatora.

**Damian Kaminski** 43:44  
Mhm.  
No.

**Lukasz Bott** 44:12  
Powiedzmy tak.

**Damian Kaminski** 44:13  
O k.

**Lukasz Bott** 44:14  
I i obserwatora, czy tym współpracownika, ale w każdym razie musiało mnie jawnie nadać tak, czyli to jest to odpowiada na taką troszkę sytuację, właśnie tego trochę co Janusz podał scenariusz, że jest w filmie bezpiecznik jakiś tak, który właśnie by się czepiał i to jest bardziej taka kwestia organizacji pracy. Tak.  
Yy, z drugiej strony mamy tą kwestię właśnie, że wzmiankuje to ania, yy jest tak jak powiedziała ania, że niekoniecznie jest świadoma tego, że przy okazji się zadziała magia, bo ta osoba dostała jakiś tam zestaw uprawnień. No i jeszcze ta trzecia opcja do tego, że to jest cytologię tak dodatkowa, tak no.  
W tej chwili zmian nie jest proste, tak no.

**Damian Kaminski** 45:00  
Dobrze no pytanie, ja się zgadzam, że możemy to zabezpieczyć tylko właśnie jak to zabezpieczyć najdelikatniej tak jak to zrobić, żeby było na imię niej, czyli żeby już z tego interfejsu móc dodać tą osobę i do komentarza i od razu nadać jej uprawnienia, żeby nie trzeba było gdzieś przechodzić indziej.  
Czyli.

**Janusz Bossak** 45:18  
Słuchajcie, wróćmy do meritum, bo to to rozszerzenia są fajne, natomiast tak te filmiki działają od 2 lat albo więcej.

**Lukasz Bott** 45:24  
Tak.

**Damian Kaminski** 45:27  
No.

**Janusz Bossak** 45:28  
Więc zostawmy to. Musimy zaopiekować temat pierwszego maila, że jak ktoś jest wzmiankowany, to do niego idzie.

**Lukasz Bott** 45:30  
Tak.  
Wanny to otrzymuje maila dokładnie i tyle, i i to jako minimum zróbmy.

**Janusz Bossak** 45:37  
To trzeba zrobić, a potem się możemy.

**Damian Kaminski** 45:39  
Nie, ale czy jednocześnie poprawiamy na ridera, bo to też jest istotne, bo ale to poczekaj, Łukasz, bo teraz będzie tak, czy nie będzie tak, że dostanie 2 maile, bo jest dodany jako obserwator. To jest jeden mail jest dodany jako.

**Lukasz Bott** 45:42  
Nie.  
No.  
Wzmiankowany no to być może, no to być może tą sytuację, gdy w momencie gdy zmian kuje, to trzeba po prostu połączyć te 2 maile w jeden, tak, że zostałeś wzmiankowany w komentarzu w tej w tej sprawie i dostały się jednocześnie uprawnienie do jako obserwator do tej sprawy i tyle i być może to uspójnić tak.

**Damian Kaminski** 45:55  
Wzmianka i drugi mail i ma dostać 2 maile.

**Janusz Bossak** 45:59  
A tak.

**Lukasz Bott** 46:22  
Czy to, bo to jest tak, jakby podwójne, zgadza się?

**Damian Kaminski** 46:26  
No ja ja uważam, że że tutaj za zmiana roli to jest przy okazji można zrobić i to już byśmy mieli zaopiekowane, ale o k jak chcecie tak totalnie po minimum no to niech będzie tak jak mówisz. Ja bym poszedł ten jednak kroczek dalej tutaj dosłownie kroczek zmieniłbym to żeby ta osoba nie dostawała w związku z tą wzmianką kolejnych mail.  
Ale no albo zapytajmy tutaj też klienta, tak?

**Lukasz Bott** 46:48  
Nie no to.

**Piotr Buczkowski** 46:51  
Tylko jeden myśl, tylko jeden mail, że zostawicie ją Kowal nie o ceta.

**Lukasz Bott** 46:55  
Tylko 1 maj wzmiankowany każda. Każdy kolejny wzmiankowany już już nie nie powoduje wysłania maila tak o wzmiankowanym, no bo.

**Damian Kaminski** 47:02  
Nie, nie powoduje Dlaczego nie, nie każde wzmiankowany powoduje, nie nie tu chodzi mi o co innego. Kolejne maile mam na myśli w ramach roli obserwatora to mam na myśli kolejne maile.

**Piotr Buczkowski** 47:05  
Nie powoduje.

**Lukasz Bott** 47:14  
Okej?

**Piotr Buczkowski** 47:15  
No nie no to musi.

**Damian Kaminski** 47:18  
Może zapytajmy tutaj też, żeby żeby nie pójść też za bardzo, bo może mój pomysł jest tutaj niespójny z tym, co się dzieje? Może okolie z tego korzysta.

**Piotr Buczkowski** 47:18  
Wymawia.

**Damian Kaminski** 47:28  
Zapytajmy, co dalej tak, czyli z racji, że dzisiaj dostanie powiedzmy tego maila, ale on jest też dodawany do opcji obserwatora to, bo no teraz.  
Utwierdził mnie tylko w przekonaniu, jak jest forward case tej sprawy, to obserwator dostaje powiadomienie. Tak tak pamiętam czy się mylę.

**Piotr Buczkowski** 47:50  
Jeszcze raz jak jest co?

**Damian Kaminski** 47:52  
Jak jest przekazanie tej sprawy między etapami od użytkownika do użytkownika? To obserwator dostaje powiadomienie o tym fakcie, tak?

**Piotr Buczkowski** 47:56  
Tak, to absolutnie tak, tak.  
Tym.

**Damian Kaminski** 48:00  
No właśnie i dla mnie to jest bez sensu, że osoba wzmiankowana to dostaje, bo to ja nie zgłaszam osoby jako obserwatora. Ja wywołuję kogoś we wzmiance.

**Janusz Bossak** 48:13  
No jak tak to trzeba opiekować według mnie.

**Lukasz Bott** 48:15  
Dobra, no to.

**Damian Kaminski** 48:16  
Że wiecie, po prostu potem czujność na te maile spada, jak my ładujemy mailami ze wszystkim co się da, to po prostu ludzie, potem tylko przekują i potem wszyscy wyłączają te maile i i nic z nich nie wynika.

**Piotr Buczkowski** 48:18  
Yy, zmień po prostu żeby.

**Lukasz Bott** 48:29  
Standardowy koszt ksero psa.

**Damian Kaminski** 48:35  
Więc ja bym poszedł o ten kroczek dalej zmieniłbym skutek w zmian kowania, że rola nie obserwator tylko rider.  
Email o tej wzmiance i tak jak Janusz powiedział, obserwujemy jeszcze przy każdym komentarzu co to jest za komentarz? Jeśli to jest komentarz zagnieżdżony do komentarza ze wzmianką, to wtedy tamten ci w wzmiankowana oni dostają też powiadomienie Jeszcze raz, że ktoś odpowiedział na komentarz, w którym byłeś wzmiankowany.

**Lukasz Bott** 48:45  
I.  
No k.

**Damian Kaminski** 49:06  
A jeśli to jest równoległy komentarz bez żadnej wzmianki, no to nie idzie do tych osób żaden żaden komunikat.  
No dobrze to według mnie temat wyczerpaliśmy słownie to może już wykorzystany.  
Kopali lata, żeby to opisał. Możemy to tu później wrzucić. Mogę to zaopiekować.

**Lukasz Bott** 49:36  
Dobra, to dałem, przypisuję tobie i i.

**Damian Kaminski** 49:38  
No to przypisz do mnie, no.

**Lukasz Bott** 49:40  
I zdejmuje z tego.

**Damian Kaminski** 49:44  
No dobra, jest za 10. Nie wiem czy jeszcze coś podejmujemy pilnego, czy czy zostawiamy.

**Lukasz Bott** 49:45  
To niejako nie, nie, nie, nie był tutaj. Ja za chwilę jeszcze tam gdzieś mi Lucyna wywołała.

**Damian Kaminski** 49:53  
No i do mnie coś dzwoniła, nie wiem o co chodziło jeszcze.

**Lukasz Bott** 49:53  
Yy.

**Damian Kaminski** 49:57  
Się pali coś.

**Lukasz Bott** 50:05  
Dobra, no to kończymy.

**Anna Skupinska** 50:10  
Mhm.  
Do zobaczenia na spotkaniu firmowym.

**Lukasz Bott** 50:11  
Do dzięki d.

**Damian Kaminski** 50:14  
Cześć.

**Adrian Kotowski** 50:15  
Cześć.

**Janusz Bossak** 55:00  
No.

**Janusz Bossak** zatrzymano transkrypcję
**Transkrypcja**

12 listopada 2025, 09:06AM

**Janusz Bossak** rozpoczęto transkrypcję

**Lukasz Bott** 0:19  
Udostępnie, bo mówię z piątku został, słyszycie mnie?

**Damian Kaminski** 0:24  
Tak.

**Janusz Bossak** 0:24  
Tak słychać.

**Lukasz Bott** 0:26  
Dobra, jakbyście coś słyszeli w tle jakieś głosy to Przepraszam z górę za kolegów zbijania, który mi się ze ścianą wydzierają, więc.  
Jak to jest?  
Przyjemność mieszkania wtedy w tym mieszkaniu prasowanie.  
Yy, słuchajcie dobre.  
Tutaj takie zgłoszenie dotyczące.  
Tych źródeł opartych na bazie danych burak lu i Mateusz tam dopytuje się, czy w ogóle źródła online nie będą działały w nowych raportach. Ja nie wiem, no, przetestowałam przed chwilą przed przed spotkaniami tam nawet dali. Tak źródeł działa, działa online. Być może to jest specyfika coś tam? Dla bazy Oracle możemy mieć problem z przetestowaniem tego.  
Ale to ja jeszcze to sobie to mu się.

**Damian Kaminski** 1:19  
To znaczy, ja ja to poruszałem w piątek z Mateuszem na takim 1 x 1 w sensie no konwersacji.

**Lukasz Bott** 1:22  
No.

**Damian Kaminski** 1:28  
No i cóż, no tu może być jakieś inne zapytanie w kontekście nowego nowych raportów, tak natomiast jakbyś podjechał do góry tam już, bo nie pamiętam w tym momencie, on wrzucił tu jakiegoś loga.

**Lukasz Bott** 1:40  
Wrócił loga natomiast no.

**Damian Kaminski** 1:42  
Miałem życie.  
Tylko ten rok nie ma zapytania z kulowego chyba.

**Lukasz Bott** 1:47  
Nie ma jakiejś zapytanie, jest kolorowo, ale sądząc po treści tego zapytania, to jest wiesz jakieś konkretne zapytanie do konkretnych tabel do konkretnej bazie.  
Mm no i teraz tak naprawdę, no nie jej nie wiadomo co, co było przy czym to znaczy, yy ja był. Ja Jestem o tyle, byłbym zdziwiony, że skoro tak mamy źródło online, bo opierające się o jakiś sterownik.  
Tak do bazy o rakla, więc my robimy ten robimy komunikację od cb tutaj sterowniku dc. No to moim zdaniem to powinno być transparentne. Tak to my się komunikujemy ze sterownikiem od bbc, a to i po to się robi sterownik od cb żeby to on tłumaczył w tą i we w tą tak to komunikację tak z danym silnikiem.  
No chyba, że chyba, że coś jest dosyć specyficzne dla.

**Damian Kaminski** 2:39  
Nie, nie, nie, ja to inaczej rozumiem.  
Ono.  
On nie to znaczy. Ja nie uważam, że on tłumaczę, w sensie on odpowiada za połączenie ten sterownik odbc, ale nie za tłumaczenie. W sensie my musimy zadać pytanie w języ.  
Pora klonowym.

**Lukasz Bott** 3:02  
No o k no ale to.

**Damian Kaminski** 3:03  
Znaczy to, co tutaj wzbudza podejrzenia, że coś jest nie tak, to jest komunikacja, to znaczy to jest oświadczenie Mateusza, że stare raporty działają.

**Lukasz Bott** 3:06  
No.  
No właśnie o to chodzi, nie?

**Damian Kaminski** 3:15  
Czyli tu jest coś innego? Nie tak. Tu jest na końcu jakieś asino query limit, znak zapytania.  
Może właśnie.

**Lukasz Bott** 3:22  
To jest jakiś parametr.  
Czy jakiś przekazywany?

**Damian Kaminski** 3:27  
No właśnie, więc może tutaj tego tu coś brakuje jakiegoś konkretnego pokrycia w kontekście.  
Mm te integracji.  
No ktoś musi na to spojrzeć.

**Lukasz Bott** 3:40  
O k no to jest inwalidzi charakter, więc może właśnie chodzi o o to coś. My przekazujemy być, może przekazujemy jakiś parametr, nie.  
Albo powinniśmy wartość jakiegoś parametru przekazywać, nie przekazujemy i stąd się to.

**Damian Kaminski** 3:53  
Dokładnie, a starych raportach może to było pokryte jakość? Nie wiem no.

**Lukasz Bott** 3:57  
No tak, a a tutaj on to no i sterownik przekazuje coś takiego. Właśnie taki znak zapytania do silnika aura klasowego aura nam pokazuje gest kozakiewicza. Tak, bo nie wiem co to jest, no.  
No dobra, no w każdym czasie jeden no na pewno.

**Damian Kaminski** 4:14  
No no ktoś musi na to spojrzeć z deweloperów.

**Lukasz Bott** 4:18  
Tak na pewno nie jest to, że źródło online nie działają, bo działają tak no bo przed chwilą no mówię, no spotkanie przetestowałem dobra, to w takim razie to już.

**Damian Kaminski** 4:27  
Znaczy z tego co? Co co można zasugerować, to z tego co ja zrozumiałem, to tak dla starych raportów, to co Piotr mówił, czyli tu można by powiązać.  
Do zgłoszenia ani z rejestracją zapytań sql owych, no ale tu jest zarejestrowane, natomiast włączając ten moduł rejestracji zapytań jest kulowych vlogach przywołuje przy wywołaniu.  
Raportu no to należałoby porównać jakie zapytanie leci ze starego raportu analogicznego, a jakie z tego no i mamy tam działa tu nie działa, mamy jakąś różnicę.

**Lukasz Bott** 5:01  
Mhm.

**Damian Kaminski** 5:02  
Mimo, że to będzie rozwiązanie, bo może to jest tylko właśnie ten jakiś.  
Limit, nie wiem, to może powinien. No domyślam się, że limit powinien określać jakieś.

**Lukasz Bott** 5:12  
Możliwe, że to powinnam limit. Wiesz co to jest Majewski Queen to jest po pierwsze, to jest składnia moje kule majes que lowa, że daje ci limit coś tam i tu powinno pójść. Wiesz, pójść po prostu konkretna liczba. Tak, bo to macie zwrócić ileś tam wietrzy.

**Damian Kaminski** 5:13  
Jakiś parametr internetowy tak.  
No to może po prostu nie było takiego przyjemną? Widzicie no.  
Nie mamy wszystkich przypadków biznesowych po stronie testów i i ten olek no był dowożony przez ostatnie lata w jakiś tam sposób tak tam gdzie była teta czy jakieś inne narzędzia, no to.

**Lukasz Bott** 5:49  
Jakoś to działały.

**Janusz Bossak** 5:49  
Znaczy.

**Damian Kaminski** 5:50  
To były jakieś drobnostki, poprawiane, żeby to było kompatybilne, no i tyle dla prostych zapytań.

**Lukasz Bott** 5:57  
No ok, no nie wiem.  
No dobra, to tutaj to, czyli to deweloper musi się pewnie.  
Pewnie by trzeba było skontaktować się z Mateuszem, żeby jakoś tą sesję yy z klientem może tam potrzebna jest to połączenie tej tak jak mówisz tego mechanizmu logowania. Zapytanie sql owych i i zobaczenia.

**Damian Kaminski** 6:19  
Tak no to nie na pewno nie jest klientem, bo to według to jest rossman, to wiesz, tam jest. Mamy przecież ludzie od tego.

**Lukasz Bott** 6:26  
Właśnie nie no to w tym w tym sensie o to mi chodziło, także z naszymi ludźmi w kontekście klienta nie, bo chodzi mi o to, że my nie mamy bardzo reagują, ale podejrzewam, że to nie jest kwestia Oracle jako takiego tylko właśnie być może my jakoś tam niekoniecznie dobrze parujemy zapytanie to jest kulowe, dobra, słuchajcie, pozostały jakieś jesteśmy 2 2, 3, 5, 7.

**Damian Kaminski** 6:29  
Mhm.  
Ok.

**Lukasz Bott** 6:53  
7, co to jest?  
Bo to wsi na którejś bodajże z kolegów.  
Tona kamilu wisi a luba do wyszukiwania procesów permanentnie przechowuje wartość to to już gdzieś tam dyskutowaliśmy. Tutaj się koledzy dopytują, czy też proszą, żeby się tym zająć, bo to nam, bo to coś jakieś tam blocked w nauce jest.

**Damian Kaminski** 7:10  
Tak.

**Lukasz Bott** 7:19  
Mm a chodzi o coś takiego, że.  
Zresztą sam sam tego doświadczyłem, że jak zostawimy jak przed filtrujemy sobie ciulato listę procesów, czy listę raportów czy coś, to ten filtr pozostaje na stałe, nawet jeżeli się człowiek wyloguje i chyba no i tutaj tak z komentarza wynika, że dyskusja propozycji są takie albo żeby to było ustawiane jakoś tam czasowo.  
Yy, że ten filtr yy nie nie albo no przynajmniej, że jak się wyloguje to faktycznie czyści mi te wszystkie ustawione filtr. Tak no i.  
Z tych kierunków pewnie musimy pójść.  
Trzeba to się z tym trzeba się tym zająć w tym sensie, no bo coś tam w nauce cholerni to blokuje. Tak czytam, Jestem się czepiają moim zdaniem to bardziej jest.  
Niedogodność ani, ani także.

**Damian Kaminski** 8:10  
No tak, tylko w nauce temat jest jeszcze inny, bo co to znaczy wylogować się w nauce, skoro z tego co kojarzę to tam jest a d tak więc nie ma takiego typowego wylogowania.

**Lukasz Bott** 8:17  
No tam jest tam jest logowanie.  
No to nie, no jak tam, jak zamkniesz przeglądarkę?

**Damian Kaminski** 8:27  
Całą przeglądarkę, no to według mnie można to do tego tak podejść, nie nie okna tylko znaczy nie zakładki tylko przeglądarkę.

**Lukasz Bott** 8:37  
No tak, no że jak masz nie wiem, możesz mieć odpocząć, no była modlitwa w kilku zakładkach tak było może kilka spraw nie ogarniasz na raz.

**Damian Kaminski** 8:47  
Nie według mnie ma to sens, no można to tak zredefiniować, no to jest raczej drobnostka, tak zmiana jakiegoś parametru po stronie lokal zosta sposobu przechowywania w lost or pytanie czy macie na to jakieś inne? Ewentualnie nie wiem, tykamy analizował, bo tam ma Daniel zna do nas w tym tematem pisał.

**Lukasz Bott** 8:47  
Nie no to wiesz.

**Damian Kaminski** 9:07  
Sorry, trochę trudno mi sklecić dzisiaj myśli.

**Lukasz Bott** 9:12  
Nie wiem, to pytanie, to to byś?

**Damian Kaminski** 9:13  
Ta propozycja według mnie ma sens albo do momentu kliknięcia wyloguj, albo do momentu zamknięcia okna przeglądarki nie zakładki tylko okna przeglądarki.

**Kamil Dubaniowski** 9:22  
Ale rozumiem, że to mówimy o sercu, tak filtry nas na raportach też interesują czy nie?

**Damian Kaminski** 9:28  
Filtr na raportach nic są nie nie poczekaj, ale filtry na raportach w momencie kliknięcia refresh się dla strony, a nie dla raportu się i tak resetują.

**Lukasz Bott** 9:28  
Nie mówimy o tym serce?

**Janusz Bossak** 9:41  
Ale oni chcą, żeby się recytowały, czy żeby nie się nie zresetowały.

**Damian Kaminski** 9:44  
Nie oni chcą i mają w sumie tutaj mają tutaj logiczne poparcie ku temu, że zobacz masz taki masz taką stronę karty wpisane. Teraz tak wyłączasz komputer, włączasz, wchodzisz do tego zakładki procesy i dalej masz karty, no i jest taki.

**Lukasz Bott** 9:45  
Nie to.  
Ale chciałeś inny proces uruchomić, no.  
No.

**Damian Kaminski** 10:10  
Mamy jakiś dłuższy okres?  
Więc można by było zmienić, może nie wiem, no bo to była sugestia przemka, żeby to trzymać. No ale Daniel w sumie podał dobry przykład, jak wchodzimy na Google PL to nie mamy bitego do myślenie słowa ostatniego wyszukiwania. Tak tylko wchodzimy na czystą kartę.

**Lukasz Bott** 10:13  
Żeby wytrzymamy permanentnie wygląda na chwilę obecną.  
I no tak.

**Janusz Bossak** 10:36  
To tak to znaczy na pewno wylogowanie i zalogowanie powinno oczyścić, że to trzeba rozpisać sobie teraz, czyli które momenty czyszczą.

**Lukasz Bott** 10:43  
I.

**Janusz Bossak** 10:48  
Na pewnych logowanie wylogowanie.

**Damian Kaminski** 10:48  
A według mnie przynajmniej to wylogowanie, zalogowanie i i zamknięcie całego okna, bo jak się przełączasz między to może być potrzeba, żeby jednak.

**Lukasz Bott** 10:53  
Tak.

**Damian Kaminski** 10:56  
Na tamtej karcie to było, skoro zwłaszcza w kontekście raportów mogę mieć taki przypadek, że otwieram sobie nowe karty. Zamykam, bo szukam raportu i kilka ma nazwę. Nie wiem dokumenty kadrowe, tak.

**Janusz Bossak** 11:10  
Może być zasada, że do końca jakby dnia.

**Lukasz Bott** 11:15  
Którzy do końca jak już to mamy parametr tam związane z obsługą czasu trwania sesji, więc do końca trwania sesji.

**Janusz Bossak** 11:23  
Do końca trwania sesji na przykład tak.

**Lukasz Bott** 11:26  
Czyli dopóki jest sesja, no to ten chyba, że jawnie się wylogujesz, jeżeli ile jest możliwość wylogowania bądź całkowicie zamkniesz przeglądarkę, nie pojedynczy każdym, tylko całą przeglądarkę, tak wszystkie.  
Możliwe to ma sens.

**Janusz Bossak** 11:42  
Ale to wtedy trzeba tak rozpisać i powiedzieć, że w takich przypadkach będzie się działo tak, no.

**Lukasz Bott** 11:48  
Dobra, to tylko teraz tak pytanie pierwsze takiej natury organizacyjnej kto rozpisuje, bo to jest karmienie, no tobie to wisi.  
No i drugiej organizacyjne czy jak to rozpiszesz jeżeli się podejmujesz to czy to robimy w tym sprincie tak albo już no w kolejnym tak, bo ten screen to się za 2 dni skończy tak.

**Janusz Bossak** 12:08  
Czy to? No to to już jest prosta sprawa, czy to robimy w tym sprzęcie, czy to jest hotfix?

**Lukasz Bott** 12:14  
Nie jest to hotfix.

**Janusz Bossak** 12:16  
Koniec wszystko.

**Lukasz Bott** 12:17  
To jest skuję o to.

**Janusz Bossak** 12:20  
No dobrze, nie nie wywala im danych, nie wywala im błędów.

**Lukasz Bott** 12:20  
I to już od.

**Janusz Bossak** 12:26  
Powoduje niewygodę.  
I to może być następnym lub nawet następnym wystarczy, że dobrze im powiemy kiedy i zaplanujemy tą paczkę, że im to zrobimy.

**Lukasz Bott** 12:36  
Dokładnie tak.

**Janusz Bossak** 12:37  
Bo może są jeszcze inne tego typu problemy, które można by naprawić.  
Dostarczając odpowiednią właśnie paczkę wartości. Zauważcie jak to pięknie się teraz wpisuje, tak?  
Paczką wartości może być poprawa.  
Zachowania się systemu.  
Przy wybranych filtrach i wyszukiwaniach i to może dotyczyć raportów.  
Procesów.  
Potem samych raportach pamiętania.  
Elementów wyszukiwania.  
Tak więc można by się nad tym zastanowić szerzej i zrobić z tego paczkę wartości. Nie.

**Lukasz Bott** 13:21  
Dobra.

**Janusz Bossak** 13:21  
Ale to przykład.

**Lukasz Bott** 13:23  
Dobra pytanie, Kamil, czy zostawiamy to u ciebie?  
I to ogarniesz.

**Kamil Dubaniowski** 13:29  
No tak, jeśli znacie jakieś inne tematy tak jak już tu zaczął, no to też dajcie mi znać, ewentualnie przypinać je na mnie, to ja tam w module raport owym nie wiem czy mamy soli do zmiany. Kojarzę, że były ostatnie Dyskusje na temat filtrów.  
Ale raczej nie znaczy w zakresie tej listy, tak, co tam się podpowiadać. Tej opcji zaznacz wszystko, to tam mi przychodzi do głowy.  
Ale czy coś więcej pytań?

**Lukasz Bott** 13:57  
Dobra, czyli to Kamil, zostawiłem u ciebie.  
Mm kolejny, który mamy tamten tutaj 057474.  
Yy.  
To dla mnie, no tu też o ósmy jest inwestycja, to możemy wcześniej wstawiony.  
Dobra, tu chodzi o o to wyświetlanie tego linku tak i.  
Któryś z kolegów zrobił jakiś trik, który tutaj umieścił to Bartek, że sztucznie się podaje w tych treściach baby before i after. Mówimy o tym o dostępie tymczasowym, że trzeba dodać diva tak jakiegoś i wtedy wtedy faktycznie podobno to.  
Wtedy dobrze formatuje ten link, tak no przynajmniej jest widoczny we wszystkich.  
Tych klientach poczty.  
O to chodzi generalnie o to.

**Damian Kaminski** 14:55  
No właśnie pytanie jest, to jest klucz czy we wszystkich?

**Lukasz Bott** 14:59  
No dobra stwierdzeniem we wszystkim.

**Damian Kaminski** 15:00  
Bo tu rozmawialiśmy o tym nie niejednokrotnie z Piotrem, że u jednego tak u drugiego nie i tam też jest mhm.

**Lukasz Bott** 15:07  
Tak, ale Damian w piątej tak zgadza się, nie jesteśmy w stanie chyba obsłużyć wszystkich możliwych przypadków, dlatego na dyskusji dyskusji piątkowej tak też był Piotrek. Tak z konsultantami właśnie wyszło. Po pierwsze poprosiliśmy, bo właśnie Bartek zgłosił, że on taki trik zrobił. To poprosiliśmy, żeby umieścił to, jak ten trik wygląda tak. No i jeśli ten trik by zadziałał, to być może go tutaj.

**Damian Kaminski** 15:22  
Mhm.

**Lukasz Bott** 15:39  
Sugestia Piotra, żeby to na stałe w jakiś tam sposób, no może już dodać tak tak, no.

**Damian Kaminski** 15:45  
Poprawić.  
No dobra, jeśli Piotr to widział i i zatwierdził to no nie mam uwag, bo niejednokrotnie o tym dyskutowaliśmy i Piotr zawsze mówił, że właśnie to muszą być te style inline nowe do sprawdzenia. No mogę to dobra, to to.  
Przepiszę, że tak powiem tak, jak mają być to zrobione, jak ma to działać.

**Lukasz Bott** 16:05  
Dokładnie, czyli zaopiekujesz się tak dobra?

**Damian Kaminski** 16:10  
Tak no, pozostaje pytanie gdzie to testować w sensie?  
Na ilu skrzynkach to sprawdzamy? Tak.

**Lukasz Bott** 16:16  
Wiesz co to?  
Wiesz co tutaj doszliśmy? Chyba do wniosku takiego, że mm tak noge mail, no bo to jest popularna platforma.  
Pewnie w gwałt luku takim stacjonarnym, że ktoś ma no i konto na wiki. Jeżeli chodzi o taki polski serwisy, no to pewnie Wirtualna Polska jest dosyć chyba najpopularniejszym tak no.  
Wirtualna Polska, Wirtualna Polska tlen to jest w tej chwili to samo tak, czyli o 2 dawne.

**Damian Kaminski** 16:47  
No o k no.

**Lukasz Bott** 16:53  
Więc to jest to samo? Tak, no to.

**Damian Kaminski** 16:55  
Można jeszcze Onet wrzucić i.

**Lukasz Bott** 16:57  
No one to chyba też jest tak dosyć.  
Popularny i tyle to.

**Damian Kaminski** 17:04  
O k.

**Lukasz Bott** 17:10  
Dzień dobry. Zostałem w takim razie siebie.

**Damian Kaminski** 17:13  
Dobry.

**Lukasz Bott** 17:15  
I jeszcze mamy jenot właśnie Turcja co do tego czy to jest czy nie hotfix na razie na razie merytoryka.  
Mm.  
Chodzi o funkcję seti info działającą w kontekście.  
Pól wymaganych bo.  
W tej wersji czerwcowej, jeżeli pole jest wymagane, to ten komunikat pochodzący z set field info się nie wyświetla, a w wersji 25, czyli marcowej tegorocznej działa to poprawnie, czyli.  
Się komunie jeżeli jest ten film info używane a pole nawet jest wymagane tak to to będzie ten komunikat set film info.  
Trzeba to naprawić pewnie tak no zweryfikować.

**Damian Kaminski** 18:01  
No to to pewnie Kamili Mariusz.  
Tak, to kto opiekował te ukrywanie pole jest wymagane.

**Kamil Dubaniowski** 18:10  
No tak tak no nie powiem, no ale albo Mariusz albanie.

**Damian Kaminski** 18:10  
Kamil, pamiętasz?  
Albania.

**Lukasz Bott** 18:17  
Co Kamil?

**Damian Kaminski** 18:17  
Za mocno za mocno to ukryli, no.

**Lukasz Bott** 18:21  
Pewnie dla ciebie to przypisać i to jakoś tam.

**Kamil Dubaniowski** 18:22  
Tak.

**Lukasz Bott** 18:24  
No i właśnie nie mam indesign.

**Damian Kaminski** 18:27  
Ale bo poczekaj najpierw, bo nie ma dla hotfix in design jest.  
Czy powinno być inwestor właśnie?

**Lukasz Bott** 18:35  
No to znaczy tak, no, Przepraszam, inwestycja. No właśnie nie ma investigate i pytanie czy czegoś?  
Nie wypełniłem, no ale wygląda, że jest.

**Damian Kaminski** 18:43  
A weź Jeszcze raz teraz rozwiń.

**Lukasz Bott** 18:46  
Może ten serwer?

**Damian Kaminski** 18:53  
Ale to jakby brakowało pól wymaganych to by się na Górze wyświetlało.

**Lukasz Bott** 18:57  
Właśnie o to chodzi, nie?

**Damian Kaminski** 19:00  
A founding jest wypełnione.

**Lukasz Bott** 19:07  
Nie wszystko nie no dzisiaj to chyba nie świeci tak więc.

**Damian Kaminski** 19:08  
Mhm.  
To nie wiem o co chodzi.

**Lukasz Bott** 19:13  
No ale to to to wiem. Ja to zauważyłem w zeszłym tygodniu tak to, że że to się jakoś, ale to świeży to nie wiem, a Michał był grzebał przy tych gier statusach coś tam, więc może może zrobić te reguły jakieś za mocne serwisy. Dobra to kamień zostawiam to tobie na new taki.  
I przejrzyj to sobie takiej.  
Ewentualnie zmień klasyfikację, bo nie wiem czy to jest hotfix nie ma żadnych utraty danych tak no po prostu to znaczy o k dobra, być może spełnia ten warunek z racji tego, że co się działo to raz nie działo tak, no no to to to.  
To też jest błąd tak, no po prostu i tyle.  
Kotwic to raczej sytuacja, że system nie działa albo jest.  
Te danych tak no, bo grozi utratą danych.  
Tutaj żadnych danych nie tracimy, tak pole jest jak jest tam, jak się tutaj to wypełnił.  
Ja się komunikat nie wyświetli z kolei tak pole jest wymagane i tak jest wymagany. No to tak jest, to musi wypełnić, tak.

**Damian Kaminski** 20:19  
No dobra, to mamy coś jeszcze.

**Lukasz Bott** 20:21  
To tylko teczne dzięki.

**Kamil Dubaniowski** 20:26  
Są jeszcze zaległości z.  
Most zgłoszeń takich nie podbitych.  
Może przejdźmy przez to. Zacząłem w sumie na razie pomijam te wszystkie ficzery i.  
Niki.  
No to jest właściwie jeden temat i to wszystko do rana idzie.  
To idąc od.  
Szóstego.  
Ja już chyba mi się udało, wszystkie są przypięte odtąd.  
To ma sens? Już rozważałem danielem.  
Nazywali siebie.  
Wysypali strasznie, nie wiem, ten backlog wcześniej działał tak, że znaczy te worki i tam otwierały się po prostu po papie. Nie wiem czy to się gdzieś chyba ta zmienić, ale nie wiem gdzie.  
Teraz otwierają się na fullscreen lista przewija się do samej góry.  
Nie wiesz, moim traktowali rację?  
No to jest do wywalenia pośrednikiem.

**Damian Kaminski** 22:23  
Trzeba.  
No właśnie.

**Kamil Dubaniowski** 22:46  
Czy jest Mateusz?  
Że na ten sprint no nie ma przypisanych sprintów. Rozumiem, że wiemy tą.  
Że jak nie jest?  
Chociaż to Damian tej decyduje tak, no bo ja nie wiem jak.

**Damian Kaminski** 23:02  
Czekaj, czekaj.  
Wysyłana wiadomość nie pojawia się od razu w konwersacji. Nie to na ten sprint sensie, no trzeba dowieźć ten komunikator do końca.  
Tam są chyba 3 błędy, które wyszły już wskutek.  
Testów poprawek, więc to jest jakaś pierdoła zakładam, no że to się nie wyświetla od razu.

**Kamil Dubaniowski** 23:24  
Pasuje się rejonu to komunikator.

**Damian Kaminski** 23:28  
Nie, bo to nie był, nie, nie ma.

**Kamil Dubaniowski** 24:06  
Ale on.

**Damian Kaminski** 24:06  
To już chyba jest poprawiony? Wiesz, bo jest to wysłała na też na czacie odnośnie komuś zaraz zobaczę.

**Kamil Dubaniowski** 24:14  
To wiem.

**Damian Kaminski** 24:15  
Więc to będzie zaraz w poniedziałek chyba Mateusz to zrobią.

**Kamil Dubaniowski** 24:20  
Panie przerobić z tego co wiem nawet.  
To było celem tego sprintu, więc idzie na ten.

**Lukasz Bott** 24:49  
A co to jest ten prefiks BEW tytule a b.

**Kamil Dubaniowski** 24:51  
Backend.  
Bo dzielą sobie zadania i to Mateusz Mateusz, Przemek, jak rozpisuje, to to oznacza, żeby było wiadomo, żeby dziewczyny tego nie testowały, no bo tego nie ma za bardzo. Jak przetestować, mają testować czy frontem działa tak jak czy kujemy o.  
Dobra, to jest progres, to nie rusza, a czemu jest in progress fortun?  
Jakbym się udało to zrobić.  
Czy jest jakiś mecz?  
Też bez fortu coś jest nie tak, coś się wysypało z tymi regułami. Efekt miał być obowiązkowy przy.  
Przechodzeniu na redu.

**Lukasz Bott** 25:47  
Tak, ale patrzę już jest na waiting for lis, czyli de facto jest zrobiony.

**Kamil Dubaniowski** 25:49  
Mam dlatego mówię.  
Takich zadań w takim wypadku nie widać w naszych statystykach, bo efektu zarobił, no to.  
Nie ma obciążenia, nie ma też widocznego spadku. Później dobra zapytam, że moje konto zgłaszał.  
Myślałem, wygoda, wszystkie przekazy Beata, no nie możliwości stosowania wartości po ką automatyczną.  
No i nigdy nie było, więc czemu to jest bag?

**Damian Kaminski** 26:31  
Baton nie wiem, no to to jest.

**Kamil Dubaniowski** 26:34  
Że nie da się wyczyścić, jak jest coś już wybrane w przycisku Radzie baton, to nie ma opcji wyczyszczenia tego.

**Lukasz Bott** 26:39  
Znaczy dobra, bo to jest chyba to to zgłoszono, to pewnie ten to jest ten sowe.  
Piotrek tak.

**Damian Kaminski** 26:49  
Nie, no ale to nie jest prawda chyba.

**Lukasz Bott** 26:52  
Nie jest, jest jest, jest prawda i zawsze tak było. To jest z tym problem, bo dlatego ja właśnie je znam to zagadnienie, bo to jest to jest dentsu. Jeżeli masz listę wyboru i ją masz kilka pozycji i ją prezentujesz poza w postaci radio batonów.

**Kamil Dubaniowski** 26:53  
Jest, ale od zawsze tak było.

**Damian Kaminski** 27:00  
O k.  
Tak.

**Lukasz Bott** 27:10  
To faktycznie przypisanie pustej wartości do d.

**Damian Kaminski** 27:10  
Mhm.

**Lukasz Bott** 27:16  
Pola reprezentującego to listę wyboru nie nie, nie powoduje wyczyszczenia tak tych ra.

**Damian Kaminski** 27:22  
Ale w regule automatycznej jakieś czy?

**Lukasz Bott** 27:24  
Tak, tak w ogóle automatycznej masz jakiś tam warunek? Jeżeli jest spełniony, żeby wyczyścić nie oczywiście.  
I dlatego ja to, bo to jest konkret. Tam było zapotrzebowanie w konkretnym procesie i dlatego tam obejście. Zastosowałem takie, że wprowadziłem jakiś taki fejkowy fejkowy opozycję typu 2 kreseczki, tak co brak wyboru nie i ten.

**Damian Kaminski** 27:48  
Brak wyboru.  
Mhm.

**Lukasz Bott** 27:52  
I i wtedy wszystkie reguły automatyczne wszystko działa działa nie, no po prostu przypisanie tych 2 kresek powoduje, że jakiś tam radio button jest zaznaczony, no i teraz.  
Na klient się tam no kręci nosem, bo bo nie bardzo mu się podoba. Podobają te 2 kreseczki. Ja wyraźnie powiedziałem klientowi, że no na chwilę obecną musimy tak to obejść, tak?  
I i już no to w takim razie ten.  
Zostawiamy to, jeżeli to on to po wpisywałaś do do zrobienia, no to zróbmy to.

**Kamil Dubaniowski** 28:34  
Czy no zgadzam się tak, no bo jak to jest zwykła lista wyboru, to da się oczywiście dzisiaj rano.

**Lukasz Bott** 28:39  
Tak, jeżeli jest zwykła lista wyboru, to jest da się wyczyścić tak, bo bo bo to jest tam jakiś tych stop tak no.

**Kamil Dubaniowski** 28:42  
Jakaś niespójność?  
Przez dłuższy czas tak było w ankietach na fejsbuku jak skanowałem czasami zaznaczyłem odpowiedź w ankiecie, w której kompletnie nie chciałem brać udziału i później moja odpowiedź, bo normalnie widoczna nie mogę jej usunąć. Później zrobili tylko na iOS, a że się dało oczyścić, a później już prowadzili wszystkim.

**Lukasz Bott** 29:13  
Wniosek nie trzeba korzystać z fejsbuka.

**Kamil Dubaniowski** 29:19  
Podczas tworzenia dasz bordo.  
Jest już na to, ale spodziewam się, że to po prostu oktawia ma tak ustawione, że się wspiął na ten.

**Lukasz Bott** 29:33  
No to tak czy siak to może być te błędy. Ja wiem, że tutaj mamy z tym mydłem raport owym **********, że tak się wyrażę, ale.

**Kamil Dubaniowski** 29:34  
Wersje czerwcowa.  
Wstałem dla mnie i tak nie powiem.

**Lukasz Bott** 29:45  
Jeżeli są jakieś takie błędy, które są ewidentne, a to pewnie jest jakiś tam techniczny błąd tak no to tak czy siak poprawialiśmy to tak.

**Kamil Dubaniowski** 29:55  
Czy tak to na pewno tylko wątpie, że nie ma przestrzeń w tym skręcie.  
Powiedzmy, że jest zostały 2 dni, więc już szkoda odciągać, żeby teraz to wchodziłaby. To nie będzie cały dzień to, że.

**Lukasz Bott** 30:08  
No o k dobrze.

**Kamil Dubaniowski** 30:10  
Wolałbym, żeby skończyła to, co miała w celach sprintu to błędy, wiadomo też, no ale to wpadło w czasie springs. Dobra, to jest ready, to jest mating.  
No i to już są wszystkie chyba od Janusz. No tak.  
Tak, teraz jeszcze moglibyśmy w sumie dogadać, bo ja z tym miałem problem i ostatnio to adrianowi czyściłem, bo oni w ogóle na tym poziom nie zaglądają. To Janusz jakbyście tam mogli się włączyć, będzie oczywiście skupieni teraz.  
Ee szczery, ja zazwyczaj przepisywałem jaki epicki do siebie.  
Czyli ja byłem właścicielem kiczera ja byłem właścicielem lepiku, bo oni nie zaglądali i później te statusy zostawały na nią albo in progress pieczy.  
A więc w momencie, kiedy ja uznawałem, że już skończyliśmy, że już mamy wszystkie PI zrealizowane, no to ja dawałem, nadam.

**Lukasz Bott** 31:04  
No tak chyba powinno być.

**Kamil Dubaniowski** 31:06  
I pytanie, czy tak zrobimy to dalej?

**Janusz Bossak** 31:09  
Wiecie co no to to wolnie, no może być znaczy może być tak.  
Że przy tym nowym sposobie, kiedy ten fixer jest rzeczywiście takim fischerem, czyli funkcjonalnością, która jest dodawana do paczki.  
W rozumieniu tego prezentu to na tym poziomie, czyli pomiędzy i a fischerem to powinien działać deweloper. On powinien stwierdzać, że dostarczam cały ten ficzer tak czyli ten tą zębatkę tym nowym rozumieniu.  
Oni tak nie do końca pracują, bo jak patrzą na backlog to nie patrzą PA jajami tak oni są na tym poziomie pkb i ów.  
Może nie wiem, może uda się ich przekonać, żeby jednak patrzyli nam backlog trochę inaczej jak wprowadzimy te nowe zasady, bo im to odcina. Teraz jak tak robią jak robią odcina ten jeden poziom, czy oni nie widzą tego oficera, czyli po co to robią? Oni patrzą tak wiecie atomową no niby taski do zrobienia a nie po co to taski robią.  
I to jest chyba główny problem, czyli pomiędzy według mnie.  
Według mnie pomiędzy PIMA fischerem to deweloper powinien mówić, zrobiłem wszystkie PIE.  
I to deweloper powinien być odpowiedzialny za ten pojedynczy fitter.  
Natomiast pomiędzy fischer ami, czyli tymi naszymi funkcjonalnościami komponentami czy jak to nazwać, a paczką, czyli tym prezentem teraz na nowo nazwanym.  
To już wy tak, bo to tym musisz stwierdzić każdy z was, czy już mamy wszystkie rzeczy, to wasze zadanie jest popychać deweloperów, że tu słuchajcie, musimy wydać tą paczkę, a jeszcze nie mamy zrobionych.  
Tych funkcjonalności, a w ramach tych funkcjonalności jakiś tam PI ów.  
Więc na tym poziomie pomiędzy oficerami a paczką to według mnie to wy powinniście decydować i stwierdzać tak uznajemy, że wszystko co żeśmy zaplanowali jest zrobione, przetestowany, gotowy do wydania tak i wydajemy tą paczki.  
Ten prezent dostarczamy tak.  
I to idzie do jakiegoś wydania? Tak naprawdę.  
No właśnie tu jeszcze pozostaje to to, co żeśmy rozmawiali tu godzinę temu.  
Czyli.  
Tak naprawdę jakby pojedyncze pb, a je idą do wersji.  
I to jest jeszcze problem.  
No bo mamy jakiś pojedynczy pb i który poszedł do wersji, ale to nie oznacza, że mamy całą.  
Paczkę gotową nie.  
Nawet się to już trzeba by deweloperami pogadać, bo.  
Jakbyśmy wrócili tak do rozmowy sprzed.  
5 może lat?  
To była taka dyskusja.  
Tak jak jak przychodził Adrian mniej więcej wtedy i on tam próbował pierwsze jakieś też zasady z tego screama tutaj trochę bardziej ogarnąć.  
Yy, to tam była szeroka dyskusja na temat.  
Właśnie tego, czego czego dotknęliśmy teraz?  
Bo.  
Może tak powinno być, że.  
Oni otwierają branża.  
Na paczkę.  
Czyli to ten nasz prezencik, tak?  
I w ramach tej paczki.  
Wrzucają te pb, a je.  
I jak zrobili, zrobimy wszystko w ramach tej paczki to dopiero cały ten branż jest albo nie jest mediowa any do persji głównej.  
I wtedy to ma sens.  
Czyli nie idzie tak, że.  
PI od razu jest znaczy inaczej, czyli trochę byłoby na mieszania, no bo nie nie istniałby jeden słuszny develop.  
Tylko by istniał develop kropka.  
Tym branż.  
Na przykład ten ma koles.  
I dopóty, dopóki nie zostaną zrobione wszystkie zadania z tego.  
Obszaru.  
To całej tej paczki nie meldujemy do głównej gałęzi.  
I to jest rzecz, którą wtedy te 5 lat temu właśnie chciałem osiągnąć.  
No i właśnie był ten argument, który tu podałem na początku tej wypowiedzi, tak znaczy, że.  
Jemy pojedyncze Birmie.  
I w ten sposób mamy bajzel nie no, bo mamy 5 z 15 pb i ów, które dotyczą jakby tej wartości, którą chcemy dostarczyć.  
No i mamy jeszcze mamy 3 zupełnie z innej paczki.  
I 2 jeszcze z innej paczki.  
Bo każdy coś tam swojego melduje i ogólnie mamy wieczny bałagan, a gdybyśmy się trzymali tego poziomu minimalnej paczki dostarczanej, to jeżeli w środku siedzi 5 10 20 pb i ów to one się mężu ją do tego branża, czyli do tej paczki na tym poziomie powinien być branż robiony.  
I dopiero na tym poziomie stwierdzamy, czy to się da, czy to się nie da zmarnować. Ja wiem, oni będą zaraz narzekać, że to są za duże kawałki, że potem się tego nie da z mediować, bo to tyle zmian może być i tak dalej, i tak dalej to jest problem deweloperów, niech się nad tym zastanowią, jak to robić.  
Ale to.  
To by nam po prostu pięknie uprościło tak czyli.  
Mamy sytuację następującą, robimy jakąś funkcjonalność?  
Dostarczamy jakąś paczkę.  
Już widzę ich sprzeciw, bo Jezus już widzę to.  
No ale jakąś paczkę dostarczamy powiedzmy.  
No strona, logowanie.  
I tam jest ileś rzeczy w tym w ramach tego i oczywiście ta paczka znowu to jest kluczowe, ona powinna być odpowiednio mała.  
Tej mojej filozofii, którą z tym sztucznym?  
Dziś miałem, omawiam i on to ciągle podkreśla, że to musi być odpowiednio małe, to to nie może być worek funkcjonalności.  
To jest wartość, którą dostarczamy.  
I minimalna wartość, powiedzmy, że to jest strona logowania.  
Na przykład bez strony.  
Zmiany hasła bez strony czegoś tam jeszcze tak jest, ale Użytkownik może się zalogować już według nowej.  
Stron to dostarczamy tomer czujemy, bo to jest ta nasza minimalna paczka i to weszło już na produkcję, ale weszło albo całe albo nic.  
A nie, że ktoś zmienił.  
Nie wiem.  
Jakąś jedną rzecz jakiegoś PA ja jednego zrobił i to już jest marihuana.  
Tak rozumiemy.

**Damian Kaminski** 39:18  
Tak to znaczy, no według mnie.  
To też nie jest tak, że tego nie robimy. Poniekąd tak robimy, bo.  
Po to są te ich lokalne branże.

**Janusz Bossak** 39:30  
No trochę tak.

**Damian Kaminski** 39:30  
Gdzie my możemy już coś przetestować, ale w zasadzie nie ma konieczności, jeśli jest to nowy ficzer właśnie, czyli jakieś nowe zagadnienie, to nie ma konieczności już budowania tego do głównego wątku, bo to nie trzeba tutaj powiedzmy dbać o kompatybilność i tak dalej, tylko możemy na razie dalej kontynuować, a wydamy to już w całości, ale testy jednocześnie mogą się w międzyczasie odbywać na branżach lokalnych, więc no to nie jest takie totalne novum.

**Janusz Bossak** 39:55  
No tak, trochę branż lokalnym, no no no słusznie. Słusznie zauważyłeś branż lokalny jest w pewnym sensie takim właśnie brałem tylko, żeby był rzeczywiście nakierowany na tą pojedynczą paczkę wartości. Nie, to jest ludzie tam nie mieszali różnych rzeczy, zresztą starają się z tego co.  
Widać no bo jak robi coś innego no to robi nowy branż, nie ma tam na ania jeden na ania 2 tak czy tam? Przemek, jeden Przemek 2.  
No i o k to są te właśnie dodatkowe.  
Poziomy, które możemy tutaj wyróżniać.  
No dobra, no też.  
Po części to działa, więc nie jest taka wielka rewolucja.  
A jakie było pytanie Kamil, bo tak odbiegliśmy.

**Kamil Dubaniowski** 40:50  
Kto ma być właścicielem? Na poziomie wcieraj epika.

**Janusz Bossak** 40:52  
A no to tak, no to już.  
To chyba.

**Damian Kaminski** 40:56  
Według mnie my opiekun biznesowy, bo jednak fischer zamykam my.

**Janusz Bossak** 41:07  
Czy teraz tak jest? Ale wydaje mi się.  
Że jak przy tej nowej jakby nomenklaturze?  
To ten ficzer to powinien domykać deweloper.  
To powinno być zadanie jego nadany tam sprint czy na dany dzień.  
Zrób to.  
Tak, a w ramach tego są tamte 3, powiedzmy PI, nie, nie on tam robi, robi, robi i mówi, zrobiłem to wiozłem ten ficzer w całości.  
To jeszcze nie jest paczka, tak, to nie jest ten prezent.  
Ale pojedyncza rzecz to jest zrobione. Teraz biorę się za coś następnych albo ktoś inny robi coś następnego, tak coś innego.  
I tak jak mówisz, no może być tak, że na razie wy, ale docelowo według mnie deweloperzy.

**Damian Kaminski** 42:01  
O k.  
Dobra, czy mamy coś jeszcze? Ja bym tym czasie jeszcze zacząłem sprawdzać to, co powiedzieliście.  
To tak szybciutko tylko.  
Daje się to zrobić, w sensie mamy takie pozycje.  
Trójka tylko to wymaga i znika to trójka tylko no nie jest to poprawne, więc według mnie powinniśmy iść w tym kierunku, bo dzisiaj da się tak zrobić, ale przez wywołanie sejf. Case w regule automatycznych, które powoduje zbędne połączenie z bazą. Tak więc tak jak widzicie trójka, o ile tu coś mam wpisane.  
Albo inaczej trójka i sobie działa ta trójka.

**Lukasz Bott** 42:50  
Dobra, wiesz co? Dzięki za to jest?

**Damian Kaminski** 42:51  
Natomiast jak jak coś wprowadzę i przejdę tam dalej, no to jednak ta trójka znika. Ale no skoro tak się da, to według mnie powinno się dać też po prostu zdjąć, bo to jest tylko frontend tak, że to spadnie to zaznaczenie i tyle.

**Lukasz Bott** 43:06  
Ale użyłeś sobie w kolejce?

**Damian Kaminski** 43:07  
Ale używam sobie kasę, no więc to jest złe podejście w kontekście optymalne ności. Natomiast no właśnie kojarzyłem, że jakieś tam.  
Jakoś to kiedyś działało.

**Lukasz Bott** 43:17  
Znaczy, wiesz, dobra, dzięki za te testy robisz się na nowo.  
Formularzu tam jeszcze jest poprzedni ster, formularz, więc.

**Damian Kaminski** 43:27  
Stary, no to musisz sprawdzić. No nie będę się upierał.  
Ale po prostu wymaga to odświeżenia.

**Lukasz Bott** 43:34  
To znaczy.

**Kamil Dubaniowski** 43:46  
Wyceny jakieś nowe rzuciliście okiem czy byłyby niepotrzebne szczerze mówiąc.

**Damian Kaminski** 43:50  
Ja też nie już patrzę.

**Lukasz Bott** 43:51  
Nie chyba wycen nie ma.

**Damian Kaminski** 43:57  
Nie ma bez opiekuna, nie ma żadnych.

**Lukasz Bott** 43:57  
Nowe.  
I jeżeli się pojawiają, to na ogół trafiają do grupy, więc siłą rzeczy.  
Wiedźmin.  
To znaczy, ja widzę to jak nowy wpadają tu widzę i nie jest to przypisane. Tak no to widzę u siebie do wykonania, tak.  
Się do wykonania po prostu.

**Damian Kaminski** 44:17  
No jest ten ta kwestia tej historii spraw powiązanych, natomiast czekam tu na Kacpra, bo.  
Rozmawiałem z nim.  
Przedstawiłem właśnie ten kontekst, który ty Kamil zaproponowałeś, że może to być.  
Historia faktycznie spraw powiązanych, ale w zasadzie. No właśnie pierwsze pytanie powinno być postawione po co im to jest potrzebne i on to ma ustalić.  
Z klientem i właśnie może tutaj ten moduł historii biznesowy był możliwy do rozwinięcia odpłatnie.

**Lukasz Bott** 44:58  
Dobra.  
Termin chyba temat fajnych tak no to kończymy tak nie jesteśmy i tak w jakimś.

**Janusz Bossak** 45:09  
Dobra.  
Bardzo hejka.

**Lukasz Bott** 45:11  
W kontakcie bieżącym nam cześć.

**Janusz Bossak** zatrzymano transkrypcję
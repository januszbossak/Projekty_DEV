**Data spotkania:** 30 października 2025

**Damian Kamiński:** Cześć.

**Janusz Bossak:** Część.

**Damian Kamiński:** No dobrze, to zacznijmy, Kamil pewnie zaraz dołączy. Czy mnie słychać?

**Janusz Bossak:** Słychać, tak. My cię słyszymy.

**Damian Kamiński:** Dobra, no to będę działał. Piotr, tutaj informacja – moje przypuszczenie co do tych adresów. Ponieważ to jest szkolenie robione przez Comarch za darmo, więc jest robione dla partnerów Comarchu. Prawdopodobnie Przemek nie chciał ujawniać adresów i wszystkim po prostu „na pałę” przypisał adresy astrafox.pl, żeby nie było jakiegoś zamieszania.

**Piotr Buczkowski:** No to niech teraz dorobi skrzynki pocztowe w domenie astrafox.pl.

**Damian Kamiński:** Albo aliasy przynajmniej. Adrian sprawdzał i mówił, że nie działa. W sensie Adrian zrobił test dzisiaj.

**Piotr Buczkowski:** Znaczy ja mam skrzynki w obydwu, ale mam dwie skrzynki, tak? Jak pamiętam, to czasami je sprawdzam, w AMODIT-cie zwykle nie.

**Damian Kamiński:** Trzeba by mu przypomnieć pewnie.

**Janusz Bossak:** Wiesz, on ma świadomość tego. Pogadam dzisiaj z nim jeszcze. Dobra, ale wracajmy tutaj.

**Damian Kamiński:** Dobra, to tak. Piotr, jak skończymy Radę, bo teraz chciałbym, żebyś był tutaj skupiony... Tam jest problem, w AMODIT-cie odpala się pula aplikacji. Założyłem wątek na AMODIT Services, zrzuciliśmy logi z Endur [system klienta - przyp. red.], ale ja nie mam pomysłu, więc jakbyś mógł tam wesprzeć jakimś słowem komentarza, co szukać i gdzie?

Dobra, to teraz tak – ten temat był zawieszony. Nie wyszukuje spraw, coś jest nie tak z Lucene w przypadku administratora. Poprosiłem jeszcze Tomasza, który jest twórcą tego zgłoszenia, żeby w Repro Steps opisał dokładnie to, co się dzieje, bo to jest mega nieczytelne. Wrzucił tutaj pełno screenów, ale które czytać, w jakiej kolejności? Mam nadzieję, że to uzupełni. Natomiast w skrócie: jeśli ktoś jest twórcą sprawy i jednocześnie administratorem, to mu po prostu nie działa wyszukiwanie po Case ID. A jak nie jest administratorem, to działa.

**Piotr Buczkowski:** A ze wszystkich zakładek?

**Damian Kamiński:** Nie wiem. Nie zadałem takiego pytania. Czy z zakładki "Wszystkie" sprawdzić dla pozostałych?

**Janusz Bossak:** Trzeba przejrzeć, słuchajcie, to wyszukiwanie, bo ja też mam wrażenie, że to czasami działa dziwnie.

**Damian Kamiński:** Tak, tak sugerujesz, żeby sprawdzić wszystkie zakładki?

**Piotr Buczkowski:** No to jest pewien zewnętrzny komponent. Znaczy na Wiki jest cały artykuł, kiedyś napisałem jak diagnozować indeksy Lucene. Napisałem się i tak do mnie to wraca.

**Damian Kamiński:** Nie no, to okej. No to skoro to jest to...

**Piotr Buczkowski:** Znaczy nie wiem, czy ktoś tam...

**Janusz Bossak:** A nie jest to odbudowa indeksu?

**Piotr Buczkowski:** Nie, nie, nie, to nie jest odbudowa. Dobrze, w Searchu szukaj. Nie w tym "skecz", tylko w tym ogólnym. Bo robiliśmy restart indeksów procesu.

**Damian Kamiński:** Jak to zrobić? Coś trzeba pobrać? Okej. Czyli chcesz taki wynik? Pytanie, czy on już tego nie zrobił? Bo on już coś takiego tu wrzucił. Czy to nie jest to?

**Piotr Buczkowski:** Tak, to jest to. To trzeba odpalić z poziomu Luke'a i zobaczyć, czy nie zwraca wyników. Jeżeli nie zwraca wyników, to trzeba zmodyfikować to zapytanie, aż będzie zwracać wynik.

**Damian Kamiński:** No dobra, no to niech podziała. Jak będzie miał problemy, to najwyżej się do mnie odezwie. I tyle.

Dobra, teraz pytanie, którego nie ma, natomiast które chcę tutaj z wami poruszyć. Czy takie zgłoszenie należałoby zrobić? Mamy sytuacje takie jak skończenie się limitów OCR. Ostatni przypadek z Orlenu – skończyła się przestrzeń na dysku i system nie mógł zapisać dokumentów. Są pewnie też inne przypadki, które w mojej ocenie powinny skutkować niezwłocznym wysłaniem maila do administratorów systemu. Po to, żeby był taki pierwszy krok do self-healingu. Coś nie działa, biznes zgłasza, a działa jakiś job, który wskutek określonych logów od razu daje diagnozę. Ktoś zacznie szukać, ale w międzyczasie dostanie maila, że przyczyną jest to i to. Co wy na to, czy coś takiego opisać? Pewnie trzeba będzie to rozbudować na większą ilość przypadków niż te dwa, które powiedziałem.

**Janusz Bossak:** Mam jeszcze jeden, czyli skończył się limit OCR-a wczoraj.

**Damian Kamiński:** Tak. No to jest to, co powiedziałem – pierwszy: koniec limitu OCR, drugi: koniec przestrzeni na zasobie. Pewnie są jakieś inne.

**Janusz Bossak:** Powinno ostrzegać. I to powinno ostrzegać, zanim się to wydarzy, a nie jak się wydarzy.

**Damian Kamiński:** To znaczy ja bym sugerował tak, że w momencie wydarzenia i potem codziennie. O jakiejś godzinie, na przykład 7:00 rano, na rozpoczęcie pracy, żeby to wskakiwało na górę skrzynki. Co wy na taki pomysł? Czy mam go wstępnie rozpisać?

**Piotr Buczkowski:** Halo, zaraz, zaraz. Co mamy robić, żeby wysyłać informację, że nie ma miejsca na dysku?

**Damian Kamiński:** Jeśli nie można zapisać pliku, to powstaje błąd w logu.

**Piotr Buczkowski:** Tak. Jak ktoś będzie te błędy analizował.

**Damian Kamiński:** Dlaczego tak uważasz? W sensie – dochodzi do zdarzenia w dniu dzisiejszym, że kończy się miejsce na dysku. Nikt nie spojrzał, nie sprawdzał, nie wchodził na zasób sieciowy, że tam kończy się miejsce. No i dochodzi do tego zdarzenia, więc wysyłany jest mail do wszystkich administratorów systemu, że skończyło się miejsce na dysku i nie można zapisać kolejnych załączników.

**Janusz Bossak:** To jest... no to w ogóle to zdarzenie to jest On-Premise.

**Piotr Buczkowski:** My nie wiemy, że się skończyło miejsce na dysku, bo wiemy [tylko], że się nie da zapisać na dysku. Jeżeli to dysk sieciowy, to niekoniecznie [brak miejsca]. Brak dostępu do dysku sieciowego.

**Damian Kamiński:** No właśnie, no to też jest kluczowe, tak? Bo wtedy jest nieskuteczne zapisywanie, ktoś musi niezwłocznie podjąć działania, bo biznes stoi. Nic nie można zapisać, wszystkie maile, które idą, stoją, niewczytywane są faktury itd. Więc uważam to za taki pierwszy krok do self-healingu, że nie idzie do nas pytanie do serwisu "co się stało, gdzie mamy szukać, o co chodzi, czemu AMODIT nie działa", tylko ten administrator od razu dostaje informację.

**Piotr Buczkowski:** Tak. Są do tego narzędzia zewnętrzne, trzeba po prostu zainstalować i skonfigurować.

**Damian Kamiński:** No dobra, tu mówisz o narzędziach zewnętrznych. Inny przypadek, który też by to wykorzystywał, to ten co powiedział Janusz i ja wcześniej, czyli skończenie się limitów OCR. No i pewnie jeszcze kolejne takie przypadki.

**Piotr Buczkowski:** Dobrze, okej. Jak najbardziej możemy dodać takie wysyłanie maili w zdefiniowanych przypadkach.

**Damian Kamiński:** Dokładnie. To będziemy sobie ustalać, co jest na tyle krytyczne, że właśnie należy powiadamiać administratorów, a co jest po prostu logiem.

**Piotr Buczkowski:** No to po prostu w pewnych miejscach dodać wysyłanie natychmiastowe maila. Oczywiście w ten sposób nie zdiagnozujemy braku dostępu do serwera pocztowego.

**Damian Kamiński:** No tak, to jest jeden wyjątek, którego nie zrobimy. Ale to trudno.

**Piotr Buczkowski:** Znaczy kiedyś był pomysł, żeby wyświetlać to administratorowi jakoś czerwony pasek w AMODIT-cie.

**Janusz Bossak:** Tak, tak, tak, dobrze by było.

**Damian Kamiński:** Znaczy wiecie co, to jest kolejny krok, tylko to najpierw musi zaopiekować Kamil pod kątem 4-eyes [four eyes principle - przyp. red.] i według mnie tak, zgadzam się. To bym robił niezależnie od maila. Może nawet powinien być pod to jakiś parametr – czy wysyłać maila, czy dawać powiadomienia w interfejsie, czy oba. I wtedy niezależnie od tego, w interfejsie może zawsze tutaj te powiadomienia byłyby pod takie "Uwagi dla administratora", czy jakkolwiek to sobie nazwiemy tę zakładkę. I tutaj też by się to pojawiało. Dokładnie to samo co w mailu. Czyli ktoś wchodzi i od razu tutaj na twarz dostaje, że jest jakieś powiadomienie systemowe do administratora i zanim rozpocznie działania, powinien się z tym zapoznać.

Dobra, no to mamy wytyczne. Ja przygotuję na ten temat jakieś PBI.

(...)

**Damian Kamiński:** Dobra, Kamil coś pisał, że go nie będzie. Kojarzycie?

**Janusz Bossak:** Nie wiem.

**Damian Kamiński:** No dobrze, mamy przypisane. To jest u Ani, to zostaje. "Dodać logowanie informacji o osiągniętym limicie" – to jest u Mateusza. To jest zbieżne z tym, co już mamy – taki pierwszy kroczek, który Mateusz ma obsłużyć. Właśnie to mówiliśmy – brak powiadomień mailowych do adminów systemów. To wszystko, co wymieniłem, to już jest omówione, a tu na razie Mateusz jako takie totalne MVP robi wpis do loga taki, który informuje, że ten limit się wyczerpał. Bo w tym momencie odpowiedź jest taka, że nie wiadomo o co chodzi, więc to jest jakieś tam pierwsze usprawnienie.

No dobrze, te tematy, które są przypisane do sprintów albo jest na Feedback Board... te są już omówione, więc możemy po prostu kontynuować po klientach. To już było mówione we wtorek – odepnę to z rady.

**Piotr Buczkowski:** Znaczy przydałoby się w końcu uwspółcześnić ten mechanizm [drukowania].

**Damian Kamiński:** Co masz na myśli?

**Piotr Buczkowski:** No ten Print – wersja do wydruku jest sprzed 10 lat. Prawie niezmieniana.

**Damian Kamiński:** Ale działa. Celem naszym nie jest tak naprawdę drukowanie spraw, no to jest jakiś skrajny przypadek. Ja dałem Patrykowi rozwiązanie. Na ten moment zostawiłbym to, po prostu zróbmy do tego minimalną dokumentację. Jak ktoś będzie chciał to poprawiać, to niech to sponsoruje, bo to nie jest nasz cel, żeby sprawy były drukowane. Więc no zgadzam się z tobą, że jest to stare, natomiast to nie jest na naszej liście priorytetów.

Dobra, dalej mamy Allianz/Wien – to jest moje zgłoszenie. Dobra. Przyznam, że nie pamiętam, czy to było omawiane na Radzie, więc po prostu wam to przedstawię jak to widzę. Jeśli mamy przypadek źródła typu Static, które no będzie coraz częściej wykorzystywane w kontekście źródła dynamicznego, czyli uzupełnionego regułami. Sytuacja jest taka: tworzymy sobie jakieś źródło, wgrywamy do systemu mapując zgodnie z nazwami kolumn, zapisujemy. I teraz, jeśli wgrywamy źródło jeszcze raz – wchodzimy w "Mapuj", to się automatycznie przypisuje tak jak było, bo źródło się nie zmieniło, więc on to zapamiętuje. Klikamy następnie "Zapisz" – efekt jest okej. Jak nie wejdziemy w "Mapuj", czyli tego kroku nie zrobimy i klikniemy "Zapisz", to w zasadzie wszystko zmienia się na LongText.

**Piotr Buczkowski:** No to jest domyślnie. Tam jest jakiś błąd po prostu, tyle.

**Damian Kamiński:** Tak, tam jest błąd. Wystarczy tylko wejść w "Mapuj" i wyjść, i to już jest przypisane tak jak było.

**Piotr Buczkowski:** Tak mówię, to jest błąd, po prostu trzeba poprawić błąd. Jeżeli już jest mapowanie, to powinien użyć.

**Damian Kamiński:** Dobra. Przypominam podejścia mamy cztery, ale powiedzmy pewnie z dwa wystarczy wybrać. Najprostsze, pewnie te, które proponuje Piotr: jeśli nie wejdziemy w "Mapuj", to przypisuje do tych samych kolumn to co było, a wszystkie nowe przypisuje jako LongText. Możemy też w jakiś sposób ostrzegać, czyli nie damy możliwości kliknięcia "Zapisz", póki ktoś nie wejdzie w "Mapuj".

**Anna Skupińska:** W takim razie to nie powinno być zbyt skomplikowane do zrobienia, skoro powinien po prostu użyć mapowania, którego nie używa.

**Piotr Buczkowski:** Może jakoś wyświetlać... że jeszcze jest domyślne mapowanie... Według mnie powinno się pojawić tutaj podsumowanie tekstowe mapowanych kolumn.

**Damian Kamiński:** Możemy wystraszyć ten przycisk, w sensie dać go _disabled_ i napisać obok "Przejdź krok mapowania".

**Piotr Buczkowski:** To równie dobrze możemy wyświetlić to okienko od razu. Wybierasz plik i wyświetla się to okienko. Nie ma sensu czekać.

**Damian Kamiński:** Masz rację, możemy tak zrobić, to będzie najprostsze, najmniej zmian. Nie wiem tylko co się stanie, jak kliknę "Zamknij". Czyli mam tutaj plik, klikam "Zamknij", nie klikam "Zapisz"... No więc wszystko jest LongText, więc pytanie, czy nie pozbyć się przycisku "Zamknij"? Bo on powoduje tylko problemy.

**Piotr Buczkowski:** Nie "Zamknij". Jeżeli na przykład wybrałeś zły plik, pomyliłeś się, widzisz, że to całkiem inne kolumny... Ewentualnie "Anuluj" dodać.

**Damian Kamiński:** No dobra, czyli zmieniamy kontekst. Podsumowując: klikamy "Wybierz plik". Po wybraniu pliku od razu przechodzimy do tego okienka mapowania i tu mamy "Zapisz", które potem pozwala przejść dalej, albo "Anuluj", które kasuje plik.

**Anna Skupińska:** Ciekawa jestem, czy użytkownik będzie wiedział, że jak kliknie "Anuluj", to plik się nie wgra. Bo wcześniej tak nie było. Będą nam klienci narzekać, że "o, nie działa wgrywanie plików".

**Damian Kamiński:** Nie no, ale naturalnym jest to, że jak wgrywam plik, wyświetla mi się jakieś kolejne okienko, to jeśli chcę iść pozytywną ścieżką, to klikam "Zapisz".

**Piotr Buczkowski:** Tutaj bardziej się obawiam, że mamy dwa razy "Zapisz". Niech tu będzie po prostu "Wczytaj". Czym to poskutkuje? Wczytaniem danych.

**Damian Kamiński:** Czyli w zasadzie po kliknięciu przycisku "Wczytaj" ten plik z automatu znika, bo już się wczytał [do tabeli].

**Piotr Buczkowski:** Tak, z podanym mapowaniem.

**Damian Kamiński:** Dobra, słuchajcie, żebyśmy teraz nie obsługiwali tego dziesięcioma nowymi wymaganiami. Na razie skupmy się tylko na tym, żeby nie rozwalać. Tak jak teraz omówiliśmy, to jest już ostatecznie: zmieniamy przycisk na "Wczytaj" i to powoduje wczytanie tego pliku. Alternatywnie "Anuluj" czyści plik i trzeba rozpocząć od początku.

**Piotr Buczkowski:** No dokładnie.

**Damian Kamiński:** Dobra. Dalej mamy Niden – problem z otwieraniem raportu, nowy moduł raportowy. Tu pytanie Aniu, jak to zgłoszenie? Ania, jak na jakim etapie jest zgłoszenie błędów SQL z nowych raportów?

**Anna Skupińska:** Jeszcze tego nie zrobiłam, zajmuję się hotfixami.

**Piotr Buczkowski:** Ale w nowszej wersji już jest zrobione chyba. Sprawdzaliśmy to kilka miesięcy temu.

**Anna Skupińska:** Tak, to było zrobione. To było zgłoszenie, żeby się trochę upewnić, że to jest już zrobione i żeby to we wszystkich miejscach [było].

**Damian Kamiński:** Dobra, zamknijmy to zgłoszenie. Prośba Aniu, jak skończysz hotfixy, to żeby zająć się tym. To ma priorytet pierwszy. Potwierdźmy, że to jest. Jeśli nie ma, to uzupełnijmy to, żebyśmy tego typu błędy mogli rozwiązywać na poziomie loga. Odpinam to w takim razie z Rady.

To jest ten błąd, Piotrze, to odkryliśmy od ciebie. AMODIT do AMODIT-a, wywołanie reguły, która jest funkcją, ma walidowany ten element, że sprawa jest zamknięta, mimo że to jest funkcja i przez to nie da się wywołać. Trzeba to obsłużyć. Jeszcze dopiszę tutaj twoje zalecenie: dla funkcji nie powinno być to walidowane.

Dobra, idziemy dalej. "Nowe raporty, filtr użytkownika, opcja zaznacz wszystko nie zaznacza wszystkiego". Okej, nie zaznacza wszystkiego, bo nie wszystko jest załadowane. Na tym polega problem. Przycisk "Zaznacz wszystko" ma się pojawiać tylko w momencie wprowadzenia wartości powodującej przeszukanie. Dodatkowo po zaznaczeniu "Zaznacz wszystko" i kliknięciu "Zastosuj", walidujemy czy lista wyświetlała wszystkie pozycje. Jeśli nie, to wyświetlamy okno z informacją, że tych pozycji jest więcej i należy zawęzić zakres wyszukiwania do maksymalnie 100 pozycji.

**Anna Skupińska:** Jeśli chodzi o wydajność, to dostanę wszystko... Jeżeli robisz "zaznacz wszystko", ten filtr w zasadzie nic nie robi, bo pozwala ci zobaczyć wszystko.

**Damian Kamiński:** Nie, nie, źle to zinterpretowałaś. "Zaznacz wszystko" pojawia się tylko w momencie wprowadzenia wartości powodującej przeszukanie. Nie ma "zaznacz wszystko" po kliknięciu [bez wpisywania]. Jeśli zaczynasz wpisywać jakąś wartość, a ona ma tak dużo pozycji, że się nie wyświetlają, wtedy to "zaznacz wszystko" ma sens.

**Anna Skupińska:** Rozumiem.

**Janusz Bossak:** Tutaj Damian, pamiętasz, nie wiem czy to jest dokładnie to samo, ale temat Przemka, gdzie mieliśmy 3 [elementy], a wyświetlały się 2?

**Damian Kamiński:** Tak, dokładnie. Nie wiemy jak generowane są te checkboxy.

**Janusz Bossak:** Legenda, która się wyświetla jak się ją włączy, pokazuje prawidłowo te 4 wartości. Czyli wykres czy tam raport wie o nich, czyli ma dane, a we filtrze tego nie ma.

**Damian Kamiński:** Tak, bo tak jak mówię, według mnie po prostu ten filtr bierze distincta na powiedzmy 100 pierwszych rekordach, niezależnie od typu raportu. Jeśli raport jest agregowaniem kolumn do na przykład jakiejś firmy i w pierwszych 1000 rekordach, na podstawie których generuje się ten raport, nie było tej trzeciej firmy, no to wyświetliły się dwie. Dlatego Aniu mówię, że właśnie w tym przypadku teoretycznym nie wyświetlamy tu wszystkiego, dlatego tu właśnie nie da się zaznaczając wykryć, czy ty masz więcej niż 100. Przynajmniej dzisiaj.

**Janusz Bossak:** To jest najbardziej denerwujące, że są 2 czy 3 elementy i z jakiegoś powodu jednego nie wyświetla.

**Damian Kamiński:** Dobra Aniu, to umawiamy się tak. Przypisuję to na kolejny sprint, czyli 45. Zadanie: przeanalizowanie i przedstawienie na kolejnej Radzie, na jakiej podstawie budowana jest lista w checkboxach filtru. Wtedy ustalimy kroki działania.

Dobra, Polpharma. Według mnie to już jest rozpisane. To były wytyczne Security od Polpharmy, żeby pokazywać równoległe sesje po zalogowaniu. Pytanie na ile traktujemy to jako istotne?

**Kamil Dubaniowski:** To nie jest tak, że ja nie wiem co robić, tylko nie mamy zaopiekowanych projektów. Ja mam za dużo, bo jeszcze dostałem wczoraj 3 tematy od Lucyny z ministerstw do wyceny, także ja i tak się nie wyrobię.

**Damian Kamiński:** Ja rozumiem. Mocno to uprościłem, przepraszam.

**Janusz Bossak:** Tutaj w międzyczasie wam pokażę przykład. To jest projekt, który tam Przemek przygotował "Projekty Sprzedaż 2025". Ja wiem, że tu są RPT. Jest RPT, klikam... i są projekty. Czyli mając taką sytuację jak tutaj, kiedy nie wpiszę RPT, nie wiem, że jest RPT. Nawet jak zaznaczę wszystko, to ten RPT się oczywiście nie zaznacza. I to jest zadziwiające. To nie jest kwestia, że tu już była tak długa lista. Są dwa elementy. Dlaczego nie ma trzeciego?

**Damian Kamiński:** Dobra, omówmy to na przyszłej Radzie. W sensie teraz Aniu masz zwizualizowany problem bardzo dosadnie. Rado, proszę o jednogłośną decyzję, co z tym [Polpharmą] robimy? Czy wrzucamy to na backlog, aż ktoś to podbije?

**Piotr Buczkowski:** Jeżeli mamy co robić, to zostawiamy na razie.

**Damian Kamiński:** Dobra, tutaj w ogóle nie wiem co to za klient. Świeży temat – Amadeus. Problem z dodaniem grupy do pola "Redaktorzy spraw".

**Piotr Buczkowski:** Pewnie o to chodzi, że w cudzysłowie w nawiasach jest login.

**Kamil Dubaniowski:** Dokładnie. Mi się wydaje, że ja to testowałem i chyba jest okej, kiedy ta nazwa z nawiasami jest jako nazwa wyświetlana. Więc jeśli ta systemowa nazwa grupy jest bez nawiasów, to wydaje mi się, że działało.

**Damian Kamiński:** Bo tu jest wyświetlana nazwa techniczna.

**Kamil Dubaniowski:** Czyli tak, w mojej opinii działa. Jak potrzebują tych nawiasów, to niech je ustawią w nazwie wyświetlanej.

**Damian Kamiński:** Dobra, co w takim razie z tym robimy?

**Kamil Dubaniowski:** Uważam, że jak damy na backlog, to i tak o tym zapomnimy. Nazwa systemowa w ogóle powinna być na wszystkich poziomach zablokowana z jakiś dziwnych znaków, ewentualnie podłoga i nic więcej.

**Damian Kamiński:** Dobra, poszło. Następne twoje Kamil. RegEx?

**Kamil Dubaniowski:** Tak. Ja rozumiem to tak, że w momencie, kiedy ma dzielić dokument po kodzie kreskowym, ze zgłoszenia wynika, że jeśli nie rozpozna żadnego kodu kreskowego, to w ogóle nie zakłada sprawy.

**Damian Kamiński:** Według mnie powinno założyć jedną.

**Kamil Dubaniowski:** Założy po prostu zbiorczą, tak?

**Janusz Bossak:** Tak, całą masę tych stron w jedną.

**Damian Kamiński:** Jedyne co, to zacząłem rozkminiać jak to w ogóle działa. Rozpisałem trzy przypadki. Może być tak, że dokument nie ma żadnego kodu – w tej sytuacji po prostu na podstawie tego dokumentu zakłada jedną sprawę. Może być tak, że nie rozpozna kodu, ale kod jest – no to po prostu nie dzieli, nadal skleja to jako część poprzedniego dokumentu.

**Piotr Buczkowski:** Bo on ma tylko dzielić po podanym kodzie. Chodzi o to, że na przykład na stronie może być kilka kodów kreskowych, ale nas interesuje tylko ten podany w schemacie. Jak nie znajdzie żadnego, to po prostu powinien nie podzielić. Jeżeli tak nie jest, czy jest błąd, to jest błąd, trzeba poprawić. Możecie mi to przypisać. Ja to nawet dzisiaj poprawię.

**Damian Kamiński:** Przypisywać od razu? Okej. Kamil, jak Piotrek będzie to robił, to jak będziesz miał jakiś już przygotowany przypadek testowy, to im podlinkuj.

**Piotr Buczkowski:** Jest takie jedno zgłoszenie, które stworzyłem w tym tygodniu. Numer 22431. Żeby tak to testować. Chodziło o to, że przy wysyłaniu przez pewien serwer ten plik jest tak formatowany, że nazwa jest w taki sposób... Tak jak wyślę z innego serwera, to nazwa jest w Queście inaczej formatowana i już problemu nie ma. Trzeba dla tego konkretnego EML-a testować. Chodziło chyba o średnik w nazwie pliku. Dzielił na dwie linijki nazwę pliku, a jak dzieli na dwie linijki to dzieli średnikiem. A priori był średnik w nazwie.

**Damian Kamiński:** No dobra, podpiąłem to. Opisałem, że tutaj jest wzorzec, jak to testować. Dobra, bo już jest jedenasta. Trochę wyczyściliśmy, będziemy w przyszłym tygodniu kontynuować. Dzięki.

**Kamil Dubaniowski:** Dzięki.

**Piotr Buczkowski:** Cześć.

**Damian Kamiński:** Cześć.

**Anna Skupińska:** No cześć.
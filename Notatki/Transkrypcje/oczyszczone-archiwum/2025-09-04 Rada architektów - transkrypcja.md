**Rada architektów 2025-09-04 - Transkrypcja**

**Data:** 2025-09-04
**Uczestnicy:** Anna Skupińska, Łukasz Bott, Janusz Bossak, Damian Kamiński, Piotr Buczkowski, Adrian Kotowski

---

**Anna Skupińska:** Yes. Yes, there's another developer.

**Łukasz Bott:** It's. Yeah, it's.

**Janusz Bossak:** And.

**Damian Kamiński:** Czyli jesteś współpracownikiem, to żeby się to wyświetlało w Twojej zakładce "Do wykonania", a w innych nie. Na razie mam ustawienia globalne. No i jest pomysł, żeby to przenieść, ale to powiedziałbym, że nie jest pilne. WIM jest bardziej krytyczne i ja bym to im też wycenił. Mamy to na poziomie głównym. Powiedziałem, jak to ewentualnie rozwiązać konfiguracyjnie Mateuszowi, ale powiedział, że to jest tyle roboty, bo tam jest multum procesów i tak dalej, że nie chce się tego podejmować. No właśnie, ale w sensie tyle roboty to się wiąże z kosztami, więc według mnie normalnie, jeśli Piotr oszacowałby jaki to jest nakład, to można niezależnie od tego, czy wyjdzie, możemy też dać gwiazdkę, bo Piotr to ma obawy co do wydajności. Możemy im to wycenić, zapytać, czy oni w ogóle są w stanie taką kwotę X zapłacić? I jeśli tak, no to możemy podjąć próbę testów. A czy to się powiedzie, czy nie? No to dam odpowiedź.

**Piotr Buczkowski:** Znaczy na tej zasadzie, że można włączyć na wybranych procesach. Tak, myślę, że tak, bo tam jest teraz po prostu `JOIN` czy `UNION`. `Work Case` czy [niezrozumiałe]. To może być `IN`, tak. To nie będzie problemu, ale zrobienie odwrotnie, że wyjątków, że dla tych nie wysyłaj, to nie.

**Damian Kamiński:** Nie no to przecież już wiesz, mówimy na skali procesu, więc wyłączają globalnie, wtedy mogą.

**Piotr Buczkowski:** Czyli albo jest ustawione w ustawieniach systemowych dla wszystkich, albo dla kilku konkretnych procesów.

**Damian Kamiński:** OK. Kilka konkretnych, może na przykład w skrajnym przypadku dotyczyć wszystkich bez jednego. Czy wtedy jest źle.

**Piotr Buczkowski:** Jeżeli będzie 100 procesów, może być problem.

**Damian Kamiński:** OK. No dobrze, to ja tak porozmawiam z Mateuszem, żeby on dokładnie określił, jaka to jest skala, żeby on to policzył? Ile tych procesów w taki sposób chce obsłużyć.

**Piotr Buczkowski:** Dobrze, OK. Teoretycznie powinno być tak, że. Czy ja albo na przykład to? Można też dobrze, można odwrotnie, tak rzeczywiście, że włączamy dla wszystkich, a wyłączamy dla pojedynczych, tylko to.

**Damian Kamiński:** Wyjątek. Ma być mniej.

**Piotr Buczkowski:** No właśnie, bo. Mówiłem, że to jest proste, że `IN`. `NOT IN` też teoretycznie nie będzie jakiś problem. Ale to będzie skomplikowane, bardzo, tak.

**Damian Kamiński:** No dlatego. Jest to specyficzne wymaganie, to jest zdecydowanie i teraz pytanie, na ile my możemy to uprościć sobie? Ale też, żeby to było w miarę uniwersalne, oczywiście nie tracąc uniwersalności totalnie. Że jeśli byśmy powiedzieli, że te sprawy, jeśli jest zaznaczone, że nie wyświetlać, to te sprawy nigdy się nie wyświetlają. Na przykład na głównej zakładce "Do wykonania", bo to nie są przypisane do ciebie. Jesteś tam tylko współpracownikiem, a sprowadzamy to tylko na tak, jak tam Mateusz zasugerował, tylko na poziom konkretnego obszaru, czyli to jedno "Do wykonania", ma inne zapytanie, czy to nie jest dobry kierunek? Czyli na poziomie obszaru gdzieś byśmy tym zarządzali.

**Piotr Buczkowski:** Nie, nie, nie, nie, to to jest jeszcze większe skomplikowanie.

**Damian Kamiński:** OK, no dobra, po prostu proponuję.

**Piotr Buczkowski:** Nie mieszajmy w to obszarów, proszę.

**Anna Skupińska:** Znaczy tak, bo może może to nie robić z tego "Do wykonania", bo "Do wykonania" tak jest dosyć ciężkie, musi ma dużo rzeczy do zrobienia, więc.

**Piotr Buczkowski:** Właśnie chodzi tylko o zakładkę "Do wykonania".

**Anna Skupińska:** Aha.

**Damian Kamiński:** Chodzi tylko o to.

**Piotr Buczkowski:** Sprawy, w którym jestem współpracownikiem? Znaczy one się pojawiają już wszędzie tak na wszystkie czy na inne. No to jest ustawienie na sprawie na liście "Do wykonania", czy pokazywać takie sprawy, czy nie.

**Anna Skupińska:** No może po prostu sobie ustalić jakim filtrem, czy chcesz je pokazywać, czy nie.

**Piotr Buczkowski:** Bo teraz jest po prostu to, co mówiłem tam, że był tam `OR`, zrobiłem, przerobiłem `OR` na `UNION`. Tam jest jeszcze też właśnie jeden `UNION`, że i `UNION` wszystkie te gdzie jesteś [niezrozumiałe] `JOIN` do `Case Activity`, tak. No to mówię, mówię tam, nie ma problemu, żeby dodać `Case` `IN`. Jeżeli tam będzie. Tak nie `OR AND AND Case` `IN`. Jeżeli tam będzie kilka procesów, to nie ma problemów, nie będzie to wydajnościowego problemu.

**Damian Kamiński:** Dobra. Dobrze to poproszę też Mateusza, żeby dokładnie zdefiniował jaka to jest proporcja, ile to dotyczy. Wtedy też właśnie może to zdefiniuje, w jaki sposób łatwiej do tego podejść. I wycenić.

**Anna Skupińska:** Czy będziemy rozmawiać o funkcji `Source Get Source`?

**Łukasz Bott:** A masz jakieś pytania odnośnie tego?

**Anna Skupińska:** Znaczy, bo to jest ciągle w `Designie`.

**Damian Kamiński:** No bo jest tak jak widać, no pytanie jest w `Designie`. Bo już [niezrozumiałe] jest w `Designie`, dlatego, że jest właśnie cały ten komentarz, który już omówiliśmy, czyli ta funkcja. Ta reguła bym powiedział, że ona jest skończona, tylko tutaj całe zgodnie z tym ustaleniem całe te źródła trzeba przerobić na `dynamic form` na ten nowy typ. I podejść do tego kompleksowo, dlatego to jest w `Designie`, bo po prostu ja tam wrzuciłem ten dodatkowy opis. Mateusz też już chce z tego korzystać, więc ja bym to pytanie: kto się tym zajmie? Czy Ania?

**Anna Skupińska:** Raczej ja robiłam już poprzednie `source`, więc mogłabym się tym zająć.

**Damian Kamiński:** No dobrze, tylko ja mówię nie tylko o tym, bo to to jest zakładam najmniejszy banał, tylko o tym, co jest niżej w komentarzu, czyli zdefiniowanie nowego źródła, zdefiniowanie kolumn, które tutaj sobie ustaliliśmy, dla tego typu źródła, żeby one od razu natywnie się podstawiały, żeby wyżej jakbyś mógł troszkę Łukasz. Tutaj było. Taki interfejs. Pamiętasz, jak to omawialiśmy na tydzień albo 2 tygodnie temu, żeby tu był plus, można było bez, czyli źródło typu `dynamic` nie wymaga wgrania pliku? Pozwala, ale można dodać.

**Janusz Bossak:** Pamiętam to, to się nie nadaje do dewelopera.

**Damian Kamiński:** Ja nie, nie, ja nie mówię, że się nadaje, to jest cały czas w `Designie`. Ja to jeszcze zaprojektuję, tylko pytanie czy właśnie w przyszłym sprincie mamy na to przestrzeń?

**Janusz Bossak:** WIM, no.

**Anna Skupińska:** W przyszłym sprincie, a ja na salę. Ja teraz będę pomagać Filipowi w robieniu matrycy. Tak, w sensie uprawnień, tak zależności.

**Damian Kamiński:** Czy mam się tym zająć? Uprawnień pól.

**Anna Skupińska:** Więc masz jeszcze trochę czasu, żeby to zaprojektować?

**Damian Kamiński:** No dobrze. Bo Mateusz też już chce z tego zacząć korzystać, więc.

**Łukasz Bott:** W zeszłym [sprincie] mówisz około Kołakowskiego, tak.

**Damian Kamiński:** Tak, tak, tak, tak, chodzi mi o te wiesz, te reguły te. Operacje na źródłach danych, tak, czyli te reguły `Source Get Source Set`, więc dobrze by było, żebyśmy od razu już mieli zdefiniowali tutaj komplet, czyli właśnie ten element i ten `dataset`. No dobra, to ja to zaprojektuję na przyszły sprint.

**Łukasz Bott:** Wyjmujemy to z Rady [architektów] i.

**Damian Kamiński:** Może możesz to zdjąć?

**Łukasz Bott:** Lub jutro jest coś twojego?

**Piotr Buczkowski:** No jak pracowałem nad tym lepiej stracą maile, tak? To jest takie coś, że jest zarejestrowane zdarzenie. Edycja sprawy, tak. I tego się nie da wyłączyć. Nie da się wyłączyć, zawsze zawsze zarejestrowane i nigdzie nie jest wyświetlany. Nie jest, nie wiem jaki to miało sens. Nie ja to robiłem.

**Anna Skupińska:** Może powinno w zasadzie w zasadzie wyświetlane gdzieś.

**Damian Kamiński:** Zaraz, zaraz, ale ja nie zrozumiałem. Jeszcze raz. W sensie nie da się wyłączyć globalnie tej.

**Piotr Buczkowski:** Jest to jest mechanizm, jest ten mechanizm rejestrowania tych zdarzeń, tak? Oprócz tego jest jeszcze jeden typ zdarzenia edycja sprawy. Który jest rejestrowany, ale nie da się włączyć, nie da się wyłączyć tego. Ale nigdzie nie jest wyświetlany przy wyświetlanie jest warunek, że pomijaj te zdarzenia. Nie wiem po co to zostało zrobione, może ktoś z was pamięta?

**Łukasz Bott:** Ale to Piotr mówisz?

**Damian Kamiński:** Dobrze, czyli jeszcze raz, w tej tabeli dedykowanej do `Case Activity`, tak. Jest po prostu zapisywane zdarzenie, że ktoś edytował niezależnie od historii sprawy, a tutaj możemy zarządzać tylko i wyłącznie takimi zdarzeniami właśnie bardziej nieingerującymi w treść sprawy, tylko podglądu dokumentu, podglądu sprawy. I tamten element tu nie jest wylicytowany jako możliwy do włączenia i wyłączenia i zawsze się loguje, ale nie jest z kolei nigdzie prezentowany po stronie frontendu.

**Piotr Buczkowski:** Tak, i nie wiem po co.

**Janusz Bossak:** No to może trzeba prezentować. Informację o tym, że ktoś edytował sprawę, no to czemu nie, tak?

**Damian Kamiński:** OK. Powtórzenie historii nieco.

**Piotr Buczkowski:** Po co powtarzać dokładnie?

**Janusz Bossak:** No właśnie, żeby też nie zaśmiecało gdzieś tam z drugiej strony, tak, bo skoro to jest w historii, to po co tutaj? No może.

**Anna Skupińska:** Znaczy może jeżeli ktoś szuka jakby co konkretny użytkownik zmienił, a nie jak została zmieniona sprawa?

**Piotr Buczkowski:** Nie, to jest tylko fakt, że jak ktoś edytował sprawę.

**Anna Skupińska:** Znaczy to jeszcze się przydaje, żeby ktoś by usuwał sprawy. To wiadomo, że ktoś coś kiedyś zmienił, nawet jeżeli sprawa jej historia zostaną usunięte.

**Damian Kamiński:** Znaczy, bo dzisiaj na historii.

**Janusz Bossak:** Ale co tam właśnie, co co co tam jest w tym zapisie? Znaczy, że edytował, ale wiadomo co edytował, że zmienił. Nie wiem kwotę.

**Damian Kamiński:** Nie, nie, nie, fakt, zakładam fakt.

**Piotr Buczkowski:** Nie po prostu edytował.

**Łukasz Bott:** No fakt.

**Damian Kamiński:** To nie jest powtórzenie historii, tylko tak jakby historia, bo dzisiejsza nasza historia, jakbyś mógł otworzyć jakąkolwiek sprawę, Łukasz, ona też w pewien sposób utrudnia odczyt edytujących z takiego wysokiego poziomu, więc może niekoniecznie trzeba się tego pozbywać. Trzeba było się nad tym zastanowić, czy to jakoś sensownie wyświetlić na froncie, bo. Zwróćcie uwagę jak byś mógł go sprawę otworzyć to tam wysoko poziomowe, bo widzimy tylko i wyłącznie właścicieli. I etapy dopiero jak wejdziemy w szczegóły, to mamy z kolei już bardzo taki. Rozdmuchany widok, czyli musimy skrolować, żeby zobaczyć kto i co i kiedy. A tutaj jak rozumiem to jest taki prosty tylko kto kiedy kto kiedy. Oj teraz jakby ten [niezrozumiałe] krok [niezrozumiałe]. Edytował. 100 pól. No to to by była taka długa lista i czas skrolować do kolejnego. Tak to co Piotr mówi, to zakładam, byłaby lista, kto, kiedy, kto, kiedy, kto, kiedy. No skoro już to mamy to zastanowić się może, czy to warto gdzieś tu w takiej formie uproszczonej wyświetlić?

**Łukasz Bott:** A ja zadam może inne pytanie. Czy te informacje, jeżeli je rejestrujemy, to czy gdzieś wyświetlamy?

**Damian Kamiński:** Tak, tak, tak, tak, oczywiście one są wtedy wróć na historię, tak jak jest historia pola na dole. To jest historia aktywności czy coś takiego. No tu jest w nowym w sumie widoku nie wiem jak włącz po prostu weź wyłącz to na tym procesie.

**Piotr Buczkowski:** Mogę miała pokazać zaraz.

**Damian Kamiński:** A no to pokaż, bo nie wiem jak na nowym na starym to było po prostu po prawej po lewej było historię pola po prawej było to.

**Łukasz Bott:** Aha, OK, dobrze. No dobra, no to jest. Ja w sumie teraz też tak pomyślałem, czy skoro o tym mówimy rejestrowaniem tego typu zdarzeń to może właśnie? Do dorzucić tutaj to, cośmy rozmawiali, to potrzebę rejestrowania użycia `Delete Case` na konkretnej sprawie i żeby to sobie ktoś tam.

**Piotr Buczkowski:** Nie. Przecież mówiłem, dlaczego nie?

**Damian Kamiński:** No mówiliśmy, gdzie to ma być ostatnio to omawialiśmy.

**Piotr Buczkowski:** To jest stosowany razem z kasowaniem sprawy i tak ma zostać.

**Łukasz Bott:** Nie no OK, dobra. Dobra, dobra. No dobra.

**Piotr Buczkowski:** Ja wtedy była spór, czy to jest aktywność administracyjna, czy inna. Obecnie ja twierdziłem administracyjna, bo obecnie z zestawie z listy usunięta może usuwać tylko administrator.

**Damian Kamiński:** Znaczy my to.

**Łukasz Bott:** Zgadza się, dobra.

**Damian Kamiński:** Tylko my to omawialiśmy, a do tego powstał jakiś [niezrozumiałe].

**Łukasz Bott:** Nie, jeszcze nie zrobiłem, zrobi, nie, nie zrobię do tego.

**Damian Kamiński:** OK. No bo to ma być tam przy logach, nie.

**Łukasz Bott:** Tak, tak, tak, tak ustaliliśmy tak, tak, tak, tak.

**Damian Kamiński:** Tak ustaliliśmy, że tylko tylko tam, bo tam będziemy szukać.

**Łukasz Bott:** Tośmy ustalili.

**Piotr Buczkowski:** Czym się uruchamia, bo.

**Łukasz Bott:** Swoją drogą zgłoszeniach od hotfixa.

**Anna Skupińska:** A co się stało?

**Łukasz Bott:** Bo tutaj. W którymś momencie przy aktualizacji AMODITa. Zmienił mi się kolor. Ten. Kolor tak interfejsy. Na czerwony, a ja miałem na swoim demo jakiś taki ciemnogranatowy.

**Anna Skupińska:** A może sprawdzić jakie jest kolor teraz w ustawieniach systemowych, może ktoś zmienił?

**Łukasz Bott:** No właśnie jest czerwony jakiś, jaki odcień czerwony?

**Damian Kamiński:** Takie jak teraz wyświetla Piotrek.

**Anna Skupińska:** A czy nie? Zobacz w ustawieniach systemowych, jaki jest ustawiony.

**Łukasz Bott:** No nie, Piotrek ma jakiś różowy, tak, no to znaczy to.

**Piotr Buczkowski:** Znaczy tutaj mi się czerwone ostatnio zauważyłem, nie wiem skąd się wzięło.

**Damian Kamiński:** No to ja czuję, że to chłopaki przy ustawieniach systemowych jak popracowali, przenieśli na Reacta to mogli to niesłusznie coś się zakodować, że się nadpisuje.

**Piotr Buczkowski:** Przecież to jest.

**Łukasz Bott:** Ja sprawdzę jeszcze w ustawieniach systemowych. Sprawdź, ale ja bym to wiązał z Reactem. Nie, nie, ja już sprawdzałem, ewidentnie jest zmieniony kolor tak ja tylko mówię w tym sensie, że w aktywności o właśnie aktywności użytkowników tej administracyjne i sprawdzę, czy przypadkiem sam sobie nie podmieniłem tak może przez jakiś przypadek, ale jeżeli nie, jeżeli nie będzie tak no to no to ten to to zgłoszę to jako hotfix, tak, no bo to [niezrozumiałe].

**Piotr Buczkowski:** Czy chodzi o to tak? Tutaj tak jednak tak też zrobiłem. Jakby wysłany mail, tak, to akurat proste o przesłanej sprawie. Można włączyć, można wyłączyć zapisywanie. Która jest ci, bo to może zajmować dużo miejsca, tak.

**Damian Kamiński:** OK.

**Piotr Buczkowski:** Stąd tak to zrobiłem, a. Wiadomo jak widać wpisów jest dużo i dużo jest tych [niezrozumiałe], co jest edycją, tak tu jest tylko to, że ktoś jakie ktoś miał uprawnienia. W momencie edycji. Ale te wpisy są.

**Damian Kamiński:** OK, ale to mamy tą historię, przecież to może z tego to wynika. Że ktoś edytował, skoro to jest tu przejdź na sprawę. Zamknij to, przejdź [niezrozumiałe].

**Piotr Buczkowski:** To kto?

**Damian Kamiński:** Informacje o sprawie. [niezrozumiałe] nie, to nie jest tu teraz, a wejdź w ludziki, trzecia pozycja, uprawnienia.

**Piotr Buczkowski:** To jest tak mniej intuicyjne, to trzeba zmienić, dlatego o tym.

**Damian Kamiński:** I na dole. Sprawdź, kto ma uprawnienia do sprawy. I czy to czasem nie jest związane z tą historią uprawnień? Że po to to zapisujesz?

**Piotr Buczkowski:** A może i tam?

**Damian Kamiński:** Że tu można na daną datę. Pamiętasz, bo to jest tak, że jak ktoś coś edytował, to wtedy zapisuje się stan właśnie uprawnień sprawy. Na ten moment edycji, że to nie mamy na. Codziennie, czy to 5 minut zapisywane tylko właśnie w momencie jakiegokolwiek podjęcia akcji? To może to po to było?

**Piotr Buczkowski:** No może być to sprawdza to no tego nie wiedziałem.

**Damian Kamiński:** To był on dla [niezrozumiałe] robione. Kojarzę właśnie, że że że zapisywana jest ta właśnie historia na dany moment i to jest właśnie przy edycji. To może po to to było wymyślone znaczy nie wiem kto to projektował. Wtedy wydawało mi się, że ty, ale to może ktoś inny jednak. No jeśli tam zapisywane są bieżące uprawnienia, to ja zakładam, że to właśnie po to było.

**Piotr Buczkowski:** Adrian, Przemek, krajno, Marek coś robił.

**Damian Kamiński:** Marek rejestrowanie aktywności użytkowników dwudziesty pierwszy.

**Piotr Buczkowski:** Adrian, pamiętasz Adrian jesteś, bo widziałem, że przez moją siostrę.

**Adrian Kotowski:** A tak jak mówisz, które opisywałem na innego inny [niezrozumiałe], to jest ten temat do aktywności tak użytkownika.

**Piotr Buczkowski:** Są wpisy [niezrozumiałe].

**Damian Kamiński:** Historii uprawnień do sprawy na dany moment.

**Piotr Buczkowski:** Które nie są wyświetlane tam w historii aktywności, co zawsze rejestrowane. [niezrozumiałe] edycja, sprawy tak.

**Adrian Kotowski:** Tak, tak, to jest [niezrozumiałe] edycji, a wszystko to jest wyżej. To jest specjalne operację. To właśnie typ jedność, sprawie tak.

**Piotr Buczkowski:** Tak. [niezrozumiałe] nie jest wyświetlane. Tutaj.

**Adrian Kotowski:** Sprawy tak, a wszystko to jest wyżej, to tych wpisów tutaj w tej historii typowych zdarzeń.

**Piotr Buczkowski:** Bo tutaj nie jest [niezrozumiałe] wyświetlane. Pytanie, czy [niezrozumiałe] są wyświetlane. Tutaj. Nie pamiętasz dobrze, dobry trop. To jest prawda, OK, znaczy. To było takie pytanie, że dodając te logowanie tych maili, po prostu zastanowiłem się, po co to jest, tak, nie wiedziałem, po co to jest.

**Adrian Kotowski:** Gdzie powinny jest to, powinny być, bo to jest.

**Damian Kamiński:** Mhm, no to pewnie to po to.

**Adrian Kotowski:** Gdy sprawdzamy to cało, jakby w sensie całą tabelę, więc to powinno to być sprawdzane, ale masz jeszcze raz zweryfikować.

**Damian Kamiński:** Tak zakładam.

**Adrian Kotowski:** To jest na przykład właśnie tych uprawnień nie ma jakby takiego ciągłego, wiecie, wyliczania.

**Piotr Buczkowski:** Znaczy okej. Dobrze. Zostawiam to tak, sprawdzę, sprawdzę, czy to jest to tak, no, bo dzięki za trop, nie pomyślałem o tym.

**Damian Kamiński:** Dobrze. Dobra, idziemy dalej w takim razie co tam Łukasz jeszcze mamy.

**Łukasz Bott:** Dobra, to w takim razie Piotrek, to ja to zdejmuję z Rady, a to sobie tam sprawdzisz.

**Piotr Buczkowski:** Tak, tak.

**Janusz Bossak:** Przepraszam was, chwilę nie słuchałem, ale tamto co pokazaliście o tych historii uprawnień to jest jeden, może o tym mówiliście, ale zrobiłem coś innego. Akurat przy Justynie na Strefach [niezrozumiałe] tak jest, jest proces, w którym jest zaznaczony, że administrator nie ma praw do tej sprawy, znaczy do tych spraw.

**Piotr Buczkowski:** Trzeba trzeba to uwzględnić. Nie było to uwzględnione.

**Janusz Bossak:** Tak. No to mi chodzi, prawda?

**Piotr Buczkowski:** Znaczy, nie rozmawialiśmy, wtedy nie wiem, nie zrobiłeś zgłoszenia o to. Ja zrobię zgłoszenie zaraz po spotkaniu.

**Janusz Bossak:** No ale to właśnie to. Wychodzi, że Justyna ma dostęp, a nie ma [niezrozumiałe].

**Piotr Buczkowski:** Tak, nie pomyśleliśmy o tym, żeby to uwzględnić tutaj to ustawienie.

**Janusz Bossak:** Tak, tak, bo to potem było dodawane.

**Damian Kamiński:** W sensie tylko to ja też gdzieś tam zauważałem te błędy, ale nie miałem czasu na przetestowanie, tylko to jest bezpieczniejsze. Tak mam na myśli to, że nawet jak wyświetla się, że ma uprawnienia, to nie ma, tak, czyli to jest ta wersja powiedzmy. Trzeba ujednolicić, ale system działa poprawnie. Tak.

**Piotr Buczkowski:** Jest, jest mylna informacja w jednym miejscu.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Niekonsekwencje, dobra. Wzmianki w komentarzu, weryfikacja działania funkcjonalności.

**Piotr Buczkowski:** Chodziło o to, że.

**Łukasz Bott:** A żeby tutaj chodziło?

**Piotr Buczkowski:** Jeżeli dodamy kogoś.

**Łukasz Bott:** Wzmiankujemy.

**Piotr Buczkowski:** Jest dodawany do [niezrozumiałe]. Nie zdajemy maila o tym, że został z tą wzmianką. [Niezrozumiałe] ma informacje, ale ponieważ został wzmiankowany, to zostaje dodany do CC. Już jako jako osoba będąca w CC, to już dostaje informacje o kolejnych komentarzach, ale już jako [niezrozumiałe]. Nie to, że wzmiankowany.

**Łukasz Bott:** Tak.

**Damian Kamiński:** To znaczy w ogóle wydaje mi się, że zastanawiam się, bo ja też gdzieś takie rozterki od klientów otrzymywałem, czy my nie, bo funkcja obserwatora wiąże się z właśnie mailingiem. Czy nie powinniśmy wprowadzić coś takiego, że można wyłączyć na procesie mailing dla obserwatorów?

**Łukasz Bott:** [Niektórym] wyłączyli na etap na konfigurację etapów, tak, że nie nie wysyła informacji powiadomień o otrzymaniu sprawy. Tak.

**Damian Kamiński:** Tak i niech on dostaje pierwszego maila inicjującego czy to będzie komentarza czy że został dodany, żeby ten fakt gdzieś tam musi odnotował, bo może tego nie zauważyć, ale czy zasadnym jest, że później on dostaje wszelkie inne?

**Piotr Buczkowski:** No to takie było założenie tego.

**Damian Kamiński:** No rozumiem, OK, że obserwator dostaje wszystkie.

**Piotr Buczkowski:** Znaczy jest rola `Reader`, tak? `Reader` to jest ma dostęp bez bez maila. Nie ma teraz możliwości edycji tego z interfejsu. Być może warto dodać edycje do interfejsu.

**Damian Kamiński:** O. No właśnie to tego nie wiedziałem. O tym zapomniałem, może nie tyle, ale wtedy to trzeba `Adjust` to `Role` tylko regułą, prawda?

**Piotr Buczkowski:** Tak.

**Łukasz Bott:** Tak, tak.

**Piotr Buczkowski:** Być może warto dodać do interfejsu.

**Damian Kamiński:** Czyli w tym obszarze sidebarze z uprawnieniami? Tylko jak to wtedy nazwać obserwator bez powiadomień?

**Piotr Buczkowski:** Odczyt.

**Łukasz Bott:** Cichy obserwator.

**Damian Kamiński:** Odczyt, tylko to jest nazwa roli, więc.

**Łukasz Bott:** Czytacz.

**Damian Kamiński:** No dobra, można się nad tym jeszcze zastanowić, OK, dobra, to jest dobry kierunek.

**Piotr Buczkowski:** Czy czytelnik, tak? Jest też rola `Forbidden`, ale też jest tylko tylko z reguł. Nie wiem, czy to.

**Damian Kamiński:** To akurat bym powiedział, że.

**Piotr Buczkowski:** Właściwe było dodawanie tego z interfejsu, żeby ktoś nie usunął. Bo to jest jasno, ma wynikać z przebiegu, tak, że na przykład sprawa trafiła do kogoś, to jest. Niewłaściwy to był niewłaściwie na tej sprawy, albo po prostu. Po pewnym czasie chcemy ukryć przed twórcą sprawy.

**Łukasz Bott:** To musi mieć.

**Piotr Buczkowski:** Jako sprawę, no bo jeśli na przykład ktoś tworzy przykład sekretariatu, a dalej już jest sprawa tajna, już tajnie do nas.

**Damian Kamiński:** To znaczy powiem Piotrze, tak tego typu wyzwania. Ono jest teoretyczne i nie twierdzę, żeby się nie przydało, natomiast nikt nigdy ja w swojej tutaj doświadczeniu nie odnotowałem takiej potrzeby, natomiast, że się wysyłają powiadomienia dla kogoś, kto miałby mieć wgląd do sprawy, to nie raz były takie kwestie. No to tutaj `Reader`, więc to można by było rozszerzać. Natomiast `Forbidden` to bym się nie śpieszył, ale na ten moment to też mogę dodać to z funkcji reguł, więc jest OK, dobra.

**Piotr Buczkowski:** No to jest `Reader`. To tak samo tutaj można tak dodać do `Reader`, jeżeli nie chcemy tych powiadomień.

**Janusz Bossak:** Jak ostatecznie?

**Damian Kamiński:** A no właśnie to pytanie jest takie, czy my słusznie dodajemy do obserwatorów tylko tego `Reader'a`? Niestety nie widać, tak, bo może powinien być `Reader`, a nie obserwator po wzmiankowaniu.

**Piotr Buczkowski:** No właśnie. No też tak powiem, gdyby to robiłem dodał do `Reader'ów`. Nie o to robiłem. To chyba Rafał. Jeszcze Rafał Bębenek robił tak, wzmiankowanie. Pamiętam.

**Damian Kamiński:** Tylko to trzeba było zaopiekować od razu dwustronnie, czyli raz zmiana tutaj backendu gdzie się dodaje, a 2 tych `endpoints` trzeba by było jednak wyświetlić.

**Piotr Buczkowski:** No tak, tak.

**Damian Kamiński:** Zapiszesz to Łukasz, to to znaczy pytanie, co sądzicie czy? Czy bo to jest zmiana wsteczna? Tak w sensie zmieni się funkcjonalność. Obecna może nie tyle co wstecz, ale od teraz zmieni się działanie tego wzmiankowana. Czy tu widzicie jakieś ryzyka?

**Janusz Bossak:** Doczekaj, poczekajcie, bo różnica pomiędzy `Reader'em` a obserwatorem przynajmniej w mojej głowie zawsze była taka, że do `Reader'a` nie są wysyłane powiadomienia, a do obserwatora są wysyłane powiadomienia.

**Damian Kamiński:** Dokładnie. Tak.

**Janusz Bossak:** W związku z tym, jeżeli obserwujemy powiadomienia z komentarzy, to według mnie powinno być tak samo, że powinien być dodawany do obserwatorów, bo chcemy, żeby dostawał powiadomienia. Tyle że z tych tylko, że zakres tych powiadomień powinien być inny.

**Damian Kamiński:** Czemu tak uważasz? Ale jakie powiadomienia chcemy, żeby on dostawał?

**Janusz Bossak:** Mailowe.

**Damian Kamiński:** Ja bym się nie, ja bym się z tym nie zgodził tak jeden do jeden. A dlaczego tak uważasz? Ja chcę kogoś jak piszę komentarz na przykład w kontekście nie wiem tutaj bieżącej [sprawy], żeby coś podjął, to ja chcę, żeby on dostał to jedno powiadomienie tak jak powiedzmy z Worda, gdzie w komentarzu sobie opisuje, że zrób to teraz. A już cię nie obchodzi, że sprawa poszła sobie dalej. Jak zrobiłeś?

**Łukasz Bott:** Znaczy. Słuchajcie, wróćmy do źródła tego.

**Janusz Bossak:** Dobra.

**Łukasz Bott:** Wróćmy do źródła tego, bo tutaj to to, o czym dyskutujemy. Pierwotnie zamieszanie wynikało z tego. Że. Jak kogoś po raz pierwszy wzmiankujemy w komentarzu, to. To ta osoba nie jest w ogóle świadoma faktu, że została wzmiankowana, tak, a dostała.

**Piotr Buczkowski:** Znaczy ma. Mówicie informacje nie ma maila. O to chodzi, że nie dostaje maila.

**Damian Kamiński:** Nie.

**Łukasz Bott:** Tak, tak, tak.

**Damian Kamiński:** Nie dostaje maila wzmiance.

**Łukasz Bott:** Tak, że została wzmiankowana, tak dostała, natomiast dostała maila, że nagle ni stąd ni zowąd jest obserwatorem sprawy, tak.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** I a to, że została wzmiankowana to ma w interfejsie w tym w tej zakładce powiadomieniu tak.

**Damian Kamiński:** No to trzeba to zaopiekować globalnie.

**Łukasz Bott:** I moim zdaniem minimum tutaj do zrobienia to zróbmy to, że jeżeli kogoś po raz pierwszy wzmiankujemy w komentarzach, to. Powiadomienie jest tutaj w interfejsie, tak jak dotychczas to bez zmian plus wysyłany jest mail, być może trzeba ten mail scalić od razu z tym pierwszym mailem dodania go do obserwatorów, tak?

**Damian Kamiński:** Nie nie, bo ustaliliśmy przed chwilą, że on niekoniecznie powinien być obserwatorem i według mnie nie powinien być.

**Łukasz Bott:** Nie, nie, nie, nie, nie, moment, nie, nie jest to takie oczywiste, że to byśmy ustalili, bo ja już słusznie zaprotestował. Ja bym ja bym zrobił minimum tutaj. Tylko tyle, że zostałem wzmiankowany po raz pierwszy w komentarzu to dostaję oprócz tego, że mam to w interfejsie. To dostaję maila tak jak masz co podałeś przykład edycji wreszcie tak, jeżeli ktoś cię w komentarzu wzmiankuje, to dostajesz maila, że zostałeś wzmiankowany w komentarzu jakimś tam w dokumencie i tyle i to jest to.

**Damian Kamiński:** Zgoda dokładnie, ale nie dostaje, ale nie dostaje maila, że ktoś potem przeniósł ten, bo to to to przez analogię, że ktoś potem przeniósł ten dokument do nowego folderu. Mnie to w sumie nie obchodzi, a tutaj dostajesz potem maila, że ta sprawa zmieniła etap, bo już jesteś jej obserwatorem, co mało cię obchodzi.

**Łukasz Bott:** Ale ale to, ale dobra to, ale to może rozdzielmy te.

**Janusz Bossak:** To są chyba 2 różne różne zapisy.

**Łukasz Bott:** Tak, ja myślę, że to są tak 2 różne rzeczy. Ja bym wiesz co ja bardziej inaczej tak. Czy można się czy ja powiedzmy, że ktoś dodał mnie do obserwatorów sprawy, tak. Może miało tam służbę, intencje mnie dodawać tak tylko, że jak ja zapoznałem się z tą sprawą to stwierdzam, ale mnie to nie dotyczy. No i się nie mogę odobserwować, tak. No i dostaje mailem.

**Damian Kamiński:** A no właśnie, a dostajesz maile, więc no dobrze, dobrze przejdźmy do minimum, czyli tak mówisz, wysyłamy maila, teraz wysyłamy maila, stałeś się obserwatorem, powinniśmy wysłać maila, ktoś cię w tej sprawie wywołał. Pytanie tam wysyłamy treść, czy nie można wysłać można nie cały jak jest długi komentarz jakąś zajawkę pierwszych 20 znaków, czy coś w tym stylu można by spojrzeć, jak to jest w Wordzie właśnie z Worda, bo tam chyba nie idzie cały komentarz, ale nie pamiętam.

**Łukasz Bott:** Minimum którym? Tak w komentarzu.

**Damian Kamiński:** Natomiast jednocześnie, jak już to opiekujemy, to żeby może nie wychodziły też 2, tak, żeby jak ci ktoś jawnie kogoś dodał do obserwatorów, to dostaje tego maila, a tutaj od razu zmieniamy tą rolę na `Reader'a`.

**Janusz Bossak:** Znaczy.

**Łukasz Bott:** Nie, nie zmieniałbym tutaj roli dla `Reader'a` zostawiamy obserwatora.

**Janusz Bossak:** Ja się skłaniam. Ja się skłaniam do tego co mówi Damian. Według mnie powinno być tak. Rola obserwator dodawana. Prawym panelu to jest zupełnie odrębny temat, natomiast jeżeli kogoś wzmiankujemy. To o co nam chodzi, czy o co chodzi użytkownikowi? On chce wywołać tego użytkownika, żeby on do tej sprawy zajrzał. Tak więc.

**Łukasz Bott:** Tak.

**Janusz Bossak:** Według mnie, tak jak Piotr powiedział, powinniśmy na to dawać go do `Reader'ów`, o ile nie jest już dodany, no po to, żeby do tej sprawy miał dostęp i mógł w ogóle na cokolwiek zareagować. Tu rodzi się pytanie, czy wolno nam wywoływać osoby spoza grono obecnych `Reader'ów`? Bo to jest pytanie główne, tak? I to było jakby przedmiotem wtedy rozważań z Rafałem właśnie czy czy wolno, czy nie wolno to doszliśmy do wniosku, że wolno, czyli teoretycznie wzmiankowanie rozszerza. Czyli daje uprawnienia do przeczytania tej sprawy, komuś może być zwykły użytkownik, który udostępni.

**Damian Kamiński:** Ale ma uprawnienia edycji, tak?

**Janusz Bossak:** No ale tylko edycji.

**Łukasz Bott:** Nie, nie wiem.

**Damian Kamiński:** To znaczy nie wiem, czy edycji może niekoniecznie edycji, bo jak ktoś jest obserwatorem, to może dodać komentarz czy nie może.

**Łukasz Bott:** Nie, `Reader`.

**Piotr Buczkowski:** Nie, nie może.

**Janusz Bossak:** Więc wiecie, no, jeżeli idąc śladem obecnego komunikatora i tego co się dzieje na Teams i tak dalej, no kto ma prawo dodać kogoś do czegoś, no do konwersacji, bo ten który tą konwersację stworzył.

**Damian Kamiński:** Oj nie, nie, nie, nie, nie.

**Janusz Bossak:** Ja bym był tutaj ostrożny z tym.

**Damian Kamiński:** Nie jest taki Janusz, jak powiedziałeś, inne osoby też mogą rozszerzyć konwersacje.

**Janusz Bossak:** No dobra znaczy. Mówię, że istnieje ryzyko, ale wracając do meritum. Ten ktoś, kogo dodamy? Powinien dostać informację o tym, że został wzmiankowany i w moim przekonaniu koniec na tym, jeżeli. Drugi drugą wzmiankę, którą może dostać. Jeżeli ktoś odpowie jawnie na komentarz. Ten, w którym on był wzmiankowany? Czyli mamy komentarz i mamy tam odpowiedź, czyli wywołuje Damian Kamiński. Co sądzisz o tej sprawie i w tym odpowiedź udzielamy odpowiedzi, nie wymieniając już Damiana. Ale jest on jakby w rodzicu tego komentarza. Nie? I wtedy powinien dostać odpowiedź. Jeżeli napisze komentarz poniżej. "Słuchajcie jeszcze nie wiem co z tym zrobić", ale nie jest to odpowiedź na.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Niczyją wzmiankę, no to nie to to idzie normalnym trybem. Ci co mają ci co obserwują tak ci co obserwują sprawę, no to widzą to jako nowy komentarz w sprawie, tak, no i dostają informacje.

**Damian Kamiński:** Nikt nie dostaje powiadomienia.

**Janusz Bossak:** I tak chyba to powinno działać.

**Damian Kamiński:** Z tym `Readerem` to też jest tak, że ten `Reader` powinien zostać nadany, jeśli nie jest może nadany. Nie wiem czy to jakkolwiek konfliktuje to właśnie otwarte pytanie, bo jeśli ktoś już jest dodany na przykład jako współwłaściciel, to może wtedy nawet nic zbędne jest dodawanie, czy może najpierw warto sprawdzić, czy ten wywołany jest już w jakiejś roli w kontekście tej sprawy i wtedy niekoniecznie nawet dodawać go jako `Reader'a`, bo. Równie dobrze ktoś może być współwłaściciel. Tak jak nasza znowu cofnę się do naszego procesu wycen, czyli przeglądamy i wywołuję, nie wiem, Anię Piotra. "Przypominam wam, że tutaj sprawa czeka na wasze podjęcia akcji", tak. A wy już jesteście współpracownikami, powiedzmy tych spraw, więc no nie wiem, czy wtedy jest jeszcze zasadne dopisywanie do roli `Reader'a` tego użytkownika, czy to już jest zbędne?

**Łukasz Bott:** No moim zdaniem to nadmiarowe.

**Damian Kamiński:** No więc tutaj można jeszcze powiedzmy pod tym kątem to zoptymalizować. Dobra podsumowując. Wzmiankowanie powinno skutkować wysłaniem powiadomienia dotyczącego udzielenia komentarza ze wzmianką, a nie informacją. O tym, że ktoś nadał komuś uprawnienia, to co to jest niezależny komunikat i niezależna funkcjonalność? Jednocześnie to wzmiankowanie, nie powinno nadać uprawnienia `Reader'a`. O ile ten użytkownik nie ma innych, czytaj wyższych, bo może mieć tylko uprawnienia albo obserwatora, albo współpracownika, albo wręcz właściciela.

**Łukasz Bott:** Albo właściciela.

**Piotr Buczkowski:** Jeżeli nie ma dostępu do odczytu dla tej sprawy z jakichś powodów.

**Damian Kamiński:** Tak, jeśli nie ma dostępu do odczytu, to wtedy nadaje mu dostęp `Reader'a`, jeśli ma, no to nic w zasadzie nie zmieniamy i tyle.

**Janusz Bossak:** No i trzeba być ostrożnym z tym `Forbidden`, tak chociaż nie, no tak.

**Łukasz Bott:** No nie no to nie dyskutujemy o `Forbidden`.

**Damian Kamiński:** `Forbidden` jest nad wszystkim, czyli możesz komuś nadać obserwatora, współpracownika, właściciela, jak dasz `Forbidden` to się nie dostanie.

**Łukasz Bott:** Nic nie zmieni.

**Janusz Bossak:** Ale chodzi mi o to, że nie powinienem nawet wzmiankować, czyli ja jestem za ograniczeniem listy osób, do których mogę wzmiankować, naprawdę. Nie podoba mi się to z punktu widzenia bezpieczeństwa.

**Damian Kamiński:** No ale wtedy eliminujesz ten element `Reader'a`, czyli najpierw musisz dać komuś obserwatora albo musimy dołożyć funkcjonalność interfejsu nadawania `Reader'a`, żeby móc go wzmiankować.

**Łukasz Bott:** No ale.

**Janusz Bossak:** Wiesz co? Chodzi mi o to, żeby to było bardziej znaczy troszkę bardziej utrudnione. Czyli tak wyobrażam sobie. Piszę tą małpkę i mam listę osób, które mają prawo do tego. Do tej sprawy tak na różne sposoby, albo są adminami albo cokolwiek, no ale mają związek z tą sprawą.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** I teraz może powinna być druga małpka albo druga jakaś ikonka, jeżeli nie widzę ktoś jest spoza tej sprawy. To żebym jawnie musiał to zrobić, tak, żeby nie wychodziło na to, że potem nam jakiś admin i od Security powie, że a tutaj ten użytkownik nie wiedział i tam panią Krysię dodał. A ona nie ma prawa wiedzieć o tej fakturze? Nie.

**Damian Kamiński:** Mhm, czyli na końcu listy byłoby "Dodaj, Dodaj nowego".

**Janusz Bossak:** Tak, i wtedy jest to wiesz? I to byśmy notowali w logach. Tak, że ten ktoś może powiedzieć to nie tylko wzmiankował, on nadał uprawnienie do tej sprawy.

**Damian Kamiński:** Czyli wzmiankując, no dobrze, tylko nadał uprawnienie.

**Anna Skupińska:** Muszę przyznać, jak się kogoś dodało. Ja bym dodała kogoś w komentarzu, to nie bym nie pomyślała, że o tej osobie się dodaje. Uprawnienie do tej sprawy.

**Janusz Bossak:** No właśnie no właśnie no właśnie i to każdy użytkownik zrobi nieświadomie kogokolwiek tutaj.

**Piotr Buczkowski:** Musisz już specjalnie wzmiankować, nie to, że wpiszesz tylko musisz wzmiankować, tak, czyli tym.

**Janusz Bossak:** No ale no to jest prosta funkcja w tej chwili.

**Łukasz Bott:** Ale mimo to.

**Anna Skupińska:** Może dało mu, że dać dopisek "uwaga, kiedy wzmiankujesz użytkownika dodajesz, dajesz uprawnienia do tej sprawy".

**Damian Kamiński:** To znaczy. Tu się Ania zgodzę i nie, bo jeśli się nad tym nie zastanowić, to masz rację, że że nie miałabyś pojęcia, ale z drugiej strony, no jeśli kogoś wzmiankujesz, czyli chcesz, żeby podjął akcję, no to musi się to wiązać z nadaniem uprawnień do tego. No wiecie, przenieśmy to na świat [niezrozumiałe] w komentuj mi to Janusz, no to muszę ci pokazać ten dokument do wglądu i poczekać aż mi skomentujesz, więc.

**Anna Skupińska:** To może zależeć na przykład ktoś chce komuś zobaczyć, hej, zobacz na ten komentarz w konwersacji, to może o tym pomyśleć, ale cóż. Tak można nie pomyśleć o tym, a tylko to.

**Damian Kamiński:** Nie no dobra, abstrahujemy, ważne jest to, żeby też to opisać, to wtedy właśnie nie jesteśmy znowu niepodważalnie i tak działa system i nikt nie może się przyczepić, że że że coś poszło nie tak dobrze. To znaczy ja się zastanawiam, bo teraz tak propozycja Janusza jest ciekawa.

**Janusz Bossak:** Czy? Jeszcze jeden pomysł jeszcze jeden pomysł. Ponieważ wydajemy komunikator.

**Damian Kamiński:** No.

**Janusz Bossak:** Może powiązać pewne koncepty tak, czyli tutaj ograniczyć, czyli można wzmiankować tylko osoby, które tutaj są. Tak w tej chwili. A skoro nie mogę wywołać osoby, której tutaj nie ma, to mogę to zrobić w komunikatorze tak wchodzę w komunikator, piszę wzmiankę i wskazuje tą sprawę i najwyżej ten ktoś nie ma dostępu do tej sprawy.

**Damian Kamiński:** No to jest, to jest dostępne w sensie.

**Łukasz Bott:** I wtedy poprosi.

**Janusz Bossak:** I. I wtedy prosi o dostęp, tak i ktoś uprawniony mu daje ten dostęp.

**Damian Kamiński:** Nie.

**Łukasz Bott:** No to słuchajcie, to jest takie.

**Damian Kamiński:** Tak, to za to to zaopiekuje to tą potrzebę. Powiedzmy komunikator uzupełni właśnie w ramach tej potrzeby.

**Janusz Bossak:** A tutaj się trzymam ściśle tego grona osób, które są dodane już do obserwatorów. Oczywiście to nie zmniejsza, czy nie wyłącza możliwości wejścia tutaj w zakładkę uprawnienia i dodania kogoś do obserwatorów i wymienienia go w tym czacie, ale to jest wtedy świadome działanie, tak po pierwsze musi istnieć ta zakładka uprawnienia. Ten ktoś musi mieć możliwość dodawania kogoś, jak dodał, czyli jawnie go dodał. Rozszerzył zakres osób uprawnionych, wtedy go wzmiankuje.

**Janusz Bossak:** Nie jest w tym zakresie osób, to nie może go wzmiankować i tyle wtedy korzystać.

**Damian Kamiński:** No tak tylko jak tego jak tego nie skomplikować, żeby wiecie, chcę kogoś wzmiankować, to muszę zrobić 10 kliknięć wcześniej, żeby to zrobić. To żebyśmy w tą stronę też nie skomplikowali tutaj z tą "Dodaj nową osobę". No jest ciekawym pomysłem, czyli mam listę osób, które dzisiaj są podpięte z jakimiś uprawnieniami. Mam na dole powiedzmy. Pierwszą osobę z [niezrozumiałe]. Rozszerzyć uprawnienia do sprawy, tak i tam sobie wtedy pojawia się okienko, gdzie wybieram osobę i obok. Co wybieram? Wybieram z listy rozwijanej, czy to jest?

**Janusz Bossak:** No to co już zaprojektować?

**Damian Kamiński:** Od najmniejszych tak, czyli odczyt, obserwator i współpracownik, tak.

**Łukasz Bott:** Słuchajcie no.

**Janusz Bossak:** Robię sobie tu małpkę. Na tej liście mam całą firmę.

**Damian Kamiński:** No tak, no i to jest łatwe w sensie UX jest super, bo mogę każdego wywołać szybko.

**Janusz Bossak:** No właśnie, no ale czy to jest to co chcemy?

**Damian Kamiński:** No i jesteś właścicielem sprawy, więc w jaki sposób odpowiadasz za ten formularz, ten dokument? Bierzesz na siebie jakąś odpowiedzialność i teraz my chcemy być mądrzejsi niż użytkownik, nie.

**Janusz Bossak:** No to tak jak pani powiedziała, nie byłam. To jak Ania powiedziała, nie byłaby świadoma, że to robi tak. Bo ja to mogę, nie wiem właśnie Anię wywołać, tak. Nie mogę nawet.

**Damian Kamiński:** No dalej już musicie się.

**Anna Skupińska:** Tak, to chyba myślał, że ta osoba tylko dostęp do tego czatu, nie.

**Damian Kamiński:** Nie no to to już ktoś kto by korzystał chyba raz, no.

**Anna Skupińska:** Ale powiedzmy, że mamy użytkowników, którzy nie znają się na tym za bardzo, więc nawet żeby było jakieś ostrzeżenie, że dołączając tego użytkownika, przyznajesz mu uprawnienia, to już byłoby dużo.

**Damian Kamiński:** Ale OK, no dobra, różne są opcje, mhm.

**Janusz Bossak:** No i wiesz, nie masz takie coś, potem nie. Bo tu jest podłączony, tam nie wiem, umowa z prezesem.

**Damian Kamiński:** Nie no łatwo jest znaleźć przypadek, który, że tak powiem tak jak tu pokazałeś, ja abstrahuję od tego tylko pytanie, czy żeby zabezpieczyć się przed takimi przypadkami jak to zrobić mądrze, żeby nie skomplikować tam, gdzie świadomie dodajemy i korzystamy. Nie, ja nie jestem przeciwny, tylko żebyśmy nie dorobili klimatologii.

**Adrian Kotowski:** Może ktoś klika "Dodaj komentarz", to pokazuje mu się.

**Anna Skupińska:** Myślę, że wystarczy ostrzeżenie.

**Łukasz Bott:** Ale czekajcie, to znaczy tak, słuchajcie, trzeba to chyba jakoś wyważyć, bo z jednej strony możliwe, że ta klika [niezrozumiałe] jest potrzebna, bo podam przykład z życia i to na na na naszej firmie. Tak na przykładzie naszej firmy zrobiłem ten oceny, sytuację do tych dokumentów CV, tak, co tutaj wspomaga pracę naszych koleżanek, tak Oli i Justyny, i i teraz tak na procesie CV u nas w firmie jest wyraźnie ustawione, że administrator osoba w roli administratora. Nie ma wglądu do tych spraw, tak i a zdarzały się sytuacje takie, bo tam, zwłaszcza w tym początkowym okresie. No czasu do czasu tamten coś [niezrozumiałe] nie działał. Dziewczyny zgłaszały uwagi. Tak, no to ja musiałem wyraźnie poprosić o to dobra, to jeżeli to jest konkretny przypadek, bo chcemy zobaczyć konkretny przypadek, nadaj mi uprawnienia i wtedy mnie dziewczyny dodawały do jednej konkretnej sprawy dodawały mnie jako właśnie tam, powiedzmy `Reader'a`, tak tam nie `Reader'a`, tylko obserwatora. Powiedzmy tak. I i obserwatora, czy tym współpracownika, ale w każdym razie musiały mnie jawnie nadać, tak, czyli to jest to odpowiada na taką troszkę sytuację, właśnie tego trochę co Janusz podał scenariusz, że jest w firmie bezpiecznik jakiś tak, który właśnie by się czepiał i to jest bardziej taka kwestia organizacji pracy. Tak. Z drugiej strony mamy tą kwestię właśnie, że wzmiankuje to Ania, jest tak jak powiedziała Ania, że niekoniecznie jest świadoma tego, że przy okazji się zadziała magia, bo ta osoba dostała jakiś tam zestaw uprawnień. No i jeszcze ta trzecia opcja do tego, że to jest [niezrozumiałe] tak dodatkowa, tak no. W tej chwili wzmianka jest proste, tak no.

**Damian Kamiński:** Dobrze no pytanie, ja się zgadzam, że możemy to zabezpieczyć tylko właśnie jak to zabezpieczyć najdelikatniej tak jak to zrobić, żeby było na [niezrozumiałe] niej, czyli żeby już z tego interfejsu móc dodać tą osobę i do komentarza i od razu nadać jej uprawnienia, żeby nie trzeba było gdzieś przechodzić indziej. Czyli.

**Janusz Bossak:** Słuchajcie, wróćmy do meritum, bo to to rozszerzenia są fajne, natomiast tak te filmiki działają od 2 lat albo więcej. Więc zostawmy to. Musimy zaopiekować temat pierwszego maila, że jak ktoś jest wzmiankowany, to do niego idzie.

**Łukasz Bott:** Wzmiakowany otrzymuje maila dokładnie i tyle, i to jako minimum zróbmy.

**Janusz Bossak:** To trzeba zrobić, a potem się możemy.

**Damian Kamiński:** Nie, ale czy jednocześnie poprawiamy na `Reader'a`, bo to też jest istotne, bo ale to poczekaj, Łukasz, bo teraz będzie tak, czy nie będzie tak, że dostanie 2 maile, bo jest dodany jako obserwator. To jest jeden mail jest dodany jako wzmiankowany, no to być może, no to być może tą sytuację, gdy w momencie gdy wzmiankuję, to trzeba po prostu połączyć te 2 maile w jeden, tak, że zostałeś wzmiankowany w komentarzu w tej w tej sprawie i dostałeś jednocześnie uprawnienie jako obserwator do tej sprawy i tyle i być może to uspójnić tak.

**Janusz Bossak:** A tak.

**Łukasz Bott:** Czy to, bo to jest tak, jakby podwójne, zgadza się?

**Damian Kamiński:** No ja ja uważam, że że tutaj za zmiana roli to jest przy okazji można zrobić i to już byśmy mieli zaopiekowane, ale OK jak chcecie tak totalnie po minimum no to niech będzie tak jak mówisz. Ja bym poszedł ten jednak kroczek dalej tutaj dosłownie kroczek zmieniłbym to żeby ta osoba nie dostawała w związku z tą wzmianką kolejnych mail. Ale no albo zapytajmy tutaj też klienta, tak?

**Łukasz Bott:** Nie no to.

**Piotr Buczkowski:** Tylko jeden myśl, tylko jeden mail, że zostawiłeś ją [niezrozumiałe] nie [niezrozumiałe].

**Łukasz Bott:** Tylko jeden mail wzmiankowany. Każda. Każdy kolejny wzmiankowany już już nie nie powoduje wysłania maila tak o wzmiankowanym, no bo.

**Damian Kamiński:** Nie, nie powoduje. Dlaczego nie, nie każde wzmiankowane powoduje, nie, nie tu chodzi mi o co innego. Kolejne maile mam na myśli w ramach roli obserwatora to mam na myśli kolejne maile.

**Piotr Buczkowski:** Nie powoduje.

**Łukasz Bott:** OK?

**Piotr Buczkowski:** No nie no to musi.

**Damian Kamiński:** Może zapytajmy tutaj też, żeby żeby nie pójść też za bardzo, bo może mój pomysł jest tutaj niespójny z tym, co się dzieje? Może [niezrozumiałe] z tego korzysta. Zapytajmy, co dalej tak, czyli z racji, że dzisiaj dostanie powiedzmy tego maila, ale on jest też dodawany do opcji obserwatora to, bo no teraz. Utwierdził mnie tylko w przekonaniu, jak jest `Work Case` tej sprawy, to obserwator dostaje powiadomienie. Tak, tak pamiętam czy się mylę.

**Piotr Buczkowski:** Jeszcze raz jak jest co?

**Damian Kamiński:** Jak jest przekazanie tej sprawy między etapami od użytkownika do użytkownika? To obserwator dostaje powiadomienie o tym fakcie, tak?

**Piotr Buczkowski:** Tak, to absolutnie tak, tak. Tym.

**Damian Kamiński:** No właśnie i dla mnie to jest bez sensu, że osoba wzmiankowana to dostaje, bo to ja nie zgłaszam osoby jako obserwatora. Ja wywołuję kogoś we wzmiance.

**Janusz Bossak:** No jak tak, to trzeba zaopiekować według mnie.

**Łukasz Bott:** Dobra, no to.

**Damian Kamiński:** Że wiecie, po prostu potem czujność na te maile spada, jak my ładujemy mailami ze wszystkim co się da, to po prostu ludzie, potem tylko przekują i potem wszyscy wyłączają te maile i i nic z nich nie wynika.

**Piotr Buczkowski:** Zmień po prostu, żeby.

**Łukasz Bott:** Standardowy koszt [niezrozumiałe].

**Damian Kamiński:** Więc ja bym poszedł o ten kroczek dalej zmieniłbym skutek wzmiankowania, że rola nie obserwator tylko `Reader`. Email o tej wzmiance i tak jak Janusz powiedział, obserwujemy jeszcze przy każdym komentarzu co to jest za komentarz? Jeśli to jest komentarz zagnieżdżony do komentarza ze wzmianką, to wtedy tamten ci wzmiankowani dostają też powiadomienie jeszcze raz, że ktoś odpowiedział na komentarz, w którym byłeś wzmiankowany.

**Łukasz Bott:** OK.

**Damian Kamiński:** A jeśli to jest równoległy komentarz bez żadnej wzmianki, no to nie idzie do tych osób żaden żaden komunikat. No dobrze to według mnie temat wyczerpaliśmy, słownie to może już wykorzystany. Copilota, żeby to opisał. Możemy to tu później wrzucić. Mogę to zaopiekować.

**Łukasz Bott:** Dobra, to dałem, przypisuję tobie.

**Damian Kamiński:** No to przypisz do mnie, no.

**Łukasz Bott:** I zdejmuje z tego.

**Damian Kamiński:** No dobra, jest za 10. Nie wiem czy jeszcze coś podejmujemy pilnego, czy czy zostawiamy.

**Łukasz Bott:** Nie, nie, nie, nie, nie był tutaj. Ja za chwilę jeszcze tam gdzieś mi Lucyna wywołała.

**Damian Kamiński:** No i do mnie coś dzwoniła, nie wiem o co chodziło jeszcze. Się pali coś.

**Łukasz Bott:** Dobra, no to kończymy.

**Anna Skupińska:** Mhm. Do zobaczenia na spotkaniu firmowym.

**Łukasz Bott:** Dzięki.

**Damian Kamiński:** Cześć.

**Adrian Kotowski:** Cześć.

**Janusz Bossak:** Zatrzymano transkrypcję.

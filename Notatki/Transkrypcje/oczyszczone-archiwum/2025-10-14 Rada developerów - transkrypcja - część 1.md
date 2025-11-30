**Data spotkania:** 14 października 2025, 08:00

---

**Janusz Bossak:** Dobra, nie tracąc czasu – Adrian, masz temat odnośnie e-doręczeń. Proszę, żebyście z Piotrem raz uzgodnili, o co tam chodzi i jak to powinno być zrobione.

**Adrian Kotowski:** Na samym początku powiem, że tam jest problem z niespójnością dokumentacji. Jest oficjalna dokumentacja od Poczty Polskiej i 2 miesiące temu dostaliśmy inną wersję dokumentacji. Tam szczerze wszystko trzeba testować na 2 razy i mam taką teorię, że może tam jest inne API czy inne intencje, które mają inne implementacje i stąd takie problemy między maszynami. Jeżeli chociażby 2 organizacje są organizowane przez 2 różne maszyny, tam jest jakieś przekierowanie na pewno do tego drugiego API i stąd ta różnica. Bo jeżeli działa jedna instancja serwisu, to wtedy nie ma problemu, nawet jak ta druga maszyna działa. Dla mnie to jest takie ograniczone, pomimo możliwości w tym obszarze, bo jednak jest ta cała API.

**Piotr Buczkowski:** Ale problem jest, że u nas z jednego serwera nie działa, z drugiego działa czy w Poczcie? Na jednym serwerze działa, na drugim nie działa.

**Adrian Kotowski:** Na jednym nie działa czy nie działa? Jeżeli są 2 maszyny?

**Piotr Buczkowski:** Ale u nas czy w Poczcie?

**Adrian Kotowski:** Który raz?

**Piotr Buczkowski:** U nas czy w Poczcie?

**Adrian Kotowski:** Przyjmujemy odpowiedź, że żądanie miało błąd forbidden czy tam coś.

**Piotr Buczkowski:** Ale u nas, u nas.

**Adrian Kotowski:** U nas, jeśli tak.

**Piotr Buczkowski:** Czy u nas mamy 2 serwery, na których działają, żeby tak powiedzieć, 2 AS?

**Adrian Kotowski:** Nie, chodzi o serwer Poczty Polskiej – tego serwera, który obsługuje API.

**Piotr Buczkowski:** Ale.

**Adrian Kotowski:** My wysyłamy żądanie, otrzymujemy błąd.

**Piotr Buczkowski:** Rozumiem, że u nas mamy 2 ASy – jeden, a się, poczekaj, poczekaj.

**Adrian Kotowski:** Mamy 2 usługi produkcyjne, akurat.

**Piotr Buczkowski:** Z jednego się udało, na drugim nie działa.

**Adrian Kotowski:** Warunkowo, bo jeżeli jest tylko jeden AS uruchomiony, to wtedy działa.

**Piotr Buczkowski:** Czy nie? A jeżeli ten drugi jest uruchomiony tylko?

**Adrian Kotowski:** To też działa. Ten drugi zawsze działa?

**Piotr Buczkowski:** Czyli Poczta może ograniczać tak, że tylko z jednego serwera się łączy dana firma?

**Adrian Kotowski:** Na testówce tak, to się potwierdziło. Na produkcji oficjalnie nie. Ale mamy jedno IP, teraz jeszcze mamy to – 4, masz 7 produkcyjnych, 2 usługi, 2 polityczne, pod usługę 2 maszyny polityczne, ale to jest system za jednego IP, bo tak się mówiliśmy z Łukaszem krok po kroku, żeby tak robić.

**Piotr Buczkowski:** Na pewno. Już sprawdź.

**Adrian Kotowski:** I tam jest jeszcze ta sama wersja programowania i takie same ustawienia oraz czasu jest taka sama. I też certyfikaty są poprawne, bo sprawdzałem, że faktycznie jest ten sam certyfikat.

**Piotr Buczkowski:** Nie, ale dobrze, po czasie sprintu zrozumiałeś, że AS jeden działa, a z AS 2 nie działa, albo odwrotnie? Skończyło się, że z jednego naszego ASa działa, z drugiego nie, ale rozumiem, że to nie jest tak?

**Adrian Kotowski:** Ciężko mi.

**Piotr Buczkowski:** Wylogowałem cię za AS.

**Adrian Kotowski:** 3 razy, bo nie do końca.

**Piotr Buczkowski:** Wywaliłem cię za AS, bo sam się zalogowałem i ty byłeś.

**Adrian Kotowski:** Dobra, OK. To jest tak, że jeżeli są 2 ASy uruchomione, wtedy z tej dwójki nie działa, wtedy jedynka działa zawsze. Nie były takie sytuacje, że jedynka nie działała. Natomiast jeżeli jest tylko dwójka uruchomiona albo jedynka, to też zawsze działa, ale nie może być tak, że jest tylko jedna maszyna – muszą być 2, bo mamy 2 pełne działały.

**Piotr Buczkowski:** Komentuj, bo już coś kręcisz.

**Janusz Bossak:** Z tej opowieści mi się wyłania obraz, że to jest problem absolutnie po naszej stronie konfiguracji. Jak mówisz – albo 2 IP, albo w ogóle, że 2 serwery, konkurencyjne żądania zbyt szybkie.

**Adrian Kotowski:** Tam były 3 problemy. 2 problemy wynikały z tego, że po prostu była źle napisana dokumentacja. Tam były te różnice między 2 wersjami. To udało mi się już uchwycić, to poprawiłem i teraz działa. Jak mówiłem, można powiedzieć 50% – jest ten problem tych 2 serwerów. Wcześniej nie działało przez 2 miesiące.

**Piotr Buczkowski:** Ale ty nie odpowiedziałeś na pytanie, czy da się przepisać to jednak do serwera.

**Adrian Kotowski:** Przypisać na drugi serwer?

**Piotr Buczkowski:** Nie wiem, coś niezrozumiale to opowiadasz.

**Janusz Bossak:** Narysuj to może, panowie?

**Piotr Buczkowski:** Bo sprawdziłem właśnie – rzeczywiście, wychodzące IP mamy ten sam: 20.56.84.214 za obydwu ASów.

**Adrian Kotowski:** Czy to mogą być różne porty?

**Piotr Buczkowski:** Jeżeli ten sam request wyjdzie teraz z jednego AS dostępnego, a za chwilę wyjdzie z 2, to będzie działać czy nie będzie działać?

**Adrian Kotowski:** Nie powinno działać. Jak wcześniej mówiłem, jeżeli tam jest, masz 2 równoległe czy 2 jednocześnie i obsługują 2 różne organizacje, ponieważ się zdarza.

**Piotr Buczkowski:** Ale.

**Adrian Kotowski:** Wtedy te dwójki nie działają.

**Piotr Buczkowski:** Zaraz.

**Adrian Kotowski:** Mam to zalogowane, takie sytuacje.

**Piotr Buczkowski:** A jeżeli jest odwrotnie, że na przykład zadziała? Czy w ogóle zadziała 2 kiedykolwiek?

**Adrian Kotowski:** I wtedy jakieś usługa, pierwsza usługa na pierwszym właśnie wyłączona. Jak w teście to próbowałem się zalogować, to działało.

**Piotr Buczkowski:** Czy możemy tam – jest taki mechanizm, że preferred server?

**Adrian Kotowski:** Mhm.

**Piotr Buczkowski:** Czy jeżeli tam ustawimy dla tej usługi zawsze AS-01, to będzie działał albo AS-02?

**Adrian Kotowski:** To mogę uruchomić, sprawdzić.

**Piotr Buczkowski:** Czy możemy tak zrobić?

**Adrian Kotowski:** Dobra, czyli nie wiem czy teraz, w ciągu dnia. Rytualnie po godzinach mogę to wstawić.

**Piotr Buczkowski:** W każdej chwili możesz to zrobić. Kolejne wywołanie, czy tam powiedzmy będzie kolejne wywołanie, będzie już uwzględniało to.

**Adrian Kotowski:** Dobra, to wiecie co? Dobra, to sprawdzam na razie.

**Janusz Bossak:** Dobra, czy to?

**Piotr Buczkowski:** Ale dobrze, jeszcze raz. A ty byś ustawił już wszędzie tę preferencję AS-02, to by działało? W ogóle byłby jeden.

**Adrian Kotowski:** No muszę sprawdzić, bo to teraz, to co mówisz, jeszcze tego nie weryfikowałem. Tego nie robiłem. Także wyłączałem już jedną usługę w nocy i zobaczę, co się stanie.

**Piotr Buczkowski:** Mi się nie podoba.

**Janusz Bossak:** Dobra, proponuję tak – ponieważ temat jest dłuższy pewnie i więcej trzeba różnych prób zrobić, to wniosek z rady jest taki, że Piotr z Adrianem intensywnie nad tym popracują wspólnie, żeby znaleźć rozwiązanie. Bo możliwe, że po prostu to jest jakaś kwestia konfiguracji po naszej stronie tych serwerów i takie mam przeczucie, że tak to jest, że to nie jest kwestia problemu Poczty Polskiej tylko ustawienia tych serwerów i sposobu ich współpracy. Dobra. Temat jeden mamy. Drugi temat to są te dashboardy systemowe. To temat Ani, myślę. Ania ogłasza, kilka słów.

**Anna Skupińska:** Przestałam się – co chcecie o nich mówić?

**Janusz Bossak:** Oczywiście, zrozumieć ten problem podmienia ID.

**Anna Skupińska:** To już rozwiązane w sumie jest. Problem chodzi o to, że można w dashboardach systemowych ustawiać sobie pola wspólne, a w tych polach wspólnych jest odwołanie do raportu, w którym znajduje się to pole, a to odwołanie do raportu to jest ID raportu. Oczywiście jak się tworzy te raporty, to my nie wiemy, jakie te raporty będą miały ID, dopóki go nie utworzymy w bazie danych. Oczywiście więc muszę, ale po prostu tam wstawiam tych dashboardów albo raportów po GUID – jest zawsze taki sam. I potem, gdy zostaną ustawione te raporty, to muszę wstawić tam zamiast tych buildów wstawić raport ID. I zrobiłam kod, który to robi wczoraj.

**Janusz Bossak:** No ale dlaczego tworzymy najpierw dashboard, a potem raporty? Nie bardzo.

**Anna Skupińska:** Z tego, że raporty, jeżeli należą do dashboardu, to potrzebują odwołania się do tego dashboardu – do ID tego dashboardu.

**Piotr Buczkowski:** A to raport jest dopiero zapisywany przed, po pierwszym zapisie? Tak, międzyczasie można go edytować.

**Anna Skupińska:** Czy ja mówię tutaj o tym, jak uruchamiamy kod, który nam te raporty tworzy? Przy update, bo to są te systemowe, one są tworzone przy update. To nie chodzi o klikanie.

**Janusz Bossak:** Mhm.

**Anna Skupińska:** Chodzi o to, że muszę – raporty się odwołują do dashboardów i dashboardy się odwołują do raportów. I nie mogę 2 zrobić naraz – pierwsze jedno musi być pierwsze. Akurat ja zrobiłam tak wcześniej, że naprawdę tworzą dashboard, a potem raporty, dlatego że raporty mają dwoje dashboardów – jest ta głowa, wygodniejsze dla skasowania się już do odwołania do raportów. No albo jest jedno pierwsze, albo drugie jest pierwsze.

**Piotr Buczkowski:** Ale zaraz, zaraz, zaraz. Powiedziałaś, że to nie jest zapis czy kliknięcie. To jest, kiedy to występuje?

**Anna Skupińska:** A czy to się dzieje, kiedy? Updateujemy system. On wtedy tworzy sobie raporty i dashboardy systemowe.

**Piotr Buczkowski:** Tylko wtedy.

**Anna Skupińska:** Tak, to jest tylko tutaj się dzieje. Później, jeszcze jeżeli coś dochodzi, już potem nie są w ogóle ruszane, bo nie powinny być zapisywane.

**Piotr Buczkowski:** Ale.

**Damian Kaminski:** Czyli tylko jak robimy update bazy danych? Tak, o to ci chodzi?

**Piotr Buczkowski:** A raporty systemowe nie mają stałych ID?

**Anna Skupińska:** Tak. Nie, ale mają GUID stare, mają stare GUID. Pogodziliśmy się dzisiaj, rozpoznaje.

**Adrian Kotowski:** Jest, także w innym miejscu ujemne, te ujemne.

**Anna Skupińska:** A czy nie? To ujemne ID to są w tych.

**Adrian Kotowski:** Źródłach.

**Anna Skupińska:** W źródłach danych.

**Piotr Buczkowski:** Źródłach.

**Łukasz Bott:** No to przy okazji chciałem ten temat poruszyć – czy na pewno musimy stosować ten ujemny ID?

**Piotr Buczkowski:** Nie, to zły pomysł. Odejdź od tego, jeżeli to możliwe.

**Łukasz Bott:** Też tak uważam. Skoro w bazie danych mamy mechanizmy bazy danych, jak się identyfikatory, które są liczbami de facto naturalnymi, no bo liczbami całkowitymi większymi od zera. To dlaczego wprowadziliśmy ten mechanizm ujemny?

**Piotr Buczkowski:** Żeby odróżnić systemowe od użytkowniczych.

**Anna Skupińska:** Nie systemowych.

**Łukasz Bott:** Tak, ale to nie łatwiej było dodać kolumnę, po prostu, że to jest systemowy?

**Anna Skupińska:** No takie są w raportach i dashboardach.

**Łukasz Bott:** To dlaczego z tego nie korzystamy?

**Piotr Buczkowski:** Bo już podjęliśmy złą decyzję.

**Łukasz Bott:** No nie wiem, żeśmy podjęli złą decyzję, więc pytanie, czy przy tej okazji, jak i tak coś tam majstruję przy tych raportach systemowych, czy tego nie uporządkować i nie zrobić prawidłowo?

**Anna Skupińska:** Jak chcecie, to możemy.

**Piotr Buczkowski:** Warto by było to zrobić.

**Łukasz Bott:** No bo, Ania, ja mówię to w.

**Piotr Buczkowski:** Tylko trzeba zaplanować dobrze migrację.

**Łukasz Bott:** Dokładnie, bo Ania, ja mówię to w kontekście takim, że ponieważ przy teście tej re-edycji tych raportów systemowych powstało kilka nowych źródeł systemowych. I oczywiście nadały się im tam te indeksy ujemne, tylko.

**Anna Skupińska:** Mhm. Mhm. Tak.

**Łukasz Bott:** To ci się odbiło rykoszetem na mechanizm synchronizacji, który nagle robił SELECT coś tam FROM, i tutaj nazwa tabeli, w której była używana, czyli DPSRC podkreślenie minus 22. I oczywiście fatal error. Bo się wywalił na składni. I na przykład synchronizacja tych źródeł nie działała. Ja robię raport systemowy i się zastanawiam, doszedłem – nie mam danych. Na szczęście miałem porównanie. Fajnie, że te dane powinny być, tak, ale nie widzę tych danych. I po nitce do kłębka doszedłem, że kurczę, problemem jest właśnie ten, że synchronizacja źródeł systemowych – a kilka jest lokalnych, bo muszą być lokalne, bo się przeliczają agregacje jakieś raz na dobę, takie zaplanowane. Właśnie powodują – ten ujemny indeks tych źródeł powoduje, że na przykład mechanizm synchronizacji się wywala. Więc jeśli moglibyśmy od tego odejść, to odejdźmy. Wiem, że się kiedyś tam podjęło taką decyzję, ale jak widać, ona się niekoniecznie sprawdziła.

**Janusz Bossak:** Co jest do zrobienia w takim razie?

**Anna Skupińska:** To jest do zrobienia, ale to zajmie trochę czasu.

**Janusz Bossak:** Ale co jest do zrobienia?

**Anna Skupińska:** A czy zamiast – jest możliwe to, żeby zmienić, żeby źródła systemowe nie miały ujemnych ID, tylko zamiast tego miały buildy i żeby było napisane, że są one systemowe? Dodać po prostu trzeba było 2 kolumny – jedna to built ID, a druga to system origin.


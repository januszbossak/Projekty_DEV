**Data spotkania:** 2 grudnia 2025, 11:59 - część 2

---

**Przemysław Sołdacki:** Ale rozumiem, że plan jest taki, żeby zdążyć. To jest realne, żeby zdążyć?

**Janusz Bossak:** Znaczy z tymi JRWA pewnie tak, bo tak wiesz – uprościliśmy to koncepcyjnie bardzo mocno i Marek pewnie się z tym upora w ciągu tam wczorajszego dzisiejszego dnia. Może do jutra nawet, bo widzę, że to sprawnie idzie i pewnie będzie mógł się zabrać za ten na przykład tą paczkę do archiwum. Z tą paczką to już mówiłem, to jest pierwsza wersja, którą robimy. To jest to, żeby w ogóle można było zweryfikować – ta paczka jest dobra. Tylko żeby zweryfikować ta paczka jest dobra, to wdrożeniowcy muszą tą paczkę generować. Ja nie wiem czy oni są na takim etapie, żeby oni w ogóle wiedzieli.

**Przemysław Sołdacki:** Ale to będzie tak, że oni coś muszą pokombinować regułami, czy będzie prosto funkcja wygeneruj paczkę?

**Janusz Bossak:** Jak wygenerować paczkę, skoro oni jeszcze JRWA nie wdrożyli? Więc... No tak. Nie, pewnie musieli kombinować regułami. Tak, bo to to jest tak samo jak z paczką w tej e-teczce – trzeba ją tam wyrzeźbić odpowiednich plików z odpowiednich rzeczy. Może nie wszystko do tej paczki wchodzić i tak dalej.

**Przemysław Sołdacki:** Znaczy, wydaje mi się, że dev powinien konsultantom powiedzieć jak to robić. To jest taka rzecz, która jak jest robiona pierwszy raz to powinni to skonsultować, żeby sobie jakieś konsultantki nie wymyślały jak to robić, bo może wymyślić źle.

**Janusz Bossak:** No to nie.

**Przemysław Sołdacki:** Po pierwszym użyciu, a potem jak wiemy jak to już robić. No bo jeśli mamy robić jakieś nie wiem – narzędzie do weryfikacji, czy nie wiem – czy to jest gotowe narzędzie do weryfikacji?

**Janusz Bossak:** Narzędzie do weryfikacji będzie polegało na tym, że wysyłamy to do archiwów państwowych na specjalny endpoint do weryfikacji paczki i oni odpowiadają – jest OK, nie jest OK.

**Przemysław Sołdacki:** Ale to musi dać coś robić, czy to jest gotowe narzędzie, które konsultant sobie sprawdzi, że działa?

**Janusz Bossak:** Endpoint, do którego można wysłać przez REST API, więc nie trzeba nawet robić jakiegoś specjalnego – to można.

**Przemysław Sołdacki:** Są jakieś te? Nie pamiętam to narzędzie, jeśli się wysyła do REST'a.

**Janusz Bossak:** Na razie można Postmanem zrobić czymkolwiek – na razie chodzi o to, żeby wysłać na ten endpoint, on jest publiczny, nie trzeba tam się rejestrować, wysłać paczkę i stwierdzić, że jest OK lub nie jest OK. Tak. Jeżeli będziemy już potrafili robić taką paczkę, czyli takiego XML'a, który będzie zawierał nam odpowiednie pliki i tak dalej.

**Przemysław Sołdacki:** No na przykład.

**Janusz Bossak:** To wtedy można to dopiero oprogramować i zrobić z tego mechanizm.

**Przemysław Sołdacki:** Jasne, ale rozumiem – znaczy, bo co tutaj dev ma robić? Bo to konsultant ma to zrobić, czy czy czy?

**Janusz Bossak:** No to musimy wspólnie z nimi ustalić optymalny, tylko że.

**Przemysław Sołdacki:** OK, będzie ustalone, dobra, OK?

**Janusz Bossak:** Nie wiadomo, czy oni są gotowi, to jest moje największe zmartwienie. Czy oni są gotowi na tym etapie teraz w grudniu, kiedy mają początek tego wdrożenia? Czy oni są gotowi już przygotowywać jakieś paczki do archiwum, skoro nawet nie mają wdrożonego procesu obiegu korespondencji i nie mają dokumentów?

**Przemysław Sołdacki:** No bo jeśli nie, no to przesuniemy sobie na nie wiem – kolejny kwartał na przykład albo jakoś.

**Janusz Bossak:** Pewnie tak, więc dlatego mówię – to planowanie, to jest takie płynne, to wszystko.

**Przemysław Sołdacki:** No ale wiesz, lepiej mieć plan i określić jaki procent planu się udał, niż nie mieć planu i nie wiedzieć w którą stronę się płynie. Ale dobra, to idźmy dalej. Ten NAMAKU rozumiem, że tam się robi i tam Adrian mnie tu popędza, żebym przeszedł weryfikację, zapłaciłem, przesłałem im swój dowód osobisty, mam nadzieję, że mnie zaakceptują, będziemy mieli tam dostęp. Dobra, generowanie dokumentacji właśnie, bo to jakiś powstało takiej nie wiem – ponoć bardziej.

**Janusz Bossak:** Dokładnie. Tak i.

**Damian Kaminski:** Znaczy, słuchajcie, z mojej perspektywy tutaj pozwolę się sobie wtrącić.

**Przemysław Sołdacki:** I.

**Damian Kaminski:** MCP jest ciekawostką, o którym może pytają klienci. Może ktoś to weźmie? Nie wiadomo kiedy i tak dalej.

**Przemysław Sołdacki:** To jest kluczowy element naszego zwiększenia ARR'u, bo jesteśmy w stanie to sprzedać w kilku dużym klientem i wygenerować na przykład 200000 rocznego przychodu.

**Damian Kaminski:** OK. Ale to już jesteś pewny, że jakbyśmy to mieli, to byśmy to za dwa dni sprzedali?

**Przemysław Sołdacki:** No Rosman to zamówił.

**Damian Kaminski:** Mówił? OK, no dobra, to ja tej wiedzy nie mam.

**Janusz Bossak:** Ja też nie mam.

**Przemysław Sołdacki:** No Rosman uruchamia na 3 miesiące taki proof of concept – jest tam skłonny płacić i chce mieć już wersję advanced, ale przez 3 miesiące będzie płacił tylko za wersję standard, czyli będzie płacił.

**Janusz Bossak:** Zamówił.

**Przemysław Sołdacki:** Nie wiem, ile tam – 4000 z hakiem miesięcznie, czyli 50000 rocznie, ale nie – więcej, bo oni za dwa serwery, to tam – no więc jak kilka 1000 miesięcznie będą płacić za to?

**Damian Kaminski:** No dobra, abstrahując od tego – według mnie tu jest jakiś problem komunikacyjny, bo skoro ty o tym wiesz, a my nie traktujemy tego jako coś, co już za chwilę ma być sprzedane i produkcyjne, no to tutaj nasze, że tak powiem interesy się ścierają.

**Janusz Bossak:** Zlecenie.

**Przemysław Sołdacki:** To dobrze, że rozmawiamy, więc macie?

**Damian Kaminski:** No tak, a teraz w drugą stronę jeszcze tylko kończąc ten wątek – generowanie dokumentacji. Jeśli to sobie dopracujemy, a według mnie to wcale nie wymaga dużo nakładów – to jest, nie wiem kilka, kilkanaście godzin.

**Janusz Bossak:** To jest znaczy.

**Damian Kaminski:** To to jest mega użyteczna rzecz, która od razu przynosi oszczędności w firmie.

**Janusz Bossak:** No trochę więcej.

**Damian Kaminski:** Bo.

**Janusz Bossak:** Tak znaczy.

**Damian Kaminski:** Bo to od razu korzysta.

**Przemysław Sołdacki:** Co więcej, generowanie dokumentacji wstawiłbym jako element licencji AI.

**Janusz Bossak:** No.

**Przemysław Sołdacki:** Wersji chociażby standard.

**Damian Kaminski:** Poczekaj, poczekaj, poczekaj – tylko element licencji. Dobra, to inaczej co ja rozumiem pod pojęciem generowanie dokumentacji – każde wdrożenie kończy się tym, że musimy wygenerować dokumentację do procesu. Nie mówię o żadnych innych dokumentach, konfiguracji systemu i tak dalej – do procesu, czyli jak przejść przez proces, instrukcja procesu. To rozumiem pod kątem generowanie dokumentacji. Jeśli my to dostarczymy.

**Janusz Bossak:** Nie, nie, nie, nie, nie – szerzej, szerzej.

**Damian Kaminski:** Ale poczekaj – można szerzej, ale to jest takie MVP, które dotyczy każdego wdrożenia, bo mamy wdrożenie dla 20 użytkowników. Oni nie mają wiedzy w ogóle i tam jest tylko i wyłącznie biznes i oni oczekują instrukcji do procesu. Na jakim etapie, co mogą przycisnąć, jakie będzie konsekwencja tego zdarzenia? I ja nie mówię, że nie można tego rozbudowywać szerzej – masz rację Janusz. Tylko jak dostarczymy instrukcje do procesu, czyli jak można stworzyć proces, jakie są przyciski, jakie są pola – to z automatu na każdym wdrożeniu, a szerzej bym powiedział – wdrożeniu każdego procesu oszczędzamy co najmniej dzień pracy. Każdego procesu co najmniej dzień pracy, bo ja wiem ile to trwa, zanim nasi ludzie to wyprodukują, bo przy tym byłem i widziałem jak to się w męczarniach tworzy. Ja uważam, że to jest rzecz, którą powinniśmy zaopiekować.

**Janusz Bossak:** Bardziej, że mamy już tutaj mówiliśmy proof of concept tego, że to się da. Mateusz to jest – wiesz, sprawny w tych rzeczach i chętny do robienia. Więc możemy jego zagospodarować i on ma wtedy te dwa tematy. Tak, to generowanie dokumentacji i te MCP – MCP już też zrobił jakieś tam w pierwotnym stanie. Teraz trzeba weekendu. Tak, bo z ciekawości – to jest właśnie taki człowiek. Wiecie, on po prostu się tym jara i lubi te rzeczy i.

**Przemysław Sołdacki:** W weekend. Takich ludzi potrzebujemy.

**Janusz Bossak:** I kombinuje sobie coś tam, więc dajmy mu to poletko, niech on się tym bawi i nie wymyśla nowych rzeczy w tym zakresie, bo z tego powstaną po prostu fajne rzeczy. Jego trzeba ukierunkowywać, więc jeżeli.

**Przemysław Sołdacki:** Tylko Janusz to co ty sam mówiłeś, że musimy mieć przypadki użycia. Bo ja ostatnio specjalnie napisałem przypadki użycia, dlaczego nie może być tak, że ktoś sobie jak generuje token tylko to musi poprawnie jakiś tam – o metryki, opisałem przypadki użycia. Tak więc tutaj jeśli chodzi o generowanie dokumentacji, to ja się zgadzam, że na razie mamy takiego PoC'a, gdzie opis procesu się robi, ale mówiliśmy sobie zaprojektować, że klikam sobie guzik „generuj dokumentację", pojawia mi się lista checkboxów, gdzie mam różnego rodzaju raporty.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Mhm.

**Przemysław Sołdacki:** Mogę kliknąć „wygeneruj wszystko" albo generuje tylko jeden proces albo tylko ustawienia systemowe. Więc to można by ten przypadek użycia opisać, po to, że jak już tam robimy to pewnie takie okienko to tam Mateusz wygeneruje w dwie godziny, bo to – użyje AI do tego – tylko trzeba jakieś tam endpoint i wywołać. Bo chodzi o to, że rzeczywiście gdybyśmy mieli jakby biznesowo dwie korzyści dla nas są – to, co mówi Damian, zmniejszamy koszty wdrożeń, skracamy – po prostu na koniec konsultant klika „wygeneruj dokumentację", wychodzi dokumentacja. Ale druga rzecz są klienci, którzy sami sobie robią procesy i możemy im powiedzieć, słuchajcie, żebyście kupili tą naszą licencję na AI, to my dokładamy do niej kolejną funkcjonalność typu generowanie dokumentacji. Kupcie i patrzcie – nam subskrypcję za AI i to będziecie sobie generować, bo nawet ostatnio rozmawiałem z Dawnym Cezarem, czyli z Res Invest – i kolesie. Więc sprzedałem ten pomysł, że może sobie wyeksportować i XML i przy dokumentacji koleś mówi, no to spoko. Posiedzę i to aktualizuje opisy procesów. I jak damy mu gotować.

**Janusz Bossak:** Właśnie to jest kluczowe, co powiedziałeś – aktualizuje opisy procesów.

**Przemysław Sołdacki:** Tak, tak.

**Janusz Bossak:** To klienci wprowadzają. My też wprowadzamy zmiany po każdym.

**Przemysław Sołdacki:** No dokładnie, dlatego generowanie dokumentacji jest ważne nawet z poziomu SLA.

**Janusz Bossak:** Dlatego. Dokładnie. To co Damian powiedział, że to jeden dzień zajmuje – to jeden dzień po każdej zmianie, bo trzeba – jak za miesiąc, za dwa dokonujemy jakieś aktualizacji.

**Przemysław Sołdacki:** Dokładnie.

**Damian Kaminski:** I ja się z wami w 100 procentach zgadzam, tylko to są już rzeczy, o które rzadziej dopytują, a w takim LOTcie.

**Janusz Bossak:** No dobrze, to zróbmy tak.

**Damian Kaminski:** To lekko powiem – 6 dni będzie kosztować ta dokumentacja. Jak zrobimy to przed tym, zanim skończą – to 6 dni zaoszczędzimy i czasu i pieniędzy.

**Przemysław Sołdacki:** No tak, dokładnie.

**Janusz Bossak:** W każdym WIMie, w LOTcie, w.

**Damian Kaminski:** Bo tam jest kilka procesów i do każdego procesu trzeba zrobić dokumentację.

**Przemysław Sołdacki:** Więc jeśli rocznie oszczędzimy na przykład 60 dni? To jest bardzo dużo. To jest dwie, trzy osobo-miesiące. To jestem w stanie podać tak.

**Damian Kaminski:** No myślę, że lekko.

**Janusz Bossak:** Spodnie lekko to jest lekko lekko.

**Damian Kaminski:** Lekko.

**Przemysław Sołdacki:** No to słuchajcie, to jest w kontekście tych zadań nawet, co tam Janusz menedżerskie. Tak, jeśli znaczy – generalnie cała roadmapa na ten rok, tak? Bo możemy sobie napisać – oszczędność nie wiem 50000 rocznie, 100000 rocznie. To jest spoko dla mnie, bo to zwiększanie rentowności. Jeśli dodatkowo dodajemy to i znajdziemy 10 klientów, którzy kupią licencję tam 4000 z hakiem miesięcznie, czyli 50000 rocznie, to mam pół miliona rocznie i to jakby ten sposób myślenia – powinniśmy każdą rzecz... MCP to nakłoni klienta, żeby kupił wersję advanced – 100000 rocznie u dużego klienta, mniejszego tam jest proporcjonalnie mniej, bo mamy kilka poziomów.

**Janusz Bossak:** Czy w sumie – ja bym był naprawdę jeszcze bardzo, ale to bardzo ostrożny. Tak? Kwestia wydajności – znaczy pierwsza kwestia oczywiście security, druga kwestia wydajność, żebyśmy nie zabili AMODIT'a po prostu takimi rzeczami, bo AI będzie pytało się może nie optymalnie różne rzeczy.


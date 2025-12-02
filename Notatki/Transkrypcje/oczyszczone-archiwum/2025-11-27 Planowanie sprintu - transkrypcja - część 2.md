**Data spotkania:** 27 listopada 2025, 13:30 - część 2

---

**[Janusz Bossak]:** Tutaj można by Mateusza jakby przy tym pozostawić. Trochę go oderwać tam od tych serwerów MCP i one są zaplanowane tak naprawdę na pierwszy kwartał. Dopiero no już tam jakieś rozpoznanie zrobił. Dzisiaj mi się tam chwalił tym bardzo mocno. No ale nie jest to takie ważne jak to nie i to indeksowanie jest tutaj uważam dużo ważniejsze i trzeba się tym zająć. Więc ja bym mu dał takie zadanie właśnie, żeby on się tym indeksowaniem zajął od strony. Procesu, tak, czyli na razie do takiej wersji podstawowej potrzebujemy. Sytuacji, w której po stronie procesu. No i teraz pytanie to do was Kamila. Czym wy już tylko o tym nowym? Znaczy, nie, nie wiem, w którym miejscu to zrobić. Nie o to mi chodzi technicznie, no bo teraz jest tak zrobione, że jest w tych ustawieniach procesu. Taki. Przycisk on wyświetla okienko i w tym okienku tam coś można tego JSON podejrzeć. Jakoś tak Piotr mówi z tego co ja zrozumiałem, że teraz to jest tak zrobione, że to bierze wszystko nie i tam niby indeksuje wszystko, więc to nie jest rozwiązanie optymalne.

**[Damian Kaminski]:** Wszystkie tekstowe.

**[Janusz Bossak]:** No i właśnie to jest pytanie jak to zrobić, tak, czyli. Czy to robić? Znaczy mój pomysł o tak mój pomysł jest taki, żeby to robić przy. Jakimś konkretnym polu, tak, czyli jestem i to Kamil raz do ciebie, tak, czyli jestem na jakimś edycji pola, wyświetla mi się ten prawy. Panel tego pola i mogę. Gdzieś nie wiem jeszcze gdzie powiedzieć, że to pole ma być indeksowane.

**[Damian Kaminski]:** Ja uważam, że nie. Już tłumaczę czemu. To znaczy, według mnie powinna być jedna spójna lista, bo tak ilość indeksów musi być ograniczona, żeby miało to sens. Musisz widzieć, które są zaindeksowane z jakieś poziome właśnie listy, żeby miało to sens, bo tak to oznacza, że każdy oddzielnie albo jak chcesz znaleźć, które są zaindeksowane, to nie wiesz. I teraz. Kolejna rzecz zastanawiam się, czy to na pewno robić na polach. Bo ktoś projekt czy to nie powinno być właśnie w jakiejś zakładce ustawienia, bo to nie jest rzecz taka. Ani łatwo zrozumiała dla osób, które które nie wiedzą, co to znaczy sobie klikać od kiwać, jak uważają. No i zastanawiam się, że to upychać w w projektowanie formularze, bo w zasadzie mówisz o tym ekranie tak projektowania formularza, a nie. Stricte już wydajnościowy mi kwestiami, które mają wpływ na raporty.

**[Kamil Dubaniowski]:** Czy ja też podejrzewam, że indeksowanie? No nie tylko na raporty, bo interesowaliśmy też Rossmann, żeby odnośnik do procesu tego działało. Lepiej sprzedają się, że indeksowanie wpłynie jakby nie tylko raporty i to trochę się przykłada, że ma sens to ustawienie pola.

**[Damian Kaminski]:** No. Tak masz.

**[Janusz Bossak]:** Tylko, że chyba to są 2 różne indeksowania.

**[Kamil Dubaniowski]:** OK.

**[Damian Kaminski]:** Może też tak być.

**[Janusz Bossak]:** To co my mówimy, to jest takie jakby dodatkowe trochę indeksowanie na polach tekstowych, a nie indeksowanie w rozumieniu włączenia indeksu na kolumnie bazę danych tam case.

**[Damian Kaminski]:** Kolumnie.

**[Janusz Bossak]:** Number coś, bo to jest przyspieszenie chyba z tym polem typu Odnośnik to właśnie polega na tym, że na kolumnie wstawiamy.

**[Kamil Dubaniowski]:** Dokładnie tak.

**[Damian Kaminski]:** A tutaj tylko w procesie, więc mogą być różne kolumny.

**[Janusz Bossak]:** A tutaj. A tu jest to jest tworzenie dodatkowej tabeli. Czy tworzenie zapisów dodatkowej tabeli, która jest jakby indeksowana z natury nie i dzięki temu możemy szybciej po niej wyszukiwać? No i to jest takie trochę obejście tego indeksowania bezpośrednio w tabeli case definition. A tam to jest czymś innym, chociaż no pytanie do to bardziej do Piotra, no już. Bo może to da się ogarnąć też tym, tak znaczy, że jak łączymy takie indeksowanie na polu typu Odnośnik to on po indeksuje prawdzie nie teksty tylko liczby. Bo tam będą ID tak. Tak mi się wydaje, no nie wiem, trzeba by Piotra pytać. No ale dobrze. Wracając z tego miejsca.

**[Damian Kaminski]:** Znaczy to jest, jeśli mówimy o tekście, to o o i dipsach to chyba jeśli kolumna jest liczbowa to. To nie wiem czy tam indeksowanie ma znaczenie. Chociaż no nie wiem, nie będę się tu mądrzył, no bo.

**[Janusz Bossak]:** No ale wracając do tych miejsc, no. Miejsce może być kilka, ja tam parę dni temu proponowałem, żeby to była osobna lista, to nam było mowa, że że jednak nie osobna lista, no bo to kolejna lista.

**[Kamil Dubaniowski]:** Tak, tak, to sama lista. No no znaczy wiecie ustawienia pól to jest kluczowe, tak czy my to robimy w ustawieniach procesu, to jest decyzja kluczowa, jeśli no tak to pasuje. No to ja osobnej listy tam nie widzę potrzeby dawać tylko Damian tu za w ogóle podważył, że to powinno być w ustawieniach procesu.

**[Janusz Bossak]:** Może na tej ludzi.

**[Damian Kaminski]:** Nie, nie w procesu podważyłem w ustawieniach formularza.

**[Janusz Bossak]:** Nie, no, może być ustawieniach procesu, tylko na razie jeszcze nie mamy ich zrobionych React. Ustawień procesu.

**[Damian Kaminski]:** Dlatego to może być wtórne w sensie może być na razie na poziomie bazy danych nawet.

**[Janusz Bossak]:** No nie, no to takie. Nie, nie, nie, nie, już tak tak nie róbmy. No to już.

**[Kamil Dubaniowski]:** Mamy mamy ten temat dotyczący, żeby poziomu ustawień procesu przygotować widok z tego procesu, więc mogłaby wręcz zacząć funkcjonować taka trochę niezależna zakładka albo gdzieś tam sekcja wręcz ustawień procesu, czyli może stworzyć sobie widok. Możesz właśnie za indeksować, czyli przygotowujesz źródło na bazie tego procesu.

**[Janusz Bossak]:** Ja mam no tak, dobra to teraz dygresja, ponieważ przerobiliśmy te ustawienia systemowe. Na React pytanie na ile jest skomplikowane i to jest pytanie pewnie do Przemka Nogasia. Przerobienie ustawień procesu na React. Ale taki jeden do jeden. I na razie tylko tej zakładki.

**[Kamil Dubaniowski]:** Wydaje mi się, że to bardziej pytanie do kogoś z backendu, no bo kto wie, czy zrobi 2 dni, ale tutaj chodzi o to, żeby wystawić te wszystkie dane, które to musimy pokazać.

**[Damian Kaminski]:** Dokładnie to jest backend.

**[Janusz Bossak]:** Bo to to mógłby być pierwszy krok, tak, zróbmy to i wtedy już na tym React. Frontendzie możemy dodać sobie. Tą funkcjonalność właśnie ustawiania indeksów i to może być wtedy. Pawelka. Do której dodaje pola, które mają być indeksowane.

**[Kamil Dubaniowski]:** Dokładnie i wtedy mam znów tak, no bo na wtedy na na na tym widoku ogólnym listy kolejna kolumna, która pokazuje ci, które pola są indeksowane. Która jeszcze nie na przykład, żebyś miał takie ogólne o zdrowiu, a tak to masz tylko te, które indeksuje już do damy.

**[Janusz Bossak]:** Być może być może być to taki widok trochę jak mamy na raportach. Jest. To on kontener z polami i po prawej stronie tego kontener. Na drugi kontener z polami indeksowanymi nie i sobie przenosić, że to pole chce, żeby było indeksowane, to ono się tą indeksuje. I tyle. I na tej liście pól. Dostępnych do potencjalnie możliwych do zaindeksowania wyświetlają się tylko te, które rzeczywiście można zaindeksować. Tak, czyli jakieś tam listy wyboru pola tekstowe i tak dalej. A ten prawy kontener, który zawiera listę pól indeksowanych czy zaindeksowanych, no to mógłby mieć na przykład ograniczenie, że można tam wstawić 10. Jak chcesz to możesz jedno wyjąć drugie włożyć.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Tam mogłoby być.

**[Damian Kaminski]:** Tylko nie mamy nigdzie takiego. Chyba jeszcze komponentu. Pytanie jakie mamy inne?

**[Janusz Bossak]:** Tak, no.

**[Damian Kaminski]:** W raportach mamy no tak, no dobrze, tak masz rację.

**[Janusz Bossak]:** Tego typu.

**[Kamil Dubaniowski]:** Czyli ja też jeszcze się zastanawiam tak, no bo. Kto będzie wiedział to to zrobi. Kto nie będzie wiedział, to będzie musiał się dowiedzieć OK, ale czy nie możemy podejść do tego wrócić do pomysłu od strony? Czyli wtedy właściwie, ale tak, ale wtedy, czy potrzebujemy, czy potrzebujemy tego poziomu po stronie ustawień procesu, bo moglibyśmy zrobić to tak, że obsługa właściwie jest tylko po stronie bazy danych, czyli nawet tak mamy taką po prostu tabelę, gdzie przechowujemy te informacje. Polach, które są indeksowane, które nie, ale w momencie, kiedy ja wrzucam taki typ pola, jak lista wyboru, czy tam słownik czy co, to ma się indeksować do filtrów, to w tle AMODIT sobie dodaje, że ma zaindeksować to pole.

**[Damian Kaminski]:** O nic się nie wyklucza. Kamil, to jest w MVP. Tak. No. No.

**[Janusz Bossak]:** No tak, tak znaczy ja też tak.

**[Damian Kaminski]:** No znaczy tu jest więcej, według mnie to płytko to rozpatrujesz, bo teraz tak po pierwsze, czy on ma domyślić się czy ty raczej musisz to od klikać, że za indeksu.

**[Kamil Dubaniowski]:** Nie, no ma się domyślić, no bo jakby tak będę musiał zrobić, jakby będzie mi to działało inaczej niż się spodziewałam. Te filtry inaczej będą działały.

**[Damian Kaminski]:** No dobra ma się domyślić, no ale. Dobra, ale ilość indeksów, żeby to miało miało chyba sensu musi być ograniczona, chociaż nie wiem to na kolumnach, może tutaj jak ta tabela nie wiem, ale chyba sobie to znaczy to sobie potwierdziliśmy, że ona będzie jakkolwiek ograniczona. Nie to Piotr potwierdził. I teraz wyobraź sobie sytuację taką. Że no tych raportów jest wiele, czyli teoretycznie jest 5-20 pól, które potencjalnie możesz zaindeksować, a możesz mieć 10.

**[Kamil Dubaniowski]:** No ale to no poziom procesu schodzi, rozumiem, a nie ogólnie 20 w całym systemie indeksowanych.

**[Janusz Bossak]:** Znaczy.

**[Damian Kaminski]:** Teraz. Nie procesu per process.

**[Kamil Dubaniowski]:** No właśnie, no to teraz o to chodzi. Ile masz słowników po których filtrujesz? W procesie pracy takich, tak w sensie takich select list mogło to o to chodzi.

**[Damian Kaminski]:** Się ile masz pól? No wiesz, my możemy coś założyć, a życie pokaże to co chce, a poza tym teraz pytanie, kto może to zrobić, czy jak użytkownik dowolny sobie robi raport z procesu jakiegoś dużego? No to co on może tam dodawać i będziemy ładować to jak chcemy. W sensie wszystko co on poda, to będzie indeksowane.

**[Janusz Bossak]:** No. Znaczy, wiecie, no jest wiele pytań bez odpowiedzi, no.

**[Damian Kaminski]:** Ja bym to zrobił na poziomie procesu jako MVP, potem bym się zastanawiał nad usprawnieniem.

**[Janusz Bossak]:** Dokładnie też tak, tak, tak, tak, zróbmy to.

**[Damian Kaminski]:** Poza tym może być konflikt, czyli coś ustaliliśmy i OK, ale przede wszystkim to bym zaczął jeszcze od czegoś innego, czyli bym zaczął od uzysku, który daje ta funkcjonalność.

**[Janusz Bossak]:** Znaczy.

**[Damian Kaminski]:** Tak na chwilkę, bo tak to, że to będzie sprawniejsze to OK. Natomiast co jest celem tej indeksacji? Celem jest to, że tutaj się będą, że tu się pojawiają te informacje, tak.

**[Janusz Bossak]:** No i że ty się czujesz po tym zdecydowanie to zdecydowanie jest łatwiejsze wyszukiwanie.

**[Damian Kaminski]:** To jest celem. I żeby co. No dobra, ale to to już jest skutek, czyli kwestia optymalizacji. Tak natomiast skąd się wzięło to wszystko stąd, że tu wyświetlało się nie wszystko.

**[Kamil Dubaniowski]:** Nie, że Piotrek powiedział, że nie zgadza się, żeby orać pokryć z definicją.

**[Janusz Bossak]:** Dokładnie. O to chodzi. Jakkolwiek.

**[Damian Kaminski]:** No dobra, tylko wiecie, cała dyskusja zaczęła się od tego. Że. Wpisuje, że LP wpisuje haus kilka zaznacz wszystko a nie wszystkie hausty się zaznaczają.

**[Janusz Bossak]:** No tak i błędu tego, które pokazywał Przemek Sołdecki także wyskakuje wigilia a nie ma a nie ma reszty, tak.

**[Damian Kaminski]:** Tak, że nie przeszukuje wszystkiego. Tak więc w zasadzie nam się tu coś wyświetla, piszemy. W mich. Ja nie wiem czy ten z miejsc to są to na pewno jest cały zakres raportu czy czy nie, bo dzisiaj tego nie wiemy, to znaczy no już tam niby jest ten, ale. Dalej tu może być więcej, bo to jest jakoś limitowane, czyli no nie dalej nie wiemy.

**[Janusz Bossak]:** To to może to możesz wziąć teraz tylko, że to użytkownik nie wie tego. Weź tam zamiast równa się zawiera i napisz SMI znajdziesz dużo więcej, no.

**[Damian Kaminski]:** A no dobra, masz rację właśnie tylko użytkownik tego nie wie. I teraz pytanie jak zrobić, żeby to było dla użytkownika oczywiste?

**[Janusz Bossak]:** Dlatego. No w ten sposób, że to jest jedna z moich propozycji, że dla niektórych typów pól można z góry przewidzieć, jakie powinny być. Operatory, czyli jeżeli daje nazwisko do. JRWA użytkownika to na przykład domyślnym operatorem nie jest równa się tylko zawiera. A tak naprawdę.

**[Damian Kaminski]:** No właśnie dokładnie i teraz, bo to co mówimy o tych proszę.

**[Janusz Bossak]:** Ale. Ale wiesz, że to już można zrobić?

**[Damian Kaminski]:** Już można tak, czyli domyśl.

**[Janusz Bossak]:** To zawsze mogę. Znaczy zawsze od momentu, kiedy zrobiliśmy tu ustaw wartość domyślną. I teraz zamiast robić to równość i robisz, zawiera i zapisz.

**[Damian Kaminski]:** No OK, to tego nie wiedziałam, bo to wynika już zmian, które to nie tak dawno 2 miesiące max to jak Łukasz prowadził do myślenia. Filtry, tak.

**[Janusz Bossak]:** No, no, no. I teraz jak weźmiesz tu klikniesz nazwisko?

**[Damian Kaminski]:** No nie działa, czekaj.

**[Janusz Bossak]:** Jestem pewny.

**[Damian Kaminski]:** To też no nie działa? Czekajcie, wyczyść.

**[Janusz Bossak]:** Wiem, że to się zapisało. No, no.

**[Damian Kaminski]:** Może jednak, ale jesteś pewny, że to działa?

**[Janusz Bossak]:** Tak znaczy, ja robiłem to.

**[Damian Kaminski]:** Dobra, nie na tym ustawiłem, nie na tym ustawiłem. Przepraszam moja wina już jeszcze raz no nazwisku ustawiona dokumencie zawiera. OK jest.

**[Janusz Bossak]:** No i tu jak sobie klikniesz to, że zawiera nie, no i teraz stan możesz wybrać wpisać ten syn. My więc jak chciałeś?

**[Damian Kaminski]:** No tak, no to będzie ten sam wynik akurat, bo to nie są te dane, które to pokazują, ale ale tak chociaż.

**[Janusz Bossak]:** I teraz kolejną rzeczą, którą można by jakby usprawnić takim w ramach wydajności. A my to jest to, żeby to szukało od początku, bo teraz zawiera to jest. Procent.

**[Damian Kaminski]:** Procent procent.

**[Janusz Bossak]:** A bardzo wielu przypadkach zdecydowanej większości przypadków. To jednak szukamy czegoś od początku. To mogło być też opcją pola. Nie, że szukaj od początku, albo szukaj w całym polu tego nie mamy w ogóle w tej chwili. Albo jako operator tak, że zawiera, czy zaczyna się od. To są takie uprawnienia, które można robić niezależnie od tego indeksowania nawet. Takie same usprawnienia zaproponowałem tam Przemek, już częściowo to zrobił do daty. Nie jeżeli daty bierzemy, weź kliknij tam obok ten daty utworzenia.

**[Damian Kaminski]:** No, to żeby domyślnie było od do.

**[Janusz Bossak]:** Tak i tutaj niekoniecznie od do, żeby tu były najpierw takie rzeczy, które są najczęściej. Wybieramy najczęściej wybieranym jest bieżący miesiąc bieżący rok. Najczęściej patrzymy bieżący dzień, tak, ale najczęściej bieżący miesiąc bieżący rok. I to powinny być pierwsze rzeczy na tej liście nie, a potem jakieś tam kolejne. Poprzedni miesiąc poprzedni rok, bo to są kolejne takie biznesowo najczęstsze i tak dalej. No i to są takie proste usprawnienia, które coś tam pomagają. I tak samo tutaj można również wstawić domyślnie w ustawieniach procesu, kiedy ten filtr wybierasz, to możesz wstawić wskazać, że użytkownik ma mieć domyślnie coś tam.

**[Damian Kaminski]:** No, znaczy zastanawiam się nad tym, co powiedziałeś, czy najczęściej jest faktycznie to, co powiedziałeś?

**[Janusz Bossak]:** Któryś z tych płaczących opcji?

**[Damian Kaminski]:** Mm nie wiem.

**[Janusz Bossak]:** Ciebie najczęściej nie znaczy zawsze. Ale często no najczęściej robisz raporty dotyczące czegoś bieżącego, tak albo jakiegoś bieżącego miesiąca. Bieżącego kwartału bieżącego roku. Najczęściej to są takie rzeczy, nie. Oczywiście to jest tylko lista, kolejność listy, no nie znaczy, że to.

**[Damian Kaminski]:** Nie wiem, powiem ci jeszcze, że nie wiem, ja nie mam takiego podejścia. Czy czy w kontekście mowy wdrożeń, które ja robiłem? To bym tak nie powiedział. No tak, tak mówię szczerze, w sensie ze swoich doświadczeń jak ja robię raporty, przeważnie sprawy, sprawy otwarte, sprawy zamknięte.

**[Janusz Bossak]:** Ale. Ale ja mówię to polu data.

**[Damian Kaminski]:** Tak, tak, tak, ja cię rozumiem.

**[Janusz Bossak]:** Domyśl o myśl o domyślnym sortowaniu możliwości wyboru, nic więc to nie ma. Ci wstawić, że to jest bieżący miesiąc? Chodzi o to, że jak pan klikniesz, weź klikniesz raz tą datę otworzenia, może nie tu jest w dniu w tej chwili ustawione.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Ile razy robisz raport na w dniu?

**[Damian Kaminski]:** To ja nie ja nie twierdzę, że to jest dobrze, absolutnie ja bym powiedział, że najlepszym i najbardziej uniwersalnym rozwiązaniem jest zakres.

**[Janusz Bossak]:** Nie, bo jest najtrudniejsze.

**[Damian Kaminski]:** Bo ja wtedy mogę wstawić od pierwszego dziewiątego.

**[Janusz Bossak]:** Nie, bo jest najtrudniejszy, nie, bo jest najtrudniejszy. Jest jak powinny jako trzeci czwarty pierwszy to są. Zobacz, jak wejdziesz na jakiekolwiek ekonomem.

**[Damian Kaminski]:** W sensie?

**[Janusz Bossak]:** To masz zawsze zakres dat gotowy? Miesiąc ostatni rok ostatni miesiąc jak w bankowości robisz sobie jakieś zestawienie? Zawsze jest z góry, najpierw są te rzeczy, które możesz wybrać. O bieżącym w zeszłym miesiącu.

**[Damian Kaminski]:** No dobra, to ja nie będę się tutaj, jeśli tak uważasz to OK. No ja mam w sensie ja mam pewnie tutaj perspektywę siebie i tego co by mi było jakbym to widział to od razu mogę wystawić i od idei sobie stwierdzam jak mi jest najlepiej, ale może masz rację, no może ludzie nie chcą się nad tym zastanawiać.

**[Janusz Bossak]:** Nieważne, no bynajmniej takie usprawnienia możemy robić tutaj do raportu, wracając, bo żeśmy zatoczyli duże koło. Podsumowując dokończmy raporty t pod każdym ich względem. Pod względem tego drzewka tam pamiętacie, było to zgłoszenie po podpisywaniu coś tam, gdzie coś wyskakuje czy nie wyskakuje. Czy się odświeża czy się nie odświeża właśnie defil ty podpisywanie różnymi typami podpisów tutaj. Ostatnio teraz Łukasz zgłaszał to podpisywanie na polu typu podpis, tak totalnie. Więc i wszelkie błędy, które są z tym związane, jest z błędy czy sortowania czy czegokolwiek. Co tutaj może być, a tam jest tych kilkadziesiąt błędów różnych zgłoszonych. Trzeba je przejrzeć i po prostu poprawiać. To jest pierwsza rzecz, którą musimy poprawić, tak, żeby po prostu ten moduł, przynajmniej ten raport działał. Bezbłędnie by tu nie było zgłoszeń do niego żadnych. Jakieś tam te zaokrąglenia właśnie tych liczb to zresztą pamiętam były jakieś zgłoszenia co do tych nie wiem czy tutaj działają, bo miały działać. Pamiętam kiedyś podsumowanie, nie wiem czy to działa w tej chwili czy nie. Ale kiedyś były tam.

**[Damian Kaminski]:** Był, nie wiem czy działają.

**[Janusz Bossak]:** Wszystkie eksporty właśnie żeby działały dobrze, tak? No jestem jakoś tam.

**[Damian Kaminski]:** Jest konieczny strony, ale to nie wiem, nie wypowiadam się, czy to jest dobrze, czy źle, może i dobrze.

**[Janusz Bossak]:** Bo jak to? Kliknij tam na lewym drzewku na przykład cloud albo tamten koma dzie jest 14 i to wtedy powinien to pokazać tylko to z przefiltrowany.

**[Damian Kaminski]:** No to już widać, że tak nie działa. Tu nie ma wartości 9000, tu jest sponsorowany po i d. 8 czy 8 249 to jest najwyższa wartość?

**[Janusz Bossak]:** No tak, ale kliknij to koma tam z lewej strony.

**[Damian Kaminski]:** Aha, czyli filtr uwzględnia apel pingu nie, tak.

**[Janusz Bossak]:** No tak, no bo jak nie masz nic wybrane to pokazuje ci maksymalne w ogóle, który widać znaczy nie widać, który w ogóle występuje.

**[Damian Kaminski]:** OK. Którego nie widać. No właśnie OK maksymalny staje ze wszystkich danych ze wszystkich stron OK.

**[Janusz Bossak]:** Jak wybierzesz coś tam ten Kamiński czy koma czy Kowalski?

**[Damian Kaminski]:** No dobra, to już wtedy uwzględniam.

**[Janusz Bossak]:** Widzisz, to inny błąd, który jest też wkurzający, znaczy wiesz, tu jest mnóstwo tych błędów, nie. Znaczy to akurat nie błąd, weź wejdź w edycję. Bo nie wiem czy to jest w ramach też bordo czy tutaj. Wejdźmy decyzję na chwilę, proszę?

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Wejdź w ogólne.

**[Damian Kaminski]:** Ogólne.

**[Janusz Bossak]:** Ogólne nieobcy tylko ogólne.

**[Damian Kaminski]:** O przepraszam.

**[Janusz Bossak]:** I właśnie coś wpisz w tym rejestracja nowy, dopisz nam jakąś jedynkę. Gdzie raporcie?

**[Damian Kaminski]:** Że przeładował.

**[Janusz Bossak]:** No i za każdą literką jak będziesz wpisywał to będzie się przecież to jest. No to na na dashboard też to występuje nie więc to nie może być coś takiego, że raport się przeładowuje dlatego, że nazwę zmieniasz. Co to ma wspólnego jedno z drugim co ma nazwa do przeładowywania raportu? I strzelania do bazy danych, tak, żeby pobrać raport. Dalej czyli. Skupmy się na tym poprawianiem. Najgorzej znaczy najgorsze, no problem znaczy krytyczna jest to, że to poprawianie nie dotyczy tylko i wyłącznie frontend tak wielu przypadkach dotyczy jednego i drugiego, a najczęściej weekendu. Dobra, słuchajcie, zostawmy te raporty, bo. Byśmy nie tracili czasu i JRWA. Repozytorium. To są rzeczy, które zajmujemy się teraz mamy.

**[Damian Kaminski]:** Repozytorium możemy omówić, bo mam kilka pytań.

**[Janusz Bossak]:** Koniec listopada początek grudnia następnym sprincie musimy wydać działające repozytorium.

**[Damian Kaminski]:** Tak jakbym chciał.

**[Janusz Bossak]:** Tak musi być. No.

**[Damian Kaminski]:** No nie tylko ode mnie to zależy, ale tak no mogę wam pokazać co mamy. Po pierwsze decyzja, gdzie to repozytorium osadzamy, bo na razie jest tu.

**[Janusz Bossak]:** Boli nam się ta lista rzeczy tutaj rozwija.

**[Damian Kaminski]:** No to te 2 to są opcjonalne, tak tylko jeśli faktycznie, no ale tak no repozytorium plików jest niezależny od procesu, więc. Albo tu albo robimy dodatkowo na dole, ale no powiedziałbym tak, komunikator okurat jest istotny, że tu repozytorium co do zasady raczej nie będzie miało znacznika ilości. Nie będziemy tu nikogo wywoływać. Więc jest jakaś?

**[Janusz Bossak]:** Ono powinno być trochę, jak tam się, że gdzieś tam możesz sobie podpiąć gdzieś.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Ale nie powinno być chyba tak eksponowane od razu.

**[Damian Kaminski]:** No rozumiem OK jak najbardziej w sensie. Może być może się okaże, że właśnie. No bo. Teraz tak tu mamy przelewy bankowe, nadawcę to też jest są takie specyficzne.

**[Janusz Bossak]:** A jak wyszukiwanie tam losowane tak też jest z modułem nadawcy, jest modułem przelewy, jest modułem. No to tak powinno być raczej jako te moduły, nie.

**[Damian Kaminski]:** Moduły. I teraz. No to może tak to trzeba zrobić, że niezależny można podpiąć w tej w różnych miejscach, ale zawsze wyświetla to samo. Bo to tu włączamy, tak? OK no to można to dorobić i tu.

**[Janusz Bossak]:** Tak mi się wydaje, że to trzeba w tych ustawieniach obszarów zrobić, że to się włącza tam i to w danym obszarze. Wtedy jest tak domyślnie może być w obszarze wszystkie procesy. Ale jak ktoś chce to sobie gdzieś indziej, bo tak jak powiedziałeś komunikator będzie miał tam prawdopodobnie jakieś. Ilości no bo możemy mieć ileś tam nowych, jakieś zmiany czy coś i to możemy tutaj wyświetlać.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** A poza repozytorium plików nie pozornym plików jest modułem tak jak właśnie mówimy nadawca. Czy to jest zresztą podobny trochę tak, bo nadawcy, czy w innych też mamy jakieś takie po lewej stronie coś? I tak tam mi to pasuje. No dobra, co dalej z tym repozytorium?

**[Damian Kaminski]:** No dobrze, na ten moment to co mamy to jest zarządzanie tylko drzewem. Klikamy jeszcze nie możemy uprawnić żadnych nie mam, mamy tylko drzewo i to będzie zakończenie tego sprintu. I teraz tak, jeśli chodzi o zarządzanie drzewem.

**[Janusz Bossak]:** Czy w tym sprincie, którym jesteśmy, będziemy mieli to zarządzanie drzewem?

**[Damian Kaminski]:** Tak.

**[Janusz Bossak]:** Już takie beke.

**[Damian Kaminski]:** Już w zasadzie je mamy, to już jest to już jest git.

**[Janusz Bossak]:** O i to już jest na tym wydaniu tak co?

**[Damian Kaminski]:** Tak repozytorium mam lokal.

**[Janusz Bossak]:** OK.

**[Damian Kaminski]:** Tak no nie wszystkie jeszcze testy są zrobione i tak, ale to już jest samolot to już działa nie i no co można dodać nowo nowe repozytoria teraz tak co do ikonek, bo one też tak zostały przeze mnie tam wymyślone w tym mockup i tu skopiowane. Pytanie, czy to jest OK, czy tu stosujemy te kolory, bo tutaj ich nie stosujemy?

**[Janusz Bossak]:** No to są drobiazgi to.

**[Damian Kaminski]:** No dobra, to są drobiazgi, no ale jak już gdzieś tam to wyznacza, będzie do tego ewentualnie wrócić. Sugestia była taka, że tu się nie wyświetlają foldery na razie się wyświetlają, ale tak naprawdę to co wyświetla się tu, to jest jeden wielkim mockup. To znaczy nie w sumie to już akurat korzysta. Czekajcie, czy tu już zrobił? OK już to wszystko podpisze. Już tu nie ma chyba danych plików dobra nie ma. No więc tak to co jest do wywalenia to jest to. Ale teraz.


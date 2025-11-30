Data spotkania: 17 listopada 2025

**Adrian Kotowski**: Cześć.

**Patrycja Walaszczyk**: Cześć.

**Mateusz Kisiel**: Cześć.

**Mariusz Piotrzkowski**: Cześć, czy to spotkanie mieliśmy mieć? Czy ono było odwołane tydzień temu? Nie pamiętam jak to miało wyglądać.

**Mateusz Kisiel**: Nie wiem, jest wpisane, to wszedłem.

**Mariusz Piotrzkowski**: OK, coś było mówione, że to będą spotkania tylko dla PM-ów. Nie pamiętam, jak to było w końcu ustalone dwa tygodnie temu, w poprzednim sprincie.

**Michal Zwierzchowski**: Coś pytałeś, ale nie wiem o co.

**Mariusz Piotrzkowski**: Pytałem, czy to spotkanie ma się odbywać przy każdym sprincie, bo w poprzednim było mówione, że chyba będziemy je pomijać. Jakieś ustalenia w tym temacie były.

**Michal Zwierzchowski**: Aha, dobra. Kamil i Janusz będą wiedzieć.

**Janusz Bossak**: Ja już jestem. Mieliśmy spotkanie odnośnie planowania sprintu w innym gronie.

**Damian Kaminski**: Dobrze, to ja mogę wyświetlić. Wzorem poprzedniego spotkania sprzed dwóch tygodni, przygotowaliśmy to w sposób analogiczny. Jeśli ktoś nie będzie uwzględniony, to dajcie znać. Może najpierw to omówimy, a potem się do tego ustosunkujemy. Jeśli macie jakieś uwagi co do sposobu zarządzania i prezentowania tego w taki sposób, to wszelkie komentarze są mile widziane.

Zacznę od obszaru, którym ja będę się opiekował, czyli repozytorium plików. Tutaj mamy nowe podejście, którego jeszcze nie mieliśmy, czyli jest wytworzona w ramach Azura rozpiska po nowemu. Janusz już to wstępnie pokazywał – całe drzewko tego, co mamy zrobić, od epika poprzez ficzery i PBI na końcu. Jest tego po prostu dość sporo naprodukowane i chciałbym tutaj zaangażować Adriana i Anię jako zespół backendowy i Filipa jako frontend. Częściowo to repozytorium plików mamy już zrobione. Może gdzieniegdzie jest ono aż nadto rozbudowane po stronie frontendowej, będziemy to w ramach MVP gdzieś tam ucinać, czy też decydować, że dane przyciski nie będą na razie realizowane. Natomiast pierwsze co, to musimy się spotkać i omówić to, co zostało przeze mnie przygotowane na podstawie wytycznych Piotra co do zmiany struktury samej bazy danych, a dalej endpointów, które mają realizować te zadania. Musimy omówić, czy to, co przygotowałem ma sens, czy macie na to jakiś lepszy pogląd, czy można coś uprościć. Według mnie jest to dużo szerzej opisane niż w niektórych przypadkach tego potrzebujemy, co spowoduje, że pewnie dłużej będziemy to tworzyć. Pytanie, czy to wszystko jest nam potrzebne? Wrzuciłem nam wstępnie na jutro spotkanie. Może jeszcze uda nam się dzisiaj złapać, chociaż po tym spotkaniu mam jeszcze jedno handlowe. Natomiast nawet jeśli się nie uda dzisiaj, tylko jutro, to wyślę wam, w jaki sposób powinniście się z tym zapoznać. Dokumentacji jest troszeczkę i chciałbym, żebyście przynajmniej taki pogląd ogólny w zakresie biznesowym do tego mieli, żebyśmy jutro rozmawiali już o szczegółach technicznych.

W kontekście tego wątku, czy ty Kamil chcesz jeszcze poruszyć jakiś duży temat, czy mam przechodzić po poszczególnych osobach?

**Kamil Dubaniowski**: Myślę, że możesz w ten sposób.

**Damian Kaminski**: Dobra, to tutaj akurat Tatiana byli w to zaangażowani. Kontynuując, Adrian, rozpisałeś zadania w ramach certyfikacji. Z tego co oszacowałeś, widziałem, że było to 3,5 dnia na poprawki, 1,5 i 2 dni na szacowanie. Chcielibyśmy Cię jeszcze wykorzystać w kontekście architektonicznym pod repozytorium, no i wykonawczym, bo tam dużo jest tych endpointów wstępnie zaplanowanych.

W kontekście Comarch Hub, czy jesteś w to zaangażowany? Czy ten temat jest jeszcze aktualny i czy zakres jest już ustalony?

**Adrian Kotowski**: Zakres jest ustalony. W tamtym tygodniu mieliśmy dostać dostępy. Łukasz, nie wiem, czy dostałeś do dokumentacji tego API.

**Lukasz Brocki**: Mamy zaplanowane, co trzeba robić. Mam dostęp do dokumentacji, trzeba zaczynać programowanie. Plus potrzebujemy dostępów.

**Damian Kaminski**: Adrian, jak rozumiem, pozostaje tylko w kontekście doradczym? Taki był cel, że Łukasz to wszystko robi.

**Adrian Kotowski**: Tak, na razie tak.

**Damian Kaminski**: OK. Jeśli chodzi o Anię, to tylko to repozytorium plików plus ewentualnie to, co teraz kończysz. Mówiłaś rano, że jeszcze kończyłaś te szablony?

**Anna Skupinska**: Może mi to trochę dłużej zająć, dlatego, że zrobiłam, żeby one działały. Teraz pracuję nad tym, żeby można było je obracać. Problem jest taki, że od strony kodu jest sporo powtarzalnego kodu. Żeby to zrefaktoryzować, trzeba będzie trochę popracować, bo trzeba wydzielić element wspólny z szablonów i załączników, i zrobić z nich część wspólną, w której będą wszystkie operacje, pod tytułem zapisywanie do podglądu, tworzenie podglądu, obracanie.

**Damian Kaminski**: Czekaj, mówisz teraz o obracaniu?

**Anna Skupinska**: Nie tylko o obracaniu. Chodzi o to, że teraz, jak to zrobiłam, jest sporo skopiowanego kodu, który się powtarza.

**Damian Kaminski**: Dobra, to ja bym to uciął. Warto by się w tym temacie może spotkać, bo może to jest coś, czego nie przewidzieliśmy.

**Lukasz Bott**: Dokładnie to miałem powiedzieć.

**Damian Kaminski**: Mam poczucie, że rezygnujemy z tego na razie. To nie jest krytyczne, a każdy szablon, który ktoś wgrywa, jest z zasady plikiem cyfrowym, a nie skanem. Obracanie tego w ogóle można pominąć.

**Anna Skupinska**: Robię obracanie dlatego, że podgląd załączników ma obracanie, więc myślałam, że to też trzeba zrobić.

**Lukasz Bott**: Nie, Aniu, nie róbmy tego. Tak jak pokazywałaś dzisiaj rano na Sprint Review, zrobiłaś podstawową funkcjonalność, której nie było i to jest to MVP. Da się podejrzeć DOCX-a czy PDF-a, bo to są najczęstsze formaty tych szablonów. DOCX dlatego, że musi być wygenerowany ze sprawy, a PDF to jeden z przypadków użycia.

**Piotr Buczkowski**: Nie ma sensu.

**Damian Kaminski**: Nie ma sensu.

**Lukasz Bott**: Ktoś gdzieś jakiś regulamin załączył. Zrobimy prosty podgląd ze stronicowaniem, koniec i tyle.

**Piotr Buczkowski**: Nie ma sensu podglądanie i obracanie, ponieważ nigdy nie zostanie to użyte. Obracanie ma sens przy skanowaniu, gdzie ktoś odwrotnie zeskanował dokument, a tutaj będą DOCX albo PDF, które nie mogą być odwrotnie.

**Damian Kaminski**: Dokładnie. Ale stanę trochę w obronie Ani, w sensie daliśmy takie wytyczne, ale jak dzisiaj zaczęła nam o tym mówić, to mam te same przemyślenia co Piotr. Daliśmy wytyczne, żeby to były takie same funkcje jak na każdym innym podglądzie, ale jak zaczęłaś mówić o problemach, to mam dokładnie to samo przemyślenie.

**Anna Skupinska**: Rozumiem.

**Damian Kaminski**: Jest to zbędne, nikt tego nie będzie potrzebował w praktyce.

**Piotr Buczkowski**: Nikt nie będzie tego potrzebował, nawet w teorii.

**Anna Skupinska**: Szkoda, bo już prawie skończyłam.

**Piotr Buczkowski**: Prośba, usuń to, żeby tego nie było.

**Janusz Bossak**: Aniu, do ciebie, jeżeli jest jakaś funkcjonalność, to warto się zastanowić, czy ona ma sens z punktu widzenia użytkownika. Nie patrzmy tylko na stronę techniczną, czy to się da zrobić, czy nie, tylko na sens tego. Na tym polega nasza praca zespołowa, żeby nawet jeżeli Damian dał takie wytyczne, to chwila refleksji albo pytanie, czy to ma sens.

**Damian Kaminski**: Podchodźcie do naszych wytycznych krytycznie. Nikt z nas nie jest alfą i omegą. Pamiętam, że rozmawialiśmy o tym z Januszem i poszliśmy po najmniejszej linii oporu, czyli kopiujemy funkcjonalność z załączników. Nikt z nas się pewnie nawet nie zastanowił, że nie ma to sensu, bo założyliśmy, że to będzie jakaś kopia, więc będzie to proste. Ale jeśli coś generuje dodatkowe problemy i wymaga więcej pracy, to warto mieć taką refleksję i dopytać.

**Anna Skupinska**: Przewidziałam to. Ta wycena była po tym, jak spojrzałam w kod, który generuje podgląd. On jest tak dostosowany do załączników, że wyciągnięcie go stamtąd będzie wymagało trochę pracy i refaktoryzacji, dlatego był dłuższy czas przewidziany.

**Damian Kaminski**: Dobra, możemy jeszcze o tym porozmawiać, ale tak jak powiedział Piotr, nie ma to sensu, bo każdy, kto generuje taki szablon, wgrywa go w dobrej formie, a jak wgra w złej, to poprawi i wgra jeszcze raz. Nie ma sensu, żeby każdy obracał te podglądy.

Przechodząc dalej. Filip – repozytorium plików. Dalej Łukasz Grodzki, integracja z UPS, SM, Global Expresem i Comarch Hubem. Łukasz, czy jesteśmy w stanie zamknąć te 3 elementy w tym sprincie?

**Lukasz Brocki**: Wszystkie trzy naraz w jednym sprincie nie ma opcji.

**Lukasz Bott**: Jesteśmy po spotkaniu w kontekście LOT-u. To jest UPS i Global Express. Tutaj od Łukasza czekamy na pytania.

**Lukasz Brocki**: Już przekazałem do Michała.

**Lukasz Bott**: Dobra, to są na kanale projektowym do LOT-u. Mamy czas. Wydaje mi się, że w pierwszej kolejności trzeba kończyć Comarch Hub. Robimy to dla Lewiatana, więc tam trzeba... Michał wysłał jakieś wytyczne od klienta odnośnie tego, co by chciał mapować. Adrian, Łukasz, jesteście w komunikacji z Michałem na mailu, więc spójrzcie na to. Myślę, że ten Comarch Hub to pierwsza kolejność. Global Express i UPS – tyle, ile się da. Pewnie tutaj będzie kwestia rozpoznania, połączenia, może pojedyncza funkcja wysyłająca.

**Damian Kaminski**: Warto by było, żebyście określili zakres biznesowy. Te integracje mogą mieć dużo opcji, pytanie, czy wszystkie są potrzebne.

**Lukasz Bott**: Łukasz opracował listę pytań i wątpliwości. Generalnie podejście mamy takie, i takie zostało zakomunikowane Michałowi, że jeżeli chodzi o integrację z UPS czy Global Express, robimy to w podobny sposób jak z DHL czy FedExem, czyli po stronie AMODIT-a będzie zestaw funkcji umożliwiających wysyłkę, odbiór, sprawdzenie statusu, anulowanie przesyłki – tak jak API będzie pozwalało.

**Damian Kaminski**: OK, czyli realizujecie wszystko, na co pozwala API, niezależnie od tego, czy klient tego potrzebuje?

**Lukasz Bott**: Nie.

**Lukasz Brocki**: Nie wszystko, bo to będzie bardzo dużo pracy. Robimy MVP, czyli tyle, ile jest wymagane dla klienta i co API pozwala. Ogólnie tak.

**Damian Kaminski**: OK, i macie to potwierdzone z klientem, gdzieś to macie spisane?

**Lukasz Bott**: Jeszcze czekamy na potwierdzenie.

**Damian Kaminski**: Dobra. Marka nie ma, natomiast zakładam, że Marek będzie kontynuował przenoszenie różnego rodzaju wywołań na poziom usługi w ramach Trust Center. Trzeba z nim ustalić status na Daily.

Mariusz, wspólnie z Kamilem i Markiem jako wsparciem. Może ty Kamil opowiesz, jaki tu jest zakres przewidziany.

**Kamil Dubaniowski**: Jeszcze nieznany, możliwe, że będzie bardzo mały, ponieważ im dalej w to idziemy, tym bardziej okazuje się, że właściwie możemy osiągnąć cel tym, co mamy. Prawdopodobnie będziemy szli w wizualizację struktury powiązań między sprawami na raporcie typu tabelarycznym i to była potencjalnie jedna z prac dla Marka, ale coraz bardziej wydaje mi się, że to nie jest w MVP potrzebne i niezbędne, żeby ten projekt wystartował. Drugi zakres to jest kwestia uprawnień i tutaj będę potrzebował konsultacji. W tym kontekście możliwe, że będą prace dla Mariusza. Chciałbym to z Piotrem i Januszem jeszcze omówić, bo Piotr Buła nieco zmienia spojrzenie na uprawnienia. Potencjalnie modyfikacja albo zupełnie nowy typ pola "odnośnik", żeby pokazać strukturę powiązań między sprawami, żeby pokazać drzewko, jak sprawy się między sobą wiążą, ale to też moim zdaniem nie jest MVP. Więc coraz więcej rzeczy, które planowaliśmy, schodzi na dalszy tor. Możliwe, że ten zakres będzie minimalny. Kluczowe dla mnie aktualnie są uprawnienia i to chciałbym w pierwszej kolejności omówić. Możliwe, że Marka na razie w ogóle nie będziemy angażować. Marek jest też krótszą część sprintu. Potencjalnie na ten moment jeszcze nie musimy tej decyzji podejmować, ale te uprawnienia chciałbym już potwierdzić, więc postaram się jeszcze dzisiaj z Januszem.

**Mariusz Piotrzkowski**: Kiedy Marek ma urlop?

**Kamil Dubaniowski**: Wraca w piątek.

**Mariusz Piotrzkowski**: Dobra, to przez te cztery dni ja będę się zajmował odpowiedziami na różne pytania w Trust Center. Będę musiał praktycznie wszystko przejąć. Już dzisiaj było drugie pytanie i trzeba też zrobić poprawkę, więc godzinę do trzech godzin dziennie mogę mieć mniej czasu.

**Kamil Dubaniowski**: Na ten moment, tak jak wspomniałem, myślę, że początek sprintu to będą raczej prace koncepcyjne nad tym projektem Piotra Buły, żebyśmy sobie nie narobili za dużo, bo coraz mniej mi się wydaje, że tam jest potrzebne, żeby osiągnąć cel, a też robić coś na siłę bez potrzeby. Przynajmniej dla tego klienta, bo rozwój jak najbardziej trzeba mieć na uwadze, ale ten klient akurat w kontekście tego projektu ma stały schemat od 97. roku, więc nie ma co się tutaj skupiać nad super panelem do zarządzania tym schematem, który się przez ponad 20-parę lat nie zmienił.

**Damian Kaminski**: OK. W kontekście Mateusza, chcielibyśmy skończyć wdrożenie tego komunikatora, więc pewnie będą jakieś poprawki. Czekamy jeszcze na wytyczne z WIM-u odnośnie konfiguracji. Trzeba będzie podpiąć odpowiednie certyfikaty. Mateusz, dobrze by było, żebyś przedyskutował kwestię połączenia tego wspólnie z Piotrem. Zaplanujcie na to godzinę czy pół i przedyskutujcie. Ten komunikator może być częścią AMODIT-a, przynajmniej bazodanowo, mimo że jest odrębną aplikacją. Warto ustalić, jak ma być tą częścią, i na przykładzie WIM-u tutaj to w odpowiedni sposób już na teście zrobić, żebyśmy mieli to przetestowane i opisane.

**Mateusz Kisiel**: Z Piotrem już rozmawialiśmy o tym kiedyś, jak to można zrobić. Tam są dwa serwery, komunikator zostanie na jednym serwerze i oba serwery będą się do niego łączyć.

**Damian Kaminski**: OK, tylko chodzi mi o bazę danych.

**Mateusz Kisiel**: Co do bazy danych, to nie ma to znaczenia. Może być baza danych odrębna albo ta sama co w AMODIT. To nie ma wpływu.

**Damian Kaminski**: Ma to znaczenie w kontekście wdrażania tego potem na chmurach.

**Mateusz Kisiel**: Na chmurze musi być w tej samej bazie, nie ma sensu robić nowej.

**Damian Kaminski**: Więc te wytyczne powinny być raczej jedne.

**Mateusz Kisiel**: Co do chmury, trzeba zrobić zmiany specjalnie pod chmurę, bo tam trzeba pobierać dane organizacji z osobnej bazy. Przydałoby się spotkanie odnośnie tego. Pytanie, czy chcemy teraz robić obsługę dla chmury?

**Damian Kaminski**: Nie wiem, czy chcemy, bo nie wiem, ile to będzie nas kosztowało. Warto by było to przemyśleć, przynajmniej na poziomie koncepcyjnym. Pytanie do Janusza i Łukasza w kontekście dokumentacji – czy mam to wpisać Mateuszowi jako zadanie na ten sprint?

**Janusz Bossak**: Nie na ten sprint, ale na pewno trzeba z Mateuszem porozmawiać i ustalić, co chcemy osiągnąć. Pisanie to ostatni krok. Wcześniej trzeba zaplanować strukturę tej dokumentacji. Dla wyjaśnienia, chodzi o to, żeby dać konsultantom narzędzie do tworzenia gotowej dokumentacji powdrożeniowej dotyczącej procesu. Chcielibyśmy w ustawieniach procesu mieć przycisk "Generuj dokumentację", który by powodował, że AI za pomocą dostępu do całej definicji procesu i posiadając właściwie skonstruowany prompt, generuje dokumentację w określonej strukturze: tytuł, wstęp, historia zmian, gotowy szablon. Drugie miejsce, gdzie taka dokumentacja mogłaby być tworzona, to są ustawienia systemowe, np. "Przygotuj dokumentację konfiguracji AMODIT-u" i on na podstawie wiedzy by ją generował. Bliżej nam jest do tej dokumentacji procesowej, bo tu już wiele rzeczy jest zrobionych, potrzeba tylko schematu i odpowiednio skonstruowanego promptu. Robiliśmy ćwiczenia i to się da zrobić już teraz z AMODIT i Copilotem, tylko trzeba napisać sensowny prompt.

**Mariusz Piotrzkowski**: Coś się stało, tylko u mnie tak brzmi?

**Damian Kaminski**: Telefon.

**Janusz Bossak**: Wyłączam telefon. Przepraszam.

**Mateusz Kisiel**: OK, możecie zaplanować takie spotkanie, żeby pokazać mi, co dokładnie ma się zwracać.

**Damian Kaminski**: Dobra, to przypisuję was trzech. Łukasz pewnie też ma w tym zakresie wiedzę.

**Mateusz Kisiel**: Czy z repozytorium plików będzie jakieś spotkanie, żeby omówić, co trzeba zrobić?

**Damian Kaminski**: Nie, z repozytorium plików Cię wywaliłem, to był błąd. Pierwsza koncepcja była taka, ale z racji, że Adrian jest bardziej dostępny, to on się tym zajmie.

**Mateusz Kisiel**: OK.

**Damian Kaminski**: Dobrze, i mamy na końcu Przemka, dla którego na razie nie mamy zadań rozwojowych. Uważamy, że warto by się pochylić nad błędami i niestabilnością w kontekście modułu raportowego. Przypisałem tu Basię, Janusza i Kamila jako osoby, które zagregują te problemy i Przemkowi przekażą.

**Janusz Bossak**: Dokładnie. Ja w tej chwili robię porządki na backlogu dotyczące modułu raportowego, żebyśmy mieli przegląd wszystkich błędów i pomysłów, żeby to spriorytetyzować i ustalić, co robimy najpierw. Będziemy ustalać takie paczki zadań, żeby mieściły się w ramach kolejnych sprintów i tak będziemy ten moduł poprawiać. Przemek, do Ciebie pytanie, pewnie trzeba zaplanować jakieś prace refaktoryzacyjne w tym module. Myślę, że warto by było, gdyby dotychczasowy zespół – Mateusz, Marek, Ania i Przemek – spotkał się i przemyślał, co warto refaktoryzować w tym nowym module raportowym, żeby działał lepiej i był bardziej stabilny.

**Lukasz Bott**: Damian, do tych raportów możesz mnie ewentualnie jeszcze dopisać, bo ja, robiąc raporty systemowe, też zgłaszałem różne rzeczy.

**Damian Kaminski**: Tak, jak najbardziej. Zakładam, że będzie to przedmiotem dyskusji na naszych spotkaniach "design".

**Przemysław Rogaś**: Co do tych błędów, to jak macie już coś rozpisane, to można mi przypisać. Od jutra zacząłbym to robić, bo innych zadań nie mam.

**Janusz Bossak**: Dobra, postaram się to dzisiaj ogarnąć.

**Damian Kaminski**: Ja chyba też coś mam na swojej tablicy z poprzedniego sprintu, to też najwyżej Ci podrzucę dzisiaj po południu.

Podsumowując, na pierwszy rzut oka nie jest to przeładowany sprint, ale dotyczy to zadań rozwojowych, natomiast mamy dość sporo bugów. W pierwszej kolejności dobrze by było, żebyście wycenili i oszacowali to, co jest na etapie "estimating" i przypisane do was. Chcemy w końcu zrealizować te bugi, bo mamy przemyślenie z czwartku i piątku, że nie zrealizowaliśmy wszystkiego, co było przypisane na poprzedni sprint, a wskakują nowe i nie nadążamy. Warto o tym pamiętać, zwłaszcza w kontekście takim jak u Mariusza, gdzie jeszcze chwilę potrwa, zanim ustalimy zakres. Żeby podejmować bugi, jeśli nie ma nic innego do zrobienia. To był tylko przykład Mariusza.

**Kamil Dubaniowski**: Potencjalnie mamy setkę zgłoszeń do przypięcia na bieżący sprint. Wiadomo, że duża część to będą testy, które zawsze będą za nami o jeden sprint, ale spodziewam się, że wpadnie też sporo bugów, których po prostu nie podjęliśmy w tym sprincie. Tak jak Damian mówi, nie możemy o nich zapominać, żeby nie przenosić ich ze sprintu na sprint. Trzeba je naprawić.

**Damian Kaminski**: Tak, tym bardziej, że mamy też głosy co do nowej wersji, że nie wszystko się tam wszystkim podoba. Abstrahując od tego, czy to wynika z przyzwyczajeń, czy nie, musimy po prostu wydać tę wersję przynajmniej stabilną, żeby nie było zarzutu, że jest dużo błędów, poza tym, że wygląda inaczej.

Piotra nie ma. Piotrze, z tego co pamiętam, ty masz kwestię tych serwisów mailowych do podpięcia. Nie wiem, czy to jest na twojej tapecie.

**Lukasz Bott**: Chodzi o ten ACS?

**Piotr Buczkowski**: W końcu muszę się tym zająć.

**Damian Kaminski**: No i potencjalnie w twoim kontekście może będzie jeszcze ten CAS. Zakładam, że wyjdzie w praniu.

**Piotr Buczkowski**: Jeżeli moja propozycja przejdzie, to nic nie trzeba będzie robić programistycznie.

**Damian Kaminski**: Dokładnie, więc wtedy pewnie jeszcze więcej można na Twojej tablicy znaleźć zaległości i będzie okazja, żeby to ponadrabiać. A poza tym, pewnie jakieś wsparcie koncepcyjne.

**Piotr Buczkowski**: CAS tak samo brzmi.

**Damian Kaminski**: Zbliżone. Czy kogoś pominęliśmy? Mam nadzieję, że nie.

Jak w ogóle podchodzicie do tego podejścia? Mieliśmy takie plany na poprzedni sprint, mieliśmy z tego jakieś rozliczenie dzisiaj na podstawie takiej tablicy priorytetów. Wypowiedzcie się, czy to jest lepsze od tego, co było wcześniej, czy gorsze?

**Adrian Kotowski**: To jest takie wysokopoziomowe, raczej nie widzimy tego na naszej tablicy. Z drugiej strony, to podejście nie pokazuje questów czy dodatkowych zadań, pojedynczych PBI, jakiś bugów. Ciekawe, jak to będzie wpływało na wynik całego sprintu, czy się uda, czy nie.

**Damian Kaminski**: Co masz na myśli mówiąc "questów"?

**Adrian Kotowski**: Chodzi mi o to, że gdzieś wpadnie jakiś hotfix, jakiś bug, który nie ma priorytetu "1", ale trzeba go zrobić. Robiliśmy takie podejście jak wcześniej, mieliśmy te sprawy w AMODIT, wpisywało się. To jest coś podobnego, tylko tutaj może być tak, że jedno zadanie jest realizowane przez parę osób.

**Damian Kaminski**: Tak, bo tutaj mamy to rozpisane bardziej po projektach niż po zadaniach.

**Adrian Kotowski**: Możemy spróbować, zobaczymy, czy to się sprawdzi. Według mnie to bardziej kwestia motywacji. Mieliśmy takie samo podejście na Azure DevOps, później zadania były robione, jak mówiłem, na AMODIT, a teraz Teams. W sumie trzeci raz robimy to samo, tylko inne narzędzie.

**Damian Kaminski**: Dlaczego trzeci raz to samo?

**Adrian Kotowski**: Mieliśmy podejście z zadaniami wysokopoziomowymi, tylko narzędzie jest inne.

**Damian Kaminski**: To narzędzie nie jest dedykowane do tego, żebyście musieli tu coś robić, raczej żeby zobaczyć wysokopoziomowo, kto się czym zajmuje i jakie są główne cele sprintu, abstrahując od tego, że są bugi i hotfixy, którymi staramy się opiekować na co dzień. Jeśli coś wpada, codziennie rano mamy przegląd. Dzisiaj się zdarzyło, że nie mamy, więc jeśli coś wpadło w piątek na koniec dnia, to może jeszcze jest niezaopiekowane. Jutro to zaopiekujemy i do kogoś przypiszemy, jeśli uznamy, że jest krytyczne.

**Adrian Kotowski**: Czy jest jakieś powiązanie tych tasków z Teams z tymi zgłoszeniami w Azure?

**Damian Kaminski**: Nie, to nie ma tego celu. Tu mamy to bardzo wysokopoziomowo.

**Mariusz Piotrzkowski**: Ja to rozumiem w taki sposób, że na Azure mamy zadania konkretne, wydzielone dla programistów z opisem, co trzeba zrobić, a w Teams mamy w kategorii przedziału czasowego jako jeden sprint, jakie są ogólne założenia. Nie widzę konfliktu jednego z drugim.

**Damian Kaminski**: Tak, taki był cel.

**Mateusz Kisiel**: Mi się podoba, że jest krótsze, bardziej konkretne. Można sobie łatwo zobaczyć, co jest do zrobienia przez jakie osoby.

**Mariusz Piotrzkowski**: Mnie też się takie ogólne założenie podoba.

**Kamil Dubaniowski**: Będą się przewijały te wrzutki, o których mówi Adrian, ale wiadomo, ważnych hotfixów nie pomijamy. Dla nas to jest ułatwienie, że wy macie cel. Wiecie, że z tego w poniedziałek będziemy was pytać. Nikt was nie zapyta, czy zrobiliście hotfixa, to musicie po prostu zrobić. Celem jest pokazanie progresu, więc rozliczamy was z tego. To ma was trochę trzymać w ryzach, że jak zrobicie coś poza i konsultant wam podziękuje, to w poniedziałek nikt wam nie powie, że super, ale nie zrobiliście celu sprintu przez to. To jest głównie po to.

**Kamil Dubaniowski**: Musimy się bronić przed tymi wrzutkami. Wy musicie się bronić trochę nami. Czyli jak konsultanci próbują wam coś wcisnąć poza sprintem, a wy wiecie, że to mnóstwo roboty, to nie podejmujecie decyzji samodzielnie. My się zobowiązujemy, że dostarczymy to. A co zrobicie przy okazji, to nikogo specjalnie nie będzie interesowało, no chyba, że jest na tyle istotne, że wspólnie podejmujemy decyzję i w trakcie sprintu zmieniamy cele. Ale jakiekolwiek wrzutki od konsultantów bez naszej wiedzy nie są wytłumaczeniem, że nie zrobiliście celu sprintu.

**Damian Kaminski**: W kontekście tego, co zapytał Adrian, może pokażę, jak chcielibyśmy, żeby to wyglądało docelowo. Takie repozytorium plików, które mamy zrobić, powinno się tu nazywać MVP 1. Odpowiadając na twoje pytanie, Adrian, jaka jest korelacja z tym, co jest osadzone w Azure – trochę nam brakuje jeszcze na to czasu, ale myślę, że to będą kolejne iteracje, które do tego doprowadzą. Jak wejdziemy na backlog, nastąpił nowy podział, nie wiem, czy wszyscy to widzieli. Janusz ustalił coś takiego jak "Inicjatywy" i w ramach tych inicjatyw mamy epiki, i takim epikiem jest właśnie "Repozytorium MVP 1". W ramach tego – to jest jeszcze spisywane, ale nie określone co to jest MVP 1 – powstanie jeszcze MVP 2 i część rzeczy, która tu jest, zostanie przeniesiona. To będzie celem sprintu. Docelowo, gdybyśmy to już mieli, to byśmy to robili. Mamy to skończyć w tym sprincie. Jutro najpóźniej w połowie dnia będziemy wiedzieli, co jest MVP 1 i na podstawie tego będziemy w stanie określić, że ten punkt zakończymy. Taka jest korelacja między tym punktem a naszym backlogiem na poziomie najwyższym, MVP 1. Oznacza to, że zrealizujemy wszystkie punkty, które są do tego podpięte, a przez to osiągniemy określone cele biznesowe. Na poziomie ficzera mamy opisane, co to jest i jak to można realizować. Tak bym to widział, że będziemy pracować docelowo.

**Adrian Kotowski**: Czy do tych tablic w Teams będą miały dostęp osoby spoza naszego działu?

**Janusz Bossak**: Nie.

**Damian Kaminski**: To istotne pytanie. Nie rozumiem, co ci to da.

**Adrian Kotowski**: Żeby mieć taką podporę, że jak ktoś mi powie "zrób coś dla jakiegoś klienta", to ja mu powiem "sorry, tego nie ma na mojej liście do zrobienia".

**Janusz Bossak**: Dobrze, że o tym mówisz, Adrian. To podstawowa zasada waszej pracy. Jeżeli mamy sprint, to nie ma czegoś takiego jak "wrzutki, bo zrób mi to czy tamto". Nie ma tak i musimy być bardziej asertywni. Oprócz sytuacji, kiedy jest to hotfix i u klienta coś padło, nie działa. Wtedy reagujemy natychmiast i naprawiamy. Każdy inny przypadek nie jest robiony w tym sprincie. Wpisujemy na listę, Damian, Kamil czy Łukasz decydują, na ile jest to ważne i czy będzie robione w następnym sprincie, czy może kiedyś. To przechodzi przez ocenę. Nie ma czegoś takiego. To do Ciebie, Adrian, i do Piotra. Wiem, że jesteście bardzo często angażowani jako deweloperzy. Co innego jest pomóc rozwiązać czy zrozumieć problem, a co innego przystąpić do prac deweloperskich, żeby coś naprawiać. Jak powiedziałem, oprócz sytuacji hotfixowych, gdzie u klienta kompletnie padło i wymaga to natychmiastowej reakcji, wszystkie inne rzeczy muszą być planowane. Naprawa błędów jest planowana na następny sprint.

**Damian Kaminski**: Cały czas dążymy do tego, co mówi Janusz, ale to jest proces. Zanim dojdziemy do stanu idealnego, gdzie będziemy się faktycznie rozliczać z effortu i być bardziej przewidywalni... Adrian, twoja rola w takiej prośbie jest prosta: możesz to podjąć, ale to musi być przypisane do ciebie w Azure. My jesteśmy stałym elementem procesu przekazania sprawy do ciebie, zgłoszenia w Azure. Ktoś może je założyć, ale musi przejść przez nas. Nie da się przypisać zadania bezpośrednio do ciebie. Jeśli przejdzie przez nas i trafi do ciebie, to będziesz się tym zajmował, nawet jutro, bo okaże się, że to hotfix. Ale jeśli nie, to nie.

**Kamil Dubaniowski**: Jedyna ścieżka aktualnie, jaka jest możliwa, to że sami sobie dodacie zgłoszenie na bieżący sprint. Nie blokujemy wam tego. Natomiast konsultant nie może wam już przypisać sprintu. My codziennie rano na Daily poświęcamy te 20 minut i bierzemy zgłoszenia z poprzedniego dnia, decydując, czy są tak ważne, że robimy je teraz, czy planujemy na kolejny sprint. Robimy tak od 2-3 tygodni. Więc jedyną ścieżką, żebyście pozwolili sobie na takie zgłoszenie, jesteście wy sami. Wszystko inne przechodzi przez nas.

**Janusz Bossak**: Są pewne wyjątki, takie serwisowe, jak Trust Center, serwis OCR. Tutaj Mateusz reaguje. Przy tego typu rzeczach, gdzie pełnimy rolę serwisu – tak. Natomiast wszelkie tematy rozwojowe, zmiany, eliminowanie błędów – to musi przejść normalnie przez proces planowania i dopiero wchodzi na odpowiedni sprint. Nie ma czegoś takiego, żeby konsultant wrzucał coś z zewnątrz.

**Damian Kaminski**: Zakładam, że mogą być jeszcze nasze wrzutki, jeśli my mamy coś przypisane na "investigation", czyli ktoś coś zgłasza, ale bez dodatkowych logów czy jakichś parametrów nie jesteśmy w stanie tego sprawdzić. W takim zgłoszeniu możemy was poprosić o jakąś wersję "kartonową", jakąś bibliotekę z parametrami, żeby coś wyświetlić. Ale to będzie raczej prośba od nas, żeby pomóc i bezpośrednio z konsultantem przeanalizować tę kwestię.

**Janusz Bossak**: Dobrze, jeśli wszystko wiadome, to działajmy.

**Kamil Dubaniowski**: Ja bym miał jedną prośbę, żeby Mateusz rzucił okiem na status "Ready to sprint", bo go nie było w piątek, kiedy to ogłaszaliśmy. Czy coś tam przypadkiem nie jest już "in progress". Resztę "ready to do" będziemy rozważać, czy faktycznie jest sens robić w kolejnym sprincie, a u ciebie jest tego sporo niepodjętych. Jak wiesz, że czegoś w ogóle nie planujesz robić, to od razu zrzucaj to na backlog ze sprintu. A co już zacząłeś i chcesz kontynuować, to oznacz jako "in progress" i przypnij na 47. sprint, żeby na 45. nic nie zostało. Zostałeś w sumie tylko ty. Ania ma dwa zgłoszenia, ale to raczej do naszej decyzji, i Damian u ciebie też coś jest.

**Mateusz Kisiel**: Dobra, czyli przypinamy na kolejny sprint czy na backlog?

**Kamil Dubaniowski**: Jeśli chcesz robić w kolejnym sprincie albo już zacząłeś, to przypinasz na kolejny. Jak wiesz, że nie będziesz tego w najbliższym czasie podejmował, a tylko rozpisałeś zadanie, żeby ci nie uciekło, to na backlog.

**Kamil Dubaniowski**: Najpierw Mateusz niech wyczyści tę listę, bo bez sensu, żebyśmy teraz siedzieli i analizowali, o co chodzi w zgłoszeniu.

**Mateusz Kisiel**: Pewnie pierwszeństwo miałyby te zgłoszenia, które teraz weszły, czyli dokumentacja procesu.

**Kamil Dubaniowski**: Tak, mam na myśli głównie te dotyczące bazy wiedzy, jakieś pomysły, dodanie opcji automatycznego tworzenia artykułów na podstawie linku do strony. One mają duży effort, właściwie na cały sprint. Jak ja ci to teraz przypnę, to wyjdzie, że masz zajęty cały sprint.

**Mateusz Kisiel**: Dobra, to ja to po prostu przypiszę.

**Kamil Dubaniowski**: Spodziewam się, że nie wszystkie chcesz z nich robić od razu.

**Mateusz Kisiel**: Tak, tak.

**Kamil Dubaniowski**: Zostają do dyskusji dwa tematy Ani odnośnie podglądów i u Damiana też coś zostało na zeszłym sprincie. Reszta już jest wyczyszczona. Ja poprzypinałem to, co zostało, albo powywalałem, gdzie były poblokowane zadania.

**Damian Kaminski**: Swoje przejrzę.

**Kamil Dubaniowski**: Rzućcie okiem na wyceny, bo dzisiaj jeszcze dwie jakieś przypisywałem, o które mnie konsultanci upomnieli. Zobaczcie też na strefę "estimate", czy nie macie żadnych zleconych wycen do zrobienia. Jedno trafiło do Adriana z tego, co kojarzę. Chyba tyle.

**Janusz Bossak**: Dobra, dzięki bardzo.

**Kamil Dubaniowski**: My zostajemy, żeby przypiąć te, które są na "ready"?

**Kamil Dubaniowski**: Tak, zdecydujmy zakres tego tematu dotyczącego podglądu szablonów, bo tam są dwa zgłoszenia niepodjęte. Czy chcemy to robić, czy nie? Mateusz, jak skończysz, to daj nam sygnał, żebyśmy też przejrzeli te twoje, co zostają.

**Mateusz Kisiel**: Dobra.

**Kamil Dubaniowski**: Reszcie dziękujemy.

**Mariusz Piotrzkowski**: No to cześć.

**Janusz Bossak**: Dzięki.

**Anna Skupinska**: Cześć.

**Filip Liwiński**: Cześć.

**Barbara Michalek**: Cześć.

**Mateusz Kisiel**: Cześć.

**Adrian Kotowski**: Cześć.

**Kamil Dubaniowski**: Udostępnię. Zacznijmy od tych tematów Ani. Nie podejmowałem ich, bo tak jak Michał pisał, pójdzie automat.

**Michal Zwierzchowski**: Ja to ogarnę.

**Kamil Dubaniowski**: Zostają te dwa duże tematy u Ani, oba oszacowane na effort 13: "implementacja logiki" i "mechanizm zapisywania podglądów na dysku" w wątku szablonów dokumentów. Nie jest "ready to do", rozumiem, że jeszcze niepodjęte, bo Ania mówiła, że statusy są aktualne. To rozpisywał Damian. Pytanie, czy chcemy to mieć w tym MVP, czy odkładamy na kiedyś?

**Damian Kaminski**: Jaką mamy alternatywę, jeśli nie chcemy?

**Lukasz Bott**: Mówimy o podglądzie szablonów w procesach.

**Kamil Dubaniowski**: Tak.

**Damian Kaminski**: To były wytyczne od Piotra, ja tylko dopisałem kryteria akceptacji. Opis robił Piotr.

**Janusz Bossak**: Tam były dwa pomysły. Jeden, żeby generować na bieżąco i nie zapisywać, a drugi, który chyba ostatecznie wygrał, żeby jednak zapisywać, tylko w zmienionej, dedykowanej strukturze.

**Kamil Dubaniowski**: OK, dla mnie tylko decyzja, czy idziemy w to dalej. Były głosy, żeby w ogóle tego nie robić, bo są obejścia.

**Lukasz Bott**: Nie, to dotyczyło tych dziwacznych funkcjonalności dodatkowych, jak obracanie, skalowanie.

**Damian Kaminski**: Tak, o to chodziło.

**Kamil Dubaniowski**: Ogólnie w zeszłym tygodniu pojawił się głos, żeby w ogóle tego nie robić, bo zaszła pomyłka i jest na to mnóstwo innych sposobów, żeby to zaopiekować. Czy jest konieczne, żebyśmy to teraz robili?

**Damian Kaminski**: Nie, nie, zróbmy to raz i będzie z głowy.

**Janusz Bossak**: Dokładnie, dostarczmy MVP.

**Damian Kaminski**: Dokładnie, MVP. Temat jest już zbadany, trzeba będzie do tego wracać. Tutaj popłynęliśmy z Januszem za grubo, nie przemyśleliśmy wszystkiego.

**Lukasz Bott**: Wszyscyśmy popłynęli. Wydawało się, że jeżeli mamy funkcjonalność podglądu, to szablony do procesu też są jakimiś dokumentami i że to będzie proste przełożenie komponentu. Być może popełniliśmy błąd koncepcyjny wcześniej, że nie mamy takiego komponentu "podgląd dokumentu", który można by użyć wszędzie.

**Damian Kaminski**: Słuchajcie, podsumowując, to można ściąć totalnie i powiedzieć, że nie ma tu żadnych opcji, jest tylko "X" i "Odśwież wygenerowanie podglądu".

**Kamil Dubaniowski**: Czyli dolną belkę w ogóle wywalamy?

**Damian Kaminski**: No. Według mnie jak chcemy zrobić MVP... można by się pokłócić, że przełączanie na kolejny szablon byłoby wygodne, ale jeśli to ma wygenerować nie wiadomo jak skomplikowane rzeczy, to zróbmy MVP, wydajmy i zobaczymy, jak to się przyjmie. Może klient wróci i powie: "Fajnie, że to macie, zróbcie nam przechodzenie, żeby było wygodniej". Może nam nawet za to zapłaci.

**Lukasz Bott**: A może powie, że to, co zrobiliśmy, wystarczy.

**Kamil Dubaniowski**: OK, przycisk odświeżania rozumiem, że zostaje?

**Damian Kaminski**: Według mnie powinien pozostać, bo jeśli coś się schrzani, to użytkownik sobie sam z tym poradzi.

**Kamil Dubaniowski**: Czyli nie robimy tej dolnej belki po prostu.

**Lukasz Bott**: W dolnej belce masz stronicowanie.

**Damian Kaminski**: Ale co tam można przechodzić? Będziesz przewijał na pięćdziesiątą stronę?

**Kamil Dubaniowski**: Tam się nie da, jest tylko licznik stron.

**Lukasz Bott**: Aha, OK. Zgadzam się, przechodzenie na kolejną stronę...

**Kamil Dubaniowski**: Na kolejny szablon.

**Lukasz Bott**: Jeżeli to ma służyć tylko do szybkiego zidentyfikowania, czy to jest ten szablon, który chcę użyć, to zazwyczaj po pierwszej czy drugiej stronie jesteś w stanie to ocenić.

**Damian Kaminski**: Ja bym jeszcze poszedł dalej. To, że kliknięcie w szablon powoduje jego pobranie, nie wiem, czy to jest dobre. Trzeba by pogadać z klientami, którzy z tego korzystają, jakie to ma konsekwencje w kontekście użyteczności. Eksportujemy plik na zewnątrz, na swój komputer. Jeśli ten plik ma być dalej procedowany w tej sprawie, może kliknięcie w szablon powinno generować podgląd, a z trzech kropek jest opcja "wygeneruj szablon". Może to jest potrzebne. Ale to już kolejne elementy. Na razie zrobiłbym to na minimum.

**Kamil Dubaniowski**: To zależy od procesu. Bazuję na tym, co robiłem dla Fereo, agencji pracy tymczasowej. Oni używali swobodnego szablonu, generowali sobie umowę, drukowali i dawali do podpisu. Przychodził kandydat, uzupełniali dane, generowali umowę. Tych szablonów było 15-20, bo zatrudniali dla różnych klientów na różnych szablonach.

**Damian Kaminski**: Jasne. Ale można by pójść dalej i zmienić ten proces na podpis kwalifikowany, wtedy nie ma potrzeby drukowania i może to pobieranie nie jest zasadne.

**Kamil Dubaniowski**: Weź pod uwagę, że to w dużej części osoby z zagranicy. Wolą przyjść do biura, gdzie mają tłumacza na miejscu.

**Damian Kaminski**: Dobra, to znaczy, że trzeba Anię zwrócić uwagę, skoro wyrzuciłeś to, co było na dole, żeby na nowo to oszacowała, jeśli robimy MVP.

**Kamil Dubaniowski**: Siódemka, przypinamy. Pewnie roboty dużo nie ma. Dużo roboty wyszło z tego, że Ania chciała zrobić to dobrze i reużyć komponentu, a wyłuskanie części wspólnej, jak opowiadała, to...

**Lukasz Bott**: Dzieła.

**Kamil Dubaniowski**: Podejście jak najbardziej OK, ale daliśmy za duży zakres, to nie jest aż tak kluczowe. Dobra, ja się do niej odezwę.

Mamy jeszcze twoje, Damian, "investigating" i "evaluating". Jedno czeka na twój komentarz.

**Damian Kaminski**: Moje "evaluating"? OK, zaraz dopiszę. Chodzi o dodanie ustawień MFA dla użytkowników zewnętrznych. Nie ma sekcji "Bezpieczeństwo" dla nich, więc nie mogą nawet zresetować MFA. Trzeba to obsłużyć, bo wdrażają to chociażby w MCIT. Jest już napisane, że trzeba tylko przekopiować kod.

**Kamil Dubaniowski**: Effort mnie trochę zastanawiał, Piotr szacował chyba na trzy dniówki.

**Damian Kaminski**: Nie, 3,5. Ja to oszacowałem, ale pewnie rozmawiałem o tym z Piotrem.

**Kamil Dubaniowski**: Kojarzy mi się, że było dużo więcej, dlatego dawaliśmy alternatywy, żeby włączyli to wszystkim.

**Damian Kaminski**: Pomyliłem się. Chodzi tylko o to, żeby sekcja "Bezpieczeństwo" wyświetlała się dla użytkowników zewnętrznych, jak już MFA jest włączone dla wszystkich.

**Kamil Dubaniowski**: Zgodzili się, że włączają wszystkim?

**Damian Kaminski**: Już włączyli. Poprawię opis, chodzi tylko o ten jeden element.

**Kamil Dubaniowski**: Trzeba przejść po każdym z osobna.

**Damian Kaminski**: Muszę się przepiąć na spotkanie, jakaś afera wyszła. Wrócę, jak się szybko skończy.

**Janusz Bossak**: Dobra.

**Kamil Dubaniowski**: OK. Łukasz, rozumiem, że tych tematów integracyjnych nie ma jeszcze rozpisanych na zadania?

**Lukasz Bott**: Nie, nie ma.

**Kamil Dubaniowski**: Marek jest tylko do piątku, więc potencjalnie, jak jutro dogadamy szczegóły dotyczące Piotra Buły, to do niego dojdzie. Mariusz ma tego sporo.

**Lukasz Bott**: Mamy wiele rzeczy na "estimating". Oszacowanie nie oznacza od razu, że to robi.

**Kamil Dubaniowski**: Dobra, pogadam z nim. Trzeba rozpisać te zadania dotyczące integracji, podjąć decyzję, czy robimy UPS czy Global Express, żeby Łukasz nie miał nierealnie wpisanych celów.

**Kamil Dubaniowski**: Janusz, na jutro chyba wrzucę spotkanie o tych uprawnieniach, chyba, że masz jeszcze dzisiaj czas.

**Janusz Bossak**: Chciałbym się teraz skoncentrować na module raportowym, siedzę w porządkowaniu.

**Kamil Dubaniowski**: Dobra, to na jutro.

**Lukasz Bott**: Mam pytanie odnośnie wydań. Mamy wersję wrześniową, którą stabilizujemy. Pojawiła się też marcowa przyszłoroczna.

**Kamil Dubaniowski**: Powinniśmy już grudniową wydać. Już powinna wyjść z dopiskiem "beta" oficjalnie.

**Lukasz Bott**: Chciałem zapytać, czy ta grudniowa ma sens.

**Kamil Dubaniowski**: Ma, bo dochodzi lista pól, matryca uprawnień. Nowości są. Ja bym ją wydał. Powinno to już wyjść. Będziemy jeszcze pakować UPS i wszystko pod LOT.

**Michal Zwierzchowski**: Zrezygnowaliśmy z wrześniowej, żeby wydać grudniową.

**Kamil Dubaniowski**: Zgadza się. To już powinno być wydane, umawialiśmy się do połowy listopada.

**Michal Zwierzchowski**: Miałem pytać, czy na wiki wrzucać i czy zaczynamy testować.

**Kamil Dubaniowski**: Ja bym szedł w to. Jest lista pól, jest matryca uprawnień. Powinna już wyjść i powinniśmy zacząć ją stabilizować. Możemy już usunąć komunikat i opcję przełączania się na stare ustawienia systemowe, testować u nas, czy wszystko zaopiekowaliśmy.

**Lukasz Bott**: Te integracje z UPS czy Global Express, jeśli koledzy to dobrze robią jako rozszerzenia, czyli osobne DLL-ki, to wpięcie tego, czy pojawi się w grudniowej czy marcowej, to będzie tylko kwestia podpięcia.

**Kamil Dubaniowski**: No tak, to jutro Buła może trochę namieszać, bo to zaingeruje, ale zobaczymy w jakim zakresie.

**Lukasz Bott**: Tak, jeśli chodzi o te uprawnienia, to trochę wymusza zmiany w bebechach AMODIT-a.

**Kamil Dubaniowski**: Chodzi bardziej o sposób na optymalne dziedziczenie uprawnień. Jeśli ustawiliśmy uprawnienia na katalogu, to żeby teraz łatwo wszystko, co jest podpięte, dziedziczyło je.

**Lukasz Bott**: Tak, tylko żeby teraz, jak coś takiego zrobisz, we wszystkich innych wdrożeniach, gdzie wykorzystujesz sprawy powiązane, nie okazało się, że gdzieś komuś chodzą jakieś uprawnienia.

**Kamil Dubaniowski**: No tak, to jest dobre. Dobra, to na jutro. Kończymy, co?

**Janusz Bossak**: Dobra, dzięki.

**Kamil Dubaniowski**: Dzięki.

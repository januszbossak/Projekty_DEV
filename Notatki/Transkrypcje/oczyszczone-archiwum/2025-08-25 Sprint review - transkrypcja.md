**Sprint Review 2025-08-25 - Transkrypcja**

**Data:** 2025-08-25
**Uczestnicy:** Janusz Bossak, Adrian Kotowski, Barbara Michałek, Damian Kamiński, Piotr Buczkowski, Anna Skupińska, Przemysław Sołdacki, Mateusz Kisiel, Łukasz Bott, Kamil Dubaniowski, Filip Liwiński, Mariusz Piotrzkowski, Przemysław Rogaś

---

**Janusz Bossak:** Czy jak tam po weekendzie wszyscy zdrowi? No tak.

**Adrian Kotowski:** Chyba przegrałem.

**Barbara Michałek:** Zimno jest, to jeszcze koniec wakacji, już po prostu 13°.

**Janusz Bossak:** No zimno, u nas też się urodził.

**Damian Kamiński:** U mnie słoneczko świeci.

**Piotr Buczkowski:** Zobacz, zobaczcie prognozy na czwartek.

**Barbara Michałek:** No właśnie piątek, ja jeszcze liczę na piątek. Może jakiś wcześniej się ten, ma 30 minut stopni, jeszcze może do nad rzeczkę można skoczyć po południu.

**Anna Skupińska:** Wreszcie jest chłodno.

**Damian Kamiński:** Musisz przestać palić w piecu.

**Janusz Bossak:** Ja już tak właśnie zastanawiałem, czy nie włączyć pieca.

**Barbara Michałek:** Ja już wczoraj odpaliłam klimę na grzanie.

**Janusz Bossak:** No dobrze, słuchajcie, jesteśmy już wszyscy, przynajmniej widzę po ilości kwadracików. Kamila coś nie widzę. No dobrze. No dobra, słuchajcie, to podsumujmy sobie ten sprint. Co tam się nam udało dokończyć? Kamil się pojawił, ale coś się nie pojawia. Czy Kamil coś pisał, że go nie będzie? No dobrze, słuchajcie, kto tam odważny pierwszy zaczyna?

**Adrian Kotowski:** Ja mogę wystartować z podpisywaniem na macOS, bo już jestem przygotowany.

**Janusz Bossak:** Dobra, to pokazuj.

**Adrian Kotowski:** Dobra, go tylko [niezrozumiałe]. Robiło to akurat na [niezrozumiałe]. Będzie to bardziej niezręczny czerwiec. Jakoś to z doświadczonym przewodnikiem Marka, więc ja postaram się to w miarę sprawnie na moje możliwości wyprowadzić, więc tak tutaj mamy przykład już przygotowanej sprawy z dokumentem. Teraz wyślę do Trust Center. Ona została wysłana i tak zaraz dostanę maila o tym, że mam wiadomość. Wypisanie [niezrozumiałe] obiekcie jest. Mieliśmy teraz. Przekierował nas. Teraz piszę tutaj numer kodu. Goście adresie numer kodu. Mam nadzieję, że widać, ale nic nie mówił, więc chyba jest w porządku.

**Janusz Bossak:** Widać wszystko.

**Adrian Kotowski:** Dobra, OK. Tak. Zrobiliśmy dokument z wpisanym Pages, tak, krótką aplikację. [Niezrozumiałe] aplikacja, jak widać żyć [niezrozumiałe] aplikacja. Tutaj powinien [niezrozumiałe] jak tak, to ja mam taki problem, bo mamy w ofercie [niezrozumiałe], więc mogę albo mówić, albo wypisywać. Nie mogę być 2 jednocześnie, więc to tam pojęcie, co ta aplikacja robi, później przełożyło się na [niezrozumiałe] i po prostu pokazać, jak to faktycznie działa. Więc tak, no aplikacja generalnie, czy inaczej, to nie jest jakby wzorowa aplikacja. Tak na początek chciałbym znać, że jest to bardziej taki prototyp, który po prostu wykazuje, że da się podpisać. Dokument na macOS. To jest moc tych naszych bibliotek, ze może właśnie do .NETa, ale jeżeli publikacje można przyzwyczaić klienta, że klienta dostarczyć i nie musi trenować nic poza tą aplikacją. Nawigacja zostały napisane właśnie na MAUI, które [niezrozumiałe] z wykorzystaniem nowej biblioteki MAUI i tworzenie aplikacji desktopowych. No na razie mam tylko odrębnych kont. Wejście on jest tylko na macOS. Starałem się tam [niezrozumiałe] użycie kodu, który mamy już tam w ramach tego istniejącego snap'a na Windowsa, no ale ten musiałam jednak społeczny projekt na razie i no to będę pokazywał jak podpisywanie, podpisał kwalifikowanym Szafirem (Szafir), czyli podpis fizyczny z czytnikiem. Tak, no to wiem, aplikacja jest 3-krokowa. Wybieram już takie [biblioteki] od dostawcy tego produktu, czyli w tym przypadku [dostawca czytnika], mając w bibliotekę ładuję certyfikaty, pobieram certyfikaty, czyli certyfikatów, gdy mam podłączony do [komputera]. Czyli na nośniku fizycznym [niezrozumiałe] ubieramy certyfikat. Już miałem będzie weryfikacji. Podpisuje. Oczywiście nie muszę pisać prywatnego PIN, tak to wygląda w skrócie, a teraz pozwólcie, że po prostu wyłączę audio i przełączyć się na właśnie na wypisywanie.

**Janusz Bossak:** To tak jak tutaj Adrian mówił, to na razie jest wersja taka, wiecie, robocza, techniczna, żeby udowodnić, że się da.

**Piotr Buczkowski:** Bo nie widzę możliwości, żeby jakikolwiek użytkownik wybierał bibliotekę.

**Janusz Bossak:** Tak, tak nie, no to spoko, znaczy chodzi o to, że na macOS jest to trochę inaczej zorganizowane i każda biblioteka siedzi w innym miejscu, znaczy siedzi w miejscu instalacji tej aplikacji, która obsługuje dany certyfikat i to po prostu będzie zrobione tak, że będzie wykrywał. Jaki jest podpis, czy jaki użytkownik ma podpis i tej biblioteki będzie brał z tego folderu? No na macOS jeszcze troszeczkę inaczej zorganizowane, tak.

**Damian Kamiński:** Ale biblioteka jest per dostawca, czyli na przykład, gdyby ktoś miał 2 podpisy, to taki przypadek?

**Janusz Bossak:** No to będzie miał 2 takie biblioteki i 2 będzie musiał. No właśnie to są rzeczy, które trzeba jeszcze obsłużyć. Tak to jest. No i tutaj się już uruchomiło podpisywanie, ciach ciach międzyczasie to co pokazywał Adrian.

**Przemysław Sołdacki:** Panie, że się udało, ale też właśnie mam uwagę, że to musi działać tak bardziej tak jak [użytkownik oczekuje].

**Janusz Bossak:** Słuchajcie, to jest w połowie drogi, jesteśmy tak, znaczy pokonaliśmy największą przeszkodę, mianowicie taką, że za pomocą naszych narzędzi takich .NETowych i plus biblioteki, które już posiadamy, jesteśmy w stanie jednak dobrać się do certyfikatu na macOS. To był problem, który Rafał wtedy nie mógł przejść. W tej chwili udało się to zrobić. I no to jest dowód na to, że da się na macOS podpisywać, tak, za pomocą tej naszej aplikacji. No bo jesteśmy w tej aplikacji tak naprawdę.

**Adrian Kotowski:** Tak, dodać, że właśnie tutaj jednak, jak już mówiłem, koncepcja podpisywania strategicznie na macOS jest zupełnie inna. Na Windowsie mamy ten magazyn i to jest dość proste, bo tam jest biblioteka do .NETowych i trzeba jakby dużo tutaj robić. Natomiast na macOSie trochę tak, że one są te sterowniki jest standard PKCS, to są stare biblioteki. Chociaż w zestawie może tam być potężnymi [niezrozumiałe], co chce na przykład Szafir, tam, żeby po prostu najprostszym dobrym, czyli po prostu wydawanie tej bryki z czytnika. Szafir, żeby tam jakieś wysyłanie ich aplikacji i wyłącznie jest w chmurze. Z kolei jeszcze robi też czegoś inaczej, będzie z naszej perspektywy to jest po prostu jedno, ale jednak pewno mieliśmy mieć takie biblioteki naszej aplikacji załadowanej, więc jakby też było parę koncepcji, to możemy zrobić, żeby właśnie użytkownik nie musiał tych bibliotek wybierać. Czy też chciałbym powiedzieć o aplikacji, bo teraz pokazałem tylko opisywanie w ramach [e-podpis]. Według tu właśnie [niezrozumiałe] do [niezrozumiałe] jeszcze też równolegle tej dostawaliśmy nurtem i Kamilem, inne jeszcze podpisy, więc zdobyliśmy też `e-podpis` oraz `SimplySign`. W [niezrozumiałe] przepis, że udało się terminologii wypisać dokumenty, a tam chodzi o spisanie [niezrozumiałe] jeszcze Janusz. Tam właśnie ktoś próbował, ale tam jeszcze jesteśmy na dużym [niezrozumiałe]. Wyszukaj tym problemu, o co tam chodzi w tym pisanie, ale to jest kwestia dla mnie jednego dnia, żeby to ustalić. Tomasz, powiedzmy, mówiąc, dlaczego to mówię? Bo właśnie ciekawe [niezrozumiałe], bo udało nam się już podpisać dokument na maszynie, która nie ma w ogóle środowiska uruchomieniowego .NET, gdzie jakby można powiedzieć, akcja u takiego prostego Kowalskiego jest też możliwa i też pokazuje właśnie, że możemy budować takie paczki self-contained, czyli są self-contained, które jakby zawierają wszystko. Jakby w sobie, więc to jest bardzo wygodne, jeśli też się tak myślałem celowo możliwości i właśnie. Przygotowanie tej aplikacji, bo ten przykład administrator czy można to było ubierać nie tylko właśnie z poziomu naszej? Właśnie strony z Trust Center też na przykład. Właśnie też [niezrozumiałe]. Jeszcze też [niezrozumiałe] tej prezentacji chciałbym, żeby po prostu najprościej pokazać, bo widać, że też podpisałem, ale teraz chciałbym też pokazać, że faktycznie to to, co podpisałem, w miejscu można powiedzieć, że to teraz znaleźć [niezrozumiałe]. Okropny jest ten dzień dobry. Tak naprawdę chciałbym zakładać weryfikacji tego konkretnego dokumentu, tego wpisałem się tyle zresztą, żebyście też widzieli, a [niezrozumiałe] nie mogą, który jak się wybierało. Dobra, po prostu tak [niezrozumiałe]. Odbierz tak się to pobierze. I teraz przejdźmy do [niezrozumiałe] Unii Europejskiej. Myśmy wtedy nowy dokument mieć nowszy dokument, utworzony się nim przed chwilą wielkie. To jest ten dokument, życzymy, sprawdźmy. Widzimy tutaj niezgodnych komunikat, że Skill prawnym przecież chodzi o inne [niezrozumiałe]. Możemy zobaczyć, czy tutaj też jakby wszystko jest jakby w porządku, jest taki podpis jak najbardziej. To też można powiedzieć poprawny, no i to jest niby wydawcy, w drugim przeszło, akurat nie mam to jest serwowanego [niezrozumiałe], nawet jest tutaj na macOS [niezrozumiałe], ale no widzicie, że to co robiłem, przyjmuje [niezrozumiałe]. No jednak jest tutaj akceptowane przez inne podmioty, no i musimy to proponować docelowego klientom, więc to to. No to tyle, jeśli chodzi o mnie w kontekście prezentacji.

**Przemysław Sołdacki:** Ja mam 2 pytania, pierwsze to jest, kiedy ta taka wersja już produkcyjna, dopracowana, kiedy ona może być dostępna?

**Adrian Kotowski:** Musimy ustalić biznesową aplikację, jak będzie wyglądała. Bo teraz, to jest prototyp, znaczy ja ten prototyp przygotowałem. Główny scenariusz, czyli podpisywanie, ale jeszcze musimy też, można powiedzieć, odpowiednio przygotować wypisywanie. Tyle, że to nowa, tylko po prostu dotować istniejący kod do tej nowej aplikacji. Ciężko mi powiedzieć. Myślę, że [niezrozumiałe] nie boli. Musimy o tym możesz wiedzieć, że całe wakacje.

**Przemysław Sołdacki:** Ale mnie nie chcemy, żeby ta aplikacja inne tryby robiła, tylko po prostu właśnie [podpis] padł.

**Adrian Kotowski:** Znaczy, to myślę, że tak to mi się bardzo podoba w aplikacji. Generalnie tego jeszcze aby tylko doradzić obsługę sytuacji, gdzie tam jest podpisywanie. Z raportu czytam, czytam szybko myślimy koncepcję, jak to będzie wyglądało. Zresztą problem tych certyfikatów, tym myślę, że tak, nie wiem, jest półtorej miesiąca, tak też było i czy też testy intensywny tej aplikacji, nie wiem, właśnie zakładając, że publikowanie zrobimy, to ja pytałem tej aplikacji na [platformie], że dużo pracy generalnie, żebyś tam jeszcze weryfikacji. No ale jak mówisz, półtorej miesiąca może by tak coś połączyć. I też nie było tak.

**Przemysław Sołdacki:** To to może, żebyś też Adrian tam nie poszedł za szeroko z tym tematem, bo kiedy w ogóle ten problem występuje? Bo jeśli klient chce sobie tam już wewnątrz AMODITa tam hurtowo podpisywać jakieś dokumenty typu [niezrozumiałe] czy w innych takich sytuacjach, no to to, że tam robi to na Windowsie to to nie jest problem, bo klienci po prostu mają Windowsa i jak trzeba to po prostu robione na Windowsie, więc tutaj tych różnych dodatkowych miejsc, gdzie podpisujemy, to nie musimy robić. Chodzi o przypadek, gdzie jest Trust Center i użytkownik, który ma podpisać to w zasadzie nie jest... znaczy ma macOS, a my nie bardzo mamy wpływ na to, kto to będzie. I chodzi o to, żeby ten przypadek, kiedy ktoś wchodzi, dostaje mailem, że ma do podpisania, a zrobił to na macOS, to żeby mu zadając jak najmniej pytań pomogło ten podpis złożyć. Bo tam ja widziałem nawet w momencie, kiedy się wybiera podpis, to tam było, że [niezrozumiałe], użytkownik może nie wiedzieć co to jest, ale tam było napisane. Podpis kwalifikowany, tylko jeśli mamy chmurowy i zwykły, to powinno być kwalifikowany na jakimś tam urządzeniu czy tam zainstalowany na laptopie, bo to jest jeden przypadek, a drugi podpis chmurowy. Który mamy SimplySign, żeby użytkownik po prostu wiedział, wybrał jak wybrał, że to jest na jego urządzeniu, to żeby mu zadało jak najmniej pytań, jak najmniej rzeczy było, że on coś musi ściągać, po prostu mu się poprowadziło go za rękę, żeby kliknął OK, wpisał PIN i żeby się podpisał. Jakby w tą stronę idziemy, nie? Jakby nie szeroko, tylko żeby to jeden konkretny przypadek, ale żeby on był jak najwygodniejszy.

**Adrian Kotowski:** Jest ciężko by to w jakiś tam właśnie [niezrozumiałe] w przeglądarce, bo to jeszcze nie mamy kontekstu, to jeszcze nie byliśmy tych sterowników, nie byliśmy tych weryfikatorów, więc tutaj trzeba będzie już najwięcej użytkownika, że mam wejść na przykład, że mam podpis chmurowy. Na przykład Szafir, że po prostu musi czy tak po prostu będzie [niezrozumiałe] tak jakby tego biednego sterownika, ale nie musi tak [niezrozumiałe] tak jak to jest tak trochę jednak na tym etapie, no można jeszcze to jest to dyskutowanie, bo to jednak ja przygotowałem prototyp. Jeszcze jest no kwestie te przechowywanie tych bibliotek, bo widzieliście jak te biblioteki miałem po prostu skitrane gdzieś, tak mówiąc delikatnie na [niezrozumiałe]. W rzeczywistości jest tak, żeby [niezrozumiałe] to pytanie, które jest jakaś grupa aplikacji czy schowane, ale tak jest na przykład takiej systemowej lokalizacji na maszynie, albo ewentualnie można jakoś sprawdzić. Należy pobrać, gdyby [niezrozumiałe] i takie jest to, że trudne akurat jest to już właśnie zwrócił uwagę na to. Życia właśnie myśleć jakbyśmy dostarczali te biblioteki. No w Polsce jest paru dostawców, nie jak już nieskończonej liczby.

**Piotr Buczkowski:** Musimy, musimy pewnie przejść przez wszystkich dostawców i przygotować.

**Adrian Kotowski:** Tak no, no właśnie my też widzimy 3 produkty komercyjne tego podpisu i no podejrzewam, że trzeba będzie też inny taki podpis przetestować.

**Piotr Buczkowski:** Się zbierać przypadki, obsługiwać tak. Dodać jakieś domyślne obsługiwanie.

**Janusz Bossak:** Dokładnie, tak to jest założenie.

**Piotr Buczkowski:** A jeżeli ten przypadek nie jest to to... No to zrobić tak jak masz teraz, czyli `SELECT` ten i ewentualnie gdzieś sobie raportować, tak, czego ludzie używają.

**Janusz Bossak:** Tak, tak dobra, ale słuchajcie, teraz nie ma co omawiać jakby technicznej strony tego. Znaczy tu dowód jest, że się da na macOS już podpisywać. Oczywiście ten proces, który widzieliście, jest jeszcze taki bardzo techniczny i trudny dla użytkownika i oczywiście nie jest to docelowy produkcyjny scenariusz. Jest to tylko i wyłącznie nasze tutaj deweloperskie Proof of Concept, że działa, nie, że można. I teraz trzeba z tego zrobić naprawdę dobry taki proces. No dla użytkownika tego, jak to Marian nazwał, zwykłego Kowalskiego, tak nie bardzo wie, że ma coś zrobić, tylko po prostu ma kliknąć. Ma mu wyskoczyć [okienko], ma wpisać PIN i ma być podpisane, a resztę to my musimy o to zadbać. Ale bardzo fajnie. Dzięki Adrian za tą prezentację. Dobrze, jedziemy dalej, kto tam dalej ma coś ciekawego do pokazania?

**Anna Skupińska:** Przypominam, pokażę to z gradientów.

**Damian Kamiński:** Możesz jak najbardziej. Akurat Przemka może to interesować.

**Anna Skupińska:** Nie jestem pewna czy jest... Aha, OK. To udostępnię. Czy widać już ekran?

**Damian Kamiński:** Tak.

**Anna Skupińska:** OK. Więc tutaj jest `AMODIT Local` i testowaliśmy edycję gradientów. To jeszcze nie będzie końcowy [produkt], bo wczoraj wieczorem w piątek jeszcze rozumiem, że [niezrozumiałe] jak ma wyglądać. Można resetować do domyślnej palety kolorów, można edytować sobie kolory i wybrać, jakie chce. To jest w stylu Zero, to jest też ta paleta, co można wybierać, więc mogę wybrać swój. Czym tutaj różowy, a tutaj niech będzie fioletowy jakiś ciemny. Zaraz stosuję i jest i się zapisuje. Tak i na razie można zmieniać kolory tego typu w Treemapie i w Pivocie. Myślę, że będziemy to dodać, zanim je wprowadzimy tutaj do kolumnowych, te kolory gradientowe, dlatego że tam jako one nie zostały skorygowane i [niezrozumiałe] u nich zrobione o tym. I poza tym Marek tam większość robił kolorów i musiałam się do niego zapytać trochę rzeczy, zanim zacznę majstrować. I Marek był chory, nie miałam okazji tego zrobić, tak.

**Janusz Bossak:** Właśnie to chyba Pivot i Treemap, no tam gdzie są takie agregaty, które mogą pokazywać pewną skalę.

**Anna Skupińska:** Tak.

**Janusz Bossak:** To jest OK. To jeszcze pamiętam, dyskutowaliśmy nad pokazywaniem tego nieagregowanego.

**Anna Skupińska:** Tak, tak, to jeszcze jeszcze tak. Janusz mi mówiłeś, żeby zrobić to w tym, ale chciałam to lepiej, żeby było ogólnie rzecz biorąc edycja gradientu, później można się zabierać za to w tabeli.

**Janusz Bossak:** To robimy to.

**Przemysław Sołdacki:** A więc co możesz taki przypadek ustawić, że tam jest na przykład ujemne? Jakieś tam to są, nie wiem, czerwone.

**Anna Skupińska:** Mhm.

**Przemysław Sołdacki:** No to jest powiedzmy szare, a...

**Anna Skupińska:** [Niezrozumiałe] takie, że tutaj za bardzo nie mam wartości ujemnych.

**Przemysław Sołdacki:** A OK.

**Janusz Bossak:** Tu jest tu jest minus 136.

**Piotr Buczkowski:** Jak to nie ma?

**Janusz Bossak:** Już 136 tutaj masz na [niezrozumiałe] na brak.

**Anna Skupińska:** A faktycznie, ale nie to nie to samo, to jest maks kwota. Przepraszam, bo kolory były brane z innego jakby innej wartości, to chyba była kwota 2 może? Nie to było pewnie o to. Też nie, a zgubiła mi się to z ujemną wartością.

**Mateusz Kisiel:** Chyba w sumie po Pivocie.

**Przemysław Sołdacki:** Wiecie co mnie zainteresowało, że tutaj te różne atrybuty mogą być. Niektóre są pogrubione, przekreślone, pochylone.

**Anna Skupińska:** A to to to jest wyraz czegoś innego zadania, to jest inna rzecz. To chodziło o to, że ja też robiłam, to chodzi o to, że możemy mieć w nazwach pól właśnie takie atrybuty i chodziło o to, żeby też w raportach się to samo pokazywało, więc, no jest.

**Janusz Bossak:** To jest inny test, jest inny test.

**Przemysław Sołdacki:** OK.

**Anna Skupińska:** Dlatego są takie różne atrybuty.

**Przemysław Sołdacki:** A takie atrybuty będziemy mogli mieć?

**Piotr Buczkowski:** Możesz sobie wstawić nazwę, nazwę, nazwę pola powiedzmy w tagu HTML-owym.

**Janusz Bossak:** Mamy klienta, który ma wzory chemiczne, chce wyświetlać.

**Piotr Buczkowski:** Albo [niezrozumiałe].

**Przemysław Sołdacki:** OK.

**Janusz Bossak:** N2H4, tak dalej.

**Przemysław Sołdacki:** Czyli nazwa danego atrybutu może być HTML-opisana, tak?

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** OK, no fajne, fajne, bo to jakby od razu zwróciło moją uwagę, dlaczego tak jest.

**Janusz Bossak:** Tak, znaczy, główny cel był taki, żeby właśnie te wzory chemiczne można było stawiać.

**Przemysław Sołdacki:** OK. Czyli Chatbot na przykład, tak, że można.

**Janusz Bossak:** Tak, tak.

**Anna Skupińska:** OK. Tutaj jest maks. Może [niezrozumiałe] minimum. OK, ja padam na kolana, minimum to będą jedne, tutaj też dał nam minimum.

**Mateusz Kisiel:** Dodajmy, że...

**Anna Skupińska:** I teraz są kolory. Ujemnego tylko że wszystkie są praktycznie takie same, więc nie ma takiej za dużej różnicy pomiędzy nimi. No OK, tutaj to jest mała różnica.

**Janusz Bossak:** Znaczy na razie jest tak zrobione. Dlaczego to robimy? Robimy dlatego, że no cóż, nasz ukochany pan Piotr Murawski, chciałby mieć możliwość zadawania swoich kolorów, jak zobaczył, jak pokazywaliśmy, że my mamy tylko taki tam niebieski do tego brązowego. Znaczy, ja mogę sobie ustawiać swoje kolory. Nie. No to już teraz może tu jest, oczywiście cała masa jeszcze innych pomysłów, tam jakieś skali tego środka przesuwania, że to wcale nie musi być zero, tylko może jakaś inna liczba.

**Anna Skupińska:** A ciąży wolę dać więcej punktów, na przykład pokażę to [niezrozumiałe] będzie inny kolor na tutaj się robił.

**Janusz Bossak:** Może być więcej. W razie MVP, tak, że jest, że można tę skalę taką, którą mieliśmy odwrócić, znaczy odwrócić w tym sensie zmienić na inne kolory. I tyle. Tutaj a propos.

**Przemysław Sołdacki:** Znaczy, wiecie, to już to już wygląda tak mniej więcej jak Tableau pozwala robić. Także ten Tableau jeszcze marzy. Można właśnie, że żeby to było [niezrozumiałe] w sposób ciągły i [niezrozumiałe] tam krokach, ale ale to już je daje dużo. O właśnie widać, które są dodatnie, które są ujemne, a które są takie bliskie zera, tak, czyli bardziej szare. To jest spoko, także fajnie, że to, że to jest. No trzeba to wrzucić do też do wszystkich typów wykresów, bo to też ma sens na przykład w wykresach słupkowych.

**Anna Skupińska:** A tak to zająłby klasa `Super` trzeba zrobić, żeby one obsługiwały gradienty w kolorach.

**Przemysław Sołdacki:** Albo znaczy, powiecie liczba można znaczy, kolor się używa, albo w takim zasadzie, że to jest jak się jak coś tam ma spektrum tej palety, znaczy, że jest właśnie ten gradient, nasilenie tego koloru, a drugi przypadek, kiedy kolor przypisujemy do konkretnej kategorii. Na przykład nie wiem, że to jest marchewka, że to jest pomidor i każdy ma swój kolor według palety.

**Anna Skupińska:** Już tak trochę mamy, jak wezmę na przykład w Treemapie i tutaj zamiast sum dam nazwę produktu. No to są [produkty].

**Przemysław Sołdacki:** Dokładnie i to działa dokładnie tak jak Tableau, także super.

**Janusz Bossak:** No dobra, świetnie Ania, dzięki. Dalej. Mateusz tam jakąś.

**Mateusz Kisiel:** Ja mogę komunikator pokazać, tak?

**Janusz Bossak:** Dobra, to.

**Mateusz Kisiel:** Widać ekran?

**Janusz Bossak:** Widać.

**Mateusz Kisiel:** Dobra, no to w tym sprincie właśnie dokańczam komunikator. Robiłem różne poprawki, stabilizacje tego. Różne błędy były też. Była to kwestia tego generowania procesów, żeby z tymi długimi kwestiami naprawić i pielęgnowanie te zmiany, które chciała Łukasz. To tak teraz ten komunikator można otworzyć też w [nowym oknie]. Zamiast osobnej karcie tam w ustawieniach systemowych jest taka opcja, no i ikona jest już nie Messengera, tylko takiego `Outlook` z `MD`. I no jak są jakieś nowe wiadomości, to się pokazuje licznik po prawej stronie, a nie w nawiasie wartość. No dobra. Na takich tam rzeczy, które powiedzmy doszły to, że jak się przewija do góry, on to jest `infinite scroll`, czyli, że się zaciągają starsze wiadomości. Automatycznie jest też przycisk do przejścia w dół. Różne poprawki były na przykład, że automatycznie się tam przewija, przewija w dół [niezrozumiałe] wiadomości. Też jest informacja, że ktoś coś pisze, jak ktoś sobie coś tutaj napisał, zmieni sobie czat na inny, tu coś napiszę, znowu powróci i to będzie miał tą starą też wiadomość, czyli nie tracimy tych informacji. No jak zamknie też to mamy, bo to będzie blokował `localStorage` czy zapisywany jest zwykle historycznie. Zmieniła się też działanie pobierania użytkowników. W tym momencie jest dodana paginacja, czyli też te w dół, jak się przejeżdża, też pobierają kolejny i tak dalej. Można sobie zrobić konwersację prywatną z jedną osobą lub grupową. To co tam mówiłem już kiedyś, ale nie było tutaj zrobione. Jak jest prywatna, to nie można zmieniać nazwy konwersacji, ani zarządzać nią, a jeżeli jest grupowa, to możemy usuwać użytkowników, dodawać. Musimy dać nazwę tej grupy.

**Janusz Bossak:** Gdzie mam taką uwagę? Nie bardzo mi pasuje słowo "grupa". Wolałbym, żeby to się nazywało "konwersacja". Nie wiem, no znaczy może być grupowa, ale nazwa grupy, tylko nazwa czatu, nazwa konwersacji.

**Mateusz Kisiel:** Tak. Znaczy, no, konwersacja sugeruje, że może być prywatna konwersacja.

**Przemysław Sołdacki:** Wiesz co, ale to się używa się pojęcia "grupa" w WhatsAppie i w Messengerze, jest po prostu grupa.

**Janusz Bossak:** Mamy też dość mocno zdefiniowaną "grupę", jako taką w AMODITcie i trochę mi to przeszkadza, że tutaj jest "grupa", bo zaraz będą oczekiwania: "to ja bym chciał tutaj grupę podpiąć", tak, a teraz tak nie jest, nie.

**Przemysław Sołdacki:** Ale wiesz, co znaczy rozumiem, ale nie wiem czy to jest... Bo znaczy to mogło być po prostu jakaś tam [niezrozumiałe].

**Piotr Buczkowski:** [Nie chodzi] o słowo "grupa", nie tutaj używane.

**Adrian Kotowski:** Chciałem po prostu "czat" na przykład, tak, żeby się nie kojarzyło z tymi silnikowymi.

**Janusz Bossak:** Bo nic nas tak [niezrozumiałe], tylko nazwa czatu, nie? To ten czat dotyczy czegoś, tak? Ten to nie chodzi o to, że dotyczy ludzi, tylko dotyczy na przykład omawiania integracji z [niezrozumiałe] tak i to jest nazwa czatu, a nie nazwa grupy.

**Łukasz Bott:** To nazwa konwersacji. Tak, no to.

**Janusz Bossak:** Konwersacji, no.

**Przemysław Sołdacki:** Ale, ale wiecie ja [niezrozumiałe]. Sprawdziłem teraz w `USA` jest właśnie jak klikam na te "nowa rozmowa" to pyta "czy to nowy kontakt czy nowa grupa" i to jakby to jest używane, no że to nie jest ta sama grupa, która jest grupą. Nie wiem użytkowników tam nie wiem w Windowsie czy w AMODITcie.

**Janusz Bossak:** Ale jest ale... Pan takie skojarzenie, no i jakoś mi to ciągle tak w [niezrozumiałe].

**Przemysław Sołdacki:** To znaczy tu się nazywa. Nie wiem w Messengerze, to się nazywa "czat grupowy". Tylko wiecie jeszcze tutaj inną rzecz zauważyłem, że z lewej strony jest "komunikator", a jak się klika w to, to pierwsze się pojawia "AMODIT Talk". Więc musimy ujednolicić. Nie możemy, że jest "komunikator", "czat", "Talk" i tak dalej. To się musi być jedna nazwa.

**Mateusz Kisiel:** Jeszcze raz to jest komunikator. Tak klikam na to.

**Przemysław Sołdacki:** Tak.

**Mateusz Kisiel:** I tutaj jest OK, czyli to trzeba zamienić na "Witaj w komunikatorze".

**Przemysław Sołdacki:** Tak. Tak i tam w ustawieniach pamiętam, że też było coś tam "AMODIT Talki" i to to nie może się tak znaczy, to musi być jedna nazwa, po prostu żeby było. Wiadomo, że to jest to.

**Mateusz Kisiel:** Z takich rzeczy jest też opcja tego wzmiankowania, tak, że jak mamy jakieś osoby w tej grupie, możemy je wzmiankować. W praktyce to nie działa jakoś szczególnie. No bo i tak dostanie powiadomienie, że została nowa wiadomość i tak więc w praktyce tylko tyle, że jest tekst napisany, czy powiedzmy Aneta przewozi. Tutaj mogę napisać tak, ale nie. Jeszcze raz Aneta. Przewozić. No tylko tyle, że [jest] napisane. Tak jakby to nie działa jakoś szczególnie w tym momencie, bo i tak dostanie powiadomienie i tak.

**Przemysław Sołdacki:** Słuchaj, na razie tak zostaw to jest. To jest OK, ale wiecie jeszcze mam pytanie, bo tam wiem, że to była odnośnie technologii, gdzie to jest, gdzie jest trzymane to w ogóle, bo chcieliście żeby oddzielna baza, ale to nie wiem.

**Mateusz Kisiel:** No tak i będzie inaczej działało na chmurze, inaczej `on-premises`. `On-premises` mamy jakąś powiedzmy bazę u klienta i na sztywno będzie się z nią łączyło, a na chmurze będzie tak, że będziemy sobie pobierać z bazy z organizacjami informacje jakie klient na jakiej bazie jest trzymany. No i na tej bazie będą będzie korzystał z tabelek, tak?

**Przemysław Sołdacki:** Nie będzie w tych samych [tabelach] w tej samej bazie co reszta tak.

**Mateusz Kisiel:** Tak, tak.

**Przemysław Sołdacki:** OK.

**Janusz Bossak:** Chciałbym na... czy `on-premises` inaczej, niech tak samo będzie.

**Przemysław Sołdacki:** To też mi się wydaje, że to powinno być tak samo.

**Mateusz Kisiel:** No ale to pod... potrzebujemy trzymać w innych miejscach tabelki, żeby nie łączyć danych różnych klientów.

**Janusz Bossak:** No tak, no ale skoro na chmurze?

**Piotr Buczkowski:** Znaczy to, że to, że może być w różnych bazach to nie znaczy, że to może być w jednej bazie. Nie może być w jednej bazie.

**Mateusz Kisiel:** No tak, tak, może może być w jednej bazie, jakby to nie ma problemu.

**Janusz Bossak:** OK.

**Piotr Buczkowski:** Czyli `on-premises` może być tak jak na chmurze.

**Janusz Bossak:** No no no rozumiem, to będzie wygodniejsze. No po co jeszcze jakąś tam osobną bazę danych nam [niezrozumiałe] instalować, no niech to będzie w bazie AMODITa, no ja tak to rozumiem.

**Mateusz Kisiel:** No tak, tak tak. Jakby tak tak jakby myślałem, że mu teraz mówicie, że `on-premises` inaczej, żeby zrobić dobra.

**Janusz Bossak:** Nie no ty powiedziałeś, że `on-premises` jest inaczej, dlatego.

**Mateusz Kisiel:** Znaczy no jest inaczej, bo się będzie pobierać `query string` z tego `connection string` z tam naszej bazy, ale to no trochę inaczej.

**Janusz Bossak:** No tak, ale ostatecznie to one będą.

**Przemysław Sołdacki:** No czyli zawsze będzie trzymane komunikator tam gdzie reszta AMODITa, tak?

**Mateusz Kisiel:** No tak, tak, może tak przyjąć.

**Przemysław Sołdacki:** OK, no no jest super.

**Janusz Bossak:** OK, no.

**Mateusz Kisiel:** Z takich to mogę pokazać jeszcze w tym jakąś zmianę?

**Janusz Bossak:** A tak z ciekawości się zapytam, czy pamiętałeś o WCAG, że tam ma być zgodne?

**Mateusz Kisiel:** Pamiętam, jakby jedyne co to w tym momencie kontrast jest zgodny, ale [niezrozumiałe] tak nie miałem czasu jeszcze robić. Czy na jednej czy to będzie kontrast? Ale no jeżeli jeżeli ktoś jest niewidomy, no to będzie miał problem, no bo w tym momencie nie przeczytamy to poprawnie.

**Łukasz Bott:** Ja mam jeszcze pytanie czy zabezpieczyłeś na przykład przed atakami XSS, bo ono tutaj będzie można wysłać tak naprawdę do wszystkich użytkowników w systemie.

**Mateusz Kisiel:** Ogólnie w Reactcie automatycznie jest takie zabezpieczenie przed XSSem, czyli jeżeli ktoś sobie napisze nie wiem jakiś powiedzmy znacznik nie wiem czy coś. No to domyślnie jakby to jest traktowane jako tekst, tak nie da się jakoś z tym nic zrobić.

**Piotr Buczkowski:** Ale to, ale to nie jest zabezpieczenie przed XSS. To jest wycinanie HTML-a, czy tam kodowanie HTML-a.

**Mateusz Kisiel:** Znaczy, no w praktyce każdy tekst jaki się pojawia w Reactcie są automatycznie ekranowane, jakby nie trafi surowo do HTML-a, tylko jest właśnie przez React też zabezpieczony.

**Janusz Bossak:** To trzeba sprawdzić, wiecie.

**Piotr Buczkowski:** Całkowicie tak.

**Łukasz Bott:** Panie przewodniczący, sprawdzić.

**Janusz Bossak:** Podobają mi się Wasze uwagi, słuszne tutaj Łukasz, że tak tak od razu na to patrzymy szeroko za każdym razem jak robimy takie [testy].

**Mateusz Kisiel:** Znaczy, ale to czy w ogóle w przypadku mówicie może, że się rozumiemy.

**Adrian Kotowski:** Znaczy ten tekst jest tak trzymany w bazie takiej postaci, bo rozumiem, że jak to nie było wycięte, to kwestia tego wyświetlenie później, że może teraz jako jest dobrze myślę dla [niezrozumiałe] jest tu, może będziemy musieli to jak [niezrozumiałe] na przykład.

**Mateusz Kisiel:** Znaczy no docelowo z tej bazy będzie miał dostęp tylko taki AMODIT, a jest napisany w Reactcie, no i wtedy jest OK. No jeżeli nie będziemy w [starej technologii] wyświetlać, to to nie będzie problemu.

**Łukasz Bott:** Mateusz, Mateusz tutaj Łukasz zwrócił słusznie uwagę, tak. Jeżeli możemy to zabezpieczmy dodatkowo na całe szczęście różnych.

**Piotr Buczkowski:** Nie, widać widać, że on wszystko encoduje po prostu, nie tylko nie tylko zabezpiecza przed XSS, ale przed jakimkolwiek HTMLem.

**Łukasz Bott:** OK, dobra.

**Piotr Buczkowski:** Znaczy u nas problemy wynikają z tego, że chcemy dopuścić HTML-a, a żeby ktoś na przykład chciał pogrubić jakiś tekst. I przypadkowo możemy dopuścić coś, że ktoś jakimś tam wymyślonym tagu wstawi jakiegoś jakiś skrypt.

**Łukasz Bott:** Chciałbym tylko...

**Piotr Buczkowski:** No a tutaj tego nie ma, bo tutaj cały HTML jest po prostu encodowany także jako tekst tylko.

**Mateusz Kisiel:** Tak więc no nie ma tego ryzyka. Jeszcze jest strona z logami. Czy tak, czy mamy powiedzmy jakieś błędy w tym AMODIT Talku, to możemy sobie podejrzeć. Tak na przykład mogę sobie wybrać `Errors` i będzie tu pisała jakieś [informacje]. Powiedzmy, że coś jest bardzo [źle], nie mógł połączyć na przykład. No i tego typu rzeczy.

**Mateusz Kisiel:** To w momencie, to jest w momencie logi, są zapisywane w oddzielnej, w oddzielnej tabeli. Nie ma chyba potrzeby teraz tego łączyć z AMODITem, wydaje mi się.

**Kamil Dubaniowski:** Może warto by było podlinkować, żeby tam dało się przełączyć na te logi z tych standardowych modeli AMODITowych, żeby tam na tej jednej stronie był przełącznik [niezrozumiałe] logi i ta metoda, no bo linku tam nikt nie będzie sobie zapisywał czy pamiętał.

**Przemysław Sołdacki:** Ale w ogóle dlaczego są oddzielne logi? Dlaczego nie są w tych samych tabelach?

**Mateusz Kisiel:** No bo docelowo chciałem, żeby była opcja, aby oddzielnie móc to zainstalować, tak, że powiedzmy oddzielnej bazie. No i też korzystam z Seriloga, który ma taką swoją strukturę, swoją strukturę tabeli z logami. To by było kompatybilne z AMODITem, więc to tak było wygodniej.

**Łukasz Bott:** Ale to może Mateusz rzuciłeś? Teraz pomysł to może skoro korzystasz z jakiegoś gotowego komponentu, to może ten komponent użyjmy też do prezentacji danych z tego loga systemowego AMODITa?

**Piotr Buczkowski:** Nie, to jest to logowanie, jeżeli chcecie.

**Mateusz Kisiel:** No nie, na serio to jest po prostu narzędzie tam do logowania, to to nie jest nic do wyświetlania, to wyświetlanie, to strona do wyświetlania zrobiłem w Reactcie.

**Łukasz Bott:** OK, dobra.

**Przemysław Sołdacki:** Wiecie, bo jakby mnie to dziwi, że na przykład mam takie logi z całego systemu w jednym miejscu, ale z jednej funkcjonalności mam w drugim miejscu to jest.

**Mateusz Kisiel:** No bo to jest takie podejście mikroserwisowe, tak?

**Przemysław Sołdacki:** No tak, dla użytkownika to jest tylko kłopot, a jeśli będziemy tam robić, żeby AI sobie jeszcze szukało i próbowało zdiagnozować, to dlaczego część funkcjonalności szuka w jednym miejscu? Część szuka w drugim miejscu. No błąd to błąd, no jakby dla systemu to znaczy. Nie wiem czy nie prościej byłoby to wrzucić jednak w te same logi.

**Adrian Kotowski:** Kiedyś mieliśmy takie podejście. Kiedyś był problem z aktywnością na proteście. Mieliśmy w oddzielnych tabelach i pamiętasz [niezrozumiałe] temu właśnie robiłem, żeby to w jednym miejscu jednak było. Być to trochę, jakby przeszli na koncepcję, którą mieliśmy ostatnio tak.

**Janusz Bossak:** No dobra, słuchajcie, to będziemy rozważać. Dzięki za uwagi, słuszne zresztą.

**Kamil Dubaniowski:** Ja bym jeszcze Mateusz na chwilkę jakbyś odpalił ten widok AMODITa, bo szczegół, ale... żebyś też na to zwracał uwagę. Z tą wersją, gdzie widać menu AMODITa po lewej, jeszcze dasz radę.

**Mateusz Kisiel:** Aha, dobra, to czekaj. No.

**Kamil Dubaniowski:** Bo zauważ, że przy tym widoku, no to już troszeczkę odbiega i warto używać tych samych komponentów, jak na przykład `search`. Tłumaczy [niezrozumiałe] w Talku, że właśnie innego to już mają jeden standard.

**Mateusz Kisiel:** Tu jest `search` jedno, a drugie znaczy gdzie?

**Kamil Dubaniowski:** W menu po lewej właśnie jak je tworzysz?

**Mateusz Kisiel:** Aha. Dobra, to tworzy w drugiej karcie.

**Adrian Kotowski:** Mam jeszcze takie pytanie. Czy mamy jakieś takie limitowanie na przykład znaków na pojedynczej wiadomości, żeby nie dało się jakiegoś nie wiadomo długiego [niezrozumiałe] wysłać?

**Mateusz Kisiel:** No widzę, jest taki kwadratowy [limit] trzydzieści. To mogę taki sam zrobić.

**Kamil Dubaniowski:** No tak bym patrzył i może te ikony, nie wiem, czy ci się uda [niezrozumiałe] pobierać też. Zobacz tam na górze masz swój [niezrozumiałe] imienny, no to też lepiej by pewnie było mi rozróżnić, ale to już takie na rozwój [niezrozumiałe].

**Mateusz Kisiel:** Na razie tutaj wstępnej wersji jeszcze bez awatarów zrobiłem. No i teraz kwestia tylko żeby to wdrożyć tak tam [niezrozumiałe] napisałem do Daniela [niezrozumiałe], żeby jakieś dane dostępowe mi dali, [żeby] to wdrożyć.

**Piotr Buczkowski:** Raczej raczej nie dostaniesz.

**Damian Kamiński:** Ja cię już wesprę w tym zakresie.

**Przemysław Sołdacki:** Widzicie, ale zwróćcie uwagę na to, żeby to jednak jednolicie, no bo tak jest tu jest "komunikator", wchodzi się, pojawia się napis "konwersacje" z prawej strony, "AMODIT Talk". Niech to będzie po prostu jedna nazwa, "komunikator" to po prostu "komunikator".

**Piotr Buczkowski:** Pomysł był taki, żeby to nie była częścią tak takiego tego dużego AMODITa, żeby nie dodawać nowych funkcjonalności.

**Przemysław Sołdacki:** Ja rozumiem, ale to OK ja to rozumiem, że tak miało być, ale tak czy inaczej żeby nie mnożyć po prostu różnych pojęć, tak tak samo jak zrobiliśmy AI i mamy AMODIT Copilot i po prostu wszędzie tak to się nazywa. Tutaj też niech to będzie jakakolwiek jedna nazwa, żeby i w ustawieniach systemowych i tutaj wszędzie, żeby to po prostu była jedna nazwa.

**Janusz Bossak:** No nie wiem. Może może nie musimy nazywać tego "komunikator", może nazwijmy to "AMODIT Talk" tak w menu już.

**Przemysław Sołdacki:** Wszystko jedno, byle się tak wszędzie tak samo nazywało, no może być.

**Janusz Bossak:** Będzie osobą własną, bo jak potem będziemy się chwalić, to tak się chwalimy, że oto mamy komunikator, a tak co mamy AMODIT Talka.

**Przemysław Sołdacki:** Wiesz, wszystko jedno tak jak tutaj jest u góry napis "konwersacje" mogłoby się nazywać "konwersacje" to jakby wszystko jedno, ale żeby wszędzie była ta sama nazwa. Bo inaczej to będzie się można pogubić.

**Janusz Bossak:** Tak, tak. Znaczy, wiecie to znowuż tutaj, dlaczego to robimy? Tak, bo to jest ważne, no robimy dla WIM-u tak była.

**Przemysław Sołdacki:** No tak, ale ale wiesz, będziemy ogłaszać i chcę oczywiście tutaj się chwalić, że mamy, no to, żeby to było spójne.

**Janusz Bossak:** Jak wiem. Chodzi o to, że to jest znowuż wersja minimalna po to, żeby zaliczyć tak i panu Piotrowi już się to spodobało. Zaliczone, może iść do odbioru, a teraz możemy to sobie upiększać, ulepszać i tak dalej. No więc no.

**Przemysław Sołdacki:** Znaczy, moim zdaniem to jest bardzo już szeroka funkcjonalność i to super działa. Podoba mi się, tylko mam uwagę taką, żeby to było spójne, nic więcej. No zobaczcie tu "obecni członkowie czatu", no i to jest zupełnie inna nazwa. Albo zróbmy. Albo no jakkolwiek niech to ma jedną nazwę, już znalazłem 5 różnych pojęć.

**Damian Kamiński:** Znaczy ja proponuję tak, to jest prototyp, który pokazuje Mateusz, jeszcze nie był w pełni testowany, więc jak już będzie gotowy, to wtedy dopiero będziemy go [pokazywać] klientowi. Ale Przemek ma rację.

**Janusz Bossak:** Są ważne te uwagi, słuszne, dzięki Przemek i po prostu trzeba teraz w następnym sprincie na dzień 2 poświęcić na to, żeby to ładnie przejrzeć, ujednolicić nazwy i tyle.

**Kamil Dubaniowski:** Wiecie no nie, pewnie wszędzie się będzie dało, no bo nie możemy zmienić na "obecni członkowie AMODIT" nie. No to jest czat mimo wszystko wewnątrz AMODITa, to jest czat.

**Mateusz Kisiel:** Znaczy konwersacji, tak.

**Kamil Dubaniowski:** Ona tak wiemy jak działać.

**Przemysław Sołdacki:** OK.

**Janusz Bossak:** I tak samo tam jest niżej "udostępnij całą historię" nie czatu, tylko konwersacji, tak.

**Mateusz Kisiel:** Tak. Tak, no. Takie szczegóły.

**Janusz Bossak:** A to tam [niezrozumiałe] przejrzeć tak ekran po ekranie i to. Co robić. Super, tam jeszcze chciałeś coś w `Billingach` mi pokazać.

**Mateusz Kisiel:** No tak, tam Łukasz chciał, żeby dodać w tej stronie, żeby dodać dodatkowe tam pola. Czy tak, czy mamy dla organizacji osoba, z którą się można skontaktować, czyli tam wpisujemy sobie kogoś, kto powiedzmy prosił nas o stworzenie tej organizacji. No i dla limitów jest też gdzieś tam komentarz, dlaczego komuś coś zwiększamy w tym momencie widzę jeszcze to niezużywane takie drobne rzeczy.

**Łukasz Bott:** To znaczy tak, no to kontekst biznesowy znów, ponieważ jest to narzędzie, które co prawda jest dla nas, tak, no, aczkolwiek klient też do swojej organizacji też ma tam dostęp, ale nie przynajmniej do tej części administracyjnej. Ale jeżeli chodzi o tą część administracyjną, to chodziło o to, żeby ułatwić życie tutaj. No osobom, które będą te ten billing generowały tak, no i między innymi to główne rozróżnienie. Na razie nie mamy tych dużo klientów, których jeszcze to to, to to pojedynczy klienci, ale jak dojdzie tych klientów więcej tak, no to żeby rozróżnić na przykład chociażby środowisko, czy to jest produkcja czy test, tak, tak, żeby osoby, które będą wystawiały faktury, to żeby szybciutko sobie były w stanie to jakoś tam gdzieś wyfiltrować. Tak, no to przy okazji Mateusz przypominam o filtrach tutaj, tak, żeby to gdzieś porobić te filtry właśnie na tych typie i typie i tym podobnych rzeczy. To to chodziło głównie tak, żeby tutaj pracę. No głównie tutaj koleżanek Oli i Justyny, które faktury wystawiają tak, to, żeby ułatwić troszkę życie.

**Mateusz Kisiel:** Tak no jeszcze jakieś testy wezmę, jakieś ulepszenia są w CRM były, ale z grubsza też wszystko.

**Janusz Bossak:** Dobra, dzięki bardzo. Co tam jeszcze coś ciekawego ma? Tam z tymi ustawieniami systemowymi, jak jesteśmy daleko. Kolega Filip. Czy to już tam coś z tymi zadaniami robiłeś?

**Filip Liwiński:** Tak, została jeszcze dzisiaj podepnę API do dodawania, usuwania, edycji, wykonywania akcji. I myślę, że będzie już pokrótce gotowe.

**Piotr Buczkowski:** Chciałby to zobaczyć.

**Janusz Bossak:** Coś można już pokazać z tego?

**Filip Liwiński:** Tak, mogę pokazać to ostatnie ekran.

**Janusz Bossak:** No to pokaż.

**Filip Liwiński:** Powinno być widać. Tutaj mamy okno modelu, dodawania też wybieraniu biblioteki `Models.Classes` albo inne. Nazwa klasy preferowanym serwer, częstotliwość i częstotliwość to jeśli będzie rozwijane. Zaproponował `v Zero` mogę pokazać. Gdzieś to mam tutaj. Żeby właśnie ułatwić to to, to właśnie tą częstotliwość. Takie podglądy tej godziny startu, do wybierania minuty. Nie dotyczy jest bazowane na typie częstotliwości.

**Łukasz Bott:** Czekajcie, czekajcie. Znaczy tutaj nie wiem, czy to może do Filipa. Nie wiem, czy dotarło tak, bo myśmy gdzieś troszkę planowali, czy rozmawialiśmy o tym, żeby to to ustawianie tej częstotliwości działania też znów uspójnić tak, jakby to, żeby to było wspólne w innych elementach AMODITa. Mamy przecież tamten częstotliwości reguł okresowych tak w procesach.

**Kamil Dubaniowski:** Tak, ale wycofaliśmy się z tego Łukasz, no bo będzie ciężej kompatybilność utrzymać.

**Łukasz Bott:** Tak.

**Damian Kamiński:** Ale tam nie ma takich opcji jak są tu.

**Piotr Buczkowski:** To jest całkiem co i inne inne rzeczy, no inny.

**Łukasz Bott:** Dobra, dobra, dobra, no dobra.

**Kamil Dubaniowski:** Także zostaje tak, tylko będzie przeliczane w tle. Czyli jak tutaj ustawiłeś godzinę 9:00, to standardowo musiałbyś sobie teraz policzyć, ile od północy jest minut do dziewiątej rano i takie ustawić przesunięcie. Tak pisać tam w minutach tak, że to i tak jest dużo ułatwień.

**Łukasz Bott:** OK, dobra, dobra, jeżeli to.

**Piotr Buczkowski:** Raz dziennie to jest `Daily` i pierwszy parametr to jest 9.

**Damian Kamiński:** `Hour`.

**Filip Liwiński:** Mhm.

**Kamil Dubaniowski:** OK, no to nawet jeśli, no ale te minutowe są najcięższe chyba.

**Piotr Buczkowski:** Jeżeli byś chciał, jeżeli byś chciał tak i żeby chciał, powiedzmy co 2 godziny, to wtedy to jest problem, bo musisz tak.

**Kamil Dubaniowski:** No także.

**Piotr Buczkowski:** Te 20 tak jakoś tam, jeżeli chcesz zacząć o ósmej, to tam musisz dodać tam 8 x 60, tak.

**Damian Kamiński:** No tak i to ta forma, którą tu koledzy prezentuje, jest dużo wygodniejsza. Tak, bo określamy co ile godzin, kiedy startuje. Kiedy kończy, więc jest bardziej intuicyjna.

**Łukasz Bott:** Jasne.

**Piotr Buczkowski:** No tak.

**Łukasz Bott:** OK, dobra, to znaczy zwłaszcza, że fajne, że wyświetla się na dole jak jak to będzie ta częstotliwość wyliczana, tak, że właśnie, że to w tej chwili, że to jest co jedną godzinę, tak nie określimy.

**Piotr Buczkowski:** Mi się to się zastanawiam jeszcze czy czy, ale to może jakieś kolejnej wersji, żeby bo teraz się wpisuje to bibliotekę. Czy klasę z palca równie dobrze można zwrócić listę dostępnych opcji?

**Filip Liwiński:** Mhm, no i tak poza tym to to zostało właśnie ten harmonogram do implementowania poza API i tutaj jeszcze mamy.

**Damian Kamiński:** Znaczy, zatrzymajmy się na chwilkę, bo to co powiedział Piotr, ja uważam, że jest bardzo istotne w sensie zdefiniujmy to od razu, bo tego jest tam 20 czy 30 pozycji, a wyeliminujemy, że ktoś popełnił błąd i zgłasza, że mu nie startuje Job. Bo źle wpisał.

**Łukasz Bott:** Dokładnie, zwłaszcza, że zwłaszcza, że tam chyba po prostu są pewne zależności tak przy wyborze jakiegoś zadania, to musisz konkretną bibliotekę, tak?

**Piotr Buczkowski:** Znaczy tak naprawdę będzie do wyboru jedna opcja, czyli klasa.

**Janusz Bossak:** To jeżeli tak można zrobić?

**Piotr Buczkowski:** No bo jak? Jak patrzysz bibliotekę, to tak naprawdę. Pierwsza nazwa to jest nazwa nazwa biblioteki, pierwszy człon nazwy klasy to jest nazwa biblioteki, tak.

**Łukasz Bott:** Był prośbę.

**Adrian Kotowski:** Tak myślałem, teraz wpadam. No powiem, że można na przykład zrobić taką weryfikację, bo tutaj wpisujemy nazwę biblioteki na przykład, a fakt faktem usługa ta będzie musiał wczytać.

**Piotr Buczkowski:** Nie, powiecie [niezrozumiałe] wszystkie, bo [niezrozumiałe] i tak zbiera wszystkie klasy tam implementujące ten interfejs `IJob`, tak, `IJob`.

**Adrian Kotowski:** Już można by sprawdzić na bieżąco, na przykład nie wiem. Mam literówkę w nazwie albo wpisałem złą nazwę biblioteki.

**Piotr Buczkowski:** Nie, nie, nie, nie będziesz nic wpisywać z palca.

**Damian Kamiński:** Słownik.

**Piotr Buczkowski:** Słownik będzie.

**Adrian Kotowski:** Na dzień dobry, dobra?

**Piotr Buczkowski:** Albo `AMODIT.Classes.FullTextSearch` czy `AMODIT.Jobs.FullTextSearch`, `AMODIT.Jobs.NotificationJob`.

**Damian Kamiński:** Nie jakieś `custom` na wszelki wypadek, tak?

**Piotr Buczkowski:** AMODIT for Rossmann, `Jobs.Origins.Sync` czy jak tam to nazwałem, już nie pamiętam.

**Adrian Kotowski:** Ale teraz tak, że skanujemy wszystkie `perki` jakby tego interfejsu, więc wiem, że to jest jakaś wydajne, bardzo.

**Piotr Buczkowski:** No tak, tak. Bardzo wydajny, to jest bardzo.

**Damian Kamiński:** Ale to robisz Adrian raz na ruski rok, za przeproszeniem.

**Piotr Buczkowski:** Przy starcie systemu. To jest robione teraz przy starcie, tak? Przy starcie procesu, o, może nie systemu, tylko procesu.

**Damian Kamiński:** To tylko w przypadku jak ktoś usunie, co nie jest standardowym działaniem, albo dorzuca jakąś nową, nowy Job na... wskutek jakiejś dedykowanej integracji.

**Piotr Buczkowski:** Jeżeli ktoś dodał, jeżeli ktoś, jeżeli ktoś doda DLL do projektu. No to proces, proces jest resetowany, jest odczytywany na nowo. Jeżeli też usunie jest to samo.

**Damian Kamiński:** No jeśli możemy, to skatalogować, się wybierać, to ja byłbym za tym, żeby od razu to wpuszczać na starcie i tyle.

**Piotr Buczkowski:** Tak.

**Łukasz Bott:** Tak, tak.

**Piotr Buczkowski:** Tak, tak, tak zrobimy.

**Łukasz Bott:** Filip, jeśli mógłbyś jeszcze pokazać, bo tak znów, to co prezentujemy, powinniśmy poprzeć jakimś kontekstem biznesowym, więc pokaż jak to obecnie wygląda dotychczas i dlaczego to zmieniamy? Tak no.

**Filip Liwiński:** No to obecnie wygląda to w ten sposób. Te wartości w ogóle nie są przejrzyste i nie są intuicyjne właśnie do dodawania czy na przykład usuwania, edytowania.

**Łukasz Bott:** Tak. Czyli tak to tak to wygląda obecnie, co jest, tak jak powiedziałeś? Słusznie jest to uciążliwe, co też Damian powiedział, że to się najczęściej konfiguruje, albo jest to konfigurowane, albo jak coś trzeba dodać. Ten odbywa bardzo rzadko, tam raz na jakiś czas. Niemniej no chcieliśmy sprawić i też, żeby uspójnić to z nowym wyglądem, tak z nowym podejściem do prezentowania ustawień systemu.

**Kamil Dubaniowski:** Czy ja ja też obstawiam, że ta intuicyjna konfiguracja usprawni może troszeczkę podnieść to jak konsultanci będą podchodzili do tego i będzie wydajniej, bo oni teraz włączą regułę co minutę i koniec i ona chodzi w weekendy niepotrzebnie tak po północy, bo bo nie potrafią godzinami.

**Piotr Buczkowski:** Możesz.

**Damian Kamiński:** Mhm, bo nie umieją tak.

**Piotr Buczkowski:** Dobrze mam jedną, mam jedną uwagę do Filipa, zachowaj format dat. Spójny z resztą systemu.

**Filip Liwiński:** Dobra.

**Piotr Buczkowski:** I w jednej linijce to po co? Po co to ma być 2 linijkach?

**Filip Liwiński:** Dobrze to zmienię. I jeszcze tutaj.

**Damian Kamiński:** No tak, bo tu w ogóle jakieś dziwne, ale to jeszcze rozumiem, że prototyp tak gdzieniegdzie jest szeroka gdzieniegdzie.

**Kamil Dubaniowski:** Era tak tak tak. Filip tutaj jakby odtworzył to co mi tam [niezrozumiałe] on.

**Piotr Buczkowski:** Nie widzę datę rozszerzają. Czy tam bardziej godzina w drugiej linijce? Tak.

**Damian Kamiński:** Mhm, no tak.

**Piotr Buczkowski:** Tam, gdzie nie ma godziny jest wąsko tak i jak `import XML`.

**Przemysław Sołdacki:** Był ze swoją uwagę. To jest pierwsza rzecz, która mi się rzuca w oczy i wygląda jak błąd 2 razy te same ikonka z lewej strony.

**Janusz Bossak:** Gdzie jest?

**Damian Kamiński:** Integracje rozszerzenia. No trzeba by było to zmienić.

**Przemysław Sołdacki:** Integracji i rozszerzenia.

**Janusz Bossak:** Winnego nie patrzymy teraz na tym.

**Przemysław Sołdacki:** Ale to jest dla mnie, to jest błąd. To jest pierwsza rzecz, co widzę.

**Kamil Dubaniowski:** Ale to będzie jedna zakładka, także nie ruszamy tego, nie ma co tego.

**Janusz Bossak:** Styl źle, ale zobacz, że jesteś na [niezrozumiałe].

**Przemysław Sołdacki:** Ale to będzie jedna zakładka. OK, to możemy od razu zrobić, żeby to była jedna zakładka, a jak się będzie nazywała?

**Damian Kamiński:** No.

**Janusz Bossak:** Zadanie no Przemek, no nie mieszajmy tego problemu. Jesteśmy na górze z zadaniem, reszta jest nieistotna.

**Kamil Dubaniowski:** Ale nie, nie to integrację, to będą integracje po prostu.

**Przemysław Sołdacki:** Integracja, OK.

**Kamil Dubaniowski:** Tam będzie lista i systemowych i definiowanych, co tak naprawdę teraz jest w 2 osobnych. Integracja modeli, to są integracje systemowe, które my dodajemy.

**Przemysław Sołdacki:** Widzę, widzę to nie wiem już pewnie z dziesiąty raz i za każdym razem to jest pierwsza rzecz, którą widzę, że jest kurde 2 razy tej samej ikonka jakby się ktoś pomylił.

**Damian Kamiński:** Tak tylko Przemku to wynika z tego, że to połączyć. Połączenie tego wymaga zbudowania dodatkowego modelu, gdzie ładnie będziemy wybierać te rozszerzenia systemowe z dostępnej takiej biblioteki. Dlatego no to nie jest takie hop siup, żeby to uspójnić, ale pewnie sprint albo 2 i to ogarniemy.

**Przemysław Sołdacki:** No dobra. OK.

**Łukasz Bott:** Chodzi o to, że myśmy w tej chwili otworzyliśmy mniej więcej w tym lewym menu, strukturę tego, co zakładarek w obecnym układzie.

**Przemysław Sołdacki:** To jest OK, ale wiecie, może można było drugą ikonkę wziąć inną po prostu.

**Łukasz Bott:** [Niezrozumiałe] lub.

**Janusz Bossak:** Dobrze, że mam mieć jakieś tematy do pokazania, kto tam ma jeszcze coś fajnego.

**Przemysław Sołdacki:** Po prostu jakąkolwiek, no.

**Damian Kamiński:** Łukasz ty prezentowałeś już, że to znaczy to jest w sumie podobne, więc pytanie, czy te ci użytkownicy wewnętrzni wiadomo. Formacie to było 2 tygodnie temu.

**Łukasz Bott:** Nowy widok dla użytkowników zewnętrznych to było w poprzednim sprincie.

**Janusz Bossak:** Przed [chwilą].

**Damian Kamiński:** OK, bo widzę, że to nadal wskoczyło w tym.

**Łukasz Bott:** Może testy się skończyły w tym.

**Damian Kamiński:** OK.

**Janusz Bossak:** Ale już u ciebie tematy.

**Mariusz Piotrzkowski:** Ja mógłbym ewentualnie pokazać prototyp działania tej funkcji `foreach attachment`, a więc zrobiłem w Instytucie, to było tak naprawdę poprawki błędów, jakiś hotfix i tego typu rzeczy, więc tam nie wiem czy jest cokolwiek pokazać.

**Janusz Bossak:** OK, no to jak skończymy tą funkcję `foreach attachment`, to będziemy.

**Mariusz Piotrzkowski:** OK, bo chciałem też pokazać to tym.

**Janusz Bossak:** Znaczy tak, tak jak było, jest potrzebna i robimy funkcję pętle po załącznikach, które są dodawane swobodnie do sprawy, tak, czyli są w tym prawym panelu. Do tej pory nie było za bardzo metody na to, jak się do nich dostać i jakie tam używać do różnych innych celów. Będzie funkcja `foreach attachment`, która po tej jakby w liście załączników może iterować. I coś można z nimi robić, tak, no nie wiem, zipa zrobić i wysłać gdzieś albo znaleźć jakiś plik, który chcemy coś z nim zrobić, zmienić mu nazwę czy cokolwiek innego, no ale nie było metody na to, teraz będzie.

**Łukasz Bott:** Znaczy, generalnie nie było metody na to z poziomu reguł, tak.

**Janusz Bossak:** Tak, tak, na poziomie reguł, żeby to automatycznie tam jakoś obsługiwać, nie.

**Łukasz Bott:** Fajnie, a takie potrzeby się ostatnimi czasy pojawiły. Tak to w ramach usprawniania wdrożeń.

**Janusz Bossak:** Dobrze. Przemek Rogaś.

**Przemysław Rogaś:** No ja mogę pokazać te ustawienia filtrów wymagane i domyślne.

**Janusz Bossak:** Dobra, to jest ważna rzecz.

**Łukasz Bott:** Czy to znowu taki troszeczkę kontekst biznesowy? Bo ja zgłaszałem te rzeczy to, ponieważ ja gdzieś tutaj pracuję nad reorganizacją, troszkę tych raportów systemowych, tak i właśnie wyszło, że takie usprawnienia by się przydały, czyli chodzi o coś takiego, że w tej chwili mamy, jeżeli mamy podłączamy jakieś źródło w szczególności źródło zewnętrzne, które ma dużo danych. No to ono nam się od razu wyświetla jego zawartość, a idea jest taka, żeby nie wyświetlać zawartości, dopóki użytkownik nie zdefiniuje wyraźnie wartości jakiegoś filtru. Tak przykładem może być nie wiem. Mamy przegląd logów jakiś tam systemowych. To musi wyraźnie zaznaczyć, że potrzebuje logi na przykład z ostatniego dnia, tak, albo nie wiem, z ostatnich 7 dni, dopóki tego wyraźnie nie zaznaczy, dopóty nie widzi nic, żadnych danych na wykresie czy tam. No generalnie w raporcie to takie trochę i troszkę inne to odrzucone trochę podejście, tak, bo my w tej chwili wyświetlamy wszystko co się da, a jak jest źródło o dużym rozmiarze? Tak no to bardzo dużo danych na wejściu jest generowanych. A tutaj odwracamy trochę tę [perspektywę] o 180°.

**Janusz Bossak:** Ja podam trochę inny przykład. Chcemy wyświetlić ilość spraw na danych na etapach w danym procesie, no i wyświetlenie tego zbiorczo nie ma sensu, no bo bierze wszystkie procesy i wszystkie etapy ze wszystkich procesów łączy. To jest kompletna, jakaś sieczka powstaje na wykresie. Natomiast jeżeli powiemy, że musisz wybrać proces, no to właśnie są te filtry wymagane, tak, czyli muszę ustalić jakiś proces w sobie na przykład obieg faktur i wtedy zobaczę ile jest spraw na poszczególnych etapach w tym procesie. No bo one są pewnie inne niż w procesie korespondencji, bo są zupełnie inne etapy, więc łączenie tego na jednym wykresie nie miałoby sensu i po to powstały filtry tak zwane wymagane, tak czy użytkownik musi je ustawić po to, żeby cokolwiek sensownego zobaczyć i nie nie pokazujemy takiej wtedy sieczki jak do tej pory, że było tam nie wiem. Tysiąc na przykład kresek, które w ogóle nic nie oznaczały i nic nie można było zobaczyć. No dobrze, to pokaż jak to się ustawia i jak to działa.

**Przemysław Rogaś:** Więc zostawiamy tutaj w menu w filtrach możemy ustawić jako wymagane. Wtedy, jak ustawimy jako wymagane, tutaj nie można zmienić. Nie można schować filtra, jakby był schowany, to zostanie [zmieniony]. Teraz przechodząc tutaj mamy informacje, że aby ustawić wartość w filtrze, tutaj jest. Border w kolorze żółtym. I po ustawieniu filtru dopiero pokazuje się raport. Jak usuniemy, to tak samo. Potem mamy informacje. Możemy ustawić wartość domyślną. Wtedy też mamy od razu po [kliknięciu] pokazuje się raport. Jak usuniemy, no to wtedy. Jest informacja. No i to w sumie tyle można dodawać do kolejnych. Kolejny, no to musimy wybrać 2. Tą wartość domyślną możemy usunąć tutaj przyciskiem. No i tak to wygląda w sumie.

**Janusz Bossak:** Bardzo fajnie.

**Mateusz Kisiel:** A ta wartość domyślna nadpisuje `localStorage` czy... Wiem, że to była kiedyś taka opcja, że `localStorage` by zapisywał filtr, jakie są ustawione.

**Przemysław Rogaś:** Wartość tak nadpisuje, nadpisuje. No jest sprawdzane. Te filtry są za każdym razem przy wejściu w raport. Są sprawdzane, no bo właśnie jest też taka sytuacja, że przykład wartość domyślna ustawimy 26. I możemy na przykład teraz usunąć?

**Mateusz Kisiel:** Mhm. I odświeżyć.

**Przemysław Rogaś:** I. I to ogólnie się zapisuje w `localStorage`, ale teraz jak odświeżę, no to jest na nowo wartość domyślna, tak, czyli jakby `localStorage` ten `null` się zapisuje, no ale ta wartość domyślna i tak zawsze będzie zaaplikowana.

**Łukasz Bott:** A słuchaj, co w sytuacji, gdy to jest wartość domyślna, a zmień na jakąś inną niż to 26, niż to domyślną, ale też nie `null`, tak, że no nie wiem, XYZ, weź to. Tylko bez 26 został tylko XYZ. Zastosuj no i i chyba o to Mateuszowi chodziło tak i teraz jakbyś wyszedł i wszedł ponownie do raportu, czy pozostanie ten moje ustawienie XYZ? Tak, bo Mateusz [dopytywał].

**Przemysław Rogaś:** No tak, no bo to jest to jest tylko jeżeli nie ma wartości, jest sprawdzane jakby wszystkie filtry są sprawdzane czy nie mają wartości. Jeżeli nie mają, no to wtedy dopiero jest domyślnie.

**Łukasz Bott:** OK, dobra. Dobra, no to nie no fajnie to wygląda.

**Janusz Bossak:** No dobrze. No i tak jak mówiliśmy, to jest głównie podyktowane tym, że rozbudowujemy ten moduł raportów systemowych. I tam są tego typu rzeczy potrzebne, no po to, żeby sensowne dane w raporcie systemowym wyświetlać. Na przykład, żeby nie pokazywać danych tam z jakiegoś długiego okresu czasu i tak dalej. Tu oczywiście ktoś może powiedzieć, ale są filtry, te ograniczanie zawartości, tak ograniczanie zawartości też jest dobre, tyle że ogranicza na sztywno tak i użytkownik już więcej nic nie może, a tutaj możemy dać na przykład szerszy zakres. Na przykład nie wiem z 3 lat i ustawić domyślnie, że to jest ostatniego roku. Ale użytkownik może sobie przeanalizować jeszcze poprzedni rok czy 2 lata wstecz, bo te dane są tak, ale domyślnie ma już ustawione na przykład, że tylko pokazuj dane z tego roku. Czy z tego miesiąca i to daj po prostu więcej możliwości dla takiej osoby już korzystającej z samego raportu, tak.

**Łukasz Bott:** Tak, to w szczególności, że ten filtr taki pod spodem, który jest, czyli ten ogranicza zakres danych. No to pomijając to, żebyśmy nie zrobili jakiegoś interfejsu informującego o tym, że on jest ustawiony tak i tego użytkownik, o ile tego gdzieś w tytule albo w opisie raportu nie damy tak, no to może być w ogóle nieświadomy, że tam jest jakieś ograniczenie.

**Janusz Bossak:** Słuchajcie, ja muszę skończyć ze swojej strony, bo mam spotkanie z nauką. Właśnie się zaczyna, mnie tam wywołują. Na temat sztucznej inteligencji, także ja tam uciekam, ale tu ewentualnie kontynuujcie i coś tam zmierzamy też do końca, no bo czas już powoli się też kończy.

**Mariusz Piotrzkowski:** Ja mam tylko prośbę o wzorniki na to co do ciebie napisałem na [niezrozumiałe]. A to już masz za chwilę?

**Przemysław Rogaś:** No dobra, prawda, mnie to w sumie tyle.

**Damian Kamiński:** Dobrze, czy ktoś jeszcze chce się czymś pochwalić?

**Przemysław Sołdacki:** Ja tylko bym dał jeden komentarz, bo my sobie tak przeglądamy dosyć tu luźno ten sprint, natomiast to co mi brakuje to żeby miał to jakoś mógł powiązać z naszą roadmapą, bo to co tutaj jest to jakby żadnej z tych rzeczy nie mam na roadmapie, a te rzeczy to na roadmapie to jakby nie mam komentarza co tam się z nimi dzieje także. To fajnie byłoby.

**Damian Kamiński:** Znaczy nie do końca, bo tutaj ustawienia systemowe, to co wchodziliśmy, to jest jakiś tam element. [niezrozumiałe], czyli pokrycia Reactorem. Natomiast tak dużo rzeczy też robiliśmy pod WIM. Tak, tak jak tu już wspominał. Co nam troszkę tą roadmapę wywraca, ale OK. Zwrócimy na to uwagę.

**Przemysław Sołdacki:** Ale wiesz co to to ja wolałbym dostać taką informację, że na przykład, skoro robimy i wiemy, że będziemy robić to, żebym dopisał do roadmapy po prostu. Czy nie? Przychodzę, że jeśli ma powstać komunikator, no to sobie dopiszemy do roadmapy "komunikator" i zaznaczymy, że go wykonaliśmy, bo skoro roadmapa się pozmieniała, no skutek tych czynów okoliczności zewnętrznych, no to po prostu, żeby to mieć zaktualizowane, żebym no ja chciałbym mieć na koniec każdego kwartału, znaczy, co nam się udało, co nam się nie udało i wiemy, że zmieniliśmy i czegoś nie robimy. Więc coś innego, to taką informację wolałbym na roadmapie mieć.

**Damian Kamiński:** No dobrze, to pewnie już w takim dedykowanym gronie do roadmapy musimy się spotkać i to zaktualizować.

**Przemysław Sołdacki:** Dokładnie. Koniec. Dobra.

**Damian Kamiński:** No dobrze, to jeśli nikt, nikt już nie chce się niczym więcej pochwalić.

**Piotr Buczkowski:** No ja mam za drobne rzeczy, żeby...

**Damian Kamiński:** No rozumiem, niektórzy po prostu realizowali błędy czy poprawki czy jakieś tam drobniejsze kwestie związane z funkcjami. Także na tym chyba zakończymy.

**Przemysław Sołdacki:** Dzięki.

**Damian Kamiński:** Dzięki.

**Łukasz Bott:** Dzięki.

**Adrian Kotowski:** Dzięki, cześć.

**Kamil Dubaniowski:** Dzięki, dzięki, cześć.

**Filip Liwiński:** Dzięki, cześć.

**Janusz Bossak:** Zatrzymano transkrypcję.

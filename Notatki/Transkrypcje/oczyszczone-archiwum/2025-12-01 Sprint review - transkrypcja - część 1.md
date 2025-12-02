**Data spotkania:** 1 grudnia 2025, 07:59 - część 1

---

**Adrian Kotowski:** Cześć.

**Mariusz Piotrzkowski:** Cześć.

**Barbara Michalek:** Cześć.

**Damian Kaminski:** Cześć.

**Filip Liwiński:** Cześć.

**Anna Skupinska:** Cześć.

**Marek Dziakowski:** Cześć.

**Lukasz Bott:** Cześć.

**Janusz Bossak:** Cześć.

**Patrycja Walaszczyk:** Cześć.

**Janusz Bossak:** Jak tam zima do was dotarła?

**Damian Kaminski:** W ubiegłym tygodniu był śnieg w ubiegły weekend, ale w tym nie. W Warszawie pusto.

**Janusz Bossak:** Ona się jakoś trzyma tak troszeczkę, ale.

**Mariusz Piotrzkowski:** U mnie lód na chodnikach taki, że się dwa razy prawie przewróciłem.

**Janusz Bossak:** Tak, wczoraj, przedwczoraj to było strasznie. Po prostu nie dało się iść. Dosłownie. Lodowisko na przystankach było.

**Mariusz Piotrzkowski:** Słyszałem, że w Bydgoszczy na SORze jest pełno osób takich właśnie, co mają jakieś złamania czy coś, bo się przewrócili.

**Janusz Bossak:** No nie dziwię się. Naprawdę, szliśmy z żoną właśnie tam do tego, szliśmy, no to się nie dało iść. Momentami trzeba było iść ulicą, bo tam jedynie było jakoś bez lodu, ale na chodnikach to po prostu jakaś tragedia. Dobrze, jesteśmy w komplecie. Jeszcze nie wciągniemy Kamila. Piotra nie ma dzisiaj? Dobrze? No dobra, to tak mniej więcej w naszym gronie jesteśmy. Także jeśli się dołączy, wiadomo. Oddaję ci głos może.

**Damian Kaminski:** No dobrze, to znaczy, jeśli ktoś jest gotowy i chce zacząć, to to nie ma problemu. A jeśli nie, no to ja mogę zacząć od jednego z produktów poprzedniego sprintu.

**Janusz Bossak:** Ja bym chciał, żebyśmy szli, że tak powiem, projektami, nie.

**Damian Kaminski:** A dobra, no dobrze, to znaczy, no to okej. To zacznę od pierwszego projektu, który nadzorowałem tutaj wspólnie. Do tej pory pracowaliśmy nad nim z Danielem i z Przemkiem. To jest pierwsze wydanie, zawiera błędy. Więc pierwsze takie wydanie, które od strony już samej aplikacji jest jakkolwiek używane i w tym sprincie będziemy rozbudowywać się o kolejne funkcjonalności i eliminować błędy. Tu jeszcze dopiero w piątek udało nam się to zwizualizować i spiąć. Mówię oczywiście o repozytorium plików. Więc to nam się udało. W poprzednim sprincie możemy zarządzać tą strukturą, czyli tworzyć nowe przestrzenie, czyli te węzły najwyższego rzędu. Możemy, czy nie możemy? Dzisiaj tego przyznaję, że jeszcze nie przetestowałem. Wiem, że jeszcze prace trwały w weekend, więc może coś się, może coś się tu rozpoczęło. Niemniej...

**Janusz Bossak:** No jeszcze tak.

**Damian Kaminski:** Co do zasady mogliśmy tu tworzyć, to już jest efekt naszych działań po stronie frontendu. Możemy wgrywać pliki, możemy te pliki przeglądać tak, jak tutaj widzicie. Mamy jeszcze problemy, że te pliki się wielokrotnie wyświetlają, no ale to tak jak wspomniałem wcześniej, jest taki pierwszy prototyp, który uzyskaliśmy i właśnie w ramach tego prototypu mamy możliwość definiowania struktury w głąb, czyli i te węzły najwyższego rzędu i podwęzły, i możliwość redefiniowania nazw tych folderów, tych węzłów, jak również ich usuwania. Możemy też właśnie wgrywać pliki. Na razie to wgrywanie pojedynczych plików poprzez tutaj kliknięcie "wybierz plik". Docelowo będzie można tutaj metodą drag & drop w ten obszar roboczy ładować większą ilość plików. Jeśli chodzi o ograniczenia plików, to analogiczne jak w kontekście AMODIT. Samo wyszukiwanie tutaj akurat nam już działa, ale tylko po tym, co jest widoczne. Czyli jak wpiszę jeden, to wyświetlą mi się wszystkie węzły, które zawierają jedynkę. Natomiast tego jeszcze nie dopracowaliśmy. To jest tylko i wyłącznie już efekt filtrowania po wyświetlanych elementach. Jeszcze będziemy nad tym pracować, żeby to działało analogicznie jak w menu, bo tyle nam się udało. Nie wiem, czy tu są jakieś pytania. Zakładam, że za dwa tygodnie będziemy już mieli bardziej dopracowaną wersję. Myślę, że teraz już zaczniemy też w ramach tego, że w piątek de facto udało nam się wydać i spiąć tych kilka elementów frontendowych z backendowymi, to już od tego sprintu będziemy tu również angażować właśnie koleżanki testerki.

**Janusz Bossak:** Nie no super, bardzo fajnie. Dobrze, że to już się frontend z backendem spina. O to chodziło, żebyśmy już doprowadzili do takiego stanu w miarę działającego tak. No i teraz ten sprint, żebyśmy już na koniec tak jak się umawialiśmy sprintu tego, który zaczynamy, żeby to już było zainstalowane w WIMie i żebyśmy mieli feedback jakiś od klienta. Ale dobrze, no idzie dobrze.

**Damian Kaminski:** Okej, no to w tym zakresie to wszystko. Czy ktoś chce, czy ja mam wywoływać po kolei? Czy ktoś chce się wypowiedzieć?

**Adrian Kotowski:** Ja mam przygotowaną prezentację odnośnie zmiany w SignApp, to mogę teraz. Jestem przygotowany i mogę odpalić.

**Damian Kaminski:** Proszę bardzo.

**Adrian Kotowski:** Dobra. W ostatnim sprincie budowałem aplikację do podpisywania na maku. Aplikacja jest, można powiedzieć, ma wszystkie te elementy, które sobie ustaliliśmy w MVP. Teraz dzisiaj chciałbym zaprezentować główną nową funkcjonalność, która została jeszcze dodana, wcześniej brakowało. To jest podpisywanie multi, podpisywanie masowe z raportu. Tutaj mogę wybrać, czy jest... dane, które istniały wcześniej w tej poprzedniej wersji aplikacji, więc to nie jest jakby nic nowego, aczkolwiek, no dałem teraz to, żeby to było podpisywanie jakby w tej nowej wersji aplikacji. Więc tutaj wybieramy opcję podpisywanie. Zaznaczyłem dwa elementy, czy tam więcej niż jeden. Wybieram opcję "Uruchom aplikację SignApp". Teraz mi się tworzy, tutaj mam właśnie widok, więc teraz wybieram opcję "Podpisz". Co wybrałem właśnie Szafir. Teraz w aplikacji Szafir generuje kod. Sobie tylko muszę zaraz się szybko zalogować. Mam jakiś kod. To jest to właściwie uwagi, to jest to, że udało mi się poprawić przy okazji podpisywanie. Przedtem teraz trzeba podać tylko jednorazowo, a nie właśnie dwa razy przybycie podpisaniem dokumentu. I teraz nam się pojawi ekran drugiego dokumentu. Muszę jakby dwa razy to zatwierdzić dokument, bo po prostu dwa dokumenty. I dać aplikacja. Czy to łącznikiem się dokumenty mi się podpisały? Tak, ponadto jeszcze też dałem... Nie było jak się wydaje... Odkryliśmy nową sesję podpisywania. Widzimy tutaj po stronie AMODIT. Mamy tutaj wizualną informację, jeżeli coś się dzieje, to byśmy, że teraz się na przykład rozmyśliliśmy i chcemy dobra, to jednak nie, jednak trzeba było trzy dokumenty wybrać, a nie dwa, więc zapamiętałem. I też jakby to się będzie działo w sensie podpisywania po prostu... Też jak wizualizuje przez SignalR. Jest takie jeszcze innych rzeczy, to też dałem wyzerowanie certyfikatów, które tego może nie widać, ale teraz pokażę. Wcześniej to powiedziałem. W poprzednich wersjach SignApp było trochę tak, że wyświetlały nam wszystkie certyfikaty, czy aktywne, czy nieaktywne i to można było sortować, znaczy filtrować w sensie aktywne, nieaktywne. Włącz nieaktywne. To ma jeszcze dodałem coś takiego jak domyślne nie wyświetlanie certyfikatów, które jakby którymi nie możemy podpisać. Bo załóżmy jakiś certyfikat, że certyfikacji i... który tak naprawdę nie służy do podpisywania, ma inną rolę akurat w naszym systemie. Ale jeżeli przed wyświetlany, że stąd widzimy tutaj, że widzimy tylko wszystkie te certyfikaty, które faktycznie, które faktycznie do czegoś nam służyły, które pozwolą podpisać dokument. Jeśli ktoś chciałbym się tutaj pokazać, jak wygląda sytuacja, w której na przykład nie mamy żadnych certyfikatów dostępnych, bo nie wiem, czy to pokazywałem ostatnio. Załóżmy, że... aplikację do podpisywania, zaraz zamknie odświeżymy. To tak, widzimy też ekran specjalny ekran informuje, że nie ma tu sobie certyfikatów. I jeszcze tego chwilkę jeszcze teraz pokażę. Ponowne włączenie tutaj przejść tak na otwarcie jeszcze raz... Powinno się brać odświeżyć to okienko. O tak, widzimy te certyfikaty. To tak ogólnie, czy po prostu mówiąc to tutaj mamy już aktualnie wsparcie dla dwóch podpisów w sensie Szafirem. Jak testowałem, praktycznie też mamy wsparcie dla podpisów PW, ale nie było możliwości... Może być jakieś pytanie.

**Przemysław Sołdacki:** Tak, może takie dziwne, ale ty dlaczego ta aplikacja się nazywa AMODIT SignApp 3?

**Adrian Kotowski:** No znaczy poprzednie wersje nazywały się albo nic... 2, więc możemy to zmienić ewentualnie. Znaczy tutaj przyjąłem jak się 3.0, bo ta wersja na Windowsa tak. Tutaj teraz wszystko już dostają numerek właśnie dwójkę, żeby wiedziałem, że wreszcie jakaś jedynka, ale więc tak tak przyjąłem, że przynajmniej w kontekście wersji, żeby to jakoś wyróżnić, bo to jest.

**Przemysław Sołdacki:** To co na dole się pojawia, że to jest wersja trzecia, jest okej. Tylko że w samym tytule, no czemu się pojawia? To trochę wygląda jak jakaś taka wersja testowa. To jest. A druga rzecz, jak się tutaj w ten guzik w lewym dolnym rogu "Podpisz certyfikatem", to tam też jest "Podpisz SignApp", bodajże się to nazywa.

**Damian Kaminski:** Czy?

**Adrian Kotowski:** Ok, dobra?

**Przemysław Sołdacki:** Tak, to to to jakby nie...

**Damian Kaminski:** Dobrze, ze jeszcze raz.

**Przemysław Sołdacki:** Bo tutaj "Podpisz SimplySign", no to jak ktoś ma SimplySign to rozumie, ale "Podpisz za pomocą SignApp", nie wiadomo co to jest, bo ktoś mówi "ja nie mam, mam Szafir".

**Damian Kaminski:** Tak.

**Przemysław Sołdacki:** I jakby nie... Moim zdaniem nie wiadomo co to jest.

**Adrian Kotowski:** Czy też istniejąca jakby.

**Damian Kaminski:** Znaczy tak, jest to nie jest coś, co teraz powstało, to z tego klienci korzystają i są świadomi, co to jest.

**Przemysław Sołdacki:** Ale jeszcze jakieś chociaż... że to jest nie wiem, że podpisz własnym certyfikatem czy coś takiego.

**Damian Kaminski:** Chyba, że mówimy o nowych.

**Janusz Bossak:** Czy nie mieliśmy?

**Przemysław Sołdacki:** Czy tam "Podpisz innym certyfikatem"?

**Janusz Bossak:** Żadnego z klientów nie mieliśmy żadnego zgłoszenia, że to jest niezrozumiałe.

**Adrian Kotowski:** Czy myślę, że jest taka różnica też, bo na przykład w Trust Center jest tutaj napis "Podpisz certyfikatem kwalifikowanym", "Podpisem kwalifikowanym", a tu jest "Podpisem...". Więc akurat w przypadku Trust Center to jest chyba bardziej taka jakby... I mówi, że podpisem kwalifikowanym, bo jest jakieś tam nazwy aplikacji.

**Przemysław Sołdacki:** Że tak mi, tak mi się wydaje. Wiecie, bo wiadomo, że jeśli klienta już przeszkolimy, to on nie będzie zgłaszał, że to jest jakiś problem, tylko takie pierwsze użycie to bym trochę nie wiedział co to jest. No to jest detal, ale po prostu to...

**Damian Kaminski:** Może i masz rację. Z drugiej strony podpisywanie masowe z raportu to jest już użycie bardziej zaawansowanych użytkowników, więc trzeba by się zastanowić czy to na pewno tu, czy z poziomu sprawy ewentualnie.

**Przemysław Sołdacki:** Zastanówcie się, czy po prostu nie zmienić nazwę, no bo to proste jest tak. Jeden napis zmiany kwalifikowanej, wtedy się aplikacja Szafir pojawia i to jest ok, ale po prostu, że wiadomo, że do czego ta opcja służy. No dobra, tylko tyle.

**Damian Kaminski:** Przedyskutujemy.

**Adrian Kotowski:** No bo tutaj to jeszcze tego nie wracałem z tego tej aplikacji tej dałem się wielkie, jakby takie brakujące mniejsze się tam wizualne elementy tej podświetlanie, likwidowanie, bo połączanie aktywnych, nieaktywnych certyfikatów. Czy akurat to nie widzisz tego, bo mamy tylko te certyfikaty. My takie wszystkie drobne elementy, jakieś tam, które były w projekcie. Dodałem też więc, no to generalnie już ta aplikacja. Myślę, że jest gotowa do publikacji, tylko innym się teraz blokerem jest to, że po prostu dalej czekamy na to weryfikację konta oraz tego pro subskrypcji Apple Developer ID, więc tylko teraz ograniczy, żeby to aplikacje wydać. Aczkolwiek możemy już się wydawać jako przykład taki prototyp do klientów, to klienci nie będą musieli tam zatwierdzić się z tymi operacyjnymi na maku, że no tak, zaufaj temu dostawcy, ufać tej aplikacji. No ale już można z tego korzystać. Na przykład właśnie na maku, więc to też sprawdzałem te... które tutaj wygenerowałem, to tam są na zielono w Adobe Readerze, więc tam myślę, że też to jakoś w miarę wygląda. No to jeszcze jest ta aplikacja, nie jest jakąś odpowiedź, nie ma wszystkich 100% funkcjonalności jak ten SignApp dwójka, bo na przykład nie ma tej opcji wybierania na przykład języka, nie ma to jakiś tam załóżmy dark mode, chociaż nie wiem czy w ogóle dark mode to były w ogóle w tej aplikacji drugiej. No jeszcze tam są dodatkowe... która można jakby tam dodać, to u mnie dodanie nowego certyfikatu nie jest jakimś problemem dużym, tylko trzeba go po prostu mieliśmy jak się testować, ale na razie mamy dwa certyfikaty, które najpopularniejsze w Polsce, więc myślę, że tutaj powinno to wystarczyć dla większości klientów.

**Janusz Bossak:** No dobra, czyli takie MVP jeden możemy zamykać, to jest to, co chcieliśmy. Certyfikację jeszcze dla aplikacji samej jako takiej trzeba zrobić i na razie temat zamykamy. To jest to co potrzebne jest też dla WIMu, no bo tu między innymi dla WIMu było tak. No dobra.

**Adrian Kotowski:** Tematu. Dzięki to daje głos i ekran.

**Damian Kaminski:** Okej. Czy jest ktoś chętny na następny? No dobrze, skoro nie, no to po kolei. Tabele. Filip, Kamil.

**Kamil Dubaniowski:** Pole tabela tak? To Filip, nie Mariusz.

**Damian Kaminski:** Nie mam na myśli styl tabel dla design. O, przepraszam, nie na te. Przepraszam, wrócił, tak?

**Kamil Dubaniowski:** Ten na ten sprint pass.

**Damian Kaminski:** Dobra, przepraszam, już się poprawiam.

**Kamil Dubaniowski:** Ale tak, tak wywołaliśmy temat, to ja wróciłem. Porządkowanie wyglądu pola typu tabela na formularzu i to był powiedzmy pierwszy krok, który chciałbym zrobić, bo gdzieś tam nam się troszeczkę ten wygląd tabeli rozjechał w pewnym momencie. To Mariusz, jakbyś mógł pokazać, co tam się udało i jeszcze są 2 czy 3 zadania na ten sprint w tym temacie rozpisane.

**Mariusz Piotrzkowski:** Dobra już pokazuje.

**Kamil Dubaniowski:** Ale to mniejszy temat, ale równie istotny. Głównie wyszedł z tematów zgłaszanych po prostu przez klientów, którzy testowali wersję czerwcową.

**Mariusz Piotrzkowski:** Były drobne zmiany odnośnie przycisków na w tabeli tego przycisku, co jest pod tabelą do dodawania. Gdzieś to miałem tabele w tym chyba.

**Kamil Dubaniowski:** To pokazuje, bo Daniel pewnie będzie tym zainteresowany. To chyba Neuca zgłosiła, jak dobrze pamiętam to nie, ale chyba nie ma.

**Mariusz Piotrzkowski:** Dodaj sobie przykładowa tabela. Na razie zostało zrobione coś takiego, bo tylko miałam chyba 2 czy 3 zadania na ten sprint. To zresztą na kolejny mamy. Yy. Po pierwsze było jakieś tam ujednolicenie nazw, bo były chyba inne nazwy w tych dwóch miejscach. Po drugie to zrobimy taki fajny przycisk, który nie jest już nieaktualna, dać oddzielnie tak jak wcześniej, tylko połączony. Mamy "Dodaj", czyli główna akcja wykonywana często i dwie dodatkowe. No i to w sumie chyba tyle z tego tematu co było z tabelami, bo resztę chyba Marek robi jeszcze.

**Kamil Dubaniowski:** Tak, Marek jeszcze rozumiem.

**Damian Kaminski:** Ale to import. Teraz jednak wróciliście z importem do tego hamburgera też.

**Kamil Dubaniowski:** Na to było zgłoszenie, które weszło przypadkiem. Klient to zobaczył. Powiedział, że cieszy się, że go posłuchaliśmy, więc ja nie chcę już się z tego wycofywać. To zgłosił Łukasz, nie wiedząc, że my tą opcję przenieśliśmy.

**Mariusz Piotrzkowski:** No i teraz jest w 2 miejscach.

**Damian Kaminski:** Okej.

**Kamil Dubaniowski:** I klient dostał tą wersję, to Neuca właśnie, więc już zostawmy to, niech będzie. To menu trochę też się zmieni wyglądowo, bo tego tej ikony, które teraz mamy w menu używamy do lewych menu do zwijania rozwijania, więc tu pojawią się takie przycisk typu 3 kropki jak menu zwykłe. Ale już uznałem, niech mają, nam to jakoś tam szczególnie nie nie przeszkadza. To było więcej zmian, tylko Marek to od razu puszczał do wersji, bo to były jakieś proste CSSy między innymi.

**Mariusz Piotrzkowski:** On chyba muszę do dewelopera, to ja mogę zobaczyć co tam się zmieniło. Ja swoich tam jeszcze nie puszczałem, więc nie będzie moich zmian tam, ale to potem się połączy.

**Kamil Dubaniowski:** Tak. Ten przycisk co Mariusz robił, pojawił się z wyglądu na to, że jak tabela ma więcej kolumn i pojawia się poziomy scroll, to scroll był bardzo blisko od tego ala przycisku, bo wcześniej to były tylko po prostu tekst "Dodaj". I tyle i ludzie, chcąc scrollować przez przypadek, dodawali wiersze. O tak to wyglądało wcześniej. Tu widać u Marka, czy starczy tego?

**Mariusz Piotrzkowski:** Znaczy, to jest to jest to deweloper, bo mówi, że wrzucał na deweloper wrzucał chyba.

**Kamil Dubaniowski:** Tak, tak, tak, tak, tak, tak.

**Mariusz Piotrzkowski:** A co dokładnie zmieniło, bo nie pamiętam?

**Kamil Dubaniowski:** Yy przesunęliśmy te ikony do sortowania bliżej nazw, bo u ciebie jeszcze prawdopodobnie to jest takie rozszerzone, że nie do końca wiadomo czego dotyczy konkretna ikona, zwłaszcza kolumny więcej.

**Mariusz Piotrzkowski:** A rzeczywiście, rzeczywiście.

**Kamil Dubaniowski:** Marek poprawił pozycjonowanie tego przycisku do drag & drop. Zrobiliśmy go w mniej takim agresywnym kolorze, bo to nie jest raczej nadużywana akcja ten po lewej. I nie wiem czy zdążył, mieliśmy też zrobić, żeby na hover się X podświetlał, bo też był taki jakby nieaktywny. To ty chyba robiliśmy już, czy Marek? Marek, no u ciebie jest jeszcze tak na sztywno, że to no cały cała całe wiersze podświetla. Tutaj dodaliśmy ten kolor, jakieś takie mniejsze rzeczy, ale tak jak mówię, to co klienci zgłaszali. Zgłosiłem też, żeby zwiększyć odstępy nieco tam raz 2, a teraz jest chyba jeden piksel między wierszami i to też w niektórych przypadkach się zlewa. I tak samo między kolumnami. Zobaczcie, jak nie jest blisko tego inputa do wpisywania kolejnej kolumny tego Marek jeszcze nie.

**Mariusz Piotrzkowski:** No nie, to też Marek. Już wyjście?

**Kamil Dubaniowski:** Ale to jest chyba zgłoszone.

**Mariusz Piotrzkowski:** Mhm, tam rozpisałeś.

**Kamil Dubaniowski:** Znaczy jest zgłoszone na pewno tak, także to i będzie trzeba.

**Damian Kaminski:** No to sortowanie zmienia indeksy wierszy, czy to jest tylko?

**Kamil Dubaniowski:** Ale to te ID nie, nie, nie to znaczy zostaje tak jak jest, bo to jest numeracja, a CaseID case index o to ci chodzi ten typ pola tak robił indeks jest row index no.

**Damian Kaminski** 19:18  
To indeks chyba tak.

**Kamil Dubaniowski:** Działa tak jak działał do tej pory. Spodziewam się, że zmienia, ale dopiero po zapisie. Nie mam pojęcia szczerze mówiąc.

**Damian Kaminski:** Okej.

**Kamil Dubaniowski:** Tego nie ruszaliśmy tylko lokalizację i one się zmieniają tak jak mówię, jak tam jest tego więcej.

**Damian Kaminski:** Jasne.

**Kamil Dubaniowski:** A i tutaj ID wiersza też to dodatkowa kolumna, która wyskoczyła mu. Mariusz ją sobie włączył. Na wcześniej miał jakieś dziwne nagłówek, taki wybór i podkreślony jakoś dziwnie to wyglądało, więc zrobiliśmy z Markiem albo Mariusz nie wiem kto to realizował Marek, tak żeby on był lżejszy, bo jest techniczny, to niech będzie taki wygaszony, a wtedy on był wręcz jakby wyróżniony spośród wszystkich jak po jakieś nie wiem najważniejsze, ale jest dosyć techniczny tego biznes raczej nie używa.

**Mariusz Piotrzkowski:** Chyba też Marek.

**Kamil Dubaniowski:** No i tak jak wspomniałem jeszcze tam jakieś zadania są rozpisane w tym sprincie. Chciałbym się przejrzeć jak wygląda tabela w tabeli, bo to też nie wygląda jeszcze najlepiej. Tam pojawiają się jakieś rytualnie potrzebne. To też chciałbym poprawić. Dobra, to nie wiem, ale czy miałeś jakieś jeszcze tam tematy tak jak?

**Mariusz Piotrzkowski:** No to będą to poprawiały. To miałem jakieś konsultacje z Adrianem i tego typu rzeczy, ale to raczej nie ma co pokazywać. Plus jeszcze jeden temat w trakcie, które jeszcze nie zdążyłem dokończyć.

**Damian Kaminski:** No dobrze. Dobra, to może Mateusz i ta instrukcja, bo myślę, że to jest fajna rzecz też tutaj dla działów wdrożeniowego i serwisowego. Jest to na razie, może dopowiem, że jest to na razie pierwszy prototyp w celu zweryfikowania, jak to działa, czyli i miejsce, gdzie z tego można skorzystać i zakres to jest produktem ostatecznym, będzie jeszcze elementem dopracowywania, ale sama funkcjonalność jest. Proszę Mateusz.

**Mateusz Kisiel:** Doszła dodatkowa funkcja dla tego Copilota naszego, która specjalizuje się w tworzeniu dokumentacji do procesu. Na przykład stwórz mi dokumentację do procesu OCR v3. Jest proces, który się nazywa OCR v3 tam 3 jakiś dopisek jeszcze jest, to on go znajduje i tworzy dokumentację. Widzę, że pobiera sobie pierwsze dane tego procesu. W tym sprincie też powstałe 2 rzeczy związane z MCP, możliwość dla naszego AMODITa, aby podłączać się do zewnętrznych serwerów MCP. Teraz dwójka to jeszcze zrobiłem, że można stworzyć w AMODIT serwer MCP. I można używać naszych funkcji z AMODIT wewnątrz jakiś innych aplikacji. I na przykład w Cursorze, że stworzył.

**Damian Kaminski:** Możesz Mateusz rozszerzyć MCP, żeby dla wszystkich było zrozumiałe co to daje faktycznie.

**Mateusz Kisiel:** To jest taki standard uruchamiania funkcji przez właśnie takie czaty LLM, czyli przykładowo może by mieć jakąś funkcję do pobrania listy procesów czy do pobrania jakiś dodatkowych informacji. No i w Cursorze czy w jakiejś innej aplikacji jakiekolwiek jak podłączymy się tego serwera naszego w AMODIT to jest możliwość aby mógł te funkcje wywoływać i mieć dodatkowe informacje o AMODIT. Do tego kto to zrobił dokumentację dla tego procesu. Mogę go teraz pobrać w Markdownie?

**Janusz Bossak:** Tutaj dodam, że ten to znaczy to generowanie procesu, ten jakby wzorzec to wzięliśmy z działu wdrożeń, to oni nam dostarczyli się tym momencie i to jest jakby jeden rozdział z tego dokumentu, który nam dział wdrożeń dostarczył, czyli rozdział opisujący pojedynczy proces. Tak no cały dokument jest szerszy. Ma sekcje dotyczące tam ustawień systemowych, ogólnie takiej architektury i wszystkich procesów i raportów i tak dalej na razie to co teraz pokazujemy to jest generowanie jednego z rozdziałów o jednym z procesów, tak potem bardziej rozbudowane.

**Mateusz Kisiel:** Tak to jest na... To jest... To jest na razie taka wersja wstępna, to jeszcze będzie udoskonalany. Na razie od czwartku o tym rozmawialiśmy. Nie poprawiałam tego jeszcze. Ale tak pobierany jest najpierw tworzona jest sekcja "Opis procesu", jest tak jakiś opis biznesowy, do czego to ma służyć. Następnie etapy procesu, no w tym wypadku jest jeden etap, będzie jeszcze tworzony diagram tych etapów i wyświetlane w Wordzie czy Markdownie. Pola jakie są... no i te pola będą... będą... będą z opisem też jak jest taki opis nadany w tym wypadku opisu nie ma. Reguły jakie są w tym procesie?

**Lukasz Bott:** No właśnie miałem zapytać o te opisy, ten opis podstawowy procesu to jest generowany na podstawie tego, co zostało wprowadzone do opisu, czy on sobie wy...

**Mateusz Kisiel:** Znaczy tutaj...

**Lukasz Bott:** ...wykoncypował co ten proces robi?

**Janusz Bossak:** Potrafi wykoncypować nawet jeżeli nie ma jawnie wpisanego opisu dla procesu, to on całkiem sensownie sam wymyśla na podstawie jakby samej...

**Lukasz Bott:** To jest... Okej.

**Damian Kaminski:** Tak pewnie będzie to docelowo połączenie tego tak jedno i drugie.

**Lukasz Bott:** Ale, ale jakbyśmy opisali proces? No właśnie chodzi mi o...

**Janusz Bossak:** Jakbyśmy opisali no to będzie miał szerszy kontekst, nie będzie więcej wiedział.

**Lukasz Bott:** Jest dobra, ale no, ale nadal coś sam własnego wymyśli tak, ale nie...

**Janusz Bossak:** Tak, nawet jeżeli nie ma formalnie tego pola, opis procesu wypełnionego to i tak i tak potrafi wygenerować opis.

**Damian Kaminski:** To jest prototyp pierwszy, który...

**Lukasz Bott:** Dobra, ale jeżeli pole będzie wypełnione, to użyje te pole.

**Damian Kaminski:** Nie Łukasz, to znaczy tak jest to pierwszy prototyp, który stworzyliśmy, który produkuje tak jak teraz i teraz możemy nad tym pracować i ustalić, czy jeśli jest pole wypełnione, to ma tak jak ty powiedziałeś. Na razie tak nie jest. Czy to ma być kombinacja tego, co jest opisane w tym polu? Rozszerzona? To, co wie o o samym procesie, czy ma w ogóle na przykład tego to pole być nie wiem. Opis procesu jako takim zdefiniowany oddzielny jakiś kontekst wynikający z aspektów technicznych.

**Lukasz Bott:** No okej dobra no. Okej dobra.

**Damian Kaminski:** To jest wszystko do dopracowania bardziej na razie udowodniliśmy, że coś takiego się da zrobić. Ta funkcjonalność na układa jakkolwiek ustrukturyzowany ten dokument zgodnie z naszymi wytycznymi, no teraz na pewno wymaga to dyskusji dalszej, co w ramach tej tego standardowego opisu powinno się zawierać. Czyli na przykład dopracowanie tego, że każdy etap jest opisany z wszystkimi możliwymi przyciskami na nim do wyboru, co jest wygodne z perspektywy takiego użytkownika jako instrukcji tak, bo wtedy ma od razu przechodzi do konkretnego paragrafu z opisem etapu i ma wytłumaczone co się stanie pod każdym przyciskiem, który użyje tak.

**Mateusz Kisiel:** Okej. W ogóle w tym wypadku wydarzy... on nie użył tej funkcji, bo... W tym momencie on jak do siebie wygenerował na podstawie... tego procesu. Tej funkcji nie użył, bo nie skomentowałam tego i będę musiał to jeszcze przywrócić. No w tym momencie może potem odpalę, jeszcze pokaże jak to wygląda. Mogę pokazać w tym MCP jeszcze jak to jest?

**Damian Kaminski:** Znaczy, ja nie wiem czy czy jakie funkcji nie użył.

**Przemysław Sołdacki:** Poczekajcie, bo ja mam jedną wątpliwość, bo nie mam tego na roadmapie, że to robimy. I nie wiem czy jest jakiś w ogóle projekt tego jak to powinno działać, no bo tutaj jakby mnóstwo pytań się pojawia, czy to będzie tylko tak, że mogę z tekstu sobie wywołać w z czata, czy będę miał gdzieś guzik wygeneruj dokumentację, czy będę mógł wygenerować naraz dokumentację całego systemu, czy każdy proces oddzielnie, jakby jest mnóstwo pytań, więc pytanie, czy mamy jakiś projekt, ale ja tego też na roadmapie nie mam, więc nie do końca wiem.

**Janusz Bossak:** To jest rzecz, która... No nie no Przemek. To jest to, co Mariusz Mateusz Kołakowski między innymi zgłaszał i robimy, no zgodnie z tym, co żeśmy się umówili, no najpierw rzeczy, które oni chcą. A jedną z nich jest tworzenie dokumentacji.

**Przemysław Sołdacki:** To Janusz to ja muszę mieć to na roadmapie, bo nie wiem tego na roadmapie.

**Damian Kaminski:** No dobrze, to myślę, że to należałoby, jeśli Przemku do tego nie widzisz, to to uzupełnimy już poza dzisiejszym spotkaniem.

**Przemysław Sołdacki:** No tak, to sobie zróbmy spotkanie, no bo są rzeczy z tych rzeczy, która jest zaproponował Mateusz i Daniel. No to wybraliśmy niektóre rzeczy na roadmapy, ale tego nie ja. Nie mówię, że to jest zły pomysł, bo uważam, że to bardzo dobry pomysł, żeby to zrobić, tylko to musi być na roadmapie i musi być opisane te te właśnie przypadki użycia, kto kiedy może to zrobić.

**Damian Kaminski:** Jak najbardziej tu pełna zgoda. Słuchajcie, to co prezentujemy, to jest efekt pracy 3 dniowej chyba może maksymalnie czterodniowej Mateusza i to mówiąc dniach kalendarzowych, a nie w roboczo godzinach. Raczej udowodniliśmy, że fajnie to zaczyna działać i teraz na podstawie tego, że mamy taki efekt, musimy siąść, zaplanować, gdzie to ma być, jak ma być dokładnie struktura tego dokumentu rozpisana więc na razie tylko pokazaliśmy, że taka funkcjonalność jest dostępna i jest na razie w pierwszej fazie prototypu.

**Mateusz Kisiel:** Rozmawialiśmy już takie przyjemne, mogły być w tym miejscu, pod zależności na przykład tak i ktoś by sobie po prostu chciał wygenerować dokumentację. To tylko klika trzydziestki się wygeneruje.

**Przemysław Sołdacki:** Jakby to to jest właśnie kwestia, żebyśmy to dobrze zaprojektowali, bo to jakby tak mówię mi się podoba, że to w ogóle jest potrzebne. Na pewno tylko żeby było wiadomo jak to działa. I też druga wątpliwość, w którym się pojawia. No bo mamy coraz więcej funkcji dostępnych z poziomu Copilota, ale użytkownik musi wiedzieć, czy może takie funkcje użyć, czy jakby, jak to rozwiązać, to jest do zastanowienia.

**Mateusz Kisiel:** No to mogę pokazać jedną z rzeczy, którą właśnie też robiłem w tym sprincie. Czyli jest serwer MCP no i docelowo tak jakby można sobie dodać jakiś serwer zewnętrzny do AMODIT, czyli wpisać nazwę jego ścieżkę, gdzie on się znajduje, ewentualnie jeżeli chcemy chcemy przez sieć, żeby był odpalany, to można dać Remote HTTP i wpisać adres jego. No i po takim zadaniu. Trzeba kliknąć przycisk synchronizuj narzędzia i tam pobiera sobie narzędzia z tego MCP no i przykładowo tu jest dodany jakiś Weather Service, który jest uruchomiony na na serwerze u nas testowym. No i można go zapytać dzięki temu jaka jest pogoda we Wrocławiu, tak?

**Przemysław Sołdacki:** Ale znaczy ja to rozumiem, tylko ty sam dodajesz wewnątrz AMODITa dużo funkcji, żeby i skąd zwykły użytkownik ma wiedzieć o co może pytać.

**Mateusz Kisiel:** Tak do do czego chce dojść? Tak i wiem właśnie teraz kontynuując. Tak więc no docelowo jest pomysł taki, żeby dołożyć tutaj jeden serwer, który będzie zawsze i to będzie serwer AMODITa i tutaj będzie lista funkcji dostępnych w AMODITcie i będzie można zarządzać, kto ma dostęp do jakich funkcji, czyli przykładowo. Yy no będzie jakaś funkcja, nie wiem pobrania pobrania szczegółów procesu, to będzie można sobie ustawić uprawnienie w niej, czy ma być dostępne dla wszystkich, czy tylko dla administratorów, czy dla jakiejś wybranych grup czy użytkowników. I dzięki temu będzie można...

**Przemysław Sołdacki:** Tylko to jest od strony administratora, ale też chodzimy o stronę użytkownika. Czy jestem sobie użytkownikiem? Wchodzę w Copilota i jak się dowiedzieć o co mogę go poprosić tak czy on powinien mi sam nie wiem, że mogę takiego helpa wywołać, że powiedz mi o co tam nie wiem o co mogę cię pytać, ale to też nie nie wpadnie użytkownik, że może o to zapytać, że może dostać takiego, więc dobrze jakby nie wiem jakiś guzik czyli podpowiedź, nie wiem, pokaż dostępne możliwości.

**Mateusz Kisiel:** No tak.

**Przemysław Sołdacki:** Cokolwiek?

**Janusz Bossak:** No.

**Przemysław Sołdacki:** No to zastanawiałem, więc jakby widzę, po prostu powstają kolejne rzeczy i one są fajne tylko użytkownik może nie wiedzieć, że takie są.

**Janusz Bossak:** Ja myślę, że użytkownik...

**Damian Kaminski:** Z jednej strony masz rację, a z drugiej strony patrząc na rozwój tych wszystkich AI no to żaden AI takiego czegoś nie ma.

**Janusz Bossak:** Znaczy, jak użytkownik będzie się o coś pytał, no to albo się dowie, albo się nie dopytaj. Na przykład jak powie proszę, opisz mi taki proces i on nie opisze, znaczy będzie wiedział, że to nie potrafi, tak, jak znaczy trochę tak nie bardzo rozumiem jakby. Cel tego można tak jak który wypisał teraz Mateusz, tak jakie masz dostępne funkcje? No i proszę bardzo, no to postaci takiej konwersacyjny odpowiada co potrafi nie.

**Przemysław Sołdacki:** Znaczy podam wam przykład, nawet ja próbowałem sobie wygenerować, PBI. I nawet mi się udało, ale tak patrzę. Kurde szkoda, że tej specyfikacji, którą ustaliłem z czatem nie mogę pobrać się okazało, że mogę, tylko muszę go o to poprosić, ale nie wiedziałem o tym i jakby myślę, że przybywa nam funkcji, więc jakby w pewnym momencie to już nikt nie będzie pamiętał jakie te funkcje są, więc takie. No nie wiem, wiecie, zgłaszam taki temat, no to zastanowienia jak to zrobić, no bo większość użytkowników nie wpadnie na to, że mogą o coś poprosić na przykład nawet wygenerowanie dokumentacji. Tak. Czy mogę poprosić o wygenerowaniem dokumentację procesową, może dokumentacji całej, a może coś jeszcze więc do zastanowienia jak jak tutaj Copilot może pomóc w tym, żeby właśnie pokaz? Jeszcze umie robić no ale widzę, że to się wypisało tak tylko lepiej też nie wpadłbym na to jakie żeby takie pytanie zadać.

**Damian Kaminski:** Trzeba się nad tym pochylić, bo z drugiej strony też no właśnie tych funkcji, tak jak powiedziałeś jest coraz więcej, więc jeśli wywalimy taką ścianę tekstu to też nikt nie będzie tego czytał i znowu trzeba będzie, a ja żeby to zweryfikować.

**Przemysław Sołdacki:** No dokładnie.

**Damian Kaminski:** Ee. No ale warto może się nad tym zastanowić.

**Przemysław Sołdacki:** Czy wiecie, bo czasami te LLMy mają także się pojawiają jakieś guziki z sugestiami, albo wprost pyta, czy chcę, chciałbyś jeszcze coś tam, no to to też jest fajne, bo bo jakby podpowiada co jeszcze może zrobić tak, czyli na przykład jak ja tam rozmawiam o procesie, to mógłby spytać, czy chcesz, żebym ci wygenerował dokumentację? No to ale to zostawianie, ja nie wiem jak to zrobić, ale ale taki problem wydaje mi się zaczyna się pojawiać, no bo po prostu jest dużo tych funkcji i to fajnie, że jest dużo funkcji, to żeby było wiadomo jak się do niej dostać.

**Mariusz Piotrzkowski:** W Copilocie na Studio Code czy Visual Studio pełnym jest coś takiego, że jest takie, że taka rozwijana lista, która zawiera wszystkie dodatkowe funkcje, jakie on może wykonywać i nazwijcie można sobie włączać lub wyłączać nawet jego funkcję, jeżeli byśmy chcieli, żeby czegoś tam odpalał przez przypadek. Na przykład budowanie projektu automatyczny, no i może żeby takie coś też dodać wrogu do naszego czata, że przycisk miałem wybierz funkcję, czy po prostu funkcję, mechanizmy możliwości, żeby użytkownik wyłączyć coś, czego mu się nie podoba, że nie wiem, żebym nie miał, nie odpala. Automatycznych procesów czy cokolwiek. Może coś takiego, bo trzeba zrobić.

**Przemysław Sołdacki:** To włączanie wyłączanie to jest jakby drugi etap, ale wiecie może taki nie wiem, jakiś znak zapytania jak w helpie i on wtedy powie. Zobacz, możesz mnie pytać o to i tamto to przykładowo, no tak, żeby ktoś mógł wpaść na to osoby. Na przykład tu widzę, że umie opowiadać żarty programistyczne, no w życiu bym nie wpadł, że umie to robić.

**Mateusz Kisiel:** No bo jest taki dodany serwer MCPI tak jest Joke Service i dzięki temu nie i że to wyłączę to już nie będzie umiał.

**Przemysław Sołdacki:** A okej. Jasne, znaczy jedzie, ale jakby zgłaszam ogólnie takie zagadnienie, że do wymyślenia jak to robić, żeby yy. Żeby można było się zorientować co umie robić, bo to, bo to fajne jest jak bym dużo rzeczy umie robić, no to żeby jakby żebyśmy się łatwiej tym chwalili. Okej, dobra, nie wtrącam się dalej.

**Mateusz Kisiel:** Tak no i.

**Damian Kaminski:** Dobrze, jeszcze w kontekście tego MCP jakbyś Mateusz, bo według mnie tutaj brakuje kontekstu biznesowego nieco, bo mamy pogodę. Mamy Joke Service, ale to są jakieś takie przypadki testowe, a jakie możemy mieć z tego korzyści biznesowe?

**Mateusz Kisiel:** Jeszcze. Przykładowo klient będzie miał jakiś inny system i ten system będzie udostępniał serwer MCP. Na przykład nie wiem, może jakiś Comarch czy coś innego to będzie można się podłączyć do niego i wykorzystywać jego funkcję. Czyli nie wiem zapytać się jakieś tam dane tak samo jak u nas o AMODIT jest opcja pytania się o jakie są dostępne procesy, to może nam się zapytać o coś z innego systemu i też pokażę jeszcze jak w AMODITcie się uruchamia taki serwer MCP jak jest uruchomiony to można się podpiąć w innym narzędziu, na przykład w Cursorze. I używać tych funkcji, które tu sama.

**Przemysław Sołdacki:** Wiesz co pytam, to jeszcze jak to jest logowanie zrobione uprawnienia.

**Mateusz Kisiel:** W tym momencie zrobiłem taką uproszczoną stronkę MCP Auth. I można sobie wygenerować token tej ważnej, powiedzmy 30 dni. No i po jego wygenerowaniu. Generuje się ten token i można skopiować sobie dane do Cursorze do do połączenia i to jakby loguje to jakby to jakby ten token jest ważny dla tego użytkownika, czyli tak samo jakbyśmy się logowali logowali tym użytkownikiem w AMODITcie, w którym obecnie jesteśmy zalogowani.

**Przemysław Sołdacki:** Ok.

**Mateusz Kisiel:** Czyli uprawnienia są dalej sprawdzane dla tego użytkownika i tak dalej.

**Damian Kaminski:** Czyli jak administrator to zrobi to jest pełne, a jak zrobi to zwykły użytkownik to nie dostanie informacji od treści procesów tak.

**Przemysław Sołdacki:** Ja to to.

**Mateusz Kisiel:** No tak. Tak tak, no jakby innej opcji nie ma.

**Przemysław Sołdacki:** Czyli użytkownik sobie sam musi najpierw wygenerować token, żeby móc korzystać z zewnętrznego MCP.

**Janusz Bossak:** No tak.

**Mateusz Kisiel:** Tak tak, no jakby innej opcji nie ma.

**Damian Kaminski:** Czy to nam może pomóc w testach?

**Janusz Bossak:** To tak.

**Mateusz Kisiel:** Mm.

**Przemysław Sołdacki:** Bo to zastanawiam się jak to zrobić, no bo ja jestem zalogowany do AMODITa i chciałbym żeby z moimi uprawnieniami się to dostało do innego systemu.

**Janusz Bossak:** No to trzeba wygenerować sobie token.

**Przemysław Sołdacki:** Ja się. Ale nie mogłoby się samo wygenerować. Na przykład chciałbym się podpiąć, żeby nie wiem. SharePoint nami ciągną dane.

**Janusz Bossak:** Nie. Może ktoś inny by chciał się za ciebie podpiąć?

**Przemysław Sołdacki:** No to absolutnie nie nigdy.

**Janusz Bossak:** No właśnie dlatego musisz wygenerować token, bo ty nie. No przynajmniej tak jest w każdym jakby systemie, bo jak robisz to Azure musisz tam wygenerować ten PAT personal access token i tak dalej. No to jest po prostu standard, tak w ten sposób się to systemy integruje. Yy i każdym serwerem tcp gdzie?

**Przemysław Sołdacki:** Ile jeszcze o tym standardem i o OAuth to ile wiem można robić, bo to jest przykład, że załóżmy chcę podpiąć się. Znaczy to jest używane i akurat analizowałam pod kątem BI załóżmy chce się logować do Power BI do AMODITa i żeby wyciągało dane te do których ja mam uprawnienia albo na przykład łączę się. Załóżmy z Teamsów albo nawet i chciałbym, żeby no ja jestem zalogowany do Teams, żeby po. Brało to co ja mam prawo pobrać za AMODIT w momencie jak na Teamsach agentowi powiem weź sprawdźmy w AMODITcie to, żeby on. Z moimi uprawnieniami to zrobił, no bo to, że ja co co 30 dni będę musiał się go z powrotem podpinać, to to w ogóle jest. No strasznie niewygodne.

**Damian Kaminski:** Ale czy ale to już jedziesz krok dalej? To chyba jest zdefiniowane z tego, co Mateusz pokazał. Tak, to jest propozycja 30.

**Mateusz Kisiel:** Czy moje dane 90 dni, ale tutaj tak nie jest docelowe? To jest na razie taka wersja wstępna w p do docelowo to będzie musiało być.

**Przemysław Sołdacki:** Nie no wiecie, jako jako jako prototyp to jest spoko, ale docelowo trzeba wymyślić no bo jestem zalogowany przez. Konto do osoby czy też Microsoftowe albo jestem w Active Directory, no i jakby żebym się nie musiał logować i podpinać systemy w jedną i w drugą stronę.

**Mateusz Kisiel:** Znaczy wydaje, wydaje mi się, że narzędzia takie jak Cursor czy Claude jakby w ogóle nie będą zwracały uwagę na to, że jesteśmy w Access do Active Directory i i nie będzie to miało dla nich żadnego znaczenia, jakby same te narzędzia nie przesyłają takiej informacji. Wydaje mi się.

**Przemysław Sołdacki:** Wiesz co? Sprawdź ten protokół i OAuth, bo wydaje mi się, że właśnie coś takiego jest.

**Mateusz Kisiel:** Znaczy no nie, no jakby to nie jest kwestia jakby. Claude albo albo Cursor wysyła jakiś request do naszego serwera i no po prostu nie przesyła informacji gdzie jesteśmy zalogowani i tak dalej te takich oni standard używają jeszcze inny tam jest. Promują taki dużo, bardziej skomplikowany standard OAuth 2.1 i. Co z tego, by trzeba bardziej skorzystać, ale to i tak nie byłoby takie takie logowanie jak mówisz.

**Przemysław Sołdacki:** Tak. Ale OAuth, yy no właśnie, bo OAuth jest używany, no jakby do wielu rzeczy jestem zalogowany tam nie wiem do Office'a w tej chwili to on używa OAuth z tego co się orientuje. Dobra, wiesz co to jest do do jakiś tam weryfikacji?

**Mateusz Kisiel:** No to jest, to jest ogólnie większy temat z tym logowaniem.

**Przemysław Sołdacki:** A kiedy ja będę mógł tego, rozumiem, że jak będzie jakaś tam kolejna wersja, będę mógł się potknąć, bo ja chcę tym Chatem GPT się podpiąć do AMODITa.

**Mateusz Kisiel:** Chatem GPT w sensie na stronie sobie wpisujesz do takich MCP ma dostęp i.

**Przemysław Sołdacki:** Tak, ale znaczy to wiem, że to nie działa na stronie, ale mam zainstalowane jeden wersję desktop. Yy GPT i ta i tam można dopinać swoje serwerem MCP i tam chętnie dopiero.

**Mateusz Kisiel:** No tak, no to. Tak to na przykładzie Cursora mogę pokazać jak to wygląda. Ty może dodać sobie New MCP Server i się wpisuje w w w. W mcp.json to coś tam skopiowało ze strony. No i można go teraz pytać o jakieś rzeczy. AMODIT na przykład jest. Zapytałem go, jakie są dostępne procesy, w AMODIT. Można spytać? Znaczy dokładnie ma dostęp do tych funkcji, do których ma naszych Copilot. A AMODITcie? Czyli tutaj jest lista tych funkcji? Mm. Może wyszukiwać jakieś artykuły z wiki?

**Przemysław Sołdacki:** Powiem ja chcę się podpiąć, bo na przykład wygenerowanie dokumentacji procesu czy w ogóle dokumentacji całego systemu bym zrobił w trakcie GP, to bym powiedział, weź wyszukaj wszystkie procesy z AMODITa i wygeneruj mnie dokumentację i on sobie po wyciąga jakby wtedy my nie musimy w Copilocie tego programować, bo GPlay to zrobi jeszcze uzupełnienie jakimiś danymi z internetu na przykład, bo sobie jeszcze coś tam poczytam, więc jakby wtedy my jakby.

**Mateusz Kisiel:** Pobrania. No tak.

**Przemysław Sołdacki:** No bo to duzi klienci to mówią, że oni oni nie będą tego Copilota naszego korzystać, bo oni mają swoich agentów i cię agenci będą robić im to, co oni chcą, tylko żeby się dało podpiąć do domu AMODITa. Więc, yy, to to to jest potrzebne?

**Mateusz Kisiel:** Tak to. To będzie to udostępniało.

**Przemysław Sołdacki:** To jest super.

**Mateusz Kisiel:** Miałem zapytać go, co się tutaj o coś czy.

**Przemysław Sołdacki:** No powiedz wygeneruj.

**Mateusz Kisiel:** Kończymy.

**Damian Kaminski:** Znaczy konkluzja, według mnie jest taka, że skoro. Wykorzystanie będzie tak jak mówi Przemek, to warto by się zastanowić. Pewnie noc sposobem licencjonowania tego, bo wtedy nie będziemy zarabiać na tokena. Ach, tak.

**Przemysław Sołdacki:** Znaczy, ale licencjonowanie jest takie, że mamy lice. AI Standard i Advanced i będzie wydaje mi się, że w ogóle generalnie MC to tylko w wersji Advanced, natomiast w Copilocie generowanie dokumentacji to powinno być w wersji Standard. Yy to.

**Damian Kaminski:** Mhm o k. To znaczy bardziej mi chodzi o ten MCP, bo jak rozumiem wtedy wszystko my tylko odpowiadamy, ale to nie korzysta faktycznie z.

**Przemysław Sołdacki:** Tak, ale klient płaci nam 100000 rocznie za to, że ma do tego dostępu i to jest o k.

**Damian Kaminski:** O k.

**Przemysław Sołdacki:** Nawet nawet Rossmann nawet, że tak powiem tu się nie zająknął, jeśli jak my im podaliśmy te ceny, więc wydaje mi się, że to jest o k. Wtedy tokeny sobie mogę go używać swoje nie ma problemu. No tomiast tutaj to jest jeszcze jeden aspekt to jest taki, ale to na inną dyskusję. Nie chcę tutaj tego drążyć, mianowicie my chcemy, żeby klienci płacili za wersję Standard, ale chcielibyśmy, żeby nasi pracownicy, nasi konsultanci, będąc u klienta, mogli korzystać z AI, mimo że klient nie ma jak. No bo on jest na przykład wygenerują sobie dokumentację. Zamiast pisać ręcznie albo osobie wygenerują proces, mimo że klient nie kupił tej licencji, to jest zastanowienia jak to zrobi, bo to byłoby przydatne. To jest korzystne dla nas.

**Damian Kaminski:** Może jakieś takie tokeny czasowe dla osób z odpowiednim adresem mailowym, gdzie mogło sobie go wygenerować po naszej stronie.

**Przemysław Sołdacki:** Że jeśli na przykład może jest, nie wiem, jeśli adres ktoś ma amodit.com albo astrafox.pl, to, że może sobie się podpiąć i sobie wygenerował.

**Damian Kaminski:** Ten token.

**Przemysław Sołdacki:** To jest jakby szeroki temat do zastanowienia, więc w ogóle takie przydałoby się spotkanie oddzielne o tym.

**Damian Kaminski:** To nie na to spotkanie.

**Mateusz Kisiel:** Spytałem o coś tam, zaczął pliki szukać w AMODITcie, bo to jest Cursor i Cursor ma jeszcze swoje funkcje do przeszukiwania plików. Mm. No ale teraz przytyłam do jednego folderu i będzie pewnie teraz używał tych funkcji swoich.

**Przemysław Sołdacki:** Wiecie to testowania. Rozumiem, że pierwsza wersja MCP jak będzie to będzie można się wyżywać na tym.

**Damian Kaminski:** Jeżeli chyba na tym bym podsumował, że no jak widać czas dyskusji, który na to poświęciliśmy i to, że cały czas coś powstaje. No to staramy się być na bieżąco ze wszystkimi możliwościami, AI owymi a i przeszedłbym dalej tak pewnie za 2 tygodnie znowu będziemy ja. Ich kolejny krok w ramach tej tej integracji z AI prezentować. Dobra, a dalej to tak Marek czy ty chcesz się czymś pochwalić?

**Marek Dziakowski:** Ile mnie tydzień nie było w kolejnym tygodniu, tu tutaj głównie.

**Damian Kaminski:** Mhm.

**Marek Dziakowski:** Yy, Trust Center zgłoszenia jakieś tam odpowiedzi był problem też z blockchainem. Zresztą poprawki były do tego i pod koniec zaczęłam się Multi OTP, ale jeszcze tutaj nie mam ze pokazania.

**Damian Kaminski:** O k. Łukasz Brodzki.

**Lukasz Brocki:** Yy, ja zajmowałem się 2 tematami. No plus jeszcze był problem z SimplySign, którym się zajmowałem. W pierwszym tygodniu zajmowałem się Comarch Hubem. To nie zdążyłem zrobić, bo no najpierw problem SimplySignem, a potem w poniedziałek miałem blok, na który dostałem odpowiedź dopiero w pierwszej połowie piątku, czyli no 3 dni temu, także no po prostu Comarch Hub przez blocker nie udało mi się zrobić, ale zrobiłem integrację z Global Express. Tutaj pokażę raczej dokumentacja, bo to jest najważniejsze dla potem wdrożenie owców one jeszcze nie przyszła internal testów jak przyjdzie internal. Testy jeszcze dodam obsługę licencji, bo najpierw chcę sprawdzić czy na pewno wszystko działa tak, że mamy przykład co jest potrzebne w rejestrze. Kompania jest go też później przygotuję, aby można było tylko zaimportować i będzie wszystko gotowe.

**Damian Kaminski:** Mhm.

**Lukasz Brocki:** No i to jest najbardziej rozbudowana funkcja, czyli otworzenie przesyłki. Ona ma wszystkie wymagane parametry. Nie dodałem na razie żadnych opcjonalnych jako taki MVP, jeżeli będą jakieś potrzebne, to będziemy oczywiście dalej rozwijać, no ich trochę jest, więc no nie chciałem marnować czasu na coś, co potem może się okazać nieprzydatne. Tak.

**Lukasz Bott:** Łukasz, Przepraszam, to ja dodam kontekst biznesowy, tak, no bo bo mówisz o integracja Comarch Global Express comarchu plis potrzebny dla i p. To są integralne oba oba dotyczą integracji. System Comarch. To jest alternatywa dla KSeFu naszego KSeF Connectora no klient się uparł, to Lewiatan bodajże tak uparł się, że nie nie chce korzystać z naszego KSeF Connectora tylko z rozwiązań Comarch owych, a to co teraz Łukasz pokazuje Global Expres to jest integracja z kolejną firmą kurierską na potrzeby wdrożenia w w PGL Lot. To tak pokrótce.

**Lukasz Brocki:** No i dla Global Expres mamy oczywiście oprócz dodawania przesyłki mamy wezwanie kuriera. Śledzenie i anulowanie przesyłki czyli no taka podstawowa obsługa pełna jest, no jeżeli będą potrzebne jakieś dodatkowe rzeczy, no to oczywiście będziemy je dodawać już na życzenie klienta. Ogólnie wszystko ja przynajmniej przy moich testach jeszcze będę czekał, aż testerki potwierdzą, że wszystko działa i no dodam licencję i będzie to gotowe do oddania.

**Lukasz Bott:** Łukasz, ja rozumiem, że mamy dostęp do jakiegoś środowiska takiego.

**Lukasz Brocki:** Tak jest środowisko, to są jeszcze gdzieś umieszczę na wiki, potem dokumentację, bo o nią musiałem się doprosić. Ona nie jest ogólnie dostępna jest w pliku Word, więc także pewnie tutaj do głównego. To tutaj do tego głównego grodu, tam jako załącznik ten plik, żeby był ogólnie dostępny dla wszystkich.

**Lukasz Bott:** Tak do do do łącz. Bardziej mi chodziło, że tutaj to co testuje, czy to jest środowisko testowe dostarczone przez Global Expres tak to jak się tam samochód.

**Lukasz Brocki:** Tak. Tak, zgadza się.

**Lukasz Bott:** Dobra.

**Przemysław Sołdacki:** Ja mam pytanko, bo to to co to pokazujecie to są jest wiki te nasze wewnętrzne.

**Lukasz Brocki:** Redmine jest naszym wewnętrznym wiki.

**Damian Kaminski:** Tak.

**Przemysław Sołdacki:** A czy tak to nie powinno być też na zewnętrznym czy?

**Lukasz Bott:** No będzie jeśli.

**Damian Kaminski:** W ogranie w innej formie tak, bo ale na pewno.

**Lukasz Bott:** Dodamy będzie.

**Przemysław Sołdacki:** Czyli ciepło. Także zacząłem zastanawiać, czy dałoby się zrobić, że tutaj jakimś Niemczech boxem zaznaczamy, że Ten artykuł ma iść na wiki, żeby on się sam tam wrzucał. No to wiki.

**Janusz Bossak:** Nie ma sensu.

**Lukasz Bott:** Wiesz co, Przemek? Nie podjęliśmy decyzję, że nie robimy tak, wolimy mieć kontrolę nad tym.

**Damian Kaminski:** Znaczy trzeba go zredagować na pewno w tej postaci takiej mocno technicznej nie ma to sensu na wiki globalnym, więc trzeba po prostu korzystać z znowu za AI i.

**Lukasz Bott:** Tak.

**Przemysław Sołdacki:** Czy mógłby nam to, że składać do kupy?

**Damian Kaminski:** Tak.

**Przemysław Sołdacki:** Dobra.

**Damian Kaminski:** Tak, już częściowo to wykorzystujemy chociażby w w o to może Łukasz przy okazji jak jesteś przy głosie, pochwal się tym Changelogiem, bo to może nie jest typowe działanie deweloperskie, ale już wiem, że udało ci się wyprodukować do tej najnowszej wersji chyba grudniowej. Tak, to może warto, żeby to globalnie zaprezentować.

**Lukasz Bott:** Doktor. Nie może doszli też i. To momencik. Łukasz brodowski, jeszcze coś tam ten masz?

**Lukasz Brocki:** Nie, to wszystko tak naprawdę, no temat SimpliSign no Comarch ERP, który był został zblokowany plus Global Express.

**Lukasz Bott:** Dzięki. Tak no to jeszcze dojdzie jeszcze jedno integrację w ramach Lotu jeszcze jedna integracja z firmą kurierską z UPSem tak, czyli niedługo będziemy obsługiwali wszystkich kurierów.

**Przemysław Sołdacki:** Wrzućcie mi to info, co my zaczęliśmy obsługiwać, bo to do cennika potrzebuje.

**Lukasz Bott:** No to wiesz co to na razie? Na razie ten nam klient musi to odebrać. Tak to jest w ramach wdrożenia, więc.

**Przemysław Sołdacki:** No ale ale tak czy inaczej, no jeśli to będzie jakąś wyceniane, no bo mamy 2 pozycje w cenniku, więc jeśli jakiś kolejny jest obsługiwany, no to to mi podajcie.

**Lukasz Bott:** Dobra, to Damian mnie wywołałeś tak no generalnie to też dzięki Damian towi tak no bo to rozpoczęli tam jakieś gdzieś procesy i ten i tobie januszowi tak, no gdzie się rozpoczęliście ten proces zbierania z z naszego. Z naszego właśnie tego.

**Damian Kaminski:** Azure'a.

**Lukasz Bott:** Azure tak czyli backloga tak czyni wszystkie zgłoszenia najróżniejsze nowości, nowości na podstawie właśnie. Danych stamtąd pochodzących i tutaj właśnie Damian tego produktu, który gdzieś tam przygotowałeś, tak ja go w sumie jeszcze potem gdzieś zmodyfikowała, troszkę automatycznie troszkę. No niestety jeszcze manualnie tak, ale generowany jest właśnie część. Krok na stronę wiki nie tylko do wersji grudniowej, bo też już do tej czerwcowej też aktualizowany był to samo metodą. Powstają 2 artykuły takiej podsumowuj. Kluczowe zmiany nowości zmiany to, co Przemek tam prosiłeś, żeby jeszcze jakieś obrazki do tego dorzucić, to się to, to postaram się to dorzucić, żeby to jakoś wizualnie. No i taki już. Jak już naprawdę ktoś będzie chciał, to to. To taki lista wszystkich zmian. Tak, oczywiście to jest jakoś tam przyrodę zredagowane przez. Tak, ale też w momencie wprowadzania, jak gdzieś tam też jeszcze tą. Przeglądam pod kątem takim, że tu gdzieś chociażby nie wiem, nazwy klientów się nie pojawiły tak chociaż prąd to względnie.

**Damian Kaminski:** No właśnie pod tym kątem, zwłaszcza nie nie chcemy tego automatyzować, bo mimo że działa LLM i możemy mu napisać odpowiednie prompty to to zawsze może się coś przekraść to nie chcielibyśmy żeby się prze kradło.

**Lukasz Bott:** Tak tu.

**Damian Kaminski:** Publicznej wiadomości.

**Lukasz Bott:** My też to jest właśnie te nazwy jak się tam klientów, ale też i gdzieś tu mamy to sekcję dotyczącą ch. Przejechałem bezpieczeństwa i w tej sekcji bezpieczeństwa tak też. Wydajemy albo enigmatyczne poprawki bezpieczeństwa, tak, albo po prostu. No akurat tutaj w tym Changelogu do wersji grudniowej to były napisane takie, żeby, że, że można było je. Podać tak więc. Bardzo chociażby to też muszę.

**Przemysław Sołdacki:** Bycie ja ja ja bym poszedł mocno w to, żeby to w promptach zrobić i może jeden prompt, który to generuje drugi, który później jeszcze sprawdza to pod różnymi względami czy tam coś nie przemknęło?

**Lukasz Bott:** Wiesz, co to to znaczy w tym pierwszym już jest uwzględnione, że to te właśnie kwestie. Takie właśnie wytyczne, reguły, czego co ma uwzględnić, czego nie uwzględniać.

**Przemysław Sołdacki:** Tak, ale jeśli chcesz mieć pewność, że ręcznie sprawdzać, no to można jeszcze drugim punktem kazać mu, co jeszcze raz ma sprawdzić się coś nie przemknęło. Wiecie, bo jakby z tymi LLMami używamy coraz mocniej. Na przykład w tej chwili LLM decyduje, czy zajmiemy się danym klientem. Czy w ogóle chcemy obsługiwać danego klienta i czy chcemy do danego postępowania ofertowego podejść? Jest to może, że tak powiem przeniesienie dużej odpowiedzialności, ale ale to jest robione przy użyciu LLMa lepiej niż było robione ręcznie przez handlowców, więc jakby tutaj też jakby zachęcam do tego, żeby jak najwięcej przenieść na LLMa.

**Lukasz Bott:** No tak no.

**Damian Kaminski:** Co do zasady tak jest to zrobione tak każda poprawka nasza, która uzyskuje status Done jest wydawana to tak, jak tu widzicie, jest reprezentowana numerem tym naszym wewnętrznym. To jest na potrzeby wykorzystania przez serwisantów, jaki krótkim zdaniem opisowym czego to dotyczy?

**Lukasz Bott:** Tak to.

**Damian Kaminski:** I tutaj akurat to co Łukasz prezentuje, to jest taka pierwsze wydanie tej wersji grudniowej, czyli tak jak widzimy Zero. Natomiast jeśli mamy, jeślibyś Łukasz pokazał wersję czerwcową. No to tam mamy do każdego tego sub wydania tak, czyli tej końcówki naszego hot fixa tam 120 123 to mamy informacje właśnie, co w ramach tego wyszło. No i to zwłaszcza jest odpowiedź na potrzeby dużych klientów, którzy bardzo często czy od drążenia owców czy od serwisantów oczekują, że jeśli podnoszą ze 100 do 104, to co w tym okresie się faktycznie zmieniło, więc to to po prostu automatyzuje, usprawnia przekazywanie. Tych informacji.

**Lukasz Bott:** To to to, co tutaj warto podkreślić, także to właśnie wykorzystanie tych narzędzi LLM, tak, no przede wszystkim usprawniło wygenerowanie tej listy tak fakt, że jeszcze pewne rzeczy tutaj troszkę manualnie tam robimy tak, no, ale chociażby ze względu, żeby mieć nad tym jeszcze jakoś kontrolę, tak co tam. Nie wiem, co to, co to ustrojstwo wygenerowało, tak. Żeby nie poszły jakiś. No głupota, głupota.

**Damian Kaminski:** Dobra, zostało nam ostatnie 5 minut jeszcze jest Przemek, chyba który się nie wypowiadał i chyba o nikim nie zapomnieliśmy z deweloperów, więc nie wiem Przemku czy ty jeszcze chcesz, wiem, że tam działałeś raportami.

**Kamil Dubaniowski:** Przemka i Filipa jesz?

**Damian Kaminski:** O k Filip tam trochę proszę.

**Przemysław Rogaś:** No ja działałem z błędami w w module raportowym, no i tam miałem trochę zadań z edytora formularza. No ale to takie jakieś zmiany poglądowe nieduże.

**Kamil Dubaniowski:** Myślę, że najistotniejsze Przemek jakbyś pokazał dodawanie nowej sekcji, bo to jest taka znaczy, to jest w ogóle nowość. Nie było tego w edytorze grafiki, znaczy o k stary nie było na liście, nie było było w edytorze graficznym, ale nieco inaczej, żeby też konsultanci, jak tam Daniel i Mateusz będą to oglądali. Żeby zobaczyli o co chodzi. Wcześniej to dodawanie sekcji było na samym dole ekranu, czyli powiedzmy, że w przy dużych formularzach mogło być to ręcznie nieintuicyjne, zwłaszcza dla serwisu, który wchodzi na gotowe i mają już tu w sekcję i pola, więc dodanie nowej sekcji gdzieś tam na samym dole ekranu, powiedzmy, że było mniej intuicyjne i nie kontekstowe, bo sekcja dodawała się na samym dole i trzeba było ją później przeciągnąć, ewentualnie w miejsce, gdzie faktycznie ma być.

**Przemysław Rogaś:** No to.

**Kamil Dubaniowski:** Tutaj możemy tak jak dodajemy pola, możemy dodać po prostu sekcję już w tym miejscu, w którym jej potrzebujemy i i i ujednolicić. Chcieliśmy to natomiast zmian było dużo, bo zgłoszeń było tam, powiedzmy takich mniejszych. Myślę, że więcej niż 15, ale to są zgłoszenia typu, na przykład ten formularz na Górze nawigacja się zmieniła. Mamy teraz to jako TriSelect. Wcześniej było to tak, że powtarzaliśmy całą ścieżkę, czyli był formularz główny jako pierwsza opcja. Druga opcja to był formularz główny, strzałka w prawo, tabela. Zarobiliśmy teraz TriSelect, żeby to też lepiej prezentować. Zmieniła się lokalizacja prawego panelu, czyli jest już przeniesiony poziom niżej, żeby tabelka nawigacji z wyszukiwaniem nam nie skakała. Nie zawyżała się co chwilę. Zmieniła się też zmienił się nagłówek prawego panelu. Jeśli klikniemy na jakieś pole, to teraz wyświetla się tam. Już informacja na temat nazwy tego pola, a nie typu tego pola, jest też ikona. Ten nagłówek został zamrożony, czyli nie ucieka nam podczas skalowania takie tak jak cały czas właściwie już dopracowujemy tylko i co sprint właściwie wydaje mi się, że im więcej to będzie używane, tym więcej będzie takich poprawek już na konkretne zgłoszenia. Ee natomiast już jesteśmy. Myślę, że blisko docelowego, że kto? W tym sprincie będziemy to, co Przemek podnosił coś próbowali wyróżnieniem jeszcze bardziej tego prawego panelu podziałać z kolorami. Już coś próbowałem nawet w zeszłym tygodniu, ale jeszcze bez jakiś tam efektów, które pokazać, bo podoba mi się to to, co AI tam wyprodukował. Yy. No mnóstwo tych zgłoszeń było tutaj ikonki w wyszukiwaniu w ogóle to wyszukiwanie przynieśliśmy. Na prawo doszło, wyszukiwanie po ujdzie pola w tych dodatkowych ustawieniach wyszukiwania. W tej wyszukiwarce pojawiają się ikony i już poszliśmy za ciosem i one też są w kolorach, tak jak w tym lewym panelu, żeby to wszystko było spójne, więc takie takie raczej nie ma sobie robimy. Ok i Filip jakbyś mógł jeszcze pokazać tą listę na szybko, bo jeszcze mamy 2 minuty.

**Filip Liwiński:** Dobra.

**Kamil Dubaniowski:** No tutaj dużo jakby się działo po pierwsze to co teraz tak jest dosyć mały krajem o k.

**Damian Kaminski:** Troszkę powiększy bo słabo to widać.

**Kamil Dubaniowski:** Yy tak tutaj, podobnie jak w tym edytorze graficznym obsłużyliśmy już dodawanie pól i dodawanie sekcji. Ona jest kontekstowe, czyli mamy ten przycisk po lewej stronie, trochę na wzór naszego widoku backlogu zrobiliśmy to, czyli po lewej jest przycisk plusik na poziomie sekcji. Mamy do wyboru opcje dodania nowej sekcji lub pola do tej sekcji, natomiast pola dodaje się też kontekstowo i tutaj jak najedziemy na przykład z tym miejscu, no ten plusik, no to ta linia nam sugeruje, że w tym miejscu pod spodem jeszcze turfy dodamy po prostu doda się nowe pole, po kliknięciu wyskakuje już okno do wprowadzenia nazwy był typu pola, ale dodajemy to już kontekstowo, czyli w miejscu gdzie nam to pole jest potrzebne, a nie tak jak było w starym widoku listy gdzieś tam w nagłówku czy było podać nazwę pole, wybrać jego typ kliknąć Dodaj. Nią się dodawał. Na samym dole sekcji i wtedy była kolejna robota, żeby teraz jeszcze odpowiednio sobie w tym miejscu, w którym potrzebuję, to pole ustawić. Natomiast tutaj już dodajemy kontekstowo. Pojawiły się te ikony też, żeby tutaj troszeczkę graficznie to wyglądało lepiej, bo konsultanci narzekali, że bardzo czarno biało się tu zrobiło i ciężko to czytać. Zmienił się sposób wyboru typu kolumn, w sekcji do Przemek zgłosił chyba na ostatni region, żeby uspójnić do tego, jak to się robi. To, że graficznym? I nie wiem czy a jeszcze widzę, że tabela jest rozwijana.

**Damian Kaminski:** Życie pokazać jak to działa te kolumny, a to jest po prostu wybór o k. Dobra, dobra, tu się nic nie dzieje z tej strony o k.

**Kamil Dubaniowski:** Przestawiasz po prostu tak tak jak w edytorze graficznym. A i na cholerę chyba z tego co kojarzę wszystkie teksty teraz mają ramkę, bo wcześniej było widać, że to w ogóle można edytować online, czyli teraz pojawia się ta ramka, co sugeruje, że można kliknąć i inne na przykład edytować nazwę wyświetlaną ta funkcjonalność była tylko graficznie jakby nie było jasna, że tak się da. Yy. Ktoś jeszcze takiego większego kojarzysz? Filip, dodaliśmy to w poszukiwanie jako wspólny komponent, żeby zdradzić choreograficznego i listy. No było to samo po prostu, czyli zmiany Przemka też będą wpływały na zmiany Filipa, tak samo ten prawy panel został zrobiony jako jeden komponent, żeby też.

**Filip Liwiński:** Tylko tej konki.

**Kamil Dubaniowski:** Ee jakby zachować tutaj.

**Przemysław Sołdacki:** Mam pytanko, bo pamiętam, że to mają być te wersje językowe to tak rozumiem dalej jest to możliwość.

**Kamil Dubaniowski:** Tak, mamy tutaj na Górze ten przycisk do włączenia colum, które pokazują ci poszczególne języki i wartości jak aktualnie dla nich masz przypisane? Jeśli nie masz przypisanej żadnej wartości i ta wartość jest dziedziczona z ustawienia systemowego z nazwy systemowej, to widzisz to tak bardziej na szaro. Natomiast jak już nadasz sobie jakąś nazwę taką indywidualną dla języka polskiego, no to ten tekst jest już po prostu taki wyróżniony. No ciemniejszym kolorem, a jeśli nie masz ustawionych no to pokazujemy jaka wartość jest aktualnie dziedziczona. Coś Filip, chciałem jeszcze powiedzieć, a ja ci przerwałem.

**Filip Liwiński:** Jeszcze tej konki to był plus i minus to te strzałki.

**Kamil Dubaniowski:** A tak tak u spóźniamy też u spóźniamy i w tym sprincie chciałbym też taki cel, właściwość pisałem żebyśmy wypracowali jeden przynajmniej dla tabel.

**Barbara Michalek:** A jeszcze chyba reguły właśnie było to.

**Filip Liwiński:** I jeszcze ten ikonka znaczy przycisk reguł.

**Kamil Dubaniowski:** Reguła tabeli też doszła to też dla Mateusza i Daniela. Istotne, żeby to w dziale przekazali. No bo wygląda to zupełnie inaczej niż było wcześniej. Wchodziło się do tabeli i tam był w górnym w górnej belce przycisk do włączenia reguł tej tabeli. Natomiast teraz po prostu trzeba znaleźć tabelę na liście. Jedną z akcji włączenie reguł tej tabeli i docelowo planujemy, żeby ten przycisk był na każdym polu. Natomiast, żeby on odnosił kontekstowo do reguł powiązanych z tym polem. Razie mamy obsługę dla tabel tak jak było, natomiast rozwojowo planujemy, żeby to był Odnośnik taki do już przefiltrowanej listy reguł pokazujących tylko reguły powiązane z tym polem, z którego to w sobie wywołałem.

**Janusz Bossak:** A na tym edytorze graficznym też to jest?

**Kamil Dubaniowski:** Yy ta do reguł tabeli jeszcze nie.

**Janusz Bossak:** Jeszcze nie no tak mi się wydawało.

**Kamil Dubaniowski:** Jeszcze nie to będzie w prawym panelu tak, no bo tutaj nie używamy przycisków przy nazwach, więc to będzie też przeniesione do prawego panelu i to też mam na liście wpisane.

**Janusz Bossak:** O k.

**Kamil Dubaniowski:** Ten prawy panel też będzie właściwy podejmowany w tym sprincie. To musimy jeszcze kilkaset czy pewnie obgadać? Co do lokalizacji tych przycisków pozostałych usuń zmień typ pola to wszystko ja gdzieś tam na to Plan mam, ale wolałbym to potwierdzić z wami na projekcie.

**Przemysław Sołdacki:** Poziomu listy będzie można panelu rozwinąć.

**Kamil Dubaniowski:** Jest już teraz tutaj ustawienia sobie klikniesz i to jest ten sam panel, tylko jeszcze widzę, że tutaj nie było chyba zmian Przemka wrzucanych, bo nie ma jeszcze tego nagłówka z tż, że wydać jako wspólną wersję.

**Filip Liwiński:** Tak.

**Przemysław Sołdacki:** W sumie w reakcje, skoro jakby w innym miejscu trzeba drugi raz robić nie nie da się także jakby ten sam kawałek kodu działa i tu i tu.

**Kamil Dubaniowski:** Znaczy no bo takie pracują na osobnych. To to tak jest, tak jest tylko, że Przemek nie pewnie jeszcze nie nie nie publikował do wersji, którą Filip.

**Przemysław Sołdacki:** A jasne. Rozumiem.

**Janusz Bossak:** No dobrze.

**Filip Liwiński:** No dobrze.

**Janusz Bossak:** Bardzo ładnie to zaczyna wyglądać. Myślę, że koledzy wdrożeniowe polubią te listę pól i i polubią ten edytor graficzny. I raczej nie będą się już cofali do starej wersji. Bo już był.

**Kamil Dubaniowski:** Nie ma takiej możliwości technicznej.

**Janusz Bossak:** No już widać, że jest to lepiej po prostu tej chwili fajnie. To jeszcze mamy. Dobra, bardzo wam dziękuję. Naprawdę fajnie przygotowana dzisiejsza tam Sprint Review. Ładny prezentację, widać, że idziemy zgodnie z założeniami. Ciśniemy mocno teraz tą tą. Pozyton ium i te elementy do joty RWA, no bo to musimy tym sprzęcie jak wiecie wydać. Także dzięki za solidną robotę i miłego dnia widzimy się po południu na planowaniu.

**Damian Kaminski:** Dzięki cześć.

**Marek Dziakowski:** Mojego dnia cześć.

**Filip Liwiński:** Dzięki cześć.

**Adrian Kotowski:** Dzięki cześć.

**Mariusz Piotrzkowski:** Część.

**Oktawia Ostrowska:** Dzięki cześć.

**Mateusz Kisiel:** Czy?

**Janusz Bossak:** Wejść.

**Janusz Bossak:** Zatrzymano transkrypcję.

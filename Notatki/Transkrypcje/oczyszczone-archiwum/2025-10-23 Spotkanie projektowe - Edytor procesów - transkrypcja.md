**Data spotkania:** 23 października 2025, 10:34

---

**Przemysław Rogaś:** Jeśli chodzi o zmiany w edytorze formularza, to były głównie tylko ustawienia. Nic szczególnego, żadnych dużych zmian. Zostało dodane przesuwanie sekcji z takich funkcjonalności, ale tak to raczej nic ciekawego.

**Przemysław Sołdacki:** A edytor diagramów był robiony?

**Przemysław Rogaś:** Tak jak zostało zrobione, zostało oddane na testy i już nic nie było ruszane.

**Przemysław Sołdacki:** A edytor reguł jakoś był ruszany czy nie?

**Przemysław Rogaś:** To jest już skończony projekt na ten moment.

**Przemysław Sołdacki:** Damian to robił, nie ma teraz Damiana. Rozumiem, że odpowiedź jest taka, że nie zaczęliśmy tego implementować. Więc pytanie – co dalej, co jest w planach? Już się wypowiedziałem. Kamil, Janusz?

**Kamil Dubaniowski:** Co jeśli chodzi o diagram? Spodziewam się, że ten prawy panel teraz trzeba by ruszyć, bo robimy już MVP 2.

**Przemysław Sołdacki:** Ta wersja, która jest teraz, rozumiem będzie już grudniowa? Pracujemy nad grudniową?

**Kamil Dubaniowski:** Tak, to jest jak MVP 1, czyli właściwie odtwarzamy tę funkcjonalność, żeby dało się zbudować diagram.

**Przemysław Sołdacki:** Ale te MVP 1 w sensie nowy diagram w ogóle nie poszedł do tej już wydanej wersji?

**Kamil Dubaniowski:** Do czerwcowej, do czerwcowej.

**Przemysław Sołdacki:** Dobra. No to w porządku. Róbmy już tę grudniową, którą wydamy na koniec roku. Czyli teraz te MVP 2 – rozumiem prawy panel do diagramu?

**Kamil Dubaniowski:** Prawy panel dobiera ustawienia etapów. To co mamy na liście etapów. Spodziewam się, że ta lista etapów też będzie musiała się pojawić – ta, co była do tej pory, czyli nie taka litograficzna, a widok listy.

**Przemysław Sołdacki:** Jako zakładka?

**Kamil Dubaniowski:** Jako zakładka kolejna. To bym pewnie ująłem w MVP 2. Dalej jak to łączyć z regułami i cała reszta – co dyskutowaliśmy – to myślę, że to już na dalszy etap, bo raczej do tej marcowej już tego nie dobijemy. Zobaczymy jak będzie czas, to tak, jak nie – to nie.

**Przemysław Sołdacki:** Czy mamy projekt do tego prawego panelu?

**Kamil Dubaniowski:** Nie mam.

**Przemysław Sołdacki:** No to trzeba by go zrobić, żeby mogło pójść do implementacji. Myślę, że tak powiem, nie przypalałbym czasu. Kto to będzie robił?

**Kamil Dubaniowski:** Pewnie ja, ten diagram opiekowałem się w jakimś zakresie, więc ten prawy panel też. Lista pewnie będzie dużo szybsza do zrobienia, bo działamy na tym samym schemacie cały czas list. Pewnie to pójdzie się szybciej.

**Przemysław Sołdacki:** Prawy panel będzie w zasadzie zawierał to samo co pozycja na liście, tutaj chyba jakiejś filozofii nie ma.

**Kamil Dubaniowski:** Tak, tak. Czy o tyle ten prawy panel – to jest właśnie ta filozofia, że ten prawy panel tutaj powinien być docelowo bardziej złożony i żebyśmy tu koncepcji nie zgubili. Tam miały być też właśnie reguły, miały być ustawienia samego etapu, ale miały być też te wymagania, które projektował jeszcze Janusz. Więc ten prawy panel będzie trochę inny niż pozostałe.

**Przemysław Sołdacki:** Te wymagania to w jakimś tam kolejnym MVP, bo ta koncepcja nie jest tak dopracowana. Jest na to pomysł, ale trzeba zweryfikować, czy to w ogóle jest potrzebne konsultantom. Sobie o tym rozmawialiśmy, ale nie było takiego zderzenia z działem wdrożeń czy serwisu, zwłaszcza wdrożeń – czy oni rzeczywiście tak pracują? Bo może oni pracują w zupełnie innych narzędziach, często dostarczanych przez klienta i w ogóle nie będą chcieli tego robić.

**Kamil Dubaniowski:** Ja myślę, że powinniśmy iść w tę kierunkowość, bo w większości przypadków to jest Word, Excel, który później ginie i przychodzi serwis i nic nie wie.

**Przemysław Sołdacki:** Może być też tak, że my po prostu wrzucamy Word i Excel do ustawień procesu jako dokumentacja procesu. To jest proste do zrobienia. Ewentualnie jest tak, że wrzucamy pliki, a AI nam rozpisuje to na punkty. Ale ta koncepcja jest jeszcze nie wypracowana. Więc najpierw zróbmy odtworzenie tego, co mamy i tego, co jest łatwo dostępne, tak by bez zmiany trybu pracy – żeby ten edytor formularzy, zakładam, że on już jest kompletny. Nie wiem, czy tam coś jeszcze by się dało dodać, może będzie.

**Kamil Dubaniowski:** Jeszcze wychodzą jakieś elementy, gdzieś coś zgubiliśmy. Ja staram się też usprawnić coś, czego nie było – chociażby zarządzanie kolejnością sekcji. Nie dało się tego robić w starym edytorze. To właśnie takie niuanse zgłaszam jeszcze na ten moment. Ale na głównych klockach to już jest w miarę gotowe.

**Przemysław Sołdacki:** Musimy doprowadzić to do końca nie wymyślając nowych rzeczy. Czyli robimy najpierw, że jest w pełni zrobiony edytor formularzy, edytor diagramu i edytor reguł. A wtedy będziemy mogli robić te rzeczy, które też są teoretycznie łatwe, bo mamy powiązanie reguł z etapami, z polami. Więc moglibyśmy na diagramie wyświetlać powiązane reguły, na formularzu też powiązane reguły. W drugą stronę – klikam regułę, to mogę zobaczyć jakich pól ona dotyczy. Bo to i tak gdzieś tam w bazie jest. Ale to też jest już kolejny etap, bo to jest w sumie coś nowego, czego nie ma w tej chwili.

**Janusz Bossak:** Ja proponuję, żebyśmy zrobili pewną weryfikację naszych założeń i hipotez, które mieliśmy rok temu. Czy to rzeczywiście w tak znacznym stopniu pomaga konsultantom? Na razie odbiór tego edytora jest taki średni bym powiedział – niekoniecznie im to przyspiesza. Inny warunek – wygląda to ładnie i prezentuje się lepiej. Ale to są różne głosy na ten temat. Więc ja bym proponował zrobić pewną weryfikację tych naszych założeń i hipotez. Przejść przez to jeszcze raz i określić, co rzeczywiście musimy zrobić. Na przykład z punktu widzenia handlowego, żeby to w miarę wyglądało nowocześnie, ale też żeby nie przepalać godzin niepotrzebnych. Róbmy takie rzeczy, które Mateusz, Ida i Daniel uznają za wartościowe.

**Kamil Dubaniowski:** Jestem też na świeżo po spotkaniu z Agrestem. Oni są bardzo dobrze nastawieni do nowego wyglądu AMODIT i miałem z nimi tą prezentację – też pozytywnie odbierali. Ale mimo wszystko dzisiaj na końcu padło, że mają ładniejsze aplikacje od AMODIT. Ale co z tego, jak są powolne, irytujące w użytku? Dla nich kluczowa jest wydajność. Powiedzieli, że mógłby być brzydszy, ale żeby był szybszy.

**Janusz Bossak:** No właśnie.

**Przemysław Sołdacki:** Ja bym chciał osiągnąć taki efekt, że wasza komunikacja jako działu R&D była bardzo silna z działem wdrożeń, działem serwisu. Żebyście tam się ustalili założenia do roadmapy i zaproponowali roadmapę na przyszły rok.

**Janusz Bossak:** No i to chcemy naprawiać. Dokładnie.

**Przemysław Sołdacki:** Pamiętam z Danielem rozmawiałem, to on pytanie, czy może być ta lista pól najpierw, a dopiero później graficzny edytor – że mu się najpierw odpalało to. Możemy po prostu zapamiętać per użytkownik, co tam ostatnio on miał włączone. Zgadzam się, że może być tak, że mamy super pomysły, że to będzie ładniej i chyba lepiej, a się okazuje, że to w ogóle nikt tego nie potrzebuje. Więc ja wolę ściąć wymagania i dać mniej tych wymagań i zrobić te rzeczy, które naprawdę robią różnicę. Bo kluczowe kierunki do roadmapy biznesowo to są dwa: zwiększenia atrakcyjności, żeby łatwiej sprzedać system – i to nawet niekoniecznie przez nową funkcjonalność, tylko to, że to, co jest, jest lepiej robione. A druga rzecz, że realnie skraca wdrożenia i ułatwia serwisowanie. Więc być może część naszych pomysłów nie pomaga w żadnej z tych rzeczy.

**Janusz Bossak:** Tego mówię – to wymaga rewizji naszych założeń, które mieliśmy.

**Przemysław Sołdacki:** Właściwie Janusz, jak to będzie zrobione?

**Janusz Bossak:** Jeżeli chcemy, najpierw uruchomić regularne spotkania tutaj właśnie, tak jak mówiłeś, z Mateuszem i z Danielem. Przegadać te rzeczy, które już są zrobione. I określić, które z tych, które planowaliśmy do tej pory, są dla nich najważniejsze. A może są inne, które oni uważają, że im się bardziej przydadzą. Mamy też zaległości trochę – mamy zaległość związaną z tym eksport-import procesów. Akurat Piotr teraz coś tam robił w tym zakresie. Opóźnienia mamy nowe we wszystkich właściwie tych założeniach. A do tego mamy końcówkę roku i WIM, więc jeszcze mamy tematy – repozytorium do zrobienia dla WIM, repozytorium do zrobienia dla Lotu. Więc mam parę rzeczy tutaj. Naprawdę trzeba zrobić głęboką rewizję tego.

**Przemysław Sołdacki:** Jestem zwolennikiem tego, że możemy nawet całkowicie zatrzymać roadmapę naszą. Bo jeśli chodzi o priorytety, powinniśmy najpierw domknąć to, co jest do domknięcia, czyli WIM i być może jakiegoś innego klienta. Teraz powinniśmy nie wiem – mieć sprint taki, że zamykamy WIM i to byłby cel sprintu. Robimy wszystko i większość zespołu, żeby się zajęła tym, żeby ten WIM skończyć. Chyba że nie wszystko da się zrównoleglić, więc pewnie nie ma sensu, żeby cały dział tylko się zajmował WIM.

**Damian Kaminski:** Od razu powiem – nie da się tak. Janusz chciał za portami w zasadzie zatrzymaliśmy wszystko dla dwóch osób. Okazało się, że po dwóch dniach skończyliśmy to niestety wszystko.

**Przemysław Sołdacki:** To jest super, że skończyliśmy. Słuchaj, ja bym tak chciał, że i mamy sprint i mówicie pięć rzeczy skończyliśmy, albo nawet jedną rzecz, ale skończyliśmy – super. Przed czasem – to tak ja wolę to niż mieć rozgrzebane tam nie wiem dziesięć czy dwadzieścia tematów i ktoś tam podciąga czy z drugiej strony. Bo takie mówię priorytety – domknąć wdrożenia, bo proszę, bo mamy wystawić faktury, zamknąć projekty. Dopóki tego nie mamy, to nie mamy pieniędzy z tego projektu i nie możemy klientowi nic nowego sprzedać, bo mówię: "A przecież projekt robicie". To co wy chcecie nowego? Więc to jest ważne. Na drugim miejscu jest to, żeby ustalić – ja szczerze mówiąc, ja cały czas czekam, żebyście mi przedstawili propozycje roadmapy przedyskutowanej z działem wdrożeń, działem serwisu.

**Janusz Bossak:** No tak, no to uzgodniliśmy, że tak będziemy robić. Teraz były te warsztaty dodatkowe.

**Przemysław Sołdacki:** Tylko pytanie – kiedy ja to dostanę?

**Janusz Bossak:** W przyszłym tygodniu myślę, że będziemy się w tym temacie już spotykać.

**Damian Kaminski:** My spisaliśmy wszystkie potrzeby, które widzimy i teraz – czyli po naszej stronie związane z tymi wdrożeniami, które wiemy – i ogólnie wszystkimi, powiedzmy, kwestiami, które wymagają zaopiekowania. Do tego do tej listy trzeba jeszcze dopisać to, co właśnie wymasz potrzebne jest serwisowi i wdrożeniom – ogólnie potrzebne, nie to, że na już, tylko ogólnie. No i potem zrobić ostatni element ćwiczenia, czyli wszystkiemu nadać priorytety.

**Przemysław Sołdacki:** Dostaliście te pliki, które przygotował Mateusz i Daniel?

**Damian Kaminski:** Tak.

**Przemysław Sołdacki:** O k.

**Damian Kaminski:** Już częściowo się do nich też odnieśliśmy. Po prostu teraz musimy z nimi wspólnie na wspólnej roadmapie – bo to jest nie tak, że my każdy ma swoją – tylko na wspólnym kierunku rozwoju ustawić, co jest ważniejsze od czego.

**Przemysław Sołdacki:** Dokładnie, bo tak to powinno być zrobione – wy sobie dyskutujecie, tam robicie propozycje roadmapę i wtedy ja ją oglądam. Trzeba uwzględnić oprócz tego, że właśnie wsparcie serwisu i wdrożeń, żeby szybciej im się pracowało, to trzeba tam uwzględnić, jakie rzeczy chcemy zrobić, żeby się jeszcze lepiej sprzedawało. Bo lepiej się będzie sprzedawało jak będą w pełni działające rzeczy – tam domykanie nie wiem moduł raportowy, że działa w pełni i że wygląd jest już ten taki współczesny. No to to się dzieje tak, ale to też jest jakiś tam element. Więc chciałbym dostać propozycję roadmapy i będziemy dyskutować, czy ja tam na jakieś uwagi mam czy nie mam, ale najpierw trzeba zacząć od tego, że wypracujecie to sobie tą mapę. Tylko to trzeba dosyć szybko zrobić. Ja tutaj też pytam Natalię o coś, a Natalia mówi: "No ale dobra, ale jaka jest roadmapa?" Ja mówię: "No to jeszcze ja roadmapy nie widziałem, bo nie dostałem tej propozycji". Więc nie chcę, żeby tak jedni na drugich czekali. Ja na pewno bym chciał po prostu dostać od was propozycję, że nie wiem – Daniel i Mateusz się powiedzieli, że taka roadmapa ma dla nich sens, ta kolejność robienia i priorytety są z nimi potwierdzone. Jeśli będzie wybór, czy na przykład poprawiać wygląd, czy robić coś dla serwisu, to wtedy będziemy to dyskutować. To już ze mną bardziej. Czy bardziej wspierać wdrożenia, czy bardziej wspierać sprzedaż. To będzie tego typu dyskusja. Każda rzecz może wspierać albo sprzedaż, albo wspierać wdrożenie. Więc coś trzeba wybrać. Więc prośba od was o propozycję. Po pierwsze rewizja tego, co w ogóle jest na roadmapie, co nam się udało lub uda w tym roku, a co się nie uda. No i później ustalenie priorytetów. Bo może rzeczy, które mamy na roadmapie, to stwierdzimy, że jednak nie robimy. Kiedy jesteście w stanie realnie to przygotować?

**Damian Kaminski:** Może? Proponuję, że jesteśmy w stanie dzisiaj odpowiedzieć, natomiast musimy zsynchronizować kalendarza, w sensie trzeba.

**Przemysław Sołdacki:** Stójcie tak, żebym wiedział konkretnie, kiedy to będzie. Że tam nie wiem, że tam wkrótce – tylko, że wiem, że wtedy i wtedy już powinno to być gotowe. To też zmobilizuje tutaj osoby, to zaangażowane, żeby po prostu to zrobić. To trzeba siąść, przedyskutować, wybrać rzeczy, bo to jest tak, że my nie musimy całej rozmowy mieć jakoś super ułożonej. Tylko musimy wiedzieć, co w tym momencie – jakbyśmy mieli wybrać, nie wiem, każda załóżmy wdrożenia jak mają wybrać tylko trzy rzeczy, serwis jak ma wybrać tylko trzy rzeczy i jakieś pro sprzedażowe trzy rzeczy – to co to będzie? Cała reszta jest nieważna, ale te najważniejsze, które zrobią nam różnicę – to jakie to rzeczy?

**Janusz Bossak:** To też wynika z tego z tych naszych rozmów. Najpierw strategia taka naprawdę sensowną, uzgodniona też z wami. Bo są wiesz, albo rzucamy siły na to, żeby robić – bo też są takie głosy – wersje dla małych czy mniejszych firm rzędu sto plus. I robisz demo i szablony pod to, tak standardowe, żeby szybko się wdrażało. Albo idziemy w kierunku Enterprise firm – coś innego. Albo idziemy w tą i w tą stronę. Więc to są decyzje powiedział na poziomie, na razie strategicznym, które po tych warsztatach widzimy, że trzeba podjąć.

**Przemysław Sołdacki:** Tylko na ile ta decyzja o tą konkretną rzecz – co pytasz – na ile to wpływa na roadmapę?

**Janusz Bossak:** No wpływa, no bo albo będziemy realizować jakieś zadania, których nawet na tej roadmapie nie ma, a będą potrzebne do tego, żeby móc sprzedawać mniejsze rozwiązania szybciej, taniej i łatwiej.

**Przemysław Sołdacki:** Ale czy jesteś w stanie podać przykład co by to było?

**Janusz Bossak:** Albo nie będzie tylko...

**Damian Kaminski:** Obydwaj macie rację. Powiedziałbym tak, że to, co mówi Janusz, to jest kierunek rozwojowy taki ogólny, w sensie w kierunku jakich produktów my chcemy iść, co chcemy usprawniać. A to, co mówi Przemek – czuję, że bardziej dotyka bieżących wdrożeń i usprawnień pracy wewnętrznej. Czyli jak lepiej obsługiwać po prostu regułę, jak lepiej obsługiwać formularz dla naszych konsultantów.

**Janusz Bossak:** No tak, tak, tak, tak.

**Przemysław Sołdacki:** Janusz, o co mi chodzi, że te kierunki – tak jak mówię, skrócenie czasu wdrożeń sam zaproponowałeś, że celem jest skrócenie wdrożenie o 30%, co by nam się przekładało na 2 miliony rocznie. Albo co najmniej 1,5 miliona rocznie oszczędności. Więc to jest ważne co – pytanie, co trzeba zrobić, żeby te 30% szybciej się wdrażało? To jest jedna rzecz. Natomiast ja nie czuję gdzie tutaj decyzja odnośnie wielkości docelowego klienta wpływa na naszą roadmapę.

**Janusz Bossak:** Ja też jeszcze nie wiem. No to trzeba zbadać.

**Przemysław Sołdacki:** Bo wiesz, bo ja nie chcę się zastanawiać nad decyzją, która nie ma żadnego znaczenia. Bo z tego, co rozmawialiśmy już tam w szerszym gronie, że takie rzeczy jak szablony procesów to ma robić dział wdrożeń – oni wdrażają, to sobie zrobią szablony. Najwyżej wgramy do bazy demo, że sobie zrobię nie wiem trzy warianty obiegu faktur i będą one dostępne i dla klientów, i dla nich, i dla wszystkich innych. Ale to poza wgraniem plików niewiele oznacza. Więc pytanie, jakie są tutaj, bo strategia nasza moim zdaniem jest zdefiniowana – rok temu ją rozpisaliśmy i tu się w sumie zweryfikujemy, czy się coś zmieniło. Czekam na propozycję po tych waszych warsztatach. Rozumiem, że w przyszłym tygodniu się dowiem, jakie są wnioski i tyle.

**Janusz Bossak:** Dobrze.

**Przemysław Sołdacki:** Pytanie, czy macie jakieś uwagi do strategii, bo ona jest ustalona?

**Janusz Bossak:** No dzisiaj ci nie odpowiem na to. To jest jakby temat na osobne spotkanie. Dzisiaj co do tej naszej roadmapy, to mówię, na ten moment na to spotkanie w tym momencie nie jestem w stanie odpowiedzieć. Zrobimy spotkanie z Mateuszem i Danielem, które jest umówione. Wczoraj mieliśmy spotkanie, zrobiliśmy rewizję wszystkich projektów. Jest ponad 30, prawie 40 otwartych tematów, które w tej chwili są prowadzone przez nas. Jeszcze raz jakby na nowo ustalić priorytetem, biorąc pod uwagę końcówkę roku i ten WIM w szczególności i Lot, który...

**Przemysław Sołdacki:** Ja od razu mówię, jeśli tutaj miałbym jako zarząd decydować, najważniejsze jest domknięcie wszystkich wdrożeń.

**Janusz Bossak:** No dokładnie.

**Przemysław Sołdacki:** Ja mogę poczekać z tym, że mamy edytor diagramów. Bo to jakiś edytor jest, konsultanci pracują, tu się tragedia nie stanie, jak poczekamy dwa miesiące dłużej. Bo ten diagram działa tak samo od piętnastu lat. Więc nie wiem – dwa, trzy miesiące nie robią różnicy. A różnicę robi, czy my zamkniemy wdrożenia. Bo to są przeliczalne pieniądze. Więc najbliższe sprinty bym się skupił na tym, żeby zamknąć wdrożenia i wtedy będziemy mieli zamknięte wdrożenia. Zaczniemy się zajmować rozwojem. To jest absolutnie, bym tak do tego podszedł. Bo mnie interesuje, ile my faktur wystawimy w tym roku. Więc jeśli nie wiem się okaże, że nie skończyliśmy WIM w terminie i mamy aferę i negocjacje i kary, i tak dalej, bo robiliśmy edytor formularza – to nie, to ja tak nie chcę.

**Janusz Bossak:** No bo te głąby – no to to jest. Właśnie dlatego mówię, no to.

**Przemysław Sołdacki:** Co to jest priorytet? To jest jeden – to trzeba zrobić. Więc jeśli są jakieś rzeczy, które nie wiem, wdrożenia czekają na pracę R&D, to trzeba je zrobić najpierw.

**Janusz Bossak:** Dokładnie. Dobra, słuchajcie, ja muszę kończyć, sorry, ale.

**Przemysław Sołdacki:** No dobra, no jakby to wiemy, o co chodzi. Nie będziemy trzymać wszystkich.

**Janusz Bossak:** Kolejne jakieś półtorej godziny niedostępnym będę, jechał. Nie wiem, czy raczej trzymać to na kawę.

**Przemysław Sołdacki:** Dobra, to prośba tylko – podajcie mi, do kiedy ta mapa będzie przedyskutowana.

**Damian Kaminski:** Na razie powiedzmy sobie, że w przyszłym tygodniu. Postaramy się, żeby to była pierwsza część.

**Przemysław Sołdacki:** Jeszcze raz, żeby była jasność, czego ja bym oczekiwał. Ja chciałbym dostać od was propozycja roadmapy taką z dokładnością nie wiem właśnie do kwartałów, gdzie tam są rzeczy, że na przykład nie wiem zrobienie rzeczy dla WIM, zrobienie rzeczy dla czegoś tam i po kolei. A później poukładane, że rzeczy rozwojowe – tak, żeby było wiadomo, co jeszcze w tym roku i nie wiem, w Q1 może. Dalej nie musicie planować, po prostu chcę wiedzieć, co teraz jest najważniejsze i co będzie robione. Tyle. Więc nie wiem – czy ja dostanę to do końca przyszłego tygodnia, czy to dłużej potrzebujecie? Nie wiem, ale podajcie mi datę jakąś.

**Damian Kaminski:** Wydaje mi się, nie wiem co wy sądzicie, że milionów przyszły tydzień jest realny. Bo tam jest w ogóle konieczność zrewidowania obecnego kwartału, który jest kluczowy. Więc my musimy ustalić, co jest priorytetem.

**Janusz Bossak:** Tak, tak, myślę, że tak.

**Przemysław Sołdacki:** To słuchajcie, jeśli tak, to jest przyszły tydzień – to będzie tam nie wiem się kończy trzydziestego pierwszego, to ja bym chciał wtedy nie wiem trzeciego listopada. To nie chcę, raz jakieś tam święto?

**Damian Kaminski:** Nie.

**Przemysław Sołdacki:** Nie, już nie. No to początek listopada, czyli trzeciego listopada dostaję od was nie wiem plik i sobie go możemy jeszcze przedyskutować. Nie wiem poniedziałek, czy we wtorek i i tyle – jedziemy dalej.

**Damian Kaminski:** Mhm.

**Przemysław Sołdacki:** Dobra, słuchajcie, to tyle. To dzięki.

**Janusz Bossak:** Dobra, dzięki bardzo.

**Przemysław Sołdacki:** Hej.

**Damian Kaminski:** Cześć. A jeszcze – a już Przemek się rozłączył? No dobrze. Nie nie, to już napiszę do Przemka, bo tam zaprosił mnie na – w sensie – dzwonił mnie na spotkanie poprzednie przed tym, ale nie wiem, czy ja tam byłem zaproszony. Nie mam tego w kalendarzu, więc jak mam w nim uczestniczyć, to muszę mieć, bo miałem konflikt. No dobra.

**Janusz Bossak:** No dobra, ja mówię, ja jestem w tej chwili w Poznaniu – tej rodziny odstawiłem i zaraz ruszam dalej.

**Damian Kaminski:** Wracasz? O k.

**Janusz Bossak:** Pociąg miał już tam prawie 80 minut opóźnienie. Także dobrze, że ich wziąłem, bo nie zdążyłby tutaj.

**Damian Kaminski:** No bywa.

**Janusz Bossak:** Dobra, no to.

**Damian Kaminski:** Polskie koleje.

**Janusz Bossak:** No to jeszcze pracował.

**Damian Kaminski:** Tory były za długie tory.

**Janusz Bossak:** Ekspres – nie, no też taki ekspres.

**Damian Kaminski:** No.

**Janusz Bossak:** Miał być w Bydgoszczy, to jeszcze z Gdańska nie wyruszył.

**Damian Kaminski:** No ja już wrzuciłem tutaj, jak coś – żeby już powiedzmy operacyjnie już podjąłem tutaj to, co przed chwilą umawialiśmy. Więc jak Daniel potwierdzi, to poniedziałek dwunasta trzydzieści możemy już o tym rozmawiać.

**Janusz Bossak:** Dobra. Dobra, okej?

**Damian Kaminski:** Dobra, to hej.

**Janusz Bossak:** No hejka, na razie.

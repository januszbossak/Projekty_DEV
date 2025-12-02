**Data spotkania:** 28 listopada 2025, 11:02 - część 3

---

**[Janusz Bossak]:** Znaczy to są.

**[Kamil Dubaniowski]:** Ja tam w zgłoszeniu wyceny to opisałem, bo przypominam wam, że no my mamy tą funkcję już, bo jest wykonaj przed wykonaniem reguły i tam wyskakuje ci okienko i na razie mamy tam obsłużone tylko pole Użytkownik i możesz wybrać z listy w okienku jakiegoś użytkownika. I później użyć go w dalszym dalszej części kodu.

**[Janusz Bossak]:** No to jest.

**[Kamil Dubaniowski]:** Ja też chyba. No i na razie mamy tylko te 2 rzeczy obsłużone i ja bym chciał to rozwinąć, bo to co tutaj mówimy, możesz później chcieli wykorzystać na pojedynczej sprawie tak, ktoś klika okienko akceptuje, a my go zapytamy, dobra, teraz podaj tam ocenę od Zero do 5, no strzelam jakiś dziwny przykład tak i i podajesz nam piątkę. I my tą piątkę wykorzystujemy w dalszej w dalszym kodzie kodu akceptacji jakiejś sprawy i i my to już mamy tylko ja bym chciał rozszerzyć na żeby działało na modular portowy masowo.

**[Lukasz Bott]:** Ale dobra czy? A o k to właśnie miałem o to zapytać.

**[Janusz Bossak]:** Znaczy to są.

**[Damian Kaminski]:** Jeszcze raz możesz powtórzyć masowo, co ma zadziałać.

**[Kamil Dubaniowski]:** Bo bo bo tak. Aktualnie mamy funkcjonalność, wykonaj przed wykonaniem reguły, no i tam wyskakuje jakiś komunikat, tak. Regułą. Na ręcznie. I może być w tym komunikacie pytanie o to. No cokolwiek, co tam ci pasuje do kontekstu, tak czy na pewno wykonać regułę i może tam osadzić akcję tak nie. Jak dasz tak to dopiero wykonuje się docelowy kod. Reguły jak klikniesz nie no to przerywam i wykonanie reguł i teraz ta funkcjonalność wykonaj przed wykonaniem reguły. Może w pytaniu zawierać select. Listę po użytkownikach, czyli po prostu masz osadzone poletko Użytkownik i możesz wybrać użytkownika z listy i wyskakuje ci na przykład pytanie, czy na pewno chcesz przesłać dalej? Jeśli tak, to do kogo? No i może sobie z listy wybrać tą osobę i my teraz użyjemy tej wybranej osoby w dalszej części kodu, no i na razie obsługujemy to tylko w kontekście pola Użytkownik i tu Łukasz podpowiada, że jeszcze komentarz można zebrać w trakcie wykonywania tej tego tego wstępnego kodu i to aktualnie działa na pojedynczej sprawie.

**[Damian Kaminski]:** Musisz wejść do środka, klikasz tam regułę?

**[Damian Kaminski]:** Chcesz to okno wywołać na raporcie, tak?

**[Kamil Dubaniowski]:** Ja chcę wywołać to, bo teraz ona się nie wywołuje nawet w tej w tej części, którą mamy one się w ogóle nie wywołuje. Ta funkcjonalność wykonaj przed wykonaniem reguły w ogóle nie jest ujęta w regułach masowych ws. Poziom raportu to nie działa, więc to jest pierwsze do zrobienia, żeby żeby żeby to wykonaj przed.

**[Damian Kaminski]:** W sensie o KW sensie to się nie weryfikuje.

**[Kamil Dubaniowski]:** Tak, ja się w ogóle nie wywołujemy tego okna, jeśli ryguła jest wykonywana masowa, wykonujemy albo nic albo nie, nie testowałem tego.

**[Damian Kaminski]:** Nie poczekaj, poczekaj, nie to nie jest tak, że oczywiste jest to, że nie wywołujemy okna, bo żadnego okna nie wywołujemy w kontekście raportu, ale pytanie, czy to okno jest? O nie okno, czy ten kod jest obsługiwany? Czyli zmierzamy do tego, żeby wykonała się reguła? Ktoś musi. Tym duble czekiem potwierdzić tak chce to zrobić i teraz z raportu, jeśli my tego w ogóle nie uwzględniamy, czyli wykonujemy główny treść, reguły bez kliknięcia, tak.

**[Kamil Dubaniowski]:** Tego nie wiem, właśnie tego nie wiem i to jest kluczowe, bo albo ten kot w ogóle się nie wykonuje. To było jeszcze w miarę akceptowalne, ale jeśli my od razu przechodzimy do wykonania kodu głównego, to to w sumie nawet może nie mieć sensu, bo tam w tym kodzie głównym masz odwołanie do decyzji z tego wstępnego kodu.

**[Damian Kaminski]:** Ok. No dokładnie, dokładnie tylko wiesz. To rodzi pewne ryzyka, no bo wyświetlacz ekran o k tylko. Ten ekran też może się wyświetlać w zależności od kontekstu reguły, więc teraz. Co w przypadku Przepraszam od kontekstu sprawy.

**[Kamil Dubaniowski]:** Ten wstępny może mieć kontekst sprawy.

**[Lukasz Bott]:** No może, a czy a czemu nie treść może być taka jak jest taka treść sprawy, a inna jak jest inna treść sprawy.

**[Kamil Dubaniowski]:** Może być ich warunki.

**[Lukasz Bott]:** Może mieć no. Tak no bo może się na przykład sobie tam ten treść komunikatu możesz uzależnić się od wartości jakiegoś wartości pola ustawionego gdzieś tam wcześniej, tak na przykład nie i w jednej sprawie będziesz miał wartość XAW drugiej sprawie y tak a.

**[Damian Kaminski]:** Zmierzam do tego, że jak ktoś myśli co robi i dobrze zrobi raport, to będzie to działać tak jak ktoś nie myśli to powie, że źle to działa, no.

**[Lukasz Bott]:** No ale nie wiem. Dobra, słuchajcie. Słuchaj, słuchajcie, w każdym razie przede wszystkim to, co to do czego zmierza Kamil, to ja tak to rozumiem, że taki mechanizm gdzieś już mamy i być może trzeba go właśnie usprawnić. Może trzeba go w jakiś sposób. Zabezpieczyć, żeby, że o k. Jeżeli chcesz to wykorzystać do masowych. To na przykład Nie możesz robić właśnie, żeby to nie wiem jakieś treści komunikatu, czy coś były kontekstowe tak od kontekstu danej sprawy, tak.

**[Damian Kaminski]:** No ale jak to sprawdzisz?

**[Lukasz Bott]:** Jako dobra praktyka na chociażby tak ale.

**[Damian Kaminski]:** Nie, a jako dobra praktyka, to tak w sensie w dokumentacji to tak, no to znowu wracamy do dokumentacji jak zawsze. No jest wiele aspektów. Ja bym po prostu ja Jestem za tym, że. W sumie nie wiem, sam sobie może przeczyta, to znaczy powinniśmy robić mówi, p tu się zgadzam z Kamilem nie powinniśmy może od razu uwzględniać w przypadku brzegowych, tylko je opisywać, jak sobie chcesz popsuć to sobie popsujesz to działa tak z takimi założeniami z takimi uproszczeniami w założeniach, że nie ma kontekstu i i tak dalej, bo to ma usprawniać wam pracę, a jak sobie na psujecie, że macie różne konteksty no to nie będzie działać.

**[Kamil Dubaniowski]:** Tylko właśnie to co wtedy ma się wydarzyć w tym, co weźmie błędem czy.

**[Damian Kaminski]:** No.

**[Kamil Dubaniowski]:** Trzeba to też.

**[Damian Kaminski]:** No właśnie, no właśnie, bo wiesz pytanie którą, które okno wyświetlasz na ekranie pierwszej sprawy i powielasz odpowiedź pierwszej sprawy we wszystkich sprawach?

**[Lukasz Bott]:** Nie no.

**[Kamil Dubaniowski]:** Bo on musiał. Czy w ogóle powinno nie wykonać się na tym?

**[Damian Kaminski]:** Były musiała być reguła etapu. Nie Przepraszam reguła raportu najlepiej.

**[Kamil Dubaniowski]:** No tak, też pomyślałem o tym, szczerze mówiąc, gdzieś tam w tle, żeby te reguły, które mają warunek przed wykonaniem w ogóle nie podpowiadać ich w opcjach, że może dodać sobie tą regułę do masowych, to jest jakby wyłączenie, że nikt nie zrobi głupiego błędu.

**[Lukasz Bott]:** To też jest wiesz?

**[Kamil Dubaniowski]:** Yy i i też teraz właśnie się da zrobić tak, że dodajesz jakąś regułę, która w ogóle się nie wykonuje, nie działa, bo ma ten warunek przed wykonaniem, więc wtedy wykluczamy w ogóle z listy ustawieniach raportu, że tych reguł i widać, jeśli mają warunek przed wykonaniem. A żeby osiągnąć to, co zlecił klient do wyceny narobimy coś takiego jak typ reguły, reguła do raportu masowego.

**[Damian Kaminski]:** Na. No tak.

**[Kamil Dubaniowski]:** I i wtedy.

**[Damian Kaminski]:** Że wiesz, można pójść po niskiej linii oporu, czyli jednak pozwolić na to tylko. To znaczy jeszcze inaczej, słuchajcie, miało być ja nie wiem, jest na to zgłoszenie, miało być inaczej, miało być na poziomie reguły, w tym pierwszym ekranie. Czech, boks. Pokazuj na liście. Bo pokazuj jako dostępne w masowych. I on miał być odznaczony? Czyli dla wszystkich obecnych. Miało być chyba miał uwzględnić, że jeśli jest null, no to to to pokażemy, a jeśli jest tworzona nowa reguła, to domyślnie jest nie. No jakoś się tam trzeba pewnie obsłużyć i wtedy nie pokazuje się, czyli ktoś musi to po pierwsze włączyć świadomie jak włączy to ponosi tego konsekwencje.

**[Kamil Dubaniowski]:** O k no to jest najprostsze tak, że trochę zrzucanie.

**[Damian Kaminski]:** No tylko wy musicie przyjąć jakieś założenie nawet do wycenie tego klienta, że pokażemy na ekranie ten ekran, to okno, które wywołuje pierwsza reguła.

**[Kamil Dubaniowski]:** Możemy też zwrócić błąd po prostu tak, bo bo to może nie mieć sensu taki wykonać się tam, no. No co ma się zrobić na tych sprawach, gdzie w ogóle nie dotyczy? To pytanie nie wykonali tak kodu dla nich. Wspierałem. Po prostu błąd, że są wybrane sprawy, które nie spełniają zakresu.

**[Damian Kaminski]:** Czyli inaczej, czyli walida pierwsze co robisz, to robisz walidację treści przed wykonaniem reguły.

**[Janusz Bossak]:** Czy?

**[Damian Kaminski]:** O boże, ona w kontekście tej sprawy ma za każdym razem ten sam wynik. To byś musiał tak robić tak i jeśli nie ma to dajesz błąd.

**[Janusz Bossak]:** Znaczy. Może ja trochę podtrzymuję, bo tak widzę. Różne koncepcje wydaje mi się, że po pierwsze trzeba dokończyć i rozbudować. Tą funkcjonalność, którą mamy tym wywołaniem przed uruchomieniem reguły. Na sprawie już pomijam na razie raport tak i tam to co teraz można zrobić to nie jest do końca to o co nam chodzi, bo to są elementy sterujące już przepływem. A my potrzebujemy element, który ktoś sobie coś wpisze i zostanie użyty w regule, więc to trochę jest coś innego niż ten wybór użytkownika. Czy komentarzu w tej chwili? No to.

**[Damian Kaminski]:** Mhm.

**[Kamil Dubaniowski]:** Ale ten wybór użytkownika możesz użyć później dowolnie w kodzie. Nie wiem, może wysłać maila do tej osoby, możesz użyć w dalszej części kodu, to to jest ten kontekst, to działa tak, jakbyśmy sobie życzyli, tylko obsługuje ten typ pola. Jeden konkretnie Nie możesz wpisać nic innego.

**[Janusz Bossak]:** O k no.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** I trzeba dodać teraz.

**[Lukasz Bott]:** W komentarzu spieszysz. A w komentarzu piszesz, chcesz sprawę przedłużyć o 2 dni? Nie tylko więc piszesz tylko o liczbę 2.

**[Janusz Bossak]:** Nie teraz dalej chodzi mi o to, żeby tam tak jak ci użytkownicy są obsłużeni. No to zwracamy tego użytkownika tam jakimś zmiennej takim możemy to uszyć i trzeba teraz dorobić żeby można było. Tam pole numeryczne. Czy pole daty? I na razie bym się do tego. Jakby ograniczył, potem będziemy dodawali kolejne pola, tak i teraz. Na tym kończy się jakby pierwsze mp jeden kropka jeden tak, czyli że można w polu znaczy w oknie tym dialogowym dodawać inne. Typy pól, czyli pole numeryczne i pole data. I one zostaną zwrócone w jakieś zmiennych i można je użyć w regule. To jest pierwsze pierwsza część. Trzeba to zrobić. Druga część to, co mówi Damian, ja rozumiem tak, że rzeczywiście po. Powinno być tak, że uruchamia się. Jak gdyby tak trochę, no ale to tak pewnie będzie pierwsze okno dialogowe z pierwszej sprawy, która jest na tym liście raportu i z pierwszej sprawy, która zostanie zaznaczona. Tak, no bo. No tak pierwsze. I i to okienko się pojawi. No i raport to już jest trudno, tak, raport musi być tak skonstruowany, żeby miał jakby jeden kontekst. Nie jak ktoś zrobi głupio. No to będzie miał głupie.

**[Kamil Dubaniowski]:** Jeden kontekst.

**[Janusz Bossak]:** Pojawia się to okno. Ktoś wpisuje jakieś wartości i tu jest cała magia to wartości, raport sobie gdzieś tam w swojej głowie zapamiętuje tak jak teraz się to dzieje trochę przy tym pinie i podpisywaniu masowym, czyli zapamiętuję sobie tą liczbę czy tą datę czy tego użytkownika wybranego. I uruchamia te sprawy kolejne. Już nie uruchamiając. Tego okna dialogowego. Przed wykonaniem reguły.

**[Kamil Dubaniowski]:** Dodam zapamiętuje też decyzję użytkownika z tego pierwszego okna dialogowego tam możesz mieć tak nie może tak.

**[Janusz Bossak]:** Tak, tak.

**[Damian Kaminski]:** No dokładnie, ale ja na dobra skończ już, bo ja mam kontrpropozycję.

**[Janusz Bossak]:** I. I wykonuje i wykonuje tą część reguły już taki jak gdyby po wykonaniu tej akcji to pokaż to okienko jest, czyli pomija tą część tego wykonania.

**[Damian Kaminski]:** Zapamiętuję po prostu wynik. Pierwszy pierwszy pierwszy wskazanie.

**[Janusz Bossak]:** Zapamiętuj wynik pierwszej i podstawia po prostu tak jakąś tam i na każdego kolejnego się to już dzieje automatycznie tak, czyli ta sama decyzja jest dla wszystkich.

**[Damian Kaminski]:** Mhm.

**[Janusz Bossak]:** I ta sama te same wartości są dla wszystkich spraw, które będą masowo obsłużone z poziomu raportu. Tak ja to widzę.

**[Damian Kaminski]:** No dobrze, tylko teraz tak z poziomu raportu w zasadzie. Mm ja to widzę z kolei także. Na na na poziomie sprawy ten ***** czek dotyczy jakiś newralgicznych kwestii, jeśli mają być jakieś 2 tryby wyboru tak czy czy na pewno chcesz usunąć, czy na pewno chcesz pominąć, a teraz tak w kontekście masowych raczej to nie będzie miał zastosowania, jeżeli tam tam właśnie bardziej potrzebujemy kwestii wskazania kogoś i żeby czy wskazania jakieś daty i żeby wykonać to od razu masowo i teraz zastanawiam się nad jeszcze innym kontekstem.

**[Kamil Dubaniowski]:** Tak.

**[Damian Kaminski]:** Żeby to była jednak w cudzysłowie reguła raportu, ale tylko skończę to zaraz komentujecie, bo sama reguła zostaje na poziomie procesu. Tylko, że jest funkcją, ale. To, co zbieramy, definiujemy na poziomie raportu. Czyli mamy jakieś byt, w którym? Podajemy nazwę i typ pola, czyli podpina się to pod to wywołanie masowe. Ee, ale definiujemy nazwę powiedzmy tego wywołania na poziomie na poziomie raportu wskazujemy, że potrzebujemy pole numeryczne i pole data. I to się wywołuje na poziomie raportu. To jest przypisane do jakichś stałych zmiennych, czyli jest numer, jest jakieś i d. Przy tym na przykład nie wiem jakiś tam numer raportu i w tej funkcji, która jest osadzona na procesie, możemy odwołać się do tych zmiennych do wartości tych zmiennych.

**[Janusz Bossak]:** No może tak wejść znaczy ten pomysł, który tam pierwotnie tutaj też ty powiedziałaś, ja znaczy tak to jest decyzja też jeszcze do Piotra Buczkowskiego. Tak?

**[Kamil Dubaniowski]:** Uniwersalne.

**[Janusz Bossak]:** Mamy już tą funkcjonalność i jakby ograniczamy się do tego, że pierwsze wywołanie na pierwszej sprawie powoduje jego wyświetlenie, bo nie mamy jeszcze tych wartości, to możemy po tym poznać. Tak, czyli raport wie, że powinien coś mieć, a nie ma. Yy no i tyle.

**[Damian Kaminski]:** No tylko tu jest to ryzyko niespójności, nie, że ktoś to tak zaprojektuje i prędzej czy później się z tym zmierzymy, bo ktoś w końcu na to to wymyślili.

**[Kamil Dubaniowski]:** Powiedzcie to mp może np może być takie a później można to rozwinąć do tego nie wiem poziomu, że jak on dojdzie do sprawy, która nagle okazuje się, że ma inny wynik to wyskakuje kolejne okno. To zrobiłem 10, ale tu jest inna sytuacja. No i teraz chcę, żebyś podał mi to jak i leci dalej tak i ewentualnie już ma w pamięci 2 2 odpowiedzi i wiecie to jest komplikujemy, ale to nie Jestem vipem vip jest takie, że leci po pierwszym kontekście do końca resztę.

**[Damian Kaminski]:** To zmienia. No.

**[Janusz Bossak]:** No nie czy?

**[Damian Kaminski]:** To też jest opcja.

**[Kamil Dubaniowski]:** Wyłapie, że jest inny kontekst, to nawet nie podejmuje i i po prostu niewykonalne.

**[Janusz Bossak]:** No ale jaka może być sytuacja innego kontekstu? Nie bardzo rozumiem.

**[Kamil Dubaniowski]:** Czyli na nie wiem na jednej sprawie masz wskazane, że to jest faktura proforma, a na innej, że to jest zwykły efekt, krawat i teraz kontekst może być taki, że jeśli to jest faktura proforma, to zadaj takie pytanie i zbierz takie dane. A jak to jest faktura vat, to zadaj takie pytanie i zbierz takie dane. A Tomasz na jednym raporcie tym wykładowym?

**[Damian Kaminski]:** To już jest Janusz, bardziej skomplikowany przypadek, ale wiesz, prawda jest taka, że do niego dojdziemy kiedyś nie.

**[Janusz Bossak]:** No. Znaczy ten pomysł, który ty Damian podałeś też? Może dokładnie na tknąć się na te same problemy. Co teraz powiedzieliśmy tak, czyli jeżeli byśmy to mieli definiowane po stronie raportu, czyli widzę to tak, że tam okienku gdzie włączam akcje masowe. Mam jakiś nóż element oprócz tego, że wybiorę. Regułę, która się ma uruchamiać. To jeszcze definiuje na tym poziomie jakieś pola, które chce zbierać tak i teraz zobaczcie ile tu jest różnych rzeczy. Nazwę tego pola, nazwę w innym języku.

**[Damian Kaminski]:** Mhm, masz rację, masz red.

**[Janusz Bossak]:** I tak dalej i tak dalej. Cała masa rzeczy, które muszę tutaj zrobić, żeby mi się to pole wyświetliło, tak?

**[Kamil Dubaniowski]:** No tutaj.

**[Janusz Bossak]:** Yy no nie wiem.

**[Kamil Dubaniowski]:** No i to też jest już tylko na poziom raportu, a czemu nie móc wykonać tej samej akcji jak wejdę do sprawy?

**[Janusz Bossak]:** No właśnie, no i teraz tam musiałbym osobno.

**[Kamil Dubaniowski]:** Pojedynczej, więc dlatego.

**[Damian Kaminski]:** Znaczy, nie, nie to tu może się wykonać, tylko musiałbyś tą funkcję osadzić do przycisku, ale tak masz rację, w sensie nie trzeba kodu przepisywać, ale trzeba Jeszcze raz definiować od przycisk. Tak, to ja rzuciłem pomysł. Nie mówię, że to jest najlepsze rozwiązanie. Ale to, co ty powiedziałeś z tym kontekstem, że on porównuje tak, że dokładnie jest ta sama treść. Idzie sprawa po sprawie. Sprawa po sprawie patrzy, że są te same możliwości i jest ten sam, a odpowiedź skoro są te same możliwości jak dochodzi do sprawy, która ma inne możliwości, bo z tego to wynika, no to się zatrzymuje i pyta drugi raz dla teraz dla kolejnego ciągu i nawet może pamiętać w odpowiedzi 2 i i jakby było nawet na zmianę to zrobi tak to spraw po 2 decyzjach.

**[Kamil Dubaniowski]:** No musiałby 2 pamiętać wtedy taki dla dzieci.

**[Damian Kaminski]:** To jest niezły, to to można tak jako mvp tam 2 czy 3, a dzisiaj zrobić założenie takie, że jest jeden kontekst tak, czyli przed wykonaniem reguły nie może zmieniać kontekstu w zależności od danych, choć zawsze statyczne, takie samo. Wtedy to będzie działać.

**[Kamil Dubaniowski]:** No i to to naprawdę dużo. Ja się tego użytkownika też trzeba dopracować, bo z tego co kojarzę tam nie można grób wybierać. I zablokowałem się na przykład no takim kryzysie, że coś tam warunkowo. Właśnie chciałem, żeby podali grupę, do której chcą przekazać sprawę czy tam wysłać maila no i już nie mogłem więc tego użytkownika bym dopracował pod kątem, że możesz wybrać z listy użytkowników bądź grup. A drugi wątek to jest właśnie przestrzenią, datę i liczbę. I i to bym uznala wtedy dużo rzeczy da się zrobić o wiele intuicyjnie niej, bo masz jeden przycisk na formularzu, który tam robi. Nie wiem, akceptuj i tutaj pytamy cię o k, ale teraz tam albo no, najlepszy przypadek, jaki miałem zmieni właściciela, tak, że to nie do mnie korespondencja przekaż do innego właściciela i teraz, no jak to zrobić na formularzu? Muszę gdzieś znaleźć sekcję, gdzie jest wskazany właściciel. Muszę zmienić siebie na kogoś innego i i przekazać sprawę osobnym przyciskiem. Gdzieś tam może osadzony. Nawet na formularzu, ale muszę to wiedzieć, a tak to mam na górnej belce przycisk zmień właściciela klikam, a modlitwy nie pyta o k na kogo chcesz zmienić? Wybierasz z listy, wysyłam zmieniam pieniądz właściciel.

**[Damian Kaminski]:** Ale to czekaj, bo teraz to taki działa. Tak czy co ty opisałeś?

**[Kamil Dubaniowski]:** No no właśnie nie, no bo nie można wybrać grupy, a ja akurat miałem wybrałem reszcie kej ze przekazuje się do grupy.

**[Damian Kaminski]:** No k. To znaczy w ogóle pole Użytkownik? Ma kilka rzeczy, które można poprawić, to to też można do tego siąść, bo kiedyś było tak, a teraz znowu są nowe potrzeby. Jest tego coraz więcej, coraz więcej grup i tak dalej i tam nie można. Ograniczyć na nim, że mają być na przykład dostępne 3 grupy, trzeba robić pośredni krok w postaci na przykład słownikach, w którym osadzimy 3 grupy i wtedy mapować ciepło nazwach na nazwy grup, a w zasadzie można było to zrobić. Po nazwach tych grup po prostu definiując, że wybór jest 3.

**[Kamil Dubaniowski]:** No to też kolejny kejs dlatego naszego warunku, żeby tam też definiować zakres.

**[Damian Kaminski]:** Powinno być poprawione i wtedy. Aha, tylko tam to w regułach musiałoby być nie.

**[Kamil Dubaniowski]:** Tylko tam nie dotąd to jest zupełnie tak, to jest zupełnie inny kontekst. Tak to jest jakby po prostu użytkownika i jak najbardziej na tym rozwój tego warunku mógłby do tego iść, że możesz napisać sobie, że o k. Tutaj teraz zapytaj o użytkownika liczbę bądź datę, ale żeby tam się dało też na przykład narzucić zakres, że o k. Na grupy, ale tylko te może wybrać z listy Użytkownik albo zakresu od jeden do 5, bo nie można przesunąć o więcej niż 5 dni termin.

**[Damian Kaminski]:** Mhm.

**[Kamil Dubaniowski]:** Żeby żeby już też jakby.

**[Damian Kaminski]:** No raczej dat tam od jeden do 5 można myśleć, że tutaj daty. No tak.

**[Kamil Dubaniowski]:** Od jeden do 5 dni.

**[Damian Kaminski]:** Nawet jeśli to sprowadzi no mów, mów.

**[Kamil Dubaniowski]:** Od nimi chodzi o tak, bo tu jest ten case do wyceny, że klient musi podać o ile dni zmienia termin realizacji zadania. Na przykład ma teraz.

**[Damian Kaminski]:** Czyli lista rozwijana. I definiujesz co chcesz możesz zdefiniować daty możesz zdefiniować, bo to można potem przełożyć na dzisiaj w sensie jako mvp, że jeśli byś zrobił pole typu lista rozwijana, to tam możesz podać tak 1, 2 3 4 5 możesz podać Damian Kamil, Łukasz Janusz, możesz podać? 5 dat. Z najbliższych dni oczywiście w przyszłości możemy dołożyć pole data, ale dzisiaj lista rozwijana daje ci perspektywę taku, że możesz wrzucić coś, co tam, co chcesz. Może w tym kierunku powinniśmy pójść?

**[Lukasz Bott]:** I wtedy opisujesz sobie komentarzem odpowiednim, tak czy co to jak to prezentować się?

**[Kamil Dubaniowski]:** Znaczy w ogóle teraz nawet jak to mówimy? To. Decyzja mogłaby, bo tam pisał. Proszę Tomek serwisu klinowski mogłoby być tak, że wystarczy sama obsługa tego, co jest tylko, żeby to działało. Z poziomu raportu masowo i ja mógłbym zapytać, o ile przesunąć datę o jeden i tam jako przycisk już akcji i tak jeden dzień 2 dni. I w zależności od tego co klikną to ja lubię plus jeden albo plus 2 dni na obecny i dacie, bo nie da się więcej niż o 2 dni przesunąć terminu. W tym czasie tak, ale jakby teraz jak o tym dyskutujemy, to właściwie gdyby te.

**[Damian Kaminski]:** No tak, że sam przycisk definiuje co zrobisz.

**[Kamil Dubaniowski]:** Tak, że sam przycisk ci już jakby. Definiuje, którą część kodu wykonać. Jak kliknę ktoś jeden to wykonuje się kod, który dodaje plus jeden dzień, a jak ktoś kliknie, że od 2 dni to wykonuje się kod, który dodaje 2 dni do obecnej daty? Ee i i to już właściwie zamyka temat, gdyby te reguły w ogóle odpalały się na raportach jaką osobę. Nawet nie trzeba dodawać obsługi nowego typu pola, tak naprawdę jako pierwszy vip.

**[Lukasz Bott]:** Mamy mpi Zero pu.

**[Kamil Dubaniowski]:** No i co ważne Tomek Kalinowski zaznaczył, że obsługa błędów musi być, bo na pojedynczych spraw, w sensie jak w jakiejś sprawie, no w ten kot się nie wykona. Tak, to trzeba pokazać, ale to robimy w sumie.

**[Damian Kaminski]:** Jaka obsługa błędów? No właśnie pokazujemy na czerwono wiersz.

**[Kamil Dubaniowski]:** Tak, tak, tak jest.

**[Damian Kaminski]:** Bo mnie też pytał przed chwilą. Mm. Przemek. Jaki ma być skutek? Bo to też według mnie jest temat rozwojowy. Zaraz wam pokażę i powiem, mogę powiedzieć.

**[Kamil Dubaniowski]:** To jeszcze może źle skończyć to Janusz czy do tej wyceny w sensie do akceptacji jej potrzebujesz jeszcze coś, bo możemy dać taką cenę klientowi? Tam może trochę realizacja będzie się różniła od tego Cytat, co zaproponowaliśmy, bo będzie to jako przycisk w pierwszej wersji 1 2 dni.

**[Damian Kaminski]:** No mów.

**[Kamil Dubaniowski]:** Ale czy czy to jest ok? Co tam opisaliśmy za nią, czy jeszcze mam do tego jakieś pytania?

**[Janusz Bossak]:** Znaczy to, co napisała ania, to jest jakieś techniczne i ja tego nie rozumiem co tam jest napisane szczerze mówiąc znaczy.

**[Kamil Dubaniowski]:** No zgadzam się tam więcej w komentarzach jest biznesowego tematu niż sobie realizacji.

**[Lukasz Bott]:** Znaczy.

**[Damian Kaminski]:** Ale dobra, czyli podsumowując to co powiedziałeś czyli. W ramach mpp nie zmieniamy w ogóle kontekstu na sprawie, bo obsłużyć jesteście to w stanie po prostu 3 przyciskami, czyli Anuluj. Jeden lub 2. Ee i tylko chodzi o to, żeby wyświetlić ten komunikat z poziomu raportu i powielić jego odpowiedź na wszystkich.

**[Kamil Dubaniowski]:** No i żeby zapamiętał raport, kontekst i powielił na wszystkich zaznaczonych sprawach.

**[Damian Kaminski]:** Tak, tak, a potem kolejne wydanie to jest już ingerencja w sam ten popup gdzie dokładacie dodatkowe pole jakiegoś tematyczne. Nie wiem tam numeryczne lista wyboru, cokolwiek co się zastanowicie, no i potem odtworzenie tego analogicznie po stronie raportu.

**[Janusz Bossak]:** Tak, tak, tak.

**[Kamil Dubaniowski]:** Jest.

**[Janusz Bossak]:** No nie, no nie? Znaczy.

**[Damian Kaminski]:** Jak to, no nie?

**[Janusz Bossak]:** Kolejność musi być odwrotna, najpierw musimy dodać możliwość. Wyświetlania w tym polu jakieś wartości numerycznej.

**[Kamil Dubaniowski]:** Ale to to ja przerwę wip możemy zminimalizować.

**[Damian Kaminski]:** No tak powiedziałem. Na sprawie.

**[Kamil Dubaniowski]:** W ogóle nakład pracy dla tego klienta, bo z biznesowego kontekstu oni mogą przesunąć maksymalnie o 2 dni. Czyli możesz dodać jeden lub 2 dni, ja zasugerowałem.

**[Damian Kaminski]:** No tak.

**[Janusz Bossak]:** O nie. No nie tam jest napisanych komentarzy, oni nie chcą mieć 5 przycisków, że tu są 2. Tu są 3, tu jest 5 tu coś.

**[Damian Kaminski]:** Ale to.

**[Janusz Bossak]:** No nie oni chcą wpisać liczbę 2 3 1.

**[Damian Kaminski]:** Znaczy, słuchajcie, powiedziałbym tak.

**[Janusz Bossak]:** Bo gdyby to było przesunięcie?

**[Damian Kaminski]:** Ja bym nie wyceniał przycisków to to co Kamil idzie w to to to nie jest nasz produkt ostateczny, to może być krok pośredni, żeby szybciej dostarczyć klientowi rozwiązanie. Jeśli to są faktycznie tylko jeden albo 2 dni. Bo my możemy pracować już nad wyświetleniem na raporcie tego okna dialogowego, na którym nie ma kontekstu wyboru czegokolwiek, jakieś treści, tylko jest po prostu podjęcie jednej tam z 2 czy 3 akcji.

**[Kamil Dubaniowski]:** Ja Janusz ja może ile pamiętam temat, ale ja kojarzę tak, że Tomek to tak wymyślił, że my mamy wali dować czy oni nie podali więcej niż 2?

**[Damian Kaminski]:** I w.

**[Janusz Bossak]:** No chyba.

**[Kamil Dubaniowski]:** Bo kot reguły to robi jak próbujesz dodać więcej niż 2 dni to jest błąd, no to to jest zupełnie bez sensu. No to ograniczmy wybór do jeden lub 2 a a to, że nie wiem, może jeszcze Tomka to odpytać, ale nawet jeśli byśmy poszli takim torem to my nic nie tracimy. Tak najpierw zróbmy, żeby to w ogóle działało to co jest na module raport owym masowo, później, potencjalnie jeśli będzie potrzeba, to dodajmy obsługę numeryczną.

**[Damian Kaminski]:** No tak dokładnie.

**[Janusz Bossak]:** No dobrze rozumiem.

**[Kamil Dubaniowski]:** Bo na razie nie działa w ogóle to, co już mamy nie działa na module ofertowym i ja mogę mieć już. Jakby taki kontekst zupełnie niepowiązany z tym co wyceniamy tutaj chcę użyć takiej reguły, a ona mi się nie wykonuje, to powiedzmy, że to moim zdaniem jest pierwszy pierwszy cel, żeby to co działa działało też w module kopertowym, a później możemy, jeśli będzie potrzeba dokładać kolejne pola. Jestem za tym, to już powiedziałem. Jestem za tym, bo sam miałem takie potrzeby, ale ale na razie obsłużymy, żeby to w ogóle działa ona masowych.

**[Damian Kaminski]:** Tak no po prostu jak klient chce coś zasponsorować to nie róbmy rozwiązania takiego, które będzie działało tylko dla prostych rozwiązań, tylko to możemy mu dostarczyć szybciej, ale docelowo dajemy pole do wprowadzenia, tak.

**[Janusz Bossak]:** Według mnie to jest konieczne, absolutnie koniecznie znaczy to, co teraz podajecie, to jest obejście. To jest word cloud, tak znaczy dla tego przypadku da się tak zrobić, że skoro to jest tylko jeden lub 2 dni.

**[Kamil Dubaniowski]:** Tak, tak, tak, tak, tak.

**[Janusz Bossak]:** No to wybieram. Mam 2. Rozumiem, że wtedy są generowane przyciski? Tym oknie i wybieram jeden lub 2 tak ten przycisk.

**[Damian Kaminski]:** No tak, no to jest wiecie to jest ten vip jeden powiedzmy do zrobienia po sprincie, a po 2 sprintach to już ma być spolem.

**[Kamil Dubaniowski]:** Ps. Dla. Tego chce zmiany kolejności, bo to co wspomniałem, no po prostu aktualnie to w ogóle nie działa, więc nie dodawajmy nowych rzeczy, zróbmy, żeby to co jest działało, a później dodajemy kolejną nowość. Patrząc trochę na kontekst tego klienta, bo.

**[Damian Kaminski]:** No ja Jestem za, ale my dzisiaj nie mamy w tym polu żadnego zbierania tak jeszcze, a mamy te użytkownika tak.

**[Kamil Dubaniowski]:** Mamy zbieranie, mamy zbieranie użytkowa. Wynika i komentarz. No i teraz powiedzmy, że ja mógłbym chcieć to wykonać nawet bez zbierania danych. Po prostu mam kod, który mnie pyta, czy na pewno przesłać do akceptacji i jak ja to użyję na regule na raporcie, żeby to masowo można było wysyłać do akceptacji, to mi to pytanie się nie nie wyświetli i prawdopodobnie w ogóle kot się nie wykona tak, czyli jeśli albo czy na pewno no tak dobrze, no ale wolałbym, żeby to działało, czyli żeby mnie zapytała, czy na pewno wysłać czy na pewno usunąć.

**[Damian Kaminski]:** Mhm. No czyli dobrze. Nie no to jasne oczywiście, ale jak się nie wykona to dobrze, bo to bezpieczne.

**[Kamil Dubaniowski]:** To dobrze, no to takie ubezpiecznie niedobrze, ale bezpiecznie bezpiecznie niedobrze. No natomiast do tego bym zaczął.

**[Damian Kaminski]:** No wiecie, masowość się kłóci z ostrzeżeniami, albo chcemy masowo i szybko, albo chcemy ostrzegać tu jedyne tylko co to właśnie ten kontekst dodatkowej definicji, jakieś wartości, której nie ma.

**[Kamil Dubaniowski]:** No no.

**[Damian Kaminski]:** Czy w postaci właśnie 2 dni?

**[Kamil Dubaniowski]:** Nikt nikomu nie nie nie zgodzę się. Ja jak masz przycisk usuń której robili bikes i ktoś mi z klikiem go kliknie zamiast zaakceptować i się wykonał od razu nas tu sprawach to wolałbym, żeby mnie zapytała czy na pewno usunę.

**[Damian Kaminski]:** I ten. No. Kto to zrobił produkcyjnie?

**[Kamil Dubaniowski]:** No nie no wiem, ale różne inne akcje, nie wiem centymetry czy jakiś może być czy odrzuć, akceptuje tak i chciałem kliknąć Akceptuję, a 100 spraw odrzuciłem przez przypadek. Odrzuć też powinno być zabezpieczone pytaniem, czy na pewno, bo już tam powiedzmy jakby jakaś negatywna ścieżka wręcz albo sprawy od razu się oznaczają jako hiden, no różne są konteksty.

**[Damian Kaminski]:** No to była nie, no to wiesz, no to jak ktoś takie coś daje produkcyjnie, no to.

**[Lukasz Bott]:** Nie, no ale czekaj.

**[Damian Kaminski]:** Nie wiesz, dlaczego już ci mówię, bo jak odrzucam, ja w ogóle nigdy nie dałem. Odrzuć na masowość, jak odrzucasz, to podaj powód.

**[Kamil Dubaniowski]:** A może właśnie może może powinno wyskoczyć okienko z pytaniem, bo masowo ten sam powód podajesz?

**[Damian Kaminski]:** Musisz podać powód, to musisz znać kontekst. Nie odrzucasz masowo.

**[Lukasz Bott]:** No. No i właśnie.

**[Damian Kaminski]:** No to chyba tylko wypadkach gdzie nie wiem ktoś wnioskuje o o nie wiem urlop którego już nie ma. No tak, no bo kiedy odrzucasz z jednym powodem no nie wiem.

**[Lukasz Bott]:** Najbardziej właśnie.

**[Kamil Dubaniowski]:** Ja zarobiłem w szkoleniach bhp rozwalaniem no za.

**[Damian Kaminski]:** No wiesz, no teoretyczne sytuacje, no może tak się zdarzyć, ale ale według mnie to nie jest naturalne użycie, jednak naturalnym jest coś, co przepycha dalej, co właśnie nie wymaga komentarza. Komentarz według mnie, za każdym razem ma jakiś kontekst, no chyba, że to jest jakaś decyzja odgórna, że no nie wiem, zamykamy wszystkie sprawy, bo ten proces już nie działa. Proszę zrobić w nowym.

**[Lukasz Bott]:** No ale to wiesz, no ale to wtedy robisz sobie właśnie regułę, gdzie hard sobie to tą decyzję, tak.

**[Damian Kaminski]:** Dokładnie robisz regułę cykliczną, która zamyka wszystkie sprawy i wysyła do właścicieli aktualnych, że zamykamy tą sprawę. Przechodzimy na nowe procesy, no.

**[Lukasz Bott]:** I Jurka wierzył. Czy zamykamy, czy zamknęliśmy tę sprawę? Bo bo coś tam nie i tyle.

**[Kamil Dubaniowski]:** No dobra, nie ma co jakby mamy, bo już spalony co co do czego dążymy. Czyli pierwszy etap to jest, żeby to w ogóle działało na module kopertowym masowo, d. Drugi kontekst to jest rozszerzenie tego nowe typy pól. Trzeci kontekst to jest może właśnie wyłapywanie, że no tutaj i wchodzimy w inny warunek. Inne pytanie powinienem zadać, więc przerywam, zadaje pytanie i lecę dalej masowo z tym co zaznaczone. To jest anglik 3 już. Ocenia. Mpi 4. Może na tych zakresach danych, o które pytamy tak, czyli pytamy o użytkownika? Pytamy o datę, pytamy o. Liczbę, żeby dało się narzucić jakiś warunek. Dodatkowo tak, że pytają użytkownika, ale tylko z tej grupy pytaj o liczbę, ale tylko z zakresu od jeden do 10, bo kontekstowo to może być jakieś pytanie o nie wiem, ocenę będą sobie zbierać feedback i od użytkowników. Czy proces jest prosty czy nie? Tak na końcu procesu po wykonaniu akcji zapytają, okej, dziękujemy teraz pytanie, jak tam oceniasz proces?

**[Lukasz Bott]:** Liczbę.

**[Kamil Dubaniowski]:** Od jeden do 10.

**[Damian Kaminski]:** No i właśnie w tym kontekście ja sugeruję, bo jakie typy pól chcemy tam zdefiniować? Mamy użytkownika mamy tekstowe.

**[Kamil Dubaniowski]:** Znaczy to to nie nie patrzę na to pod kątem typu pola na formularzu amlogic mo to może być kolejne bp, tak że że patrzy w ogóle na jakieś pole i zamiast Użytkownik uzupełnić to pole na formularzu uzupełnia je w. W oknie dialogowym to kolejny typ mogłoby być to pod pryzmatem, że to jest zupełnie coś niezależnego. My zbieramy jakiś konkretny typ danych, które później masz przechowywanych zmianę i możesz sobie użyć go w kodzie.

**[Damian Kaminski]:** No.

**[Kamil Dubaniowski]:** Możesz wstawić do jakiegoś pola, możesz coś dodać, użyć w jakiejś funkcji reguł, tą wartość, którą.

**[Damian Kaminski]:** Czyli pole tekstowe zakładasz?

**[Kamil Dubaniowski]:** No ja zakładam numeryczne, bo tekstowe pewnie będzie zależy jak to będzie Stream mi to.

**[Damian Kaminski]:** No ale właśnie tekst numeryczne to co to znaczy, że będzie się tak zachowywać jak pole, nie będziesz mógł w niego w nie wprowadzić tekstu.

**[Kamil Dubaniowski]:** No tak.

**[Damian Kaminski]:** Tak, zakładasz tak.

**[Kamil Dubaniowski]:** Tak no tekst jest zbyt dużą zmienną, no bo o co zapytać użytkownika? Do kogo chcesz przesłać ją ci podała Kamil dubaniowski z małych a albo.

**[Damian Kaminski]:** Nie, nie, nie, no, nie, nie, to użytkownika już mamy, to już nie podważam to czego mamy możemy mieć teraz tekstowe, ogólnie, które przyjmujemy, że interpretujemy, czy to jest liczba, czy to nie jest liczba, jak nie jest, no to.

**[Kamil Dubaniowski]:** No tak, tak, tak, tak, tak.

**[Damian Kaminski]:** To nie jest, ale można też osadzić na nim jakieś walidację, bo te walidację też mogą być różne. Możemy przyjąć, że walidację określamy rexem, no ale to jest skomplikowane nawet dla naszych wdrożeń owców bym powiedział.

**[Kamil Dubaniowski]:** Mam jeszcze 2 liczby, bo tak.

**[Damian Kaminski]:** No to właśnie to wybierasz jaki typ czy tak, czyli czy string czy czy jakiś decimal. Ee. Ale teraz perspektywa tego, jak oceniasz coś, to czy warto? To wali dować czy dołożyć powiedzmy mamy tekst, mamy liczbę potencjalnie datę. I lista wyboru, która której możesz przedstawić wszystko w zasadzie, bo możesz wybrać daty, wtedy masz ograniczenie. Oczywiście, jeśli ma to sens, jeśli tych dat jest 5, a nie 50. Ee, możesz wybrać skalę, może wybrać jakieś określone stringi, nie masz błędu.

**[Kamil Dubaniowski]:** No pasuje mi wszystko. Poza tym takimi w ogóle swobodnym tekstem, bo to jest niedożywiony, swobodnego tekstu, w ogóle jakby jaki przypadek biznesowy komentarz już mamy. No to w komentarzu możesz wpisać sobie dowolny tekst i później wykorzystać ten komentarz w kodzie.

**[Damian Kaminski]:** A czyli byś nie nie brał swobodnego tekstu? Tylko że komentarza Nie zakładasz wyświetlać tutaj.

**[Kamil Dubaniowski]:** Jest już obsłużony komentarz i Użytkownik aktualnie jest obsłużony, czyli możesz wpisać.

**[Damian Kaminski]:** Nie komentarz jest po akcji.

**[Kamil Dubaniowski]:** Łukasz, jak to wygląda?

**[Damian Kaminski]:** Po wyborze.

**[Lukasz Bott]:** Nie wiem moim zdaniem.

**[Damian Kaminski]:** 100%.

**[Lukasz Bott]:** Komentarz jest po wyborze.

**[Damian Kaminski]:** Tak. Mogę wam to pokazać?

**[Lukasz Bott]:** No ale nie, bo bardziej chodzi mi. Chodziło mi o to, że potem, ale to jest nadal wykonywane. Ten komentarz jest po wyborze, ale nadal wykonywany w kontekście tak jakby to jego tej regu. Tak, że bo tak to mi chodzi to.

**[Kamil Dubaniowski]:** Przed tak.

**[Damian Kaminski]:** Nie, to jest wykonywane w to znaczy.

**[Kamil Dubaniowski]:** Ale to mówisz o tym ustawieniu po prawej stronie ustawienie reguły, że tam, no to nie, no to nie to w kodzie tej premier reguły możesz dać parametr, że zapytaj o komentarz. To jest inny komentarz niż ten tam spk boxa.

**[Damian Kaminski]:** Tak, tak.

**[Lukasz Bott]:** Nie, nie, nie. Dokładnie tam i tu jest cały numer.

**[Damian Kaminski]:** I wtedy to jest tym samym ekranie.

**[Kamil Dubaniowski]:** Bo nie wiem w sumie.

**[Lukasz Bott]:** Tak, tak, tak.

**[Kamil Dubaniowski]:** Nie wydaje mi się, że w ogóle te dane zbieramy po podjęciu decyzji. Tak, tak mi się wydaje, że podejmujesz decyzję na przykład tak czy przekazać dalej kilka tak, a my cię wtedy dopiero pytamy w drugim komunikacie. No to pokaż użytkownika i tak samo jest z tym komentarzem i dopiero jak to wszystko już przejdziesz, to wykonuje się tylko te reguły, tak mi się kojarzą.

**[Damian Kaminski]:** Czekajcie. Kurde.

**[Lukasz Bott]:** No ok, dobra, ale ale co do zasady chodziło mi o to, że to jest właśnie w ramach tej całej i to są 2. To tak jakby 2 różne komentarze, Damian.

**[Damian Kaminski]:** Aha. Dobra, słuchajcie, bo muszę muszę lecieć dalej, bo nie zrobię, nie zrobię tego, co zaplanowałem we to znaczy trzeba określić to, co idziemy, z czym z czym do klienta i według mnie trzeba to zrobić po prostu na filmie z tego prototyp, jak to będzie się zachowywać?

**[Lukasz Bott]:** I.

**[Kamil Dubaniowski]:** No dobra no.

**[Damian Kaminski]:** Jeśli ma to działać inaczej niż dzisiaj, czyli jakie pola i tyle? I tak powinniśmy. Ja tak robię z tą historią biznesową, tak, chcę to zrobić, żeby klient zobaczył, jak to będzie wyglądało i żeby zaakceptował to jak to będzie wyglądało. Bo tam wiecie to, że się nie wykona to o k. Natomiast te przejścia same tak, że tu będziesz wybierać, a potem jak klikniesz dopiero wybór to pojawi się drugie okno, gdzie będziesz wskazywać zakres, ale już. Wskazujesz zakres pytanie czy. To pytanie o polecie nie zaskoczy co wtedy tam jeszcze można anulować? Czasami ktoś może nie wiedzieć co będzie dalej. Tak na razie mówię wykonać, a potem go pyta.

**[Kamil Dubaniowski]:** Tak, tak.

**[Damian Kaminski]:** To teraz coś podaj, a on mówi, ale ja nie wiem w sumie co mam tu podejść to dobre najpierw się dowiem Jeszcze raz będę to wykonywał.

**[Kamil Dubaniowski]:** Odświeżenia tego użyłem z 2 x 3. Może w tym okresie ostatnio?

**[Damian Kaminski]:** No trzeba według mnie zabrać dokładnie co my mamy na dzisiaj, co byśmy chcieli mieć docelowo, czy to ma być właśnie kolejne okno, czy w jednym oknie?

**[Kamil Dubaniowski]:** To też nie ma co tam super się nad tą wygrywać, a ja wyceniła dodanie tego do modułu raport owego i dodanie nowego typu pola na w ogóle 2 dni. Chyba ja jej podbiłem razy 2 x 4.

**[Damian Kaminski]:** No. Oj.

**[Lukasz Bott]:** Nie człowieku z testami jakimiś tymi nie daj.

**[Damian Kaminski]:** O jo jo ya i tanie. Ja bym tutaj.

**[Lukasz Bott]:** To jest grzebanie wieś.

**[Damian Kaminski]:** To jeszcze po jeszcze podwoił twoją wycenę.

**[Lukasz Bott]:** Co najmniej.

**[Kamil Dubaniowski]:** No to Janusz to taka uwaga do tej wyceny po prostu, żebyś jeszcze chyba tym na tym etapie może zaktualizuj tam więcej dniówek. Możliwe, że klient nie będzie w ogóle tego chciał albo poprosi o.

**[Janusz Bossak]:** No ile chcecie.

**[Kamil Dubaniowski]:** Czyli, że na zaplecze Jeszcze raz? To ta.

**[Janusz Bossak]:** Ile tych dniówek?

**[Kamil Dubaniowski]:** No ja dałem 4 chyba aktualnie tak.

**[Damian Kaminski]:** Znaczy.

**[Kamil Dubaniowski]:** Ania dała 2 4.

**[Lukasz Bott]:** A ja myślę, że to jest na tyle porąbane, nawet jeżeli byśmy przyjęli jakiś mwp Zero pół tak no mimo wszystko to jest grzebanie.

**[Damian Kaminski]:** 4 to jest jak dla mnie bez przyjmowania wartości. A jak teraz my jeszcze będziemy siedzieć w grzebać w przyjmowaniu wartości?

**[Lukasz Bott]:** Tak jakieś tam.

**[Damian Kaminski]:** No nie wiem, ja bym to tak tanie nie dawał.

**[Janusz Bossak]:** Ja to cofam do poprawy. Do was prośba jest o nie wiem kto to dostanie, że spojrzy chyba ania dostanie tak.

**[Lukasz Bott]:** No ale ja nie nie brało udziału w której bezpłatnie.

**[Kamil Dubaniowski]:** To ja poproszę. Ja mam admina na strefę się to ja przynajmniej sobie to ze względu.

**[Janusz Bossak]:** Tak jest ania, czego ja jesteś dodany? Nie, nie jesteś dodany już się dodaje do słowa. Właścicieli Kamil. Chyba niebieskim prośba, żebyś wtedy.

**[Kamil Dubaniowski]:** Pierwsza bardziej biznesowo zostawię to mania tam była.

**[Janusz Bossak]:** Michałek koncepcie techniczne to są można przekopiować do tych technicznych, a biznesowo w tej pierwszym okienku tam nie. No dobra, no to chyba mamy. W razie 2 godziny 3 minuty go damy.

**[Damian Kaminski]:** No właśnie dobra, ja idę coś jeszcze zrobić.

**[Janusz Bossak]:** Dobra idę. Razie.

**[Lukasz Bott]:** No właśnie.

**[Janusz Bossak]:** Zatrzymano transkrypcję


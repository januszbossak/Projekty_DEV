Data spotkania: 18 listopada 2025

**Janusz Bossak**: Rozmawialiśmy właśnie na temat tych filtrów użytkownika. Temat jest dużo bardziej złożony, niż mi się wczoraj wydawało. Jest kilka rzeczy do poprawienia, powiedzmy wizualnie, co da się zrobić w miarę sensownie. Natomiast Piotr zwrócił uwagę na problemy wydajnościowe i na to, że do wielu rzeczy podeszliśmy totalnie błędnie. Jak chociażby wyświetlanie imion i nazwisk w filtrze typu "nazwisko". Te nazwiska są brane ze wszystkiego, co jest wyświetlane, czyli jedziemy po bazie danych po jakimś polu tekstowym i wyświetlamy.

**Mateusz Kisiel**: Takie pola wyboru często są limitowane do 20 opcji. Z tego, co pamiętam, nie pobieramy wszystkich danych, tylko pobieramy 20 pierwszych.

**Janusz Bossak**: Tak, ale wybieramy spośród miliona, które potencjalnie mamy w raporcie, i to niezaindeksowanych. A jeszcze jest tak zrobione, że jak jest na przykład nazwisko "Kamiński", to w tej chwili jak wpiszesz "ami", to też szuka. Wydajnościowo to jest po prostu zabójstwo dla systemu. Szukanie po nieindeksowanym polu... Prośba do was, ja wam podeślę za chwilę to nagranie. Macie dostęp do spotkania Rady Deweloperów? Tam jest to nagranie i jest tam dużo na ten temat. Piotr sugeruje użyć indeksów na tych polach. Taki mechanizm był kiedyś przygotowywany i nie został rozwinięty, aczkolwiek jego zalążki istnieją i to trzeba będzie rozwinąć. Chciałbym, żeby w tym obszarze rzeczy były pokazywane prawidłowo, mówię o polach tekstowych.

Potem jest problem z polem typu słownikowego. Niby jest fajniejsze, bo jest osłownikowane, ale też nie do końca wiadomo, co właściwie wyświetlić w filtrze. Mamy dwa przypadki. Jeden, gdzie w słowniku jest tylko kilka pozycji, na przykład jakieś kategorie A, B, C, D. Wtedy jest sens wyświetlić te cztery kategorie, nawet jeżeli którejś z nich nie ma w danych raportu. Z drugiej strony, jeżeli słownik to na przykład słownik klientów, który zawiera 10 000 pozycji w naszym AMODIT-owym słowniku, a na raporcie wyświetlamy 5 klientów, to po co mi w filtrze 10 000 pozycji, skoro mam 5 w tym raporcie? To są dwie sprzeczne sytuacje, ale musimy je jakoś ogarnąć.

**Mateusz Kisiel**: To obecnie która opcja jest domyślna?

**Janusz Bossak**: Teoretycznie ta pierwsza, czyli wyświetlamy to, co jest w raporcie. Ale obecnie wyświetlamy to jeszcze źle. To jest związane z `DISTINCT`, o którym mówiła gdzieś Ania. Jeżeli wśród pierwszych 20 wyników będziesz miał 20 razy "część A", to dostaniesz jedną pozycję w filtrze o nazwie "część A", a nie będzie w ogóle pozycji B, C i D, mimo że dalej gdzieś w raporcie występują.

**Mateusz Kisiel**: Tak, to trzeba w SQL robić `DISTINCT`.

**Janusz Bossak**: Tak, i to jest rzecz do natychmiastowego poprawienia. Przy czym to poprawi trochę, że będzie się lepiej wyświetlało, ale nie do końca nadal dobrze, bo może być tych części więcej niż 20, które w tej chwili w filtrze wypisujemy. Można sobie z tym poradzić, wpisując jakiś fragment i wtedy pojawiają się następne. Pytanie, jak to sensownie zrobić. Natomiast to nie chroni nas przed problemem wydajnościowym, bo czytamy z danych, które idą już do raportu. Nie wiem, jak to jest w sumie robione, bo jeżeli raport miałby 10 000 pozycji, to my na backendzie z tych 10 000 pozycji będziemy robili `DISTINCT`.

**Mateusz Kisiel**: Nie jestem tego pewien, ale wydaje mi się, że to jest sprawdzane na frontendzie, jakie są dane w raporcie i na podstawie tego jest jakieś zawężanie, ale to trzeba sprawdzić. Ogólnie większość tych filtrów działa w ten sposób, że idzie dodatkowe zapytanie raportowe. Czyli jak dodasz jakieś pole tekstowe, które ma ileś tam opcji, to idzie po prostu dodatkowy request i powstaje nowy mini-raport z tym polem.

**Janusz Bossak**: Oczywiście, dopytujemy się do backendu.

**Mateusz Kisiel**: Jest też taka sytuacja, że jak mamy tabelę, to w tabeli jest paginacja, więc mamy tam pierwsze 50 pozycji. Jeżeli chcemy mieć wszystkie opcje do wyboru, to nie możemy brać ich tylko z tej pierwszej strony, tylko musimy brać z całości. I żeby brać z całości, właśnie po to chyba idzie to nowe zapytanie.

**Janusz Bossak**: OK. W pierwszej kolejności prosiłbym, żebyście wysłuchali tego 30-minutowego spotkania Rady Deweloperów. Żebyście obaj wysłuchali go ze zrozumieniem, zwłaszcza części, która dotyczy tych filtrów użytkownika i w szczególności elementów wydajnościowych, bo chciałbym, żebyśmy w którymś momencie do tego doszli. Na razie, w pierwszym etapie porządkowania tych filtrów, nie będziemy zbyt mocno walczyć z wydajnością. Zostawimy to na drugą turę. Teraz chciałbym uporządkować je od strony wyglądu i domyślnego zachowania w różnych okolicznościach. Będą to bardziej prace po stronie frontendu i niektóre, jak to z `DISTINCT`, po stronie backendu, ale jeszcze bez głębokich zmian, o których mówi Piotr na tym spotkaniu.

**Mateusz Kisiel**: Czy tak naprawdę ta zmiana z `DISTINCT` nie jest frontendowa? My wysyłamy request z nową definicją raportu do backendu i backend to potem zwraca. Czyli po prostu trzeba dołożyć ten `DISTINCT` w requeście, który idzie z frontendu.

**Janusz Bossak**: Przemek, ty wiesz, o czym my mówimy?

**Przemysław Rogaś**: Poniekąd, ale nie do końca.

**Janusz Bossak**: Dobra, już postaram się pokazać. Mamy taki raport, który się nazywa "Sprzedaż". To jest świetny przykład. Legenda po prawej stronie pokazuje "AMODIT", "BRP", "PROG", bo takie występują tutaj. Ale filtr pokazuje "AMODIT", "BRP" i tyle. A jak wpiszę "ER", to nic nie ma. To jest pierwsza rzecz do poprawienia. Legenda to widzi, a filtr nie.

**Mateusz Kisiel**: Dziwi mnie, że to teraz wyszło. To było testowane, powinno wyjść wcześniej. Myślę, że to mogło kiedyś działać.

**Janusz Bossak**: Sprawdziliśmy to z Anią w którymś momencie i chodzi o to, że w pierwszych 20 wynikach, ale nie agregatach, tylko danych źródłowych, jest "AMODIT" i "BRP", a "PROG" pojawia się dalej niż w pierwszych 20. To jest pierwsza rzecz na backendzie do poprawienia, żeby to się tutaj przynajmniej pojawiało. Dla użytkownika jest to zupełnie niezrozumiałe, że raport wie o tym, a filtr nie. Mam kilkanaście takich mniejszych i większych rzeczy. Chciałbym, Przemek, z tobą popracować, a w niektórych przypadkach, jak ten, poprosić Mateusza, żeby na backendzie poprawił pewne tematy.

**Mateusz Kisiel**: Tak jak mówię, to jest przypadek też dla frontendu. Trzeba po prostu wysłać w requeście definicję raportu, która dodatkowo robi `DISTINCT`. W tym momencie jest przesyłane w takiej postaci jak w tabeli i przez to jakaś paginacja może się psuć.

**Janusz Bossak**: Tam jest chyba na siłę wpisane 20.

**Mateusz Kisiel**: Być może, to jest możliwe.

**Janusz Bossak**: Tylko że to powinien być `SELECT DISTINCT`. U mnie to jest na backendzie, nie na frontendzie.

**Mateusz Kisiel**: Backend zwraca to, o co poprosi front.

**Przemysław Rogaś**: Z tego, co ja rozumiem, ma to sens jedynie tam, gdzie jest paginacja, jak w tabeli, a tak to nie powinno być żadnego limitu.

**Mateusz Kisiel**: Myślę, że nawet dla tabel chyba nie ma to sensu.

**Przemysław Rogaś**: Fakt, bo będziesz szukał tylko po jednej stronie, to bez sensu.

**Przemysław Rogaś**: Ogólnie takie zadania ja bym zgłaszał najpierw na frontend. I na przykład, jeżeli ja stwierdzę, że to jest jednak na backendzie, to wtedy ja zgłaszam to na backend.

**Janusz Bossak**: Dobra, ja mam listę use case'ów spisanych, które jeszcze nie są PBI-ami na backlogu. Chciałbym pracować z tobą bardziej dynamicznie, więcej mówić, o co mi chodzi, i po kolei byśmy rzeczy naprawiali. Będę to też starał się spisywać na backlogu. Jest robiony do tego epic i tam będę podpinał wszystkie rzeczy związane z naprawą kwestii filtrów użytkownika, zarówno po stronie używania, jak i tworzenia. Na przykład domyślne ustawienie wartości i inne drobne tematy. Sprawdziłeś coś, Mateusz?

**Mateusz Kisiel**: [problemy z internetem]

**Janusz Bossak**: Coś cię wycięło, sam się dołączyłeś.

**Mateusz Kisiel**: Nie mam internetu w laptopie z jakiegoś powodu, chyba Wi-Fi się psuje. U was działa, więc to dziwne. Z telefonu się teraz łączę. Halo?

**Janusz Bossak**: Słychać cię.

**Przemysław Rogaś**: Trochę słabo cię słychać.

**Mateusz Kisiel**: OK, teraz lepiej?

**Janusz Bossak**: Tak.

**Przemysław Rogaś**: Lepiej, ale cicho.

**Mateusz Kisiel**: Dobra, teraz powinno być dobrze. Mogę pokazać to miejsce, gdzie są pobierane te wartości. Jest tutaj funkcja `getPossibleValues`. Ona pobiera możliwe wartości. Przesyłamy definicję takiego nowego, tymczasowego raportu, z którego są brane te dane. I tutaj widzimy, że jest ustawiony limit na 20. Być może trzeba by tu dołożyć agregację.

**Janusz Bossak**: Ale to pobiera dane, które już są po stronie frontendu, tak?

**Mateusz Kisiel**: Nie, to jest dodatkowe zapytanie do backendu, taki mini-raport na potrzeby tego, co będzie w polu wyboru. Tak jak miałeś dwie wartości zamiast czterech, to dlatego, że limit 20 wziął tylko 20 elementów. Tymczasowo zadziałałoby, gdyby zrobić tu jakiegoś `DISTINCT`. Trzeba zobaczyć, jak to jest zrobione.

**Janusz Bossak**: To trzeba będzie na pewno poprawić.

**Mateusz Kisiel**: Tak, `DISTINCT` jest robiony po stronie frontendu, a nie po stronie backendu. I to jest problem.

**Janusz Bossak**: OK.

**Przemysław Rogaś**: Czyli ten limit 20 to nie jest limit rekordów w raporcie, tylko faktycznie limit elementów w filtrach?

**Mateusz Kisiel**: Ten limit 20, który jest tu ustawiony, to jest limit, który idzie do backendu. Backend bierze 20 elementów, a potem dodatkowo jest robiony `DISTINCT` po stronie frontendu. I przez to jest problem. Powinno to być robione po stronie backendu.

**Janusz Bossak**: A możesz zobaczyć, jak jest zrobiona legenda, że ma cztery wartości? To jest ten sam przypadek, dokładnie ten sam.

**Przemysław Rogaś**: Ogólnie legenda chyba też jest źle zrobiona, na przykład dla tabel, bo jest brana pod uwagę na podstawie danych, które są na frontendzie. Czyli jak masz otwartą pierwszą stronę w tabeli, to bierze tylko dla pierwszej strony. Później jak włączysz drugą, to legenda ci się zmieni.

**Mateusz Kisiel**: Prawdopodobnie legenda bierze po prostu dane z raportu, czyli jak mamy tabelkę, to będzie brało tylko z tej otwartej strony.

**Janusz Bossak**: Tak jak Przemek mówi, to też niedobre rozwiązanie. Trzeba to będzie wszystko ujednolicić. Bardzo nieeleganckie, a proste rozwiązanie to zamiast 20 wpisać 200 i liczyć, że w pierwszych 200 będzie więcej.

**Mateusz Kisiel**: Nie, nie.

**Przemysław Rogaś**: A nawet jak jest 20, to da się to potem doładować, jak chcesz więcej zobaczyć?

**Mateusz Kisiel**: Nie, tutaj w filtrach nie ma takiej opcji. Chociaż wydaje mi się, że jak się scrollem przewija w dół, to chyba się ładuje więcej wartości. A może nie.

**Janusz Bossak**: Nie, nie.

**Przemysław Rogaś**: Trzeba wyszukać.

**Janusz Bossak**: Dopiero jak wpiszesz "erp". Mało tego, jak go wpiszesz, to on się wyszuka, ale znikają mi wtedy "BRP" i "AMODIT", czyli ich nie widzę. Widzę tylko ten, który znalazłem.

**Mateusz Kisiel**: Tak, tak, to jest do poprawki. Tego `DISTINCT` nie można robić po stronie frontendu.

**Janusz Bossak**: Dobra, trzeba wymyślić, jak dostać 20 unikalnych wartości. To będzie pierwsza taka poprawka. Także spokojnie możesz już sobie zaplanować pracę nad tym.

**Przemysław Rogaś**: Chyba Mateusz to weźmie w całości.

**Mateusz Kisiel**: Tak, ja to zrobię.

**Janusz Bossak**: Dobrze. Teraz wam pokażę, co sobie rozpisałem. Mam tych przypadków użycia sporo. [Janusz pokazuje ekran] Tu mam różne przypadki użycia rozpisane. Będziemy na podstawie tego pracować, będzie wiadomo, co jest do zrobienia. Jest tu np. filtrowanie krótkiej i długiej listy – to, o czym teraz rozmawiamy. Obsługa "zaznacz wszystko", bo to też teraz działa źle. Zaznacza 20, jeśli jest więcej, a użytkownik myśli, że zaznaczył wszystko. Powinno być "zaznacz widoczne", jeśli jest ich więcej niż 20.

Mamy też wybór operatora tekstowego, żeby domyślnie był ustawiony na "zawiera". Ale rozmowa na Radzie Deweloperów trochę zmienia moje podejście. Piotr mocno "nakrzyczał" od strony wydajnościowej. Musimy zrobić indeksowanie, żeby można było po tym polu tekstowym wybierać, nie zabijając bazy danych, ale to zostawimy sobie na później.

**Przemysław Rogaś**: Wracając do "zaznacz wszystko", w jakim kierunku pójdziemy? Mam wrażenie, że efekt "zaznacz wszystko" będzie taki sam jak niezaznaczenie niczego.

**Mateusz Kisiel**: Chyba zmiana tekstu na "zaznacz widoczne".

**Janusz Bossak**: Tak, powinno być "zaznacz widoczne". Udostępnię wam to, żebyście mogli sobie przeglądać.

Potem jest temat daty, tu jest dużo do uporządkowania. Mamy teraz dużo operatorów na dacie, takie jawne jak "bieżący miesiąc", "poprzedni miesiąc", które nie wymagają wybierania daty. Z punktu widzenia biznesowego są ważniejsze i powinny być jako pierwsze. Najczęściej użytkownik będzie wybierał "w zeszłym miesiącu", "w tym miesiącu", "poprzednie 30 dni", "poprzednie 90 dni" itd. Dopiero niżej, dla bardziej zaawansowanych, będzie "nie wcześniej niż", "nie później niż", czy zakres od-do. To jest tylko uporządkowanie kolejności i nadanie odpowiednich nazw.

Potem mamy komunikat o wymaganych filtrach. To do ciebie, Przemek, jako do UX-owca. Mamy tzw. "empty state screen", czyli sytuację, w której nie ma danych albo wymagane jest podanie filtrów. Musimy się zastanowić, jak to ładnie zrobić wizualnie, żeby informować użytkownika, że musi najpierw podać np. obszar czy projekt, żeby cokolwiek zobaczyć.

Z tego wyniknęło też ogarnięcie "empty state screen" dla wszystkich typów raportów. Wchodzimy, mamy raport tabelaryczny, ale nie mamy danych i wypisuje "brak danych" na środku pustego ekranu. Nawet nie wiadomo, jaki to jest raport.

**Przemysław Rogaś**: Masz jakiś pomysł na to? Kristina dostarczyła ilustracje, można ich użyć.

**Janusz Bossak**: Albo ilustracje, albo takie mockupowe, żeby nie było pusto. Na przykład wykres, który jest pusty. Z tabelką jest najłatwiej, bo można wyświetlić kolumny i napisać w pierwszym wierszu "brak danych". I zachęcić do akcji, jeśli jest przycisk "Dodaj nowy". Mogłoby być na środku ekranu: "W tym raporcie nie masz jeszcze żadnych danych. Wprowadź pierwszą umowę". Musielibyśmy nad tymi "empty state screens" popracować. Tutaj odwołam się do twojej wyobraźni i umiejętności projektowania.

Jak widać, jest tego trochę. Po dzisiejszym spotkaniu z Piotrem postaram się dopisać kolejne use case'y, żebyśmy mieli komplet.

**Mateusz Kisiel**: A ten raport, który pokazywałeś, jest na jakiejś witrynie testowej czy na `strefa.dev`?

**Janusz Bossak**: Jest na `strefa.amodit.com`, nazywa się "Sprzedaż 2025 per prod". Jest udostępniony dla wybranych osób.

**Mateusz Kisiel**: Nieważne. Chciałem zobaczyć na testowej. Rzeczywiście, nie ma opcji dodania `DISTINCT`, więc trzeba to dołożyć do backendu.

**Janusz Bossak**: OK. Czyli w tym, co pokazywałeś, w wierszu, gdzie jest agregacja, trzeba dodać `DISTINCT`.

**Mateusz Kisiel**: Będzie dodatkowa opcja włączenia `DISTINCT`.

**Janusz Bossak**: I na backendzie wtedy `DISTINCT` zwraca te wartości, OK. Dobra, słuchajcie, na razie tyle. Będę sukcesywnie przerzucał te rzeczy do backlogu. Przemek, czego byś potrzebował ode mnie, żeby zacząć coś robić?

**Przemysław Rogaś**: Jakieś pierwsze zadanie. Jeśli nie masz rozpisanych, to pewnie są jakieś błędy do poprawienia, cokolwiek do zrobienia.

**Janusz Bossak**: Dobra, będę ci wrzucał zadania. Zacznijmy od porządkowania pola "Data", z tymi nazwami, bo to jest akurat tylko robota po stronie frontendu.

**Mateusz Kisiel**: Na tę poprawkę z filtrem zrobić jakiegoś buga?

**Janusz Bossak**: Tak, chyba nawet jest. Chociaż nie mam go zidentyfikowanego, więc możliwe, że nie ma.

**Mateusz Kisiel**: To zrobię nowego. Jak się powtórzy, to się usunie tego pierwszego.

**Janusz Bossak**: Podepnij go pod numerek 20153. To jest taki ogólny ficzer "Ulepszanie filtrów użytkownika". Żeby mi to nie zginęło. Pod to będę też podpinał zadania dla ciebie, Przemek.

**Przemysław Rogaś**: Dobra.

**Janusz Bossak**: OK, dobra, to tyle na razie. Dzięki bardzo.

**Mateusz Kisiel**: Dzięki, cześć.

**Przemysław Rogaś**: Na razie, dzięki.

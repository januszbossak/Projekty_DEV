**Data spotkania:** 21 listopada 2025, 09:21 AM

**Janusz Bossak:** No dobra, to jesteśmy. Co mamy? Mamy stan sprintu.

**Kamil Dubaniowski:** Zacznę od tego, co podsumowałem na czacie. Piotrek kończy teraz temat "Ametystowy", więc nie chcę go wytrącać, ale deklarował, że dzisiaj to skończy. Od przyszłego tygodnia chciałbym, żeby zbudował strukturę pod **JRWA** [Jednolity Rzeczowy Wykaz Akt] na wzór tego, co było robione z **GUS TERYT**, tak jak się umówiliśmy. Nie wiem, czy będzie potrzeba, aby to zadanie w dalszym kroku przejął Mariusz, chociaż spodziewałem się, że Piotrek to zrobi od ręki przy okazji – czyli możliwość podpięcia tego źródła w polu, odnośnik do źródła zewnętrznego i zwrotka JSON wybranej pozycji. Na tym zamykam ten sprint, nic więcej nie planuję, bo mamy tydzień i nic więcej się nie uda. Drugi krok to pewnie interfejs do zarządzania tym widokiem, żeby można było te katalogi z poziomu **AMODIT-a** dodawać i edytować.

**Damian Kamiński:** Jakie katalogi? Jeszcze raz, powtórzyć coś?

**Kamil Dubaniowski:** Katalogi, cała struktura. Wczoraj miałem spotkanie z **LOT-em** [Polskie Linie Lotnicze], konsultanci mieli status. Na koniec dopytałem o temat uprawnień. Padło hasło od osoby zarządzającej schematem w LOT, że on nie bierze na siebie odpowiedzialności przypisywania konkretnych klas do działów. Nie chce sytuacji, że ktoś nie będzie mógł użyć jakiejś klasy, bo on jej nie przypisał, więc prawdopodobnie wszyscy będą widzieć wszystkie klasy. Czyli kwestia uprawnień na ten moment nam odpada. Docelowo pewnie przy innych projektach klient może mieć zupełnie inne wymagania, ale w tym projekcie, jeśli uznamy, że nie mamy czasu, to jest duża szansa, że nie będziemy musieli tego robić. Oni mają to jeszcze wewnętrznie przedyskutować.

**Damian Kamiński:** Widziałbym to tak: jeśli jesteśmy w temacie, to warto by było to rozpisać, ale tego po prostu nie robić. Doświadczenia, które tu zbierzemy, posłużą jako propozycja, gdy przyjdzie następny klient i kolejnym wdrożeniem **AMODIT-a** oraz licencjami zasponsoruje rozwój w tym zakresie. Skoro teraz jesteśmy mocno w temacie, warto wykorzystać ten pęd.

**Kamil Dubaniowski:** To nie jest nic skomplikowanego, tym bardziej że robimy dedykowane rozwiązanie, będą dedykowane tabele. Powstałaby dedykowana tabela do uprawnień, gdzie przypisujesz działy, które mają mieć dostęp do danego katalogu **JRWA**. Ale skoro klient zaznacza, że niekoniecznie widzi taką potrzebę, to nie wiem, czy jest sens robić to w tym projekcie.

**Damian Kamiński:** Zgadzam się, jak nie widzi potrzeby, to po co mamy to robić? Tylko że działy bym od razu podważył, bo w dziale może być dyrektor i my. Janusz niekoniecznie miałby te same uprawnienia co my. Działy odpadają, nasze grupy są bardziej elastyczne, ale nie mówię, że są jedynym rozwiązaniem.

**Kamil Dubaniowski:** Czy grupy wymagają wtedy konfiguracji? Zazwyczaj jest dziedziczenie. Dlatego tego nie ruszam, bo nie mamy konkretnego przypadku. Nie ma co teraz wymyślać na siłę, później przyjdzie klient i okaże się, że to i tak nie spełnia wymagań. Zobaczymy, z czym do nas wrócą. Cel na ten moment jest taki: mamy źródło danych takie jak **GUS TERYT**, mamy możliwość podpięcia go do pola "Źródło/Odnośnik".

**Kamil Dubaniowski:** Zewnętrzny panel na formularzu to już przyszły sprint. Pewnie nawet więcej niż jeden, bo będzie tam sporo akcji do zorganizowania.

**Łukasz Bott:** Czyli, jeżeli dobrze zrozumiałem, nie idziemy w żadne rejestry, procesy i podprocesy, tylko budujemy dedykowane **źródło danych**?

**Kamil Dubaniowski:** Nie, nie. Dedykowana tabela, dedykowane źródło na podstawie naszej tabeli **AMODIT-owej**, tak jak z **GUS TERYT**. Konsultant ostatecznie podpina to pod "Odnośnik do źródła zewnętrznego". Ty jako pracownik merytoryczny wyszukujesz odpowiedni katalog wpisując symbol lub nazwę. Jak coś wybierzesz, to w wartości tego pola – jeśli będziesz chciał użyć tego w kodzie reguł – dostajesz JSON-a ze wszystkimi informacjami o wybranej pozycji.

**Łukasz Bott:** To jest gites.

**Kamil Dubaniowski:** Czyli będziesz miał kategorię archiwalną w formie JSON-a i możesz to sobie potem rozparcelować na sprawę, na poszczególne pola. Czyli na przykład przepisać z tego JSON-a, że "Kategoria archiwalna wybranej klasy to..." i że "przechowujemy tę sprawę elektronicznie", bo tak wynika z wybranej klasy. Jeśli dana klasa będzie miała opis, możemy go też zwrócić w tym JSON-ie i możesz go wyświetlić w _tooltipie_ albo w polu _static text_, żeby pokazać pracownikowi merytorycznemu opis tego, co wybrał.

**Łukasz Bott:** Jasne. Pomyślałem sobie o czymś takim, żeby jako opcję zwracać gotowe, sformatowane atrybuty, np. w postaci tabelarycznej "nazwa atrybutu – wartość" dla danej klasy. Tak, żeby można było to szybko wyświetlić, np. w polu statycznym, bez wpisania reguły i formatowania, bez dłubania w HTML-u. Chodzi o przyjazną wizualizację tego JSON-a.

**Kamil Dubaniowski:** Wydaje mi się, że i tak będziemy musieli zapisać to w pojedynczych polach na formularzu, np. kategoria archiwalna, bo to będzie potrzebne do raportów albo kodu reguł.

**Janusz Bossak:** Mamy tę notację z kropką?

**Kamil Dubaniowski:** Jest. **Bracket** [nawias] z kropką. Wtedy odnosisz się do konkretnej wartości.

**Łukasz Bott:** Czyli to by zwracało obiekt dla danej klasy i tam jest skończona liczba parametrów opisujących dany węzeł?

**Kamil Dubaniowski:** Tak, my będziemy tym zarządzać i tym, co będzie w opisie. Lista jest skończona.

**Janusz Bossak:** W polu "Odnośnik", jeżeli coś wybierzesz i pole nazywa się np. "Pole1", to robisz to w nawiasach kwadratowych: `[Pole1].Numer`. I tak samo tutaj musi to działać. W tym polu, gdzie wybieramy **JRWA**, mamy wszystkie parametry dostępne po kropce. Powiedzmy, że pole nazywa się "JRWA". Mam nawiasy kwadratowe `[JRWA].KlasaArchiwalna`, `[JRWA].DataObowiązywania`, `[JRWA].Nazwa`, `[JRWA].Symbol`. Mogę to użyć tam, gdzie chcę. Nie trzeba obsługiwać żadnych JSON-ów. Jak ktoś będzie potrzebował JSON-a, to zwróci JSON-a, ale najprościej będzie przez notację kropki.

**Łukasz Bott:** OK, nazwa atrybutu.

**Kamil Dubaniowski:** To będę robił.

**Damian Kamiński:** Mogę szybko powiedzieć status i się przełączyć, bo mamy daily. Wczoraj udało się odpalić komunikator, dostałem rano potwierdzenie, że im działa, więc czekamy na uwagi. Repozytorium plików: Ania dzisiaj przygotuje pierwszy endpoint, więc będę prosił Filipa, żeby się już pod niego podpinał. Będzie już pierwsze tworzenie folderów. Kontynuujemy w przyszłym tygodniu. Jedyne ryzyko i bloker to sytuacja Adriana – czuję, że w tym sprincie do nas nie dołączy i nie podgonimy backendu. Nie rozpoczęliśmy jeszcze procesu certyfikacji, jesteśmy na etapie rejestracji.

**Janusz Bossak:** Mówisz o tym na **macOS**?

**Damian Kamiński:** Tak. Zaraz jeszcze dopytam, bo rozumiem, że Kamil teraz robi ostatnie poprawki UI-owe i teoretycznie dzisiaj mamy gotowca, tylko niecertyfikowanego?

**Kamil Dubaniowski:** Tak, można to zainstalować, tylko będą musieli zaznaczyć, że zgadzają się na instalację [z nieznanego źródła].

**Damian Kamiński:** Zaproponuję Filipowi, że o ile ktoś posiada Maca, ale nie jest to dyrektor (bo z dyrektorem nie będziemy tak działać), to przekażemy to w poniedziałek lub wtorek. Niech ktoś to przejdzie z działu IT. Jeśli okaże się, że to tylko dyrektor, to takie obejście bez certyfikacji źle wygląda.

**Janusz Bossak:** Musimy tę certyfikację przejść, ale można tak zrobić do testów. Oni mają świadomość, że to jest przed certyfikacją.

**Damian Kamiński:** OK, dopytam czy jest ich więcej. Przełączam się na daily.

**Łukasz Bott:** Status co do **LOT-u**. Łukasz Brocki jest zaangażowany w kwestie integracji z dwoma nowymi kurierami: **UPS** i **Global Express**. Wszystkie dane mamy pozyskane, Global Express chyba uda się zrobić jeszcze w tym sprincie. Łukasz siedzi też przy tym Comarch Hubie. Po weekendzie, we wtorek, mam spotkanie techniczne z LOT-em, żeby dogadać pozostałe integracje związane z systemami **SIEM** [Security Information and Event Management], czyli monitorowanie zdarzeń. Mam pomysł, żebyśmy tam nic nie robili, tylko wskazali im, w co się podłączyć. Logi systemowe można zwrócić w ustandaryzowanym formacie. Pytam, czy można się bezpośrednio łączyć, bo systemy SIEM nasłuchują na porcie sieciowym, więc można wysłać to bezpośrednio po protokole. Chcę ustalić, na ile my musimy coś robić, a na ile oni sami sobie poradzą.

**Kamil Dubaniowski:** Wracając do mnie. Zasypałem wczoraj chłopaków tematami dotyczącymi edytora graficznego formularza i listy pól, żeby zamykać temat. Sporo tego wyszło – bugi, zmiany wizualne i moje pomysły. Wrzuciłem też temat porządkowania pola typu tabela, bo trochę się rozjechało wizualnie i funkcjonalnie – teraz import mamy w dwóch miejscach przez to nowe zgłoszenie. Nie mam kim tego zrobić, bo Ania była przypisana, ale ze względu na to, że Adrian nie udziela się w repozytorium, nie chcę jej stamtąd wyciągać. Można to zrobić w przyszłym sprincie, to nie jest kluczowe dla klienta, ale wizualnie wygląda słabo (ikonki posklejane z tekstem).

**Janusz Bossak:** Mariuszowi nie można tego dać?

**Kamil Dubaniowski:** Zobaczymy, jak pójdzie temat **JRWA**. Jeśli Piotrek weźmie to w całości na siebie, to w przyszłym tygodniu mógłbym dać to Mariuszowi. Mariusz mocno zaangażował się w pracę, kończy tematy z komentarzami z zeszłego sprintu. Skoro Piotrek będzie robił pierwsze dni przy JRWA, a może nawet całość, to można to przełożyć na Mariusza.

**Janusz Bossak:** Pomyślałem o tych poprawkach w edytorze formularza. Zgłaszali to też Mateusz i Daniel, my sami też o tym mówiliśmy – podgląd na reguły. Czy jednak tego nie zrobić? Klikam na pole i w prawym panelu jest nowa sekcja "Reguły". Powinna się pojawić przynajmniej lista nazw reguł, w których pole jest użyte. Jak kliknę, to się rozwinie. To byłby duży krok naprzód. Tak samo w regułach tabeli – klikając w pole "Tabela", mógłbym zobaczyć regułę tabeli.

**Kamil Dubaniowski:** Reguły tabeli, odkąd weszła nowa lista pól, w ogóle są niedostępne nigdzie.

**Janusz Bossak:** No właśnie, więc to trzeba naprawić.

**Kamil Dubaniowski:** To i dodawanie nowej sekcji z poziomu listy pól. To są jeszcze dwa tematy rozpisane. Na dodawanie sekcji z poziomu listy nie mam nawet pomysłu, bo tam używamy tabeli Ant Design, która ma sporo ograniczeń.

**Janusz Bossak:** Ale wiesz, że my teoretycznie nie mamy czegoś takiego jak sekcja bez pól?

**Kamil Dubaniowski:** Po stronie frontendu jest to obsłużone – wyświetlamy taką sekcję z komunikatem, że nie zawiera pól. Po stronie edytora graficznego też da się dodać pustą sekcję i dopiero później dorzucać pola.

**Janusz Bossak:** Trzeba by zmienić logikę po stronie backendu, żeby te sekcje miały swoją reprezentację w bazie danych, a nie tylko redundantny zapis w każdym rekordzie definicji pola. Ale to jest większa zmiana.

**Kamil Dubaniowski:** Zgłaszałem te poprawki wizualne do zaokrągleń – to temat poboczny, wszędzie weszły te "ósemki" [radius 8px], Filip wie, że stosujemy "piątkę", ale na formularzu nadal jest trójka. Tego bym na razie nie ruszał. Jeszcze podświetlenia pól – Przemek będzie to uspójniał. Pola typu **Search** na liście pól w edytorze mają bardzo mocne podświetlenie, a lista rozwijana obok ma inny kolor i cień.

**Janusz Bossak:** Mam problem czasowy z **Backlogiem** zmian na module raportowym. Czego się tam nie dotknie, to wymaga gruntownej przebudowy. Mateusz zabrał się za indeksy i to jest jeden z wielu grubszych tematów. Trzeba zrobić dobrą logikę na backendzie, bo bez tego poprawki wizualne mają mniejszy sens. Dałem Szymkowi poprawki w związku z operatorem daty, żeby je uporządkował. Denerwuje mnie, że operatory są nielogiczne – raz "zeszły tydzień", a potem "poprzedni miesiąc". Powinny być najpierw te operatory, w których nie trzeba nic wpisywać: "poprzedni tydzień", "ostatnie 7 dni", "ostatnie 30 dni". Ludzie będą z nich częściej korzystać niż z "nie wcześniej niż data...". Przemek to robi.

**Janusz Bossak:** Wracając do zespołów. Wydaje mi się, że powinniśmy wrócić do koncepcji **Zespołów Zadaniowych**. Zespół dostaje cel na sprint czy kwartał i się z niego wywiązuje. Na przykład w zespole jest Przemek, Rogaś, Ania. Wychodzi na to, że mamy dwa zespoły deweloperskie backendowe i jeden frontendowy. Mamy trzy testerki, po jednej do każdego zespołu. Przykładowo Marek, będąc w zespole "Trust Center", zajmuje się głównie tym, ale robi też inne rzeczy. Zespół Mateusza mógłby zajmować się np. **OCR** i ogólnie AI. Prośba, żebyście pomyśleli, jak to widzicie.

**Łukasz Bott:** Wygląda na to, że tak. Będziemy odcinali.

**Janusz Bossak:** No to kończymy, dzięki bardzo.
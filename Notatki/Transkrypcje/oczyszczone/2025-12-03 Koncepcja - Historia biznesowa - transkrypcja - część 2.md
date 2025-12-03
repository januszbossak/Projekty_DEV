**Data spotkania:** 3 grudnia 2025, 10:16 - część 2

---

**Damian Kaminski:** No tak, ale jest zagregowana do tej jednej sprawy, bo to bym tak widział. Tak jak powiedziałeś o tym raporcie. Raport też musi być jakimś, załóżmy raport osadzony. No to wtedy CaseID powinien być w tym zdarzeniu przypisywany do sprawy głównej, która agreguje całą historię biznesową, niezależnie od historii poszczególnych spraw. Treść może być napisane, że przekazano do właściwego działu i utworzono kopię sprawy. I tu jest link do sprawy tej właściwej, która już to obsługuje, bo tam właśnie są różne procesy dla różnych działów. Ale jednym agregatem jest powiedzmy dany klient, czyli co z danym klientem, jaka korespondencja była prowadzona. Czyli stworzona przyszła korespondencja, została wysłana korespondencja, przyszła korespondencja, została wysłana korespondencja.

**Janusz Bossak:** Jak na to patrzę, to mam pytanie do Łukasza, bo możemy to w ogóle źle zrobiliśmy. Bo cała idea była taka, żeby to było niezwiązane ze sprawą. Znaczy.

**Damian Kaminski:** Ale jak to wtedy odfiltrować? W sensie i tak musisz to osadzić na jakiejś sprawie, która agreguje tą całą biznesową historię.

**Janusz Bossak:** No, ale mogę nad czymkolwiek to osadzać. I ideałem była tak.

**Lukasz Brocki:** Nie musi być bezpośrednio do sprawy i tyle.

**Janusz Bossak:** Może to zrobić w raporcie? Tak, ale właśnie rzeczywiście brakuje mi tutaj teraz, tak na to patrzę, tego spięcia. Bo w sumie ta historia biznesowa, ona jest troszkę takim odpowiednikiem właśnie tej nieszczęsnej teczki JRWA. Bo ja muszę to jakiś ciąg zdarzeń przypiąć, a teraz nie mam jak przypiąć tego do żadnego ciągu zdarzeń. To są jakieś oderwane.

**Damian Kaminski:** No nie wiem czy się z tobą zgadzam, bo i tak kontekst koniec końców jest taki, że ktoś ma ten byt kontrahenta. Chyba, że od tego odchodzimy za pośrednictwem źródeł, ale to dalej da się to zrobić jako zestawienie tabelaryczne, tylko wtedy musielibyśmy przygotowywać pod to pewnie dedykowane widoki.

**Janusz Bossak:** To jest chyba ten business subject? Tutaj jestem.

**Damian Kaminski:** Na przykład to może być to, na przykład to może być to.

**Janusz Bossak:** Tu powinno. Co to jest, Łukasz? Jakbyś mi przypomniał?

**Lukasz Brocki:** Na ten moment jest to tylko notatka. To nie jest z niczym powiązana bezpośrednio.

**Damian Kaminski:** No właśnie, to jest elastyczne. Dokładnie.

**Lukasz Brocki:** Też czego powinien dotyczyć ten event, ale to nie jest w żaden sposób wykorzystywane gdziekolwiek.

**Janusz Bossak:** No właśnie, i według mnie.

**Damian Kaminski:** Bardzo elastycznie do tego podeszliśmy.

**Janusz Bossak:** Tak, i teraz ten ID tym business subject, to jest właśnie to ID, którym ja myślę. Czyli takie ID tej wyższej sprawy.

**Damian Kaminski:** OK, ale to oznacza, że wyższej sprawy. Aha, wyższej sprawy, no dobrze. Tylko że ta ID niestety jest tak elastyczne, że jego typ, czyli to co jest tutaj, jest niezdefiniowany słownikiem po stronie kodu. Czyli jest jakieś ID, jest jakiś typ i to ty określasz, co to jest za ID, co to jest za typ. Nie, to nie jest skatalogowane, tak Łukasz, dobrze mówię?

**Lukasz Brocki:** Tak, nie jest w żaden sposób.

**Damian Kaminski:** Można by to skatalogować. I tu właśnie ewentualnie wtedy działanie serwisowe, gdy ktoś użył tego inaczej, to ustalamy, że katalogujemy to per user, per ID. I ewentualnie w przyszłości rozbudowujemy inne przypadki, tylko już zero co do zasady mamy tutaj.

**Janusz Bossak:** Ale to już może być.

**Damian Kaminski:** Systemem. No bo jakie ID tu powiedzmy wstawisz? Bo ID sprawy to rozumiem ID sprawy nadrzędnej, a to jest ID sprawy podrzędnej. To ID, które się zapisuje natywnie, więc można by szukać po tym. Ale jeśli nie jesteśmy w stanie chyba jednocześnie przypisać ID jeden i dwa, tego też nie mamy przypadku. Czyli możemy albo wybrać user, albo case. No nie jest to zrobione idealnie pod kątem wszechstronnym, ale jednocześnie jest to też bardzo elastyczne. Tylko jak ktoś chce tak zrobić i jak tego od razu nie wyprostujemy, to później będzie tylko ciężej. Pytanie, ostatecznie powinniśmy wejść od tyłu. Czego my oczekujemy od tej historii, gdzie my chcemy ją wyświetlać i w jakim kontekście? Bo jeśli mówisz, że nie tak.

**Janusz Bossak:** Znaczy.

**Damian Kaminski:** No to całość.

**Janusz Bossak:** Znaczy, OK. Dobra, po co? Jakby teraz jak na to patrzę, to mam wrażenie, że to źle zrobiliśmy. Znaczy źle w sensie przydatności dla Aliansów wtedy. Tak jak ja miałem w głowie rozumienie tego, jak rozmawiałem z Aliansem, bo to, co jest teraz zrobione, to jest w sumie to, co pokazujesz właśnie w prawym panelu w tej chwili. Bo to jest historia związana z tą sprawą przez to, że ma w bazie danych ten case. I to rozumiem, że to jest ten case, do której tworzę tą historię i mogę tworzyć dowolne zdarzenia, ale dla tej sprawy, tej konkretnej tej korespondencji przychodzącej, nie żadnej korespondencji wychodzącej ani czegokolwiek innego, co jest w innych procesach.

**Damian Kaminski:** Tak, ale może być kluczowe w twojej historii biznesowej tej korespondencji wychodzącej zdarzenie takie, że wysłał ktoś odpowiedź z korespondencji wychodzącej.

**Janusz Bossak:** Ale jak to zmapujesz z tą historią? W tej chwili nie ma takiej możliwości.

**Damian Kaminski:** No, po linked tworzysz. Historię tworzysz odpowiedź, ona się mapuje z przychodzącą. Tak naukowo, ale tak.

**Janusz Bossak:** No nie, bo tutaj chodziło o to, że tamtej historii. Znaczy inaczej, w tamtej sprawie, czyli korespondencji wychodzącej, musiałbyś wpisywać do historii biznesowej zdarzenie, że wysłano korespondencję. To złe słowo w tej sprawie, ale w rozumieniu w tej teczce sprawy, czyli różnym procesu. No mi to się akurat teraz, jak gadamy o tym JRWA przez ostatni miesiąc, to to się idealnie nadaje jakby. Historia biznesowa idealnie się nadaje pod JRWA, bo można by powiedzieć, że ta teczka sprawy właśnie.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** W rozumieniu JRWA to jest identyfikator dla nas. I jak tu byśmy zrobili ten subject ID, to powinna być dokładnie numer teczki sprawy. Czy to jest zdarzenie w tej teczce JRWA, czyli tej teczce, która zawiera wiele spraw amoditowych? Z korespondencji przychodzącej, z korespondencji wychodzącej, z jakichś tam innych dowolnych. I tak dalej. I wtedy ten subject ID jest wspólny. I wtedy nie ma znaczenia, czy to robisz właśnie z poziomu sprawy, którą widać tu po prawej stronie formularza ekranu korespondencji przychodzącej, czy to robisz z poziomu raportu. Na przykład powinno się dać raportować wszystkie zdarzenia biznesowe dla teczki sprawy o takim numerze. I to ten subject ID, to jest właśnie taki numer czy nazwa czy symbol.

**Damian Kaminski:** Tylko sam nie jest to wtedy, byśmy musieli zrobić, że to musi być skategoryzowane, że to ma być case ID tutaj. Bo dzisiaj tu możesz zdefiniować co chcesz, a to skutkuje, że ciężko to otworzyć tu, bo nie wiadomo co tu jest.

**Janusz Bossak:** Tak, dlatego.

**Damian Kaminski:** Tak.

**Janusz Bossak:** W moim przekonaniu teraz, jak patrzę z perspektywy tych wielu już miesięcy i ostatnich miesięcy związanych z JRWA, to to nie jest zrobione jakby optymalnie. Znaczy pomysł nie był optymalny.

**Damian Kaminski:** Nie, był jakimś pomysłem, po prostu niesprawdzonym w boju. Dopiero jak weszliśmy.

**Janusz Bossak:** Tak.

**Damian Kaminski:** No, ale mów.

**Janusz Bossak:** Chodzi mi o to, że teraz dlatego Rossmana. Jeżeli mielibyśmy coś robić, to może jeszcze jest czas, bo dopóty dopóki ktoś tego na siłę nie wykorzystuje. Nie wiem, jak jest z tą historią biznesową, czy już ktoś z tego korzysta, czy nie. Chyba tak mi się wydaje, mimo wszystko w jakiś sposób.

**Damian Kaminski:** Wiem, korzystamy, ale to można zaorać w sensie. Tak jak to jest, to może będzie potrzebne jakieś działanie serwisowe, a może nie, bo można to w razie czego przenieść do tabeli lokalnej w sensie inne rozwiązanie systemowe, czyli info zapisywania.

**Janusz Bossak:** Znaczy ja podejrzewam, że nikt z tego nie korzystał, bo nie ma uwag.

**Damian Kaminski:** No, dwóch klientów chyba. To znaczy chyba MSIT korzysta.

**Janusz Bossak:** Jeżeli można. Nie wiem, czy mam ci to.

**Damian Kaminski:** Łukasz, jak to inaczej? Dla kogo to było?

**Lukasz Brocki:** Nie wiem.

**Janusz Bossak:** To było robione prototyp pod Alians.

**Damian Kaminski:** Tylko jesteście pewni, że?

**Janusz Bossak:** Tylko i częściowo potencjalnie, żeby na przyszłość nie było takich problemów z raportowaniem. Ale czy to zostało jakby zmaterializowane, czyli wdrożone w procesach? Do tego nie wiem, czy ktoś tam się tym zajmował. O, Kamil się pojawi, może ten kamień, wiesz?

**Damian Kaminski:** Kamil już, już jest długo.

**Janusz Bossak:** Nie mógłbyś teraz? Spojrzałem, że jest.

**Damian Kaminski:** Tak, tak, tak, ale bo jak oddzwoniłem?

**Kamil Dubaniowski:** Tak, więc stąd zrobię swoje. Tak, że kompletnie nie słuchałem. Ten wątek złapałem, wiem o co chodzi. Nie mam pojęcia. Nie używaliśmy tego w sensie, tam już Piotrek porobił te dedykowane, jak kojarzę, wpisy do tabeli. I to zostało, oni w ogóle ten temat raportowania porzucili.

**Janusz Bossak:** Pamiętam, że prawdopodobnie ta historia biznesowa nie jest nigdzie.

**Kamil Dubaniowski:** Nigdzie nie zużywamy. Ja tak moim zdaniem tak jest.

**Janusz Bossak:** Produkcyjnie, tak, bo to każdy się.

**Damian Kaminski:** Nie, no to potwierdzam, że jest MSIT, ale da się to tam inaczej zrobić.

**Kamil Dubaniowski:** Znaczy trzeba by rzucić okiem na ten MSIT pod tym kątem, gdzie Piotr zapisał te dane. Bo możliwe, że on użył do tego tej tabeli, ale to nie było robione funkcjami tym AddCaseEvent, więc ciężko mi się odnieść. Piotrek to od strony bazy wtedy wrzucił, bo Piotr to zrobił zanim powstała ta funkcja CaseEvent i cały koncept tej biznesowej historii, żeby, terminu zgodził, gdyby szybko dostarczyć klientowi.

**Janusz Bossak:** No, czy?

**Damian Kaminski:** No dobra, to może ja wam teraz. Zatrzymajmy się, bo jeszcze w międzyczasie sprawdziłem coś, co z Kamilem omawialiśmy, tylko ja.

**Janusz Bossak:** Znaczy to.

**Damian Kaminski:** Wczoraj skończyłem i tak od trzeciej, więc nie zdążyłem tego wszystkiego zrobić. Bo może tak, zatrzymajmy się na chwilę i podam wam koncepcję, jaką miałem na Rossmana. I może trzeba w ogóle zmienić tą koncepcję w całości? Mianowicie, nie wiem jakie są ograniczenia na temat. Mianowicie tam są po prostu różne procesy obiegu korespondencji. Problem zrodził się w ten sposób, że oni przekazując między tymi procesami, czyli wcześniej, jeśli była korespondencja obsługiwana analogowo, ktoś ją skanował i decydował gdzie ona idzie. W wyniku tego nie było pomyłek. Po prostu, ja zapytam wprost, nie było pomyłek przed dwoma laty. Nie było, po prostu robiła to osoba kompetentna, przekazywała to zawsze dobrze albo wcześniej dopytywała zanim coś przekazała. Weszły e-Doręczenia i automatyzacja przekazywania. Automatyzacja spowodowała, że zaczęły pojawiać się błędy. Skutkiem tych błędów było to, że trzeba było dorobić przycisk, który kopiuje sprawę między procesami. A skutkiem kopii jest to, że nowa sprawa nie ma historii, bo jest kopią. W związku z tym nie ma tej informacji, co działo się wcześniej, dlaczego tak się działo i jak to wyglądało. Ktoś nagle dostaje i ma niespójność, że dostaje sprawę w dniu dzisiejszym, a sprawa jest sprzed trzech dni i potrzebują wiedzieć. A jednocześnie nie mają dostępu do tego, co działo się historycznie, bo to jest inny proces obsługiwany przez inny dział. Z Kamilem w sumie omawialiśmy chyba wczoraj przy okazji tego AssignProcedure. Ja to teraz jeszcze przetestowałem i w sumie jest w AssignProcedure przeniesienie historii. Mimo że trzeba zrobić jednak krok wstecz i zapytać kolegów z Rossmana, czy nie można wykorzystać AssignProcedure, bo to jest etap wprowadzenie karty, którego nie ma na tym procesie. Tu jest rejestracja. No właśnie, tylko on się z jakiegoś powodu pojawił, a tu go w ogóle nie ma. Bo ta sprawa została przepięta, czyli mamy takie konsekwencje. Ten SPECMED została przepięta z innego procesu i to się po prostu dorysowało, jak wejdziemy sobie w edycję. Do tego po prostu tu nie ma. To jest rejestracja, zapoznanie się z pismem, archiwum, konsultacja. Jak widzicie, jest jakieś wprowadzenie karty, które pochodzi z innego procesu.

**Janusz Bossak:** Nawet bardzo fajny feature unexpected, bo pokazuje rzeczywiście to szło jakimś innym procesem. Tylko tu pewnie trzeba by napisać na tym wprowadzeniu karty nazwę procesu, jeżeli jest inny od obecnego.

**Damian Kaminski:** Może, może, ale dzięki temu też w sumie oni uzyskują to co potrzebują, czyli mają w tej historii podstawowej, że to było gdzieś indziej. I nawet jest, że to jest proces akceptacja karty projektu, a nie ten proces, w którym teraz jesteśmy, czyli korespondencja przychodząca. Tylko jakie mogą być ograniczenia, że są pola niespójne co do nazw technicznych i takie AssignProcedure spowoduje utratę danych. I tego nie wiem, bo to jest jedyne ograniczenie co do zastosowania tej funkcji. Tak jak teraz, no to patrz.

**Janusz Bossak:** No, ale AssignProcedure ma jakieś tam.

**Damian Kaminski:** Przenosi. Mhm, mów, mów.

**Janusz Bossak:** I tak dalej, ale z drugiej strony, jeżeli robią kopię jakiegoś tam sprawy na inny proces i tworzą sobie, no to w sumie jest to samo co ten AssignProcedure. No trzeba i tak i tak dość precyzyjnie.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** No tak, ostrożnie właśnie dokonać mapowania różnych pól. No bo czy to robię, tworzę sprawę w innym procesie i potem przypisuję pola, czy robię funkcjonalność AssignProcedure? No to efekt końcowy powinien być podobny.

**Damian Kaminski:** Mapować. Ale nie jest, bo AssignProcedure, czekaj, żebym się nie pomylił, bo AssignProcedure nie ma przypisywania. Może to tylko trzeba zrobić. Już sprawdzam, bo przed chwilą to robiłem i według mnie nie ma. Nie ma mapowania.

**Janusz Bossak:** Weź, to jest w tym pierwszym etapie.

**Damian Kaminski:** Czy jest?

**Janusz Bossak:** No właśnie, ja nie pamiętam czy on właśnie ma, czy według mnie mapuje wszystko.

**Damian Kaminski:** Mapuje to co jest zgodne technicznie. I teraz pytanie, jak te procesy zostały skonfigurowane? Zmiana ich nazw to też jest jakiś tam wyzwaniem. Może trzeba było tylko tutaj zrobić tak jak w CopyCaseAndAssign, bo w CopyCaseAndAssign mamy.

**Janusz Bossak:** No tak, czy może zamiast AssignProcedure by nie robić CreateCase i odpowiednio?

**Damian Kaminski:** Aha, właśnie tam jest jeszcze inaczej. Tam jest CreateCase i tam dopiero jest mapowanie z jednego na drugie. To nie jest nawet CopyCase, bo to nie jest ten sam proces. To jest CreateCase i przenoszenie ręczne. I wtedy ja Assam, że gdyby było rozbudowane.

**Janusz Bossak:** Tak.

**Damian Kaminski:** O te elementy, nawet może bym powiedział, że jako opcję trzeba by było to zrobić, czyli tak obiektowo. To może to jest rozwiązanie problemu Rossmana. Tylko dalej wtedy zostajemy z historią biznesową niewyjaśnioną. Ale może to nie jest jeszcze odpowiedni moment, żeby to wyjaśniać.

**Janusz Bossak:** Znaczy wydaje mi się, że ta historia biznesowa ona będzie miała zastosowanie wtedy, kiedy będziemy mieli jeszcze dodatkową jakąś, jeden parametr na tym poziomie wyższym. Czyli w tych jakby danych.

**Damian Kaminski:** Czyli dodanie po prostu dodatkowej kolumny z jakimś.

**Janusz Bossak:** Tak, tu musi być.

**Damian Kaminski:** Dodatkowej kolumny z informacją, tak?

**Janusz Bossak:** Dokładnie. Tu musi być ta nadrzędna sprawa. Znaczy dziwię się sam sobie, bo też tam uczestniczyłem w tym, że tego nie zrobiliśmy. Znaczy bo brakuje tej kontekstu. No bo patrząc teraz na JRWA, to jest ten numer sprawy JRWA. Do niej jakby dołączamy jakąś historię, jakieś zdarzenie tutaj. W twoim przypadku to też może być jakaś, tak jak mówisz, sprawa czy numer jakikolwiek. I teraz, nawet jeżeli to się przeniosło do innej sprawy poprzez CreateCase i przepisanie wartości, to tam będzie jakiś numer sprawy biznesowej. Znaczy to jest jakaś sprawa biznesowa. I to co mówiliśmy o tym klient 360, to takim numerem sprawy biznesowej może być numer klienta. I wiemy, że to jest numer klienta i po prostu będziemy później agregować po tym numerze klienta, więc to może być różnie. Może być numer sprawy, tak jak mówimy JRWA, może być to numer klienta czy jakikolwiek inny identyfikator, wokół którego chcemy się kręcić w tej historii biznesowej.

**Damian Kaminski:** No może ja tutaj też źle założyłem. To znaczy chciałem, widziałem na to potencjał, ale może się pomyliłem. Może tak, nie że źle założyłem, ale się pomyliłem. Bo w kontekście Rossmana kluczowa, cała reszta te wszystkie kafelki to jest jakiś dodatek, że to tak można. Raczej chodziło o pokazanie, jak można wykorzystać tą historię biznesową, ale tak naprawdę dla nich istotne byłoby to, czyli nastąpiło przekierowanie do innego działu przez daną osobę w danym dniu. A w tej treści zawarliby, sprawa została moja. Nie mają dostępu do tej sprawy źródłowej, bo to jest inny proces, inny dostępy. I w tej treści wtedy by sobie wpisali z takiego działu do takiego działu. Tamten dział otrzymał to, wtedy stwierdził, że to nie należy do nich i przekazał to do tej sprawy. I tu mogliby już sobie zapisać co sobie, co im się podoba. Wdrożeniowo by to po prostu ustalili. I to też mogłoby się u nich sprowadzać tylko do tego. Cała reszta jest jakimś tam dodatkiem, że tu można więcej, że to nie jest jednokafelkowe. Więc na razie przygotowałem taki mockup, ale może.
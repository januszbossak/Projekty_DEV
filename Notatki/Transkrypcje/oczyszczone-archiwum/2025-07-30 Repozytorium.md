**Data spotkania:** 30 lipca 2025

**Damian Kamiński:** Proszę.

**Łukasz Bott:** To, co pokazujesz, jest zrobione dla Rossmanna, w kontekście działów i spraw. Myślę, że podstawą jest też rozróżnienie nomenklaturowe. Często we wdrożeniach pojawia się wymaganie obiegu dokumentów, a przez dokument rozumiane jest to, co my rozumiemy – sprawa. Czyli jest to fizycznie załącznik, plik, plus zestaw atrybutów, które go opisują, i to realizujemy w postaci formularza. Jeżeli tak traktujemy repozytorium jako dokument plus jego metadane, czyli po naszemu sprawa, i jak to jest w tej chwili reprezentowane, to jest repozytorium spraw i dokumentów. Natomiast wydaje mi się, że często repozytorium jest rozumiane jako stricte repozytorium dokumentów. My możemy mieć sprawę, która jest powiązana z danym dokumentem, bo ona dotyczy procesowania tego dokumentu, np. opiniowania, akceptacji, czy obiegu faktury, ale na poziomie...

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Na poziomie dokumentu można by było oznaczyć, że przekaż go do repozytorium. Może nie tyle fizycznie, bo on nadal fizycznie siedzi w sprawie, natomiast w repozytorium jest symboliczny link do niego. Repozytorium może sobie zorganizować, niezależnie od tego, jak ma zorganizowane procesy. Może sobie zbudować całą hierarchię katalogów, w oparciu o numerację i JRWA. Czyli to, że fizyczny dokument jest w jakimś repozytorium, to jest tylko znacznik. Dodałem do repozytorium, do tego węzła, a może pojawiać się w kilku węzłach, bo dotyczy wielu aspektów. Repozytorium to też JRWA, czyli organizowanie dokumentów pod kątem tego. To moja szybka pomoc, nie opinia.

**Damian Kamiński:** To, co powiedziałeś, według mnie, tak jest.

**Łukasz Bott:** Dokument trafia do repozytorium, ale w kontekście sprawy.

**Damian Kamiński:** W kontekście sprawy, możemy mieć takie uproszczenie, że sprawa reprezentuje jeden bądź zestaw dokumentów. Tu mamy uproszczenie do jednego.

**Łukasz Bott:** Tak.

**Damian Kamiński:** Mamy dokument i jak go mogę osadzić?

**Łukasz Bott:** W procesie chyba nie włączało się ustawienie.

**Damian Kamiński:** Jest wyłączony domyślnie.

**Łukasz Bott:** I widzisz, tu masz dobry przykład, symulację JRWA. Struktura mogłaby być bardziej rozbudowana, wielopoziomowa.

**Damian Kamiński:** Mógłby być węzeł JRWA oczywiście nadrzędny, gdzieś kilka węzłów równoległych, czyli repozytorium firmy jako węzeł, a węzeł JRWA jako JRWA, bo możemy w ramach JRWA zarządzać dokumentacją, która podlega pod JRWA, a równolegle do tego najwyższy węzeł to po prostu repozytorium firmowe i tyle niezależnych dokumentów, które są wewnętrznymi dokumentami. Chciałem zobaczyć w tym repozytorium, gdzie były sprawy? Jest coś z czterdziestki i chcę tę sprawę dodać do czterdziestki. OK. I teraz możemy sobie zobaczyć, że ta czterdziestka ma reprezentację i jedną, i drugą, niezależnie od procesu mamy tu jakieś byty. Może to sobie zapiszmy, to będzie ładniej wyglądać, a czemu się to nie zapisało? No dobra. To mamy.

**Łukasz Bott:** Ale to jest to, co mamy w tej chwili.

**Damian Kamiński:** Coś nie działa ze zmianą ikony. Olewam to, jest, jak jest. Dzisiaj możemy mieć tak: Czy uważacie, że powinna być możliwość wrzucania do repozytorium stricte plików? Czy jednak podchodzimy do tego w ten sposób, że jeśli chcecie pliki, to OK, natomiast mamy dwa procesy: jeden dokument pojedynczy, drugi zestawy dokumentów i zawsze jest to za pośrednictwem sprawy.

**Łukasz Bott:** Nasze podejście jest takie, że to jest do procesowania spraw, a ze sprawą może być powiązany dokument. Dokument może być inicjatorem sprawy, tak jak w obiegu faktur punktem wyjścia jest skan faktury. Natomiast wciąż, pojęciowo, musisz mieć tę sprawę, która ma swój przebieg – dłuższy, krótszy, bardziej rozgałęziony – i ma atrybuty. Najczęściej są one powiązane z dokumentem, bo jeżeli to będzie dokument umowy, to...

**Damian Kamiński:** Jeśli to jest repozytorium, to zakładam, że sprawę traktujemy bardziej jako rejestr. Przepływ nie jest istotny. Ta sprawa ma stan.

**Łukasz Bott:** Rozumiem, że do repozytorium możesz przypisać sprawy z pięciu różnych procesów. W tym rozumiem, że też repozytorium. Chodzi mi o coś takiego: czy jeżeli zrobisz taki worek na dokumenty...

**Damian Kamiński:** Tak, tak.

**Łukasz Bott:** ...który oznaczasz w repozytorium, ale ten dokument to jest po prostu wrzucony dokument. Zakładamy, że nie ma z nim żadnego obiegu, żadnych atrybutów.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Czyli nawet nie odpowiada to bibliotece w raporcie. W SharePoint tworzy się bibliotekę i w bibliotece można sobie zrobić atrybuty. I taki worek, nie wiem, czy nie zrobi się jakimś śmietnikiem. Jakiś worek oczywiście może ustrukturyzowany według jakiegoś kryterium, np. JRWA, czy innych folderów, które sobie zdefiniujemy. Tylko jakby miał być używany? Ktoś wrzuci umowę...

**Damian Kamiński:** Ale wiesz, czy to będzie śmietnik, to nie zależy od nas. Jak ktoś będzie chciał zrobić śmietnik, to wszędzie go zrobi, więc nie jest to kwestia, żebyśmy zadbali o to, by nie można było zrobić śmietnika.

**Łukasz Bott:** Zgadza się. Może źle to nazwałem. Bardziej chodziło mi o scenariusz, że masz z jednej strony proces obiegu umowy, który rządzi się swoim workflow, ma atrybuty, i dokument umowy jest tam w trakcie procesowania lub jest już przetworzony. Z drugiej strony masz worek z dokumentami, gdzie ktoś może wrzucać aneksy, ale zakładamy, że próbujemy zrobić taką strukturę jak system plików. Może być sytuacja, której oczywiście nie unikniemy, bo jest to w gestii zarządzających, że ktoś uruchomi proces, będzie procesować umowę i faktycznie pójdzie zgodnie z zasadami i uruchomi sprawy w AMODIT-cie według wskazanego procesu. Ale ktoś inny to oleje i wrzuci do tego worka. Potem będzie miał pretensje: "A dlaczego ta umowa jeszcze nie jest zaakceptowana?". O to mi bardziej chodziło, w tym sensie śmietnik.

**Damian Kamiński:** Nie wiem, czy dobrze wszystko zrozumiałem, ale po prostu na sprawie powinna być jakaś walidacja. Jeśli na sprawie konkretny etap wymaga podpięcia pod repozytorium, to nie wiem, czy mamy teraz coś takiego, czy jest osadzone w repozytorium, czy nie jest. I ewentualnie, czy możemy też zweryfikować, czy jest dobrze, czyli na podstawie jakichś parametrów formularza możemy stwierdzić, że to powinno być mniej więcej tutaj? Bo może być takie wymaganie, że w określonym węźle wynikającym z zależności od danego użytkownika czy z parametrów na sprawie można to obsłużyć logiką reguł na podstawie danych, kto obsługuje i co mamy na formularzu danej sprawy, jaki jest to proces, czy jak są wypełnione dane dotyczące sprawy reprezentującej te dokumenty. Natomiast czego dzisiaj nie mamy, to możliwości udostępnienia.

**Łukasz Bott:** Tak, Damian, na szybko mamy funkcje reguł, które dodają sprawę do repozytorium i sprawdzają, czy sprawa jest podpięta w repozytorium.

**Damian Kamiński:** OK, to może jeszcze od razu na nie spójrzmy.

**Łukasz Bott:** To jest nadal pojęcie sprawy, bo funkcje mają w sobie nazwę "case", a nie "dok".

**Janusz Bossak:** Poczekajcie, ja bym zrobił krok wstecz, bo trochę teoretyzujemy. Nie wiemy, co pan Piotr rozumie przez repozytorium. On miał przysłać jakiś dokument, w którym to opisze. Może od tego zacznijmy – czy on ten dokument przysłał? Jeżeli nie, to trzeba go poprosić, żebyśmy wiedzieli. Tak jak ja zrobiłem mockup komunikatora, o to mi chodzi. Teraz chciałbym, żebyśmy najpierw dowiedzieli się, o co mu chodzi, bo repozytorium to bardzo pojemne pojęcie. Nasze repozytorium jest repozytorium spraw. I realizuje swoje funkcjonalności w określony sposób, bo tam trochę dyktando potrzeb. Pewnie mogłoby być inaczej, pod potrzeby JRWA, ale to jest repozytorium cały czas spraw, w których są dokumenty. Niektórzy ludzie, może pan Piotr, przez repozytorium mogą rozumieć repozytorium dokumentów. I to jest niebezpieczne, ponieważ to kompletnie zmienia filozofię AMODIT-a. Filozofię, tak jak Łukasz powiedział, opartą o sprawy. Nośnikiem informacji jest sprawa, w której może być, ale nie musi być dokument, tak jak te wzorce.

**Janusz Bossak:** Kiedyś na tych LO było coś takiego jak typowe repozytorium dokumentów, gdzie wgrywało się dokument i dokument był nośnikiem informacji. Wokół tego dokumentu mogły być puszczane różnego rodzaju procesy. To zupełnie odwrotna filozofia. Nie chciałbym iść w stronę taką, żeby AMODIT-a nagle zamieniać w inny system o innej filozofii działania. Nasza filozofia to repozytorium spraw i posługiwanie się sprawami. W tym obszarze możemy coś usprawniać, natomiast nie chciałbym tego przewracać. Na którymś ze spotkań Piotr powiedział, że moglibyśmy prezentować zawartość tabeli i traktować to tak jakby dla nas zawsze pierwotną tabelą jest "case definition". A Piotr powiedział, że mogłoby być tak, że dla potrzeb tego repozytorium pierwotną tabelą jest… tak. Ale elementy same w sobie nie mają informacji o uprawnieniach. Uprawnienia do danego załącznika wynikają ze sprawy i z uprawnień do tej sprawy.

**Damian Kamiński:** OK. I teraz może to, co powiedziałeś, powinno być tutaj. Klikając na sprawę, nie powinienem dostawać otwarcia tej sprawy, tylko może powinien być jeszcze kolejny element, który pokaże nam załączniki.

**Janusz Bossak:** Według mnie powinno być inaczej. To, co już teraz widzisz, to powinny być załączniki.

**Damian Kamiński:** Dokument.

**Kamil Dubaniowski:** To da się w tym momencie zrobić w oparciu o moduły raportowe, bo ten widok można podmienić na raport i zdefiniować sobie, że tu mają się wyświetlać tylko pola załączniki. I to powinieneś zrobić gdzieś na szczycie, żeby był dziedziczony przez podrzędne węzły.

**Damian Kamiński:** Tutaj "Dodaj widok".

**Kamil Dubaniowski:** To działa jak nasz raport, czyli możesz kliknąć i otworzyć podgląd dokumentu.

**Damian Kamiński:** Tylko to nie zadziałało. Co tu muszę? "Dodaj widok", ale wszystko muszę zdefiniować.

**Kamil Dubaniowski:** Raport musisz wyklikać, który będzie pokazywał to, co ty chcesz. To jest w oparciu o moduły raportowe.

**Damian Kamiński:** Tak, tylko nie zmierzam do tego, że klikam na węzeł, mam "Dodaj widok". Powinno być "Stwórz raport na podstawie". Tak bym to rozumiał, że to jest odnośnik do tego węzła. Przechodzę do kliknięcia przycisku "Stwórz raport".

**Janusz Bossak:** Ale nie wiesz, co chcesz?

**Kamil Dubaniowski:** Bo nie wiesz, co będzie chciał wyświetlić użytkownik jako widok tego węzła. Jak wejdziesz do tego węzła, co chcesz wiedzieć? Skąd mamy wiedzieć?

**Damian Kamiński:** OK. Nie upieram się, że to jest oczywiste, jak mówicie, natomiast chyba to nie jest właściwe.

**Kamil Dubaniowski:** To było robione w ciągu dniówki przez Marka na szybko, bo Rossmann nie chciał tu widoku listy, tylko tabelaryczny, żeby wyświetlić w osobnej kolumnie nazwę, datę, aktualnego właściciela i tak dalej. Czyli nie mieli pod każdy węzeł, bo każdy dział chciał widzieć inne kolumny, dlatego to jest tak uniwersalnie, że po prostu definiujesz w danym węźle raport. Dla każdego działu mogłem zdefiniować taki raport, jaki był potrzebny. Taki węzeł najwyższy po prostu jest dziedziczony przez wszystkie kolejne, czyli tylko tam, gdzie jakieś działy miały swoje wyjątkowe kolumny, musiałem to przerabiać, a reszta ma podstawowy widok.

**Janusz Bossak:** Wybierz jakiś dokument kadrowy czy coś.

**Damian Kamiński:** Tak, ale tu nie ma nic zdefiniowanego w filtrach, że to jest ten dokument, który wskazałem. Wszystkie. Mogę jeszcze wskazać drugi, czyli korespondencję przychodzącą, to będzie więcej widoku, wspólny dokument etap.

**Janusz Bossak:** Czekaj i został na tym etapie bez tego nawet aktualny etap. Może ten proces tam wybierze.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Mamy dwa. A ten aktualny etap możesz wyrzucić albo coś tam. I teraz jak tak zostawisz? Zapisz to. Więcej nie potrzeba żadnych okładek. I teraz jak to w ogóle?

**Damian Kamiński:** Jak to znaleźć?

**Janusz Bossak:** Nie, nie, to jest tutaj, w tym węźle.

**Damian Kamiński:** To jest tu.

**Kamil Dubaniowski:** Wtedy pod jakiś konkretny węzeł to wpiąłeś, tylko musisz się teraz dostać do tego węzła.

**Damian Kamiński:** A dobra, to teraz to rozumiem. Dopiero, czyli to jednak ma znaczenie ten widok. Dobra. Myślałem, że to się stworzy.

**Janusz Bossak:** I teraz tu masz dokumenty z jakichś spraw tego procesu. Tu masz nawet podgląd, jak klikniesz sobie na ten proces, tam dokumentów. Można by tu dać tytuł sprawy czy cokolwiek. Możesz wejść, to jest sprawa i sobie obejrzeć. Może się okazać, że masz w tej sprawie 15 plików i będziesz widział 15 razy tę sprawę, bo te 15 plików jest w tej jednej sprawie i masz repozytorium plików. To, co tu też Kamil mówił, to, co było robione dla Rossmanna. Tu jeszcze była jedna bardzo ciekawa funkcjonalność, której chyba nie ma w tym module raportowym zwykłym. Jak podepniesz korespondencję przychodzącą i wychodzącą, na przykład, i w korespondencji przychodzącej masz datę przyjścia tej korespondencji, a w korespondencji wychodzącej masz datę wysłania korespondencji, to on jest w stanie posortować to po zdarzeniach, mimo że to są zdarzenia z różnych procesów i różne daty.

**Kamil Dubaniowski:** Ten moduł jest rozszerzony o tyle, że możesz wybierać kolumny z dwóch różnych procesów i on ci je wyświetli, jeśli na przykład jest data nadania w korespondencji wychodzącej i data wpływu w korespondencji przychodzącej, to możesz wyświetlić te dwie kolumny. Przy sprawach korespondencji przychodzącej jedna z nich będzie pusta.

**Janusz Bossak:** Tak. I to jest rzecz, której nie ma w normalnych raportach. Ciągle się dziwię dlaczego, skoro to jest bardzo fajna funkcjonalność. Mam dokumenty z dwóch różnych źródeł. Mogę mieć, na przykład, zamówienia i faktury i mogę sobie wyświetlić kwotę zamówienia, kwotę faktury w jednym raporcie.

**Damian Kamiński:** Tylko coś to nie działa, jak zdefiniowałem dwa, to coś tu przestało działać.

**Kamil Dubaniowski:** Wbijałeś to pewnie w jakiś konkretny węzeł, bo widzisz, tamten dziedziczy z poprzedniego.

**Damian Kamiński:** Cały węzeł nadrzędny dziedziczy to. Po pierwsze, jak wpiąłem nawet tu, to wszystko, natomiast jest jakiś problem, coś tu nie działa, bo jak dam, aha, teraz...

**Kamil Dubaniowski:** Może nie masz spraw?

**Damian Kamiński:** Nie wiem, gdzie nawet tu jest. Zmień widok 4.1, bo tu mogę tylko przywróć domyślny. A w 4.1 to wpiąłem. Natomiast tu są jakieś sprawy, a ich nie wyświetlamy.

**Kamil Dubaniowski:** Może nie dałeś, że zamknięte też?

**Damian Kamiński:** Dałem właśnie. Jeszcze raz, zobacz, jeszcze raz zatwierdź domyślny i teraz...

**Janusz Bossak:** Ale to nie ma nic wspólnego z tymi sprawami, które teraz tam widzisz.

**Kamil Dubaniowski:** Ale to zobacz, jakie to są procesy. W ogóle to ich nie bierzesz do definicji swojego raportu, więc...

**Damian Kamiński:** Masz rację, nie wziąłem. Masz rację, bo to są sprawy, a nie korespondencja. Dobrze, przepraszam, zwracam honor.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Konkretnie tak. To jest mechanizm, na bazie którego można zbudować to repozyzytorium i doprowadzić do tego, co ten Piotr Murawski chce. Ale nie wiem, czy on tak chce. Wolałbym, żeby...

**Kamil Dubaniowski:** Według mnie, nasze repozytorium wymaga jednej kluczowej zmiany opcji do wyboru: czy repozytorium ma być uzależnione od struktury działów, czy ma być takim swobodnym repozytorium na bazie? Właśnie, że tworzy sobie nowy węzeł, tam podfoldery i tak dalej, i jak mi potrzeba, to udostępniam to komu chce. Trochę działa na takiej zasadzie, że jesteś w dziale, to widzisz wszystkie węzły w tym dziale i przy okazji wszystkie sprawy, które są wpięte do tych węzłów i to jest uzależnione od... Takie wymaganie było w Rossmannie i tak zrobiliśmy, a powinna być opcja, że po prostu nie masz tej kolumny "działy", bo to jest wtedy dla danej organizacji nieistotne i w ramach każdego użytkownika widzę tylko to, do czego mam dostęp, albo to, co sobie stworzyłem i udostępniłem gdzieś dalej.

**Damian Kamiński:** Ale poczekaj, a czemu tak uważasz? Według mnie ten podział jest dobry, bo ja wchodzę jako administrator. Uważam, że ma sens, że ja wtedy widzę: "Aha, dobra, tu sobie namieszał dział operacyjny, a tu technologiczny". I automatycznie, każdy ma dostęp do jakiegoś zasobu w tej postaci, jak ty mówisz. Jak to ma wyglądać? Każdy sobie tworzy od poziomu użytkownika, czyli ma swojego użytkownika i tu dopiero robi wewnątrz, tak jak w SharePoint.

**Janusz Bossak:** Chodziło o to, żeby udostępniać. Czyli jest dział organizacyjny, który tworzy sobie regulaminy i udostępnia je dla wszystkich.

**Damian Kamiński:** I wtedy ja klikam tu "Udostępnij", pojawia się jakaś gwiazdka albo jakieś oznaczenie, że to jest, albo zmienia się ikonka, że to jest folder udostępniony i go wszyscy widzą. Czyli mamy poziom, powiedzmy, ten podstawowy, swój. Jak jestem kimś konkretnym, zaraz przełączymy się w jakiegoś Jana archiwistę, to będę tu miał.

**Janusz Bossak:** Nie jest przypisany i archiwista do żadnego działu. Na przykład taka sytuacja, mimo nieprzypisania do działu, powinien mieć dostęp do folderu wspólnego.

**Damian Kamiński:** O i mam tu "Dział operacyjny", a mam drugi folder od razu udostępniony. I wtedy w tym udostępnionym mam strukturę pełną dla udostępnionych folderów. Czyli jakiś dział regulaminów po pierwsze, a potem poniżej folder nazwy folderów udostępnionych. Czyli mam swój dział i w ramach niego mam swoją strukturę, a mam drugi równoległy folder reprezentujący, tak jak mamy tutaj. Notabene to też ciekawy temat, że mi się tak wyświetla, że jakby były zagnieżdżone udostępnione i tu mam strukturę wtedy udostępnionych.

**Kamil Dubaniowski:** To pojedyncze pliki, ale tak my moglibyśmy zachować strukturę. Czyli masz tam pod spodem udostępniane.

**Damian Kamiński:** Dokładnie.

**Kamil Dubaniowski:** I to już się da zrobić. Tylko, udostępniasz cały dział, nie można udostępnić wybranych folderów z tego działu, tylko da się udostępnić. Tak, to się da.

**Damian Kamiński:** Mówisz "dzisiaj"? To jest kwestia do zrobienia, że ja chcę kliknąć, będąc użytkownikiem, chcę kliknąć tutaj i udostępnić ten dokument. Ten folder.

**Kamil Dubaniowski:** To też prowadzi do tego, kto to może zrobić. Moim zdaniem nie każdy członek działu powinien móc udostępniać całe foldery.

**Damian Kamiński:** No dobra, można to definiować tak, kto może. Jak zarządzanie słownikami, grupami. Może być przypisane do działu, tak. Użytkownicy danego działu mogą udostępniać w ramach repozytorium foldery.

**Kamil Dubaniowski:** To się sprowadza do tego, że repozytorium jest mocnym narzędziem do nadawania uprawnień, bo jak nadasz uprawnienia do folderu, to nadasz do wszystkich spraw, które w tym folderze są. Masz od razu odczyt, że to na pewno nie może robić każdy. Ale zgodzę się, jeśli w ten sposób do tego podejdziemy, to podział na działy jest w porządku.

**Damian Kamiński:** Tak, zgadza się.

**Kamil Dubaniowski:** Tylko udostępnianie trzeba przemyśleć, pewnie na zasadzie struktury. Czyli udostępnij i pokazuje ci się graficznie struktura całej organizacji, bo spodziewam się, że będą foldery udostępnione w całej firmie.

**Janusz Bossak:** Tak, tak.

**Kamil Dubaniowski:** I teraz, żeby tam...

**Damian Kamiński:** Nie, nie, poczekaj. Chcesz udostępniać innym, tak naprawdę udostępniać strukturze, a nie tak, jak wszystko, co mamy. Czyli może jednak powinniśmy udostępniać użytkownikom i grupom domyślnie? Czy na podstawie innej struktury, czyli ja w ramach swojego folderu?

**Kamil Dubaniowski:** Czy to jest coś, co może być połączone, tak? Coś, czego nam brakuje, na przykład w module raportowym, że chcesz udostępnić wybranym działom.

**Damian Kamiński:** Działu operacyjnego. I to, i to.

**Kamil Dubaniowski:** I wybierasz sobie z drzewka tam strukturę.

**Damian Kamiński:** Zapisuję.

**Kamil Dubaniowski:** I wtedy mielibyśmy ten sam identyczny interfejs do udostępniania użytkownikom, grupom lub w ramach struktury konkretnym wybranym działom. To sprowadza się do tego, że jak ktoś dojdzie do działu, wypadnie z działu, to dostaje uprawnienia. A teraz nie mam takiej opcji. Trzeba tworzyć sztuczne grupy, która by zbierała ludzi z tego działu i udostępniać raport tej grupie. Tak mi się kojarzy. Może to się gdzieś tam w międzyczasie zmieniło. Jest taka opcja udostępnienia do działu, ale wydaje mi się, że nie. Może jest jakiś parametr, że jest użytkownikiem działu. Coś takiego może mamy.

**Damian Kamiński:** Mapowanie dostępu. Nie, nie. Grupa. Wszyscy. Lub. Struktura.

**Kamil Dubaniowski:** Tu właściwie było rozszerzenie, bo grup może być więcej niż jedna, która ma mieć do tego dostęp.

**Damian Kamiński:** Tak, tak, to mam grupy. Wszyscy. To w domyśle miałem lub struktura dla całej gałęzi wskazanej ze struktury. To jest jeszcze tu mówiłeś?

**Kamil Dubaniowski:** Chyba wszystko dla adminów jeszcze jest taka opcja, ale nie wiem, czy to będzie miało akurat tu zastosowanie. Że tylko dla mnie, tak? To jest właściwe.

**Damian Kamiński:** To bym robił wspólnie.

**Kamil Dubaniowski:** Znaczy inaczej. To też do zastanowienia się, czy repozytorium domyślnie jest tak, jak teraz, z dostępem na poziomie działu, czy wprowadzamy jeszcze jeden poziom, że coś jest tylko dla mnie? Czy już to pomijamy? Dla mnie jest tylko na poziomie spraw. Zakładam, że niekoniecznie chcemy konkurować znowu z dyskami sieciowymi. Pewnie trzeba dopytać pana Piotra pod tym kątem. Rozumiem. Natomiast ja rozumiem, że repozytorium z założenia jest formą dzielenia się informacją, a nie przechowywania własnych spraw, więc nie robimy folderów, które tylko ja widzę. Nie idziemy w tym kierunku.

**Kamil Dubaniowski:** Spodziewam się, że mógłbym tak chcieć. Docelowo, nie może jako MVP, ale docelowo przydałby się folder "Moje umowy". I sobie coś tam będę odkładał dla siebie, ale to tak jak.

**Łukasz Bott:** Moje umowy. Jeżeli jesteś w jakiś sposób oznaczony w tych umowach, jest tu proces i nie zmieniamy koncepcji filozofii, czyli bazujemy na sprawach, to zrobię raport. Po co repozytorium?

**Damian Kamiński:** Widziałbym to wtedy tak...

**Kamil Dubaniowski:** Tak, ale tak można podważyć całą zasadność repozytorium.

**Damian Kamiński:** To ja bym widział to wtedy tak...

**Łukasz Bott:** Lub zasadność modułów raportowych, bo wszyscy pójdą sobie...

**Kamil Dubaniowski:** Tak, z jakiegoś powodu Rossmann chciał to repozytorium w kontekście właśnie tych folderów, między innymi możliwości swobodnego tworzenia tych folderów. Ja w raporcie mogę zrobić folder tylko w oparciu o dane, które tam są, a czasami foldery nie są w żaden sposób spięte z tymi danymi. Taki to był zalążek, dlaczego to repozytorium w ogóle powstało.

**Janusz Bossak:** To był główny powód. Tak, że właśnie tu każdy dział, dział prawny robi swoje foldery i przechowuje, tak jak oni chcą, jakieś swoje rzeczy. Dział HR przechowuje swoje w jakiś tam sposób, dział finansowy swoje, w jakiś sposób w ogóle niezależny od innych działów. Dlatego to repozytorium tak powstało. Według mnie ono ma duży sens. Braki są w tym obszarze, o którym też pan Piotr się dopytuje, czyli udostępniania. Czyli jest jakiś dział, powiedzmy ten administracyjny czy organizacyjny, który chce regulaminy czy instrukcje udostępnić dla wszystkich. Tak. I o to chodzi. Może to jest w zupełności wystarczające.

**Damian Kamiński:** Dobra, czyli spisałem to tak jako "pomysł Kamila". Nie wyskakiwałbym z nim przy panu Piotrze. Raczej po prostu dwie główne.

**Kamil Dubaniowski:** Ja to bardziej myślałem, że w ramach swojej organizacji tworzę sobie taki folder, który jest tylko mój imienny i tam, na przykład, pod umowami, bo jest ogólny folder "Umowy", to ja sobie zrobię...

**Damian Kamiński:** Ale inni go nie widzą.

**Kamil Dubaniowski:** Tak. Ja sobie zrobiłem "Moje umowy" i tam będę zrzucał dodatkowo jakieś rzeczy, które faktycznie są dla mnie istotne.

**Damian Kamiński:** Czyli...

**Kamil Dubaniowski:** Tak. Łukasz, to co powiedział? Jasne, mogę mieć raport, ale w repozytorium wolę mieć to w jednym miejscu, więc zrobię sobie folder "Moje umowy" i tam podpinam, będę wpinał na bieżąco coś, co jest dla mnie istotne. Jak już skończę opiekę nad umową, to wypnę.

**Damian Kamiński:** Tak, tego kto tego wtedy nie widzi. Janusz widzi twoje umowy, tak, ja ich nie widzę.

**Kamil Dubaniowski:** Tak, bo to są... Janusz jako admin, tak, czy jako mój przełożony?

**Damian Kamiński:** Janusz jako twój przełożony.

**Łukasz Bott:** Niekoniecznie, bo jeżeli "moje", to moje. Bo bardzo wiem, że "Moje umowy" czy coś, to jest mój worek. Jak ja sobie go zorganizuję, to jest.

**Kamil Dubaniowski:** Niekoniecznie. Żeby później...

**Damian Kamiński:** Ale twoje sprawy Janusz widzi. Więc i tak ma do tego dostęp z innego poziomu, nawet jak tego nie pokażemy.

**Kamil Dubaniowski:** Tak, ale pytanie, bo Janusz jako przełożony będzie też działał na tym repozytorium.

**Łukasz Bott:** Tak, ale...

**Damian Kamiński:** Może jeszcze inaczej. Może tu powinno być w dziale, tylko to strasznie rozbudowujemy. Bo może w dziale powinny być domyślnie od razu katalogi każdego użytkownika. I każdy ma dostęp tylko do swojego.

**Łukasz Bott:** Ale to sugerowałoby, że ja mogę wejść w twój katalog, a i tak kliknę i nic nie będę widział.

**Damian Kamiński:** Nie, nie, ty nie widzisz mojego katalogu. Janusz widzi nasze wszystkie katalogi, bo i tak widzi sprawy.

**Łukasz Bott:** W sensie jako przełożony, administrator. Dobra.

**Damian Kamiński:** Tak, ale ja domyślnie w dziale operacyjnym widzę tu siebie i to jest mój katalog. W jego ramach mogę robić i jeszcze dodatkowe katalogi i to tylko widzę ja plus Janusz. I katalogi, które zostały ustalone w ramach działu. Nie widzi swoich katalogów. Tak. Na równym poziomie, czyli tutaj widziałbym to tak: Damian Kamiński i to byłby pewnie katalog jako pierwszy, żeby było to łatwo mierzalne, a cała reszta alfabetycznie.

**Kamil Dubaniowski:** Jest to opcja, ale nieco zmienia założenia. To, co ja wspomniałem: będziesz musiał sobie wydzielić "Moje umowy", a ja bym wolał mieć ten katalog gdzieś tam przy węźle związanym z umowami.

**Janusz Bossak:** Tak będzie.

**Damian Kamiński:** Dobra, tylko z drugiej strony, to możesz to wyświetlić w formie tabelarycznej i tak jak pokazałeś i tu możemy mieć kolumnę, co jest czyje.

**Kamil Dubaniowski:** Tak.

**Damian Kamiński:** Żebyśmy nie komplikowali, dobra, na razie zostawmy to. Mamy taki ogólny poziom repozytorium moich jednostek, czy też mojej jednostki, czyli to jako jedna reprezentacja i druga udostępniona.

**Kamil Dubaniowski:** Dobra, tak jak powiedziałeś, może zostawmy to.

**Damian Kamiński:** I wtedy buduje nam się drzewko w ramach katalogów.

**Kamil Dubaniowski:** Ale to drzewko. Ja bym nadal widział w tej samej formie, czyli udostępnionej. Pod spodem widzę wszystkie struktury działów, które mi coś udostępniły. Zawężoną do tego, oczywiście, nie wiem, jak zarząd nic nie udostępnił, to nie widzę tego węzła. Tak teraz to działa, czyli jeśli mam udostępnione działy administracji dodatkowo, a wynika ze struktury, że jestem w dziale operacyjnym, to po prostu pod tą kreską pojawia mi się katalog działu operacyjnego.

**Damian Kamiński:** Czekaj, już robię, żebyśmy zobaczyli, bo ty może lepiej wiesz, jak to działa. Zobaczymy, jak to działa.

**Kamil Dubaniowski:** Tam na dole to jest bardzo tak, i daj, na przykład, ten dział finanse.

**Damian Kamiński:** Finanse damy.

**Kamil Dubaniowski:** Żeby gdzieś mi te działy jako po prostu najwyższe, po raz pierwszy mi wpadły do tego prawego menu, bo tam już jest.

**Damian Kamiński:** O, ale to jest spoko, w sensie ja bym to właśnie tak rozdzielił, tylko może bym to nazwał, że to jest udostępnione i tu widzę sobie jakieś udostępnione.

**Kamil Dubaniowski:** Tak o to mi chodzi. Dokładnie. Czyli żeby nadal ta kolumna pierwsza była na poziomie działów, a ta kolumna druga już jest na poziomie folderów z tych działów.

**Damian Kamiński:** OK, tylko teraz jeszcze skomplikuję.

**Kamil Dubaniowski:** Jak dodasz coś z wyższego poziomu, to nie trzymamy tej struktury, bo każdy dział jest udostępniony jako niezależny.

**Damian Kamiński:** No. A no właśnie, to może to powinniśmy jakoś ustrukturyzować, żeby to było bardziej czytelne, chociaż pewnie zarząd tam mało co będzie udostępniał, bo to nie jest rola zarządu. Ale już jakiś dyrektor...

**Kamil Dubaniowski:** To jest akurat dwupoziomowa struktura, więc nic tam nie ugramy więcej. Tak.

**Damian Kamiński:** Czyli jak zrobię tak, to będę miał zarząd i finanse jako osobno, tak?

**Kamil Dubaniowski:** Tak, na jednym poziomie bez zagnieżdżania.

**Damian Kamiński:** Oj, nie ten. OK. No to wiecie, to wszystko, ale patrząc przez pryzmat WIM-u, nie będę się tam teraz logował. Tamta struktura jest rozdmuchana, to jest duża organizacja, więc takie coś może być nieczytelne.

**Kamil Dubaniowski:** Tylko zauważ, że tutaj, jak wejdziesz w zarząd, to masz udostępniony tylko poziom zarządu, czyli konkretnie z tego działu. A teraz to by miało się wydarzyć, jak udostępniasz zarząd czy te podrzędne.

**Damian Kamiński:** Mhm.

**Kamil Dubaniowski:** OK, no dobra, tu trochę to kuje.

**Damian Kamiński:** Nie, nie, udostępnianie jest na tym poziomie, ja udostępniam konkretny folder i wszystkie podrzędne oczywiście tak, ale nie cały zarząd, tylko konkretny folder. Klikam "Udostępnij", wskazuję komu. Więc wtedy, wchodząc na zarząd jako użytkownik, widzę to. Jak udostępnię sobie czwórkę, to widzę czwórkę i wszystko, co jest pod czwórką, tak?

**Kamil Dubaniowski:** Potencjalnie. Zastanawiam się, czy wszystko pod też, no i co w przyszłości, jak będą tam dochodziły kolejne foldery? Czy to faktycznie ma dziedziczyć?

**Damian Kamiński:** Myślę, że tak, tylko musimy zwizualizować to udostępnienie, żeby ten, kto widzi, to powinien być jakiś tam gwiazdka, jakiś znaczek, inny folder, że to jest folder udostępniony. No, a jak on jest udostępniony, to wszystko pod spodem też. Nie ma sensu, przecież tak samo jest w SharePoint. Jak udostępnisz, to to jest dziedziczone cały czas. Jak udostępnisz nadrzędny, to ktoś ma wgląd we wszystko w głąb.

**Kamil Dubaniowski:** Dobra, to OK. Z tematów, które ja bym jeszcze chciał w tym wątku, to JRWA. Jeśli faktycznie będzie przy okazji tego, to brakuje funkcjonalności eksportu/importu tej struktury folderów, bo akurat w przypadku JRWA z roku na rok taka podstawa się kopiuje, a jedynie te foldery dodane przez użytkowników już w ramach roku są tworzone na bieżąco. Czyli jest jakiś szablon, on taki ogólny, który może sobie właśnie, i to jest w ogóle, że co roku ta struktura jest w ramach JRWA inna i oni po prostu przełączają się, że w tym roku była taka i widzą ją, w kolejnym była taka i mogą się przełączyć na przyszły, zeszły rok.

**Damian Kamiński:** Czy ty, Kamil, jesteś tego jeszcze 100% pewny?

**Kamil Dubaniowski:** Tak, przynajmniej tak wtedy wynikało, jak ja to analizowałem. Ale wątpię, że coś w tym zakresie się zmieniło. To z prezentacji oglądałem wtedy.

**Damian Kamiński:** 100%, tak.

**Kamil Dubaniowski:** Ja wręcz sobie od nich wziąłem gotowe pliki, eksportowałem to z danego roku jako strukturę i później to przekładałem na naszą, żeby robić jakiś przykład.

**Damian Kamiński:** Mhm. No dobra, a czy my nie możemy zrobić tak, że tutaj, jeśli włączamy JRWA, to jest jakiś znowu węzeł JRWA, który jest niezależnie zarządzany? I teraz jak włączamy węzeł JRWA, to pierwszymi węzłami są lata. Ustalamy, że ten węzeł na poziomie węzła można, powiedzmy, wygasić (nieaktywny), czyli on już się nie będzie podpowiadał do podpinania nowych dokumentów, tak jak pozycje słownikowe. To jest historyczne, a teraz przychodzi kolejny rok. Powiedzmy, jeszcze ten rok, stary, z racji, że kończymy jakieś sprawy, to ten węzeł 2024 jest dostępny do tam końca stycznia. Tak się umawiamy. To jest końcem stycznia, go dezaktywuję, czyli jest widoczny do filtrowania, ale nie można go dodać, jak jesteśmy na sprawie, już tu go oznaczyć, może jest albo wyłączony, albo w ogóle się nie wyświetla. Wtedy w kontekście tego. Natomiast, jak robimy nowe, to robimy tak naprawdę węzeł, zaczynamy od roku, a potem na roku klikamy sobie zaimplementowanie struktury podrzędnej i wrzucamy to, co przed chwilą wyeksportowaliśmy z tego 2023. Robimy 2025, tak?

**Kamil Dubaniowski:** OK.

**Damian Kamiński:** Jak ty byś do tego podszedł, w kontekście tego, jakie masz doświadczenie właśnie z EZD, bo ja nie wiem, to jest...

**Kamil Dubaniowski:** Jedyne, czego tu by nam brakowało, to nie wiem, jak to osiągnąć, to to, że nie będziemy w stanie wyłapać, co jest tą podstawą, a co już jest tworzone jako dodatki, bo to chodzi o to, że masz jeden katalog, na przykład jak tutaj "410 nadzór nad samorządem gminnym", i teraz jakiś użytkownik sobie tam w ciągu roku będzie tworzył 15 różnych folderów, a naszym zadaniem jest skopiować to do poziomu "nadzoru nad samorządem gminnym". Reszta folderów nas nie interesuje i to będzie w ramach różnych tutaj węzłów. W innym momencie będzie to odcięcie, które foldery są takie, powiedzmy, systemowo wymagane, a które to już są takie dodatkowe, niewymagane, po prostu robione dla wygody przez użytkowników.

**Damian Kamiński:** Dobra, ale to poczekaj, czy my możemy określić poziom zagnieżdżenia? Do trzeciego jest systemowo, w głąb już jest indywidualnie.

**Kamil Dubaniowski:** Tego nie pamiętam.

**Damian Kamiński:** Bo jeśli jesteśmy, no to przy eksporcie możemy wskazać "wyeksportuj węzły do trzeciego zagnieżdżenia", tak? W przeciwnym wypadku oni muszą mieć wzorzec stworzony, po prostu muszą sobie ustalić. Raz go definiują przy definicji pierwszej, eksportują i potem tylko importują z każdym kolejnym rokiem.

**Kamil Dubaniowski:** Tak. Mhm.

**Damian Kamiński:** To jest do obejścia, nawet jeśli tego zapomnieli, konsultant nie podpowiedział, no to wyeksportują i ktoś siądzie i w dwie godziny wyczyści te zbędne, tak? Jakiś tam sposób.

**Kamil Dubaniowski:** OK, no dobra, to tak, czyli opcja w ogóle eksportu/importu tego, żeby była to, że będziemy importować do węzła takiego nadrzędnego, który będzie rokiem. Wydaje mi się, że to przejdzie. Tak, nie trzeba by pewnie jeszcze wrócić i poczytać. Zobaczyć, jak wygląda ta opcja wygaszania w takim wypadku, chociaż to nie taka, moim zdaniem, całkowita, tylko to powinno być na zasadzie "Ukryj", a później gdzieś opcja "Pokaż ukryte". Bo zdarzy się, że będziesz miał do wpięcia w 2026 jakiś dokument z końcówki 2025, więc potencjalnie musisz mieć podgląd nawet na etapie wpinania spraw do tych zeszłych lat.

**Damian Kamiński:** Dobra, głąb. Możliwość definiowania węzłów z konsekwencją w głąb też źle. Jako ukryte, aktywne. Może niekoniecznie jak słowniki, ale to usunę.

**Kamil Dubaniowski:** Co do tego repozytorium, jeszcze tak technologicznie patrząc, korzystamy z jakiegoś gotowego komponentu, tam jest mnóstwo ograniczeń. To jest jakaś biblioteka, którą jeszcze Borys wynalazł lata temu, więc jest duża szansa, że będziemy to szyli po prostu od zera, bo te zmiany mogą być niemożliwe do wprowadzenia, nawet drobiazgi typu zmiana strzałki, która rozwija te katalogi, była niemożliwa na etapie, jak Mariusz próbował coś zmodernizować. Ten wygląda tak, więc jest szansa, że w czasie całkowicie się wysypie. Dobra, to wracając do tego.

**Damian Kamiński:** No dobra.

**Kamil Dubaniowski:** Tam jest też tak, że każdy katalog w ramach tego akurat JRWA jest opisany specyficznymi parametrami, które później są dziedziczone przez wszystkie sprawy wpięte do tych katalogów. Czyli jest tam, na przykład, to "410" jakieś tam, a w ramach tego ktoś zdefiniował, że ten folder ma być przechowywany przez 10 lat, że jest to tam "Kategoria A", więc wszystko, co zostanie do tego folderu wpięte, dziedziczy tę kategorię A i jest to sygnał później w procesie usuwania tych dokumentów, że ten dokument można usunąć po 10 latach. Czyli ja sobie zapisałem taki punkt, że po prostu te foldery muszą mieć opcję przypisywania parametrów. To, jakie parametry, to też trzeba gdzieś, moim zdaniem, móc definiować, bo to nie dla każdego przypadku będą te same. W WIM będzie chciał inne parametry, albo w ogóle Rossmann chciał, i nie zrobiliśmy, jakieś tam parametry swoje.

**Damian Kamiński:** Czyli musimy mieć de facto rejestr, tak? Czyli każdy folder...

**Kamil Dubaniowski:** Taki formularz, tak.

**Damian Kamiński:** Musiałby mieć formularz jak sprawa, tak.

**Kamil Dubaniowski:** Dokładnie, może nie nawet każdy folder, ale w takim wypadku jako definicja repozytorium, czyli jakimi parametrami można w tym repozytorium opisywać foldery? Czyli taka definicja repozytorium już się nam budowała.

**Damian Kamiński:** No dobra, ale to wtedy, czyli tak, powiedzmy, nadaj cechy temu węzłowi i wszystkim w głąb, powiedzmy, i tam określamy sobie nazwę pola i typ pola, tak jak mamy.

**Kamil Dubaniowski:** Wydaje mi się, że na tym. Tak, ale na tym etapie ja bym tego nie robił, węzeł tylko już wtedy jako definicja całego repozytorium.

**Damian Kamiński:** I wartość, tak.

**Kamil Dubaniowski:** Czyli wszystkie foldery w tym repozytorium mogą być opisywane takim zestawem parametrów, bo to raczej nie będzie tak, że na przykład...

**Damian Kamiński:** OK, ale może i JRWA, bo wiesz, zakładam, że my to jednak jakoś wydzieliły, czyli to JRWA to będzie coś raczej niezależnego od tego repozytorium strukturalnego, tak? Tak zakładasz.

**Kamil Dubaniowski:** Nie zakładałem tak. Zakładałem, że jest jedna definicja repozytorium. Jeśli ktoś będzie korzystał, to w ramach JRWA, to tak działa. I też zobaczcie na to uprawnienie tutaj pod kątem.

**Damian Kamiński:** No poczekaj, ale to wtedy JRWA jest udostępniane, jest węzłem, który jest udostępniony wszystkim, tak?

**Kamil Dubaniowski:** W takim wypadku tak to powinno właśnie wyglądać. Właśnie na to chciałem zwrócić uwagę, że uzależnienie oddziału w przypadku odwołania zupełnie mija się z celem. No bo to nie jest w żaden sposób działowe, to jest ogólnofirmowe.

**Damian Kamiński:** No więc ja się zastanawiam, czy pod tym kątem i odwołanie powinniśmy mieć trzeciego poziomu, czyli tak: moje, czy też mojego zespołu, udostępnione. I trzecie, włączamy sobie w ustawieniach systemowych, że ta instancja obsługuje JRWA i to jest sztywne, bo tu mamy coś sztywnego, jakąś teczkę. Tam mamy gotowe procesy, które zawsze są dwa, bo muszą być dwa i tak samo tu sztywno JRWA i tam lecimy w głąb. Musimy mieć tylko pewność, że wszyscy mogą widzieć całą strukturę JRWA.

**Kamil Dubaniowski:** Czyli wtedy to byłoby pewnie dla działów udostępnione, ale...

**Damian Kamiński:** Wtedy to. OK. Czyli udostępnione globalnie jakiś administrator zarządza, który dział ma dostęp, do którego węzła i w głąb, ale to by była niezależna.

**Kamil Dubaniowski:** W przypadku JRWA, wydaje mi się, że wszyscy widzą wszystko, jeśli masz dostęp do JRWA i twoim zadaniem jest wpinać tam sprawy albo później archiwizować. W mojej ocenie już widzisz wtedy całą strukturę JRWA. Ale też nie jestem specjalistą.

**Damian Kamiński:** Nie powiedziałbym, w sensie, zobacz, my pracujemy w naszym dziale. Janusz dostaje jakiś dokument do działu DEV. Musimy go obsłużyć. Korespondencja przychodząca. Czy ja na pewno powinienem? Ty się zajmujesz sprawami osobowymi, a jakimiś innymi proceduralnymi. Czy ja na pewno powinienem widzieć sprawy osobowe? Niekoniecznie powinienem widzieć strukturę JRWA. Może nawet mogę wpiąć w to, ale czy na podstawie tej struktury ja powinienem mieć dostęp? Dobra.

**Kamil Dubaniowski:** Nie mam takiej wiedzy, w sensie nie wiem, co dokładnie, nawet oni tam wpinają. To jest też porozumienie w zakresie.

**Janusz Bossak:** Zależy, do czego służy repozytorium, bo to nie jest...

**Damian Kamiński:** Dokładnie.

**Janusz Bossak:** Nośnik do tego, żeby przekazywać sobie sprawy, bo sprawy się przekazuje tradycyjnie. Natomiast repozytorium jest do czegoś statycznego bardziej. Ktoś chce mieć jakąś listę czegoś łatwo dostępną, związaną z działem i tak dalej. Tak się na przykład my tworzymy jakąś naszą dokumentację. Wyobraźmy sobie, że to jest nasze wewnętrzne wiki. Gdybyśmy w AMODIT-cie trzymali backlog, to moglibyśmy tworzyć foldery i pisać "funkcjonalność wykresu Gantta" i wszystkie rzeczy związane z Ganttem, byśmy podpisali pod ten folder i "funkcjonalność Gantta". A wszystkie dotyczące bezpieczeństwa, byśmy podpisali. Mało tego, moglibyśmy tę samą sprawę podpinać do wielu takich folderów, bo tak teraz można robić. Czyli jeżeli to dotyczy i Gantta, i bezpieczeństwa, to mogłoby być i tu, i tu. Czyli to jest kwestia organizacji pewnych informacji w pewną strukturę folderów i druga warstwa to jest udostępnianie tego, kto ma prawo to widzieć: czy wszyscy, czy tylko właśnie z działu. To jest, według mnie, tylko i wyłącznie, znaczy tylko, ale to "tylko" jest duże, sposób prezentowania pewnych informacji, inny sposób niż lista spraw.

**Damian Kamiński:** No bo widzicie, tu jeszcze pytam Claude'a: "JRWA to system klasyfikacji dokumentacji stosowany w administracji publicznej w Polsce". I tam zaraz jeszcze możemy dalej, ale bardziej bym w podstawowym założeniu oceniał to jako słowniki zagnieżdżone nieskończenie, bo to użytkownik określa, jak. Czyli to służy do sklasyfikowania konkretnej sprawy, a przez to dokumentów związanych z tą sprawą, niż nadaniu uprawnień. Niezależnie może być nadawanie uprawnień do konkretnych węzłów. Tak mi się wydaje.

**Janusz Bossak:** No.

**Kamil Dubaniowski:** Wydaje mi się, że tutaj w tym wypadku akurat, jak ja jeżdżę na te spotkania, chociażby ze szpitalami, to obsługuje dedykowany dział. Wpływa korespondencja. To jest dział kancelarii, który decyduje, że to będzie w tym węźle przechowywane. Później na koniec, potencjalnie, wchodzi dział archiwum, który też musi mieć dostęp do całej struktury. To nie jest tak, że ty jako pracownik działu decydujesz, gdzie wepniesz ten dokument w strukturę JRWA, bo ty nawet tego pewnie nie wiesz, to jest kancelaryjny dział.

**Damian Kamiński:** Mhm. Właśnie, OK, dochodzisz do meritum. Czyli węzeł JRWA jest dostępny tylko określonym użytkownikom, którzy mają wtedy dostęp przez całe JRWA i oni o tym decydują, a ja jako zwykły użytkownik nie muszę tego widzieć, nie muszę o tym wiedzieć i nie dziedziczę żadnych uprawnień.

**Kamil Dubaniowski:** Tak się spodziewałem, ale wiecie, to jest na bazie raczej nie doświadczeń, tylko logiki, jak ja rozumiem przynajmniej to spotkanie. Tak byłem.

**Janusz Bossak:** Ja to tak rozumiem. Przynajmniej jak sobie przekładam w głowie, jak to jest z planem kont. Księgowa wie, gdzie ten wydatek zaksięgować, na koszty zarządu, jakiś tam analityk. Taką czy siaką. I to jest dokładnie tutaj, tylko, że tu dział administracyjny decyduje, jaką sprawę zaksięgować, że to jest sprawa związana z czymś tam, i idzie do jakiegoś tam folderu. I to reguła. Podobna sytuacja, jak...

**Kamil Dubaniowski:** Dokładnie, JRWA też jest jakąś organizacją.

**Damian Kamiński:** Właśnie, i tu masz dostęp powszechny do struktury, a dostęp ograniczony do szczegółowych list, czyli każdy może ewentualnie zapoznać się ze strukturą, natomiast sama przynależność jakiejś sprawy do struktury nie daje uprawnień do konkretnych spraw. Czyli ja, powiedzmy, obsługując jakąś sprawę jako specjalista od tego tematu, mógłbym wskazać, że to powinno być w tej strukturze, w tym punkcie i mam dostęp do samej struktury, ale to nie znaczy, że ja będę widział w ramach tego punktu wszystkie inne sprawy. Tak bym to definiował.

**Kamil Dubaniowski:** To zmienia też założenie podstawowe naszych.

**Damian Kamiński:** Mogę, nie wykluczam tego, czyli tylko wtedy na poziomie administracji jakiś administrator mógłby powiedzieć, czyli z założenia...

**Kamil Dubaniowski:** Wydaje mi się, że powoli w tych dyskusjach dążymy do tego, że i tak będzie jakiś panel konfiguracji tego repozytorium.

**Damian Kamiński:** Tak.

**Kamil Dubaniowski:** Tak, ja będę sobie decydował, w jakim zakresie to wykorzystam. Jeśli to będzie pod JRWA, to mogę, na przykład, właśnie wyłączyć to domyślne nadawanie uprawnień, że masz dostęp do folderu, to masz dostęp do wszystkiego, co w nim jest. Nie jest możliwe, że mamy mieć dostęp do folderu, ale widzę tylko te sprawy, do których mam uprawnienia, bo byłem je w trakcie obiegu, bo może ja nie powinienem widzieć nawet w tym samym folderze, ale spraw innych użytkowników. Tylko te, które dotyczą mnie, które sprawy ja obsługiwałem, bo reszta to już jest dla mnie nieistotna.

**Łukasz Bott:** I ja bym w ten sposób przed.

**Damian Kamiński:** Dokładnie tak.

**Łukasz Bott:** To by to było zgodne z filozofią AMODIT-a. Czyli i to, co już powiedział, JRWA, to jest kwestia organizacji informacji, bardziej niż kwestia dostępu.

**Damian Kamiński:** I masz rację. Dokładnie tak. A jak wdrożymy, to nam wyjdzie.

**Łukasz Bott:** I tyle. Czyli ja mogę węzeł widzieć, tak?

**Damian Kamiński:** Tak.

**Łukasz Bott:** Ale jeżeli ja do niego wejdę i nic nie widzę, to znaczy tylko tyle, że albo nic o tym nie ma, albo jest coś, do czego ja i tak nie powinienem mieć uprawnień.

**Damian Kamiński:** Dokładnie, czyli ten węzeł JRWA powinien z założenia prezentować strukturę wszystkim. Ale służy tylko i wyłącznie filtrowaniu jako filtr słownikowy. Jak robiłem coś w tym węźle, to mi się wyświetli. Jak nic nie robiłem, to nic mi się nie wyświetli, ale mogę podpiąć każdą nową sprawę do tego węzła. A jest jakiś administrator JRWA, czyli jakieś właśnie biuro, które tym zarządza, które widzi całą treść tej struktury, jako taki po prostu administrator procesu. W zasadzie można to na poziomie procesu określić.

**Łukasz Bott:** Tak.

**Damian Kamiński:** Ale też nie musi mieć uprawnień do tych spraw.

**Damian Kamiński:** Nie, to już zakładam kogoś, kto jest z tym biurem, który odpowiada za ten porządek JRWA. Ale tu z kolei znowu nie musimy tworzyć jakichś funkcjonalności z tego poziomu. Możemy zarządzić na poziomie obserwatora/redaktora procesu. Czyli jeśli proces korespondencji jest obsługiwany w ramach JRWA, to na poziomie procesu korespondencji to biuro uzyskuje uprawnienia, bo jest tam wprowadzone jako obserwator lub też edytor, czy po prostu bierze udział w każdym przebiegu. Czyli jest odpowiedni etap, klasyfikacja, i oni są tam aktorem na tym etapie. Na tej podstawie, że to przez nich przeszło jako przez grupę, to mają dostęp do wglądu w te dokumenty wszystkie i tyle. Bo ktoś musi taki być i właśnie takie biuro i taki archiwista, który na koniec to wszystko zatwierdzi, że jest to zgodne z prawem. Co więcej, coś, co też musimy zaopiekować w kontekście JRWA, to możliwość wyeksportowania danych zgodnie ze strukturą JRWA, po to, żeby przynajmniej na razie jako MVP, móc zanieść na pendrive wszystkie niezbędne dokumenty XML do urzędu, do archiwum państwowego. Pewnie docelowo będzie trzeba zrobić też integrację API. Natomiast nikt jeszcze bezpośrednio raczej nas nie pytał, czy wy już to macie. Raczej każdy mówił: "Dobra, to na razie offline'owo, a potem w przyszłości gdzieś jakaś integracja bezpośrednia".

**Kamil Dubaniowski:** Też ten temat badałem. Trzeba by pewnie podejść kompleksowo, bo tam, zanim coś przekażesz, to musisz złożyć wniosek i to jest cały proces wokół tego, który moglibyśmy wtedy mieć zintegrowany. Czyli u nas by się składało ten wniosek. Po co składać wniosek?

**Damian Kamiński:** Właśnie. Tak jest.

**Kamil Dubaniowski:** Znaczy, po co ten eksport cyfrowy, jak i tak wniosek muszę wejść, zalogować się, no to jak już się zaloguję, żeby złożyć wniosek, to już wrzucę ten plik tam od razu.

**Damian Kamiński:** Może i masz rację. Ja tu nie mam wiedzy. Zawsze mówiłem, że w razie czego możemy zrobić, bo oni też, ktoś tu w LOT-cie chyba pytał. Powiedziałem, że jak będą chcieli, można przesłać, możemy przygotować na razie w formie offline'owej. Wygeneruje się paczka. Będziecie mieli ją, wiesz, jedno nie wyklucza drugiego. Oni też mogą chcieć zarchiwizować coś, co idzie przez API. Może też chcą, żeby zostało u nich w formie, w jakiej poszło.

**Kamil Dubaniowski:** I tak obstajesz przy tym, że JRWA pewnie będzie jako osobno, czyli najpierw zrobimy to, czego wymaga WIM, bo to już poszło i musimy, a JRWA nadal będzie pewnie tak, dopóki nie trafi się jakiś faktycznie klient. Roboty to jest, moim zdaniem, dużo więcej niż w tej pierwszej części, o której rozmawialiśmy. To i tak nie wszystko, bo ja nie do końca rozumiem te tematy związane z wybieraniem lokalizacji, później jakiegoś składu chronologicznego. Dwa, trzy lata temu to tak pooglądałem pod tym kątem, ale to jest już dla mnie trochę zawiłe. Nie jestem archiwistą. Może tamten nasz partner, nie pamiętam, kto to był, co był w Bydgoszczy w tym szpitalu onkologicznym, mogliby nam jakieś konsultacje w tym zakresie dać, bo gdzieś się w tym specjalizują.

**Damian Kamiński:** To może powinniśmy zrobić taki?

**Kamil Dubaniowski:** Też mi się tak wydaje, że nie ma co tu, wiecie, bo...

**Damian Kamiński:** Taki warsztat nawet odpłatnie, ale wiecie, jak startujemy, to...

**Kamil Dubaniowski:** Oni to jakoś zrobili w oparciu o model. Ja przyznaję, że się jakoś na tym specjalnie nie skupiałem. Janusz nawet nie miałem jak, bo oni nam nie udostępnili pulpitu. Ja byłem akurat zdalnie na tym spotkaniu. Janusz był na miejscu, mówił, że dobrze to wyszło. Jeśli chodzi o te tematy archiwum, my to mamy zrobione tak sobie, bo nie wiemy do końca, co mielibyśmy mieć, więc też nasze demo jest pod tym kątem słabe. No, ale tak z nimi pewnie trzeba by się spotkać i pogadać, co oni by potrzebowali, żeby to zrobić lepiej, albo jakoś systemowo w ogóle.

**Damian Kamiński:** Czyli ktoś wygrał przetarg i zrobił e-Dokumentację w AMODIT-cie, tak?

**Kamil Dubaniowski:** Nasz partner złapał klienta. To temu teraz ten klient do nich wrócił i znów robili prezentację w oparciu o to, co gdzieś tam lata temu dla nich przygotowali i my byliśmy jako wsparcie w tej prezentacji.

**Damian Kamiński:** Czyli to nie weszło produkcyjnie, tylko to był koncept, tak?

**Kamil Dubaniowski:** Koncept robili dla nich, dla tam kilku lat, więc pewnie też by się dało to i tak już tym, co mamy, może jakoś lepiej zrobić, ale tak jak mówię, no ja nie znam zakresu, co tam biznesowo jest potrzeba, a dwa, że nie widziałem tego, co oni zrobili, więc ciężko mi się odnieść. Więc z tych rzeczy, to ja jeszcze wyłapałem, no to na pewno to, co wspomniałem, czyli te foldery muszą być w jakiś sposób opisane konkretnymi parametrami, a co więcej, później wszystko, co do nich jest spięte, my musimy mieć opcję, tak mi się wydaje, żeby tu nie robić jakichś reguł dla folderów. My musimy mieć opcję pobrania tych parametrów na sprawę, czyli jak coś jest w folderze, tam informowanie wojewody o sytuacji w zarządach gminy. No to jeśli w tym folderze jest przypisane, że archiwizacja 10 lat, to my musimy to pobrać, pewnie lokalnie, na każdą sprawę, która jest w tym folderze, żeby zadziałała jakaś reguła automatyczna, albo jakaś funkcja, która jest w stanie odpytać o parametry z folderu, no i wtedy reguła okresowa, tak, która odpytuje, ile tu jest? Czy już minął termin i...

**Damian Kamiński:** No te.

**Kamil Dubaniowski:** I usuwa na przykład, tak? Czy oznacza jako do usunięcia albo do przekazania. No, która pobiera te parametry. No i tu jest konkretnie kolejny problem, niekoniecznie może on występuje u Piotra Buły, bo nie znam się, ale w tym naszym repozytorium sprawa może być w 50 folderach. I teraz każdy z tych 50 folderów może mieć inne parametry i teraz jak odpytać o to, co nas faktycznie interesuje? JRWA, nie wiem, pewnie raczej jest tak, że...

**Damian Kamiński:** Nie, to musiała być reguła.

**Kamil Dubaniowski:** Sprawa w jednym katalogu, ale ciężko powiedzieć. Znowu ta funkcja musi odpytać z jakiego katalogu. No, a jeśli sprawa będzie w więcej niż jednym, to trzeba by podać konkretnie nazwę katalogu, o który pytamy. Mamy na poziomie wdrożenia, no nie będziemy wiedzieli takiego. Mamy się odpytać.

**Damian Kamiński:** Nie będziemy wiedzieli, no jeśli będzie to repozytorium i ono będzie oznaczone, tak jak tu w przykładzie. Jeśli to jest dobre oznaczenie, no to wykrywamy sobie jakimś refleksem, że tu jest taka numeracja, czyli jest jakiś numer w kwadratowych nawiasach. Dojdziemy jakoś. Można mieć jakiś parametr, tak. Funkcja `GetRepositoryParams` jako powiesz właśnie parametry węzła.

**Kamil Dubaniowski:** Ale skąd będzie wiedział, pisząc regułę, z którego pobrać? Będziesz miał sprawę w pięćdziesiątym i sześćdziesiątym. I teraz w pięćdziesiątym jest 10, a w sześćdziesiątym 15. No właśnie o to mi chodzi, że pewnie nie.

**Damian Kamiński:** Ale nie, to pytanie, czy tak można? To może też ograniczenie wpięcia do max jednego węzła, tak?

**Kamil Dubaniowski:** I to też musiałby być konfiguracyjne. I to wszystko, moim zdaniem, trochę zaczyna się sprowadzać do tego, że repozytoriów może być danej organizacji więcej niż jedno i każde będzie miało inną definicję. Bo repozytorium JRWA będzie się opierało na innych zasadach. Inną definicję stworzysz właśnie, że nie dziedziczy uprawnień, podziałach, czy tam widzisz tylko to, do czego masz uprawnienia wynikające z obiegu sprawy. I to będzie zupełnie inne niż takie repozytorium, na przykład, dokumentów kancelaryjnych.

**Damian Kamiński:** Zgadzam się z tobą i dlatego ja sugeruję, żeby to był zupełnie odrębny węzeł włączany w ustawieniach systemowych. To jest JRWA cykl i tu jest, i wtedy mogą być w jednym JRWA i w innych, ale w ramach JRWA może być tylko przypięte do jednego.

**Kamil Dubaniowski:** Czyli nawet bym szedł w... I pytanie, czy to w takim jednym panelu zamykać? Bo to nie będzie pewnie nawet jakoś biznesowo zrozumiane, tak, że tu będzie tak ten poziom, tak, że tu jest repozytorium na takiej zasadzie, a tu jest JRWA. Definicja na takiej zasadzie i później w ramach procesu definiujesz, że w tym procesie można wpinać sprawy do repozytorium typu JRWA, zdefiniowanego tak i na takich zasadach, że mówię, no to już robi się spora zmiana.

**Damian Kamiński:** Aha, czy zrobić JRWA jako oddzielnie? Spoko. Według mnie też OK.

**Kamil Dubaniowski:** Dużo roboty, dlatego wątpię, że to wejdzie bez finansowania gdzieś tam od klienta.

**Damian Kamiński:** Czy może musimy określić jakieś MVP? Wiesz, żeby to było jakkolwiek prezentowane? Jestem bardzo ciekawy feedbacku LOT-u. Oni dostali od nas to dokładnie to środowisko. Dałem im to. Powiesz, lepiej dać coś, co jest niedopracowane, niż nie dać nic. Tak uznałem, bo najwyżej zadadzą pytania.

**Kamil Dubaniowski:** Bo nie mamy teraz takich klientów.

**Damian Kamiński:** A nie ma, a nie pozostają tylko z prezentacją. Bo jeśli nasza konkurencja dała, no to jak my nie dajemy, no to już słabiej wypadamy. I teraz jestem ciekawy, czy w ogóle przejdziemy do jakichś kolejnych etapów, a jeśli nie, to dobrze by było uzyskać jakiś feedback, dlaczego? Czy właśnie doświadczenia systemu były negatywne i w jakim zakresie? Mogą powiedzieć, że JRWA u was było dla nas w ogóle niezrozumiałe. I wtedy niekoniecznie, jeśli chcemy w to brnąć i obsługiwać, to może niekoniecznie powinniśmy czekać na finalne stosowanie, ale jakieś totalne MVP, które będzie miało sens zrobić, żeby móc to właśnie prezentować poprawnie. No, ale to wiecie, wyjdzie w praniu, tak? To nie mówię, że teraz podejmujemy tę decyzję. Na ten moment skupiamy się na WIM-ie, tak, żeby tam odhaczyć wymaganie repozytorium. Dobra, bo jesteśmy już chyba po czasie, też dużo zebraliśmy. Uważam, pozostaje jeszcze wkład pana...

**Janusz Bossak:** Znaczy...

**Damian Kamiński:** ...pana Piotra. Ja mogę wysłać za chwilę maila z prośbą, żeby przygotował taki zbiór funkcjonalności, których oczekuje, że ich repozytorium będzie posiadać.

**Janusz Bossak:** Dobra.

**Łukasz Bott:** Dobra.

**Kamil Dubaniowski:** Ja mam jeszcze jeden temat w kontekście WIM-u, bo widziałem, że wpadło jutro spotkanie. Mnie tam wyprosił Daniel, dzisiaj właściwie, możliwe, że już widzieliście. Wcześniej to jest w temacie tak was wprowadzę, nam Łukasz akurat chyba nie, ale was, że są problemy komunikacyjne, że mocno tam...

**Damian Kamiński:** Czekajcie, mi się zaczęło spotkanie. O Jezu. Dobra, przełączam się, przepraszam.

**Kamil Dubaniowski:** No. To ja już tobie. Nie wiem, czy Mateusz z tobą tam wczoraj gadał, Przemek, bo do mnie dzwonił, że są te problemy komunikacyjne w kontekście serwisu, bo serwis nie wie, jak do nich podchodzić. Bardzo roszczeniowo nas tutaj już zaczynają dyktować maile, tak, wręcz. Piotr, podpisując jako Piotr, Daniel zrobił to spotkanie, żeby to obgadać, ale do mnie wczoraj Mateusz dzwonił, że Przemek i on planują mi dać to wdrożenie, że ja będę jakby na celowniku. Więc ja powiedziałem od razu, że nie chcę tego projektu, to też tobie mówię.

**Janusz Bossak:** Nie wiem. Bardziej widziałem Damiana, bo on jest jakoś już zaangażowany. Tam podobno był jakiś konflikt na linii pan Piotr i Damian. Ale po ostatnich rozmowach nie wyglądało mi to na konflikt. Z tego, co ja z kolei z Mateuszem wczoraj rozmawiałem, to Mateusz twierdził, że on się zaangażuje tam osobiście.

**Kamil Dubaniowski:** Tak, tak też mnie zdziwił ten telefon później, więc ja mu powiedziałem od razu, że nie.

**Janusz Bossak:** I to raczej od Damiana, w tym kontekście nie.

**Łukasz Bott:** P.

**Kamil Dubaniowski:** Przemek sugerował, żeby dać mnie i Mateusz właśnie do mnie zadzwonił, co ja o tym myślę, to powiedziałem mu, że absolutnie. Znaczy ja mogę uczestniczyć tak, jak teraz, czyli robię po prostu, dostaję zlecenie, zrób to i ja to robię, ale ja nie chcę się tam angażować na full time. Byłem na spotkaniu, jednym idzie po 10 minutach. Ten Piotr już zaczął do mnie mieć jakieś problemy i się tam drzeć, więc to, że on Damiana tam wykluczył, to skończy się pewnie podobnie w ciągu kolejnych dwóch dni ze mną. Tak więc nie ma co tak do tego podchodzić, że tam Damiana "wymiotowali", bo taki jest ten człowiek.

**Janusz Bossak:** Strasznie konfliktowy, według mnie.

**Kamil Dubaniowski:** Tak, szuka wszędzie, gdzie się da. Stąd też Daniel tak zrobił to spotkanie, bo on już tam wielkimi literami zaczyna mu maile pisać, ten Piotr, z jakimiś tam roszczeniami, że to tylko ich dobra wola, że nam nie naliczyli kary. Już tam takie teksty padają. Także nie chcę tego projektu, bo wiem, że ja nie będę miał energii się z nim użerać. To powinien być ktoś na takim poziomie, jak był Piotr Pawłowski. Wydaje mi się, że to idealna osoba do tego wdrożenia i nawet nie patrząc na umiejętności takiej osoby, powinniśmy szukać do tego projektu, która po prostu po tych ośmiu godzinach roboty sobie oleje temat i będzie tam dalej, a ja będę siedział później po nocach znowu, bo pan Piotr będzie się tam darł na spotkaniu.

**Janusz Bossak:** Ja też nie jestem za tym, żebyście tam przed. Wydaje mi się, że tutaj Damian byłby OK. Tym bardziej, że już tam przeszedł jakieś problemy z tym panem Piotrem, więc może sobie jakoś tam wypracują, ale to jest człowiek rzeczywiście mocno konfliktowy. Trzeba znaleźć na niego sposób. I pewnie naszego Przemka Sołdackiego w to trzeba zaangażować, żeby on postawił trochę taki parasol ochronny. Żeby ten gościu sobie z nami po prostu nie leciał w kulki, bo tu wszyscy i Daniel, i wy, i podejrzewam i Wiktor, i wcześniej Fryderyk, wszyscy tam wkładają serce w to i robią, a ten gość po prostu po chamsku się zachowuje i właśnie takie teksty różne dziwne wrzuca. Potem się nagle z nim, że oni tak, nie wiem, to dwie ubiegłe nówkę ma, czy co?

**Kamil Dubaniowski:** No, takie mam wrażenie. Ja nie byłem na miejscu. Mateusz mówi, że był, że spotkanie, po czym jeden dzień, jeden temat, w ogóle jedno słowo. I on już zatrzymuje całe spotkanie i tam dziesięciominutowy wykład, bo jedno słowo dziś dołożyłem. I to wykład na zasadzie, że krzyczy. Mega specyficzny temat, raz pod kątem wdrożeniowym, a dwa pod kątem tej osoby. Myślę, że o wiele sprawniej szło bez niego w tym projekcie. Bo jak jest spotkanie na temat X, a ja powiedziałem jedno słowo nie tak i jestem w stanie je skorygować w ciągu minuty, po prostu zamienić, żeby on dobrze to zrozumiał, a on później przez 10 minut spotkania ze mną. To też przedłuża nam cały temat. Ale tak, jak mówię, jestem otwarty, żeby Damiana wspierać i robić zlecone tematy, ale ja nie chcę tego tematu prowadzić, bo raz, że tam byli. Już jest drugi czy nawet trzeci. Wdrożenie przez to przeszło. To już widać skalę, jaki to jest klient. I to nie jest też, moim zdaniem, temat, że damy Damianowi i on to zrobi, bo ten do końca roku jest nierealnie jedną osobą. Nawet nie wiem, czy dwie osoby jesteśmy w stanie to ogarnąć. Żeby się nie skończyło po prostu tak jak z projektem. Że był jeden znowu przedstawiony, jeszcze wtedy chyba nawet bez PM-a. Znowu się gdzieś pod koniec roku spotkamy, że nawet nie wiemy, co dokładnie robimy. I to też sugerowałem, że tam trzeba ten projekt zacząć od zera. Spisać wymagania, bo później będzie do końca projektu, tak jak teraz jest. Przecież to oczywiste jest, bo mamy jednym słowem napisane, że ma być.

**Janusz Bossak:** Tak, bez takich, że tak powiem, odpowiednich wymagań, czarno na białym, no to ten gościu nas będzie za każdym razem naciągał.

**Kamil Dubaniowski:** Nie skończymy tego projektu.

**Janusz Bossak:** Tak, bo on znajdzie, tak jak tutaj. Tak to komunikator. Przecież ja, przepraszam, już klnę, ale ja z nim o tym rozmawiałem, tak? I on wtedy mówił: "Tak, to jest taki komunikator". Koniec. Tak samo to repozytorium. Wiele rzeczy, on tam się wtedy godził, a teraz są niewłaściwe i teraz nawet podejrzewam, jeżeli się umówimy na coś, to się nagle za miesiąc lub dwa okaże, że nie, że on tak to nie miał na myśli. Więc z nim to trzeba wszystko na papierze.

**Kamil Dubaniowski:** Bardzo formalnie, dokładnie tak. Ale później, jak to, wiesz, nie, o to chodzi, tak, znajdziesz. Będziesz miał tu spisane, to się skończy tak, że będą krzyki i będzie naciskał, żeby robić po swojemu. To musi być ktoś mega asertywny i raz nastawiony na to, że, no, ale też widzisz jego podejście, tak jak mu się ktoś nie podoba, jak Damian. No to się stawiał, no to już nie ma Damiana. I tak będzie. My możemy spisać, co chcemy, a później postawisz mu papier przed nim. On ci powie, że "No i co z tego?" i już nie będzie chciał z tobą pracować. Więc dużo zależy też od Przemka, jak on do tego tematu podejdzie. Wszyscy mamy wątpliwości co do tego klienta i może być tak, że będziemy wypalać kolejne miesiące, a na końcu będziemy…

**Janusz Bossak:** Tak może być.

**Kamil Dubaniowski:** Dobra, no tylko tyle chciałem, w sensie, żebyście mniej więcej wiedzieli, co tam się wczoraj i dzisiaj.

**Łukasz Bott:** Ja miałem okazję. Proszę się, nie, nie wiem, czy na szczęście, czy nieszczęście, zdalni, ale tak osłuchałem się wykładu na temat, jak system powinien, ten programowanie być robione.

**Janusz Bossak:** Dokładnie.

**Łukasz Bott:** Chciałem tylko powiedzieć, że w AMODIT-cie to się to, co oni by robili, to czy to się robi troszeczkę inaczej, tak, tak i tak.

**Kamil Dubaniowski:** Dobra, nie przedłużam, nie zabieram czasu. Rozpisałem w międzyczasie temat tych integracji ustawień systemowych. Jeden wątek zostawiam gdzieś tam. Pogadamy sobie już pewnie w innym czasie, bo nie wiem do końca, co z historią edycji tych integracji, czy to w ogóle robimy jako część biznesową. Jeśli tak, to w jakim zakresie. Tyle, reszta jest już rozpisana. Przemek, tam z tego, co rozumiem, już będzie zaczynał działać.

**Łukasz Bott:** Dobrze.

**Janusz Bossak:** No dobra, tak robię.

**Kamil Dubaniowski:** Dzięki.

**Łukasz Bott:** Gotowe.

**Damian Kamiński:** Zatrzymano transkrypcję.

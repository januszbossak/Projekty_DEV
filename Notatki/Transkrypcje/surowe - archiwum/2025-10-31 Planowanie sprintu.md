**Transkrypcja**

31 października 2025, 09:02AM

**Janusz Bossak** 0:26  
Majka jesteście jesteście.

**Damian Kaminski** 0:28  
Cześć. Ja Jestem jeszcze Kamila nie ma.  
No dobra, to znaczy to też przy kamilu byłoby.  
Wartościowe, bo.  
Żeby się nie powtarzać się o jest.  
Dobra.  
Mam takie przemyślenie.  
Że.  
No nie mam na tyle wiedzy technicznej albo pewnej wiedzy technicznej.  
Żeby dobrze zaprojektować ten backend dla repozytorium plików i tutaj potrzebujemy po prostu takiego.  
No równorzędnego partnera no właśnie nie moja tak tylko czy to powinno być element? No domyślam się, że nie moja chciałbym to ustalić. Pytanie jak ty Kamil ewentualnie to robisz, chociaż raczej tutaj pewnie poprawiamy niż niż tworzymy coś nowego.

**Janusz Bossak** 1:09  
Ale tam twoja robota.

**Kamil Dubaniowski** 1:25  
Znaczy teraz przy tych redaktor owych było sporo nowego, ale ja trochę na takiej zasadzie, że właściwie daje temat przemkowi czy filipowi do tej pory głównie w Przemek robił jako pierwowzór? Filip, na przykład po nim już miał beknąć, więc raczej Przemek był dzień wiodącym i on ustala z Piotrem na przykład co trzeba po stronie backendu.

**Damian Kaminski** 1:25  
No bo.  
No.  
No dobra, tylko dalej bym powiedział, że to jest odtwórcze, czyli my backend mamy w kontekście struktury danych nie mamy tylko w funkcjonalności odczytu i zapisu do tej struktury i z tej struktury, a tu mówię o samej strukturze filler, czyli jakie tabele powinny być definiowane w ramach repozytorium i a nawet coś tutaj już zaproponowałem, tylko w zasadzie zaproponowałem poziom tabel, nie chcę wchodzić na w sensie, czyli, że może go być to takie tabele, nie chcę wchodzić w ogóle w szczegóły, co za tabelę.  
Mają mieć kolumny i co ma być kluczem dla tych kolumn? Jakie mają być relacje między tymi tabelami? No bo to nie moje zadanie już.  
Tylko pytanie właśnie, czy do tego przypisujemy Piotra w tym kontekście czy innego dewelopera.  
To niestety tutaj. No właśnie to Mateuszem mam taki problem, że Mateusz nie jest dostępny tyle czasu i pytanie, czy my z nim zdążymy i zaprojektować i zrobić, czy raczej właśnie tu potrzebne jest wsparcie kogoś innego, kto?  
Ustali architekturę, a Mateusz będzie bardziej wykonawców.  
Wspólnie no tam w oparciu o, ale jaja tak.

**Janusz Bossak** 2:56  
No.  
Mateusz ma tu jakby ryzyko, że tak powiem wszyte w siebie, no bo ale też, że tak powiem nie, no myślę, że on powinien się tam mocno zaangażować w to.  
Nawet po godzinach jak mu powiemy, żeby robił to będzie robił.  
On i tak rozlicza się godzinowo.

**Damian Kaminski** 3:19  
No tak się domyślam, tak samo jak ma już tam coś tam.  
Mariusz, to jest pokolenie z, ale to ze śmiechem naprawdę pozytywnym mówię.  
Na początku chyba wszyscy byli zdziwieni, którym wypowiedziałem już teraz przywykliśmy, ale te bóle głowy ibuprofenie, no ale odrabia i jego sprawa. Ja w to nie wnikam. Temat jest zrobiony i.  
Ale no no to jest takie zdarzenie właśnie z dzisiejszymi problemami, nie młodych ludzi pracowników jak podchodzą do.  
Do komunikacji do do pracy do wszystkiego.

**Janusz Bossak** 3:55  
Dobra.

**Damian Kaminski** 3:55  
Natomiast no tak jak mówię, mówię to pozytywnie, niemniej no to znaczy tak, czyli sugerujesz januszu, żeby powiedzieć mateuszowi, przeanalizuj, to daj uwagi. Hill, przygotuj to tak, jak powinno być. Czy ktoś ma to po nim rywalizować, czy zostawiamy to wolne, bo to jest odrębna aplikacja.

**Janusz Bossak** 4:11  
No co co doby.  
Co do backendu i do architektury tego backendu to jakoś większe mam zaufanie do Piotra.  
Że największe tak mam.

**Damian Kaminski** 4:22  
No.  
Domyślam się, ja też no mhm, ale.

**Janusz Bossak** 4:26  
I wolałbym, żeby to Piotr przynajmniej.  
Wyznaczył ramy.  
Tak, że robimy tak?  
Tak i tak, a resztę już nie chce sobie Mateusz tam czy ktoś tego weekendu kombinuje tak endpoint i tak dalej, ale mi chodzi o to, żeby Piotr architekturę.  
Że to ma być tak zrobione? Tak będzie komunikacja z użytkownikami. Tak ma być tam zapisywanie folderach. Tak ma być to tak, ma być to nie i takie wiesz, założenia nie.  
Kamienie milowe no fundamenty, że tak powiem konstrukcja na nim na tej konstrukcji, na tych założeniach Mateusz ma zrobić backend opracować tak, czyli endpoint, co jak kto tam będzie się chłopcy.

**Damian Kaminski** 5:16  
No właśnie to coś wam pokażę i pytanie czy.  
To powinien być taki poziom szczegółowości czy nie?  
W ramach tego repozytorium zrobiłem po prostu cały backend i tutaj jest o tu jest krótko, tylko te główne główne wytyczne i teraz tego wynikają pb i na przykład PI. Struktura danych tabeli, jakiś model bazodanowy.  
No i tutaj wymieniłem jakie te tabele mogą być?  
Mm natomiast.

**Janusz Bossak** 5:45  
Naprawdę, z całym szacunkiem do Twojej wiedzy i tak dalej, może nawet to jest dobrze, znaczy nawet się nie chce zastanawiać nad tym.

**Damian Kaminski** 5:53  
Nie, ale ja nie chcę wchodzić w szczegóły. Pytanie, czy ten poziom szczegółowości no.

**Janusz Bossak** 5:53  
To jest.  
Ale nie to nie to już jest za duży.

**Damian Kaminski** 5:59  
O k no właśnie.

**Janusz Bossak** 6:00  
Czyli ty jesteś biznes?  
Tak, twój poziom jest.

**Damian Kaminski** 6:03  
O k.  
No nie chcę robić czegoś, co jest błędne. Mhm.

**Janusz Bossak** 6:07  
Tak, twój poziom to jest. Ja chcę mieć strukturę folderów ową.  
Chce mieć uprawnienia, które działają tak i tak.  
Chce mieć przenoszenie, chcę mieć coś tam, chcę mieć coś tam, chcę mieć coś tam. To jest twój poziom juz kwasów.

**Damian Kaminski** 6:22  
O k. Dobrze, ale ale to może inaczej. Czy ten poziom szczegółowości ma być tu opisany? Ja nie muszę w niego wchodzić, ale mam wymienić, że struktura bazy danych, jakaś moja propozycja, nie muszę mogę to skasować, ale czy mam poprosić Piotra wypisz tu jakie mają być tabelę i kolumny w ramach tych tabel?

**Janusz Bossak** 6:23  
Tak.  
Pasować.  
A tam poczekaj jeszcze, bo to ten poprzedni ekran, który pokazywałeś tam.

**Damian Kaminski** 6:45  
Mhm proszę.

**Janusz Bossak** 6:47  
O tutaj, bo tu jest o to jest. No to jest poziom, o którym powinniśmy mówić tak kluczowe założenia techniczne backendu struktura organizacyjna przestrzenie.

**Damian Kaminski** 6:52  
Tak.

**Janusz Bossak** 6:57  
No o k. Przestrzeni foldery do 20 poziomów.  
Pliki, dobrze przechowywanie, pliki fizyczne na dysku na bazie nie na bazie danych metadane w dedykowanej tabeli, świetnie system uprawnień, dziedziczenie jest poziomu przestrzeni bez możliwości przerywania, świetnie obsługa plików maksymalnie 2 gigabajty. Zdolność z typami to jest bardzo dobrze. To jest koniec twojego poziomu.

**Damian Kaminski** 7:22  
O k. Tylko żeby kolejny poziom, że tak powiem wiedzieć jak robić, żeby oni sobie dobrze tą wiedzę przekazywali, bo tu mi się wydaje, że że mogą być to czy coś takiego im wrzucić proszę to uzupełnić. Według waszego uznania to nie jest żadne wytyczne, to może być na prowadzenie czy nie wchodzimy.

**Janusz Bossak** 7:25  
To.  
Nie znaczy, ja ja bym tutaj w opisie, jeżeli to jest struktura, ja bym to napisał tak, tytuł tego zaprojektowanie struktury danych i modelu bazodanowego u góry w tytule nie.

**Damian Kaminski** 7:51  
Mhm.

**Janusz Bossak** 7:52  
Dla projektowaniem, bo to jest zadanie, które mają zrobić teraz.

**Damian Kaminski** 7:52  
No.  
Mhm.

**Janusz Bossak** 8:01  
Tam struktury danych i modelu bazodanowego no do do repozytorium plików, ale też na początku nie ten repozytorium plików bardzo dobrze i teraz tutaj.  
W opisie na podstawie tamtych założeń, które są podane tym ilościowych również tak co do ilości tych poziomów co do wielkości p.  
Kilku zaprojektować zaproponować może tak zaproponować i zaprojektować.  
Strukturę danych.

**Damian Kaminski** 8:37  
Kurt, co tu się dzieje, że tu mogę dietować?

**Janusz Bossak** 8:41  
To jest jeden jakby zadanie dla deweloperów tak, czyli zaprojektowanie struktury danych, drugie może nawet wcześniejsze to jest zaproponowanie.  
Architektury aplikacji. O tak bym to nazwał.  
Tak, czyli właśnie to co tu się sprzeczaliśmy wczoraj i też tam z przemkiem nawet chyba są dac im tak, że to jest odrębna aplikacja.  
Czyli odrębny tam nie wiem, dl cokolwiek wczytywane komunikacja z systemem ma model będzie taki tak ten poziom tak czyli architektura aplikacji. To jest pierwszy.  
A pod nim dopiero ten jest drugi, czyli architektura bazy danych.  
Bo to będzie wynikało z tej architektury aplikacji, bo jeżeli w architekturze aplikacji zapiszemy sobie, że.  
To jest część amo tita.  
No to pewnie struktura może wyglądać inaczej będą to tabele wy a modlicie?  
A jeżeli strukturze aplikacji napiszemy, że to jest odrębna aplikacja, która komunikuje się tylko i wyłącznie na poziomie, tam nie wiem.  
Uprawnień użytkowników z czegokolwiek.  
To wtedy ta struktura może będzie inna tak, bo trzeba rozkminić na przykład to, co było w komunikatorze czy.  
Yy użytkownicy są kopie owani.  
I to jest pewien ból, jeżeli oni są kopiowane ani czy oni są tylko.  
Komunikowanie z ja w sumie nie wiem jak to jest. Właśnie brakuje tego poziomu do opisu komunikatora, jak to jest zrobione?  
Użyć komisji mają drugą odrębną tabelę w komunikatorze i wszyscy są kopią ani tam.  
Czy są utrzymane?

**Damian Kaminski** 10:28  
Nie odpowiem ci, nie odpowiem ci, nie chcę to zmyślić.

**Janusz Bossak** 10:30  
No właśnie i to jest ten poziom, który potrzebujemy tutaj i to mają rozkminić deweloperzy. Szczególności Piotr jako architekt systemowy.  
To jest jego zadanie.  
Wymyślać architekturę systemu i pilnować jej, żeby była spójna rozwijana w przyszłości i tak dalej jak on tą architekturę jakby zapoda to następnym zadaniem dewelopera jakiegokolwiek jest zaproponować, jak to za implementuje.

**Damian Kaminski** 11:02  
Mhm.

**Janusz Bossak** 11:03  
To powinno podlegać potem weryfikacji Piotra, że o k. To jest dobry. To jest dobry pomysł, to nie, bo coś tam wydajność. Na przykład tych danych.  
I tak to powinno powstawać. No czyli ty dajesz ten ogólny tutaj ogólne założenia, jakie są wymagania nasze jako biznesu?

**Damian Kaminski** 11:24  
Tak, to znaczy, wiesz, wiesz co czuję, że nie pracowaliśmy do tej pory.

**Janusz Bossak** 11:24  
Oni.

**Damian Kaminski** 11:28  
I jak nawet te 2 bym zostawił i pokazał Piotrowi tak, to tak to chcemy, żeby to było klarowne, żeby jak ty poświęcisz na to 2 3 4 godziny, to w zasadzie potem ten kto robi, nie ma już pytań do ciebie, bo tu wszystko jest rozpisane, bo do tej pory pracowaliśmy. Tak jest to.  
Piotr to bierze mówi, no to ja wiem w głowie, jak to trzeba zrobić i to robi, nie.

**Janusz Bossak** 11:51  
Właśnie on nie ma tak znaczy on ma to wiedzieć w głowie, ale ma to napisać.

**Damian Kaminski** 11:55  
Przełożyć na papier dokładnie tylko chodzi mi o to, żeby na przykład dać takie 2 zajawki.

**Janusz Bossak** 11:58  
Uczmy, uczmy Piotra jednej rzeczy, naprawdę go nauczmy, nauczmy ich włącza mikrofon i gada.  
Ja wiem, że on ma problem nawet z wysławianiem się czasami tam.  
Szybciej myśli niż mówi.  
I przez to taki i przerywa zdania i tak dalej, ale o k.  
Niech on to opowiada, jak nie potrafi mówić do głuchego telefonu, to niektóry z was tam będzie i będzie go jeszcze podpytywał Piotr ale powiedz jak jak to będzie zorganizowane jak to ta architektura będzie gdzie to będzie, jak to będzie się komunikowała za modlitwę, wiesz i go tam golcowa tak żeby wypowiedział to wszystko i z tego powstanie. Piękny opis architektury w którymś momencie.

**Damian Kaminski** 12:45  
O k no dobra, to jest jedno z podejść, czyli zrobić z nim spotkanie po prostu omówić punkt po punkcie. Co tu trzeba zrobić? TPBI?

**Janusz Bossak** 12:53  
To jest najszybciej, bo jak mu powie, że ma to zrobić, to on powie, że nie ma czasu, że zrobi to jutro w poniedziałek albo w poniedziałek mu wejdą 3 flipsy a jak go weźmiesz tutaj suche pro, potrzebuję z tobą 30 minut.

**Damian Kaminski** 12:56  
No właśnie, no tak.  
Będę ważniejsze rzeczy.

**Janusz Bossak** 13:06  
Omówimy architektury tego projektowanego pozyton podium i ból. Czujesz go tam to to powiedz, to powiedz to i powstanie jakaś tam wersja pierwsza i to uporządkuje.  
I to tam Piotrowi, teraz Piotr, czy to jest wszystko, czy coś jeszcze tutaj ci do głowy przychodzi, no.  
I no ważna i znowuż nagrywasz.

**Damian Kaminski** 13:26  
O k.

**Janusz Bossak** 13:29  
Spotkanie z nim przechodzić przez to, co to aj aj tam z treści ło i dopisujecie nie tu jeszcze trzeba uzupełnić jeszcze o tym zapomnieliśmy tak dalej później jak już będziemy taki pierwszy cykl mieli to nawet myślę, że.  
Będziemy w stanie opracować.  
Właśnie taką listę czy jakby sposób pytania Piotra o pewne rzeczy, bo to są powtarzalne rzeczy. My robimy, nie robimy samolotu, nagle tak my robimy ciągle oprogramowanie w zakresie dita.  
Więc tu się pojawiają te same tematy tak uprawnienia, użytkownicy, komunikacja z amor gitem, gdzie przechowywać pliki, gdzie przechowywać? Coś tam jest ciągle to samo, nie.  
Czy to ma być mikro serwis, czy nie microservices gdzie ten microservices miałby być jeżeli to będą jakieś tam inne rzeczy, więc nauczymy się jakby rozmawiać też i Piotra odpytywać o tą architekturę.

**Damian Kaminski** 14:14  
Mhm.  
No dobra, to poproszę go żeby.  
Żebyśmy się dzisiaj spotkali?

**Janusz Bossak** 14:32  
Dokładnie.

**Damian Kaminski** 14:34  
Dobra, to to mi rozmawialiście teraz?  
Czym wracamy do takiego Najwyższego poziomu tego, co zaproponował Kamil?

**Kamil Dubaniowski** 14:45  
Ja bym od tego wyszedł, bo moim zdaniem są niektórzy w planie już przeładowanie, czyli na przykład Adrian, który ma krzew, który ma ma kosa i który ma komar haba no nierealne. W 8 dni nawet jakieś minimalne vip z tego złożyć.

**Damian Kaminski** 14:45  
Czy co?  
Mhm, o Ki tu się zgadzam, ja bym coś takiego samego zrobił z adrianem, bo ja znowu mam poczucie, że to będzie trochę jak jak zaczął z tym sejm hubem, czyli coś co powiedzieliśmy tutaj o piotrze to dokładnie to samo chciałbym zrobić z adrianem, wziąć z nim, bo ja go dzisiaj tam pytam, wszystko niby jasne, ale znowu żeby się nie wy doktoryzować z tego ksw konektora tylko rozpiszę z nim to co jest do zrobienia, on coś tam już po wymieniał, ale na takim poziomie technicznym, że tam nic nie idzie zrozumieć.  
Chciałbym okroić to do tego, czego faktycznie potrzebujemy biznesowo.  
Ee.

**Janusz Bossak** 15:36  
Pytać pytać, nagrać zeznania, zbierać jesteśmy jak.

**Damian Kaminski** 15:39  
Dokładnie dobra. No to wróćmy. Czyli tak przypominam wam tylko, że już żebyśmy mieli jeden, no spójne źródło prawdy to tutaj w tym.  
Ogólnym programiści, testerzy mamy road mapy i tu mamy ten plik, więc tak to co?  
Odpowiadając na twoje pytanie, Kamil, to co ja bym chciał wziąć, to w zasadzie.  
4 pierwsze punkty stąd, czyli to bym chciał skończyć to rozpisać i to.

**Kamil Dubaniowski** 16:08  
No ale to nie angażuję.

**Damian Kaminski** 16:11  
Ee i to i nic i nic.  
Przepraszam, to i to to 5 punktów?  
To tu zakładam, że nie angażuje deweloperów, praktycznie może z Mariuszem tylko tam dość czytania, ale tak komunikator do końca.  
Tu jest mat i tu niestety widzę konflikt, że tu Mateusz ma pracę. Tu Mateusz ma pracę.  
Chociaż tu myśleliśmy jeszcze alternatywnie o ani wtedy.  
No ale nie wiem jak ania z tym jajem nie mam pojęcia jak to ocenić czy to jest radialne czy nie.  
Ee.  
No i tu się obawiam, że Mateusza nie starczy.  
Na na ten sprint.  
No ale z drugiej strony też to chyba nie ma co zakładać, że te repozytorium wyprodukujemy w jeden sprint.

**Janusz Bossak** 16:59  
Nie wiem.

**Damian Kaminski** 16:59  
Może 2 pytanie tylko, czy 2 wystarczą na Mateusza?

**Kamil Dubaniowski** 17:08  
Czyli na razie planujesz dla Mateusza ten komunikator się repozytorium?

**Damian Kaminski** 17:14  
I wiem, że to jest za dużo.

**Janusz Bossak** 17:18  
No i zauważy.

**Kamil Dubaniowski** 17:18  
Znaczy pytanie tak, p tak co my chcemy osiągnąć w tym sprzęcie w kontekście tego repozytorium może być tak, że backendu tam za dużo.

**Janusz Bossak** 17:30  
Czy wiecie trochę mamy wyprzedzenie, bo tam jednak filmik rozumiem trochę frontendu już zrobił.

**Damian Kaminski** 17:36  
Tak.

**Janusz Bossak** 17:37  
I to jest fajnie, że mamy to, więc zróbmy jakiś element backendowych, ale ja myślę, że jeżeli po 8 dniach będziemy mieli naprawdę rozk minioną architekturę i strukturę backendu.

**Damian Kaminski** 17:56  
To praca będzie przyjemna i szybka.

**Janusz Bossak** 17:58  
To będzie to duży wkład. Wolałbym nie dawać jeszcze do robienia w rozumieniu pisania kodu.

**Damian Kaminski** 18:06  
O k.

**Janusz Bossak** 18:06  
Tylko niech się zastanowią, ale po bożemu tak wiesz, nie żeby to było nie nam, że a wiem dobra to był tam zrobimy tak czy siak, nie, nie, nie to ma być napisane.

**Damian Kaminski** 18:07  
Rozpisanie.

**Janusz Bossak** 18:17  
Jakie endpoint będą do czego będą mają już ten front end, więc z filipem można porozmawiać, w którym miejscu on potrzebuje. Jakich danych, niech to wszyscy wszystko rozkminiają i spróbujmy to zrobić tak jak po.

**Damian Kaminski** 18:17  
O k.

**Janusz Bossak** 18:32  
Powinno się to robić tak jak podręcznym.

**Damian Kaminski** 18:35  
Dobrze pytanie, czy my to jakoś spisujemy? W sensie teraz na potrzeby tego spotkania i co ewentualnie proponujecie, czy po prostu notatniku czy jakieś nie wiem excel tego.

**Janusz Bossak** 18:36  
Powstanie projekt.  
Właśnie.  
Ale co?

**Damian Kaminski** 18:50  
Czyli czym się zajmujemy w tym sprincie tak wysoko poziomowe?

**Janusz Bossak** 18:55  
No dobrze.

**Kamil Dubaniowski** 18:57  
Ja bym to robił w perspektywie na ludzi, no bo wtedy będzie widać na przykład nie mam żadnego takiego sprecyzowanego celu dla Łukasza brodzkiego. No i pytanie czy ten komar hab musi robić Adrian?

**Janusz Bossak** 18:57  
No to.

**Damian Kaminski** 19:08  
No i bardzo dobre pytanie. Dobra to poczekajcie to odpale excela i na tym wysokim poziomie sobie to zróbmy.

**Janusz Bossak** 19:15  
Arek selon paxton.  
To jest na przykład tam jest taki planer w tym teams nie może z tego planera korzystać w tym naszym kanale sobie decydować.

**Damian Kaminski** 19:26  
A możemy też możemy?

**Janusz Bossak** 19:29  
Myślałam prymitywny proste narzędzie, no ale może?

**Damian Kaminski** 19:37  
Tylko.  
Jak to robić w kontekście zespołu?  
A ja tu kilka miałem podejść coś z tym sobie pisałem, ale.

**Janusz Bossak** 19:48  
Nie wiem, to jakoś można było.

**Damian Kaminski** 19:51  
Dobra dobra, można masz rację, bo to by musiało być tak tu.  
Chyba trzeba ten planer wtedy pod 5.

**Janusz Bossak** 20:18  
Dobrze.

**Damian Kaminski** 20:21  
Mm no dobra.

**Janusz Bossak** 20:24  
Zaraz zobaczę czy ja też tak widzę to.

**Damian Kaminski** 20:29  
Tylko może tutaj zamiast.  
Do wykonania będziemy sobie rzucać imiona, żeby to był. No zaraz zobaczymy.

**Janusz Bossak** 20:39  
Prawda przypisywać można do konkretnie przepis to masz konkretnie.

**Damian Kaminski** 20:43  
Tak tylko jak tak.

**Kamil Dubaniowski** 20:44  
Będą zaraz powiadomienia, czy też jest?

**Damian Kaminski** 20:46  
No właśnie będą powiadomienia szuja przypiszę na razie siebie zobaczę jak to będzie wyglądać w sensie czy jak ty Kamil uważasz, bo ja bym to wiedział, że zadania to jest pozycja, a tu są osoby, wtedy będzie łatwiej, tym pewnie zarządzić tak albo możemy wrócić do excela.

**Janusz Bossak** 21:02  
Bo tam, ale możesz przepiąć się na siatkę. Weź tam zobaczył góry nie kanban panem tylko o siatka i masz wtedy. No tak, nie.

**Damian Kaminski** 21:13  
Czekaj, tablica, harmonogram to nie tablica, a co tu mamy w tablicy o o k dobra, no to jest tak lepiej. Według mnie dobra projekt repozytorium, no możemy tu przepisać, mogą to widzieć do czego są?

**Janusz Bossak** 21:31  
Przecież to nawet jak będziemy zmieniać no to najwyżej no.

**Damian Kaminski** 21:42  
No dobrze.  
No to to mamy teraz dalej mamy.  
Przełącz się na razie na.

**Kamil Dubaniowski** 22:20  
Bierzesz to na siebie, tak?

**Damian Kaminski** 22:22  
Mog.  
Czy ty to weźmiesz?

**Kamil Dubaniowski** 22:25  
No dowolnie to już jakby jak uważasz możemy na końcu się podzielić.

**Damian Kaminski** 22:27  
Znaczy albo inaczej to a powiedz, bo ja tak ja powiedziałem, co ja widzę, co co jest potrzeba. No w zasadzie potrzeba jest taka, żeby realizować to.  
Albo to mi się nie otworzyło. No to zamykam, tylko to było tu.  
Na chwilkę wrócę.  
Niekoniecznie muszę to brać, znaczy uważam, że po prostu powinniśmy iść od góry, bo to są nasze priorytety. Tak to ułożyliśmy od góry.  
Ee, mogę to oddać, bo to jest jedna rzecz niezależna w sumie ja nie mam możliwości testu, więc może to powinno być u ciebie masz projekt masz jak testować maszyn szafira.  
No i tyle. Ja będę tylko ja będę tylko pośredniczył w przekazaniu do testów dla klienta, bo według mnie niezależnie od samej certyfikacji powinniśmy to dać im i powiedzieć, sprawdźcie, czy wszystko działa.

**Kamil Dubaniowski** 23:11  
Mhm.

**Damian Kaminski** 23:23  
Pomy się certyfikuje, a potem powiemy ani uwzględniliśmy, że u niego jest coś inaczej.  
I wszystko.  
W piach jeszcze teraz.

**Kamil Dubaniowski** 23:37  
Dzień dobry. No ja już to był jakby miał musiał w planie, więc.

**Damian Kaminski** 23:40  
No dobra, dobrze to w takim razie może tak sobie to otworze jak to otworzyć.

**Kamil Dubaniowski** 23:48  
Te medicum długopis.

**Damian Kaminski** 23:50  
Skończymy za chwilę.  
To się dzieje.  
Dobra.  
Dobra dalej mamy.  
Chce w konar tor a modified.  
Endu nie ma.  
Dalej było.  
Komunikat.  
Już konkretny.  
Dobra.  
Mm.  
No dobra no i jest ja też wywoła, który jest znany.  
Się zapytania, bo czyli tak to mamy to zostawiam może też rozpiszę, żeby to było jednak to.  
Dobra, czyli tak to jest zaopiekowane, to jest zaopiekowane, to jest zaopiekowane.  
To też na poziomie takim wysokim, bo tu trzeba to będzie porozbijać na kilka rzeczy. Na razie mówimy o integracji, jeszcze ten kwestia wizualizacji nowego schematu xml, ale to według mnie kolejne fazy, bo tego jeszcze nie mamy. Dopiero po 15 listopada będzie to przekazywane, więc no, ale też musimy to zaplanować przynajmniej projekt, żeby to potem sprawnie pod grać.  
To jest twoje, no i teraz mamy tutaj o rw, a czy my?

**Kamil Dubaniowski** 27:03  
Moim zdaniem na tym etapie w przyszłym spięcie to raczej tak samo jak z tym repozytorium, jak czyli projekt, żebyśmy znaczy wyznaczenie może kierunku celu, co my chcemy osiągnąć? Co chcemy kupić w Polsce? Jesteśmy chyba za daleko.

**Damian Kaminski** 27:03  
Jesteśmy.

**Janusz Bossak** 27:15  
Ja to rozpracowuję naprawdę i.

**Damian Kaminski** 27:17  
No właśnie, czy ty to do ciebie to Janusz przypisać, że ty to po prostu ustalisz, czy coś robimy, czy nie robimy o.

**Janusz Bossak** 27:21  
Tak.  
Tak, tak.

**Damian Kaminski** 27:25  
Bo to jest na tym poziomie na razie czyli.  
Dobra, czyli tak dostosowanie a modi pod yotova.

**Janusz Bossak** 27:33  
Dalej dalej w Las.  
To jest coraz trudniejsze.  
Mimo naszych naczelnym.  
Bo dzisiaj się rano na spacerze jeszcze pomyślałem o jednym problemie.  
No i zapytałem się tam oczywiście jaja, żeby zbadał rynek.  
No ale okazuje się, że zgodnie z moimi przypuszczeniami.  
Yy, że to nie jest tak, że każdy sobie widzi całej o RA.  
No i o trybuła nakłada się matryc.

**Damian Kaminski** 28:05  
No właśnie.

**Janusz Bossak** 28:07  
Kompetencji.

**Damian Kaminski** 28:09  
Czyli wynikającą ze struktur organizacji tak.

**Janusz Bossak** 28:11  
Dokładnie tak to jest w ogóle obowiązek, to jest wręcz w rozporządzeniem tak napisane.  
Że no zgodnie z ochroną danych osobowych tak dalej i minimalnych dostępów.  
Yy ludzie powinni mieć dostępy do tych.  
Jakby część i o RA, które ich dotyczy nie mogą sobie zakładać teczek, na przykład gdzieś tam nie wiem, księgowy sobie założy w Radzie nadzorczej teczkę, no nie?  
Księgowy sobie może założyć teczkę tam, gdzie ma dostęp do zakładanie teczek.  
Yy i tyle, on może dopisywać do istniejących teczek jakieś dokumenty, bo przyszły i tu się różni właśnie dopisywanie możesz zakładanie Nie możesz.

**Damian Kaminski** 28:59  
I to jest chyba to, dlaczego Kamil oparto repozytorium, prawda? Bo tam było przypisanie.

**Kamil Dubaniowski** 29:03  
Ja to.

**Damian Kaminski** 29:06  
Do działów.

**Kamil Dubaniowski** 29:06  
Powiedzmy, że miałem dużo dużo przesłanek, żeby to tak tak działało. Niekoniecznie właśnie to mi się podobało, że to jest parę działo, bo nawet tutaj wiedzy wtedy nie miałem, że to tak działa.

**Damian Kaminski** 29:17  
No ale jakieś tam uproszczenia poczyniłeś w kontekście tego co co wam modlicie się da.  
Znaczy tego, co powiedziałeś tutaj Janusz to same teczki, bo można nałożyć filtr na odnośniki do.

**Janusz Bossak** 29:23  
Więc.

**Damian Kaminski** 29:32  
Spraw, bo w zasadzie Teczka jest odnośnikiem, że widać wszystko, nawet jeśli nie mam dostępu.  
Tylko muszę ktoś mi musi powiedzieć, że to do tej teczki powinno być przypięte.  
Bo ja nie mając do niej dostępu, nie wiem co w niej jest. Po części nie mogę tylko na podstawie tytułu wywnioskować, no tylko zamów. Wchodzimy bardzo mocno już w temat.

**Janusz Bossak** 29:57  
Jest największym nasz.

**Damian Kaminski** 29:58  
Zróbmy to, może na designie poświęciliśmy to spotkanie temu, co?

**Janusz Bossak** 30:02  
Dobra, dobra.

**Damian Kaminski** 30:03  
Dobra, Kamil, to teraz powiedz co poza tym z tych niższych rzeczy, ty widzisz na ten sprint tak, czyli tu.

**Kamil Dubaniowski** 30:11  
Nie ma tego narodu mapie, ale moim zdaniem to już jest fala zgłoszeń odnośnie wzmianek, to kompletnie nie działa jak powinno, więc ja mam w planie na Mariusza tak zmianki i tego jest na tyle już dużo.  
Że prawdopodobnie najlepiej zrobić od nowa.  
Bo go tam co się nie dotkniemy to jest coś nie tak, więc Mariusz szacuję, że to jest 60% jego sprintu, więc cel moim zdaniem.  
Jedyny jaki powinien już mieć na ten sprint.

**Janusz Bossak** 30:42  
Dokładnie dokładnie i to jest taki poziom, jakby oczekiwał. To jest zadanie dla niego i on ma to dowieść. Ma po tym spięcie. To działać po prostu i mamy po tym spięcie. Znaczy, no to bardzo upraszczam. Tak, ale właśnie tak to powinno działać. Po tym sprzęcie powinniśmy o tym temacie zapomnieć. Nigdy więcej nie pojawiają się problemy wzmiankach.  
Temat rozwiązany stabilny, najlepiej jakby były do tego napisane testy to end, to to byłby taki poziom rozwiązania tematu.  
Poświęciliśmy napisaliśmy testy, jesteśmy w stanie to kontrolować.

**Damian Kaminski** 31:14  
Mhm.

**Janusz Bossak** 31:20  
No byłoby ideałem takie coś.  
Pewnie się tak nie uda tutaj, no ale.

**Damian Kaminski** 31:27  
No jak się nie uda w jeden film to będzie w 2. No ale podejmujemy temat, to już wiecie jak już jest podjęty to to kiedyś będzie skończony.

**Kamil Dubaniowski** 31:36  
To jest spoza wrót mapy, ale moim zdaniem ważne.  
Dla Adriana miałem tego sobie napad, to już jest rozpisane.  
Dla przemka coś co jest naród mapie mniej ważne, ale jako, że no nie widzę innych ważniejszych dla przemka, to chciałbym zamknąć temat fraj.  
W tej wersji robi tak, jak się umówiliśmy. W pierwszym kwartale robimy pvp, czyli odtwarzamy jak było.  
I tutaj będzie potrzebny backend.

**Damian Kaminski** 32:07  
Ok, ale to przypiszesz, czyli tak for usta.  
Systemowych te.  
Może chodzi mi o to, że nie robimy do tego nowego mechanizmu, tylko.

**Kamil Dubaniowski** 32:21  
Tak, ktoś będzie musiał przepisać pytanie, kto?

**Damian Kaminski** 32:22  
Dobra, to już nie wchodzę na poziom szczegółów jak po prostu temat o k.

**Kamil Dubaniowski** 32:26  
Mam bardziej kto, nie, żebyśmy też zaplanowali. No bo to jednak jakaś tam robota jest, ale to możemy jakoś.

**Damian Kaminski** 32:31  
A no to dobrze to.  
Tą.

**Kamil Dubaniowski** 32:34  
Patrząc, kto będzie wolny, może być nie wiem. Łukasz robił te ustawienia systemowe. Do tej pory Adrian.

**Damian Kaminski** 32:37  
A.  
Ania albo Łukasz bo bo ania i Łukasz na razie nie są w ogóle zaopiekowani, więc.  
Więc jedno z nich.

**Kamil Dubaniowski** 32:46  
No tutaj my ani.  
Dajmy ani kasza bym wiedział chyba w tym komarch kawie, ale coś pogadamy i nasze co mam na liście to jest dla ani też.

**Damian Kaminski** 33:00  
Poczekaj od razu przypiszę to co jeszcze pamiętam joby to to możemy przypisać tu Marek, Jestem sobie kierownikiem.  
Oj coś tu słabo to.

**Kamil Dubaniowski** 33:17  
Ani chciałbym dać jedno z zadań Mariusza. No też było tam szacowane chyba na efekt 15, więc powiedzmy, że może stanowić już jakiś cel, a jest istotną zmianą. Nawet ostatnio to wyszło gdzieś na spotkaniach szablony jako podgląd szablon, bo teraz gdzieś tam w nauce ładują do każdej sprawy. Ten sam plik jako załącznik.

**Damian Kaminski** 33:25  
Mhm.

**Kamil Dubaniowski** 33:38  
I tego już były tam no 1000, z tego co kojarzę.

**Damian Kaminski** 33:42  
Tak tak, 1000 tam było dziesiątki, chyba 1000.

**Kamil Dubaniowski** 33:45  
No.

**Damian Kaminski** 33:47  
No i to jest temat, który wraca. No wczoraj nawet pokazywałem to ja to robiłem w specyficzny sposób.

**Janusz Bossak** 33:54  
Co oni tam załączyli jakieś regulacje czy co?

**Damian Kaminski** 33:54  
No tu się zgadzam.

**Kamil Dubaniowski** 33:58  
Dasz tak chyba szczegółowo nie weszliśmy nawet wykonały.

**Damian Kaminski** 34:00  
Zaraz cię pokażę, zaraz się pokaże tak w jedną minutę potrzebę biznesową, gdzie to trzeba już pokazuje.

**Janusz Bossak** 34:08  
Czuję tak, by to wydaje mi się, że to.

**Damian Kaminski** 34:11  
Jak ja to zrobiłem, a jak oni to zrobili od razu pokażę różnicę i i no źle zrobili według mnie, ale zrobili żeby im było wygodniej, czyli jest tak są delegacje.  
Wyjeżdżam na delegację i tutaj mam zapoznałem się z opisem procedury służbowej i tu mam tą ten opis. Tak to sobie podpiołem tylko, że żeby go przeczytać to muszę go pobrać, ale to jest według mnie jak ktoś myśli o optymalne ności systemu bardziej optymalne, mimo że niewygodne pobrało mi i mam tu sobie jakiś tam dokument to jest tylko pokazówka, a jak oni robili wczytywanie i ten szablon do Opola, żeby można było go tu podejrzeć i teraz jest ile?

**Janusz Bossak** 34:39  
Ten poza.

**Damian Kaminski** 34:53  
Formularzy delegacji czy tam ichniejszych jakiś tam procesów tyle jest takich samych dokumentów, tylko po to, żeby to widzieć tutaj.

**Janusz Bossak** 35:02  
No i tu trochę zapraszamy, czekajcie, bo to jest ciekawy wątek.

**Damian Kaminski** 35:02  
To jest totalnym bezsensem.

**Janusz Bossak** 35:08  
Ja wczoraj miałem takie przemyślenia jeszcze odnośnie tego filmu i tego repozytorium.  
Czy my?  
Znaczy, nie nie to, żebym chciał, jakby już teraz zmienić, bo z panem Piotrem się nie dogadamy.  
Ale uważam, że jest to.  
Zbędny ruch.

**Damian Kaminski** 35:27  
Podglądów szablonów.

**Janusz Bossak** 35:29  
Nie, nie mówię o repozytorium filmu.

**Kamil Dubaniowski** 35:29  
Repozytorium.

**Janusz Bossak** 35:32  
Bo to mi się skojarzyło tak, bo mając repozytorium takie jak jest w zimie.  
Tam umieścili byśmy czy umieściłby klient pewnie taki dokument.  
I tu jakoś.  
Limonkową tak znaczy jest dokument repozytorium.

**Damian Kaminski** 35:47  
Tak kliknę, otwiera mu się w nowej zakładce.

**Janusz Bossak** 35:51  
Tak tylko pytanie, czy to jest?

**Damian Kaminski** 35:52  
Tak, mhm.

**Janusz Bossak** 35:55  
Zgodne z filozofią, a modrica właśnie nie bardzo tak.

**Damian Kaminski** 36:00  
Czemu?

**Janusz Bossak** 36:00  
Mogłoby być nie no, bo modlitwa jest procesowy tak, czyli ten.  
Dokument podróży służbowej czy opisu podróży służbowej akurat taki.

**Damian Kaminski** 36:11  
No.

**Janusz Bossak** 36:13  
Można dostarczyć inaczej, jest przecież to było prawej stronie panem help u.  
I opisie help u dla tej procedury tu powinien być Napisany ten dokument tu po prostu powinni być wrzucony jako tekst.

**Damian Kaminski** 36:32  
No ale.  
Jako techno, ale jeśli.  
Grafiki też się da.  
No nie wiem, nie będę się spierał, ale.

**Janusz Bossak** 36:45  
Jeden jeden z przypadków, tak mówiliśmy o tych właśnie, żeby były.  
Glony, które można nas prawie podglądać i to uważam, że jest bardzo dobry pomysł, bo jest bardzo dużo takich przypadków, gdzie trzeba mieć jakieś dokumenty, które są.  
Nie po to, żeby z nich skorzystać w rozumieniu wypełnić je, ale żeby je pokazać, nie.  
I tak jak teraz, jakbyś miał ten dokument pdf podpięty jako szablon o to on tutaj się pojawia nie. No jak jest problem, że tu kliknąć i był kuba podgląd.

**Damian Kaminski** 37:20  
Oczko powinno być dokładniej widzę podgląd.  
To znaczy, nie, nie, nie, nie sugeruję, że na pewno oczko, ale coś jak jakiś ficzer, że mogę pobrać, a mogę podejrzeć.

**Janusz Bossak** 37:31  
Po prostu nie robimy podglądów dla dokumentów, jeżeli nie chcemy już tam odkładać tego gdzieś tam jako pliki, no bo te podglądy wiecie, że one powstają jako tam jakieś od pegi nie i my wyświetlamy tak naprawdę to i od pegi, ale Jestem mechanizm, który Piotr chce tutaj zastosować w repozytorium właśnie tym filmu, czyli wykorzystać to, co ja chciałem od samego początku, czyli g picture, który może robić w lot, tylko, że to właśnie zajmuje tam parę sekund nie i może być i jest zasobożerne, no bo.

**Damian Kaminski** 37:44  
No.

**Janusz Bossak** 38:02  
Ten podmiot musi się wygenerować 1000 razy każdym razem, jak ktoś poglądem.

**Damian Kaminski** 38:06  
Tylko tutaj akurat to znaczy, tak to będzie prostsze, żeby to kiedy picture generowało na na żądanie. Ale jeśli chodzi o szablony, to stworzenie tego podglądu szablonu w postaci od pega nawet powiedziałbym, że tu akurat mogłoby być zasadne, bo szablonów jest dużo mniej niż założenia plików repozytorium.  
Tak zakładam i w przypadku takim po prostu częściej do niego ktoś zagląda, ale to jest wtórne. Możemy na razie zrobić np. Tak jak powiedziałeś, że to ktoś klika i generuje w tym momencie czeka chwilę i już.

**Janusz Bossak** 38:38  
Ja bym powiedział tak, że my powinniśmy zdefiniować problem biznesowym. Problem biznesowym polega na tym, że klienci użytkownicy mają pewną pulę stałych dokumentów.  
Jak właśnie różnego rodzaju instrukcje, regulaminy i tak dalej, które chcą mieć wyświetlane.  
Na sprawach.  
Bez konieczności ich nazwijmy multipli kowania.  
I koniec to jest problematyczne i.

**Damian Kaminski** 39:05  
Wiecie co to znaczy to się zgadzam i to powinien określić Kamil i chyba powinniśmy iść dalej. Najwyżej jak starczy nam czasu to wrócimy do poszczególnych problemów, bo znowu przez.  
Dziękujemy, tak, wchodzimy bardzo głęboko w konkretne zadanie.

**Janusz Bossak** 39:22  
Znaczy.  
Dlaczego nie? Ale to jest ważne z jednej strony, bo też to pokazuje, jak powinniśmy myśleć o pewnych problemach, to Przepraszam za dygresję dzisiaj jest temat tych krów od rana już od siódmej ranami, tutaj najpierw stanik pisał teraz do mnie Kamil maciąg dzwonił i tak dalej.

**Damian Kaminski** 39:24  
A mam.  
Jakie krów?

**Janusz Bossak** 39:47  
No tych paszportów krów i tam rejestracji to kiedyś tam mówiłem.

**Damian Kaminski** 39:50  
Aha o k.

**Janusz Bossak** 39:52  
No i.  
Ten stanik pisze do mnie Janusz, jaka jest wycena na oc r paszportu krowy?

**Damian Kaminski** 40:03  
Jaką chcemy?

**Janusz Bossak** 40:04  
Witam nie ale poczekaj, bo to pokazuje poziom rozumowania nie mówię, ale czy ty wiesz po co to jest robione? Nie wiem.

**Damian Kaminski** 40:12  
No właśnie.

**Janusz Bossak** 40:16  
Czyli, ale i teraz wracając do naszego tematu, chodzi mi o to, że niektórzy z nas każdy z nas mogą mieć jakby.  
Bardzo wąskie spojrzenie na problem.  
I próbują rozwiązać ten problem, a naszym zadaniem tutaj jako.  
Projekt nerów jest zawsze ten step back tak i szukanie szerszego kontekstu powiązań między różnymi rzeczami, tak jak tu w tym przypadku i repozytorium i poglądami i tak dalej, bo my musimy znajdować rozwiązania w miarę ogólne, na pewne ogólne problemy, a nie rozwiązywać pojedynczy problem.  
O to mi tylko chodziło. U nas w tym w tej dygresji.

**Damian Kaminski** 40:59  
Mhm.  
Ale nie zgadzam się z tobą. Masz rację, bo może tam w ogóle nie jest potrzebny o cerę w kontekście tych.  
Paszportów.

**Janusz Bossak** 41:08  
Wiem już to te kropy, nieważne no tutaj tak, bo gdzie ten podgląd taki siaki może z repozytorium jak będziemy mieli, może tu może w szablonach może nie może z GD picture. Może nie zgadnę picture może i od peggy my musimy patrzeć na to szerzej, no.

**Damian Kaminski** 41:22  
Szeroko to znaczy szeroko patrząc to powiedziałbym, tak, tu mamy 2 aspekty ten aspekt, który ja pokazuję i do tego mogłoby być wykorzystane repozytorium, bo mamy jeden plik, który jest szablonem, ale tak naprawdę on nie jest szablonem w rozumieniu amo. Dita tylko jest dokumentem do zapoznania się regulaminem w stałym w kontekście swojej struktury i treści.  
A inny aspekt podglądu szablonu to jest mam nazwany szablony umowa taka i taka, ale ja po nazwie nie Jestem w stanie rozróżnić czy ja mam zastosować to uczy tą więc jak wejdę w podgląd i zobaczę konkretny parametr tego szablonu czyli czy on ma taki zapis czy ma taki zapis pozwoli mi to wybrać który szablon ja chce wyprodukować zamiast go produkować na pałę po prostu klikać jeden drugi, trzeci piąty, więc to jest ta różnica między powiedzmy czymś co jest regulaminem do wyświetlenia wtedy z repozytorium.

**Janusz Bossak** 42:11  
No tak.

**Damian Kaminski** 42:18  
Jak najbardziej, a czymś co jest faktycznym podglądem szablonu w celu wybrania tego, który mam, na podstawie którego mam stworzyć dokument wynikający z szablony i treści formularza.

**Janusz Bossak** 42:28  
No tak tak.  
Dokładnie tak.  
Dobra, jedźmy dalej.

**Damian Kaminski** 42:35  
No dobra, to to Kamil masz masz rozpisane w sensie omówione co co trzeba by uwzględnić nie.

**Kamil Dubaniowski** 42:43  
Czy w tym wypadku, którego podgląd ja rozumiem, że to podgląd z repozytorium to nie ruszamy? To wieś, bo w mojej ocenie osobny typ pola Odnośnik do dokumentu z repozytoriów. No takie dosadne, tak, no ale dobra to na razie podglądy tak, żeby zaopiekować.

**Damian Kaminski** 42:43  
Ale dobra.  
Tylko podno.  
No to już przeszłość jakaś tak?

**Kamil Dubaniowski** 42:58  
Na razie w tej formie.

**Damian Kaminski** 43:00  
Dobra, ale tu ania backend i frontend.

**Kamil Dubaniowski** 43:00  
Yy.  
No tak tak.

**Damian Kaminski** 43:05  
Dobra, o k.

**Kamil Dubaniowski** 43:08  
To już mówiłem Przemek i mam dla niego diagram. Nie wiem, czy chcemy coś robić, to jest pytanie.

**Janusz Bossak** 43:17  
No na razie ja gram ja gram spada na niższą.

**Kamil Dubaniowski** 43:18  
Bo mp jeden jest.

**Damian Kaminski** 43:22  
Znaczy było pytanie, co Przemek jeszcze ma tak, bo wczoraj zakładam, że dla niego będzie prostym tematem, bo to jest robienie 2 przycisków i powielenie go w ramach wszystkich tych i w zasadzie więcej jest backendu niż frontu, tak?

**Kamil Dubaniowski** 43:30  
No da się.  
Wraca się i ja dla przemka z kluczowych tematów nie mam. No nic, jest diagramie spora i dałem tą bazę wiedzy.

**Janusz Bossak** 43:41  
Poczekaj.  
Tych ustawieniach systemowych, bo to mówisz w ustawieniach systemowych tak to faraj a przemyk sołdecki teraz na którymś spotkaniu powiedział, że właśnie coś tam próbował robić przez ustawienia systemowe i nie mógł.

**Kamil Dubaniowski** 43:47  
Tak, tak, tak.

**Damian Kaminski** 43:47  
Tak.

**Kamil Dubaniowski** 43:55  
Kwestia wersji nie były jakiegoś przycisku, ale to jakby w nowszej było Przemek zrobił męża do starszych.

**Damian Kaminski** 44:03  
No tak, ale nie mógł w nowej, a mógł w starej tak więc no po to to jest, żebyśmy wyłapywali takie rzeczy według mnie to.

**Janusz Bossak** 44:04  
O k.  
No.

**Kamil Dubaniowski** 44:12  
Nie mógł zwiększyć ilości pól na formularzu, bo nie było przycisku.

**Janusz Bossak** 44:15  
A no właśnie i tam gdzieś coś musiał przejść, tak?

**Damian Kaminski** 44:17  
No więc tu nie ma. No masz lat maksymalna jest wpływ w ogóle nie jest zdefiniowane.

**Janusz Bossak** 44:22  
Może to uzupełnijmy od razu nie.

**Kamil Dubaniowski** 44:24  
To jest zrobione już tak tam szymek się odniósł, że że że on to zrobił tylko że nie z mężem do starszych wersji zarobił tylko chyba do deweloper i grudniowej.

**Janusz Bossak** 44:25  
A już rozumiem.

**Kamil Dubaniowski** 44:34  
Ale to to jakby już zapakowane, bo to do tej pory było też w osobnym oknie robione chyba z tego co kojarzę albo nie dało się i po prostu to co było przynieść ciekawostkę.

**Damian Kaminski** 44:43  
Już zaraz spojrzymy.

**Janusz Bossak** 44:47  
No bo tam cały ten ciąg zdarzeń tak owszem oka wie sądeckiego był, że.  
To znaczy, to się wiąże z edytorem formularza, że mu nie powiedział, że już nie może dodawać pól. To było pierwsze.

**Damian Kaminski** 44:58  
Tak, tak.

**Kamil Dubaniowski** 44:59  
Tak no ja mam to zadanie. No w sumie to jest taki minimalny, ale to też nie jest duży temat dla przemka, bo mam kilka usprawnień, żeby dodał szukanie po typie w tym edytorze formularza, zapamiętywanie zakładki, w której byłem ostatnio, czyli ten temat bardzo rozdmuchany przez Daniela, czyli, że oni więcej pracują na liście niż na edytorze i dlaczego edytor jest pierwszy, to teraz będzie im zapamiętywał, gdzie byli ostatnio zmiana ścieżki dodawania nowego pola to jest też nie zaopiekowana, że teraz bardzo jest słaby x tego.

**Janusz Bossak** 44:59  
Tak.

**Damian Kaminski** 45:28  
Czekaj, czekaj, czekaj, czekaj za szybko w sensie ja mam już to zapisywać.

**Kamil Dubaniowski** 45:31  
Znaczy ja tego nie rozpisuję, no nie, nie ja to to, to bym uznał jako jeden ogólny, czyli dalsze usprawnienie edytora formularza. No bo tam jest trochę jeszcze.

**Damian Kaminski** 45:38  
Ale poczekaj, popatrzmy na to, w sensie to jest tragedia, w sensie czego tu brakuje, żeby to, bo to jest jak rozumiem wycięte i powiększone ze starych ustawień systemowych, bo nie mamy backendu do tego.

**Kamil Dubaniowski** 45:51  
Tak.

**Damian Kaminski** 45:53  
Bo to jest jak to jest złożone, jak to wygląda, to jest ja wiem, że tu rzadko kto zagląda tylko w razie potrzeby, ale no tragiczne.  
Tylko, że pewnej rzeczy aha ok, bo to w tle po prostu działa stary mechanizm.  
O k.  
Nie da się tego starego połączyć z reaktorem, tu trzeba ten backend po nowemu, tak.  
No dobra, no to są 4 pola. No pytanie, co nie ktoś nie może zrobić w sensie one gdzieś, co w bazie danych zrobienie do tego backendu to nie jest chyba.

**Kamil Dubaniowski** 46:33  
Tak, czy to jest najważniejsze?

**Janusz Bossak** 46:35  
Teraz nie rozwiązujemy, znaczy generalnie temat jest do zaopiekowania i musi pytać.

**Damian Kaminski** 46:37  
Dobry.

**Kamil Dubaniowski** 46:39  
No bo te okna mamy też w planie chyba na drugi kwartał wszystkie okna z ustawień systemowych to jest między innymi wynikiem.

**Damian Kaminski** 46:43  
No dobra, dobra, to jeśli tak podchodzimy to.

**Janusz Bossak** 46:45  
Chwilą przed chwilą mówiliście o tym edytorze diagramu. Ja uważam, że lepiej byłoby.  
A ten moment zostali, ten jest diagramu tak jak jest.

**Damian Kaminski** 46:53  
No.

**Janusz Bossak** 46:57  
No i nawet go już tam jakby włączyć do.  
Dita, żeby był natomiast skupić się na dopracowaniu, ale takim naprawdę już super dopracowaniu tego edytora formularza. Nie żeby to naprawdę konsultanci, żeby się na niego przenieśli. Ja wczoraj robiłem też właśnie tą pioter va, no i muszę wam powiedzieć, że 50 procentach przypadków przełączałem się na listę. Nie.

**Damian Kaminski** 47:25  
No właśnie, tylko edytor formularza to jest powiedziane bardzo wszyscy wiemy, do czego dążymy, w sensie, żeby, ale tak bardzo wysoko poziomowa, czyli do wyrównania. Ale czy my wiemy, czego brakuje? Bo według mnie tutaj chodzi o zadania, czyli ktoś z nas?  
Musi te zadania wytyczyć i to jest praca, bo odtworzenie ich dla przemka według mnie nie jest problemem, tylko znalezienie tych różnic i i i je, i ich opisanie.

**Janusz Bossak** 47:44  
Tak.

**Kamil Dubaniowski** 47:54  
Znaczy wiecie, no tak, to to to jak nie znajdzie, to my musimy powiedzieć. Ja Jestem ciekaw co tam. Janusz to już było, może już jest zaopiekowana część takich krytyków, ja już nie wypatrywałem szczerze mówiąc raczej wszystkie funkcjonalności są.

**Janusz Bossak** 47:57  
Tak.

**Damian Kaminski** 48:00  
Nowość.

**Janusz Bossak** 48:07  
Na przykład.  
Yy, no co tam, mogę Jeszcze raz nie przypomnę sobie jakoś tak.

**Kamil Dubaniowski** 48:14  
Miejscowo to nie jest dobrze zrobiony w sensie, że złe doświadczenia jest pracy z tym, ale no da się tam.

**Janusz Bossak** 48:18  
To jest.  
No właśnie, ale my musimy.  
No to też właśnie.

**Kamil Dubaniowski** 48:23  
No takie bym nauce na ten sparing tak taki dałbym cel na ten sparing, bo wyrównanie no tak bym tego nie nazwał, bo tak jak mówię no nie mamy do czego wyrównywać, bo my mamy już dużo więcej niż było w starym edytorze graficznym, ale ten remix jest to poprawie naprawdę.

**Damian Kaminski** 48:23  
No bo nie przekonamy ludzi nie jak.

**Janusz Bossak** 48:25  
Bo nie.  
Jest do poprawy dużo tak, tak, tak, tak, tak.  
No wiesz, to na to się na pewno nakładają jakieś przyzwyczajenia, nie że.

**Damian Kaminski** 48:48  
Oczywiście trzeba się na nowo przyzwyczaić.

**Kamil Dubaniowski** 48:49  
Ale.

**Janusz Bossak** 48:51  
To na pewno.

**Kamil Dubaniowski** 48:51  
W ogóle zacząć korzystać to jest ja. Ja szczerze od dłuższego czasu korzystałem ze starego edytora, w sensie jak miałem poukładać formularz, może to dlatego jakby mi jak nie sprawia większych problemów i ja nie widzę tych wad, które widzi Daniel, który nie korzystał nigdy telegraficznego. No i teraz się czepia każdej pierdoły.

**Damian Kaminski** 49:13  
No dobrze, ale to to w sumie dochodzisz do kolejnego, no.

**Janusz Bossak** 49:14  
Szacunkiem dla mnie.  
Daniel jest mało, że tak powiem referencyjny.

**Damian Kaminski** 49:20  
No niestety ja już o tym też mówiłem w sensie.  
Ja bym powiedział, nie chcę tego bardzo ogólnikowa, ale powiedziałbym tak, że Daniel słabo znałem odejść niestety.

**Janusz Bossak** 49:31  
No właśnie.

**Damian Kaminski** 49:33  
No tak no tak, bo każdy każdy ma swoje cechy, nie.

**Janusz Bossak** 49:34  
Znaczy no jest to jakiś klient, tak można powiedzieć klient słabo znający amonit.  
No i tyle no tak i trzeba to też umieć zaopiekować, czyli skoro człowiek nie znający modlitwa czy słabo znająca morita ma takie problemy, to znaczy, że inni słabo znająca modli to też będą mieli takie problemy.

**Damian Kaminski** 49:53  
A takich jest przewaga.

**Janusz Bossak** 49:55  
No właśnie więc trzeba takich słuchać. No to to nie jest to, że on jest niewłaściwym.  
Znaczy chodzi mi o jego pomysły, tak, że nie zawsze są jakby właściwe. Natomiast spostrzeżenia jak najbardziej tak.

**Damian Kaminski** 50:01  
Klientem.

**Janusz Bossak** 50:08  
Coś jest dla niego niewygodne, coś jest nie w tym miejscu co on by się spodziewał. No to okej, takich rzeczy trzeba słuchać.  
Niekoniecznie słuchać jego rozwiązań, jak on by to rozwiązał, to o to nie chodzi.

**Damian Kaminski** 50:20  
Mhm, problemów po prostu z czym ma wyzwania?

**Janusz Bossak** 50:21  
Słuchać problemów, a nie jego propozycji rozwiązania.

**Kamil Dubaniowski** 50:27  
Dobra, czyli diagram je w takim razie z tego planu?

**Damian Kaminski** 50:30  
Ale poczekaj to teraz Kamil w kontekście jeszcze właśnie układania co z listą?

**Kamil Dubaniowski** 50:37  
Listę opiekuje Filip na i teraz też mam ją w planie. Nie, nie, nie, jeszcze nie doszliśmy do tego.

**Damian Kaminski** 50:37  
Ból.  
No to mamy zapisane, czekaj.  
No właśnie i tam właśnie może lista pól tak i tutaj dodaje.

**Kamil Dubaniowski** 50:48  
Znaczy, nie chcę teraz wyciąg.  
Z tego Filipa będzie wyglądała jakbym nie wiem, no bo Filip już zrobił dużą część, jak pisałem mu zadania, on aktualnie teraz też w tym sprzęcie jeszcze to kontynuuję, bo bo co miałeś na myśli, żeby przemka to zaangażować?

**Damian Kaminski** 50:54  
Jak to wyciągać?  
No.  
Nie, nie w ogóle nie, nie, nie chodzi mi o to, że lista pól. Pytanie co tu jest do zrobienia w sensie.

**Kamil Dubaniowski** 51:10  
Tu jest temat wyrównania, bo tam jest dużo braków względem starej wersji nie ma na przykład odnośnika do słownika szybkiego, tak jak było w starej wersji, nie ma w ogóle ustawień pola, tak tam na razie wyświetlamy listę i pokazujemy jakie pola somi pozwalamy edytować nazwy.  
Także tam to jest naprawdę taki poziom vip.

**Damian Kaminski** 51:28  
Dobra, ale to jest jedno wyrównanie, a te przenoszenie właśnie szybkie do innej sekcji to to też planuje, że to będzie na tej liście.

**Kamil Dubaniowski** 51:39  
Co masz na myśli przenoszenie? Bo tam teraz ten nowy widok?

**Damian Kaminski** 51:40  
Bo wczoraj cię nie było i wczoraj padł taki no pomysł nowatorski, bo tego w ogóle nigdzie nie mamy ze strony Janusza, że już pokazuje, tylko muszę. My tu chyba tego nie mam. Dobrze, że zaznaczamy 5 pól na przykład z kontrolerem i wtedy je sobie przesuwam.

**Kamil Dubaniowski** 52:00  
Mhm.

**Damian Kaminski** 52:03  
Ja nie mówię, że to Janusz rzucił taki pomysł, ja go ona nie oceniam na razie, bo nie wiem jak właśnie trzeba go doprecyzować.  
Natomiast pytanie, czy faktycznie?  
Znaczy tak, to jest jedno z podejść pytanie jaką mamy na to alternatywę w kontekście listy?

**Kamil Dubaniowski** 52:19  
No dziś to jest na razie pojedyncze przenosimy pojedyncze Polak europosłem to już jest i tak usprawnienie względem starej wersji, bo tam trzeba było zmieniać kolejność patrząc na numerki i zapisywać zmiany.  
No więc teraz po prostu łapiesz za element, ale fakt jest taki, że no nie jest to zmiana masowa. W starej wsi też nie była, no bo każdy pole musiałeś przeklikać zmienić numer.

**Janusz Bossak** 52:39  
Tutaj.

**Damian Kaminski** 52:41  
No nie wiem, znaczy była, była były Czechy boxy i Janusz na to zwrócił uwagę. To prawda były checkboxy przenieść.

**Kamil Dubaniowski** 52:46  
Ale przestrzeń wybiorę przez ten w dół.

**Damian Kaminski** 52:49  
Tak, nie, nie, to inaczej mam na myśli przeniesienie do innej sekcji zbioru zbioru pól.

**Kamil Dubaniowski** 52:56  
Tak, że zmieniamy sekcja.

**Damian Kaminski** 52:56  
Nie samo tak tak, tak, tak, tak.

**Janusz Bossak** 53:00  
Znaczy co?

**Damian Kaminski** 53:00  
Wiecie no to znowu.

**Janusz Bossak** 53:02  
Ja mam jeszcze taką.

**Kamil Dubaniowski** 53:02  
No mam też pisane ta akcje masowe, tam było usuwanie, którego też nie mamy nie masowe, ale było mamy to przenoszenie między sekcjami i to też zaznaczyłem sobie, że dało się masowo. Nie mam na razie na to pomysłu, bo mamy dyrektyw dropła może niepotrzebnie.  
Ee też takie zaznaczenie elementów, później ich złapanie i wędrowanie z nimi przez długi formularz do jakiejś tam konkretnej sekcji też będzie słabe, więc tak ten drop tu jest na minus w tym wypadku.

**Damian Kaminski** 53:26  
Też mam takie poczucie.  
Też mam takie poczucie.

**Janusz Bossak** 53:30  
Moja natomiast na to miałem pomysł taki, że jak zaznaczysz kilka.  
Pól na formularzu i chwycisz w celu przenoszenia to wtedy.  
W mojej wizji pojawia się dynamicznym taki prawy panel, który reprezentował.  
Tylko prostokąty sekcji tak sekcja pierwsza sekcja druga sekcja, czyli to z nazwami tych sekcji nie i to sobie przenosisz na ten prawy panel, który reprezentuje te sekcje i puszczać w jakiejś tam sekcji.

**Damian Kaminski** 54:03  
To znaczy, to jest takie już podejście typowo popowe, bo jeszcze jest prostsze w kontekście takim bym powiedział właśnie, że się dynamicznie tutaj nie zmienia, nie przeładowuje się to tylko można zaznaczyć, powiedzmy z kontrolerem jak zaznaczysz z kontrolerem 2 to zmienia się prawy sidebar, bo też wczoraj o tym mówiliśmy i wtedy tutaj pojawia się menu kontekstowe dla więcej niż jednego elementu.  
Ja nie określam co w tym menu może być w przyszłości, ale dzisiaj nad potrzeby te co omawiamy, mogłoby się tu pojawić, przenieść do sekcji i wskazujesz tylko sekcję, klikasz przenieś i to przenosi. Według tej kolejności, które jest tu do tamtej sekcji, na samym końcu tej sekcji i wtedy zjeżdżam do tej sekcji i układam nie, bo to też jest podejście.

**Janusz Bossak** 54:45  
Temat jest taki, żeby już tak trochę zaparkować to j.  
Jest cały szereg zgłoszeń, to nawet w tej chwili dosłownie. Piotr napisał, że brak obsługi błędów przy edycji pól na formularzu nie zdublowałam nazwę pola. Zmiana się nie zapisała, ale nie dostałem żadnej informacji o błędzie. Tak to się wczytuje w ten problem, który miał Przemek, że dodał Polek, które się nie dodawało, bo już nie było miejsca na dodawanie, więc.

**Damian Kaminski** 55:04  
No właśnie.

**Janusz Bossak** 55:13  
Z.  
Według mnie trzeba tak zaopiekuj my wszystkie problemy, które są i ja mam uwagę taką, że tak jak tutaj widzę, to jest wersja 109 tam.

**Damian Kaminski** 55:15  
Zaopiekujemy błędem nowe ficzery tak.

**Kamil Dubaniowski** 55:26  
Tak.

**Janusz Bossak** 55:26  
Gdzieś tam zobacz, no.

**Damian Kaminski** 55:26  
Tak tak, ta sama co ma modlitw astra fox.

**Janusz Bossak** 55:30  
Ale już jest przecież nowsza wersja u pszemka widziałem bez tych linii, już tam pewnie ileś rzeczy ma zaopiekowany ich więc wygrywamy te nowsze wersje o tak jak tutaj.

**Damian Kaminski** 55:42  
No to trzeba poprosić tego Michała napiszę.

**Janusz Bossak** 55:44  
Żeby też, bo rozumiem, że to chcemy pchać do tej wersji nawet czerwcowej. Tak, bo to jednak jest element tego formularza.  
I dopóty do można, no to przynajmniej to wrzucajmy, żeby ten formularz tam był coraz lepszy, coraz lepszy coraz lepszy, tak.

**Kamil Dubaniowski** 56:02  
No to też decyzja, bo w sumie Przemek o mnie wczoraj pytał, czy te usprawnienia sprawdzenia. Nie wiem jak to nazwać zmiany, niedoróbki, niedoróbki, Jestem świadom, że no do czerwcowej musimy, ale jak coś zmieniamy właśnie koncepcję czegoś, to też lecimy od czerwcowej wzwyż czy na przykład zmiana koncepcji to jest już?

**Janusz Bossak** 56:20  
No pytanie jak jak jaka zmiana koncepcji nie może nie może już tam jakieś draken dropy na na wiele może nie, ale błędy tak jak w to co mówił Przemek, czy to co mówił teraz Piotr?  
Czy jakieś drobne usprawnienia tak które tam robimy? No to według mnie powinny lecieć do czerwcowej, no.

**Kamil Dubaniowski** 56:42  
Ale o k temat jest za jakby zaznaczony wiemy do czego dążymy, więc na razie dla przemka ten formularz i tu jest sporo.  
Więc może to też będzie wystarczający?

**Damian Kaminski** 56:52  
Bo też mam takie przemyślenie, że wiecie, żeby dobrze przykładać dobrze interpretować, może lewar tego co zrobimy na to, jaki to będzie miało wpływ, bo dalej to jest raz technologicznie poprawa tego długu i usprawnienie i tak dalej, a 2 to jest.  
Teraz skupiamy się trochę na usprawnianiu wdrożeń, bo jeśli my poprawiamy wix, to jest w zasadzie usprawnianie wdrożeń, tylko znowu.  
Ile czasu poświęcamy na edycję formularza?

**Janusz Bossak** 57:23  
I ważne, jeżeli to będzie.  
5%.  
Szybciej to jest to 5% szybciej, po prostu jak usprawnimy inny element, jak to na przykład przenoszenie procesów, to będzie kolejne 2% czy 3% czy 5% i to nie jest tak, że my zrobimy jedną rzecz i o sprawdziliśmy, nie my musimy zrobić 20 30 drobnych usprawnień, tylko że każde się przyczyni do tego poprawienia. O tą jeden dzień krócej zamiast robić tydzień, to robiłem.  
4 dni, natomiast 5 tak.

**Damian Kaminski** 58:00  
Mhm.

**Janusz Bossak** 58:01  
I o to chodzi nie, bo trochę tutaj, trochę tutaj trochę, tu szybciej łatwiej się pola dodaje. Łatwiej się reguły pisze. Łatwiej się przenosi między tymi łatwiej się uprawnienia nadaje w każdej czynności, coś będzie łatwiej, trochę nie.  
Więc tutaj.

**Damian Kaminski** 58:17  
To się z tobą zgadzam, że tak uprawnienia według mnie to jest game changer, to co my zrobiliśmy teraz, to naprawdę jest inny. W ogóle sposób zarządzania tym poglądu świadomości z jednego ekranu, co jak jest ustawione fillm natomiast to czy ja zaznaczę 2 pola pojedynczo czy podwójnie, to już jest fajny fischer, ale bez niego. Ja to zrobię w 10 sekund dłużej, nie.  
Czyli nie będzie minutę dłużej wdrożenie, ale o k dobra, po prostu chodzi mi o to, że są rzeczy, które naprawdę usprawniają, a są rzeczy, które, no są fajnym elementem. Natomiast w kontekście usprawnienia to one są już drugorzędne.  
Bardziej jest to bayerem niż niż usprawnieniem dobra, ale to wszystko trzeba robić, bo bajery też są istotne z punktu widzenia marketingowego, więc.

**Kamil Dubaniowski** 59:12  
Dobra, ja mam stopni temat dla Filipa właśnie to co padło matryce uprawnień tam cały czas jest kwestia, że to mogłoby być bardziej czytelne oznaczenia tych wyliczeń. No nie mam na to jeszcze planu, cały czas się wysypuje gdzieś tam, ale no chciałbym to zaopiekować w tym przyszłym sprincie też miejmy na uwadze, że ten sprint tak naprawdę zgodnie z naszymi ustaleniami jest zamykającym paczkę.

**Damian Kaminski** 59:12  
Wszystko.  
No.  
No właśnie.

**Kamil Dubaniowski** 59:38  
Marcowym.  
Grudniową Przepraszam.  
Więc więc nic już facto powinniśmy zacząć te drugą część kwartału stabilizować tą wersję, a nie do niej dorzucę jeszcze.

**Damian Kaminski** 59:53  
Tylko tutaj Kamil, ty nie masz na to planów, w sensie nie, nie wiesz jeszcze jak zrobić. No właśnie i to może na designie powinniśmy przedyskutować.

**Kamil Dubaniowski** 59:58  
Nie wiemy jak nie, nie wiem jeszcze jak.  
Ja ja myślę, że to będzie przegadany design dopóki i nie mam w ogóle na to kompletnie może powinienem spisać problemy i wtedy będzie o czym dyskutować, bo jak zaczniemy szukać tych problemów wspólnie, to to skończymy na szukaniu problemów.

**Damian Kaminski** 1:00:17  
Znaczy, ja mam takie poczucie, że.  
Że na podstawie tych naszych doświadczeń, że.  
Wyświetlać powinniśmy minimum, czyli.  
To, że to dziedziczy?  
To nie powinno się raczej wyświetlać. My powinniśmy wyświetlać wyjątki.

**Kamil Dubaniowski** 1:00:31  
Znaczy w tej matrycy dla mnie to było o tyle kluczowe, że widząc te wszystkie.  
Dzięki. Ja mam świadomość, że jeśli zmienię teraz coś na górnej sekcji, na przykład na etapie star.  
Na poziomie sekcji to wszystkie te mi po prostu się się zaktualizują również po tej jednej zmianie, czyli jak zmienisz sekcję domyśla na etapie start edycji nie wiem na.  
Odczyt to wszystkie te poniżej, ze spinaczem po prostu odziedziczą.  
To ustawienie, żeby była ta świadomość, że ta jedna zmiana wpływa na wszystkie poniżej, ze spinaczem może to być tak jak Przemek sugerował, żeby te ustawienia, które dziedziczą po prostu były szalone. No i do tego na razie się przychylam, że tylko te które.

**Damian Kaminski** 1:01:19  
Ale po, ale dobra to cię nie rozumiemy. O k masz rację, że dziedziczą tylko pytanie.  
Ile jest takich, które dziedziczą, a ile jest takich, które nie dziedziczą, bo według mnie więcej jest takich, które dziedziczą, żeby to odwrócić. W sensie zmierzam do tego, że pokazywać wyjątki, a nie, a nie.

**Kamil Dubaniowski** 1:01:33  
No tak, bo to mówiłem, że wyjątki będą w kolorze.

**Damian Kaminski** 1:01:39  
Teraz kolejna rzecz, która może tu też jest istotna. Mamy tutaj tak tak pokazane przestrzeni jest dość dużo.  
Czasami nazwy pól są podobne, bo są to techniczne coś tam jeszcze doliczamy albo jest nie wiem jakaś opcja, jeden opcja 2 czy opis opcja i opis, wybór coś takiego i pytanie czy tutaj też nie pomogłoby wyświetlenie jakieś ikonki tego typu? No bo znowu sprowadzamy to do tabeli dużej tabeli. W przypadku dużych formularzy, co w mojej opinii tutaj przewagą właśnie listy.  
Listy reguł było wprowadzenie tego koloru, który determinuje, jaki to jest typ.

**Kamil Dubaniowski** 1:02:22  
No torby trzeba mam projekt to było już u kristiny, żeby po prostu dla tych konkretnych typów pól przemian chwilę ekran.

**Damian Kaminski** 1:02:33  
Mhm.

**Kamil Dubaniowski** 1:02:33  
No i to też mam jako Plan dla przemka na tym sprintu, chociażby tak, czyli w ramach usprawnienia vixa, bo to też zwracali uwagę konsultanci, że tam jest zbyt czarno białe. To wszystko na tym edytorze graficznym i wszystko się zlewa, więc chciałbym, żeby ikony tematycznie.

**Damian Kaminski** 1:02:40  
No.  
Tak.

**Kamil Dubaniowski** 1:02:50  
Po typie no jakiś kolor miały przepisane, więc jeśli to już ogarniemy no to to można propagować i na listę pól i na to matryce chociaż znowu na matrycy powiedzieli, że jest zbyt kolorowo, że to rozprasza, więc może tam sam tekst. No ale tak na razie kazałem filipowi listy pól te ikony w ogóle wyrzucić, bo miał błędne inne niż Przemek zaktualizował, więc na razie jest zupełnie wywaliliśmy zostawiłem sam tekst, wydaje mi się, że możliwe, że to wręcz powinno być tak, że.

**Damian Kaminski** 1:02:59  
To się zgadza.

**Kamil Dubaniowski** 1:03:20  
W kolumnie typ jest faktycznie sam tekst, a ta ikona będzie obok nazwy systemowej pole.

**Damian Kaminski** 1:03:23  
Mhm.  
No.  
Mogłoby tak być, a kto mówił, że jest za kolorowo?

**Kamil Dubaniowski** 1:03:32  
Na matrycy uprawnień to mówił Mateusz kołakowski, chociażby, że tam po prostu tutaj, przy dużych formularzach tak kolorystyka tam już zakłóca odczyty. No nie wiem, to takie wiecie, też pierwsze wrażenia. No ale ważne dobra, więc znaczy mamy mamy na tapecie temat, tak, ja chciałbym w tym sprincie, przynajmniej w pierwszej połowie skupić się i zrobić jakiś.

**Damian Kaminski** 1:03:48  
Nie no ważna ale.  
O k.

**Kamil Dubaniowski** 1:03:57  
Okap tego co wiem, co chce zmienić, później możemy to przegadać. Ja też przedstawię te swoje problemy, które gdzieś tam nie blokują, bo to jest to, że to jest matryca i że to się krzyżowo na siebie nakłada i jeszcze doszła ta kolumna z domyślnymi ustawieniami to tam naprawdę jest więcej niż jeden wymiar i to mocno mi komplikuje temat, że że no nie da się zaznaczyć to co dziedziczy na szaro, bo czasami dziedziczenie to jest wyjątek.  
No i teraz część dziedziczeniem będzie na szaro, a część dziedziczenia będzie w kolorze, bo jest wyjątkiem od reguły, bo ustawieniem domyślnym jest na przykład modyfikacja, a na jakimś konkretnym polu uznałem, że nie modyfikacja tylko dzielić z sekcji. No i to jest wyjątek. Dziedziczenie z sekcji staje się wyjątkiem i i wtedy już to przy zmianie takiej jakby Najwyższego poziomu nie jest intuicyjne. Dlaczego mi się to nie zmienia?  
Dlaczego tu akurat to nie działa ta zmiana?  
A też z matrycy nie wynika trzeba by dopiero zagłębić się w ttip, więc dobra zostawmy, nie dyskutujemy teraz, bo się tam ja już nad tym trochę jak Adrian doktory zuje, no ale nie da się inaczej przypadki są.

**Damian Kaminski** 1:05:01  
Wiesz, to jest też tak, że.  
Dzisiaj byś w ogóle tego nie dostrzegł, a tu jednak już pokazujesz bardzo dużo, więc nawet jak zmieniam to po zmianie powinienem zrobić, a ty przyjąłeś, powinienem zrobić przynajmniej rzut oka. Nie jak ja coś tu zmieniam na domyślnym.  
Nie działa.  
Nie działa.  
Czy ja coś źle robię?

**Kamil Dubaniowski** 1:05:33  
Nie no dobrze.  
Ale wydaje mi się, że coś w ogóle wysypało i nie wiem czy nie napisali sobie tutaj zmian, bo wczoraj wszystkie ikony na Górze były po lewej zwróciłem na to uwagę filipowi to przeniósł do prawej, a w docelowym projektu typu użytkownika był po lewej, a reszta była po prawej.  
Yy więc nie wiem czy nie napisał sobie jakiejś zmian. 100.

**Damian Kaminski** 1:05:58  
No nie działa, to w sensie zmierzam do tego, że jak ustawiam odczyt to z kroluje i.

**Kamil Dubaniowski** 1:06:01  
A na innych poziomach.

**Damian Kaminski** 1:06:07  
To widzę od razu się zmieniło i nawet jeśli gdzieś jest jakiś wyjątek, to wtedy najadę i zobaczę tak uprawnienie domyślne uprawnienie do myślenia, a tutaj mam Dziedzic w sekcji o k. Czyli dziedziczy stąd tak.  
No.  
I tak to jest duże usprawnienie, że jak ja coś zmienię, to ja od razu to widzę, jakie jest to, jaki jest skutek tego dla całej listy formularza, więc to, że gdzieś tam czegoś nie pokażemy, to też nie jest.

**Kamil Dubaniowski** 1:06:26  
No.  
No to jest też.  
Tak to jest największy game change tak, bo tutaj też schodzimy do poziomu tabeli, wręcz nawet tak, czyli widzisz, no dosłownie wszystko, dlatego to się staje może gdzieś przy koloryzowane tak przy dużych formularzach, bo tego jest mnóstwo. No ale masz pogląd na całość. Czyli wiesz jak tabela działa w całości, bo widzisz jakie są ustawienia uprawnień na tabeli, ale też widzisz jakie są już wewnątrz tabeli na polach, no ale dobra, no to jakby wiemy, że to jest zasadne, że to jest dobrze, tylko że trzyma tu pracować, może ten wygląd co ten?

**Damian Kaminski** 1:06:46  
No tak, wcześniej trzeba było się przełączać.  
Jedyna sugestia jaką ja bym dał za nim cokolwiek zmienisz z kolorami to ja bym się nie sugerował, że Mateusz tak powiedział, tylko powiedziałbym, że to daj nam ten swój.  
Formularz wrzućmy go tu kolorowy, zrobić z tego screena i wrzucić to do firmy. Usuń te kolory.  
I wydaje mi się, że to wcale nie będzie czytelniejsze, że to się zleje jak to będzie sam tekst.

**Kamil Dubaniowski** 1:07:29  
No nie wiem, to nawet o tym nie myślę, żeby tak wyrażę. Myślałem, żeby na przykład kontekście tych dziedziczenia w tej korony były szare czy cokolwiek, no ale czyli te główne wyjątki tylko są w kolorze, a to co mniej istotne dziedziczone jest jest, ale dobra, no będę nad tym siedział, wewnątrz będzie mógł i ja w sumie na tym kończę listę tematów, które.

**Damian Kaminski** 1:07:41  
O k.

**Kamil Dubaniowski** 1:07:53  
Są pod moją opieką i chciałbym podjąć w najbliższym sprincie i wydaje mi się, że po ludziach teraz tak trzeba przejść i zobaczyć.

**Damian Kaminski** 1:07:53  
Dobra.  
No to mamy tak.

**Kamil Dubaniowski** 1:08:01  
To ma.

**Damian Kaminski** 1:08:02  
Adrian nie ma przypisanego tego.  
Jak tam ten sam chleb się no nie tylko.

**Kamil Dubaniowski** 1:08:07  
Numark hab.

**Janusz Bossak** 1:08:11  
Tak.

**Damian Kaminski** 1:08:14  
Komarch hap toma.

**Kamil Dubaniowski** 1:08:21  
Miałem w ogóle nie wiem o co chodzi w tym temacie, więc też wydaje mi się, że no powinien to.

**Damian Kaminski** 1:08:23  
Ja też nie wiem.

**Janusz Bossak** 1:08:24  
Ten Comarch erp to z tego co ja kojarzyłem kiedyś, bo jak raz z gościem z tego comarchu rozmawiałem, ale to już było z 2 lata temu, jak w ogóle zaczynaliśmy krzew, że oni robią swój taki i tak jak my mamy connector krzew. To oni mają swój nie.  
Yy, to są wystawione jakieś end pointy.  
Tak jak nasz connector ma wystawiony i trzeba się ich odpytać albo coś wysłać i koniec.

**Damian Kaminski** 1:08:51  
O k no to tym trzeba będzie się pochwalić tak, bo rozumiem, że tak klient się zdecydował na to dlatego, że korzysta z Comarch i wtedy ma jedno i tym narzędziom wysługuje i wysyłkę i pobieranie, natomiast przy pobieraniu przechodzi to najpierw przy zamku dita, więc Comarch pobiera, wpada do addicta, przechodzi ścieżkę, wpada do narzędzia Comarch owego, żeby zaksięgować.

**Janusz Bossak** 1:08:53  
Filozofia.  
W pierwszej kolejności chciałbym wiedzieć, jak działa ten komar hap, znaczy może nie tyle jak tylko po co on został zrobiony tak, jakie jakby mała funkcjonalności, co umożliwia i no, a druga koncepcja naszej integracji z tym, czyli jak to będzie wyglądało, jak już będziemy mieli połączone? Tak, to jest ten powiem, który mnie interesuje w tej chwili, czy my to już wiemy, żeby się znowu, że Adrian nie doktoryzował i nie robił połączenia na przykład z Nie wiem 50 punktami, które tam są.  
Jak potrzebujemy 2.

**Damian Kaminski** 1:09:44  
I tu zapomnieliśmy właśnie łukaszu, bo to temu o tym nic nie wiemy, bo Łukasz jest na urlopie. To Łukasz opiekuje naszej strony ten temat i to Łukasz musi.  
Adriano, widać no właśnie MVWP.  
I potem z tego.  
Zrobić jakieś jakieś podsumowanie?  
Opisowe tak czy przed, czy po to już, ale no po prostu tym powinien się opiekować Łukasz.  
Przynajmniej inaczej przynajmniej tak było to przypisane. Tak dlatego my trochę Adrian działa sam sobie i tylko no bo my nie mamy tej wiedzy, którą ma Łukasz, on to gdzieś tam opiekował i wycenią.

**Janusz Bossak** 1:10:30  
Trzeba poczekać do poniedziałku, żeby się dowiedzieć.

**Kamil Dubaniowski** 1:10:32  
No o k no pewno czy teraz celem byłoby przejrzenie kto co ma i czy nie ma za dużo? 2. Myślę, że to jest.  
Maks na ringu, ale Adrian mówi, że na przykład ten ksywkę to jest jakaś tam mała rzecz, więc nie wiem. Najwięcej oszacował, że zajmie ten Senat forma, bo tam jest całe video.

**Damian Kaminski** 1:10:54  
No i właśnie pytanie, czy to jest dobre, że Adrian to robi?  
Bo brakuje nam tego backendu Adrian zajmuje się tutaj frontem.  
Ee no mówiąc wprost nie mając takiego wyczucia stylu jak chłopaki od reacta tylko ja nie wiem na ile to by się dało podzielić i oni by się byli w stanie zaangażować w to, bo to jest jakiś tam znowu, a i tu jest kluczowa ważna rzecz, którą Adrian tak jakby podjął samodzielnie.  
W czym to jest pisane, bo to jest pisane w jeszcze nowszej technologii niż reaktor.

**Kamil Dubaniowski** 1:11:32  
Czy to jest coś desktopowego na madrymi pisał mój.

**Damian Kaminski** 1:11:34  
Możemy zadzwonić Adriana, no, jakieś mu i coś takiego i ja nie wiem, ja nie Jestem w stanie tego ocenić, czy to jest dobry krok, czy zły krok. Dlaczego to jest takie krok? On powiedział, że po prostu to jest uniwersalne pod kątem maca i Windowsa.  
Ee.  
No nie wiem co ty Janusz sądzisz, w zwalniamy Adriana i oto na przykład go odczytujemy.

**Janusz Bossak** 1:12:01  
Nie wiem czy go teraz niekoniecznie teraz.

**Damian Kaminski** 1:12:01  
Niekoniecznie, niekoniecznie teraz, ale pytanie, kto tą decyzję?  
W takim zakresie powinien podjąć.

**Janusz Bossak** 1:12:06  
Nie.  
Znaczy pier.  
Nie słyszę, że Adrian wziął ten mój. No to jest coś nowszego, ale.  
No.

**Damian Kaminski** 1:12:19  
Wiesz, on zrobił prototyp, który się do niczego nie nadaje, tylko do pokazania nam i powiedział, że zrobił to w tym podjął tą decyzję autorytarnie po prostu tak jak nie tylko to co co się no możemy tylko wyciągać wnioski, nie z tego snapa.

**Janusz Bossak** 1:12:30  
My tak.

**Damian Kaminski** 1:12:33  
Ee bo już czasu nie cofniemy, żeby właśnie takich tematów unikać. Natomiast no pytanie, kto tą decyzję ma podjąć to no nie wiem, to jest poza naszymi kompetencjami według mnie.

**Janusz Bossak** 1:12:44  
Zespół nie to jest to, to jest to samo co.  
Yy no.

**Damian Kaminski** 1:12:57  
Czy może inaczej? Ja nie Jestem w stanie podjąć decyzji, czy to czy coś innego, ale jak usłyszę jakieś argumenty za i przeciw, no to wtedy mogę coś.

**Janusz Bossak** 1:13:05  
Czekajcie, wypadł znaczy, że przeczytałem komunikatu od żony, tam już na lotnisku są coś tam i się wybiłem z rytmu. Chodziło mi o to repozytorium. Tak czy ten ten przykład z tym.  
Ma kokosem i z tym, że Adrian wybrał jakąś technologię, to jest dokładnie to, co przed chwilą omawialiśmy o tej architekturze. Rozwiązania dla repozytorium to jest dokładnie ten sam poziom.  
Autorytarnie tak jak mówisz Adrian, wybrał jakąś architekturę, jakiś sposób, technologie i tak dalej, bo nie było projektu.  
I było to jego tej właśnie górnej fazy.  
Że architektonicznie robimy tak, bierzemy taką technologię, taką technologię, to będzie zrobione tak i tak dlatego, że na przykład przyszłościowo chcemy zastąpić 2 apy jednym sin apm, który będzie działał ten sam znaczy ten sam kod tylko skompilowany na Windows i ten sam kod skompilowany na maka po prostu będzie to działało, ale będzie jedno źródło prawdy w jednym kodzie, a nie tak jak teraz mamy 2.

**Damian Kaminski** 1:13:48  
Mhm.

**Janusz Bossak** 1:14:17  
Ale to musi być ten poziom, tak znaczy poziom projektu, dlaczego to robimy? Jak to robimy, jaki jest cel?  
Architektura rozwiązania, technologia dobrana i dopiero dopiero w tym momencie te wszystkie endpoint ty front, trendy i tak dalej i tak dalej, bo to wynika z całej architektury projektu. W moim przekonaniu naszym wielkim problemem jest to, że my nie robimy tej warstwy.  
Albo już robimy po łebkach, słabo i właściwie przeskakujemy od pomysłu do zadań na blogu.

**Damian Kaminski** 1:14:52  
Tak, nie mamy elementu projekt analityki systemowej.

**Janusz Bossak** 1:14:58  
Tak.

**Damian Kaminski** 1:14:59  
Mamy biznesową i wykonanie.

**Janusz Bossak** 1:15:01  
Więc osoba i robimy.

**Damian Kaminski** 1:15:04  
No tak, tak tak.  
No i trzeba w to wejść i to wymaga współpracy właśnie spotkań tych zespołowych, bo my nie mamy takiej roli w sensie w jednej osobie skupionej wiedzy.  
Tylko one są rozproszone i wtedy tą właśnie rolę trzeba wykonać zespołem, czyli zderzyć to, co potrzebuje biznes i to, jaka jest propozycja wykonania i spisać w postaci projektu architektury.

**Janusz Bossak** 1:15:31  
Padnie i to naprawdę to nie jest strata czasu, bo to może się wydawać, że to takie tam administracyjne.

**Damian Kaminski** 1:15:36  
To jest unikanie błędów, a nie strata czasu to w ogóle.

**Janusz Bossak** 1:15:38  
To jest dokładnie to jest. To jest unikanie błędów, unikanie późniejszego rozczarowania, takiego wiesz odkrywania o kurde, jak to Adrian zrobiła, dlaczego on tak zrobił? A dlaczego wybrał jakieś mój a nie tamto? No sorry, no bo zabrakło tego fragmentu, nie.  
No i właśnie rozmowy o architekturze jak my to robimy i tu jest potrzebny i Piotr.  
Na pewno jako architekt i frontend owiec.  
Jakiś jeden czy drugi?  
Ktoś kto dba?  
O taką długoterminową spójność tego wszystkiego co my robimy, a nie, że my sobie sami na głowę bierzemy 5 technologii i ten zrobił w korze. Pamiętam to, bo rozwiązanie kolorowe jak robił rap.  
Teraz Center jest też Napisany w w doktor.  
Teraz ten tu robi jakiś mój wiesz, ja nie wiem.

**Damian Kaminski** 1:16:38  
Potem nie ma komu tego zaopiekować, dokładnie.

**Janusz Bossak** 1:16:41  
Tak no niech ktoś dba o tą architekturę, no.  
A nie że sobie sami na głowę bierzemy kłopoty na przyszłość wytwarzamy, nie.  
To naprawdę musi być ten architekt Piotr nie bez powodu się nazywa architektem gumowym. No to właśnie o to chodzi o ten poziom tak trzymania również tej technologii.  
W ryzach tak.

**Damian Kaminski** 1:17:06  
W ryzach te.

**Janusz Bossak** 1:17:10  
No także musimy tym na ten poziom wejść. To przykład repozytorium, zróbmy to dobrze, tam po prostu po bożemu.

**Kamil Dubaniowski** 1:17:17  
Skoro ten Adrian twierdzi, że to jest najwięcej roboty, no nie wiem czy to jest czas się cofać teraz do poziomu projektu może lepszy niż ze tak to to wróćmy do tematu. Ustalmy z Piotrem, czy to Akceptuję?

**Damian Kaminski** 1:17:24  
Ale co jest najwięcej to.

**Kamil Dubaniowski** 1:17:32  
Wtedy zaczniemy w ogóle to robić?

**Janusz Bossak** 1:17:35  
On zrobił, można powiedzieć dla mnie to, co jest zrobione przez Adriana to jest proof of Concept, że daje się.  
Na maku podpisywać.

**Damian Kaminski** 1:17:44  
Tak.

**Janusz Bossak** 1:17:44  
I teraz i teraz trzeba zrobić projekt i aplikację, która będzie to robić. Na razie to były go.  
Mniej bardziej.

**Damian Kaminski** 1:17:53  
Projekt wizualny już nawet jest, tylko zostaje wybrać właśnie ten aspekt zrobić analizę systemową, czyli czym to robimy?

**Janusz Bossak** 1:18:00  
Według mnie warto się cofnąć o ten jeden krok i zrobić to dobrze.

**Kamil Dubaniowski** 1:18:05  
To od tego zacznijmy.

**Damian Kaminski** 1:18:05  
Dobra, to idźmy dalej. Najwyżej na koniec spotkania może jedno takie może do prosimy tutaj 3 osoby, czyli nie wiem. Piotr Adriana i jeszcze kogoś od reacta, bo ja pytam, a czemu nie reaktor? Bo to nie jest ten reaktor aplikacyjny, tylko to jest jakiś reaktor inny.  
Ale nie Jestem w stanie powtórzyć on coś tam dodał do reaktor.  
Jakieś jakieś jedno słówko i no i on stwierdził, że to wtedy nie reaktor.

**Janusz Bossak** 1:18:34  
No bo bo my też według mnie nie używamy tego reaktora, którego powinniśmy tam native czy coś on się nazywa.

**Damian Kaminski** 1:18:42  
No.  
No właśnie o coś takiego tak tak tak, tak, tak.

**Janusz Bossak** 1:18:45  
Bo jest no reaktor aktowi nie, nie do końca równy to tak samo jak te dotnet kolory właśnie dotnet framework. Pan 4 8 to jest to są ten sam poziom różnicy, nie.  
Są takie właśnie wersje, reakcja jak ten REACT native, które się charakteryzują tym, że możesz z niego wyprodukować na przykład aplikację mobilną.  
A z tego reaktora, którego my używamy, nie.

**Damian Kaminski** 1:19:12  
Mhm.

**Janusz Bossak** 1:19:14  
Tylko mówię no.  
To są decyzje architektoniczne, ja bym chciał, nie chciałbym ja ich podejmować, bo nie znam konsekwencji, znaczy ja ja mogę podjąć decyzję, jak mi ktoś powie, jeżeli weźmiemy to to wtedy, to to to to jeżeli weźmiemy to to wtedy, to, to, to i tamto, nie, to będzie nas kosztowało tyle to tyle to będziemy robić 2 miesiące, a ta technologią 6 miesięcy decyzje.

**Damian Kaminski** 1:19:23  
No właśnie.  
Będzie taki tak.  
Dobra i według mnie, zróbmy może na koniec spotkania oddzwonimy i to ustalmy na na tym przykładzie.  
Dobra, według mnie ania jest niedoszacowana, to znaczy tutaj ogólnie można przyjąć, że ania będzie dalej pracować nad raportami i błędami, ale można też co innego nad czymś innym się zastanowić, może na razie kontynuujmy kto jest kompletny?

**Kamil Dubaniowski** 1:20:05  
Filip moim zdaniem zamknięty temat.  
Nie.

**Damian Kaminski** 1:20:11  
Marek też.

**Kamil Dubaniowski** 1:20:13  
Nie wiem, jeżeli będziecie go tam angażować w ten projekt.

**Damian Kaminski** 1:20:18  
Aha czekaj, bo nie, no ale pozorem no.  
Niekoniecznie, dużo w sensie tam już może inaczej.  
Pod kątem okapu już niedużo pod kątem potem połączenia tego, no to niekoniecznie ten sprint, bo teraz będziemy pracować nad projektem, więc no nie dużo.

**Kamil Dubaniowski** 1:20:37  
O k.  
No dobrze, no wydaje mi się, że te 2 tematy są.

**Damian Kaminski** 1:20:45  
Dobra nas pomijam.  
Marek.

**Kamil Dubaniowski** 1:20:51  
Też Jestem Ryszard, pewien, że jest to prawdą, to zamknięty temat.  
Mateusz chyba też patrząc na to, że nie będzie dobra. Moja tata spięcie z krótszym.

**Damian Kaminski** 1:20:58  
Znaczy według mnie za dużo, według mnie za dużo.

**Kamil Dubaniowski** 1:21:02  
Czy no ma komunikator? Taka projekt to jest projekt, tak jak powiedziałeś, to będą jakieś spotkania.

**Damian Kaminski** 1:21:08  
O k. Tutaj jest ten kaz u Piotra znowu trzeba spojrzeć na jego tablicę, bo.  
O kurde ktoś znowu coś?  
Adrian.  
Parent.

**Kamil Dubaniowski** 1:21:50  
Od piksel z Parlamentem.  
W tym czasie michałowi przypomni, czy to blokował, jak się da.

**Damian Kaminski** 1:22:19  
Super.  
Piotr.  
Nie wiem, powiem wam czy to trzyma. Wydaje mi się, że to mu ułożyłam.  
Jakby znowu to się jakoś rozwaliło tak jak chciało ta kolejność.

**Kamil Dubaniowski** 1:22:40  
Ale to jest czterdziesty trzeci. To o tym mówisz.  
Czy na przykład?

**Damian Kaminski** 1:22:43  
No tak aktualny według mnie jak z nim się gdzieś tam spotkaliśmy, to czy ja z nim się spotkałem i tłumaczyłem, to układałem to tak, żeby na Górze właśnie były już te to, które były don.

**Kamil Dubaniowski** 1:22:44  
K.

**Damian Kaminski** 1:22:54  
I wydaje mi się, że one gdzieś.  
Dobra in progress, dodanie możliwości działania modlić w środowisku z kilkoma nie zaufanymi dobra, to on to już robi, więc pewnie to zaraz skończy, chociaż nie wiadomo.  
A nie skończy to jest duże wyzwanie. Tu mamy potwierdzone, że to jest tylko ad, bo to już mi się udało potwierdzić.  
Zrobimy tak.

**Kamil Dubaniowski** 1:23:29  
Widzę, że w końcu nam zaczął wykrywać spadać przyrastać na team sprint.

**Damian Kaminski** 1:23:34  
No to jakiś sukces pierwszy jest tych naszych zmian.  
Dobra kredytu to jest ten s.

**Janusz Bossak** 1:23:39  
Bardzo proszę.

**Damian Kaminski** 1:23:56  
Dobra.

**Kamil Dubaniowski** 1:23:57  
Według statystyki zrobiliśmy 28% sprintu.

**Damian Kaminski** 1:24:01  
Ale wiesz, bo tam dużo chyba jest na testach, więc to nie ma co jeszcze tutaj.

**Kamil Dubaniowski** 1:24:03  
Tak.

**Damian Kaminski** 1:24:06  
No ale tak pierwszy raz chyba jest tak, że niebieski spada.

**Kamil Dubaniowski** 1:24:13  
No ale to jest kwestia tego, że ja się.  
Trening work nie było uzupełniane na Zero i to jest kwestia, że ten wykres mieliśmy cały czas w miejscu, bo mieliśmy effort 8 jakby mining 8, no więc on uznawał, że nic nie zrobiliśmy.

**Damian Kaminski** 1:24:28  
Mhm, a tu.

**Kamil Dubaniowski** 1:24:29  
Nawet jak było dam.

**Janusz Bossak** 1:24:30  
Zobacz jest na count nawet i też spada. Nie czyli liczba spraw już jest no bardzo dobrze, no wreszcie.

**Damian Kaminski** 1:24:36  
Nie no zaczyna to w końcu wyglądać nie.

**Janusz Bossak** 1:24:39  
Wreszcie będziemy.

**Damian Kaminski** 1:24:44  
No wiecie, 40% w jeszcze przed zakończeniem sprintu to.

**Kamil Dubaniowski** 1:24:44  
No i tak nie jest idealnie.

**Damian Kaminski** 1:24:49  
To jest dobry.  
Porównaniu do ostatnich to dobry wynik, ale jak spojrzymy też na to, to tutaj zobaczcie, tak nie było.

**Janusz Bossak** 1:24:54  
Jeszcze jak?

**Damian Kaminski** 1:24:59  
To też jest pewnie związane z przenoszeniem, ale sprint do tyłu. My nie mieliśmy 95%, a tu naprawdę to dobrze wygląda, bo wiadomo, że jeszcze to musi przejść testy. To, co dzisiaj powiedziała Basia, to, że wrzucicie to nie znaczy, że przetestujecie, że przetestujemy, ale to jest o k według mnie, że mamy taką inną wersję.  
Ale to, że z poprzedniego sprintu mamy 95 skończonych, to według mnie.  
Dobry prognostyk.  
No ale dobra, to będziemy jeszcze się nad tym.  
Zastanawiać, dobra, wrócę do tego.  
Nie to było to.  
Dobra a CS przypisałem.  
Tu jeste mating.  
To jest jakaś pierdoła, a nie to jeszcze co innego.  
Jarosław.  
To jest jakiś bank po prostu przet.  
Położenie spraw.

**Kamil Dubaniowski** 1:26:05  
To jest też.

**Damian Kaminski** 1:26:05  
To jest backen to KA, no to git, to Piotra tablica jest w zasadzie ma 2 zadania kluczowe, reszta to jest jakieś tam.  
No 2 zadania, tak.

**Kamil Dubaniowski** 1:26:16  
Myślę, że realnie Piotr.

**Damian Kaminski** 1:26:18  
No to myślę, że bardzo realnym myślę, że coś jeszcze dorzuci, ale no zawsze będzie miał jakieś tam bagi hotfix psy czy wyniki właśnie potrzeb backendowych, więc dobra to zostawmy to.

**Janusz Bossak** 1:26:31  
No tam jest liczone ten architektura pozyton podium to jest na Piotra powinno być.

**Damian Kaminski** 1:26:36  
Jest projekt repozytorium plików tak, w sensie tutaj jest wpisem.

**Janusz Bossak** 1:26:40  
Tak, tak, tak.

**Damian Kaminski** 1:26:41  
Tak.  
Żeby właśnie miał na to przestrzeń, musimy.  
No musimy go właśnie.  
Nauczyć angażowania w projektowanie, a nie tylko to, że on ma to w głowie, bo to wszyscy wiemy.  
Myśli to po prostu przekazywać, poświęcać na to czas.

**Janusz Bossak** 1:26:58  
Bo jak będziemy jak będziemy dokładnie jak będziemy od początku dobrze projektować, to na końcu to co teraz robi, czyli poprawki różnego rodzaju będzie miał tego mniej, bo będzie wszystko dobrze zaprojektowane tak jak powinno być.

**Damian Kaminski** 1:27:12  
No tak, za jednym zamachem zrobimy to tak jak trzeba nie no koniec końców to będzie mniej pracy, jeśli byśmy subowali poświęcony czas na dane zagadnienie.

**Janusz Bossak** 1:27:21  
Dokładnie.  
Podstawowa zasada tworzenia oprogramowania im wcześniej.  
Robisz różne rzeczy, czyli na przykład naprawiasz błędy, poprawiasz koncepcję, tym jest mniejszy koszt, bo jak koncepcję sobie poprawiasz na etapie koncepcji?  
No to koszt jest niewielki, pan godzina 2 straty czy coś takiego? Ale jak już według tej koncepcji zrobisz coś, no to już masz stratę ogromne, bo ktoś na przykład 2 tygodnie czy 3 tygodnie coś robił, a potem mówimy nie to w sumie do bani, trzeba inaczej tych robi.

**Damian Kaminski** 1:27:44  
No tak.  
No tak plus testerzy Jeszcze raz wszystko, bo to mogło mieć wpływ, więc no to bardzo dobra Przemek, edytor formularza poprawa ju x to jest nie nie szacowane. Tak, w sensie to będzie wynikać z tego, ile jest zadań i fora i no to jest raczej bardzo drobny temat.

**Kamil Dubaniowski** 1:28:06  
Będzie sporo temat.  
Za tę.  
Mały temat, ale no zobaczymy no sprytnie jest długi 8 dni.

**Damian Kaminski** 1:28:21  
Dobra, czy kogoś tu nie mamy, to znaczy tak, według mnie z tego w ogóle Łukasza nie masz rację z tego to jest niewiadomą. To to ty, Kamil, ewentualnie wiesz co, co byś tu już widział i ile z tego wyprodukujemy, więc według mnie Przemek potencjalnie ma przestrzeń. Ania według mnie ma przestrzeń i Łukasz w ogóle nie jest.

**Kamil Dubaniowski** 1:28:24  
Łukasz nie jest.  
Czy przemka można zaangażować na pewno do projektu tego, mimo tego, że będzie robił to Adrian do maka?

**Damian Kaminski** 1:28:48  
Tak tak, to uważam, że można.

**Kamil Dubaniowski** 1:28:50  
Jako konsultacje na pewno tak tam Piotr powinien się pojawić, ale ja myślę, że powinniśmy teraz skupić się, że Łukasz nie jest opakowany i zamknąć to spotkanie i nie wiem zrobić chwilę przerwy i do designu zastanowić się, jakie chcemy robić spotkanie indywidualne właśnie w jakiejś tematach, czyli makro jest moim zdaniem wymaga takiego spotkania.  
Ale to już indywidualnie bym rozwijał, żeby dobrać składy pod to.

**Damian Kaminski** 1:29:11  
O k.  
No dobra, no to pytanie, co z Łukaszem?

**Kamil Dubaniowski** 1:29:16  
No rozmawia, co tam trzeba zrobić?

**Damian Kaminski** 1:29:20  
Już już otwieram.

**Janusz Bossak** 1:29:23  
A on nie jest na tym komar head.

**Kamil Dubaniowski** 1:29:26  
Nie zostało Adriana, tak.

**Damian Kaminski** 1:29:26  
No to znaczy, no zastanawiamy się nad tym, ale na razie nie.

**Kamil Dubaniowski** 1:29:31  
Bo jeśli to dotyczy kse fu.

**Janusz Bossak** 1:29:31  
A też tematów, ilość tematów, które dzisiaj.  
Adrian.  
Polegających na jakichś poprawkach, by nadawcy tego typu rzeczy to niech to przejmie może Łukasz, tak on się tym nadawcą tam zajmuje.

**Damian Kaminski** 1:29:41  
Tak.

**Kamil Dubaniowski** 1:29:48  
Polecony chyba był temat.

**Janusz Bossak** 1:29:49  
Ale polecony to są doręczenia, no.

**Kamil Dubaniowski** 1:29:51  
Tak, no ale to też niedobrze. Adreno bardzo dużo u siebie takich tematów dzieje z jedną osobą.

**Janusz Bossak** 1:29:57  
Ktoś musi się zająć tymi jeden cieniami się nauczyć też po prostu no nie ma bata, nie nie może być tak, że Adrian tylko jedyny, który wie jak to działa.

**Damian Kaminski** 1:30:06  
Znaczy, słuchajcie kom to może inaczej? Comarch hap jest nowym tematem, Adrian go gdzieś tam rozkminił, ale jeszcze raczej chyba na poziomie koncepcyjnym czy bardzo wstępnym we wdrożeniu. Według mnie możemy spojrzeć w sumie.  
Bo ja z nim rozmawiałem 2 dni temu i według mnie on powiedział dobra w tym komach hubie to on na razie planuje, a nie jeszcze robi, ale już więc on to co zaplanował, może przekazać łukaszowi i według mnie.

**Kamil Dubaniowski** 1:30:29  
Tak tak, zgadza się. No tak było.

**Janusz Bossak** 1:30:30  
Słuchajcie, brak jest znowu.

**Damian Kaminski** 1:30:37  
To jest dedykowany do synchronizacji indesign on nic tu jeszcze nie zrobił, on dopiero.  
Projektuje no i coś tu opisał.  
Może w całości powinien to jest 18000, licząc po 2. To jest 9 dniówek, z czego pewnie nie tu były jakieś testy. No to może właśnie powinien to przejąć 13, czyli ze 3 dni.

**Janusz Bossak** 1:31:00  
A możemy się cofnąć o ten jeden krok wyżej?  
Architektonicznych projektowy.

**Damian Kaminski** 1:31:05  
No.  
Czyli dobra tu mamy mamy tylko tutaj punktem wyjścia są wymagania do wyceny do zlecenia o k. Coś tu jest to o to ci chodzi? Tak, żebyśmy dowiedzieli się, co jest potrzebą biznesową.

**Kamil Dubaniowski** 1:31:08  
No tak to miał do tej pory Łukasz.

**Janusz Bossak** 1:31:10  
Pod.  
I żeby był opis projektu?  
Po co to robimy, dla którego klienta?

**Damian Kaminski** 1:31:23  
O to jest najlepsze, po prostu te linkowania to nie tu z Mateuszem trzeba pogadać, to mnie tak irytują. Tu jest wymagania, tu są, a tu wchodzę, wymagania tu są 20 glinkowa nie wiadomo gdzie są właściwe informacje.  
Naprawdę?

**Janusz Bossak** 1:31:40  
Przez cały.  
Ten problem, o którym mówimy spisywania wymagań gdzieś trzymania ich, ciągle jest ten sam.

**Damian Kaminski** 1:31:51  
Już wiemy skąd wynika Comarch erp.

**Kamil Dubaniowski** 1:31:55  
Ja tam za 2 minuty na toalete, chyba, że robimy jakąś przerwę taką dla wszystkich.

**Janusz Bossak** 1:32:00  
Dobra, zróbmy przerwę. Ja też noszę już.

**Damian Kaminski** 1:32:02  
Będzie to poczekajcie, jak zrobimy przerwę to teraz tak.  
Tutaj to już mam zaplanowane. Ja mam czas do dwunastej.  
Potem mam pół godziny wrzucony spotkanie i potem od dwunastej mamy design.

**Kamil Dubaniowski** 1:32:17  
No to ja myślę, że wrócimy tylko na temat, żeby Łukasza zaopiekować, żeby każdy miał Plan i wtedy robimy, bo już taką długą przerwę teraz bym potrzebował 5 minut dosłownie tak 20 minut. Myślę, że nam starszy nauka.

**Damian Kaminski** 1:32:27  
No to łapiemy się 40 po i mamy jeszcze 20 minut, dobra?

**Kamil Dubaniowski** 1:32:30  
Dobra.

**Janusz Bossak** 1:38:28  
No Jestem.

**Kamil Dubaniowski** 1:38:32  
Jestem, Jestem też.

**Janusz Bossak** 1:38:39  
Ale muszę powiedzieć, że te nasze spotkania to dzisiejsze jest naprawdę konstruktywne.

**Kamil Dubaniowski** 1:38:45  
Stwierdzam się tak jakby nie, nie może, nie, nie, nie jest jakieś rewolucyjne i tak bym pewnie planował to co mniej więcej, ale przynajmniej wiem, że.

**Janusz Bossak** 1:38:45  
Jest.

**Kamil Dubaniowski** 1:38:54  
Nikt mi nie powie, że tego nie mieliśmy robić w ten sprint.

**Janusz Bossak** 1:38:59  
Dobrze, dobrze jest, dobrze jest coraz lepiej. No właśnie o to chodzi, żeby się wiesz tak krok po kroku doskonalić nie nie tam jakąś rewolucję.  
Super pomysły tylko.  
Tak mi się wydaje, to brakuje mi jednej rzeczy, znaczy mówię o tym projektowaniu, to tych dokumentach i szukamy ciągle.  
Yy, jakby miejsca ich przechowywania, sposobu ich edytowania, żebyśmy wszyscy mieli do tego dostęp.  
I to jest ciągle dla mnie jeszcze taka właśnie rozwiązana sprawa, nie.  
Nie wiem właśnie gdzie to trzymać, jak to trzymać, jak to sprawnie uzupełniać.  
Rzecz, którą byśmy musieli jeszcze.  
Przepracować i.  
Wymyślać.

**Kamil Dubaniowski** 1:39:52  
Ratusz, myślę, że poniedziałek w sumie to my powinniśmy już sobie zrobić kolejne spotkanie i to, co robimy teraz.  
Zrobić.  
Perspektywie no kolejnego sprintu dla nas.  
Żeby właśnie było tak, że już mamy gotowe projekty, bo teraz cały sprint my powinniśmy nad nimi pracować.  
Tylko musimy też ustalić, co jakie tematy podejmujemy w kolejnym sparingu już.

**Janusz Bossak** 1:40:14  
No tak.  
Tak, ale właśnie no mi brakuje takiego, wiecie fizycznego miejsca, gdzie my to trzymamy.  
Projekty.

**Damian Kaminski** 1:40:23  
O czym teraz? Aha.

**Janusz Bossak** 1:40:26  
No to właśnie.

**Damian Kaminski** 1:40:26  
Znaczy, no już zaproponowaliśmy to rozwiązanie tak na kanałach to.

**Janusz Bossak** 1:40:32  
No dobrze, no trzeba.

**Damian Kaminski** 1:40:32  
Podejmujecie, czy to jest zasadne? Tak.

**Janusz Bossak** 1:40:35  
Przy przedyskutować to jest no nie wiem, no jest na razie tu dobra, ja się do tego na razie jest tam jeden projekt wim repozytorium plików.  
Są materiały źródłowe i repozytorium plików, opisem bp jeden.  
Dobrze no i.  
Tu powinno teraz powstać to, co mówiliśmy przed chwilą poprzednim spotkaniu, czyli rozmowa z Piotrem z pisanie tej architektury.  
Spisanie projektu, potem deweloperskiego technicznego.  
Dodanie tych założeń do projektu front endowego, żebyśmy to mieli wiecie jako.  
Opisy projektowe, no ale dobra.

**Damian Kaminski** 1:41:21  
Znaczy nie mamy.  
Musimy to podzielić, bo tak mamy teraz, powiedzmy 3 potencjalne przestrzeni mamy teams trwa.  
Mamy stricte backlog i mamy wiki ażurowe.  
I teraz trzeba się zastanowić, czy te 3 kanały są zasadne, to znaczy bez backlogu w ogóle sobie nie poradzimy, więc pozostają te 2 pozostałe natomiast.  
One też się może uzupełniają, a niekoniecznie wykluczają, bo na team się, bo bo tak no a zuzia nie ma wygody, osadzania, powiedzmy plików filmów i tak dalej. Nie wiem, w ogóle się taka możliwość jest.  
Mm z kolei.  
Jeśli będziemy mieli projektowe te opisy, tak jak tutaj Janusz, chcę docelowo, z czego wynika dopiero, bo jak to znaczy, według mnie te 3 elementy się uzupełniają. Ma to sens, niekoniecznie zawsze będzie występować element.  
Im sowy.  
Bo on może być pominięty, tak?  
Czyli nie będzie plików takich postaci? Nie wiem nagrań czy dostarczenia czegoś od klienta, bo to jest nasza wewnętrzna potrzeba i mamy tylko element.  
Wiki ażurowego, czyli ogólnej dokumentacji przedprojektowej i backlog w postaci już powiązań z tą dokumentacją.

**Janusz Bossak** 1:42:50  
Czy?  
Znaczy mówię.  
Uporządkować jakby.  
Parę rzeczy.  
To co wydaje mi się?  
Minimalnie potrzebne.  
W dokumentacji projektu.  
Pomijam źródłowe elementy tak, bo źródłowe to są, wrzucamy i mamy, czyli właśnie jakieś nagrania jakieś tam rzeczy tak dalej natomiast.  
Projekt minimalnie składa się z 3 plików.  
Pierwszy plik.  
Uzasadnienie biznesowe.  
I powiedzmy w tym uzasadnieniu biznesowym, żeby już nie robi.  
Wbijać się na drobne, tam też metryczka pliku tak, czyli kto się od nas opiekuje.  
Tak jakieś takie podstawowe tam kilka informacji nie, ale bynajmniej ta te uzasadnienie biznesowe według mnie jest bardzo kluczowe. Czyli po co? Dlaczego dla kogo, w jakim terminie?  
Tak to robimy. Czy to wynika właśnie zamówienia z czegoś tam tutaj dalej?  
Drugi plik.  
Który według mnie jest masyw to jest takie.  
Już rozbicie na te mbp.  
Czyli jak my sobie wyobrażamy dostarczenie tego w czasie jeszcze może nie w czasie w rozumianym konkretnych dat był to kwartał tak i taki tylko, że sekwencji tak, że najpierw będzie to MP, jak to skończymy, to będzie tamto, jak tamto skończymy to będzie jeszcze następny, albo jakieś następne, nie.  
Yy i ono powinno być ten plik tak skonstruowany, że to mbp, nad którym pracujemy, powinno być najbardziej szczegółowe.  
Tam już powinny być wszystkie przypadki użycia rozpisane.  
No zabierający dużo w sumie tekstu tak no bo to jednak już powinno być wiadomo co my chcemy zrobić, tak.  
No i tu ewentualnie.  
Generalnie jeżeli to miało być by być jakoś szczególnie długi, ten plik, to może może lepiej mieć takie pod pliki do tego.  
Które opisują szczegółowo dany mbp tak, czyli znowuż cel tego mbp, co my chcemy tutaj dowieść.  
Takie tam przypadki użycia będą obsłużone.  
I tego typu rzeczy i trzeci plik.  
To powinnam być ten właśnie ten architektoniczno techniczny.  
Tam w tym pliku architektoniczną technicznym.  
Ma być opisane wszystko to jak.  
Z punktu widzenia technologii chcemy to zrobić właśnie te mój, miłuj czy REACT taki czy inny, czy jako osobna aplikacja czy współdzielona. Czy wam modlicie, czy obok micro serwisy, komunikacja wszystko techniczne.  
Co będzie?  
Miało wpływ na projekt i tam powinny być.  
Aktualne ustalenia.  
Nie historyczne, że pan miesiące temu mieliśmy taki pomysł.  
Nie, jeżeli jest jakaś rada deweloperów.  
I ustalamy, że jednak podchodzimy do tego w ten sposób. To powinno być tam napisane.  
W trybie teraźniejszym robimy to tak.  
I ważne, żeby było kiedyś to to będzie w materiałach źródłowych tam może być.  
Odnośnie Odnośnik można gdzieś tam sobie na końcu mieć tabelkę, bo na początku, że w dniu trzydziestego pierwszego października nastąpiła zmiana podejścia na takie, ale tekst.  
Ma być wyrażony w czasie teraźniejszym. Robimy to tak.  
Jerzy tam rozważaliśmy i chyba będziemy robić. Nie robimy to tak, to jest stan na dzień i tyle tak 3 pliki.  
Uzasadnienie biznesowe z krótką m.  
Pi czyli nasz nasza root mapa tego produktu tego projektu.  
I ten t.  
No perspektywa techniczna, architektoniczną, techniczna i tyle to są 3 kluczowe pliki, które do których ja bym chciał zaglądać i które powinny być z każdą radą, z każdą dyskusją z każdym odbiorem.  
Yy na przykład przez przy sprint Review analizowane uzupełniane.

**Damian Kaminski** 1:47:34  
Ale to poczekaj, czyli chcesz mieć taki stan obecny tego projektu?  
A historyczne jak po prostu ten stan obecny zapisujemy jako stan na dzień taki i taki aktualizujemy nowy stan, tak.  
Dobrze to rozumiem.

**Janusz Bossak** 1:47:53  
Czy ale co się będzie zmieniać?  
No nie rozumiem pytania teraz.

**Damian Kaminski** 1:48:01  
No bo ten stan.

**Janusz Bossak** 1:48:02  
Nie no i.  
No.

**Damian Kaminski** 1:48:04  
To jest jakiś opis mvp dzisiejszego tak to znaczy, no ustalamy, że tak jest zakres projektu, po czym rozwijamy go dalej za jakiś czas.

**Janusz Bossak** 1:48:14  
Wpisujemy tam.  
No bo jakby w stanie zerowym.  
Ja tak rozumiem, no mamy pomysł na MWP, czyli co dostarczymy w wersji pierwszej?  
I ten pomysł musimy skonkretyzować, że w wersji pierwszej będzie to to i to, ale nie będzie tego i tego, i tego to wpisujemy sobie w md p 2, bo na tym etapie tak nam się wydaje, tak.  
I przychodzi moment i to i teraz to miałem bp planujemy dobra to np. Jeden zrobimy wku, jeden 2026.  
No i robimy, przychodzi pierwszy kwartał, robimy tą mbp tego projektu wku jeden 2026 rozpisujemy wtedy na.  
Blog na ficzery no pb a je do tam jeszcze szczegółach mamy jakieś rzeczy i tak dalej nie, ale wiemy jaki jest zakres, że chcemy dostarczyć funkcjonalność, która będzie obejmowała takie rzeczy, takie tej przypadki użycia, czy na przykład będzie można.  
Dodawać coś tam będzie można robić, coś tam będzie można tam usuwać.  
Ale na przykład w TVP 2 jest napisane, że będzie dodana. Nie wiem możliwość przeglądu historii zmian tam czegoś.  
I kosztowne będzie czytał, mówię, aha no dobra, czyli vip tej historii nie ma. Ona będzie mvp 2, czyli robimy to, co jest w mbp jeden i wiemy świadomie, że nie będzie nam na przykład historii zmian.  
No i o k.  
I dowozimy i teraz zbliża się to mbp 2. W międzyczasie możemy nabyć jakąś nową wiedzę, coś do szczegółowi i tak dalej i wtedy modyfikujemy zapisy w tym mbp 2 zanim zaczniemy ten projekt mbp 2 realizować może coś z tego mp 2 przejdzie na MP 3, bo się okaże, że są inne ważniejsze rzeczy, które trzeba zrobić.  
Ale ten plik w każdej chwili w każdym tygodniu w każdym sprincie powinien pokazywać stan.  
Stan na dzisiaj wiedzy o tym projekcie, co zamierzamy w nim robić, co robimy, w którym miejscu jesteśmy może być napisane, mtvp skończone w dniu trzydziestego pierwszego października 2025. Nie koniec, czyli wiadomo, że to.  
Tam jest zostało zrobione.

**Damian Kaminski** 1:50:36  
Mhm.

**Janusz Bossak** 1:50:39  
Tak znaczy, wiecie, no nie prowadzimy tego jeszcze w ten sposób. Ja tam kilka.

**Damian Kaminski** 1:50:43  
Nie no k bo bo teraz jeszcze zdążę to z tym, że dzisiaj mamy też jak piszemy sobie jakąś tam starą funkcjonalność to mamy 2, projektowa i powykonawcza.  
Ee.  
I to też nie zawsze jest czytelne.  
A tutaj byśmy to uprościli, w sensie byłoby to w jednym miejscu tak mamy spisane w zasadzie powykonawczą plus ewentualne jakieś refleksje po tym wykonaniu, co można.  
Rozwijać, ale bardziej w kontekście takim.  
Z grubsza tak, 2 3 punkty, 5 punktów i.  
Może w przyszłości tak.

**Janusz Bossak** 1:51:19  
Dokładnie.  
Szukam tutaj, bo chciałem podkręcać jedną rzecz.

**Damian Kaminski** 1:51:26  
Dobra, bo mamy jeszcze przynajmniej ja mam 7 minut.  
No chyba czy my wróciliśmy do.

**Kamil Dubaniowski** 1:51:32  
Bo o tym napomnienie 2 tematy, Łukasz, moim zdaniem do zaopiekowania, bo na razie to co decyzja, że przypinamy mu tego, co marhaba robimy spotkanie i nagranie przekazuje dobra, no to tak jak możesz w tych zadaniach to przerzuć.

**Damian Kaminski** 1:51:34  
No właśnie.  
Ja bym był chyba za tym.  
Już.

**Kamil Dubaniowski** 1:51:46  
Yy i moim zdaniem to i tak nie jest chyba cały sparing dla Łukasza. Nie wiem czy.

**Damian Kaminski** 1:51:53  
No tak, ale są wiesz jeszcze błędy nie więc.

**Kamil Dubaniowski** 1:51:54  
Też tak często.  
No ważne, że ma chociaż jeden tak, żebyśmy mogli to później sobie uznać, że zrealizował czy nie.

**Damian Kaminski** 1:52:03  
Dobra, to ja na razie może tu wpiszę, że to są czy już to zdjąć za Adriana po prostu.

**Kamil Dubaniowski** 1:52:08  
Czy będzie zaangażowany od tyle, żeby przekazać wiedzę, uczestniczyć w aktualnie w projektowaniu? Nie wiem, czy to Łukasz ma opiekować nadal.

**Damian Kaminski** 1:52:17  
No to właśnie może niech tak będzie tak jak tutaj Piotr jest archi.  
Tekstem dla repozytorium to tak samo Adrian Adrian, tu jest powiedzmy architektem, niech ma doświadczenia. W sumie mamy też tą komunikację z.  
Naszym.  
Ee tym torem, teraz go też rozwijamy i w sumie to może być w jakiś sposób spójne, że Adrian na to spojrzy i powie, no tu zaprojektowaliśmy to to i to, ale może nawet w ramach tego zlecenia pod klienta powiedzieliśmy, słuchajcie, no to jest minimum, a my mamy analogiczne rozwiązanie. Możemy wam jeszcze to rozszerzyć odpłatnie o takiej takie elementy, po to, żeby to było.  
Bardziej rozliczalny i tak dalej transakcyjne, bo to teraz robimy w kontekście tej integracji naszej wewnętrznej, a tu mogły być pisane tylko właśnie takie podstawowe wymagania, więc no dobrze było może, żeby właśnie Adrian już to gdzieś nadzorował, ale nie nie wykonywał.

**Kamil Dubaniowski** 1:53:18  
O k dobra, no i teraz tak, żeby to było świadome, nie podejmujemy w tym sprincie tematów z diagramu z listy reguł.  
I raportów systemowych.

**Damian Kaminski** 1:53:35  
Tak tylko to musi właśnie wybrzmieć też nie.  
To w poniedziałek trzeba powiedzieć żeby.  
Czeka Jeszcze raz raporty systemowe. To znaczy inaczej raporty systemowe, bo tu Janusz zaczął, ale nie wiem, czy w ogóle to kontynuujesz to według mnie jest zadanie Łukasza.

**Janusz Bossak** 1:53:51  
Tego.

**Kamil Dubaniowski** 1:53:53  
Czy właśnie nie to powinno być wspólne zadanie, żebyśmy za projekt?  
I co my chcemy, co nam już potrzebni, bo jak widzieliście s ql to później może pisać na maj.

**Damian Kaminski** 1:53:59  
O k no dobra, to niech Łukasz po prostu tu.

**Kamil Dubaniowski** 1:54:07  
Nie mówię, że tak złożony tematy, no ale to co ja chcę podkreślić to co Janusz, to znaczy także sql, to powinien być ostatni etap, a nie pierwszy etap.

**Damian Kaminski** 1:54:16  
Dobra, to przypisuje tu po prostu nasz zespół.

**Kamil Dubaniowski** 1:54:21  
Tak i w tym zakresie, zanim trzeba wszystko odpiąć, co jest potencjalnie przeszło, bo chyba też przekonaliśmy. Jesteś na przyszły sprint z tych tematów. Moim zdaniem to jest za dalekie.

**Damian Kaminski** 1:54:32  
Mhm.

**Kamil Dubaniowski** 1:54:34  
Realizacja.

**Damian Kaminski** 1:54:35  
Dobra i jeszcze coś.

**Kamil Dubaniowski** 1:54:37  
Diagram i lista reguł.

**Damian Kaminski** 1:54:42  
Jak dla mnie starego no.  
Pytanie czy ja mam to zapisać, żeby to było jawne, że tego nie robimy tutaj na przykład czy?  
Jak to?

**Kamil Dubaniowski** 1:54:53  
Znaczy nie, no to jakby dla mnie wystarczy nasza wewnętrzna informacja, także świadomie nic nie robimy w tych tematach, mimo tego, że.

**Damian Kaminski** 1:54:56  
Ustalenie.

**Kamil Dubaniowski** 1:55:01  
Ee za ten sprint jakby celem jest zamknięcie paczki grudniowej, czyli jakby to jest o tyle świadoma decyzja, że w wersji grudniowej nie będzie w ogóle listy reguł nowej.  
I nie będzie nic w diagramie nowego, poza tym, że jest po prostu nowa wizualizacja, czyli diagram nie ma prawego panelu, nie podejmujemy tego tematu.

**Damian Kaminski** 1:55:22  
No dobra, tylko to oznacza. To ma konsekwencje, tu nie.  
Czyli my musimy.  
To stąd wywalić.  
To stąd wywalić tak czy no jakiś, ale może inaczej diagram.

**Kamil Dubaniowski** 1:55:38  
Kwartału, więc pracować możemy tylko to jest o tyle świadoma decyzja, że ten sprint zamyka nam wersję grudniową beta, którą powinniśmy zamknąć tam 1,5 miesiąca temu, no ale zamykamy ją dopiero za 2 tygodnie, czyli ustalamy, że no po prostu te tematy nie wchodzą do wersji grudniowej świadomie przenosimy tu nam marzec, mimo tego, że realizować, no będziemy teraz, no bo tak naprawdę tak powinien wyglądać cyklu, no.

**Damian Kaminski** 1:55:59  
Rozumiem o co ci chodzi, to znaczy rozumiem ogólnie się z tobą zgadzam, tylko to musimy też według mnie Janusz musi to zatwierdzić i Przemek musi to zatwierdzić, bo zawsze będzie taka tendencja, ale skoro już mamy to dopełnimy.

**Janusz Bossak** 1:56:13  
Nie, nie, nie, nie, nie, nie, nie, dobrze, dobrze, dobrze.

**Kamil Dubaniowski** 1:56:14  
No tak, skończyła się wersja czerwcową, dlatego chcę dać jasne odcięcie, że ten sprint zamyka nam no nowości w wersji grudniowej.

**Damian Kaminski** 1:56:15  
Ja nie no właśnie o to chodzi, dlatego to.  
Artykułuje.

**Janusz Bossak** 1:56:21  
Tak.  
Tylko żeby.

**Damian Kaminski** 1:56:24  
Bo to jest pokusa, zawsze, że a już mamy to dopniemy.

**Janusz Bossak** 1:56:28  
Popychamy edytor formularza, bo on jest on już jest zaistniał w wersji czerwcowej i go do popychamy.  
Tak nawet nie musimy. Według mnie tego edytora diagramu do wersji grudniowej teraz rzucać w ogóle.  
Niech będzie tym, który jest, nie będzie kusił i róbmy tak, żeby wydać to w wersji marcowej prostu nasza relacja.

**Kamil Dubaniowski** 1:56:52  
O k.

**Damian Kaminski** 1:56:52  
Dobra, czyli tak n czy beta do.  
Dobrze to zanotuję to czyli idzie tak.  
26 0 3.

**Kamil Dubaniowski** 1:57:05  
Tak wydanie prace trwają tak, ale wydanie znaczy trwają. Aktualnie są zawieszone na był skupiony w wersji grudniu.

**Damian Kaminski** 1:57:11  
No bo mam poczucie, że my musimy to omówić też chyba z przemkiem, żeby nie było jakiegoś zgrzytu na koniec.  
Ale tak wysoko wysoko poziomowe nieco do tej decyzji mam na myśli.

**Janusz Bossak** 1:57:22  
Sam.

**Kamil Dubaniowski** 1:57:22  
No.  
Tak ja.

**Damian Kaminski** 1:57:27  
Rudy mapy.

**Kamil Dubaniowski** 1:57:28  
No Przemek musi być świadome, że to nie ma miejsca na zgrzyt, bo mamy projekty od klientów i koniec.

**Janusz Bossak** 1:57:29  
No tak tak.

**Damian Kaminski** 1:57:33  
Mhm.  
No tak, tylko żeby po prostu wiecie, no nie było takiego jakiegoś tutaj, że on nie wiedział, że my to tak zaplanowaliśmy.

**Kamil Dubaniowski** 1:57:40  
No tak, tak jak najbardziej przedstawić wersję, co mamy w planie na wersję marcową na grudniową może.  
No bo realnie patrząc to, że my teraz przesuwamy diagram na marzec, to jest efekt taki, że u klientów to będzie gdzieś tam dopiero w czerwcu przyszłego roku.  
Pół roku odkładamy ten temat, tak jakby do do wydania dla klienta, no bo marzec my wydamy, to jest niby już produkcyjny, ale wiecie jak to wygląda, że instalacja to się odbywa tam 2 3 miesiące później.

**Damian Kaminski** 1:58:13  
Znaczy tu bym niekoniecznie to zamykam.  
No bo to jest taki element pobor.  
Boczny, jeśli my nie będziemy robić zmian w w funkcjonujących funkcjonalnościach raportów, tylko zmienimy źródła.  
To to można by dopychać.  
Żeby jednak te raporty systemowe w jakimś minimalnym zakresie do grudnia wydać, bo one są można powiedzieć takim pobocznym wątkiem do całego amo tita tak, powstaną jakieś źródła.  
W rasie definicję raportu i w zasadzie to jest, ale to mówię o szansie, że to możemy się nad tym zastanowić, że nawet jak tego nie robimy w tym sprincie, tylko w kolejnym, to to można dopchnąć.

**Kamil Dubaniowski** 1:58:53  
No tak, tak, tak tak to jest o tyle też i tak przy okazji tych raportów wychodzą jakieś wątki do samego modułu poprawki, no ale to to jakby na zasadzie bardów.

**Damian Kaminski** 1:59:03  
No to to tak zapiszę tak, że tu spróbujemy coś w ramach Przepraszam 25 12 dopchnąć na razie przynajmniej jest taki stan.  
No i tyle.  
To naprawiamy, to naprawiamy, to, to gdzieś się toczy w toczyło w tym sprincie. Tak nie wiem czy to zostało skończone.

**Kamil Dubaniowski** 1:59:28  
Tak, ja właśnie prosiłem przemko ta prezentacja się tak toczyło, że całej spieprzenia jak robiła.  
Ale efekt jeszcze nie bardzo chciał się nim chwalić, więc chcę zobaczyć. Dzisiaj jesteśmy wczoraj w sumie mieliśmy oglądać, ale nie zdążyłem.

**Damian Kaminski** 1:59:48  
Dobra, nic na razie wpisuję to ustalimy.

**Kamil Dubaniowski** 1:59:50  
Więc ja też tam sobie z gwiazdką zapisałem, że tą bazę wiedzy potencjalnie jeszcze Przemek coś tam będzie grzebał w niej w przyszłym sprincie, no bo tak jak mówię jeszcze tego nie widziałem, więc pewnie będę miał jakieś uwagi. No ale to główny cel był taki, że no żeby to nie było napisane przez ja i to tak jak nawet mamy tu zdefiniowane to chodzi o bezpieczeństwo, a nie.

**Damian Kaminski** 2:00:00  
Mhm.

**Kamil Dubaniowski** 2:00:09  
Tam jux czy ju wygląd są?  
Spodziewałem się, że w.

**Damian Kaminski** 2:00:14  
Dobra.  
Mów, ale ja chyba się to znaczy nie chyba muszę się przełączać, bo mi się zaczęło tam to spotkanie.

**Kamil Dubaniowski** 2:00:19  
Ja mam myślę, że tak tak to to co to co teraz bym miał w planie to właśnie nie wiem czy robić ten design czy ten czas na designie poświęcić na to żeby mamy już przypisane tematy, żebyśmy właśnie teraz skupili się na tym nawet krótkim jakimś blokiem tekstu napisać co jest naszym vip na ten sprint w tym temacie, a a potem zdecydować czy robimy jakieś indywidualne spotkania w temat.

**Damian Kaminski** 2:00:45  
To tak szybko w sensie masz na myśli, że w każdym temacie co Jestem vip tak.

**Kamil Dubaniowski** 2:00:49  
Tak, w sensie, co jest celem? Tak mamy mamy o k jest moim zdaniem teraz mamy temat edytor formularza.  
Ale jaki jest ten?

**Damian Kaminski** 2:00:59  
Dobra, to już już już to komentuje. W sensie my możemy to zrobić tutaj, nie, w sensie ja chciałem tylko to pokazać, że teraz to można otworzyć i tu napisać, że 2 punktach to znaczy, że robimy projekt na jeden dashboard, który zawiera 3 raporty, a tu robimy w komunikatorze. W zasadzie to już tu jest w sumie opisane tak to jest celem, czyli usprawnienie czatów grupowych i tam mogę tam. No dopisać, że integracja z grupami.

**Kamil Dubaniowski** 2:00:59  
Sąd będzie dla nas sukcesem na koniec sprintu.  
Tak, tak, tak, tak.  
No.

**Damian Kaminski** 2:01:27  
I ty, no dobra, można możemy to zrobić, ale według mnie decyzja o tym ju a Juma q to jest istotna. No to jest istotne.

**Kamil Dubaniowski** 2:01:29  
To to bym przed jako.  
Tak.  
No.  
No to to to zrobimy. To w ramach design i tyle.

**Damian Kaminski** 2:01:39  
Dobra, przełączam się, słyszymy się za pół godziny.

**Janusz Bossak** 2:01:41  
No i ten ta rozmowa z Piotrem nie architektoniczną to jest ważne.

**Kamil Dubaniowski** 2:01:45  
Tak to scrap tak ja rozumiem, że to jest ten temat. No ja taki skład zaraz tam zmontuję na design i wydaje mi się, że jeszcze jeden temat był, a ten komar hap.

**Janusz Bossak** 2:01:55  
Niefajna naczy z Piotrem mieliśmy rozmawiać o repozytorium i architekturze repozytorium.

**Kamil Dubaniowski** 2:02:00  
A to jeszcze trzeci temat, to znaczy Senat też pod kątem jakości tektury. Czy nie robimy tego kuster tak czy Piotr się zgadza na to miły i czy to pasuje ogólnie do architektura morita, czy w ogóle ktoś wie więcej coś o tym i poza adrianem?

**Janusz Bossak** 2:02:12  
Czy to jest bardziej front?  
To jest to jest frontend mniej.

**Kamil Dubaniowski** 2:02:17  
Tak no bo to taki temat jest no.

**Janusz Bossak** 2:02:19  
Inna biblioteka niż tą, którą my tam stosujemy. My mamy jakieś ten andy.  
Join i te rzeczy a miło jest po prostu inną biblioteką. No się wydaje, że namówię podejmowanie tego tematu.

**Kamil Dubaniowski** 2:02:31  
Dobra no.  
To od czego zaczynamy od jako prezydium?

**Janusz Bossak** 2:02:38  
No to trzeba wziąć znaczy repozytorium wolę, żeby już Damian może załatwił wiatrem.  
Bo on to repozytorium, rozumiem, opiekuję i najwięcej wie, więc najlepiej będzie z Piotrem rozmawiał i niech się oni już mówią, a my możemy tego właśnie Adriana tutaj wziąć i ten te 2 tematy ogarnąć tak, czyli.

**Kamil Dubaniowski** 2:02:57  
O KA, to jest ich kolor?

**Janusz Bossak** 2:03:00  
Partner, Comarch hab.  
No żebyśmy mieli te pliki projektowe, nie z tego wynikające.  
No dobra, ale to teraz czy na tym designer?

**Kamil Dubaniowski** 2:03:11  
Na dizajnie myślę.

**Janusz Bossak** 2:03:12  
Dobra.

**Kamil Dubaniowski** 2:03:15  
Mamy też im chwilę, żeby się tam.  
Nie wyrwali teraz taką nagle z roboty.

**Janusz Bossak** 2:03:21  
No ja tutaj nad tym też była, a właśnie bo tam. No może ty wiesz, bo Damian twierdził na tej chwili, że te foldery.  
Działają raporcie to sobie pokazywałem, że nie działa, no mnie działam, więc.  
On twierdzi, że nóż specyficzny.  
Moje jakieś dane, ale no robię. Kurde, no zwykły proces, który ma.  
10 pól i próbuje zrobić foldery i no nie działają. No więc co robię nie tak? No jak jest specyficzne dane, to nie jest jakiś.  
Zaimportowany proces cokolwiek, no po prostu wyklikane pierwszy proces 5 pól tam czy 10. Wchodzę w raport, biorę ten proces, wybieram typ raportu, wybieram grupy według folderów i nie ma folderów. No no co można zrobić tutaj nie tak po drodze.

**Kamil Dubaniowski** 2:04:20  
Znaczy w sensie to jest ta dziewiątka? Tak, wersja też sprawdzę w najbliższym siebie.

**Janusz Bossak** 2:04:24  
100 100 dziewiąta no.  
Na na środowisku testy to co ja przynajmniej robię tak to jest na testy emoticon no no bo.  
Próbuję, że tak powiem znaleźć najwygodniejszy sposób.  
Reprezentowania.  
Tej struktury i rotorua tak no bo można iść w stronę taką jak tu.  
Czyli jakby bardzo.  
Dosłownego odwzorowania tego, jak jest to zapisywane w wiatr była tak, czyli poziom tym Kategoria, pierwsza, druga, trzecia i czwarta.  
I te numerki.  
To pozwala właśnie powinno pozwolić, ale nie pozwala tak.  
Utworzyć właśnie drzewko, no ale tu musiałoby mieć tam trochę inaczej, być zorganizowane nie, no, ale próbuję tutaj to s jeden sobie wrzucić.  
Bo teraz jest no ja.  
Pierdziu no.  
Godzinę straciłem na to i to nie działało, a teraz działa.

**Kamil Dubaniowski** 2:05:36  
Już zwykli kuję tym na końcówce, no jest mnie o k no znaczy widziałem nadejdzie tak to nie, że tam widziałem na Daily, że nie było nic.

**Janusz Bossak** 2:05:46  
No nie działało, no przecież to wczoraj robiłem wieczorem już w końcu rzuciłem mu wydana, tam mam dosyć wkurzony Jestem, że to nie działa i i zostawiłem nie, a teraz wchodzę i oczywiście działań.  
No ale bynajmniej.  
Wracając do meritum, jakby tego i o r była tak, że szukam sposobu.  
Która metoda będzie najwygodniejsza? Tak czy metoda rodzic dziecko?  
Jako parent ma swoje zalety, ale nie mamy.  
Jakby mechanizmu, żeby to przedstawić tylko w gacie Jestem mechanizm i trzeba by go dorabiać.  
Albo taka metoda, jak tutaj zaprezentowałem, że po prostu jawnie wpisujemy.  
Te numerki?  
4 grupach.  
Ale gdzieś tam pod spodem trzymamy ten numerek taki.  
By sklejony, no bo trudno jest później operować teorema kolumnami jakby bez sensu nie, bo ten numer jest moje konsekwencją tak, że jak jest coś Zero Zero.  
To zanim jest numerek Zero?  
1 0 0 1, nie.  
Ostatnia ta czwarta kolumna w sumie konsumuje wszystkie poprzednie.  
Tyle że są te gałązki wyższe, które są tylko częścią. Jak gdyby tak takim subst ringiem tej ostatniej ewentualnie nie mają tych kolejnych zer, czyli pierwsze Zero pierwsze 2 cyfry.  
Pierwsze 3 cyfry i 4 cyfry takie są grupy.

**Kamil Dubaniowski** 2:07:32  
Mhm.

**Janusz Bossak** 2:07:32  
No i no dobra, jak teraz mam to do drzewko to mogę popróbować dalej. Tak no tak zrobiłem, że to jest jednocześnie i.  
Wyrobić według parlamenta i we i według takiego polskiego schematu no i tu sobie popróbuję co jest wygodniejsze, nie.  
No to ma później konsekwencje właśnie i w raportowaniu i w.  
Tym najważniejszym momencie, czyli przydzielaniu.  
Yy do sprawy.  
Klasyfikowaniu sprawy do jakiegoś tam?  
Teczki sprawy no.  
A teczki sprawy do Piotr wywołany to jest jak wykluczone, no dobra, to jak to działa to nie wiem, może się coś tu odświeżyło nie wiem, nie mam pojęcia.  
Ale działa, nie ma tematem na razie dobra to to dzięki.

**Kamil Dubaniowski** 2:08:27  
No dzięki.

**Janusz Bossak** zatrzymano transkrypcję
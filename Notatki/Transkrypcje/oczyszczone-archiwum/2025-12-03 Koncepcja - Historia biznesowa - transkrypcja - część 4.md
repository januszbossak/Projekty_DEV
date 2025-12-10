**Data spotkania:** 3 grudnia 2025, 10:16 - część 4

---

**Janusz Bossak:** Spinacz. To w moim przekonaniu musimy mieć to zapisane bezpośrednio w tej bazie, w tych kolumnach, których tutaj, które pokazujemy i których teraz tam nie mamy tego.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** I tam powinien być ten spójnik, wydaje mi się. Na pierwszy rzut oka, że tym spójnikiem jest właśnie to, co w sumie jest później, czyli w tym.

**Damian Kaminski:** Ale no właśnie, ten spójnik OK.

**Janusz Bossak:** Nie, nie, ja już tego. Ja już nic z tego nie rozumiem, wiecie?

**Damian Kaminski:** Dobra, bo ten spójnik nie istnieje w Rossmanie w sensie. Ten spójnik jest łatwy, jak jest JRWA i teczka, która istnieje pierwsza. A tutaj tym spójnikiem musi być ostatni element, bo to on ma wyświetlić to, co działo się wcześniej.

**Janusz Bossak:** No właśnie.

**Damian Kaminski:** A nie pierwsza sprawa ma wyświetlić to, co było następne, bo oni widzą ostatnią sprawę, która powstaje w tym momencie. Więc to nie może być coś w stylu MainCaseID, bo jego nie ma jeszcze, jak powstaje pierwsza sprawa, czyli jest pobieranie z e-Doręczeń. Czyli to jest bardziej w tym stylu, co powiedział Łukasz, że my tworząc nową sprawę, mamy tabelę powiązań wstecznych.

**Janusz Bossak:** Jak wstecznych? A skąd on był?

**Damian Kaminski:** Że ta nowo powstająca sprawa ma powiązania, że ten byt wirtualny wcześniej istniał w obrębie innych procesów. I w związku z tym trzeba tu wyświetlić to.

**Janusz Bossak:** Znaczy tak.

**Damian Kaminski:** Ja też tak na gorąco myślę, może gdzieś się nie spina to, ale.

**Janusz Bossak:** Wracając do tego pomysłu, który którymś momencie rzuciłeś, czyli pola linked.

**Damian Kaminski:** No.

**Janusz Bossak:** Pole linked jest genialne do tego, żeby tą naszą jakąkolwiek sprawę związać z czymkolwiek innym. Czyli z tą sprawą, którą uznajemy za nadrzędną. Znaczy może nie nadrzędną, ale powiązaną. O tak, boże, taki related.

**Damian Kaminski:** Mhm. Mhm.

**Janusz Bossak:** Tyle że problem z polem linked polega na tym, że musisz wybrać proces, żeby skonfigurować to pole. Brakuje nam funkcjonalności pod tytułem pole linked z dowolnego procesu.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** I z dowolnej sprawy, oczywiście do takiej, do której mam dostęp. I wtedy, tak jak mówisz, jeżeli tym obiegiem tam e-Doręczenia mi coś wpadnie, to ktoś kumaty weźmie i powie, to dotyczy tego. I wybiera sobie tam jakąś korespondencję czy cokolwiek innego.

**Damian Kaminski:** No tylko mamy to natywnie, bo mamy to w formie. Tylko mamy to w formie.

**Janusz Bossak:** No w tym prawym panelu.

**Damian Kaminski:** Tych spraw powiązanych, tak ogólnie.

**Janusz Bossak:** Tak, tak, tak. On nie ma linked.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** I można to wykorzystać, ale jeszcze raz się bym przyjrzał, bo ja mam wrażenie, że my nie, no sami nie pamiętamy. Ja też się przyznaję, nie pamiętam, bo czytam to co jest na środku ekranu, bo mam na wielkim ekranie to. I tu jest, zobaczcie te dwa, jakby czy to są dwa przykłady, że to jest jeden przykład, ale jest tak obejrzeć.

**Damian Kaminski:** Dwa.

**Janusz Bossak:** EventID, ObjectBusinessSubjectName, ObjectBusinessSubjectID, ObjectBusinessSubjectType. A poniżej i tam jest AddCaseEvent tego obiektu. A poniżej mamy ObjectType.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** EventTypeID, SubjectCreateObject.

**Damian Kaminski:** Bo.

**Janusz Bossak:** I teraz jest sam user, Jan Kowalski. Nie wiem, czy to jest.

**Damian Kaminski:** Bo to jest zagnieżdżone.

**Lukasz Brocki:** To jest to samo na dwa sposoby. Obsługa na dwa sposoby, bo można zrobić obiekt subject i go uzupełnić i go dodać do obiektu, który jest przekazywany do funkcji. Bo można bezpośrednio ten obiekt, który jest dodawany do CaseEvent, uzupełnić.

**Janusz Bossak:** No ale to jak mam tą środkową, czyli ten ObjectBusinessSubjectID, to efekt końcowy w zapisie w bazie danych jest identyczny jak ten na dole?

**Lukasz Brocki:** Tak, zgadza się.

**Janusz Bossak:** Czyli trafia to do tego message w sumie.

**Lukasz Brocki:** Dokładnie, to będzie identyczne.

**Janusz Bossak:** No i.

**Damian Kaminski:** To po co jest to, po co jest to?

**Janusz Bossak:** No właśnie, to jest zmyłka.

**Damian Kaminski:** No właśnie.

**Janusz Bossak:** Znaczy to musisz zrobić.

**Lukasz Brocki:** W sumie tak, ta linijka nie jest potrzebna, bo nas kropka name, od razu Jan Kowalski.

**Damian Kaminski:** Widzą to będzie natywnie zrobione, prawda?

**Lukasz Brocki:** Tak.

**Damian Kaminski:** No niepotrzebnie to jest podane.

**Janusz Bossak:** Wydaje mi się. Dobrze, ale wracając jeszcze do tego, bo kluczowe jest tutaj te trzy rzeczy, bo to pamiętam. Myśmy ustalali właśnie ten BusinessSubjectName, BusinessSubjectID i BusinessSubjectType. To jest kluczowe, bo to rozwiązuje nam ten temat, tylko że to jest trzymane właśnie w tym message. I tu jedyna rzecz, która mi nie pasuje, bo niełatwo się tym będzie posługiwać w jakichś tam raportach. Ale to jest właśnie to, o co nam chodzi. To jest ta spinka. To jest ten poziom spinania.

**Damian Kaminski:** Tak, to się zgadza. To się w 100 procentach zgadza, tylko po prostu forma zapisu, tak jak mówisz. Dlatego może rozwiązanie Łukasza jest słuszne. Powoduje, że to jest słabo indeksowane, będzie to niewydajne, bo mamy JSON, który co do zasady trzeba w całości przeszukiwać, żeby stwierdzić, czy mamy to wyświetlić, czy nie mamy. A jak mamy jednak kolumny?

**Lukasz Brocki:** Tak. A jak przerzucimy to do oddzielnej tabeli, w ogóle do oddzielnej tabeli, to można nawet dać kilka subject. Tak, możemy, dotyczy to kilku i wtedy mamy.

**Janusz Bossak:** No tak, dokładnie.

**Lukasz Brocki:** Tyle nie, że przeszukujemy pole JSON, tylko po kolumnach lecimy, więc jest o wiele szybciej. Plus możliwości łatwego przeszukiwania w wielu kontekstach.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Tak mi się wydaje. My mamy to źle zrobione według mnie. Bo ten EventType.

**Damian Kaminski:** Znaczy wiesz, nie tak źle, tylko to da się poprawić. To nie jest.

**Janusz Bossak:** Znaczy trochę jest to przekombinowane. Bo nie do końca chyba wtedy rozumieliśmy, czy ja tam nie do końca rozumiałem jeszcze te wszystkie jakby tematy z Aliansu. I tak żeśmy próbowali coś zrobić. Mi się wydawało, że to jest OK, ale to nie jest OK.

**Damian Kaminski:** No tak, tylko skutek teraz naszej dyskusji z ostatnich minut jest tylko taki, że z tego nie robimy JSON, tylko robimy wiązanie w innej tabeli.

**Janusz Bossak:** Tak.

**Damian Kaminski:** I dalej musimy to sprowadzić do tego, że ten typ musi być skatalogowany. On nie może być, jaki kto chce.

**Janusz Bossak:** Tak.

**Damian Kaminski:** My musimy wiedzieć, czy mamy pokazać dla user, nawet odnosząc się.

**Lukasz Brocki:** Tak, jeżeli mamy mieć wyszukiwanie po typie, to musi to być skategoryzowane w jakikolwiek sposób, ale musi.

**Damian Kaminski:** No.

**Janusz Bossak:** Znaczy według mnie to nie powinno być kategoryzowanie przez słownik.

**Damian Kaminski:** Nie, nie w systemie.

**Janusz Bossak:** Bo znaczy z jednej strony.

**Lukasz Brocki:** W systemie tak.

**Damian Kaminski:** W kodzie.

**Janusz Bossak:** No właśnie, pytanie czy?

**Lukasz Brocki:** Enumerator.

**Janusz Bossak:** Czy w kodzie?

**Damian Kaminski:** W kodzie, bo potem nawet powiedziałbym to, co ty Janusz tam rzuciłeś chyba wczoraj. Tu Łukasz tego nie słyszał, ale nawet jeśli zrobimy taki pulpit menadżera, kogo sobie tam nazwiemy, to my możemy mu wyświetlić ostatnie twoje ostatnie zdarzenia biznesowe i wyszukać po user ID, dać mu listę co on ostatnio zrobił kluczowego. Bo ta historia biznesowa ma przedstawiać kluczowe elementy, a nie tam całą historię spraw, które przemieli.

**Janusz Bossak:** Dokładnie, więc to są takie typy, które są amoditowymi typami. Natomiast to, co jest wyżej, w drugim szarym kwadraciku od góry, gdzie jest EventType, MailSend. Mhm.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Jeszcze tutaj. I to były zdarzenia, których wtedy żeśmy dyskutowali, nie wiemy jakie typ eventu.

**Damian Kaminski:** To już jest słownik, tak?

**Janusz Bossak:** To jest słownik i tak i tutaj.

**Damian Kaminski:** Czyli to mówiąc wprost, to żeby zobrazować to, co mówisz, to jest po prostu to pobranie korespondencji z e-Doręczeń, róbcie co chcecie, nazywajcie to jak chcecie. To są wasze zdarzenia biznesowe.

**Janusz Bossak:** Tak. I ponieważ one mogą być powtarzalne, dlatego była propozycja jakiegoś tam słownika. I z tego słownika się tutaj przypisuje coś tam. No tu akurat jest w tym opisie funkcji to zrobione tak tekstową, że MailSend, ale to może być tam pobranie wartości ze słownika i.

**Damian Kaminski:** I to tak jest, to jest tu. Zobacz, to jest wtedy pobranie wartości, bo to ID jest globalne w kontekście wszystkich słowników. Czyli można podać tak, a można podać nazwę słownika i nazwę wartości. To jest alternatywa.

**Janusz Bossak:** No, no, no, no, no tak, tak, coś takiego.

**Damian Kaminski:** Mhm, tak.

**Janusz Bossak:** OK, to powoli cośmy odtworzyli sobie, jak to teoretycznie powinno działać. Ten pomysł tutaj Łukasza według mnie jest bardzo dobry, bo tym JSON to będzie kłopot w odtwarzaniu tego, robieniu raportów i tak dalej. A jeżeli damy te właściwie dwa parametry, według mnie nawet wystarczą, typ powiązania i to ID powiązania. Żebyśmy wiedzieli, jak to jest na przykład user, to będziemy szukać po user ID. Jeżeli to będzie napisane case, to będziemy szukać po CaseID sprawy. Jeżeli co, możemy jeszcze mieć grupę. Po grupie na przykład będziemy.

**Damian Kaminski:** Tylko teraz, tylko teraz wróćmy do tego przypadku ich i pytanie, jak wy widzicie wtedy ten panel faktycznie już w takim użyciu widocznym dla użytkownika. Bo załóżmy, że mamy te wiązania i mamy typ case, więc wiążemy, możemy powiązać dwojako, albo inaczej musimy inaczej. Otwierając, które są powiązane w zasadzie szuka. Może tak teoretycznie, bo właśnie to jest przedmiotem ustalenia. Przeszukujemy bazę w kontekście tej tabeli, którą mamy po CaseID i to mamy wynik historii zdarzeń biznesowych powiązanych z tą sprawą. A teraz przeszukujemy drugą tabelę tych powiązań w kontekście tego powiązania po CaseID. I wtedy mamy informacje z innych spraw, z innych historii biznesowych tych spraw, które są powiązane z tą sprawą. I teraz jak to tu wyświetlić, żeby to się nie mieszało. Bo powiedzmy wchodzimy i teraz mamy informacje chronologicznie przedstawione. Ale przekierowanie do innego działu, może inaczej, pobranie to jest jeden proces, przekazanie do właściwego działu to jest ten sam, powiedzmy proces. Przekierowanie do innego działu to już jest jakiś proces obiegu korespondencji X. Dopiero tutaj zaczyna się proces korespondencji tej właściwej. Teraz jak to ludziom pokazać, co pochodzi z innego kontekstu, a co pochodzi z tego? Innego kontekstu mam na myśli sprawy jako bytu technicznego. Ale no właśnie wszystko wyświetlamy, bo wszystko jest zasadne dla kontekstu biznesowego. Nie wiem czy, dobrze, czy rozumiecie o co mi chodzi?

**Janusz Bossak:** Rozumiemy. Ja bym na to spojrzał raczej od strony jakby użytkowej. Bo w tym Rossmanie ciągle nie rozumiem, nie wiem, w którym momencie i kto ma decydować co z czym powiązać.

**Damian Kaminski:** Automat. O co z czym powiązać decyduje użytkownik, mówiąc, że to do niego nie należy. Więc tu wtedy następuje, powiedzmy wiązanie, czyli nowo powstająca sprawa wiąże się historią biznesową ze starą sprawą.

**Janusz Bossak:** Bo punkty wejścia to są jakie? To jest ten, że utworzy się przez e-Doręczenia albo utworzy się normalnie ze zwykłego maila coś?

**Damian Kaminski:** Tak.

**Janusz Bossak:** Pytanie właśnie, gdzie jest początek?

**Damian Kaminski:** No załóżmy, że e-Doręczenia, żeby to już uprościć. E-Doręczenia proces pobierania z e-Doręczeń jako osobny byt tylko do tego. I on kieruje na różne procesy. Bo on powstał dlatego, że nie ma jednego procesu obiegu korespondencji, tylko jest kilka, więc musiał być jeden byt, który będzie spięty z e-Doręczeniami i będzie to dalej dzielił.

**Janusz Bossak:** Rozumiem, czyli.

**Damian Kaminski:** Wiesz, to tak naprawdę łata, mamy historyczne podejście. To nie jest wdrożenie nowe, które byłoby inne, tylko jest jak było i teraz trzeba na to nanieść właśnie.

**Janusz Bossak:** Dobrze, OK, dobra. Czyli powiem jak ja to rozumiem. Chyba źle rozumiałem, a teraz już mi się objaśniło. Czyli jak coś wpłynie z e-Doręczeń.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To nie interesuje nas jakiś nad, nadsprawa tego wszystkiego jak w rozumieniu teczki JRWA, do której trzeba to włączyć. Nie interesuje nas to. Interesuje nas to, że ten konkretny dokument wpłynął z e-Doręczeń. I w którymś momencie ktoś go przepnie na inny proces.

**Damian Kaminski:** Nie.

**Janusz Bossak:** A my chcemy śledzić ten dokument, który przed tymi e-Doręczeniami po prostu.
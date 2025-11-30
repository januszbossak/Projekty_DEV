**Data spotkania:** 3 listopada 2025, 08:01 - część 4

---

**Damian Kaminski:** To może jeszcze ja dopowiem, Piotrze, bo tam rozmawialiśmy o wydaniu takim oficjalnym, bo to poszło tylko nie było o tym informacji tej historii logowania maili. To to jest tylko backendowo na razie czy tutaj też jesteś w stanie coś pokazać?

**Piotr Buczkowski:** No to zgłoszenie było. To było zgłoszenie.

**Damian Kaminski:** No teraz o tym po prostu przypomniałem, że rozmawialiśmy pod koniec tygodnia, żeby to.

**Piotr Buczkowski:** Już patrzę. Znaczy. To to wersji to czerwcowej, tak?

**Damian Kaminski:** Już mam 21 512. A to jest po prostu na sprawie. To chyba to jednak już pokazywałaś, ale może warto o tym przypomnieć, bo to już właśnie jest.

**Piotr Buczkowski:** Tutaj będzie jeszcze nie ma tej funkcjonalności, którym mówiliśmy, czyli tak naprawdę logowane i logowane jest dodanie do kolejki do wysłania. Jeszcze nie wiem, czy to rzeczywiście zostało wysłane czy nie, czy na przykład job sobie.

**Damian Kaminski:** Tylko nie pokazujesz, nie wiem czy. Pokazujesz coś?

**Piotr Buczkowski:** A sorry, przepraszam z to już rozłączyłem, zapomniałem, że jeszcze rozłączyłem. To tak jak w piątek żeśmy mówili, to będzie zakończone. Będzie to zadanie będzie zakończone, będzie nowe zadanie, że dodać oznaczanie, że dany mecz został nie tylko dodany do kolejki do wysłania, został wysłany z tej kolejki. Znaczy tutaj wpis będzie dodawany tak jak teraz, ale będzie dodatkowy znacznik, że wysłany. A jak nie, jak będzie wpis, nie będzie wysłany, to znaczy, że jest w kolejce.

**Damian Kaminski:** To będzie z poziomu sprawy, czyli z poziomu sprawy będzie informacja o wysłanych mailach ze sprawy. W ramach pierwszego MVP będzie to właśnie informacja o tym, jakie maile zostały wygenerowane. Jeśli ktoś ma ustawione, że dostaje maile raz dziennie.

**Piotr Buczkowski:** Tak, tak, tak.

**Damian Kaminski:** No to to jeszcze nie jest potwierdzenie i teraz do tego dochodzi kolejne zgłoszenie, które będziemy realizować w tym sprincie, które właśnie uzupełnij informacje, że ten mail faktycznie już został wysłany. To zostanie odznaczony przez. No właśnie joba, ale skorelowane go jeszcze z ustawieniami użytkownika, tak jak często te maile faktycznie dostaje.

**Daniel Reszka:** Na blogach tego nie będzie.

**Piotr Buczkowski:** No też.

**Damian Kaminski:** Jak to w logach?

**Daniel Reszka:** W ramach ogólnych. Maile wysyłane.

**Damian Kaminski:** A po co to ma być w logach ogólnych?

**Piotr Buczkowski:** Znaczy to, co jest to, co jest w logach to nic się nie zmieniło, tylko że logi wiadomo co wygasają, skasowane. Jeżeli oczywiście ktoś tego nie wyłączy, bo...

**Daniel Reszka:** A to będą utrzymane to tak.

**Piotr Buczkowski:** Chyba będę trwać w czasie, a to jest trzymane tak.

**Daniel Reszka:** OK.

**Damian Kaminski:** To jest historia, żebyśmy dobrze zrozumieli kontekst biznesowy. To jest też z WIM-u potrzeba. Historia maili wysłanych do sprawy i tylko to w sensie nie jakieś inne maile, tylko to są w kontekście sprawy historia wysłanych maili.

**Piotr Buczkowski:** To jest.

**Przemysław Sołdacki:** Gdzie mam jeszcze pytanie, bo to od klienta, z którym ostatnio rozmawiałem i to dla niego jakby było na tyle krytyczne, że jakby klient jest chętny zmienić system, bo nie potrafimy tego obsłużyć. Mianowicie kwestia, że w momencie, kiedy się wczytują maile, to jest pod kątem OCR-a, czyli faktury się wczytują i niektóre faktury nie są wczytywane z jakiegoś powodu, że tam jakiś niewłaściwy format PDF czy coś w tym stylu, żeby rejestr, przypadki, które mail się nie wczytał, czy tam?

**Piotr Buczkowski:** W tej chwili w tej chwili jest taki mechanizm, który powoduje, że jest wysyłany mail do wskazanych osób. Czy to jest gdzieś tutaj było?

**Damian Kaminski:** Wyżej, bo jesteś w plikach wyżej. Musisz przyjść sekcję mail od.

**Piotr Buczkowski:** A okej?

**Przemysław Sołdacki:** A jest mail wysyłany w momencie, kiedy się dany...

**Piotr Buczkowski:** Nie udało danego maila wczytać.

**Przemysław Sołdacki:** OK. To klient musi to w trybie ekspresowym dostać tą wersję.

**Piotr Buczkowski:** A nie przed. To jest od zawsze. A nie to jest ustawienie systemowe, przepraszam.

**Daniel Reszka:** Chodzić te log errors coś takiego.

**Piotr Buczkowski:** Tak, oto nie, nie sen temat postu.

**Przemysław Sołdacki:** Znaczy powiem wam o co?

**Piotr Buczkowski:** I wiele wiele firm z tego korzysta.

**Przemysław Sołdacki:** To OK. No to tylko jedną rzecz powiem, bo klientowi nie chodzi o to, że się błąd wczyta, to znaczy mail się wczytał, ale z jakimiś błędami, tylko że się w ogóle nie wczytał.

**Piotr Buczkowski:** Nie, jeżeli nie udało się spasować maila. Znaczy, po pierwsze musi to dojść do nas, tak?

**Przemysław Sołdacki:** No tak.

**Piotr Buczkowski:** Jeżeli może dojść do skrzynki zdefiniowanej, został pobrany przez LoadMail, job, ale z jakiś powodów nie zostały otworzone sprawa. Informacja o tym jest wysyłana do osób. Czytam to na adres mailowy, zdefiniowany w tym miejscu.

**Przemysław Sołdacki:** W której wersji to jest to jakiegoś czasu? Czy to jest?

**Piotr Buczkowski:** Od zawsze, od zawsze.

**Przemysław Sołdacki:** No to kurde Daniel koniecznie od razu was trzeba to ustawić.

**Daniel Reszka:** No właśnie zobaczyć co tam jest.

**Przemysław Sołdacki:** No wiesz co możesz najpierw ustawić się żeby szu, a można 2 maile wpisać.

**Piotr Buczkowski:** Można kilka maili wpisać rozdzielone średnikiem.

**Przemysław Sołdacki:** Daniel to wpiszmy dane tego dyrektora plus na przykład nie wiem, twój mail albo konsultanta, żeby sprawdzić, czy to dobrze dochodzi, jeśli coś jakoś faktura im się nie wczytała, żeby od razu wiedzieli, że się nie wczytała.

**Piotr Buczkowski:** Tam prosiłem o jakiś sygnał, mówili, że czasami kilka razy wysyłają i dopiero któraś przechodzi. Jeżeli dałoby się informacje, kiedy wysłaliśmy, który nie wszedł, to poproszę, przeszukam logi z tego czasu logi serwera mailowego.

**Daniel Reszka:** Właśnie czekamy na to Piotrek wiem, ja od czwartku już to.

**Przemysław Sołdacki:** Wiecie, bo to znaczy.

**Piotr Buczkowski:** Bo to jest za dużo, żeby szukać.

**Przemysław Sołdacki:** Biznesowo jest tak, że oni wysłali na przykład 500 maili, czyli 500 faktur i kilka faktur się nie wczytało. Nie wiedzą która i później jest problem, że nie zapłacili faktury, bo nie wiedzieli, że nie weszła i to jest ich główny ból. Nie chcą informacji, że coś się wczytało, ale na przykład coś tam może częściowo nie odczytał czy jakieś inne rzeczy, tylko to, że po prostu została pominięta faktura, bo dla nich jest największy ból. Także.

**Piotr Buczkowski:** Znaczy to.

**Damian Kaminski:** Znaczy, ja przyznam, że ta informacja, o której dzisiaj Piotr mówi, ona jest od zawsze, ale ona nie jest rozpropagowana wśród wiedzy. Ee bo ja samo nie nie wiedziałem i zakładam, że większość działu i serwisu i wdrożeń o niej nie wie, więc trzeba to pewnie uzupełnić w postaci dokumentacji do twórz sprawę z maila tam, jeśli ktoś to definiuje. To zrobię zgłoszenie, że po prostu dopisać, że należy tutaj uzupełnić parametr, aby właśnie w przypadkach błędów ktoś zostawał taki komunikat.

**Przemysław Sołdacki:** Wiesz co i od razu jak tutaj widzę ten jakbym wszedł w te ustawienia systemowe, nie wiedziałbym do końca, że to do tego służy ten opis, który mamy pod spodem. Sen information na bounty validity mail to dis adres to, no to jakby to miało, nie wiem 3 zdania i opisywało dokładnie na czym to polega, no to byśmy mogli dotrzeć. Chociażby nie wiem, Copilot mógłby mieć do tego dostęp i by powiedział, że coś takiego jest. Czy Copilot czyta te ustawienia systemowe, ale pewnie łatwo zrobić, żeby mógł to czytać.

**Damian Kaminski:** To tego jesteśmy świadomi.

**Przemysław Sołdacki:** Tylko tu opisy, żeby były to jakieś takie zrozumiałe, że to to chodzi, tak.

**Damian Kaminski:** Biznesowe.

**Piotr Buczkowski:** Znaczy jakiś czas temu przygotowałem mechanizm, że można te opisy robić, wbijam luz, tłumaczeniem, tak są opisy do funkcji.

**Damian Kaminski:** Tak jest.

**Piotr Buczkowski:** Może warto zacząć z tego korzystać?

**Przemysław Sołdacki:** Życie toczy.

**Damian Kaminski:** Nie to było. Tak, tak to było na naszą prośbę tutaj zgadzam się i zgadzam się z waszymi obydwoma wypowiedziami i my tutaj, w kontekście Janusza, Kamila, Łukasza mamy tego pełną świadomość po prostu. To jest plan, żeby się zajmować tym w tym kwartale, bo tutaj nie, nie właśnie na podstawie tego, co stworzył Piotr nie ma już potrzeby angażowania deweloperów, możemy to sami przygotować. To opis.

**Przemysław Sołdacki:** Dobra, no to to wasko to jest po prostu pilne. Bo klient jest tak powiem, jeśli tego szybko nie rozwiążemy, ten klient będzie chciał odejść, a to są jest dla nas strata finansowa.

**Piotr Buczkowski:** Znaczy oni tam korzystają z tej współdzielonej skrzynki chmurowej co jest.

**Przemysław Sołdacki:** Przenieśmy to na nich będzie na ich skrzynce też nie musi być na naszych.

**Piotr Buczkowski:** To niewłaściwe.

**Przemysław Sołdacki:** No mieli dostęp.

**Piotr Buczkowski:** To można dostępu mąż.

**Damian Kaminski:** Dobra, to słuchajcie. Ja proponuję, żebyście zrobili krótkie spotkanie. Może właśnie tu Piotrek, Danie, w sprawie tego klienta, żeby to zaopiekować, a teraz kontynuujmy cele tego spotkania.

**Przemysław Sołdacki:** Wykładnia.

**Daniel Reszka:** Ja tylko dopytam tutaj normalnie średnikiem jak zwana ja się podaję tak. W kontekście tego pola. O KAO to mi chodziło właśnie.

**Piotr Buczkowski:** To jest po prostu wstawiany do adresu tu.

**Daniel Reszka:** OK.

**Piotr Buczkowski:** Przecinek też.

**Damian Kaminski:** Dobrze, Piotrze czy coś jeszcze? Chciałbyś? Omówić.

**Piotr Buczkowski:** Nie, tylko ty.

**Damian Kaminski:** Dobra, Marek TrustCenter.

**Marek Dziakowski:** Jeżeli chodzi o TrustCenter aktualnie. Przynosimy po kolei joby, zaczęliśmy od blockchaina, jest, znaczy nie wiem co to zbytnio pokazywać, bo to nowość.

**Damian Kaminski:** Możesz opowiedzieć?

**Marek Dziakowski:** Tak, są problemy z blockchainem, aktualnie pojawiają się bloki, które są jakby nie są w łańcuchu, tylko jakby oddzielnie. Z tego względu postanowiliśmy przenieść to i dzielić to z projektu webowego. Aktualnie będzie to organizowane przez usługę Windows Service, czyli w zasadzie tak jak to ma miejsce w AMODIT, więc będzie analogiczny.

**Damian Kaminski:** OK, po prostu działania. Takie optymalizacyjne to wszystko tak. Dobrze jeszcze mamy. A nie? Łukasz ja briana według mnie z osób, które się nie wypowiadały, więc. A nie odczytywać też coś, zaprezentować, coś opowiedzieć? Ania robiła też dużo poprawek i błędów, więc proszę.

**Anna Skupinska:** E nie działał mi przepraszam, miałam wyłączony mikrofon. Tak jeśli chodzi o mnie to ostatnio mam dużo poprawek, dlatego, że Łukasza pytanie było, a to z nim robię te rzeczy od raportów, od raportów systemowych. Więc, no to, no póki Łukasz moc nie, nie przyjdzie, to te raporty są trochę na stopie, a ostatnio robię.

**Lukasz Bott:** Ja już myślałem, że zrobiłaś.

**Damian Kaminski:** Do. Już jest.

**Anna Skupinska:** No właśnie, skoro jesteś w związku to super.

**Damian Kaminski:** No to się tym zajmiecie.

**Anna Skupinska:** Pracowałam też trochę nad tłumaczeniami, ale przestałam na tym pracować, żeby zrobić się błędy, bo to było ważniejsze.

**Damian Kaminski:** Dobrze, ja mogę, proszę, proszę.

**Lukasz Bott:** No dobra to.

**Damian Kaminski:** OK, ja wspólnie tutaj za nią testowaliśmy też funkcjonalności, które powstały jakiś czas temu w związku z tymi dynamicznymi źródłami. Nie będę tego pokazywał. Bardziej powiem, że zostało to przetestowane w boju właśnie już w potrzebach takich wdrożeniowych. Kilka dodatkowych aspektów takich usprawniających prace wdrożeniowe zostało też dodatkowo rozwiązanych. No i tyle, że tak powiem. Przełożyliśmy teorię na praktykę, więc tutaj za nią też współpracowałem w ramach tego sprint, żeby te funkcjonalności były jeszcze lepiej dopracowane. Dobrze, Łukasz, Adrian, Łukasza nie było połowę sprintu, więc nie wiem, czy ty masz jakieś nowe duże.

**Lukasz Brocki:** Ja tylko jakieś mniejsze poprawki, a tak to ponad połowę sprintu mnie nie było, więc większość rzeczy nawet nie brałem do siebie.

**Damian Kaminski:** OK, Adrian.

**Adrian Kotowski:** To mnie tak pokrótce, udało się ustabilizować te problemy zapie doręczeń. Tam już muszę. Teraz klienci już tam były, żadne błędy nie występują. Drobne poprawki backendowych obszarze do formularzy i to jest jakaś mniejsze funkcjonalności. Też teraz pracuję nad tym rozszerzeniem, chce w konektora, myślę, że tam ciekawsze rzeczy będę miał za 2 tygodni do pokazania, jak już ta integracja z, z nowej integracji z konektorem będzie zakończone i ten wyjdzie nowy też. Tak będę właśnie pracował nad nowym, nowo nowym Mikołajem w tej aplikacji do podpisywania dokumentów, fajna forma QKCS, więc myślę, że 2 tygodnie tam będzie jakiś ciekawszy, jego ciekawszy demonstrację. Jeszcze jakieś tam wsparcie w obszarze e-Nadawcy i to tyle, jeśli chodzi o mnie. Bardziej można powiedzieć opowiadając, niż pokazując.

**Damian Kaminski:** A technicznie jakbyś mógł powiedzieć jeszcze o tej integracji na Maka, podpisywanie Szafirem działa już jest skończone tak, m szafirem.

**Adrian Kotowski:** Tak, lecieliśmy, przepijemy trwają jeszcze, to jest to jest właśnie zlecam Kamilowi, bo nie mam nic, dysponuje fizycznie tutaj podpisem m szafir, natomiast tutaj głównie teraz chcemy skupić na nowym wyglądzie. Już teraz dostaliśmy bardzo szczegółowy projekt wytyczne do aplikacji. Właśnie wybraliśmy technologie MAUI.NET, związku z tym, że to kontynuacja można powiedzieć taka następca sama rina, więc tutaj chcemy iść w tą stronę. Widzę, że jakieś pytania są, to może pierw Daniel widzę.

**Daniel Reszka:** Znaczy, ja chciałem o to e-Doręczenia, czy tam już wszystko jest zrobione, bo tam coś mówili, że teraz rzeczywiście wpadają wszystkie te doręczenie, tylko tam jest problem coś z raczkowaniem, że zamiast to w jednym, jakby w jednym nie wiem.

**Adrian Kotowski:** Natomiast co to to problem e-Nadawcy jest to temat inny jakby inną usługę, to już to też jest jakby teraz mam już tam pomysł jak to poprawić.

**Daniel Reszka:** W sensie analizujesz to jeszcze tak?

**Adrian Kotowski:** Teraz tylko przekazałem Łukaszowi, bo do teraz jestem Łukasz, ale mam już pomysł jak to naprawić, więc to.

**Daniel Reszka:** OK. Dobra, to ja tylko to chciał.

**Adrian Kotowski:** Teraz Przemyk tak dzięki Przemek.

**Przemysław Sołdacki:** Tak wiesz co, bo jak ty mówisz, że nie możesz testować m Szafira, ponieważ Szafira i musi tam komuś dawać, to w takich sytuacjach to tam nie ma co czekać, po prostu trzeba ci kupić m Szafira, bo jeśli to ma przyspieszyć ci pracę, no tam nie wiem ile kosztuje ten Szafir, nie wiem 100 zł, 200 zł czy tam 300? Nie wiem wszystko jedno to po prostu dobrze byś miał.

**Damian Kaminski:** Ale.

**Janusz Bossak:** Wreszcie.

**Damian Kaminski:** Czy ta współpraca to jest jakaś problematyczna? W sensie było to z Kamilem naszym tutaj Dubaniowskim, więc wydaje mi się, że to nie jest tutaj problem.

**Przemysław Sołdacki:** No ja wiem, ale, ale wiesz, to jest jakiś taki narzut pracy, że tam komunikacja między 2 osobami. Jedna osoba testuje, przekazuje błędy. No to w sumie lepiej kupić tego Szafira, nie wiem, to pewnie trzeba się najpierw autoryzować kość onlineowo, żeby ten podpis dostać i sobie już testować. Bez sensu, żeby tutaj Adrian tego nie miał czy coś.

**Kamil Dubaniowski:** No o ile się nic nie zmieniło to niestety dałem Szafie. Ja trzeba do nich dopiero jechać do centrali jednej z pamiętam, że życzy.

**Damian Kaminski:** OK.

**Przemysław Sołdacki:** No to nawet jeśli, ale wiecie, jeśli.

**Adrian Kotowski:** Czy to już piłem? To nie ma problemu.

**Przemysław Sołdacki:** No to wiesz, bo chodzi o to, że nie wiem, teraz będzie sprawdzał za jakiś czas, nie wiem jakiś powiedzmy problem wystąpi, to żebyś po prostu odpalił siebie, przetestował, zobaczył na czym problem polega, a nie prosił Kamila, żeby on ci testował i ci przekazywał błędy. To jakby wie.

**Adrian Kotowski:** Czy to to samo jakby rozciągnąć na innych dostawców, bo też mamy w planach? Poza tym miałem PP. Na przykład podpisy PWP też ogarnąć podpisy właśnie od Enigmy, więc to jest też.

**Przemysław Sołdacki:** Słuchaj, to znaczy to z punktu widzenia firmy, jakby dla mnie jest opłacalne, żebyś ty sobie zrobił. Nawet nie wiem. 5 różnych rodzajów podpisów i ich miał po to, żebyś mógł to diagnozować u siebie i jakby nie czekając na kogokolwiek, bo to to nie jest jakiś koszt znaczący, a może ci przyspieszyć pracę?

**Damian Kaminski:** No dobra, to Adrian sobie po prostu załatw. Ja widzę tylko usprawniając, że można się potwierdzić online e-bankowością, więc.

**Kamil Dubaniowski:** Ale wybrane banki tam było bardzo ograniczona. Pula jakieś kradną, ja się nie wpiąłem.

**Damian Kaminski:** No to pytanie czy ci będzie pasować?

**Kamil Dubaniowski:** 5 banków i to takie typu. Taka o chyba jest jak taki bardziej popularni.

**Piotr Buczkowski:** Nie można podpisać się dowodem to co ostatnio wyszło. PM obywatelem, przepraszam.

**Kamil Dubaniowski:** Ja ostatnio nawet dostałem komunikat, że jak się nie zaloguje do aplikacji w jakimś tam czasie, bo coś zmienili, to będę musiał przyjechać fizycznie, znowu się autoryzować UNI.

**Damian Kaminski:** Wrzucam na czat jakie banki są dostępne. Żeby usprawnić.

**Przemysław Sołdacki:** Słuchajcie, to albo to się online da, albo trzeba będzie podjechać, natomiast jakby. Przekaz ode mnie jest taki, że jakby ja nie mam oporu tutaj mentalnego, żeby zapłacić za wystawienie jakiegoś podpisu, żeby Adrian sobie szybciej testował. Jest Adrian, jak potrzebuję, żebyś nie musiał nikogo czekać, to sobie pojedź. Firma zapłaci ci za to, żebyś ten podpis miał i tyle.

**Adrian Kotowski:** Dzień dobry tu złożę wniosek i tam opłacę to i tam staram się fizycznie załatwić ten.

**Przemysław Sołdacki:** No już się tam rozliczysz tam nie dasz info do Justyny, Justyna ci ogarnie. Po prostu, bo ten jesteś na bi bi.

**Adrian Kotowski:** Tak, tak.

**Przemysław Sołdacki:** No to doliczyć do faktury i tyle. Ma tematu.

**Adrian Kotowski:** No tak, tak jak jest w wieku Szafir brałem mieć to mogę tam mógł złożyć też jako jedyny wniosek.

**Przemysław Sołdacki:** Ją dokładnie. Wiecie bo szkoda sobie doda. Dodatkowy nakład pracy tylko po to, żeby oszczędzić 200 zł. No to lepiej wydać jej, żeby się mógł szybciej pracować.

**Adrian Kotowski:** I to jest wreszcie przetestować sytuacji na przykład, że mamy na przykład 2 te certyfikaty. Zawód PC podpięty do komputera i żeby zobaczyć jakimi się wtedy aplikacja zachowało też w sumie jest to kilka jest.

**Przemysław Sołdacki:** Ale to możesz iść 3 kupić i nie ma problemu i sobie testuj wszystko. To nie są, nie są pieniądze, nad którymi warto by się było zastanawiać, tak powiem.

**Adrian Kotowski:** No ten wraz. No dobra, okej, jasne.

**Damian Kaminski:** No dobrze, to to już sobie Adrian załatwi pytanie, czy został on jeszcze kilka minut, czy ktoś jeszcze chciałby coś poruszyć? Coś mi się przypomniało, to warto było czym warto by było się podzielić. No dobrze, to rozumiem, że możemy nad tym skończyć. Czy to Janusz też jeszcze coś dopowiedzieć na koniec?

**Janusz Bossak:** A wszystko było poruszone. Planujemy kolejny sprint, planujemy roadmapę na następny rok. Dużo roboty. Dobra, dzięki bardzo, bardzo fajne, fajna prezentacja. Rzeczy się udało zrobić, jedziemy dalej, majcie się na razie.

**Kamil Dubaniowski:** Dzięki.

**Damian Kaminski:** Cześć.

**Marek Dziakowski:** Cześć.

**Filip Liwiński:** Dzięki, cześć.

**Oktawia Ostrowska:** Dzięki, cześć.

**Mariusz Piotrzkowski:** Cześć.


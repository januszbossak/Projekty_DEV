**Data spotkania:** 30 listopada 2025, 11:33

---

**Damian Kaminski:** Dobrze, to może tak bardziej wysokopoziomowo, bez wchodzenia w szczegóły. W kontekście WIM mocno ucięliśmy. Ja zaprezentowałem WIM, że będzie ucięcie, bo wcześniej wysłałem im prototyp, który przygotowałem na Figmie. On się spodobał, więc nie chciałem, żeby doszło do takiej sytuacji, że jak wyślę im maila, że teraz proponujemy takie rozwiązanie, to żeby nie poczuli jakiegoś dysonansu, że wczoraj rozmawialiśmy o tym, a dzisiaj mówimy, że już zupełnie inaczej do tego podchodzimy. Pan Piotr miał dobry humor, więc wybrał to trochę w żart, że on ma karty, bo zaraz trzeba będzie negocjować nową umowę serwisową. Coś tam może jeszcze da się ugrać i że termin też tutaj może niekoniecznie jest aż tak wiążący. Tak zrozumiałem, że może MVP na początek, a potem coś więcej. Niemniej, jest to opisane. Trzeba to teraz przełożyć na zadania na backlogu. Pozostaje tylko im to wysłać. Pytanie, czy mam to? Przygotowałem, omówiłem to wstępnie z Januszem, z Piotrem. Ostatecznie nikt tego jeszcze nie czytał poza mną. Plik jest dostępny. Pytanie, czy ktoś z was przed wysyłką do WIM chce to przejrzeć, bo zakładam, że będzie z tego konieczne spotkanie. Pan Piotr nie powie: "Okej, spoko, nie ma problemu, to zacznijcie połowę i zróbcie nam połowę".

**Przemysław Sołdacki:** Powiedz mi, czy to, co masz teraz, to już jest okrojone i w półtora miesiąca do zaimplementowania?

**Damian Kaminski:** Mocno to okroiliśmy. Myślę, że nie wiem, co ty, Piotrze, sądzisz na ten temat? Czy masz do tego obiekcje, że to nie da się tego zrobić? Powiem tak, Filip to już to, co mamy praktycznie do zrobienia po stronie backendu, to frontendowo praktycznie. Pewnie, jak powiemy, że 80%, a może więcej jest pokryte, to tak jest. Ale tutaj backend jest głównym wyzwaniem.

**Piotr Buczkowski:** Tak, podpięcie to doprowadza do celu, zajmie.

**Damian Kaminski:** Tak, tak, tak. To jest na razie w formie MVP. Wracając do tego, co Przemku zasugerowałeś w tym spotkaniu globalnie, żeby spojrzeć na to wysokopoziomowo, mamy podejście takie, że zrobimy to tak jak komunikator, odrębną aplikacją wpiętą w AMODIT. Dzięki czemu korzystamy przy wytwarzaniu jej z AI, bez ryzyka, że AI napsuje nam AMODIT.

**Przemysław Sołdacki:** To jest okej.

**Piotr Buczkowski:** AI może sobie robić po swojemu, nie musi się trzymać zasad AMODIT.

**Przemysław Sołdacki:** To wyglądało podobnie. Do AMODIT. Frontendowo nie mam uwag, może tak być. Backendowo nie chcę, żebyśmy mieli zupełnie oddzielną strukturę i miękkich wiązań, ale tak jak rozmawialiśmy, że.

**Piotr Buczkowski:** Tak będzie.

**Przemysław Sołdacki:** Rozumiem, że jakieś nowe struktury danych mogą powstać, ale to musi być.

**Piotr Buczkowski:** Będzie poza monitorem całkowicie.

**Przemysław Sołdacki:** W tę stronę chcecie iść?

**Damian Kaminski:** Będzie to osadzone w AMODIT.

**Piotr Buczkowski:** Jeśli tak mamy to robić, to tak. Nie. Będzie tylko strona widoczna jako zewnętrzna aplikacja.

**Damian Kaminski:** Dokładnie. Ale to nie będzie tak, że jakiś inny adres, tylko to będzie tak jak komunikator. Po prostu będzie zakładka, która będzie wywoływać w ramach AMODIT odrębną aplikację.

**Przemysław Sołdacki:** Tylko komunikator to jest coś, czego w ogóle nie było. To jest zupełnie inna bajka. Tam chyba jakieś powiązania są, bo grupy się ściąga użytkowników. Można kogoś wywołać. Nie wiem, czy sprawę można wywołać w komunikatorze.

**Damian Kaminski:** Na razie nie można.

**Przemysław Sołdacki:** Nie można. To jest taki mocno standalone. To jest okej. Tam tylko parę rzeczy sięgamy. Natomiast tutaj jest kwestia, czy w tym repozytorium to jest oddzielna struktura na przechowywanie plików? Jest zupełnie. To nie ma żadnego związku z procesami i tak dalej. Czy to jednak jest tak, że taki dokument to jest de facto sprawa z załączonym dokumentem?

**Damian Kaminski:** Nie, nie, nie. Nie mówimy o repozytorium plików.

**Piotr Buczkowski:** Jest całkowicie odrębne.

**Przemysław Sołdacki:** Powiedzcie, czy w takim razie jak się będzie definiowało metadane opisujące dokument?

**Piotr Buczkowski:** Nie będzie się definiowało.

**Przemysław Sołdacki:** Czyli po prostu dokumentu.

**Piotr Buczkowski:** Było takie wymaganie.

**Damian Kaminski:** Nie było. Nie było doprecyzowane, o tak, może to nazwę. Było o to pyta.

**Piotr Buczkowski:** Jeśli coś mieliśmy, to dane opisujące dokument, to niech sobie sprawdzi.

**Przemysław Sołdacki:** Co?

**Piotr Buczkowski:** Niech robią sprawy.

**Przemysław Sołdacki:** Jeśli by się okazało, że te metadane muszą być, to bez sensu robić drugi edytor metadanych. Już jeden.

**Piotr Buczkowski:** Ale to pewnie wtedy nic nie robimy.

**Przemysław Sołdacki:** Robimy jedną rzecz: interfejs, który ułatwia dostęp do tych dokumentów. Nie tak, że wchodzisz z prawej, masz dokument, tylko w drugą stronę. Masz dokument, a do tego, jak trzeba, to ściągamy dane sprawy.

**Piotr Buczkowski:** Musimy się zdecydować, co chcemy robić.

**Przemysław Sołdacki:** To jest pytanie i to do Damiana.

**Damian Kaminski:** Słuchajcie.

**Piotr Buczkowski:** Czy rozumiem, czy robimy repozytorium, gdzie rzucamy pliki?

**Damian Kaminski:** Tak, to jest naszym celem.

**Piotr Buczkowski:** Czy dostosujemy wyświetlanie spraw do. Inaczej by się tam sprawy.

**Damian Kaminski:** Nie mówimy o repozytorium plików, a nie spraw. Repozytorium spraw mamy.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** Poczekajcie jeszcze chwilę. Może te wytyczne?

**Przemysław Sołdacki:** Rozumiem, że plik albo jest w procesie i to nie ma związku z repozytorium, albo jest w repozytorium, nie ma to związku z procesem. Okej. Natomiast, jeśli byśmy chcieli implementować, że mamy plik, ale są metadane, to żebyśmy nie wymyślali nowych edytorów. Moglibyśmy robić tak, że jest specjalny proces nazywający się "repozytorium", który nie jest widoczny normalnie jako proces, tylko po to, że tam jest jeden.

**Piotr Buczkowski:** To po co robimy repozytorium?

**Damian Kaminski:** Czekajcie, ale co to znaczy metadane? Poczekajcie, co rozumiecie pod pojęciem "metadane"? Metadane można bardzo mocno uprościć do.

**Przemysław Sołdacki:** Nie byłem na żadnym spotkaniu, to się nie wypowiem.

**Damian Kaminski:** Trzech typów metadanych: nazwa pliku (techniczna i nazwa pliku w systemie, jak go sobie nazywamy), opis (to jest druga metoda) i trzecia to jest zbiór metadanych typu tagi. Po tych trzech parametrach możemy wyszukać, co chcemy. To jesteśmy w stanie wdrożyć w ramach tej aplikacji. Tyle. Nie ma innych meta tagów. Jeśli chcemy metadane zaawansowane, to robimy sprawy z załącznikami.

**Przemysław Sołdacki:** Jeśli to wystarcza, to jest okej. Być może w WIM to wystarcza. Martwię się o taki przypadek, jak ktoś powie: "Ja bym chciał tu jeszcze sobie opisywać nie tylko tymi tagami, ale jeszcze na przykład ze słownika coś wybierać, a tu jeszcze bym chciał jakieś pole liczbowe".

**Damian Kaminski:** To też to, co wymieniłem.

**Piotr Buczkowski:** To rób sobie sprawy.

**Przemysław Sołdacki:** Jeśli to rozwiązuje problem w WIM i docelowo chcemy się trzymać tej struktury, to spoko. To jest okej, bo wtedy rozumiem, że i te nasze moduły raportowe nie potrafią się dostawać do repozytoriów. To w ogóle nie ma związku. Jest sobie oddzielna struktura. Najwyżej mamy wspólnych użytkowników. Uprawnienia grup, czy cokolwiek.

**Damian Kaminski:** Ty, Przemku, widziałeś ten projekt?

**Piotr Buczkowski:** To jest tak jak SharePoint.

**Przemysław Sołdacki:** Nie, nie widziałem. Nie widziałem. Wiecie, bo ja też nie chcę decydować o tym, co jest dla mnie ważne.

**Damian Kaminski:** Dobra. Nie chodzi o to, żebyś decydował, tylko żeby wyobrazić sobie, co my chcemy zrobić, bo może właśnie tu następuje jakieś nieporozumienie na poziomie tego, jak my to chcemy zaopiekować. Ja tylko szybciutko pokażę, że to nie ma być związane z żadnymi raportami.

**Janusz Bossak:** Murawski to widział, tak, to, co pokazujesz.

**Damian Kaminski:** Murawski to widział i powiedział: "Super, tu to nie działa, to nie działa". Mówię: "Okej, ze wszystkim się zgadzam". Nic nie wymyślił nowego, tylko powiedział to to, że tak powiem, nie jest obsadzone w MVP, ale oczywiście jest przewidziane, że to tak by działało. Nie zaskoczył mnie niczym. Powiedział, że jest super i nie powiedział nic o metadanych, mimo że tu ich nie ma. Już pokazuje sekundkę.

**Przemysław Sołdacki:** Może w pewnym momencie się okaże, że jednak są potrzebne. Ale ja może wam powiem biznesowo, jak ja to widzę. Po pierwsze, chcę to domknąć, ten projekt, żeby on to odebrał, żebyśmy się nie napracowali za dużo. Musimy to w grudniu odebrać, czyli musimy mu przed początkiem grudnia to dać, żeby on przed świętami to przetestował i to odebrał, bo w momencie, kiedy on odbierze, okaże się, że są nowe rzeczy. Będziemy negocjować nową umowę serwisową i w ramach umowy serwisowej.

**Damian Kaminski:** Raduje.

**Przemysław Sołdacki:** Trzeba przewidzieć godzinę na dalszy rozwój. W tym ma być może rozwój tego repozytorium. Tyle. Jeśli tak to zrobimy, to jest okej. Drugi aspekt biznesowy, że jeśli to robimy repozytorium, my byśmy może chcieli je sprzedać innym klientom. Byłoby takie w miarę uniwersalne. Ale tak jak mówicie, może takie, że jak klient chce bardziej wyrafinowane rzeczy, to niech sobie robi proces, a jak chce proste rzeczy, to niech użyje repozytorium. I to jest okej. Dobra, coś widzę, tylko muszę sobie powiększyć.

**Damian Kaminski:** Już powiększam. Mogę to dać, jak sobie chcesz poklikać.

**Przemysław Sołdacki:** Słuchaj, ja nie chcę za was tego robić, bo mam dużo innych rzeczy, typu strategia sprzedażowa do zrobienia.

**Damian Kaminski:** Nie, tak. Nie chodzi o to, żebyś dawał tu wytyczne, bo one już zebrane. Klient je zaakceptował. Mu się to spodobało. Po prostu mówił, że miał na to czas. Na początku myślałem, że to sarkazm. Będziemy rozmawiać teraz przez godzinę, bo to było wczoraj to spotkania. Rozmawialiśmy 5 minut na ten temat. Powiedział, że mamy tu sobie poziom uprawnień i tu, na przykład, gdzieś tam na poziomie niżej. Nie widać, że te uprawnienia są dziedziczone, co oczywiście musi być wynikową. Tutaj aktualne uprawnienia powinno być z góry.

**Przemysław Sołdacki:** Tak, tak.

**Damian Kaminski:** Upraszczamy filler. Po 5 minutach powiedział, że nie mamy o czym dyskutować. Wszystko jest fajnie, tylko to jest coś, co jest pełnofunkcjonalne, powiedzmy, w zakresie tego, co oni potrzebowali. Jak takie repozytorium powinno działać, czyli z liczeniem uprawnień, możliwością ich zrywania i tak dalej. Ustawiają na dowolnym poziomie folderów lub też plików. My to upraszczamy do tego stopnia, że przynajmniej on tego nie widział. Przynajmniej w naszych założeniach, że tylko najwyższy poziom, który roboczo nazywam przestrzenią repozytorium, żeby odróżnić to do obszaru, który korzystamy w ramach menu. Tu stawiamy uprawnienia, i one dziedziczone są w dół. To jest nasze, powiedzmy, zmniejszenie zakresu. Nie ma zrywania.

**Przemysław Sołdacki:** Nie można na tych gałęziach niższych sobie na podfolderach zmieniać uprawnień.

**Damian Kaminski:** Tak, ale można robić.

**Przemysław Sołdacki:** Nie wiem, czy on to łyknie. Ale być może jest jeden z dwóch wariantów: albo jemu to wisi, jak to działa, bo oni tak mają jakieś repozytoria, mają tylko się czepił dla czepiania, żeby nas przeczołgać, albo jest tak, że chcą zniwelować coś w swoim repozytorium. I wtedy już może powiedzieć, że sorry, ale te uprawnienia muszą być. To też jest inna sprawa. Jakby on to odebrał, to później mogę zamówić u nas projekt migracji danych i wtedy jak będzie migrować, to mu uprawnienia doprogramujemy. Tak czy inaczej odbierzmy ten projekt, bo dopóki nie mamy odebranego projektu, to on nie kupi nic nowego. Będzie problem z serwisowaniem. Zamkniemy projekt, to będziemy mogli to rozbudowywać jeszcze przez 5 lat, więc zgadzam się.

**Damian Kaminski:** Tak, tylko to nie jest jedyny element tego projektu.

**Przemysław Sołdacki:** Tak, ale jeden z kilku.

**Damian Kaminski:** Powiem tak, ja mogę wysłać te założenia, które mamy. Tego na pewno to jest 100% pewności, że on to podważy i będzie chciał wyjaśnić, czemu tak i tak dalej. Tu pewnie potrzebowałbym wsparcia, żeby w jakiś negocjacjach docelowo jak to będzie zaopiekowane. Natomiast ja rozpiszę to, co my ustaliliśmy jako MVP. Muszę się skupić tu z Mateuszem nad samym procesem faktur, bo on jest jeszcze nie zrobiony.

**Przemysław Sołdacki:** To są dwie różne rzeczy. Ten proces faktur trzeba dowieźć, żeby mu wszystko działało. Natomiast, jeśli da się zrobić bez tych bardziej skomplikowanych uprawnień, to super. Pytanie, o ile więcej pracy, żeby zrobić te uprawnienia dla folderów.

**Damian Kaminski:** Jeszcze też braki, więc to.

**Przemysław Sołdacki:** Czy to jest trudne, łatwe? Tyle. Ale zróbmy to MVP. Być może on powie, że muszą być uprawnienia, więc nie wiem, czy to dużo więcej pracy. Biorąc pod uwagę, że robimy apkę od zera.

**Damian Kaminski:** Podejdźmy tak, że dokładnie zróbmy MVP. To nie będzie zamykać możliwości rozwoju. Zobaczymy, gdzie będziemy: czy to będzie 20 listopada, 20 grudnia, czy 20 stycznia. Ja dzisiaj nie wiem. Dopiero jak to zrobimy, to możemy powiedzieć: "Dobra, mamy jeszcze chwilę, dołożymy coś", albo "Nie mamy inne priorytety, a klient się zgodził, że dowieziemy to później, albo w ogóle tego nie zrobimy".

**Przemysław Sołdacki:** Dobra, to wiesz co? Przeszliśmy te założenia. Co w tym uprawnieniu łyknie, to łyknie. Jeśli nie, to najwyżej będzie trzeba to robić, albo się z nim jakoś dogadamy. Miał dobry humor, może pewnego dnia mieć gorszy humor i przypiecze się i nie podpisze protokołu. Ale dobra, rozumiem założenie: robimy oddzielne struktury w bazie. W tej samej bazie, tak. Robimy oddzielną aplikację, którą wsadzamy. Koniec. Rozwijamy ją przy użyciu AI.

**Damian Kaminski:** Nie wiem, czy w tej samej bazie. Nie wiem, tu chyba w oddzielnej bazie. Tak rozumiałem. Ale nie wiem, to Piotr niech ewentualnie da tutaj wytyczne.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** Czy to jest?

**Janusz Bossak:** Komunikator ma.

**Damian Kaminski:** Oddzielny.

**Janusz Bossak:** Komunikator ten, co Mateusz.

**Przemysław Sołdacki:** Komunikator miał być w oddzielnej, ale zrobiliśmy w tej samej.

**Piotr Buczkowski:** Nie pójdziemy.

**Przemysław Sołdacki:** Co tu będziemy? Jeśli to być może odpalali, to będę miał dwa razy więcej baz danych.

**Piotr Buczkowski:** Nie, nie będzie odpalany na chmurze.

**Przemysław Sołdacki:** Jak nie będzie, jak będzie klient jest w chmurze, to jak mogą?

**Damian Kaminski:** Przemek chce to spieniężyć.

**Przemysław Sołdacki:** Tak.

**Piotr Buczkowski:** Jak ktoś będzie chciał, to będzie mu się tworzyło oddzielną bazę danych.

**Przemysław Sołdacki:** Łukasz postawił kropkę. Miał dwa razy więcej baz do zarządzania.

**Piotr Buczkowski:** Nie będzie miał kilka razy więcej.

**Przemysław Sołdacki:** Tyle, ile klientów by chciało z tego korzystać.

**Piotr Buczkowski:** Tak.

**Przemysław Sołdacki:** Na bazie demo ma być komunikator. Przy każdej bazie demo będziemy teraz dwie bazy tworzyć.

**Piotr Buczkowski:** To nie będzie na demo.

**Damian Kaminski:** Co do?

**Przemysław Sołdacki:** Jak nie będzie, jak chcemy to, żeby było.

**Piotr Buczkowski:** Pół roku na zrobienie. Pół roku na zrobienie tego porządnie, żeby to było częściowo, a nie na łapu-capu.

**Przemysław Sołdacki:** Dlaczego mamy na bazie demo nie dawać? Piotrek, skoro to jest kilka tabelek, zakładam, które obsługują komunikator. Dlaczego mają nie być w tej samej bazie?

**Piotr Buczkowski:** Może to, co jest zrobione w tym, może popsuć resztę bazy AMODIT.

**Damian Kaminski:** Tylko.

**Przemysław Sołdacki:** Jeśli to są oddzielne tabelki, to.

**Piotr Buczkowski:** Nie wiem, jak to będzie zrobione. Nie będzie testowane. Ma być na szybko zrobione. Nie chcą obciążać bazy AMODIT takim czymś.

**Damian Kaminski:** Przemek co do.

**Przemysław Sołdacki:** Słuchajcie, przygotujcie się na to, że będzie takie zagadnienie migrowania tych pobocznych baz, typu komunikator i repozytorium do głównej bazy AMODIT. To na pewno nastąpi.

**Piotr Buczkowski:** To będzie, nie wiem, dwa, trzy miesiące na to czasu, i zrobimy to.

**Przemysław Sołdacki:** Na przeniesienie tabel. No i bazy.

**Piotr Buczkowski:** Na zrobienie tego tak, żeby to pasowało do AMODIT, a nie po prostu na szybko przemocy. AI czy przy pomocy czegokolwiek.

**Przemysław Sołdacki:** Raczej nie rozumiem tego. Jeśli mam oddzielną bazę i tam, załóżmy, mam pięć, dziesięć tabel, i mówię: "Dobra, to te tabele będą tylko w innej bazie i będę się łączył do tej bazy". Te tabelki nie mają nic wspólnego z wszystkimi innymi tabelkami. Co tam może się popsuć?

**Piotr Buczkowski:** Może być obciążona baza danych. Przeciążona, bo zadał na przeciążone pliki.

**Przemysław Sołdacki:** To może być. Absolutnie. Dobra, już, tak jak mówisz.

**Damian Kaminski:** Szybko, Przemek, co do dem. Według mnie do dem powinniśmy podejść do tego w ten sposób: jak małe ZD. Jest jedno demo publiczne, gdzie są te funkcjonalności właśnie typu dodatkowe, wymagające dodatkowych konfiguracji? Jak ktoś chce zobaczyć, tylko jak to działa, żeby tylko tego dotknąć. Tak jak tu jest jedno demo, w każdej godzinie parzystej się resetuje. Każdy może się zalogować, tu są podane loginy. Tak wygląda z DI. To nam mega dużo uprości, bo ci klienci proszą o to, my to generujemy, utrzymujemy, a potem ktoś się tam nie loguje, ani razu, albo loguje raz na 5 minut i mówi: "Jak mi nie wytłumaczą, to nie zrobią instrukcji, to ja tu nic nie zrobię".

**Przemysław Sołdacki:** Damian, słuchaj, po to tam mamy automatyczną dokumentację. To jakby oddzielna dyskusja.

**Damian Kaminski:** Piotr, u ciebie jest straszne zamieszanie.

**Piotr Buczkowski:** Przechodzili obok koncertu w sali konferencyjnej.

**Przemysław Sołdacki:** Okej. Dobra. Ja nie chciałbym przypadkowo na tym spotkaniu zmieniać założenia, jak działa nam sprzedaż i bazy demo. Wróćmy do meritum, bo w ogóle spotkanie dotyczy czego innego. Procesów. Dyskutujemy o czym innym.

**Damian Kaminski:** Po prostu.

**Przemysław Sołdacki:** Podsumowując, zróbmy komunikator. Zróbmy do końca, niech WIM odbierze ten. Zrób MVP do repozytorium. Może być oddzielna aplikacja z oddzielną bazą danych. Tylko żeby dało się kliknąć wewnątrz AMODIT. Nie wiem, podpiąć tam do menu i tyle. Później będziemy robić z tym porządek. Aplikacja jest w całości zrobiona w AI. Ma działać. Może się okaże, że działa dobrze. Docelowo podejrzewam, że wszystko i tak przeniesiemy do projektu AMODIT. Bierzcie to gdzieś tam pod uwagę, że tak pewnie będzie trzeba zrobić. Janusz chce mieć komunikator Astrafoxie.

**Damian Kaminski:** Tak.

**Przemysław Sołdacki:** To może go od razu tam uruchomić u nas, tylko to będzie podwajało nam liczbę baz na serwerze. Dobra, słuchajcie, a co w temacie naszego edytora procesu?

**Damian Kaminski:** Przemku, ty się możesz wypowiedzieć. Coś robiłeś w ostatnim czasie?

**Przemysław Rogaś:** Z takich nowości to nie, głównie usprawnienia.

**Damian Kaminski:** Dobra, to może pokaż to, żebyśmy to.

**Przemysław Sołdacki:** Co to znaczy usprawnienia?

**Przemysław Rogaś:** W sekundę. Z takich rzeczy, to teraz ostatnim zadaniem, mieliśmy przy odnośniku. Teraz dodając odnośnik do źródła zewnętrznego, musi mieć moim źródło danych i pełne, żeby dodać. Filtruj. Jestem. Może tutaj jeszcze było?

**Przemysław Sołdacki:** Zauważyłem, że tam pojawiło się, że nie muszę najpierw robić wiersza, żeby dodać pole. Tak się od razu dodaje.

**Przemysław Rogaś:** Tak, tak.

**Przemysław Sołdacki:** To jest spoko. A jak chcę usunąć, właśnie znajdź, żebym chciał wierszy usunąć.

**Przemysław Rogaś:** Wiersza ogólnie nie usuniesz, o ile nie jest pusty.

**Przemysław Sołdacki:** Okej. Bardzo dobrze. A jeszcze pytanie, bo tam pisałem, że jak mi zbrakło kolumn w bazie, to po prostu nic się nie stało, bez żadnego komunikatu. Rozumiem, że tam dodamy, żeby był jakiś komunikat.

**Przemysław Rogaś:** Tak, trzeba obsłużyć i te ustawienia odnośnie tam ilości pól na formularzu też.

**Przemysław Sołdacki:** Tak.

**Przemysław Rogaś:** Chyba trzeba zaaplikować do poprzedniej wersji też, bo to jest robione to Piotr, że będę dawał.

**Przemysław Sołdacki:** Może być do następnej wersji. Ważne, że to jest zrobione. Jak jest zrobione, to ja już nie mam więcej pytań.

**Damian Kaminski:** To na poziomie samych ustawień, nie, że w bazie danych zabrakło, tylko że limit jest przekroczony.

**Przemysław Sołdacki:** Limit jest przekroczony, ale nic nie powiedziało. Ani błąd nie wyskoczył. Po prostu się nie dodało pole, i nie wiedziałem, czy wstało. Chodzi o to, żeby się pojawił komunikat, żeby on coś mówił, a nie "Skontaktuj się z administratorem". Tylko "Przekroczony limit pól, żeby zmienić limit pól, kliknij tutaj". Jak jest adminem, to już mógł wejść i sobie poprawić.

**Damian Kaminski:** Tak, tak, tak. Chodzi mi tylko o to. Ty, Przemku, przygotujesz do tego opis backendowy, do tego wymagania?

**Przemysław Rogaś:** W sensie, jakieś zadanko bym wrzucił i dla siebie.

**Damian Kaminski:** Okej. W sensie, przygotujesz to we własnym zakresie, czy potrzebujesz, żeby ci to przygotować?

**Przemysław Rogaś:** Przygotuję. Co tu jeszcze? Ikonki się zmieniły, takie drobne rzeczy. Wszystkie są teraz outline. Te optymalizacje do pobierania użytkowników, słowników.

**Przemysław Sołdacki:** Okej.

**Przemysław Rogaś:** Teraz po prostu, w czym były pobierane wszystkie. Piotr zgłasza, żeby to ograniczyć. Teraz pokazuje się 50, tylko. Wyszukać. Jak chce się, znajdziemy więcej.

**Przemysław Sołdacki:** Pięćdziesiątych to i tak dużo. Mogło być równie dobrze 20.

**Przemysław Rogaś:** To też.

**Przemysław Sołdacki:** Okej. Niech będzie 50.

**Przemysław Rogaś:** Jest, no i to się teraz pobiera dopiero po kliknięciu. To akurat jest schowany. Od razu się pokazuje. Edycja słowników. Trochę teraz jest bardziej przyjaźnie. Wcześniej trzeba było kliknąć tutaj obok, że chcę edytować. Wtedy nam się model odpowiadał. Teraz po prostu zmieniamy. Teraz nam się wyskoczy model z akceptacją ryzyka. Trzeba akceptować. Taki przycisk został dodany, żeby przejść do słownika. To samo było dla odnośnika.

**Piotr Buczkowski:** Da się tutaj szukać? Wróć, wróć.

**Przemysław Rogaś:** Nie, nie da się.

**Piotr Buczkowski:** Nie da się?

**Przemysław Rogaś:** Nie, nie. Powinno. Masz rację, że powinno się dać znaleźć.

**Piotr Buczkowski:** Do czego się nie da?

**Przemysław Rogaś:** Szukać.

**Piotr Buczkowski:** Zgłaszałem to jakiś czas temu.

**Janusz Bossak:** Powinno dawać się faktycznie.

**Piotr Buczkowski:** Słowniki. Tego się nie da.

**Przemysław Sołdacki:** To trzeba zrobić, żeby się dało. Dobra, pytałem, bo to są też różne poprawki do edytora. Czy uwzględniliście jakieś sugestie z działu wdrożeń, z działu SA?

**Damian Kaminski:** Te poprawki też wynikają właśnie z tych sugestii.

**Przemysław Sołdacki:** Okej. Dobra, czyli to już idzie w tę stronę, bo też trzeba zaplanować w roadmapie, jakie jeszcze rzeczy, bo może jakieś grubsze rzeczy będą chcieli, więc warto zrobić.

**Janusz Bossak:** W obszarze to jest zbiorcze edytowanie, czyli na przykład klikam jednocześnie na użytkownik 2 i odnośnik jeden. I chcę, na przykład, dla nich ustawić coś wspólnego, typu ustawienia.

**Przemysław Sołdacki:** Tak.

**Damian Kaminski:** Uprawnienia tak masz na myśli, ale to mamy matrycę uprawnień.

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** Tak.

**Janusz Bossak:** Albo chcemy.

**Przemysław Sołdacki:** Pamiętam dyskusję z Kamilem, gdzie Kamil mówi, że skoro jedyną rzeczą to są uprawnienia, to można to z poziomu matrycy robić.

**Janusz Bossak:** Nie, ale mogę chcieć te trzy, na przykład, użytkownik, odnośnik i słownik, jednocześnie przenieść do innej sekcji. Teraz będę musiał robić trzy ruchy, każdego przenieść. W starym mieliśmy tak. Rzeczywiście, to przyznaję.

**Przemysław Sołdacki:** Co? To jakby wariantem można, oczywiście, narzekać tych checkboxów, ale to będzie brzydko. To, co się w wielu systemach robi, że jak trzymam kontrolę, to mogę zaznaczyć kilka.

**Damian Kaminski:** Czy to powinno być na pewno na graficznym, czy to nie powinny być takie masowe działania jednak na liście?

**Przemysław Sołdacki:** Na liście. A kliknij listę.

**Janusz Bossak:** Dlaczego by nie na graficznym? Skoro z tej.

**Przemysław Rogaś:** Tutaj.

**Przemysław Sołdacki:** Właśnie, bo tutaj mamy checkbox. W nowej wersji też powinien być.

**Damian Kaminski:** Janusz, jak zaznaczysz pięć pól, czyli pięć wierszy, to to będzie de facto cały twój ekran roboczy, który widzisz i też to przesuwać pod jakieś inne pole.

**Janusz Bossak:** Weź zaznacz. Kliknij u góry. Przejdź do sekcji. Tę funkcjonalność trzeba zrobić.

**Damian Kaminski:** Czy one nie wystarczą na liście?

**Przemysław Sołdacki:** Moim zdaniem, w ramach MVP, zróbmy to na liście. Daniel zresztą twierdzi, że dla niego jest lista ważniejsza niż edytor graficzny. Okej. Nie kłóćmy się z naszym wewnętrznym klientem. Może wdrożenia są bardziej potrzebne, więc pewnie na liście wystarczy. Nie musi być w dwóch miejscach. Jak ktoś wie, że chce hurtowo, to.

**Damian Kaminski:** Jak to wtedy Janusz, widzisz, że przejdźmy na litograficznym, że klikam na jedno pole z kontrolerem, klikam, powiedzmy, na drugie. Wtedy prawy side bar zmienia zupełnie swój kontekst. Właśnie na potrzeby tego, że mam dwa pola. Tu mam przenieść do sekcji. Tak, tę opcję.

**Janusz Bossak:** Tak. Przykład masz z prawej strony listę sekcji. Trzeba wymyśleć. Nie mam jeszcze na to.

**Przemysław Sołdacki:** Można by zrobić tak, że na tej liście, na widoku listy, albo są checkbox, albo z kontrolą zaznaczam i wtedy przez drag & drop przesuwam, zmieniając kolejność wewnątrz sekcji, albo przenoszę do innej sekcji przez drag & drop. Będzie jakiś help, albo nauczymy konsultantów, że tak się robi, i będą sobie radzili szybko. Dana rzecz ma się dać zrobić. Nie musi we wszystkich miejscach być. Może być w jednym miejscu.

**Damian Kaminski:** Mam jeszcze doświadczenia. Mam jeszcze doświadczenia z WordPress. Muszę się przełączać za chwilę. Mogę wam wrzucić co najwyżej jakieś demo, bo w WordPressie jest tak, że z prawej strony można sobie wyświetlić drzewko organizacji formularza. Tam mielibyśmy podzielone sekcje, pola. Wtedy daną sekcję, albo dane pole w ramach drzewka, czyli same nazwy, można przesuwać sprawnie.

**Przemysław Sołdacki:** Można tak zrobić, albo zrobić na liście to samo. Zaznaczasz kilka, przeciągasz, i tyle.

**Janusz Bossak:** Listę i tak pewnie zostawimy, bo z różnych innych powodów.

**Przemysław Sołdacki:** Zostawimy. Chyba już nawet mamy nową wersję tego zrobioną. Czy nie mamy? Zaprojektowaną na pewno mamy.

**Janusz Bossak:** Tak.

**Damian Kaminski:** Zaprojektowaną mam.

**Przemysław Sołdacki:** Tak. To i tak trzeba zrobić, więc nie musimy robić, że i w edytorze graficznym na liście. Zróbmy to, na przykład, tylko na liście, i to wystarczy. Kto będzie chciał hurtowo, to sobie wejdzie na listę. Dobra, rozumiem. Przemek, do ciebie pytanie, czy ty wiesz, co dalej masz robić?

**Przemysław Rogaś:** Na ten moment ja edycji procesu nie mam nic zaplanowane.

**Przemysław Sołdacki:** To spytaj Kamila, co tam dalej trzeba robić, i tyle. Janusz, swoją drogą, ta nasza organizacja, rozumiem, będzie bardziej szła w stronę Scruma i podzielenia zespołu i celów sprintu.

**Janusz Bossak:** Tak mieliśmy kiedyś. Teraz trzeba będzie to zrobić na nowo i bardziej.

**Przemysław Sołdacki:** Tak. Chodzi mi o to, że gdybyśmy mieli, na przykład, cel sprintu: dokończyć edytor formularza, to wtedy wiadomo, że ten zespół pracuje. Na przykład, jedna osoba nad listą, druga nad matrycą uprawnień. Kamil.

**Janusz Bossak:** Wiadomo. Jest za duża zmienność.

**Przemysław Sołdacki:** Tak. Chodzi o to, że porządkuje pracę. W takim sensie, że wtedy, na przykład, Przemek nie musi pytać Kamila, czy to, czy tamto, bo wie, że celem jest, żeby to wyszlifować i szlifuje.

**Janusz Bossak:** Połowę roadmapy wyrzucić i wtedy będziemy tak mogli pracować.

**Przemysław Sołdacki:** Zróbmy to. Ja wolę mieć po kolei, niż rozgrzebane dziesięć rzeczy naraz.

**Janusz Bossak:** Teraz jest trochę. Widać, to jest szarpanina. Mnie tu Przemka rzucimy na to, Filip na to, a nie z powrotem.

**Przemysław Sołdacki:** Realnie tak. Wiesz, że coś musi poczekać. Jakaś część zespołu musimy przewidzieć na takie rzeczy, bo klient chce, na przykład, i jest pilne, albo trzeba poprawkę zrobić. Mamy jeden czy dwa zespoły, gdzie celem sprintu jest dokończyć edytor procesów i nic innego nie robimy, aż mówimy: "Jest dokończony. Dziękuję". Same do tematu. Idziemy dalej. Wolę mieć na roadmapie mniej rzeczy i je dowieść, niż mieć dużo rzeczy i ich nie dowieść.

**Janusz Bossak:** Dokładnie.

**Przemysław Sołdacki:** Dobra. Tak po prostu.

**Janusz Bossak:** Dobra.

**Przemysław Sołdacki:** Przemek diagram też robiłeś? Ktoś inny robi?

**Przemysław Rogaś:** Ja robię diagram. Z tym że diagram już jest na takim etapie, że prace są skończone. Póki co będzie ten prawy pasek, ale to też jeszcze do ustalenia.

**Przemysław Sołdacki:** Dobra, to przedyskutujcie z Kamilem, bo wtedy ja będę wiedział, że to jest zrobione. Jest to ładne, super, bardzo mi się podoba. Brakuje funkcjonalności edycji. Prawego panelu brakuje.

**Janusz Bossak:** To jest też taki poziom, o który mi chodzi. Określania tych kolejnych poziomów MVP. W MVP jeden jest to. Jesteśmy zadowoleni. Mamy świadomość, że jest jeszcze coś.

**Przemysław Sołdacki:** Tak. Dokładnie tak.

**Janusz Bossak:** Postanawiamy.

**Przemysław Sołdacki:** Tak, ja też wolę, żeby na przykład cel sprintu czy pozycja na roadmapie: "Zrobienie diagramu bez prawego panelu". Później kolejny etap na roadmapie: "Zrobienie prawego panelu do diagramu". To jest dla mnie spoko, bo ja wiem, to jest domknięte.

**Janusz Bossak:** Dokładnie. Tak. Dokładnie to. Jeśli będziemy mieli ten podział na poszczególne MVP, będzie nam łatwiej rozmawiać, bo jak wpisujemy sobie na roadmapę "zrobienie diagramu", to każdy ma inny poziom wyobrażenia o tym, co zostanie zrobione.

**Przemysław Sołdacki:** Dokładnie. Taka rozdzielczość musi być na wasze dwutygodniowe sprinty. Już taka szczegółowa. Ja mogę mieć na kwartał, że w danym kwartale cały diagram, czy cały edytor procesów, zostanie zrobiony. Jak nie cały, to te rzeczy będą zrobione, a te rzeczy będą robione w kolejnym kwartale. To jest taki poziom dokładności. Nie potrzebuję, ale muszę wiedzieć, co zostaje domknięte. Nie, że robimy i tak jesteśmy może w 30 procentach, może w 70. Trudno powiedzieć. Po prostu zamykamy jedną rzecz. Mówimy: "Dobra, jest zamknięte. Stało się". Robimy następną. Ja na takim poziomie chciałbym tym zarządzać. Nie chciałbym wchodzić głębiej w szczegóły, bo pewnie za często wchodzę. Dobra, dzięki.

**Janusz Bossak:** Dobra. Dzięki bardzo.

**Przemysław Rogaś:** Na razie.

**Przemysław Sołdacki:** Zatrzymano transkrypcję.

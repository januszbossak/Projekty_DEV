**Data spotkania**: 8 września 2025

**Janusz Bossak**: To, żebym może już nie przedłużać czasu, mało... Już nie nasze podsumowanie projektu. Z tego co widzę, też sprint był bardzo tak nastawiony na poprawianie, dokończenie, dowożenie różnych rzeczy. Wciąż jakoś spektakularnie nic nowego. Ale też ważny, jeśli chodzi o właśnie jakość potem produktu, który dostarczamy. Dobrze Damian, może tobie oddam głos. Nie wiem, czy Kamil jest? Chyba Kamila jeszcze nie widzę, żeby się połączył. I przejdźmy te rzeczy, które były zrobione.

**Damian Kaminski**: Dobrze, no tak jak powiedziałeś, w czwartek już się trochę pochwaliliśmy. Sprint był głównie nastawiony na to, żeby stabilizować tą wersję, którą mamy wydać w tym tygodniu. Więc no właśnie, może nie ma takich rzeczy super nowych. Stabilizujemy jeszcze i poprawiamy komunikator. Tego nie wiem, czy mamy drugi raz pokazywać, bo w sumie w czwartek prezentowaliśmy. I ostatnio też. Pytanie, czy ktoś chciałby się czymś pochwalić, co zrobił ostatnio? Z was. Ja już przeglądam co tu ewentualnie...

**Janusz Bossak**: Z takich rzeczy, co pewnie nie były za bardzo pokazywane, ale nie wiem, czy już jesteśmy w takim stanie, żeby to pokazywać, to jest ta matryca uprawnień.

**Damian Kaminski**: Przemek... pytanie, czy to już, czy Przemek, czy Filip... Przepraszam, Filip. Czy to już możemy zaprezentować?

**Filip Liwiński**: Mogę zaprezentować, ale tam jeszcze nie ma niektórych rzeczy zaimplementowanych, ale cała logika jest zaimplementowana. Dobra, no to już udostępniam.

**Damian Kaminski**: To nic, proszę, pokaż to. Czyli zanim zaczniesz tu podpowiadać, to ja krótkie jeszcze wprowadzenie biznesowe. Chodzi o to, żeby był po prostu wygodniejszy sposób, globalny, tak jak widzimy, możliwe definiowanie uprawnień dla pól, no po to, żeby można było to w łatwy sposób po pierwsze i odczytać dla serwisu, i też definiować. No ten widok, który teraz widzimy, może na pierwszy rzut oka jest przytłaczający, natomiast jest dużo sprawniejszy w poruszaniu się dla osób, które no właśnie serwisują czy też konfigurują. Dobrze, proszę Filip, opowiedz, ja ewentualnie uzupełnię.

**Filip Liwiński**: Dobrze, to aktualnie żeby podejrzeć jakieś uprawnienia pola, trzeba wejść zarówno w zakładkę właśnie formularza, trzeba zaznaczyć dane pole, przejść do "edytuj uprawnienia" i dopiero tutaj mamy te wszystkie ustawione uprawnienia. Jest to dość nieintuicyjne, nie można tego jakby w szybszy sposób zobaczyć. Dlatego tutaj właśnie mamy tą matrycę, która też grupuje sekcję i pola. Na przykład pole "checkboxy", "sekcja test". Też minimalizować. Ale to jest to tabela i też pole w każdej tabeli jest w swojej sekcji. No i możemy zmieniać uprawnienia, na przykład w pole 1 mamy z sekcji, czyli z tej sekcji, czy edycja. Że to jest domyślnie, będzie jeszcze na wartość, będzie sekcja, to jakaś ikonka właśnie takiego dymka z typem, po którego najechaniu wyświetli się treść, z której sekcji jest to dokładnie dziedziczone. No i możemy zmieniać sobie te uprawnienia. I również to jest dla... są uwzględnione wyjątki dla użytkowników. Jeśli jakiś wyjątek jest stworzony, to domyślnie i kolor właśnie tutaj tego modela zmieniony na taki pomarańczowy. Było wiadomo, że coś jest właśnie zmieniane dla tego typu, tego pola. Możemy to sobie zmieniać, jak usuniemy, to wraca właśnie na szare po chwili. No i pokrótce to chyba tyle. No i też mamy tu właśnie ten check.

**Damian Kaminski**: Dobrze, no bardzo duża zmiana w kontekście... No dobrze, tu zewnętrzni, wewnętrzni to po prostu zmiana kontekstu.

**Piotr Buczkowski**: Nie. Z tej strony, dlaczego to nie są to ikonki?

**Damian Kaminski**: No właśnie też tutaj się nad tym zastanawiam, czy one nie powinny być jednak po lewej. To może jeszcze trzeba na designie omówić, bo to służy... no miałem to samo spostrzeżenie.

**Piotr Buczkowski**: Szukałem gdzie to jest, nie mogłem znaleźć, dopiero po chwili gdzieś rzuciłem okiem na prawą stronę.

**Damian Kaminski**: Tak, tak, tak. To może jeszcze warto się nad tym zastanowić.

**Kamil Dubaniowski**: Czy tak to... tak to rzuciłem ze względu na to, że no tego się używa bardzo sporadycznie i to zazwyczaj nasi konsultanci, żeby sobie sekcję techniczną dać tylko dla siebie, także no, dlatego ja też odpuściłem później tłumaczenie tych wyjątków, bo to jest tak zagmatwane, że szkoda na to czasu, może kiedyś.

**Damian Kaminski**: A możesz przescrollować w prawo? No właśnie, to znaczy, ale mimo wszystko ja bym Kamil... Tak na pierwszy rzut oka wydaje mi się, że gdyby to było przypięte do lewego menu, to by było bardziej intuicyjne niż tu, że to jest aż z prawej strony skrajnie. Dobra, słuchajcie, to jeszcze jest pierwszy rzut oka, więc sobie na tym jeszcze podyskutujemy. To znaczy warto zwrócić uwagę też, że tu mamy przegląd całego formularza, tak, co jest też olbrzymim usprawnieniem, bo można tutaj edytować tabelę, podtabele i tak dalej. No i co jeszcze jest planowany widok bardziej kompaktowy. Kamil, jakbyś mógł tu się wypowiedzieć?

**Kamil Dubaniowski**: Tak, będzie zmiana trybu na kompaktowy, gdzie tak naprawdę znikną te dopiski obok ikon, czyli zostaną same ikony ze względu na to, że czasami tych etapów jest naprawdę dużo. Jak ktoś już będzie na tyle obyty z tym widokiem, że będzie ogarniał sobie samymi ikonkami, to będzie mógł sobie przełączyć na tryb kompaktowy bez dopisku i będą same te oczka, ołówki, a z opisami przy najechaniu.

**Piotr Buczkowski**: Trzeba by ten widok uruchomić na jakimś procesie z SIT. Zobaczcie, jak to wygląda.

**Kamil Dubaniowski**: No dlatego mówię, że przy dużej ilości etapów...

**Piotr Buczkowski**: Tak, tak, tak, dla testów, tak, żeby zobaczyć skomplikowany formularz bardzo.

**Damian Kaminski**: No. Nie można wyeksportować, to nie problem pewnie, żeby wrzucić go tutaj. OK, czy coś jeszcze do tego widoku?

**Lukasz Bott**: Znaczy ja... czekajcie, ja bym tylko dodał, bo może tutaj dla nas jest oczywiste, ale też dla naszych gości, tak, Natalii, tam Mateusza, tak, że w kolumnach mamy nazwy etapów, tak? Czyli skrzyżowanie wiersza i kolumny to jest uprawnienie na danym etapie dla danego pola czy tam sekcji, tak? No to tam...

**Filip Liwiński**: Nie chyba.

**Lukasz Bott**: Trzeba to interpretować, no chyba tutaj jeszcze... ale rozumiem, że to co koledzy mówią, tak, to jest MVP. Czy tam te pierwsze wersje. Jakaś propozycja też pewnie powinno być filtrowanie etapów, tak, to żeby...

**Kamil Dubaniowski**: Czy działające, ale jeszcze nie zgodnie...

**Lukasz Bott**: No bo to już widzimy taki przykład skrajny, gdzie trzeba przewijać, trochę ginie od lewej do prawej.

**Janusz Bossak**: Tak, w projekcie jest taka opcja, żeby właśnie można było wybierać, które etapy chcemy wyświetlić. Bo nie zawsze wszystkie. Może pracujemy akurat nad początkiem procesu i potrzebujemy 3 pierwsze na przykład etapy. Albo pracujemy nad jakimś tam elementem, nie wiem, obsługi dekretacji, akceptacji i potrzebujemy kolejne tam jakieś 2 czy 3 etapy, żeby wyświetlić. No a w skrajnym wypadku możemy wyświetlić sobie wszystkie, tak, żeby prześledzić czy gdzieś tam czegoś nie zapomnieliśmy na którymś polu. W tej chwili żeby przejść taki duży proces i sprawdzić wszystkie uprawnienia, to najczęściej trzeba po prostu się przeklikiwać... trzeba się przeklikać przez wszystko. W tej chwili właśnie po to jest ta matryca, po to jest ona taka duża, żeby tak zwanym rzutem oka można było stwierdzić, czy wszystko jest OK, czy gdzieś tam nie została jakaś edycja albo coś innego, gdzie miało być coś ukryte na przykład.

**Damian Kaminski**: Dobrze, jak Filip jesteś przy głosie, jeszcze może pokażmy ten widok jobów. Tam chyba zakończone zostały prace już.

**Filip Liwiński**: No tylko jeszcze jedna poprawka została.

**Damian Kaminski**: Więc tak ostatecznie to wygląda. Jest ładnie tabelarycznie i widać tylko te joby, które są pracujące, tak domyślnie, plus mamy tutaj właśnie to już nowe rozwiązanie w postaci filtrowania i...

**Piotr Buczkowski**: Nie mówiłem wcześniej, czy jest przycisk "potwierdź status"?

**Filip Liwiński**: Nie ma.

**Piotr Buczkowski**: Badamy.

**Janusz Bossak**: Nie no jest, no. Znaczy całkowicie wszystkich, a w bycie pojedynczego.

**Damian Kaminski**: Ale nie uruchom, tylko odśwież. Janusz, Piotrowi chodzi o odśwież.

**Piotr Buczkowski**: Trzeba było zawsze odśwież. Bo często jest tak, że trzeba odświeżyć, tak, żeby zobaczyć czy wykonało. Nie chcę, żeby to było automatycznie, bo to szkoda czasu, ale...

**Damian Kaminski**: No dodajmy tutaj obok po prostu tak jak na raportach, w prawym górnym rogu.

**Piotr Buczkowski**: No tak, tak.

**Filip Liwiński**: Dobra.

**Piotr Buczkowski**: Po prostu odczytać status wszystkim postępem, wszystkie joby jeszcze raz, tak.

**Kamil Dubaniowski**: Filip, ikony nie wyskakują, te przyciski do akcji edycji i... a OK, dobra, dobra, jesteś na małym ekranie.

**Filip Liwiński**: Wyskakują, są.

**Damian Kaminski**: Wyskakują.

**Kamil Dubaniowski**: Czyli one wyskakują dopiero po najechaniu na kolumnę z nazwą.

**Filip Liwiński**: Tak.

**Kamil Dubaniowski**: To to bym jeszcze przemyślał, bo to była uwaga gdzieś tam po wstępnych... to jest tak już na tym prototypie moim na v0, nie pamiętam kto zgłaszał, ale badania, czy nie Janek Pijanowski, że intuicyjnie byłoby, że te akcje już widać jak w ogóle jesteś na wierszu. Każdy się domyśli, że trzeba jechać akurat na tą kolumnę.

**Janusz Bossak**: Tak, to prawda. No dobrze, co tam dalej mamy? Słuchajcie.

**Damian Kaminski**: Czy w ogóle w kontekście ustawień systemowych jeszcze coś możemy powiedzieć, jakieś nowości?

**Kamil Dubaniowski**: Jest Przemek, nie wiem Adrian, jak tam poszło w piątek jeszcze z tym tematem.

**Damian Kaminski**: Jest Przemek.

**Kamil Dubaniowski**: Integracji.

**Przemysław Rogaś**: No tam dużych nowości nie ma, tam walidacja, podpięty backend i walidacja dodana. No to pokażę jak to wygląda. Więc teraz dodając parametr, dodałem tutaj po prostu kategorie parametrów, czyli ogólne, endpoint albo inny. W przypadku ogólnych tutaj nazwa będzie... predefiniowane nazwy. Tam zgodnie z... wzięte są z dokumentacji. I tutaj w zależności od nazwy, na przykład jak mamy "password", no to będzie typ hasło. Jak jest na przykład tutaj typ autoryzacji, jak się... OK, istnieje. No to dobra, Authorization Type, no to jest wybór też ze zdefiniowanej listy. Można dodać, powiedzmy na nowym. Można dodać Endpoint, wtedy musimy podać nazwę endpointu. Klient. I wtedy wybieramy nazwę zgodną z nazwą integracji i endpointu. Jakbyśmy teraz zmienili endpoint, no to będzie też się zmieniać nazwa parametrów. Ta nazwa endpoint no to tak naprawdę się nie zapisuje. To jest tylko dla pomocy. No i taki moment możemy dodać. Te grupy chyba były już wcześniej pokazywane. Jedynie zmieniło się to, że można nie podawać grupy i jest domyślna grupa. Ze względu na to, że tutaj większość tych istniejących integracji już nie ma grupy po prostu. Domyślnie można dodawać inne parametry, wtedy możemy wpisać nazwę i tutaj po prostu mamy prefiks, którego nie można usunąć. Trzeba wpisać coś z tym, że też jest walidacja. Jakbyśmy na przykład chcieli zrobić Request Type. No to będzie... nie, to nie jest... jakbyśmy chcieli zrobić przykład.

**Piotr Buczkowski**: Test Request.

**Przemysław Rogaś**: To będzie niedostępne, bo jakby to jest, bo Authorization Type będzie po prostu niedostępna, żeby nie można było jakby napisać w walidacji z tych predefiniowanych. I w przypadku innych no to wybieramy już ręcznie parametr.

**Janusz Bossak**: Tak się zastanawiam, słuchajcie, czy nie...

**Piotr Buczkowski**: Trochę tą grupę nie rozumiem, bo grupa jest zależna od integracji.

**Adrian Kotowski**: Znaczy to działa trochę tak, że grupa głównie służy do tego, żeby wskazać tą zakładkę, gdzie są te parametry rozmieszczone. Więc jakby grupa może mieć na przykład nazwę związaną z nazwy...

**Piotr Buczkowski**: A to nie dodajemy do bieżącej wybranej grupy? Czy jak?

**Adrian Kotowski**: Możemy do tej bieżącej, ale możemy trafić do innej. Czasami było też tak w niektórych integracjach ich kolor jest po prostu bardzo dużo parametrów, trzeba było tworzyć i po prostu... W sumie to też radziłem im, żeby tworzyć sobie parę grup w ramach jednej integracji oraz to jest tak skonstruowane, że może być parę grup faktycznie w jednej integracji, ale te grupy wszystkie będą w jednej zakładce. Teraz Przemek pokazuje tutaj.

**Piotr Buczkowski**: No tak, tak, to...

**Damian Kaminski**: Tak, bo są inne parametry do POST-a, inne do GET-a na przykład, więc warto by to rozdzielić taką grupą, mimo że endpoint jest ten sam.

**Adrian Kotowski**: Tak.

**Piotr Buczkowski**: No tak, jak najbardziej. Znaczy nie end... Jest jeden serwer endpoint, jest różne to GET-a, POST-a czy czegoś?

**Damian Kaminski**: No tak, ale też w ramach nawet tego samego endpointa może być inne grupowanie dla POST-a, inne dla...

**Adrian Kotowski**: Tak, znaczy można zrobić, tak?

**Piotr Buczkowski**: No ale to jest oddzielna grupa tak już.

**Damian Kaminski**: No tak i wtedy ten...

**Adrian Kotowski**: Tak, znaczy tym bardziej bardzo idea jest taka, znaczy parametry ogólne i na nie też od każdego można tworzyć oddzielną grupę, w tej zakładce, żeby było po prostu wygodniej te parametry przeglądać. To jest duża dowolność, możemy te parametry dowolnie w grupach dodawać w ramach tej integracji, więc to jest takie bardzo wygodne. I też jak jest biznesowy cel całej tej walidacji, bo też do tej pory było tak, że często właśnie konsultanci dawali te parametry ręcznie, było dużo błędów.

**Damian Kaminski**: Parametry grupy.

**Adrian Kotowski**: Gdzieś tam nie wiem, literówki się na przykład... nie wiem, dał dobrze nazwę wyświetlaną, ale dał złą nazwę techniczną i były takie problemy. Później mieliśmy dużo takich zgłoszeń, a ta walidacja no po prostu wymusi ten field jako required, które ktoś na przykład nie wiem, nie jest pewny, to po prostu ma to podpowiedzieć jak to wygląda teraz i że to bardzo usprawni proces. Myślę, że wdrożeń też w przyszłości.

**Damian Kaminski**: Mhm. Wyeliminuje błędy takie najprostsze, tak.

**Adrian Kotowski**: Tak, tak, jeszcze chciałem...

**Damian Kaminski**: A powiększyliście też tu długość nazwy?

**Janusz Bossak**: W tabeli trzeba zwiększyć. Tam jest chyba 50.

**Damian Kaminski**: Backendowo, tak, że po prostu nie ograniczało nas ten człon przed Authorization Type, tak, żeby ten test suffix, który jest de facto nazwą endpointa, tak, do calla, którego wywołujemy, był wcześniej. No właśnie ograniczany jeśli...

**Adrian Kotowski**: Do tego nie daliśmy, ale po prostu jak będziemy już wydawać wersję, to jeszcze ja muszę tam dodać bodajże obsługę eksportu, importu tych parametrów, to dzisiaj pewnie zaimplementuję. Też mogę przy okazji dodać to rozszerzenie tej kolumny, żeby nas nie... uwaga, więcej tu znaków, więc to też zapewnimy.

**Damian Kaminski**: Jeśli po prostu ta... No koniecznie, tak, tak, tak, bo to było duże ograniczenie, trzeba było stosować jakieś skróty, zwłaszcza właśnie jak z jednym systemem było wiele endpointów i...

**Adrian Kotowski**: Tak.

**Damian Kaminski**: I tu właśnie było ExternalREST, potem nazwa systemu, potem właśnie nazwa jakaś biznesowa dla tej funkcji. I ona, trzeba było z nią kombinować.

**Janusz Bossak**: Pytanie słuchajcie, czy tutaj na interfejsie użytkownika wyświetlać w ogóle ten External.REST.TestREST? Bo skoro TestREST jest widoczny u góry, a ten ExternalREST to jest w ogóle już nasze techniczne oznaczenie w bazie danych, to dla użytkownika, nawet konsultanta, nie jest to chyba istotne, a szkoda tutaj miejsca i to no zaciemnia trochę obraz, nie?

**Damian Kaminski**: Tak, ja się zgadzam, ExternalREST niekoniecznie, ale TestREST i ten, który teraz widzimy jako nazwę grupy i ten, który jest w nazwie pola, to nie są te same dane.

**Adrian Kotowski**: Że teraz...

**Damian Kaminski**: One mogą być różne. Nazwa grupy nie jest w ogóle istotna, to jest biznesowa nazwa.

**Adrian Kotowski**: Znaczy tak.

**Janusz Bossak**: OK, no to...

**Adrian Kotowski**: No to teraz można to zrobić tak, że po prostu to często jak tylko jest to, że nazwa grupy jednak jest... nazywa się tak samo jak nazwa integracji, no ale to nie jest 100%, bo to jest dowolność. Można to już różnić.

**Damian Kaminski**: Nie jest, tak.

**Janusz Bossak**: No dobrze. Tutaj widzę po lewej stronie w pierwszej kolumnie jest Integracja AMODIT i Rozszerzenia AMODIT. W końcu mamy jak? Bo wiele było różnych koncepcji. Robimy tak, że jest jedna zakładka Integracje, w której są i te nasze standardowe integracje i te rozszerzenia, czyli takie integracje, którą robią... konsultanci?

**Damian Kaminski**: Dedykowane.

**Janusz Bossak**: Czy jest to...

**Damian Kaminski**: To Kamil, jak to?

**Janusz Bossak**: Jakie jest?

**Kamil Dubaniowski**: Ma być jedna przejściowo, bo to miało być pokazane w piątek, ale mieliśmy mały problem techniczny, więc się wycofaliśmy. Zostaje Integracja AMODIT, przejściowo nadal mamy te Rozszerzenia AMODIT. Zmieniliśmy ikonkę dla Przemka.

**Janusz Bossak**: Znaczy, bo...

**Adrian Kotowski**: Wiemy wszystko.

**Damian Kaminski**: Są zawarte tutaj, prawda? Czyli te Test Test 2 to są rozszerzenia.

**Kamil Dubaniowski**: Tak, tak.

**Janusz Bossak**: Czyli...

**Kamil Dubaniowski**: To są, tak, dokładnie.

**Damian Kaminski**: A możesz kliknąć to rozszerzenie, żebyśmy spojrzeli jak?

**Adrian Kotowski**: Jak mógł...

**Kamil Dubaniowski**: No to są jeszcze jakby był zdublowane.

**Damian Kaminski**: OK.

**Adrian Kotowski**: Czy byś mógł też Przemek pokazać na tej liście integracji jeszcze te integracje, że to faktycznie mamy integracji na samej górze są integracje wbudowane. Jakbyście zobaczyli tak to ten podział, że to czy faktycznie jest to co, o czym mówiliśmy teraz.

**Kamil Dubaniowski**: No i jest też ten panel, jak rozumiem, bo to chyba było do potencjalnie ukrycia sobie integracji, z której nie korzystasz. Też tej listy nie zaśmiecać.

**Janusz Bossak**: Zwolennikiem tego, żeby to było rozdzielane.

**Przemysław Rogaś**: A tak, no jest, to też można pokazać. Domyślnie można to teraz wyłączać. Teraz znika włączenie.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: Nieintuicyjny ten przycisk "nowa".

**Kamil Dubaniowski**: Tak, też, też to dokładnie mieliśmy.

**Janusz Bossak**: Dokładnie, słuchajcie, to musi być, według mnie to powinno być rozdzielone: integracje te systemowe, które sobie można włączyć, wyłączyć i skonfigurować, i rozszerzenia. No te, które dodajemy jako konsultanci w ramach konkretnego wdrożenia. Te są systemowe, tamte są własne, więc...

**Damian Kaminski**: No tak, można by przenieść tu na poziom tego menu Integracje Systemowe, jakiś nazwa katalog czy coś w tym stylu, tak, bo to w formie... bo rozumiem, że jeszcze no to nad tym modelem będziemy pracować, żeby uzupełnić go o jakieś grafiki, ewentualnie krótkie opisy. Tak? Możesz jeszcze raz kliknąć "nowa"?

**Kamil Dubaniowski**: Jak podobnie w zakładce z zadaniami brakuje jeszcze opisów.

**Damian Kaminski**: Czy to będziemy mieli coś jak na procesach czy raportach, jakieś "i", gdzie będzie można odczytać sobie, co to jest, tak?

**Janusz Bossak**: No tak, tak, tak.

**Przemysław Rogaś**: Czy nie ma... opisy miały być tutaj akurat krótkie opisy, ale po prostu ich nie ma, więc nic tutaj się nie wyświetli.

**Damian Kaminski**: No dobrze, bo to jest wydanie na razie minimum, żeby zapewnić kompatybilność. No trzeba będziemy to rozwijać.

**Adrian Kotowski**: Też chciałem dodać, że teraz jest tak, że te integracje wbudowane systemowe nie są synchronizowane. Też jak chcesz odtworzyć jakąś integrację, nową integrację systemową, to musi ten dodać wpis, tam nie wiem w jakimś JSONie i ta integracja zostanie automatycznie dodana jako właśnie tu wpis też przy okazji aktualizacji bazy. I teraz jest tak, że tu jest też specjalnym miejscem na opis tej integracji systemowej. Znaczy to ogólnie też integracje systemowe też mogą mieć opisy, ale plan jest taki, żeby przygotować takie opisy dla tych integracji systemowych, żeby one miały takie tam ładne biznesowe uzasadnienie, po co one są. Więc też pewnie niebawem będzie w AMODITcie, więc tak tylko chciałem dodać.

**Kamil Dubaniowski**: I też widzę Przemek, że już jest ten przycisk "zapisz" wyszarzony i on zszedł na poziom zakładki, tak? I tak jest w każdej zakładce czy...

**Damian Kaminski**: Mhm.

**Przemysław Rogaś**: Wiesz co, ja to robiłem w ogóle na innym branchu, więc to jest tylko jakby w ramach integracji. No ale no jest wyszarzony, dopóki nie ma zmiany. Się pojawiają zmiany.

**Kamil Dubaniowski**: OK. Dobra, czyli rozumiem, że podejmują decyzję, że nie zostaje tak jak jest. Na poziomie tego skrajnie lewego menu będzie podział na Integracja AMODIT i te Rozszerzenia, tak jak teraz mamy, nie robimy tego na jednej liście.

**Janusz Bossak**: A według mnie tak, że bo to jest coś innego i to jest coś innego. Tutaj w rozszerzeniach właśnie jest "nowa" i można importować i tak dalej, a w integracjach jest jakby sterowanie tylko którą włączyć, wyłączyć, tak? Bo on nic, użytkownik... znaczy konfigurować może, tak, ale decyduje o tym... nie może decydować, że chce mieć nową integrację AMODIT, no bo to nie on decyduje, tylko my. I że taką dajemy, a on może z niej korzystać lub nie korzystać. Tak więc to są dwa, według tego.

**Adrian Kotowski**: Właśnie jesteśmy, bardzo ważny aspekt, że parametry systemowe, czy jako taką nie możemy go dawać, nie możemy modyfikować, tylko możemy najwyżej zmodyfikować wartość. Czy nie możemy zmienić typu istniejącego parametru systemowego i nie możemy dać nowego parametru w tej właśnie grupie parametrów systemowych integracji systemowej. A oczywiście integracja systemowa jest jak najbardziej nakazana i tak trzeba czynić, więc też są różnice w interfejsie, tak.

**Kamil Dubaniowski**: Tak.

**Janusz Bossak**: Dokładnie.

**Damian Kaminski**: Mhm.

**Kamil Dubaniowski**: Czy zostajemy przy tych nazwach? Bo wiecie, jakby...

**Damian Kaminski**: Znaczy, według mnie to jest na inny poziom, na inne spotkanie.

**Kamil Dubaniowski**: Dobra, no to lećmy dalej, tak, to prawda.

**Damian Kaminski**: Dobrze Przemku, skoro masz ekran, jeszcze coś powiesz o edycji procesu? Bo tam pewnie dużo zmian takich usprawniających. Natomiast może jakbyś to w kilku zdaniach podsumował, bo widziałem, że tam było sporo zgłoszeń dotyczących poszczególnych pól. Znaczy już mamy wszystkie pola w zakresie edycji w parametrów tych pól pokryte?

**Przemysław Rogaś**: Nie, to były już, to ja już to pokazywałem, to po prostu były na testach zadania. Tam testy trwały, już ten, nic nowego nie powiem.

**Damian Kaminski**: OK. Czyli w kontekście edytora formularza mamy zamknięte prace i skończone, teoretycznie pokryte wszystkie pola. Chyba, że nam się już w takich testach produkcyjnych jeszcze wyjdą jakieś uwagi, tak?

**Przemysław Rogaś**: Mhm, no tak.

**Janusz Bossak**: Super.

**Damian Kaminski**: No dobrze, Ania czy coś w kontekście kolorów tutaj jesteś w stanie jeszcze dopowiedzieć tam?

**Anna Skupinska**: A niestety ostatnio nad kolorami nie pracowałam, zajmowałam się testami i hotfixami, bo wzywają trochę pierwszeństwo.

**Damian Kaminski**: OK.

**Janusz Bossak**: Dobrze, dobrze, to też ważne.

**Anna Skupinska**: Ale kolory jeśli chodzi o kolory, to tak jakby taka podstawowa rzecz dla gradientów już jest, jest testowany, chyba już jest, niestety znaczy zaraz sprawdzę czy już została przetestowana, czy już jest...

**Damian Kaminski**: No.

**Anna Skupinska**: ...zmergowana.

**Damian Kaminski**: Znaczy, ja widzę, że tu była jakaś, jakieś wydanie, tylko to znowu było na poprzednim sprincie, czyli trzydziestym piątym, ale może przeszło z racji na testy.

**Anna Skupinska**: Właśnie przeszło już, bo nie widzę w moich zadaniach. Jest już przeszło testy.

**Damian Kaminski**: Mhm. No dobra, to może krótko o tym opowiedz.

**Anna Skupinska**: Jeszcze nie to, że to jest taka podstawowa, nie robiłam jeszcze, jeszcze kolorów dla tablic i jak dotąd nie ma jeszcze takich bardziej zaawansowanych gradientów, że można sobie wybrać parę rzeczy. Po prostu takie na bazie postawę gradienty na razie są.

**Janusz Bossak**: Nie, nie, na razie zostawiamy tak jak jest, tam więcej na razie nie będziemy w tych gradientach robić. Mamy inne tematy, nie objęte były z powodu też WIM-u zrobione i tyle. Na razie tam nie będziemy tego za bardzo rozwijać.

**Damian Kaminski**: Mhm.

**Janusz Bossak**: Też musimy być jednak my... ilość tych tematów, które trzeba ogarnąć i w szczególności te klienckie tematy, więc nie, nie dokładamy sobie roboty.

**Anna Skupinska**: Ja się chcę zająć resztą problemów z testami integracyjnymi, bo jeszcze naprawiałam, a w piątek parę, ale widzę, że jeszcze jeden jest, jeden jest coś nie tak i będę musiała go naprawić i będą wszystkie działać, będzie w porządku.

**Damian Kaminski**: Jeszcze na poprzednim sprincie, w ten, który skończyliśmy, mam tutaj kwestie raportów systemowych. Nie wiem, czy ty Łukasz chcesz o tym krótko opowiedzieć, o tej możliwości ich kopiowania i zapisywania jako własne.

**Lukasz Bott**: Opiniowania, zapisywania... to tak, nie wiem. Ja wiem, że o mnie chodzi.

**Damian Kaminski**: Łukasz Bott. To znaczy, bo mówiłeś o tym o tym konsultantom, natomiast tutaj nie wiem, czy to wybrzmiało na tej w tym gronie, więc może warto to jeszcze raz powiedzieć.

**Lukasz Bott**: A chodzi o to dodanie do tej grupy, te?

**Damian Kaminski**: Że można stworzyć na podstawie raportu systemowego po prostu swój własny raport, taki customowy, że dajemy taką możliwość.

**Lukasz Bott**: Tak, tak, to to znaczy, to nie było... Może to było tak gdzieś tam, natomiast nie było to, nie, nie było to oczywiste.

**Damian Kaminski**: Niejawnie.

**Lukasz Bott**: Tak, to też generalnie w minionym sprincie pracuję nad tymi właśnie... jak to nazywamy? Konfiguracją raportów systemowych, tak. Idziemy w tym kierunku, że robimy te dashboardy, a to o czym Damian mówi, to po pierwsze, a w tym momencie... to może inaczej. Jeszcze jak mamy jakiś raport systemowy, aczkolwiek będziemy mówię, szli raczej w kierunku kilku dashboardów takich zestawień niż niż listy raportów, to jest też jakiś stary raport, momencik.

**Janusz Bossak**: Jak chcesz coś pokazać, to nie, nie pokazujesz.

**Damian Kaminski**: Szuka chyba Łukasz. To znaczy to ty znajdź się na spokojnie. Jeszcze tam wprowadzenie krótkie: chodzi o to, żebyśmy udostępnili administratorom systemu możliwość skorzystania z naszego raportu i dostosowania go pod siebie. Taki jest cel biznesowy, czyli jeśli mamy stworzony raport, który w jakiś sposób...

**Lukasz Bott**: Dobrze. Nie, nie dobra, dobra, dobra.

**Damian Kaminski**: ...swoim zakresem, definicją jest pomocny administratorowi, natomiast on chciałby go przerobić pod siebie. To właśnie tutaj naszym celem jest udostępnienie takich narzędzi, którymi będzie mógł go skopiować i przerobić właśnie na własne potrzeby.

**Lukasz Bott**: Dobra to jest. Tak, to znaczy. Generalnie co do zasady było tak, że raporty systemowe są przygotowane przez nas, jest to jakaś tam pewna propozycja. Oczywiście staram się zrobić tak, żeby one były w miarę uniwersalne i i i sensowne. Tak to w życiu. Natomiast no ktoś może stwierdzić, że jednak dany raport jest jest dla niego OK, ale chciałby wprowadzić jakieś modyfikacje. Do tej pory by musiał, do tej pory by musiał nam po prostu zgłosić taką prośbę. Jest, nazwijmy to jeden wytrych, jeżeli stworzymy specjalną grupę użytkowników do zarządzania raportami systemowymi. Wtedy te raporty systemowe dla tych użytkowników są możliwe do powiedzmy edycji, do skopiowania, tak i i wtedy można sobie gdzieś tam ten raport skopiować i czy tam powielić, tak i i uszyć, tak. To tak powinno być.

**Damian Kaminski**: Przy pomocy "zapisz jako", tak.

**Lukasz Bott**: Tak, musimy, przypomnij co "zapisz jako" ale... coś?

**Anna Skupinska**: Tylko, że może...

**Damian Kaminski**: Dobrze, strzałeczki pod pod "zapisz" jeszcze raz pod...

**Anna Skupinska**: Tylko pamiętajcie, że ten raport będzie zmieniony tak długo jak się nie zrobi update bazy danych, bo wtedy nadpisze.

**Damian Kaminski**: Nie, nie, nie, nie, nie, nie, dobra, jeszcze raz, jeszcze raz, żebyśmy dobrze zrozumieli kontekst biznesowy. Dokładnie wchodzimy w edycję, trzeba stworzyć odpowiednią grupę. Do tego wiedza będzie zawarta na Wiki, natomiast po stworzeniu, po wejściu w edycję takiego raportu można kliknąć w jego edycji "zapisz jako", zapisać go pod własną nazwą jako nowy twór, w którym my nie będziemy ingerować i który pozostanie w tej definicji, którą zdefiniował administrator po stronie swojego środowiska. Natomiast właśnie nie zalecana jest edycja tych raportów z tymi IDkami, z tymi nazwami...

**Anna Skupinska**: A nie przepraszam, zapomniałam, dobrze, jak "zapisz jako", to będzie stworzony nowy. Przepraszam.

**Lukasz Bott**: No w pierwszej...

**Damian Kaminski**: ...które są, bo tutaj tak jak powiedziała Ania, one będą przez nas modyfikowane. Jeśli nastąpi taka potrzeba w ramach update'u. Natomiast głównie chodzi o to, że mamy te propozycje i żeby one nie były zamknięte, czyli nie były ograniczone. To ktoś może bez konieczności wyklikiwania ich od nowa, po prostu stworzyć sobie ich kopię i przerobić pod własne potrzeby. To jest, to jest cel.

**Piotr Buczkowski**: Ale nie może zapytania zmieniać.

**Damian Kaminski**: Nie może po prostu zredefiniować go na zasadzie samych ustawień raportu, nie zapytania do źródła.

**Piotr Buczkowski**: Nie, chodzi mi o to, żeby tak, żeby nie było, można było pisać zapytań.

**Damian Kaminski**: Nie, mówimy tylko o konfiguracji z poziomu interfejsu.

**Piotr Buczkowski**: Dobrze.

**Lukasz Bott**: Dokładnie tak i to znaczy tak, no źródła systemowe też zostaną opisane, one też mogą być do użycia i można sobie na ich bazie coś tam wyklikać indywidualnie, tak, no. To są same źródła systemowych, też one nie były, one pozostaną w trybie do odczytu, tak w sensie takim, że nie da się nie będąc administratorem... To znaczy, nie da się ich, tych systemów nie będzie, nie będzie możliwości ich zmiany. To Piotrek wspomniał, tak, zmiany tam na przykład zapytania, natomiast można jej będzie jak najbardziej użyć, tak, do własnych raportów. No jest to, co na czymś jest, skupiam, tak, no to na... w pełni ten sprint redefinicja na zasadzie takiej, że przeglądam te co dotychczas zrobiliśmy, niektóre są jeszcze zrobione w starej technologii. Tak to po pierwsze zastanawiam się, czy w ogóle taki raport jest potrzebny, czy on jest czytelny i za wiele tej informacji... To trzeba tutaj też usprawnienia. Poszły, doszły takie usprawnienia jak to, że na przykład mamy taki raport w tej chwili wyświetlam, tak, no powiedzmy, że jest, zwłaszcza w szczególności, to ta lista użytkowników po lewej stronie, tak, no jest tego gęsto, dużo. No oczywiście tym możemy sobie już gdzieś w tym konkretnym raporcie jakoś tam sobie filtrować. Natomiast doszło taka funkcjonalność, która umożliwia zdefiniowanie... tutaj jak mamy tą listę na górze, mamy listę filtrów, tak, to można sobie zdefiniować, które filtry są wymagane i to jest jedna rzecz. Jeśli taki filtr jest wymagany i nie został... nie została ustawiona domyślna wartość, to przy otwieraniu raportu raport się nie będzie wyświetlał. Będzie stosowny komunikat, że musisz podać wartość filtru, żeby, żeby można było wyświetlić jakiś dane. To dotyczy głównie sytuacji takiej, gdy mamy w kontekście tu raportów systemowych to na przykład bazujemy na jakichś danych z logu systemowego albo logów z API Monitora wydajności, gdzie tych danych jest no bardzo dużo i wyświetlanie ich od razu bez, bez jakiegoś narzuconego filtru no powoduje nieczytelność takiego raportu. Więc będzie możliwe zdefiniowanie sobie po pierwsze wymagalnego filtru, a ewentualnie dodania domyślnej wartości, czyli na przykład sobie wyświetlam dane z ostatnich kilku dni, a nie z całego miesiąca czy tam jakiegoś okresu dłuższego. Jakby spowodował nieczytelność, tak. Inne, inne zastosowanie mamy gdzieś tam raporty z takie dotyczące statystyk. Na przykład nie wiem ilości spraw w poszczególnych procesach i etapach. Tak więc, więc tutaj też wyświetlenie wyświetlenie takiego raportu. Nie wiem z jakiegoś, nawet niech będzie przekroju miesięcznego, tak od razu na wszystkich sprawach, etapach, no to to może być niezbyt czytelne, więc trzeba będzie sobie narzucić jakiś tam filtr typu na proces, tak żeby... żeby ten proces wstępnie sobie filtrować, no bo interesuje nas raczej ilość spraw w konkretnym procesie, na przykład w danym okresie tak czasu. O niej... co też przekrojowo ilość spraw ogólnie ile jest w systemie, może też jest informacją jakoś tam wartościową, tak, ale, ale głównie chodzi o to, żeby te filtry umożliwiły właśnie takie... może inaczej, żeby jeżeli chcemy sobie coś wyświetlić to żeby użytkownik no świadomie zawęził sobie zakres wyświetlanych danych, zanim cokolwiek mu pokażemy. Te prace.

**Damian Kaminski**: No dobrze, no to dzięki.

**Lukasz Bott**: Tak, ale my jeszcze z takich rzeczy... jak mogę tylko jak już jestem przy głosie, to pracuję nad tą tak zwaną listą, to przy okazji jakiś taki błąd wizualny zauważyłem. Chodzi o czy czy listę Security Checklist, czyli coś co tutaj już z Danielem Reszką śmy wstępnie rozmawiali. W pierwszej kolejności damy to do klientów, którzy nam przygotowują, którzy sami wykonują te testy bezpieczeństwa. Chodzi o sytuację taką, żeby serwery tych klientów, dotyczy to głównie z klientów, którzy mają instalację u siebie, żeby one były właśnie... to się fachowo mówi hardening tak, albo no nie wiem mówi tuning, tak, żeby one były skonfigurowane zgodnie z tutaj z naszymi wytycznymi odnośnie bezpieczeństwa. I taka checklista będzie podlegała potwierdzeniu właśnie z jednej strony przez naszego na przykład konsultanta, który to skonfiguruje, ale też i przez klienta. To chodzi o takie troszkę... nie chciałbym której brzydkiego słowa używać, ale chodzi o sytuację taką, żeby później, jak klient nam gdzie się robić swoje pen test, tak, swoje pen testy, żeby żeby można było zaweryfikować i porównać, że OK. Ale myśmy jednak to zabezpieczenie zrobili, tak, czy żeby nie było sytuacji takiej, że klient robi testy na nie... nie, nie zabezpieczonym systemie, a myśmy byli świadomi tego, że można było zabezpieczyć. Tak, żeby nie było sytuacji, że nam ponownie wytykają jakieś błędy, które już i tak dawno powinny być być po prostu zabezpieczone. To o to chodzi. Więc tyle ode mnie tak, no. Nie wiem kto tam następny.

**Damian Kaminski**: Nie ma następnych co do zasady, natomiast proszę bardzo kto chce.

**Piotr Buczkowski**: Ja.

**Mateusz Kisiel**: To mogę ja jeszcze w sumie, to po Piotrze.

**Piotr Buczkowski**: Ja mogę pokazać... jak to...

**Janusz Bossak**: Wszyscy się rzucają. Piotr był pierwszy.

**Damian Kaminski**: Proszę, Piotr.

**Piotr Buczkowski**: Mogę pokazać ten mechanizm dla WIM-u, czyli logowanie wysyłanych maili ze sprawy.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: To doszło... chodzi o log w historii sprawy czy tam zdarzeniach sprawy, że z danej sprawy został wysłany jakiś mail. No to zostało to dodane do rozszerzony mechanizm logowania aktywności użytkownika, zostały dodane 3 opcje nowe. Postanowiłem rozbić tak to jedno na jakie na dodatkowe podrzędne, tak, że jeżeli logujemy maile, to też możemy włączyć, wyłączyć logowanie treści albo załączników, no bo tu względnie bardziej chodzi o względy pojemności, tak, bo to jest zapisywane w bazie danych. To może dużo zajmować, tak zwłaszcza załączniki, treść załączników.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: Jeżeli jest normalnie, jeżeli nie, nie jest logowana treść, to jest tylko nazwa załącznika, tak podana. Wiadomo, że załącznik jest na sprawie, możemy odtworzyć. Jeżeli załącznik był pobrany ze sprawy, to możemy zobaczyć tak, to zostało wysłane. Ale powiedzmy, że obydwa. Po włączeniu oprócz tych standardowych, tak do tej pory zalogowanych zdarzeń, mamy też akcje i e-mail. W szczegółach jest jego treść, są załączniki, można pobrać.

**Damian Kaminski**: Znaczy ta lista załączników, rozumiem, jeśli jest zaznaczony na nie, to po prostu jest nieaktywna. Tak? Jest tylko informacja o nazwie.

**Piotr Buczkowski**: Logowany będą tylko, nie będzie linku, będzie tylko nazwa załącznika.

**Damian Kaminski**: OK.

**Piotr Buczkowski**: No ale zazwyczaj to są załączniki pobierane z formularza, więc można sobie tak pobrać. A no mówię, to może zajmować dużo miejsca, dlatego to postanowiłem to wydzielić, żeby można było wyłączyć albo włączyć. Chyba na na tej sprawie nie mam takich. Dobrze, na szybko nie znajdę, tak?

**Damian Kaminski**: No, no myślę, że jesteśmy sobie w stanie to wyobrazić.

**Piotr Buczkowski**: No. Zalogowane są email ten standardowe tak, e-maile też wysłane przez SendMessage, ten regex.

**Lukasz Bott**: Pierwsze, jeżeli mogę taka mała sugestia, jesteś przy tym ekranie, to nie wiem jak mamy tutaj temat maila albo gdzieś dodać ten link do sprawy tak, bo...

**Piotr Buczkowski**: Ale to jest na sprawie w kontekście sprawy.

**Lukasz Bott**: A dobra, dobrze, OK, dobra, sorry.

**Damian Kaminski**: To jest w kontekście, natomiast jak się jeszcze raz byś pokazał jeszcze jakby zjechał w dół, bo tam jest za każdym razem jeszcze dodatkowa informacja o uprawnieniach, jakbyś mógł to wytłumaczyć.

**Lukasz Bott**: Dobra.

**Piotr Buczkowski**: Tak, ale, ale to, to jest to, co do tej pory były. Znaczy nie wiem, czy to jest potrzebne tak w tym widoku, no bo to jest na przykład, że odczyt załącznika tak, że odczytał załączniki uprawnienia, że to użyto w trakcie zdarzenia. Tak.

**Lukasz Bott**: Dlaczego mógł odczytać, tak?

**Piotr Buczkowski**: Tak, dlaczego mógł wykonać tą akcję.

**Damian Kaminski**: I to jest do każdego zdarzenia takie tak zapisane, tak?

**Piotr Buczkowski**: Tak, tak, tak, to jest. To jest, te są te mechanizmy rejestracji zdarzeń użytkownika. Znaczy tutaj trochę, bo czasami może być mylące, jeżeli to jest... Dobrze, nie mam chyba tutaj tego. Nie mam tutaj tego przykładu, gdzie mail jest to mail taki ten odroczony, tak, czyli na przykład ktoś ma raz dziennie wysyłać maile, to wtedy będzie to user systemowy tak wysłał. No bo generator systemowy wtedy to to generuje to.

**Damian Kaminski**: OK. Natomiast to znaczy tak, jeśli tu jest napisane, Piotr Buczkowski e-mail, to znaczy, że ty ten email wysłałeś, tak.

**Piotr Buczkowski**: Ja wysłałem e-mail do Piotr Buczkowski 5 tak w tym mojego posta.

**Damian Kaminski**: A uprawnienia dotyczą tego użytkownika, który jest w pierwszym wierszu?

**Piotr Buczkowski**: Nie. Tak, tego, który wykonał akcję.

**Damian Kaminski**: Piotr Buczkowski. Mhm. OK.

**Piotr Buczkowski**: Tutaj to jest dyskusja była tak, co, także ja, ja dodałem tak użytkownika Piotr Buczkowski 5. Jako ja jest to, że mówi, że mu wysłałem maila, ale tutaj jako on jest, że on został dodany do... To jest trochę mylące, ale nie wiem czy to zmieniasz, tak. Że on został dodany.

**Damian Kaminski**: Znaczy, ja tam dałem odpowiedź do tego. No dobrze, ale to może też nie na, nie na to spotkanie.

**Piotr Buczkowski**: No ale, ale mówię to to, to nie była część tej zmiany, to tak już było, tak.

**Damian Kaminski**: Dokładnie mhm OK. To jeszcze sobie o tym podyskutujemy na na jakimś designie czy Radzie.

**Piotr Buczkowski**: No to tyle.

**Damian Kaminski**: No dobra, super, jeszcze się zgłaszał Mateusz, chyba że ty Piotr jeszcze coś chcesz uzupełnić?

**Piotr Buczkowski**: Nie, nie mam to. Jedyne było takie coś, co można ładnie pokazać, tak?

**Damian Kaminski**: Przepraszam na to.

**Mateusz Kisiel**: To ja generowanie procesu pokażę. Teraz można mu napisać "wygeneruj proces do zakupu sprzętu".

**Damian Kaminski**: Możesz powiększyć ekran, bo jest słabo widoczny, bo masz dużo większą rozdzielczość.

**Mateusz Kisiel**: Ja już. On teraz sobie zbiera instrukcje, pobiera instrukcje do zbierania wymagań i teraz ma taki prompt spory. Mm, w którym prosi o pobranie. Znaczy to jest taki prompt Janusza, który on używał do testów, no i on na podstawie niego wie o coś powinien zapytać użytkownika, tak, czyli powiedzmy pyta się, kto bierze udział w procesie, jakie są główne kroki i tak dalej, może nam odpowiadać na pytania, pytania pojedynczo. Tam się będzie dopytywał. Można też napisać "zaproponuj coś".

**Piotr Buczkowski**: Można dodać jakoś tą listę propozycji pytań to "wygeneruj proces podaj nazwę" tak, żeby ludzie...

**Mateusz Kisiel**: No no.

**Damian Kaminski**: Znaczy, to jest propozycja pytań, zwrócił uwagę. Tylko masz na myśli, żeby to było bardziej takie wizardowe, tak, żeby odpowiadać na poszczególne...

**Piotr Buczkowski**: Na początku. Tak, żeby wiedzieć od czego zacząć?

**Mateusz Kisiel**: To zazwyczaj pewnie będzie tak, że się mógł wrzucić jakąś listę wymagań tak z jakiegoś dokumentu. Ponoć tak przynajmniej Przemek mówił już to zazwyczaj jakiś dokument będzie jakiś Wordowy przykładowo.

**Piotr Buczkowski**: No to...

**Janusz Bossak**: Więcej będziemy...

**Damian Kaminski**: No to zależy od osoby, która pracuje, tak na ile dobrze to...

**Janusz Bossak**: Słuchajcie, tutaj celem było to, żeby ten...

**Mateusz Kisiel**: Przykładowo.

**Janusz Bossak**: ...żeby ten nasz czat, Copilot, stał się taki konsultacyjny, tak. Czyli jeżeli ktoś tak jak tutaj Mateusz napisał, że chce tam jakiś proces zakupowy, to jego zadaniem jest jakby dopytać, tak, ale o co ci chodzi z tym procesem zakupowym? Co on ma robić, dla kogo, nie jest? Ilu będzie użytkowników, jak to ma działać i tak dalej. Tak, czy to jest cały szereg takich pytań, na które trzeba odpowiedzieć i w zależności od tego, co odpowiada ta osoba, tak on dalej prowadzi tą rozmowę. Tak więc to jest... no taki już konsultant, tak, nie tylko "zrób mi coś tam", tylko on wie o co się dopytywać w zależności od tego, jakie padają odpowiedzi.

**Mateusz Kisiel**: No i teraz powiedzmy, że ktoś sobie już to wypełnił całe, że już zebrał ich potrzebną informację, to możemy napisać "wygeneruj". Copilot pyta tak czy taki proces jest odpowiedni. Jeśli chcesz, mogę cię mogę przejść do technicznego projektowania procesu. Czy chcesz dać jeszcze jakieś szczegóły? Nie, wszystko. Wszystko jest. No i teraz on przekierowuje do generowania procesu, tej takiej strony już gdzie się, gdzie jest podgląd. Mm no i on to jest trzeba ten komunikat zmienić, "bez tworzenia sprawy". To jest tak naprawdę w tym momencie generowanie, generowanie podsumowania tego czatu, czyli teraz teraz AI na podstawie tego czatu generuje takie podsumowanie do tego procesu, to jeśli one napisało...

**Damian Kaminski**: Mhm.

**Mateusz Kisiel**: Widać to jest ten...

**Damian Kaminski**: ...do uwzględniania uprawnienia, że to tylko administrator może taki nowy proces definiować, jeśli tak jest ograniczony.

**Mateusz Kisiel**: Mm, zapomniałem o tym, ale no i tak nie może zrobić nowego procesu, tak, czyli no co najwyżej to po prostu błąd będzie miał.

**Janusz Bossak**: A to, a dodać to wszędzie mamy te uprawnienia, tak.

**Mateusz Kisiel**: No to dania jest.

**Damian Kaminski**: No OK. Tak, tak.

**Mateusz Kisiel**: No i to jest już ten stary wygląd, tak, czyli może sobie dalej dopytywać, coś zmieniać, zmieniać jakieś etapy i tak dalej. No i trzeba poczekać aż się wygeneruje, bo to trochę trwa.

**Janusz Bossak**: Jak ktoś właśnie Mateuszem rozmawiałem, czemu tak długo trwa, ale to tak naprawdę nic po naszej stronie. To model teraz myśli.

**Mateusz Kisiel**: No tak, no w tym momencie się generuje to cały ten JSON, który który który reprezentuje ten proces, więc to tego nie możemy przyspieszyć, bo potrzebujemy, jakby nie da się tego ani równolegle, ani nic takiego. No, bo potrzebujemy mieć całe te informacje, które, które całą całą informacje są potrzebne, żeby no.

**Piotr Buczkowski**: Tata, teraz teraz serwery Microsoftu pracują, nie nie nasze.

**Mateusz Kisiel**: Tak, no i tu co?

**Damian Kaminski**: Tak, ale to działa w takim trybie teraz, powiedzmy, agentowym, że tam jest wiele zapytań obsługiwanych, czy to jeden prompt tak długo generowany jest?

**Janusz Bossak**: Teraz. Jeden, jeden.

**Mateusz Kisiel**: Jeden.

**Damian Kaminski**: OK.

**Mateusz Kisiel**: No ale też przykładowo nie można tego zrównoleglić, bo jak się zmieni jedną rzecz, to on powiedzmy wy co coś zrobili, a czy potem coś zdubluje będą jakieś problemy, więc lepiej żeby to było mm tak, żeby pełne informacje miał.

**Damian Kaminski**: Słuchajcie no...

**Janusz Bossak**: Może co najwyżej ja...

**Damian Kaminski**: Na podstawie tego jak mamy, proszę.

**Janusz Bossak**: W tym...

**Mateusz Kisiel**: No i też i też widać, że OK.

**Janusz Bossak**: Przepraszam, dobra.

**Mateusz Kisiel**: Znaczy też widać, że już nie ma takiego jednego drugiego zapytania, tylko jest było jedno zapytanie na starcie, które rozpoczęły ten proces. No i teraz co jakiś czas odpytuje i sprawdza, czy już się zakończył generować. No i to było potrzebne, żeby na chmurze gdzie jest time out na gateway nie było, nie było problemów. No i już to było testowane chyba przez Janusza i to działa nawet na chmurze.

**Damian Kaminski**: To co powiedział Janusz bym powiedział, że że v0 czy w innych dowolnych narzędziach prototypowych, z których korzystamy. No to też trochę trwa, więc to jest według mnie jak najbardziej akceptowalne osoby, które mają doświadczenie akurat z tego typu produktów.

**Janusz Bossak**: Znaczy ja bym tylko... atrakcyjnił ten to oczekiwanie.

**Damian Kaminski**: Spinner.

**Janusz Bossak**: To tam w tym v0 to nawet pokazują takie obrazki, że tam pracuje nad wyglądem, pracuje nad czymś, robię coś tam i tam jakieś latają różne rzeczy, żeby to wyglądało atrakcyjnie, tak, że coś się dzieje tam, że on tak ciężko tam pracuje, nie pod spodem, więc moglibyśmy też wyświetlać tak losowo jakieś rzeczy, że pracuje nad formularzem, pracuje nad diagramem, dodaje kolejne etapy. Rozważam coś tam, wiesz takie.

**Damian Kaminski**: No tak, żeby nie było nudno.

**Janusz Bossak**: Żeby nie było nudno, bo tak to nie wiadomo. Zaciął się, nie zaciął, robi coś nie.

**Mateusz Kisiel**: No to jest do zrobienia jeszcze to, żeby w momencie klika ten przycisk utwórz nowy proces, żeby się na starcie pokazywał ten Copilot, tak, bo w tym momencie się jeszcze dalej pokazuje ten stary wygląd, no ale to już jest szczegół.

**Damian Kaminski**: No i jeszcze to co tutaj jest na dole chyba Switch To Process, to Piotr sugerował, żeby to pokrywać, nie?

**Janusz Bossak**: Ale...

**Mateusz Kisiel**: Tak, to też jest to, tak, no no to trzeba jakieś znaczy, no to ma tą zaletę, że w tym momencie mogę sobie kliknąć ten przycisk i i się pokazuje ten modal, więc być może warto by przemyśleć jak to powinno wyglądać. Tak.

**Piotr Buczkowski**: Chodzi mi o to, żeby to nie, to nie...

**Damian Kaminski**: Trzeba ukryć do przycisku to.

**Piotr Buczkowski**: To nie wyglądało tak jak wywołanie JavaScript.

**Janusz Bossak**: Tak, wygląda jakby jakiś błąd się pojawił, jakieś coś nie wiadomo. A to nie jest żaden...

**Piotr Buczkowski**: Więc...

**Damian Kaminski**: No po prostu musimy to napisać. Jakiś wywołały, tak, czy przejdź, czy czy dokonały biznesową nazwę, a tą techniczną ukryć gdzieś pod spodem, tak.

**Mateusz Kisiel**: Znaczy to jest jakaś nazwa tej funkcji, która się przez elementy wykonuje. No i żeby było wiadomo, co chcemy uruchomić. Tak zrobiłem, że się pisze ta nazwa taka techniczna, ale może może jakieś tłumaczenia trzeba by dołożyć.

**Piotr Buczkowski**: No ale to ile, to ty wiesz?

**Damian Kaminski**: No da się ją jakoś na pewno sprytniej przedstawić.

**Janusz Bossak**: No tak, bynajmniej podsumowując nasz Copilot zyskał jakby umiejętność bycia takim konsultantem od tworzenia procesów tak, czyli jest w stanie dopytać się użytkownika samodzielnie, bo do tej pory było tak, że ktoś wpisywał jakąś tam polecenie, że chcę proces taki i taki on bezdusznie po prostu robił ten proces. Tak, a w tej chwili dopytuje się tak.

**Damian Kaminski**: Tak, może jeszcze Mateusz podjedź na górę to, co mówi Janusz, żeby to pokazać tak, bo tak bardzo pobieżnie to pokazaliśmy tak, czyli tutaj, jak rozumiem Janusz zebrał takich 20 kluczowych pytań, które są istotne z punktu widzenia analityka. Tak, czyli kto uruchamia proces, jakie są główne kroki, żeby naprowadzić tego tworzącego na to, co kluczowe jest do zdefiniowania, aby ten proces odzwierciedlał jak najbardziej potrzeby? Tak.

**Janusz Bossak**: Im więcej potem szczegółów się poda... No to jeszcze ewentualnie z Mateuszem potem porozmawiam, bo ten jak ja używam tego produktu tak w normalnych tych czatach, no to później one się pytają po jednym.

**Mateusz Kisiel**: Tak, to ten ten tak sam się pyta, jak to jest twój prompt dokładnie i widziałam, że się dopytuje dalej.

**Damian Kaminski**: Tak jak w tym, co wysłał Przemek, tak żeby to ona od razu zadał pytanie, czy chcesz rozpocząć pracę nad kolejnymi punktami i tam tylko odpisujemy tak ją wtedy zadaje jeszcze raz pierwszy punkt i dopytuje o te 3 pytania, a nie od razu 20, tak?

**Janusz Bossak**: Tak, tak.

**Mateusz Kisiel**: A no i też ten prompt już nie jest w AMODITcie tylko jest po stronie tego mikro serwisu, czyli bez aktualizacji AMODITa można go zmieniać łatwo.

**Janusz Bossak**: No i to jest super, bardzo dobrze.

**Piotr Buczkowski**: Zrozumiało słówko "gity"?

**Mateusz Kisiel**: Jeszcze raz.

**Damian Kaminski**: No chyba tak, tak, no bo przeniósł.

**Piotr Buczkowski**: Zrozumiało słówko gity?

**Janusz Bossak**: No dobrze, bardzo, bardzo fajna rzecz idąca w stronę właśnie upraszczania wdrożeń i ułatwiania naszym konsultantom, ale też i klientom tworzenia całkiem sensownych wtedy już procesów, no bo jednak nie tylko w oparciu o jego nazwę, którą podał użytkownik, ale jednak o pewną analizę ustrukturyzowaną tej analizy i tak dalej. Super, bardzo fajne.

**Damian Kaminski**: Dobrze, mamy jeszcze 7 minut. Czy ktoś jeszcze chce się czymś pochwalić?

**Mariusz Piotrzkowski**: Ja mogę pokazać tą funkcję ForEachAttachment z tobą robiłem w tym sensie.

**Damian Kaminski**: P...

**Janusz Bossak**: Oj właśnie miałem ostatnie potrzeby jej użycia, ale nie było jeszcze.

**Mariusz Piotrzkowski**: To on na moim środowisku testowym przygotowywanie takie proces reguła jest taka prosta, po prostu sobie robię jakąś listę plików, potem wszystkie pliki, które są PDF-em dodaje do listy, a dla wszystkich ogólnie plików po prostu sobie zapisuje ich nazwę po kolei. No i po wykonaniu reguły otrzymujemy coś takiego, że otrzymujemy te nazwy wszystkich plików, można pobrać jeszcze rozmiary, metadane, różne inne rzeczy oraz dla przykładu plik zmergowany, który jest mergem tych wszystkich PDF-ów, czyli tego to, jak tego i tego. No i w wyniku mamy coś takiego. Więc dostępnych parametrów... no to mamy tutaj w dokumentacji. ID, Tag, TagBody, no to samo co w GetExcelData w sumie.

**Damian Kaminski**: I Value też jest dostępny, natomiast Value jest pobierane dopiero na żądanie. Tak to co Piotr sugerował pod kątem optymalizacji.

**Mariusz Piotrzkowski**: Tak, tak. Tak, tak jest zrobione, tak, że dopóki się nie pobierzemy Value, to no chyba, że się wstawi to jak w tym przypadku do listy, z tego co pamiętam lista, a jeżeli dodajemy dokument do listy, to automatycznie pobiera Value, ale nie jestem pewien, natomiast to dopiero byłoby robione w kolejnych funkcjach. Sama ta funkcja dopóki się jawnie nie pobierzemy Value, to to go Value nie, nie, nie zwróci, nie, nie, nie odwoła się do bazy danych, także jest optymalnie.

**Janusz Bossak**: Wiem, że teraz... jakby czepiam się tego przykładu konkretnego, jak drugi raz puścisz ten zmergowany, będzie też zmergowany tak i tak będziemy mieli więcej.

**Mariusz Piotrzkowski**: Nie, nie, bo to dodałem do pola ten zmergowany dokument, a nie jest w tych załącznikach.

**Janusz Bossak**: To jest dodawanie na listę, dobra, dobra, no tak to by był...

**Piotr Buczkowski**: No możesz jeszcze kod pokazać. AddToList nie wystarczy this?

**Mariusz Piotrzkowski**: Z tego co pisaliśmy, to uzgodniliśmy, z tego co pamiętam, uzgodniliśmy, że nie będziemy robić z 2 powodów. Po pierwsze powodowałoby to tworzenie zmiennych, które zawierają zbyt dużo elementów, wtedy można by robić głupie, głupie nieoptymalne rzeczy, a po drugie był problem z tym, że trzeba by by zmodyfikować mocno mechanizm pobierania Value dla zmiennej FileContent, to by miało wpływ na wiele różnych funkcji, no i to było zbyt dużo roboty, żeby to zrobić na raz.

**Damian Kaminski**: Możesz kliknąć na "to list"?

**Piotr Buczkowski**: Coś mi się tu nie podoba? No dobrze, to nie teraz, nie no teraz...

**Damian Kaminski**: Commentary, OK.

**Janusz Bossak**: Czy wygląda dobrze? Tak na pierwszy rzut oka?

**Lukasz Bott**: W pasie.

**Damian Kaminski**: Znaczy... No dobrze, to już już już uzupełniamy. Proszę, chcesz powiedzieć o tym?

**Lukasz Bott**: Dobra, to znaczy generalnie chodzi o to, że w AMODITcie do sprawy możemy dołączyć załączniki i możemy dołączyć je do pola na formularzu, do dedykowanego pola typu dokument i wtedy już mieliśmy przygotowane funkcje, które umożliwiają z poziomu reguł właśnie jakieś tam operacje na tych plikach dołączonych. Natomiast bolączką było to, że nie mieliśmy takiej możliwości dla plików załączonych tak swobodnie do, czyli do tak zwanej listy plików w sprawie. No i po to powstała ta właśnie konstrukcja językowa silnika reguł Attachment, czyli taka dodatkowa pętla, która umożliwia właśnie iterację po, po tej liście swobodnie dołączonych plików po to, żeby wykonać na nich jakieś tam operacje. To tutaj implementacje... implementacje myśmy... no była to taka potrzeba, po prostu natury trochę konsultacyjnej. Tak to konsultantom powinno ułatwić troszkę pracę, no może niekoniecznie to jest biznesowo tak, ale, ale to o to chodziło, tak intencja pojawienia się tej konstrukcji językowej.

**Mariusz Piotrzkowski**: No na przykład można zobaczyć jakie pliki, kto modyfikował ostatnio, jakie są na przykład rozmiary wszystkich plików w sprawie, jakiś stan OCR, kiedy były zmodyfikowane i tak dalej.

**Lukasz Bott**: Dokładnie tak.

**Damian Kaminski**: Znaczy tutaj tak biznesowo to bardziej była potrzeba po prostu przechowywania tych dokumentów właśnie na liście po to, żeby móc je później rozdzielać. Na przykład taki konkretny kontekst biznesowy: to jest zestaw dokumentów, które muszą być podpisane przez użytkownika, natomiast niekoniecznie chcemy je osadzać w tabeli, a chcemy mieć możliwość odwołania się do nich w prosty sposób, żeby po podpisaniu przenieść je na przykład do e-teczki. Tu jednocześnie Mateusz, mam nadzieję, że że słuchasz aktywnie, to to prośba właśnie o przekazanie, bo w WIM też z tego korzysta. Musieliście robić wcześniej tabelę plików, że taka funkcja jest. Możemy też w piątek o tym jeszcze wspomnimy na na spotkaniu z konsultantami. I jeszcze to, co mi przyszło do głowy na podstawie tego name i tej listy... Ee to nie wiem, czy to już wszystko przetestowaliście, natomiast co w przypadku, gdy będą dwa takie same załączniki o tej samej nazwie? Czy to nie będzie powodowało błędu, może trzeba było to jakoś jeszcze zabezpieczyć?

**Piotr Buczkowski**: Nie.

**Mariusz Piotrzkowski**: Nie, nie będzie, po prostu ID będzie inny, a nazwa będzie taka sama.

**Damian Kaminski**: OK, no bo tu attachment zdefiniujemy po nazwie, tak, to to miałem na myśli.

**Piotr Buczkowski**: Nie.

**Mariusz Piotrzkowski**: A w taki sposób?

**Piotr Buczkowski**: I też powinno zadziałać.

**Mariusz Piotrzkowski**: Tak, tak, też zadziała.

**Damian Kaminski**: To może to trzeba napisać w przykładzie w syntaxie tutaj, żeby jeśli są takie przypadki, to odwoływać się poprzez ID, bo tu nie ma jawnie tego wymienionego.

**Mariusz Piotrzkowski**: Dobra, to jest, tylko dopiszę.

**Daniel Reszka**: A to ID jesteśmy w stanie wydobyć?

**Piotr Buczkowski**: No czy... this.Id.

**Daniel Reszka**: W sensie tutaj robisz "this" tak i sobie zdobywasz to tak?

**Piotr Buczkowski**: I jest jeden, i jest jednym z propertiesów. Tak jak name.

**Daniel Reszka**: OK, dobra.

**Janusz Bossak**: No to dopóki...

**Damian Kaminski**: No nie jest to wymienione, tak jak widzimy tutaj z prawej strony nie ma takiego przykładu.

**Mariusz Piotrzkowski**: No to...

**Piotr Buczkowski**: Było.

**Mariusz Piotrzkowski**: Będę musiał sobie dopisać potem, żeby...

**Piotr Buczkowski**: Było. Nie, nie ma w przykładzie.

**Mariusz Piotrzkowski**: Żeby...

**Damian Kaminski**: Nie ma.

**Mariusz Piotrzkowski**: W przypadkach a i nie napisałem, żeby zaraz dopiszę, żeby to jeszcze potem poprawić, bo na razie jest na internecie to jest, a potem jak przyjdzie na AMODITa ja sobie dopiszę tutaj.

**Piotr Buczkowski**: Znaczy, docelowo trzeba zrobić, żeby było, można było też podać "this", ale jedno jeżeli teraz był problem.

**Damian Kaminski**: No to dopisz to do...

**Piotr Buczkowski**: Nie, nie, tak. W pierwszej wersji będzie.

**Mariusz Piotrzkowski**: Tak, bo chodzi o to...

**Damian Kaminski**: To znaczy Piotrze z tym "this" to nie ma chyba takiego przypadku w sensie innego i nie wiem czy to będzie intuicyjne dla, dla wdrożeniowców. To znaczy, jeśli to opiszemy jako przykład to OK. Natomiast takie same "this" to wydaje mi się, że nigdzie indziej w innych funkcjach nie jest w ten sposób definiowany jest.

**Piotr Buczkowski**: Jak to nie? Jak w ForEachObject?

**Janusz Bossak**: We wszystkim na ForEachObject jest też tak.

**Damian Kaminski**: No tak, ale wtedy w ForEachObject odwołujemy się "this.coś", tak?

**Piotr Buczkowski**: No tak jak tutaj.

**Damian Kaminski**: No tak, tylko tu masz propozycję taką, żeby po prostu "this" bez żadnego parametru, tak.

**Piotr Buczkowski**: Tak, tak.

**Damian Kaminski**: OK, no ja to rozumiem, tylko trzeba wtedy napisać taki przypadek użycia, tak, żeby to było dla kogoś zrozumiałe, że to jest właśnie taki obiektowe.

**Piotr Buczkowski**: Znaczy, już nie pamiętam, nie pamiętam. Tak, tak, tak. Nie. W przykładzie to w ForEach... w przykładzie Attachment, czy to będzie opisać?

**Janusz Bossak**: Dobrze, słuchajcie, my musimy kończyć, bo mam w tej chwili spotkanie dotyczące Centrum Onkologii i przetargu, więc tam się udaję do Moniki. Chyba przeszliśmy wszystkie te Mateusz, przynajmniej zdecydowaną większość. A dzisiaj przypominam, że później mamy planowanie, tak, o czternastej. Sprint.

**Damian Kaminski**: OK.

**Janusz Bossak**: Także dzięki wszystkim naprawdę za wielki wkład, te szczególne podziękowania dziewczynom testerkom. Muszą się uwijać po prostu jak w ukropie z tymi testami, bo jest ich naprawdę dużo, także szczególne podziękowania dla nich, a dla nas wszystkich również naprawdę za duży, duży wkład i świetną robotę. Dobra. Trzymajcie się.

**Damian Kaminski**: Cześć.

**Janusz Bossak**: Cześć.

**Filip Liwiński**: Cześć.

**Marek Dziakowski**: Na razie.

**Adrian Kotowski**: Cześć.

**Oktawia Ostrowska**: Cześć.
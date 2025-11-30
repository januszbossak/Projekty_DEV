**Data spotkania:** 27 listopada 2025, 10:10

---

**Przemysław Sołdacki:** Chcę napisać wizard do eksportu i importu. Wydaje mi się, że mogę wybrać, które procesy wyeksportować – czy wszystkie, czy pojedyncze, czy wybrane. Jeśli proces ma powiązane rzeczy typu rejestr, słownik, to żeby mógł pociągnąć też te raporty, słowniki, cokolwiek. Żeby pokazywało kompleksowo – jak eksportuję, kliknąć "wrzuć mi wszystko" i przyniesie mi wszystko, albo mogę wybrać niektóre rzeczy. Podczas importu to samo.

**Janusz Bossak:** Mam od dłuższego czasu przeczucie, że to powinno być zupełnie inaczej. Kiedyś z Piotrem rozmawiałem, ale jakoś odrzucił tę myśl. Powiem ci o co chodzi. Musiałbym zautomatyzować proces eksportowania rzeczy na środowisku testowym. Wyobrażam sobie, że wchodzę na środowisko produkcyjne, na które chcę przenieść te zmiany, i w jakiś sposób wskazuję, że moje zmiany są na środowisku testowym. I poprzez API tam się dobieram.

**Przemysław Sołdacki:** To nie przejdzie. Te środowiska się nie widzą, bardzo często się nie widzą. Są na innych serwerach, na innych sieciach, mogą się nie widzieć. Poza tym wtedy stracilibyśmy możliwość sprawdzenia, co de facto było w tych plikach, takiego śledzenia. Więc zostawiłbym, że to idzie poprzez pliki. Ktoś eksportuje, przenosi przez jakieś mechanizmy, logując się na inne terminale do drugiego środowiska, wgrywa i importuje.

**Janusz Bossak:** Właśnie.

**Przemysław Sołdacki:** Tylko to ja bym tutaj napisał eksport powiązań, powiązanych elementów. W takim razie tak ogólnie i słownik.

**Janusz Bossak:** Tak, bo wtedy musi pociągnąć nasze, tak jak tam te rozmowy w sprawdzaniu zależności, że istnieją na przykład inne procesy, które są wykorzystywane w polach Odnośnik.

**Przemysław Sołdacki:** I to właśnie o to chodzi, że wtedy mi pokazuje, co tam jest powiązane i mogę sobie checkboxem zaznaczyć, że to też mnie importuj, skoro już będzie. Ładnie to coś, co jest zmian, ale ładnie mi się podobają. Nagle wchodzę, patrzę – fajne, dużo takich jest tam zależności. Te zależności pewnie za chwilę się wczytują, pewne ustawienia formularza się długo ładują. W ogóle, bo takie ramki doszły do tych guzików.

**Janusz Bossak:** To jest przypadek. Już usunęliśmy to, ale się nie.

**Przemysław Sołdacki:** Tak, to nawet ładne.

**Janusz Bossak:** Niestety poszło do jednego z klientów i mu się spodobało.

**Przemysław Sołdacki:** Ale mi też się spodobało. To fajne jest.

**Janusz Bossak:** Ale to znaczy, że biblioteka Design została zaktualizowana i coś tam monitor dodali. Nie może tak być, że po aktualizacji biblioteki Design nam się zmieniają style.

**Przemysław Sołdacki:** Ale znaczy, czekaj, jeszcze się odtwarzam tutaj?

**Janusz Bossak:** Tak, bo w jednym miejscu jest, w innych nie ma.

**Przemysław Sołdacki:** Może nie, bo tu jak wszedłem na te procesy, jak tu najeżdżam i że one są w takich rameczkach – fajnie wygląda. Ale dobra, może nie może przypadkowych ruchów. Zobacz, jak mam powiązania i widzę, że tu mam powiązania. Obserwatorzy, że sobie mogę zaznaczyć checkbox, także to też tak tutaj widzę, że mogę sobie wybrać. Tutaj ja rozumiem, mógłby być jakiś powiązane raporty, wstawione raporty, jeśli są. Bo tutaj mam brak, brak, brak, ale podczas eksportu to tam, gdzie brak, to mi się nie pojawia, tylko te rzeczy, które są. I wtedy mogę checkboxami zaznaczyć, żeby wrzucić. Później po prostu importu to samo – widzę, że w pliku są jakieś rzeczy, mówię "to i to mi wrzucić, a resztę nie wrzucę". Więc to to jest?

**Janusz Bossak:** Problem jest, że tak powiem, rozgałęzień kolejnych warstw tego przenoszenia. Tak jak to powiedzieliśmy o tych i to chyba jest najtrudniejszy element tego wszystkiego. Jest jakiś proces, który zależy od jakiegoś rejestru poprzez pole Odnośnik. I teraz tamten rejestr też może mieć kolejne inne odnośniki do jeszcze innych rzeczy. Ogólnie rzecz biorąc, nie wiadomo, jak głęboko to sięga.

**Przemysław Sołdacki:** Tak, ale to można to jakoś ograniczyć. Jeśli nie, to za chwilę by się okazało, że tam wszystko ze wszystkim jest powiązane. Ale taka naturalna hierarchia, że jest proces, pod procesem mogą być podpięte słowniki. A jeśli jest proces, to mam tylko informację, że jest proces, ale już nie jedzie dalej w głąb tego drzewka, tylko będę ostrzeżenie, że tutaj oddzielnie na liście procesów jest ten proces, że może też bym chciał go jakoś zaznaczyć. Na razie nie projektujemy tego, tylko chodzi mi o to, że ogólnie taka, że wybieram swoje, eksportuję i wybieram się importuje. Mogę, nie muszę pojedynczą. Ja chcę całą paczkę, bo wiem, że proces związany jest z 5 raportami i 2 słownikami, to go eksportuję w całości, importuję. I tu jest problem nadpisywania i to musi być dobrze ogarnięte, tak że na przykład to już mam słownik i już go na produkcji zmieniam i nie chcę, żeby mi się domyślnie pozamieniał, bo na testach jest inny. Więc to jest świadomy wybór tego nadpisywania. To tyle. Ale to może jedźmy dalej, co tu mamy?

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** Bo to jest, zakładam, że to może pomóc mocno naszym wdrożeniowcom, serwisantom, więc oni o to prosili. Więc to jest tutaj dokończenie. I wydaje mi się, że tutaj celem biznesowym z mojego punktu widzenia najważniejsze jest to, że patrzę, dlaczego mi się pole zmienia. Tam powinniśmy się zmieniać, bo jest reguła, albo na przykład pole znika, bo jest reguła. Wiem, która jej szukać, bo teraz patrzę, znika. A może jest ten, nie wiem, hidden field, no to wchodzę reguły, szukam po nazwie pola, szukam, czytam. To się da zrobić, ale muszę się naszukać, a my i tak te informacje mamy w bazie.

**Janusz Bossak:** Do pewnego stopnia tak. Szczególnych przypadków nie ma, bo wtedy, kiedy sobie nazwę pola zapisz do zmiennej, potem będziesz chciał to używał, ale mówię, to są takie przypadki.

**Przemysław Sołdacki:** Ale to jest, nie wiem, 5% przypadków, że ktoś tak zrobił. Jak mnie znajdzie, to nie znajdzie. No to trudno, to sobie będzie dalej drążył temat, ale zwykle po prostu znajdziemy, pokażę, jest, jest szybciej. Dobra, historia edycji procesu. Jest to zrozumiałe i ten K1 ważny jest dobrze rozpisany. Bardziej mnie interesuje, to co jest dalej i przynajmniej na takim ogólnym poziomie. Poprawki w module raportowym. Tam jest wprost puszka pandory.

**Janusz Bossak:** Ja bym to nie żeby tak klientowi, to trzeba napisać jakiejś stabilizacji, a czy tam usprawnienia w module raportowym, że jak poprawki, to wiadomo, że są błędy.

**Przemysław Sołdacki:** Ale weź klient, który używa, to wiesz, że tam są błędy, ale to jest okej, zrozumiałe, o co chodzi. Nie wiem, czy to dalej spisywać, bo to jest puszka pandory. Jak zaczniemy tam grzebać, to wiesz, piłkarze tam jest 50 rzeczy do poprawienia, a niektóre grube nawet. Ja bym to znaczy, dobra, jak do tego podejść. To może to wy jak do tego podejść, bo to będziemy musieli sobie.

**Janusz Bossak:** Ale trzeba napisać jakieś prace koncepcyjne nad tam czymś nie. Część do klienta interesuje klienta interesuje wynik, tak więc my możemy sobie wpisać, że ten pulpit medycznym jest.

**Przemysław Sołdacki:** Zostawię tak jak jest. Ja nie mówię, że ja w takiej formie to prześle klientowi, ale sobie jeszcze tam poczyszczę to zanim wyślę, ale dobrze żebyśmy mieli. A ja powiem skryptów. Tak, jak już to będziemy mieli zrobione, to my zrobiliśmy trochę ten jak przetworzeniu skryptu, tylko po prostu wsadzimy w ten nowy interfejs, żeby to tak wyglądało. Docelowo funkcjonalność dla SSL jest services. To tak, to będziemy sobie szczegółowo ustalać, bo to w każdym kwartale jest.

**Janusz Bossak:** To ja. Tylko.

**Przemysław Sołdacki:** Danych z rejestrów między środowiskami.

**Janusz Bossak:** To jest temat, który ja nie wiem, czy on jest. Według mnie dużo bardziej istotne jest co innego, tak z punktu widzenia wydajnościowego. To, co zresztą dzisiaj tam przed chwilą rozmawialiśmy, żeby Piotr w końcu opracował koncepcję rozdzielenia case definition, tak żeby były podzielne procesy, dodatkowe tabele i z definition tam 1, 2, 3, 4 jakoś i żeby to ze sobą wszystko współgrało, działało na raportach i tak dalej, ale jednocześnie obciążało całą bazę. Tak to jest.

**Przemysław Sołdacki:** Gadałem chwilę z Piotrem, kiedyś przy w kuchni i pojawiło się pytanie, czy to coś da? Bo w sumie to jest nasza hipoteza, że to coś da, może się okazać, że to nic nie da.

**Janusz Bossak:** Może się tak pogadaj jeszcze. Piotr nawet zrobił jakieś daleko idące próby przy okazji AmRest, bo tu głównie AmRest tam się o to zapraszał. I tam mieliśmy koncepcję jakiś plastrowanie bazy danych, czegoś tam wydzielania tabel do innej nawet i łączenia. No i to Piotr jakoś ostatecznie się tak skończyło, że to w sumie niewiele co daje.

**Przemysław Sołdacki:** Właśnie, bo najłatwiej byłoby zrobić klony tej tabeli niż kilka tabel. Czy to z mniejsze przeciążenie na serwerze, czy będą szybciej zapytania robione, nie wiemy, bo będą miały oddzielne indeksy. Może wymagałoby jeszcze głębszego robienia, czyli już nie w takiej formie, czyli tylko jak jest jeden proces, to kolumny są dokładnie takie, jakie są w procesie, nie ma jakiś innych przypisywania, w której kolumnie to jest trzymane, tylko po prostu jeden do jednego. Ale to też nie wiadomo, czy to coś da. Należałoby jakieś eksperymenty z tym zrobić.

**Janusz Bossak:** Wiesz tu.

**Przemysław Sołdacki:** Wiesz co, to możemy wpisać coś takiego i to myślę, że bym to wpisał, a przede wszystkim to bym chyba podniósł wyżej. To jak koncepcja będziemy mieli, to zrobimy. To tutaj można wpisać prace koncepcyjne na wydajność tej maści, case definition. Możemy popracować, potestować, bo nie wiadomo, czy to jest dobra metoda, czy to w ogóle coś da. Może trzeba coś zupełnie innego. Może trzeba dane po prostu replikować do Redis i wtedy mieć po prostu szybkie czytanie. Nie zrobimy testów, to tam się nie napalałbym, że to jest gruba zmiana. Tak czy inaczej musimy zobaczyć, czy to coś daje. Tam nie wiem, miliona rekordów i zobaczyć, czy podzielenie tego na pół to czy daje, bo może nic.

**Janusz Bossak:** Jakby inspiracją do tego jest kilka rzeczy. Po pierwsze zmniejszenie rozmiarów bazy danych ze względu na brak kupy. I klienci woleliby mieć odłożone już ileś lat, do których już nie sięgają i mieć bazę, która jest mniejsza, do której sięgają na bieżąco. To jest pierwszy.

**Przemysław Sołdacki:** Dobra, dzielenie tabeli proces. Dzielenie tabeli rok.

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** Usuwanie starych danych czy tam archiwizacja bardziej.

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** 100.

**Janusz Bossak:** I to właśnie był główny powód, tak żeby w momencie, kiedy te tak jak MSIT trzeba, AmRest mają już tych kilkanaście lat danych. Po co im to tam trzymać? Nie, a obciąża system i wszystkie nasze jakieś SQL pytania.

**Przemysław Sołdacki:** Metoda nie wymagająca jakiś drastycznych prac naszej stronie, to jest taka, że kopiujemy tę bazę, która jest tak jak jest i sobie leży, a zrobienie mechanizmu kasowania po prostu starych danych może dać, ale jaja osowanie.

**Janusz Bossak:** Tutaj jest to kasowanie. Dlaczego się pracę przerwały? Dlatego, że ktoś może mieć załóżmy jakiś proces czy rejestr, do którego się odnosi. Bo bieżących rzeczach, ale tamten już jest nieużywany od lat, ale do niego ciągle się odnosimy, bo to jest rejestr klientów, który zrobiliśmy 10 lat temu. I te sprawy mają niskie numerki i ciągle tam są, więc to nie jest tak prosto, że wziąć wszystko, co było w latach 2010-2020 wyciąć. Bo możemy się tam ciągle odwoływać, tak?

**Przemysław Sołdacki:** To po prostu trzeba zrobić dobrze, tak. Jeśli są procesy, w których, jeśli jest proces, który jest nowy, tak mam, jeśli podzielimy nowe na stare, na nowe i stare, to jeśli jest jakiś proces nowy, który się odwołuje polem Odnośnik do starej sprawy, to tej starej sprawy nie należy usuwać. Na przykład da się jakiś algorytm przyjąć, który będzie miał sens, bo wtedy mówimy, u dużego klienta zwłaszcza mówimy, słuchajcie, zgredźcie sobie tę bazę, a na nowej bazie odpalcie skrypt, który wam wytnie to, co jest do wycięcia. To sklep czy po prostu jakieś tam narzędzie pochodzi sobie, zrobiliście bazę, mniejszą, jeszcze puścicie, żeby się baza sama zoptymalizowała, przebudowała rejestry, czy te indeksy. I baza będzie śmigać po prostu 5 razy szybciej, bo będzie miała 5 razy mniej danych. I to i tak jest jakieś tam czynności, jak pójdzie coś nie tak, to tworzycie z jakby przełączyć się dalej na tę bazę starą. Przykład także, że jakaś tam operacja, że oni sobie puszczają w weekend w taką takie coś i już.

**Janusz Bossak:** Temat, który wraca jak bumerang przez wiele lat ostatnich i nie ma na to ciągle sensownego rozwiązania takiego, które dałoby się wprowadzić na produkcję.

**Przemysław Sołdacki:** Nie jest, bo we WSI to dokładnie zrobiliśmy. Wywaliliśmy wszystkie dane starsze niż 3 lata.

**Janusz Bossak:** Tak, no brute force takie rozwiązanie trochę.

**Przemysław Sołdacki:** Ale to jest klientowi niepotrzebne, bo jeszcze tak naprawdę raporty łączące dane z wielu lat to są potrzebne tylko na bardzo, bardzo ogólnym poziomie. Ja patrzę, jak mamy dane sprzedażowe, to my też mamy przechowane z 3 lat. Te dane starsze gdzieś tam są, ale my ich nie używamy w raportach. Tu raz na jakiś tam na rok chcę zobaczyć, nie wiem, nasze obroty z iluś tam lat, ja nawet nie muszę tego z Tableau wyciągać, to sobie w Optimie pytam. Ale szczegółowych danych nie potrzebuję. Co mnie obchodzi tam 10 lat temu nie wiem jakaś faktura, no.

**Janusz Bossak:** To może być, może 10 lat temu nie i z naszego punktu widzenia może nie, ale tak jak Neuca na przykład, no to oni chcą mieć jakieś dane audytowe, tak kto podjął taką decyzję, że.

**Przemysław Sołdacki:** Ale będą mieli w tej starej bazie.

**Janusz Bossak:** No.

**Przemysław Sołdacki:** Bazę sobie zostawiają, a nowe dane są nowe, bo to drastycznie zmienia. Przykładowo masz dane z 10 lat, a potrzebne są tylko z ostatnich 2, to wszystko będzie szybciej działać. Indeksy mniejsze i mniejsze zasoby w bazie, a tam ta baza może być całkiem wyłączona albo wyłączona, ale jeśli tam nikt nie loguje, więc serwer bazodanowy i tak sobie tam wygasi, będzie utrzymał nie trzymając nic w pamięci. Więc dobra, prace koncepcyjne to jest zrozumiałe dla klienta też. Zrozumiałe, jak coś nam wyjdzie, to wyjdzie. Tutaj zarządzanie wymaganiami. Napisałbym o co chodzi. Jest rzecz w kontekście, a którą bym rozważył, żeby zrobić dużo wcześniej niż patrzy. Bo to może być związane z tym przenoszeniem procesów i to jest kwestia tego, co tutaj uważam, musi być dla nas drastyczną poprawą potencjalnie. No skoro Mateusz robi szablony procesów, no to do tego jest potrzebny mechanizm przenoszenia i tutaj wsparła. I przy tym, bo ja mam taką wizję, to jest pomysł do przeanalizowania. Gdybyśmy dali rzecz prosto w implementacji, czyli wchodzę sobie w ten powiedzmy definicję procesu i tu miałbym zakładkę dokumenty czy wgrywam pliki, nic więcej i nadaje im nazwy i nic więcej, prosta sprawa, tak jak mamy tam budujemy ten archiwum, archiwum, to tam ma strukturę, to po prostu lista plików, koniec. I gdybyśmy wiedzieli tak, że jeśli w procesie sobie dodam plik, który się nazywa "konfig zalecenia dla AI" do konfiguracji procesu, czymkolwiek sobie to nazwiemy, to w momencie importu, znaczy przenoszenia, można by uruchomić coś, żeby AI wzięło te zalecenia, przeczytało sobie te zalecenia, na tej podstawie wypytało użytkownika, a następnie naniosło zmiany na proces. Wtedy mógłbym wrzucić w procesie taką zasady, jak skonfigurować ten proces? I wiedziałbym, że to niezależnie od konsultanta zostanie zrobione w ten sam sposób.

**Janusz Bossak:** To się nie uda, znaczy. To musi przejść, to znaczy to doświadczenia. Zdobywam teraz przetwarzanie tych zapisów transkrypcji. Niestety, śmieci na wejściu, śmieci na wyjściu. Nie to wrzucanie takich luźnych plików, jakiś tam wymagań od klienta, jakiś nie wiem, właśnie notatki ze spotkania czegoś tam. To jest taki bałagan. Ogólnie rzecz biorąc, tak i teraz z tego dopiero trzeba zrobić ustrukturyzowaną informację dla AI, zatwierdzoną, z której on będzie coś mógł zrobił, bo jak on bawili na takim bałaganie, to bałagan wytworzy.

**Przemysław Sołdacki:** Tak, tak. Ale słuchaj, to nie tam nie będzie bałagan, bo tak jak ktoś musi świadomie zrobić szablon procesu, stworzyć regułę, stworzyć to i tak dalej, to ten projektant tego procesu może opisać, co musi być skonfigurowane i może to konfigurację robić człowiek.

**Janusz Bossak:** Ja będę tego.

**Przemysław Sołdacki:** Ale będzie, bo jakie moglibyśmy mieć pliki? Opis procesu, to mamy do tego pole. Ale byłby taki plik, mógłby nie być w systemie nawet, tylko w systemie jest o tyle dobrze, że jak sobie importuję, eksportuję, to te pliki też by mi się przyniosły. I tam mógłbym mieć plik przygotowany przez nas, nie tam przez byle kogo, gdzie jest definicja, jak skonfigurować ten proces. I może konsultant sobie odpali i ręcznie skonfigurować proces z tymi wytycznymi. Ale AI też może to zrobić, bo to będzie bardzo dobrze ustandaryzowane i przetestowane przez nas, to nie jest przypadkowe. Chodzi o to, że jeśli wiadomo, że tak jak tutaj mamy obserwatorzy spraw i to nie powinni być przypadkowi ludzie, tylko innym elementem konfiguracji jest spytaj, kto powinien mieć możliwość oglądania wszystkich spraw. No to trzeba się dowiedzieć od klienta, tak kto będzie mógł wszystkie sprawy zmienić, kto będzie mógł zmieniać sam proces. To pytania do klienta, zanim w ogóle ten proces powinien pójść na produkcję. Jeśli jest, załóżmy jest ścieżka akceptacji faktur, to pytanie powyżej, jakiego progu musi być dodatkowa akceptacja? Trzeba spytać klienta, kto ma robić dodatkowo akceptację powyżej tej kwoty, trzeba spytać klienta. To są te rzeczy i później to wgrać w proces. Więc może to robić człowiek, ale to dobrze zrobić, to tę konfigurację, jakby konsultant dostanie pytania od AI, zdobędzie informacje od klienta, odpowie i na podstawie tego mówię, dobra, to ja już tam pozmieniam te rzeczy.

**Janusz Bossak:** Czy?

**Przemysław Sołdacki:** Więc to nie jest tak, że coś tam wrzucamy jakieś śmieci i sobie AI pracuje, nie, nie, to musi być bardzo dobrze przygotowany. Tak jak my programujemy proces, programujemy reguły, to zaprogramujemy AI pisząc takiego profesjonalnego prompta.

**Janusz Bossak:** Musi być analiza, znaczy ten, no, to co już kiedyś tam mówiłem, tak, że to musi być prowadzenie tego konsultanta przez proces analizy zdobywania informacji, uzupełnienie tej informacji uzupełniania kontekstowo, czyli w zależności od tego, co odpowiedziano wcześniej, poprzednim pytaniu czy 2-3 pytaniach wcześniej, to dalsza analiza musi przebiegać zgodnie z tym, co tam powiedziano i jaki to jest rodzaj, typ procesu, co tam powinno w nim się jeszcze znajdować, tak dalej.

**Przemysław Sołdacki:** Dokładnie, ale. Ale podam ci przykład, może być takie coś, że projektant procesu mówi, jeśli klient powie, że nie chce mieć dodatkowej akceptacji, usuń etap, ten usuń tę i tę regułę i tyle. A jeśli klient podał, że chce, żeby podał od jakiego progu, ale dodatkowa akceptacja, to wejdź w regułę, tę konkretnie zmień nawet w tej linijce, albo w tym miejscu ten próg. I koniec, albo tam, że na przykład jest zmienna wysokość progu. Zmień wartość tej zmiennej i tyle. To nie jest tak, że coś tam sobie coś tam zrób. Nie, to bardzo konkretne polecenia, gdzie co trzeba pozmieniać. Jeśli tak byśmy zrobili, to zarówno nasz konsultant, a jak i nawet sam klient mógłby sobie wgrać taki szablon i mieć AI wypytać, co tam trzeba zrobić? Ktoś odpowie i AI jest w stanie to wykonać, tak, ale w takim trybie bardziej konwersacyjnym. Więc chodzi mi o to, że taki plik to nie jest jakiś taki, nie wiem, ktoś sobie coś wrzucić, tylko to jest instrukcja dla AI, jak skonfigurować ten proces. I dopóki my tego nie robimy na AI, to człowiek będzie to robił. I to możemy bardzo dobrze przetestować na ludziach. Najpierw także, to jest jakiś pomysł. Ja nie mówię, że tak musimy zrobione, ale nam sobie pomyślałem, że może powinniśmy zrobić spotkanie, gdzie, bo jak ty będziesz i tak w Warszawie, to mógłbyś być nawet jeden dzień dłużej, w ściągnęlibyśmy jeszcze innych ludzi tutaj od koncepcji, żebyśmy sobie porysowali na tablicy za i przeciw różne możliwe pomysły, bo ja rzuciłem jeden pomysł. Ja nie mówię, że tak musi być, ale to jest jakiś pomysł, ktoś może będzie miał lepszy, może złożymy kilka pomysłów jeden. I taką pracę koncepcyjną nad tym, jak AI mogłoby ustandaryzować pracę, bo to widziałeś. To są Marcin zrobił takiego.

**Janusz Bossak:** To też kiedyś myśmy zrobili, znaczy tak, no widziałem to, taki generator prądu.

**Przemysław Sołdacki:** Ale wiesz, wiesz co jest dla mnie największą korzyścią z tego, największą korzyścią jest standaryzacja, czyli ja po prostu wrzuciłem zapytanie od klienta, maila, on pokazał, że to jest to, spytał, czy to na pewno jest to, powiedziałem tak, zrobił sobie według zasad, które mamy w strategii, opisał i. Dla mnie największą zaletą jest to, że niezależnie, kto to będzie robił, czy to nie robił Marcin, czy którykolwiek handlowiec, wszyscy będą tak samo oceniać klienta. To jest standaryzacja. I chciałbym tak samo mieć, że bierze mi konsultant, którykolwiek nowy, stary, wrzuca i kurde wie, jak ma to zrobić. I jak chcemy, żeby firma pracowała inaczej, zmieniamy naszego agenta, naszego prompta i firma działa inaczej. To jest dla mnie ważniejsze, nawet być może niż samo podniesienie wydajności, bo to jest zapewnienie jakości. Tutaj, no na przykład on coś zrobił, ale ja mówię, a to chyba jednak tylko skanowanie, no i on biorę, że to pod uwagę i trochę bardziej świadomie. To nie jest regułka napisana, nie. Więc tego typu mechanizmy byłyby super, tak jak mówię, do standaryzacji. Dobra, czekaj, wróćmy tu.

**Janusz Bossak:** Wracając do tego jeszcze, co rozmawialiśmy o tym, znaczy, wydaje mi się, że to, co teraz omówiliśmy, to jest koncepcja. Tak rzeczywiście na ten kwartał tam nie wiem, trzeci czy czwarty przyszłego roku, żeby aż tak daleko iść i budować te procesy w oparciu taki dialog. Natomiast to, co robi teraz Mateusz, mówiąc Mateuszu Kołakowskiemu, czyli próbuje stworzyć te standardowe procesy, to według mnie tu powinniśmy mocno się nad tym pochylić i to, co tutaj zresztą mówiłeś przed chwilą.

**Przemysław Sołdacki:** Ale to właśnie o to chodzi.

**Janusz Bossak:** Żeby te standardowe procesy nie takie noże standardowe, wiadomo, tak, które są trochę pseudo standardowe, bo one się za każdym razem jednak ciutkę zmieniają, żeby tutaj mu pomóc. I tak powiedziałeś, żeby tu AI potrafiło powiedzieć co.

**Przemysław Sołdacki:** Tak, więc co to może AI, że tak powiem, cię się niejasno wyraziłem. Mi chodzi o te standardowe procesy, nie jakiekolwiek.

**Janusz Bossak:** Bo ja myślałem, że mówisz o takich normalnych, dużych procesach o wdrażaniu klienta i tak dalej, ale to wtedy mi nie bardzo.

**Przemysław Sołdacki:** Nie, właśnie chodzi o to, że załóżmy ja pamiętam, jak z spytałem, czy możemy sobie teczkę wdrożyć u nas firmy. I natychmiast dostałem 10 pytań, które mogłoby AI mi zadać. Może moje odpowiedzi były mało ciekawe, bo w zasadzie nie wiedziałem, co odpowiedzieć, ale mogło być tak, że Mateusz Kołakowski, żeby było jasne, robi te szablony i w tym szablonie na razie nie ma gdzie wpisać, ale mógłbym ich miejsce na przykład właśnie wrzucenie dokumentu i ten dokument musi się nazywać X, jakoś tam nie wiem, "wytyczne dla AI" czy tam "wytyczne konfiguracji procesu" i musi się tak nazywać. Mamy coś zakodowane, może to być po angielsku, nie ma znaczenia. I jeśli taki plik jest, to podczas importu AI mówi, słuchaj, tu są wytyczne, czy ja mam to skonfigurować, albo po prostu jest specjalny guzik "skonfiguruj według wytycznych" i wtedy dokładnie AI robi to, co projektant szablonu przygotował. Więc ja prace koncepcyjne nad tym, to możemy sobie tutaj wrzucić nawet, bo to nie jest takie proste. Nad użyciem AI do konfiguracji szablonów procesu, bo o to mi chodzi, żeby to było jasne, nie, nie cokolwiek, tylko to muszą być szablony zrobione przez nas, żeby one były przemyślane, że to tak jak my sobie piszemy reguły standardowego szablonu. To możemy od razu dać wytyczne, jak ten szablon należy skonfigurować, typu dodać jakiś tam userów, trzeba grupę założyć albo grupa i już się zaimportowała, ale trzeba kogoś dodać do tej grupy, to ten proces zadziałał i tak dalej. Więc zostawiam, że to jakieś prace koncepcyjne. No i tutaj ewentualnie gdzieś tam można by wrzucić. Więc nie chcę tego napychać się naszej mapy. Raczej właśnie.

**Janusz Bossak:** Znaczy, no już ciasne robić.

**Przemysław Sołdacki:** Ale zaczyna się napychać, to mam. Więc nie wiem, możemy to wiesz przenieść dalej. Możemy to przenieść na K3, żeby tu nie było napchane. I to bym wysoko do.

**Janusz Bossak:** Samo to przenoszenie procesów między środowiskami, a wiem, ile z tym było gadania i tak dalej, to zajmie całego Damiana plus pół Piotra.

**Przemysław Sołdacki:** No dlatego wiesz. Tak jak mówiłem, widzę 2 najgrubsze rzeczy, przenoszenie procesów i dokończenie tego raptem. 2 zespoły oddzielne, które pracują tylko nad tym przez 3 miesiące, aż dojdą do zajebistości, że te rzeczy po prostu działają tak, że przez najbliższe lata nie będziemy się musieli do tego dotykać, bo po prostu wszystko tam działa. Więc chodzi o to, żebyśmy się nie rozpraszali na inne rzeczy, bo to jest trudne. To nie jest tak, że tam klikam import, nie, tylko musimy tam ileś rzeczy musi sprawdzić, czy mi to nie zepsuje na produkcji, że na przykład coś się nadpisuje, czy na pewno chce. Więc zrobienie tego dobrze to będzie jakieś tam wyzwanie. No dobra, ale wiesz co, bo tak nie mamy tu nic, co jest na K4 stało. Coś co tu poprzekładać.

**Janusz Bossak:** O K4 jest tak daleko, że.

**Przemysław Sołdacki:** Ale wiesz co, żebyśmy mieli jakieś ramy tego, no jakby.

**Janusz Bossak:** Wzrok ten myśli.

**Przemysław Sołdacki:** Mam jeszcze jedną koncepcję, ale to też dyskusje, bo wiesz, ja jestem generatorem pomysłu swoim dobrym, tak jak ja. Niekoniecznie moje pomysły są dobre, ale jakieś są. Chodzi mi o to, że my działamy w trochę innym trybie, zawijam, przynajmniej to tworzenie procesu. Dział robimy na tej zasadzie, że rozmawiamy z AI, AI generuje sona, a my programistycznie tego sona zamieniamy na definicję procesu i wrzucamy do AMODIT i to jest droga w jedną stronę. Natomiast mogło być tak, że przestajemy działać w trybie takiego AI ma pytanie odpowiedź, tylko w trybie agenta, gdzie mówimy "tu jest specyfikacja wymagań", sobie ten proces on sobie robi to po kawałku. Dodaj etap, dodaje drugie etap, dodaje strzałkę, dodaje regułę. I później sobie ten sam agent lub drugi agent sprawdza, czy to, co tam zrobił, to w ogóle jest zgodne ze specyfikacją i sprawdza, czy to w ogóle działa, bo na przykład i jakby pozdrowienia modrica programistycznie jest dobre odpowiadanie, czy ta operacja jest w ogóle wykonalna? Jeśli nie, to dlaczego? Na przykład? Bo agent mówi, to usunę sobie regułę, a AMODIT mówi, nie możesz poznać, bo pola są, które w tam albo chcę zmienić pole, nie możesz, bo jest reguła, która korzysta z tego pola. I on mówi, aha, dobra, czyli tryb agentowy, gdzie to sobie chodzi w tle i coś tam robi, pracuje tak pojedynczo nad konkretnymi kimś procesami. Tylko to jest taka wizja odległa. Wydaje mi się, ale chociaż już się okazać wcale nie, bo za pół roku to w ogóle te agenci to będą tak zapierdzielać, że po prostu to będzie normalne.

**Janusz Bossak:** Znaczy, ja tutaj wrócę do tematu, może trochę obok, ale jednak ważne go tych testów end-to-end. Dlaczego do tego wracam? Bo to jest też jeden z elementów tak pracę takiego agenta, że coś działa. Czyli, że ten proces, który sobie tam robię, jestem w stanie zewnętrznym narzędziem typu Playwright przetestować, że mogę przejść tego etapu na ten, że się to przekazało tej osoby, które się miało przekazać i tak dalej, tak.

**Przemysław Sołdacki:** A czy Playwright jest oparty o AI?

**Janusz Bossak:** Znaczy sam jako taki nie, bo to jest język programowania. Można powiedzieć tylko język programowania testów, ale i wspiera Playwright i ja sam pisałem, jest mnóstwo różnych opracowań, gdzie można za pomocą AI dość łatwy. Znaczy to znowuż to pozorność łatwości, tak, no, ale można generować sobie takie skrypty, skrypty Playwrightowe i teraz te skrypty już potem normalnie uruchamiasz i to działa. Ja już takie próby zrobiłem. To, co tutaj rozmawialiśmy, mam opracowany no o ileś.

**Przemysław Sołdacki:** Zastanawiam się, czy to nie jest ślepa uliczka.

**Janusz Bossak:** Nie, to jest w ogóle baza i podstawa wszystkiego. Zresztą jak czytam o tych agentach i tutaj przerabiam różne rzeczy. Jeżeli mówimy o agentach, które mają pisać na przykład frontend, to w każdym przykładzie, jaki widzę na YouTubie w różnych filmikach, każdym przykładzie jest AI agent, który dokładnie robi to, o czym mówię, czyli używa testów, że pisze sobie testy Playwrightowe i za pomocą Playwright patrzy dosłownie, patrzy na aplikację i sprawdza, czy ona działa tak, jak powinna działać. I to jest w ogóle warunek sine qua non, to po prostu musimy coś takiego mieć.

**Przemysław Sołdacki:** Co tak, ale wiesz co, znaczy zastanawiam się, dlaczego mówi ślepa uliczka, bo te przejście z takiego działania zwykłego na działania agentowe to mogę sobie wyobrazić agenta, który robi to, co robią nasze testerki, czyli mają jakąś tam specyfikację tego, jak to powinno działać, mają wiedzę ogólną i sobie klikają i testują, czy to działa i czy jest zgodne ze specyfikacją. I mógł być agent, który robi dokładnie to samo w całości i nie pisze sobie żadnych skryptów, tylko po prostu robi to ręcznie. Różnica, jaką widzę, że taki agent będzie działał wolniej, zużywał dużo więcej zasobów niż odpalenie skryptu w Playwright. Więc jeśli byśmy chcieli puszczać dużo testów represyjnych, to by tam zżerało dużo pieniędzy, więc może być wydajniej, żeby agent pisał tylko skrypty.

**Janusz Bossak:** Tak, tak, no bo to tak się robi.

**Przemysław Sołdacki:** Tylko. Idealnie by było, gdyby taki agent, jeśli już pisze sobie te skrypty i ewentualnie też aktualizuje, to robiłby to, czego nasze testerki się nie chcą podjąć chwili pisania skryptów. I moglibyśmy być tak, że czy już na etapie projektowania funkcjonalności, czy nawet później, że nasze testerki piszą, co powinno być przetestowane, agent pisze z tego wszystkiego razem skrypty Playwrightowe.

**Janusz Bossak:** Dokładnie tak, tak to już mam zrobione. Cała zabawa polega na tym, przynajmniej na tym etapie mojej wiedzy i umiejętności posługiwania się AI, że trzeba go nauczyć. Co to znaczy, znaczy musi wiedzieć, jak wygląda na przykład pole typu data u nas, czyli gdzie on musi klikać, w co, że tam w ten zegarek czy w ten kalendarz, że mu się pojawi akurat takie coś, a nie coś innego. I to jest.

**Przemysław Sołdacki:** A on tego?

**Janusz Bossak:** Nie. Znaczy po części wyczaję, ale często się.

**Przemysław Sołdacki:** Może na razie nie.

**Janusz Bossak:** Może na razie nie. I to jest robota, którą ja znaczy teraz już nie robię, ale robiłem tam miesiąc czy 1,5 miesiąca temu i zacząłem ten Page Object Model, bo to tak się nazywa robić, tak, czyli biorę sobie nasz formularz i to jest ten nasz Page Object i opracowuję z AI wszystkie elementy, które na tym formularzu mogą potencjalnie wystąpić, czyli pole typu data, pole typu text, pole typu takiego przycisk, taki przycisk, taki prawy panel, historia, coś tam, coś tam. I wtedy jak już masz opracowany ten Page Object Model i to jest największa robota, którą trzeba zrobić. To później napisanie testu "przetestuj mi następujący scenariusz", dosłownie tak możesz pisać, nie weź się, zaloguj do tego, zrób to, zrób to, zrób to. Kliknij to, sprawdź, czy to jest to. I on z takiego opisu robi test, który możesz wielokrotnie używać, tylko napiszę ten test dobrze zgodnie z tym Object Model i w momencie, kiedy ja coś zmienię w tym modelu, to wszędzie mi się to zmieni, bo to jest od.

**Przemysław Sołdacki:** No. Tylko, bo wtedy rola naszych testerek zmieni się ręcznych testerek, bo rozumiem, one ręcznie testują, nie piszą skryptów, zmieni się na nadzorców agenta, który pisze testy Playwright.

**Janusz Bossak:** Czy one piszą skrypty same dla siebie właśnie takim języku naturalnym, że te jakby scenariusz repo nie.

**Przemysław Sołdacki:** Czyli one piszą jakby wytyczne do testowania i nadzorują to, żeby agent te wymagania przełożył na Playwright.

**Janusz Bossak:** Tak, znaczy.

**Przemysław Sołdacki:** Tak, tak, taka jest wizja docelowa.

**Janusz Bossak:** Znaczy. Ogólnie tak, no właśnie nie wiem, czy to one, czy powinien być, powinna być osoba, która się na tym zna, znaczy mówię o tej warstwie przetwarzania tego na tego Playwright. Dziewczyny powinny się zajmować testami rzeczy nowych, które jeszcze nie są przełożone na Playwright, bo dopiero jak coś jest ustabilizowany i uznajemy, że tak to ma działać, wtedy jest sens przełożyć tego to na Playwright.

**Przemysław Sołdacki:** Wiesz co, ale ja bym jednak się upierał nad tym, że ja podejrzewam, że w ciągu określonego czasu, to dosyć krótkiego, pół roku, rok, 2 lata, trudno na tym etapie to przewidzieć, że główną pracą ludzi, takich pracowników biurowych, będzie nadzorowanie AI, tak samo jak wejdzie robotyka, jakąś większą skalę, zadaniem tych różnych inżynierów, na przykład budowlanych, nie będzie noszenie cegieł, tylko patrzenie, czy te roboty dobrze te cegły noszą i czy nie wiem, jak robot nie wiem tynku je, czy tynku je właściwą ścianę. I praca w tą stronę się będzie zmieniała, więc my powinniśmy.

**Janusz Bossak:** Dokładnie.

**Przemysław Sołdacki:** Jakby takie coś, że ktoś siedzi i klika ręcznie testy, to to może robić tylko po to, żeby dobrze nakierować tego agenta i AI, żeby on testował to, co trzeba testować i żeby testował w taki sposób, jaki trzeba testować. Więc jeśli testerka opisuje, co trzeba testować, agent zmienia to na Playwright, to ona może sprawdzić, czy te testy w Playwright, jak się odpalają, czy one w ogóle poszły w dobrą stronę. A jeśli nie, to mówię agentowi, słuchaj, agent, głupoty mi tu robisz, weź mnie nie klikaj tego, nie się klika coś innego, bo w ogóle nie, nie ta ikonka. I on to sobie poprawi. Gdy tak jestem w stanie sobie to wyobrazić i widząc to, co się teraz dzieje.

**Janusz Bossak:** Teoretycznie. Na tym etapie no to wymaga jednak znajomości tego Playwright, znajomości tej ideologii, nazwijmy to, znaczy metodyki Page Object Model, znajomości wszystkich tych selektorów.

**Przemysław Sołdacki:** To nie przekracza zdolności intelektualnych naszych testerek. O ile pisanie skryptu jestem w stanie powiedzieć, że one się będą z tym źle czuły. Pewnie się źle czują, dlatego on tam mimo prób nie udało się to i je. Gdybym ja teraz miał pisać skrypty w Pythonie, to by była dla mnie męka, ale ja mówię, powiem agentowi, napisz mi skrypt, który robi to i to, i on napisze i to zadziała. To ja wiem, że to jest dobrze zrobione, bo ja wiedziałem, czy to ja zauważam, na przykład dałem Gemini, żeby mi przeanalizował tabelkę w Excelu i na podstawie danych policzył mi segmentację, to mi pokazał, że umieszcza się 4 skrypty w Pythonie napisał. I mi dało odpowiedź, czyli on nie robił tego ręcznie, tylko napisał skrypty, które to robią, zobaczył, co wyszło, zrobił kolejny, z tym zrobił, po 4 skryptach wyszła wynik końcowy. I dla mnie to jest lepiej, bo jest mniejsze ryzyko pomyłki, bo to ostatecznie poszła algorytmem, więc pewnie to będzie w tą stronę szło. No ale ja i tak musiałem nadzorować to, co dostałem, to to jest to, co chciałem, nie, więc człowiek będzie takim kierowcą do tego AI.

**Janusz Bossak:** Czy generalnie mi chodzi o to, że te testy end-to-end są nam niezbędne w wielu przypadkach?

**Przemysław Sołdacki:** Słuchaj, wpisałem na na K4, jak się da wcześniej, pewnie testerki mogłyby to wcześniej, jak to jest coś rusza, jeszcze im dasz.

**Janusz Bossak:** Po pierwsze, muszę robić ciągle, muszą robić teraz jednak K4. Chciałbym mieć efekty, znaczy działające testy i pokryte.

**Przemysław Sołdacki:** Ale to co wpisać na K4?

**Janusz Bossak:** Znaczy, według mnie to powinniśmy robić we wszystkich kół i od K1, K2, K3, K4, my też musimy pracować nad testami, mamy bardziej bliskie pokrycie testami.

**Przemysław Sołdacki:** Ale tego nie robimy i jak to zaczniemy robić, to będziemy robić cały czas, tylko chodzi o to uruchomienie tego mechanizmu, czyli nauczenie testerek, pokazanie im, jak to się robi.

**Janusz Bossak:** Daliśmy sobie uszatku jednym zrobić, no.

**Przemysław Sołdacki:** Dobra, no ale wiesz, jak się boję, znaczy tylko pod warunkiem, że to nie zaangażuje deweloperów. To tak.

**Janusz Bossak:** Znaczy, człowiek zapisać. Zapisaliśmy sobie strategii stabilizację. To jest jeden z elementów stabilizacji systemu. Musimy mieć testy, musimy mieć testy po prostu.

**Przemysław Sołdacki:** Wiesz co, dobrze, ja to wrzucę.

**Janusz Bossak:** Na przykład ten przypadek, który tutaj widzieliśmy dzisiaj na tym, tak że zrobiły się te rameczki. To jest rzecz, którą muszą wykrywać testy.

**Przemysław Sołdacki:** Ale. Tylko wiesz co, agent mógłby tego nie zauważyć, bo pewnie by nie zauważył, że na co zwrócić uwagę, człowiek zauważy. I wtedy testerka mówi, słuchaj, agent, dopisz taką rzecz w tym Playwright, czy się nie pojawiają jakieś rameczki dziwne. Znaczy nawet nie wiedziałbym w sumie, jak agentowi to wytłumaczyć, ale wiesz, jakby dalej, jak chodzi mi o to, że my nie zrezygnujemy z ludzi, ale będzie tak, że jeśli powie testerka, że agent, napisz mi taki skrypt, co tam będzie sprawdzał, czy się ramki z powrotem nie pojawiły, bo tutaj zobacz na guzikach są takie ramki, to on podejrzewam będzie w stanie wyczaić, jak ten skrypt napisać.

**Janusz Bossak:** To są też metody takie, robi się zrzuty ekranów i on porównuje na przykład zrzut ekranu do zrzutu ekranu, tak, czy to się zmieniło. I co się na tym zrzucie ekranu zmieniło, tak, czyli po aktualizacji, czy jest tak samo, jak było przed aktualizacją? Ale to są inne techniki, niekoniecznie się nawet innych testów nie tutaj.

**Przemysław Sołdacki:** Jest to, to ja tak napiszę, czyli my w K1 tworzymy mechanizm testów end-to-end w Playwright z użyciem agenta. Zaangażowanie testerów bez angażowania programistów. Jeśli tak, to róbmy. Daje sobie jakiś deweloper siedział, bo nie zrobimy rzeczy, które tu są.

**Janusz Bossak:** Nie jest potrzebny, no potrzebny testem.

**Przemysław Sołdacki:** To tylko zanotowałem, że tak jest dobrze. Wiesz co?

**Janusz Bossak:** Tylko nie będę się tym zajmować.

**Przemysław Sołdacki:** Słuchaj, to przyjrzyjmy się tutaj dalej. Czekaj te zmiany. Halo. Ale mało. Wysłałam spotkania później mam wywiad, także nie pogadamy o trzynastej. To, że o trzynastej? No hej. Dobra, właśnie 5 minut nam zostało się. W takiej koszulce, no dobra. Dopełnieniem o tym w kalendarzu mieli wpisali, którą dzisiaj. Kiedy więc dobra jest to zarządzanie wymaganiami ze znakiem zapytania i tu nie wiem, czy jest to proces, obsługa wymagań do procesu projekt.

**Janusz Bossak:** Bo to jest być związane z nim zarządzaniem wymaganiami. Tak, czyli gdybyśmy już je mieli, to wtedy na ile ten edytor procesu mógłby być z tym spokojnie tak.

**Przemysław Sołdacki:** Dobra, ja to połączę, bo to jest w sumie. Dobra, bo tutaj gdzie ja wiedziałem, że to jest dobrze czuję. Dobra. To będzie powiązane. Zobaczymy, ale okej. Jakbyśmy te rzeczy zrobili i byłyby dobrze zrobione i działały, to monitor wydajności na poziomie reguł uważam byłoby fajne dla serwisantów. Że wchodzą, no i AI im mówi, słuchaj, wczoraj ktoś zepsuł regułę i ona teraz zamula.

**Janusz Bossak:** Znaczy, ja już tutaj z Mateuszem rozmawiałem właśnie o dokładnie o tym rozmawialiśmy. Już wielokrotnie już rozmawialiśmy, żeby trzeba, no bo zaczęła się dyskusję od analizy logów. Ja mówię, Mateusz, no dobra, no to patrzysz na takie logi, zapisy w logach, ale od razu powinien sobie ten AI uświadomić, że skoro się coś pojawiło w logu, to powinien zacząć szukać przyczyny tego, tak, czyli jeżeli w logu jest napisane, że reguła nie działa, no to sprawdź, czy przypadkiem ktoś nie ostatnio nie zmieniał czegoś regule, tak.

**Przemysław Sołdacki:** Bo to człowiek wyczai.

**Janusz Bossak:** Tak.

**Przemysław Sołdacki:** Tak, czyli jest jakiś algorytm rozwiązywania problemu i żeby to dobrze działało i przede wszystkim trzeba wiedzieć, który problem w tym rozwiązywać, bo to, co mogłoby robić, znaczy zanim to trafi do AI i to musimy przygotować, czyli na przykład wyciągamy statystykę z ostatnio nie wiem, dzień, tydzień i miesiąc, tak w różnych perspektywach, co najbardziej zamula serwer albo co generuje najwięcej błędów. I te zestawienia dajemy do AI. Dodatkowo wyciągamy dane, które czy te reguły, które tam się pojawiają, były zmienione w ostatnim czasie i to informacje też zbieramy i przekazujemy do AI i dajemy wytyczne, jak się powinno tego typu problemy diagnozować. Dajemy do AI, ale mówi, dobra, to ja chcę sprawdzić tę regułę. I wyciąga reguła, jest sprawdza, co tam zostało zmienione, bo mamy w historii, co zostało zmienione. Więc my musimy i algorytmicznie zebrać dane i dać wytyczne do AI, jak to robić, bo to jest znowu ten sam temat. Dla mnie standaryzacja obsługi, czyli którykolwiek konsultant się do klienta nie zalogował, to dostanie na tacy, że tak powiem, zrobione śledztwo, tak jak się powinno robić śledztwo, nie tak, że tylko Piotrek Buczkowski umie, tylko że już każdy będzie to umiał. Więc to bym to dał i to możemy sobie i taki profiler to jest. Też ciekawy temat, że jeśli reguła ci się wysypuje, to robić co do linijki dostał, gdzie się wysypuje i w którym miejscu na zamula. To jest zostawienia, a tu jest tylko prace koncepcyjne, ja może, że bez słowa taki manager. Bo to nawet mamy gdzieś wpisane chyba w dokumentacji. Tam dobrze pamiętam.

**Janusz Bossak:** Nie jest, znaczy tu Piotr się strasznie upiera, to nie jest debugger i nigdy nie będzie. Bo to nie jest dość śledzenie na bieżąco tego, co się dzieje. To jest tylko analiza.

**Przemysław Sołdacki:** Tak, post factum.

**Janusz Bossak:** Znaczy, które się zdarzyły?

**Przemysław Sołdacki:** Post factum, zgadzam się, ale to jest debugger, który odpala, odpaliła się reguła i możesz nie zatrzymujesz realizacji.

**Janusz Bossak:** To nieźle. Analizator.

**Przemysław Sołdacki:** Analizator, jak zwał, tak zwał, dobry. To już daje mi jakiś obraz tego roadmapy, którą my możemy. Zresztą te zmiany ja to zrzucam na koniec, bo nie postrzegam tego jako czegoś, co mi zwiększyć efektywność, ale okej. Dobra, to jakoś mamy to ogarnięte. No to jest mnóstwo znaków zapytania, mnóstwo rzeczy, które trzeba będzie sobie po prostu dyskutować. Dzień dobry, czy coś my jeszcze bez coś, jakbyśmy się pojawił, ale mi uciekła. Dobra, wiesz co, zostaną się czy zrobić takie spotkanie, gdzie my tam nie wiem w Warszawie, skoro już będziesz kogoś ciągnąć, żebyśmy sobie pogadali, bo pewnie i Mateusza, Daniela ma, znaczy Mateusza Kołakowskiego i Mateusza Kisiela, też zresztą Piotra Buczkowskiego byśmy sobie zrobili, to wiesz, zapytałam, kiedy ci tam wygodnie, jak w macie być chyba poniedziałek, wtorek, no to może nie wiem, środę jeszcze. To to byłoby wygodne. Słuchaj to. To tak to chyba tyle.

**Janusz Bossak:** Dobra.

**Przemysław Sołdacki:** No i tak już to tych 2 spotkań nie wiem, możecie nie robić, możecie, ale jak chcecie, to zróbcie, nie to napiszcie mieć z grubsza, gdzie jesteśmy.

**Janusz Bossak:** Przegadamy jest, dobra, okej.

**Przemysław Sołdacki:** Super, to dzięki, hej.


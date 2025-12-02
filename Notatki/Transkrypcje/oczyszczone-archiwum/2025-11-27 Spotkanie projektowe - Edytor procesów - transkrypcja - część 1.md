**Data spotkania:** 27 listopada 2025, 11:33 - część 1

---

**Damian Kaminski:** Bo ja też jestem. Ale szczerze, to bym się chyba wyłączył.

**Janusz Bossak:** Dobrze, możesz się wyłączyć, bo tutaj teraz rozumiem takie frontendowe tematy.

**Damian Kaminski:** Dobra, to dzięki.

**Janusz Bossak:** Dobrze, co mamy tutaj? Przemka nie będzie, bo na poprzednim spotkaniu też mówiłem, że Przemek Sołdacki ma jakiś wywiad i nie może uczestniczyć. On potem się zapozna z tym podsumowaniem. Gdzie jesteśmy? Kamil?

**Kamil Dubaniowski:** W tym edytorze ja w sumie nic nowego. To są niuanse, jakieś tam 3-4 zgłoszenia wrzuciłem wczoraj Przemkowi, takie bardziej na zasadzie, żebym miał co robić. Te co mieliśmy już omówione, chciałbym na przyszły sprint spisać zmiany w tym prawym panelu ustawień pola. Bo tam jest dużo do poprawy, chociażby układ, kolejność tych ustawień. Jakieś mamy na samej górze, z których mało kto korzysta, a te istotne są gdzieś na samym dole. Więc ustawienia pola w edytorze graficznym i w tym edytorze listy, to jest wspólny komponent. Chciałbym, żeby był jak najbardziej poprawny, no ale to na przyszły sprint. Na ten sprint Przemek, pokażę, już pozmieniał nagłówek tego panelu. Takie wybierałem zadania, które wiem, że nie musimy ustalać, nie uzgadniać, ogólnie słuszne. A te prace nad prawym panelem: co tam zmienić, gdzie co przenieść, czy usuwać te zakładkę, co ty Janusz tam bardzo za nią optujesz, czyli te zakładki, gdzie są właściwie dwa przyciski? Tylko czy jakoś to przerabiać czy nie, tego nie podejmowałem. Zostaje jak jest na razie. I tyle. Filip działa cały czas z tą listą pól, więc tam też sporo zadań wyjdzie w tym sprincie. Ja więcej nie robię. Czy coś z modelem graficznym, czy z listą reguł, no to tego nie przyzna. To tematy Damiana i na razie odłożone, jak rozumiem. To już było. Przemek, to publikowałeś tak, jak to pamiętam?

**Przemysław Rogaś:** Tak, tak. W ogóle tutaj też wcześniej zmienił się layout, tutaj właśnie przyciski dodawania sekcji.

**Kamil Dubaniowski:** Tak, czyli obsłużyliśmy opcję dodawania sekcji z edytora graficznego pomiędzy sekcjami. Czyli nie trzeba już lecieć na sam dół, żeby dodać nową sekcję, tylko dodajesz sekcję w tym miejscu, gdzie jest ona ci potrzebna. Utrzymaliśmy ten schemat, że nie widać tego, trzeba najechać, więc to jest trochę taka wiedza, że trzeba wiedzieć, że w to miejsce trzeba trafić, ale.

**Janusz Bossak:** Się szybciutko zorientuję. To bardzo ładnie.

**Kamil Dubaniowski:** Tak, tak, tak. Natomiast nie chcę tego na stałe pokazywać, bo zaraz będą uwagi, że jest nieczytelnie. Także jest w ten sposób. Pozaokrąglaliśmy już te sekcje, tak jak jest na formularzu, chociaż tu stosujemy piątkę. Na formularzu jest jeszcze trójka, no ale też nie chcę tego formularza teraz prawdziwego sprawy przerabiać. Niech tam zostanie trójka. My tu już stosujemy piątkę, tak jak ma być. Zgłosiłem też zadanie dla Filipa, żeby ujednolicił, bo on tam gdzieś ósemki nawet stosował, żeby poprzerabiał to na piątki. Zaokrąglenia rogów. A sekcja nie ma ikony, to prawo świeckie. Wiem, tak zmieniliśmy, że w nagłówku tej sekcji jest ikona nawiązująca do typu tego pola, a tutaj nie pojawia się tak jak do tej pory nazwa typu pola, bo to było mało intuicyjne. Zwłaszcza jak ktoś zrobił coś takiego, to nie wiedział, jakie pole edytuje, no bo była tylko nazwa. Nie wiem, tam "Tabela", bo był typ pola tutaj wpisany. Ten w ogóle nagłówek się też skontrolował, czyli w ogóle nie było go widać. Skanowaniu to też zmieniliśmy. Ujednoliciliśmy wygląd tego prawego panelu, czyli on jest już też takim boksem, tak jak na liście u Filipa. Wcześniej on był takim tutaj elementem na całej wysokości strony. Czyli wchodziłaś tutaj do tego poziomu, to dla mnie było nieintuicyjne, bo na przykład jak wszedłem sobie w ten panel, no to wszedłem tu "Powiększ/Zmniejsz". A teraz jak w tym powiększeniu otworzyłem prawy panel, to on wychodził aż tutaj do góry. Ten przycisk mi się przesuwał w lewo i tu miałem tego X-a. Więc uznałem, że nie powinniśmy przesuwać tej nawigacji, no bo jak tutaj kliknąłem powiększenie, to też tutaj spodziewam się kliknięcia pomniejszenia. A tutaj mi się wtedy ładował ten panel prawy i ten przycisk mi uciekał gdzieś tam. Także no jakieś tam niuanse mówię, robimy.

**Janusz Bossak:** Mogę jakąś jedną uwagę? Ten na hover pojawiający się "Dodaj sekcję" i "Dodaj wiersz". One są tego samego koloru. Nie wiem, czy może sekcje zrobić innego koloru, żeby było widać dodaję wiersz czy sekcję. No jest napis wprawdzie, ale tak dalej, taka drobna jest taki wizualny.

**Kamil Dubaniowski:** Jasne. Tak. Okej, dobra, pomyślimy coś z tym. Tutaj Przemek chyba do usuwania wierszy jest czerwony. W ogóle tak to jest bardzo mała różnica, więc może w ogóle oderwać tę kolorystykę tą do dodawania od naszej systemowej. Bo tu jest tak minimalna różnica między tymi kolorami, że mogłoby to być, że to jest po prostu zielone, no bo dodajesz coś nowego. Ale to pomyślę.

**Janusz Bossak:** Dobra. Czyli poczekaj, tutaj, czyli jak ktoś by miał inną kolorystykę, na przykład różową, miałby czerwoną, to miałby czerwone tutaj?

**Kamil Dubaniowski:** Tak, to będzie czerwoną "Dodaj wiersz". Tak, więc to wydaje mi się, że warto by było oderwać pewnie o tej systemowej. Dodanie nawiązujemy do zielonego, tak jak wszędzie, mniej więcej to wygląda. Ale dobra, okej. Jest do przemyślenia temat.

**Janusz Bossak:** No to do przemyślenia. Ale wygląda to ładniej. Druga drobna uwaga moja. Nie wiem, zaraz te marginesy, które są. One tak były tak dookoła tych sekcji w ramach tej środkowej części i dookoła.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** W prawym panelu są większe niż ten margines, który jest z listą pól. Ta lista pól jest taka, jak widać bardziej przyklejona do góry, jest mniejszy margines na topie i mniejszy margines po lewej, po prawej. Czy to jest zamierzone, czy tak po prostu, bo jest. Znaczy, ja widzę po prostu to nie, że znaczy potrafię.

**Kamil Dubaniowski:** Tutaj tak mówisz o tym, tak?

**Przemysław Rogaś:** Znaczy, no ja właśnie pisałem o tym Kamilowi, gdzie muszę to powiększyć, żeby ten przycisk zmieścić, nie?

**Kamil Dubaniowski:** Tu by trzeba było zwiększyć. Tak, tak, tak, więc no to ja się zgodziłem świadomie. Pytanie, czy to wtedy powiększać? Tak? No bo miejsce potencjalnie mamy, to nie mało.

**Janusz Bossak:** Trochę znaczy, mam trochę taki dyskomfort, że to jest nierówno.

**Kamil Dubaniowski:** Okej, okej. Tutaj też widać, że po zwinięciu ten margines jest większy, więc można by było pewnie też do tego poziomu to zdjąć niżej, tutaj to powiększyć ten.

**Janusz Bossak:** Minimalny, ale nie upieram się, nie upieram przy tym.

**Kamil Dubaniowski:** Tak trochę. Okej. Dobra, co jeszcze?

**Janusz Bossak:** Co tam jest, jakiego. Pokaż o tutaj właśnie, to co to jest?

**Kamil Dubaniowski:** Tak, to jest ustawienia, które Piotr wnioskował, czyli żeby też nie domyślnie, ale na życzenie jak coś serwisowo szukamy to, żeby włączyć sobie szukanie też po tych atrybutach technicznych. No i w tym sprincie, bo to już było po tym ID pola i po nazwie kolumny w bazie danych, doszło jeszcze po GUID-zie. I po prostu jak to włączę, to teraz powiedzmy, że to pole ma tam jakiś GUID "54e", no to jak zaczynam wpisywać "54e", to mi podpowie to pole. W sumie byłem w jego ustawieniach, więc nic się nie wydarzyło, ale jakbym zamknął i wpiszę "54e" i wybiorę, to automatycznie mnie do tego pola przekieruje, otworzy jego ustawienia.

**Przemysław Rogaś:** Teraz też mi się przypomniało, że w sumie mnie tam Piotr chciał jeszcze, żeby tego GUID-a w modalu edytować, nie wiem czy.

**Janusz Bossak:** Państwa.

**Kamil Dubaniowski:** Edytować, tak, to prawda, nie rozpisałem tego. No dobra, to jeszcze może zdążymy zrobić.

**Janusz Bossak:** No i super.

**Kamil Dubaniowski:** Okej, co wam jeszcze? No.

**Janusz Bossak:** Z regułami coś poszliśmy do przodu jeszcze nie, no to dopiero wiemy.

**Kamil Dubaniowski:** To Filip tak to co na razie mówiliśmy, wątpię już tam się z tym wyrobił. Wiem, czy coś tam Przemek z tobą konsultował Filip. Ale z tymi regułami ja nie robiłem projektu pod docelowe rozwiązanie. Na razie robimy to zapewnienie kompatybilności, czyli żeby dało się edytować reguły tabeli. Jest ten przycisk. Uruchom tak to co ci pokazywałem, ale on otwiera jeszcze po staremu, czyli te terminy nie wiem. No i w tym kontekście listy. Wydarzyło się na pewno więcej, ale ja już tak szczegółowo nie pamiętam co było, a co dodawaliśmy. Przemek wnioskował, żeby zmienić tutaj sposób wyboru liczby kolumn, bo była to dropdown lista, żeby było spójne z edytorem graficznym, więc teraz w ten sposób sobie ustawiasz, ile chcesz kolumn w sekcji.

**Janusz Bossak:** Mhm.

**Kamil Dubaniowski:** Co tam dalej? Dodaliśmy tego searcha też jako wspólny komponent, bo on był, ale teraz jakby zmiana Przemka. No jak pójdzie dalej, no to będzie też u Filipa, przynajmniej tak powinno być, bo tutaj jak widzicie, jeszcze tego szukania po ID na przykład nie ma, ale to po prostu rozumiem, że jeszcze nie było do oficjalnej paczki wydania, więc Filip po prostu jeszcze tego u siebie nie ma. Rozpisałem Filipowi zadanie na to dodawanie pól i sekcji tak jak gdzieś tam projekt zrobiliśmy.

**Janusz Bossak:** Mhm.

**Kamil Dubaniowski:** Gdzie jeszcze też tego nie ma?

**Janusz Bossak:** Mhm.

**Kamil Dubaniowski:** A zmieniło się to, że ja najeżdżasz na pole, to robi się wokół niego ramka, bo wcześniej to było takie nieintuicyjne, że coś możesz tu kliknąć i edytować inne na hover. Teraz dodaliśmy te ramkę podobnie tutaj, czyli sugerujemy, że coś możesz edytować. Tak samo tu tam, gdzie się da. Tutaj jeszcze pewnie do dopracowania, bo niektórych pól jakby jak tabela, no nie ma wartości domyślnej, więc pewnie trzeba by coś tutaj zasugerować, że tu się nic nie da kliknąć. Na razie po prostu ramka się nie pokazuje, ale to raczej nie jest wystarczająco intuicyjne na przykład dla pola odnośnika. Tak, no nie mamy wartości domyślnej. W sumie powiedzmy, że ktoś mógłby pomyśleć, że dlaczego i będzie klikał, ale.

**Piotr Buczkowski:** Nie, nie, nie róbmy tego.

**Kamil Dubaniowski:** Trzeba pewnie dodać. Znaczy tylko chcę pokazać, że się nie da, tak czyli.

**Piotr Buczkowski:** To ponad dla pola Odnośnik nie ma po prostu wartości domyślnej.

**Kamil Dubaniowski:** Tak, tak, ja nie chcę dorabiać dla pola Odnośnik wersji domyślnej, tylko chcę pokazać, że tu się nie da kliknąć.

**Piotr Buczkowski:** Choć tak samo jak dla pola Słownik podrzędny też nie ma wartości domyślnej.

**Kamil Dubaniowski:** Tak, no to tam gdzie nie ma, po prostu nie pokazuje się ta ramka i wydaje mi się, że to jest za mało. Ktoś może uznać, że to jakiś błąd i będzie tu usilnie klikał, tym bardziej że kurs.

**Piotr Buczkowski:** No to według mnie nawet nie powinno być tej kolumny.

**Janusz Bossak:** No tak, no ale kolumna jest jakby wspólna dla wszystkich tak.

**Kamil Dubaniowski:** Tak.

**Piotr Buczkowski:** Ale nie powinno być te kolumny w ogóle dla wszystkich.

**Kamil Dubaniowski:** Okej, znaczy no wiecie jak to się skończy. Była i zaraz będzie "a czemu nie ma?" i teraz ja nie wiem czy mam tu ustawioną wartość domyślną, muszę wchodzić do ustawień każdego pola i sprawdzać, bo mi się coś tam nie działa, więc.

**Piotr Buczkowski:** To ewentualnie tylko do wyświetlania tak edycja w ustawieniach pola. Tak w ustawieniach Polak. Przepraszam nie systemowych.

**Kamil Dubaniowski:** Do odczytu. Systemowy znaczy ustawienie w pola.

**Janusz Bossak:** Może tak?

**Kamil Dubaniowski:** Okej dobra, no to Filip się tam ewentualnie niepotrzebnie narobił.

**Piotr Buczkowski:** I wtedy wtedy na przykład?

**Kamil Dubaniowski:** Dobra no jest tak jest jakaś.

**Piotr Buczkowski:** Jest pusto, nie ma dostępny, no bo dla tego typu nie ma dostępnego tego tak. Tak samo dla tabeli nie ma domyślnej wartości, tak.

**Kamil Dubaniowski:** Tak, tak, tak mówię, ale pól tam rozpisywałem to wiele pól nie ma takiej wartości domyślnej. Dobra, to najwyżej jeszcze to przegadamy, żeby usunąć stąd edycję online. Zgłosiłem Filipowi, nie wiem czy już weszło, weszło tak, czyli żeby no niestety mieliśmy to i spodziewam się, że będą o to się upominać, żeby można było potencjalnie sobie wyświetlić te dodatkowe kolumny. One domyślnie są wyłączone, bo to nie jest zawsze ci potrzebne. To bardzo rzadko sprawdzasz, więc one domyślnie są wyłączone, ale wyłączyć sobie można. Co więcej. Nie pamiętam szczerze mówiąc, musiałbym pewnie zajrzeć tam na Filipa tablicę, ale no wiecie, nie będzie tu nic spektakularnego. Dodaliśmy ikony, żeby zwiększyć te czytelność. Jednym z większych zadań, ale jeszcze nie rozpisanych. To jest decyzja właściwie tam chyba z wczoraj to pewnie na przyszły sprint jest decyzja, że wracamy do starej nawigacji, czyli tabela nie będzie rozwijana, nie będziemy wchodzić w głąb tabeli na widoku listy, tylko po prostu będzie pole tabela, a jak będę chciał wejść do pól w tabeli, to będzie strzałka w prawo i po prostu tabela mi się załaduje z polami tej tabeli. Bo tak jak w starym edytorze, tak jak tutaj to właściwie działa tak, czyli jak chcę wejść do tabeli to sobie przez nawigację albo szukam tego pola na formularzu wchodzę i widzę już wtedy listę tylko tych pól w tej tabeli. Bo to jest fajne jak jest jedna tabela, a jak wejdą zagnieżdżenia, to to już no po prostu będą narzekać ludzie, żeby było lepiej, bo przy dużych zagnieżdżeniach nie wiadomo co jest tabelą, nie wiadomo co jest sektorem. Nie wiem jeszcze jak tu by doszła kolejna tabela, kolejne sekcje, no to uważam, że tamta koncepcja była po prostu lepsza. A też no jakby pracując na tym widoku, no nie potrzebujesz tego, żeby wiedzieć jakie tam są pola, jak chcesz wejść, żeby coś edytować tutaj tabeli, no to wejdziesz do środka. Ta koncepcja zostanie w matrycy, no bo tutaj jak najbardziej to ma sens. Niestety jakby to zagnieżdżenie może nie będzie super czytelne, ale tutaj chodzi o sprawdzenie i ustawienie uprawnień, a uprawnienia są zależne od tego, jakie jest uprawnienie wyżej. Czyli jak tabela ma jakieś uprawnienia a sekcja dziedziczy no to tutaj niestety musimy takie zagnieżdżenia robić, żeby to pokazać. No ale tutaj też jest o wiele mniej elementów klerykalnych, mamy więcej miejsca, jakoś to możemy lepiej włożyć niż tutaj, gdzie już jakieś tam akcje się wyświetlają, dojdzie jeszcze ten plus do dodawania nowego pola w tym miejscu i tak dalej i tak dalej, więc żeby zwiększyć czytelność pewnie na przyszły sprint z tego niestety się wycofali.

**Janusz Bossak:** No i git.

**Kamil Dubaniowski:** Tyle tam walczymy trochę z tą tabelą, no bo tutaj zgłosiłem chociażby, że za bardzo to tak agresywnie, nie ma żadnej animacji wyświetlenia tych dodatkowych kolumn z tłumaczeniami. No ale Filip coś tam kombinował i chyba nawet coś mi zaproponował, że coś na kolumnach będzie mógł zadziałać, ale na razie widzę, że jeszcze działa. Postawiono także tak jak mówię, nie ma tutaj rewolucji, już nie będzie rewolucja, to będzie sposób dodawania puli sekcji. No bo na razie jest tak, sekcji w ogóle jeszcze nie ma. No i druga rewolucja, to będzie to, że nie będzie tego zagnieżdżenia wejścia do tabeli z tego widoku. I ludzie, jaką możemy obgadać w sumie teraz tak bardziej designowo. To jest to tak, Przemek jak się wstrzymał z tym i w sumie dobrze w necie to ustalić przełączę tę tabelę na chwilkę widok pod formularza i teraz zauważcie, że tutaj jak kliknąłem tabela to otworzył mi się prawy panel z ustawieniami tej tabeli, kliknąłem sobie w pole, tabela, ustawiłem ustawienia tej tabeli, natomiast jak tabela jest w formie po formularza to kliknięcie tutaj w to pole, bo tak naprawdę to jest odzwierciedlenie, że takie pole tabela jest w formie pod formularza, wchodzi mi do tej tabeli. I to jest dla mnie trochę takie pomieszanie, no bo jak jest pole tutaj to klikam i otwierają mi się jego ustawienia, ale jak jest pole tutaj w lewym panelu, bo jest widok pod formularza, to kliknięcie w to wchodzi do środka. Moim zdaniem nawigacja to jest tu. Jak chcę wejść do ustawień tabeli, to nawiguje sobie tędy, a tutaj po prostu. No pokazujemy ci jak ta, jak to pole będzie wyglądało na realnym formularzu, że będzie tutaj z lewej, ale kliknięcie w to pole nie powinno mi wchodzić do tej tabeli, tylko powinno otwierać prawy panel ustawień tej tabeli.

**Janusz Bossak:** Czy powinno jedno i drugie?

**Kamil Dubaniowski:** Znaczy tak robi teraz, no ale teraz, jeśli. Jeśli to przestawię z powrotem, czekajcie na tabele.

**Janusz Bossak:** No i bardzo dobrze robi.

**Kamil Dubaniowski:** Na tabele, no to dlaczego ten widok? Wracam na formularz główny, jak kliknę tutaj w tabelę to dlaczego nie wchodzi mi do tej tabeli? To jest jakby to samo, tak naprawdę tylko w innym widoku. To tylko otwiera prawy panel, więc idźmy w jednym kierunku, albo to jest od razu otwarcie prawego panelu i nawigacja, czego ja nie chcę, bo jak wchodzisz do środka. No to powinieneś mieć prawy panel pól, które tam są, a nie prawy panel tej tabeli. Prawy panel tej tabeli jak chcesz oglądać i coś zmieniać na.

**Janusz Bossak:** Przypadek no to jest szczególny przypadek, no bo co ma, co miałoby się stać? Teraz weźmiesz ten formularz główny, zamienisz na tabelę. Wybierz.

**Kamil Dubaniowski:** No to to jest też zmiana, którą chcę właściwie trochę tak bez konsultacji, ale no powinno zamykać tym prawie panem.

**Janusz Bossak:** No i całym domy.

**Kamil Dubaniowski:** Bo teraz no bo teraz.

**Janusz Bossak:** Zamknęłoby prawy panel, zawsze dla mnie jest to okej no.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Znaczy ja rozumiem, no.

**Kamil Dubaniowski:** W tabeli dokładnie i tak samo w sumie było w starym. Nie możesz ustawiać ustawień tabeli będąc w tabeli.

**Janusz Bossak:** Będąc teraz w tym widoku, nie możesz wrócić do prawego panelu tabeli. No tak, tak tak.

**Kamil Dubaniowski:** A tutaj będzie to takie, no miałem i teraz jak do tego wrócić, więc ja bym zamykał. Wchodzisz w nowy kontekst. No i teraz wybierz co tu chcesz edytować, tamto już zniknęło jak chcesz edytować tabelę, no to wracasz tam gdzie ta tabela jest. I sobie tu jeszcze raz klikasz i tu edytujesz ustawienia tabeli, a jak już wchodzisz do tabeli no to edytujesz co w tej tabeli tam w środku. Więc jakby nawet gdzieś tam sobie z czatem dyskutując o tym. Powinniśmy się zdecydować na jedno i ja się z tym zgadzam, że ten element to jest wizualizacja, nie nawigacja. Nawigacje obsługujemy tędy albo właśnie przez jakieś tam dedykowany przycisk, że ja wchodzę do środka, a teraz decydując się, że jakieś tam jeden wyjątkowy element jest wizualizacją i nawigacją. No to robimy zamieszanie. Więc ja nawet dla tego widoku chciałbym wprowadzić zmianę, jest już rozpisana nawet, ale Przemek wstrzymał implementację, że to jest nieklikalne. To jest jak najbardziej klikalne, ale efektem jest otworzenie prawego panelu tego pola, bo to jest pole. Tak naprawdę to jest pole typu tabela, inaczej zlokalizowane, to ja się w prawym panelu ustawień jak chcę wejść do środka, to albo ten ryk, albo przez ten przycisk, że wchodzę do środka i chce edytować pola tej tabeli. Tego pod formularza to by było wtedy tylko wizualizacja, nieklikalna, to jak najbardziej możemy kliknąć. Efekt na hover pewnie powinien być taki sam jak tu, tu jeszcze nie ma, ale gdzieś tam w Przemka już to jest zagrożone, że jak najeżdżasz na nazwę to się podświetla lekko na pomarańczowo i tu tak samo. Żeby zasugerować, że to jest sport?

**Przemysław Rogaś:** Nie czy ten hover, no to ja bym zostawił tak jak jest w każdym menu menu nie no bo to jest patrzeć nie.

**Kamil Dubaniowski:** Okej. No dobra, no to już ciebie szczegół, ale żeby to nie było klikalne, no bo teraz to tak jak mówię, to jest trzeci element nawigacji. Że ja mogę się tu przełączać między tematem i idźmy w jedno, że to jest wizualizacja, nie nawigacja. To pokazuje ci jaki jest efekt. Pokazuje ci lokalizację, konkretnie gdzie to pole teraz jest, ale nie wchodzisz tędy do środka. Jesteś w kontekście formularza głównego i tu się baw ustawieniami, jak chcesz wejść głębiej, to albo przez przycisk, albo przez tą tutaj. A to Przemek też zmienił. Jeszcze w sumie opowiedzieliśmy o tym, zmieniliśmy, żeby to była struktura drzewo, żeby nie było takiego jak tutaj, że pokazujemy. To jest teraz równie takie już sekunda. Żeby tu nie było takich jakby zagnieżdżeń, że cała ścieżka tylko po prostu mamy drzewko już teraz. Po prostu widzi, że to jest podsiad pod sobą, to jest jakieś tam. Formularz jako równy z formularzem głównym. Jak chcesz tu to idziesz tu, że też jakaś tam zmiana, no ale tak jak mówię to jest teraz.

**Piotr Buczkowski:** Ale za zdobycie co masz? Tylko formularz główny.

**Kamil Dubaniowski:** Domyślny formularz główny domyślnie. A to są tabele w tym formularzu.

**Piotr Buczkowski:** Do tabel domyślnie nie widzisz?

**Kamil Dubaniowski:** Nie, tu są tabele.

**Janusz Bossak:** Ale jak jest tabela w tabeli to co będzie?

**Kamil Dubaniowski:** No to będzie tabela i pod możemy dodać.

**Janusz Bossak:** Będzie wcięta.

**Kamil Dubaniowski:** Z okazji przetestujemy.

**Piotr Buczkowski:** Chodzi mi o to, żeby to tabele pierwszego poziomu domyślnie były widoczne tak bez wycięcia, bo.

**Kamil Dubaniowski:** Tak znaczy, dlaczego one są elementem formularza głównego?

**Piotr Buczkowski:** No tak, no no. Jeszcze to byście nie widać ich tak?

**Kamil Dubaniowski:** Domyślnie są wszystkie widoczne rozwinięte z tym wcięciem. Wszystko jest rozwinięte domyślnie, takie bo przynajmniej założenie.

**Piotr Buczkowski:** Ok.

**Janusz Bossak:** Ale nie rozumiem tego ostatniego, bo jest tam przewiń na sam dół.

**Kamil Dubaniowski:** Bo a to ja też o to pytałem Przemka, ponoć twoja decyzja, że jak coś jest w widoku, jak tabela jest widoku pod formularza?

**Janusz Bossak:** O tak.

**Kamil Dubaniowski:** To jest wtedy na równo z formularzem głównym, czyli nie jest jakby.

**Janusz Bossak:** No okej.

**Kamil Dubaniowski:** Dzieckiem tylko oba stanowią teraz, że są rodzicem, bo ty.

**Janusz Bossak:** No technicznie jest dzieckiem, ale.

**Kamil Dubaniowski:** Tak tak, no ale wizualnie miało być jakby na równo. A jak jest tabelą, czyli konkretnie elementem tego formularza? No to jak jest jakby rodzic dziecko, część tego, która jest rozwinięta to myśle. No bo nawet w tym wypadku tak jakby jakieś zagnieżdżenia no to w tej starej wizualizacji to robiło się już po prostu mega długie, jakieś tam cała ścieżka była pokazywana.

**Janusz Bossak:** No no. Nie no to ten układ tego drzewka jest dla mnie okej.

**Kamil Dubaniowski:** Co tam widzę widzę.

**Janusz Bossak:** Nie bardzo jeszcze skumałem może się rozproszyłem przez chwilę jakbyś wrócił teraz tak wybierasz tą tabelę z tego menu tutaj, tak.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** I to, co jest twoją? Kliknij. Techniki no niech się wybierze.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Yy. A no właśnie to nie nie dobra, to chodziło mi o tą tabelę w lewym teraz 100 o to tą dobierasz to mówię.

**Kamil Dubaniowski:** Mhm. Tu tak.

**Janusz Bossak:** I co według teraz twoich założeń ma być, bo teraz się pojawił i formularz i prawy panel, ale to coś mówię, że to ma się inaczej zachować.

**Kamil Dubaniowski:** No teraz już widzę problem, bo ja już jestem gdzieś tam w środku w zagnieżdżeniu. I jak kliknę to. To tak naprawdę widzę jakieś tam formularz tabeli pierwszej, a kliknę tutaj i zostanę w tym formularzu tabeli pierwszej, a będę miał prawy panel tabeli drugiej.

**Janusz Bossak:** No no no.

**Kamil Dubaniowski:** Ale znowu teraz jest. Zobacz, teraz też mamy taki bug, powiedzmy bug, w którym sobie wchodzę sobie. Czekaj, bo to chyba już jak zrobiłeś, że zamykamy ten panel tak, czyli na przykład jestem na polu tekstowe krótki tekst. To już chyba jest robione jak przejdę do tabeli a nie nadal jest. No i zobaczcie jestem w tabeli a mam ustawienia pola z głównego formularza, więc stąd też ta moja sugestia, żeby ten prawy panel od razu zamykać po zmianie kontekstu jak wchodzę do tabeli to zamykam prawy panel, no żeby tu nie pokazywać pola z nie tego formularza tak naprawdę. No to jest pole z formularza głównego. To pole. Dobra, jeszcze będę o tym myślał, no nie wiem mamy. Za dużo przypadków. Żeby w każdym było dobrze. Jeszcze chciałbym to menu sprowadzić poziom niżej, bo ona teraz też trochę tak zaczyna wyglądać, jak tutaj zlewa się trochę z tym elementem nawigacji, a powinno być bardziej elementem tu formularza. Tak naprawdę ta część to jest wygląd formularza. Środek. A tu są jakieś tam ustawienia, projektować szukanie. Szczerze to mam gdzieś tam na tapecie. Dobra no nie wiem, tak trochę trochę gdzieś tam wydaje mi się, że. Za dużo, ale nie mam pomysłu na to tekst. Nawigacja tu nawigacja, tu jeszcze nawigacja poprzez wejście w ustawienia tego pola tu i kliknięcie tu tak, czyli 3 sposoby wejścia do środka.

**Janusz Bossak:** Znaczy, wiesz, no, zbyt znaczy większa liczba możliwości nie jest zła, byle było intuicyjnie tak, no bo jeden będzie wolał tak, ktoś inny będzie wolał tak, to to miejsce.

**Kamil Dubaniowski:** Bo też w sumie tak naprawdę wiecie, ten moment nie jest realny na faktycznej sprawie. No bo ja nie wchodzę do tabeli, widzę tabelę po prostu więc możliwe, że ten panel powinien być tylko dostępny na poziomie formularza głównego. I wtedy znika ten problem, który teraz przed chwilką wyłapaliśmy, że jak już jestem na przykład w tej tabeli to mogę kliknąć tu i zostają mi ustawienia jakiegoś tam innego pola. Tak więc wtedy jeśli to by znikało w momencie wejścia do tabeli, no bo to nie jest elementem tabeli, to jest elementem formularza głównego.

**Janusz Bossak:** To jest tak, jakbyś zamknął ten lewy panel tak, czyli wchodzisz to tutaj z tabeli, a jednocześnie się wykonało to no kliknij tutaj. Dotąd na ten chleb to znaczy, on to zostaje tak, no teraz, ale w tym.

**Kamil Dubaniowski:** Gdzie to zwinięcie tak?

**Janusz Bossak:** W tej koncepcji, którą podajesz, to jak tutaj wybieram w tym menu rozwijanym tabela, to jakby rezygnuje na razie z tego poziomu formularza.

**Kamil Dubaniowski:** Mhm. Głównego, tak.

**Janusz Bossak:** Głównego, no bo jestem teraz, wszedłem w środek, tak jestem w tabeli.

**Kamil Dubaniowski:** Tak. Tak no i to to jest jakby rozwiązanie znaczy, wiecie, możemy po prostu wrócić do tej mojej koncepcji. To nie jest nawigacja, tylko to jest element, który ja klikam i ustawiam ustawienia tego pola, który występuje na formularzu głównym, a jak chce edytować zawartość tego pod formularza to muszę kliknąć w tamten przycisk edytuj pola formularza albo wejść do tego pod formularza z tego poziomu. No i powiedzmy, że to jest już o tyle spójne, że trzymamy się tej zasady, że to jest prezentacja efektu, a nie nawigacja. Ten ta część ekranu środkowa.

**Przemysław Rogaś:** Ale może być też sytuacja, że masz więcej niż jeden pod formularz i jakby dla po formularza to nie rozwiąże wtedy problemu.

**Kamil Dubaniowski:** Z prezentacją. No.

**Janusz Bossak:** Bo jeszcze masz tabelki w pod formularzu, nie?

**Przemysław Rogaś:** Bo jak wejdziesz w inny pod formularz, to wtedy tej sekcji nie możesz schować, nie? Nie wiem, ciężko mi to wyjaśnić.

**Kamil Dubaniowski:** Czyli chodzi o to, że na formularzu głównym mam 2 pod formularze różne.

**Przemysław Rogaś:** Tak, tak i wtedy, jak wejdziesz w pod formularz.

**Kamil Dubaniowski:** Dodam kolejną.

**Przemysław Rogaś:** To. Nie możesz tej sekcji zamknąć z wyborem pod formularza, bo.

**Kamil Dubaniowski:** A jak wejdę tu?

**Przemysław Rogaś:** Mhm.

**Kamil Dubaniowski:** No ale ja bym nie zamykał w sensie tutaj w tym momencie powinienem zostać na formularzu głównym, bo oba te pod formularze są elementem formularza głównego. Powinny mi się otworzyć po prostu prawy panel tego pod formularza.

**Janusz Bossak:** No tak, ale będę miał.

**Kamil Dubaniowski:** A jak już wejdę do środka tego, czyli do tabeli piątej, no to to mi znika. No bo po co?

**Przemysław Rogaś:** Ale jakbyś patrzę, ale jakbyś weźmy ten otwórz jeszcze raz jakbyś tam z tego selecta tego tri selecta nawigacji na przykład wszedł teraz do.

**Kamil Dubaniowski:** Tu.

**Przemysław Rogaś:** Yy tego pod formularza tabela 2.

**Kamil Dubaniowski:** Mhm.

**Przemysław Rogaś:** I teraz jesteś w tym formularzu i nie możesz zamknąć tego z lewej strony, tak samo jak w przypadku zwykłej tabeli. I jak klikniesz tabela 5 no to będziesz miał ustawienia tabeli 5 i zawartość.

**Kamil Dubaniowski:** Mhm. A dlaczego nie mogę zamknąć? W sensie to powinno się zwinąć. Ukryć w ogóle nie powinno być tego paska, bo jestem już w środku tego pod formularza, więc ustawiam zawartość tego pod formularza. Jak chcę coś grzebać w ustawieniach tego, no to muszę wyjść na formularz główny. Tak mieliśmy do tej pory.

**Przemysław Rogaś:** Mhm.

**Kamil Dubaniowski:** I tutaj możemy się jak najbardziej to wyświetlić z powrotem.

**Janusz Bossak:** Ja już się zagubiłem w tych równych.

**Kamil Dubaniowski:** Dobra, ja spróbuję, to może jakoś filmie gdzieś tam.

**Janusz Bossak:** Więc. No właśnie jeszcze Kamil jedną rzecz, żeby mieć w takiej tabeli 5, która jest teraz pod formularzem inną tabelkę, bo to jest możliwe, tak.

**Kamil Dubaniowski:** O tak.

**Janusz Bossak:** Więc tu, jakbyśmy dodali tabelę, to co się wydarzy?

**Kamil Dubaniowski:** No to wtedy po prostu tak wtedy wchodzę do do tabeli piątej. Tego nie mam, bo to nie jest element tabeli piątej, tylko formularza głównego. Mam tutaj to pole, tabela, no i po prostu jako kolejne pole, które mogę edytować z tego poziomu, zmienić jego ustawienia. A jak wejdę do środka.

**Janusz Bossak:** No i teraz kliknij tutaj i teraz jest już na tabeli jeden znaczy chodzi mi trochę o to, że ten poczekaj, bo teraz tam u góry właśnie ten napis, bo to co było kiedyś niby niefajne, ale jednak fajne wiedziałeś gdzie jesteś teraz masz tylko tabela jeden i nie wiesz gdzie jesteś.

**Kamil Dubaniowski:** Tak. Mhm. Wydaje mi się, że Przemek tutaj w takim wypadku powinniśmy rozwinąć tego breadcrumba o kolejne poziomy. Nie wiem, no bo to wręcz powinno być, że procesy wszystkie pola edytory graficzne tu powinien być, no bo jestem w tym miejscu jak się przełączy na listę, to tu powinna pokazać się lista. A jak schodzę jeszcze gdzieś tam do ustawień poszczególnych podformularzy? No bo nie wiem, czy chcemy kolejnego breadcrumba tutaj na tym poziomie.

**Janusz Bossak:** No właśnie, no no no może na tym poziomie tej tabelki. No tak naprawdę, bo tu jest ten breadcrumb.

**Kamil Dubaniowski:** Tak.

**Przemysław Rogaś:** Ale to teraz zniknęło jak dodaliśmy triselecta, bo wcześniej były strzałki tak jak na starym formularzu.

**Janusz Bossak:** Dokładnie dokładnie.

**Kamil Dubaniowski:** Tylko one, no co?

**Przemysław Rogaś:** Ewentualnie można wybór zrobić triselectem a wartość niech się wyświetla ze strzałkami.

**Kamil Dubaniowski:** Ze strzałkami tylko co to będzie się tak rozciągało w nieskończoność przez zagnieżdżenia, czy pokazywaliśmy na przykład pierwszej ostatni? No i też zaleta tego jest taka, że z tego poziomu mógłbym szybko tam wrócić sobie poziom wyżej poziom niżej, a tutaj i tak będę musiał rozwinąć selecta tylko mi powie jaka jest ścieżka.

**Janusz Bossak:** Znaczy ten breadcrumb u góry zupełnie nawigacyjny to nie nie pasuje mi za bardzo, no bo to do czegoś innego służy to jest taki pod brew.

**Kamil Dubaniowski:** Mhm, ok.

**Janusz Bossak:** Na tym poziomie on mógłby się zachowywać podobnie, tak jak mamy poziom, procesy u góry to tutaj byś miał poziom formularz główny.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** I tam można też kliknąć chyba w te procesy. I coś się wydarzy. Nie wiem, no trzeba to przemyśleć.

**Kamil Dubaniowski:** No ogólnie truć dobra to pomyślałem jeszcze ok. Dobra no. Z tego co pamiętam to chyba więcej to jest jeszcze zagwozdka tak co z tym robić. Ja postaram się to zaprojektować jakoś w figmie, może się uda i i będziemy decydować natomiast no mi ta konkluzja z dyskusji z czatem się podoba tak, że no albo prezentacja i na to się decydujemy, żeby pokazać efekt, jaki będzie widział użytkownik. Albo nawigacja i wtedy. Trzeba to rozgraniczyć jak wszystko jest do do tego i do tego, no to mamy takie problemy.

**Janusz Bossak:** Ja się muszę przepiąć na kolejne.

**Kamil Dubaniowski:** Moja też uciekam. Dobra, dzięki.

**Janusz Bossak:** Dzięki bardzo.

**Przemysław Sołdacki:** Zatrzymano transkrypcję.

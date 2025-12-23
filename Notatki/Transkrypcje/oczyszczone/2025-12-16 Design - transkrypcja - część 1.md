**Data spotkania:** 16 grudnia 2025, 11:09

---

**Łukasz Bott:** Daj mi dosłownie minutkę, nie rozłączają się?

**Damian Kamiński:** Cześć, dobrze, dobrze. No ja też dopiero co skończyłem, więc spoko. Ja w międzyczasie mam co robić, więc czekam na linii.

**Łukasz Bott:** To zaś odesłałem, tak, tak, ja tutaj w ten się ogarnie. Byłem jedną rzecz, chcę dokończyć.

**Damian Kamiński:** Dobra.

**Łukasz Bott:** No dobra, jestem gotów, jeżeli.

**Damian Kamiński:** No dobra, tylko ja nie jestem w żaden sposób od razu przyznaję przygotowany w kontekście tego, żebym coś tam przeglądał wcześniej, więc ty musisz powiedzieć, jeszcze raz mi przypomnieć, gdzie to jest i możemy po prostu to mówić. Myślę, a mamy nagrywanie włączone, dobrze, to się potem poprosi Janusza.

**Łukasz Bott:** Nie, no dobra, tu jest. Dobra. Dobry to. No właśnie, tak, tak, no to się weźmy przez to po prostu, gdzie to jest, tak? Którego czy dobra, to tak pierwsza rzecz, to raporty z te propozycje raportów systemowych, oczywiście z odpowiednimi źródłami są na developer MySQL AMODIT lokal.

**Damian Kamiński:** No. OK.

**Łukasz Bott:** A dokładnie tym folderze LD system reports model.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** I to jest pogrupowane tak jak dotyczy osoby te grupy, kategorie tych raportów systemowych, czyli tak statystyki procesów. Nie ma tłumaczenia zrobionego w słowniku, więc dlatego nie wyświetla, ale to jest, to są modelowe, więc one będą służyły ewentualnie później do testów jakiś taki właśnie, żeby po przeniesieniu na systemowe to, żeby mieć punkt odniesienia i zobaczyć. Wiesz, porównać podczas testów, tak, działanie. Taką mam intencję i gdzieś tam zgłoszenia, jak robiłem, to pisał, żeby tego, że można tę definicję.

**Damian Kamiński:** OK.

**Łukasz Bott:** To tutaj raportu, który tam jest, to sobie skopiować, a nie przenieść, tak, no bo potem kurtyny rozjeżdża się wszystko, tak, ale dobra, to jest generalnie tu i też linki do tych. A no i teraz tak generalnie, tak jak gdzieś tam kiedyś rozmawialiśmy. Zrobiłem to na zasadzie też dashboardów.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** To też jest opisane w tym dokumencie na wiki wewnętrznym. Rzucą tutaj jeszcze raz na czat.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** To jest link. No to macie i teraz tak. Zawsze jest link do dashboardu, czyli jest to pogrupowane tam. Najwyższy poziom to jest ten kategoria procesów, potem dashboard i potem, no i w ramach tego jest link po prostu do konkretnego dashboardu, tak, czyli możesz sobie tytuły są nazwy po prostu, tak jak są tytuły tych zawodów.

**Damian Kamiński:** Dobre, bym powiedział, że możemy nawet na tym zostać, bo ja bym powiedział, że najpierw określmy sobie zakres, nie wiadomo co nam jeszcze starczy czasu, bo mamy tak.

**Łukasz Bott:** Nie, no dobra, wiesz co, ale to wizualnie, skoro zrobiłem to wizualnie, pokażę, tak, wszystkie, tak, no to tam.

**Damian Kamiński:** No dobra, to zobaczmy. Dobra, czyli czasy procesowania spraw, tak.

**Łukasz Bott:** Dobra i teraz mamy tak? Procesowania spraw, ja go. I tutaj tak, on kiedyś on jest jeszcze do do do robienia, bo tak, bo mamy 2 rzeczy i ja tak jakby 2, 2 czasy. Ja tutaj przerobiłem to i na razie uwzględniłem. Tylko na razie dla spraw otwartych, to też troszkę wynikło z dyskusji z Danielem, dla spraw otwartych, czas przebywania w systemie, tak, a nie tego, ile czasu dana sprawa jest procesowana w sensie takim.

**Damian Kamiński:** Czyli ująłeś tutaj też sprawę otwarte, bo czasami zdarza się, że nie są zamykane, więc to jest wtedy.

**Łukasz Bott:** Tak, to jest, są to są.

**Damian Kamiński:** Tylko OK. Czyli, ale może inaczej.

**Łukasz Bott:** Według procesy tarczy.

**Damian Kamiński:** Czyli tu są ujęte, czyli jeśli jest powiedzmy proces, który tak naprawdę jest, nie wiem, matrycą, matrycą akceptacji, ale jest jednocześnie procesem, bo ktoś go nie chce ujawniać z jakichś powodów, to w zasadzie wtedy te matryce będą tutaj miały taką średni czas trwania, ile faktycznie tam jest wdrożony. Tak?

**Łukasz Bott:** Średnio to nie jest średni czas trwania, tylko średni czas przebywania w systemie, czyli od momentu utworzenia do momentu, w którym oglądasz.

**Damian Kamiński:** Do dzisiaj, mhm, OK.

**Łukasz Bott:** Na moment oglądania, przy czym domyślnie ze względu na ilość danych jest to przefiltrowany po bieżącym miesiącu, czyli on wyświetla tylko stan od dzisiaj poprzednie, nie bieżący miesiąc, tak, no po prostu. Licząc miesiąc, czyli oglądamy w tej chwili średni czas, średni czas przebywania spraw według procesów utworzonych w grudniu. Tak.

**Damian Kamiński:** No okej, no to to bym się do tego pewnie czepiał, bo 1 grudnia mamy wybrakowane dane, lepiej by było 30 dni, pewnie, nie.

**Łukasz Bott:** No to. No to pewnie może ostro poprzednie 30 dni, tak, no, no to to jest właśnie do do zaznaczenia.

**Damian Kamiński:** A nawet bym powiedział, no pytanie na ile to jest, że tak powiem, duże zwiększenie zakresu, bo żeby zebrać jakąś statystykę, to może kwartał powinien być. Tylko no nie wiem, jaki to ma wpływ, no ale OK. Czyli średni czas, który, czyli tak to nam daje.

**Łukasz Bott:** Średni czas przebywania, nie procesowania, bo czas procesowania to jest odrębny parametr liczony przez system.

**Damian Kamiński:** To.

**Łukasz Bott:** I on siedzi w tabeli case history, tak.

**Damian Kamiński:** Czyli średni czas to jest ile czasu sprawa?

**Łukasz Bott:** Ile średnio tutaj średni czas przebywania w systemie, czyli proces, czyli dobra, no na na przykład jakiegoś procesu, nie tych matrixa, bo nie ma danych. Hej, hej, aj, dobra, bądźmy sobie.

**Damian Kamiński:** No.

**Łukasz Bott:** Zobaczmy. Bo dobra, wszystkie jakieś takie dobre jest tylko jedna. Nie jest to policzone. Ile tych spraw jest, tak? No to inny spraw, dobra, number of days średnio 14 dni sprawy według procesu EIO faktury.

**Damian Kamiński:** No OK.

**Łukasz Bott:** Ten, który zostały utworzone.

**Damian Kamiński:** Ale to uwzględnia i otwartej, zamknięte czy tylko otwarte?

**Łukasz Bott:** Być może? Tylko otwarte, otwartych trzeba dorobić wersję dla zamknięte.

**Damian Kamiński:** Dobrze, czyli przebywania to znaczy ile czasu te sprawy wiszą? Jeśli one zostaną zamknięte, to ten raport nie prezentuje żadnych danych.

**Łukasz Bott:** Od momentu. Tak. Tak. Więc tutaj pisza była ewentualnie dodać zakładki dla zamkniętych, nie, chyba że chcemy dodać filtr, tak.

**Damian Kamiński:** OK.

**Łukasz Bott:** Otwarte, zamknięte, no.

**Damian Kamiński:** Rzeczy. A czy da się to zanegować na jednym procesie, na jednym raporcie?

**Łukasz Bott:** Dachy.

**Damian Kamiński:** Znaczy inaczej, jaką to niesie wartość dodaną? O tak, tak, jaką to niesie wartość dodaną dla czytającego? Co mu to mówi? Bo od tego bym kontekstu wychodził, czyli tak zakładamy, że sprawa nie dobiega końca z jakiegoś powodu, albo takie są założenia procesu, albo...

**Łukasz Bott:** Da, da, da, bo tu.

**Damian Kamiński:** To się zatrzymało i teraz to jest w dodatku średnia, albo no właśnie i teraz.

**Łukasz Bott:** No.

**Damian Kamiński:** To. Może inaczej, porównam to teraz do spraw zamkniętych, jeśli takie samo założenie, czyli średni czas procesowania spraw zamkniętych. To to może wpłynąć nam OK. Patrzymy, gdzie mamy długie procesy, czyli co, którym procesem warto się zająć w kontekście usprawnienia i to jest zaleta tamtego raportu. Teraz pytanie, jaka jest zaleta tego raportu, jaką my jak my to przedstawimy? Co to daje, co można z tego odczytać takiego sensownego?

**Łukasz Bott:** No to opis biznesowy wygenerowany przez AI i pozwala na porównanie efektywności poszczególnych procesów, identyfikacji tych wymagających optymalizacji. No głupoty, dobra. Wiesz co?

**Damian Kamiński:** No. Średnią liczbę dni. OK. Tylko w zasadzie może inaczej. Jeszcze powiem, jeśli założenie jest takie, że proces jednak dobiega końca, czyli te sprawy się kończą, a nie ich założeniem jest takie, że one po prostu trwają bez końca w systemie, bo wtedy nic tu nie usprawnimy. To w zasadzie te 14 dni przeniesie się na zestawienie spraw zamkniętych. Tak.

**Łukasz Bott:** Dokładnie, tak, dokładnie, tak, jeżeli byliśmy dzisiaj zamknęli, tak, no to tak.

**Damian Kamiński:** Dobra.

**Łukasz Bott:** Byłabym otwarte albo zamknięte, no. I teraz tak, wiesz co, ten proc. Ten raport mógłby być pomocny. Tutaj Daniel właśnie zgłasza coś takiego, że często klientów interesuje następująca sytuacja.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Sprawa trafiła, została utworzona w systemie. Zaczyna się jej czas, przebywanie w tym systemie, tak.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** I na przykład, no to okej, powiedzmy jak ona sobie leży? Dzień 2, może 3, to jeszcze jest OK. Ale często właśnie 5. Potrzebuję raport, który właśnie mówi, być może to było, może powinien być parametr tutaj gdzieś tego raportu, żeby sobie wyfiltrować sprawy, które leżą na przykład dłużej niż 2 dni, bo to oznacza, że już coś trzeba się czymś zająć, nie. Tak, taka, tak mi to danie.

**Damian Kamiński:** No dobra, tylko to, to tylko to jest zupełnie inna perspektywa. OK. Rozumiem, to zastanawiam się szczerze, zastanawiam się nad sensem tego raportu, nie, nie chcę go podważać, tylko zastanawiam się jaką faktycznie daje.

**Łukasz Bott:** Perspektywa, no tam.

**Damian Kamiński:** Miarodajną informa.

**Łukasz Bott:** No wiesz, w kontekście wielu procesów, tak, jakiś tam. No to ten, no bo tak, no wyświetlenie, znaczy, oczywiście to bazuje na jakimś tam źródle zewnętrznym, można by było ewentualnie tabelkę wyświetlić z case ID, tytułem i ile dana sprawa, konkretna sprawa, tak, według konkretnego procesu, ile przebywa w systemie? Tak, bo to, to jest to co oglądamy, to jest pewien agregat, nie wizualnych. A pod spodem jest nienormalna tabela, gdzie jest po prostu policzone dla każdej pojedynczej sprawy, tak, ile ona przybywa w systemie.

**Damian Kamiński:** Tak, tylko teraz, jakbyśmy to rozszerzyli. Czyli. Bo tak. Tu na przykład widzimy, że średni czas procesowania jakimś tam procesie to jest 14 dni.

**Łukasz Bott:** Tak, średnio z tych spraw, no.

**Damian Kamiński:** Ale jeśli przyjmiemy, że ten proces ma 30 etapów. No to w zasadzie. Abstrahując od tego, że ten proces jest optymalny, to przebieg tej sprawy jest dobry, nawet bym powiedział bardzo dobry, bo średnio etap trwa pół dnia. No zakładając, że różne osoby mają różną dostępność. To powiedzmy. Ale w drugą stronę, jeśli byśmy tu pokazali ilość spraw aktywnych, które nie zostały podjęte przez ostatnie 2 dni.

**Łukasz Bott:** No tak, no to.

**Damian Kamiński:** To, to by może pokazało, gdzie są procesy, w których jest duża inercja. Pytanie tylko, czy takie podejście jest łatwe tu do realizacji, tego nie wiem. Dobra, powiedziałbym, że idźmy na razie dalej, mamy z tego konkluzje. Będziemy mieli nagranie, na razie tam oto.

**Łukasz Bott:** Tak, nie, no po prostu.

**Damian Kamiński:** Słaba, no jest to jakaś statystyka, natomiast ja nie widzę wartości dodanej dla biznesu, dlatego nie chciałbym się na tym skupiać. Coś jest, tak, kto jak kto interpretuje, to już jest drugorzędne.

**Łukasz Bott:** Dobra. No jest. Dobre statystyki, dobra statystyki utworzonych spraw, no to tutaj bieżący miesiąc, ilość utworzonych sprawdzam miesiącu.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Według tutaj po wszystkim procesach, tak, więc trzeba sobie przez proces przefiltrować.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Liczba utworzonych spraw per użytkownik, nie, czyli tutaj dajemy informacje, kto najwięcej spraw tworzy, tak.

**Damian Kamiński:** No dobra, OK, chociaż też tutaj będzie duże zakłamanie w kontekście systemowych, nie, bo pewnie dużo też spraw.

**Łukasz Bott:** Tak, tak, no to wiadomo, wiadomo, no to wtedy.

**Damian Kamiński:** Więc może system trzeba wykluczyć?

**Łukasz Bott:** Może tak, czy o system wykluczyć? Mm, no to wizualnie podobny, tylko po innej dacie, pokazy mody modification date, tak, czy po dacie modyfikacji, podobne zestawienie, ile spraw zostało zmienionych w bieżącym miesiącu, tak, w poszczególnych dniach i przez właściciela.

**Damian Kamiński:** No. To już jest ciekawe, bo to pokazuje z kolei ja. W danych dniach system był intensywnie używany, tak, mhm, i obciążony jednocześnie, tak, bo to może pokazać właśnie, że nam dojść do dziesiątego.

**Łukasz Bott:** Obciążono, no tak, tak.

**Damian Kamiński:** Obsługujemy 10000 faktur do dziesiątego, to robimy mega dużo, a potem od dziesiątego to w zasadzie mało się dzieje w systemie. No okej, no to jest ciekawe.

**Łukasz Bott:** Tak. No i to, to, to, to, to, to powiedziałeś, umożliwia analizę aktywności użytkownika i tam dynamiki zmian w ujęciu dziennym. No to akurat. I to tak samo, tak, dobra, czy?

**Damian Kamiński:** Ale to czekaj, czekaj, to drugie mnie interesowało.

**Łukasz Bott:** Co?

**Damian Kamiński:** To jest bieżąca ilość spraw u właścicieli, tak?

**Łukasz Bott:** U poszczególnych właścicieli, tak.

**Damian Kamiński:** A. Jakbyśmy to zestawili. Ile sprawa na osoba edytowała? Czy my poza tą ilością edycji możemy wyciągnąć, że Basia edytowała 50 spraw?

**Łukasz Bott:** No to jest twoje naborów w kwestii 49.

**Damian Kamiński:** Ale sam tytuł, sam tytuł mi mówi, że.

**Łukasz Bott:** No to jest.

**Damian Kamiński:** To jest. Basia ma tyle w swojej zakładce do wykonania, to jest to czy to?

**Łukasz Bott:** Tak, bóg tam, gdzie jest oznaczona jako case opener.

**Damian Kamiński:** No właśnie, a ja bym. Żeby nawiązać do tego poprzedniego?

**Łukasz Bott:** A.

**Damian Kamiński:** Mm, to ja bym powiedział, że. Zakładam, że tak jest, że w historii mamy informacje, kto edytował, czyli kiedy pierwsze, pierwszy raport.

**Łukasz Bott:** Tak, to kto i kiedy, no tak, kto i kiedy modyfikował, mam, tak, to, to, to trzeba było wyciągnąć, ale z histy.

**Damian Kamiński:** To ja bym to zamienił, że w sensie to już jest coś innego, czyli to jest nie statystyki zmodyfikowanych, tylko to co tu prezentujesz, to jest nie wiem, stan obłożenia użytkowników, bo to jest, czyli właśnie ilość spraw poszczególnych właścicieli.

**Łukasz Bott:** OK.

**Damian Kamiński:** Mm, to, to bym był oddzielny, natomiast to by było ciekawe, czyli którzy użytkownicy faktycznie są bardzo aktywni, czyli kto ile edytował w danym miesiącu? No mówiąc wprost, tak jak tam mamy w poszczególnych dniach.

**Łukasz Bott:** Zmodyfikowaną.

**Damian Kamiński:** Ilość edycji, no to tu moglibyśmy mieć dostawienie. Nawet już nie w poszczególnych dniach, tylko bym powiedział przez ostatnie 30 dni, kto ile razy modyfikował sprawę AMODIT?

**Łukasz Bott:** OK.

**Damian Kamiński:** Czy nawet bieżący miesiąc? No to to już jest wtórne. Mm, bo można to przecież tutaj, skoro jest wyciągnięte, to można to sobie przed bytować. No to by było ciekawe, bym powiedział, bo to pokazuje. No właśnie kto pracuje, a kto nie? No w sensie w systemie, ja nie mówię globalnie, ale kto pracuje w systemie i jak bardzo jest ten system zaangażowany?

**Łukasz Bott:** Mhm, OK. Dobra, no to.

**Damian Kamiński:** No to bym wymienił, a to co tłumacz, to ja bym niekoniecznie to wyrzucał, natomiast bym to raczej.

**Łukasz Bott:** Nie, to może trzeba przemianować, nie tytuł.

**Damian Kamiński:** Przemianować, wyciągnąć do odrębnego jako bieżąco obciążenie, przy czym tutaj też z racji na ilości ja bym wykluczył. Wszystkich tych, którzy mają mniej niż 10, bo czy mniej niż 5, przynajmniej żeby tu było naprawdę pokazane, to kto ma bardzo po kolejkowanie sprawy w swojej zakładce do wykonania, a nie takie jakieś pojedyncze strz. Cały, bo to tylko zaburza, że tak powiem. Odbiór, nie, jak tutaj wyświetlimy 100 pozycji, no bo tylu zerówki nieraz jest, nie.

**Łukasz Bott:** Mhm. No i jeżeli to wiesz, jeżeli jest tutaj by zrobił, bo jest jakiś kształt robiony, tak. No to można by było.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Są wartość dorzucić do filtra i ustawić się jako domyślną filtr. Na przykład nie wiem, wiem, więcej niż 5, więcej równo 5.

**Damian Kamiński:** Tak. Tak, jeszcze jest to pokażę, że na przykład nie wiem, jakieś osoby przeciążony, tak, bo powiedzmy, pokazujemy więcej niż 5, a może w ogóle powinniśmy dać standardowo 10, bo co nas obchodzi, że ktoś ma 5? No na bieżąco możesz mieć 5, no ale jak masz 25, no to niekoniecznie to obsłuży wszystko dzisiaj, cały czas masz niekończ.

**Łukasz Bott:** No tak.

**Damian Kamiński:** Będą się kolejkę. Dobra, idźmy dalej, no to jest to, już to jest zajęcie. Uważam, że to daje fajną wartość.

**Łukasz Bott:** Dobra, to już jest to.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Z logów systemowych, to tutaj jest.

**Damian Kamiński:** Mhm. No spoko.

**Łukasz Bott:** Legenda, nie wiem dlaczego Kuźniar się upierał, żeby 1, 3, 2 sortować, czyli widzimy dla administratora. Widzimy, że na przykład nie wiem.

**Damian Kamiński:** Po ilościach sortuje.

**Łukasz Bott:** O ilościach, a OK, dobra.

**Damian Kamiński:** Czerwony na górze, potem. No źle jest, powinno być.

**Łukasz Bott:** Tak, tak, po ilościach. Po powinien posortować po. Zaczęły legendy, tak.

**Damian Kamiński:** Tak, tak, legendę.

**Łukasz Bott:** Dobra. Dobra i tutaj, no informacja dla administratora, tak, widać, że z ilość błędów spadła, tak, w ostatnich, w ostatnich dniach.

**Damian Kamiński:** To jasne, tutaj wszystko jasne? Mhm.

**Łukasz Bott:** I informacyjne utrzymują się wymienic na stałym poziomie, tak samo ostrzeżenia też na stałym poziomie, tak nisko.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** I dla odmiany, ponieważ ten raport, który oglądamy, jest ze źródła lokalnego, takiego wzrostowo naliczonego, czyli ta tej ilości tutaj są agregat jest robiony w momencie przeliczenia, tak, to na względem poprzedniego dnia. Zakładam, że synchronizacja tego źródła i to przeliczenie będzie następowało. No gdzieś tam w godzinach nocnych raz na dobę, nie.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Sąd będzie tak pokazywał, aczkolwiek tutaj w tym środowisku deweloperskim te czasy ze względu na testy czy coś, to te czasy tam są czasami ustawione. W środę w środku dnia, więc może być tak, że nie wiem, jeżeli za godzinę wejdziemy w ten raport. Tak, no to już będzie tutaj się pojawi. Szesnasty nie zostanie przeprocedować, to na to trzeba zwrócić uwagę, a to jest to samo, tylko że w bieżącym dniu.

**Damian Kamiński:** OK.

**Łukasz Bott:** I teraz zaraz zobaczymy pewną ciekawostkę.

**Damian Kamiński:** No, no, że co, przefiltruj w po dwójce, tak się pojawi czy co?

**Łukasz Bott:** Patrz, log status naturalki pie jest 2.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** A powinien być jeden. Lock status 30. 3 jedynka, jedynka, jedynka 30. Skąd to się 2? 2.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** 12 człowiek to tak jakby. Z tak jakby skądś zostawił, wiesz? Oszustka. Od czapy zupełnie.

**Damian Kamiński:** Mhm, a pokaż, no nie wiem, chodzimy jeszcze w edycję tego.

**Łukasz Bott:** No to jest. No możemy wieść, wejść w edycję tego, ale tu.

**Damian Kamiński:** No weź wejdź na chwilkę.

**Łukasz Bott:** No dobra, wiesz co, bo tutaj jest. To jest sytuacja taka, że ja to. Mm, no.

**Damian Kamiński:** Lock status, bo zacz masz sumę lock status i to może być powodem agregacja i tutaj maksimum w zasadzie albo minimum to, bo liczba to będzie jako liczba, to jest ilość.

**Łukasz Bott:** Dobra, dzięki. Nie, to powinno lock status, to jest liczba.

**Damian Kamiński:** Liczba to jest, wiesz, suma to jest suma wartości, liczba to jest ilość, liczba unikalnych, to jest ilość unikalnych. Ja bym dał minimum albo maksimum, to albo średnią, bo to wszystko tylko według mnie lepszą agregat, to nie wiem, chyba maksimum czy minimum jest w ułatwi ejsze wyliczeniu niż średnia.

**Łukasz Bott:** Nie, tu. Moment, tu nie powinno być w żadnej agregacji, tu powinno albo powinna być jeszcze opcja wartość.

**Damian Kamiński:** No a kliknij na sumę, można ją wyłączyć.

**Łukasz Bott:** Wysłałam.

**Damian Kamiński:** Jak klikniesz drugi raz na to samo. No tak, tylko co do zasady coś agreguje i nie wiadomo, czy tu nie da się wyłączyć. Zmień na chwilę na nie wiem, średnią albo maksimum i zobacz, czy to w ogóle rozwiąże problem. No.

**Łukasz Bott:** Dobrze, dzięki.

**Damian Kamiński:** Natomiast tak, no trzeba było to ewentualnie. Nad wartością się zastanowić, tak, tak, tak.

**Łukasz Bott:** Nie, no po prostu. Bo powinno być tak, powinno moim zdaniem powinna być może wartość. No to przy okazji poprawiliśmy błąd. Dobra, to już nie będę zgłaszał. Dobra, no to.

**Damian Kamiński:** No dobra, to jest ciekawe z tymi z tymi modułami, to też ciekawe. No dobra, idźmy dalej.

**Łukasz Bott:** Masz, co się stało? Siedzieliśmy gdzieś tam edytowanie śmy i wyskoczył nam zupełnie na sam początek.

**Damian Kamiński:** Ewelina.

**Łukasz Bott:** Performance monitor, no to podoba podobne do logów, tak, jeżeli chodzi o zasady działania. No tutaj tabelarycznej, tak już jak ktoś chce. Ty też ostatnie 7 dni pokazuje wszystko.

**Damian Kamiński:** Dobra, to tabela, a jeszcze ten łączny trzeba OK. To tylko tak tabela co pokazuje wszystko pokazuje.

**Łukasz Bott:** I ten. Tak z ostatnich 7 dni.

**Damian Kamiński:** No właśnie i nad tym można było zdecydowanie pewnie popracować, bo czego mi tu brakuje, tu powinien być pivot jeszcze. Jako trzeci pod formularz, który agregowanie właśnie to, co mamy w tabeli, bo ani jedno, ani drugie.

**Łukasz Bott:** Okej?

**Damian Kamiński:** Nie jest wystarczające, bo na pivocie ja zmieniam sobie tak, mam 7 dni, OK, zakresem mogę sobie żonglować, natomiast wtedy patrzę, tak patrzę na pivot pod kątem nie wiem reguł, jobów, jakieś ludy, mail i tak dalej. No ostatnio tak rozkminiam liśmy dla nie pamiętam jakie to klient, ale to sam wdraża z Erykiem.

**Łukasz Bott:** OK.

**Damian Kamiński:** No i. To i spojrzeliśmy tak? Jak jaka analizowaliśmy, tak szybko przedstawiając czego, bo mi się zaczęło już spotkanie jakieś, czy nie?

**Łukasz Bott:** Nie wiem, o co ci chodzi.

**Damian Kamiński:** Mieliśmy, no to chyba od pół do, do wpół do zaczęliśmy od tego, a nie my, moment do równy i dobra. No pivot jest niezbędny, o tak bym powiedział, żeby to dobrze analizować, bo my wzięliśmy tak łączny czas wykonywania reguły w miesiącu.

**Łukasz Bott:** OK, dobra, no.

**Damian Kamiński:** No i wyszedł jakiś wynik i stwierdziliśmy, dobra, to nawet nie jest dużo, to jest jakoś sensownie, ale teraz tak wzięliśmy z miesiąca, potem wzięliśmy dobre, ja mówię, no to teraz zobaczymy na ile te dane są. Nie przekłamane w kontekście tego, jak to wyświetlamy, wzięliśmy pół miesiąca i okazało się, że dane są takie same. Wzięliśmy pierwszy tydzień. Okazało się, że dane są takie same, czyli cała praca jest wykonywana w pierwszych 5 dniach miesiąca, a przez to, że patrzyliśmy przez pryzmat całego miesiąca i podzieliliśmy sobie to na 30. Łączny czas to wyszło nam, że no wykonuje się to tam nie wiem. 2 godziny dziennie, a okazało się na koniec, że jak zaczęliśmy właśnie zgłębiać i schodzić ten poziom niżej.

**Łukasz Bott:** Mhm. Średnio dziennie, no OK, no.

**Damian Kamiński:** Poziom niżej w mniejszym zakresie, no to się okazało, że wykonanie joba, a w zasadzie jednej reguły. Cyklicznej trwa 5 godzin dziennie. Bo tyle jest spraw po prostu na początku miesiąca.

**Łukasz Bott:** Ale tylko, tylko przyspiesze tam kilka dni miesiąca, tak?

**Damian Kamiński:** Dokładnie, a później to już są wiesz, pojedyncze wywołania, bo wtedy spływają wszystkie faktury kosztowe i tam się budżety mielą i tak dalej. A przeszliśmy na spotkanie z klientem i pytamy, no dobra i teraz tak. Od ósmej do czternastej codziennie mielicie bez przerwy daną regułę. A czy to co ona mieli w ogóle jest potrzebne biznesowi ad hoc, no nie. No to prosty, proste rozwiązanie. Przenieście to na godziny nocne. I nie będzie.

**Łukasz Bott:** I na weekend.

**Damian Kamiński:** I na weekend czy tam nawet nocy, bo chodziło to tak, system działa wolno, tylko wiesz, to jest ogólne pojęcie, a kiedy działa wolno? A no my to my znaleźliśmy, że pewnie działa wolno na początku miesiąca i pewnie kiedy wtedy, kiedy ludzie też mają najwięcej roboty, a wy jednocześnie wykonujecie jakieś zadania, które w ogóle tym ludziom w tym momencie nie są potrzebne. Czyli wiesz, jak faktura przejdzie, to oni gdzieś tam w budżetach coś tam doładowującego przeliczają i tak dalej, a te budżety w zasadzie można by przeglądać w wynikowo następnego dnia.

**Łukasz Bott:** No. No tak.

**Damian Kamiński:** No i problem rozwiązany, więc żeby to przeanalizować, ty widziałeś taki proces dedykowany do zbierania danych z monitora.

**Łukasz Bott:** No chłopaki w serwisie albo wdrożenie chcę chyba tak robili.

**Damian Kamiński:** No i według mnie i według mnie to powinniśmy odtworzyć te same raporty są w tym procesie, one tam są naprawdę sensowne. Jak się wie co czego się szuka i tam te filtry, które są przygotowane.

**Łukasz Bott:** OK, dobra, no.

**Damian Kamiński:** Naprawdę pozwalają to robić. To, to, to naprawdę będzie użyteczny w sensie, otworzyłbym to po prostu tutaj na poziomie raportu i tyle, tylko właśnie pivotem.

**Łukasz Bott:** OK. Dobra, no pivot, tak faktycznie było tam w pivocie, coś będzie jaśniejsze, coś będziecie mniejsze, tak, no i wtedy możesz drążyć, nie.

**Damian Kamiński:** No i tyle i potem, tak jak mówisz. Dokładnie, a potem już tabela jak najbardziej, bo potem z tej całej agregaty. No to sprawdzam ile trwa konkretnej jedno wywołanie danej reguły czy danego joba, no i się okazuje, że trwa właśnie 2 godziny. Tu warto by było w pivocie. Przeliczyć to, kurde, to jest strasznie niewygodne, że to jest pytanie, na ile to się da, jakbyś przejechał w prawo. No właśnie total duration, tu dobrze by było, żebyśmy. Na ile się da narzucić, bo teraz pytanie, co to jest 0,5?

**Łukasz Bott:** Mm, to jest sekundach. Czyli zero 500.

**Damian Kamiński:** To jest sekundach.

**Łukasz Bott:** To jest 0,05 sekundy.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Tak mi się wydaje tam.

**Damian Kamiński:** No dobra, no według mnie musimy nanieść tutaj jednostkę, bo to jest ważne.

**Łukasz Bott:** Mhm.

**Damian Kamiński:** Bo inaczej nie mamy kontekstu, no i tyle, no ale posortuj to na na po największych wartościach. Z ciekawości jeszcze raz. Mhm.

**Łukasz Bott:** 70, 65.

**Damian Kamiński:** No OK, nie, ale ta to przyzwoicie. No ale to są pojedyncze wywołania.

**Łukasz Bott:** Tak, to jest środowisko deweloperskie, to.

**Damian Kamiński:** No dobra, no to tutaj dołożyłbym po prostu jeszcze chyba tam wyjdę ze 3 raporty, pivot gotowe, tak jak są tam. Odrębne na pewnie joby, odrębne na reguły. I coś tam jeszcze chyba jest.

**Łukasz Bott:** Dobra, wiesz co, to to, jakbyś to, jakbyś miał ten proces, albo wiesz od kogo mam, mam go wziąć, to.

**Damian Kamiński:** Od Eryka na pewno, ja wiesz co, ja gdzieś miałem, ale zanim znajdę, to Eryk ci go da z marszu, więc tu wgrywasz na środowisko i masz gotowce, tylko trzeba to przepisać na na to.

**Łukasz Bott:** Dobra. Jest dobra, to dorywczo. Zrobiłaś to, jest mi winien coś tam?

**Damian Kamiński:** Dobra, to idźmy, co tam dalej, to to jak najbardziej.

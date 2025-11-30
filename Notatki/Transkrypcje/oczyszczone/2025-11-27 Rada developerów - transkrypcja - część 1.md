**Data spotkania:** 27 listopada 2025, 09:09

---

**[Janusz Bossak]:** Teraz jest dobrze. Chyba dobrze teraz zaczęła.

**[Kamil Dubaniowski]:** Doradzimy co tam. Na pewno ja bym chciał omówić te reguły tabeli, jak będziemy do tego wchodzić na początek, to bym Filipowi dłoń.

**[Damian Kaminski]:** Dobra, to ty pokazujesz czy mam pokazać? Ja mogę pokazać tylko.

**[Kamil Dubaniowski]:** Dorzuć, a ja szukam Filipa na liście.

**[Damian Kaminski]:** Jest takie ryzyko, że w razie co będę musiał się ewakuować.

**[Kamil Dubaniowski]:** To dasz znać?

**[Damian Kaminski]:** Na Teams. Ale to powiem, jeśli mnie tam wywołają, bo udało mi się z tego wymigać. Według mnie tam to nie powinno być zaangażowanie naszego działu w ten temat. Dobra, clock squares queries.

**[Kamil Dubaniowski]:** To jest pierwszy akurat. To pierwsze pewnie głównie do ciebie. Możemy i może na decyzję, czy chcemy co dalej robić tak jak mamy, czy robimy już Reactowe ten jedyny edytor, ale to raczej większy temat, nie na ten sprint. Wtedy wyszedł. Znam o co chodzi na nowej liście pól. W ustawieniach procesu dodaliśmy akcję, która miałaby otwierać edytor reguł tabeli. Czyli to, co nam brakowało, mieliśmy w edytorze, że wchodzisz sobie w tabelę i klikasz edytuj regułę tabeli. No to my dodaliśmy na nowej liście pól traktatowej i ten edytor nam się otwiera, ale ten przycisk.

**[Piotr Buczkowski]:** Trzeba programować to w jaki sposób jest otwierany?

**[Kamil Dubaniowski]:** Czyli.

**[Piotr Buczkowski]:** I co wywołać, żeby zamknąć?

**[Kamil Dubaniowski]:** OK. Czyli przerabiamy jakby to, to nie jest jakiś tam większy temat.

**[Piotr Buczkowski]:** To jest drobna poprawka, trzeba tam dodać wykrywanie, że to otwieramy właśnie z Reacta i wywołać co innego niż tam. Hit na parent, to pewnie tutaj parent jest coś, bracie, to tego nie ma.

**[Kamil Dubaniowski]:** Tak, zgadza się. Dobra, no to tyle chciałem w sumie wiedzieć, czy to jest jakiś większy temat i lepiej iść od razu w nowy.

**[Piotr Buczkowski]:** Jest po prostu czarna funkcja JavaScript w tym okienku, która wywołuje coś z parent, a ponieważ ten parent jest inny, to trzeba zrobić coś inaczej, żeby działał i tu i tu.

**[Kamil Dubaniowski]:** Dobra, to Filip.

**[Damian Kaminski]:** Dobra, tylko to, co powiedział właśnie Piotr, to jest jasne dla Filipa, co trzeba zrobić, bo to nie jest React, tak.

**[Kamil Dubaniowski]:** Znaczy nie, Filip nic nie zrobi. Filip będzie czekał na poprawkę i wtedy.

**[Damian Kaminski]:** No właśnie.

**[Piotr Buczkowski]:** Nie, Filip musi powiedzieć co wywołać, żeby zamknąć to okienko.

**[Kamil Dubaniowski]:** OK, bo też Filip od razu jak to robimy, to zróbmy to docelowo, bo pewnie jeszcze chwilę te reguły, stary edytor z nami zostanie, to ja chciałbym, żeby to jednak otwierało się w popup. Czyli to Anuluj powinno.

**[Piotr Buczkowski]:** W jaki sposób to się powołuje?

**[Kamil Dubaniowski]:** Aktualnie otwiera się w nowej karcie w ogóle, więc teraz to jest do zmiany po stronie Filipa, a ja chciałbym to w popup.

**[Piotr Buczkowski]:** W nowej karcie to OK, to wystarczy tej formacji.

**[Kamil Dubaniowski]:** Tak może, bo docelowo ma być w oknie, docelowo ma być.

**[Damian Kaminski]:** Ale poczekaj, Piotr, to ty sugerujesz, że to ma być w nowej karcie?

**[Kamil Dubaniowski]:** Teraz ja bym chciał, bo docelowo ta reguła, ten edytor miałby się otworzyć.

**[Damian Kaminski]:** Bo Kamil tak nie chce.

**[Kamil Dubaniowski]:** Dobra, to może cała koncepcja od początku. Planujemy, żeby na liście pól w ogóle był taki odnośnik do wszystkich reguł powiązanych z tym polem. No i na początku wiadomo, że na nie mamy tego, natomiast docelowo ma się otworzyć to w dużym oknie popup. Widzę listę wszystkich reguł powiązanych z tym polem i potencjalnie mogę sobie tam przejść do edycji tej reguły. I to nie ma być przejście do zakładki reguł, bo to będzie już jakby wybicie użytkownika. On jest na liście pól, otworzył sobie tylko podgląd listy powiązanych reguł, więc ja nie chcę go przekierować do nowej zakładki czy w ogóle do zmienić mu zakładkę na listy reguł. Tylko chcę pokazać tę listę w formie okna.

**[Damian Kaminski]:** Ale popup, to znaczy mówisz tylko, że popup, że to będzie okno zamykane w tle, jest to gdzie pracujemy, czyli nasze bieżące, natomiast.

**[Kamil Dubaniowski]:** Tak, lista pól.

**[Damian Kaminski]:** Będzie pełnoekranowy popup.

**[Kamil Dubaniowski]:** Tak, no jak najwięcej miejsca zająć. Wiadomo, tam jakaś minimalna ramka, żeby było widać, że to jednak jest popup, żeby ktoś się zorientował, że to się zamyka, ale no nie chcę zmieniać właśnie kontekstu. Tak jak jesteś na liście pól i tylko podglądasz sobie listę powiązanych reguł, no to chciałbym, żeby to było w oknie popup, żeby nie zmieniać właśnie użytkownikowi kontekstu. No bo nie wiemy, czy on wejdzie do jakiejś reguły, czy nie wejdzie, chciał tylko zobaczyć listę powiązanych.

**[Damian Kaminski]:** No właśnie OK. Tak, tak, tak. Czyli de facto tak jak jest teraz, bym powiedział, tylko już po nowemu, czyli będzie to jeden element zarówno wywoływany z listy reguł, który otworzy popup z jakimiś regułami, i tak samo tam to będzie popup z regułami.

**[Kamil Dubaniowski]:** Tak, wtedy no na ten moment po reguły, chociaż była też koncepcja, żeby pole, tabela miało swoją listę reguł, tak, czyli żeby nie było jednej zbiorczej reguły tabeli, tylko tam pamiętam, że.

**[Damian Kaminski]:** No tak, ale to już jest ten krok pośredni, o którym mówisz, tylko żeby wyświetlić, a potem jak już wyświetlisz, tak jak powiedzmy tu ta będzie inaczej w React, ale tak jak tu klikasz sobie przycisk, no to otwiera się popup i ten popup będzie analogiczny z tej perspektywy. Z tamtej perspektywy będzie to jeden element przygotowany przez tutaj React.

**[Kamil Dubaniowski]:** Tak. Tak, no i. Wejdź może na albo dobra, to ja udostępnię, że jak jest teraz i o co mi chodzi. Dopiero pulpit. O stronę by się przydało przerobić też tam jakieś tereny się wyświetlanie wiadomo pól.

**[Janusz Bossak]:** Tutaj jest w jak widzę bez tych ramek na tym pasku i według mnie to lepiej wygląda bez tych ramek.

**[Kamil Dubaniowski]:** Tak, no to tak powinno zostać. No już nawet mamy widzisz, no to już jakby jest wersja deweloperska, czyli wyższa niż jest nas trochę obsiana i wywalili. Znaczy to aktualizacja SignApp, tak.

**[Damian Kaminski]:** No to trzeba szybko to zaktualizować i nie przyzwyczajać, no bo innej opcji nie ma.

**[Kamil Dubaniowski]:** Tak, dobra i teraz tabela, tak, czyli doszła tutaj akcja reguły i ja chciałbym, żeby ona była na wszystkich polach, czyli tutaj na liście wyboru, na przykład też ten piorun otwiera mi się tutaj na pełen ekran lista niekompletna reguła lista. Ja z tej listy mogę wejść sobie do edytora, ale to nadal wszystko dzieje się jakby w oknie popup. Czyli nie ma przekierowania na tę zakładkę.

**[Piotr Buczkowski]:** Ja wiem, że technicznie.

**[Damian Kaminski]:** Dobra, to znaczy powiem tak, na razie jest to na etapie koncepcji, nie ma w ogóle projektu mockup, więc według ciebie, Piotrze, mało może i ktoś inny, no zróbmy mockup, bo to jest mało kosztowe i się zastanówmy, czy ma to sens.

**[Kamil Dubaniowski]:** Dobra, ale tutaj decyzja, no bo to jest o tyle kluczowe, że teraz to się otwiera w nowej zakładce i mogłoby tak zostać na teraz, tak, tylko wtedy obsłużymy to Anuluj i zapisz regułę. No bo tak naprawdę to powinno zamykać wtedy kartę, nic więcej, bo w tle mamy tę listę pól.

**[Damian Kaminski]:** No dobra, ale to w takim razie. No właśnie tego typu rozwiązania jest, co jest prostsze róbmy, bo to jest tymczasowe rozwiązanie, więc róbmy to, co jest po prostu prostsze.

**[Janusz Bossak]:** No tak, ale przerobienie tak.

**[Piotr Buczkowski]:** Zamykanie tego okienka jest proste.

**[Janusz Bossak]:** Tak, no.

**[Piotr Buczkowski]:** Jeżeli wiem, że się otwiera w.

**[Damian Kaminski]:** Czyli zamknięcie tej zakładki tak jest proste pod przyciskiem.

**[Piotr Buczkowski]:** Trzeba programować to, więc po prostu weź proszę być.

**[Damian Kaminski]:** No to tak rób, bo jeśli to jest proste, to tyle według mnie to nie jest bloker, to jest rozwiązanie na nie wiem kwartał.

**[Kamil Dubaniowski]:** Na Anuluj, OK.

**[Damian Kaminski]:** Maks pół roku, to nie jest jakiś problem tutaj, który by powodował, że coś jest mniej użyteczne.

**[Piotr Buczkowski]:** Jest to mój do parent close, no to window parent nie ma, jest pewnie window opener, tak. Trzeba obsłużyć window, jeżeli jest null, to inaczej.

**[Janusz Bossak]:** No i dobrze, bo tutaj doszliśmy też do takiego momentu, w którym może warto o tym parę słów powiedzieć, bo jak będziemy przerabiać te reguły, w szczególności edytor, taki, który widzimy teraz, jak tu zacznij coś tam pisać w tym edytorze. No właśnie on to wygląda tak, ten edytor, tak, no to też mieć w którymś momencie w React.

**[Damian Kaminski]:** Tak.

**[Janusz Bossak]:** No i to jest pierwsze wyzwanie, które trzeba.

**[Damian Kaminski]:** Tylko nie powinniśmy tym na tym dzisiaj zająć się spotkania. Byliśmy samotni, nie wchodzili, trzeba to zaprojektować, zgadza się.

**[Janusz Bossak]:** Tak. Ale. Dlatego lepiej jest to rozwiązanie, które powiedział Piotr, niech to będzie nawet to stare okienko. I OK. Dopóty, dopóki nie rozwiążemy.

**[Piotr Buczkowski]:** Albo. To otwierajcie po prostu.

**[Janusz Bossak]:** No bo jeszcze.

**[Piotr Buczkowski]:** Wtedy będzie działać bez żadnych zmian po window parent będzie.

**[Kamil Dubaniowski]:** Tutaj tak, czyli o KW sensie tej ramie po prostu.

**[Piotr Buczkowski]:** A nie, sorry, nie będzie, mój błąd. Musiałaby być ta funkcja. Musielibyście dodać tę funkcję, która zamyka o tej nazwie, co tam wywoływane.

**[Damian Kaminski]:** Znaczy według mnie, że to, że to się otwiera w nowej zakładce to.

**[Piotr Buczkowski]:** Pytanie, kto to pytanie, gdzie ma być zmiana? No na tym edit, ról czy React?

**[Damian Kaminski]:** To nie jest problem. Co to znaczy?

**[Kamil Dubaniowski]:** Mniejsze ryzyko, że popsujemy coś starych, jeśli zrobimy React, tak.

**[Piotr Buczkowski]:** Tam tak jak widziałeś tam jest window parent, coś tam, tak, to tu funkcję trzeba otworzyć. Nas trzeba utworzyć taką funkcję, trzeba script na stronie, która jest w React, tak.

**[Damian Kaminski]:** Na tej stronie, którą teraz? Aha, React.

**[Piotr Buczkowski]:** Close dialog, tak, która będzie potrafiła zamknąć ten dialog. Tutaj mi to parę minął, parent jest.

**[Damian Kaminski]:** Rozumiem, to znaczy z mojej perspektywy to to to.

**[Piotr Buczkowski]:** Dobrze, Przemek wczoraj robił. Bo aut tam jest podobne zasady, tak? Że jest wywoływana funkcja ta ustawia. Poprawny. Pobrany funkcję JavaScript, która ustawia wartość wygenerowanego tokenu o akt. On dodał do React jakoś tam, w jaki sposób funkcje ciała, sklep, która robi to samo, co robiła na starym. O tej samej nazwie, tak?

**[Damian Kaminski]:** OK. Czyli pod tym przyciskiem, który jest teraz dostępny na tym starym wyglądzie, Przemek tak jakby wstrzyknie JavaScript, który ma się wykonać, tak.

**[Piotr Buczkowski]:** Nie, nie. Nie. Teraz jest funkcja close dialog. Starym skrypt JavaScript, starym naszej kilku ze skryptami JavaScript, tak, która potrafi.

**[Damian Kaminski]:** No.

**[Piotr Buczkowski]:** Zamknąć aktualnie otworzony dialog. Tak naprawdę zamyka wszystkie aktualnie otworzone dialogi. Taka sama funkcja test musi być w React zrobiona. Żeby to zadziałało.

**[Damian Kaminski]:** Ale ja. Bo widzimy teraz ekran, który nie jest React, więc tu mi się coś nie zgadza w kontekście, chyba że masz na to inny plan, że.

**[Piotr Buczkowski]:** No window parent tutaj jest strona, która wywołała tę zakładkę. Strona jest w React i ona nie posiada close dialog funkcji.

**[Damian Kaminski]:** OK. Czyli trzeba dlatego narzędnika dorobić close dialog, tak.

**[Kamil Dubaniowski]:** Tutaj.

**[Piotr Buczkowski]:** Tak, tak.

**[Damian Kaminski]:** OK.


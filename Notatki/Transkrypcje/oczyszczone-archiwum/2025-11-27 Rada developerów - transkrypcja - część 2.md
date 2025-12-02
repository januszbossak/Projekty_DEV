**Data spotkania:** 27 listopada 2025, 09:09 - część 2

---

**[Piotr Buczkowski]:** Która będzie potrafiła zamknąć tę otworzoną zakładkę, tak.

**[Damian Kaminski]:** Filip, rozumiesz? To byli w stanie to zrobić.

**[Filip Liwiński]:** Dobra, rozumiem, no nie wiem co życie.

**[Kamil Dubaniowski]:** Jak coś to Przemka tam pod pytasz?

**[Damian Kaminski]:** No to jak ty rozumiesz tutaj, Przemek na pewno też będzie wiedział o co chodzi. W sensie chodziło mi tylko o to, czy po prostu z punktu widzenia React wiesz, co trzeba zrobić? No to OK, to trzeba to opisać i któryś z was to zrobi.

**[Piotr Buczkowski]:** W tym. To było w starym, te słowa po prostu wykrywa wszystkie tam okienka dialog otworzone i zamyka. Zakładamy, że jest tylko na raz jedno otwarte.

**[Damian Kaminski]:** Dobra, tylko podsumowując. To jest już aspekt techniczny, natomiast funkcjonalny będzie tak jak teraz Kamil pokazywał, otwieramy w nowej zakładce, klikamy przycisk, zamyka się ta zakładka, wracamy do poprzedniej, tak?

**[Piotr Buczkowski]:** Nie, sorry, nie, nie, nie, nie.

**[Damian Kaminski]:** Właśnie, czyli jak?

**[Piotr Buczkowski]:** Znaczy. Otwieramy popup. Na tej stronie React.

**[Damian Kaminski]:** W iframe pełnoekranowym.

**[Piotr Buczkowski]:** Tak.

**[Damian Kaminski]:** OK.

**[Piotr Buczkowski]:** Chyba jeżeli chcecie w nowej zakładce, to trzeba przerobić. No edit form.

**[Kamil Dubaniowski]:** Nie, no nie musi być. Moim zdaniem to nawet jest OK, że to się otworzy w tamtym kontekście także.

**[Piotr Buczkowski]:** Mówię, że albo zmiana tutaj, albo zmiana tutaj.

**[Kamil Dubaniowski]:** Zarówno React, no nie ryzykujmy, że zepsujemy coś, co działało. Tam mamy ostatnie 2 dni sprintu. No.

**[Damian Kaminski]:** No ale to jest coś, co wejdzie do grudnia, tak.

**[Kamil Dubaniowski]:** Grudniowej.

**[Damian Kaminski]:** OK. No dobrze, to jeszcze raz pytanie podsumowujące. Od tak otwieramy to w tym ekran, w tym oknie przeglądarki, w którym widzimy, otwiera się to na pełny ekran w formie takiego przykrycia tego, co jest pod spodem, musi być dorobiona do tej funkcji część React, która będzie interpretowała i zamykała ten to, to otwarte okienko. Ja to tak rozumiem z perspektywy tego, co powiedzieliście, czy tu nie popełniam błędów w opisie tego i czy ty, Filip, wiesz jak to zrobić?

**[Kamil Dubaniowski]:** Ja też tak samo to rozumiem.

**[Filip Liwiński]:** No też to tak zrozumiałem.

**[Damian Kaminski]:** I czy wiesz jak to zrobić?

**[Filip Liwiński]:** Mm.

**[Damian Kaminski]:** Czy coś chcesz dopytać Piotra?

**[Kamil Dubaniowski]:** Zacznijmy, jak będziesz miał pytania, to pewnie najlepiej z Przemkiem konsultować, jak to robił wczoraj i to będzie na bieżąco.

**[Damian Kaminski]:** No to skonsultuj to z Przemkiem, jeśli nie wiecie, to od razu dopytajcie Piotra, żeby po prostu podczas jego nieobecności móc to zaopiekować. Tak.

**[Filip Liwiński]:** Dobra, dobra.

**[Kamil Dubaniowski]:** No to chcieliby dzięki, bo chyba tam dalej to nie będzie sensu, żebyśmy się trzymali, namiar jakbyś wrócił, d.

**[Damian Kaminski]:** Już, już, już. Dobra, to co z tym robimy?

**[Kamil Dubaniowski]:** Przypisz do Filipa w takim razie, tak.

**[Damian Kaminski]:** Filipa, tak.

**[Kamil Dubaniowski]:** I wrzuć na ten sprint, no bo ten temat był w tym sprincie robiony nieskończony.

**[Damian Kaminski]:** OK. A to możemy to od 5 już stąd. Dobra, czy tu coś? Dostaliśmy jakąś odpowiedź, tu mieliśmy coś. Nie dostaliśmy odpowiedzi. No to czekamy.

**[Kamil Dubaniowski]:** No ja to wrzuciłem na 2 tych. No następnie spytałem na razie dopiero trampek, no bo to temat tam dostępy, bo jako jedyny.

**[Damian Kaminski]:** Tu się coś nowego pojawia u od LPP. A OK. To jest większy temat, już go redaguje. Czyli tak pomysł jest, to znaczy to jest temat naprawdę duży i to on może wymagać wyceny, ale pytanie, czy w ogóle chcemy w tę stronę iść, czyli czy przedstawić bardzo wstępną koncepcję klientowi i zapytać, czy w ogóle mamy to wyceniać? To znaczy mamy te formularze. To jest związane z tym, w jakim kierunku powiedz mi, jakie klientów w ostatnim czasie pozyskaliśmy, jak i klienci korzystają z AMODIT. Mamy te duże firmy, które traktują od lat jako portal pracownika typu LPP. Wszystkie w zasadzie, które wykorzystują to do aspektów HR-owych. I mamy kwestionariusz osobowy. Który często wypełniany jest na telefonie ze względu na to, że to jest dostęp tymczasowy ze względu na to, do jakich ludzi po prostu to trafia. Niekoniecznie właśnie oni mają czy mają, czy korzystają z komputerów na co dzień, tak, bo często po prostu są to jacyś pracownicy. Już mówiąc wprost tymczasowi, na przykład magazynowi związani właśnie teraz z okresem świątecznym i wypełniają to na telefonie, mówiąc wprost i teraz, tak, jeśli mamy taki formularz, to on często zawiera 200-250 pól. W związku z tym jego czytelność w formie takiej go długiego węża, no jest może mniej użyteczna i pomysł jest taki, żeby jeśli dzielimy to na sekcję, to wyświetlać formularz w kontekście takim sekwencyjnym, czyli wypełnij jedną sekcję i na końcu nie jest to przewijane na 200 pól, tylko jest powiedzmy 20 pól jest. Załóżmy jakaś strzałka dalej, kolejna sekcja teraz. Dlaczego to jest skomplikowane, bo pod tym dalej w zasadzie może powinniśmy od razu robić jakąkolwiek walidację tej części formularza. Mówimy oczywiście tutaj o ujęciu tylko mobilnym, więc inaczej by się zachowywał nieco formularz na przeglądarce na komputerze, a inaczej na mobilu, bo od razu jeśli coś wykryjemy, co jest niespójne, no to powiedzmy pokazujemy, że jeszcze na tym widoku.

**[Kamil Dubaniowski]:** Może przerwę i zasugeruję co mi przyszło do głowy, jak mamy ten tryb wyświetlania formularz i tam są 2 opcje, to dodałbym trzecią i to jest na zasadzie takiego. No nie wiem, póki co krokowego. Jakby trzeba.

**[Damian Kaminski]:** No.

**[Kamil Dubaniowski]:** Domyślnie to włączy i tak świadomie to włączyć i to nie będzie tak, że nam obojgu inaczej na desktop, inaczej tylko wtedy taki proces po prostu jest tak ustawiony, że no trzeba przechodzić każdą sekcję po kolei.

**[Damian Kaminski]:** OK. To jest jakaś propozycja, czyli tak naprawdę to jest trochę pod etapy, nie na, czyli jeden etap, na którym wyświetlamy różne różne wizualizacje formularza w formie takiego wizarda, no.

**[Lukasz Bott]:** Wiecie co?

**[Kamil Dubaniowski]:** Dodania tak masz.

**[Lukasz Bott]:** Damian, Damian, Damian, koledzy, słuchajcie, jak była jeszcze Christina, my to dyskutowaliśmy, a ja dokładnie to rozwiązałem właśnie etapem, czyli za każdą sekcję formularza odpowiadał etap w procesie i po prostu przełączanie między etapami tak powodowało przełączanie między zakładkami.

**[Damian Kaminski]:** OK, Łukasz, tylko to nie jest proste, dobra, tylko tu mówimy o grant temporary access.

**[Lukasz Bott]:** Nie, no mówię, że doraźnie, doraźnie tak to zostało rozwiązane. Tak, natomiast była koncepcja właśnie takiego, jak to powiedział wizard. Takiego właśnie krokowego przechodzenia nie i może w tym kierunku powinniśmy pójść.

**[Damian Kaminski]:** Tak, bo po prostu udostępnia, bo różne etapy się konfliktują z tym naszym GT, a które powoduje, że mamy dostęp na danym etapie. Tak.

**[Lukasz Bott]:** No tak, no to akurat było tak, że te kilka kolejnych etapów, czyli wypełnienie kilka kolejnych sekcji wykonywała jedna osoba w danym momencie. Tak.

**[Damian Kaminski]:** Wewnętrzny to był proces po prostu. No i nie był to ktoś z grant temporary, React, tak.

**[Lukasz Bott]:** Nie, grant temporary access, dopiero był na gdzieś tam na samym końcu, jak już były to formularz wypełniony.

**[Damian Kaminski]:** Nowość. Dobra, to podsumowując mniej więcej rozumiecie o co chodzi, jaki jest na to, jaki jest problem? Może o tak, bo jeszcze rozwiązanie to do tego może możemy jeszcze dojść i dyskutować. Pytanie tylko czy? Była się czy mamy w czy ta propozycja na przykład Kamila, że to jest specjalny tryb wyświetlania, to jest dobry kierunek w ogóle co?

**[Kamil Dubaniowski]:** Nawet teraz się wycofuję, oferuje się. Wycofuję się, to powinno być w takim razie ustawienie per etap, no bo taki tryb jest wymagany tylko na konkretnym etapie, kiedy ktoś uzupełnia dane, ale później, jak już rekruter, na przykład przegląda, no to nie, to są zwykłe wtedy zakładki dla niego i on sobie je przechodzi przez nie jak chce w dowolnej kolejności, więc to powinno być per etap.

**[Damian Kaminski]:** No właśnie. Tak masz lat. Może jeszcze inaczej, może to powinien być po prostu etap grant temporary, React. Nawet powiedzmy, jeśli się nie zdecydujemy na walidację, czyli możemy podejść do tego na zasadzie MVP, to powiedziałbym w drugą stronę walidacja jest na końcu i to jest OK, ale poszczególne kliknięcie dalej powinno według mnie przynajmniej zapisać stan. Bo telefony mają tę perspektywę, że mamy gesty, może ktoś klikając w pole się pomylić, kliknie cofnij i wywala mu 150 pól, które już wprowadził, więc powiedziałbym, że przynajmniej zapisanie tego, co już wprowadził przy przejściu dalej, czyli kole po 20, powiedzmy w pól sobie tam ustawą na sekcji już był sprawdziło. A walidacja nawet niech się odbywa, żeby tu nie konfliktować, że trzeba było opisać odrębne reguły pod daną sekcję i tak dalej, to może to byłoby prostsze pytanie, tylko czy w ogóle chcemy coś takiego zaczynać się nad tym zastanawiać i proponować klientowi, że w tym kierunku byśmy szli, możemy to wyceniać czy nie? No bo na razie nie ma jeszcze na to zlecenia, bo przedstawiony jest problem, jest oczekiwanie na jakoś propozycję rozwiązania z naszej strony.

**[Kamil Dubaniowski]:** Ja uważam, że to ma sens od dłuższego czasu i to nie tylko w tych tematach, nawet nasze tematy związane nie wiem tam gdzieś. Zgłoszeniem do wycen, żeby przeprowadzić tego użytkownika w takiej kolejności, w jakiej my chcemy, żeby nie szedł do dalszych zakładek, zanim nie uzupełni pierwszej. No bo możliwe, że uzupełnienie pierwszej wpływa na kształt tej ostatniej zakładki, tak, jakie tam pola się pokażą, nie pokażą, więc takie wizard, rok prowadzimy przez formularz, tak jak masz go uzupełnić. No moim zdaniem się przydawał AMODIT coś takiego, MVP, no i to wręcz mają jako takie pod etapy, dla etapu głównego i dla każdym etapie jest inny formularz, ale to jakby to jest właśnie na takiej zasadzie dalej, dalej i dalej. Więc u nas byłby to zbiorczy etap, nadal na przykład dekretacja, ale prowadzimy się przez formularz zakładka po zakładce. Nie skaczesz po tym jak chcesz?

**[Janusz Bossak]:** Ja mam takie.

**[Damian Kaminski]:** Czyli zamieniamy sekcję na kroki, tak, powiedzmy tak to sobie zdefiniujmy, że jesteśmy w jednym etapie, ale na różnych krokach.

**[Janusz Bossak]:** Ja mam takie przemyślenie, że to. Jak zwykle zależy, tak. Nie wiem czy to się da jedno z drugim połączyć, znaczy sekcji jest tym wizardem, bo my mamy tak, że. Układ formularza sekcji jest jakby jeden, tak, czy to na desktopie, czy na mobilnym, to w tej chwili to jest ta sama struktura.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Może nie wiem, propozycja pierwsza może trzeba by robić osobny. Jakby formularzy nie w sensie osobny formularz, tylko osobny układ pól, które mamy do wyświetlania na widoku mobilnym. To jest pierwsza propozycja, czyli mamy te same pola, tylko inaczej może poukładane w inne części. Druga propozycja to jest taka. Że dla tego typu przypadku wypełniania danych. To rzeczywiście taki powinien być projektowany wizard, tak, dlaczego mówię specjalnie o tym wypełnianiu danych, ponieważ ten przykład, który podałeś jakiś dekretacji już mi tutaj nie bardzo pasuje, bo to już jest bardziej złożony temat. Tak, to nie jest sekwencja.

**[Damian Kaminski]:** Jakie dekret kto podał tę?

**[Kamil Dubaniowski]:** Kojarzyłem w sensie chodzi mi o to, że mamy tak kilka zakładek, gdzie na ostatniej masz wskazać osobę akceptującą, tak, a tam na przykład jakiś filtr nakładamy w zależności od tego, co tam zadekretował, a ktoś od razu idzie do tej ostatniej na przykład.

**[Janusz Bossak]:** Tak, ja myślę.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Tak znaczy, wracając do myśli, to ja myślę, że to jest pewien szczególny przypadek wypełniania sekwencyjnego, tak, czyli jako kandydat jako ktoś tam dostaje i tak, i że to nie jest praca na formularzu, jak to się dzieje właśnie w ramach dekretowania, ja muszę zajrzeć nam gdzieś, nie wiem zobaczyć podgląd, potem wrócić, potem sprawdzić jeszcze coś, dopiero dopisać tak dalej, tak dalej, tu mamy sytuację pusty formularz.

**[Damian Kaminski]:** Tak, zdecydowanie według.

**[Janusz Bossak]:** I idziemy krok po kroku, proszę uzupełnić imię, nazwisko, PESEL. Pisałeś dalej. Teraz uzupełni dane rodziny, to to to popełniłeś dalej, idź tu, idź tu, idź tu i według mnie powinniśmy to przemyśleć. Czyli jak zrobić? Takie właśnie wizard do formularza, który mamy, tak, czyli formularz, formularz um, ale to jest pewien obiekt, taki wizard, który ma się odpowiednio zachowywać, w szczególności na widoku.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Mobilnym, ale może nie tylko, może no normalnej desktop też.

**[Damian Kaminski]:** Znaczy wiecie mobilny jednak jest ograniczony, więc tutaj takie prowadzenie jest dużo wygodniejsze, bo ciężej się w tym wszystkim połapać. Mamy mniej przestrzeni roboczej, ale według mnie to znaczy to tutaj Janusz powiedziałeś tam z polami, tak dalej, to już jest spojrzenie bardziej szerokie, ale nie mówię, że absolutnie nie chcę go wykluczać. Według mnie wydaje mi się tak, że powinniśmy zdefiniować tutaj persony aktorów, czyli co my chcemy zaopiekować? Przykład jeden to jest kandydat do pracy, przykład jakiś drugi to jest Kamil, ale no według mnie dekretacja faktury z mobila. Nie jest prostą sprawą, zwłaszcza jak tę tabelę, ale tego nie wykluczam i jak zdefiniujemy te przypadki użycia, to wtedy możemy podjąć decyzję, czy jesteśmy w stanie to zaaplikować jedną funkcjonalnością. Czy to jest nierealizowane, że tu trzeba zastosować inne rozwiązania dla tego aktora i takiego przypadku życia, a inne dla innego, no najlepiej by było, gdyby dało się to zaaplikować jednym, ale to może być trudne.

**[Kamil Dubaniowski]:** Czy dla mnie na ten moment to jest przypadek dosłownie, jak nazwał to Janusz, czyli wypełnianie danych, żeby kandydat nie czuł takiego rozproszenia. Czy ja już byłem w tej zakładce? Nie byłem uzupełniają. To wszystko, co ode mnie chcieli, czy może nie wszystko, to po prostu dalej walidacja, wszystko OK, idziemy dalej, mnie, no to od razu ci sygnalizujemy, że w karcie nie wiem. Członkowie rodziny nie zadeklarowały, że nie masz żadnych członków rodziny, więc nie możesz iść dalej. No to jest to.

**[Damian Kaminski]:** Tak, tylko że wymagana tylko, że wiesz, to są 2 aspekty walidacji jest walidacja wymagalności, którą pewnie jesteśmy w stanie w łatwy sposób wykryć i walidacja merytoryczna, czyli wykonanie reguły jakiejś, która jest na końcu de facto i możliwe, że wrócimy się na pierwszą zakładkę jeszcze raz przechodzić wszystko, bo źle wypełniłeś nie wiem podałeś. A nawet nie tyle co przy zadaniowych, ale też automatycznych. No bo walidujemy PESEL, tak, czy suma kontrolna jest OK, ale czy na tej pierwszej zakładce mamy walidować też jakieś tam pole, mam się wykonywać reguła z pola, który jest na kolejnej zakładce, bo my dzisiaj reguły automatyczne szykujemy, często przed etapem, a niepełne pole. Przynajmniej powiedzmy czasami po kilka etapów. I wiesz do czego zmierzam? Tak, że. W takim kontekście wizarda trzeba było szykować reguły automatyczne do tej sekcji. Przypisywać je jakoś do kroku.

**[Kamil Dubaniowski]:** Czy to może teraz?

**[Damian Kaminski]:** Żeby tu wykryć, że ktoś?

**[Kamil Dubaniowski]:** Znowu ta koncepcja Łukasza, tak, w sensie to obejście w sumie, ale może trzeba je dopracować, czyli zrobić taki. Dedykowany tryb etapu, tak, czyli etap, ale ma pod zadania, pod zadania opierające się na uzupełnianiu formularza. O czym to się? No w sensie, żeby diagram też się nie sypał przez to, żeby to był jeden etap aby diagramie, ale złożony z kilku kroków takich właśnie zbierania danych. Kilka kilka formularzy takich mniejszych, tam uzupełniać.

**[Damian Kaminski]:** Dobra, słuchajcie temat jest jak widać trudny, chyba trzeba go poruszyć, nie wiem czy my jesteśmy w stanie dzisiaj go omówić.

**[Kamil Dubaniowski]:** I wtedy mamy kod reguł, który?

**[Damian Kaminski]:** Chyba trzeba wymyślić najpierw koncepcję taką designerską przez nas to było najwygodniejsze mając naszą perspektywę i potem skonfrontować to tutaj.

**[Janusz Bossak]:** Tak, tak to jest.

**[Damian Kaminski]:** Zespołem deweloperskim.

**[Kamil Dubaniowski]:** Bo tak naprawdę w rozwiązaniu Łukasza jedyny minus, bo mam nad tym pełną kontrolę, może sterować sobie tym dalej, wstecz. Wszystko sobie opisuje w kodzie reguł, co ma się dziać, cofać, a jedyny minus tego jest taki, że jak masz nie wiem 10, no to diagram ci się rozsypie, bo aż 10 nadmiarowych etapów, które de facto są tylko zbieraniem danych, a etap to jest jeden uzupełnienie danych, taki proces.

**[Damian Kaminski]:** No. Diagram tak.


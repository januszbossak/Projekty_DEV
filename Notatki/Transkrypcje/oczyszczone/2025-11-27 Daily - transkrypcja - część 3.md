**Data spotkania:** 27 listopada 2025, 08:19 - część 3

---

**Janusz Bossak:** A ja nie mam być, bycie siły, też siedzę po nocach tutaj znaczy po nocach. No tam popołudniami robię sobie te. Analizy tych wszystkich spotkań, no mogę się zająć tym testami E2E, ale no nie chciałbym być w potem wąskim gardłem do czegoś tak znaczy, ja to już mam rozpracowane wiem jak to robić. Ktoś musi to robić, po prostu siedzi.

**Michał Zwierzchowski:** No ja też ja też nad tym siedziałem i też mam w sobie coś generował, więc też jakieś mam. Matko właśnie w później kwestia. No pisanie na tej.

**Janusz Bossak:** Trzeba to robić, po prostu to jest tak, to jest prawie że full time job.

**Michał Zwierzchowski:** Ten spór.

**Janusz Bossak:** A przynajmniej no pół. Pół czasu. Trzeba mieć to wpisane swojej kalendarz i po prostu dzień w dzień dzień w dzień, dzień w dzień coś tam dorabiać, sprawdzać ten Page Object Model, jechać kolejny elementy i tak dalej i tak dalej i tak dalej to po prostu jest robota.

**Michał Zwierzchowski:** Bo to znaczy, no no to muszę tam ten szkiełek tego wszystkiego tej planety do tego i to było kiedyś przekona dziewczyny przygotowane dziewczyny napisać jakoś tego nie piszą, ja teraz też.

**Janusz Bossak:** Dziewczyny to nie będą pisać. No dziewczyny nie będą pisać no to już tam już z nich rozmawiałem, nie.

**Michał Zwierzchowski:** No właśnie ja ja też chcę jakiś czas do tego wracam i tam próbuję teraz w tym ja, ale to też nie jest tak, że wygra. Page Object Model i tego, bo nawet do jakieś.

**Janusz Bossak:** To Michał, możemy się umówić tak, że pogadamy sobie osobno jakimś spotkaniu, bo ja mam tam jakąś metodykę wypracowaną. Muszę do tego wrócić.

**Michał Zwierzchowski:** No.

**Janusz Bossak:** I możemy to obgadać, tak?

**Łukasz Bott:** Słuchajcie, no to jeżeli ten może ja mógłbym jakoś to wesprzeć, to test tak, no jeżeli to by miało być, wiesz trochę tak na zasadzie, że nie wiem godzina dziennie tak czy coś.

**Janusz Bossak:** Łukasz. Masz zaległości z dokumentacją, więc nie rzucaj się jeszcze kolejne rzeczy.

**Łukasz Bott:** Wiem. Dobra, dobra, no to nie, no, rzucam propozycję swojej osoby, on może w ten sposób.

**Janusz Bossak:** Wolałbym, żebyś nadgonił dokumentację. Wolałbym, żebyś nadgonił tą dokumentację, niż brał na siebie kolejną rzecz, która też obciąży cię nie.

**Łukasz Bott:** Dobra. Jasne, jasne, jasne, ale w razie czego był zgłaszam swoją osobę, jakby się może potem jak ponad mgnieniu, no.

**Michał Zwierzchowski:** No ale to tak jak już dobrze no to trzeba dużo czasu na to poświęcić, bo tak z doskoku to tak nic z tego nie wychodzi, no.

**Janusz Bossak:** Tak znaczy, wiesz, ja, no dobra, to jest, nie, nie, nie gadajmy już na ten temat tutaj jedźmy z tymi zgłoszeniami, co tu mamy jeszcze do ustalenia?

**Kamil Dubaniowski:** Dobra, to już wracam, bo tak leciałem sobie przed kolejkę tych moich nie rozważam, jest to od Piotra dotyczące tej spacji podwójnej w raporcie co mówił na daily, on to zrobił dla starego i zgłosił wagę potencjalnie dla nowego to robić. Pytanie, czy chcemy? Czy o tyle to jest? Zależy w którą stronę patrzeć tak jak ktoś sobie właśnie skopiuje tak jak ten klient. I widzi inne dane, niż są na przykład na sprawie. No to można to uznać za bardzo, bo to jest pacje mogą później jakoś ktoś weryfikuje na raporcie mówi. No nie ma spacji takami reguła na przykład nie działa, a okazuje się, że na końcu słowa są 2 spacje i to się faktycznie nie wykonuje rynku. Więc no raczej powinniśmy mieć spójność danych. Nie powinniśmy ewentualnie jak już, no to zabezpieczyć po stronie formularzu, żeby te spacje ostatnie końcowe się usuwały. Ale, ale także na raporcie pokazujemy inne dane, niż są na sprawie. No to raczej jest błąd.

**Łukasz Bott:** Ale czekaj, Kamila to jest pacjent nie przyszły z zewnętrznego się była przypadkiem.

**Kamil Dubaniowski:** Tak no w tym wypadku tak, ale ja już mówię o takim, no bo to jest mega specyficzny przypadek, tak po co im te 2 spacje w kluczu? Nie wiem. No tak mają to jak było. Mm nie, nie oceniamy, nie wiem dlaczego, ale już mówię o takim przypadku biznesowym. Ktoś tam coś wpisywał z palca władował 2 spacje, a później na raporcie ich nie widzi i coś w kodzie na przykład nie wykonał. To już jakby pewnie będzie go.

**Janusz Bossak:** Tak trudno mi się do tego odnieść, bo to wymaga głębokiego zanurzenia się w ten temat, a pachnie mi to tak jak powiedziałeś tutaj jakimś wyjątkiem. Nie, że normalna zasada była taka, że oczyszczamy te spacje. No tutaj te dane przychodzą gdzieś tam zewnątrz i z jakiegoś powodu muszą takie pozostać, nie. No i. Tym jest jakby problem. Nie wiem, ja ja nie umiem.

**Kamil Dubaniowski:** Czy też nie rozumiem? Bo bo rozumiem, że no po co im kopiować? Oni właśnie tam było nawet na filmiku pokazane, że w źródle pokazujemy spację jak wszedł tam do naszych źródeł pokazał te dane z poziomu źródeł danych, są spacje na raporcie spacji po skopiowaniu ręcznie nie ma, ale po eksporcie danych z raportu spacje są więc. Co oni pojedyncze klucze kopiują. Nie mam pojęcia jak jest przypadek biznesowy, że oni kopiują z poziomu raportu, po prostu biorą sobie raport otwierają i kopiują z tabelki klucz. Nie wiem co oni dokładnie robią.

**Janusz Bossak:** Albo i nie, bo oni, bo może oni szukają, bo nie ponieważ wiedzą, że tam są podwójne spacje, to to piszą coś coś, spacja, spacja i drugi wyraz.

**Kamil Dubaniowski:** A. Albo wręcz z tego zewnętrznego systemu. Tak może kupiłem ten klucz.

**Janusz Bossak:** No.

**Kamil Dubaniowski:** Teraz płacą u nas nie ma.

**Janusz Bossak:** Ale to Piotr powiedział, no jeżeli to jest tak, no to powiedzmy, że to jest okej, no bo Piotr powiedział, że ta zmiana jego nic nie zmienia w bazach danych.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Jeżeli w bazie danych jest zapisane z formacjami, to pozostanie z 2 specjalnymi. To jest tylko i wyłącznie. Na frontendzie w raportach. Czyli można powiedzieć, że nasz frontend na raporcie jest. Zbyt. Tak i. No nie wiem inteligentny tak, że próbuję usuwać, że próbuję usuwa spację. Wyświetlaniu. A nie ma być taki inteligentny i nie ma usuwać. Tak znaczy chodzi mi też o taką sytuację trochę inną, bo my też usuwamy w wielu momentach na raportach różnego rodzaju znaczki HTMLowe. Tak więc, żeby to też jeszcze znaczy nie wylać dziecka z kąpielą, znaczy strasznie się boję takich właśnie. Specyficznych jak tutaj sytuacji. Które mogą mieć wpływ na to, co już robiliśmy wcześniej, bo pamiętasz tam pojawiały się na przykład te znaczki p. Paragraf i tak dalej i były tam gdzieś usuwanie, mamy jakiś wyświetlanie HTML też tam co się dzieje by jedno na drugie nagle jeszcze nie weszło i okaże się teraz poprawimy tu, żeby się jednak wyświetlały te 2 spacje, a za chwilę się okaże, że. Rozjeżdżają się jakieś tam inne rzeczy my? Dobra, nie wiem co z tym zrobić, nie wiem.

**Kamil Dubaniowski:** Na razie podeptana po prostu.

**Łukasz Bott:** Pytanie jest w tej chwili, jak to u klienta jest dla klienta jest to rozwiązane, tak.

**Kamil Dubaniowski:** Tak, dopóki nie przejdzie na nowy moduł.

**Łukasz Bott:** No to znaczy, że skoro jest to naprawione dla klienta i wiemy co jest naprawić i prawdopodobnie we frontendzie to zaplanujmy to na nie wiem na niekoniecznie na następny może na ten noworoczny sprint tak i tyle. Tak to w tym momencie już to chyba nie jest takie pilne, tak?

**Janusz Bossak:** To jest. Tak to jest AmRest i to dotyczy wyszukiwania zaawansowanego po prostu tylko stwierdził, że mam nowych raportach też tak się dzieje, to znaczy też usuwamy te spacje, ale z tego.

**Kamil Dubaniowski:** A nie czy nie ja inaczej kojarzę temat, czekaj mi się wydaje, że to był wczoraj analizowany to był tak krew. Taka jest to zgłosił, to nie AmRest.

**Łukasz Bott:** Pt.

**Damian Kaminski:** Znaczy mówicie o tych sytuacjach, o których mówił Piotr? Tak.

**Kamil Dubaniowski:** Tak.

**Damian Kaminski:** Bo nie wiem czy Janusz to dobrze interpretował byś tak nie chciałem szczytem wtrącać, ale według mnie tu tylko chodzi o to, że. W komórce są 2 spacje, a my wyświetlamy jedną zamiast wyświetlać czysto to, co jest w komórce.

**Kamil Dubaniowski:** To wręcz nie my, tak jak ja zrozumiałem Piotra tylko przeglądarkę usuwa.

**Damian Kaminski:** Tylko CSS. No właśnie w sensie my za pośrednictwem naszych styli tak, ale to interpretuje de facto przeglądarka, tak.

**Łukasz Bott:** No i może przeglądarka ma wiesz wyłączony jakiś interpreter, że jak ma 2 spacje po kolei to i tak zastępuje to jedno z pasją, nie?

**Janusz Bossak:** Tak.

**Damian Kaminski:** No może, ale to wynika z tego, jakie właśnie my mamy style na naszej aplikacji tak przeglądarka tylko je w jakiś sposób interpretuje.

**Łukasz Bott:** Im. Niedobra, ale to słuchajcie pytanie jest takie.

**Damian Kaminski:** No i się powinniśmy wyświetlać to jakie są dane, jeśli to zepsuje komuś innemu coś to tu będzie. Według mnie łatwo się odwołać do tego w ten sposób, że no dane są złe, może wcześniej to omijaliśmy, ale trzeba w takim razie poprawić dane. No to to też serwisowo w razie czego łatwo jest zrobić, no bo można po jakichś tam sprawach przeliterować i i wykasować spację na końcu czy podwójne spacje, jeśli by takie były. A ktoś by ich nie chciał tak, czyli wynika to już z błędów prowadzania.

**Kamil Dubaniowski:** Szymkowi tam nas.

**Janusz Bossak:** Gdzie jeżeli to jest prowo to niech tak Piotr zrobi jak mówił że.

**Kamil Dubaniowski:** Może Piotrek nie, nie chcę tego robić, no bo to React nam Przemkowi. Myślę, że ogarnie to raczej nie powinien zepsuć. Się szacować niestety dobra na następny sprint.

**Damian Kaminski:** Zanim zacznie robić to niech napisze co zrobi, niech ewentualnie wtedy no zakładam, że tam nie będzie dużo to będzie 5 zdań, więc Piotr może to przeczytać i wyrazić swoją opinię, skoro wie co trzeba zrobić i zrobił to w starych.

**Kamil Dubaniowski:** Dobra. No no na na następny sprint tego nie wrzucam zanim ten klient przejdzie na nowy raport, które mamy jeszcze niespokojnie. Cześć dałem na kolejny. Jak sugerował Łukasz, bo wydaje mi się, że są ważniejsze wagi, ten moment zaopiekowany nogent już jest. Na starym tak tu mam problem. Ja po stronie nowej listy pól dodaliśmy znaczy Filip dodał. Ten przycisk do odpalenia reguł tabeli. I problem polega na tym, że w starym mechanizmie. To okno otwierało się, ale link się nie zmieniał i był po prostu ten stary link formularzowy do. Listy listy pól, natomiast teraz lista pól ma już swój link Reactowy. To okno do edycji po kliknięciu tego przycisku się otwiera w nowej karcie i te przyciski, które są tutaj w ogóle nie reagują, one nie jakby. Nie wiem czy przerabiać je.

**Damian Kaminski:** No i co możemy z tym zrobić?

**Kamil Dubaniowski:** No właśnie tego nie wiem. Potrzebowałbym pewnie narady, że to dzisiaj umówić. Dzisiaj zjadłam. Dzisiaj zjadłam tak ta w sumie już jest rano.

**Damian Kaminski:** Już jest rada. No właśnie powiecie może to jest pierwszy krok, żeby już to przerabiać też na React, ale.

**Kamil Dubaniowski:** Dobra. To umówmy, to za chwilę nie ma co jeszcze zobaczyć, czy są jakieś ważne były błędy. To też Basia zgłosiła. Wiem o co chodzi i chodzi o to, że pozwalamy aktualnie na dodanie 2 sekcji o tej samej nazwie, bo nie jest to case sensitive, czyli jak jedna sekcja jest napisana z wielkim i tak druga z małej to można je dodać, a później jak dodajesz pole, to pole się dodaje losowo w albo pewnie w tej, która była dodana jako pierwsza i ty chcesz dodać do tej tak pewnie pewnie tak więc raczej chodzi o to, żeby no zrobić case sensitive.

**Damian Kaminski:** Mniejsze maili.

**Kamil Dubaniowski:** Nazwy sekcji i walidować, że już taka istnieje, więc to jest OK.

**Damian Kaminski:** To trzeba zrobić po 2 stronach, więc można zacząć od frontendu. A backend też powinien to mieć, no bo może ktoś równolegle robić. Ale już jak też nie ma frontendu to zakładam, że 90% mamy wyeliminowane, więc to znowu można dać chłopakom, żeby już to zrobili po stronie frontendu a zrobili do tego zadanie zaplanowane na później do backendu również.

**Janusz Bossak:** A jak to działało przedtem?

**Kamil Dubaniowski:** Właśnie sprawdziłem, bo to Basia zgłosiła w ogóle inny kontekst, zanim tam doszliśmy. W sumie Basia sama się zorientowała, że to chodzi o to, że publikowana tylko nie jest czułe na wielkość znaków. To tam wczoraj pod koniec dnia, więc dalej już nie szedłem. Nie, nie znam, zaraz odpalę tą marcową i zobaczę jak to wygląda.

**Janusz Bossak:** Dobra.

**Kamil Dubaniowski:** Dobra, powiedzmy jeszcze zostałem, bo to wczoraj było czy jeszcze nawet przedwczoraj ten limit sprawca nie możemy zdiagnozować tego dłuższego czasu pojawia się sporadycznie. Czy ja mam to komuś przypisać? Będziemy to analizować, czy zostawiamy, jak jest i uznajemy, że za pół roku znowu AmRest najwyżej się wkurzy.

**Łukasz Bott:** Nie, AmRest rosną.

**Kamil Dubaniowski:** Rosną tak.

**Janusz Bossak:** Warto by było to jakieś, ale to nie jest na tyle pilne, że skoro to się losowo pojawia co jakiś czas i da się to naprawiać.

**Kamil Dubaniowski:** To zróbmy tak, nie wiem.

**Łukasz Bott:** Znaczy to się samo naprawia.

**Janusz Bossak:** To.

**Kamil Dubaniowski:** Tak, to po kolejnym wykonaniu joba tak jak ja rozumiem.

**Janusz Bossak:** Ja podejrzewam ja podejrzewam. Rossmann ma 2 serwery, tam mnie load balancing tam tkwi problem to się jakoś skosztuję przez chwilę jest jakoś tak pójdzie zapytanie do jednego serwera, za chwilę one się skrzyżują i wyrównają i wtedy już rano.

**Kamil Dubaniowski:** OK, no dobra. Reszta to są moje dotyczące tabel z wczoraj możemy mieć na radę.

**Janusz Bossak:** No ja potrzebuję minuty zrobienie na razie.

**Kamil Dubaniowski:** Dzięki. Dobra.

**Janusz Bossak:** [zatrzymano transkrypcję]


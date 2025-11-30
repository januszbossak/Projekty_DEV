**Kamil Dubaniowski**: Przerwę troszeczkę, ale czy z tych raportów błąd ten dotyczący, że jak wejdę na sprawę, zrobię coś na niej i wracam na raport, to ona dalej tam jest, a według filtrów już być nie powinno – czy to możemy wrzucić na ten sprint? Bo to moim zdaniem jest na tyle krytyczne i irytujące, że...

**Damian Kaminski**: No.

**Kamil Dubaniowski**: Mamy przestrzeń.

**Damian Kaminski**: Jeszcze raz powiedz które?

**Kamil Dubaniowski**: Wchodzę na przykład na wycenę, anuluję ją, przenosi mnie z powrotem do raportu i sprawa tam cały czas siedzi, dopóki nie odświeżę całej strony. Nie powinno już jej tu być. Nie odświeża mi, nie działa – właśnie o to chodzi. A w ogóle działało to tak, że jak wracałem, to automatycznie mi odświeżał raport, nie musiałem nic klikać i ta sprawa znikała.

**Damian Kaminski**: Znaczy, nie całej strony, tutaj nie klikniesz "Odśwież". Jak to możliwe?

**Kamil Dubaniowski**: A teraz?

**Lukasz Bott**: Ale wiesz co, tylko moment. Mówisz o raporcie, czy mówisz o dashboardzie?

**Damian Kaminski**: Czekaj.

**Kamil Dubaniowski**: No tu pracuję, dokładnie tu. Teraz anuluję tematy, o których dostałem sygnał, że są nieaktualne. No i anulowałem.

**Janusz Bossak**: Tak i się nie czyści.

**Damian Kaminski**: No dobra, poczekaj. Czyli tak: było przygotowanie wyceny przez dział Dev, wpuściłem to do Janusza i teraz jak kliknę "Odśwież" to nie...

**Lukasz Bott**: No.

**Kamil Dubaniowski**: Tak. No. Pozostają.

**Damian Kaminski**: W sensie ma zostać, tylko powinien się zmienić etap.

**Damian Kaminski**: Bo to ma zostać, bo jest dalej aktywną... no zobaczymy.

**Kamil Dubaniowski**: No.

**Damian Kaminski**: No masz rację, to nie działa tu.

**Janusz Bossak**: No nie działa, nie działa.

**Damian Kaminski**: Bo to już jest etap "akceptacja wyceny przez dyrektora". No powinien przycisk "Odśwież" odświeżać stan tej zakładki.

**Kamil Dubaniowski**: Ale już...

**Kamil Dubaniowski**: Tak. No nawet po wykonaniu akcji, jak się wraca na ten raport, to wtedy było tak, że aktualizowało ci te dane. Jak nawet sprawa na przykład zmieniła etap i już nie powinna się tu pokazywać, to ona znikała. A teraz nawet, że się nie aktualizują dane, to sprawy nie znikają, przycisk "Odśwież" nie działa. Więc dla mnie to jest hotfix.

**Lukasz Bott**: Wiesz co, moim zdaniem do pilnej... Kamil, zgodzę się, do pilnej poprawki, bo to nie działa chyba w kontekście dashboardu. Jak masz dashboard, bo jakbyś miał ten raport wydzielony jako odrębny, to prawdopodobnie to, o czym mówimy, działa.

**Janusz Bossak**: To zróbmy taką próbę. Mamy gotowy raport, to możemy spróbować wydzielić go.

**Lukasz Bott**: Szybko to można sprawdzić, tutaj wejść do edycji.

**Janusz Bossak**: Jakikolwiek raport, który jest...

**Lukasz Bott**: Aby jakikolwiek inny, tak, gdzieś...

**Janusz Bossak**: Nie w dashboardzie. No taki.

**Damian Kaminski**: Jeszcze raz, co mam zrobić?

**Janusz Bossak**: Wejść na raport, który nie jest w dashboardzie.

**Damian Kaminski**: I porównać, czy to tak samo działa, tak?

**Lukasz Bott**: Tak.

**Janusz Bossak**: Na jakikolwiek, tak. I wejdźmy do sprawy.

**Lukasz Bott**: Tak, tak.

**Damian Kaminski**: Już, już wiem gdzie mam taki przykład. To od razu wejdę na taki przykład: Rejestracja. Wchodzę w sprawę.

**Lukasz Bott**: Stary. Ale to jest stary raport.

**Janusz Bossak**: To jest nowy.

**Damian Kaminski**: Nie stary, masz rację. Przepraszam, już robimy nowe.

**Janusz Bossak**: Jest, tam jest "Rejestracja".

**Damian Kaminski**: Tu bym wolał już przejść tędy, chociaż możemy zakładać, że to nie ma znaczenia. Rejestracja, nowy, wchodzę. Dotyczy pracownika, wskażemy jakiegoś indeksu.

**Lukasz Bott**: I to po indeksie powinieneś zmienić.

**Damian Kaminski**: I już zmieniło na indeksację, więc nie powinno być widoczne. To jest sprawa 666. Czy tu mamy ID-ki? Mamy, dobra. Klikam wstecz. Nie ma. Klikam "Odśwież". Działa. W raportach działa. No pozostaje pytanie, czy "Wstecz" powinno odświeżyć? Nie.

**Janusz Bossak**: Ale zniknęło dopiero po odświeżeniu.

**Damian Kaminski**: No.

**Lukasz Bott**: Wymuszenie "Odśwież" działa.

**Damian Kaminski**: Tak, tak, tak. No właśnie mówię, że tutaj przynajmniej to działa.

**Janusz Bossak**: Ale inaczej powinno być. Poczekaj, żeby mieć tę samą sytuację. Wejdź w ustawienia tego raportu i zmień tak, żeby okno się otwierało w pop-upie, a nie na zakładce.

**Damian Kaminski**: OK.

**Lukasz Bott**: No dokładnie. Tak, aby był... To jest faktycznie, otwiera się w zakładce.

**Damian Kaminski**: Dobra, 667.

**Janusz Bossak**: To samo zrób.

**Damian Kaminski**: Wybieram pracownika. Indeksuję. Zamykam. Wisi. Klikam "Odśwież". Nie ma.

**Janusz Bossak**: No przynajmniej tak powinno działać, tak?

**Damian Kaminski**: No to jest minimum. "Odśwież" powinno odświeżać. Akurat w tym wypadku, gdzie to było... no powinno skutecznie odświeżać, a teraz nie odświeża po prostu.

**Lukasz Bott**: To jest coś... trzeba to naprawić, bo nie wiem, chyba było naprawiane, albo nie wiem, bo też Ola... Ola miała na to [zgłoszenie]. U nas w Backu tam mają jakiś...

**Damian Kaminski**: Ale zobaczcie teraz, tylko kliknąłem...

**Janusz Bossak**: Macie issue.

**Damian Kaminski**: O, to było ciekawe. Że tylko kliknąłem w filtry. Jeszcze nie zdążyłem nic wybrać, albo no, nie zdążyłem już...

**Lukasz Bott**: No.

**Damian Kaminski**: Już się odświeżyło. Jest "akceptacja wyceny przez dyrektora Dev". No nic nie wybrałem, gdybym wybrał to by się wybrało, tylko kliknąłem w ten kafelek i odświeżył się cały ekran. I teraz już jest dobrze. Chciałem jeszcze sprawdzić co innego. Jeśli tu zrobię tak jak tutaj – to jest obsłużone. Nie, tutaj trzyma. Dobrze. No "Odśwież" powinno odświeżyć i znowu tę zakładkę, tak, żeby nie polecieli z całym.

**Damian Kaminski**: No to jest hotfix. Czy tam bug z pierwszym priorytetem. Według mnie można to wrzucać.

**Kamil Dubaniowski**: Czy mi się wydaje, że to już było zgłoszone? Ale nie wiem, czy było zgłoszenie faktyczne. Pamiętam, że na pewno o tym mówiliśmy już do tego.

**Damian Kaminski**: To jest frontend, więc tu jest proste rozwiązanie. Wywołanie jakiegoś backendu i endpointa i odświeżenie widoku, i tyle. Coś tu jest nieskuteczne. No według mnie to idzie w ramach tych ogólnie zgłoszeń szykowanych przez Janusza, więc trzeba to wrzucać Przemkowi i kolejkować tylko, ustawiać priorytety – co jest ważniejszym błędem, a co jest mniej ważnym.

**Janusz Bossak**: To jest denerwujące. Tylko dobrze by było ustalić, jak ma być.

**Damian Kaminski**: Znaczy, przede wszystkim przycisk "Odśwież" zawsze powinien odświeżać, bo to jest niezależne od tej strzałeczki powrotu. Bo ktoś może coś zmienić, czyli ja coś działam, a ktoś mi mówi "ja już tu przekazałem tę sprawę", bo jestem na callu, i klikając "Odśwież" nie widzę tego. Tak, to jest pierwsza rzecz. Inną rzeczą, według mnie odrębnym zgłoszeniem, to jest zdarzenie po przejściu strzałki, ewentualnie zamknięciu pop-upu. Czy to też ma generować z automatu odświeżenie, czy też nie? To jest już odrębny przypadek użycia.

**Janusz Bossak**: Wejdź jeszcze raz proszę w ustawienia tego raportu. I w opcje. I tam, gdzie właśnie jest to ustawienie tego, że to jest w pop-upie. "Wykonuje akcję podczas otwierania sprawy". O, tu jest coś, ale "po wejściu na sprawę zostanie"...

**Damian Kaminski**: Tak, tak, tak.

**Janusz Bossak**: Może wiecie, to w ogóle powinna być na przykład opcja tutaj. Jawna. Właśnie tego odświeżania. Ale nie, to nie ma sensu. Opcja ma się odświeżać i koniec.

**Damian Kaminski**: Znaczy pytanie inaczej. Znajdźmy, bo mamy pomysł i rozwiązanie potencjalne. Pytanie, kiedy to byłoby niepożądane? Czyli co może ewentualnie być przy tej zmianie negatywnie odebrane? Czy są jakieś takie przypadki, czy nam przychodzą do głowy?

**Janusz Bossak**: Znaczy, no przypadek taki: jeżeli nie zmieniam nic, wychodzę, no to bym chciał być w tym miejscu, co byłem.

**Damian Kaminski**: Powiedziałbym analogicznie. A no właśnie. I teraz chciałbyś być w tym miejscu co byłeś, ale zwróć uwagę: wchodzę do tej sprawy...

**Janusz Bossak**: A nie zmieniasz nic, to OK. Ale jak robię tak na przykład?

**Lukasz Bott**: Nic nie robili.

**Damian Kaminski**: Wybieram "Zapisz". Zamykam. Czyli wypełniłem ten wiersz. Jadę dalej, nie odpowiadam za przekazanie, ale odpowiadam za uzupełnienie jakichś parametrów i teraz jak jestem w drugim, to łatwo mi...

**Janusz Bossak**: Tak, no ale teraz zauważ, że gdybyś miał tutaj... Poczekaj, ale gdybyś miał tą... Zresztą możesz zrobić: weź to pole tutaj. Pokaż na tym raporcie, wejdź do edycji i pokaż to pole, które...

**Damian Kaminski**: Ono to będzie imię, się wypełni, już pokazuję. Patrz, już jest, nie.

**Lukasz Bott**: A no i Damian, a propos tego...

**Janusz Bossak**: No czyli to już jest błąd, bo ja bym chciał po wyjściu z tej sprawy, po zapisaniu i wyjściu, żeby mi się to odświeżyło tutaj.

**Lukasz Bott**: I słuchajcie, zgłosiłem to, rzuciłem wam na czata. Rzekomo to właśnie było naprawione, bo ja... to Ola właśnie utyskiwała i to miało być naprawione w boardach i raportach właśnie. Że właśnie tego typu sytuacja: wchodzę na sprawę w pop-upie...

**Janusz Bossak**: No ale rzekomo miało być, czy zostało naprawione? Czy zostało zmergowane?

**Damian Kaminski**: Według statusu zgłoszenia jest done. "Odświeżenie raportu tabelarycznego w dashboardzie nie wyświetla zmienionej wartości pola".

**Lukasz Bott**: Dokładnie to jest to, co przed chwilą zrobiliśmy.

**Janusz Bossak**: No to do jakiej wersji poszło?

**Damian Kaminski**: Na sprawie.

**Lukasz Bott**: Zobacz na dole.

**Damian Kaminski**: Ale poczekajcie, poczekajcie. Kliknięcie przycisku "Odśwież" w dashboardzie powoduje odświeżenie wartości raportów. OK, dobra. No do wszystkich.

**Janusz Bossak**: Ale dokładnie numerek, bo chodzi o to...

**Lukasz Bott**: Nie, release po...

**Damian Kaminski**: Dobra, D123. No dobra, może macie dobry trop. 122.

**Damian Kaminski**: No to trzeba poprosić Michała.

**Janusz Bossak**: Ale jeszcze raz tam zajrzymy, bo tam jest tylko mowa o tym kliknięciu.

**Damian Kaminski**: Tak, tu jest mowa o przycisku "Odśwież". Czyli naprawienie tego, co przed chwilą powiedziałem, że to powinien być totalny priorytet, że tu "Odśwież" odświeża ten stan. I to teoretycznie zostało naprawione. A nie to co mówimy, że dokonuje zmian na sprawie i czy to poprzez przejście strzałki wstecz, czy to po zamknięciu pop-upu. To nie dotyczy tego zgłoszenia, że tutaj wybieram coś, zapisuję, zamykam i z automatu mi się tu odświeża.

**Lukasz Bott**: Mhm. Zgłoszenie, Damian, które ja podałem, to właśnie dotyczy sytuacji z pop-upem. Właśnie takiej, że zostaje zmieniona wartość, "Zapisz", "X" i się nie odświeża, i to powinni poprawić.

**Damian Kaminski**: Nie, nie, nie. Czekaj. "Kliknięcie przycisku Odśwież w dashboardzie powoduje również odświeżenie zawartości raportu w aktywnej zakładce" – tak jest kryterium akceptacji.

**Lukasz Bott**: Tak.

**Damian Kaminski**: Czyli nie zamknięcie, tylko kliknięcie tego przycisku.

**Lukasz Bott**: Tak. Tak, tak, tak. No ale nie... no tak. Dobra, okej, wiemy o co chodzi.

**Damian Kaminski**: A to co mówisz, to już teraz tak: "Sprawa otwiera się w oknie. Zmieniamy wartość na wybranym polu. Po zamknięciu sprawy i kliknięciu na dashboardzie przycisku Odśwież wciąż się wyświetla wartość sprzed zmiany" – czyli dwa działania.

**Janusz Bossak**: Dobrze, trzeba zrobić kolejne zgłoszenie, które... znaczy pewnie kilka zgłoszeń i to można Przemkowi od razu podpiąć. Zróbmy tak. Bo: pierwsza sytuacja – i w raporcie zwykłym, i w raporcie na dashboardzie. Na razie mówmy o tabelarycznym, ale to też dotyczy Gantta, kalendarza. Ogólnie wszystkich tych raportów, w których się wyświetla pojedynczą sprawę. Czyli nie... źródła danych? Klikam sprawę, otwiera mi się ta sprawa i dokonuję w niej jakiegoś manewru. Tego typu, który pokazywałeś. Wybieram coś w polach, wpisuję, tak dalej. I według mnie to jest obojętne, czy klikam akcję jakąś, czy klikam "Zapisz" – nie ma znaczenia. Po powrocie do raportu powinienem być nadal w tym samym miejscu tego raportu i mieć odświeżone w tym rekordzie dane. To jest sytuacja, w której ten rekord nie zniknie z powodu zmiany danych w raporcie.

**Damian Kaminski**: Tego nie zrozumiałem. Nie zniknie? On może zniknąć.

**Janusz Bossak**: Ale nie, no to na razie opisujemy przypadek, kiedy nie zniknie. Jeżeli nie zniknie, czyli nie zmieni się stan filtrów na tyle, że on będzie nadal w tym miejscu. To moim oczekiwaniem jest, że będę w tym samym miejscu. Bo może ja przeglądam raport, który ma 100 pozycji. Wchodzę w każdą sprawę, wprowadzam jakąś wartość, zamykam. Następną – wprowadzam wartość, zamykam. Ale chcę być na tym raporcie.

**Damian Kaminski**: No tak, tylko to nie jest tak, że "nie zniknie". To czy on zniknie, czy nie zniknie, zależy od definicji tego raportu. Bo jak ty ustawisz zakres wyświetlanych danych – jak tu bym ustawił w filtrach...

**Lukasz Bott**: Tak, no i żeby zależało od tego pola, które zmieniasz.

**Janusz Bossak**: Ja rozumiem, ja to rozumiem, ale opisuję przypadek użycia.

**Damian Kaminski**: ...że nazwisko ma być puste. Nie jest puste, no to zniknie.

**Janusz Bossak**: Ale ja opisuję przypadek użycia. Przypadek użycia jest jednostanowy. Jeżeli mam sytuację taką, że po zedytowaniu danych w formularzu tej sprawy ona nadal będzie tutaj wyświetlana, to chcę być tak jak teraz – jesteś na przykład na czwartej pozycji raportu i żeby mi się to nie przesunęło na pierwszą, nie przeskoczyło gdzieś indziej. Chcę być tutaj. Jeżeli będę na piętnastej stronie tego raportu, to po wyjściu z tej sprawy chcę być na tej piętnastej stronie tego raportu i na tym konkretnym rekordzie, na którym byłem, tylko mają mi się odświeżyć dane. To jest przypadek użycia, kiedy ten rekord po tych zmianach nie zniknie. Drugi przypadek użycia jest taki, który spowoduje zniknięcie tego rekordu. Z jakiegokolwiek powodu: przeszedł na inny etap, nie spełnia wymogów, whatever. Co się ma wtedy wydarzyć? Jestem tak jak teraz na raz, dwa, trzy, czwartej, piątej pozycji. Wchodzę, coś robię i ten rekord znika. Co ma się wydarzyć po tym zniknięciu?

**Damian Kaminski**: No wydaje mi się, że za daleko idziesz.

**Janusz Bossak**: Nie no jak, no podstawowy przypadek użycia to jest...

**Damian Kaminski**: Bardzo konkretne potrzeby. No bo zobacz, mam do wypełnienia, jestem jakimś tam HR-owcem albo praktykantem najlepiej, bo to może być to – i moja odpowiedzialność polega na tym, żeby znaleźć dla tych dokumentów właściwych pracowników i tyle. Nie mam możliwości wybierania akcji, mogę tylko wypełniać formularz. Więc ja mam ustawione, że interesuje mnie tam, gdzie nazwisko jest puste. Wszedłem w tę pierwszą sprawę z 1118. Wybieram, zapisuję, zamykam, a tu w tym raporcie jest dużo więcej tych spraw, tu widzę tylko tam jakąś ograniczoną liczbę i teraz jeszcze się to nie odświeżyło. No ale ja mam filtr. Więc co ma się teraz pojawić tu, a jednocześnie nie zastosować tego filtru? Bo mi to zaraz zniknie. Teraz ta osiemnastka, bo ja już wypełniłem nazwisko.

**Janusz Bossak**: Nie. No i właśnie o to mi chodzi. Mówimy o tym, opisując ten przypadek użycia. Bo rozróżnijmy dwa przypadki użycia. Pierwszy przypadek – no to podejrzewam jest jakiś SignalR czy inny tam do wykorzystania. Tak, pierwszy przypadek: wchodzę w sprawę, wracam z niej i mają mi się uzupełnić imię, nazwisko, organizacja, data przekazania, tak? I chcę być w tym miejscu, w którym jestem dokładnie. Jeżeli jest to piąta sprawa z listy, to chcę być na piątej. Jeżeli jestem na trzeciej stronie, w piątej sprawie, to jak wrócę, to chcę być tutaj. Nie na pierwszej stronie, tak, chcę być tu, dokładnie w tym miejscu, tak samo jak było.

**Damian Kaminski**: Mhm. No tak, tylko dane mogą... to znaczy, no nie do końca. Wejdę tu. Wypełnię. Zapiszę. 1778, czyli ta. Odświeżam. Jestem tu i nawet mam. Ale to, że to mam, wynika z domyślnego ustawienia sortowania po ID. Bo jeśli te dane sortowałbym po nazwisku, to dla mnie byłoby naturalnym, że to zniknie. To znaczy, że ja źle korzystam z raportu.

**Janusz Bossak**: Czyli to jest trzeci przypadek użycia.

**Damian Kaminski**: Bo według mnie to, że ja zastosuję, że chcę działać tylko po nazwiskach, gdzie są puste... to jest już jakiś konkretny mój przypadek. I to znaczy, że ja już nie chcę tego widzieć. Ja chcę widzieć tylko puste, obsłużyć tylko te 102 pozycje, które są puste.

**Janusz Bossak**: Ja to rozumiem, no ale dobra, nieważne.

**Damian Kaminski**: Nie, nie wiem czy...

**Janusz Bossak**: Nie rozumiemy się w ogóle w tym.

**Damian Kaminski**: No właśnie się nie rozumiemy, ale nie wiem, czy ty nie idziesz w stronę taką już, że ktoś w ogóle nie myśli, co ma zdefiniowane.

**Janusz Bossak**: No bo nie wiem, co ma zdefiniowane. Jestem zwykłym użytkownikiem raportów. No ale widzisz, to ty mieszasz przypadki użycia. Jeszcze raz: pojedyncza odpowiedzialność. Jeżeli mówimy o jednym przypadku użycia, to nie mieszajmy do niego drugiego przypadku użycia. Przypadek użycia pierwszy jest taki, że nie są wybrane żadne filtry, nie jest wybrane, że jest puste czy niepuste i tak dalej. Jestem sobie teraz na którejś pozycji, tej którą wyświetlasz na przykład. Wchodzę, zmieniam, wracam i chcę być w tym miejscu.

**Damian Kaminski**: Mhm. No i tak jesteś.

**Janusz Bossak**: Tak.

**Damian Kaminski**: Według mnie teraz tak to działa, tylko nie ma odświeżenia. Czyli jak tu zmieniam...

**Janusz Bossak**: No i ma być odświeżenie.

**Damian Kaminski**: Jeszcze raz tu. 54. No to tak to zadziała, tylko jeszcze nie działa odświeżenie. Czyli teraz "zamknij okno" powinno odświeżyć. Obsługujemy ten wiersz 54. No i teraz jak go odświeżę to mam. Czyli to powinno się zadziać automatycznie.

**Damian Kaminski**: No dobrze, tylko to odświeżenie może mieć jeszcze kontekst sortowania.

**Janusz Bossak**: Ale to już jest następny przypadek użycia. No właśnie nie mieszaj przypadków użycia.

**Damian Kaminski**: No dobra, no to tu brakuje tylko wywołania przycisku "Odśwież" na przycisku X.

**Janusz Bossak**: Tylko pytanie, czy chcemy tu to odświeżać? Znaczy ja chcę uniknąć sytuacji, że trzeba klikać "Odśwież" tutaj.

**Damian Kaminski**: Tak, no rozumiem cię i według mnie to powinno tak działać. Natomiast chodzi mi o teraz ten inny przypadek. Specjalnie wrzucam w kontekście tego, że ktoś powie: "a mi to teraz się przesunęło". Ale to już wynika, że się przesunęło z tego, że tak jest skonfigurowany raport. To znaczy, że musisz sobie przestawić ten raport.

**Janusz Bossak**: Tak. No dobrze i teraz trzeba odpowiedzieć na pytanie: jak system ma się zachować w sytuacji, kiedy po tej kolumnie, w której coś zmieniamy – na przykład ta kolumna jest posortowana – jak ma się zachować? To my mamy odpowiedzieć. Jeżeli jak teraz wejdę i wypełnię i byłem w tym miejscu... to jak chcę jako twórca tego systemu, żeby ten system się zachowywał? To jest przypadek użycia.

**Damian Kaminski**: No ja chcę, żeby się... już pokazuję. Tu mam... w tej kolumnie mam... kurde, tu akurat nie mam. Czekaj, muszę to usunąć. Jestem na piątej, tu nazwisko jest wypełnione. I tu nie jest pierwsze niewypełnione. I teraz ja... no zobaczymy.

**Janusz Bossak**: No i teraz jest. To jest sprawa 9647.

**Damian Kaminski**: Tak, wypełniam nazwisko, tylko musi być... A no właśnie, dobra, wezmę Nowaka. Zapisz, zamknij.

**Janusz Bossak**: Nie, poczekaj, poczekaj, poczekaj. I teraz jest pytanie: jak chcemy, żeby się zachował? Bo jakie mamy scenariusze? Scenariusz może być pierwszy taki, że wypełni się ten rekord w tym miejscu, w którym jest. I koniec.

**Damian Kaminski**: Czyli jest wywołanie odświeżenia tego rekordu.

**Janusz Bossak**: Tego, ale nie sortowania.

**Damian Kaminski**: Nie sortowania, przez nie przejścia przez filtr i tak dalej.

**Janusz Bossak**: Dokładnie, i o to mi chodziło, i to jest przypadek użycia. Tak, czyli mówimy: jak wychodzę i zmieniają się warunki, czyli teoretycznie po tym polu jest sortowane... i teoretycznie powinno wskoczyć od razu gdzieś tam do Nowaka. Ale dla mnie jako użytkownika, który wypełnia teraz te puste pola, prawdopodobnie wygodnie jest zobaczyć, że to pole już mam wypełnione, przejść o pole wyżej, wypełnić to kolejne, wypełnić kolejne... I tu będzie Adamowski, Bramowski, Nowak, Kowalski i tak dalej. I widzę, że je wypełniłem. I teraz klikam "Odśwież" i teraz mi się posortuje.

**Damian Kaminski**: Mhm. Tak. No pytanie czy tak się da?

**Janusz Bossak**: To jest przypadek użycia o tym również.

**Damian Kaminski**: Tak, tak, tak. No to teraz dlatego chciałem to rozbić właśnie, że na taki przypadek, że wypełniłem ten wiersz, ale go już tu nie ma, bo właśnie to odśwież tak nie działa.

**Janusz Bossak**: To jest właśnie podejście: myślenie takimi przypadkami użycia. Jeden przypadek i teraz przypadek kolejny – ten, o którym mówiłeś słusznie, powinniśmy go rozważyć: co jeżeli wybierasz nazwisko "nie przypisano"?

**Damian Kaminski**: No to tu już... no okej, dobra, tak, masz rację. Co wtedy? Czy ma się wypełnić, czy ma zostać, czy jednak ma zniknąć? Czyli konsekwencja taka: co ma spowodować ten przycisk? Czy on ma być zbieżny z "Odśwież", ale wtedy zniknie nam to na podstawie tego filtru? Czy on ma – tak jak powiedziałeś – wypełnić ten wiersz i do momentu kliknięcia "Odśwież" nic tu ma się nie zmienić poza tymi danymi?

**Janusz Bossak**: Według mnie tak powinno być. Czyli wchodzenie w sprawę powinno powodować jej aktualizację wyświetlanego tutaj elementu i nieruszanie raportu. Bo ja może chcę iść teraz do następnego, następnego, następnego rekordu. I w którymś momencie, jak wypełnię sobie 5-10, to kliknę "Odśwież" i mi te na przykład teraz znikną, bo już nie są puste. Ale one się tu jakby wyświetlają nadal, bo ciągle nie odświeżyłem tego raportu – znaczy nie wykonałem "Odśwież". Odświeża mi się rekord jeden, a nie raport.

**Damian Kaminski**: Tak i tu cię rozumiem. Jeszcze patrzę, co tu się wydarza wtedy. Ale chyba nie odświeża. Czyli tak, ten ostatni... Aha, tu mam posortowanie.

**Damian Kaminski**: Nie, okej. Jest OK. Jeszcze patrzę, co robi ta paginacja, bo ona ciekawe też, jak wpływa.

**Damian Kaminski**: Damian Kamiński na sprawie 1488. OK, ona nie psuje, ona nie powoduje odświeżenia danych.

**Janusz Bossak**: No bo teraz w ogóle się nie odświeża.

**Damian Kaminski**: Znaczy, no nie wiemy tak naprawdę, co się dzieje w tle. No teoretycznie gdzieś z pamięci to odczytuje, tak? Bo przechodzę i ta sprawa dalej tu wisi, nie ma wypełnionych danych, mimo że one są wypełnione. Czyli gdzieś z pamięci musi to ciągnąć na podstawie poprzedniego pobrania danych przyciskiem "Odśwież".

**Janusz Bossak**: Wniosek myślę projektowy – według mnie, jeżeli się zgodzicie – jest taki, że w sumie bez względu na to, czy to jest raport ten... Chociaż nie wiem, teraz tak myślę o kalendarzu czy innym... czy w Ganttcie. To edycja samej sprawy nie powinna jeszcze przebudowywać tego raportu. Ale nie jestem pewien, bo teraz myślę o Kanbanie. Czy w Ganttcie?

**Damian Kaminski**: Znaczy, według mnie to powinny być... no właśnie niekoniecznie zbieżne zachowania w kontekście typu raportu.

**Janusz Bossak**: Tak. Dobrze, tak, tak, masz rację. Według mnie, dobra, na razie ograniczmy się do tego.

**Damian Kaminski**: Dlatego właśnie podejście takie, że na pewno to robi to... No doszliśmy do tego, że niekoniecznie to jest to samo. To mogłoby tak być, ale mogłoby być lepiej, tak jak właśnie zaproponowałeś, czyli wypełnia ten wiersz. Pytanie, co wtedy się stanie z paginacją? I no nie wiem, ja nie wiem jak to... Musiałbym na to spojrzeć, bo to jest z mojej perspektywy dość skomplikowana operacja, bo on musi tutaj wypełnić te dane. Czyli w zasadzie pobrać je ze sprawy.

**Janusz Bossak**: Dajcie tu Przemka.

**Damian Kaminski**: Tylko wiecie, powiem tak: ja powinienem się zająć rzeczami, które mam zaplanowane.

**Janusz Bossak**: OK, no dobra.

**Lukasz Bott**: Ja też.

**Damian Kaminski**: Więc myślę, że we czterech tu nie musimy nad tym siedzieć. Ale może Przemek zaproponować jakieś rozwiązanie. No i możemy wtedy się nad tym pochylić, co tu można zrobić. Czy to będzie tak proste, że tylko wyświetlimy? No ale właśnie, jak te inne elementy ekranu, jakie mają na to wpływ? Bo jednak jak przerzucamy dalej, no to on coś odświeża. I tutaj, jeśli on by trzymał to w jakiś sposób w pamięci, no to musi odświeżyć pamięć tego jednego wiersza, nie stosować filtrów, nie stosować sortowania, które teoretycznie jest narzucone. Więc to też pytanie, czy to przeskoczy? Bo jak tu przełączamy, to jednak coś się przeładowuje. No nie jest to trywialne.

**Janusz Bossak**: No ale dobra, wiadomo o co chodzi.

**Damian Kaminski**: Niemniej no konkluzja chyba jest taka, że może nie warto iść w "to równa się to". Bo jak potem będziemy chcieli jednak to rozbudować, to znowu będzie, że system jest niespójny. Raz dzieje się tak, a raz dzieje się tak. Więc może lepiej zachować na razie, że zamykamy i jeszcze się nic nie dzieje. Jak chcesz, żeby się zadziało – kliknij "Odśwież". I zastanowić się nad tym właśnie, co docelowo ma być tu. I wdrażać te zmiany nawet wolniej, ale konsekwentnie, niż zmieniać te zachowanie, że teraz będzie tak, a za miesiąc to będzie inaczej. Takie jest moje odczucie. Bo ktoś się też przyzwyczaja do jakiegoś trybu pracy, nie? I teraz jak tu będzie miał "Odśwież", a potem zobaczy, że nie ma tego "Odśwież" pod tym przyciskiem, tylko jest jakieś inne zdarzenie... no to wprowadzamy zmiany, które wzajemnie się wykluczają.

**Janusz Bossak**: Znaczy według mnie odrębnym przypadkiem użycia po prostu jest naciśnięcie przycisku typu "Indeksuję", typu "Akceptuję" i tak dalej. To jest według mnie odrębny przypadek użycia. Ten przypadek użycia może zmieniać stan tej sprawy dość drastycznie. Może ją przekazać do kogoś innego i tak dalej. I na wyświetlanych kolumnach może nie być tej informacji na przykład, że się zmienił etap. Bo na przykład się zmienił etap, albo że się wyświetla właściciela, bo może nie wyświetlamy właściciela. I Użytkownik może być zdezorientowany, że on coś zrobił, a ta sprawa nadal jest w tym miejscu. I jeszcze do tego niczym się nie zmieniła – znaczy nic się jakby z punktu widzenia wizualnego nie zmieniło na tym raporcie tabelarycznym.

**Damian Kaminski**: Bo tu wydaje mi się, że jest jeszcze inny przypadek użycia. Że zwróć uwagę, że ja mogę teraz kliknąć "Indeksuję". Muszę mieć wypełnione. "Indeksuję" i ja zostaję na tym pop-upie. I zamykam i te 17150 tu jest. A teraz wejdę tu i nie wiem w sumie co się zdarzy – i zmienię zachowanie przycisku "Indeksuję" na wyrzucenie.

**Janusz Bossak**: No dobra, no to już...

**Damian Kaminski**: Bo jeszcze jest to, że tego X-a już nie będzie, czyli "Wróć do listy spraw". I chyba wtedy nas z automatu wyrzuci.

**Janusz Bossak**: No jesteś na ...52. No i widzisz, teraz się nic nie wydarzyło.

**Damian Kaminski**: No właśnie. 52 i tu nic się nie wydarzyło. No właśnie, a może to powinno być inne?

**Janusz Bossak**: Znaczy według mnie, jeżeli to jest tak, że "Wróć do listy spraw"... W moim przekonaniu po wykonaniu – ale muszę się zastanowić, nie jestem pewien – powinna się odświeżać lista całości. Tak jakby już ta sprawa została inaczej posortowana i tak dalej, bo wykonałem akcję. Ale nie jestem przekonany. Muszę się, że tak powiem... chwilę głębiej zastanowić.

**Damian Kaminski**: No tych przypadków jest no niestety dużo, więc no tak, trzeba się nad tym zastanawiać.

**Janusz Bossak**: I dlatego ważne jest spisywanie tych przypadków użycia. Bo jak je się rozpisuje pojedynczo, to masz przegląd tych różnych przypadków po prostu. Tak, bo jak potem się dyskutuje tak jak tam z Przemkiem czy coś, to wszyscy mamy tendencję do patrzenia bardziej globalnie. Ale trzeba rozważyć konkret. Zresztą to, co mówiliśmy tam o tym Mateuszu – tak to zrobił zgłoszenie tam na tej 50. sekundzie filmu. On ma opisać przypadek, co ma się wydarzyć. No dokładnie tego samego dotyczy to, co teraz rozmawiamy. Co ma się wydarzyć, jeżeli użytkownik w takiej konkretnej sytuacji – bo to jest przypadek użycia, żeby opisać tę konkretną sytuację – zrobi tak? Czyli konkretną sytuacją jest: wyświetlam raport, wchodzę w sprawę, klikam przycisk akcji, a przycisk akcji jest ustawiony "Wróć do listy spraw". To jest przypadek użycia, to są warunki brzegowe tego przypadku użycia. Co się ma wydarzyć?

**Damian Kaminski**: No tak, tylko jest jeszcze to trochę zamieszane, że my to wiemy patrząc z punktu widzenia ekspertów systemu. A ktoś, kto korzysta, w ogóle nie wie, że tam jest jakieś "Wróć do listy spraw". Raz działa tak, raz działa tak – on w sumie nie wie z jakiego powodu. I to też pytanie, jaki jest odbiór użytkownika końcowego? Że tu na jednym raporcie to mi tak działa, a tu na drugim tak... Ja w ogóle tego nie rozumiem, czemu to tak działa? Nie? Że tu odświeża, a tu klikam X i teoretycznie wracam też, a tu nie odświeża. I też ten punkt widzenia według mnie jest do przemyślenia – czy nie za bardzo komplikujemy na przykład tak, że są różne zachowania w zależności od tego, jak tam jest w backendzie, a ktoś, kto tego używa, nie ma pojęcia, że jest w backendzie tak albo tak, bo on tego nie widzi.

**Janusz Bossak**: Bardzo dobra uwaga. No dlatego rozważamy przypadek użycia z punktu widzenia tego aktora, który to robi. Czyli jak bierzemy jako aktora tę przysłowiową panią Krysię z działu HR? I my powinniśmy wiedzieć, jak ona pracuje na tego typu raportach. Czy tam jakiegoś księgowego, czy panią w kancelarii, czy kogokolwiek innego. I naszym zadaniem jest domyślać się, a jak nie domyśleć się, to zapytać. Uśrednić w pewnym sensie te tryby pracy i właśnie spowodować wygodniejszą wersję.

**Damian Kaminski**: No tak.

**Janusz Bossak**: Tak, ale chodzi mi o to, że to, co powiedziałeś, wcale tak nie musi być, że ktoś będzie zauważał, że to działa inaczej. Dla niego będzie to działało intuicyjnie. Czyli raz będzie znikać, ale dla niego to jest oczywiste, że no przecież oczywiste, że skoro zmieniał etap...

**Damian Kaminski**: Nie, ja nie oceniam teraz, czy to jest lepsze, czy to jest lepsze, czy to powinno być różnie. Tylko właśnie mówię, że ktoś właśnie patrząc na to z boku stwierdzi – no właśnie tak jak mówisz – albo to jest intuicyjne, albo to jest niezrozumiałe. Bo tu działa tak, a tu działa tak. W zasadzie tu edytuję, tu przyciskam przycisk, tylko tu dodatkowo klikam X, nie? Dla niego to jest kliknięcie X-a – system zachowuje się inaczej.

**Janusz Bossak**: No... I to jest nieintuicyjne w momencie, kiedy on się nad tym zastanawia.

**Damian Kaminski**: No.

**Janusz Bossak**: Na tym to polega, nie? Pewnie będzie cała masa przypadków i duża przestrzeń sytuacji, gdzie coś, co jest dla jednego intuicyjne, dla drugiego nie będzie nadal intuicyjne.

**Damian Kaminski**: No na to nie mamy wpływu, to są różne...

**Janusz Bossak**: Na to już nie mamy. No dobra. Podsumuję sobie to tutaj w transkrypcji spotkania i...

**Damian Kaminski**: No tak, chyba powiedzieliśmy o tym dość skrupulatnie, więc tam pewnie kilka przypadków będziesz w stanie opisać.

**Janusz Bossak**: Dobra. To tyle na razie.

**Damian Kaminski**: Cześć.

**Janusz Bossak**: Dzięki, hej.
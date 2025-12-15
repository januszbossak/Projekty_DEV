**Data spotkania:** 9 grudnia 2025, 12:30 - część 3

---

**Damian Kamiński:** Tutaj. Upuść pole tutaj, tu moglibyśmy napisać na kwadratowych nawiasach puste 5, puste 6, puste 8.

**Kamil Dubaniowski:** Wymaga zmiany backendzie i to już poruszyłem. Też czekamy na w sumie jakiegoś wykładowcę, bo aktualnie.

**Damian Kamiński:** Tylko. Mhm.

**Kamil Dubaniowski:** To jest tak, że musielibyśmy po dodaniu każdego pola zaciągać cały formularz na nowo, więc powiedzmy, że nie wydajnie, bo te pola jeszcze fizycznie nie istnieją. One tylko są tu takimi wydmuszkami, dopiero po kolejnym ładowaniu formularza. One są gdzieś tam w backendzie wyciągnięte, ja zasugerowałem.

**Damian Kamiński:** Jak to, nie nie rozumiem.

**Kamil Dubaniowski:** No jeśli dodasz teraz nowe pole, na przykład nie wiem tam tekstowe krótkie.

**Janusz Bossak:** Znaczy, nie istnieją.

**Kamil Dubaniowski:** I wrzucisz je gdzieś do nowej linii? No tutaj dorzuciłeś do tej co już istniała, ale OK, to po prawej, tak tak.

**Damian Kamiński:** No nowy proszę cię, a jak do nowej.

**Kamil Dubaniowski:** To to po prawej co się dodało automatycznie nie istnieje. To nie jest pole puste.

**Damian Kamiński:** No mam. Takie tak, kiedy zaistnieje.

**Janusz Bossak:** Jak wyjdziesz z tego?

**Kamil Dubaniowski:** Ja rozumiem to tak, że dopiero przy ponownym ładowaniu formularza, czyli jakoś w tym momencie dopiero, ale to trzeba sprawdzić z Piotrem, natomiast ja zasugerowałem, żeby teraz jak ty puszczałeś to tekstowe krótkie 2.

**Damian Kamiński:** Mm. No ale to.

**Kamil Dubaniowski:** To, żeby tak naprawdę do bazy poszło od razu 2 to tekstowe krótkie.

**Damian Kamiński:** Poczekaj, polewali darowane, przełączam się na listę.

**Kamil Dubaniowski:** Sprawdzę ściany.

**Damian Kamiński:** Walidowane puste 2.

**Janusz Bossak:** No ale to jest już efekt, znaczy nie wiem, trzeba sprawdzić.

**Damian Kamiński:** Niemożliwe, że nie istnieje w sensie przecież od.

**Janusz Bossak:** Kiedy i gdzie strzał do bazy?

**Damian Kamiński:** To co ja w momencie jak wychodzę, to jest strzał do bazy.

**Janusz Bossak:** Tak. No bo znaczy, a weź wstaw między pola 2, ale nie pole, linię pustą.

**Damian Kamiński:** No a jak wyłączę aplikację? No dobra, numeryczne tutaj. OK linie i przechodzę na inną zakładkę i odświeżam, czyli tamta cały czas istnieje.

**Janusz Bossak:** I ta nie istnieje. I nie tego nie będzie. I nie będzie 2 pustych.

**Damian Kamiński:** Mm. Czekajcie, to jest pole walidowane puste, puste puste.

**Janusz Bossak:** Nie ma takiej sytuacji.

**Damian Kamiński:** Pole walidowane pusty. No dobra, zgadza się, tylko to wtedy jest bez i tu rozumiem i tu nie ma, bo to jest bezzasadne, bo to jest brak wiersza, ale jak już dodam numeryczne.

**Janusz Bossak:** Będziesz?

**Damian Kamiński:** Tu i teraz przejdę tu, odświeżę, to według mnie teraz się pojawi, bo już istnieje wiersz numeryczne puste 3. Tylko sekundę, coś mnie tu niepokoi, mocno tu było puste 3 za numerycznym jeden, wprowadzam numeryczne 2.

**Janusz Bossak:** I one się przed przemianą.

**Damian Kamiński:** No tylko czekaj, to tak nie może być. Numeryczne. To nam rozwala wszystko. W sensie? To jest bardzo duże ryzyko, jeśli tak jest.

**Janusz Bossak:** Co?

**Damian Kamiński:** Dlaczego już tłumaczę, bo teraz tak. Oni mogą chcieć, żebyśmy układając tutaj formularz. Mm. Ja mogę ukrywać to pole puste 2, bo to jest.

**Kamil Dubaniowski:** Tak, tak, to już było podnoszone dawno, do tego zmierzam, że mamy tutaj brak duży względem starej listy.

**Damian Kamiński:** A, czyli, że to trzeba zaopiekować, tak?

**Kamil Dubaniowski:** Tak, to jest główny cel, żeby z tego poziomu już była świadomość, że to jest pole, żeby ten tekst właśnie puste tam 1, 2 się dodał, żebym ja mógł wejść w edycję ustawienia tego pola pustego, ale co więcej, to musi być tak, jakby nadal ta sama funkcjonalność, że jeśli ja w to miejsce upuszczę inne pole, to jakby zastępuje to puste już innym polem, bo to nadal jest taki.

**Damian Kamiński:** OK.

**Kamil Dubaniowski:** Pusty tak.

**Damian Kamiński:** Znaczy powiedziałbym z tą edycją, to już jest kolejne MVP, natomiast te puste według mnie często są obsługiwane w regułach, więc ja zmierzam tylko do tego, że dodając kolejny wiersz, dodając kolejne pole. To to w tym momencie ustawia się jako puste 2, a tak według mnie nie powinno być, po co renumeracja pól. Puste 9, bo ja chcę zachować wszystko, co jest w regułach, bo tu jest w regule odniesienie, że puste 2 to wyświetleń mi tylko wtedy, kiedy ten numeryczne jest, powiedzmy, niewypełnione albo wypełnione coś takiego, bo my teraz wprowadzając numerację za każdym dodaniem nowego pola, wywalamy całe reguły. On powinien dodawać nowe pole z wyższym auto incrementowym.

**Kamil Dubaniowski:** No jak teraz zastąpisz i wrzucisz chcesz to w to pole?

**Janusz Bossak:** Ale jakie reguły się wywalają, co mają, co mają reguły wspólnego z pustymi polami.

**Kamil Dubaniowski:** Z moją byłą może sterować widocznością pustego, żeby formularz w nadanym.

**Łukasz Bott:** No mogą mieć.

**Damian Kamiński:** Mają. I to dużo częściej regułami niż tutaj bym powiedział.

**Łukasz Bott:** Tak to jest, jak już to jest tak, to jest częsty trik właśnie.

**Damian Kamiński:** No zobacz, to jest faktycznie pole na backendzie, to jest faktycznie pole puste, to tak jakbyś nagle pole walidowane dodając sobie tutaj kolejne pole walidowane od góry, to byś sobie stwierdził, nie to będzie jeden, a to 2, a to 3. No tu mam źle to ułożone, musiałbym zaraz ci pokażę do czego zmierzam, jest.

**Janusz Bossak:** Wiem, wiem wiem, rozumiem, ma rację, jest niezależny od położenia.

**Damian Kamiński:** Wiesz, mam mam tak. Tak i teraz, i teraz dodaję pole walidowane tu i wszystkie te 1, 2, 3 zmieniają numer o jeden wyżej. Po prostu pola puste powinny być auto incrementowane w kontekście nazwy. Dodaję sobie nowe OK. Niech on się nazywa puste 58, żeby nie wpłynęło to na to wszystko co ja już mam poukładane w regułach.

**Janusz Bossak:** No i tak i nie, tak i nie.

**Kamil Dubaniowski:** Ale to zobacz, że te pola puste tworzą się automatycznie po wrzuceniu jakiegoś pola do.

**Janusz Bossak:** No i później potem usuniesz to pole się usunęła.

**Kamil Dubaniowski:** Więc co? No właśnie i.

**Damian Kamiński:** No dobrze, jeśli usunę to pełna zgoda, ale jeśli one są. To jak ja dodaję nowy, wiesz, bo chcę tu wstawić.

**Janusz Bossak:** No jak jak usuwam tu też wpływa na reguły tak.

**Damian Kamiński:** Jako usuniesz pełna zgoda, ale przeważnie dodajemy ani usuwamy.

**Janusz Bossak:** Czy wydaje mi się to jakiś nie wiem, znaczy w życiu nie robiłem żadnych reguł na pustych polach, o tak bym powiedział, nie widzę potrzeby robienia reguł na pustych polach.

**Kamil Dubaniowski:** Nie nie, uprawnienia najczęściej, czyli jak masz na jakimś etapie ukryte inne pole na przykład nie wiem. Imię ukrywasz na danym etapie, to jest całe przesunięcie wiersza i teraz dodajesz sobie to pole puste w miejsce tego pola imię, które na danym etapie się ukrywa, żeby nie przestawić się inne pola i to puste. Nie wiem.

**Janusz Bossak:** Pole puste. Z reguły.

**Łukasz Bott:** Nie pole masz dodany, natomiast regułą sobie je odkrywasz, albo ukrywasz i wtedy wizualnie na formularzu wizualnie się pojawia luka, albo nie.

**Kamil Dubaniowski:** Tak. Gość na danym etapie.

**Łukasz Bott:** Ja Janusz również, że.

**Janusz Bossak:** Ten mechanizm to trzeba ten mechanizm poprawić i to jest rzecz, która już od dawna wisi do poprawienia. To, co już kiedyś tutaj jeszcze jak Christina była, Kamil proponowaliście, tam zarządzanie wierszem jako takim. I sytuacją, w której w jakimś miejscu chcę mieć to, albo to, czyli jedno lub drugie pole, czyli wybieram coś w pierwszym na przykład pole walidowane pierwsze to poszły, że to byłby Słownik i w drugim miejscu tam po prawej stronie chcę mieć alternatywnie w zależności od wybrania tego czegoś w polu pierwszym, jak nic nie wybrałem to ma być puste, jak wybrałem to ma być. Na przykład data, a jak wybrałem coś innego to ma być PESEL. I o to chodzi, żeby można było w jednym miejscu wyświetlić 2 różne typy pól. Teraz jest to kompletnie niemożliwe do uzyskania.

**Damian Kamiński:** Na tym formularzu, bo ogólnie jest.

**Janusz Bossak:** Może żadnym nie występujesz tym w ten sposób. Chyba, że umiecie zrobić.

**Damian Kamiński:** No jak.

**Łukasz Bott:** No to pewnie da się, tylko to jest taka gimnastyka w regułach.

**Janusz Bossak:** No właśnie, znaczy według mnie się nie da, ale.

**Łukasz Bott:** Że na pewno nie jest, nie jest to łatwe.

**Janusz Bossak:** Mamy szczególności w tabelce.

**Damian Kamiński:** Nie. W tabeli to OK, w tabeli, ale tabela. To jest zupełnie inna kwestia według mnie. Jeśli walidowane jeden nie jest puste. Realizowane 2 i hide.

**Janusz Bossak:** Dobra, dobra.

**Damian Kamiński:** Dobra sekundkę teraz. Poprzestawiał. No OK teraz. Chodzi o to, żeby 2 i 3 zmieniało się tutaj, tak.

**Janusz Bossak:** W jednym miejscu, żeby było albo to albo to.

**Damian Kamiński:** Mhm, mhm.

**Janusz Bossak:** No dobra, słuchajcie.

**Damian Kamiński:** Dobra, przejdźmy dalej, ja najwyżej.

**Janusz Bossak:** Znaczy trzymaj.

**Damian Kamiński:** Zaraz tutaj dorobię, bo to trzeba.

**Kamil Dubaniowski:** Dobra, tak, bo powinniśmy kończyć.

**Janusz Bossak:** Więc się zasad. Czas nam się skończył. Nie przedłużajmy, jedźmy dalej z tematami i może my sign up mieć więcej, jeżeli jest okres taki, kiedy potrzebujemy tego do określania różnych rzeczy, ale też się nie rozwodzimy, że tak powiem. Drobiazgami raczej.

**Damian Kamiński:** Mówisz, że to jeszcze jest uporczywe, przy przesuwaniu mi się na siłę to otwiera?

**Janusz Bossak:** No może tak ktoś by chciał się to jest dowieść, że nie wiadomo kto jakby chciał, tak jakby chcieli tak nie.

**Kamil Dubaniowski:** Ogólnie jest tutaj.

**Damian Kamiński:** Nie, jak według mnie przesuwam to nie jest to, jak klikam to oczywiście, ale jeśli przesuwam to po co mam mi się to otwierać.

**Kamil Dubaniowski:** No pewnie tak i zauważcie też, że w momencie kiedy ten prawy panel wyjeżdża i nie macie miejsca, to zmienia się też rzeczywisty układ formularza i to jest mega mylące czasami, bo. Dodajesz jakieś pole, miejsce, upuść pole tutaj i ono de facto nie dodaje się w tym miejscu, co ty widzisz. Tylko dodaje się gdzieś tam niżej, bo układ jest 3 kolumnowy, to widzisz 2, 2 kolumny jest takie, trochę zakłamanie rzeczywistości, ale nie da się inaczej.

**Janusz Bossak:** Czy? Powinno być tak, że prawy rozwijanie prawego panelu nie powinno przynajmniej w jakimś stopniu wpływać na zmianę układu, że jak mamy układ 3, to najwyżej niech będą węższe te kolumny, ale nadal 3.

**Kamil Dubaniowski:** Myślę, że do tego powinniśmy dążyć, bo tak jak mówię ja w pierwszym momencie zgłosiłem to jako bug, bo nie załapałem sam. Na początku możesz Damian zrobić tak, żeby rozwinąć prawy panel na jakimś polu, żeby ci się nie mieściło tak jak miałeś wcześniej, czyli rozwiniesz, czy to? No i teraz złap jakiekolwiek nowe pole i upuść je gdzieś tam w tych wolnych przestrzeniach.

**Damian Kamiński:** Tak. Mhm.

**Kamil Dubaniowski:** No to jest OK. To musi być. Nie pamiętam już w przypadku, albo to w pierwszej linii.

**Damian Kamiński:** Tu.

**Kamil Dubaniowski:** Te niżej po prawej. O tu. Tak. SPK. Możliwe, że już to poprawił.

**Janusz Bossak:** Nie, to jest OK, znaczy jak puszczasz chyba w miejsca wyznaczone, ale chodzi o to, że o to wygląda źle, bo jeszcze jakbyś zrobił czterokołumnowe, to w ogóle będziesz miał, będzie wyglądało jak dwukołumnowy.

**Damian Kamiński:** Może powinniśmy wtedy wprowadzać jakieś linie?

**Janusz Bossak:** No to jest ta koncepcja wiersza.

**Damian Kamiński:** Albo zmniejszyć szerokość pola po prostu, nie ma innej opcji.

**Janusz Bossak:** Według mnie powinniśmy zmniejszyć szerokość pola, nawet jeżeli to nie będzie proporcjonalne do tego, co jest na formularzu, ale to jest edytor tego pola, a nie formularz tak jako taki do pracy, więc według mnie ważniejsze jest w moim przekonaniu utrzymywanie tego podziału na 2, 3 czy 4 kolumny, bo wtedy wiem na czym pracuję, tak jak ten formularz będzie wyglądał. To jest ważniejsze niż to, że trzeba tutaj ten jedną kolumnę przenieść niżej. No bo po co? Z drugiej strony jak ktoś będzie chciał testować przypadek, a co się stanie, kiedy będzie węższy formularz, to jednak powinno przeskakiwać tak. Dobra, ja muszę lecieć, idę.

**Kamil Dubaniowski:** Możliwe, że mnie nie złapiecie przez moment, bo mi bateria pada, a nie mam prądu, zapowiadali, więc jakaś awaria musi być.

**Janusz Bossak:** Od Dynamo do roweru przełączyć doładować.

**Kamil Dubaniowski:** Tak jest.

**Janusz Bossak:** Na razie trzymajcie się, dzięki.

**Kamil Dubaniowski:** No hej.

**Damian Kamiński:** Cześć.

**Kamil Dubaniowski:** Zatrzymano transkrypcję.

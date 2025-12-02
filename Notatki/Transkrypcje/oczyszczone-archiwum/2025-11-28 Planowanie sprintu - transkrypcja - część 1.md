**Data spotkania:** 28 listopada 2025, 11:02

---

**[Damian Kaminski]:** Cześć.

**[Lukasz Bott]:** Z tej rzeczy.

**[Damian Kaminski]:** Rozwiązała się nieco ta kwestia proxy.

**[Lukasz Bott]:** Jeśli o proxy.

**[Damian Kaminski]:** Co rano omawialiśmy, to co napisałeś komentarz, nawet to już wiem nieco więcej na ten temat.

**[Lukasz Bott]:** Którego klienta było w końcu?

**[Damian Kaminski]:** Od tego trzeba zacząć – bank Pekao. To nie jest trywialne, w sensie nie jest do zrzucenia, tylko że tu jest opis zły, bo po prostu pisała to koleżanka, która ma jeszcze małe doświadczenie i za mało napisała. Tu chodzi o to, że ten bank – teraz już rozumiem, że bank, to nie ma co dyskutować z ich podejściem do bezpieczeństwa. Tu chodzi o to, żeby wykorzystać ten mechanizm, który my mamy na proxy, bo my mamy dzisiaj możliwość definiowania proxy tylko w ramach tego naszego. Proxy nie są obsługiwane funkcje typu get data from GUS albo get data from GUS, ten ex. Ja bym powiedział, że to trzeba inaczej. To nie tak, że my powinniśmy to wpiąć, że te wywołania mają iść tędy. Tylko poprosiłem to w tym zgłoszeniu Adriana. Nie wiem, jak ta lista, czy ta lista jest łatwo wyciągana, ale w mojej opinii to powinno być tak, że...

**[Lukasz Bott]:** Dzięki, że się tym zająłeś. Osiadł tu, nie wiem, to, ale to tak wyszło przed.

**[Damian Kaminski]:** Nie, ja się nie zająłem, tym to wyszło przy okazji, bo czekaliśmy jeszcze tam na WIM, więc tam zwróciłem uwagę właśnie Mateuszowi, żeby oni najpierw konsultowali to wewnętrzni, tutaj też zaraz to może omówimy. Bo on powiedział, że...

**[Lukasz Bott]:** Odpisałem, to nie chodzi o to, żebym zrzucił na drzewo, tak tylko w tym duchu, że czy na przykład coś takiego, jak rozmawiali z klientem, tak, czy to przedstawili, tak, bo takie najczęściej.

**[Damian Kaminski]:** To dobrze odpisałeś. Tak przedstawili, w sensie tu jest inna kwestia. Chodzi tylko – czekaj, czy klient? Klient po prostu nie odpowiesz. To jest bank tutaj, nie że tak powiem, w ogóle powiedzą, że nie i koniec, bo to jest bank. Kwestie Security to są...

**[Lukasz Bott]:** Ale to jest bank dopiero, z którym zaczynamy rozmawiać.

**[Damian Kaminski]:** Ja nie wiem, czy PKO nie jest według... znaczy ja nie słyszałem, żeby był naszym klientem.

**[Lukasz Bott]:** Właśnie o to mi chodzi, że taka...

**[Damian Kaminski]:** Ale według mnie to już jest wdrożenie, tam idzie, więc raczej jest już naszym klientem.

**[Lukasz Bott]:** Skoro o to pytają...

**[Damian Kaminski]:** Skoro już o to pytają na takim etapie, to według mnie jest to... nie wiedzieliby o tym na etapie planowania czy wyceniania, bo nigdy tego nie sprawdzą aż tak drobiazgowo.

**[Lukasz Bott]:** Wiesz co, zależy jak były prowadzone rozmowy i czy na przykład podczas rozmów brały po stronie banku ich dział IT Security mógł o to zapytać, tak, chociaż też mogliby być tego nieświadomi.

**[Damian Kaminski]:** Już pytam, jakie są deadline i czy jest w trakcie wdrożenia. Według mnie, bo na to będzie wycena.

**[Damian Kaminski]:** To jest dedykowane dla niego, my to możemy, oni nie mogą, bo mają wewnętrzne procedury i to jest jasne, ale według mnie to powinno być w ustawieniach. Teraz tutaj powinniśmy dołożyć: używaj proxy dla modułów i tu checkboxy, i to będzie wtedy super uniwersalne dla jednego tak, dla drugiego tak, dla piątego tak. Wszyscy – ktoś chce wszystko przez proxy, a ktoś powie: a ja chcę kolorystyki, żeby szły bezpośrednio, a albo inaczej wszystko ma iść przez proxy, a SMTP ma nie iść przez proxy. Może nawet nie idzie dzisiaj.

**[Lukasz Bott]:** Może możemy ten...

**[Damian Kaminski]:** Dlatego niech Adrian zacznie od tego – poprosiłem Adriana, bo Adrian to już badał, ponoć oni konsultowali to z nim. Żeby wymienił, które moduły dzisiaj idą przez proxy. Można by było według mnie to w takim kierunku powinniśmy iść i potem najwyżej będziemy tu dokładać kolejny, kolejny, kolejny, który tam ktoś będzie potrzebował.

**[Lukasz Bott]:** Dobra, dzięki za to, że rozmawiałeś i przy okazji to wyszło.

**[Damian Kaminski]:** Bo ja też powiedziałem, że na drzewo z tym zgłoszeniem, ale dopiero jak Mateusz je rozwinął, podał klienta i dopiero dał jakiś kontekst, to to, że tak powiem, nabiera to jakiegoś sensu i rangi.

**[Damian Kaminski]:** Właśnie to też trzeba dopisać do zlecenia – jest wycena, a nie że my to robimy.

**[Lukasz Bott]:** W tym w ogóle tego w ogóle to PI nie powinno się pojawić, tak.

**[Damian Kaminski]:** Właśnie, bo tu stąd to uruchamiamy i wtedy to wiąże, tak.

**[Lukasz Bott]:** Chyba że... Nie, nie chodzi o uruchamianie, tylko po prostu może tak na tipsach czy gdzieś tam czy dzwoniąc tak zapytać się właśnie o te możliwości? Nie, czy jak konsultowali z Janem, Adrianem, może trzeba uczulić, że nie powinni tego na to PI robić, tylko powinni właśnie wycenę, bo to nie jest błąd, a AMODIT tak, no my mamy rozwiązanie, tak.

**[Damian Kaminski]:** Ty masz admina dlatego procesu.

**[Lukasz Bott]:** A to czy ci trzeba to zmienić?

**[Damian Kaminski]:** To jest bullshit. To jest za mało. Ja bym to nawet dał, że my możemy to edytować przy prośbie o wycenie, gdzie dokładnie jeszcze zbiera, skoro my to opiekujemy na razie tak jest przyjęte do wyceny, to żeby już tego nie cofać, nie da się zresztą cofnąć. Chyba że jak przypiszę siebie, to może...

**[Lukasz Bott]:** Tak.

**[Damian Kaminski]:** Zadaj pytanie, to jest to dodanie komentarza. Pewnie tak.

**[Lukasz Bott]:** Tak, na przykład z prośbą, bo ten...

**[Damian Kaminski]:** Ale to cofnie wtedy na ten etap, nie wiem.

**[Lukasz Bott]:** Moment.

**[Damian Kaminski]:** Czekaj, jest może go to tu podejrzeć?

**[Lukasz Bott]:** Proces wyceny.

**[Damian Kaminski]:** Przygotowanie prośby o wycenę, zadaj pytanie, gdzieś cofa.

**[Lukasz Bott]:** Nie mamy takiego procesu.

**[Damian Kaminski]:** To raczej jest po prostu wrzucenie komentarza.

**[Lukasz Bott]:** Jakby to się chyba... Inaczej jest. A my się z prośbą o wycenę, tak to jest to... Dobra.

**[Damian Kaminski]:** Ja bym to po prostu zablokował. Dla nas my możemy tu, jak zbierzemy dane do kogoś, zadzwonimy, to od razu możemy to uzupełnić. Żeby dla dewelopera to szło na gotowo, chociaż możemy to też na etapie już propozycji też opisywać, no ale to jest zupełnie niekompletny opis, o co tu chodzi? W sensie wie to tylko Adrian, no to Adrian, no można to przypisać, ale to jest niekompletne.

**[Lukasz Bott]:** Wpis, wiesz, no ale widzisz, pytanie jest takie, czy chcemy wyręczać się, czy też chcemy się wzajemnie uczyć na zasadzie troszkę takiej, że... Tutaj koleżanka Neta to zgłosiła, jest początkująca, tak? To delikatnie trzeba tam może uświadomić, tak, no ale im więcej oni nam dadzą, tak. To jest wymaganie, tak, no napisali jak napisali, tak, czy mogli im więcej coś napisać czy podkowie tak. Opis wymagań, co mam z tym zrobić? Uprawnienia i widoczność. W zarządzaj uprawnienia. Opis wymagań. Dobrze, chyba to był... Prosty to jest przyjęte do wyceny, dobra, to trzeba, bo mogę tak zrobić. Wiesz, że dodałem regułę, która będzie to, to po leo dla nas odblokowała do... Czyli dla członków tej grupy tam, co tam jestem. I djembe w czynach, które tak do kogo tam trafia. Nie zrobić to od ręki, tak, może chcesz?

**[Damian Kaminski]:** Nie, dobra, tam to.

**[Lukasz Bott]:** Proszę mi się tymi muszę zrobić regułę automatyczną, która to... Które to odblokuje nam pole do edycji? Tak, no bo nie mogę tego zrobić. Myślę, że nie, nie zrobię tak, że to edycje, tylko my będziemy mogli mieć, bo... To jak mam zrobić, mam pisać tę regułę dla nas do edycji, czy idziemy zgodnie z procedurą, niech doprecyzowują?

**[Damian Kaminski]:** Reguły do edycji. Ja bym powiedział, że pole blokować do edycji, tyle tylko tyle.

**[Lukasz Bott]:** A tak po prostu tak, no to nie dobro tematu.

**[Damian Kaminski]:** Ale możemy też wpis... Możemy też im cofać pole do edycji, jak dasz, to wtedy można wszystko zrobić. Można nie uzupełniać, można zadać pytanie, ale jak trzeba, to możemy opisać po swojemu, bo jest opisany jakieś, powiedzmy.

**[Lukasz Bott]:** Dzień dobry, przygotowanie, czyli to były jest etap przygotowanie ceny przez dział DF czy przyjęte do wyceny? Jak to tam było? Dobra, przygotowywaniu.

**[Damian Kaminski]:** To czekaj, czekaj, bo ja tu w międzyczasie opisuję co innego. Już ci mówię, które to było tutaj, to jest etap.

**[Lukasz Bott]:** Na 2 zrobię, no przyjęte, dobra, no przyjęte do wyceny w modyfikacje, dobra, zrobiłam.

**[Damian Kaminski]:** Przyjęte do wyceny.

**[Lukasz Bott]:** Jakby świeży.

**[Damian Kaminski]:** Już, już zaraz należy jeszcze porobię to skrajny dla...

**[Lukasz Bott]:** Domu to mnie tutaj coś. Aśka się dopytaj. Coś znów z tymi słownikami zagnieżdżony mi kulturalne. Można się zgłaszać.

**[Damian Kaminski]:** Co w ogóle zresztą, co oni mają jakieś spotkania?

**[Lukasz Bott]:** Nie wiem, może na 12 świecie, bo normalnie był w piątki o dwunastej 30.

**[Damian Kaminski]:** Bo był design dwunasty 30, a to przez ten dobre. Nie wiem, dobra, tak by był naczelnikiem.

**[Lukasz Bott]:** Nie wiem, no ja miałem z Januszem 1x1 o jedenastej, ale to już minęło trochę czasu. Może coś pilnego jednak mieć wpływu. Ma to... Mili... Też mam podobnie widzieć. I to oni będą nie będą się dowiadywały się czy...

**[Damian Kaminski]:** Nie, nie pytałem, nie, nie robię tutaj jeszcze zgłoszenia.

**[Lukasz Bott]:** Też jakiś tam drobnicy robi coś tam, wersja kurne 100 trzydziestka jest felerna, no ja... Mamy co jakiś czas jakiś taki. Wizualnie jest ładna, bo zrobiło nową probowanie przycisków, ale kuźwa znowu jak bumerang wracają błędy, które już były rozwiązane.

**[Damian Kaminski]:** Do tych rozumiem, nie wywoływały się już piszczy, wywołałeś już. Właśnie. Allo.

**[Kamil Dubaniowski]:** Zaplanowaliście?

**[Lukasz Bott]:** Czy czegokolwiek? Czekaliśmy na was.

**[Kamil Dubaniowski]:** Zagadałem się z Januszem, z Markiem, ale to była, bo tam znaczy no pers pisywać sobie temat. Za chwilę też pieniądze łączyć.

**[Damian Kaminski]:** Odpisałeś.

**[Kamil Dubaniowski]:** I zielony dzień. Na razie nic nie zrobiłem zgodnie z planem. To piątek, więc tutaj.

**[Damian Kaminski]:** A w międzyczasie.

**[Kamil Dubaniowski]:** A jeszcze ten hotfix przetestuj sobie Damian, bo tak.

**[Damian Kaminski]:** Był. Już wiem, wiem, nie działa, ja już gadałem z Mateuszem, bo czekaliśmy na WIM to i hotfix i omówiliśmy ten temat. Ten temat tego proxy ma to sens. Te proxy to jest w kontekście banku, no ale nie było to po prostu zapisane.

**[Lukasz Bott]:** Tego procesu.

**[Kamil Dubaniowski]:** Nic, ten zapisany w tym zgłoszeniem próby takie domyśl się.

**[Lukasz Bott]:** Znaczy, nie wiem, może inaczej, no z tego co Damian po rozmowie tam z Mateuszem i Adrianem, tak, ewentualnie. Po prostu z mit relacjonował tak, że Adrian podobno był, jest świadomy tego, tak, co tam.

**[Kamil Dubaniowski]:** Tak, no to to chodzi, że oni chcą jakoś jakby otworzyć, ale nie ten serwer, na którym stoi AMODIT. Tak, ja to rozumiem. Tak, nie wiem dlaczego tak.

**[Damian Kaminski]:** Fillon, no wiesz, to jest bank, więc tutaj pewnie nie dojdziemy po prostu procedury i nie będą robić wyjątków dla jakiejś aplikacji jednej. Po prostu są serwery, zakładam, które mają wyjście na świat, a wszystkie serwery aplikacyjne i tak dalej mają nie mieć i po to, żeby po prostu jednego miejsca kontrolować, co wychodzi na świat i to monitorować. Podejrzewam, że to chodzi też o to.

**[Lukasz Bott]:** Winnica.

**[Damian Kaminski]:** I tyle. I my to dzisiaj mamy, czyli to to nie jest tak, że my mamy zrobić coś nowego, tylko mamy dołożyć moduły, które dzisiaj w sensie dzisiaj komunikują się bezpośrednio, czyli pomijają mechanizmy proxy, bo my mamy mechanizm proxy, tylko on nie jest skuteczny, dlatego konkretnego wywołania, czyli połączenia z naszym AMODIT serwisem tu idzie bezpośrednio.

**[Lukasz Bott]:** Teściom.

**[Damian Kaminski]:** I według mnie to inaczej, to nie powinniśmy dokładać, tylko my teraz musimy spisać, co dzisiaj idzie przez nasze proxy. Zrobić do tego listę w tym miejscu, gdzie jest definiujesz proxy, checkboxami i wybierasz i dołożyć im jeszcze właśnie te mechanizmy połączenia z naszym serwisem ma iść przez proxy albo ma nie iść. W zasadzie to bym zrobił jednym boksem, czyli po prostu połączenie z naszym serwisem ma iść przez proxy albo ma już bezpośrednio, plus wszystko to, co już jest, i wtedy będzie to na tyle uniwersalne, że jeden, bo wiesz. Zaraz tak połączenie z serwerem poczty czy ma iść czy ma nie iść, inne kolorystyki, czy mają iść czy mają nie iść, bo powiedzą, że jak na zewnątrz coś idzie, czyli do serwisy, to ma iść przez proxy, a jak wewnątrz kolorystyka jest powiedzmy bezpośrednio z ich innym systemem, to już nie musi iść przez proxy, bo to jest w ich infrastrukturze, więc według mnie to też. A może to powinno być nawet na poziomie już konkretnego wywołania kolorystyki, tak, czy ma iść przez proxy czy nie.

**[Lukasz Bott]:** Chyba tak. No to jest.

**[Damian Kaminski]:** To też do rozkminiania, bo to też ma sens, czy żeby to było definiowane na poziomie konkretnego wywołania, no bo możesz strzelać na zewnątrz i do wewnątrz.

**[Lukasz Bott]:** Znaczy w tej chwili jest... Jest jakby ja tutaj na wiki naszym tym wewnętrznym nie defa żur, rzuciłem hasło proxy, czy przypadkiem może jakaś dokumentacja do tego się nie pojawiła? To tylko dotyczy to kolorystyka. Faktycznie się w kontekście KSeF co się pojawiło. Jeszcze w kontekście na faktur, ale co by to było? A tok... Piszczy... Ustnych proxy. A. Mateusz już ten z właśnie per konkretna, wiesz co, dałem per konkretna konfiguracja, na przykład AMODIT i jak konfigurujesz tam nie w ustawieniach systemowych, to tam możesz włączyć opcję. A a ja już proxy nie i wtedy.

**[Damian Kaminski]:** No to właśnie pytanie, czy to powinno być na poziomie modułów czy raczej na poziomie proxy? Bo według mnie to jest bardziej...

**[Damian Kaminski]:** To tak jak z tymi indeksami, co mówimy, nie, że można na poziomie raportów pozaznaczać, że ta to ma być indeksowane, bo będziemy po tym filtrować, ale wtedy nie masz agregacji, co idzie taka, co idzie, tak musisz biegać po wielu miejscach. A ja bym to raczej zareagował. Właśnie definiujemy proxy i ustalamy, co przez to proxy idzie, a co nie idzie. No ale to już jest tylko zmiana miejsca wyświetlania, bo w zasadzie skoro mówi, że to jest to to to to już tylko trzeba to w innym miejscu wyświetlić.

**[Lukasz Bott]:** Tak, ale tylko... Tak, no w tej... No właśnie o to chodzi, żeby to uporządkować, tak, bo to właśnie w tym momencie robi się misz masz, tak, no bo z jednej strony masz niezależnie od tego, gdzieś tam mam to w ustawieniach systemowych, gdzie podajesz to proxy nie, a potem w jednej czy w drugiej funkcjonalności, głównie tych integracyjnych, albo masz możliwość wyłączenia, albo nie masz możliwości włączenia tego proxy. No bo w zależności od tego, który deweloper robił i czy to przewidział, tak, no albo czy wyszło gdzieś tam przy okazji, tak, no bo... No wewnątrz dziki do tego do... CR już proxy, bo w żywcu wyszło.

**[Kamil Dubaniowski]:** Dobra, jesteśmy w komplecie.

**[Damian Kaminski]:** Mogę powiedzieć, nie wiem, to ja nóż... Trzeba chyba częściej tak mówić. To jest priorytetem faktycznym, bo powiem wam, że tak to ruszyło tutaj repozytorium, że ja na bieżąco im teraz PA ja produkuję i za chwilę już dodaję, że zrobione.

**[Janusz Bossak]:** Wiecie co to znaczy?

**[Damian Kaminski]:** Aż jestem pod wrażeniem, co się wydarzyło przez ostatnie 2 godziny.

**[Janusz Bossak]:** Właśnie. Znaczy, ja bym chciał, żebyśmy teraz takich kilka kwestii organizacyjnych, tak, i jak widać to działa. Tak znaczy ten Daily. Jest takie miałkie, bo każdy coś tam sobie opowiada. Ja bym chciał, żebyśmy w pewnym sensie wrócili, bo przez jakiś tam krótki okres czasu tak było, żebyście wy mówili, że projektami? Czyli tak. Zatrzymamy Daily, Damian mówi. Przypominasz codziennie w tym Daily naszym celem jest dowiezienie repozytorium. I proszę Ania, Filip, kto tam, kto tam, co w ramach tego projektu zostało zrobione? Tyle. Kamil mówi. Naszym celem jest dowiezienie JRWA, rozumieniu tam obsługi pola typu Odnośnik, Marek, co zostało zrobione? Oni mają się tym zajmować. My musimy prowadzić te projekty. Tak. I potem po takim przejściu projektowym, czyli wszystko, co robimy dla dowiezienia celu sprintu, potem może być swobodna wypowiedź. Jania może powiedzieć, no jeszcze tam robiłam hotfixa i trzeba to zrobić, Marek może powiedzieć, no bo tam był też hotfix do TrustCenter, robiłem to i tamto, i tak dalej, nie Piotr może powiedzieć, bo nie powiedzmy, nie uczestniczy w żadnym z tych projektów, o których mówimy i proszę bardzo, to może być druga część, to jest wypowiedź swobodna, natomiast. Wydaje mi się, że właśnie ten początek powinien być taki i jak będziemy codziennie wbijać do głowy: naszym celem jest dowiezienie repozytorium. Co wczoraj udało się zrobić, co planujemy dzisiaj zrobić? I wtedy ludzie mówią, nie to coś takiego, co sądzicie? Bo jak widać taki dzisiaj to zadziałało, nie.

**[Damian Kaminski]:** Nie wiem, może przekroczyliśmy właśnie taki próg, że mamy już backend dobry w sensie bardzo bardzo danych i te mechanizmy pobierania i tak dalej i teraz już stricte endpointy poszły, czyli już wykorzystanie tego, co mamy i to jest szybsze, natomiast gdzieś tam pewnie testy też leżą, to wiem, ale na razie robimy uzysk funkcjonalności, będziemy to uzupełniać. Natomiast dużo się dzieje, jeszcze dzisiaj będzie na plot pliku i może nawet nie wiem odczytywanie już listy tej pliku, więc w zasadzie bez usuwania i bez uprawnień i bez historii już mamy komplet, czyli można będzie wgrywać. I zaraz w przyszłym tygodniu pewnie już podglądać, więc minimum, które jest potrzebne, żeby korzystać z repozytorium jest.

**[Janusz Bossak]:** I bardzo fajnie. Bardzo fajnie. No to chodzi. Dobra, to co? Co dalej jeszcze tutaj? Znaczy repozytorium, idziemy do przodu i może nawet zrobimy więcej, niż pierwotnie zakładaliśmy. Tam pozostaje kwestia i to bym chciał wtedy może jak jest chwila czasu i Filip jest dostępny, bo nie wiem. Filip tak opiekuje te frontendowe rzeczy repozytorium.

**[Damian Kaminski]:** Repozytorium, tak.

**[Janusz Bossak]:** Tak, czyli Filip od frontendu. To, żeby może wyrównać poziom taki wizualny, tak do tych elementów pozostałych, o czym mówiliśmy, tak, czyli tabelka, żeby to wyglądało, te kafelki, żeby wyglądały, jeżeli on ma przed tym.

**[Damian Kaminski]:** Tak. To mu zwrócę. Natomiast na razie już niech podpina ten endpoint, skoro one są, bo powiem tak, te wizualizacje kwestie to możemy zrobić w tym czasie, gdzie Ania będzie jeszcze robić jakieś testy, tak, Ania będzie produkować testy, a Filip może wtedy robić już tylko to, co się zmienia pod kątem takim właśnie tylko i wyłącznie frontendowym, a póki może to niech się łączy, żeby to było jak najszybciej do testowania, co gra, co nie gra. Ale tak tu trzeba omówić, co robimy. Chociażby wczoraj też zapytałem z kolorami, bo tutaj są powiedzmy kolory tego repozytorium. Ja widzę, że idziemy też w kolory w backendzie procesu, ale menu główne nie ma kolorów. Pytanie, czy będziemy dokładać, bo może to ma sens, żeby to jednak troszkę pokolorować, bo te ikonki są takie, no co szare. I tak poszliśmy w tym kierunku, ale czemu by ich nie zrobić jednak jakimś delikatnym kolorem i wtedy, żeby to było jakkolwiek spójne?

**[Kamil Dubaniowski]:** No to proces, ten obszar można jak najbardziej wybierać ikoną, który mimo jak da się wybrać ikonę, to tam można dołożyć pewnie wybór w kolorze tylko. Obszar. Ale czy ma mieć?

**[Damian Kaminski]:** Bardziej mi chodzi o to, że do wykonania powiadomienia i tak dalej.

**[Kamil Dubaniowski]:** K.

**[Damian Kaminski]:** Nie wiem, to wrzucam po prostu do zastanowienia się, czy... Z jednej strony robimy tu kolorki przy polach przy na backendzie, a tutaj nie, więc czy to tak będzie docelowo? Czy jednak będziemy to jakkolwiek kolorować? Będziesz jak patrzę na OneDrive, który powiedzmy w jakimś zakresie jest zbieżny, no to oni też nie kolorują.

**[Janusz Bossak]:** Czy ja właśnie nie wiem, czy to kolorowanie znaczy. No tak, w niektórych momentach to kolorowanie tam się nam tak powiem włącza.

**[Damian Kaminski]:** No bo wiecie, patrzcie tutaj coś wam pokażę, oni te systemowe tak jakby nie mają pokolorowany, ale już te...

**[Janusz Bossak]:** No.

**[Damian Kaminski]:** Mają. My mamy tak samo jak rozumiem z tego, co mówisz, Kamil, że obszar można ustawić tak.

**[Kamil Dubaniowski]:** Ikona koloru nie.

**[Damian Kaminski]:** Na ikonę, o k.

**[Janusz Bossak]:** Na razie no można by było zrobić, żeby była tak... Dobra, ale.

**[Damian Kaminski]:** Dobra, to później zmierzam bardziej do tego, żeby nie wydać czegoś kolorowego i załóżmy, że to podejdzie klientowi, a potem zrobimy szare i powie: nie, no było fajnie, bo fajnie rozróżniamy, a teraz nie jest fajnie i żeby to nie było zgodne z gdzieś tam naszym designem, to lepiej zrobić szare, może po kolorowe, no żeby to już było takie powiedzmy ostateczne, to tu trzeba będzie też tą decyzję podjąć.

**[Lukasz Bott]:** No to nie powinno być tak, że to powinno być kolory systemu wzięte.

**[Janusz Bossak]:** Według mnie powinny być szare. Zobacz w lewym menu tam, gdzie masz Kategoria, coś tam 7, niżej, niżej, niżej, niżej, niżej, o tutaj też nie, no i traktor rozwijasz, no i to są widzisz podfoldery.

**[Damian Kaminski]:** Tu na przykład 2, tak?

**[Lukasz Bott]:** Wszystko.

**[Janusz Bossak]:** Jest szara i ja bym to tak zostawił, tak samo tutaj zrobić. Repozytorium też ten, ten taki nie wiem, symbol bazy danych czy coś takiego.

**[Damian Kaminski]:** O k.

**[Janusz Bossak]:** Tam, gdzie masz te fioletowe też bym zrobił szare.

**[Damian Kaminski]:** No. Czyli bo, ale ikony zostawiamy, że jak coś jest otwarte, to robimy taką otwartą aktówkę tutaj, tak.

**[Janusz Bossak]:** Tak, żeby tak może być. No to już tak może być. Ja bym to zmienił na szare w środku, jak już jest otwarty, masz tą środkową część, gdzie prezentujemy pliki i foldery, no to tam te foldery mogą być kolorowe. No tak samo jak są na zakładce projekty czy raporty, nie są foldery oznaczane kolorami.

**[Damian Kaminski]:** Tylko zmieniamy na szare po prostu.

**[Kamil Dubaniowski]:** Też w tym lewym menu, no i poleruje się aktywny tylko folder, tak jest pomarańczowy na przykład repozytorium plików po lewej maksymalną. To to tak bym zostawił też.

**[Damian Kaminski]:** Teraz nie zrozumiałem.

**[Lukasz Bott]:** No pole po lewym w lewym menu, tak?

**[Damian Kaminski]:** No tu.

**[Kamil Dubaniowski]:** Ikona się koloruje aktywnego.

**[Damian Kaminski]:** No ale zawsze się koloruje, tak.

**[Kamil Dubaniowski]:** Tak, no i to to to mówię, tak, żebyśmy to utrzymali też. Zauważyć, że my tutaj z Przemkiem daliśmy na całą szerokość właśnie to zaznaczenie. Zobacz.

**[Damian Kaminski]:** A żeby to no jasne, jasne, o k, rozumiem.

**[Kamil Dubaniowski]:** Na elemencie i kwadratowy rogi są, nie są zaokrąglone, głównie ze względu na scroll, to tak zrobiliśmy i też te elementy drag and drop, żeby nam się zmieściło. To tak chcieliśmy, więc też bym już jak my musieliśmy na to już trzymajmy się tego, że to zaznaczenia jest kwadratowe czy z ostrymi kątami.

**[Damian Kaminski]:** O k. Dobra, dobra, postaram się to po wyłapywać, ale pewnie i tak jeszcze będę z wami konsultował, czego nie złapałem.

**[Kamil Dubaniowski]:** Podesłałem ci na czacie, jeżeli też rowerem na tym lupę do wyszukiwania jest mniejszy niż inne.

**[Damian Kaminski]:** Dobra, dzięki. No chyba tego nie zrobię na szybkiego, żeby to było szczere, żeby to porównać. Mogę zrobić? Dobrze, to zostaw. Robię to na projekcie. Dobra, to. To do czego wracamy?

**[Janusz Bossak]:** Nie wiem, tam macie tematy, wiecie, może mamy wszystko uzgodnione i tylko działać, no to nie ma co tym.

**[Kamil Dubaniowski]:** Trzeba pewnie rozpisać znowu, trzymałbym się tego, bo to dla nas nawet na ten jutrzejszy na poniedziałkowy przegląd jest fajny, żeby mieć te rozpisany na tym plenerze. Jako cele sprintu może powinno być inne narzędzie. Deweloperzy, co się dzieli? Na co dzień, no ten raczej nie zaglądają, ale moja zaglądam.

**[Damian Kaminski]:** Dobra, to to tworzymy analogicznie kolejny, tak.

**[Kamil Dubaniowski]:** Myślę, że tak nam to też rozjaśnić, żebyśmy wiedzieli, co jest w planie, ewentualnie coś wywalili, zobaczyli, że nie mamy składu na jakiś temat.

**[Lukasz Bott]:** Ja bym jeszcze ten, żebyśmy przejrzeli zgłoszenia. Bo coś, bo doszły nowe jakieś, więc nie wiem, czy dzisiaj to czy w poniedziałek tam przypiszemy, ale to jak już jesteśmy, to może przypiszemy.

**[Janusz Bossak]:** Że ja tutaj pracuję nad tym ciągle notatka. Robię drugą rundę, czyli lepiej teraz wygenerowałem te notatki, więcej mam tych dokumentów, się czekam na dokumenty od Przemka, żeby mi tam z tych spotkań projektowych przekazał te do x. I uczulam wszystkich was również na jeżeli uzgadniacie coś z kimkolwiek z Piotrem, Adrianem, jakiekolwiek spotkanie, wszystkie nagrywaliśmy wszystkie po prostu, tak, jeżeli są. I te spotkania mi przekazujcie. Bo wygląda na to, że ten sposób prowadzenie tego projektu będzie fajny i tej chwili jestem w drugiej fazie, znaczy pierwotnie już tam przerobiłem do jakoś października. Przeczytałem, to jest fajnie, ale mogłoby być lepiej i teraz robię drugą rundę. Gdzie te notatki jeszcze raz będą przetwarzane i już te notatki są też lepsze niż te, które miałem za pierwszym razem, bo są za powiem pełniejsze, tak znaczy tak bardziej nastawione właśnie na to, żeby później aktualizować projekty. I wygląda na to, że to jest naprawdę fajny sposób, że nawet to inaczej bym nawet nie aktualizując tych projektów, mając zestaw tam kilkudziesięciu tych notatek, mogę za pomocą kursora, w szczególności temu to kursora, no bo kursor sam z siebie indeksuje wszystkie pliki. Się zapytać, jaki jest stan projektu repozytorium i on przejrzy te wszystkie notatki i odpowiada, nie tylko, że musi przeglądać wszystkie tam 50 notatek z różnych spotkań za każdym razem, tak na ten dokument właśnie prowadzenia projektu ułatwia. No bo wtedy jadę pojedynczą notatkę i ono aktualizuje ten projekt i wtedy już od razu mam jeden dokument, który opisuje ten projekt, a nie że za każdym razem ja musi przeglądać tamtych 50 notatek, żeby znaleźć kontekst tego projektu. Nie, ale wygląda to fajnie, prawda? Jest to bardzo fajny sposób prowadzenia tego. Także ja to rozwijam dalej. Dzwonimy, robimy coś, czy każdy?

**[Kamil Dubaniowski]:** Tak, ja już tyle wstępnie.

**[Damian Kaminski]:** Tak, tak, ja się staram tu coś zrobić, a ty już zrobiłeś tak, a wpisałeś otruła, dobra, bo aha, to to ty zrobiłeś w międzyczasie, tu próbowałem wyklikać.

**[Kamil Dubaniowski]:** Tak, tak, tak. Jak kopiujesz zeszłego, co to wiem, że nie skończyłem.

**[Damian Kaminski]:** Dokładnie, dokładnie tak, tak, tak, tak, tak zacząłem tu też testować, czy to się daje kopiować, więc przechodźmy przez to, co jest kopiujemy i po prostu udoskonalamy, w sensie przepisujemy najwyżej, że to jest tak jak w moim przypadku repozytorium będzie jakieś musiałem wypić 2.


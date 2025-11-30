**Transkrypcja**

16 września 2025, 08:00AM

**Anna Skupinska** 0:13  
Cześć.

**Janusz Bossak** 0:14  
Cześć.  
Pytanie, czy mamy jakieś tematy narady?  
Przepraszam, nie ma was gdzieś tam spotkanie?

**Anna Skupinska** 0:26  
W sensie czy soros delic został już opracowany czy nie?

**Janusz Bossak** 0:31  
Nie wiem.

**Kamil Dubaniowski** 0:32  
Czy no na pewno bym miał jeden właśnie z przemkiem. Skończyłem rozmowę odnośnie edytora formularza i jednego ze zgłoszeń od Mateusza kołakowskiego. To jak nie ma tematów mogli.

**Anna Skupinska** 0:36  
Mhm.

**Kamil Dubaniowski** 0:44  
Byliśmy potencjalnie o tym pogadać. To chyba jeśli ona i tak pełnego składu Piotrek też warto, żeby posłuchał o tym.

**Anna Skupinska** 0:48  
Chcę.  
Tak, to soros the lead to ile pamiętam chcieliśmy zupełnie przerobić jak moto ma działać to edycja źródeł, więc to lepiej zrobić już w następnym wydaniu. Teraz tego nie robić.

**Janusz Bossak** 1:04  
Na moim tutaj.  
Pulpicie jest dużo zadań na radę wrzuconych.  
Wiem, że ten Łukasz to sobie sortuje według sprintów, a ja mam po prostu wszystkie oznaczone rada.  
A Łukasz pisze, zaraz dołączymy dobrze.

**Kamil Dubaniowski** 1:24  
Może ja, bo ja tego nie wrzucałem konkretne rady, bo to tak jak mówię wyszło teraz na na bieżąco już się loguje do przemka na środowisko lokalne, pokażę o co chodzi.

**Janusz Bossak** 1:34  
Brzmi.

**Kamil Dubaniowski** 1:36  
Chodzi o odtworzenie.  
Właśnie to jest pytanie, czy odtworzenie logiki z polami pustymi jak było, czy już podejście do tej nowej propozycji są gdzieś tą dawną dyskutujemy, czyli żeby przesunięcia?  
Działały w ramach wiersza, a nie całego formularza, jak teraz. Już mówię o co dokładnie dostępnej pulpit.  
Przypadek jaki mamy teraz? Mateusz kołakowski zgłosił to chyba w piątek, że nie może teraz kliknąć na to tutaj. To jest tak naprawdę po stronie backendu pole puste.  
Żeby sterować uprawnieniami tego pola no w tym.

**Janusz Bossak** 2:20  
Znaczy puste w sensie o typie pusty.

**Kamil Dubaniowski** 2:22  
Typ pola, typ pola puste tak no i oni mają te pola na formularzu w wielu klientów. No bo właśnie tak jak chcą, żeby im w to miejsce nie wskoczyło, pole numer awarii, no to dodawali pole puste. Wiele jest też takich warunkowych.  
Użyć tego pola pustego także muszę tu dać pole puste, bo jak ukrywam to pole to to mi wskakuje tutaj. Tak więc muszę mieć jeszcze jedno zapasowe pole puste, które będzie widoczne tylko na etapie, gdzie ukrywam pole, osoba rejestrująca mną pełno takich zależności. No wiemy, że tak tak robimy i tak robiliśmy.  
I teraz.

**Janusz Bossak** 3:00  
Ponieważ.

**Damian Kaminski** 3:01  
Znaczy, ja bym jeszcze tutaj inaczej do tego podszedł, bo o tym rozmawialiśmy, rzucę trochę inne światła zdecydujmy, co jest najlepszym wykorzystaniem, bo jeszcze był pomysł grupy.  
Grupy pól, czyli zakładamy, że wyświetli się jedno, to znaczy grupa pól bym określił jako.

**Janusz Bossak** 3:15  
No więc.

**Damian Kaminski** 3:21  
Alternatywa z dodatkiem pustego na przykład tak czy, ale ten pusty to zawsze można można uznać po prostu jako Ukryj oba, czyli wyświetlamy albo jedno albo drugie, albo ukrywamy obydwa. Tak, no to wtedy to działa tak jakieś zwykłe pole, więc może ta zadatkiem pustego to już zbędnie dodałem natomiast.  
Osadzamy konkretnie pole w danym miejscu i można wyświetlić tylko jedno.

**Janusz Bossak** 3:48  
Słuchajcie, no sprowadźmy się na ziemię, że tak powiem oczywiście pomysłów na rozwój i inne sposoby ogarniania pól pustych jest kilka. Tak też mówiliśmy o tym już dawno, żeby te pole puste, żeby to Piotra była propozycja, żeby można było je używać jako tak zwany aliasy, tak znaczy, żeby takie mini pole z taki tekst tak znaczy, że w tym jednym polu mógłbym wstawiać jakąś wartość.  
Więc.  
Ponieważ mamy.  
Taki moment, jaki mamy znaczy, chcemy to wydać, żeby to działało, ponieważ mamy.  
Taką logikę jaką mamy, czyli mamy te pola puste.  
W moim przekonaniu na ten moment.  
W tym mśp powinniśmy dorobić na liście pól po lewej stronie pole pusty.  
Tutaj wyświetlać to pole puste, czy tam, gdzie jest w tej chwili upuść pole tutaj powinno być napisane, że to jest pole typu pole puste było widać, że on tu jest i musi działać tak jak inne pola, tak znaczy można je usunąć, można je przesunąć.  
Coś można z tym zrobić tak, no bo takim takie mamy formularze. No teraz wiecie jak ja nie chcę w 100 kilkudziesięciu wdrożeniach.  
Popsuć tego nie.

**Damian Kaminski** 5:12  
No tak, tylko pytanie, czy powinniśmy iść w tą stronę, czy pozostawić tak jak jest z wiedzą, że.

**Kamil Dubaniowski** 5:12  
Czy?

**Janusz Bossak** 5:13  
Int.

**Kamil Dubaniowski** 5:18  
Czy możemy w ogóle tak, bo bo ja wam jeszcze powiem co przed chwilką Przemek mi po pierwsze backend aktualnie nam w ogóle nie zwraca tych pustych, więc tutaj endpoint do potrawki potencjalnie.  
Druga rzecz jest taka, że w momencie, kiedy ktoś sobie o k. Wiem, że muszę tutaj mieć tyle, bo tyle pól planuje już sobie na dodawałem w momencie kiedy zmienimy to, żeby backend nam zwracał faktycznie istniejące już pola puste, no bo to jest tylko teraz na froncie to te pola jeszcze jak ja rozumiem, nie istnieją jak w momencie teraz ktoś doda sobie tutaj to pole, ale już zaplanował sobie te niżej tak, bo wie, że będzie miał mnóstwo pól do dodania, to w tym momencie te wszystkie musiał usunąć, bo ich nie ma nawet pojęcia.  
Ee więc jak zaczniemy teraz bazować na tym, co faktycznie zwraca bekę? No to efekt będzie taki, że po dodaniu pola te wszystkie moje zaplanowane zostaną usunięte. Ja bym się zastanowił, że jeśli w ogóle mamy teraz taką rozterkę, no to trudno w ten sposób pracujecie z tym nadal postaramy tutaj sobie edytuj się te pola puste to jest.

**Janusz Bossak** 6:17  
Będą tam właśnie kombinować z tym przechodzeniem.  
Znaczy ta wersja, która którą mieliśmy robiona jeszcze przez przemka madeja.  
Yy, ona jakby te pola puste dopiero dodawała.  
Jakby później tak w momencie, kiedy tu jest troszeczkę inaczej, tak tutaj to właśnie nie ma żadnego guzika. Zapisz ani wyjdź stąd i tak dalej, tylko wszystko się dzieje na bieżąco. To jest delikatna różnica, bo w tamtym trzeba było wyjść, żeby on jakby zapisał i wtedy dopiero się działo. To co powiedziałeś kamienie, że te wszystkie puste miejsca były wypełniane polami pustymi.  
Jeżeli była taka potrzeba, więc tam była cała taka.  
Logika jakaś za tym stała tak miarę sensowna.  
Znaczy, wydaje mi się, że najszybciej byłoby po prostu pokazywać te pola puste, gdzie one fizycznie są?  
Bo one fizycznie obecnie gdzieś są.  
Tak jak pokazałeś. Jeżeli dodam tutaj jakieś pole, znaczy linie, tak.  
No to to to to jeszcze nie są pola puste, bo fizycznie ich tutaj nie ma, powiedzmy w tym obok osoby tak obok tej osoby rejestrującej. Załóżmy, że byłoby pole puste i to byłoby tu widać. Czyli nie można by było zrobić upuść pole tutaj, bo tam jest pole puste, o typie puste, a tutaj upuść pole tutaj to jest tylko placeholder.

**Damian Kaminski** 7:36  
Place holtery są mhm.

**Janusz Bossak** 7:53  
I ono nie generuje jeszcze.  
Pola pustego.

**Damian Kaminski** 8:01  
Ale bo ja się zastanawiam nad pomysłem dodania typu pola pustego po lewej stronie.  
Ee, czy to jest dobry kierunek? Bo tutaj poniekąd zgadzam się z Kamilem, czy nie zostawić tego taki zastanowić się nad tym dobrze, zamiast później wycofywać jakieś rzeczy, które wprowadzimy.  
Mm.  
Czy nie wiem nawet jak tak jak teraz prezentujecie, ktoś dołożył sobie wiersze, ale dopiero osadza się to pole puste, może ono nie jest dostępne na liście, tylko nie wiem w ramach tego place holdera jest jakiś.  
Jakiś znaczek, który powoduje osadzenie tego pola, czyli jego wytworzenie, a niekoniecznie że mamy ten typ pola na liście po lewej stronie tylko w ramach tego kafelka jest dostępny.  
Mm.  
No nie wiem, tak rzucam pomysłem, nie mówię, że Jestem do tego 100% przekonany, ale zastanawiam się, czy pole puste powinno być polem wybieranym z tej lewej listy.

**Janusz Bossak** 9:05  
Znaczy.  
Dzień no.  
Nie możemy teraz wymyśleć jakieś skompy?  
I nowe i logiki.  
Mając to co mamy tak tutaj można co najwyżej na razie jest backendu dodać to, czego brakuje, żeby wracało, znaczy zwracało informację, że to są te pola puste.

**Damian Kaminski** 9:19  
Dokładnie.

**Janusz Bossak** 9:28  
I skoro można było wybrać pole puste.  
To powinno się dać wybrać według mnie pole puste, tak.  
Mm i to jest najprostsze według mnie najbardziej intuicyjny najbardziej dla konsultantów podobny do tego, co mamy teraz tak, czyli jawnie umieszczone na formularzu pola puste i to byłaby wersja, to nasza tutaj MVP, któraś tam?  
I tyle tak potem możemy się zastanawiać, jak od tego odejść w ogóle tak i to co mówił tutaj Kamil. Na początku tego zaczął.  
Pomysły już były dawno, żeby by traktować nasz formularz jako wiersze.  
Formularza.  
I żeby rzeczywiście nie było tak, że jak coś tam usuwam, to mi się wciąga to co jest.  
O tutaj, tak jak jest dwukolorowa?

**Kamil Dubaniowski** 10:27  
To tak to to chodzi o ten moment tak, czyli w momencie, kiedy mam.  
Spyta to jeszcze tu dorzucę, tu niech będzie jakaś lista.

**Janusz Bossak** 10:35  
Weź jakieś proste, weź jakiś takich bardziej prosty przykład.

**Kamil Dubaniowski** 10:39  
Znaczy to tak i teraz na jakimś etapie tą datę muszę ukryć.  
A to jest powiedzmy nie wiem.  
Miejsce, data od data do a tutaj już jest jakaś tam? Nie wiem. Lista wyboru, która zupełnie nie pasuje mi do tego wiersza. Te wiersz ten wiersz ma jak najbardziej tematycznie ze sobą powiązanie. Dlatego tak użyłem w ogóle formularz i teraz tak ja na jakimś etapie ukryje tą datę jeden tu to Mistrz skutkuje tu, no a to przeskakuje mi wiersz wyżej, no i oni teraz, żeby to zabezpieczyć, to tutaj dodają jakieś pole puste, które w ogóle teraz tak robi. Tak no taki będzie efekt, że to jest jakieś pole puste, która jest potrzebne tylko po to, żeby na jakimś etapie ono zajęło miejsce.  
Yy tego pola kwota jeden, bo kwota jeden pójdzie tu więc fizycznie tak mają. Teraz tak wygląda ich formularz, bo na jakimś jednym etapie muszą sobie zagwarantować, że pole puste wskoczy w to miejsce, a nie to pole wskoczy w to miejsce.

**Damian Kaminski** 11:30  
No dobra, jak mamy teraz na liście pole puste to po prostu my tego nie jesteśmy w stanie tu wyświetlić, tak?  
Czy w sensie czy?

**Kamil Dubaniowski** 11:39  
Znaczy no po pierwsze, żeby to, no bo to jest puste, tak to jest puste z jakiegoś powodu, że ktoś jeszcze tu czegoś nie wrzucił, więc my nie wiemy czy on potrzebuje, czy po prostu sobie zaraz coś dorzuci.

**Janusz Bossak** 11:39  
Znaczy.

**Damian Kaminski** 11:48  
No nie, ale chodzi mi o to, że jeśli na liście byś dodał wolę pusty, to one się tu jawnie nie wyświetla na tym ekranie.

**Janusz Bossak** 11:57  
Czyli chodzi mnie ja się nie, ale słuchajcie, nie nie poczekajcie, poczekajcie poczekajcie to jest Dodaj ten wiersz Jeszcze raz.  
Jak zrobiłaś i Dodaj w to drugie pole coś tam.  
Dobra, czyli mamy data, jeden kwota jeden niby puste i kwota 2 i teraz wejść na listę tam.

**Damian Kaminski** 12:18  
No właśnie.

**Kamil Dubaniowski** 12:20  
O kwocie jeden będzie pusta.

**Damian Kaminski** 12:26  
Mhm i ono zniknie jak tam?

**Kamil Dubaniowski** 12:29  
Coś dorzucę.

**Janusz Bossak** 12:31  
A czy wolno się tutaj fizycznie dodaje?

**Kamil Dubaniowski** 12:33  
Tak.

**Damian Kaminski** 12:37  
Ja bym.

**Kamil Dubaniowski** 12:37  
Nie zaplanował wykład.

**Damian Kaminski** 12:39  
Ja bym nie upychał.  
Na siłę w to evip.

**Janusz Bossak** 12:46  
Nie no to jest.

**Damian Kaminski** 12:46  
Obsługi.

**Janusz Bossak** 12:48  
To czekajcie, to jest dobrze. No jeżeli taki jest jak pokazujesz.  
I teraz w to pole przed kwotą 2, że już tam nie wiem, listę wyboru albo cokolwiek tam, jakkolwiek datę tam nieważne.  
I teraz przejść na tą listę.

**Kamil Dubaniowski** 13:07  
No to pozostaje jeden znikniesz z kwota jeden dokument jeden.

**Janusz Bossak** 13:10  
Co jest git no.

**Damian Kaminski** 13:12  
Czy go się coś psuje? Kolumny tak się psują jeszcze.

**Janusz Bossak** 13:12  
To nic nie pamięta.

**Kamil Dubaniowski** 13:14  
Kolumne się tak nie zapamiętuje kolumb układu.

**Janusz Bossak** 13:18  
To trzeba poprawić tak, ale to wtedy mi się wydaje, że to nie ma problemu z tym.

**Kamil Dubaniowski** 13:18  
Zgłoszę.

**Damian Kaminski** 13:25  
Znaczy, patrzymy na to przez pryzmat. Ja też uważam, że powinniśmy zrobić jak najmniej w tej, bo mówimy jeszcze cały czas o czerwcowej, tak?

**Janusz Bossak** 13:33  
No tak, także nic dużo nie znaczy. Według mnie ta logika oprócz tutaj tego, że znika 3 kolumny, pojawiają się 2.  
Yy, w trybie pan przejścia między listą edytorem, to ta logika jest dobrze zrobiona.  
Znaczy, że tam się pojawiają puste, kiedy tutaj udajemy, że są puste.  
Ale o tyle jest to nawet bardziej wygodne, że ja nie mam tego jakby z materiału.  
Że tu jest puste i mogę tu włożyć co mi się podoba i to puste samo znika nie więc to jest bardzo dobra logika. Według mnie w tej chwili zrobiona bardzo dobrze.

**Kamil Dubaniowski** 14:11  
No tak, tylko teraz jakby ktoś chciał właśnie to co powiedziałem, że na to puste ma żyć tylko na etapie, na przykład nowe, bo na etapie nowe będę ukrywał to data jeden i ja to pole puste. W ogóle tutaj robię, żeby to pole puste. Właśnie wskoczyło mi wiersz wyżej.  
No to nie mam jak teraz kliknąć, żeby ukryć to pole na pozostałych etapach, żeby ono było tylko na etat nowe dostępne.

**Damian Kaminski** 14:34  
Z reguł tylko tak albo z listy.

**Kamil Dubaniowski** 14:36  
Znaczy z listy.

**Janusz Bossak** 14:37  
Bo ono się nie się nie nazywa puste, jeden znaczy. No ja rozumiem, że chodzi na na tym widoku nie wierzy, że ono się nazywa puste jeden.

**Kamil Dubaniowski** 14:37  
Tutaj.  
Tak, że raz, że nie wiem, że on się tak nazywa.

**Damian Kaminski** 14:44  
Nie ma kontekstu jego jego funkcji, tak tak jak na liście.

**Kamil Dubaniowski** 14:48  
No wiem jak się odnieść właśnie do niego skodzie reguł potencjalnie no a 2, że nie mogę tak jak na pole kwota 2 kliknąć i zarządzać uprawnieniami i ukryć to pole puste, no bo na żadnym etapie nie jest mi potrzebne tylko na etapie nowe nie mogę tego zrobić, no bo jakby tu jest tylko place Holder autostrad, nie wiem, że to jest właśnie zgłoszenie Mateusza nie brakuje.  
Ustawień uprawnień do tych pól pustych to tych powodów orderów.  
No i tak jak wspomniałem tak tłumnie nie zwracane jest na Weekend. My nie wiemy, że to jest pole puste, jeden znaczy nie jest zresztą z backendu możemy to dodać tylko, że wtedy to będzie już puste jeden, no i co to puste jeden po stronie znaczy puste pole tak po stronie frontendu miałby mieć taką właściwość, że mimo tego, że widzę, że tu jest puste jeden to i tak mogę na niej coś wypuścić, ale jak nic nie jest opuszczone to mogę wejść i potencjalnie edytować.  
Pragnienie.

**Janusz Bossak** 15:52  
Za skomplikowane.

**Damian Kaminski** 15:52  
Znaczy ja w ramach evip zastanawiałbym się tylko nad serwisem.  
Tego co jest, żeby jak ktoś wejdzie w ten tryb nie popsuł układu.  
A nad tym tematem popracowałbym w kontekście design nowych spotkań jak to obsłużyć? Bo to jest skomplikowane.

**Janusz Bossak** 16:10  
Miałem zostawił tak jak jest?  
W tej chwili, ponieważ to jest.  
Trudny przypadek.  
Że ktoś?

**Damian Kaminski** 16:18  
To nie jest temat na 3 dni, że my już wiemy, jaki ktoś to zaraz zrobi.

**Kamil Dubaniowski** 16:20  
Tak tak, ja nawet tego nie planuję. Ja nawet tego nie planuję do wydania czerwcowego, to od razu mówię, że jakby listę mają i niech tam się bawią po staremu.

**Janusz Bossak** 16:20  
Tak.

**Damian Kaminski** 16:27  
Dokładnie.

**Janusz Bossak** 16:29  
Także jest list tygodni. Na razie to jest zaawansowane wymaganie i tutaj, a my będziemy dążyli do tego, żeby uporządkować sposób zachowania się pól na formularzu, ale to naprawdę trzeba zrobić ostrożnie, żeby wiecie, nie popsuć setek.

**Kamil Dubaniowski** 16:29  
A.  
Znaczy, moim zdaniem nie wyjdziemy z tego, to będzie musiało być na takiej zasadzie, że mamy 2 logiki zakładu tego formularza jest stara, która działa po prostu i ewentualnie jakiś przełącznik, że ktoś świadomie przełącza na nową logikę i sobie podporządkuje, to pozmienia w kodzie po usuwa niepotrzebne pola puste, które zrobił, bo tak działa stara logika, a po prostu nowe procesy tworzą się już domyślnie z nową logiką.  
I tak jak mówię, no ta stara logika powoduje takie rzeczy, że później nie masz realnie tak jak wygląda ten formularz, bo formularz realnie wygląda powinien wyglądać tak.

**Janusz Bossak** 17:20  
To to do tej nowej logiki musi dojść nowe pojęcie na przykład wiersz.  
Albo grupa to co mówił do mnie tak, czyli że masz to 3 pola w wierszu je traktujesz jako grupę pól nie i ona do niej nie może nic doskoczyć niższego wiersza, tak i wtedy mamy.

**Damian Kaminski** 17:42  
Dokładnie.

**Kamil Dubaniowski** 17:43  
Albo wręcz właśnie tak, że na poziomie wiersza ja sobie mogę go założyć jakąś kłódkę, tak, że nie przyjmuj tutaj pól pozostałych wierszy niżej, tak jak ja wtedy ukryję sobie to data jeden, no to ten wiersz jest za zamknięty. Zablokowany nie nic nie przyjmie, no i wtedy to łączymy 2 logiki. Tak naprawdę.

**Janusz Bossak** 18:01  
Dokładnie wie, że to jest tak jak mówisz, to jest na parę spotkań na przedyskutowanie wielu różnych jakby wariantów.

**Damian Kaminski** 18:08  
Jakieś nie który będziemy mogli przetestować?

**Kamil Dubaniowski** 18:12  
A napiszę na razie do szymka, że zostawiamy mateuszowi też dam znać.

**Janusz Bossak** 18:17  
Jedynie nie Przemek poprawi ten pamiętanie 3.

**Kamil Dubaniowski** 18:19  
Tak tak, widzę, że to.  
W ogóle nie zapamiętuje.  
Już do niego też.

**Piotr Buczkowski** 18:27  
Gdzie zgłaszać ewentualne błędy, żeby takie niedogodności, tak jak na przykład to?  
Z tym podmianą literki są w zeszłym tygodniu zauważyłem.

**Kamil Dubaniowski** 18:39  
Ja ja im wysłałam wszystko po prostu albo do mnie albo bezpośrednio już ma na blok to już jak projekcie.

**Damian Kaminski** 18:39  
Do Kamila.  
Znaczy, wiecie, to znaczy nawet jeśli na backlog ja widzę, że musimy zastosować pewien rodzaj.

**Piotr Buczkowski** 18:45  
Znaczy te.

**Damian Kaminski** 18:53  
Pewną rolę eksperta, bo ciężko jest się w tym wszystkim połapać. Ja nie będę miał pojęcia, co już było, co nie musi być opieką do danego projektu i on wie, czy to jest powtórzenie, bo tak jak z tymi raportami, tak gdzie trafia, to do mnie i 3 te same tematy w ciągu 2 tygodni, a to oznacza też, jaki jest priorytet tego zgłoszenia wpadają niezależnie i nie da rady, żeby 3 osoby równolegle ogarniały, że to jest ten samo zgłoszenie, to nawet jak wrzucamy na backlog, powinno być najpierw przypisane do Kamila.  
Jako opiekuna zgłoszenia opiekuna całego tematu, który wie, jakie są wytyczne, wie, czy to wchodzi, wiem, p czy czy to jest świadomy jeszcze błąd, tak jak tutaj, powiedzmy mamy i i który to właściwie przypisze.  
Więc to znaczy, podsumowując, na backlog jak najbardziej może być, natomiast powinien być wskazywany Kamil jako osoba walida jąca to.

**Janusz Bossak** 19:53  
Czy no?  
Czy wydaje mi się, że powinniśmy? Ja widzę, że wielu osobom bi też zresztą nie jest jakoś wygodnie robić zgłoszenia na na wykroku nie.

**Damian Kaminski** 20:24  
Mhm.

**Janusz Bossak** 20:25  
W ten sposób działać tak, czyli jeżeli to jest edytor procesów, no bo to jest edytor procesów.  
Element edytora procesów to po prostu tam zgłaszajmy, nie?

**Damian Kaminski** 20:35  
To też jest dobre rozwiązanie, bo jak tych tematów jest kilka, to nie nie każdy zapamięta tak kto jest czyim opiekunem, a to też z drugiej strony rozszerza, że poza Kamilem jest dedykowany tester. Poza mną, powiedzmy w komunikatorze jest jeszcze Basia i ta walidacja jest podwójna, tak i ona może pomagać robić zgłoszenia i walidowane. Czy już takiego czegoś nie było, albo jest w trakcie obsługi.  
Więc no to jest jakiś pomysł?

**Janusz Bossak** 21:05  
Tutaj wtedy.  
Tak jest teraz moduł raportow by tak raportow stabilizacji. No ja wiem, że tu będzie dużo różnych rzeczy, no ale przynajmniej będzie widać że.  
Coś ktoś zgłosił i ktoś tam będzie to sobie przeglądał.  
Kto jest opiekunem i będzie z tego robił zgłoszenia? Może ten ktoś będzie to przeglądał? Zauważy, że a to już jest to samo, co było tam nie. No bo to już nie robię drugi raz, bo ten ktoś wie dokładnie.  
Jakie są zgłoszenia i powinienem o to, jakby dbać tak natomiast?

**Kamil Dubaniowski** 21:35  
Czy ja mam o tyle obawę, że jak będzie dzień dzieja siedzę cały dzień w sprzedaży, to później robię sobie takich zaległości, że się z tego nie wygrzebię, a zgłoszenia będą tylko nie wrzucone i deweloperzy nie będą mieli co robić.

**Damian Kaminski** 21:48  
Ale to ja bym to znaczy pytanie tylko czy takie, czy to nie jest przestrzeń przede wszystkim, gdzie zgłaszać w kontekście, gdzie zapytać, czy tego już nie ma, czy to zgłaszać, bo wiesz jak na czymś też pracujemy, to w zasadzie wersja sprzed tygodnia to jest już zupełnie inna wersja niż obecna.

**Janusz Bossak** 21:50  
To rozwiązanie.

**Damian Kaminski** 22:08  
I ja też dostaję dużo pytań, no słuchaj tutaj w raportach coś nie działa, bo te raporty już są produkcyjne. No ale jak widzimy są błędy i one się powielają, wracają te same i tak dalej i też nie wszyscy niektórzy po prostu nie wprost pytają czy to trzeba zgłaszać.  
I może trzeba zrobić do tego przestrzeń?

**Janusz Bossak** 22:29  
No to do tego co mówisz Kamil, według mnie do tych kanałów zresztą do projektów bym chciał, żeby te projekty w końcu ruszyły. To co ja zacząłem tam robić na tym wiki, bo uważam, że to jest bardzo pomocne.  
Yy, powinny być 2 osoby, czyli znaczy właściwie 3, tak i to nam rozwiązuje temat.  
Jeden z was tak, czyli Damian Kamil, Łukasz jako.  
Libery menedżer, jeden deweloper, odpowiednio, Piotr ania, Adrian, Marek i tak dalej i jeden test. Jedna z testerek po prostu tak albo Basia, oktawia albo Patrycja i wtedy te 3 osoby są odpowiedzialne za to, żeby taki kanał też jakby przeglądać. No bo są bezpośrednio odpowiedzialne za dany projekt i oczywiście będą uczestniczyły w kilku projektach, więc odpowiednio trzeba tam będzie analizować kilka.  
Yy.

**Damian Kaminski** 23:26  
Ale to jednocześnie według mnie nie przerzuca odpowiedzialności zakładania bagów na na zorzę na nas tylko bardziej daje przestrzeń, czy to się nadaje na bak, czy to na przykład już jest gdzieś zgłoszony nad tym pracujemy, albo jest rozwiązane w ogóle w nowszej wersji, bo dalej według mnie ja bym na takim kanale chciał móc odpowiedzieć. To jest błąd, którego wcześniej nie było, Zgłoś go i tyle.

**Janusz Bossak** 23:51  
Do tego.

**Damian Kaminski** 23:51  
Żeby żeby nie było tak jak Kamil mówi, że kogoś nie ma i potem tutaj 20 zgłoszeń już trzeba obsłużyć i spada to na jedną osobę.

**Janusz Bossak** 24:01  
Dlatego dlatego.  
Po jednym z.  
Moich tam pomysłów było dodanie tego live i work item generator. To jest rzecz, którą wymyślił Microsoft.  
Nie jest jakiś dodatek logiczny firmy.  
Który zaczął współpracować z tym ogólnie blogiem i tam jest kilka jego jakby zastosowań do naszej od kontekstu tak potrafi generować, potrafi tam wyszukiwać tak dalej możliwe, bo nie to ciągle jest nieskonfigurowany nie wiem o co tam chodzi, z tym coś nie działa, trzeba się temu przyjrzeć, możliwe, że to by nam pozwoliło właśnie na.  
Pani odpowiedzi, czy takie coś już jest?  
Tak, czyli zaczynasz wpisywać jakiś jakiegoś baga, a on ci pokaże, że tego typu zgłoszenia już są tak i wtedy można się łatwiej zorientować, że ktoś próbuje zgłosić podobną rzecz, która już była na przykład nie.  
No ale to do sprawdzenia.  
World generator. No dobra, słuchajcie, jedźmy dalej, bo.  
Usprawnianie.

**Piotr Buczkowski** 25:13  
To jakie jest, jakie jest?

**Janusz Bossak** 25:16  
Makaron.

**Piotr Buczkowski** 25:16  
Konkluzja.

**Janusz Bossak** 25:18  
Wrzucaj na kanał odpowiedni do projektu, czyli jeżeli masz do edytora procesu.

**Piotr Buczkowski** 25:19  
Bo tam będzie wrzuć siłę, to dotyczące tej nazwy tak edycji nazwy pola, na przykład to było dobrze.

**Janusz Bossak** 25:28  
Tak, tak, tak, tak, tak, tak.

**Piotr Buczkowski** 25:30  
No bo teraz mamy zdrowie. Zgłoszenie dotyczące sekcji i uprawnień do sekcji mam 2 uwagi.  
No takie drobiazgi, tak, że jest to coś coś jest, no nie zaznacza, nie wiadomo do czego się edytuje czy coś.

**Janusz Bossak** 25:38  
Dobrze.  
Dobrze, to to tak róbmy na razie zobaczymy jak to nam będzie jakby szło. No tu mamy kanał pen testy, no to tam do pen testów mamy kanał ten level sidebar to myślę, że już można może usunąć, no ale niech będzie moduł raportów owy nowy x prawy bardzo dobrze.  
Forma też dobrze.  
Więc tutaj mamy parę takich kanałów. Już jak będzie brakować to dorobimy tak, żeby to miało sens.  
Dobra, co my tam mamy dalej?

**Damian Kaminski** 26:25  
Już patrzę czy nie wiem, czy Łukasz ty wyświetlasz.

**Lukasz Bott** 26:27  
Jest tak, jeżeli się tam?

**Damian Kaminski** 26:35  
Coś tu nowego wskoczyło od Marka.

**Lukasz Bott** 26:38  
To znaczy przypisane jest do Marka, wskoczyło od Daniela i to ja, no przekierowałem.  
Chodzi o Marka, prosiłem o evaluating na. Na ile to się da zrobić.  
Bo chodziło o to, żeby skrócić, sprowadzając do tutaj najszybciej całą dyskusję i to ten wątek. Chodziło o to, że żeby skrócić prezentowane nazwy plików tak do właśnie pierwszych kilka literek na początku kilka na koniec i pośrodku jakiś tam właśnie kropki, gwiazdki czy coś w tym stylu.  
Bo czasami się w tytule w nazwie pliku pojawia się na przykład. Nie wiem. Umowa z Łukasz bot tak, no i to to już tam.  
Tea temat wyszedł yy chyba został zgłoszony do naszego radka szczerskiego tak do jodu do i od tak i i.  
I to gdzieś tam było zamieszanie u klienta.  
Na szczęście nie nie skończyło się to jakimś tam incydentem, ale żeby się potencjalnie zabezpieczyć przed tym, to chyba właśnie Radek zasugerował, żeby właśnie tego typu mechanizm zastosować.  
Bo nie ma co za bardzo tutaj dyskutować, tylko to zróbmy no i tyle.  
Ewentualnie Marka może w to wciągnąłem się tak i dopytać.

**Damian Kaminski** 28:06  
Ale co tu jest ryzykiem, że nazwa pliku po prostu przenosi jakieś poufne dane? Tak.

**Lukasz Bott** 28:11  
Tak tak, tak, że masz to znaczy przenosi dane, które można potraktować jako poufne.  
Kwestia chodziło o to, że.

**Damian Kaminski** 28:20  
No i ja to za. No tak o k. Zadbajmy o to systemowe, ja takie tematy powiedzmy waderko planując zadbałem, że tam jest po prostu imię i pierwsza literka nazwiska tak i to nie jest wtedy.

**Lukasz Bott** 28:33  
Tak no no wiesz, ale nie wymusisz na wszystkich, że że że będą o to dbali w szczególności jak ktoś tam nie wiem załączy plik z zewnętrznego źródła tak mówię, bo ja rozumiem, że ty mówisz o sytuacji takiej, że tam dokument jakoś tak.

**Damian Kaminski** 28:37  
No tak, tak, tak tak.

**Janusz Bossak** 28:46  
Wiesz?

**Damian Kaminski** 28:49  
My przygotowujemy dokument.

**Lukasz Bott** 28:51  
A ty przygotowujesz po stronie morita generujesz to nazwę pliku to wtedy masz kontrolę nad tym, ale jeżeli jest to dowolny dokument, który może być załączony z dowolnego źródła.

**Janusz Bossak** 29:02  
Ale tam w naszym procesie, znaczy.  
Czasami mnie to zadziwię.  
No ale tu mówisz o przesyłanych sms em, tak nie mailem smsem. No dobra, no to no to smsem jakoś może mniej pan.

**Damian Kaminski** 29:15  
Ale to też właśnie smsem, ale co tam przychodzi, poszukam te nasze trasy Center.  
Roz. Senter.  
Dobra no jest pełna nazwa dokumentu o k jest amadi teraz Center myśli cod SMS.  
Dalej jest kod kropka nazwa dokumentu i w cudzysłowie jest pełna nazwa dokumentu, czyli ta nazwa dokumentu miała być ścięta do 8 znaków. Tak?

**Janusz Bossak** 29:44  
Słuchajcie, mamy.  
Procesie.  
Wysyłania tych dokumentów.  
Takie pole, gdzie podaje się cudzysłowie, przyjazną nazwę pliku.

**Damian Kaminski** 29:57  
Mhm.

**Janusz Bossak** 29:57  
A przyjazna nazwa pliku jest używa.  
Ona do e maila.  
Tak.  
I niech będzie używana do smsa koniec kropka wszystko.  
I wtedy jakby nie my odpowiadamy za to tak tutaj masz szanowny użytkowniku.  
Wpisz sobie co ci się tam żywnie podoba. Nie pisz tutaj imion i nazwisk.  
Bo to idzie i może gdzieś wyciec, więc wpisuj tylko to co jest bezpieczne i tyle.

**Lukasz Bott** 30:31  
Ale to ja już mówisz. Ja już mówisz o formularzu pomodlcie tak i funkcjach za modlitwa wysyłających, ale jeżeli ktoś korzysta z tras Center z pominięciem mamuta.

**Janusz Bossak** 30:41  
Ale ta trase przecież wysyła ten komunikat.

**Damian Kaminski** 30:43  
Nie, nie januszowi chodzi o to, że endpoint teraz Center ma takie pole jak przyjazna nazwa dokumentu, która powinna być używana w mailach i analogicznie w smsach, czyli nie wysyłamy jawnie nazwy pliku, tylko przyjazną nazwę dokumentu, która jest definiowana.  
Ee.  
No to znaczy, to nie jest rozwiązanie systemowe w kontekście myślenia za użytkownika, ale to jest rozwiązanie, z którego można korzystać. No i teraz pytanie, czy my chcemy myśleć za użytkownika? Jednak jeszcze to nadpisać, czy tak jak Janusz proponuję to konfigurator jest odpowiedzialny za to jakie dane wychodzą do użytkownika.

**Janusz Bossak** 31:25  
Według mnie tak.  
Znaczy wschodzie, no nie jesteśmy w stanie myśleć za wszystkich.  
Może ktoś?

**Damian Kaminski** 31:36  
No bo to znaczy ja tu widzę ewentualnie, ale takie uwagi zwrotne, a wcześniej ładnie. My mieliśmy przygotowane takie adecco, że jest umowa. Anna KA, teraz jest umowa i jest jakieś i jest an kropka k jest wycięte jak my tam żadnych danych poufnych nie wysyłamy.

**Lukasz Bott** 31:48  
Umów.

**Damian Kaminski** 31:58  
Ee.

**Janusz Bossak** 31:59  
No więc o to mi chodzi, że lepiej jest według mnie.  
Dać użytkownikom więcej, czyli mogą nazwać sobie w sposób przyjazny ten dokument tak jak chcą.  
Nie mając tam nazw we znaczy imion i nazwisk.  
I niech z tego korzystają. No faktem jest, że powiedzą, no ale tutaj nam się nie wiem, podpowiada taka nazwa. Tak wiem wtedy w każdej umowie w każdym dokumencie będą musieli usuwać sami tak sobie.  
Imię nazwisko skracać do takiego, które jest właściwe.

**Damian Kaminski** 32:37  
Że no przyjazna po to też i wszystko zabezpieczamy przyjazna nazwa nie powinna przenosić danych poufnych. No to osoba konfigurując poza integrację powinna mieć tego świadomość, że to powinna być informacja taka, że jeśli wypłynie nie do tej osoby co trzeba, to nie przeniesie żadnych danych. Ale no.

**Janusz Bossak** 32:57  
Należy to.

**Damian Kaminski** 32:57  
Rozumiem oba punkty widzenia.

**Janusz Bossak** 32:59  
Tej przyjaznej nazwie w tym polu można by kosztował już teraz fantazjuje nie, ale są funkcje i wcale nie.  
Nie związane z jajem, ale tam przynajmniej po stronie języka python jest dużo takich bibliotek, które wykrywają dane osobowe. Nie czy imię nazwiska wykrywają i można by tak robić, że jeżeli tam my jako amo dit, podpowiadamy użytkownikowi w tym polu, bo tam przepisujemy tak naprawdę tą nazwę.  
Yy pliku dosłownie na początku i ktoś może sobie tam wpisać co mu się tam żywnie podoba, nie to moglibyśmy mu sugerować, że nazwie jest nazwisko nie albo imię i rozważ.  
Usunięcie.

**Damian Kaminski** 33:49  
Znaczy, ale teraz mówisz o o tym naszym, powiedzmy procesie demo? Nie.

**Janusz Bossak** 33:53  
I tak tak tak, tak, tak.

**Damian Kaminski** 33:55  
Mhm, bo bo ktoś może też to wyklikać w ramach innego procesu.

**Janusz Bossak** 33:59  
No znaczy więc.  
No tak, dobra, słuchaj.

**Lukasz Bott** 34:01  
Dobra.  
Ale to słuchajcie, tylko rozumiem. Janusz konkluzja jest taka, że nie zajmujemy się tym tematem, czyli nie robimy tego, no ale w takim razie trzeba dać odpowiednie wytyczne. Nie wiem na wiki to opisać, że tak jest to zalecenia.

**Damian Kaminski** 34:16  
Nie, niekoniecznie, nie zajmujemy się inaczej, zmieniamy, zmieniamy jedną rzecz, zmieniamy po stronie tras Center. To, co jest przekazywane w s msie, nie przekazujemy nazwy bezwzględnej pliku, tylko przekazujemy nazwę przyjazną, tak jak jest to przekazywane w mailu.

**Janusz Bossak** 34:36  
Dokładnie o to mi chodziło, tak?

**Damian Kaminski** 34:39  
Czekaj, zaraz ci pokażę.

**Lukasz Bott** 34:44  
O k dobra, bo akurat Jestem na bieżąco z tym, bo czy czy kliś się tam robi? Rozumiem, że po prostu jak jest funkcja teraz Center tak sen dokumentalny czy taka właśnie kolwiek nazywa to tam jest opcja tej przyjaznej nazwie tak podanie, tak to o to ci chodzi.

**Damian Kaminski** 35:02  
Tak i ona jest użyta w mailu jako umowa do podpisania.

**Lukasz Bott** 35:03  
Tylko i i w mailu jest używana, a nie jest używana w momencie wysyłania sms em dobra, no to o k. Dobra to taka konkluzja jest.

**Damian Kaminski** 35:08  
Dokładnie.  
Nie według mnie jest.  
Według mnie jest patrzę teraz na smsy, według mnie to tak działa.

**Lukasz Bott** 35:19  
Jest już.  
Przyznał w końcu, że jest używania tarczy jest.

**Damian Kaminski** 35:24  
O ile jest zdefiniowano tak tak tak według mnie to tak działa. Dopytaj Marka, ale według mnie jak jak widzę smsy to to tak działa. Jeśli jest zdefiniowana nazwa przyjazna to patrzę we s msy i tam gdzie zakładam, nie miałem mamą na przykład kropka PFA jak miałem znalazłem maila umowa do podpisania to w s msie mam umowa do podpisania bez rozszerzenia, więc raczej to tak jest.

**Lukasz Bott** 35:29  
No i dobra, no to.  
Dobra.  
Czyli innymi słowy, ja dopytuję Marka? Dopytuję. Marka, żeby potwierdził, że w smsie jest używana ta przyjazna nazwa, o ile jest podana tak, a ogólnie nie wiem na piątkowym spotkaniu z konsultantami tak możemy zwrócić uwagę, żeby żeby tą tą tą funkcjonariuszy nas przyjaznych we właściwy sposób używania, tak w ogóle używali, a 2 używali właśnie tak, żeby unikać właśnie na przykład podawania podawania jakiś tam.  
Danych, które potencjalnie mogą być uznane za poufne. Tak.  
I tyle tak, no ewentualnie to jako wytyczne też może krótki artykuł na wiki, czyli jako takiej tam nie wiem.  
Uwagi do funkcji tej tej tej Center centrum Saint tak zrobić to można w dokumentacji dopisać tej funkcji.  
Jako tako adnotacji tak, że zalecenie czy też.  
Tak zalecenie, że nie nie powinno się właśnie.  
Tak robić tak, żeby tam?  
Umieszczać.  
Dobra.  
To to z nowości to ja to ogarnę po tym.  
Nieprawidłowe działanie identyfikacji z sprawie nożnej. Sprawa pożywna i z hiden tru.  
Czy tu mamy czas na przedyskutowanie nam się już za kilka minut kończy spotkanie.

**Damian Kaminski** 37:42  
No nie wiem, super, nie Piotr musiałby się wypowiedzieć jakie tam są zależności.  
To jest Huberta z tego co pamiętam zgłoszenie.  
No jest problem z usunięciem dead casa, jeśli są sprawy powiązane i to zależy z życiem i to zależy właśnie od rodzaju powiązania. Już tu nie pamiętam, ale tak abstrahując od tego.

**Lukasz Bott** 37:57  
Nie użyciem.

**Piotr Buczkowski** 38:04  
Trzeba trzeba stworzyć tą sytuację.

**Damian Kaminski** 38:08  
No właśnie.

**Piotr Buczkowski** 38:11  
Zapłacą za bardzo skaczecie, żebym przeczytał.

**Lukasz Bott** 38:14  
Dobra.  
Zostawię.

**Piotr Buczkowski** 38:17  
Podrzędna.  
No.  
Obsłużyć tą sytuację to jak?

**Damian Kaminski** 38:24  
Na nadrzędne nie da się usunąć nadrzędnej sprawy nigdy.

**Piotr Buczkowski** 38:27  
No tak, bo bo ona podrzędnej jest idi w klasie jest connected cars tak.

**Damian Kaminski** 38:32  
Mhm.

**Lukasz Bott** 38:32  
Tak.

**Piotr Buczkowski** 38:33  
I przez to nie pozwala referencje usunąć. No nikt nie pomyślał z takiej sytuacji, trzeba trzeba ją obsłużyć.

**Lukasz Bott** 38:43  
Pytanie, czy to nie jest właściwa sytuacja, może powinien być jakiś komunikat, że no Nie możesz użyć tej funkcji, bo bo masz podpięte.  
A niedobra, bo podrzędną oznaczenie jako usunięto dobra no.

**Piotr Buczkowski** 38:53  
No trzeba było kejs jeden jest oznacza.  
Usunięto tak także, ale też niemożliwe do edycji. Pewnie przez to tak.  
Ponieważ tamta sprawa jest nie inaczej, sprawy usunięte nie jest to pobierane do kolekcji.  
I kejs kodeksem cases, tak.  
A Forest pewnie pokonał cases do do od czepiania od połączonych.  
Rozumiecie tak i przez to nie jest odczepiane od kasy hidden od tej, która jest ukryta i później przy samym delikt. Baza danych zwraca błąd, że sorry Nie możesz, bo tutaj jest referencja.

**Lukasz Bott** 39:34  
Bo został referencje. Dobra, rozumiem?

**Piotr Buczkowski** 39:37  
To nie to, że jest kontakt, ma wracać i broń boże, tylko trzeba po prostu sprawdzić, czyli to oddzielnie, czy przypadkiem jakiejś jakiejś iden nie ma tak wśród kobiet?

**Lukasz Bott** 39:53  
No dobra, no to pytanie, czy to czy to coś to jest w ogóle do dyskusji na daszki taktów, czy po prostu wiadomo co zrobić i.  
I nie wiem, wrzucamy to, może już nie na ten spęd tylko nie wiem na kolejny.

**Piotr Buczkowski** 40:03  
Znaczy ja wiem co zrobić. Trzeba to obsłużyć tak, a co zrobić czy co dokładnie zrobić to ja wiem.  
Mogę opisać tak jest.

**Damian Kaminski** 40:10  
To przypisz to do Piotra na kolejny sprint najwyżej Piotrek to zdejmie z siebie jako piszę i komuś się to rozpiszę.

**Lukasz Bott** 40:18  
Dokładnie.  
Umiem to zrobić, tak?  
Dyskutować no dobra.

**Piotr Buczkowski** 40:35  
Ja tam chodzę siała wpisywałem, ale to chyba bez, bo to jest na split tak.

**Damian Kaminski** 40:40  
Tak.

**Piotr Buczkowski** 40:41  
A to a da się bez sprintu na.

**Damian Kaminski** 40:44  
Nie chcesz tego zobaczyć?

**Lukasz Bott** 40:47  
Jeżeli coś masz, to albo oznacz, albo po prostu powiedz.

**Piotr Buczkowski** 40:50  
Jako blok jako backlog wpisałem już nie pamiętam dokładnie miałam jakieś strony, pytanie już moment.

**Lukasz Bott** 40:59  
Znaczy słuchajcie, no bo czas czasowo to formalnie śmy skończyli tak więc.

**Damian Kaminski** 41:03  
Znaczy, według mnie powinniśmy mieć blocker na godzinę, bo to już nie pierwszy raz i nie zdążamy przejść przez te tematy. I o k. Możemy je przesuwać, ale żebyśmy przynajmniej widzieli, że to spada, a nie także po prostu. Nie. Nie dochodzimy do pewnych elementów.

**Lukasz Bott** 41:07  
Tak, tak.

**Piotr Buczkowski** 41:23  
No dobrze.

**Lukasz Bott** 41:25  
No pytanie czy?

**Damian Kaminski** 41:25  
Znaczy, Piotr, jeśli coś tam chcesz zreferować, to to mów według mnie już zróbmy to do jedenastej i tyle.

**Lukasz Bott** 41:28  
Tak.

**Piotr Buczkowski** 41:29  
Konie, wiem, że wpisałem, ale nie pamiętam co wpisałem so.

**Damian Kaminski** 41:32  
Nie może znaleźć tak.

**Piotr Buczkowski** 41:34  
Tak.  
Jak?

**Damian Kaminski** 41:36  
Dobrze a aniu czy ty jesteś w stanie nam zreferować ten temat?  
O aktualizacji systemu, bo tu mówiłaś, że to uzupełniła, zaś to może byśmy to jeszcze omówili.  
Nie.

**Anna Skupinska** 42:01  
Jest choć mnie o k. Miałbym gadam do wyłączonego mikrofonu, więc jest baza danych wam, od której są zawarte dane organizacji. To nie jest ta sama baza danych, gdzie są sprawy i tak dalej i w niej jest tabela, w której można umieszczać wiadomości.  
I te wiadomości jakby się pokazują, jeżeli nie ma dostępu do bazy danych, czy jeżeli jest nie można się modlić połączyć z bazą danych, to wtedy sięga do tej drugiej bazy danych, w której są informacje o filly.  
W organizacjach i umieszcza wiadomość i stamtąd jeszcze to się pojawia w przypadkach jeszcze logowaniu i przy stop menniczej tym pasku narzędziowym tylko nie Jestem pewna ile z tych funkcje zostało zachowane, kiedy zaczęliśmy przechodzić na ratować te rzeczy.

**Damian Kaminski** 42:48  
Mhm, dobrze, ale to poczekaj, czyli tak.  
Przy logowaniu i przy i w top menu to mówimy o tym, że to był.

**Anna Skupinska** 42:56  
Tak znaczy, to to będzie ten taki pasek, gdzie są te tak ten pasek na Górze, gdzie są, który się zawsze pojawia, gdzie są o tutaj z użytkownikiem Łukasz bochni z logiem to się powinny pojawiać.

**Damian Kaminski** 42:59  
Na Górze.  
Mhm.

**Lukasz Bott** 43:07  
Czy jeszcze nad tym tak?

**Damian Kaminski** 43:08  
Nad tym tak.

**Anna Skupinska** 43:09  
Tak więc tak samo miało być?

**Damian Kaminski** 43:12  
Więc ta baza danych, tylko żeby to ta baza danych.  
Jest weryfikowana za każdym razem, ale dodatkowo nawet jak nie odpowiada baza modi, to ona też jest weryfikowana? Tak.

**Anna Skupinska** 43:24  
Ja próbuje się połączyć właśnie z tą bazą, gdzie są zapisane informacje organizacji.

**Lukasz Bott** 43:30  
Ale to dotyczy rozwiązania chmurowego.

**Damian Kaminski** 43:33  
Tak.

**Lukasz Bott** 43:33  
No bo w instalacji on prem nie masz bazy danych tej org. Tak no.

**Anna Skupinska** 43:39  
No w sumie.

**Damian Kaminski** 43:41  
Znaczy, słuchajcie, jedno nie wyklucza drugiego, bo skoro jest taki mechanizm, to można było się zastanowić nad możliwością wypełniania tej zewnętrznej bazy z poziomu pola wa. Modlicie, żeby tym mógł sterować administrator z drugiej strony, wypełniając to globalnie na przykład taki Łukasz poskrobko mógłby z poziomu jednej bazy przekazać informację do wszystkich amonitów, że fillon.

**Anna Skupinska** 43:53  
Mhm.

**Damian Kaminski** 44:05  
Będzie dzisiaj a update.  
Pytanie tylko, czy ten pierwszy przypadek użycia powoduje jakieś ryzyka czy niebezpieczeństwa, że ktoś tam coś może podmienić i tak dalej.

**Anna Skupinska** 44:17  
A czy to się manipuluje? W zaczął nią z bazy danych nie było żadnego od tego meni zrobionego. Jeżeli ktoś ma dostęp do buta można tym manipulować to i tak ma dostęp do bazy danych, więc.  
Jest afera.

**Lukasz Bott** 44:30  
Ale to czekajcie, czekajcie, bo ja teraz sobie troszkę o innej rzeczy pomyślałem, skoro mamy ten mechanizm powiadomień.

**Damian Kaminski** 44:30  
Nie no.

**Lukasz Bott** 44:37  
W końcu to może.  
To w jakiś sposób wykorzystać i tutaj dać możliwość. Dodaj powiadomienie systemowe i wtedy ono mając ten znacznik, że jest systemowe, to się pojawia na tej belce filler poziomie i tak na na na Górze.  
Tyle i w tej.

**Anna Skupinska** 44:56  
Dlaczego okazać, że nie było ich za dużo, ale tak można było też użyć tego systemu, że się pojawiają tam na Górze. Tylko oczywiście tabelka została przerobiona, więc nie jest, jeżeli nie dodali tego, no to nie ma.

**Lukasz Bott** 45:07  
Nie nie, no to.

**Damian Kaminski** 45:07  
Wiesz, za dużo nie musi być, bo możemy zrobić ograniczenie jedno i koniec jak chcesz inne to odepnij to albo uzupełni to o drugą informację. Nie ma tam choinki możliwej do do do podpięcia.

**Lukasz Bott** 45:14  
Tak, tak tam.  
Tak w danym momencie może być tylko jedno systemowe, tak i tyle.  
Więc albo je przeredagować, albo usuniesz i wprowadzić nowe, nie.

**Damian Kaminski** 45:30  
To znaczy, dobra, to jest element, powiedzmy już front endowy i tego, jak ty można wysterować. Załóżmy, że na razie zróbmy wyświetlanie tak, czyli tak jak rozumiem.  
Mamy bazę danych, która jest dostępna z poziomu chmury i pozostaje tylko, żeby dorobić frontend, który pobierze z tej bazy informacje i wyświetli i to jest rozwiązanie dla klientów chmurowych.  
Ee, później możemy pracować nad sposobami wypełniania tych informacji, natomiast to nie jest rozwiązanie dla klientów on premii sowych. A jakbyś zjechał do dołu? Potrzeba wynika z ze zgłoszenia tutaj on premise owego ha Mateusz, tak czy nie?

**Lukasz Bott** 46:15  
Tak no Mateusz chodziło o pewnie gdzie Rossmann RP, no czyli duzi klienci, on prawicowi, tak, no to za chwilę też pewnie byś to nawet mógł opchnąć orlenowi tak i też by się pewnie ucieszył, gdyby we teczce mógł wyświetlić komunikat nie.

**Damian Kaminski** 46:17  
Rossmann, LPP.  
Mhm.

**Lukasz Bott** 46:30  
Jeżeli więc, yy, więc myślę, że to.

**Damian Kaminski** 46:37  
Znaczy to co ania tutaj?

**Lukasz Bott** 46:38  
Może może powinno być to dwutorowo zrobiony? Tak no chmura to chmura tak i tam sobie zarządza Łukasz tym.  
Yy za pomocą tej bazy organizacji dodatkowej bazy a won premium no to nie wiem, no taki komunikat, jeżeli nie chcemy robić interfejsu na chwilę obecną a na szybko no to może prosty interfejs na zasadzie, że gdzieś w ustawieniach systemowych dorzucić taki atrybut tak jakie mamy tam sekcje dotyczące Józef. Interfejs wyglądu nie wyglądu, no to tam dorzucić pole tak komunikat systemowy, tak, albo mamy takie.  
Nie wiem czy się zachowały w tych nowych ustawieniach, ale mamy te pola do do tego do zarządzania komunikatem przy na stronie logowania. Tak.  
Być futer być jakiś czy coś w tym stylu tak na stronę logowania można wyświetlić komunikat.

**Janusz Bossak** 47:25  
W ogóle ciekawa.

**Damian Kaminski** 47:27  
Słuchajcie, ja bym też to wyżej poziomo podniósł Janusz, co w ogóle o tym sądzisz? Czy my to jest funkcjonalność, która nie jest narodu mapie wynika z potrzeb klienta? Czy my nie powinniśmy tego po prostu wycenić i pójść do LPI do rossmana i powiedzieć, zrobiłem wam to po 2000 od głowy jeszcze Orlen można zapytać i wtedy dopiero do tego siądziemy.

**Janusz Bossak** 47:47  
Równie tanie.  
Absolutnie tak finansowanie jest zawsze miłe, tak wiecie, no im może musimy się tego nauczyć, że po prostu różne tego typu rzeczy jakoś tam zdobywać finansowanie niekoniecznie jest 20000.

**Damian Kaminski** 48:02  
Ja powiedziałem 2.

**Janusz Bossak** 48:02  
Ale.  
Ja wiem, wiem, no ale tak tak.

**Lukasz Bott** 48:06  
Ale no od 10 klientów Damian.

**Damian Kaminski** 48:08  
No to tak można jak najbardziej.

**Janusz Bossak** 48:11  
Po 4 od 10 i wyjdzie wam.  
Coś tam na waciki będzie nie.  
Nie jak najbardziej, natomiast mnie ciągle zastanawia jedno, że my to mieliśmy zrobione. No ja nie wiem na czym my dyskutujemy.

**Damian Kaminski** 48:25  
Znaczy i to mamy Janusz, tylko to co ania powiedziała, nie wiem, czy tam byłeś skupiony, czyli tak mamy to tylko dla rozwiązań chmurowych i nie jest to i i zakładam, że backend, to znaczy wiemy gdzie odpytać mamy przestrzeń do przechowywania tych informacji, natomiast z racji, że zmieniliśmy ramę, to nie jest to obsłużone w nowej ramie.  
I tylko dla chmurowych, a pytają nas o to, on premise sowi i tego nie mamy.

**Anna Skupinska** 48:49  
A czy trzeba by zapytać osoby, która to robi, robimy nowe ramy czy uwzględniły to?  
Czy dodałeś, że te wiadomości się wyświetlają?

**Janusz Bossak** 48:57  
Nie, nie, nie.

**Damian Kaminski** 48:58  
No to to można zapytać, ale.

**Janusz Bossak** 49:00  
Się ten pomysł, który?

**Piotr Buczkowski** 49:01  
Ja właśnie to co ja mówiłem to też jest właśnie też jedna rzecz, którą pewnie w nowej ramie tej reaktory nie została uwzględniona.  
Chodzi o wylogowanie automatycznie.

**Lukasz Bott** 49:13  
No dobry.

**Damian Kaminski** 49:18  
Że tam się też pojawia taki pasek, tak?

**Piotr Buczkowski** 49:21  
Po pierwsze sprawdzanie taki ile zostało do wylogowania, a po drugie jeżeli mam dla was 2 zakładki w jednej się wylogowuje to starym starej wersji tej drugiej zakładce też po chwili cię wylogowało, o której zostaje i każda kolejna akcja tylko w vi premii.  
Błąd tak.

**Lukasz Bott** 49:40  
No to swoje pietrek, dobrze, że zwróciłeś na to uwagę, bo to trzeba.

**Damian Kaminski** 49:42  
Zaraz to sprawdzę na swoim domu.

**Kamil Dubaniowski** 49:45  
Znaczy odliczanie na pewno robiliśmy.

**Piotr Buczkowski** 49:46  
Zgłoszenie tak, zgłoszenie 2 1 9 7 4.

**Damian Kaminski** 49:55  
Piszesz Łukasz.  
2 1 9 7 4.

**Piotr Buczkowski** 49:58  
2 1 dzień.

**Lukasz Bott** 50:01  
2 1.

**Piotr Buczkowski** 50:02  
9 7 4 dziewiątka, przedostatnio ze mną na siódemkę.  
Takie jest efekt.  
2 zakładki w jednej się wylogowuje drugiej powinno się też wylogować.  
Tam jest stary.

**Damian Kaminski** 50:25  
Czyli ajm wylogował, a rama została tak?

**Piotr Buczkowski** 50:28  
No bo bo frame działa ten to i sołtyka i to ta w reakcje nie.

**Lukasz Bott** 50:40  
Wys.

**Piotr Buczkowski** 50:40  
Cały czas mu spamuje tym.

**Damian Kaminski** 50:42  
Dobra no przywieźcie to według mnie nie wiem, Kamil to zaopiekujesz.

**Kamil Dubaniowski** 50:46  
No do przemka, te emocje jakby nawet przeze mnie żeby wychodziło, ale.  
Wydaje mi się, że to jest coś, co było.

**Piotr Buczkowski** 50:54  
Oj to już właśnie tam jest ten licznik, ale tego szczerze mówiąc nie sprawdziłem właśnie czy to działa czy nie.

**Kamil Dubaniowski** 51:03  
Licznik na pewno uwzględniłem Przemek robił a testy też tego były to było nawet zgłoszenie osobne no ten licznik.  
A jak się coś wysypało to po drodze.

**Damian Kaminski** 51:13  
Ale poczekajcie, bo tak kolejny sprint ja nie wiem jak jest Przemek obłożony na ile to jest krytyczne pod kątem wydania tego na.

**Kamil Dubaniowski** 51:22  
Czy efekt jest taki, że no wylogowany zostałeś tylko widzisz ramę jak klikniesz cokolwiek, no to cię wywali.

**Damian Kaminski** 51:22  
Na chmurę.  
Wywali gdzie do logowania.

**Kamil Dubaniowski** 51:34  
Tak to działało chyba do tej pory.

**Piotr Buczkowski** 51:37  
Znaczy jak się zalogujesz ten i premie to będziesz 2 razy mierzycie ramy.

**Kamil Dubaniowski** 51:37  
Pamiętam, ale.  
Ok.

**Damian Kaminski** 51:47  
No nie nazwałbym tego wersję stabilną, jeśli takie coś się dzieje, a auto wylogowanie jest czymś, czym ludzie mają do czynienia codziennie.

**Lukasz Bott** 51:58  
Słuchajcie z tym auto wylogowanie to od razu to podpada pod bezpiekę, bo w pn testach nam wytknęli któryś, że nie mamy tego dobrze obsłużone.

**Damian Kaminski** 52:03  
Tak, tak.

**Janusz Bossak** 52:11  
No to jako hotfix to.  
Traktować i zrobić natychmiast rękę.

**Lukasz Bott** 52:20  
Tak na ten sprint jeszcze i oznaczenie jako hotfix.

**Janusz Bossak** 52:25  
No tak, ale chcemy to wydawać.  
Nie możemy wydawać rzeczy, które mają potencjalne dziury, bezpieczeństwo.

**Lukasz Bott** 52:57  
Tak do przemka, to czy ktoś inny się tym?

**Janusz Bossak** 53:02  
Pojętny.

**Lukasz Bott** 53:19  
No dobra.  
A co?  
Wracając do tego tematu, co to co z tym robimy?

**Damian Kaminski** 53:32  
Znaczy, tak jak wspomniałem, mamy to obsłużone tylko dla chmur i to musi i to powinniśmy też wykorzystać dla siebie, ale dla klientów trzeba to wycenić i tyle, więc trzeba to podzielić na 2.

**Janusz Bossak** 53:46  
Aby ocenić, ale też ja bym wrócił do tego pomysłu, który tutaj Łukasz chyba ty podałeś, żeby.  
Tak w tych powiadomieniach naszych.  
Jakiś sposób wyróżniać takie powiadomienia systemowe?  
Albo w jakimś innym mechanizmie to co dla fejmu tam kombinujemy jakieś annosy czy cokolwiek innego.  
Żeby to właśnie się wtedy pojawiało jako takie komunikat systemowy, tak właśnie wyróżniony.  
To jest, bo chodzi też o łatwość dodawania tego znaczy łatwość. No tak, żeby administrator chciał łeb konfiga zmieniać gdzieś tam coś wpisywać, tak i tak dalej.

**Lukasz Bott** 54:21  
No tak tak, no to.

**Janusz Bossak** 54:29  
Tylko żeby to było tak wiecie, no wchodzę i mi się taki komunikat wyświetla, tak to nie musi być nawet ten pasek od góry to może być po prostu denerwujący okno po każdym zalogowaniu tak wchodzę i.

**Lukasz Bott** 54:42  
No to po wchodzisz pierwszy raz ten pop ci się wyświetla tak i.

**Janusz Bossak** 54:46  
Tak.

**Lukasz Bott** 54:48  
No tak, no ja ostatnimi czasy mam konto w mBanku tak no to jak mają jakoś tam ofertę handlową, żeby wziąć się założyć lokatę albo kredyt, jakieś coś to loguje się i mi od razu wyskakuje popup, który oczywiście zamykam tak no on.

**Janusz Bossak** 55:07  
No ale też prawdą jest, że w mBanku też mam konto jest tak, że jeżeli są tam jakieś informacje o wyłudzenie tak dalej, to u góry jest taki czerwony pasek.

**Lukasz Bott** 55:07  
Nie.  
Krytyczny tak to są.  
Tak dokładnie tak jak on jeszcze jest ginie czasami zanim się zalogujesz nie.

**Janusz Bossak** 55:19  
I.  
Tak no.  
Więc taki pasek jest jak najbardziej pożądany.  
Znaczy, zróbmy tak wycenimy to jakoś tam uzyskamy na to pieniądze, a wymyślimy jak to powinno być zrobione do końca.  
Bo widać, że jest kilka jakby propozycji tak, ale też nie chciałbym tego robić jakiegoś.  
Wielkiej funkcjonalności, a raczej coś w miarę szybko do tego, żeby to działało.

**Lukasz Bott** 56:00  
Dobry mijania to z ciebie zdejmuje do siebie przypiszę i.  
A dzięki za to dzięki moze i ty.  
Się tam do kolegów odezwy, czyli do Mateusza i nich.  
Finansowanie na to w sądzie?  
Dobra spłacie jedenasta się zbliża, który już nic nie przedyskutujemy takiego.

**Janusz Bossak** 56:21  
Dobra, ja muszę uciekać na spotkaniem menedżerskie.

**Damian Kaminski** 56:25  
Jeszcze jest tylko tak nadmienie jeden temat tam wrzucony klient się zdecydował po 2 miesiącach od oferty na analizę bazy danych.  
To tak na razie wrzucam, bo powiedzieć tam się.  
Zadeklarowałem, że damy jakąś odpowiedź, może dzisiaj natomiast, no po prostu klient chce wykupić 2 dni, żeby przeanalizować, dlaczego wolno działa, czyli jakieś tam reguły się wykonują po półtorej minuty i właśnie baza danych jest mocno obciążona, więc tutaj nie wiem, kto mógłby się tym zająć. Znaczy wiem, kto wiedział, jak się tym zająć, ale ale pytanie, czy tutaj właśnie Piotra wrzucamy od razu, czy jeszcze mam jakiś krok pośredni?

**Janusz Bossak** 57:14  
Zwróćmy Piotra.

**Lukasz Bott** 57:18  
Ale ja bym wiesz co, ale ja bym miał pomysł taki, żeby benton walnie może któryś z czy z koleżanek i kolegów od nas zespołu zrobił to razem z Piotrem?

**Damian Kaminski** 57:18  
No dobra to.

**Lukasz Bott** 57:29  
Żeby ewentualnie nabrał też takiej wiedzy i był powiedzmy.  
No.  
Zastępcy tak potencjalnym.

**Damian Kaminski** 57:39  
Nie no tak, żeby patrzeć jak to analizować. No Jestem za pytanie tylko kto?

**Anna Skupinska** 57:46  
Miałam jej zadań to może?

**Lukasz Bott** 57:52  
Nie no to musi być osoba, która tam potencjalnie tak. No ja pomyślałem o moim imienniku tak czyli łukaszu grodzkim.

**Anna Skupinska** 57:55  
Mhm.

**Piotr Buczkowski** 57:58  
No czy tylko pytanie to ma być analiza czy poprawianie też tak tego?

**Damian Kaminski** 58:03  
Ana.  
Iza na razie jest 2 dni tamen material na analizę i potem wnioski i wycena, poprawę ewentualnie.  
Na razie to jest analiza.

**Lukasz Bott** 58:15  
A słuchaj, ja monitor wydajności to tam nie było uruchomione.

**Damian Kaminski** 58:19  
Nie wiem, więc nie to trzeba zbadać konkretny przypadek z Łukaszem, ewentualnie porozmawiać.

**Lukasz Bott** 58:24  
Czuję się poskrobko, tak?

**Damian Kaminski** 58:25  
Boże, Przepraszam, nie, nie, nie poskrobko to jest on remisowe z danielem, on zna bardziej temat, no bo tak jak mówię wczoraj dostaliśmy potwierdzenie, że klient się zgadza, a ja zaproponowałem rozwiązanie 2 dni na analizę w lipcu, więc no już szczerze mówiąc nie pamiętam. Daniel jest z nimi na bieżąco, więc tutaj też nie chcę robić za głuchy telefon, tylko trzeba się do Daniela odezwać, ustalić co wiemy i.

**Lukasz Bott** 58:50  
Dobra.

**Damian Kaminski** 58:52  
I zrobić analizę problemu. Na razie nic jeszcze nie mówić. Nie mówimy o poprawkach.

**Lukasz Bott** 58:59  
Dobra, no znaczy, czyli tu jest?

**Damian Kaminski** 59:02  
Na 2 płaszczyznach nie to może być poprawka systemowa, a może być poprawka procesowa? Tak więc tutaj, no nie wiemy na ten moment właśnie po to jest ta analiza.

**Lukasz Bott** 59:15  
No też ktoś od Daniela musiał wybrać udział w tym?

**Damian Kaminski** 59:20  
No to jest opiekun klienta i niech się można go zaangażować. Dobra, wrzucę tam Piotra, w sensie wywołam. Poproszę, żeby Daniel się do ciebie odezwał i żebyście ustalili jakiś termin. Klient czekał 2 miesiące, więc według mnie to nie jest coś, co musimy jutro rozpocząć, ale po prostu musimy jakkolwiek zdeklarować termin, kiedy taką analizę poczynimy i tyle.

**Lukasz Bott** 59:41  
Dokładnie.

**Damian Kaminski** 59:44  
Dobra, to tyle dzięki.

**Lukasz Bott** 59:46  
Dzięki dobry.

**Damian Kaminski** 59:47  
Cześć.

**Lukasz Bott** 59:48  
Część.

**Anna Skupinska** 59:49  
Cześć.

**Janusz Bossak** zatrzymano transkrypcję
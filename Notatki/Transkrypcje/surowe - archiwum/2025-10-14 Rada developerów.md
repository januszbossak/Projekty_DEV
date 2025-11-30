**Transkrypcja**

14 października 2025, 08:00AM

**Janusz Bossak** 0:18  
No dobra, słuchajcie, ten nie tracąc czasu, bo to Adrian masz temat odnośnie tego tych e doręczeń to jest proszę, żebyście z Piotrem razu.  
Uzgodnili o co tam chodzi i jak to powinno być zrobione.

**Adrian Kotowski** 0:35  
Na samym początku powiem, że no tam jest problem z niespójność ta dokumentacji, bo jest oficjalna dokumentacja od Poczty Polskiej i 2 miesiące temu dostaliśmy odp.  
To i znaczy inna wersja i dokumentacji, więc tam tam szczerze po prostu to, że tować wszystko na 2 razy i mam do teorii, że po prostu może jakoś tam jest inna api po prostu czy inne intencje, aby która ma inne implementacje, po prostu i stąd takie problemy między maszynami, że nie wiem jak to działają.  
Czyli 2 dzioby są uruchamiane przez znaczy jeżeli chociaż na przykład 2 organizacji są organizowane przez 2 różne 2 różne maszyny, tam jest jakoś nie wiem, czy przekierowanie na pewno te drugie api i stąd, jakby ta różnica jest bowiem, że działa jedna instancja serwisu, to wtedy nie ma problemu, nawet jak ta wersja. Maszyna druga działa, więc no to dla mnie takie jest. No jeszcze próbuję, to mam to ograniczony pomimo możliwości, po prostu w tym obszarze. No bo jednak jest ten ta cała pi.

**Piotr Buczkowski** 1:30  
Ale problem jest, że u nas z jednego serwera nie działa drugiego działaczy w poczcie.  
No jednym serwerze działa na drugim nie działa.

**Adrian Kotowski** 1:40  
Na jednym nie działa czy nie działa? Jeżeli są 2 maszyny?

**Piotr Buczkowski** 1:41  
Ale u nas czy poczcie?

**Adrian Kotowski** 1:45  
Któryś raz.

**Piotr Buczkowski** 1:47  
U nas czy poczcie?

**Adrian Kotowski** 1:49  
No przyjmujemy odpowiedź, że żądanie jakby był błąd forbidden czy tam no.

**Piotr Buczkowski** 1:55  
Ale u nas u nas.

**Adrian Kotowski** 1:57  
U nas jeśli tak znaczy.

**Piotr Buczkowski** 1:57  
Czy u nas my mamy 2 serwery, na którym działają, żeby tak 2 a?

**Adrian Kotowski** 2:01  
Nie, nie, jeśli się społeczny polski przychodzi serwera tego serwera, który obsługuje api.

**Piotr Buczkowski** 2:08  
Ale.

**Adrian Kotowski** 2:09  
My wysyłamy żądanie, otrzymujemy autora.

**Piotr Buczkowski** 2:10  
Zrozumiałym, że u nas mamy 2 asy tak jeden, a się poczekaj, poczekaj.

**Adrian Kotowski** 2:14  
Znaczy, mamy 2 usługi produkcyjne, akurat?

**Piotr Buczkowski** 2:17  
Dla jednym, ale się działo na drugim nie działa.

**Adrian Kotowski** 2:20  
Tam, gdzie warunkowo, bo jeżeli jest tylko jeden a s uruchomiony to wtedy działa.

**Piotr Buczkowski** 2:20  
Czy nie?  
A jeżeli ten dług jest uruchomiony tylko.

**Adrian Kotowski** 2:33  
Mm to to to też działalność.  
To twój zawsze działa?

**Piotr Buczkowski** 2:37  
Czy czyli po czy poczta może ograniczać tak, że tylko z jednego serwera się łączy dana firma?

**Adrian Kotowski** 2:43  
Znaczy na stówce tak to się tym stawiam tak na produkcji oficjalnie nie.  
Ale mamy jedno ip, teraz jeszcze mamy tych 4, masz 7 produkcyjne, 2 usługi, 2 polityczne pod usługę 2 maszyny polityczny, ale to jest system jak powstałego ip, bo tak się mówiliśmy z Łukaszem po kroku, żeby tak robić.

**Piotr Buczkowski** 2:55  
Na pewno.  
Już poprze.

**Adrian Kotowski** 3:09  
No i tam jest jeszcze sama wersja tego programowania i takie same ustawienia, no oraz też czasu jest taka sama.  
I też certyfikaty są poprawne, bo sprawdzałem, że faktycznie jest ten sam certyfikat tego, że plany.

**Piotr Buczkowski** 3:24  
Nie, ale dobrze po czasie sprintu zrozumiały, że SA jeden działa, a z alsa 2 nie działa, albo odwrotnie skończona się z jednego naszego.  
Naszego asa działa z drugiego nie, ale rozumiem, że to nie jest to tak.

**Adrian Kotowski** 3:39  
Znaczy ciężko mi.

**Piotr Buczkowski** 3:39  
Wyloguje cię za SA.

**Adrian Kotowski** 3:42  
Słuchaj, 3 razy, bo nie do końca.

**Piotr Buczkowski** 3:43  
Wywaliłem cię za sa bo sam się zalogowałam i ty byłeś.

**Adrian Kotowski** 3:47  
A dobra o k. Znaczy to jest tak, że jeżeli są 2 2 asy uruchomione, jeżeli no.  
Wtedy z tej dwójki nie działa wtedy jedynka działa zawsze nie były takie sytuacje, że linki nie jest to działało. Natomiast jeżeli jest tylko dwójka uruchomiona albo jedynka, to też zawsze działa, ale nie może być tak, że jest tylko jedna maszyny muszą być 2, bo no to mamy 2 pełne działały.

**Piotr Buczkowski** 4:10  
Koment bo już coś kręcisz.

**Janusz Bossak** 4:13  
To znaczy tej opowieści mi się wyłania obraz, że to jest problem absolutnie po naszej stronie konfiguracji, tak jak mówisz albo 2 i p Ki, albo w ogóle, że 2 serwery konkurencyjne żądanie zbyt szybkie.

**Adrian Kotowski** 4:28  
Znaczy to jest jakby tam były generalnie 3 problemy znaczy 2 problemy wynikały z tego, że po prostu była źle napisana dokumentację. Tam były te różnice między 2 wersjami. To udało mi się już chwycić. To poprawiłem i teraz działa. Tak jak mówiłem, można powiedzieć 50%, że po prostu jest ten problem tych 2 serwerów wcześniej nie działało przez 2 miesiące.

**Piotr Buczkowski** 4:48  
Ale ty nie odpowiedziałaś na pytanie, czy da się przepisać ten.  
To jednak serwera.

**Adrian Kotowski** 4:56  
Się przypisać na drugi serwer.

**Piotr Buczkowski** 4:58  
Że.  
Nie wiem, coś znał okrągło to opowiadasz.

**Janusz Bossak** 5:06  
Narysuj, my to może panowie panie?

**Piotr Buczkowski** 5:09  
Bo sprawdziłem właśnie tak rzeczywiście wychodzące, a ip mamy ten sam 20, 56, 84 214 za obydwu asów.

**Adrian Kotowski** 5:22  
Czy te mogą być różne porty?

**Piotr Buczkowski** 5:23  
Jeżeli ten sam request wyjście teraz jeden a dostępny job wyjdzie za 2 to będzie działać czy nie będzie działać?

**Adrian Kotowski** 5:33  
No znaczy nie powinno działać. No jak wcześniej mówiłem, no jeżeli tam jest, masz 2 2 równoległe czy 2 2 jednocześnie i obsługują 2 różne organizacje, ponieważ się zdarza.

**Piotr Buczkowski** 5:44  
Ale.

**Adrian Kotowski** 5:46  
Wtedy te dwójki nie działa.

**Piotr Buczkowski** 5:47  
Zaraz.

**Adrian Kotowski** 5:51  
Mam to zalogowany takie sytuacje tak że.

**Piotr Buczkowski** 5:53  
A jeżeli jest odwrotnie, że na przykład zadziała, czy w ogóle zadziała 2 kiedykolwiek?

**Adrian Kotowski** 5:58  
No i wtedy jakieś usługa. Pierwsze usługa na pierwszym właśnie wyłączona, tak jak w teście to udałem się zalogować to działało.

**Piotr Buczkowski** 6:07  
Czy możemy tam jest taki mechanizm, że preferred Server?

**Adrian Kotowski** 6:11  
Mhm.

**Piotr Buczkowski** 6:11  
Czy jeżeli tam ustawimy dla tej usługi zawsze, a 0 1 tak, to to będzie działał albo a 0 2.

**Adrian Kotowski** 6:18  
To mogę to uruchomić sprawdzić, no.

**Piotr Buczkowski** 6:22  
Czy możemy tak zrobić?

**Adrian Kotowski** 6:23  
No dobra, czyli nie wiem czy teraz to w ciągu dnia, bo rytualnie po godzinach mogę to wstawić chyba się.

**Piotr Buczkowski** 6:27  
W każdej chwili możesz to zrobić kolejne wywołanie w kolejne wywołanie, czy tam powiedzmy będzie kolejne wywołanie, tak będzie już uwzględniało to.

**Adrian Kotowski** 6:28  
A dobra to wiecie to.  
Dobra, no to sprawdza to na razie.

**Janusz Bossak** 6:41  
Dobra, czy to?

**Piotr Buczkowski** 6:42  
Ale dobrze Jeszcze raz.  
A ty byś ustawił już wszędzie tę preferencję, a 0 2 to by działało.  
W ogóle byłby jeden.

**Adrian Kotowski** 6:50  
Dzień no muszę muszę sprawdzić, no bo to teraz to co mówisz jeszcze tego nie weryfikowałem tego narobiłem także wyłączałem już jedną usługę w nocy i zobaczę co się stanie.

**Piotr Buczkowski** 7:03  
Mi się nie podoba.

**Janusz Bossak** 7:08  
Dobra, słuchajcie, to proponuję tak, ponieważ temat jest dłuższy pewnie i więcej trzeba różnych prób zrobić to wniosek z rady jest taki, że Piotr z adrianem intensywnie nad tym popracują wspólnie, żeby znaleźć rozwiązanie, bo możliwe, że po prostu to jest jakaś kwestia konfiguracji po naszej stronie tych serwerów i takie mam jakieś przeczucie, że tak to jest, że to nie jest kwestia problemu Poczty Polskiej tylko.  
Ustawienia tych serwerów i sposobu ich, że tak powiem, współpracy, tak.  
Dobra.  
Temat jeden mamy drugi temat to są te dashboard gdy systemowe to temat ani myśleniem ogłasza.  
Kilka słów powiedzieć.

**Anna Skupinska** 7:52  
Przestałem się, co chcecie o nich mówić.

**Janusz Bossak** 7:56  
Oczywiście zrozumieć ten problem podmienia idiotów.

**Anna Skupinska** 8:02  
Znaczy to to już rozwiązane w sumie jest problem. Chodzi o to, że w.  
Można w dashboard systemowych ustawiać sobie pola wspólny, a w tych polach wspólnych jest odwołania do raportu, w którym znajduje się to pole, a to odwołanie do raportu, to jest idea raportu. Oczywiście jak się tworzy te raporty, to my nie wiemy, jakie te raporty będą miały i d, dopóki go nie utworzymy w bazie danych.  
Oczywiście więc muszę, no ale po prostu tam wstawiam.  
Yy tych dasz wordów, a czy raportów po gui jest zawsze taki sam i potem, gdy zostaną ustawione te raporty, to muszę wstawić tam zamiast tych buildów wstawić raport i d no i zrobiłam kod który to robi wczoraj.

**Janusz Bossak** 8:43  
No ale dlaczego tworzymy najpierw dashboard, a potem raportem nie bardzo.

**Anna Skupinska** 8:46  
Eda tego, że raporty, jak jeżeli należą do dashboard u to potrzebują odwołania się do tego dashboard do idea tego dashboard du.

**Piotr Buczkowski** 8:52  
A to raport jest dopiero zapisywany przed po pierwszą 10. Zapisz, tak międzyczasie można go edytować.

**Anna Skupinska** 8:58  
A czy ja mówię tutaj o tym jak chcemy ill, jak uruchamiamy kod, który nam te raporty tworzy?  
Przy aparacie, bo to są te systemowe, one są tworzone przy updacie to nie chodzi o klikanie.

**Janusz Bossak** 9:10  
Mhm.

**Anna Skupinska** 9:11  
Tak więc chodzi o to, że muszę, że raporty się odwołują do nas wordów i raporty da się ją do raportów, no i nie mogę 2 zrobić naraz pierwszych. Jedno musi być pierwszy. No akurat ja zrobiłam tak wcześniej, że naprawdę tworzą dashboard, a potem raporty, dlatego, że raporty ma dwoje, dodasz bardów, jest ta głową wygodniejsze dla skazuje się już do odwołania do raportów. No więc.  
No albo jest jedno pierwsze, albo drugie jest pierwsze.

**Piotr Buczkowski** 9:35  
Ale zaraz zaraz zaraz.  
Powiedziałeś, że to nie jest zapis czy kitty to jest, kiedy to występuje.

**Anna Skupinska** 9:42  
A czy to się dzieje kiedy?  
Ab datujemy system on wtedy tworzy sobie raporty i dashboard systemowe.

**Piotr Buczkowski** 9:52  
Tylko wtedy.

**Anna Skupinska** 9:53  
Tak, to jest tylko tutaj się dzieje. Później jeszcze doszło już potem nie są w ogóle ruszane, bo nie powinny być zapisywane.

**Piotr Buczkowski** 9:57  
Ale.

**Damian Kaminski** 9:57  
Czyli tylko jak robimy update bazy danych tak o to ci chodzi to.

**Piotr Buczkowski** 10:00  
A raporty systemowe nie mają stałych jajników.

**Anna Skupinska** 10:00  
Tak.  
Nie, ale mają guide stare, mają stare guide.  
Pogodzila się dzisiaj rozpoznaje.

**Adrian Kotowski** 10:10  
Jest także w innym mieć ujemne te ujemne.

**Anna Skupinska** 10:13  
A czy nie to jem na indyki to są w tych.

**Adrian Kotowski** 10:17  
Źródłach.

**Anna Skupinska** 10:17  
W źródłach danych.

**Piotr Buczkowski** 10:18  
Wśród.

**Lukasz Bott** 10:19  
No to przy okazji chciałem ten temat poruszyć, czy na pewno musimy stosować ten ujemny aiki bo.

**Piotr Buczkowski** 10:25  
Nie, to zły pomysł, odejdź od tego, jeżeli to możliwe.

**Lukasz Bott** 10:27  
Też też tak uważam. No skoro w bazie danych mamy mechanizmami bazy danych, jak się identyfikatory, które są liczbami de facto naturalnymi, no bo w większymi całkowitymi większymi od zera.  
To dlaczego śmy wprowadzili ten mechanizm ujemny? Tak no.

**Piotr Buczkowski** 10:42  
Żeby odróżnić systemowe od kasty.

**Anna Skupinska** 10:46  
Nie systemowych.

**Lukasz Bott** 10:47  
Tak, ale to nie łatwiej było dodać kolumnę, po prostu, że to jest systemowy.

**Anna Skupinska** 10:47  
A no takie z raportach i dashboard dach.

**Lukasz Bott** 10:54  
To dlaczego z tego nie korzystam?

**Piotr Buczkowski** 10:57  
Był to podjęliśmy złą decyzję.

**Lukasz Bott** 11:00  
No nie wiem, żeśmy podjęli złą decyzję, więc pytanie, czy przy tej okazji jak i tak coś tam majstruje, my przy tych raportach systemowych, tak czy to czy tego nie uporządkować i nie zrobić prawilnie tak no.

**Anna Skupinska** 11:12  
A jak chcecie to możemy.

**Piotr Buczkowski** 11:14  
Warto by było to warto, by było to zrobić.

**Lukasz Bott** 11:14  
No bo a ja mówię ania.  
Ja mówię to w.

**Piotr Buczkowski** 11:18  
Tylko trzeba trzeba zaplanować dobrze.  
Migracje.

**Lukasz Bott** 11:23  
Dokładnie, bo bania, bo ja mówię to w kontekście takim, że ponieważ przy test tej reedycji tych raportów systemowych powstało kilka nowych źródeł systemowych, tak, no i no i oczywiście nadała się im tam te indeksy ujemne, tylko.

**Anna Skupinska** 11:26  
Mhm.  
Mhm.  
Tak.

**Lukasz Bott** 11:42  
To ci się odbiło rykoszetem na mechanizm synchronizacji, który nagle, w który robił selekt coś tam from i tutaj nazwa tabeli, w której był używane, czyli DPSRC podkreślenie minus 22. No i oczywiście fatal error. Tak no bo się wywalił na składni tak. No i na przykład synchronizacja tych źródeł nie działała. Ja robię raport systemowy i się zastanawiam, doszło, nie mam danych, nie.  
Na szczęście miałem porów.  
Fajnie, że te dane powinny być tak, ale nie widzę tych danych no i po nitce do kłębka doszedłem, że kurne problemem jest właśnie właśnie ten, że się synchronizacja źródeł systemowych, a kilka jest lokalnych, bo muszą być lokalne, bo się przeliczają agregację jakieś raz na dobę taki 100 zaplanowane. No właśnie powodują ten ujemny indeks tych źródeł powoduje, że no na przykład mechanizm synchronizacji się wywala, więc jej jeśli moglibyśmy od tego odejść, to odejdźmy tak no.  
Wiem, że się kiedyś tam podjęli taką decyzję, jak widać się ona niekoniecznie.  
Sprawdziło tak czy sprawdza.

**Janusz Bossak** 12:51  
Co jest do zrobienia w takim razie w tym w takim?

**Anna Skupinska** 12:54  
To jest do zrobienia, ale to zajmie trochę czasu.

**Janusz Bossak** 12:57  
Ale co jest do zrobienia, że co?

**Anna Skupinska** 12:59  
A czy a czy zamiast jest możliwe to żeby zmienić żeby źle systemowe nie miało ujemnych laików, tylko zamiast tego miał i buildy i żeby było napisane, że są one systemowe dodać po prostu trzeba było 2 2 kolumny jeden odbył idea, a druga od systemu origi.

**Piotr Buczkowski** 13:16  
To znaczy tak naprawdę tutaj trzeba też pomyśleć o emigracji. Tak, bo to już jest.

**Anna Skupinska** 13:19  
E tek tak to też opowiedzieć o tym, że żeby to się jeżeli jest po staremu to żeby się ustawiło na nowy system bez problemu.

**Piotr Buczkowski** 13:27  
Znaczy trzeba dodać kolumnę.

**Anna Skupinska** 13:30  
A jeszcze jest inny problem, bo.

**Piotr Buczkowski** 13:31  
Prawie czy czy jeżeli kolumna, czy ta kolumna, system, raport, że miała też na przykład ujemną wartość i tam przepisywać wartość zajmuje. Jeżeli już utworzymy tak ignorujemy wartość normalną i później przy jakiś migracji? Jeżeli ktoś ma ustawione gdzieś minus.

**Anna Skupinska** 13:41  
Tak to też.

**Piotr Buczkowski** 13:48  
To, że nadstawię tej kolumny szukać tak i poprawić.

**Anna Skupinska** 13:54  
Tak więc problem też taka jest taki, że jeżeli ktoś już zrobił wcześniej jakiś raport oparty o źródło systemowe i ono nagle się zmieni i d no to nagle ta idea będzie wskazać na miejsce, gdzie nic nie ma, więc te raporty wszystkie zostaną popsute.

**Piotr Buczkowski** 14:07  
Dobrze, dlatego mówię to to i która jest teraz trzeba przepisać do nowej klub.

**Anna Skupinska** 14:12  
Tak.

**Piotr Buczkowski** 14:13  
I.  
Przy szukaniu źródła z raportu.  
Szukać po tej, jeżeli zwartość i jawna to szukać po tej kolumnie, gdzie zostało to przepisane.

**Anna Skupinska** 14:24  
Mhm.

**Janusz Bossak** 14:26  
Ja mam wrażenie takie, że.  
No czyli nasi klienci jakoś chyba nie bardzo na razie korzystają z tych źródeł systemowych.  
I z tych raportów systemowych i prawdopodobieństwo, że ktoś sobie zrobił, jest bardzo małe.

**Piotr Buczkowski** 14:40  
Ewentualnie.

**Janusz Bossak** 14:42  
Ja bym tą kompatybilnością.

**Piotr Buczkowski** 14:43  
Na czas migracji dodać.

**Damian Kaminski** 14:43  
Jest zerowe mówiąc wprost.

**Janusz Bossak** 14:45  
Zerowe ja bym tą kompatybilność tutaj przerwał, po prostu ********* to i zrobić po bożemu, tak jak tu Łukasz mówił, tak jak to powinno być. Po prostu trudno, najwyżej nie będzie działać tak jak.

**Lukasz Bott** 14:59  
Mhm.

**Damian Kaminski** 14:59  
Słuchajcie, nawet serwis nie miał do końca świadomości, to wybrzmiało. Była taka informacja, że coś takiego jak raporty systemowe istnieją. Abstrahując już od klientów, jak zdarzy się jeden klient, który raz tam zajrzał, to na pewno z tego nie korzystał, jakoś tam wybitnie i nic tu się nie stanie.

**Lukasz Bott** 15:18  
I też mi się jeżeli jeżeli zajrzał to zajrzał do raportów systemowych, ale niekoniecznie może tak nie nie, ale niekoniecznie może tworzył coś własnego na podstawie źródeł systemowych, bo to to jest. To są 2, 2 odrębne byty. Tak no to że ze sobą.

**Damian Kaminski** 15:22  
Z ciekawości.  
Zawsze może poprawić tak, jeśli struktura źródła się nie zmieni, można wyeksportować i zmienić aidy źródła systemowego i będzie działać.

**Lukasz Bott** 15:35  
Tak no można.  
Mm, tak, ewentualnie możemy przyjąć taką zasadę, prawdopodobieństwo jest tak jak mówicie, jest prawdopodobnie niskie, tak, że ktokolwiek z tego korzystał, to możemy przyjąć na klatę, że jeżeli będzie miał z tym problem, to mu tam nie wiem. Na zasadach gwarancji nieodpłatnie mu to konfigurujemy, tak.

**Janusz Bossak** 16:01  
Do.  
Dokładnie tak, nawet możemy tutaj już nie wyręczać się serwisem w sensie danielem, tylko w razie czego to czy Łukasz, czy ktoś tam on nas się zaloguje i tam 1, 2 czy 3 raporty poprawi, jeżeli będzie trzeba tak i koniec.

**Lukasz Bott** 16:05  
Tak.  
Dokładnie tak zróbmy i tyle, a.

**Janusz Bossak** 16:18  
Tak jak dopiero mówisz teraz jakiś takich mechanizmów, które tam uwzględnią, że był minus, teraz nie ma i tak dalej zróbmy to po prostu tak jak powinno być i już.  
Ania, możesz to zaplanować.

**Anna Skupinska** 16:31  
Jasne.

**Janusz Bossak** 16:33  
Yy, tutaj Damian, ty się opiekujesz, czeka mnie się tymi systemowymi. Łukasz, a Łukasz się opiekujesz? Dobra, to Łukasz za nią zaplanujcie to dokładnie Jeszcze raz ten przejście nasze Jeszcze raz na to przejście na na te buildy, dla raportów systemowych i po stronie źródeł systemowych.

**Damian Kaminski** 16:38  
Łukasz.

**Lukasz Bott** 16:50  
Źródłem.

**Janusz Bossak** 16:54  
I po stronie raportów no i tak żeby się nie popsuły, normalne raporty i normalne źródła, tak nie nie systemowe.

**Lukasz Bott** 17:03  
No.

**Janusz Bossak** 17:05  
Może to jest moment, kiedy warto przejść w ogóle na gui, gdy źródłach systemowych, obojętnie czy systemowych, czy nie systemowych źródłach danych, tak źródło danych ma swój limit.

**Piotr Buczkowski** 17:19  
Część stronie z raportach z raportów warto.  
Chcemy dzisiaj innego idy.  
Odwołania.

**Janusz Bossak** 17:27  
Znaczy, to jest zadanie dla was tutaj Łukasz i ania, tak, musicie to przemyśleć wszystkie konsekwencje właśnie używania tego.  
W raportach dashboard dach, stare raporty trzeba przemyśleć, czy coś tam się nie popsuje. Wiecie, no wszystkie te.  
Skrajne przypadki, tak, żeby wziąć, także to jest wasze zadanie na następną radę za 2 dni, żebyście mieli już taki przygotowany.  
Projekt tego przejścia na te guide.  
Za wszystkimi możliwymi potencjalnymi konsekwencjami.  
Dobra, to to mamy następna jest tabelka formularzu.

**Piotr Buczkowski** 18:11  
To, że to było mój błąd?  
Rzeczywiście, ja to zgłaszałem. Tabelka była nie ma.  
Moja moje.  
Moje to.  
Gdyby nie wywołało, że ta się uświetnić tak tabelka w postaci tabela.  
Jeżeli to jest tabela zagnieżdżone, a w tabelce typu formularz.  
Bo to musi być bardzo mała tabelka 2 3 kolumnami, żeby to miało sens.

**Janusz Bossak** 18:45  
No tak tak, no bo tu na tym małym kafelku, bo rozumiem, że to chodzi o te małe kafelki, nie o.

**Piotr Buczkowski** 18:48  
Tak.

**Kamil Dubaniowski** 18:50  
Tak tak te.

**Piotr Buczkowski** 18:50  
Tak.  
Możecie wyświetlić to 2, 1 1 6 9 czy ja mam wyświetlić?

**Janusz Bossak** 18:56  
Weź.

**Piotr Buczkowski** 19:01  
To chodzi o to, tak?

**Janusz Bossak** 19:04  
No no no no tak rozumiem, no k, znaczy wiecie, no sens wyświetlania tego jest tak jak mówisz, no duża tabela, to jakby nie ma sensu.  
No ale to jest kwestia tego, jak to sobie tam poukłada, tak jeżeli tu będzie miał tabelkę na przykład nie wiem z imieniem, nazwiskiem członka rodziny, to czemu nie tak?  
No dobrze.

**Kamil Dubaniowski** 19:28  
Dobra, no ale co na to jak ktoś doda tutaj 20 pól? No to musimy też to obsłużyć, skoro to obsługuje.

**Piotr Buczkowski** 19:35  
No to będzie źle wyglądało, ale.

**Janusz Bossak** 19:37  
Krolem.

**Piotr Buczkowski** 19:38  
Nie, nie, to nie nie, to nie.

**Kamil Dubaniowski** 19:39  
Nie no bo na na no to jest osobne zgłoszenie też.

**Piotr Buczkowski** 19:41  
Nie.

**Janusz Bossak** 19:43  
Skoro być tak.

**Piotr Buczkowski** 19:43  
Niech ktoś przemyśli.  
Zobaczysz, że to źle wygląda i przemyśleć swoje zachowanie.

**Kamil Dubaniowski** 19:49  
No myślę, że tu też się wypadki przypadek, no ale jak już wyszło to.  
Żeby ten kontakt utrzymać.

**Janusz Bossak** 19:54  
Nie no słuchaj, jesteś.  
Niech stanie wszystkiego obsłuży jak bo to trzeba by tą tabelkę też zamienić na z kolei znowu już.

**Piotr Buczkowski** 20:00  
Powinno powinno dobrze działać, jeżeli tabela w tabeli, ale soby dwe jako formularze tak.  
Wtedy okej.

**Janusz Bossak** 20:12  
Bo to wtedy będzie taki formularz w formularzu.

**Piotr Buczkowski** 20:15  
Tak jak tak jak w telefonie.  
Jak to bywa w telefonie o telefonie?

**Janusz Bossak** 20:20  
No to jeżeli to tak się wyświetla, no to.  
Jest pytanie czy?  
Tabelkę zagniesz żoną można ustawić w tryb pod formularza.

**Piotr Buczkowski** 20:31  
Yy formularza nie pod formularzem.

**Janusz Bossak** 20:33  
Formularzem tak.

**Piotr Buczkowski** 20:35  
Pod formalność to jest to z lewej tak i nie można, znaczy nie będzie się już spała i też nie ma polski.

**Janusz Bossak** 20:42  
Jako potwor formularz może być tak.

**Damian Kaminski** 20:43  
To.

**Piotr Buczkowski** 20:45  
Tak, tak znaczy powinniśmy się bać?  
Tak jak na telefonie, tak?

**Janusz Bossak** 20:53  
No nie wiem jak się wyświetli.

**Lukasz Bott** 20:53  
W sensie w wersji mobilnej.

**Piotr Buczkowski** 20:55  
Tak, tak.  
Znaczy.  
Z takim przeciąganiem lewo, prawo tak.

**Janusz Bossak** 20:59  
No właśnie to trzeba postawić.

**Damian Kaminski** 21:03  
Czyli nie o k czyli w formie tabelarycznej tylko po prostu z przeciąganiem.

**Piotr Buczkowski** 21:08  
Nie, nie, nie.

**Janusz Bossak** 21:10  
Nie, nie, nie, bo znaczy słuchajcie, bo są 2 rozwiązania.  
Pierwsze rozwiązanie, jeżeli zamieniam tabelę główną.  
Na widok formularza tak jak tu.  
To mogłoby być tak, jak mówi Piotr.  
Jakby konsekwentnie, tak jak na mobilnym widoku, wymuszenie pokazywania tej pod tabelki też jako formularze owej po prostu.

**Piotr Buczkowski** 21:36  
No tak.

**Janusz Bossak** 21:37  
Czyli nie ma czegoś takiego, że mogę sobie właśnie taki obrazek zrobić jak teraz, czyli że mam pierwszą tabelę tą główną jako formularz, a tą pod tabelkę jako tabelkę i to jest pytanie czy chcemy, czy nie chcemy tak, żeby było tak, że to.

**Damian Kaminski** 21:51  
A czy to nam coś upraszcza?  
Teraz rozpatrujemy to w skrajnych przypadkach, czyli tabela i jedno kolumnowa i tabela wielo kolumnowa.

**Janusz Bossak** 21:56  
Znaczy.  
Znaczy trudno ocenić, czy coś upraszcza, tego wolałbym mieć jakby jednolitość zachowania, tak żeby nowość. Wracając do tej dokumentacji naszej, że to tak działa, jakby było wiadomo.  
Ale jeżeli ktoś ustawia.  
W tej tabelce, którą tu Piotr pokazywał wewnątrz.  
Formularza.  
Bardzo dużo colum no to musi się liczyć z tym, że będzie mu ta tabelka dla niego niewygodna, tak, że będzie musiałem przewijać, ale dlaczego by mu tego zabronić? Tak o to mi chodzi.

**Damian Kaminski** 22:38  
No no właśnie do tego zmierzam, bo my możemy napisać to nawet w konsekwencji tej dzisiejszej dyskusji, że my tak zalecamy, a wszystkie inne rozwiązania.

**Janusz Bossak** 22:38  
I.

**Piotr Buczkowski** 22:45  
Znaczy dobrze, przy powinniśmy przywrócić starą zachowanie i tylko tyle.

**Janusz Bossak** 22:52  
Tylko tyle dokładnie.  
Znaczy no.

**Damian Kaminski** 22:56  
Możecie to podsumować w takim razie?

**Janusz Bossak** 22:58  
Mia jeszcze interesuje odpowiedź na jedno pytanie, czy dobrze było, gdyby ktoś w międzyczasie by klikał taki przykład, bo Piotr powiedział jedną rzecz, która mnie zainteresowała, że na mobilnym to się wyświetla jako formularz, znaczy formularz? Tak no bo złe nazwy.  
Yy używam.  
Czyli tam jest ten zamieniania tej tabelki?

**Piotr Buczkowski** 23:16  
No bo.  
No bo no, jeżeli jeżeli popatrzysz na to.  
To to wygląda jak ekran telefonu. Tak jeden taki sekcja to jest tak jakby ile telefonów obok siebie włożyć.

**Janusz Bossak** 23:27  
Tak.  
Ale wiem.  
Ja wiem, ja wiem, tylko mi chodzi o to teraz jak to co jest na czerwono zakreślone wygląda na telefonie czy tak jak jest.

**Piotr Buczkowski** 23:38  
Na telefonie na telefonie wszystkie to chociaż nie wiem czy wszystkie na pewno tabelę tego pierwszego poziomu sami są zamieniane na.

**Janusz Bossak** 23:43  
No właśnie.

**Mariusz Piotrzkowski** 23:45  
Mogę pokazać, mam gotowa.

**Piotr Buczkowski** 23:49  
Na formularz wygląd formularza, a czy pod tabelę zamieniane to nie wiem.

**Janusz Bossak** 23:53  
No właśnie to bo tak powiedziałeś, jakbyś był pewny, że tak jest. No to pokaż Mariusz.

**Mariusz Piotrzkowski** 23:57  
Mogę pokazać, mam gotowa.  
Tutaj jest na starej wersji, tu jest na starej wersji, normalnie było tak.  
W wersji.

**Piotr Buczkowski** 24:08  
No i nieużyteczne nie należy tak robić, ale działa coś tam działa.

**Mariusz Piotrzkowski** 24:13  
W wersji mobilnej, choć wierzyć.

**Piotr Buczkowski** 24:19  
Chyba za duża na to.

**Mariusz Piotrzkowski** 24:21  
Mhm wersji mobilnej. Tak, czyli oba są naderwane jako formularza.

**Piotr Buczkowski** 24:22  
No o to czy czyli, czyli moja moja pewność była dobra.

**Janusz Bossak** 24:23  
No właśnie czyli.  
Moja pewność była dobra, czyli na wersji mobilnej.  
Sam system siebie nie pytając się użytkownika jak sobie zaprojektował tą tabelkę wyświetla tą tabelkę w ten sposób według mnie tak powinno działać na formularzu tak samo, bo to jest dokładnie powinno być to dokładnym odzwierciedleniem.

**Piotr Buczkowski** 24:37  
Tak.  
Tak.  
Takie takie coś proponowałem.

**Mariusz Piotrzkowski** 24:50  
Aktualnie jest coś takiego, że na mobilnym to się wyświetla w taki sam sposób.  
Czyli mamy główną tabelę i tą pod tabelę, jednak w przypadku tak jest w łonie napisane pełnego jest jakiś błąd, ktoś nie przewidział, że w ogóle tam tabela się może środku renderować i cały czas kombinuje jak to naprawić.

**Piotr Buczkowski** 24:55  
I.  
Nie naprawiaj zrób tak, żeby było jak na mobilnym.

**Mariusz Piotrzkowski** 25:11  
O k dobra, a to to bardzo uprości sprawę. Powiem szczerze, że już się nad tym chyba z 6 godzin.

**Damian Kaminski** 25:17  
A jeszcze możesz wrócić na ten widok mobilny na chwilkę.

**Janusz Bossak** 25:17  
No.

**Mariusz Piotrzkowski** 25:20  
W nowej czy w starej wersji?

**Damian Kaminski** 25:22  
Nie wiem to co przed chwilą pokazywałaś. Tam są 2 strzałki, które robią to samo pytanie, czy to tak powinno być? Taki był projekt.

**Janusz Bossak** 25:23  
A ten widok?

**Mariusz Piotrzkowski** 25:27  
Nie one niedawno to samo, bo jedna przewija tabelę zewnętrzną, a druga wewnętrzną.

**Damian Kaminski** 25:32  
Poczekaj tu masz strzałkę na wysokości?  
O to właśnie na środku ekranu i nad tym masz też strzałkę w prawo, która robi to samo według mnie.

**Piotr Buczkowski** 25:41  
Tak to.

**Mariusz Piotrzkowski** 25:43  
A o to ci chodzi, dobra?

**Piotr Buczkowski** 25:44  
To to robi to samo, tak?

**Mariusz Piotrzkowski** 25:46  
Tak, ale weź pod uwagę, że to może być wysoka tabela taką, która ma tam 15 20 pól na przykład i.

**Piotr Buczkowski** 25:53  
Chodziło o to, żeby było jakoś tam zaznaczone, tak, że to jest tylko ta część, tak.

**Janusz Bossak** 26:00  
Paluchem możesz przygotować tamtą.

**Piotr Buczkowski** 26:00  
Tylko.  
Już nie.  
Kiedyś można było już nie.

**Mariusz Piotrzkowski** 26:05  
To ty się teraz?

**Piotr Buczkowski** 26:09  
Bo ta jq jquery wrobel coś tam się zaczęło wiesić i.

**Damian Kaminski** 26:09  
No bo.  
Według mnie to jest do uproszczenia, albo to albo to, ale no dobra, to już poza tym zgłoszeń.

**Mariusz Piotrzkowski** 26:18  
Chyba kolejny błąd zarowym przez przypadek.  
Dodanie nowego wiersza jest puste.  
To też zaraz sprawdzę co z tym jest nie tak, ale to chyba od osoby zgłoszenia zrobią.

**Lukasz Bott** 26:31  
Swoją drogą w tym trybie mobilnym to też nie jest za wygodne do użyciem.

**Mariusz Piotrzkowski** 26:36  
W ogóle to źle działa.

**Janusz Bossak** 26:37  
Były tabelki w trybie mobilnym nie są wygodne, no bo bo nie są po prostu no.

**Lukasz Bott** 26:41  
Tak.

**Janusz Bossak** 26:44  
Struktura jest złożona takiej tabelki, no bo ma wiele wierszy, każdym wierszu ileś tych rzeczy, no to to nie jest wygodne do uzupełniania na mobilnym. No ktoś się uprze, no to wypełnia, no ale.  
A już tabelka w tabelce to już w ogóle jest.

**Lukasz Bott** 26:59  
To o tym bardziej mówić, to już wszystko co masz.

**Janusz Bossak** 27:02  
No dobra, słuchajcie, czyli wniosek jest jaki?  
Że robimy na wersji?  
Desktopowej.  
Tak jak jest na wersji tutaj, to co prezentuje Mariusz na wersji mobilnej, tak.

**Mariusz Piotrzkowski** 27:17  
Czyli coś takiego będzie tylko te rozpiski czy Wołyń?

**Damian Kaminski** 27:17  
Czyli, czyli opisując to, jeśli tabela nadrzędna jest wyświetlana w formie formularza.  
To wszystkie tabele osadzone również są wyświetlane w formie formularza.  
Tak.

**Lukasz Bott** 27:30  
Niezależnie od tych ustawień no.

**Janusz Bossak** 27:35  
No dobrze, no to jest.

**Damian Kaminski** 27:37  
Dobra, trzeba zrobić z tego wiki na wiki zaraz tej dyskusji.  
Może zamknijmy dyskusję, w sensie zamknijmy nagrywanie, rozpocznijmy następne.

**Janusz Bossak** 27:42  
Znaczy.

**Lukasz Bott** 27:47  
Ale czy chcesz tutaj na wiki wydawać to rozumiem, że to trzeba zrobić, bo w tej chwili nie jest to zrobione.

**Damian Kaminski** 27:51  
Tylko trzeba to opisać, bo zaraz coś powie, a czemu to się nam zmieniło?

**Janusz Bossak** 27:55  
Dokładny.

**Damian Kaminski** 27:55  
Bo może ktoś tak używał i my wtedy powiemy dlatego, że takie jest zalecenie projekt.  
I koniec nie ma wtedy baga.

**Janusz Bossak** 28:07  
Cóż, nie znaczy jeszcze trochę namieszam, bo może jednak może jednak.  
Dać w takim trybie możliwość wyboru. To są od czego zaczęliśmy, że jak sobie proj.  
Jak tam zaprojektował tabelkę i nie włączył jej w trybie?  
Formularza no to dostanie ją w takim zwykłym trybie tak, a w mobilnym jest tak jak Mariusz pokazał. No więc to jest pytanie, czy chcemy mieć równo w mobilnym i na desktopie, czy chcemy, żeby na desktopie jednak można było decydować?  
Czy ma być jako tabelka, czy ma być jako formularz?

**Damian Kaminski** 28:48  
Znaczy, jakbyśmy już mógł pokazać Jeszcze raz ten ekran, tam on de facto obrazuje ograniczenia. Jeśli to jest tabela maksymalnie 2 kolumnowa, to ma to sens w kontekście takiego juja tak czyli xa, ale jeśli jest to tabelka więcej niż dwukolorowa, no to.  
Jest to po prostu niepraktyczne, tak, bo tam widzimy, że się nie chodzi mi o tą wersję. To jest topową, bo tutaj jest jasne to, co przed chwilą wyświetlać, że tam o tylko o właśnie. No to jest po prostu niepraktyczne, no przewijanie jakieś.

**Lukasz Bott** 29:17  
No to.  
Piotr powiedział, działa.

**Janusz Bossak** 29:26  
Ale to jest wersja stara.  
Formularza.  
A jak jest na nowej?

**Damian Kaminski** 29:30  
No ale chcesz chcesz pozwolić na to tak, żeby to tak było?

**Janusz Bossak** 29:33  
Jak jest jak jest to ta sama sprawa dokładnie.

**Mariusz Piotrzkowski** 29:37  
Aktualnie wcale się nie wyświetli, bo jest błąd.

**Janusz Bossak** 29:41  
A no to to jest błąd krytyczny jest hotfix, no to naprawienia natychmiast.

**Damian Kaminski** 29:49  
W sensie jak gdzie tu się to powinno wyświetlić?

**Mariusz Piotrzkowski** 29:52  
Pomiędzy tymi wierszami.

**Damian Kaminski** 29:53  
Mhm.

**Mariusz Piotrzkowski** 29:54  
To jest właśnie ten błąd, który próbując wczoraj rozkminić, no i tam się dużo zmieniło, że mi to zajęło chyba z 3 godziny, bo to w ogóle oglądać jak to działa wszystko.  
No i teraz pytanie co mam z tym zrobić się jak to ma w końcu działać? Nie.  
Bo się znowu pogubiłem.

**Janusz Bossak** 30:12  
Znaczy, po pierwsze w ogóle ma działać, znaczy, żeby w ogóle się tabelka pokazała.  
Jest kwestia tylko w jakim trybie tak czy trybie tabel kowym czy trybie formularze owym.

**Lukasz Bott** 30:23  
No ale to jest, jeżeli to robimy, to dla nowym formularzu, to może zróbmy, że docelowo tak już Mariusz ma.  
Roboty jakoś robić to to to niech zrobi to docelowo może tak.

**Janusz Bossak** 30:34  
Ale Mariusz teraz.  
Tam Jeszcze raz może coś się pogubiłem, jeżeli ten formularz teraz ten, który masz wyświetlisz w trybie mobilnym to będzie działać dobrze, tak?

**Mariusz Piotrzkowski** 30:47  
Jeżeli się w mobilnym to powinien działać, wydaje mi się dobrze, ale tam przed chwilą miałem, miałem jeszcze jakiś błąd przy dodawaniu wierszy, ale to wyświetlanie jest poprawne każdym bądź razie.

**Janusz Bossak** 30:56  
To zrób tak, żeby no chyba tak to powinno działać nie w trybie desktopowym jak jak w mobilnym.

**Damian Kaminski** 31:05  
A możesz Jeszcze raz wrócić na tą wersję marcową?  
Mhm, możesz teraz zamienić ten widok tabeli wewnętrznej na układ formularzy owy.  
Żeśmy zobaczyli, bo teoretycznie, no będziemy się zbliżać do tego efektu, który teraz zrobisz. Zobaczymy jak ten edytuj pola formularza.  
A nie to to dobre.  
Czyli coś takiego dostaniemy?  
Konsekwencją, czyli zobaczcie, że tam jest też z krol poziomy, tylko wyświetlanie jest pionowe.

**Mariusz Piotrzkowski** 31:53  
To są jakieś glicze w ogóle znowu na starej wersji też to jest całe w ogóle według mnie dobrze robienie.

**Damian Kaminski** 31:55  
No właśnie.  
Nie, a Przepraszam to.  
O k dobra no właśnie, bo tak tak było zaprojektowane desktopową tak czyli.  
Tam nie było tych strzałek.  
Tylko jest właśnie pionowo z krol tak poziomy przewijania.

**Lukasz Bott** 32:18  
Nie.

**Damian Kaminski** 32:19  
Wierszy w formie colum.

**Janusz Bossak** 32:27  
No nie wiem czy to w taki wersji jest wygodniejsze czy nie.

**Damian Kaminski** 32:31  
No według mnie nie.  
Tutaj te Dodaj wiersze i Dodaj wiersze 2 razy to w ogóle nie wiadomo o co chodzi na dole.

**Janusz Bossak** 32:35  
Czyli.

**Damian Kaminski** 32:47  
To jest 2 razy w trzeciego kolumnie jest raz.

**Janusz Bossak** 32:51  
Chyba wniosek jednak jest taki, że to trzeba zrobić i tak i tak i tak znaczy.

**Mariusz Piotrzkowski** 32:51  
To chyba jakiś glicz.

**Janusz Bossak** 32:57  
Czyli w formie tabel kowej wtedy, kiedy ma to sens o niektórych.  
Albo w formie takiej, ale też dobrze. Jeżeli to ma sens dla innych, tak.

**Damian Kaminski** 33:09  
Znaczy pytanie, czy w ogóle ktoś takiego zagnieżdżenia używa? No ale tego niestety nie wiemy.  
Yy no pewnie można to jakoś sprawdzić na chmurach, ale.

**Janusz Bossak** 33:21  
Dobra, przejdźmy. Chodzi mi o to, żeby Mariusz miał jak najmniej robotę i żebyśmy mieli temat jakoś ogarnięty. Jeszcze raz nowy widok.  
Mobilny pokaż go.  
Tego przypadku.

**Damian Kaminski** 33:37  
Działa mobilny, działa tak Mariusz.

**Janusz Bossak** 33:40  
Nowych.

**Mariusz Piotrzkowski** 33:41  
Nie Jestem pewien, czy do końca działała, które dodawałem nowe wiersze. To jest ten film.

**Damian Kaminski** 33:43  
No dobra, jest jakieś jeden błąd o k. Ale co do zasady działa no.

**Mariusz Piotrzkowski** 33:47  
Bo teraz mi będzie miło.

**Janusz Bossak** 33:48  
Bo uważam, że należy tak samo zrobić.  
Widoku desktopowym, czyli jakby teraz wykorzystać to co jest tutaj.  
I to wykorzystać w widoku desktopowym w takim trybie.  
Jak tutaj mówiliśmy wcześniej, czyli jeżeli tabelka główna.  
Jest formularze owa, to pod tabelka jest z definicji też formularza.

**Mariusz Piotrzkowski** 34:13  
Tylko to też nie jest tak. Sweter jest topowym, bo ty mamy do przewijania, to jest strzałki, lewo prawą, a w desktopowym mamy normalnie paski i też nie wiem czym to się dokładnie różni. Musimy sprawdzić w kodzie.

**Damian Kaminski** 34:19  
No właśnie, ale co ty Janusz masz na myśli, że tak samo, że właśnie ta nawigacja też działa tak jak tu?

**Janusz Bossak** 34:25  
Trzeba sprawdzić znaczy, bo tu.  
No dobrze by było. No skoro to mamy.  
W widoku mobilnym.  
To znaczy.

**Kamil Dubaniowski** 34:39  
Ale tylko w zagnieżdżeniu, no bo ta standardowa nadrzędna powinna być z krolem.

**Janusz Bossak** 34:46  
Standardowa nadrzędna są nie no standardowa, nadrzędna jest osobnymi kafelkami.

**Kamil Dubaniowski** 34:51  
No ale też może dojść do momentu, kiedy ci się nie zmieszczą.

**Damian Kaminski** 34:52  
Nie, ale, ale jak zdasz, Mariusz wróć na to marcową i Dodaj tam jeszcze nad, że tej nadrzędnej 5 kolumn.  
Tu Kamil ma rację, pojawia się skroń, tak jak dodamy.

**Mariusz Piotrzkowski** 35:05  
Po jakiś błąd w ogóle w teraz robi.

**Damian Kaminski** 35:07  
No po prostu są 3. Dodaj teraz przewiń w prawo na tym z królem na dol.

**Mariusz Piotrzkowski** 35:10  
Tyle tylko ze nie, bo błąd się zrobi, musiał odsiedzieć w dół poszło zamiast obok.

**Damian Kaminski** 35:15  
O k.  
I tu Kamil ma rację, że tu jest też z krol.

**Janusz Bossak** 35:22  
Że to jest marcowa, dobrze?  
No to jest o k. Czyli ten.

**Kamil Dubaniowski** 35:32  
Znaczy o tyle ma to sens, że w zagnieżdżeniu mogłyby być strzałki, że chcemy się zmieścić w ramach tej jednej karteczki tak, no bo.

**Janusz Bossak** 35:40  
Nie no desktopowej by to był dziwnie wyglądało całe, a jakby idea przechodzenia na taką formę formularza ową była po to właśnie, żeby jak masz tutaj nie wiem. 4 członków rodziny.  
To, żeby ich zobaczyć w całości, tak?  
Obok.

**Kamil Dubaniowski** 35:55  
Nie, nie, ale mówię podrzędnych nadrzędnej jak najbardziej, skoro żeby właśnie zapełnić cały ekran, no ale dla już zagnieżdżenia jako ekran traktujemy ten jeden pojedynczy.  
Jedną pojedynczą kolumnę.

**Lukasz Bott** 36:07  
I kolumne to.

**Janusz Bossak** 36:07  
Tak.  
Tak, tak, tak, tak, tak, ten tabelka zagniesz żona powinna się zachowywać jak na mobilnym nie czy mieć tylko zagnieżdżone tak.

**Kamil Dubaniowski** 36:13  
Tak, ale tylko za gniewna.

**Janusz Bossak** 36:17  
Czyli tak powinno wyglądać.  
Dla tej głównej tabelki, a dla zagnieżdżony powinno wyglądać jak na mobilnym, czyli to jest z boku mieć takie przewijaki nie.

**Damian Kaminski** 36:30  
Pewnie jakis boku dodawanie wiersza w nagłówku tej osadzonej tak.

**Kamil Dubaniowski** 36:30  
No bo.

**Janusz Bossak** 36:36  
Tak jak jest teraz już w tym nowym projektem, to to.  
Pokaż teraz Jeszcze raz to, ale w nowym wydaniu.

**Damian Kaminski** 36:51  
No i tu pod tym tabby mamy właśnie tą.  
Wewnętrzną.

**Mariusz Piotrzkowski** 36:57  
To znowu coś się gdzie czuję poczty i zniknęły strzałki w ogóle przesuwają się w dół. Nie wiem, te te podpory są bardzo zróżnicowane, te znaczy tebel jako formularz jest dużo błędów.  
Powiem szczerze, nie wiem czy nie byłoby lepiej tego od zera po prostu przerobić, żeby też było zgodne z łódce aggie, bo też był z tym problemem.

**Piotr Buczkowski** 37:12  
Nie.

**Janusz Bossak** 37:16  
Bo to się popsuło przy tym w CAG no.

**Mariusz Piotrzkowski** 37:19  
Znaczy nie, nie tylko przywódca g, bo na stary na mobilnym też z tego co widziałem są takie problemy, no zobacz sobie tutaj, włączę na mobilnym.  
No i zrobię tak, przewijam podrzędne, przewijam, nadrzędny, przewijam podrzędny i znowu się wszystko co się w ogóle stało teraz.

**Janusz Bossak** 37:30  
Przewijakiem tak, bo to jest ten.

**Damian Kaminski** 37:37  
No tak, tylko tam jest te strzałki się na siebie nakładają, jest to jest.

**Mariusz Piotrzkowski** 37:41  
Teraz w ogóle.

**Damian Kaminski** 37:42  
Niepraktyczne mega.

**Mariusz Piotrzkowski** 37:43  
Nie, nie wiadomo teraz, co się dzieje, nie.

**Janusz Bossak** 37:45  
Nie no to trzeba naprawdę.

**Damian Kaminski** 37:46  
Znaczy mamy taki przypadek według mnie, na ekranie, którego nikt realnie nie ma po prostu system na to pozwalał. Nie ograniczyliśmy tego, bo funkcjonalność jest otwarta, ale.  
No nie wiem czy ktoś tak to zaprojektował, no bo.

**Janusz Bossak** 38:01  
Można można, bo to jest nowość, jest dokumentacja. To co dyskutowali tam godzinę temu, jeżeli byśmy napisali, że owszem, na desktopie można sobie zaprojektować tak, że masz tabelkę pod żadną, to nie jest, to wystarczy jedno zdanie dokumentacji. Taka konfiguracja nie jest obsługiwana na widoku mobilnym. Koniec kropka.

**Mariusz Piotrzkowski** 38:26  
Co się teraz stało?

**Janusz Bossak** 38:28  
I temat.

**Damian Kaminski** 38:29  
Masz jakieś puddingi duże?

**Janusz Bossak** 38:33  
I ja bym poszedł w tym kierunku, że na widoku mobilnym nie jest obsługiwana.  
Tabelka zagniesz żona po prostu tylko musi być to w dokumentacji napisane.  
I wtedy tak trzeba proces ułożyć, żeby nie było tabelki zagnieżdżone i tak.

**Damian Kaminski** 38:52  
No.  
Mogą przełączyć się na pod formularze.

**Janusz Bossak** 38:56  
Mogą się na przykład przyłączyć na pot formularz tak i no pot formularzu, proszę bardzo.  
Chociaż nie wiem jak to tutaj to działa też na ten pod formularzem. On niestety słuchajcie, no mamy takie rzeczy.  
To dyskusja jest ciągle nad tym, czy ta elastyczność, którą dajemy, musimy ją bronić za wszelką cenę.  
Czy właśnie nie?  
Nie ciąć, nie ograniczać i mówić owszem, no jest elastyczność na desktopie, to są możesz robić więcej przykład różnych rzeczy.  
Ale jak chcesz to samo mieć na mobilnym no to niestety nie Nie możesz tak sobie przełączyć formula.  
Wiesz, ona któreś teraz prezentacji ostatniej, której byliśmy?  
Gościu się nawet zdziwił trochę, że my mamy tak zrobione, że nie trzeba definiować na nowo formularza dla widoku mobilnego.  
Nie wiem, czy widzieli po prostu inne systemy, gdzie formularz, mimo że tak jak u nas był do definiowania, to trzeba było definiować 2 razy.  
Dla widoku desktopowego i dla widoku mobilnego.  
A u nas się to samo jakby układa dobrze w miarę dobrze tak jak tutaj widać.  
No dobra, słuchajcie.  
Wniosek.  
Jakiś pamięć?

**Lukasz Bott** 40:27  
Znaczy.  
To chyba konkluzja. Konkluzja jest taka jeżeli chodzi o.  
Nowy formularz sprawy to jeżeli ta funkcjonalność mówię o desktopie, tak.  
Jeżeli ta funkcjonalność pod podstawę na mnie działa, no to trzeba ewidentnie naprawić tak no bo.  
Do do zastanowienia się, czy robimy tu właśnie w takim.  
W ten sposób tak, no tryb, a to co powiedziałaś Janusz, jeżeli chodzi o tryb mobilny, dajemy może jako tak właśnie na p. Tak albo nawet docelowo tak dajemy zastrzeżenie w dokumentacji i tyle.  
Żeby się z tego nie doktoryzować, no.

**Damian Kaminski** 41:11  
Znaczy tak marcowa, no działa słabo pytanie jeszcze jakbyśmy się wrócili do grudniowej, czy też ma takie problemy, jeśli ma to według mnie można z góry założyć, że nic z tego nie korzystał, bo by nam zgłaszali, że to jest nieużywane i teraz, jeśli przyjmujemy taką tezę.

**Lukasz Bott** 41:25  
Tak.

**Damian Kaminski** 41:31  
No to możemy po prostu wykastrować coś, że czegoś nie ma, bo to jest nieużywane i tyle.

**Janusz Bossak** 41:37  
Dobrze to jest. Wracając do początku Piotr, to zgłoszenie, które jest to, kto jest robił, to jest od konsultantów. Czy to jest nasze wewnętrzne?

**Piotr Buczkowski** 41:43  
Ja ja.  
Ja testując coś zauważyłem, że mi tabelka zniknęła.

**Janusz Bossak** 41:48  
Trujemy.  
Według mnie konstruujemy znaczy, jeżeli.

**Mariusz Piotrzkowski** 41:54  
Tutaj działa na grudniowe, teraz jest twój.

**Damian Kaminski** 41:55  
No dobra, pokaż, poczekaj, pokaż w formie normalnej nie nie takiej mobilnej.

**Piotr Buczkowski** 42:00  
Założeniem było tylko przywrócenie funkcjonalności z poprzedniej wersji.  
Nie poprawa niecoś tylko że kiedyś działało, teraz nie działa tak.

**Janusz Bossak** 42:09  
Dobra, no to przywrócić funkcjonalność w poprzedniej wersji i koniec i nic więcej nie robimy.

**Mariusz Piotrzkowski** 42:15  
Dobrze spróbuję.

**Damian Kaminski** 42:16  
Nie czekamy na zgłoszenia, no pojawiały się to będziemy obsługiwać, nie pojawiał się to.

**Janusz Bossak** 42:21  
Czyli poszedł w stronę tego kastrowania i nie umożliwiania takich cudów.  
Czyli nie można by ustawić.  
Tabelki pod tabelce w trybie formularza owym i tabelarycznym no i tyle.  
No bo widzicie co się dzieje tak jakaś.  
Totalnie nie.

**Damian Kaminski** 42:44  
Poczekaj, ale teraz powiedziałeś w trybie formularzami tabelarycznym to nie do końca zrozumiałem, że w ogóle nie można pod tabelki ustawić, jeśli mamy tryb formularze owy.

**Janusz Bossak** 42:47  
No.  
Dokładnie.

**Damian Kaminski** 42:56  
O k.

**Mariusz Piotrzkowski** 42:56  
Też byłbym za tym.

**Damian Kaminski** 42:59  
Czyli w zasadzie to, że się teraz nie wyświetla wcale nie jest błędem.

**Janusz Bossak** 43:05  
No jest realizacją trochę taką aneks spekta twitter tego założenia, że w trybie formularz owym tabelki się nie wyświetlają. Jeżeli ktoś chce, to tabelki się wyświetlają w trybie tabel kowym jako pod tabelki i w trybie pod formą.

**Piotr Buczkowski** 43:20  
Dobrze dla ułatwienia możemy zrobić tak, że jeżeli pod tabelka, a tabelka nadrzędna jest w trybie formularzem, to pod tabelka też musi być trybie formularza.

**Janusz Bossak** 43:30  
Jeżeli to coś łatwego.

**Lukasz Bott** 43:30  
Ale co co masz na myśli, musi, w którym momencie?

**Janusz Bossak** 43:33  
Może tak się wyświetli jak teraz.

**Piotr Buczkowski** 43:34  
Wymuszamy nawet na tak się wyświetli, nawet jeżeli to się dostawi inaczej to się to jako podforum jako formularz.

**Lukasz Bott** 43:34  
To tak się wyświetli, tak, nie.

**Damian Kaminski** 43:36  
Tak jak teraz, tak?

**Lukasz Bott** 43:38  
Niezależnie od ustawień.

**Damian Kaminski** 43:44  
Słuchajcie, możemy to wydać do wersji, tak, zróbmy tak, żeby było jakkolwiek się to wyświetlało do grudniowej pytanie, czy ktoś zgłosi baga, a możemy przyjąć założenie, że w wersji grudniowej, którą wydajemy, opisujemy, że zmieniamy sposób wyświetlania tabel w taki sposób jest dokumentacja, będzie miał prezentować, jak ktoś się do tego przyczepi, to to się zgłosi.

**Janusz Bossak** 43:44  
Moż.

**Damian Kaminski** 44:08  
A według mnie nikt się nie zgłosi.  
Bo akurat formy formularze owe są najrzadziej według nieużywane, używanym sposobem wyświetlania tabeli.

**Lukasz Bott** 44:19  
To już naprawdę trzeba wiedzieć, że tak można.

**Janusz Bossak** 44:24  
Ale sądzi według mnie takim papierkiem lakmusowym jest, czy ma zgłoszeń dotyczących.  
Takiego trybu, formularz nowego no nie ma.

**Damian Kaminski** 44:33  
Nie ma dokładnie, no bo bo to jest no niewygodne.

**Janusz Bossak** 44:37  
Czy może nikt tego, że to nie działa za bardzo i konsultanci tak nie konfigurując?  
No tak, ale to też jest.

**Damian Kaminski** 44:45  
Ja jedno wdrożenie miałem, gdzie zastosowałem tryb formularze owy, gdzie trzeba było zgłosić, po prostu był ograniczenie pól, bo jeszcze wtedy było i trzeba było dopisać dużo nowych pól w formie adresów i żeby to wyświetlić na jednym ekranie i tylko i tylko wtedy waderko.  
Ale nie robiłem tam formularza w formularzu, tylko po prostu ten nadrzędna tabela jest układem formularze owym.

**Lukasz Bott** 45:10  
No ja ja raz popełniłem lata temu w błąd spocie jest używany do konfiguracji cennika ze względu na strukturę taką merytoryczną, biznesową tego cennika i tam, ale tam są używane po formularze, tak.

**Janusz Bossak** 45:10  
No tak.  
No właśnie.

**Damian Kaminski** 45:25  
No to pod formularze według mnie są już dużo części używane w hr owych różnych właśnie Zgłoś do ZUS i tak dalej to to to jest akurat, ale o formularze owym. No mi się przez 5 lat zdarzyło raz.

**Lukasz Bott** 45:25  
Więc jak?  
Tak.  
To znaczną.

**Janusz Bossak** 45:35  
Nie, bo.

**Lukasz Bott** 45:36  
Są pod formularze i i formularze owy tryb, ale to wtedy to. No generalnie to działa tak, no.

**Janusz Bossak** 45:37  
Chodzi.  
Wiecie, chodzi mi o to, że mamy funkcjonalność, którą chcemy poświęcić ileś czasu, no bo Mariusz jak się tym zajmie to zużyje. Nie wiem. 2 3, może 5 dni.

**Lukasz Bott** 45:43  
Jeśli cholery jest niewygodny?

**Damian Kaminski** 45:55  
Nie chcę go nie korzysta.

**Janusz Bossak** 45:57  
Ja ani nikt z tego nie korzysta, więc może lepiej poświęcić 5 dni pracy Mariusza no bardziej ciekawe zajęcia niż robienie rzeczy, których nikt nie korzysta, nie.  
O to mi chodzi.

**Damian Kaminski** 46:10  
No dobrze, to jaka jest konkluzja, czyli możemy wrócić do stanu takiego, żeby po prostu się to wyświetlało? Jakkolwiek tak jak jest najłatwiej to wyświetlić. Niezależnie czy w formularzu owo czy tabelarycznym już bym od tego w ogóle abstra chował i napisać, że wersji grudniowej nie wspieramy w wersji formularza owej.  
W ogóle tabel na przykład.

**Janusz Bossak** 46:33  
Nigdy nie wspieraliśmy.

**Lukasz Bott** 46:36  
Znaczy pod tabeli.

**Damian Kaminski** 46:38  
Pod tabel tak w sensie?

**Janusz Bossak** 46:39  
Tak, zróbmy dobry.  
No Piotr, rozumiem, że przywrócenie jakby działania starego jest łatwe, tak.

**Piotr Buczkowski** 46:46  
Nie wiem.

**Janusz Bossak** 46:47  
Nie wiesz.

**Mariusz Piotrzkowski** 46:47  
Zmienił się mocno kod.

**Piotr Buczkowski** 46:48  
Myślałem, myślałem, że jest łatwe.

**Mariusz Piotrzkowski** 46:50  
Zmienił się mocno kod, bo był przerabiany, przerabiany był wygląd tych formularzy, bo jak widać na przykład na grudniowej mamy tutaj jak po prostu label, a w tym nowym już jest pokazują.  
A w tym nowym jest po lewej stronie są tyle belki, wszystkie podpisy i się mocno zmienił. Układ mocno się zmienił, kod nie widziałem kto dokładnie robił chyba tylko osób różnych to robiło i może dlatego jest taki bałagan. No i powiem szczerze, że się zmieniło na tyle dużo, że jak sobie porównałem 2 pliki jeden do jednego to nie wiedziałem co jest czym i dlatego mi zajęło tyle czasu w ogóle, żeby to ogarnąć jak to działa też 6 czy 7 godzin, jak wczoraj to robiłem.  
Plus jeszcze dzisiaj także.  
Nie wiem czy przewrócenie jeden jeden do jednego będzie takie proste, biorąc pod uwagę, że mamy inny trochę wygląd, inny inny sposób renderowania.

**Janusz Bossak** 47:42  
Zróbmy tak Mariusz i Piotr, jeden dzień macie na taki próg of Concept, czyli czy da się to zrobić szybko i łatwo czy nie?  
I w czwartek na Radzie przedyskutujemy dalsze kroki. Nawet niecały jeden dzień tak poświęcicie na to.  
Dobra.

**Mariusz Piotrzkowski** 48:06  
Ja bym nad tym kombinował cały czas dzisiaj.

**Janusz Bossak** 48:08  
Ale też, żebyś tam nie nie za dużo, nie tylko masz wiedzieć czy to jest proste czy nie proste.

**Mariusz Piotrzkowski** 48:15  
Trochę jeszcze pokombinuję i zobaczę co wg mnie właśnie teraz próbuję z czatem GP, może mi coś podpowie z tym autem.

**Janusz Bossak** 48:20  
Dobra.  
O k.  
No to tyle czy mamy jeszcze jakieś tematy narady?

**Piotr Buczkowski** 48:27  
I ja mam uwagę do osób, które tam to część reaktor owo tak planują, czy.  
Nadzorują.  
Sprawdzajcie jakie są wywołania, bo w vlogach vlog ever znów jest pobieranie wszystkich użytkowników przez wejścia przy wejściu na lodowcu 200. Jakieś menu, z którego najpewniej nikt nie skorzysta.

**Damian Kaminski** 48:52  
Myślę, że można.

**Piotr Buczkowski** 48:52  
To co było to jest to, że formularze z pobierane wszystkie pozycje słownika, wszyscy użytkownicy, wszystkie słowniki w przypadku najpewniej nikt z tego nie skorzysta.  
Nie wiem i.

**Damian Kaminski** 49:07  
Za wcześnie po prostu tak, dopiero jeśli jest taka.

**Piotr Buczkowski** 49:09  
Tak, nie, nie wiem, nie wiem jak to pilnować, kto ma tego pilnować jak nie wiem.

**Damian Kaminski** 49:19  
Dobra, no niech kamień porozmawia przede wszystkim z chłopakami, no niech oni sami się pilnują.  
Yy, ale no rozumiem, że walidacja na drugą parę oczu jest.

**Piotr Buczkowski** 49:28  
No znaczy, no bo wczoraj coś tam wystrasze błąd starym widoku lover.

**Damian Kaminski** 49:29  
Pewnie potrzebna.

**Piotr Buczkowski** 49:36  
Jedna rzecz tam poprawiałem, no bo ze sprawie jeszcze do starego widoku podpięcie tak to patrzę, a tutaj pobieramy wszystkich użytkowników. Czy wejście na ten nowy look wziąłeś?  
No.  
Po co po co? Jak niepotrzebne jest najpewniej?  
Jeżeli ktoś chce roz jeżeli ktoś rozwinie filtr lista użytkowników, żeby wybrać pis tylko nagłe, szybko wnika to wtedy tak, ale też nie wszystkich.

**Damian Kaminski** 49:56  
Kamila, ogarniesz to.

**Piotr Buczkowski** 50:06  
Wreszcie jest 200000 użytkowników.

**Damian Kaminski** 50:11  
No nie mają tej perspektywy. No dobrze, że Piotr o tym mówisz, tylko trzeba z chłopakami pogadać, bo oni to testują na właśnie nie spotkali się z takim przypadkiem i bagatelizują może.

**Kamil Dubaniowski** 50:25  
Ja zarostu Filipa się odezwa.

**Piotr Buczkowski** 50:30  
No to to przypadek właśnie z użytkownikami i do logu i do edytora uprawnień do pola czytam te sekcje to, że to, że formularzy.  
Też nie też powinno być dopiero jak to się otworzy, będzie chciał wybrać jakieś użytkownika.  
Tak.  
I to już jakoś stronicowania.  
Czy tam wyszukiwanie tak.

**Kamil Dubaniowski** 50:54  
Mhm.  
Mm wtedy to, że graficznym też tak jest u przemka.

**Piotr Buczkowski** 51:01  
Tak tak, to już jeżeli wejdziesz, jeżeli wejdziesz to ustawienie pola, nieważne czy nawet nawet nie dotkniesz matryc, decyzji uprawnień, to i tak ci pobiera wszystkich użytkowników.

**Kamil Dubaniowski** 51:02  
I matrycą prawną pewnie też.  
Dobra, to jest jak się dogadam.  
Dobra, to ja miałbym jeszcze jeden temat. Właściwie Mariusza też dotyczy zgłosiłem.  
Klient zgłosił baga.  
Nauka konkretnie mówiąc, że w nowej wersji nie można oznaczać. No i faktycznie tak jest, tylko, że to wynika z ustawień procesu, że jest wyłączone dvd i dodawanie do DI do kontry obu torów.

**Piotr Buczkowski** 51:46  
No tak i to.

**Kamil Dubaniowski** 51:47  
Tak i tak było, więc to nie jest błąd, tylko teraz.  
Czy to jest prawidłowe działanie? No bo wyłączamy dodawanie do DWI. To skutkuje wyłączenie możliwości oznaczania się w komentarzach. Natomiast no jest 50 osób, które mają dostęp do tej sprawy, mają uprawnienia i ja ich nie mogę oznaczyć.  
Bo wyłączyłem możliwość dodawania do 2.  
Nowych nie mogę dodawać, ale Dlaczego nie mogę oznaczyć tych 50, które mają uprawnienia?

**Janusz Bossak** 52:20  
No tych powinno się dać. Dlaczego?

**Kamil Dubaniowski** 52:21  
No właśnie no właśnie i to chcieliśmy potwierdzić, no bo tak to jakby wymaga zmiany całkowicie tej logiki. Aktualnie jest bardzo prosto, nie da się oznaczać nowych, to nie da się oznaczać też obecny.

**Janusz Bossak** 52:34  
Nie, nie, nie, nie, nie, nie do wszystkich, którzy mają w danym momencie prawo do tej sprawy, mogę to ich wskazać tutaj wymiankowa dom i Dlaczego nie?  
To znaczy, ja takie miałem od początku jakby w głowie, że to tak działa. Wyłączenie 2 oznacza tylko, że nie mogę dodawać nowych do raczej spoza tej sprawy.

**Kamil Dubaniowski** 52:47  
To masz.

**Damian Kaminski** 52:47  
Te dysku.

**Kamil Dubaniowski** 52:56  
No to tak tak.  
Tak też to odebrałem jak zacząłem jakby te testy, ale tak nie jest w ogóle jest teraz tak, że jak masz?  
Wyłączone de www.ale włączonych kontry obu torów.  
No to mimo wszystko możesz tagować możesz oznaczać kogokolwiek, jest wyłączona kontakt trybu, ktorzy wyłączeni i w drugą stronę nie pamiętam jakie jest zachowanie, że jak masz włączonych kontrybucji też się nam tak. No czyli tak naprawdę to jest zależne od jednego z, natomiast mi się wydaje, że powinniśmy przejść już czysto nad w tak, czyli DW ogóle zmieniłbym nazwę tego ustawienia w ustawieniach procesu, że to jest DIW zmian kowanie.

**Mariusz Piotrzkowski** 53:26  
Też się do.

**Kamil Dubaniowski** 53:45  
Żeby to było jednoznaczne, że to do tego służy. No i wyłączenie de w i w zmian kowania po prostu po pierwsze blokuje możliwość dodawania nowych DWW tym panelu uprawnień no i zmian kowania nowych.

**Janusz Bossak** 54:01  
To już jak tak to już idźmy szerzej i dodajmy oprócz devo.  
Jeszcze czek boks, że można w wymiankowa znać czy tam chodzi mi o to, że.  
Żeby używanie devo nie było.  
Nie dotyczyła wzmiankowanym tak taką zmian kowanie byłoby osobną opcję, że w tej sprawie.

**Damian Kaminski** 54:21  
Znaczy, dyskutowaliśmy na ten temat, może przypomnę gdzieś miesiąc temu.  
W kontekście też maili.  
I wtedy padł jeszcze taki pomysł, że może oprócz 2 powinna być jeszcze jakaś rola.  
Po prostu samego odczytu, bo dzisiaj de wód to jest to są też powiadomienia o o zmianie stanu i tak dalej.  
To też zgłoszenie u mnie wisi, to trzeba było razem zaopiekować, czyli to tak jak proponuję teraz Janusz tak, czyli że można wzmiankowana wać.  
Mimo, że nie można zdefiniować na debiut, tak.

**Kamil Dubaniowski** 54:58  
Czy to to jest też nomenklatura? No my to mamy tak naprawdę 3 nazwy na jedno to są obserwatorzy, no to to, że są obserwatorami, dostałem powiadomienia, no to jest jak najbardziej zgodne z nazwą obcych bakterii. Obserwujesz sprawę?

**Damian Kaminski** 55:09  
Ale obserwacja no tak, ale obserwator można go nazwać w takim aktywnym, czyli dostaje właśnie te powiadomienia o fordzie na przykład tak. A jak ty kogoś wywołujesz w kontekście komentarza, to chcę, żeby on teraz tu podjął jakieś działania albo się z czymś zapoznał, a on nie musi wiedzieć, że ta sprawa przeszła do kolejnej osoby i tak dalej, więc.  
To nie jest tożsame z 2.

**Janusz Bossak** 55:33  
No ale technicznie jak to jest teraz, jeżeli kogoś wzmiankuje, to on jest fizycznie dodawany do DW.  
Czyli od momentu, kiedy go wzmiankowanym w tej sprawie dostaje informację, że sprawa przeszła na kolejny etap, że Dodano, nie wiem, plik jakiś, no tej sprawy, że normalnie tak jakby był w.

**Kamil Dubaniowski** 55:55  
Tak tylko najlepsze jest to, że w momencie, kiedy go wzmiankuje, on jeszcze nie ma uprawnień, nie dostaje powiadomienia, że został dodany do do, że został dodany komentarz dopiero kolejne zmiany do niego teraz.

**Janusz Bossak** 55:56  
No właśnie.  
Takie zgłoszenie i też było naprawiane chyba czy nie?

**Kamil Dubaniowski** 56:10  
No nie wiem, ja teraz je przypisałem dopiero.  
I przetestowałem faktycznie tak jest, że dopiero drugie akcja.  
Na sprawie dochodzą do osoby wzmiankowanej.  
Czyli jak ktoś mnie wzmiankuje to nie wiem jak.

**Janusz Bossak** 56:24  
Że tak było, że to już podjęliśmy, bo to dosyć takie było.

**Kamil Dubaniowski** 56:28  
Nie, nie do tej pory do tej pory nie ma, nie ma jakby mailowego powiadomienia, że zostałeś wzmiankowany. Ja wręcz tam rozpisałem zadanie na to, żeby był dedykowany mail inny od tego, że zostałeś dodany do, że znaczy, że został dodany komentarz.  
Bo teraz jak bycie ktoś wzmiankowano pierwszy raz nie dostaniesz maila, wzmiankuje się drugi raz to dostajesz maila, że został dodany nowy komentarz.  
A nie, że ktoś cię w wymiankowo w ogóle nie mamy takiego powiadomienia.

**Janusz Bossak** 56:52  
Czyli.  
Wszystkie te rzeczy tylko miło potwierdzają, że powinniśmy mieć opisy tych funkcjonalności.  
Bo sami o tym dyskutujemy tak i sobie przypominamy za każdym razem.  
A powinniśmy zaglądać do instrukcji?  
Opis tam systemów zmian kowania i tam powinno być wszystko, to to, co teraz powiedzieliśmy opisane.  
Dobra, ale wracając, bo już muszę iść na spotkanie, za rządowe powinno działać. Według mnie jest moja opinia, tak w ten sposób, że to wzmiankowana nie tutaj.  
Yy, wśród osób, które już mają dostęp do sprawy, powinno być absolutnie oczywiste.  
I to jest taka zmiana na teraz, jak to rozdzielanie ról przed dw i jeszcze jakieś miarkowanie to jest osobny temat, tak tu powinno być tak, że jeżeli.  
To 2 jest wyłączone, to i tak i tak mogę w wymiankowa do osób, które są ze sprawy i tyle tak powinno brzmieć poprawka do tego.  
Co tu jest na ekranie?  
Dobra, ja muszę uciekać, muszę jeszcze do.

**Damian Kaminski** 58:05  
Też muszę się przełączyć.

**Janusz Bossak** 58:07  
No 2 minuty.

**Kamil Dubaniowski** 58:08  
Ale też zmieniamy przy okazji tego, że tylko ustawienie DW steruje wzmiankowanym to kon kon trybu torów od tego odcinamy.

**Janusz Bossak** 58:17  
Odcinamy no był kontry butor to jest poważniejszy temat tak o co o ten.

**Kamil Dubaniowski** 58:20  
O k zgadzam się.  
No to Mariusz, masz trudniejszą ścieżkę.

**Damian Kaminski** 58:26  
No to nie da rady na ten sprint to od razu trzeba by przepiąć bo to to co Mariusz mu że się nie wyrobi.

**Mariusz Piotrzkowski** 58:27  
No to już.  
Tak właśnie chciałam to powiedzieć, bo już jeszcze ten błąd teraz plus jeszcze inne rzeczy, które mam to już nie ma szansy muszą co najmniej co najmniej jest 10 fortelu, 15 zwolnić już w tym 50.

**Kamil Dubaniowski** 58:37  
Dobra.  
To tylko przerób może forty właśnie pod tym kątem, żebym wiedział co co zabierać.

**Janusz Bossak** 58:44  
Dobra na razie.

**Mariusz Piotrzkowski** 58:45  
Jeśli mogę wysłać listy rzeczy, które najchętniej bym komuś oddał, bowiem, że to się inaczej, to i ktoś inny to zrobi szybciej.

**Kamil Dubaniowski** 58:50  
Tam już 2 dostałem od ciebie, no to wiem, a jak masz coś jeszcze to podrzucę.

**Mariusz Piotrzkowski** 58:53  
Pewnie coś się jeszcze będzie jak teraz ta pszczółka być.

**Damian Kaminski** 58:57  
Kamila jeszcze ci podesłałem powiązane z tym temat, no ale to.

**Lukasz Bott** 58:57  
To jeśli.

**Damian Kaminski** 59:01  
Myślę, że to trzeba na design przełożyć i zaplanować globalnie.

**Lukasz Bott** 59:09  
Marek, jeszcze słuchajcie, Marek zgłasza tam coś z tym blockchainem, ale to rozumiem. Marek jest grubsza sprawa.

**Marek Dziakowski** 59:14  
Tak no no trzeba ustalić prostu jak tam, jak to robimy, jak chcemy to robić, nawet potrzebny jest janosz.

**Lukasz Bott** 59:21  
Dobra.

**Marek Dziakowski** 59:21  
Bo to ostrzegam, że z kosztami po prostu.

**Damian Kaminski** 59:24  
O k no to na czwartek.  
Chyba, że ale to jest jakoś krytyczne, terminowo też.

**Lukasz Bott** 59:29  
Ale to to to.

**Damian Kaminski** 59:36  
W sensie, że trzeba podjąć decyzję niezwłocznie.

**Marek Dziakowski** 59:38  
Nie trzeba to moim zdaniem zrobić miarę szybko, ale niekoniecznie musi być to już podjęte dzisiaj.

**Lukasz Bott** 59:46  
To Marek może w podobny sposób? Jeżeli masz to przemyślane technicznie, co tam trzeba zrobić? Tak czy ten? No to bądź z tym przemyśleniem może nie wiem, skonsultuj tutaj z kolegami tak i po prostu na czwartkowo rady tak postulat.

**Marek Dziakowski** 59:52  
Mhm.  
Mam cały dokument przygotowany w razie co to też mogę.

**Lukasz Bott** 1:00:04  
Okej, dobra, no po prostu to spoko.

**Marek Dziakowski** 1:00:07  
No no to w czwartek po prostu przygotowano o k. Dzięki.

**Lukasz Bott** 1:00:09  
Dobra w czwartek.  
Cześć.

**Janusz Bossak** zatrzymano transkrypcję
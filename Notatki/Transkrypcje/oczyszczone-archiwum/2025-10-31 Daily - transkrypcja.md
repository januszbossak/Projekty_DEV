**Data spotkania:** 31 października 2025, 08:20

---

**Marek Dziakowski:** Cześć.

**Mariusz Piotrzkowski:** Cześć.

**Damian Kaminski:** Cześć.

**Anna Skupinska:** Cześć.

**Adrian Kotowski:** Cześć.

**Janusz Bossak:** No hejka, przepraszam ale się zagadałem z kolegą tutaj. Już wszystko pokazuje ciech. Gotowy? Dobrze, testerki. Pozdrawiam, cześć.

**Oktawia Ostrowska:** Ja chciałabym dokończyć dzisiaj swoje zadania większości zryli z testów. Blokerów żadnych nie mam. Barbara kolejna.

**Barbara Michalek:** Cześć, jeśli chodzi o mnie, to wczoraj 5-6 zadań na dan, jeden jedno zgłoszenie do Mateusza, jeden pas, internal testy jedno tam blokuje nikt do Marka, a dzisiaj chcę jak najwięcej listów na koniec sprintu. Dzięki, ja.

**Patrycja Walaszczyk:** Cześć. Ja dzisiaj dokończę realist test i w poniedziałek mnie nie mogą urlop i blokerów nie mam chyba Michał następny, dzięki.

**Janusz Bossak:** Chyba dzisiaj wziął urlop, coś mi się wydaje.

**Patrycja Walaszczyk:** A tak mówił.

**Janusz Bossak:** Dobrze, no to deweloperzy. Filip pierwszy.

**Filip Liwiński:** Cześć, no to mnie zadanka z listy to Rafał malarza i dzisiaj też tam kontynuacja to to co mi zostało. I Piotr kolejny.

**Piotr Buczkowski:** Już się nie da końcu. Brak. Wczoraj zajmowałem się. Takim mechanizmem ułatwiającym testowanie wczytywania maili. Yy, czy tam prasowania ML, czyli można z poziomu procesu teraz wczytać plik EML testowy? Jest to wiele łatwiej. Przy okazji był błąd jaki zgłoszony z PA. No nie powiem tak, no tak. Ale tak kiepsko opisane, że nie wiadomo. Czy wystąpił czy nie ten błąd? Dobrze, poza tym dużo było jakieś tam konsultacji, tak z konsultantami tam. Indeks w Rossmanie właśnie wczytywanie poszukiwanie straconego maila. Z własną czy coś takiego? Dzisiaj może zajmę się tym w końcu co miałam wczoraj, czyli działa. W środowisku z wieloma wantę nie zaufam nie zaufanymi.

**Damian Kaminski:** A w Zimbra ta udało się tam to też rozwiązać. Tu pula aplikacji.

**Piotr Buczkowski:** Co znaczy udało się pominąć problem, ale trzeba go rozwiązać. To jak napisałem, że to, że wyłączyli wymaganie SSL, to nie znaczy, że SSL nie warto korzystać.

**Damian Kaminski:** OK.

**Piotr Buczkowski:** Może warto to skonfigurować? Oczywiście pytanie, kto to będzie potrafił zrobić.

**Damian Kaminski:** No właśnie, może konsekwencją tego nowego web config, a powinny być jakieś minimalne zalecenie jak zrobić jakiś taki certyfikat lokalny.

**Piotr Buczkowski:** Znaczy to jest nowsza biblioteka majewską.

**Damian Kaminski:** Ona była przyczyną tak, rozumiem, tylko zmierzam do tego, że powiedzmy, jeśli klient nas w tym nie wspiera, to żeby dało się to zrobić, bo pewnie da się to rozwiązać jakoś samodzielnie, tak jakimś takim własnym certyfikatem.

**Piotr Buczkowski:** To jest podział. Tak, tak. Znaczy no trzeba trzeba skądś kurować moje skóry. Po prostu. Po prostu działa. Nie wiem do czego tam nie działa, tak?

**Damian Kaminski:** No dobra, wrócimy do tego najwyżej. Tego co powiedziałeś, to nie zrozumiałem, ale nie chcę tu zajmować czasu teraz.

**Janusz Bossak:** W tym jeszcze nawiązując tego wasko, no skąd się to wzięło? Tak? No, bo Przemek był tam na spotkaniu takim menedżerskim. I oni już generalnie chcieli odejść od nas, bo uznali, że naszą cerę nie działa i że nie potrafimy rozwiązać różnych problemów, które oni zgłaszają od pół roku i między innymi właśnie był problem. Z tymi mailami nie, że oni chcieli wiedzieć, które maile się nie czytały. I to jest główny problem tak, żeby było.

**Piotr Buczkowski:** Krocie to ten mail nie mogłem znaleźć, żeby to dotarło do nas.

**Janusz Bossak:** Znaczy, mówię o jaki tam jest główny problem, tak ich głównym problemem było to, że z całego strumienia maili, które wpadają do AMODIT, niektóre się nie zaczytują. Oni chcą wiedzieć, które z nich decydują.

**Piotr Buczkowski:** Jest jej.

**Damian Kaminski:** Może spam?

**Piotr Buczkowski:** Jest jest mechanizm powiadomienia o tym, które maile jest, przy których mailach był błąd.

**Janusz Bossak:** O to jest co innego. Bo to już oznacza, że ten mail był i był błąd. Chodzi, które w ogóle nie weszły.

**Piotr Buczkowski:** Jak mam powiadomić, o czym, że nie dostaliśmy maila?

**Janusz Bossak:** Nie wiem, no trzeba się temu przyjrzeć, no nie odpowiadać tak, że tak powiem pobieżnie tylko rozwiązać problem klienta, albo mu to bardzo wyraźnie wytłumaczyć, że to jest sprawa. Nie wiem serwera pocztowego albo cokolwiek innego.

**Piotr Buczkowski:** Po pierwsze z wykorzystują produkcji nie testowy serwer pocztowy, który mi nikt, którego nikt nie kontroluje, nikt nie ma żadnego monitorowania i.

**Janusz Bossak:** No to. No to trzeba takiej właśnie rozmowy z niej poprowadzić, żeby to były merytoryczne rozmowy mówiące o tym, jak należy problem rozwiązać i nie znaczy ja nie mam pretensji do ciebie żadnej, tak, tylko bardziej tutaj trochę do opieszałości naszego serwisu. Właśnie, że tak po łebkach, jakby traktował klienta i efekt jest taki, że klient powiedział, że idzie do innego do konkurencji. O to chodzi. Żeby nie umiemy rozwiązywać problemu klientem.

**Damian Kaminski:** Problem.

**Janusz Bossak:** Nie ma komunikacji odpowiedniej, nikt się nie interesował tym klientem za bardzo tylko tak coś tam zrobiliśmy i uznaliśmy, że jest OK. Klientach raz drugi się tam dopytywał i w końcu stwierdził, że tam mam w nosie, jej przestaje się nas pytać i no nic nam nie mówiąc już wybrał inny system już jest właściwie w momencie podpisywania szczęście, że Przemek tam pojechał. Może uda się odwrócić sytuację i klient zostanie u nas. No ale takie czynności musimy wykonać, żeby właśnie pokazać, że jednak się interesujemy problemem klientom.

**Damian Kaminski:** No tak, tylko to jest działanie na poziomie menedżerskim, no to nasz dział nie ma na to bezpośredniego wpływu. Tak, w sensie to już.

**Janusz Bossak:** No ma w tym sensie, że to właśnie jakiej też odpowiedzi udzieli Piotr, na przykład wpłynie na na coś się tutaj Jestem wpłynie na to, jakie jakie?

**Piotr Buczkowski:** Mimo to, no to straciliśmy klienta, bo bo za późno to zostało zgłoszone, żeby cokolwiek mu zrobić.

**Janusz Bossak:** No to jeszcze nie straciliśmy. Oni powiedzieli, że jeszcze w takim razie nie podejmą tej decyzji o odejściu, tak tylko chcą się od nas tam paru rzeczy dowiedzieć, więc warto ten problem rozwiązać. No zachowania klienta to jest tam 50 czy 60000 rocznie. Oni nam przynoszą, więc to jest klient już znaczący, tak? Bo kupuje różne ten Mateusz jesteś. Nie widzę wszystkich was nie ma Mateusza dobra, bo z Mateuszem jest do obgadania. Z kolei temat tego Google owego o CRA, bo oni tam podobno testowali ten googlowy o CR jest o niebo lepszy od tego naszego Azure. Ale to musimy zbadać, dobra, ale jedźmy dalej. Mariusz.

**Mariusz Piotrzkowski:** Cześć, tak powiem się w okienkach, dobra?

**Janusz Bossak:** Jestem.

**Mariusz Piotrzkowski:** Wczoraj kombinowałem z 2 rzeczami na interfejsie i obie na razie mi powiększenie średniej. Do mnie mogę dojść do porozumienia z kodem pieszo. To jest logika na belce wyświetlania, logika na wyświetlenia reguły na belce i to już od dłuższego czasu tam kombinuje z tym drugie to drobna załącznika, no i sam sobie jest taki problem, że tak jest dużo takich rzeczy jak po prostu układanie elementów i to strasznie źle idzie, kombinuje i z Copilot i bez będę cię dalej kontynuować. W sumie tyle.

**Anna Skupinska:** Jeśli chodzi o mnie, to wczoraj pracowałam nad hotfixem i udało mu się go rozwiązać. To jest ten tego problemu, że siedzisz na nim cały dzień i zmieniasz jedną linijkę w kodzie, żeby się coś poprawiło i myślę, że będę go dzisiaj wgrywać i chciałabym się też dzisiaj zająć. Yy. W ewentualnymi fail testami i mediami, które są do zrobienia przed koniec sprintu.

**Janusz Bossak:** Dobrze.

**Anna Skupinska:** Adrian Kotowski.

**Adrian Kotowski:** Cześć, ja pracowałem trochę, pracowałem trochę.

**Barbara Michalek:** Czy była jasność to, co dzisiaj czekaj? A jak coś dzisiaj wejdzie na internal test to już jest za późno to żebyście mieli na tego świadomość, że jak dzisiaj coś wchodzi no to my już mamy zadania na dzisiaj przepisane na listę. Tak więc ostatniego dnia jak ktoś nam wrzuci na ten no to my i tak tego nie będzie robić.

**Janusz Bossak:** Będziemy o tym rozmawiać. To jest oczywiste, dobra, Adrian.

**Adrian Kotowski:** Dobra, to chciałem się tak, jeśli chodzi o mnie, to wczoraj pracowałem nad tym korektorem, że rozszerzenie tej integracji to te nowe elementy, ale finalnie też wyszło, że ten ten temat błędy w nadawcy eskalowała i musiałem się tym zająć. Tam zrobiłem parę testów integracyjnych tam, żeby to jakoś odwzorować ten problem, znaczy problem jest generalnie z formatem dat tam usługa, jej witryna, jakby inne formaty generują, więc jakby dzisiaj, ponieważ poprawki przygotuje do tego jeszcze trochę, to jest zweryfikuje. W każdym razie też problem ministra się porażki stronie niż po stronie Poczty Polskiej. No i dzisiaj to postaram się to jakoś ogarnąć i jeszcze będę dalej kontynuować ten temat tego tej integracji, troszeczkę integracji z korektorem też czekamy jeszcze też na dostępy do środowiska testowego, co Marhaba też miałem spotkanie i z dzisiaj powinno to do końca dnia dojść i to tyle jeśli chodzi o mnie oddaje głos Marek.

**Marek Dziakowski:** Ja wczoraj kilka konsultacji miałem też tam z Kamilem taką krótką wycenę nośnie TrustCenter. Poza tym kontynuowałem pracę nad blockchainem wydzieliłem to już do usługi windowsowej dzisiaj to będę testował lokalnie, jeszcze czy wszystko jest OK jak dobrze pójdzie w przyszłym tygodniu idzie to na na testa na na demo no i tam w dalszej konsekwencji na produkcję. A no dzisiaj jeszcze do zgłoszenia, którym mówiła Basia, to zaraz sprawdzę co tam, co tam się stało i jeszcze dzisiaj chciałbym o piętnastej wyjść. Z takich rzeczy, jako że jest koniec miesiąca, to w sumie można się pochwalić, że w tym miesiącu TrustCenter podjęło jakiś rekord naprawdę. Eee od kiedy istnieje, bo w zasadzie jest duża szansa, że w tym miesiącu przejdzie jakieś 90000 dokumentów przez TrustCenter, gdzie dla porównania na przykład w roku dwudziestym trzecim, czyli mam zaledwie 2 lata temu, no przeszło przez cały rok 150000. A w tamtym roku było 200 przez cały rok, a tutaj mamy 90 przez jeden miesiąc gigantyczny. Przez. To wszystko tym.

**Janusz Bossak:** No to super no.

**Damian Kaminski:** Bardzo ładnie.

**Marek Dziakowski:** Nie wiem, nie wiem kto jest kolejnego znikł.

**Janusz Bossak:** No może zniknąć a nie wiem to jest team psy to jakaś główna masakra jest po prostu.

**Mariusz Piotrzkowski:** Na awf.

**Janusz Bossak:** Marek był Przemek Rogaś.

**Filip Liwiński:** Siemka dzisiaj nie ma.

**Janusz Bossak:** Mateusz też nie ma. Dobrze. Koledzy. Kamil, Damian, jakieś tematy dla. Zespołu.

**Damian Kaminski:** Ee, to znaczy tak co do ani to przypominam. Tam jak mówisz jakieś faili istotne to OK, nie nie podważam tego, przypominam o tym błędzie jest kulowym z raportami. Ee do briana. Jeszcze pytanie z podsumowania tego, co mówiłeś, jeśli chodzi o ten KSeF Connector czy tam wszystko jest jasne w kontekście tych zadań, czy na pewno wszystko wiesz, jaki jest cel, czy tam konsultowałeś to z maćkiem? Czy potrzebne są jakieś spotkania?

**Adrian Kotowski:** Znaczy, miałem przyniesie konsultacji, ale tam nie ma jakichś takich. No dużych nos się ustaleń prostu ma być to, co jest już, no ten nawet drobny ten poprawki. Nie wiem, nawet point to będzie oni po naszej stronie i tam się dostosuje, bo i tak oni będą musieli to później dorobić ten nowy instancje tego korektora jesteście tutaj i po ich stronie, bo mamy AMODIT Connector oni mają korektor po prostu.

**Damian Kaminski:** OK. Czyli nie potrzebuję żadnych konsultacji, wszystko co tam ci przekazałem, jest jasne i i i nie nie zmieniają się założenia względem tego, co my ustalaliśmy tak po jakieś konsultacje z maćkiem.

**Adrian Kotowski:** Tak. No jest w porządku, tak? Jeszcze musisz z piotrkiem się na konsultował tam w sprawie tych butów, ale to tam raczej już w którym wewnętrznie.

**Damian Kaminski:** No dobrze.

**Janusz Bossak:** Kamil. Jak nie ma?

**Kamil Dubaniowski:** Nie z mojej strony nie będziemy dzisiaj pewnie się z wami kontaktować w kontekście już przyszłego sprintu. Staramy się wyznaczyć jakieś cele powiązane z taką roadmapą, żeby przynajmniej jeden cel na sprint. Każdy taki miał roadmapowy, ale to to będziemy tak średnia pewnie się odzywać. Tam już wczoraj zacząłem kilka czatów z wami, ale to jeszcze nie ze wszystkimi.

**Janusz Bossak:** No no.

**Damian Kaminski:** Dobrze może jeszcze pytań, no o ten estimating tak czy te spotkanie? Kiedy odbywają się te spotkania i czy ktoś to robi? W ogóle.

**Marek Dziakowski:** Ustaliliśmy jakiś czas temu, że nie robimy tylko każdy dostaje tak zgłoszenia z odpowiednim statusem i sam to.

**Kamil Dubaniowski:** Takie jest jak jak jest już takie do do właściwie zdecydowane, że wiem, że daje komuś. Natomiast są też takie gdzie. Są słuszne, nie planujemy ich na już ja oznaczam wtedy jest mating, ale nie przypisuję imiennie do nikogo, no bo myślałem, że jednak te te piątkowe tam będziecie utrzymywać, ale to jest tylko w kontekście tego statusu, gdzie nie ma przypisanej osoby, tylko te by mi zależało, żeby szacować wtedy, czy jest mating bez przypisanej osoby.

**Damian Kaminski:** Znaczy, słuchajcie, jest tego 30, z czego na przyszły sprint? Powiedzmy z 10 na ten sprint jeszcze widzę, że jako estima miting jest nie po.

**Mariusz Piotrzkowski:** Czyli.

**Marek Dziakowski:** I.

**Kamil Dubaniowski:** Ale Tomasz no myśli, że jest osoba przypisana czy nie przypisana, bo mi chodzi tylko o ten nieprzypisane.

**Damian Kaminski:** Właśnie muszę zobaczyć kolumny sekundę.

**Kamil Dubaniowski:** Jak jest niepisana to to ewentualnie możecie robić jakoś tam, że nie wiem dyżurami tak, że ktoś bierze na ten sprint nawet to może być jedną osobę, bo tego nie jest dużo, a po prostu no nie chciałem jej nikomu imiennie tego przepisywać, bo jest niepowiązane z nikim nie jest tematyczne, nikt tego nie robił czy coś w tym stylu.

**Mariusz Piotrzkowski:** Czyli sobie zmienić na dół jak już sobie oszacuje.

**Kamil Dubaniowski:** Tak jak jest oszacowany kredytu.

**Mariusz Piotrzkowski:** A OK dobra?

**Damian Kaminski:** Jak się nazywa ta kolumna z właścicielem?

**Kamil Dubaniowski:** Czasem tu.

**Damian Kaminski:** Ktoś mi podpowie? Już mówię, ile jest takich, które nie mają przypisanego. No pewnie 20 mniej więcej.

**Janusz Bossak:** Słuchajcie, no trzeba to zaraz będziemy mieli spotkanie, to sprintowe, więc możemy. Wciągać poszczególne osoby i postarać się oszacować. Ja mam tylko jeden temat. Według mnie hotfix tak wersja 109 nie działają w ogóle, grupowanie po folderach cokolwiek tutaj wybiorę. Chciałem wczoraj sobie coś tam zrobić, nic się nie dzieje, tak mogę sobie wybierać cokolwiek i nie ma folderów, zniknęły kompletnie.

**Damian Kaminski:** To wczoraj był update.

**Janusz Bossak:** Nie wiem, no ja to wczoraj wykryłem tak no.

**Damian Kaminski:** Michał.

**Kamil Dubaniowski:** Nie już jest 100 szesnasta wersja. Także wątpię, że wczorajszy.

**Damian Kaminski:** Nie, ale chwilę, bo ja mam tą samą u siebie. Wczoraj pokazywałem, że to działa, więc to mega dziwne.

**Janusz Bossak:** Działają jak tutaj. Jak już jest to działa? Nie. Ale jak?

**Damian Kaminski:** Dla nowego raportu nie da się tak.

**Janusz Bossak:** A robi nowy raport jakiejś?

**Piotr Buczkowski:** Nie dałem. Mamy takie wszystkie pana.

**Janusz Bossak:** Nie dział. Już pomijam, że w ogóle się nie odświeża, no ale dobra już nie będę się tutaj. Pastwił nad tym, ale fatalnie działają te raporty, fatalnie znaczy działają dużo, nie ktoś tam wyłączy ten trafem, bo.

**Piotr Buczkowski:** Polskiej, bo.

**Damian Kaminski:** Wiatr wyciszyć.

**Janusz Bossak:** Kurde, po prostu hałas taki, że na skupić. Bardzo dużo rzeczy to nie działa, po prostu bardzo dużo. Po prostu ja nie wiem, ja z tym mam jakieś.

**Damian Kaminski:** Znaczy powiem tak, Janusz. To jest jakiś warunek brzegowy przetestowałem to teraz na tej samej wersji to działa. Więc to musi wynikać z ze specyfiki tego raportu. Coś tam trzeba głębiej zbadać, bo.

**Janusz Bossak:** To jest banalne na pewno górę.

**Damian Kaminski:** No byłbym.

**Janusz Bossak:** 5 spraw.

**Damian Kaminski:** Nie podważam czy niebanalny, czy nie mówię tylko, że w innym działa.

**Janusz Bossak:** Świeżo zrobiony i nie działa więc. Wersja 100 dziewiąta i tak dobra, nie będziemy wszystkich trzymać, potem pogadamy, trzeba dojść do tego, dlaczego to nie działa tu dużo więcej rzeczy nie działa. No więc o to chodzi. Działa odświeżanie. Tak, robisz sobie tutaj jakąś zmianę, na przykład coś wpiszesz.

**Damian Kaminski:** Nie pokazujesz. Ale dobra, to pogadajmy już o tym w mniejszym gronie.

**Janusz Bossak:** Dobra. OK. No to tyle. Yy jak.

**Damian Kaminski:** Może jeszcze taka taka refleksja odnośnie poniedziałku zastanówcie się już dzisiaj, czy w kontekście rzeczy, które zrobiliście w tym sprincie? Jesteście przygotowani, żeby pokazać to w poniedziałek, bo czasami wydaje się, że jesteśmy zaskoczeni. Nie nikogo to był absolutnie nie wytykam, ale jesteśmy zaskoczeni tym, że trzeba to pokazać, więc warto mieć dzisiaj może chwilę refleksji. Co tam w Piotr poniedziałek powiemy i czy jesteśmy w stanie to pokazać, żeby być po prostu lepiej przygotowanym.

**Janusz Bossak:** Tak i i sprint Review nie jest miejscem do narzekań. Sprint Review jest miejscem do pokazywania, co się udało zrobić.

**Damian Kaminski:** Efektów.

**Janusz Bossak:** Dla interesariuszy efektów mieliśmy takie zadania. Udało się nam zrobić to i to, a można powiedzieć, a tego, że dania się nie udało zrobić, bo wpadły inne i tyle więcej komentarza do tego nie trzeba tak, czyli robimy to udało się zrobić to tak to wygląda. Cóż na uwagę.

**Damian Kaminski:** Tak no i to co powiedział Janusz też jest ważny. W sensie to jest nasz wewnętrzny pijar, potem przez pryzmat tego, co powiemy innym na takim spotkaniu, oceniają nas, czy jesteśmy efektywni, czy nie, więc mówmy o tym, co się udało, a nie to to o tym, co się nie udało. A to co się nie udało to omawiamy we własnym gronie.

**Janusz Bossak:** Dokładnie. Dobra, OK. Rzecz biorąc tak no dzisiaj pewnie jeszcze będzie sporo różnych spotkań, ale jeżeli z kimś nie zobaczę albo nie usłyszę, to życzę, że tak powiem. Spokojnych wyjazdów, bo część z was gdzieś tam się przemieszcza i bezpiecznych wyjazdów i bezpiecznych powrotów, tak żebyśmy się w poniedziałek wszyscy zobaczyli, nie. Także trzymajcie się miłego dnia.

**Marek Dziakowski:** Miłego dnia, cześć.

**Janusz Bossak:** Hej.

**Anna Skupinska:** Cześć.

**Oktawia Ostrowska:** Miłego dnia.

**Adrian Kotowski:** Dzięki, cześć.

**Janusz Bossak:** Cześć.

**Janusz Bossak:** [zatrzymano transkrypcję]


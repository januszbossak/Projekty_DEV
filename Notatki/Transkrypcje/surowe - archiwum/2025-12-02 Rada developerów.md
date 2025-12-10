**Transkrypcja**

2 grudnia 2025, 09:00AM

**Anna Skupinska** 0:16  
Cześć.

**Damian Kaminski** 0:41  
Cześć.

**Anna Skupinska** 0:44  
Cześć.

**Damian Kaminski** 0:47  
Daniu chciałaś chyba.

**Anna Skupinska** 0:49  
Tak już.

**Damian Kaminski** 0:49  
Proszę mówić, to proszę, masz pierwszeństwo.

**Anna Skupinska** 0:56  
O k. To może po prostu na początek?  
Yy udostępnie.

**Damian Kaminski** 1:02  
A jaki to jest temat?

**Anna Skupinska** 1:04  
Era poza forum.

**Damian Kaminski** 1:06  
Dobra, to myślę, że jeszcze zdzwonimy sobie adrianę.

**Anna Skupinska** 1:29  
Dobrze to zacznę jak będzie Adrian.

**Damian Kaminski** 1:29  
No dobrze, zarejestruj biznesowo, w sensie bardziej pod kątem co jest.

**Anna Skupinska** 1:31  
Aha o k. Dobrze więc tutaj mam.  
Api, które ma za zadanie kasować plik z repozytorium i my żeby umieszczać pliki repozytorium używamy a motkę Przepraszam klasa, talent i kasetach ment mają i ma już własny kod od usuwania.  
Załączniku przez djt jest gorzej wam, ale oprócz tego muszę też usunąć po jakby połączenie tego pliku z folderem mamy tabelę wiele do wielu, która u w której jest zapisywany, że jakieś za.  
Łącznik ma połączenie z.  
No i najpierw robię to dlatego, że one mają constraint, więc teraz niestety jest taki problem, że jeżeli na przykład to wyjdzie, a potem to nie wyjdzie. No to jest problem, bo jest usunięte połączenia. Plik ciągle będzie istniał, więc myślę, że powinnam.  
Tutaj jest to.  
Zaraz pokażę kot w emotki satyryczny, to więc emotkę jest attachment jak usuwamy jakiś plik to on tutaj ustala wszystko jak połączenie z innymi rzeczami, więc myślę, że powinnam tutaj też dodać to usunięcie tego połączenia z folderem jeśli nie istnieje.  
I też jest pytanie, czy to jest dobry pomysł? Wydaje mi się, że tak, ale chciałabym się upewnić.

**Adrian Kotowski** 2:53  
Jak najbardziej to jest tutaj dobry pomysł, też mamy gwarancję tradycyjność, jak tutaj to wszystko się wykona na raz.

**Anna Skupinska** 3:01  
Mhm.  
Dobrze, bo oczywiście to jest zmiana w kodzie, który już istnieje i służy też do ataku.  
Tu więc trzeba to dokładnie sprawdzić to, czego się popsuje. A o k super.  
Że ktoś inny ma jakieś uwagi na temat tego pomysłu.

**Damian Kaminski** 3:17  
No my się tu nie wypowiemy, jeśli mówimy na poziomie kodu tak ja rozumiem, że po prostu znaczy nie do końca zrozumiałem to w kontekście jakie połączenie usuwasz.

**Anna Skupinska** 3:19  
Mhm.  
Rozumiem.  
Dlatego, że mamy tabelę wiele do wielu, która ma, w które są zapisane informacje, do których folderów należą, które pliki znaczy, które elementy z attachment.

**Damian Kaminski** 3:39  
Czy jest tabela która mapuje której di pliku jest mapowanie na który folder? No to.

**Anna Skupinska** 3:42  
Tak.  
Takie więc jak usuwamy plik, to musimy też usunąć to połączenie, więc na początku są połączenie, potem folder no i prawda jest taki, że jak jedno się usunie, a drugie nie, to zostaje nam klika połączenie nie ma.

**Damian Kaminski** 3:46  
No tak.  
Nie no to musi być to transakcyjne, tak?

**Anna Skupinska** 3:54  
Jest jest lepiej to usuwać tutaj, żeby było w jednej transakcji, bo wtedy albo się oba po usunął, albo tylko jedno, albo obaw się usuną, albo żadne. No tak.

**Damian Kaminski** 4:03  
Dokładnie.  
Nie będzie takich.

**Anna Skupinska** 4:08  
O k. Dobrze to.

**Damian Kaminski** 4:08  
Wolnych połączeniach czy wolnych zapisów. Tak.

**Anna Skupinska** 4:12  
Tak o k. To w takim razie to na tym polega moje pytanie.

**Damian Kaminski** 4:17  
O k.  
Dobrze.

**Lukasz Bott** 4:22  
Najszybsza rada.

**Damian Kaminski** 4:23  
To.  
Nie.

**Adrian Kotowski** 4:25  
Zjemy się takich bachory to nie odnośnie tego roku nic mu.

**Lukasz Bott** 4:26  
Poza tym niektórych mięśni, które się nie odbyły.

**Adrian Kotowski** 4:30  
Sprawnie by tam wczoraj sobie przeglądałem, to znaczy nasze założenie. Wtedy jeden to chciałem jeszcze dopytać na przykład o kontekście uprawnień, bo teraz zakładamy, że ten model lub prawnej będzie bardziej zaawansowany niż ten model z tego istniejącego repozytorium repozytorium spraw. Tak naprawdę, bo teraz przewodnikiem chciałem ten wynik interesować jego odpowiedzi bardziej tego, że chciałem bardziej. Co o tym sądzicie? Na przykład tak posłuchać? Pierwszy pierwsze pytanie na przykład, czy rozruszamy taką sytuację, że można na przykład napisać dla tego samego użytkownika?  
Można mówić, pisać uprawnienie, na przykład Użytkownik ma uprawnienia.  
Nazwać się czytelnika na najwyższym poziomie na poziomie forum przestrzeni, a ktoś na przykład na niższym poziomie nadalem uprawnienia.  
Przychodzi, wiem edytora, czy w tym, że chcemy coś takiego dość robić i czy działałoby to w drugą stronę, czy ktoś ma na przykład uprawnienia edytora? Ktoś niższym poziomie mu da jej uprawnienia czytelnika i to mu się odbiera. Jak w ogóle w nim zmniejsza poziom uprawnień na danym drzewie takiego?

**Damian Kaminski** 5:41  
Dobrze, to znaczy tak.  
Po kolei po pierwsze, to nie jest na ten moment zakres naszych prac, ale jednocześnie chcemy być przygotowani na takie podejście, ale przy założeniach, że nie ma zwiększania zmniejszania uprawnień. Styl sensu stricte tylko jest zerwanie dziedziczenia i nadawanie uprawnień od nowa.

**Adrian Kotowski** 6:05  
Bądź to jest fakt, to to samo musimy. Patrzymy, czy Użytkownik ma jakieś tam prawa do jakieś uprawnienia. Jest tu jakiś zadań, czy nie ma to na przykład na pierwszym poziomie czy na trzecim poziomie? Musimy ustalić, które są ważniejsze, więc zakładamy, że na przykład te niższe są znaczy najbliżej użytkownika. To pewnie są ważniejsze, więc jakby teraz wpisujemy de facto, więc czy to nazywamy to nad wpisywaniem, czy zrywaniem, czy to jest tak, bo jedno i to samo?

**Damian Kaminski** 6:30  
No nie do końca, bo nie nie ma jednocześnie występowania dziedziczenia plus coś.  
Jest zerwanie i nadawanie od nowa.

**Adrian Kotowski** 6:42  
Znaczy, no, ale to robimy minister, czy nie użyjemy tych uprawnień na samej Górze, po prostu musimy je ignorować. Jeżeli mamy uprawnienia niższym poziomie nadany, jakby można powiedzieć, że bierzemy te uprawy. Nie ja bliżej węzła niż te dalej. Jak naprawdę, jeżeli mówimy ciągle o tym samym użytkowniku, to pewnie jest wpisywany, bo żadnych uprawnień nie usuwaliśmy, tylko musimy po prostu uwzględnić te ważniejsze.  
Skryje kwestia niezwykle, który tak naprawdę, bo tu chodzi o to, żeby nabić przemył uprawnienie ten już sam Użytkownik ma 2 różne nadanie uprawnień. No to która się robić ważniejszy?

**Damian Kaminski** 7:22  
Znaczy.  
No okej, to masz rację, że to jest nomenklatura, tylko trochę nie to znaczy to nie jest tak, które ważniejsze po prostu do jednego folderu można mieć jeden typ uprawnień.  
Nie można mieć 2.

**Adrian Kotowski** 7:36  
No takie o k, ale zakładamy, że taki scenariusz może iść nie czy możemy komuś nadal zwiększyć uprawnienia do danych poziomie czytamy. To akceptować.

**Damian Kaminski** 7:43  
Znaczy można mieć 2 o k można mieć 2 w specyficznym przypadku.  
Można mieć 2, ale to według mnie i tak będzie zaopiekowane jako jakieś tam kolejne mv, p niekoniecznie będzie realizowany dla filmu. Na razie zakładamy, że nie będzie przypadek, kiedy można mieć przypisane 2 rodzaje uprawnień. To zakładam takie, że.  
Ktoś ma uprawnienia na poziomie wysokim jakiekolwiek.  
I dziedziczone one są w dół, natomiast w przyszłości, jeśli dojdziemy do poziomu do do funkcjonalności zrywania uprawnień nadawania ich od nowa i na tym niższym poziomie temu samemu użytkownikowi nadamy uprawnienia odczytu, to na tych wszystkich wyższych, czyli pomiędzy nie wiem, czy Jestem rozumiany, czy mam to pokazać na przykładzie.

**Adrian Kotowski** 8:32  
Rozumiem przygotować, nie wie to nie.

**Damian Kaminski** 8:34  
To na tych wyższych musimy zapisać mu uprawnienie dostępu do struktury. To, o czym wczoraj Adrian rozmawialiśmy, bo on może stracić te wyższe uprawnienia, tak wynikające z tak tych węzłów najwyższych, a wtedy dalej powinien zachować kontekst, w którym folderze w głąb tam on ma te uprawnienia do tego zerwanego i powinien widzieć ścieżkę dojścia do tego folderu. Tak więc to jest przypadek, kiedy, ale to tylko według mnie, w tym dodatkowym jakimś parametrze uprawnień.

**Adrian Kotowski** 9:05  
Myślę, że interesy, bo takie potrzebne algorytmy, że dałoby się to jednak być automatycznie. Po prostu mamy coś takiego, jak mieliśmy takiego jak te punkty referencyjne uprawnień, terminie się na rózne przykład, czyli jakby węzły w strukturze full, na których są nadawane ręcznie uprawnie i to może być na przykład węże, węże Najwyższego poziomu, czyli na przykład folder w przestrzeni, jak to może być na przykład benzyny?  
Gdzieś tam.  
Raczej nie będzie dużo tych folderów z tymi pragnieniami bezpośrednio nad innymi, bo no użytkownicy raczej nie będę sobie tam ręcznie dodawać. 1000 takich miejsc tylko to będzie zwyczaj w parę katalogów, albo ktoś nadal komuś uprawnia, nawet cały folder przestrzeni samej Górze, albo na przykład nadaje na jakiś tam po.  
Podnieś pod dżemu tych folderów, więc to to można myśleć nawet wyliczyć. Wczoraj właśnie patrzymy jak to wygląda na przykładzie to specjalne zapytanie na bazie danych, które rolnicy nie mogę na przykład jak po pytaniu węzeł, to nawet te pytanie może nam wyliczyć na przykład wszystkich przodków tego węzła do góry. To nie jest jakieś takie bardzo wymagające obliczeniowo jakiej zasadzie?

**Damian Kaminski** 10:08  
Zatrzymajmy się na tym, powiedziałbym, tak?  
Chcemy zrobić rep.  
Zresztą w taki sposób.  
Na ten moment, żeby można było przypisywać uprawnienia na Górze.  
I żeby to działało, czyli na węzłach Najwyższego rzędu.  
Sposób zapisania tych uprawnień.  
Jest na pewno do do zrewidowania przez ciebie, żeby ten sposób zapisania ich nie kolidował w przyszłości właśnie z funkcjonalnością zerwania, żeby on był po prostu kompatybilny. Jak to wymyślisz?  
W oparciu zakładam o te struktury bazodanowe, które zasugerował Piotr.  
To jest już twoja kwestia. Warto by było. Nie chciałbym, żebyśmy robili to, bo to nie jest zakres naszego naszego teraz wdrożenia tego MWP.  
Może będzie kolejnym sprintem, może nie nie zakładałbym, że będzie może będzie więc bardziej chciałbym, żebyśmy zrobili.  
To znaczy bardziej chciał musimy zrobić uprawnienia dla Najwyższego rzędu. One nie powinny stać w konflikcie do później zrywania uprawnień, więc sugeruję, żebyśmy się nie doktoryzowania i z tego całkowicie, ale napisali, jak w przyszłości potencjalnie widzimy rozwój tej funkcjonalności w kontekście tych potrzeb, które dzisiaj sobie definiujemy. Czyli, że to faktycznie nie koliduje i na tym powinniśmy zatrzymać i nie nie działać w ten sposób, tylko dać takie możliwości, że na poziomie tego węzła.  
Klikam prawym, nadaj uprawnienia i wyświetla nam się okienko nadawania uprawnień.

**Adrian Kotowski** 11:45  
Chciałbym widzieć pełny obraz, bo nawet teraz jak będę projektował to funkcjonalność, no to się nie można okazać, że nie wiem, zrobił to minimalnym kosztem, żeby działało to żeby działało to na przykład dla tych mężów Najwyższego poziomu i zrobił tak, żeby tycznie na przykład nie wiem dzieła uprawnienia tam nad niższych poziomach, ale to nie będzie szczery, będą tylko bardziej tak ideowo, żeby się później się okaże, że to co zaprojektowałem, jakby tam te uprawnienia niższego poziomu, to będzie nieefektywne, bo to jest bardzo ważne, żeby też szybko wyleciało, więc no też chciałbym jeszcze liczyć.

**Damian Kaminski** 12:10  
No zgadzam się z tobą, ale to to. No więc ta twoja koncepcja, która proponujesz powinna być zrealizowana o potencjalny rozwój, czy ona nie koliduje, czy daje się w tym kierunku rozwinąć, ale nie musimy jej teraz zrobić, tylko żeby się nad tym zastanowić. Czy jeśli później będziemy w ten sposób do tego podchodzić, to nie mamy konfliktu, że wprowadzając nowy update rozwalimy wszystkie uprawnienia, które są przestaną one działać.

**Adrian Kotowski** 12:29  
Ale dobrobytu może.  
Dobra, ale to chciałem tu zaprojektować celowość, to powiedzcie mi to pytanie, czy nakładam się? Wspieramy tę opcję? Przykład zwiększania poziomów uprawnień, że nie wiem zwiększania albo odbieranie, bo to rozumiem, że to powiedziałeś dawać też wyliczenie.

**Damian Kaminski** 12:46  
Nie, nie, nie zrywa, nie zrywania.  
Bolder 22 dziedziczy po folderze jeden, który dziedziczy PO PSL. Poprze przestrzeni nie mogę na poziomie folderu 22. Dodać, że poza tymi co widzą w wyżej, tutaj widzi jeszcze ktoś zrywam i nadaje to od nowa i film, i ten i wszystkie w głąb.  
Mają nowo zdefiniowane uprawnienia.

**Adrian Kotowski** 13:15  
Ale to będzie pewnie wieczorem dynamicznie, więc takie pytanie jeszcze mam, ale dobra, czyli zakładam, że na poziomie przestrzeń mam już my nie uprawnień. Trzeba jeden przykład podałem, że wczoraj mam przykład 2 2 przypadki. Pierwszy jest taki, że na przykład na poziomie tego folderu przestrzeń mam uprawnienia na przykład do odczytu, a na poziomie 22 czy na folderze 22 mam porównanie tylko do.  
Mam w nie do decyzji, więc ja rozumiem, że to jest przypadek zwiększenia jakby uprawni to jest w porządku, ale ci biznesowe na przykład sytuacja odwrotna ma sens, bo to załóżmy, że mamy mamy na najwyższym poziomie możliwość edycji, a na tym na poziomie 20 należy 22 możliwość tylko samego odczytu. Czy to ma być wspierane takie obniżenie uprawnień?

**Damian Kaminski** 14:05  
Nie widzę problemu.  
Widzisz jakiś problem logiczny?

**Adrian Kotowski** 14:10  
Znaczy, no i jest to.

**Damian Kaminski** 14:11  
Nie ma to znaczenia z punktu widzenia takiego logicznego czy zwiększają, czy zmniejszamy.

**Adrian Kotowski** 14:16  
No musi się.

**Damian Kaminski** 14:17  
Są inne po prostu.

**Adrian Kotowski** 14:20  
Znaczy no dobra, w sensie, no myślę, że jest to też zrobienie tylko, że właśnie tak to nie wiem czy to prawo miałoby ręce i nogi, że komuś zwyczajnie nie wiem jak jest zwyczaj. Jest także Użytkownik wysyłanie widziało strukturę, a mama jedynie do możliwości, więc jakieś tam po poszczególnych folderów czy to?  
Wiem, że.

**Damian Kaminski** 14:39  
No masz rację, ale.  
Tak naprawdę tu może wskoczyć inne osoba, dlatego mówię, że to nie jest powiązane, zrywamy i nadajemy je od nowa. To jest według mnie najbardziej praktyczne podejście i czy one będą wyższe czy niższe.  
To nas nie obchodzi, bo ta logika nie zależy od tego, czy je podwyższamy, czy zmniejszamy one po prostu są inne.

**Adrian Kotowski** 15:03  
Dobra, a czy bo?

**Damian Kaminski** 15:04  
Tak mi się wydaje, że to logicznie jest mega proste, że że tutaj nie musimy analizować jakiegoś zmniejszania zwiększania, po prostu są inne.

**Adrian Kotowski** 15:12  
Mam inaczej na przykład muszę powiedzieć lityczny przykład, załóżmy, że nie dają komuś redmine na poziomie folderu świadczeń i teraz ktoś na przykład inny Użytkownik, inne admin na przykład na domi uprawnienia.  
Ale to tylko dotyczy tu na poziomie em się od tego folderu 22, że to też jakby miałoby sens.

**Damian Kaminski** 15:29  
Nie no admin powinien być wykluczony, wtedy już nie. No jak ktoś jest adminem o k no to nie jest pisane, ale no to dobrze, przy akurat jakiś tam przypadek brzegowy no według mnie admin już nie powinien być możliwy do zdefiniowania gdziekolwiek z jakimikolwiek uprawnieniami, najpierw musi przestać być adminem na poziomie tej przestrzeni, a potem dopiero gdzieś wpinamy.

**Adrian Kotowski** 15:50  
Czyli dokładnie można znaleźć na poziomie przestrzeni, tak.

**Damian Kaminski** 15:51  
Albo inaczej.  
To znaczy pytanie, czy warto go wtedy usuwać? Może to nie ma znaczenia, że admina zdefiniujemy gdzieś indziej nie ograniczy mu to, jeśli jest adminem, no to jest adminem.  
No nie wiem, nie wiem jakie to rodzi, tu podałeś się akurat no jakiś konkretny przykład, ale trzeba by było się nad tym zastanowić.  
Ja bym powiedział, że jak ktoś jest adminem przestrzeni to już nie można mu zmniejszyć uprawnień co do zasady.  
To nie to wtedy już totalnie nie ma sensu.

**Adrian Kotowski** 16:28  
Dzień według mnie podobnie jest.

**Damian Kaminski** 16:28  
Natomiast zmniejszanie uprawnień w ramach jakiegoś zasobu.  
No ma sens, bo powiedzmy, że na przykładzie takiego filmu.  
Nadaj robimy przestrzeń pielęgniarek.  
I tutaj możecie sobie tworzyć, robić co chcecie. Wszystkie pielęgniarki, cała grupa, ale jeden folder w ramach tej przestrzeni pielęgniarek, to jest folder regulaminy.  
I na nim ograniczamy możliwość edycji dla wszystkich pielęgniarek, bo to są regulaminy. Tu może edytować jedna osoba, która jest pielęgniarką przełożoną.  
A cała reszta może tylko odczytywać i to jest przypadek biznesowy, który uważam wtedy ma sens.  
A w a cała reszta waszej przestrzeni jest do waszej dyspozycji. Możecie tworzyć foldery, strukturę w głąb. Przecież jak chcecie, natomiast regulaminów nie możecie edytować, tu są tylko regulaminy.  
Tak.

**Adrian Kotowski** 17:23  
Dobra, powiem tutaj przekonałeś, które też jest to w przypadku, czyli załóżmy, że admin przestrzeni można być taką dodany do do do poziomu przestrzeni jako.  
Wpis uprawnień, natomiast wszystkie inne te typy prawni, edytor, czytelnik, mogą być notowane. Miałabyś mogą być celowo dodawane do różnych poziomów folderów i zakładając, że może być obniżane albo zwiększanie uprawnień.

**Damian Kaminski** 17:46  
Tak przy czym?  
Z tym adminem nie wiem co jest lepiej, tu warto by było, żebyśmy może to przedstawił, czy lepiej jest tak, że jeśli jesteś adminem przestrzeń, to reszta uprawnień już nie jest u ciebie realizowanych.  
Czy no?  
No tak, czyli nie jest realizowanych, ale można cię wpisać gdziekolwiek, co pozwala na przygotowanie.  
Widoczności struktury, zanim odejmę ci uprawnienia administratora, czyli najpierw zdefiniuje, że będziesz tu tu i tu, a potem ci odejmie administratora i później twoje uprawnienia już wynikają z tego zdefiniowania dopiero wtedy.  
I masz jakieś ograniczenia lub też uprawnienia, albo.  
Nie możemy zdefiniować uprawnień dla kogoś, kto jest administratorem przestrzeni, dopiero jak zdejmiemy mu to możemy mu te uprawnienia nadać. Nie wiem, co jest lepsze, nie wiem.  
W sumie.  
W kontekście naszego systemu nie ma takiego podejścia, że jak ktoś jest administratorem systemu, to nie może być administratorem procesu.  
Może być i tym i tym równolegle dopiero zdjęcie.  
Administratora systemu włącza te uprawnienia wynikające na przykład do administratora systemu, więc raczej.  
To powinno być nadrzędne, że można zdefiniować, ale nie można dla administratora ograniczać, no bo to nie ma sensu administrator może wszystko, a do administrator repozytorium tak.  
Danej danej przestrzeni.

**Adrian Kotowski** 19:15  
Że jeśli chodzi o wydajność, to byłoby lepsze jakby taki ten minister ator przestrzeni byłby definiowany jakby odgórnie, jakby on by wszystko jakby pewnie jakbym opisywał, to się z tym.  
Administratorem przestrzeni.

**Damian Kaminski** 19:27  
No i tak zróbmy, jeśli jest administratorem przestrzeni, to wiemy, bo tu na tym głównym węźle to mamy to dlatego użytkownika już nie sprawdzamy uprawnień. Chyba to znaczy. Jedyne co sprawdzamy to czy dalej jest administratorem przestrzeni?

**Adrian Kotowski** 19:40  
My tak znaczy, można było temu człowiekowi doradzić. Na przykład mówiłeś nie przypadek, że można mu dawać te uprawnienia. Na przykład nie wiem duplikować czy on jest ********* przestrzeni, ale można będzie zadowolenie poziomie, dodać jakieś, nie wiem na przykład po.  
Korektora i to wtedy mogłoby być tak, że są 2 uprawnienia, jakby że na jednego folderu są 2 uprawnienia i tak jest brany wybrany to, że Użytkownik administratorem, ale jak na przykład się wyłączy tygodni ministra pora, bo mówiłeś, że to chciałbym sprawdzić sobie tam coś i zabrać mu tego możemy uznawać tego ministra w przestrzeni. Wtedy musi ta struktura będzie generowała zgodnie z tymi normalnymi.

**Damian Kaminski** 19:54  
Mhm.

**Adrian Kotowski** 20:15  
Pragnieniami typu edytor albo czytelnik.

**Damian Kaminski** 20:15  
Uprawnienie.  
No tak, mogłoby tak być.  
Dobra, ale nie chcę, żeby to spotkanie zjadło nam, że tak powiem tutaj na samo repozytorium na to jeszcze mamy poświęcony odrębne. Nie wiem, czy ktoś chce to skomentować, czy to dla was też jest?  
Zgodne z logiką systemu.

**Janusz Bossak** 20:39  
Ja tam szczerze mówiąc trochę tak się wyłączyłem słuchania.

**Damian Kaminski** 20:42  
Wyłączyłeś no właśnie, no nie chciałbym, żebyśmy tutaj, jeśli są jakieś znaczy możemy dalej dyskutować Adrian, ale jeśli reszta, że tak powiem, nie jest zaangażowana, to niekoniecznie musimy ich trzymać. Pytanie, czy jeszcze coś stąd mamy, co wymagałoby?  
Ee przejrzenia.  
Posortuj sobie dwudziesty czwarty sięgnie to okej, tu nie ma żadnych nowych tematów. To może tak pytanie najpierw, czy ktoś jeszcze chce coś poruszyć w kontekście stricte rady, może nie związanej z repozytoriami możemy Adrian zostać, bo przestrzeń jakąś jeszcze na to mam.

**Janusz Bossak** 21:21  
Że to są 2 tematy, ale to one wymagałyby pewnie Piotra, bo jeden wraca temat.  
Pobierania danych ur towo jakby z raportu to jest temat, który też Przemek wpisał na radę linie na radę deko, narod, mapę.  
Zbieranie danych za pomocą tego protokołu open data.  
A tu jest jakiś klient, już nie pamiętam nazwy, a RL Stage.  
Który by tam jakoś chciał dane z raportów pobierać.  
Myślę, że mówiąc nie wiem co z tym zrobić, czy robić jakieś chwilowe obejście. Już tam mamy podobno jednego takiego klienta, który strzela nam do amo tita po api i wyciągam milion.  
Danych.  
I obciąża chmurę.  
I to byłby kolejny, który by tam nam strzelał po to tylko, żeby dane sobie wyciągać.

**Damian Kaminski** 22:14  
Możemy to na chmurze ograniczać?

**Janusz Bossak** 22:14  
Gdzieś tam.  
No tak, no ale trzeba jakoś przemyśleć. Tak znaczy nie chciałbym, żeby to był Janek pijanowski pisze. Klient wrócił do tematu i dopytuje się o nasze rest api. Nie?  
No i pytanie do mnie do ciebie, co myślicie? No nie wiem czy widzisz tą na kanale to do ciebie mówię do Damiana też ty jesteś tam skierowany.  
Na tym kanale.

**Damian Kaminski** 22:36  
To nie jeszcze się z tym nie zapoznawałem, ale tutaj akurat tam znajomym nie pytał o to jest taki system do.  
Ale akurat na to trafiłem. Nie chciałem tym przykrywać. To jest taki system do zbierania zamówień z różnych źródeł ich pochodzenia, czyli powiedzmy ktoś tam w jakimś ma sklep internetowy i ma swoją stronę. Ma allegro, ma jakiegoś powiedzmy Amazona i różne typy fills źródeł sprzedaży kanałów sprzedaży.  
No i.  
To narzędzia pilot to zbiera tak, czyli jest takim menadżerem sprzedaży, czyli wszystkie zamówienia trafiają po prostu w jedno miejsce. Nie trzeba obserwować wielu różnych źródeł, no i oni też mają u sobie u siebie limit zapytań i koniec, bo.

**Janusz Bossak** 23:18  
Tak, no to powinniśmy mieć takie limity zapytań, czy to godzinne, czy minutowe, czy dzienne czy jakoś.

**Damian Kaminski** 23:22  
Tak ich jak chcemy zwiększe jak ktoś chce więcej, no to sorry to kosztuje, bo są z tym związane wydajności.

**Janusz Bossak** 23:33  
Słuszna uwaga, to jedna rzecz, którą trzeba pewnie zrobić, no ale teraz już wiesz, jacyś klienci coś mają, no i to wprowadzenie im ograniczeń, to już będzie odbierane, że coś tutaj, ale.

**Damian Kaminski** 23:43  
No według mnie powinniśmy zacząć od analizy, czyli zobaczyć, na kogo będzie miało to wpływ i jakie to faktyczne, czy jesteśmy w stanie to jakoś sprawdzić o te zapytania zewnątrz.  
Myślę, że no po prostu to też klienci muszą zrozumieć, że jak wprowadzimy coś takiego, no to.  
Muszą się dostosować, muszą zmniejszyć na przykład częstotliwość. No nie wiem, ja mogę przerzucić po prostu tutaj jako niu, żeby to nam nie wypadło i zostawić to na Radzie.  
Wróci Piotr, to będziemy to omawiać.  
Pytanie tylko, czy zanim wróci Piotr?  
Jesteśmy w stanie to do kogoś przypisać może Łukasz poskrobko nawet nie wiem, kto mógłby nam pokazać listę. Nie wiem.  
Firm klientów, którzy 20 pierwszych, którzy najwięcej mają tego typu połączeń zewnętrznych aplikacji.  
Bo to nam da jakiś obraz jak do tego podejść i czy to dotyczy jednego klienta, czy to dotyczy jakiejś skali, jakie poziomy przyjmować i tak dalej, bo tak to błądzimy tak.

**Adrian Kotowski** 25:04  
To się teraz przed kolorem mieście jest wykorzystywany ten logowanie bonito mi to, że w jedności też i to można z tego skorzystać, ale twarzy to jeszcze integracji niezależnych, który też odwołuje się, odwołują się do się tam z jednej strony kapi, ale nieco się relegowany.

**Damian Kaminski** 25:21  
No tak, bo tu pewnie by trzeba było ograniczyć.

**Adrian Kotowski** 25:26  
Ale myślę, że tak trzeba by lepiej jakoś z może nie tyle z mojej radości, żeby to zabrać globalnie czy jakoś nie wiem ruch wychodzący by zbadać tej wiem o filtrować jakieś tam nasze nasze witryny tam i po prostu zobaczyć co jest na zewnątrz, więc to chyba lepiej jednak.

**Damian Kaminski** 25:38  
Tak.  
Stef connector i tak dalej.

**Adrian Kotowski** 25:42  
Dziś ażur monitor może.

**Lukasz Bott** 25:42  
Ale.  
Dałem, żebym dobrze zrozumiał i ty chciałeś, żeby zestawienie wywołani zewnętrznych usług do nas.

**Damian Kaminski** 25:45  
No.  
No bo ja to tak rozumiem, czy oni od nas strzelają tak dużo na zewnątrz?

**Lukasz Bott** 25:58  
Ja to jest zrozumiałem, że że ktoś wykorzystuje nasze rest ap, no i robi tego dużo i faktycznie rest api to gdzieś kiedyś z piotrkiem pogadałem. No no nie jest zbytnio na chwilę obecną, nawet jakoś tam wydajnościowo przygotowane, żeby obsługiwać właśnie jakieś takie duże masowe r.

**Damian Kaminski** 26:01  
Do Janusz.

**Janusz Bossak** 26:21  
No tak.  
Tym jest problem właśnie nie.

**Damian Kaminski** 26:26  
No okej, no to w takim razie w 2 strony tak.  
Dobra, coś zostawmy, żeby tutaj.

**Janusz Bossak** 26:31  
Nie no, chodzi o to, żeby inne systemy nie strzelały do amo dita albo że.

**Damian Kaminski** 26:36  
A właśnie, czyli o k.

**Lukasz Bott** 26:37  
To znaczy może inaczej mogę sobie strzelać tylko tylko na jakiś tam.

**Janusz Bossak** 26:41  
Tak no bo.

**Lukasz Bott** 26:43  
Regulacjach tak przy zakładaniu jakieś.

**Janusz Bossak** 26:44  
Może my strzelamy do zewnętrznych systemów? To jest problem tych zewnętrznych systemów. Jeżeli my strzelamy za często, ale chodzi o to, żebyśmy.  
Yy chronili amo dita szczególności, a modico na chmurze, no bo jak to robi sobie klient na on premises, no to jego sprawa. Tak, no to sobie tam obciąża, ale jeżeli to robi na chmurze i nam wysyła co minutę zapytanie o raport, który zawiera, nie wiem 100000 pozycji, no to tak nie chcemy.  
W tym jest problem, nie.

**Adrian Kotowski** 27:19  
Takie wzorce chmurowe, że jeżeli jest jakiś limit i czy powiedza pytań, to na przykład można zwracać, że nie wiem. Przekroczony limit gdziem status HTTPI to też w sumie jest wykorzystywany.

**Damian Kaminski** 27:28  
No to wiecie, to to już jest wtórne pytanie na początku musimy ustalić, jaka to jest skala, kogo to dotyczy, jaki ten limit powinien być dobrze. Jeszcze tutaj Adrian ty zasugerowałeś, że zbiera coś takiego monitor wydajności, ale z zewnętrznych zapytań.

**Adrian Kotowski** 27:42  
Nie wiem czy to jest w drugą stronę, tylko ja myślałem, że to jest wchodzący samowita monitor wspiera ruch jakby skoro resta więc to wychodzący, ale monitor acer monitor powinny rejestrować tych cały ludzki. Tam wychodzę przechodzący też.

**Damian Kaminski** 27:57  
Dobra, to zapytamy Łukasza, czy czy on coś tu jest w stanie z tych statystyk serwerowych wyciągnąć?  
No i tyle. Ja nie znam tego tematu, przyznaję. Janusz, więc zaraz się z nim zapoznam i podstawę, bo kogo to w ogóle dotyczy to jakieś klient mój.

**Janusz Bossak** 28:15  
Ellie Stage.

**Damian Kaminski** 28:17  
A to nie to ja nie miałem nigdy z nim przyjemność.

**Janusz Bossak** 28:20  
Znaczy, wiesz, to jest temat raczej taki ogólnorozwojowy, no bo mamy wpisane na root mapę na 2.  
Ten open data standard tak, no to Przemek tam mocno ciśnie, no bo chodzi o to, żeby wyciągać dane do tablo czy do ja i tak dalej, więc ja bym raczej wtedy przyspieszył tę pracę. Może, które są zaplanowane na ten *****, żeby może one były wku jeden.

**Damian Kaminski** 28:35  
Mhm.

**Janusz Bossak** 28:46  
Yy i żeby się tym zająć, no żeby właśnie nie obciążać amo dita, takimi wiesz, r questami typu podaj mi dane z tej sprawy, podaj mi dane z tej sprawy, podaj mi i tak 100000 razem nie.

**Damian Kaminski** 28:58  
Widzę to, że my te to było i że to może się nie spodobać klientom. No to jest oczywiste. Ja znam też przypadek biznesowy z innej firmy, projektach płacił do tej pory miał tych miał jakiś żądań, ileś płacił do tej pory rząd stawki rzędu 1000 zł, a nagle została mu zaproponowana w zasadzie bez możliwości negocjacji. Stawka w okolicach 15000. No ale to wynikało właśnie z potrzeb.  
Z potrzeb tego konkretnego.  
Podmiotu tak, że oni tak taką dużą mieli skalę, więc my wprowadziliśmy.  
Na resta pi.  
Nasz ten nasz.  
Licencję no i teraz może kolejnym krokiem i wprowadziliśmy to za raczkowało zaczęli wszyscy tego korzystać i nie mieliśmy z tym problemu. No ale dochodzimy do sytuacji, gdzie każdy wszystko ze wszystkim integruje. No i zapowiadamy, że za 3 miesiące wprowadzamy nowy certyfikacje na to, że resta pupy jest ograniczone do nie wiem 10000 czy miliona zapytań w miesiącu jest to skalowane per dzień nie tak, że jednego dnia można strzelić milion tylko na 30 dni dzielone. Chcesz więcej o k to rozmawiamy z powrotem o o licencji, podwyższamy ci tą licencji nie ma.  
Wtedy finansowanie zasobów na to, no i tyle.

**Janusz Bossak** 30:18  
Ja się tutaj jak powiedziałaś najpierw trzeba to zbadać, ile to rzeczywiście obecny jest w szczególności tych skrajnych przypadkach, gdzie tam ludzie mają swoje.  
Systemy i strzelają bezpośrednio na przykład do Trade Center, bo to tam też występuje.  
No i tak samo czy strzelają do amo dita, ile tych danych pobierają, nie żebyśmy wiedzieli jaki to jest strumień.  
No ale to wracając do tego Stage.  
No trzeba temat pewnie.  
Rozpoznać tak no może jakieś obejście dla nich z tymi raportami? Tutaj pamiętam. Propozycja była taka, żeby.  
Wywołanie jakiego się pointa, którego pewnie nie mamy dotyczącego jakiegoś raportu.  
Może działało w ten sposób, że najpierw się ten raport po stronie amo dita wygeneruje, zapiszą się.  
Jego wyniki.  
Gdzieś to znaczy, to jest moja, absolutnie teraz wymyślona koncepcja, tak i potem cała ta paczka wyników zostanie przekazana. Tak, no ale no to trzeba całą tą koncepcję wymyśleć. Tak na razie tego nie ma, nie mamy czegoś takiego jak odpytywanie się o dane z raportu.  
Nie ma takiego endpoint tu.

**Damian Kaminski** 31:33  
No tak, to też w kontekście chmury pewnie mogłoby być jakoś nie wiem nawet kolejkowa owane.

**Janusz Bossak** 31:38  
Jakbyś kolejkowanie, no no trzeba temat zgłębić, skoro się kolejny klient o to pyta.  
Zobaczyć jak coś z tym zrobić, no.

**Damian Kaminski** 31:48  
No tak, bo ile pyta o konkretną sprawę, to dostaję odpowiedź od razu. No jak pyta o zestawienie.

**Janusz Bossak** 31:48  
Trudno jest.

**Damian Kaminski** 31:55  
Jakiegoś nie wiem miliona danych, no to to musi najpierw zostać zebrane w modlitwie, tak?

**Janusz Bossak** 32:00  
No właśnie o to chodzi, no więc to naprawdę to nie temat na tej radę, żeby o tym jakby zdecydować tylko jedyne, co możemy zdecydować. Jeszcze ma się tym zająć, tak.

**Damian Kaminski** 32:05  
Tak, tak, tak, tak, dobra.  
Mamy zapisane jest wrzucone na radę o k.  
Jeszcze coś Łukasz było z ostatniego piątku, tylko znaczy czytam co tutaj, czego coś przypisaliśmy na radę.  
Czy ty pamiętasz?

**Lukasz Bott** 32:23  
Wiesz co to wczoraj to?

**Damian Kaminski** 32:26  
Czy to było to?

**Lukasz Bott** 32:27  
Ja mam spisane z spisane numery.  
Tak, 2 2 411 tu mam taki spisany.  
Żeby się tym zająć.

**Damian Kaminski** 32:40  
Dobra, bo to Janusz ty opisałeś.  
Mm.

**Janusz Bossak** 32:49  
A no tak, tak tak, bo to było zgłoszone chyba przez LP albo przez no.

**Damian Kaminski** 32:54  
Tak, tak, tak.

**Janusz Bossak** 32:56  
Coś takiego?  
No tak, czy to przy okazji tych też ogólnie filtrów?  
No ale co jest jakaś wątpliwość co do tego?

**Lukasz Bott** 33:10  
Czy musimy te rady dali?

**Damian Kaminski** 33:11  
Nie może nie tyle, co jest wątpliwość to.

**Janusz Bossak** 33:15  
Ja pamiętam, myśmy Damian chyba rozmawiali na ten temat.

**Damian Kaminski** 33:18  
Tak, tak, tak tylko tam była taka konkluzja, że może powinniśmy się spotykać. Ty to opisałeś zaproponowałeś tylko ja tu widzę.  
Takie cząstkowe, że to jest cząstkowe rozwiązanie, pytanie, czy to na pewno jest już koniec, bo ty to opisałeś w kontekście tylko i wyłącznie tych filtrów lewych.  
Ee a nie ma kontekstu filtrów górnych, a de facto o k. Zgadzam się, że najczęściej pewnie wykorzystują filtr po lewej stronie, natomiast równie dobrze ktoś może wykorzystać filtry na Górze. No i pytanie, czy to na razie robimy? Obsługujemy tylko to, czyli ktoś może zdefiniować filtr różnorako albo przez drzewko, tak jak mamy tu albo na Górze ograniczyć to w jakim zakresie i teraz?

**Janusz Bossak** 34:05  
Znaczy.

**Damian Kaminski** 34:05  
Na razie rozpatrujemy, rozumiem tylko drzewko, jeśli.  
Bo wiesz, załóżmy tak mamy drzewko i filtr na Górze takie combo.  
I znika z drzewka wszystko.  
Ee, czyli jest realizowany to co ty zaproponowałeś gdy na raporcie nie ma już co pokazać, powinno przenieść zaznaczenie do najbliższego rodzica. W raporcie wyświetlać pozycje odpowiadające temu nowemu zaznaczeniu.  
A jeśli tutaj?  
W połączeniu z filtrami górnymi dalej nie ma nic.  
To co wtedy?  
Musiałbym przygotować taki przypadek, bo nie wiem faktycznie, co się wtedy wydarzy.

**Janusz Bossak** 34:51  
Znaczy no tam jest temat rzeczy.

**Damian Kaminski** 34:53  
Ale rozumiesz o co mi chodzi, tak?

**Janusz Bossak** 34:54  
Tak, tak, tak myśmy rozmawiali w ogóle o zmianie.  
Mm jakby sposobu zachowania się systemu po wykonaniu masowych czynności, ogólnie rzecz biorąc.

**Damian Kaminski** 35:09  
Tak.

**Janusz Bossak** 35:11  
I tam mieliśmy jakieś konkluzje z tym związane, polegające na tym, że znaczy moja chyba była taka, bo pamiętam, że miałeś inny pomysł trochę.  
Moja konkluzja była taka i mój pomysł jest taki, żeby wykonywało się.  
To ta akcja masowa.  
Czy to jest podpisywanie, czy to jest?  
Akcja masowa w rozumieniu wykonywania jakichś reguł.

**Damian Kaminski** 35:38  
Przeciwko.

**Janusz Bossak** 35:40  
I żeby.  
Nic się nie zmieniało na raporcie.  
Tak, czyli momencie, kiedy wykonuje tą akcję?  
To.  
Nie zmienia mi się kontekst raportu, czyli tylko i wyłącznie.  
Za pomocą nie wiem sygnał r.  
Te pojedyncze rekordy.  
Są aktualizowane, pamiętasz, bo to wiązało się z jeszcze innym zupełnie tematem aktualizowania informacji po wykonaniu raportu. Po wykonaniu takiej akcji masowej, że te pojedyncze rekordy, które zostały nazwijmy to dotknięte wykonaniem.  
To ich zmienia się ich stan. Tutaj widać, że jest na przykład tam, no na zielono dokładnie o to mi chodzi, tyle że.  
Po.  
Pojawiają się też na przykład, jeżeli wykonanie tej czynności, którą wykonałeś spowodowałoby. Nie wiem. Uzupełnienie daty przekazania, to ona powinna się tu pokazać.  
Jeżeli.  
Te czynności spowodowały zmianę stanu tego.  
Ale nie jest tutaj to wyświetlone. Na przykład nie mamy etapu, ale gdybyśmy mieli etap, to tam powinno się napisać. Powinni się napisać ten etap, mimo że on teraz nie pasuje do ustawień filtrów.  
Po powinno to zniknąć.

**Damian Kaminski** 37:03  
Mhm, rozumiem, rozumiem twoje podejście. Znaczy według mnie to już jest bardziej długofalowa wizja.

**Janusz Bossak** 37:11  
Ale tak powinno być w moim przekonaniu, ja jako Użytkownik bym to rozumiał, tak mi się wydaje tak, że wykonuje pewien pewną masową czynność, która zmienia mi rzeczy, które mam, jak gdyby raport po wykonaniu, czyli widzę, co się zmieniło i teraz dopiero decyduje odśwież mi raport tak i teraz wszystko inne się dopiero teraz wykonuje, tak, że znikają sprawy, odświeżają się filtry i tak dalej i tak dalej nie.

**Damian Kaminski** 37:12  
O k.  
Mhm.  
Mhm.  
Tak, ale o k.  
Mhm no.  
Notabene zobaczcie jeszcze.  
Co się dzieje tu chyba niepożądany skutek. Już wam pokazuję, chciałem tylko sprawdzić, czy dobrze myślę, jak mamy ustawione domyślnie na zawiera tu mimo że nie ma żadnego filtru, jest wyczyść wszystkie jak kliknę wyczyść to zniknął. Zobaczcie te zawiera, mimo że tam jest nic nie jest zdefiniowane.  
Powinniśmy to chyba poprawić.

**Janusz Bossak** 38:02  
No to jest tak.  
Dodatkowe efekty.  
On jeszcze nic nie zawiera, nie?

**Damian Kaminski** 38:10  
Tak dokładnie. Natomiast to co mówisz Janusz, to tu mamy, powiedziałbym tak to co mówisz, to już jest kolejny element wtajemniczenia w aktualizację danych na raportach. Natomiast my mamy tu pewną niespójność.  
To znaczy.  
Mm.  
I od tego należałoby według mnie w ogóle zacząć jakąkolwiek dyskusję.  
I to co się dzieje po podpisaniu i tak dalej, bo.  
Zaraz wam pokażę.  
Tylko spojrzę, czy taka akcja masowe tak jest indeksu i po podpisaniu, czyli jest masowe podpisanie i akcja wykonywana po podpisaniu.  
Czyli tu mamy pierwszą niespójność w systemach i ja bym od tego zaczął jako zgłoszenie, czyli jeśli podpisuje, a ten podpis skutkuje jednocześnie wykonaniem jakiejś akcji, to zobaczcie jak jak się zachowuje system.  
Wybieram podpis.

**Janusz Bossak** 39:29  
Co się robi?

**Damian Kaminski** 39:29  
Jeszcze mieli rozpoczął proces podpisywania i na razie czekam, nie wiem czemu to tyle trwa.  
O k dokument został podpisany na drugim ekranie. Tu cały czas mieli, no to coś się.  
Coś się znowu zmieniło od ostatnich kilku dni?

**Janusz Bossak** 39:54  
Znaczy.

**Damian Kaminski** 39:55  
No dobra, no nie działa tak jak powinno, nie mniej.

**Janusz Bossak** 39:56  
Nie wiem, co tu się miałoby wydarzyć w tej chwili, ale.

**Damian Kaminski** 40:00  
Potem zdarzeniu powinno się odświeżyć okienko, tak jak na tym zgłoszeniu. Czy chcesz odświeżyć raport?

**Janusz Bossak** 40:08  
No tak.

**Damian Kaminski** 40:08  
I teraz tu mamy niespójność, bo to od to okienko odświeżenie raportu wynika z tego, że oraz wykonano akcje.  
I teraz mamy niespójność w postacią, teraz przeładował już wszystko. Mamy niespójność w postaci takiej, że jeśli podpisujemy z wywołaniem akcji masowej, to wyświetlamy pop, czy chcesz odświeżyć czy zamknąć? Czyli chcesz zobaczyć stan sprzed wykonania tej akcji, bo to oznacza zamki? Czy chcesz już odświeżyć, czy nie widzieć tych spraw, na których albo albo nie widzieć, albo zobaczyć zaktualizowany raport o te akcje, bo nie wiadomo jaka to może być akcja po prostu wypełnienia dodatkowych pula może być akcja przeniesienia na inny etap i na tym etapie już nie widzimy.  
Spraw na tym raporcie natomiast nie mamy tego okienka dla samego wykonania akcji.

**Janusz Bossak** 40:54  
No tak tak, no to to jest to, co mówiłem, że myśmy o tym już rozmawiali. Ta dokładnie tą samą dyskusję prowadziliśmy.  
I jak absolutnie Jestem za tym, żeby to uspójnić, żeby to nie miało znaczenia, czy to jest podpisywanie z akcją, czy podpisywanie bez akcji, czy wykonywanie samej akcji masowej.  
To chciałbym, żeby.

**Damian Kaminski** 41:15  
Powinniśmy kończyć ekranem po podsumowaniem, tak?

**Janusz Bossak** 41:19  
Powinniśmy po pierwsze.  
Zmieniać stan tych rekordów, które?  
Podlegały tej masowej akcji jakiejś, czyli żeby mi się tutaj wyświetlało na przykład w kolumnie organizacja czy w kolumnie data przekazania? No w takich, których po prostu mamy coś wyświetlamy. Jeżeli ta akcja jakakolwiek by to nie była. Akcja masowa powoduje zmiany jakieś to, żeby to się tu wyświetlało, żebym widział, że się zmieniło. Tak natomiast nie ma się wykonać odświeżenie takie tak znaczy ja po prostu chcę przejrzeć tą stronę, którą widzę.  
I jakby no zapoznać się z tym, że co mi się tu wydarzyło, nie.  
Faktem jest, że my nie mamy opcji cofnij tak, że jak ktoś wykona akcję masową to nie ma.  
Opcji cofnij tą akcję masową, no to już jest zupełnie inna sprawa.  
Ee no ale przynajmniej będę widział i będę mógł ocenić co mi się tutaj zadziałało, bo nie wiem, będę mógł sobie zrobić chociażby screen tej strony, jeżeli coś zrobiłem źle i wejść wtedy pojedyncze, to jest prawy i je poprawić, a w momencie kiedy znikają mi z ekranu to ja nie wiem co się wydarzyło. Tak coś poszło zniknęło, nie wiadomo, nie.  
Rozdzielić te 2 jakby 2 Stany jest stan taki, jakby raport po wykonaniu czynności masowych, czyli widzę na ekranie, co się wydarzyło. I dopiero klikam odśwież i wtedy mi się jakby no na nowo czytują filtry zgodnie już z tym co jest po wykonaniu tych akcji tak, czyli jakieś sprawy się przenoszą na inne etapy znikają z powodu filtrów tych u góry czy tych z boku nie ma znaczenia, tak po prostu robi się sytuacja i teraz wracając zataczając pętlę.  
Do tego zgłoszenia, od którego zaczęliśmy to to jest właśnie taki przypadek końcowy, to znaczy, że.  
Zmienia się stan filtrów po lewej stronie, bo nie ma już nic do pokazania w związku z tym odświeżeniem.  
I co zrobić? To jest zupełnie jakby inne zagadnienie. To jest zagadnienie dopiero jako następni tego, o czym mówimy teraz. Czyli co zrobić, jak tam miałbyś po lewej stronie rozwiniętego tego smsa? Weź tam na przykład tego smsa. Rozwiń po lewej stronie, no i tam ostatnio i tutaj jest jakaś pozycja, nie.

**Damian Kaminski** 43:44  
Mhm.

**Janusz Bossak** 43:45  
No i teraz byłbyś na tej pozycji dokładnie tutaj. Data podpisu nie przypisaną to, co zrobić, kiedy te 2 rzeczy znikną?

**Damian Kaminski** 43:55  
Dokładnie.

**Janusz Bossak** 43:56  
Tak, bo to będzie oznaczało, że w ogóle już zmysla nie ma.  
Nie ma nic dla niego.  
Tak, czyli ani nie mogę stać na tej pozycji, którą teraz stoimy, ani nie mogę stać na pozycji zmysł, bo bo już go nie ma.

**Damian Kaminski** 44:05  
Dokładnie.  
Nie do do do do tego zmierzam, tak tak tak, że to trzeba wtedy.

**Janusz Bossak** 44:13  
Więc to powinno spowodować.  
Sytuację taką, że to byłoby równoznaczne z tym przyciśnięciem u góry wyczyść filtr, bo zmysł zniknął, nie ma już go, nie ma nic do zrobienia. Ósmy psa nie.

**Damian Kaminski** 44:26  
No tak, tylko teraz jeszcze skomplikuje.  
Czyli mamy maj i lipiec.  
Jak dacie utworzenia dam.  
No niech będzie, że to jest.  
W miesiącu.

**Janusz Bossak** 44:42  
Ale.  
Ale wtedy zadziała dobrze.

**Damian Kaminski** 44:44  
Maj.

**Janusz Bossak** 44:46  
2 działa dobrze.  
Bo bo skoro tak, to prawdopodobnie zaznaczyłeś tylko tą umowę i tylko ta jedna zniknęła.  
I wtedy zmysł po lewej stronie zostanie, bo jest jakiś inny jeszcze.

**Damian Kaminski** 45:01  
Ale będzie pusto.  
Rozumiesz?  
Więc czy to jest właśnie, ale będzie pusto, czyli aha, ale pozostanie do tego zmierzasz o k.

**Janusz Bossak** 45:07  
No tak, no nie no k.

**Damian Kaminski** 45:13  
Że to nie zniknie. Mhm, dobra, masz rację.

**Janusz Bossak** 45:13  
Jeżeli.  
Znaczy, bo to drzewko po lewej stronie się buduje, no więc ono się buduje zgodnie z filtrami, no i albo będzie, bo nie.

**Damian Kaminski** 45:23  
Ale nie nie pozostanie. Przepraszam, nie pozostanie, bo jak my to obsłużymy, bo zobacz, czekaj, czekaj, czekaj, czy pozostanie jak dam styczeń?  
A nie to dobra o k. Jest tylko tutaj, po prostu się nic nie wyświetla, o KOK jest, bo to się buduje niezależnie od tego.

**Janusz Bossak** 45:41  
No właśnie, no więc on tu pozostanie, tylko będzie napisane, że i teraz, gdybyś u góry ten filtr zlikwidował to na tym smsie coś się pojawi się nie pojawi dlatego że jest ten fryz górny nie.

**Damian Kaminski** 45:50  
Tak, tak, tak, tak masz lec.  
Mhm.

**Janusz Bossak** 45:54  
Ale słuchajcie, no to jest temat do obsłużenia, według mnie to co tutaj jest zgłoszone od rossmana jest właściwie końcowym efektem tego, o czym rozmawialiśmy przedtem. Tak wydaje mi się, że wydaje się to zrobić, niezależnie to znaczy, żeby się odświeżyło, tak jak rossman chce, czyli żeby odpowiednio tutaj znikało i tak dalej.

**Damian Kaminski** 46:06  
Dobra, to znaczy.

**Janusz Bossak** 46:15  
I to się wpisuje w ten nasz temat naprawiania czy poprawiania raportów, przy czym to naprawdę nie jest.  
Najważniejszy problem.  
Bo to jest estetyka.

**Damian Kaminski** 46:27  
No nie, bo to jako Użytkownik ma takie przypadki. To jest kwestia wytłumaczenia jak wyczyść filtr, musisz pamiętać i sobie poradzisz.

**Janusz Bossak** 46:29  
Czy wygody?  
Tak to jest temat taki raczej wygody jakiejś takiej. No trochę niespójności systemu, ale to nie wywala systemu i nie powoduje, że nie można z nim pracować, jest po prostu mniej przyjazny.  
Natomiast mamy prawdopodobnie ileś tematów związanych z samymi błędami i te trzeba głównym.  
Głównie poprawiać, nie.

**Damian Kaminski** 46:59  
No dobra, z tym tematem, o którym mówisz, że tu odświeżenie, to według mnie to trzeba jeszcze przegadać na jakimś designie, bo ja tu widzę dużo ryzyk to ma się stać z całą ramą dookoła, jak które filtry mają uwzględniać, czy to mrozimy wtedy, bo tu są, żebyśmy potem nie, nie wykopali sobie dołu, że tu odświeżymy, a ktoś powie, a tu teraz jest ta informacja, tu jej nie ma.  
No właśnie.  
Dobra.  
Ee to podsumowując.  
Ten twój opis, jak rozumiem w tym momencie taki pozostaje, po prostu trzeba to tylko zaplanować.  
Poproszę Mateusza, żeby to zwali dołował zresztą nie wiem czy tego już tu nie zapisałem.  
Aha.  
O k.  
Mateusz jeszcze sugerował.  
Odświeżenie całej strony.  
Tylko, że to nie ma sensu, bo tego filtra już nie ma.  
A teraz twój twoja propozycja pokrywa się z tym pytanie, czy chcemy jeszcze dołożyć coś takiego?  
Halo.

**Janusz Bossak** 48:42  
No.  
Pytasz się mnie?

**Damian Kaminski** 48:49  
No.  
Czy jako, bo twoja propozycja sprowadza się do tego odśwież z filtrami?  
Ale to powinno być za aktualnymi chwili.

**Janusz Bossak** 49:04  
Znaczy to jest jak widzisz propozycja Mateusza nie maja.

**Damian Kaminski** 49:08  
Tak, ja wiem, tylko powiedzmy twoja propozycja jest rozbudowana przez Mateusza o opcję jeszcze przeładuj raport czyli odśwież na czysto tak jakbyśmy kliknęli w 5.

**Janusz Bossak** 49:20  
Znaczy.  
No to trzeba.  
Znaczy, są 2 rzeczy pierwsze poinformowanie?  
Użytkownika tego raportu.  
Może to być zrobione w następujący sposób, jest komunikat na środku, który podsumowuje, co się wydarzyło, że tam przeanalizowane czytam.  
No akcje masowe dla tam tylu i tylu spraw dla tylu nie wykonano na przykład błędy, na przykład nie można było zaktualizować, nie można było przesłać coś tam coś.  
I powinno być komunikat według mnie duży komunikat, że mogę zamknąć to okienko w ten poparł z tym komunikatem, ale jeszcze nic mi się nie odświeży, że tu 2 powinny być nie tak.

**Damian Kaminski** 50:10  
I to jest ta opcja, ta opcja zamknij to realizuje.

**Janusz Bossak** 50:13  
Tak, zamknij po prostu zamykam i to, co ja mówiłem wcześniej zostajemy na tym ekranie.  
Z tymi zmianami, które już są w rekordach, natomiast nie.  
Wpłynęły jeszcze na filtry.  
Czyli widzę tą listę nam na zielono na czerwono mogę ją sobie przejrzeć, mogę zajrzeć do tych spraw na przykład na czerwono.  
Yy, które się tam nie wykonały, żeby stwierdzić co tam było nie tak, nie.

**Damian Kaminski** 50:42  
Mhm.

**Janusz Bossak** 50:43  
I dopiero.  
Potem mogę coś zrobić. Tak, mogę ogólnie rzecz biorąc kliknąć odśwież i wtedy mi się ten raport jakby przebuduje już tymi oświeconymi rekordami.  
Mogę działać na filtrach, mogę wybrać inny filtr i wtedy cokolwiek właściwie zrobię, to powinno się zastosować już te te zmiany. Tak ten raport powinien się już według mnie zaaktualizować tak, a jak kliknę to zielone tutaj zamknij i odśwież no to po prostu przyjąłem do wiadomości i wszystko się wykonało, zamykam, odświeżają mi się filtry, te rekordy już mi znikają zgodnie z ich jakby przeznaczeniem i aktualnym stanem i tyle. A jak zamknę.  
To wracam po prostu do raportu, w którym widzę te rzeczy, które się zmieniły. No i to jest moja główna mój główny postulat, żeby.  
To zostawało jak tutaj kliknę. Zamknij, żebym widział co się pozmieniało po wykonaniu tych akcji masowych.

**Damian Kaminski** 51:41  
Tak, to tak teraz jest akurat domyślnie. W sensie tak to działa, dlatego przypadku tak to działa dla przypadku kiedy w ogóle nie wyświetlamy tego okienka, czyli wykonujemy akcje masową typu.

**Janusz Bossak** 51:45  
No i bardzo dobrze.

**Damian Kaminski** 51:52  
Indeksu.  
Za indeksuje zostaniemy na zielonym, czyli tak jakbyśmy kliknęli zamki należałoby tu właśnie jeszcze może dołożyć właśnie czy chcę.  
To pozostałość. No właśnie, ale zdaniem dołożymy to to według mnie musimy zdecydować, co się dzieje tu, bo to będzie zaraz nagminne, że że ten przypadek, który opisał Mateusz właśnie w błędzie, że nie tylko po podpisaniu znikają nam właśnie mamy jakiś dziwny filtr, ale też po wykonaniu akcji masowej też ten filtr będzie pozostała, więc najpierw musimy zaopiekować kwestię filtra, a później według mnie dopiero wyświetlać. Ten poparł dla spraw masowych.  
No żeby nie, nie nie storpedować sobie właśnie tutaj nie wygenerować dodatkowych zgłoszeń, że teraz coś zmieniliśmy. Ktoś kilka odśwież, a tutaj nagle wszystko znika i nie wiadomo co co za filtr jest użyt dobra to według mnie.  
Ee.  
Najpierw musimy zaopiekować tą lewą stronę.  
Dobra, przejrzę to jeszcze, jeśli tutaj tu nie ma chyba akceptant criteria, więc dopiszę i.  
I tyle, chyba na tym możemy skończyć. Chyba, że ty Łukasz coś jeszcze z tego piątkowego spotkania masz, co, co musimy zaopiekować.

**Lukasz Bott** 53:08  
Jest to sprawdźcie, czy numerek 2 2 8 1 6.  
Mają zapisane.

**Damian Kaminski** 53:15  
8 1, 6 no tak, no tylko że tu nie ma Piotra.  
To jest ten.  
Nieznany powód błędu, czyli z jakiegoś powodu przy api nie ma połączenia do bazy danych.

**Lukasz Bott** 53:24  
O k do.  
Dobra, zobacz w komentarzu, chcemy to wpisali, bo to chyba jakiś.  
Nie wiem czy to.

**Damian Kaminski** 53:37  
No trzeba podbić.  
Bo zaraz nie będzie pewnie tych wpisów.

**Lukasz Bott** 53:41  
Do jarka może zresztą do jarka to życzenie, no to może trzeba to.

**Damian Kaminski** 53:48  
No wyślę mu to bezpośrednio.

**Lukasz Bott** 53:50  
Nie no to ale nie chodzi mi o to, żeby tutaj nie zmień piotrka na jarka na blok i waiting for information tyle tak no.

**Damian Kaminski** 53:53  
Dobra.  
Dobrze.

**Lukasz Bott** 54:07  
I już.

**Damian Kaminski** 54:07  
Podejrzewam, że już jest po ptakach i.

**Lukasz Bott** 54:10  
Znaczy, no jeżeli to jest błąd taki, który się raz na jakiś czas wydarza, poza tym dzieje.  
Jeśli za chwilę zasadzie nie ma tego problemu tak, no bo to.  
Nie będzie takie wiesz.

**Damian Kaminski** 54:23  
No tak, są tylko po prostu takie komunikaty negatywne dla biznesu, tak.  
Dobra, wysyłam to na tym się dla jarka, żeby tego nie przegapił.

**Lukasz Bott** 54:32  
No.  
Czy mamy z tym coś robić tak dalej? No i tutaj faktycznie był pierd liwe.

**Damian Kaminski** 54:50  
Dobra no to chyba na tym możemy skończyć, czy jeszcze coś masz?

**Lukasz Bott** 54:55  
Nie, ja nie, nie mam. Mamy jeszcze jedno, ale to już dyskutowaliśmy, nadejdzie.

**Damian Kaminski** 54:57  
No to resztę zostawmy no.  
Dobra.  
No to dzięki. A Adrian czekaj, tylko ja spojrzę, czy ty chcesz coś jeszcze w kontekście repozytorium dyskutować czy tu już?

**Lukasz Bott** 55:05  
Dzięki.

**Adrian Kotowski** 55:12  
Będę spotkanie później tam byłeś tam 5 minut do końca, a więc tak to.

**Damian Kaminski** 55:16  
No bo ja mam teraz spotkanie z Allianz, są jakieś tam sprawie integracji?  
Dobra, to słyszymy się o dwunastej.

**Lukasz Bott** 55:25  
Na przyszłość.

**Adrian Kotowski** 55:26  
Cze.

**Damian Kaminski** 55:26  
Cześć.

**Anna Skupinska** 55:27  
No cześć.

**Janusz Bossak** zatrzymano transkrypcję
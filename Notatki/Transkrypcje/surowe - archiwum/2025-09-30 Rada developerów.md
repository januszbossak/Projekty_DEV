**Transkrypcja**

30 września 2025, 08:01AM

**Lukasz Bott** 0:18  
Jesteś?  
Stoi unia.  
Coś tam chyba chciał przedyskutować jeszcze tak?  
Generalnie radę coś zostawiamy.  
I luźno rzucony temat.  
Dobre.  
Promil tam co się nadejdzie się pojawiło, że jak się tam chcieliście temat chyba przedyskutować jeszcze coś tam z tymi kolejkami, maili.

**Kamil Dubaniowski** 0:59  
Tak kolejki maili i ta nową funkcjonalność, którą robił Piotrek, czyli historia maili wysyłanych.  
Żeby to ze sobą zgrać, ale.  
Wydaje mi się, że tutaj trzeba raczej podejść do tego w ten sposób, że.  
Żeby wysyłka maila rejestrowała się kiedy mail faktycznie zejdzie z kolejki i się wyślę, no bo.  
Bo to wydaje mi się, że że to jest takie trochę, może później powodować jakieś niepotrzebne.  
Niejasności, że jeśli coś zarejestrowało się w kolejce, ale faktycznie się nie wysłało, a my to zarejestrujemy jako wysłane, no to powiedzmy, że może mieć admin. Jakiś raport maili wysłanych taka ludzie będą mówić, że im te maile nie doszły. Admin będzie widział je jako wysłane, no bo teraz rejestrujemy jak tylko wpadną w kolejkę, więc wydaje mi się, że to jest raczej do do wyrównania.

**Lukasz Bott** 1:49  
Mhm.

**Kamil Dubaniowski** 1:55  
Wtedy nie ma, nie ma tutaj tematu usuwania z kolejki, no bo usunięcie z kolejki nie wpływa na maile wysłane.  
Bo w kolejce są tylko niewysłane tak.

**Lukasz Bott** 2:11  
Sprawdzano to pytanie, czy to nie wiem?  
Piotrek jakiś komentarz do tego.

**Piotr Buczkowski** 2:20  
To trzeba pomyśleć jak to zrobić.

**Lukasz Bott** 2:23  
Czyli niekoniecznie jest to do rozwiązania teraz na naradę.

**Anna Skupinska** 2:25  
Tak.  
Czy tu jest?

**Lukasz Bott** 2:29  
To.

**Anna Skupinska** 2:30  
Panie raportu z johnem do pola igiego.

**Lukasz Bott** 2:34  
To moja dobra, to tak ten to czekajcie wątek kolejki maili, no to co Kamil tu chyba trzeba jakieś dedykowane spotkanie tam.

**Kamil Dubaniowski** 2:34  
Jak na temat.

**Lukasz Bott** 2:42  
Zorganizować, bo kto to implementuje?

**Piotr Buczkowski** 2:43  
No nie no trzeba, bo ja to wiem.  
Trzeba typu.

**Lukasz Bott** 2:49  
To.

**Piotr Buczkowski** 2:50  
Trzeba przemyśleć jak to zrobić, tak?

**Lukasz Bott** 2:55  
No dobrze, no to w tej chwili nic zdecydujemy.

**Piotr Buczkowski** 3:04  
Może być tak, że na przykład zdarzenia.  
Zarejestrowania w kolejce jest należenie wysłaniem.  
Może tak?  
No nie było tak, że muszę się zastanowić.  
No bo to też maile wysyłane od razu tak które.  
Do kolejki mogą trafić tylko wtedy, jeżeli.  
Jeżeli się w momencie wysyłania nie da wysłać tak, z jakich powodów nie ma połączenia do serwera czy coś.

**Kamil Dubaniowski** 3:42  
No i wtedy jakby usługa odpowiada za wysyłkę, to moment wykonania usługi nie mógłby być tym momentem, kiedy dopiero trafiłem wpisy do do do tabeli wysłanych.

**Piotr Buczkowski** 3:52  
No ale tam już nie ma informacje, której sprawie to dotyczy czy coś, a to jest pers sprawa.  
Nie no tak się to zrobić, tak trzeba po prostu to, której sprawy to dotyczy czy rejestrować czy nie, bo nie wszystko rejestrujemy. Przecież tak nie w ten sam sposób.  
No dobrze to jest zastanowić.  
No tak samo.  
Ten mail zbiorczy tak.  
Ostatnio Maria zbiorcze, które powiedzmy składa usługa jeden job, tam notyfikowana job Przepraszam.  
Ale zapisuję do kolejki, którą wysyła nam tutaj taki mail już dotyczy kilku spraw.  
Tak.  
Czyli nie może być na takim mailu zapisane jeden i te sprawy?  
O tym momencie w momencie tej kompilacji tych tego maila zbiorczego zapisuje do poszczególnych spraw, że wysłano mail samo mail wysłaną mail samej tak.  
No mówię, no bo.  
Ja to no trudniejszy temat tak czy jednak?  
Nie, nie to mówienia takim tym tak trzeba najpierw.  
Zastanowić się dobrze.

**Anna Skupinska** 5:25  
Myślę, że musieliśmy przerobić.

**Lukasz Bott** 5:25  
No dobrze, no to.

**Kamil Dubaniowski** 5:26  
No tak tak, mimo jakby tego nowego zadania usuwania z kolejki, to ja myślę, że tutaj tak jest do przegadania on tak czy czy byśmy dali to usuwaniem czy nie to i tak to jest do przegadania, no bo.  
To to realnie teraz to tak jakby nie nie są prawdziwe dane, no bo te maile mogły nie wyjść, może usługa stać.  
Kolejka nie schodzi, a my będziemy mieli dane w tabeli, że wysłano.

**Piotr Buczkowski** 5:50  
No tak znaczy też wiadomo, że to my te co rejestrujemy fakt wysłania czy doszedł, to nie jesteśmy w stanie zarejestrować.

**Kamil Dubaniowski** 5:57  
Zgadza się.

**Piotr Buczkowski** 6:08  
Wyłącz.

**Lukasz Bott** 6:10  
Dobra to.

**Piotr Buczkowski** 6:10  
To może muszę się muszę się zastanowić jak to zrobić.

**Kamil Dubaniowski** 6:14  
Tak, ja ja też pamiętam, że to w ogóle jest opcja do włączenia tak że rejestrować. No więc tego na razie jeszcze nikt pewnie nie używa. Tak czy inaczej pozabija mem, jeśli tak, to w ogóle testowo ile używają.

**Piotr Buczkowski** 6:17  
Tak, tak, tak.

**Kamil Dubaniowski** 6:27  
Także na razie jeszcze mamy chwilę.

**Lukasz Bott** 6:33  
Dobra, bo tak wyrazie, jeżeli trzeba, to nie odrębne spotkanie projektowe. Tak odnośnie tego tematu i tyle.  
Że przygadać yy, jeżeli chodzi o ten temat teraz z listy dodawania możliwości zbudowania raportu zwężeniem do Polaków podnośnik to temat wyszedł w piątek na spotkanie z konsultantami.  
I według komentarza zanotowanego wygląda na tym.

**Piotr Buczkowski** 6:57  
Ale to to jest na nowej funkcjonalności, tak?  
Do nowych raportach.

**Lukasz Bott** 7:01  
No wygląda na to, że jest ona nowych wersjach, więc ja wiesz co to ja sobie to to pisałem, ja to sprawdzę, bo może tematu Nie ma faktycznie.

**Piotr Buczkowski** 7:08  
To Kamil próbował to pokazać, ale coś nie działało.

**Lukasz Bott** 7:13  
No to w takim razie, ale.

**Piotr Buczkowski** 7:13  
Kamilę Damian Damian, Przepraszam.

**Kamil Dubaniowski** 7:14  
Damian Damian.

**Lukasz Bott** 7:17  
Ale trzeba to dobrze przetestować. No to dobra, to jest sprawcy tak jeżeli jest, no to.  
Jeżeli nie działa, to i tak trzeba będzie poprawić.  
To zdjąłem z rady.  
I tutaj jeszcze jest rozszerzenie funkcji typu set coś tam fighter.  
O możliwość ustawiania pozycji w polu, gdy filtr zwraca w.

**Piotr Buczkowski** 7:49  
Seti fold tak teraz jest taka zasada, że jeżeli filtru ci nowa wartość to na zostawiane jako jako wybrana.  
Do sentra Reference, która została dodana opcja sendi fold, który można to wyłączyć i przydałoby się do tych pozostałych funkcji.  
Też zadać.

**Lukasz Bott** 8:08  
Dobra, to ja sobie to ja sobie to wezmę.  
Zweryfikuje i tyle.  
Teatr zweryfikuje. Jeżeli jeżeli już wierny sfinks jest to w podobny sposób, trzeba będzie zrobić dobra. No to tematu Nie było wysłuchać. Do koniec koniec rady.  
Chyba, że coś mamy jeszcze, a jeżeli mamy siedzieć i.  
Się gapić to nie ma sensu, dobra?

**Kamil Dubaniowski** 8:43  
Setlist część jest nieco inaczej, działa tam nie było go na liście, ale rozumiem, że jak w funkcji setlist ja sobie tam tylko jeden jedną pozycję jako list strona nie będzie automatycznie wybrana, bo to jest tylko to jest.

**Piotr Buczkowski** 8:49  
No nie.  
Szczerze mówiąc nie nie mam pojęcia.

**Kamil Dubaniowski** 8:57  
No właśnie dlatego też nie mam i chciałem, żeby tam wypali. Jak Łukasz będziesz weryfikował to jeszcze to ostatnia część to zobacz.

**Lukasz Bott** 9:02  
Dobra dopisałem sobie dobra.  
Syfilis.

**Kamil Dubaniowski** 9:09  
To nie jest filtr tak naprawdę tylko budowanie tej listy dynamicznie, ale.

**Lukasz Bott** 9:10  
O k.

**Piotr Buczkowski** 9:12  
No tak.

**Lukasz Bott** 9:18  
To jest też troszkę inaczej, bo pole typu lista zachowuje się tak naprawdę jako pole tekstowe. Tam nie, nie, nie musi, nie musi być może wpisać wartość inną niż to, co się proponuje z listy nie i też będzie zostanie zapamiętany.

**Kamil Dubaniowski** 9:39  
No dobra, to tyle chciałem.

**Lukasz Bott** 9:39  
No dobra, dobra, ale to zwrócę na to uwagę, dobrze?  
Słuchajcie kończą nie ma.  
Siedzisz?

**Kamil Dubaniowski** 9:50  
Jeszcze te referenty Square chyba doszło nowe tam od czasu zgłoszenia to mogę wejść.

**Piotr Buczkowski** 9:54  
Co tam jest, tam jest?

**Kamil Dubaniowski** 9:55  
Był dobry.

**Lukasz Bott** 9:56  
Tak był.

**Kamil Dubaniowski** 9:58  
A że dodane już jest te infor?

**Piotr Buczkowski** 10:00  
Znaczy no ma wszystkie opcje.  
A może niestety Reference query exe tak.

**Kamil Dubaniowski** 10:10  
Tak to jest to.

**Piotr Buczkowski** 10:10  
Jest.

**Lukasz Bott** 10:10  
Jeszcze.

**Piotr Buczkowski** 10:11  
Tam na pewno jest referent skóry. Jest to nie wiem.

**Kamil Dubaniowski** 10:15  
Ale to już nie ruszamy, bo to.  
Dzięki w takim razie cześć.

**Lukasz Bott** 10:23  
Dobre dzięki.

zatrzymano transkrypcję
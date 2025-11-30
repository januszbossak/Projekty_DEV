**Data spotkania:** 30 września 2025

**Łukasz Bott:** Jesteś? Stoi unia? Coś tam chyba chciał przedyskutować jeszcze, tak? Generalnie Radę coś zostawiamy. I luźno rzucony temat. Kamil, tam co się na Teamsie pojawiło, że jak się tam chcieliście temat chyba przedyskutować jeszcze coś tam z tymi kolejkami maili.

**Kamil Dubaniowski:** Tak, kolejki maili i ta nowa funkcjonalność, którą robił Piotrek, czyli historia maili wysyłanych. Żeby to ze sobą zgrać, ale wydaje mi się, że tutaj trzeba raczej podejść do tego w ten sposób, żeby wysyłka maila rejestrowała się, kiedy mail faktycznie zejdzie z kolejki i się wyśle. No bo to wydaje mi się, że to jest takie trochę, może później powodować jakieś niepotrzebne niejasności. Że jeśli coś zarejestrowało się w kolejce, ale faktycznie się nie wysłało, a my to zarejestrujemy jako wysłane, no to powiedzmy, że może mieć admin jakiś raport maili wysłanych, tak, a ludzie będą mówić, że im te maile nie doszły. Admin będzie widział je jako wysłane, no bo teraz rejestrujemy jak tylko wpadną w kolejkę. Więc wydaje mi się, że to jest raczej do wyrównania.

**Łukasz Bott:** Mhm.

**Kamil Dubaniowski:** Wtedy nie ma, nie ma tutaj tematu usuwania z kolejki, no bo usunięcie z kolejki nie wpływa na maile wysłane. Bo w kolejce są tylko niewysłane, tak.

**Łukasz Bott:** Sprawdzono to pytanie, czy to nie wiem? Piotrek, jakiś komentarz do tego?

**Piotr Buczkowski:** To trzeba pomyśleć, jak to zrobić.

**Łukasz Bott:** Czyli niekoniecznie jest to do rozwiązania teraz na Radę.

**Anna Skupińska:** Tak. Czy tu jest?

**Łukasz Bott:** To...

**Anna Skupińska:** Pytanie raportu z zawężeniem do pola odnośnik.

**Łukasz Bott:** To moja... dobra, to tak. Ten... to czekajcie, wątek kolejki maili. No to co, Kamil, tu chyba trzeba jakieś dedykowane spotkanie tam zorganizować, bo kto to implementuje?

**Piotr Buczkowski:** No nie no, trzeba, bo ja to wiem. Trzeba typu... Trzeba przemyśleć, jak to zrobić, tak?

**Łukasz Bott:** No dobrze, no to w tej chwili nic nie zdecydujemy.

**Piotr Buczkowski:** Może być tak, że na przykład zdarzenie zarejestrowania w kolejce jest zdarzeniem "wysłaniem"? Może tak? No nie, było tak, że muszę się zastanowić. No bo to też maile wysyłane od razu, tak, które do kolejki mogą trafić tylko wtedy, jeżeli się w momencie wysyłania nie da wysłać, tak? Z jakichś powodów nie ma połączenia do serwera czy coś.

**Kamil Dubaniowski:** No i wtedy jakby usługa odpowiada za wysyłkę, to moment wykonania usługi nie mógłby być tym momentem, kiedy dopiero trafią wpisy do tabeli wysłanych?

**Piotr Buczkowski:** No ale tam już nie ma informacji, której sprawy to dotyczy czy coś, a to jest per sprawa. Nie no, da się to zrobić, tak. Trzeba po prostu to, której sprawy to dotyczy, czy rejestrować czy nie, bo nie wszystko rejestrujemy przecież, tak, nie w ten sam sposób. No dobrze, to muszę się zastanowić. No tak samo ten mail zbiorczy, tak. Ostatnio maile zbiorcze, które powiedzmy składa usługa, jeden Job, tam Notification Job przepraszam. Ale zapisuję do kolejki, którą wysyła nam tutaj... Taki mail już dotyczy kilku spraw. Tak. Czyli nie może być na takim mailu zapisane jeden `ItemID` sprawy? W momencie tej kompilacji tego maila zbiorczego zapisuje do poszczególnych spraw, że "wysłano mail", "wysłano mail", "wysłano mail", tak? No mówię, no bo ja to... no trudniejszy temat, tak? Czy jednak... Nie, nie, to mówienie o takim tym, tak. Trzeba najpierw zastanowić się dobrze.

**Anna Skupińska:** Myślę, że musielibyśmy przerobić.

**Kamil Dubaniowski:** No tak, tak. Mimo jakby tego nowego zadania usuwania z kolejki, to ja myślę, że tutaj tak jest do przegadania. Tak, czy byśmy dali to usuwanie, czy nie, to i tak to jest do przegadania, no bo to realnie teraz to tak jakby nie są prawdziwe dane. No bo te maile mogły nie wyjść, może usługa stać, kolejka nie schodzi, a my będziemy mieli dane w tabeli, że wysłano.

**Piotr Buczkowski:** No tak, znaczy też wiadomo, że to my co rejestrujemy fakt wysłania. Czy doszedł, to nie jesteśmy w stanie zarejestrować.

**Kamil Dubaniowski:** Zgadza się.

**Piotr Buczkowski:** To muszę się zastanowić, jak to zrobić.

**Kamil Dubaniowski:** Tak, ja też pamiętam, że to w ogóle jest opcja do włączenia, tak, że rejestrować. No więc tego na razie jeszcze nikt pewnie nie używa. Tak czy inaczej, poza Biamem (?), jeśli tak, to w ogóle testowo ile używają. Także na razie jeszcze mamy chwilę.

**Łukasz Bott:** Dobra, bo tak w razie, jeżeli trzeba, to odrębne spotkanie projektowe. Tak odnośnie tego tematu i tyle. Żeby przegadać. Jeżeli chodzi o ten temat teraz z listy: dodawania możliwości zbudowania raportu z zawężeniem do pola typu Odnośnik. To temat wyszedł w piątek na spotkanie z konsultantami. I według komentarza zanotowanego wygląda na to...

**Piotr Buczkowski:** Ale to jest na nowej funkcjonalności, tak? W nowych raportach?

**Łukasz Bott:** No wygląda na to, że jest w nowych wersjach, więc ja wiesz co, to ja sobie to zapisałem, ja to sprawdzę, bo może tematu nie ma faktycznie.

**Piotr Buczkowski:** To Damian próbował to pokazać, ale coś nie działało.

**Łukasz Bott:** Ale trzeba to dobrze przetestować. No to dobra, to sprawdzę to. Jeżeli jest, no to... Jeżeli nie działa, to i tak trzeba będzie poprawić. To zdejmuję z Rady. I tutaj jeszcze jest rozszerzenie funkcji typu `SetListFilter` o możliwość ustawiania pozycji w polu, gdy filtr zwraca [jedną wartość].

**Piotr Buczkowski:** `SetDefault`. Tak, teraz jest taka zasada, że jeżeli filtr zwróci nową wartość, to ona zostaje jako wybrana. Do `SendReference` chyba została dodana opcja `SetDefault`, którą można to wyłączyć i przydałoby się do tych pozostałych funkcji też dodać.

**Łukasz Bott:** Dobra, to ja sobie to wezmę. Zweryfikuję i tyle. Tak zweryfikuję. Jeżeli już w jednym z funkcji jest, to w podobny sposób trzeba będzie zrobić. Dobra. No to tematu nie było. Koniec Rady. Chyba, że coś mamy jeszcze? A jeżeli mamy siedzieć i się gapić, to nie ma sensu, dobra?

**Kamil Dubaniowski:** `SetList` też jest nieco inaczej, działa. Tam nie było go na liście, ale rozumiem, że jak w funkcji `SetList` ja sobie dam tylko jedną pozycję jako listę, to ona nie będzie automatycznie wybrana, bo to jest tylko... to jest...

**Piotr Buczkowski:** No nie. Szczerze mówiąc nie mam pojęcia.

**Kamil Dubaniowski:** No właśnie dlatego też nie mam i chciałem, żeby tam wypalić. Jak Łukasz będziesz weryfikował to jeszcze to ostatnie, też to zobacz.

**Łukasz Bott:** Dobra, dopisałem sobie. Dobra. `SetList`.

**Kamil Dubaniowski:** To nie jest filtr tak naprawdę, tylko budowanie tej listy dynamicznie, ale...

**Piotr Buczkowski:** No tak.

**Łukasz Bott:** To jest też troszkę inaczej, bo pole typu Lista zachowuje się tak naprawdę jako pole tekstowe. Tam nie musi być... może wpisać wartość inną niż to, co się proponuje z listy, nie? I też zostanie zapamiętany.

**Kamil Dubaniowski:** No dobra, to tyle chciałem.

**Łukasz Bott:** No dobra, dobra, ale to zwrócę na to uwagę, dobrze? Słuchajcie, kończymy, nie ma [co].

**Kamil Dubaniowski:** Jeszcze te `ReferenceQuery`, chyba doszło nowe tam od czasu zgłoszenia, to mogę wejść?

**Piotr Buczkowski:** Co tam jest? Tam jest?

**Kamil Dubaniowski:** Był dobry.

**Łukasz Bott:** Tak, był.

**Kamil Dubaniowski:** A że dodane już jest `ThrowError`?

**Piotr Buczkowski:** Znaczy no ma wszystkie opcje. A może w `ReferenceQueryEx`, tak?

**Kamil Dubaniowski:** Tak, to jest to.

**Piotr Buczkowski:** Jest. Tam na pewno jest `ReferenceQuery`. Jest, to nie wiem.

**Kamil Dubaniowski:** Ale to już nie ruszamy, bo to [jest]. Dzięki w takim razie, cześć.

**Łukasz Bott:** Dobra dzięki.

**Kamil Dubaniowski:** Teraz jeszcze na końcu tak się skupiłem, jak powie...
Jak sytuacja, kiedy wrzuciłeś 10 plików, one się jeszcze ładują i dorzucasz kolejnych 5?
To w ramach tej sesji doda się kolejnych 5 czy...?

**Damian Kamiński:** Nie ma takiego przypadku, nie zrobiliśmy.

**Janusz Bossak:** Trzeba czekać.
Znaczy można by zrobić tak, żeby rzeczywiście jak się ładują, to nie można dorzucić, trzeba poczekać aż się skończą, no.

**Damian Kamiński:** No robi się oddzielna sesja.
No ale to tak frontend jest w stanie to wykryć, więc...

**Janusz Bossak:** Jeżeli tak można i tutaj widać, że się dołożyły. No to może być, że to jest ciągle trwająca ta sesja jedna, nie.

**Damian Kamiński:** Tak, ja wręcz się zastanawiam, żeby z kolei ktoś tego nie wyłączył prawym sidebarem, klikając tak i przykryje...
To, że ładuje tym zapomni się rozłączy, może w ogóle powinniśmy wtedy tutaj dać to ładowanie, a tu wyszarzyć cały ten ekran miał wtedy nie będzie miał tej opcji wynikającej z przeciągania, tak i ten i ten Dodaj plik ten tak, tak.

**Janusz Bossak:** Dokładnie, bo trwa synchronizacja tego.
Tak trwa synchronizacja tego co robi nie.
Natomiast przy tych długo trwających może mieć sens, bo tutaj patrzę, że są te iksy tam nie.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Może mieć sens właśnie wtedy taki X, bo rozumiem, że teraz po tej patrzę na tą lewą stronę gdzie się tam ładuje. Ten Deloitte mówię: o kurde tego nie chciałem ładować, tego MP4, no i teraz jak tego X-a nacisnę to się skończy i to ładowanie przerwie.

**Damian Kamiński:** Mhm. Nie w wyniku, ale czy przerwało to nie wiem.

**Janusz Bossak:** No to trzeba by rozważyć, bo to może być nie mogłem wychwycić plik, który go nie chce ładować.

**Damian Kamiński:** Zaraz to sprawdzimy.
Jeszcze raz zrobimy to.
X-a nie zdążymy, jeszcze raz.
Nie wiem, jeszcze raz.

**Janusz Bossak:** [Musisz] wrócić na pustym, na pustym folderze, wziąć nie?

**Damian Kamiński:** Tak, tak, tak, tak.
To jeszcze jakiś błąd tym?
Wybraliśmy ten większy.
Żebym... Ha widzisz nie ma X-a, bo tam były jakieś artefakty widocznie przez to, że wyświetlamy kilka... Nie ma X-a jak ładuje.
Nie możesz przerwać.
X się pojawia dopiero po zakończeniu uploadu.
No i to jest chyba OK w ramach MVP.
Teraz inne pytanie jesteście?

**Janusz Bossak:** Tak, tak no.

**Damian Kamiński:** Inne pytanie.
Wgrałem to wszystko.
Jak się okazuje kurde to nie to, no i teraz to robię:
Usuń.
Usuń.
Usuń... Nie mogę skasować inaczej, tylko tak: nie mogę skasować folderu póki nie usunę wszystkich. Na razie jest takie zabezpieczenie.
No właśnie więc pytanie, czy robimy jakąś formę?
Tutaj nie wiem, checkboxa "zaznacz wiele" i wtedy pojawia się akcja, że do tych wielu może usunąć?

**Janusz Bossak:** A co było opisane w MVP 1?

**Damian Kamiński:** No podeszliśmy do tego w MVP 1, to znaczy nie było to w ogóle zaopiekowane. Było opisane tak, że nie da się usunąć. Nie było opisane. Mówisz o naszym czy o [firmowym]?

**Janusz Bossak:** Znaczy nie rozumiem czym się różni [nasze]...

**Damian Kamiński:** Może inaczej: o wymaganiach firmowych czy o naszym MVP? W naszych wymaganiach MVP nie było to.
No jak powiem, nie przewidziałem takiego przypadku. Dopiero jak zacząłem z tego korzystać to dopiero mi się to uwydatniło, że teraz nie mogę usuwać. Było tak, że po prostu nie możesz usunąć folderu, jeśli w folderze znajdują się jakieś podrzędne rzeczy, tak, czyli albo folder albo pliki.

**Janusz Bossak:** Na ten moment zrobiłbym, owszem, usuwanie pliku można usunąć.
Ale pojedynczego.
Natomiast zbiorczo no to... no to zbiorcze zostawiamy na MVP 2.

**Damian Kamiński:** No to to jest... to to jest...
Czytam nawet już [MVP] 3, no ale OK, to znaczy no dobra, to zależy jak to rozumiecie. No dobrze, bo moglibyśmy w zasadzie to robić, bo to jest tylko frontend.

**Janusz Bossak:** No to musisz ocenić, czy mamy przestrzeń i nie wiem co tam Filip tym zajmuje. Jeżeli tak no to możemy zrobić, no jeżeli...

**Damian Kamiński:** Dobra.
Tylko pytanie, Kamil masz no to jakiś pomysł w kontekście takim wizualnym czym się mogę wzorować? Czy tu trzeba to wymyślić po nowemu?
Gdzieś coś takiego kojarzę, że mamy?

**Kamil Dubaniowski:** Czy no mamy tylko zaznaczanie na raportach wszystkiego, no i lub wybranych, to musiałby być checkbox, albo możemy iść w standard, czyli Ctrl+Click w tym powinien działać.
Bo wydaje mi się, że na Googlu, no innych takich typowo aplikowanych tematach działa.

**Damian Kamiński:** No właśnie ja też się wzoruje trochę OneDrivem.

**Kamil Dubaniowski:** Spodziewam się, że tam nie ma też checkboxa do akcji masowych, ale jak zaznaczysz pierwszy i z Shiftem [ostatni] pójdzie gdzieś tam niżej.

**Damian Kamiński:** To się otwiera, nie, bo zależy chyba jak wyświetlisz tak. O, jak wyświetlam kafelkowo to można wejść, a można po prostu zaznaczyć w ten sposób i tu wtedy pojawiają się te akcje masowe i na przykład.

**Kamil Dubaniowski:** OK, raz się pytam wtedy jak...

**Damian Kamiński:** Ale poczekaj teraz jak damy listę dla porównania, no to tu po prostu się pojawiają, nie?

**Kamil Dubaniowski:** No i zaznaczysz pierwszy?

**Damian Kamiński:** A Shiftem już powiem, już powiem.
No tak, jakoś działa, tylko tu pewnie nie złapało dokładnie tego co co miało złapać, czyli pierwszy i Shiftem.
To znaczy o wiele...

**Kamil Dubaniowski:** A na samej górze jest przycisk do zaznaczenia wszystkiego?

**Damian Kamiński:** Tylko...
Jest.

**Kamil Dubaniowski:** No to jakby [wziąć] przed nim na wzór raportu w ten... Nawet może kiedyś dodać i do raportów, ale na razie checkboxy i "zaznacz wszystko" na to.

**Damian Kamiński:** To Shift był w raportach? Ja nie wiem czy on jest, ale on był na pewno.
Czyli tak samo to zrobić? Na podglądzie pojawia się ikonka checkboxa?

**Kamil Dubaniowski:** Że nachodzę...

**Damian Kamiński:** No na row-erze [wierszu].

**Kamil Dubaniowski:** No tak i wtedy można by te w raportach też w sumie zrobić, bo teraz ona świeci tam cały czas na wszystkich.
Bo nie ma innego sposobu, no mamy już też jakby [checkb]oxy, używamy ich, jest opcja zaznacz wszystko, nie tylko tutaj.
Nic nowego nie wymyślimy.

**Damian Kamiński:** No dobra.
Czy coś jeszcze chciał?
No dobra, chyba na ten moment to wszystko. Jak to jest zaraz, bo wysyłałem wam chyba. Aha dobrze, a z tym ładowaniem?
Z tym ładowaniem już wam pokazuje.
Czy to też wymyślać coś nowego, czy?
Taką chmurkę mamy na sprawie.
Mamy tak.
Przysłania "Upuść pliki tutaj".
Czy czy zostajemy z taką chmurką? Jak jest na sprawie? Bo to jest tak bardzo sprawy? Tak? Czy w ten sam sposób robimy tu?

**Janusz Bossak:** A nie taka czarno-pomarańczowa?

**Damian Kamiński:** Nie tam jest pomarańczowy, tylko napis "Wybierz", to jest, a my mamy to, a my mamy to tutaj "Dodaj pliki" po prostu, bo no, bo to nie ma sensu, tak, to to musi się wyświetlać tak jak tu, więc u nas to jest tu, a jak już przeciągasz, no to wtedy jest zdarzenie.

**Janusz Bossak:** No właśnie.

**Damian Kamiński:** Już wynik zdarzeniowy, tak.

**Janusz Bossak:** Znaczy tak.
Tutaj jest trochę sytuacja inna, zresztą tam nie wiem czy wtedy nie jakoś nie, nie umieliśmy, nie, nie wiem z czego to wyniknęło, ale tak jak widzę Teamsy czy inne rozwiązania to to kratkowane pole do upuszczenia one traktują zawsze jako cały tą przestrzeń, tak, czy nie muszę tam trafiać w środek tego.
Tutaj tak nie jest właśnie, nie.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Bo tu jakby się to na stałe wyświetla tak?
Żeby...

**Damian Kamiński:** No trzeba w to miejsce najechać, tak, ale to też jest nie jest tragiczne.

**Janusz Bossak:** Ale też mogłoby być tak tutaj, to już jest inny w ogóle wątek, ale mogłoby być tak, że jak jadę i przeciągam coś, to mi się cały ten prawy panel jakby robi takim miejscem na upuszczenie, a w tym przypadku repozytorium no to jest jakby oczywiste, tak mogłoby być tak. Czyli jak sobie to przeciągam, jakbyś otworzył 2 okienka Windows, nie wiem czy na Windowsach tak to działa i jakbyśmy między okienkiem Windowsów a okienkiem Windowsów przeciągał pliki, czy tam się pojawi?
Przestrzeń na całym okienku, że można upuścić.

**Damian Kamiński:** Już pokazuję.
To znaczy nie wiem jak jaki będzie efekt, ale zrobić tak oczywiście można.

**Janusz Bossak:** Tak tutaj ciągniesz.

**Damian Kamiński:** Tylko czekaj, czekaj, muszę tu wziąć coś inny folder, bo to jest ten sam, gdzie jest moje temu... OK, no dobrzy i mamy tak, nie tu się nic nie pojawia, to po prostu puszczam.

**Janusz Bossak:** Nic się nie powiem [nie pojawia].

**Damian Kamiński:** I się przeniosło.

**Janusz Bossak:** Znaczy no różne są jakby techniki, tak. No Teams sobie ostatnio, już od dłuższego czasu tak się dzieje, zresztą tamte wszystkie: ChatGPT, Gemini, inne też jak przeciągam pliki, to się ta przestrzeń cała tak wyraźnie podświetla, że tutaj mogę upuszczać.
Więc.
Znaczy po prostu nie?
Nie bardzo jest jakby wytłumaczalne, dlaczego to jest takie małe, tak i dlaczego miałbym trafić tam na środku ekranu?

**Damian Kamiński:** Ale to teraz mówisz o sprawie? No tak, odnosisz się, czy że można to by...

**Janusz Bossak:** O sprawie i o repozytorium, no bo teraz repozytorium mam takie jakby na środku tylko ten prostokącik. No widzisz tu mogę puścić gdziekolwiek nie.

**Damian Kamiński:** Tak.

**Janusz Bossak:** Właśnie o to mi chodzi. Jeżeli teraz w tym repozytorium, które projektujesz tak jest, [to] znaczy, że się wyświetla tam na środku zachęta do upuszczenia, ale mogę puścić tak jak teraz to robisz.

**Damian Kamiński:** No trzeba w tym obszarze roboczym, nie można tu, ale jak tu to gdziekolwiek, tak, to bo to po prostu najeżdżamy na tą ramkę i się pojawia, że można upuścić.

**Janusz Bossak:** A mi chodzi o to, że może te pomarańczowe kropeczki powinny być wokół całego tego obszaru, który jest teraz wyszarzony i tylko na środku taki napis "Upuść pliki tutaj", tak i gdziekolwiek puścisz to będzie działać.
Tak.

**Damian Kamiński:** Mm.

**Janusz Bossak:** Bo teraz to muszę, muszę trafić w ten pomarańczowy prostokąt.

**Damian Kamiński:** Nie, nie, nie, absolutnie, nie, nie, to jest tylko informacja.

**Janusz Bossak:** To właśnie oświadczenie, tak znaczy, on mi sugeruje, żebym trafił nie tam w to.

**Damian Kamiński:** No dobra, to wykasujemy w takim razie prostokąt, skoro on Cię sugeruje, bo dopiero teraz zrozumiałem o co Ci chodzi. Czyli jeszcze raz tak jak Claude ma to w ten sposób.
No to po prostu najeżdżam i po prostu jest tylko ikona nie ma ramki.

**Janusz Bossak:** No widzisz, to wszystko, ale jest, ale widzisz na środku jest jakaś tam ikona "Drag files here" nie i to niech tam zostanie tak jak ty masz to napisane.

**Damian Kamiński:** No tak.
Tak tylko nie będzie tej ramki tak, czyli będzie...

**Janusz Bossak:** Jeszcze raz.
Tylko ramki... ramka może być nawet, ale wokół całej tej szarości nie.
Czyli tutaj u nas. Zobacz, jak widzisz to się wszystkie...

**Damian Kamiński:** OK.
Rozumiem, po prostu tutaj obramować to całość, tak?

**Janusz Bossak:** Tak jest, tak, jest. Tam gdzie się robi szarość, to to ta ramka była inna, [a na] środku niech będzie "Upuść pliki tutaj" tam "Upuść pliki aby je przesłać", nawet może być ikonka tak jak tutaj było w Cloudzie taka taki symbol tam pliku.

**Damian Kamiński:** Znaczy, no właśnie pytanie czy bo to to to jest moje pytanie, czy robimy spójne z ikonką jaka jest na sprawie, czy robimy nową?

**Janusz Bossak:** OK.
Można tą wziąć, no może wziąć to i to na środku właśnie tam napisać.

**Damian Kamiński:** Dobra, czy po prostu ta ramka ma być po prostu na całą tę pole?

**Janusz Bossak:** Tak.

**Damian Kamiński:** OK.
Dobra tyle.

**Janusz Bossak:** Bo chyba tutaj ta na na sprawie też ona kolor zmienia, kolor taki wódki [?] dostaje.

**Damian Kamiński:** Ona nie, ona takiego robi. Taki "bounce" to chyba się nazywa, czyli czyli o powiększa [zoom in].

**Janusz Bossak:** Rozumiem, no no to można by tutaj też dodać ewentualnie taką rameczkę, żeby ona tam się robiła, ale to słuchajcie to są takie drobiazgi, że tam... ale [w] dbałości o jakby spójność wizualną, warto o to też zadbać.

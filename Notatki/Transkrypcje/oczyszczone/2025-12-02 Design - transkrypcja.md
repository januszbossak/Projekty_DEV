**Data spotkania:** 2 grudnia 2025, 11:01

---

**Janusz Bossak:** Sam jesteś.

**Kamil Dubaniowski:** Całość. Tak patrzyłem na skład – wszyscy na czerwono.

**Janusz Bossak:** Byłem na tym menedżerskim spotkaniu.

**Kamil Dubaniowski:** Nie będzie Łukasz. Może nam się uda coś ustalić wspólnie, bo chciałbym ten prawy panel omówić. To już to, co potwierdziłem, rozpisał Przemkowi, jak wróci, żeby miał co robić. Nagrywanie najwyżej się podniosą. Spisałem sobie tam na razie taką listę, co chciałbym ustalić. Jeszcze nie zagłębiałem się w same ustawienia poszczególnych typów pól, bo to pewnie więcej roboty na start. Chciałbym zrobić taki bardziej ogólny przegląd tego. Co pierwsze – ustalimy ten nagłówek. Chciałbym omówić te punkty, czy akcje: zarządzanie, widocznością i usuń, przenosimy do nagłówka. To jest to, co zaczęliśmy kiedyś dyskusję. Pamiętam, że specjalnie dzieliłeś tutaj osobną sekcję na te dwie akcje. To jest zarządzanie polem.

**Janusz Bossak:** Mhm.

**Kamil Dubaniowski:** Dlaczego mi się to trochę nie klei? Sam ten panel to już jest zarządzanie polem, w którym wydzielamy zakładkę zarządzanie polem i tam są tylko dwa przyciski akcji: usuń lub zmień typ pola. Zmianę typu pola, to co zasugerowałem, od razu bym widział tutaj. Już robimy tego typu przyciski. Pokażę, jak to wygląda. Więc to byłoby pierwsze, co możemy ustalić. Aby zmienić typ pola, muszę przejść tutaj do "Zarządzaj" i mam "Zmień typ pola". Czego aktualnie nie ma, to po pierwsze powinniśmy dodać, żeby tutaj był widoczny typ pola jako informacja w danych podstawowych i obok tego akcja, tak jak tutaj te wersje językowe, po prostu ołówek (edycja) do zmiany typu pola. Ona wywoła to samo okno, co wywołuje się teraz, czyli to z tym ostrzeżeniem i zapisem.

**Janusz Bossak:** Może być. Może ta sekcja powstała, bo nie miałem innego pomysłu.

**Kamil Dubaniowski:** Rozumiem. Ale wtedy też nie było tyle akcji.

**Janusz Bossak:** Wtedy odkryłem, że patrząc na listę pól, tą, którą normalnie mamy po staremu, to tam jest taki przycisk, jak "Zmień typ pola".

**Kamil Dubaniowski:** My to zrobiliśmy i byłoby nawet spójnie, tak. No bo teraz to wygląda w ten sposób: jest ten edytuj przy typie. Można to zrobić z listy, ale żeby ktoś się odnalazł, jeśli nauczy się już tego prawego panelu, to będzie mu wygodniej. Będzie typ pola i taki sam edytuj po prawej. Oczywiście opcja tylko do odczytu. Edytuj dopiero pozwala coś zmienić.

**Janusz Bossak:** Mam tylko taką uwagę, jak tu pokazałeś w tej kolumnie "Typ", żeby tam się ten ołówek pokazywał. Ja mam takie odczucie UX-owe, że rzeczy, które są destrukcyjne, nie powinny być łatwo dostępne. Takie coś zachęca użytkownika, że to zaraz sobie kliknie i coś zmieni, a architektura **AMODIT** jest taka, że zmiana typu pola jest bardzo, w niektórych przypadkach, destrukcyjna. Wiąże się ze zmianami w bazie danych, z przypisywaniem, z obciążeniem serwera i z wieloma innymi rzeczami.

**Kamil Dubaniowski:** Rozumiem, dlaczego to robię. Bo tak było. Zmiany typu pola można było zrobić z listy.

**Janusz Bossak:** Nie, nie, nie. Nie tak było. Trzeba było zaznaczyć i wejść u góry "Zmień typ pola", więc trzeba było wykonać kilka czynności, które do tego prowadziły. Nie mówię, że to było dobrze czy źle, ale mówię o sytuacji takiej, jak tutaj ładnie jest prezentowane. To są czynności, które zachęcają do kliknięcia.

**Kamil Dubaniowski:** Zaznaczyć i tu się aktywował przecież.

**Janusz Bossak:** Tym mnie do kliknięcia. Z ciekawości kliknąłem. Przy tym typie trochę mam obawę.

**Kamil Dubaniowski:** Czy to też jest teraz wielopoziomowy, zrobione w sensie, że nic się nie wydarzy, jak kliknę. Zastanawiam się, bo znów dwie perspektywy: nasi konsultanci i ci, którzy pracują dopiero nad procesem, tam zmiana typu. Spodziewam się, że może nie jest super częsta, ale się zdarza. Serwis raczej tego nie powinien nawet używać.

**Janusz Bossak:** To jest na produkcji.

**Kamil Dubaniowski:** I klient to samo.

**Janusz Bossak:** Dlatego mówię, to nie jest źle, tylko mam takie obawy, że to jest wyeksponowane.

**Kamil Dubaniowski:** Dobra, parkujemy. Ja to zgłoszę Filipowi, żeby potencjalnie, jeśli będzie już w prawym panelu (bo do tej pory jeszcze tego nie mamy), to wtedy u Filipa to wywalimy. Dla mnie okej. Tę zmianę typu robię bardzo rzadko, ewentualnie gdzieś tam na procesach demo, jak coś klientowi prezentuję.

**Janusz Bossak:** To ma być dostępne, ale właśnie nie zachęcające.

**Kamil Dubaniowski:** Dobra. Ta opcja, że idzie to tutaj obok, jest okej. Nie możemy tego aż tak bardzo ukrywać. Wiem, że to jest akcja mało używana, ale tym bardziej powinna być intuicyjna. Jeśli chcę zmienić typ pola, to szukam informacji na temat aktualnego typu pola i przy tym mam potencjalnie ten edytuj z ostrzeżeniem, tak jak jest. Jak to ukryjemy za bardzo, to przez to, że to jest bardzo rzadko używana akcja, to będą szukać, tracić czas.

**Janusz Bossak:** Tu można pomyśleć w ogóle, to już trochę odbiegam, że zmiany na produkcji. Tylko musielibyśmy jakoś odróżniać, że to jest produkcja, a to jest środowisko testowe. Może powinno być w ogóle jakoś bardziej restrykcyjne.

**Kamil Dubaniowski:** Tak, żeby ten.

**Lukasz Bott:** Zasady.

**Janusz Bossak:** Tak, że niestety definicji procesu. Mamy ten problem, że to się dzieje od razu, czyli jak ktoś zmieni, to natychmiast ta zmiana jest. Nie mamy tej warstwy bufora.

**Lukasz Bott:** Tryb publiczny?

**Janusz Bossak:** Tak, nieopublikowane i opublikowane.

**Lukasz Bott:** Opublikowania w tym sprincie?

**Janusz Bossak:** Gdyby to się nam udało wprowadzić, byłoby super, ale to jest odrębny temat do przemyślenia.

**Lukasz Bott:** Szkic.

**Janusz Bossak:** Publikowanie zmian. Pamiętam, jak robiliśmy pierwszy edytor graficzny formularza, ten poprzedni. Też była ta koncepcja i nie bardzo się dało ją ograć w tych strukturach, które mamy. Odpowiedź działa w swoim założeniu i trudno jest to zmienić.

**Kamil Dubaniowski:** Dobra, to pierwsze ustalenie mamy. Chciałbym wrócić do drugiego przycisku, bo celem moim jest, żeby tych sekcji było mniej, żeby jak najwięcej zmieścić bez konieczności rozwijania. Piotr też wnioskował o to, ale to będzie dalej wychodziło. Zobaczymy, ile z tego się da wyczyścić. Zostaje nam akcja usuń pole w tej sekcji, bo to już przejdzie tam poziom wyżej obok typu pola, żeby było logicznie powiązane. Zostaje nam to usuń pole. Opcja: albo możemy mieć to gdzieś na samym dole tego panelu (tak mamy zrobione w raportach), albo druga propozycja, którą firma mi tu wrzuciła, to jeśli idziemy już, że akcje są w górnej belce, to akcja usunięcia jest w górnej belce, tylko na plus/minus. Trzeba po prostu wiedzieć, że tutaj trzeba szukać, ale to też nie ma być jakoś super eksponowana akcja, bo te pola też raczej usuwamy rzadko. Na etapie projektowania zdarza się częściej niż u klienta produkcyjnego. Wdrożeniowcy będą musieli wiedzieć, że tak to jest tu ukryte. Da się chyba bardziej intuicyjna, bo ktoś może nie wiedzieć, czy powinien się przeskalować na sam dół, żeby znaleźć tą akcję. Tutaj pewnie zerknę, co jest i znajdę. Nic to też do decyzji, bo chciałbym się tej sekcji pozbyć, a dąży do tego, żebyśmy zostali z trzema sekcjami. Aktualnie mamy ich w skrajnych sytuacjach sześć albo pięć.

**Janusz Bossak:** Okej.

**Kamil Dubaniowski:** Zobaczymy, co.

**Janusz Bossak:** Zobaczymy. Obawiam się, że to jest UX. Każdy ma inne ścieżki, inne przyzwyczajenia. Jedni wolą tak, inni inaczej. Możemy to przesuwać, raz tu, raz tam, ale trzeba dać to pod dobrze.

**Kamil Dubaniowski:** Czy to jest tyle intuicyjne i znane, bo tak samo usuwa się załączniki na formularzu.

**Janusz Bossak:** Ale na przykład dzisiejsza rozmowa. Nie wiem, czy tam byłeś. To "usuń" na sprawie.

**Kamil Dubaniowski:** Nie byłem na rozmowie, ale kojarzę.

**Janusz Bossak:** Propozycja padła taka, żeby na ten przycisk "Usuń" na pierwszym etapie, tak jak to normalnie w **AMODIT** jest, był widoczny dla wszystkich i usuwał sprawę. Natomiast na kolejnych etapach, tak jak kiedyś było po przekazaniu, to dla zwykłych użytkowników on znika, a dla administratorów jest w trzech kropkach.

**Kamil Dubaniowski:** Okej.

**Janusz Bossak:** Żeby nie był ciągle widoczny, bo jest zgłoszenie związane z tym, że on w ogóle nie występuje dla spraw zamkniętych.

**Kamil Dubaniowski:** Zamkniętych.

**Lukasz Bott:** Tak.

**Janusz Bossak:** I przy okazji jest koncepcja, żeby jednak go właśnie przenieść pod te trzy kropki. Czerwono może być.

**Kamil Dubaniowski:** Mogłoby być, żeby to jeszcze wyróżnić, że to jest "Usuń administracyjnie" albo coś w tym stylu, żeby miał świadomość.

**Janusz Bossak:** Na czerwono niech będzie, że to jest "Usuń sprawę".

**Lukasz Bott:** To usuń sprawę, tak jak dotychczas było.

**Janusz Bossak:** Kiedyś było w tym panelu, klienci mają zastrzeżenia, że tego nie ma. Tam było na czerwono. Daliśmy im, że jest w trzech kropkach i jest czerwony. To jest ten sam, który był tam. Dzięki temu administratorzy będą rozumieli, że to jest ten przycisk.

**Kamil Dubaniowski:** Ma sens i wtedy spina się z tym. Dobra, czyli rozumiem, że to możemy zatwierdzić. Mogę to już zgłaszać, że przenosimy ten przycisk.

**Janusz Bossak:** Dobra.

**Kamil Dubaniowski:** Usuń. Kolejny temat, właściwie powiązany z tym wyżej: zarządzanie widocznością. To jest kolejna zakładka. Wracamy do tego, co jest. Widoczność. Mamy plus przycisk. To są właściwości, tak samo jak są właściwości: czy pole ma być długiego tekstu (pięcio- czy dwuliniowe). Tak samo dla mnie właściwością jest, czy ma być na listach, czy dostępne w raportach, czy jest polem systemowym. Wiem, że to pewnie bardziej się wiąże do tych do czynności uprawnień. Rozumiem, żeby jeszcze ich nie mnożyć. Spodziewam się, że na spokojnie to jest na tyle rzadko używane, że jeśli spakujemy to do ogólnej zakładki właściwości pola i te właściwości po prostu będą dla wszystkich pól zawsze. Nie stracimy za dużo. Pozbędziemy się tej zakładki, a zarządzanie uprawnieniami zaplanowałem, żeby było w tej walce akcji, tak jak już wszystko. Wyskakuje mi tutaj pseudo okienko, ale powinno mi wyskoczyć to okno po kliknięciu oczka. Te opcje przenosimy do właściwości pola, do zakładki z właściwościami.

**Janusz Bossak:** To oczko, gdzie ono się teraz pojawia?

**Kamil Dubaniowski:** Aktualnie tutaj go nie ma. W projekcie jest w górnej belce. Zasymulował jakieś tam inne okno uprawnień. Docelowo tutaj zarządzaj widocznością.

**Janusz Bossak:** Może być tutaj, ale też jak mamy listę, to tak.

**Kamil Dubaniowski:** To Mateusz sugerował i ono jest ukryte, bo uważam, że tam nie ma sensu wywalać tych akcji.

**Lukasz Bott:** Czekaj, bo tutaj trochę taka niekonsekwentność w nazewnictwie. Projekt używa "widoczność", ale rozumiem, że tu chodzi o uprawnienia.

**Kamil Dubaniowski:** Przemek podważył.

**Janusz Bossak:** To jest dyskusja ciągła. Czy to są uprawnienia? To nie są uprawnienia, to jest widoczność. Mówisz, że to jest wymagane albo niewymagane, albo jest tylko do odczytu. Jakie te uprawnienia są? Sposób wyświetlania.

**Lukasz Bott:** W tym sensie, okej.

**Janusz Bossak:** Bardziej nawet nie.

**Lukasz Bott:** Nie, nie, bardziej mi chodziło o konsekwencje w sensie używania terminologii.

**Janusz Bossak:** Tak, żebyśmy nie. Pojawia się jakiś element uprawnień w tych wyjątkach, które są pod spodem, że widoczny tylko dla albo edycja tylko dla.

**Kamil Dubaniowski:** Mogłoby być tak: widoczność i uprawnienia, tak sklejone. Mimo wszystko.

**Janusz Bossak:** Zostawiłbym ze względu na historyczne.

**Lukasz Bott:** Tak, nie wiem. Chciałem powiedzieć, że słowo "uprawnienia" już funkcjonuje w takim kontekście.

**Janusz Bossak:** Nawet jeżeli nie jest do końca tym, czym powinno być, to ponieważ 15 lat tak mieliśmy, to niech to zostanie.

**Kamil Dubaniowski:** Dobra, czyli zgadzamy się, że to może być ta akcja typu "oczko". Idziemy spójnie, bo to będzie też tutaj w tym menu dostępne. Zmieniamy tutaj tooltip na "Zarządzaj widocznością i uprawnieniami".

**Janusz Bossak:** Tak.

**Lukasz Bott:** Jest kolejnym w kolejności. W formularzu masz widoczne kwestie związane z widocznością bądź niewidocznością. Te uprawnienia to są te specyficzne pola. Widoczność i uprawnienia, może tak być.

**Kamil Dubaniowski:** Prawnie nie widać. Tak.

**Lukasz Bott:** A to, co tutaj masz opcję widoczności, to do ustawień pola. Ja bym to wrzucił faktycznie.

**Kamil Dubaniowski:** Wiemy, że to ma jakiś wpływ, bo niedostępne w raportach to wcale nie znaczy, że ja nie mam dostępu do tego pola. Nie mogę go po prostu jako twórca używać w raportach. Z jakiegoś powodu zazwyczaj chodzi o to, że jest to pole techniczne. To jest właściwość pola. Nie chcę mieć w raportach, żeby ludzie go nie wykorzystywali.

**Lukasz Bott:** A to w końcu zweryfikowałeś? To niedostępne w raportach. W pole systemowe, czym to się różni?

**Kamil Dubaniowski:** Tego nie ogarniałem, co robi dokładnie pole systemowe. Zatrzymałem się na tym poziomie, że to jest głównie do podpisów. Niedługo sikałem tego tematu.

**Lukasz Bott:** To na pewno było coś z kwestiami integracyjnymi, podpisami integracyjnymi. Już ono jest ignorowane i coś ma jeszcze wpływ na wyszukiwanie czy właśnie, że nie jest wyszukiwane, nie jest indeksowane. To ma szersze zastosowanie.

**Kamil Dubaniowski:** Moim zdaniem, jak będziemy robić rewizję w ogóle tych nazw ustawień, to warto by było dać jakąś informację, co to robi. Pokaż na listach też nie jest jasne. Nie wiem, o co chodzi. Jako pierwszy kontakt nie wiem, na jakich listach, o jakiejś ci chodzi. Mi się tu pokaże, jak ja to wyłączę. Wszystkie opcje będzie trzeba sensownie opisać. Na razie ustalmy ich lokalizację. Zrobimy to w drugim kroku. Decydujemy się, że to idzie do góry.

**Kamil Dubaniowski:** Czynności prawne. Do nagłówka. Jeżeli powyższe "na tak", to właśnie gdzie przenieść pole systemowe widoczność? To do właściwości. Myślę, że będzie dobrze. Zobaczymy. Ja jeszcze to przerobię na koniec i obejrzymy sobie projekt zanim to polecam Szymkowi. Wydaje mi się, że będzie to raczej logiczne, tam w niedzielę po prostu taką podsekcję. Tego typu chyba, że sklei się to z jakimś innym ustawieniami tematycznie. Akcja historia i otwieranie panelu reguł. To też przewidziałem. Po prostu idąc za ciosem w tym nagłówku. Chciałem to potwierdzić. Dla tabel reguły tabeli są dostępne też tutaj. O tyle wyjęliśmy to na wierzch. Mniej się kojarzy, bo wcześniej trzeba było wejść do tabeli, żeby te reguły odpalić. Znałem to na wierzch. Może później, jak się już nauczą, to będzie można coś z tym pomyśleć. Historia pola. Aktualnie na tym widoku edytora graficznego w ogóle nie mamy tej funkcjonalności, więc trzeba będzie dodać, bo Przemek tego nie zrobił na starym edytorze graficznym. Nie zrobił też na nowym, więc trzeba dodać, żeby się wyświetlało to w ogóle i akcje. Chodziło o to, że nie jest super używana, ale jest dostępna.

**Janusz Bossak:** Na liście jest też pod tymi trzema kropkami. To bardzo dobrze wygląda. Wszystkie.

**Kamil Dubaniowski:** Tak. To jest zgłoszenie jeszcze z czasów, kiedy dziewczyny zaczęły to testować graficznie. Dorzucę do tego, jak to działa aktualnie. Graficznie nie wiedziały, jak dodać nowe pole do tabeli. Robiły tak i zgłosiły, że nie działa. Dopiero później wyłapały, czy ktoś inny zasugerował, że to akcja "Edytuj pola tabeli". Efekt tego jest, że wchodzimy do tej tabeli. Nie wiem, czy znajdziemy na to jakiś lepszy sposób. Aktualnie pamiętam, że były sugestie, żeby taka akcja spowodowała dodanie do tej tabeli pola i przeniosła mnie do tego widoku. To było z dyskusji z dziewczynami, że to już by było dla nich bardziej intuicyjne. Pracują na głównym, a teraz jeśli coś potrzebują do tabeli, to rzucają sobie do tabeli. Druga propozycja jest też taka, że zauważcie, że teraz, jak wrzucę pole tabela, to ono mi się dodaje. Może efektem powinno być od razu wejście do tej tabeli, bo raczej, jak wrzucam tabelę, to chcę przejść do jej edycji. Później już będę sobie tego przycisku nie szukał.

**Janusz Bossak:** Nie ma nazwy tabeli. Nie wiesz, jakby tak było, jak mówisz, czyli położenie tabeli na formularzu i przeniesienie od razu nas tam.

**Kamil Dubaniowski:** Już mimo to przeniesie.

**Janusz Bossak:** Tracimy ten moment nadania nazwy.

**Kamil Dubaniowski:** Przemek cały czas czeka na backend, bo jest zgłoszenie, żeby po zwróceniu tego pola o tę nazwę mnie zapytało. To jest cały czas mylące, że użytkownik nie wie, jaką nazwę nadać. Wiem, że było założenie, żeby zawsze systemową. Jak mam tu ustawione PL, to znów mogę mieć zagadkę, jaką nazwę ustalam. Widzę tu, zobacz, polski, to pewnie po polsku. Jaka jest systemowa wtedy? Poprosiłem Przemka, żeby na to zwrócił uwagę. Gdzieś tam na czatach było okienko, które zapyta o nazwę systemową, stricte, i napiszę, że podajesz nazwę systemową, bo będzie label obok tego, co ja wpisuję. Później tłumaczenia można oczywiście wprowadzać. Druga opcja z tą tabelą: zastanawiałem się, czy tu nie dać po prostu też akcji, tak jak są na liście, i tutaj byłaby akcja, żeby wejść do tabeli. Najeżdżam i wyskakuje mi tutaj jakaś akcja i sobie wchodzę do tabeli. Bo kliknięcie w tabelę otwiera mi prawy panel. W temacie wejścia do tabeli mogłoby być może bardziej intuicyjne, choć przy drag & drop to nadal nie jest to, bo wszyscy będą robili tak, jak dziewczyny na pierwszy kontakt. Nie mam dobrego pomysłu. Możemy na razie to tak zostawić. Nie wiem, czy to powinno być w danych podstawowych. Czy akcja "Edytuj pola tabeli" czy jednak, tak jak wszystkie akcje, przeniesiona na tę belkę. Na liście jest tak, czyli "Przejdź do listy pól tabeli", jest akcja, więc byłoby spójnie, tylko wtedy trzeba by pewnie te inne akcje schować. Główna akcja to jest wejście do edycji tej tabeli. Taką akcję moglibyśmy przenieść na belkę. Będzie pewnie jeszcze mniej intuicyjne niż przycisk z napisem. Nie wiem, już trochę nad tym myślę i nie mam dobrego rozwiązania, więc też nie oczekuję od was. Możemy to zostawić zaparkować sobie. Przemyślicie. Nie będę na razie zgłaszał. Niech będzie, jak jest, czyli jest przycisk w tym miejscu w danych podstawowych. Chociaż nie wiem, czy on powinien być na samej górze, bo to nie jest jednak najważniejsza dana podstawowa. To mogłoby być gdzieś tu na samym dole tych danych podstawowych.

**Janusz Bossak:** Czy ja wiem, to jest główna. Ja bym go nawet wyciągnął ponad to wszystko.

**Kamil Dubaniowski:** Okej, mogłoby tak być, tak. To by się jakoś super wyróżniło wtedy nad sekcjami.

**Janusz Bossak:** To nie, bo to nie są dane podstawowe. Dane podstawowe to nazwa, nazwa wyświetlana i tak dalej, a to jest czynność, tak. To jest zupełnie inny typ pola i mamy edycję pola tabeli.

**Kamil Dubaniowski:** Dobra, to na pewno biorę, tak, że tak powinno być. Czy wybór najbardziej, co będzie intuicyjne? Pewnie nie, bo sama taka ikonka nie powie tyle, co przycisk, a to jest na tyle specyficzna i częsta akcja, że wejście do tabeli jest potrzebne. Pamiętajmy, że jest to nawigacja, ale nie wiem, jak to jest używane i czy ludzie w ogóle tego używają. Mi z tego poziomu jest najwygodniej, bo zwłaszcza jak mam zagnieżdżone tabele, to wchodzę od razu na poziom, który chcę, a nie przeklikuję się przez trzy tabele.

**Janusz Bossak:** To jest okej. To u góry jest, według mnie, bardzo okej.

**Kamil Dubaniowski:** Dobra, to na razie podsumuję to tak, że zostaje. Odnośnie intuicyjności, jak wejść do edycji pól w polu typu tabela. Postanawiamy, że zostaje akcja w prawym panelu jako pełny przycisk z tekstem, tylko wyjmujemy ten przycisk sekcji dane podstawowe ponad wszystkie sekcje. Nie do belki głównej, do belki górnej, tytułowej prawego panelu, tylko jako element już prawego panelu. Akcja powyżej wszystkimi sekcjami już z informacjami o tym polu tabela.

**Janusz Bossak:** Tak.

**Kamil Dubaniowski:** Zmienić nazwę zakładki "Ustawienia" na "Właściwości". To bardziej mi się klei logicznie. Jeśli wchodzę z widoku listy, to mam zębatkę, co sugeruje, że wchodzę w ustawienia. To jest cały panel ustawień. "Ustawienia w ustawieniach" to trochę dziwnie, więc wolałbym to nazwać "Właściwości pola". To już są specyficzne właściwości dla konkretnego typu pola: maska dla pól tekstowych, ilość wierszy dla pól typu długi tekst i tak dalej. Wszystkie już specyficzne. To jest minimalna zmiana, ale wydaje mi się, że tak być powinno.

**Janusz Bossak:** Tak być ta sama nazwa, tak jak "zarządzanie polem" to jakaś była pierwsza koncepcja.

**Kamil Dubaniowski:** Dobra, czyli "Właściwości" zostaje. Dalej: "Wartość domyślna" i "Podpowiedź". To był temat od Damiana. Zasugerował, że tego rzadko się używa. Pomyślałem, że podpowiedź jak najbardziej powinna być podstawową daną uzupełnianą, żeby ludzie wiedzieli, co to za pole. To, że tego nie robimy, to już inny temat. Wartość domyślna wydaje mi się, że bardzo rzadko używana i z tym się zgadzam. Tylko też nigdzie indziej mi ona nie pasuje.

**Janusz Bossak:** Ale jest na liście, jest tutaj.

**Kamil Dubaniowski:** Tak. Piotr zasugerował, my to mamy aktualnie, ale Piotr bardzo się upiera, żeby wręcz wywalić stąd edycję wartości domyślnej. Inne, żeby edycja była tylko dla podpowiedzi, bo to wszystkie pola mogą mieć podpowiedź dla tych nazw wyświetlanych. Jest też tradycyjne dla nas systemowych. Ale Piotr bardzo naciska, żeby usunąć. Zgadzam się z nim, bo tutaj będzie trzeba jakoś dziwnie wymyśleć, żeby pokazać, że dla tych pól się nie da ustawić wartości domyślnej, pewnie jakiś kursor powinien się zmieniać na taki zakazany. Jakiś może tooltip dla tego typu pola, że nie da się ustawić wartości domyślnej. Pytanie, w którą stronę idziemy: czy wywalamy całkiem i edycja wartości domyślnej jest tylko z prawego panelu, czy dodajemy obsługę, żeby pokazać, że tu się nie da?

**Janusz Bossak:** Jak dla ostatecznego tekstu da się ustawić. To jest w ogóle właśnie to, akurat odnośnie wartości dla pola static.

**Kamil Dubaniowski:** Nie, to podpowiedź. My to zmieniliśmy UI-owo tak naprawdę.

**Janusz Bossak:** Dokładnie mam ten problem, który właśnie wystąpił. Dla mnie treść, którą wstawiam do pola static, jest wartością domyślną tego pola. To od zawsze było, według mnie, zawsze było źle. Ustawiało się i ustawia się nadal wartość pola static tekst poprzez podpowiedź. To jest wartość domyślna.

**Kamil Dubaniowski:** Spodziewam się, że kwestia tego, że ta wartość domyślna nie ma tłumaczeń.

**Janusz Bossak:** To jest wartość domyślna.

**Kamil Dubaniowski:** My też zmieniliśmy tutaj w prawym panelu. Jak ktoś nie skojarzy, że to jest to, to ma tekst. No bo ostateczny tekst, więc tekst dla tego pola statyczny tekst i to jest tu okej. Ale na tabeli nie jesteśmy w stanie tego przedstawić, bo to jest to samo, co pokazałem. Pokaże się tu po prostu.

**Janusz Bossak:** Jasne. Jeszcze mam pytanie odnośnie tej kolumny "Wartość domyślna". Rozumiem, że tam mamy po prawej stronie możliwość wybierania, które kolumny są wyświetlane. Tu mamy "Wartość domyślna". Możemy nie pokazywać, więc ja bym to zostawił. Jak ktoś chce sobie wyświetlać, to będzie musiał wiedzieć, że niektóre pola mają wartość domyślną, a niektóre nie.

**Kamil Dubaniowski:** Spodziewam się, że Filip obsłużył to, czyli jakiś warunek w kodzie jest, że pokazuje ramkę dla wybranych, a dla innych nie. Więc dla innych nie. Mógłby się kursor zmienić na taki zakazany. Byłoby jasne, bo tu nadal wygląda, jakby mógł coś kliknąć, ale nic się nie dzieje. Jest kursor ustawiony, tylko jako jedyny klikalny. Jest też niespójne, że to jest jako jedyne konieczne do zatwierdzenia. Inne wartości mogę pisać z palca i wyjść. Tu muszę zatwierdzać. Filip musi to uspójnić. Stąd pytanie, czy w ogóle chcemy tę edycję i utrzymać, bo tu jest trochę błędów wymienionych przez Filipa, bo dodawał inaczej niż w innych miejscach się zachowuje. I teraz nie wiem, czy to naprawiać, czy w ogóle rezygnować z tego i robimy tak, jak Piotr chce, że ta kolumna tylko pokazuje, ale nie pozwala edytować.

**Janusz Bossak:** Ja bym zostawił tak, jak jest.

**Kamil Dubaniowski:** Zostawiamy edycję, dobra.

**Janusz Bossak:** Było tak, niech tak będzie.

**Kamil Dubaniowski:** Dobra, co to był za temat? Gdzie przenieść "Wartość domyślną" i "Podpowiedź" z tego prawego panelu? Możemy zostawić, tylko to, co zasugerował Damian, to tak: jest praktycznie nieużywana. Zajmuje sporo miejsca, bo całą linię. Mogłyby się tu zaczynać ustawienia pola, a tych ustawień właściwości pola jest mnóstwo dla pola "Tabela". To jest dużo skanowania, więc im więcej stąd z tych danych podstawowych wyciągniemy, to tu mamy więcej miejsca na te właściwości. Nie mam pomysłu, gdzie to wywalić.

**Janusz Bossak:** Zostawić. Musi gdzieś być.

**Kamil Dubaniowski:** Nie mam na to lepszego miejsca. Jedynie, co to ułożyłem kolejność, bo to było chyba tak, że najpierw była ta podpowiedź, czy coś w tym stylu. Nie było po kolei. Było jeszcze wyżej. Chyba nazwą wyjawiłem, to już kompletnie bez sensu.

**Janusz Bossak:** Przenieść to do właściwości pola i tę wartość domyślną dać to, co teraz się nazywa "Ustawienia pola". Bo to jednak jest trochę zależne od typu pola, bo w niektórych występuje, w innych nie. A tutaj chodziło w tych danych podstawowych, żeby było zawsze to, co jest spójne dla wszystkich.

**Kamil Dubaniowski:** Spójne dla wszystkich. Podpowiedź.

**Janusz Bossak:** Podpowiedź jest, bo to jest tylko kilka.

**Kamil Dubaniowski:** Dla ostatnich nie ma. Dla statik jest tym tekstem. Odkąd okej, ma to sens. Wtedy trzeba by się zastanowić, gdzie, bo na pewno częściej użyję maski dla pola tekstowego niż tej wartości domyślnej. To właściwie gdzieś by spadło pewnie na sam koniec, żeby to już było zawsze w tym samym miejscu.

**Janusz Bossak:** Tak. Trzeba podejrzewam, że i tak będą ludzie używać z tej listy tutaj.

**Kamil Dubaniowski:** Nie, o ile w ogóle będą tego używać. Co najczęściej użyjesz dla pola data, żeby ci wstawiało dzisiejszą datę. Ale to i tak zazwyczaj się robi z poziomu.

**Janusz Bossak:** Tu jest bardzo słabo. Bardzo słabo, bo bardzo ograniczona jest możliwość. Jest tylko brak. Dzisiaj wybrana data.

**Lukasz Bott:** Najczęściej dlatego robisz to z reguł, bo najczęściej musisz zrobić jakąś kalkulację. Także ta data, którą tam musisz wstawić, przypisać do pola, zależy na przykład od jakichś tam warunków, tak, że to na przykład od dzisiaj plus dwa. Tyle. Przepraszam, tylko taka sygnał. Janusz, Mariusz, Damian. Na kanale informacja, że naprawili ten hotfix. Nie wnikałem jeszcze w szczegóły, ale określił, że jakaś złośliwość rzeczy martwych. I szykuje. Poprosiłem go, żeby przyszykował instrukcję. Napisał, że dwie-cztery strony, cztery tego będzie.

**Kamil Dubaniowski:** Dobra, czyli.

**Lukasz Bott:** Zrzutami. W każdym razie naprawia.

**Kamil Dubaniowski:** Wracając, to bardziej domyślą przenosimy do.

**Janusz Bossak:** Dobra, dzięki.

**Kamil Dubaniowski:** Odpowiedź zostaje. Tę sami byśmy chcieli, żeby była używana częściej. Ostatnie, myślę, że nie mamy co rozmawiać, bo to Piotrek wręcz narzucił, żeby to zrobić. Mamy te informacje techniczne, mamy ten GUID i on jest teraz online edycja z ostrzeżeniem. Więc robimy przycisk edytuj. Pole jest tylko do odczytu. Tu jest edytuj i otwierać to okno do wprowadzenia stałej wartości. Widzisz też starą wartość, masz pole do wpisania nowej.

**Janusz Bossak:** Tylko bym zrobił dwie rzeczy: do kopii zostawić tak jak jest wyżej, na ID czy field name mogę skopiować i obok dopiero przycisk na wejście do edycji.

**Kamil Dubaniowski:** Tak i edytuj. Pewnie ten edytuj po lewej bym dał, żeby to się zachowało spójnie, że zawsze w tym samym miejscu na kopiowanie. Edytuj obok po lewej to jest specyficznie, tylko to pole da się edytować. Ten edytuj też jest uzależniony od ustawienia systemowego, więc ono nie będzie zawsze. Zazwyczaj będzie to pewnie kopii, tylko jak ktoś włączy to ustawienie systemowe, że można edytować GUID-y pól, to dopiero pojawi się ten edytuj tutaj obok.

**Lukasz Bott:** Kto będzie wiedział, jaką nową wartość GUIDa wprowadzić?

**Kamil Dubaniowski:** To jest już specyficzna sytuacja. Nie wiem, bo to jest tak: kopiowanie z testowego, wrzucanie na produkcyjne tych GUID-ów. To jest ten wątek, więc to Piotr myślę, że to wymusił. To była jednorazowa akcja. Ma to sens, musiał to robić z poziomu bazy, ale wydaje mi się, że to nie jest częsta akcja, że te GUID-y podmieniamy.

**Janusz Bossak:** To zupełnie odrębny temat.

**Lukasz Bott:** Tak było. Dobra, odchodzę.

**Kamil Dubaniowski:** Raczej rzadko się to zdarza, więc mamy to. Niech zostanie obsłużymy to dobrze, żeby edycja nie była za łatwa. Do tej pory robiło się na zapas, ułatwiliśmy dla wdrożeń. Jest okej. Ja nie mam na ten moment, co do tego, jak bardziej wyróżnić ten prawy panel. To jest kolejny krok, ale to będę dalej walczył z tą firmą. Coś mi tam sugerują, że od przyszłego roku to Figma nie będzie taka "unlimited", więc nie będzie trzeba pakietów dokupić.

**Janusz Bossak:** To jest osobny temat do przegadania. Powinniśmy przenieść się na Cursora i w Cursorze to robić. Dać mu tam te wszystkie system design i tak dalej. Będziemy mieli to samo.

**Kamil Dubaniowski:** To był ten wątek, że Cursora ciężko udostępnić.

**Janusz Bossak:** Już to wymyślimy. Będziemy mieli najwyżej jakąś taką stronę do publikowania. Trzeba przejść ten proces, pomyśleć i będziemy mieli.

**Kamil Dubaniowski:** Zobaczymy, jak będzie. Ja mam w Figmie najwyższy pakiet. Ta firma też da się zasilić biblioteką. Ona jest w stanie mi na podstawie projektu spisać guideline do tego, co my tu używamy, jakiej czcionki. Ja muszę na to wszystko zwracać uwagę, żeby tam nie używać ikon innych niż MDI. Wszyscy, których testowałem, jak wskażesz mu konkretną bibliotekę, to robi się ciężko, albo wywala błędy.

**Janusz Bossak:** O właśnie.

**Kamil Dubaniowski:** Dalej: kolejne kroki, co chciałbym na kolejnych Designach omówić. Jak mi się uda wypracować, co do tego, jak ten prawy panel bardziej wyróżnić, ale też nie przez kolorki, tylko bardziej w układ. To też chciałbym zaprezentować. To będzie raczej praca ciągła. Te właściwości dla poszczególnych pól. Będziemy przeglądać pod kątem nazewnictwa, bo nazewnictwo niektórych ustawień nie jest okej. Pod kątem instrukcji do tych pól, żeby też były jakieś tooltipy dla admina i kolejność. To będzie trochę takie "na oko" i na naszą ocenę. Myślę, że nasze doświadczenie będzie wystarczające. Sugestia Damiana, że na samej górze są właściwości, z których właściwie się nie korzysta, a na samym dole te, które są potrzebne. Tę kolejność będzie trzeba przejść pole po polu. Nazewnictwo tych właściwości, czy jest jasne, intuicyjne. Ostatnia kwestia, opisy, instrukcje do tych ustawień.

**Lukasz Bott:** Nie tyle do zaprojektowania, natomiast jest temat. Dwa tematy, ale wyszły w PKF. Pierwszy temat znów wraca kwestia uproszczonych okienek modalnych do edycji zawartości wierszy. Bez poziomu raportu. W PKF by się to przydało. Jeszcze jedna rzecz do przegadania: edycja, jak mamy proces typu rejestr. Żeby zaimportować dane z zewnętrznego źródła, musimy ustawić klucz. W tej chwili chyba nie przewidzieli mechanizmu resetu klucza, nie dość, że resetu, to jeszcze zmiany klucza. Na przykład pierwsze próby były na klucz korzystał z kolumny ABC, a okazuje się, że później wystarczy tylko z kolumny A, żeby był klucz. W tym momencie chyba bez grzebania w bazie danych to.

**Janusz Bossak:** Klucz można.

**Lukasz Bott:** Właściwie chyba w tej chwili nie ma możliwości zmiany klucza.

**Janusz Bossak:** Nie, można zmieniać klucz. Dlaczego nie można? Myślałem, że jest możliwość rozwinięcia tego.

**Lukasz Bott:** Tak. Przynajmniej w nowym interfejsie definicji procesu. Żadnej akcji nie było. Okienko w ogóle nie otwierało się do zmiany klucza. Może to jest błąd.

**Janusz Bossak:** To jest błąd. Działało. Trzeba sprawdzić na starszych wersjach, na 100% można było zmieniać klucz. Przecież możesz mieć sytuację taką, gdzie stworzysz go i wierzysz jedną wartość. Jest nieunikalna. Dajesz drugą. Jest unikalna. Złączenie jedno i drugie.

**Lukasz Bott:** Tak.

**Janusz Bossak:** Jak tak działa, jeżeli tak nie działa, to znaczy, że powstał jakiś błąd kiedyś tam i nie został zauważony.

**Lukasz Bott:** Dobra, ja to sprawdzam. Dobra, w takim razie.

**Janusz Bossak:** Tak mi się wydaje. Tak, że to tak było założenie. Jak to możliwe, żeby jednorazowo ustawić klucz?

**Lukasz Bott:** Właśnie, ja tak jestem przekonany do tej opcji. Dobra. To jest do sprawdzenia, bo to być może faktycznie jest błąd. Ale ten temat edycji tutaj jeszcze był taki specyficzny przypadek, specyficzny dla PKF. Normalnie: masz raport osadzony na sprawie. W raporcie wyświetlasz wiersze z tabeli na sprawach. Te wiersze musisz w tym raporcie edytować.

**Janusz Bossak:** Nie rozumiem.

**Lukasz Bott:** Masz sprawę. Rejestracja czasu pracy. Sprawa wygląda w ten sposób, że masz na dany dzień. Wypełniasz tabelkę, przy jakich zleceniach, projektach pracowałeś i ile czasu. Czyli masz główny formularz i tabelkę na tym formularzu i raport osadzony bazuje na tej tabelce z formularza sprawy. Trzeba w jakiś sposób to znaczy tak. Chcą zrobić coś takiego: osoba widzi w raporcie ustawienie wierszy z tabel z różnych dni, bo rejestrację robisz na jeden dzień, ale masz z kilku dni. Trzeba tu powiedzieć o korektę czasu pracy, żeby zbiorczo móc to edytować.

**Janusz Bossak:** Ale jak potem to edytować? Nie mamy czegoś takiego jak edycja na tym raporcie.

**Lukasz Bott:** Właśnie nie mamy. To jest pytanie, czy nie chcielibyśmy czegoś takiego zrobić. Dlatego mówię, trochę wraca ten temat uproszczonych okienek modalnych. Tutaj wyświetlałbyś formularz wiersza tabeli. Oni tak mają swój cel, więc w bazie danych wiadomo, co zmienić i w którym miejscu.

**Janusz Bossak:** Teoretycznie da się tak wyświetlać, bo przy różnych błędach czasami się tak zdarza, że wyświetla się formularz dla wiersza tabeli. Istnieje. To jest dość szeroki temat. Nie chciałbym go otwierać na nowo.

**Lukasz Bott:** Rozumiem, dlaczego jeszcze tam trochę słowo. Kamilowi powiedziałem, że to nie jest robota na tydzień, czy nawet na najbliższy kwartał. To jest grubsza sprawa. Trzeba uwzględnić wiele różnych aspektów.

**Janusz Bossak:** Dokładnie.

**Lukasz Bott:** Trzeba sobie jakoś to obejść i poradzić.

**Janusz Bossak:** Na czym polega tam zmiana tych wpisów? Żeby wchodzić w każdy i coś tam zmieniać.

**Lukasz Bott:** Mówiąc najprościej, to masz tak: w Excelu zestawienie godzin na różne dni, z różnych miesięcy i w różnych projektach. Widzisz, że w tym dniu trzeba zmienić. Pracowałem mniej. Troszkę więcej przy tym projekcie, a z innego dnia trzeba usunąć. Może wprowadzić inny wiersz. Trzeba było zrobić z raportu tabelarycznego możliwość edycji w trybie Excelowym.

**Janusz Bossak:** Dopasować.

**Lukasz Bott:** Bo rzecz polega na tym, że kierownik projektu widzi zbiorczo godziny poświęcone na dany projekt i jego ludzi. Widząc to, chciałby to zmienić: tu troszeczkę, tu inaczej, tu, że źle przypisał godziny. Tego typu edycje.

**Janusz Bossak:** Tak, bo pytanie. Kiedyś chodził mi po głowie taki pomysł, żeby mieć takie pole "ala Excel". W Devexpressach coś takiego jest. To znowu w React. Nie na sprawę, nie do starych osadzonych raportów. Takie pole typu Excel. Tam wrzucamy dane i mogę sobie edytować. Problem zaczyna się w momencie, kiedy tam miały być jakieś reguły, jakieś zależności jednego od drugiego. Dopóki to były po prostu teksty, to nie ma problemu. Ale jak to ma na coś oddziaływać, szczególnie w pojedynczym wierszu, to już zaczyna mieć to inny wymiar. Nie mam na to dobrego pomysłu.

**Lukasz Bott:** Gdzieś tam mieliśmy takie funkcje, które potrafiły pracować z arkuszem Excela. Coś tam pobierać z arkusza.

**Janusz Bossak:** Tak, jest taka funkcja. Get Excel Data. Nie wiem, czy jest Set Excel Data. Proszę to sprawdzić.

**Lukasz Bott:** Możesz sprawdzić.

**Janusz Bossak:** Zobaczymy reguły. Wtedy można by iść w kierunku takim, że to się robi takim.

**Lukasz Bott:** Wtedy byś takiego Excela modyfikował z poziomu edycji, potem go importował.

**Janusz Bossak:** Takie.

**Lukasz Bott:** To trochę, wiesz, pytanie, czy lewą ręką za prawe ucho pod pachą.

**Janusz Bossak:** Dokładnie. Nie mam na to pomysłu. Temat edytowania danych w raportach wraca jak bumerang. Mamy do czynienia z raportami tymi starymi. W nowych też trzeba się z tym tematem zmierzyć.

**Lukasz Bott:** Na razie jakieś obejścia znaleźliśmy. Gimnastyka.

**Janusz Bossak:** Get Excel Data jest. Set Excel Data nie.

**Lukasz Bott:** Nie ma. Chyba stanęło na tym. To nie rozwiąże problemu, bo nawet jeżeli sobie ten Excel edytował, to potem musisz go w jakiś sposób zaciągnąć do systemu. System ma być w miarę prosty. Interfejsy webowe rządzą się takimi a nie innymi zasadami. To nie jest aplikacja okienkowa.

**Janusz Bossak:** Dobra, nie wymyślimy nic na razie na tym.

**Lukasz Bott:** Nie mówię, że rzucam hasło, ale to jest do dyskusji na radzie, może jakiś inny design, ale na pewno nie do realizacji w ciągu kilku dni.

**Janusz Bossak:** Nie, bo w ogóle nie ma sensownego pomysłu na to. Dobra, to chwila przerwy.

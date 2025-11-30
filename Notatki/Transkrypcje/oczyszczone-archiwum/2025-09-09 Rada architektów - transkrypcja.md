**Rada architektów 2025-09-09 - Transkrypcja**

**Data:** 2025-09-09
**Uczestnicy:** Damian Kamiński, Łukasz Bott, Janusz Bossak, Piotr Buczkowski, Anna Skupińska, Marek Dziakowski, Kamil Dubaniowski, Adrian Kotowski

---

**Damian Kamiński:** Cześć.

**Łukasz Bott:** Wróć do Damian, to AI podzieliło na części całkowite, a nie tam ułamkiem 5.

**Damian Kamiński:** Dobrze, nie no to wyprodukowałem dzisiaj rano, bo tam przeglądałem backlog i tak właśnie przypomniałem, że to omawialiśmy tydzień temu, więc mówię, napiszę od razu już będzie z głowy. Sprytnie mi to też przygotowało. W ogóle z Claude'a jak kopiuje do tego twojego Obsidiana, Janusz, to od razu to jest w tym md, nie wiem, jak to jest nazwa.

**Janusz Bossak:** No. Markdown.

**Damian Kamiński:** Markdown, Markdown, no więc to jest kompatybilne, więc to też wygodne. Dobra, co mamy już?

**Janusz Bossak:** Z tym to tak a propos tych podglądów u nas w AMODITcie. Bo zauważyłem, że tutaj pliki txt nie wyświetla się podgląd, tylko pobiera. Że jest kilka takich jakby nie jest zgodność.

**Piotr Buczkowski:** To się coś popsuło, bo powinno wyświetlić po prostu tekst.

**Janusz Bossak:** Właśnie.

**Łukasz Bott:** Mnie też się wydaje, że kiedyś wyświetlał.

**Janusz Bossak:** Też mi się wydaje, że było, bo już była o tym dyskusja, jak tam rozmawialiśmy o HTML-ach i wtedy też były te teksty, się wyświetlały na 100% się wyświetlały, bynajmniej teraz się nie wyświetlają i jeszcze do tego jest inne zachowanie na raporcie i inne na sprawie. Jak na sprawie klikam w plik txt, to od razu go pobiera. Co nie jest oczekiwane, no powinien być podgląd, ale jak jestem w raporcie i mam wyświetlane dokumenty i klikam na plik txt, to on się próbuje wyświetlić. Znaczy pojawia się panel podglądu i tam mruga, że ciągle nie ma podglądu. Ciągle nie ma podglądu, w końcu przestaje mrugać, ale podglądu nie ma, nie. Więc warto by było to [naprawić].

**Damian Kamiński:** Znaczy będzie teraz zajmował się Przemek tymi raportami, czyli podglądami w raporcie już w Reactcie, to po prostu niech to zweryfikuje. Zwrócę mu na to uwagę. I no właśnie, jeśli coś jest backendowo nie tak, no to pewnie jak to rozwiąże to i tu, i tu się problem rozwiąże.

**Łukasz Bott:** Ja bym tutaj jeszcze rozważył jedną rzecz, skoro mówimy o [podglądzie] do tych właśnie formatów takich tekstowych tak, czyli txt, może Markdown, może nie wiem JSON-a, tak, w końcu to są HTML-a. Tak w końcu to były formaty tekstowe. Jeżeli da się to wyświetlić, no to wyświetlajmy tak, no.

**Janusz Bossak:** Według mnie tak jak mówisz, tak powinno być, że trzeba zrobić z tego zgłoszenie, tak, jakieś feature'y do do [realizacji].

**Janusz Bossak:** Znaczy nie wyświetlanie się formatu txt jest według mnie błędem. Tak natomiast rozszerzenie na inne jest zadaniem.

**Łukasz Bott:** Tak, tak, tak.

**Janusz Bossak:** Bo bo się pod znaczy wyświetlały się teksty, no. Natomiast tak to, co powiedział Łukasz jest, uważam bardzo istotne, bo pliki typu właśnie JSON, plik XML, plik log. A w szczególności teraz ostatnio nam tutaj potrzebne Markdown (md), no mogłyby się wyświetlać, znaczy bardzo mógłbyś wyświetlać.

**Łukasz Bott:** No można. Markdown jest dosyć popularnym w tej chwili w formatem, tak, no takim.

**Janusz Bossak:** Z Markdownem to jest tak, że albo mógłby się wyświetlać po prostu jako tekst i wtedy widać te hashe i tak dalej w środku i to jest najprostsza metoda, a druga jest taka, gdyby interpretował już tego Markdowna i żeby to się wyświetlało już tak jak po interpretacji Markdowna powinno wyglądać, czyli z nagłówkami z tam obrazkami, co tam w środku w nim jest, nie, więc. Ale to jest osobny temat, zupełnie nie.

**Łukasz Bott:** No pewnie. No to wiesz, to jest to, to może ja bym poszedł, nawet może dalej, tak. Bo są są pewnie wtyczki, jakieś komponenty, które właśnie renderują ten Markdown i umożliwiają edycję pewnie w Markdownie nie, więc może ten nasz edytor w polach tekstowych zastąpić właśnie takim [Markdownowym], nie.

**Janusz Bossak:** Do tego. Do tego Quill'a, którego używamy jest wtyczka właśnie Markdownowa, ale jest jakaś słaba, bo już ją tam testowałem, no nie obsługuje całego zakresu tych znaczników Markdowna ona. No już kiedyś o tym myślałem, żeby tak właśnie zrobić nie, ale to mówię to z tym Markdownem, no to.

**Damian Kamiński:** Coś jeszcze tu sugerowaliście JSON? Tak.

**Janusz Bossak:** XML, JSON.

**Łukasz Bott:** JSON, nie chcemy tak.

**Janusz Bossak:** Log. Na przykład jakieś pliki logów ktoś załącza i żeby się wyświetlały.

**Łukasz Bott:** No o ile to będzie, o ile to będzie format tekstowy, logi? Tak, no bo.

**Janusz Bossak:** Wszystko.

**Piotr Buczkowski:** Znaczy. To tutaj trzeba te [niezrozumiałe].

**Janusz Bossak:** Znaczy, no musi być format tekstowy, tak, tak, tak, nie.

**Piotr Buczkowski:** Znaczy tutaj jest jeszcze taki problem. Na przykład wyszedł wam wreszcie, że wreszcie co pliki `xlsm`. Czy jest z makrami Excel? Normalnie są obsługiwane, tylko oni tam mają takie pliki, które się generują. Podgląd generuje 5 minut, jej zamula system i właśnie myślałam nad funkcjonalnością, żeby wyłączyć niektóre typy plików z generowania podglądu.

**Damian Kamiński:** OK. Dlatego według mnie to trzeba, bo to jest bardzo ważne i my musimy to zamieścić i wtedy nikt nie będzie się czepiał jak będzie chciał coś dodatkowego, to znowu proszę bardzo wycena, a nie tak, że my czegoś nie obsługujemy. Tu jest wpisane co, więc tu też to jest uwzględnić nie uwzględnić go przygotować. Musimy to po prostu przy okazji tego opisać. Tak, bo tu mam pod Ctrl+V, bo te txt. Pytanie czy coś jeszcze chcecie tu wymienić?

**Piotr Buczkowski:** Znaczy tutaj trzeba po prostu dodać listę rozszerzeń plików, które się wyświetla po prostu tak jak są, tak.

**Damian Kamiński:** Dokładnie. Tak.

**Piotr Buczkowski:** W `iframe` czy fajnie, tak, fajnie, żeby to było w `iframe` sandboxowym.

**Łukasz Bott:** HTML.

**Łukasz Bott:** HTML jeszcze format przeważnie.

**Piotr Buczkowski:** Wyświetlamy w parametrze sandboxowym, żeby nie było testów penetracyjnych jakiś uwaga, dlaczego pozwalamy jakiś atak z jakiegoś pliku, który coś może zawierać?

**Damian Kamiński:** No właśnie, ale HTML może zawierać linki.

**Piotr Buczkowski:** Dlatego wyświetlamy wyświetlamy wyświetlamy w `iframe` sandboxowym, który mocno ogranicza, który do tego służy, tak.

**Damian Kamiński:** Aha, ale to podgląd, dobra, to tak obraz.

**Piotr Buczkowski:** Znaczy jest parametrem `sandbox`.

**Damian Kamiński:** Mam to coś zapisać, coś takiego?

**Piotr Buczkowski:** Z tego jest.

**Łukasz Bott:** Tak dopisz to, dopisz.

**Damian Kamiński:** To to jeszcze raz. To już jest tak, bo oni będą przerabiać cały ten podgląd na Reacta to nie ma wpływu.

**Piotr Buczkowski:** To nie no nie jest, no to to to co jest teraz to jest jeżeli mają przerabiać no to trzeba wpisać żeby przerobili takie jak żeby było dobrze, czyli że te pliki właśnie tekstowe nie wyświetlamy po prostu w DIVie tylko w `iframe` z parametrem `sandbox`. Bez `allow-script` bez `allow`... Coś tam jeszcze jest?

**Janusz Bossak:** Bo to jest cały zestaw w tych w ogóle rzeczy do podglądania. Tak, no te pliki zawierające pocztę, ale nie będące HTML tylko MSG. Nie wiem czy to się daje też podglądać.

**Piotr Buczkowski:** MSG nie, MSG jest trybem normalnym, trzeba mieć Outlooka. EML teoretycznie można w pliku tekstowym można wyświetlić, no tylko wiadomo to jest format.

**Łukasz Bott:** EML.

**Damian Kamiński:** Chcemy wyświetlać?

**Piotr Buczkowski:** Często też binarny tak, bo jest Base64 encode, także nie ma sensu.

**Damian Kamiński:** Nie ma sensu dobra, no tak, bo trzeba przetłumaczyć tak.

**Piotr Buczkowski:** To trzeba Outlooka mieć albo inny program pocztowy.

**Damian Kamiński:** Dobrze, poczekajcie jeszcze to domy, gdzie to było, pliki tekstowe nie wyświetlamy zdjęcie tylko w `iframe` z parametrem `sandbox` to jest dobrze. Dobra. Tak, zapiszę, żeby było wiadomo do kogo się udać, dobra?

**Janusz Bossak:** To jeszcze jedna nie wiem czy tam już pisałeś, ale chodziło mi o to, żeby ten ktoś, kto będzie to robił, miał świadomość obu przypadków, czyli przypadek na sprawie podgląd i przypadek w raporcie podgląd tak.

**Damian Kamiński:** Nie nie, to poczekaj, to na razie robimy w ramach raportów jak to zrobią i spiszę nam jeszcze to to wtedy to posłuży do testów na sprawie i wtedy ewentualnie to ujednolicimy na sprawie dobra, tak się umówmy, no bo i tak backend będzie musiał być pod to, jeśli jakkolwiek musi być przygotowany, no to zakładam, że będzie wtedy wrócimy do sprawy. No i frontendowców poprawiał na sprawie, tak bym to rozumiał.

**Łukasz Bott:** Wiesz co? A jedną rzecz, jak jestem przy Markdown, to ewentualnie tylko pytanie jest takie, czy szukamy komponentu, który to renderuje od razu i wyświetla sformatowany czy po prostu wyświetlamy z tymi tagami markdownowymi? Możemy jako MVP, tak zróbmy po prostu i tyle.

**Janusz Bossak:** Czy to sprawdzenie, a właśnie czy mamy jakiś komponent, który to robi?

**Łukasz Bott:** Nie nie, jeżeliby jeżeli jest prosty jakiś, komponent, który to wyświetla renderuje to tak, a jeżeli nie to.

**Janusz Bossak:** Czym? A czy czy my generujemy te podglądy `GdPicture` czy ciągle jakimiś innymi jakimiś narzędziami?

**Piotr Buczkowski:** A co która podglądy?

**Janusz Bossak:** W ogóle podglądy dokumentów no tak jak tekstowy czy właśnie Markdown czy inny.

**Piotr Buczkowski:** Nie, nie, nie. Przecież cały czas mówię o tym. Dokumenty tekstowe po prostu wyświetlamy.

**Łukasz Bott:** Czyli tak jak sobie to przeglądarka interpretuje?

**Piotr Buczkowski:** Podglądy generujemy tylko dla dokumentów [obrazkowych/PDF].

**Damian Kamiński:** OK.

**Janusz Bossak:** No to już idąc tym tropem. Ponieważ to tutaj ostatnio robiąc jakieś próby z AIem. Czy tekst pliku tekstowego jest dostępny w `GetAttachmentContent`? Wydaje mi się, że nie.

**Piotr Buczkowski:** Tak. A powinien być.

**Janusz Bossak:** A powinien właśnie.

**Damian Kamiński:** Chciałem coś związku z tym zapisać.

**Janusz Bossak:** W związku z tym trzeba napisać osobne zgłoszenie.

**Łukasz Bott:** To pewnie jako odrębne zgłoszenie.

**Janusz Bossak:** Bo ono już nie dotyczy podglądów. A dotyczy funkcji `GetAttachmentContent`. Żeby ona zawierała content [pliku].

**Damian Kamiński:** To znaczy ja pisałem, więc się chwilę zamyśliłem, a teraz nie zawiera?

**Janusz Bossak:** No w moim przekonaniu nie.

**Damian Kaminski:** A w mojej opinii tak powiem, że w sensie, że jak masz ta ich stronę, to czy jak weźmiesz `Content` to czy dostaniesz wynik tekstowej treści? Według mnie tak.

**Janusz Bossak:** Dostajesz nazwę pliku potem i mój email. No email, kto tam stworzył ten plik, co jest też zresztą denerwujące. Strasznie mnie to denerwuje, że w `GetAttachmentContent` dostaje na początku jakieś takie dodatkowe informacje.

**Piotr Buczkowski:** To tak głośno, bo teraz po prostu zwraca treść, użyto do indeksowania.

**Damian Kamiński:** Tej to zrobił, tak?

**Piotr Buczkowski:** Tak, nie, nie, to to co jest, żeby ta indeksowanie, a tam też dajemy trochę metadanych, tak to był kto do do auto to zmodyfikował.

**Janusz Bossak:** Trzeba by wejść do jakiejś sprawy, które już coś jest, no bo jak?

**Piotr Buczkowski:** Nie to było na szybko robione tak zgłaszaj takie rzeczy.

**Janusz Bossak:** Dobrze przetestuję i zgłoszę.

**Damian Kamiński:** Mam to jeszcze sprawdzić.

**Janusz Bossak:** Nie już teraz nie sprawdzajmy na noże, bo nie sprawdzajmy.

**Damian Kamiński:** Dobra. To jedziemy. Dobra to zapisane OK. Czemu to jest no rada architektów?

**Łukasz Bott:** Miałyśmy tego nie zdjęli. Zobacz, możemy coś jest w komentarzach. Nie wiem, może nie zdjęliśmy tego domu?

**Damian Kamiński:** [Dobra] zapytam, bo to już jest `internal test`. Zapytam Łukasza w takim razie, czy coś tutaj trzeba umawiać? Jeszcze nie będę zdejmował. Dobra, idziemy dalej. Nie wiem czy tam wczoraj wyszło z tym Copilotem, ale to może nie teraz.

**Łukasz Bott:** Ale to jest to, bo to pozwala się przed chwilą gdzieś tam na czasie o to.

**Damian Kaminski:** No bo to znaczy w ogóle mam takie pytanie globalne. Bo są jakieś takie głównie od Mateusza, czy też od bardziej właśnie tych starszych wdrożeniowców są jakieś pytania, pomysły i tak dalej. Gdzie powinna być przestrzeń, żeby to wrzucać tu?

**Janusz Bossak:** Była kiedyś na [tablicy] analityką.

**Damian Kamiński:** Bo to jeszcze wiecie, nie jest wycena, tylko jest po prostu takie strzał przedyskutujmy czy warto w ogóle poświęcać czas na wycenę?

**Janusz Bossak:** Według mnie tak powinno być, bo to robi śmietnik nam z [backlogu].

**Damian Kamiński:** Czy warto się nad tym pochylać? Tak, ja się zgadzam, że tu jest już planowanie zadań, a nie zastanawianie się nad pomysłami. No jeśli było to może warto ją wznowić. Nie wiem jak się nazywa ten proces, ale dobrze by było, żeby jakiś taki krótki był.

**Kamil Dubaniowski:** Czy to szło przez wyceny? I to jest też duża część procesów, które zawisły, bo no nie mają co zaznaczyć w finansowaniu. Na przykład tak, ja nie mówię, że, że to, bo to akurat gdzieś tam powiedzmy, że przepłynęliśmy sobie dalej, no ale to pomysły i tak wyszło. Jakoś nie, nie, nie mając z tego nakazu, że moim zdaniem na dowód to my tego tak bardzo może przez to, że nie było przeglądu w tych wycen.

**Damian Kaminski:** No wtedy może na razie powinniśmy przeglądać i to i tamto, albo po prostu mieć dedykowane spotkanie do tamtego jako taki kontekst biznesowy, decyzja, czy w ogóle się nad tym pochylamy, ale gdzieś jakąś przestrzeń trzeba zrobić, jeśli nie chcemy właśnie takiego śmietnika tu mieć.

**Janusz Bossak:** To pytanie jest też po części wyceną to co wczoraj tam z Agnieszką [Gracz] rozmawialiśmy i z Mateuszem tak, no, bo klient chciałby cenę pod ten pomysł. Tak więc oni powinni to zgłaszać za pomocą wycen, nawet jeżeli to jest takie bardzo abstrakcyjne. Jeszcze pytanie, może ten proces się powinien nazywać "wyceny i pytania" i po prostu w środku zaznaczamy, że to jest pytanie, a nie wycena, żeby już nie mnożyć procesów.

**Damian Kamiński:** OK.

**Łukasz Bott:** No to jest. No to jest tam taka opcja, po prostu się wyceny, ten rozwój czy jakoś tak czy tam pomysł rozwojowy.

**Janusz Bossak:** Znaczy znaczy, to jest chyba są 2 kategorie "pomysł rozwojowy", znaczy, że chcą, żeby było zrealizowane, tylko nie ma chętnych do zapłacenia, ale są pytania po prostu. Czy można by było w AMODITcie coś tam? Nie, nie można by było na przykład brzmi odpowiedź albo można by było, ale po co tak brzmi odpowiedź? Więc to nie jest jeszcze pomysł rozwojowy do realizacji. Do wyceny.

**Damian Kamiński:** Tylko takie zapytanie o to, czy czy coś takiego dałoby się zrobić nawet jeszcze nie, za ile nie, żeby nad tym się pochylał ktoś do wyceny tylko na poziomie właśnie naszym, powiedzmy tak czy no jakiś tam powiedzmy ekspertów tak, szeroko mówiąc i systemowych i biznesowych.

**Łukasz Bott:** Wiecie co to znaczy tak na szybko i na gorąco. Odpowiadając to ja bym się na razie z Ganttem [powstrzymał] i dawania tam jakiś.

**Damian Kamiński:** Nie, nie, nie, nie dobra, to nie chodzi o ten przykład chodzi ogólnie o kontekst. Wpada jakaś potrzeba, gdzie ją zamieszczać, żeby nie została pominięta, kiedy ją omawiać? W jakim gronie i tak dalej.

**Janusz Bossak:** Z wyceny przez wyceny nie tutaj. Tu ja uważam, że ten nasz backlog dla konsultantów powinien być dostępny jakby tylko i wyłącznie w trybie wpisuje hotfixy lub bugi i koniec jaki?

**Damian Kamiński:** Bugi. Mhm. To jest też jakieś rozwiązanie.

**Janusz Bossak:** Jak mają pomysły to zgłaszają to nas tak do do ciebie. Damian do Kamila do Łukasza do mnie do nas do Piotrka Buczkowskiego tak do nas. Ogólnie rzecz biorąc, my to przetwarzamy w głowie. Analizujemy na radzie. Powstaje projekt zapisany na wiki. Opisowy, że dobrze by było zrobić coś takiego, bo to jest ważne, bo coś tam coś tam i na podstawie do tego dopiero powstają wpisy na backlog, czyli zadania do zrobienia nie taka ścieżka tego.

**Damian Kamiński:** I tu masz rację, tylko wtedy trzeba mieć 3 przestrzenie, które trzeba przeglądać tak po prostu tutaj, jak wrzucają. To jest wygodnie, bo jak sobie tak wrzucimy? Ja oczywiście bardzo mocno upraszczam teraz, ale, ale tak jak wrzucimy tutaj mówię, napisz przypisz do mnie ja sobie wrzucę na radę, poruszymy, no i w zasadzie mamy jedno `query`, które nam agreguje wszystko w tym wypadku.

**Janusz Bossak:** No może tak być, tylko musimy z tym po prostu żyć. Tak znaczy musimy wiedzieć jak to szybko eliminować, ustawiać jakiś status, że to nie jest `New`, tylko to jest jakieś pytanie.

**Damian Kaminski:** No. Właśnie to co do tego, co mam zrobić, zamknąć to, bo ja nie wiem jak w bójki było wczoraj konkluzja.

**Janusz Bossak:** Tutaj jest [removed] na razie.

**Damian Kamiński:** OK. No i dobra i odpinamy. Dobra, idźmy dalej zgłoszenie Mateusza i tutaj na radę ze względu na to, żeby ono nie jest mocno skomplikowane, ale pytanie, co powinniśmy tutaj wyświetlać? Jakie są opcje, czyli tak. Raport typu Gantt.

**Łukasz Bott:** Kliknij to kliknij na ten obrazek to się wyświetli i większy.

**Damian Kamiński:** Tak, tak tylko wytłumaczysz wszystko czy przeczytać jednak.

**Łukasz Bott:** Znaczy, pokaż obrazek i opowiedz o co chodzi, no.

**Damian Kamiński:** Na wykresie grupują dobra. Dobra, więc tak mamy klocek grupujący to, co jest wewnątrz i teraz ten klocek grupujący po pierwsze wyświetla etykietę z pierwszej pozycji. Pytanie, co powinien wyświetlać? Jakie są ewentualnie zalecenia, czy ta pierwsza pozycja właśnie powinna być jakaś w cudzysłowie teoretyczna, żeby przenosić do poziomu wyżej [jakąś] wartość?

**Janusz Bossak:** Rzecz rządzi Marka teraz rzecz Marka, bo Marek to robił i żeby on od razu o tym słyszał. Żebyśmy go 2 razy i myśli?

**Damian Kamiński:** Już już już.

**Janusz Bossak:** Znaczy, słuchajcie, z Ganttem jest tak te zielone, one się jakby tworzą automaty.

**Damian Kamiński:** Frontend.

**Janusz Bossak:** Więc tutaj za bardzo nie mamy nad nimi panowania niewielkie. To jest po pierwsze, po drugie ten Gantt w rozumieniu tego, co daje DevExpress, jeszcze nie wszystko ma, co byśmy tutaj z Markiem chcieli, żeby miał. Więc Gantt jest ogólnie do rozbudowy tak jako taki, no ale to wróćmy do tego, co zacząłeś mówi Marek. Ciągnęliśmy cię, żebyś od razu słuchał, to mówimy o Gantcie.

**Marek Dziakowski:** Mhm.

**Damian Kamiński:** No dobrze, więc mamy w wierszach projekty i zadania i teraz mamy tutaj ten projekty i zadania, natomiast na label agregowany tego kafelka, który jest generowany dopiero w wizualizacji go nie ma nigdzie w bazie danych tak przenosimy po prostu po pierwsze wartość pierwszego kafelka wewnętrznego, czyli label jest kopiowany i może ja nie mówię, że to jest źle? Wtedy trzeba dać zalecenia, że może ten pierwszy kafelek, który jest już faktycznie jakąś sprawą. Powinien być takim teoretycznym po to, żeby w dobry sposób agregować. No i drugie ilość dni też tu już jest akurat jakiś błąd według mnie, bo ona powinna być kalkulowana na podstawie tych wewnętrznych to już jest ewidentny błąd, bo o ile to jest trudne do ustalenia o to to jest typowy bug.

**Janusz Bossak:** Źle skonfigurowany raport.

**Damian Kamiński:** OK. Dlaczego?

**Janusz Bossak:** Dlatego, że teraz jest tak, że on w projekt pokazuje 2 wiersze. Tak.

**Damian Kaminski:** Jak to 2 wiersze w sensie 2 2 zagnieżdżenia główne i te wewnętrzne? Tak, mhm.

**Janusz Bossak:** Chyba tak. I one pochodzą z danych na sprawie.

**Damian Kaminski:** Ja tu jest link.

**Janusz Bossak:** Pytam zabić, gdyby tam zrobić same zadania. I zrobić je jak to [kiedyś] Marek robił rekurencyjne. Że za no to wtedy by się zaczęło agregować prawidłowo.

**Damian Kamiński:** No dobra, ale no. Pytanie, czy to znaczy OK możemy i masz rację. Natomiast no że gdybyśmy jakoś to zrobili, to by się prawidłowo wyświetlało. Niemniej wydaje mi się, że to powinno jednak sumować wszystko, albo tego nie wyświetlać, no bo w tym momencie wyświetla złą wartość.

**Marek Dziakowski:** Ta etykietka była zrobiona tymczasowo i tak trochę o niej zapomnieliśmy. Tym Gancie myślę, że no to można to przerobić tylko pytanie, no jak no na na na etykietę można wrzucić wszystko. Można by wykrywać co to jest, czy jest to liczba i wtedy. Wszystkie te wszystkie te informacje z tych tak by podległych wierszy to wyświetlić.

**Damian Kamiński:** No albo nie wyświetlamy w ogóle tego tooltipa po najechaniu to jest jedna opcja i wtedy sobie licz, albo jeśli już wyświetlamy to powinniśmy wyświetlać to co powinno to to to co on wskazuje czyli ilość data, zakres i ilość dni roboczych też prawidłową.

**Marek Dziakowski:** No no bo w ogóle właśnie. Znaczy. Ja bym po prostu zostawiłbym. Datę od do, bo ona jest chyba dobrze wyliczana czy nie, nie też jest źle OK. Znaczy to...

**Damian Kamiński:** Nie jest dziewiąty, zależy wrzesień, a to jest luty.

**Marek Dziakowski:** No czy to wszystko można poprawić? No nie?

**Damian Kamiński:** Ona to, co jest tu jest brane w całości z pierwszego kafelka tak czyli i label i tooltip.

**Marek Dziakowski:** Mhm. Mhm, to można to poprawić, żeby to wyświetlało wszystko dobrze.

**Damian Kamiński:** No dobrze, tylko co to znaczy dobrze? W sensie tutaj tutaj.

**Marek Dziakowski:** Czy label? No właśnie label to bym chyba wyrzucił, bo jak sumować na przykład jakieś tutaj akurat jest liczba, ale jak będzie napis, no to co wtedy?

**Damian Kaminski:** No nie ma jak zgadzam się. No to liczbę możemy traktować jako napis równie dobrze i tak masz rację, że to nie da się tego za agregować sensownie.

**Anna Skupińska:** Czy można byłoby wszystkie wypisać tak po kolei jeden za drugim napisy, technicznie rzecz biorąc.

**Damian Kaminski:** Nie, nie, nie, jeśli to by były napisy jednowyrazowe, no to już ci się tu nie zmieści. Nie, nie. Ja bym już był za tym, że wywalisz to w ogóle.

**Marek Dziakowski:** No to chyba jeszcze można w ogóle kilka etykietek wrzucić też. Wtedy pytanie, jak to by było rozumiane? Też każdy wiersz łączyć jakoś.

**Damian Kamiński:** Ja bym się przychylał do tego zaproponowałeś etykiety są definiowane do tych pojedynczych elementów agregację nie robią etykiet bo nie wiadomo jakie za agregować te etykiety. Natomiast to jeśli chcemy wyświetlać to musi się wyliczać. Prawidłowo, czyli jedynka jest do skasowania, dwójka jest do poprawienia.

**Kamil Dubaniowski:** A może nazwę pola to po prostu na tej agregującej czyli ilość dni po prostu tekstem. Żeby było wiadomo co to jest, to 10 5, 15, 19. Nie wiem, tak. Ma być puste, to wolałbym chyba już mieć tą informację, no bo teraz musiałbym ją wrzucać jeszcze na tooltipie.

**Damian Kamiński:** Ale czy to dobrze będzie biznesowo wyglądać? Jak to napiszemy sobie ilość dni?

**Marek Dziakowski:** W sumie można.

**Łukasz Bott:** Nie, jeżeli jeżeli już to na tym zielonym agregującym prostokącie, to powinny moim zdaniem być jeżeli ma być jakaś etykieta to powinien być okres od do, bo wtedy wiemy, że to ten, bo tutaj mamy wizualnie na nad coś we wrześniu się gdzieś tam w połowie zaczyna niby tak no kończy się gdzieś tam w lutym, pomijając, że tutaj tą datę do podały luty tak, ale po prostu można by było napisać tylko te daty od do tak jako agregujący.

**Damian Kaminski:** Tylko Łukasz poczekaj, bo raz mamy to tu, po co dublować 2. Pomyśl teraz tak, że masz zagregowane tylko 10 i 5 i już i masz taki kafelek malutki i nie masz na to miejsca. Ja bym tu nie ja bym tu nie wrzucał chyba nic.

**Marek Dziakowski:** Tego nie będzie widać po prostu.

**Damian Kaminski:** Po prostu jest do tego tooltip, a data do jak najedziesz to ci się wyświetli tak jak dla każdego innego.

**Janusz Bossak:** Ten Gantt który mamy z DevExpress. On ma jeszcze jedną możliwość wyświetlania czegoś za. W tym zielonym paskiem.

**Damian Kamiński:** Czyli, że label jest obok tak?

**Janusz Bossak:** Tak znaczy za wyświetla się najczęściej menedżera, kierownika menedżera, osobę odpowiedzialną za to zadanie tak przynajmniej tam w tych przykładach DevExpressie jest nie. Ale istnieje taka przestrzeń, żeby jeszcze coś wyświetlać za takim niebieskim paseczkiem, czy za tym zielonym paseczkiem.

**Łukasz Bott:** A czekajcie. To jest pogrupowane po jakimś. Rozumiem projekcie i zadań no może nazwę projektu po prostu dać.

**Damian Kamiński:** Projekt zadań.

**Janusz Bossak:** Ale nazwa projektu jest tam widzisz pierwszej kolumnie projekt, korespondencja więc.

**Łukasz Bott:** No ale masz masz nazwę, ale masz nazwę na zasadzie, że coś tam 3 kropki, a tu masz duży.

**Janusz Bossak:** Po co powielać?

**Damian Kamiński:** No tak, tylko jak to określać? Bo zobaczcie ty etykieta te jest ilość dni, czyli oni sobie tu roboczych oni sobie tu wyświetlają to co dasz etykieta, nowy kolumnę, etykieta dla agregacji. To ja bym poszedł najmniejszą linią oporu wyeliminował bym błędy. A nad rozwojami bym się później zastanawiał.

**Janusz Bossak:** Trzeba tutaj patrzy na naszym Astrafoxie to to coś to nie działa, nie. Gantt wymaga według mnie głębszego przejrzenia takiego. Są pewnie takie przypadki właśnie skrajne, że to nie działań. I to pamiętam. To Marek, Przypomnijmy, o to mamy te 2 tryby takie zbudowaniem hierarchii. I bez tego budowania hierarchii to się różnie zachowuje w obu tych trybach nie i trzeba mieć też tutaj do tego świadomość tego mamy 2 tryby budowania Gantta, jeden tryb jest taki jak tu pokazany, czyli wstawiam 2 nazwy, co oznacza pierwszy poziom, drugi poziom agregacji, ale trzeba mieć świadomość, że dane w tym projekcie i w tym zadaniu pochodzą z tej samej sprawy.

**Damian Kamiński:** Tak.

**Janusz Bossak:** Tu nie ma żadnego agregowania. Tak, bo to jest czytanie z tej sprawy. W tej sprawie jest coś jakiś numerek?

**Marek Dziakowski:** Tak.

**Janusz Bossak:** Z tej sprawy pochodzi tylko tam nazwa korespondencja i tak dalej, bo ona się powtarza w każdej sprawie z tym zadaniem. Tak no to jest link prawdopodobne.

**Damian Kamiński:** To znaczy zadanie, to jest sprawa tak, a zadanie to jest reprezentacja sprawy, a projekt jest słownikiem.

**Janusz Bossak:** No tak, ale patrzmy na pojedynczą sprawę. Tak pojedyncza sprawą w sądzie.

**Damian Kamiński:** Tak, czyli wiersze to jest pojedyncza sprawa.

**Janusz Bossak:** Nie, bo to agregacja też się pochodzi z tej pojedynczej sprawy, tylko jest jakby grupowanie m po elemencie z tej sprawy tak czyli elementem. No to jest.

**Damian Kaminski:** Nie, nie, nie, nie poczekaj albo źle zrozumiałem, albo źle powiedziałeś. W sensie agregacja jest agregacją wszystkich spraw, czyli tak w ramach korespondencji. Ja bym rozumiał, że to jest są sprawy.

**Janusz Bossak:** No tak no.

**Damian Kaminski:** Jest 10 spraw. Każde mają swoje zadanie i od do.

**Marek Dziakowski:** No każdy każda sprawa ma projekt przypisany, dlatego to tak się.

**Janusz Bossak:** Nie do końca.

**Damian Kaminski:** No ok, ma projekt, zgadza się, ale jako pole słownikowe wtedy na podstawie tego, że ma jeden projekt to jest agregowane, ale każdy wiersz tutaj to bym oprócz zielonych każdy niebieski to jest sprawa albo przynajmniej wiersz w tabeli.

**Janusz Bossak:** Dziękuję. Nie. Zielony to jest też z tej sprawy. To nie jest nic innego, jak byś miał na sprawie 2 pola pole a i pole b zamiast projekty zadanie być tutaj wrzucił a i b. To tak to działa. To nie musi być Słownik, żeby cokolwiek.

**Marek Dziakowski:** No tak znaczy tutaj na gazecie nie ma agregacji, nie ma one to tak sztucznie są zagregowane po prostu te dane są pobierane pojedyncze.

**Janusz Bossak:** Wam się wydaje, że jest agregacji, ale nie ma tam agregacji. To jest punkt, jest tylko grupowanie.

**Marek Dziakowski:** Tak.

**Janusz Bossak:** Jest tak samo, jakbyśmy to drzewko budowali grupy po folderach to dokładnie ten sam mechanizm grupowania po folderach. I to jest najpierw grupy i po wnioskodawcy, potem grupuj po rodzaju wniosku. Tak należy doczytać.

**Damian Kamiński:** Czyli. No ale nie no zobaczcie tutaj. Jest tak długo, no nie, no to nie jest sprawa. Tu jak klikam to to jest sprawa, a zielone to jest agregacja od samego początku do końca no niebieskie to nie jest byt w bazie danych tylko to mi się wyświetla we froncie według mnie dopiero.

**Marek Dziakowski:** Zielone. Tak. Tak zielone nie jest bytem, nie da się w niego kliknąć, bo to nie istnieje taka sprawa.

**Damian Kamiński:** No właśnie, a ja zrozumiem Janusza, że powiedział, że to jest, że sprawy to nie jest ze sprawy w sensie ten zakres.

**Janusz Bossak:** Nie. Jest. Jest ze sprawy. Bo to jest wnioskodawca. Wnioskodawca istnieje w tej sprawie.

**Damian Kamiński:** Nie, ale poczekaj, poczekaj wnioskodawca tak, ale kafelek zielony nam agreguje na poziomie wnioskodawcy, jakiś zakres dat od do i tego zakresu, czyli początkowej daty i końca nie ma nigdzie na sprawie. Ja w wpisanego to jest wynik pierwszego i ostatniego elementu.

**Janusz Bossak:** Jest.

**Damian Kaminski:** Nie, no, zobacz, zareagowałem teraz urlopy.

**Janusz Bossak:** A ta? Tak, tak, tak, tak, no tak.

**Damian Kaminski:** Więc więc tego mogłoby nie być, nie byłoby widoczne i i dalej by to wszystko było OK na poziomie Damian Kamiński, jak rozwinę to to wyświetla mi się to jak mam zwinięte, no to widzę w jakim zakresie ja brałem urlopy, czyli brałem od marca 22 do grudnia 25, ale to mi nic nie mówi. W sensie to mówi, że ja wziąłem pierwszy urlop. Mogłem wziąć 2 urlopy, jeden dzień w marcu, 01 marca 22 i ostatni jeden dzień, czyli mogłem wziąć 2 urlopy. 2 dni urlopu i taki kafelek się buduje.

**Janusz Bossak:** Kliknij na nim prawym klawiszem. Tutaj działa ten przeliczanie, bo tam była taka opcja.

**Damian Kaminski:** Nie da się poprawić. Nic się nie dzieje.

**Marek Dziakowski:** W tym drugim trybie jest.

**Damian Kamiński:** Poczekajcie jeszcze wrzucę tutaj od do. A nie Przepraszam, nie do etykiety tylko do tooltipu. No i bierze po prostu z tego. I tyle znaczy ja bym to rozwiązał. Najprościej etykiet się nie generują na tych kafelkach. A to jeśli ma się generować no to musi być wyliczane. I to jest rozwiązanie tego baga, bo to jest zgłoszony bak, tak, że to nie jest 10 i ten tooltip pokazuje złe dane. Albo totalnie w ogóle tego nie ma i to też jest może być rozwiązaniem, że wywalamy to.

**Janusz Bossak:** Niby są.

**Damian Kamiński:** Tylko no jest mniej wygodne dla użytkownika, jednak ten tytul tip pomaga. Jeśli miałbym wskazać jakiś zakres.

**Janusz Bossak:** Tu są jakby do zadań do tych jednostkowych rzeczy, które są tak, natomiast tutaj trzeba by Marek pomyśl nad tym jak wyświetlać jakąś agregację, a poza tym jak określić co ma się tam w tym wyświetlać? Tak, bo to nie jest urlop od do. Oni.

**Marek Dziakowski:** Czy ten kafelek zielony mógłby mieć w ogóle jakiś kastowy, który nie jest zależny od tego, jakie są ustawienia tooltipów na tych niebieskich, że po prostu on jest tak nie nawet tego się nie tworzy, on się generuje automatycznie systemowy, jakiś taki i wtedy byśmy.

**Damian Kaminski:** Mógłby tylko gdzie to wcisnąć?

**Janusz Bossak:** Właśnie. Ale nie wiemy, co tam będzie, nie w ogólności, nie wiesz.

**Damian Kaminski:** Znaczy wiemy, że będzie jedna oś jest definiowana, jest datą zawsze, bo to jest zawsze od do, więc my możemy wyświetlić od i do tutaj do myślenia, bo to jest definiowane. Natomiast count no to tu już może być count, może być jakieś sumy czy różne pozycje, więc.

**Marek Dziakowski:** No tak. Czy ten count do wyrzucenia raczej z tych nawiasów?

**Damian Kaminski:** Dokładnie czyli to usuwamy i to usuwamy, zostawiamy od do tak idziemy po minimum.

**Marek Dziakowski:** Ja bym ja bym tak zostałem tak zrobił.

**Damian Kaminski:** Dobra, to tak to opiszę. Do Marka to później przepisać tak. Dobra, na razie jeszcze przypiszę siebie napiszę to już tak ładnie. Jak skończę to ci przypisz. Łukasz feature mam do zaglądać.

**Lukasz Bott:** Wiesz co to to jest? To jest jedno i drugie, to znaczy tak to jest takie zagregowane część rzeczy już jest realizowana bądź zrealizowana, jeśli jest tam pomysłów to bym bardziej tak, bo umożliwić na nadania jest w języku dla różnych elementów raportu. Kliknij na obrazek, tak. Mamy przykład raportu dashboard akurat tutaj z klejącego się z 3 raportów i tutaj w Zielonej ramce tytuły są przetłumaczone na interfejs, bo korzystanie z interfejsu polskiego tak. No ale niestety źródło danych jest takie, które ma etykiety kolumny po angielsku. Tak, no na na poziomie źródła danych, bo jest to źródło bądź co bądź zewnętrzny, w sensie takim, nawet jeżeli jest to systemowe czy coś, no to tam ciężko jest zrobić etykiety w zależności od języka. Tak więc tutaj pytanie, czy zresztą o tym już jakiś czas temu dyskutowaliśmy, żeby nadać dać możliwość na poziomie raportu nadawania aliasów w zależności od wersji językowej, przy czym i na polach, ale też jak masz tutaj i nie wiem na kolorach czy tu etykietach czy jakiś tam gdzieś danych segregowanych, to zamiast wyświetlać na przykład tak jak na dole masz podpis na osi count Report id no to by można było napisać ilość rekordów. Tak czytam ilość raportów tak, bo to, bo to o to chodzi, nie.

**Damian Kaminski:** W sensie count przetłumaczyć samo?

**Lukasz Bott:** No nawet nie, nie, nie, nie tyle przetłumaczmy ja bym własną etykietę nadał tak żeby to było ewidentnie interpretowane, tak.

**Damian Kaminski:** Dobra, to o k. To po kolei to znaczy tak pytanie, czy to powinno być na poziomie pól na poziomie raportu globalnie? Czy to jednak powinno być tylko dla typu źródła zewnętrzne, definiowane lub systemowe?

**Marek Dziakowski:** Ja bym to ja bym to zrobił po prostu dla wykresy. Że typ wykres i tam ustawiam oś XY jak się nazywa i tyle.

**Lukasz Bott:** Ewentualnie dla wykresów.

**Damian Kaminski:** Ale poczekaj teraz mówimy ogólnie o danych, bo chodzi o czy nie mówimy o nie? No mówimy o danych. W sensie raport created by to jest nazwa pola albo kolumny w źródle definiowanym i teraz czy my chcemy doprowadzić do tego, że ktoś zmienia nazwę pola dla sprawy?

**Lukasz Bott:** Nie dla sprawy tylko to by było na poziomie raportu i mogłoby wyobrażam sobie, żeby mogło być na poziomie raportu. Masz pole wrócić do do tej konfiguracji tego ganta niech będzie gant nie i wejdź i tutaj w wierszach wybrałeś sobie taki pole, nie niosło dawca, ale wyjątkowo na tym raporcie te nie chcę go jako wnioskodawca, tylko na przykład wnioskujący tak i tylko w tym raporcie konkretnie chce tak za etykietować topole, tak więc tutaj by była jak klikasz na te 3 kropki nie pojawia się meni na na nadaj alias tak czytam etykietę.

**Damian Kaminski:** To wnioskodawcę poprawiamy tak. Mhm. Nadaje etykietę tak kostiumową. Jedną czy w językach?

**Lukasz Bott:** No moim zdaniem języka jak już to.

**Janusz Bossak:** A wiecie co to nie jest, to nie jest takie proste.

**Lukasz Bott:** Wiem języka. Nie dlatego ja właśnie nie będę się upierał, dlatego wrzuciłem to narady tak i jeżeli to nie jest proste, no przecież jemy tak tylko, że mamy miszmasz.

**Janusz Bossak:** Nie. Czy ja Jestem za tym tylko, że nie jest takie proste, jakby w tym konstrukcji, o którym mówicie, bo wnioskodawca wrzucony na wiersz w zależności od rodzaju raportu. Albo to słowo jest widoczne wnioskodawca, albo nie, bo jeżeli to będę raport typu kolumny, to będzie widoczne jak będzie piwot to nie będzie widoczne.

**Damian Kaminski:** Ale to możemy też dać tylko dla określonych typów, nie?

**Janusz Bossak:** No tak, ale wolałbym mieć jakby mechanizm uniwersalny. Tak i wtedy już będzie widoczne, tak jak właśnie zresztą tam tym przykładzie mój pomysł taki na szybko idzie w tą stronę, że tak tu Marek i ania pewnie mogą potwierdzić lub zaprzeczyć, że ogólnie wiemy co jest użyte do tego raportu, czyli albo jest w filtrach? Albo jest użyte, nie wiem w sortowaniu albo jest użyte gdziekolwiek tak to wiemy, mamy zbiór informacji, gdzie co jest użyte wróć teraz na na ten edytowanie raportu tutaj dokładnie ta zakładka gdzieś tłumaczenia i w opcjach. 2, kogo my po prostu? Po lewej stronie oryginalna nazwa po prawej przekopiowane ona ta oryginalna nazwa, czyli wnioskodawca wnioskodawca, czyli nazwa wyświetlana na tym raporcie i mogę sobie definiować. Oczywiście tu się pojawia warstwa wielojęzyczności. No bo jeżeli teraz ktoś sobie kombinuje ten raport i nie robi tego tylko dla siebie, no bo jakby robił dla siebie to będzie miał w tym języku, w którym on robi. No ale powiedzmy, że on robi dla takiego idealna, a w nim co najmniej 2 czy 3 języki używają, no więc on, każdy raport każdą nazwę w tym raporcie, który użył, musi tutaj przetłumaczyć. I teraz idziemy dalej. Wyobraźmy sobie, że chłopak robi za chwilę następny raport. Który ma te same rzeczy do pokazania i wszystkie te tłumaczenia musi zrobić na nowo. W tym drugim raporcie, więc robienie tego w moim przekonaniu per raport nie jest wygodne po prostu.

**Damian Kaminski:** Ale wiesz, może być może być zbieżny, a może być rozbieżny to może być potrzeba per raport.

**Janusz Bossak:** Wiele. No właśnie mi się mocno nad tym zastanowić. To jest potrzeba per raport, czy to jest potrzeba bardziej globalna? Znaczy zgadzam się co do tych kantów, to mnie też denerwuje i to one się pojawiają właśnie na etykietach.

**Damian Kaminski:** Czyli systemowych nazw, żeby je po prostu przetłumaczyć.

**Janusz Bossak:** Tak, że count tam czy sum czy min to najczęściej potrzeba albo wellu jeszcze się pojawia, tam potrzebujemy coś, na przykład wartość sprzedaży, a nie sum. Sprzedaż tak, potrzebuję wartość sprzedaży tam napisać, czy sprzedaż w latach. No więc to to się zgadzam, że te rzeczy te agregaty dobrze by było móc nazywać. Tomiast na nazwami poszczególnych forum. No po pierwsze to nazwę.

**Damian Kaminski:** Ja bym był za raportem jak o tym myślę.

**Janusz Bossak:** Poszczególnie. W procesach mamy tłumaczone tak, no bo teoretycznie.

**Lukasz Bott:** I tak no to w procesach tak. No to ja też sobie pomyślałem.

**Janusz Bossak:** No tak tak mamy. Ale uwaga, uwaga, mamy to zrobione w procesach. Więc może?

**Lukasz Bott:** Może trzeba było dorzucić do źródeł tłumaczeń.

**Janusz Bossak:** W tym kierunku moja myśl. Według mnie trzeba dorzucić do źródeł, żeby tam można było określać aliasy dla tych nazw, które tam są i w każdym języku, w jakim potrzebujemy i wtedy tu będą używane tak samo jakby były używane od procesie tłumaczenia po prostu.

**Lukasz Bott:** Były polą dokładnie.

**Janusz Bossak:** Natomiast niezależnie to jest pierwsza warstwa, czyli nazwy takie, które się tam mają wyświetlać, ale ten co co widać na dole ten count Report id. To powinno być ustawiane pr raport absolutny, bo to jest cecha tego raportu. Tak na tym raporcie ja wyświetlam coś i to dla mnie coś oznacza, tak?

**Damian Kaminski:** Dobra, to podsumowując, czyli tak powinno być powinno być coś takiego tutaj. Bo już ja się zgubiłem czy na raporcie nie ma być dobra, czyli po pierwsze raporty ma być natywnie przetłumaczony w zakresie takich rzeczy jak count average i max min. I tak dam max min. No nie trzeba może tłumaczyć, ale nie wiem co tam jeszcze jest, to to na to trzeba zrobić.

**Janusz Bossak:** Nie, nie, nie, nie wiem ile rozumiesz. Jeszcze raz. Pierwsza warstwa nazwy kolumn. Ten raport created by raport tip raport kategorie raport sap kategorii to są rzeczy, które pochodzą ze źródła zewnętrznego. Źródła danych na poziomie źródła danych wprowadzamy tłumacz.

**Damian Kaminski:** Tak.

**Lukasz Bott:** Mechanizm ma mechanizm tłumaczyć dokładnie.

**Damian Kaminski:** Tak to zrozumiałem. To jest proste, no każdą kolumnę możemy nazwać tak, bo w dowolnym języku.

**Janusz Bossak:** To jest zadanie niezależne, koniec zadania tak i już mamy 50% lepiej albo 90%, lepiej teraz idziemy do raportu. Tutaj tak i ten raport, który tam wyświetlasz ten przykładowy, no ma jakieś tam count Report id no to teraz miałby napisane count Raport. No i teraz wszędzie tam w tych miejscach, gdzie jest teraz właśnie jakieś count sumy tutaj agregację. Bo to jest w tym przypadku raportu jest co innego, a jakbyś wziął piwot no to jest co innego. Jakbyś wziął kolumnowy tutaj to będziesz miał oś do opisania, tak. I teraz zobaczcie są. Normalnym naszym normalnym znaczy w systemach, które robią raporty, możesz wejść i sobie oś x oś y opisać i my musimy zrobić podobnie. W raportach opisujesz oś x to, że ona jest kant, coś tam sumy czegoś o k ale ty chcesz dać nazwę napis osi XI, to powinno być osobna jakby gdzieś nie wiem gdzie jeszcze.

**Damian Kaminski:** Tutaj. Wiersze, kolumny, etykieta, etykieta. W nagłówku tech tych 2 yy.

**Janusz Bossak:** To nie jest tak, to nie jest tutaj. Bo to jest no bo na przykład w etykiecie możesz to dać. Suma liczby sum liczby dni urlopu weź podjedź tam teraz gdzieś.

**Damian Kaminski:** Ale zobacz tu, mamy sum, tu mi się wyświetla brzydko sum. A tutaj mamy już przetłumaczone, powinno być po prostu w nawiasie suma po polsku.

**Janusz Bossak:** Ale w ogóle nie chce mieć tego suma.

**Lukasz Bott:** Ale nie nadal. Dane i Damian nadal chyba nie nie nie rozumiesz? Są tłumaczeni suma, suma, liczba dni urlopu, a ja bym chciał to nazwać. Łączna ilość dni urlop.

**Janusz Bossak:** Dokładnie o to chodzi. Nie chcę mieć na.

**Damian Kaminski:** Dobra, okej i macie rację i nie macie w sensie nie wszyscy będą chcieli to re definiować, bo niektórzy będą chcieli uprosić prosto, więc ja bym też zaczął od tego, że tu jednak powinno być po polsku, bo to mamy tylko nie wyświetlamy, a jak ktoś chce zrobić to o k. To nadaje etykietę własną i wtedy tak jak mówicie to moje Jestem, p bo mamy wszystko przetłumaczone, mamy wszystkie dane tylko z jakiegoś powodu tego nie wyświetlamy tu prawidłowo, a to co wy mówicie to już jest kolejny krok.

**Janusz Bossak:** To się zgadza, to się zdaje. To jest zadań. Tak zgadzam się. Dobrze jakby to było tak jak tutaj. Skoro w samej agregację wybieram suma. To dlaczego mi się tu piszesz? Jak się? A skoro pisze się rok obok tam planowany tak year. No to jest rok już dobrze nie, ale no właśnie. Dlaczego proszę się soniu, a nie suma? Więc tu tu się z tobą Damian zgadzam absolutnie natomiast tak z Łukaszem poszliśmy o krok dalej nam chodzi o to, żeby cały ten napis nawias sum.

**Damian Kaminski:** Rozumiem, teraz już rozumiem móc zdefiniować własne m.

**Janusz Bossak:** Tak i to totalna liczba dni wolnych albo wolne dni sobie nazwę. Jakkolwiek sobie to chcę.

**Lukasz Bott:** Albo w albo w tym moim przykładzie na obrazku ilość rekordów tak no bo w kontekście źródła w kontekście źródła dane, które pochodzi z jakiegoś tam bazy, no to raczej mówimy o ilościach na przykład rekordów. Tak, no bo.

**Janusz Bossak:** A liczba reklam?

**Damian Kaminski:** Tak, a nie suma id tak.

**Lukasz Bott:** Tak, tak, a nie jakieś ID?

**Janusz Bossak:** I to najczęściej będzie dotyczyło. Chociaż nie no, wielu rzeczy będzie dotyczył tak, bo jak to przemienisz teraz na weź tam jakiś wykres słupkowy no to będzie na przykład dotyczyło kolumn.

**Damian Kaminski** 48:00  
Kolumny niech będzie i nie zastęp tylko wniosku. To znaczy, muszę to zapisać już?

**Janusz Bossak:** No właśnie też to jest w ogóle słuchajcie dla mnie od samego początku jak robimy ten moduł raportowy po prostu to tak jest. Ja już słyszałem tu jakby argumenty Ani i Marka wszystkich. Ale mnie to po prostu tak męczy, że jest co innego podglądzie. Co innego w edycji, no po prostu.

**Damian Kaminski:** Dobra, słuchajcie, bo żebyśmy całej rady nie spędzili na projektowanie tego? To znaczy tak, zróbmy MVP a potem rozwijajmy czyli. Nasze MVP to jest tak przetłumaczenie to co w zasadzie wyświetlenie tłumaczeń, bo one są już zdefiniowane na trybie odczytu. To jest jedna rzecz najprostsza według mnie totalnie teraz druga rzecz to jest zdefiniowanie na tym poziomie tłumaczeń dla kolumn i przeniesienie tych tłumaczeń na poziom raportów, bo to jest raz, że musimy je.

**Janusz Bossak:** Według to jest to jest ważniejsze, to jest ważniejsze dla raportów systemowych w tej chwili. Użycie tak.

**Damian Kaminski:** Tak i i zróbmy to pod raporty systemowe, czyli tłumaczenie agregacji różnego rodzaju i tłumaczenie kolumn plus wyświetlenie tych tłumaczonych kolumn na raportach, bo to jest też odrębne chyba zadanie tak najgorsza to zapisać, a potem trzeba to pobrać. A potem idźmy dalej dopiero. Bo tu już nasze plany to może sięgają dłużej niż sprintu, nie?

**Lukasz Bott:** O k dobra, to ja to, czyli rozbiję to rozpatruję to na drobne, tak?

**Damian Kaminski:** No a to to co ze sugerowaliście, że zmiany etykiety, bo właśnie w kontekście sumy id-ków na przykład to jest zasadne tym jak najbardziej tym dla raportu biznes może systemowych też. No to kolejne zadanie i tyle. Dobra. Wiecie to wraca. To było już.

**Lukasz Bott:** No chciał zauważyć radę. Nam się skończyła tak 10 minut temu, no ale jeżeli coś zobacz coś jeszcze nie jest takiego.

**Damian Kaminski:** Wyciągnijmy do tej jedenastej. Dobra, to przejrzę tak maile systemowe, to przenieśmy na kolejne stworzenie funkcji do komunikatów. To nie jest krytyczne komunikat informujący aktualizacji. To też wiem propozycje.

**Lukasz Bott:** Wiesz, co to to znaczy? Tak tylko jedną rzecz. Damian to są tematem Mateusza i jak bumerang nawrzucał w piątek, więc przynajmniej może na czwartkowej razie nie przyglądajmy.

**Damian Kaminski:** Tak no to w zasadzie nie ma tu nic krytycznego, jeśli chcemy omówić, to możemy w 10 minut jeszcze jeden temat omówić. Yy, możemy zacząć od tych maili, natomiast to jest bardzo duże wyzwanie i wdrożeń i i deweloperskie i testu testowe i tutaj. Może to powinno być Janusz ujęte na naszej mapie, no bo nie oszukujmy się ten mail wygląda jak z poprzedniej epoki. No i cóż, ale to też nie jest łatwe do poprawienia, bo tu trzeba było podejść do tego szeroko, żeby poprawić wszystko tak, jak poprawiamy wygląd sprawy tak samo. No właśnie to co wychodzi na zewnątrz systemu też należałoby odświeżyć. Natomiast tych szablonów jest bardzo dużo.

**Piotr Buczkowski:** Tylko wbrew wbrew pozorom tutaj nie można robić fajerwerków. Ma być prosto.

**Damian Kaminski:** Tak ma być prosto, ale znowu to co uciekamy w naszym głównym ekranie od szarości, tak samo tu powinniśmy od tego uciec, zrobić jakąś prostą ramkę. Jeśli już chcemy ramkę białe tła i i tyle no. To tak ogólnie, no bo tutaj to trzeba zrobić z tego pewnie za 20 PBI dla różnych szablonów.

**Piotr Buczkowski:** Znaczy mówię. Bo po pierwsze po drugie trzeba każdy taki szablon trzeba przetestować na stronach, które wyliczają jakieś tam współczynnik spamu. Tak, czy taka treść nie będzie kwalifikowana jako spam? Nie jest takie, że sobie tutaj wpiszecie, co chcecie.

**Damian Kaminski:** Więc tu Janusz decyzja, czy po prostu trzeba się tym, czy czy mamy się tym opiekować, czy na razie jeszcze świadomie to wstrzymujemy? Na przykład na pierwszy kwartał przyszłego roku.

**Piotr Buczkowski:** No czy ja. Tutaj wiem, że jest takie coś, że jest problem, że jak ktoś sobie coś to zmieni, to później mu update nadpisze. No szybko można dodać, że wykluczanie, szablonów, z update.

**Damian Kaminski:** No już ten pomysł był i on się nie skończy, że tak powiem nie doszedł do skutku, ale to jest minimum.

**Janusz Bossak:** 100 x 100 razy już o tym mówiliśmy od kilkunastu lat. Czy są od kilku lat? Przynajmniej więc temat trzeba podjąć i go zrobić skutecznie mają wszystkie rzeczy, o których Piotr mówi na uwadze, czyli treść, jakość tego tej treści. To, że właśnie musimy to zaopiekować w momencie nagrywania, czyli aktualizacji. Wszystko to już było mówione. Nawet nie wiem czy nie jest pisane już nawet gdzieś.

**Damian Kaminski:** Masz rację, tylko znowu zgodnie z naszą tendencją było mówione, że nie to nie z bazy danych, tylko już musimy zrobić do tego interfejs i tak dalej doszliśmy już do takiego powiedzmy projektu, który pewnie trzeba było osiągnąć. 2 sprinty, 2 osoby i to wtedy zrobią pytanie, jakie określamy MVP wtedy świadomie przesuwamy to na przykład na przyszły kwartał, a dzisiaj jak ktoś to sobie zmienić, to niech sobie zmienia na własną odpowiedzialność, uwzględniając to, co powiedział Piotr, że gdzieś komuś nie dojdzie, czy czy cokolwiek innego. Tylko teraz pytanie jeszcze, bo bo tu już o tym też rozmawialiśmy, Piotrze.

**Janusz Bossak:** No to trzeba te mapy, jeżeli nie ma finansowania to musi być naród mapy.

**Damian Kaminski:** Dokładnie więc dobra globalną zmianę, wstrzymujemy natomiast, powiedzmy co do zmian ka stołowych po stronie klientów, jak to zaopiekować? Czy to ma być jedna kolumna? Załóżmy, idziemy po totalnym minimum, czyli tylko backend, czy to ma być jedna kolumna, która tylko oznacza, czy updatować czy nie i po prostu poprawiają ten domyślny? Domyślny szablon czy ma być druga jakaś kolumna, która będzie zawierać szablon i wtedy? Powiedzmy jakaś kolumna, która decyduje, który szablon wysyłać czy domyślny czy customowy. Rozumiesz, rozumiecie o co mi chodzi?

**Janusz Bossak:** Mam wrażenie, że myśmy to wszystko osią mówili. Szukam właśnie w dokumentację do tego.

**Damian Kaminski:** Janusz masz rację, ja to poruszałem tylko doszliśmy do wniosku, że właśnie zaczęliśmy od takiego minimum, potem, że jednak to ma być w ustawieniach systemowych, ma być interfejs, bo to jest zbyt skomplikowane i nie ustaliliśmy takiego właśnie MVP. Jak dla mnie, jeśli chcemy zachować pełną kompatybilność wsteczną, to powinniśmy dodać do maili 2 dodatkowe kolumny, czyli customowy szablon i jedna kolumna decydująca, według którego ma wysyłać. My zawsze poprawiamy nasz domyślny szablon, jak ktoś ustawi kolumnę, że chce to stosować customowy szablon, to go sobie definiuje i bierzemy wtedy dane z niego i on ma nad nim władzę i to będzie minimum, które będzie można rozwijać. I mogę to tak opisać, jeśli nie widzicie tu żadnych zagrożeń.

**Marek Dziakowski:** Starszy pewnie tylko jedna kolumna jak jest uzupełnione customowy szable no to niech korzysta z customowego jak nie no to systemowe.

**Lukasz Bott:** W sensie jedna kolumna w sensie znacznik, że to, że sobie go skasować i przy aktualizacji bazy danych.

**Damian Kaminski:** Nie, nie, nie chodzi Markowi o customowy w sensie treść customowego, jeśli jest wypełniona, to wtedy z niego bierze, jeśli jest puste, to to to domyślne.

**Lukasz Bott:** A o k dobra. To jest standardowy dom.

**Damian Kaminski:** Tylko no. Tylko jeśli byśmy potem przekładali to na interfejs, to ktoś sobie tworzy customowe, ale jeszcze nie chce z niego korzystać i ma tam jakieś switch. Tak to sobie wyobrażam później.

**Lukasz Bott:** No ale to wiesz, ale to możesz.

**Damian Kaminski:** Więc ten Switch mógłby być już po stronie backendu w postaci kolumny.

**Marek Dziakowski:** Czy to na produkcji raczej tak się nie robi takich rzeczy, że sprawdza się jakby idą maile, tylko gdzieś tam sobie na teście to pewnie będą robić produkcji rzeczy, wrzucają takie konkretne tempa i ty.

**Damian Kaminski:** Masz rację i nie masz, bo nie wszyscy mają testa, w sensie są też mali klienci, którzy mają tylko produkcję.

**Piotr Buczkowski:** Wszyscy wszyscy mają test, niektórzy mają produkcję.

**Lukasz Bott:** Produkcyjnie korzystają z testów, dobra? Nie słuchajcie jeszcze jedno pytanie, teraz mi wyszło jaka to jest skala? Ja wiem, że temat wraca jak bumerang. Janusz ma racje, że to już przygotowaliśmy n raz.

**Damian Kaminski:** Wszyscy won wszyscy duzi wszyscy on mam na myśli, że wszyscy duzi mają z tym problem. Orlen co aktualizacje poprawia szablony maili.

**Lukasz Bott:** O k no dobra, nie nie, ale chodzi nie wiesz, no chodziło mi o to czy ale czy na pewno wszyscy duzi? No muszę Orlen teraz oglądamy LPP.

**Damian Kaminski:** I inni też mają z tym problem tylko no no cóż mają zrobić, no jak nie działa, no właśnie.

**Piotr Buczkowski:** Mam zrobić to pomijanie wskazanych maili. Zrobię to w godzinę. Trzeba przebadajcie pomijania, gdy tu maili.

**Damian Kaminski:** A pomijanie no tak tylko czy to będzie też przyszłościowe w sensie czy jak zrobimy tak ad-hoc?

**Piotr Buczkowski:** Nie. Nie, ale, ale rozwiążę problem obecny.

**Damian Kaminski:** No dobra, ale zrobienie dodatkowych 2 kolumn czyli.

**Lukasz Bott:** Rozwiąże ci problem w Orlenie czy?

**Damian Kaminski:** Pytanie jaki to jest? Wiesz porównanie ile na to trzeba poświęcić pracę, a ile na to? Żebyśmy nie robili rozwiązanie?

**Piotr Buczkowski:** No na pomijanie update godzinę.

**Damian Kaminski:** A na dorobienie dodatkowego customowego i jakiegoś znacznika, z którego korzystaj.

**Piotr Buczkowski:** Więcej.

**Damian Kaminski:** Czyli 5 czy 20?

**Lukasz Bott:** No dojść jeszcze testy.

**Piotr Buczkowski:** No nie no bo to trzeba byłoby wszystkie tak pobieranie szablonów, że szukaj najpierw z customowym, tak.

**Damian Kaminski:** Znaczy, bo zmierzam do tego, że słuchajcie, jeśli pójdziemy w to, co Piotr, bo to jest minimum rozwiązanie i jest spoko, tylko wtedy, jeśli my za kwartał za pół roku zrobimy update wszystkich maili, to trzeba będzie wykonywać pracę ręczną, nie.

**Piotr Buczkowski:** Nie. Nie, nie zrobimy update wszystkich maili, zrobimy nowy mechanizm.

**Damian Kaminski:** Czyli nową jakość nowe, nieistniejące dzisiaj miejsca, gdzie będziemy to składować? Tak.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** O k no dobra, to jeśli taka jest wizja updatu całego mechanizmu szablonów maili, no to k. To twoje rozwiązanie jest. Z jakąś przyszłością? Tak? No to tak, zróbmy to tak, zróbmy jedną kolumnę, która steruje czy datuje przy podnoszeniu wersji czy nie i jak ktoś tam sobie ustawi, że nie no to to nie audytu i tyle jest jakiś custom ustawiana true i wtedy nie datujemy.

**Janusz Bossak:** Czekam na menedżerskie spotkanie na razie dzięki.

**Lukasz Bott:** Tak kończymy, ale to takie minimum ustali.

**Damian Kaminski:** Dobra, Piotr, to zrobię do tego, PA ja takiego w po minimum.

**Lukasz Bott:** No reszty temat.

**Damian Kaminski:** No i tyle ich nie przedłużaj my w takim razie mamy 11 resztę na czwartek.

**Lukasz Bott:** Tak rośnie. Dobra na razie cześć.

**Damian Kaminski:** Cześć.

**Marek Dziakowski:** Cześć.

**Janusz Bossak:** zatrzymano transkrypcję
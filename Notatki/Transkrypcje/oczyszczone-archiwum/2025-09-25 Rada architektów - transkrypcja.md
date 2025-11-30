**Data spotkania:** 25 września 2025

**Piotr Buczkowski:** Ktoś coś mówi?

**Kamil Dubaniowski:** No coś nie ma chłopaków, no patrzę.

**Piotr Buczkowski:** Łukasz, ktoś napisał, że się spóźni tak chwilę.

**Kamil Dubaniowski:** Zapisane. Już patrzę, ja też mam to gdzieś. Może tak... dopiero tak pewnie... I tak będą ciebie tematy, możemy zacząć bez wyświetlania, bo wczoraj z tym adresem padło. Że oni w tym momencie z poziomu bazy danych...

**Damian Kamiński:** Poczekaj chwilkę Kamil, a Mateusza nie, bo mówi o AI, to jeszcze gadać nie?

**Kamil Dubaniowski:** Nie, nie, nie. Tylko oni akurat tam AI-owe tematy to jak rzucę chyba wszystko na czat, ale to myślę, że można samym spotkaniem. A tutaj, bo to trochę się znaczy zdziwiłem – nie zdziwiłem, bo nie korzystam z tego jakoś czynnie – ta praca wspólna na dokumentach. Oni w tym momencie w obawie przed tym, że jakiś dokument przed zakończeniem edycji zniknie z SharePointa, to puszczają z poziomu bazy zamykanie – tak mi przynajmniej tłumaczył – z bazy czy regułą... Nie pamiętam. Regułą zamykanie otwartych w trakcie edycji dokumentów po jakimś tam okresie. Od momentu ich jakby otwarcia, bo czasami te dokumenty wiszą jako "w trakcie edycji", nie kliknęli po prostu ludzie przycisku "Zakończ edycję" po kilka tygodni. No a w tym czasie dokument może zniknąć z tego Cache'a i wtedy będzie trochę już słabo albo nie wróci nowa wersja do AMODIT-a.

**Piotr Buczkowski:** Tak.

**Kamil Dubaniowski:** No pytanie, czy nie mógłby to być może jakiś Job, który po prostu przechodził i na koniec dnia gdzieś tam o północy zamykał edycję w obecnym stanie?

**Piotr Buczkowski:** Pytanie, czy tak ma być, czy wszyscy tak chcą?

**Kamil Dubaniowski:** No tak, no to wtedy ci co nie chcą, to po prostu nie aktywują tego Joba. Ale tutaj ewidentnie no u nich to jest problem, że no znaczy wiecie – wydajnościowo, no bo oni piszą reguły okresowe, które mielą te sprawy.

**Piotr Buczkowski:** Wiem, sam to Ronowi podpowiedziałem.

**Kamil Dubaniowski:** No znaczy, wydaje mi się, że pewnie moglibyśmy pójść w kierunku tego. No i tak jak mówię, jak ktoś nie będzie potrzebował tego zamykania, no to po prostu nie użyje tego, prawda? Tyle. Trzeba by pewnie jakoś określać tak gdzieś coś jakby jaki jest termin.

**Piotr Buczkowski:** No tak, jakieś typu, że zamykaj automatycznie edycje powiedzmy po 2 dniach.

**Kamil Dubaniowski:** No.

**Piotr Buczkowski:** Braku jakiejś akcji użytkownika. Tylko, że to musi być akcja po stronie SharePointa, tak. Czyli powiedzmy, że dzisiaj coś tam pisałem, a zostawiłem do poniedziałku, no to w poniedziałek już powiedzmy mi wróci automatycznie. A jeżeli jutro coś zrobię, pojutrze coś zrobię, no to znaczy, że ja pracuję, tak.

**Kamil Dubaniowski:** No tak, OK. No dobra, ale uznajemy, że słuszne i mogę to kosztować. I podobny temat co robią teraz, może też o tym rozmawialiście. Sprawy, które zostały uruchomione i nie poszły w obieg. W Rossmannie pamiętam, że robiliśmy takie podejście. Oni niekoniecznie naciskają na kompleksowe podejście, tylko znów oni teraz z poziomu bazy, albo właśnie regułami, po roku czy po dwóch od utworzenia, jeśli sprawa nie wyszła w obieg, no to usuwają masowo tam właśnie z bazy. Chyba jak dobrze pamiętam. I wydaje mi się, że tutaj w tym kontekście też w sumie mogłoby być jakieś ustawienie systemowe, że na przykład ustawiasz sobie rok, właśnie jakieś okresy. Nie wiem. 10 miesięcy, 5 miesięcy, 3 miesiące. I żeby Job od tej daty utworzenia usuwał takie sprawy, które wiszą. Tak, że nie jakoś tam permanentnie, ale wydaje mi się, że...

**Damian Kamiński:** Natomiast no właśnie, żeby po prostu... "sprawą usuniętą" masz na myśli?

**Łukasz Bott:** Co tam jak mówisz, tak jakbyś chustę wsadził między zęby.

**Piotr Buczkowski:** W ogóle.

**Łukasz Bott:** Kimś?

**Damian Kamiński:** Jeszcze raz.

**Łukasz Bott:** Jakbyś hełmofon założył w czołgu siedział.

**Kamil Dubaniowski:** Myślę, że słuszne, że nie będą musieli teraz robić tam zapytania, żeby znaleźć te sprawy. Tak, to to wszystko sobie wyliminują i samo usunięcie też wykonać. Oby no i nie mówię tu o `CaseIsHidden` tylko po prostu właśnie `CaseIsHidden` i nawet byłbym za tym, to może mogło być jakieś dodatkowe ustawienie akurat, czy usuwać takie które no mają jakieś dane też wprowadzone. Ale spodziewam się, że jak coś wisi rok, to po prostu ktoś zaczął wniosek na przykład urlopowy i go nie złożył.

**Piotr Buczkowski:** Czy to były właśnie wnioski urlopowe, że często ludzie składali wniosek i [nie wysyłali], tak żeby zobaczyć, ile mają dni urlopu?

**Kamil Dubaniowski:** Dokładnie, no.

**Damian Kamiński:** Teraz mnie słychać dobrze?

**Kamil Dubaniowski:** Tak, tak.

**Łukasz Bott:** Lepiej.

**Damian Kamiński:** Znaczy ja się z wami zgadzam... co, źle dalej?

**Kamil Dubaniowski:** Nie, dobrze.

**Damian Kamiński:** OK. To znaczy ja potwierdzam, że tego typu rozwiązania trzeba było stosować regułami okresowymi, które czyszczą, jeśli ktoś nie edytował sprawy na pierwszym etapie. I według mnie to idzie do `CaseIsHidden`. I do spraw, które pozostają na pierwszym etapie, można by było wprowadzić usprawnienia do `CaseIsHidden` na poziomie globalnym systemu, że "usuwaj sprawy starsze niż". Jak ktoś oznaczy, to określa sobie po jakim czasie, powiedzmy rok, i może system sobie to wyczyści jakimś Jobem. A tu z kolei na poziomie procesu bym powiedział, bo mogą być takie procesy, w których coś powstaje tak – rejestr – i on nie powinien być opróżniany, bo nikt go nie edytuje i po prostu [jest] na pierwszym etapie. A są takie, które są na pierwszym etapie, no ktoś zdefiniował, ale nikt niestety... etap początkowy, nikt ich nie ruszył przez określony czas. Który na poziomie procesu można było zdefiniować, to też wywala.

**Kamil Dubaniowski:** Znaczy ja bym szedł w kierunku globalnego ustawienia, bo to raczej nie będzie tak, że faktury mi usuwaj po roku, a wnioski urlopowe po pół. Pewnie globalnie.

**Łukasz Bott:** No nie Kamil, nie czekaj, czekaj...

**Piotr Buczkowski:** Nie, nie. Jak najbardziej.

**Kamil Dubaniowski:** Ale rejestr w ogóle mógł z tego wyłączyć.

**Damian Kamiński:** Znaczy może być tak, że no właśnie, że niektórych nigdy nie usuwaj.

**Kamil Dubaniowski:** Rejestr w ogóle bym nie jakby same procesy, no bo to ci wisi w zadaniach do wykonania, a rejestrem trzeba zarządzać ręcznie. To już się pewnie niestety to trzeba robić odpowiedzialnie.

**Damian Kamiński:** No dobra, ja podałem przykład tylko. Wiesz, czasami masz rację i nie masz, bo czasami może być sytuacja taka, że ktoś wykorzystuje proces jako rejestr, bo musi mieć... Nie wiem, jakiś tam zakres uprawnień. Bo jest to matryca jakaś, tak, i nie wszyscy mają to widzieć, więc... Nie skupiaj się, że tylko techniczny podział, to jest to, co jest przechowywane biznesowo.

**Łukasz Bott:** Czyli ja bym to zrobił na poziomie definicji procesu, ale w sensie takim formularza i niezależnie, czy to jest proces, podproces, rejestr. Ustawienie jakieś takie wiesz: "nigdy nie usuwaj tych właśnie spraw, które nie poszły w obieg" / "Usuwaj, ale..." i tutaj podaję jeszcze jakieś tam interwał, po jakim czasie, tak?

**Kamil Dubaniowski:** No dobra, no jakby takie... swój czas poziomu bazy sobie zrobią. Razem wreszcie na wszystkie procesy, które chcą.

**Damian Kamiński:** No i to też pewnie powinno robić `Hidden` najpierw, nie? A potem powiedzmy dopiero po roku. Bo ktoś może stracić i powiedzieć "halo, ale to czegoś nie przewidzieliśmy". Tak więc tak krokowo. I to jeden Job mógłby robić: tak usuwać sprawy nowo założone i usuwać sprawy w ogóle te, które są w koszu. Jeśli tak administrator podejmie decyzję.

**Kamil Dubaniowski:** Tak, tak, tak.

**Łukasz Bott:** Damian, i teraz to jest... wszystkie moje szkolenia szlag trafił. Bo ja na wszystkich tłumaczę, jak działa kosz. Mówicie, że on jest bezdenny i trzyma do końca świata.

**Damian Kamiński:** Ale on dalej może być bezdenny. Ja mówię tylko o opcji – ktoś może podjąć decyzję, że "czyść mi go", a nie, że jest to przez nas narzucone, że ma być czyszczony. To jest według mnie parametr. Jeśli ktoś chce, to ustawia jakiś interwał, powiedzmy bufor, tak? Rok, 2, 5 lat od określenia jako `CaseIsHidden` i wedle uznania, tak.

**Łukasz Bott:** No tak, tak, tak. Nie, no to... Chodzi... nie, bo jest dokładnie tak. No jeżeli to sparametryzujemy, tak, że opróżniamy kosz, tak. Opróżniamy co jakiś tam interwał. Czyli no bo ja tłumaczę zazwyczaj jako właśnie taką analogię do kosza, który masz w systemie plików. W Windowsie. On, jeżeli tam sobie nie zmienisz tego, to chyba domyślnie co 30 dni jest po prostu opróżniany, tak?

**Damian Kamiński:** W Windowsie tak jest.

**Łukasz Bott:** Tak, tak, tak mi się wydaje.

**Damian Kamiński:** Nie wiem. Ja powiem ci szczerze, że w Windows 95 może w XP-ku to czyściłem, a od tamtej pory to rzadko, chyba że gdzieś jest przeładowany dysk. Bo dzisiaj te dyski są tak duże, ale nie zauważyłem... wydawało, bo ja bym powiedział, że nie jest czyszczony, ale może się mylę? Może coś takiego wprowadzili?

**Piotr Buczkowski:** W Windowsie nie jest czyszczony. W Google jest.

**Damian Kamiński:** A no to tak, to masz rację, tak, tak tak. W poczcie czy też na dysku Google'owym to masz rację, chyba 30 dni.

**Piotr Buczkowski:** W Windowsie nie. Tak dokładnie.

**Damian Kamiński:** No dobra, mniejsza o to. Według mnie to nie powinniśmy nic narzucać. Jeśli już to wprowadzamy opcję, która pozwala czyścić. Jak ktoś nie chce, nie musi i tyle. Po prostu dzisiaj, żeby wyczyścić sprawy z kosza trzeba napisać regułę, bo nawet nie da się tego zrobić zbiorczo jakimś wywołaniem. A tak dałoby się i ten Job. No tu się pojawia kolejna, powiedzmy jeszcze taka wynikająca może z tego potrzeba, że tego typu Job na przykład niekoniecznie powinien móc się... ustawiać częściej niż jeden dzień. Ale to już jest... Nie wiem czy są inne takie Joby, które moglibyśmy tak określić, więc to już jako tylko dygresja. Że może niektóre Joby powinniśmy wprowadzić ograniczenie, że nie powinny się wykonywać częściej niż tak...

**Piotr Buczkowski:** Może warto? Miasteczko, który ma się wykonywać na przykład co godzinę i tyle.

**Damian Kamiński:** No no no, na pewno tak.

**Piotr Buczkowski:** To po to wysyłanie powiadomień tych takich odroczonych, tak? Że na przykład nie chcę od razu, tylko raz dziennie czy tam co godzinę. Te zbiorcze, on musi się co godzinę wywoływać.

**Damian Kamiński:** No to... Nie no zgadzam się z tobą, no reguły okresowe czasami muszą się odpalać co 5 minut. Tak więc ten Job też musi chodzić z odpowiednią częstotliwością. Mam na myśli, że tutaj w związku z tym, że powiedzmy taki [Job czyszczący] by powstał, to może do tego Joba powinniśmy od razu dać ograniczenie, że nie można go ustawić tylko w perspektywie dni powiedzmy, tak? Czy czy tam tam jest Month, tak?

**Łukasz Bott:** Nie możesz częściej niż... Wiem. Tak, no.

**Damian Kamiński:** No o to mi chodzi. I może może w tym kierunku też trzeba było przejrzeć, czy jeszcze jakieś tak powinniśmy ustawić, żeby ktoś się nie zapędzał i nie obciążał zbędnie. Ale dobra to taka dygresja. Dobra, Kamil, mów co tam dalej? Bo jeszcze pewnie coś jest.

**Kamil Dubaniowski:** Wydaje mi się, że takie pilne tematy, no bo reszta to jest na przykład do formularza sprawy – przełączanie sekcji. Bo oni mają sekcję w zakładkach i często mimo tych zakładek sekcje są długie. Jak ktoś zeskroluje się na sam dół, no i sekcji w zakładce, to teraz żeby przejść na kolejną zakładkę musi wracać na górę i przełączać się na kolejną. Oni właściwie to jest tak, że lecą sekcja, zakładka po zakładce i uzupełniają dane na formularzu i właściwie za każdym razem zjeżdżają na sam dół, powrót na górę, zmiana zakładki, uzupełniają, jadą do samego dołu, powrót na górę. Oni chcieli, żeby na dole formularza...

**Damian Kamiński:** No i co sugerujesz? Były zakładki?

**Kamil Dubaniowski:** Dać strzałkę lewo/prawo do następnej sekcji, po prostu do następnej zakładki. Bo nie chcę też, żeby zamrażać belkę sekcji z zakładkami, no bo zmniejszy nam się formularz, tak. W sensie będzie cały czas zasłaniała belka pola.

**Damian Kamiński:** Zgadzam się.

**Kamil Dubaniowski:** Więc tego też nie chcę, bo zaraz będą uwagi co do kompaktowości, ale ten pomysł, że na samym dole sprawy jest strzałka w prawo do następnej zakładki – myślę, że nie jest zły.

**Damian Kamiński:** Albo alternatywnie zakładki też na dole.

**Kamil Dubaniowski:** Albo tak, no ale dobra to jakby na razie...

**Piotr Buczkowski:** Nie, nie, nie, nie, nie, nie.

**Łukasz Bott:** Nie, ja też jestem za tym. Ja też pomyślałem o strzałkach.

**Damian Kamiński:** Lepiej strzałki.

**Kamil Dubaniowski:** Mogłaby być "Następna", tak, i wręcz jej nazwa, tam gdzieś w nawiasie czy coś w tym stylu, i "Poprzednia", jeśli jest jakaś. No bo to nie będzie jak to jak chcesz przeskakiwać gdzieś już tam z piątej na dziesiątą. No to lecisz do góry, trudno. Ale to jest do takich zastosowań, gdzie właśnie faktycznie uzupełniasz jakiś formularz złożony z kilku etapów i sobie przełączasz. Myślę, że fajny pomysł.

**Łukasz Bott:** Tak.

**Damian Kamiński:** No tak, tylko według mnie pomysł fajny, tylko znowu to jest gdzieś tam pod ich potrzeby. Może trzeba by to im jakoś zaproponować pakietowo, co chcemy zrobić i powiedzieć żeby się dołożyli, nie?

**Kamil Dubaniowski:** Tak, dlatego mówię. Co do tamtych nie mam wątpliwości, że to jest ogólne i słuszne. Tutaj może faktycznie można z nimi pogadać, czy tak się coś zrobić?

**Piotr Buczkowski:** Nie. Według mnie zostawienie, żeby zakładki były zawsze widoczne, będzie OK.

**Kamil Dubaniowski:** No trochę się obawiam, że jak właśnie uwag co do tej kompaktowości.

**Damian Kamiński:** Nie, nie, właśnie tutaj zamrażamy... zmniejszamy ilość przestrzeni roboczej.

**Piotr Buczkowski:** No tak żeśmy już zmniejszyli, że na przyciski...

**Kamil Dubaniowski:** To jest jeden wiersz teraz. Tam nie do końca się z tym [zgadzam], bo wyszło chyba nawet teraz bardziej kompaktowo niż było, bo zniknęła tabelka z dokumentami i tak dalej, więc to teraz mamy 2 wiersze zajęte... Ale to już... No dobra, znaczy to dlatego mówię – tamtych byłem pewien, że nie wymagają jakoś super dyskusji. To warto by było pewnie przemyśleć i zaprojektować, żeby to było uniwersalne. Co oni jeszcze tu mi dali? Mamy ten nowy w ustawieniach procesu widok... to robił Mariusz chyba z tobą, Damian – te powiązania.

**Damian Kamiński:** No.

**Kamil Dubaniowski:** No to wiemy, że to nie jest docelowy chyba wygląd, tak, także do tego by wrócić. Tam na górze jest ta...

**Damian Kamiński:** No nie, nie, nie, na pewno. Ale co, powiedzieli, że jest spoko tylko kolor, zbyt kolorowo?

**Kamil Dubaniowski:** Znaczy, nie, nie o to chodzi. Nawet 2 uwagi. Pierwsza, że tam na górze jest Legenda i oni to zrozumieli na pierwszy strzał, że to są filtry i chcieli w to klikać, żeby na przykład tylko grupy zostały. Jakie są powiązania grup w tym procesie? Więc ta Legenda albo gdzieś tam pewnie musi spaść na dół, a funkcjonalność filtrów tam na pewno się przyda, bo czasami może być tego sporo tych powiązań. I faktycznie chcesz się skupić tylko na grupach, bo szukasz jakichś powiązań, zależności co do grup, to też fajnie.

**Damian Kamiński:** Mhm.

**Kamil Dubaniowski:** Im pokazałem, że ja zapytany, jakie grupy biorą udział w tym procesie, normalnie wylistowałem na podstawie kodu reguł wszystkie grupy, które tam były wymienione i weryfikowaliśmy. I nawet się zgadzało, bo to są ich często jakieś tam właśnie tematy, tak, że oni muszą dać informacje, jakie grupy są używane w tym procesie. No i nie ma tego, znaczy teraz to jest tabela, to powiązań to... Więc to pierwsza uwaga: Legenda i przydałyby się filtry.

**Damian Kamiński:** Mhm. Ale ona nie czyta reguł, więc ona też jest ułomna jeszcze, nie czyta.

**Kamil Dubaniowski:** No więc, więc tak. Tym bardziej ten AI się powinien przydać. I co do tego, oni też no niestety, ale na ten moment dokumentację do procesów piszą sobie poza AMODIT-em. Jak pewnie większość, którzy tą dokumentację w ogóle robią dokumentację do procesów. I powiedzieli, że bardzo by im się przydał eksport tego, bo teraz co z tego, że mają te powiązania, jak muszą je przepisać do dokumentacji? A tak to by sobie wyeksportowali JSON-a czy jako gotowca więc tam z eksportu... no ale tak jak mówię to są takie niuanse już.
Co dalej? Statystyki procesu. Czyli ile jest spraw w tym procesie, kiedy została utworzona ostatnia sprawa w tym procesie? Bo oni mają tak dużą skalę, że jakby informacja czasami do nich nie dotrze, że dany proces już w ogóle został wygaszony, nie jest używany, a wisi cały czas i gdzieś tam. Tak, więc oni po tym by sobie mogli odpytać patrząc, że ostatnia sprawa w tym procesie była zrobiona rok temu, no to by zapytali, czy ten proces ma nową wersję, czy w ogóle już było, nie używają tak. I coś takiego. Ja widzę jako Raport Systemowy, tylko no oni od razu zaznaczyli, że lokalizacja aktualnie tych raportów systemowych i konieczność ich gdzieś tam szukania... A w tych zwykłych raportach to nie... ja pamiętam, że był pomysł i oni wręcz nawet bez naszych, gdzieś tam moich sugestii to samo zasugerowali, żeby te statystyki, które mieliśmy dawno temu, w prawym górnym tym pasku ustawień – tam, gdzie są użytkownicy, grupy, słowniki – to żeby tam logami systemowymi dodać właśnie odnośnik do tych raportów systemowych.

**Łukasz Bott:** No to tak będzie.

**Kamil Dubaniowski:** No i tak mi się właśnie wydaje, że że o tym też dyskutowaliśmy. No to to jakby tyle. Plus właśnie uwzględnienie... Nie wiem czy takie raporty systemowe mamy, no ale żeby były właśnie w tym kontekście, tak? Żeby analizować sobie, czy dany proces jest aktywny, kiedy miał ostatnie uruchomienie, ile ma spraw? To to to jakby ich taka główna potrzeba.

**Łukasz Bott:** OK. Dobra, to wiesz co, to to jest złe. To teraz dopisałem na listę, bo to chyba da się taki raport. Zrobiło się jakoś tak sensownie.

**Kamil Dubaniowski:** Trzeba by rzucić okiem, co my w tych statystykach rejestrowaliśmy, bo tam była też chyba właśnie aktualna liczba użytkowników, żeby nie było tak... bo te statystyki to ostatecznie wywaliliśmy na poczet raportów systemowych. Nie ma już w wersji czerwcowej tej zakładki statystyki i przydałoby się zobaczyć, czy wszystko pokrywamy, co było w tych statystykach.

**Łukasz Bott:** Wiesz co? No, ja rozmawiałem wczoraj z tym zdaniem [klientem?], to podobne rzeczy odnośnie użytkowników zgłaszał. Tak więc zrobimy. Coś tam zaproponujemy, jakieś raporty.

**Kamil Dubaniowski:** Coś czym mnie zaskoczyli – ponoć nasz marketing bardzo promuje, że AMODIT jest narzędziem CLM (Contract Lifecycle Management) do zarządzania dokumentacją, taką powiedzmy jakąś bardziej nie wiem, ja to rozumiem prawną, tak? Że nie nie do końca, że jesteśmy w stanie generować te dokumenty na podstawie formularzy. No ale wydaje mi się, że to jest bardziej pod kątem tego... co, nie wiem czy wy byliście na hackathonie? Co robił dział Piotr Wągiel dla jakiegoś tam urzędu? To jest takie narzędzie. A nie AMODIT. Nie wiem skąd to się w ogóle na LinkedInie pojawiło i czemu tak bez naszej wiedzy trochę. I ludzie zaraz zaczną o to pytać, ale w ogóle nie wiem co my w tym zakresie zrobiliśmy, bo nic z tego co kojarzę ostatnio...

**Łukasz Bott:** Czyli zupełnie ktoś inny.

**Damian Kamiński:** Ale masz ten link?

**Kamil Dubaniowski:** Nie, wiesz co, nie nie znalazłem. Wczoraj wpisałem AMODIT CLM tak ogólnie na Google, no to nic nie podpowiedział, ale na LinkedIna nie zajrzałem, już tam skończyliśmy dosyć późno to spotkanie.

**Anna Skupińska:** W sumie CLM to jest coś z zarządzaniem dokumentami.

**Kamil Dubaniowski:** Bardziej tworzenie tej dokumentacji. Tak ja to zrozumiałem.

**Anna Skupińska:** Znaczy on to potrafi generować dane na podstawie tego, co użytkownicy... a nie za to chyba jakimś CLM-em wiemy.

**Kamil Dubaniowski:** No dokładnie.

**Damian Kamiński:** Znaczy no trzeba by się dowiedzieć.

**Piotr Buczkowski:** Tylko mi Contract Lifecycle Management... to bardziej jakiś cel.

**Damian Kamiński:** Bo to jak nie mamy przykładu, to też ktoś mógł zinterpretować po swojemu. Trzeba się odwołać do konkretnego wpisu i przeczytać go w naszym rozumieniu.

**Kamil Dubaniowski:** W międzyczasie poszukam. Dobra, znaczy myślę, że tyle. Tam padały jeszcze uwagi do AI, które wam wrzucałem na tym niezależnym czacie. O, i to tłumaczenie formularzy. Uważam, że jest też marketingowo i ogólnie funkcjonalnie słuszne, żeby sobie stare formularze potłumaczyć wręcz AI-em. Jakby patrząc na to, jak sobie radzi przy tworzeniu nowego procesu. Sam pewnie też mógłby te tooltipy pododawać do pól, no bo będzie w stanie pewnie sensownie je opisać. Coś, czego konsultanci nie robią. Więc nie tylko na zasadzie, że tworzyć nowy proces, ale wydaje mi się, że ten AI też mógłby wspierać już istniejące. Bo ja sobie sam zdefiniuję formularz, ale nie chce mi się pisać tych opisów czy robić tłumaczeń, więc tam mógłbym odpalić wtedy na zasadzie akcji: "tak, że tutaj mi teraz przetłumacz te pola na niemiecki".

**Damian Kamiński:** Dla istniejących.

**Kamil Dubaniowski:** Dla istniejących, które ja sam sobie zrobiłem, ale nawet dla tych, które teraz po prostu dzisiaj zaczynam nowy proces, ale nie chcę go robić z AI-em. Zrobię go sam, no bo tak jak chcę. Przecież wiadomo, że to jeszcze będzie długo... to będzie tak wyglądało, że sami będziemy definiować te procesy. Zrobię sobie je po angielsku. No ale teraz potrzebuję tłumaczenia na polski, niemiecki i czeski.

**Damian Kamiński:** No myślę, że to tak zwłaszcza dla wsparcia. No wrzuciłem tutaj ten CLM jako Contract Lifecycle Management. Nie wiem czy wy to tak... przedstawiciel, nie usłyszałem, no to mamy bym powiedział. Jeśli tak to rozumieć. Tak, czyli przygotowanie... od przygotowania do archiwizacji umowy, tak.

**Kamil Dubaniowski:** A ja zrozumiałem właśnie bardziej pod kątem... Może wiecie o co chodzi, że nasze szablony nie są w stanie dobrze przenieść tych danych na... no w sensie z formularza na szablon, żeby to faktycznie uznać za coś, co później ma ładne formatowanie i nadaje się do generowania PDF i podpisu. Bo jak wchodzą jakieś paragrafy inne rzeczy, no to nie mamy takiego ładnego edytora po stronie AMODIT-a, żeby te dane zbierać.

**Damian Kamiński:** No nie mamy. Mamy pewne ograniczenia, ale niemniej no ja uważam, że w Orlenie ładne umowy powstają w AMODIT-cie i tam jest nie wiem, już 20 szablonów, które...

**Łukasz Bott:** No ale nadal używasz szablonu Wordowego, tak? Który odpowiednio pobiera dane. Tak, no to...

**Damian Kamiński:** Tak, tak, tak, tak, tak.

**Łukasz Bott:** Dużym problemem... słuchajcie, jeżeli jest sam tam tekst jakiś, nie, no to jeszcze może pobiera. Ale dużym problemem z dokumentami generowanymi na podstawie tych szablonów to jest to, że no słabo sobie radzi – nie wiem – z prezentowaniem tabelek, tak. Zwłaszcza tam, jak wiesz jak to...

**Damian Kamiński:** No dobra, ale w jakiej umowie masz tabelkę biznesowo?

**Łukasz Bott:** W biznesowej no nie, no może się zdarzyć jakaś tam tabela, nie wiem tylko pewnie by zazwyczaj to będzie jedno, tam kilku kolumnowa maksymalnie. Kto sobie z tym poradzi?

**Damian Kamiński:** Dobra, no bo to jest może być długa dyskusja. Powiem tak: tabelki obsługujemy, można sterować ich szerokością, można sterować ich wielkością czcionki, bo to było dołożone jakieś rok czy 2 lata temu. Jest artykuł...

**Piotr Buczkowski:** Jest cały artykuł, kiedyś napisałem o tym.

**Damian Kamiński:** Ale to ja zakładam, że oni wrzucili ten CLM, bo to może w cudzysłowie "żre", tak?

**Łukasz Bott:** No że hasło tak, no bo jest wiesz. Wszędzie tam no to jest jakiś Contract Lifecycle Management, tak? Czyli...

**Damian Kamiński:** Dokładnie, jako konkurencja dla Autenti i tak dalej, bo oni mają tego typu narzędzia, gdzie też pewnie to wszystko można zrobić, tak? Czyli w narzędziu przygotować draft, zasilić jakąś seryjną korespondencją danymi i puścić do ludzi.

**Kamil Dubaniowski:** Dobra, to ja ostatnio...

**Damian Kamiński:** Pewnie trzeba będzie to lepiej zaopiekować. No w tych szablonach i ich możliwości edycji po stronie systemu już mówimy od jakiegoś czasu. Trzeba będzie w końcu to może zaopiekować jakąś, lub równa pół, tak?

**Kamil Dubaniowski:** Zgadza się. I co jeszcze chciałem, ostatni element taki niuans też, ale tak jak mamy administratorów słowników czy grup, to uznali, że u nich słusznym będzie dodanie tej opcji też po stronie Bazy Wiedzy (Copilota). Czyli dział kadrowy sobie zrobi jakąś bazę wiedzy na temat...

**Kamil Dubaniowski:** Prawny. Wydaje mi się, że bazę wiedzy aktualnie widzi tylko Admin. W sensie, że te zakładkę, tam możesz udostępnić wiedzę, kto ma móc z niej korzystać, ale nie kto może nią zarządzać. Zarządzać aktualnie mogą tylko admini. A to chodzi o to, żeby HR sam sobie wrzucał tak artykuły tam, wpisy dotyczące nie wiem Kodeksu Pracy, z których później AI miałby odpowiadać ludziom.

**Łukasz Bott:** A w tym sensie, dobra, okej.

**Damian Kamiński:** Tak, tak, tak. No to jest też opcja. No wiecie to jest...

**Kamil Dubaniowski:** Więc wydaje mi się tu też słuszne na rozwój tego komponentu.

**Damian Kamiński:** Dokładnie, zobaczyli jakieś prototypy, no i mają refleksje. No tak samo jak przecież teraz te repozytorium, tam też wprowadzać jakiś zakres uprawnień. Więc tak samo tu nawet się zacząłem zastanawiać, czy to nie powinno być powiązane. Bo pytanie, czy... Bo ta baza wiedzy przeważnie będzie zajmować dużo wiedzy i czy nie lepiej tym zarządzać plikami, a nie tekstem.

**Kamil Dubaniowski:** Czy nie wiem, co jest szybsze w czytaniu? Wydaje mi się, że to jest kwestia, że pewnie to jest w stanie szybciej przeczytać, tam formatowanie dla niego nie jest ważne.

**Damian Kamiński:** No ale przecież my możemy mieć potem po wczytaniu do repozytorium... Jak sobie to zrobimy, to znaczy ja to nie mówię, że takie ma być rozwiązanie, tylko rzucam jakieś pomysły na razie. Że wiesz, no po wczytaniu pliku, jeśli one są oznaczony jakkolwiek, jakiś węzeł repozytorium, że to jest jakaś baza wiedzy. No to on sobie go odczyta. Skąd ten tu? W naszym FullText Searchu, tak? I gdzieś tam może zapisać sobie, więc on nie musi się odwoływać za każdym razem do pliku, tylko z niego może utworzyć sobie jakiś już zbiór informacji niezależnie. No ale i przechowywać to tak jak teraz, tylko inaczej byśmy [rozwiązali] to wczytywanie. Bo dzisiaj, jeśli mamy bazę wiedzy, to co? Muszą tytułować sobie powiedzmy dany artykuł z jakąś datą, tak? Tu mieliby to w plikach i regulaminy mogliby wrzucać z pliku. Do zastanowienia się według mnie.

**Kamil Dubaniowski:** Wiesz, jakby sprowadza się to teraz do Ctrl+A, Ctrl+C z Worda, jeśli mają. Jest też nie jest jakieś dla nich, czy wrzucisz plik czy skopiujesz, no to to pewnie przeżyją. Ale wygodniej byłoby plik. Wręcz też ta nazwa dla mnie była w tym momencie taka niezrozumiała, no bo tam było "Dodaj dokument", po czym wyskakiwał mi właśnie input do wklejania tekstu. Więc tam zmieniłem, że w projekcie teraz jest "Dodaj treść". Wyskakuje to okienko do wklejenia treści. Ale zgadzam się, no zgadzam się, że wygodniej byłoby mi wrzucać pliki pewnie. Alternatywnie te treści, jeśli miałbym gdzieś chciał je pisać, może na szybko sam.

**Damian Kamiński:** No dokładnie, bo to zależy właśnie co jest celem udostępnienia. Tak my piszemy artykuły, bo chcemy mieć, bo mamy to w tekście, bo mamy to na Wiki, nie mamy plików. A z kolei taki typowy dział HR, no to ma regulaminy wewnętrzne w plikach, więc po prostu najwygodniej byłoby im je przerzucić i tyle. No ale to do zaprojektowania, do przedyskutowania.

**Kamil Dubaniowski:** No rozwój tam akurat do tej bazy wiedzy mam kilka jeszcze pomysłów, chociażby to, że jak dodajesz nową treść, to żeby określić sobie, że ona obowiązuje na przykład do końca roku. Albo Kodeks Pracy – co roku aktualizację. W tym wypadku to było nawet jeśli wydaje mi się, że na tym naszym spotkaniu z klientami w zeszłym roku, gdzie zapowiadaliśmy te nowości, to było jedno z pytań: czy będzie się to dało wersjonować, żeby on zachowywał starą wersję dowodowo? Tak, że dlaczego mi odpowiedział 2 lata temu w ten sposób? Bo takie było źródło. Ale żeby też było tak, że w momencie kiedy kończy się rok, to żeby już nie odpowiadał na tamtej bazie i czekał na nową treść, no bo będzie już nieaktualna. Co do finansów to się zdarza tak przecież co chwilę coś się zmienia. Co do kredek to się zmienia non stop, więc wydaje mi się, że tak mogłoby być. Tak, czyli dodatkowy parametr: data ważności tej treści w tym momencie. A jeśli data jest przekroczona, to już z niej nie korzysta i mówi, że nie wie.

**Damian Kamiński:** Datę obowiązywania, czyli od - do. Bo możesz wiesz, w grudniu już mieć regulamin na przyszły rok, a chcesz, żeby on obowiązywał od pierwszego, a do trzydziestego pierwszego się wygasił ten poprzedni? No tak, to to słuszne.

**Kamil Dubaniowski:** No i właśnie tam wersjonowanie, tak, żeby starych też nie tracić, żeby to gdzieś tam pewnie filtrować sobie później, pokazywać tylko bieżące, ale móc też zobaczyć takie wywalone, potencjalnie je usunąć, jak faktycznie już nie są w żadnym wypadku potrzebne. Tak jak mówię najważniejsze dla mnie i to zgłoszę, bo to faktycznie jest słuszne, bez żadnych tam projektów, to jest zamykanie dokumentacji w trakcie edycji z Office'a. Znaczy jeszcze pamiętam, i masowy Job do zamykania spraw z tym, co wszystko tu ustaliliśmy, czyli ustawienie po stronie procesu i ustawienie systemowe do czyszczenia kosza.

**Damian Kamiński:** Dobra, mamy jeszcze tutaj?

**Łukasz Bott:** Tak, jedną rzecz. To jest moje i to jest potrzebne, znaczy potrzebne jak... dobra jest potrzebne, bo po prostu ułatwi życie. Mianowicie mamy sytuację taką. Chodzi o to, żeby zrobić to jako Executor Action, tak.

**Damian Kamiński:** Dla pola typu raport, tak?

**Piotr Buczkowski:** Tak, no bo obecnie mamy Executor i jeszcze 2 pola typu dokument. Dlaczego mamy nie być na raport typu "odśwież", "wydrukuj" i coś tam jeszcze.

**Damian Kamiński:** Mhm. No spoko, tylko spojrzę na Yamała jak on, żeby tam wiesz nie było potem jakoś mało czytelne. Już patrzę.

**Łukasz Bott:** Ale co do zasady jest, robimy tak?

**Piotr Buczkowski:** No to...

**Łukasz Bott:** Dobra. Buduję swój... gdzieś tam dopiszę to, w zasadzie jest gotowe tak pomysł. Czyli co? Nie robimy funkcji reguły dodatkowej tylko jako opcja w `ExecuteOnText`, tak, funkcji?

**Piotr Buczkowski:** No tak.

**Łukasz Bott:** OK, dobra.

**Piotr Buczkowski:** Obsługa pola typu raport w `ExecuteOnText`.

**Łukasz Bott:** Dobra.

**Piotr Buczkowski:** Mówię, że teraz masz `Refresh`, dojdzie `Wydrukuj` i dojdzie `Wygeneruj CSV`, tak? Czy tam wygeneruje Excel, eksport do Excela?

**Damian Kamiński:** No dobra to jest już obiektowa funkcję, więc tak, no to słuszne są 3 przykłady. No jest przestrzeń, żeby to...

**Łukasz Bott:** Dobrze, dobra.

**Damian Kamiński:** ...wykonać. Jest funkcja... Może pokażę, bo musielibyśmy wtedy całość przebudowywać tego opisu. Bo tu mamy zdefiniowaną akcję JavaScript na dokumencie, tak? Czyli musielibyśmy przerobić na polu typu dokument, typu raport, tak.

**Łukasz Bott:** Wiesz, no jeżeli dochodzi [nowy typ], no to ja, jeżeli się rozszerzy funkcjonalność, no to trzeba też zaktualizować opis tej funkcji.

**Damian Kamiński:** No dobra.

**Piotr Buczkowski:** Niezwyczajnego. Tak to zostało zrobione to `CaseID`.

**Damian Kamiński:** Gdzie tu patrzysz, czy patrzysz na to?

**Piotr Buczkowski:** No na opis patrzę, że `CaseID` no to nie... w `ForRow` na przykład nie powinno być.

**Damian Kamiński:** Na opis, ok. "Wiersz w tabeli na formularzu". Że można się odwołać do innego w ogóle, do innej sprawy.

**Piotr Buczkowski:** Wiersz w tabeli, tylko już tak.

**Damian Kamiński:** Znaczy, chodzi ci o to, że jest ryzyko, że powinno być tylko do tabeli? Ograniczenie w ramach tego formularza nie innej sprawy, tak?

**Piotr Buczkowski:** Nie, nie, żeby nie wskazywać, że w kontekście do bieżącej sprawy, tak.

**Damian Kamiński:** No o to mi chodzi.

**Piotr Buczkowski:** Jeżeli chcesz tabeli to `ForRow`.

**Damian Kamiński:** No właśnie, no żeby nie nie przeskakiwać w inny kontekst, no to to już nie wiem. Nie korzystałem nigdy z tego w ten sposób. Nie wiem, czy to było od początku, czy jakie to ma potrzeby?

**Piotr Buczkowski:** No jest pole w tabeli, pole typu dokument w tabeli. Chcesz na polu w tabeli wykonać?

**Damian Kamiński:** Rozumiem o czym mówisz i ja zrozumiałem to, co powiedziałeś, że tu jest ryzyko, że jeśli jest `CaseID`, to można załadować...

**Piotr Buczkowski:** Nie, całkowicie mi się to nie podoba w ten sposób, że to jest zrobione. Bo `ForRow` albo regulator tabeli, tak. W ten sposób przełączenie się w kontekst wiersza tabeli, nie tak.

**Damian Kamiński:** No OK. Ale jest tak, więc no najwyżej trzeba zrobić zgłoszenie.

**Piotr Buczkowski:** Nic mówi, to jest kolejny przykład, że nie myślimy jak coś zrobić, tylko po linii najmniejszego oporu i żeby konkretny problem rozwiązać, klapki na oczach, nie patrzymy w bok. Tak jak z eksportem do Excela. Wkurzyło mnie tak ta zmiana.

**Damian Kamiński:** Rozumiem Piotrze, rozumiem wszystkie twoje argumenty, natomiast nie to było celem i założeniem tego tej poprawki.

**Piotr Buczkowski:** Właśnie cele i założenia nie zostały przemyślane.

**Damian Kamiński:** No OK. Rozumiem, wyciągnę wnioski. Dobra no.

**Łukasz Bott:** Dobra. Jeszcze jeden temat.

**Damian Kamiński:** No.

**Łukasz Bott:** Dobra to to ja to przerobię, bo to jest moje zgłoszenie. To czyli nie robimy nowej funkcji reguł, tylko po prostu rozszerzamy `ExecuteOnText` na obsługę pole typu raport.

**Piotr Buczkowski:** Przygotujmy się na przykład do obsługi pola typu odnośnik czy coś? Nie wiem co to może jeszcze być. Ja dążę, żeby ta funkcja może dla różnych typów pól działać.

**Kamil Dubaniowski:** Jak wszystko to ja jeszcze jedną rzecz, bo w sumie to zaznaczyłem, zapisałem wczoraj.

**Damian Kamiński:** Jeszcze jedno było.

**Łukasz Bott:** Jeszcze jedno zgłoszenie wyświetlam, to znaczy tak, to Eryk zgłosił jako błąd.

**Piotr Buczkowski:** Tak sam powiedziałem, że to jest błąd. Tak, to jest błąd.

**Łukasz Bott:** Dobra, czyli to do poprawienia. Piotrek, a...

**Piotr Buczkowski:** Jeżeli ustawię jeden, to powiedzmy dziś, jeżeli dzisiaj o 1:00 wpiszę jeden, to ustawił mi, że do końca jutrzejszego dnia... do końca dzisiejszego dnia powinno zostawić.

**Łukasz Bott:** Czyli wiesz jak to poprawić? Tak?

**Piotr Buczkowski:** No tak, no. Trzeba inaczej wyliczyć datę ważności tego tokenu tak, że od dzisiaj od północy, a nie od kolejnego dnia.

**Piotr Buczkowski:** Znaczy tak naprawdę zapisuje, że...

**Damian Kamiński:** Dzisiejszą godzinę tak, aktualną.

**Piotr Buczkowski:** Wracamy do dwudziestego... do północy 26.09.25, tam 00:00, tak? Tylko, że tak płynnie jak sprawdza to jaki jest taki czas, to przez cały okres dwudziestego szóstego jest ważne, ale już nie powinno być po tej godzinie... że jest to tak naprawdę, że jest ważne.

**Damian Kamiński:** Nie uwzględnia godziny, tak.

**Piotr Buczkowski:** No tak, czyli albo powinien zapisywać, że jak dzisiaj ustawię to jest ważne do 25.09 00:00 czyli jakby to w przeszłości... no ale później sprawdza, że jest nadal 25 wrzesień. To nadal jest ważne. No albo przy sprawdzaniu sprawdzać czy co do godziny tak czy czas nie minął. No to już w którą stronę to wszystko jedno.

**Łukasz Bott:** Dobra, no to my nie wiemy jak to poprawić? Natomiast ja to dałem na radę, bo tutaj tak jakby nie wiem czy to Eryk chce upchnąć 2 rzeczy w jednym zgłoszeniu.

**Piotr Buczkowski:** Tak to też była moja uwaga. Tak, klient chce, żeby za każdym razem się logować.

**Łukasz Bott:** No dobra, no to co Piotr, przypisać tobie w takim razie, skoro wiesz, co tu trzeba zrobić?

**Piotr Buczkowski:** No można.

**Łukasz Bott:** Nie wiem czy na ten sprint czy na kolejny. Dobra, to co? To moje, ja to już sobie ogarnę. Coś jeszcze miałeś?

**Kamil Dubaniowski:** Tak, więc to tak, bo to mi się wieczorem przypomniało tylko na czacie sobie zapisałem, a nie w tym pliku co omawialiśmy. Padł pomysł i to w temacie logów, które aktualnie i tak przerabiamy na Reacta. Żeby po stronie tej serii zakładki "Kolejka maili" dodać tak jak zaplanowałem w logach systemowych checkboxy do zaznaczania z opcją usunięcia maili z kolejki. Teraz i tak to robią, robią to z poziomu bazy danych. Najczęściej to będzie używane na czas testów, czyli ludzie...

**Anna Skupińska:** Chodzi o to też, pewna reakcja była jakby lista z kolejką maili może można było.

**Kamil Dubaniowski:** Ona jest tak, w sensie jest w starym interfejsie. Przekładamy ją teraz na REACT, ale nowa funkcjonalność, jaką zasugerowali, to właśnie, żeby z tego poziomu dało się usuwać rzeczy z kolejki, bo mają taką sytuację, że testują nowy proces. Nie chcą ludziom tłumaczyć, żeby tam teraz czy właśnie zmieniać wręcz w bazie, żeby te maile nie wychodziły. No bo większość chce te maile na testach, no ale jest jakiś tam zarząd i dochodzi do nich jakieś tam, powiedzmy powiadomienie. Oni wtedy muszą szybko usuwać z kolejki z poziomu bazy danych, żeby to powiadomienie nie wyszło.

**Łukasz Bott:** Oczywiście przy założeniu, że zdążą w okienko.

**Damian Kamiński:** Nie no ale to wiecie, biznesowo mogą zatrzymać Joba, usunąć i odpalić z powrotem.

**Piotr Buczkowski:** W Webconie jest taka funkcjonalność, że wysyła już wszystkie maile do... Można takie coś. To chodzi o to, że jak właśnie ten co robi proces, to wszystkie maile idą do niego.

**Łukasz Bott:** Ale to jest gdzie się konfiguruje?

**Damian Kamiński:** Ale mówisz teraz w Webconie, tak?

**Piotr Buczkowski:** Tak.

**Damian Kamiński:** No tak, to oni mi o tym mówili, ale tego nie robiliśmy. No wiecie pytanie, czy jest to potrzebne, bo jak ktoś zobaczy, że wychodzi taki mail to to też jest jakaś opcja. To o której mówi Kamil, pytanie, co jest bardziej użyteczne?

**Kamil Dubaniowski:** No tak, ale wtedy wtedy dostaniesz ty tego maila, czyli i tak wiesz, że zadziałało.

**Piotr Buczkowski:** To tam właśnie też chodziło o to, żeby sprawdzać tak czy mail jest za prawidłowe.

**Damian Kamiński:** Tylko Piotrze, ty mówisz "Wysyłaj wszystkie maile do". To znaczy jakie maile? Wszystkie wszystkie?

**Kamil Dubaniowski:** Z tego procesu.

**Piotr Buczkowski:** Znaczy w Webconie jest tak, że to jest ustawienie systemowe i to jest dla środowiska. Czytam środowiska testowego, produkcyjnego... tutaj mi się czytało proces, tak.

**Łukasz Bott:** No tak, mówiłem, możesz po prostu się chcieć to mieć w innym, niekoniecznie.

**Piotr Buczkowski:** No, pracujesz nad jednym procesem, nie chcesz wysyłać, nie chcesz ludziom wysyłać maili, ale chcesz sprawdzać czy prawidłowo maile wychodzą, tak.

**Łukasz Bott:** No tak, czy mail wychodzi, jest we właściwym formacie treści, no jasne.

**Piotr Buczkowski:** Wszystkie maile wysyłane ze spraw z tego procesu idą na wskazany adres mailowy, nie do osoby, do której miało być wysłane. Czyli wpisujesz sobie albo swój adres mailowy, albo adres jakiejś grupy do grupy dystrybucyjnej.

**Damian Kamiński:** Po prostu robią wtedy dedykowane.

**Piotr Buczkowski:** Gdzie jest na przykład kilka osób.

**Łukasz Bott:** Użytkownika systemowego.

**Kamil Dubaniowski:** Chodzi mi o to, czy byłbym w stanie się połapać, że to jest mail z tej akcji? Tak? Czy nie wiem, czy mi na przykład 5 maili, bo coś wpadło na grupę tych samych maili, tak, o to mi chodzi, czy to jest intuicyjne?

**Piotr Buczkowski:** No to już musisz się zastanowić, ty pracujesz nad tym procesem. Wiesz, czego się spodziewasz. Chodzi o to, że na przykład testujesz proces. Wiesz, że wyszedłeś do osoby, której ją przekazałeś. Nie musisz do niej dzwonić: "Hej, dostałaś maila? Przekażesz mi go z powrotem sprawdzić?" tylko ten idzie do ciebie.

**Piotr Buczkowski:** Widzisz, że przyszedł na przykład mail do Łukasza Bota – "Wyszło do Łukasza Bota", tak, bo tak jest w tytule, ale przyszedł do ciebie i widzisz, że jest prawidłowy, tak?

**Kamil Dubaniowski:** OK, no nie no ma to sens.

**Piotr Buczkowski:** Bo ty pracujesz nad procesem.

**Kamil Dubaniowski:** Tak znaczy, ja bym nie wycinał też tego ich pomysłu, bo a czemu by nie? Tak czasami się zdarzy, że były takie sytuacje, że ta kolejka się już tak naprawdę stwierdziła, że oni uznali, że tych maili to w ogóle nie ma sensu wysyłać albo był Job zatrzymany i się narobiło tam pełno maili, tak? I oni teraz muszą usuwać z poziomu bazy. Czemu by nie usunąć z tego interfejsu i tak już pokazujemy tą kolejkę. No to można by ją pewnie też z tego poziomu wyczyścić.

**Łukasz Bott:** Funkcję dodać tak, no to w interfejsie możliwość czyszczenia.

**Kamil Dubaniowski:** Ale tak... Tak, to na pewno, no bo nawet 2 różne osoby mogą projektować 2 procesy, więc to jak najbardziej ma sens. Także ja robię sobie tutaj do siebie i ja testuję, a Damian robi proces w tym samym, u tego samego klienta i będzie on testował ten mail. OK. No to 2 rzeczy już szóstej. Więc ja to...

**Damian Kamiński:** No tak, tylko wtedy trzeba jeszcze... no ale to już jako piszesz. Żeby tam działało zaznaczanie stawem [Shiftem?] i zaznaczanie wszystkiego tak. A nie tylko pojedynczych, no bo jak mam zaznaczyć 100 no to nie będę 100 razy klikał. Przynajmniej Shiftem, żebym mógł w pierwszy i ostatni wszystko pomiędzy tak się zaznaczy.

**Kamil Dubaniowski:** Tak. To Shiftem chyba domyślnie...

**Damian Kamiński:** Czy Shiftem... Przepraszam Shiftem masz rację tak, tak tak sorry.

**Kamil Dubaniowski:** No dobra, no to mamy. Ja więcej tam nie mam przynajmniej tych spisanych. Te 2 najważniejsze, które omówiliśmy, dodam na pewno plus to do projektu. Może nie na teraz, tylko jako dodatkowy już kolejny krok. A resztę trzeba zaprojektować i może jeszcze raz gadać. Z tych moich.

**Łukasz Bott:** No dobrze, no to kończymy w takim razie. Dzięki.

**Kamil Dubaniowski:** Dzięki.

**Damian Kamiński:** Dzięki.

**Anna Skupińska:** Cześć.

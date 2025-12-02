**Data spotkania:** 13 listopada 2025, 11:32

---

**Piotr Buczkowski:** Okej.

**Kamil Dubaniowski:** Ich sytuacja typu wyjątek, typu dziedziczenie, to robi Filip. Przemek kontynuuje tematy związane z edytorem graficznym formularza, ale to też raczej na zasadzie zgłoszeń bugów, braków, niż nowości. Nic się nie zmieniło. Lista pól to też Filip, ale tam bardziej wyrównujemy braki funkcjonalne względem starego wyglądu. Jak miałbym pokazać, to ewentualnie ten projekt możemy omówić w matrycy? Bo tam feedback dał tylko Daniel, który odebrał ten.

**Przemysław Sołdacki:** Będzie łatwiej, jak coś zobaczymy, bo z opisu to niewiele jestem w stanie wywnioskować.

**Kamil Dubaniowski:** Poprawkę, że to firma, więc tu nie jest jeden do jednego, tak jak to będzie u nas. Czekajcie, odświeżę, bo chyba publikowałem zmiany wczoraj. To, co wejdzie w tym sprincie, to są niuanse typu: usuwamy te łańcuchy służące do oznaczania, że coś dziedziczy.

**Przemysław Sołdacki:** Rozumiem, to będzie wyglądać bardziej tak, jak do tej pory, bez tych ramek.

**Kamil Dubaniowski:** Tak, zmiana oznaczeń będzie głównie tutaj filler.

**Przemysław Sołdacki:** Okej.

**Kamil Dubaniowski:** Robimy wcięcie, żeby odróżnić ustawienia sekcji jeszcze bardziej od ustawień pól. W tej sekcji to, co jest dziedziczone z ustawień sekcji, jest szare i kursywą. Wyjątek łamiący reguły dziedziczenia z sekcji jest oznaczony pomarańczową ramką. Ramek aktualnie w ogóle nie mamy. Filip zrobił to celowo, żeby to nie były selekty, bo bardzo długo trwało ładowanie tych wszystkich selektorów. Zrobimy tylko taki wizualny wygląd selektorów, ale docelowo select będzie robiony dopiero w momencie, kiedy ktoś kliknie.

**Przemysław Sołdacki:** Zdecydowanie tak to powinno działać, ale tylko mówisz, że ramki. Nawet we wszystkich tych miejscach, gdzie teraz są rameczki, żeby to wyglądało jak selekty, to ma zostać?

**Kamil Dubaniowski:** Tak.

**Przemysław Sołdacki:** Moim zdaniem jest nadmiar kresek na tym ekranie. Po kliknięciu rozwija mi się dropdown, gdzie mogę coś przeoczyć. Ten select to wcale nie znaczy, że musi być ramka. Wystarczy, jak w to kliknę, mi się wtedy rozwinie. Po prostu zrobiło się to ciężkie, strasznie dużo kresek, obwódek, ramek oddzielających. Moje subiektywne wrażenie, że to nadmiar tuszu, kosztem treści.

**Janusz Bossak:** W tabelce mamy podobnie, tylko że są mniejsze te odległości.

**Przemysław Sołdacki:** Wiem, ale to bardziej ma być coś takiego, że widać to graficznie. Ten kolor ma znaczenie. Na przykład, tu mam cały obszar jest zielony, a ten zielony tu się gubi wśród tych szarych różnych kresek. Rozumiem ideę tej edycji, ale w tym zastosowaniu chcę zobaczyć, gdzie mam edycję, gdzie mam ukryte. Ta informacja gubi się wśród nadmiaru tych elementów graficznych. Tak mi się wydaje. Nie jestem od tego, żeby jakieś decyzje finalne podejmować, to jest moja pierwsza sugestia, dlaczego nagle pojawiło się tyle ramek.

**Janusz Bossak:** Ale było tak.

**Kamil Dubaniowski:** Nie było.

**Przemysław Sołdacki:** Bez ramek to wyglądało moim zdaniem dużo lepiej.

**Kamil Dubaniowski:** Zastosowałem te ramki, żeby pokazać zaznaczenia tych wyjątków. To też sugestia edycji.

**Przemysław Sołdacki:** Jak jest wyjątek i wtedy pojawia się ramka, to jest okej. Ale jak nie ma żadnego wyjątku, to po co mi te ramki? Mógłbym nie mieć ramek. Mógłbym nie mieć też tych ptaszków do rozwijania. Jak kliknę, to mi się rozwinie menu. Będę wiedział, że kliknąłem, i się rozwija. Dużo naraz powtarzających się elementów, które nic nie wnoszą. Ramka nic nie wnosi. Ten ptaszek do rozwijania też nic nie wnosi, tylko zajmuje miejsce na ekranie. Na przykład, gdybyśmy mieli nie trzy, ale dziesięć etapów, to to się już w ogóle nie zmieści na ekranie. Gdybyśmy to mieli bardziej wyśnione, to byłoby lepiej.

**Kamil Dubaniowski:** Czy my mamy jakąś ustaloną maksymalną szerokość tego wszystkiego? Także to rozjechała się Sigma. Nie wiem, jeśli coś jest listą wyboru, to usuniemy teraz wszystkie ramki wokół pól tekstowych na formularzu. Nazwa mówi, że to jest.

**Przemysław Sołdacki:** Ale to jest to samo, bo w polu na formularzu ty masz wprowadzić dane. Tutaj nie. Tu masz zobaczyć, co jest ustawione, i dopiero jak klikniesz, to się zmienia.

**Kamil Dubaniowski:** Nie, tu masz pracować w kontekście konfiguracji procesów i ustawień matrycy uprawnień. Podgląd do wydruku, do przeczytania, do dokumentacji. To możemy zrobić niezależnie. To jest troszeczkę decyzyjnym. Ustawiasz uprawnienia, więc ja wchodząc w taki formularz, jak mamy teraz, uznałbym, że to wszystko jest do odczytu, bo to nie są selekty. Listy, tego się nie da wybrać. Dopiero po kliknięciu bym zauważył, że coś się rozwija.

**Przemysław Sołdacki:** A to możemy zrobić, że ta ramka się pojawia na przykład na hover. Jak najeżdżam, to mi się pojawia. Wiem, że mogę edytować. Ale ogoliłbym to z tych wszystkich narzutów, bo mamy tło, tylko że to jest sekcja, to jest okej. Ale te ramki, jeśli by ich się pozbyć, to uważam, że byłoby dużo bardziej czytelne.

**Damian Kaminski:** Byłbym przeciwny hoverowi, bo wtedy jeżdżąc myszką, to będzie skakać.

**Kamil Dubaniowski:** No tak.

**Przemysław Sołdacki:** Można zrobić, żeby nie skakało.

**Kamil Dubaniowski:** Teraz tak, jak mówi Przemek.

**Przemysław Sołdacki:** Jest czyściej moim zdaniem. Jak najeżdżasz, to ci się coś tam rameczka pojawia, i to uważam, jest lepiej. Nawet w skrajnym wypadku, w takim widoku bardziej kompaktowym, nie chciałbym mieć napisu "edycja". Wiem, że to jest edycja. Po jednym dniu używania wiedziałbym to. Uważam, że to jest fajne, i jeszcze nie będzie tych łańcuszków.

**Kamil Dubaniowski:** Tak i tych gwiazdek też już. Tylko w takim wypadku, co to powinno być w ramce od początku? Tak to powinno wyglądać. Tylko pomarańczowa ramka, a wszystkie inne bez ramki.

**Przemysław Sołdacki:** Jak najeżdżasz i wtedy ci się pojawia, że to można zmieniać. I to jest okej. Ale nie tak, że wszędzie narysowane ramki. Po prostu za dużo.

**Kamil Dubaniowski:** Dobra.

**Przemysław Sołdacki:** Daję feedback. Zastanówcie się nad tym. Okej. Lista. Robimy tę listę pól, czy na razie zostaje?

**Kamil Dubaniowski:** Tak, jest. Dochodzą już kolejne elementy. Na przykład, dodaliśmy już opcję ustawienia ilości kolumn w sekcji. Doszły ustawienia pól. Była dyskusja, czy to ma być na hover, czy zawsze. Na razie zostawiłem. Zawsze męczyłem. Nie miałem czasu tego gdzieś tam z kimś przegadać. Pojawiło się ustawianie domyślnych wartości. Predefiniowane.

**Przemysław Sołdacki:** Okej.

**Kamil Dubaniowski:** To jest Kompani. Są pola zablokowane do edycji. Jest okej. Doszły te opcje: "Zwiń wszystko", "Rozwiń wszystko", bo zauważyłem, że z tego korzystają. Ale okej, to jeszcze nie wygląda najlepiej.

**Przemysław Sołdacki:** Czyli to jest robienie rzeczy, które do tej pory się dało robić?

**Kamil Dubaniowski:** Były dokładnie na starej liście. Tylko robimy to po nowemu. Tam, na przykład, te ustawienia kolumn były gdzieś tam w oderwanym miejscu, niezwiązanym z nagłówkami. Porządkujemy to trochę. Dodajemy to, co było, jak historia pola. Widzę, że najeżdża też. Miało tak nie być narażonym do zgłaszania. Jeszcze nie śledziłem tych zmian. Basia testuje.

**Przemysław Sołdacki:** Spoko.

**Kamil Dubaniowski:** Na razie wyrównują.

**Przemysław Sołdacki:** Graficznie mam tylko jedną uwagę. Tu jest "Typ", i przy sekcji, rozumiem, zamiast słowa "Typ" jest wskazana ilość kolumn.

**Kamil Dubaniowski:** Tak, może być sekcja. Tutaj dopisać. Wtedy "Drop".

**Przemysław Sołdacki:** Ale jeszcze jedna rzecz. W edytorze graficznym ilość kolumn jest 104 ikonki, którymi się to wybiera. Tu jest zupełnie inaczej. Czy tak chcemy?

**Kamil Dubaniowski:** No nie wiem.

**Przemysław Sołdacki:** Nie mówię, które rozwiązanie jest lepsze. Kwestia spójności. Czy chcemy zachować? Bo można, na przykład, zostawić napis "Sekcja", i w tym dropdownie te cztery ikonki pokazać. Na przykład, głośno myślę. Chodzi mi po prostu bardziej o to, żeby było spójnie. Że i tu, i tu jest podobny sposób. Dobra, rozumiem, że to jest w trakcie implementacji?

**Kamil Dubaniowski:** Tak. Na ten sprint celem jest, de facto, jeszcze nie rozpisałem jednego zadania, i raczej już nie rozpiszę, bo nie mam na to dobrego pomysłu. Jak opisać tutaj sekcję, żeby to było czytelne, bo w edytorze graficznym w sumie też jest to do poprawki. Raczej to już zostawię na kolejny sprint. Bo z tego poziomu, jak mam długi formularz, to nie jest dla mnie intuicyjne, żeby dodać nową sekcję na przykład tu. Muszę jechać na sam dół.

**Przemysław Sołdacki:** Okej.

**Kamil Dubaniowski:** Trzeba to i zarówno w tym edytorze graficznym przemyśleć, jak i na liście, żeby to dodawanie sekcji jakoś dobrze zaprezentować. Tego na ten sprint nie rozpisywałem. Ale ogólnie, poza tymi sekcjami, będziemy mieli już wyrównane. Powinniśmy mieć wyrównane wszystko tak, jak było w starej liście. Czyli z tamtej możemy już rezygnować od wersji grudniowej.

**Przemysław Sołdacki:** Mam pytanie. Pamiętam, jak ten stary edytor wygląda. Czy z tego poziomu "Dodaj pole" mogę? To tutaj jest "Dodaj pole"?

**Kamil Dubaniowski:** Tak, do sekcji bezpośrednio, konkretnej sekcji.

**Przemysław Sołdacki:** W sekcji dodaje. Okej. Rozumiem, bo tam był przycisk "Dodaj pole" i "Dodaj sekcję".

**Kamil Dubaniowski:** Nie, tam był przycisk tylko do dodawania pól. Jak chciałeś dodać nową sekcję, to w momencie dodawania pola musiałeś wpisać nową nazwę sekcji. Będzie lepiej. Jeszcze nie wiem jak, ale wiem, że to jest do poprawki, bo to było bardzo nieintuicyjne na pierwszy kontakt. W sumie tyle. Wszystkie inne ustawienia, typu, że na przykład na liście mogliśmy szybko zmienić liczbę po przecinku w polu numerycznym. Nie widzę tego miejsca, bo tam było w typie i obok.

**Przemysław Sołdacki:** A wpisywało się nazwę. No rozumiem.

**Piotr Buczkowski:** Zróbcie w nowym okienku.

**Przemysław Sołdacki:** Czekaj, trybik jest. Co w tym trybiku jest?

**Kamil Dubaniowski:** Tak. Wszystkie te same.

**Piotr Buczkowski:** Zróbcie w oddzielnym wątku.

**Przemysław Sołdacki:** Okej, to to.

**Kamil Dubaniowski:** Wszystkie te dedykowane ustawienia już pod konkretny typ pola są w prawym panelu. Otwiera się go tym kołem zębatym.

**Przemysław Sołdacki:** Bardzo dobrze.

**Piotr Buczkowski:** Kiedyś wszystko było w tym, ale przechodziliśmy po kolei na to okienko. To tylko zostało.

**Kamil Dubaniowski:** Tak, zostało to ustawienie, i jeszcze na rzecz której tu nie odtworzyłem, i sumie na razie też nie rozpisywałem, bo nie chciałem na szybko bez większego zastanowienia i dyskusji, że z tego poziomu z listy dało się łatwo przejść do ustawień tego słownika. Teraz też możemy, ale dopiero z tego poziomu. Pewnie jeszcze to będę chciał odtworzyć jakoś z poziomu listy. Szybko przechodzić.

**Piotr Buczkowski:** Może być przy słowniku tutaj link.

**Kamil Dubaniowski:** Tutaj pewnie będzie tak, jak jakaś tradycja. Będzie przycisk, link czy coś.

**Piotr Buczkowski:** Tak, tak. Obok.

**Przemysław Sołdacki:** A nie może być słowo "Słownik" od razu linkiem do słownika?

**Piotr Buczkowski:** I pole dla pola "Odnośnik" też, to przejście do definicji procesu.

**Kamil Dubaniowski:** Tak, to samo i do źródła zewnętrznego też zrobiliśmy. Też dodamy.

**Przemysław Sołdacki:** No.

**Kamil Dubaniowski:** No.

**Przemysław Sołdacki:** Właśnie. Mogłoby być tak, że oni gdzieś tutaj pojawia się jakaś ikonka. Nie wiem, kluczyka, czy czegoś. Jak najeżdżam, to mi podaje nazwę tego słownika. "Przejdź do słownika X", albo "przejdź do".

**Kamil Dubaniowski:** Tak zrobimy, bo to też jest cenna informacja, jaki tu jest słownik podpięty.

**Przemysław Sołdacki:** Nie widać, jaki słownik.

**Kamil Dubaniowski:** Tak, tych dwóch rzeczy nie rozpisałem z mojej listy, co było do zrobienia. Widzę, że jeszcze jest nadal problem z tym tekstem statycznym, ale to też było zgłoszone, że nie ma takiego realnego podglądu. Jeśli jest jakieś formatowanie tekstu, coś się sypie. Jeszcze widzę, że to Filip ma tak. Te wszystkie wartości, gdzie mamy typ na przykład datetime, to wszystko przenieśliśmy. Tak jak działało do tej pory. Takie domyślne ustawienia.

**Przemysław Sołdacki:** To jest ważne.

**Piotr Buczkowski:** Nie lepiej, żeby ustawienia, jak było.

**Kamil Dubaniowski:** Jest, natomiast możesz sobie tę wartość domyślną, na przykład, wywalić, jeśli nie chcesz jej w ogóle mieć na liście. Ta lista też. Zaraz spodziewam się zgłoszeń, że kiedyś to można było tutaj szybko to ustawić, a teraz muszę wchodzić do ustawień. Albo nawet nie mogę podejrzeć, jakie jest aktualnie ustawienie wartości domyślnej i muszę wchodzić do każdego pola z osobna. Ta lista do tego ma między innymi służyć: przejrzeć, jakie masz aktualnie ustawienia domyślne. Szybko to zrobić, zobaczyć, że "okej, nie mam żadnych działań".

**Piotr Buczkowski:** Szkoczość. Wyświetlić, ale jako.

**Kamil Dubaniowski:** Wstawiać.

**Przemysław Sołdacki:** Niech decydują o tym ludzie z Sali Wdrożeń. Jeśli stwierdzą, że im potrzebne, to nie będzie. Nikt nie narzekał, że jest gorzej niż było.

**Kamil Dubaniowski:** A teraz się to zdarza, więc wolę na razie nic się nie zabierać.

**Przemysław Sołdacki:** Nie da. Super. Uważam, że w ogóle fajnie, że to powstaje i że będziemy mogli te stare rzeczy wyłączać. Ale rozumiem, że z edytorem diagramu na razie nic nie robimy.

**Kamil Dubaniowski:** Tego tematu nie opiekuję, więc nic nie zlecałem.

**Janusz Bossak:** Nie wiem na razie.

**Damian Kaminski:** Nie, ja też nie. Pakuję to, co było i co Przemek poprawiał w kontekście niedziałających elementów. Na czym stanęliśmy? Nie wiem, czy ty, Przemku, coś jeszcze poprawiałeś w ostatnim czasie? Chyba nie.

**Przemysław Rogaś:** Nie. Zgłosiliście tam uwagi tylko raz. Ja to.

**Kamil Dubaniowski:** Świadoma.

**Przemysław Rogaś:** Zmieniłem, i to już przeszło testy. I już jest. Nic więcej nie ma.

**Kamil Dubaniowski:** Tak jak planowali.

**Przemysław Sołdacki:** Okej. Ale to znaczy, że my wydajemy ten nowy edytor diagramów.

**Damian Kaminski:** Nawet jeśli decyzja oficjalnie nie zapadła, to traktujemy to jako totalnie wersję beta.

**Kamil Dubaniowski:** Na pewno będziemy musieli dać przełącznik do starego. Ale dodać etap się da, połączenia dodać się da.

**Przemysław Sołdacki:** Teraz kliknąć.

**Kamil Dubaniowski:** Paczkę ciągu etapów. Filip już sekunda.

**Przemysław Sołdacki:** Spoko. Wygląda.

**Kamil Dubaniowski:** Moim zdaniem zasada założenia MVP są jak najbardziej spełnione. Diagram narysujesz, i to było celem.

**Przemysław Sołdacki:** A kliknij. Ścieżkę można dodawać z tego poziomu.

**Kamil Dubaniowski:** Ścieżki tak, mogę łączyć.

**Przemysław Sołdacki:** Tak, ale chodzi mi o to, czy tam się reguła pojawia? Bo jak na linię klikniesz.

**Kamil Dubaniowski:** Mogę usunąć połączenie albo dodać regułę. Tylko nie ma edytora tej reguły. Domyślnie robi, że przekazanie z tego etapu na ten. Nic więcej.

**Przemysław Sołdacki:** Tego starego edytora graficznego praktycznie nikt nie używał, więc możemy zostawić taki, jaki jest. Nowe bajery, animuje się ładnie. Zdecydowanie.

**Kamil Dubaniowski:** Tak mi się też wydaje.

**Janusz Bossak:** To jest trochę ładniejsze niż tamten, i ma troszkę więcej możliwości.

**Przemysław Sołdacki:** Tak. Rozumiem, że edycja etapów i reguł to zostawiamy stare. Nic się tu nie.

**Janusz Bossak:** Ale nie jest to rewolucja.

**Kamil Dubaniowski:** Tak, na razie tak. Dojdzie prawy panel, ale świadomie planując kolejny sprint, odłożyliśmy ten temat na dalszy tor, bo mieliśmy zlecenia, które są ważniejsze.

**Przemysław Sołdacki:** Nie mam uwag do tego.

**Damian Kaminski:** Tak. Teraz ten wygląd dotyczy tylko i wyłącznie tego miejsca, bo na sprawie tego Przemek nie dotykał.

**Kamil Dubaniowski:** Nie, tam zostaje stary.

**Przemysław Sołdacki:** Absolutnie okej, tak bym zostawił. Do roadmapy musimy w tym roku dokończyć i dać dobrą, działającą wersję. To, co robimy, żeby to jakoś domknąć. Za miesiąc skończy się rok. Będą już wszyscy na wigilię. Musimy wtedy ewentualnie coś testować, poprawiać. Mamy ważne rzeczy do dokończenia.

**Janusz Bossak:** WIM i LOT. WIM do dokończenia, znaczy do zrobienia.

**Przemysław Sołdacki:** Do LOTu.

**Janusz Bossak:** Do dokończenia. Odbiorą pewnie ten komunikator, bo chyba jeszcze formalnie nie jest odebrany.

**Damian Kaminski:** Nie jest, ale został dzisiaj skutecznie zainstalowany w Zimbrze. Tam drobny problem jest, ale to wtórne. Da się z niego korzystać. Po prostu w jednym momencie wyskakuje błąd. Mateusz ma na to spojrzeć. Jutro to prezentujemy.

**Janusz Bossak:** Okej. Z pozostałych tematów, to jest ten makro z tym Szafirem. Adrian ma jakieś ciągle problemy. Nie do końca działa tak, jak powinno. Repozytorium to największy kawałek do zrobienia. Do LOTu mamy JRWA, bardzo szeroki temat, który trzeba mocno wysprzątać.

**Przemysław Sołdacki:** Zanim LOT, to skończmy WIM.

**Janusz Bossak:** Dokładnie.

**Przemysław Sołdacki:** Odbierzmy. Wszystkie siły bym skierował na to, żeby te wszystkie rzeczy pozamykać. Jak po drodze wyjdą jakieś błędy w edytorze formularzy, czy czymkolwiek innym, to trzeba je po prostu naprawiać, żebyśmy na koniec roku wydali paczkę, która zawiera te wszystkie rzeczy w pełni działające. WIM jest odebrany przed końcem roku – to jest cel. Później będziemy rozkładać na następny rok roadmapy. Słuchajcie, wydaje mi się, że jesteśmy w bardzo dobrym miejscu, bo ten edytor formularzy jest prawie działający. Ten MVP Diagramu jest okej. Dalej będziemy planować. Trzeba prostą, ważną, stabilną wersję, której nikt się nie będzie bał zainstalować. Nic się tam nie wywróci. Jak będzie już kolejna wersja po kolejnym sprincie, to wróćmy na Astrafox, żebyście tam trochę nad nią poznęcali. Dobra, coś tam mamy jeszcze. Rozumiem, lista reguł. Damian tego na razie nie dotykasz.

**Kamil Dubaniowski:** No.

**Damian Kaminski:** Nie dotykam.

**Przemysław Sołdacki:** Dobra. Okej. Domknijmy to, co jest otwarte.

**Janusz Bossak:** Mam.

**Przemysław Sołdacki:** Dobra. Dzięki.

**Janusz Bossak:** Dzięki.

**Damian Kaminski:** Dzięki.

**Przemysław Sołdacki:** Hej.

**Przemysław Sołdacki:** Zatrzymano transkrypcję.

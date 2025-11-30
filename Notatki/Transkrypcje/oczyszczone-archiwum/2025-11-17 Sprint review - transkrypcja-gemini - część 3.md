**Data spotkania:** 17 listopada 2025, 08:04 - część 3

---

**Przemysław Rogaś:** Znaczy to dobra, to ja też sobie tutaj sprawą sobie wydania. Tutaj brakowało wcześniej pola nadrzędnego dla pól, które są w tabeli dla pól typu numeryczne i i kwota.

**Kamil Dubaniowski:** OK dobra.

**Przemysław Rogaś:** Teraz można na ustawiać pole nadrzędne i typ połączenia. Tak teraz można szukać po takie pola. I bo. Tutaj klikamy, żeby akurat szukanie podtypy pola jest domyślnie. Tutaj spiszemy na przykład tekstu, to znaj nie mam też po typie pola. Szukanie po atrybutach też technicznych tutaj. Tylko trzeba zaznaczyć, żeby szukać i teraz mogę na przykład po ID szukać. Lilusię.

**Piotr Buczkowski:** Mój też.

**Przemysław Rogaś:** Szłam.

**Piotr Buczkowski:** GUID też.

**Przemysław Rogaś:** OK, to to nie nie było tego wymagania.

**Piotr Buczkowski:** Bo dostajesz XML z testów, widzisz, że tam jest zbój, tam coś tam 1, 2, 3, 4, to szukasz podwód, żeby go zmienić na boisko?

**Przemysław Rogaś:** Lista wyboru, tutaj można teraz do mając pozycję. Można edytować wcześniej, nie było możliwości edycji. Możliwość wklejania wielu elementów. Czy jeżeli ktoś ma. Tak to po wklejeniu z automatu się wszystkie dodają.

**Daniel Reszka:** Zmiana kolejności.

**Przemysław Rogaś:** Zmiana kolejności odbyła od początku. Po prostu drag and drop.

**Daniel Reszka:** OK.

**Przemysław Rogaś:** Na polu typu dokument wcześniej brakowało tutaj ustawienia do wyboru Storage. Aktualnie tutaj nie pokażę, bo nie mam w bazie wystawione. Ale taka tutaj jest teraz select z możliwością wybrania Storage, o ile jest ustawiona w bazie. To pole Odnośnik. W końcu tutaj możliwość wyszukiwania została dodana. To chyba tyle, reszta to jakieś poprawki.

**Daniel Reszka:** Odnośnik do zewnętrznego też ma możliwość wyszukiwania czy jeszcze nie?

**Przemysław Rogaś:** Tak, tak.

**Lukasz Bott:** Przemek, mam jeszcze uwagę do tej listy wyboru.

**Przemysław Rogaś:** Mhm.

**Lukasz Bott:** Jak tam pokazywałeś, że można skopiować kilka pozycji z notatnika, super, natomiast dobrze nie przewijaj, masz tutaj 2 pozycje na dole, SDASD, więc może dodać jakiś mechanizm walidacji, żeby to były wartości unikalne.

**Kamil Dubaniowski:** W terminie było więc backendzie potrzebny, ale to OK. Rozwój, możemy sobie to odwrócić.

**Przemysław Rogaś:** Tak, można.

**Lukasz Bott:** Nie, dodajmy tak.

**Przemysław Sołdacki:** Dzisiaj ja mam pytanie takie, bo nie wiem czy to jest problem, czy to nie jest problem, czy wam się to wszystko nie zlewa graficznie, bo jakby mamy z lewej strony toolbox taki to później formularz i prawy panel i plazmy. O ile tam gdzieś w środku będą tego typu rzeczy jak ja gram i tak dalej, to one się graficznie różnie, a tutaj wszystko to są jakieś pola i czy one nie powinny się jakoś odróżnić, że ten toolbox nie wiem, może jakimś innym tłem zrobić albo, bo to się trochę zlewa, która część to jest to co my edytujemy, a co to jest ta tam meritum, które edytujemy. Czy to tak jakby się zastanawiam, bo może to nie jest dla was problemem graficzny, ale czy to wizualnie nie powinno się jakoś odróżniać?

**Daniel Reszka:** Znaczy ja uważam tak jak Przemek, że tutaj odcięcie jakieś mogło być większe, czyli po lewej masz komponenty, które dodaje w środku to co edytujesz, a po prawej ustawienia tych komponentów. To są 3 niezależne rzeczy.

**Przemysław Sołdacki:** No właśnie, bo jakby meritum to jest to coś na środku i to jest OK jakby w sensie układu, ale to czy jeszcze jakoś bardziej nie odróżnić, że gdzie jest formularz, a gdzie jest są jakieś narzędzia do tego formularza?

**Przemysław Rogaś:** Ja bym na przykład dałbym tło do środka, nie do boku. Tak delikatnie ciemniejsze, trochę ciemniejsze niż tutaj ten header. Wydaje mi się, że tak bym mogłaby być OK.

**Kamil Dubaniowski:** Będziemy kombinować, tam, mieliśmy do tego podejście w tym sprincie, jakieś propozycje na szybko, ale ten problem też będzie z tym problem. Zaznaczamy na samym początku naszych prezentacji tego tematu. Ja proponowałem, żeby te toolboxy właśnie wręcz zrobić tak trochę, żeby było widać, one są moderowane ramką, tak jak to zrobił Filip na liście. Tam jest to jako taki jakby tu chyba jeszcze nie będzie. Ciebie nie wiem, zobacz na jakieś pole. Nie masz w edycji, ale dobra, jakby znamy temat, wiem, że jest taki, będziemy myśleć czy kolorami to gracie jakoś ramkami, żeby to od siebie oderwać troszeczkę. Dobra to Przemek, ja przynajmniej takich spisanych więcej nie mam tematów, jakie były twoje cele sprintu, więc to chyba wszystko z tych ważnych.

**Przemysław Rogaś:** Dobra, dzięki.

**Kamil Dubaniowski:** Dzięki też. To tam dalej ja będę jak w leciał po swoich te co były u mnie pod opieką komenta. Mariusz i wzmianki tam mieliśmy temat. Od klientów nawarstwiło się sporo zgłoszeń w temacie wzmianek i komentarzy, więc podjęliśmy to jako jakby cały projekt. Właściwie można powiedzieć, że troszeczkę od nowa całkowita reflektory racja tego mechanizmu w AMODIT. I to był cel należy.

**Mariusz Piotrzkowski:** Jeszcze nie zdążę, dostałem dosłownie parę drobnych elementów do dokończenia. Myślę, że dzień maksymalnie 2, ale przy okazji też skończyłem to, co się mówiliśmy o wyświetlaniu reguł na pasku i to mogą pokazać, że teraz dynamicznie będzie ustawiać. Dobra już udostępnia. I ogólnie problem był taki, że dotychczasowo tak szczęśliwie siały tylko 3 reguły na pasku, prostu jakieś takie predefiniowane i przede wszystkim czasami był problem, że one się nachodziło na siebie w sensie, że 2 wiersze się robił, albo że po prostu brzydko wyglądało. Teraz będzie coś takiego, że będą dynamicznie, w zależności od tego, czy jakieś drobne problemy są, w zależności od tego jaki. Jakie są regulowane się schowają do paska? Na co się trzeba się z tym prasowaniem jest nie tak i to są dane parametr dla ustawień, reguły, w którym gdzie to miałem, w którym jest taki taka opcja zawsze wyświetlaj my nie rozwijanym. Dotyczy do tego, że dana reguła będzie widoczna tylko w tym menu dropdown, nie będzie normalnym miejscu w normalnej listwie, nigdy się wyświetlać. Na przykład tutaj jest taka reguła, która, nieważne jak to nie ma, ona nie będzie widoczna, a pozostałe się chowają do środka.

**Kamil Dubaniowski:** Czyli zmieniliśmy tę logikę, to jakby w wyniku zgłoszeń w sporej części klientów, że nie rozumieją, dlaczego mają tylko 3 reguły. Więc teraz ile masz miejsca, tyle ci się wyświetli, chyba że są jakby systemowo wskazane reguły, które są mało istotne, rzadko używane, można je sobie schować na stałe. Natomiast to, ile widzisz reguł, zależy od tego, jak duży masz w tym momencie, ile masz przestrzeni wolnej na nie. Jeśli ktoś chce utrzymać ten układ 3, to powinien po prostu dla pozostałych mniej istotnych, świadomie je ukryć, żeby to nie było takie przez nas narzucone, a żeby to było projektowe działanie.

**Mariusz Piotrzkowski:** I oczywiście kolejność reguł cały czas jest według tego. Tutaj jest podane, jeśli sobie zmienimy, tam ma być w jakiejś kolejności, tak też będzie na toolbarszu, czyli te są zachowane. I to w sumie chyba tyle z tego co dokończyłem. To jak jest z tymi komentarzami jeszcze tego nie dokończyłem, ale tam parę problemów z walidacją tego po stronie serwera i zapisywaniem tych wszystkich zmianek. Ogólnie będzie teraz tak, że zamiast kogo pola do edycji będzie pole typu edytowalne HTML, czyli będzie można tam wstawić z pana w pana, który jest wzmianką. Nie będzie to teraz zwykła małpa, tylko bardziej taki interaktywny element. Ale to był dopiero za 2, 3 dni będę mieć. Tylko nie zdążyłem, bo miałem trochę problemów z tym. Także na tego tyle ode mnie.

**Kamil Dubaniowski:** I to chyba wszystkie, które były u mnie. A mieliśmy jeszcze też obrony podglądy. Ania, ty tutaj zaczęłaś, że musisz coś odpalić tak, bo to jeszcze miałam na samym początku listy.

**Anna Skupinska:** Tak. Tak taka, to musiałam tylko odpalić moją własną witrynę, a poza tym to. Czy widać?

**Kamil Dubaniowski:** Tak.

**Anna Skupinska:** OK. Więc ogólnie rzecz biorąc problem polega na tym, że jak na dzisiaj można robić podgląd załączników, ale nie było podglądu szablonu. To tam podglądu szablonu, tylko że to jest jeszcze nieskończone. Zrobiłam, że można zobaczyć je, ale jest parę rzeczy, które trzeba dopracować, więc czekamy podgląd i to jest podgląd szablonu. Tak, zrobiłam jeszcze to, żeby można było podążać kolejne strony. Jeśli kliknie załaduj kolejne strony jeszcze rzeczy, które można zobaczyć w pełnym ekranie. To jest jakby, ale. Więc można zobaczyć te szablony, tylko że trzeba jeszcze parę rzeczy zrobić, pilnie na to jest taka rzecz, że to obracanie nie działa i też jak się kliknie wyjście to cię wraca do załączników, nie do szablonów, ale po prostu tego to takie bardziej takich rzeczy chciałam o porozmawiać, może na nasze spotkaniu, ale ogólnie takie MVP, takie bardzo MVP jest zrobione, że można zobaczyć podgląd załącznika.

**Kamil Dubaniowski:** Celem było w tym wypadku akurat właśnie umożliwienie podglądów. Mamy też plan rozwoju na to. Natomiast, czy teraz, czy później, to, czy będziemy się zastanawiać, wyszło to od klienta również. Właściwie od sposobu, w jaki oni sobie pewną sytuację obsłużyli nie wydajnie, załączając ten sam załącznik do setek spraw, bo nie mieli gdzie go pokazać. Powiedzmy, że przykład regulamin pracy musisz się zapoznać w ramach obsługi sprawy z regulaminem jako pracownik i oni ten sam regulamin ładowali do każdego załączenie do każdej sprawy jako załącznik, przez co zapychają sobie bazę danych. Zapytali nas dlaczego mają tyle samych załączników w bazie. To był także inny wątek, bo my jak każdą stronę podglądu przechowujemy jako osobny wpis w bazie, o nim myśleli, że to są duplikaty. Natomiast zupełnie nie tak obsłużone. Na to są inne obejścia, więc możliwe, że będziemy robili takie maksymalne MVP tego projektu, bo to po prostu jest źle obsłużona u klienta. Dało się lepiej, tak co obsłużyliśmy my nie wiem, albo oni sami sobie tak zrobili. Żeby uniknąć takich sytuacji, to robimy te podglądy szablonów, między innymi do tego. Nie, żeby było.

**Przemysław Sołdacki:** To ja tylko mam uwagę, że jeśli już to robimy, to róbmy, żeby to działało tak samo jak ta lista plików, bo to widziałem, że nie klikała podgląd, a na liście plików po prostu klikam w plik, się otwiera podgląd.

**Kamil Dubaniowski:** Nie możemy tak. Szablony nie służą do tego. Szybki podgląd w szablonie to jest opcja, którą zrobisz raz, żeby się upewnić, że wybierasz dobry szablon, ale szablony służą do generowania zazwyczaj jakiś dokumentów, więc domyślną opcją tak jak jest teraz. Pozostaje, że jak klikniesz to generujesz ten szablon, plik z tego szablonu na przykład umowę. Bo to jest jakby domyślna akcja.

**Przemysław Sołdacki:** OK, ale wiesz co to, bo to może być mylące.

**Damian Kaminski:** Tak Kamil to ma rację, ale warto się nad tym zastanowić, czy da się to jakoś usprawnić?

**Przemysław Sołdacki:** Bo żeby nie było tak, że ktoś przypadkiem klika myśląc, że chce zobaczyć co to za szablon i mu się tworzy plik, raczej było odwrotnie, zrobił, że klikam, to mi się robi podgląd, a jak chcę utworzyć z tego plik to po prostu wtedy klikam utwórz plik czy tam wygeneruj.

**Damian Kaminski:** Ja myślę, że to.

**Kamil Dubaniowski:** Oba. Chciałem się, że to będzie źle odebrane, bo to jest zmiana dla tych, co aktualnie korzystają, więc teraz, jeśli masz już, jak już masz tam, wiesz kilka lat praktyki, że wybierasz sobie i od razu masz umowę, to będzie teraz się wkurzał, że musi wyświetla podgląd czegoś co on zna na pamięć. Nie tak, że musieliśmy trochę tu uważać. Nie mogliśmy. Tak był taki pomysł. Oczywiście tak chcieliśmy na początku, ale później.

**Janusz Bossak:** Dział obecnie, a kto działa obecnie?

**Przemysław Sołdacki:** OK. Być może tak, być może tak.

**Kamil Dubaniowski:** Się wycofaliśmy. Dobra, nie przedłużałem, działamy nad tymi poglądami jeszcze nie nieskończony. OK, to ja już teraz daję głos Damian.

**Damian Kaminski:** Znaczy, ja będę musiał się równo skończyć i przełączyć się na spotkanie, więc to co ze swojej strony tutaj kolejny element zakończony, to są prace nad komunikatorem.

**Kamil Dubaniowski:** Ona mnie chyba wszystko.

**Damian Kaminski:** Może szybciutko pokażę. Tutaj, żeby nie przedłużać, to powiem tylko o tym co zostało uzupełnione. To wspólnie z Mateuszem komunikator został już wgrany do klienta, któremu był on przygotowywany, czyli WIM. I w zasadzie tym samym na ten moment kończymy pracę, powiedzmy takie w ramach MVP, czekamy na potencjalne uwagi ze strony klienta, jeśli takowe się pojawią. I później na ten moment byśmy powiedzieli, że kończymy tę pracę do momentu dalszego jakiegoś ustalenia rozwoju. To co nowego względem ostatniej wersji, którą pokazywałem się pojawiło, to jest sam element. Czy proces tworzenia nowej konwersacji? Po kliknięciu plusika mamy tutaj zmienioną konwent, inicjowania tej konwersacji. To znaczy nie musimy decydować jaki to jest. W konwersacji wynika to po prostu z naszego. Z naszej potrzeby tego co oznaczymy, czyli możemy wskazać jednego użytkownika i rozpocząć taką konwersację, możemy wskazać więcej niż jednego. Wtedy tworzymy analogicznie jak w tym się taką konwersację grupową, której możemy nadać nazwę i alternatywnie możemy jeszcze utworzyć konwersację z grupami, do których należymy, czyli wtedy już wybieramy nie spośród użytkowników, tylko z grupą. Ta konwersacja oparta na grupie AMODIT-owej jest konwersacja z jedną grupą. Tutaj mamy to ograniczenie, że można zrobić konwersację tylko i wyłącznie z jedną grupą, a nie wielu grup. Oczywiście, jeśli tworzymy konwersację na bazie grupy AMODIT-owej filter, to w tle automatycznie działa synchronizacja użytkowników, którzy wchodzą w skład tego czatu. Tej danej konwersacji, więc w zależności od tego jak zmieniamy regulujemy składem grupy, czy kogoś dodajemy, czy kogoś usuwamy, to dana osoba albo zostaje wypięta danej konwersacji, albo zostaje do niej automatycznie dołączona. I to w zasadzie tyle w kontekście tego, co C uległo zmianie względem poprzedniej prezentacji. Nie wiem, czy tutaj są jakieś co do tego pytania. Zakładam, że przygotujemy do całego komunikatora instrukcje i może jeszcze jakąś krótką prezentację tu i na potrzeby wewnętrzne i na potrzeby marketingu, więc to będzie gdzieś tam dalszymi elementami prac już takimi po produkcyjnymi, ale jeszcze czekamy właśnie tu na uwagę klienta, żeby się nie pośpieszyć. Proszę Daniel.

**Daniel Reszka:** Damian, a jak historia czatu wtedy jak takie Józef jest dodany i inne usunięty.

**Damian Kaminski:** W przypadku tych czatów opartych na użytkownikach. Może przejdę tutaj do jakieś?

**Daniel Reszka:** Nie, nie mówię o grupie, bo mówisz, że w grupie synchronizacja będzie automatycznie dodawało słowa użytkowników, czy nie?

**Damian Kaminski:** Tak, jeśli mówimy o czacie opartym na grupie, to z automatu każdy widzi całą historię tego czatu. Natomiast jeśli mamy tutaj.

**Daniel Reszka:** A ten co wypadnie z grupy?

**Damian Kaminski:** Przestaję widzieć.

**Daniel Reszka:** Ale archiwalnej też nie widzi.

**Damian Kaminski:** Nie.

**Janusz Bossak:** No tak, bo wypadł z grupy.

**Damian Kaminski:** Tak jak nie widzi spraw fakturalnych, po prostu już przestaję widzieć tą konwersację.

**Daniel Reszka:** No tak, tak. Ale sprawy z kolei jeżeli które się robił to je dalej widzi, nie.

**Damian Kaminski:** Tutaj tego nie zachowywaliśmy jak m wypi.

**Daniel Reszka:** OK.

**Damian Kaminski:** Natomiast w przypadku, gdy jest to grupa oparta na pojedynczych użytkownikach, których wskazujemy, to przy dodawaniu użytkownika możemy określić tak, jak w Teams'ie, czy udostępniamy całą historię, czy też od danego momentu.

**Daniel Reszka:** Mniej wtedy potem to jest dodawania. Jak usuniesz takiej grupy, to traci też cały czas.

**Damian Kaminski:** Tak, tak, tak.

**Daniel Reszka:** OK. Jakby to jest spójne, zachowana, dobre.

**Damian Kaminski:** Czy ty Mateusz jeszcze chcesz ewentualnie coś dodać czy coś zapomniałem?

**Mateusz Kisiel:** Komunikatora nie, jedyne co to, że w funkcji do wysyłki OCR doszła teraz opcja ustawienia, ile strony pierwszych i ostatnich ma się limitować, czyli domyślnie już będzie ustawione, że nie wysyłają się wszystkie strony faktury, a tylko zakres pierwszy 10 i 3 ostatnie domyślnie.

**Damian Kaminski:** OK, ale to już inny. Inny wątek.

**Przemysław Sołdacki:** To mam pytanie, czy to będzie konfigurowalne w jakiś sposób?

**Mateusz Kisiel:** Spacerem.

**Przemysław Sołdacki:** Tak, tak.

**Mateusz Kisiel:** Zaraz pokazuje ekran teraz. Widać.

**Janusz Bossak:** Mhm.

**Damian Kaminski:** Tak.

**Mateusz Kisiel:** To będzie opcja PDF first pages i można ustawić ile się pierwszych stron wysyła do OCR-a i PDF last page tyle się wysyła ostatnich stron. I to działa tylko dla PDFów, jak mamy jakieś zdjęcie to dla zdjęcia się to nie limituje.

**Przemysław Sołdacki:** A jak chce się wszystkie?

**Mateusz Kisiel:** To można ustawić na Zero. Jak to ustawione na Zero, wtedy się wysyła wszystko.

**Przemysław Sołdacki:** OK.

**Mateusz Kisiel:** Też pytanie, czy jest sens wysyłać do k. No jeszcze był taki temat, że ktoś miał 200 stron i na początku nie wiedzieliśmy, że można to limitować i myśleliśmy, że trzeba spasować te wszystkie tam nie wiem 6000 pozycji w tabeli. To nie można zrobić tyle spraw, więc trzeba jeszcze opcja, że jak się zrobi mapowanie, mapowanie tabelki do pola tekstowego, to się wpisze w pole tekstowe JSON tych produktów, żeby nie trzeba było robić tylu spraw. Bo 6000 spraw się nie stworzy w AMODIT jakoś sensownie.

**Janusz Bossak:** Czy się stworzy tylko?

**Piotr Buczkowski:** Tworzy się, ale później nie wyświetla.

**Mateusz Kisiel:** No tak, ale przede wszystkim bardzo długo też tworzy to.

**Janusz Bossak:** Może?

**Mateusz Kisiel:** Problematyczne to jest.

**Janusz Bossak:** No dobra.

**Daniel Reszka:** I to będzie tutaj w wersji czerwcowej czy w grudniowej dopiero.

**Mateusz Kisiel:** To to to wrzuciłem do wersji czerwcowej.

**Daniel Reszka:** I u starych klientów, jak nie będzie tego ustawionego w ogóle, to jest 10 i 3. Tak, bo to będzie domyślnie.

**Mateusz Kisiel:** Dzień dobry. Domyślnie się ustawić 10 pierwszych i 3 ostatnie, czyli wprost tego co słyszałem co Damian mówił, to kiedyś zawsze ustawiało się ręcznie w jakiś tam regule, żeby limitować to, ale teraz jak widzę to raczej mało kto takie coś używa, więc dodałem automatycznie, żeby to się działo w tej funkcji do wysyłania.

**Daniel Reszka:** Nie wydaje się zasadne jest OK.

**Janusz Bossak:** Znaczy.

**Mateusz Kisiel:** Dobra.

**Janusz Bossak:** Czyli nie ma, jeżeli będzie dokument maksymalnie 13 stronicowy to się wyślę cały.

**Mateusz Kisiel:** Tak.

**Daniel Reszka:** Mhm, tak, tak, ja to rozumiem, bo to jest pierwsze 10 i ostatnie 3 i to jak się najeżdża na siebie, to po prostu sumuje, część wspólną.

**Mateusz Kisiel:** Dobra, dzięki.


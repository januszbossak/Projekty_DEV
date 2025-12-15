**Data spotkania:** 5 grudnia 2025, 09:11

---

**Łukasz Bott:** Janusz chyba się włączył, przez chwilę wyłączył. Nas nie było, więc... A nie, jest. Dobra, już jesteś.

**Janusz Bossak:** Jestem chwilę. Tutaj testujemy JRWA, tam Marek zrobił. Generalnie coś tam działa, ale jeszcze parę rzeczy trzeba dorabiać, ale na przykład...

**Kamil Dubaniowski:** Zauważyłem też, pisałem. Pytam, co tam zauważyłeś, żebyśmy się nie zdublowali, bo ja też testuję i do Marka już pisałem.

**Janusz Bossak:** No to może nie ma sensu, żeby Kamil testował.

**Kamil Dubaniowski:** Nie, wydaje mi się, że powinniśmy, bo każdy ma swoje spojrzenie.

**Janusz Bossak:** Znaczy, po pierwsze, to nie tu tylko placeholder "Znajdź kategorię archiwalną". Bo to nie jest kategoria archiwalna, to jest BE-10. Czy to jest kategoria archiwalna?

**Kamil Dubaniowski:** Tak, tak.

**Janusz Bossak:** Więc tutaj albo "kategorię JRWA", albo "klasę JRWA".

**Kamil Dubaniowski:** Tak. Wolę. Mi tam brakuje symbolu. Marek powiedział, że musiał go wywalić z listy wyboru, bo coś tam psuła. Prawdopodobnie będzie musiał ją dokleić do nazwy, więc zasugerowałem, żeby w ogóle wydzielił osobną kolumnę w bazie danych w strukturze na taką nazwę wyświetlaną, bo spodziewam się, że jak sklei to do nazwy, no to utrudni konsultantom, bo teraz będą musieli symbol wycinać z nazwy, jeśli będą chcieli samą nazwę.

**Janusz Bossak:** Nie, nie, nie, nie, nie. Według mnie powinniśmy... No właśnie. No trzeba zdecydować, co ma się tutaj wyświetlić po wybraniu.

**Kamil Dubaniowski:** Znaczy sam wybór jest potrzebny, żeby tam był symbol, bo ludzie będą szukać po symbolach.

**Janusz Bossak:** Ale można szukać, tylko że go nie widać. Ale jak wpisuję "000", to jest "Walne zgromadzenie".

**Kamil Dubaniowski:** OK.

**Janusz Bossak:** Właśnie, no to to jest rzecz, którą trzeba ewentualnie przemyśleć.

**Kamil Dubaniowski:** No bo to pole Odnośnik też trochę inaczej się zachowuje niż zwykłe pole Odnośnik. Tam możesz wybrać tylko jedną wartość wyświetlaną, a w tym ze standardowym Odnośnik możesz wybrać pierwszą i drugą wartość wyświetlaną. I wtedy tutaj, jeślibyśmy rozbudowali Odnośnik do źródła zewnętrznego, to bym sobie wskazał te 2 kolumny: symbol i nazwa. No i mamy.

**Janusz Bossak:** No to niech tak zrobi i tak zrobię.

**Kamil Dubaniowski:** Tak, o tym z nim też gadałem, ale to pewnie trochę większy temat, więc no...

**Janusz Bossak:** No tak, no ale wiesz, robimy to, już zróbmy, bo patrzę, wziąłem sobie tutaj ten... Że znowu schodzimy z planowania. No wiesz, to jest jakieś planowanie. No bo to jest planowanie tego, co ma być. Tak, bo tutaj jak zaczynam pisać moją... Tę roszową szkolną... Zobacz, mam wszystko – mam, widzę ulicę, miasto, województwo i tak dalej, powiat i województwo. Nie, więc patrząc coś takiego. Jak tutaj piszę? Właśnie tam nie wiem, nieruchomości. To akurat nie ma. No to może nam się, trzymajmy tego "Walne zgromadzenie", bo... No jest "Walne zgromadzenie", ale... No właśnie, jak teraz? Tu już powinno być to "000" według mnie.

**Kamil Dubaniowski:** Sugerowałem, żeby pokazało też ścieżkę, skąd pochodzi to.

**Janusz Bossak:** Super.

**Damian Kamiński:** Ale jak ty chcesz tą ścieżkę pokazać?

**Janusz Bossak:** Znaczy tak jest, nie.

**Kamil Dubaniowski:** W sensie, żeby te szare się tutaj też wyświetliły. Jeśli znalazło mi "Walne zgromadzenie", które pochodzi z "Zarządzania" i "Gremia", akurat, no to powinno mi pokazać tą pozycję.

**Damian Kamiński:** A, w ten sposób? OK. Teraz jest, bo ja nie jestem w tym temacie. No dobra, sprytnie to rozwiązaliście.

**Janusz Bossak:** Tak, tak, no. Czyli w momencie kiedy tu bym wpisał "Walne zgromadzenie", to powinno wyświetlić "Zarządzanie" na szaro, "Gremia kolegialne" na szaro i "Walne zgromadzenie".

**Kamil Dubaniowski:** No, to klientem z dorosłym.

**Damian Kamiński:** No ale to jest proste w sensie, żeby on to zrobił, no bo to bierze po prostu parent i tyle.

**Janusz Bossak:** Przy czym... Ojej, no proste, ale wiecie, no trzeba Markowi teraz dawać feedback, co ma zrobić. Na razie jest podłączone technicznie. Tak, teraz przechodzimy do fazy UX-owej, czyli żeby to ładnie wyglądało. Tak, technicznie widać działa. Jeszcze nie sprawdzałem tego, jak tu wybiorę...

**Damian Kamiński:** Tak, tak.

**Janusz Bossak:** To co to oznacza, że mam już w tym JSON-ie wszystkie informacje i mogę się do nich dobrać? Bo chodzi mi o to, że tutaj się nie... nie wpisują tu.

**Kamil Dubaniowski:** Tak, powinno być i to... To pewnie kodu Marek nie napisał.

**Janusz Bossak:** Pewnie Marek nie napisał kodu, aczkolwiek wydawało mi się, że coś tutaj... Jest "Ustaw".

**Kamil Dubaniowski:** A jest przykład z przyciskiem. Od przeciwnikiem.

**Janusz Bossak:** Parse JSON, no właśnie, no to ja zrobię inaczej.

**Kamil Dubaniowski:** Czy możesz dom przełączyć na automat?

**Janusz Bossak:** Powiedzmy tylko... Tylko właśnie mi chodzi o to, żeby to było inaczej. Ja chciałem zrobić to tak właśnie bez tych JSON-ów. Tak, i tu powinno być... To powinno być tak.

**Kamil Dubaniowski:** To coś nowego, bo my też się nad tym zastanawialiśmy. Teraz jest robione na wzór GUST. Identycznie jest ta funkcja JSON. Tutaj już źródło, a później rozpracowuje sobie.

**Łukasz Bott:** Wiesz co, sam mechanizm, który tutaj ja już w linii siódmej zaproponowałem, to już istnieje od dłuższego czasu. Pytanie, czy faktycznie TERYT i JRWA była?

**Janusz Bossak:** No dobra, no. Tylko pytanie, czy to działa? Nie.

**Łukasz Bott:** To obsługuje, nie. Sprawdźmy proste i tyle.

**Kamil Dubaniowski:** Spodziewam się, spodziewam się, że nie.

**Janusz Bossak:** Właśnie, czyli tutaj, co? Tak, nie tak?

**Łukasz Bott:** Chyba tak.

**Janusz Bossak:** Jeśli nie, nie, nie, nie działa. Tak.

**Łukasz Bott:** Czy możliwość nie jest dodana obsługa? Tak, no.

**Damian Kamiński:** Ale co chce się tam zrobić? Chcecie pobrać po prostu OK nazwę?

**Janusz Bossak:** Znaczy jest taka funkcjonalność, jak to jest polem Odnośnik, to tu można działać, tylko że to chyba działa tylko i wyłącznie na razie dla danych z odnośnika do procesu.

**Damian Kamiński:** Tak, tak, rozumiem.

**Łukasz Bott:** Do źródła zewnętrznego też, ale wygląda na to, że nie można. Być może GUST, TERYT, no i JRWA może nie obsługuje tej składni. O to mi chodzi.

**Damian Kamiński:** Ale po pierwsze nie wiadomo, czy ta składnia czy walidator...

**Janusz Bossak:** No dobrze.

**Damian Kamiński:** Dobrze interpretuję, to do tych chcesz zrobić, więc to niekoniecznie nie działa.

**Łukasz Bott:** No to też to.

**Kamil Dubaniowski:** Nie, Marek to dopytał i zrobił na wzór GUST, czyli spodziewam się, że tego nie obsłużą, no bo jeśli GUST nie było tutaj...

**Janusz Bossak:** Do mnie... Dobra, wersji, słuchajcie, wersji tej pierwszej, co robimy, absolutnie jest to wystarczające.

**Kamil Dubaniowski:** No, jedna linia kodu więcej, tak naprawdę nic się tym.

**Janusz Bossak:** Ponownie zamknij i ja to ustawiam na... Jako w trakcie edycji uruchomionej w trakcie.

**Łukasz Bott:** Automatyczną.

**Kamil Dubaniowski:** To warunek dopisz, mówiłem już, jeśli tego źródła jest wybrane.

**Janusz Bossak:** Dobrze. Przepraszam, jeżeli... Nie, JRWA... Źródło... Jest różne.

**Łukasz Bott:** Rozwaliły się.

**Janusz Bossak:** Tak, tak, widzę, widzę, widzę, widzę. Różne pustego. To wtedy... Części są. I tutaj koniec.

**Kamil Dubaniowski:** Pytam, w imię masz "J" na końcu zamiast zamknięcia kwadratowego nawiasu. W źródło.

**Łukasz Bott:** Źródłem, posłowie, źródło.

**Janusz Bossak:** To to widzę. Tak, tak, tak. Dzień dobry, jeżeli źródło jest różne od pustego, to wtedy rób to. Dobra, zamknij. Kliknij.

**Łukasz Bott:** Zgodnie ze szkoleniem zeszłego tygodnia powinno być jeszcze "else". No dobra, nie, no że na wypadek gdy jest puste, to tak, żeby wyczyścić, nie.

**Janusz Bossak:** A, no, no, no, tak robimy.

**Kamil Dubaniowski:** Jakby patrząc wydajnościowo, to jeszcze powinniśmy mieć dalej, że jeśli już uzupełni jakieś dane, to żeby nie mieli...

**Łukasz Bott:** Miał dość. Dobra.

**Janusz Bossak:** No i działa, nie? I tutaj elegancko się rzuca.

**Łukasz Bott:** Jak zmieniliśmy na inny?

**Janusz Bossak:** Czy mogę tak wybierać? To jest tutaj wybiera. Tak, no i teraz jak tutaj wybieram, nie wiem, "001". To jest "Rada nadzorcza", nie? I wybieram, to jest OK. No teraz pytanie właśnie, co tu w tym wierszu, w tym polu powinno się napisać? Tak, w moim przekonaniu powinno się napisać "001" przecinek albo spacja albo cokolwiek "Rada nadzorcza". Opis? Opis i tyle, nie.

**Damian Kamiński:** I tyle.

**Kamil Dubaniowski:** Opis, nie, opis może być bardzo długi. Tak, to wręcz trzeba zmienić na długi tekst dla mnie.

**Damian Kamiński:** Klasa nie dotyczy tych ludzi.

**Janusz Bossak:** Ewentualnie, ewentualnie ta kategoria, tak?

**Łukasz Bott:** Kategoria.

**Damian Kamiński:** Ja nie wiem, czy ten, co wpina, ma świadomość kategorii.

**Kamil Dubaniowski:** No to jest, to jest pewnie mniej istotne. To raczej dla archiwistów jest istotne. A ja tutaj widzę jeszcze jedną rzecz, która potencjalnie tam wraz z JRWA była i my tego tu nie mamy. Zgubiliśmy w sumie. Musi dodać do źródła: elektroniczne czy papierowe prowadzenie. Tego nie ma.

**Damian Kamiński:** Elektroniczna, tak. No.

**Kamil Dubaniowski:** Bo było w zgłoszeniu.

**Damian Kamiński:** I to by potrzeba było, żeby było już tam nawet na poziomie wyszukiwania, bo może być tak, że są 2 węzły, które są podobne. Jeden jest dotyczący elektronicznych, a drugi papierowych. Jeśli zawsze wpinam w 2 i zawsze mi się myli, więc oni tam też mają na poziomie wyszukiwania i drzewa już wskazane. Tak, to to też powinien być element, który według mnie powinien się pojawiać już tu.

**Janusz Bossak:** Tu się zastanawiałem.

**Damian Kamiński:** Jako EPI tyle.

**Janusz Bossak:** Tak, tutaj się zastanawiam, czy to nie powinno być drzewko? Nie. Nie tak spłaszczone, wszystko do lewej, tylko rzeczywiście, żeby to było "Zarządzanie", a tutaj z lekkim wcięciem "Gremia kolegialne" i z wcięciem "Walne zgromadzenie" i tak dalej, nie? Potem.

**Kamil Dubaniowski:** No to też sugerowałem, bo tego później nie będzie widać. Tylko też miejcie na uwadze, że i tak to wyświetlamy pierwszego liścia.

**Damian Kamiński:** No właśnie.

**Kamil Dubaniowski:** No bo nie załadujemy tu 900 pozycji, czy tam ponad 900. I spodziewam się, że będzie potrzeba zrobienia i tak wyboru typu "tree" – drzewo. Wtedy jakby świadomie ktoś przełączy na tym wybór, tak jak jest to w JRWA. No bo ktoś, kto zna symbole, będzie wolał tak, a ktoś, kto się uczy dopiero z tym, który symboli nie zna, no to będzie wolał drzewo całe z wcięciami, tak.

**Janusz Bossak:** No bo ja tak szczerze mówiąc...

**Damian Kamiński:** Bo to, co teraz macie?

**Janusz Bossak:** Myślałem, że to będzie tak jak tutaj, nie. Nie mam tu, zobaczcie, tu nie mam...

**Damian Kamiński:** No właśnie, no właśnie. Dokładnie to samo chciałem powiedzieć – wyszukiwarka, a nie przeglądarka.

**Janusz Bossak:** Że poza... No i jest poloneza, nie. I teraz, jeżeli chcemy iść w tą stronę, o którą mówicie, to to powinno być jako opcja. Bardziej bym to widział podobną do tego, co mamy przy wyborze przy polu typu Odnośnik dla procesu, gdzie mamy te filtry. Tak, i tam klikam, otwiera mi się okienko dodatkowe, w którym mam już pełnowymiarowe filtry. Tak, i wtedy miałbym kolumny: kategoria, kolumny nazwa, kolumny opis, kolumny tam kategoria archiwalna, kolumny coś tam jeszcze. Tak? I tam sobie szukam już, jak mi się chce bardzo precyzyjnie i ze wszystkiego. Tak. Natomiast tu to jest do szybkiego wybierania. Znaczy, bo wiecie, jaki jest cel? Tak sobie trzeba zadać pytanie, że tu widzę 20 rzeczy, to znaczy i tak nie wiem.

**Damian Kamiński:** To się nie ma. To jest połączenie 2 rzeczy.

**Janusz Bossak:** I tak nie wybiorę.

**Damian Kamiński:** Wyszukiwarki i drzewa. I wyszło taki trochę kadłubek, który właśnie nie jest ani dobrą wyszukiwarką, ani drzewem, bo sugeruje, że jest drzewem, a tak naprawdę jest wyszukiwarką.

**Janusz Bossak:** Więc może to sprowadzić do takiego czegoś, czyli żeby było – nie było tego symbolu tu rozwijania, tu tylko żeby był symbol taki, jaki jest. Wiecie, o co mi chodzi? Nie?

**Damian Kamiński:** Mhm.

**Kamil Dubaniowski:** Tak, tak, tak, tak.

**Janusz Bossak:** Tym, że.

**Damian Kamiński:** Po prostu ukryć te rozwijanie i tyle, bo wtedy jak wpiszesz tam, to też ci się pojawi wynik.

**Kamil Dubaniowski:** No tak, tylko to nie przejdzie. Znaczy przejdzie, bo to w sumie też zwrócą nam ze swoim po tych 20 pierwszych, tak jak mówicie.

**Damian Kamiński:** No dokładnie.

**Kamil Dubaniowski:** Ale to od razu już trzeba planować, może jeszcze nawet na przyszły tydzień, no zrobienie tego drugiego poziomu, czyli właśnie kliknięcia w jakieś wyszukiwanie zaawansowane, gdzie zobaczę całe drzewko. Czy, no nie wiem, jak wtedy pójść, bo ci ludzie, jak wyszło w locie, w ogóle zaczynają dopiero pracę z tym JRWA i ludzie z biznesu nie znają tej struktury kompletnie. Więc jakim damy takie czyste "wpisz", no to co oni mają wpisać? Oni wręcz będą się doktoryzować i tam zastanawiali, gdzie to pasuje.

**Damian Kamiński:** Mhm, muszą widzieć, że.

**Kamil Dubaniowski:** Przewidzieć drzewo na pierwszy strzał? Tak, bo tak jak później oni zaznaczyli, jak już się nauczą, to zazwyczaj to będzie 5 pozycji na osobę. W takim sensie, że dany człowiek z danego działu będzie używał 5 standardowo tam.

**Damian Kamiński:** Się nauczył, tak.

**Kamil Dubaniowski:** Klasy JRWA sugerowali, żeby podpowiadać te 5 ostatnio użytych. No to też będzie na dalszym etapie do zrobienia. Ale tak.

**Damian Kamiński:** Znaczy Janusz, ja bym powiedział, że... Bo czekajcie, to jest nowe pole dla JRWA.

**Janusz Bossak:** Widziałem. To jest, znaczy to.

**Damian Kamiński:** Nie, nie chodzi mi o JRWA. Wiem tam, to wiem, co to jest. To jest nowe pole.

**Janusz Bossak:** To jest pole typu Odnośnik.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** Do źródła zewnętrznego, który jest podpięty pod specjalne źródło zewnętrzne, jakim jest JRWA, tak jak GUST, TERYT.

**Damian Kamiński:** No dobra, to teraz, jakbyś przeszedł na to, według mnie powinniśmy stworzyć tu nowe okno wyszukiwania. Jakbyś przyszedł na grupy.

**Janusz Bossak:** No i teraz, ale teraz zobacz, bo chciałem tylko to pokazać. Tak, tu zasymulowałem na polu typu Odnośnik do procesu i jest jakby sam do siebie, nie? Czyli do tego procesu to robiła. I teraz tak, oby nie było.

**Damian Kamiński:** Mhm. No.

**Janusz Bossak:** Byłoby to.

**Damian Kamiński:** No.

**Janusz Bossak:** Czyli w tym polu, jak tutaj jest GUST, TERYT, no to pojawiłoby się taki symbol. I ten symbol oznaczał, że otwieram takie okienko. Tak, i tu już sobie wrzucam, co mi się tam podoba.

**Damian Kamiński:** No właśnie, nie wiem, czy takie, wiesz, bo tak jak powiedział Janusz, wyszukiwać, jak już będziesz wiedział, to wyszukasz z tamtego pola ogólnego. A jakbyś spojrzał na grupy, albo może ja pokażę, bo mam lepiej to przy...

**Janusz Bossak:** Rozumiem. Znaczy tu, tu mogłoby być, tu mogłoby być drzewo, nie.

**Kamil Dubaniowski:** Zdrową.

**Damian Kamiński:** Drzewo i jedna wyszukiwarka nad drzewem. Jeśli chcesz wyszukać, bo wiesz, że to w głównej gałęzi tej, ale w jakiś podgałęziach tej gałęzi.

**Janusz Bossak:** Tak, no też tak w ogóle, no. Tak.

**Damian Kamiński:** I tyle. Jedna wyszukiwarka i drzewo. I tam jest radio button na najniższym poziomie po prostu. I wybieram.

**Kamil Dubaniowski:** Że zrobiłbym, że domyślnie zwinięte, tak, żeby też nie rozwijać.

**Damian Kamiński:** Koniecznie, bo to... Gdzieś tam wisi to zgłoszenie jeszcze, nie, chyba nie obsłużone, ale jak takie drzewo ma kilka 1000 czy kilkaset wierszy... Nie wiem, jakie może być duże JRWA, to zależy od organizacji. No to potem, jeśli chcesz od razu je rozwinąć, to wymiana danych między backendem a frontendem może trwać kilka sekund, więc.

**Kamil Dubaniowski:** No, jeszcze niepotrzebne też, no bo człowiek będzie szukał głównej gałęzi, będzie schodził niżej. Jeśli chociaż mniej więcej już zdecyduje, że dobra, to prawdopodobnie będzie zarząd, taki tam sobie będzie schodził, schodzi, schodzi.

**Damian Kamiński:** No.

**Kamil Dubaniowski:** Jak podamy wszystko rozwinąć, to to będzie skanował 5 minut.

**Janusz Bossak:** Coś takiego, tak.

**Damian Kamiński:** Tak, tak.

**Kamil Dubaniowski:** Coś takiego, no.

**Damian Kamiński:** W zasadzie tak jak masz tu nawet po lewej stronie, bo tam masz też wyszukiwarkę. I to jest właśnie to "Wyszukaj JRWA" na górze czy "Wyszukaj" tam po prostu "Szukaj". Możesz szukać. Jak wpiszesz "45", to wyświetli ci się "45" i możesz rozwijać w dół. Tak, czy ta testowa. Czy masz jakieś, wiesz, że to jest na pewno nadrzędnych i teraz sprawdzasz to, co tam głębiej powinieneś się znaleźć?

**Janusz Bossak:** Tak. Dokładnie, no to tak powinno działać i okno z takim.

**Kamil Dubaniowski:** Czego to uzależnić? W sensie, że to jest dostępne tylko dla źródła o konkretnej nazwie? Czy to ma być jakieś ustawienie?

**Janusz Bossak:** Ja też byłam... Znaczy, wiecie, no, robimy to. My też JRWA, tak robimy.

**Kamil Dubaniowski:** Pewnie na źródło.

**Damian Kamiński:** Znaczy... Ale wiecie, to ja bym mniej się nie ograniczał już, że o jakiejś nazwie, bo może go być inne dane, które w ten sam sposób, bo tak samo przecież lampki możemy obsłużyć, więc.

**Janusz Bossak:** Słuchajcie, nie, nie, nie, nie, schodzimy na ziemię. Ja wiem, chętnie byśmy to pociągnęli, ale do JRWA, tak jak do GUST, powstały osobne tabele.

**Damian Kamiński:** Mhm.

**Kamil Dubaniowski:** Tylko podmiotach woła.

**Janusz Bossak:** Tylko po to było.

**Damian Kamiński:** OK, no dobra, dobra, to róbcie tak, żeby to zrobić po prostu.

**Janusz Bossak:** Więc ja wiem, ja też bym tak chciał, jak mówisz, też miałem takie zakusy i mam ciągle takie zakusy.

**Damian Kamiński:** Że jak źródło drzewiaste, to można to użyć, tak?

**Janusz Bossak:** Jak źródło drzewiaste, to ten tak. Ale JRWA jest jakoś tam specyficzne, no bo ma konkretne te kategorie, konkretne nazwy, konkretne opisy, konkretne kategorie archiwalne i tak dalej i tak dalej.

**Damian Kamiński:** OK.

**Janusz Bossak:** I to jest pod to. Tak, to jest specjalizowany moduł pod to. Można będzie według mnie i nawet należałoby w przyszłości rozważyć uniwersalizację tego, tak żeby to było właśnie dla takich struktur drzewiastych możliwe. Ale wygrała taka koncepcja na razie, żeby jednak to było od JRWA.

**Damian Kamiński:** Dobra, jasne.

**Kamil Dubaniowski:** Bo, bo, bo wiecie co, jakby tak zgadzam się, to trzeba pójść dalej kiedyś, jak będzie czas, bo wybór działu. Myślę, że to by było idealną.

**Janusz Bossak:** Tak, tak, tak, no jest dużo takich przykładów. Znaczy, to chyba trzeba będzie zrobić tak, żeby wykorzystać ten mechanizm jako taki. A źródło danym będzie różne, nie? Że jak podepnę, tak jak mówicie, jakieś coś nowego, co będziemy mieli typu działy.

**Damian Kamiński:** I zrobić to odrębnie.

**Janusz Bossak:** To ten mechanizm powinien zadziałać.

**Damian Kamiński:** Mhm.

**Kamil Dubaniowski:** Jakby JRWA jest domyślnie, bo ma swoją dedykowaną tabelę, wiemy gdzie będzie parent wskazany i to sobie obsługujemy bez zwykli kiwania. A dla takiego źródła twojego, którego my nie znamy, no to pewnie będzie to ustawienie. Będziesz musiał wskazać kolumnę z parentem i tak dalej. Tak. No dobra, zostawmy tak. Czy jeszcze coś chcemy o tym pogadać, bo jeśli nie, to ja bym zatrzymał nagrywanie dla notatki.

**Janusz Bossak:** Dokładnie.

**Kamil Dubaniowski:** No i pójdziemy dalej.

**Janusz Bossak:** Dobrze.

**Damian Kamiński:** Ja muszę się przełączać na nim.

**Janusz Bossak:** A ja szczerze mówiąc się muszę przełączyć na Przemka na tym.

**Kamil Dubaniowski:** Dobra, no to i tak myślę, że dobrze poszło. W sensie jeszcze. Janusz, tak podsumowując, co my tam pogadaliśmy chwilę na tym trialu, że my byśmy pewnie potrzebowali, żebyście to wy z Przemkiem wyznaczali nam cel, a my sobie dalej idziemy z tym, już organizujemy się, rozpisujemy zadania, bo żeby nie było takich sytuacji, że to my wybieramy cele, bo później przychodzi Przemek czy ty i mówicie, że to nie są te cele, a my już gdzieś...

**Janusz Bossak:** Tak. Tak bym chciał. Nie rozumiem, to roadmapa jest taka ważna, wiesz, musi być ta mapa i my musimy się nauczyć, no realizować cele z tej roadmapy. Tak, ja. No tak jak teraz jest ten sprint, to właśnie to jest sytuacja, to już taka chyba, która będzie typową sytuacją, że są 2 cele na ten sprint. Jeden to jest oddanie do użytku repozytorium, gdzie repozytorium jest zainstalowany u klienta i to właśnie tak sformułowany cel. O, już się Przemek.

**Damian Kamiński:** No.

**Kamil Dubaniowski:** Dobra, to jeszcze mam.

**Damian Kamiński:** No tak.

**Janusz Bossak:** Mieć przegląd tego, żeby to robić we właściwym, że tak powiem, kierunku. Przepraszam, muszę się przebrać.

**Kamil Dubaniowski:** Dobra, jeszcze mamy design, to będę musiał kontynuować. Dzięki.

**Damian Kamiński:** Nie, no jasne.

**Janusz Bossak:** Dobra.

**Damian Kamiński:** Cześć, no dobra.

**Janusz Bossak:** Zatrzymano transkrypcję.

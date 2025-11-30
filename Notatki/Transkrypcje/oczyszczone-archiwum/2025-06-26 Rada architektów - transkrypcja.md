**Data spotkania:** 26 czerwca 2025

**Adrian Kotowski:** Komunikujemy, że pozostałe kanały byłyby po prostu takimi formami wymiennymi.

**Janusz Bossak:** Dobra, musimy to jakoś przeanalizować. Powiem tak, to co teraz pokazuję na ekranie – zobaczcie, w zasadzie mamy tę funkcjonalność news feedu. Skąd pochodzi ta informacja?

**Janusz Bossak:** W naszym przypadku pochodzi z systemu zewnętrznego, z bloga na amodit.pl. Tam jest coś oznaczone i tu się pojawia. To jest news feed. To, co powiedział przed chwilą Mateusz, zainspirowało mnie. Już wam pokażę, o co chodzi.

**Janusz Bossak:** Rozumiem, o co chodzi Mateuszowi. Nie patrzcie, że to się nazywa teraz "Baza wiedzy", to będzie się nazywało "Newsy". Wniosek czy ogłoszenia?

**Janusz Bossak:** Tak, to by się nazywało "Ogłoszenia". Wchodzimy i tu mamy ogłoszenie, np. o "Skowronku", które ma jakąś treść. Tutaj, na tym etapie, to kwestia dorobienia uprawnień: kto to ogłoszenie ma widzieć (tylko właściciel, admini, nikt, wybrane osoby, grupy itd.).

**Janusz Bossak:** Więc zrobimy sobie ogłoszenia. To nie będzie "Baza wiedzy", tylko "Baza ogłoszeń", lista ogłoszeń. I takie ogłoszenia nam budują... To się zrobi osobno?

**Janusz Bossak:** Powiedzmy "Ogłoszenia" i będziemy mieli te anonse i ten news feed załatwiony właściwie w jednym. Czyli dorabiamy mechanizm taki jak baza wiedzy, gdzie korzystamy z tego kodu.

**Piotr Buczkowski:** A gdzie to jest zapisywane?

**Janusz Bossak:** To jest teraz zapisywane... Nie wiem gdzie to jest zapisywane, Mateusz?

**Mateusz Kisiel:** To jest zapisywane w dwóch miejscach. Raz po stronie mikroserwisu z ChromaDB, a druga rzecz po stronie AMODIT – AMODIT ma do tego dostęp. To, co robiliśmy – tabelki, pamiętasz?

**Janusz Bossak:** No ale to mogłoby być zapisywane po stronie jakiejś tabelki newsów i już. Dodatkowa tablica SQL. Po prostu jest news i lista osób, które się do tego doczepiają.

**Piotr Buczkowski:** Ale to jest całkiem nowy mechanizm zrobiony tak jak to, tak?

**Janusz Bossak:** No całkiem nowy mechanizm.

**Mariusz Piotrzkowski:** Zastanówmy się...

**Piotr Buczkowski:** [Niezrozumiałe] pojęcie od razu?

**Janusz Bossak:** Ale zobaczcie. To już mamy, w sensie tutaj Mateusz ma to do bazy wiedzy, więc kod mamy. Więc wystarczy niektóre rzeczy ponazywać inaczej, to nie jest jakieś "rocket science".

**Piotr Buczkowski:** Nadawać uprawnienia, pilnować uprawnień.

**Mateusz Kisiel:** Jedna rzecz jest inna, bo tak – zapisujemy te rzeczy w tym mikroserwisie z ChromaDB.

**Piotr Buczkowski:** No to nie będzie żadnego mikroserwisu.

**Mateusz Kisiel:** No właśnie, więc musielibyśmy zapisywać w innym miejscu. Trzeba to zmienić.

**Janusz Bossak:** No ale...

**Piotr Buczkowski:** Zrobić nowy?

**Janusz Bossak:** No i?

**Mateusz Kisiel:** Tak, no.

**Piotr Buczkowski:** Bo to jest całkiem inny mechanizm. Może będzie wyglądać tak samo, ale to jest całkiem inny mechanizm.

**Janusz Bossak:** Ja wiem, rozumiem, ale chodzi o to, żeby pokazać panu Piotrowi, że to tak będzie wyglądało. Tak, to będą newsy. Tu sobie wrzucasz nowy news, piszesz zawartość tego newsa.

**Piotr Buczkowski:** Już się przyczepi: "To dodaj dokument". Co to za dokument?

**Janusz Bossak:** Ojej, no to będzie się nazywało news czy anons.

**Piotr Buczkowski:** Ale zaraz się przyczepi.

**Janusz Bossak:** Ja wiem, on jest specyficzny.

**Piotr Buczkowski:** Jak zobaczy "Dodaj dokument"...

**Janusz Bossak:** Tak, to jest jedna ścieżka. Natomiast uważam, że jest całkiem OK na te anonse i news feedy ta ścieżka, o której Damian mówiłeś – że z Wiktorem to ogarniecie procesami, tylko nie można mu powiedzieć, że to są procesy.

**Piotr Buczkowski:** Czy trzeba zdefiniować proces, zrobić widok, zrobić raport, udostępnić widok w menu i skonfigurować?

**Janusz Bossak:** Tak. Dokładnie gotowy, wszystko skonfigurowane, ponazywane i to jest po prostu zrobione na procesie. Panu Piotrowi się po prostu nie podoba, że wiele rzeczy w AMODIT, takich które on uważa za natywne funkcjonalności, my robimy na procesach.

**Janusz Bossak:** No właśnie takie anonse. To powinna być według niego natywna funkcjonalność systemu. System powinien umieć obsługiwać anonse. Tylko my mamy zupełnie inną filozofię.

**Janusz Bossak:** Niby po co tak ma być, skoro 90% klientów tego nie chce? A 10% może chce. No to te 10% może zrobić to sobie na procesie. Dokładnie to samo z tym procesem.

**Janusz Bossak:** I tu akurat po części się zgadzam, że powinniśmy z panem Piotrem na te procesy patrzeć. Tak jak w przypadku tego [projektu], gdzie pora reakcji/SLA to "use case", żeby tu było jak najmniej, żeby to nie było obciążone tymi wszystkimi elementami procesu.

**Janusz Bossak:** To musi być jakiś mechanizm, który "obdziera" tę sprawę ze wszystkiego, co jest zbędne w danym kontekście. Jeżeli jesteśmy w kontekście anonsu, to widać tylko to, co ma być widać. Koniec, nic więcej.

**Piotr Buczkowski:** Przecież można ukryć te przyciski z ustawy/konfiguracji.

**Janusz Bossak:** Tak, właśnie o to mi chodzi, ale to musiałoby być jakoś tak sprytnie zrobione. Wtedy da się to wykorzystać do wielu znaczeń.

**Piotr Buczkowski:** Ja tutaj taką opcję bym dodał, żeby wyświetlać komentarze jako zakładkę.

**Janusz Bossak:** Tak, one powinny zająć tutaj miejsce... coś w tym rodzaju?

**Piotr Buczkowski:** Nie komentarze, żeby to miało sens, komunikator – te komentarze muszą być w głównej części.

**Janusz Bossak:** Tak, to jest pomysł, który też rozważałem. Czyli sprawa w procesie, który się nazywa "Komunikator"? To taka jedna sprawa byłaby jakimś wątkiem?

**Janusz Bossak:** Zakładam wątek, w tym wątku wybieram sobie osoby, z którymi chcę gadać i piszę do nich. Do niektórych piszę jawnie, np. do Damiana, ale wcześniej do tej sprawy, tam gdzie obserwatorzy czy współpracownicy, dodałem sobie np. Arka.

**Janusz Bossak:** I teraz mogę wskazać/wzmiankować jedną osobę z tej grupy i wtedy mamy taką sprawę, która jest związana z jakimś tematem i ma ileś tam osób. To odpowiednik takiego czata.

**Piotr Buczkowski:** I co do czatu – to nie będzie czat, bo po czacie spodziewam się, że jak coś napiszę, albo ktoś mi odpisze, to ja to widzę bez konieczności odświeżania strony. A tego nie mamy.

**Adrian Kotowski:** Trzeba by jakiś mechanizm dołożyć. Też pytanie, czy można by ukryć ten formularz? Wtedy ten widok formularza sprawy... Bo jeżeli zakładam, że tutaj [komunikujemy się].

**Janusz Bossak:** To musiałoby tak być, że to wszystko tutaj znika.

**Piotr Buczkowski:** To ja zaproponowałem, żeby ustawić komentarze na formularzu jako sekcję. Wtedy powiedzmy, mamy jedną sekcję i tam wskazujemy tytuł, czy do kogo ma to być kierowane (do grupy itp.).

**Mariusz Piotrzkowski:** Odnośnie tego, co mówisz – zastanawiam się, czy jeżeli dużo osób miałoby taki komunikator cały czas w tle odpalony, to czy to by nie zjadło zasobów serwera? Bo biorąc pod uwagę, że to będzie rzeczywiście sprawa...

**Piotr Buczkowski:** Zjadłoby.

**Mariusz Piotrzkowski:** No to, czyli to raczej byłoby ciężkie. Nie wiem, czy nie lepiej byłoby po prostu zainwestować trochę czasu i zrobić to osobno? Funkcjonalność do komunikacji real-time jako osobny mechanizm na serwerze i potem to ewentualnie połączyć w jakiś inny sposób?

**Piotr Buczkowski:** Znaczy, moja propozycja była taka, żeby wykorzystać istniejący mechanizm, zainstalować obok i podpiąć dla AMODIT.

**Mariusz Piotrzkowski:** Taka [aplikacja] to nie będzie się otwierać sama z siebie. Oni chcą komunikator.

**Piotr Buczkowski:** Jak będzie istniejący mechanizm, który się odświeża sam z siebie, no to będzie się odświeżał.

**Janusz Bossak:** Tak, o to mi chodzi, ale to musiałoby być jakoś tak sprytnie zrobione, żeby nie zawsze zjadało zasoby, tylko wtedy, kiedy rzeczywiście jest to potrzebne.

**Adrian Kotowski:** Można by to wygrać tak: ten proces będzie miał interaktywne komentarze, a wszystkie pozostałe domyślnie tego nie będą miały.

**Mariusz Piotrzkowski:** Tylko czy oni potem by nie chcieli, żeby im na przykład powiadomienia przychodziły? Że jak mają odpaloną kartę w tle (załóżmy mają 10 kart i jedna z nich to komunikator), to jakiś dźwięk im się odtwarza jak przyjdzie wiadomość? Bo jeżeli tak, to już w ogóle "zabijemy" serwery.

**Mariusz Piotrzkowski:** To może w takiej sytuacji po prostu zrobimy osobne systemy i jakąś integrację? W tym sensie, że instalujemy coś na bazie Matrixa albo jakieś forum?

**Janusz Bossak:** Tak, dlatego była wczoraj taka sugestia, żeby może poszukać jakiegoś gotowca, komunikatora open source i się zintegrować.

**Mariusz Piotrzkowski:** Kwestia czy musi być odpowiednia licencja? Jak będzie na licencji GPL v3, tak jak większość bibliotek do Matrixa, no to tego nie możemy zaimplementować. Musielibyśmy wtedy kod AMODIT udostępnić.

**Piotr Buczkowski:** Jakby było obok, to nie byłoby częścią AMODIT, tylko stałoby obok.

**Mariusz Piotrzkowski:** No przecież GPL v3 działa tak, że jeżeli bibliotekę podłączysz do swojej aplikacji, to zgodnie z licencją wszystko też musi być open source. Do czego jest używana ta biblioteka?

**Adrian Kotowski:** Jakby to był oddzielny komponent.

**Mariusz Piotrzkowski:** No w takiej sytuacji dałoby radę to obejść. Oczywiście trzeba by naprawdę dobrze do tego podejść, żeby tej licencji nie złamać.

**Janusz Bossak:** Można też poszukać czegoś, co jest na licencji MIT. Więc to byłoby w sumie chyba najprostsze. Inne rozwiązanie to napisać to, biorąc ten Cursor AI i kazać mu napisać taki komunikator (łamiąc wszelkie zasady efektywności kodu) i skompilować go.

**Mariusz Piotrzkowski:** To by tak szybko nie poszło.

**Adrian Kotowski:** A jakbyśmy poszli w stronę tego, że jest to oddzielny komponent, poza AMODIT, to jak informować użytkowników o tym, że mają wiadomość w tej aplikacji? Wiem, że trzeba [mieć powiadomienia].

**Piotr Buczkowski:** Dodalibyśmy jakąś integrację, która łączy się z tą aplikacją, coś tam pobiera i wyświetla.

**Adrian Kotowski:** I każdy ma skrzynkę. Ten mail jest... No też myślę, że nie.

**Adrian Kotowski:** Ktoś weźmie pod uwagę, że trzeba tu jednak komunikat instant.

**Mariusz Piotrzkowski:** No ale w sumie na frontendzie to możemy po prostu do innej witryny/serwera się odwołać i żeby sobie pobierał na bieżąco komunikaty (np. raz na minutę sprawdzał w sprawie).

**Piotr Buczkowski:** Sprawdzał aktualne requesty.

**Janusz Bossak:** No dobrze, słuchajcie, dziś ile jest różnych pomysłów? Na razie nie mamy nawet pomysłu, nad którym możemy zacząć pracować.

**Janusz Bossak:** Dobra, słuchajcie, "parkujemy" ten temat? Bo to zajmuje nam dużo czasu. Prośba do was, żeby do końca dnia pogłówkować przy kawie/herbacie i wrzucić różne pomysły na naszej grupie, na kanale "Wymagania".

**Janusz Bossak:** Jak zorganizować ten komunikator? Anonse, rozumiem, robimy na procesie (tak jak mówiłeś Damian) i ten news feed też jako proces. Na razie zobaczmy, czy da się to tak "przepchnąć".

**Mateusz Kisiel:** Jeszcze co do tych newsów – gdyby to zrobić w tej obecnej bazie wiedzy (czyli zapisywanie w bazie wektorowej), to od razu można by też pytać o ten news AI (AskAI)?

**Piotr Buczkowski:** Tam nie będzie dostępu do zewnętrznego systemu.

**Janusz Bossak:** Znaczy, pan Piotr rozważa podpięcie się, jakieś tam otwarcie kanału, ale na razie bym tego nie mieszał. To na później. Z drugiej strony, tak "biznesowo" to nie bardzo pasuje – o newsie chcę się dowiedzieć, a nie o niego zapytać. News po prostu jest.

**Mariusz Piotrzkowski:** Jeżeli mogę – to ja co najwyżej bym zrobił coś takiego, że na czacie po prostu jest funkcja "Zapytaj AI" i to by się łączyło z naszym AMODIT-owym AI. Ale to już jest kolejna sprawa.

**Janusz Bossak:** Nie, nie, te anonse i news feed... Mówię, albo robimy to jako proces, albo tak jak pokazywałem – tym mechanizmem. Teraz mamy nowości, które przychodzą z REST API (z połączenia z WordPressem, na którym jest nasz blog AMODIT). Ale przecież taki news feed, tu na drugiej zakładce, mógłby przychodzić z dowolnego źródła.

**Janusz Bossak:** Można zrobić prosty mechanizm dodawania takich newsów i określania [widoczności], tak jak na przykładzie interfejsu tej bazy wiedzy. Robilibyśmy prosty mechanizm, gdzie te newsy się wpisuje i pojawiają. Nawet do tego stopnia, że takim newsem jest sprawa w procesie.

**Janusz Bossak:** Ten news feed jest podłączony do procesu o nazwie "News feed" czy "Anonse". I tak jak się sprawy/zmiany pokazują, tak na tej samej zasadzie pojawiałyby się sprawy z tego procesu "Anonse". Żeby to było w powiadomieniach, żebym nie musiał szukać, robić jakiegoś raportu. Wchodzę w "Anonse" i widzę. Tak jak Damian mówisz – to powinny być sprawy.

**Damian Kamiński:** Tak by było najprościej. Nie musimy wtedy nic robić. Jakikolwiek pomysł/wymaganie robimy na poziomie konfiguracyjnym, a nie deweloperskim.

**Janusz Bossak:** Dobrze, to parkujemy ten temat. Chwilowo mamy temat gruby – to jest "Repozytorium". Ale tutaj ja sobie zanotowałem, że czekamy na wymagania od Piotra Murawskiego. Zanim cokolwiek wymyślimy, to trzeba posłuchać, jak on rozumie "repozytorium".

**Janusz Bossak:** Jesteśmy w sporze co do rozumienia słowa "repozytorium" – my rozumiemy inaczej, on rozumie inaczej. Czekamy na informację od niego.

**Janusz Bossak:** Potem mamy temat "Call function" (wywołanie funkcji). Tu ustaliliśmy, jak rozumiem, że dodajemy możliwość wywołania z innych procesów. Czyli dodajemy drugi parametr do "Call function". Opcjonalny – jak go nie ma, to woła z tego procesu. Jak jest, to może zawołać z innego procesu.

**Janusz Bossak:** Ustaliliśmy, że na razie nie dodajemy parametrów, zostawiamy tak jak jest. Czyli albo ktoś stosuje sobie jakieś parametry jawnie (tworzy zmienne), które potem są w ramach tego "Snippetu".

**Piotr Buczkowski:** On chce "Snippet", nie funkcję. To u nas się snippets nazywa funkcją.

**Janusz Bossak:** To proponuję dokonać zmiany i dla pana Murawskiego nazwać to "Call snippet". Szczerze mówiąc, jak to robiliśmy, to trochę protestowałem przeciwko nazwie "Call function", bo to właśnie żadna funkcja nie jest. Tylko jest to wstawianie kawałka kodu w miejsce, w którym się to wywołuje. To trochę miesza.

**Janusz Bossak:** Może czas na zmianę nazwy? Ale tak jakoś kompatybilnie, żeby stara nazwa też działała (alias), ale się nie podpowiadała. Nowa nazywa się "Call snippet" i w opisie przestajemy nazywać to "function", tylko "snippet". Wiadomo wtedy, co to jest.

**Janusz Bossak:** Na razie pozostawiamy tak. Nawet nie zmieniając nazwy funkcji jest szansa, że on to "łyknie".

**Janusz Bossak:** Jest też duży temat: zmienne procesu. Tutaj sytuacja jest taka sama – kompletnie inaczej my rozumiemy zmienną procesu, a on inaczej. To, co Przemek tłumaczył – on to wziął z BPMN (Business Process Model and Notation), gdzie jest takie pojęcie jak zmienna procesu.

**Janusz Bossak:** On jako przykłady podaje: 1) początkowa liczba dni urlopu dla wszystkich pracowników, 2) dostępna liczba dni konsultacyjnych różnych lekarzy w różnych dniach. Z punktu widzenia AMODIT nie ma czegoś takiego jak "zmienna procesu". Gdzie to miałoby być w procesie?

**Piotr Buczkowski:** Co on rozumie przez proces? Nasz proces (czyli sprawy)? Bo tutaj trochę nie rozumiem.

**Janusz Bossak:** No właśnie, czepia się nazewnictwa. Z naszego punktu widzenia my to mamy, bo to są u nas rejestry, tylko że on może nie chcieć słyszeć o rejestrach. Zaraz mu się włączają wszystkie negatywne skojarzenia.

**Janusz Bossak:** U nas to jest albo rejestr, albo słownik, albo źródło danych. On sam sobie trochę zaprzecza, bo mówi o zmiennej procesu, a potem mówi, żeby to było możliwe do wykorzystania w każdym procesie (np. te dni urlopowe). No to to już nie jest zmienna procesu, tylko zmienna systemowa.

**Adrian Kotowski:** Nawet można powiedzieć, że globalna.

**Janusz Bossak:** Tak.

**Piotr Buczkowski:** No ale to są bardziej jakieś dane tabelaryczne, np. lista pracowników, lista dni urlopu (pracownik – dni urlopu).

**Janusz Bossak:** Tak.

**Piotr Buczkowski:** Może warto jakoś usprawnić aktualizację tego?

**Janusz Bossak:** Dokładnie. Mamy te źródła danych (już nawet dobrze się nazywają "Zewnętrzne źródła danych"). I tu jednym ze źródeł jest "Static". Nawet lepsze niż Excel. Biorę sobie jakiegoś Excela, wrzucam plik, który ma 1500 pracowników i początkową liczbę dni urlopu, i mam tutaj tabelkę tych ludzi. Oczywiście trzeba zadbać o identyfikatory itd.

**Janusz Bossak:** I teraz, biorąc sobie jakiś proces, powinno być coś podobnego jak funkcja `GetDictionaryItem`. Podaje się nazwę słownika (w naszym przypadku nazwę źródła danych), podaje się item ID i zwraca value.

**Łukasz Bott:** Ale Janusz, czekaj. Jeżeli chodzi o źródła danych, to po stronie reguł mamy obsługę w tym trybie obiektowym.

**Janusz Bossak:** Ja wiem. Ale mówię o drugą stronę. To pokazuję na przykładzie `Get`, ale potrzebny jest też `Set` (ustawianie wartości). `Get` jest łatwiejszy.

**Łukasz Bott:** OK. Ale jeśli chodzi o to, żeby `Set` zrobić...

**Janusz Bossak:** No chodzi mi o to, żeby był taki odpowiednik `Get`, żeby był `Set`. Albo trzeba zrobić jakiś nasz `SetEx` (Set External) do zewnętrznego źródła. Podajemy nazwę, podajemy item ID i podajemy value.

**Łukasz Bott:** Oczywiście to by działało tylko dla tych źródeł, które są reprezentowane w bazie danych AMODITa, tak?

**Janusz Bossak:** Tylko tak. Nawet byłbym skłonny pójść dalej i takie źródła danych muszą być specjalnie oznaczane. Na pewno muszą mieć ten tryb "Static". To nie może być SQL elem, musi być "local".

**Piotr Buczkowski:** Jeżeli to jest online, to trzeba zapewnić jakąś procedurę "ratującą".

**Janusz Bossak:** Według mnie "Static", absolutnie tylko i wyłącznie "Static" powinien mieć taką możliwość. To jest wtedy rzeczywiście coś, co można nazwać zmienną AMODIT-ową/modelową. Jest taki zbiór "Static", wrzuciliśmy tam ileś pozycji, kolumn, informacji. To na przykład może się nadawać do budżetów. Idealnie – mamy jakiś budżet na coś.

**Piotr Buczkowski:** Gdzie indziej to się chyba "matryce" nazywa.

**Janusz Bossak:** No często jakieś matryce się robi w rejestrach, a tak to można by robić tutaj. Takie źródło "Static" wrzucam i mogę na nim manipulować. Tylko musimy mieć mechanizm `Set` – trzeba się zastanowić jak to zrobić, żeby też od strony wydajnościowej było sensownie (może kilka wartości naraz aktualizować, a nie każdą po kolei).

**Janusz Bossak:** Pewnie w większości przypadków to jest jednostkowa zmiana. Np. zmieniam liczbę dni urlopu z 26 na 24 i zapisuję.

**Piotr Buczkowski:** Znaczy urlop to jest zwykle: liczba dostępnych w roku, liczba wykorzystanych, liczba pozostałych, liczba planowanych.

**Janusz Bossak:** Tak, ale to samo masz przy budżecie finansowym – masz jakąś kwotę 100 000 i wykorzystaną jakąś część.

**Anna Skupińska:** To brzmi trochę jak jakieś parametry, tylko że użytkownika, a nie systemowe.

**Janusz Bossak:** Tak.

**Piotr Buczkowski:** Urlop może być per użytkownik, ale mogą być też dane dotyczące jednostek organizacyjnych, sprzętu itp.

**Janusz Bossak:** To otwiera zupełnie nowe możliwości. Tak jak Piotr powiedziałeś – sprzęt. Możemy mieć listę sprzętu (komputery, monitory, myszki) i sobie na tej liście wpisywać różne rzeczy. Nie musimy robić spraw.

**Janusz Bossak:** Wprawdzie nie ma wtedy historii zmian wprost w źródle, ale historia będzie po stronie tych spraw, które to zmieniają. Ta sprawa zmieniła liczbę monitorów z 5 na 4, a inna sprawa dotycząca przyjęcia nowych monitorów zmieniła z 4 na 20. To się da wy-raportować później.

**Janusz Bossak:** Ale to byłaby rewolucja w pewnym sensie – zupełnie inny sposób myślenia o tworzeniu procesu i tych danych. Myślę, że to by go [klienta] mocno satysfakcjonowało, gdybyśmy to pokazali.

**Janusz Bossak:** Potrzebujemy tylko tego "Seta" sprytnego do tego. Przy założeniu, że jest to źródło danych "Static". Czyli raz wrzucamy i ono siedzi u nas jako "Static" i nie można go zmieniać [ręcznie/z zewnątrz], tylko można go zmieniać od tego momentu z poziomu procesów. Pewnie też i dodawać nowe pozycje – np. jak kupiliśmy nowy typ monitora, to powinniśmy móc dodać go do takiego źródła.

**Damian Kamiński:** Samo źródło jeszcze powinniśmy zabezpieczyć. Moje spostrzeżenie z [innego projektu] – można dodać źródło "Static", ale można je jednym przyciskiem usunąć.

**Janusz Bossak:** To może jeszcze powinien być inny typ? Nie "Static", bo "Static" źle się kojarzy (że statyczne).

**Łukasz Bott:** Źródło danych edytowalne.

**Janusz Bossak:** Jakoś tak.

**Łukasz Bott:** Przy czym można je zainicjować np. importem z Excela.

**Janusz Bossak:** Tak. Ale można też zrobić i zostawić puste. I przyjmujesz pierwszy monitor na stan i go procesem dodajesz.

**Damian Kamiński:** No tak, ale musisz zainicjować samą tabelę, więc albo Excelem, albo w bazie danych musisz wyklikać strukturę tej tabeli.

**Janusz Bossak:** Ale nawet jakby tutaj nie wybierać Excela, tylko wpisać nazwę i zrobić "Zapisz", to powinno utworzyć pustą tabelę DBSRC_12.

**Damian Kamiński:** Nie, wtedy powstaje normalnie tabela w bazie danych, ale kolumny trzeba wyklikać.

**Łukasz Bott:** No racja, to jest dobre.

**Janusz Bossak:** No dobrze, to mogłoby być tak jak tutaj jest. Czyli jest Excel, wybieram sobie typy pól, wybieram nazwy.

**Damian Kamiński:** Musi być tak, żeby to było uniwersalne, też na chmurze. Żeby ktoś bez dostępu do bazy mógł sobie to zdefiniować.

**Janusz Bossak:** To będzie taki "Static", tylko żeby później nie można było usunąć źródła danych, bo się wszystko rozsypie.

**Łukasz Bott:** Jak ktoś sobie popsuje, to popsuje.

**Janusz Bossak:** Słuchajcie, z tą koncepcją się zgadzamy, rozumiem. Czyli jedziemy na tym czymś, co tutaj potencjalnie nazywa się "Static". Na razie nie zmieniając niczego na zapleczu. W sensie źródła danych – wczytujesz Excela i korzystasz. I tylko takie źródło mogłoby być "setowane". Musielibyśmy mieć dwie rzeczy: `Set` i `Add`.

**Łukasz Bott:** Funkcja `Set` mogłaby po prostu wykrywać: jeżeli podany jest klucz, którego nie ma jeszcze, to robi `Insert` (Add). A jeżeli wywołam dla pozycji, która już istnieje, to robi `Update`.

**Janusz Bossak:** Było coś takiego kiedyś? `GetExcelData`... to jest sytuacja, kiedy mamy plik Excela przypięty do sprawy, to wtedy możemy coś tam poprawić. Ale nie mieszajmy tego. Chodzi mi o to, że musi być jakaś funkcja `Set`, nie wiem czy to ta sama – ja bym raczej zrobił nową `SetEx` (external set). I tak samo mógłby być `GetEx`.

**Piotr Buczkowski:** Ja bym zaproponował coś jak `ForRecord` – że możemy kilka pól przypisać.

**Piotr Buczkowski:** Nazwa pola, odnośnik zewnętrzny i tam możemy jako nazwę po prostu pola... czy pobrać czy ustawić.

**Janusz Bossak:** Piotrze, zastanów się nad tym. Dobra.

**Janusz Bossak:** Jeszcze jeden temat, który mam do Ani – to jest heatmapa (filler?). Musimy wrócić do tematu, który był omawiany jeszcze za czasów Krystyny, a mianowicie kolorowanie.

**Anna Skupińska:** Jednak trzeba będzie dać kolorowanie gradientów.

**Janusz Bossak:** [Notowanie?] pivota.

**Anna Skupińska:** No bo teraz jest tak, że tylko kolorowanie takich rzeczy, które nie są gradientami, może sobie stać. A gradienty są kodowane [jako] kolory w środku.

**Janusz Bossak:** Przechodząc do edycji kolorów – jemu chodzi o kolorowanie gradientowe. Czyli tu musiałaby być kwota w walucie krajowej.

**Janusz Bossak:** Są dwa podejścia do tego. Jeden to zrobienie tego na tym pivocie – mamy agregację i precyzję, a trzeba by było trzecią rzecz: kolor. I tam w tym kolorze wybierać (najmniejsza, największa wartość – zielona, czerwona itd.).

**Janusz Bossak:** Natomiast druga koncepcja moja: AmCharts ma heatmapę. To jest taki wykres w sumie.

**Łukasz Bott:** AmCharts.

**Janusz Bossak:** Jak tam siedzi? U nas nie?

**Łukasz Bott:** No "zerżnęli" od nas.

**Janusz Bossak:** I to jest druga koncepcja. Może trzeba po prostu dodać typ "Heatmapa"? Wziąć ten typ i go dodać do monitora?

**Anna Skupińska:** Czyli taki typ jak pivot, tylko że nie możesz robić wielu kolumn, tylko jeden wiersz, jedną kolumnę?

**Janusz Bossak:** No tak: wiersz, kolumny i jakieś gradienty kolorowe. Tam można podawać minimum, maksimum. Trzeba rozkminić co tam można zrobić. Ale taką heatmapę można dać.

**Janusz Bossak:** Znaczy jedna i druga rzecz jest przydatna. Wrzucenie tych kolorów/zarządzania kolorami na pivocie trzeba zrobić i tak, i tak, bo mamy to już przygotowane w sensie projektu. A niezależnie można spróbować dodać nowy typ wykresu (oprócz liniowych, słupkowych) – heatmapę.

**Janusz Bossak:** Proszę się nad tym zastanowić, w szczególności podejściem do tego pivota. Trzeba przypomnieć kwestie omawiane z Krystyną – wersja minimalistyczna. Taka, żeby przynajmniej dało się kolory zmieniać, bo jemu się nie podobało, że najwyższa wartość jest niebieska, a on chciałby czerwoną. Trzeba umożliwić ustawianie koloru w tym gradiencie.

**Anna Skupińska:** Wydaje mi się, że były dwa zadania do projektu: jeden na heatmapę, a drugi na to, żeby można było zmieniać kolory w gradientach.

**Janusz Bossak:** Tak, rozbudowa pivota o możliwość edycji kolorów, przynajmniej w postaci gradientu.

**Janusz Bossak:** No dobra, słuchajcie, to tyle mamy. Czyli tak: komunikator – wszyscy się zastanawiamy. Anonse/news feedy robi Wiktor z Damianem na procesie. A my się zastanawiamy nad tym, żeby tutaj to podłączyć.

**Janusz Bossak:** Repozytorium – czekamy. Wielofirmowość – pokażemy co mamy. I ta heatmapa oraz ten `Set`/`Get` do źródła danych. To jest według mnie bardzo fajna rzecz, będę naciskał, żebyśmy to zrobili, bo to uprości wdrożenia i poprawi wydajność (nie będą konsultanci robić rejestrów po 400 000 pozycji).

**Janusz Bossak:** Dobra, kończymy. Mam za chwilę spotkanie z Przemkiem.

**Mariusz Piotrzkowski:** Jeszcze chciałem wam pokazać coś na szybko, dosłownie 30 sekund. Testowałem sobie filtry do WCAG. Kusiło mnie, żeby sprawdzić, jakby można było zrobić tryb ciemny w AMODIT-cie i udało mi się uzyskać taki efekt regułką w CSS.

**Mariusz Piotrzkowski:** Mateusz zasugerował, żebym to pokazał.

**Janusz Bossak:** Mi się podoba. Ja wszystkiego tak używam.

**Mariusz Piotrzkowski:** Mogę zmienić kontrast.

**Łukasz Bott:** Tu kontrast trzeba by bardziej ten...

**Janusz Bossak:** Są dwa tematy: jeden to kontrast/kwestie WCAG, ale tryb ciemny jako tryb ciemny jest OK.

**Piotr Buczkowski:** No to co zmieniłeś? Tylko tło?

**Anna Skupińska:** Jeszcze musiał zmienić kolory napisów.

**Mariusz Piotrzkowski:** Użyłem 3 filtrów. Najpierw kontrast (0.8, żeby nie było zbyt ciemne), następnie `invert` (żeby odwrócić kolory czarny/biały), a następnie `hue-rotate`, żeby anulować odwrócenie kolorów (żeby kolory nie były odwrócone).

**Anna Skupińska:** Sprytne.

**Mariusz Piotrzkowski:** Bo jeżeli nie, to jak robię `hue-rotate`, to się zmienia zielony na fioletowy. Jak zrobię `hue-rotate` na 180 stopni, to wraca do normalnych kolorów.

**Mariusz Piotrzkowski:** Na części Reactowej jest trochę gorzej, bo tam są inaczej zrobione style, ale mniej więcej widać jaki można by uzyskać efekt, gdyby trochę poprawić te tła wszystkim.

**Janusz Bossak:** Dobre, dobre. Warto pociągnąć temat. Podobają mi się takie jednoliniowe rozwiązania.

**Mariusz Piotrzkowski:** To taki eksperyment, ma sporo wad.

**Piotr Buczkowski:** Jak się przejdzie, to wszystkie pozycje zrobią się [nieczytelne?].

**Adrian Kotowski:** Wydaje mi się, że pasek Ci się nie odwrócił przypadkiem?

**Janusz Bossak:** Też na niego spojrzałem, czy on teraz czarny nie jest biały, a biały czarny?

**Mariusz Piotrzkowski:** Tak, odwrócił się. Dla paska można po prostu [wyłączyć filtr].

**Piotr Buczkowski:** Obrazki też zmienia?

**Janusz Bossak:** Aż mi się wierzyć nie chce.

**Mariusz Piotrzkowski:** Tak, wszystko zmienił. Musiałbym znowu zrobić odwrócenie w pasku.

**Janusz Bossak:** Weź wróć z powrotem.

**Mariusz Piotrzkowski:** To jest oryginalne.

**Piotr Buczkowski:** Dla `image` trzeba po prostu nie odwracać.

**Mariusz Piotrzkowski:** Tak, trzeba by zrobić po prostu inwerter.

**Janusz Bossak:** Markot (Mariusz Kot?).

**Adrian Kotowski:** Mi się jeszcze rzucił [w oczy] przykład z jakimś podglądem, np. dokument.

**Janusz Bossak:** Dobra, słuchaj, ja muszę kończyć, ale bardzo ciekawe to, co pokazałeś.

**Mariusz Piotrzkowski:** Trzeba by trochę z tym pokombinować.

**Piotr Buczkowski:** To format daty i czasu – tam jedno "d" trzeba poprawić. Nie wiem, czy tak zawsze jest?

**Mariusz Piotrzkowski:** Tak zawsze było, chyba nie pamiętam, żeby to kiedyś inaczej wyglądało.

**Piotr Buczkowski:** No to powinno być "dd".

**Janusz Bossak:** Ten układ czarny mi się bardzo podoba, ja bym go chciał na AMODIT-cie.

**Damian Kamiński:** Ja muszę uciekać. Dzięki.

**Łukasz Bott:** Dzięki.

**Janusz Bossak:** Ja też uciekam. Pod koniec dnia się spotkamy na dosłownie 15 minut, bo jutro mamy spotkanie i chciałbym wiedzieć, co już ustaliliśmy i co robimy. Wrzucam spotkanie na 16:00. Na razie dzięki.
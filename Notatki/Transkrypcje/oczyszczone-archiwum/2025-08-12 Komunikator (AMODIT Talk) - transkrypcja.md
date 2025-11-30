Data spotkania: **12 sierpnia 2025**

**Mateusz Kisiel**: Mechanizmu pobierania listy organizacji i na podstawie tego tworzenia już tych tabelek w odpowiednich bazach.

**Janusz Bossak**: Żeby nie powstał... Czy inaczej mówiąc: no kompletnie tego nie promujemy, w ogóle nie chwalimy się tym. To jest zrobione dla firmy i tylko w firmie pewnie to pozostanie.

**Mateusz Kisiel**: Znaczy ogólnie w wersjach on-premises to można dawać, tak? Tylko na chmurze trzeba by to przystosować jeszcze.

**Janusz Bossak**: Czy chodzi mi też o taką kompatybilność? To jak ludzie zaczną z tego korzystać? W takiej firmie powiedzmy, że im się to spodoba i tam będą setki już wiadomości, czatów i oni będą z tego korzystać. No i przyjdzie teraz aktualizacja za pół roku. To żeby nie było tak, że mamy wersję osobną dla firmy, którą musimy utrzymywać i osobną wersję dla ludzi, którzy mają to w chmurze czy nie wiem w Polfarmexie tu, czy gdzieś indziej.

**Mateusz Kisiel**: Nie, no prawdopodobnie to się skończy tak, że wtedy po tej aktualizacji, jak już zrobię tę wersję chmurową, będę musiał w niej pozmieniać konfigurację. Właściwie konfiguracja się trochę zmieni.

**Piotr Buczkowski**: No właśnie tak nie powinno być.

**Mateusz Kisiel**: Ale jakby wszystko....

**Janusz Bossak**: Znaczy boję się takich właśnie rozwiązań. Wiesz, połowicznych, że takie jest zrobione "coś na teraz". I o ile to nie chwyci i oni nie będą z tego korzystać, no to pół biedy, bo to tam wygaśnie. Za pół roku czy za rok stwierdzą, że to właściwie im nie było potrzebne i tylko tak się bardziej ofertowo czepiali, że to chcą. Ale jeżeli im się to spodoba....

**Janusz Bossak**: No i co wtedy, nie?

**Mateusz Kisiel**: Wiadomości żadnych nie stracą. W bazie, w tabelkach żadnych informacji nie stracą przy aktualizacji. No to myślę, że w jakimś tam URL-u, w jakiejś konfiguracji myślę sobie zmienić... Ale to jest kwestia, nie wiem, 10 minut przykładowo.

**Piotr Buczkowski**: Znaczy, teraz tak działa, że są dwie możliwe konfiguracje: albo konfiguracja lokalna (on-premises), albo chmurowa. Samochód (System) wykrywa tak, w której konfiguracji działa.

**Piotr Buczkowski**: Nic nie trzeba zmieniać, tak? Tak samo tutaj powinno być.

**Mateusz Kisiel**: No mogę Ci pokazać, jak wygląda konfiguracja. Obecnie nam się takie głównie bezpieczeństwem konfiguracje... Więc myślę, że... No ale tak, no może się uda zrobić bez tych zmian.

**Piotr Buczkowski**: Znaczy... I tak jak mówię w AMODIT jest tak, że sprawdza czy jest wpis do tabeli konfiguracyjnej bazy określającej listy organizacji chmurowych. Czy jest po prostu bezpośredni link do bazy danych? Czy to znaczy, że jest jedna baza danych? W zależności od tego... A tam jeszcze jak jest ta baza chmurowa, to jest jeszcze parametr, że powiedzmy adresy mają postać `*.amodit.com`, gdzie gwiazdka to jest identyfikator czy tam nazwa organizacji, w której pracujemy, na przykład Astrafox Test. Nie wiem, Velux, cokolwiek tam innego, tak?

**Mateusz Kisiel**: W tym momencie na przykład....

**Piotr Buczkowski**: A w `appsettings`?

**Mateusz Kisiel**: W tym momencie config zawiera w sobie Connection String do bazy danych, w której się zapisują te tabelki. No to docelowo w AMODIT może będzie to tak, że zamiast tego Connection Stringa, który bezpośrednio wskazuje....

**Piotr Buczkowski**: Znaczy, czy równie dobrze to może być Connection String do bazy istniejącej? Do bazy AMODIT, w której będą te tabele?

**Mateusz Kisiel**: O czym? No tak, tak... Tak jakby o to mi chodzi, że w tym momencie trzeba ustawić konkretnie Connection Stringa. W przypadku chmury będzie tak, że ten Connection String będzie się pobierał z tej bazy, którą tam pokazywałeś kiedyś.

**Piotr Buczkowski**: Czy nazwy kolumn w tabelach są zgodne z tą naszą konwencją AMODIT-ową, czy po prostu tak jak Entity Framework sobie zrobiło?

**Mateusz Kisiel**: To jest tak, że sam wybierałem nazwy kolumn. No i nie robiłem tych konwencji, to mogę w sumie zmienić nazwę. Chociaż no teraz już ciężko zmienić tę nazwę, to nie wiem czy jest sens. Możemy przyjąć/przygotować te trzy tabelki, będą oddzielnie po prostu w innej konwencji.

**Piotr Buczkowski**: Jak się te tabelki nazywają?

**Mateusz Kisiel**: Już Ci mówię. `ChatMessages`, `Chat` i `ChatUsers`. Ale one jeszcze nie są w AMODIT, to jest osobna baza. A, zaraz zobaczę... Nie są chyba już dodane w AMODIT 02. OK, ja zrobiłem chyba osobną bazę lokalną AMODIT 02 i nie są to tabelki obecnie.

**Piotr Buczkowski**: Jest jeszcze `LogUsers`?

**Mateusz Kisiel**: Tak, Logs to są jakieś strony...

**Piotr Buczkowski**: Migracje historii?

**Mateusz Kisiel**: Tak, to jest historia migracji, bo tutaj się Entity Framework... Inaczej zarządzanie migracjami. Uważam, że ten mechanizm jest lepszy.

**Piotr Buczkowski**: A po co jest tabela Users?

**Mateusz Kisiel**: Chciałem mieć kopię tych informacji o użytkownikach i w razie czego może jakieś dodatkowe informacje w tym wrzucić, ale być może ona nie będzie nam potrzebna, więc ja może nam to usunę. I też wszystkie te wiadomości są szyfrowane, tak? Czyli tam jak się podaje w bazie, to się tych wiadomości nie przeczyta. No bo taki też pomysł miał Damian, żeby wszystkie wiadomości zaszyfrować.

**Piotr Buczkowski**: Czym jest szyfrowany? Gdzie jest klucz?

**Mateusz Kisiel**: Klucz jest w pliku konfiguracyjnym. No i jeżeli będzie to jakaś wersja chmurowa, to albo trzeba go zaszyfrować wszystkich tym samym kluczem, albo dla każdego klienta innym kluczem, ale wtedy trzeba by w tej Twojej bazie dołożyć jeszcze kolumnę z kluczem tego klienta.

**Janusz Bossak**: No dobrze, jakoś tak zamarło. W którą stronę w końcu idziemy? Jak widzę, że w rozważaniu...

**Mateusz Kisiel**: Znaczy no mi się wydaje, że już nie ma co się cofać, bo teraz cofnięcie tego nowa... To jest praktycznie robienie od zera, więc wydaje mi się, że już lepiej to po prostu dokończyć.

**Piotr Buczkowski**: A jak to będzie działać?

**Mateusz Kisiel**: Ogólnie teraz zmieniłem już, że się nie wpisuje w backendzie tego serwisu URL-a do AMODIT-a, tylko jest ten URL w tym tokenie JWT. No i jak przychodzi, jak się klika ten przycisk w AMODIT-cie "Otwórz komunikator"...

**Piotr Buczkowski**: A po co? Dlaczego?

**Mateusz Kisiel**: Jeszcze raz: co po co?

**Piotr Buczkowski**: Po co wywołujesz AMODIT-a?

**Mateusz Kisiel**: Dlatego, no bo chcę już przystosowywać z grubsza do tej wersji chmurowej, żeby przynajmniej częściowo było bliżej tej wersji chmurowej. Tak? Żeby już nie trzeba było wpisywać jednego jakiegoś URL-a do AMODIT-a, skoro w przyszłości będzie też...

**Mateusz Kisiel**: Dlatego, no bo musi pobrać sobie ten serwis, na przykład listę użytkowników z AMODIT-a, więc musi jakby znać, o co pyta.

**Piotr Buczkowski**: Przez API pobierali użytkowników?

**Mateusz Kisiel**: Przez API. To jest tak samo, jak pobiera AMODIT sobie. Przez to chyba jakiś tam `UsersController`. Do tego samego kontrolera pobiera też ten serwis.

**Piotr Buczkowski**: Ale to musiałby się cookiesem zalogować.

**Mateusz Kisiel**: No i właśnie loguje się za pomocą tokena JWT. Zrobiłem specjalnie logowanie/uwierzytelnianie przez JWT w Auth.

**Piotr Buczkowski**: Dlaczego?

**Mateusz Kisiel**: No żeby można było z tych kontrolerów korzystać.

**Piotr Buczkowski**: A to nie lepiej tego REST API zewnętrznego można było użyć?

**Mateusz Kisiel**: Znaczy, on nie miał opcji pobrania listy użytkowników, chyba z tego co widać.

**Piotr Buczkowski**: To trzeba dodać, dodać pobieranie listy użytkowników do tego zewnętrznego.

**Mateusz Kisiel**: No ale ogólnie wydaje mi się, że korzystanie z tego JWT zamiast cookiesa jest bardziej takim nowoczesnym sposobem i [daje] więcej możliwości takich integracyjnych.

**Piotr Buczkowski**: Dobrze, to jest firma, tam jest logowanie Windows. Zapewniam Cię, że Integrated [Auth] to nie będzie działać.

**Mateusz Kisiel**: Znaczy, zrobiłem obsługę, że działa.

**Mateusz Kisiel**: W odpowiednich miejscach, w handlerach, w tym `Global.asax` zrobię obsługę tego.

**Piotr Buczkowski**: Czy dostęp anonimowy włączyłeś?

**Mateusz Kisiel**: Tak. Mm, no mogę Ci pokazać commit w tym, co zrobiłem.

**Janusz Bossak**: Taki jeden wniosek przysłuchując się tej dyskusji: ta dyskusja powinna się odbyć 3 tygodnie temu.

**Mateusz Kisiel**: Znaczy, ja zacząłem tydzień temu.

**Janusz Bossak**: No, czy... no to tydzień temu, tak. Także też tych prac aż tak dużo do cofnięcia nie ma, jeżeli to było tydzień temu, no bo to są prace z jednego tygodnia.

**Mateusz Kisiel**: No ale to serio dużo robiłem tego, więc [byłoby] taką szkodę...

**Janusz Bossak**: Wiem, wiem no. Chodzi mi o to, że powinien powstawać jednak dla takich rzeczy projekt. Ten projekt powinien przechodzić jakąś akceptację, porady architektów. No właśnie po to, żeby był właśnie zgodny z filozofią AMODIT-a, zgodny z potrzebą klienta i tak dalej. Głównie tą filozofią AMODIT-a w różnych kontekstach: i on-premisesowych i chmurowych. No bo trochę teraz tak stoimy, że tak powiem, przed faktem dokonanym, że zostało tak zrobione, taka technologia użyta. Takie rzeczy może i dobrze, może i nie, tak nie wiadomo. I teraz albo to akceptujemy, albo wywalamy do kosza i robimy jeszcze raz.

**Janusz Bossak**: Ja też bym się nie odważył, że tak powiem, projektować architektury, tylko zostawiam to Wam tutaj. No bo mogę powiedzieć, co ja od strony biznesowej sobie wyobrażam, ale jak to tam wewnętrznie bebechy mają być zrobione, to już jest po Waszej stronie.

**Mateusz Kisiel**: No jeśli chodzi o ten sam serwis tego komunikatora, to jest zrobione fajnie, w nowej technologii. Problem jest właśnie z integracją z AMODIT, tak? No bo to są już bardziej skomplikowane rzeczy.

**Janusz Bossak**: Proszę. Posiadanie tego jako osobnej aplikacji no może mieć też pewien wymiar marketingowy, aczkolwiek pewnie bardzo mały i słaby, bo my nie będziemy wchodzić na rynek komunikatorów. Nie będziemy rozwijać tego jako konkurencja do Teamsów, Slacka czy czegokolwiek innego. Więc jedyny argument jaki widzę, no to jest ten techniczny, że ten SignalR... to tam coś nie obciąża AMODIT-a. Ale to jest jedyna rzecz, która jest zaletą. Reszta jest wadą.

**Mateusz Kisiel**: Znaczy, no jeśli chodzi o jakieś przyszłe projekty, to można by już wykorzystać ten mechanizm, co powstał teraz. Bo jeżeli się teraz cofniemy, to już się go nie wykorzysta.

**Piotr Buczkowski**: Znaczy... Takie projekty jako oddzielne są fajne właśnie dla instalacji on-premises. Instalacje tej naszej chmurowej mogą być kłopotliwe.

**Mateusz Kisiel**: To chyba, że na razie tylko dla firmy to po prostu zrobimy, i dla chmury najwyżej w przyszłości się przebuduje.

**Janusz Bossak**: Podobnie było chyba, pamiętam, z e-Doręczeniami. Gdzie te klucze przechowywać? Nie, no chyba w e-Doręczeniach było tak, że na tym... w chmurze, w końcu w tym Key Vaulcie gdzieś te klucze umieszczaliśmy i tak dalej. A właśnie od początku trzeba myśleć o to, co mówi Piotr. Nie, że coraz więcej tych instalacji chmurowych i będzie to absolutny warunek "must have", że to musi działać i tak i tak – na chmurze i on-premisesowo. Znaczy wiesz, ja tutaj Mateusz nie mam do Ciebie jakichś tam może pretensji czy coś. I też co... Jeżeli nawet cofniemy ten projekt o tydzień, to też nie jest żaden jakiś tam problem. Czasami trzeba takie decyzje podjąć. No bo ważne jest to, co jest przed nami i ileś tam miesięcy i lat używania tego, versus tydzień robienia. Więc wolałbym zrobić drugą wersję, może inaczej trochę zaprojektowaną, z wykorzystaniem tych doświadczeń, które już przez ten tydzień nabyłeś. Ale żeby to było zgodne, a nie takie na siłę dopasowywane teraz do AMODIT-a.

**Mateusz Kisiel**: Moim zdaniem lepiej to działa, jak jest osobna aplikacja, ale no... Więc jest właśnie problem z jakąś chmurą, tak? Jest konfiguracja.

**Janusz Bossak**: No tak, tylko że wiesz, cała idea w tym, żeby to dobrze działało i na chmurze i on-premisesowo. No a nie jako... to nie jest... Znaczy nie robimy aplikacji w rozumieniu czegoś innego niż AMODIT. My robimy komunikator w AMODIT-cie. Technologia jest tutaj już wtórna. Komunikator nigdy przez nikogo nie zostanie użyty jako taki Teams, tak? Czy ktoś nie będzie miał AMODIT-a, a będzie sobie używał tego komunikatora? No nie, tak nie będzie to działało. To jest funkcjonalność. Tak jak Copilot jest funkcjonalnością AMODIT-a. Aczkolwiek bardziej Copilota bym wyobrażał sobie jako odrębną aplikację. Bo teoretycznie moglibyśmy go w przyszłości gdzieś tam na Dockerze/Azure na przykład postawić czy nawet na panelu, żeby gdzieś tam był i ktoś się mógł pytać. To już prędzej sobie wyobrażam takiego AMODIT Copilota jako taką właśnie aplikację, która gdzieś tam na backendzie korzysta z jakiejś bazy wiedzy takiej czy innej i odpowiada na jakieś pytania, niż ten komunikator, który jakby nie ma w ogóle racji bytu poza AMODIT-em.

**Kamil Dubaniowski**: Ja wręcz tak myślałem, czy ten Copilot nie powinien być jednym z użytkowników do czatu. Czyli wtedy łączymy Copilota z tym AMODIT Talkiem i jak chcesz pogadać z systemem, to wchodzisz tam, gdzie gadasz z ludźmi, tylko że odpowie sobie Copilotem. Żeby nie było znowu dwóch różnych miejsc.

**Janusz Bossak**: A to byłoby strasznie jakieś pomieszane. Wydaje mi się już...

**Kamil Dubaniowski**: Trochę tak jak było na Teamsach, gdzie mieliśmy tego Daily Bota. On tam coś do Ciebie pisał, czasami mogłeś coś tam sobie odpisać...

**Piotr Buczkowski**: To co wysłałeś mi się nie podoba. Czego tam `Display Generic`?

**Mateusz Kisiel**: No bo chcę wyświetlać nazwę użytkownika...

**Piotr Buczkowski**: Ale dlaczego czary? `CandidateIdentity`?

**Piotr Buczkowski**: To, co wysłałeś, jest w `Global.asax`?

**Piotr Buczkowski**: `CurrentPrincipal`... Przecież z tego powinno pobrać.

**Mateusz Kisiel**: Znaczy no plan był taki, że jeżeli jest podany ten Bearer Token w autoryzacji, no to sprawdzany jest czy jest poprawny, czy został wygenerowany przez AMODIT. Zgodnie z tym kluczem JWT. No i jeżeli jest to...

**Piotr Buczkowski**: Tutaj tego nie powinno być w ogóle, po co tutaj jest?

**Mateusz Kisiel**: A no dlatego, no bo potrzebujemy pobrać informacje o obecnym użytkowniku, tak? No i w niektórych...

**Piotr Buczkowski**: No to z kontekstu nie powinien pobrać?

**Mateusz Kisiel**: No nie ma w kontekście, tego nie ma w `HttpContext`. `Current` tego nie było.

**Piotr Buczkowski**: No tutaj nie możesz ustawić... Tutaj wstawiasz.

**Mateusz Kisiel**: No... Ale jest to dalej SignalR-em, więc musiałem w taki sposób zrobić. No ewentualnie może rzeczywiście da się jakoś ustawić, ale to nie widziałem jak.

**Piotr Buczkowski**: Na pewno się uda tam wstawić. Nie pamiętam gdzie to.

**Mateusz Kisiel**: Tak, no pewnie lepiej byłoby wstawić w `HttpContext`.

**Piotr Buczkowski**: Nie no... Tutaj powinna być zmiana. I też byłbym za tym, żeby sprawdzić czy mamy ten token i dopiero potem to wykonywać.

**Mateusz Kisiel**: To `GetTokenFromRequest` chyba go pobiera i sprawdza, czy jest w ogóle.

**Piotr Buczkowski**: Tworzysz obiekt... coś tam wywołuje w nim.

**Mateusz Kisiel**: Znaczy no tylko tworzę, żeby nie robić go statycznego, tak? Żeby nie było metod statycznych.

**Piotr Buczkowski**: Jedna wystarczyłaby, tak. Jedna metoda statyczna. Czy tam instancyjna... Może dlatego, że ja bym to inaczej zrobił.

**Mateusz Kisiel**: Znaczy no, być może jest miejsce do ulepszenia. Niezbyt... to trzeba jakoś jeszcze udoskonalić, ale to na razie wstępna wersja, która po prostu działa.

**Piotr Buczkowski**: Dobrze, więc się nie będę wypowiadał po takim krótkim przejrzeniu. Nie były już jakieś tokeny zrobione? Pamiętam, nie był jakiś token?

**Mateusz Kisiel**: Też nie korzystałem z tego REST API, które robiłeś, więc też nie do końca wiedziałem, co już mamy. Jak to działa, więc zrobiłem jakby od zera.

**Piotr Buczkowski**: Przecież REST API działa też...

**Mateusz Kisiel**: Ale to...

**Piotr Buczkowski**: Trzeba było ustawić jakieś konto... Jeszcze tego zaraz nie ma.

**Mateusz Kisiel**: Ale też tam generujesz właśnie taki OAuth token.

**Piotr Buczkowski**: No nie, nie, to działa... to jest dla użytkowników integracji zewnętrznych.

**Mateusz Kisiel**: OK.

**Piotr Buczkowski**: Czyli wpisujesz `ClientSecret`, tam podajesz, na podstawie tego generujesz token OAuth i się tym tokenem [logujesz].

**Mateusz Kisiel**: Znaczy no jakieś uwierzytelnianie trzeba było zrobić, tak? No po ciasteczku się nie dało, no bo były to różne domeny. I choćby nawet na developmencie to było ciężkie do zaimplementowania, żeby można było testować to lokalnie. Więc wydaje mi się, że takie JWT jest takie najbardziej zdaje się nowoczesne, standardowe.

**Piotr Buczkowski**: Dodać modyfikacji w `Web.config` nie ma?

**Mateusz Kisiel**: W poprzednim może jakimś commicie? Tam było kilka, możesz też zobaczyć mojego brancha `mateusz-dev`, tam są commity.

**Piotr Buczkowski**: Stąd, tak?

**Mateusz Kisiel**: Tak, na przykład jest CORS niżej.

**Piotr Buczkowski**: Możesz pokazać jak to działa? Używanie przez użytkownika tego?

**Mateusz Kisiel**: Mm, no dobra. Też w sumie mam opisane w Wordzie jak działa to logowanie.

**Piotr Buczkowski**: Możesz pokazać?

**Mateusz Kisiel**: No dobra, to [adres] `mateusz.amodit.local`. Tak? Jestem przez komunikator. Klikam go. I teraz tak... To już akurat byłem zalogowany, to się wyloguję pierwsze.

**Piotr Buczkowski**: Możesz w trybie incognito otworzyć?

**Mateusz Kisiel**: Dobra, to będzie najlepiej. Przekierowuję po tokena z AMODIT-a. A, tak w ogóle nie jest bezpieczne, nie ma HTTPS-a, to trzeba uznać. Przejdź. I tak to się dzieje, pierwsze się pobiera z tego lokalnego backendu jakieś tam informacje.

**Piotr Buczkowski**: To po stronie klienta jest przekierowanie jakieś?

**Mateusz Kisiel**: No to po kolei co się dzieje. Powiem: pierwsze co, sprawdzane jest to, że nie jesteśmy zalogowani. Skoro nie jesteśmy zalogowani, to jest przekierowanie robione, takie bardzo szybkie, ale nie było go tutaj widać. Nie mogę też tego [pokazać], bo to nie jest wysyłany request, to jest przekierowanie. Jest przekierowanie na AMODIT-a z ukośnikiem tam `JWT Login`. No i wtedy AMODIT generuje taki jednorazowy kod. No i ten kod jest następnie... jest przekierowanie z powrotem do `talk` (komunikatora) i ten jednorazowy kod jest dawany w Query Stringu. No i ten AMODIT Talk pobiera sobie ten kod i na podstawie tego kodu generuje token. I to jest już na przykład metoda `Generate`. No i ten generator wykonuje z AMODIT-a endpoint i przesyła mu ten kod jednorazowy. Tak, i na podstawie tego kodu wie, że skoro on wygenerował ten kod i jest poprawny, to generuje mu ten token JWT. No dalej już sobie korzysta z tego tokena. No i dzięki temu, że mamy ten pośredni krok z tym kodem, nie jest nigdy w adresie przekazywany ten token. Więc jak sobie ten kod podejrzy z adresu i spróbuje użyć, to już on będzie nieaktywny, bo to jednorazowy kod. No bo alternatywą jest podanie bezpośrednio takiego tokena w adresie, ale to jest gorsze, no bo taki token byłby dostępny te 15 minut czy ileś, więc lepiej tak nie robić.

**Piotr Buczkowski**: Widzę jeden problem. W farmie masz dwa serwery.

**Mateusz Kisiel**: OK. To jest w pamięci trzymane... No tak, to będzie problem. No to będzie trzeba... będzie trzeba w jakiejś bazie to zapisać, tak? Ten jednorazowy kod.

**Piotr Buczkowski**: Będzie przechowywany.

**Mateusz Kisiel**: Tak, no bo trzeba w jakimś wspólnym...

**Piotr Buczkowski**: W pamięci jest przechowywany, tak.

**Mateusz Kisiel**: W jakimś wspólnym cache'u... W tym momencie jest w pamięci, tak. Trzeba w jakimś wspólnym albo w bazie.

**Piotr Buczkowski**: Nie pamiętam jak się tam rozróżniają te serwery, bo to chodzi, że w farmie masz dwie domeny, tak? Starą i nową. Część ludzi pracuje na starej części, część na nowej.

**Mateusz Kisiel**: Tak, no ja rozumiem. Jak jest Load Balancer no to to się może trafić.

**Piotr Buczkowski**: Nie, nie, nie ma Load Balancera takiego, że load balansuje, rotuje na który serwer pójdziesz. Część ludzi używa starego serwera, część nowego. Są podłączeni do dwóch domen, mają dwa adresy, dwa różne DNS-y...

**Mateusz Kisiel**: Ale też właśnie myślałem, że trzeba by ten kod zapisywać w bazie, ale no na razie tak zrobiłem tymczasowo, jeszcze w pamięci, nie miałem na to czasu. Chciałem pierwsze już zrobić ten komunikator, żeby jakoś wstępnie działało. Ja właśnie w tym tygodniu planuję to zrobić w bazie.

**Piotr Buczkowski**: Dodać... Jest na to miejsce, tak. Jest takie coś jak przechowywanie, wysyłanie powiadomień, wysyłanie zaproszeń. I tam jest zapisywane, że wysłano zaproszenie na ten adres z tym kodem (z GUID).

**Mateusz Kisiel**: A jak się nazywa ta tabela?

**Piotr Buczkowski**: Nie pamiętam, ale jak weźmiesz listę użytkowników plus i zaprosisz użytkowników...

**Mateusz Kisiel**: `UserActivityLog` na przykład jest. Wydaje mi się Activity...

**Piotr Buczkowski**: Nie. Ale tam są różne rzeczy zapisywane, tak? Normalnie to jest sens tak, że ta osoba zaprosiła taką osobę.

**Mateusz Kisiel**: Znaczy no... Wyszukiwanie byłoby powiedzmy z jakimś filtrem, żeby sprawdzać tylko na przykład przez ostatnie 3 godziny. Więc też nie szukałoby jakoś dużo.

**Mateusz Kisiel**: To pytanie właśnie, jak to... czy kontynuować to dalej i robić osobną aplikację czy...

**Piotr Buczkowski**: Nigdzie indziej nie prosiłem... będzie używany.

**Mateusz Kisiel**: Znaczy pewnie tak, tylko no pytanie czy warto już mieć tam konfigurację gotową na jakieś przyszłe właśnie zewnętrzne aplikacje, które chcielibyśmy robić? Jak już się raz te szlaki przetrze, to już będzie nam łatwiej robić to w przyszłości.

**Mateusz Kisiel**: Taka cisza teraz.

**Piotr Buczkowski**: Nie wiem. Za mało czasu miałem, żeby to przemyśleć.

**Mateusz Kisiel**: Myślę, że można by na przykład jutro już jakieś spotkanie zrobić, przemyśleć to sobie i wtedy jeszcze [pogadać].

**Piotr Buczkowski**: No nie, musiałbym to zobaczyć, pobawić się tym. Nie to, że w czasie samego spotkania nic nie powiem więcej niż teraz.

**Mateusz Kisiel**: Myślę, że w razie czego mogę Ci podać linka do tego projektu, w którym jest ten Talk.

**Piotr Buczkowski**: To to jest tak w tym?

**Mateusz Kisiel**: Tak, tutaj.

**Piotr Buczkowski**: Dobrze, na razie nie ma chyba więcej, więc nie ma co więcej rozmawiać.

**Mateusz Kisiel**: To po prostu będę dalej kontynuował na razie to, co obecnie robię i potem najwyżej coś jutro jeszcze ustalimy.

**Piotr Buczkowski**: Dobrze, to kończmy.

**Mateusz Kisiel**: Dobra. No to cześć.

**Piotr Buczkowski**: Cześć.

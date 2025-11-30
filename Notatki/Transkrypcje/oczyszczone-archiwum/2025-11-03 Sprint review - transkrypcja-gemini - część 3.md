**Data spotkania:** 3 listopada 2025, 08:01 - część 3

---

**Damian Kaminski:** Przemka chyba z nami nie ma, więc nie wiem czy ty Kamil coś będziesz w jego imieniu jeszcze prezentował czy.

**Janusz Bossak:** Nie wiem czy.

**Kamil Dubaniowski:** Przemek w tym sprincie pracował nad widokiem stroną bazy wiedzy. Niestety nie ma go, więc nie pokażemy tego, bo on ma to lokalnie u siebie. Nie wiem czemu Przemka nie ma, jeszcze nie dawał sygnału.

**Damian Kaminski:** Ale to może podsumuj, że to też jest w sumie w powiązane z tym, co przed chwilą nie.

**Kamil Dubaniowski:** Jestem. Tak to jest związane głównie z seriami bezpieczeństwa, ponieważ ten frontend i wydajności zapewne też, frontend, który mieliśmy do tej pory dotyczący bazy wiedzy, mogę go w sumie pokazać. To też był pewien element. Koncept strona bazy wiedzy służy do zarządzania wiedzą wewnątrz organizacji, z której później Copilot może korzystać. Czyli każda firma może de facto prowadzić sobie swoją indywidualną bazę wiedzy. Mamy to podpięte na razie w takiej formie. Tak to jest strona napisana przez AI. Jest to dostępne tutaj w tym miejscu baza wiedzy. Przemek to przepisywał na nowo, tak, żeby to było spójne z naszym design systemem i żeby też było bezpieczne i wydajne, więc tą stronę przepisywaliśmy w tym spięcie i de facto ona ma schemat identyczny jak chociażby obszary, słowniki, źródła danych, klucze szyfrujące, więc mamy już szablon pod te kolejne strony, do której będzie potrzeba na napisanie backendu. Natomiast struktura tych wszystkich stron jest identyczna. Zaczęliśmy od tej, bo te są niby jeszcze w starej technologii, słowniki, fillm obszary i tak dalej. Ale pisane przez pod jakimś mocniejszym nadzorem terenu, natomiast to było tak robione przy użyciu AI i tam dłużej z tego co Mateusz mówił jego ingerencji w to nie było, weszło tak jak AI wyprodukować. Także Przemek to przepisywał w tym sprincie. Jak będzie Przemek w dalszej części to tego poproszę, żeby pokazał, jak się nie pojawi to wam wrzucę screeny, jak już się z nim złapią. Jak to wygląda aktualnie. No i w sumie dalsze prace nad edytorem formularza, natomiast tam podobnie na reagowaliśmy na zgłoszenia na braki. Nie zmieniamy tam już jakoś super tego widoku, jedynie co to potencjalnie wyrównujemy, jeśli o czymś zapomnieliśmy względem starego edytora bądź usprawniamy, patrząc na to, co dało się na liście, żeby ten edytor graficzny jednak też zachęcał do pracy i miał te same funkcjonalności, które mieliśmy na liście pól, ale tak jak mówię, to wygląd jest identyczny. Zmieniają się niuanse. Z takich rzeczy, które pamiętam z tego edytora graficznego, to między innymi doszedł właśnie też drag and drop sekcji, którego nie mieliśmy starym edytorze, a pojawił się w tym, czyli można łapiąc też sekcję. Zauważcie, że całość jest zwijana, żeby to było łatwiejsze do przesunięcia, czyli teraz przynosząc zegar całą sekcję przesyłają sobie do góry pola, ponownie się rozwijają w momencie kiedy już puszczam. Tak jak mówię, wyglądało tutaj różnice dużych nie zauważyć, natomiast pojawiają się poprawki i idealnie to jest chyba jedyna nowa rzecz, która weszła w ten weekend, drag and drop sekcji. O, tak to też się pojawiło. Tak, ja to wpisałem na listę zadań na ten sprint. Nie wiem, pokrótce mógłbym opowiadać co jest na ten sprint, ale jest sporo tematów, między innymi w tym edytorze też. Wyrównanie lista i edytor będą teraz mocno jeszcze eksploatowane w tym sprzęcie.

**Janusz Bossak:** Mam jakiś był temat, pamiętam szukania typów, to chyba jeszcze nie jest zrobione. Dobrze, co tam mamy jeszcze?

**Piotr Buczkowski:** Ja mogę nie wiem rozbudowane API pokazać trochę.

**Damian Kaminski:** Maku.

**Janusz Bossak:** Dobra.

**Piotr Buczkowski:** To już.

**Damian Kaminski:** Pojawiła się potrzeba przekazywania dużych plików. Tak?

**Piotr Buczkowski:** To może?

**Damian Kaminski:** To ja jeszcze zarysuje background, tak może. Do tej pory wgrywanie plików do AMODIT było możliwe, zarówno w ramach sprawy, jak i przez interfejs standardowo i tam maksymalna wielkość tego pliku była ustawiana w ustawieniach systemowych, natomiast tu pojawiła się potrzeba przekazywania z dedykowanego formularza przygotowanego przez Piotr akurat Węgla do AMODIT dużych plików, z kilkuset megowych czy nawet powyżej jednego giga i w związku z tym powstał nowy endpoint do właśnie przekazywania tego typu danych.

**Piotr Buczkowski:** Tak, przekazywania w inny sposób, nie poprzez JSON, gdzie właśnie duże pliki powodowały, że serializatory już nie były w stanie obsłużyć, także przez form data. Tutaj akurat do pola typu z plikiem, pedofil, starałem się SequelA wgrać.

**Daniel Reszka:** Ale jest jakieś ograniczenie, bo teraz mówicie, że mogą być jednogiglowe, ale gdzieś się ustawy jakieś górne ograniczenie.

**Piotr Buczkowski:** Tyle ile IIS jest, tyle ile jest IIS zdefiniowane. Bo to nie przechodzi żadnych, właśnie to jej serializacji, dodaj salon czy JSON i czy deserializacji JSON już nie, nie powinno być problemów. Przemoc to testowa, testowałem u siebie chyba na 500 megabajtach, to było 150.

**Daniel Reszka:** To jakbyście robili pod to dokumentację? Znaczy, chodzi mi o to, że jakbyście robili dokumentację, to żeby opisać, że jak gdzieś by nie przychodził plik, to żebyśmy wiedzieli gdzie szukać, już w przeszłości, że to jest IIS ustawione.

**Piotr Buczkowski:** Dlaczego to dokładnie to samo ustawienie co było do tej pory?

**Daniel Reszka:** Znaczy do tej pory.

**Piotr Buczkowski:** Przypnij przy plikach dodawanych. Stąd.

**Damian Kaminski:** Po prostu to jest to samo ograniczenie, tylko wcześniej w JSON nie dało się przekazać tu pliku równemu tej formie przekazywania plików.

**Piotr Buczkowski:** Bo to jest dokładnie to samo. Tak. Nie, nie, to znaczy wcześniej było inny sposób przekazywania, to znaczy więc interfejsu jest przekazywane od dawna przez form data. Zresztą opis zewnętrzny było przez JSON przez Base64. JSON za powodowała te problemy. Co mówiłem? Teraz też API też jest już możliwość do przekazywania przez form data, gdzie po prostu mamy... Teza jest, a ustawienia tak. A w sumie nie tutaj mogę pograć.

**Damian Kaminski:** Czy one są po prostu jednakowe dla całej witryny? Tak po prostu, Piotrze.

**Piotr Buczkowski:** I jest to tak dokładnie, tak?

**Daniel Reszka:** OK, a to jest ustawień systemowych, do czegoś w ogóle są w takim razie czy nie, bo jeszcze ustawienia IIS...

**Damian Kaminski:** Jak da się?

**Piotr Buczkowski:** Jeszcze raz. Jeszcze raz, nie zrozumiem.

**Daniel Reszka:** W ustawieniach systemowych AMODIT tam mamy też PDF maks. Jeszcze coś takiego.

**Piotr Buczkowski:** Nie, nie, nie ma czegoś takiego, to jest... Już moment.

**Damian Kaminski:** To jest max PDF jest coś takiego.

**Piotr Buczkowski:** To jest chodzi o obsługę plików. Nie pamiętam. To chodziło o, to był mechanizm ograniczania wielkości PDF, ograniczania liczby kolorów na skanie PDFów, żeby był mniejszy plik. I chodziło o to, że pliki o większym rozmiarze, no nie dało się dajnie obsłużyć. To tylko do tego mechanizmu.

**Damian Kaminski:** Znaczy.

**Daniel Reszka:** Czyli to nie ma nic wspólnego z wgrywaniem plików? Tak.

**Piotr Buczkowski:** Nie, nie, nie z wgrywaniem plików ma tylko... Czy to jest?

**Daniel Reszka:** A jest.

**Piotr Buczkowski:** Max request lęk, tam jeszcze jest drugi parametr opisany na wieki. Już nie pamiętam dzielnic. Tak, max request lęk jest. Jest jeszcze drugi parametr. Ale mówię, nie pamiętam w tej chwili, który to jest, ale jest napisany na wieki.

**Daniel Reszka:** OK, ale to jest jeden i ten sam parametr.

**Damian Kaminski:** Będziemy w tym kwartale jest plan, żeby uzupełnić tą dokumentację i właśnie tego typu. Było to jak teraz powinny być wyjaśnione, żebyśmy dobrze sami wszyscy rozumieli, co dany parametr oznacza. A jeszcze Piotr jakbyś mógł uzupełnić.

**Piotr Buczkowski:** Nie. Trzeba poprawić opis, bo to jest właśnie to.

**Damian Kaminski:** Tak, ale jakbyś mógł zapełnić jeszcze to funkcjonalność swoją, to teraz ten moment powinien to oczywiście wymaga obsługi dwukrotnego wywołania, żeby wczytać utworzyć sprawę powiedzmy i wczytać do niego dokument.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** Czyli już nie.

**Piotr Buczkowski:** Znaczy to decyzja programisty, czy wie, że ma na przykład pliki małe, tam nie wiem do kilkunastu megabajtów, gdzie możemy spokojnie jako jest serializować. Czytamy z Base64, umieścić w JSON i to przejdzie. Czy ma pliki duże, który nie przejdą przez JSON, musi przesłać właśnie jako form data.

**Damian Kaminski:** Wdrożenia WCA to jest zadanie.

**Piotr Buczkowski:** Programisty programującego tę aplikację wykorzystującego wykorzystującą nasze naszego API. Ale programisty nie od nas. Znaczy nie, nie działa. Może nie działa, nie działa AMODIT.

**Damian Kaminski:** No właśnie, ale czy to de facto wdrożeniowiec powinien ustalić zaopiekować? Mhm, OK. No dobra, to jeszcze chciałbyś coś dopowiedzieć innym zakresie?

**Piotr Buczkowski:** Znaczy, reszta to było poprawki, testy, poprawki czy tam drobne zmiany z tego, co robimy, może, ale to coś co przyda się testerka, jeżeli te stoją szczyty. Panie maili. Że. To był ten.

**Damian Kaminski:** Myślę, że serwisowi też może być to przydatne.

**Piotr Buczkowski:** Tak, czy jeżeli będzie takie coś, że dziś nie wczytał maila, to jest tam w logach original mail, co jest? Nie ma breakpointa. OK, musiałeś. Nie wiem dlaczego tak długo.

**Damian Kaminski:** A spróbuj teraz odświeżyć adres taki jak masz case creating.

**Piotr Buczkowski:** No dobrze coś.

**Damian Kaminski:** Nie działa, no to dopowiedz po prostu.

**Piotr Buczkowski:** Dobrze, można sobie wybrać publikę mail. Czytałem wczytany z nocy, jeżeli był w logu, że oryginalny mail. Coś mi wolno działa, powinno to być praktycznie od razu. Tutaj właśnie był problem w tej firmie ostatnio, że nazwa pliku była zawierała średnik i była zawinięta w 2 linii, więc nadto willing to jest znak średnika było źle. To panie to nie tam, przecież to co innego, ale.

**Damian Kaminski:** Dobrze chodzi w grubsze, z grubsza chodzi o to, że można za imitować to jak działa job, który ładuje.

**Piotr Buczkowski:** Tak. Czy też właśnie obsłużyć mail, który jest nie został wczytany prawidłowo przez usługę?

**Damian Kaminski:** Maile.

**Daniel Reszka:** Znaczy właśnie, bo to są 2 różne rzeczy. Chyba nie imituje. My tylko właśnie możemy maile zaczytać, bo to jest inaczej robione ręcznie, inaczej z usługi.

**Damian Kaminski:** Tak to. Nie wywołać, za imitować mam na myśli, tak, czyli trzeba mieć link.

**Piotr Buczkowski:** Znaczy tak, to tak naprawdę jest robiona ta wywołana dokładnie ta sama metoda, która jest wywoływana w jobie.

**Daniel Reszka:** Czyli log się odłoży load mail wtedy. Jak tak zrobimy?

**Piotr Buczkowski:** Nie, nie, nie wiem, bo to tylko ten plik, to to nie.

**Daniel Reszka:** No właśnie, czyli to nie jest dokładnie to samo. To jest tylko za przeczytanie tego maila ręcznie po prostu tak.

**Damian Kaminski:** No to samą metodą tylko.

**Piotr Buczkowski:** A nie, przepraszam, jeżeli chodzi o poziom, to tak jak najbardziej. Ale nie będzie wykonania, o to chodzi.

**Daniel Reszka:** No chyba nie będzie OK, ale log się odłoży, tak.

**Piotr Buczkowski:** Ale. Tak, tak.

**Daniel Reszka:** Jakby był jakiś błąd przy próbie właśnie tej wczytania nawet wręcz, no i tak.

**Piotr Buczkowski:** Tak, tak, tak.

**Daniel Reszka:** O to mi chodzi, OK, to to ma sens.

**Piotr Buczkowski:** Teraz.


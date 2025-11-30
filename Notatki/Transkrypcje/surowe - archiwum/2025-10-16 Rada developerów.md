**Transkrypcja**

16 października 2025, 08:01AM

**Marek Dziakowski** 0:35  
Dobra cecha, pogadamy o tym tym celu Janusz słynął.

**Piotr Buczkowski** 0:45  
Możemy gadać.

**Marek Dziakowski** 0:48  
Dobra no ogólnie.  
Pomysł sam w sobie bierze się od tego, żeby właśnie w presenter trzeba przerobić.  
Jedną funkcję wydzielić ją tu wczoraj też rozmawiałem z Mateuszem, bo on już ma jakby zrobione.  
Serwisy.  
W ramach tego ja i też może on pokazać zasadzie w sumie jak to wygląda strony samego zarządzania tymi serwisami.  
Żeby zobaczyć jakie są plusy, no bo.  
Jest w zasadzie bardzo dużo, żeby robić to w ten sposób.  
Na początku pewnie się to nie będzie aż tak różniło od jakiegoś tam lokalnego lokalne in lokalnych instancji, żeby tego nie robić przez chmurę, ale myślę, że z czasem. No tak jak wczoraj rozmawialiśmy, to jakieś skalowanie czy w ogóle ab date, no to wszystko jest dużo dużo prostsze i szybsze do zrobienia niż niżeli przy okazji tych lokalnych rozwiązań.

**Piotr Buczkowski** 1:54  
Czy dobrze to tylko rozróżnijmy to mówimy o jednej usłudze dla tras Center, gdzie teraz Center jest tylko u nas tak tylko na chmurze.  
Yy, to jest całkiem co innego, jeśli na przykład jakieś tam.  
Mikro serwisy do modlitwa działa modlić jest zainstalowany w kilkudziesięciu lokalizacjach u klientów, gdzie wielu przypadkach nie ma administratora nawet.

**Marek Dziakowski** 2:21  
Mhm, tak to jest na przykład.

**Piotr Buczkowski** 2:22  
I to wszystko musiałoby być robione rękami wdrożeń owców.  
Biegli nie są.  
Często.

**Marek Dziakowski** 2:31  
I tak też nawet jakbyśmy chcieli jakieś takie rozwiązania robić wspólne to to nie przejdzie, bo jaką ktoś ma na nam premię a modlitwa, no to zazwyczaj ruch jest tak ograniczony, że jest problem z czymkolwiek, więc no te.

**Piotr Buczkowski** 2:44  
Znaczy, że ktoś ma na premię, a młodzi tato, chcę mieć wszystko nam premię po pierwsze, tak.  
Związane z zawodem item no tutaj mamy na przykład czy teraz Center czy ocean, no to żeśmy ustalili tak, że jest to przez nas zawsze.

**Marek Dziakowski** 2:56  
Mhm.

**Piotr Buczkowski** 2:58  
Stąd tutaj możemy takie rozwiązania chmurowe typowo robić korzystające z in no za jakieś tam funkcjonalności azur.

**Adrian Kotowski** 3:08  
Ja jeszcze takie pytanie o te wydzielenie, jakbyś mógł ten Marek to trzeba wpisać, bo rozumiem, że najlepiej, bo jakby to, że tak będzie po prostu dzienne baseny serwisu, ale zakładam, że pewnie tutaj w tym przypadku nie będzie to łatwe.

**Piotr Buczkowski** 3:19  
Bo nie nie, nie, to jest tutaj mówimy o teraz Center.

**Marek Dziakowski** 3:20  
Nie, nie, nie.

**Adrian Kotowski** 3:23  
Tak właśnie, żeby dzielna baza, dlatego się ciemno tebel, bo tak to powinno być.

**Marek Dziakowski** 3:23  
To jest.

**Piotr Buczkowski** 3:26  
Gleb, ale po co? Nie? Nie, absolutnie nie.

**Marek Dziakowski** 3:27  
Już już ją może wytłumaczę po prostu może.

**Adrian Kotowski** 3:29  
To masz 4 zależność, to nie jest idealny microservices, ale no.

**Piotr Buczkowski** 3:33  
Bo tu chodzi o to, żeby część jedno zadanie, które była teraz robione.  
To jest podpisywanie dodawanie pliku do tego kraju, tak?  
To nie może być oddzielny plik skądś indziej.

**Marek Dziakowski** 3:46  
No nie, może musisz to samo ta sama bazę co jest?

**Piotr Buczkowski** 3:48  
Tu bardziej chodzi o to to wydzielenie do innego procesu. Tak nie jest Łeba o to chodzi.

**Marek Dziakowski** 3:54  
Tak był problem polega na tym, że aktualnie no te zadanie jest wykonywane przez 2 serwery webowe i one czasami się zdarza taka sytuacja, w którym debat komenty są dodawane jednocześnie i dodawane są do tego samego ostatniego bloku i po prostu jeden wisi.  
Po prostu wisi i nic nie do niego dalej już podłączane.  
No żeby to rozwiązać już kompleksowo. Właśnie do tego proponuję przejście wydzielenie tego tej funkcjonalności do do serwisu nie robienie jakiś tam obejść, blokad czy czegokolwiek, bo większej skali to się nie sprawdził po prostu, a skala teraz Center się z roku na rok drastycznie zmienia.

**Piotr Buczkowski** 4:35  
Znaczy, ale to i tak, skoro nawet nie będziemy robić blokad, to i tak będzie musiał być jeden jeden wątek tak po kolei robić.

**Marek Dziakowski** 4:42  
No tak, tak, no tak no zasada będzie taka, że po prostu.

**Piotr Buczkowski** 4:44  
No to skalowaniu nie ma mowy.

**Marek Dziakowski** 4:48  
Nie, nie, zasada będzie taka, że po prostu będzie kolejka serwerem będą zgłaszać do kolejki, żeby tak do dodać no i tyle jej jakiś tam worker będzie sobie to dodawał.

**Piotr Buczkowski** 4:54  
No tak to.  
Nie mów ma skalowaniu, bo to nie ma mowy ma skalowaniu wrażenie.

**Marek Dziakowski** 5:03  
Nie, nie w tej sytuacji. No rzeczywiście nie ma, chyba że.

**Piotr Buczkowski** 5:05  
Nie wiem jak jest odwrotność powiedzieć.

**Marek Dziakowski** 5:08  
Chyba żeby na przykład nie wiem, no ta kolejka była jakaś gigantyczna i ten worker, bo już nie wyrabiał jeden no to można by drugi dodać, który też to robił.

**Piotr Buczkowski** 5:14  
No ale nie możemy, bo musi być po kolei zgodnie z tym założeniem.

**Marek Dziakowski** 5:18  
No w zasadzie tak, ale to jakby sama.  
Chociaż no tak, musiałby tak czy siak czekać, no nie ma też sensu, nie nie, to musiał być jeden tak, tak, tak.

**Adrian Kotowski** 5:24  
Tylko musi być chroniczne obsługa tego tak no.

**Mateusz Kisiel** 5:24  
No tak, ale.  
Tak, ale ten jakby proces się zajmuje tylko i wyłącznie tym kolejkowanie NA wcześniej było tak, że zajmował się też całą witryną i musiał więcej rzeczy robić.  
Wydaje mi się, że są 2 przypadki z tego, co na początku Piotr mówił, że jest jeden przypadek, taki, że możemy sobie postawić jakiś microservices, który będzie wspólny dla wszystkich klientów, jak na przykład ten z jajem. Na drugi przypadek jest taki, że jak chcemy zrobić jakieś microservices, które być może będą per klient na przykład ten tok, ten komunikator, więc no w tym pierwszym to możemy sobie stawiać na azur, a w tym drugim trzeba bardziej się skupiać.

**Marek Dziakowski** 6:05  
No na przykład takie podejście jak zastosowałeś, czyli tą dekoloryzację do koloryzacji tych serwisów.

**Mateusz Kisiel** 6:09  
Tak no to mogę pokazać w tym jak to wygląda, bo to wygląda na dosyć.

**Marek Dziakowski** 6:11  
No to to jest o tyle fajne, że właśnie nie trzeba zmieniać nic praktycznie w kodzie, bo sobie po prostu tworzymy kontener z tego serwisu i wrzucamy sobie go do aszura. Jeżeli ktoś chce mieć to on premises się zgadza na to, żeby coś takiego utrzymywać, no to wtedy on sobie po prostu stawia dokkera lokalnie i i jest to samo w zasadzie.

**Mateusz Kisiel** 6:32  
Tak no tak naprawdę.  
Jeżeli chce się uruchomić te usługi, a ja ją jajowe czy w chmurze, czy gdzieś na naszym serwerze, no to jest tylko kwestia skopiowania jednego pliku docker compose i uruchomienia jednego polecenia.  
Doker composers, ap compose ap no i to automatycznie już tworzy wszystkie obrazy i kontenery i samą konfigurację załatwia tak jak chcemy.

**Piotr Buczkowski** 7:01  
I nic nie musiałeś robić, żeby tylko to było jedno polecenie zrobione jest tak.

**Mateusz Kisiel** 7:02  
Tak.  
Znaczy, nie chodzi mi o to, że chodzi mi o to, że wdrażanie tego jest bardzo proste, tak, że nie trzeba praktycznie żadnego jest to konfigurować się nic takiego.

**Lukasz Bott** 7:14  
Dobra Mateusza pytanie następujące.  
Ta sytuacja tak, no bo jeżeli to jest tutaj naszych murzy, no to my na to mamy wpływ tak.  
Ramy funkcję tą funkcjonalność.  
No to wtedy.  
Kiedy ten? No to my tym zarządzamy, powiedzmy, że robimy takiego dokkera, którego stawiamy lokalnie u klienta.

**Mateusz Kisiel** 7:36  
Mhm.

**Lukasz Bott** 7:36  
Bo to Marek rzucił hasło jest, że jeżeli klient się godzina, utrzymanie tego, no ale od czasu do czasu, no na przykład ten usługi jej oc. Niech będę tam przykład, nie pewnie te prąd ty modyfikujesz tak tutaj, jeżeli oni sobie wzięli w wersję.

**Piotr Buczkowski** 7:40  
Dziś znaczy.

**Lukasz Bott** 7:52  
Xd tak stan jakiś tam dzień tego dockera.  
No to jak jest potem aktualizacja aktualizacją takiego?

**Mateusz Kisiel** 7:58  
No dobra, to to mogę powiedzieć. To właśnie fajne jest to, że tak naprawdę nie musimy żadnych plików przesyłać, jeżeli chcemy gdzieś to wgrywać, to jedyne co potrzebujemy znać to nazwę obrazu. No jeżeli ktoś chce zrobić sobie, aby to po prostu abdykuje tego obraza ten obraz, no i ten obraz automatycznie się pobiera przez tok'ra, czyli powiedzmy, mogę zademonstrować.

**Lukasz Bott** 8:14  
Ale dobra, no to o k.

**Adrian Kotowski** 8:16  
Na przykład wersja.

**Piotr Buczkowski** 8:16  
Skąd się pobiera?  
Skąd się pobiera?

**Mateusz Kisiel** 8:18  
Powiedzmy tak, że zrobię jakąś zmianę w kodzie coś tej pozmieniałem sobie, no to teraz chce to jest aby ratować gdzieś tam na jakimś serwerze to robię docker compose.  
Mało tego jako bild.  
Minus minus pusz, ewentualnie też zrobiłem sobie polecenie deploy, które praktycznie robi to samo tylko jeszcze.

**Lukasz Bott** 8:33  
Dobra.

**Piotr Buczkowski** 8:37  
O jak jak fajnie hasło wszystkim udostępniłeś.

**Mateusz Kisiel** 8:41  
No trudno już.  
W każdym razie dobra, możemy możemy sobie łatwo to zdeprecjonować, no i w tym momencie.  
Obrazy, ok, możesz sobie włączyć włączyć do pokera?  
Obrazy, które tutaj są, czyli jeden obraz to jest.  
Auto Service ten do autentykacji drugi do jaja.  
Wgrywają się na chmurę, tam w mazurze jest taki rodzaj rodzaj rizo orsa o nazwie container.

**Adrian Kotowski** 9:17  
Incense.

**Mateusz Kisiel** 9:19  
Kontener register coś takiego? Tak no.  
No dobra, to Jeszcze raz uruchomię.

**Lukasz Bott** 9:25  
Dobre dobre nie ma to już, no może tak.

**Mateusz Kisiel** 9:27  
No tak, ale dobra to jakby wiesz w to.

**Piotr Buczkowski** 9:29  
To na mnie jest, nie mówię tak?

**Mateusz Kisiel** 9:30  
No dobra, ale to znaczy zarządzania tego od chmury powinna pokazać.

**Lukasz Bott** 9:31  
Dobra.  
Ale czekaj, to ja pomogłem podążę to jednak pytanie, bo tu mówisz o tej to mówisz, że wystarczy, że tam sobie do teraz aktualizują. Jeżeli to są zmiany w tym takim kodzie.

**Mateusz Kisiel** 9:38  
No.

**Lukasz Bott** 9:47  
Jego pytanie, czy ten doker na przykład?

**Mateusz Kisiel** 9:49  
No.

**Lukasz Bott** 9:50  
Trzyma jakieś dane powiedzmy doker zainstalowałem u klienta lokalnie i powiedzmy, że ten czy jakikolwiek te usługi aj no one się na czymś uczą, na przykład niech będzie ta baza wiedzy tak u klienta klient sobie buduje swoją bazę wiedzy, to pytanie czy te dane do tej bazy wiedzy jest otrzymane w tym do pokerze? W ramach tego ten, czy czy nie no bo chodzi mi o to, żeby wiesz, no bo jak sobie napiszę, bo w tej chwili jaka aktualizujemy amundi ta ta aktualizujemy no.

**Piotr Buczkowski** 9:54  
W bazie danych.

**Mateusz Kisiel** 9:56  
No.

**Lukasz Bott** 10:23  
Taką typową, a tylko część aplikacyjną tak no nie zmieniamy danych, które już są nie.

**Mateusz Kisiel** 10:23  
No nie, no jakby dane są zapisywane.  
No tak, dane są dalej w bazie danych, tak.  
Jakby my tylko zmieniamy tak samo jak teraz aktualizujemy. No nie, nie wpisujemy żadnych danych.

**Lukasz Bott** 10:35  
O k. Dobrze.  
Mnie no to dlatego dzięki to chciałem się upewnić, że doker sam z siebie jako takich danych.  
Danych klient ad czy danych z bazy amonit nie trzyma?

**Piotr Buczkowski** 10:45  
Musi musisz pamiętać, żeby tak było.  
Musisz pamiętać, żeby tak było, żeby nie zrobić czegoś, co co przechowuje lokalnie tak jakoś w jakiś sposób tak.

**Mateusz Kisiel** 10:56  
Znaczy na przykład jakieś tam?

**Piotr Buczkowski** 10:56  
To nie to, że to jest.  
Automatycznie tak zrobię, tylko musisz pamiętać, żeby tak robić.

**Mateusz Kisiel** 11:00  
Tak no jak jakieś obrazki może sobie trzymać jakby lokalnie tak możecie dobrać się do czegoś przydadzą w tej aplikacji.

**Piotr Buczkowski** 11:05  
Możesz robić jakieś pewnie pliki lokalni sobie zapisywać? Tak.  
Pokaże, tylko musisz pamiętać, że Nie możesz na nich.  
Dłuższy perspektywie polegać tak.

**Mateusz Kisiel** 11:18  
Co jest fajnego to mogę pokazać jak się tutaj na chmurze to obfituje, powiedzmy, że już się z aktualizował ten obraz, bo to widać już się wgrało i teraz to sobie wgrać nową wersję na chmurze. No to mogę sobie zmienić na przykład cokolwiek w jakiejś zmiennej środowiskowej na jakąś inną zrobić sejf ocenił revision.  
I w tym momencie.

**Piotr Buczkowski** 11:38  
Na produkcji to zmieniasz.

**Mateusz Kisiel** 11:40  
Tak to jest produkcja, ale właśnie fajne jest to, że nie ma żadnego przestoju.

**Piotr Buczkowski** 11:43  
To właśnie powoduje, że.

**Mateusz Kisiel** 11:47  
No właśnie właśnie nie powoduje.

**Piotr Buczkowski** 11:49  
Za łatwo to się robi dokładnie.

**Mateusz Kisiel** 11:51  
Bo zobacz, że zobaczy, że tak zobacz, że tak naprawdę stara instancja ciągle jest uruchomiona, jakby nie ma żadnego przestoju. To jest fajne, że.  
Powstaje nowy nowa instancja serwera, która się uruchamia, no i w czasie jak się ona uruchamia, ciągle stara jest w gotowości, obsługuje requesty.  
W pewnym momencie będzie chwila, gdy będą obie uruchomione. Otóż widać, że uruchomiła się nowa i teraz stara jest provisioning, czyli stara już schodzi.  
No i tak naprawdę nie było żadnego przestoju i to jest duża zaleta tego.  
No w a ja jeszcze też można tak jak coś.

**Piotr Buczkowski** 12:24  
A jak jak to co jak doker robi jakieś zadanie, które trwa pół godziny?

**Mateusz Kisiel** 12:30  
No to wtedy jest. Ogólnie to działa tak, że jeżeli jakiś request idzie, bo to to jest aplikacja webowa tak czyli obsługi jakieś questy i ten aż już sobie monitoruje ten questy i tak długo trzyma, bo w tym momencie są obie instancje uruchomione i tak długo trzyma stary masz wszystkie requesty z niej zejdą i jak zejdą z niej requesty to uruchamia się wtedy już tylko nowa stara schodzi.

**Adrian Kotowski** 12:53  
No to jaki był kontynuuje się. Myślałem, że to jest Center, bo to jak kontenery się windowsowym dzisiaj dostałem te te te swoje serwisy uruchamiasz.

**Piotr Buczkowski** 12:57  
Nie właśnie mieszamy te tematy.

**Mateusz Kisiel** 13:02  
Jeszcze Jeszcze raz co?

**Adrian Kotowski** 13:03  
Ale jakim kontynencie, jaki tam takich tam jest? Choć system operacyjny tych kontenerach, Linux, sol.

**Mateusz Kisiel** 13:11  
Możesz powtórzyć? Nie rozumiem ciebie?

**Adrian Kotowski** 13:12  
Jaki tam jest? Choć w sensie system operacyjny, jaki jest, jak jest?

**Mateusz Kisiel** 13:15  
Aha, no to to to, to możesz sobie zdefiniować w kontenerze tak, czyli w w obrazie w tym wypadku akurat mam linuxa.

**Adrian Kotowski** 13:22  
Że tak to nie ma po prostu jaki wybrałeś u nas w naszym przypadku też tak z ciekawości chciałem się.

**Mateusz Kisiel** 13:26  
To tak, no jak sobie zawiedziemy na doker fail to doker fajny jest zdefiniowane wszystko no w tym wypadku ja tej korzystam z mr c Microsoft net asp net no i to pod spodem ma linuxa z tego co kojarzę.

**Adrian Kotowski** 13:43  
Przecież można nie wybrać dla teraz Center, bo to znaczy jak ten kot wydzielin, bo teraz też jest to chyba chciałem coś napisane.

**Marek Dziakowski** 13:51  
Bo tak.

**Mateusz Kisiel** 13:52  
Ogólnie to jak mało jak chcemy korzystać z Windowsa, możemy jak chcemy, możemy z Linuksa. Ja tutaj korzystam z Linuksa, ponieważ mam też inne kontenery na linuksie i trzeba mieć jakby wszystkie, jak się lokalnie uruchamiać, trzymać wszystkie w tym samym rodzaju trzeba, bo wszystkie linuksowe albo wszystkie windowsowe.  
Ale nad morze tego problemu nie ma, więc tak może to dowolnie można.

**Adrian Kotowski** 14:11  
Tak.  
A propos tych kontenerach, czyli unię doktor composer też wydaje mi się, że lepiej od razu iść, ale to bardziej dojrzałe rozwiązanie i też no bardziej dostosowane do takich produkcyjnych już jakby instalacji, więc mi się wydaje, że po prostu.  
Mielibyśmy więc większe możliwości. To jest lepsza okres ochrony sekretów, też na przykład auto lecieli na przykład po jakimś tam jakieś awarii.

**Mateusz Kisiel** 14:29  
Znaczy.  
No można potem myśleć na przechodzenie na kubernetes, a myślę, że na razie tak prostszym rozwiązaniem jest doker i to praktycznie mi wystarczy do wszystkiego. Na przykład możemy też sobie łatwo tej zmieniać.  
Mocy tego serwera na przykład jest minimalna liczba repliki, maksymalna liczba replik, no i jak ekspert tej ustawie, na przykład 10. To będzie wtedy on w zależności od obciążenia zwiększą albo zmniejszą ilość serwerów, czyli będzie będzie robił automatyczne skalowanie, więc na przykład w nocy jak tam nikt nie korzysta, bo nie byłaby byłby jeden serwer, a jak się nagle pojawia jakoś dużo dużo zapytań w pewnym momencie to może sobie zrobić nawet 10 serwerów i do balancing prowadzić między innymi.  
To jest też fajne, no i też oczywiście można ustawiać, można ustawiać.

**Piotr Buczkowski** 15:24  
No ale trzeba oczywiście pamiętać, żeby tak zaprogramować, żeby to było, żeby to działało, tak.

**Mateusz Kisiel** 15:27  
Tak, no żeby.  
Tak tak, no żeby tam nie było jakiś tam rozbieżności w Kaliszu i tak dalej. No tutaj akurat w przypadku tego ja ja to praktycznie można zupełnie niezależnie puszczać jakieś nowe rzeczy, nie ma tam jakichś wspólnych wspólnych licznik a nic takiego.  
Mm też można sobie ustawiać łatwo ile ma pamięci jakieś tam moce, moce procesora?  
Mm.  
Coś myślałem.

**Piotr Buczkowski** 15:59  
Za.  
Łatwo się niektóre rzeczy robi.

**Mateusz Kisiel** 16:01  
No właśnie łatwo się robi. To jest wygodne i zaoszczędza dużo czasu uważam.

**Piotr Buczkowski** 16:03  
Zna łatwo, za łatwo można popsuć.

**Mateusz Kisiel** 16:09  
Br. Właśnie fajne jest to, że można sobie łatwo też przynosić nawet do jakiegoś innego aszura, bo z przypadku w przypadku wirtualnych maszyn to trzeba na nowo wszystko konfigurować ręcznie i to można można się pomylić przy tym.

**Piotr Buczkowski** 16:25  
Jak często takie rzeczy robimy?  
Nie no dobrze.

**Mateusz Kisiel** 16:30  
Też też też jeszcze inna rzecz jest fajna, że na przykład HTTPSA można łatwo konfigurować, bo zrobiłem aplikację na chaty TPI to jest coś takiego jak ingres, który automatycznie załatwia SAI. Jedyne co musiałem zrobić to od Łukasza poskrobko certyfikat, certyfikat na naszą domenę na nasz adres dns a wgrać żeby.  
Żeby była krótka, tak?  
No ale jakby polecam bardzo, bo to jest wygodne.

**Piotr Buczkowski** 17:01  
No ale to trzeba.  
Trzeba zaplanować, co możemy w tym, co możemy w tym zrobić. Tak, a czego nie.  
Nie to, że wszystko nagle mikro serwisy, bo nie nie da się.

**Mateusz Kisiel** 17:12  
Znaczy, no w tym momencie.

**Adrian Kotowski** 17:12  
A możesz pokazać jeszcze konfiguracji na przykład, bo tam wcześniej pokazywałeś to jest po prostu podawania poszczególnych kluczy konfiguracyjnych.

**Mateusz Kisiel** 17:20  
Aha, to tak, no to jakby jak to działa jak mamy jakieś jakąś aplikację zrobioną tym nowym świecie w tym kolorze?  
No to mamy zazwyczaj te pliki app settings kropka json i ona tutaj zawierają jakieś dane konfiguracyjne tak jakby te tego pliku nie ma w nie ma wyobraźnię do pokera, więc żeby to sobie skonfigurować na chmurze to to się podaje w zmiennych środowiskowych i jest taka konwencja, że.  
Zaraz settings.

**Adrian Kotowski** 17:51  
Podwójnie dwukropkiem jakoś tak chyba to.

**Mateusz Kisiel** 17:54  
Chyba 2 podkreśla wyniki z tego, co kojarzę są między.

**Adrian Kotowski** 17:57  
A dobro tak, że można podawać to tak.

**Mateusz Kisiel** 17:59  
Albo albo kropki zaraz zobaczymy.  
Tak no jakby powiedzmy, że chcę sobie coś wpisać w ażurowe jaja i od serki to jest ażur jaj o CRK, no to po prostu się oddziela. 2 podkreśla nikami i automatycznie automatycznie się nikt czarkowy sobie to do zczytuje w ten sposób.

**Adrian Kotowski** 18:27  
Z ciekawości, czy można wybrać? Na przykład jest wskazać, bo to sobie tego nigdy nie nie sprawdzałem.

**Mateusz Kisiel** 18:31  
Można.  
Można można na przykład w tym momencie nie wiem, czy mam to wpisane, ale.  
Mm.

**Adrian Kotowski** 18:39  
Spędziłem entry jakieś.

**Mateusz Kisiel** 18:40  
Akurat akurat dlatego dla tej instancji tego nie ma, ale gdzieś tak przed robiłam, że.

**Adrian Kotowski** 18:44  
Możesz rozwinąć jakiś ten pasek w sensie emanuela interesy? Tam jeszcze do wyboru, tak z ciekawości.

**Mateusz Kisiel** 18:48  
Tak jest jest referendum i można podać Reference do pracy i wtedy nie trzeba wpisywać. Na przykład jest modlitwa i ja i connection string to chyba to jest używane tutaj gdzieś z tego co mi się wydaje a tutaj jest connection string default connection jest Reference to Secret.

**Adrian Kotowski** 18:50  
K.  
Dobra, okej?  
Należałoby po prostu nie podawać tam 10 razy. Jakieś tam wpisałem, dobra, ok, to w porządku.

**Mateusz Kisiel** 19:11  
No i w tym momencie chodzą właśnie takie 3 micro serwisy ode mnie, czyli ten auto servis, a modlitwa i chroma Service, czyli ten od bazy wiedzy.  
No i mam też ten registry z tymi obrazami, Tomasz, moglibyśmy pokorzystać wszyscy powiedzmy na swe wspólnego registry, żeby łatwo tym obrazami zarządzać.

**Adrian Kotowski** 19:34  
Teraz zdaje się, masz po prostu 3 3 jakby to czy te rodziny obrazu w sensie te 3 mikro serwisy? Tak no.

**Mateusz Kisiel** 19:42  
Tak gdzieś tak powiem opisać jak się tej wejdzie w to.  
Identity.

**Adrian Kotowski** 19:52  
Grozi teraz do testów tych integracyjnych mamy ten nasz jakby od od premii słaby ten serwer ten do dokkera a dotyczy ten doktor HA tutaj na na.  
Tych produkcyjnych mikro serwisów mamy bardzo korzystamy z tego z rejestru mazurze.

**Mateusz Kisiel** 20:15  
Ody są wszystkie obrazy jakie są, czyli do tego rejestru też wrzucałem ten amok i tok, czyli te komunikatory, no i to jest też o tyle fajne, że można dawać uprawnienia uprawnienia, że na przykład ktoś ma uprawnienie tylko i wyłącznie do pobierania danych, a nie do wgrywania. Czyli zrobiłem taki taki klucz, że że można go będzie bezpiecznie podawać klientom, żeby sobie pobierali z tego rejestru amadi potok.  
I i nie będą w stanie nic to jej zepsuć, ponieważ nie mają uprawnień do wgrywania.

**Piotr Buczkowski** 20:48  
Jakoś wersjonowanie czy coś?

**Mateusz Kisiel** 20:52  
Wersjonowanie można zrobić czy tak w każdy ten obraz do kierowy jeszcze proszę pokażę, pokażę tutaj.  
Jak się buduje w docker compose musiał pokazać teraz.  
To jest to.  
No tutaj jest dobra jak się jak się buduje ten obraz to się podaje także.  
Także tak no i ten tak oznacza oznacza zazwyczaj wersję tego i domyśla się, nie podaje tego tagu to jest tak wpisywany lei test, ale może także z innymi tagami wygrywać.  
Na przykład jak się daje zrobić dwukropek i się wpisze jakąś się nie nazwę na przykład w wersji ja nie wiem fał i jeden kropka jeden no to będzie będzie wygrane Z TAGIEM jeden jeden i można sobie wtedy te.  
Te tagi łatwo zmieniać, tak.  
Tak samo jak sobie wejdzie na przykład jakąś.  
Ktoś ma jest quel ma jest quel doker.  
I tak samo sama się jakieś tak i tak jest tak 9 kropka 4 0 jest też jest też latest, akurat tego nie napisali.  
Jest też jest o k. No ten lajk jest jakby dla każdego domyślnie jak się nie podaje tagu.  
Więc no wersjonowanie można też łatwo załatwić, ewentualnie jeżeli ktoś mnie jeżeli ktoś chce mieć zawsze najnowszą wersję, to może po prostu wpisać sobie albo latest, albo nie podawać tego tagu.

**Piotr Buczkowski** 22:41  
No dobrze, ale mieliśmy z nim rozmawiać teraz senter, tak.

**Mateusz Kisiel** 22:45  
No dobra, tak w skrócie pokazałam jak to wygląda z tym doktorem.

**Piotr Buczkowski** 22:47  
Teraz to co ma zrobić Marek o, nie ma nic związanego z witryną webową, tak?

**Marek Dziakowski** 22:53  
Tak tutaj nie, nie, nie, to jakby chcemy, tylko po prostu utrzymać ten sam sposób, tak.

**Piotr Buczkowski** 22:53  
Czy ma być?  
Bardziej.

**Marek Dziakowski** 23:01  
Żeby nie było rozbieżności tylko trzymać, chociaż jeden kierunek mniej więcej, więc dlatego tutaj też Mateusz pokazuje jak to wygląda.

**Piotr Buczkowski** 23:08  
To jest całkiem co innego niż to, co pokazywał Mateusz tak.

**Mateusz Kisiel** 23:11  
To znaczy można to zrobić też tak samo w kontenerach docelowych i też o tym kontenera po uruchomić tak, by tak naprawdę nie ma potrzeby, żeby to była usługa webowa.

**Adrian Kotowski** 23:17  
Czy te?  
Że teraz na wiem, że robimy, bo się może troszkę szefowanie zrobić, wspólne był to gdyby był znaczy najlepiej jakby było najbardziej optymalnie, bo mamy teraz te to główne aplikacje, te wszystkie apki wbudowane w aplikacje bogu oraz mieliśmy teraz microservices, więc jakoś fajnie by to nie wiem czy ewentualnie pilnować tego określania. Po prostu w tym.

**Piotr Buczkowski** 23:36  
Podsłuch.

**Mateusz Kisiel** 23:39  
W przypadku a modlitwa jest ten problem, że tu klienta by trzeba było każdy kon premii sucha myć, ale na przykład takie.

**Piotr Buczkowski** 23:43  
Znaczy dobrze, ustalmy termin, ustalimy jeden temat rozmowy, mówimy o teraz Center, trzeba nam rodzicie.

**Adrian Kotowski** 23:44  
Tak, ale teraz to też nie mówimy jeszcze.

**Marek Dziakowski** 23:50  
Nie no mówmy już o teraz Center.

**Adrian Kotowski** 23:50  
Presenter ciągle.

**Mateusz Kisiel** 23:51  
O o. Ogólnie można mikro, mikro serwisach cenowo, bo takie wspólne testowanie takiej rangi jak by uruchomić dla microservices też był dobrym pomysłem.

**Piotr Buczkowski** 23:53  
No nie, nie, nie.

**Marek Dziakowski** 24:00  
Tylko, że tutaj będzie raczej tej w tej sytuacji będzie jeden.

**Piotr Buczkowski** 24:01  
Wiem, że zabawa jest fajna technologiami, ale myślmy sensownych.

**Marek Dziakowski** 24:08  
Taką tutaj, no będzie to jeden serwis, nie tego tego nie zyska. Polujemy tak samo tak jak Piotr mówię na początku, bo musi to być robione po kolei.

**Adrian Kotowski** 24:18  
Czy można to generalnie wyskalowane bać nie horyzontalnie tylko po prostu wertykalnie się po prostu więcej pamięci daje ci ramu takiej zasadzie?

**Marek Dziakowski** 24:19  
Przez jedną zamek.  
No no tak, no to tak jak.

**Piotr Buczkowski** 24:26  
Znaczy tutaj problem jest w tym, że musimy kolejkowa zadaniu także generować się po kolei.  
Nie możemy jednocześnie 2 zadań wykonać, bo się popsuje.

**Marek Dziakowski** 24:38  
Tak no ważna jest ta kolejność.  
Żeby ją zachować było inaczej, to nie ma sensu, więc tutaj no kolejka będzie trzymała kolejność, no po prostu no jeden jeden worker będzie mógł tylko przerabiać to.

**Piotr Buczkowski** 24:49  
No tak.

**Marek Dziakowski** 24:50  
No i i tyle. No to dlatego tak, no to co to co powiedział Adrian? No to też jest bardzo proste. W razie co, gdyby trzeba było dołączyć tam ze sobą serwerowych, no to w tym przykładzie Mateusza byłoby to dosyć proste.  
Raczej.

**Piotr Buczkowski** 25:08  
Będzie taka potrzeba.

**Marek Dziakowski** 25:10  
No właśnie nie wiem, nie wiem, ale lepiej się przygotować na wszelki wypadek niż potem myśleć nad tym.  
Zrobić sobie furtkę, żeby można było to zrobić.  
Prosto.  
No to ogólnie do piosenki no będzie jeszcze potrzebne ten sygnal r.  
Żeby w takie dosyć prosty sposób też sygnalizować się zwrotnie, że dawne.  
Pytanie zostało wykonane przy tej.

**Piotr Buczkowski** 25:34  
No i jak jak będzie to usługa notyfikowało trenerze zakończyła pracę nad tym czy będzie, czy.

**Marek Dziakowski** 25:43  
No będzie.

**Piotr Buczkowski** 25:44  
Czy po prostu oficyna musi sobie?  
Dynamicznie czy tam aktywnie sprawdzać?

**Marek Dziakowski** 25:51  
No nie chciałbym, żeby ona to opypy wała, bo bo to różnie może być tak jak w przypadku nie wiem większej ilości dokumentów tym to będzie mogło to trwać trochę więcej czasu, więc bez sensu, żeby to tak pytało czy tam raczej bym nie robił drugiej kolejki, zadaniami wykonywanymi tylko bym właśnie skorzystał z signal a.  
Proponowanego no są opcje.

**Piotr Buczkowski** 26:10  
Więc sygnal r. Gdzie sygnal RG?

**Marek Dziakowski** 26:14  
No jest opcja, jeżeli byśmy to robili, władze urzędu ażur udostępnia taką opcję jak si r serwis.

**Piotr Buczkowski** 26:19  
Ale kto będzie modyfikował ten sygnal r.

**Marek Dziakowski** 26:23  
Worker worker będzie zgłaszał, że dane z gus dane no dokument.

**Piotr Buczkowski** 26:27  
Czyli ta usługa dodająca do blockchaina? Tak?

**Marek Dziakowski** 26:29  
Tak, tak, on będzie zgłaszał, że się stało wykonują.

**Piotr Buczkowski** 26:31  
Czyli tak naprawdę witryna, witryna signal r. Naszej witrynie, przeglądarce signal będzie z innego serwera? Tak.

**Marek Dziakowski** 26:39  
Tak.

**Piotr Buczkowski** 26:42  
Da się tak.

**Marek Dziakowski** 26:43  
Wydaje mi się, że tak.

**Piotr Buczkowski** 26:45  
Czy pewnie jakieś korsy czy całość będzie potrzeba tak?

**Marek Dziakowski** 26:49  
No tak no tutaj, no trzeba będzie zrobić jeszcze tego, no że potwierdzić, bo tak to się nie robiliśmy, więc.  
Ale no tak, no moim zdaniem no jest to jest to opcja, żeby w ten sposób to zrobić po prostu.  
Mówię no można by kolejki robić też jako wtedy te serwery webowe mi się prosto pytały jedną stopniach kolejek no.

**Piotr Buczkowski** 27:11  
Nie, to nie wiem, ale będą też nie to już lepiej by było, że.

**Marek Dziakowski** 27:12  
Raczej no tak tak.

**Mateusz Kisiel** 27:13  
Znaczy.  
Znaczy te kolejki też nie są takie głupie, żeby się odczytywać.

**Piotr Buczkowski** 27:16  
W ogóle, że tak rezygnujemy z tego, że użytkownika użytkownikowi się pojawia automatycznie także podpisano po prostu jest, że to comment czeka na podpisanie. Sprawdź za chwilę, albo to i to, albo dostaniesz maila z informacją, że podpisane tak.

**Marek Dziakowski** 27:22  
A ewentualnie.  
Mhm.

**Piotr Buczkowski** 27:31  
Żeby Użytkownik ręcznie musimy nacisnąć przycisk tak, bo wiadomo, że nie będzie naciskał tak szybko, tak często jakby to robiło automat.

**Mateusz Kisiel** 27:31  
Znaczy.

**Marek Dziakowski** 27:39  
No tak tak.

**Mateusz Kisiel** 27:41  
Też wydaje mi się, że to podejście drugie, czyli żeby zamiast skorzystać z sygnal era wrzucać do jakiejś drugiej kolejki też nie jest złym pomysłem, bo to nie jest tak, że się odpytuje to co jakiś czas tylko jest ciągłe połączenie jakieś po tcp, no i dostaje też jakieś notyfikacje jak coś doszło do kolejki, więc wydaje mi się, że wydajnościowo niekoniecznie jest najgorsze rozwiązanie ma tą zaletę, że jak padnie serwer no to będzie dalej to w kolejce, więc jak się wydaje jak serwer wstanie będzie mógł sobie to wziąć tej kolejki.

**Piotr Buczkowski** 28:07  
I tak to jest w bazie danych, że czeka na podpisanie tak.

**Marek Dziakowski** 28:10  
No tak jak padnie to i tak sobie to najwyżej weźmie dane z bazy.

**Adrian Kotowski** 28:15  
Można ewentualnie jakimś kol wieku pomyśleć też wysyłać właśnie kolwiek do tego no nie wiem do tej głównej aplikacji, teraz to właśnie też kolejkowa być tak, że jakaś nie wiem.

**Piotr Buczkowski** 28:25  
No ale to musi trafić na odpowiedni serwer, tak?

**Marek Dziakowski** 28:28  
No tak, no to jest też problem, żeby to odpowiedniego serweru wróciło to.

**Piotr Buczkowski** 28:36  
Dobrze, według mnie koniecznie musimy wydzielić tak to podpisywaniu do oddzielnego procesu, bo to dawno powinno być zrobione. Ja nie wiem, najprostsze to jest po prostu zrobić usługę do osoby, która będzie działała na serwerze, bardziej skomplikowana jest zrobić ten microservices czy tam doker czy cokolwiek, który gdzieś tam będziesz tutaj działa o tak będzie.  
Co chwilę tam sprawdzał, czy ma coś w kolejce, jeżeli masz coś w kolejce, czyli w bazie danych tak dokumenty do podpisu do do podpisania do dodania do blockchaina to pobiera. Dodaj do blockchaina zapisuje informacje, że do do do blockchaina.  
A jakiś proces tak ewentualnie.  
Znaczy, no na przykład wysłałam maila tak, że dodany do blockchaina, a czy nawet użytkownikowi możemy na razie zrezygnować tak pierwszej wersji, że Użytkownik dostaje takie informacje? Proszę czekać na maila z informacją o podanie o do blockchaina, tak?  
Albo proszę tutaj odświeżyć status sobie ręcznie.  
Że dodanie sygnale a to ewentualnie drugi krok.  
Jak już będziemy mieli to w zielenia, tak?  
No to jest ważne.

**Adrian Kotowski** 29:50  
Myślałem jeszcze jakiś ten znajduje się na przykład iryd na przykład albo serwis bas, żeby tak dlatego komunikację można by też zresztą można kolejkowanie czy dlatego tak kolejkowanie wprowadzić gdzieś różne komponenty nie powiązać?

**Piotr Buczkowski** 30:00  
Co co sorry, bo nie zrozumiałem co co.

**Adrian Kotowski** 30:03  
I ten gryf albo Service bus można sobie ten definiować właśnie te eventy i taka lepsza forma komunikacji takim blokerem.

**Marek Dziakowski** 30:13  
No tak, no tutaj.

**Piotr Buczkowski** 30:14  
Znaczy tutaj w zasadzie nie nie jest potrzebna komunikacja, tak.  
Jest dodawany, jest dodawany wpis w bazie danych i ten ten wpis musi być obsłużony, tak.

**Adrian Kotowski** 30:19  
Właśnie to jest ten wątek, żeby jednak przekazywać informacje.  
To były bardziej uniwersalny jakby taki mechanizm, bo teraz mówimy, że ma być jeden microservices, który tam ma obsługiwać, wydziela do funkcjonalność. To można w przyszłości troszkę łatwo rozszerzyć tak, abyśmy mieli to wypady na przyszłość.  
Mieć pytanie, czy będziemy mieć jakieś?

**Piotr Buczkowski** 30:42  
Specyficzny przypadek, gdy gdzie mamy?  
Trasę do rejestru u nas tak to ma się dziać tylko u nas tylko na jednym serwerze to ma się dziać po kolei tak to to co mówiłem, że nie możemy na przykład współmierności zrobić.

**Adrian Kotowski** 30:57  
Mi chodzi o to, że inny funkcjonariusz trzeba będzie podzielić, to możesz z tego samego skorzystać, no bo teraz byśmy 2.

**Piotr Buczkowski** 31:01  
No ale to inna funkcjonalność nie będzie pasować do tego przykładu.

**Marek Dziakowski** 31:05  
Czy może pasować do samej koncepcji kolejki? Na przykład tym Basia no można różne kolejki tworzyć i jeżeli byśmy kiedyś chcieli jakość funkcjonalność tak w ten sposób zrobić, no to już by było.

**Piotr Buczkowski** 31:18  
Znaczy ja jakiś czas temu próbowałam kiedy ***** tak zrobić przez microservices przez kolejkowanie, no.  
Nie udało się.  
Bo kolejkowanie.

**Adrian Kotowski** 31:27  
Zdecydowanie proszę.

**Piotr Buczkowski** 31:30  
Znaczy ogólnie nie ma sensu na przykład przez te systemy kolejkowe przesyłać plików, bo to jest za duże, nie do tego to zostało zrobione.

**Marek Dziakowski** 31:36  
Za dużo tak.

**Adrian Kotowski** 31:38  
Ale myśmy wysyłali po prostu komunikaty, że też się udało. Nie byśmy nie wysłali do dużych do dużych treści. Jest to bardziej takie, żeby jakieś.

**Marek Dziakowski** 31:44  
No tylko że.

**Adrian Kotowski** 31:47  
Inicjować.

**Piotr Buczkowski** 31:48  
Ale.

**Adrian Kotowski** 31:50  
Że to, że się udało dokument dotyczył czym dodać, podpisać ci doradzić do glutenu?

**Piotr Buczkowski** 31:55  
No i co co zrobi z ta akcja?

**Adrian Kotowski** 31:58  
Również obsłużyć to wykrycie jakoś nie wiem sesję użytkownika po stronie, a aplikacji teraz Center i na przykład jakiś komunikat, nie wiem już wołać takiej sadzie.  
Znaczy mogę zbadać jeszcze, ale tak, ale też alternatywa, bo mówicie.

**Piotr Buczkowski** 32:16  
Ponieważ.

**Adrian Kotowski** 32:20  
Jako alternatywa sesji signal, a więc tak no to chciałem coś takiego zaproponować.

**Piotr Buczkowski** 32:25  
Ale to jest sygnal ries po to, żeby z przeglądała z przeglądarką gadać. Tak jest to, co tutaj alternatywy jakiś inny.

**Marek Dziakowski** 32:30  
Mhm.

**Adrian Kotowski** 32:33  
Ale chodzi o to, że był po stronie serwera na przykład tego teraz Center i.  
Nie przykład, mógłbyś jakoś to kolei to współpracować.

**Piotr Buczkowski** 32:40  
Po sygnale na serwerze.  
Sygnale arias do przeglądarki chyba tego te badania z przeglądarką tak że przeglądarka dostaje.

**Mateusz Kisiel** 32:48  
Czy serwery między sobą też trzeba ką?  
Serwery między sobą po sygnale czy też mogą się komunikować?

**Adrian Kotowski** 32:55  
Tak no 2 strony jest klient i serwer, tak więc tutaj można jakoś to ta spróbować powiązać.

**Piotr Buczkowski** 32:59  
Nie chodzi mi, że serwer do serwera czy jest sens?

**Adrian Kotowski** 33:03  
Układ jest sens igor era na przykład z rejestrowane po stronie serwera i można by też po stronie serwera powiem zerwać ten nowej wenty, które przychodzą właśnie na przykład informacje o tym, że jest.

**Piotr Buczkowski** 33:14  
Tutaj mamy tutaj mówimy o komunikacji, serwer, serwer przez sygnale r.  
Czy to ma sens?

**Adrian Kotowski** 33:19  
No tak, no ale też z tym mieć tyle do powiedzenia po stronie klienta.

**Piotr Buczkowski** 33:24  
No ale to mówimy o komunikacji, że ten microservices podpis dodający do odroczenia będzie notyfikowało serwer w w a serwer w wba notyfikować klienta przeglądarkę.

**Adrian Kotowski** 33:35  
Tak no można by to referencje przesyłać. No jak się tak jak to się nazywa indicator tej sesji właśnie singer, niektórzy nie zapachową, ale to można by przekazywać jakoś od tej strony to to do tego podejść.

**Piotr Buczkowski** 33:38  
Praca razem.

**Mateusz Kisiel** 33:48  
Znaczy, wydaje mi się to tak, trzeba mieć połączenie nawiązane, tak nie może sobie wysłać do klienta bez połączenia.

**Piotr Buczkowski** 33:53  
No właśnie ja.  
Tak, jeżeli widzisz jak to działa na przykład.  
Teraz tak to tam jest, cały czas wiszą tak ta sygnale coś tam connection tak jak seo, barker proces.

**Adrian Kotowski** 34:05  
To nie można po prostu liczyć tego tego połączenia, bo ty tego połączenia trwałego lat p.

**Piotr Buczkowski** 34:07  
Nie, nie, nie, nie.

**Mateusz Kisiel** 34:11  
Też też klient może mieć nawet nie mieć publicznego ip, żeby do niego się połączyć.

**Piotr Buczkowski** 34:16  
To jest tak, że właśnie klient się trzyma połączenie tak i to.

**Adrian Kotowski** 34:17  
Tunelowanie wtedy robione, żeby to to to działało.

**Piotr Buczkowski** 34:22  
Zwrotny idzie, czy najpierw klient musi nawiązać połączenie? Musieli otworzyć nadzór w stronę, żebyśmy mogli takie połączenie zarejestrować jakby taksi numer.

**Mateusz Kisiel** 34:33  
Jeszcze to można zobaczyć na te różne inne rodzaje tych kolejek, no bo na przykład do przesyłania plików co mówiłeś Piotr? Na przykład kawka jest dobra, chyba YouTube z tego korzysta, że między tymi kolejnymi etapami pro procesowania filmów właśnie w kawce wrzucaj do obsługuje.

**Piotr Buczkowski** 34:51  
Nie wiem, ja próbowałem rabbita tak to komunikaty tylko małe tak czyli takie coś, że powiedzmy mam plik w bazie danych wygeneruj mi z tego pliku.  
Yy pogląd i zapisz w tym miejscu, a ja sobie z tego miejsca gdzie zapisałeś pobiorę tak, ale broń boże, żeby to szło przez kolejkę te pliki.

**Mateusz Kisiel** 35:13  
No tak, to lepiej jakiś może link wrzucić wtedy czy coś?

**Piotr Buczkowski** 35:16  
No nie no.

**Marek Dziakowski** 35:17  
Nie no, dostęp do bazy.

**Piotr Buczkowski** 35:19  
Kolejka ma serwis, ma dostęp do tych samych.

**Mateusz Kisiel** 35:25  
Wieków.

**Piotr Buczkowski** 35:25  
Zasobów są.

**Mateusz Kisiel** 35:27  
Tak to zamiast.

**Piotr Buczkowski** 35:28  
Co witryna, czyli do do miejsca, gdzie jest są składowane pliki źródłowe do miejsca, gdzie są składowane pliki tym poglądów?  
Nie działa na tych samych, tak?  
Także komunikat przechodzi tylko, że polecenie wygenerowania podglądu albo odwrotnie, że pogląd gotowy tak.  
A nie to, że w legendary mi podgląd dla dlatego dlatego dla tej tablicy bajtów, a zwracam mi.  
Listę tablicy bajtów z podglądem tak.

**Mateusz Kisiel** 36:00  
No to jeżeli nie przesyłamy plików to można byłoby korzystać z tych kolejek czy nie. Czy taki był problem?

**Piotr Buczkowski** 36:05  
Można można tylko, że tam było do podglądu to nie był problem, ale do innych rzeczy były duży problem.  
Nie chciałem tylko do podglądu z tego robić.  
Tak było na przykład do wydzielania.  
Yy.

**Marek Dziakowski** 36:24  
Stron z.

**Piotr Buczkowski** 36:24  
Do celu tak do ceru miejscowego.  
Gdzie po prostu potrzebuję zwrócić?  
W sumie też by się dało, ale.  
Ponieważ to jest samo część młodej, to trzeba byłoby instalować klienta, to zrezygnowałam z tego.  
W międzyczasie g picture naprawił tak działanie podaja, Jestem także.  
Dokładnie działanie podaja, jesien podaja jesem jeżeli witryna jest na działy się ciałem.  
No tam to okazało się, że był problem.

**Mateusz Kisiel** 37:00  
Też tak.  
Ogólnie im więcej będziemy takich dodatkowych usług klientów, on premises instalować tym bardziej wydaje mi się, że dokker ma sens, bo wtedy można sobie jeden poleceniem w doker com pauzie wszystko zawrzeć i nie będzie trzeba instalować osoba tych rzeczy.

**Piotr Buczkowski** 37:15  
Lub mówiąc.  
U klientów często nie ma nawet żadnego administratora. Wszystkim się zajmują nasi konsultanci.  
Sen, że to była jak najprostsza.

**Mateusz Kisiel** 37:27  
Właśnie doker upraszcza znacznie wydaje mi się.

**Piotr Buczkowski** 37:30  
Nic nie uprości tego, że nagrywasz pliki?  
Podano jego zip.  
Bo musisz mieć infrastrukturę do tego, to myślę, że ją zainstalować.

**Mateusz Kisiel** 37:42  
Znaczy no trzeba tego zainstalować ten program, który tego doker obsługuje tak reszta to już wtedy postać jest.

**Piotr Buczkowski** 37:47  
Musisz skonfigurować połączenia sieciowe? Tak?

**Adrian Kotowski** 37:54  
No ja też w sumie no jak to też się Witam. Właśnie to podejście, bo dość starszym podejście też trzeba je instalować.

**Piotr Buczkowski** 37:56  
Są klienci, co mają wszystko na jednym serwer i baza danych i a modlić i usługę i witrynę.  
Nie możemy w to iść tak tylko, że no ktoś musi musiałby być.  
Się zajmować od nas instalacją klientów pewnie.

**Marek Dziakowski** 38:25  
No te instalacją klientów o modlitwę to jest jedna rzecz, no no teraz Center to jest już co innego.

**Piotr Buczkowski** 38:31  
Nie no tutaj mieszamy trochę tak tematy, no teraz Center to zadanie. Czy to zrobimy i na początku myślałam, że to po prostu jak najszybciej tak.

**Marek Dziakowski** 38:33  
Tak no.

**Piotr Buczkowski** 38:40  
Wydzielić do do dzielnej usługi, która działa na jednym serwerze, tak która sobie zapisuje na razie zrezygnować z tego powiadomienia dynamicznego o podpisanie odpisania o dodanie do blockchaina nie podpisaniem.  
Podpisanie to już wcześniej robione w inny sposób, tak?  
Pytanie, czy czy jeżeli 2 osoby naraz próbują podpisać też nie będzie problemu? Tak.  
Przed czy to jakaś blokowane jest to, że naraz 2 osoby nie mogą podpisywać jakieś dokumenty? Podpisy przez 2 osoby?

**Marek Dziakowski** 39:08  
Jestem prawie pewien, że to nie jest to obsłużą.

**Piotr Buczkowski** 39:12  
No to kolejny kolejny temat, bo.

**Marek Dziakowski** 39:12  
Ja się po prostu.  
No tak, no że tak, ale Jestem pewien, że to nie jest obsłużone, bo chyba nawet kiedyś Rafał i mówił o tym, że to chyba nie jest obsłużone i trzeba to obsłużyć.  
W jakiś sposób.

**Piotr Buczkowski** 39:26  
Według mnie pierwsze tak to jest w jakiś sposób wydzielenia tego dodawania do popcornu.  
Czy zrobienie tego microservices będą servis i microservices będzie szybkie? No to już Marek twoja decyzja.  
Jeżeli to zrobienie tego jakoś jako mikro, mikro serwis wiąże się z jakimiś kosztami, to trzeba najpierw ludzie zyskać akceptację tych kosztów.

**Marek Dziakowski** 39:51  
Tam były.

**Piotr Buczkowski** 39:52  
Znaczy utrz.  
Tak.

**Marek Dziakowski** 39:54  
Tak no tam dosyć małe te koszta były prawie że zerowe.

**Piotr Buczkowski** 39:58  
Ale trzeba najpierw.

**Marek Dziakowski** 40:00  
No tak tak, no tego chciałem Janusza.

**Piotr Buczkowski** 40:00  
Zyskać akceptację tych kosztów.

**Marek Dziakowski** 40:03  
Ale wysłałam ten dokument, żebym to przejrzał.

**Piotr Buczkowski** 40:05  
Pytanie, czy nie odpowiedział tak?

**Marek Dziakowski** 40:07  
No a jeszcze nie wiem. Wczoraj mówił mi, że dzisiaj będzie nic mi nie mówił, że jest jakiś redeco także.  
Dynamicznie się widzisz z nim, no wszystko.

**Piotr Buczkowski** 40:17  
Może by to omawiać dzisiaj to tak.

**Marek Dziakowski** 40:20  
Możliwe, ale wczoraj też z Łukaszem pod sklepu rozmawiałem, więc to mam powiedział, że tam zle monami trochę to skonsultuje czy oni w ogóle mieli coś takiego do czynienia, tam walnie jakieś dodatkowe informacje, że będzie.  
Wygląda.  
No myślę, że taki pot można by zrobić jakieś tam proste, że na razie bez komunikatów tylko po prostu wydzielenie. Zobaczcie kto wyjdzie jak będzie.

**Piotr Buczkowski** 40:38  
Nie dobrze.  
Jeżeli takie są problemy z tym.  
Chciałem powiedzieć jeszcze, byśmy się język blockchain, tak, to trzeba to podzielić tak koniecznych do niej szybciej.

**Marek Dziakowski** 41:03  
Myślę no ja bym to za pana, bo ona już kolejny spin, bo w tym też raczej nie ma sensu tak się nie zmieszcze numer no tak, tak no właśnie.

**Piotr Buczkowski** 41:09  
Tak teraz się kończy spędzić tak?  
To nie, no ale no na kolejne jak najbardziej.

**Marek Dziakowski** 41:17  
Dobra, no to.  
Po prostu może zróbmy tak, że spróbuję to zrobić, więc w ten sposób co jest co co robi tu Mateusz, żeby się podobnie.

**Piotr Buczkowski** 41:25  
Dlaczego Mateusz to mówię to jest chyba całkiem co innego, tak?

**Marek Dziakowski** 41:28  
Nie no.

**Piotr Buczkowski** 41:29  
Bo tutaj ma niezależni, ma nie nasłuchiwać na łebie tylko po prostu sobie działać tam w tle.

**Mateusz Kisiel** 41:34  
Znaczy, to nie ma znaczenia, to jakby to może on w ogóle nie korzystać z jakiś połączeń.

**Piotr Buczkowski** 41:35  
Sprawdzać.  
No tak, tak tak.

**Marek Dziakowski** 41:41  
No tak, tylko po to, żeby było to tokarze o to chodzi.

**Piotr Buczkowski** 41:45  
No tak tak.

**Adrian Kotowski** 41:45  
Jeszcze teraz wybaczcie przerwę wyszukałem, że można na przykład łatwo ten i ten wida powiązać z signor RN na przykład, że błąd razu środkowe udzielał odpowiedź do pewnego właśnie z serwisu rc. Myślę, że to też jest jakaś pomyśl.

**Piotr Buczkowski** 41:58  
Chcemy to jak najszybciej zrobić. Tak może zaczniemy od czegoś łatwiejszego.

**Adrian Kotowski** 42:00  
Ale to jest taka dość gotowe rozwiązanie. Generalnie jest takie.  
Żeby były to te przetwarzanie i tego tego dodanie do blockchaina i od razu byłeś komunikat, a to się wydaje w miarę takie no artykuł nawet na na na dokumentacji Microsoftu o tym jak to zrobić.

**Marek Dziakowski** 42:14  
No weź pokaż, podeślij jakąś.

**Adrian Kotowski** 42:17  
Na grupkę.  
Szybko znalazłem, może nie być.  
Dobra.

**Piotr Buczkowski** 42:25  
O czym mówię, zróbmy.  
Po kolei tak najpierw wydzielamy tego generowanym chaina do kolejki do jakiegoś oddzielnego procesu, które po kolei będzie to robił.

**Marek Dziakowski** 42:28  
To chyba to jest to dziecko?

**Piotr Buczkowski** 42:37  
Który zapewni nas, że nie będziemy psuć blockchaina? Tak, bo to jest największy problem.  
Ułatwienie dodatkowa komunikacja szybsze poinformowaniu użytkownika później.

**Marek Dziakowski** 42:43  
Znaczy no blockchain.  
To jest tak, że no blockchain się jako taką nie psuły, po prostu są dokumenty, które nie są jego częścią. Piszą także te dokumenty. Problem jest.

**Piotr Buczkowski** 42:59  
No.  
I cokolwiek tak, ale żeby nie była tak jej dokumentów.

**Marek Dziakowski** 43:07  
Tak, tak.  
No bo teraz skala się zwiększyła, no gdzieś tam sprawdzałem, to pół roku temu to było tam może ze 4 dokumenty czy tam 2 tak wiszące, no jak sprawdziłem to ostatnio to było ich ponad 50.

**Piotr Buczkowski** 43:23  
To no to w ciągu następnego sprintu musimy przejść na usługę, żeby nie było więcej tych dokumentów.

**Marek Dziakowski** 43:24  
No i to szybko rośnie widać.  
Mhm.

**Piotr Buczkowski** 43:31  
Możemy na na na moment ograniczyć tak funkcjonalność czas Center właśnie z tych powiadomień, responsywność, no jest to konieczne, tak jak najszybciej musimy zrobić pierwszy krok, czyli wydzielić to usługi.  
Nawet ograniczając funkcjonalność, tak.

**Marek Dziakowski** 43:53  
No k.  
Myślę, że tak można tu podsumować.

**Piotr Buczkowski** 43:57  
Później będziemy mogli rozbudowywać. To jest tak, jak będzie zapotrzebowanie.

**Marek Dziakowski** 44:03  
No tak, myślę, że rozbudowa to w przyszłości nie będzie jakoś.

**Piotr Buczkowski** 44:09  
Nawet jak to będzie przyniesienie do jednego typu dokkera czy tam cabernet, a czy coś to, ale już będziemy mieli tak.  
Wydzielony już teraz nie będziemy psuć jakiś kolejnych plików.  
Dobrze.  
To tyle czy coś jeszcze?

**Marek Dziakowski** 44:30  
No ode mnie to tyle.

**Lukasz Bott** 44:33  
To chyba tyle tak, a nie ten nasz temat to, no to wiemy co mamy tak co robić. Ten generalnie koncepcja jest taka, żeby to te źródła. Generalnie tak te źródła systemowe, bo to z nimi jest tam problem z tymi ujemnymi identyfikatorami.

**Anna Skupinska** 44:41  
Tak omawialiśmy do wczoraj.

**Lukasz Bott** 44:52  
Będą teraz dodatnimi identyfikatorami tak i z buildem, więc będzie można je łatwo.  
Część dotychczasowe źródła, które mają ten.  
Ziemny gui tym to po prostu pozostaną tak, no i z czasem jej się po prostu sukcesywnie albo zamieni, albo po prostu zostawi tak, żeby.  
Nie wróciły to, co się będzie wymagało zmiany jakieś tak, no to z pewnością wszystkie te miejsca, głównie w module raport owym.  
Więc korzystamy z źródeł.  
Systemowych, tutaj ania jeszcze jedno mi wpadło Odnośnik do źródła.  
Nosimy pole typu Odnośnik do źródła danych, totalnie jeszcze ewentualnie tak trzeba będzie zmienić po prostu sposób. Jeżeli ktoś się odwołuje do zewnętrznego źródła danych tego systemowego, tak, no to żeby.  
Już się odwoływał do do tych źródeł, które mają właśnie ten guid i dodatni.  
Identyfikator.

**Anna Skupinska** 45:57  
Chodzi o to, żeby zmienić, żeby już odwołanie się do źródła to było przez bujny.

**Lukasz Bott** 46:04  
To znaczy, nie, nie chodzi mi o to. Chodzi mi o to, że.

**Anna Skupinska** 46:04  
No nie.

**Lukasz Bott** 46:08  
Że żeby chodzi mi tylko o to, że w tych miejscach, o których wymieniłem gdzieś tam, no po prostu musimy zmienić to tak, jeżeli zmienimy teraz to zabrać źródła, to zewnętrzne tak te źródła danych systemowe, raz, że będą odpowiedni tam oznaczone jako systemowe będą miały dodatni identyfikatory i guide. No to już po prostu, żeby pamiętać o tych kilku miejscach tak gdzie, gdzie gdzie to występuje? Tak gdzie to zagadnienie występuje, żeby właśnie tam pobierać, bo rozumiem, że to, że frontend to jest front end, on bierze z jakiegoś backendu, więc po stronie backendu trzeba tak.  
Zapewnić, że.

**Anna Skupinska** 46:43  
E tak, to głównie praca postowania weekendu oczywiście.

**Lukasz Bott** 46:47  
No dokładnie, więc zmiany tam w tych wszystkich miejscach, gdzie jest odwołanie do źródeł danych systemowych po ujemnych indeksach. No trzeba być zrobić tak, żeby obsługiwały teraz ten dodatnie indeksy. Tak, no bo rozumiem, że guild ci będą potrzebne do tylko do tak jakby do synchronizacji, tak w sensie do przenoszenia między środowiskami tak jakimś tam testowy ma docelowe.

**Anna Skupinska** 47:14  
Mhm.  
Wykładnie.

**Lukasz Bott** 47:18  
Dobry taktu.  
Wymyślony.

**Anna Skupinska** 47:23  
Chcielibyście jakieś szczegóły?  
No jak nie no to.

**Lukasz Bott** 47:29  
Nie mieliście to, jak będziemy się zabierali za to tak, no to jeszcze ewentualnie to to przedyskutowanie.

**Anna Skupinska** 47:35  
Tak na pewno dojdą 2 dia nowe 2 nowe kolumny, czyli czy jest systemowe źródło i czy jaki magu it i zastanawiam się, czy wszystkim źródłem generować guide tylko tym, które są systemowe?

**Lukasz Bott** 47:49  
Wiesz co no?  
Na wszelki wypadek.

**Anna Skupinska** 47:53  
Podobnie zdasz burdami, żeby wszystkie miały bujdy.  
Na razie zrobiłam tak, że tylko systemowe mają.

**Lukasz Bott** 47:58  
No i czyli tak jak jej, jeżeli nawet tego liderów na razie do czegokolwiek nie będziemy używali, to to tak.

**Anna Skupinska** 48:07  
A zrobisz, żeby wszystkie te sporty?  
Miały wójt i.  
Dalej.  
A ja też mieć koryta.

**Lukasz Bott** 48:25  
Bo to, bo to anusz się później, może przyda właśnie do jakichś mechanizmów eksportu importu w postaci definicji, na przykład źródeł czy dashboard ów poprzez poprzez pliki tak no, poprzez interfejs, bo bo w tej chwili nie ma takiej możliwości, tak ja sobie skonfigurowałem źródło danych na przykład w jednym środowisku i chciałbym je przenieść na inne środowisko. Oczywiście na tym docelowym środowisko to może będę musiał zaktualizować na przykład connection string tak.  
Jakiś, ale, ale co do zasady, no to reszta nie wiem. Zapytanie jest kulowe czy coś w tym stylu opis nazwa ten no mi się nie zmienia, tak.

**Anna Skupinska** 49:05  
Dokładnie.

**Lukasz Bott** 49:10  
Dobra, to tyle, dobra.

**Anna Skupinska** 49:11  
A to, że się przydadzą coś innego o k.

**Lukasz Bott** 49:13  
Dobra, dzięki za spotkanie.  
Cześć.

**Mateusz Kisiel** 49:18  
Cześć.

**Anna Skupinska** 49:18  
No cześć.

**Marek Dziakowski** 49:18  
Część.

**Adrian Kotowski** 49:20  
I cześć.

zatrzymano transkrypcję
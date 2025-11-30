**Data spotkania:** 16 października 2025, 08:01

---

**Marek Dziakowski:** Dobra, czekaj, pogadamy o tym – tym celu Janusz słynął.

**Piotr Buczkowski:** Możemy gadać.

**Marek Dziakowski:** Dobra. Pomysł sam w sobie bierze się od tego, żeby właśnie w TrustCenter trzeba przerobić jedną funkcję, wydzielić ją. Tu wczoraj też rozmawiałem z Mateuszem, bo on już ma jakby zrobione serwisy. W ramach tego ja też może on pokazać – zasadzie, w sumie, jak to wygląda ze strony samego zarządzania tymi serwisami. Żeby zobaczyć, jakie są plusy, no bo jest w zasadzie bardzo dużo, żeby robić to w ten sposób. Na początku pewnie się to nie będzie aż tak różniło od jakiegoś tam lokalnego, lokalnych instancji, żeby tego nie robić przez chmurę, ale myślę, że z czasem – tak jak wczoraj rozmawialiśmy – to jakieś skalowanie czy w ogóle update, to wszystko jest dużo prostsze i szybsze do zrobienia niż przy okazji tych lokalnych rozwiązań.

**Piotr Buczkowski:** Czy dobrze to? Tylko rozróżnijmy, to mówimy o jednej usłudze dla TrustCenter, gdzie TrustCenter jest tylko u nas, tak, tylko na chmurze. To jest całkiem co innego, jeśli na przykład jakieś tam microservices do AMODIT – AMODIT jest zainstalowany w kilkudziesięciu lokalizacjach u klientów, gdzie w wielu przypadkach nie ma nawet administratora.

**Marek Dziakowski:** Mhm, tak, to jest na przykład.

**Piotr Buczkowski:** I to wszystko musiałoby być robione rękami wdrożeniowców. Bo nie są często.

**Marek Dziakowski:** I tak też, nawet jakbyśmy chcieli jakieś takie rozwiązania robić wspólne, to to nie przejdzie, bo jaką ktoś ma on-premise AMODIT, no to zazwyczaj ruch jest tak ograniczony, że jest problem z czymkolwiek, więc te.

**Piotr Buczkowski:** Znaczy, ktoś ma on-premise AMODIT, chce mieć wszystko on-premise po pierwsze, tak. Związane z bezpieczeństwem IT. No tutaj mamy na przykład czy TrustCenter, czy OCR, no to ustaliliśmy tak, że jest to przez nas zawsze.

**Marek Dziakowski:** Mhm.

**Piotr Buczkowski:** Stąd tutaj możemy takie rozwiązania chmurowe typowo robić, korzystające z Azure – jakieś tam funkcjonalności Azure.

**Adrian Kotowski:** Ja jeszcze takie pytanie o to wydzielenie. Jakbyś mógł, ten Marek, to trzeba wypisać, bo rozumiem, że najlepiej, bo jakby to – że tak będzie po prostu dzielna baza nowego serwisu, ale zakładam, że pewnie tutaj w tym przypadku nie będzie to łatwe.

**Piotr Buczkowski:** Bo nie, nie, nie, to jest – tutaj mówimy o TrustCenter.

**Marek Dziakowski:** Nie, nie, nie.

**Adrian Kotowski:** Tak właśnie, żeby dzielna baza, dlatego się pytam o tabele, bo tak to powinno być.

**Marek Dziakowski:** To jest.

**Piotr Buczkowski:** Tabele, ale po co? Nie? Nie, absolutnie nie.

**Marek Dziakowski:** Już, już, ja może wytłumaczę po prostu, może.

**Adrian Kotowski:** To masz tę zależność, to nie jest idealny microservices, ale no.

**Piotr Buczkowski:** Bo tu chodzi o to, żeby część – jedno zadanie, które było teraz robione. To jest podpisywanie, dodawanie pliku do tego kraju, tak? To nie może być oddzielny plik skądś indziej.

**Marek Dziakowski:** No nie, może musi to – ta sama baza, co jest.

**Piotr Buczkowski:** Tu bardziej chodzi o to, to wydzielenie do innego procesu. Tak, nie jest – tabela, o to chodzi.

**Marek Dziakowski:** Tak. Problem polega na tym, że aktualnie to zadanie jest wykonywane przez 2 serwery webowe i one – czasami się zdarza taka sytuacja, w której dokumenty są dodawane jednocześnie i dodawane są do tego samego ostatniego bloku i po prostu jeden wisi. Po prostu wisi i nic nie jest do niego dalej już podłączane. Żeby to rozwiązać już kompleksowo, właśnie do tego proponuję przejście – wydzielenie tego, tej funkcjonalności do serwisu. Nie robienie jakichś tam obejść, blokad czy czegokolwiek, bo na większej skali to się nie sprawdziło po prostu, a skala TrustCenter się z roku na rok drastycznie zmienia.

**Piotr Buczkowski:** Znaczy, ale to i tak, skoro nawet nie będziemy robić blokad, to i tak będzie musiał być jeden wątek, tak, po kolei robić.

**Marek Dziakowski:** No tak, tak, no tak. Zasada będzie taka, że po prostu.

**Piotr Buczkowski:** No to o skalowaniu nie ma mowy.

**Marek Dziakowski:** Nie, nie. Zasada będzie taka, że po prostu będzie kolejka. Serwery będą zgłaszać do kolejki, żeby tak dodać, no i tyle. Jakiś tam worker będzie sobie to dodawał.

**Piotr Buczkowski:** No tak, to nie mów o skalowaniu, bo to nie ma mowy o skalowaniu – w żaden sposób.

**Marek Dziakowski:** Nie, nie, w tej sytuacji. No rzeczywiście nie ma, chyba że.

**Piotr Buczkowski:** Nie wiem, jak jest – odwrotność powiedzieć.

**Marek Dziakowski:** Chyba, żeby na przykład nie wiem, ta kolejka była jakaś gigantyczna i ten worker już nie wyrabiał – jeden, no to można by drugi dodać, który też to robił.

**Piotr Buczkowski:** No ale nie możemy, bo musi być po kolei zgodnie z tym założeniem.

**Marek Dziakowski:** No w zasadzie tak, ale to jakby sama. Chociaż, no tak, musiałby tak czy siak czekać. No nie ma też sensu, nie, nie, to musi być jeden, tak, tak, tak.

**Adrian Kotowski:** Tylko musi być chroniczna obsługa tego, tak.

**Mateusz Kisiel:** No tak, ale. Tak, ale ten jakby proces się zajmuje tylko i wyłącznie tym kolejkowaniem. Wcześniej było tak, że zajmował się też całą witryną i musiał więcej rzeczy robić. Wydaje mi się, że są 2 przypadki z tego, co na początku Piotr mówił, że jest jeden przypadek taki, że możemy sobie postawić jakiś microservices, który będzie wspólny dla wszystkich klientów, jak na przykład ten z AI. Drugi przypadek jest taki, że jak chcemy zrobić jakieś microservices, które być może będą per klient – na przykład ten Talk, ten komunikator – więc w tym pierwszym to możemy sobie stawiać na Azure, a w tym drugim trzeba bardziej się skupiać.

**Marek Dziakowski:** No, na przykład takie podejście, jak zastosowałeś, czyli tą dockeryzację, do konteneryzacji tych serwisów.

**Mateusz Kisiel:** Tak, no to mogę pokazać, w tym jak to wygląda, bo to wygląda na dosyć.

**Marek Dziakowski:** No to to jest o tyle fajne, że właśnie nie trzeba zmieniać nic praktycznie w kodzie, bo sobie po prostu tworzymy kontener z tego serwisu i wrzucamy sobie go do Azure. Jeżeli ktoś chce mieć to on-premise, zgadza się na to, żeby coś takiego utrzymywać, no to wtedy on sobie po prostu stawia dockera lokalnie i jest to samo w zasadzie.

**Mateusz Kisiel:** Tak, no tak naprawdę. Jeżeli chce się uruchomić te usługi AI czy w chmurze, czy gdzieś na naszym serwerze, no to jest tylko kwestia skopiowania jednego pliku `docker-compose` i uruchomienia jednego polecenia. Docker Compose, `compose up`, no i to automatycznie już tworzy wszystkie obrazy i kontenery i samą konfigurację załatwia tak, jak chcemy.

**Piotr Buczkowski:** I nic nie musiałeś robić, żeby tylko to było jedno polecenie? Zrobione jest tak?

**Mateusz Kisiel:** Tak. Znaczy, nie chodzi mi o to, że – chodzi mi o to, że wdrażanie tego jest bardzo proste, tak, że nie trzeba praktycznie żadnego – jest to skonfigurować się, nic takiego.

**Łukasz Bott:** Dobra, Mateusza, pytanie następujące. Ta sytuacja – tak, no bo jeżeli to jest tutaj na naszej chmurze, no to my na to mamy wpływ, tak. Mamy tę funkcjonalność. No to wtedy. Kiedy ten? No to my tym zarządzamy. Powiedzmy, że robimy takiego dockera, którego stawiamy lokalnie u klienta.

**Mateusz Kisiel:** Mhm.

**Łukasz Bott:** Bo to Marek rzucił hasło jest, że jeżeli klient się zgodzi na utrzymanie tego, no ale od czasu do czasu, no na przykład tę usługę OCR. Niech będzie tam przykład – nie, pewnie tę, prąd ty modyfikujesz, tak. Tutaj, jeżeli oni sobie wzięli wersję.

**Piotr Buczkowski:** Dzisiaj, znaczy.

**Łukasz Bott:** Stan jakiś tam tego dockera. No to jak jest potem aktualizacja, aktualizacją takiego?

**Mateusz Kisiel:** No dobra, to, to mogę powiedzieć. To właśnie fajne jest to, że tak naprawdę nie musimy żadnych plików przesyłać. Jeżeli chcemy gdzieś to wgrywać, to jedyne, co potrzebujemy znać, to nazwę obrazu. Jeżeli ktoś chce zrobić sobie update, to po prostu updatuje tego obrazu – ten obraz, no i ten obraz automatycznie się pobiera przez dockera. Czyli powiedzmy, mogę zademonstrować.

**Łukasz Bott:** Ale dobra, no to OK.

**Adrian Kotowski:** Na przykład wersja.

**Piotr Buczkowski:** Skąd się pobiera? Skąd się pobiera?

**Mateusz Kisiel:** Powiedzmy tak, że zrobię jakąś zmianę w kodzie, coś tu pozmieniałem sobie, no to teraz chcę to jest updatować gdzieś tam na jakimś serwerze. To robię `docker compose build` minus, minus `push`, ewentualnie też zrobiłem sobie polecenie `deploy`, które praktycznie robi to samo, tylko jeszcze.

**Łukasz Bott:** Dobra.

**Piotr Buczkowski:** O, jak fajnie hasło wszystkim udostępniłeś.

**Mateusz Kisiel:** No trudno już. W każdym razie dobra, możemy sobie łatwo to zdeploy'ować. No i w tym momencie. Obrazy, OK, możesz sobie włączyć, włączyć do dockera? Obrazy, które tutaj są, czyli jeden obraz to jest Auto Service, ten do autentykacji, drugi do AI. Wgrywają się na chmurę, tam w Azure jest taki rodzaj resource'a o nazwie Container.

**Adrian Kotowski:** Instance.

**Mateusz Kisiel:** Container Registry, coś takiego? Tak. No dobra, to jeszcze raz uruchomię.

**Łukasz Bott:** Dobra, dobra, nie ma, to już, no może tak.

**Mateusz Kisiel:** No tak, ale dobra, to jakby wiesz, to.

**Piotr Buczkowski:** To na pewno jest, nie mówię, tak?

**Mateusz Kisiel:** No dobra, ale to znaczy – zarządzania tego z chmury powinienem pokazać.

**Łukasz Bott:** Dobra. Ale czekaj, to ja pomogę, podążę. To jednak pytanie, bo tu mówisz o tym, to mówisz, że wystarczy, że tam sobie dockera aktualizują. Jeżeli to są zmiany w tym takim kodzie.

**Mateusz Kisiel:** No.

**Łukasz Bott:** Jego pytanie, czy ten docker na przykład?

**Mateusz Kisiel:** No.

**Łukasz Bott:** Trzyma jakieś dane? Powiedzmy, docker zainstalowałem u klienta lokalnie i powiedzmy, że ten czy jakikolwiek te usługi AI – one się na czymś uczą, na przykład niech będzie ta baza wiedzy, tak, u klienta. Klient sobie buduje swoją bazę wiedzy. To pytanie, czy te dane do tej bazy wiedzy jest trzymane w tym dockerze? W ramach tego, czy nie? No bo chodzi mi o to, żeby, wiesz, bo jak sobie napiszę – bo w tej chwili jak aktualizujemy AMODIT, to aktualizujemy.

**Piotr Buczkowski:** W bazie danych.

**Mateusz Kisiel:** No.

**Łukasz Bott:** Taką typową, a tylko część aplikacyjną, tak. Nie zmieniamy danych, które już są, nie.

**Mateusz Kisiel:** No nie, no jakby dane są zapisywane. No tak, dane są dalej w bazie danych, tak. Jakby my tylko zmieniamy, tak samo jak teraz aktualizujemy. No nie, nie wpisujemy żadnych danych.

**Łukasz Bott:** OK. Dobrze. Mnie, no to dlatego dzięki – to chciałem się upewnić, że docker sam z siebie jako takich danych. Danych klienckich czy danych z bazy AMODIT nie trzyma?

**Piotr Buczkowski:** Musisz pamiętać, żeby tak było. Musisz pamiętać, żeby tak było, żeby nie zrobić czegoś, co przechowuje lokalnie, tak, jakoś w jakiś sposób, tak.

**Mateusz Kisiel:** Znaczy, na przykład jakieś tam?

**Piotr Buczkowski:** To nie to, że to jest automatycznie tak zrobione, tylko musisz pamiętać, żeby tak robić.

**Mateusz Kisiel:** Tak, no jak jakieś obrazki, może sobie trzymać jakby lokalnie, tak, możecie się dobrać do czegoś, przydadzą w tej aplikacji.

**Piotr Buczkowski:** Możesz robić jakieś pewnie pliki lokalnie sobie zapisywać, tak. Pokazuję, tylko musisz pamiętać, że nie możesz na nich w dłuższej perspektywie polegać, tak.

**Mateusz Kisiel:** Co jest fajnego, to mogę pokazać, jak się tutaj na chmurze to updatuje. Powiedzmy, że już się updatował ten obraz, bo to widać, już się wgrało i teraz to sobie wgrać, nową wersję na chmurze. No to mogę sobie zmienić na przykład cokolwiek w jakiejś zmiennej środowiskowej na jakąś inną, zrobić save and create revision. I w tym momencie.

**Piotr Buczkowski:** Na produkcji to zmieniasz.

**Mateusz Kisiel:** Tak, to jest produkcja, ale właśnie fajne jest to, że nie ma żadnego przestoju.

**Piotr Buczkowski:** To właśnie powoduje, że.

**Mateusz Kisiel:** No właśnie, właśnie nie powoduje.

**Piotr Buczkowski:** Za łatwo to się robi, dokładnie.

**Mateusz Kisiel:** Bo zobacz, że – zobaczę, że – tak, zobacz, że tak naprawdę stara instancja ciągle jest uruchomiona, jakby nie ma żadnego przestoju. To jest fajne, że powstaje nowa instancja serwera, która się uruchamia, no i w czasie, jak się ona uruchamia, ciągle stara jest w gotowości, obsługuje requesty. W pewnym momencie będzie chwila, gdy będą obie uruchomione. O, już widać, że uruchomiła się nowa i teraz stara jest provisioning, czyli stara już schodzi. No i tak naprawdę nie było żadnego przestoju i to jest duża zaleta tego. No i jeszcze też można tak – jak coś.

**Piotr Buczkowski:** A jak, jak to, co, jak docker robi jakieś zadanie, które trwa pół godziny?

**Mateusz Kisiel:** No to wtedy jest. Ogólnie to działa tak, że jeżeli jakiś request idzie, bo to jest aplikacja webowa, tak, czyli obsługuje jakieś requesty, i ten Azure sobie monitoruje ten requesty i tak długo trzyma – bo w tym momencie są obie instancje uruchomione – i tak długo trzyma starą, aż wszystkie requesty z niej zejdą. I jak zejdą z niej requesty, to uruchamia się wtedy już tylko nowa, stara schodzi.

**Adrian Kotowski:** No to jaki był – kontynuuje się. Myślałem, że to jest TrustCenter, bo to jak kontenery się windowsowym – dzisiaj dostałem te, te swoje serwisy uruchamiasz.

**Piotr Buczkowski:** Nie, właśnie mieszamy te tematy.

**Mateusz Kisiel:** Jeszcze, jeszcze raz, co?

**Adrian Kotowski:** Ale jaki kontener, jaki tam taki tam jest? Chociaż system operacyjny tych kontenerach – Linux, coś?

**Mateusz Kisiel:** Możesz powtórzyć? Nie rozumiem ciebie.

**Adrian Kotowski:** Jaki tam jest? Chociaż w sensie system operacyjny, jaki jest, jak jest?

**Mateusz Kisiel:** Aha, no to, to możesz sobie zdefiniować w kontenerze, tak, czyli w obrazie – w tym wypadku akurat mam Linuxa.

**Adrian Kotowski:** Że tak, to nie ma – po prostu jaki wybrałeś u nas? W naszym przypadku też, tak z ciekawości chciałem się.

**Mateusz Kisiel:** To tak. Jak sobie zawiedziemy na dockerfile, to dockerfile – jest zdefiniowane wszystko. W tym wypadku ja tutaj korzystam z MCR Microsoft .NET ASP.NET, no i to pod spodem ma Linuxa, z tego co kojarzę.

**Adrian Kotowski:** Przecież można nie wybrać dla TrustCenter, bo to znaczy, jak ten kod wydzielimy, bo TrustCenter też jest to chyba chciałem coś napisane.

**Marek Dziakowski:** Bo tak.

**Mateusz Kisiel:** Ogólnie to, jak mało – jak chcemy korzystać z Windowsa, możemy. Jak chcemy, możemy z Linuksa. Ja tutaj korzystam z Linuksa, ponieważ mam też inne kontenery na Linuksie i trzeba mieć jakby wszystkie, jak się lokalnie uruchamia – trzymać wszystkie w tym samym rodzaju trzeba, bo wszystkie linuksowe albo wszystkie windowsowe. Ale na Azure tego problemu nie ma, więc tak może to dowolnie można.

**Adrian Kotowski:** Tak. A propos tych kontenerach, czyli, a nie – docker compose też wydaje mi się, że lepiej od razu iść, ale to bardziej dojrzałe rozwiązanie i też bardziej dostosowane do takich produkcyjnych już jakby instalacji, więc mi się wydaje, że po prostu mielibyśmy więc większe możliwości. To jest lepsza – okres ochrony sekretów, też na przykład – auto-healing na przykład, po jakimś tam jakiejś awarii.

**Mateusz Kisiel:** Znaczy, no można potem myśleć o przechodzeniu na Kubernetes, a myślę, że na razie tak prostszym rozwiązaniem jest docker i to praktycznie mi wystarczy do wszystkiego. Na przykład możemy też sobie łatwo tej zmieniać mocy tego serwera. Na przykład jest minimalna liczba replik, maksymalna liczba replik, no i jak ekspert to ustawi, na przykład 10 – to będzie wtedy on w zależności od obciążenia zwiększał albo zmniejszał ilość serwerów, czyli będzie robił automatyczne skalowanie. Więc na przykład w nocy, jak tam nikt nie korzysta, to byłby jeden serwer, a jak się nagle pojawia jakoś dużo zapytań w pewnym momencie, to może sobie zrobić nawet 10 serwerów i load balancing prowadzić między nimi.


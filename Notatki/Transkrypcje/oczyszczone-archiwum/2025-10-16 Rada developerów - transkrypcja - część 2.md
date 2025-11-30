**Data spotkania:** 16 października 2025, 08:01 - część 2

---

To jest też fajne. I też oczywiście można ustawiać, można ustawiać.

**Piotr Buczkowski:** No ale trzeba oczywiście pamiętać, żeby tak zaprogramować, żeby to było, żeby to działało, tak.

**Mateusz Kisiel:** Tak. No żeby tam nie było jakichś tam rozbieżności w cache'u i tak dalej. No tutaj akurat w przypadku tego AI to praktycznie można zupełnie niezależnie puszczać jakieś nowe rzeczy, nie ma tam jakichś wspólnych liczników, nic takiego. Też można sobie ustawiać łatwo, ile ma pamięci, jakieś tam mocy, mocy procesora. Coś myślałem.

**Piotr Buczkowski:** Za łatwo się niektóre rzeczy robi.

**Mateusz Kisiel:** No właśnie łatwo się robi. To jest wygodne i zaoszczędza dużo czasu, uważam.

**Piotr Buczkowski:** Zna łatwo, za łatwo można popsuć.

**Mateusz Kisiel:** Właśnie fajne jest to, że można sobie łatwo też przenosić nawet do jakiegoś innego Azure'a, bo w przypadku, w przypadku wirtualnych maszyn to trzeba na nowo wszystko konfigurować ręcznie i to można, można się pomylić przy tym.

**Piotr Buczkowski:** Jak często takie rzeczy robimy? Nie, no dobrze.

**Mateusz Kisiel:** Też, też jeszcze inna rzecz jest fajna, że na przykład HTTPS można łatwo konfigurować, bo zrobiłem aplikację na HTTP/TLS – to jest coś takiego jak Ingress, który automatycznie załatwia SSL. Jedyne, co musiałem zrobić, to od Łukasza pobrać certyfikat, certyfikat na naszą domenę, na nasz adres DNS, a wgrać, żeby. Żeby była krótka, tak? No ale jakby polecam bardzo, bo to jest wygodne.

**Piotr Buczkowski:** No ale to trzeba. Trzeba zaplanować, co możemy w tym, co możemy w tym zrobić, tak, a czego nie. Nie to, że wszystko nagle microservices, bo nie, nie da się.

**Mateusz Kisiel:** Znaczy, no w tym momencie.

**Adrian Kotowski:** A możesz pokazać jeszcze konfiguracji, na przykład, bo tam wcześniej pokazywałeś to jest po prostu podawania poszczególnych kluczy konfiguracyjnych.

**Mateusz Kisiel:** Aha, to tak. No to jakby, jak to działa, jak mamy jakąś aplikację zrobioną w tym nowym świecie, w tym .NET Core? No to mamy zazwyczaj te pliki `appsettings.json` i one tutaj zawierają jakieś dane konfiguracyjne, tak. Jakby tego pliku nie ma w, nie ma w obrazie do dockera, więc żeby to sobie skonfigurować na chmurze, to się podaje w zmiennych środowiskowych i jest taka konwencja, że. Zaraz settings.

**Adrian Kotowski:** Podwójnie dwukropkiem jakoś tak, chyba to.

**Mateusz Kisiel:** Chyba 2 podkreślniki z tego, co kojarzę, są między.

**Adrian Kotowski:** A dobrze, tak, że można podawać to tak.

**Mateusz Kisiel:** Albo, albo kropki, zaraz zobaczymy. Tak, no jakby powiedzmy, że chcę sobie coś wpisać w Azure AI OCR – to jest Azure AI OCR – no to po prostu się oddziela 2 podkreślnikami i automatycznie .NET Core sobie to odczytuje w ten sposób.

**Adrian Kotowski:** Z ciekawości, czy można wybrać? Na przykład jest wskazać, bo to sobie tego nigdy nie, nie sprawdzałem.

**Mateusz Kisiel:** Można. Można, można, na przykład w tym momencie nie wiem, czy mam to wpisane, ale.

**Adrian Kotowski:** Z pięćdziesiąt entry jakieś.

**Mateusz Kisiel:** Akurat, akurat dla tej instancji tego nie ma, ale gdzieś tak przedtem robiłem, że.

**Adrian Kotowski:** Możesz rozwinąć jakiś ten pasek? W sensie, manual entry? Tam jeszcze do wyboru, tak z ciekawości.

**Mateusz Kisiel:** Tak, jest, jest reference i można podać reference do secret i wtedy nie trzeba wpisywać. Na przykład jest AMODIT AI connection string – to chyba to jest używane tutaj, gdzieś, z tego, co mi się wydaje. A tutaj jest connection string default connection – jest reference to secret.

**Adrian Kotowski:** OK. Dobra, okej? Należałoby po prostu nie podawać tam 10 razy. Jakieś tam wpisałem, dobra, OK, to w porządku.

**Mateusz Kisiel:** No i w tym momencie chodzą właśnie takie 3 microservices ode mnie, czyli ten Auto Service, AMODIT AI i Chroma Service, czyli ten od bazy wiedzy. No i mam też ten registry z tymi obrazami. Tomasz, moglibyśmy pokorzystać wszyscy, powiedzmy, na wspólnego registry, żeby łatwo tym obrazami zarządzać.

**Adrian Kotowski:** Teraz zdaje się, masz po prostu 3, jakby to, czy te rodziny obrazu, w sensie te 3 microservices? Tak.

**Mateusz Kisiel:** Tak, gdzieś tak powiem. Opisać, jak się do tego wejdzie. Identity.

**Adrian Kotowski:** Powiedz teraz, do testów tych integracyjnych mamy ten nasz jakby on-premise, słaby ten serwer, ten do dockera, a dotyczy – ten Docker Hub tutaj na, na tych produkcyjnych microservices mamy – bardzo korzystamy z tego, z rejestru na Azure.

**Mateusz Kisiel:** Tutaj są wszystkie obrazy, jakie są, czyli do tego rejestru też wrzucałem ten AMODIT Talk, czyli te komunikatory. No i to jest też o tyle fajne, że można dawać uprawnienia, uprawnienia, że na przykład ktoś ma uprawnienie tylko i wyłącznie do pobierania danych, a nie do wgrywania. Czyli zrobiłem taki klucz, że można go będzie bezpiecznie podawać klientom, żeby sobie pobierali z tego rejestru AMODIT Talk. I nie będą w stanie nic to jej zepsuć, ponieważ nie mają uprawnień do wgrywania.

**Piotr Buczkowski:** Jakoś wersjonowanie czy coś?

**Mateusz Kisiel:** Wersjonowanie można zrobić. W każdy ten obraz dockerowy – jeszcze, proszę, pokażę, pokażę tutaj. Jak się buduje w docker compose, musiałem pokazać teraz. To jest to. No tutaj jest dobra – jak się buduje ten obraz, to się podaje także. Także tak – i ten tag oznacza zazwyczaj wersję tego i domyślnie, jeśli nie podaje się tego tagu, to jest tak wpisywany `latest`, ale może także z innymi tagami wgrywać. Na przykład jak się daje zrobić dwukropek i się wpisze jakąś, nie, nazwę – na przykład w wersji, ja nie wiem, `v1.1` – no to będzie wygrane z tagiem `v1.1` i można sobie wtedy te tagi łatwo zmieniać, tak. Tak samo, jak sobie wejdzie na przykład jakąś. Ktoś ma MySQL, ma MySQL docker. I tak samo sama się jakieś tagi i tak jest tak – `9.4.0` jest też, jest też `latest`, akurat tego nie napisali. Jest też, jest OK. Ten `latest` jest jakby dla każdego domyślnie, jak się nie podaje tagu. Więc wersjonowanie można też łatwo załatwić. Ewentualnie, jeżeli ktoś, jeżeli ktoś chce mieć zawsze najnowszą wersję, to może po prostu wpisać sobie albo `latest`, albo nie podawać tego tagu.

**Piotr Buczkowski:** No dobrze, ale mieliśmy rozmawiać o TrustCenter, tak.

**Mateusz Kisiel:** No dobra, tak w skrócie pokazałem, jak to wygląda z tym dockerem.

**Piotr Buczkowski:** Teraz to, co ma zrobić Marek – o, nie ma nic związanego z witryną webową, tak?

**Marek Dziakowski:** Tak, tutaj nie, nie, nie, to jakby chcemy tylko po prostu utrzymać ten sam sposób, tak.

**Piotr Buczkowski:** Czy ma być? Bardziej.

**Marek Dziakowski:** Żeby nie było rozbieżności, tylko trzymać chociaż jeden kierunek mniej więcej, więc dlatego tutaj też Mateusz pokazuje, jak to wygląda.

**Piotr Buczkowski:** To jest całkiem co innego niż to, co pokazywał Mateusz, tak.

**Mateusz Kisiel:** To znaczy, można to zrobić też tak samo w kontenerach dockerowych i też o tym kontenera po uruchomić tak, by tak naprawdę nie ma potrzeby, żeby to była usługa webowa.

**Adrian Kotowski:** Czy te? Że teraz, nie wiem, że robimy, bo się może troszeczkę szufladkowanie zrobić, wspólne byłoby to, gdyby był – znaczy najlepiej jakby było najbardziej optymalnie, bo mamy teraz te główne aplikacje, te wszystkie apki wbudowane w aplikacje, a także mieliśmy teraz microservices, więc jakoś fajnie by to nie wiem, czy ewentualnie pilnować tego określania. Po prostu w tym.

**Piotr Buczkowski:** Posłuchaj.

**Mateusz Kisiel:** W przypadku AMODIT jest ten problem, że u klienta by trzeba było każdy on-premise aktualizować, ale na przykład takie.

**Piotr Buczkowski:** Znaczy, dobrze, ustalmy termin, ustalimy jeden temat rozmowy, mówimy o TrustCenter, trzeba nam rozstrzygnąć.

**Adrian Kotowski:** Tak, ale teraz to też nie mówimy jeszcze.

**Marek Dziakowski:** Nie, mówmy już o TrustCenter.

**Adrian Kotowski:** TrustCenter ciągle.

**Mateusz Kisiel:** Ogólnie można o microservices'ach cieniowo, bo takie wspólne testowanie takiej infrastruktury, jak by uruchomić dla microservices też był dobrym pomysłem.

**Piotr Buczkowski:** No nie, nie, nie.

**Marek Dziakowski:** Tylko, że tutaj będzie raczej w tej sytuacji będzie jeden.

**Piotr Buczkowski:** Wiem, że zabawa jest fajna technologiami, ale myślmy sensownie.

**Marek Dziakowski:** Taka tutaj – będzie to jeden serwis, nie tego tego nie uzyskamy. Mówimy tak samo, tak jak Piotr mówił na początku, bo musi to być robione po kolei.

**Adrian Kotowski:** Czy można to generalnie wyskalować? Bać nie horyzontalnie, tylko po prostu wertykalnie się – po prostu więcej pamięci daje, CPU, RAM, w takiej zasadzie?

**Marek Dziakowski:** Przez jedną instancję. No, no, tak, to tak jak.

**Piotr Buczkowski:** Znaczy, tutaj problem jest w tym, że musimy kolejkować zadania, także generować się po kolei. Nie możemy jednocześnie 2 zadań wykonać, bo się popsuje.

**Marek Dziakowski:** Tak, ważna jest ta kolejność. Żeby ją zachować, było inaczej, to nie ma sensu, więc tutaj kolejka będzie trzymała kolejność. Po prostu jeden worker będzie mógł tylko przerabiać to.

**Piotr Buczkowski:** No tak.

**Marek Dziakowski:** No i tyle. No to dlatego, tak – to, co powiedział Adrian? To też jest bardzo proste. W razie co, gdyby trzeba było dołączyć tam ze sobą serwerowych, no to w tym przykładzie Mateusza byłoby to dosyć proste. Raczej.

**Piotr Buczkowski:** Będzie taka potrzeba.

**Marek Dziakowski:** No właśnie nie wiem, nie wiem, ale lepiej się przygotować na wszelki wypadek niż potem myśleć nad tym. Zrobić sobie furtkę, żeby można było to zrobić prosto. No to ogólnie do tego – będzie jeszcze potrzebny ten SignalR. Żeby w taki dosyć prosty sposób też sygnalizować się zwrotnie, że dane. Zadanie zostało wykonane przy tej.

**Piotr Buczkowski:** No i jak będzie to usługa notyfikowała TrustCenter, że zakończyła pracę nad tym, czy będzie, czy.

**Marek Dziakowski:** No będzie.

**Piotr Buczkowski:** Czy po prostu witryna musi sobie? Dynamicznie czy tam aktywnie sprawdzać?

**Marek Dziakowski:** No nie chciałbym, żeby ona to odpytywała, bo to różnie może być, tak jak w przypadku nie wiem, większej ilości dokumentów – to będzie mogło to trwać trochę więcej czasu, więc bez sensu, żeby to tak pytało. Czy tam raczej bym nie robił drugiej kolejki zadaniami wykonywanymi, tylko bym właśnie skorzystał z SignalR. Proponowanego. Są opcje.

**Piotr Buczkowski:** Więc SignalR. Gdzie SignalR?

**Marek Dziakowski:** No jest opcja, jeżeli byśmy to robili. Władze Azure, Azure udostępnia taką opcję, jak SignalR Service.

**Piotr Buczkowski:** Ale kto będzie modyfikował ten SignalR?

**Marek Dziakowski:** Worker, worker będzie zgłaszał, że dane zgłoszą, dane – dokument.

**Piotr Buczkowski:** Czyli ta usługa dodająca do blockchaina? Tak?

**Marek Dziakowski:** Tak, tak, on będzie zgłaszał, że się stało wykonany.

**Piotr Buczkowski:** Czyli tak naprawdę witryna, witryna SignalR. Naszej witrynie, przeglądarce SignalR będzie z innego serwera? Tak.

**Marek Dziakowski:** Tak.

**Piotr Buczkowski:** Da się tak?

**Marek Dziakowski:** Wydaje mi się, że tak.

**Piotr Buczkowski:** Czy pewnie jakieś CORS czy całość będzie potrzeba, tak?

**Marek Dziakowski:** No tak, tutaj trzeba będzie zrobić jeszcze tego – potwierdzić, bo tak to się nie robiliśmy, więc. Ale no tak, moim zdaniem jest to opcja, żeby w ten sposób to zrobić po prostu. Mówię, można by kolejki robić też jako – wtedy te serwery webowe by się prosto pytały jedną stacjoną kolejek.

**Piotr Buczkowski:** Nie, to nie wiem, ale będą też – nie, to już lepiej by było, że.

**Marek Dziakowski:** Raczej, no tak, tak.

**Mateusz Kisiel:** Znaczy. Znaczy, te kolejki też nie są takie głupie, żeby się odczytywać.

**Piotr Buczkowski:** W ogóle, że tak rezygnujemy z tego, że użytkownikowi, użytkownikowi się pojawia automatycznie, także podpisano – po prostu jest, że ten dokument czeka na podpisanie. Sprawdź za chwilę, albo to i to, albo dostaniesz maila z informacją, że podpisane, tak.

**Marek Dziakowski:** A ewentualnie. Mhm.

**Piotr Buczkowski:** Żeby użytkownik ręcznie musiał nacisnąć przycisk, tak, bo wiadomo, że nie będzie naciskał tak szybko, tak często, jakby to robiło automat.

**Mateusz Kisiel:** Znaczy.

**Marek Dziakowski:** No tak, tak.

**Mateusz Kisiel:** Też wydaje mi się, że to podejście drugie, czyli żeby zamiast skorzystać z SignalR, wrzucać do jakiejś drugiej kolejki też nie jest złym pomysłem, bo to nie jest tak, że się odpytuje to co jakiś czas, tylko jest ciągłe połączenie jakieś po TCP, no i dostaje też jakieś notyfikacje, jak coś doszło do kolejki, więc wydaje mi się, że wydajnościowo niekoniecznie jest najgorsze rozwiązanie. Ma tą zaletę, że jak padnie serwer, no to będzie dalej to w kolejce, więc jak się, jak serwer wstanie, będzie mógł sobie to wziąć z tej kolejki.


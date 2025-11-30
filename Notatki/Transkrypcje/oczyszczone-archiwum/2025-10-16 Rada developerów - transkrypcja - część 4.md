**Data spotkania:** 16 października 2025, 08:01 - część 4

---

**Marek Dziakowski:** No tak, tak, tego chciałem Janusza.

**Piotr Buczkowski:** Uzyskać akceptację tych kosztów.

**Marek Dziakowski:** Ale wysłałem ten dokument, żeby to przejrzał.

**Piotr Buczkowski:** Pytanie, czy nie odpowiedział, tak?

**Marek Dziakowski:** No a jeszcze nie wiem. Wczoraj mówił mi, że dzisiaj będzie – nic mi nie mówił, że jest jakiś redeco, także. Dynamicznie się widzisz z nim, no wszystko.

**Piotr Buczkowski:** Może by to omawiać dzisiaj to, tak.

**Marek Dziakowski:** Możliwe, ale wczoraj też z Łukaszem Podsklepką rozmawiałem, więc to – mam powiedział, że tam z Joanną trochę to skonsultuje, czy oni w ogóle mieli coś takiego do czynienia, tam będzie jakieś dodatkowe informacje, że będzie. Wygląda. No myślę, że taki PoC można by zrobić – jakieś tam proste, że na razie bez komunikatów, tylko po prostu wydzielenie. Zobaczcie, co wyjdzie, jak będzie.

**Piotr Buczkowski:** Nie, dobrze. Jeżeli takie są problemy z tym. Chciałem powiedzieć jeszcze, byśmy się – język blockchain, tak, to trzeba to podzielić tak – koniecznych do niej szybciej.

**Marek Dziakowski:** Myślę – ja bym to za sprint, bo ona już kolejny sprint, bo w tym też raczej nie ma sensu – tak się nie zmieszczę. Numer, no tak, tak, no właśnie.

**Piotr Buczkowski:** Tak, teraz się kończy sprint, tak? To nie, no ale na kolejne jak najbardziej.

**Marek Dziakowski:** Dobra, to. Po prostu może zróbmy tak, że spróbuję to zrobić, więc w ten sposób, co jest – co robi tu Mateusz, żeby się podobnie.

**Piotr Buczkowski:** Dlaczego Mateusz? To, mówię, to jest chyba całkiem co innego, tak?

**Marek Dziakowski:** Nie, no.

**Piotr Buczkowski:** Bo tutaj ma niezależnie, ma nie nasłuchiwać na HTTP, tylko po prostu sobie działać tam w tle.

**Mateusz Kisiel:** Znaczy, to nie ma znaczenia, to jakby to może on w ogóle nie korzystać z jakichś połączeń.

**Piotr Buczkowski:** Sprawdzać. No tak, tak, tak.

**Marek Dziakowski:** No tak, tylko po to, żeby było to dockerze – o to chodzi.

**Piotr Buczkowski:** No tak, tak.

**Adrian Kotowski:** Jeszcze teraz, wybaczcie, przerwę – wyszukałem, że można na przykład łatwo ten event grid powiązać z SignalR na przykład, że – przez Azure środkowe – udzielał odpowiedź do pewnego – właśnie z Service Bus. Myślę, że to też jest jakiś pomysł.

**Piotr Buczkowski:** Chcemy to jak najszybciej zrobić. Tak, może zaczniemy od czegoś łatwiejszego.

**Adrian Kotowski:** Ale to jest taka dość gotowe rozwiązanie. Generalnie jest takie. Żeby były to te przetwarzanie i tego, tego dodanie do blockchaina i od razu byłby komunikat. A to się wydaje w miarę takie – artykuł nawet na, na dokumentacji Microsoftu o tym, jak to zrobić.

**Marek Dziakowski:** No weź pokaż, podeślij jakąś.

**Adrian Kotowski:** Na grupkę. Szybko znalazłem, może nie być. Dobra.

**Piotr Buczkowski:** O czym mówię, zróbmy. Po kolei – tak, najpierw wydzielamy tego generowania blockchaina do kolejki, do jakiegoś oddzielnego procesu, który po kolei będzie to robił.

**Marek Dziakowski:** To chyba to jest to właśnie?

**Piotr Buczkowski:** Który zapewni nas, że nie będziemy psuć blockchaina, tak, bo to jest największy problem. Ułatwienie – dodatkowa komunikacja, szybsze poinformowanie użytkownika – później.

**Marek Dziakowski:** Znaczy, blockchain. To jest tak, że blockchain się jako taki nie psuje, po prostu są dokumenty, które nie są jego częścią. Wiszą, także te dokumenty. Problem jest.

**Piotr Buczkowski:** No. I cokolwiek, tak, ale żeby nie było tak jej dokumentów.

**Marek Dziakowski:** Tak, tak. No bo teraz skala się zwiększyła. Gdzieś tam sprawdzałem, to pół roku temu to było tam może ze 4 dokumenty czy tam 2, tak, wiszące. Jak sprawdziłem to ostatnio, to było ich ponad 50.

**Piotr Buczkowski:** To, to w ciągu następnego sprintu musimy przejść na usługę, żeby nie było więcej tych dokumentów.

**Marek Dziakowski:** No i to szybko rośnie, widać. Mhm.

**Piotr Buczkowski:** Możemy na, na moment ograniczyć, tak, funkcjonalność TrustCenter właśnie z tych powiadomień, responsywność – jest to konieczne, tak, jak najszybciej musimy zrobić pierwszy krok, czyli wydzielić to do usługi. Nawet ograniczając funkcjonalność, tak.

**Marek Dziakowski:** OK. Myślę, że tak można tu podsumować.

**Piotr Buczkowski:** Później będziemy mogli rozbudowywać. To jest tak, jak będzie zapotrzebowanie.

**Marek Dziakowski:** No tak, myślę, że rozbudowa to w przyszłości nie będzie jakoś.

**Piotr Buczkowski:** Nawet jak to będzie przeniesienie do jednego typu dockera czy tam Kubernetes czy coś, to ale już będziemy mieli, tak. Wydzielony, już teraz nie będziemy psuć jakichś kolejnych plików. Dobrze. To tyle – czy coś jeszcze?

**Marek Dziakowski:** No ode mnie to tyle.

**Łukasz Bott:** To chyba tyle, tak. A nie, ten nasz temat to, to wiemy, co mamy, tak, co robić. Ten generalnie koncepcja jest taka, żeby to te źródła. Generalnie tak, te źródła systemowe, bo to z nimi jest tam problem z tymi ujemnymi identyfikatorami.

**Anna Skupińska:** Tak, omawialiśmy to wczoraj.

**Łukasz Bott:** Będą teraz dodatnimi identyfikatorami, tak, i z GUID'em, więc będzie można je łatwo. Część dotychczasowe źródła, które mają ten ujemny GUID – tym to po prostu pozostaną, tak, i z czasem się po prostu sukcesywnie albo zamieni, albo po prostu zostawi, tak, żeby. Nie wracały to, co się będzie wymagało zmiany jakieś – tak, to z pewnością wszystkie te miejsca, głównie w module raportowym. Więc korzystamy z źródeł. Systemowych. Tutaj, Ania, jeszcze jedno mi wpadło – odnośnik do źródła. Nosimy pole typu odnośnik do źródła danych, to także jeszcze ewentualnie, tak, trzeba będzie zmienić po prostu sposób. Jeżeli ktoś się odwołuje do zewnętrznego źródła danych tego systemowego, tak, to żeby. Już się odwoływał do, do tych źródeł, które mają właśnie ten GUID i dodatni. Identyfikator.

**Anna Skupińska:** Chodzi o to, żeby zmienić, żeby już odwołanie się do źródła to było przez GUID?

**Łukasz Bott:** To znaczy, nie, nie chodzi mi o to. Chodzi mi o to, że.

**Anna Skupińska:** No nie.

**Łukasz Bott:** Że żeby – chodzi mi tylko o to, że w tych miejscach, o których wymieniłem gdzieś tam, po prostu musimy zmienić to tak, jeżeli zmienimy teraz to. Te źródła, to zewnętrzne – tak, te źródła danych systemowe – raz, że będą odpowiednio tam oznaczone jako systemowe, będą miały dodatni identyfikatory i GUID. No to już po prostu, żeby pamiętać o tych kilku miejscach, tak, gdzie, gdzie to występuje? Tak, gdzie to zagadnienie występuje, żeby właśnie tam pobierać, bo rozumiem, że to, że frontend – to jest frontend, on bierze z jakiegoś backendu, więc po stronie backendu trzeba, tak. Zapewnić, że.

**Anna Skupińska:** Tak, to głównie praca po stronie backendu, oczywiście.

**Łukasz Bott:** No dokładnie, więc zmiany tam w tych wszystkich miejscach, gdzie jest odwołanie do źródeł danych systemowych po ujemnych indeksach. Trzeba zrobić tak, żeby obsługiwały teraz ten dodatnie indeksy. Tak, bo rozumiem, że GUID ci będą potrzebne do tylko do, tak jakby, do synchronizacji, tak, w sensie do przenoszenia między środowiskami – tak, jakimś tam testowym, docelowym.

**Anna Skupińska:** Mhm. Dokładnie.

**Łukasz Bott:** Dobry takt. Wymyślony.

**Anna Skupińska:** Chcielibyście jakieś szczegóły? No jak nie, no to.

**Łukasz Bott:** Nie – mieliście to, jak będziemy się zabierali za to, tak, to jeszcze ewentualnie to, to przedyskutujemy.

**Anna Skupińska:** Tak, na pewno dojdą 2 nowe kolumny, czyli czy jest systemowe źródło i jaki ma GUID. I zastanawiam się, czy wszystkim źródłem generować GUID, tylko tym, które są systemowe?

**Łukasz Bott:** Wiesz co, na wszelki wypadek.

**Anna Skupińska:** Podobnie sądzisz z GUID'ami, żeby wszystkie miały GUID'y. Na razie zrobiłam tak, że tylko systemowe mają.

**Łukasz Bott:** No i czyli tak jak – jeżeli nawet tego GUID'ów na razie do czegokolwiek nie będziemy używali, to, to tak.

**Anna Skupińska:** A zrobisz, żeby wszystkie te źródła? Miały GUID i. Dalej. A ja też mieć kolejną.

**Łukasz Bott:** Bo to, bo to, Janusz się później może przyda właśnie do jakichś mechanizmów eksportu-importu w postaci definicji, na przykład źródeł czy dashboardów poprzez, poprzez pliki, tak, poprzez interfejs, bo w tej chwili nie ma takiej możliwości, tak. Ja sobie skonfigurowałem źródło danych, na przykład w jednym środowisku i chciałbym je przenieść na inne środowisko. Oczywiście na tym docelowym środowisku to może będę musiał zaktualizować, na przykład connection string, tak. Jakiś, ale co do zasady, to reszta – nie wiem, zapytanie SQL czy coś w tym stylu, opis, nazwa – ten, mi się nie zmienia, tak.

**Anna Skupińska:** Dokładnie.

**Łukasz Bott:** Dobra, to tyle, dobra.

**Anna Skupińska:** A to, że się przydadzą coś innego, OK.

**Łukasz Bott:** Dobra, dzięki za spotkanie. Cześć.

**Mateusz Kisiel:** Cześć.

**Anna Skupińska:** No cześć.

**Marek Dziakowski:** Część.

**Adrian Kotowski:** I cześć.


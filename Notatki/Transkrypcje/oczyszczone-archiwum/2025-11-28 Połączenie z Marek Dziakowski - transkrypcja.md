**Data spotkania:** 28 listopada 2025, 10:30

---

**Janusz Bossak:** Przez skrzynkę przez serwer pocztowy klienta.

**Marek Dziakowski:** Tak, żeby wychodziły z domeny klienta. Technicznie jest to możliwe, bo tak samo działamy z Turbo SMTP – my wysyłamy do nich, oni to wysyłają dalej. Tylko że w Turbo SMTP możemy sobie ustawić naszą nazwę. A tutaj klient musiałby dać nam dostępy, żebyśmy przyjmowali wszystkie maile, które od nas wychodzą. Czyli nawet jeżeli nie powinien się zdarzyć, ale zdarzył się jakiś spam, bo coś się przycięło, pójdzie 1000 maili. To 1000 maili przejdzie przez skrzynkę przez ich serwer pocztowy i 1000 maili wyjdzie od nich. To jest jedna taka rzecz. Inna rzecz to też, czy chcemy z punktu handlowego sprzedawać – my wystawiamy te dokumenty, podpisujemy je też po swojej stronie, a one miałyby wychodzić, że od nich.

**Janusz Bossak:** Mam.

**Marek Dziakowski:** Z poziomu handlowego niezbyt. Dobre.

**Janusz Bossak:** Nie widzę problemu z poziomu handlowego. Biznesowo chodzi prawdopodobnie o to, że niektórzy klienci to też podnosili i tam myśmy pamiętam robili jakieś mechanizmy, nazwijmy to aliasów, że to nie idzie z AMODIT czy z TrustCenter. Tylko wygląda jakby szło od klienta i to już taka funkcjonalność jest. Więc pytanie o co im chodzi? Czy im chodzi o to, żeby to wyglądało, że to wychodzi od nich? Czy im chodzi o to, żeby fizycznie to szło przez ich serwery? Bo to są 2 różne rzeczy. Pierwszą mamy jakoś rozwiązaną, bo to było robione jeszcze tam chyba dla Rossmanna. Bo gdzie mi się zapalały żółte lampki, bo TrustCenter to jest przecież nasza usługa i do tego obsługuje wielu klientów, że wysyła Rossmann, wysyła Adecco, wysyła i tak dalej.

**Marek Dziakowski:** Tak.

**Janusz Bossak:** I nagle jakaś część tej wysyłki TrustCenter miałaby kierować przez serwer klienta, przez serwer pocztowy klienta.

**Marek Dziakowski:** To swoją drogą, że trzeba by było to też programować, żeby tak działało. To dodatkowa komplikacja.

**Janusz Bossak:** To taka całkiem spora, bo wszystkie maile, wszystko co wychodzi od nas, musiałyby być przerobione, żeby mogły wychodzić skądś, nie z domyślnego punktu.

**Marek Dziakowski:** Tak, tylko że istnieje potencjalne ryzyko, że coś tam wyślemy nie to co trzeba, nie przez ich serwer na przykład pójdzie coś, co miało iść do innego klienta zupełnie.

**Janusz Bossak:** Może niewielkie ryzyko, ale.

**Marek Dziakowski:** Tak, bardziej teoretyczne bym powiedział, ale powiedzmy, że jest to jakieś dodatkowe pole, gdzie mogłoby coś takiego jakoś się zadziać z jakiegoś względu pomyłki takiej czy innej. Jest takie ryzyko powiedzmy. To jedna kwestia. Druga kwestia to też, że teraz już nie moglibyśmy powiedzieć, że gwarantujemy w 100 procentach, że nasze maile, nasza usługa na pewno działa, wychodzi. Bo powiedzmy, że serwer klienta pada i nagle będą: "A czemu mi maile nie przyszły? A czemu coś tam?" A dlaczego maile nie przychodzą? I teraz będzie do nas ruch kierowany pewnie od PGO: "Dlaczego nasze maile nie wyszły? Bo nie wiem, wskaźnik spamu macie taki albo coś tam". To jest kolejne miejsce, gdzie musimy reagować.

**Janusz Bossak:** Tak.

**Marek Dziakowski:** Także.

**Janusz Bossak:** Mi się pomysł ogólnie nie podoba.

**Marek Dziakowski:** Mi też nie.

**Janusz Bossak:** Nie chciałbym tego realizować, szczerze mówiąc. Więc albo to wyceniamy bardzo, bardzo drogo, jeżeli w ogóle, albo odpowiadałbym, że to nie leży w naszym interesie, żeby tak było. Ponieważ to jest zamknięta usługa, która coś robi. I tutaj można wrócić do tego pierwszego, tej pierwszej kwestii, czyli że my możemy personalizować adres mailowy. To wiesz o tym, że tak można robić?

**Marek Dziakowski:** Nie wiedziałem.

**Janusz Bossak:** Można jeszcze tak.

**Marek Dziakowski:** To może to załatwi sprawę.

**Janusz Bossak:** Nie pamiętam jak to się tam ustawia, ale chyba w ustawieniach organizacji. Nie pamiętam, dobra, nie chcę teraz zgadywać. Trzeba by pogrzebać w dokumentacji, ale na 100% tak było, bo Adecco ma tak, że właśnie podnoszone było to, że ci pracownicy tam czy kandydaci byli zdziwieni, że dostają jakiś TrustCenter, w ogóle nie wiedzieli o co chodzi.

**Marek Dziakowski:** Mhm.

**Janusz Bossak:** A tak to dostają mail z Adecco.

**Marek Dziakowski:** A to nie chodziło o SMS-y?

**Janusz Bossak:** Maile też.

**Marek Dziakowski:** Maile też.

**Janusz Bossak:** Tak, tak, tak.

**Marek Dziakowski:** Pamiętam, że SMS-y na pewno są z Adecco, ale maile też były.

**Janusz Bossak:** To trzeba to sprawdzić. Wydaje mi się, że jest taka funkcjonalność, więc trzeba to ogarnąć, bo możliwe, że to jest wystarczające dla tego tematu.

**Marek Dziakowski:** OK. Dobra. To jeżeli rzeczywiście tak jest, to tak tylko.

**Janusz Bossak:** Za to na spokojnie.

**Marek Dziakowski:** Nie bardzo.

**Janusz Bossak:** Kolejność tak jak ustaliliśmy – JRWA. Potem jak skończy się ten wątek, to się zajmij tym. To cena nie jest taka pilna, że to musi być dzisiaj.

**Marek Dziakowski:** Dobra.

**Janusz Bossak:** Ja po prostu wczoraj zobaczyłem, że jest. To przerzuciłem do ciebie, żeby nie zapomnieć.

**Marek Dziakowski:** Tak.

**Janusz Bossak:** Ale to jak zrobisz tam w poniedziałek czy wtorek jest OK. Najpierw trzeba tam trochę pogrzebać, poszukać, bo wydaje mi się, że ta opcja na nazywanie maila, jakiś tam sposób takiego aliasu robienia, jest zrobiona. To było robione, nie pamiętam, ale.

**Marek Dziakowski:** Dobra. Zerknę, to raczej nie jest jakoś głęboko zakopane. Tutaj też jest ta druga kwestia, widzę, że tam już pisze tak, tak. Jest kwestia.

**Janusz Bossak:** Ktoś wie, też była, chce tam pogadać. To czekam na ciebie, tutaj wciągniemy od razu.

**Marek Dziakowski:** Dobra, dobra. To jest kwestia z symbolami, bo klient ponoć chce mieć możliwość podzielić te jeszcze na dodatkowe kategorie, czyli nie tylko 4, tam jeszcze piąty poziom dodać. Pytanie, czy my to chcemy? W ramach tego rozwiązania JRWA też wliczyć, czy to ma być jakoś tam rozwiązane? Nie wiem z poziomu już samego AMODIT.

**Janusz Bossak:** Nie wiem. Dobra, Kamil, to mieliśmy akurat chwilę na temat wyceny odnośnie TrustCenter, ale widzę, że piszesz o tym. To cię wciągnęliśmy, ponieważ mają to, żeby już od razu było. Nagrywam jak zwykle, to transkrypcje robimy, więc będziemy mieli notatkę.

**Kamil Dubaniowski:** OK. Jestem. Jasne. Tak, nie wiem czy maks, żeby mnie chwilę też przed tym się spotkaliśmy. O to JRWA i temat jest taki, że nie wiem jak planować te podteczki, czyli chodzi o te nieruchomości już przysłowiowe. Czyli mamy nie wiem tam kontrolę przeciwpożarową i robię sobie w tym katalogu JRWA podteczkę na nieruchomość Poloneza i na nieruchomość tam jakąś inną. I teraz czy te podteczki mają być elementem struktury JRWA? Czyli odwoła, wskazuje OK. A podteczka w takim wypadku będzie po prostu czymś słownikiem.

**Janusz Bossak:** Nie, nie. Czy?

**Kamil Dubaniowski:** Rejestrem.

**Janusz Bossak:** Nie. Nie, to według mnie. Nie jestem tu ekspertem, ale z tego co ja tam wyczytałem, co napisałem ten kompendium i później w tych przypadkach użycia różnych, działa to w ten sposób, że jeżeli masz temat, powiedzmy te nieruchomości, zakładasz dla tej nieruchomości i w tej teczce dla nieruchomości zakładasz podteczki dla tych spraw? Bo normalna sytuacja jest taka, że zakładasz teczkę sprawy, która ma czteroczęściowy symbol i ją przyczepiasz do klasy JRWA. Tu mówimy o sytuacji takiej, że tworzysz teczkę sprawy. Ona ma symbol czteroznakowy i w niej tworzysz podteczkę sprawy, która ma symbol pięcioznakowy?

**Kamil Dubaniowski:** OK, to ja teraz od razu swoją – jak ja to rozumiałem, ja to rozumiałem patrząc na te filmiki z eZD RP, że jest katalog JRWA, nie wiem tam właśnie te wspomniane kontrole przeciwpożarowe. I teraz ja mogę sobie zaplanować w tym podkatalog Poloneza tam 90 i jakieś inne nieruchomości. I teraz ja do tych podkatalogów mogę wpinać teczki spraw dotyczące tych nieruchomości. Ja to tak rozumiem, czyli jest może źle, ale tak, gdzieś tam oglądając te filmiki, bo oni dodają ten element. Na tym nagraniu tuż pod klasę, klasę JRWA, czyli kończą ci się klasy JRWA i oni tam mają normalnie "Dodaj podkatalog" czy "podteczkę" jak to sobie tam nazywają. I to jest ten element, który ja myślałem, że jest elementem struktury właśnie tego JRWA, ale takim pomijanym w docelowym. Gdzieś tam nie wiem jak przekazują to już do archiwów państwowych, no to te podteczki to są tylko dla nich, żeby później łatwo znaleźć właśnie sprawy dotyczące tej konkretnej nieruchomości. Ale to jest pod, jakby nad sprawą, a ty to jakby rezerwujesz teraz, że to jest element pod sprawą.

**Janusz Bossak:** Nie chcę być tutaj wyrocznią, bo kompletnie się na tym nie znam. To znaczy bazuję na tym co prze tworzyłem umysłowo, jeśli chodzi o to, i przeszedłem tam różne fazy rozumienia tego. Istnieje coś takiego, co jest już poza właściwie metodyką JRWA, a związane się właśnie z tym, że robimy to elektronicznie. To jest to, że możesz sobie raportować na przykład wszystko, co dotyczy nieruchomości, ale rejestrować w innych gałązkach JRWA. Przykład: masz gałązkę JRWA pokontrolne i to nie są kontrole, tylko nieruchomości. To są po prostu kontrole. Masz kontrolę ZUS-owską, kontrolę nieruchomości i tak dalej. I teraz jak założysz teczkę kontroli nieruchomości, to poza strukturą, poza tą metodyką JRWA możesz tam elektronicznie dodać symbol tej nieruchomości i dla własnej wygody, poza całym tym modelem JRWA, możesz sobie raportować teraz kontrolę dotyczącą tej nieruchomości, jakieś tam badania techniczne dotyczące tej nieruchomości, zlecenie remontu tej nieruchomości. Ale samą tę sprawę tego remontu, tego badania i tak dalej może w różnych miejscach całej struktury JRWA – tam gdzie są badania, tam gdzie są remonty, tam gdzie coś. I to jest jedna metoda. Czyli masz to rozproszone w różnych miejscach, ale ponieważ jest to w systemie elektronicznym, to jest łatwość zrobienia zestawienia danych dla danej nieruchomości. Ja to tak rozumiem i to jest poza metodyką. Druga metoda z wykorzystaniem tych podteczek jest taka, że właśnie w katalogu nieruchomości zakładasz teczkę dla nieruchomości i w niej rejestrujesz podteczki tej kontroli, tego badania, tego remontu. Nie robisz tego gdzieś tam w strukturze, tylko tutaj. Tak, czyli masz taki pudełko czy karton nieruchomości i w niej siedzą wszystkie jakieś kwestie związane z daną nieruchomością i wtedy nie siedzą gdzieś indziej. Ja tak rozumiem. Tak gdzieś z tych rozporządzeń innych rzeczy wynika, że sprawa może mieć tylko jedno miejsce w JRWA. Czyli tak patrząc analogowo, czyli jak masz jakiś papier, kartkę, to może się wpiąć tylko w jedno miejsce, w jednej teczce. I teraz jest kwestia tego, jak sobie to zorganizujesz. Ja rozumiem, że są te 2 metody: albo rozrzucasz to po różnych miejscach, gdzie są te kontrole, badania, remonty, jakieś inne rzeczy. I to jest fajne jak masz jedną siedzibę – już trzymamy się tych nieruchomości, ale to może dotyczyć innych zagadnień. Jak masz jeden taki podmiot, no to co za różnica gdzie to siedzi? Tak patrzę już kontrolę, no to tam były kontrole. Albo możesz to organizować właśnie przez te teczki w ramach nieruchomości, które będą miały swoje podteczki dla poszczególnych spraw. I tyle. Ja tak to rozumiem, to jest moja wiedza na ten moment, czy ona jest właściwa? Nie wiem. Takie jest moje rozumienie tego zagadnienia. Dobrze by było, jakbyśmy się jakiegoś eksperta zapytali, jakiegoś archiwisty. Nie teraz, im się już nie domin. Nie, był taki archiwista, pamiętam tam gdzie pracowałem, tam się jego zapytam. Nie, musielibyśmy mieć naprawdę jakiegoś. Albo trzeba zadzwonić do jakiegoś archiwisty? Może ktoś nam poradzi, coś. Nie może do archiwum państwowego trzeba zadzwonić i się poprosić o eksperta, poradę. Nie wiem, by się upewnić.

**Kamil Dubaniowski:** A jeszcze bo wiem, że te podteczki tydzień wyłapałeś w tej strukturze LOT. Pamiętam, że to było jaki to dokument, bo w tej oficjalnej strukturze co oni tam wpada się przesłali, no to się kończy na poziomie czwartym. A te podteczki to dziś było opisane, że oni używają czy.

**Janusz Bossak:** To jest, jeżeli jest gdziekolwiek, to jest w tej kolumnie uwagi przy tej kategorii czy tej klasie?

**Kamil Dubaniowski:** Czwartej. Dobra, dobra, to jeszcze to przejrzę, OK, żeby była to.

**Janusz Bossak:** Tam w uwagach powinno być napisane coś w stylu, że dla nieruchomości prowadzi się odrębne tam teczki dla nieruchomości, coś takiego.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Ja to sobie wrzuciłem wszystko do tego, do któregoś tam czata do Gemini i chyba wszystkie te dokumenty. Jak, jako chyba nawet do czata GPT i tak jako projekt i się jego pytałem. To jest najlepsze rozwiązanie, bo tak to możesz nam się naczytać tego. Ja mam nawet tego czata, możemy go tutaj zaraz odpytać. Czy on będzie GPT? Mam taki projekt LOT, to pokażę. I to jest część betty? O i tu mam JRWA LOT. I tu mam te podpięte pliki i teraz się możemy do nich pytać, tak? Czyli do. Mówię ci, znika. Bo inaczej jak. Tak jak. Jak? Błąd. Zobaczymy co wymyśli coś sensownego. Zastaną książki, instrukcji, instrukcji archiwalne, że dokumentacja nieruchomości było się być klasyfikowana według klasyfikacji, torba z grupy 68, gospodarka, gospodarowanie nieruchomościami. Dla nieruchomości prowadzi się odrębną teczkę zgodnie z zasadą podziału na sprawy i klasy. Wewnątrz akt wykazu akt z teczki muszą być opisywane i przechowywane zgodnie z instrukcją kancelaryjną. Układach sygnatury, daty. Po zakończeniu sprawy akta trafiają po upływie 2 lat do archiwum zakładowego. Grupa 68. Gospodarowanie nieruchomościami. Najważniejszych klasy 680 wyjaśnienia, interpretacje, opinie, akty prawne gospodarowania, wiedza o nieruchomościach i aktualizacja. 6 8 1 0 ewidencja nieruchomości 6, 8 1 1. Państwowy jak tworzy się teczki nieruchomości w LOT to jest: Teczka nieruchomości to teczka aktowa, w której gromadzi się dokumenty naszej jednej konkretnej nieruchomości w ramach danej sprawy lub zestawu spraw powiązanych tematycznie. Dokumenty były grupowane według symbolu takiego mateczki, były układane w kolejności klasy JRWA. Struktura i zawartość teczki nieruchomości: każda teczka musi zawierać opis teczki, pełną nazwę, kategorie, tytuł teczki 6 8 1 0 ewidencja nieruchomości nieruchomość przy ulicy w Warszawie. A czyli tutaj się robi to w ten sposób, tak? Akta sprawy w kolejności numerów spraw oraz technologicznie. Dokumenty własności, zakup, dokumenty prawne. Czy dla jednej nieruchomości jest jedna teczka? Nie zawsze. Instrukcja kancelaryjna jasno wskazuje: teczkę zakłada się dla spraw prowadzonych w ramach jednej klasy JRWA. Jeśli dokumentacja jest obszerna lub dotyczy wielu spraw, możliwe są teczki wydzielone, zbiorcze lub wielotomowe. W ogóle jakieś nowe pojęcia. W praktyce nieruchomości przy ulicy X może mieć teczkę 68 10 ewidencja nieruchomości ulicy X. Czyli to widzisz, to jest trochę inaczej. Tak, znowu masz teczkę 6, 8 2 3 zakup nieruchomości, czyli to nie jest jakby jedna teczka nieruchomości.

**Kamil Dubaniowski:** Tak, dla mnie to to jest właśnie ten cudzysłowie i też jak ja dyskutowałem z czatem, to on mi to nazwał w ten sposób, że czasem określa się to jako sygnatury kancelaryjne, symbol teczki, lokalne rozszerzenie JRWA lub podteczki. To jest ten dodatkowy piąty poziom, czyli masz 6 8 10 to jest temat JRWA i teraz pod tym 6 8 10 możesz mieć ewidencję nieruchomości ulica X, ewidencję nieruchomości ulica Y. I wszystkie sprawy, które dotyczą ewidencji tej nieruchomości, a ich może być wiele, po prostu wpinasz do tej teczki. Czyli sprawy są w teczce, czyli jakby ta teczka to jest dodatkowy poziom JRWA nadrzędny nad sprawą. I może się okazać, że zamykasz ewidencję nieruchomości X, bo już więcej tam spraw nie ma. I jakby patrząc później na wszystkie sprawy w tych teczkach, czyli jeśli będziesz miał ewidencję nieruchomości X i Y, to wszystkie te sprawy mimo tego, że są dla ciebie skatalogowane w dodatkowych katalogach, no jak później przekazuje się do archiwum, no to one mają ten symbol 6 8, 10, tak, bo wszystkie dotyczą tego tematu ewidencji nieruchomości. A to, że ty sobie podzieliłeś sprawy na poszczególne nieruchomości dodatkowo, to jest już twoje udogodnienie.

**Janusz Bossak:** Ale to nie będzie 6 8 10 nie będzie tylko ewidencja nieruchomości X. Będziesz miał za chwilę 6 8 10 ewidencji nieruchomości Y.

**Kamil Dubaniowski:** Tak, to mi chodzi.

**Janusz Bossak:** Z dalej.

**Kamil Dubaniowski:** Tak, ale to ewidencja nieruchomości ulica X to jest już ja rozumiem, właśnie ta podteczka. I w tej podteczce możesz mieć różne sprawy, bo była tam jakaś jedna sprawa dotycząca ewidencji. Przyszło 5 pism w tej sprawie. Po 2 miesiącach odpaliła się kolejna sprawa związana z ewidencją nieruchomości przy ulicy X. Znowu to wpinasz jako nową sprawę. Tam będzie 10 innych dokumentów dotyczących tej ewidencji, ale wpada to w ten katalog ewidencji nieruchomości X. Wchodzisz tam i widzisz wszystkie sprawy dotyczące ewidencji nieruchomości X. W każdej sprawie możesz mieć po ich z dokumentów.

**Janusz Bossak:** Tak. Dobrze, ale jak chcesz teraz, gdybyś chciał przejrzeć historię nieruchomości X? To ona jest tutaj?

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Tutaj, tutaj, tutaj i jeszcze pewnie w 15 innych miejscach. I teraz.

**Kamil Dubaniowski:** Tak, tak, tak. Tak jest.

**Janusz Bossak:** To co mówiłem: elektronicznie to jest dość łatwe. Analogowo to jest tak, że w tytule jest tutaj adres i oczywiście możesz się pomylić, bo w tym tytule napiszesz Poloneza 93, to jest łatwo tak, ale ktoś się pomyli tak i jakoś tam z myślnikiem, bez myślnika napisze coś tam, coś tam, bo to jest tylko tekst, to nie jest żadna symbolika, to jest tekst, żeby człowiek umiał przeczytać, że to jest ewidencja nieruchomości Poloneza 93. A to jest ewidencja nieruchomości Poloneza 93. Elektronika wprowadza jeszcze dodatkową możliwość, że możemy mieć w teczce symbol tej nieruchomości, którą w AMODIT będziemy używać. I dzięki temu możesz teraz zrobić raport pokazujący wszystkie tematy związane z nieruchomością i on sobie wyszuka, żeby tu była jakaś sprawa w tej teczce według chronologii, nawet tak będzie mógł to zrobić. To będzie miał daty. I że był najpierw zakup nieruchomości, potem było coś tam, potem było tutaj podział, potem był najem, tam młode Werner, różne rzeczy się działy różnych tych teczkach, o których tutaj mówimy, czy w podteczkach tych teczek. Ale dzięki temu, że mamy to elektronicznie, to możemy to łatwo zebrać.

**Kamil Dubaniowski:** Mhm. Dobra, to ja bym zapytał teraz z tego twojego, jeśli mam całą dokumentację, czy on może ty kojarzysz, czy są inne przykłady niż to nieruchomości, czy oni tak mają więcej? Bo jak to dotyczy tylko nieruchomości? To to jest żaden problem, bo spodziewałem się, że mają tych nieruchomości skończoną ilość. Twój sposób wtedy byłby czymś, co spełni wymagania nawet lepiej. A w ogóle nie musimy iść w te podteczki takie w rozumieniu JRWA, bo to po prostu będzie: mam sprawę, no to muszę, jeśli wskazałem, że dotyczy nieruchomości, to muszę wskazać w dodatkowym polu jakiej nieruchomości. I to już może być zwykły słownik. Tak, nie muszę tego w żaden sposób gdzieś tam.

**Janusz Bossak:** Jedna klasa równa się jedna teczka JRWA. Podteczki sprawach kadrowych, ale kadrowe to są osobne tematem.

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** Do teczki w komisjach i zespołach, klasa trzecia, komisja BHP protokoły 2024. Tak, na każdej komisji, to dobrze, to robisz komisja BHP protokoły 2024 i w środek wpinasz. Tylko właśnie dla mnie to jest komisja BHP protokoły 2024 to jest teczka czteroznakowa. W środku masz teczki pięcioznakowe związane z jakimiś sprawami tych komisji? Chyba że ich tam nie ma dużo. Wtedy po prostu walisz wszystko, czyli bezpośrednio już tę naszą AMODIT-ową sprawę wpinasz w tę teczkę. Tak i to nie jest wtedy ona nie ma struktury teczki i podteczki. Tylko jeżeli będzie 50 spraw dotyczących protokołów BHP, to 50 spraw będzie w tej teczce "Komisja BHP protokoły 2024" i to jest teczka sprawy. Tak i może już mieć drugą teczkę sprawy, która się nazywa też, widzisz, pod pod gałązką 0 0 3 nazywa się "Komisja rekrutacyjna postępowania 2024" i wtedy, jak masz dokument dotyczący komisji rekrutacyjnej, to wpinasz do tej teczki. I nie robisz podteczek do tego. Natomiast ja tak rozumiem, że jeżeli to byłoby na tyle wewnątrz jeszcze tego złożone, pomożesz o ile? Ta instrukcja kancelaryjna przewiduje zakładać podteczki dla takiej teczki. Bo ja tak rozumiałem te podteczki dla nieruchomości, czyli jest jakaś. Nie tak jak oni tutaj napisali, u nich jest tak nie. Gotując relację między teczką nieruchomość. Problem właśnie to jest klucz do młodych piłkarzy. Dokument znajduje się wewnątrz sprawy, a AMODIT tak, sprawa AMODIT-owa jest jedynym poziomem niżej niż teczka JRWA, ponieważ teczka grupuje wiele spraw w jednej sprawie, a AMODIT może znajdować się wiele dokumentów. Konsekwencji, teczka nieruchomości to jest grupa spraw, a AMODIT o tym samym symbolu JRWA. Przykład: sprawa AMODIT zakup działki idzie do klasy 6 8 2 3. Aktualizacja ewidencji działki idzie do klasy 6 8 10. To jest tutaj każda z tych spraw trafia po zakończeniu do swojej teczki JRWA. Rekomendowana struktura teczek nieruchomości dla LOT w AMODIT, aby zachować zgodność: pole symbolizował obowiązkowy w sprawach dotyczących nieruchomości, pole identyfikator. To właśnie to jest to nie nasz elektroniczny identyfikator nieruchomości, nie mający nic wspólnego z JRWA. To jest dodatkowe pole, nie? Na przykład numer księgi wieczystej, adres, identyfikator, jakiś wewnętrzny LOT, automatyczne grupowanie spraw widokach. Właśnie to jest, ale widokach to jest właśnie to, co mówię, czyli wrzucasz do różnych tych kategorii czy klas? Ale widoku potem grupuje sobie nieruchomość Poloneza 93. Tak i obojętnie gdzie ona tam siedzi. Tak, czyli teczki nieruchomości w LOT muszą być prowadzone w klasach 68 takich. Dla każdej nieruchomości prowadzi się odrębne teczki po jednej dla każdej klasy JRWA. Właśnie to jest to, to. To jest kluczowe zdanie. Bo ja byłem ciągle przekonany, że prowadzi się jedną teczkę dla nieruchomości. Ale to zobacz, tu jest: dla każdej nieruchomości prowadzi się odrębne teczki po jednej dla każdej klasy JRWA. Czyli generalnie jest wiele teczek nieruchomości.

**Kamil Dubaniowski:** Tak, w zależności od klasy JRWA. Tak może być teczka właśnie w tej w tematach przeciwpożarowych może być teczka, tam nie wiem, jakiś innych tematach kontroli. Dla każdej z tych klas JRWA tam robisz teczkę nieruchomości. I zbierasz sprawy, które dotyczą tej klasy dla tej nieruchomości.

**Janusz Bossak:** Dobrze. To ja mam takie właśnie kompendium wiedzy. Tak, czerpię z tego tutaj mam zrobionego tego, dane te dokumenty. I tutaj dodałem ten jednolity rzeczowy wykaz akt, wszystkie te dokumenty z LOT, nie takie instrukcja i rozporządzenie, tylko tyle. I on na podstawie tego go tutaj, jak powiem, odpytuje. Także tyle mogę powiedzieć. Nie wiem, to jak powiedziałem, nie jestem jakby wyrocznią w tej sprawie, bo nie mam żadnej praktyki. To znaczy to są moje domysły na podstawie tutaj analizy takiej własnej analizy za pomocą tego czata. Ale jak to jest naprawdę, tak żeby mieć na 100% pewności, że trzeba się kogoś zapytać? Albo znaczy już mniej więcej wiemy, tylko może potwierdzić tak, nawet zadając wprost pytanie w LOT, jak oni to robią tej chwili. Tak jakoś robią, nie papierową, chyba że nie prowadzą tego. Ja też byłam w ogóle nie mają zapisane, ale nie prowadzą lub.

**Kamil Dubaniowski:** Ja jeszcze zanim zadamy to pytanie, podeślę wam, żebyście wiedzieli na czym ja bazowałem. To fragment nagrania z instrukcji kancelaryjnej jest tego JRWA z eZD RP, jak oni to robią. To jest w skrócie powiem wam, bo tam więcej jest chyba 7 minut przed tym zrobiłem, który wam wyślę. Cały filmik omawiający JRWA to jest filmik, który pokazuje jak zarządza się strukturą JRWA w tym eZD RP. Czy to jest widok administratora, który ma zadanie, nie wiem, wprowadzić nowy katalog, nową klasę, usunąć jakąś klasę. I pokażę wam tę część dotyczącą podteczek za chwilkę, ale to już podeślę po spotkaniu. I najwyżej jak wyciągnie jest to jakieś nowe wnioski, to się złapiemy jeszcze raz. Bo ja cały czas jednak nawet patrząc na to nagranie, rozumiem to tak, że te podteczki dodaje się jako element, jakby taki dodatkowy do struktury JRWA. I to był trochę ten zakres Marka, a jak chcemy inaczej, że to będzie po prostu jakiś tam element wybieralny w polu typu, nie wiem, słownik, odnośnik do właśnie tej konkretnej nieruchomości czy czegokolwiek innego. To też musimy to teraz chyba postanowić, żebyśmy to przekazali na wdrożenia, że tak będą musieli robić, tak, że my kończymy JRWA na poziomie czwartym. A jak do tego mają być jakieś tematycznie jeszcze prowadzone podteczki, no to to już będzie, nie wiem, rejestry, słownik, czy jakkolwiek inaczej to widzi.

**Janusz Bossak:** Czy czy nie, to to powinno być? Według mnie to powinna być, to powinien być proces, który się tam załóżmy nazywa "Teczka JRWA".

**Kamil Dubaniowski:** Mhm.

**Janusz Bossak:** I on wtedy będzie miał ten czteroznakowy symbol. I albo będzie osobny proces, który się będzie nazywał "Podteczka JRWA", który będzie miał tę właściwość, że będzie nadawał pięcioznakowe symbol. Albo jeżeli chcą bardziej komplikować sobie, no to to może być nadal ta sama teczka JRWA, tylko użyta jakby na poziomie, że wie, że jest w teczce JRWA, to już sama dostaje ten pięcioznakowy symbol. Więc pytanie takie wdrożeniowe: która rozwiązanie jest łatwiejsze? Czy lepiej mieć 2 procesy? Jeden proces na podteczki, drugi proces na teczki JRWA i odpowiednio do teczek lub podteczek wpinać te nasze sprawy AMODIT-owe?

**Marek Dziakowski:** Czyli wtedy każda sprawa w teczce musiałaby mieć ręcznie wybierany z tego pola, jaki ma symbol. Tak.

**Janusz Bossak:** Znaczy każda sprawa, tak. Na razie zapomnijmy na chwilę o podteczkach, tak?

**Marek Dziakowski:** Mhm.

**Kamil Dubaniowski:** Czy Januszem, ja też, bo ja już trochę się tak na tę nomenklaturę jest, d przestawiłem. Teczka to jest dla ciebie w rozumieniu AMODIT sprawa, tak brzmi to dobrze rozumiał? Bo sprawa w rozumieniu AMODIT to jest zbiór dokumentów dotyczących jednego tematu. To jest sprawa i ty to nazywasz teczką.

**Janusz Bossak:** Też. Bo to się tak nazywa, więc sprawa czy teczka, tak.

**Kamil Dubaniowski:** Sprawa, oni to jakby tak, czyli sprawa, nie wiem, jest jakieś kontrole w nieruchomości i wokół tego było 10 pism różnych, tak, coś tam zostaliśmy straży pożarnej, coś tam dostaliśmy z sanepidu, coś tam dostaliśmy skądś tam i to jest jedna sprawa kontroli tej nieruchomości w jakimś tam temacie. To jest teczkę.

**Janusz Bossak:** Tak, ja tak nazwałem to teczką, żeby mieć konsultantom dać wyraźny sygnał, że to nie jest sprawa AMODIT-owa, żeby nie mylili sprawy AMODIT-owej ze sprawą JRWA. Tak, możemy to nazwać sprawą JRWA.

**Kamil Dubaniowski:** Tak, sprawa JRWA. Oni taką też nomenklaturę podali tam w opisie analizy: sprawa AMODIT, sprawa JRWA, bo niestety nieszczęśliwie to się nazywa sprawą. OK, więc ja teraz trochę lepiej to rozumiem.

**Janusz Bossak:** Teraz wracając do pytania Marka: sprawa JRWA, czyli to co ja nazywam teczką JRWA, ta sprawa JRWA musi otrzymać, znaczy musi być przypisana do klasy JRWA. Klasa JRWA to jest to, co ty właśnie masz tam robić, czyli ten nasz taki słownik tych, te tych czteroznakowy słownik, tak od zera, znaczy od jednego znaku do 4 znaków. Masz klasę i na końcu tej ostatnia klasa, gdzieś tam każdej gałąź JRWA ma wtedy przypisaną kategorię, taki walną, daty tam obowiązywania i będzie miała po naszej stronie również jakieś kwestie związane z uprawnieniami. Tak w LOT może to będą mniej istotne, ale jednak.

**Marek Dziakowski:** Czyli wykluczamy możliwość piątej kategorii, ewentualnie podziału.

**Janusz Bossak:** Nie ma, to nie ma takiego czegoś, znaczy.

**Marek Dziakowski:** OK, czyli.

**Kamil Dubaniowski:** Właśnie dobra i teraz teraz byśmy już rozumiał czym znaczy, jak już ustaliliśmy to nazewnictwo, o czym ja mówiłem, bo według mnie może być ten piąty poziom i zaraz wam to pokażę na tym nagraniu i to jest właśnie ten poziom. Tak, to jest kolejna taka podklasa, czyli masz JRWA tam 0, 0, 0, 7 i w ramach tego 0 0 0 7 możesz sobie zrobić, nie wiem, 10 podklas i każda z tych podklas dotyczy jednej nieruchomości, czyli masz nieruchomość A. I teraz te nieruchomość A możesz wpinać kolejne w tej Twojej nomenklaturze teczki sprawy JRWA, czyli w ramach nieruchomości A toczyła się w tym roku taka sprawa, tam było 10 dokumentów, toczyła się kolejna sprawa, tam było 15 dokumentów, kolejna sprawa. I ona wszystkie te sprawy dotyczyły tej klasy JRWA tej nieruchomości. I dopiero pod tą nieruchomością są sprawy, które jej dotyczyły. Ja tak rozumiem, to po tym nagraniu z eZD RP. Czyli że tworzysz sobie taki dodatkowy, nie wynikający już z instrukcji kancelaryjnej, jest przepisów poziom w tym JRWA, żeby sprawy JRWA toczące się w tej klasie już porządkować sobie tak po swojemu, żeby łatwo je później znaleźć. Wchodzisz w klasę 0, 0 7 i nie masz tam zbioru spraw JRWA, które dotyczyły wszystkich nieruchomości, tylko masz te sprawy podzielone na poszczególne nieruchomości. Chodzisz sobie do środka i widzisz sprawy JRWA, które toczyły się w obrębie tej nieruchomości w tej klasie JRWA. I to też jest zaznaczone jasno, że później jak przekażesz to do archiwum, to ich nie interesuje, że ty sobie to podzieliłeś dodatkowo dla swojego ułatwienia, żeby widzieć nieruchomości w tej klasie jako osobne. Masz przekazać to zgodnie z tym, jak sprawy były zakładane. Numeracja ma być spójna dla całej klasy JRWA, a to, że sobie to podzieliłeś na dodatkowe katalogi, dodatkowe takie podklasy, żeby widzieć, że te sprawy dotyczyły tej nieruchomości, to jest już twoje ułatwienie. Możesz, nie musisz tego robić.

**Janusz Bossak:** Rozumiem. Wielokrotnie w różnych momentach dyskusji z tym czatem on podkreślał, że JRWA jest normatywny, podlega ustawie i rozporządzeniu i tu nie ma pola na własną interpretację. Więc nie wiem, czy ten sposób, który podałeś, który w tym eZD RP zrobili, czy on jest prawnie dopuszczalny. Tak, widocznie ktoś znalazł jakąś taką trochę lukę w moim przekonaniu. Ten piąty poziom to to i to jest w rozporządzeniu. To jest właśnie to, że możesz prowadzić teczki i podteczki. I to jest to, jakby to nie przykleja się do struktury do tych klas JRWA, że to jest jakaś jeszcze podklasa. Tylko możesz prowadzić teczkę w tej klasie, trzy czy czteroznakową i tak, powiedzmy, że cztero, bo mówimy o tym, że jest jakiś piąty symbol jeszcze. Tak możesz prowadzić teczkę. Ta teczka ma swój numer i teraz w ramach tej teczki możesz mieć te podteczki, które są pięcioznakowe. W tym momencie teczki spraw, tak, sprawy sprawy JRWA. Ta sprawa, znaczy, że są 2 poziomy sprawy JRWA, żeby już mówić nomenklatury.

**Kamil Dubaniowski:** Spraw.

**Janusz Bossak:** Sprawę o niteczki, tak, czyli dla klasy czteroznakowej zakładam sprawę JRWA dla nieruchomości Poloneza 93 określonej klasie JRWA i koniec. I teraz w ramach tej sprawy JRWA mogę zakładać i to oni właśnie używają nomenklatury podteczki, bo tak jest w rozporządzeniu. Podteczka jest tak nazwane, czyli taką pod sprawę JRWA zakładasz. Jakby te, no ja dlatego nazywam to teczką, no jest teczka i podteczka. Teczka JRWA, a teraz podteczka JRWA. Czy ta sprawa JRWA, która zawiera jakieś tam sprawy AMODIT-owe, nie, ale tych spraw, tych teczek w tej teczce nieruchomości masz wiele. Jakaś powiedzmy to jest sprawa kontroli, tak, czyli teczka ta główna nazywa się "Kontrola na Poloneza 93". I masz tam: kontrola kominiarska sprawa, kontrola budowlana sprawa. Sprawa JRWA pięcioznakowa, a w niej dokumenty, na przykład pismo odnośnie kontroli, protokół tej kontroli, wezwanie do naprawienia czegoś tam i tak dalej. Ponowna kontrola jest to w ramach tej kontroli sprawa, inna sprawa, naprawa dachu na Poloneza 93, nie coś tam i robisz tutaj kolejne rzeczy. I dla mnie to są 2 poziomy naszej AMODIT-owej sprawy w rozumieniu, my ją sobie nazywamy sprawą JRWA, że ona reprezentuje ten poziom pierwszy i mamy drugi poziom. I tutaj właśnie mam wątpliwość, czy to powinno być to samo, czy to powinien być inny proces, ale ten drugi poziom ma pięcioznakowy symbol i dopiero do niego teraz dokładamy te nasze sprawy AMODIT-owe. A w 95 procentach innych gałązek JRWA, innych klas, bo mamy tylko sprawę tę czteroznakową i do niej już dokładamy te sprawy AMODIT-owe.

**Marek Dziakowski:** I teraz pytanie, w jaki sposób zrealizować tę platformę? Czy to ma być w ramach procesu?

**Kamil Dubaniowski:** Koncepcja Janusza wychodzi, to będzie proces, tak.

**Marek Dziakowski:** Tak, czyli proces sprawy powiązane. Tak.

**Janusz Bossak:** Ja bym tutaj inaczej, nawet gdyby było tak jak mówi Kamil, że można by tak zrobić, to nadal uważam, że to nie powinno być zapisywane w tej strukturze klasy JRWA.

**Marek Dziakowski:** Bo tutaj, jeżeli chodzi o procesy pod procesy, no to też robi się pytanie, w jaki sposób te widoki, czyli raporty były różnicowane. Łatwiej jest zrobić na podstawie słownika i gdzieś tam wyciągnąć, potem filtrować to niż połączyć 2 procesy.

**Janusz Bossak:** Nie wiem, jeden proces.

**Marek Dziakowski:** Jeżeli miały być pod folderem, to wtedy by były 2.

**Janusz Bossak:** Dlatego pod folderem jakoś nie wiem. Nie umiem się do tego odnieść, nie umiem tego zrozumieć. Na razie nie wyobrażam sobie czy nie umiem sobie wyobrazić tej struktury.

**Kamil Dubaniowski:** Czekacie jeszcze? Prawda umożliwia dodanie podteczki dla wybranej komórki organizacyjnej. Dzięki niej pracownicy komórki będą mogli dodawać szczegółowe zagadnienia do danej klasy. W pierwszej kolejności wskazujemy komórkę organizacyjną, następnie wprowadzamy nazwę podteczki oraz wybieramy rok, w którym będzie obowiązywać. Zobaczcie, ona zeszła tutaj do poziomu, mamy szóstkę, później 61 613 to jest klasa końcowa, czyli kończymy na trzeciej klasie.

**Marek Dziakowski:** Tak, tak.

**Janusz Bossak:** Tak.

**Marek Dziakowski:** Mhm.

**Kamil Dubaniowski:** Tu mogłaby być jeszcze klasa czwarta, na przykład 612. Ma jeszcze tam jakąś klasę czwartą i na tym kończy się JRWA. I ona teraz dodaje podteczkę, która dostaje symbol zakładane i podteczki tam 613 kropka 1. To mogłaby być tam nieruchomość Poloneza. I to się robi z poziomu.

**Janusz Bossak:** Ale jest to 613 kropka 1 kropka rok. Za chwilę tam będzie tak, no.

**Kamil Dubaniowski:** Tak. Podteczki nie są przenoszone na kolejny rok, powinny one zostać być stworzone niezwłocznie po rozpoczęciu nowego roku, zanim pracownicy rozpoczną zakładanie spraw. Zapamiętaj: system automatycznie wyświetli symbol dla zakładanej podteczki, wskazując pierwszy wolny numer w danej klasie w ramach wybranej komórki organizacyjnej. Utworzenie podteczki potwierdzamy przyciskiem zapisz. Po utworzeniu podteczki pojawi się ona na liście JRWA. Po jej zaznaczeniu dostępne są opcje edytuj i usuń. W trybie edycji można jedynie zmienić nazwę podteczki. Funkcja usuń zatwierdza usunięcie podteczki, przy czym system blokuje tę możliwość, jeśli w podteczce zarejestrowano jakąkolwiek sprawę. Warto dodać, że zarządzanie JRWA można przydzielić wybranemu użytkownikowi.

**Janusz Bossak:** Ale dla mnie to jest właśnie ten poziom. To według mnie to jest ten poziom, który ona tu pokazała. To jest poziom sprawy JRWA.

**Kamil Dubaniowski:** Sprawy.

**Janusz Bossak:** Sprawie AMODIT-owej sprawy.

**Kamil Dubaniowski:** Rejestrze, tak. Czy OK, wiecie, to o to mi chodziło, tak, żebyśmy podjęli tę decyzję, czy to jest kluczowa? To jest też ta informacja, że podteczki trzeba zakładać na każdy rok osobno. Nie są elementem przenoszącym walnym względem struktury JRWA, więc to jest jak najbardziej argument za tym, żeby tego nie ładować w tę strukturę JRWA, bo ona raczej jest stała, niezmienna. Nawet uważamy, że nie trzeba jej kopiować tak jak oni tu sugerują z roku na rok. A te podteczki jak najbardziej trzeba zakładać na każdy rok osobno.

**Janusz Bossak:** Manor.

**Kamil Dubaniowski:** Bo może jakaś nieruchomości już nie jest nasza albo doszła nowa?

**Janusz Bossak:** To jest wiedza odmienna od mojej wiedzy. To co ona powiedziała. Moja analiza wykazała, że to co ona powiedziała jest nieprawdą, znaczy, że zakłada się te teczki dla tej nieruchomości raz i więcej się ich nie zakłada. Nie przenosi się z roku na rok, nie tworzy się. Może ten eZD tak ma, ale nie ma takiej potrzeby prawnej wynikającej z rozporządzenia. Jak już raz założyłeś tę nieruchomość, teczkę, to wpinasz w środku podteczki, które w tamtym roku na przykład dwudziestym czwartym miały numerek 24 na końcu, ale do tej samej teczki głównej wpinasz sprawy teraz w roku 2025. I ta teczka jest jakby nie zamykana, jest ciągnie się. Ale mówię, naprawdę pogadajmy z jakimś archiwistą, bo nasza wiedza wynikająca z gadania sztuczną inteligencją może nas zaprowadzić na manowce.

**Kamil Dubaniowski:** Ale znaczy wiecie, dobra, to zróbmy tak: robimy czteropoziomową strukturę, bo robimy teraz. Jak dojdzie, że te podteczki są nieoptymalne, nie chcemy robić ich przez rejestr, to zrobimy po prostu i tak, no tabelę tak, która będzie miała link tak do do rodzica.

**Janusz Bossak:** To znaczy.

**Kamil Dubaniowski:** Tyle.

**Janusz Bossak:** Pokaż taki moment, gdzie nie jest mowa o podteczkach, tylko zakładaniu teczki w takich kategoriach, w których się zakłada teczki.

**Kamil Dubaniowski:** Teczki w sensie w rozumieniu sprawy JRWA.

**Janusz Bossak:** Sprawa jest. Już tak się przyzwyczaiłem w głowie, że to są teczki, żeby wciągać tam ciągle, że to są teczki. Przepraszam, ale dostałem krosa i muszę zjeść.

**Marek Dziakowski:** Takie zakładanie drugiej tabeli nie będzie zbyt wydajne, ale trzeba będzie łączyć wyniki z 2 tabel.

**Kamil Dubaniowski:** Zacznijmy od zakładanej na konkretnym piśmie, ale tworzonej po to, by kompletować dokumenty, które można będzie identyfikować po wspólnym znaku sprawy. W tym celu klikamy przycisk "Załóż sprawę" znajdujący się na ekranie startowym. Wyświetli się okno, w którym należy podać tytuł zakładanej sprawy oraz wskazać jej klasę z jednolitego rzeczowego wykazu akt. W skrócie JRWA zawiera on między innymi informacje o tym.

**Janusz Bossak:** I teraz zatrzymaj. I to to co teraz to się będzie działo, to jest to, co Marek będzie w tym naszym polu typ Odnośnik. To jest dokładnie ten moment.

**Kamil Dubaniowski:** Odnośnik. W jaki sposób będziesz prowadzić sprawę papierową czy elektronicznie oraz jaka jest jej kwalifikacja archiwalna. W systemie eZD RP możesz wybrać odpowiednią klasę, wpisując jej symbol, hasło lub ich fragment. Jeśli to zrobisz, zostaną wyświetlone pasujące pozycje. Wybieramy odpowiednią z listy. Jeśli nie znasz numeru lub nie wiesz, jak klasa została nazwana, możesz rozwinąć drzewo JRWA, który jest podzielone na klasy rzeczowe.

**Janusz Bossak:** To jest dokładnie to. Tego nie mamy tych.

**Kamil Dubaniowski:** Jak zobaczcie, że tu się da w ogóle zmieniać schematy. Nie wiem, to jest ten cały czas konflikt, który mamy, że u nich te schematy można importować i wręcz oni deklarują to, co przed chwilą padło, że schematy powinno się z roku na rok kopiować, utworzyć nowe, właściwie tak zamykać poprzedni i otwierać nowych. Tu jest wybór schematu, a tu dopiero jest. System wyświetli numer sprawy, rok i założenia, kategorię archiwalną oraz cały znak sprawy. Po sprawdzeniu tych danych klikamy przycisk zapisz. System przeniesie nas automatycznie do widoku sprawy. Zobacz, tak wygląda sprawa prowadzona papierowo zwana.

**Janusz Bossak:** I proste. I teraz zobacz ten numer DK z raz 2 3 4, tak. 4 części. I powiedz mi, czym to się różni ten numer od tego, co pokazywała ta pani tam chwilę wcześniej, tak, czyli miał oczywiście, że nie.

**Kamil Dubaniowski:** Nie miał, nie miał roku.

**Marek Dziakowski:** Miał rok.

**Kamil Dubaniowski:** Miał też, znaczy miał do podania, ale w numeracji tam nie widziałem, żeby się zapytać, to tak.

**Marek Dziakowski:** Tak. Było, było po zapisaniu się dopiero pojawił, tak?

**Kamil Dubaniowski:** OK.

**Janusz Bossak:** To jest ten poziom. I teraz według mnie, jeżeli tak założysz teczkę sprawę, to może ci przyjść na myśl, że jednak założysz podsprawy do tej sprawy. I według mnie tamten sposób i ten sposób w mojej głowie to jest tożsame. Bo efekt końcowy to jest taki sam obiekt. W naszym rozumieniu AMODIT-owym to będzie proces pod tytułem tam sprawa JRWA. I tu zostanie otworzone tak jak on pokazał ten człowiek, bo teraz mężczyzna mówił tak, a przedtem na tym drugim filmiku pani mówiła i pokazała zakładanie teczki dla nieruchomości. W moim przekonaniu powstanie dokładnie taki sam obiekt. Sprawa JRWA. Takie jest moje rozumienie tego, nie?

**Kamil Dubaniowski:** OK. Tyle, tak. To wtedy spada to na konsultantów. Może to być jeden proces. Właściwie jak zakładasz nową sprawę, to będzie pole do potencjalnie wskazania sprawy nadrzędnej, tę sprawę w rozumieniu JRWA. Czyli zakładam sprawę JRWA, uznaję, że to jest taka nadrzędna, która będzie kumulowała w sobie sprawę JRWA dotyczące tej nieruchomości. Więc jak będę później zakładał sprawę dotyczącą tej nieruchomości, no to będę musiał sprawę w sprawę nadrzędną nieruchomości wskazania.

**Janusz Bossak:** Dokładnie. My możemy sobie zrobić niezależnie to, że masz tam jakieś pole typu identyfikator nieruchomości i po prostu w sprawach tych JRWA, ale sprawach rozumieniu AMODIT-owych będziesz wskazywał tę nieruchomość. I tyle. I potem możesz sobie robić raport, co już jest, nie ma nic wspólnego z JRWA. Tak, po prostu możesz raportować o po tej nieruchomości, gdziekolwiek w jakiejkolwiek sprawie ta nieruchomość występuje. Bo właśnie jedną rzecz, to to jest dla mnie ciągle zagadką, że jeżeli w tych różnych klasach, to jak tutaj ten czat nam przed chwilą pokazywał, zakładam, mam 5 albo 10 nieruchomości, to co muszę bardzo się pilnować, żeby w klasie tam 0 6 80 moja nieruchomość Poloneza 93 była pod numerkiem jeden i w klasie 0 6 81 też, żeby była pod numerkiem jeden. I w klasie jeszcze jakieś też pod numerkiem jeden. Co może być trudne do utrzymania? Muszę dokładnie w takiej kolejności zakładać w każdej z tych klas i pamiętać, że tam założyłem trzecią. A jak rozumiesz nie. Więc żeby to było łatwiejsze, w moim przekonaniu, to sobie można założyć tę nieruchomość Poloneza 93 pod numerkiem jeden w klasie tam 0 6 80. I mieć symbol już na naszym nowym formularzu, że to jest nieruchomość Poloneza 93. A w innej klasie tam 0 6 81 założyć tę teczkę na Poloneza 93 pod numerkiem 2 czy 3 czy 5. Bo akurat tak się złożyło, że w takiej kolejności było zrobione, ale ona będzie oznaczona też polem na formularzu Poloneza 93. I wtedy będzie ci łatwo to kompletować, bo tak to oprócz nazwy w tytule nie wie, że to dotyczy Poloneza 93. To byłby jedyny wspólny element, tak kawałek nazwy, której też może się pomylić, bo jest zwykłym tekstem.

**Kamil Dubaniowski:** Ja wiem.

**Janusz Bossak:** Papierowo to działa, ale tak elektronicznie słabo nie.

**Kamil Dubaniowski:** Mhm. Potencjalnie tak patrząc na to, to moim rozumieniu, jeśli są klasy JRWA, czyli ten nasz trzeci, czwarty poziom, które od uznają, że wymagają dodatkowego przyporządkowania do jakiegoś właśnie obiektu, nie wiem elementu. Może po stronie tego nasze naszej klasy JRWA powinien być tylko taki czek, że tam wymagane przyporządkowanie dla konsultantów, żeby oni mogli dodać, że jeśli wpinasz coś do tej klasy, no to jest zasada, że w dodatkowym polu musisz jeszcze coś wybrać, czyli właśnie ten obiekt, czy cokolwiek innego, żeby oni mogli wtedy pokazać to pole dynamicznie jako obligatoryjne, że teraz przepis jeszcze obiekt, jak tam nieruchomości, cokolwiek innego, żeby jakby wyspecjalizować te klasy, które LOT wymaga, że żeby przyporządkować dodatkowo. Ale.

**Janusz Bossak:** Tak.

**Kamil Dubaniowski:** Bo to tak naprawdę wtedy mógłby być najprostszy słownik nieruchomości i tyle. Wybierasz klasę, zakładasz nową sprawę JRWA i wskazujesz do jakiej klasy tam, że dotyczy to kontroli, a dodatkowo w polu obok wybierasz ze słownika tę nieruchomość. I tyle. I później po tym możesz sobie właśnie pogrupować jakiś raport czy filtrować tak po tej konkretnej nieruchomości, zobaczyć wszystkie sprawy JRWA, które tej nieruchomości dotyczy.

**Janusz Bossak:** Dokładnie tak.

**Kamil Dubaniowski:** I to nawet nie musi być ten poziom jeszcze wyżej, że musisz założyć sprawę nadrzędną JRWA i później w niej zakładać sprawy podrzędnej JRWA, bo nie jest jeden poziom spraw JRWA, ale niektóre ze spraw JRWA mogą mieć dodatkową klasyfikację. Właśnie podział na te nieruchomości czy co tam jeszcze sobie dzieli LOT.

**Janusz Bossak:** Tak, ja mam takie wrażenie, że ten program tutaj ten eZD RP on został zrobiony przez archiwisty papierowego. Tak. I żeby innym archiwistą papierowym to było dla nich zrozumiałe, no to ona odzwierciedla tak naprawdę logikę papierową. A logika elektroniczna jest inna? Nie wiem, na ile rozporządzenie tego też aż tak bardzo nie analizowałem wpr. Władza zasady elektronicznej elektronicznego prowadzenia tego JRWA. Bo pamiętasz, że jak rozmawialiśmy o teczkach pracowniczych, to to była dość spora różnica między prowadzeniem w postaci papierowej a prowadzeniem w postaci elektronicznej. Chociażby numeracja. Zupełnie inaczej jest podejście w tej numeracji elektronicznej niż tutaj. Więc tu jesteśmy w takim stanie hybrydy jakiejś takiej, nie trochę taki, trochę takiej. I to, co powiedziałaś tu przed chwilą, to tak, no elektronicznie nie tak jest. Najlepiej byłoby w ogóle nie zakładać tych podteczek, tylko zakładać teczki i oznaczać w środku, że to dotyczy tej czy tamtej nieruchomości konieczne. Mi się tym nie przejmować, nie znaczy. Chodzi mi o to, że można prowadzić te dokumenty prościej.

**Kamil Dubaniowski:** Tak.

**Janusz Bossak:** Dzięki temu, że to jest robione elektronicznie, a potem troszkę już poza modelem JRWA sobie robić raporty, tak. Przypomniałaś mi, żebym nie zapomniał, bo chcę to wypowiedzieć też do później notatki. Jest jeszcze jeden temat, który musimy zaopiekować, który się nie tylko dotyczy tej kwestii, ale innych. To są raportowanie z pól typu Odnośnik. Czyli że jak, tak jak teraz możemy raportować z tabelki, czyli wybieram sobie tabelkę i mogę wybrać kolumny z tej tabelki. To samo musi dotyczyć pola Odnośnik, czyli jak wybiorę pole Odnośnik, że chcę, żeby się pojawiło na raporcie, to powinienem móc wybrać pola z tego procesu, na które wskazuje to pole Odnośnik. Rozumiecie?

**Kamil Dubaniowski:** Tak, wtedy by nie trzeba było kopiować tych danych na pojedyncze dokumenty.

**Janusz Bossak:** Dokładnie. I to według mnie to powinniśmy wpisać w ten projekt. I przy okazji tego JRWA to zrobić, bo to się pojawia bardzo często, nawet ostatnio też Mateusz Kołakowski o tym mówił. To jest uproszczenie, bardzo dużo uproszczenie tworzenia raportów.

**Kamil Dubaniowski:** Tylko, że te tym kontekście będzie odnosił do źródła zewnętrznego, więc jeszcze trochę inaczej.

**Janusz Bossak:** Nie, bo będziesz miał akta.

**Kamil Dubaniowski:** A sprawa, sprawa OK. Na aktach, na sprawę przekopujemy dane z JRWA, tak, a tam rozumiem.

**Janusz Bossak:** Sprawa JRWA i te sprawy AMODIT-owe. Jest to powiązanie ten poziom. I wtedy, jak będziesz chciał raportować ze sprawy JRWA, żebyś mógł pokazać te elementy ze tych spraw AMODIT-owych. Także to też trzeba będzie taką rzecz zaopiekować. Dobra, słuchajcie, bo tam mieliśmy chyba mieć jakiś tej chwili już.

**Kamil Dubaniowski:** 3 nas dwunasta, tak trzynaste.

**Janusz Bossak:** Jest tak od pół godziny planowanie sprintu nam ciebie.

**Kamil Dubaniowski:** Planowanie. Dobra, dobra, to Marek dla ciebie jasne, tak, czteropoziomowe JRWA i na tym kończy.

**Marek Dziakowski:** Tak, tak.

**Janusz Bossak:** Teraz tutaj ci przygotuję z tego notatkę, jak się tylko wygeneruje, to ci dam.

**Marek Dziakowski:** Tak. OK, to część rozumiem, tam reszta jak będę się jakieś pytanie pojawiały już co do samego pola i użytkowaniu na to.

**Kamil Dubaniowski:** Tam też widzieliście, że oni mają dwa widoki później. Jak wybierasz katalogu JRWA, to możesz po prostu takim polem, a możesz też zobaczyć całe drzewo.

**Marek Dziakowski:** Później.

**Kamil Dubaniowski:** I spodziewam się, że w kolejnym, nie w tym MVP, w kolejnym kroku mogą na nas to wymusić, bo LOT po prostu ludzie nie znają struktury JRWA, bo jak się okazało, wspominałem wczoraj, oni dopiero zaczynają z tym pracować. Więc takie drzewo będzie dla nich spodziewał się wygodniejsze. Taka lista wyboru, gdzie wpisujesz symbol i my podpowiadamy, jest dla kogoś, który pewnie trochę z tym popracował, wie jakiej klasy obsługuje i zna je na pamięć już. A przy pierwszych takich klasyfikacjach to oni będą mieli pewnie problem, będą chcieli widzieć całe drzewo. Ale dobra, to jeszcze będziemy.

**Janusz Bossak:** Ale to później. Dobra, dzięki bardzo.


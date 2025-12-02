**Data spotkania:** 27 listopada 2025, 09:09 - część 4

---

**[Janusz Bossak]:** A może tak zrobić? Ja bym chciał może wykorzystać tego Piotra i o tym JRWA porozmawiać.

**[Damian Kaminski]:** No właśnie.

**[Lukasz Bott]:** Ja się rozłączam, bo mam spotkanie za chwilę.

**[Janusz Bossak]:** Dobra.

**[Anna Skupinska]:** Ja też o innych rzeczy. No cześć.

**[Janusz Bossak]:** Hej.

**[Damian Kaminski]:** Kamil ty preferujesz temat?

**[Kamil Dubaniowski]:** Tak, tylko ja mam 9 minut, bo LOT mam o jedenastej. Tam to tak. Tak, wie wszystko, to ja nie wiem komu może lepiej Marka od razu dzwonić, jeśli jego tutaj przewidujemy, że przejmie temat. Tak robimy czy.

**[Damian Kaminski]:** No to tak, tak, jeśli Piotr wszystko wie, tylko podsumujmy to.

**[Kamil Dubaniowski]:** Tak, no znaczy, Piotrek przekażę tak bardziej o to chodzi, żeby Marek, no tak zakres i pewnie powinni się też chłopaki spotkać się wszystkie nie wiem czy z nami czy są oddzielnie. Doprecyzować szczegóły teraz to zdąży w te 9 minut co najwyżej wdrożyć. O co chodzi? Jest.

**[Marek Dziakowski]:** Cześć.

**[Kamil Dubaniowski]:** Cześć, to może wtedy Marek chwilę?

**[Marek Dziakowski]:** Tak, tak, oddzwoń.

**[Kamil Dubaniowski]:** Temat na przyszły sprint już raczej, bo Piotr tam będzie nieobecny przez pierwsze dni sprintu, a jest to jakby element wdrożenia, które realizujemy w LOT.

**[Marek Dziakowski]:** No.

**[Kamil Dubaniowski]:** Temat jednolitego rzeczowego wykazu akt i obserwuja w skrócie biznesowo. Temat polega na tym, że. Użytkownik musi wybrać pewną klasyfikację na formularzu i tyle, jakby taki bardziej złożony słownik ze strukturą. Zależności i plan jest taki, żeby zrobić to na zasadzie działania takiego jak działa GUS TERYT, nie wiem czy się orientujesz w tym dosyć specyficznym słowniku, ale jest to słownik, który działa nieco inaczej niż źródło zewnętrzne, tak, które działa w polu odnośnik do źródła zewnętrznego na formularzu.

**[Piotr Buczkowski]:** Jest to źródło zewnętrzne.

**[Kamil Dubaniowski]:** Tutaj akurat w tym GUS TERYT jak rozumiem, my sięgamy po dane gdzieś tam na zewnątrz, natomiast w tym JRWA to będzie po prostu sięganie bezpośrednio do tabeli AMODIT, no bo dane będą uzupełniane przez klienta to już tak wyła, każdy ma inne struktury tych. W kategorii oferta była mają inną zależności, mogą być inne i potrzeb. Wiemy odtworzyć de facto to, jak działa GUS TERYT. Przełożyć to na te schematy i odwoła.

**[Marek Dziakowski]:** Czyli no OK. Czyli funkcjonalności od strony UI mają być takie same jak ma GUS TERYT, a jeżeli chodzi o uzupełnianie danych, no to tutaj się tym nie przejmujemy. Nie potrzebujemy tego jakoś tam.

**[Piotr Buczkowski]:** Znaczy.

**[Marek Dziakowski]:** Uzupełnić automatycznie.

**[Piotr Buczkowski]:** Ogólnie to nie to nie jest, mimo że to jest jakaś tam drzewko, to nie jest wybieranie z drzewka, to jest wybieranie z listy, pojedyncza jest wyszukiwaniem, tak.

**[Damian Kaminski]:** Tylko. Jak wy to powiedzieliście, to? Z mojej perspektywy to nie rozumiem koncepcji działać jak GUS TERYT, jakim zakresie czy Marek rozumiesz.

**[Piotr Buczkowski]:** Już pokazuje, już pokazuje.

**[Marek Dziakowski]:** Nie, gdzieś tam miałem krótką styczność tylko z GUS TERYT.

**[Damian Kaminski]:** Bo.

**[Marek Dziakowski]:** Wiem, że jest.

**[Piotr Buczkowski]:** Definiujesz definiujesz klasę. I o ten własne source. O implementując o taki. Pakiet interfejs. Projektujesz źródło danych jako te 5. Tutaj jeszcze trwał tam jakieś tam. No w JSON chyba tak co będzie zapisywane w. Jaka wartość będzie zapisywana w polu tekstowym tak wybraniu? Niż.

**[Marek Dziakowski]:** No.

**[Piotr Buczkowski]:** No i tutaj sobie co sobie tutaj czujesz, to to twoje.

**[Marek Dziakowski]:** K sekundka tylko, bo coś ktoś dzwoni, sekundka nawracam.

**[Damian Kaminski]:** Czyli funkcjonalnie będzie można szukać po dowolnej wartości? Tak, nie początku.

**[Piotr Buczkowski]:** Po tym, co po tym co zaprojektujesz po tym co Marek, czy ktoś tam za zaprogramuje.

**[Damian Kaminski]:** Ta programuje czyli nie konfiguracyjny, nie tylko.

**[Kamil Dubaniowski]:** Czy wiecie możemy, no, bo potem będziesz szukał, będziesz szukał po symbolu, będziesz szukał po nazwie.

**[Damian Kaminski]:** Albo po nazwie, no bo tych 2 rzeczach.

**[Piotr Buczkowski]:** W tym momencie szuka, szuka po, może nie po wszystkim, tak, większość ciepło.

**[Kamil Dubaniowski]:** No i.

**[Damian Kaminski]:** Tu mamy z założenia 2 pola, tak, mamy pole symbol jako ID biznesowe. I nazwę jako opis tego symbolu.

**[Piotr Buczkowski]:** No tylko tutaj się odwołuje gdzieś tam tak. Web serwisu, żeby ta i tam przekazuje tak co co szukasz, no tutaj będzie sam w sobie tych tabelach lokalnych szukał.

**[Marek Dziakowski]:** Już jestem.

**[Janusz Bossak]:** Tak, bo tutaj nie będzie tego tak GUS TERYT to jest zasilanie z zewnątrz.

**[Marek Dziakowski]:** Tak to kojarzy.

**[Janusz Bossak]:** A tutaj nie ma tego zasilania z zewnątrz, po prostu my raz zasilimy te tabelki.

**[Marek Dziakowski]:** No.

**[Janusz Bossak]:** Tą strukturą ter była później dorobimy do tego interfejs użytkownika, który będzie to można robić, ale na razie zakładamy, że ta tabela zostaną jednorazowo poziomu bazy danych uzupełnione, a celem tej operacji jest umożliwienie. Nie wiem kto to pokazuje w tej chwili, ale tak jakby na na sprawie pokazać jak działa GUS TERYT.

**[Damian Kaminski]:** Piotr.

**[Piotr Buczkowski]:** Ja.

**[Janusz Bossak]:** Chodzi o to, że jest pole, które jest polem odnośnik do źródła zewnętrznego. Wybrany źródłem zewnętrznym jest w tym przypadku GUS TERYT, a dlatego JRWA to będzie wybranym źródłem zewnętrznym JRWA trzeba takie przygotować.

**[Marek Dziakowski]:** No.

**[Janusz Bossak]:** I to się zachowuje wtedy w ten sposób, że w tym polu odnośnik jak zaczynasz, dlatego mówię o tym GUS TERYT, piszesz miasto stara szkoła, tak jak ja mieszkam czy Bydgoszcz, to on wyszukuje, zgadza.

**[Damian Kaminski]:** Już pokazuje, przejmę ekran.

**[Piotr Buczkowski]:** To nie pozwolicie mi pokazać?

**[Janusz Bossak]:** Słońce się.

**[Damian Kaminski]:** Dobra proszę.

**[Janusz Bossak]:** No i to samo ma się dziać, tak, czyli ktoś pisze tam nie wiem dokumenty rady nadzor. No i no i on mu wyszukuje, który to jest węzeł w tym JRWA i jak on kliknie, że to jest to, no to mu się tam. Do tego pola czy pisze?

**[Marek Dziakowski]:** Czyli.

**[Janusz Bossak]:** I jeszcze najlepiej, gdyby zwracało JSON z pełną informacją o tym, co tam zostało wybrane i wtedy ktoś w ramach reguły.

**[Piotr Buczkowski]:** Tutaj tutaj.

**[Janusz Bossak]:** Będziemy tego użyć.

**[Piotr Buczkowski]:** W React zwraca pełnego JSON, tutaj nie musi tak, bo może tak. GUS TERYT, to musielibyśmy się za każdym razem z reguły odejmować gdzieś tam, bo tak mamy możemy lokalnie się odwołać.

**[Damian Kaminski]:** Znaczy, ja mam pytanie wyżej poziomo w sensie, a czemu dać Sterling?

**[Piotr Buczkowski]:** Dobrze, coś mi to długo.

**[Damian Kaminski]:** Żeby pokazać ten GUS TERYT?

**[Piotr Buczkowski]:** Nie, ja chcę pokazać, jak to wewnętrznie działa w kodzie, tak.

**[Damian Kaminski]:** Swoje. OK, dobra, no dobra, a ja zapytam wyżej poziomo. A czemu w ogóle idziemy w tę stronę a nie zwykły rejestry?

**[Kamil Dubaniowski]:** Gdzie wydajniej?

**[Janusz Bossak]:** Bo to jest wygodniej. Szybciej wygodniej. Wydajniej.

**[Damian Kaminski]:** Ale w sensie szybciej, no dobra, wydajnie to.

**[Kamil Dubaniowski]:** No i nie, nie, nie, nie dotykamy case definition. To jest główna zaleta.

**[Damian Kaminski]:** OK.

**[Piotr Buczkowski]:** To dlaczego nie jedziecie w słowniki zagnieżdżone?

**[Damian Kaminski]:** Dobra, to znaczy. W niedzielę tak nie idziemy w słowniki, ale możemy.

**[Piotr Buczkowski]:** Hierarchicznym.

**[Janusz Bossak]:** Tak znaczy.

**[Kamil Dubaniowski]:** No tak, no tutaj temat uprawnień to raz będziemy jeszcze rozwijać, d.

**[Piotr Buczkowski]:** Panie rejestr.

**[Kamil Dubaniowski]:** A temat? Parametrów, które opisują do mnie katalog. W słownikach trzeba by się tam bawić tymi.

**[Damian Kaminski]:** Nie, ale to ja nie mówię o słownikach, a o rejestrach w sensie, bo chcę zaraz rozwinąć myśl w kontekście powiedzmy potencjalnie w ogóle rejestrów kontrahentów, tak, żebyśmy popatrzyli na to.

**[Janusz Bossak]:** Nie, już ustaliliśmy, że robimy tak, nie, nie, nie kombinujmy teraz już no nowych.

**[Damian Kaminski]:** Ale ja nie podważam Janusz, tylko może jeszcze raz powiem wszystko, że może za chwilę jak zrobimy to tutaj, bo tu mówimy, nie wiem, tam będzie w tym JRWA 150-200, jak będzie 500 pozycji, pewnie max. Ale pytanie, czy tego samego mechanizmu, który tutaj w ten sposób sugerujecie, nie powinniśmy później zacząć wykorzystywać do przeszukiwania kontrahentów. Pod w kontrahentach często mamy 100000 i pytanie, czy to rozwiązanie, które tu planujecie, będzie wykorzystywane właśnie czymś innym?

**[Janusz Bossak]:** No.

**[Piotr Buczkowski]:** To jest, nie to jest rozwiązanie do JRWA.

**[Damian Kaminski]:** OK.

**[Piotr Buczkowski]:** Tylko i wyłącznie do JRWA proszę nie.

**[Damian Kaminski]:** Tylko dobra.

**[Piotr Buczkowski]:** Nie generalizuj się ich od razu, bo bycie kupa.

**[Janusz Bossak]:** Tak, tak, tak, tak znaczy?

**[Damian Kaminski]:** Dobra, rzucam tylko, że dobra jak przemyślane to OK.

**[Janusz Bossak]:** I dla. Natomiast idea tego tak jakby będziemy mieli tutaj dla GUS TERYT i dla JRWA to taka idea może być stosowana czy mogłaby być powielana do innych rozwiązań? Te 2 akurat źródła charakteryzują się.

**[Damian Kaminski]:** No.

**[Janusz Bossak]:** Jednym ważnym elementem są praktycznie stałe, niezmienne. Nie ma na nich pracy, tak jak masz kontrahentów, to tam nagle zmieniasz adres tego kontrahenta coś tam no.

**[Damian Kaminski]:** Powiedziałbym, że to akurat jest takie samo, czyli adres kontrahenta zmienia się tak rzadko jak JRWA.

**[Janusz Bossak]:** Nie.

**[Piotr Buczkowski]:** To tak naprawdę ja też wywoła. To jest słownik z uprawnieniami.

**[Janusz Bossak]:** Nie. Muszę się przełączyć na Przemka, także idę tam.

**[Kamil Dubaniowski]:** Też za chwilkę uciekam na ten LOT, więc znaczy tak kluczowe, żebyście może jak najwięcej teraz Piotr Marek przez te dni, kiedy jeszcze Piotrek jesteś, przekazali sobie tej wiedzy, a.

**[Piotr Buczkowski]:** Marek, zostawmy stajnie chwilę OK, możesz?

**[Kamil Dubaniowski]:** Tak, tak, a ja Marek też jeszcze, bo bo jest kilka niuansów różnych od tych GUS TERYT, bo na przykład tutaj będzie struktura, czyli są jakieś katalogi nadrzędne i podrzędne.

**[Marek Dziakowski]:** Dobrze.

**[Piotr Buczkowski]:** Dobrze, ja pokażę jak to technicznie jest zrobione, tak.

**[Kamil Dubaniowski]:** Dobra, a później ja ja się rozpiszę z funkcjonalnościami, których będziemy na pewno oczekiwanie na dalszym etapie, tak, czyli, że są jakieś katalogi, których nie da się wybrać, bo to są katalogi nadrzędne, powinno się tylko te najniższego poziomu. To będą jakieś niuanse, ale to już w kontekście samego pola wyboru.

**[Marek Dziakowski]:** OK.

**[Kamil Dubaniowski]:** Ja uciekam na tym odcinki.

**[Damian Kaminski]:** No dobra, ja się chyba też przyłączam. Zostawiam was.

**[Piotr Buczkowski]:** Dobrze, to ja mówię. Ogólnie jest źródło danych typu 5, czyli klas.

**[Damian Kaminski]:** Na razie.

**[Piotr Buczkowski]:** Podajesz jakoś nazwę, podajesz klasę? Która obsługuje to? Plujesz sobie tutaj też trzeba to jaki jest to jest, to jest wartość, która jest zapisywana w polu case definition, tak. Implementuje klasę, która to też klasy, która implementuje te interfejs, tak jak GUS TERYT, tak. Obiec kilka tych. Taką jest zwraca powiedzmy JSON z 2 property sami. To jest zapisywane w bazie, najlepiej jest wyświetlane tak. Tutaj to jak zrobisz tecz tutaj pewnie. Pewnie tutaj przekazuje tak tutaj w szokuje to trzeba po prostu sobie sam też do końca nie pamiętam. To jakieś dodatkowe funkcje, która popierają tak jak jest, jakie są properties zdefiniowane ten powiedzmy GUS TERYT. Tutaj powiedzieć miano stałe zapisane, no bo. Tutaj pewnie będziesz chciał takie funkcje to robić, które wyszukują i na koniec zwracają obiekty do zapisania w bazie danych. Tak. Czy to wartość do zapisania w bazie danych?

**[Marek Dziakowski]:** OK. Tam jeszcze była jakaś kwestia uprawnień, to trochę nie zrozumiałem.

**[Piotr Buczkowski]:** To było normalnie słowniku, to każdy może każdy każdy opozycję słownika wybrać co nie, a tutaj będzie tak, że będzie tabelka. To będzie oddzielna tabela, tak?

**[Marek Dziakowski]:** Tak, tak.

**[Piotr Buczkowski]:** Gdzie będzie, jak powiedzmy pozycja dotarła i kto ma uprawnienia do wybrania tej pozycji, czyli ty będziesz po prostu tutaj w jakimś selekcję musiał uwzględnić, że masz uprawnienia do tej pozycji, że możesz wybrać tylko te pozycje, które do których masz uprawnienia.

**[Marek Dziakowski]:** OK. Czyli ok.

**[Piotr Buczkowski]:** Gdyby nie to to to to można było słownikami z hierarchicznym i załatwić.

**[Marek Dziakowski]:** No ma.

**[Piotr Buczkowski]:** Tam też są zasady takie, że na przykład możesz tylko wybrać. Pozycje, które tam mają oznaczone, że możesz je wybrać, tak. Na przykład widzisz drzewko, ale nie możesz wybrać tych. Nie gałęzi, tak, nie nie najniższej gałęzi.

**[Marek Dziakowski]:** Czerni. Oczywiście.

**[Piotr Buczkowski]:** Liście liście osiądziemy tak.

**[Marek Dziakowski]:** Jasne, no to zrozumiałem.

**[Piotr Buczkowski]:** No ale to już tak liścia mogłabyś tam różnym poziomie, tak?

**[Marek Dziakowski]:** No tak, tak, no jak dobrze wiem, OK, no więc nie rozumiem.

**[Piotr Buczkowski]:** No ale technicznie te technicznie to jest po prostu to źródło danych typu klasa.

**[Marek Dziakowski]:** Aby.

**[Piotr Buczkowski]:** To trzeba zrobić w klasę, która implementuje.

**[Marek Dziakowski]:** OK, do tego do przetrzymywania danych z samego JRWA będzie jedna tabela, a do.

**[Piotr Buczkowski]:** Będą 2 tabele 2 albo 3 tabele. Już nie pamiętam. Tam było zaproponowane tak czyli. Lista pozycji, uprawnienia do pozycji. I przypisanie. Czy się jeszcze być? Ale nie pamiętam w tej.

**[Marek Dziakowski]:** A jest gdzieś to opisane?

**[Piotr Buczkowski]:** No bo. Tak.

**[Marek Dziakowski]:** My się jakoś wycena czy coś.

**[Piotr Buczkowski]:** Kamila mi się spytać.

**[Marek Dziakowski]:** Dobra tak zwanego po.

**[Piotr Buczkowski]:** Ogólnie to jest tak, że właśnie to jest chyba. To jest to jest do serca tak się dziwnie nazywają, bo tak zrobione, że źródle zewnętrznym tak to jest do. Pobierania wybranej wartości, ale to nie pamiętam. To czego?

**[Marek Dziakowski]:** No to sobie najmniej przejrzy. Co do czego jest jeszcze dobra? To kiedy to trzeba zrobić w przyszłym sprint czy przyszły tydzień?

**[Piotr Buczkowski]:** To do Kamila pytanie.

**[Marek Dziakowski]:** Dobra, to też zrobię.

**[Piotr Buczkowski]:** No to to teraz tylko.

**[Marek Dziakowski]:** Dobra, to jest zapis z tego spotkania, to w razie co tam będę sobie do niego odwoływał się grę i coś tam.

**[Piotr Buczkowski]:** Mówię tak na szybko. To właśnie, że w tej to tejże bors szukaj minus jeden GUS TERYT.

**[Marek Dziakowski]:** No.

**[Piotr Buczkowski]:** Masz tura to jest klasa na tym się trzeba wzorować.

**[Marek Dziakowski]:** Dobra.

**[Piotr Buczkowski]:** Tak tutaj trzeba tylko właśnie. To plus to jest ważne, tak?

**[Marek Dziakowski]:** No. Dobra. To jak coś to w kontakcie mam.

**[Piotr Buczkowski]:** No to tylko tak.

**[Marek Dziakowski]:** Cześć.

**[Janusz Bossak]:** Zatrzymano transkrypcję.


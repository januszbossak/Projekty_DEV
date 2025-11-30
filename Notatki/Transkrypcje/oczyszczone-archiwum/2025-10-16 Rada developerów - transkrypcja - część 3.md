**Data spotkania:** 16 października 2025, 08:01 - część 3

---

**Piotr Buczkowski:** I tak to jest w bazie danych, że czeka na podpisanie, tak.

**Marek Dziakowski:** No tak, jak padnie, to i tak sobie to najwyżej weźmie dane z bazy.

**Adrian Kotowski:** Można ewentualnie jakimś callback pomyśleć też – wysyłać właśnie callback do tego, nie wiem, do tej głównej aplikacji. TrustCenter to właśnie też kolejkowa być, tak, że jakaś, nie wiem.

**Piotr Buczkowski:** No ale to musi trafić na odpowiedni serwer, tak?

**Marek Dziakowski:** No tak, to jest też problem, żeby to do odpowiedniego serwera wróciło to.

**Piotr Buczkowski:** Dobrze, według mnie koniecznie musimy wydzielić, tak, to podpisywanie do oddzielnego procesu, bo to dawno powinno być zrobione. Ja nie wiem, najprostsze to jest po prostu zrobić usługę osobną, która będzie działała na serwerze. Bardziej skomplikowana jest zrobić ten microservices czy tam docker czy cokolwiek, który gdzieś tam będzie tutaj działał – tak będzie. Co chwilę tam sprawdzał, czy ma coś w kolejce, jeżeli ma coś w kolejce, czyli w bazie danych, tak, dokumenty do podpisu, do dodania do blockchaina, to pobiera. Dodaje do blockchaina, zapisuje informacje, że dodano do blockchaina. A jakiś proces, tak, ewentualnie. Znaczy, na przykład wysyła maila, tak, że dodany do blockchaina. A czy nawet użytkownikowi możemy na razie zrezygnować, tak, w pierwszej wersji, że użytkownik dostaje takie informacje? Proszę czekać na maila z informacją o dodaniu do blockchaina, tak? Albo proszę tutaj odświeżyć status sobie ręcznie. Że dodanie SignalR'a – to ewentualnie drugi krok. Jak już będziemy mieli to wydzielone, tak? No to jest ważne.

**Adrian Kotowski:** Myślałem jeszcze jakiś ten – znajduje się na przykład event grid na przykład albo Service Bus, żeby tak – dlatego komunikację można by też, zresztą, można kolejkowanie czy dlatego tak kolejkowanie wprowadzić, gdzieś różne komponenty nie powiązać.

**Piotr Buczkowski:** Co, co, sorry, bo nie zrozumiałem, co, co.

**Adrian Kotowski:** I ten event grid albo Service Bus można sobie ten definiować właśnie te eventy i taka lepsza forma komunikacji takim brokerem.

**Marek Dziakowski:** No tak, tutaj.

**Piotr Buczkowski:** Znaczy, tutaj w zasadzie nie, nie jest potrzebna komunikacja, tak. Jest dodawany, jest dodawany wpis w bazie danych i ten wpis musi być obsłużony, tak.

**Adrian Kotowski:** Właśnie, to jest ten wątek, żeby jednak przekazywać informacje. To byłby bardziej uniwersalny jakby taki mechanizm, bo teraz mówimy, że ma być jeden microservices, który tam ma obsługiwać, wydziela tę funkcjonalność. To można w przyszłości troszeczkę łatwo rozszerzyć tak, abyśmy mieli to – wypady na przyszłość. Mieć – pytanie, czy będziemy mieć jakieś?

**Piotr Buczkowski:** Specyficzny przypadek, gdy gdzie mamy? TrustCenter jest u nas, tak, to ma się dziać tylko u nas, tylko na jednym serwerze, to ma się dziać po kolei, tak. To, co mówiłem, że nie możemy na przykład równocześności zrobić.

**Adrian Kotowski:** Mi chodzi o to, że inną funkcjonalność trzeba będzie podzielić, to możesz z tego samego skorzystać, no bo teraz byśmy 2.

**Piotr Buczkowski:** No ale to inna funkcjonalność nie będzie pasować do tego przykładu.

**Marek Dziakowski:** Czy może pasować do samej koncepcji kolejki? Na przykład tym Service Bus – można różne kolejki tworzyć i jeżeli byśmy kiedyś chcieli jakąś funkcjonalność tak w ten sposób zrobić, no to już by było.

**Piotr Buczkowski:** Znaczy, ja jakiś czas temu próbowałem kiedyś OCR tak zrobić przez microservices, przez kolejkowanie. Nie udało się. Bo kolejkowanie.

**Adrian Kotowski:** Zdecydowanie, proszę.

**Piotr Buczkowski:** Znaczy, ogólnie nie ma sensu na przykład przez te systemy kolejkowe przesyłać plików, bo to jest za duże, nie do tego to zostało zrobione.

**Marek Dziakowski:** Za dużo, tak.

**Adrian Kotowski:** Ale my byśmy wysyłali po prostu komunikaty, że też się udało. Nie byśmy nie wysłali dużych treści. Jest to bardziej takie, żeby jakieś.

**Marek Dziakowski:** No tylko że.

**Adrian Kotowski:** Inicjować.

**Piotr Buczkowski:** Ale.

**Adrian Kotowski:** Że to, że się udało – dokument dotyczył czym dodać, podpisać, że dodać do blockchaina?

**Piotr Buczkowski:** No i co, co zrobi z ta akcją?

**Adrian Kotowski:** Również obsłużyć to wykrycie jakoś, nie wiem, sesję użytkownika po stronie aplikacji TrustCenter i na przykład jakiś komunikat, nie wiem, już wołać w takiej zasadzie. Znaczy, mogę zbadać jeszcze, ale tak, ale też alternatywa, bo mówicie.

**Piotr Buczkowski:** Ponieważ.

**Adrian Kotowski:** Jako alternatywa sesji SignalR, więc tak, to chciałem coś takiego zaproponować.

**Piotr Buczkowski:** Ale to jest SignalR po to, żeby z przeglądarką gadać. Tak jest to – co tutaj alternatywy jakiś inny?

**Marek Dziakowski:** Mhm.

**Adrian Kotowski:** Ale chodzi o to, że był po stronie serwera, na przykład tego TrustCenter i. Nie, przykład, mógłbyś jakoś to – kolejny, to współpracować.

**Piotr Buczkowski:** Po SignalR na serwerze. SignalR'ias do przeglądarki, chyba tego te – gadania z przeglądarką, tak, że przeglądarka dostaje.

**Mateusz Kisiel:** Czy serwery między sobą też? Trzeba? Serwery między sobą po SignalR czy też mogą się komunikować?

**Adrian Kotowski:** Tak, 2 strony jest – klient i serwer, tak, więc tutaj można jakoś to – tą spróbować powiązać.

**Piotr Buczkowski:** Nie, chodzi mi, że serwer do serwera czy jest sens?

**Adrian Kotowski:** Układ jest sens – event grid na przykład z zarejestrowane po stronie serwera i można by też po stronie serwera powiem, zerwać ten nowy eventy, które przychodzą właśnie – na przykład informacje o tym, że jest.

**Piotr Buczkowski:** Tutaj mamy, tutaj mówimy o komunikacji serwer-serwer przez SignalR. Czy to ma sens?

**Adrian Kotowski:** No tak, ale też z tym mieć tyle – do powiedzenia po stronie klienta.

**Piotr Buczkowski:** No ale to mówimy o komunikacji, że ten microservices, podpis dodający do blockchaina, będzie notyfikował serwer WWW, a serwer WWW notyfikować klienta, przeglądarkę.

**Adrian Kotowski:** Tak, można by to referencje przesyłać. Jak się, tak jak to się nazywa – indicator tej sesji właśnie SignalR, niektórzy nie – zapachową, ale to można by przekazywać jakoś od tej strony to, to do tego podejść.

**Piotr Buczkowski:** Poza zasięgiem.

**Mateusz Kisiel:** Znaczy, wydaje mi się to tak, trzeba mieć połączenie nawiązane, tak. Nie może sobie wysłać do klienta bez połączenia.

**Piotr Buczkowski:** No właśnie ja. Tak, jeżeli widzisz, jak to działa, na przykład. TrustCenter – tak, to tam jest cały czas wiszą, tak, ta SignalR coś tam connection, tak jak SQL Server, proces.

**Adrian Kotowski:** To nie można po prostu liczyć tego, tego połączenia, bo ty tego połączenia trwałego HTTP.

**Piotr Buczkowski:** Nie, nie, nie, nie.

**Mateusz Kisiel:** Też, też klient może mieć nawet nie mieć publicznego IP, żeby do niego się połączyć.

**Piotr Buczkowski:** To jest tak, że właśnie klient się trzyma połączenie, tak, i to.

**Adrian Kotowski:** Tunelowanie wtedy robione, żeby to, to działało.

**Piotr Buczkowski:** Zwrotny idzie – czy najpierw klient musi nawiązać połączenie? Musiał otworzyć kanał w stronę, żebyśmy mogli takie połączenie zarejestrować jakby – taki numer.

**Mateusz Kisiel:** Jeszcze to można zobaczyć na te różne inne rodzaje tych kolejek, no bo na przykład do przesyłania plików, co mówiłeś, Piotr? Na przykład Kafka jest dobra, chyba YouTube z tego korzysta, że między tymi kolejnymi etapami przetwarzania filmów właśnie w Kafce wrzucają do obsługuje.

**Piotr Buczkowski:** Nie wiem, ja próbowałem RabbitMQ, tak – to komunikaty tylko małe, tak, czyli takie coś, że powiedzmy mam plik w bazie danych, wygeneruj mi z tego pliku podgląd i zapisz w tym miejscu, a ja sobie z tego miejsca, gdzie zapisałeś, pobiorę, tak. Ale broń Boże, żeby to szło przez kolejkę, te pliki.

**Mateusz Kisiel:** No tak, to lepiej jakiś może link wrzucić wtedy czy coś.

**Piotr Buczkowski:** No nie, no.

**Marek Dziakowski:** Nie, dostęp do bazy.

**Piotr Buczkowski:** Kolejka, ma serwis, ma dostęp do tych samych.

**Mateusz Kisiel:** Plików.

**Piotr Buczkowski:** Zasobów są.

**Mateusz Kisiel:** Tak, to zamiast.

**Piotr Buczkowski:** Co witryna, czyli do miejsca, gdzie są składowane pliki źródłowe, do miejsca, gdzie są składowane pliki tych poglądów? Nie działa na tych samych, tak? Także komunikat przechodzi tylko, że polecenie wygenerowania podglądu albo odwrotnie, że pogląd gotowy, tak. A nie to, że w kolejce mi podgląd dla – dla tej tablicy bajtów, a zwracam mi listę tablicy bajtów z podglądem, tak.

**Mateusz Kisiel:** No to jeżeli nie przesyłamy plików, to można byłoby korzystać z tych kolejek, czy nie. Czy taki był problem?

**Piotr Buczkowski:** Można, można, tylko że tam było do podglądu, to nie był problem, ale do innych rzeczy były duży problem. Nie chciałem tylko do podglądu z tego robić. Tak było na przykład do wydzielania.

**Marek Dziakowski:** Stron z.

**Piotr Buczkowski:** Do OCR, tak, do OCR miejscowego. Gdzie po prostu potrzebuję zwrócić? W sumie też by się dało, ale. Ponieważ to jest sama część AMODIT, to trzeba byłoby instalować klienta, to zrezygnowałem z tego. W międzyczasie gPicture naprawił, tak, działanie Pdfium JSON, także. Dokładnie działanie Pdfium JSON – jeżeli witryna jest na działy się ciałem. No tam to okazało się, że był problem.

**Mateusz Kisiel:** Też tak. Ogólnie im więcej będziemy takich dodatkowych usług klientów on-premise instalować, tym bardziej wydaje mi się, że docker ma sens, bo wtedy można sobie jednym poleceniem w docker-compose wszystko zawrzeć i nie będzie trzeba instalować osobno tych rzeczy.

**Piotr Buczkowski:** Lub – mówiąc. U klientów często nie ma nawet żadnego administratora. Wszystkim się zajmują nasi konsultanci. Sens, że to była, jak najprostsza.

**Mateusz Kisiel:** Właśnie docker upraszcza znacznie, wydaje mi się.

**Piotr Buczkowski:** Nic nie uprości tego, że nagrywasz pliki? Podano jego zip. Bo musisz mieć infrastrukturę do tego, to myślę, że ją zainstalować.

**Mateusz Kisiel:** Znaczy, no trzeba tego zainstalować ten program, który tego dockera obsługuje, tak. Reszta to już wtedy prosta jest.

**Piotr Buczkowski:** Musisz skonfigurować połączenia sieciowe, tak?

**Adrian Kotowski:** No ja też w sumie, jak to też się. Witam. Właśnie to podejście, bo dość – starsze podejście też trzeba je instalować.

**Piotr Buczkowski:** Są klienci, co mają wszystko na jednym serwerze – i bazę danych, i AMODIT, i usługę, i witrynę. Nie możemy w to iść, tak, tylko że ktoś musi, musiałby być. Się zajmować od nas instalacją u klientów pewnie.

**Marek Dziakowski:** No ta instalacja u klientów AMODIT to jest jedna rzecz. TrustCenter to jest już co innego.

**Piotr Buczkowski:** Nie, tutaj mieszamy trochę, tak, tematy. TrustCenter to zadanie. Czy to zrobimy – i na początku myślałem, że to po prostu jak najszybciej, tak.

**Marek Dziakowski:** Tak.

**Piotr Buczkowski:** Wydzielić do, do dzielnej usługi, która działa na jednym serwerze, tak, która sobie zapisuje. Na razie zrezygnować z tego powiadomienia dynamicznego o podpisanie – odpisania, o dodanie do blockchaina, nie podpisaniem. Podpisanie to już wcześniej robione w inny sposób, tak? Pytanie, czy, czy jeżeli 2 osoby naraz próbują podpisać, też nie będzie problemu, tak. Przed – czy to jakaś blokowane jest to, że naraz 2 osoby nie mogą podpisywać jakiegoś dokumentu? Podpisy przez 2 osoby?

**Marek Dziakowski:** Jestem prawie pewien, że to nie jest obsłużone.

**Piotr Buczkowski:** No to kolejny, kolejny temat, bo.

**Marek Dziakowski:** Ja się po prostu. No tak, że tak, ale jestem pewien, że to nie jest obsłużone, bo chyba nawet kiedyś Rafał mówił o tym, że to chyba nie jest obsłużone i trzeba to obsłużyć. W jakiś sposób.

**Piotr Buczkowski:** Według mnie pierwsze – tak, to jest w jakiś sposób wydzielenie tego dodawania do blockchaina. Czy zrobienie tego microservices będzie – microservices będzie szybkie? No to już Marek twoja decyzja. Jeżeli to zrobienie tego jakoś jako mikro, microservices wiąże się z jakimiś kosztami, to trzeba najpierw uzyskać akceptację tych kosztów.

**Marek Dziakowski:** Tam były.

**Piotr Buczkowski:** Znaczy, utrzymanie. Tak.

**Marek Dziakowski:** Tak, tam dosyć małe te koszty były, prawie że zerowe.

**Piotr Buczkowski:** Ale trzeba najpierw.


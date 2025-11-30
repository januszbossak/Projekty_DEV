**Data spotkania:** 7 listopada 2025, 09:01 - część 3

---

**Damian Kaminski:** Znaczy – pani Krysia musi powiedzieć dokładnie, co robi dzisiaj, bo ona już robi to, bo ona robi to analogowo i my musimy w takim przypadku wiedzieć. Pani Krysia mówi – no, ja pakuję jedną sprawę i wysyłam do AD – albo biorę w teczkę i niosę do AD – kopię za potwierdzeniem z oryginałem. Albo mówi – ja biorę z całego miesiąca – albo powie – ja biorę z całego roku – czyli moja teczka to jest nie teczka, tylko ja jadę furgonetką z obstawą, bo ja mam tyle rzeczy do przewiezienia. I to są właśnie przypadki użycia, które zobrazują nam, z czym my się mierzymy.

**Janusz Bossak:** Tak, dokładnie. Ja pamiętam właśnie z Rossmana rozmowy na ten temat, bo tam też dość mocno omawialiśmy i oni mieli to. I zresztą tutaj też jest tak zwane archiwum zakładowe. Archiwum zakładowe, to jest takie archiwum podręczne, czyli w te dokumenty, z którymi pracuje – z którymi – do których dyrektor może chcieć za miesiąc tam zajrzeć, nie – pani Krysiu, a tam w zeszłym miesiącu mieliśmy taką umowę, niech pani mi ją przyniesie, tak – i ona mają w archiwum zakładowym – ten folder – znaczy ten segregator, tak – to pudło i tak dalej. I to dziewczyny z Rossmana mówiły, że w miarę upływu czasu one to pakują do pudeł – dokumenty, które już są rzadziej – że tak powiem – potrzebne – i one trafiają do pudła. Mają – są oznakowane, oklejone i tak dalej i tak dalej. I jak właśnie – tak jak powiedziałeś – przychodzi końcówka roku, one te już zapakowane, już przygotowane pudła przekazują do archiwum zewnętrznego. Akurat to nie było państwowe archiwum, ale – no – takie zewnętrzne archiwum gdzieś tam pod Łodzią, gdzie oni to zawożą i to sobie tam leżało już na wieki, nie. I o to chodzi, że tu jest też takie flow pewnie, że jest to do tego archiwum zakładowego, czyli taki podręczny archiwum, ale w którymś momencie – tak jak powiedziałeś – może raz na rok – a może po miesiącu – nie wiem – trafia to do tego państwowego archiwum, nie. I w obie strony może być też, tak – no, bo może być tak, że po 3 latach przyjdzie jakiś emeryt i powie – potrzebuję tam moje dokumenty, bo chcę wnioskować o zwiększenie emerytury, nie. No i się okazuje, że te już są oddane do tego archiwum państwowego, no – ale to oni jako firma muszą tam się poprosić, tak – tego archiwum państwowego – przywiozą im te dokumenty fizycznie i oni tam temu człowiekowi je tam wydadzą czy udostępnią. No – tak sobie to wyobrażam, nie. Więc wracając tutaj – przypadki użycia, częstotliwość tych przypadków – to jest właśnie raz na rok, raz na tydzień, codziennie i tak dalej – i to muszą koledzy wdrożeń od LOT się dowiedzieć. Zadać pytania po prostu, mając już – będąc już uzbrojonymi w trochę wiedzy – ogólnie o tym JRWA. To kompendium – ja im tam zresztą przypadki użycia wygenerowałem – wygenerowałem – nie wiem – ze 100 albo i więcej przypadków użycia. One są trochę uproszczone, no – bo są na początku naszej drogi – teraz tak – przy tej wiedzy, którą mamy – oni powinni je zgłębiać i ewentualnie dopisywać nowe, tak – rozdrabniać na mniejsze, tak – żeby to jak najlepiej uszczegółowić, ale mają przynajmniej materiał, nad którym można pracować i w tym obszarze. A do AD – tak – to AD jest – zresztą też – tak samo powinni postąpić. Tam są te przypadki – nie wiem – pięć – jest przypadków użycia wygenerowanych, natomiast to trzeba dopytać i upewnić się. No dobra, ale wracając do tych naszych pomysłów – ja bym się jeszcze nie zastanawiał – kto co. No – na razie identyfikujemy, co mamy zrobić. Mamy ten UPS, Global Express i to AD.

**Damian Kaminski:** Znaczy – musi – musi to pójść w tym kierunku na analizie z nimi – niech opowiedzą i nagrajmy to – jak oni archiwizację danych – z jaką częstotliwością, jak to wygląda, czy to kompletują właśnie latami, czy miesiącami, jak to dzisiaj robią? No, bo oni – niezależnie od tego, że to ma iść – bo my to możemy też zrealizować – im powiedzieć – powiemy – opowiedzcie, jak dzisiaj, a my wam powiemy, czy – to jakie są wymagania API – jest spójny z tym, co macie dzisiaj, albo co musicie zmienić – jak będziecie musieli zmienić swoją pracę, bo – jak zbierzemy od nich dzisiejszy stan rzeczywisty, to powiemy im – tak samo będzie tu działać tylko w systemie, albo musicie teraz podchodzić inaczej. Zamykacie per sprawa, potem ewentualnie – musimy wam zrobić jakieś walidację, jeśli wy chcecie miesiącami – to generujecie sobie – powiedzmy – albo jakieś pliki – albo leci połączenie do AD, ale zanim to wyślemy, to robicie dodatkowo walidację – czy wszystkie sprawy z danego miesiąca są już zamknięte, czy – czy? No właśnie – no, nie wiemy tego, tak.

**Janusz Bossak:** Dokładnie, więc...

**Damian Kaminski:** Według mnie muszą nam opowiedzieć, jak robią to dzisiaj. My powiemy im, że wtedy – my wrócimy, spiszemy to, damy im jeszcze do walidacji, czy na pewno jest to tak – zwali – budujemy to pod kątem tego, jak to trzeba robić w kontekście takim technologicznym przy wykorzystaniu integracji. Czy to jest spójne, czy rozbieżne, w jakich punktach. A dzięki temu, że też opowiedzą, to my będziemy wiedzieli, z jakim – jaką skalą się mierzymy. Czy to jest raz na rok i – no właśnie – to będzie może generować jakieś timeouty albo coś w tym stylu, bo jest tego dużo. Czy to jest regularnie co miesiąc i wysyłają po prostu to, co wpadło z poprzedniego miesiąca.

**Janusz Bossak:** Tak – znaczy chodzi mi też o to, że nie my mamy robić za nich wdrożenie, tak.

**Damian Kaminski:** No tak, no – my odtwarzamy ich system.

**Łukasz Bott:** I...

**Janusz Bossak:** Tak – zrobiliśmy – i tak – znaczy – nie mówię o naszych chłopakach, nie?

**Damian Kaminski:** A, OK.

**Janusz Bossak:** Że nie naszą rolą – tu działu – jest robić za nich wdrożenie i daliśmy im w tej chwili bardzo duży wkład. Ty – teraz muszą to pociągnąć sami. Naszym zadaniem, natomiast i to – i to – znaczy – zostawić to AD – w tej chwili wydaje mi się, tak – na nasze chłopski rozum, że to da się, tak jak tutaj Łukasz powiedział, zrobić to za pomocą REST API i to będzie prawdopodobnie wystarczający workaround. I żeby oni się nie nastawiali, że oni na nas czekają, że my mamy zrobić im integrację z AD.

**Łukasz Bott:** No – na – na chwilę obecną – tak to było wyceniane i takie jest zrozumienie, że to my robimy integrację, natomiast ja już to dawałem – to zastrzeżenie, że być może – COLA REST – i wtedy my co najwyżej możemy być jakimś wsparciem technicznym, jakby mieli problem – nie wiem – połączenia się – wywołania tych REST API, tak. No, ale to wtedy całkowicie nie zarabiamy my jako dział, tak – na tym, bo...

**Janusz Bossak:** Trudno – ważne jest, żeby dowieźć.

**Łukasz Bott:** Nie, no – ja też wolę, szczerze mówiąc – jakkolwiek dziwnie to zabrzmi – nie zarobić, ale skoro można to zrobić inną metodą – może prościej, tak, no to...

**Janusz Bossak:** Trzeba z chłopakami tam z wdrożeń tą temat przegadać. Natomiast do JRWA mamy – poważnie – znacznie poważniejsze – inne poważne tematy do przedyskutowania. No – a jakimś tam – według mnie – dedykowanym – może nawet spotkaniu, ale dość pilnie, bo to trzeba już też zacząć robić. Jak tak mówimy o tym, co jest do zrobienia do końca kwartału. Bo po tej mojej analizie dość szczegółowej wychodzi, że – no – parę rzeczy warto zrobić jakby systemową AMODIT. Główna kwestia to jest takie pole "Odnośnik", które by po tej strukturze JRWA się poruszało. Jak – czyli byłoby takim – właśnie – hierarchicznym jakimś przedstawieniem tego. Na razie tylko mam mgliste wyobrażenie, tak – znaczy – nie mam jakiegoś projektu – w głowie na razie mam taki mgliste wyobrażenie, no – bo tam się pojawia – to jest jakby czynność, którą będzie się wykonywało przy każdym dokumencie – każdym – każdy, ponieważ JRWA polega na tym, że to jest działanie normatywne, czyli uregulowane ustawą i rozporządzeniem. I to nie jest widzimisie, że komuś się chce czy komuś się nie chce. Każdy dokument – dosłownie każdy – nawet jak wpadnie im niechciana oferta na pizzę, to muszą to podpiąć pod JRWA, tak. Więc będą to robić dzień w dzień – setki razy – na każdy dokument, który wpadnie – każdy dokument, który jest wewnętrznie wyprodukowany – wysyłane – notatka z działu do działu, tak – jak my sobie robimy notatkę z Tips Day – czy po spotkaniu Sprint Review – to ta notatka musi być odnotowana w JRWA. Wszystko. Więc to jest rzecz, która ich obciąża bardzo mocno robotą, więc to musi być robione płynnie, wygodnie – to nie może być 15 kliknięć, bo nas po prostu zabiją. I to jest główne zastrzeżenie też do tych systemów z DI, bo też kazałem GPT przeanalizować opinię na temat obsługi tych systemów z DI. To jest główne zastrzeżenie, że jest niewygodnie, że jest nielogiczne, że trzeba bardzo wiele klikać. I ja myślę, że to jest problem, tak – to nie jest problem tego, że to się da na naszym formularzu za pomocą 5 podłowników hierarchicznych wyklikać, bo nas zjedzą po prostu – jak powiedział, że to jest w ogóle nieużywane. I w tym jest problem – tak – czy to – to jest rzecz, którą według mnie powinniśmy zrobić – taki asystent – ja tak sobie go tam nazwałem, którym będzie "Asystent klasyfikacji", czyli takie obsłużenie pola odnośnik – na przykład – to – co Łukasz ty wczoraj pokazywałeś tam – odnośnie tego szukania, nie – to może, może to powinno być tak, że oprócz tego szukania – takiego właśnie, które tam pokazywałeś – to jest w tym polu – taki drugi guziczek – i JRWA...

**Łukasz Bott:** Mhm.

**Janusz Bossak:** Który otwiera taki – nazwijmy to – klasyfikator JRWA, gdzie ja sobie wpisuję coś tam i tam jest – tam są wszystkie te mechanizmy wyszukiwania – tam w tym okienku byłyby te mechanizmy, pokazywanie tego jako drzewko – to okienko by uwzględniało moje uprawnienia do odpowiednich węzłów JRWA. Ono mi pomagało znaleźć teczkę sprawy, bo zauważcie, że to – klasyfikując – ja nie szukam w sumie... Halo, jesteście?

**Damian Kaminski:** Tak, tak, tak, tak – tylko wyłączyłem już tam ten temat, bo była to już, tak...

**Łukasz Bott:** Tak, jesteśmy.

**Janusz Bossak:** Jakby coś – a – bo tak mi mrugnęła okiem to, jakby zgasło, tak – i – ale rąbnęło to okienko i rano wpadło mi pod inne okna, jakby w ogóle zniknęło. No, więc w tym oknie wyskakującym powinien być cała ta logika...

**Damian Kaminski:** Nie. Mhm.

**Janusz Bossak:** Wyszukiwania – teczki sprawy, pod którą mogę to podpiąć, bo to jest tak – zwykły człowiek w kancelarii – czy gdzieś – pierwszym jego zadaniem jest podpięcie pod teczkę sprawy – nie pod węzeł JRWA – pod teczkę sprawy. Te teczki są przypięte do węzłów JRWA. I teraz on musi zidentyfikować – prowadzi – czy to coś, co ma przed sobą – jakiś papier, jakiś dokument, jakieś pismo – to on musi wykombinować, gdzie je wpiąć – w którą teczkę – nie w którą gałązkę JRWA – którą teczkę?

**Damian Kaminski:** Tak, tak.

**Janusz Bossak:** Którą teczkę? I teraz – dopiero jak nie umie, nie wie pod co to wpiąć albo stwierdza, że to jest zupełnie nowa sprawa, to tworzy teczkę nową, jeżeli ma uprawnienie. I to jest cała idea tego. I tutaj uważam, że...

**Damian Kaminski:** Znaczy – uprawnienia do teczki raczej po prostu powinien mieć z racji, że obsługuje – kwestia potem – gdzie może ją przypiąć, czy ma uprawnienia do tego JRWA, ale – przepraszam was – muszę się po prostu przełączyć – czy – żeby ustalić co robimy na spotkaniu z filmem, bo będzie za 10 minut?

**Janusz Bossak:** No dobra, to tam jest...

**Damian Kaminski:** Więc myślę, że kontynuujmy po prostu na designie – no – możecie to omówić sami – nie ma problemu, ale...

**Janusz Bossak:** Ale – dobra – z tym – to wiesz – ten repozytorium – damy radę – nie – w tej wersji uproszczonej – a – poszedł, wiesz. Dobra.

**Łukasz Bott:** Dobra, to tutaj – jeżeli chodzi o to – to rozumiem, że JRWA to nie tylko do LOT będzie potrzebne, ale też ogólnie, tak – i rozwiązanie systemowe.

**Janusz Bossak:** JRWA – przyda się do wielu – jeżeli będziemy szli w kierunek takich firm, jak na przykład RPIK Tychy, tak – albo ogólnie jakieś komunalne spółki i tak dalej, bo w nich wszystkich jest JRWA – w uczelniach jest JRWA. No – tego typu firmach – szpitalach – jest JRWA, a – tak – jak w WIM – nie wiem, czym mówiłem – im tego nie używać, oni są zwolnieni z JRWA czy jakoś inaczej się to ogarniają, ale w WIM – jakoś dziwnym trafem – ten JRWA właśnie nie pojawiło. A według mnie oni powinni być też – chyba, że oni są jakimś...

**Łukasz Bott:** Wiesz co – no – to – w końcu wojska jest, to może inaczej – trochę.

**Janusz Bossak:** Tak, może oni podlegają pod jakieś wojskowe to – kwestie. No dobra, no – bynajmniej – to jest rzecz, która jest warta – nazwijmy to – zrobienia – albo która wymaga zrobienia – może nie tyle – tak – jest – nawet warte, ale wymaga zrobienia ze względu na ten LOT, bo to jest jakby centralny kluczowy punkt każdego procesu, bo – tak jak powiedziałem – to będzie szło. To nie jest tylko korespondencja przychodząca – każdy proces – wniosek na zarząd – delegacja – wniosek urlopowy – korespondencja przychodząca – korespondencja wychodząca – korespondencja wewnętrzna pomiędzy działami, czyli różnego rodzaju notatki – każdy podlega JRWA – bez wyjątku. I w każdym takim procesie będzie ten moment, gdzie trzeba wskazać tą teczkę, więc tu trzeba to zrobić naprawdę dobrze, tak – od strony UX-owej, nie – żeby to było najprostsze.

**Łukasz Bott:** No tak.

**Janusz Bossak:** Jak się da?

**Łukasz Bott:** Dobra. No, ale to już jest kwestia designu. Rozumiem, że organizacyjnie – i jeżeli chodzi o to AD LOT – to po prostu na chwilę obecną musimy pozyskać scenariusze użycia i zastanowimy się, ale wygląda na to, że jako taki MVP być może da się to zrobić za pomocą COLA REST, no – bo tam specyfikacja tego jest – REST API – tak – jak każdy inny.

**Janusz Bossak:** Możemy pomóc, tak – jak tutaj powiedzieliście – w którymś momencie możemy pomóc kolegom skonfigurować to – tak – powiedzieć – przygotować te COLA REST – powiedzieć im, jak to wykorzystywać, jakie parametry tam przekazywać i tak dalej, no – i tyle.

**Łukasz Bott:** Dokładnie tak. No, tutaj ten UPS – no, to UPS – to musimy zrobić i chyba trzeba po prostu zrobić tak samo, jak byśmy to zrobili ten FedEx czy tam DHL, a – jako kolejny moduł. Więc tutaj myślę, że Łukasza Borowskiego trzeba w to zaangażować, bo już – tak – on chyba też i mentalnie, więc co tam ma zrobić – rozszerzają to.

**Janusz Bossak:** Kiedyś – kiedyś była taka koncepcja – w którymś momencie – chyba któregoś klienta, że jest portal taki zbiorczy – chyba się nazywa "Apaczka" – coś takiego. I teoretycznie już kiedyś to rozważałem, ale jakoś przestałem później. Gdybyśmy my zintegrowali się z tą Apaczką, to oni mają integrację ze wszystkim – każdą firmą kurierską, jaka jest w Polsce.

**Łukasz Bott:** Czym – są brokerem takim, nie?

**Janusz Bossak:** Takim brokerem. I tyle, że – no – nie wiem, jak to wygląda z punktu widzenia kosztów. Używania – czy Apaczka bierze jakiś tam prowizję jeszcze od tego – pewnie bierze – to bierze od tych kurierów czy bierze od klienta, nie. Od tych firm kurierskich czy bierze od klienta, który z tego korzysta? No, bo gdyby to się tak udało – no, ale ktoś to musiał by głęboko zbadać, że my robimy integrację z Apaczką. Ta integracja z punktu widzenia użytkownika jest – nazwijmy to – niejawna, czyli użytkownik nie wie, że to jest Apaczka, tylko widzi te firmy kurierskie, które są przez tą Apaczkę zrobione, nie.

**Łukasz Bott:** Nie – OK – dobra.

**Janusz Bossak:** Ale nie wiem – to jest tylko taki mój pomysł do...

**Łukasz Bott:** Wiesz co, ale to – to może być przyszłościowy, bo – tutaj – jeżeli chodzi o UPS LOT – to po prostu LOT ma konkretną umowę z UPS, no – dostaliśmy kontakt do konkretnej osoby z UPS, która jest opiekunem LOT, no – i – i tyle, tak. I tak samo z tym Global Expressem, czyli to po prostu – Global Express – kolejna firma kurierska, z którą LOT po prostu – wprowadzenie – z tą firmą ma podpisaną umowę, nie.

**Janusz Bossak:** Właśnie – to jest problem.

**Łukasz Bott:** I tyle. Więc – i wygląda na to, że z tym Global Expressem też będziemy musieli zrobić. Potrzeba rozpoznać, czy tam mają jakieś do tego...

**Janusz Bossak:** Właśnie szukam tutaj ten – o – Apaczka – to są chyba – tą – no, nie wiem – no gdzieś była taka właśnie – ten – Apaczka – nie wiem, czy to jest dokładnie – to kiedyś znalazłem jakiegoś takiego brokera właśnie kurierskiego, gdzie on – ta firma twierdzi, że ma integrację ze wszystkimi – no, sama nie jest – jakby firmą kurierską – ona jest firmą informatyczną, niektóra tylko takim proxy jest dla tych.

**Łukasz Bott:** No tak, no – i pobierają jakiś tam ułamek – ta prowizja – od tego – i tyle.

**Janusz Bossak:** Że to – sprawdzić. Dobra, nieważne – czyli mamy tak – ze WIM – tą integrację z tym KAS, a LOT – UPS, Global Express i AD.

**Łukasz Bott:** Do LOT – to z takich dużych – tam w LOT jeszcze są inne integracji, ale one są pomniejsze i raczej da się ogarnąć.

**Janusz Bossak:** I JRWA – dla LOT – i repozytorium. Repozytorium dla WIM. No – i są pomniejsze, które też tam robimy, czyli ten podpisywanie na Macu przez Szafira – to też już ma tam – niby – Adrian ogarnięte, także – pisząc...

**Łukasz Bott:** Ale to jest pod tego klienta, czy to po prostu żebyśmy mieli?

**Janusz Bossak:** WIM – WIM.

**Łukasz Bott:** WIM potrzebuję – dobra.

**Janusz Bossak:** Bo oni tam mają jakiegoś dyrektora, kogoś tam – to ma Maca – i on się nie przestawi na Windowsa i...

**Łukasz Bott:** Nie wiem.

**Janusz Bossak:** Wiadomo – oni – ja już mówiłem temu Piotrowi – Mnie – to ja – pierwsze – my mu kupimy tego SimpleSign. My – ja nie mówię – ja mogę nawet z prywatnych pieniędzy za 245 zł móc kupić tego SimpleSign i temat jest rozwiązany, bo SimpleSign obsługujemy na Macu. Po co wytwarzać jakieś oprogramowanie specjalnie, bo on ma akurat Szafira? No to niech zrezygnuje z tego Szafira i niech kupi – no – i tyle – to jest 245 zł – gotową integrację – nie – działającą. No, ale się uparli, że nie – że musi być, bo co – inaczej jest – gdy jest to nieznane grono osób, które będzie się w ten sposób podpisywać – no, to OK – nieznane grono – no, to musimy zapewnić, że nie wiadomo, co oni tam używają, a ma działać.

**Łukasz Bott:** No tak.

**Janusz Bossak:** Ale to jest znane grono i to jest tam 2 dyrektorów. To – no – kupmy im po prostu SimpleSign – i już następnego dnia temat jest załatwiony. Można odhaczyć – koniec tematu, nie. Mamy obsługę i po stronie AMODIT i po stronie TrustCenter – wszystko jest zrobione – gotowe. Jedyne – zmiana po prostu podpisu kwalifikowanego z Szafira na SimpleSign – najprostsze z możliwych rozwiązań, no – ale jakoś nie – uparł się – jak głupi – jeden człowiek – i robimy. No, ale trudne – dobra – mamy zidentyfikowane.

**Łukasz Bott:** Tutaj – wiesz co?

**Janusz Bossak:** Ja – no.

**Łukasz Bott:** To – to jeszcze tą wycenę – jakbyśmy...

**Janusz Bossak:** Wycenę – dobrze.

**Łukasz Bott:** Wycena, dlatego – to jest – to ona się troszkę zahacza o to repozytorium PKF – PKF chce – myśmy w tej chwili – wiesz – czy mamy pliki w bazie danych bądź w jakimś tam folderze, nie.

**Janusz Bossak:** Tak.

**Łukasz Bott:** Natomiast to, co by miało dojść – to oni by chcieli, jeżeli mamy to być w folderze, to – to oni chcą konfigurować, w którym folderze – może inaczej – w folderze, w którym mają być pliki załączone do spraw – per proces. A okazuje się, że Piotrek Myszkowski mówi, że już mamy taki mechanizm na poziomie pola typu dokument.

**Janusz Bossak:** Czy – pytanie jest – po czym?

**Łukasz Bott:** I mówi, że to można łatwo rozszerzyć o ten – na poziomie procesu. Użytkuję – jest jakiś tam – szczególnie trudne.

**Janusz Bossak:** Ten komentarz – pliki załączone do spraw – w tym – zarządzana przez – wymaga żadnego programisty z naszej strony – mocy najwyżej konfiguracji w danej instancji – o – przy czym oczywiście może być tą konfiguracją mieszana baza danych i przestrzeń dyskowa. Teraz – dwójka – nowość – dla wybranych procesów pliki załączane do spraw będą umieszczane w dedykowanych folderach przestrzeni dyskowej. Konfigurację tego wariantu przechowywania plików konfigurował by się z poziomu ustawień procesów w systemie. Może istnieć konfiguracja mieszana powyższych 2 opcji, czyli część plików może być przechowywana w bazie danych, część w domyślnej strukturze folderu, a jeszcze inna część we wskazanych – konfiguracji wybranych procesów – folderach. We wszystkich powyższych opcjach zwykły użytkownik będzie miał dostęp do plików tylko z interfejsu system. Administratorzy, technicznie – i nawet jeśli będą mieli dostęp do folderu, to tylko w celu wykonania kopii zapasowej – i nie mogą generować strukturę folderów lub plików – po prostu – z rurą foldery zarządza – tak – informacyjnie – z nowym kolegą Maciejem, gdyż on nie jest programistą. Rozwiązaniem – Donald Trump. Koledzy Piotra – dobrze – moje pytanie kardynalne – po co? Po co to jest? Po co my to mamy zrobić?

**Łukasz Bott:** Czy – oni chcą to w jakiś sposób sobie wydzielić.

**Janusz Bossak:** Interesuje – że chcą – po co? Po co? Jak oni z tego będą korzystać? Po co to chcą mieć?

**Łukasz Bott:** No dobrze, to jeszcze – jeszcze raz mogę o to dopytać. Tam pewnie chodziło o kwestie – być może jest zestaw spraw – na przykład – poufnych, tak – i wtedy...

**Janusz Bossak:** No – to wiedzieć – brakuje mi...

**Łukasz Bott:** Chcieliby – na przykład – w zupełnie innym miejscu fizycznie trzymać.

**Janusz Bossak:** Brakuje mnie informacji biznesowej – to jest opis techniczny – technicznie wiem – da się tak zrobić, ale po co? Po co? Po co biznesowo oni chcą mieć to wydzielone? Dowiedz się tego.

**Łukasz Bott:** Dobra.

**Janusz Bossak:** Bo to jest klucz, no. Nie – jakoś nie mogę tego nauczyć wielu osób w firmie – zawetowania pytania – po co? To mnie – nerwy – przykład – to chyba tobie mówiłem – tego Mateusza Pietrzaka – niektórymi mówi, że ma – mamy – czy – czy możemy tam wydobywać link do TrustCenter, bo on by chciał wysyłać informację do użytkownika, że dokument jest podpisany. Znaczy tego – nie – tego mi nie powiedział najpierw – tylko ogólnie – jak wydobyć link do – tego dokumentu w TrustCenter. My – i się pytam – po co? No, bo chcę wysłać maila. Ale po co? No, żeby poinformować, że ten człowiek nie – znaczy ten człowiek nie – nie jest uczestnikiem tego podpisywania, ale chcę być informowany. Wy – jedna odpowiedź – rola obserwator – koniec.

**Łukasz Bott:** No dobrze, myśmy rozmawiali.

**Janusz Bossak:** To jest – to jest – to kardynalne pytanie – po co – po co ktoś chce mieć jakąś funkcjonalność? Bo może jest rozwiązanie kompletnie inne – w ogóle w innym miejscu – i tak dalej – po co oni to chcą mieć?

**Łukasz Bott:** Dobra.

**Janusz Bossak:** Jak tego nie rozumiemy, nie wiemy – nie znamy – to według mnie to jest tylko i wyłącznie techniczne – i sposób rozwiązania – tylko po co? Po co to robić? Co to da im? Co oni chcą osiągnąć? Jak to już będą mieli?

**Łukasz Bott:** Dobra, dobra – zadam takie pytanie. No, bo technicznie to wiadomo było, że to da się zrobić.

**Janusz Bossak:** No, wszystko się da – tak – tylko po co? Po co biznesowo to jest komuś potrzebne, tak – bo chcą kupować, bo chcą archiwizować, bo chcą – chcę wiedzieć, co oni chcą z tym robić.

**Łukasz Bott:** Do Pan – OK, dobra – to ja się podpytam jeszcze.

**Janusz Bossak:** Dobra, dzięki bardzo.

**Łukasz Bott:** Dobra, dzięki.


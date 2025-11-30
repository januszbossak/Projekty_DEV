**Transkrypcja**

4 listopada 2025, 09:00AM

**Marek Dziakowski** 0:18  
Cześć.

**Anna Skupinska** 0:21  
Cześć, no jakieś tematy.

**Piotr Buczkowski** 0:24  
Właśnie miała.

**Marek Dziakowski** 0:24  
Ja bym miał jednej.

**Piotr Buczkowski** 0:28  
Podobno są tam.

**Anna Skupinska** 0:31  
Mhm.

**Marek Dziakowski** 0:32  
Jakieś zadania są miał jeden jeden temat to takiej szybkiego przegadania.  
Wynik z ostatnich analiz zgłasz i stres centy.

**Damian Kaminski** 0:43  
To znaczy no.

**Janusz Bossak** 0:45  
No to powiedz co tam ciekawego.

**Marek Dziakowski** 0:47  
Co chwilę to jeszcze Mariusza po zgłasz w wyzwaniu prosił.  
Bo on tam ze mną tam na zawał się to wyłączyć.  
Dzwonię i ogólnie pojawi.  
Mają się takie dokumenty i teraz Center, które którymi się nie zgadza z status patrząc na jakby etap w w procesy podpisywania, że wszystkie procesy są zgłoszone, nie jest to jakiś oddzielny tryb podpisywania, w którym użytkownicy mają sami to zakończyć.  
Ee, po prostu status się nie zgadzają i mąż.  
Iwe, że jest to też poniekąd.  
Takie pokłosie tych problemów pazurze z dostępem do bazy, bo gdzieś tam niektóre daty się zgadzały też.  
Z tymi awariami, gdzie nie było dostępu.  
Myślimy z Mariuszem, czy by nie robić takiej opcji? W panelu administracyjnym dokumentu, gdzie os.  
Osoba, która tam wchodzi, mogłaby zweryfikować poprawność statusu.  
Jeżeli widzimy, w jaki jest problem to mogłabym kliknąć guzik i by pokazało, że.  
Jest problem.  
Ze statusem na przykład i czy go poprawić obraz ewentualnie no jeszcze opcja jakiegoś joba, który by to automatycznie sam robił, tylko to jest trochę więcej pracy wtedy.

**Janusz Bossak** 2:17  
Kiedy, kiedy się to zaczyna?  
Znaczy jaka jest przyczyna tego, że tak się dzieje?  
Coś nie znaczy poprawianie tego ręczne to już mi się nie podoba.  
Ale ja.  
Chciałbym zrozumieć problem.  
Jaki jest Jeszcze raz, bo nie zrozumiałem?

**Marek Dziakowski** 2:34  
Problemem jest to, że są dokumenty, które mają zły status, to znaczy, że wszystkie osoby podpisały dokument, ale on nie został dodany blockchain dalej już, bo status się nie zmienił na jedynkę czy tam zmieniły, potem z powrotem ustawił na Zero, jest taki.  
Mm.

**Damian Kaminski** 2:53  
No ale czemu tak się stało? W sensie się nie zmieniło, albo się zmienił, nie wiemy.

**Janusz Bossak** 2:53  
No.

**Damian Kaminski** 2:59  
W sensie to jest przyczyną?

**Marek Dziakowski** 2:59  
To jest. No jest dobre pytanie, no są logiem, tego jeszcze nie zdążyłem przeanalizować nowych przypadków, bo to się zdarzało sporadycznie wcześniej.  
Dodałem dodatkowe logowaniu, no to przez ponad prawie miesiąc, no nic się nie działo, takiego nie było przypadku dopiero tam parę dni temu się jeden zdarzył.

**Damian Kaminski** 3:16  
Czyli może być skrajny przypadek, którego nie uwzględniliśmy albo kwestie wydajnościowe tak coś spowodowało.

**Janusz Bossak** 3:21  
Wydajnościowe jakieś obciążenie na tak?

**Marek Dziakowski** 3:23  
Jeszcze jeszcze jest, jeszcze jest opcja, że to był mogło się zgrać w czasie z problemami z dostępem do bazy danych.

**Janusz Bossak** 3:24  
Mhm.  
No właśnie.

**Marek Dziakowski** 3:31  
Gdzieś tam.

**Damian Kaminski** 3:31  
Czyli wydajnościowe tak czy był jakiś inny problem?

**Marek Dziakowski** 3:34  
To nie wydaje na ścianę, tylko te problemy, które Łukasz poskrobko zgłaszał z.  
Z microsoftem.  
Tam raz na jakiś czas na przykład logowanie nie działa na na tym nastka pokusie i tego typu czy ogólnie się nie robić.

**Mariusz Piotrzkowski** 3:46  
No na przykład poprosić sobie sytuację, jak bardzo dany się wyłączyła. No nie wiem 30 sekund, no i w tym czasie jeżeli serwer prześle jakieś dane no i baza niby powiedział aż dostanie, ale czy sobie tego nie zapisała na dysku czy gdziekolwiek to są dane wtedy zasadniczo uszkodzone. No i takie sytuacje, żeby to zapobiec. Właśnie chcemy zrobić jakiś mechanizm, który by to ewentualnie pozwolił ręcznie obejść nie.

**Marek Dziakowski** 4:07  
Ręcznie czy automatycznie no można dorobić joba które?

**Janusz Bossak** 4:07  
Znaczy.

**Damian Kaminski** 4:08  
No dobrze, ale takie status, bo no właśnie to co powiedział Janusz, że ktoś ma to klikać, no to nie jest profesjonalne rozwiązanie, to jest takie łatanie.  
A to jest problem, żeby znaleźć tego typu sprawy systemowo w sensie jakimś dziobem.

**Mariusz Piotrzkowski** 4:23  
Znaczy.

**Marek Dziakowski** 4:23  
Nie, nie, nie, nie, nie problem.

**Mariusz Piotrzkowski** 4:25  
My mieliśmy takie 3 pomysły. No pierwsze 2 już Marek o mówił, że możnaby albo zrobić ręcznie albo automatycznego joba, no jest to już coś, coś, co można by zrobić pomiędzy teoretycznie, czyli po prostu samo wyszukiwanie taki sposób, że jest jest jakiś automatyczny na bazie danych skrypt to nawet nie musiałby być na samym teraz Center, który po prostu filtruje, bo ma już sobie tego kwerendę zrobił, która wyszukuje takie błędne sprawą błędnym statusie. No i teoretycznie można go zrobić taką kwerendę, która się automatycznie wykonuje raz na jakiś czas i zbiera dane, a potem byśmy to ręcznie.  
Uprawiali. Jest też taka opcja.

**Janusz Bossak** 4:59  
Znaczy.  
Lepiej byłoby znaleźć przyczynę tego problemu tak i nie dopuścić do tego, żeby się to działo. No te, które już się wydarzyły, to można ręcznie jakoś tam popchnąć.

**Marek Dziakowski** 5:12  
Można można n status po prostu zmienić na jeden ręcznie, nawet dalej już jakby się włączył tryb podpisywali.

**Janusz Bossak** 5:12  
Ale.

**Marek Dziakowski** 5:19  
Zakończą w sensie tak?

**Janusz Bossak** 5:20  
Zakończę, no bo rozumiem, że one jakby się nie kończą z powodu braku tego przestawienia się na ten tak na tą jedynkę tam.

**Marek Dziakowski** 5:26  
Tak, tak, tak, tak, tak statusu zmian statusu.  
Więc no można można ręcznie na razie zrobić pytanie tylko czy?  
Czy nie warto też jakiegoś takiego zabezpieczenia dodatkowego zrobić, które by raz?

**Janusz Bossak** 5:38  
Nie no zdecydowanie.

**Anna Skupinska** 5:38  
Mówisz, że na przykład sprawdzać, czy baza danych naprawdę zapisała te dane, gdzie ja w niej zapisujemy?

**Marek Dziakowski** 5:43  
No ale jak to sprawdzić?

**Piotr Buczkowski** 5:46  
Zaraz zaraz.  
Co żeście zapisali do bazy danych i to się nie zapisało i nie zwróciło błędu.

**Marek Dziakowski** 5:55  
Mm.

**Janusz Bossak** 5:56  
No nie wiadomo właśnie, czy to się w ogóle zapisało do bazy danych.

**Marek Dziakowski** 5:58  
To jest tylko tak tylko takie domysły, że mogło tak być.

**Mariusz Piotrzkowski** 6:01  
Nie wiem jaka jest przyczyna dokładnie.

**Piotr Buczkowski** 6:05  
No ale to co co, ale jak się nie zapisało to przecież kolejne sprawdzenie powinno sprawdzić, że.

**Janusz Bossak** 6:05  
Znaczy.

**Piotr Buczkowski** 6:10  
Nie zapisało się, nie rozumiem.

**Janusz Bossak** 6:13  
No się.

**Marek Dziakowski** 6:14  
Sprawdzenie.

**Piotr Buczkowski** 6:18  
Po co zapisujecie do bazy danych i tyle nic nie wiem.

**Mariusz Piotrzkowski** 6:23  
No jest polecenie tyś.

**Janusz Bossak** 6:23  
No jak.

**Damian Kaminski** 6:23  
To jest zdarzenie, to jest zdarzenie jak rozumiem piotrze, może tu się nie nie zrozumieliście, że ktoś podpisuje.  
Jednorazowa akcja wskutek podpisu jest zapisanie do bazy danych, jeśli to się nie wydarzyło, no to to już tak zostało tak marku.

**Piotr Buczkowski** 6:38  
No to no to dokument jest dalej to podpisu rozumiem tak czy nie.

**Marek Dziakowski** 6:41  
No nie no wszystkie są.

**Damian Kaminski** 6:42  
Oni chyba nie wszystko po prostu częściowo się wydarzyły zdarzenia po podpisaniu, a częściowo nie, czyli został podpisany, ale nie został dodany do blockchaina, tak?

**Marek Dziakowski** 6:52  
Tak.

**Janusz Bossak** 6:53  
Ale to no właśnie, może ten trop, który mówi Piotr, to może takie sytuacje jakby.  
Identyfikować, czyli robić jakiegoś joba po stronie tras Center, który sprawdza taką sytuację, że są wszystkie podpisy, ale nie ma blockchaina i wykonać tą.

**Piotr Buczkowski** 7:10  
No teraz ogólnie to będzie w dobie robione.

**Marek Dziakowski** 7:14  
Było słudze tak, można to zrobić, że raz w miesiącu się to odpala i weryfikuje sobie te czy są takie dokumenty.

**Janusz Bossak** 7:19  
No nie no raz w miesiącu to nie no nie wiem, bo czekaj codziennie codziennie, no no jak no.

**Damian Kaminski** 7:21  
Zarzad.  
Tylko no co tydzień co najmniej, a może codziennie.

**Marek Dziakowski** 7:22  
Znaczy ja obstawiam ja. No to może być raz dziennie, ale o k no.

**Janusz Bossak** 7:28  
Znaczy, bo bo ja rozumiem, że w takich przypadkach mamy sytuację taką, że wszyscy podpisali, ale dokument jest ciągle niepodpisany, więc to nie może leżeć miesiąc, bo ktoś na to czeka na ten dokument. Tak więc to może być raz dziennie na koniec dnia czy tam wieczorem przejrzeć i jak znajdzie 1 2 5 10 takich dokumentów w ciągu dnia? No to je tam jakby systemowo popchnie.

**Marek Dziakowski** 7:37  
No tak tak.

**Damian Kaminski** 7:52  
Znaczy, no właśnie musimy mieć zawsze w takich, bo to jest wyzwanie jakieś techniczne, ale musimy postawić sobie pytanie. A co jest blokerem biznesowym? W sensie, co jest skutkiem biznesowym tego wyzwania? Bo wiecie.  
Yy sytuacja może być taka raz dziennie jest ok, ale równie dobrze może powinien być przycisk, o którym mówi Marek, bo jeśli to jest bardzo istotne, że to ma być podpisane w tej godzinie i zakończone procesowanie, żeby był dowód pod to.  
Ee bo no po prostu proces biznesowy tego wymaga. To może poza grobem powinno być jeszcze jakiś trigger, który administrator tego dokumentu, wchodząc z poziomu amo. Dita przechodząc do tras Center do tego dokumentu.  
Może wywołać tak, bo on potrzebuje już to wszyscy podpisali, ale protest tak jakby nie dobiegł końca, bo nastąpił jakiś błąd.

**Janusz Bossak** 8:46  
Znaczy no jest takie, no o k dobra, to jest dobry kierunek, znaczy jest takie zdarzenie.

**Damian Kaminski** 8:46  
Więc.

**Janusz Bossak** 8:51  
Ee po stronie amo, dita, gdzie ktoś?  
Na przykład mając tak zrobione w procesie klika, sprawdź status.  
I to byłaby dobra funkcja, żeby ta funkcja wymuszała nie tylko takie pasywne sprawdzenie statusu.  
Ale właśnie aktywne sprawdzenie statusu, czyli jeżeli ten status się nie zgadza, to jakby wymusza jego zmianę, tak znaczy podejmuje tą akcję, o którą mówimy właśnie tutaj. Tak, czyli przed udzieleniem odpowiedzi podaj mi status, ma się aktywnie ten status aktualizować po stronie tras Center.

**Marek Dziakowski** 9:32  
Jest też taka droga, bo można sprawdzić status dokumentu i status podpisujący czy w sensie, czy każda osoba już złożyła swój podpis. Jeżeli status dokumentów się z tym nie zgadza i jest możliwość wywołania endpoint, u który zakończy wymusi zakończenie procesu podpisywania, czyli ustawić status odpowiedni, sprawdzi, czy oczywiście może go ustawić i tego, że to jakby wtedy musi to pod strony klienta ktoś za modlitwa wywołać takie jest ważny.

**Janusz Bossak** 10:01  
No dlatego mówię, że według mnie taką funkcją jest ten. Sprawdź status, czek, status tam tras Center check status coś takiego, bo to.

**Damian Kaminski** 10:11  
Czy równoległe rzeczy czyli, bo są właśnie procesy podpisywania, które są krytyczne i są takie, które mają się toczyć swoim życiem? Każdy poczeka, nic się nie dzieje, więc i job, który to sprawdza samodzielnie, codziennie w godzinach gdzieś tam wieczornych, przy niskim obciążeniu.  
Ee i wywołanie ręczne dla procesów krytycznych.

**Janusz Bossak** 10:35  
No słuchajcie, a inny pomysł taki, że.  
No właśnie rozumiem, że my nie wiemy kiedy to się wydarza, no ale żeby po jakimś czasie, ale krótkim czasie.  
Typu 10 minut, 15 minut właśnie się wywoływała taka akcja tutaj, o której powiedział Marek, takiego sprawdzenia i wymuszenia końca.  
Na wszelki wypadek tak jest tam gdzie jakby nic się znaczy, gdzie wszystko się wydarzyło prawidłowo. No to nic się nie wydarzy nowego, ale jeżeli znajdzie taki przypadek, no to prawdopodobnie zakończy prawidłowo. Tym razem tak, tak jak mówicie, może była jakaś przerwa w dostępie? Nie wiem, to zbyt duże obciążenie, cokolwiek. No to po tych 15 minutach to sobie sprawdzić. Czyli musiałoby być coś takiego, że po każdym podpisaniu tworzy się jakaś kolejka.  
Którą ten job czy inny job obsługuje i po prostu po 15 minutach od podpisania sprawdza jeszcze czy tam się już ten blockchain wygenerował? Nie.

**Mariusz Piotrzkowski** 11:39  
Pytanie tylko, czy to nie w ciąży bardzo danych zbytnio takie dodatkowe sprawdzanie.

**Janusz Bossak** 11:45  
Ile tam jest ekspresem też nie wiem, no to ja rzucam pomysły, ale co będzie?

**Marek Dziakowski** 11:51  
Myślę, że tutaj jakby job chodził raz dziennie w nocy to też by to zadziałało tylko tak jak mówicie tutaj to przesunięcie w czasie. No jednym może zależeć.

**Janusz Bossak** 12:00  
Są.  
Przypadki, że ludzie czekają na podpis, teraz oni do siebie dzwonią, bo już nie raz było tak, że.  
Krzywo już.

**Damian Kaminski** 12:08  
I takie według mnie trzeba obsłużyć w pierwszej kolejności, czyli ja bym powiedział tak, skoro to się zdarza rzadko, a nie nagminnie, że my mamy codziennie takie przypadki, to w pierwszej kolejności zrobić to w kontekście wywołania ręcznego, żeby jeśli ktoś potrzebuje już teraz nie ma problem, to może to obsłużyć, a potem od razu zrobić, żeby to się odbywało też cyklicznie co noc.

**Janusz Bossak** 12:10  
Patrzyli, że tak.

**Marek Dziakowski** 12:31  
No teraz to jest to obejście, bo można tak jak mówiłem, skorzystać z funkcji finishing i po prostu zakończy i będzie tam jakby remedium na ten przypadek. No bardziej chodzi o takie systemowe od naszej strony zabezpieczenie, bo czasami jest tak.

**Damian Kaminski** 12:46  
O k to też powinno być opisane. W sensie musimy mieć na to.  
Jakąś instrukcję?  
Że jak rozwiązać ten problem?

**Marek Dziakowski** 12:58  
Tak faktycznie no dobrze było by to opisać, że taki przypadek, gdzie te statusem mi się nie zgadzają.  
Że można z tego skorzystać, bo no często nawet do naszej strony ludzie nie wiedzą.  
Jest w funkcję reguł teraz Center finish Sejmu też.

**Damian Kaminski** 13:26  
No dobra, to słuchajcie, podsumujmy.  
Czyli to co powiedzieliśmy wywołani nadchodz tu Janusz zaproponował status, ale finishing robi to samo, dokładnie tak.

**Marek Dziakowski** 13:35  
Tak.

**Damian Kaminski** 13:37  
No to trzeba tylko to opisać. Tu jest takie zadanie, a równocześnie.  
Zaprojektować joba, który będzie wykonywał to codziennie dla procesów nie newralgicznych, tak tak jak to, gdzie ktoś sobie czeka. Spokojnie ktoś ma podpisać się, podpisał, ma się ukończyć proces w całości i tyle.

**Mariusz Piotrzkowski** 13:56  
Dobrze pamiętam, że transfer jest też używany poza monolitem. Co w takiej sytuacji?

**Marek Dziakowski** 14:01  
To jest ten moment. Projekt można skorzystać, jeżeli klient będzie chciał, no tylko, że wtedy musi.

**Damian Kaminski** 14:05  
To jest rozwiązanie po stronie presenter.

**Marek Dziakowski** 14:07  
Tak, myślę sobie.  
Znaczy tu chodzi też osoby, które nie korzystają z moneta i mogą mieć teoretycznie taką samą sytuacją. Wtedy musieliby się sami zabezpieczyć. W sensie dodać możliwość skorzystania z anty pointu od tego finishing.

**Damian Kaminski** 14:16  
No tak.  
No i o k. To jest ich zadanie. Mamy do tego rozwiązanie. Proszę skorzystać z tej funkcji.

**Marek Dziakowski** 14:25  
Ale to już jakby ich zadanie już tam.

**Damian Kaminski** 14:33  
No systemy informatyczne mają to do siebie, że może coś nie zadziałać, po prostu ważne, że mamy na to jakieś rozwiązanie. No i wtedy rozwiązaniem jest ono, jeśli ktoś będzie potrzebował tego krytycznie użyć, to zrobi sobie wywołanie z poziomu postu.  
Analitycy odpali tak na serwerze, na którym to stoi mając wszystkie dane.

**Marek Dziakowski** 14:53  
No tak tak.

**Lukasz Bott** 14:57  
No że słuchajcie, tak nawyki na pewno jest opis z tej funkcji teraz niż tak jak się zauważyli, pewnie brakuje może wiedzy, że taki krok może powinien gdzieś być w procesach przynajmniej tych modlicie tak projektowanych zrobionych, więc tutaj pewnie Marek prośba o jakieś opisanie takiego scenariusza, kiedy to kiedy by to trzeba było zrobić tak i tutaj nas piątkowych spotkaniach możemy taki kącik szkoleniowej zrobić.  
Yy i i powiedzieć taki uczyliśmy wdrożeń owcu, że słuchajcie co takie i takie sytuacje, gdy się z tym spotkacie, no to musicie to funkcje.  
Teraz wywoływać tak no i to rozwiązuje taki tego typu scenariusz taki właśnie.  
Pilnego zakończenia podpisywania tak.

**Marek Dziakowski** 15:52  
O k dobra czyli.  
To już nie tylko chodzi o fundusze nik, jeżeli chodzi o tego, no bo tam to nie jest bardzo bardzo pilne, więc może to poczekać.  
Ale rozumiem, że jest zielone światło, że żeby go zrobić.

**Damian Kaminski** 16:09  
Nie no tak, no bo przecież no nie wyłapią ludzie wszystkiego sami, no nie wszyscy są na tyle.

**Marek Dziakowski** 16:13  
No tak tak.  
No to też wynikło gdzieś tam ze zgłoszenia, które w którym dokument wisi od lipca dopiero no po dłuższym dużo dłuższym czasie, kiedy w ogóle się zgłasza, bo to o to.

**Damian Kaminski** 16:23  
No właśnie.

**Lukasz Bott** 16:29  
Ale to słuchaj, to, że on wisiał?  
Tyle czasu to się ktoś upomniał o to czy.

**Marek Dziakowski** 16:36  
Tak.  
Więc się upomniał.

**Lukasz Bott** 16:38  
Może może też powinniśmy jakieś nie dać się? Nie wiem narzędzie, które umożliwia właśnie zrobienie takiego jakiegoś raportu, że że na przykład masz dokumenty liczące dłużej niż na przykład nie wiem 5 dni, tak.

**Damian Kaminski** 16:50  
Ale to to jest po stronie emo. Dita tak, bo to w sensie ten dokument nie wrócił do amo tita jak rozumiem, tak z tego względu, więc on, no to już jest element wdrożeniowy.

**Marek Dziakowski** 16:56  
Tak tak nie wrócił.

**Janusz Bossak** 17:01  
No tak, no ale nie wrócił do tego, że się po stronie trasy Enter nie zakończył proces no.

**Lukasz Bott** 17:07  
No właśnie o to chodzi.

**Damian Kaminski** 17:07  
No tak, no tak, ale no to wtedy trzeba dołożyć wykorzystanie pointa. Finisz signing do tego procesu i on wywoła skutek taki, który zakończy ten proces.  
A kwestia raportu, no to już jest wiecie, no mamy proces podpisywania, no to naturalnym jest, że w procesie podpisywania mamy etapie etapy, przygotowanie do podpisu w podpisie podpisane, więc to po prostu wisi na etapie w podpisie, bo nie wróciło stres Center.  
Po prostu nie wydaje mi się, że potrzebny jest jakieś dodatkowe narzędzie.

**Lukasz Bott** 17:44  
To znaczy, wiesz, to ja miałem bardziej na myśli dla nas narzędzi, że żeby na przykład nie wiem jakoś taki raport, czy czy monitoring taki właśnie, że o tu coś podejrzanie długo wisi, nie.

**Mariusz Piotrzkowski** 17:58  
Marek ma kwerendę, można by z tego zrobić, żeby się samo w bazie danych ona wykonywała po prostu raz na mnie wiem raz na dobę jakąś procedurą spowodowaną i zapisywał. Zapisywałam się jaką widzę.

**Damian Kaminski** 18:06  
Ale poczekajcie i nie zanim kwerendę Jeszcze raz co to ma rozwiązać w sensie kto będzie to obserwował? Co to ma nam dać, że coś wisi długo w trans Center? No bo wiecie, zrobimy coś, do czego nikt potem nie zajrzy.

**Lukasz Bott** 18:14  
No właśnie.  
To znaczy nie, no, bo to Damian dzięki za to czy trzeźwe ten.

**Janusz Bossak** 18:24  
Dobra.

**Lukasz Bott** 18:30  
Tak oczywiście nie mnie, bo to znaczy mnie faktycznie, gdybyśmy sobie dla nas zrobili taki raport, no to co? No nawet jeżeli stwierdzamy, że o coś wisi w miesiąc.  
No to mamy.

**Damian Kaminski** 18:40  
No właśnie będziesz pisał do wszystkich.

**Janusz Bossak** 18:40  
Dobra.

**Lukasz Bott** 18:42  
To właśnie więc.  
Tak no właśnie.

**Janusz Bossak** 18:45  
Marek dobra, słuchajcie, zrobimy Marek po pierwsze tak co Marek proponujesz jako rozwiązanie?

**Damian Kaminski** 18:45  
Może inaczej może inaczej, czy my mamy?

**Marek Dziakowski** 18:52  
I proponuję tego trzeba zrobić, które by to automatycznie cordobę skanował dokumenty pod tym kątem i ewentualnie poprawiał jeżeli jest taka potrzeba.

**Janusz Bossak** 19:04  
I tak zróbmy i tak zróbmy i koniec.

**Damian Kaminski** 19:05  
No właśnie, ale jeszcze w sumie Łukasz poruszył jedną rzecz, tylko to tylko szybko w tym kontekście wycisza cię piotrze, bo strasznie jest głośno. Marku, czy my teraz już mamy coś takiego jak?

**Marek Dziakowski** 19:05  
O k.

**Janusz Bossak** 19:11  
Ktoś ma?

**Damian Kaminski** 19:19  
Nie możliwość wysłania do Trade Center dokumentu do podpisu na czas nieokreślony.  
Czy można ja mogę wysłać do ciebie dokument i to on będzie wisiał 10 lat wam od teraz Center Przepraszam.

**Marek Dziakowski** 19:36  
Ogólnie.

**Damian Kaminski** 19:36  
Bo mamy coś takiego jak termin podpisania.

**Marek Dziakowski** 19:39  
Tak.

**Damian Kaminski** 19:39  
I teraz ten termin podpisania można określić, a można go nie określać. No i pytanie czy jeśli ja go nie określam, to możemy powinniśmy wprowadzić, że nieokreślony termin oznacza, że dokument czeka na zebranie podpisu? Nie wiem pół roku, no to już jest taka przestrzeń, że ja nie wiem, czy w ogóle aż tak długa jest potrzebna, ale załóżmy.  
Dajemy jakąś elastyczność do pół roku i jeśli w ciągu pół roku się to nie zostanie podpisany, no to my go wygłaszamy niezależnie od woli zlecającego podpis, no bo.  
Poza coś trzymać 10 lat?  
To zastanów się nad tym, sprawdź ewentualnie i wróć na kolejnej Radzie według mnie, bo może to już jest jakoś zaopiekowane, jeśli nie jest to trzeba trzeba pewnie do tego zrobić jeszcze jakieś wpis na wiki, że no właśnie nie będziemy trzymać dokumentów w nieskończoność, tylko nie przydzielony termin podpisu zostaje nad pisanym terminem przez nas tak jakimś określonym wrzucamy to do wiki możemy wysłać komunikat do wszystkich klientów korzystających z tras Center, że od teraz jest tak.  
No i tyle.  
I wtedy to pytanie jako tak, o ile dobrze zrozumiałem Łukasza w sensie samo się rozwiązuje. Nikt nie musi tego obserwować, czy coś wisi, czy nie wisi po prostu mija określony czas, który przyjęliśmy.  
Dany proces w trans centry jest zakończony w wyniku braku podjęcia akcji koniec.

**Lukasz Bott** 21:10  
Mam niebieskie, mniej więcej o to mi chodziło.

**Marek Dziakowski** 21:15  
K.

**Damian Kaminski** 21:19  
Przygotuj się na kolejny marku na kolejną radę i i daj nam tutaj wynik twojego śledztwa w tym zakresie mamy zdefiniujemy jakieś sensowne ramy biznesowe do tego.  
Dobra, przechodzimy do bieżących tematów czy coś jeszcze?

**Janusz Bossak** 21:45  
No to był też bieżący.

**Damian Kaminski** 21:47  
No w sensie do zgłoszonych może?

**Lukasz Bott** 21:49  
Nie, to znaczy tak, Daniel powiedział, nie miałem na myśli, miałaś na myśli te, które gdzieś tam od lat pisze o na radę architektów? Tak.

**Damian Kaminski** 21:57  
Znaczy już nie od lat już nie od lat, w świetle już tu naprawdę to jest rada architektów bez żadnego.

**Lukasz Bott** 21:59  
No nie, no ale okej, dobra do.  
Znaczy, słuchajcie, na pewno dobra to z takich.

**Damian Kaminski** 22:07  
A nie nie bez żadnego.  
Z ostatnich 30 dni i to powinniśmy przede wszystkim wyczyścić.

**Lukasz Bott** 22:11  
Dobra.  
Dobra, to za wiesz co to za chwilę, bo ten, bo to co wyszło z taki bieżąco bieżące ek tak.  
Bieżących rzeczy to to ta kwestia.  
Moduł dla tych usług jajowych, że tam się nagle wyszło, że mam to już dorobił, no w jakiś tam dobrej wierze tak pewnie rej.  
Normalnie tego co tam się jest przetwarzane tak to już się okazało, że faktycznie możemy tutaj o o rodo i nie rodu i tym podobne rzeczy tam zahaczyć. Rozumiem, że to jest w ogóle temat do omówienia, pewnie to jest z Mateuszem, to może na to zrobimy od odrębne spotkanie, no.

**Janusz Bossak** 22:52  
To jest temat zap.

**Damian Kaminski** 22:52  
Już to omawialiśmy wczoraj wstępnie z januszem i z Mateuszem powstały z tego konkluzje i jeszcze nie zdążyłem zrobić z tego PI, natomiast jest trochę przemyśleń jak to rozwiązać i tak na pewno trzeba to spisać i się nad tym pochylić na dedykowanym spotkaniu, bo tam są zadania po stronie i tego biling owego serwisu i samego amo tita.

**Lukasz Bott** 22:57  
O k dobra.  
O k. Dobra. No to jeżeli to jest.

**Damian Kaminski** 23:16  
I w zasadzie może od tego zacznijmy, bo to jest związane z tym temat. Na razie jeszcze bez opisu, bo tu bardziej pytanie właśnie może do Piotra, jaką on ma sugestię, bo wczoraj podejmowaliśmy właśnie taki temat, w jaki sposób jeszcze po stronie amo tita wykryć i zapobiec wysyłania tych samych plików do a i CR.  
Bo możemy oczywiście wyliczać hasz.

**Janusz Bossak** 23:44  
Bo ja, bo ja, bo ja, bo ty już mówisz o rozwiązaniu, bo tam tej dyskusji wyniknęły 2 przypadki, w których może wystąpić.

**Damian Kaminski** 23:46  
No.  
Dobra.

**Janusz Bossak** 23:55  
Jeden taki, który był kiedyś zeskanuj to co nam tam naliczyli, potem chyba 20000 zł za przetwarzanie tego samego dokumentu, który był wysyłany wielokrotnie z reguły okresowej tam co minutę przez cały Weekend nie i tam wysłał się kilkadziesiąt 1000 razy. W tym czasie to jest jeden przypadek i to podobno mamy obsłużone, bo tam jest jakaś para.  
Fors.  
Który musi być ustawiony, żeby ponownie się ten dokument o c rysował i żeby się tam naliczało.  
Oferowanie w tym momencie tak natomiast, jeżeli tego parametru fors nie ma ustawionego, no to on wie, że już taki dokument był i drugi raz go nie robi.  
Czyli tą sytuację mamy obsłużą. Mateusz podał drugą sytuację potencjalnie możliwą.  
O której rozmawialiśmy o mianowicie zakładanie sprawy z maila.  
Czyli.  
Kiedy to może nastąpić wtedy, kiedy będzie jakiś problem po stronie?  
Ee właśnie tego mechanizmu zakładania sprawy z maila, że z jakiegoś powodu.  
Yy ten sam mail.  
Będzie powodował co tam period odpowiedni, czyli co 5 minut na przykład na nowo założenie sprawy z tym samym dokumentem i ten proces ruszy. Wyślę ten dokument do oc, a i tak dalej i ja powiedziałem wczoraj tyle, że to nie jest problem o CRUOC era, tylko problem zabezpieczenia tego mechanizmu zakładającego sprawy, żeby nie zakładał spraw z tego samego maila na skutek błędu w tym mechanizmie, tak.  
Czyli nie wiem, serwer pocztowy się nie wiem, nie wiem co się może wydarzyć, tak zaciął, nie.

**Damian Kaminski** 25:46  
Po prostu błąd komunikacyjny.

**Janusz Bossak** 25:48  
Tak jakiś błąd komunikacyjny gdzie my niby ustawiamy to jako odczytana to się ta sprawa w skrzynce pocztowej ona się nie zapisuje jako odczytana, czyli ciągle jest do odczytu, no i za 5 minut ją znowu już odczytujemy. Zakładamy nową sprawę i tak dalej, i to na razie. To są 2 przypadki, których mowa.  
Może dojść do takiego masowego.  
Wysyłania dokumentu tego samego do oc sera, no i to jest jakby kontekst tego pierwszy kontekst.

**Damian Kaminski** 26:18  
Czy analogią do tego jest jeszcze zakładanie z pliku tak, gdyby nie było uprawnień? Edycji zapisu do danego zasobu sieciowego, to też będzie ten sam skutek. Z tego co kojarzę, czyli po prostu odczytujemy ten plik. Nie możemy go skasować po odczytaniu znowu odczytujemy znowu odczytujemy.  
Ale to jest ten sam mechanizm, zakładanie z pliku czy z maila.

**Janusz Bossak** 26:37  
Tak.  
Tak no i moja konkluzja wczoraj była na koniec spotkania taka, że to nie jest problem o cera.  
Znaczy, nie chciałbym, żeby o CR był jakby.

**Damian Kaminski** 26:49  
Tylko.

**Janusz Bossak** 26:53  
Tym meczem, gdzie to się łapie tak tym meczu?  
Bo to już jest za późno, to my musimy rozwiązać problem z zakładaniem sprawy z maila i z zakładaniem sprawy z pliku, żeby tutaj ten mechanizm zadziałał i nie będzie wtedy problemu z serem, że pójdzie coś wielokrotnie do tego celu, tylko tyle taki był mój.  
Postulat.

**Damian Kaminski** 27:17  
Ja jeszcze uzupełnię pierwszy przypadek, bo on nie jest rozwiązany forstem dlaczego dlatego, że.  
Dzisiaj świat na dzisiaj, powiedzmy pewnego rodzaju świadomość jest co do używania forsa, że trzeba dodać parametr forces, aby Jeszcze raz ten sam dokument wysłać do cera, natomiast ja tu widzę duże ryzyko przeniesiony.

**Piotr Buczkowski** 27:40  
W Rosji jest taka zasada, że to myślenie jest z reguły ręczne, jest wydawany w Polsce.

**Janusz Bossak** 27:46  
No właśnie.

**Piotr Buczkowski** 27:47  
Czy jest jakaś naciśnie przycisk to jest dodawany w Polsce, jeżeli działa z reguły automatyczne, nie jest dodawany w Polsce.

**Damian Kaminski** 27:47  
No.  
I to jest natywnie.

**Piotr Buczkowski** 27:55  
Tak.

**Damian Kaminski** 27:56  
A o k no to to uzupełnienie, to to wszystko właśnie, bo ja się obawiałem, że tu ktoś wstawi przy testach.

**Janusz Bossak** 28:01  
Czyli to nie jest tak, że ktoś wpisze sobie fors ustawieniach wysyłki.

**Piotr Buczkowski** 28:07  
Nie.

**Janusz Bossak** 28:08  
O k.

**Damian Kaminski** 28:08  
O k no to super to to jest bezpieczne w takim wypadku, bo no właśnie.

**Piotr Buczkowski** 28:14  
Ręcznie jak nawet jak nawet wyślesz ponownie, to wyślesz 2 3 razy, a nie 2000 razy.

**Damian Kaminski** 28:14  
Ja się obawiałem, że ktoś wpisze i.  
Tak jest o k.

**Janusz Bossak** 28:19  
No tak, tak tak, no bo czasami trzeba wysłać 2 3 razy, bo te stój, bo testujesz coś, sprawdzasz tak, coś nie wyszło Jeszcze raz, ale to jest oczywiste, że ten, no ale tak.

**Piotr Buczkowski** 28:22  
No tak.

**Kamil Dubaniowski** 28:29  
Znaczy, to tak, masz pewność, że to jest też w tym nowym, tak jak naszym nie skanuj to było skanuj to kojarzę, że tak było.

**Damian Kaminski** 28:30  
No.

**Piotr Buczkowski** 28:36  
Ja mówię jakie Wschodu i to.

**Damian Kaminski** 28:38  
A no to o k to no to to jest rozwiązanie super do tego czyli wysyłanie.  
Z jednej sprawy wielu takich samych dokumentów, reguły okresową.  
Powinno kastrować.

**Piotr Buczkowski** 28:52  
Znaczy tam mówicie, że to nie jest kwestia Zero, to jest kwestia cera, żeby oceny się przy takim czy nie bronił.  
Tak samo jak się broni skanuj to.

**Janusz Bossak** 29:02  
A jeszcze jedna była kwestia poruszana przez Mateusza, a mianowicie dużych plików tak typu 100 stron na przykład.  
I tam mamy jakiś mechanizm, bo pamiętam przynajmniej tak do skanu i to było, że można było ograniczyć ile stron idzie do oc era i też tutaj jest pytanie jak to zrobić z tym naszym teraz nowym oc serem?

**Lukasz Bott** 29:28  
Znaczy, wiesz, no znaczy tak, jeżeli kto, jeżeli Użytkownik jest świadomy, że tego jest dużo tak, no to może być kwestia zastosowania mechanizmu wydzielania stron. Tak, no ale to jest obsługa manualna.

**Janusz Bossak** 29:42  
No tak, no ale chodzi o to, że wiesz.

**Lukasz Bott** 29:42  
Yy.

**Damian Kaminski** 29:42  
Dobra, słuchajcie, to może może po kolei ja bym sugerował, że to co to co powiedział Piotr jest super rozwiązaniem, czyli po stronie amo. Dita, mimo że ten parametr już został zgłoszony i jest opublikowany na na naszym tym.

**Janusz Bossak** 29:45  
No.

**Damian Kaminski** 30:00  
W tym taksie.  
Trzeba go wywalić.  
I po prostu dodać to natywnie. Ten parametr ma być kasowany z reguły okresowej ma być dodawany do reguły ręcznej i tyle i wtedy nikt nie ma problemów jak ktoś chce ręcznie wysłać 10 razy ten sam dokument to jest jego wola, co jest oczywistym przypadkiem testowym dla wszystkich wdrożeń faktur, które testujemy. Ktoś testuje 10 razy sprawę w różnych przypadkach wysyła tą samą fakturę, no bo.

**Piotr Buczkowski** 30:27  
Gdzie ma być ten parametr analizowany?

**Damian Kaminski** 30:32  
Co to znaczy?

**Piotr Buczkowski** 30:33  
Faworycie trzeba cerze.

**Damian Kaminski** 30:35  
Wa modlicie według mnie.

**Janusz Bossak** 30:39  
Według mnie potterze też no bo.

**Piotr Buczkowski** 30:41  
No tak.

**Damian Kaminski** 30:43  
Bo jak w o w w sensie?  
Czemu jeszcze w o cerze?

**Lukasz Bott** 30:48  
Oceną stali.

**Piotr Buczkowski** 30:50  
Musisz sobie prze.  
Odbywać listę haczów przetworzonych plików.

**Damian Kaminski** 30:55  
No tak, mhm.

**Piotr Buczkowski** 30:56  
Jeżeli znowu w nowo wysłaniem pliku.  
Nie ma forse i hasz znajdzie to zwraca tak jak taka stanowi to zwraca że duplikat.  
Nie przyjmuję takiego pliku.

**Damian Kaminski** 31:10  
No tu jest jeszcze inny parametr, zaraz może do tego wrócimy, natomiast w sensie jeśli my to zaopiekujemy po stronie amo tita, że jest Force albo nie ma forsa i to jest.

**Piotr Buczkowski** 31:19  
I tu i tu.

**Damian Kaminski** 31:24  
No.

**Janusz Bossak** 31:24  
Zobacz, jak dlaczego i tu i tu Piotr.

**Damian Kaminski** 31:26  
No właśnie.

**Piotr Buczkowski** 31:28  
A chcecie bezpiecznie czy nie?

**Janusz Bossak** 31:30  
No tak, no ale powiedz.

**Damian Kaminski** 31:31  
Nie, no ale poczekaj czy da się zrobić obejście tego, że natywnie to amok i doda albo usunie?

**Piotr Buczkowski** 31:38  
Ja mówię o tym, gdzie to być analizowane.

**Damian Kaminski** 31:38  
Sprzedajecie inaczej?

**Lukasz Bott** 31:43  
Zgodzę się z piotrkiem po stronie po stronie silnika o c powinny.

**Janusz Bossak** 31:45  
Wyłapywane no no.

**Piotr Buczkowski** 31:47  
To, że sobie ustawisz forsy to to znaczy, że gdzieś jeszcze to musi być zrealizowane, tak.

**Damian Kaminski** 31:52  
A nie no to oczywiście, no to to musi być interpretacja postu, to tak to może tu się nie zrozumieliśmy. Co do oczywistej rzeczy, że tutaj po prostu.

**Lukasz Bott** 31:52  
Czy?

**Piotr Buczkowski** 32:01  
Nie było ustawianie Force oczywiście po stronie mohito, ale analizowanie tego, czy jest w Polsce, czy nie i jak nie ma forse to sprawdzanie czy tam ten dokument już nie był przetworzony to po stronie ocen.

**Damian Kaminski** 32:06  
Tak oczywiście.  
To jasne, o to tak tak, czyli tylko chodzi o to, że aamodt sam zaopiekuje zależności od typu reguły, czy to dodaje, czy tego nie dodaje.

**Piotr Buczkowski** 32:21  
No tak.

**Damian Kaminski** 32:23  
Teraz, jeśli tego nie dodaje, to znaczy to teraz tak pytanie, co ma się stać, bo tu jeszcze poruszaliśmy kwestię, że tak ze względów bezpieczeństwa chcemy wykastrować biling z treści dokumentów, czyli to ma być obsługiwany na bieżąco.  
Ale z kolei pytanie.  
Co jeśli ktoś?  
Załóżmy, że nie mamy forsa i ktoś to wysyła i teraz jak możemy to obsłużyć.  
Ee mogli.  
Przechowywać odpowiedź po stronie amo. Tita w gotowy wymagałoby rozbudowania modlitwa, czyli.

**Piotr Buczkowski** 32:59  
Ale o co chodzi?  
Nie rozumiem.

**Janusz Bossak** 33:03  
No no chodzi o to, że jeżeli ktoś jest wysyłają drugi raz, to czy ma dostać już gotową odpowiedź od zera?

**Damian Kaminski** 33:09  
Odpowiedź.

**Piotr Buczkowski** 33:10  
Nie ma zostać błąd, że duplikat.

**Janusz Bossak** 33:14  
O k.

**Damian Kaminski** 33:15  
O k.

**Piotr Buczkowski** 33:19  
Po stronie ocena, bo się być tabela z listą chaszczy przetworzonych dokumentów.

**Janusz Bossak** 33:19  
Tak no bo.

**Piotr Buczkowski** 33:24  
Dokładnie zaindeksowane tak żeby.

**Janusz Bossak** 33:24  
Tak.

**Piotr Buczkowski** 33:26  
Przychodzi dokumenty wyliczamy has sprawdzamy czy jest tutaj tebel, jeżeli jest to zwracamy błąd jeżeli nie no to przyjmujemy do przetworzenia.

**Janusz Bossak** 33:33  
I teraz pytanie o tą tabelę haszysz rozumiem, że to tabela chaszczy powinna być w tym micro serwisie o CR owym.  
O k po tamtej stronie, tak?

**Piotr Buczkowski** 33:43  
Tak.

**Lukasz Bott** 33:47  
Chyba, że przyjdzie dokument z atrybutem Force troom tak, bo wtedy nawet jeżeli.

**Piotr Buczkowski** 33:52  
No to wtedy nie nie musi sprawdzać.

**Lukasz Bott** 33:56  
Kasza dziękuję.

**Damian Kaminski** 33:58  
Dobrze, teraz co z sytuacją taką, że ktoś zrobi?

**Piotr Buczkowski** 34:00  
Znaczy.  
Dobrze.

**Damian Kaminski** 34:03  
Mhm.

**Janusz Bossak** 34:04  
No mów mów Piotr.

**Piotr Buczkowski** 34:07  
To czy czy ktoś oprócz czy z tego ma.  
Właśnie sprawdzałam o dita jest to już ta spoza morita tylko czy tylko czy to trzeba morita?

**Damian Kaminski** 34:17  
No nie korzysta.

**Lukasz Bott** 34:17  
To znaczy tak.  
Czekajcie, czekajcie w to znaczy, tak?

**Damian Kaminski** 34:19  
No.

**Lukasz Bott** 34:24  
Microservices ten do do ogólnie do tych wszystkich usług a jajowych ma własne restauracje i możesz teoretycznie możesz z tego skorzystać. O ile tą specyfikację i takiej gdzieś tam był początkowo zamysł, ale potem zmieniliśmy to, że jeżeli bo mamy właśnie takich, no w tej chwili 2 może się trzeci klient szykuje taki, który właśnie który potrzebował zin.  
Wprowadź swój na swoje narzędzie jakieś tam informatyczne, bo oni tam nie mieli oc era do tutaj głównie dotyczy faktur no i teraz no i teraz właśnie opcji były takie, albo im dajemy specyfikacje rest apy bezpośrednio micro servisu tylko w obrębie tych właśnie funkcję obserwujących, ale stwierdziliśmy, że jednak nie nie dajemy, tak nie dajemy, bo wolimy mieć nad tym kontrolę, więc w tej chwili podejście jest takie, że.  
Musisz sobie zainstalować jedno licencyjnego amo dita, w którym konfigurujemy mu proces, który właśnie wysyła do obserwacji, a wszelką komunikację, czyli wysyłkę dokumentu do do CA odbiór jakichkolwiek danych tak po cyfryzacji robi poprzez rest api amo dita tak czyli.

**Damian Kaminski** 35:46  
No i to jest, zabezpiecza to no i super i wtedy nie mamy sytuacji takiej, że no.

**Lukasz Bott** 35:50  
Tak, ale.  
Tylko pytanie jest takie i tuby i rozumiem tutaj piotrka, że Piotrek zadaje to pytanie, czy nie przewidujemy jakiegoś?  
Przyjdzie, nie wiem, jakiś klient, który miliony nam zapłaci i on nie chciała mu dita, ale chce naszego ocena.

**Damian Kaminski** 36:09  
No tak, zapłaci miliony to bierze na siebie odpowiedzialność i wtedy powinna być dokumentacja do tego właśnie z tym, że trzeba tak to zabezpieczyć jak my to zabezpieczamy to trzeba potem jeszcze opisać w naszym restauracji czy w naszym ażurowym wiki, że jeśli ktoś by się łączył to na siebie bierze odpowiedzialność, że reguły cykliczne nie mają prawa wysyłać parametrów fors i koniec.

**Janusz Bossak** 36:09  
To będziemy się do innych.

**Lukasz Bott** 36:34  
Czy?

**Damian Kaminski** 36:34  
To jest nasze zalecenie, a jak ktoś wyślę no to ponosi tego odpowiedzialność.  
Yy no.

**Lukasz Bott** 36:39  
O k no dobra, dobra no.

**Damian Kaminski** 36:42  
No i teraz znowu możemy się spierać, czy to, że to przekazaliśmy, jest wystarczającym, żeby ktoś potem zapłacił rachunek za wysłanie jakiegoś limitu, przy czym też mamy te limity miesięczne, więc no jak ktoś w danym miesiącu zapłacić za kwotę dwumiesięczną, to według mnie też mu nie ubędzie z kieszeni. W sensie to nie zrobi z tego afery.

**Lukasz Bott** 36:53  
Daniel.  
Damian, to o czym mówisz, to te rzeczy takie właśnie zabezpieczenie zabezpieczenia naszego biznesu, tak że że ktoś za głupie wysłanie nieświadomie, pomimo tak, że myśmy go ostrzegali, gdzieś ten, to to właśnie wszystkie ostrzeżenia. Czy te warunki to powinny być wpisywane w ogólnych warunków użytkowania, a i o c tak no jest teraz nawet mi Monika pietruszewska gdzieś tam.

**Damian Kaminski** 37:05  
No.  
No tak.

**Lukasz Bott** 37:34  
Do do tej do.  
Do tutaj podesłała do konsultacji tak kolejno tam.  
Iterację tak tego dokumentu właśnie umowy dla jaja c tak no ale rozumiem, że na razie tego, że.

**Damian Kaminski** 37:48  
Dobra, słuchaj się do.  
To jest już formalność, bo teraz zwróćmy tylko do do tutaj do tego, bo tak to są przypadki dla zabezpieczeniach w ramach wywołania stej.

**Lukasz Bott** 37:52  
Tak.

**Damian Kaminski** 37:59  
Samej sprawy.  
Pytanie.  
I to dotyczy reguły. Sent tu o cer, tak.  
Tam jest tutaj.

**Lukasz Bott** 38:14  
Wiesz co, nie to jest. No już ci mówię, jeżeli chcesz.

**Damian Kaminski** 38:15  
Ktoś kojarzy?  
Dobra, a teraz co z tym? Bo to jest odrębny, powiedziałbym przypadek.  
Jak to zabezpieczyć?  
Czyli mamy problem?

**Piotr Buczkowski** 38:34  
Znaczy, to jest inne zadanie, które jest opisane. Jest zadanie zrobione pewnie odłożone na święte nigdy jak to służyć.

**Damian Kaminski** 38:35  
Krok wcześniej.

**Piotr Buczkowski** 38:44  
Po stronie obu dita tak.

**Damian Kaminski** 38:46  
Jest już opisane tak.  
Dobra, coś powiesz więcej?

**Piotr Buczkowski** 38:53  
Dodać dodać, dodać oddzielnych jak je znaleźć.

**Damian Kaminski** 38:53  
Jak jak go znaleźć?  
To mam na myśli.

**Piotr Buczkowski** 38:59  
Już.

**Damian Kaminski** 39:00  
Skoro jest opisane to weźmy gotowce.  
Dawno czy niedawno?

**Piotr Buczkowski** 39:30  
Dawno.

**Damian Kaminski** 39:31  
Dawno.  
To.

**Lukasz Bott** 39:34  
Damian, na czacie wróciłem się nazwę tej funkcji, obecnie, który powinno się używać do.

**Damian Kaminski** 39:35  
No.

**Lukasz Bott** 39:40  
A ja chcę.

**Piotr Buczkowski** 40:04  
Napisałem tobie.  
Dobrze, nie potrafię znaleźć.

**Damian Kaminski** 40:20  
No dobra, to jakbyś mógł dopowiedzieć?

**Piotr Buczkowski** 40:23  
Ogólnie teraz jest tak, że.  
To.  
Popiera nie odczytane maile ze skrzynki.  
Pobiera jeden bajt od przetwarza to go zaznacza. Jak odczytano było słowem zależności od ustawienia. Tak?  
Yy.  
Chodzi o to, żeby dodać oddzielną.  
Pośrednio tabelę tak.  
Że wczytujemy mail.  
Zapisujemy w tabeli jego identyfikator.  
I przetwarzamy tak jak przetwarzamy. Zaznaczamy, że tworzyliśmy usunęliśmy wtedy.  
Ponownym wczytaniu prawda czytałem na następny mecz, sprawdzamy tej tabeli czy był przetworzony, jeżeli nie był to przetwarzamy, dodajemy tak, dodajemy przetwarzamy. Zaznaczamy, że przetworzone.  
W tym przypadku, jeżeli nie uda się to zaznaczanie jako.

**Damian Kaminski** 41:24  
Jakieś błąd połączenia?

**Piotr Buczkowski** 41:25  
Jako przetworzone to już przed sprawdzaniu, czy przetworzyć dany mail, zostanie to wykryte, że już przed tworzyliśmy.  
Numer sprawy tak, czyli tabela gdzie jest?  
Z maila sprawy utworzonej tak kiedy powiedzmy czy?  
Status nie wiem cokolwiek.

**Damian Kaminski** 41:44  
Okej, a dla pliku przy czym tu trzeba zwrócić uwagę, że ja mogę celowo chcieć wczytywać drugi plik to musiało być powiązane. Według mnie też z datą jakąś modyfikację tego pliku, tak?

**Piotr Buczkowski** 41:54  
Mały co znaczy pliku?  
A z plików?

**Damian Kaminski** 41:57  
No bo no właśnie.  
Rozumiesz o to mi chodzi, że wrzucam jeden za chwilę ten sam.

**Piotr Buczkowski** 42:06  
Tak, tak, to to to nie było.  
Jakbym to też co było podobny sposób tylko wymyślać co będzie identyfikatorem pliku, bo oddzwoń niekoniecznie musi być dobrym pomysłem, bo.

**Damian Kaminski** 42:23  
Znaczy hasz według mnie i data modyfikacji tego pliku.

**Piotr Buczkowski** 42:28  
No tak tak.

**Damian Kaminski** 42:29  
Bo to by było połączenie, że no jak wrzucam drugi raz ten sam, no to ma już inną datę modyfikacji, powiedzmy tak, albo mogę go zapisać ponownie i ma zmienioną datę modyfikacji.

**Piotr Buczkowski** 42:37  
Pytanie pytanie, czy takiej plik ma jakieś na przykład we te fe się identyfikator? Nie wiem.  
Maseczki w mailu jest.  
Który jest tam jakieś unikalnym guide?  
I to jest bardzo dobrym, tak?  
Identyfikatorem.  
Maila z prawie utworzonej tak.

**Damian Kaminski** 43:11  
No dobra, to pewnie do rozpisania.  
A tu dam, czyli tu wtedy hash.  
Pliku.  
I datą modyfikacji.

**Piotr Buczkowski** 43:29  
Pewnie znalazło też warto tak, żeby było wiadomo.

**Damian Kaminski** 43:48  
Pomyslow, d czy skan chyba?  
No dobra to.  
Mamy to rozpisane, ja to rozpiszę na 2 zadania odrębne.  
Powiedziałbym, że to jest. To jest wyższy priorytet. No to to zaraz za tym tak.  
Dobra pytanie, czy mamy przestrzeń, żeby kontynuować?  
Tu mamy nie wyszukuje spraw.  
Aha, to w zasadzie nie mamy odpowiedzi, więc czekamy. Zostawmy to może jeszcze na tej Radzie Tomek dostał wytyczne, chyba, że z tobą się kontaktował. Piotrze, czy nie kojarzysz?

**Piotr Buczkowski** 44:35  
Ale to polpharma o nie, to ktoś ktoś sin.

**Damian Kaminski** 44:37  
Tak to jest ten lusi nie miał tam przetestować.

**Piotr Buczkowski** 44:40  
To w rossmanie.  
Testowaliśmy, naprawienie indeks w Polsce jest walka o indeksy, same prawo chyba.

**Damian Kaminski** 44:50  
O k.  
No to może tutaj zrobił to samo, no.  
Wiedza jest w dziale serwisu, więc.

**Piotr Buczkowski** 44:56  
Ale albo Kacper przez przez pomyłkę nie uruchomił tego fix indeks na na kopii tylko na produkcji i poprawił produkcji.  
Miał skopiować tak skopiował indeks, miał na tym ich kopie indeksu, przetestować naprawdę nie indeksu z luka.  
Jak naprawił to okazało się, że usługa już działa indeksuje się wszystko poprawnie.

**Damian Kaminski** 45:29  
No to dobrze.  
Dobra, tu jeszcze jest coś coś świeżo w miarę podpiął pod.  
Aha pod ciebie, ale ktoś to też podpiął pod radę.  
Względna kategorii maili o zmianie na sprawie wysyłanych do osób z CI con.  
Chodzi o maile o edycji dokumentu, dodania komentarza i tak dalej. Teraz są one traktowane jako powiadomienia główne, tak samo jak powiadomienia o przekazaniu sprawy do danego użytkownika. Może powinny być traktowane jako powiadomienia dodatkowe, tak, aby można było je sobie wyłączyć w panelu użytkownika.  
Myślę, że ma to sens.  
Nieraz były zagwozdki co jest co i dlaczego.  
To akurat jest główny to to.  
Jest gdzieś taka tabela jak to jest?  
Inte jak każdy typ maila jest interpretowany.  
Ale nie wiem kto obecnie jest jej posiadaniu, raz ją widziałem w excelu, gdzieś ktoś to spisał.

**Piotr Buczkowski** 46:51  
To znaczy.

**Damian Kaminski** 46:55  
Jeszcze raz powiedz.

**Piotr Buczkowski** 46:57  
Dobrze i.

**Janusz Bossak** 46:59  
No ja ja mam taką tabelę gdzieś w tym excelu.

**Damian Kaminski** 47:02  
Znaczy, słuchajcie, to odpowiedzmy na to pytanie, czy to ta propozycja jest zgodna? Jeśli tak, no to w zasadzie decyzją rady tak zmieniamy taką kategorię i temat jest zamknięty, bo to jest proste pytanie na konkretne zagadnienie.

**Janusz Bossak** 47:17  
Ale nie chciałbym tak szybko zmieniać. Dlaczego?  
No to jest co teraz fakt jako powiadomienia główne tak samo jak powiadomienia przekazaniu sprawy do tego rzadko może powinny być traktowane jako dodatkowe. Tak nie ja bym tak. No tak szybko nie zmieniał, bo jeden kto kto tak napisał wpisałeś, a to a wam wreszcie tak chcieli.

**Damian Kaminski** 47:21  
O k dobra.

**Piotr Buczkowski** 47:39  
To z rozmowy z awansem tak po rozmowy zabrał z tym, dlaczego po co oni dostają takie maile?

**Janusz Bossak** 47:44  
Czy wydaje mi się, że ten?  
Wydaje mi się, że tam to jest większa sprawa, jeśli chodzi o te powiadomienia, tak to jest cały szereg różnego rodzaju rzeczy, może trzeba więcej grup, może trzeba customowe jakby budować zasady wysyłanie powiadomień, czyli co ma być wysyłane kiedy.  
Więc to jest do przemyślenia. Ja bym takich szybkich zmian nie robił.

**Damian Kaminski** 48:11  
O k. Kto wie gdzie jest ta tabela? Ty Janusz mówi, że masz tą tabelę tak wywołać cię tu w komentarzu, żeby ją tu gdzieś jakoś podpiąć.

**Janusz Bossak** 48:15  
Tak.  
No wywoła imię, ja muszę ją poszukać, bo nie wiem gdzie mamy, ale ale mam komuś przekazywałem ono gdzieś już była w miarę publiczna.  
Nie wiem czy gdzieś pod wiki wewnętrzne nie jest podpięta, ale sprawdzę.

**Damian Kaminski** 48:33  
Mhm, no właśnie, żeby to tutaj spiąć i już nie będę teraz tego szukał. No i trzeba pewnie poświęcić temu jakiś design i ustalić co tam jest do do zdefiniowania.

**Janusz Bossak** 48:46  
Jeśli byłem z Rafałem.

**Damian Kaminski** 48:49  
To znaczy tylko zastanawiam się nad tym, co z tym zrobić, żeby to nie przepadło, bo nie ja bym to odpiął od Piotra.  
Tylko czy ktoś jest chętny, żeby ten temat zaopiekować?

**Anna Skupinska** 49:05  
Jedna kategorii maili o zmianie na sprawie wysłanych osób z cte dokonano, kto kończyło do przepisać. Jeżeli nikt się nie zajmował.

**Piotr Buczkowski** 49:11  
Tylko, że to to nie jest, to nie jest pytanie o.

**Damian Kaminski** 49:12  
To ja pytam o.

**Janusz Bossak** 49:13  
Nie, nie, nie, to nie.

**Piotr Buczkowski** 49:15  
Kto to wykona? Tylko czy jest sens to wykonywać tak.

**Damian Kaminski** 49:18  
Kto to tak? Czy jest sens, trzeba się pochylić nad całą dobę, to znaczy to jest tania. Nie pytanie jakiego dewelopera, tylko kogo z nas tutaj? W sensie ja Łukasz Kamil.

**Anna Skupinska** 49:19  
Aha.

**Damian Kaminski** 49:39  
Dobra przypiszę to do siebie, skoro nie ma chętnych.  
No ale trzeba temu poświęcić po prostu jakieś spotkanie i.  
Bo tutaj no jest to niedopowiedzenie nie o edycji dodaniu i TPITD tak, czyli trzeba określić co to jest to i TD. Jeśli zmienić to zmienić to raz zrobić jakieś tego pewnie.  
Wpis na wiki.

**Janusz Bossak** 50:04  
Już znalazłem ten już na ta na czata wrzucam artykuł na wiki wewnętrznym, w którym jest to tablica.

**Damian Kaminski** 50:13  
O k no to trzeba to według mnie po prostu już zaopiekować.  
Całościowo i pewnie też opublikować to w jakimś okrojonym zakresie na wiki głównym, tak, żeby ktoś wiedział jakie.  
Zmieniając to ustawienie w profilu na co to będzie miało wpływ?  
Bo to były wielokrotnie pytanie, ja pamiętam na wdrożeniach.  
A kiedy?

**Janusz Bossak** 50:42  
Żeby to tablice z stworzyliśmy z Rafałem. Nie wiem ile lat temu ile lat to już nie pracuje. 8.

**Damian Kaminski** 50:48  
No.  
Może być nieaktualna, tak to masz na myśli.

**Janusz Bossak** 50:52  
Żeby być lekko nieaktualna, tak?

**Damian Kaminski** 50:55  
No to tu na pewno będzie jeszcze potrzebne wsparcie jakiegoś dewelopera, który nam.  
To zweryfikuje, no ale to musimy po prostu to zaplanować, bo to jest większy temat.  
Się no.  
To nie jest na godzinę, nie?  
Żeby to zdefiniować i.  
I przeanalizować i.  
I poprawić.

**Piotr Buczkowski** 51:20  
Raczej nie.

**Damian Kaminski** 51:27  
No dobra.  
To zdejmę to z rady na razie.  
LP jest.  
Aha no pytanie aniu, czy to miałeś przestrzeń żeby sprawdzić, bo.  
To na ostatniej Radzie sobie umawialiśmy.

**Anna Skupinska** 52:04  
Nie, nie znam się tym, myślę, że chciałam się tym dzisiaj zająć.

**Damian Kaminski** 52:10  
No dobra, to gdzieś sobie zanotuj to na następnej Radzie się do tego odwołamy.

**Anna Skupinska** 52:12  
Mhm, jasne, to jest to indesign troszeczkę wynika, że zacznie zaznacza wszystkiego tak to muszę zobaczyć.

**Damian Kaminski** 52:19  
Znaczy tu jest pierwsze zdanie, tak to trzeba zrobić.  
Nic nie produkujemy, chodzi o to, żeby sprawdzić właśnie, kiedy to zaznacz wszystko.

**Anna Skupinska** 52:27  
Prawda?

**Damian Kaminski** 52:28  
Kiedy lista pod zaznacz wszystko na podstawie czego jest generowana tak Janusz pokazywał ten przykład.

**Anna Skupinska** 52:34  
Mhm.

**Damian Kaminski** 52:36  
Gdzie były 2?  
A na raporcie były 3 wyświetlały się 2.  
Strzech.

**Janusz Bossak** 52:43  
No to jest jeden z wielu tak tych setek błędów, o których mówię, że są dolara sportowym, no po prostu.

**Damian Kaminski** 52:55  
Dobra.  
Dost tematów, które są przypisane do klientów, mamy wszystko zaopiekowane. Tak polpharma czeka na Tomasza. Tutaj czekamy na informa.  
Dodani wam wreszcie na razie.  
Nic nie odpowiadamy, tak trzeba do tego tematu wrócić, no po kolei dalej to mogę jechać jeszcze z.  
Się chcemy jeszcze jakąś jedną rzecz, to po kolei po prostu.  
A to jest rymów ft.

**Piotr Buczkowski** 53:23  
Znaczy ja ja tylko jedną. Ja to jedną uwagę, bo której?  
I nie ma wpisu, tak?  
To porozmawiać z Łukaszem pod kropką?  
Czopach wykonywanych przez wielu czopach wykonywanych przez tą serwis.  
Jest takie coś rząd, sprawdź, że jobs sprawdza, czy serwis się nie zatrzymuje i wtedy jeżeli się nie zatrzymuje, to przerywa działanie.  
Tak, żeby nic nie nic nie popsuć.  
Tylko ja to zrobiłem dla grobów, które istniały, powiedzmy tam 2 3 lata temu, no tą tej pory przyszło wiele nowych dziobów typu do jaj do nadawcy takie nadawcy do czegoś.  
Trzeba przejrzeć wszystkie te żaby czy prawidłowo się potrafią przerwać działanie?  
Nie wiem jak to Zgłoś.

**Damian Kaminski** 54:15  
Chociaż zapętlenia tak.

**Piotr Buczkowski** 54:17  
Nie chodzi o zatrzymanie usługi, jeżeli jak zatrzymamy, zatrzymam usługi, usługę żeby.  
Żeby czop potrafił się zatrzymać tak, żeby był świadomy tego, że usługa się zatrzymuje.

**Damian Kaminski** 54:31  
Mhm.

**Piotr Buczkowski** 54:32  
Że jeżeli ma powiedzmy, ma do wykonania 100 zadań, jest po 3 czy po 5 6 tak to nie robi następnego, tylko powiedzmy.

**Damian Kaminski** 54:38  
To nie kontynuował.  
Kończy to obecne.

**Piotr Buczkowski** 54:43  
Dokończy to co robi, nie, nie zaczął następnego, tylko się przerywa tak, ale bezpiecznie.

**Damian Kaminski** 54:50  
Mhm.

**Piotr Buczkowski** 54:50  
Żeby na przykład go kill procesu nie zatrzymał, nie zatrzymał jakaś zadania w środku, to co może powodować?  
No co może powodować?

**Damian Kaminski** 55:01  
Ubytek danych.

**Piotr Buczkowski** 55:03  
No jakieś tam niespójność danych.

**Damian Kaminski** 55:06  
No to ważne.  
Zrobisz do tego zgłoszenie?

**Piotr Buczkowski** 55:11  
Właśnie nie wiem jak zrobić czy to wszystkich czołgów myli czy jeden i.

**Damian Kaminski** 55:15  
Zrobić twitter dla ogólnego, a potem przejrzeć wszystkie joby.  
I pb i je po prostu pod spodem i będziemy przydzielać po kolei.

**Piotr Buczkowski** 55:28  
Dlaczego to będzie ważne, bo będzie to mechanizm ograniczenia wydajności z serwerów.  
No może a s czyli tych serwisowych na czas.  
Będąc tak, żeby ograć oszczędzić pieniądze, to wymaga zatrzymania restartu serwera.  
Czyli zatrzymanie usługi.  
Warto by było tak, żeby ta usługa się bezpiecznie zatrzymała.  
2 razy dziennie.

**Damian Kaminski** 56:14  
Dobra, to tak to nazywam.  
Przypiszę to Piotr do ciebie.

**Piotr Buczkowski** 56:21  
Ja muszę przejrzeć ten początek tak jak słaby, zarejestrowane.

**Damian Kaminski** 56:27  
Tak i wypisz po prostu tutaj przynajmniej jakie joby, a potem z tego zrobimy w jamie.

**Piotr Buczkowski** 56:29  
Tak tak, dla której dziobów trzeba prześledzić czy to, czy to ma sens tak, czy.  
Bo to było na przykład dla lot mes dla lodzka.  
Jakie trust tak.  
Przeczytam.  
No właśnie pewnie dla tych sadul nie, bo to trudno to zrobić, dobrze.  
Proces robic potężny.

**Damian Kaminski** 57:09  
No dobra, ja niestety się za 3 minuty muszę przełączać, więc chyba na tym zakończymy.  
Czy mam tu wrzucić radę?  
Nie przepadnie to z Twojej tablicy, w sensie nie zagubi się w Twojej tablicy.

**Piotr Buczkowski** 57:32  
Nie wiem.

**Damian Kaminski** 57:35  
Dobra, to na razie prewencyjnie wrzucę.  
Żebyśmy gdzieś temu to odczytywali co jakiś czas dobra, Piotr, ja tylko przypominam o tym o tych wytycznych do repozytorium, żeby je opisać.

**Piotr Buczkowski** 57:48  
Po spotkaniu się zajmuje.

**Damian Kaminski** 57:49  
Z mojej strony wszystko.  
No dobra, to w takim razie dzięki za dzisiaj.

**Lukasz Bott** 57:58  
Dzięki.

**Damian Kaminski** 57:59  
Cześć.

**Janusz Bossak** zatrzymano transkrypcję
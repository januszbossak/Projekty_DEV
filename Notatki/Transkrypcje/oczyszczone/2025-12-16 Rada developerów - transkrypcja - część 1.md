**Data spotkania:** 16 grudnia 2025, 09:01

---

**Anna Skupińska:** Szt.

**Damian Kamiński:** Cześć. Aniu, czy ty? Potrzebujemy poruszyć tej kwestii związanej z uprawnieniami do podglądów, o których poruszałaś na przykład.

**Anna Skupińska:** A czy ogólnie rzecz biorąc to?

**Damian Kamiński:** Czy już się wyjaśnił?

**Anna Skupińska:** Halo, czy mnie słychać?

**Damian Kamiński:** Tak, tak, tak, mów.

**Anna Skupińska:** Tak, bo ogólnie rzecz biorąc do pobierania plików i wysiadania podglądów używamy tych starych endpointów i on oczywiście nie sprawdzają prawie nie repozytorium, więc można było zrobić, żeby dodać w nich kod, który sprawdza, że jeżeli plik jest w repozytorium, to że sprawdza uprawnienia repozytorium też od niego.

**Damian Kamiński:** No dobra, czyli tu wszystko jest, no.

**Piotr Buczkowski:** Stop, stop, stop, stop, stop, ale. Oczywiste. Znaczy, mamy, używamy i on powinien wiedzieć, jak sprawdzi się uprawnienia.

**Anna Skupińska:** Tak. Ee, tak, a on sprawdzał swoje uprawnienia, a nie te nasze repozytorium uprawnienia.

**Piotr Buczkowski:** Ale uprawnienia prezydium co teraz jego uprawnieniami. To ma być spójne, tak robisz, bo.

**Anna Skupińska:** No i czy Adrian robił te uprawnienia, więc nie jestem pewna, czy on dodawał to w uprawnieniach dla case attachment?

**Piotr Buczkowski:** Tworząc obiekt albo podnosi wykryć dobrze, może wtrącamy się w środku dyskusji, bo nie wie.

**Damian Kamiński:** Poczekaj, Piotr, to. Nie, nie bardzo dobrze, to specjalnie, to znaczy ja na początku tylko zapytałem Ani, czy musimy to omówić, bo wiem, że to padło. Powiedziałbym, że na testy biznesowe nie jest to krytyczne, bo to dotyczy właśnie próby jakiegoś przechwycenia. Nie jest to takie proste z perspektywy takiego użytkownika biznesowego typu, tak jak i kierowanie po sprawach, że można sobie zmieniać case ID w adresie i w zasadzie. Strzelać tutaj nie jest to takie proste, nie podajemy tego adresu jawnie, niemniej tak trzeba to zaopiekować. Już tylko chodzi mi o to, że chcę dzwonić Adriana. Ee, jeszcze raz po prostu do tego tematu wrócimy od początku, tak, czyli tutaj cześć, Adrian.

**Adrian Kotowski:** Cześć.

**Damian Kamiński:** Chcemy porozmawiać o uprawnieniach do plików i do samych podglądów repozytorium w kontekście. Użytkowników pod kątem właśnie jakieś pen testów potencjalnych, czyli nie takiego prostego, że ktoś nie widzi, ale czy? No właśnie w ramach pen testów można w jakiś sposób, nie wiem. Postmanem, zewnętrzną aplikacją. Zapytaniami wykraść te, dostać się po prostu czy do podglądu, czy do plików. To tu Piotr, jakbyś mógł jeszcze raz powtórzyć to co proponujesz? I Adam się ustosunkuje? Czy tak to działa?

**Piotr Buczkowski:** Kreator case attachment powinien sprawdzać czy to jest załącznik, czy to jest dokument do sprawy i wtedy działa tak jak teraz, czy to jest zaocznie repozytorium? Wtedy sprawdza uprawnienia repozytorium albo praca dul. Album tru sata zachęt.

**Adrian Kotowski:** OK, dobra, to jest najprostsze rozwiązanie tej teraz. Tak patrzę, to faktycznie ten obszar obsługi plików był taki trochę pominięty, a nie rozumiem po prostu, że teraz jak mamy ten mechanizm.

**Piotr Buczkowski:** No trzeba to, to, to, to do tej pory nie mieliśmy repozytorium. To nie było takie straszne sprawdzanie uprawnienia z repozytorium.

**Adrian Kotowski:** Tak, tak wiem. Znaczy chodzi mi teraz, że w momencie developmentu jakby ochrona tych, znaczy dostęp do uprawnień, jakby nie.

**Damian Kamiński:** No tak.

**Piotr Buczkowski:** Chciał, chciałbym, chciałbym, żeby to było spójne, tak, że tworzysz i tam odkryć apartment. Jeżeli masz podany, jeżeli masz uprawnienia, wszystko się dzieje ładnie, jeżeli nie masz uprawnień, że się null. Tak samo jak teraz stworzysz do. To. Podpięty do sprawy sprawdza, czy to sprawy masz dostęp, jeżeli nie masz, to sprawdza się dużo, czytam, zwraca pusta, to czym zresztą pamiętam.

**Adrian Kotowski:** Dzień dobry, okej, ale to jeszcze jestem przed kontrolerzy, bo to musimy, że jak będziemy to obsługiwać na nisko poziomie. Przykład na poziomie załóżmy tam pobierania danych z.

**Piotr Buczkowski:** Yy. Dostajesz, tak?

**Adrian Kotowski:** Tak, no okej, no.

**Piotr Buczkowski:** Tworzysz obiekt.

**Adrian Kotowski:** Tak, no jak zwróci.

**Piotr Buczkowski:** W kreatorze kraje tam odkryć attachment sprawdzasz czy sprawdzane jest, czy masz uprawnienia, albo jeżeli to jest do sprawy, to sprawdzasz na sprawie, czy może do sprawy, jeżeli to jest profesorem, sprawdza, czy to może do repozytorium dostęp i zwracasz albo obiekt wypełniony, albo null.

**Adrian Kotowski:** Znaczy ja rozumiem tylko.

**Piotr Buczkowski:** Tak jak teraz.

**Adrian Kotowski:** Pytanie takie, bo to już nie mogą być dziewczyny, że albo po prostu obiektu nie ma, albo nie miałem uprawnień i jak normalnie w kontrolerze czy powinniśmy sprawdzić?

**Piotr Buczkowski:** No to na motce jest takie coś, że jest pedałem wklei tam od case out reason. Czy gottwald, czy premier, czy jakoś tak.

**Adrian Kotowski:** Ale to jest kolei ciekawe, bo też widziałem w niektórych miejscach na temat liście.

**Piotr Buczkowski:** I zwraca odpowiedni komunikat błędu, wtedy, tak, z kontrolera albo 404 albo.

**Adrian Kotowski:** Ja myślę, że to jest bezsens tyle, nie, po prostu dawać lepiej zabrać zawsze forbidden, bo na przykład teraz widziałem, to jest tak metrycznych, bo coś takiego, że na mnie niektórzy, niektórzy ci autorzy zarzucili, że na przykład zwracamy, czy to się na przykład, że można pozyskać informacji o osobach, które się nie pobierze zasobu. Ale przykład możesz sobie numerować, więc zawsze lepiej chyba zwrócić forbidden według mnie, bo nie wiadomo, czy nie ma to, nie ma zasobu, czy jest zabroniony.

**Piotr Buczkowski:** Fortnite jest 400. Czy tak? Róż. Różnica pomiędzy 404, 403 według mnie nie ma znaczenia, znaczy. Może jasna, nie masz dostępu, to, to, no nie masz dostępów.

**Adrian Kotowski:** Tak, ale właśnie chodzi o to, żeby zmienić jednak innego napastnika, że jednak nie wiesz, czy da się po prostu nie masz do niego uprawnień. Więc wracaj mnie, no, no, no, no, no trwa jakby jest trochę bez sensu. Myślę, że dzisiaj tak, no Łukasz się tego przyczepi, czy będzie to?

**Piotr Buczkowski:** Jabol. Nie, to do, tak, do tego się nie przyczepiają. Przyczepiają się do tego, że mogłaś sobie trenować i poprać jakieś dane, a nie to, że ci zwracają forbidden czy czy not found.

**Adrian Kotowski:** Nie, no zdarzało się, że parę było takich 15, gdzie po prostu były ten problem, że macie.

**Piotr Buczkowski:** Nie, nie było, nie, nie, nie pamiętam takiego.

**Damian Kamiński:** Ale mówisz o Adrian, no faktycznie zdarzenia chyba AMODIT czy gdzieś tam przeczytanych?

**Adrian Kotowski:** Tak, że mieliśmy w którejś z tych też. Testów tam było tak właśnie, że bądźcie nie tego, że mieliśmy te, że mamy numery tych obiektów właśnie takie numeryczne. Czy takie całkowite liczbowe, że łatwo jest po prostu iść do góry? O jeden to jest przeglądać zasoby, bo nie mamy bolidów.

**Damian Kamiński:** Mhm.

**Piotr Buczkowski:** Nie pamiętam, Adrian, takiego pen testu nie było. Zwrócono uwagę, że simy zwracamy 404 zamiast 403.

**Adrian Kotowski:** No to ty mogę posiłkować znaleźć, były takie na pewno.

**Piotr Buczkowski:** Czy odwrotnie? Jak najbardziej były takie to coś, że po prostu nie sprawdzaliśmy dokładnie uprawnień, na przykład zwracaliśmy dane użytkownika o danym. Który użytkownik, który od powiedzmy atakujący sobie wpisał z palca? W jakimś tam narzędziu?

**Adrian Kotowski:** No teraz właśnie poruszyłem ten temat, potem widziałem, że ani w jednym temat pojęcie dodawać właśnie to zabezpieczenie, żeby zwracać się internal server error. Właśnie teraz informacji o tym, że to się nie trwam.

**Damian Kamiński:** Dobra. No.

**Piotr Buczkowski:** Znaczy nie. Też proszę 404 statki, tak, czy 403, 404 nie internet, to jest internet.

**Adrian Kotowski:** Tak właśnie to też.

**Piotr Buczkowski:** To i to jest to też inaczej traktowane chociażby przez gateway, tak?

**Anna Skupińska:** No ale to nie będzie tutaj, to po prostu chciałam, żeby tą informację zataić, że tego, tego pliku nie ma na przykład.

**Piotr Buczkowski:** Czy ta?

**Damian Kamiński:** No dobrze, czyli zalecenie Piotra jest takie, że. Nie jest problemem, że pokazujemy, że on jest po prostu access i tyle.

**Piotr Buczkowski:** No tak.

**Adrian Kotowski:** No dobra, OK, no to to.

**Piotr Buczkowski:** Czy to czytam fortnite, fortnite 400?

**Damian Kamiński:** Czy forbidden? Dobra, to tak ustalamy.

**Adrian Kotowski:** No to jak miałaś dobrze, to jest to co mógłbyś, to jest dosłownie mnie tam chwilę, to mogę dodać jeszcze tyle dać.

**Damian Kamiński:** Tak, to jest chwila. To jest chwila w kontekście i załączników i podglądów, tak.

**Piotr Buczkowski:** No tak, tak.

**Damian Kamiński:** No dobra, bo to znaczy był. Właśnie chciałem powiedzieć, że jeśli to jest duże wyzwanie, to nie chciałbym tego teraz upychać. Bo to nie wpłynie na testy takie typowo biznesowe, ale jeśli to jest chwila, no to róbmy to od razu.

**Adrian Kotowski:** No znaczy, no lepiej by to.

**Piotr Buczkowski:** No i tak i tak macie informacje, co się stało, tak, czy.

**Damian Kamiński:** OK, no jeśli to myślałem, że to jest coś, coś grubszego.

**Adrian Kotowski:** Czy to jest?

**Piotr Buczkowski:** Mówię nam odkryć jest zwracany ten aut, tak, czy jakość.

**Damian Kamiński:** Dobrze, to ty, to Adrian zaopiekujesz? Tak?

**Adrian Kotowski:** Tak, no właśnie teraz naprawdę.

**Damian Kamiński:** A ten kontekst Ani gdzie, a nieco innego zwracała, to Ania ma to poprawić, czy ty to będziesz?

**Adrian Kotowski:** Też to poprawię, bo tam mam dużą zmianę, też bez sensu, żeby to 2 osoby tam teraz zmodyfikowały to tam też chwilami wzajemnie.

**Damian Kamiński:** No to właśnie żeby się dogadać. Dobra, czyli ty to, ty to zaopiekujesz.

**Piotr Buczkowski:** Znaczy.

**Adrian Kotowski:** Tak, no.

**Piotr Buczkowski:** Nie zwracajcie braku dostępu jako pięćsetka, więc to jest pięćsetka.

**Damian Kamiński:** No i weźmy taką uwagę w kontekście globalnym, a nie tylko repozytorium, tak, żebyśmy nie wracali do tych dyskusji.

**Adrian Kotowski:** No tak, znaczy to właśnie te właśnie w tym miejscu niepokoiło, bo to jest nie obsłużony błąd jakby, a tam myślałem tylko obsłużone zwracać.

**Damian Kamiński:** Mhm. No dobra.

**Piotr Buczkowski:** Jedyny błąd, którego nie powinniśmy zwracać, to jest autora. Jest tak. 401, bo wtedy ci blogu.

**Damian Kamiński:** Czy coś jeszcze w tym kontekście chcecie poruszyć albo w ogóle w repozytorium chcecie o coś Piotra dopytać? Czy wszystko jest poza tym na razie jasne?

**Adrian Kotowski:** No na razie wszystko jest jakoś ten. Tak to jeden tak.

**Damian Kamiński:** Dobra.

**Anna Skupińska:** A takie właśnie jedna rzecz co do zapisywania, bo teraz używam po prostu case attachment, jak one zapisują pliki, to one używają sobie własnego systemu, zapisywania plików, nie zmieniają chyba tam nic za bardzo, gdzie one się zapisują i słyszałam, że.

**Piotr Buczkowski:** Znaczy właśnie, właśnie z, no tak, tak przecież proponowałem jaką ma być, jak ma wyglądać ścieżka.

**Anna Skupińska:** Potrzebowałam, żeby zmienić, to chodzi o to, tak, OK, to będę się tam pogrzebać i zmienić folder, w którym to się zapisuje.

**Piotr Buczkowski:** To koniecznie.

**Anna Skupińska:** Mhm.

**Damian Kamiński:** W sensie zapisywanie fizyczne pliku.

**Anna Skupińska:** Tak.

**Piotr Buczkowski:** Tak, jeżeli mam zapisywanie pliku na dysku, a nie w barze.

**Damian Kamiński:** Tak, to było omówione, tak jak, tak jak te.

**Anna Skupińska:** Tak, tak, to jeszcze trzeba zrobić, to jeszcze zrobię.

**Damian Kamiński:** OK. Dobra. Ale tu wszystko jest jasne, tak, tylko trzeba po prostu to poprawić, ale wiadomo jak i co trzeba zrobić.

**Adrian Kotowski:** Się jest na tym, bo myślałem trochę o tym, o tych uprawnieniach i reszta też przydałby się może mechanizmy na przykład historii prawnie, bo teraz mamy historię zmian w folderze, a adoro w sumie czy to a k.

**Damian Kamiński:** No dobra.

**Anna Skupińska:** Jest, robię zapisywanie w historii, że jak zmienić uprawnienia folderu, to się zapisuje do historii.

**Adrian Kotowski:** A dobra faktycznie, bo nawet ci kiedyś mówiłem tutaj, dobra, OK, tak, tak, tak, znaczy to, to jest bardziej ogólnie się jakby historia folderu, nie historię uprawni folderu, dobra racja, tylko i to, to, to, to, to też mieliśmy dzięki też nawierzchnie, dobra to.

**Damian Kamiński:** A po staniu jest już jakiś raport?

**Anna Skupińska:** Jeszcze takie pytanie co do zapisywania historii, bo zauważyłam, że jeżeli jest folder i znaczy nie wiem, jest sprawa i ktoś pobiera z tej sprawy dokument, to jest to zapisywane w historii sprawy. Pytanie, czy powinniśmy też za to zapisywać w repo historie pozorem, jak ktoś pobierze plik?

**Damian Kamiński:** Dobrze by było.

**Anna Skupińska:** Czy nie?

**Damian Kamiński:** Dobrze było.

**Anna Skupińska:** OK.

**Adrian Kotowski:** Że to nie, to masz ten.

**Damian Kamiński:** Chociaż poczekajcie, poczekajcie, bo na sprawie my to mamy jako dodatkowe logi, bo to może być dużo częstsze. Dużo częstsze działanie niż samo wgrywanie czy usuwanie i na sprawach mamy po prostu na procesach mamy dodatkowy checkbox podglądu i pobierania. Znaczy, wydaje mi się, że chyba podgląd nie ma sensu, no bo jak ktoś ma uprawnienia, to wiesz, no nie wiem, zawsze może się znaleźć klient, który powie, że chce widzieć kto przegląda, bo mógł się pomylić i mógł nastąpić. Nadanie uprawnień niezgodnie z polityką.

**Adrian Kotowski:** Czy takie pytanie, kto to powinien mieć dostęp do do historii folderu teraz?

**Damian Kamiński:** Jeszcze tego nie definiowaliśmy, na razie stwierdziliśmy, że ma się zapisywać w ogóle, jeszcze historia nie jest wycie. Pociągnięta do interfejsu i.

**Anna Skupińska:** Wskazuje, że administratorzy pewno.

**Damian Kamiński:** Na razie ustaliliśmy, że może być to po prostu jako MSP jako raport dodatkowy. Nie wiem, ja to znaczy, może inaczej, nie, nie wiem. Jedyny pomysł, jaki na to mam sensowny, to jest tak jak historia, mail i historia aktywności, czyli po prostu po stronie tutaj. Ja bym to raczej dokładał tutaj. O. Akurat coś robicie. Czy się dobra? No pytanie, czy macie na to lepszy pomysł? Bo mój, mój najlepszy jak dotąd jest taki, żeby tutaj dołożyć. Historię repozytorium.

**Anna Skupińska:** No można było po prostu coś kolejną zakładkę.

**Damian Kamiński:** Piotr, nie masz obiekcji co do tego?

**Piotr Buczkowski:** Jeszcze, jeszcze raz, żeby trochę śmiechu skruszył.

**Damian Kamiński:** Żeby w ramach logów dołożyć kolejną zakładkę pod historię repozytorium. Mamy tutaj tą aktywność administracyjną i tak samo. I tak samo to, to, to znaczy.

**Łukasz Bott:** Ale tu czekaj, ale historia, bo to represent, to czekajcie.

**Anna Skupińska:** Ryszard robi cię słońce od pobierania tej historii.

**Łukasz Bott:** A ta historia repozytorium to nie, nie, nie, nie ten nie zawiera się w aktywności administracyjnej.

**Anna Skupińska:** Ja.

**Damian Kamiński:** Nie, nie, nie.

**Anna Skupińska:** A jest w oddzielnym miejscu zapisywano.

**Łukasz Bott:** Ukryli, dobra, no ale.

**Piotr Buczkowski:** Tutaj jest już bardzo dużo o tych.

**Damian Kamiński:** Nie, no, historia administracyjnej przecież nie masz, że ktoś nadał uprawnienia do konkretnej.

**Piotr Buczkowski:** Znaczy, ja bym tutaj rozdzieli na przykład loginy, login, loga odbył tego, tak dużo, że trudno cokolwiek już z innego znaleźć.

**Łukasz Bott:** No, no to na to ta.

**Damian Kamiński:** Że tu nie powinno tego być, nie.

**Piotr Buczkowski:** Znaczy ja bym to właśnie wydzielił do.

**Damian Kamiński:** Też, też się zgadzam. Wyrzucić to.

**Piotr Buczkowski:** Do innej zakładki.

**Damian Kamiński:** No dobra, no ale to już jest postulat odrębny, ale masz rację, to nie ma sensu, żeby tutaj w historii typowo administracyjny był.

**Piotr Buczkowski:** Wczoraj właśnie wczoraj czy to coś szukałem, czytam, czytam zeszłym tygodniu i przekopać się logout to.

**Łukasz Bott:** A to. Ale słuchaj, ja po prostu tutaj nie dodać kolejnego przycisku filtru, po prostu filtr po typie aktywności.

**Damian Kamiński:** Co najmniej filtr.

**Piotr Buczkowski:** No to są całkiem, całkiem. To nie jest login, nokaut nie jest administracji, aktywność administracyjna, to jest aktywność zwykła.

**Łukasz Bott:** Nie, nie, no, no, OK, dobra? Wiesz co, ale to, to się wiąże jeszcze z innym tematem, no bo tutaj też i klienci właśnie. Ja nawet raport pod raporty systemowy taki właśnie zrobiłem, bazując na tym login, log out, tak, czy ten właśnie data ostatniego logowania, jakieś tam ileś logowań, tak, do systemu, tak, danego użytkownika? No to to akurat w module raportów nie zrobiłem, tak. No ale faktycznie może.

**Damian Kamiński:** No to trzeba docelowo pewnie wyciągnąć tutaj, tak, na użytkownikach.

**Łukasz Bott:** No tak, tak, no użytkownika, wiesz, wczoraj z Danielem gdzieś tam rozmawiałem był, bo byliśmy o firmie, tak. No to też się a propos tych raportów systemowych przypomniał na przykład tutaj informacja jakaś taka właśnie gdzieś to statystykach użytkowników, do tego ich typów niej typów i tym podobnych rzeczy, nie. Czy to wewnętrzny, zewnętrzny, czy administrator, zastaw koksu, czy nie i tym podobne, nie.

**Damian Kamiński:** Tu jest zresztą data ostatniego, tak. Dobra. Kończąc tutaj ten wątek, Ania, uważam, że skoro tu logujemy nawet logowania, to tak, pobranie, tak, na razie podglądu nie. Ee, czyli odpowiadając na twoje pytanie, pobranie mogę zrobić na to zgłoszenie? Pobranie zapisujemy do historii.

**Anna Skupińska:** Tak, zgaduję, że ona musi być z waginą, bo tutaj mamy wyświetlanie rzeczy z nacją. Agencja to oznacza to, że musisz podać.

**Damian Kamiński:** Nie, nie, poczekaj na, ja wiem co to znaczy. Natomiast na razie nie mówimy o tym, że to wrzucamy tu. Na razie mówimy o tym, że zapisujemy do logów. Czy ktoś pobrał dokument?

**Anna Skupińska:** A OK.

**Damian Kamiński:** Ee, a odrębnie na to trzeba będzie pewnie przygotować. To znaczy chciałbym też to podzielić, tak, bo słuchajcie, no osoby odpowiedzialne są odpowiedzialne za React, mają. Albo inaczej, wy jesteście na obciążeni. W kontekście ich, tak, zawsze się nie wyrobimy, ze nie wyrabiamy ze zgłoszeniami dla nich, bo dużo szybciej po prostu obsługują to, co muszą zrobić, więc raczej tym elementem, nie pamiętam. Chyba to Filip rogu wizualnym zajmie się Filip, a będzie potrzebował do tego, tak jak mówisz, pewnie jakiegoś backendu. I ten weekend trzeba będzie przygotować. Natomiast nie powiedziałbym, że to jest coś, z czym to jest ostatnia rzecz, którą będziemy się zajmować, o tak. Bo to już nie wpływa na funkcjonalność samą w sobie, tylko to jest po prostu. Audit log i tyle.

**Łukasz Bott:** A jeżeli teraz to jest jakoś tam rejestrowany, czy już możemy to rejestrować i niech tam sobie siedzi w jakiejś tabelce.

**Damian Kamiński:** To już wstecz będziemy mieli dane. Dokładnie.

**Łukasz Bott:** Niech sobie tam siedzi w bazie danych.

**Damian Kamiński:** Ale spoko, no nie wiem, jeśli ty byś się chciał o tym zająć, no to ja mogę zobaczyć, czy Filip tam ma jakieś inne zgłoszenia, bo jeśli masz ochotę, żeby to samemu zrobić, to to też może nie mam nic przeciwko, po prostu często jest tak, że tych rzeczy backendowych jest dużo, a frontendowych ledwo się tutaj z kolegami wyrabiamy, żeby to po projektować, bo to zaprojektujemy, projektowanie trwa tyle co wykonanie, czasami, więc. Na ananas jest powiedzmy. Nie robimy tylko tego, a Filip z tutaj Przemkiem robią tylko to, więc no często jest tak, że się po prostu nie wyrabiamy już mówiąc wprost. Że coś dziś przygotowujemy, a już jutro jest to zrobione, dobra, mniejsza o to, na razie konkluzja jest taka, zapisujemy, a jeszcze żeby to wyświetlać, to to do tego dojdziemy. Na razie jeśli to zapisujemy, to nawet na potrzeby testów, to to, co ci napisałem w tym zgłoszeniu, wystarczy, że podepniesz tutaj tylko pod źródła dane i wrzucisz tam do testów, że jest raport o nazwie takiej i takiej, i to się raportuje, dziewczyny już mogą to sprawdzać, a to, że tu wyświetlimy później, to już będzie tylko zakres.

**Anna Skupińska:** A czy jest, to zrobiłam tylko nie robiłam raportu, tylko zrobią po prostu fillm źródło danych, więc mogą wejść źródła danych i zobaczyć.

**Damian Kamiński:** No to trzeba z tego źródła zrobić. Według mnie raport, żeby można było to odfiltrować łatwo. To będzie wygodniejsze. No jednak źródło danych jest ograniczony, dobra, ale nie chciałbym teraz całej rady. Tu już na ten temat poświęci, bo on jest raczej dość prosty, więc jak to zrobisz, to puścimy to dziewczynom.

**Anna Skupińska:** No OK.

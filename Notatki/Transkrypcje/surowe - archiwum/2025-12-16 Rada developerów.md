**Transkrypcja**

16 grudnia 2025, 09:01AM

**Anna Skupinska** 0:10  
Szt.

**Damian Kaminski** 0:12  
Cześć.  
Aniu czy ty?  
Potrzebujemy poruszyć tej kwestii związanej z uprawnieniami do podglądów, o których poruszałaś na przykład.

**Anna Skupinska** 0:23  
A czy ogólnie rzecz biorąc to?

**Damian Kaminski** 0:25  
Czy już się wyjaśnił?

**Anna Skupinska** 0:28  
Halo, czy mnie słychać?

**Damian Kaminski** 0:29  
Tak, tak, tak mów.

**Anna Skupinska** 0:29  
Tak, bo ogólnie rzecz biorąc do pobierania plików i wysiadania podglądów używamy tych starych and pointów i on oczywiście nie sprawdzają prawie nie repozytorium, więc można było zrobić, żeby dodać w nich kod, który sprawdza, że jeżeli plik jest w repozytorium, to że sprawdza uprawnienia repozytorium też od niego.

**Damian Kaminski** 0:50  
No dobra, czyli tu wszystko jest, no.

**Piotr Buczkowski** 0:52  
Stop stop stop stop stop ale.  
Oczywiste.  
Znaczy, mamy, używamy i on powinien wiedzieć, jak sprawdzi się uprawnienia.

**Anna Skupinska** 0:59  
Tak.  
Ee tak, a on sprawdzał swoje uprawnienia a nie te nasze repozytorium uprawnienia.

**Piotr Buczkowski** 1:06  
Ale uprawnienia prezydium co teraz jego uprawnieniami.  
To ma być spójne, tak robisz, bo.

**Anna Skupinska** 1:12  
No i czy Adrian robił te uprawnienia, więc nie Jestem pewna, czy on dodawał to w uprawnieniach dla kasy attachment?

**Piotr Buczkowski** 1:21  
Tworząc obiekt albo podnosi wykryć dobrze, może wtrącamy się w środku dyskusji, bo nie wie.

**Damian Kaminski** 1:23  
Poczekaj Piotr to.  
Nie, nie bardzo dobrze to specjalnie to znaczy ja na początku tylko zapytałem ani czy musimy to omówić, bo wiem, że to padło. Powiedziałbym, że na testy biznesowe nie jest to krytyczne, bo to dotyczy właśnie próby jakiegoś przechwycenia. Nie jest to takie proste z perspektywy takiego użytkownika biznesowego typu, tak jak i kierowanie po sprawach, że można sobie zmieniać klase i DW adresie i i w zasadzie.  
Strzelać tutaj nie jest to takie proste, nie podajemy tego adresu jawnie, niemniej tak trzeba to zaopiekować. Już tylko chodzi mi o to, że chcę dzwonić Adriana.  
Ee Jeszcze raz po prostu do tego tematu wrócimy od początku tak, czyli tutaj cześć Adrian.

**Adrian Kotowski** 2:08  
Cześć.

**Damian Kaminski** 2:09  
Chcemy porozmawiać o uprawnieniach do plików i do samych podglądów repozytorium w kontekście.  
Użytkowników pod kątem właśnie jakieś pen testów potencjalnych, czyli nie takiego prostego, że ktoś nie widzi, ale czy? No właśnie w ramach pen testów można w jakiś sposób nie wiem. Post mannym zewnętrzną aplikacją.  
Zapytaniami wykraść te dostać się po prostu czy do podglądu czy do plików. To tu Piotr, jakbyś mógł Jeszcze raz powtórzyć to co proponujesz? i Adam się ustosunkuje? Czy tak to działa?

**Piotr Buczkowski** 2:43  
Kreator kejsa tashkent powinien sprawdzać czy to jest załącznik, czy to jest dokument do sprawy i wtedy działa tak jak teraz, czy to jest zaocznie repozytorium? Wtedy sprawdza uprawnienia prowizorium albo praca dul.  
Album tru sata zachęt.

**Adrian Kotowski** 3:02  
Ok, dobra, to jest najprostsze rozwiązanie tej teraz tak patrzę to faktycznie ten obszar obsługi plików był taki trochę pominięty, a nie rozumiem po prostu, że teraz jak mamy ten mechanizm.

**Piotr Buczkowski** 3:12  
No trzeba to to, to to do tej pory nie mieliśmy repozytorium. To nie było takie straszne sprawdzanie uprawnienia z repozytorium.

**Adrian Kotowski** 3:16  
Tak tak wiem. Znaczy chodzi mi teraz, że że w momencie developmentu jakby ochrona tych znaczy dostęp do uprawnień, jakby nie.

**Damian Kaminski** 3:16  
No tak.

**Piotr Buczkowski** 3:22  
Chciał, chciałbym, chciałbym, żeby to było spójne, tak, że tworzysz i tam odkryć apartment. Jeżeli masz podany, jeżeli masz uprawnienia, wszystko się dzieje ładnie, jeżeli nie masz uprawnień, że się nul.  
Tak samo jak teraz stworzysz do.  
To.  
Podpięty do sprawy sprawdza czy to sprawy masz dostęp, jeżeli nie masz to sprawdza się dużo czytam, zwraca pusta to czym zresztą pamiętam.

**Adrian Kotowski** 3:47  
Dzień dobry, okej, ale to jeszcze Jestem przed kontrolerzy, bo to musimy, że jak będziemy to obsługiwać na nisko poziomie. Przykład na poziomie załóżmy tam pobierania danych z.

**Piotr Buczkowski** 3:56  
Yy.  
Dostajesz tak?

**Adrian Kotowski** 4:00  
Tak no okej, no.

**Piotr Buczkowski** 4:01  
Tworzysz obiekt.

**Adrian Kotowski** 4:04  
Tak no jak zwróci.

**Piotr Buczkowski** 4:04  
W kreatorze kraje tam odkryć attachment sprawdzasz czy sprawdzane jest, czy masz uprawnienia, albo jeżeli to jest do sprawy, to sprawdzasz na sprawie, czy może do sprawy, jeżeli to jest profesorem, sprawdza, czy to może do repozytorium dostęp i zwracasz albo obiekt wypełniony albo dul.

**Adrian Kotowski** 4:22  
Znaczy ja rozumiem tylko.

**Piotr Buczkowski** 4:22  
Tak jak teraz.

**Adrian Kotowski** 4:24  
Pytanie takie, bo to już nie mogą być dziewczyny, że albo po prostu obiektu nie ma albo nie miałem uprawnień i jak normalnie w kontrolerze czy powinniśmy sprawdzić?

**Piotr Buczkowski** 4:30  
No to na motce jest takie coś, że jest pedałem wklei tam od case out reason.  
Czy gottwald, czy premier czy jakoś tak.

**Adrian Kotowski** 4:43  
Ale to jest kolei ciekawe, bo też widziałem w niektórych miejscach na temat liście.

**Piotr Buczkowski** 4:46  
I zwraca odpowiedni komunikat błędu, wtedy tak z kontrolera albo 404 albo.

**Adrian Kotowski** 4:53  
Ja myślę, że to jest bezsens tyle nie po prostu dawać lepiej zabrać zawsze forbidden, bo na przykład teraz widziałem to jest tak metrycznych, bo coś takiego, że na mnie niektórzy niektórzy ci autorzy zarzucili, że na przykład zwracamy, czy to się na przykład, że można pozyskać informacji o osobach, które się nie pobierze zasobu. Ale przykład możesz sobie numerować, więc zawsze lepiej chyba zwrócić forbidden według mnie, bo nie wiadomo czy nie ma to nie ma zasobu, czy jest zabroniony.

**Piotr Buczkowski** 4:54  
Fortnite jest 400. Czy tak?  
Róż. Różnica pomiędzy 404 403 według mnie nie ma znaczenia, znaczy.  
Może jasna, nie masz dostępu to to, no nie masz dostępów.

**Adrian Kotowski** 5:32  
Tak, ale właśnie chodzi o to, żeby zmienić jednak innego napastnika, że jednak nie wiesz, czy da się po prostu nie masz do niego uprawnień.  
Więc wracaj mnie, no no no no no trwa jakby jest trochę bez sensu. Myślę, że dzisiaj tak no Łukasz się tego przyczepi czy będzie to?

**Piotr Buczkowski** 5:42  
Jabol.  
Nie to do tak, do tego się nie przyczepiają.  
Przyczepiają się do tego, że mogłaś sobie trenować i poprać jakieś dane, a nie to, że ci zwracają forbidden czy czy not found.

**Adrian Kotowski** 6:02  
Nie no, zdarzało się, że parę było takich 15, gdzie po prostu były ten problem, że macie.

**Piotr Buczkowski** 6:06  
Nie, nie było, nie, nie, nie pamiętam takiego.

**Damian Kaminski** 6:08  
Ale mówisz o Adrian, no faktycznie zdarzenia chyba modlicie czy gdzieś tam przeczytanych?

**Adrian Kotowski** 6:12  
Tak, że mieliśmy w którejś z tych też.  
Testów tam było tak właśnie, że bądźcie nie tego, że mieliśmy te, że mamy numery tych obiektów właśnie takie numeryczne. Czy takie całkowite liczbowe, że łatwo jest po prostu iść do góry? O jeden to jest przeglądać zasoby, bo nie mamy bolidów.

**Damian Kaminski** 6:24  
Mhm.

**Piotr Buczkowski** 6:28  
Nie pamiętam Adrian takiego pen testu nie było. Zwrócono uwagę, że simy zwracamy 404 zamiast 403.

**Adrian Kotowski** 6:31  
No to ty mogę posiłkować znaleźć były takie na pewno.

**Piotr Buczkowski** 6:38  
Czy odwrotnie?  
Jak najbardziej były takie to coś, że że że po prostu nie sprawdzaliśmy dokładnie uprawnień, na przykład zwracaliśmy dane użytkownika o danym.  
Który Użytkownik, który od powiedzmy atakujący sobie wpisał z palca?  
W jakimś tam narzędziu?

**Adrian Kotowski** 7:00  
No teraz właśnie poruszyłem ten temat, potem widziałem, że ani w jednym temat pojęcie dodawać właśnie to zabezpieczenie, żeby zwracać się internal Server error. Właśnie teraz informacji o tym, że to się nie Trwam.

**Damian Kaminski** 7:00  
Dobra.  
No.

**Piotr Buczkowski** 7:10  
Znaczy nie.  
Też proszę 404 statki tak czy 403 404 nie internet to jest internet.

**Adrian Kotowski** 7:19  
Tak właśnie to też.

**Piotr Buczkowski** 7:20  
To i to jest to też inaczej traktowane chociażby przez gateway, tak?

**Anna Skupinska** 7:24  
No ale to nie będzie tutaj, to po prostu chciałam, żeby tą informację zataić, że tego tego pliku nie ma na przykład.

**Piotr Buczkowski** 7:25  
Czy ta?

**Damian Kaminski** 7:32  
No dobrze, czyli zalecenie Piotra jest takie, że.  
Nie jest problemem, że pokazujemy, że on jest po prostu akces i tyle.

**Piotr Buczkowski** 7:40  
No tak.

**Adrian Kotowski** 7:41  
No dobra o k, no to to.

**Piotr Buczkowski** 7:42  
Czy to czytam fortnite, fortnite 400?

**Damian Kaminski** 7:44  
Czy forbidden?  
Dobra, to tak ustalamy.

**Adrian Kotowski** 7:47  
No to jak miałaś dobrze to jest to co mógłbyś, to jest dosłownie mnie tam chwilę to mogę dodać jeszcze tyle dać.

**Damian Kaminski** 7:51  
Tak, to jest chwila.  
To jest chwila w kontekście i załączników i podglądów, tak.

**Piotr Buczkowski** 7:58  
No tak tak.

**Damian Kaminski** 7:59  
No dobra, bo to znaczy był. Właśnie chciałem powiedzieć, że jeśli to jest duże wyzwanie, to nie chciałbym tego teraz upychać.  
Bo to nie wpłynie na testy takie typowo biznesowe, ale jeśli to jest chwila, no to róbmy to od razu.

**Adrian Kotowski** 8:12  
No znaczy, no lepiej by to.

**Piotr Buczkowski** 8:13  
No i tak i tak macie informacje co się stało tak czy.

**Damian Kaminski** 8:17  
O k no jeśli to myślałem, że to jest coś coś grubszego.

**Adrian Kotowski** 8:17  
Czy to jest?

**Piotr Buczkowski** 8:17  
Mówię nam odkryć jest zwracany ten aut tak czy jakość.

**Damian Kaminski** 8:24  
Dobrze, to ty, to Adrian zaopiekujesz? Tak?

**Adrian Kotowski** 8:26  
Tak no właśnie teraz naprawdę.

**Damian Kaminski** 8:27  
A ten kontekst ani gdzie, a nieco innego zwracała to ania ma to poprawić, czy czy ty to będziesz?

**Adrian Kotowski** 8:32  
Też to poprawię, bo tam mam dużą zmianę, też bez sensu, żeby to 2 osoby tam teraz zmodyfikowały to tam też chwilami wzajemnie.

**Damian Kaminski** 8:36  
No to właśnie żeby się dogadać. Dobra, czyli ty to ty to zaopiekujesz.

**Piotr Buczkowski** 8:39  
Znaczy.

**Adrian Kotowski** 8:41  
Tak no.

**Piotr Buczkowski** 8:42  
Nie zwracajcie braku dostępu jako pięćsetka, więc to jest pięćsetka.

**Damian Kaminski** 8:49  
No i weźmy taką uwagę w kontekście globalnym, a nie tylko repozytorium, tak żebyśmy nie wracali do tych dyskusji.

**Adrian Kotowski** 8:53  
No tak, znaczy to właśnie te właśnie w tym miejscu niepokoiło, bo to jest nie obsłużony błąd jakby, a tam myślałem tylko obsłużone zwracać.

**Damian Kaminski** 8:58  
Mhm.  
No dobra.

**Piotr Buczkowski** 9:02  
Jedyny błąd, którego nie powinniśmy zwracać, to jest autora. Jest tak.  
401, bo wtedy ci blogu.

**Damian Kaminski** 9:15  
Czy coś jeszcze w tym kontekście chcecie poruszyć albo w ogóle w repozytorium chcecie o coś Piotra dopytać?  
Czy wszystko jest poza tym na razie jasne?

**Adrian Kotowski** 9:24  
No na razie wszystko jest jakoś ten. Tak to jeden tak.

**Damian Kaminski** 9:27  
Dobra.

**Anna Skupinska** 9:27  
A takie właśnie jedna rzecz co do zapisywania, bo teraz używam po prostu case attachment jak one zapisują pliki to one używają sobie własnego systemu, zapisywania plików nie zmieniają chyba tam nic za bardzo gdzie one się zapisują i słyszałam, że.

**Piotr Buczkowski** 9:39  
Znaczy właśnie właśnie z no tak, tak przecież proponowałem jaką ma być, jak ma wyglądać ścieżka.

**Anna Skupinska** 9:41  
Potrzebowałam, żeby zmienić to chodzi o to tak, ok, to będę się tam pogrzebać i zmienić folder, w którym to się zapisuje.

**Piotr Buczkowski** 9:50  
To koniecznie.

**Anna Skupinska** 9:51  
Mhm.

**Damian Kaminski** 9:52  
W sensie zapisywanie fizyczne pliku.

**Anna Skupinska** 9:54  
Tak.

**Piotr Buczkowski** 9:54  
Tak, jeżeli mam zapisywanie pliku na dysku a nie w barze.

**Damian Kaminski** 9:56  
Tak to było omówione tak jak tak jak te.

**Anna Skupinska** 9:58  
Tak, tak, to jeszcze trzeba zrobić to jeszcze zrobię.

**Damian Kaminski** 10:00  
O k.  
Dobra.  
Ale tu wszystko jest jasne, tak tylko trzeba po prostu to poprawić, ale wiadomo jak i co trzeba zrobić.

**Adrian Kotowski** 10:10  
Się jest na tym, bo myślałem trochę o tym o tych uprawnieniach i reszta też przydałby się może mechanizmy na przykład historii prawnie, bo teraz mamy historię zmian w folderze, a adoro w sumie czy to a k.

**Damian Kaminski** 10:11  
No dobra.

**Anna Skupinska** 10:21  
Jest robię zapisywanie w historii, że jak zmienić uprawnienia folderu to się zapisuje do historii.

**Adrian Kotowski** 10:26  
A dobra faktycznie, bo nawet ci kiedyś mówiłem tutaj dobra, o k tak, tak, tak znaczy to to jest bardziej ogólnie się jakby historia folderu nie historię uprawni folderu dobra racja, tylko i to to to to, to to też mieliśmy dzięki też nawierzchnie dobra to.

**Damian Kaminski** 10:38  
A po staniu jest już jakiś raport?

**Anna Skupinska** 10:39  
Jeszcze takie pytanie co do zapisywania historii, bo zauważyłam, że jeżeli jest folder i znaczy nie wiem jest sprawa i ktoś pobiera z tej sprawy dokument, to jest to zapisywane w historii sprawy. Pytanie, czy powinniśmy też za to zapisywać w repo historie pozorem, jak ktoś pobierze plik?

**Damian Kaminski** 10:55  
Dobrze by było.

**Anna Skupinska** 10:55  
Czy nie?

**Damian Kaminski** 10:56  
Dobrze było.

**Anna Skupinska** 10:57  
O k.

**Adrian Kotowski** 10:58  
Że to nie to masz ten.

**Damian Kaminski** 10:58  
Chociaż poczekajcie, poczekajcie, bo na sprawie my to mamy jako dodatkowe logi, bo to może być dużo częstsze.  
Dużo częstsze działanie niż samo wgrywanie czy usuwanie i na sprawach mamy po prostu na procesach mamy dodatkowy checkbox podglądu i pobierania.  
Znaczy, wydaje mi się, że chyba podgląd nie ma sensu, no bo jak ktoś ma uprawnienia to wiesz, no nie wiem, zawsze może się znaleźć klient, który powie, że chce widzieć Kto przegląda, bo mógł się pomylić i mógł nastąpić.  
Nadanie uprawnień niezgodnie z polityką.

**Adrian Kotowski** 11:44  
Czy takie pytanie kto to powinien mieć dostęp do do historii folderu teraz?

**Damian Kaminski** 11:48  
Jeszcze tego nie definiowali śmy na razie stwierdziliśmy, że ma się zapisywać w ogóle jeszcze historia nie jest wycie.  
Pociągnięta do interfejsu i.

**Anna Skupinska** 11:56  
Wskazuje, że administratorzy pewno.

**Damian Kaminski** 11:58  
Na razie ustaliliśmy, że może być to po prostu jako mśp jako raport dodatkowy. Nie wiem, ja to znaczy, może inaczej nie, nie wiem. Jedyny pomysł, jaki na to mam sensowny to jest tak jak historia, mail i historia aktywności, czyli po prostu po stronie tutaj. Ja bym to raczej dokładał tutaj.  
O.  
Akurat coś robicie.  
Czy się dobra?  
No pytanie czy macie na to lepszy pomysł? Bo mój mój najlepszy jak dotąd jest taki, żeby tutaj dołożyć.  
Historię repozytorium.

**Anna Skupinska** 12:34  
No można było po prostu coś kolejną zakładkę.

**Damian Kaminski** 12:39  
Piotr, nie masz obiekcji co do tego?

**Piotr Buczkowski** 12:41  
Jeszcze Jeszcze raz żeby trochę śmiechu skruszył.

**Damian Kaminski** 12:43  
Żeby w ramach logów dołożyć kolejną zakładkę pod historię repozytorium.  
Mamy tutaj tą aktywność administracyjną i tak samo.  
I tak samo to to to znaczy.

**Lukasz Bott** 12:58  
Ale tu czekaj, ale historia, bo to represent to czekajcie.

**Anna Skupinska** 13:00  
Ryszard robi cię słońce od pobierania tej historii.

**Lukasz Bott** 13:04  
A ta historia yy repozytorium to nie, nie, nie, nie ten nie zawiera się w aktywności administracyjnej.

**Anna Skupinska** 13:11  
Ja.

**Damian Kaminski** 13:12  
Nie, nie, nie.

**Anna Skupinska** 13:13  
A jest w oddzielnym miejscu zapisywano.

**Lukasz Bott** 13:17  
Ukryli dobra, no ale.

**Piotr Buczkowski** 13:17  
Tutaj jest już bardzo dużo o tych.

**Damian Kaminski** 13:18  
Nie no, historia administracyjnej przecież nie masz, że ktoś nadał uprawnienia do konkretnej.

**Piotr Buczkowski** 13:22  
Znaczy, ja bym tutaj rozdzieli na przykład loginy, login, loga odbył tego tak dużo, że trudno cokolwiek już z innego znaleźć.

**Lukasz Bott** 13:30  
No no to na to ta.

**Damian Kaminski** 13:30  
Że tu nie powinno tego być, nie.

**Piotr Buczkowski** 13:33  
Znaczy ja bym to właśnie wydzielił do.

**Damian Kaminski** 13:33  
Też też się zgadzam. Wyrzucić to.

**Piotr Buczkowski** 13:36  
Do innej zakładki.

**Damian Kaminski** 13:38  
No dobra, no ale to już jest postulat odrębny, ale masz rację to nie ma sensu, żeby tutaj w historii typowo administracyjny był.

**Piotr Buczkowski** 13:44  
Wczoraj właśnie wczoraj czy to coś szukałem, czytam, czytam zeszłym tygodniu i przekopać się logout to.

**Lukasz Bott** 13:50  
A to.  
Ale słuchaj, ja po prostu tutaj nie dodać kolejnego przycisku filtru, po prostu filtr po typie aktywności.

**Damian Kaminski** 13:56  
Co najmniej filtr.

**Piotr Buczkowski** 13:59  
No to są całkiem całkiem. To nie jest login, nokaut nie jest administracji, aktywność administracyjna to jest aktywność zwykła.

**Lukasz Bott** 14:05  
Nie nie no no o k dobra?  
Wiesz co, ale to to się wiąże jeszcze z innym tematem, no bo tutaj też i klienci właśnie.  
Ja nawet raport pod raporty systemowy taki właśnie zrobiłem, bazując na tym login log out tak czy ten właśnie data ostatniego logowania jakieś tam ileś logowań tak do systemu tak danego użytkownika? No to to akurat w module raportow nie zrobiłem tak. No ale faktycznie może.

**Damian Kaminski** 14:32  
No to trzeba docelowo pewnie wyciągnąć tutaj tak na użytkownikach.

**Lukasz Bott** 14:37  
No tak tak no użytkownika wiesz wczoraj z danielem gdzieś tam rozmawiałem był, bo byliśmy o firmie tak. No to też się a propos tych raportów systemowych przypomniał na przykład tutaj informacja jakaś taka właśnie gdzieś to statystykach użytkowników, do tego ich typów niej typów i tym podobnych rzeczy nie. Czy to wewnętrzny zewnętrzny, czy administrator zastaw koksu, czy nie i tym podobne nie.

**Damian Kaminski** 14:37  
Tu jest zresztą data ostatniego, tak.  
Dobra.  
Kończąc tutaj ten wątek ania, uważam, że skoro tu logujemy nawet logowania, to tak pobranie tak na razie podglądu nie.  
Ee, czyli odpowiadając na twoje pytanie pobranie mogę zrobić na to zgłoszenie? Pobranie zapisujemy do historii.

**Anna Skupinska** 15:19  
Tak, zgaduję, że ona musi być z waginą, bo tutaj mamy wyświetlanie rzeczy z nacją.  
Agencja to oznacza to, że musisz podać.

**Damian Kaminski** 15:26  
Nie, nie poczekaj na ja wiem co to znaczy. Natomiast na razie nie mówimy o tym, że to wrzucamy tu. Na razie mówimy o tym, że zapisujemy do logów. Czy ktoś pobrał dokument?

**Anna Skupinska** 15:32  
A o k.

**Damian Kaminski** 15:38  
Ee a odrębnie na to trzeba będzie pewnie przygotować. To znaczy chciałbym też to podzielić tak, bo słuchajcie, no osoby odpowiedzialne są odpowiedzialne za REACT mają.  
Albo inaczej wy jesteście na obciążeni.  
W kontekście ich tak zawsze się nie wyrobimy, ze nie wyrabiamy ze zgłoszeniami dla nich, bo dużo szybciej po prostu obsługują to, co muszą zrobić, więc raczej tym elementem nie pamiętam. Chyba to Filip rogu wizualnym zajmie się Filip, a będzie potrzebował do tego tak jak mówisz, pewnie jakiegoś backendu.  
I ten Weekend trzeba będzie przygotować. Natomiast nie powiedziałbym, że to jest coś, z czym to jest ostatnia rzecz, którą będziemy się zajmować o tak.  
Bo to już nie wpływa na funkcjonalność samą w sobie, tylko to jest po prostu.  
Audit log i tyle.

**Lukasz Bott** 16:29  
A jeżeli teraz to jest jakoś tam rejestrowany, czy już możemy to rejestrować i niech tam sobie siedzi w jakiejś tabelce.

**Damian Kaminski** 16:34  
To już wstecz będziemy mieli dane.  
Dokładnie.

**Lukasz Bott** 16:37  
Niech sobie tam siedzi w bazie danych.

**Damian Kaminski** 16:41  
Ale spoko, no nie wiem, jeśli ty byś się chciał o tym zająć, no to ja mogę zobaczyć czy Filip tam ma jakieś inne zgłoszenia, bo jeśli masz ochotę, żeby to samemu zrobić to to też może nie mam nic przeciwko po prostu często jest tak, że tych rzeczy backendowych jest dużo, a front endowych ledwo się tutaj z kolegami wyrabiamy, żeby to po projektować, bo to zaprojektujemy projektowanie trwa tyle co wykonanie, czasami więc.  
Na ananas jest powiedzmy.  
Nie robimy tylko tego, a a Filip z tutaj przemkiem robią tylko to, więc no często jest tak, że się po prostu nie wyrabiamy już mówiąc wprost.  
Że coś dziś przygotowujemy, a już jutro jest to zrobione dobra, mniejsza o to na razie konkluzja jest taka zapisujemy, a jeszcze żeby to wyświetlać, to to do tego dojdziemy. Na razie jeśli to zapisujemy, to nawet na potrzeby testów, to to, co ci napisałem w tym zgłoszeniu, wystarczy, że podepniesz tutaj tylko pod źródła dane i wrzucisz tam do testów, że jest raport o nazwie takiej i takiej, i to się raportuje dziewczyny już mogą to sprawdzać, a to, że tu wyświetlimy później to już będzie tylko zakres.

**Anna Skupinska** 17:48  
A czy jest to zrobiłam tylko nie robiłam raportu, tylko zrobią po prostu fillm źródło danych, więc mogą wejść źródła danych i zobaczyć.

**Damian Kaminski** 17:54  
No to trzeba z tego źródła zrobić. Według mnie raport, żeby można było to odfiltrować łatwo.  
To będzie wygodniejsze. No jednak źródło danych jest ograniczony, dobra, ale nie chciałbym teraz całej rady. Tu już na ten temat poświęci, bo on jest raczej dość prosty, więc jak to zrobisz, to puścimy to dziewczynom.

**Anna Skupinska** 18:03  
No o k.

**Damian Kaminski** 18:12  
Dobra, wracamy do tego do do do głównego wątku, czyli rady tutaj.  
Piotr buczkowski dodatkowo na screenie widać spójność formatu danych. Ja to wpisałem na radę piotrze, czy to jest temat, który jeszcze wymaga dopisania czegoś? Czy według ciebie to już wszystko jest jasne i można to przekazać? Zakładam, że w.

**Piotr Buczkowski** 18:30  
Znaczy po pierwsze okazało.  
Mówi się, że w nowszej wersji już to.  
Jest spójnie, znaczy jest przekazywany format rok miesiąc dzieni tak to standardowy, ale nadal jest przekazywany jako strik.

**Damian Kaminski** 18:45  
Mhm, ale to jest front endowe zadanie czy Black endowe?

**Piotr Buczkowski** 18:49  
Nie wiem, nie wiem.

**Damian Kaminski** 18:49  
Według ciebie nie wiesz o k. Dobra?  
Dobra.

**Piotr Buczkowski** 18:59  
Znaczy w tej wersji, co tam jest u klienta? Po prostu przekazywał to, co widać, czyli na przykład tutaj, w tym format dzień, miesiąc rok.  
Nowej wersji też 6 też sorry szczerbca było już, że zawsze przekazuje rok miesiąc dzień, ale przekazuje jego string.  
Mimo że to działa według mnie lepiej to zrobi, żeby to przekazywało po prostu jako dalej. Tak będzie na pewno mniej problemów.

**Damian Kaminski** 19:26  
Dobra.  
No to wrzucam to.  
Przemkowi i niech to weryfikuj.

**Piotr Buczkowski** 19:37  
Właśnie mówię, nie wiem, pewnie powinien pewnie backend, ale nie wiem.

**Lukasz Bott** 19:39  
Zdaje mi zdradę.

**Damian Kaminski** 19:40  
Rozumiem.  
O k.  
Niech sprawdzi jak jak da się to rozwiązać właśnie co się da frontend owo to chcemy wrzucać tu na chłopaków, żeby oni jednak mieli ten swój backlog pełny, żebyśmy tutaj my się nie stresowali, że cały czas musimy im coś do produkować, a jak zweryfikują nawet taka rzecz pomoc, to wolę ich, wolimy ich obciążyć niż was.

**Piotr Buczkowski** 20:00  
Możesz, możesz. To możesz tam wrócić jeszcze do tamtego pytania.

**Damian Kaminski** 20:03  
Tak.

**Piotr Buczkowski** 20:04  
Jest tam załącznika jakiejś jest pokaż załącznik.  
To tutaj chodzi o to, p. 8 nie, nie, nie, nie, nie skromnie, p. 8.  
Zaczęło się tak.  
6 p 5 jest o k to 8. Natomiast tam zakresie po prostu.

**Damian Kaminski** 20:23  
O k to moja jak już wiesz co to mu wskaże.

**Piotr Buczkowski** 20:36  
Moje z nowej wersji jest już to w formacie tym takim uniwersalnym jak wyżej, ale nadal jako stringa lepiej, żeby dalej tutaj było.

**Damian Kaminski** 20:46  
Dobra.  
Tak samo zaznaczyłem.  
Dobra.  
No niech to Przemek sprawdza.  
Teraz tak tu było coś, co mniej wzbudziło podejrzenie don, a jednak rada architektów czy ty Piotr specjalnie to wrzuciłeś, czy to przeoczenie kasujemy to, czy chcesz coś tu poruszyć?

**Piotr Buczkowski** 21:11  
Poczekaj potem jeszcze chyba przed rokiem jest jakiś komentarz jakiś komentarz mój.

**Damian Kaminski** 21:16  
Już patrzymy nie ma, a kiedy to było tak przed nie dziesiątego to świeży temat chyba nie przed urlopem.  
Chociaż nie wiem.

**Piotr Buczkowski** 21:27  
Może tak dobrze wróć na details.

**Damian Kaminski** 21:35  
Wyliczany przed utworzeniem sprawy.

**Piotr Buczkowski** 21:45  
No nie powiem do czego to znaczy coś miałem, że.  
Po prostu zrobiłem tak, czy?  
Czy może chciałem, żeby czy czy jest sens zapisywać ten numer w case titel, czy on ma być automatycznie?

**Damian Kaminski** 22:05  
Nie według mnie nie ma sensu w tej stajni, to znaczy nie wiem jak dzisiaj jest może inaczej.

**Piotr Buczkowski** 22:05  
To.  
Bo teraz jest tak, że jeżeli jest cd i to właśnie stąd był błąd, tak, jeżeli jest kd.  
To trening starczą sprawdzać czy ten pejsaty Jezusa stoi, który jeżeli go nie ma, to go dodaje i stąd, jeżeli w tej stadion był zły kaisai, czyli na przykład 2 sprawy było naraz zrobione.

**Damian Kaminski** 22:27  
Mhm.

**Piotr Buczkowski** 22:28  
I dostały ten sam kejs idiotkę stali tool to jedna.  
No tak to.  
No to po prostu dodawano, miał 2 numery w tej strajku. Tak jeden ten nadany w momencie tworzenia sprawy, a drugi ten rzeczywisty.

**Damian Kaminski** 22:45  
Był to znaczy w kastrat tylko ci przypomnę, nie wiem czy pamiętasz, że tu jest ukrywanie tak czy to nie konfliktuje wtedy.

**Piotr Buczkowski** 22:55  
Ukrywanie.

**Damian Kaminski** 23:02  
Tu nie wyszukuje, czekaj, no gdzieś było.

**Lukasz Bott** 23:04  
Chodzi o to, że że jest jakiś parlament, który tym steruje.

**Damian Kaminski** 23:07  
Tak tak, tak jest parametr sprawy w tytule sprawy tutaj jest jeszcze to nie pamiętasz o tym.

**Lukasz Bott** 23:08  
Mi też się tak właśnie mi coś.  
No.

**Damian Kaminski** 23:16  
Że jak kliknę na tak to po stronie.

**Lukasz Bott** 23:19  
To będzie ukryte, no no no bo pamiętam, bo to Damian nawet dla Orlenu było specjalnie robimy.

**Damian Kaminski** 23:23  
O Orlen tak się do tego przyczepił, że to ich myli, że tam.  
Wygląda jak numer to numer teczki, a to jest numer wewnętrzny, czyli żeby powieść, żeby po prostu tego tu nie było? Tak jak to zaznaczysz.  
Żeby to nie skonfliktował na mnie.  
Jak zaznacza, tak.  
To powinno zniknąć i znika.

**Piotr Buczkowski** 23:48  
Łączą włącza dodawanie tego.  
Co zrobiłeś? Sorry bo.

**Damian Kaminski** 23:54  
Jeszcze raz tutaj wyłączyłem ostatnią pozycja i d sprawy w tytule sprawy kliknąłem na Ukryj.

**Piotr Buczkowski** 24:04  
No ale to ukrywa, a nie w usuwa.

**Damian Kaminski** 24:08  
Tak, tak, tak, tak, to znaczy tylko chodzi mi o to, że jak bo nie wiem jak to działa skąd bierze tą wartość czy.  
Z kolumny keitel, bo zapytałeś czy warto dodawać, no ja.

**Piotr Buczkowski** 24:17  
No.  
No tak, tak, tak tak tak. No popatrz nas popatrz na inne w zgłoszeniu.

**Damian Kaminski** 24:21  
O k.

**Piotr Buczkowski** 24:28  
Dobrze już wiem, po prostu chciałem pytanie, czy będzie ciałem, czy czy to poprawiać, czy po prostu sądzić ten mechanizm, żeby w tej sprawie trolling nie było okej i w nawiasie.

**Lukasz Bott** 24:41  
A co jeżeli ktoś sobie nadpisze regułą?

**Damian Kaminski** 24:45  
Ale to nas pisze.

**Piotr Buczkowski** 24:45  
Znaczy, to jest tylko domyśle. Oczywiście to jest domyślne.

**Damian Kaminski** 24:49  
Nie, nie pytasz czy czy tytuł domyślnie jeśli mamy tak jak tak jak było, czyli tu to czy tu powinien być kasę idi tak.  
To jest twoje pytanie powinien. No według mnie to zawsze tak było i to Orlen co do tego tam miał obiekcje, a tylko w jednym procesie, ale jednak bym powiedział, że ludzie są do tego przyzwyczajeni. Nawet jak wiesz robią screen'a.

**Piotr Buczkowski** 24:58  
Tak.  
Znaczy po, bo to jest, bo to jest kwestia tego, czy.  
Dobrze inaczej czy zapisywać to w krystaliczną czy nie.

**Damian Kaminski** 25:18  
Chodzi ci po stronie bazy danych?

**Piotr Buczkowski** 25:19  
Bo bo teraz jest, bo teraz jeżeli tego nie ma, to jest opisywaną tematycznie tak.

**Lukasz Bott** 25:26  
Ale do tego, czy tylko na poziomie frontendu jest wizualnie dopisywać.

**Piotr Buczkowski** 25:29  
Popatrz na screen, popatrz na screeny.

**Damian Kaminski** 25:31  
W bazie danych zakładom zarzutu 81. A tu 79.

**Lukasz Bott** 25:33  
No no tak.  
Tak tak no no widzę no.

**Damian Kaminski** 25:36  
Znaczy, a co nam to daje, że my to tu zapisem, bo ja nie widzę korzyści.  
Ale może jakaś jest?  
Że to zwracamy to watpi wtedy, ale wap też jest informacja zawsze odrębny węzeł kensei jest.  
Więc chyba nie ma?  
Korzyści tego, że zapisujemy to wartość w kolumnie keitel, bo rozumiem, że tak brzmi pytanie.

**Piotr Buczkowski** 25:59  
Takie są.

**Lukasz Bott** 26:05  
Wyrwie Piotr krochmal.

**Damian Kaminski** 26:06  
Wiem, wiem, wiem, że tak jest to znaczy dobra widzę, kiedy to może być przydatne w polach typu Odnośnik, tak.  
Bo tam ludzie mogą pamiętać kasai i to im się wyświetla domyślnie w tytule.

**Piotr Buczkowski** 26:23  
Nie.

**Damian Kaminski** 26:25  
Wreszcie strasznie rwie Piotr.  
Halo, halo.  
Musisz chyba postulować o lepszy komputer.  
No to już któryś raz się powtarza.

**Lukasz Bott** 26:44  
Oby wysiadły baterie w słuchawkach i mikrofonie.

**Damian Kaminski** 26:47  
Nie, nie wydaje mi się, że chyba Piotr ma jakieś może po uruchomione jakieś usługi i.  
To już w ostatnich 2 tygodniach kilka razy się zdarzyło, więc nie wiem czy.

**Lukasz Bott** 26:54  
No to.  
Może będzie miał zmieniany komputer tak jak mi wymienili to Piotr Piotrek też ma chyba wieku.

**Piotr Buczkowski** 27:07  
Tylko jedno okres halo halo słychać halo halo słychać.

**Damian Kaminski** 27:10  
Halo, halo.  
Tak teraz słychać, ale to w biurze masz tak słabo.

**Piotr Buczkowski** 27:11  
Czy nie?  
Tak, tak w biurze Jestem.

**Damian Kaminski** 27:18  
Mhm.  
No dobra, no to pole typu Odnośnik skomentowałem, że może to być wykorzystywane przez biznes.  
To może inaczej, bo to już jest dom. Pytanie, co tu faktycznie zrobiłeś, bo tu nie ma akceptant kryteria określone, a nie jest Przepraszam utworzyć sprawdzić czy tytuł.

**Piotr Buczkowski** 27:38  
Yy.  
Tak jak mówię, teraz było tak, że kasa itd.  
Była próba.  
Wyznaczenie jaka jest i przez przed internetem i insert był z tym saidi więc zaznaczonym przed internetem co spowodowało że.  
Jeżeli było 2 naraz inserty, no to dostawały te 2 2 razy ten sam okres i tak.

**Damian Kaminski** 28:03  
O k.

**Piotr Buczkowski** 28:03  
Ja zrobiłem, że update jest po po incydencie na podstawie z insert owanego już kasi d.

**Damian Kaminski** 28:10  
O k.

**Piotr Buczkowski** 28:10  
Czyli najpierw idzie na pojeździe wpis bez said, a później jest dotowany ten kejs id. Pytanie na radę architektów jest taki, a może to pominąć w ogóle?

**Damian Kaminski** 28:17  
No i.  
No to to tak jak mówię przestaną działać pola typu Odnośnik z filtrowaniem po itd.  
O k.

**Piotr Buczkowski** 28:33  
Jest to prawda.

**Damian Kaminski** 28:33  
Takie jest takie jest przykład, a ludzie mogą z tego korzystać, bo jak jakieś nie wiem.  
MPK jakieś oparte na rejestrach właśnie odnośniki, no to mogą pamiętać jakieś tam numerki, więc to by było ryzykowne.

**Piotr Buczkowski** 28:49  
Tak a propos zasięg sieci i teraz jest dobrze tak dobrze mnie słychać.

**Damian Kaminski** 28:52  
Tak, tak.

**Piotr Buczkowski** 28:53  
Co się w sieci z tego pokoju, gdzie Łukasz odsiedzi jest o wiele lepszy niż tam dzieja się Jestem teraz.  
Stoję przy biurku Łukasz.

**Damian Kaminski** 29:05  
No to trzeba może przekazać komuś, że żeby coś poprawili.

**Lukasz Bott** 29:05  
To może tam jest bliżej ten gdzieś?

**Piotr Buczkowski** 29:08  
Stoję, bo ktoś krzesło z winą.

**Damian Kaminski** 29:14  
No dobra, to ja bym to raczej chyba utrzymał tak jak jest. No wiem, że to dodatkowy zapis, ale.  
Myślę, że tutaj pozbycie się tego może spowodować się jakieś zgłoszenia typu bagi.

**Piotr Buczkowski** 29:26  
Ojej, czyli wszystko jest o k. Bez bez zmian, tak?

**Damian Kaminski** 29:28  
Dobra to odpinamy.

**Piotr Buczkowski** 29:30  
Błąd poprawiony taka sytuacja jak tutaj już nie powinnam wstawić.

**Damian Kaminski** 29:34  
O k. Dobra teraz.

**Lukasz Bott** 29:35  
Czyli wyeliminowałeś hazard, tak więc taki troszkę można powiedzieć.

**Damian Kaminski** 29:39  
No.  
Łukasz pytanie do ciebie, czy temat jest zaopiekowany, bo ja go tu nie widzę.  
To, bo to zakładam, że albo Piotr albo ewentualnie Adrian. Te odpowiedzi po resta ppi zmiennych typu dec.  
Że nie nie jest niespójny ilość miejsc po przecinku.

**Piotr Buczkowski** 30:01  
Wyszło odpowiada.

**Damian Kaminski** 30:03  
A już poprawiony dobra to nie mam pytań, tylko kojarzę to było.

**Piotr Buczkowski** 30:06  
Było tam było Get Well for.  
Ford PA tam jest zapisywany zwracany tylko z 4.  
Miejscami.

**Damian Kaminski** 30:17  
Dobra jako poprawiony to nie ma tematu, po prostu kojarzyłem, a i nie wiedziałem kto, czy to już jest zaopiekowane.

**Piotr Buczkowski** 30:22  
Tak uznał, uznałem, że to bardzo ważny powód i od razu zrobiłem.

**Damian Kaminski** 30:25  
Tak tak, nawet hotfix.  
Dobra, to co my tu jeszcze mamy czeka Jeszcze raz ran, tego już nie ma, dobra.  
Tu Piotra coś.  
Co musimy tu?  
Omówić na razie.

**Piotr Buczkowski** 30:42  
Yy.  
Musimy możemy dla sprawy stwierdzić, że sorry za dużo tutaj jest danych i nie indeksu jemy wszystkiego tego na przykład nie indeksuje my załączników.  
Wiem, że jest możliwość.

**Damian Kaminski** 30:59  
Nie rozumiem.

**Piotr Buczkowski** 30:59  
Na przykład.  
Zobacz, przejdź niżej.  
Tylko nie patrzy, nie jest na scenie widocznie załączników patrz na licznik po lewej.

**Damian Kaminski** 31:14  
Mhm.

**Piotr Buczkowski** 31:14  
Dla tej sprawy został przekroczony maksymalna długość wpisu w Stream bilde rze.

**Damian Kaminski** 31:19  
O k.

**Piotr Buczkowski** 31:20  
Zainteresowań.  
Po pierwsze najłatwiej to jest po prostu sprawdzać także.  
Yy, jeżeli sprawdzać tak jak to, jak dodajemy tekst tego sunil, to raczej nie przekroczyliśmy, jeżeli przekraczamy. No to sorry, więcej nie interesujemy.  
A drugiej rzeczy to po prostu, jeżeli jest, widzimy, że jest na przykład 100 załączników, czy tam nie wiem. 20 załączników w tych nie interesujemy.

**Damian Kaminski** 31:49  
Mhm, ale jakie to ma?  
Konsekwencje nie wiem biznesowe.

**Piotr Buczkowski** 31:56  
Biznesowe takie, że na przykład nie, nie nie poszukasz po treści tych załączników wyszukiwarce.

**Damian Kaminski** 32:02  
O k. Czyli nie indeks ujemy o k. Czyli nie puszczamy lusina na tym tak.

**Piotr Buczkowski** 32:04  
Techniczne takie, że nami.  
Nie tyle, że nie puszczamy lotnictwo, nie znaczy nie dodajemy do Rusin zawartości tych plików.

**Damian Kaminski** 32:15  
Mhm, ale to jest związane z tym, że one są w tabeli tak.

**Piotr Buczkowski** 32:19  
Że jest ich dużo.

**Damian Kaminski** 32:20  
Że jest ich dużo o k.

**Piotr Buczkowski** 32:22  
Mówię, nie patrzcie na to, ile jest kilku widocznym na screenie, patrzcie na ten licznik po lewej.

**Damian Kaminski** 32:28  
Mhm, czyli też jest 172, tak?

**Piotr Buczkowski** 32:30  
Tak.

**Damian Kaminski** 32:34  
No dobra, a to jest faktycznym przykład biznesowy.

**Piotr Buczkowski** 32:37  
Tak w tym w tej firmie znaczy w tej firmie było polecenie, że wyłączyć indeksowanie załączników dla tego procesu.

**Lukasz Bott** 32:46  
I ktoś dodał.

**Piotr Buczkowski** 32:47  
I to ktoś to wyłączyli i to wszystko działa tak i jak najbardziej tak powinno dostać.

**Lukasz Bott** 32:48  
Mnóstwo.

**Damian Kaminski** 32:54  
Aha, tylko natywnie powinniśmy to obsługiwać, że jeśli jest tak dużo, to sorry.

**Piotr Buczkowski** 32:55  
Tylko pytanie, czy my natywnie nie powinniśmy wykryć, że sorry?  
Jeżeli jest, powiedzmy tabela z 50 czy tam z 20 załącznikami, to to to nawet nie próbuję, aby dostosować załączników, bo nie ma sensu.

**Damian Kaminski** 33:05  
Przestajemy.

**Piotr Buczkowski** 33:09  
Po to indeks rośnie. Indeks puchnie, tak.

**Damian Kaminski** 33:09  
O k.

**Lukasz Bott** 33:15  
Ale to co to to mnie działoby się yy z punktu widzenia użytkownika obsługującego obsługującego sprawę rozumiem, że działoby się to cicho, tak nie był tego świadomy.

**Damian Kaminski** 33:15  
No dobra no.  
Tak.

**Piotr Buczkowski** 33:25  
No i tak no albo indeks jemy tylko nie wiem, kilka pierwszych załączników, jakiś limit tak, żeby nie indeksować 100 załączników, bo bo to nie ma sensu.

**Damian Kaminski** 33:35  
No tak, no bo tu można zarzucić, że to jest złe podejście do organizacji procesu, tak, skoro ktoś coś takiego robi. No pytanie, czemu tak, a nie odrębne sprawy na przykład tak, nie wiemy tak naprawdę, ale tu jest to jakieś starocie. 2010 2009, no to zrób sobie oddzielne sprawy na takie archiwa i tyle.

**Piotr Buczkowski** 33:47  
No to jak nie wiem, nie wiem co tam było, nie wiem, nie wiem.

**Lukasz Bott** 33:57  
Teraz będą mieli repozytorium dokumentów.

**Piotr Buczkowski** 33:57  
To być może być może to właśnie jest jakieś jakieś archiwum.

**Damian Kaminski** 34:01  
No właśnie.

**Lukasz Bott** 34:02  
No to teraz może trzeba zaproponować tym klientowi to repozytorium dokumentów, które dla filmu stworzyliśmy.

**Damian Kaminski** 34:08  
Na przykład.

**Lukasz Bott** 34:09  
No tak.

**Damian Kaminski** 34:11  
Bardzo możliwe tak bardzo możliwe, że masz rację.  
Dobra, według mnie tak no ustalimy tylko zasugeruj jakiś limit, nie wiem jak jaki jest zdroworozsądkowy, nie wiem pierwszych 10, no to już jest dużo. No to już jest naprawdę na potrzeby biznesowe, to już jest dużo.

**Piotr Buczkowski** 34:22  
No no tak tak.

**Lukasz Bott** 34:27  
Zwłaszcza, że statystycznie rzecz biorąc, pewnie te pierwsze 10 cm najważniejsze dokumenty tak w pierwszej kolejności załączone, no chyba, że ktoś tutaj, tak jak tutaj pewnie alfabetycznie.  
Wrzucał.  
Masz zrobił kopiuj wklej zawartości tego.

**Damian Kaminski** 34:51  
Tylko jaki to ma, jak to powinienem opisać? To dotyczy tylko tabeli, czy też załączników na liście załączników.

**Piotr Buczkowski** 35:00  
Wszystkich no tam wszystkich.

**Damian Kaminski** 35:05  
Dobrze, a jak załącznik jest usuwany to jest usuwany jego indeksacja czyli jak ktoś powiedzmy ma 9 ma 10 usunie jeden.

**Lukasz Bott** 35:05  
Załączonych do sprawy dokumentów.

**Piotr Buczkowski** 35:11  
Jej.  
I jeżeli usuniesz załącznik wprowadzić jakokolwiek zmiana dla sprawy cały wpis w indeksie dla tej sprawy jest stworzone na nowo.

**Damian Kaminski** 35:22  
O k.

**Piotr Buczkowski** 35:25  
Znaczy tak naprawdę załącznik, powiedzmy nieco na nowo odczytywane tylko w tej tabeli fulltext czytałam ft, z reszta jest odczytywana jego zawartość, ale ponieważ usuniętego już nie ma, bo to nie zostanie o jego usunięcie, jego zawartość odczytana.  
No ale sprawdz.

**Damian Kaminski** 35:58  
Dobra.

**Piotr Buczkowski** 35:59  
Panie.  
Przed dodaniem zawartości do steyera, sprawdzić, czy nie przekroczymy długości dostępnej stronie, bierze też należy zrobić.  
Szczerze mówiąc do tej pory nigdy tego nie robiłem, ale jak widać trzeba.

**Damian Kaminski** 36:15  
Ale to przed indeksację.

**Piotr Buczkowski** 36:18  
Masz masz, masz trening wildera do którego dodajesz tera liści z poszczególnych pól z załączników. Wszystko tak komentarze co tam masz?

**Damian Kaminski** 36:18  
Jak?

**Piotr Buczkowski** 36:27  
Przed dodaniem treści z danego pliku z danego komentarza należy sprawdzić, czy po dodaniu tego nie przekroczyły maksymalne i długości stringu Stream bilde.

**Lukasz Bott** 36:39  
Żebym to ta maksymalna długość jest znana? Tak?

**Piotr Buczkowski** 36:43  
Tak jest znana. Jest to określone w bibliotece.

**Lukasz Bott** 36:47  
No to jest systemowa wartość, robimy taki dobry.

**Piotr Buczkowski** 36:49  
Tak, tak.

**Damian Kaminski** 37:01  
Dobra, czyli to rozumiem, że to jest przypadek taki, jeśliby ktoś wrzucił pień załączników, ale na tyle dużych, że już po 5 kończymy i tyle.

**Piotr Buczkowski** 37:10  
No i jeżeli ktoś powiedzmy wrzuci.

**Damian Kaminski** 37:15  
Książkę telefoniczną.

**Piotr Buczkowski** 37:17  
Tak, książka telefoniczna wojnę i pokój czy cokolwiek tam tam takiego co głowa tego to jeszcze trzeba tam nie pamiętam ile milionów o ile milionów tych literek niż.

**Damian Kaminski** 37:25  
Dobra, czy coś tu jeszcze z wytycznych?

**Piotr Buczkowski** 37:32  
Ja pamiętam jakieś rozmiar to był chyba w puencie błędzie zamieszczone.

**Damian Kaminski** 37:37  
Dobra, ja bym tylko powiedział, że.  
Trzeba tutaj. Czy ty Łukasz przygotujesz na to jakiś krótki wpis?

**Lukasz Bott** 37:48  
Co wpis na.

**Damian Kaminski** 37:48  
Bo to trzeba było według mnie to powinniśmy opisać na wiki.  
Ee jako jakieś takie typu faku coś takiego odpowiedź Dlaczego nie można wyszukać?  
Mm albo dopisać do gdzieś tam wyszukiwania pełno tekstowego.  
Właśnie jakieś takie jakiś taki dopisek, że maksymalnie obsługujemy do 10 załączników na na sprawie. O ile załączniki nie są na tyle duże, że już wcześniej limit.  
Indeksowanych pozycji jest przekroczony i wtedy nie jest to, żeby ktoś nam nie zarzucił, że a ja mam na sprawie 20. My wprowadzamy 10 i nie mogę znaleźć punkt. Tym załączniku to nie jest błąd, tylko założenie.

**Lukasz Bott** 38:30  
Jeden jedenastego dwunastego nie znajduje tak.

**Damian Kaminski** 38:33  
Dokładnie, żebyśmy to mieli po prostu na wiki, żeby ktoś tego nie podważył, że to jest błąd aplikacji. No nie błąd tylko tak działa aplikacja.

**Lukasz Bott** 38:41  
Dobra, wiesz co ty sobie numer zgłoszenia zapisałem tutaj rzymowi. Dobra, to taką adnotację można dodać tylko może, ale rozumiem, że to trzeba to nie wiem, no mogę mogę teraz dodać tak albo po prostu jak to zadanie zostanie zrobione na dan? Tak, bo.

**Damian Kaminski** 38:58  
Według nie można już dodawać.

**Lukasz Bott** 39:00  
W sumie to jako taka dobra praktyka, tak, że jeżeli.

**Damian Kaminski** 39:03  
Pełno tekstowe.

**Lukasz Bott** 39:09  
Nie oddał konfiguracja wyszukiwania pewną tekstowego. Ja myślę, że to w tym artykule jako taka.

**Damian Kaminski** 39:13  
Znaczy pytanie, czy sama konfiguracja czy używanie nie, bo to jest konfigurator, ale o k nawet tu gdziekolwiek jak to zamieścimy to już.

**Lukasz Bott** 39:21  
Tak wiesz, jakieś takie uwagi dodatkowe uwagi, tak no wyszukiwanie to też.  
Albo wyszukiwań sprawy, bo Jezus?

**Damian Kaminski** 39:30  
Tutaj jest pełno tekstowe, tak?

**Lukasz Bott** 39:33  
Z którego to roku artykuł łomatko.

**Damian Kaminski** 39:35  
Dwudziestego.

**Lukasz Bott** 39:39  
Znaczy, z dwudziestego czasu zostało zł.

**Damian Kaminski** 39:39  
Dobra, to gdzieś tam znajdziesz i tam rzucisz.  
Dobra, idziemy dalej, żeby jakoś skończyć po ludzku.  
Dobra, to tu opisałem. Już możesz robić 22 952 3. Zapamiętasz tak.

**Lukasz Bott** 39:53  
Tak ja sobie tak.  
Zapisz, bo się nie zapisał.

**Damian Kaminski** 39:59  
Nie, ale według mnie się, że piszą, bo tutaj tu miałem ciebie wywołać, a już rozumiem, że będziesz na to masz to spisane, to tamto już było zapisane.

**Lukasz Bott** 40:01  
Nie, nie, nie zapisałeś sejf?

**Damian Kaminski** 40:09  
Dobra, brak tłumaczeń nazw przycisków na liście spraw do wykonania języku ukraińskim, czemu to jest no.  
Czemu to jest na Radzie?  
Widoku listy spraw do wykonania użytkownicy korzystający z interfejsu w ukraińskim widzą jedynie techniczne nazwy przycisków. Tłumaczenia zostały ustawione i są widoczne na poziomie pojedynczej sprawy, jednak nie są stosowane w widoku listy. Problem dotyczy wszystkich procesów oraz wszystkich użytkowników.

**Lukasz Bott** 40:44  
Ale tu mamy to.  
Bo być może nie dodali obsługi języka ukraińskiego.

**Damian Kaminski** 40:51  
No ale zobacz tu jest.

**Lukasz Bott** 40:55  
Co?  
Interfejs interfejs jest, ale żeby dodać tłumaczenie to musisz ustawić parametr.

**Damian Kaminski** 40:56  
Tu.

**Piotr Buczkowski** 41:02  
Nie, nie wejdź, wejdź do sprawy, tak?

**Damian Kaminski** 41:05  
Nie no przecież tu działa. Zobacz.  
Nie działa tylko na liście.

**Piotr Buczkowski** 41:11  
Pytanie, czy na liście? Bo bo bo to, bo to co to co jest tu mi się kolano na liście, to jest przeliczone tabelkę isaksson.

**Lukasz Bott** 41:12  
A na liście, a na liście ok. Dobra, dobra, dobra.

**Piotr Buczkowski** 41:23  
Taka kasa.  
Jakoś się jakaś jest taka kolumna w kes definition.  
Coś?  
I tam powinny być tam sobie się.

**Damian Kaminski** 41:33  
Problem dotyczy wszystkich języków.

**Piotr Buczkowski** 41:35  
No właśnie i to nie to nie jest tłumaczone, to trzeba dać tłumaczenie, tak.

**Lukasz Bott** 41:35  
No dobra, dobra.

**Piotr Buczkowski** 41:40  
Że nie to, że zapisywałaś tłumaczenia w tym hotelu, tylko że tłumaczyć przy wyświetlaniu.

**Damian Kaminski** 41:40  
Dobra, to jakie są wytyczne?

**Lukasz Bott** 41:47  
Ale to tłumaczyć tłumaczenie robić w blocie jak renderujesz listę.

**Piotr Buczkowski** 41:52  
Dobrze Jeszcze raz teraz ten hotel z tym już siedziskami jest zapisywany w tabeli jest definition żeby go nie nie przeliczać w momencie wyświetlania sprawy.

**Lukasz Bott** 42:02  
Jasne, zgadza się. No o k.

**Piotr Buczkowski** 42:03  
Bo to by było zabójczo wydajnościowo, ale tam jest zapisywana wartość.  
Warto się jaka wartość.  
Wyświetlana tak wartość teraz sory za wewnętrzna.

**Lukasz Bott** 42:16  
Ok.

**Piotr Buczkowski** 42:19  
Bo to było robione, kiedy nikt nie myślał jeszcze od nazwami wyświetlanych. Trzeba tam dodać jakiś znacznik, że tłumacz tak.  
Przetłumacz to wartość na przykład z jakimś, żeby to szybko działało tak, że mnie wyszukiwać nie tworzyć kejsa nie tworzyć znaczy kasa jest, ale nie tworzyć jakieś tam ról, tak.

**Damian Kaminski** 42:42  
Czyli tak to byli kiedyś?

**Piotr Buczkowski** 42:43  
Nie, nie, nie, może nie może to być też, no przecież na przykład tłumaczenie bieżącego użytkownika dla bieżącego użytkownika.  
Ponieważ odbiorcą może być Użytkownik z innym językiem.

**Damian Kaminski** 42:56  
Mhm.

**Lukasz Bott** 42:56  
Mhm.

**Piotr Buczkowski** 42:57  
Czy jeżeli ja na przykład wysłałam tą sprawę to nie może być po polsku, skoro wysłałem do ukraińca?  
On chciałby mieć o swoje po swojemu, tak?

**Damian Kaminski** 43:11  
Czyli dzisiaj zapisywany html odpowiedzialny za wyświetlanie tej belki w zakładce do wykonania jako gotowiec, należy dołożyć obsługę tłumaczeń za pomocą indyków, przycisków tak.

**Piotr Buczkowski** 43:15  
Tak.  
Trzeba myśleć jak tu dobrze zapisywać w tej w tej w tej pozycji, żeby to później szybko i.  
Wydajnie było można było przetłumaczyć momencie, wyświetlenie listy spraw.

**Damian Kaminski** 43:38  
Dobra, to niech tak.

**Piotr Buczkowski** 43:38  
Mogę mogę, mogę ja to myśleć?  
Że jest taka potrzeba.  
Albo potwierdzi, czy to jest tak jak ktoś myślę, że tak jest ok.

**Damian Kaminski** 43:54  
Dobra, to na razie niech to ma u siebie Mariusz, jak on nie zdąży albo nie da rady, to przekażemy to do ciebie. Na razie zapisuję to tak, że trzeba wymyślić i przedstawić na razie nad tym nie przyjść do realizacji i tyle. Na razie zadanie polega na opracowaniu metody, jak to obsługiwać.  
A ty na razie zajmuj się tym co.  
Tym co musisz, a do tego w razie co wrócimy, no to tak jest od samego początku, więc jeszcze chwilę poczekają. Dobra, czy my coś tu jeszcze mamy? Limit zapytań to jest temat niekoniecznie, nawet jeśli nigdy utworzenia.  
Ee.  
To jest w ogóle dobra?  
Tu tylko ten element, bo wczoraj to stępnie z Kamilem omawialiśmy.  
Czyli tak, jeśli Użytkownik nie ma prawa do utworzenia sprawy z poziomu panelu amo tita, to nie powinien mieć możliwości również poprzez link, bo dzisiaj sklejając sobie link ten.  
Zostawcie każdy go wywołując tworzy sprawę.

**Piotr Buczkowski** 44:59  
No tak.

**Lukasz Bott** 44:59  
Niezależnie od tego, czy ma tutaj uprawnienia, czy nie ma tak.

**Damian Kaminski** 45:02  
Tak dokładnie i teraz mamy na to. Trzeba nałożyć konteksty uprawnień, ale też Stanów.  
I w kontekście uprawnień to jest proste, bo proces może być uruchamiany przez i uruchamia sprawy, jeśli pole jest null lub router należy do grupy lub jest jawnie zdefiniowany.

**Piotr Buczkowski** 45:20  
Trzeba trzeba dodać, trzeba dodać drugiej sprawdzanie w tym momencie i tyle.

**Damian Kaminski** 45:25  
Ale chwilkę jeszcze to.  
Ten procesu.

**Piotr Buczkowski** 45:31  
To to tak samo trzeba dodać.

**Lukasz Bott** 45:37  
No co ty masz na myśli stan aktywny w sensie?

**Piotr Buczkowski** 45:39  
Zwykły Użytkownik nie może nie może utworzyć sprawy z procesu, który jest nieaktywny.

**Damian Kaminski** 45:46  
Czyli tak tylko to jest tak aktywny, nieaktywny usunięto. Co to jest te nazwy, to to dużo dużo, że tak powiem.

**Lukasz Bott** 45:46  
A o k stan aktywno tam dobrze?  
Ja to chodzi dobra, dobra?

**Piotr Buczkowski** 45:52  
Aktywny aktywny można tworzyć sprawy nieaktywny tylko administratorzy mogą sprawdzić, tworzyć sprawy usunięte nie można tworzyć spraw.

**Damian Kaminski** 45:58  
Dokładnie.  
Znaczy może inaczej to są już wytyczne jak powinno być, a dzisiaj aktywny po prostu wyświetla się wszystkim w zakładce procesy nieaktywny tylko administratorom unii usunięty nikomu tak.

**Lukasz Bott** 46:03  
O k. Dobrze.  
Nie wiem czy ja wiem, nie, nie, nie, to nie, to nie musisz mi tego tłumaczyć.

**Piotr Buczkowski** 46:12  
I i nie jest to nie jest to, nie jest to sprawdzane w tym momencie, czy tam na tej stronie, która podałem.

**Damian Kaminski** 46:21  
Dobra, czyli stan procesu działa?

**Piotr Buczkowski** 46:26  
Znaczy zachować dodać sprawdzenie dodatkowe w tym momencie przy samym tworzeniu sprawy.  
O nie tylko przy wyświetlaniu ikonek. Czy tam kafelków, jakie masz procesy dostępne?

**Damian Kaminski** 46:39  
Dobra, czyli analogicznie jak dla t fej su no zastanawialiśmy się.

**Piotr Buczkowski** 46:45  
Znaczy to.

**Damian Kaminski** 46:47  
No.

**Piotr Buczkowski** 46:48  
Dodać sprawdzanie went połacie po prostu dodatkowe, tak czy czy jest czy masz prawo to zrobić?  
Tak naprawdę tam jest jedna funkcja.  
Wywołać tak.  
Greatest czy coś jakoś tak?

**Damian Kaminski** 47:05  
Tak tylko zastanawiam się nad tym, czy sam nawet przypadkiem gdzieś tak nie robiłem.  
To znaczy, ja może nie, bo ja akurat linku osobiście nigdy nie korzystałem, tylko czy jest taki przypadek, że.  
Gdzieś może wdrożony, że coś jest ustawione jako nieaktywne, ale.  
Na przykład jest to zaszyte z poziomu. Nie wiem innego procesu doszedłeś do jakiego się tapu, więc przyciśnij ten przycisk i utworzy ci się.

**Piotr Buczkowski** 47:34  
Jeżeli robisz z reguły klientka jest to jak najbardziej od od definicji logiki reguły zależy, czy utworzyć ten proces, sprawę czy nie.

**Lukasz Bott** 47:44  
No tak, bo rozumiem, że klient case właśnie sprawdzę.

**Piotr Buczkowski** 47:45  
Tam.

**Damian Kaminski** 47:46  
Ale ale chodzi ci o to, że robisz to jako wtedy, zrobisz to na uprawnieniach systemowych.

**Piotr Buczkowski** 47:46  
No to to.  
No nie.

**Lukasz Bott** 47:52  
Nie.

**Piotr Buczkowski** 47:52  
Jeżeli jeżeli w regule, jeżeli w regule jest skrytkę jest zadany proces, to utworzy sprawę niezależnie od tego, w jakim ten proces jest te stanie, kto może tworzyć ręcznie to.

**Damian Kaminski** 47:53  
Nie, bo mam na myśli, bo poczekaj, no powiedz.  
Mhm.  
A bo to nie jest link jasne, bo to jest odrębnie o k. Dobra, dobra, masz rację.

**Piotr Buczkowski** 48:07  
To jest po prostu.

**Damian Kaminski** 48:09  
Dobrze na zinterpretowałem to mhm.

**Piotr Buczkowski** 48:10  
Wrogie była utworzy.  
Reguła otworzy sprawę, bo bo bo administrator, bo twórca reguły zdecydował, że w tym momencie Użytkownik mał. Mam miec możliwość utworzenia utworzenia tej sprawy, ale tylko w tym momencie w tej reguły jest o k.

**Damian Kaminski** 48:24  
Mhm.  
Dobra, czyli aktywny wszyscy nieaktywny tylko admini.  
I tu już uprawnień raczej czy to ma sens jeszcze po tym sprawdzać uprawnienia? Chyba nie.

**Piotr Buczkowski** 48:42  
Jak?  
Znaczy, jak najbardziej znaczy administrator, zawsze może tak.

**Damian Kaminski** 48:44  
Bo.  
No właśnie więc nie trzeba.

**Piotr Buczkowski** 48:49  
Jeżeli ktoś nie jest znaczy tam mówię jest jedna funkcja, która sprawdza, czy Użytkownik musi może utworzyć sprawę z tego procesu. Ona jest używana.  
Przez zwracanie listy dostępnie procesu trzeba ją użyć tutaj nic nie trzeba wymyślać dodatkowego.

**Damian Kaminski** 49:04  
O k to podasz jakąś jakieś?

**Piotr Buczkowski** 49:07  
Nie, nie.  
Przy tworzeniu sprawy na MKISPX dodać sprawdzenie, czy Użytkownik może stworzyć.  
Sprawę z tego z procesu z wykorzystaniem obecnie istniejącej funkcji używanej przy zwracanie listy dostępnych procesów.  
Tak.

**Damian Kaminski** 49:28  
Czekaj za szybko przy tworzeniu sprawy na mk s px dodać sprawdzanie.

**Lukasz Bott** 49:35  
Sprawdzenie, czy Użytkownik może utworzyć sprawę.

**Piotr Buczkowski** 49:36  
Yy.  
Sprawę z przesłanego procesu tak z przesłanego provide.

**Damian Kaminski** 49:54  
Mhm.

**Piotr Buczkowski** 49:54  
Bo tam jest w atrybucie tak, że MK tutaj spx może mieć albo ksiki, kiedy otwiera sprawa albo proc. I tworzy sprawy i otwiera.  
Należy użyć tej samej metody, który jest używana do spraw do zwracania listy dostępnych procesów dla danego użytkownika.  
No tam jest, że pobierz wszystkie procesy i dla każdego procesu sprawdź, czy Użytkownik.  
Może tworzyć sprawy.

**Damian Kaminski** 50:27  
Dobra no zakładce procesy, żeby było wiadomo o co chodzi z tą listą.  
Dobra.  
Która jest wykorzystywana?  
No dobra, to w zasadzie możemy tu wrócić już na religii, tu dół i wziąć kto tam będzie miał czas, to się tym najwyżej zajmie effort jeden.

**Piotr Buczkowski** 50:54  
Jeden.  
Może trzeba dodać, trzeba dodać sprawdzania.

**Damian Kaminski** 50:56  
No to super.  
Dobra.  
No to.  
To reszta chyba czeka i może poczekać. Tak mi się wydaje. Jeszcze możemy zobaczyć change date czy tutaj coś jest?  
Tłumaczenie, mówiliśmy dodać wykrywanie przekroczenia Stream, omówiliśmy błąd w raporcie opartym.  
A.  
Dobra tu pytanie, czy to jest, bo to ja chyba podpiołem, czy to jest zadanie front endowe czy backend owe pewnie back endowe tak czyli translacja.

**Piotr Buczkowski** 51:31  
Brak endowy.

**Damian Kaminski** 51:33  
O k.  
No dobra, no to to musimy obsłużyć, no bo to na starych działało, na nowych też powinno działać no i tyle.

**Piotr Buczkowski** 51:42  
No to.  
Dla starych raportach dla oral dla są tam specjalne wyjątki jak tworzyć zapytanie.

**Damian Kaminski** 51:48  
Mhm, dobra dopisze to, że że w zasadzie no tu pewnie.  
Nie, to już jest opisane promoc budowania lub fortu.  
W ramach starego modułu no k jest translacja składni, zapytań no dostosowaną do roku należy wykonać analogiczną w nowych raportach. No to to czeka już w zasadzie chciałem się tylko upewnić, że to.  
Że to tak wszystko jest dobrze. Nie masz tu pierwszy uwag, tak.

**Piotr Buczkowski** 52:15  
Po prostu trzeba trzeba wykryć co to jest źle robione, co nie działało na uralu i zrobić tak, żeby działało też na reagowaniu.

**Damian Kaminski** 52:22  
Nie.

**Piotr Buczkowski** 52:23  
Oczywiście zachowując działanie na moje skóra jest serwer.

**Damian Kaminski** 52:27  
Mhm, dobra, to wydaje mi się, że to jest import danych do tabeli. Odnośnik do źródła to jest jeszcze dość świeże.  
Łukasz z redaguje, czy to musimy?  
Czy zostawiamy?  
Import danych z excela do tabeli pojawia się problem z polem Odnośnik do źródła zewnętrznego. Klucz główny jest ustawiony na inną kolumnę niż to, które jest wyświetlany. Aha, czyli eksport i import powoduje, że się zmieniają dane tak.

**Piotr Buczkowski** 53:00  
Oj tego się nie da zrobić.

**Lukasz Bott** 53:02  
No właśnie.

**Piotr Buczkowski** 53:04  
Znaczy.

**Damian Kaminski** 53:05  
No bo tak to rozumiem, że po prostu eksportując importując to samo po prostu zmieniają ci się dane w odnośniku.

**Piotr Buczkowski** 53:09  
A albo albo eksportujemy klucz wartość klucza.

**Damian Kaminski** 53:13  
Mhm.

**Piotr Buczkowski** 53:14  
I wtedy z importem miała problemu.  
Albo że tego się nie da zrobić.

**Damian Kaminski** 53:19  
No właśnie.  
Znaczy.  
Chyba żeby się.  
No ale to takie obejście, że jakaś dodatkowa kolumna, która by wpływała na to, ale to takie rzeźba.

**Piotr Buczkowski** 53:34  
Mówię, albo po prostu to zmieniamy eksport. Tak znaczy nieprawda. Nie poprawiamy importu z poprawiamy eksport, że eksport takiego pola zwraca wartość z klucza, a nie wartość. Wyświetlano wtedy import działa od razu.

**Damian Kaminski** 53:47  
Mhm.

**Piotr Buczkowski** 53:49  
Albo to jest nie do wykonania.

**Lukasz Bott** 53:52  
Jasne.

**Damian Kaminski** 53:54  
Jeszcze alternatywnie, jeśli to jest źródło zewnętrzne, to można by zbudować raport do eksportu.

**Piotr Buczkowski** 53:59  
A ja jak jest dla odnośnika zwykłego do sprawy?

**Damian Kaminski** 54:07  
Nie wiem, nie wiem co jest zwracane w eksporcie w imporcie na pewno jak wprowadzasz bezpośrednio KID, to tak jest przypisywane pewnie tak samo, pewnie tak samo jak tu.

**Piotr Buczkowski** 54:15  
No no tak, bo.  
To to ja to tego właśnie jest moja uwaga także.

**Damian Kaminski** 54:24  
Nie jest to spójne, nie?

**Piotr Buczkowski** 54:25  
Dla dla dla odnośnika też jeżeli zapiszemy tytuł sprawy czy tam nazywają się czy tam wartość wyświetlaną tak to już imporcie też może na mnie wyczyścić.

**Lukasz Bott** 54:36  
No tak, no chyba, że zapewnisz, że ta nazwa wyświetlana jest unikalna, nie.

**Piotr Buczkowski** 54:38  
Jest.  
Sobie tak tak samo można odczuwać zewnętrznego tak, jeżeli jest nazwa unikalne, to możemy przepisać po nazwie wyświetlanej, ale jeżeli nie jest no to nie przypiszemy.

**Damian Kaminski** 54:50  
Znaczy najprościej bym powiedział, że wtedy jeśli te dane trzeba eksportować importować, to chyba.  
Raport osadzony wtedy.  
Do eksportu.

**Piotr Buczkowski** 54:59  
Znaczy tam co do tabeli importu do tabeli, tam było też w dyskusja dziś, że wyczyścił pola ukryte. Tak czytam tylko dotyczy tu.

**Lukasz Bott** 55:07  
No no.

**Piotr Buczkowski** 55:09  
Bo teraz to działa tak, że jest po prostu skasowane wiersze dodawane nowe, tak.

**Damian Kaminski** 55:14  
Mhm.

**Piotr Buczkowski** 55:14  
Być może trzeba dać opcję, że updatu i wiersze.  
I wtedy on nie zmienia tych pól.  
Które, które nie potrafi tak, które nie widać, których nie ma danych.

**Damian Kaminski** 55:27  
Mhm.  
Tylko.  
Musiało być wtedy określenie klucza.

**Piotr Buczkowski** 55:35  
No nie to znaczy po po numerze, tak.

**Damian Kaminski** 55:38  
Okej, masz na myśli tak, no bo dzisiaj Ki chyba nie jest eksportowane nawet z tabeli.

**Piotr Buczkowski** 55:40  
Tak, tak, tak.  
No to powinno być.

**Damian Kaminski** 55:49  
Mhm no dobra, no ale to już jest odrębne zgłoszenie.

**Piotr Buczkowski** 55:51  
Znaczy.  
Tak.  
No tak.

**Damian Kaminski** 55:55  
Można by to tak zaopiekować. No tak jak w rejestrach, tak.

**Piotr Buczkowski** 55:57  
Ten mechanizm nie służył do tego, żeby nie wiem wyeksportować do excela, zmodyfikować w excelu i w kracie excela na nowo.

**Damian Kaminski** 56:02  
Tak.

**Piotr Buczkowski** 56:04  
To nie do tego ten mechanizm jest ten ten mechanizm jest do wypełnienia tabeli na podstawie excela.

**Damian Kaminski** 56:04  
Dokładnie.

**Piotr Buczkowski** 56:09  
A nie to, że ktoś nie lubi interfejsu webowego i co excelu pracować?

**Damian Kaminski** 56:15  
Znaczy, jeśli jest taki przypadek, to po prostu trzeba się dowiedzieć, Dlaczego nie lubi tak i co możemy usprawnić, żeby nie musiał eksportować do excela.

**Lukasz Bott** 56:15  
No tak no.  
No widzę bo to jest, p tak.

**Damian Kaminski** 56:23  
Bo to jest faktyczna przyczyna problemu, że ktoś chce wyeksportować żeby obsłużyć dzień. Witam importować no to pytanie, co możemy poprawić w naszym interfejsie, żeby wyeliminować w ogóle te 2 kroki?

**Lukasz Bott** 56:34  
Już ci mówię co?

**Damian Kaminski** 56:35  
No.

**Lukasz Bott** 56:37  
To sprowadza się do czegoś, czego nie mamy, a mianowicie jak masz raport z tabelarycznym.

**Damian Kaminski** 56:45  
Raport, tak, nie tabela.

**Lukasz Bott** 56:45  
Tak.  
Nie nie, tabelę na formula, nie tabelę na formularzu tylko powiedzmy, że dane z tabeli też przedstawiasz w postaci raportu, no i nie ma trybu edycji.

**Damian Kaminski** 56:56  
No.

**Piotr Buczkowski** 56:56  
Ganges.  
Żaden z tabeli przedstawiasz znacie tabeli?

**Lukasz Bott** 57:01  
No podłącz robić sobie na raport z jakiegoś procesu i podłączysz to pelno.

**Damian Kaminski** 57:02  
No właśnie raport osadzony w dowolny raport z tabeli, tak po prostu raport z procesu, ale to akurat.

**Lukasz Bott** 57:06  
Tak.

**Piotr Buczkowski** 57:07  
Akto ktoś tak a ktoś tak robi po co?

**Damian Kaminski** 57:12  
Ale czekaj, Piotr, bo, bo ty narzuciła swoją interpretację.  
Dokładnie Łukasz wyjaśni, jak to jest, co nie działa Jeszcze raz.

**Lukasz Bott** 57:22  
Dobra to widzę customer dotyczy dotyczy to klienta PKFPK to dotyczy tego procesu to od strony tak biznesowej nie, nie wnikając w technikę w technikalia na razie tak.

**Damian Kaminski** 57:27  
Tak.  
Mhm.

**Lukasz Bott** 57:36  
Od strony biznesowej to dotyczy tego procesu związanego z rejestracją czasu pracy na dany dzień. Tak czytam nawet na kilka dni tak i chodzi o to, że mają sobie gdzieś sformatowany excel tak w jakiś tam sposób, który który zawiera dane, to tak jakbyśmy my chciałbyś się za cały tydzień RCAU nas tam i tam się wypełnić nie, ale sobie te informacje.

**Damian Kaminski** 57:41  
Mhm.  
Mhm.

**Lukasz Bott** 58:06  
Gdzieś tam ski prałeś sobie weksel tak i chciałbyś sobie hurtowo zaimportować sobie zawartość tego excela. Tak, one są oczywiście w odpowiednik tam kolumna kolejności.

**Damian Kaminski** 58:16  
No to ja wiem, bo ja ja ich badałem trochę pod kątem wymagań, ale powiedz mi tak tam jest rtp na każdy dzień odrębny, każda sprawa jest na jeden dzień, tak?

**Lukasz Bott** 58:19  
No.  
Na dany na dany dzień jest sprawa, na której jest tabela, gdzie wpisujesz konkretne godziny na zad.

**Damian Kaminski** 58:31  
Mhm.  
Zadania z tego dnia.

**Lukasz Bott** 58:35  
Tak no konkretne projekty, no to czy dam zlecenie?

**Damian Kaminski** 58:36  
Czyli tak jak u nas tylko u nas jest to zewnętrzna aplikacja, ale u nas też klikasz na dany dzień wyświetlają ci się zadanie z danego dnia i Teraz ja bym powiedział tak, a czemu tam nie jest zrobione tak że jest fillm nie wiem jakiś checkbox skopiuj z dnia poprzedniego, bo najczęściej to jest tak, że oni mają.

**Lukasz Bott** 58:42  
No dokładnie tak.  
I to Damian, moment moment i i tak, i właśnie tego typu mechanizmy naprawdę to Kamil spyrka też już po po mnie to przejął, to byśmy tam już taki do do godziliśmy moim zdaniem, że na razie myślę, że ten temat spokojnie możemy zaparkować.

**Damian Kaminski** 58:52  
No.  
No dobra, tylko jest investigate to co z tym robimy, no bo nie da się tego zrobić. Tak jak powiedzieliśmy więc pytanie, by to służycie wdrożeniowe, ewentualnie odrzucicie taką potrzebę czy coś mamy z tym robić, bo nie wiadomo co z tym zgłoszeniem w takim razie.

**Lukasz Bott** 59:22  
Jakie? A jaki mamy możliwe Stany? No możemy zrobić strimów, albo tu Piotrek do hamburski zgłosił dobra.  
Czy to jeszcze w innym?

**Damian Kaminski** 59:32  
No właśnie to to jest taka rzeźba, ale no to tak można zrobić. Też tak też tak.  
Pomyślałem tak tylko, no to jest taka rzeźba, no.

**Lukasz Bott** 59:39  
No.  
Dobra, to jest to ok. Dobra, to to teraz to Piotr burski, to to jest jeszcze pewnie jest jeszcze inny kontekst, tak?

**Damian Kaminski** 59:52  
Znaczy nie, no to jest to, że dodajesz pole techniczne. Dodatkowe eksportu jest z tym polem, potem po imporcie masz jakąś regułę automatyczną, że jeśli polę Odnośnik jest puste, bo go po prostu nie wiem, założenia powinni czyścić, a po latach jest wypełnione, to wypełni Odnośnik wartością pola technicznego, no.

**Lukasz Bott** 59:54  
Tak no.

**Piotr Buczkowski** 1:00:06  
Halo.  
Ale dlaczego? Ale Dlaczego nie eksportują tego excela i wczytaj excela?

**Damian Kaminski** 1:00:12  
No to trzeba pogadać z klientem, żeby.

**Piotr Buczkowski** 1:00:15  
Żeby tego nie robił.

**Damian Kaminski** 1:00:16  
No.  
No wiesz, siła, siła przyzwyczajeń to tak jak z tymi polami wymaganymi nie dobra słuchajcie, bo mi się zaczęło spotkanie kończymy, zostawiam to Łukasz u ciebie i tyle.

**Lukasz Bott** 1:00:28  
Nie no dobra, wiesz co nie jest, to niech to.

**Damian Kaminski** 1:00:34  
Dobra.  
To miłego dnia. Do zobaczenia po południu, jeśli jeśli przychodzicie.

zatrzymano transkrypcję
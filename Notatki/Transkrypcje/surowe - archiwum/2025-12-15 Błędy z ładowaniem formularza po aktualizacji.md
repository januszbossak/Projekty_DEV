Wątek z Teams

Przejdź do kanału

- Tomasz Kalinowski
    
    1.12 11:40
    
    ## [AgroUbezpieczenia] Błędy z ładowaniem formularza po aktualizacji
    
    Duty developer team
    
    Klient onpremise:
    
    Wersja przed aktualizacją: 250630.87 (lub 104), Wersja po aktualizacji 250630.132. Wersja która jest teraz: 250331.136.
    
    Baza została odtworzona z backupu, więc obecnie jest w wersji starszej (prawdopodobnie wersja bazy jest zgodna z wersją przed aktualizacją). W eventviewer nic nie ma. Działało na wersji przed aktualizacją. Po aktu się zjebało, nie wiem dlaczego. Aktualizacja była robiona zgodnie z przyjętym standardem, pliki nie miały atrybutu "blocked".
    
    Widok webapp:
    
    ![obraz](blob:https://teams.microsoft.com/3bdecbef-d429-4082-a30c-579ee8e16dac "obraz")
    
    Do zgłoszenia załącze logi z bazy bo niestety jest nawet problem załadować zakładki systemowe.
    

- Janusz Bossak
    
    1.12 11:43
    
    Baza została odtworzona z backupu, - czyli jaka wersja bazy teraz jest, dla której wersji AMODIT?
    

- Tomasz Kalinowski
    
    1.12 11:43
    
    gdzie to sprawdzę?
    

- Janusz Bossak
    
    1.12 11:44
    
    data backupu? z kiedy był i jaka była wtedy wersja AMODIT
    

- Lukasz Bott
    
    1.12 11:44
    
    aktualizowałeś bazę za pomocą AMODITDatabaseAdmin przed aktualizacją aplikacji?
    

- jeśli masz dostęp do bazy danych, to w tabeli parameters powinien być jeden z pierwszych parametrów dotyczący wersji bazy danych
    

- Tomasz Kalinowski
    
    1.12 11:46
    
    ![obraz](blob:https://teams.microsoft.com/61a8f671-270f-4c58-99a6-3c733345ef8c "obraz")
    

- napisałem że aktualizacja przebiegała zgodnie z naszymi standardami
    

- Tomasz Kalinowski
    
    1.12 11:47
    
    nawet zrobiłem wirtualkę od 0, wrzuciłem 250630.132, z bazą zaktualizowaną do tej wersji i był ten sam błąd
    

- backup zrobiony 28.11, ale zawiera dane 27.11 ponieważ jest robiony późnym wieczorem automatycznie
    

- Tomasz Kalinowski
    
    1.12 12:06
    
    ![obraz](blob:https://teams.microsoft.com/c27f0e20-7dfb-4efe-b6b8-baa0712a6c25 "obraz")
    

- Lukasz Bott
    
    1.12 12:11
    
    Tomasz
    
    , wyciągnij jeszcze z tabeli systemlog te błędy, które się pojawiły.
    

- Tomasz Kalinowski
    
    1.12 12:39
    
    prosze
    
    ![](blob:https://teams.microsoft.com/b3978913-3366-4ee3-b6eb-b4347beb9715)
    
    agro-ajax.txt
    
    ![](blob:https://teams.microsoft.com/99d20f28-5ac3-49fe-87f9-f95c27706e25)
    
    agro-newtonsoft-utmQuery.txt
    
    ![](blob:https://teams.microsoft.com/393a4988-9051-453a-8ca1-d478a4916739)
    
    agro-newtonsoft-items.txt
    
    ![👍](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/yes/default/50_f.png?v=v70)
    
    1 reakcja Lubię to.
    

- Lukasz Bott
    
    1.12 12:44
    
    wygląda to bardziej na błędy w samej aplikacji niż w bazie danych, niemniej zgłaszam to na wewnętrzny kanał DEV, aby się ktoś temu przyjrzał
    

- Mariusz Piotrzkowski
    
    1.12 12:47
    
    Możesz przetestować w trybie incognito albo na przeglądarce, która nigdy nie odpalała tego jeszcze?
    

- Tomasz Kalinowski
    
    1.12 12:50
    
    co ciekawe konto na którym uruchamia się pula i webapp, dla folderów amodit prod i test ma uprawnienia full-control
    

- Mariusz
    
     
    
    Piotrzkowski
    
     gdyby to było takie proste to nie zawracałbym wam głowy, ale proszę,
    
    ![obraz](blob:https://teams.microsoft.com/ae66ab2b-9d05-42e2-93a3-30d834f4403d "obraz")
    

- Mariusz Piotrzkowski
    
    1.12 12:55
    
    dzięki, chciałem tylko coś wykluczyć
    

- Janusz Bossak
    
    1.12 12:55
    
    Tomasz
    
     
    
    Kalinowski
    
     a czy możesz wrócić do poprzedniej wersji aplikacji pasujacej do daty z backupu?
    
    czy wtedy AMODIT działa?
    

- Mariusz Piotrzkowski
    
    1.12 13:00
    
    Tomasz
    
     
    
    Kalinowski
    
     możemy się połączyć w wolnej chwili? Mam kilka pomysłów, które chciałbym przetestować. 
    

- najbardziej mnie dziwi, że odpala się .aspx a nie react
    

- ustawienia systemowe przez przeglądarkę działają?
    

- Tomasz Kalinowski
    
    1.12 13:02
    
    Janusz
    
     
    
    Bossak
    
     nie działa, bo wróciłem do marcowej, która powinna działać, a nie działa. Wcześniej (w sensie w pt, cofałem po aktualizacji do wcześniejszych ale nie pomogło)
    

- Janusz Bossak
    
    1.12 13:02
    
    Tomasz
    
     
    
    Kalinowski
    
     zanim cokolwiek zrobicie to cofnijcie aktualizacje do takiej ktora dzialala
    
    i trzeba ja zrobic ponownie
    

- Mariusz Piotrzkowski
    
    1.12 13:02
    
    Jeżeli tak to spróbuj zmienić:
    
    ![obraz](blob:https://teams.microsoft.com/4e91dc3e-7b43-4662-aee4-ad36f7a0244d "obraz")
    

- Janusz Bossak
    
    1.12 13:02
    
    jak to? nie masz backupu aby po nieudanej aktualizacji wrócić do pprzedniej?
    

- Janusz Bossak
    
    1.12 13:09
    
    Piotr
    
     
    
    Buczkowski
    
     tutaj
    

- Piotr Buczkowski
    
    1.12 13:11
    
    Utmquery - co to za pole?
    

- Nie ma sensu przywracać bazy, co najwyżej przywrócić starą wersję Amodit
    

- Tomasz Kalinowski
    
    1.12 13:13
    
    Janusz ale co takim działaniem chcesz potwierdzić? 
    
    ![obraz](blob:https://teams.microsoft.com/59168de4-f56a-4cdf-984f-7c780d742f06 "obraz")
    
    dać na react?
    

- Piotr Buczkowski
    
    1.12 13:13
    
    Mariusz Piotrzkowski
    
     sprawdzisz kiedy jest wypełniane to utmquery w gettopmenucontent?
    

- Mariusz Piotrzkowski
    
    1.12 13:14
    
    ![obraz](blob:https://teams.microsoft.com/91fdad36-0b0d-4a80-9478-6f518b61de4d "obraz")
    

- Tomasz Kalinowski
    
    1.12 13:14
    
    Czy winą może być złe ustawienie strefy czasowej?
    

- ![obraz](blob:https://teams.microsoft.com/ac445d7e-a80a-45ec-b825-efd1f1c039f8 "obraz")
    

- Piotr Buczkowski
    
    1.12 13:40
    
    wygląda na to, że z jakiś powodów źle działa przypisanie do property w JObject
    

- obydwa błędy to pierwsze przypisanie do tego obiektu - odpowiednio w caselist i usercontroler
    

- Piotr Buczkowski
    
    1.12 13:48
    
    może źle się przegrała biblioteka Newtonsoft,JSON?
    

- Mariusz Piotrzkowski
    
    1.12 13:50
    
    sprawdzałem, wygląda dobrze
    

- ten sam rozmiar co na moim środowisku
    

- Piotr Buczkowski
    
    1.12 13:51
    
    to nie mam pojęcia o co chodzi
    

- Mariusz Piotrzkowski
    
    1.12 13:51
    
    ![obraz](blob:https://teams.microsoft.com/47351801-45a5-4c0b-ae7e-c412813e8848 "obraz")
    

- nie miał tylko tych dwóch plików
    

- ale to raczej nie powinno być potrzebne? w marcowej też nie miał i tam działało
    

- Piotr Buczkowski
    
    1.12 13:51
    
    nawet nie wie co to jest?
    

- Mariusz Piotrzkowski
    
    1.12 13:52
    
    ![obraz](blob:https://teams.microsoft.com/071afb5e-08eb-46ba-8418-e89370813b96 "obraz")
    

- ogólnie na środowisku, które mi pokazywał co chwilę waliło komunikatami o zabezpieczeniach, tak jakby podnieśli politykę bezpieczeństwa na maksa w defenderze
    

- i bardzo wolno ten serwer chodził
    

- może rzeczywiście klient coś namieszał
    

- Mariusz Piotrzkowski
    
    1.12 13:54
    
    Tomasz
    
     
    
    Kalinowski
    
     próbowaliście po prostu serwer ponownie uruchomić? mam na myśli restart całego systemu 
    

- Tomasz Kalinowski
    
    1.12 13:55
    
    tak
    

- Piotr Buczkowski
    
    1.12 13:55
    
    a czy newtonsoft jest w odpowiedniej wersji?
    

- i czy na pewno ten plik nie jest blocked?
    

- jaka to wersja Windows
    

- Tomasz Kalinowski
    
    1.12 14:02
    
    ![obraz](blob:https://teams.microsoft.com/fd4d763f-930e-4b4a-b54a-4e1e6b00afee "obraz")
    

- Piotr
    
     
    
    Buczkowski
    
     
    
    ![obraz](blob:https://teams.microsoft.com/f6640cc8-1b52-45ee-bc65-cf4484f6a9ff "obraz")
    

- Piotr Buczkowski
    
    1.12 14:03
    
    sprawdźcie jeszcze wersję newtonsoft.dll - jeżeli jest zgodna z paczką to więcej na razie nie wymyśle
    

- przywróćcie starą wersję AMODIT
    

- jeżeli nic nie pomoże
    

- Tomasz Kalinowski
    
    1.12 14:05
    
    ![obraz](blob:https://teams.microsoft.com/32528bb3-3a75-4929-b6d1-f957e8d0e06b "obraz")
    

- Mariusz Piotrzkowski
    
    1.12 14:05
    
    ![obraz](blob:https://teams.microsoft.com/d1b5c3ef-291a-40e5-be7c-1f45434cb824 "obraz")
    

- taka jest najnowsza jaką mamy na 250630.mysql.amodit.local
    

- Tomasz Kalinowski
    
    1.12 14:05
    
    a jak ta co działała, teraz nie zadziała?
    

- Mariusz Piotrzkowski
    
    1.12 14:06
    
    może spróbuj dodać katalog amodit do wyjątków defendera - dla testu, TYMCZASOWO
    

- Tomasz Kalinowski
    
    1.12 14:07
    
    klient twierdzi że defendera wyłączyli
    

- Piotr Buczkowski
    
    1.12 14:07
    
    czy w event viewer sprawdzaliście w Application i AMODWebApp?
    

- Tomasz Kalinowski
    
    1.12 14:08
    
    Piotrek, tak, ale nic nie wskazywało w EV na coś konkretnego
    

- Tomasz Kalinowski
    
    1.12 14:18
    
    wróciłem na wersję 104 gdzie działało, przez chwile widziałem wstążkę z panelem administracyjnym, potem to samo:
    
    ![obraz](blob:https://teams.microsoft.com/150fe98d-1894-4d31-926c-a76f831949b3 "obraz")
    

- Piotr Buczkowski
    
    1.12 14:40
    
    Czy w logach te same błędy?
    

- Co jest w tym event viewer?
    

- Mariusz Piotrzkowski
    
    1.12 14:54
    
    Zaproponowałem Tomaszowi, aby zrobić obok drugiego amodita na osobnej bazie i od zera, kopiować configi, aby sprawdzić gdzie się wywali. 
    
    Piotr
    
     
    
    Buczkowski
    
     myślisz, że to dobry pomysł?
    

- wykluczylibyśmy w taki sposób np. problemy z systemem, iis-em itp
    

- Piotr Buczkowski
    
    1.12 15:19
    
    Spróbujcie tak zrobic
    

- Może być nawet do tej samej bazy ale z nowej witryny
    

- Tomasz Kalinowski
    
    1.12 16:44
    
    Zrobiłem nową instancję, z czystą bazą, konfig webconfig.safe, zrobiony https, port 2443. Stworzyłem usera, loguję.
    
    ![obraz](blob:https://teams.microsoft.com/ec4e3fec-86b5-4d82-93fd-74bc968d42b2 "obraz")
    
    Po zalogowaniu:
    
    ![obraz](blob:https://teams.microsoft.com/bcb0ab0c-f61e-421a-bff8-4ea0e6a2c36c "obraz")
    

- Piotrek, udało nam się zalogować do forms/parameters.aspx
    
    tam mamy atrybut caselist - reactcaselist a przekierowuje na forms/macaselist.aspx po kliknięciu na logo amodit
    

- w bazie mamy:
    
    ![obraz](blob:https://teams.microsoft.com/cd14d668-2866-40c4-891c-7ae33d97c3a3 "obraz")
    

- Piotr
    
     
    
    Buczkowski
    
    ![obraz](blob:https://teams.microsoft.com/b8a24592-52e7-42bf-938c-f0cb728aec49 "obraz")
    

- wychodzi na to że tylko caselist się wywala:
    
    ![obraz](blob:https://teams.microsoft.com/7e0a4bb0-2afb-4916-9ace-244d2b5b9ac4 "obraz")
    

- Piotr Buczkowski
    
    1.12 16:53
    
    Błąd jest w kontrolerze prz wypełnianiu jobject
    

- Taki mechanizm jest wykorzystywany w wielu miejscach i nie da się tego zmienic
    

- Mariusz Piotrzkowski
    
    2.12 12:58
    
    Problem został rozwiązany. Okazało się, że przekompilowane / zcachowane pliki dll w GUC były corrupted i mechanizm tego nie wykrył. Usunęliśmy Newtonsoft* z C:\Windows\assembly\GAC_64, po czym ponownie uruchomiliśmy wszystko i zaczęło działać. Potem napiszę do tego artykuł jak znajdować i wykrywać takie problemy (użyliśmy resmon.exe do znalezienia gdzie znajdował się aktywnie używany plik .dll). 
    
    ![🎉](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/1f389_partypopper/default/50_f.png?v=v12)
    
    Liczba reakcji Strzelający pojemnik z serpentyną: 2.
    
    2
    
    ![❤️](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/heart/default/50_f.png?v=v34)
    
    1 reakcja Serce.
    
    ![👍](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/yes/default/50_f.png?v=v70)
    
    1 reakcja Lubię to.
    

- Daniel Reszka
    
    2.12 14:30
    
    Ale to są pliki serwerowe czy Amoditowe?
    
    Ogólnie to dziwne, jeśli faktycznie stawiali serwer od 0, że to się tam zadziało ponownie...
    

- Tomasz Kalinowski
    
    2.12 14:34
    
    Wyszło dodatkowo że postawienie aktywnej dodatkowej witryny psuje ustawienia newtonsoftowe (do działającej produkcji dodano instancje test) i pojawia się ten sam błąd. Żeby znowu mi to zadziałało musiałem usunąć pliki z lokalizacji c:\windows\assembly\gac_msil\newtonsoft.json\ Będziemy z Mariuszem sprawdzać zachowanie witryn po restarcie w trybie (1 lub 2), (1 i 2), przy wrzuceniu kolejnej witryny na serwer.
    

- Piotr Buczkowski
    
    2.12 14:35
    
    Nie pamiętam kiedy musiałem coś ręcznie usuwać z GAC, chyba to było jeszcze na Windows 2003
    

- Ta dll to część Amodita, którą Windows sobie kompiluje i skompilowaną kopiuje do GAC. Tak jak napisałem - dawno nie spotkałem się z problemem z tym mechanizmem.
    

- Mariusz Piotrzkowski
    
    2.12 14:38
    
    może po prostu jest uszkodzony mechanizm .net w systemie?
    

- może jakiś `dism /online /cleanup-image /restorehealth` oraz `sfc /scannow` by pomogło?
    

- Tomasz Kalinowski
    
    2.12 14:39
    
    Piotrek zauważyłem że u klienta mocno agresywnie pracuje windows defender. PRzy nowej instancji blokował aplikacje, it klienta musiało wyłączyć AV na jakiś czas. Może on albo jakieś zmienione polityki wpływają na działanie środowiska w ten sposób że podmienianie plików powoduje problem z ładowaniem widoków witryny.
    

- Mariusz Piotrzkowski
    
    2.12 14:43
    
    Może być, że po prostu defender blokuje kompilację
    

- bo kompilacja to taki dosyć "wrażliwy" proces w kontekście antywirusów
    

- Daniel Reszka
    
    2.12 14:46
    
    da się dodać jakieś wyjątki na zaporze pod to? (aby to ignorował - czy to zbyt ogólne i nie tylko Amodit z tego korzysta?)
    

- Mariusz Piotrzkowski
    
    2.12 14:48
    
    zapora raczej tutaj wiele nie da - to nie problem z połączeniem / siecią
    

- a wyjątki w windows defender by można, tylko nie wiadomo co wykluczyć dokładnie
    

- Tomasz Kalinowski
    
    2.12 14:49
    
    nie wiem jakie jest severity / protection level po stronie managementu, jeśli jest wysokie to może blokować wszystko co w jakikolwiek sposób ma wpływ na integralność systemu. Przy asynchronous service pojawiał się komunikat "malicious software"
    

- Mariusz Piotrzkowski
    
    2.12 14:49
    
    bo nie możemy wszystkiego tak po prostu wykluczyć
    

- Tomasz Kalinowski
    
    2.12 14:52
    
    Daniel
    
     
    
    Reszka
    
     takie coś miałem:
    
    ![obraz](blob:https://teams.microsoft.com/ab80a4aa-75c5-49b4-a65c-f0586b266c89 "obraz")
    
    ![obraz](blob:https://teams.microsoft.com/4e3ce246-be5e-4147-88e1-6c6949f5b09e "obraz")
    

- Daniel Reszka
    
    2.12 14:54
    
    to moim zdaniem na serwerze błędy w takim razie Defendera
    

- Mariusz Piotrzkowski
    
    2.12 14:54
    
    czyli ich wina
    

- Piotr
    
     
    
    Buczkowski
    
     jak bardzo ważne jest wskazanie "<bindingRedirect oldVersion="0.0.0.0-12.0.0.0" newVersion="12.0.0.0" />" w web.config?
    

- aktualnie newtonsoft ma chyba 13.0.3.0 a my mamy w web config cały czas 12.0.0.0
    

- ale przy zmianie tego błąd nie ustępował (próbowaliśmy)
    

- Tomasz Kalinowski
    
    2.12 14:56
    
    ale potem to wyłączyli, błąd był mimo wszystko, w takiej sytuacji trudno stwierdzić czy z poziomu serwera na którym skonfigurowany jest defender dla całej organizacji, czy tam nie było jakiś logów związanych z webapp
    

- Mariusz Piotrzkowski
    
    2.12 14:58
    
    sam fakt, że wyłączyli po czasie wiele nie znaczy
    

- jeżeli się da opracować repro steps to trzeba sprawdzić z i bez defendera
    
    ![👍](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/yes/default/50_f.png?v=v70)
    
    1 reakcja Lubię to.
    

- Piotr Buczkowski
    
    2.12 15:18
    
    Co do wpisu w web.config to ważne aby w new nie była nowsza wersja niż jest
    

- Nie pamiętam co się dzieje gdy jest starsza
    

- Mariusz Piotrzkowski
    
    2.12 15:18
    
    a co jeśli w systemie byłaby jakaś inna aplikacja, która ma newtonsofta 12, a w amodicie jest dll z wersją 13? 
    

- wtedy by chyba z GACa brał tą przekompilowaną z innej apki?
    

- Piotr Buczkowski
    
    2.12 16:09
    
    W Gac może być wiele wersji tej samej biblioteki
    

- Tomasz Kalinowski
    
    czwartek 15:53
    
    Mariusz
    
     
    
    Piotrzkowski
    
    , 
    
    Piotr
    
     
    
    Buczkowski
    
    Mam ten sam problem w PCBC
    
    ![obraz](blob:https://teams.microsoft.com/5b189141-4be4-49df-89e5-49fc0cd0671b "obraz")
    
    1. Amodit nie był aktualizowany
    2. Wgrywana była nowa wersja konektora (tam plików json nie ma)
    3. Był aktualizowany klient Symfonia F-K do 2026
    
    Może któraś z tych opcji wpływa jakoś na amodita, wywalając pliki newtonsoftowe?
    
    dw 
    
    Daniel
    
     
    
    Reszka
    

- Piotr Buczkowski
    
    czwartek 15:55
    
    ale co jest w logu?
    

- Tomasz Kalinowski
    
    czwartek 15:57
    
    ![obraz](blob:https://teams.microsoft.com/2b3f7849-f080-4315-91d8-e0c25b9c8603 "obraz")
    

- Piotr Buczkowski
    
    czwartek 15:59
    
    jak wtedy doszliście, że problem jest w GAC?
    

- Daniel Reszka
    
    czwartek 16:00
    
    tu Mariusz chyba pomagał w tej analizie
    

- Tomasz Kalinowski
    
    czwartek 16:00
    
    Mariusz
    
     
    
    Piotrzkowski
    
     znalazł w resource monitor, zakładka procesor usługę amodit_asynchronous - gdzie wskazywało na ścieżki biblioteki newtonsoftowej, mariusz dobrze mówię?
    

- Ta wiadomość została usunięta.
    

- Tomasz Kalinowski
    
    czwartek 16:09
    
    ![obraz](blob:https://teams.microsoft.com/0b550b77-9900-46c8-875f-f17d697cea79 "obraz")
    

- usunąłem pliki i teraz jest ok, oba przypadki były wykonywane przy wykorzystaniu amodit 250630. W PCBC jest poprawka .99. Może coś jest w plikach amoditowych co powoduje taki impact?
    

- Daniel Reszka
    
    czwartek 16:13
    
    Piotr
    
     
    
    Buczkowski
    
     musimy tutaj ustalić co i czemu tak się dzieje, aby uniknąć kolejnych takich scenariuszy u pozostałych klientów onprem - najpierw ustalmy czy wina jest po aktualizacji konektora czy Symfonii.
    
    Jesteś w stanie Tomek to jakoś stwierdzić?
    

- Piotr Buczkowski
    
    czwartek 16:14
    
    tam są dwie usługi?
    

- w jakich wersjach?
    

- Tomasz Kalinowski
    
    czwartek 16:14
    
    Tak Piotrek
    

- obie w wersji czerwcowej
    

- w konektorze nic specjalnego nie ma:
    
    ![obraz](blob:https://teams.microsoft.com/684298f8-e3d4-44f7-824f-4a7f9aff1e5b "obraz")
    

- Tomasz Kalinowski
    
    czwartek 16:24
    
    jeśli chodzi o symfo, to czekam na więcej danych
    

- Tomasz Kalinowski
    
    czwartek 16:38
    
    usunięcie plików newtonsofta chyba nie pomaga bo znowu się popsuło ![😕](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/confused/default/60_anim_f.png?v=v18)
    

- Piotr
    
     
    
    Buczkowski
    
     teraz jest tak, restartowałem serwer, to jeszcze jak nie działa, wyślę zaraz update po usunięciu plików
    
    ![obraz](blob:https://teams.microsoft.com/b59a06a5-c802-4398-895f-87566220cad0 "obraz")
    

- Piotr Buczkowski
    
    czwartek 16:42
    
    czy są jakieś wpisy dotyczące Newtonsoft w web.config?
    

- Tomasz Kalinowski
    
    czwartek 16:44
    
    ![obraz](blob:https://teams.microsoft.com/5ec00192-ce80-4c5b-94e1-587f795216c3 "obraz")
    

- xape twierdzi że nowa wersja symfonii może mieć wpływ na działanie webapp - na razie to nic potwierdzonego
    

- Piotr Buczkowski
    
    czwartek 16:45
    
    usuńcie wpis <dependentAssembly>
    

- Tomasz Kalinowski
    
    czwartek 16:45
    
    w sensie całość? od rozpoczęcia do zakończenia?
    

- Piotr Buczkowski
    
    czwartek 16:45
    
    czy to na pewno wpis z web.config z aplikacji webowej?
    

- Tomasz Kalinowski
    
    czwartek 16:45
    
    na 100%
    

- Piotr Buczkowski
    
    czwartek 16:46
    
          <dependentAssembly>  
    <assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30ad4fe6b2a6aeed" culture="neutral" />  
    <bindingRedirect oldVersion="0.0.0.0-13.0.0.0" newVersion="13.0.0.0" />  
    </dependentAssembly>
    

- tak jest u nas
    

- ale u nas nie ma <applicationSettings> widocznych na dole
    

- Tomasz Kalinowski
    
    czwartek 16:47
    
    a to tak jak zmieniał Mariusz jak to analizowaliśmy, potem wrócił do 12.0
    

- najpierw sprawdzaliśmy .NET
    

- Piotr Buczkowski
    
    czwartek 16:47
    
    usuńcie ten wpis
    

- czy w Agro też jest Symfonia?
    

- Tomasz Kalinowski
    
    czwartek 16:48
    
    taak
    

- Piotr Buczkowski
    
    czwartek 16:48
    
    co jest w tym applicationSettings?
    

- Tomasz Kalinowski
    
    czwartek 16:49
    
    ![obraz](blob:https://teams.microsoft.com/e8fec82e-5164-4b6d-9468-23f45db3832e "obraz")
    

- Piotrek usuwam wszystko co jest w dependentassembly
    

- ![obraz](blob:https://teams.microsoft.com/f32ba963-e09b-45e9-b401-2b34f7c24cec "obraz")
    
    Tu nie wpisywać 13.0.0 tak jak to u was jest?
    

- Piotr Buczkowski
    
    czwartek 16:52
    
    usuń też applicationSettings
    

- jest błąd w pliku wzorcowym - nie powinno tego być
    

- Tomasz Kalinowski
    
    czwartek 16:53
    
    git?
    

- Piotrek, teraz mam taki wpis w resource:
    
    ![obraz](blob:https://teams.microsoft.com/87dad71f-fe00-40f3-a59e-94d144ce4a0c "obraz")
    

- Piotr Buczkowski
    
    czwartek 16:53
    
    czy działa?
    

- Tomasz Kalinowski
    
    czwartek 16:55
    
    tak, ale żeby się upewnić potrzebuję zrestartować serwer
    

- Piotr Buczkowski
    
    czwartek 16:55
    
    ok
    

- Tomasz Kalinowski
    
    czwartek 16:59
    
    tak, działa, rozumiem że te dwie rzeczy w jakiś sposób psują amodit?
    

- Piotr Buczkowski
    
    czwartek 16:59
    
    tylko to odwołanie do wersji 12 Newtonsoft.Json
    
    ![👍](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/yes/default/50_f.png?v=v70)
    
    1 reakcja Lubię to.
    

- wartość z applicationSettings jest po prostu niepotrzebna
    

- właśnie poprawiam pliki wzorcowe web.config aby tego nie było
    
    ![❤️](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/heart/default/50_f.png?v=v34)
    
    1 reakcja Serce.
    

- najlepiej poprawić to u innych klientów, gdzie były wgrywany plik na podstawie web.config.safe.txt
    

- Tomasz Kalinowski
    
    czwartek 17:01
    
    Czy jakbym wskazał wersję 13.0 to czy to by coś zmieniło?
    

- Piotr Buczkowski
    
    czwartek 17:02
    
    ![obraz](blob:https://teams.microsoft.com/07b85e8a-3eb7-496a-82c7-62e6a4128123 "obraz")
    

- nie ma potrzeby wskazywania wersji
    

- ma w swoim katalogu plik newtonsoft.json.dll i z niego powinien korzystać a nie szukać podanej wersji w GAC
    

- Tomasz Kalinowski
    
    czwartek 17:04
    
    okej, dzięki za wyjaśnienie
    

- Daniel Reszka
    
    czwartek 17:33
    
    "najlepiej poprawić to u innych klientów, gdzie były wgrywany plik na podstawie web.config.safe.txt"
    
    czy przyszła aktualizacja to poprawi (w sensie check config z DBAdmina)?
    
    czy trzeba ręcznie wszędzie poprawiać u klientów?
    

- Piotr Buczkowski
    
    piątek 08:59
    
    trzeba ręcznie poprawić
    

- ale w sumie można dodać sprawdzanie do check config - nie pomyślałem, że ktoś z tego korzysta
    

- Daniel Reszka
    
    piątek 09:13
    
    Przy każdej aktualizacji tego używamy na serwisie
    

- Tomasz Kalinowski
    
    piątek 09:18
    
    Piotr
    
     
    
    Buczkowski
    
     jednak jest to samo, już nie wiem o co tu chodzi... ![🤔](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/think/default/60_anim_f.png?v=v21)![🙁](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/sad/default/60_anim_f.png?v=v31)
    
    ![obraz](blob:https://teams.microsoft.com/2ec7652c-e597-4f71-bec4-3c49e46c2664 "obraz")
    

- Tomasz Kalinowski
    
    piątek 09:19
    
    cały czas wywala błędy newtonsoftu
    
    ![obraz](blob:https://teams.microsoft.com/983a1157-5c6e-4b43-8755-dbe4b51a96cd "obraz")
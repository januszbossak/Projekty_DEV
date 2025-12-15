**Data spotkania:** 1-2 grudnia 2025 - część 1

---

**Tomasz Kalinowski:** [[AgroUbezpieczenia]] Błędy z ładowaniem formularza po aktualizacji. Duty developer team. Klient onpremise. Wersja przed aktualizacją: 250630.87 (lub 104), wersja po aktualizacji 250630.132. Wersja która jest teraz: 250331.136. Baza została odtworzona z backupu, więc obecnie jest w wersji starszej (prawdopodobnie wersja bazy jest zgodna z wersją przed aktualizacją). W eventviewer nic nie ma. Działało na wersji przed aktualizacją. Po aktualizacji się zepsuło, nie wiem dlaczego. Aktualizacja była robiona zgodnie z przyjętym standardem, pliki nie miały atrybutu "blocked". Do zgłoszenia załączę logi z bazy, bo niestety jest nawet problem załadować zakładki systemowe.

**Janusz Bossak:** Baza została odtworzona z backupu – czyli jaka wersja bazy teraz jest, dla której wersji AMODIT?

**Tomasz Kalinowski:** Gdzie to sprawdzę?

**Janusz Bossak:** Data backupu? Z kiedy był i jaka była wtedy wersja AMODIT?

**Lukasz Bott:** Aktualizowałeś bazę za pomocą AMODITDatabaseAdmin przed aktualizacją aplikacji? Jeśli masz dostęp do bazy danych, to w tabeli parameters powinien być jeden z pierwszych parametrów dotyczący wersji bazy danych.

**Tomasz Kalinowski:** Napisałem, że aktualizacja przebiegała zgodnie z naszymi standardami. Nawet zrobiłem wirtualkę od zera, wrzuciłem 250630.132, z bazą zaktualizowaną do tej wersji i był ten sam błąd. Backup zrobiony 28.11, ale zawiera dane 27.11, ponieważ jest robiony późnym wieczorem automatycznie.

**Lukasz Bott:** Tomasz, wyciągnij jeszcze z tabeli systemlog te błędy, które się pojawiły.

**Tomasz Kalinowski:** Proszę. [Załączniki: agro-ajax.txt, agro-newtonsoft-utmQuery.txt, agro-newtonsoft-items.txt]

**Lukasz Bott:** Wygląda to bardziej na błędy w samej aplikacji niż w bazie danych, niemniej zgłaszam to na wewnętrzny kanał DEV, aby się ktoś temu przyjrzał.

**Mariusz Piotrzkowski:** Możesz przetestować w trybie incognito albo na przeglądarce, która nigdy nie odpalała tego jeszcze?

**Tomasz Kalinowski:** Co ciekawe, konto na którym uruchamia się pula i webapp, dla folderów AMODIT prod i test ma uprawnienia full-control.

**Mariusz Piotrzkowski:** Gdyby to było takie proste, to nie zawracałbym wam głowy, ale proszę. Ustawienia systemowe przez przeglądarkę działają?

**Mariusz Piotrzkowski:** Dzięki, chciałem tylko coś wykluczyć. Najbardziej mnie dziwi, że odpala się .aspx a nie React.

**Janusz Bossak:** Tomasz Kalinowski, a czy możesz wrócić do poprzedniej wersji aplikacji pasującej do daty z backupu? Czy wtedy AMODIT działa?

**Mariusz Piotrzkowski:** Tomasz Kalinowski, możemy się połączyć w wolnej chwili? Mam kilka pomysłów, które chciałbym przetestować.

**Tomasz Kalinowski:** Janusz Bossak, nie działa, bo wróciłem do marcowej, która powinna działać, a nie działa. Wcześniej (w sensie w piątek, cofałem po aktualizacji do wcześniejszych, ale nie pomogło).

**Janusz Bossak:** Tomasz Kalinowski, zanim cokolwiek zrobicie, to cofnijcie aktualizację do takiej która działała i trzeba ją zrobić ponownie. Jak to? Nie masz backupu, aby po nieudanej aktualizacji wrócić do poprzedniej?

**Mariusz Piotrzkowski:** Jeżeli tak, to spróbuj zmienić [ustawienie].

**Janusz Bossak:** Piotr Buczkowski, tutaj.

**Piotr Buczkowski:** UtmQuery – co to za pole? Nie ma sensu przywracać bazy, co najwyżej przywrócić starą wersję AMODIT.

**Tomasz Kalinowski:** Janusz, ale co takim działaniem chcesz potwierdzić? Dać na React?

**Piotr Buczkowski:** Mariusz Piotrzkowski, sprawdzisz kiedy jest wypełniane to utmQuery w gettopmenucontent?

**Mariusz Piotrzkowski:** [Odpowiedź dotycząca utmQuery]

**Tomasz Kalinowski:** Czy winą może być złe ustawienie strefy czasowej?

**Piotr Buczkowski:** Wygląda na to, że z jakiś powodów źle działa przypisanie do property w JObject. Obydwa błędy to pierwsze przypisanie do tego obiektu – odpowiednio w caselist i usercontroler.

**Piotr Buczkowski:** Może źle się przegrała biblioteka Newtonsoft.JSON?

**Mariusz Piotrzkowski:** Sprawdzałem, wygląda dobrze. Ten sam rozmiar co na moim środowisku.

**Piotr Buczkowski:** To nie mam pojęcia o co chodzi.

**Mariusz Piotrzkowski:** Nie miał tylko tych dwóch plików. Ale to raczej nie powinno być potrzebne? W marcowej też nie miał i tam działało.

**Piotr Buczkowski:** Nawet nie wie co to jest?

**Mariusz Piotrzkowski:** Ogólnie na środowisku, które mi pokazywał, co chwilę waliło komunikatami o zabezpieczeniach, tak jakby podnieśli politykę bezpieczeństwa na maksa w defenderze. I bardzo wolno ten serwer chodził. Może rzeczywiście klient coś namieszał.

**Mariusz Piotrzkowski:** Tomasz Kalinowski, próbowaliście po prostu serwer ponownie uruchomić? Mam na myśli restart całego systemu.

**Tomasz Kalinowski:** Tak.

**Piotr Buczkowski:** A czy Newtonsoft jest w odpowiedniej wersji? I czy na pewno ten plik nie jest blocked? Jaka to wersja Windows?

**Tomasz Kalinowski:** [Zrzut ekranu z informacjami o Windows]

**Piotr Buczkowski:** Sprawdźcie jeszcze wersję newtonsoft.dll – jeżeli jest zgodna z paczką, to więcej na razie nie wymyślę. Przywróćcie starą wersję AMODIT, jeżeli nic nie pomoże.

**Tomasz Kalinowski:** [Zrzut ekranu]

**Mariusz Piotrzkowski:** Taka jest najnowsza jaką mamy na 250630.mysql.amodit.local.

**Tomasz Kalinowski:** A jak ta co działała, teraz nie zadziała?

**Mariusz Piotrzkowski:** Może spróbuj dodać katalog AMODIT do wyjątków defendera – dla testu, tymczasowo.

**Tomasz Kalinowski:** Klient twierdzi, że defendera wyłączyli.

**Piotr Buczkowski:** Czy w event viewer sprawdzaliście w Application i AMODWebApp?

**Tomasz Kalinowski:** Piotrek, tak, ale nic nie wskazywało w EV na coś konkretnego.

**Tomasz Kalinowski:** Wróciłem na wersję 104, gdzie działało, przez chwilę widziałem wstążkę z panelem administracyjnym, potem to samo.

**Piotr Buczkowski:** Czy w logach te same błędy? Co jest w tym event viewer?

**Mariusz Piotrzkowski:** Zaproponowałem Tomaszowi, aby zrobić obok drugiego AMODITa na osobnej bazie i od zera, kopiować configi, aby sprawdzić gdzie się wywali. Piotr Buczkowski, myślisz, że to dobry pomysł? Wykluczylibyśmy w taki sposób np. problemy z systemem, IIS-em itp.

**Piotr Buczkowski:** Spróbujcie tak zrobić. Może być nawet do tej samej bazy, ale z nowej witryny.

**Tomasz Kalinowski:** Zrobiłem nową instancję, z czystą bazą, konfig webconfig.safe, zrobiony HTTPS, port 2443. Stworzyłem usera, loguję. Po zalogowaniu: Piotrek, udało nam się zalogować do forms/parameters.aspx. Tam mamy atrybut caselist – reactcaselist, a przekierowuje na forms/macaselist.aspx po kliknięciu na logo AMODIT. W bazie mamy [ustawienie].

**Piotr Buczkowski:** [Zrzut ekranu] Wychodzi na to, że tylko caselist się wywala.

**Piotr Buczkowski:** Błąd jest w kontrolerze przy wypełnianiu JObject. Taki mechanizm jest wykorzystywany w wielu miejscach i nie da się tego zmienić.



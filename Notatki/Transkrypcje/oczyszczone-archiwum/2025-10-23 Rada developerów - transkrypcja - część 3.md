**Data spotkania:** 23 października 2025, 08:02 - część 3

---

**Damian Kaminski:** Czy jakiś inny jeszcze tu jest potrzebny, czy – czy reszta?

**Anna Skupinska:** A, czy – tak, bo trzeba zrobić coś takiego, że on – trzeba uruchomić raport React, wziąć z tego raportu ID spraw i później użyć tych ID spraw, żeby uruchomić kod, żeby użyć szablonu, żeby generować ten plik, a później przesłać ten plik z powrotem. Do tego trzeba napisać taki bukiet.

**Damian Kaminski:** Mhm. To znaczy, no – ID spraw, jak rozumiem, w tym wypadku już mamy ten element, tak? Tylko trzeba to albo zreusować, albo...

**Anna Skupinska:** A, trzeba – w sumie faktycznie, masz rację. Przepraszam, faktycznie, faktycznie masz rację. To nie trzeba jeszcze raz odpalać tego, że on zostanie przesłany. Co – w takim razie jeszcze mniej to wymaga pracy.

**Damian Kaminski:** No właśnie. Dobra, zróbmy na razie tego PBI. Ja, czekając, ja spojrzę na kalendarz. Dobra – opisz na razie ten element, jeśli możesz – jakbyś to widziała w kontekście tej definicji typu rozszerzenia. Ja postaram się po prostu złapać z Januszem albo z Kamilem, żeby to zatwierdzić. Chwilę jeszcze to zajmie. Nie wiem, czy dzisiaj się uda, mówiąc szczerze. Jak nie dzisiaj, to jutro po Daily.

**Anna Skupinska:** Rozumiem.

**Damian Kaminski:** Bo Kamil do trzynastej jest niedostępny. Jak po trzynastej się z nim złapię, to – chociaż mi się tu zwolniło – więc po trzynastej ja mam jakoś przestrzeń. No to może wtedy – dobra, to na razie to tak zapakujmy. Zerknijmy jeszcze co jest na... Na razie nie wiem, czy ty coś, Piotrze, masz?

**Piotr Buczkowski:** Nie, nie, bo...

**Damian Kaminski:** Nie masz. Co my tu mamy? Zmianę sposobu, bo... Opis problemu przy imporcie XML. To dalej jest na radzie, ale to już mamy omówione, tak. Odpinamy to. To było twoje.

**Piotr Buczkowski:** Może projekt ma być zrobiony, tak?

**Damian Kaminski:** W sensie – według mnie ustaliliśmy, że to teraz może tak wyglądać, jak zaproponowałeś, a i tak trzeba to obsłużyć w ramach nowego całego zgłoszenia, tak?

**Piotr Buczkowski:** To tak, tak. No tak – zaprojektować chciałbym, oglądać.

**Damian Kaminski:** Dobra, to – to odpinam. W sensie – ty to zaprojektujesz, czy my mamy to zaprojektować?

**Piotr Buczkowski:** No nie, projektujecie, tak.

**Damian Kaminski:** No dobra, to dla siebie na razie. Mamy dalej. Ale nie – czy tutaj to – chyba kto to podpiął pod radę?

**Anna Skupinska:** A, to próbowałam to znaleźć, ale mi się nie udało, więc postanowiłam się zająć tym później. Być może to jest problem. Wydaje mi się, że problem polega na – ciężko było – jeszcze – polega problem, jest coś z LastDate, ale nie dam się tego odtworzyć ani znaleźć. Tak, no muszę, muszę na to po prostu dłużej, żeby to znaleźć. To jest niejasne.

**Damian Kaminski:** Dobra, ale to dotyczy nowych raportów, tak, czy...?

**Anna Skupinska:** Znaczy nie, nie do końca – to dotyczy źródeł systemowych.

**Damian Kaminski:** OK.

**Anna Skupinska:** Systemowych źródeł danych.

**Damian Kaminski:** Dobrze, jeszcze chciałem zobaczyć – było zgłoszenie, które ja robiłem, o które prosił Piotr – i ewentualnie, jeśli tego nie ma, to żeby – jeśli tego nikt nie podjął, to żebyś tym się zajęła. Logowanie SQL. Coś takiego tam było?

**Piotr Buczkowski:** No, chodziło o to, żeby w raportach nowych każdy błąd...

**Damian Kaminski:** Tak, tak, tak.

**Piotr Buczkowski:** Zapytaniu SQL zawierał treść zapytania SQL, tak jak jest w starych, starych raportach.

**Damian Kaminski:** Już zaraz to znajdę, bo to – w taskach to znajdę po swoich. Jej, to...

**Piotr Buczkowski:** Tam jest to – to funkcja, tak – Execute OK, czy jakoś tak – Executed? Która po prostu, jeżeli jest błąd, loguje też pełną zawartość – jest SQL razem z parametrami. GetCommandData, czy jakoś – tam jest taka funkcja, jakoś tak.

**Damian Kaminski:** Można. O, Mateusz. No to – jak Mateusz chyba o tym zapomniał, bo nawet o tym nie wspomniał. Zajmuje się tamto, Aniu. Ja proponuję, że zrób to, co mówiliśmy w kontekście tego – jak, jakbyś to widziała – do tych szablonów. Natomiast zajmij się tym później, w wolnej chwili, bo rozumiem, że SQL Schema masz ogarnięte, tak, już?

**Anna Skupinska:** Tak, to już robiłam. Teraz czeka na – a, to czeka na sprawdzenie. I ten błąd – Basi – to też udało mi się poprawić pomiędzy spotkaniami i...

**Damian Kaminski:** No to super. To to byłoby istotne, bo to właśnie może nam pomóc rozwiązać, co jest przyczyną błędów, tak? Więc przepisałem to do ciebie. To ty możesz się zająć, żebyś miała jakoś właśnie zadania, jeśli wszystko, co aktualnie...

**Anna Skupinska:** Czy wszędzie, gdzie jest jakiś błąd z zapytaniem SQL, on powinien...? A, tylko na raportach – OK. To jest ograniczenie jakieś.

**Damian Kaminski:** No, na nowych raportach.

**Piotr Buczkowski:** Znaczy, nie wiem – jak tylko... W starych, tych funkcjach drukowania – jest SQL, jest takie coś, że zrobiłem tam... Także zawsze, jak jest wykonywany, to jeżeli wystąpił jakiś błąd przy wykonaniu SQL, to razem z błędem jest pełna treść tego zapytania, ale SQL razem z parametrami logowania. Być może w nowych raportach nie przechodzi to tak, bo tam korzystają – korzystacie z tego SQL Builder?

**Anna Skupinska:** Tak, my sami sobie generujemy SQL dla naszych nowych raportów.

**Piotr Buczkowski:** No właśnie, ale też pewnie Executor nie przechodzi przez te funkcje, które ja zrobiłem, tak?

**Anna Skupinska:** A, jak się nazywa ta funkcja od Executor, której używasz do tego?

**Piotr Buczkowski:** Już, już pokazuję.

**Anna Skupinska:** Może to będzie na tyle proste – po prostu jej użycie tej funkcji.

**Piotr Buczkowski:** Ogród, więc... O tutaj. Było dostępne w ekran.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Normalnie to – to wszystkie, wszystkie nasze DB Command, tak? I do przemysłu – to jak? Tutaj jest – no, normalnie to jest...

**Damian Kaminski:** Tylko ja mam taką słabą jakość. A ja – ty dobrze widzisz ten kod?

**Anna Skupinska:** A...

**Damian Kaminski:** Kupa pikseli za...

**Anna Skupinska:** No, czy – to jest trochę rozmyta?

**Damian Kaminski:** No, OK, dobra.

**Piotr Buczkowski:** Może tutaj chodzi o to, żeby ten Command to nie był zwykły Command, tylko to był ten – chyba nasz, tak?

**Anna Skupinska:** Czyli zamiast DB Command użyć AmodDB...?

**Piotr Buczkowski:** Amod DB Command – to wtedy on po prostu przechodzi.

**Anna Skupinska:** A, czy on potrafi wszystkie różne podtypy połączeń obsłużyć? Na przykład ODBC, MySQL, MySQL?

**Piotr Buczkowski:** Znaczy, nie pamiętam, czy ODBC potrafi. Na pewno potrafi MySQL, ale SQL Server – zależności od tego, który mamy, tak.

**Anna Skupinska:** OK, to się zobaczy.

**Piotr Buczkowski:** Może da się? Albo może to tutaj jest – przepraszam. W każdym razie tak, że jest – czyli jest jakikolwiek – może tutaj to nie jest zastosowany – że jest jakikolwiek błąd, to jest takie logowanie.

**Anna Skupinska:** Mhm, dobrze. OK, to zobaczę to.

**Damian Kaminski:** No dobra, to – to...

**Piotr Buczkowski:** No nie, bo to – to albo to, bo tutaj jest trochę chyba i... SQL wyskoczy tutaj, tak. A tutaj jest inny błąd. Możemy skoczyć – OK, chyba tak to jest.

**Anna Skupinska:** Pamiętamy – chyba mamy właśnie te błędy i kilka jeszcze. Tylko wejdę na...

**Piotr Buczkowski:** To było, żeby to w ten sposób, tak – żeby to na przykład było w jednym wpisie.

**Anna Skupinska:** Jak wejdziesz na AmodReportPreview.SQLBuilder, jest funkcja Executor. I ona – ja się orientuję, to my, jeżeli pojawiają się jakiś wyjątek, to my zapisujemy – jest funkcja DatabaseError i ona zapisuje SQL do Error.

**Piotr Buczkowski:** Jakiego rozu?

**Anna Skupinska:** To jest, to jest plik – to jest plik AmodReportPreview.SQLBuilder i funkcja się nazywa DatabaseError.

**Damian Kaminski:** No i co z nim potem dalej robi?

**Piotr Buczkowski:** Nie wiem.

**Anna Skupinska:** On – sposób – wpisać w Solution Explorer. Mam od Report... Preview... Także – życzę – wyskoczy. Amod Report Preview...

**Piotr Buczkowski:** Który – pomysł dużo?

**Anna Skupinska:** To są testy.

**Piotr Buczkowski:** Testów, tak? Poprosiła.

**Anna Skupinska:** O tutaj – SQL Builder. I wyjdę – to, to są chyba ciągle testy.

**Piotr Buczkowski:** Żeby mi się sklepy zaczęły ładować.

**Anna Skupinska:** A, to...

**Piotr Buczkowski:** Dobrze.

**Anna Skupinska:** Znaczy raczej wpisać całą nazwę – AmodReportPreview.SQLBuilder.

**Piotr Buczkowski:** No, tak. Że to jest – to IDbCommand, tak – przechodzi przez... Rider – i tutaj jest...

**Anna Skupinska:** Raczej na pewno to – może tego użyje. Tak, na początku sprawdza. Dlatego ten, którego my używamy, nie działa, bo on powinien – przy – jaki ty mi – jaki jest błąd bazy danych, to powinien zapisać. Ja składam – może, może nie.

**Piotr Buczkowski:** O, to jest tak – działa, że jeżeli wystąpił błąd, to on generuje swój, tak – Exception, który zawiera ten całe info.

**Anna Skupinska:** Mhm.

**Piotr Buczkowski:** Tak, i później też było logowanie gdzie indziej, gdziekolwiek indziej, tak – i logowane już z tym naszym dodatkowym błędem, naszą dodatkową informacją o zawartości.


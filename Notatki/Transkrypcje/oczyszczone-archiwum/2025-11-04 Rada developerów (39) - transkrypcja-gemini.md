**Data spotkania:** 4 listopada 2025

---

**Marek Dziakowski**: Cześć.

**Anna Skupinska**: Cześć. Są jakieś tematy?

**Marek Dziakowski**: Ja bym miał jeden temat do szybkiego przegadania, wynik z ostatnich analiz zgłoszeń z Trust Center. Z Mariuszem analizowaliśmy. Pojawiają się dokumenty w Trust Center, których status nie zgadza się z etapem w procesie podpisywania. Wszystkie procesy są zgłoszone, nie jest to jakiś oddzielny tryb podpisywania, w którym użytkownicy mają sami to zakończyć. Po prostu statusy się nie zgadzają. Możliwe, że jest to też pokłosie problemów na Azure z dostępem do bazy, bo niektóre daty się zgadzały z tymi awariami. Myślimy z Mariuszem, czy nie zrobić takiej opcji w panelu administracyjnym dokumentu, gdzie osoba, która tam wchodzi, mogłaby zweryfikować poprawność statusu. Jeżeli widzimy, w czym jest problem, mogłaby kliknąć guzik, który by pokazał, że jest problem ze statusem i czy go poprawić. Ewentualnie jest jeszcze opcja jakiegoś joba, który by to automatycznie sam robił, tylko to jest trochę więcej pracy.

**Janusz Bossak**: Jaka jest przyczyna tego, że tak się dzieje? Poprawianie tego ręczne już mi się nie podoba. Chciałbym zrozumieć problem.

**Marek Dziakowski**: Problemem jest to, że są dokumenty, które mają zły status. To znaczy, że wszystkie osoby podpisały dokument, ale on nie został dodany do blockchaina, bo status się nie zmienił na "1" albo zmienił się i potem z powrotem ustawił na "0".

**Damian Kaminski**: Ale czemu tak się stało? Nie wiemy. Jaka jest przyczyna?

**Marek Dziakowski**: To jest dobre pytanie. W logach... jeszcze nie zdążyłem przeanalizować nowych przypadków, bo to się zdarzało sporadycznie wcześniej. Dodałem dodatkowe logowanie i przez prawie miesiąc nic się nie działo, dopiero parę dni temu się jeden zdarzył.

**Damian Kaminski**: Czyli może być skrajny przypadek, którego nie uwzględniliśmy, albo kwestie wydajnościowe.

**Janusz Bossak**: Wydajnościowe, jakieś obciążenie?

**Marek Dziakowski**: Jest jeszcze opcja, że mogło się to zgrać w czasie z problemami z dostępem do bazy danych, te problemy, które Łukasz zgłaszał z Microsoftem.

**Mariusz Piotrzkowski**: Wyobraźmy sobie sytuację, że baza danych wyłączyła się na 30 sekund. W tym czasie, jeżeli serwer prześle jakieś dane i baza niby odpowie, że je dostanie, ale nie zapisała ich na dysku, to te dane są zasadniczo uszkodzone. Żeby temu zapobiec, chcemy zrobić jakiś mechanizm, który by to ewentualnie pozwolił ręcznie obejść.

**Damian Kaminski**: Ale to, że ktoś ma to klikać, nie jest profesjonalnym rozwiązaniem, to jest łatanie. Czy jest problem, żeby znaleźć tego typu sprawy systemowo, jakimś jobem?

**Marek Dziakowski**: Nie, nie ma problemu.

**Mariusz Piotrzkowski**: Mieliśmy trzy pomysły. Pierwsze dwa już Marek omówił: albo ręcznie, albo automatyczny job. Jest też coś pomiędzy: samo wyszukiwanie automatycznym skryptem na bazie danych. Marek już zrobił kwerendę, która wyszukuje takie błędne sprawy. Można by zrobić kwerendę, która wykonuje się automatycznie raz na jakiś czas i zbiera dane, a potem byśmy to ręcznie poprawiali.

**Janusz Bossak**: Lepiej byłoby znaleźć przyczynę problemu i nie dopuścić do tego. Te, które już się wydarzyły, można ręcznie popchnąć.

**Marek Dziakowski**: Można po prostu zmienić status na "1" ręcznie i wtedy włączy się tryb podpisywania i się zakończy.

**Janusz Bossak**: Zakończy się, bo rozumiem, że one się nie kończą z powodu braku przestawienia na tę jedynkę.

**Marek Dziakowski**: Tak, z powodu zmiany statusu. Można ręcznie na razie to zrobić. Pytanie, czy nie warto zrobić jakiegoś dodatkowego zabezpieczenia?

**Janusz Bossak**: Zdecydowanie.

**Anna Skupinska**: Czyli na przykład sprawdzać, czy baza danych naprawdę zapisała te dane, które w niej zapisujemy?

**Piotr Buczkowski**: Zaraz, zaraz. Zapisaliście do bazy danych, to się nie zapisało i nie zwróciło błędu?

**Janusz Bossak**: Nie wiadomo właśnie, czy to się w ogóle zapisało.

**Marek Dziakowski**: To są tylko domysły, że mogło tak być.

**Mariusz Piotrzkowski**: Nie wiem, jaka jest dokładnie przyczyna.

**Piotr Buczkowski**: Ale jak się nie zapisało, to przecież kolejne sprawdzenie powinno wykazać, że się nie zapisało. Nie rozumiem.

**Damian Kaminski**: To jest zdarzenie jednorazowe. Jak rozumiem, Piotrze, ktoś podpisuje dokument, wskutek podpisu następuje zapis do bazy danych. Jeśli to się nie wydarzyło, to tak już zostało.

**Piotr Buczkowski**: No to dokument jest dalej do podpisu, rozumiem?

**Marek Dziakowski**: Nie, wszystkie są...

**Damian Kaminski**: Chyba częściowo się wydarzyły zdarzenia po podpisaniu, a częściowo nie. Czyli został podpisany, ale nie został dodany do blockchaina.

**Marek Dziakowski**: Tak.

**Janusz Bossak**: Może ten trop, o którym mówi Piotr. Robić jakiegoś joba po stronie Trust Center, który sprawdza sytuację, że są wszystkie podpisy, ale nie ma blockchaina, i wykonuje tę akcję.

**Marek Dziakowski**: Można zrobić, żeby raz na miesiąc się to odpalało i weryfikowało.

**Janusz Bossak**: Nie, raz na miesiąc to nie. Codziennie.

**Damian Kaminski**: Co tydzień co najmniej, a może codziennie.

**Marek Dziakowski**: Może być raz dziennie.

**Janusz Bossak**: Rozumiem, że w takich przypadkach wszyscy podpisali, ale dokument jest ciągle niepodpisany. To nie może leżeć miesiąc, bo ktoś na to czeka. Może być raz dziennie na koniec dnia. Jak znajdzie takie dokumenty, to je systemowo popchnie.

**Damian Kaminski**: Musimy postawić sobie pytanie: co jest blokerem biznesowym? Sytuacja może być taka, że raz dziennie jest OK, ale równie dobrze może powinien być przycisk, o którym mówi Marek. Jeśli jest bardzo istotne, że to ma być podpisane w tej godzinie, żeby był dowód, to może poza jobem powinien być jakiś trigger, który administrator dokumentu może wywołać z poziomu AMODIT, przechodząc do Trust Center.

**Janusz Bossak**: To jest dobry kierunek. Jest takie zdarzenie po stronie AMODIT, gdzie ktoś klika "sprawdź status". Ta funkcja mogłaby wymuszać nie tylko pasywne, ale aktywne sprawdzenie statusu. Czyli, jeżeli status się nie zgadza, wymusza jego zmianę.

**Marek Dziakowski**: Jest taka droga. Można sprawdzić status dokumentu i statusy podpisujących. Jeżeli status dokumentu się z tym nie zgadza, jest możliwość wywołania endpointu, który wymusi zakończenie procesu podpisywania. Ale wtedy klient musi to wywołać z AMODIT.

**Janusz Bossak**: Dlatego mówię, że taką funkcją jest `TrustCenter_CheckStatus`.

**Damian Kaminski**: Czyli dwie równoległe rzeczy: job, który sprawdza to samodzielnie codziennie w godzinach wieczornych, i wywołanie ręczne dla procesów krytycznych.

**Janusz Bossak**: A inny pomysł: żeby po krótkim czasie, 10-15 minut, wywoływała się taka akcja sprawdzenia i wymuszenia końca na wszelki wypadek. Jeżeli wszystko się wydarzyło prawidłowo, to nic się nie stanie. Ale jeśli znajdzie taki przypadek, to go zakończy. Po każdym podpisaniu tworzyłaby się jakaś kolejka, którą job obsługuje, i po 15 minutach sprawdza, czy blockchain się wygenerował.

**Mariusz Piotrzkowski**: Pytanie, czy to nie obciąży zbytnio bazy danych?

**Marek Dziakowski**: Myślę, że job chodzący raz dziennie w nocy też by zadziałał, tylko jest to przesunięcie w czasie.

**Damian Kaminski**: Trzeba obsłużyć przypadki krytyczne w pierwszej kolejności. Skoro zdarza się to rzadko, to najpierw zrobić wywołanie ręczne, a potem job, który będzie to robił cyklicznie co noc.

**Marek Dziakowski**: Jest obejście, bo można skorzystać z funkcji `Finishing` i to zakończy. To jest remedium na ten przypadek. Chodzi o systemowe zabezpieczenie od naszej strony.

**Damian Kaminski**: OK, to też powinno być opisane. Musimy mieć na to jakąś instrukcję.

**Marek Dziakowski**: Dobrze by było to opisać. Taki przypadek, gdzie statusy się nie zgadzają, że można z tego skorzystać, bo często nawet u nas ludzie nie wiedzą, że jest funkcja w regułach `TrustCenter_FinishSigning`.

**Damian Kaminski**: Podsumujmy. Wywołanie ręczne. Janusz zaproponował `CheckStatus`, ale `Finishing` robi to samo. Trzeba to opisać, a równocześnie zaprojektować joba, który będzie to wykonywał codziennie dla procesów nienewralgicznych.

**Mariusz Piotrzkowski**: Trust Center jest też używany poza monolitem. Co w takiej sytuacji?

**Marek Dziakowski**: Można z tego skorzystać, jeśli klient chce, ale wtedy musi się sam zabezpieczyć i dodać możliwość skorzystania z endpointu od `Finishing`.

**Damian Kaminski**: To jest ich zadanie. My mamy rozwiązanie.

**Łukasz Bott**: Na Wiki na pewno jest opis tej funkcji. Pewnie brakuje wiedzy, że taki krok powinien być w procesach. Marek, prośba o opisanie takiego scenariusza. Na piątkowych spotkaniach możemy zrobić kącik szkoleniowy i uczyć wdrożeniowców.

**Marek Dziakowski**: OK. Czyli nie tylko `Finishing`. Ten job nie jest bardzo pilny, więc może poczekać, ale rozumiem, że jest zielone światło, żeby go zrobić.

**Damian Kaminski**: Tak, bo ludzie nie wyłapią wszystkiego sami.

**Marek Dziakowski**: To wynikło ze zgłoszenia, w którym dokument wisi od lipca.

**Łukasz Bott**: To, że wisiał tyle czasu... ktoś się o to upomniał?

**Marek Dziakowski**: Tak, upomniał się.

**Łukasz Bott**: Może powinniśmy dać jakieś narzędzie, które umożliwia zrobienie raportu, że dokumenty wiszą dłużej niż np. 5 dni.

**Damian Kaminski**: Ale to jest po stronie AMODIT. Ten dokument nie wrócił do AMODIT, więc to element wdrożeniowy.

**Janusz Bossak**: Ale nie wrócił, bo po stronie Trust Center nie zakończył się proces.

**Damian Kaminski**: No tak, ale wtedy trzeba dołożyć wykorzystanie endpointu `FinishSigning` do tego procesu i on zakończy ten proces. A kwestia raportu... mamy proces podpisywania, naturalne jest, że ma etapy. To po prostu wisi na etapie "w podpisie", bo nie wróciło z Trust Center. Nie wydaje mi się, że potrzebne jest dodatkowe narzędzie.

**Łukasz Bott**: Miałem na myśli narzędzie dla nas, żeby monitorować, że coś podejrzanie długo wisi.

**Mariusz Piotrzkowski**: Marek ma kwerendę. Można by zrobić, żeby sama się w bazie danych wykonywała raz na dobę.

**Damian Kaminski**: Zanim zrobimy kwerendę, co to ma rozwiązać? Kto to będzie obserwował? Zrobimy coś, do czego nikt potem nie zajrzy.

**Janusz Bossak**: Dobra. Marek, co proponujesz jako rozwiązanie?

**Marek Dziakowski**: Proponuję zrobić tego joba, który by automatycznie raz na dobę skanował dokumenty pod tym kątem i ewentualnie poprawiał.

**Janusz Bossak**: I tak zróbmy, koniec.

**Damian Kaminski**: Łukasz poruszył jeszcze jedną rzecz. Marku, czy mamy możliwość wysłania do Trust Center dokumentu do podpisu na czas nieokreślony? Czy mogę wysłać do ciebie dokument, który będzie wisiał 10 lat? Mamy termin podpisania, który można określić lub nie. Jeśli go nie określam, czy powinniśmy wprowadzić, że nieokreślony termin oznacza, że dokument czeka np. pół roku, a potem go wygaszamy? Trzymanie czegoś 10 lat nie ma sensu. Zastanów się nad tym, sprawdź i wróć na kolejnej Radzie. Może to już jest zaopiekowane. Jeśli nie, trzeba zrobić wpis na Wiki, że nie będziemy trzymać dokumentów w nieskończoność. I wtedy problem, który poruszył Łukasz, sam się rozwiązuje.

**Łukasz Bott**: Mniej więcej o to mi chodziło.

**Damian Kaminski**: Przygotuj się na kolejną radę i daj nam tutaj wynik twojego śledztwa. Zdefiniujemy jakieś sensowne ramy biznesowe. Dobra, przechodzimy do bieżących tematów.

**Łukasz Bott**: To, co wyszło z bieżących rzeczy, to kwestia modułu dla usług AI. Wyszło, że Mateusz to już dorobił, normalizując to, co jest przetwarzane. Okazało się, że możemy zahaczyć o RODO. Rozumiem, że to temat do omówienia z Mateuszem na odrębnym spotkaniu.

**Damian Kaminski**: Już to omawialiśmy wczoraj wstępnie z Januszem i z Mateuszem. Powstały z tego konkluzje, jeszcze nie zdążyłem zrobić z tego PBI. Jest trochę przemyśleń, jak to rozwiązać. Trzeba to spisać i pochylić się nad tym na dedykowanym spotkaniu, bo tam są zadania po stronie i serwisu bilingowego, i samego AMODIT.

**Damian Kaminski**: Może od tego zacznijmy. Pytanie do Piotra, jaką ma sugestię. Wczoraj podejmowaliśmy temat, w jaki sposób po stronie AMODIT wykryć i zapobiec wysyłaniu tych samych plików do AI OCR. Możemy oczywiście wyliczać hash.

**Janusz Bossak**: Z tej dyskusji wyniknęły dwa przypadki. Jeden, który nas kosztował chyba 20 000 zł za przetwarzanie tego samego dokumentu wysyłanego wielokrotnie z reguły okresowej co minutę przez cały weekend. To podobno mamy obsłużone, bo jest parametr `force`, który musi być ustawiony, żeby ponownie się dokument OCR-ował. Jeśli parametru `force` nie ma, to wie, że już taki dokument był i drugi raz go nie robi. Drugi przypadek, który podał Mateusz, to zakładanie sprawy z maila. Problem może nastąpić, gdy ten sam mail będzie co 5 minut powodował założenie nowej sprawy z tym samym dokumentem. Powiedziałem wczoraj, że to nie jest problem OCR, tylko zabezpieczenia mechanizmu zakładającego sprawy, żeby nie zakładał spraw z tego samego maila na skutek błędu. Jakiś błąd komunikacyjny, gdzie niby ustawiamy mail jako odczytany, a on się nie zapisuje jako odczytany.

**Damian Kaminski**: Analgią jest zakładanie z pliku, gdyby nie było uprawnień do zapisu na zasobie sieciowym. Odczytujemy plik, nie możemy go skasować, znowu odczytujemy.

**Janusz Bossak**: Tak. Moja konkluzja była taka, że to nie jest problem OCR. Nie chciałbym, żeby OCR był miejscem, gdzie to się łapie, bo to już za późno. Musimy rozwiązać problem z zakładaniem sprawy z maila i z pliku.

**Damian Kaminski**: Uzupełnię pierwszy przypadek. On nie jest rozwiązany przez `force`. Jest świadomość, że trzeba dodać parametr `force`, żeby jeszcze raz wysłać ten sam dokument, ale widzę ryzyko...

**Piotr Buczkowski**: Jest taka zasada, że domyślnie z reguły ręcznej jest dodawany `force`.

**Janusz Bossak**: Właśnie.

**Piotr Buczkowski**: Jak się naciśnie przycisk, to jest dodawany `force`. Jeżeli działa z reguły automatycznej, nie jest dodawany. To jest natywnie.

**Damian Kaminski**: A, OK. To super, to jest bezpieczne.

**Piotr Buczkowski**: Ręcznie, nawet jak wyślesz ponownie, to wyślesz 2-3 razy, a nie 2000.

**Janusz Bossak**: Czasami trzeba wysłać 2-3 razy, bo testujesz coś.

**Kamil Dubaniowski**: Czy masz pewność, że w nowym `Skanuj` też tak jest?

**Piotr Buczkowski**: Ja mówię, jak jest w `Skanuj OCR`.

**Damian Kaminski**: OK, to jest rozwiązanie, czyli wysyłanie z jednej sprawy wielu takich samych dokumentów regułą okresową powinno być zablokowane.

**Piotr Buczkowski**: Mówicie, że to nie jest kwestia OCR. To jest kwestia OCR, żeby się przed tym bronił, tak samo jak broni się `Skanuj OCR`.

**Janusz Bossak**: Jeszcze jedna kwestia poruszana przez Mateusza: duże pliki, np. 100 stron. W `Skanuj OCR` był mechanizm, że można było ograniczyć, ile stron idzie do OCR. Jak to zrobić z nowym OCR?

**Łukasz Bott**: Jeżeli użytkownik jest świadomy, że tego jest dużo, to może zastosować mechanizm wydzielania stron, ale to obsługa manualna.

**Damian Kaminski**: To, co powiedział Piotr, jest super rozwiązaniem. Po stronie AMODIT, mimo że parametr `force` jest opublikowany, trzeba go wywalić i dodać to natywnie. Parametr ma być kasowany z reguły okresowej i dodawany do ręcznej.

**Piotr Buczkowski**: Gdzie ma być ten parametr analizowany, w AMODIT czy w OCR?

**Damian Kaminski**: W AMODIT, według mnie.

**Janusz Bossak**: Według mnie w OCR też.

**Piotr Buczkowski**: Tak. OCR musi przechowywać listę hashy przetworzonych plików.

**Damian Kaminski**: Tak.

**Piotr Buczkowski**: Jeżeli w nowo wysłanym pliku nie ma `force` i hash się zgadza, to zwraca błąd, że duplikat.

**Damian Kaminski**: Jeśli my to zaopiekujemy po stronie AMODIT...

**Piotr Buczkowski**: I tu, i tu.

**Janusz Bossak**: Dlaczego i tu, i tu, Piotr?

**Piotr Buczkowski**: Chcecie bezpiecznie czy nie?

**Damian Kaminski**: Czy da się zrobić obejście tego, że natywnie AMODIT to doda albo usunie?

**Piotr Buczkowski**: Ja mówię o tym, gdzie to ma być analizowane.

**Łukasz Bott**: Zgodzę się z Piotrem, po stronie silnika OCR powinno to być wyłapywane.

**Piotr Buczkowski**: To, że ustawisz `force`, znaczy, że gdzieś to musi być zrealizowane.

**Damian Kaminski**: Oczywiście, musi być interpretacja po stronie OCR. Chodzi o to, że AMODIT sam zaopiekuje się dodawaniem lub niedodawaniem `force` w zależności od typu reguły.

**Piotr Buczkowski**: Tak.

**Damian Kaminski**: A co, jeśli ktoś, załóżmy, nie ma `force` i wysyła ten sam plik? Chcemy wykastrować biling z treści dokumentów.

**Piotr Buczkowski**: Co masz na myśli?

**Janusz Bossak**: Chodzi o to, że jeśli ktoś wysyła drugi raz, to czy ma dostać gotową odpowiedź od OCR?

**Piotr Buczkowski**: Nie, ma dostać błąd, że duplikat. Po stronie OCR powinna być tabela z listą hashy przetworzonych dokumentów, zaindeksowana. Przychodzi dokument, wyliczamy hash, sprawdzamy, czy jest w tabeli. Jeśli jest, zwracamy błąd. Jeśli nie, przyjmujemy do przetworzenia.

**Janusz Bossak**: I ta tabela hashy powinna być w mikroserwisie OCR-owym, po tamtej stronie?

**Piotr Buczkowski**: Tak.

**Łukasz Bott**: Chyba że przyjdzie dokument z atrybutem `force: true`.

**Piotr Buczkowski**: Wtedy nie musi sprawdzać hasha.

**Janusz Bossak**: Mów, Piotr.

**Piotr Buczkowski**: Czy ktoś oprócz AMODIT korzysta z tego OCR-a?

**Damian Kaminski**: Nie korzysta.

**Łukasz Bott**: Mikroserwis AI ma własne REST API, teoretycznie można z tego skorzystać. Mamy dwóch, może trzeciego klienta, który potrzebował zintegrować swoje narzędzie z OCR do faktur. Opcje były takie, żeby dać im specyfikację REST API mikroserwisu, ale stwierdziliśmy, że nie, bo wolimy mieć nad tym kontrolę. Obecnie podejście jest takie, że klient musi zainstalować jedno-licencyjnego AMODIT, w którym konfigurujemy mu proces wysyłający do OCR, a wszelką komunikację robi przez REST API AMODIT.

**Damian Kaminski**: I to zabezpiecza.

**Łukasz Bott**: Ale pytanie, czy nie przewidujemy, że przyjdzie klient, który zapłaci miliony i nie będzie chciał AMODIT, a tylko nasz OCR.

**Damian Kaminski**: Jak zapłaci miliony, to bierze na siebie odpowiedzialność. Powinna być dokumentacja, że trzeba to zabezpieczyć tak, jak my to robimy. Jeśli ktoś będzie się łączył bezpośrednio, to na niego spada odpowiedzialność, że reguły cykliczne nie mogą wysyłać parametru `force`. To nasze zalecenie, a jak ktoś wyśle, to jego odpowiedzialność.

**Łukasz Bott**: Te warunki powinny być wpisane w ogólnych warunkach użytkowania AI OCR.

**Damian Kaminski**: Dobra, to formalność. Wróćmy do tego, bo to są przypadki zabezpieczeń w ramach wywołania z tej samej sprawy. To dotyczy reguły `SendToOcr`, tak?

**Łukasz Bott**: Nazwę funkcji wrzuciłem na czat.

**Damian Kaminski**: A co z tym problemem zakładania spraw z maila/pliku?

**Piotr Buczkowski**: To jest inne zadanie, które jest opisane, ale odłożone.

**Damian Kaminski**: Jest już opisane? Jak je znaleźć?

**Piotr Buczkowski**: Dawno. Nie potrafię znaleźć.

**Damian Kaminski**: To jakbyś mógł dopowiedzieć?

**Piotr Buczkowski**: Teraz job pobiera nieodczytane maile, bierze jeden, przetwarza, zaznacza jako odczytany. Chodzi o to, żeby dodać pośrednią tabelę. Wczytujemy mail, zapisujemy w tabeli jego identyfikator, przetwarzamy, zaznaczamy, że przetworzyliśmy. Przy ponownym wczytaniu maili sprawdzamy w tej tabeli, czy był już przetwarzany. Jeśli nie, to przetwarzamy. W przypadku błędu połączenia, przy ponownym sprawdzaniu zostanie wykryte, że już go przetwarzaliśmy. Tabela z ID maila, ID sprawy utworzonej, status.

**Damian Kaminski**: OK. A dla plików? Mogę celowo chcieć wczytać drugi raz ten sam plik.

**Piotr Buczkowski**: Z plików to nie było. Trzeba by wymyślić, co będzie identyfikatorem pliku.

**Damian Kaminski**: Hash i data modyfikacji.

**Piotr Buczkowski**: Tak.

**Damian Kaminski**: Jak wrzucam drugi raz ten sam plik, to ma inną datę modyfikacji.

**Piotr Buczkowski**: Pytanie, czy plik ma jakiś identyfikator w NTFS? W mailu jest `Message-ID`, który jest unikalnym GUID-em i to jest bardzo dobry identyfikator.

**Damian Kaminski**: Dobra, to do rozpisania. Tu hash pliku i data modyfikacji.

**Piotr Buczkowski**: I nazwa też, żeby było wiadomo.

**Damian Kaminski**: `ScanID`. Dobra. Mamy to rozpisane, ja to rozpiszę na dwa odrębne zadania. Powiedziałbym, że to ma wyższy priorytet.

**Piotr Buczkowski**: A co ze zgłoszeniem "Nie wyszukuje spraw"?

**Damian Kaminski**: Czekamy na odpowiedź. Tomek dostał wytyczne.

**Piotr Buczkowski**: W Rossmanie testowaliśmy naprawianie indeksu.

**Damian Kaminski**: To może tu jest to samo. Wiedza jest w dziale serwisu.

**Piotr Buczkowski**: Albo Kacper przez pomyłkę uruchomił `fix-index` na produkcji zamiast na kopii i naprawił.

**Damian Kaminski**: Dobra. Jest też świeże zgłoszenie, podpięte pod ciebie i pod radę: "Zmiana kategorii maili o zmianie na sprawie". Chodzi o maile o edycji dokumentu, dodaniu komentarza. Teraz są traktowane jako powiadomienia główne, tak samo jak o przekazaniu sprawy. Propozycja jest, żeby były traktowane jako dodatkowe, aby można było je wyłączyć w panelu użytkownika. Myślę, że ma to sens.

**Janusz Bossak**: Nie chciałbym tak szybko zmieniać. To jest teraz jako powiadomienia główne. Kto to napisał?

**Damian Kaminski**: W AmRest tak chcieli.

**Piotr Buczkowski**: To z rozmowy z AmRest, dlaczego dostają takie maile.

**Janusz Bossak**: Wydaje mi się, że to większa sprawa. Może trzeba więcej grup, może customowe zasady wysyłania powiadomień. To do przemyślenia, nie robiłbym szybkich zmian.

**Damian Kaminski**: Kto wie, gdzie jest ta tabela? Janusz, masz ją?

**Janusz Bossak**: Tak, muszę ją poszukać. Komuś przekazywałem, może jest na wewnętrznej Wiki. Sprawdzę.

**Damian Kaminski**: Trzeba to spiąć i ustalić, co tam jest do zdefiniowania. Zdejmę to z Piotra. Kto jest chętny to zaopiekować?

**Anna Skupinska**: Zmiana kategorii maili...

**Piotr Buczkowski**: To nie jest pytanie, kto to wykona, tylko czy jest sens to wykonywać.

**Damian Kaminski**: Kto to przeanalizuje? Ja, Łukasz, Kamil? Dobra, przypiszę do siebie, skoro nie ma chętnych. Trzeba temu poświęcić spotkanie. Trzeba określić, co to jest "itd." i zrobić wpis na Wiki.

**Janusz Bossak**: Znalazłem artykuł na wewnętrznej Wiki, wrzucam na czat.

**Damian Kaminski**: OK, trzeba to zaopiekować całościowo i opublikować na głównej Wiki, żeby ktoś wiedział, na co ma wpływ zmiana ustawień w profilu.

**Janusz Bossak**: Tę tablicę tworzyliśmy z Rafałem nie wiem, ile lat temu. Może być lekko nieaktualna.

**Damian Kaminski**: No to na pewno będzie potrzebne wsparcie dewelopera, który to zweryfikuje. To większy temat, nie na godzinę. Zdejmę to z rady na razie. Aniu, czy miałaś przestrzeń sprawdzić temat z ostatniej rady?

**Anna Skupinska**: Nie, jeszcze się tym nie zajęłam. Myślałam, żeby dzisiaj.

**Damian Kaminski**: Dobra, zanotuj i na następnej radzie się do tego odwołamy.

**Anna Skupinska**: Jasne, chodzi o to, że "zaznacz wszystko" nie zaznacza wszystkiego.

**Damian Kaminski**: Tak, trzeba sprawdzić, na podstawie czego jest generowana ta lista. Janusz pokazywał przykład, gdzie na raporcie były 3, a wyświetlały się 2 z 3.

**Janusz Bossak**: To jeden z wielu błędów w module raportowym.

**Damian Kaminski**: Z tematów przypisanych do klientów mamy wszystko zaopiekowane. Coś jeszcze?

**Piotr Buczkowski**: Mam jedną uwagę. W jobach wykonywanych przez serwis jest mechanizm, który sprawdza, czy serwis się nie zatrzymuje, i wtedy przerywa działanie. Zrobiłem to dla jobów, które istniały 2-3 lata temu. Przyszło wiele nowych: do AI, do e-Nadawcy. Trzeba przejrzeć wszystkie, czy potrafią prawidłowo przerwać działanie.

**Damian Kaminski**: Żeby nie było zapętlenia?

**Piotr Buczkowski**: Nie, chodzi o zatrzymanie usługi. Jak zatrzymam usługę, żeby job potrafił się zatrzymać, był świadomy, że usługa się zatrzymuje. Jak ma do wykonania 100 zadań i jest po 5-6, to nie robi następnego, tylko kończy to, co robi i się przerywa bezpiecznie, żeby `kill` nie zatrzymał go w środku zadania, co może powodować niespójność danych.

**Damian Kaminski**: Ważne. Zrobisz do tego zgłoszenie?

**Piotr Buczkowski**: Nie wiem, jak to zgłosić, czy dla wszystkich jobów, czy po jednym.

**Damian Kaminski**: Zrób ogólne, a pod spodem PBI dla każdego joba i będziemy przydzielać.

**Piotr Buczkowski**: To będzie ważne, bo będzie mechanizm ograniczenia wydajności serwerów, np. serwisowych na czas, żeby oszczędzić pieniądze. To wymaga zatrzymania i restartu serwera.

**Damian Kaminski**: Dobra, tak to nazywam i przypisuję do ciebie.

**Piotr Buczkowski**: Muszę przejrzeć, jakie joby są zarejestrowane.

**Damian Kaminski**: Tak, i wypisz, które joby trzeba prześledzić. Niestety, za 3 minuty muszę się przełączać, więc chyba na tym zakończymy. Przypominam, Piotrze, o tych wytycznych do repozytorium, żeby je opisać.

**Piotr Buczkowski**: Po spotkaniu się tym zajmę.

**Damian Kaminski**: Z mojej strony wszystko. Dzięki za dzisiaj. Cześć.

**Łukasz Bott**: Dzięki.

**Data spotkania:** 25 listopada 2025, 09:00 - część 4

---

**Damian Kaminski:** Tak, tak, tak, twoim, twoim, bo mówisz, że jakieś.

**Janusz Bossak:** Znaczy mój temat to jest na wycenach, czy i i Łukasza tego Brockiego trzeba wciągnąć.

**Damian Kaminski:** A ten?

**Janusz Bossak:** Pytanie jest w zasadzie do, do, do Piotra też i do, do. Jakbyś mógł wyświetlić tę wycenę.

**Damian Kaminski:** Mogę.

**Lukasz Brocki:** Cześć.

**Janusz Bossak:** Cześć Łukasz. Chcemy omówić ten temat tego DokSign. Ogólna, jakby moja, moje rozumienie tego jest takie, że mamy integrację zrobioną z DokSignem, tak samo jak tam z AD, czyli generalnie mamy koncepcję wyślij, zapomnij, tak, czyli wysyłamy coś, to idzie ze do DokSigna, dopisanie, coś tam się dzieje, my pobieramy dokument. Dla LOTU jest to za mało, ponieważ DokSign ma pewne funkcjonalności, które pozwalają im na jakby pracę z tym dokumentem po stronie DokSign. I z tego, co ja rozumiem, to jest to jakaś koncepcja tego envelope, trochę, trochę mi to się kojarzy z Nadawcą, gdzie też jest taki envelope.

**Lukasz Brocki:** Zgadza się.

**Janusz Bossak:** I chcemy im udostępnić, umożliwić wysłanie. Tego dokumentu do podpisu w ramach takiego envelope.

**Lukasz Brocki:** Takie dokładnie to zostało wycenione.

**Damian Kaminski:** Czyli do edycji, tak jeszcze, czyli jak?

**Janusz Bossak:** Do edycji, wtedy oni.

**Lukasz Brocki:** Tak, edycja, dodanie tam podpisujących ewentualnych i tak dalej.

**Damian Kaminski:** Czyli przeniesienie zarządzania procesem podpisywania na poziom DokSigna. Więc w skrócie, tak.

**Janusz Bossak:** Znaczy troszeczkę tak, znaczy tam jest po prostu więcej możliwości tej zmiany podpisującego i tam parę innych rzeczy, które mogą sobie zrobić po stronie DokSign.

**Lukasz Brocki:** Tak.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Efekt końcowy jest taki, czy ma być taki, że ja, jak ja rozumiem, że my po stronie AMODIT nie aktualizujemy danych w AMODIT?

**Lukasz Brocki:** Tak, po wysłaniu nie aktualizujemy, potem co najwyżej pobieramy ten dokument już podpisany. Jeżeli coś się zmieni po stronie.

**Janusz Bossak:** Oni chcą.

**Damian Kaminski:** Podpisane.

**Janusz Bossak:** Tak.

**Damian Kaminski:** Czyli AMODIT w zasadzie trwa tylko przygotowanie dokumentu. Nie ma definicji, kto podpisuje, kiedy, jakie czasy, jakie formami i tak dalej.

**Lukasz Brocki:** Zgadza się.

**Janusz Bossak:** Nie jest definicja, kto podpisuje?

**Lukasz Brocki:** Znaczy można to wstępnie przygotować, ale jeżeli coś zostanie zmienione po stronie w DokSignie, to to nie będzie odzwierciedlone w AMODIT.

**Damian Kaminski:** OK. Mhm. Mhm.

**Janusz Bossak:** Tak i to jest jeden temat, potem oni, jakbyś to mógł Łukasz wyjaśnić z tym tokenem, bo oni już normalnie mają drugi temat w tej wycenie, prośbę, którą rozszerzyli teraz jakby ostatnio, że oni by chcieli jednak wykonywać też inne endpointy czy wywoływać inne endpointy do DokSigna niż ten, niż te, które my tam zaprogramowaliśmy i użyliśmy, nie. Czyli mi się zaraz skojarzyło to z CallRest, dlaczego by nie wywołać tego przez CallRest, skoro to są inne endpointy do DokSigna. Tam się potem okazało, że jest jakiś do tego, do kogo trzeba się logować tam OAuth, tam przez ten JWT i tak dalej. No i teraz pytanie, czy robić?

**Piotr Buczkowski:** Powiedzieliśmy dorobić logowanie OAuth do CallRest.

**Damian Kaminski:** No według mnie też, bo my nawet do samego, czy. Sami do siebie musimy wtedy basic auth korzystać.

**Lukasz Brocki:** Tak, to był, co Piotr zaproponował. Byłoby najlepszym rozwiązaniem, bo oni chcieli po prostu pozyskać token. No ale nie powinniśmy tak zawracać tokenu samego.

**Janusz Bossak:** No nie, nie, no właśnie to mi się strasznie tam nie podobało w tym pomyśle, żeby.

**Lukasz Brocki:** Tak, dlatego co od razu odrzuciłem, tak jako takie, no nie powinno tak być robione, więc od razu napisałem, że no nie powinno być tak.

**Damian Kaminski:** Że token jest przetrzymywany w sprawie, tak?

**Janusz Bossak:** Funkcja typu. Nie, nie, nie. No w ogóle zapomnijmy o takich pomysłach, jakieś tam get token i że to sobie zapisujesz w jakiejś zmiennej gdzieś tam.

**Damian Kaminski:** Ale to tak, tak jest robione we wszystkich integracjach, gdzie mamy OAuth, niestety, w sensie gdzieś to znaczy można to przetrzymać w pamięci.

**Piotr Buczkowski:** Logowanie, logowanie OAuth można jak najbardziej zasymulować obecnymi funkcjonalnościami. Do kogo to było? Obsłużone natywnie.

**Janusz Bossak:** No to tak zróbmy, żeby to było obsłużone natywnie i nie róbmy takich tutaj na okrętkę różnych rzeczy.

**Damian Kaminski:** Dokładnie.

**Janusz Bossak:** I to samo. Chciałem właśnie zaproponować, żeby rozszerzyć funkcję CallRest, czy ten mechanizm ogólny CallRest, o to, żeby on obsługiwał te tokeny? Tutaj jest jakiś tam problem taki, że ten token jest zmienny, że on tam się co pół godziny do godziny może zmienić i tak dalej.

**Damian Kaminski:** Tak, no tu musimy wszystko uwzględnić, czyli i tak dalej, tak.

**Piotr Buczkowski:** No ale to jest ogólne zasady.

**Janusz Bossak:** Tak, tak, tak, tak, więc OK. Czyli zgadzamy się co do zasady idei, że tam pierwsze, ten pierwszą część tego, ten envelope, to to możemy im zrealizować bez jakby dodatkowych tutaj po naszej stronie robót. No bo po prostu wysyłamy jakby w kontekście tego envelope i oni sobie coś tam potem robią. Ja się odczytywałem tutaj czata i on twierdzi, że tam są jakby 3 stany, taki, znaczy 2 stany właśnie takich create. To jest stworzenie tej, tej, tej koperty tego envelope. Tak i potem jest edycja tej koperty, no ale pytanie, czy my potrzebujemy ten edit? No bo i tak ktoś wejdzie sobie, to znaczy, my potrzebujemy tylko link do tego, takie fajne, żeby ten administrator czy tam ktoś, kto po stronie AMODIT tę sprawę edytuje, żeby mógł tak jak u nas wejść do TrustCenter, to tutaj, żeby mógł wejść do tego DokSigna, tak i coś tam w nim zmienić, ale nie żeby zmieniał z poziomu AMODIT, bo o to mi chodziło, tak, że. Nie robimy funkcjonalności. Edycji wysłanej koperty, która jest już w DokSignie, tylko pozwalamy na przejście do DokSigna i niech robi, co tam chce, nie dodaje podpisujących, usuwa, zmienia cokolwiek, nie.

**Lukasz Brocki:** Tak. Pozwalamy na utworzenie plus na pobranie, ty potem dokumentu oraz wygenerowanie linku, który przeniesie potem do tego envelope już po stronie DokSigna.

**Damian Kaminski:** Tak, tak jak tu.

**Janusz Bossak:** No. OK. Jest tylko pytanie, czy to jest tam wystarczająco, więc ja po prostu nigdy nie używałem tego DokSigna i nie wiem, czy rozwiązujemy jakby problem klienta, tak, znaczy czy mamy, czy to są wszystkie klocki potrzebne?

**Damian Kaminski:** Znaczy, według mnie zróbmy MVP, czyli zróbmy tak, że i i to tak uargumentujmy, że robimy tylko połączenie, nie robimy nadpisywania z poziomu AMODIT, czyli właśnie powiedzmy tej edycji, bo i tak to wtedy nie gwarantujemy spójności danych, czyli my zrobimy edycję, jak ktoś może sobie poprawić i tak tam, więc po co to robić?

**Janusz Bossak:** On może tam wpisać podpisującego, którego nie mamy w ogóle w AMODIT, no.

**Damian Kaminski:** No właśnie. Więc zróbmy według mnie jako MVP minimum ze wskazaniem, że chcemy robić tylko to, czyli zarejestrowani z możliwością dalszej obsługi w DokSignie, a nie z możliwością rekonfiguracji tych parametrów, bo my to zrobimy, jak to się tak wejdzie, tam namiesza i mamy niespójne dane, więc mało to daje.

**Janusz Bossak:** Dobra, czyli. Łukasz Brocki, do ciebie prośba. Żeby to tak opisać, tyle będzie z tego zapis z transkrypcji, więc będzie można się posłużyć tym. No, ale robimy 2 kroki – krok pierwszy wysyłanie tego envelope, znaczy tworzenie i i tak tworzenie envelope, drugiej tworzenie linku do tego DokSigna, żeby mógł się ten człowiek przenieść tam DokSign i tam dokonać jakichś zmian. Pobranie pliku to już mamy i niezależnie ta dodatkowa wycena, o którą prosi LOTU, to. Współpraca z tym OAuth i robimy ją na zasadzie jakby natywnej, to znaczy do rozszerzamy funkcjonalność CallRest o obsługę OAuth i dzięki temu będą oni mogli sobie wy. Pływać dowolny endpoint. Do DokSigna jakiekolwiek chcą, no bo wykorzystają po prostu natywnie funkcje CallRest, która będzie obsługiwała OAuth, tak.

**Lukasz Brocki:** Dobrze.

**Janusz Bossak:** OK. To taką wycenę też, znaczy, no wycenę, zdaje się, pracochłonności po naszej stronie przygotuj tutaj.

**Lukasz Brocki:** Nie pamiętam, co tam to zgłasza. Ja też się skontaktuję, zaraz obejrzę.

**Janusz Bossak:** Na razie przygotuj dla nas tutaj.

**Lukasz Brocki:** A dobra, OK, dobra, wewnętrznie, tylko dobra?

**Janusz Bossak:** Jeśli chodzi o ten OAuth, reszcie tutaj koniecznie z Piotrem. Czy tam z Adrianem? No nie wiem, kto tam się tym bardziej opiekuje obecnie i ustalcie dokładnie, co będzie zrobione, żeby to już było takie, wiecie.

**Piotr Buczkowski:** No bo tutaj na przykład może być logowanie też certyfikatem.

**Janusz Bossak:** Oj, gdzieś czasem certyfikatu.

**Damian Kaminski:** Się gdzie?

**Piotr Buczkowski:** Na przykład, na przykład te Mazura, tak jak ja, żeby teraz szeroko pojętą.

**Janusz Bossak:** Po OAuth.

**Damian Kaminski:** Ale to mówisz o jakimś kolejnym typie połączenia, tak?

**Piotr Buczkowski:** Tak, bo OAuth, ale logowanie certyfikatem, bo MAUI jest zablokował. Przynajmniej w PowerPoint właśnie ten, czy tam zablokuje niedługo.

**Lukasz Brocki:** Czyli login hasło plus certyfikat, tak dobrze rozumiem, czy jeszcze inaczej?

**Piotr Buczkowski:** To aplikacja tion. Jak?

**Lukasz Brocki:** Login hasło plus certyfikat.

**Piotr Buczkowski:** Nie, certyfikat, po co login hasło.

**Lukasz Brocki:** Tak. Tak samo certyfikat, dobra.

**Janusz Bossak:** No trzeba gdzieś go trzymać w jakimś KeyVault albo gdzieś.

**Piotr Buczkowski:** Mamy KeyVault i też jest, właśnie ja na razie dla SharePoint zrobiłem parametr systemowy problem typu plik. Czyli plik do paszportu lub fix musi mieć paszport. No ale właśnie nie wiem, czy w ramach tego.

**Damian Kaminski:** No właśnie, czy to jest wymagane teraz, bo.

**Piotr Buczkowski:** Zmiany trzeba to rozbudować.

**Damian Kaminski:** Może róbmy krok po kroku.

**Janusz Bossak:** Słusznie, słusznie, no ale dlatego Łukasz prośba – opracowanie tego takiej strony deweloperskiej, tak tutaj, w zespole z Piotrem, żeby to nie było takie tam dobra, dobra, to tam zrobimy certyfikat. Nie, nie, zróbmy to dobrze, to znaczy dobrze, mam na myśli przemyślmy różne przypadki.

**Lukasz Brocki:** Dobra.

**Janusz Bossak:** Opiszmy te przypadki nawet, czyli w takiej sytuacji będzie to robione tak, w takiej sytuacji będzie robione tak, w takiej sytuacji będzie robione tak, tak, czyli od takiej strony deweloperskiej to. Z Piotrem pracujcie, pomyślcie chwilę, pogadajcie, ustalcie różne przypadki, co z nimi zrobić? Właśnie gdzie tym? Certyfikat zapisywać, co jest lepsze, co gorsze i tak dalej, dobra i wtedy możemy.

**Lukasz Brocki:** A KeyVaultem się zajmował Adrian, jak coś, tak dobrze kojarzę.

**Piotr Buczkowski:** Tak, tak.

**Lukasz Brocki:** OK.

**Janusz Bossak:** Przechodnie, tak.

**Piotr Buczkowski:** No ale ja najpewniej trochę. Rozszerzę to w ramach tej zmiany doszedł.


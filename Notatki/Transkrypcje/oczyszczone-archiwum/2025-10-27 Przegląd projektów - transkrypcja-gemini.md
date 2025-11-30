**Data spotkania:** 27 października 2025

---

**Janusz Bossak**: Dyskutować, nie prowadzić konwersacji i tak dalej. No i tworzysz kolejne jako Użytkownik: "Chcę móc wybrać, jakie osoby są uczestnikami tej konwersacji" i tak dalej. Zbiór takich historyjek tworzy dla mnie MVP. To sprowadza się do MVP, feature'ów i PBI, jak zwał tak zwał, jakieś tam funkcjonalności czy historyjki, jakkolwiek, ale chodzi mi o to, żeby to było jasne i od razu oczywiste. My właściwie patrząc na sprint, patrzymy na PBI, a ja bym chciał, żebyśmy patrzyli piętro wyżej, żebyśmy patrzyli na feature'y.

**Kamil Dubaniowski**: Tak.

**Janusz Bossak**: Że w tym sprincie mamy dowieźć jakiś feature. Na przykład to, co było z tym komunikatorem: możliwość utworzenia grupy... właśnie chcę unikać słowa "grupa", ale możliwość utworzenia tej konwersacji, komunikacji dla grupy AMODIT-owej. I to jest cel, że na koniec sprintu ta funkcjonalność zostanie dowieziona. Takich rzeczy prawdopodobnie jest 5, 6, 10 i to powinno być rozpisane. Na przykład w kwartale to dowieziemy, w tym sprincie to, w tym sprincie te dwie rzeczy, bo są łatwe i krótkie. Na koniec mamy to gotowe. Chciałbym, żebyśmy myśleli takimi kategoriami. Teraz mam wrażenie, że jest ciągła szarpanina. Przypomnijmy sobie: "kurde, ten komunikator, a co tam nie było do zrobienia? A, chyba to jeszcze nie. Dobra, no to może niech Mateusz tam poprawi, żeby się te linie zgadzały". Albo kiedyś zrobił jakieś grupy. No jakieś tam zrobił, ale nie wiem, czy dobrze, czy nie dobrze. Tego mi brakuje. Wiem, że i ty, i Damian już staracie się to jakoś opisywać, ale ja na przykład nie umiem tego śledzić, nie wiem którym narzędziem. Teraz na przykład zaczęliśmy to w Excelu wpisywać. Nie wiem, czy my to robimy – ty, Damian, Łukasz, wszyscy razem – w jednolity sposób na backlogu. Dla mnie jest to OK, tylko chcę to wiedzieć.

**Kamil Dubaniowski**: Wydaje mi się, że nie jest jednolicie. Ja już od dłuższego czasu chciałem działać w ten sposób. To nie jest idealne, bo brakuje mnóstwa zgłoszeń, czasami coś podpinam na siłę, nie tak, jak bym sobie życzył, bo nie mam czasu rozpisywać nowego epica, a powiedzmy, że jakoś mi tam pasuje. Na przykład: modernizacja konfiguracji procesu, MVP 2. Już w tym momencie robimy prezentowanie definicji formularza w widoku listy pól i pod to podpinam pojedyncze zadania dla Filipa. Backend jest, więc działa sam Filip w tym projekcie. Usprawnienia w edytorze graficznym formularza – to tak naprawdę Przemek realizuje ten projekt. To są wszystkie zgłoszenia, które wpadają gdzieś na czatach i inne rzeczy, że coś tu było inaczej, czegoś brakuje albo coś nie działa, jak powinno. I tak mam w sumie pod każdy z tych tematów. Modernizacja konfiguracji procesu to było MVP 1 i takie feature'y wtedy realizowaliśmy. Ustawienia systemowe MVP 2 – tam gdzieś jest, co robiliśmy w MVP 2. Staram się to już tak układać i działam na tym widoku, tworząc nowy temat, nowy feature i z tego poziomu opisuję pojedyncze PBI. Od dłuższego czasu to sobie układam, ale wydaje mi się, że to nie jest standard.

**Janusz Bossak**: Pamiętam jak pracujesz. Damian, pojawiłeś się. Cześć.

**Damian Kaminski**: Tak, przepraszam za spóźnienie, ale mam kolejne przemyślenie, co jeszcze powinno być wymaganym polem. Jestem po spotkaniu z Anią. Abstrahując od przypadku Ani, bo nie chcę wszystkiego na jedną osobę zrzucać. Jest PBI czy bug, jest obsłużenie i jest jakieś rozwiązanie. Podam przykład. Dziewczyny muszą to przetestować. Są dwa podejścia, ale już napisałem kryteria akceptacji. I teraz pytam: "Gdzie ja to mogę przetestować, żeby nie pisać tego od zera?". Gdzieś mam to lokalnie. Można podejść do tego tak, że jak ja to zrobię po swojemu, to mogę znaleźć coś, czego deweloper nie przewidział. Zgadzam się. Ale jeśli chcę na to spojrzeć i na podstawie tego, że deweloper to testował, spojrzeć już na reguły, to jednak w pewien sposób to przyspiesza. Może obniża mój poziom czujności, bo korzystam z czyjegoś wytworu, ale jednak przyspiesza.

Teraz drugi scenariusz: robię to po swojemu, nie mamy zapisanego, gdzie ona to testowała, na jakich regułach, na jakim procesie. Mówię, że jest źle. Wraca to do niej do poprawki. Pytam Anię: "A gdzie to jest?". "Nie pamiętam, już nie wiem, czy to istnieje". Więc robi jeszcze raz testy od zera i traci czas. Mój postulat: przy przejściu z "In Progress" na "Internal Test" powinno być wypełnione pole, gdzie to testowano. Może tester z tego nie skorzystać, to pytanie do dziewczyn, czy chcą na to patrzeć po swojemu, ale powinno być zapisane: "przetestowane na `ania.amodit.local` na procesie takim i takim". Bo jak będzie robić poprawkę do tej poprawki, bo tester powiedział, że jest dalej źle, to już ma jakiś przypadek, który wcześniej robiła, a nie robi od nowa albo szuka go nie wiadomo gdzie. Rozumiecie, o co mi chodzi?

**Janusz Bossak**: Tak.

**Damian Kaminski**: Tak to teraz wygląda. Jeden przypadek przetestowałem, mówię do Ani, a ten drugi gdzieś jest na środowisku, ale nie wiadomo gdzie. Temat jest prosty. I teraz ja, żeby przyspieszyć testy, muszę tworzyć go od nowa albo szukać po omacku.

**Janusz Bossak**: Mam dzisiaj taki poziom wkurzenia, że nawet nie chce mi się wypowiadać. To z niczego nie wynika, po prostu mam taki dzień, że wszystko mnie drażni, jestem nerwowy i muszę się opanowywać, żeby nie powiedzieć za dużo, czego będę żałował.

**Damian Kaminski**: Jest proszenie: "popraw mi ten opis, to ja ci go zaakceptuję i go zrobisz". Wysłała mi. Pytam: "Gdzie ta poprawka?". "Tu". Mówię: "No to niestety, to są wytyczne do poprawki, jak ma wyglądać opis". Jak ja mam to zatwierdzić? Mogę wchodzić na jej środowisko, ale w zasadzie jakby mi to wrzuciła, to nie muszę wchodzić, tylko patrzę i mówię: "Dobrze, puszczaj". Mogę sprawdzić, czy na pewno się tak samo wyświetla, ale na poziomie designerskim. Chodziło o to, że nie dało się wyszukać po `null` i chciałem, żeby mi to opisała, jak już to przetestuje, to żeby napisała, jak to będzie działać, abym mógł ten przykład ocenić. Czasami ciężko jest się porozumieć.

**Janusz Bossak**: A teraz merytorycznie: nie da się wyszukiwać po `null`?

**Damian Kaminski**: Nie dało się, ale już się da, na razie na `internal`. Zostało to stworzone i sprawdzone pobieżnie, bo nie było przypadków biznesowych. Zacząłem używać funkcji `GetDataSet` produkcyjnie w WIM i wyszło sporo problemów. Nie dało się wyszukiwać po `null`. Jak `query` nie zwracało wyników, był błąd. Nie dało się też przypisać wartości z pola. Żeby zastosować `IS NULL` dla pola typu data, trzeba było robić tak: `if (pole_data == null) { warunek = "IS NULL"; } query = query + warunek;`. Powiedziałem Ani: "Czemu tak? Czemu system sam tego nie zrobi?". Nie muszę przed każdym `WHERE` sprawdzać dziesięciu pól. Jak pole jest puste, system ma wiedzieć, że to `null` i sam to podstawić.

**Janusz Bossak**: Zastanawiam się, jak tego wszystkiego uniknąć. To jest rola waszej dwójki w szczególności, bo ja już dawno przestałem się tym zajmować. Przez to, że macie mnóstwo innych zajęć, to się rozprasza. Jeśli przyjmiemy, że jesteśmy, a wy w szczególności, product ownerami, to naszym zadaniem jest tworzenie dobrych opisów z kryteriami akceptacji. Powinniśmy wspierać się AI, ale rozsądnie. Od nas zależy jakość pracy dewelopera. Deweloper powinien być zaangażowany w trakcie opracowywania, konsultować się, podpowiadać: "to jest bez sensu, zróbmy tak, bo wydajność...". Albo odwrotnie, deweloper będzie coś upraszczał, bo mu tak łatwiej. Pamiętam dyskusję z Piotrem o takim `query`. Mówił, że nikt tego nie będzie używał, bo jest koszmarnie skomplikowane. Ale na drugi dzień zrobił to tak, jak powiedziałem. To jest nasze zadanie.

Taka funkcja wymaga rozwoju, na przykład o obsługę `null`, o której mogliśmy nie myśleć na początku. I tu wracam do MVP. Musi być wersja MVP, która opisuje, co to będzie robić. Nam ciągle tego brakuje.

**Damian Kaminski**: Czemu to pominęliśmy? Bo dopiero teraz zacząłem tego używać na potrzeby biznesowe. Po pierwsze, to był uproszczony tryb, podjęła się czegoś, co było bardziej opowiedziane niż spisane. Po drugie, nie był określony motyw, jak będziemy z tego korzystać. To nie była realizacja konkretnej potrzeby, tylko przygotowanie narzędzia. Dopiero jak potrzeba zaistniała, okazało się, jakie mamy braki. Tych warunków brzegowych nie zawsze da się przewidzieć. Najlepiej jest od razu podać przypadek użycia, wtedy może to poskutkuje zastanowieniem się, czy na pewno będziemy mogli to zrealizować. Ale i tak na koniec może się okazać, że funkcjonalność działa, ale na danych klienta nie, bo nikt nie przewidział, że będą takie dane. Tego nie wyeliminujemy do zera.

**Kamil Dubaniowski**: Żeby wyjść z czymś z tego spotkania, wróciłbym do przypisania zespołów do tematów, które musimy zrealizować w najbliższym sprincie. Od tego zacznijmy. Jak będę wiedział, co jest moje i jakim zespołem to robię, to na razie w trybie awaryjnym, póki nie mamy zapasu dla deweloperów, rozpiszemy feature, rozpiszemy PBI pod nim. Trochę nam to zbuduje WIP na najbliższy sprint. Mamy tydzień. Lepiej zrobić podstawy, niż robić tak jak teraz.

**Janusz Bossak**: Dla mnie ważne jest, żebyśmy pracowali projektowo, bo to przynosi efekt. I żeby ludzie mieli cel. Nie tak, że "ktoś nie ma roboty, to damy mu to". Chcę, żeby był zespół, nawet wirtualny, i miał cel: "wy macie dowieźć komunikator w tym terminie, koniec". "Dowieźć" powinno być zdefiniowane w `definition of done`: co komunikator ma zawierać, jaki ma mieć opis, jak ma być instalowany, dokumentacja dla wdrożeniowca itd.

**Kamil Dubaniowski**: Jestem za. Jak będę miał projekt, rozpiszę feature, rozpiszę PBI, jestem w stanie z tego wypracować `definition of done`. To gwarantuje, że mamy zadania na backlogu. A teraz, jak planujemy sprint, nie ma zadań i wrzucamy, co jest. Damian, wróćmy do tego Excela, dodałem tam kolumnę "Zespół".

**Damian Kaminski**: Dobra. Jeszcze raz dopytam. Kamil, mówiłeś, że nie da się wyczyścić pola daty. Zerknąłem, faktycznie tak było na starym. Ale to chyba problem. Każde inne pole mogę wyczyścić. Jak tu skasuję i spróbuję zapisać, mam błąd.

**Kamil Dubaniowski**: Może powinien być jeden komponent do wyboru daty i czasu, a nie dwa osobne.

**Damian Kaminski**: Jak używam kosza, powinien on mieć odniesienie do całości.

**Kamil Dubaniowski**: To nie będzie intuicyjne. Jak widzisz tylko wybór daty, nie spodziewasz się, że wyczyści też godzinę.

**Damian Kaminski**: Rozumiem, ale dzisiaj nie ma żadnej możliwości. To minimum, bez zmiany interfejsu. Trzeba móc wyczyścić pole. Tak samo tu. Jak używam kosza, to chcę się tego pozbyć. Jak chcę zmienić, to wybiorę inne. Tu akurat kosz działa.

**Kamil Dubaniowski**: Roadmapa. I lecimy zespołami, podzielmy to.

**Damian Kaminski**: Coś jeszcze pytaliście, jak ja pracuję?

**Kamil Dubaniowski**: To ustalimy na koniec. Gwarancją, że mamy rozpisane PBI, będzie praca na backlogu. Ważniejsze jest zadanie niż opis projektu.

**Damian Kaminski**: No dobrze. Mariusz.

**Kamil Dubaniowski**: Mariusz.

**Damian Kaminski**: Do backendu mogę wziąć Anię, która jest dostępna. Piotr i Adrian są zajęci.

**Kamil Dubaniowski**: Nie liczyłbym, że cokolwiek ruszą w tym sprincie.

**Damian Kaminski**: Ania mogłaby, bo to, co robi, jest do skreślenia ad hoc. Nie jest potrzebne.

**Kamil Dubaniowski**: Bugi wolałbym, żeby poprawiła.

**Damian Kaminski**: A napisałeś do niej? Bo ona nie robi bugów. Zapytałem ją, co robi, powiedziała, że tłumaczenia. Trzeba jej dać coś, co przyniesie wymierne korzyści teraz.

**Kamil Dubaniowski**: Dobra, wpiszmy Anię, zobaczymy, jak to wyjdzie.

**Damian Kaminski**: Ja bym chciał Adriana. Co jest dla nas MVP 1 dla aplikacji Szafir na macOS? To, co pokazał Adrian, prototyp wyglądu, jest napisany w czymś nowszym niż React. To to samo, co mamy, tylko po nowemu. U niego to było na pół ekranu. Nie może tak wyjść produkcyjnie. Pytanie, czy potrzebujemy czegoś więcej? "Wyczyść certyfikat" to za dużo dla domyślnego ekranu, bo to opcja dla definiowania domyślnego certyfikatu.

**Janusz Bossak**: Co to znaczy "wyczyść"?

**Damian Kaminski**: Już pokazuję.

**Kamil Dubaniowski**: Stop, nie rozmawiajmy o tym. Będzie projekt przypisany. Chcesz go mi oddać, to ja będę robił spotkania i ustalimy.

**Damian Kaminski**: Tak.

**Janusz Bossak**: Dobrze.

**Damian Kaminski**: OK, tu masz wzór. Możesz to przejąć i dowieźć. Masz też Szafira, więc możesz testować. Powinniśmy wydać wersję prototypową dla klienta do testów, zanim uzyskamy certyfikację.

**Janusz Bossak**: Na czym polega uzyskanie tej certyfikacji? Czy to w ogóle możliwe?

**Damian Kaminski**: Z tego, co powiedział Adrian, tak. To tak jak na Windowsie, że pojawia się "niezaufany wystawca". Nie wiem, ile to potrwa.

**Kamil Dubaniowski**: e-Doręczenia chmura. Dopisz mnie tam.

**Damian Kaminski**: No tak, ale widzisz, przez to, że nie było tam kogoś z biznesu, deweloper nie czuje tego tak jak my. Tak jak z tą aktualizacją biblioteki – nie działa i nie wiadomo dlaczego. Nikt nie pomyśli "out of the box", żeby napisać do twórców.

**Kamil Dubaniowski**: To temat zupełnie niezaopiekowany. Łukasz przekazał mi analizę.

**Damian Kaminski**: Nie chciałbym się do tego deklarować. Może Łukasz powinien porzucić raporty i skupić się na tym.

**Kamil Dubaniowski**: Będzie potrzebny frontend i backend. Czekam na informacje od PM-a, na jaki zakres umawiają się z LOT-em do końca roku, bo muszą pochwalić się wdrożeniem. My negocjujemy, co realnie dowieziemy.

**Janusz Bossak**: Muszą wydać pieniądze, dowieźć sukces, a resztę zrobi się potem.

**Damian Kaminski**: Listę pól robisz z Filipem?

**Kamil Dubaniowski**: Z Filipem. Backend jest zrobiony.

**Damian Kaminski**: Jak będę robił KSeF, to mogę to zaopiekować.

**Kamil Dubaniowski**: Dodam cię do czatu z Piotrem, jest szansa, że to będzie po ich stronie, a po naszej ewentualnie funkcja do odczytu.

**Damian Kaminski**: Aha, czyli rozbudowanie połączenia. OK. Jestem w temacie KSeF, więc niech to zostanie w jednym miejscu. Tryb awaryjny jest po to, żeby dokonać płatności poza KSeF. Wdrażanie kogoś nowego będzie trudne.

**Kamil Dubaniowski**: Ten zielony temat to ja z Filipem. Już był ogarnięty w edytorze formularza.

**Damian Kaminski**: To jest skończone.

**Kamil Dubaniowski**: Tu Przemek i backend, nie wiem, kto ma robić.

**Janusz Bossak**: Czy robimy edytor diagramu?

**Damian Kaminski**: Ustaliliśmy, że to będzie beta do pierwszych testów.

**Janusz Bossak**: Kluczowe dla firmy to WIM i LOT. Reszta jest nieważna.

**Damian Kaminski**: Kamil ma prosty temat dla PKF, który Piotr wycenił na 2 dniówki, ja przekazałem 3, a to da 50 000 zł faktury.

**Janusz Bossak**: To natychmiast.

**Damian Kaminski**: Powinniśmy przejrzeć tablicę Piotra i ustalić priorytety.

**Janusz Bossak**: Co to za temat za 50 000?

**Damian Kaminski**: Przekazywanie plików przez API rzędu 2 GB. Piotr powiedział, że trzeba zrobić dedykowany endpoint. To jest 1-2 dni.

**Janusz Bossak**: I to wygeneruje 50 000 zł?

**Damian Kaminski**: To jest bloker dla rozliczenia o wartości 53 000 zł.

**Janusz Bossak**: A my z tego coś dostaniemy?

**Damian Kaminski**: W tym projekcie mamy 9 wolnych man-dayów. Możemy zażądać, żeby to było przeksięgowane na nas. Kamil zrobił coś wycenione na 21 dni w 15.

**Janusz Bossak**: Bardzo dobrze. Zróbmy to. Nie chcę, żebyśmy byli blokerami. Musimy przeglądać tablicę i patrzeć, na czym można zarobić. Edytor reguł czy diagramów może poczekać.

**Damian Kaminski**: Z raportami coś się zadeklarowaliśmy w umowie, ale jak zrobimy dwa, to przymkną na to oko.

**Janusz Bossak**: Ja się tym raportom przyjrzę szczegółowo.

**Damian Kaminski**: A jak nie, to zrobię raporty systemowe na ich środowisku i nawet nie będą wiedzieć, czy to systemowy, czy zrobiony przeze mnie.

**Janusz Bossak**: Dokładnie.

**Kamil Dubaniowski**: Trzeba dobrać zadania, bo nie wszyscy deweloperzy są zaopiekowani. Dla Przemka na przykład nie mam nic nowego.

**Janusz Bossak**: A co nam zostaje z modułu raportowego? Przemek jest od Reacta, moduł jest w React.

**Damian Kaminski**: Można tam coś znaleźć. A co z repozytorium? Skoro będziemy je obsługiwać na nowo pod kątem backendu, to frontend może też powinien się zmienić od razu.

**Janusz Bossak**: Tego starego repozytorium nie dotykamy. Robimy nowe.

**Damian Kaminski**: Poczekaj, bo to jest JRWA. To jest repozytorium. To, co robiliśmy LOT-owi na prezentacji, jest oparte o nasze stare repozytorium, tylko nie spełnia wymagań.

**Janusz Bossak**: Musimy to przedyskutować. Wolałbym mieć jedno repozytorium, a nie dwa.

**Damian Kaminski**: Ale to, które ja planuję, to repozytorium plików, ono nie ma odniesienia do spraw.

**Janusz Bossak**: Wiem, wiem, tak chce Murawski. Głupie repozytorium. To jest robota, nad którą powinniśmy siedzieć i gadać.

**Damian Kaminski**: Dlatego nie chciałbym się skupiać na przypisywaniu tu rzeczy nieistotnych.

**Kamil Dubaniowski**: Zaczęliśmy od tego, że każdy ma mieć cel. Nie mamy celu dla Piotra Buczkowskiego ani dla Łukasza.

**Damian Kaminski**: To nie jest tak, że nie mamy. Tu nie jest wszystko spisane. Trzeba wziąć tablicę Piotra i to uzupełnić.

**Kamil Dubaniowski**: Sporo tematów, które zdefiniowaliśmy, jest już skończonych albo zaraz będzie. Adrian zaraz nie będzie miał celu.

**Damian Kaminski**: Jak nie ma? Przecież ten Comarch Hub jest wpisany.

**Kamil Dubaniowski**: Nie mamy go tu na roadmapie.

**Damian Kaminski**: No nie mamy. To trzeba dopisać. Wiemy kto? Łukasz.

**Kamil Dubaniowski**: Ja nie wiem, o co chodzi.

**Damian Kaminski**: Łukasz. To nieduży wysiłek, ale to jest praca. Integracja z Comarch Hub jest wyceniona na 18 000 zł. Może to być cały tydzień pracy dla Adriana. Adrian ma też dokończyć SignApp, to z tobą może dokończyć, a ja czekam. Trzeba najprościej jak się da zrobić ten wygląd. To się staje krytyczne, bo w grudniu musimy to mieć, a jeszcze trzeba przetestować.

**Kamil Dubaniowski**: OK, Adrian jest opakowany. Marek?

**Damian Kaminski**: Marek cały ten tydzień robi, później jest wolny. Może to robić też Marek. Dobra, wróćmy do Piotra.

**Kamil Dubaniowski**: Wydaje mi się, że to, co Marek robi teraz, skoro zajmuje cały sprint, też powinno być na roadmapie.

**Damian Kaminski**: Masz rację. Dodawanie dokumentów do blockchain. To są kwestie bezpieczeństwa, coś się wykrzacza na produkcji. Piotr mówił, że trzeba to pilnie zaopiekować.

**Janusz Bossak**: Mówisz o tym blockchainie? Wiem.

**Damian Kaminski**: Jest jakiś wyścig, bo są dwa serwery i coś się krzaczy.

**Janusz Bossak**: Krytyczne w tym sensie, że tak, ale to się daje naprawiać. Tych błędów występuje kilka na kwartał i Marek to naprawia ręcznie.

**Damian Kaminski**: Tylko w zeszłym tygodniu Rossmann w jeden dzień puścił 10 000 dokumentów do Trust Center.

**Janusz Bossak**: To zwiększa prawdopodobieństwo wystąpienia takich błędów.

**Damian Kaminski**: W jeden dzień przebili 10 000, więc grubo. Kwestia, ile my na tym zarobiliśmy, to już drugorzędne.

**Kamil Dubaniowski**: Mariusz. JRWA. Nie wiem, czy to nie powinien być główny cel dla niego.

**Janusz Bossak**: Tak, JRWA.

**Kamil Dubaniowski**: Jak nie mamy celu dla Marka... może JRWA?

**Damian Kaminski**: Ale teraz rozpisaliśmy, że JRWA robi Piotr.

**Kamil Dubaniowski**: Tylko pierwszy krok. A interfejs?

**Janusz Bossak**: Tak.

**Kamil Dubaniowski**: No to mamy cel dla Marka, idealnie pasuje.

**Janusz Bossak**: Zgadza się. Zgadzam się.

**Kamil Dubaniowski**: Zostaje Mariusz.

**Damian Kaminski**: Mariusz ma wzmianki.

**Kamil Dubaniowski**: Ale czy to jest...

**Janusz Bossak**: Wzmianki są ważne.

**Kamil Dubaniowski**: OK.

**Damian Kaminski**: To jest ważny temat, bo to jest coś, co nie działa i klienci to zgłaszają. Zgłosiła to Neuca i my. To się nie odświeża, są problemy, żeby to dobrze działało.

**Janusz Bossak**: To jest zadanie dla niego.

**Damian Kaminski**: Czyli Mariusz wzmianki, Marek JRWA, Łukasz...

**Janusz Bossak**: Comarch Hub.

**Damian Kaminski**: No tak, Łukasz Comarch Hub, zgadza się. A Piotr?

**Janusz Bossak**: Piotr ma te swoje rzeczy, które tam musi podokańczać.

**Damian Kaminski**: Ale to jest na ten tydzień.

**Janusz Bossak**: Nie, nie, nie, on tam ma tych rzeczy więcej.

**Damian Kaminski**: No ma, ale my teraz mamy je tu wypisane i zaraz po tym spotkaniu musimy wejść i ustalić, co jest ważne, a co nie jest ważne.

**Janusz Bossak**: Dobrze.

**Damian Kaminski**: To robimy my. A co z Anią?

**Kamil Dubaniowski**: Została z tymi tłumaczeniami, co nie jest w ogóle istotne. Dla niej miałem podgląd szablonów, to było na 15 dni.

**Janusz Bossak**: Podgląd szablonów to jest grubsza sprawa. Może na razie nie.

**Damian Kaminski**: Nie dawajmy jej tego. Ania powinna się skupić na repozytorium.

**Kamil Dubaniowski**: OK.

**Damian Kaminski**: Został Przemek i Filip.

**Kamil Dubaniowski**: Filip – lista pól i matryca uprawnień. Przemek – edytor formularza.

**Damian Kaminski**: No i mamy rozpisane. To teraz kwestia, żeby te wszystkie tematy znalazły się na roadmapie. I tyle.

**Janusz Bossak**: To teraz trzeba to wszystko wpisać i będziemy mieli jasność.

**Kamil Dubaniowski**: No, to jest to, od czego chciałem zacząć.

**Janusz Bossak**: Dobra, to kończymy.

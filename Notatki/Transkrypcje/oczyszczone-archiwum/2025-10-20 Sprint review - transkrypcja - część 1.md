**Data spotkania:** 20 października 2025, 07:03

---

**Przemysław Rogaś:** Moich zadań z formularza. Czy że nie pamiętam już – to było w tym sprincie, co w poprzednim? Dobra, to ja zacznę. Dla mnie diagram – funkcjonalnie tak, mamy tam wszystkie. Jak standardowo na tym navigatora coś się, coś nie działa. Zamek. Więc możemy dodawać etapy, możemy łączyć etapy. Dodać regułę. Możemy usuwać połączenia. Mamy kilka układów, możemy zmienić, gdzie jest pionowe czy poziomy sposób. Mamy układ hierarchiczny, hierarchiczny zwarty, to znaczy, że hierarchiczny zwarty to znaczy, że linie są połączone. Podstawowe to jest układ z biblioteki Dagre, czyli taki bardziej przypominający drzewo. No i ogólnie są tutaj przeniesione już wszystkie warunki z starego diagramu. Naj, działa to tak, jak powinno.

**Kamil Dubaniowski:** To ja będę ci podpowiadał, chyba że macie do tego jakieś pytania. Sobie odpaliłem zeszłych sprint i co tam w edytorze jeszcze byśmy powiedzieli. Na pewno w zeszłym sprincie pojawił się search po polach.

**Przemysław Rogaś:** O serwisie nie mówiłem – o tym – wyszło w sprincie.

**Kamil Dubaniowski:** Nie, chociaż nie wiem. Jest, jest w czterdziestym pierwszym jako Done zaznaczony, więc możliwe.

**Piotr Buczkowski:** Pokój w nazwie pola też.

**Kamil Dubaniowski:** To dodałem na ten sprint zgłoszenia, tak, tak jak tam sugerowałeś – jeszcze tego nie robiliśmy. W piątek pisałem zgłoszenia dopiero.

**Janusz Bossak:** No i podziały, podziały widzę, że już zniknęły. To kreski na hover – combo pojawiają bardzo.

**Kamil Dubaniowski:** Tak, zniknęły, zniknęły, powiedzmy.

**Janusz Bossak:** Dużo lepiej.

**Kamil Dubaniowski:** W tym momencie dopiero na, właśnie na hover lub na, na drag – lub dopiero jak trzymasz jakieś pole i przeciągasz, to pojawiają się w momencie, kiedy najedziesz pomiędzy wiersze.

**Janusz Bossak:** Bardzo dobrze, dużo lepiej.

**Kamil Dubaniowski:** Tak.

**Przemysław Rogaś:** W praktyce teraz jest trochę ciężej, nie?

**Kamil Dubaniowski:** Z tych.

**Przemysław Rogaś:** Wjechać na to.

**Piotr Buczkowski:** To chyba nie ma, bo to jest 3-kolumnowa, przy tym szerokości się do 2 zjechała.

**Kamil Dubaniowski:** 3-kolumnowy. Zawinę.

**Przemysław Rogaś:** Tak, no to też właśnie była zmiana w tym względzie, że to wyglądało – jak na sprawie jest ograniczona długość pola. 500 pikseli.

**Kamil Dubaniowski:** Rzecz, która też się zmieniła, to ujednoliciliśmy ikony. Tutaj, jak jest na przykład – jest pole Użytkownik, to na formularzu ostatecznie była inna, inny kolor i inny rozmiar versus tu, z tego co widzę, jako Done oznaczone. Więc po prostu też pracowaliśmy nad tym, żeby ten edytor zbliżyć jak najbardziej do wyglądu realnego formularza.

**Barbara Michałek:** Trochę jeszcze były pola zablokowane, tak, że na przykład jak mamy proces Kompanii SS, to możemy zablokować pola do edycji. Te były też chyba w tym sprincie.

**Kamil Dubaniowski:** Tak, tak, plus pole statyczny tekst było poprawiane. Jego edycja, to też możesz. Czyli były zgłoszenia co do wielkości tego okna. Tutaj jeszcze Jan Piotr zauważył właśnie tą pierwszą opcję wyboru, że trzeba poprawić. To też zgłosiłem – dla każdego języka, dla którego nie zdefiniowano nazwy, nie tyle nazwy, a samego tekstu, bo w tym momencie jesteśmy w edycji tekstu, ale to już takie szczegóły. Natomiast samo okno jest już większe, podobnych rozmiarów, jak mieliśmy do tej pory.

**Barbara Michałek:** No i chyba też to, że teraz w edytorze się wyświetla ten tekst, bo wcześniej się nie wyświetlał. Teraz tutaj w podglądzie też się wyświetla, to też było zmieniane.

**Kamil Dubaniowski:** Tak. Tak, pracowaliśmy nad tymi polami, które właśnie chociażby statyczny tekst, czyli to, co faktycznie w nim mamy wpisane, już nam się wyświetla w podglądzie formularza. I sama nazwa chyba pola statycznego nie była wyświetlana, teraz ją wyświetlamy, ale z informacją, że na docelowym formularzu ona jest niewidoczna. Takie niuanse, tak. I mamy kolejną listę zadań na ten sprint – podobnych już zmian kosmetycznych w edytorze.

**Przemysław Rogaś:** Tutaj jeszcze była zmiana – było wcześniej nieintuicyjne usuwanie wyjątków poprzez tutaj X na selekcję, teraz jest obok przycisk.

**Kamil Dubaniowski:** No.

**Przemysław Rogaś:** Bardziej jest to widoczne teraz.

**Kamil Dubaniowski:** Jak ja w pierwszej wersji jeszcze, jaką mieliśmy w starym edytorze, no to wyglądało to w ten sposób, że trzeba było z listy wybrać. Usuń ten wiersz. Trzeba było rozwinąć listę i wybrać pozycję. Usuń ten wiersz, także już jest tak, jak używamy wszędzie indziej.

**Przemysław Rogaś:** Jeszcze coś, co dodaliśmy – właśnie Piotr zgłaszał taki komunikat o niezapisanych zmianach, jak chcemy wyjść. Jest tam anulować.

**Kamil Dubaniowski:** I tak, patrząc po sprincie to.

**Barbara Michałek:** Są jeszcze były chyba te pola Odnośnik, jeśli chodzi o zmianę. Właśnie źródła.

**Kamil Dubaniowski:** Tak, tutaj też będzie.

**Barbara Michałek:** Czekam tytułów – to też było. Zresztą sprincie.

**Kamil Dubaniowski:** Do tego też będzie zmieniana. W bieżącym 45 już jest rozpisana. Aktualnie wygląda to w ten sposób, że jeśli chcemy zmienić źródło w polu Odnośnik zewnętrzny, wewnętrzny lub Słownik, no to trzeba przejść przez tą edycję i zaznaczyć. Tylko, że akceptujemy, bo jeśli zmieniamy źródło w odnośniku lub słownik podmieniamy na inny, no to jest jakby 100% szansy, że dane się utracą, no bo nie będą się pokrywały ID w sprawach, więc w ten sposób to się już teraz da zrobić. I w przyszłym sprincie jest do tego zaprojektowana zmiana, bo tu dojdzie kolejna opcja przy tym polu – przejścia do tego źródła. To zgubiliśmy w nowej wersji, czyli jeśli mam wybrany słownik, nie wiem, MPK, to będzie jeszcze link do tego słownika obok właśnie tego pola. Tam w tle widać plany, jakiś słownik czy źródło X. No to z tego poziomu będzie szło łatwo przejść do tego źródła i w starej wersji mieliśmy to tylko przy słownikach. Dla nowej rozpisałem to też, żeby łatwo z tego poziomu przejść do procesu, który jest podpięty, bądź rejestru i tak samo do źródła zewnętrznego, które jest tu podpięte, żeby szybko przejść do jego edycji z tego poziomu. Ale to już przyszły sprint. OK, to chyba tyle, chyba że Przemek jeszcze coś ci przyszło.

**Przemysław Rogaś:** Te pola zablokowane – w tym, że teraz coś. Nie mogę zmienić.

**Kamil Dubaniowski:** Może znajdź ten rejestr Kompanii, są – powinien też być. Jest chyba na każdej instalacji.

**Przemysław Rogaś:** To znaczy, to mam wyszukać?

**Kamil Dubaniowski:** Kompanii, tutaj pisz chociaż. Tu też rejestry powinny być widać, tak, ten pierwszy.

**Przemysław Rogaś:** Więc tak, w przypadku pól zablokowanych mamy tutaj ikonkę i jest tutaj kłódka. Nie możemy otworzyć żadnego z ustawień, tutaj wszędzie, gdzie nie możemy zablokować, to jest też.

**Kamil Dubaniowski:** Czyli można de facto zmieniać sobie tylko nazwę wyświetlaną i podpowiedzi. OK. To, co? Chyba wszystko.

**Przemysław Rogaś:** Dzięki.

**Kamil Dubaniowski:** Dzięki. Filip, czy chciałbyś pokazać nam tę listę pól nową?

**Filip Liwiński:** Tak, pewnie już wstępnie.

**Kamil Dubaniowski:** OK. Czyli do tej pory w edytorze formularza Przemek pracował nad tym edytorem graficznym. Filip w poprzednich sprintach realizował tą matrycę uprawnień. I w tym sprincie rozpoczęliśmy także – to jest dopiero pierwszy sprint, gdzie nad tym działamy – odtworzenie i zmiany w tej liście pól, czyli nowy wygląd listy pół. W tym momencie wygląda to już tak. Też głównym celem – może ja dopowiem, zanim Filip jeszcze zacznie opowiadać – tej listy w tym momencie, kiedy głównym miejscem edycji formularza ma być edytor. Na ten moment lista de facto służy do takiego szybkiego przeglądu. Jakie pola mam plus? Łatwa możliwość wprowadzania nazw wyświetlanych w różnych językach i również ta nazwa domyślna, czyli troszeczkę wychodzimy z tej zakładki tłumaczenia. Przenosimy to na tą listę edytora formularza. Żeby robić to z tego miejsca. Tu też od razu dobrze widać, która nazwa jest już zdefiniowana, a która jest dziedziczona, czyli jeśli dla nazwy domyślnej ustawiłem wartość test, to ona jest ciemna. Po prostu czarna, natomiast szara jest wskazaniem, że ta nazwa jest dziedziczona z domyślnej, czyli tutaj dla języka polskiego będzie się wyświetlało test, ponieważ domyślna jest test, ale na przykład dla angielskiego jest już jakaś ustawiona i zerwano to dziedziczenie i podobnie jest dla nazw systemowych, technicznych – jeśli domyślnie jest w ogóle ustawiona, to widać, że wszystko jest dziedziczone z nazwy systemowej. OK, chwilę poddaję głos. Widzę, że Damian już się pojawił.

**Filip Liwiński:** Tak, tak.

**Damian Kamiński:** A jeśli chodzi o przesuwanie, to jak to tu wygląda? Teraz w sensie ustalenie?

**Kamil Dubaniowski:** Nie, nie robiliśmy, nie robiliśmy jeszcze.

**Damian Kamiński:** Jeszcze na razie nie, OK.

**Filip Liwiński:** Tak i tłumaczenia można rozwijać tutaj w nagłówku kolumny przez kliknięcie ten przycisk. Sekcje – właśnie domyślna, polski, angielski i niemiecki to zdefiniowane w aplikacji, tak samo dla podpowiedzi. I nazw systemowych można edytować inline szybką edycję. Tak samo typ poprzez okno modalne – jest tam ten sam model, co w edytorze graficznym. Indeksem, nazwy, tłumaczenia, wszystkie też można edytować inline. I też można ukrywać widoczne kolumny, jak ktoś chciał któryś nie widzieć – tak samo słowo – jest funkcją przywrócenia domyślnych. I też szukanie po polach. Jest podświetlane – na całej komórka jest podświetlana i po najechaniu podświetlenie. I to jeszcze – tabele rozklaszowane do danego. Przykład – w tym mamy skutkiem awarii. Może nie to, czy powołano kontrolę wolnego sprawować.

**Kamil Dubaniowski:** No i to też jest zmiana względem starej listy, że tutaj nie trzeba się przełączać między widokiem formularza głównego a tabelami. Wszystko jest jakby na jednym widoku zagnieżdżone, tak jak to zrobiliśmy w matrycy uprawnień, żeby utrzymać tą zasadę, a tak będzie łatwiejszy przegląd przez cały formularz, jakie mamy pola, jakiego typu i wewnątrz tabeli, poza tabelami.

**Janusz Bossak:** Te ikony pól są identyczne.

**Piotr Buczkowski:** Może jakoś?

**Kamil Dubaniowski:** A tu też już tak mam.

**Piotr Buczkowski:** Różnic to tabela bardziej.

**Kamil Dubaniowski:** No jest trochę problem, bo zaczyna nam się to wtedy gubić pośród sekcji, więc jeszcze coś pokombinuję. Może jakaś ikona, ale tak – te typy. Jeszcze chyba się nie pokrywają, ale powinny.

**Filip Liwiński:** Nie, tak już się pokrywają.

**Kamil Dubaniowski:** Ten statyczny tekst trochę mnie – OK, bo ja zmieniałem ikony też, ale to na przyszły sprint. Rozpisałem zmianę tych ikon, bo używamy chociażby tej korony dla dokumentów, która jako jedyna jest wypełniona, wszystkie inne to są outline. Dodaj – czas też jest wersja outline, nowa – to wszystko po zgłoszeniach, że jeszcze będą zmiany, ale to ogólnie w edytorze graficznym też używamy złych. One, Janusz, mogą wyglądać inaczej, bo są chyba dużo ciemniejsze. Ja też pamiętam waszą uwagę gdzieś z pierwszych prezentacji do tego graficznego, że on po prostu jest zbyt czarno-biały i cały czas zastanawiam się, czy nie wrócić do koncepcji Kristiny, żeby typy pól oznaczać jednak konkretnym kolorem, czyli na przykład wszystkie tekstowe, nieważne czy walidowane, czy nie, czy jakieś tam listy wyboru – innym kolorem, żeby jednak trochę się od siebie różniło, się od samego efektu, czyli od formularza, który jest gdzieś tam na środku ekranu, a te wszystkie pola nam się zlewają w tym jeden. Jeden ekran, a na edytorze dzieje się dużo więcej niż tutaj, więc tam przeprowadzenie tych kolorów moim zdaniem jak najbardziej ma sens.

**Janusz Bossak:** Kolor kolorem, ale tak patrzę tam, nie wiem – tekstowe, długi tekst – jak ktoś ma taką. Niż, chyba to na graficznym edytorze. Jakoś tak.

**Kamil Dubaniowski:** Nie, tylko samo jest.

**Janusz Bossak:** Dobrze, jakoś tak klikalne.

**Kamil Dubaniowski:** Tak, tak, tak.

**Damian Kamiński:** Czy może warto wprowadzić przynajmniej kolorowe ikony i to porównać?

**Kamil Dubaniowski:** Tak, bo to mi chodzi. Może przełączyć na chwilkę na edytor? Wiem, że to Przemka, ale chciałbym jakby poruszyć ten panel, tak, z wyborem – to ta sama ikona, tylko chciałbym, żeby ten panel właśnie tutaj jakoś troszeczkę odciąć od samego formularza, który jest w środkowej części ekranu. I jak klikniesz na jakieś pole na formularzu, to wyświetla się ten prawy panel i w tym prawym panelu też te sekcje. Chyba wypadałoby pokolorować, tym bardziej, że Piotr tutaj zasugerował, żeby domyślne ustawienia były też rozwinięte i trochę mi się wydaje, że jak to porozwijamy do domyślnej, to co się zacznie – wszystko zlewać, nie będzie tak już czytelne, co jest sekcją, a co jakimś wyborem. Tu jeszcze tego mało, tak, ale na ustawieniach na przykład tabeli, gdzie tego jest mnóstwo. No to te ostatnie 2 sekcje już stają się pomijane, niewidoczne właściwie, a są istotne też.

**Piotr Buczkowski:** Znaczy. Jak tak klikałem to. Znacznie mniej wykorzystywane jest podpowiedź czy wartość domyślna niż to, co jest w ustawienia pola.

**Kamil Dubaniowski:** No wiesz, będziemy w tym sprincie pewnie nad tym myśleć. Dobra, chyba tyle.

**Filip Liwiński:** Dzień dobry.

**Janusz Bossak:** Dzięki bardzo.

**Piotr Buczkowski:** To ja mogę pokazać coś, co było źródłem wielu zgłoszeń moich.

**Damian Kamiński:** Proszę.

**Piotr Buczkowski:** Dałem dokładniejszą walidację pól przy. Przy imporcie XML, tak, żeby może system nie pozwalał przynajmniej. Bardziej ostrzegał przed zmianą powodującą problemy typu gubienie danych czy wręcz błędy w zapisie spraw. Do tej pory były tylko tak naprawdę te 3 ostatnie walidowane. Dodałem 4 inne, tak, które po części wynikają z tych 3 ostatnich. No ale nie wszystkie. Stąd właśnie też moje te tam zgłoszenia dotyczące wyszukiwania. Pokój – idzie wyszukiwania po polu, bo chociażby to, co pomaga w testowaniu – w tym przypadku trzeba na teście czy na deweloperskim znaleźć to pole i wprowadzić jest tym, co mamy na produkcji.


**Data spotkania:** 4 grudnia 2025, 12:02 - część 2

---

**[Przemysław Sołdacki]:** Janusz, ja się zastanawiałem nad tym, bo to u innych klientów też jest taka sytuacja, gdzie jest proces i on na każdy rok jest inny – że tam „Wniosek o coś tam 2025” albo „2026”. I to zakończenie... czy nie byłoby dobrze zrobić tak, że jak ucinamy, to zostawiamy ostatnie słowo?

**[Janusz Bossak]:** Wiecie, no tak robimy z nazwami plików wyświetlanych w sprawach. Jak nazwa pliku jest długa, to tam jest technika taka, że zostaje kilkanaście znaków pierwszych, kilkanaście znaków ostatnich, a w środku są kropeczki. Czyli coś, coś, coś, kropeczki i końcówka.

**[Przemysław Sołdacki]:** Właśnie, to mogłoby mieć sens. I to nawet by nie znaków, tylko po prostu słów, bo jakby to ostatnie słowo może być kluczowe.

**[Janusz Bossak]:** Wiecie co, ja myślę, że ta propozycja, żeby to się tutaj zajmowało więcej wierszy – ale tak w sposób wyśrodkowany, czyli jakby były 3, to żeby ta „Elektroniczna akceptacja materiałów promocyjnych” lekko poszła do góry i ten trzeci wiersz posłanek... żeby to zawsze było wizualnie wyważone.

**[Daniel Reszka]:** Mhm.

**[Miłosz Śliwiński]:** Tak, tym bardziej, że na przykład ja nie mam problemu z tym, jak damy limit znaków. Czyli to o czym rozmawialiśmy, że byłoby ustawione, że nie wiem, nazwa może mieć określony limit znaków i trzeba sobie w tym zarządzić. Bo to też dla nas jest dobry punkt wyjścia, że my przyjmując te procesy do realizacji, to od razu wiemy, że ta nazwa może być skończona. I żeby tam inwencja twórcza biznesu nie była zbyt płynna.

**[Janusz Bossak]:** No to jest większy problem, bo my mamy taką zasadę tej kompatybilności wstecznej. Skoro daliśmy kiedyś, że to ma być te 255 znaków, a teraz te 255 znaków nie mieści się na ten kafelek, to nie chciałbym ograniczać możliwości, żeby były nazwy krótsze tylko dlatego, że się na kafelkach nie mieszczą.

**[Miłosz Śliwiński]:** No ale to pytanie, czy właśnie wtedy jak mamy te 255, to możemy przyjąć, że po prostu czcionka się zmniejsza, ale nazwa jest pełna?

**[Janusz Bossak]:** No nie, zmniejszanie czcionki to też nie jest UX-owo dobry pomysł. Ale okej, słuchajcie, ja myślę, że mamy według mnie co najmniej dwie propozycje tutaj. Jedna to taka, że dodajemy więcej wierszy, czyli jeżeli nazwa jest dłuższa, to się będzie zawijać. Pewnie 4 wiersze powinny być wystarczające. Jeżeli by nie były, to możemy pójść w ten pomysł, który tu Przemek rzucił, czyli robienie w środku jakichś 3 kropek – pokazywanie maksymalnie co się da z przodu i maksymalnie co się da z tyłu, a środek wycięty. I trzecia możliwość, tak jak jest teraz, że zostawiamy jednak na końcu 3 kropeczki, a treść pozostaje w tooltipie. No jak już ktoś będzie miał tak strasznie długą nazwę... no to trudno, niech biznes robi krótsze nazwy, albo niech te rzeczy istotne umieszcza na początku.

**[Przemysław Sołdacki]:** Janusz, ale możemy taki też zrobić: jeśli mamy 255 znaków, to możemy wpisać nazwę na 255 znaków i zobaczyć, czy to jeszcze by dało radę jakoś wyświetlić. No to jest taki skrajny przypadek, ale żebyśmy na w czasie testowania kamieni...

**[Janusz Bossak]:** Zobaczymy. Tu jest ile... raz, dwa... 10... tylko 30 jest w jednej linijce, tak pi razy drzwi.

**[Daniel Reszka]:** 255 to za dużo chyba będzie.

**[Janusz Bossak]:** To jest już taki naprawdę skrajny przypadek.

**[Miłosz Śliwiński]:** Ja tak strzeliłem 255. Nie wiem, tylko tak przyjąłem, bo w ustawieniach bazodanowych aplikacji dla pola tekstowego standardowo jest 255. Może być też to długie pole i wtedy nie ma limitu znaków.

**[Janusz Bossak]:** Nie, tu jest chyba limit na samym polu, tym do wpisywania nazwy. A to chyba o ile pamiętam ma 150 według mnie, ale mogę się mylić. Też nie pamiętam takich szczegółów.

**[Daniel Reszka]:** Znaczy, myślę, że to trzy-linijkowe rozwiązanie będzie już okej. No bo to raczej rzadko będzie większa, a jak większa, to myślę, że powinno być to, co właśnie Przemek powiedział – że nie 3 kropki na końcu, tylko 3 kropki w środku: 2 pierwsze linijki, 3 kropki i 2 ostatnie linijki? Jakoś tak to dzielić, ale pełna nazwa dalej powinna zostać.

**[Janusz Bossak]:** Tak, tak, zdecydowanie.

**[Daniel Reszka]:** No i to jest chyba wtedy rozwiązanie takie na każdy temat, bo masz początek, koniec i masz tooltip. A w tę ilość znaków to chyba nie ma co się tutaj zagnieżdżać.

**[Janusz Bossak]:** Dobra.

**[Miłosz Śliwiński]:** No dobra, no to tę kwestię mamy omówioną.

**[Daniel Reszka]:** I jeszcze druga kwestia była. Mówiliście też, ewentualnie te procesy znowu wydzielić? Bo mnie to też bardzo boli.

**[Janusz Bossak]:** Tak, tak, to na pewno.

**[Miłosz Śliwiński]:** Bo to znacznie zaburza czytelność.

**[Janusz Bossak]:** Zdecydowanie tak.

**[Przemysław Sołdacki]:** Janusz, a a propos tych szerokości kafelków. No bo tak jak tutaj Daniel zauważył, że mamy... że przy mniejszym ekranie to się mniej kolumn pojawia, przy większym maksymalnie 6. No to chyba też nie jest jakiś w ogóle problem, żeby pozwolić, żeby się robiło więcej? Jak ktoś ma wielki ekran, to może być 10. To chyba też nie jest trudnym jakimś tam dużym problemem do przyjrzenia się i przetestowania, czy to w ogóle wiesz, jest lepiej czy nie.

**[Janusz Bossak]:** No dokładnie.

**[Daniel Reszka]:** Znaczy ja to już zgłaszałem, to już jest zgłoszone i było analizowane. To jest proste i wydawało mi się, że to jest zrobione, ale muszę zobaczyć, bo może to jest jeszcze na testach albo niepodjęte po prostu. Bo to było analizowane z Kamilem nawet i tam jest po prostu ustawiony maksymalny parametr, a nie powinno go być. Ilości kolumn. Więc to jest na sztywno, więc wydaje mi się, że to też nie jest duża zmiana i zasadna. Ale to jak Janusz mówi, no bo on nie jest... ale wygląda nieestetycznie potem.

**[Daniel Reszka]:** Dobra. I czy do tego jeszcze coś mieliście tutaj? A jeszcze to pogrubienie czcionki, no ale to nie wiem, czy to może być konfigurowalne czy nie.

**[Janusz Bossak]:** O ile pamiętam, tylko na folderach było pogrubienie.

**[Daniel Reszka]:** Tak, tylko na folderach było, bo one z reguły nie mają dużej nazwy.

**[Janusz Bossak]:** No i dokładnie nam klienci zwrócili uwagę, dlaczego foldery są takie grube, a pozostałe procesy są nie? No i stwierdziliśmy, że w sumie racja.

**[Miłosz Śliwiński]:** Ja akurat co do wizualizacji w ogóle tych folderów i procesów to chyba Daniel masz tę propozycję? Tamte screeny, które wysłałem?

**[Daniel Reszka]:** Mam, to pokażę Januszowi potem, bo omawialiśmy to. Ale to jest cała przebudowa już jakby interfejsu, więc to nie jest dyskusja taka na teraz.

**[Miłosz Śliwiński]:** Jasne, wiesz, to tak jak mówię – tutaj nie w odniesieniu do tego, tylko w kontekście tym rozwojowym. Bo ja pamiętam, że też byłem zapraszany na te warsztaty UX-owe i ja parę takich usprawnień do wizualizacji tego systemu zgłaszałem. Mam doświadczenie z różnych źródeł i właśnie AMODIT jest bardzo fajnie odbierany. Natomiast największe zastrzeżenie jest do tego, że nie wygląda nowocześnie.

**[Janusz Bossak]:** Trochę się zmienia, trochę się zmienia.

**[Miłosz Śliwiński]:** Trochę się zmienia tak, no to prawda.

**[Janusz Bossak]:** No to znaczy, tak jak tu mówiliśmy w którymś momencie, to jest kwestia też gustu. Ale z wieloma klientami rozmawialiśmy i mówią: dla nas ważniejsze jest, że to świetnie działa. Tak? Trochę może tam wyglądać gorzej, to trudno, ale to świetnie działa i dużo lepiej od innych.

**[Miłosz Śliwiński]:** Dokładnie, to na pewno.

**[Janusz Bossak]:** Więc dbamy oczywiście o tę część wizualną, jak widać, zmieniamy powolutku. Będzie się też zmieniało całe zaplecze. Tamten kwestia edytora formularza, edytora diagramu, edytora reguł... ten obszar teraz intensywnie jest przebudowywany. Więc tam też będą zmiany. Tutaj te zmiany pewnie, o których za chwilę będziemy mówili, czyli na formularzu sprawy, też zostały dość mocno przebudowane. Tutaj to, co macie uwagi do ewentualnie pól wymaganych.

**[Janusz Bossak]:** Więc pewnie do tego zaraz przejdziemy. Także no zmienia się w AMODIT. Dużo tak. Zmienia się dużo wizualnie i też technologicznie, bo przechodzimy na Reacta. Więc w większości – oprócz może jeszcze mCase'a samego, czyli sprawy – to praktycznie wszystkie te rzeczy, które tutaj zmieniamy... no to też przy okazji przechodzimy na technologię. Już typowo rozdzielenie frontendu od backendu i tutaj jest to Reactowo wszystko robione.

**[Daniel Reszka]:** Mieliście jeszcze uwagę do tych dymków, że one coś zasłaniają?

**[Michał Mirończuk]:** Musiałbyś Danielu wejść w folder, bo właśnie widzę, że to sprawdzasz. To z naszej perspektywy może wyglądać zabawnie i banalnie, ale myślę, że z perspektywy użytkownika może być dosyć irytujące. Jak tutaj byś miał dymek, bo masz krótką nazwę, ale jak będziesz miał długą nazwę na pierwszym miejscu, to zasłoni ci strzałkę cofania.

**[Janusz Bossak]:** Dobra, dobre spostrzeżenie. To na pierwszy... foldery powinny być na dole, a nie znaczy dymki do dołu, a nie do góry, bo zasłaniają ten „Dodaj proces”. Znaczy odjechać na bok gdzieś? No tak, no jest to jakaś tam niedogodność.

**[Miłosz Śliwiński]:** No to chyba bardziej o cofanie nam chodziło nawet niż „Dodaj proces”, bo nie da się cofnąć tego widoku.

**[Daniel Reszka]:** Tak, no bo jak macie długą nazwę, jakby zasłoniło wszystko.

**[Janusz Bossak]:** Ważna uwaga.

**[Daniel Reszka]:** I dalej to są te pola wymagane. Czyli tutaj jakby ustalone tak, że tamte rzeczy są do zgłoszenia, do omówienia wewnętrznie i do przeanalizowania. No i teraz idziemy do tych pól wymaganych. To nie wiem, czy Janusz widziałeś, jest ta różnica? Że jakby kiedyś się bardziej rzucało w oczy, teraz mniej się rzuca.

**[Janusz Bossak]:** No ja wiem jaka jest różnica. Sam to projektowałem.

**[Daniel Reszka]:** No to teraz wypowiedzmy się jakby komentarzem do klienta, jak to zostało przeanalizowane.

**[Janusz Bossak]:** Znaczy to, co zostało zrobione i zaproponowane, jest i tak i tak kompromisem. Większość klientów nie chciała żadnych oznaczeń oprócz na przykład gwiazdki. Przy tym document type, że to jest najczęściej stosowany sposób, to jest tam czerwona gwiazdka w polu. I najlepiej, gdyby te pola nie świeciły na pomarańczowo. W ogóle można powiedzieć, że wynegocjowaliśmy, że jednak jakaś część tego pola będzie podświetlona na pomarańczowo, żeby jednak klientowi zwracać uwagę.

**[Janusz Bossak]:** Nowoczesne wszelkie UX-owe rozwiązania idą w stronę taką najczęściej, że to nie jest zaznaczane. Iż dopiero jak klient nie wypełni i próbuje coś przesłać, to wtedy mu się dopiero podświetlają te pola, których nie uzupełnił. Klient powinien z natury wiedzieć co ma uzupełniać. I zostawiliśmy to delikatne podkreślenie, żeby było wiadomo, które z tych pól jest absolutnie wymagane i nie przejdzie dalej bez wypełnienia.

**[Janusz Bossak]:** I uważamy, że jest to bardzo dobre, kompromisowe rozwiązanie. I bez szans – to od razu mówię z góry – na powrót do takiego żaru miast tego formularza, gdzie tam kilkanaście pól jest pomarańczowych. W tabelce na formularzu i tak dalej... no bo tutaj wszystko było pomarańczowe: nazwa, cała obwódka i jeszcze napis pod spodem „pole jest wymagane”. No to mieliśmy na to mnóstwo zgłoszeń. Mnóstwo po prostu. Nie wiem, no 70-80% naszych klientów wielokrotnie od długiego czasu nas bombardowało tym zgłoszeniem, że dlaczego to wszystko u was się tak na pomarańczowo świeci?

**[Miłosz Śliwiński]:** To ja akurat w tej kwestii... podejście, że biznes powinien wiedzieć co ma uzupełniać, to się nie zgodzę. Bo u nas są procesy, jest cała masa procesów takich, które często robią nowi użytkownicy albo robią to pierwszy raz. I dla nich to nie jest oczywiste. I nawet jak mają instrukcję, a proces jest złożony, wielopoziomowy, to uzupełnienie przez niego tego formularza nie jest takie oczywiste. I on często nie wie jakby co ma uzupełnić i oczekuje bardziej od samego procesu, że go poprowadzi za rękę.

**[Janusz Bossak]:** Ale to jest zupełnie inne zagadnienie. To jest w ogóle przejście na taki tryb Wizarda, tak? Który prowadzi i mówi: „uzupełnij to, uzupełnij to”.

**[Miłosz Śliwiński]:** No tak, w kontekście tego procesu to taka uwaga, dygresja. Natomiast jeśli chodzi o to podkreślenie... To pewnie jakbym dostał gwiazdkę, to wolałbym gwiazdkę niż to podkreślenie. Ta gwiazdka byłaby bardziej taka... Klienci zgłaszali i mnie przekonali, bo taki jest standard od form formularza i pewnie to jest okej. Samo podkreślenie dla mnie jest mało czytelne. Podoba mi się ta zmiana z tym powiadomieniem, które wyskakuje w górę, że tam jest informacja o tym.

**[Miłosz Śliwiński]:** Natomiast to podkreślenie jest mało czytelne i my na testach mieliśmy zgłoszenia od użytkowników. I ja wiem, że u nas to będzie dużym problemem przy takim wdrożeniu biznesowym, że to nie jest czytelne. Oni nie wiedzą, co mają gdzieś tam wrócić, przeklikać. A sam komunikat... ile pól? Jak dostaną, że jest 8 czy 80 pól wymaganych do uzupełnienia – a tak się zdarza – to cofnięcie się i klikanie, przeskanowanie po takim widoku (gdzie jest biały ekran) tego lekkiego niebieskiego, czy tego pomarańczowego podpisu, jest no nie jest intuicyjne.

**[Miłosz Śliwiński]:** Jeśli nie da się dostawić gwiazdki, a zostaje ta kwestia podkreślenia... Bo pytanie, czy możemy chociaż dostawić ten napis, że wymagane? Że pole jest wymagane w tym wariancie?

**[Janusz Bossak]:** Nie. Możemy czy...? Wiesz, możesz wejść do jakiegoś procesu gdzieś na testa, gdzie są takie pola wymagane?


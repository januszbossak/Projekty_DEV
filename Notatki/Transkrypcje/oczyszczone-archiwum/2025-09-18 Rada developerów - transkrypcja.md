**Transkrypcja**

18 września 2025, 08:01

**Lukasz Bott:**
Jesteśmy. Z listy na radach zostały rzeczy na bieżący sprint. Jak idziemy po kolei?

**Janusz Bossak:**
No.

**Lukasz Bott:**
Zmiany w komentarzu, chodziło o weryfikację działania funkcjonalności.

**Damian Kaminski:**
To przypisana jest do mnie. Ten sprint powinno być docelowo skończone.

**Lukasz Bott:**
A to jest.

**Damian Kaminski:**
To jest to, co omawialiśmy. Tylko nie skończyłem tego. Jest opisane w komentarzu.

**Lukasz Bott:**
Gdybyś powiadomienia, to jest z tymi powiadomieniami.

**Damian Kaminski:**
To było omówione, odepnij już to.

**Lukasz Bott:**
Stoją na Tobie. To stworzenie funkcji do komunikatów. Bardziej w tej chwili muszą robić taką rzeźbę HTML-a i tym podobne, pole statyczne. Chcieliby, żeby była funkcja, zestaw funkcji do tego.

**Damian Kaminski:**
Właśnie, czy moglibyśmy tak jak mamy set field alias danger, to tak samo set. Nie wiem, static czy set coś tam.

**Lukasz Bott:**
Nie, tutaj Create Callout, tak tutaj zasugerowali.

**Damian Kaminski:**
Ok, była propozycja, tak może być.

**Lukasz Bott:**
Ale znów to jest rozwój AMODIT. Mateusz Okoniewskiego może według zasady niech znajdzie sponsora na to.

**Janusz Bossak:**
Wiecie co, sponsor, ale to jest wygląd i to jest szybkość wdrażania. Często stosują takie rzeczy. Pytanie do Piotrka Buczkowskiego, czy w kontekście naszego mechanizmu reguł to jest w ogóle wykonalne, żeby tak to działało?

**Piotr Buczkowski:**
No tak.

**Janusz Bossak:**
Okej.

**Lukasz Bott:**
Na wynik duży to, że tworzą sobie funkcję, która.

**Piotr Buczkowski:**
Wróć do tego przykładu.

**Janusz Bossak:**
Rozumiem, że to jest tam powinno być static tekst, że pole static tekst równa się wynik tej funkcji.

**Piotr Buczkowski:**
Dokładnie tak chciałem zaproponować.

**Lukasz Bott:**
Ok, dobra.

**Janusz Bossak:**
Czy przed Create Callout tam jest jakaś nazwa typu?

**Piotr Buczkowski:**
Create Callout zwraca taki sprawdzalny, który możesz przypisać do pola typu static tekst.

**Lukasz Bott:**
Ok, dobra, dobra.

**Janusz Bossak:**
Tak, jak zresztą jest tam potem w tym niżej, info test jest właśnie.

**Lukasz Bott:**
Tak, tak.

**Damian Kaminski:**
Tylko ten Create Callout musiałby mieć 2 parametry, rodzaj z tych co tutaj i wartość, tak?

**Janusz Bossak:**
Tak, to jest ten komunikat.

**Piotr Buczkowski:**
Tekst i styl.

**Lukasz Bott:**
Tekst i który styl? Przy czym styl my narzucamy jako taki szablonowy, że w razie.

**Piotr Buczkowski:**
Tak, jedną z tych.

**Damian Kaminski:**
Chodzi o to, żeby bazować na tym, nie generować jakichś innych komunikatów, tylko że wszystkie były jednakowe. Teraz tylko czy to będzie działać w regule automatycznej?

**Lukasz Bott:**
Czy musiał w automatycznej?

**Piotr Buczkowski:**
Tak.

**Damian Kaminski:**
Tak jak teraz. Dobra. Co ty Łukasz? Zapytałeś czy potwierdziłeś się? Dlaczego?

**Lukasz Bott:**
Mniej to był. Szum.

**Damian Kaminski:**
Zapytałeś, dlaczego w automatycznej czy że w automatycznej?

**Lukasz Bott:**
Nie, nie potwierdziłem, że automatycznie.

**Damian Kaminski:**
Ok, dobra.

**Lukasz Bott:**
Nie, to nie ma sensu. Nie ma sensu, wręcz tak.

**Damian Kaminski:**
Nie, po prostu nie będzie to przypisane, tylko będzie się generować na bieżąco.

**Janusz Bossak:**
Ok.

**Lukasz Bott:**
Pod warunkiem, że tego komunikatu nie będą ciągnęli z jakiejś bazy danych.

**Janusz Bossak:**
Można dopisać do następnego sprintu. Dzisiaj tak mamy.

**Damian Kaminski:**
A kto zajmował się tymi komunikatami na stronie? Ania czy Mariusz?

**Kamil Dubaniowski:**
Na stronie przerabiała Ania. Tosty to nie rynek, to już dawno było. Ania, a później Mariusz to przejął, bo jeszcze były takie komunikaty pod formularzem, takie będzie nasze, że X pól wymaganych.

**Janusz Bossak:**
Obojętnie, Ania może, Kamil może.

**Lukasz Bott:**
Dobra, na przyszły sprint i nie dyskutuję mi tam.

**Damian Kaminski:**
Dobra, tylko trzeba tutaj napisać, jak to ma działać. Sugerowałeś Ty to Łukasz, poprawisz, żeby to było przypisanie do pola. Create Callout to przed powinno być zdefiniowane.

**Lukasz Bott:**
Dobry wynik, tak dobra.

**Janusz Bossak:**
Weź tam skopiuj z tego info test równa się tam niżej 3 linijki i tam postaw góry, że info test równa się i ten Create Callout. I to będzie wiadomo, że to.

**Janusz Bossak:**
Czyli musi być nazwa pola statycznego równa się create callout komunikat i rodzaj komunikatu.

**Lukasz Bott:**
Ta propozycja, być może. Jeszcze jedno dopiszę uwagę.

**Damian Kaminski:**
Ja bym w ogóle wywalił te ich tutaj to co oni tam wypisali, bo to nie jest poprawne. Jak zjedziemy w dół, to ustalmy może powinno się to wyświetlać według nas, bo tu rozmawialiśmy już o tym z Mateuszem, też z Kamilem, że to nie będzie się kończyć tak jak tutaj, tylko na pełną szerokość pola, szerokość kolumny.

**Kamil Dubaniowski:**
Tak, bo to zaraz znowu będzie wyglądało jak przycisk na pewno.

**Janusz Bossak:**
Pole na szerokość.

**Lukasz Bott:**
Czyli tak jak tutaj, na tym żółtym komunikacie.

**Damian Kaminski:**
Nawet nie żółty. Żółty też się nie kończy, gdzieś tam jest ucięty, tak jak niebieski. Oczywiście gdzieś tam paddingi jakieś muszą być.

**Janusz Bossak:**
Nie, nie, nie. To jest problem pola static.

**Lukasz Bott:**
Tak dokładnie.

**Janusz Bossak:**
Pole static teraz jest rysowane na całą szerokość formularza. Nie mamy czegoś takiego jak pole static w ramach jednej kolumny.

**Piotr Buczkowski:**
A chcemy mieć?

**Damian Kaminski:**
Tak.

**Janusz Bossak:**
Tak.

**Kamil Dubaniowski:**
No tak. Ale nawet jeśli, to zobaczcie, to powinno być na szerokość kolumny, żebyśmy nie dorobili sobie błędów, które i tak chcieliśmy usuwać, wyrównywać. Teraz zrobimy kolejne.

**Janusz Bossak:**
Dobrze, ale chodzi mi o to, że to są 2 zagadnienia. Jedno zagadnienie: w obecnym stanie, tak jak działa pole static, ten callout ma być na szerokość pola static, tak jak ten żółty tutaj. Koniec kropka, koniec zagadnienia. Drugie zagadnienie, odrębne zupełnie jest takie, że pole static obecnie ma tylko taką właściwość, że jest na całą szerokość formularza. I jeżeli tutaj Piotr mówi, że można by zrobić tak, że pole static mogłoby przyjmować szerokość jednej kolumny, to byłoby super, bardzo super i to jest bardzo.

**Damian Kaminski:**
Ale to powinna być opcja, tak?

**Janusz Bossak:**
To powinno być opcją. Pole static i ono jest w jednej kolumnie, tak jak tabelka może być wyświetlana w jednej kolumnie i to wdrożeniowo by się bardzo przydało.

**Damian Kaminski:**
Dokładnie. Dobra, zacznijmy od tego, żeby się wyświetlało na stałą szerokość, a potem będziemy dogrywać opcje.

**Lukasz Bott:**
Zrobiłem to tak. Najpierw tę funkcję, a tamto to jest drobne PBI powiązane z tymi jakoś.

**Kamil Dubaniowski:**
Ja bym jeszcze do tego dodał na rozwój trzecie, żeby w ustawieniach pola static dało się też tego użyć. Bo mogę mieć static, który się nie zmienia i jest.

**Damian Kaminski:**
Tak, bo jest instrukcją.

**Kamil Dubaniowski:**
Tak.

**Damian Kaminski:**
Tak też by mogło być. Ale to znowu, to niech będzie. To już trzecie. Na razie zrobią to sobie w regułach najwyżej tej instrukcji i tyle.

**Kamil Dubaniowski:**
Tak.

**Janusz Bossak:**
Program może być w regułach, tak.

**Kamil Dubaniowski:**
Dlatego mówię, na rozwój, ale żeby było. Bo dla klienta tak.

**Damian Kaminski:**
Będzie szybciej wtedy, tak.

**Lukasz Bott:**
Dobra, to ja też tam na spokojnie zanotowałem sobie na kartce. To po spotkaniu szybko to zmontuję. Jakie tutaj MVP? Na razie tylko dorabiamy tą funkcję i tak jak jest tu napisane?

**Janusz Bossak:**
Też tutaj tylko uzupełnienie, bo Kamil, chyba Ty mówisz o tym, co ja wczoraj też tam wrzuciłem, że to jest rzecz też do poprawienia. W tej chwili w nowym edytorze formularza dla pola static nie można wpisać w ogóle ładnego tekstu, tylko trzeba pisać całą tą rzeźbę div class colour i tak dalej, zamiast po prostu ładnie pisać w edytorze, tak jak kiedyś było, można było normalnie.

**Piotr Buczkowski:**
Dla pola static to by było, może być opcja, że display jako callout, tak?

**Janusz Bossak:**
Albo w ogóle od razu, że wpisuje tekst.

**Piotr Buczkowski:**
To sorry, to jest inaczej, bo tak nie można sterować. Dobrze, to można też do pola static dodać, że to jest callout, gdzie wpisujesz tekst i wybierasz styl, tak? Możesz też dawać static dynamicznie z reguły, różne komunikaty przepisywać z różnymi stylami, bo.

**Janusz Bossak:**
To właśnie jak tutaj.

**Piotr Buczkowski:**
Tak.

**Janusz Bossak:**
Dobra, to trzecie zagadnienie, czyli że właściwość pola static byłaby taka, że od razu mogłoby być uznawane za callout i tyle.

**Piotr Buczkowski:**
Że tutaj styl info danger warning, czy to tam jest jeszcze?

**Janusz Bossak:**
Ale to jest trzecie, jakby zagadnienie. Dobra, ok. To jedźmy dalej.

**Lukasz Bott:**
Znowu wraca jak bumerang. Nie wiem, ale to dasz. Więc nie odkryliśmy, ale to chyba miałeś odpisać, tak?

**Damian Kaminski:**
Tak, nie odpisałem. Po prostu jest napisane odepnij od rady i zostaw na mnie. To Janusz. To mam wrzucać jako, to jak? Teraz dla Mateusza, a przy okazji dopytam.

**Janusz Bossak:**
To nie jest do końca.

**Damian Kaminski:**
Nie jest to błąd, tak? Nie jest to hotfix, ale jeśli by powiedzmy nic nie miał, to wrzucać jeszcze.

**Janusz Bossak:**
Fix, pewna mała inne rzeczy.

**Lukasz Bott:**
Nie wiecie co, Damian? Ja myślę, że Gant to.

**Damian Kaminski:**
Dobra, nie. Dlatego pytam, dlatego pytam, czy to?

**Lukasz Bott:**
Jeżeli mamy klientów, którzy z tego korzystają, to jest garstka, pewnie.

**Janusz Bossak:**
W ogóle Ganta świetnie według mnie ma opanowanego Marek. Marek powinien takie rzeczy robić, ale tak jak powiedzieliśmy, to akurat nie jest jakimś konfliktem. I na razie tego tutaj. Nie, tak, nie zajmujemy się tylko tym. Mówimy o grupowaniu tak w pierwszym.

**Lukasz Bott:**
Dobra, co to jest prowadzenie kontroli dostępu do reguł wywoływanych z poziomu raportów? Są Damian, to jest twój temat przy tłumaczom.

**Damian Kaminski:**
To już weź do komentarza. Chyba też omówione, tylko jeszcze nie zaopiekowane. To było omawiane. Tylko już sam nie pamiętam, czy to było ustalone, potwierdzone czy nie. Mianowicie, z tego co ja pamiętam, to propozycja była taka, że zostawiamy tak jak jest, że nie jest to luka bezpieczeństwa, bo i tak na poziomie wywołania reguły jest weryfikacja, czy ktoś ma do niej uprawnienie czy nie. Natomiast usprawnieniem miało być to, że będzie jak podejść do góry, ale to już przy okazji. Według mnie to trzeba przenieść do elementu modyfikacji całego wyglądu, bo to tak było i tak jest. Natomiast jeszcze wyżej tam jest chyba na początku taka checkbox domyślnie ma być nie zaznaczony dla nowych reguł i po prostu dla wszystkich starych po to, żeby utrzymać wsteczną. Czyli dostępna, a nie dla nowych miałbyś nie zaznaczony, a dla starych już zaznaczony. Czyli żeby reguła była dostępna w raportach, tak jak pola. Według mnie to nie jest krytyczne. To jest tak jak było i ja bym to opiekował dopiero w momencie, kiedy będziemy pracować nad nowym wyglądem reguł. Chyba że uważacie, że to jest bardzo istotne.

**Janusz Bossak:**
Nie jest istotne. Według mnie tak jak jest, jest całkiem dobrze. W tej chwili można wybierać te reguły. Jeżeli ktoś wybierze regułę, która nie powinna być wykonana, to i tak się ona nie wykona w kontekście tego użytkownika, który potem z niej skorzysta.

**Damian Kaminski:**
Dokładnie.

**Lukasz Bott:**
To są rady, tak?

**Damian Kaminski:**
Zdajmy, tak, tak, tak.

**Lukasz Bott:**
Pisz. I list. A może z braku wsparcia dla, co jest wieczór?

**Janusz Bossak:**
Co to jest ACS?

**Piotr Buczkowski:**
Application Apollo. Trzeba to zrobić, tylko nie ma czasu.

**Lukasz Bott:**
Ale to czeka Piotrek, to chyba trzeba zrobić, bo to jest istotne.

**Piotr Buczkowski:**
Wiem.

**Lukasz Bott:**
Ryży, tak czy siak Microsoft to.

**Janusz Bossak:**
Drugi, 2026.

**Damian Kaminski:**
To już chyba też Piotr omawialiśmy, nie?

**Piotr Buczkowski:**
Dlaczego to jest kwestia, czy zrobić to na szybko, tak jak do tej pory, czy zrobić to dobrze?

**Janusz Bossak:**
Zdecydowanie zrobić dobrze.

**Damian Kaminski:**
Zobacz na dole, nie było tak, że tam gdzieś zapisaliśmy? Bo mi się kojarzy, to jest z tym grafem. To już też omawialiśmy na którymś spotkaniu i że najwyżej zajmiemy się tym albo właśnie w trzecim albo w pierwszym kwartale przyszłego roku, bo jest jeszcze na to przestrzeń. Była taka konkluzja, że trzeba zrobić to dobrze, więc trzeba znaleźć na to przestrzeń.

**Piotr Buczkowski:**
To jest kwestia zrobienia list, czytam zarządzania listą konfiguracji out. Nie wiem jak to nazwać. Chodzi o to, może szamota pokazać ustawienia systemowe.

**Janusz Bossak:**
Ale teraz coś tam Marek coś, nie Marek dorabiał jakieś outy do Trust Center. To jeszcze.

**Piotr Buczkowski:**
Nie, całkiem co innego.

**Janusz Bossak:**
Ok.

**Piotr Buczkowski:**
Dostał ustawienia systemowe. Weź trochę niżej. Weź poczta przechodząca. Teraz tutaj masz taką na przykład konfigurację, aplikacja Azure, co nie?

**Lukasz Bott:**
Trzeba jakieś.

**Piotr Buczkowski:**
Tak samo może być dla Google, dla innego.

**Lukasz Bott:**
Chodzi o to, żeby zrobić interfejs do tego, tak?

**Piotr Buczkowski:**
Tak, bo trzeba byłoby dodać nowy taki parametr. To danie takiego nowego parametru i obsłużenie go przy logowaniu. To SharePoint, a to będzie proste, tak? Tylko że.

**Janusz Bossak:**
Dobra, słuchajcie, ponieważ to jest termin 2 kwietnia 2026, to na pewno nie możemy tego robić w pierwszym kwartale przyszłego roku. Teraz.

**Piotr Buczkowski:**
Nie, a nie?

**Lukasz Bott:**
Trzeba to zrobić w trzecim kwartale, w czwartym kwartale tego roku, żeby mieć.

**Janusz Bossak:**
Więc to już na najbliższe jakieś sprinty należy planować. Może nie najbliższy w sensie ten za tydzień, ale naprawdę już w takim tempie. Nawet bym to zrobił na ten za tydzień już, żeby się za to zabrać. Zróbmy na ten za tydzień, najwyżej będziemy przesuwać jeszcze, ale wolę już mieć to zaopiekowane, bo to już się pojawia któryś tam raz z kolei.

**Lukasz Bott:**
Zostawiamy to sobie jeszcze na razie architektur, żeby to jakoś kontrolować, czy?

**Janusz Bossak:**
Myślę, że nie. To tutaj Piotr to zaprojektuje i.

**Damian Kaminski:**
Jeszcze, jakbyś mógł, jak zrobisz to, zostać na tym ekranie, bo to już było ostatnie zgłoszenie. Czy wykorzystaliście już z tego? Bo to ja i child i ten generator. Ktoś to testował, ok?

**Janusz Bossak:**
Myśmy nie działa. Właśnie nie umiem tego do końca. Niby działa, są wpisane wszystkie te.

**Lukasz Bott:**
O tym mówisz?

**Janusz Bossak:**
API i tak dalej, tak. Ale.

**Damian Kaminski:**
Wejdź na 21841. To tam 21841, to jest Feature.

**Lukasz Bott:**
I co tego ustrojstwa robi?

**Damian Kaminski:**
Nie wiem co robi, jeszcze nie testowałem. Nie chcę nic popsuć, dlatego najpierw pytam. Teraz jak wejdziesz w tą zakładkę AI ten generator, to tutaj wyświetlają się, bo dlatego proponowałem to, bo tu są childy podpięte pod ten Feature. I jak zjedziesz niżej, to tu jest coś regenerator work items. Natomiast zanim cokolwiek kliknę, to wolałem zapytać, czy ktoś to weryfikował, co tu się stanie?

**Janusz Bossak:**
Nie. To się niby uruchamia, niby coś robi, ale w tym momencie się wywala i nie umiem zdiagnozować tego. Tam Michała prosiłem i Łukasza Poskrobko, ale jakoś nie. Na razie się nie udało. Ja też ten jakoś bardzo się tym nie zajmuję. To jest w ogóle wytwór Microsoftu, więc to powinno w miarę dobrze z tym cały Azure backlog działać, bo to jest stworzone przez Microsoft właśnie do tego. Ale coś jest zwalone z konfiguracją gdzieś, czy myśmy rencie. Nie mam czasu się tym zajmować.

**Damian Kaminski:**
Ok.

**Janusz Bossak:**
Ale to właśnie do tego miał służyć, że wpisujesz sobie jakąś tam ideę, jakiś Feature i on Ci pomaga rozbić to na zadania.

**Damian Kaminski:**
PBI. I to by było super.

**Janusz Bossak:**
Potrafi też jakby inaczej sformułować dany Feature, czyli wpisujesz sobie ogólnie tak jak tam rozumiesz, a on z tego robi porządny opis, porządne kryteria i tak dalej. Kilka ciekawych takich rzeczy. To jest ten kierunek, który powinniśmy jakby używać do takiego dobrego opisywania, nadawania dobrych tytułów poszczególnym PBI czy Feature i tak dalej.

**Damian Kaminski:**
Zacząłem klikać, ale w ogóle to nie reaguje, więc no.

**Janusz Bossak:**
Trzeba to kiedyś tam na spokojnie do tego podejść. Słuchajcie, jeszcze jedna rzecz to, bo w międzyczasie wygenerowałem z poprzedniej rady naszej podsumowanie. Jak to fajnie wygląda. Dlatego starałem się teraz w czasie tego spotkania mówić o tym, o czym mówimy, bo tutaj jest wzięta transkrypcja z tego i po prostu podsumował elegancko. Edytor formularza, problem z obsługą pól pustych i tutaj ryzyko, proponowane rozwiązania, decyzje, zadania, bezpieczeństwo, dane poufne w nazwach plików. To przeczytałem to przed chwilą, to naprawdę ma sens. Oddaje ducha tego, o czym rozmawialiśmy w czasie tej rady. Więc będę takie podsumowania robił i wrzucał po każdej Radzie, bo to zwykłe podsumowanie, co robi ten Microsoft Copilot jest takie sobie, słabe.

**Damian Kaminski:**
Uproszczenie bardzo mocno.

**Janusz Bossak:**
A tutaj ukierunkowane. Miałem co ma czego ma tam wynajdywać, co ma wynajdywać, w jaki sposób opisywać, właśnie dzielić na te ryzyka, proponowane rozwiązanie, decyzje i zadania. I dużo lepiej tak takie podsumowanie czytać. Także będziemy robić i dlatego na tej Radzie warto w ten sposób mówić, że na głos. On nie widzi, prędko widzi transkrypcję, więc na głos wypowiedzieć to zagadnienie, nad którym pracujemy i wtedy on będzie wiedział, że to jest to zagadnienie. Wokół niego będzie tam się koncentrował. Dobra.

**Lukasz Bott:**
Dokończymy. Lista.

**Janusz Bossak:**
Dzięki Mary.

**Lukasz Bott:**
Coś Kamil?

**Kamil Dubaniowski:**
No.

**Janusz Bossak:**
Dobra, to dzięki.

**Lukasz Bott:**
Dzięki.

**Kamil Dubaniowski:**
Dzięki.

**Damian Kaminski:**
Dzięki.

**Janusz Bossak:**
Zatrzymano transkrypcję.

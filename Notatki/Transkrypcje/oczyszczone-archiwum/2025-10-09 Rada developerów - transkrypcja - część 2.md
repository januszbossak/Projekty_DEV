**Data spotkania:** 9 października 2025, 08:00 - część 2

---

**Damian Kaminski:** W kontekście wczorajszego, tylko krótkie pytanie. Piotrze, czy potrzebne jest zgłoszenie, albo czy w ogóle jest taki problem, że procesy wyłączone odpalają jakieś reguły cykliczne, automatyczne, czy coś w tym stylu? Czy to powinniśmy jakkolwiek opiekować?

**Piotr Buczkowski:** Jakie procesy, jakie reguły? To są reguły procesu, reguły.

**Damian Kaminski:** To znaczy... Dobrze by było, żeby to może spisać i trochę przemianować co to znaczy procesy te aktywne, nieaktywne, usunięte, bo czuję, że nie każdy to rozumie.

**Piotr Buczkowski:** Znaczy...

**Damian Kaminski:** Nie każdy – i to nawet o sobie mówię – nie każdy wie, co się pod tym kryje.

**Piotr Buczkowski:** Znaczy... Procesy nieaktywne to pierwotnie miało być to, że na przykład procesy w trakcie powodzenia. Tylko było – administrator może tworzyć sprawy z procesów nieaktywnych.

**Damian Kaminski:** Bo ja bym powiedział tak: proces nieaktywny to taki, który się nie wyświetla na liście procesów, ale można na nim operować, jak się stworzy sprawę w ramach jakiegoś innego wywołania?

**Piotr Buczkowski:** Ale administratorowi się wyświetla.

**Damian Kaminski:** No tak, administratorowi się wyświetla, więc ja nawet...

**Piotr Buczkowski:** To było założenie było takie, że to są procesy w trakcie tworzenia, powiedzmy.

**Damian Kaminski:** No właśnie, to może nie powinny nazywać się nieaktywne, tylko właśnie jakieś robocze.

**Piotr Buczkowski:** No, ale też...

**Janusz Bossak:** No to...

**Damian Kaminski:** Bo...

**Janusz Bossak:** Tak.

**Piotr Buczkowski:** Też jak najbardziej może być tak, że...

**Łukasz Bott:** No, też nie...

**Piotr Buczkowski:** Znaczy, czasem usunięte nie musi. To jest tylko kwestia tego, czy się wyświetla na stronie tworzenia sprawy czy nie. Nie ma żadnych innych ograniczeń.

**Damian Kaminski:** Czyli to... Dobra.

**Łukasz Bott:** Czyli na przykład z CreateCase mogę sobie utworzyć sprawę według procesu usuniętego?

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** Tak.

**Piotr Buczkowski:** Tak samo reguły powinny działać, bo nie przypominam sobie, żeby były jakieś ograniczenia.

**Damian Kaminski:** Nieaktywnego. No więc te... No właśnie, te powiedzmy tagi, czy jakkolwiek to nazwiemy – kategorie tych procesów są takie... Mają małe konsekwencje, w sensie dotyczą tylko i wyłącznie zakładki procesy. Dobra, może na razie wystarczy to opisać, że tak to działa, żeby też nikt nie miał potem do tego pretensji. Ale z drugiej strony, właśnie ktoś coś na przykład tworzy jakieś reguły powiedzmy okresowych i potem kliknie usunięte i założy, że to usunięte. No to to nie przeszkadza, jednak to się wykonuje w tle, więc nie mówię, że już, tylko może powinniśmy zaplanować, żeby tego typu procesy w jakiś sposób – ich reguły – dezaktywować, żeby to też optymalizować.

**Piotr Buczkowski:** Bo...

**Łukasz Bott:** Znaczy sprawy...

**Piotr Buczkowski:** Nie, nie myślę, że nie możemy tego zmienić.

**Damian Kaminski:** Nie możemy?

**Janusz Bossak:** Znaczy, raczej trzeba wprowadzić czwartą kategorię, która będzie tak działała. A te kategorie to już – nie wiem ile razy, z 50 razy – mówiliśmy o tym, że trzeba nazwać opisowo.

**Damian Kaminski:** OK, no to można tak zrobić.

**Janusz Bossak:** Czyli nie "aktywny", "nieaktywny", "usunięty", tylko "sprawy z tego procesu są widoczne na listach", "nie są widoczne na listach". Właśnie to, co powiedziałeś, że wykonuje... Mimo że na przykład reguły okresowe się wykonują – to po prostu opis. Niech to będzie jeden akapit opisu, ale niech to mówi, co będzie się działo.

**Damian Kaminski:** Co to robi dokładnie.

**Piotr Buczkowski:** To może być długi akapit?

**Damian Kaminski:** Znaczy, według mnie to jest kwestia opisania tego, jaki jest stan, żeby nikt nie miał do tego zarzutu, żebyśmy mogli powiedzieć: usunięte to nic nie robi poza tym, że nie widzi tego ani admin, ani użytkownik na liście procesy, a poza tym wszystko działa w tle.

**Janusz Bossak:** Skoro jest tak, że dla każdego stanu wszystko działa w tle, to można to napisać przed tym wszystkim, czyli niezależnie od tego, co wybierzesz, reguły na przykład okresowe wykonywane są dla każdego typu...

**Damian Kaminski:** Dokładnie.

**Janusz Bossak:** ...stanu procesu.

**Łukasz Bott:** I że sprawy działają.

**Janusz Bossak:** No, no.

**Damian Kaminski:** Dobrze, ale jeszcze to, co powiedział Janusz, bo to jest istotne – czy temat mamy jakkolwiek kontynuować, czy nie. Jeśli dodamy nową kategorię, to wtedy w jej ramach możemy takie ograniczenia porobić. Czy tu chodziło ci o to, że to jest większe jakieś wyzwanie w ogóle – wdrożenie deweloperskie – żeby...

**Janusz Bossak:** Kompatybilność wsteczna. Ludzie sobie to zrobili jako usunięte i na przykład mają świadomość, że działają te reguły okresowe. No i nie możemy teraz nagle zrobić, że przestaną działać. Więc lepiej zrobić czwartą kategorię – zatrzymane.

**Damian Kaminski:** Przezwać tę, a nazwać usunięte i właśnie czy zatrzymane odrębną?

**Janusz Bossak:** Tak. I wtedy w ogóle dla tych spraw z tego procesu po prostu wszystko stoi. One są, leżą w archiwum i nic się nie dzieje.

**Damian Kaminski:** Zamrożone. No właśnie, może proces archiwalny.

**Janusz Bossak:** Także wolę...

**Damian Kaminski:** Dobra, to znaczy to też trzeba się zastanowić, bo niekoniecznie wszystkie reguły – może automatyczne – powinny działać, bo jednak one coś tam ukrywać mogą w podglądzie. I niekoniecznie to powinno być – wszystkie tam, powiedzmy, sekcje techniczne – powinny być dostępne. Dobra, no to powiedzmy, mam to z tyłu głowy...

**Łukasz Bott:** Pytanie... Więc... Nie lubię czegoś...

**Janusz Bossak:** Automatycznie pewnie tak. Natomiast okresowe... Automatyczne, tak jak mówisz, ale wchodzisz w sprawę, no to może coś tam się musi...

**Damian Kaminski:** Tak, okresowe...

**Janusz Bossak:** ...przeliczyć, wyświetlić czy cokolwiek. Ale okresowe lepiej, żeby się nie wykonywały, nie?

**Damian Kaminski:** Dobra, zapakujmy to. Ja będę o tym pamiętał. Gdzieś tam się to rozpiszę na kolejne kwartały.

**Łukasz Bott:** Tak. Pytanie – to jest to, jeszcze sobie zanotuj – pytanie takie: co ze sprawą, która jest otwarta według takiego zatrzymanego procesu? Bo mówimy, że wstrzymujemy jakieś tam reguły okresowe, ale czy sprawa może być dalej procedowana? Czy ona się...

**Damian Kaminski:** No to to jest znowu do analizy, co z tym zrobić. Na ten moment jako as-is ja bym powiedział, że trzeba zrobić wpis na wiki stanu jaki jest i ewentualnie dać sugestie co do zmiany nazw i opisów – co oznaczają te kategorie. I to jest tyle, więc tu nie ma poprawek deweloperskich, tylko poprawy w opisie i wyjaśnienie co to znaczy.

**Łukasz Bott:** No deweloperska będzie o tyle, że gdzieś tam trzeba będzie w tym formularzu – w ustawieniach tam – dopisać to właśnie te akapity.

**Damian Kaminski:** No, tak. Dobra, idźmy dalej z jakimiś innymi tematami, jeśli mamy.

**Łukasz Bott:** Tak jak powiedziałem, na początku nie ma nic na radę takich...

**Kamil Dubaniowski:** Ja też bym to trochę organizował, ale to bo na radę jest oznaczonych 134 zgłoszeń.

**Piotr Buczkowski:** To może...

**Łukasz Bott:** Słucham?

**Piotr Buczkowski:** Może ja zadam pytanie.

**Kamil Dubaniowski:** Do rady.

**Piotr Buczkowski:** Pytanie bez zgłoszenia – to znaczy zgłoszenie jest, bo to jest to wczytywanie tych XML, które powodowało...

**Kamil Dubaniowski:** Tak, tak, tak.

**Łukasz Bott:** No, no.

**Damian Kaminski:** Możesz? Tak.

**Piotr Buczkowski:** Replika... Miałaś... Czy może być tak, że jeżeli wykryjemy coś, czego się nie da automatycznie naprawić, to mówimy: sorry, nie da się automatycznie naprawić i nie możesz wgrać?

**Damian Kaminski:** Ja nie rozumiem kontekstu. Aha, dobra, import procesu, tak?

**Piotr Buczkowski:** Import procesu. Zgłoszenie już mówię, który...

**Damian Kaminski:** Już rozumiem. Tam, gdzie był ten dubel, bo ktoś coś tam pozmieniał w kartotekach?

**Piotr Buczkowski:** 22195.

**Damian Kaminski:** Wyświetlasz, czy mam wyświetlić?

**Piotr Buczkowski:** Nie wiem, tylko czy ja mam...

**Damian Kaminski:** Ja już, sekundę.

**Piotr Buczkowski:** To ja udostępniam.

**Damian Kaminski:** No to udostępnia. To jest chyba na kanwie...

**Piotr Buczkowski:** 22200.

**Damian Kaminski:** Polpharmy, tak?

**Piotr Buczkowski:** Ponad... Nie wiem czy to... Tak. Znaczy to już naprawiłem, tylko że to może powodować przekłamanie danych. To jest tak, że oni dodali na produkcji pole. Później na teście czy na deweloper dodali jakieś pole do tekstu i dodali takie samo pole jak na produkcji – tej samej nazwie. Na dew, ale już ponieważ dodali to pole jakieś inne wcześniej, to CaseText6 zostało przypisane do jednego pola. I teraz jak zaimportujemy taki...

**Damian Kaminski:** Proces.

**Piotr Buczkowski:** Taki proces D to na produkcji to co było wpisane w tym polu dodanym ręcznie przejdzie do tego nowego pola. I według mnie to jest bardzo niebezpieczne. I do tego jeszcze zostawiłem to na sobie, bo też poprawiłem, żeby to jakoś rozwiązać. Także planuję dodać: sorry, nie da się tego wczytać, musisz ręcznie poprawić na produkcji to i to.


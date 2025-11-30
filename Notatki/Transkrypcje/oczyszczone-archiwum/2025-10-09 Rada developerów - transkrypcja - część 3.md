**Data spotkania:** 9 października 2025, 08:00 - część 3

---

**Łukasz Bott:** No, ale to...

**Damian Kaminski:** Znaczy w ogóle zarządzanie formularzem na środowisku produkcyjnym... Powinno być przyblokowane dodawanie jakiegoś pola, powinno być zabezpieczone. Nie wiem czy globalnie systemowo, czy na poziomie procesu, ale lepiej pewnie globalnie systemowo. I wtedy odblokowanie tego powinno – nie wiem – dodawać im jakieś przypomnienie, czy próba dodania pola na takim procesie – na powiedzmy oznaczamy, że to jest środowisko produkcyjne. Jak ktoś dodaje pole, to wyskakuje mu jakiś dodatkowy... Popatrz, że powinien zrobić to na środowisku testowym i potem przenieść. Bo potem rodzą się właśnie takie kwestie, że ktoś coś dodał, bo zapomniał, nie wiem dlaczego, ale zrobił to nie tak jak trzeba i się rozjeżdżają nam te środowiska. I potem mają problemy z unifikacją i już przestają pracować na testowym, bo już ono się rozjechało, bo ktoś poszedł na łatwiznę.

**Łukasz Bott:** Ileś razy to powtarzam przy każdym szkoleniu, że tak się nie robi.

**Damian Kaminski:** Cały czas koło zamknięte – jest nowy wdrożeniowiec świeży i już on nie pamięta. I może powinniśmy jakoś oznaczać środowisko właśnie produkcyjnie i ostrzegać przy próbie dodania pola, że...

**Łukasz Bott:** Nie, i dokładnie tak.

**Damian Kaminski:** To nie jest poprawne podejście.

**Łukasz Bott:** Znaczy, dodanie pola, dodanie reguły to jest... Czyli dodanie reguł...

**Damian Kaminski:** Reguła akurat jest to...

**Łukasz Bott:** Reguła to...

**Piotr Buczkowski:** Regułę to jest prosto, bo po prostu nadpisujesz nową.

**Damian Kaminski:** Też można, ale to się przepisze, nie?

**Łukasz Bott:** Tak, tak, tak.

**Piotr Buczkowski:** Mają jakieś dane, tak.

**Damian Kaminski:** Bo regułą to – jest jakieś, jest jakaś akcja krytyczna – też można oczywiście. Ale na przykład robisz, nie wiem tam, hide field, hide section, bo ktoś coś widzi i szybko reagujesz na produkcji, to rozumiem. Ale dodanie pola, czyli jakaś nowa zupełnie funkcjonalność, nie powinna mieć działania na środowisku produkcyjnym bezpośrednio.

**Łukasz Bott:** Czyli trzeba wprowadzić – jak już trochę wracając do tej rozmowy o stanach czy tam nie wiem typach procesu – stanach procesu, to trzeba... Nie globalnie tak.

**Damian Kaminski:** Środowisk raczej globalnie chyba, bo jak będzie na procesie to... To będą zapominać, żeby to oznaczać.

**Łukasz Bott:** Że... Czyli w ustawieniach systemowych trzeba gdzieś wprowadzić – to by się faktycznie przydało, bo ja... Nie musiałem robić na poziomie... Na poziomie... Dobra, ja to sobie robiłem na poziomie reguł, ale tylko dlatego, że w nazwie organizacji w ustawieniach systemowych miałem tam wpisane słowo klucz "test" albo "prod". Raczej "test". I wtedy sobie jakimś tam if'em robiłem w regule, że jeśli `SystemParameter` – czy jak to było? – `OrganizationName` zawiera "test", to wiem, że działam w trybie testowym. I tam się trochę proces inaczej zachowywał.

**Damian Kaminski:** Ale to już reguła, więc to też co innego.

**Łukasz Bott:** Ale to już było... Ale to już w ogóle... Ale to OK. Ale jeżeli dodamy taki parametr systemowy – że to jest produkcja – to w tym momencie...

**Damian Kaminski:** A że ten parametr będzie można odczytywać?

**Łukasz Bott:** To po pierwsze tak – to po pierwsze ma to wpływ na tę funkcjonalność, które tutaj omawiamy, w sensie, że jeżeli jest to produkcja, to jest zablokowane dodawanie jakiegokolwiek czy usuwanie pól, tak?

**Damian Kaminski:** Znaczy nie wiem czy zablokowanie, bo jak zablokowanie to będą po prostu...

**Łukasz Bott:** No to może... Dobra, to być może ostrzeżenie z jakimś tam fill system. Potwierdź, że tak, że jesteś pewny. Wpisz kod wysłany na maila, że potwierdzam, że taką operację chcesz wykonać. Chodzi o to, żeby to było upierdliwe, żeby rzeczywiście człowiek zastanowił się kilka razy, że: OK, dobra, no to może jednak faktycznie trzeba to po bożemu zrobić. Ale zdaję sobie sprawę, że faktycznie może być sytuacja awaryjna i musisz jakieś pole wprowadzić, nie?

**Damian Kaminski:** Utrudnić. Tak, tak, tak. Dobra, i się zgadzam. Przy czym to powinno być tak, że do każdego wprowadzenia robisz akcję jednorazową, która się resetuje. Po prostu zmierzam do tego, żeby to nie było odznaczanie – jak już ustawimy, że jest produkcyjna wersja – to żeby nie było tak, że ktoś, jest zablokowane, ktoś wejdzie, przestawi, że testowa, wtedy doda pole, zapomni przestawić, że produkcyjna, no i będzie znowu za miesiąc czy za pół roku to samo.

**Łukasz Bott:** To liczę, że by trzeba było ten znacznik, czy to jest wersja produkcyjna, że jak już go ustawiłeś, tego się nie da odustawić, nie?

**Damian Kaminski:** Może, może tak. Chociaż z interfejsu, czemu nie?

**Kamil Dubaniowski:** Chociaż...

**Damian Kaminski:** Natomiast może wtedy na formularzu tam, gdzie można dodawać pola, tam powinien być jakiś dodatkowy checkbox, że chcę wprowadzać zmiany i jestem świadomy, że zaburzę kompatybilność ze środowiskiem testowym. I musisz go zaznaczyć przy każdym wejściu na zakładkę, gdzie możesz edytować pola. Wtedy dopiero odblokowuje ci się możliwość dodawania, czy ten panel właśnie z nowymi polami.

**Łukasz Bott:** OK, no to warto to zrobić.

**Damian Kaminski:** No to... Dobra, to może inaczej. Wróćmy – to według mnie warto to zrobić, ale to trzeba zaplanować i co to musi obejmować. A co do tego, Piotrze, to jeszcze raz może jakbyś zadał pytanie, żebyśmy ten wątek rozwiązali?

**Łukasz Bott:** Tak, tak.

**Piotr Buczkowski:** Teraz jeżeli wgrywamy taki proces, to pojawia się pytanie – tam się pojawia lista zmian czy tam różnic. I się pojawia pytanie, czy nadpisać czy utworzyć nowy?

**Łukasz Bott:** Przy imporcie.

**Piotr Buczkowski:** W takim przypadku jak ten chciałbym dodać opcję: sorry, tego pliku się nie da wgrać.

**Damian Kaminski:** W sensie nie można stworzyć nowego nawet?

**Piotr Buczkowski:** Znaczy sorry, tak – możesz stworzyć nowy proces. Nie możesz nadpisać. Mój błąd, źle się wyraziłem.

**Damian Kaminski:** Nie można nadpisać. Dobra, tylko żeby potem oni nie zrobili tak – to stworzy nowy, co mi szkodzi. Myślę, to powinno być ostateczność, żeby ktoś miał świadomość. Jakoś to sprytnie trzeba było zrobić, żeby nie robili.

**Piotr Buczkowski:** Bo jeżeli stworzą nowy, to muszą wyeksportować, wgrać na dew i ten nowy rozwijać.

**Damian Kaminski:** No właśnie, ale wtedy przeniesienie wszystkich spraw już istniejących – jak tu mówimy o kartotekach – to by było...

**Piotr Buczkowski:** Nie, nie. Nie przenosi.

**Damian Kaminski:** Ja wiem. Zgadzam się z tobą, więc pytanie tylko – co to nam zblokuje w sensie?

**Łukasz Bott:** To znaczy... Też – konsekwencje jakie są tego, że...

**Damian Kaminski:** Znaczy wiem, jakie są konsekwencje. Zastanawiam się... Dobra, według mnie trzeba to zaprojektować dobrze – komunikat – żeby był zrozumiany, żeby ktoś...

**Piotr Buczkowski:** Bo co tutaj?

**Damian Kaminski:** ...nie poszedł na łatwiznę i nie kliknął: dobra, stwórzę nowy, nie myśląc, co będzie z konsekwencją, nie?

**Łukasz Bott:** Tak.

**Piotr Buczkowski:** Co trzeba było zrobić? Co tutaj trzeba było zrobić? Na dew podmienić przepisanie do CaseText6, CaseText7 odwrotnie. Już, OK. Ale to trzeba było zrobić na dew z bazy danych.

**Damian Kaminski:** O widzisz, i tu jest kolejny element wprowadzenia tego, czy to jest wersja produkcyjna, czy testowa. I jeśli będzie testowa – co tu, Kamil, w kontekście właśnie przypisywania pól do właśnie tego CaseZWarcia i tak dalej – to może to też powinno wtedy się odblokowywać. Jeśli to jest wpisane, że wersja testowa, to tam można sobie rotować jakie pole gdzie jest przypisane, a na produkcyjnej ta kolumna jest tylko do odczytu.

**Piotr Buczkowski:** Ale to, to co wczoraj pisałem właśnie – żeby wyświetlać tą CaseText6 na przykład w ustawieniach – to może właśnie dać możliwość ręcznego przepisania dla takich przypadków.

**Damian Kaminski:** Ale w momencie importu, czy...

**Piotr Buczkowski:** Nie, w momencie edycji pola – że w szczególnych przypadkach masz mieć możliwość zdefiniowania, do której kolumny w bazie danych jest przypisane to pole.

**Damian Kaminski:** I zgoda, tylko to właśnie powinno być chyba równolegle wprowadzone z tym – to jest środowiska...

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** I wtedy mamy to zaopiekowane, można podejrzeć nawet, jeśli ktoś by tak to zrobił, to wracam.

**Piotr Buczkowski:** Bo mówię, że to... tutaj był taki przypadek, że aby to naprawić, trzeba było ręcznie w bazie danych po stronie dew zapewnić przepisanie tych 2 pól – zamienić przypisanie 6-7, 7-6. Trzeba to zrobić z bazy danych. Akurat jest u nas Marcinem, także zrobiliśmy. Ale coś...

**Damian Kaminski:** No dobrze, czyli tak – tutaj musimy podjąć decyzję, czy po prostu blokować nadpisanie, bo to powoduje problem.

**Piotr Buczkowski:** Tak.

**Damian Kaminski:** No chyba tak. Bo lepiej nie mieć problemu i wolniej to zrobić, zapytać: dlaczego mam blokadę, niż zrobić tak jak tutaj, potem mieć... Klient ma pretensje, użytkować mają pretensje, że nadpisało a nie działa.

**Piotr Buczkowski:** Tutaj akurat było, że: dlaczego już przestały mi się tworzyć te takie pracownika z resztą, bo...

**Damian Kaminski:** Wiem, bo ja też w tym uczestniczyłem w rozwiązywaniu. I też miałem te obiekcje, to ty, że tam jakieś CaseID są dziwne dodawane. Dobra, według mnie tak – tylko trzeba dobrze zaprojektować cały komunikat, żeby on był zrozumiały, że właśnie należy poprawić przypisania na tym procesie źródłowym ze środowiska źródłowego i wgrać pliki jeszcze raz, i wyeksportować i zaimportować plik jeszcze raz, żeby oni wiedzieli co mają zrobić.

**Piotr Buczkowski:** Dobrze, no to... Zaproponuję jakiś tak... Sprawa, czy to jest?

**Damian Kaminski:** OK. Jeszcze Kamil poruszył słuszną kwestię, że jest ponad 100 zgłoszeń przypisanych.

**Kamil Dubaniowski:** Znaczy, ja mogę w tym momencie przyjąć założenie, że wszystko co jest nie z bieżącego roku – bo tego będzie tam kilkanaście – wtedy nam zostanie. Wywalamy ten... Bo jak nie umówiliśmy do tej pory, to znaczy, że nie jestem w ogóle ruszany, więc wróci do nas, jak będziemy potem nadrabiać.

**Damian Kaminski:** Mhm.

**Kamil Dubaniowski:** I najwyżej wtedy sobie na bieżąco będziemy oznaczać zadania z backlogu na radę. Ale teraz to jest zupełnie nadmiarowe.

**Łukasz Bott:** Wiesz co?

**Kamil Dubaniowski:** Bo na sprint to my powinniśmy mieć już omówione tematy, a nie omawiać w trakcie. Chyba że to są takie, że robię coś i nie wiem jako deweloper – no to sobie wrzucam na radę z bieżącego sprintu, żeby to przedyskutować z szerszym gronem. Ale tak to...


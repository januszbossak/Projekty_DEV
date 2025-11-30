**Data spotkania:** 18 listopada 2025, 11:02 - część 5

---

**Kamil Dubaniowski:** Zobaczcie, jakby oni mają to tylko tutaj – na tym poziomie to jest numer katalogu JRWA 0031. To jest informacja o tym, w jakim katalogu JRWA jest. Więc jak on tu wpisze 0031, to spodziewam się, że pełnotekstowo będzie leciał po wszystkich tutaj informacjach i znajdzie mu to 0031, ale innych filtrów to nie widzę. Zaraz poklikam na aktualnym systemie, czyli tam to wygląda.

**Mariusz Piotrzkowski:** Jestem ciekaw, czy oni to wyszukiwanie pełnotekstowe zrobili na backendzie czy na frontendzie.

**Kamil Dubaniowski:** Znaczy, mają łatwiej, oni robią tylko to, oni nie robią nic więcej, więc oni mają pod to dedykowaną tabelę pewnie i tylko takie dane tam są – żadnych innych uników. Nie możesz sobie dodać nowego pola, u nich masz takie pola i koniec.

**Mariusz Piotrzkowski:** Mhm.

**Kamil Dubaniowski:** Dobra, nie przedłużam. W sensie – zarezerwujcie sobie na to czas. Bo tak jak wam powiedziałem, nawet nie mówię, że już musimy coś dowieźć. My będziemy teraz robić pewnie jakąś wydmuszkę, żeby cokolwiek im pokazać mniej więcej, jak to ma działać, tego dwudziestego ósmego. Ale powinniśmy już gdzieś tam myśleć o docelowym rozwiązaniu, więc tą koncepcję chciałbym zamknąć jak najszybciej.

**Mariusz Piotrzkowski:** Jeżeli możesz na szybko – powiem ostatnie 30 sekund – jeśli chodzi o samo zarządzanie, kto miał JRWA, to ja proponuję dodać do prawego panelu albo w stanie sprawy jakąś sekcję albo dodać coś jak repozytorium, że po prostu po włączeniu w sprawie JRWA się nam pokazuje nowy prawy panel i tam jest zarządzanie tym – drugim – to by było najprościej.

**Kamil Dubaniowski:** Znaczy zarządzać, zarządza wyznaczony użytkownik z odpowiednim uprawnieniem tą strukturą. Ja bym teraz z panelem do zarządzania strukturą, a wpisanie, tak. Wpisanie z poziomu drzewa też nie jest jakby tam super. Teraz istotne, jeśli będzie to po prostu zwykłe pole gdzieś tam na formularzu, gdzie muszę podać symbol i on mi filtruje.

**Mariusz Piotrzkowski:** Nie, nie jestem – struktury – tylko przepisanie. Żeby mógł się przyglądać i wpisać do konkretnego działu.

**Piotr Buczkowski:** Nie, nie, nie – na formularzu oddzielny panel, nie róbmy tego jako nie – nie naginajmy do tego jakichś istniejących typów pól.

**Kamil Dubaniowski:** Prawdę tak, tryb OK.

**Mariusz Piotrzkowski:** Tak.

**Kamil Dubaniowski:** Dobra. OK.

**Mariusz Piotrzkowski:** Tak, zgadzam się.

**Kamil Dubaniowski:** Nie, nie będę się upierał. Jak zauważyliście – tak znowu wyłączyłem tamten filmik – ale tam, gdzie ktoś wyszukuje już do jakiego katalogu chce wpisać, to on ma 2 zakładki do takiego wpisania właśnie – z palca numeru katalogu albo nazwy katalogu – a obok, a obok była druga zakładka – struktura – i wtedy mu się wyświetla drzewko i on może sobie przeklikać przez to drzewko i kliknąć – tu wpinam – czyli tak jak u nas w repozytorium.

**Mariusz Piotrzkowski:** Będzie o wiele prościej czasowo, nie? Mhm. I drzewka. To ci, bo to ci powiem, tak, paradoksalnie zrobienie tych mechanizmów w nowym prawym panelu byłoby szybsze niż zmodyfikowanie aktualnego pola.

**Kamil Dubaniowski:** OK. Wiecie, będziemy mieli temat zamknięty – tych przetargów, gdzie Piotr jest obowiązkowy – było multum do tej pory, że zrobiliśmy żadnego, nie wygraliśmy – wygraliśmy LOT, i trzeba to w końcu zrobić. 50000 za to bierzemy jako zadanie, także budżet jakieś tam mam.

**Piotr Buczkowski:** Proponuję zacząć od tego, żeby przygotować tabelę, przygotować klasy – na razie edycja z poziomu bazy danych. I wyświetlanie tego tak, także można było wpiąć.

**Kamil Dubaniowski:** I uprawnienia – to, to dla mnie byłoby gdzieś tam.

**Piotr Buczkowski:** Tak i uprawnienia tam. Mam pomysł, jak zrobić wydanie uprawnienia, także żeby dziedziczenie łatwo szło. Typu, że powiedzmy jest zestaw uprawnień, który może być przypięty do wielu folderów, tak?

**Kamil Dubaniowski:** Tak.

**Piotr Buczkowski:** Obecnie, na przykład, domyślnie jest, na przykład, przypięty do wszystkich folderów tam, gdzie nie ma przerwania dziedziczenia.

**Mariusz Piotrzkowski:** Zgadzam się.

**Kamil Dubaniowski:** Mhm. Takie jest założenie.

**Piotr Buczkowski:** Także to, także łatwy join jest tak wtedy, tak.

**Mariusz Piotrzkowski:** Zgadzam się.

**Piotr Buczkowski:** Szukaj w zestawie tam, gdzie mam uprawnienia – join do połączenia do folderu. Join do folderu, tak. Czyli wszystkie foldery, gdzie ma uprawnienia.

**Mariusz Piotrzkowski:** Mhm.

**Piotr Buczkowski:** Nie.

**Kamil Dubaniowski:** A czekajcie – do sobie. Bo jest taka zasada, że mamy katalog końcowy i katalogiem końcowym jest ten, który ma przypisaną kategorię archiwalną, czyli wpinać mogę tylko do takiego katalogu, który ma przypisaną kategorię. Ten katalog jest tylko takim katalogiem jakby nadrzędnym, żeby hierarchię utrzymać, ale.

**Piotr Buczkowski:** No to. To over kategorii.

**Kamil Dubaniowski:** Tak, tylko to dokładnie, tak.

**Mariusz Piotrzkowski:** A jeszcze ja bym – 2 pytania z perspektywy samej struktury – czy. Może być taka sytuacja, że sprawa będzie przepisana do wielu zbiorów jednocześnie.

**Piotr Buczkowski:** Nie.

**Kamil Dubaniowski:** Nie – Janusz tu wspominał, że w takiej sytuacji wręcz należy stworzyć kopię, ale nie spodziewałem się, że tak będzie jakoś tam.

**Piotr Buczkowski:** To znaczy.

**Mariusz Piotrzkowski:** Rozumiem.

**Piotr Buczkowski:** Znaczy. Róbmy oddzielną tabelę, czy będzie case ID i folderami i tak.

**Mariusz Piotrzkowski:** Drugie pytanie takie – czy zakładamy?

**Piotr Buczkowski:** I w razie czego, jakby to było potrzebne, będzie, będzie tak samo będziemy robić w repozytorium, tak – na razie pliku aby był tylko w jednym miejscu repozytorium. Ale ponieważ to będzie, to wiele do wielu, to będzie możliwe tego rozszerzenie na podpięcie w wielu miejscach.

**Kamil Dubaniowski:** Mhm, mhm.

**Mariusz Piotrzkowski:** Dobra, chciałem drugie pytanie – czy zakładamy, że te klasy można dowolnie modyfikować, czyli na przykład coś takiego, że moglibyśmy sobie zmienić sygnaturę? Jak jest, to będą jakieś sprawy w środku?

**Kamil Dubaniowski:** To zależy od koncepcji, bo.

**Mariusz Piotrzkowski:** Na przykład – będę przykład – tutaj jest napisane 060.

**Piotr Buczkowski:** To jest, to jest zatwierdzane przez – to jest zatwierdzane. To nie jest tak, że to sobie modyfikujesz, tak.

**Kamil Dubaniowski:** Tak, to jest, to przechodzi wręcz jakby taką, powiedzmy, ale uchwałę.

**Mariusz Piotrzkowski:** Tak, tak, tak, ale mi chodzi mi chodzi z samych możliwości – samej możliwości systemu – gdyby to nie było zatwierdzone, na przykład coś by się pomylił, źle wpisał czy cokolwiek, czy zakładamy, że to jest przykład.

**Piotr Buczkowski:** Pierwszy. Czyli w wersji – edycja tylko z poziomu bazy danych.

**Mariusz Piotrzkowski:** Rozumiem, dobra.

**Kamil Dubaniowski:** Docelowo można zmieniać nazwy katalogów. To, to osoba tam, jakby nawet administrująca – było pokazane, że może zrobić co więcej, może usunąć katalog, ale tu walidacja – jeśli nie ma nad nim żadnych podpiętych naszych, jakby już amoditowych wtedy spraw, zagranicznych, czyli dopóki ten katalog jest pusty, to mogę go usunąć jako osoba zarządzająca, ale jak już coś tam jest, to nie mogę. Więc kolejne elementy będziemy dokładać. Wiecie, to nie jest już, że my tam dwudziestego ósmego czy na koniec roku musimy mieć działające rozwiązanie, musi być coś, co oni są w stanie zaprezentować, bo klient też jest tego świadom.

**Piotr Buczkowski:** Tak.

**Mariusz Piotrzkowski:** Dobry. Nowej. Mhm.

**Kamil Dubaniowski:** Że robimy demówkę, to nie jest tak, że my tam. Buszujemy, mają tego świadomość, dali taki termin, oni muszą jako LOT się pochwalić na koniec roku, że coś mają, więc my musimy coś zrobić, ale róbmy już tak, jak.

**Mariusz Piotrzkowski:** Pytanie jeszcze mam do Piotra – czy będziemy używać GUID tutaj, na przykład, do albo do poszczególnych zapisów czy samym po prostu ID zwykłe?

**Piotr Buczkowski:** Po co takie obiekty? Nie lubię GUID-ów, po nie widać.

**Mariusz Piotrzkowski:** Nie wiem tak, tylko chciałem dopytać w kontekście archiwizacji – w kontekście archiwizacji, bo jeżeli to ma być eksportowane, zapisywane gdzieś poza czy po prostu wysyłane do urzędu czy gdziekolwiek, to może takie GUID-y by się przydały. Nie mam pojęcia.

**Piotr Buczkowski:** Znaczy – według – można być GUID jako taki dodatkowy, tak jak mamy w procesie, tak, ale nie, nie, nie do robienia relacji, bo to nie lubię tego.

**Mariusz Piotrzkowski:** OK, rozumiem. Nie, to nie chodzi mi stricte właśnie do eksportu, żeby zachować. Spójność danych, nie.

**Piotr Buczkowski:** Będzie jakiś eksport czy import?

**Mariusz Piotrzkowski:** Z tego, co mówią, to musi iść do archiwum państwowego, więc trzeba będzie założyć, że to będzie eksportowane, importowane w dużych paczkach, nie.

**Kamil Dubaniowski:** Sprawy już pojedyncze. Tak, tak, to niestety jakby jest kolejne dane, czyli przekazanie tego do archiwów musimy przygotować. Coś takiego, jak robimy w e-teczce, czyli plik odpowiedniej strukturze, który mówi, co jest.

**Piotr Buczkowski:** No to generujemy plik i tyle, tak.

**Kamil Dubaniowski:** Tak, to musi być zestaw. Tak, wydaje mi się, że podobnie jak w e-teczce, czyli do każdego załącznika skanu musi być XML, który opisuje ten skan, biorąc dane po prostu sprowadzone są u nas na formularzu. I tutaj – co do tego, że jedna sprawa może być w wielu. Ja szczerze nie wiem, znaczy zaprojektujemy to uniwersalnie, ale spodziewam się, że tak nie będzie. Bo nie wyobrażam sobie sytuację, że w jednym katalogu jest ta sama sprawa i w jednym ona ma okres przechowywania 10 lat, w drugim 5. Uważam, że wtedy, tak jak Janusz powiedział.

**Mariusz Piotrzkowski:** Mhm. Mhm.

**Kamil Dubaniowski:** No, być wręcz kopia, bo to są zupełnie – znaczy. Pismo jest jedno, ale dotyczy 2 tematów, to musimy je przechowywać 2 razy, to możemy usunąć podpięciu, tak, a to po 10.

**Mariusz Piotrzkowski:** Jako 2 sprawy. Rozumiem, znaczy będzie taka możliwość, pewnie fizycznie, ale.

**Kamil Dubaniowski:** Bo, bo te pisma się kasuje bez śladu – tak brakowanie na tym polega, że możesz sobie wtedy wykasować i bez śladu po 10 latach.

**Mariusz Piotrzkowski:** Mhm, czyli taka możliwość byłaby teoretycznie, ale praktycznie mamy wyłączony, bo tak działają. Ja to rozumiem.

**Kamil Dubaniowski:** Tak, tak się spodziewam, tak, że potencjalnie w takiej sytuacji oni muszą skopiować tę sprawę. Bo my nie wiemy, gdzie oni ją wepchną – jak w jednym katalogu będzie miało być 10 lat, a w drugim 5. To usunięcie po 5 latach spowoduje, że ono też się usunie przecież, bo jest jedna w tym katalogu, co ma być 10 lat. Tak, więc potencjalnie spodziewałem się, że trzeba tu niestety ich kopie, ale tak.

**Mariusz Piotrzkowski:** Rozumiem. Czy będziemy też, czy będziemy też w przyszłym roku realizować etap, w którym będziemy to wszystko podłączali do modułu raportowego, żeby dało się to wyciągać, coś ukrywać raportami?

**Kamil Dubaniowski:** Spodziewam się, że taki widok będzie ostatecznie potrzebny dla archiwistów właśnie. To jest ostatni etap procesu, tak.

**Mariusz Piotrzkowski:** To też trzeba mieć dobre endpoint-y do – trzeba będzie dorobić, powinien spełnić jej mechanizmy do tego modułu raportowego, żeby to się ładnie wyświetlało i w ogóle dało się wyświetlić z tych tabel nowych.

**Kamil Dubaniowski:** Nie mamy wiedzy takiej biznesowej. Niestety projekt sprzedaliśmy jako, że jesteśmy specjalistami od tego tematu, a nie mamy wiedzy biznesowej, więc ja nie wiem, jak pracują ci archiwiści – czy oni po prostu lecą po spisie spraw i mają też taki płaski widok tabelaryczny, czy jednak działają na strukturze i szukają katalogów?

**Mariusz Piotrzkowski:** Domyślam się – skontaktować i po prostu poprosić o jakiegoś archiwistę, jakiegoś menadżera czy coś, żeby opisać jako, jakoś z tym pracowali.

**Kamil Dubaniowski:** Mieliśmy tam konsultacje z tym Arturem z firmy, która jest partnerem AMODIT – oni trafiali w AMODIT, a specjalizują się w archiwach.

**Mariusz Piotrzkowski:** Mhm.

**Kamil Dubaniowski:** Ale tam, powiedzmy, że on szył tym, co było, czyli zrobił to w odnośnikach, a też mają jakąś archiwistkę, która – powiedział, że nawet ona nie do końca tam jakoś jest specjalistą, nie ogarniam, więc.

**Mariusz Piotrzkowski:** Fajnie by było mieć kogoś, który powie, jak to dokładnie działa z perspektywy UX, ale to już w kolejnym etapie. To już będziemy robić pewnie w grudniu, żeby zaprojektować to tak, żeby już dla użytkownika było wygodne, bo jak my zrobimy po swojemu, to użytkownicy mogą narzekać, że jest źle. Wiesz, o co chodzi?

**Kamil Dubaniowski:** No. Odnośnikiem najlepszym, moim zdaniem, jest to, jakby w sensie takim użytkowym – bo to na tym pracują już produkcyjne. Od lat ludzie i trzeba by tam się przeklikiwać – są konta testowe, one są ogólnodostępne, czyli możemy po prostu – każdy z nas może się zalogować tym samym loginem, hasłem do demówki – oni ją czyszczą tam co godzinę. Chyba czy codziennie, nie powiem. Tam można poklikać. Ale wiecie, jakby nie znając założeń, to też ciężko się tam odnaleźć, takiej skargi. Dobra, ja się przyłączam do Przemka, nie wiem, czy zablokujecie sobie jakiś czas na spisanie, żebym ja wiedział, co wam rozpisać. Myślę, że wiem po tej końcówce, bo tu się chyba najwięcej teraz zwykle trwało, ale.

**Mariusz Piotrzkowski:** Dobra.

**Kamil Dubaniowski:** Też, wydaje mi się, że taki wkład, jak dostanę od was, to będzie mi łatwiej, żebym poleciał.

**Mariusz Piotrzkowski:** Odważę, ja mówię, że ja się do czwartku znowu jest Trust Center, dzisiaj jeszcze cudem nic nie wpadło, ale założę się, że coś wpadnie prędzej czy później i z tego powodu też mam mniej czasu, więc jeśli miałbym się tym zająć ostro, to dopiero od piątku tak, w pełną parę, nie.

**Kamil Dubaniowski:** Dobra, na razie zacznijmy od koncepcji, żebym ja to był w stanie też przedstawić konsultantom z tego projektu naszym, żeby oni wiedzieli, na co czekają i może na razie w ogóle nie pchali tematu, tak zrobić.

**Mariusz Piotrzkowski:** Wiesz, co mógłbyś zrobić – w porze na was, a ja takiego mockupa prawego panelu, jak to mniej więcej mogłoby wyglądać. I my ci powiemy, czy takie coś by się dało zrobić w miarę OK i wtedy mi pokazał, że jako takie prototyp interfejsu z prawego panelu, jakby to wyglądało w przypadku dodawania spraw, nie.

**Kamil Dubaniowski:** Dobra, dobra, to tego zacznijmy. OK, samą architekturę wam – dobra, to tak zacznijmy. Dobra, ja uciekam.

**Mariusz Piotrzkowski:** Żebyś mogła zrobić – potem nam pokaż to i zobaczymy, co, co, co to w ogóle się da zrobić i czy to zgodne.

**Kamil Dubaniowski:** OK, za chwilkę – jak tam spotkania pokończę, to do tego siądę.

**Mariusz Piotrzkowski:** Dobra, spoko, spoko.

**Kamil Dubaniowski:** Dzięki.

**Mariusz Piotrzkowski:** Dzięki również. To miłego w takim razie.


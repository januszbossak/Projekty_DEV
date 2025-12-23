**Data spotkania:** 5 grudnia 2025, 09:11

---

**Łukasz Bott:** Janusz chyba się włączył na chwilę i wyłączył, bo nas nie było, ale już jesteś.

**Janusz Bossak:** Jestem. Tutaj testujemy PoC, który Marek zrobił. Generalnie coś tam działa, ale jeszcze parę rzeczy trzeba dorobić.

**Kamil Dubaniowski:** Zauważyłem też i pisałem do Marka, co tam zauważyłem, żebyśmy się nie zdublowali, bo ja też testuję.

**Janusz Bossak:** No to może nie ma sensu, żeby dwaj testowali.

**Kamil Dubaniowski:** Wydaje mi się, że powinniśmy, bo każdy ma inne spojrzenie. Po pierwsze, to nie tu, tylko placeholder "znajdź kategorię archiwalną". Bo to nie jest kategoria archiwalna, to jest BE 10. A to jest kategoria archiwalna?

**Kamil Dubaniowski:** Tak, tak.

**Janusz Bossak:** Więc tutaj albo "kategorię JRWA", albo "klasę JRWA".

**Kamil Dubaniowski:** Tak, brakuje mi tam symbolu. Marek powiedział, że musiał go wywalić z listy wyboru, bo coś tam psuło. Prawdopodobnie będzie musiał go dokleić do nazwy, więc zasugerowałem, żeby w ogóle wydzielił osobną kolumnę w bazie danych, w strukturze, na taką nazwę wyświetlaną. Spodziewam się, że jak sklei to do nazwy, to utrudni konsultantom, bo teraz będą musieli symbol wycinać z nazwy, jeśli będą chcieli samą nazwę.

**Janusz Bossak:** Nie, według mnie powinniśmy zdecydować, co ma się tutaj wyświetlić po wybraniu.

**Kamil Dubaniowski:** Sam wybór jest potrzebny, żeby tam był symbol, bo ludzie będą szukać po symbolach.

**Janusz Bossak:** Można szukać, tylko go nie widać. Jak wpisuję "000", to jest "walne zgromadzenie".

**Kamil Dubaniowski:** OK.

**Janusz Bossak:** To jest rzecz, którą trzeba ewentualnie przemyśleć.

**Kamil Dubaniowski:** Pole odnośnik też trochę inaczej się zachowuje niż zwykłe pole odnośnik. Tam możesz wybrać tylko jedną wartość wyświetlaną, a w standardowym odnośniku możesz wybrać pierwszą i drugą wartość wyświetlaną. Gdybyśmy rozbudowali odnośnik do źródła zewnętrznego, to bym sobie wskazał te dwie kolumny: symbol i nazwa.

**Janusz Bossak:** No to niech tak zrobi. Robimy to, więc zróbmy to porządnie. Patrzę na planowanie. To jest planowanie tego, co ma być. Tutaj mam wszystko: widzę ulicę, miasto, powiat i województwo. Jak piszę "nieruchomości"... no akurat nie ma. Trzymajmy się tego walnego zgromadzenia. Już powinno być to "000" według mnie.

**Kamil Dubaniowski:** Sugerował, żeby pokazał też ścieżkę, skąd to pochodzi.

**Janusz Bossak:** Super.

**Damian Kamiński:** Ale jak ty chcesz tę ścieżkę pokazać?

**Kamil Dubaniowski:** W sensie, żeby te szare elementy też się tutaj wyświetliły. Znalazło mi "walne zgromadzenie", które pochodzi z "zarządzania gremiami kolegialnymi", więc powinno mi pokazać całą pozycję.

**Damian Kamiński:** A, w ten sposób? OK, teraz rozumiem, bo nie byłem w temacie. Sprytnie to rozwiązaliście.

**Janusz Bossak:** Tak. Czyli w momencie, kiedy bym wpisał "walne zgromadzenie", to powinno wyświetlić "Zarządzanie" (na szaro), "Gremia kolegialne" (na szaro) i "Walne zgromadzenie".

**Kamil Dubaniowski:** Tak jak u klienta w EZD RP.

**Damian Kamiński:** To jest proste do zrobienia, bo bierze po prostu parenta i tyle.

**Janusz Bossak:** Proste, ale trzeba Markowi dawać feedback, co ma zrobić. Na razie jest podłączone technicznie. Teraz przechodzimy do fazy UX-owej, czyli żeby to ładnie wyglądało. Technicznie widać, że działa. Jeszcze nie sprawdzałem tego, jak wybiorę, czy mam już w tym JSON-ie wszystkie informacje i mogę się do nich dobrać. Bo chodzi mi o to, że tutaj się one nie wpisują.

**Kamil Dubaniowski:** Tak powinno być, ale tego kodu Marek pewnie jeszcze nie napisał.

**Janusz Bossak:** Pewnie nie napisał, aczkolwiek wydawało mi się, że coś tu jest ustawione. Jest przykład z przyciskiem "parse JSON". Zrobię to inaczej. Chciałem zrobić to bez tych JSON-ów.

**Kamil Dubaniowski:** To coś nowego, bo też się nad tym zastanawialiśmy. Teraz jest robione na wzór GUS-u. Identycznie jest ta funkcja JSON. Najpierw źródło, a później sią to rozpracowuje.

**Łukasz Bott:** Sam mechanizm, który Janusz zaproponował, istnieje od dłuższego czasu. Pytanie, czy GUS TERYT i JRWA to obsługują.

**Janusz Bossak:** Pytanie, czy to działa.

**Łukasz Bott:** Do źródła zewnętrznego też, ale wygląda na to, że GUS TERYT i JRWA mogą nie obsługiwać tej składni. O to mi chodzi.

**Damian Kamiński:** Nie wiadomo, czy walidator dobrze to interpretuje, więc to niekoniecznie oznacza, że nie działa.

**Kamil Dubaniowski:** Marek dopytał i zrobił na wzór GUS-u, więc spodziewam się, że tego nie obsłużą.

**Janusz Bossak:** W wersji pierwszej, którą robimy, jest to wystarczające. Jako w trakcie edycji ustawiam na automatyczną. Jeżeli źródło JRWA jest różne od pustego, to wtedy rób to. Działa i elegancko się rzuca.

**Janusz Bossak:** Jak wybieram "001", to jest "rada nadzorcza" i to jest OK. Teraz pytanie, co w tym polu powinno się napisać. W moim przekonaniu powinno być "001, rada nadzorcza".

**Kamil Dubaniowski:** Opis może być bardzo długi, więc trzeba to zmienić na długi tekst. Klasa nie dotyczy tych ludzi. To jest pewnie mniej istotne dla nich, bardziej dla archiwistów. Widzę jeszcze jedną rzecz, o której była mowa przy EZD RP, a tutaj jej nie mamy: oznaczenie czy prowadzenie jest elektroniczne, czy papierowe.

**Damian Kamiński:** To powinno być już na poziomie wyszukiwania, bo mogą być dwa podobne węzły – jeden dla elektronicznych, drugi dla papierowych. To powinien być element, który pojawia się już tutaj.

**Janusz Bossak:** Zastanawiałem się, czy to nie powinno być drzewko (tree), a nie tak spłaszczone do lewej. Żeby było "Zarządzanie", a pod nim z wcięciem "Gremia kolegialne" i "Walne zgromadzenie".

**Kamil Dubaniowski:** Też to sugerowałem. Pamiętajcie jednak, że wyświetlamy tylko pierwszego liścia, bo nie załadujemy tu 900 pozycji. Będzie potrzeba zrobienia wyboru typu tree. Ktoś, kto zna symbole, będzie wolał wyszukiwarkę, a ktoś, kto się uczy, będzie wolał całe drzewo.

**Damian Kamiński:** To, co teraz macie, to bardziej wyszukiwarka niż przeglądarka.

**Janusz Bossak:** Można by to sprowadzić do okienka, podobnego do tego pry polu odnośnik dla procesu, gdzie mamy filtry. Klikam, otwiera się okno z zaawansowanym wyszukiwaniem, gdzie mam kolumny: kategoria, nazwa, opis, kategoria archiwalna. A tu, na formularzu, byłoby do szybkiego wybierania.

**Damian Kamiński:** To połączenie wyszukiwarki i drzewa wyszło jako taki "kadłubek". Sugeruje, że jest drzewem, a jest wyszukiwarką.

**Janusz Bossak:** Więc może ukryć to rozwijanie i zostawić samą wyszukiwarkę? Jak wpiszesz symbol, to pojawi się wynik.

**Kamil Dubaniowski:** To trzeba planować na przyszły tydzień – zrobienie wyszukiwania zaawansowanego z pełnym drzewkiem. Ludzie z biznesu nie znają struktury JRWA, więc jak damy im czyste pole "wpisz", to nie będą wiedzieli, co wpisać. Oni muszą widzieć drzewo na starcie. Później, jak się nauczą, będą używać 5 stałych pozycji. Sugerowali też, żeby podpowiadać 5 ostatnio użytych.

**Damian Kamiński:** To jest nowe pole dla JRWA?

**Janusz Bossak:** To jest pole typu odnośnik do źródła zewnętrznego, podpięte pod specjalne źródło, jakim jest JRWA, tak jak GUS TERYT.

**Damian Kamiński:** Według mnie powinniśmy stworzyć tu nowe okno wyszukiwania z drzewem i wyszukiwarką nad nim.

**Kamil Dubaniowski:** Domyślnie zwinięte, żeby nie muliło przy przesyłaniu danych.

**Damian Kamiński:** Tak, bo JRWA może mieć kilka tysięcy wierszy. Jak ktoś wpisze "45", to wyświetlą się wyniki i będzie można rozwijać w dół.

**Janusz Bossak:** Dokładnie tak to powinno działać.

**Kamil Dubaniowski:** Uzależnimy to od konkretnego źródła?

**Damian Kamiński:** Nie ograniczałbym się do nazwy, bo inne dane też można tak obsłużyć, na przykład działy.

**Janusz Bossak:** Schodzimy na ziemię. Do JRWA powstały osobne tabele, bo to ma konkretne kategorie, nazwy i opisy. To jest specjalizowany moduł. W przyszłości można to uniwersalizować dla innych struktur drzewiastych, ale na razie robimy to pod JRWA.

**Kamil Dubaniowski:** Dobra, zostawmy to. Czy coś jeszcze, czy zatrzymujemy nagrywanie?

**Janusz Bossak:** Muszę się przełączyć na spotkanie z Przemkiem.

**Kamil Dubaniowski:** Podsumowując rano na triażu: potrzebujemy, żebyście wy z Przemkiem wyznaczali nam cele, a my się już zorganizujemy i rozpiszemy zadania. Żeby nie było sytuacji, że my wybieramy cele, a potem wy mówicie, że to nie te.

**Janusz Bossak:** Tak bym chciał. Ta roadmapa jest ważna. W tym sprincie mamy dwa cele: oddanie repozytorium do użytku (instalacja u klienta) i JRWA.

**Kamil Dubaniowski:** Dzięki, cześć.

**Janusz Bossak:** Cześć.

zatrzymano transkrypcję

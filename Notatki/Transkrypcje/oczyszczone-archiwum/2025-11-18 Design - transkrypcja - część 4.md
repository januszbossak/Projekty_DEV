**Data spotkania:** 18 listopada 2025, 11:02 - część 4

---

I ja uważam, że teraz jak im bardziej o tym mówimy, to naprawdę właściwie to można by zostawić tą kwestię. Wizualną. Kamil – rzeczywiście na poziomie wdrożeniowym – a zająć się jedynie tą strukturą. Uprawnień do tego, do tej teczki – to tak jak powiedziałeś – według mnie to jest w tej chwili kluczowe.

**Kamil Dubaniowski:** Tęczową, tak, czyli jak zdecydować, który dział ma mieć dostęp do tych teczek i później w polu? Nie wiem, czy Odnośnik, czy Odnośnik do źródła zewnętrznego, jak wydajnie pokazać zalogowanemu użytkownikowi tylko te teczki, te klasy JRWA, do których on może coś wpiąć. To jest moim zdaniem klucz na start, czyli powinniśmy już wiedzieć, jak dla teczki.

**Piotr Buczkowski:** Nie, to, to nie, to nie będzie żaden Odnośnik do źródła zewnętrznego, to musi być odrębne okienko, oddzielne okienko pracujące na tej strukturze.

**Kamil Dubaniowski:** Dobra, to tak. JRWA dla mnie może być jak najbardziej czymś nowym w AMODIT, tak, to nie będę się upierał, natomiast.

**Janusz Bossak:** No.

**Piotr Buczkowski:** Dobrze, to, co musimy zrobić – musimy zrobić tabelę na to z strukturą tych, plus tabelę na uprawnienia, tak. Zrobić okienko, które pozwala wybrać.

**Kamil Dubaniowski:** Dział.

**Piotr Buczkowski:** Pozycję na podstawie uprawnień. I przypisać ID tego po tej pozycji w jakimś elemencie, na sprawie w teczce, tak.

**Janusz Bossak:** Tak mi się skojarzyło – jak z tym Gugiel, tak, że mamy takie pole, w które wpisujemy adres i on tam z tej bazy wyszukuje. To, to byśmy mieli takie pole do JRWA – on tam sobie w tym JRWA już przegląda i uprawnienia również bierze pod uwagę. To musiałoby być coś w tym rodzaju.

**Piotr Buczkowski:** Najlepiej, tylko co do wydajności to. Najlepiej by było też tak, żeby, powiedzmy. Była jakoś oddzielna tabela, która przypisuje sprawy będącymi tymi teczkami spraw do struktury, na której można działać, ale ona byłaby automatycznie wypełniona ze sprawy, tak. Tak, żeby nie przeszukiwać case definition, tylko na przykład tę tabelę tylko, gdzie będą indeksy wszystkie odpowiednio. Żeby to nie było pole w VARCHAR czy coś, czy case ID.

**Janusz Bossak:** No tak, znaczy to pamiętasz? Kiedyś był taki pomysł i co resztę weszło na właściwe tory, jak żeśmy ten Rossmann rozważali.

**Piotr Buczkowski:** Czy to jest coś bardzo podobnego do tego, co żeśmy – co było na radzeniu architektów? Czyli ta moja tabela do – że stworzyłem do indeksowania – tylko tabela do indeksowania JRWA.

**Janusz Bossak:** Tak. Tak, tak, tak, tak, tak, tak – coś w tym rodzaju by to musiało być.

**Mariusz Piotrzkowski:** I to mnie właśnie chodziło.

**Janusz Bossak:** Bo też. No tak, ale. Tak jak pamiętam, myśmy rozwiązali to w Rossmanie. Bez tego – to tam było zrobione, tak, że ileś tych pól. Pierwszych. Które określają ogólne informacje o tej teczce, czy jakaś tam data? Numer pracownika i tak dalej, i tak dalej, i tak dalej – one są poukładane w tym case definition tam po kolei i na nich. Są poustawiane indeksy. Takie normalne bazodanowe, nie, i dzięki temu później to wyszukiwanie jest na tych ogólnych informacjach bardzo szybkich. Której tak samo mogłoby być – indeks na polu rok, indeks na polu numer. Tej teczki, indeks na polu. Nie wiem, nazwa tej teczki czy tam cokolwiek innego – i na tych 4-5 polach po prostu indeksy założone i będzie działać. Albo tak jak mówisz – to jest lepiej, bo to jest uniwersalne rozwiązanie, nie, które pozwala na nie tylko wykorzystanie tego do JRWA, ale w ogóle po prostu tabela, w której mamy, trzymamy indeksy do określonych pól z case definition.

**Mariusz Piotrzkowski:** Takie coś mają, wspólne są, z siebie robi.

**Janusz Bossak:** Tak.

**Mariusz Piotrzkowski:** Takie ogólne indeksowanie.

**Janusz Bossak:** Znaczy, tak jak powiedziałem – wcześniej mówiłem o tym, że można tak – zrobiliśmy w Rossmanie po prostu zaindeksować tabelę case definition na określonym tam – case VARCHAR 15. I będzie w środku, w tym case VARCHAR 15 tam, na przykład, numer tej teczki. Ale Piotr mówi tu o bardziej uniwersalnym mechanizmie, żeby można było indeksować.

**Piotr Buczkowski:** Bardziej nie bardziej przepisanym do spraw, to ja ten w tak.

**Janusz Bossak:** Ale jeszcze – nie wiem, czy tutaj akurat to przypisanie do JRWA jest istotne. Z punktu widzenia. Jakby mechanizmu, czy to się nazywa JRWA, czy to się nazywa umowa, czy to się nazywa cokolwiek – nie ma znaczenia. Jeżeli chcemy po czymś mieć indeksowane, tak jak zresztą mówiłeś rano na tym – ja tak przynajmniej to rozumiem – to ja sobie włączam mechanizm, że po tym polu mi indeksuje i. I tyle – im indeksuje. Tym mechanizmem, o którym mówisz?

**Piotr Buczkowski:** No tak, ale tam masz płaską strukturę, tak, nie masz struktury przypisanej do jakiegoś takiego drzewka.

**Janusz Bossak:** Ale to też, ale tu też ostatecznie jest płaska struktura. Ja wiem, ja też się na to łapię, że to jest drzewo. Drzewo jest efektem ubocznym. Tak naprawdę to jest płaska struktura, która się składa z czterocyfrowego symbolu, w którym mogą nie wystąpić wszystkie, czyli Zero albo 01 albo 0111 albo 01111 – koniec. Ale ogólnie to jest płaska struktura. Tylko tak dla. Wygody się to przedstawia właśnie w takiej hierarchii drzewka, ale to nie musi być. Samo JRWA jest w zasadzie płaskie, nie? I możemy przetrzymywać w jednej kolumnie? Numerek, który się będzie składał z żera albo 00 albo 000 albo 4 cyfr – i to jest numerek JRWA w jednej kolumnie i wszystko. Tu jest tylko problem, jakby sortowania tego, tak. Że powinno być Zero, potem 01, 02. Potem dopiero jeden. Potem jeden zero. Które od pierwszego numerka było to sortowane, a nie jako string, bo jako string, to wtedy się najpierw posortuje Zero, potem jedynka, potem dwójka, a potem dopiero 01, 02, 03 i tak dalej. Ale to na to też są sposoby, żeby tak to posortować i to jest jedna kolumna. W drugiej kolumnie mamy numer teczki. Który się składa z tego numeru JRWA plus unikalny numer w skali roku w ramach tego węzełka. I potem numer roku.Inter – 3 elementy mogą być też trzymane jako osobne pola i też zaindeksowane i mamy wszystkie elementy, tak – 4 elementy do opisu teczki ten JRWA. Numer teczki jako takiej, numer wewnętrzny dokumentów tej teczce. I i ten rok. I to tyle, nie, wszystko.

**Mariusz Piotrzkowski:** Czy chcemy na lewym panelu – tam, gdzie mamy do wykonania, wszystkie, zamknięte i tak dalej?

**Janusz Bossak:** Muszę się przełączyć do Przemka, wiesz, albo ja mu napiszę, że nie bardzo mamy. Teraz wszyscy są zajęci, widzę.

**Mariusz Piotrzkowski:** Czy, czy w tym prawym panelu?

**Piotr Buczkowski:** Bo ja mam za godzinę szata szkolenie.

**Mariusz Piotrzkowski:** RODO, ja też mam.

**Piotr Buczkowski:** RODO – wciąż coś zjeść, może przed.

**Kamil Dubaniowski:** Czy ja bym tak – znacie nasze potrzeby? Ja bym chyba to tak, jak zrobiliśmy – trochę w tym, w tym repozytorium.

**Janusz Bossak:** A musisz wiedzieć, że tak – dobra, uciekamy?

**Kamil Dubaniowski:** Takiej architektury zostawił wam, czyli koncepcja powinien.

**Mariusz Piotrzkowski:** Ja tylko, ja tylko mam pytanie bardzo ważne – czy chcemy na lewym panelu mieć coś takiego, że użytkownik podobnie jak te zakładki – wszystkie, usunięte, zamknięte, do wykonania – może sobie kliknąć, na przykład, moje JRWA, wyświetlić wszystkie sprawy, jakie on ma w JRWA, żeby nimi zarządzać.

**Piotr Buczkowski:** Wsparciem. Myślę, że będzie miało. Nie – schemat tego jego scope, gdzie będą, na przykład, tylko procesy używane w JRWA.

**Kamil Dubaniowski:** Dotyczący tego.

**Piotr Buczkowski:** I po prostu wszystkie, wszystkie, niezależnie od tego, czy jest wpięte w JRWA, wszystkie, które mają uprawnienia.

**Kamil Dubaniowski:** Raportu.

**Piotr Buczkowski:** Tak.

**Mariusz Piotrzkowski:** Czyżby tam był?

**Piotr Buczkowski:** Będzie widzi.

**Kamil Dubaniowski:** Tak, jak ja wam polecam, żebyście też, nie wiem, jak będziecie o tym myśleć. To jest pewnie reklama mi się odpali, ale.

**Piotr Buczkowski:** Ja to, ja to ja bym traktował jako pewnego rodzaju słownik, tak, słownik.

**Kamil Dubaniowski:** Co dokładnie na tym polega, który ma trochę?

**Piotr Buczkowski:** Słownik hierarchiczny, który ma specjalny, specjalny edytor, który zapisuje tak naprawdę tylko. Uwzględniał uprawnienia i zapisuje tylko. ID. Tego wybranego węzła, gdzie to wpina?

**Mariusz Piotrzkowski:** Tak, właśnie zgadzam się z tym.

**Piotr Buczkowski:** Tak. I specjalnym polu albo specjalnym polu na case definition albo obok tabeli, gdzie będzie case ID itd. I ta wartość, tak. Tak, żeby można – nie można wpisać, nie, nie można wprowadzić kilka, tak wiem, jest tego sprawa.

**Kamil Dubaniowski:** Tak, docelowo jedna sprawa, więc do jednego.

**Piotr Buczkowski:** Tak. Powiedzmy, że z repozytorium – repozytorium mi się to myli, bo tuż przed tym repozytorium.

**Kamil Dubaniowski:** Tak, tam, tam można.

**Piotr Buczkowski:** Było spotkanie.

**Mariusz Piotrzkowski:** No, ja bym proponował, żeby tą strukturę zrobić to – jak się dostanę, to nam Piotr na czacie – JRWA właśnie schema – gdzie będzie po prostu cała struktura zapisana jako każda najmniejsza kategoria osobny wpis w tabeli i z tego się składa – by się wyszukiwało całą strukturę.

**Piotr Buczkowski:** Znaczy struktury – struktura tak w jednej tabeli wszystko, tak, żeby to można było płasko wyświetlić, wyszukać.

**Mariusz Piotrzkowski:** Mhm, tak.

**Piotr Buczkowski:** Plus, plus tabela na uprawnienia, plus tabela na połączenie pomiędzy strukturą a sprawą.

**Mariusz Piotrzkowski:** Języka – tam się z tym do pełności.

**Kamil Dubaniowski:** Zobaczcie sobie na to – taki widok ma człowiek obsługujący LOT Mazowiecki, kierownikiem jakiegoś wydziału. Spis spraw, przez które on ma prawo, do których on ma uprawnień. Wygląda to tak.

**Mariusz Piotrzkowski:** Czy tam jest możliwość wyszukiwania po dziale i obiektuję?

**Kamil Dubaniowski:** Widzę pełnotekstowe, nie wiem, co tu można szukać, nie widzę filtrów. Zobacz – jestem znak sprawy.

**Mariusz Piotrzkowski:** Jeżeli, jeżeli, jeżeli.

**Piotr Buczkowski:** Pytanie, czy, na przykład, może wyszukać w danym węźle i po podwęzłach, tak.

**Mariusz Piotrzkowski:** Właśnie o to mi chodzi.

**Kamil Dubaniowski:** Jest demówka do tego, więc ja sobie poklikam za chwilkę po tym, ale spodziewam się, że ta osoba tych spraw nie ma setki, a raczej, tak jak tutaj, kilka. Kilkanaście i oni powinni się raczej w tym orientować na takiej zasadzie – nawet nie przewidzieli żadnych filtrów. Ja teraz – zobacz, jak wygląda aktualnie – bo te nagrania to już swoje lata mają – jest demówka tego narzędzia z DR-PP, ale nie mają żadnego takiego widoku – przynajmniej ja do tej pory nie znalazłem – gdzie byłaby widoczna struktura i mogę wejść do jakiegoś konkretnego węzła i sobie zawęzić, że tylko sprawy z tego węzła zobaczę. Mam po prostu pełną listę wszystkich spraw, które do których mam dostęp, mam ich znaki.

**Mariusz Piotrzkowski:** Poszukiwania, nie.

**Kamil Dubaniowski:** Mam ich znaki i koniec.

**Mariusz Piotrzkowski:** Bo chodzi mi o to, że wyszukiwanie – na przykład tutaj mamy tą listę – jeżeli chcemy sobie wpisać jakiś tam numer JRWA, jakąś konkretną kategorię, dział czy coś takiego, to to jest to albo 1000 razy bardziej skomplikowane obliczeniowo niż wyszukiwanie, na przykład, po nad sprawach, dosłownie 1000 razy.


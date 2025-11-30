**Data spotkania:** 14 października 2025, 08:00 - część 3

---

**Piotr Buczkowski:** Na telefonie, na telefonie wszystkie – to chociaż nie wiem, czy wszystkie na pewno tabelę tego pierwszego poziomu – same są zamieniane na.

**Janusz Bossak:** No właśnie.

**Mariusz Piotrzkowski:** Mogę pokazać, mam gotowe.

**Piotr Buczkowski:** Na formularz, wygląd formularza, a czy podtabelę zamieniane, to nie wiem.

**Janusz Bossak:** No właśnie, to – bo tak powiedziałeś, jakbyś był pewny, że tak jest. No to pokaż, Mariusz.

**Mariusz Piotrzkowski:** Mogę pokazać, mam gotowe. Tutaj jest na starej wersji, tu jest na starej wersji, normalnie było tak. W wersji.

**Piotr Buczkowski:** No i nieużyteczne, nie należy tak robić, ale działa, coś tam działa.

**Mariusz Piotrzkowski:** W wersji mobilnej, choć wierzyć.

**Piotr Buczkowski:** Chyba za duża na to.

**Mariusz Piotrzkowski:** Mhm, wersji mobilnej. Tak, czyli obie są renderowane jako formularza.

**Piotr Buczkowski:** No, o to, czy – czyli moja pewność była dobra.

**Janusz Bossak:** No właśnie, czyli moja pewność była dobra, czyli na wersji mobilnej. Sam system, nie pytając się użytkownika, jak sobie zaprojektował tą tabelkę, wyświetla tą tabelkę w ten sposób. Według mnie tak powinno działać na formularzu tak samo, bo to jest dokładnie – powinno być to dokładnym odzwierciedleniem.

**Piotr Buczkowski:** Tak. Tak. Takie coś proponowałem.

**Mariusz Piotrzkowski:** Aktualnie jest coś takiego, że na mobilnym to się wyświetla w taki sam sposób. Czyli mamy główną tabelę i tą podtabelę. Jednak w przypadku – tak jest w Lonie napisane – pełnego jest jakiś błąd. Ktoś nie przewidział, że w ogóle tam tabela się może w środku renderować i cały czas kombinuję, jak to naprawić.

**Piotr Buczkowski:** I – nie naprawiaj, zrób tak, żeby było jak na mobilnym.

**Mariusz Piotrzkowski:** OK, dobra, a to to bardzo uprości sprawę. Powiem szczerze, że już się nad tym chyba z 6 godzin.

**Damian Kaminski:** A jeszcze możesz wrócić na ten widok mobilny na chwilkę?

**Janusz Bossak:** No.

**Mariusz Piotrzkowski:** W nowej czy w starej wersji?

**Damian Kaminski:** Nie wiem, to co przed chwilą pokazywałeś. Tam są 2 strzałki, które robią to samo. Pytanie, czy to tak powinno być? Taki był projekt.

**Janusz Bossak:** A ten widok?

**Mariusz Piotrzkowski:** Nie, one nie robią to samo, bo jedna przewija tabelę zewnętrzną, a druga wewnętrzną.

**Damian Kaminski:** Poczekaj, tu masz strzałkę na wysokości – o to właśnie, na środku ekranu. I nad tym masz też strzałkę w prawo, która robi to samo według mnie.

**Piotr Buczkowski:** Tak to.

**Mariusz Piotrzkowski:** A, o to ci chodzi, dobra.

**Piotr Buczkowski:** To robi to samo, tak?

**Mariusz Piotrzkowski:** Tak, ale weź pod uwagę, że to może być wysoka tabela, taka, która ma tam 15, 20 pól na przykład i.

**Piotr Buczkowski:** Chodziło o to, żeby było jakoś tam zaznaczone, tak, że to jest tylko ta część, tak.

**Janusz Bossak:** Paluchem możesz przewinąć tamtą.

**Piotr Buczkowski:** Tylko. Już nie. Kiedyś można było, już nie.

**Mariusz Piotrzkowski:** To ty się teraz?

**Piotr Buczkowski:** Bo ta jQuery, Wrobel, coś tam się zaczęło wieszać i.

**Damian Kaminski:** No bo według mnie to jest do uproszczenia – albo to, albo to, ale no dobra, to już poza tym zgłoszeniem.

**Mariusz Piotrzkowski:** Chyba kolejny błąd zarobię przez przypadek. Dodanie nowego wiersza jest puste. To też zaraz sprawdzę, co z tym jest nie tak, ale to chyba od osobnego zgłoszenia zrobię.

**Łukasz Bott:** Swoją drogą, w tym trybie mobilnym to też nie jest za wygodne do użycia.

**Mariusz Piotrzkowski:** W ogóle to źle działa.

**Janusz Bossak:** Wielkie tabelki w trybie mobilnym nie są wygodne, no bo nie są po prostu. No. Struktura jest złożona takiej tabelki, no bo ma wiele wierszy, w każdym wierszu ileś tych rzeczy. No to to nie jest wygodne do uzupełniania na mobilnym. No, ktoś się uprze, no to wypełnia, no ale. A już tabelka w tabelce to już w ogóle jest.

**Łukasz Bott:** To o tym bardziej mówię, to już wszystko, co masz.

**Janusz Bossak:** No dobra, czyli wniosek jest jaki? Że robimy na wersji desktopowej tak jak jest na wersji tutaj, to co prezentuje Mariusz na wersji mobilnej, tak.

**Mariusz Piotrzkowski:** Czyli coś takiego będzie, tylko te rozpiski czy Wołyń?

**Damian Kaminski:** Czyli, czyli opisując to – jeśli tabela nadrzędna jest wyświetlana w formie formularza, to wszystkie tabele osadzone również są wyświetlane w formie formularza. Tak.

**Łukasz Bott:** Niezależnie od tych ustawień, no.

**Janusz Bossak:** No dobrze, no to jest.

**Damian Kaminski:** Dobra, trzeba zrobić z tego wiki, na wiki zaraz tej dyskusji. Może zamknijmy dyskusję, w sensie zamknijmy nagrywanie, rozpocznijmy następne.

**Janusz Bossak:** Znaczy.

**Łukasz Bott:** Ale czy chcesz tutaj na wiki wydawać, to rozumiem, że to trzeba zrobić, bo w tej chwili nie jest to zrobione.

**Damian Kaminski:** Tylko trzeba to opisać, bo zaraz ktoś powie „a czemu to się nam zmieniło"?

**Janusz Bossak:** Dokładnie.

**Damian Kaminski:** Bo może ktoś tak używał i my wtedy powiemy „dlatego, że takie jest zalecenie projektu". I koniec, nie ma wtedy baga.

**Janusz Bossak:** Cóż, nie – znaczy, jeszcze trochę namieszam, bo może jednak, może jednak dać w takim trybie możliwość wyboru. To są, od czego zaczęliśmy, że jak sobie zaprojektował tabelkę i nie włączył jej w trybie formularza, no to dostanie ją w takim zwykłym trybie, tak. A w mobilnym jest tak, jak Mariusz pokazał. No więc to jest pytanie, czy chcemy mieć równo w mobilnym i na desktopie, czy chcemy, żeby na desktopie jednak można było decydować? Czy ma być jako tabelka, czy ma być jako formularz?

**Damian Kaminski:** Znaczy, jakbyśmy już mogli pokazać jeszcze raz ten ekran, tam on de facto obrazuje ograniczenia. Jeśli to jest tabela maksymalnie dwukolumnowa, to ma to sens w kontekście takiego GUI, tak, czyli XA. Ale jeśli jest to tabelka więcej niż dwukolorowa, no to jest to po prostu niepraktyczne, tak? Bo tam widzimy, że się – nie chodzi mi o tą wersję. To jest desktopowa, bo tutaj jest jasne to, co przed chwilą wyświetlać, że tam o – tylko o właśnie. No to jest po prostu niepraktyczne, no przewijanie jakieś.

**Łukasz Bott:** No to Piotr powiedział, działa.

**Janusz Bossak:** Ale to jest wersja stara formularza. A jak jest na nowej?

**Damian Kaminski:** No ale chcesz, chcesz pozwolić na to tak, żeby to tak było?

**Janusz Bossak:** Jak jest, jak jest – to ta sama sprawa dokładnie.

**Mariusz Piotrzkowski:** Aktualnie wcale się nie wyświetli, bo jest błąd.

**Janusz Bossak:** A, no to to jest błąd krytyczny, jest hotfix – no to naprawienia natychmiast.

**Damian Kaminski:** W sensie, jak, gdzie tu się to powinno wyświetlić?

**Mariusz Piotrzkowski:** Pomiędzy tymi wierszami.

**Damian Kaminski:** Mhm.

**Mariusz Piotrzkowski:** To jest właśnie ten błąd, który próbując wczoraj rozkminić, no i tam się dużo zmieniło, że mi to zajęło chyba z 3 godziny, bo to w ogóle oglądać, jak to działa wszystko. No i teraz pytanie, co mam z tym zrobić, jak to ma w końcu działać? Nie. Bo się znowu pogubiłem.

**Janusz Bossak:** Po pierwsze, w ogóle ma działać. Znaczy, żeby w ogóle się tabelka pokazała. Jest kwestia tylko w jakim trybie – tak, czy w trybie tabelkowym, czy w trybie formularzowym.

**Łukasz Bott:** No ale to jest, jeżeli to robimy, to dla nowego formularza, to może zróbmy, że docelowo tak. Już Mariusz ma roboty, jakoś robić to – to niech zrobi to docelowo może tak.

**Janusz Bossak:** Ale Mariusz teraz – tam jeszcze raz, może coś się pogubiłem. Jeżeli ten formularz teraz, ten który masz, wyświetlisz w trybie mobilnym, to będzie działać dobrze, tak?

**Mariusz Piotrzkowski:** Jeżeli w mobilnym, to powinien działać, wydaje mi się, dobrze. Ale tam przed chwilą miałem, miałem jeszcze jakiś błąd przy dodawaniu wierszy, ale to wyświetlanie jest poprawne w każdym bądź razie.

**Janusz Bossak:** To zrób tak, żeby – no chyba tak to powinno działać, nie, w trybie desktopowym jak w mobilnym.

**Damian Kaminski:** A możesz jeszcze raz wrócić na tą wersję marcową? Mhm, możesz teraz zamienić ten widok tabeli wewnętrznej na układ formularzowy? Żeśmy zobaczyli, bo teoretycznie będziemy się zbliżać do tego efektu, który teraz zrobisz. Zobaczymy, jak ten – edytuj pola formularza. A nie, to to dobre. Czyli coś takiego dostaniemy konsekwencją? Czyli zobaczcie, że tam jest też scroll poziomy, tylko wyświetlanie jest pionowe.

**Mariusz Piotrzkowski:** To są jakieś glitche w ogóle, znowu na starej wersji też to jest całe w ogóle według mnie – dobrze robi.

**Damian Kaminski:** No właśnie. Nie, a przepraszam, to. OK, dobra, no właśnie, bo tak, tak było zaprojektowane desktopową, tak, czyli tam nie było tych strzałek. Tylko jest właśnie pionowo z scrollem, tak, poziomym przewijania.

**Łukasz Bott:** Nie.

**Damian Kaminski:** Wierszy w formie kolumn.

**Janusz Bossak:** No nie wiem, czy to w takiej wersji jest wygodniejsze czy nie.

**Damian Kaminski:** No według mnie nie. Tutaj te „Dodaj wiersz" i „Dodaj wiersz" 2 razy, to w ogóle nie wiadomo, o co chodzi na dole.

**Janusz Bossak:** Czyli.

**Damian Kaminski:** To jest 2 razy, w trzeciego kolumnie jest raz.

**Janusz Bossak:** Chyba wniosek jednak jest taki, że to trzeba zrobić i tak, i tak, i tak. Znaczy.

**Mariusz Piotrzkowski:** To chyba jakiś glitch.

**Janusz Bossak:** Czyli w formie tabelkowej wtedy, kiedy ma to sens w niektórych. Albo w formie takiej, ale też dobrze. Jeżeli to ma sens dla innych, tak.

**Damian Kaminski:** Znaczy pytanie, czy w ogóle ktoś takiego zagnieżdżenia używa? No ale tego niestety nie wiemy. Yy, no pewnie można to jakoś sprawdzić na chmurach, ale.

**Janusz Bossak:** Dobra, przejdźmy. Chodzi mi o to, żeby Mariusz miał jak najmniej roboty i żebyśmy mieli temat jakoś ogarnięty. Jeszcze raz nowy widok. Mobilny, pokaż go. Tego przypadku.

**Damian Kaminski:** Działa mobilny, działa, tak, Mariusz?

**Janusz Bossak:** Nowych.


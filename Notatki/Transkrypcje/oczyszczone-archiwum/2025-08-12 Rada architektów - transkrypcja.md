**Rada architektów 2025-08-12 - Transkrypcja**

**Data:** 2025-08-12
**Uczestnicy:** Janusz Bossak, Łukasz Bott, Piotr Buczkowski, Adrian Kotowski, Anna Skupińska

---

**Adrian Kotowski:** Mogę chwilę? Coś pokażę. Wpadłem na szybko na pomysł w temacie przesyłania plików. Jak mamy ten przykład, załóżmy pod API wysyłane, to można by zrobić, żeby wprowadzić zmienną, która by odniosła się do listy załączników na sprawie.

**Piotr Buczkowski:** Tak, tak, można jak najbardziej. Trzymając dokument, możesz tak użyć. Weź przejdź do Bearerów tutaj.

**Adrian Kotowski:** No i to po prostu w tej funkcji było... Czekaj, tu zresztą są... jedne to jest `Forms`, a to powinny być...

**Piotr Buczkowski:** No bo gdzieś niżej, niżej, chyba pod Formsami, o ile pamiętam.

**Adrian Kotowski:** Endpoint nie. To jest kwestia [niezrozumiałe]... o jest, tak? Security?

**Piotr Buczkowski:** No właśnie takie podejście, jak niżej, tak i tutaj, żeby też dało się to, co teraz na samym dole widać.

**Adrian Kotowski:** OK. Czyli po prostu parametr.

**Piotr Buczkowski:** Tylko, żeby tutaj się też dało to zrobić.

**Adrian Kotowski:** OK, dobra.

**Piotr Buczkowski:** I na przykład użyć `DocumentName` i `DocumentValue`, gdzie jest Base64, powiedzmy.

**Adrian Kotowski:** Ale to już teraz można zrobić, bo tu zakładamy, że jest taki format, gdzie jest klucz-wartość.

**Piotr Buczkowski:** No tak, tak, bo to jest ten właśnie...

**Adrian Kotowski:** Nowa linia jakby nie ma.

**Piotr Buczkowski:** Podobnie dla tej `multipart`, to jest trochę inaczej, bo to jest takie jak z [niezrozumiałe], no ale żeby to prawidłowo było sformatowane, tak?

**Adrian Kotowski:** Tak, no nowa linia przełamuje i kolejna para klucz-wartość. Tak to można sterować.

**Piotr Buczkowski:** No ale żeby właśnie nie trzeba było definiować takich parametrów, jak tutaj jest `CustomHeaderKey1`, `CustomHeaderValue1`.

**Adrian Kotowski:** Tak, tak, znaczy no wiadomo, to stało... Był [pomysł], żeby płynąć przez pliki, bo wszystkie właśnie to tak na szybko... to, że teraz możemy lepiej było zrobić tak.

**Piotr Buczkowski:** No właśnie, chodzi mi o to, żeby nie iść po linii najmniejszego oporu.

**Adrian Kotowski:** No i też fajnie mieć mniej parametrów, bo to jednak to jest ciężko się później przewija.

**Piotr Buczkowski:** No tak, tak i takie Header 1, 2... nic nie mówi.

**Adrian Kotowski:** Można przerobić tutaj się to już tak, to już jest tutaj w nagłówkach... można to zrobić i w tych parach `form-data`.

**Piotr Buczkowski:** No na `multipart/form-data`, tak? Czy jak to się nazywa... nigdy nie potrafię tego zapamiętać.

**Adrian Kotowski:** No ale to nie byłoby dużo roboty, bo już ten... Też właśnie pytam jeszcze tej Form i te `form-data` tak? Czy `x-www-form-urlencoded` też można przerobić, ale to nie byłoby dużo roboty, bo już tam są gotowe. I na przykład to, żeby tam i [niezrozumiałe] to też jest chwila, żeby to dodać.

**Piotr Buczkowski:** No tak, tak. No i warto właśnie tą tablicę `documents`, żeby się dało udać, bo rzeczywiście to jest...

**Lukasz Bott:** Do...

**Adrian Kotowski:** Prawda.

**Piotr Buczkowski:** To bardzo popularne może być, tak bardzo przydatne.

**Janusz Bossak:** Mhm, no dobra. Ja tutaj wrzuciłem na czata ten link do zadania związanego właśnie z tym `foreach document`, tak to co [Adrian] tam chce. Tak, żeby też on tutaj gdzieś się pojawił. No dobra. Potem temat mamy Łukasz, co tam dalej?

**Adrian Kotowski:** Jeszcze mam taki szybki temat, bo nie wiem, czytali, będzie potrzebny nam ten temat właśnie tego interfejsu do Joba, który spowodował ten problem z tą kompatybilnością wsteczną. To mogę też pokazać. Były duże problemy, teraz udało się to jakoś opanować. W każdym razie było tak, że tutaj Marek dodał, czy rozszerzył interfejs ten, dodał do nazwy pole `Owner` (?) i to do wszystkich... w sensie czy istniejących Jobów, które są budowane w projekcie w solucji AMODIT, ale też są Joby, które są budowane poza solucją AMODIT, czyli na przykład wszystkie Joby integracji. I to spowodowało, że tam brakowało definicji tego nowego pola i te wszystkie Joby [przestały działać].

**Piotr Buczkowski:** Wiem, sprawa zdaje się olbrzymia problemem w Rossmannie, na szczęście tylko na Stage.

**Adrian Kotowski:** Tak, no ale to już to...

**Piotr Buczkowski:** No w sensie te [niezrozumiałe] problemy z odczytem na produkcji z tej biblioteki bazowej, bo chyba już... No właśnie. Ona w swojej wersji testowałem wcześniej na wersji, która już ma to poprawione...

**Adrian Kotowski:** W każdym razie tu zaproponowałem, żeby stworzyć właśnie nowy interfejs, który byłby tylko w tych Jobach, gdzie [nowa funkcjonalność] jest wymagana. To powoduje, że też te istniejące Joby nie będą mieć problemu z kompatybilnością, bo one nie będą tego interfejsu implementowały. Za tym, co dziś Piotrek...

**Piotr Buczkowski:** Znaczy tam napisałem wczoraj Markowi, ale zapomniałem, że jest na urlopie. A da się tam lepiej zrobić?

**Adrian Kotowski:** Wiesz, myślę, że coś się jakoś tak w sensie...

**Piotr Buczkowski:** Czy da się to lepiej zrobić tak, bo... Ktoś mówi?

**Adrian Kotowski:** Na cieście myślałem jeszcze nad tym, że można na przykład zrobić... dodać wtedy, jakby to pole jest domyślnie ustawione, ale wymaga, żeby było nadpisywane w każdej klasie. To jedna opcja była, no a druga to [nowy interfejs].

**Piotr Buczkowski:** Dobrze, ja już muszę się zastanowić.

**Adrian Kotowski:** No to na razie zostawmy tak jak jest, no bo to [rozwiązanie] jest bezpieczne w miarę. A jeszcze inny mam taki temat, bo chciałem dodać taki test jednostkowy w związku z tymi częstymi problemami z kompatybilnością wsteczną. Miałbym test, który by z całej biblioteki `AMODIT.Classes` lub też innych rzeczy typowo wszystkie publiczne metody zapisywał co jakiś czas do pliku, taki snapshot. I teraz byłby taki test jednostkowy, który za każdym razem by się uruchamiał i porównywałbym stan, który jest w tym pliku (przypiętym do naszego projektu) z tym, co teraz aktualnie jest. Na podstawie tego byśmy mogli na przykład zweryfikować, czy ktoś zmodyfikował jakoś publiczne metody, albo po prostu usunął. Żeby nam można powiedzieć, wcześniej wykrywał te sytuacje, że jest jakiś problem z kompatybilnością wsteczną, więc to już się takie dość proste rozwiązanie i nie jest to trudno zrealizować.

**Janusz Bossak:** No dobry pomysł.

**Adrian Kotowski:** Myślałem odnośnie, żeby zrobić coś takiego samemu, ale w kontekście tych interfejsów. Jak mi się uda trochę czasu odłożyć, czy to się tym zajmę, żeby coś takiego przygotować, to by działało jako normalny test jednostkowy i tam co jakiś czas trzeba by tego snapshota aktualizować, żeby miało aktualną listę tych metod. Nie wiem czy jakieś inne tematy, czy jestem jeszcze potrzebny na spotkaniu?

**Janusz Bossak:** Po części tak, bo jest ten temat zastępstwo za grupę, co tutaj Piotr też przed chwileczką na Daily mówił, że to inaczej działa w tych starych zastępstwach, a inaczej w nowych. Piotrek byś mógł rozwinąć myśl?

**Piotr Buczkowski:** Dobrze, to jeszcze za chwilę przełączam. Chodzi o zastępstwo za grupę, tak, czyli stary mechanizm. Jeżeli ja jestem, zastępuję osobę i ta osoba należy do grupy A, to ja też widzę sprawy przypisane do grupy A. W nowym mechanizmie tego nie widać. No to oczywiście wykryłem testując tę zmianę sposobu pobierania dla zastępstw.

**Adrian Kotowski:** Pamiętaj, że było takie założenie, że ten nowy mechanizm nie wspiera teraz tych zastępstw z grup, na przykład...

**Piotr Buczkowski:** No właśnie stary wspierał. Stary wspiera. Trochę jest niespójne.

**Adrian Kotowski:** To właśnie mógłby być ten problem z tym, że teraz to jest pytanie, czy jeszcze bardziej jakby można powiedzieć, jeszcze bardziej byłyby złożone, bo teraz też ten mechanizm, że my to jakby te zapytania rozbijamy tak bardziej szczegółowo.

**Piotr Buczkowski:** Znaczy, na UC, gdyby korzystali z nowego mechanizmu zastępstw, pewnie nie byłoby problemu tego wydajnościowego, no bo nie byłoby tej grupy tak, 70 czy tam iluś grup. Tylko 70, a zastępcy? A korzystając ze starego stan był 70 + 70 grup, tak z 40 parametrów User. Ponad 140. Już uruchamiam... Trochę nie byłem przygotowany.

**Adrian Kotowski:** Ale też pytanie, czy te grupy do klienta są jakieś takie duże, na przykład ten, czy to nie jest 5 osób, czy nie wiem z 50?

**Piotr Buczkowski:** Nie, nie ma żadnego znaczenia. Zapytany jest ID, a ID użytkownika tego abstrakcyjnego dla grupy. Nieważne ile w niej osób jest. Ta osoba, ten mój użytkownik, `Buczko23`, jest w grupie 1. Jest zastępstwo za grupę, tak? Sprawa jest przypisana do grupy 1. A ta osoba w grupie HR jest, a w grupie 1 nie ma.

**Anna Skupińska:** Zaraz, czyli to użytkownik jest przypisany do tej grupy?

**Piotr Buczkowski:** Bieżący nie, ale bieżący użytkownik jest zastępcą użytkownika `Buczko23`. A on jest w grupie 1. No i Użytkownik 22, będąc zastępcą, widzi sprawę przypisaną do grupy 1, ponieważ jest zastępcą członka grupy 1. W nowym mechanizmie tego nie ma.

**Janusz Bossak:** Pamiętam, myśmy na ten temat dyskutowali wtedy dość szeroko. Że... gdyby...

**Piotr Buczkowski:** Ale też dziwiłem się, że w starym mechanizmie jest tak zastępstwo za grupy.

**Janusz Bossak:** No właśnie mi się też tak wydawało, bo te dyskusje, że nie ma sensu zastępować kogoś z grupy, bo po to jest grupa, żeby ktoś inny z tej grupy to wziął.

**Adrian Kotowski:** Tak, też właśnie to pamiętam.

**Piotr Buczkowski:** Tutaj jest ten sam mechanizm, że 22 jest zastępcą 23. To tylko sprawy przypisane do 23. Tak nie ma do grupy 1.

**Janusz Bossak:** No właśnie i teraz będzie. No bo to ma daleko idące konsekwencje i na pewno trzeba to dobrze przemyśleć. Ale jeżeli grupa jest jednoosobowa... bo to to jest chyba najważniejszy przypadek. Grupa jednoosobowa, grupa jako rola, tak na przykład Dyrektor Finansowy. I jest tam w tej grupie Dyrektor Finansowy jedna osoba, no i kto go zastępuje? Wtedy... znaczy to tak powinno działać dla grup jednoosobowych.

**Piotr Buczkowski:** Może można zrobić taki wyjątek, że dla grupy jednoosobowej tak. Ewentualnie ustawienie grupy, że zastosować zastępstwa. Też się da zrobić teraz.

**Janusz Bossak:** O, o to też może być. Bo powiedzmy, tak jak na przykład jest w Rossmannie, z góry wiadomo, że jest grupa jakaś tam HR, która zawiera, nie wiem 20 ludzi... no i nigdy nie będzie ta grupa pusta. Więc ktoś z tej grupy się zajmie tymi sprawami i nie potrzebuje jeden członek mieć zastępcy, którym prawdopodobnie albo z dużym prawdopodobieństwem będzie inny członek tej grupy.

**Piotr Buczkowski:** No to... Może i rzeczywiście to jest takie coś, że robimy grupy czasami jako rolę. Żeby jak ktoś kogoś innego przypisuje, że tylko jest jeden członek, tak, żeby łatwo było zarządzać, kto jest na przykład...

**Janusz Bossak:** Tak, tak. Na przykład Dyrektorem Finansowym tak, albo tak jak u nas tam RODO. Tak, no to jest jeden człowiek, Radka tam wpisujemy, ale za chwilę może nie być Radek, może być ktoś inny, tak, bo się zmieni, ale rola pozostaje.

**Piotr Buczkowski:** I nie musimy zmieniać wtedy reguł procesów.

**Janusz Bossak:** Tak, no i w takim przypadku jednoosobowej grupy zastępstwo dla takiej grupy ma sens.

**Piotr Buczkowski:** O czym mówię, można dodać parametr "uwzględnij zastępstwa dla tej grupy". Tak, nie wiem czy jak to nazwać lepiej.

**Lukasz Bott:** To może lepiej właśnie ten parametr.

**Janusz Bossak:** Wiecie no... Można jeszcze jedną [opcję] przyjąć, znaczy komplikując sobie sprawę. Że jeżeli zastępstwo jest do grupy, czyli jeden członek grupy zastępuje niby drugiego członka grupy, no to to nie uznajemy tego jako zastępstwo, no bo i tak i tak to są członkowie grupy, więc mogą wykonać. Ale jeżeli członek grupy daje zastępstwo komuś spoza grupy...

**Piotr Buczkowski:** No tak, to... Znaczy tam jest nawet jest jakiś `DISTINCT` robiony teraz, żeby 2 razy nie pytać o tę samą grupę.

**Janusz Bossak:** No nie wiem, znaczy rozumiem, mamy problem taki, że stary mechanizm to uwzględnia, nowy nie uwzględnia. Pytanie co chcemy? Czy docelowo chcemy przejść na całkowicie na nowy mechanizm?

**Piotr Buczkowski:** No trzeba kilka godzin, żeby to dodało do prac nad tym, nad tą zmianą. Ujednolicić.

**Adrian Kotowski:** Widziałem taki pomysł na przykład, jak gdyby zrobić taką... można wyjść na trochę tak wizualnie to oszukać użytkownika. Na przykład teraz jak w wyświetlaniu jesteśmy [zalogowani], to na przykład patrzymy jako użytkownik, na przykład Szymon Kowalski... żeby jakby to powiedzieć... to samo zapytanie, tylko że tego użytkownika... po prostu podmienić ID jednej grupy, na przykład, że w określonej sprawie konkretna grupa.

**Piotr Buczkowski:** Ale to jest... o to chodzi Ci?

**Adrian Kotowski:** Tak, ale jakiego? Ale drugie, bo to jest z innej perspektywy.

**Piotr Buczkowski:** Potem to też dodanie tego, żeby to działało dobrze, też trochę zajmie w nowych zapytaniach. Ale obsługa w zapytaniu tego zajmuje 0,1 kodu tego co było.

**Janusz Bossak:** No no. No dobra słuchajcie no. Albo zostawiamy, że jest jaki jest, czyli stary mechanizm obsługuje, nowy nie obsługuje, tylko to musi być gdzieś w instrukcjach, dokumentacji i tak dalej. Ale dodałbym to rozróżnienie... I stary pewnie też powinien obsługiwać absolutnie tą sytuację grup jednoosobowych lub tak jak powiedział Piotr, może to nawet bardziej jest sensowne - grup oznaczonych, że uwzględniają zastępstwa. Ale na pewno w 100 procentach według mnie zastępstwo dla grup jednoosobowych powinno być uwzględniane.

**Adrian Kotowski:** Jeszcze poczekajcie chwilę... W jednym mechanizmie, założenie, że to jest weryfikowane ID mojego aktualnego użytkownika. Mi w sumie chodziło mi o to, żeby po prostu można było...

**Piotr Buczkowski:** Nie, to tutaj tylko, bo tam są teraz 2 zapytania. Nie wiem czy pamiętacie. Jest `CASE...` ta system to jest ten gdzie ja albo mojej grupy `UNION`... Działań kategorii, gdzie dozwolonym zastępstwo... I te sprawy, które są jako zastępcę, czyli pobranie tamtego filtrowania, tylko ta zostaje tak. Przypisane do osób, które je zastępuje.

**Anna Skupińska:** Tak więc jak wyszukujemy po... [niezrozumiałe].

**Piotr Buczkowski:** Znaczy, to ja mówiłem jakie zrobione zapytanie, no to takie co nie...

**Anna Skupińska:** A chodzi ci, że w starym to było kod od starego?

**Piotr Buczkowski:** Nie, moja zmiana była taka, że tutaj zamiast tego `UNION` było `OR`.

**Anna Skupińska:** A rozumiem, że jak było `OR` to były problemy wydajnościowe?

**Piotr Buczkowski:** Tak.

**Anna Skupińska:** No ciekawe, że jak było `OR` to były problemy wydajnościowe, a nie ma jak są 2 selecty.

**Piotr Buczkowski:** Tak wyszło z testów na UC.

**Janusz Bossak:** W sumie to dziwne, bo pamiętam kiedyś dawno temu lata temu zawsze była mowa, że `UNION` to jest bardziej obciążający i należy unikać, dzisiaj dla Unionów. A teraz wychodzi, że jednak...

**Adrian Kotowski:** No i nie robi tym, czy sobota były tak naprawdę...

**Piotr Buczkowski:** Być może serwery bazodanowe nauczyły się robić wydajne tabele tymczasowe.

**Janusz Bossak:** O. No dobra.

**Piotr Buczkowski:** No to dobrze, to zrobię tak: pierwsze ryzyka, że domyślnie dla jednoosobowej grupy stosujemy. To będzie proste. A po drugie trochę większe, no bo to wymaga pytania jakiegoś interfejsu, że zaznaczamy opcję "Uwzględnij daną grupę w zastępstwach".

**Anna Skupińska:** Będziesz Piotr dodawał nową kolumnę?

**Piotr Buczkowski:** Nie wiem jeszcze, nie wiem jeszcze.

**Anna Skupińska:** Czy można łapać? No bo jak coś to jest [stałe] to będzie można to uwzględnić bezpośrednio w SQL. A tak to będzie trzeba jakby wyszukiwać je najpierw przed zrobieniem SQL limitu tutaj dodawać.

**Piotr Buczkowski:** Znaczy tu i tak teraz ja zrobiłem tak, że nazwy są przekazywane przez numer, po prostu wpisany numer, a nie przez parametry, tak, bo wcześniej tutaj było tak wyglądało zapytanie... No to teraz jest po prostu ta lista ID-ków.

**Janusz Bossak:** Dobrze, ja mam jeszcze jeden temat jak że mam chwilę. Od tutaj Zbigniewa Szymanowskiego, temat, który się wielokrotnie już pojawia i pojawia się po raz kolejny. A mianowicie ustawianie szerokości kolumn w formularzu. Mieliśmy, pamiętacie taki pomysł i to Marek raczył nawet realizować, to chyba dla Polmleku była taka tabelka kompaktowa. No ale wróćmy do jakby najprostszej rzeczy, że w ustawieniu danej kolumny w tabeli w definicji gdybym wpisał, nie wiem 50 pikseli, żeby to się wyświetlało jako tutaj nie wiem 50 pikseli.

**Piotr Buczkowski:** Wiesz, nawet jest na to już w ogóle... Już nie zostało oprogramowane tak od dawna jest ten pomysł.

**Janusz Bossak:** No to zróbmy może go, bo to jest tak wiele tych rzeczy tak często to się jakby powtarza.

**Lukasz Bott:** No to to odnośnie Zbyszka czy też to też ten temat w PKI się pojawił?

**Janusz Bossak:** No no tak to jest. Generalnie to się myśmy się po prostu już do tego przyzwyczaili tak, ale no jest coś takiego jak wiesz tutaj te ilości czy jakieś jednostki miary, które są najczęściej właśnie takim symbolem typu KG, SZT. No ale zależy jakie to są ilości, no ale w bardzo wielu przypadkach te ilości się ograniczają tak jak tutaj dostałem 999 na przykład maksymalnie, albo tysiąca, no i nikt nie potrzebuje takiej [szerokości].

**Lukasz Bott:** No to nawet wiesz, słuchaj, to nawet jeżeli tutaj byś 9 cyfrową liczbę wpisał w ilości, to nadal masz połowę okienka, tak?

**Janusz Bossak:** To dotąd będzie gdzieś tak. Także, jeżeli mamy to zrobić, to zróbmy, jeżeli to nie stoi w sprzeczności z jakimiś tam innymi rzeczami. To dodajmy taką rzecz tutaj, jakiś tam właśnie jakiś symbol czy coś, no to żeby to po prostu można było te kolumny robić węższe. Jedyne co widzę jakiś problem, chociaż nie wiem, czy to jest problem... czy tabelka w tabelce? Ale to chyba na to wtedy dla tabelki w tabelce nie określamy szerokości tak, tylko jakby...

**Piotr Buczkowski:** Znaczy ta tabelka w tabelce jest w nowej linijce.

**Janusz Bossak:** Raczej chyba dla dowolnego typu kolumny, no bo co tekstowe ma sens? Długi tekst ma sens.

**Piotr Buczkowski:** Jak najbardziej można też zwiększyć, tak.

**Lukasz Bott:** Słuchajcie zwiększenie przyda się przy polu typu Odnośnik.

**Piotr Buczkowski:** Znaczy udostępniam ekran, tak. Widzicie, to jest prosty rzecz, tam te 2 pola były. Oddzielnie dla wyświetlania, oddzielnie dla wydruku. Żeby się dało styl wpisać, tak czyli `width` nie wiem co tam można jeszcze było wpisać. Można to użyć jako właśnie suwak, tak?

**Janusz Bossak:** Nawet tak w ten sposób, bo tam wiecie konsultanci kombinują i wpisują kiedyś JavaScripty żeby coś tam zrobić.

**Piotr Buczkowski:** Już wiem, dlaczego to było w starym, że można... Jeżeli nie chcemy, żeby tam zawijało.

**Janusz Bossak:** No dobra, no i teraz możesz pokazać to, co teraz zmieniłeś. Czy to ma oddziaływanie na ten? Nie ma, bo to nie jest [wdrożone].

**Piotr Buczkowski:** Nie. Nie ma, nie było, jakoś był kiedyś pomysł dodałem kolumny, ale nie było czasu zrealizować.

**Anna Skupińska:** A nie powinno być trudno tego zrealizować. Można byłoby zrobić zadanie, skoro już jest kolumna.

**Janusz Bossak:** No to zróbmy zadanie i to zróbmy. Będzie fajnie, bo to przy okazji właśnie tego nowoczesnego wyglądu formularza.

**Piotr Buczkowski:** Nie wiem pytanie jak to zrobić, po prostu dajemy wpisać użytkownikowi dowolny styl CSS z palca czy robimy...?

**Anna Skupińska:** Pytanie, czy można umieścić jakiś kod złośliwy w CSS-ie. Poza tym, jeżeli ktoś ma już dostęp do bazy danych, no to można.

**Piotr Buczkowski:** Nie.

**Janusz Bossak:** Znaczy wiecie co? Wolałbym nie dawać aż takich możliwości, przynajmniej na początek. Zostawmy czy po prostu kilka wybranych?

**Lukasz Bott:** Kilka wybranych styli, a pewnie najczęstszym to będzie szerokość po prostu.

**Janusz Bossak:** Na razie zróbmy szerokość i ewentualnie to zawijanie, tak czy ma zawijać nie jako opcja i tyle. Jak będą chcieli coś kiedyś więcej to będziemy kombinować. Mamy przestrzeń tak, natomiast na razie niech to będzie w ten sposób, niech to się tak zapisuje. W razie czego jakiś bardzo zaawansowany konsultant będzie mógł sobie tutaj wejść i to powpisywać więcej takich rzeczy, które będzie chciał.

**Anna Skupińska:** Dobra w sumie. Oczywiście, jeżeli ktoś z bardziej zaawansowany może wpisać więcej, to zawsze może wpisać coś złośliwego.

**Piotr Buczkowski:** Co? Tylko administrator może.

**Anna Skupińska:** No tak, ale to też trochę zależy jak tam będziemy wkładać, jeżeli to będzie `style` w elemencie, a to można na przykład zrobić, że o koniec stylu i teraz wpisuje jakieś nie wiem `onClick` albo on coś tam i wpisuje JavaScript więc...

**Janusz Bossak:** No ale wiesz. Ale już tutaj Łukasz potem będzie miał pan testy i się tam przyczepi. Jakiś pan tester, że można wpisać coś nie.

**Lukasz Bott:** Ania ma rację, że zwróćmy na to uwagę, dlatego zróbmy tylko ograniczoną liczbę i tylko i wyłącznie przez interfejs. Tak no oczywiście jak ktoś grzebie w bazie danych, to na swoją odpowiedzialność tak.

**Janusz Bossak:** Dokładnie. Znaczy po stronie jakby frontendu czy tam na backendu, który odczytuje z bazy danych, powinien odczytywać oczekiwane rzeczy. Tak więc oczekiwaną rzeczą jest tylko width, z odpowiednią liczbą.

**Anna Skupińska:** I tak i tylko te rzeczy będzie wkładać. Jak ktoś dopisze coś więcej to się nie pojawi.

**Janusz Bossak:** To się nie pojawi, bo tego nie interpretuje, tak jak gdyby uczymy go interpretować tylko te rzeczy i koniec. Tak, jest coś innego, cokolwiek tekstu tutaj bla, bla, bla "Kubuś Puchatek", to on tego nie interpretuje ani jako błąd, ani po prostu.

**Lukasz Bott:** Ignoruje.

**Janusz Bossak:** Ignoruje i tyle. Tak to powinno działać. No dobra, no to mamy zadanie dobrze określone. To ja z moich takich tematów to wszystko.

**Lukasz Bott:** Ja ja to bym się rozłączył, bo chce się jeszcze do spotkanie o jedenastej.

**Janusz Bossak:** Dobra, dzięki.

**Anna Skupińska:** Mam pytanie Janusz związane z tym featurem, to chodzi po prostu o to, żeby można było do tabel do raportu typu tabel wsadzać kolory, które mają agregację tak, żeby się ten kolor był z gradientem. Znaczy no to to nie działa do końca dobrze, bo on patrzy tylko na wartości z danej strony. Trzeba zrobić tak, żeby on pobierał jakby wszystkie wartości, żeby się to prawidłowo kolorowało.

**Janusz Bossak:** Tak, tak, tak. Znaczy ma sens kolorować na przykład na raporcie tabelarycznym, który nie jest raportem agregującym nic, wartości. Czyli mamy jakąś na przykład nie wiem kwotę wynagrodzenia. Załóżmy czy cokolwiek innego wartość sprzedaży, no i będę miał to pokolorowane według maksymalnej i minimalnej i tam zerowej wartości. Przyszłościowo teraz już tak mówię o kolejnych jakby możliwościach to powinna być jakaś możliwość dzielenia na więcej jakby elementów. Czyli powiedzmy, że od tam maksimum do jakiejś wartości X, to jest tam właśnie czerwone, pomiędzy czymś, a czymś to jest jakieś... i niekoniecznie jest gradientem. Tylko jest jakimś kolorem, który określam na jakieś wartości. No ale to na razie zostawmy. To co robimy, to robimy głównie pod WIM i pod wymaganie pana Piotra, że on by chciał tam mieć inne kolory niż te które...

**Anna Skupińska:** Tak, ja oddałam do testowania te zmiany kolorów, gradientów na `AMODIT Local` jak na razie tylko to ma, tylko jest dla typu Pivot i dla mapy. Dla innych to za bardzo kolorów z agregacją się nie da wstawić, nie ma to chyba sensu.

**Janusz Bossak:** Dobra, to ja teraz będę sobie tutaj międzyczasie testował i będę ci zwracał jakieś tam uwagi, informacje.

**Anna Skupińska:** Dobrze. Dla mnie to wszystko.

**Janusz Bossak:** Dobra, to dzięki bardzo. Na razie.

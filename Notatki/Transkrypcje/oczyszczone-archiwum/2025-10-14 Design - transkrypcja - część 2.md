**Data spotkania:** 14 października 2025, 10:14 - część 2

---

**Janusz Bossak:** Pokazuję wam tutaj jeszcze jedną rzecz, czyli te commity. I zastanawiam się, bo tu jesteśmy na wersji 25.0.3.31 i według mnie to powinno być zgodne z tym changelog, które zrobiłeś. Czyli jeżeli jest tutaj wersja 25.0.3.31.121, tutaj zrobił... I rozumiem, że ten commit, ten commit i ten commit poszedł do tej wersji. Potem zrobiliśmy wersję kolejną i teraz ten, ten i ten idzie do tej wersji. Tak mi się wydaje, że to tak działa, chyba że w drugą stronę, że to jest ten commit... Z tego jest wersja robiona. Właśnie nigdy nie wiem, co jest pierwsze, ale skoro tutaj są 3 i nie ma jeszcze wersji, to nie ma... Chodzi mi o to, czy jesteśmy w stanie – nie, znaczy inaczej – to jest o tyle głupie, że tu nie ma eksportu. Nie, tu nie mogę wziąć sobie eksportu. I nie wiem dlaczego, ale z tego poziomu nie ma eksportu. Ale chodzi mi o to, czy to jest zgodne z tym changelog, jakbyśmy mogli chociaż tak losowo sprawdzić kilka przykładów? Jakbyś mógł tam otworzyć, dziś miałem sobie...

**Damian Kaminski:** No jasne, no to wybierz, to tam też. Co mam ci znaleźć?

**Janusz Bossak:** Na przykład jakieś dodatkowe logowanie OCR. Mateusz zrobił.

**Damian Kaminski:** Sekundkę.

**Janusz Bossak:** I właśnie, że tutaj czasami są pisane te PBI, tak? Tutaj hash 22164 i hash 22166. Ale tutaj na przykład Mateusz nie podał, czyli coś zrobił, ale nie podał, tak jak tutaj. Poprawka do job'a OCR parse JSON tego...

**Damian Kaminski:** No to tego nie ma, jak nie ma. Ja pobieram tylko z tych... Chyba.

**Janusz Bossak:** Chociaż nie, tu jest jakieś numery – hash 22270, tak.

**Damian Kaminski:** Poczekajcie, po pierwsze to przerzucę na nowy wygląd, bo nie wiem z jakiegoś powodu zbudowałem to po staremu. Pisz. Dobra, i teraz filtrach. Dobrze, czego mam szukać? Tak, powiedzmy.

**Janusz Bossak:** Na przykład, dostosowanie wyświetlanego tooltip, poprawienie czyszczących się filtrów przy odświeżaniu. Coś tam, koniec wersji poprawki. Tak jest, pomidor, nie? On dotyczy numerka 22164 na przykład.

**Damian Kaminski:** Czyli tak, mogę, że "zawiera"? I teraz jeszcze tu kiepsko wyświetlanego...

**Janusz Bossak:** Powiecie, nazwa zgłoszenia może być inna niż commitu. W commicie on sobie wpisuje, jak mu się żywnie podoba, nie? Bądź gotów wpisać Kubuś Puchatek, nie?

**Łukasz Bott:** Jeżeli... Nie powiesz co, bo jak robią commit, mogą oznaczyć – przynajmniej tak jest przez wersję przeglądarkową, jak się wyprostował, robi – w tym miejscu to oznacza, do którego to jest zgłoszenie czy tam zgłoszeń. Więc tutaj jedynym kluczem byłby, jeżeli jest numerek, to OK. I 22164, ja spoglądam na bok – jest taki bug, Films naprawił tytuł. Gdy mam wybrany filtr użytkownika i odświeżę raport, dasz bardziej, filtr się resetuje. To będę mój... Moje... A nie, tu ma się zgłosiła, ale OK, dobra, to to samo obserwowałam, tak.

**Janusz Bossak:** Teraz – znaczy ten cały nasz workflow do generowania tych changelog jest super, tylko bym chciał, żeby ten changelog, powiem, miał sens i żeby mówił... Jestem na przykład ciekawy, co jest w ramach tego 22164 tak na tym changelog, tym co wygenerowało AI.

**Damian Kaminski:** Po naszej stronie... To znaczy, tak – tu jest w ogóle pytanie, co to jest za tytuł: "dostosowanie wyświetlanego tooltip".

**Janusz Bossak:** To jest tytuł commitu, jest tytuł commitu.

**Damian Kaminski:** No właśnie, a to to jest jeszcze jakieś... No właśnie.

**Janusz Bossak:** Pasto 3, 22164, 22166 zakomunikował za jednym jakby zamachem, nie?

**Łukasz Bott:** Tak, i tak. I przecinkami jest rozdzielone: co 22164 – czyli środkowe, to jest poprawienie czyszczących się filtrów przy otwieraniu – i to jest faktycznie tego problem dotyczy.

**Janusz Bossak:** Teraz mi chodzi o to, czy w tym changelog, który wygenerował AI...

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Pod numerem właśnie nie wiem – 120 – bo nie wiem, do którego to jest przypisane, czy do tego...

**Damian Kaminski:** 120.

**Łukasz Bott:** Nie, do wyższego, bo popatrz, popatrz na daty.

**Damian Kaminski:** Jest.

**Janusz Bossak:** Dobrze. I czy są te wszystkie zmiany: 22103, 22164, 22166 pojawiały?

**Damian Kaminski:** A dobra, to sekundkę, to...

**Łukasz Bott:** Nie musisz. Wydawać, spojrzeć na ten oryginalny, tak?

**Damian Kaminski:** To ja wyświetlę wam. Czyli tak, ja na razie wyszukałem po tym twoim numerku 2160. Przepraszam, 22160. Teraz zmienię co innego.

**Janusz Bossak:** I Wiki. Wiki, wielkimi, pokaż Wiki.

**Damian Kaminski:** A na Wiki. Ale poczekaj, to było... Ja jeszcze tego... To było wersji marcowej.

**Janusz Bossak:** To jest wersja marcowa, tak? 25.0.3.31. A takim branchie tutaj jestem, nie?

**Łukasz Bott:** Dwudziestka, tak.

**Damian Kaminski:** Poprawiono wyświetlanie tooltip w raporcie typu Kanban, naprawiono problem z resetowaniem filtrów po odświeżeniu raportów Dashboard.

**Łukasz Bott:** OK, tak. I to się zgadza. To jest też – Damian – się pokrywa z tym, co ty mi wysłałeś, nie?

**Janusz Bossak:** A jeszcze jest 22166.

**Damian Kaminski:** Ale poczekaj, bo ja mogłem coś usunąć. To ja się przyznaję, że ja to oczyściłem, żeby nie... Wolałem za mało i żeby... I wysłałem oryginał – to co mi wypluł – Łukaszowi. Jeśli chcę to poprawić, niż za dużo i potem się z czegoś tłumaczyć.

**Łukasz Bott:** Tak, tak. Ale wiesz co, ale Damian, ale akurat tutaj w 25.0.3.31.120 są tylko te to, co tym oryginalnie źródłowy, tak? Bo ty mi wysłałaś coś szczerze mnie...

**Damian Kaminski:** Tak, tak. Sekundkę, zaraz znajdę.

**Łukasz Bott:** A to co umieściłeś na Wiki, a to co umieściłeś – chyba na Wiki – to już jest przez ciebie filtrowane?

**Damian Kaminski:** Tak.

**Łukasz Bott:** No tak.

**Damian Kaminski:** Tak, tak, tak. No nie chciałem publikować czegoś, czego nie byłem pewny.

**Łukasz Bott:** No, ale dlatego wydania – to się te 2 numery zgadzają, tak – czy nie mamy tego trzeciego? A ten trzeci to było...

**Janusz Bossak:** Ale poczekajcie, jeszcze mam w tym w tej wersji – jeżeli to dotyczy tej wersji – dość ważny błąd i poprawkę: wykrywanie duplikatów pól przy imporcie XML. Marek.

**Łukasz Bott:** Dobra, a jaki to jest aldik? A jaki to jest aldik?

**Janusz Bossak:** Masz 195, 22195.

**Łukasz Bott:** 2...

**Damian Kaminski:** Dajcie, tu mam oryginał już. Najpierw spójrzmy na oryginał.

**Łukasz Bott:** 22195.

**Damian Kaminski:** Nie, tutaj mi tylko tyle wypluł, tak. Czyli 120 zawiera tylko to. Dobrze, to teraz zerknijmy na źródło.

**Janusz Bossak:** Wejście.

**Damian Kaminski:** Weźmiemy sobie tak... Wersja...

**Janusz Bossak:** Chodzi mi o to, wiecie, żeby doprowadzić do tego, żeby to dawało sensowny wynik, żeby nie było tak, że opuściło ileś rzeczy albo...

**Damian Kaminski:** Numer. Jasne, tutaj też takie ryzyko jest. Już tego tak dogłębnie nie sprawdzałem, po prostu chciałem coś wydać, żeby klient się – z przeproszeniem – odczepił.

**Łukasz Bott:** Dobra.

**Janusz Bossak:** Nie.

**Łukasz Bott:** Daniel przeprasza.

**Janusz Bossak:** Ja jestem w...

**Łukasz Bott:** Słuchajcie, odnośnie 22195, czyli przyjemności procesu z XML mogą powstać pole zduplikowane przypisaniem do column. Dlaczego tego Damian prawdopodobnie nie ma? Ponieważ Damian korzysta – nie masz, bo korzysta...

**Damian Kaminski:** Nie ma.

**Łukasz Bott:** Bo budujesz sobie ten proces, gdzieś tam podejrzałem – pod spodem budujesz tą tabelę na podstawie release version, tak? A to zgłoszenie to jest hotfix. Wisi na in progress u Piotrka Buczkowskiego i w ogóle nie jest do niczego zmergowany. Commity są factycznie...

**Damian Kaminski:** Tak. No.

**Janusz Bossak:** Jest zmergowany, bo...

**Łukasz Bott:** Commity są.

**Damian Kaminski:** Ale ja tego, w sensie my tego nie wiemy, że jest. Właśnie muszą aktualizować. Jeśli by to teraz zaktualizował na Done i byłaby wersja, to to się tu pojawi.

**Łukasz Bott:** Tak, ale...

**Damian Kaminski:** I wtedy można uzupełnić. Dlatego...

**Łukasz Bott:** Nie pojawi się w momencie, gdy jeszcze będzie oznaczone w zgłoszeniu release version. A tutaj nic nie jest oznaczone.

**Damian Kaminski:** Tak. I będzie Done, bo ja tutaj dałem filtr – tylko to mnie interesuje. No, po co mamy zaśmiecać czymś, co nie jest skończone?

**Łukasz Bott:** Tak, tak. Panie...

**Damian Kaminski:** To jest changelog, tak?

**Łukasz Bott:** Ale commit, ale faktycznie commity Piotrek do tego robił i commit być może w tym czasie gdzieś tam weszły, tak.

**Janusz Bossak:** Dobrze. Jest.


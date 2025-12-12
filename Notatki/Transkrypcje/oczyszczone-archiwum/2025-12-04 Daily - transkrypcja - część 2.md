**Data spotkania:** 4 grudnia 2025, 08:20 – część 2

---

**Damian Kamiński:** Ten Zabbix to jest chyba taka szyna, automatyzacja pewnych zdarzeń – jak Zapier?

**Łukasz Bott:** Wiesz co, nie. Bardziej to jest właśnie używane przez administratorów sieciowych do monitorowania systemów. I może monitorować różne – w tym sensie mają różne paginy, wtyczki do różnych już tam gotowych. Już może różne systemy gotowe monitorować, jak wspomniałem.

**Janusz Bossak:** Pogadamy później, dobra.

**Łukasz Bott:** No.

**Janusz Bossak:** Kamil.

**Kamil Dubaniowski:** Tak jak właśnie teraz robię przegląd tego raportu typu tabela – i to bym chciał dzisiaj, Przemek, z tobą trochę się zaopiekować. Cały czas spadają jakieś nowe zgłoszenia z LPP, więc ja po prostu chciałbym dzisiaj usiąść i testować na bieżąco zgłaszać, żeby klient testował tylko my. I to co jest już zgłoszone – Damian, tam trochę od ciebie odpinam, zgodnie z celem ze sprintu, czyli na razie skupiam się na raporcie typu tabela. Ten temat dzisiaj też wrzucam na blok. 

Kim jest? To tyle, reszta to są te projektowe spotkania. Rada jeszcze jest i LPP – mam wrzucony status. Wczoraj była też prezentacja dla Axel, tam przygotowałem mimo wszystko demówkę dla nich. Ten totalizator też na koniec dnia jeszcze sprzedażowo – odpowiadałem na pytanie.

**Damian Kamiński:** Jeśli chodzi o mnie, na początku ten temat za deco – znamy już konsekwencje. Natomiast tak, jeśli chodzi o działania Mariusza, to jak powiedział, na razie testujemy. Podzieliliśmy to na pół, czyli poprawne wyświetlanie pola typu checkbox. A dalej dorobimy pewnie możliwość wyłączenia wiersza nagłówkowego już w trybie PBI. 

Ja dalej wyjaśnienie, w zasadzie równolegle, problemów KSeF Connectorów zarówno w WIM, jak i w Gawarze. Natomiast udało się w Gawarze – dużo dodatkowych prac i spotkań takich wdrożeniowych, udrożnienia ruchu, konsultacji właśnie z działem wdrożeń. Natomiast ostatecznie udało się już ten Connector połączyć skutecznie z AMODIT w obu tych instancjach z tymi nowymi rozwiązaniami przygotowanymi przez Adriana. Więc tutaj już mamy na koniec dnia stabilne połączenia. 

Poza tym spotkanie dotyczące historii biznesowej w kontekście wyceny dla CRM – przygotowania na razie mockupu dla Rossmana. Poza tym wsparcie dla Orlenu, bo tam się pojawiły jakieś problemy ze statusami w integracji. 

Repozytorium plików – mieliśmy spotkanie z Adrianem dotyczące uprawnień. Omówiliśmy to sobie i zakładam, że Adrian dzisiaj będzie już nad tym pracował w ramach MVP. Natomiast samo przygotowanie działania algorytmów jest przygotowane tak właśnie, żeby można było to rozwijać i żeby to nie konfliktowało w kontekście tego, co ty wdrażamy w ramach MVP na ten moment. 

Jeśli chodzi o dzisiaj, to standardowe nasze spotkania – czyli Rada i spotkanie projektowe. Poza tym będąc do tego, co powiedziała Ania – czyli foldery. Będą dalsze ustalenia, co robimy dalej z repozytorium. I praca w WIM.

**Janusz Bossak:** Dobrze. Działamy. W takim razie sporo jeszcze tematów widzę. To repozytorium chyba jest szansa, że się nam uda – jeszcze mamy chwilę. Pytanie, jak tam z tym jotterPL czyszczenie to już jest na tyle, że można to sobie potestować gdzieś, w sensie?

**Marek Dziakowski:** Dzisiaj będę testował chwilę i wygram tą testy integration. Jak zrobię, to dam ci znać.

**Janusz Bossak:** Dobra.

**Kamil Dubaniowski:** Ja dostałem Marek tam – niestety w Wordzie tylko – i to jest nadal nie tak jak powinno być. Ale możecie to jakoś łatwiej robić ten schemat z LPP? Jutro była w sensie nazwy folderów i tam numerację ich. Wcześniej było w PDF-ie chyba, jak kojarzę – to przyznają, że będzie łatwiej kopiować.

**Janusz Bossak:** Można tam za pomocą AI przetworzyć to – tam dość sprawnie AI przetwarza takie rzeczy.

**Marek Dziakowski:** OK.

**Janusz Bossak:** Wrzucić do jakiegoś tam promptu i przetworzy to. Dobra. Dzięki bardzo, miłego dnia. Wszystkim dzisiaj sporo spotkań różnych tutaj – przynajmniej ja mam cały dzień. Działamy tutaj. Wrzuciłem – ktoś byłby ciekawy, czym się różni Zabbix od tych systemów klasy SIEM – to na tym czacie teraz zdaje i wrzuciłem, żebyśmy wiedzieli, o co chodzi. Znaczy, nie bardzo rozumiem, co my mamy wspólnego w takim razie z Zabbixem – bardziej Zabbix to Łukasza podskrobie. Też po prostu monitoring infrastruktury.

**Łukasz Bott:** Tak, no i w LPP mają monitoring infrastruktury.

**Janusz Bossak:** No, ale co ma z tym?

**Łukasz Bott:** To znaczy my – tylko tyle, że my w AMODIT coś logujemy, zalogujemy w event logu czy w tym, w tabeli system log i nie będziemy się jakoś tam bezpośrednio integrować z Zabbix, wywoływać jego API czy coś. Tylko udało się udało się wynegocjować, że oni – my im tylko przekażemy zapytanie SQL-owe do tabeli system log, na co mają czytać – jeszcze do case activity i user activity – i na co mają zwracać uwagę. I tyle. Niech sobie monitoruje.

**Janusz Bossak:** Ale to wtedy to jest wtedy nie Zabbix, tylko ten, te systemy klasy SIEM, chyba że ten.

**Łukasz Bott:** Proszę troszeczkę inaczej. Tak się z nimi umówiłem – do Zabbix, PSA, a do SIEM-u mamy na razie przedstawić, co jak są u nas te zdarzenia.

**Janusz Bossak:** Nie rozumiem tego.

**Łukasz Bott:** To, co będziemy musieli dorobić – i tu też tam gdzieś Kamil odpowiedziałem w komentarzu – to prawdopodobnie tutaj raczej na zasadzie takiej, że jeżeli my logujemy coś, na przykład w event log, jak powiedziałem – na przykład nie wiem, że błędne logowanie użytkownika – to to zdarzenie wysyłamy do SIEM-u. Ale to już SIEM na podstawie nie wiem historii tego typu zdarzeń czy coś – on będzie decydował, ten system będzie, SIEM decydował o tym, czy to jest bezpieczne, czy niebezpieczne, czy to jest podejrzane zachowanie.

**Janusz Bossak:** Dokładnie. Dobra, to już wiemy wszystko. W takim razie dzięki bardzo. Zostajemy chwilę jeszcze tutaj – Kamil, Łukasz, Damian, Michał. Działamy. Na razie miłego dnia.

**Marek Dziakowski:** Miłego dnia, cześć.

**Barbara Michalek:** Dzięki, cześć.

**Filip Liwiński:** Dzięki.

**Anna Skupinska:** No cześć.

**Janusz Bossak:** Oddaję panu głos, co tam jakieś mamy nowe tematy? Przegląd szybki.

**Łukasz Bott:** Tak. Wczoraj przy okazji tego EAP – tam były jedne problemy z tą biblioteką ITEX gdzieś, ale to na konkretnym przykładzie plików będziemy wiedzieli, w czym jest problem. Marek przeanalizuje. Natomiast niezależnie od tego pojawił się błąd. Ja to wrzuciłem na zgłoszenie. Błąd, który się pojawia co jakiś czas w AMODIT i dotyczy jakichś tych constraintów na tabelach – różnych jakichś tych powiązań – foreign keys, klucze i nie wiem jak to jest rozwiązywane czy coś, ale z punktu widzenia użytkownika nie wydaje się, żeby coś tam nie działało poprawnie. Ale mimo wszystko sypie jakimś takim dziwnym logiem.

**Janusz Bossak:** Jak ktoś na to spojrzy, to może jest jakiś problem w bazie danych – że jakieś klucze nie są założone, czy coś.

**Łukasz Bott:** Tak wygląda, czy to może być bardzo dawno?

**Janusz Bossak:** Dobrze. Ja mam pytanie odnośnie wyceny, która wisi na mnie. Pamiętasz to – Łukasz, opiekowałeś tam z Anetą, ponieważ web model web proxy dla funkcji GetDataFromGUS i GetDataFromGUSex – którą miałeś chyba im wyjaśnić, że to jest robione przez ten serwis samochodowy.com, tak mi się wydaje. Bo nie wiem, co z tym zleceniem zrobić – jest wycena i co?

**Łukasz Bott:** Tak, Janusz. Nie, no i właśnie.

**Kamil Dubaniowski:** To jest robota.

**Łukasz Bott:** Pamiętam, jest robota. Właśnie, o to chodzi, że jest robota. I teraz tak pytanie – myśmy chyba Adriana prosili o to, żeby on.

**Janusz Bossak:** To nikt nie jest przypisany do wyceny. Dobra, to daj.

**Łukasz Bott:** Nie, nie jest do wyceny – na razie nie wiem, do wyceny na razie nie, tylko.

**Kamil Dubaniowski:** Mi to nad raną konsultował teatr.

**Łukasz Bott:** Dobra, Janusz, o co chodzi? To jest temat – jest w banku. Bank ma jakieś tam toxin proxy gateway, wychodzący do, który steruje ruchem do internetu tym, co mamy może być wymieniany. I teraz okazało się, że wszystkie systemy, które u nich są, muszą przez tego gateway iść. I wyszło, że nie wszystkie nasze funkcje przechodzą przez proxy. Ten mechanizm proxy mamy już zrobiony w AMODIT i on jest używany przez funkcję CallRest między innymi. Ale się okazuje, że też tego typu funkcji – to, co chyba Adriana, Kamil, poprosiliśmy – żeby znalazł wszystkie te miejsca takie, gdzie tego typu właśnie to web proxy trzeba by było użyć.

**Janusz Bossak:** Czy Adrian zna temat, wie o co chodzi? Jak mu przekażę do wyceny, będzie wiedział, o co mu? Się tylko pytam.

**Damian Kamiński:** Trzeba to dopisać, według mnie nawet jest.

**Adrian Kotowski:** Tak, kojarzę, by się włączyłem – niech mnie trochę się spóźniłem, budzi po prostu mi nie działał dzisiaj. Znaczy, to by ten temat proxych przyczajać tam od różnych integracji i tych miejsc jest w sumie więcej, czy.

**Łukasz Bott:** Tak, no no no.

**Adrian Kotowski:** To odnośnie GUS – jeden z głównych ktoś jest znany, to mieście, ale trzeba zrobić przegląd wszystkich miejsc. I też ewentualnie jeszcze innych integracji, bo na przykład jeździ typu Deutsche Bank – właśnie mają ten problem, że jak się choć, jak się nowa integracja, to może nie działać.

**Janusz Bossak:** Dobrze, słuchajcie. Znowuż działajmy dwuetapowo. Jakiś tam Pekao Towarzystwo Funduszy Inwestycyjnych zleca nam – zróbmy to tak, te dwie funkcje są wiadome i żeby to działało, ile to będzie kosztować. Przy okazji, nie mówiąc klientowi, robimy sobie przegląd i możemy ten dzień czy dwa tutaj dopisać. Ale te pozostałe rzeczy zrobimy w innym cyklu, w innym.

**Damian Kamiński:** Znaczy, ja się zgadzam z Januszem. Natomiast według mnie efekt wdrożenia tego powinien być taki, że tam, gdzie mamy ustawienia systemowe i zakładkę proxy, to powinny pojawić się po prostu checkboxy dla każdego dzisiejszego użycia proxy – czyli trzeba sprawdzić, gdzie my dzisiaj używamy i pozwolić na zaznaczanie docelowe, czy chcemy używać w ramach tego, co gdzie używamy dalej. Czyli z poziomu konfiguracji można wybrać, czy to ma iść przez serwer proxy czy bezpośrednio. Poza tym, że to, co już mamy, będzie można definiować, to dokładamy te dwie dodatkowe funkcje, czyli połączenie z GUS-em jako w zasadzie jedno tutaj, bo to, czy to będzie ex czy nie ex, to nie ma znaczenia – po prostu funkcja łączenia z GUS-em.

**Łukasz Bott:** Tak. GUS Teryt też jeszcze nie.

**Damian Kamiński:** No wiesz, tu jest wymagane to jedno, więc to już pytanie, czy gus teryt to też – wydaje mi się, że to idzie przez nasze serwisy, więc to można do – znaczy, to idzie przez services, według z tego co wiem.

**Janusz Bossak:** Nie, jak GUS Teryt to jest lokalny.

**Łukasz Bott:** Tak, przyznasz.

**Janusz Bossak:** GUS Teryt, znaczy jeżeli klient ma on-premise, to GUS Teryt jest lokalnie, bo on wtedy jest zasilany tam raz na jakiś czas, na pół roku jakoś tak to było zrobione. Są trwałe jakby dwie wersje, wersje taka on.

**Damian Kamiński:** Nie, nie, nie, nie na pół roku, jak nie nie, to jest lokalnie w tym kontekście, że jest pamięć podręczna – jest odpytanie i zapisanie odpowiedzi. Jeśli ktoś o to samo zapyta, to najpierw sprawdzi, czy lokalnie już jest odpowiedź.

**Janusz Bossak:** Według mnie.

**Łukasz Bott:** Dobra, ale to był Piotrek – pewnie by musiał powiedzieć, którego nie mamy.

**Damian Kamiński:** Ale to jak to widzisz, raz na pół roku, że przeszukujemy cały GUS Teryt? Na pół roku na pewno nie.

**Janusz Bossak:** Aktualizujemy danymi z GUS Teryt.

**Damian Kamiński:** Jeśli jest lokalnie.

**Janusz Bossak:** Dobra. Tak. To jest inna procedura aktualizacji, tak mi się wydaje. Przynajmniej ja, przynajmniej tak to rozumiem. Dobra, ale nieważne. Adrian, daję tobie to do wyceny.

**Damian Kamiński:** Dobra, nie będę się upierał.

**Łukasz Bott:** Adrian zniknął, ale dobra, to jemu to dajemy like.

**Janusz Bossak:** Będzie wiedział, o co chodzi. I trzeba też uczulić, bo tutaj dzisiaj patrzyłem na wycenę – nawet wycenę, którą robił Łukasz Brocki, to jest.

**Łukasz Bott:** Autoryzacje certyfikatu.

**Janusz Bossak:** Tak. To ja tutaj dopisałem. To była cała jego odpowiedź. Tutaj należy przygotować integrację, należy jako funkcjonalność. Ale znaczy, dobrze by było, gdyby to było zapisany. Dobrze, znaczy żeby to mówiło to, co tutaj wielokrotnie mówią – żeby to była taka analiza techniczna, architektoniczna, jak to zostanie zrobione. To jest opis dla nas. To jest ta klienta tutaj, ale Jenny? A kto jest dla klienta? Chociaż ona też jest taka mało jakby czytelna dla klienta. I musimy uczulać też naszych tutaj kolegów i koleżanki, bo Ania też tu może robić, którzy wyceniają, żeby tu pisali naprawdę techniczną taką architektoniczną informację, jak to będzie zrobione – czyli co zostanie wykorzystane, że sprzedawać – tak jak ja to dopisałem, że rozwijamy Custom SMS Gateway. Bo bez tego słowa nie ma o tym. Wyglądało jako nowa opcja SMS poprzez tę bramkę. To już sobie wyobraziłem, że.

**Łukasz Bott:** Nowa integracja.

**Janusz Bossak:** Że Łukasz zrobi jakąś osobną w ogóle integrację, tylko z tym, z tą bramką, którą tutaj używa klient. Więc bardzo proszę, żebyście też uczulali kolegów. Ja też to będę tu sprawdzał, żeby tu naprawdę wpisywali koncepcję techniczną tego rozwiązania. Nie zawsze to musi być jakiś rozbudowany opis, bo często to są zwykłe jakieś tam kwestie, ale jak tutaj warto po prostu napisać nawet to, co się niby ma w głowie, że to przecież to oczywiste, że tak będzie, to niech to oczywistość to będzie napisane, żeby nie było potem wątpliwości, że ktoś to zrobił jakoś inaczej albo że nie pomyślał o czymś. Dobra. To tam na tym wycenę czekamy od Adriana wtedy. 

Co jeszcze mamy? Trochę do tych wycen cofnąłem się, bo wczoraj nie robiliśmy tego przeglądu. Tego teraz to zrobiłem. Czy mamy jakieś bieżące wpływające zadania na backlogu, które trzeba mówić?



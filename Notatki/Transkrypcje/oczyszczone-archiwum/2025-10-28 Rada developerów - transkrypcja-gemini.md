**Data spotkania:** 28 października 2025

---

**Damian Kaminski:** Cześć. Aniu, czy z tym data source potrzebujemy coś omawiać na Radzie, czy na razie to odpuszczamy?

**Anna Skupinska:** Jest to pewne, chyba że chciałabyś coś zmienić.

**Damian Kaminski:** To jest oznaczone jako "na radę", ale nie jest na ten moment krytyczne. Zostawiam to.

**Piotr Buczkowski:** Tam coś było z tym logowaniem w MS SQL-u, ale okazało się, że w najnowszych wersjach już to jest.

**Damian Kaminski:** Ale to jest `dashboard_datasource_synchronization`, a ty mówisz o raportach.

**Piotr Buczkowski:** A, o raportach, dobrze.

**Damian Kaminski:** Aniu, udało ci się zająć tamtym tematem z raportami?

**Anna Skupinska:** Jeszcze tego nie sprawdzałam, ale myślę, że będę musiała się tym zająć.

**Damian Kaminski:** To ma priorytet nad tym, bo tamtego zadania nie widzę na twojej tablicy. Zostało na poprzednim sprincie. To jest priorytet 1, musimy to zrobić, bo uprości to rozwiązywanie większości błędów z raportami.

**Janusz Bossak:** Przeglądam teraz te raporty i patrzę, czego nam funkcjonalnie brakuje. Mam parę kluczowych rzeczy do przedyskutowania na następnej Radzie.

**Damian Kaminski:** Dobrze, to teraz informacja o synchronizacji słowników. Tu w zasadzie chodzi tylko o ten błąd. Jaka jest sugestia co do naprawy?

**Piotr Buczkowski:** Po pierwsze, sprawdzić, o co chodzi. Po drugie, zmienić miejsce, z którego jest pobierana data ostatniej synchronizacji, bo się zmieniło.

**Kamil Dubaniowski:** Z tego, co kojarzę, to było osobne zgłoszenie od Kacpra Tuczyńskiego, że w rejestrach nie widać prawdziwej daty synchronizacji.

**Piotr Buczkowski:** To to samo. Z tabeli z historią synchronizacji, która odnosi się do słowników i rejestrów, należy pobierać datę ostatniej synchronizacji. Trzeba przygotować do tego endpointy. Inaczej mówiąc, jest endpoint do pobierania właściwości słownika czy rejestru i w nim trzeba zmienić sposób pobierania tej daty.

**Damian Kaminski:** Zastanawiam się, na ile to jest kluczowe w kontekście starego formularza. Czy warto to poprawiać, skoro wszystko działa? Blokujących problemów nie ma, poza tym, że wyświetla się wykrzyknik.

**Piotr Buczkowski:** To jest kosmetyka.

**Damian Kaminski:** Odpinam to. Przejdźmy przez tematy, które dotyczą klientów.

**Kamil Dubaniowski:** Mam zgłoszenie 16558. Konsultanci je podbili. Jest oznaczone na radę i chciałbym je omówić.

**Damian Kaminski:** Proszę.

**Kamil Dubaniowski:** To temat, który wraca przy każdej aktualizacji, bo muszą coś zmieniać w konfiguracji u klienta. Chodzi o raport typu Gantt. Wcześniej działało tak, że po wejściu na Gantta ładowało się wszystkie kategorie. Na przykład klient miał kategorie "pokoje" i na wykresie widział zarówno te zajęte w danym terminie, jak i te wolne. Ładowaliśmy wszystkie kategorie, jakie znaleźliśmy przez `DISTINCT` ze wszystkich spraw w AMODIT. Jak klient miał 10 000 pokoi, to ładowaliśmy mu 10 000. Zmiana polega na tym, że teraz ładujemy tylko te, gdzie w danym okresie są jakieś sprawy. Dla klienta to nie jest OK, bo nie widzi wolnych pokoi i nie może planować.

**Janusz Bossak:** To dokładnie ten sam problem, co z brakującymi datami.

**Damian Kaminski:** Tak. Może powinien być jakiś parametr. To niby to samo, ale trochę co innego. Tam są daty, których w ogóle nie ma, a tu byty (sprawy) istnieją, tylko nie mają danych w zadanym okresie.

**Janusz Bossak:** Ale to jest to samo, bo danych dostarczonych do raportu dla danego projektu nie ma, więc nie jest on przesyłany.

**Kamil Dubaniowski:** To musi być parametr. Na radzie była dyskusja z Piotrem, żeby to zrobić dobrze, żeby nie było niewydajne. Pytanie, czy robimy to na starym i nowym module, czy tylko na nowym?

**Damian Kaminski:** Tylko na nowym. Inaczej nie wymusimy przesiadki.

**Janusz Bossak:** Zgadza się. Tak samo Comarch mówił na konferencji – wszystkie nowe rzeczy są tylko w nowej, subskrypcyjnej wersji. Mają plan, żeby do 2029 wszyscy przeszli na subskrypcję.

**Damian Kaminski:** Dobra. Jak to zrobić wydajnie? Pewnie musiałby istnieć jakiś słownik.

**Piotr Buczkowski:** Daty są proste do wyliczenia. A tu musiałoby być pole słownikowe, lista pozycji ze słownika, lista spraw z rejestru, lista użytkowników, coś ze źródła zewnętrznego. Coś, co ma zdefiniowaną, skończoną listę.

**Janusz Bossak:** Mam wrażenie, że już o tym rozmawialiśmy i że to było rozwiązane.

**Kamil Dubaniowski:** Też to wczoraj testowałem. Mateusz w tym grzebał i zrobiłem sobie testy, pokazuje mi wszystkie sprawy.

**Damian Kaminski:** Dobrze, sprawdźmy to. Tworzę raport typu "Planowanie zasobów", w kolumnach "Wnioskodawca" i... są wszyscy. To działa.

**Kamil Dubaniowski:** Zapisz i zakończ edycję. Zależność była taka, że w edycji widać wszystkich, a po zapisie tylko tych, dla których masz sprawy.

**Damian Kaminski:** Ciężko powiedzieć, o co chodzi. Jest inaczej. Tu jest Krzysztof Górski i Emil Patyna, a tam był Krzysztof Górski i Monika Pruszyńska. Mój gdzieś podskoczył wyżej. Może mam jakąś sprawę bez daty końca i dlatego nie umie tego wyrysować.

**Janusz Bossak:** Trzeba to rozkminić, ale to nie jest poziom na Radę. My tu rozkminiamy, a nie decydujemy. Rada ma decydować, co robić.

**Damian Kaminski:** Zalecenie doraźne powinno być takie, żeby zrobili to na nowych raportach. Niezależnie od tego trzeba zaplanować, jak to powinno wyglądać docelowo. Piotr zasugerował, ale to trzeba rozpisać.

**Kamil Dubaniowski:** Rozumiem, że robimy to tylko w nowym module, tylko dla określonych typów pól, które są limitowane (słowniki, użytkownicy), a nie dla pól tekstowych, które pochodzą z `CaseDefinition`.

**Janusz Bossak:** A co, jeśli słownik ma 100 000 pozycji? Albo rejestr? Nie podoba mi się ten pomysł. Trzeba to głęboko przemyśleć.

**Damian Kaminski:** To temat wielowątkowy i nie wpisuje się w bieżące potrzeby.

**Janusz Bossak:** Odwieszamy na kołek. Jeśli to nie jest błąd w rozumieniu "działało inaczej, a teraz działa inaczej", to mamy inne priorytety.

**Damian Kaminski:** Dam im sugestię, żeby zrobili to po nowemu, co częściowo wyeliminuje problem.

**Kamil Dubaniowski:** Oni tego nie zrobią, nadal będą nadpisywać te filtry w plikach JS.

**Piotr Buczkowski:** Chodziło o usunięcie domyślnego filtra zakresu dat. On pobierał wszystkie sprawy, nie tylko z widocznego okresu. To powodowało, że np. wykres urlopów w AmRest nie działał, bo był za duży (setki tysięcy spraw z 10 lat).

**Damian Kaminski:** Klient robi coś, czego efektem jest działanie nowych raportów, a my się zastanawiamy, czy to dobrze. Odpowiedziałbym: proszę korzystać z nowych raportów, nie trzeba robić tej poprawki, macie tak, jak chcieliście.

**Piotr Buczkowski:** Pytanie, czy zaraz nie "poprawimy" tego w nowych raportach, bo okaże się, że w rzeczywistych przykładach to jest nieużywalne.

**Damian Kaminski:** To prawda. W takim razie powinniśmy to zaopiekować kompleksowo. Jak chcemy ograniczać, to trzeba budować tę listę w sposób optymalny.

**Janusz Bossak:** Proszę Marka o dołączenie, ma pilny temat z Trust Center do omówienia.

**Marek Dziakowski:** Cześć. Ktoś pamięta, dlaczego było założenie, żeby niektóre joby w Trust Center działały tylko w nocy? Chodzi o `BackgroundWorkers`. Wyszedł problem, że brakuje nam miejsca w hot storage, bo jest duży przemiał dokumentów i job nie wyrabia.

**Piotr Buczkowski:** Jaki job? Transfer?

**Damian Kaminski:** Chodzi o usuwanie plików z hot storage, nie o swapowanie na bloba.

**Piotr Buczkowski:** Było założenie, że raz dziennie, po co więcej. Być może przerabia za małą paczkę na raz.

**Marek Dziakowski:** On wykonuje się 10 razy na godzinę w nocy, ale nie wyrabia. Wisi bardzo dużo dokumentów. Robi po 25 na raz.

**Damian Kaminski:** No właśnie. Jak robi 25 w 10 sekund, a jest wywoływany kilkadziesiąt razy w ciągu nocy, to może trzeba robić 150 za jednym wywołaniem.

**Piotr Buczkowski:** Dziwię się. W AMODIT jest podobny job, który robi w paczkach, aż zrobi wszystko. A ten w Trust Center najwyraźniej został źle przemyślany.

**Janusz Bossak:** Tak, bo teraz Rossmann wrzuca nam po 10 000 dokumentów dziennie.

**Damian Kaminski:** Trzeba zwiększyć ten wolumen. Jeśli job po prostu wykonuje pracę i nic nie obciąża, to zwiększenie z 25 na 200 powinno rozwiązać problem.

**Marek Dziakowski:** Zastanawiam się, czy w przyszłości nie lepiej byłoby te joby przerobić.

**Piotr Buczkowski:** Jeśli robisz joby w oddzielnym serwisie, to wszystkie takie joby trzeba tam przenieść. Nie wiem, dlaczego to zostało zrobione w procesie webowym, a nie jako oddzielna usługa od początku.

**Marek Dziakowski:** To teraz pytanie do Janusza, czy idziemy w to? To będzie trochę pracy.

**Piotr Buczkowski:** Musimy iść w to.

**Janusz Bossak:** Musimy, niestety.

**Damian Kaminski:** Dobrze, ale możemy to podzielić. Na ile to krytyczne?

**Marek Dziakowski:** Bardzo krytyczne.

**Piotr Buczkowski:** Bo Trust Center przestanie działać. Najpierw musimy przenieść dodawanie do blockchaina do osobnej usługi, a potem zacząć przenosić kolejne rzeczy.

**Damian Kaminski:** Czy możemy ustalić, że Marek pracuje tydzień nad Trust Center, a tydzień nad innymi priorytetowymi zadaniami? Robimy to 2 razy dłużej, ale akceptujemy to.

**Janusz Bossak:** To są zadania krytyczne. Zastanawiam się, czy nie dać Markowi jeszcze kogoś, żeby to przyspieszyć. Jak Rossmann czy Adecco wrzucą kolejne parę tysięcy dokumentów, to się zatka i będziemy "kwiczeć".

**Marek Dziakowski:** Zawsze jest opcja skalowania hot storage w górę, ale to wiąże się z kosztami.

**Piotr Buczkowski:** A w dół się chyba nie da.

**Janusz Bossak:** Uważam, że to co Marek robi z blockchainem to absolutny must-have. A tutaj, na razie bez przerabiania, po prostu zwiększmy limit z 25 na 500 czy więcej. Niech on posprząta, a w następnym cyklu zajmiemy się przeniesieniem tego joba.

**Marek Dziakowski:** Dobra, dorobię ustawienie i zwiększymy ilość dokumentów do przegrania.

**Janusz Bossak:** Dokumenty po podpisaniu i tak wiszą w hot storage przez jakiś czas, standardowo miesiąc.

**Piotr Buczkowski:** Tak, założenie jest takie, że na czas obsługi są w hot storage, żeby nie sięgać do cold storage (bloba), bo pobieranie stamtąd jest droższe, jeśli robi się to często.

**Damian Kaminski:** Warto by sprawdzić, czy te 30 dni jest zgodne z realiami. Może wystarczyłoby 14 dni.

**Piotr Buczkowski:** Warto to sprawdzić, ale zacznijmy od najważniejszego.

**Damian Kaminski:** Dobrze, Marku, w miarę możliwości opisuj to, co robisz. Załóż PBI.

**Janusz Bossak:** PBI to absolutny must-have. Powinien być zakaz robienia czegokolwiek bez PBI, i to nie PBI w postaci samego tytułu. Jak się wam nie chce pisać, użyjcie AI, napiszcie 2 zdania, a ono wam to rozbuduje. Będzie nam łatwiej testować, pisać dokumentację itd.

**Damian Kaminski:** Będziemy też lepiej robić, bo jak próbujemy coś opisać, to od razu weryfikujemy, czy wszystko przemyśleliśmy.

**Marek Dziakowski:** Dobra, założę feature "Przeniesienie zadań cyklicznych do usługi" i pod to będę podpinał kolejne PBI. Na razie blockchain jest priorytetem, a w kolejnych sprintach reszta.

**Janusz Bossak:** Muszę uciekać, dzięki.

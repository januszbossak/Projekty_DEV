**Data spotkania:** 20 października 2025, 07:03 - część 2

---

Żeby. Żeby nie popsuć danych na produkcji.

**Janusz Bossak:** Noszę, noszę – to się wpisuje w tą naszą inicjatywę.

**Piotr Buczkowski:** I stąd też moja tam uwaga, żeby to okienko było szersze, bo to trochę się robi.

**Janusz Bossak:** Szerszy, tak.

**Piotr Buczkowski:** Nie ma, nie ma sensu.

**Janusz Bossak:** To się wpisuje w tą inicjatywę, co mieliśmy 2 sprinty temu – importowanie procesu, tak, to jest dokładnie ten element.

**Piotr Buczkowski:** W ciągu tygodnia dwoje konsultantów u 2 klientów popsuło procesy na produkcji, więc postanowiłem to zrobić. Pomagały mi przywrócić.

**Janusz Bossak:** Super.

**Piotr Buczkowski:** Inną zmianą to było też prace nad finki-ID – tam pełną obsługę słowników? Zagnieżdżonych, nie zagnieżdżony – znaczy zagnieżdżony też – hierarchicznych i zagnieżdżonych dodałem. No to teraz moich pracy.

**Janusz Bossak:** To sugeruję okienko rozszerzyć i nawet może dać po 2 kolumny na to, co jest lokalnie i to, co jest importowane. Żeby to było widać, że jest nazwa, GUID, na przykład albo to.

**Piotr Buczkowski:** To są – to staram się wymyślić różne konflikty, tak, typu, że pola tej samej nazwie ma inne GUID i to, ale ten sam typ, czyli wiadomo, że trzeba. Ujednolicić i GUID i to było pole ma te same nazwy, ale przypisane do innego pola w bazie danych – tutaj też trzeba ostrożnie to. Jeszcze tego nie dorobiłem, ale to właśnie powinno blokować import. Aż do przywrócenia. Aż do przywrócenia spójności. No to tyle.

**Janusz Bossak:** No dobrze. Od pozostałych kolegów, koleżanek. Cześć Natalia, widzę, jesteś.

**Natalia Laskowska:** Sorry się tak nie, nie chce.

**Janusz Bossak:** Ale widzę, że jesteś. Mówiłaś, że nie będziesz.

**Natalia Laskowska:** Tak, tak, bo pan prezes jest na urlopie, więc mogłam wpaść do was.

**Janusz Bossak:** OK. Dobra, co tam dalej? Marek, proszę ciebie, nowego, ciekawego?

**Marek Dziakowski:** Takich widocznych zmian to dodałem obsługę wyświetlania pola typu Podpis w nowym module raportowym. W zasadzie wygląda tak samo jak stary, więc nie wiem, czy to jest co pokazywać. Poza tym na dużo bugów było, więc też tak nie bardzo mam co pokazać.

**Janusz Bossak:** Jest stroną w tym landing page'u po podpisaniu – to jest już jakoś wprowadzone? Jaka jest sytuacja tam?

**Marek Dziakowski:** Tak jest, jest już to dodane na TrustCenter produkcyjnym – tych wszystkich pozostałych.

**Janusz Bossak:** Znaczy, chodziło o to, żeby można było wybierać, która strona będzie tą stroną landing page'u, tak.

**Marek Dziakowski:** Wybierać – tego nie kojarzę. Było zmiana, żeby po prostu zmienić tą stronę, na którą użytkownik będzie przekierowany, a co dalej, to? Nie wiem.

**Janusz Bossak:** Dobra, to trzeba to jeszcze. Pogadać.

**Damian Kamiński:** Z Marka zamkniętych tematów chyba w tym sprincie, to tam już w zeszłym to pokazywaliśmy, więc może nie będę tego powtarzał, ale SimplySign podpisywanie na nowych raportach to już jest wydane, przy czym – znamy. Może tak, jesteśmy świadomi, że można jeszcze to usprawnić. Na razie jest to po prostu odwzorowane, czyli działa, natomiast jeszcze usprawnimy ten proces, żeby tam nie było 2 przycisków. Zaloguj i wywołaj do podpisu, tylko żeby to był taki jeden. Wizard. Powiedzmy.

**Janusz Bossak:** OK.

**Damian Kamiński:** Natomiast jest to pokryte. Tam była poprawka, jeszcze jakaś drobna na początku sprintu.

**Janusz Bossak:** Dobra, Adrian, ciebie.

**Adrian Kotowski:** Ja też zajmowałem się tam innymi bugami i ten temat problemów z e-doręczeniami dalej to kontynuuję. To są zgłoszone właśnie uwagi co do Centralnego Ośrodka Informatyki. No ale nic teraz pokazywać, bo też, jakby mam dość inne tematy. Właśnie ta aplikacja do dopisywania na macOS – tym się będę sobie bawił i tutaj. No to tyle, jeśli chodzi o mnie.

**Janusz Bossak:** Na temat. Już bliżej niż dalej, bo tak – różne fazy.

**Adrian Kotowski:** Teraz jak mówię, wstrzymałem pracy, bo tym API e-doręczeń i teraz chcę kupić, bo żeby tu sprawdzić pracę. Chcę sobie zakupić właśnie ten podpis SimplySign, bo to teraz aktualnie trwają testy tego tematycznego wykrywania podpisów właśnie na tym Szafir i Szafir – tym się akurat zajmuję i teraz chciałbym dodać właśnie tę obsługę tego trzeciego. To już mamy dane, ale teraz to jest – te drugie testuję, żeby testowe, jak tu podpisów. Będę dodanie obsługi tego podpisu się mieli – już myślę, że do końca tego miesiąca obsługę 3 podpisów, których głównych – Szafir, Szafir oraz SimplySign. I też w planach jest dodanie jeszcze innych podpisów, bo już tam był chyba jakiś nas. Podpisując bez – Poczta Polska by też go oddać, więc tutaj stabilne zmiany właśnie – to nie do końca tego – do końca miesiąca już pozyskam ten podpis. To jestem dopisywania z tym pisaniem, to postaram się już to dostarczyć.

**Kamil Dubaniowski:** To Janusz, nie wiem, ale trzeba pomyśleć, żebyśmy mieli po prostu zestaw wszystkich podpisów. A niestety Mac niezbędny, więc nie wiem czy to na jedną osobę, wtedy na Adriana – trochę bezcelowe. Bo jak ktoś inny by musiał serwis robić, to znowu nie mamy podpisów do testów, będą tylko u Adriana i jego będziemy tylko obciążać. Więc może jakieś się da uzyskać deweloperskie? Nie mam pojęcia.

**Adrian Kotowski:** No teraz i tak teraz tak dziwnie, że właśnie to jest test podpisu Szafir – testuje właśnie Kamil te testy, a ja już nie muszę prosić, więc jakby się piramid mam sam, więc – tak, żeby nie skakać po prostu przy ludziach – trzeba mieć właśnie taki zestaw tych podpisów.

**Janusz Bossak:** Myślimy. Patrycja, masz przecież jakiś podpis. Basia już podpis, Oktawia.

**Patrycja Walaszczyk:** I.

**Kamil Dubaniowski:** Tylko nie mają Maców.

**Patrycja Walaszczyk:** Ale nie mam Maców właśnie.

**Barbara Michałek:** A ja nie mam żadnego podpisu.

**Patrycja Walaszczyk:** Ja mam PZ podpis.

**Barbara Michałek:** I Oktawia ma jakieś?

**Janusz Bossak:** No dobra, to zastanowimy się, jak to rozwiązać. Nie mamy odpowiedzi tej chwili. Dobrze, co dalej, kto tu jest dalej? Ciekawe. Łukasz Brocki.

**Łukasz Brocki:** Ja tak naprawdę w tym sprincie to głównie jakieś poprawki – też był problem w e-nadawcy. Jeden problem został rozwiązany, ale jeszcze od Poczty Polskiej muszę tam dostać informacje, bo jest problem, który występuje kilka godzin w ciągu dnia i potem on znika. I ciężko w ogóle przez to w jakikolwiek sposób to zdiagnozować, także w poprzednim sprincie to głównie jakieś poprawki. Na pewno nic, co można pokazać.

**Janusz Bossak:** Dobrze, Mariusz.

**Mariusz Piotrzkowski:** Ja również miałem na ten sprint jakieś 15 chyba błędów przypisanych i tylko jeden PBI, które jeszcze muszę trochę dokończyć, bo coś tam zostało drobnego, tak, że też nie mam co pokazać.

**Janusz Bossak:** A nie?

**Damian Kamiński:** A nie, jak te raporty.

**Anna Skupińska:** No chciałam coś pokazać, ja bym chciała coś pokazać, ale niestety ten GlobalConnect mi się nie chce połączyć. Jakoś mi się zaciął, nic się nie odzywa, więc znowu się trochę pewnie zresetować komputer i parę rzeczy. Ale w poprzednim sprincie pracowałam nad dashboardami, źródłami danych systemowymi i będziemy zawsze zmieniać dlatego, że część tych źródeł danych, które są, nie są – online średnio działają na MSSQL ze względu na ujemne ID. Trzeba zrobić, żeby nie były ujemne, żeby móc coś z tym. Żeby móc, żeby to dokończyć, tylko, że gdy ktoś inny mógł pokazać na deweloperskim, ja nie mogę, nie mogę się połączyć do piwnicy. No cóż, to trudno nie będzie.

**Damian Kamiński:** Ja mogę pokazać sekundkę, sekundkę, już, już. W sensie, już są skończone te dashboardy, tak?

**Anna Skupińska:** Możesz pokazać źródła, co dodasz. Nie pamiętam.

**Damian Kamiński:** Momencik, też nie jestem już połączony.

**Barbara Michałek:** Znaczy, ja nie mam nic na testach, jeśli chodzi o te dashboardy, więc.

**Anna Skupińska:** No bo jeszcze nie było oddawane do testów, Basia.

**Barbara Michałek:** A Łukasza chyba tak? Łukasz jest na urlopie, więc.

**Anna Skupińska:** Ratujemy jeden – jedna rzecz do testowania. Nic – zauważyłam, że tak długo siedziała w testach, więc pomyślałam sobie, że po prostu to ma niski priorytet.

**Damian Kamiński:** Początkowo – zaraz pokażę. No dobrze, co mam, gdzie mam przejść? Do źródeł?

**Anna Skupińska:** Ktoś weźmie źródła danych? I na systemowe. Tak, mam zadanie 22132 na Internet Test. I tak chyba już czeka z miesiąc, nie myśląc, że są tydzień.

**Barbara Michałek:** A jest różnica pomiędzy miesiącem a tygodniem.

**Anna Skupińska:** Tak. Jest to więc myślę – albo projektu, więc myślałam, że może macie coś innych na wyższych priorytetach.

**Barbara Michałek:** Jest, tak było. Było co innego.

**Anna Skupińska:** OK, to. Ja się lubię.

**Damian Kamiński:** Coś to się dzieje.

**Anna Skupińska:** A resztę systemowe – i to jest MSSQL wersja piąta. Ja tutaj.

**Damian Kamiński:** Mhm, to które mam wybrać?

**Anna Skupińska:** A wiesz, te na przykład też – mnie statystyki. I to tutaj – jak teraz będziesz na klucz, to widzicie, że to jest właśnie połączenie. I to jest lokalne i na MySQL składa poprawnie, bo MySQL składa sobie radzi. Jeżeli nazwy mają u-minus, to MSSQL ma z tym problem i to jest źródło danych systemowe, które jest lokalne. Ona się tworzy też.

**Piotr Buczkowski:** Czyli chodzi o nazwę tabeli tworzone na podstawie jej – nie było nigdzie pisałem, że MySQL.

**Anna Skupińska:** Tak, tak, ja myślę o tym, że wystarczy po prostu zmienić jej nazwę tabeli, żeby coś z tego minusa się – coś jakiś inny znak, na przykład.

**Damian Kamiński:** Trzeba dać teraz wiodące, na przykład może. Zero 01.

**Anna Skupińska:** A czy myślę, że to po prostu zamiast minusa dać podkreślenie i też będzie w porządku?

**Damian Kamiński:** Albo.

**Piotr Buczkowski:** Albo S, jakoś S_systemowe, tak?

**Anna Skupińska:** Dlatego, że czy tylko, że mamy już zamieniać całość, że zamiast ujemnych ID, to będzie na GUID'ami i z kolumną, która będzie inne rzeczy napisała. No i to są jeszcze inne. Źródła, które zostały zaprojektowane. Przez.

**Damian Kamiński:** Dobra, czyli tutaj jest wszystko. Znaczy, ja zastanawiam się, czy to na pewno powinno być możliwość zmiany tego harmonogramu. Ale to już niekoniecznie może.

**Anna Skupińska:** Pytanie, bo to pytanie trochę do, do was tego, że na razie to jest – można zmienić. Uczyniłam je, zmieniałam, ale możemy ustawić, żeby można – ktoś mógł sobie zostawić, bo, nie wiem, może ktoś ma inne potrzeby i na przykład takie za często albo za rzadko.

**Janusz Bossak:** Wracając.

**Damian Kamiński:** No dobra, do, do przemyślenia. Według mnie systemowe to systemowe – to nasze, my o tym decydujemy, nie częściej niż raz dziennie. Tutaj co godzinę, według mnie nie ma potrzeby, żeby to.

**Anna Skupińska:** A może ktoś chciałby, żeby było rzadziej? Było na przykład wolniejszy system?

**Janusz Bossak:** Dobrze, ale to nie jest teraz czas na tym.

**Damian Kamiński:** No nie, teraz, co?


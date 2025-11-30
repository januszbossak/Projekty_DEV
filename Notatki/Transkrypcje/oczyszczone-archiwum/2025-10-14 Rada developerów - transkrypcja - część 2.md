**Data spotkania:** 14 października 2025, 08:00 - część 2

---

**Piotr Buczkowski:** To znaczy tak naprawdę tutaj trzeba też pomyśleć o migracji. Bo to już jest.

**Anna Skupińska:** E, tak, to też – opowiedzieć o tym, że żeby to się, jeżeli jest po staremu, to żeby się ustawiło na nowy system bez problemu.

**Piotr Buczkowski:** Trzeba dodać kolumnę.

**Anna Skupińska:** A jeszcze jest inny problem, bo.

**Piotr Buczkowski:** Prawda? Czy jeżeli kolumna, czy ta kolumna system raport, że miała też na przykład ujemną wartość i tam przepisywać wartość zajmuje. Jeżeli już utworzymy, tak ignorujemy wartość normalną i później przy jakiejś migracji? Jeżeli ktoś ma ustawione gdzieś minus.

**Anna Skupińska:** Tak, to też.

**Piotr Buczkowski:** To, że w ustawieniu tej kolumny szukać tak i poprawić.

**Anna Skupińska:** Tak, więc problem też taki jest, że jeżeli ktoś już zrobił wcześniej jakiś raport oparty o źródło systemowe i ono nagle się zmieni ID, to nagle to ID będzie wskazywać na miejsce, gdzie nic nie ma, więc te raporty wszystkie zostaną popsute.

**Piotr Buczkowski:** Dobrze, dlatego mówię, to – która jest teraz, trzeba przepisać do nowej kolumny.

**Anna Skupińska:** Tak.

**Piotr Buczkowski:** I przy szukaniu źródła z raportu szukać po tej – jeżeli wartość ujemna, to szukać po tej kolumnie, gdzie zostało to przepisane.

**Anna Skupińska:** Mhm.

**Janusz Bossak:** Ja mam wrażenie takie, że nasi klienci jakoś chyba nie bardzo na razie korzystają z tych źródeł systemowych i z tych raportów systemowych. I prawdopodobieństwo, że ktoś sobie zrobił, jest bardzo małe.

**Piotr Buczkowski:** Ewentualnie.

**Janusz Bossak:** Ja bym tą kompatybilnością.

**Piotr Buczkowski:** Na czas migracji dodać.

**Damian Kaminski:** Jest zerowe, mówiąc wprost.

**Janusz Bossak:** Zerowe. Ja bym tą kompatybilność tutaj przerwał, po prostu to i zrobić po bożemu, tak jak tu Łukasz mówił, tak jak to powinno być. Po prostu trudno, najwyżej nie będzie działać.

**Łukasz Bott:** Mhm.

**Damian Kaminski:** Nawet serwis nie miał do końca świadomości, to wybrzmiało. Była taka informacja, że coś takiego jak raporty systemowe istnieją. Abstrahując już od klientów – jak zdarzy się jeden klient, który raz tam zajrzał, to na pewno z tego nie korzystał jakoś tam wybitnie i nic tu się nie stanie.

**Łukasz Bott:** I też mi się – jeżeli zajrzał, to zajrzał do raportów systemowych, ale niekoniecznie może tworzył coś własnego na podstawie źródeł systemowych, bo to są 2 odrębne byty. Tak, no to, że ze sobą.

**Damian Kaminski:** Z ciekawości. Zawsze może poprawić – tak, jeśli struktura źródła się nie zmieni, można wyeksportować i zmienić ID źródła systemowego i będzie działać.

**Łukasz Bott:** Tak, no można. Mm, tak, ewentualnie możemy przyjąć taką zasadę – prawdopodobieństwo jest, jak mówicie, prawdopodobnie niskie, że ktokolwiek z tego korzystał. To możemy przyjąć na klatę, że jeżeli będzie miał z tym problem, to mu tam nie wiem, na zasadach gwarancji nieodpłatnie mu to skonfigurujemy.

**Janusz Bossak:** Dokładnie tak, nawet możemy tutaj już nie wyręczać się serwisem, w sensie Danielem, tylko w razie czego to czy Łukasz, czy ktoś tam z nas się zaloguje i tam 1, 2 czy 3 raporty poprawi, jeżeli będzie trzeba. I koniec.

**Łukasz Bott:** Tak. Dokładnie, tak zróbmy i tyle.

**Janusz Bossak:** Tak jak Piotr mówi, teraz jakichś takich mechanizmów, które tam uwzględnią, że był minus, teraz nie ma i tak dalej – zróbmy to po prostu tak jak powinno być i już. Ania, możesz to zaplanować?

**Anna Skupińska:** Jasne.

**Janusz Bossak:** Tutaj Damian, ty się opiekujesz, czekaj mnie się tymi systemowymi. Łukasz, a Łukasz się opiekujesz? Dobra, to Łukasz z Anią zaplanujcie to dokładnie. Jeszcze raz, to przejście nasze. Jeszcze raz na to przejście na te buildy dla raportów systemowych i po stronie źródeł systemowych.

**Damian Kaminski:** Łukasz.

**Łukasz Bott:** Źródłem.

**Janusz Bossak:** I po stronie raportów, no i tak, żeby się nie popsuły normalne raporty i normalne źródła – tak, nie systemowe.

**Łukasz Bott:** No.

**Janusz Bossak:** Może to jest moment, kiedy warto przejść w ogóle na GUID w źródłach systemowych, obojętnie czy systemowych, czy nie systemowych – źródłach danych. Tak, źródło danych ma swój GUID.

**Piotr Buczkowski:** Część z raportem, z raportów warto. Chcemy dzisiaj innego ID. Odwołania.

**Janusz Bossak:** To jest zadanie dla was tutaj, Łukasz i Ania. Tak, musicie to przemyśleć, wszystkie konsekwencje właśnie używania tego w raportach, dashboardach, stare raporty trzeba przemyśleć, czy coś tam się nie popsuje. Wiecie, wszystkie te skrajne przypadki, tak, żeby wziąć pod uwagę. Także to jest wasze zadanie na następną radę za 2 dni, żebyście mieli już taki przygotowany projekt tego przejścia na te GUID ze wszystkimi możliwymi potencjalnymi konsekwencjami. Dobra, to mamy. Następna jest tabelka w formularzu.

**Piotr Buczkowski:** To było mój błąd? Rzeczywiście, ja to zgłaszałem. Tabelka była, nie ma. Moja, moje. Moje to. Gdyby nie wywołało, że to się uświetni – tak, tabelka w postaci tabela. Jeżeli to jest tabela zagnieżdżona w tabelce typu formularz. Bo to musi być bardzo mała tabelka, 2-3 kolumnami, żeby to miało sens.

**Janusz Bossak:** No tak, tak, no bo tu na tym małym kafelku – bo rozumiem, że to chodzi o te małe kafelki, nie o.

**Piotr Buczkowski:** Tak.

**Kamil Dubaniowski:** Tak, tak, te.

**Piotr Buczkowski:** Tak. Możecie wyświetlić to 2169 czy ja mam wyświetlić?

**Janusz Bossak:** Weź.

**Piotr Buczkowski:** To chodzi o to, tak?

**Janusz Bossak:** No, no, no, no, tak rozumiem. No OK, wiecie, sens wyświetlania tego jest, jak mówisz – duża tabela, to jakby nie ma sensu. No ale to jest kwestia tego, jak to sobie tam poukłada. Tak, jeżeli tu będzie miał tabelkę, na przykład nie wiem, z imieniem, nazwiskiem członka rodziny, to czemu nie? Tak? No dobrze.

**Kamil Dubaniowski:** Dobra, no ale co na to, jak ktoś doda tutaj 20 pól? No to musimy też to obsłużyć, skoro to obsługuje.

**Piotr Buczkowski:** No to będzie źle wyglądało, ale.

**Janusz Bossak:** Sprawdźmy.

**Piotr Buczkowski:** Nie, nie, to nie, nie, to nie.

**Kamil Dubaniowski:** Nie, no bo to jest osobne zgłoszenie też.

**Piotr Buczkowski:** Nie.

**Janusz Bossak:** Skoro być tak.

**Piotr Buczkowski:** Niech ktoś przemyśli. Zobaczy, że to źle wygląda i przemyśli swoje zachowanie.

**Kamil Dubaniowski:** No myślę, że tu też się wypadki przypadek, no ale jak już wyszło to, żeby ten kontakt utrzymać.

**Janusz Bossak:** Nie, no, niech staniesz, wszystko obsłuży. Bo to trzeba by tą tabelkę też zamienić na, z kolei znowu już.

**Piotr Buczkowski:** Powinno dobrze działać, jeżeli tabela w tabeli, ale obydwie jako formularze. Tak. Wtedy okej.

**Janusz Bossak:** Bo to wtedy będzie taki formularz w formularzu.

**Piotr Buczkowski:** Tak jak, tak jak w telefonie. Jak to bywa w telefonie – o telefonie?

**Janusz Bossak:** No to jeżeli to tak się wyświetla. No to jest pytanie, czy tabelkę zagnieżdżoną można ustawić w tryb podformularza?

**Piotr Buczkowski:** Formularza, nie podformularza.

**Janusz Bossak:** Formularzem, tak.

**Piotr Buczkowski:** Podformularza to jest to z lewej, tak, i nie można. Znaczy, nie będzie się już mieściła i też nie ma porady.

**Janusz Bossak:** Jako podformularz może być tak.

**Damian Kaminski:** To.

**Piotr Buczkowski:** Tak, tak. Znaczy, powinniśmy się brać – tak jak na telefonie, tak?

**Janusz Bossak:** No nie wiem, jak się wyświetli.

**Łukasz Bott:** W sensie, w wersji mobilnej?

**Piotr Buczkowski:** Tak, tak. Znaczy z takim przeciąganiem lewo, prawo, tak.

**Janusz Bossak:** No właśnie, to trzeba pokazać.

**Damian Kaminski:** Czyli nie, OK, czyli w formie tabelarycznej, tylko po prostu z przeciąganiem.

**Piotr Buczkowski:** Nie, nie, nie.

**Janusz Bossak:** Nie, nie, nie, bo słuchajcie, bo są 2 rozwiązania. Pierwsze rozwiązanie – jeżeli zamieniam tabelę główną na widok formularza, tak jak tu, to mogłoby być tak, jak mówi Piotr. Jakby konsekwentnie, tak jak na mobilnym widoku, wymuszenie pokazywania tej podtabelki też jako formularzowej po prostu.

**Piotr Buczkowski:** No tak.

**Janusz Bossak:** Czyli nie ma czegoś takiego, że mogę sobie właśnie taki obrazek zrobić jak teraz, czyli że mam pierwszą tabelę, tą główną, jako formularz, a tą podtabelkę jako tabelkę. I to jest pytanie, czy chcemy, czy nie chcemy tak, żeby było tak, że to.

**Damian Kaminski:** A czy to nam coś upraszcza? Teraz rozpatrujemy to w skrajnych przypadkach, czyli tabela jednokolumnowa i tabela wielokolumnowa.

**Janusz Bossak:** Trudno ocenić, czy coś upraszcza. Tego, wolałbym mieć jakby jednolitość zachowania, tak, żeby, wracając do tej dokumentacji naszej, że to tak działa, jakby było wiadomo. Ale jeżeli ktoś ustawia w tej tabelce, którą tu Piotr pokazywał wewnątrz formularza, bardzo dużo kolumn, no to musi się liczyć z tym, że będzie mu ta tabelka dla niego niewygodna, tak, że będzie musiał przewijać. Ale dlaczego by mu tego zabronić? Tak, o to mi chodzi.

**Damian Kaminski:** No, no, właśnie do tego zmierzam, bo my możemy napisać to nawet w konsekwencji tej dzisiejszej dyskusji, że my tak zalecamy, a wszystkie inne rozwiązania.

**Janusz Bossak:** I.

**Piotr Buczkowski:** Znaczy, dobrze, przy – powinniśmy przywrócić stare zachowanie i tylko tyle.

**Janusz Bossak:** Tylko tyle, dokładnie. Znaczy, no.

**Damian Kaminski:** Możecie to podsumować w takim razie?

**Janusz Bossak:** Mnie jeszcze interesuje odpowiedź na jedno pytanie, czy dobrze było, gdyby ktoś w międzyczasie by kliknął taki przykład. Bo Piotr powiedział jedną rzecz, która mnie zainteresowała, że na mobilnym to się wyświetla jako formularz. Znaczy, formularz? Tak, no bo złe nazwy używam. Czyli tam jest to zamienianie tej tabelki?

**Piotr Buczkowski:** No bo, no bo, no – jeżeli, jeżeli popatrzysz na to, to to wygląda jak ekran telefonu. Tak, jeden taki sekcja to jest tak, jakby ile telefonów obok siebie włożyć.

**Janusz Bossak:** Tak. Ale wiem. Ja wiem, ja wiem, tylko mi chodzi o to teraz, jak to, co jest na czerwono zakreślone, wygląda na telefonie, czy tak jak jest?


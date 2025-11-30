**Transkrypcja**

28 października 2025, 09:01AM

**Janusz Bossak** 0:17  
No hej ja.

**Anna Skupinska** 0:18  
Cześć.

**Damian Kaminski** 0:21  
Cześć.  
Dobrze tutaj z tym data source, aniu, to coś potrzebujemy omawiać na Radzie.

**Anna Skupinska** 1:02  
Jest to pewna, chyba, że chciałabyś coś zmienić.

**Damian Kaminski** 1:02  
Czy na razie to odpuszczamy?  
W sensie to jest oznaczone jako naradę, to nie jest na ten moment krytyczny, zostawiam to, no bo nie wiem jaką mam.

**Piotr Buczkowski** 1:12  
No to tam coś było z tym z tym logowaniem chyba tylko męsku, a co się okazało, że już jest najnowszej wersjach. Już to jest chyba tak.

**Damian Kaminski** 1:19  
Ale to jest dashboard source source, synchronization a nie, bo ty mówisz o.

**Piotr Buczkowski** 1:25  
Raportach dobrze.

**Damian Kaminski** 1:25  
To raportach, a tamto z raportami ani się udało.

**Anna Skupinska** 1:29  
A jeszcze tego nie czekałam, ale myślę, że będę musiał się tym zająć.

**Damian Kaminski** 1:34  
A no to to to ma priorytet nad tym to, bo tamtego ja nie widzę na Twojej tablicy.

**Anna Skupinska** 1:37  
Aha, rozumiem.

**Damian Kaminski** 1:41  
Nie widziałem.  
To zostało na poprzednim sprincie.

**Anna Skupinska** 1:49  
Którego zadania?

**Damian Kaminski** 1:51  
No właśnie nie pamiętam którego zadania mówiąc wprost, ale.  
Było takie zadanie.

**Anna Skupinska** 2:00  
Chyba go nie ma o tym mówiliśmy, ale nie.

**Damian Kaminski** 2:02  
Nie, nie było na pewno.  
Było na pewno, bo ja przepisywałem Piotrowi.  
To było skład coś.  
Tutaj.  
No i jest przypisane do ciebie.  
Dobra.  
Dwudziesty pierwszy rok.  
No te stare sprinty trzeba chyba powywalać bo widzicie jaki błąd się wkradł.  
No dobra, już nie istotne, w sensie nie wiem, czy akurat stąd to to możemy wywalać, może jednak to był.  
Zła sugestia, ale dobra, no to to jest priorytet, jeden to musimy zrobić, bo to nam uprości rozwiązywanie błędów wszelkich z raportami. Tak, to znaczy może nie wszelkich, ale w większości.  
Więc no to to co ci wysłałem mi to i to jako drugie, to to ma wyższy priorytet niż te tematy, które. No właśnie są jeszcze nie dopracowane w kontekście.  
W kontekście wymogów, a wiem, że Janusz jeszcze teraz pracuję nad tymi raportami systemowymi, więc no gdzieś tam to dogramy i może na przyszły sprint to zaplanujemy.  
Dobrze, więc tak to pomijam Jeszcze raz powiedz tylko potwierdziłeś tak.

**Janusz Bossak** 3:35  
Tak tak, może przeglądam teraz te raporty i patrzeć co nam jakby funkcjonalnie brakuje do tego.

**Damian Kaminski** 3:42  
Dobra to jest donut pilem to.

**Janusz Bossak** 3:43  
Tam jest, ale taki bym powiedział kluczowych rzeczy do zrobienia to przedyskutowania pewnie na następnej Radzie, ale tu.

**Damian Kaminski** 3:56  
Ale tak patrze w pierwszej kolejności na.  
Na to, co jest przypisane gdzieś tam do sprintów.  
O k to chyba mój dopisek.  
Z tą diagnozą.  
No dobrze, INFORMACJA O synchronizacji słowników tu w zasadzie chodzi tylko i wyłącznie o taki błąd. Pytanie jaka tu jest sugestia co do naprawy tego i.  
I w zasadzie wszystko i temat jest ready tu du.

**Piotr Buczkowski** 4:42  
Po pierwsze sprawdzić co to jest po drugie.  
Zmienić miejsce, z którego jest zatrzymywana Data ostatniej synchronizacji, bo się zmieniło.

**Kamil Dubaniowski** 4:53  
No to było osobne zgłoszenie jak dobrze kojarze z tą datą.

**Damian Kaminski** 5:00  
A pomożesz mi to znaleźć?

**Kamil Dubaniowski** 5:05  
Kojarzę też było Piotra.

**Damian Kaminski** 5:07  
To było u Piotra. To był Piotr, tylko ja to zdjąłem.

**Kamil Dubaniowski** 5:09  
Nie, nie kojarzę to tą zmianę ostatniej synchronizacji i to zgłaszał zatrzymana Kacper tuczyński.

**Piotr Buczkowski** 5:14  
Albo co 2, bo to co 2 zgłoszenia tak jedno to jest takie, że już teraz definicji słownika nie ma datę ostatniej synchronizacji, tylko jest tam z tych historii.  
Ostatni wpis, a druga to jest takie jakieś tam prze prze synchronizacji z synchronizacji z agenta jest jakiś taki błąd.  
Trzeba by sprawdzić co do czego.

**Kamil Dubaniowski** 5:35  
A ja chyba jeszcze trzeci to ma do tego do mieszałem, bo Kacper to zgłaszał, że w rejestrach nie widać daty prawdziwej synchronizacji, jak to są tym są tacy no to to było osobno zgłoszenie.

**Piotr Buczkowski** 5:43  
No to te samo.  
A może to rejestr były?  
Dobrze.

**Damian Kaminski** 5:53  
No raczej należy sprawdzić skąd jest pobierana data ostatnich synchronizacji tak i zaktualizować.  
Co jeszcze powiedziałeś?

**Piotr Buczkowski** 6:00  
Jest tabela z synchronizacja historii, odnosząca się zarówno do słowników, jak gdy do rejestrów zmniejsza pobierać.  
Data ostatniej synchronizacji.

**Damian Kaminski** 6:10  
Więc pointy do tego jest są przygotowane.

**Piotr Buczkowski** 6:14  
Trzeba powiedzieć, przygotować.

**Damian Kaminski** 6:15  
A o k dobra.

**Piotr Buczkowski** 6:21  
Znaczy inaczej jest endpoint do popierania properties of słownika. Czy rejestr tak i w tym w tym momencie trzeba tak zmienić sposób pobierania tej daty?

**Damian Kaminski** 6:32  
No dobrze, to Teraz ja w ogóle zastanawiam się na ile jest to kluczowe w kontekście starego formularza, czy warto to tu poprawiać, skoro wszystko działa, bo ja bym to rozdzielił, czyli należy przygotować ten point jako backend.  
Jak będziemy robić nowy wygląd to się wyeliminuje ten błąd, bo pewnie te słowniki będziemy opiekować.  
W najbliższym czasie, a tu nie ma żadnych problemów.  
Blokujących, poza tym, że się wyświetla wykrzyknik.

**Piotr Buczkowski** 7:11  
To jest co to jest?  
Powiedzmy.  
Powiedzmy czy mniej logistycy?

**Damian Kaminski** 7:17  
Nie wiem co sądzicie.  
No wiesz, to wszystkie pewnie środowiska gdzie jest synchronizowane.

**Piotr Buczkowski** 7:36  
Trzeba nie dyskutować, trzeba to tak nazwać, tak.  
Czy chcemy to jak nazwać, czy nie to tej inne pytanie? Tak, nie zgadniemy o co chodzi?

**Damian Kaminski** 7:47  
Dobra odpinam to.  
Dobrze to z rzeczy, które są przypisane jakkolwiek do sprintu to jest wszystko jakoś tu wybitnie tego mało.  
Bo tylko z ostatnich 30 dni.  
No dobra, no to jest część date. No dobra, możemy się skupić na tych.  
Nie wiem czy ktoś ma jakieś priorytety własne.

**Kamil Dubaniowski** 8:29  
Ja kojarzę, czekajcie na ciebie chwilę.  
Temat z wczoraj i wiem żeby tego.

**Damian Kaminski** 8:41  
Myślenie to przejdziemy przez te, które dotyczą klientów.  
Pewnie dzisiaj nam się skończy czas.

**Janusz Bossak** 8:54  
Tak w międzyczasie.  
Mocnych module raport owym.  
Portach systemowych znaczy to, czego nam znaczy po części powiedzmy, brakuje to taki nazwijmy to mini ETS Jestem, czyli takiego strumieniowego przetwarzania danych. Tak, no, bo w tej chwili, żeby zrobić jakieś źródło danych, no to mamy zapytanie sql owe, które się wykona i i jest no jedynym.  
Ułatwieniem w tym jest to, że może być przyrostowe.  
Do niektórych jakby zastosowań, jeśli chodzi o systemy, raport owe dane trzeba przygotować sposób.  
Taki systematyczny, tak i nie zawsze jest to możliwe za pomocą jednego zapytanie sql.  
Więc dobrze by było to zastanowienia, tak ja nie mówię, że mamy to robić tylko przedyskutować takim mini systemy TL, to chodzi mi o to, że wiecie co to jest ettl nie takie system, który przetwarza jakby strumieniowo, że dostajesz jakieś dane o nie przetwarza na jakieś, no i tworzy tam tymczasową tabelę, potem jakiś tam inny sposób dołączając jakieś jeszcze dane, przetwarza tą drugą tabelę nie i taki takich krokach.

**Piotr Buczkowski** 10:09  
Nie robimy. Sumie robimy system Works.

**Janusz Bossak** 10:13  
Nie, ale ja mówię o przygotowaniu danych do raportów ze źródeł, nawet tych naszych, tak, żeby przetworzyć te dane, tak, żeby one potem były w raportach łatwo dostępne i szybko dostępne.  
Ten system ets, no to on przetwarza raz tam na przykład w nocy coś tam przyrost owo będzie dorabiał.  
Ale właśnie brakuje mi takiego mechanizmu, żeby jak zrobi jedną tabelę, ten deb src coś tam i jak ją skończy to żeby to wywołało jakby aktualizowanie następnej tak o tym tylko chodzi. Właśnie tylko taki mechanizm, żeby można było wskazać jakby strumień kolejności aktualizacji tych deb src szczególności tych.

**Damian Kaminski** 10:55  
No właśnie, czyli chodzi tylko o to, żeby tutaj móc ustawić.  
Harmonogram coś jak na regułach, tak?

**Janusz Bossak** 11:03  
Tak to znaczy. No nawet nie harmonogram, tylko że tutaj powinno być coś, że następne.  
Synchronizuj coś tak albo w drugą stronę, że synchronizuj o ile została zaktualizowana tabela, tam jakaś nie.  
Czyli masz powiedzmy tabelę, a.  
I tabelę BI tabelę c tak i chodzi mi o to, żeby tabela c syn jakby synchronizowana się wtedy gdy zakończyła się synchronizacja tabeli. BA tabela b ma się synchronizować wtedy kiedy skończyła się synchronizacja tabeli, a.  
A tabela a jest pierwsza tak czyli najpierw robimy a na przykład raz na godzinę jak to się skończy, ale jak się skończy.  
To wtedy się zaczyna synchronizacja tabeli b.

**Damian Kaminski** 11:52  
No a przesunięciem tego nie zrobimy, w sensie nie mamy gwarancji zakończenia, tak.

**Janusz Bossak** 11:52  
Tak jest.  
A nie wiem jak długo się będzie test chroni zostać. No właśnie nie wiesz czy to będzie 2 sekundy, 5 minut czy 20 minut? Tak.

**Piotr Buczkowski** 12:02  
Znaczy, to jest to jest pokolei robione nie jest robione celowo.

**Damian Kaminski** 12:02  
No.

**Janusz Bossak** 12:07  
No ale właśnie chodzi mi o to, żeby to tylko tyle tak, żeby jawnie powiedzieć, że jak skończysz to.

**Damian Kaminski** 12:12  
No to po kolei, ale to to to może inaczej, a jak po kolei to jak po kolei?

**Piotr Buczkowski** 12:13  
Znaczy, to to trzeba było.

**Damian Kaminski** 12:17  
Według 1 2 3.  
No czyli tu trzeba było indeks nadać tak.

**Piotr Buczkowski** 12:23  
No nie, pewnie zależy od i poda 3 dni.  
Innego także i on by sobie sterował, że.  
Najpierw te, które niezależnie od niczego później po kolei.  
Ta, która zależała.

**Janusz Bossak** 12:37  
Tak no tak.

**Damian Kaminski** 12:38  
Te, które zależą tak.

**Janusz Bossak** 12:39  
Ta, która nie zależy od niczego, to dla niej jest ten harmonogram. Tak naprawdę to ten harmonogram nie, bo tutaj masz co godzinę i o k, ale w innym.

**Piotr Buczkowski** 12:39  
Tak.

**Janusz Bossak** 12:50  
W innej tabeli, która w jakiś sposób korzysta z danych z tego deser c powinno być w harmonogramie nieco godzinę, tylko po zaktualizowaniu klaud agent.  
I tyle.  
Czy jak tam to się zaktualizuje skończy to wtedy ma się robić to.  
To to jest.

**Damian Kaminski** 13:11  
Czyli chodzi ci o to, że wtedy harmonogram synchronizacji tutaj, po aktualizacji innej w zasadzie tu nie ma żadnego stricte harmonogramu, tylko jeśli to się zaktualizuje, to tamto też ma się wywołać.

**Janusz Bossak** 13:22  
To to dopiero tamta ma się wywołać.

**Damian Kaminski** 13:24  
Czyli tylko na jednej de facto ustawiasz cykliczność, a drugie są konsekwencją.

**Janusz Bossak** 13:28  
Czy na początku tego łańcucha nie? No, bo możesz mieć wiele takich łańcuchów, tak?  
Yy zaczynających się od tutaj klaud agent albo zaczynające się od syn Group, ale jak zrobi się syn Group, to potem ma się zrobić. Nie wiem tam następny test webcon waniem, bo tamten zależy od tych danych, które będą w tym pierwszym i to tyle.  
Nie wydaje się to jakoś skomplikowane, ale dużo by pomogło przy przetwarzaniu danych.

**Damian Kaminski** 13:57  
To może powinno być tutaj dopisek, następnie wykonaj synchronizację jakiejś tam innej.

**Janusz Bossak** 14:03  
No.

**Damian Kaminski** 14:04  
Chociaż to wtedy.

**Janusz Bossak** 14:06  
W tym harmonogramie powinno być.

**Damian Kaminski** 14:06  
Chociaż może i podejście Piotr.

**Janusz Bossak** 14:09  
Zamiast co godzinę czytam co ten tylko po.  
Zakończeniu.  
Nie wiem synchronizacji jakiegoś tam innej tabeli z tych nie.  
Nie wiem jak to wywołać, tak to to już zostawiam tutaj deweloperom jaki to trigger by był i skąd byśmy wiedzieli, że tamta się synchronizacja skończyła tak, no ale.  
No to mi chodzi, żeby to było.

**Damian Kaminski** 14:34  
Nie no to to wiem, to chyba się nawet vlogach gdzieś tam zapisuje, tak mi się wydaje.  
Chociaż może to dotyczy.  
Rejestrów, a nie źródeł.

**Janusz Bossak** 14:45  
Będziemy.  
To jest jeden z moich wniosków odnośnie patrzenia na te dane.  
Do tych raportów systemowych nie.  
Po prostu niektóre raporty wymagają trochę bardziej.  
Złożonych przekształceń.  
Aby przygotować do nich dane, to jest drugi jeszcze taki temat, jeżeli jeszcze tutaj to jest.  
Jakby linia czasu.  
Pytanie, jak sobie radzić?  
Z brakami w datach.  
Czyli.  
Po prostu jakieś mamy miesiąc 1, 2, 3, 4 do 31 i w niektórych.  
W dniach nie ma czegoś, szuka, nie utworzono spraw albo nie zamknięto spraw.  
W tej chwili jest tak, że chociaż tu z Markiem rozmawiałem na drugiej linii przed chwilą i on mówi, że to niby jest zrobiony, ale jakoś mi to nie działa.  
Żeby się pokazywał, mówię o wypełnianiu.

**Damian Kaminski** 15:52  
Ale o czym teraz mówisz?

**Janusz Bossak** 15:57  
Też o raportach systemowych i o tym, żeby.  
Wypełniać dni.  
W których nie było żadnego zdarzenia. W tej chwili mamy.

**Damian Kaminski** 16:07  
No ale no dobra, tylko wydaje mi się, że zmieniamy mocno temat.

**Janusz Bossak** 16:11  
No dobra, no, czekałem na to, aż ktoś ktoś przygotuje się do dobra koniec z mojej strony.

**Damian Kaminski** 16:17  
Dobra, to idziemy z tym. To znaczy, tak?  
Tutaj w ogóle ja podważam zasadność tego, czyli rozbudowanie funkcji attykę i sprint.  
Mało kto tego używa rosman tego potrzebował dałem gotowego csa to poprawić. Patryk jest zadowolony, klient jest zadowolony.  
Nie wiem czy w ogóle to robić, czyli chodzi o to, żeby z poziomu tutaj sprawy.  
W ramach funkcji dało się sterować, co ma wydrukować z tego nagłówka.  
Czy widzicie zasadność to w kontekście nie wiem jakiś innych klientów, ktoś tego naprawdę korzysta i aż taki musi mieć wpływ na to, co tu się wyświetli.

**Piotr Buczkowski** 17:01  
Przecież słyszał blody to komentów.

**Damian Kaminski** 17:04  
No tak napisałem to w komentarzu.  
Że zostało to zrealizowane szablonem więc.  
Pytanie, czy to w ogóle powinno wisieć na blogu czy jawnie to odrzucam.

**Janusz Bossak** 17:22  
Znaczy dobrze jest, by to było wyjaśnione i żeby konsultanci wiedzieli, że tak można, bo podejrzewam, że nie wiedzą.  
I dokładnie jak to trzeba zrobić, nie.

**Damian Kaminski** 17:35  
Czyli, że trzeba przygotować do tego dokumentacja?

**Janusz Bossak** 17:38  
No dostosowanie jak do 99% pozostałej części, a mówi tak.

**Damian Kaminski** 17:48  
Mogę to wrzucić do siebie. Nie wiem, kiedyś to zrobię. Nie obiecuję tu żadnych.  
Robiłem to patrykowi, więc no wiem, jak to się robi.  
Dobra, może przejdźmy dobra, to to był klient. Teraz tak alians z nim brak wali.

**Kamil Dubaniowski** 18:06  
Czy ja mam to 16 5 5 8 to jest iq. Widać, że już temat, który przeleżał swoje a.

**Damian Kaminski** 18:15  
W sensie chcesz je podnieść? Tak.

**Kamil Dubaniowski** 18:15  
Konsultanci niego tak tak konsultanci.

**Damian Kaminski** 18:17  
Dobra.

**Kamil Dubaniowski** 18:20  
Ona jest tutaj na radę już wrzucona i chciałbym omówić.

**Damian Kaminski** 18:22  
Tylko.  
16, dobra, proszę bardzo.

**Kamil Dubaniowski** 18:26  
Tak no to jest temat, który gdzieś tam wraca przy każdej aktualizacji, bo muszą coś tam u danego klienta zmieniać konfigu a ta zmiana z tego co z dyskusji wynika wcale nie jest dobra, bo to było specjalnie zrobione żeby tak działało.

**Damian Kaminski** 18:44  
Dobra, ja to weź. No właśnie powiedz to mam to otwarcie otworzyć coś.

**Kamil Dubaniowski** 18:44  
O co chodzi tak, o co chodzi? To chodzi o.  
To jest dyskusja kiepskim suszenia. Chodzi o to, że w raporcie typu gant.  
Ee wcześniej działało tak, że jak wchodziłeś na ganta to ładowało ci wszystkie kategorie, czyli klient na przykład zrobił sobie kategorię pokoje i na gacie widział zarówno te pokoje, które w danym terminie są zajęte, jak i te które.  
Danym terminie nie mają żadnych spraw, czyli ładowaliśmy wszystkie kategorie, jakie znaleźliśmy distinct, a ze wszystkich spraw w amo gicie klient miał na przykład 10000 pokoi po całej Polsce pracowniczych. No to ładowaliśmy mu 10000 pokoi i pokazywaliśmy wszystkie tak tak tu, gdzie projekty? Tak?

**Damian Kaminski** 19:27  
Tutaj w wierszach to jest trochę to, co mówi Janusz mówił, no z latami.

**Kamil Dubaniowski** 19:32  
No i teraz zmiana polega na tym, że ładujemy tylko te, gdzie są w danym okresie, czyli październik, grudzień, jakieś sprawy, no i dla klienta to nie jest o k, bo on przez to nie widzi jakie pokoje ma wolne i nie może z tego poziomu na przykład planować, że do tego pokoju przydziela teraz ludzi.

**Janusz Bossak** 19:52  
No to jest dokładnie ten sam.

**Damian Kaminski** 19:54  
Tak to jest dokładnie to samo. No to może powinien być jakiś parametr tylko to niby to samo, ale to jest trochę trochę co innego, bo tam są daty, których nie ma w ogóle, a tu są sprawy, które nie mają danych, więc sprawy istnieją.

**Kamil Dubaniowski** 19:59  
Tak tylko no.

**Janusz Bossak** 20:08  
Ale to jest to same, ale to jest to samo, bo to tam też te daty nie mają danych, bo w jakimś.

**Damian Kaminski** 20:15  
Data nie ma danych, czyli nie ma bytu, a tu byt jest tylko nie ma danych. Aha, może i to no dobra, może i to samo może i masz rację o k Przepraszam, masz rację.

**Janusz Bossak** 20:24  
Jakby danych dostarczonych do tego raportu nie ma tego projektu. Nie ma go, ponieważ nie ma do niego danych, nie więc on też nie jest przesyłany.

**Damian Kaminski** 20:25  
Tak tak, zgadzam się.  
Nie ma tych propozycji.  
Tak.

**Kamil Dubaniowski** 20:36  
Znaczy, to musi być parametrem, tylko ja to widziałem radę, bo tam jest dyskusja Piotr, między innymi nad tym się właśnie się udzielał, że.  
Żeby bardziej, żeby to zrobić dobrze, żeby to znowu nie było niewydajne tak i i pytanie po pierwsze, czy robimy to na starym i na nowym module, czy tylko na nowym, bo tamten klient, który działa cały czas na starym.

**Damian Kaminski** 20:44  
Skąd to wziąć?

**Kamil Dubaniowski** 20:58  
Yy.

**Janusz Bossak** 20:59  
Ona nowym lubimy.

**Damian Kaminski** 20:59  
Nie na nowym według mnie tylko na nowym, no inaczej nie wymusimy.

**Kamil Dubaniowski** 21:01  
Ok.

**Janusz Bossak** 21:03  
To jest tak samo jak Comarch mówił na tym swojej konferencji. Teraz wszystkie rzeczy nowe są w nowym po prostu tak i mało tego i jeszcze w nowym subskrypcyjnych m tylko.

**Kamil Dubaniowski** 21:03  
Mhm no i.

**Damian Kaminski** 21:08  
O to chodzi.  
No.

**Janusz Bossak** 21:14  
Mają cały Plan przerzucania ludzi na subskrypcję, nie, że jak chcesz, to to będzie w nowym subs.  
Więc musisz przejść na nowo?

**Damian Kaminski** 21:22  
I tak jak ktoś kupił lifetime w cudzysłowie, to mają to w nosie po prostu tak chcesz to.

**Janusz Bossak** 21:27  
Tak, oni mają tam Plan do 2029 roku, że wszyscy mają przejść na subskrypcję.

**Damian Kaminski** 21:32  
Mhm.

**Janusz Bossak** 21:33  
Kto się nie zgodzi, to w 2029 roku i tak zostanie przypięty na subskrypcję tylko na dużo, jakby mniej korzystnych warunkach.

**Damian Kaminski** 21:43  
To jest element strategii, ale to już nie to spotkanie.  
Dobra, no jak to zrobić wydajnie? Pewnie musiałby do tego istnieć jakiś Słownik, tak, chociaż nie wiem jak z datami w ogóle, no ale datę akurat są jakkolwiek przewidywalne.

**Piotr Buczkowski** 21:59  
Tate jest proste, no bo wiadomo może być wyliczyć tak.

**Damian Kaminski** 22:01  
Tak, a do tego, a do tego możemy było Słownik synchronizowany, nawet jak są to dane w rejestrze. No to Słownik się synchronizuje z rejestrem i wtedy podpinamy, że kolumna ta to są dane.

**Piotr Buczkowski** 22:12  
Nie, to musiał być polec pole słownikowa.  
Po prostu.

**Damian Kaminski** 22:16  
O k. To musi być pole słownikowe i wtedy zaznaczenie, że.

**Piotr Buczkowski** 22:17  
Ewentualnie ewentualnie rejestrze użytkownicy tak.

**Janusz Bossak** 22:22  
Że coś co istnieje jakby tylko.

**Piotr Buczkowski** 22:24  
Tak nie to, że nie nie robimy, nie robimy tik na kryzys definition tylko.

**Damian Kaminski** 22:24  
Mate by te zdefiniowane.

**Kamil Dubaniowski** 22:25  
Gdzie nie jest?  
Podtekst.

**Damian Kaminski** 22:29  
Mhm.

**Piotr Buczkowski** 22:30  
Lista pozycji słownika lista.  
Z rejestru tak spraw z rejestru lista użytkowników. Nie wiem, co tam jeszcze może być.  
Źródła zewnętrznego, tak.

**Damian Kaminski** 22:43  
Mhm i wtedy po prostu.

**Janusz Bossak** 22:46  
Wydaje mi się, ja bym to ciągnął matka, bo ja mam wrażenie, że myśmy już o tym rozmawiali, że to było.

**Damian Kaminski** 22:52  
Tam star.

**Kamil Dubaniowski** 22:53  
Znaczy, ja też wczoraj to testowałem i Mateusz w tym grzebał, bo Mateusz robił pierwsze zgłoszenie, które tam jest linkowane. No i zrobiłem sobie na testy, pokazuje mi wszystkie.

**Janusz Bossak** 23:04  
Też mi się wydaje, że to już była dyskusja na ten temat i.

**Kamil Dubaniowski** 23:05  
Sprawy.

**Janusz Bossak** 23:09  
Że to było już rozwiązane. Dokładnie dokładnie był ten sam problem.

**Damian Kaminski** 23:14  
No dobrze, no ale to czekajcie, no to mamy zgłoszenie, to jakich ono jest wersji?

**Janusz Bossak** 23:20  
To jest było 16 558, tak jak kamień, w kiedy to było zgłoszone? Weź tą na daty zobaczymy.

**Kamil Dubaniowski** 23:27  
Znaczy, podbili mi to niedawno. Tam w komentarzu jest chyba nawet i od dodali ten tag, który ja niedawno sprowadziłem.

**Damian Kaminski** 23:32  
23.

**Kamil Dubaniowski** 23:35  
No ale podbicie było jakoś w tym tygodniu wczoraj albo.

**Damian Kaminski** 23:38  
Dobra, ale to. No to słuchajcie, to sekunda, no już to sprawdzam utwórz raport.  
Planu.

**Kamil Dubaniowski** 23:48  
Oczy mi się o tyle to nie zgadza, że ja mam zwykłe pole tekstowe i mi nadal pokazuje oba mama to już tłumaczył to tak, że mimo tego, że ja ustawiałem październik to niby on pokazuje dane z całego roku, może to było zmienione.  
Że ten zakres jest większy, że nie tylko z tego co widzę tylko.

**Janusz Bossak** 24:03  
Acres był na pewno.

**Damian Kaminski** 24:08  
Mm.  
I w kolumnach chce mieć wnioskodawcę tak tylko to jest typu Użytkownik.

**Kamil Dubaniowski** 24:15  
No to już widzisz, że ci załadował, tylko też była taka zależność, że.

**Damian Kaminski** 24:18  
Tylko poczekaj, załadował mi. Zobacz mnie 20 razy.  
Nie nie wiedzieć czemu.  
Ale dobra poczekajcie, może wystarczy, a stop stop stop, bo ja to zrobiłem w.

**Janusz Bossak** 24:25  
Bo.  
Gangster.

**Kamil Dubaniowski** 24:28  
Bo to jest to jest gang, a my nowy raport, który tam jest używany, to mamy tutaj inaczej nazywamy to nie jest gang, planowanie zasobów, tak.

**Damian Kaminski** 24:35  
Planowanie zasobów.  
No to masz rację to widać, no to.  
Test nowych tych i koniec.

**Janusz Bossak** 24:44  
Znaczy nie do końca.

**Kamil Dubaniowski** 24:44  
Ale zależność była taka, że po zapisie niby w edycji widać wszystkich, a po zapisie tylko tych, których masz sprawę.

**Damian Kaminski** 24:45  
No.  
Już patrzymy.

**Kamil Dubaniowski** 25:00  
Może oni też na siłę od tych 2 lat ładują kartę jako realizacji nad wpisują w tym łeb konfigu myśląc, że to nadal nie działa no i.  
Bo ja kazałem przetestować, jak kazałem przetestować teraz to mi właśnie dali taką odpowiedź, że nie będą rzeźbić na produkcji, bo oni napisali już ten konflikt.

**Damian Kaminski** 25:11  
Wszystko działa.  
Wszystko działa.  
To czy skąd to bierze to raczej to nie bierze z użytkowników, więc pewnie jest jakiś distinct, więc to może niekoniecznie jest wydajne dla 10, no nie wiem.  
Nie będę tego oceniał, ale według mnie ja mam dużo więcej użytkowników na tym środowisku.  
Możemy sobie spojrzeć.

**Kamil Dubaniowski** 25:39  
No adaś klikaj dalej, bo mi się wydaje, że lista się ludzi zmieniała.

**Damian Kaminski** 25:42  
Nie, nie zmieniała się podskakiwało, gdzie coś gdzieś było. Czekaj Jeszcze raz tam, gdzie przeskoczyło.

**Janusz Bossak** 25:48  
Weź tam Damian.

**Damian Kaminski** 25:48  
O na przykład tu podskoczyło u mnie, ale to dlatego, że widzisz 3 są w jednym terminie, nie.

**Kamil Dubaniowski** 25:54  
O k.

**Damian Kaminski** 25:59  
Tu podskoczyło, bo są 2, ale.  
Dobrze to działa tylko no tych użytkowników jest zdecydowanie więcej jest jakieś Piotr Murawski tak, a tutaj go nie ma.  
Więc.

**Janusz Bossak** 26:12  
Bo nie ma urlopu żadnego tak czytam, nie ma sprawy jak.

**Damian Kaminski** 26:14  
No nie ma urlopu, więc pytanie czy.  
No właśnie, bo widzicie, bo tu jest jeszcze kwestia taka, że tu mam wszystko, ale jeśli dodam.  
Tak jakbym teraz mam Józefa, który nie ma globalnie żadnego urlopu, czyli tak jak mamy tam, powiedzmy, ty mówiłeś o pokojach, tak.

**Kamil Dubaniowski** 26:35  
Mhm.

**Damian Kaminski** 26:36  
Jeśli mam pokój stworzony, który ani razu jeszcze nie był zarezerwowany, to pewnie się taki nie wyświetli, czyli zupełnie nowy, ale jeśli on już jest w danych nieograniczony.  
Czyli może zróbmy tak Dodaj warunek?  
Ee utworzenia Data utworzenia.  
Miesiąc w roku, gdzie w roku.  
Prorokuj wskaże.  
Ten rok to pewnie.  
No właśnie, czyli ona analizuje wszystkie dane distinct tem i na tej podstawie tworzy, a nie bierze źródło jako właśnie jakiś.  
Jakąś listę tak, która była? Nie wiem. Rejestrem jest to użytkowników czy coś w tym stylu, tylko bierze zakres danych, które ma.  
No nie jest to docelowe, ale już jakieś połowiczne rozwiązanie jest tak.  
Na teraz co mogło włączyć po prostu, a teraz możemy to tylko usprawnić.  
No wy klikanie takiego raportu to jest 2 minuty, więc doraźnie mogą to jakoś zaopiekować konsultanci czy tam serwisanci, a my pewnie musimy się pochylić nad tym jak to.  
Jak tu dodać pozycję?  
Że wyświetlaj wszystkie pozycje danego.  
Danej listy tak coś w tym stylu.

**Janusz Bossak** 28:15  
Jeszcze w ogóle brakuje jednej, którą normalnie.  
Wiem, że jest inny typ, bo ja tu sobie robię obok.

**Damian Kaminski** 28:25  
A jeszcze w międzyczasie, Piotr, ty sprawdziłeś te?  
Wczoraj te tą wigilię.

**Kamil Dubaniowski** 28:32  
Ja to testowałem jest ok i to.

**Piotr Buczkowski** 28:32  
Super.

**Damian Kaminski** 28:33  
A o k dobra, bo to o k.

**Piotr Buczkowski** 28:34  
Znaczy, ja ja sprawdziłem tylko w kodzie, że jest dwudziesty czwarty.

**Damian Kaminski** 28:38  
Tak tak, to Kamil miał Kamil miał testy.

**Kamil Dubaniowski** 28:39  
Ja sprawdziłem użytkowa.  
Bo jest kolejny przykład tego, że może nawet nie deweloper, ale serwisant czy wdrożeniowiec powinien być zobowiązany przygotować.  
Odtworzyć błąd na naszym środowisku.  
Bo nie.  
Było w zgłoszeniem napisane jak to zrobił, tylko że nie działa. Jak usiadłem do analizy, to wyszło, że nie wpisał regionu Polska dlatego mnie liczyło wigilii wolnym.

**Damian Kaminski** 29:06  
No właśnie i sprowadzamy to znowu do do kwestii tego testing.

**Piotr Buczkowski** 29:06  
No tak.

**Damian Kaminski** 29:11  
I według mnie nie tylko deweloperzy, ale to samo albo retro steps.  
Skoro jest przetestowane na środowisku, to proszę podać w retro steps Link do sprawy, która to testuje albo Link do widoku jakiegokolwiek słownika źródła gdzie ty to testowałeś?  
No bo ty musiałeś teraz wszedłbyś tam i byś to zrobił w minutę.

**Kamil Dubaniowski** 29:30  
Nie, nie odtwarzają błędów.  
W talii, a oni by może się też zagwarantowali jakby to przepisali, a tak to no większość wierzy klientom na słowo. Po prostu zgłaszam później ja to, czy ktokolwiek analizuje zgłoszenie, musi odtwarzać właśnie, bo oni nawet tego nie zrobili.

**Damian Kaminski** 29:35  
A robiłeś to po kolei sam?

**Kamil Dubaniowski** 29:49  
To zgłosili, jak klient zgłosił.

**Damian Kaminski** 29:54  
Dobra, co robimy z tym? Mamy tu ustalone, jak to robimy, co robimy, czy na razie doraźnie mówimy, że proszę się przesiąść na nowe raporty, co już częściowo wyeliminuje problem i problem będzie dotyczył tylko takich Bytów, które?  
Zakresie całych danych nie są zdefiniowane, ale no to podejrzewam, że eliminuje 90% problemów.

**Kamil Dubaniowski** 30:14  
Czy mi się wydaje, że na starych weź to przełóż na starych się moim zdaniem na starych zadziała identycznie.

**Janusz Bossak** 30:22  
Gram w tym.

**Damian Kaminski** 30:22  
Przełóż na stary już przekładam, poczekaj to wyłączę, żeby to już bym żeby miał na przyszłość jakiś tam przykład teraz na stare.

**Marek Dziakowski** 30:35  
Cześć.

**Damian Kaminski** 30:37  
Tylko widzisz, tu jest tu. Nie ma tego planowanie zasobów, tu jest gant.

**Kamil Dubaniowski** 30:41  
No tak, ale tam to gant jest po prostu.

**Damian Kaminski** 30:45  
O k.

**Janusz Bossak** 30:46  
Stary gant to jest obecny planowanie zasobów.

**Kamil Dubaniowski** 30:48  
Planowanie zasobów tak ano wygrał wcześniej funkcjonował.

**Damian Kaminski** 30:50  
O k dobra.  
Czyli tak data od.  
Nota do.  
No tu jest fajnie i powiem wam szczerze, bo tam musiałem szukać, a tu jest wygodnie, że od razu nie szuka tylko pól da towych szybciej to zrobiłem na starym.  
Kategoria, wnioskodawca.  
No są wszyscy.

**Kamil Dubaniowski** 31:27  
Na zapisz i zakończ edycję, bo to było też, że w zgłoszeniu.

**Damian Kaminski** 31:27  
Jest tak samo maszynę już mhm, dobra?  
Stary gant.  
Ciężko powiedzieć o co tu chodzi, ale wszystko czym. No jest inaczej. Tutaj jest Krzysztof górski, emil patyna, a tu jest Krzysztof górski Monika pie pruszyńska więc jest inaczej.

**Kamil Dubaniowski** 32:04  
Kamil skoczył dziś wyżej, jest też.

**Damian Kaminski** 32:07  
A m skoczył gdzieś wyszli.

**Kamil Dubaniowski** 32:08  
A nie ma wpisów na ten tydzień na ten rok.

**Damian Kaminski** 32:12  
W sensie?  
Tuma.

**Kamil Dubaniowski** 32:17  
Co ma, ale w tam dalej w 24 styczniem.

**Damian Kaminski** 32:18  
Też miał.  
A bezkitu nie ma, no ale w sensie no nie wiadomo trochę jak to działa. Kamil ma rację, że znaczy może mieć jakąś może sprawę, która ma początek. Nie ma końca, może być taki przypadek, że jest tu, bo coś jest zdefiniowane, ale nie umie tego wyrysować.

**Janusz Bossak** 32:20  
No tak, ale gdzieś mam wcale, że.  
Trzeba to rozkminić, to nie jest teraz chyba już poziom naradę według bo.  
Rozkminiamy a nie decydujemy tak rada ma decydować co zrobić.

**Damian Kaminski** 32:47  
Nie no to znaczy po prostu zalecenie powinno być takie doraźne, żeby zrobić to na nowych raportach, a.  
Niezależnie od tego, no to trzeba zaplanować, jak to powinno wyglądać, więc.  
Piotr zasugerował.  
Ale to trzeba rozpisać według mnie znowu na.  
No szeroki zakres, bo to są daty, użytkownicy, słowniki, rejestry. Pewnie coś jeszcze pytanie co?  
Kamila rozpiszesz.

**Kamil Dubaniowski** 33:26  
Do końca wiem.  
To na co się umówiliśmy?  
Rozumiem, że robimy tylko w nowym, robimy tylko na określonych typach pól, które są jakby limitowane i nie pochodzą z definition, czyli mamy do nich dostęp właśnie z poziomu słowników czy z poziomu rejestru, czy też rejestr powstanie to jest definition, jest to jest definition, więc pytanie czy rejestr też odnośnie kasy?

**Damian Kaminski** 33:47  
Które są jakimiś odnośnikami tak ogólnie mówiąc.

**Janusz Bossak** 33:55  
No ale co, jeżeli Słownik na 100000 funny?  
Albo rejestr ma 100000. To co mamy wszystkie wyświetlać? Znaczy nie podoba mi się ten pomysł. W końcu w ogólności słuszne, ale też w ogólności trudny do zrealizowania, bo zaraz się okaże, że to nie to ograniczajmy jednak z tego słownika, że nie chodzi nam o te 100000 pozycji, tylko o wybrane, nie żeby i tak dalej. No więc nie, nie podoba mi się.  
A to przemyśleć według mnie jeszcze bardzo tak głęboko, że tak powiem, chcą obejść źródłem.  
Tej informacji.  
Jakie są tego konsekwencje później?

**Damian Kaminski** 34:38  
No temat jest.  
Wielowątkowy.

**Janusz Bossak** 34:42  
No dokładnie.  
To nie jest prosta taka zmiana, że ja to dajmy tam niech się bierze to ze słownika nie.

**Damian Kaminski** 34:49  
No wielowątkowej trochę może nie teraz wpisuje się w nasze bieżące potrzeby, więc no pytanie co z nim w ogóle robimy?

**Janusz Bossak** 34:54  
Dokładnie.  
Od wieszamy na kołek.

**Damian Kaminski** 35:00  
Zajmujemy zdrady.

**Kamil Dubaniowski** 35:04  
Czy jak to zrobimy? No to będzie wisiał kolejne 2 lata.

**Janusz Bossak** 35:07  
No to.

**Damian Kaminski** 35:08  
No to będzie, no póki ktoś powie wykładam kasę i róbcie.

**Janusz Bossak** 35:15  
Jeżeli to nie jest błąd w rozumieniu działało inaczej, teraz działa inaczej.

**Damian Kaminski** 35:22  
No to po prostu mamy inne priorytety.

**Janusz Bossak** 35:24  
Mamy inne priorytety, dokładnie, no zajmujemy się tym.

**Kamil Dubaniowski** 35:27  
Czy no jest tak typu?

**Damian Kaminski** 35:27  
Według mnie da im sugestie, że zróbcie po nowemu i częściowo to wyeliminuje wasz problem dalej będzie tak, że byt, którego nie ma w źródle, ogólnie nie będzie się wyświetlał.

**Kamil Dubaniowski** 35:39  
To tego nie zrobią, po prostu nadal będą na podpisywali te filtry były w konfigu.  
I.

**Janusz Bossak** 35:45  
Czy to jest właśnie nadpisywanie filtry w łeb?

**Damian Kaminski** 35:46  
Jak to?

**Kamil Dubaniowski** 35:47  
No zobaczcie sobie ustawię w opisie jak oni to robią aktualnie.

**Piotr Buczkowski** 35:52  
Ale w konfigu.

**Kamil Dubaniowski** 35:53  
Znaczy nie wiem, czy w konfliktu akurat tym wpływa, ale.

**Damian Kaminski** 35:55  
Aktualnie aktualizacja polega na.  
Ścieżki em scripps Object and Report, gant tunes, JS.

**Kamil Dubaniowski** 36:05  
To nie w końcu.

**Damian Kaminski** 36:07  
No dobra, tylko co oni dzięki temu osiągają, że.

**Kamil Dubaniowski** 36:09  
Mają tak jak działało to po staremu, czyli ładuje wszystkie, nieważne czy to jest Słownik, tekst czy cokolwiek po prostu ładuje im na tej instalacji. Postaram mu tak jak działał wcześniej.

**Damian Kaminski** 36:18  
Ale wszystkie ze źródła czyli.

**Kamil Dubaniowski** 36:21  
Nie wszystkie wszystkie.

**Damian Kaminski** 36:22  
A skąd on wiedział wszystkich, jeśli to jest?

**Piotr Buczkowski** 36:26  
Znaczy dobrze inaczej, inaczej to wiem już jak to działa.

**Damian Kaminski** 36:26  
Wolę tekstowe.

**Piotr Buczkowski** 36:31  
W tym momencie on po prostu pobiera wszystkie sprawy.  
Nie nie tylko z tego okresu, który jest wybrany.  
Widoczny Przepraszam.

**Kamil Dubaniowski** 36:41  
Dzięki temu ma dostęp do wszystkich.

**Piotr Buczkowski** 36:43  
I.

**Damian Kaminski** 36:43  
Nie to też nie do wszystkich, bo jeśli nie będzie sprawy dla danego.

**Piotr Buczkowski** 36:46  
Do do do właśnie jeżeli lata nowego elementu nie będzie żadnej sprawy, nigdy nie było tego nie będzie.

**Damian Kaminski** 36:48  
No do tego zmierzam.  
No.

**Piotr Buczkowski** 36:55  
Ale to pewnie jest wystarczająco do wystarczająco dobre przybliżenie, tak?  
Że jeżeli stwo dodać nowy, które nie jest, nikt nie był nigdy wykorzystany, to muszą przynajmniej jedną sprawę dodać.

**Damian Kaminski** 37:07  
Do tego zmierzałem tak i teraz, ale.

**Piotr Buczkowski** 37:09  
Tylko to to to po to powodowało na przykład, że wykres urlopów wam wreszcie nie działo.  
Po prostu był za duży.

**Damian Kaminski** 37:17  
Mhm.

**Piotr Buczkowski** 37:17  
Gdzie były 1000 spraw? Tak czytam setki 1000 spraw.

**Damian Kaminski** 37:22  
Jak się ktoś co przeglądać wszystkich tak po prostu.

**Piotr Buczkowski** 37:26  
No bo on pobierał tak wszystkie.

**Damian Kaminski** 37:28  
No dobrze, no to w takim razie.

**Piotr Buczkowski** 37:29  
Sprawy z całego od całych 10 lat. Tak?

**Damian Kaminski** 37:34  
Tak, ale to jak rozumiem my to co oni robią moglibyśmy wrzucić pod już pokazuje tutaj.  
Żeby zrobić łatwą poprawkę tutaj można ograniczyć.  
A tutaj musielibyśmy wprowadzić, że pobieraj dane bez ograniczenia danych ze źródła, tak.  
Pobieraj dane do wierszy bez ograniczenia danych ze źródła, więc jak tu wprowadzę, że jest?  
Data utworzenia.

**Piotr Buczkowski** 38:08  
Znaczy ta data od data od data do to wygląda wynika z bieżącego widoku. Tak?

**Damian Kaminski** 38:08  
Tylko z tego.  
Nie właśnie nie na nowych, nie?  
No właśnie nie, więc może tylko to wystarczy, że zastosują nowe, no patrz.

**Piotr Buczkowski** 38:19  
Nie jest, nie, nie jest tak, to bardzo, to bardzo źle jest.

**Damian Kaminski** 38:24  
Dlaczego?  
Właśnie jest tak jak chce klient tam.

**Piotr Buczkowski** 38:27  
Czyli co?  
Czyli popieracie wszystkie sprawy z całego okresu działalności firmy?

**Anna Skupinska** 38:34  
Nie, to zależy o co w filtrów można ustalić na filtry, że który chce się nie.

**Damian Kaminski** 38:36  
Tak.  
No czyli tak, czyli tak jak nie ustawisz filtrów to tak jak powiedziałeś Piotr.

**Anna Skupinska** 38:43  
I oczywiście też. Yy też też źródła danych, jeżeli jest jakiś proces, tylko z tego procesu pobieramy dane.

**Piotr Buczkowski** 38:45  
No to czy pobieracie sprawy z 5 lat? Powiedzmy, bo.

**Damian Kaminski** 38:48  
Tak.

**Janusz Bossak** 38:49  
Jeżeli ktoś nie ustawił filtru, że ma być o za rok 2023, 4 i 5, no to pobierane są za wszystkie. No jak ustawił filtr od 2023 do 2025?

**Piotr Buczkowski** 38:59  
No ale to znaczy, że raport z urlopów, a wreszcie nie będzie działać.

**Janusz Bossak** 39:04  
Wystarczy pokazać, że ma pokazywać za rok 2025.

**Piotr Buczkowski** 39:07  
Wreszcie jest 50000 użytkowników.

**Damian Kaminski** 39:11  
No dobrze, ale to można wprowadzić inny filtr. Pokazuj tylko po 2 bezpośrednich podwładnych tak albo ludzi z konkretnego działu. Może być to filtr wymagany, trzeba wybrać dział, żeby ograniczyć zakres, więc mamy też do tego narzędzia.

**Janusz Bossak** 39:11  
No ale.  
Będzie to.  
Ja naprawdę szczerze mówiąc nie do końca jakby.

**Damian Kaminski** 39:30  
Znaczy, według mnie to, co mamy teraz możliwe, że rozwiąże problem?

**Janusz Bossak** 39:32  
Problem.

**Piotr Buczkowski** 39:33  
Tak, to będzie, to będzie nie to będzie niewydaje rozwiąże problem będzie niewydajny.

**Janusz Bossak** 39:41  
Tak znaczy, ja akurat jest z tego co mówicie, to też się nie zgadzam na takie rozwiązanie.  
Znaczy to, co tam ci konsultanci robią, to był jakiś aneks spekta twitter.  
Trochę.

**Damian Kaminski** 39:57  
Nie, nie, to niekoniecznie, nie wiadomo, czy to robią konsultanci, czy oni sami to wymyślił.  
Kto to kto to wymyślił nie wiadomo czy to konsultant robi czy czy beetsma to sobie sama robi.  
Może to?

**Kamil Dubaniowski** 40:09  
Spodziewam się, że wątpię, żeby sami na to wpadli. To musiał ktoś im odpowiedzieć.

**Janusz Bossak** 40:16  
Ale to jest pomijanie w ogóle, nie jak klient sobie może zamieniać biblioteki i używać jakiejś innej biblioteki z innej ścieżki.

**Piotr Buczkowski** 40:27  
Nie tam jest.  
Chodziło o usunięcie tego filtra domyślnego? Tak?

**Janusz Bossak** 40:38  
Nie wiem, nie rozumiem tego.

**Damian Kaminski** 40:38  
Dobre, bo.

**Piotr Buczkowski** 40:38  
Naszej.

**Damian Kaminski** 40:43  
Znaczy, słuchajcie, klient robi coś, czego efektem jest to, jak działają nowe raporty, a my się nad tym zastanawiamy, czy jest dobrze czy źle, czy będzie wydajnie, czy nie wydajnie.  
Zamknąłbym to odpowiedział, proszę korzystać z nowych raportów, nie trzeba robić tej poprawki. Macie tak jak chcieliście.

**Piotr Buczkowski** 41:00  
Około pytanie, czy czy czy zaraz tego nie zrobimy w nowych raportach, bo okaże się, że.

**Damian Kaminski** 41:01  
A to czy?

**Piotr Buczkowski** 41:06  
Yy, w rzeczywistych przykładach to jest nie nieużywane.

**Damian Kaminski** 41:11  
O k no dobrze to jest słuszny argument, no to może?

**Kamil Dubaniowski** 41:19  
Czyli rozumiem, że nowy moduł działał posterunku? Tak?

**Damian Kaminski** 41:19  
No ograniczając to powinniśmy wtedy zaopiekować to kompleksowo, czyli jeśli chcemy ograniczyć, to powinniśmy wtedy budować tą listę w jakiś sposób.  
Najbardziej optymalne, a nie tylko kliknąć ograniczenie tak i to by było wynik. Zadanie wynikające z tej potrzeby z ograniczenia, bo bo się dany nie ładują.

**Piotr Buczkowski** 41:32  
No tak.  
Tak.

**Damian Kaminski** 41:44  
Dobra, według mnie po prostu na teraz korzystajcie z tego i temat mamy zamknięty, niemniej trzeba go zaplanować.  
Jesteśmy te.

**Kamil Dubaniowski** 42:04  
Jesteś mamą?

**Anna Skupinska** 42:06  
Wszyscy przerwało.

**Janusz Bossak** 42:08  
Grałem.

**Kamil Dubaniowski** 42:08  
Zaczął pisać ten.

**Janusz Bossak** 42:11  
Prosiły Marka o dołączenie, bo Marek ma jakiś temat strat. Senter też pilnie omówienie.

**Damian Kaminski** 42:18  
To proszę.

**Marek Dziakowski** 42:19  
Tak, czy ktoś pamięta, dlaczego było takie założenie z dziobami w presenter, żeby działały niektóre działały tylko w nocy.  
Czy to wynikało z czegoś?

**Piotr Buczkowski** 42:32  
To ja jakie torby?

**Marek Dziakowski** 42:35  
No na przykład aktualnie znaczy chodzi o ten background, workery. Aktualnie wyszedł problem, że brakuje nam miejsca w hot storage, bo po prostu jest duży przemiał dokumentu i z tego, co się udało ustalić, no to po prostu ten job nie wyrabia, on tam przerabia.

**Piotr Buczkowski** 42:35  
Jakie trzeba by transfer?

**Damian Kaminski** 42:50  
Mhm.

**Marek Dziakowski** 42:56  
A po 25 dokumentów ciągu?  
Tam jednego uruchomienia uruchamia się.

**Damian Kaminski** 43:01  
Chodzi o to, żeby słabo ować tak schot na na bloba.

**Piotr Buczkowski** 43:02  
A czyli czy czyli?

**Marek Dziakowski** 43:05  
Usunąć shot storage.  
Fizycznie, żeby tam ich nie było, nie stopować.

**Piotr Buczkowski** 43:08  
No to to to.

**Damian Kaminski** 43:11  
O k.

**Piotr Buczkowski** 43:11  
To takie było złożenie, że raz dziennie tak po co więcej one być może są mało przerabia na raz.

**Marek Dziakowski** 43:16  
To nawet nie raz dziennie, bo on się tam wykonuje, powiedzmy 10 razy na godzinę w nocy, no ale to nie wyrabia się teraz już aktualnie.

**Piotr Buczkowski** 43:25  
No to trzeba zwiększyć mu paczkę do robienia.

**Damian Kaminski** 43:27  
Ale nie wyrabia w czasie czy po prostu ma z założenia za mało wolumen na jedną wywołanie.

**Marek Dziakowski** 43:34  
Nie wyrabia się w ciągu nocy, aktualnie wisi tą no bardzo dużo tych dokumentów bardzo, bardzo, bardzo dużo.

**Piotr Buczkowski** 43:39  
To albo mówię, że po 25 robi tak.

**Damian Kaminski** 43:41  
No właśnie do tego zmierzam. No i 25 robi w 10 sekund, wywołujemy go. Nie wiem. 5 razy czy 20 wką ciągu nocy, to trzeba może robić 100 albo 150 za jednym wywołaniem.

**Marek Dziakowski** 43:41  
Tak, tak, tak, no tak, tak, tak.  
No właśnie.  
O k. Czyli nie było jakiegoś takiego dodatkowego założenia, ze względów nie wiem na na żura czy coś nie kojarzy.

**Piotr Buczkowski** 43:57  
Dziwię się, że znaczy jest też taki podobny drop wam o diecie tylko nie robi 25, tylko robi 1000.

**Marek Dziakowski** 44:03  
Mhm.  
W ciągu jednego wykonania tak, a on chodzi w nocy czy chodzić sobie cały czas dobra, no to zrobię poprawkę, znaczy zrobię specjalne ustawienie, bo tam on korzysta z takiego ogólnego tego zakresu ilości.

**Piotr Buczkowski** 44:08  
Tak.  
Turcy nocy.  
Znaczy on dobrze inaczej.  
No nie robi 1000, on robi w paczkach po ileś, dopóki się nie nie zrobię wszystkiego.

**Marek Dziakowski** 44:29  
No właśnie tutaj jak nie zrobi no to czeka do kolejnej nocy po prostu.

**Piotr Buczkowski** 44:33  
No to świat został przemyślany.

**Janusz Bossak** 44:35  
No tak, bo tam, a teraz zaczynają nam wrzucać. Wiecie, po parę 1000 dziennie, nie.

**Damian Kaminski** 44:40  
No i 10000 tam wrzucił rosłon.

**Marek Dziakowski** 44:43  
Tak jednak.

**Janusz Bossak** 44:44  
Jeden dzień.

**Damian Kaminski** 44:45  
No to po prostu trzeba zwiększyć ten wolumen. No jeśli ten job po prostu robi, ale on nic tam nie obciąża sobie robi, bo taki był wcześniej wolumen to chyba najprostsze zwiększenie 25. Nie wiem na na 200 i.  
I sam się problem rozwiąże, tak.

**Marek Dziakowski** 44:59  
Mm no tak, w zasadzie tak zastanawiam się.  
Czy gdzieś tam w przyszłości nie lepiej byłoby w ogóle te czopy przerobić trochę, bo aktualnie?

**Piotr Buczkowski** 45:10  
To znaczy, jeżeli albo przerabia już robisz ten jobe w oddzielnym, tak to wszystko wszystkie takie joby przenieść do tego.

**Marek Dziakowski** 45:13  
Tak.  
Teraz.  
Wszystkie żeby przenosić. No właśnie tak też tak uważam, że tak powiem, bo aktualnie to niby to działa na 2 serwerach, ale tak naprawdę i działa i tak tylko jeden.

**Piotr Buczkowski** 45:18  
Tak wszystko.  
Nie, nie wiem dlaczego to nie wiem dlaczego to zostało zrobione w tym.  
Procesie webowym a niepodzielnym samowicie jest codzienny proces, do tego dzienna usługa tak powinno to być zrobione początku.  
I dodawanie do Polak chaina i to i inne rzeczy.

**Marek Dziakowski** 45:42  
Dobry.  
No to teraz też pytanie do Janusza no czy czy idziemy w to? No bo to będzie praca, no trochę tego będzie.

**Piotr Buczkowski** 45:52  
Musimy iść w to.

**Janusz Bossak** 45:54  
Przyjmijmy musimy, no niestety.

**Damian Kaminski** 45:55  
No dobra, tylko, no wiecie, to możemy jakoś podzielić. W sensie nie musimy być 0 1 kowi musimy iść w to pytanie teraz na ile jest to krytyczne, jak szybko musimy to zrobić.

**Marek Dziakowski** 45:55  
Rozmawiałem.

**Piotr Buczkowski** 46:04  
Jest po pierwsze, musimy przenieś.

**Marek Dziakowski** 46:05  
Bardzo krytyczne.

**Piotr Buczkowski** 46:09  
Dodawanie do blockchaina jak przeniesiemy do dokonywania do blockchaina do usługi czy tam do tego serwisu, czy jak się tam nazywa.

**Marek Dziakowski** 46:15  
Mhm.

**Piotr Buczkowski** 46:17  
Zainstalujemy to będzie działać przez zaczniemy przenosić. Musimy zacząć przenosić kolejne rzeczy.

**Janusz Bossak** 46:23  
Dogodny.

**Damian Kaminski** 46:24  
Ja tego nie podważam, tylko słuchajcie, zmierzam do tego, czy możemy na przykład ustalić tak, że w ramach sprintu Marek pracuje tydzień nad tras Center tydzień nad zadaniami, które tutaj są priorytetem i wtedy robimy to, powiedzmy 2 razy dłużej, ale to akceptujemy, bo no nie są to ryzyka krytyczne, ale są to usprawniające prace. Tak.

**Janusz Bossak** 46:43  
Krytycznym to są krytyczne.

**Piotr Buczkowski** 46:45  
Krytyczne, bo przestanie działać teraz Center.

**Janusz Bossak** 46:48  
Są krytyczne Damian.

**Damian Kaminski** 46:48  
Ale no o k. To dlatego zadaję to pytanie, ja nie mówię, że tak musi być ja tylko.

**Janusz Bossak** 46:51  
Siemka. Zastanawiam czy nie dać Marka jeszcze kogoś, żeby to przyspieszyć.

**Damian Kaminski** 46:55  
O k.

**Janusz Bossak** 46:55  
To syntetyczne to są takie, że jak się to ********** albo się zatka i zabraknie miejsca i przez tam wiesz taki rossman czy adecco wrzuci kolejne parę 1000 dokumentów. No i co będziemy kwiczeć tak.

**Marek Dziakowski** 47:07  
Nie no tu zawsze jest opcja skalowania, tylko, że to wiąże się z kosztami po prostu, bo można choć story skalować do góry ten to przestrzeń, ale znaczy będziemy płacić.

**Piotr Buczkowski** 47:16  
No a w dół, ale w dół się chyba nie da.

**Marek Dziakowski** 47:18  
Nie wiem tego.  
Nie, nie wiem, nie wiem.

**Piotr Buczkowski** 47:22  
To raczej jest ten problem, że się chyba rzadko kiedy duda tak.

**Marek Dziakowski** 47:25  
Tak no to możliwe, no to możliwe.

**Janusz Bossak** 47:26  
Dobra, spróbuj, to znaczy ja uważam tak to co robisz, mam z tym blockchainem to jest absolutny must have, a tutaj według mnie bez razie przerabiania tego tak jak Piotr powiedział tam przerzucania w inne miejsce, żeby to się działo, to po prostu zwiększyć ten limit. Tak z tych 25 na dowolną większą liczbę 500 czy ileś tam i niech on posprząta trochę tak, a potem dopiero w następnym jakimś cyklu się zajmiemy tym, żeby ten job tam przenieść to, co mówi Piotr w innym miejscu.

**Marek Dziakowski** 47:54  
Dobra, to ja dorobię ustawienie i zjem.  
Ilość tych dokumentów przegramy.

**Janusz Bossak** 48:02  
I niech on tam posprząta, żeby nie było tam w tym hot story, stylu dokumentów.

**Marek Dziakowski** 48:07  
Dobra.

**Janusz Bossak** 48:09  
Znaczy druga rzecz tą jak ktoś rzuca 10000, no to te dokumenty też czekają w tym historyczny dzień 2 3 na nim ktoś tam odpiszą, nie.

**Piotr Buczkowski** 48:16  
No nie.

**Marek Dziakowski** 48:17  
Miesiąc ciekawią.

**Piotr Buczkowski** 48:17  
Ale takie za takie jest, tak takie jest założenie tak, że na czas obsługi te komentów są one w historycznych, tak.

**Damian Kaminski** 48:25  
Tak.

**Marek Dziakowski** 48:26  
Najwyższą tam miesiąc aktualnie.

**Piotr Buczkowski** 48:28  
No.

**Janusz Bossak** 48:29  
Ale właśnie pytanie, czy wiszą miesiąc czy jeżeli po 2 dniach zostały już podpisane, to nadal wiszą w pod story?

**Marek Dziakowski** 48:35  
Wydaje mi się, że.

**Damian Kaminski** 48:35  
Bo jeszcze ktoś nie może pobrać o to chodzi.

**Piotr Buczkowski** 48:35  
No zakładamy, że jeszcze przez kilka dni ktoś tam będzie pobierał, sprawdzał coś.  
To, żeby nie sięgać do tego cold cold Store czy bloba.

**Marek Dziakowski** 48:44  
Bloba.

**Piotr Buczkowski** 48:47  
To co jeszcze podstaw być podobna zasada jest mama dzieci.

**Damian Kaminski** 48:52  
Tak tutaj były nad tym dywagacje w na początku roku, że to pobranie z col de też kosztuje tyle samo co ty, utrzymanie jakieś tam były.

**Janusz Bossak** 48:52  
No taki balans między tym.  
No no no no no.

**Piotr Buczkowski** 49:01  
Tak, bo kot teoretyczny jest taniej, jeżeli tam wrzucić coś i zapominasz o tym.

**Damian Kaminski** 49:06  
No.

**Marek Dziakowski** 49:07  
Mhm.

**Piotr Buczkowski** 49:07  
A jeżeli cały czas sięgasz po tym to to wychodzi drożej niż od stolicy, bo pobranie jest drogie.

**Damian Kaminski** 49:13  
Tak.

**Janusz Bossak** 49:14  
Ano rozumiem, dobra.

**Piotr Buczkowski** 49:16  
Dlatego na czas takiej obsługi jest hot stories, tak?  
Czas tych kilku tygodni po wrzuceniu.

**Damian Kaminski** 49:22  
Ale to też według mnie nie powinniśmy o tym zapomnieć. Tylko może pytanie, czy mamy do tego jakieś statystyki, czy przy jeden te przez nas założenia 30 dni są zgodne z realiami? Czy my mamy na przykład informacje?  
Takie ostatnie logowanie do dokumentu względem ostatniego podpisania. Ostatnie pobranie dokumentach dokumentu względem ostatniego podpisania, czyli mamy datę ostatniego podpisania ostatniego pobrania i ostatniego zajrzenia. Jeśli z tego sobie mamy listę wszystkich i odetniemy, gdzie jest różnica większa niż powiedzmy 30 dni, to się okaże, że różnica większa niż 30 dni to jest 1%. A jak odetniemy różnica większa niż 14 dni, to się okaże, że to jest raptem 5%.  
Więc może z tych 30 jeszcze możemy zejść na na 14, bo mało kto z tego korzysta?

**Piotr Buczkowski** 50:13  
Tak warto to byłoby sprawdzić, ale zacznijmy od najważniejszej oczy.

**Damian Kaminski** 50:18  
Nie no spoko, to markowi wrzucam gdzieś tam kiedyś sobie o tym przypomni, bo to też może gdzieś tam wpływać na na optymalnych kosztów nie.

**Piotr Buczkowski** 50:27  
No tak.

**Janusz Bossak** 50:35  
No.

**Damian Kaminski** 50:37  
No dobrze, to pozostaje, tylko chyba to, żeby smarków w miarę możliwości opisywał to co robisz tak, żebyśmy nie mieli sytuacji takiej jak z Rafałem, że.  
Jak to zmieniasz to nie wiem, może skonsultuj to jeszcze z Piotr? Opisz to powiedz tak jak wcześniej tutaj skonsultuj to z Piotrem. Jeśli uważasz, że to stosowne i żeby pod to były jakieś PI, potem może na ich podstawie będzie można zrobić jakieś aktualizacje do dokumentacji.

**Janusz Bossak** 51:06  
W zasadzie w ogóle nie powinniśmy o takich rzeczach nawet rozmawiać. Znaczy pb i jest absolutnym must have jeżeli coś robimy.  
Znaczy, według mnie powinien być praktycznie zakaz, to przez deweloperów robienia czegokolwiek jeżeli nie ma PA ja i to nie PA ja w postaci tytułu.  
A opis brzmi jak w tytule.  
To jest do niczego PI.  
Jeżeli nie chce się wam pisać, to wejście tego tą sztuczną inteligencję napiszcie 2 zdaniach ona wam rozbuduje to.

**Damian Kaminski** 51:40  
Mhm.

**Janusz Bossak** 51:41  
Potrzebnego pb i naprawdę zacznijmy to robić, po prostu będziemy mieli łatwiej w przyszłości właśnie łatwiej testować, łatwiej pisać, łatwiej robić dokumentację i tak dalej i tak dalej po prostu.

**Damian Kaminski** 51:53  
I będziemy lepiej robić, bo jak coś próbujemy opisać.  
To za automatu rozpoczynamy jakiś tok myślowy i się okazuje, że czegoś nie przemyśleliśmy, a jak robimy to dochodzimy do tego punktu. Dopiero jak coś zrobimy ten pierwszy element.

**Janusz Bossak** 52:07  
Ja muszę poprosić o zbadanie, jakby nie wiem warunków brzegowych, no różne rzeczy można tak no i nie zawsze on wymyśli dobrze, ale.  
Coś tam podpowie, więc ja nie twierdzę, że to ma być takie Zero jedynkowe wrzuć do ja wszystko dobrze zrobi, nie to ma być.  
Taki drugi kolega z którym się gada nie zawsze mówi mądrze, ale może czasami coś podpowie tak no i po prostu bierzemy i rozbudowujemy, a to co na pewno umie robić to ładnie to ubrać w słowa tak i napisać.  
I kryteria akceptacji może rozbudować i tak dalej, więc im więcej będziemy mieli dobrego tekstu, tym lepiej.

**Damian Kaminski** 52:47  
No to sugestia marku, według mnie powinieneś założyć sobie fitter o nazwie przeniesienie zadań cyklicznych do usługi i pod to podpisuje kolejne PI dla tych kolejnych powiedzmy zadań, które robisz.

**Marek Dziakowski** 53:01  
Dobra dobra, no na razie blockchain jest priorytetem, ale rozumiem, że w kolejnych sprintach dalej kolejne.

**Janusz Bossak** 53:08  
Tak.

**Marek Dziakowski** 53:09  
Ceny priorytetów Racing pokoleń.

**Janusz Bossak** 53:11  
Dokładnie.

**Marek Dziakowski** 53:12  
Dobra.

**Janusz Bossak** 53:16  
Ja muszę uciekać, bo mam inne spotkanie dzięki barki.

**Damian Kaminski** 53:20  
No dobra, no i ja tutaj tylko zanotowałem, że.  
Nowe raporty nie wymagają tych poprawek i co w przyszłości trzeba z tym zrobić i nie wiem odpinam to chyba od rady.  
I tyle.  
Nie wiem, czy przechodzimy jeszcze przez jakiekolwiek inne zadania, czy.  
Kończymy.

**Piotr Buczkowski** 53:45  
Chciałabym kończy.

**Damian Kaminski** 53:45  
Nauki.  
Nauka z jedynką.  
To jest u mnie.  
To chyba już niepotrzebnie jest na razie, ale przejrzę to sobie szuflade nowo dobra to kończymy.

**Marek Dziakowski** 54:01  
Jeśli do usłyszenia cześć.

**Damian Kaminski** 54:01  
Na razie.  
Cześć.

**Anna Skupinska** 54:05  
No cześć.

**Janusz Bossak** zatrzymano transkrypcję
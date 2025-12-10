**Data spotkania:** 3 grudnia 2025, 08:19 - część 6

---

**Janusz Bossak:** No to jest już mniej, to jest tylko kwestia czytelności, tak.

**Damian Kamiński:** Tak, to już jest kwestia, że to nie przeszkadza, nie blokuje procesu, nie.

**Janusz Bossak:** Jeżeli, jeżeli tak, nawet jeżeli tam jest jakieś zgoda RODO AP2, to.

**Damian Kamiński:** Jeszcze zobaczmy, co się dzieje, bo oni często wypełniają, tak, czy tutaj też to widać i jak to w ogóle się tu wtedy wyświetla. No tu się wyświetla git, tylko ten. To trzeba też. Na to nie było zgłoszenie. Tego nie było chyba.

**Łukasz Bott:** Dowiemy szybko decyzja.

**Damian Kamiński:** No już jest udrożnione.

**Łukasz Bott:** Jeżeli czekaj, czekaj, jeżeli jest, jeżeli to, czyli udrożniłbyś tak w tym sensie?

**Janusz Bossak:** Znaczy już jest poprawiony.

**Damian Kamiński:** Tak, już tylko teraz. No jeszcze mogą. Potencjalnie tu widzę, że na telefonach skasować. Wiesz, więc patrzę, czy to jest w edycji. Tylko to zrobiłem. Dobra, zrobiłem to na dev, to jeszcze nie jest produkcja, ale no od czegoś trzeba zacząć.

**Łukasz Bott:** Nie.

**Michał Zwierzchowski:** Nadal są witryny 3: dev, pity i Adecco.

**Damian Kamiński:** Pity nie dotyczy, pity nie dotyczy. Tylko czy, pytanie, czemu na tylko odczycie można to?

**Łukasz Bott:** To pytanie, czy jaka decyzja, czy.

**Damian Kamiński:** Zrobić. No usunąłem niestety. Tak, czy nie jest to skuteczne? Raz przepraszam. No usunąłem, teraz się wyświetlają tylko nagłówki. No to to jest kolejny już hotfix. Czyli tabela jest w trybie formularza, jest ustawiona tylko do odczytu, a można usuwać wiersz. Nie wiem, czy dodawać.

**Łukasz Bott:** W trybie mobilnym.

**Damian Kamiński:** W trybie mobilnym. Dodać nie można, usunąć można. No to też jest do ukrycia CSS-em, no.

**Janusz Bossak:** Więcej, nie są. Ja bym szedł w kierunku cofnięcia tej wersji.

**Łukasz Bott:** Tak, cofnijmy.

**Michał Zwierzchowski:** Dobra, ja już napisałem na tą naszą grupę i ustalę tutaj z Danielem i z Łukaszem.

**Janusz Bossak:** Cofnijmy tą.

**Kamil Dubaniowski:** To w niedzie tej wersji, no to jest cofnięcie do marcowej.

**Michał Zwierzchowski:** Marcowej.

**Janusz Bossak:** No trudno.

**Kamil Dubaniowski:** Stary interfejs.

**Janusz Bossak:** No ale przecież wczoraj. Przegraliśmy, ale to.

**Kamil Dubaniowski:** O k.

**Janusz Bossak:** Przedwczoraj była inna.

**Damian Kamiński:** No tylko że wiecie, kurde.

**Michał Zwierzchowski:** No chyba.

**Damian Kamiński:** No to mega źle o nas świadczy. No pytanie, jaka to jest skala? No bo może tym CSS-em to wyprostujemy tutaj, jeśli to tylko ich dotyczy. Może poczekajmy jeszcze dzień na kolejne zgłoszenia.

**Michał Zwierzchowski:** No chyba, że będzie szybki hotfix i wieczorem wygramy.

**Damian Kamiński:** A tu faktycznie zaraz zrobimy to CSS-em.

**Janusz Bossak:** No to jeżeli się CSS-em to uda tak ponaprawiać, to o k, no. Liczba ważniejsze jest tego wniosek długofalowy. No to jest. Michał, to co ciągle tam gadamy, tak te testy tu end to end. Takie rzeczy u takich wrażliwych klientów, że to też jest tak, że dopóty, dopóki taki błąd nie wystąpi, to nie wiesz co testować, nie.

**Damian Kamiński:** No tak.

**Janusz Bossak:** Bo nie wiesz. Nie ma być tego. No albo wiesz, no to właśnie o to chodzi. Na przykład tego z ukryj, tak. To test powinien przechodzić, że jeżeli jesteś w trybie tam tylko do odczytu, to nie powinno być guzika usuń wiersz, nie. No i to taki test powinien być. No i teraz jakby się to zapuściło, to by przeszło tylko, że no pomóc nam obaj, tak, więc. To jest po prostu. Moja ocena tego, z Przemkiem rozmawiałem, oczywiście, on nie zgodził się na zatrudnienie kogoś do pisania tych testów end to end. To ja innych zrobi. Nie, no super.

**Michał Zwierzchowski:** No tak, no ja właśnie zacząłem przeglądać, jest na tym, jak testować jakiś tam kurs. Niby Playwright, Cypress i tam jakieś takie.

**Janusz Bossak:** Wiem. Ja też to robiłem, no i utknąłem, no bo to jest full-time job, no nawet z użyciem AI.

**Michał Zwierzchowski:** Oni tam widziałem to nawet, nawet oferują, jest mający lub ten kurs jest część darmowy, część płatna, ale widziałem, że jest jakaś tam część, że położeniu, w której też pomagają. No to tam kilkadziesiąt tysięcy chyba. Złotych.

**Janusz Bossak:** To na razie, no.

**Łukasz Bott:** W składzie, ale to tutaj.

**Janusz Bossak:** Dobra, no wróćmy do tematu, no.

**Łukasz Bott:** Ale tutaj jeszcze ja bym widział, jeżeli chodzi o testy, ale to od strony takiej organizacyjnej i u nas i z klientem. Znów podam przykład Deutsche Bank, tak? Tam poprzednia project managerka, która tam kierowała. Ja byłem z nią umówiony w ten sposób, że jak aktualizowaliśmy coś, to oczywiście pierwsze środowisko testowe. Tam mieliśmy czeklistę, tak, co ma działać po aktualizacji. Po tym się, jeżeli to działało, zielone światło szło na produkcję. Aktualizacja produkcji i na produkcji zaraz po tym aktualizacji trzeba było to samo czeklistę przejść. Jeżeli działało, to o k. Następny dzień support taki hotline, tak? Support, żeby jakby się coś działo, nie działało na produkcji po aktualizacji, cofamy do poprzedniej wersji i tyle, koniec. I dopóki nie zostanie naprawione.

**Janusz Bossak:** Co tam się tak?

**Łukasz Bott:** I tutaj nie wiem, może, że w tym Adecco.

**Janusz Bossak:** A to dobre.

**Łukasz Bott:** Może też trzeba tak zrobić taką procedurę zastosować. Skoro to jest zwłaszcza krytycznie jakiś tam proces, tak, czyli że. Aktualizujemy Adecco dev, skoro mamy takie środowisko i być może te procesy, sorry, ale to chwilę trwa, ale trzeba je przeklikać i zobaczyć, tak, czy działają. Jeżeli tak, to aktualizujemy produkcję. Jeżeli nie, no to nie ma zielonego światła na aktualizację produkcji i tyle.

**Damian Kamiński:** No już to, że ten ta kolumna też już jest usunięta. Ukryta, to jest na razie tylko u mnie tutaj lokalnie. No ale to teraz też mogę przekleić i to ukryć. No to tyle możemy zrobić na już, na teraz, na za 3 minuty.

**Michał Zwierzchowski:** Dobra, czyli.

**Damian Kamiński:** Wyświetlamy to i kasuję tą kolumnę i w zasadzie zakładam, że mają to udrożnione. Nie wiem, po prostu muszą to sprawdzić. Ale możemy zrobić to samo i na dev, i na i na produkcji, i na drzewiej. W międzyczasie wewnętrznie gdzieś to przetestować. Czy wszystko gra? Przejść cały proces, jeśli gra, no to tu jest udrożnione. Ja nie wiem, co się dzieje w innych klientów, nie, czy tam są takie przypadki, ale tutaj mielibyśmy to załatwione.

**Michał Zwierzchowski:** No bo ta wersja jest w tej chwili na wszystkich witrynach na chmurze, to 120.

**Damian Kamiński:** Jeszcze przeglądam tu inne. No wiem, wiem, że na wszystkich, tylko no pytanie, czy ktoś też w ten sposób z tego korzysta. Do tej pory, ale tu nie widzę innych artefaktów związanych z tym.

**Michał Zwierzchowski:** No tak, tak.

**Damian Kamiński:** Dobra, tu jest to samo.

**Michał Zwierzchowski:** Lubić to, co robimy. Systemem Adecco cofamy, zostawiamy, czekamy na poprawkę.

**Damian Kamiński:** No tu też jest źle, czekajcie. Aha, bo to jest drugie tylko pole. Dobra, to to też da się szybko ukryć. To jest.

**Janusz Bossak:** Według mnie cofamy, no według mnie cofamy, że to jest wczoraj była w nocy, dzisiaj jest pierwszy dzień, tak, czyli już zgłosili błąd, tak, czyli o dziewiątej się zorientowali, zgłosili błąd.

**Damian Kamiński:** Tutaj.

**Michał Zwierzchowski:** No tak, no wczoraj podziemia do nas, to jakoś aktualnie zobaczysz.

**Janusz Bossak:** A wczoraj o dziewiętnastej aktualizowaliśmy. Cofnijmy tą do wczoraj wersję. I te błędy poprawne i dopiero wtedy zrobimy, koniecznie, nie, bo to nie wiemy, gdzie jeszcze coś się sypnie, tak? A widać, że jest dużo tego.

**Damian Kamiński:** To nie poprawiać, mam tego, cofamy.

**Michał Zwierzchowski:** Dobra, to pierwszy. Dobra, podpiszę dodanie, no.

**Janusz Bossak:** No Damian, no jak uważasz, no.

**Damian Kamiński:** Nie, no o k, ale w sensie, ja wcale nie tutaj postuluję, że ja to będę poprawiał, bo tak jak mówisz, nie wiem, co jeszcze i gdzie więcej, tylko pytanie, jak się dowiedzieć. Zrobimy to, żeby żeby tych iteracji tych nie było wiele.

**Janusz Bossak:** No to jest testować.

**Damian Kamiński:** Że to poprawimy, wydamy i zaraz znowu będziemy cofać. To najgorsze jest to, że to jest bardzo duża zmiana wizualna frontendu, nie tego pierwszego ekranu, że to widać.

**Łukasz Bott:** Damian, no ale to. Damian, ale podejrzewam, że to co pokazujesz, czyli Adecco, tak porąbany formularz jest w Adecco. Inni klienci. Myślę, że statystycznie nie korzystają z tak.

**Damian Kamiński:** Mhm.

**Łukasz Bott:** Mi się przypomniało w sensie będzie jeden tylko, bo Bondspot, Bondspot, ale na szczęście Bondspot ma u siebie i po drugie dawno nie aktualizował i oni tam.

**Damian Kamiński:** Zgadzam się z tobą, ale tego nie wiemy.

**Janusz Bossak:** A.

**Łukasz Bott:** Nie siedzę na tej wersji, jakiej siedzę.

**Janusz Bossak:** Michał, czym możemy wydzielić Adecco i samo Adecco cofnąć?

**Michał Zwierzchowski:** Tak.

**Janusz Bossak:** Co?

**Michał Zwierzchowski:** Tak, bo to są, bo są oddzielne witryny. 3 oddzielne dla Adecco i każda może mieć inną wersję.

**Damian Kamiński:** A. No to.

**Janusz Bossak:** No to cofnijmy Adecco. Cofajmy Adecco natychmiast.

**Łukasz Bott:** Tak.

**Kamil Dubaniowski:** Ale zostawcie na devie.

**Damian Kamiński:** Prod, dev, prod, def, trans. Pity są nieistotne, pity zaraz będą w styczniu.

**Janusz Bossak:** Nie, prod.

**Kamil Dubaniowski:** Zostawmy dev.

**Janusz Bossak:** Prod. Prod.

**Kamil Dubaniowski:** Pewnie możemy.

**Michał Zwierzchowski:** Możecie, możecie dołączyć Daniela na szybko do spotkania, żeby wiedział, bo ja mu napisałem, ale ta.

**Damian Kamiński:** No już.

**Michał Zwierzchowski:** Bo on tam stale z klientami, także.

**Kamil Dubaniowski:** Znaczy, ja bym zostawił, niech oni przejdą ścieżki, które są dla nich krytyczne i zrobimy takie testy. Robi na przykład aresztuj właśnie text. Łukasz też mówił, inni też tak prowadzą.

**Damian Kamiński:** Mhm.

**Janusz Bossak:** No. Niech, niech.

**Damian Kamiński:** Znaczy, konkluzja jest taka, że tutaj ten dev powinien być zaktualizowany do czerwcowej już dużo wcześniej i oni powinni przejść te testy wcześniej. Nie mielibyśmy sytuacji tak jak mamy.

**Daniel Reszka:** Cześć. Cześć, co tam?

**Janusz Bossak:** Znaczy, wiesz. No ale, no, no dokładnie, no tak powinno być. Czy ciągle nie, nie trzymamy się jakiś podstawowych procedur? No kurde, błąd.

**Daniel Reszka:** Adam, coś ustaliliście? Chyba.

**Michał Zwierzchowski:** Cześć, jestem.

**Daniel Reszka:** Co się dzieje, bo jestem w trakcie coś.

**Janusz Bossak:** Adecco się zbzikało.

**Damian Kamiński:** Ee.

**Daniel Reszka:** No i czyli to jest jednak błąd, tak?

**Damian Kamiński:** [kontynuacja rozmowy]


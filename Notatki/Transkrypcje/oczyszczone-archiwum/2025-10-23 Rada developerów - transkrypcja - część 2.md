**Data spotkania:** 23 października 2025, 08:02 - część 2

---

**Anna Skupinska:** Tego się nie spodziewał.

**Piotr Buczkowski:** Ustawienia eksportu.

**Damian Kaminski:** 2, czy jeden mogę zaznaczyć?

**Piotr Buczkowski:** Zaznaczyła. A to tak, bo – to nie wgraliśmy jego procesu, tak?

**Anna Skupinska:** A, czy on się wgrał tylko pod nazwą Empty? To jest ten proces. Ja też stworzyłam 2 sprawy, żeby było z czego generować.

**Piotr Buczkowski:** Dobrze, dobrze, wrócić do wyszukiwania, ustaw tam ustawienia eksportu.

**Anna Skupinska:** Tak i zapisz, wyjdź.

**Piotr Buczkowski:** CSV.

**Anna Skupinska:** A, to się tutaj – jest wyłącz. To nie jest to, to nic, to nie zmieni, że będzie trzeba samemu zmienić nazwę pliku, znaczy rozszerzenie pliku.

**Damian Kaminski:** No, no to...

**Piotr Buczkowski:** No teraz pobierz, pobierz.

**Anna Skupinska:** Widzę, że jest ponad 2.

**Piotr Buczkowski:** Pole XSLT.

**Damian Kaminski:** XML.

**Anna Skupinska:** No i teraz musisz tylko zmienić nazwę z XLS na CSV.

**Piotr Buczkowski:** Zachowaj.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Otwórz folder. I weź w notatniku odpal.

**Damian Kaminski:** Zmieniać, czy w notatniku odpalić?

**Anna Skupinska:** Tak, w notatniku. Można się dobrze przeczytać. Bo jak pamiętam, ten szablon to po prostu...

**Piotr Buczkowski:** Potem jeszcze skanuje ten plik.

**Damian Kaminski:** Nie wiem, ale coś mi się zawiesiło. Poczekaj sekundkę, na drugim ekranie – o, już, już jest, już jest.

**Piotr Buczkowski:** No bo jest tam jeszcze nie...

**Damian Kaminski:** No, coś tam było chwilę widocznie. Dobrze jest.

**Anna Skupinska:** Tak, a – czy tak się pokazywało. Więc jak się przeczyta ten plik szablonu, to on po prostu wpisuje 3 wartości. Jak tam nie dawałam do tych 2 spraw wartości jednej.

**Piotr Buczkowski:** No i to był testowy plik Deutsche Banku, którym chcieli tam po prostu całe zestawienia generować. Taki test zrobiłem, także tak to można zrobić. Banku nie pamiętam już, kurczę – może nie, Deutsche Banku. No w każdym razie chodzi o to, że może być...

**Damian Kaminski:** Dobrze.

**Piotr Buczkowski:** Co tam, tych, co tam chcesz, tak?

**Damian Kaminski:** To teraz wiemy jak to działa, tak? Zakładam wiemy, że – no właśnie – trzeba do tego zrobić kilka rzeczy, czyli najpierw trzeba dołożyć tutaj w ramach definicji szablonów rozszerzenie, żeby to już dobrze działało po nowemu. Ja bym chciał też informacje – jak ty, Aniu, widzisz to z poziomu... Nie wiem, technicznie – jak ty to widzisz z poziomu?

**Anna Skupinska:** Mhm. Z poziomu backendu. Więc będę musiała zrobić tak, żeby on brał to zapytanie – tą definicję raportu – i brał sobie wszystkie CaseID, które jakby ten raport zwraca, i potem po prostu może je włożyć do starego kodu, bo stary kod po prostu używa jedynie szablonu, tego rozszerzenia i listy – lista spraw, z których ma zrobić ten raport – i po prostu wtedy mogę część kodu użyć. Nie będę musiała od nowa ich tworzyć.

**Damian Kaminski:** No dobrze, teraz pytanie w kontekście nowych raportów, bo tu trzeba przycisnąć jeden przycisk, potem drugi przycisk. Czy jesteśmy w stanie to jakoś zautomatyzować, żeby było mniej więcej analogicznie jak wywołanie?

**Anna Skupinska:** A, czy Krystyna to zaprojektowała? Możecie zobaczyć w zadaniu 19020 jest pokazane jak to Krystyna zaprojektowała. Ona tam wstawiła 2 obrazki. I tak, które zamierzam też zrobić. A, czy – tak, to jest jeden tutaj i tam – drugi. Jak właśnie analizowałam to, zauważyłam – czy na pewno to wybieranie formatu jest potrzebne?

**Damian Kaminski:** Dobra, ale to tak – eksport danych, czyli w ramach tego, że tu można eksportować, to jeszcze – pozwól – na eksport danych do szablony XSLT. Dobra, na razie powiedzmy, że tak.

**Anna Skupinska:** Dlatego to od nas...

**Damian Kaminski:** Tu już definiujemy tak, na tym poziomie konfiguracyjnym, jaki szablon, to będzie wynikowa, więc to w ogóle nie jest potrzebne. Akcja wykonywana po eksporcie, czyli reguła.

**Anna Skupinska:** I tak będę musiała jeszcze zmienić trochę – trochę zmienić GraphJSON, żeby można było zapisać informacje, które tutaj umieszczamy. No też, jeśli chodzi o backend, taka mała zmiana, no ale oczywiście będzie potrzebna.

**Damian Kaminski:** No dobrze, a to jest – w sensie można wiele szablonów zdefiniować?

**Anna Skupinska:** Nie, można na pewno tylko jeden, więc to powinno być tak, że jak wybierzesz szablon, to się to znika, ale wyżej.

**Damian Kaminski:** W tym polu. OK, dobrze.

**Anna Skupinska:** A może zrobić tak, że się wiesza i nie można nic z nim zrobić?

**Damian Kaminski:** No dobra, tylko – szczerze mówiąc – nie podoba mi się to, w sensie że to jest tu. Czy to nie mogłoby być tak jak akcje masowe?

**Anna Skupinska:** W sensie, że użytkownik zaznacza sprawy – a, czy to będzie podobne, ponieważ tak podobne do akcji masowych – użytkownik zaznacza sprawy, a potem wybiera eksportu według szablonu.

**Damian Kaminski:** Poczekaj, jak z tego wyjść? Nie da się stąd wyjść?

**Piotr Buczkowski:** No nie da się, bo został ukryty.

**Damian Kaminski:** Dobra.

**Piotr Buczkowski:** Nagłówek, który – żeby to wyświetlać w React, a tutaj jest problem czasami, że znika, tak.

**Damian Kaminski:** Mhm. Reguła, React... Czy to nie mogło być tak?

**Anna Skupinska:** A, czy – myślę, że się trochę ludziom z regułami miesza, ale możemy dać eksport do szablonu, na przykład tutaj obok, przycisk.

**Damian Kaminski:** No, bo wtedy jest jakaś zdarzeniowość – zaznaczam i coś wywołuję, a nie muszę gdzieś tam pamiętać, że tu jest. Mi się to w ogóle nie kojarzy z tym eksportem. Ten eksport to jest eksport danych, a ten eksport to jest eksport według mnie.

**Anna Skupinska:** Żeby w ten sam eksport, bo był w tym samym miejscu, gdzie są inne eksporty, więc taki jest plus tego podejścia. Wszystko – jeśli użytkownik wiedział, że ja chcę eksportować dane, to one są w tym miejscu – eksporty są w tym jednym miejscu.

**Damian Kaminski:** No niby tak, ale te checkboxy nie mają związku z tym eksportem.

**Anna Skupinska:** Mają.

**Damian Kaminski:** Jaki?

**Anna Skupinska:** A, przepraszam – tak, że boksy po lewej – tak, mają, bo zaznaczasz sprawy, które mają zostać wyeksportowane.

**Damian Kaminski:** Nie, nie – to ty teraz mówisz o tym co zrobisz, a ja mówię jak jest.

**Anna Skupinska:** A, w sensie załączniki – to a, faktycznie, tak.

**Damian Kaminski:** W sensie, że one się pojawiają. Zobacz, one się pojawiają tylko, jakie zaznaczone? Ty masowe tutaj.

**Anna Skupinska:** No tak, ale możemy zrobić, że się pojawiały też, jeżeli mamy eksport według szablonu – możemy też zrobić.

**Damian Kaminski:** Czyli jak teraz zapisze? No tak, tylko – no to według mnie jest większa niespójność, że jak ja zaznaczam jakiś checkbox, czyli mam – wróćmy do edycji. Włączmy sobie te akcje. Aha, to nie ma akurat. Czy jak włączę podpisywanie masowe, czy jak włączę akcje masowe? To za to pojawia mi się – to pojawiają mi się checkboxy zaznaczenia. Zaznaczenie checkboxa to ma takie następstwo, że pojawia się jakiś przycisk na dole, że – jak zaznaczyłem – to coś będę chciał z tym robić. Od razu mi się kojarzy gdzie ja mam dalej kliknąć. Jak to jest tu, to mi się nic nie kojarzy. W sensie, jak już wiem, to wiem. Zgadzam się, ale jak nie wiem – w sensie dzisiaj – ten eksport, nie wiem w ogóle co to tu jest. Znowu jakiś babol – co to jest? Z definicji tego tu nie powinno być.

**Anna Skupinska:** Myślę, że pojawią się z lewej strony, bo przy sprawie nie ma miejsca.

**Damian Kaminski:** Aha, załączniki. Nie, nie – dobra, załączniki, ale... Nie, nie – dobra, teraz to rozumiem. Załącznikiem myślałem, że to widok. To jest może kwestia konfiguracji, pozwoleń na eksport załączników. OK, teraz tego nie ma. No nie wiem, ja bym to raczej widział tutaj. A pytanie w ogóle jest jeszcze inne – czy to nie powinno być podpięte w ogóle pod akcje masowe? Bo żeby wykonać eksport, to zawsze jest "Wykonaj regułę", tak? Teraz w ustawieniach.

**Anna Skupinska:** Nie, można – możesz albo to tak zrobić, żeby się wykonała, albo nie, ale nie musisz. Po prostu eksportować bez wykonywania.

**Damian Kaminski:** Jesteś pewna? Dobra, nie podważam tego, ale to jeszcze raz – spojrzmy.

**Anna Skupinska:** A, czy – tak, bo w starym można wybrać, czy mają się uruchamiać reguły, czy nie. Teraz jak eksportujesz, to się nie uruchamia reguł, ale będzie ustawienie eksportu.

**Damian Kaminski:** No, aha.

**Anna Skupinska:** To tam możesz sobie wybrać regułę, ale nie musisz.

**Damian Kaminski:** Dobra, bo jak tu wybiorę, to tu mogę po prostu "Pobierz" i to jest wtedy bez reguły, tak?

**Anna Skupinska:** Tak.

**Damian Kaminski:** A mogę wywołać regułę i to też pobierze i wykona regułę.

**Anna Skupinska:** Tak, a – czy w sensie – jak w ustawieniach eksportu wybierzesz, to wtedy ten eksport? Tak mi się wydaje, że wtedy uruchomi regułę.

**Damian Kaminski:** Jeszcze raz się zgubiłem. Jeszcze raz.

**Anna Skupinska:** Na wszystkich sprawach, które zaznaczyłeś w ustawieniach eksportu, możesz sobie wybrać regułę. Jak uruchomisz wtedy eksport z tego szablonu, to wtedy on uruchomi też na wszystkich sprawach regułę – moją regułę, którą wybierzesz.

**Damian Kaminski:** OK, dobra, już rozumiem. OK, czyli pobiera, a potem wykonuje regułę, że już coś zostało pobrane i dalej się tu nie będzie wyświetlać, bo są inne filtry.

**Anna Skupinska:** Na przykład.

**Damian Kaminski:** No, powiem szczerze, że mi się ta propozycja nie podoba.

**Anna Skupinska:** No to co chciałbyś zmienić?

**Damian Kaminski:** No, chciałbym – tylko chciałbym przedyskutować. Może, o tak – ja nie, nie mówię, że już tu autorytarnie to zmieniam, ale chciałbym to przedyskutować w takim razie z Kamilem i z Januszem. Więc może zróbmy na razie tak – trzeba przygotować do tego PBI, który będzie i tak definiował te...

**Anna Skupinska:** Mhm.

**Damian Kaminski:** Szablonów, tak? Czyli coś, co mamy tutaj?

**Anna Skupinska:** Mhm.

**Damian Kaminski:** To możesz już w międzyczasie zrobić?

**Anna Skupinska:** Dobrze.


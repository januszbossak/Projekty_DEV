**Data spotkania:** 3 listopada 2025, 08:01

---

**Janusz Bossak:** Dobra, naprawa nie jest. OK, tym podsumowaniu podsumujmy ten sprint, co tam się nam udało zrobić. Potem zacznie. Może tej Kamili Damian moderuje tematy?

**Damian Kaminski:** No dobrze, to znaczy pytanie, czy ktoś chce zacząć?

**Mariusz Piotrzkowski:** Ja w sumie jedną drobną rzecz, którą zrobiłem w tym sprincie, taką nową, poza naprawami błędów, to jest ten dolny pasek nawigacji dokumentu, to mógłbym ewentualnie pokazać, to będzie krótkie.

**Damian Kaminski:** Proszę bardzo.

**Kamil Dubaniowski:** Jadam kontekst biznesowy. To jest funkcjonalność, którą mieliśmy do tej pory, zmienił się nieco interfejs. Jak wiemy tej sprawy, wcześniej przełączanie dokumentów było tutaj w środkowej części tego podglądu. Natomiast teraz zeszło to na dolną belkę nawigacji. Klienci się o to upomnieli, tak naprawdę my chcieliśmy właściwie z tego zrezygnować, natomiast wyszło, że jednak jest to używane – przełączenie się między kolejnymi dokumentami. Wygląda teraz w ten sposób, że dopóki mamy jeszcze coś po lewej, to idziemy do lewej, jak mamy coś po prawej, jedziemy do prawej. W momencie, kiedy już skończyliśmy całą listę, to po prostu to jest, strzałki w lewo.

**Mariusz Piotrzkowski:** Oczywiście biorąc pod uwagę, że nie ma podglądu plików takich jak na przykład plik MKV – tutaj mam, to on się w ogóle nie wyświetla na tej liście, nie jest jako poprzedni, bo nie ma podglądu. Ale tak taki drobny rework tego dolnego. Sporo było ustawiania z tym, żeby to się dobrze sformatowało, żeby przycinał odpowiednio nazwy. Ale poza tym nie było to nic bardziej skomplikowanego.

**Piotr Buczkowski:** Mamy podglądy do plików wideo, może MKV na dodać. Mamy podglądy do plików wideo, może MKV dodać.

**Mariusz Piotrzkowski:** Może? Bo to jest nietypowy format w sumie.

**Piotr Buczkowski:** Być może. Zapomnieliśmy o tym. To nie wiem, czy to jest teraz często raz spotykamy.

**Mariusz Piotrzkowski:** Czy tylko tak słabo Piotr słyszę, czy to u wszystkich tak jest?

**Kamil Dubaniowski:** Coś ciebie tak.

**Mariusz Piotrzkowski:** Z tego co zrozumiałem, to Piotr mówił, że mamy mechanizm podglądu filmów, ale w tym przypadku MKV jako...

**Kamil Dubaniowski:** Nie został.

**Mariusz Piotrzkowski:** Nie jest obsługiwany. Podejrzewam, że dlatego, że MKV może zawierać tak naprawdę wszystkie formaty obrazu i audio i wiele różnych ścieżek, więc byłby bardzo skomplikowany, żeby go obsłużyć. Prawdopodobnie w 100 procentach byłoby tak, że jedna trzecia pliku będzie działała. Reszta nie, więc pewnie dlatego nie ma akurat, ale zgaduję, że to był jakiś klasyczny MP4, no to pewnie by zadziałało.

**Piotr Buczkowski:** Tam jest chyba po prostu lista rozszerzeń obsługiwanych, można spróbować dodać. Nie wiem czy jest sens, czy nie. Słuchajcie, teraz lepiej.

**Mariusz Piotrzkowski:** Chyba nie ma sensu. To było coraz lepiej.

**Damian Kaminski:** Tak.

**Mariusz Piotrzkowski:** Według mnie nie ma sensu, bo to jak mówiłem jest zbyt dużo kombinacji, co MKV może zawierać. To jest najbardziej rozbudowany format chyba filmów, kontener filmów.

**Piotr Buczkowski:** Znaczy tutaj tak jest po prostu obiekt typu wideo. Albo usłyszy, albo nie.

**Mariusz Piotrzkowski:** Afektywne, tak, bo to...

**Piotr Buczkowski:** No dobrze, to to taka uwaga.

**Mariusz Piotrzkowski:** Podobnie z nowych rzeczy to w sumie tyle, bo jeszcze tam nad 2 nowymi rzeczami pracuję, to w tym sprzęcie pewnie dopiero dokończę. Dzięki.

**Damian Kaminski:** OK. Związane z tym tematem jest też temat Filipa, bo poprawiliśmy też podgląd raportu, żeby on był jednolity, natomiast on jeszcze tej poprawki nie zawiera i czy on będzie miał możliwość jakiegoś przełączania się w takim kontekście, to to pewnie należałoby się zastanowić, może i tak. Natomiast nie wiem, czy Filip jesteś w stanie to pokazać.

**Kamil Dubaniowski:** No takie przełączenie wnioskowali też tam jeden ze starszych klientów. To co pamiętacie?

**Damian Kaminski:** Na raporcie można myśli.

**Kamil Dubaniowski:** Tak, tak, z wyszukiwania zaawansowanego tego Bielii. Pamiętacie to wyszło wśród konsultantów. Tak jak powiedział, że to jest klientom, bo ze 2013, że dla nich w ogóle było robione wyszukiwanie zaawansowane i oni mieli tam właśnie podglądy takie luźne na sprawie dodane. I z wyszukiwania dało się je podglądać. Mogłyby to wejść jak najlepiej do nowego sportowego, no ale.

**Damian Kaminski:** No dobra, no to jest odrębny niestety komponent, bo tutaj to mamy Reactowe, a tu nie Reactowe, więc trzeba to zrobić tak jakby odtworzyć na nowo, ale możemy się nad tym pochylić.

**Filip Liwiński:** To tak, to mogę pokazać ten podgląd dokumentów na raportach.

**Damian Kaminski:** Proszę bardzo.

**Filip Liwiński:** Tak, jest przybliżonym do tego raportu na sprawie. Że z paginacją to same akcje to na sprawie. Też widok pełnoekranowy. Też ładowanie kolejnych stron. Też jaką sprawie? No i to w sumie tyle. Mogę przy okazji pokazać sortowanie na formularzu, na liście, liście formularzu. I to jest tam dodawaliśmy funkcje dodawania pola. No to dodawanie Forest teraz wszyscy. I mamy okno modalne do budowania jakiegoś tam pola. Słownik. Tak i sortowania, sortowanie puli sekcji. Drop. I tak samo pól. Też po zagnieżdżonych bratnie.

**Damian Kaminski:** A między sekcjami też można przenosić tak pola?

**Filip Liwiński:** Jeszcze jeszcze właśnie tego nie robiłem.

**Kamil Dubaniowski:** Jeszcze nie, to mam wpisane na ten sprint.

**Filip Liwiński:** Tak.

**Damian Kaminski:** OK.

**Piotr Buczkowski:** Bo to co zauważyłem w piątek, obsługuje przecież błędy w duplikowanie nazwę.

**Filip Liwiński:** Ee.

**Kamil Dubaniowski:** To też, też, tak, jak ci tam się napisałem, to jest do obu tematów i do formularza graficznego i do listy. To już sobie dopisałem do listy zadań. Tym na tym te 2 tygodnie.

**Filip Liwiński:** I co tam jeszcze? No i w sumie to jest repozytorium plików, tu nie wiem Damian pokazywać.

**Damian Kaminski:** Myślę, że na ten moment chyba się wstrzymamy, bo znaczy nie wiem jak Janusz to niż bo.

**Kamil Dubaniowski:** Znaczy tutaj wiem, że jest chyba też z nami Daniel. Powinien być przynajmniej, a jak nie to obejrzą nagranie, bo to było jedno z ich zgłoszeń. Temat dotyczący pola typu static poziomu tej listy. Ona teraz jest już również edytowalne w poziomie takiego okna.

**Filip Liwiński:** Tak.

**Kamil Dubaniowski:** Narzędziami tak, czyli nie już tam inline, tylko można sobie je edytować i formatować. Natomiast pozostałe typy tekstowe zwykłe są inline, żeby przyspieszyć, bo tutaj się nie używa stylowania, więc nie ma sensu otwierać jakiegoś okna. Teksty zazwyczaj tłumaczeń nas w pól są krótkie, więc edycja pól na przykład jest inline. Wyjątkiem właśnie jest to pole static, które się otwiera w edytorze z forma. I zmiana typu pola chyba już była. Zmieniliśmy tutaj jedynie nieco tam styl tego przycisku, żeby to wyglądało tak jak w innych miejscach, ale cały schemat działa tak samo, więc to jakaś kosmetyka jeszcze weszła w tym sprincie. A od przyszłego sprzętu też jest sporo tematów takich wyrównawczych, żebyśmy właśnie dogonili tę starą listę. Między innymi w momencie, kiedy Filip dodał pole typu Słownik, to my nie widzimy tutaj, jaki to jest Słownik. I nie da się szybko do tego słownika przejść, więc takie jeszcze niuanse ze starej listy. Wszystko wypisałem listę i to jest też cel sprintu, ale to za 2 tygodnie.

**Damian Kaminski:** OK, jeśli to wszystko to Filip pokaż, może jednak uważam, że...

**Filip Liwiński:** Nam, że.

**Damian Kaminski:** Ee, pokaż to czym się zajmowałeś. Więc kontekst biznesowy – tworzymy zupełnie nową funkcjonalność na potrzeby realizacji umowy dla WIM-u. Tak jak zrobiliśmy komunikator, tak samo repozytorium plików, czyli coś, co jest zupełnie nowym podejściem w kontekście obsługi obiektów w AMODIT. Tak, czyli nie powiązanie ze sprawą, to nie sprawa niesie pliki, tylko pliki są totalnie niezależne, tak jak w każdym repozytorium plików. Jesteśmy na razie na etapie, gdzie mamy już jako jakiś zalążek frontendu, on już w sumie jest dość mocno zaawansowany w kontekście tego, jakie na wstępie te repozytorium będzie miał funkcjonalności, natomiast nie mamy jeszcze żadnego backendu, więc bardziej może w formie zabawkowej. Możliwość przeszukiwania drzewa, to drzewo się wyrysowuje tak jak widzicie i możliwość udostępniania określonych zasobów. Różne widoki, więc tutaj staramy się być spójni z tym co już istnieje, w zakładce procesy czy raporty, czyli te układy kafelkowy, czy też układy listowe. I to na ten moment chyba tyle, bo tu jeszcze to nie działa tak nigdzie, w sensie nie ma do tego backendu. Tutaj czekamy na wytyczne od Piotra. I będziemy, może jako jeszcze ciekawostkę, będziemy to robić analogicznie jako komunikator, czyli zewnętrzną aplikacją przy wsparciu Java, po prostu, żeby przyspieszyć prace nad tym.


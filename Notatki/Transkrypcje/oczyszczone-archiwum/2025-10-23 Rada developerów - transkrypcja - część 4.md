**Data spotkania:** 23 października 2025, 08:02 - część 4

---

**Anna Skupinska:** Mhm.

**Piotr Buczkowski:** SQL.

**Anna Skupinska:** A, my podobnie. To...

**Piotr Buczkowski:** Czy nie – to, że – nie, to, że tutaj tak zapisujemy błąd, tylko generujemy nowy Exception, który zawiera dodatkowe informacje.

**Anna Skupinska:** Właśnie mamy coś bardzo podobnego właśnie w tym DatabaseError. Jak będziesz na AmodReport.Preview.SQLBuilder, to tam jest ta funkcja. Naprawdę, to po prostu wpisać – to jest Amod Abstract... i tak dalej – ale łatwiej po prostu wpisać nazwę do wyszukiwania, zauważyłam.

**Piotr Buczkowski:** Może już poczekaj.

**Damian Kaminski:** No, ja tą nazwę na czat, żeby Piotr miał to szybciej.

**Anna Skupinska:** No.

**Piotr Buczkowski:** I to – wiecie, co mam patrzeć?

**Damian Kaminski:** Mhm.

**Anna Skupinska:** AmodReportPreview – zaraz – to tak. I tutaj – ta-da – jest. No to właśnie ta funkcja i ona się uruchamia za każdym razem, jak jest błąd w bazie danych. To możesz zobaczyć, jest używana w – są 3 referencje do niej. Ja nawet zapisuję jeszcze – ci pokazuję – wiesz, wysyła do frontendu ID loga, więc można teraz zobaczyć – był stopień błąd – i on ma taki ID, żeby później nie było problemów, że ludzie nam wysyłają, że to był błąd, i później wysyłają loga, który jest zupełnie niezwiązany z tym błędem.

**Damian Kaminski:** No tak, tylko ty mówisz, że to mamy, ale to się nie wyświetla.

**Anna Skupinska:** A, czy – najwyraźniej z jakiegoś powodu to nie działa. Możesz zobaczyć, jak, kiedy to jest używane – po tłumacz referencje. To jest używane przy Executor, jak używamy.

**Piotr Buczkowski:** Dobrze, co – tam przykłady, kiedy to się nie zalogowało? Pytanie, czy w tych przykładach to właśnie jest logowane, tak?

**Anna Skupinska:** No, będziemy już trzeba przejrzeć te przykłady, znaczy – no, jeżeli w zadaniu są przykłady.

**Piotr Buczkowski:** No tak, to jest sprawdzić, czy przejdzie – to jest tylko wątki. No, bo wiesz – ja wtedy tak próbowałem zrobić, żeby to było ogólne, żeby na przykład... Stąd ten właśnie – ten override – może w szefie kodu nic nie trzeba było zmieniać praktycznie, tak. Wszystko to przeszło przez te – jakby – o, to standardowy – naszą tworzenia Connection, tworzenia DB Command – wszystko szło przez to. Także tak jak – także tutaj też właśnie ten sposób, że to zwraca nadpisany... egzemplarz też właśnie też, żeby nic nie trzeba było zmieniać, żeby nie było podwójnych logowań tego samego, tak.

**Anna Skupinska:** Rozumiem.

**Piotr Buczkowski:** Że logowanie jest tam, gdzie było, tylko też rozszerzone.

**Anna Skupinska:** No cóż – co – pewnie dużo będzie analizy w tym zadaniu. Będę musiała spróbować odtworzyć błędy i zobaczyć, dlaczego one się nie logują.

**Piotr Buczkowski:** No, trzeba, trzeba.

**Damian Kaminski:** No tak, tylko to – raz tą analizę jak zrobisz, to potem wszyscy – cała reszta analiz będzie uproszczona, bo będziemy mieli loga. Powód błędu niewyświetlania raportu, więc – no – trzeba to zrobić raz, żeby potem było łatwiej przy wszystkich innych błędach.

**Anna Skupinska:** Dlaczego – trzeba pamiętać, że czasami błąd nie jest w bazie danych, tylko błąd jest – no, w trakcie – jakby w kodzie poza bazą danych. Wtedy nie pokazujemy SQL, bo nie ma sensu, bo...

**Piotr Buczkowski:** No nie, nie, nie – no, to powinny być tylko błąd – no – Executor Reader, Executor Command, tak? Tak, z jakiego SQL – tak, tak, tak. Dlatego pytał – tak, to jest coś, co jest związane z SQL.

**Anna Skupinska:** Będę musiała zobaczyć te błędy, które wyszły – one w ogóle się zdarzyły w bazie danych, czy nie gdzieś indziej?

**Damian Kaminski:** Ale jakie błędy – w sensie potrzebujesz bagów?

**Anna Skupinska:** A, czy...?

**Piotr Buczkowski:** Co – to mają być tylko błędy przy wywołaniu – nie wiem – jak z jakiegoś Reader.

**Anna Skupinska:** No, jeśli tak, tylko problem jest taki, że teraz w nowych raportach jest tak, że nieważne – jakiś błąd się zdarzy w bazie, nieważne jaki błąd się zdarzy w backendzie – to ci pokazuje ten sam komunikat, że wystąpił błąd przy pobieraniu danych z bazy danych.

**Piotr Buczkowski:** No to, ale logowane – jeżeli jest logowany błąd, przy którym wystąpił przy wykonaniu zapytania.

**Anna Skupinska:** No.

**Piotr Buczkowski:** Jest gdzieś wykonujecie – dzieci, bo w którymś momencie zapytanie, tak – no, to trzeba do tego wykonania zapytania...

**Anna Skupinska:** Tak, tak, tak.

**Piotr Buczkowski:** Dodać takie logowanie, jak ja dodałem tutaj. Tylko w tym miejscu, jeżeli było – wystąpił gdzie indziej, to to kompletnie co innego jest.

**Anna Skupinska:** Znaczy – tak się trochę zastanawiam, znaczy – no cóż – będę musiała nad tym trochę posiedzieć i popatrzeć, bo teraz – co?

**Piotr Buczkowski:** Może, może w ten sposób da się jakoś, tak – nie wiem – z jakiego taką... Command korzystacie – może ten Command? Może, może da się podpiąć pod tego DBCommand? Tak, to – tego, tego naszego DBCommand – tak, gdzie to było?

**Anna Skupinska:** Muszę się – muszę się... Czy – mogę pokazać, jak to wygląda u nas? Jak będziesz z powrotem na SQLBuilder, to tam jest funkcja Executor. I tam w tym Execute jest uruchamiany SQL.

**Damian Kaminski:** To jest 182.

**Piotr Buczkowski:** Gdzie mam szukać?

**Anna Skupinska:** Ctrl+F – Executor – wpisz. I to jest ta funkcja. Jak zjedziesz niżej – to trochę niżej – i tutaj w tym try-catch on właśnie uruchamia kod. I poniżej są catche, które uruchamiają funkcję DatabaseError, tylko że one mają tylko dla konkretnych – tych wyjątków – więc może w tym jest problem, a nie dlatego, że... A, w sumie – jeżeli jest też – no, to w sumie też on pokazuje. Wszystko powinno być w sobie, no – więc nie jestem pewna, gdzie może on się przekraść, ten – co – możliwość.

**Piotr Buczkowski:** Nie, no – to jest tutaj, tak? To znaczy – być może tutaj, chyba że tutaj, tutaj wewnątrz też jest to, tak.

**Anna Skupinska:** A, tutaj – on pewną, że ten DatabaseError – on właśnie daje LogError i wszystko wpisuje, znaczy wpisuje...

**Piotr Buczkowski:** Prawdopodobnie to – to jest AmodDBException – to jest to moje Exception, tak? Które powinno powodować, że – też tego nie – to nie jest potrzebne, na przykład.

**Anna Skupinska:** Więc można się parę razy wpisywać.

**Piotr Buczkowski:** No, ale to już się pojawi.

**Anna Skupinska:** A, więc tak – zwłaszcza z taką – nie wygląda jakby błąd.

**Piotr Buczkowski:** No, ale w – tam albo tam albo tam – jest jakaś stara wersja, tak? Tego tutejszego, tak – to być może tam jest stara wersja.

**Anna Skupinska:** Tak, możliwe, że tam jest stara wersja, zanim myśmy to dali, więc trzeba po prostu...

**Piotr Buczkowski:** Bo – to wiem – sierpień, tak – sierpień. Jakieś pięć-cztery temu? Pytanie, w której wersji to te dane, tak? Tutaj jest kieszeń.

**Anna Skupinska:** W marcu tego roku.

**Piotr Buczkowski:** Marcowa, pytanie. W sumie poprzednie, tak – a nie, poczekaj, nie – to skoro jest "pending", to jeszcze wcześniej, tak.

**Anna Skupinska:** A, możemy po prostu wejść do starszej wersji i zobaczyć, czy – jakieś – jak tam było zwracane. Być może jedyną rzeczą, którą użytkownik musi zrobić, to zaktualizować na nową wersję.

**Damian Kaminski:** Masz na myśli, że nowy AMODIT będzie już to logował?

**Anna Skupinska:** No, kod od tego jest tutaj w AMODIT.

**Damian Kaminski:** No dobrze, a jesteśmy w stanie ustalić, w jakiej wersji?

**Anna Skupinska:** Nie, widzisz, że on...?

**Piotr Buczkowski:** Sierpniu, tak – zrobił...

**Damian Kaminski:** Bo mamy przykłady błędów, tak – no, to pytanie, jaka wersja ma być AMODIT, żeby to sprawdzić?

**Piotr Buczkowski:** No tutaj – pani chyba dodałaś to lokalnie, i tak. To te – sierpniu, tak?

**Anna Skupinska:** Tak, ale mam wtedy – noga, ID – także dawałam logo ID, dlatego że – no, no – problem trochę taki, że jak ludzie zgłaszali błędy, to podawali niewłaściwego loga, i wtedy później – naprawdę – że to jest log, później mówię – a błąd ciągle występuje.

**Damian Kaminski:** Dobra, inaczej – na develop to, co pokazujecie – jest? To już – robię test, który wiem, że działał.

**Anna Skupinska:** To chyba powinno być – że robię tak.

**Piotr Buczkowski:** No, to jest – develop, tak?

**Damian Kaminski:** Dobra, zaraz spróbuję zrobić test.

**Piotr Buczkowski:** Tak.

**Anna Skupinska:** Tak, bo on tutaj nie tylko daje tego SQL, ale też rzuca definicję raportu, żeby łatwiej było można go odtworzyć – ten błąd.

**Piotr Buczkowski:** No to – to było. To jest marcowa wersja, widzę, tak.

**Anna Skupinska:** Tak, więc to było już w marcowej, tak mi się wydaje. Wejdę na wersję marcową, zobaczę, że to jest wersja marcowa, bo to – dlatego że to było nadawane w marcu, nie znaczy, że jest – trafiło do wersji marcowej.

**Piotr Buczkowski:** No tak, tak, tak, tak.

**Damian Kaminski:** Dobrze, już sekundkę, już sprawdzam. No... My się...  No, bo było to widoczne tylko dla... Za sekundkę – może inaczej to będzie prostszy.

**Anna Skupinska:** OK, więc w wersji marcowej jest to najnowsze wersje – miasta, gdzie zrobimy trochę inaczej, ale on ciągle powinien wpisywać te – GetCommandInfo – w wersji marcowej to jest – o, może wyślę wam na czat kod.

**Piotr Buczkowski:** Ale pytanie, czy – jak to tam jest wersja, tak?

**Anna Skupinska:** No, no pytanie, bo to jest – nam takie jest najnowsze, bardzo – jakby są obrazek – więc on powinien wpisywać, nieważne, jakiś – co się stanie – to wpisywać do – GetCommandInfo.

**Piotr Buczkowski:** Gdzie u klienta?

**Anna Skupinska:** Za – niektórzy oni mają marcową.

**Piotr Buczkowski:** Którą oni mają wersję? Czy mamy March, czy...?

**Anna Skupinska:** Tak właśnie.

**Piotr Buczkowski:** Oddzielnie, z kolei.

**Anna Skupinska:** Tak, wszędzie było oddzielnie, później zostało – dlatego dostała ubrane w tę samą funkcję, bo one chyba musiały być inaczej, bo te... Nie jestem – dlaczego tak zrobiliśmy, ale – potem po prostu włożyliśmy to do DatabaseError, żeby to nie było – nie było tyle powtarzania kodu.

**Piotr Buczkowski:** Może macie tej – tabeli – tak – dla oddzielnie dla MySQL, Exception, czy innych?

**Anna Skupinska:** Na samym dole jest to zrobione dla Exception ex, więc powinna być dla wszystkich wyjątków. Myślę, że to było dlatego, że DatabaseError – a, tak to – od razu jest DatabaseError – że on musiał mieć oddzielne – jakby oddzielne typy – to dlatego to było zrobione. Bo on nie mógł już po prostu całego Exception ex – on musiał mieć oddzielny typ – i bo każdy typ trochę inaczej działał. Nie jestem pewna, jak to później naprawiliśmy, ale działa teraz lepiej – nie ma tyle powtórzeń kodu.

**Piotr Buczkowski:** No dobrze, czyli najprawdopodobniej to już jest zrobione, tylko trzeba nową wersję.

**Anna Skupinska:** Tak.

**Damian Kaminski:** No i nawet ten błąd... Kurde, o co tu chodzi?

**Anna Skupinska:** Można pokazać ekran, Damian?

**Damian Kaminski:** Mogę, już pokazuję.


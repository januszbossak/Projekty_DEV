**Data spotkania:** 18 listopada 2025, 11:02 - część 2

---

**Kamil Dubaniowski:** I to jest przynajmniej tak, jak tutaj pokazują. Ustawiane na poziomie działów i wręcz oni podeszli do tego w ten sposób, że wchodzisz w odpowiednią klasę. Na przykład tutaj ta ewidencja osobowa – domyślnie do tej klasy dostęp mają wszystkie działy, czyli wszystkie działy mogą tutaj podpinać teczki spraw, ale możesz nałożyć ograniczenie, że na przykład biuro dyrektora generalnego jest wyjątkiem i oni mają do tego katalogu nie mieć dostępu i jeśli nałożysz to ograniczenie tu na poziom tej ewidencji. Osobowej, czyli poziom 22, to wszystkie katalogi pod spodem. Dziedziczą to ograniczenie, czyli w ogóle do tego, co tu i pod spodem. To biuro dyrektora generalnego nie może dodawać spraw. I to tylko do tego ma jakby uprawnienie się sprowadzać, że musimy na poziomie działów. Łatwo jej, jakby żeby to było też łatwo zarządzane, bo spodziewałem się, że to może mieć jakieś zmiany, że będą musieli tym zarządzać sobie po stronie klienta, łatwo przypisać dział albo właśnie przypisać wyjątki. Nie wiem, co wygodniejsze. Czekam na dane od klienta, jak u nich wyglądają te uprawnienia aktualnie i wtedy zdecydujemy, co robić. Pierwsze, czy na zasadzie w każdej piątki, czy wskaż działy, które mają mieć dostęp. To musimy obsłużyć, żeby łatwo to przepisywać. No i teraz do tego całego naszego schematu, do tej architektury. Musimy też wiedzieć, jak przechowywać te informacje i jak później łatwo wykorzystać je na naszym procesie, formularzu, sprawy, gdzie dostałem sprawę do obsługi i ja muszę jako człowiek z działu tam – biuro dyrektora generalnego. Jak rozwinę listę, żeby wpiąć do odpowiedniego katalogu JRWA, żebym widział tylko te, do których mam dostęp? Żeby to zrobić wydajnie, tak, żeby nie bawić się w jakieś set-reference, filtr, tak, czy reference query? Może i będzie trzeba tak, ale to to powinniśmy podjąć, bo to, że ja mam dostęp do tego katalogu. Ewidencja osobowa – to jest kluczowa informacja. Nie oznacza, że ja mam dostęp do wszystkich spraw w tym katalogu. Nie, ja mam dostęp do tych spraw, które obsługiwałem, czyli tutaj nasze uprawnienia są niezmienne, ale chodzi tylko o to, żeby uniemożliwić błędne wpięcie do katalogu, do którego ja w ogóle jako pracownik tego działu nie powinienem móc nic wpisać. Więc bardziej chodzi o te uprawnienia w tę stronę, czyli żeby każdy widział tylko te katalogi, do których może coś wpinać. I jak przechowywać te dane w działach, tak, jak to później dobrze obsłużyć i używać w samym procesie już obiegu pojedynczego dokumentu?

**Janusz Bossak:** Tak, bo to jest. Tak, to jest jakby pierwsza rzecz, to jest ten poziom prawa do tworzenia nowych teczek. A drugi poziom, ale ten myślę, że już byśmy rozwiązywali za pomocą mechanizmów AMODIT, bo teczka sprawy będzie procesem pod tytułem teczka sprawy, tak jak mamy te dokumenty w teczkach pracowniczych. To teczka sprawy będzie takim.

**Kamil Dubaniowski:** No, natomiast.

**Janusz Bossak:** Sprawą w procesie pod tytułem teczka i obiegową na przykład. I teraz, jak już taka teczka sprawy zostanie założona przez kogoś, kto miałby uprawnienia. To. Jak ja jestem teraz jakiegoś innego działu? I mam jakiś dokument, który dotyczy tamtej sprawy. I to jest dla mnie niejasne do końca – tutaj Kamil to też nie wiem, jak to się dzieje. Że ja bym mógł w jakiś sposób wpiąć ten mój dokument, który teraz dostałem, do tej teczki sprawy. Która istnieje? I pytanie, jak to się ma stać? Z punktu widzenia biznesowego, nie. Że po pierwsze – ja będę wiedział, że istnieje taka. Sprawa już założona dotycząca, nie wiem, reklamacji Kowalskiego? Czy ja mam się o to publicznie na forum, naszym komunikatorze odpytać, szukać. Nie bardzo, tego nie wiem, jak oni pracują, nie wiem, jak to się dzieje, że oni wiedzą, że istnieją jakieś teczki, do których trzeba wpinać, skoro teczka już po jej założeniu, bo to jest ograniczenie takie, że prawo do założenia ma tylko ten dział, ale później prawo do wpinania już do tej teczki mogą mieć inni, czyli ta teczka może być. Udostępniona innym działom i chyba na tym to polega, żeby po prostu ten, kto ją zakłada, mówi: OK. Tutaj będzie prawnik, księgowa i ktoś tam – ją po prostu udostępnia z góry tą teczkę do tych działów i jak tam do nich pisma wpadną, to oni będą mieli tą teczkę. Do dyspozycji, będą mogli do tej teczki sobie te sprawy podpinać.

**Kamil Dubaniowski:** Lekko rozumiem, czyli, że to jest prowadzone do poziomu uprawnień naszych na AMODIT? Osoba, która zakłada teczkę, powinny by zarządzać uprawnieniami do tej teczki i udostępniać odpowiednim ludziom.

**Janusz Bossak:** No właśnie, czy ludziom, czy działom, nie mam.

**Kamil Dubaniowski:** Działom, działom i ludziom, w sumie, tak, to.

**Piotr Buczkowski:** Nie róbmy tego, tak.

**Janusz Bossak:** Tutaj w tym. Musimy, bo.

**Piotr Buczkowski:** Nie rób tego w oparciu o sprawy.

**Janusz Bossak:** Musimy – nawet w oparciu o co? Przecież to są teczki spraw, to co to mają być innego?

**Piotr Buczkowski:** A jak będziecie sprawy – to masz sprawy do tej teczki wpinać.

**Janusz Bossak:** No linkować.

**Mariusz Piotrzkowski:** Ja jestem zdecydowanie przeciwko temu, bo będzie straszne.

**Piotr Buczkowski:** A co, co będzie? Na co – powiecie na tej teczce – jakie dane będą na tej teczce?

**Kamil Dubaniowski:** Numer teczki. Czyli ten katalog, w którym ta teczka jest? Pewnie jakieś daty, tak. Bo to kluczowe, kiedy została utworzona, przez kogo.

**Janusz Bossak:** Niewiele – z 10, powiedzmy, jakieś malowanie, pewnie.

**Kamil Dubaniowski:** I pewnie przydałoby się osadzić raport, żeby na poziomie sprawy tej teczki sprawy pokazać, jakie są pisma w środku.

**Janusz Bossak:** Tak, że tam były jakieś pismo, nie wiem, reklamacja – potem była jakaś odpowiedź do tego z innego procesu, bo ta odpowiedź mogła pójść. Potem, nie wiem. Prawnik napisał jakąś opinię, trzeba ją tam podpiąć.

**Piotr Buczkowski:** Czyli wszystko prawie wszystko oprzeć o body tej sprawy, tak.

**Janusz Bossak:** No tak.

**Piotr Buczkowski:** I chcemy optymalnie, nie chcemy żadnej optymalizacji robić.

**Kamil Dubaniowski:** Czy ten schemat JRWA? Ja jestem za optymalizacją. Bo to jest coś dedykowanego, ale flow obiegu tej sprawy – nie wiem, czy da się ustandaryzować, czy ja bym przyszedł, chyba.

**Piotr Buczkowski:** Czy to, czy tam będzie tylko do tego używany?

**Kamil Dubaniowski:** Nie będą inne procesy z tego, co kojarzę, na razie – zaczynam.

**Piotr Buczkowski:** No to nie róbmy tego, tak, nie róbmy tego, tak. To wydajnościowo tego nie obsłużymy dobrze.

**Janusz Bossak:** No ale nie. Ale to cała idea w tym, żeby to był AMODIT. Ja – co mamy robić? Osobny według ciebie system, osobną aplikację do tego. Nie bardzo rozumiem teraz jakby.

**Piotr Buczkowski:** Nie widzę możliwości budowania takiej struktury na podstawie spraw wydajnej.

**Janusz Bossak:** No ale przecież ona się opiera o sprawę, więc nie bardzo.

**Piotr Buczkowski:** No ale tutaj ile jest połączeń, tak, tak, to sprawa jest.

**Janusz Bossak:** I znaczy będzie połączenie pomiędzy taką sprawą z procesu, który się będzie nazywał teczka JRWA. I ta jedna sprawa będzie, można powiedzieć, gromadziła informacje o.

**Kamil Dubaniowski:** Pismach.

**Janusz Bossak:** Innych sprawach, czyli będzie posiadała linki, tak? Connected to case ID, na przykład.

**Kamil Dubaniowski:** To jest, powiedzmy, taki poziom, że mamy kontrahenta i wchodzimy na kontrahenta i widzimy wszystkie sprawy faktur, które były podpinane do tego kontrahenta w polu Odnośnik.

**Janusz Bossak:** Wszystkie faktury czy wszystkie umowy, tak. To dokładnie jest ten temat. To znaczy, ja nie widzę tu jakiegoś szczególnego obciążenia.

**Mariusz Piotrzkowski:** Są tu pytania – po pierwsze, ile w tym JRWA ma być kategorii takich elementarnych, ile tych zbiorów najgłębszych – i mówię o tych teczkach, to się tworzy tylko tych kategorii.

**Kamil Dubaniowski:** Tak, to wynika tutaj już – pan pokazuje 4, chyba, z tego, co pamiętam, tak, tutaj jest pierwsza nadrzędna, druga, trzecia i czwarta, co jest zamknięciem.

**Mariusz Piotrzkowski:** Tak, ale nie wiem, mi chodzi, ile będzie tych elementarnych, czyli ile będzie różnych tego czwartego poziomu, czy to będzie na poziomie 100, 1000, 10000, miliona?

**Kamil Dubaniowski:** Nie, to jest cała lista, więc my mieścimy się na stronie tam, na kilku stronach PDF-a.

**Janusz Bossak:** Koło.

**Mariusz Piotrzkowski:** Czy jest to – zakładam, że około 1000?

**Janusz Bossak:** 2000 – niecały 1000, niecały 1000.

**Mariusz Piotrzkowski:** Dobra, ile spraw to ma być rocznie?

**Janusz Bossak:** Milion.

**Mariusz Piotrzkowski:** To jeśli, jeśli miałbyś milion spraw, to w takiej sytuacji po roku.

**Janusz Bossak:** Nie wiem, nie wiem, ale dużo.

**Mariusz Piotrzkowski:** Zasilenie tego na sprawach. Podejrzewam, że wyszukiwanie będzie zajmować około 30 sekund. Jeżeli to zasilmy na sprawach z taką ilością parametrów.

**Janusz Bossak:** Najbardziej rozumiem. A czym? A czym się różni wyszukiwanie teraz w sprawach 10 milionów od tego, że będzie podpięte tam JRWA?

**Mariusz Piotrzkowski:** Ja bym to w ogóle inaczej optymalizował – ja bym tego nie robił na sprawach, tylko bym zrobił osobną zupełnie tabelę w bazie danych, które będą przechowywały dane dedykowane do JRWA, czyli odnośnie tego, jaka sprawa jest w jakim, w jakim repozytorium JRWA i tak dalej.

**Janusz Bossak:** Ale to przecież Odnośnik się zrobi. Jednym polem Odnośnik masz podpięcie pod teczkę sprawy.

**Mariusz Piotrzkowski:** Tak, ale jeśli zrobią to polem Odnośnik, to jest uniwersalny mechanizm, mało optymalizowany pod konkretne działanie. Jeśli chcemy, żeby to było wydajne, to zgadzam się w pełni z Piotrem. Musimy zrobić z tego osobny mechanizm.

**Janusz Bossak:** Ale. Ale co, ale co tu ma być wydajne? Panowie.

**Mariusz Piotrzkowski:** Wyszukiwanie. Przeglądanie.

**Janusz Bossak:** Ale jakie wyszukiwanie, w którym momencie?

**Mariusz Piotrzkowski:** No to jak Kamil mówi, że w tym celu będę – bardziej wszystkie jakieś tam jest, ale ja do jakiegoś kontrahenta, jeśli do tego kontrahenta będzie, nie wiem. 10, 10000 z 5 milionów spraw.

**Janusz Bossak:** Ale ile możesz wybierać – jedna teczka sprawy, ludzie.

**Kamil Dubaniowski:** Jedna teczka sprawy, to będzie tam, powiedzmy, nie wiem. 10 dokumentów, który będzie taki max.

**Janusz Bossak:** 10 dokumentów, 15.

**Mariusz Piotrzkowski:** No tak, ale jak jest zbiór ogólny, w którym to jest poszukiwane? To jest pytanie. Podam wam przykład, natomiast teraz sobie pracuję na logach.

**Janusz Bossak:** No ale przecież teraz mamy – nie, nie, nie, kompletnie nie rozumiem waszego jakby waszej obawy, przecież mamy wdrożenia, w których jest po 10 milionów rekordów i działa to.

**Mariusz Piotrzkowski:** No i teraz spróbujmy zrobić raport, który łączy to – bierze 3 różne rodzaje spraw. Łączy te sprawy w taki sposób, że każda jest prawdą powiązana. Następnie daję z tego wynik. Taki raport będzie wykonywać minutę.

**Janusz Bossak:** Ale po co nam taki raport?

**Mariusz Piotrzkowski:** No bo tak chcecie, żeby JRWA trochę było a działało z tego, co ja rozumiem.

**Janusz Bossak:** Nie.

**Mariusz Piotrzkowski:** A tetra – jak rozumiem, że można to źle rozumiem.

**Piotr Buczkowski:** Ja kompletnie tego nie rozumiem.

**Janusz Bossak:** Właśnie dlatego was tu wzięliśmy. Byśmy wszyscy razem to zaczęli rozumieć, bo.

**Mariusz Piotrzkowski:** Dobra, to może?

**Janusz Bossak:** Potem jest właśnie tak jak dzisiaj z tym filtrami użytkownika. Na początku każdy mówi, ja tego nie rozumiem, ja tam, niech robią, jak chcą i zrobią, jak chcą, i potem jest problem, nie. Chodzi o to, żeby to teraz zrozumieć.

**Kamil Dubaniowski:** Dobra, to jakby może tak od podstaw idąc – ja od początku procesu. Może tak – jesteśmy sobie w dziale administracja w LOTU, przyszło pismo, i to my musimy je rozpakować, zeskanować.


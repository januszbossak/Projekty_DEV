**Data spotkania:** 14 października 2025, 10:14 - część 3

---

**Damian Kaminski:** No pytanie teraz do Michała w zasadzie – czy da się ograniczyć commit, jeśli coś nie jest na Done, tak?

**Łukasz Bott:** Znaczy to, co Janusz pokazuje, to pewnie jest po prostu część commitów jako takich – które, gdzie, kiedy...

**Janusz Bossak:** To są commity, ale commit to jest merge, tak czy nie?

**Łukasz Bott:** No, to wygląda, że nie koniecznie.

**Damian Kaminski:** Znaczy dzwonimy, jeśli chcemy nad tym dyskutować, to dzwonimy Michała.

**Łukasz Bott:** Nie, to Michał... No tak, dokładnie, niech to wyjaśni.

**Damian Kaminski:** Bo inaczej to...

**Janusz Bossak:** Albo Piotr. Piotrek powie, dlaczego ten 22195...

**Damian Kaminski:** Albo Piotr.

**Janusz Bossak:** Jest w takim stanie, że może on po prostu nie poprawił – znaczy, nie poprawił na backlogu, czyli zostawił na in progress, mimo że już jest zmergowane i scommitowane i tak dalej, nie?

**Damian Kaminski:** No, ale commit to co oznacza? Commit nie oznacza dodanie po prostu gdzieś tam do...

**Janusz Bossak:** I...

**Łukasz Bott:** Być może taki jest...

**Damian Kaminski:** Tych plików, ale jeszcze nie wyszło to do żadnej z wersji. No bo skoro nie ma...

**Łukasz Bott:** Moim zdaniem to jest tak: Piotrek Buczkowski zrobił poprawkę w swoim lokalnym środowisku developerskim i testuje.

**Damian Kaminski:** Też mi się tak wydaje.

**Janusz Bossak:** Dobra.

**Łukasz Bott:** Zrobił commit do repozytorium i to jest, moim zdaniem...

**Damian Kaminski:** Dzwonimy, bo...

**Łukasz Bott:** Nie zgadujmy.

**Damian Kaminski:** Trzeba pytać o źródła.

**Łukasz Bott:** Jednego i drugiego tak momentalnie, tak?

**Janusz Bossak:** Dobra.

**Łukasz Bott:** Piotra i Michała, może dzwonić?

**Janusz Bossak:** Michał.

**Damian Kaminski:** Ale podsumowując, nie pominął, tak?

**Łukasz Bott:** No, to co zaznaczone było jako Done, tak – i te 2 ten...

**Piotr Buczkowski:** Jakieś spotkanie teraz było?

**Damian Kaminski:** Jest po prostu...

**Łukasz Bott:** Nie, hop takie.

**Janusz Bossak:** Nie mamy pytań takich.

**Damian Kaminski:** Ale...

**Janusz Bossak:** Damian zrobił mechanizm do tam generowania mniej więcej automatycznie – czy tam półautomatycznie – changelog. I trochę tak sprawdzamy, czy wszystko zostało uwzględnione i natykamy się na różne przypadki, które chcemy jakby zweryfikować. I jest taki commit dla zadania 22195.

**Damian Kaminski:** Wyświetlisz, czy mam wyświetlać?

**Janusz Bossak:** Wykrywanie duplikatów pól przy imporcie XML.

**Michał Zwierzchowski:** Poczekajcie, poczekajcie na...

**Piotr Buczkowski:** Ja tego nie dokończyłem, nie miałem czasu.

**Janusz Bossak:** No tak, ale chodzi nam o to – jest commit w środę o ósmej 58.

**Łukasz Bott:** No, no.

**Piotr Buczkowski:** Tak.

**Janusz Bossak:** Do wersji 25.0.3.31. To co to oznacza?

**Piotr Buczkowski:** Znaczy, poprawiłem to, żeby to nie był...

**Michał Zwierzchowski:** To jest...

**Piotr Buczkowski:** No to sprawiało problemy, że to były... Żeby już nie robił... Nie był to hotfix, ale wykryłem jeszcze jeden błąd w czasie testów.

**Janusz Bossak:** Tak, to już jest. Znaczy, chodzi mi o to, że to jest w tej wersji, tak?

**Michał Zwierzchowski:** Tak, to jest on... Paweł PBI.

**Piotr Buczkowski:** Tak.

**Michał Zwierzchowski:** Bo patrzycie na branch developer.

**Damian Kaminski:** Na developer, a nie OK – na developer, a nie na wersjach wydanych, tak?

**Janusz Bossak:** Nie, weź zmień wersję...

**Michał Zwierzchowski:** Znaczy, no patrzycie na branch developer. No to nie wiem, czy na innych nie ma też, bo na innych też może być.

**Damian Kaminski:** Nie, dobra. Słuchajcie, abstrahujemy od tego.

**Piotr Buczkowski:** Być może zrobiłem też do innych, bo wgrałem poprawkę, która powodowała popsicie procesu.

**Damian Kaminski:** A no właśnie.

**Łukasz Bott:** Dobrze.

**Damian Kaminski:** Czyli teraz tak – chcemy patrzeć na wersję...

**Piotr Buczkowski:** Już się nie psuje procesu.

**Michał Zwierzchowski:** Niżej, niżej, niżej, niżej...

**Janusz Bossak:** Formalnie, gdzie ta poprawka trafiła? Czy trafiła do wersji 25.0...

**Damian Kaminski:** Tą, to...

**Janusz Bossak:** 3.31 według mnie tak, bo jest commit na tym branche 25.0.3.31.

**Michał Zwierzchowski:** No to jak jest, to...

**Janusz Bossak:** I jest przeznaczona wersją 120. Więc teoretycznie wersji 120 ta funkcjonalność jest tam w większym, mniejszym stopniu – w pełni, nie w pełni, ale poprawiono coś tam, wyszło. I teraz ten changelog...

**Michał Zwierzchowski:** Jak?

**Piotr Buczkowski:** Czy już nie jest już... Już proces nie jest psuty, że się nie da otworzyć sprawy. Ale jeszcze może jedno pole w pewnym przypadku zniknąć w imporcie, to znaczy nie dodać się.

**Damian Kaminski:** Dobra, tylko słupy, zawsze chodzi o co innego – że to jest w ramach 22195, tak? Czyli wejdźmy teraz na 22195. I to jest in progress. I teraz gdzie się pojawia konflikt? To, że ty coś wydałeś, a my w naszym changelog bierzemy wszystkie zgłoszenia, które są w statusie Done. I tu mamy tą 120. W zasadzie do 120 są 2 poprawki plus twój commit, który... No właśnie, w naszym źródle się nie pojawia. I teraz pytanie, jak to połączyć?

**Piotr Buczkowski:** To było tak, że ja zrobiłem merge. I w czasie jeszcze testów po merge zauważyłem jeden błąd.

**Łukasz Bott:** Dobra.

**Piotr Buczkowski:** I nie było innych... To nie miałem czasu jeszcze zdiagnozować tego błędu.

**Damian Kaminski:** Nie puściłeś tego dalej, tak? Czy ty źle statusy tutaj oznaczyłeś – zrobiłeś commit, nie oznaczyłeś, że to jest do wydania, tak?

**Piotr Buczkowski:** Czy to nie jest? Robiłem commit i po commicie miałem zrobić do waiting for release, ale w czasie testów po merge do wersji wcześniejszej...

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Zauważyłem jeszcze jeden błąd.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** I nie miałem czasu, żeby go... Postanowiłem go jeszcze zdiagnozować przed przekazaniem do – czy to w ramach tego, czy coś – nie zdążyłem, nie miałem kiedy tego zrobić. Nie wiem, takie...

**Damian Kaminski:** No dobra, nie, ale to, wiesz, to nie rozliczamy, że tego nie zrobiłeś, tylko bardziej chodzi nam o to, żeby to dobrze rozumieć wszystko, jak to powinno być. Czyli to był błąd, powiedzmy, kwestii obsługi zgłoszenia.

**Piotr Buczkowski:** To zakwalifikowałem jako hotfix, bo po wgraniu takiego... Jest XML nie da się tworzyć spraw tego procesu.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Ta poprawka już się... W czasie testów zauważyłem jeszcze mniej, jak mniej krytyczny błąd. I rzeczywiście może mogłem zrobić... Nie miałem czasu go diagnozować, żeby go opisać ten błąd, nawet tak.

**Damian Kaminski:** No dobra, ale to teraz słuchajcie, bo tak – ja powiedzmy wypuściłem i tu jest... I tutaj go nie ma, a to jest... No to, ale to też możemy ustalić, że niekoniecznie wypuszczamy to codziennie. Możemy to opuszczać z tygodniowym buforem. I jak się zdarzą jakieś takie, powiedzmy, kwestie, to my tu nie musimy wydawać changelog dzisiaj do tego, co się wydarzyło wczoraj, tylko możemy mieć bufor kilkudniowy. Nawet może 7-dniowy.

**Łukasz Bott:** Ja bym, wiesz co, ja bym postulował nawet miesięcznie. Raz na miesiąc jak to zaktualizujemy, to będzie dobrze. Tylko wtedy musimy przyjąć jasne kryteria – że które przyjąłeś – że to jest Done i jest oznaczona release version, tak?

**Damian Kaminski:** Co to? Inaczej bym powiedział. Nie raz na miesiąc. To powinno być spójne z tym, co mamy – tu jest 119, tam jest 119, bo ktoś może to pobrać, a to znaczy, że powinien mieć informację, co jest w tej wersji, nie?

**Łukasz Bott:** No OK, dobra. Ale to... To tutaj Michał, tak akurat tą listą – tym konkretnym artykułem – to Michał zawiaduje.

**Piotr Buczkowski:** Czyja jest... To potrzebny?

**Łukasz Bott:** Dzięki, Piotr. Już to miejsce, wiemy o co chodzi.

**Damian Kaminski:** Ty, Michał, z jaką częstotliwością tu robisz update? Częściej niż raz w tygodniu?

**Michał Zwierzchowski:** Jak sobie przypomnę – czasami częściej, czasami rzadziej.

**Łukasz Bott:** Albo na życzenie, nie? Jeżeli...

**Michał Zwierzchowski:** Albo narzekanie, tak.

**Damian Kaminski:** No dobra, ale też możemy przyjąć jakąś, powiedzmy, zasadę. Bo to może być element – nie wiem – twojej pracy na spotkaniu piątkowym, bo tam przysłuchuję się. Ale de facto pewnie wam klikanie tego to zajmuje tam 20 minut, nie więcej. A tam czasami tylko jesteś wywoływany do tablicy, a jak ktoś potrzebuje dzisiaj mieć 120, to dostanie ją od ciebie offline'owo, tak? Nie musimy tutaj codziennie w tego publikować. A jeślibyś jednocześnie miał zautomatyzowane generowanie changelog, to razem z tym mógłbyś w sumie uzupełnić też to, czyli wkleić po prostu tekst, który byś... Który byś mógł skopiować, żeby to – ta wersja, którą wypuszczasz tutaj – miała pokrycie w liście zmian.

**Michał Zwierzchowski:** Ale ten... Nie, bo ja jeszcze tutaj sprawdzam, czy wszystkie zadania są zamknięte.

**Łukasz Bott:** No, ale tutaj przyjmiemy – na changelog przyjmiemy właśnie takich kryterium, że one muszą być Done i muszą być oznaczone w konkretnej release version, nie?

**Michał Zwierzchowski:** A dobra. No dobra, są... No tak. No to można było tego...

**Damian Kaminski:** No dobra, to znaczy, pozostaje tylko kwestia merytoryki, bo żeby tutaj też teraz wszystkiego nie zrzucić na Michała – nie wiem – musimy po prostu podjąć decyzję, że powiedzmy przygotowanie tego... To ktoś to może musi jeszcze zwalidować, czy wszystko co pisane jest poprawne i do publikacji?

**Łukasz Bott:** Nie, może pozostać tak jak jest. Czy Michał był – odpowiada za tamtą tabelkę z przepisami wydań, tak? A akurat zarządzanie Wiki changelog – to jest mój gdzieś tutaj zakres, zakres obowiązku, więc tutaj... Jeszcze raz, Damian, dzięki za narzędzie. Pewnie jutro jakoś tam nie wiem, przetestuję, uzupełniamy resztę. I teraz kwestia umówienia się jako częstotliwości – robimy tak, czy raz na miesiąc wystarczy, czy raz na tydzień, czy co 2 tygodnie? Bo na żądanie to zawsze można – to nie jest problem, jakby, tak masz przypadek Orlenu.

**Damian Kaminski:** Znaczy, żeby nie było żądania, to według mnie to powinno być po prostu synchronizowane z tym, co robi Michał. Czyli Michał wrzuca wersję tu, a ty wrzucasz opis tu. I według mnie częstotliwość raz na tydzień to jest zupełności wystarczająco. A może raz na 2 tygodnie?

**Łukasz Bott:** Nie. Czyli innymi... A wiecie co, najlepiej to jest po prostu... Moim zdaniem tak...

**Michał Zwierzchowski:** Poczekaj, ale to jak jest zautomatyzowane, to może od razu zautomatyzować uzupełnianie tam numeru wersji? Nie dałoby się? Bo w sumie link jest praktycznie... O czym... Tak, wielki ten link jest stały, tu jest 120, więc brakuje tylko w sumie końcówki z datą builda, nie?

**Łukasz Bott:** Nie, to nie jest to tak zautomatyzowane, że tu idzie tekst. Ten tekst, który oglądamy, to jednak Damian jakoś tam przejrzał i manualnie wkleja, tak.

**Michał Zwierzchowski:** A no.

**Damian Kaminski:** Tak, tak.

**Łukasz Bott:** To nie... To na razie aż takie automatyzacji nie róbmy, bo to musi ktoś zweryfikować. Bo Damian przygotował narzędzie do wygenerowania tego changelog, ale to wymaga jakiegoś tam przejrzenia, bo na przykład na niektóre z niektórych zgłoszeń na przykład tutaj nie ma – tylko dlatego, że właśnie tak jak nam powiedział – wstyd się w tym słowie chwalić nimi, bo to jakiś tam nasz babel, albo był niejasno opisany.

**Michał Zwierzchowski:** A wiecie co? Jeszcze apropos... Apropos changelog i tego, że coś ucieka – mogę udostępnić ekran?

**Damian Kaminski:** Tak, ale ja bym dał auto poprawkę. Skoro pracujemy w trybach dwutygodniowych, to według mnie raz na 2 tygodnie.

**Łukasz Bott:** No, to tu, pani o tym samym – to miałam samą powiedzieć – to na koniec na koniec sprintu czy na początku kolejnego sprintu za poprzedni sprint, tak? Po prostu generujemy changelog i tyle.


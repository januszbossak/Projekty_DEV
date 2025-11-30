**Data spotkania:** 3 listopada 2025, 08:01 - część 2

---

**Piotr Buczkowski:** Nie.

**Damian Kaminski:** Tak, Piotrze.

**Piotr Buczkowski:** Potem nie.

**Damian Kaminski:** To uzupełnij, jeśli chcesz coś jeszcze dopowiedzieć, to możesz tu wysoko poziomo.

**Piotr Buczkowski:** Wymagania, które usłyszałem, wymagania, które od was usłyszałem w czasie piątkowego spotkania sprawiają, że to będzie czymś siemowita. Popartą obecne struktury.

**Damian Kaminski:** No to tak jak słyszycie tutaj jeszcze ustalamy właśnie ten backend do wymagań, więc ja miałem jeszcze stan piątku, a dzisiaj w takim, więc no może na razie nie będziemy się w tym zakresie rozwodzić, bo jest właśnie jeszcze na etapie projektowania, skoro już tak zaleca, to nie tak będziemy to realizować.

**Lukasz Bott:** Damian, przepraszam, mam pytanie takie z ciekawości, bo stwierdziłeś, że przynajmniej tak funkcjonalnie to, że to będzie odrębne jakiś tam repozytorium plików niepowiązanych ze sprawami, tak, czyli że file, ale rozumiem, że przewidujemy jakość funkcjonalność typu, że mamy na sprawie i podłącz plik z repozytorium.

**Damian Kaminski:** Tak, tak.

**Piotr Buczkowski:** Właśnie dlatego, właśnie dlatego nie będziemy to robić jako...

**Damian Kaminski:** Dalekosiężnie tak.

**Piotr Buczkowski:** Takiej funkcjonalności powiązania plików ze sprawą. Roślina dla takich funkcjonalności i przemyślałem to i to to będzie wewnętrzna AMODIT. To nie będzie to zewnętrzna aplikacja. Żeby zrobić właśnie takie powiązania ze sprawcami typu, że powiedzmy na koniec sprawy podany plik wpinasz do repozytorium albo z repozytorium pobierasz plik do sprawy. Czy z pliku z repozytorium startujesz sprawę?

**Damian Kaminski:** Natomiast są to funkcjonalności, które wiemy, że będą przydatne w przyszłości. Nie wchodzi to w ramach naszego MVP, więc na starcie przy wydaniu produkcyjnym takiej funkcjonalności, integracji ze sprawami w tą czy w drugą stronę jeszcze nie będzie.

**Lukasz Bott:** OK, dobra.

**Janusz Bossak:** No ale tak powiem przyszłościowo trzeba mieć już dobrą, ale niektóre, żeby dało się to zrobić.

**Damian Kaminski:** Tak. Dokładnie.

**Lukasz Bott:** Ewentualnie tutaj możliwość pobrania jakiegoś tam linku do pliku i nie wiem to w tekście załączenia linku, przynajmniej.

**Piotr Buczkowski:** Nie.

**Damian Kaminski:** Znaczy, to może będzie rozwiązanie właśnie na początku tak, żeby posługiwać się linkami, ale docelowo pewnie będzie taka integracja, jak powiedziałeś, natomiast robimy to na razie na zaliczenie.

**Lukasz Bott:** No takie.

**Damian Kaminski:** A potem najchętniej byśmy to mówiąc wprost wystawili za to komuś rachunek za kolejne funkcjonalności, więc trzeba znaleźć klienta.

**Lukasz Bott:** Dobry.

**Damian Kaminski:** No dobrze, to tak jak mówię to jeszcze nie jest gotowe, więc tutaj nie będę się skupiał na funkcjonalnościach bardziej zabawkowo, że właśnie pracujemy nad tym tematem i tu ze strony właśnie Filipa już jesteśmy bardziej zaawansowani niż backendowo, ale będziemy to w tym sprincie nadrabiać.

**Filip Liwiński:** No dobra, to chyba tyle ode mnie.

**Damian Kaminski:** Dobra, dzięki.

**Daniel Reszka:** Przepraszam, bo nie słyszałem początku. Te pliki gdzie będą przechowywane, w bazie czy na dysku?

**Damian Kaminski:** Nie. Na dysku.

**Piotr Buczkowski:** Tak samo jak obecne załączniki.

**Daniel Reszka:** Tak samo, OK.

**Piotr Buczkowski:** Tylko nie przypięte do spraw. Tak naprawdę.

**Daniel Reszka:** OK.

**Piotr Buczkowski:** Tak, pomyślałem, żeby to był taki odpowiednik, powiedzmy obecne jakiś tych skanów. Tylko uporządkowany. No tak. Co pragnieniami?

**Daniel Reszka:** I to będzie jakiś osobny folder, bo teraz już nikt są jakby przypięte do folderów spraw, to będzie po prostu folder ze wszystkimi załącznikami czy struktura tych plików na dysku?

**Damian Kaminski:** Znaczy, słuchajcie, to zbyt szczegółowe pytanie, jesteśmy na etapie jeszcze projektowania tego backendu całego, więc jak to już będzie, to wtedy będziemy w stanie potwierdzić ostateczną wersję, żeby tu nie wprowadzać zamieszania.

**Piotr Buczkowski:** To jest to jeszcze wymyślimy.

**Daniel Reszka:** Okej, znaczy chodzi o to, żeby. Dobra.

**Piotr Buczkowski:** Nie, cisza i tylko powiem, mogę powiedzieć tylko, że raczej według mnie powinniśmy jednak pójść w rozbudowywała AMODIT z wykorzystaniem obecnych struktur AMODIT-owych do przechowywania plików. Żeby nie robić tego też oddzielnie, żeby można było właśnie te takie integracje ze sprawami zrobić w przyszłości. Chcieliście, żebym przemyślał, to przemyślałem.

**Damian Kaminski:** Mhm. Bardzo się cieszymy.

**Janusz Bossak:** To się cieszymy.

**Lukasz Bott:** To pierwsze może jeszcze uwzględnienie jedną rzecz projektując to, bo gdzieś tam ze strony PKF, tak dobrze PKF jest to jakieś zapotrzebowanie, żeby można było przechowywać pliki ścieżkę do przechowywania plików per proces, tak mówiąc, może tutaj gdzieś projektu jest backend, którzy też mieli taką funkcjonalność, może docelowo uwzględnienie. Żeby sobie może uchem, nie wiem czy jest to powiązane, ale skoro pliki to pliki, to rzucam hasło tak.

**Piotr Buczkowski:** OK. Sobie jest sens tak skazać, że ścieżkę dla plików repozytorium.

**Lukasz Bott:** Mielisz.

**Piotr Buczkowski:** Bo jeżeli będzie można podpinać pod sprawy, to i tak nie będziemy przekopiowywać do folderu sprawy. No dobrze, to przemyślano tak. OK.

**Damian Kaminski:** Dobrze, kto następny jest chętny? Mateusz, coś, że ja?

**Mateusz Kisiel:** Tak to mogę pokazać. Przecież.

**Damian Kaminski:** Tak.

**Mateusz Kisiel:** To tak, to doszły w Copilot 2 rzeczy. W Copilot jest teraz opcja, żeby wyeksportować się jakiś plik, na przykład wyeksportuj mi listę procesów związanych z OCR. No i teraz pobierze listę procesów, zobaczyć co daje odpowiedni wynik. Tak, zrobił tej listy tych procesów można pobrać ją w Wordzie albo w Markdown. No i tak to wygląda. Jeszcze jest opcja teraz, że ma dostęp do spraw, właśnie robiłem test pokażę, czyli przykładowo mamy jakąś fakturę? Tutaj akurat. I pytałem o Martins, znaczy widziałem przed chwilą jakąś sprawę, które Sed.com. Takie zapytanie można zrobić: znajdź mi faktury z OCR FAU3, gdzie nabywca to Sed. I teraz wykonuje zapytanie do pobrania spraw z tym filtrem. I dostał jakieś 5 faktur. Tak jak teraz spytać, przejdź do drugiej. I w tym momencie przekierowuje do niej, można sobie zobaczyć nabywcę. Jest Sed.

**Lukasz Bott:** Mateusz, rozumiem, że te zapytanie uwzględnia uprawnienia użytkownika.

**Mateusz Kisiel:** No tak, tak, znaczy na póki co na razie to jest takie, miałem VIP. Docelowo to będzie działało inaczej, przez tworzenie raportów takich tymczasowych. Znaczy ja to widzę. Na razie takie właśnie proof of concept zrobiłem, że można zrobić. No i jeszcze w bilingu doszła opcja podgląd zdjęcia logów z OCR-a, bo wcześniej nie było takich loków i trzeba go przez bazę wchodzić. Na teraz już nie tylko ja to mogę robić, ale na przykład Łukasz jak będziesz chciał tam sprawdzić, ktoś użył albo dlaczego coś nie zadziałało. Można teraz przez stronę wchodzić.

**Lukasz Bott:** OK, dobra, dzięki.

**Mateusz Kisiel:** I zobaczyć co taki był wynik i tak dalej. To na przykład widać, że S2 używa dalej starego OCR-a, bo jest ten jestem wynik taki Azure'owy, czyli nie przerzucili się jeszcze na ten nowy model, który mamy.

**Lukasz Bott:** OK, no tutaj sygnał, nie wiem czy jest zdaniem to dobrze. Jeżeli Jestem zły, jest naszą, nie wiem klientem serwisowym czy coś, to możesz swoich przebić.

**Daniel Reszka:** Ale gdzie przepięć?

**Lukasz Bott:** Ale to. Słucham?

**Daniel Reszka:** Gdzie przepięć?

**Lukasz Bott:** No to znaczy przejąć się ich na ten nowy sposób obsługi.

**Daniel Reszka:** No ale ostatnio przegraliśmy tego, posłuchasz tam jakieś problemy są, to Janek, możecie do ciebie będzie odżywał. Trzeba ustalić, czy to jest na pewno dobry sposób.

**Lukasz Bott:** No dobra, tu się zdzwonimy po.

**Mateusz Kisiel:** Znaczy, ktoś mnie zgłaszał, że brakuje opcji pobrania sobie całego string z OCR do jakiegoś pola, ale okazało się, że tak naprawdę nie jest to potrzebne. Nie chcieli mieć tylko jedną wartość z tego całego stringa, więc robię tego użyć mechanizmu fields. Mam mechanizm to specjalny.

**Daniel Reszka:** Tak, ale tam jeszcze czegoś Mateusz brakuje, to Janek będzie wyjaśniał to z Łukaszem, bo tam jakiś kod się jeszcze pobierał, który nie jesteśmy pewni.

**Lukasz Bott:** Dobra.

**Mateusz Kisiel:** No właśnie wiem, to takie kod po, znaczy oni brali z tego długiego tekstu, to lepiej robić za pomocą address email.

**Lukasz Bott:** Dobra.

**Daniel Reszka:** Znaczy tak, plan jest taki, żeby przepiąć rzeczywiście wszystkich na nowy, więc w tym jest tu też na planujemy.

**Damian Kaminski:** Słuchajcie to.

**Lukasz Bott:** Był tutaj zbędna dyskusja poza to spotkanie, tak, Przemek.

**Janusz Bossak:** Dobra, to panie, dyskusja nad tym.

**Damian Kaminski:** Operacyjne rzeczy.

**Janusz Bossak:** Poczekajcie, Przemek ma jakieś.

**Mateusz Kisiel:** Widzę, że przyjęcie zgłoszenia.

**Przemysław Sołdacki:** Ale wyciąłem, mam tylko jedną uwagę, jak patrzę co mamy w tej bazie, kto gdzie mam przechowam, gdzie są przechowywane bilingi, to my tam zaczynamy przechowywać bardzo wrażliwe dane. Wszystkie dane odczytane z OCR-a, dane związane z tym, co Copilot zachowuje, tam jest mnóstwo danych, które są wrażliwe, mogą być dane osobowe, mogą być jakieś tam tajemnice firm i tak dalej. Dostęp do tej bazy musi być mega chroniony, zarówno jakby żeby ktoś się nie włamał zewnątrz, żeby jak najmniej osób od nas mogło mieć dostęp do tego, bo to są po prostu ekstremalnie wrażliwe dane, tak jak mamy mocno chronioną bazy w TrustCenter, bo tam ciężko, cokolwiek się z tego, tam wszystko jest szyfrowane i tak dalej, a tutaj wydaje mi się, że tak jakby nie, nie składam, nie przyłożyliśmy wystarczająco dużo uwagi dla tego bezpieczeństwa, więc zastanówcie się nad tym, jak to zabezpieczać, bo niektóre, bo dopóki to były dane typu, że firma X przetwarzała ileś tam dokumentów, no to jest luz, ale jak mamy wszystkie dane, co zostało odczytane, z którego dokumentu z OCR-a i to mogło być zarówno faktury, mogą być potencjalni zupełnie inne dokumenty kadrowe i tak dalej, to to musi być bardzo dobrze zabezpieczona baza.

**Damian Kaminski:** Może powinna być do tego jakaś też, to znaczy może jest retencja. A może też powinien być jakiś parametr, który by określał?

**Janusz Bossak:** To jest temat, który trzeba omówić. To jest temat, który trzeba mówić, bo trzeba spełnić jakby 2 rzeczy. Z jednej strony to, co mówi Przemek, czyli bezpieczeństwo, a z drugiej strony rozliczalność w sensie takim, że trzeba wiedzieć i firmy chcą wiedzieć jak działało tam. Ja. Ogólnie rzecz biorąc, tak to akurat OCR, że mówimy, ale...

**Mateusz Kisiel:** Czy?

**Janusz Bossak:** Jeżeli ja gdzieś jest, to trzeba umieć to udowodnić, że to ja i coś tam odczytało tak, a nie inaczej.

**Mateusz Kisiel:** Że co można zrobić to dodać szyfrowanie w bazie danych, tak żeby nie było to zapisane w plain tekście, tylko szyfrowany.

**Janusz Bossak:** Zaparkujemy na razie ten temat i do tego wracamy. Jak najbardziej i to bezpieczeństwo trzeba tutaj absolutnie zapewnić poziomie czy bazy czy pojedynczych pojedynczej firmy. Każda powinna mieć swoim kluczem. Może szyfrowanym trzeba się nad tym zastanowić.

**Przemysław Sołdacki:** To jeszcze tylko jedna sugestia w tym zakresie, bo my dane takie skrypty billingowe musimy u siebie przechowywać, natomiast w wielu wypadkach nie będziemy potrzebowali przechowywać tych wszystkich danych, co się z OCR-a roz przeczytało czy co AI odpowiedziało i mogłoby być tak, że to się zapisuje u klienta w jego bazie, bo to zwłaszcza u klientów premisowych ma sens, że to czy mamy u klienta, u nas nie, u nas tylko zostaje oddany billingowe, na przykład te właśnie wyniki u nas się w ogóle nawet nie są do nas przesyłane. To jakby zmniejsza nasze ryzyko, że ktoś nie wiem od nas wykradł dane, bo wtedy te dane do nas nie dotarł, tylko zostały klienta, więc to jest do zastanowienia, czy gdzieś tam jakąś strukturę w bazie AMODIT zostawić.

**Janusz Bossak:** Mega ważny temat, tak.

**Damian Kaminski:** Tak, może wystarczy zachować tylko nazwę załącznika i CaseID od danego klienta i to jest wystarczające, żeby znaleźć czego to dotyczyło?

**Janusz Bossak:** Możemy kontynuować, jechać dalej. Ten temat już mam. Naprawdę mamy jeszcze trochę temat chyba do omówienia, ale mi się wydaje przynajmniej. Potem możemy dyskusję jeszcze zrobić.


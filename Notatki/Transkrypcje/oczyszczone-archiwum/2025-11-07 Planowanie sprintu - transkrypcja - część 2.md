**Data spotkania:** 7 listopada 2025, 09:01 - część 2

---

**Janusz Bossak:** Już patrzę teraz na to. Moduł repozytorium plików w systemie ma na celu umożliwienie nam – że kluczowe założenia aplikacji – moduł będzie częścią AMODIT – jednak pliki będą zapisywane w tabeli CaseAttachment, tak jak pliki załączone do spraw. Czyli jednak tak idziemy – no dobrze. Powiedziało – dość rewolucyjna zmiana koncepcji w stosunku do tego, co żeśmy początkowo myśleli, ale dobrze. Należy dodać kolumny określające, że dany wpis jest pliki Repositorium, a nie skanem – to też – plik nieprzypisane do sprawy. Będzie wykorzystywana klasa AmodThumbnail – generowanie podglądu standardowo jak teraz. Pliki będą zapisywane zgodnie z konfiguracją załączników – dysku, Blob – przy zapisaniu na dysku struktura taka sama jak obecnie dla skanów – plik, gdzie nie ma – skanowany – tak – czyli podzielony latami. Trzeba tylko zmienić... Nato mi się nie podoba, ale może być – należy dodać...

**Damian Kaminski:** Czemu – dzisiaj – nie podoba?

**Janusz Bossak:** No nie wiem, poczekaj, tak – w pierwszej chwili – należy dodać indeksowanie tych plików – rosyjskim – obecnych – zawartość załącznika do sprawy – termin – niby – no bo...

**Damian Kaminski:** Że struktury nie ma – masz na myśli, tak?

**Janusz Bossak:** No, że struktura – ale zaraz – za nim już – jakby dokończyłem wypowiedź – to w głowie mi przeleciała druga myśl, że ta struktura repozytorium jest zmienna, a nie chcemy bez przerwy przerzucać tych plików, stąd tam...

**Damian Kaminski:** No, przerzucać.

**Janusz Bossak:** Więc niech one sobie leżą w jakiejś tam strukturze.

**Damian Kaminski:** Tylko, że wiesz – tak – jak tutaj jest – taka sama jak obecnie dla skanów.

**Janusz Bossak:** Czy taka sama w sensie?

**Damian Kaminski:** Aha, dla skanów – dobra, to ja skanów nie znam, bo – OK – jest...

**Janusz Bossak:** Była taka funkcjonalność.

**Damian Kaminski:** Tak, tak, tak – wiem, wiem o czym mówisz, tylko nie wiem, jak ta struktura de facto wygląda. O, tak – może to mam na myśli, że nie dam, bo – jak mamy sprawy – to mamy lata i – itd. – jednak to – tu powiedział, to tu mamy lata i ID, powiedzmy, folderu, w którym bezpośrednio jest ten plik.

**Łukasz Bott:** Minister skanów.

**Janusz Bossak:** Znaczy, ja to rozumiem, że to jest taka sama jak obecnie dla skanów, czy nie ta sama, tylko taka sama?

**Damian Kaminski:** Ale – tak, ale co to znaczy, czyli – czyli jaka tak naprawdę, bo tutaj nie jest to zdefiniowane.

**Łukasz Bott:** W sensie konstrukcyjnie – czyli...

**Janusz Bossak:** Latami – latami podzielono.

**Łukasz Bott:** Lata.

**Damian Kaminski:** Ale w sensie – lata i nieskończona ilość plików.

**Łukasz Bott:** Nie, lata – lata – potem obecna struktura dla załączników do spraw jest tak – jest rok...

**Janusz Bossak:** Tak.

**Damian Kaminski:** Poczekaj, poczekaj, Łukasz – tu jest dla skanów, a ja nie wiem, czy to właśnie to jest zbieżne z tym, co ty mówisz.

**Łukasz Bott:** Proces.

**Damian Kaminski:** Bo skany w tym rozumieniu Piotr rozumie jako "Dołącz skan" – taki, co był pod zębatką. Ja nie mam przekonania, że to jest tak jak dla plików ze spraw.

**Janusz Bossak:** No, to nie jest tak – jakby – no pewnie, że nie.

**Łukasz Bott:** Czekaj, bo ja...

**Damian Kaminski:** No a, chyba – a chyba Łukasz to tak próbuje wytłumaczyć.

**Łukasz Bott:** Nie, nie – moment, bo – pytanie jest taki – dobra, ja zrozumiałem – ten sposób – twoje pytanie – dobra – i odpowiadam. W obecnej strukturze, jeżeli chodzimy – jeżeli mówimy o pliki – jeżeli mówimy o strukturę plików, tak – tych dokumentów załączanych do spraw – to to wygląda w ten sposób – jest rok, identyfikator procesu, i potem są już poszczególne katalogi, które mają ID sprawy, tak, i potem już...

**Damian Kaminski:** ID sprawy. Ale właśnie – to ja tak tego nie interpretuję. No właśnie – tak nie będzie – tak nie będzie. Według mnie tu chodzi o inną funkcjonalność – o funkcjonalność skanów, która była jeszcze – chyba – przed dokument...

**Janusz Bossak:** Tak nie będzie i tak nie będzie.

**Łukasz Bott:** Tak – słuchajcie, słuchajcie – macie – czekajcie – macie niejasność, więc albo dzwonimy Piotra, bo jest – bo jest w firmie.

**Damian Kaminski:** W sprawach – trzeba może dzwonić Piotra.

**Janusz Bossak:** Ale ja wiem, ale ja wiem.

**Damian Kaminski:** No to – to powiedz.

**Janusz Bossak:** Ta funkcja – bo ciągle przerywamy sobie w momencie, kiedy mówimy o tym, jak ta funkcja skanów działała, to – żeby wyrównać naszą wiedzę – i nie odzywajcie się nawet – jak ktoś wie – po prostu wypowiem, żeby było wiadomo o czym mówimy.

**Damian Kaminski:** No właśnie – powiedz.

**Janusz Bossak:** Funkcja skanów polegała na tym, że użytkownik mógł skanować dokumenty. I one leciały do takiego – nazwijmy to – wspólnego worka – nie były przypisywane do spraw, nie były pobierane – tak jak teraz przez sprawę od razu i zakładana była sprawa. Czekały w takiej kolejce i była specjalna funkcjonalność pozwalająca na przeglądanie tej kolejki zeskanowanych rzeczy. I z tej kolejki – to nie były sprawy, to były tylko i wyłącznie widoki tych skanów – takie właśnie niby repozytorium – i z tego miejsca można było uruchomić sprawę z wybranym skanem, czyli jakby włączyć – czy uruchomić sprawę – i włączyć ten skan do tej sprawy nowo powstałej, czyli takie ręczne uruchamianie spraw na podstawie dokumentów będących w jakimś katalogu. Tak to działało. Tego nie ma już, ale rzeczy po tym zostały, tak – czyli teoretycznie nadal można tam skanować, ale nikt tego nie będzie widział, bo nie ma w tej chwili w ogóle interfejsu do tego. No i Piotr proponuje wykorzystanie tego mechanizmu, czyli tam będą – w taki sposób, jak były składowane te skany – w taki sposób będą składowane te dokumenty z repozytorium teraz, czyli – po pierwsze – nie będą przypisane do żadnej sprawy. Będą takimi właśnie luźnymi, jeszcze jakby poza-AMODITowymi elementami. I on proponuje, żeby one były w katalogach po latach, czyli będzie główny katalog "Repository", łamana 2025. Jak się zacznie rok 2026 i zaczną wpadać nowe dokumenty, to te nowe wpadną do 2026. To jest tylko i wyłącznie po to, żeby w jednym katalogu nie było tam – nie wiem – milion dokumentów, no – chyba że w ciągu roku milion.

**Damian Kaminski:** No, ale właśnie – to – to nie jest – to się nie wyklucza, bym powiedział.

**Janusz Bossak:** No, to mówię – można to jeszcze dzielić na miesiące, tak – i – znaczy – chodzi o to, żeby była jakaś struktura, a nie jeden wielki wór, tak – teraz tam...

**Łukasz Bott:** Ale to – czekajcie – to...

**Damian Kaminski:** Czyli tak naprawdę wzywając wątpliwości – struktura logiczna w aplikacji – nie – jak będzie się miała do struktury fizycznej na plikach – po prostu to będą rozbieżne zbiory – trudne – lata, a tu na tematy.

**Janusz Bossak:** Tak.

**Łukasz Bott:** O, tak.

**Janusz Bossak:** Tak, tak, ponieważ interfejsem dla użytkownika jest interfejs AMODIT i on tam te pliki widzi. On nie ma zaglądać – to nie ma być dla pani sekretarki, która będzie biegać po dysku i coś tam sobie szukać.

**Damian Kaminski:** Tak.

**Janusz Bossak:** Z punktu widzenia użytkownika w zasadzie nie ma znaczenia, jak my to przechowujemy, tak.

**Damian Kaminski:** No, teraz – z punktu widzenia odtworzenia systemu w innym systemie – to jest bardzo nieuser-friendly. Natomiast czy my musimy to zabezpieczać? Możemy to olać. No – u nas jest tak i tyle, tak.

**Janusz Bossak:** Znaczy – to znaczy – zauważ – to będzie zapisane w tych CaseAttachment – w CaseAttachment będzie link do miejsca, gdzie ten plik leży.

**Damian Kaminski:** W bazie. Mhm.

**Janusz Bossak:** I – tego jeszcze nie wiem, ale gdzieś będzie informacja, w którym folderze tej struktury naszego repozytorium, tej, którą widzi użytkownik – on w sumie ma być pokazany, tak – i to tyle. To składanie 2 informacji – logicznej struktury, którą widzi użytkownik, a system sobie z jakiegoś miejsca, w którym sobie zapisał ten plik, stamtąd to bierze, nie – i tyle. Więc to jest chyba, że – OK – ten podział na te podgrupy typu lata i miesiące według mnie jest OK, tak – to tylko zabezpiecza nas, żeby nie było wszystko w jednym wielkim worku.

**Damian Kaminski:** OK.

**Janusz Bossak:** Równie dobrze można robić, że – jak ten worek ma już, nie wiem, 5000, to zakładamy nowy worek, no – czyli możesz mieć takie "repozytorium łamane" – 0001...

**Damian Kaminski:** To znaczy tylko – tak – tu chyba – jedną uwagę chyba mam, bo tu nie ma nic o nazwie – że wiecie, w tak dużym zbiorze będzie wiele plików o tych samych nazwach – jest takie bardzo duże ryzyko, więc to – czy to znaczy, że my będziemy te nazwy zmieniać na – podpisywać jakimś ID tego konkretnego dokumentu jako prefiksem do nazwy, tak?

**Janusz Bossak:** Pliku. Ale my – on tyle pisze, tak – poczekaj, poczekaj, bo tu pisze jeszcze dalej – to przeczytajmy – nowa kolumna w CaseAttachment – tabela "RepositoryFolder" – struktura folderów – możliwe tworzenie wielu folderów, dalej – tabela "Repository" – połączenie pomiędzy – właśnie to, co mówiliśmy, tak – pomiędzy RepositoryFolder a Attachment – tabela "RepositoryRights" i tabela "RepositoryHistory" – zmiany repozytorium. No dobrze – nie ma – nie ma tej informacji, o której mówisz, czyli potencjalnie istnieje takie ryzyko, że 2 pliki będą miały identyczną nazwę.

**Damian Kaminski:** Tak. Regulamin jednego działu i regulamin drugiego działu i wszystko – i obydwoje nazwał "Regulamin".

**Janusz Bossak:** Będzie "Regulamin.pdf", "Regulamin.pdf" – nie – więc albo my musimy dodawać jakąś tam tak zwaną sól do tego, żeby było zawsze po naszemu – i tak się chyba będzie robiło.

**Łukasz Bott:** W tej chwili to chyba jest dodawany CaseID – no, nie – nie – tylko AttachmentID.

**Damian Kaminski:** Nie – A, tak – a, no tak – masz rację, tak chyba jest, bo można wgrać te same 2 pliki do tej samej...

**Łukasz Bott:** Tak, nawet tej samej sprawy i się nie pogryzą. A tu tego jeszcze tam dochodzi kolejny indeks związany z wersjonowaniem, tak – czyli jak masz jednym kliku...

**Damian Kaminski:** Sprawy.

**Janusz Bossak:** Można zapytać? No – no dobra.

**Łukasz Bott:** Jeszcze do mnie odpowiedni znacznik dla podglądu, tak?

**Janusz Bossak:** To wygląda – coraz bym powiedział – prościej po tym, co napisał Piotr, bo wykorzystujemy – nie wiem – 50% rzeczy, które po prostu mamy już, nie. Parę tabel trzeba dodać i obsługę tych tabel, ale nie jest to robienie – wiecie – kompletnie nowej aplikacji od podstaw – zupełnie. Więc trochę – trochę mnie to uspokaja, co tutaj Piotr napisał. Cieszy mnie, że – że to poszło w tą stronę.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** No i dobra – no, czy teraz trzeba po prostu rozprawić? Robotę – frontend w zasadzie mamy. Pytanie jest teraz – tutaj on napisał w zakresie MVP – podstawowa struktura organizacyjna – przestrzenie, foldery, pliki – system uprawnień tylko dla folderów pierwszego poziomu. CRUD, czyli tam – zapis, odczyt, usuwanie – operacja na strukturze i plikach – przechowywanie fizyczne plus metadane w bazie – no i OK – no, to jest całkiem sensowny MVP numer jeden.

**Damian Kaminski:** Znaczy tu było więcej i Piotr widzę, że to – to wszystko, co było napisane, to jeszcze było przeze mnie wrzucone jako opis, natomiast na chwilę – może przejmę to – albo – Aniu – nikt nie wyświetla – dobra, to żebyśmy widzieli to samo.

**Janusz Bossak:** Mi zerwało cię – zrywa ciągle.

**Damian Kaminski:** Więc, tu jest – zobaczcie – to, co usunął – podstawowe wyszukiwanie po nazwach...

**Janusz Bossak:** Znaczy ja bym z tego zrobił w tym jego wpisie MVP 2 – czy MVP next – i tam powinny być te wszystkie rzeczy – powinniśmy to widzieć – no i co, co planujemy jeszcze i czego nie uwzględniliśmy tutaj, nie.

**Damian Kaminski:** I tu zapisałem, że na razie brak wersjonowania w historii zmian – chyba – no – przenoszenia plików poza zakresem MVP jeden. Przepraszam. Może Piotr założył, że to będzie, bo on tutaj opisał, że mamy indeksowanie takich plików – Lucene. Ja tu jeszcze dołożyłem – nie wiem, czy to zdążyłeś, Janusz, spojrzeć – co właśnie w przyszłości, tak – czyli właśnie przerywanie dziedziczenia, możliwość ustawienia plików jako nieusuwalne, integracja ze sprawami – no i metadane plików, tak – wysoko-poziomowe. Ale to...

**Janusz Bossak:** To jest dalej, no.

**Damian Kaminski:** Raczej jest wszystko – dalej, nie – bo tu nawet Piotr napisał, że w tym swoim opisie, że uprawnienia do folderu na razie tylko dla tych z pierwszego poziomu. Więc to zakładam, że jeśli mamy już tabelę przygotowaną, to będzie można tutaj określić dowolne – jakieś – RAI – to pewnie z odwołanie do folderu, tak – RF ID – tak – RF ID – kiedy będzie można to pewnie w sposób – pewnie rozbudowywać później.

**Janusz Bossak:** No dobrze – znaczy, no mówię – jestem trochę, że tak powiem – uspokojony. Znaczy obawiałem się, że to jest dużo więcej roboty – to znaczy nadal jest dużo, ale zaczyna być widać, że to jest szansa zrobić to w tym czasie – tym bardziej, że już ten frontend – w dużym stopniu mamy, tak – trzeba go będzie połączyć z – więc...

**Damian Kaminski:** Tak, no – pozostaje pytanie właśnie – kogo do tego przypisujemy.

**Janusz Bossak:** Ktoś, kto ma mniej zadań w tym momencie. Każdy może być – tak – nie ma znaczenia – znaczy – każdy, kto potrafi – tak – czyli Piotr, Ania, Łukasz Borowski, Adrian.

**Damian Kaminski:** Znaczy...

**Łukasz Bott:** Jest – zgodził.

**Damian Kaminski:** No, tu się zastanawiam poważnie nad Adrianem, mówiąc szczerze, bo on kończy ten – ten – dzisiaj mówił, że będzie się zapoznawał z jakimiś tam wytycznymi do tworzenia tego frontendu. No, niech się dość sprawnie zapoznaję. Tam nie wchodził w szczegóły, bym powiedział. I chyba Adrian byłby taką osobą dostępną – może pod to – tak czuję, bo – no bo co – to znaczy – nie wiem, jak u Piotra to wygląda. Łukasz jest...

**Łukasz Bott:** Dobra, to czekajcie, bo mamy jeszcze – bo tu mamy tak – WIM – nam się teraz doszedł projekt w LOT – i to jest tak – Łukasz Borowski – no, ja go zaangażowałem, zresztą – tak – jest zaangażowany w te integracje w LOT. Pytanie – jak – i teraz tak – i to są integracje dotyczące UPS, dotyczące...

**Damian Kaminski:** No. Mhm.

**Janusz Bossak:** No tak.

**Łukasz Bott:** Tej – tej – jak się potem okazało – to nie chodzi o rozszerzenie nadawcy o kolejny typ przesyłki, tylko jednak Global Express jako dedykowana firma kurierska. To na razie jeszcze śpię m – tutaj po naszej stronie – i z wdrożeń – musimy ustalić, czy – czy to nie jest jakaś tam część tych – Quest – tak – no bo myśmy tego nie wyceniali – wysyłaliśmy na dawcę, ale to tu bym widział Łukasza w tych integracyjnych rzeczach dla LOT. I dla LOT mamy ten duży temat – AD – i on musi się do grudnia zamknąć – przynajmniej w jakimś tam – no – ustalimy – no – przynajmniej jakieś tam zakresem MVP, tak, no – żeby coś przynajmniej się integrowało – było – no i...

**Janusz Bossak:** Jeżeli ma to robić Łukasz, wszystko – to to Łukasz jest w takim razie zarobiony po sufit, tak – więc on – jeżeli będzie robił i ten UPS – i ten Global Express – i to AD – to do końca roku ma...

**Łukasz Bott:** No – pytanie, czy chcemy Łukasza do AD, czy AD nie – miał robić Adrian – no właśnie.

**Janusz Bossak:** No tak, że – jak Adrian zacznie robić AD...

**Łukasz Bott:** To nie zrobimy repozytorium, no.

**Janusz Bossak:** Kto – to on – zrobili repozytorium jako takiego – tutaj, nie.

**Łukasz Bott:** Nie, no – no właśnie – chodzi o to, że – że w takim razie podzielmy tych 2 kolegów – tak – albo jednego. Jeżeli ja biorę Łukasza do LOT, tak, no – to rozumiem, że robi tematy lotowskie.

**Janusz Bossak:** Może zrobić tak, że te drobniejsze – typu UPS – chociaż trudno powiedzieć, czy one są drobniejsze...

**Łukasz Bott:** A...

**Janusz Bossak:** I ten Global Express dać komuś innemu, a AD – jako duży temat – komuś innemu, tak.

**Łukasz Bott:** No też można tak zrobić – rozdzielić. Tak – znaczy wiecie – z AD – to – to też trzeba się dobrze zastanowić, bo czy przypadkiem nie wystarczy użycie COLA REST API? To znaczy pytanie jest takie – czy chcemy, czy chcemy AD zrobić jako moduł AMODIT – i do tego mamy jakiś tam interfejs, jakiś backend, jakiś zestaw – może funkcji, reguł – i po prostu jest tu tak, jak każdy inny komponent, tak – obsługiwany – czy jako MVP? No, bo skoro jest konkretna specyfikacja REST API tego – do – do tego AD – no, to równie dobrze może to zrobić dział – dział wdrożeń, tak – i wywołując COLA REST, tak, no...

**Janusz Bossak:** To jest bardzo dobre spostrzeżenie, bo zauważcie, że robimy jeden wdrożenie na AD w tej chwili. Jak zacznie to się ewentualnie powtarzać – będziemy mieli drugiego, trzeciego i piątego klienta – to może wtedy warto dopiero robić dedykowane połączenie, tak. Ważne jest...

**Damian Kaminski:** No, to jest alternatywa. Tak – masz rację. Zgadzam się.

**Janusz Bossak:** Tak – ważne jest według mnie rozpoznanie – takie biznesowe.

**Damian Kaminski:** Co – czy to się da tak łatwo – na ile to jest trudno.

**Janusz Bossak:** O co – tak – o co – o co w ogóle chodzi? Znaczy – oprócz hasła, że integracja z AD – to co to znaczy – znaczy – jakie są przypadki użycia? Bo ja jestem ostatnio zafiksowany na ten przypadki użycia. Uważam, że one świetnie opisują rzeczywistość i będę po tym z wami chciał się jeszcze podzielić tutaj moimi spostrzeżeniami z ostatniego tygodnia. Bo to pozwala – to pozwala spojrzeć na zagadnienie, które mamy przed sobą, tak – jak masz przypadek użycia, czyli co klient...

**Damian Kaminski:** Dokładnie.

**Janusz Bossak:** Zamierza...

**Damian Kaminski:** Zrobić – jakie ma dane wejściowe, bo to jest często dla nas nie wiadomo – to ja mam to samo w Aliansie.

**Janusz Bossak:** Tak – żeby – tak, czyli jest...

**Damian Kaminski:** Musimy zrobić.

**Janusz Bossak:** Już dokończę tego, tak – czyli ten użytkownik konkretny – prawie, że z imienia nazwiska – pani Krysia w dziale kancelaryjnym. Co pani robi, pani Krysiu? O, ja muszę wysłać to tam, nie – ale jak to pani robi, nie? Jeżeli tego nie robi teraz – no, bo może jeszcze nie ma – to przynajmniej sobie wyobraża, no bo jednak jest specjalistką od tego. I w jakąś okrężnymi metodami do tej pory może przekazywali dokumenty do tego archiwum, więc co nieco zna się, tak – więc co ona uważa, że powinno być robione? Możemy się dopytać. Ja to właśnie robiłem przy okazji tego JRWA. Wpisałem do GPT, że jesteś specjalistą – archiwistą kancelaryjnym – specjalistą od tam – obsługi kancelarii – i tak dalej i tak dalej – i był tam pytania drążące – zadawałem, tak, no – i w końcu coś tam sensownego – na moją ocenę – wypisał, tak – rzeczywiście – to wrzuciłem do drugiego GPT, który miał to zweryfikować – podobnie będąc specjalistą – i – no – podejrzewam, że jest to tam w 80-90 procentach prawdą, tak – znaczy większą prawdą niż sam znam, no – bo nie znam żadnej innej, więc trudno mi jest ocenić.


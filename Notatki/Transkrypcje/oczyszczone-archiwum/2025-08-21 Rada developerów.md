**Data spotkania**: 21 sierpnia 2025

**Lukasz Bott**: Do tej funkcjonalności dashboard, że to jest kopia, tak. Trudno się mówi.

**Damian Kaminski**: Nagrywam, żeby potem tylko podsumować.

**Lukasz Bott**: To nie wiem, czy co?

**Damian Kaminski**: Włączyłem.

**Lukasz Bott**: Dobra, to jeszcze raz podsumowując, kwestię raportów systemowych. W pierwszej kolejności Ania naprawia ten hotfix. Tak, czyli aby była możliwość wyboru raportu systemowego do dashboard.

**Anna Skupinska**: Muszę też jeszcze leżę w bazie, nie można było edytować tych raportów systemowych. On się tak trochę gubi.

**Lukasz Bott**: Ale to jest kopia.

**Anna Skupinska**: To jest kopia, tylko że problem jest taki, że to jest kopia i kopiuje się, że to jest jako raport systemowy. Ona ciągle ma tę flagę raportu systemowego i system głupieje, bo nie wie co zrobić.

**Lukasz Bott**: OK, dobra i to jest.

**Kamil Dubaniowski**: Ale czy my tak chcemy w ogóle? No bo wtedy tak naprawdę, po co nam ten pojedynczy raport? Czemu od razu nie robimy tych raportów na dashboard?

**Lukasz Bott**: I dobra i to jest w ramach podsumowania.

**Damian Kaminski**: Ja się zgadzam tu z Kamilem.

**Lukasz Bott**: To czekajcie, słuchajcie. Ania naprawiasz hotfix, a druga rzecz jako podsumowanie, ponieważ mamy dyskusję odnośnie organizacji tych raportów systemowych, jak widać szerzej też i innych raportów, to przenieśmy to na odrębną dyskusję do zaplanowania, a tu i teraz naprawmy hotfix, tak żeby...

**Anna Skupinska**: Mhm. Znaczy, tylko że problem jest tak naprawdę z tym hotfixem, i będzie można stosować raporty systemowe. To co zrobić z ich edycją? Czy raczej zrobić, żeby po skopiowaniu już nie były systemowe, żeby można było je dowolnie edytować, czy raczej zrobić, żeby w ogóle nie można ich edytować, żeby zostały systemowe?

**Kamil Dubaniowski**: Kopiować i niech będą zwykłe.

**Damian Kaminski**: Ale z jakiej perspektywy to jest pytanie? Z perspektywy Łukasza czy z perspektywy klienta?

**Anna Skupinska**: Znaczy trochę z naszej, bo jeżeli pozwolimy...

**Kamil Dubaniowski**: Klienta.

**Damian Kaminski**: Nie z naszej. Dobra, to jeszcze raz. Z naszej to powinno być dedykowane środowisko, na którym Łukasz przygotowuje raporty systemowe i wszystko może edytować. Jak ma gotowe, to mówi komuś z was: "są gotowe, a zaktualizowane są te i te. Trzeba tak ustawić teraz definicję, żeby były raportami systemowymi, czy nikt nie może ich edytować w środowisku produkcyjnym?".

**Lukasz Bott**: Dokładnie.

**Damian Kaminski**: Bo to nie mija się z celem. Ty coś poprawiasz. Łukasz coś musi nadrabiać. On musi produkować to jako zwykłe raporty. Następnie daje ci informację: "jest zaktualizowana definicja, trzeba to wydać do wersji". Pobierasz sobie definicję, ustawiasz odpowiednie flagi i wpisujesz je do wersji produkcyjnej.

**Lukasz Bott**: Dokładnie tak. Bo tak to będziemy się wozić z tym.

**Damian Kaminski**: Będziemy zmieniać flagi, żeby Łukasz mógł edytować. Bez sensu.

**Anna Skupinska**: OK, w stosunku do klienta.

**Damian Kaminski**: Jesteśmy to w stanie zaopiekować w ten sposób.

**Anna Skupinska**: I to teraz można edytować raporty systemowe, ale trzeba być w takiej specjalnej grupie, jak się pojawia możliwość edycji.

**Damian Kaminski**: Łukasz musi być w tej grupie.

**Anna Skupinska**: A czy uwierzono, Łukasz, muszę po prostu zrobić zwykły raport i podać jego definicję, i co to da, wystarczy.

**Lukasz Bott**: To.

**Damian Kaminski**: No to już, jak wygodniej.

**Lukasz Bott**: No.

**Anna Skupinska**: Bo chodzi o...

**Lukasz Bott**: Dobrze, to.

**Anna Skupinska**: Mogła.

**Lukasz Bott**: Zadzwonimy się za chwileczkę jeszcze po poradzie.

**Anna Skupinska**: Dobrze, ale jeśli chodzi właśnie o ten hotfix, czy jak kopiujemy raport systemowy, to on ciągle jest systemowy.

**Damian Kaminski**: Podstawowe pytanie jest, czy go można skopiować, czy my chcemy udostępniać klientom?

**Kamil Dubaniowski**: Ja bym tak pod tym kątem, że klient zobaczy, że fajne i na przykład chce to opublikować, bo uznają oni już indywidualnie, że to można puścić szerzej w organizacji.

**Anna Skupinska**: Czy na tym polega hotfix.

**Lukasz Bott**: Tak, tak.

**Damian Kaminski**: Mhm, OK. No dobrze, czyli.

**Kamil Dubaniowski**: Albo kopiują i wręcz chcą go edytować troszeczkę pod siebie, bo może coś im tam nie gra.

**Anna Skupinska**: No właśnie, czyli warto było, żeby ta kopia nie była zaliczona jako raporty systemowe, że można by ją edytować.

**Lukasz Bott**: No.

**Damian Kaminski**: Z poziomu kluczyka powinna być opcja "kopiuj".

**Lukasz Bott**: To tak zrób.

**Damian Kaminski**: Dla raportów systemowych. I wtedy ktoś przechodzi od razu w, jakby ma zaimplementowaną definicję raportu systemowego, do raportu zwykłego.

**Anna Skupinska**: Tak.

**Damian Kaminski**: No to tak trzeba zrobić w tym menu rozwijanym "kopiuj, edytuj" czy coś w tym stylu i wtedy sobie ma już definicję, może przerabiać to jako zwykły raport dalej.

**Anna Skupinska**: Mhm. Czy myślę, że po prostu, ale tak, żeby się od razu kopiowała jako zwykły raport. Było ciężko znaleźć tak, że jak na przykład mamy update, to żeby on nie wyszukiwał nie tylko te raporty systemowe, które są, ale też ich kopie.

**Damian Kaminski**: Nie, nie, nie, Aniu, oczywiście, że nie. On kopiuje stan bieżący. Jak my zrobimy modyfikacje, to my nie wpływamy na te kopie. Absolutnie. On kopiuje stan bieżącej konfiguracji.

**Anna Skupinska**: No właśnie.

**Lukasz Bott**: Nie.

**Anna Skupinska**: No właśnie.

**Damian Kaminski**: Tym bardziej, że oni mogą tam chcieć to przerobić po swojemu, totalnie.

**Lukasz Bott**: Damian. Ale to jak przerabia totalnie, to jest...

**Damian Kaminski**: Nie powinniśmy już wpływać na to?

**Lukasz Bott**: Ale, rozumiem, że chodzi tobie o to, że oglądam jakiś raport systemowy, taki predefiniowany, tak? I powiedzmy, że czegoś mi tutaj brakuje, tak? Coś bym chciał. Właśnie może do tego typu wrzucić.

**Damian Kaminski**: Dokładnie.

**Lukasz Bott**: I co do zasady tego raportu nie mogę edytować, no bo to jest raport systemowy, predefiniowany. I rozumiem, że tutaj dodajemy opcję "kopiuj".

**Damian Kaminski**: Tak.

**Lukasz Bott**: I on przychodzi.

**Damian Kaminski**: Kopiujemy taki, jaki jest na dzień dzisiejszy.

**Lukasz Bott**: Tak i sobie.

**Damian Kaminski**: I on zostaje moim raportem. Cokolwiek mogę z nim zrobić, opublikować, zostawić sobie. Jak my zredefiniujemy definicję "attachment statistics", to to ma wpływ tylko na raport systemowy "attachment statistics". I jego kopia zostaje taka, jaka była na podstawie tej wcześniejszej definicji. Jak on stwierdzi: "O, fajną rzecz wprowadzili i nie chce tego sam wyklikać", robi kopię sobie drugi raz.

**Lukasz Bott**: Dokładnie. Dokładnie tak.

**Kamil Dubaniowski**: Tam jest już chyba taka opcja, żebyśmy nie tworzyli nowej, chyba "zapisz jako".

**Damian Kaminski**: Tylko on nie może wejść w tryb edycji, Kamil. Ale można by ją wtedy tu, do tych raportów, wyciągnąć. Funkcjonalność jest, tylko trzeba by może ją inaczej nazwać, żeby to było zrozumiałe dla administratora. Kamilowi chodzi o to, że jak wejdziesz na inny dowolny raport, to jest "zapisz jako" i wtedy zapisuje ci się cała definicja. Tylko tutaj musiała być trochę inna funkcjonalność tego przycisku, bo ona musi zmienić tamte flagi, tak, że to już nie jest raport systemowy.

**Lukasz Bott**: Czekajcie, bo to jest stan.

**Damian Kaminski**: Myślę, że już Ania sobie z tym poradzi. Jak wejdziesz w "edytuj", o to chodzi Kamilowi, to tu jest strzałeczka pod "zapisz" i możesz zrobić "zapisz jako". Na górze. I jak to zrobisz, to zapisuje ci się definicja kopii, tylko w systemowych musi być to wyciągnięte na tę warstwę wcześniejszą, tak, odczytu.

**Kamil Dubaniowski**: To jest tak naprawdę kopia, tak?

**Lukasz Bott**: Dokładnie.

**Kamil Dubaniowski**: Zastanawiam się, czy faktycznie tak, czy nie lepiej te systemowe zablokować pod kątem zmiany. Nie wiem, widoku, te wszystkie zakładki takie podstawowe. Bo czemu admin nie zdecydowałby, że ten raport systemowy jednak udostępni wszystkim kierownikom? Bo to są statystyki z procesów, które oni opiekują i coś tam, coś tam. Że, jakby, zablokować opcję edycji, że nie można zmienić definicji, ale wejście w ustawienia jest ograniczone właśnie tylko do tworzenia swojej wersji, do kopiowania i do udostępniania.

**Lukasz Bott**: No właśnie.

**Kamil Dubaniowski**: Cały lewy panel jest zablokowany.

**Damian Kaminski**: Ale to według mnie to jest chyba bardziej skomplikowane niż wyciągnięcie tego tutaj, bo możemy kliknąć.

**Kamil Dubaniowski**: Tak, tylko że chroni nas troszeczkę przed niepotrzebnym tworzeniem kopii. Bo teraz będzie taki case, że chcę to udostępnić dalej. To muszę zrobić kopię.

**Damian Kaminski**: No dobra, to wyciągamy przycisk "udostępnij" też na tę listę dla raportów systemowych. Nie blokujemy tam, tylko tu jest przycisk "udostępnij" dla admina i on ma to samo co w edycji raportu. Wydaje mi się, że to będzie prostsze, bo wtedy tylko mamy tu model wyświetlić.

**Lukasz Bott**: Chodzi ci o to, tak, żeby to "udostępnij" było dostępne.

**Kamil Dubaniowski**: Nie wiem, czy wyciąganie jest prostsze niż zablokowanie, albo wręcz ukrycie tego lewego panelu w opcji edycji raportu systemowego.

**Damian Kaminski**: Tak.

**Kamil Dubaniowski**: Żebyśmy nie tworzyli, wiecie, nowych ścieżek. Ścieżka będzie zawsze ta sama, tylko tu mam na przykład cały ten lewy panel wyłączony, czy wręcz nie widoczny.

**Damian Kaminski**: No, lewy panel ograniczyć zakres też tak.

**Kamil Dubaniowski**: No tak, bo tam mogą być jakieś Łukasza filtry, których nie powinien naruszyć. No i to grupowanie po folderach już mniej tragiczne. Ale pewnie wypadałoby też.

**Lukasz Bott**: Nie, to wszystko wyłączyć.

**Damian Kaminski**: Wszystko by trzeba było w zasadzie. Byłby dostępny tylko przycisk "udostępnij", bo "zapisz" też nie może nadpisać go. Więc pytanie, czy jest sens długo wpuszczać i sprawdzać, czy na pewno jest wszystko zablokowane. Nie wiem co jest prostsze, niech oceniają deweloperzy.

**Lukasz Bott**: Tutaj jestem w trybie podglądu. Dla systemowych zamiast "edytuj" mam opcję "kopiuj", tak, czy "zrób kopię tego raportu". I wtedy on przechodzi w tryb zwykłego raportu, i co ja sobie z nimi zrobię? I łatwiej jest. Tak skopiowane i tak.

**Damian Kaminski**: Jakiś raport, jak chcesz udostępniać, to sobie skopiuj sobie i udostępnij.

**Lukasz Bott**: Dokładnie.

**Damian Kaminski**: Dobra, to tak zostawiamy. Dla systemowych nie ma funkcji "edytuj", tylko jest funkcja...

**Lukasz Bott**: Utwórz kopię.

**Damian Kaminski**: Skoro "utwórz kopię" i wtedy może na tej podstawie sobie budować go jako zwykły raport, ale ma wstępnie wczytaną definicję raportu systemowego.

**Lukasz Bott**: Tak jak on był oryginalnie tam skonfigurowany.

**Damian Kaminski**: Dobra, co do tych filtrów na stronie głównej raportów, ja bym to jeszcze skonsultował z Przemkiem. Więc dzisiaj mamy okazję, mamy popołudniu z nim spotkanie, więc przedyskutujemy i wrócę, Łukasz, z informacją albo stworzymy jakiegoś PIA.

**Lukasz Bott**: Dobrze, tak na te systemowe. Dobra, tego PIA nie robić.

**Kamil Dubaniowski**: Wydaje mi się, że po prostu powinniśmy dodać kolejną sekcję tak jak jest "ulubione". Byłyby systemowe i na dole wszystkie. Wtedy admini tylko widzą te systemowe. Jak nie chcą, to sobie wyłączą je w filtrach i znikną, i w ogóle cała sekcja.

**Lukasz Bott**: Albo sekcję dokładnie.

**Damian Kaminski**: Tak. OK, no dobra, ja bym tutaj tak przegadał. Dobra, to jest jakiś pomysł, z którym może i ja się zgadzam, nawet na pierwszy rzut oka, ale niech to Przemek zaakceptuje. Bo wiesz, to on miał najwięcej tutaj aluzji do tego widoku, nie, że on co chce widzieć, czego nie chce widzieć, więc żebyśmy się zaraz nie wycofywali.

**Lukasz Bott**: Nie, mamy.

**Kamil Dubaniowski**: Przemek głównie naciskał na te filtry właśnie typu i to wcześniej zrobiła wręcz w zakładkach na górze. Tylko że później weszliśmy w taki koncept, że to są jednak sekcje tak jak tutaj, a wcześniej były zakładki. Przemek chciał jeszcze właśnie "moje, udostępnione dla mnie", tak. Ale to można wszystko przełożyć na filtry. Zamiast robić zakładki, to zrobić filtry, a po prostu jako osobną sekcję dać te systemowe. Wiemy, że tam admini będą w innym kontekście z taką pracą.

**Damian Kaminski**: OK.

**Kamil Dubaniowski**: Bo ulubione, czemu nie dać dodać sobie na przykład systemowych do ulubionych? No można tak, to jest zupełnie niezależne od siebie, a chcemy wydzielić te systemowe. Ja bym raczej nie stawiał na wydzielanie folderem, bo to nie do tego było. Raczej miały grupować tematycznie te raporty, powiązane ze sobą.

**Lukasz Bott**: Znaczy, wiesz, te foldery przede wszystkim sam mechanizm folderów jest dosyć ułomny, tak jakby patrząc z perspektywy czasu, bo to wymaga zarządzania jakimś tam słownikiem, tak, czy dwoma słownikami. I w tym momencie jak ktoś popił kategorię związane z tymi system reports, czy raporty systemowe, tak, to rozjeżdża się cały ten mechanizm. Tak, grupowanie tych raportów systemowych. To, że one tam technicznie mają jakąś flagę w bazie danych, to dobrze, tak, ale...

**Kamil Dubaniowski**: Ta flaga służyłaby do wyciągnięcia ich poza nawias zwykłych raportów, do osobnej sekcji, a folderów OK, jak ktoś sobie pozmienia nazwy tych folderów systemowych, to sobie namiesza, ale cały czas jest flaga, że to jest raport systemowy i będzie tam osobno w innej sekcji.

**Lukasz Bott**: Dokładnie. OK, dobra, to macie jakieś spotkanie z Przemkiem. Pytanie jest takie, czy robić PIA na to "kopiuj raport"? Bo co do tego chyba jesteśmy zgodni.

**Damian Kaminski**: Tak.

**Lukasz Bott**: Dobra, to ja to zrobię. Czyli jeszcze raz podsumować. Ania naprawiasz hotfix, tak, żeby się dało to coś tam zrobić. Ja robię PIA na...

**Anna Skupinska**: A też zauważam, że w innych miejscach Łukasz mógł edytować raporty systemowe. Nie jestem pewna, kiedy się to popsuło, ale można edytować i się zapisują. Oczywiście jak się jest update bazy danych, to się wszystko pozmienia z powrotem, ale można edytować teraz, więc muszę to teraz pewnie naprawić w ramach tego zadania.

**Lukasz Bott**: Połącz tak.

**Anna Skupinska**: Tak to posiadać głównie sprawdzane po stronie backendu. Jeżeli jest coś co ma znaczenie dla systemu, to żeby tego nie nadpisywał.

**Lukasz Bott**: Dobra. Czyli ja robię ten PIA. Panowie z Przemkiem dyskutujecie odnośnie prezentowania raportów systemowych na liście, czy w formie zakładek, filtrów, czy nowej sekcji. To już tam jak zdecydujecie. Chyba będzie najszybciej. Ja to zdejmuję z agendy. Nie wiem czy mamy jeszcze, znaczy, mamy kilka minut na przedyskutowanie.

**Damian Kaminski**: Jest jeszcze temat repozytorium. Dostaliśmy wytyczne, ale są nietrywialne.

**Lukasz Bott**: To wiesz co, to nietrywialne i pewnie nie wiem czy w takim gronie do przedyskutowania i być może na odrębne spotkanie i takie eksperckie.

**Damian Kaminski**: Nie starczy nam czasu.

**Lukasz Bott**: Czyli.

**Damian Kaminski**: Dobra, wrzucę to Januszowi, żeby się zapoznał i wrzucę to na ten nasz kanał.

**Lukasz Bott**: Czy z tych tematów, które pokazujesz, coś jest pilnie do przedyskutowania?

**Kamil Dubaniowski**: Kluczowe powiadomienia, to jest chyba wymóg.

**Piotr Buczkowski**: Tyle, ile ja tam zaznaczyłem. Ja tam zaznaczyłem jeden, nie wiem czy to widać, ale logowanie wszystkich maili, tak.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: Zastanawiam się, potem zaczęłam to jakby tak próbować robić. Pytanie jest, jako na przykład, że jest mail wysyłany do grupy. Rejestrować jeden mail do grupy, czy powiedzmy pięć maili, że jest pięć członków grupy.

**Lukasz Bott**: Wiesz co, chyba...

**Damian Kaminski**: Bo nie znamy stanu grupy.

**Lukasz Bott**: Tak, grupa może się zmienić w międzyczasie. Więc ja bym rejestrował per osobę, do której to idzie.

**Piotr Buczkowski**: No to.

**Damian Kaminski**: Czy dałoby się dojść? Bo jest historia grupy. Ale to strasznie trudne do...

**Piotr Buczkowski**: Czy jeden wpis, czy wiele wpisów.

**Damian Kaminski**: Analizy. Raczej wiele.

**Lukasz Bott**: Wiesz, no.

**Piotr Buczkowski**: Może trochę baza puchnąć.

**Lukasz Bott**: Może puchnąć, ale to znaczy tak. Jeżeli miałby być jeden wpis z rozdzielonym tam przecinkami adresami mailowymi do kogo to poszło versus pojedyncze wpisy, tak, no to tutaj popatrzmy też znów pod kątem trochę późniejszego, ewentualnie jakiegoś raportowania, tak? Jeżeli będą pojedyncze wpisy, pojedyncze maile, no to łatwiej będzie to chyba przefiltrować, bo chciałbym zobaczyć maile wysyłane do konkretnego użytkownika.

**Damian Kaminski**: Chyba, że no, pytanie czy nie wiem, jeśli do grupy, to dodatkowa kolumna, w której byśmy przechowywali wtedy skład tej grupy, czyli adresy mailowe odbiorców tego powiadomienia. Ale to...

**Piotr Buczkowski**: Znaczy, nie. To bardziej po prostu bym zawsze przechowywał listę odbiorców, tak?

**Damian Kaminski**: Mhm. OK, w sensie. Dobra, mogłoby być tak, że odbiorca to nie jest pojedynczy adres mailowy, tylko wtedy robimy jakimś kontekstem, wyszukanie. Ale to już optymalnie, to ty zarządzasz, co jest lepsze. Ale nie musiało być tak, że każdy wpis jest odrębny, jeśli te maile by wyszły. No właśnie, tylko wtedy pytanie, co jeśli jest do grupy? Jak ktoś ma ustawione, że to powiadomienie wychodzi raz dziennie, tak.

**Piotr Buczkowski**: W sumie masz rację, rzeczywiście, o tym nie pomyślałem. Raczej powiedziałbym, że będzie oddzielnie.

**Damian Kaminski**: Mhm.

**Piotr Buczkowski**: Bo tak naprawdę to jest wysyłane ileś tam maili, tak, oddzielnie dla każdego.

**Damian Kaminski**: Tak, zgodnie z ustawieniami konta.

**Piotr Buczkowski**: Tak. OK.

**Lukasz Bott**: Czyli będzie tym, no wiesz, Piotr, jest jeszcze ta dyskusja, czy właśnie, bo powiedziałeś ten wątek związany z puchnięciem bazy danych? Tak, no to mamy kilka takich różnych tabel, które powodują puchnięcie tej bazy danych. Nie wiem, jakiś system logi z monitora tego wydajności czy coś, ale to znów dyskusja troszkę taka.

**Piotr Buczkowski**: Ale system logów jest czyszczony, tak, w każdym.

**Lukasz Bott**: Wiesz, system logiki czyszczony to wiesz, fiction też są. Czy ta kolejka też jest czyszczona? Tak, ale chodzi mi o takie generalne, tak, ogólnie, czy przypadkiem?

**Piotr Buczkowski**: Nie, to po to, po to tam logowanie jest włączone czy wyłączone na życzenie, żeby klient wiedział tak, że sorry, tutaj będzie dużo danych, może nie wszystko chcesz logować.

**Lukasz Bott**: OK. Że mówisz o tym mechanizmie, co teraz tak pokazujesz?

**Piotr Buczkowski**: Tak, to jest ten mechanizm, to jest ten mechanizm śledzenia wejścia, pobrania dokumentu czy coś. To jest ten sam mechanizm, zostanie rozbudowany o dodatkowe zdarzenia.

**Lukasz Bott**: Że on będzie. Jasne. OK, ale muszę sobie świadomie je włączyć, tak?

**Damian Kaminski**: Tak, to nie będzie domyślnie włączone. Jak wejście w sprawy nie jest domyślnie logowane, a jak włączysz, to będzie. I tak samo to.

**Piotr Buczkowski**: Tak.

**Kamil Dubaniowski**: Tak ten proces.

**Lukasz Bott**: Jasne, dobra. Dobra. Wiesz co, tutaj jeszcze bym dopisał "Tempora Reacts" do tej listy.

**Damian Kaminski**: Dla maili.

**Piotr Buczkowski**: Możemy rozbudowywać. To na razie chciałbym.

**Damian Kaminski**: Nie, oni na razie nie korzystają z brandem polary.

**Piotr Buczkowski**: Tak.

**Lukasz Bott**: Dobra, bo to rozumiem po podwin jest tak.

**Damian Kaminski**: Podwin, tak, te.

**Piotr Buczkowski**: Tak.

**Kamil Dubaniowski**: O takie GTA w ogóle jest do przemyślenia rozbudowy, bo trochę nie da się tym zarządzać, wydaje się. Aktualnie nie wiemy komu co.

**Lukasz Bott**: To znaczy, GTA tak jest. To jest GTA, to po pierwsze problem jest. Nie ma interfejsu, bo to jest odrębna tabela, tak. Dostępu nie ma interfejsu, chociażby nawet takiego w trybie read-only, żeby sobie sprawdzić, kto, kto do jakiej sprawy, od kiedy, do kiedy ma dostęp.

**Kamil Dubaniowski**: Dokładnie.

**Damian Kaminski**: To jest zgłoszenie miesiące z LP, ale na razie nie cisną, więc zostało jak jest.

**Lukasz Bott**: To trzeba było chyba zrobić w ogóle tak.

**Damian Kaminski**: Tak, trzeba będzie to zaopiekować.

**Lukasz Bott**: Odrębny jakiś taki mechanizm do zarządzania tego, może właśnie później nie wiem, możliwość właśnie wyłączania dostępu takiego, że...

**Kamil Dubaniowski**: Odbioru dostępu takiego na życzenie. Tak, nie wiem, pomyłka czy cokolwiek innego.

**Lukasz Bott**: Nie wiem, ktoś. Tak.

**Damian Kaminski**: Znaczy, wiecie, jest ta opcja tylko z poziomu każdej sprawy, więc nie ma takiego przeglądu, żeby ktoś mógł wejść i zobaczyć: "o kurde, a tu komuś wisi dostęp pół roku".

**Lukasz Bott**: No, ale.

**Damian Kaminski**: I czy powinien wisieć? No tak, w zakładce użytkowników trzeba było dodać taką dodatkową zakładkę właśnie "dostęp jednorazowy" zainstalowany wszystko.

**Lukasz Bott**: I.

**Kamil Dubaniowski**: No pewnie RODO, który ratuje.

**Damian Kaminski**: To jest nawet pod kątem RODO, bo wiecie, są kandydaci wyrażają zgodę na obsługę, potem wysyłają powiadomienie, że proszę usunąć nasze dane.

**Lukasz Bott**: No tak.

**Damian Kaminski**: Na razie mamy to niezaopiekowane. Ale Adecco jakoś tego pilnie nie przestrzega, bo oni najwięcej chyba z tego korzystają, więc póki co wisi. Może się, może nie trzeba podsunąć pomysł, że odpłatnie im to zrobimy.

**Kamil Dubaniowski**: Lepiej nie, powiedzą: "o jeszcze nie macie takich rzeczy".

**Lukasz Bott**: Tak będzie.

**Damian Kaminski**: Przestań, tam umowy niepodpisane, zarchiwizowane. Ja ich ponagrałem, mówię: "wiecie, to wasza sprawa, ale tak, żebyście mieli świadomość". Może już się zmienił trochę skład i nie przeszła ta informacja, o której ja mówiłem, że to, co jest w zakładce "niepodpisane" i jeśli to raczej powinniście usunąć ze względu na RODO. Ale to tam ze swoim inspektorem, bo tam wisiało, wiesz, tysiąc spraw sprzed dwóch, trzech lat. Ale to ich sprawa, więc tam nie ma takiego ciśnienia. Powiemy to, nagle wyskoczy, że dlaczego tego nie mamy. Raczej podziękuję za sugestię.

**Lukasz Bott**: To Piotrek, tak, wiesz co tam zrobić? Tak, czy rejestrujemy per osobę, tak.

**Piotr Buczkowski**: Tak, tak.

**Lukasz Bott**: Dobra to zjem.

**Piotr Buczkowski**: To będzie łatwiej, bo po prostu na SendMail będzie rejestracja.

**Lukasz Bott**: Tak, i. Trudno będzie kolejna.

**Piotr Buczkowski**: Na sat, may composer, czy tam jak się nazywała teraz, zbiera te odroczone, jakby tak.

**Damian Kaminski**: Mhm.

**Lukasz Bott**: Dobra, słuchajcie, przynajmniej formalnie czas nam się kończy. Nie wiem, czy coś jeszcze dyskutujemy.

**Damian Kaminski**: Zostawiamy na dzisiaj resztę.

**Lukasz Bott**: Nie ma nic, nie ma nic z tego takiego pilnego, wymagało jakoś.

**Damian Kaminski**: Przejdzie na kolejny sprint.

**Lukasz Bott**: Dobra.

**Anna Skupinska**: Co do tych, co rozmawialiśmy o raportach systemowych, to już jakby zostało wprowadzone, bo w sumie musiałam tylko zmienić parę rzeczy w bazie danych. Może jeszcze stosować.

**Lukasz Bott**: A gdzie mogę to przetestować na deweloper?

**Anna Skupinska**: Tak, na deweloper. Bo okazuje się, że jak dashboard i kopiują raporty, to nie kopiują ich właściwości "rep system", więc wszystkie skopiowane raporty systemowe stają się niesystemowe od razu. I też patrzyłam, że fakt, i wszystkie osoby, które mają odpowiedniej grupie, która się nazywa "system Report managers", to oni mają automatycznie zrobione, że mogą edytować wszystkie raporty systemowe. Tam się trochę pomyliło, że czemu każdy użytkownik może, ale nie ma tego zabezpieczenia. Więc jedyne co potrzebowałam zrobić to po prostu zmienić, żeby "rep lock" było w bazie danych na zero i teraz będzie pomijać, bo już pokazywać.

**Lukasz Bott**: Żeby można było wybierać raporty systemowe, na dashboard.

**Kamil Dubaniowski**: To teraz jeszcze to, co Ania powiedziała. Może jak klient poczuje taką potrzebę, że chce robić kłopotu, w ogóle roboty nie mamy, tylko admin po stronie klienta zostanie dodany do takiej grupy. Niech sobie wtedy, na własną odpowiedzialność. Świadomie my mu mówimy, że możesz kopiować, ale pamiętaj, rób kopie, rób na swoich kopiach, bo jak przyjdzie aktualizacja systemu, to my te systemowe nadpiszemy.

**Damian Kaminski**: Jak najbardziej możemy też pójść w tę stronę. Tak jak mówisz, nie ma roboty.

**Kamil Dubaniowski**: Mało kto spodziewał się, że będzie chciał w ogóle te systemowe ruszać. Narobimy się niepotrzebnie.

**Damian Kaminski**: Możemy z tego zrobić nagrywane. To jest, można z tego zrobić krótki artykuł, tylko wtedy, jak rozumiem, trzeba stworzyć grupę, która jest obsługiwana natywnie, ale niezdefiniowana.

**Kamil Dubaniowski**: Tak. Jest ona już jest stworzona.

**Anna Skupinska**: Tak, więc jeśli chodzi o tę grupę, to zależy tylko od nazwy. Jeśli jest nazwa, co się nazywa "system Reports Managers" i ktoś do niej zostanie włączony, to może tworzyć raporty systemowe. Nie jest to super mega zabezpieczone, ale...

**Damian Kaminski**: No właśnie. Ona jest obsłużona tak jak "emploi" w rolach, tylko trzeba ją zdefiniować w instalacji.

**Kamil Dubaniowski**: No i tyle, moim zdaniem. Trzeba dodać. Tak, ja bym chyba w tym kierunku szedł. Po prostu wtedy taki admin ma świadomość, że te są nadpisywane przy każdej aktualizacji i po prostu musi robić z sercem.

**Damian Kaminski**: Jestem za. A możemy nawet, Kamil, powiedzieć jeszcze inaczej. W nosie mamy, czy ma świadomość. Jak powstanie artykuł, który będzie to opisywał, że tak to działa, to nikt nie może mieć do nas pretensji. Tylko warunek, że musimy. Ale nagrywamy to, więc zaraz mogę poprosić Copilota, żeby z jego ostatnich pięciu minut zrobił notatkę i możemy to wrzucić, i mamy gotowca.

**Lukasz Bott**: Czyli na czym stanęło?

**Damian Kaminski**: Czyli.

**Kamil Dubaniowski**: Że nawet nie dodajemy tej opcji "kopiuj", tylko dla klientów chętnych, którzy będą chcieli tymi systemowymi jakoś zarządzać, robić swoje wersje, po prostu podajemy instrukcję: "Dodajcie sobie taką grupę, dodajcie ludzi, którzy mogą tym zarządzać i zarządzacie, ale...".

**Anna Skupinska**: Ale nie tylko co. Chodzi o to, że bardzo prosto zrobić, że można było filtry dodawać jeszcze do dashboardów. Bo teraz dashboardy nie dają się tylko dlatego, że "rep lock" nie jest ustawiony w nich na "null". Jak się ustawi na zero, że nie są zablokowane, to wtedy można je po prostu w dashboardach normalnie używać. Jak się kopiują do dashboardów, to się kopiują jako niesystemowe. Ta flaga, że jest systemowy, się nie kopiuje.

**Damian Kaminski**: No to trzeba ją skopiować.

**Anna Skupinska**: Czy na pewno? Tego, że jeżeli będziemy kopiować, to one nie będą dalej aktualizowane i nie można ich edytować.

**Damian Kaminski**: Aha, OK, dobra, nie, nie, dobra, masz rację, po kopi można to olać. Tak, tak, tak, bo to tak jak "zapisz jako" będzie działać. Już wtedy tworzymy niezależną instancję. OK, dobra.

**Anna Skupinska**: Tak.

**Kamil Dubaniowski**: Dokładnie ktoś.

**Anna Skupinska**: Ale tak.

**Damian Kaminski**: To tylko pozostanie później, jak Łukasz to teraz zrobi pod siebie, że po kopiuje do dashboardów, to na tych trzeba będzie poustawiać, że one są zablokowane w celu aktualizacji. Natomiast potem ta funkcjonalność, tak jak działa, powinna pozostać.

**Anna Skupinska**: Mhm.

**Damian Kaminski**: Tak.

**Anna Skupinska**: Ale ogólnie rzecz biorąc, jakby dane do aktualizacji ręcznie, bo jest taki plik, w którym są dane raportów systemowych. Ja muszę ręcznie wkleić definicję, która została stworzona z bazy danych, do tego pliku.

**Damian Kaminski**: OK.

**Lukasz Bott**: No moment.

**Anna Skupinska**: Jest już zdążę po prostu, że on stworzy jakikolwiek raport i tam jego definicję i będę go zrobić, żeby był systemowy.

**Damian Kaminski**: No to Łukasz testujesz to, tak?

**Anna Skupinska**: Jak jesteś w tym, to jest raport systemowy, tak?

**Lukasz Bott**: Na pewno jest to nawet systemowym.

**Damian Kaminski**: Ale tam miałeś ołówek, wrócić na ekran listy.

**Kamil Dubaniowski**: Taka była na tym.

**Damian Kaminski**: Bo może tu jest, tu nie ma. W jednym masz, w drugim nie masz.

**Lukasz Bott**: Jak w jednym mamy, w drugim...

**Kamil Dubaniowski**: W nowych masz. Ogólnie jest tak. To akurat nie jest zależne od...

**Damian Kaminski**: Raport według kategorii nie masz?

**Kamil Dubaniowski**: Tego, że to są systemowe. To, że ten ołówek jest tutaj, jest zależne od tego, że tylko dla nowego modułu raportowego mogliśmy.

**Damian Kaminski**: Jest ta opcja.

**Anna Skupinska**: Tak, więc jak klikniesz jeszcze raz "zapisz", to powinno skończyć się niepowodzeniem. Jeżeli nie jesteś w tej grupie.

**Kamil Dubaniowski**: Ale jest Łukasz.

**Damian Kaminski**: Nie, jest w tej grupie, bo wszedł w ogóle w edycję.

**Anna Skupinska**: Znaczy, ja się.

**Lukasz Bott**: I się.

**Kamil Dubaniowski**: Określi przez błędem.

**Lukasz Bott**: Bo się nie da.

**Anna Skupinska**: Ale jak już "zapisz", to się powinno skończyć powodzeniem, czy nie?

**Lukasz Bott**: Dobrze, czekaj.

**Damian Kaminski**: Ale on jest w tej grupie.

**Lukasz Bott**: Dobra, nie wiem, moment, moment, moment. Dobra, czekajcie po kolei.

**Anna Skupinska**: Czy.

**Lukasz Bott**: Bo ja w tej chwili sobie dodałem taką grupę. Dobra, dobra, moment, nie moment. Pierwsza rzecz, ja się usunę z tej grupy i zobaczmy, co się, jaki będzie efekt. Wchodzę w raporty systemowe.

**Anna Skupinska**: Mhm, tak, i jeszcze się doda. I OK, jesteś w tej grupie, więc możesz edytować raport systemowy. Mhm, mhm. To powinien być w nich nawet ten ołówek, taka potrzeba na kod, że on jest.

**Lukasz Bott**: Dobra, jest ołówek, tak.

**Anna Skupinska**: Edytuj. Jeszcze raz "zapisz". To powinna się skończyć niepowodzeniem.

**Lukasz Bott**: I.

**Anna Skupinska**: Bo nie jesteś w grupie.

**Kamil Dubaniowski**: To nie to, moim zdaniem to jest zrobienie.

**Damian Kaminski**: Ale to.

**Kamil Dubaniowski**: Nie powinno być tego ołówka.

**Damian Kaminski**: To nie jest błąd, to powinna być informacja. Po pierwsze, ołówka nie powinno być.

**Lukasz Bott**: No jest. Też mi się tak wydaje.

**Anna Skupinska**: Mhm, mogę tak zrobić, że nie będzie ołówka, tylko...

**Kamil Dubaniowski**: Czekaj, czekaj, czekaj, Łukasz, wejdź w widok i dorzuć coś do tego raportu.

**Anna Skupinska**: Możesz go zmienić, jak chcesz, ale ci się nie zapisze.

**Kamil Dubaniowski**: No to i tak niedobrze, bo mogę jakieś dane.

**Lukasz Bott**: Dobra. To dobrze.

**Kamil Dubaniowski**: Nie, i tak nie wiem nawet, czy opcję kopiowania.

**Lukasz Bott**: Dobra, dodałem filtr, tak. Zapisz.

**Kamil Dubaniowski**: OK. Nie, tu nie ma ryzyka, bo i tak będę mógł sobie kopiować te raporty, więc i tak będę mógł coś tam więcej wyciągnąć z nich, jak będę chciał.

**Anna Skupinska**: Jak jeszcze raz "zapisz jako" coś się uda. No "zapisz jako" się udaje. I to już nie jest systemowy. Znaczy, on jest jakby w tych kategoriach, w tej samej co są raporty systemowe.

**Damian Kaminski**: Kliknij teraz "zapisz". Po prostu "zapisz".

**Anna Skupinska**: To już się powinno udać, bo nie powinien go zapisać. A nie, OK, więc "zapisz jako" kopiuje też tę flagę systemowego, to trzeba to zrobić.

**Lukasz Bott**: Ale po pierwsze, nie skopiowało się do żadnej kategorii. Została stara nazwa, a nie ta, którą nadałem.

**Anna Skupinska**: Tak.

**Lukasz Bott**: Kultu.

**Kamil Dubaniowski**: Że się nie skopiował do kategorii? Nie, pewnie gdzieś tam na wierzchu.

**Damian Kaminski**: Nie jest nazwa, bo to Łukasz jest trochę też popieprzone.

**Kamil Dubaniowski**: Ale nie przekierowało Łukasza po zrobieniu kopii. Został w starym.

**Damian Kaminski**: Dokładnie, dokładnie. Te "zapisz jako". Ja zawsze po "zapisz jako" wychodzę do początku i wchodzę jeszcze raz. To trzeba było też zaopiekować, że "zapisz jako".

**Anna Skupinska**: Aha.

**Damian Kaminski**: Nie wiadomo, gdzie my jesteśmy po wykonaniu "zapisz jako", czy na starym, czy na nowym. A według mnie powinniśmy być już raczej na nowym.

**Lukasz Bott**: No właśnie. I to jest, wiesz co, to się.

**Damian Kaminski**: Powinniśmy zostać przeładowani w nowy raport i tyle.

**Kamil Dubaniowski**: Mhm.

**Lukasz Bott**: To, co powiedziałeś dla mnie?

**Anna Skupinska**: OK. Trzeba parę poprawek dla "zapisz jako" systemowymi.

**Lukasz Bott**: Dobra, ale to, co Damian powiedziałeś, to właśnie tego typu efekty są też i w dashboardach. I ten, że właśnie w kilku miejscach coś właśnie takie typu "zapisz, kopiuj" i raport czy coś, to w końcu nie wiesz, w którym jesteś, tak, i trzeba wyjść, wejść.

**Damian Kaminski**: No tak. "Zapisz" już został poprawiony, bo tutaj też był taki mankament, że zrobiłeś poprawkę, klikałeś "zapisz", wracałeś na starą definicję raportu, który przed chwilą edytowałem się odświeżyć, żeby te twoje zmiany zostały zobaczone. Ale to już Mikołaj poprawił. Natomiast, tak, no, kolejne elementy trzeba by wynajdywać i poprawiać.

**Lukasz Bott**: Dobra, Ania, czyli ty na razie ten hotfix zrobiłaś po stronie "develop", tak, tego?

**Anna Skupinska**: Jeśli chodzi o to, że można było edytować dashboard, dodawać raporty systemowe, to tylko to jest tak. To jest poprawka po stronie bazy danych i trzeba po prostu mogę zrobić tę hotfixa i trzeba po prostu uruchomić tego debila admina i update bazy danych, i będzie dobrze, albo ręcznie to zrobicie.

**Lukasz Bott**: Żeby można było wybierać raporty systemowe na dashboard.

**Damian Kaminski**: Dobra. Aniu, zrób sobie zgłoszenie. Powiedz, czy jesteś w stanie, czy wszystko rozumiesz? "Zapisz jako" nie powinno kopiować flagi. To jest raz. Dwa, powinno przenosić od razu cały ekran na nowy raport, który stworzyłaś przed chwilą funkcją "zapisz jako", czyli łącznie z tym "breadcrumbem", który mamy na górze.

**Lukasz Bott**: Na edycję nowego raportu.

**Anna Skupinska**: Dobrze.

**Damian Kaminski**: Bo właśnie ten "breadcrumb" powoduje, że nie, chociaż no jesteśmy w 276, a "zapisz to Łukasz jako" teraz "test LB 2".

**Lukasz Bott**: Literalnie.

**Damian Kaminski**: Mhm. I widzisz, na górze przeniosło cię, jesteś na nowym, ale "breadcrumb" masz stary.

**Kamil Dubaniowski**: Zmienił się.

**Lukasz Bott**: No i. Nie.

**Damian Kaminski**: Tak, bo jest 277. Spojrzałem. Odśwież. Cały ekran. Teraz odśwież cały ekran.

**Lukasz Bott**: Tak, tak, tak.

**Damian Kaminski**: O tak odśwież. I zobacz, co się stało. Widzisz, czyli przeładowano ci adres, a został ci stary ekran. Miszmasz.

**Lukasz Bott**: No tak.

**Anna Skupinska**: Tak, wydaje mi się, że gdzieś jest system, który sprawia, że odświeżanie i od właściwie powstrzymuje. Może to, może ktoś nie pomyślał, że "repair" może się zmienić.

**Damian Kaminski**: To trzeba to poprawić. Czyli "zapisz jako" odświeża cały ekran, żeby załadowało wszystko tak jak trzeba. I dwa, nie kopiuje flagi "system reports".

**Lukasz Bott**: Ale kopiuje. Moim zdaniem powinien kopiować foldery i podfoldery definicje.

**Damian Kaminski**: Mhm, nie wiem, czy powinien. No jak uważasz? Chociaż no mógłby. Zastanawiam się, czy to jest jakiś problem? Bo to wiecie, patrzymy tylko na "zapisz jako" nie tylko przez pryzmat systemowych, ale ogólnie.

**Lukasz Bott**: O nie, nie.

**Damian Kaminski**: W sumie powinien, bo to zapisuje jako to samo jako druga wersja, więc na której dopiero będę pracował, więc tak, powinien jeszcze to uzupełniać.

**Lukasz Bott**: Bo powinien, bo ja może, wiesz. No.

**Damian Kaminski**: Bo to tam było zdefiniowane.

**Lukasz Bott**: Jeżeli tak, no moim zdaniem, wiesz, robisz "zapisz jako", robisz kopię jeden do jeden z dokładnością do nazwy. Tak naprawdę.

**Damian Kaminski**: Tak.

**Lukasz Bott**: I nawet moim zdaniem nazwy wyświetlane powinny być wyczyszczone. Tyle. Pojawia się nowa instancja pod nowym ID-kiem i pod nową nazwą, a cała reszta jest tak jakby bez zmiennej.

**Damian Kaminski**: Dobra, mamy to nagrane. Ostatnie pięć minut. Ania możesz sobie odtworzyć, zrobić sobie z tego zgłoszenia.

**Anna Skupinska**: Dobrze.

**Lukasz Bott**: Dziesięć minut.

**Damian Kaminski**: Dobra, to kończymy.

**Anna Skupinska**: I to wszystko jest jednym zgłoszeniem, tak?

**Damian Kaminski**: Jak uważasz, jak uważasz, że warto to podzielić, to podzielę na dwie lub trzy wedle uznania.

**Anna Skupinska**: Mhm.

**Lukasz Bott**: Dobra, kończymy. Dzięki.

**Damian Kaminski**: Dzięki. Cześć.

**Kamil Dubaniowski**: Dzięki.

**Anna Skupinska**: Cześć.
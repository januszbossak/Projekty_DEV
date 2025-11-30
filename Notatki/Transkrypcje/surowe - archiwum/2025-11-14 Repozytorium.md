**Transkrypcja**

14 listopada 2025, 11:06AM

**Janusz Bossak** rozpoczęto transkrypcję

**Damian Kaminski** 0:04  
Ee no dobrze, to w takim razie.  
No przede wszystkim jest to element systemu emod to repozytorium.  
Sama struktura jest wielopoziomowa.  
I można ją po prostu budować, dodając kolejne podfoldery te najwyższe foldery to mękę atura mnie przyjąłem, że nazywamy, powiedzmy przestrzeniami, żeby można było je jakoś wyróżnić. To łatwo można zrobić po stronie backendu tak, Przepraszam frontendu, żeby żeby może właśnie jakąś inną ikonkę tam przydzielać.  
Natomiast tak możliwość tworzenia struktury wewnątrz.  
Foldery zagnieżdżone tutaj było ustalone wstępnie, że 20 poziomów no możemy to po prostu w jakiś sposób ograniczyć tak, żeby to też nie było jakoś chociaż Piotr nie dał co do tego wydaje mi się.  
Uwarunkowań takich.  
Jak to nazwać technicznych? Tak raczej wynikało to po prostu z kwestii ścieżki windowsowej foldery maksymalnie 2000 obiektów.  
Pliki przechowywane w dowolnej gałęzi, czyli albo w najwyższych folderach albo w po folderach.  
Jeśli chodzi o obsługę plików, to w zakresie.  
Podglądów.  
I wczytywania tych plików nie zmieniamy nic względem tego, jak to jest obecnie, łącznie z uploadem tak, czyli bazujemy na tych zasadach, które są wam olicie na poziomie sprawy obsługiwane.  
I tutaj z racji, że będziemy to robić.  
Ee reaktor owo.  
No to ja zakładam, że tutaj nie będzie żadnego problemu, żeby wykorzystać to co reaktor owo już zrobiliśmy jako podgląd dla raportów, bo to już powstało.  
Zostało zaktualizowane, więc mam nadzieję, że to jest tylko już w zasadzie przeniesienie faktycznie takiego komponentu.  
W podstawowym oczywiście zakresie.  
Mm.  
Ale to zaraz możemy już tam przejść do szczegółów, jeśli chodzi o uprawnienia. Na ten moment ustaliliśmy sobie, że MVP jeden to jest definicja.  
Uprawnień dla poziomu Najwyższego, czyli dla tej przestrzeni.  
I wszystko reszta jest dziedziczona w dół. Nie istnieje możliwość przerywania.  
Jeśli chodzi o typy uprawnień, no to mamy pełny dostęp, czyli administrator, czyli odczyt, zapis, usuwanie, tworzenie struktury i tu jeszcze bym dodał nadawanie.  
Dostępów.  
Edycja, czyli odczyt, zapis, usuwanie swoich plików tu jest właśnie z takim zastrzeżeniem. To była moja propozycja.  
I folderów i tworzenie struktury. Odczyt to jest tylko przeglądanie.  
Administrator systemu dziedziczy uprawnienia administratora przestrzeni, więc tutaj nic nic innego.  
No i de facto jest inicjatorem pierwszej przestrzeni, bo nie mamy czegoś takiego tutaj. Ja zakładałem, że nie będzie przynajmniej na razie czegoś takiego krola administrator, repozytorium czy coś w tym stylu, czyli to administrator musi utworzyć przestrzeń i nadać w jej ramach uprawnienia administratora przestrzeń.  
No i wtedy ten już administrator przestrzeni może tym zarządzać.  
Dziedziczenie to już tak jak opowiedziałem od góry.

**Janusz Bossak** 3:55  
Mhm.

**Damian Kaminski** 3:56  
Ee.  
Wyświetlanie uprawnień no to jest już bym powiedział front tak czyli czyli jak już będziemy je zaopiekowane, no to de facto w projekcie to jest.  
Ee.  
Tutaj w zasadzie to muszę już zaktualizować, będą przechowywane.  
Tak.  
Czekaj, czy ja dobrze mówię?  
Już zgłupiałem, nie wiem, czy ty pamiętasz. Wydaje mi się, że tak jak załączniki.

**Janusz Bossak** 4:37  
Tak, tak, tak jak on.

**Damian Kaminski** 4:38  
Bo już mi się miesza z tymi szablonami, bo szablony jeszcze spojrzę tutaj to co Piotr pisał to jest potencjalny rozwój.  
Żebym nic nie przekłamał modu będzie częścią należy dodać kolumnę na pliki będą zapisywane zgodnie z konfiguracją dla załączników dobra o k. Dobrze.  
Czyli może to przekopiuje po prostu?  
O k.  
Przechowywanie w systemie plików podobnie jak.  
Yy.  
Dobra, to nie ma już tutaj znaczenia, a tu lokalizacja fizyczna można skopiować to przepisywaniu na dysku.  
Dobra, teraz struktura.  
To w zasadzie.  
Jest to samo.  
A struktura pod folderów to moga też od razu do skopiować, żeby był ten jeden dokument.  
To jest powtarzane latami to już było.  
Identyfikacja pliku w interfejsie.  
No do tego się Piotr nie odniósł.  
Chyba bezpośrednio, ale zakładam, że to.  
Skoro przechowujemy to tak jak tu, to pewnie tak to będzie. No tu można by Piotr dopytać.  
Czyli tu by było.  
Coś w tym stylu?  
Od razu wysłać ci zapytać, czy tutaj mówicie jakieś obiekcje?  
Szyfrowanie no to tutaj zakładam, że skoro przechowujemy je tak samo, to to po prostu będzie natywnie.  
Ale też nie wiem.  
To jest moje założenie.

**Janusz Bossak** 8:45  
No dobra no.

**Damian Kaminski** 8:49  
No i jeśli chodzi o metadane w bazie, to w zasadzie tam piotruś to określił tak.  
Ale będą spójne z tym to samo co co dzisiaj w zasadzie zakładam mamy.  
Ee więc pewnie trzeba było przejrzeć bazę danych już przy spisywaniu tego to wymienić.  
Dalej interfejs użytkownika tak więc tutaj już bardziej front.  
Mm, nawigacja mamy w formie drzewa, no to tak jak na projekcie operacje na plikach a plod.  
Usuwanie tylko swoich usuwanie tylko wszystkich administrator przestrzeni albo administrator systemu.  
Przenoszenie plików między folderami spoza zakresem wersjonowanie poza historia zmian poza.  
No i podgląd tak jak dzisiaj wyszukiwanie.  
Lotu.  
Do tego Piotr się nie odniósł.  
Zakładam, że do tego tak jak rozmawialiśmy wcześniej musi być jakiś inny.  
Inny proces.  
Luc zyn.  
No ale.  
To niekoniecznie musi być ciałem wypi pierwsze.  
Więc to też na potrzeby testów niekoniecznie jest może niezbędne przeszukiwanie samych dokumentów.  
No i jeśli będzie no to będzie zakładam tak jak w Rusin, czyli po nazwie i po treści.  
Cała reszta to już.  
Nieistotną to tak wysoko poziomowe to wygląda.

**Janusz Bossak** 10:35  
Dobrze no to teraz to trzeba przenieść do backlogu i to zacząć.  
Powiem materializować w postaci tych naszych mbp.  
Wieczorów, które mają, w którym vip wejść.  
Bo to jest całkiem dobrze już rozpracowane tak na takim ogólnym wysoko poziomowym.  
Poziomie tak.

**Damian Kaminski** 10:59  
No k tylko no właśnie teraz jak jak sugerujesz, według Twojej polityki powinno być to podzielone.  
Pierwszy fischer to powinno być właśnie struktura.

**Janusz Bossak** 11:11  
Że najpierw trzeba spisać tak powiem ficzery tak możemy.

**Damian Kaminski** 11:11  
I potem.

**Janusz Bossak** 11:15  
Yy robić to już na tym blogu naszym.  
Można zrobić na przykład.  
Zastanawiam się właśnie, którą strukturę to wrzucić, bo to jest musimy nad tym przed chwilą myślałem. Ogólnie tak tematy związane z realizacją zobowiązań.  
To jest jeden sposób, żeby zapisania, że to jest ta inicjatywa nasza.

**Damian Kaminski** 11:48  
Masz na myśli inicjatywę? No ja przyznam szczerze mi się to średnio podoba to podejście.  
Wolałbym, żebyśmy te inicjatywy, bo albo inaczej inicjatywa z założenia ma być skończona.

**Janusz Bossak** 12:04  
No nie, inicjatywa jest, to jest raczej cel biznesowy.  
Panie na przykład o skrócenie czasu wdrożeń 30%, no to jest.

**Damian Kaminski** 12:11  
Czy nie, nie traktujemy ją jako coś rozliczal w kontekście statusu?

**Janusz Bossak** 12:16  
Nie to jest wytyczna inicjatywa to jest jakby wytyczna tak znaczy tak tutaj gdzieś sobie inną inicjatywę pracowałem, która się nazywa wzrost satysfakcji użytkownika poprzez modernizację interfejsu i tutaj cel właśnie to powinien być cel taki biznesowy, tak który jest tak, że 80% pozytywnych ocen w ankietach in ap tak, czyli gdybyśmy mieli taką ankietę i nap.  
I byśmy mierzyli satysfakcję klienta z tego, że dostał nowy interfejs użytkownika, na przykład na sprawie.  
No to moglibyśmy stwierdzić, czy my ten cel osiągamy czy nie i czy jakieś robimy działania w związku z tym, żeby podnieść ten wskaźnik tak i on jest długofalowo może być przez 2 lata przez 3 lata obserwowane i tak dalej, tak.  
I wtedy mamy dobry cel, tak?  
I teraz to na przykład przed chwilą opracowałem sobie cel dla zwiększenia stabilności modułu raport owego.  
I tutaj jest bardzo fajnie. Też ten podpowiedział cel jest redukcja błędów, ale w rozumieniu wskaźnika p jeden do p. 2, czyli błędy krytyczne.  
Do błędów ważnych jeden p jeden to po naszemu są jakby Kategoria, a p to jest Kategoria b. Tak, czyli pierwsze to jest w ogóle zatkało kakao i nie można działać, a drugie to są błędy ważne, które uniemożliwiają tam jakąś pracę, ale jakieś obejście na to są i chcemy zmniejszyć to na razie nie mamy tego wskaźnika tak, ale może ten wskaźnik trzeba właśnie wyliczyć.  
Ten p jeden do p 2 jaką on ma teraz wartość?  
I założyć cel, że chcemy go zmniejszyć o 40%, tak no i w jakimś tam czasie będziemy sobie liczyć. Ile jest błędów z modułu raport owego?  
Yy i będziemy mogli stwierdzić, czy ten wskaźnik osiągamy czy nie, czyli to jest poziom inicjatywy tak i teraz może być inicjatywa.  
Tu właśnie też przed chwilą o tym rozmawiałem, inicjatywa dotycząca monetyzacji jakieś rzeczy, czyli robimy tak jak to pozy Toruń, no owszem, mamy klienta, który na nas to wymusza, ale z drugiej strony to jest powód do monetyzacji tego tak takie repozytorium można by sprzedawać.

**Damian Kaminski** 14:32  
No.

**Janusz Bossak** 14:32  
I i to raczej pod taką inicjatywę, tak samo jak tutaj. Przed chwilą rozmawiałem z Łukaszem odnośnie tej integracji z Comarch hubem.  
No właśnie pod.

**Damian Kaminski** 14:42  
Może żebyśmy teraz też wątku może już nie mieszali, bo powiedziałbym, że to już jest wtórne w sensie.

**Janusz Bossak** 14:50  
Tak.

**Damian Kaminski** 14:50  
Próbujemy w narzędziu do zarządu.  
Dania back logiem ująć.  
Cele biznesowe bardzo wysoko poziomowe, więc powiedziałbym, że czy to umiemy? Tak czy inaczej, to już tylko od nas zależy i nie ma to na nic wpływu. Pewnie w łatwy sposób można to też przepięć czy przezywać?  
Yy, bo w zasadzie mamy jeden epik, który przeklinamy do innej inicjatywy, jak uznamy, że to jest inaczej, będzie to gdzie indziej.  
No te inicjatywy mają ten minus, że.  
Ja wiem, że to jest tu awaria, ale ja bym wolał szczerze, żeby to był taki właśnie poziom jak pewnie tu tylko no to wtedy jest duplikacja, więc nie ma to sensu, ale to to to co ci zawsze tam to nie zawsze, ale to co ci pokazywałem, że.  
Łatwo jest właśnie poruszać się tu po drzewku, tutaj wybierając ja fajnie mogę się po tym poruszać, no filtrów po tym niestety takich wygodnych nie ma jak tu.  
A to by właśnie definiowało, że o k. Administracji mamy to to i to, a możemy też już uznać, że coś jest zaplanowane. Projektowanie obecne projektowane obecnie, jeśli poruszamy się po inicjatywach.  
No to tych inicjatyw 5 lat będziemy mieli tyle, że tam będzie się ciężko odnaleźć. W którą.

**Janusz Bossak** 16:06  
Nie, nie, nie, nie, nie, bo się inicjatywy muszą być.

**Damian Kaminski** 16:10  
Ograniczone.

**Janusz Bossak** 16:11  
Z tą naszą mapą, tak ze strategią, tak, skoro mamy bardzo dobrą inicjatywą, jest to skrócenie czasu wdrożenia 30%. Tak to powiedzmy mierzyć i powinniśmy wiedzieć, czy skróciły się te wrażenia o 30% czy nie, ale jest to pewien, jakby miernik biznesowy i tu akurat się ja pod tym podpisuję, że ten poziom inicjatywy pomaga nam.

**Damian Kaminski** 16:20  
Mhm.

**Janusz Bossak** 16:36  
Też w myśleniu o tym pod co to podpiąć, bo są takie. No właśnie ten komarch tak komar hab albo to ja terriva właśnie albo teraz to repozytorium pod co to podpiąć? Tak dlaczego my to robimy? Bo to jest pytanie, dlaczego my to robimy? Zresztą nawet tu już potem się łączyłeś z tego spotkanie, tam więcej było takich różnych drobnych rzeczy, które z Kamilem rozważaliśmy. Pierwsze pytanie, dlaczego my to robimy?  
No bo który znalazł ten błąd? No i co z tego, że znalazł?  
Jak go nie zrobimy, to co się stanie?  
No nic będzie tak ten błąd, ale on jest tylko tam w specyficznym przypadku, gdzieś tam gdzieś tam i to w ogóle Basia znalazła, no to sorry.

**Damian Kaminski** 17:11  
No tak.

**Janusz Bossak** 17:20  
Tak znaczy, musi być cel, tak?  
To jest inaczej masz.  
Budżet pieniędzy w ręku.  
Jesteś w sklepie, który ma dużo błyskotek i musisz te pieniądze, czyli nasz czas przeznaczyć na coś konkretnego. Tak nie masz kupować byle co fajne, tylko możesz kupić rzeczy po to po co cię żona wysłała, nie ma miałeś kupić?  
No szafę tak a nie po drodze kupić wieszaki i schowek na kurtki i tak dalej nie tym. Ja się dziś kupić górna szafę, miałeś pieniądze przeznaczone na to żeby kupić szafę i masz tą szafę przywieźć do domu no i na tym to polega.  
Jak dzieci musimy nie nie przyklejać nosa do witryny z cukierkami i tam będziemy sobie cukierki kupować tylko nasz cel jest przywiesza otwarty do domu. Tak to jest nasz cel.

**Damian Kaminski** 18:07  
Rozumiem.

**Janusz Bossak** 18:22  
Po to są te inicjatywy, tak, to są te najwyższe takie cele, a pod nimi są te nasze prezenty, które dowozimy, a dopiero w ramach właśnie tego aria tu się pod tym podpisuje. To to jest rzecz, która mówi, której części, a młody, a modlitwa jakieś prace będą wykonywane.  
Ta aria.  
Zauważy na poziomie.  
Twittera, czy na poziomie nawet pb, a ja podpiętego pod tego fischera może być inna.  
Tak, bo możemy zrobić tak, że jest jakiś ficzer.  
I cały jest w jakimś tam obszarze?  
Ale na przykład musimy zrobić do tego do tego MP, noże naszego.  
Zmiany na przykład w grobach.  
I to jest inny obszar morita i zmiany na frontendzie na sprawie albo na frontendzie na ustawieniach systemowych i to jest inny obszar monita, ale ciągle dostarczamy tą jedną wartość, jedną paczkę coś tam będzie działać.  
Ale to wymaga zmiany w dziobie zmiany w ustawieniach systemowych i zmiany. Nie wiem na formularzu sprawy, na przykład no.  
Więc czy różne czy tyle masz te?

**Damian Kaminski** 19:34  
Mhm.

**Janusz Bossak** 19:37  
Ale paczka wartości właśnie to jest jakby według mnie ciągle klucz.  
I tu ten ja i mi to ciągle powtarza, przy każdym tym nie traktuj.  
Tych mp jako worka funkcjonalności.  
Czy albo worka modułów, które robisz nie, to są wartości, które dostarczasz.  
Która się składa z wielu rzeczy dobra, wracamy do tego, nie będziemy można dobra. Na razie zrobiłem ogólny takie coś. Osiągnięcie nowego strumienia przychodów z modułów dodatkowych dla mnie repozytorium jest modułem dodatkowym. W ramach tego możemy zaraz utworzyć sobie.  
Yy PA ja pierwszego nie PA tylko mbp.  
I to będzie się nazywało o z to.  
Nawet nazwiemy wim było to będzie jeden.  
No i tutaj powiedzmy na razie mamy.  
Na lista, funkcjonalność, a potem będziemy za chwilę te dzieli.  
Dobra.

**Damian Kaminski** 20:48  
Ale teraz to nie zrozumiałem, gdzie ty to zapisujesz?

**Janusz Bossak** 20:51  
Czujesz się pokazać? No no nie?  
Tak.  
I teraz na razie tu będziemy dodawali ficzery.  
Czyli rzeczy które?  
Ogólnie trzeba zrobić.  
Tak.

**Damian Kaminski** 21:12  
Mhm.

**Janusz Bossak** 21:13  
Yy no i teraz co tam z tej teraz nie widzę tej Twojej tabelki nie, no to tego pliku.

**Damian Kaminski** 21:20  
Nie tabelki tylko.

**Janusz Bossak** 21:22  
Dziękuję panu mam.

**Damian Kaminski** 21:23  
To ja bym powiedział, że raczej wszystko to wrzucamy tam, bo to jest epik, czyli opis wszystkiego czy nie.

**Janusz Bossak** 21:31  
Teraz jesteśmy tak znaczy byliśmy na poziomie piku. Na razie tak trzeba z tej kasy.

**Damian Kaminski** 21:36  
No wiesz, do tego też można jak już mamy to powiedzmy tak przygotowane można podejść do tego dwojako, czyli tak bym to rozumiał, że można epikur dać tylko opis ogólny, a potem opisywać kolejne elementy, a można podejść inaczej. Tu już na popisie ogólnym wrzucić wszystko, a potem kopiować to.  
I tylko ewentualnie rozwijać, jeśli coś wymaga do szczegółu łowienia na poziomie tym niższym fischera.

**Janusz Bossak** 22:03  
Znaczy, chodzi mi o to, że tutaj powinni być teraz te ficzery tak jakiś tam fischer pierwszy.  
Yy, tak i tak dalej.

**Damian Kaminski** 22:12  
Czyli zarządzanie strukturą można to nazwać, bo tak bym to.

**Janusz Bossak** 22:15  
Drugi i na razie się nie zastanawiamy, czy to będzie w tym mbp. Jeden to na razie tylko otrzymam jak bo po prostu no nośnik tych ficzerów.

**Damian Kaminski** 22:21  
No jasne.

**Janusz Bossak** 22:26  
I za chwilę jak tu sobie wypiszemy ich będzie ich tam 15, 16 czy 20 to zdecydujemy, które z nich?

**Damian Kaminski** 22:26  
Mhm.

**Janusz Bossak** 22:35  
Zostają w tym mp jeden, a które dajemy na mp 2 kryterium jest to, że to mp jeden musi być zrobione w jeden sprint.

**Damian Kaminski** 22:45  
No powiem, a jeszcze może tylko zarysuje, że dzisiaj już pan Piotr, no co było do przewidzenia nie wiem w tak dobrym humorze, więc.  
Skomentował to tak, że.  
Wy możecie sobie oklejać.  
A wymagania są zapisane w csie.  
Więc jeszcze ja nie zaglądałem jeszcze do tego serwisu, ale według mnie wymagania w cv jest sprowadzają się do 2 zdań odnośnie repozytorium. No i pytanie, kto jak interpretuje.

**Janusz Bossak** 23:09  
No właśnie, no właśnie.  
No właśnie, więc niech niech więc niech też nie będzie niegrzeczny.

**Damian Kaminski** 23:13  
Co to jest repozytorium?  
No mówię tylko, że z tego jakiś tam.

**Janusz Bossak** 23:20  
Dobra z tym komunikatorem coś powiedział?

**Damian Kaminski** 23:20  
Zapalnik pewnie będzie.  
No że dobrze, ale jak to jest bohater TP to nie dotykamy te w ogóle nie wyświetlił się im jednak, bo.  
Nagraj mają ustawione przekierowanie automatycznie, więc nawet oni bohater TP nie są w stanie się połączyć nawet do testów, poki bo jest na HTTPSA na HTTP się jest po prostu nie wspierane, bo nie mamy certyfikatu, więc no napisałem już maila do tego pana Andrzeja po spotkaniu, żeby rozwiązać ten temat, bo on już się przewija dłuższy czas na serwis go gdzieś to mnie nie zaopiekował.

**Janusz Bossak** 23:58  
Po ich stronie tak to jest problem.

**Damian Kaminski** 24:01  
No to znaczy wspólny według mnie, ale tak oni muszą nam pomóc przy tym, czyli oni muszą nam wysłać certyfikaty, żeby osadzić je lokalnie, bo wiesz, oni je przechowują na gateway tak, czyli na bramce, czyli jak ty się łączysz z zewnątrz z serwerem zewnątrz? Mam na myśli ze swojego komputera VP, nie to przechodzisz przez jakiś tam serwer, który zarządza ruchem sieciowym i tak jakby.  
Certyfikat jest dokładany do twojego zapytania na poziomie tego tej bramki sterującej.  
Ale to powoduje, że lokalnie jak jest teraz amo dit i ten.  
Komunikator to one się komunikują lokalnie, bo są na jednym serwerze. To one nie mają certyfikatów i to powoduje problemy.  
Bo nie mamy, bo nie mają certyfikatów lokalnie osadzonych, a ruch jest wykonywany lokalnie, a nie przez tego DNA czy gateway. Ja już tu nie będę się mądrzył po prostu nie przez.

**Janusz Bossak** 24:49  
To.  
No no.

**Damian Kaminski** 24:59  
Bramkę, która steruje ruchem.  
No i w dodatku nawet jak na bramce już jest ten certyfikat.  
Nowy to i tak musimy mieć jeszcze dołożony certyfikat do samego.  
Komunikatora, bo tak naprawdę to jest odrębna aplikacja z odrębnym adresem, tylko obsadzana w ramie. No i ja de facto dowiedziałem się o tym wczoraj od Mateusza, więc dzisiaj tylko uzyskałem z kim się kontaktować w tym temacie. No i już maile poszły z naszej strony, czekamy na odzew.

**Janusz Bossak** 25:29  
To jest problem właśnie tego, że tak to zostało, że tak powiem wymyślone teraz. Dlatego Piotr dla tych pozyton podium bardziej sugeruje jednak podejście takie, że to jest częścia modi, tata i według mnie tylko komunikator też powinien był być częścią morita.  
I tyle po prostu niestety.

**Damian Kaminski** 25:46  
Znaczy wiesz co jeśli chodzi o bazę danych?  
Był Mateusz powiedział, że to może być jedna. Nie wiem jak on w końcu to zrobił.  
Ale ja mu powiedziałem, na razie zrób tak, żeby to działało i nie było żadnych ryzyk, a najwyżej to poprawimy i wyciągniemy wnioski na środowisku już produkcyjnym.  
I tu pewnie trzeba będzie jeszcze się spotkać przed produkcją i ustalić, że jeśli to ma być, powiedzmy przynajmniej bardzo danowo częściowo dita.  
Bo ja go zapytałem jakie nazwy tabel, no dowolne no to mi się tak odpowiedź nie podoba, bo wiem co Piotr potem na to powie nie dowolne, tylko muszą być odgórnie ustalone, żeby nie konflikt powały nigdy w przyszłości, no i tyle.

**Janusz Bossak** 26:24  
Dokładnie.  
Dobra, wracamy tutaj, no panem Piotrem to wiadomo jak jest tak rad ma lepszy humor oraz gorszy, więc.  
Trudno powiedzieć, jaki będzie miał jutro czy pojutrze, ale no i musimy swoje robić.

**Damian Kaminski** 26:40  
No dobrze mamy te ficzery.  
No myślę, że możemy je od razu nazywać, bo ja po prostu potem to tylko po uzupełniam. Jeśli ułożymy sobie to na taki wysoko poziomowe o to ja postaram się to po prostu pouzupełniać.

**Janusz Bossak** 26:53  
To nazywajmy.

**Damian Kaminski** 26:55  
No bo teraz tak mamy strukturę.  
I teraz ta struktura może być.  
Zarządza walna jakkolwiek, czyli możemy?  
Dodawać węzły.  
Potencjalnie usuwać węzły, pod warunkiem, że nie ma.  
Ee w tych węzłach.

**Janusz Bossak** 27:13  
To są przypadki, to są przypadki użycia.

**Damian Kaminski** 27:15  
No właśnie to są przypadki użycia, więc.  
Widziałbym to chyba właśnie w tym w tym akurat projekcie, tak jak już proponowałeś, czyli jest fischer, zarządzanie strukturą, gdzie opisujemy, jak ta struktura jest zbudowana ogólnie, a potem mamy te rozbicie na przypadki użyć i z tego wynika już konkretne PI.  
Czyli.

**Janusz Bossak** 27:36  
Tak, to jest zarządzanie strukturą folderów, tak?

**Damian Kaminski** 27:40  
Tak, tak, tak bym tak strukturą repozytorium można nazwać strukturą folderów, tak.

**Janusz Bossak** 27:46  
Jeden.

**Damian Kaminski** 27:47  
Tylko teraz no dobra przypadki użycia, bo zastanawiam się.  
No dobra teraz jak jak właśnie ty to widzisz, bo ja tu cały czas może mam jakieś niezrozumienie, przypadek użycia to jest.  
Dodanie nowego folderu.  
I teraz dlatego dodania nowego folderu.  
Co ma być następne? Bo to rozumiem. To potwierdzasz tak to jest przypadek użycia.

**Janusz Bossak** 28:17  
Nie muszą być tak rozbijane w przypadki użycia.

**Damian Kaminski** 28:20  
Mhm a jak inaczej? No właśnie to przedstawisz, jak gdybyś to widział.

**Janusz Bossak** 28:22  
Może żebyć przypadek na wyższym poziomie znaczy taki gdzie?  
W jednym przypadku opisujemy, że będąc zalogowanym do tam tego repozytorium.  
Yy mogę.  
Dodać nowy folder.  
Usunąć folder jeżeli nie ma w sobie żadnych dokumentów i coś tam jeszcze tak i to może być przypadek użycia tak czyli to jest przypadek użycia zarządzania strukturą opisuje.  
Co mogę z tym robić? Tak, jeżeli są jakieś bardziej skomplikowane przypadki, na przykład nie wiem związane z usuwaniem.  
No to opisuje inny przypadek użycia, tak więc to zależy.

**Damian Kaminski** 29:06  
Dlaczego to pytam, żeby żebyśmy może dobrze zrozumiał, dlaczego ja to tak drążę, bo chciałbym unikać takich.  
Powiedzmy w głąb.  
Ścieżek, które są de facto jedno wymiarowe, czyli no ale wiesz o co mi chodzi tak, czyli no właśnie to potwierdza, że to nie ma sensu, czyli jeśli mam stworzyć 2 przypadki użycia i oba one mają mieć?

**Janusz Bossak** 29:24  
No to nie ma sensu.

**Damian Kaminski** 29:34  
Po jednym PIU.  
No to w zasadzie mogę pominąć w przypadki stworzyć od razu te PBA je.

**Janusz Bossak** 29:41  
Pewnie tak.

**Damian Kaminski** 29:41  
Tak, to o k. No dobra, to tu się zgadzamy.

**Janusz Bossak** 29:44  
Tak, tak, tak tu chodzi o to, że wiesz, no bardziej w tym jeter włam na przykład te przypadki użycia były nie.  
Masz przypadek użycia?  
Czyli inaczej mówisz klasyfikacja?  
Tego pisma, które ci wpłynęło?  
To jest twitter.  
Tak, czyli musisz pismo sklasyfikować i teraz masz przypadek użycia. Pierwszy to pismo, które jest.  
Nie jest pismem tworzącym akta sprawy, czyli musisz zaklasyfikować do.  
Tego ogólnego takiego ogólnej teczki.  
Która nie tworzy akt sprawy, to pismo, które jest trzeba zaklasyfikować do istniejącej teczki, czyli przypadek użycia jest taki, że potrzebuje umieć mieć możliwość wyszukania istniejący tej teczki po.  
Nazwie po czymś tam dacie to jest przypadek użycia, może znaleźć teczkę, do której mam to wpiąć trzeci przypadek.  
Użycia w tym momencie jest taki, że muszę mieć możliwość utworzenia nowej teczki sprawy, do której dopiero to pismo wepchne z kolejny przypadek ojca. Tak, czyli to jest ten poziom nie jak popiera te teraz rozpiszesz, no to na przykład przypadek tworzenia nowej teczki może mieć 15 PI ów tak, bo muszę.

**Damian Kaminski** 30:53  
Mhm.  
Mhm.

**Janusz Bossak** 31:07  
Wy JRA tam stworzyć coś muszę przekopiować.  
Na przykład te klasyfikacje archiwalną do tego poziomu muszę sprawdzić, czy daty mi się zgadzają, czy ja mogę w tym węźle muszę sprawdzić uprawnienia, czy ja w ogóle w tym węźle mogę utworzyć tak dalej i tak dalej? Tak czy masz ileś pb i w którym musisz wykonać czynności, które trzeba sprawdzić nie i dlatego się opisuje te przypadki użycia tak samo jak to jest z tymi na przykład nie wiem filtrami w raportach tak, no to tak do tego podchodzimy, no bo tam jest filtr, ale tam jest w każdym filtrze, bo to akurat rozważałem tutaj tydzień temu, tak.  
Masz równa się, masz zawiera dla daty, masz tam pomiędzy i tak dalej i tak dalej i to są różne przypadki jeżeli użyje tego przypadku, czyli na przykład pomiędzy.  
To co to oznacza, że na przykład co mogę wpisać w jedną datę, a w drugą nie mogę wpisać w obie mogę wpisać nie w pierwszą, a w drugą. To będzie oznaczało, że wszystko, co wcześniej do tego, to są przypadki użycia tak, kiedy użyły użyję operatora pomiędzy.  
Dla dat.  
I dopóty, dopóki my tego nie mamy opisanego.  
To właśnie mamy takie.  
Domysły nie poziomu dewelopera. On myślał, że to tak będzie.  
Ale to potem może biznesowo nie spełniać wymagań jakiś nie.  
No to jest sponsor przeniesienie trochę roboty tej dokumentacyjnej na początek a nie na koniec nie.  
Tyle dobra, więc zarządzanie strukturą.

**Damian Kaminski** 32:41  
Znaczy, no to teraz już się zastanawiam czy tego nie skorygować, bo teraz można to zrobić. Tak można napisać fischer, to jest zarządzanie strukturą i wtedy mamy w zasadzie, może nie mamy przypadków użycia z tego będą nie wiem. 2 PIEA można zrobić struktura folderów i wtedy z tego możemy dać juz case jeden to jest zarządzanie, a 2 to jest przeglądanie.  
No i dla powiedzmy możemy dlatego przeglądania dać wytyczne, że po wejściu po wejściu na na repozytorium domyślnie wyświetlają mi się za pierwszym razem tylko nadrzędne, czyli te obszary. A jak już wchodzę wtórny raz to jest drugi powiedzmy przypadek użycia tego to czytam PBI, powiedzmy do do tego to ma się zapisywać w dziś lokal z ryżu, moje ostatnie rozwinięte węzły, żebym nie musiał za każdym razem tego rozwijać.

**Janusz Bossak** 33:08  
Dobrze bardzo.  
Możemy patrzeć na to też od strony takiej właśnie jak tu powiedzieliśmy, dokumentacyjnej tak, czyli jak gdybyśmy pisali instrukcje.

**Damian Kaminski** 33:46  
Mhm.

**Janusz Bossak** 33:47  
No tak, jak tu powiedziałeś jedną z instrukcji byłoby jak na przykład coś tam znaleźć strukturze folderu, czyli przeglądanie struktury, folderów tak i tutaj, w tym przeglądaniu struktury folderów. Teraz uwaga mogą być.  
Juz kasy tak no i tu może od razu to zróbmy tak, bo tu może być już case wyszukiwanie.

**Damian Kaminski** 34:09  
Tak, tu możesz wyszukiwanie i manualne przeglądanie drzewa.

**Janusz Bossak** 34:11  
Wyszukiwanie folderu.  
Tak.  
Ale może być drugi juz case.  
Jak w tym przeglądaniu wyszukiwanie?  
Likoum.  
To jest juz kpina.

**Damian Kaminski** 34:33  
No to jest. To jest akurat rzecz, której nie mam nawet w głowie.  
Ee i to trzeba jeszcze ustalić.  
No ale to już jest, może nie teraz.  
Wyszukiwanie właśnie plików ma ma jakieś zadanie z gwiazdką bym powiedział.

**Janusz Bossak** 34:48  
Dobrze.  
Czy coś jeszcze do przeglądania struktury ci się?  
Kojarzy no i teraz zarządzaniu strukturą podobnie.

**Damian Kaminski** 35:04  
To znaczy albo albo inaczej to czy mi się kojarzy? No kojarzy mi się po prostu przeglądanie, czyli co się, czyli opisanie jak to działa, co się jaki jest domyślny widok, czy zapamiętuje i tak dalej i teraz.  
Jak rozumiem może być też taka struktura?  
Różnorodna, czyli z samego przeglądania w spitzera mogę stworzyć jakiegoś pb a ja a z tych userów odrębne pb a je.

**Janusz Bossak** 35:22  
Bo w tym świecie.

**Damian Kaminski** 35:30  
Czy tak byś nie chciał?

**Janusz Bossak** 35:34  
Nie zrozumiałem.

**Damian Kaminski** 35:36  
Czyli gdzie teraz spisać? No właśnie wytyczne co do standardowego wyglądu struktury po wejściu albo wymagania co do właśnie zapamiętania w lokal story czy rozwiniętych drzewek rozwiniętych gałęzi.

**Janusz Bossak** 35:54  
Mm.  
Można tutaj zrobić jak oficer.

**Damian Kaminski** 36:01  
Czyli niezależnie zakładasz od przeglądania, tak?

**Janusz Bossak** 36:04  
Tak no bo.  
Przeglądanie to już jak ją utworzymy tak, ale dopiero jak utworzymy tak, czyli tu może być fischer.  
Jak to nazwać dobrze?  
Mm generalnie struktura.

**Damian Kaminski** 36:27  
Wygląd drzewa, struktury.

**Janusz Bossak** 36:29  
No właśnie, może drzewo, strukturę.  
Bo drzewo folderów.  
Berów na razie może tak.  
No i to jest właśnie ta cała.  
Graficznego.  
To jest jedna rzecz.  
Może być już tutaj. Tak to może być pierwsze nawet.  
Potem może być drzewo folderów.  
Mm.  
Mia nie upraw.  
Jenny, siniak mnie denerwują te.  
Na razie taką ogólnie, ale może może to doprecyzujemy.

**Damian Kaminski** 37:36  
Mhm.

**Janusz Bossak** 37:41  
To też pewnie jest tutaj, bo to trzeba będzie pewnie zrobić najpierw tak.  
A jeszcze wcześniej jest tak naprawdę.

**Damian Kaminski** 37:49  
Zarządzanie to już to masz, bo to można zarządzanie pod 5 tak, bo tworzenie chcesz ująć.

**Janusz Bossak** 37:55  
Znaczy cały powiedzieć o.  
Jakby materializacji tego, no to co gdzieś tam w którymś momencie to wyczytałeś, że to jest, że stosujemy te same zasady co do plików do załączników, tak?  
Yy, czyli musimy zarządzić jakby zapisem tych dokumentów tak, czyli zapis może tak.  
Obsługa.  
Zapisu do komentów.  
Wy amo dit tak tutaj może być baza, bo to skoro jest tak jak dokume.  
Czy taki jak dla załączników tak baza lub.  
Gorycz.  
I to nawet może napisać tak jak.  
Jak dla załogi.  
I jenny siłownią.  
Śniegu.  
No to już jest teraz tak, czyli to mamy wyżej.  
Może trzeba to zrobić jako pierwsze, tak.  
Yy, zapewnienie się dla nich hierarchicznego uwzględnienia uprawnień użytkownika, zarządzanie strukturą, folderów i tutaj zarządzanie strukturą folderów.

**Damian Kaminski** 39:16  
Znaczy, według mnie to powinno być chyba najwyżej, bo jak nie mamy żadnej struktury to nie ma gdzie zapisać.  
Przycisk zapisz dopiero pojawi się jak będziesz jakieś gałęzi.  
Czy w kraju raczej niż zapisz?

**Janusz Bossak** 39:31  
Ale zanim cokolwiek powiem, zobaczysz.  
To gdzieś to musi być zapisane.  
Znaczy technicznie musi istnieć przestrzeń, w której ten folder, który za chwilę w tym zarządzaniu strukturą folderów, utworzysz, on się musi gdzieś w bazie danych zmaterializować.

**Damian Kaminski** 39:48  
No tak, tabelę jakaś tabela. No tak tak tak, no ale.

**Janusz Bossak** 39:51  
Więc to ja to to traktuję jako backend zasadzie?  
Czyli to na przykład zapewnienie wyświetlanie hierarchicznego to to, że backend przesyła.

**Damian Kaminski** 40:00  
A ja nie.

**Janusz Bossak** 40:02  
No.

**Damian Kaminski** 40:03  
To znaczy, ja to, bo mi się to zgadza, w sensie, że teraz z tego można zrobić zadanie i front endowe i backend owe w tym Twitterze.

**Janusz Bossak** 40:11  
Można tak zależy od jakby stopnia tutaj granulacji nie.

**Damian Kaminski** 40:15  
Mhm.

**Janusz Bossak** 40:16  
Może być cały fischer jako backend owy.

**Damian Kaminski** 40:19  
No może być zgadza się jakieś tam szyfrowanie, no to tak, ale ale jak masz drzewo folderu zapewnieniem wyświetlanie hierarchicznego to bym powiedział, że stałbym, utworzył, że Erasmus i śnić tabela, gdzie mamy zapisane te dane muszą być endpoint odczytu tych danych, no i front ten ma to czytać, czy powiedzmy 3 PBI?

**Janusz Bossak** 40:43  
Znaczy, widzisz to to nie jest tak, że to jest jakaś.

**Damian Kaminski** 40:47  
No tak, ta osoba to pomysł.

**Janusz Bossak** 40:49  
Trzeba to pomysł tak no chodzi o to, żebyśmy mieli to rozbite, żebyśmy na naszym poziomie trochę biznesowym, ale pewnie trzeba tutaj dewelopera też w którymś momencie będzie za chwilę.

**Damian Kaminski** 40:59  
Trzeba, bo ja mam obawy, że przy takiej granulacji oni tego nie poczytają oni dostaną jedno co masz jeśli będzie to zespół?  
Ten się skupi na jednym, on tyle zrobił, a on nie wiedział, że to jest element czegoś większego.

**Janusz Bossak** 41:13  
Ale to czytać to mają to czytać na tym to polega, oni mają mieć cel bo za chwilę my tutaj zrobimy, powiedzmy to powiemy.  
Tutaj nazwiemy to jakoś ładnie.  
I powiemy, że tymi rzeczami macie zrobić tak, żeby to po stronie bazę danych było na przykład tak, czyli mówimy dobra, nie będzie jeszcze frontendu.  
Nic, ale w backendzie będzie już struktura pod to, żeby to można było robić tak, może być odwrotnie. To co już zrobiliśmy w sumie.  
Czyli frontend.  
Możemy go dać do pierwszego mbp, no bo go mamy.

**Damian Kaminski** 41:52  
Tak.

**Janusz Bossak** 41:52  
Zadaniem następnym będzie podpięcie teraz frontendu do backendu, ale żeby go podpiąć trzeba mieć backend.

**Damian Kaminski** 41:59  
No tak.

**Janusz Bossak** 42:00  
No i na tym to polega. No tak sobie przynajmniej ja to tak wyobrażam, no.  
Dobrze, zarządzanie strukturą, folderów to co ja jakby rozumiem to to jest trochę zadania i backendowych i front endowe.  
Ale to bym widział takie już czasy jak.  
Właśnie to co mówiliśmy tak dodawanie.  
Nowego to ru.  
No i to dodawanie na dowolnym poziomie. Tak to można napisać na no.

**Damian Kaminski** 42:34  
Że tam.  
Jeszcze sprawdza to, co napisał Piotr.

**Janusz Bossak** 42:44  
No nie sprawują mnie, bo może nie mogę na którymś momencie.

**Damian Kaminski** 42:50  
To znaczy.  
Co do zasady możesz.  
Tu na ten moment nie ma, znaczy nie no, Przepraszam, masz rację zgodnie z uprawnieniami.  
W tym opisie moim było, że jest 20 poziomów. W zasadzie jak rozumiem.  
Piotra wytyczne w kontekście zamieszczania tych plików.  
Lokalnie nie mają takiego ograniczenia, więc pytanie, czy chcemy je wprowadzać.  
No 20 poziomów w tej jednak już i tak bardzo dużo.  
Ee, nie wiem czy jest jakieś ryzyko niewprowadzania tego.  
Natomiast wcześniej było to tak przyjęte ze względu na.  
Windowsa, ale my w zasadzie od Windowsa struktury drzewiastej się odcinamy, bo dzielimy to na repository rok i i sprawa czyli w zasadzie mamy 3 tylko węzły.  
Ee tak jakby zagniesz zagłębienia, potem przechodzimy do kolejnego roku i do kolejnego, więc.

**Janusz Bossak** 43:53  
No i to co teraz powiedziałeś?

**Damian Kaminski** 43:54  
A Przepraszam rock i jeszcze 10000 tak o tak tam było, bo to jest rok.

**Janusz Bossak** 43:57  
To co?  
To co powiedziałaś, to powinno być.  
Obsługa zapisu dokumentów tu jest ten właśnie sposób przechowywania, albo tutaj można i obsługa, zapisy tylko sposób przechowywania, tak.

**Damian Kaminski** 44:06  
Tak, tak, tak.

**Janusz Bossak** 44:11  
Osób.  
Rów i plików.  
Że dokumentów może tak.

**Damian Kaminski** 44:27  
Tak.  
Po prostu plików.

**Janusz Bossak** 44:28  
2 zastępy być tak jak dla załączników, tak, no i tu i tu w treści. Teraz powinno być opisane.  
To, bo to jest ten techniczny taki trochę fischer.  
Który opisuje ten pomysł Piotra tak, czyli jak to będzie przechowywane, że tam nie ma tego łamania na 10000, żeby coś tam, że coś tam.  
Tak jak mieliśmy tam mniej więcej w tych szablonach nie, ale to jest właśnie to, to to miejsce tutaj, to będzie to opisane. Nie teraz to drzewo folderów, no to możemy na.  
Choć inaczej tak możemy zapewnienie wyświetlania.  
Tam hierarchicznego drzewa, folderów i to jest w zasadzie to, co mamy zrobione w tej chwili już jako frontend owo.

**Damian Kaminski** 45:13  
Tak.

**Janusz Bossak** 45:14  
I to możemy uznać, że to jest jakby zrobione.  
I tu możemy nawet.

**Damian Kaminski** 45:18  
To znaczy, no ale ja bym to ja bym tu dopisał backend, czyli tylko, czyli tak musi istnieć tabela, którą tu Piotr rozpisał, bo.  
Bo sposób przechowywania to już jest.  
Sposób może tak sposób przechowywania to jest czysty kot.  
Ee, bo to nie wynika właśnie bezpośrednio z.  
Ee, to będą zasady stałe, czyli w kodzie będzie jakieś 10000 to łam i tak dalej a drzewo folderów no tak, tak tak tylko zmierzam do tego, że drzewo folderów to po stronie frontendu mamy a po stronie backendu to jest tabela która opisuje taki folder taka nazwa taki narzędnik.

**Janusz Bossak** 45:50  
Ale trzeba to zrobić, ale trzeba to zrobić.

**Damian Kaminski** 46:04  
No i coś tam jeszcze jakieś parametry zgodnie z tym, co tutaj Piotr name i w sumie w zasadzie tylko 3 parametry, czyli tak jak dla naszej struktury. Na ten moment przynajmniej. No i ja bym dał. No tak, jak wcześniej powiedziałem, to dał do tego 3, PA ja.  
Czyli zapewnienie wyświetlania to jest raz, a może 4 raz, że ma istnieć tabela z określonymi kolumnami? 2, że mają być endpoint, skoro wyświetlania to endpoint get do tej tabeli dla dowolnego.

**Janusz Bossak** 46:37  
Ja bym nie schodził tej chwili na poziom PIOPAI to.

**Damian Kaminski** 46:38  
No.  
No.

**Janusz Bossak** 46:43  
Deweloperzy nie.  
To niech nie.

**Damian Kaminski** 46:46  
Ale to, czyli oni mają to pisać.

**Janusz Bossak** 46:49  
I ja bym tak zrobił.

**Damian Kaminski** 46:52  
Obawiam się tego można tak scedować, ale to trzeba sprawdzić o k. No dobra to jest podejście super.

**Janusz Bossak** 46:57  
Bo ja, bo ja nie wiem, ja nie wiem czy my jesteśmy na tyle kompetentni, żeby ustalać jakie endpoint mają być.  
My możemy napisać tu na tym poziomie zapewnienie współpracy frontendu z weekendem koniec kropka.  
Nie naszą rolą jest pisanie, jaki endpoint tam ma być.

**Damian Kaminski** 47:17  
Na dobra, ale walidacja tego.  
Albo inaczej czy pb i powinien mieć krótki opis.  
Ee.  
Biznesowy, że no właśnie, no to jest to tak płynne, że szok, bo to już jest przejść z analizy biznesowej do systemowej.

**Janusz Bossak** 47:35  
No tak dokładnie, bo to jest dokładnie ten krok pomiędzy tym, a pb im to jest dokładnie ta różnica, to jest biznesowe.

**Damian Kaminski** 47:37  
Bo.  
No dobra, to jeszcze inaczej bym powiedział, czyli tak robię PAII piszę proszę opisać endpoint.  
Jakie będą do tego i wycenić do tego effort tak opis wymagania co muszą ten point zawierać biznesowo jest poziom wyżej, czyli na poziomie fischera, tak?

**Janusz Bossak** 48:01  
No bo no tak znaczy nie wiem czy trzeba ich tam jakoś.  
W taki sposób, że tu opisz tylko po prostu trzeba by wziąć ich na spotkania. Przykład tam godzinę powiedzieć, słuchajcie.

**Damian Kaminski** 48:13  
No albo tak jasne, jasne no.

**Janusz Bossak** 48:17  
Co według was jest do zrobienia, żeby zadziałało to wyświetlanie tego hierarchicznego, tego, co jest tutaj zrobione? Tak czy tu będzie?  
Ppnt.  
No jak pomiędzy tym, a tym jest taka przestrzeń, że musi powstać, muszą powstać endpoint tak to można by teraz tak se myślę, można by nawet tak zrobić.  
Pracowanie.  
Pracowanie d point.  
Na razie to bardzo skrótowo tak, ale chodziło mi o ideę, jeżeli tak byśmy to zrobili, to teraz. Zobacz.  
I te opracowaniem point jak damy tu to mi się układa to w takie coś tutaj jest robota w bazie danych, tabelki, dodanie jakiegoś może.  
Kolumny w jakiejś tabeli tam kejsa nie wiem.  
Yy właśnie zapewnienie tej struktury.  
I tu do tego takie PI powinno być tak zapewnienie tej struktury po stronie story dżu tak wszystko to.

**Damian Kaminski** 49:28  
No zgadzam się z tobą, ale właśnie to teraz masz tą rozterkę, którą ja właśnie miałem wczoraj.  
Bo teraz przechodzisz od funkcjonalnych, czyli drzewo folderu, zapewnienie wyświetleniach i energicznego do takiego podziału na obszary, czyli tu backend student pointy, a wtedy dopiero frontend, więc pytanie teraz, co tutaj w tym drzewo, co co tutaj wtedy ująć w tym co podświetla sz.

**Janusz Bossak** 49:54  
O tym co podświetlaniem według mnie to jest to, co mamy gotowe.

**Damian Kaminski** 49:57  
Czyli tylko front.

**Janusz Bossak** 49:59  
Tylko front.  
I to nawet tutaj nie tu można pisać, że to jest.

**Damian Kaminski** 50:02  
No o k.  
No to znaczy bardziej w drugą stronę jest krytyczne, żeby wpisywać BE tam gdzie nie ma nic testerem do testowania nie, ale to już na poziomie pkb i nawet a nie tutaj ficzerów, bo to to już tak się sprawdziło dziewczyną, więc myślę, że będziemy w ten sam sposób tu podchodzić.

**Janusz Bossak** 50:17  
No tutaj.

**Damian Kaminski** 50:28  
No okej, no to to to jest jakieś wyjście, można to tak przedstawić, że najpierw zbudujcie całą bazę i wszystko, a potem jako garaże się, że czegoś brakuje. No to w ramach poszczególnych, bo czegoś nie przewidzieliśmy w założeniach początkowych, to w ramach już pojedynczego tego juan drzewa po folderów może się okazać, że tu jednak stworzymy jeszcze dodatkowy PI, bo tam jeszcze musi się coś nam dołożyć. Czego?  
Na poziomie wstępnego przygotowania weekendu nie założyliśmy tak, bo nie przewidzieliśmy takiego scenariusza.

**Janusz Bossak** 50:59  
To na przykład przesunąłem to wyżej, bo tak patrząc biznesowo to będzie na pewno pierwsze potrzebne. Tak, czyli mamy to przeglądanie struktury folderów, no i to już jest zrobione.

**Damian Kaminski** 51:00  
No.

**Janusz Bossak** 51:12  
Czyli nie wiem czy jest wyszukiwanie i czy jest wyszło.  
Kiwanie folderu i pliku no na pewno jest zwykłe przeglądanie tak, czyli poruszanie tu można nawet dodać tak tak.  
Taki just case.  
Bo to tytułem poruszanie się.  
Się no i.  
Się to.

**Damian Kaminski** 51:36  
To masz miejsc, kliki jakieś.  
Ale tak lubisz tak?

**Janusz Bossak** 51:39  
Nie no na tym na tym tym jedynym miejscu, czyli na mazurze.  
Alt czy obrzyn a.  
Czyli on inaczej. Ja bym chciał napisać to jest powiązane z tutaj nie wiem, aria tu jest podkreślenie.

**Damian Kaminski** 51:57  
Ha.

**Janusz Bossak** 51:59  
I alt, a zamiast wpisywać on to mi przeskakuje tutaj al MI wskakuje tu w stat nie M jak pisze to on jak piszę to tutaj wskakuje i nie da się tego zrobić inaczej znaczy muszę.

**Damian Kaminski** 52:08  
Aha.

**Janusz Bossak** 52:14  
Znaczy pamiętać, bo to jest ten powinien po.  
Że.  
Wie.

**Damian Kaminski** 52:20  
Mnie to tak nie działa, no ale to może tylko na maku.

**Janusz Bossak** 52:22  
Nie wiem jak maka, nie wiem czy masz maka.

**Damian Kaminski** 52:25  
Nie, nie mam.

**Janusz Bossak** 52:26  
No jakoś tu jest widocznie.  
Jakoś tam podpięte pod to samo i nie znalazłem sposobu na to, żeby to zmienić. Tu jedyne co mogę na maku robić to trzymać dłużej EI wtedy się pojawia lista i mogę nadążyć jedynkę i się robi to, ale dobra poruszanie się po drzewie folderów.  
I to pewnie mamy zrobione jako pierwsze.  
Tak, bo może tego nie będziemy robić w pierwszym na przykład iteracji, wyszukiwanie i wyszukiwanie pliku, to będzie trzeba przerzucić do na przykład innego.  
Yy, mbp nie.  
Ale chodzi o to, żeby było tak, czyli poruszanie się, czyli rozwijanie zwijanie.  
Yy tam to może być określony właśnie ten wygląd, czyli trzymają.

**Damian Kaminski** 53:08  
Tak, tak, tak, mhm.  
Bo wiesz tu, może to trzeba zrobić, bo tu jak łatwo skok.  
Skopać, że tak powiem taki projekt.  
Yy, bo skopaliśmy w kontekście Orlenu i tam jeszcze czekamy na poprawkę.  
Bo jest drzewo struktury i ktoś wymyślił, że załaduje od razu wszystko.  
Tylko nikt nie pomyślał, że to drzewo struktury może mieć 10000 elementów.  
I zanim się to zbuduje, to jak ktoś klika pokaż strukturę, bo tak jest właśnie zrobione, to czeka 30 sekund na wyświetlenie ekranu.

**Janusz Bossak** 53:49  
No i to jest w tym już w tym właśnie tutaj mogło być napisanie.

**Damian Kaminski** 53:52  
I tu trzeba to napisać, że poruszanie się to znaczy mamy wyświetlić tylko najwyższe węzły.  
Albo tylko najwyższe węzły rozwinięte i zapamiętać, gdzie ktoś był ostatnio, więc wtedy rozwinąć mu też te węzły, w których był ostatnio, w którym był ostatnio jako jednym węźle i tyle, żeby to zbudować maksymalnie tam nie wiem. Widok 100 pozycji, a nie 1000.

**Janusz Bossak** 54:20  
No dobra, no to na razie możemy, żeby nie rozstrzygać jakby.

**Damian Kaminski** 54:25  
Tak, tak, tak po prostu.

**Janusz Bossak** 54:25  
Problemu to piszemy poruszanie się po drzewie.  
Możemy tutaj przeglądają, żeby tutaj dać nie przeglądanie, a wyświetlanie.  
I po ruszanie.  
Się.  
Że wie.  
Moderów.  
Dobra, no i teraz to już trochę mam więcej sensu.  
Bo tu.  
Poruszanie się podzielę, które może mieć 1000 pozycji. Tak no i to jest przypadek, który trzeba.  
Mm uwzględnić, czyli na przykład tam lazy loading cokolwiek, ale jak masz to napisane.

**Damian Kaminski** 55:18  
Tak.

**Janusz Bossak** 55:23  
I o tym teraz pomyśleliśmy, to jest duża szansa, że jednak ten.  
Deweloper też o tym pomyśli, nie w którymś momencie i teraz tu pod tym teraz zauważ tu pod tym.  
A tutaj takiego nie można. Nie wiem dlaczego może tam jakoś źle jest napisane, ale podejrzewam, że jak tak zrobię i potem to już mogę work item dowolny wziąć.

**Damian Kaminski** 55:47  
Tylko musisz child.

**Janusz Bossak** 55:50  
Tak część pt.  
I tutaj produkt item i tutaj na przykład jest.  
Za zapewnić.  
Jak nie to się pisze lasy.  
Jak się po angielsku piszę?

**Damian Kaminski** 56:07  
Las.  
Ale to o k. To znaczy ja bym nawet powiedział. Pytanie rozumiem do czego zmierzasz tak tak, tak.

**Janusz Bossak** 56:12  
No.  
Chodzi mi o przykład.  
Na przykład jakby struktury no i w tej chwili chodzi co jeszcze.

**Damian Kaminski** 56:19  
No bo.  
Tam może w strukturze to akurat tak nie będzie zlezie loading szybciej bym powiedział już w plikach, ale w strukturze po prostu najprostszy jest to, że mamy ktoś wchodzi, mamy wyświetlić górne wiersze i jeszcze nie wiedzieć frontend owo górne wiersze mam na myśli te przestrzenie tak, żeby to i nie wiedzieć o tym, co jest wewnątrz. Dopiero jak ktoś klika strzałkę. Rozwiń tą przestrzeń to idzie zapytanie, a podaj mi teraz na zastępników tego.  
I dopiero to budujemy.  
Bo to zakładam, że to tak musimy zrobić, bo no Piotr o tym też mówił, że.  
Kontekście formularze już teraz nie pamiętam, ale w kontekście formularze, że.  
Po co my od razu pytamy o wszystko zamiast pytać dopiero jak jak ktoś tam wejdzie, ale nie pamiętam jakiego pola to dotyczyło. Oni mniej był taki przypadek.

**Janusz Bossak** 57:10  
Tak, tak.  
To jest no dobra.  
Mieliśmy dalej co jeszcze?

**Damian Kaminski** 57:15  
No dobra, ale to to wiem dobra zarządzać, czyli tak mamy sposób przechowywania folderów, drze tylko tak sposób przechowywania folderów i dokumentów. To tu rozumiesz wczytywanie.

**Janusz Bossak** 57:27  
Nie to rozumiem pracę nad strukturą tego, gdzie to ma się zapisywać tak czyli.

**Damian Kaminski** 57:31  
O k.  
Dobra dobra, czyli cały ten kod obsługujący.

**Janusz Bossak** 57:36  
Poziom.  
Znaczy, to jest poziom baza danych historycznie nawet nie backend, czyli nie aplikacji, a tylko baza danych historycznych. Tu jest aplikacja, która czyli backend, który przetwarza to, co jest zapisane w bazie danych.

**Damian Kaminski** 57:42  
Dobra.

**Janusz Bossak** 57:52  
Na endpoint, które dostarczają informacji, a tu mamy josé interfejs, który.  
Poprzez ten pointy odczytuje i wyświetlane.

**Damian Kaminski** 58:03  
O k. No to teraz pytanie, czy zarządzanie strukturą folderów, skoro tu jest strukturą, to może niekoniecznie zarządzanie uprawnieniami? Tak.

**Janusz Bossak** 58:11  
Bo tu jest.

**Damian Kaminski** 58:12  
Może to powinien być, a tu już jest drzewko uwzględniają.

**Janusz Bossak** 58:14  
No można to nazwać zarządzanie uprawnieniami tak ogólnie.  
Możemy to bardzo tak.

**Damian Kaminski** 58:19  
No tak, bo tam trzeba będzie nadać, tu już trzeba będzie rozpisać jakieś juz kasy, czyli jak nadać i potem.  
Bo przeglądania, bo gdzieś też trzeba opisać kto jakie ma potem funkcję już na poziomie folderu, czyli aplauz, czyli usunięcie.

**Janusz Bossak** 58:37  
Tak.  
No to tak to zmieńmy, niech to będzie.

**Damian Kaminski** 58:44  
No i co ostatnie to już zarządzanie plikami bym powiedział.

**Janusz Bossak** 58:46  
Teraz wiem, nie wiem czy te zarządzanie uprawnieniami nie powinno być w sumie wyżej.  
No bo.  
Jak the endpoint będą nam coś zwraca, są one powinny te względzie, ale może nie.

**Damian Kaminski** 58:59  
Tak.

**Janusz Bossak** 59:02  
Bo może na początku.

**Damian Kaminski** 59:03  
Nie musi być to na początek, no właśnie.

**Janusz Bossak** 59:05  
Dokładnie, bo możemy zwracać po prostu całą strukturę i to może być w mbp jeden, a web 2 zrobimy zarządzanie uprawnieniami.

**Damian Kaminski** 59:16  
No k zostaje teraz.

**Janusz Bossak** 59:22  
Co z tego?

**Damian Kaminski** 59:22  
Przeglądanie folderów, bo to już nie jest struktury, tylko przeglądanie folderów i tu bym powiedział, że tutaj twoje lazy loading musi być.  
Czyli jak mamy w folderze?  
Te powiedzmy 2000 plików to my chcemy wyświetlić na początku tylko 50, a jak ktoś, ze to kolejnych 50.  
Czyli jak już jesteś w jakiejś strukturze, to jak ci się wyświetla to co widzisz nie w sensie jak jesteś jakimś folderze?

**Janusz Bossak** 59:50  
No to czyli to jest przypadek użycia w tym miejscu? Tak.

**Damian Kaminski** 59:51  
Czyli.

**Janusz Bossak** 59:56  
Bo jak poruszam się po drzewie folderów, no to w którymś momencie trafiam na taki folder, w którym są dokumenty.

**Damian Kaminski** 1:00:02  
No tak, no pytanie, czy ty to tak interpretujesz, bo można tak jak mówisz tak można to tu ująć, albo to traktować jako tylko poruszanie się po nawigacji, czyli ja w ogóle nie patrzę na obszar roboczy, tylko poruszam się po nawigacji odrębnym.

**Janusz Bossak** 1:00:15  
Gdzie jest gdzie jest ten zrobiony u Filipa?

**Damian Kaminski** 1:00:19  
Wiesz co u Filipa nie ma, więc wejdźmy już ci daje dostęp, wejdźmy na ten mój mop, ach, bo Filip coś tam musiał przełączyć i wywalił to na razie z ze swojej.  
Yy już ci daje filma.  
Pozytywna i love.

**Janusz Bossak** 1:01:10  
Jakby Filip z tego zrobił jakiś osobny branż i to miał na razie dostępny one, bo to jest dosyć istotne.  
Mi tam Filip kreska, repozytorium czy cokolwiek żebyśmy.

**Damian Kaminski** 1:01:24  
To znaczy, no, widzisz pytanie czy Filip, bo jak oni mają te lokalne, to mogą się we 2 podpiąć do lokalnego?  
Zmierzam do tego, że tak on będzie właśnie, bo tu mamy taki przypadek, tak jak z tymi.  
Te raportami, że było raporty, a modecom i czy jakoś tam, czy lokal i właśnie jeśli to ma być praca równoległa backend owców i frontendowców to ja rozumiem, że oni powinni mieć jedno stanowisko właśnie takie nasze wydanie owe, gdzie już my będziemy lokalnie widzieli jak to m wi, p jeden postępuje, ale mamy jeszcze to podzielone jeszcze poziom niżej, czyli mamy kroki w ramach tego m wypita ktoś zrobił, to mamy do tego n ponieważ mamy do tego frontend no to wydajecie łączycie te wasze 2 branże i.

**Janusz Bossak** 1:02:12  
No tak no.

**Damian Kaminski** 1:02:12  
I sprawdzamy, jak to działa, nie?

**Janusz Bossak** 1:02:14  
Można zrobić coś takiego jak nie wiem raporty, a młody trochę było, że nie było takiego czegoś, no ale powiedzmy, że mogło być.  
I tu możemy zrobić repozytorium kropka kropka lokal.  
I tam będą różne osoby w tą mediować. Tak może mediować. Nie wiem. Ania, która będzie robiła Weekend, może mediować Filip, który był który wyrokiem frontend, ale my na naszym poziomie będziemy tam mieli jakby aktualną wersję tak, a nie tak, że tutaj zaglądasz do Filipa, tam zaglądasz do ani, ale to nigdzie nie jest połączone, nie.

**Damian Kaminski** 1:02:35  
Dokładnie.

**Janusz Bossak** 1:02:50  
I każdy coś robi swojego, a guzik widać z tego, no więc taki deweloper, ale tylko i wyłącznie na to repozytorium, dopiero jak zrobimy to repozytorium, to wtedy dopiero ono wchodzi do amo tita jako takiego nie.

**Damian Kaminski** 1:03:06  
Mhm.

**Janusz Bossak** 1:03:07  
Tutaj problemu Marek się pyta, czy my mamy gdzieś dostępną?  
Podsumowanie odnośnie tego jak pisać dokumentację do nowych projektów na wiki, ale do nowych projektów.  
Chciałbym opisać zmiany z usługami w ten sposób dodać planowanie kolejnych iteracji.

**Damian Kaminski** 1:03:28  
Ale na jakim wiki naszym wiki?

**Janusz Bossak** 1:03:31  
Gaby chodzić?

**Damian Kaminski** 1:03:36  
Nie naszym.  
To do tego teraz senter.

**Janusz Bossak** 1:04:00  
Dobrze wróćmy tutaj do naszego.  
To jest tutaj, tak.  
Co tam jeszcze musimy zapewnić to z tych grubych funkcjonalności. Co tam masz w tym?

**Damian Kaminski** 1:04:20  
Wysłałem ci, albo mogę pokazać tak, bo może.  
Może ja po tym się lepiej poruszam. No jak chcesz, jeśli chcesz sam klikać to to proszę bardzo.  
Więc powiedziałbym, że na razie to omawialiśmy tylko właśnie tą środkową kolumnę, tak?  
Ee.  
A teraz trzeba jeszcze omówić ten obszar roboczy.

**Janusz Bossak** 1:04:47  
Znaczy, no to on tu już jest tak jakoś tam.

**Damian Kaminski** 1:04:50  
To znaczy to tak tylko to jest. Wiesz, to nie jest samolot, nie.

**Janusz Bossak** 1:04:53  
Mam 2 modlicie? Jest już to zrobione, tak.

**Damian Kaminski** 1:04:55  
Tak, tak, tak, tak, tak, tak.  
No i tutaj właśnie na tym obszarze roboczym, tu jak najbardziej lezy loading musi być zastosowany to jest jedno.  
No właśnie kto widzi przyciski? Dodaj plik nowy folder tylko ci co mają przynajmniej uprawnienie edycję albo są administratorami. No to to już jest właśnie taka.

**Janusz Bossak** 1:05:17  
A są te przypadki użycia?

**Damian Kaminski** 1:05:18  
No właśnie i teraz pytanie czy to jest?  
Ja bym chyba tego nie łączył. Wiesz, w sensie dałbym to, bo bo wtedy jak to połączymy to ten fixer tak jakby jest bardzo duży.  
A jednak jak byśmy się skupili na Twitterze w kontekście tylko?  
Tylko struktury. No to jeśli struktura się buduje się wyświetla, wyświetla się zgodnie z uprawnieniami.  
No to w zasadzie mamy strukturę zamkniętą to, że nam się tu wyświetla czy też nie wyświetla w obszarze roboczym to co wynika z tego folderu struktury, na którym jesteśmy. No to już jest wtórne, to teraz już się zajmujemy, żeby właśnie wynikało.

**Janusz Bossak** 1:06:02  
No dobra, czy wiesz, możemy zrobić tak, że ty przejmiesz tamten.

**Damian Kaminski** 1:06:06  
Też to jest.  
A może i to w można połączyć, bo to w sumie bez uprawnień nic nie zrobimy, a uprawnienia są w obszarze roboczym. Dobra, możemy to łączyć. No powiedz, co mam przejąć?

**Janusz Bossak** 1:06:17  
Chodzi mi o to, że możesz ty tutaj pisać to co ja tutaj piszę.

**Damian Kaminski** 1:06:20  
Tak, tak, tak.

**Janusz Bossak** 1:06:22  
Yy, a potem możemy zrobić taki test za pomocą tego jaja, tak czy on to uznaje za właściwy fischer za duży, za mały i tak dalej.

**Damian Kaminski** 1:06:26  
Przegląd.  
A jak to zrobisz?

**Janusz Bossak** 1:06:33  
I czy?  
Mogę go się pytać po prostu nie.  
Tak, robię tutaj.  
Jemu to już się w głowie miesza, bo już się było tyle rzeczy pytam i.  
Strasznie długo tutaj pracuję wątek.  
Ale na razie daje radę, nie jest naprawdę.  
Dzięki temu, że to jest w jednym wątku z 2 tygodni.  
On skubany jest to wszystko pamięta nie i jakby zna tą całą moją strukturę.  
Jakie mam?  
Klasyfikacje i tak dalej, więc to jest fajne. No dobrze, no ale.

**Damian Kaminski** 1:07:15  
Ale nie poczekaj w sensie, no jak masz to tutaj, to teraz będziesz to po prostu przepisywał jak jak okej. No właśnie, bo tu tego byłem ciekawy jak jak ty chcesz to wrzucić do je.

**Janusz Bossak** 1:07:20  
Tak, tak, tak no.  
Nie.  
Tak po prostu kontrolce.

**Damian Kaminski** 1:07:28  
O k. Rozumiem dobra dobra myślałem, że masz jakiś sprytniejszy.

**Janusz Bossak** 1:07:31  
I.

**Damian Kaminski** 1:07:33  
Już patent na to.  
No dobra, no ja mniej więcej to rozumiem, mogę to tym się zajmować i dać ci znać jak uznam, że.  
Jest to skończone, powiedzmy na poziomie ficzerów, potem będę schodził gdzieś tam poziom niżej i tak żebyśmy no pytanie teraz bierzemy do tego Mariusza.  
A nie też w to angażujemy.

**Janusz Bossak** 1:07:57  
Znaczy nie wiem, no.  
Najpierw spiszmy to co tutaj, czyli nasze wyobrażenie tego, co jest do zrobienia tak czyli funkcjonalności ill, potem są, musimy to ustawić w kolejności, które są absolutnie niezbędne. No na pewno tą strukturę trzeba zrobić tak, bo inaczej to bez sensu. Bardzo fajnie, że mamy ten frontend.

**Damian Kaminski** 1:08:06  
Dobra.

**Janusz Bossak** 1:08:21  
Yy, wiesz, tutaj nawet nawet chociaż to nie jest rzecz, którą dowozimy.  
Tak się zastanawiam czy jako.  
Ten trybik.  
Może być taka techniczna rzecz, jak na przykład dla nas umożliwienie tego zapisywania jako branż nie.  
Osobny i żebyśmy to widzieli na jakimś tam właśnie repozytorium, a modlitwy lokal tak, to możemy sobie.

**Damian Kaminski** 1:08:49  
W sensie, że to miał być zadanie jako feather, tak.

**Janusz Bossak** 1:08:52  
To jest, no to jest zadanie, to jest zadanie dokładnie.

**Damian Kaminski** 1:08:56  
No ok tylko.

**Janusz Bossak** 1:08:57  
Oni nie wiedzą, że mają to zrobić tak i to może być zadanie.

**Damian Kaminski** 1:08:59  
Nie ma się pytanie, kto ma to zrobić, to trzeba pewnie Mariusz tego Michała pytać.

**Janusz Bossak** 1:09:03  
No to Michał na przykład tak o to chodzi, ale jak zaczynasz tak rozpisywać.  
To i po prostu zapisujesz takie rzeczy. Zresztą to zaraz zrobię.  
Zapewnienie.  
Na przykład repozytoriów.  
Kropka ale.

**Damian Kaminski** 1:09:32  
Od razu piszę to do do Michała.

**Janusz Bossak** 1:09:35  
Tak i to i to masz fischer, my i nie ma problemu tak, bo wiesz, że ktoś to ma zrobić.  
To jest pierwsze zadanie w ramach tego wszystkiego, no bo inaczej bez tego się nie da tego zrobić. Tak to może być w ogóle jako wydzielone jako mbp Zero.  
W ogóle przestrzeń, gdzie będziemy to sobie ćwiczyć, robić i tak dalej, więc o to chodzi. To jest lista takich rzeczy, zadań właściwie po części większych kawałków do zrobienia.  
Ale patrz, no z punktu widzenia tego, żeby no dowieść cel.  
No dobra.

**Damian Kaminski** 1:10:14  
Dobra teraz pytanie zasadnicze ten branż, na do której wersji mnie to wydajemy?

**Janusz Bossak** 1:10:22  
Nie wiemy pytanie, którą wersję będzie miało ostatecznie?  
Ten.  
Bim.

**Damian Kaminski** 1:10:30  
No.  
Powiedziałbym tak, nie powinniśmy tego upychać do czerwcowej, tylko pytanie, czy my grudniową będziemy w stanie ustabilizować na tyle.  
Żeby potem na ostatni moment nie wypychać tego do czerwcowej, bo nie wiem jak to potem zrobić. Jeśli zdobędzie, nie wiem 50 stopi BI to będzie pewnie dużo roboty.  
Więc no najchętniej byłoby to wydawać jednak do przyszłej, tylko przyszła.  
A będzie stabilna.

**Janusz Bossak** 1:11:06  
Ja nie znam odpowiedzi na to.

**Damian Kaminski** 1:11:08  
Tyrnowo no ja ja wiem, że nie znasz, więc pytanie czy robić to.

**Janusz Bossak** 1:11:09  
Mam taką samą rozkminkę w głowie jak ty, no.

**Damian Kaminski** 1:11:13  
Tak tak, no dlatego, że tak powiem uzewnętrzniam, żeby też lepiej podjąć, że tak powiem decyzję dyskutując na nią niż nie dyskutujący i potem w zasadzie się zastanawiać tak, gdybym zapytał, to może by było lepiej.

**Janusz Bossak** 1:11:32  
Znaczy no są to jakby ambiwalentne uczucia. Tak z jednej strony lepiej to czerwcowej, no bo wszystko inne jest tam jakoś powiedzmy, że ustabilizowana, a przynajmniej.  
Jakiś tam sposób przejrzane.  
A z drugiej strony.  
No może nie już nie nie upychać do tej nowej, no ale wtedy w tej znaczy do tej starej, czyli czerwcowej, a dać to w nowej, no ale wtedy ryzykujemy wszystkim innym, nie.  
Że coś jest, jest stabilne i tak dalej, więc.

**Damian Kaminski** 1:12:03  
Dokładnie.

**Janusz Bossak** 1:12:06  
Nie wiem, nie mam na to dobrej odpowiedzi.  
Bardziej się skłaniałbym do tej czerwcowej, no.  
Tym bardziej, że komunikator daliśmy do czerwcowej, tak?  
No tyle.

**Damian Kaminski** 1:12:23  
No właśnie i tutaj są te nasze.

**Janusz Bossak** 1:12:24  
Może może może jakaś wrześniowa, której teoretycznie zrezygnowaliśmy jako pośredniej.  
Ale może dla filmu to taka wrześniowa taki trochę czerwcowa, ale trochę bardziej nie.

**Damian Kaminski** 1:12:37  
Tylko, że nie zrezygnowaliśmy. Wiesz, obawiam się, że potem wiesz jak będzie czerwcowa.  
To może nam narobić więcej problemów niż korzyści.  
Bo będzie tak będą poprawki do do do czerwcowej, a potem ktoś powie zaraz, a tutaj to działa o klienta nie, no to wydajemy, narasta o kolejne do testów, więc.  
Już według mnie lepiej do czerwcowej niż do jakieś pseudo wrześniowej, bo tylko będzie trzeba dodatkowe poprawki, dodatkowe testy robić.

**Janusz Bossak** 1:13:05  
No tak tak.  
No pytanie jest.

**Damian Kaminski** 1:13:09  
No powinniśmy powiedzieć, że grunt do grudniowej, no taka jest, prawda? Powinniśmy dzisiaj powiedzieć, że do grudniowej to i tak jest.  
Szybko, ale.

**Janusz Bossak** 1:13:20  
Rozsądek mówi, że do grudniowych nie.  
Lepiej grudniową i grudniową stabilnym.

**Damian Kaminski** 1:13:25  
Nocowałem w tej grudniowej nowego robimy tylko te.  
Uprawnienia.

**Janusz Bossak** 1:13:29  
No właśnie, może może niewiele będziemy robić tak, bo jednak może nie damy tych edytorów wszystkich jeszcze no.

**Damian Kaminski** 1:13:36  
No właśnie, żeby żeby wydać się, żeby ona poszła i żeby zamykać znowu już zaraz czerwcową i tylko grudniową wspierać.

**Janusz Bossak** 1:13:43  
Dokładnie tak też tak mi się wydaje.

**Damian Kaminski** 1:13:44  
Back up chamy tyle tych nowości, no to potem dlatego to ciągniemy, bo upychamy tak dużo, że trzeba dużo poprawiać i.  
I no właśnie i to się.  
I to się ciągnie, dobra?

**Janusz Bossak** 1:13:56  
Tak zrób.  
Pewnie będzie to grudniu woli.

**Damian Kaminski** 1:14:00  
Dobra, to tak pisze michałowi, że to jest.  
No dobra.  
To chyba.  
Chyba wszystko.  
Kontynuuje pracę nad tym, co zaczęły się. No to jeszcze spojrzę, to widzę, zakładam wszystko, więc dobra, tylko tak ty zacząłeś budować to od nowa. Ja na razie to co jest, że tak powiem, zostało zbudowane przeze mnie. Zostawiam w celach dowodowych, później to po prostu się usunie, bo to są, powiedzmy, pewnego rodzaju duplikaty.

**Janusz Bossak** 1:14:29  
Dobra.  
Ale co mówisz te rzeczy?

**Damian Kaminski** 1:14:45  
No bo ja już zrobiłem oddzielny epik na ten repozytorium, to zrobiłeś to od nowa, więc.

**Janusz Bossak** 1:14:48  
Dobrze dobrze, no to to to.  
Możesz pousuwać możesz tym, ale choć nieco wyżej, mniej więcej o co chodzi, no chodziło mi o to, żebyśmy złapali jakby rytm taki.

**Damian Kaminski** 1:14:52  
Później to pomysł.

**Janusz Bossak** 1:14:59  
Pracy nad tym, no bo to są nowe rzeczy, które zaczynamy, jakby wdrażać też w sensie modelu pracy.

**Damian Kaminski** 1:15:08  
Mhm.

**Janusz Bossak** 1:15:09  
Mówię no te moje dyskusje z tym jajem, zresztą bardzo tak już wielokrotnie powiedziałem, ciekawe.  
Bo go mocno, że tak powiem utwierdziłem jako takiego strażnika imię tam.  
Krytykuje co chwila i bardzo dobrze.  
No główna krytyka jest ciągle, to nie jest worek funkcji.  
Mwp to jest wartość, zresztą ma w nazwie belimo.

**Damian Kaminski** 1:15:36  
Tak, tak, tak, tak tutaj się zgadzam z tobą, że tak to nie jest worek niepowiązanych funkcji tylko jak robimy m wi, p minimalne no to właśnie tak jak do tego podchodzimy, czyli coś co daje się już używać jest ograniczone, ale jest użyteczne, a nie że można wgrać plik, ale nikt go nie zobaczy.  
No to można wgrać.  
Nie, nie ma wartości, no to jest funkcja tylko.

**Janusz Bossak** 1:16:01  
Właśnie teraz.  
Tak, czy na przykład wartością dla klienta byłoby mu danie tego frontendu samego.

**Damian Kaminski** 1:16:09  
No nie no właśnie, bo to jest przegląd funkcji.

**Janusz Bossak** 1:16:09  
No nie, no nie, no bo no bo to jest mop nie, a nie wartość żadna tak, no bo on nic nie może tam zrobić.

**Damian Kaminski** 1:16:14  
Tak.

**Janusz Bossak** 1:16:19  
Tak więc, ale.

**Damian Kaminski** 1:16:21  
Co tu się rozumiemy? Tu akurat mam pełne zrozumienie dla tej dla tej logiki.

**Janusz Bossak** 1:16:26  
Natomiast danie czegoś co nie ma na przykład uprawnień, ale mogę już zapisywać, to już jest jakaś wartość tak, bo już mogę zacząć zapisywać.

**Damian Kaminski** 1:16:32  
Tak no bo to już tak.

**Janusz Bossak** 1:16:35  
Mam po prostu tak, jakby wspólny folder dla wszystkich czy wspólne foldery dla wszystkich o k. Tak potem mogę oddzielić te o tu też warto w tym naszej strukturze funkcjonalności, by dzielić, bo podejrzewam, że jest osobny przypadek użycia.  
Yy to jest.  
Nie przestrzenie, tak, to nazwałeś przestrzenie, nie obszary tego przestrzeni, bo to z przestrzenią się coś tam wiąże. Tak wiąże się właśnie ta gałązka uprawnień i tak dalej, więc.  
Tutaj gdzieś jak jest zarządzanie strukturą folderów, to pewnie tutaj powinno być u s klase.  
Tworzenie.  
Nowej.  
Przez 3 dni tak?  
No to jest specjalny to, że nie nowej przestrzeni, no bo dopiero w tej przestrzeni reszta się dzieje. My czyli tu musi być pierwsze.

**Damian Kaminski** 1:17:28  
Mhm.  
Tak.

**Janusz Bossak** 1:17:33  
No i jeszcze jak tak to rozpiszemy.  
Znaczy już tak, podsumowując, żeby już nie nie więcej nie nie ciągnąć.  
Ja pamiętam, że ja przez długi długi czas do teraz mocno naciskałem na pisanie tych opisów projektów w ramach wiki.  
No bo taki miałem pomysł, nie, że tam jest ta koncepcja biznesowa, tam są te właśnie MVWPI tak dalej i to teraz, jak tutaj przepracowałem to w głowie mocno to wydaje mi się to jest połączenie tej mojej potrzeby, takiej mojej wizji, tworzenia tych opisów i tego, co wy bardziej jakby lubicie, jesteście bliżej tego, czyli backlogu i o k, tak dla mnie to jest o k. To jakby łączymy 2 koncepcje, jest projekt rozpisany.

**Damian Kaminski** 1:17:55  
Mhm.

**Janusz Bossak** 1:18:25  
Wiadomo, co jest do zrobienia teraz, co jest do zrobienia w przyszłości, co jest jakimś blogiem pomysłów do tego projektu.  
I to jest super. To jest super.

**Damian Kaminski** 1:18:34  
Mhm, znaczy.  
Wiesz, teraz tego wszystkiego to znowu, bo ty mówisz, że teraz mecz to kupiły, bo tu będzie to jakaś struktura która.  
No będzie zawierała pewnie między.  
Pięćdziesiąta 100 węzłów. Tak zakładam.  
Różnych.  
No i mówisz, że będziemy to wali dawać ze jajem, jeśli mamy do tego tak podchodzić i potem na podstawie tego opisu, który tu mamy powiedzieć, stwórz mi teraz do tego dokumentacja, to mam tu wszystko napisane, w zasadzie moje wytyczne.  
Zróbmy to dokumentacja, ja tylko z redaguję to my to też powinniśmy zrobić, w sensie wam odejdzie, albo przynajmniej wsad do tego zapytania do prom pta, czyli te wszystkie rzeczy trzeba teraz pobrać wam olicie odpowiednio zareagować na jednym widoku, żebym mógł zaznaczyć kontrolce i powiedzieć tu jest cały zakres projektu.

**Janusz Bossak** 1:19:17  
Się.  
Jest coś takiego jak create query tak czyli był ogólnie bierzesz query w query wrzucasz wszystko co ma ten rodzica takiego i robisz na przykład eksport do csv, csv a wrzucasz do.

**Damian Kaminski** 1:19:37  
O Ki tu kopiujesz?  
O k.  
Ale nie mam pytań, już wiadomo wiem o co chodzi.

**Janusz Bossak** 1:19:47  
Jakiegoś.  
I też stworzy nie to taka prosta metoda, ale tak to jest to znaczy ta robota, którą teraz robimy.

**Damian Kaminski** 1:19:50  
Prościej.

**Janusz Bossak** 1:19:59  
To zauważ po pierwsze i tak tym trzeba zrobić.

**Damian Kaminski** 1:20:00  
Me uprościć potem. No właśnie tak tak czas trzeba poświęcić, bo jak nie zaprojektujemy dobrze to to źle dostaniemy.

**Janusz Bossak** 1:20:07  
Tak, a projektując to dobrze, oszczędzamy nasz czas na czas naszych deweloperów. Czas naszych testerek i nasz czas później na tworzenie dokumentacji, bo to już będzie raz zrobione dobrze zrobione, łatwiej to przetestować, łatwiej to wytłumaczyć.  
Nie ma takich dyskusji jak tutaj z Łukaszem z anią, czy z kimkolwiek tak, ale nie, bo ja to myślałem, czy myślałam, że to tak nie, albo zrobię jeszcze xs SLT, no nie, nie rób XLT, bo gdzie?

**Damian Kaminski** 1:20:38  
Tak powiem ci, ja nie wierzę w ich czytanie ze zrozumieniem. Nie ja teraz wiem, byłeś na tym czacie, ale to może nie zaglądałeś za brianem. Ja pytam o jedno, a on odpowiada drugie te drugie też jest interesujące, ale on nie zrozumiał pytania, ja uważam, że po tym rozpisaniu trzeba się spotkać i Jeszcze raz wytłumaczyć, a i tak będzie za mało.

**Janusz Bossak** 1:20:56  
To jest.  
Adrian jest dobrym tego przykładem, bo jakby miał tak rozpisane rzeczy.  
Tak do do nadawcy czy do innych to nie robiłby.  
Pierdyliona rzeczy niepotrzebnych on chłopak jest po prostu tak mocno zaangażowany, że on najchętniej to bym od razu wiesz, wszystko zrobił nie.

**Damian Kaminski** 1:21:17  
No tak.

**Janusz Bossak** 1:21:17  
No nie ma spojrzenia biznesowego, ona spojrzenie techniczne, że to się da, to po co nie?  
To jest.

**Damian Kaminski** 1:21:24  
Znaczy, no właśnie to znaczy trzeba tylko dobrze ukierunkować tych ludzi, bo jak ktoś się pali robotą, którą robi, to się na to przyjemnie patrzy, to szybko idzie, kto się zaangażowany, ktoś się dzieli i spostrzeżeniami wprowadza właśnie jakieś nowości tak jak ktoś tylko robi to co napisane.  
Nie, nie czerpie z tego satysfakcji. No to robię, odczepcie się, no i tyle.

**Janusz Bossak** 1:21:47  
Zobacz, zobacz jak się zmieni planowanie sprintu? Tak, bo jeżeli będziesz miał teraz to repozytorium rozpisane i będziesz miał tu już wybrane 3 rzeczy.  
No ten to to jest jedyna rzecz, której wkurza mnie tutaj, czy wkurza mnie, bo tu jest mów tu i teraz NI tu mogę zrobić od razu.  
Mów to iteration.  
Do tego nie.

**Damian Kaminski** 1:22:10  
Mhm.

**Janusz Bossak** 1:22:12  
Albo do przyszły do czterdziestego siódmego tyle że to.

**Damian Kaminski** 1:22:15  
Nie przeniesie podrzędnych.

**Janusz Bossak** 1:22:17  
Nie bierze podrzędnych, nie.  
I trzeba każdą z osobna.  
Jakby wrzucać, no ale to już jest tam jakby drobiazg tak, bo może być też tak, że to.

**Damian Kaminski** 1:22:28  
Może się jakoś to da, pytałeś ja ja.

**Janusz Bossak** 1:22:31  
Nie, nie pytałem.  
No ale nie wiem może być tych pb i tu więcej, no ale trzeba wtedy je przerzucać do drugiego i tak dalej. No musimy się tego nauczyć, ale jak to zrobimy, to zobacz, to, co właśnie mówiłeś o adrianie, czy ja mówię o ani i tak dalej o tym, że oni tam nie czytają ze zrozumieniem.

**Damian Kaminski** 1:22:34  
Nie, ale mów Przepraszam.

**Janusz Bossak** 1:22:49  
Nie wiem czy to jest nieczytanie zrozumieniem, to jest to, że oni mają inne umysły, oni mają one mają, oni mają umysły, bardzo takie bym powiedział analityczne.  
I wszystkie takie nazwijmy to ify.  
Wyłapują nie od razu, a a co jeżeli tego nie będzie? A co jeżeli coś tam, a właśnie tam z tym mikser tereny, ona nie patrzy na stronę biznesową.  
Po co ma to zrobić tylko?  
Spojrzała, są takie załączniki jakich ssl to już się zastanawia jak to wyświetlacz? Tak, ale nie mamy ona nie rozumiesz one?

**Damian Kaminski** 1:23:25  
Nie przykłada, nie przykłada wagi do tego co jest potrzebne, a co możemy olać, czego wszystko traktuje na równo, no.

**Janusz Bossak** 1:23:31  
Nie rozumiem strony biznesowej, oni nie w wiekszości przypadków nie rozumieją strony biznesowej.

**Damian Kaminski** 1:23:38  
Tak no tak, tak nie nie wiedzą po co to robią, tylko rozwiązują to zagadnienie po prostu żeby zaliczyć. A no właśnie bez.

**Janusz Bossak** 1:23:39  
Oni rozwiązują.  
I po to.

**Damian Kaminski** 1:23:48  
Bez tej perspektywy, że jak ja to zrobię, to ktoś z tego będzie jakoś korzystał, tylko nie zastanawiają się jak.

**Janusz Bossak** 1:23:54  
A to jest właśnie warstwa, którą my im teraz dajemy i ja Jestem przekonany, że jeżeli tak będą oficery rozpisywane nie tak jak do tej pory.

**Damian Kaminski** 1:23:57  
Mhm.

**Janusz Bossak** 1:24:03  
To oni będą na tą ten poziom patrzyli, nauczymy ich tego.

**Damian Kaminski** 1:24:08  
No myślę, że tak, że to to jest kwestia czasu, no wszystkiego.

**Janusz Bossak** 1:24:08  
Żeby on.

**Damian Kaminski** 1:24:12  
Można nauczyć no.

**Janusz Bossak** 1:24:14  
Dobra, to działaj, a jeszcze tylko chciałem przypomnieć, że możesz korzystać już tutaj wyświetlać tego agenta, bo ja go wrzuciłem. Może nie jest tam jakoś tak super doskonałe jak ten co ja używam, no bo ten mój się po prostu nauczył wiele rzeczy po drodze tak zwanej.

**Damian Kaminski** 1:24:25  
No no no.

**Janusz Bossak** 1:24:35  
Yy, gdzie ty jesteś?

**Damian Kaminski** 1:24:36  
Gotuje.  
Ten a ja worka i te media to i on czasami mi nie działa. Nie wiem dlaczego, ale widzę że teraz się odpalił.

**Janusz Bossak** 1:24:45  
Ale gdzie to jest?

**Damian Kaminski** 1:24:46  
To już na poziomie pojedynczej rzeczy jak chcesz, napisałeś coś i chcesz to już zredagować nie, ale w sensie chodziło mi o to, że to ja wiem, że nie o to ci chodzi. To jest jak wejdziesz na feather to masz.

**Janusz Bossak** 1:24:47  
A.  
To no.  
No nie.

**Damian Kaminski** 1:24:57  
Może pokażę, bo mam to pod ręką.

**Janusz Bossak** 1:24:58  
Że.  
Już pokazuje.

**Damian Kaminski** 1:25:00  
O to ci chodzi? Tak?

**Janusz Bossak** 1:25:02  
Nie, nie, nie, nie, nie, nie to.

**Damian Kaminski** 1:25:03  
Hej child.  
Nie, a dobra, no to pokaż ty to nie wiem.

**Janusz Bossak** 1:25:09  
Chodzi mi o tutaj w tym sach?

**Damian Kaminski** 1:25:13  
A o k dobra, teraz już rozumiem. Mhm, pamiętam już co mówię.

**Janusz Bossak** 1:25:16  
Tims mów kupa pilocie.  
Jest to klasyfikacja tematów, nadzór.

**Damian Kaminski** 1:25:24  
Już sobie sprawdza.

**Janusz Bossak** 1:25:28  
I tutaj, jeżeli teraz wrzucimy?  
Tu możesz mu tam trochę opisać, tak na przykład, że.  
No bo takiego z grubej rury zapytamy.  
Wezmę to.

**Damian Kaminski** 1:25:43  
Ale poczekaj, poczekaj to.  
A tego chyba nie mam.  
A nie dobra udostępniony to wielko nie widzę tego z lewej strony.  
Już patrzę, Dodaj.

**Janusz Bossak** 1:25:56  
Ja sobie przypiąłem tutaj, więc może.

**Damian Kaminski** 1:25:57  
Tak tak, trzeba go dodać, w sensie on jest udostępniony, trzeba go.

**Janusz Bossak** 1:26:01  
Tak.

**Damian Kaminski** 1:26:02  
Zaakceptować.  
I teraz dobra, teraz widzę, mhm.

**Janusz Bossak** 1:26:07  
No i teraz możesz tu pisać typu tam tworzę.  
MVP jeden.  
Dotyczące.  
Yy.  
Budowy.  
Repozytoriom to tłumem dla naszego klienta?  
Tak.  
Żebyś tak.

**Damian Kaminski** 1:27:08  
Ale to on tylko odpowiada w cudzysłowie, tak nie, czy on jeszcze coś? No dobra, zobaczę.

**Janusz Bossak** 1:27:13  
Nie.  
Ma tą wiedzę, którą ja tutaj wypracowałem.  
Czyli ten.  
Przewodnik klasyfikacji. Ten opis tej paczki wartości i tak dalej i tak dalej nie.  
Mm.  
No i teraz tak na podstawie obu dokumentów przewodnik klasyfikacji możemy.  
Dobrze wydaje to wspólną wartość do użytku. Nie czy można to wydać? Niezależnie więc to MP nie jest tak dobrze. Czy to jest trybik?  
Trybik to dobrze zdefiniowany component funkcjonalny, który jest częścią większego, jeśli nie może być wydany, niezależnie nie daje samodzielnych. To jest trybikiem wniosek, środowisko testowe to trybik, który powinien być częścią większego mbp. Na przykład platforma, pakiet startowy administratora, repozytorium dokumentów dobrze czy to jest PBI?  
I to atomowa jednostka pracy, wynik dekompozycji funkcji w kroku szóstym środowisko testowym może być zrealizowany jako op i skonfiguruj pozyton i tak dalej. Wniosek tak, ale tylko jeśli jest już podpięte pod konkretny trybik, no nieważ odpowiedź tak, to jest właśnie po to tak, że jak masz wątpliwość jak coś nazwać, czyli gdzie to zaklasyfikować, no on ci podpowiada, albo tak, albo tak, no to resztę to my już jesteśmy ludźmi, podejmujemy decyzje tak, ale on on tutaj działa w trybie strażnika.

**Damian Kaminski** 1:28:46  
Mhm.

**Janusz Bossak** 1:28:57  
Zasad.

**Damian Kaminski** 1:28:59  
Jasne.

**Janusz Bossak** 1:29:00  
I podaje ci według niego najlepszej wiedzy, jak to tam sklasyfikować? Nie.  
Ja potem podejmuję już własną decyzję, także to jest to nie.  
No więc tutaj możesz tak wrzucać mi się go pytać oczywiście udając tam lekki kontekst, że to pracuje.

**Damian Kaminski** 1:29:17  
Tak, tak, tak, no to jest.

**Janusz Bossak** 1:29:21  
No to tyle.

**Damian Kaminski** 1:29:22  
Dobra, wszystko wiem dobra działem, no.

**Janusz Bossak** 1:29:25  
Dobra.

**Damian Kaminski** 1:29:26  
Dam znać jak skończę, no cześć.

**Janusz Bossak** 1:29:27  
Dzięki.  
Daj znać. No jeszcze jak dasz radę dzisiaj to daj znać dzisiaj.

**Damian Kaminski** 1:29:32  
Wiesz co powiem tak dzisiaj to tak będę pracował. Pewnie tam szesnasta 30 będę kończył, ale no zamierzam jutro i pojutrze jeszcze coś pozaglądać, bo tam w tym filmie też trzeba nadgonić, więc pewnie do tego też się któregoś wieczora. No chcę mieć to na poniedziałek rozpisany przynajmniej do pełnej walidacji tak przez ciebie może nie będzie to gotowe, ale żebyśmy określiłem w p.

**Janusz Bossak** 1:29:59  
Dałeś mi znać, no będę zaglądał. No tims od czasu do czasu na Weekend dobry no hejka.

**Damian Kaminski** 1:29:59  
Będę będę pisał.

**Janusz Bossak** zatrzymano transkrypcję
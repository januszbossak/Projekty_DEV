# 2025-09-16 Rada developerów

**Data:** 16 września 2025
**Uczestnicy:** Anna Skupińska, Janusz Bossak, Kamil Dubaniowski, Damian Kamiński, Piotr Buczkowski, Łukasz Bott

---

## Tematy
- **Edytor formularza:** Problematyka pól pustych, placeholderów i zachowania układu formularza przy ukrywaniu pól.
- **Zgłaszanie błędów:** Ustalenie kanałów komunikacji (Teams vs Backlog) i roli "opiekuna" tematu.
- **Trust Center:** Bezpieczeństwo nazw plików w powiadomieniach (SMS/Email) – użycie "przyjaznej nazwy dokumentu".
- **DeleteCase:** Problem z usuwaniem spraw nadrzędnych posiadających aktywne sprawy podrzędne (Connected Cases).
- **Komunikaty systemowe (Failover):** Wyświetlanie komunikatów o awarii/statusie bazy danych dla klientów On-Premise (Rossmann, LPP).
- **Problem z wylogowywaniem:** Synchronizacja wylogowania między kartami w przeglądarce.
- **Analiza wydajności:** Zgłoszenie klienta dotyczące wolnego działania bazy danych.

---

## Transkrypcja

**Anna Skupińska**: Cześć.

**Janusz Bossak**: Cześć. Pytanie, czy mamy jakieś tematy narady? Przepraszam, nie macie gdzieś tam spotkania?

**Anna Skupińska**: W sensie czy **Source Delete** został już opracowany czy nie?

**Janusz Bossak**: Nie wiem.

**Kamil Dubaniowski**: Na pewno bym miał jeden temat, właśnie z Przemkiem skończyłem rozmowę odnośnie edytora formularza i jednego ze zgłoszeń od Mateusza Kołakowskiego. To jak nie ma tematów, moglibyśmy potencjalnie o tym pogadać. To chyba jeśli Anna i tak pełnego składu... Piotrek też warto, żeby posłuchał o tym.

**Anna Skupińska**: Tak, to **Source Delete** to o ile pamiętam chcieliśmy zupełnie przerobić, jak ma to działać, to edycja źródeł, więc to lepiej zrobić już w następnym wydaniu. Teraz tego nie robić.

**Janusz Bossak**: Na moim tutaj pulpicie jest dużo zadań na radę wrzuconych. Wiem, że Łukasz to sobie sortuje według sprintów, a ja mam po prostu wszystkie oznaczone "rada". A Łukasz pisze "zaraz dołączymy", dobrze.

**Kamil Dubaniowski**: Może ja, bo ja tego nie wrzucałem na konkretne rady, bo to tak jak mówię, wyszło teraz na bieżąco. Już się loguję do Przemka na środowisko lokalne, pokażę o co chodzi.
Chodzi o odtworzenie... Właśnie to jest pytanie, czy odtworzenie logiki z polami pustymi jak było, czy już podejście do tej nowej propozycji, o której dyskutujemy, czyli żeby przesunięcia działały w ramach wiersza, a nie całego formularza, jak teraz.
Już mówię o co dokładnie chodzi, udostępnię pulpit. Przypadek jaki mamy teraz - Mateusz Kołakowski zgłosił to chyba w piątek - że nie może teraz kliknąć na to tutaj. To jest tak naprawdę po stronie **Backendu** pole puste, żeby sterować uprawnieniami tego pola.

**Janusz Bossak**: Znaczy puste w sensie o typie "puste"?

**Kamil Dubaniowski**: Typ pola "puste", tak. No i oni mają te pola na formularzu u wielu klientów. No bo właśnie tak jak chcą, żeby im w to miejsce nie wskoczyło pole "numer awarii", no to dodawali pole puste. Wiele jest też takich warunkowych użyć tego pola pustego. "Muszę tu dać pole puste, bo jak ukrywam to pole, to to mi wskakuje tutaj. Tak więc muszę mieć jeszcze jedno zapasowe pole puste, które będzie widoczne tylko na etapie, gdzie ukrywam pole osoba rejestrująca". No pełno takich zależności. No wiemy, że tak robimy i tak robiliśmy.

**Damian Kamiński**: Znaczy, ja bym jeszcze tutaj inaczej do tego podszedł, bo o tym rozmawialiśmy. Rzucę trochę inne światło, zdecydujmy co jest najlepszym wykorzystaniem. Bo jeszcze był pomysł grupy. Grupy pól, czyli zakładamy, że wyświetli się jedno... to znaczy grupa pól bym określił jako alternatywa z dodatkiem pustego na przykład. Ale ten pusty to zawsze można uznać po prostu jako "Ukryj oba", czyli wyświetlamy albo jedno albo drugie, albo ukrywamy obydwa. Tak? No to wtedy to działa tak jak jakieś zwykłe pole, więc może ta z dodatkiem pustego to już zbędnie dodałem. Natomiast osadzamy konkretnie pole w danym miejscu i można wyświetlić tylko jedno.

**Janusz Bossak**: Słuchajcie, no sprowadźmy się na ziemię, że tak powiem. Oczywiście pomysłów na rozwój i inne sposoby ogarniania pól pustych jest kilka. Tak też mówiliśmy o tym już dawno, żeby te pole puste... żeby to Piotra była propozycja, żeby można było je używać jako tak zwane aliasy, czyli żeby takie mini pole, taki tekst... znaczy, że w tym jednym polu mógłbym wstawiać jakąś wartość.
Więc... Ponieważ mamy taki moment jaki mamy, znaczy chcemy to wydać, żeby to działało. Ponieważ mamy taką logikę jaką mamy, czyli mamy te pola puste... W moim przekonaniu na ten moment w tym **MVP** powinniśmy dorobić na liście pól po lewej stronie "pole puste". Tutaj wyświetlać to pole puste, czy tam gdzie jest w tej chwili "upuść pole tutaj", powinno być napisane, że to jest pole typu "pole puste". Żeby było widać, że on tu jest i musi działać tak jak inne pola, tak? Znaczy można je usunąć, można je przesunąć. Coś można z tym zrobić. No bo takie mamy formularze. No teraz wiecie, ja nie chcę w 100 kilkudziesięciu wdrożeniach popsuć tego, nie?

**Damian Kamiński**: No tak, tylko pytanie czy powinniśmy iść w tą stronę, czy pozostawić tak jak jest z wiedzą, że...

**Kamil Dubaniowski**: Czy możemy w ogóle tak? Bo ja wam jeszcze powiem co przed chwilką Przemek mi... Po pierwsze **Backend** aktualnie nam w ogóle nie zwraca tych pustych, więc tutaj **Endpoint** do poprawki potencjalnie.
Druga rzecz jest taka, że w momencie, kiedy ktoś sobie... OK. Wiem, że muszę tutaj mieć tyle, bo tyle pól planuję, już sobie nadodawałem. W momencie kiedy zmienimy to, żeby **Backend** nam zwracał faktycznie istniejące już pola puste - no bo to jest tylko teraz na frontendzie - to te pola jeszcze, jak ja rozumiem, nie istnieją. Jak w momencie teraz ktoś doda sobie tutaj to pole, ale już zaplanował sobie te niżej - bo wie, że będzie miał mnóstwo pól do dodania - to w tym momencie te wszystkie musiał usunąć, bo ich nie ma, nawet pojęcia.
Więc jak zaczniemy teraz bazować na tym, co faktycznie zwraca **Backend**... No to efekt będzie taki, że po dodaniu pola te wszystkie moje zaplanowane zostaną usunięte. Ja bym się zastanowił, że jeśli w ogóle mamy teraz taką rozterkę, no to trudno, w ten sposób pracujecie z tym nadal... postaramy tutaj sobie "edytuj się te pola puste"...

**Janusz Bossak**: Będą tam właśnie kombinować z tym przechodzeniem. Znaczy ta wersja, która była robiona jeszcze przez Przemka Madeja, ona jakby te pola puste dopiero dodawała... Jakby później, tak? W momencie, kiedy... Tu jest troszeczkę inaczej. Tutaj to właśnie nie ma żadnego guzika "Zapisz" ani "wyjdź stąd" i tak dalej, tylko wszystko się dzieje na bieżąco. To jest delikatna różnica, bo w tamtym trzeba było wyjść, żeby on jakby zapisał i wtedy dopiero się działo to, co powiedziałeś Kamil - że te wszystkie puste miejsca były wypełniane polami pustymi, jeżeli była taka potrzeba. Więc tam była cała taka logika jakaś za tym stała, taka w miarę sensowna.
Znaczy, wydaje mi się, że najszybciej byłoby po prostu pokazywać te pola puste, gdzie one fizycznie są. Bo one fizycznie obecnie gdzieś są. Tak jak pokazałeś. Jeżeli dodam tutaj jakieś pole, znaczy linię, no to to jeszcze nie są pola puste, bo fizycznie ich tutaj nie ma. Powiedzmy w tym obok osoby, tak? Obok tej osoby rejestrującej. Załóżmy, że byłoby pole puste i to byłoby tu widać. Czyli nie można by było zrobić "upuść pole tutaj", bo tam jest pole puste, o typie puste, a tutaj "upuść pole tutaj" to jest tylko **Placeholder**. I ono nie generuje jeszcze pola pustego.

**Damian Kamiński**: **Placeholdery** są. Ale bo ja się zastanawiam nad pomysłem dodania typu pola pustego po lewej stronie. Czy to jest dobry kierunek? Bo tutaj poniekąd zgadzam się z Kamilem, czy nie zostawić tego tak i zastanowić się nad tym dobrze, zamiast później wycofywać jakieś rzeczy, które wprowadzimy.
Czy nie wiem, nawet jak tak jak teraz prezentujecie, ktoś dołożył sobie wiersze, ale dopiero osadza się to pole puste. Może ono nie jest dostępne na liście, tylko nie wiem, w ramach tego **Placeholdera** jest jakiś znaczek, który powoduje osadzenie tego pola? Czyli jego wytworzenie, a niekoniecznie że mamy ten typ pola na liście po lewej stronie, tylko w ramach tego kafelka jest dostępny.
No nie wiem, tak rzucam pomysłem, nie mówię, że jestem do tego 100% przekonany, ale zastanawiam się, czy pole puste powinno być polem wybieranym z tej lewej listy.

**Janusz Bossak**: Nie możemy teraz wymyślać jakiejś skomplikowanej nowej logiki mając to co mamy. Tutaj można co najwyżej na razie z **Backendu** dodać to, czego brakuje, żeby zwracało informację, że to są te pola puste. I skoro można było wybrać pole puste, to powinno się dać wybrać według mnie pole puste. I to jest najprostsze, według mnie najbardziej intuicyjne, najbardziej dla konsultantów podobne do tego co mamy teraz. Czyli jawnie umieszczone na formularzu pola puste i to byłaby wersja, ta nasza tutaj **MVP**, któraś tam. I tyle. Potem możemy się zastanawiać jak od tego odejść w ogóle.
I to co mówił tutaj Kamil na początku, od tego zaczął - pomysły już były dawno, żeby traktować nasz formularz jako wiersze formularza. I żeby rzeczywiście nie było tak, że jak coś tam usuwam, to mi się wciąga to co jest. O tutaj, tak jak jest dwukolorowo...

**Kamil Dubaniowski**: To chodzi o ten moment, tak? Czyli w momencie, kiedy mam... Spyta to jeszcze tu dorzucę, tu niech będzie jakaś lista...

**Janusz Bossak**: Weź jakiś prosty przykład.

**Kamil Dubaniowski**: Znaczy to tak. I teraz na jakimś etapie tą datę muszę ukryć. A to jest powiedzmy, nie wiem, miejsce, data od, data do, a tutaj już jest jakaś tam nie wiem, lista wyboru, która zupełnie nie pasuje mi do tego wiersza. Ten wiersz ma jak najbardziej tematycznie ze sobą powiązanie. Dlatego tak użyłem w ogóle formularz.
I teraz tak - ja na jakimś etapie ukryję tą "datę 1" tu, to mi wskakuje tu, no a to przeskakuje mi wiersz wyżej. No i oni teraz, żeby to zabezpieczyć, to tutaj dodają jakieś pole puste, które w ogóle teraz tak robi... No taki będzie efekt, że to jest jakieś pole puste, które jest potrzebne tylko po to, żeby na jakimś etapie ono zajęło miejsce tego pola "kwota 1", bo "kwota 1" pójdzie tu. Więc fizycznie tak mają. Teraz tak wygląda ich formularz, bo na jakimś jednym etapie muszą sobie zagwarantować, że pole puste wskoczy w to miejsce, a nie to pole wskoczy w to miejsce.

**Damian Kamiński**: No dobra, jak mamy teraz na liście pole puste, to po prostu my tego nie jesteśmy w stanie tu wyświetlić, tak?

**Kamil Dubaniowski**: Znaczy no po pierwsze, żeby to... No bo to jest puste, tak? To jest puste z jakiegoś powodu, że ktoś jeszcze tu czegoś nie wrzucił, więc my nie wiemy czy on potrzebuje, czy po prostu sobie zaraz coś dorzuci.

**Damian Kamiński**: No nie, ale chodzi mi o to, że jeśli na liście byś dodał pole "pusty", to one się tu jawnie nie wyświetla na tym ekranie.

**Janusz Bossak**: Ale słuchajcie, nie nie, poczekajcie. Dodaj ten wiersz jeszcze raz. Jak zrobiłeś i dodaj w to drugie pole coś tam. Dobra, czyli mamy data 1, kwota 1, niby puste i kwota 2. I teraz wejdź na listę tam.

**Kamil Dubaniowski**: O, kwota 1 będzie pusta.

**Damian Kamiński**: I ono zniknie jak tam...

**Kamil Dubaniowski**: Coś dorzucę.

**Janusz Bossak**: A czy ono się tutaj fizycznie dodaje?

**Kamil Dubaniowski**: Tak.

**Damian Kamiński**: Ja bym nie upychał na siłę w to **MVP** obsługi.

**Janusz Bossak**: Nie no, to czekajcie, to jest dobrze. No jeżeli taki jest jak pokazujesz... I teraz w to pole przed kwotą 2, wrzuć tam nie wiem, listę wyboru albo cokolwiek tam, jakkolwiek datę tam, nieważne. I teraz przejdź na tą listę.

**Kamil Dubaniowski**: No to kwota 1 zniknie z "kwota 1", dokument 1...

**Janusz Bossak**: Co jest git, no.

**Damian Kamiński**: Czy go się coś psuje? Kolumny tak się psują jeszcze.

**Janusz Bossak**: To nic nie pamięta.

**Kamil Dubaniowski**: Kolumny się tak, nie zapamiętuje kolumn układu.

**Janusz Bossak**: To trzeba poprawić tak, ale to wtedy mi się wydaje, że to nie ma problemu z tym.

**Kamil Dubaniowski**: Zgłoszę.

**Damian Kamiński**: Znaczy, patrzymy na to przez pryzmat... Ja też uważam, że powinniśmy zrobić jak najmniej w tej, bo mówimy jeszcze cały czas o czerwcowej, tak?

**Janusz Bossak**: No tak, także nic dużo nie znaczy. Według mnie ta logika - oprócz tutaj tego, że znika 3 kolumny, pojawiają się 2 w trybie przejścia między listą edytorem - to ta logika jest dobrze zrobiona. Znaczy, że tam się pojawiają puste, kiedy tutaj udajemy, że są puste. Ale o tyle jest to nawet bardziej wygodne, że ja nie mam tego jakby z materiału, że tu jest puste i mogę tu włożyć co mi się podoba i to puste samo znika. Nie? Więc to jest bardzo dobra logika. Według mnie w tej chwili zrobiona bardzo dobrze.

**Kamil Dubaniowski**: No tak, tylko teraz jakby ktoś chciał właśnie to co powiedziałem, że na to puste ma żyć tylko na etapie na przykład "nowe". Bo na etapie "nowe" będę ukrywał to "data 1" i ja to pole puste w ogóle tutaj robię, żeby to pole puste właśnie wskoczyło mi wiersz wyżej. No to nie mam jak teraz kliknąć, żeby ukryć to pole na pozostałych etapach, żeby ono było tylko na etapie "nowe" dostępne.

**Damian Kamiński**: Z reguł tylko tak, albo z listy.

**Janusz Bossak**: Bo ono się nie nazywa "puste 1"? Znaczy no ja rozumiem, że chodzi na tym widoku, nie wierzysz, że ono się nazywa "puste 1".

**Kamil Dubaniowski**: Tutaj tak. Że raz, że nie wiem, że on się tak nazywa. A dwa, że nie mogę tak jak na pole "kwota 2" kliknąć i zarządzać uprawnieniami i ukryć to pole puste, no bo na żadnym etapie nie jest mi potrzebne, tylko na etapie "nowe". Nie mogę tego zrobić, no bo jakby tu jest tylko **Placeholder**. A to jest właśnie zgłoszenie Mateusza - nie brakuje ustawień uprawnień do tych pól pustych, do tych **Placeholderów**.
No i tak jak wspomniałem, tak tłumnie nie zwracane jest na **Backend**. My nie wiemy, że to jest "pole puste 1". Znaczy nie jest, zresztą z **Backendu** możemy to dodać, tylko że wtedy to będzie już "puste 1". No i co to "puste 1" po stronie... znaczy puste pole tak po stronie frontendu miałoby mieć taką właściwość, że mimo tego, że widzę, że tu jest "puste 1", to i tak mogę na niej coś upuścić? Ale jak nic nie jest upuszczone, to mogę wejść i potencjalnie edytować uprawnienie.

**Janusz Bossak**: Za skomplikowane.

**Damian Kamiński**: Znaczy ja w ramach **MVP** zastanawiałbym się tylko nad serwisem tego co jest, żeby jak ktoś wejdzie w ten tryb, nie popsuł układu. A nad tym tematem popracowałbym w kontekście design nowych spotkań - jak to obsłużyć? Bo to jest skomplikowane.

**Janusz Bossak**: Ja bym zostawił tak jak jest. W tej chwili, ponieważ to jest trudny przypadek.

**Damian Kamiński**: To nie jest temat na 3 dni, że my już wiemy, jak i ktoś to zaraz zrobi.

**Kamil Dubaniowski**: Tak tak, ja nawet tego nie planuję. Ja nawet tego nie planuję do wydania czerwcowego, to od razu mówię, że jakby listę mają i niech tam się bawią po staremu.

**Damian Kamiński**: Dokładnie.

**Janusz Bossak**: Także jest lista tygodni. Na razie to jest zaawansowane wymaganie i tutaj, a my będziemy dążyli do tego, żeby uporządkować sposób zachowania się pól na formularzu. Ale to naprawdę trzeba zrobić ostrożnie, żeby wiecie, nie popsuć setek [formularzy].

**Kamil Dubaniowski**: Znaczy, moim zdaniem nie wyjdziemy z tego. To będzie musiało być na takiej zasadzie, że mamy 2 logiki zakładu tego formularza. Jest stara, która działa po prostu i ewentualnie jakiś przełącznik, że ktoś świadomie przełącza na nową logikę i sobie podporządkuje, to pozmienia w kodzie, pousuwa niepotrzebne pola puste - które zrobił, bo tak działa stara logika. A po prostu nowe procesy tworzą się już domyślnie z nową logiką. I tak jak mówię, no ta stara logika powoduje takie rzeczy, że później nie masz realnie tak jak wygląda ten formularz. Bo formularz realnie wyglądać powinien... tak.

**Janusz Bossak**: To do tej nowej logiki musi dojść nowe pojęcie, na przykład "wiersz". Albo "grupa" - to co mówił Damian - czyli że masz te 3 pola w wierszu, je traktujesz jako grupę pól, nie? I ona do niej nie może nic doskoczyć z niższego wiersza, tak? I wtedy mamy...

**Kamil Dubaniowski**: Dokładnie. Albo wręcz właśnie tak, że na poziomie wiersza ja sobie mogę go założyć jakąś kłódkę, tak? Że nie przyjmuj tutaj pól pozostałych wierszy niżej. Tak jak ja wtedy ukryję sobie to "data 1", no to ten wiersz jest zamknięty. Zablokowany, nie? Nic nie przyjmie. No i wtedy to łączymy 2 logiki. Tak naprawdę.

**Janusz Bossak**: Dokładnie. Wiesz, że to jest tak jak mówisz, to jest na parę spotkań, na przedyskutowanie wielu różnych jakby wariantów.

**Damian Kamiński**: Jakieś, nie wiem, które będziemy mogli przetestować?

**Kamil Dubaniowski**: Napiszę na razie do Przemka, że zostawiamy. Mateuszowi też dam znać.

**Janusz Bossak**: Jedynie niech Przemek poprawi ten pamiętanie 3 [kolumn].

**Kamil Dubaniowski**: Tak, tak, widzę, że to w ogóle nie zapamiętuje. Już do niego też.

**Piotr Buczkowski**: Gdzie zgłaszać ewentualne błędy, żeby takie niedogodności, tak jak na przykład to? Z tym podmianą literki są w zeszłym tygodniu zauważyłem.

**Kamil Dubaniowski**: Ja im wysyłam wszystko po prostu. Albo do mnie, albo bezpośrednio już na **Backlog**, to już jak w projekcie.

**Damian Kamiński**: Do Kamila. Znaczy, wiecie... nawet jeśli na **Backlog**, ja widzę, że musimy zastosować pewien rodzaj... pewną rolę eksperta, bo ciężko jest się w tym wszystkim połapać. Ja nie będę miał pojęcia, co już było, co nie. Musi być opiekun dodany do projektu i on wie, czy to jest powtórzenie. Bo tak jak z tymi raportami, tak? Gdzie trafia to do mnie i 3 te same tematy w ciągu 2 tygodni. A to oznacza też, jaki jest priorytet tego zgłoszenia. Wpadają niezależnie i nie da rady, żeby 3 osoby równolegle ogarniały. Że to jest ten samo zgłoszenie, to nawet jak wrzucamy na **Backlog**, powinno być najpierw przypisane do Kamila jako opiekuna zgłoszenia, opiekuna całego tematu, który wie jakie są wytyczne, wie czy to wchodzi w **MVP**, czy to jest świadomy jeszcze błąd... tak jak tutaj powiedzmy mamy... i który to właściwie przypisze. Więc podsumowując: na **Backlog** jak najbardziej może być, natomiast powinien być wskazywany Kamil jako osoba walidująca to.

**Janusz Bossak**: Czy no... Wydaje mi się, że powinniśmy... Ja widzę, że wielu osobom bi też zresztą nie jest jakoś wygodnie robić zgłoszenia na **Backlogu**. W ten sposób działać. Tak? Czyli jeżeli to jest edytor procesów, no bo to jest edytor procesów, element edytora procesów, to po prostu tam zgłaszajmy, nie?

**Damian Kamiński**: To też jest dobre rozwiązanie, bo jak tych tematów jest kilka, to nie każdy zapamięta tak, kto jest czyim opiekunem. A to też z drugiej strony rozszerza, że poza Kamilem jest dedykowany tester. Poza mną, powiedzmy w komunikatorze jest jeszcze Basia. I ta walidacja jest podwójna, tak? I ona może pomagać robić zgłoszenia i walidowane. Czy już takiego czegoś nie było, albo jest w trakcie obsługi. Więc no to jest jakiś pomysł.

**Janusz Bossak**: Tutaj wtedy... Tak jest teraz moduł raportowy, tak? Raporty - stabilizacja. No ja wiem, że tu będzie dużo różnych rzeczy, no ale przynajmniej będzie widać, że coś ktoś zgłosił i ktoś tam będzie to sobie przeglądał. Kto jest opiekunem i będzie z tego robił zgłoszenia? Może ten ktoś będzie to przeglądał, zauważy, że: "a, to już jest to samo, co było tam", nie? No bo to już nie robię drugi raz, bo ten ktoś wie dokładnie jakie są zgłoszenia i powinienem o to jakby dbać. Natomiast...

**Kamil Dubaniowski**: Czy ja mam o tyle obawę, że jak będzie dzień, gdzie ja siedzę cały dzień w sprzedaży, to później robię sobie takich zaległości, że się z tego nie wygrzebię. A zgłoszenia będą tylko wrzucone i deweloperzy nie będą mieli co robić.

**Damian Kamiński**: Ale to ja bym... to znaczy pytanie tylko czy takie, czy to nie jest przestrzeń przede wszystkim, gdzie zgłaszać w kontekście, gdzie zapytać? Czy tego już nie ma, czy to zgłaszać? Bo wiesz, jak na czymś też pracujemy, to w zasadzie wersja sprzed tygodnia to jest już zupełnie inna wersja niż obecna. I ja też dostaję dużo pytań: "no słuchaj, tutaj w raportach coś nie działa", bo te raporty już są produkcyjne. No ale jak widzimy są błędy i one się powielają, wracają te same i tak dalej. I też nie wszyscy... niektórzy po prostu nie wprost pytają czy to trzeba zgłaszać. I może trzeba zrobić do tego przestrzeń?

**Janusz Bossak**: No to do tego co mówisz Kamil - według mnie do tych kanałów, zresztą do projektów, bym chciał, żeby te projekty w końcu ruszyły. To co ja zacząłem tam robić na tym Wiki, bo uważam, że to jest bardzo pomocne.
Powinny być 2 osoby, znaczy właściwie 3, tak? I to nam rozwiązuje temat. Jeden z was - tak, czyli Damian, Kamil, Łukasz - jako Delivery Manager. Jeden deweloper - odpowiednio Piotr, Ania, Adrian, Marek i tak dalej. I jeden test, jedna z testerek po prostu, tak? Albo Basia, Oktawia albo Patrycja. I wtedy te 3 osoby są odpowiedzialne za to, żeby taki kanał też jakby przeglądać. No bo są bezpośrednio odpowiedzialne za dany projekt i oczywiście będą uczestniczyły w kilku projektach, więc odpowiednio trzeba tam będzie analizować kilka.

**Damian Kamiński**: Ale to jednocześnie według mnie nie przerzuca odpowiedzialności zakładania bugów na nas, tylko bardziej daje przestrzeń. Czy to się nadaje na bug, czy to na przykład już jest gdzieś zgłoszony, nad tym pracujemy, albo jest rozwiązane w ogóle w nowszej wersji. Bo dalej według mnie ja bym na takim kanale chciał móc odpowiedzieć: "to jest błąd, którego wcześniej nie było, zgłoś go" i tyle. Żeby nie było tak jak Kamil mówi, że kogoś nie ma i potem tutaj 20 zgłoszeń już trzeba obsłużyć i spada to na jedną osobę.

**Janusz Bossak**: Dlatego jednym z moich tam pomysłów było dodanie tego **Live Work Item Generator**. To jest rzecz, którą wymyślił Microsoft. Nie jest jakiś dodatek logiczny firmy... Który zaczął współpracować z tym ogólnie... blogiem? I tam jest kilka jego jakby zastosowań do naszej od kontekstu. Tak? Potrafi generować, potrafi tam wyszukiwać i tak dalej. Możliwe, bo to ciągle jest nieskonfigurowane, nie wiem o co tam chodzi, z tym coś nie działa, trzeba się temu przyjrzeć. Możliwe, że to by nam pozwoliło właśnie na pani odpowiedzi "czy takie coś już jest?". Tak? Czyli zaczynasz wpisywać jakiegoś buga, a on ci pokaże, że tego typu zgłoszenia już są. Tak? I wtedy można się łatwiej zorientować, że ktoś próbuje zgłosić podobną rzecz, która już była na przykład, nie?
No ale to do sprawdzenia. **Work Item Generator**. No dobra, słuchajcie, jedźmy dalej, bo usprawnianie...

**Piotr Buczkowski**: To jakie jest... Jaka jest konkluzja?

**Janusz Bossak**: Wrzucaj na kanał odpowiedni do projektu. Czyli jeżeli masz do edytora procesu...

**Piotr Buczkowski**: Bo tam będzie w **rzucie**? To dotyczące tej nazwy tak? Edycji nazwy pola, na przykład to było dobrze.

**Janusz Bossak**: Tak, tak, tak, tak, tak, tak.

**Piotr Buczkowski**: No bo teraz mamy zrobię zgłoszenie dotyczące sekcji i uprawnień do sekcji. Mam 2 uwagi. No takie drobiazgi, tak? Że jest to coś, coś jest... no nie zaznacza, nie wiadomo do czego się edytuje czy coś.

**Janusz Bossak**: Dobrze. Dobrze, to tak róbmy na razie, zobaczymy jak to nam będzie jakby szło. No tu mamy kanał **Pentesty**, no to tam do **Pentestów**. Mamy kanał ten Level Sidebar to myślę, że już można może usunąć, no ale niech będzie. Moduł raportowy, nowy X sprawy - bardzo dobrze. Forma też dobrze.
Więc tutaj mamy parę takich kanałów. Już jak będzie brakować to dorobimy, tak? Żeby to miało sens.
Dobra, co my tam mamy dalej?

**Damian Kamiński**: Już patrzę, czy nie wiem czy Łukasz ty wyświetlasz?

**Łukasz Bott**: Jest tak, jeżeli się tam... Coś tu nowego wskoczyło od Marka. To znaczy przypisane jest do Marka, wskoczyło od Daniela i to ja przekierowałem. Chodzi o Marka, prosiłem o evaluating na ile to się da zrobić.
Bo chodziło o to, żeby skrócić - sprowadzając do tutaj najszybciej całą dyskusję i to ten wątek - chodziło o to, żeby skrócić prezentowane nazwy plików tak do właśnie pierwszych kilka literek na początku, kilka na koniec i pośrodku jakieś tam właśnie kropki, gwiazdki czy coś w tym stylu.
Bo czasami się w tytule, w nazwie pliku pojawia się na przykład, nie wiem "Umowa z Łukasz Bott", tak? No i to już tam temat wyszedł chyba, został zgłoszony do naszego Radka Szczerskiego, tak? Do IOD. I to gdzieś tam było zamieszanie u klienta. Na szczęście nie skończyło się to jakimś tam incydentem, ale żeby się potencjalnie zabezpieczyć przed tym, to chyba właśnie Radek zasugerował, żeby właśnie tego typu mechanizm zastosować. Bo nie ma co za bardzo tutaj dyskutować, tylko to zróbmy no i tyle. Ewentualnie Marka może w to wciągnąłem, żeby się dopytać.

**Damian Kamiński**: Ale co tu jest ryzykiem? Że nazwa pliku po prostu przenosi jakieś poufne dane? Tak?

**Łukasz Bott**: Tak, tak, tak, że masz... to znaczy przenosi dane, które można potraktować jako poufne.

**Damian Kamiński**: No ja to... No tak, OK. Zadbajmy o to systemowe. Ja takie tematy powiedzmy w **Adecco** planując zadbałem, że tam jest po prostu imię i pierwsza literka nazwiska. Tak? I to nie jest wtedy...

**Łukasz Bott**: Tak, no no wiesz, ale nie wymusisz na wszystkich, że będą o to dbali. W szczególności jak ktoś tam nie wiem, załączy plik z zewnętrznego źródła. Tak mówię, bo ja rozumiem, że ty mówisz o sytuacji takiej, że tam dokument jakoś tak...

**Damian Kamiński**: No tak, tak, tak, tak. My przygotowujemy dokument.

**Łukasz Bott**: A ty przygotowujesz po stronie **AMODITA**, generujesz tą nazwę pliku, to wtedy masz kontrolę nad tym. Ale jeżeli jest to dowolny dokument, który może być załączony z dowolnego źródła...

**Janusz Bossak**: Ale tam w naszym procesie... Znaczy czasami mnie to zadziwia. No ale tu mówisz o przesyłanych SMS-em, tak? Nie mailem? SMS-em. No dobra, no to SMS-em jakoś może mniej pan...

**Damian Kamiński**: Ale to też właśnie SMS-em, ale co tam przychodzi? Poszukam te nasze **Trust Center**.
Dobra no jest pełna nazwa dokumentu. OK, jest **AMODIT Trust Center**, myślnik, kod SMS. Dalej jest kod kropka nazwa dokumentu i w cudzysłowie jest pełna nazwa dokumentu. Czyli ta nazwa dokumentu miała być ścięta do 8 znaków? Tak?

**Janusz Bossak**: Słuchajcie, mamy w procesie wysyłania tych dokumentów takie pole, gdzie podaje się w cudzysłowie "przyjazną nazwę pliku".

**Damian Kamiński**: Mhm.

**Janusz Bossak**: A przyjazna nazwa pliku jest używana do e-maila. Tak? I niech będzie używana do SMS-a. Koniec, kropka, wszystko. I wtedy jakby nie my odpowiadamy za to. Tak? Tutaj masz "szanowny użytkowniku", wpisz sobie co ci się tam żywnie podoba. Nie pisz tutaj imion i nazwisk. Bo to idzie i może gdzieś wyciec, więc wpisuj tylko to co jest bezpieczne i tyle.

**Łukasz Bott**: Ale to już mówisz... Ty już mówisz o formularzu w **AMODIT**, tak? I funkcjach z **AMODITA** wysyłających. Ale jeżeli ktoś korzysta z **Trust Center** z pominięciem **AMODITA**?

**Janusz Bossak**: Ale ta **Trust Center** przecież wysyła ten komunikat.

**Damian Kamiński**: Nie, nie, Januszowi chodzi o to, że **Endpoint Trust Center** ma takie pole jak "przyjazna nazwa dokumentu", która powinna być używana w mailach i analogicznie w SMS-ach. Czyli nie wysyłamy jawnie nazwy pliku, tylko przyjazną nazwę dokumentu, która jest definiowana.
No to znaczy, to nie jest rozwiązanie systemowe w kontekście myślenia za użytkownika, ale to jest rozwiązanie, z którego można korzystać. No i teraz pytanie, czy my chcemy myśleć za użytkownika? Jednak jeszcze to nadpisać, czy tak jak Janusz proponuje - to konfigurator jest odpowiedzialny za to jakie dane wychodzą do użytkownika.

**Janusz Bossak**: Według mnie tak. Znaczy w kodzie, no nie jesteśmy w stanie myśleć za wszystkich.

**Damian Kamiński**: No bo to znaczy ja tu widzę ewentualnie... ale takie uwagi zwrotne. A wcześniej ładnie, my mieliśmy przygotowane takie **Adecco**, że jest umowa Anna K., a teraz jest umowa i jest jakieś... i jest An kropka K., jest wycięte. Jak my tam żadnych danych poufnych nie wysyłamy?

**Janusz Bossak**: No więc o to mi chodzi, że lepiej jest według mnie dać użytkownikom więcej, czyli mogą nazwać sobie w sposób przyjazny ten dokument tak jak chcą. Nie mając tam nazwy... znaczy imion i nazwisk. I niech z tego korzystają. No faktem jest, że powiedzą: "no ale tutaj nam się nie wiem, podpowiada taka nazwa". Tak? Wiem, wtedy w każdej umowie, w każdym dokumencie będą musieli usuwać sami tak sobie imię, nazwisko, skracać do takiego, które jest właściwe.

**Damian Kamiński**: Że no "przyjazna" po to też i wszystko zabezpieczamy. Przyjazna nazwa nie powinna przenosić danych poufnych. No to osoba konfigurując poza integrację powinna mieć tego świadomość, że to powinna być informacja taka, że jeśli wypłynie nie do tej osoby co trzeba, to nie przeniesie żadnych danych. Ale... Rozumiem oba punkty widzenia.

**Janusz Bossak**: W tej przyjaznej nazwie w tym polu można by - to już teraz fantazjuję, nie? - ale są funkcje i wcale nie związane z AI-em, ale tam przynajmniej po stronie języka Python jest dużo takich bibliotek, które wykrywają dane osobowe. Nie? Czy imię, nazwiska wykrywają i można by tak robić, że jeżeli tam my jako **AMODIT** podpowiadamy użytkownikowi w tym polu - bo tam przepisujemy tak naprawdę tą nazwę pliku dosłownie na początku - i ktoś może sobie tam wpisać co mu się tam żywnie podoba, nie? To moglibyśmy mu sugerować, że w nazwie jest nazwisko, nie? Albo imię. I rozważ usunięcie.

**Damian Kamiński**: Znaczy, ale teraz mówisz o... o tym naszym powiedzmy procesie demo? Nie?

**Janusz Bossak**: Tak, tak, tak, tak, tak.

**Damian Kamiński**: Mhm, bo ktoś może też to wyklikać w ramach innego procesu.

**Łukasz Bott**: Dobra. Ale to słuchajcie, tylko rozumiem Janusz konkluzja jest taka, że nie zajmujemy się tym tematem, czyli nie robimy tego? No ale w takim razie trzeba dać odpowiednie wytyczne. Nie wiem, na Wiki to opisać, że tak jest to zalecenie.

**Damian Kamiński**: Nie, niekoniecznie nie zajmujemy się. Inaczej. Zmieniamy jedną rzecz. Zmieniamy po stronie **Trust Center** to, co jest przekazywane w SMS-ie. Nie przekazujemy nazwy bezwzględnej pliku, tylko przekazujemy nazwę przyjazną, tak jak jest to przekazywane w mailu.

**Janusz Bossak**: Dokładnie o to mi chodziło, tak.

**Damian Kamiński**: Czekaj, zaraz ci pokażę.

**Łukasz Bott**: OK, dobra, bo akurat jestem na bieżąco z tym. Bo czy ktoś się tam robi... Rozumiem, że po prostu jak jest funkcja **Trust Center**, tak? "Send document" czy jak ona się tam nazywa, to tam jest opcja tej przyjaznej nazwy, tak? Podanie. Tak? To o to ci chodzi?

**Damian Kamiński**: Tak. I ona jest użyta w mailu jako "Umowa do podpisania".

**Łukasz Bott**: Tylko w mailu jest używana, a nie jest używana w momencie wysyłania SMS-em. Dobra, no to OK. Dobra to taka konkluzja jest.

**Damian Kamiński**: Nie, według mnie jest. Patrzę teraz na SMS-y, według mnie to tak działa. O ile jest zdefiniowana. Dopytaj Marka, ale według mnie jak widzę SMS-y to to tak działa. Jeśli jest zdefiniowana nazwa przyjazna, to patrzę we SMS-y i tam gdzie zakładam... nie miałem "mamo na przykład kropka pdf", a jak miałem w nazwie maila "Umowa do podpisania", to w SMS-ie mam "Umowa do podpisania" bez rozszerzenia. Więc raczej to tak jest.

**Łukasz Bott**: No i dobra, no to dobra. Czyli innymi słowy ja dopytuję Marka, żeby potwierdził, że w SMS-ie jest używana ta przyjazna nazwa - o ile jest podana, tak? A ogólnie nie wiem, na piątkowym spotkaniu z konsultantami tak możemy zwrócić uwagę, żeby tą funkcję nazw przyjaznych we właściwy sposób używali, tak? W ogóle używali. A dwa - używali właśnie tak, żeby unikać właśnie na przykład podawania jakiś tam danych, które potencjalnie mogą być uznane za poufne. Tak? I tyle tak. No ewentualnie to jako wytyczne też może krótki artykuł na Wiki, czyli jako takiej tam nie wiem... Uwagi do funkcji tej **Trust Center**. Zrobić to można w dokumentacji, dopisać tej funkcji jako taką adnotację, tak? Że zalecenie.

**Damian Kamiński**: Tak, zalecenie, że nie powinno się właśnie tak robić tak, żeby tam umieszczać [dane osobowe].

**Łukasz Bott**: Dobra. To z nowości to ja to ogarnę po tym.
"Nieprawidłowe działanie identyfikacji z sprawie nadrzędnej, sprawa podrzędna is hidden true". Czy tu mamy czas na przedyskutowanie? Nam się już za kilka minut kończy spotkanie.

**Damian Kamiński**: No nie wiem, Piotr musiałby się wypowiedzieć jakie tam są zależności. To jest Huberta z tego co pamiętam zgłoszenie. No jest problem z usunięciem **DeleteCase**, jeśli są sprawy powiązane i to zależy z życiem i to zależy właśnie od rodzaju powiązania. Już tu nie pamiętam, ale tak abstrahując od tego...

**Piotr Buczkowski**: Trzeba stworzyć tą sytuację.

**Damian Kamiński**: No właśnie.

**Piotr Buczkowski**: Za bardzo skaczecie, żebym przeczytał. Podrzędna. No. Obsłużyć tą sytuację, to jak?

**Damian Kamiński**: Na nadrzędne nie da się usunąć nadrzędnej sprawy nigdy.

**Piotr Buczkowski**: No tak, bo ona w podrzędnej jest ID w klasie jest **Connected Cases**, tak. I przez to nie pozwala referencje usunąć. No nikt nie pomyślał z takiej sytuacji, trzeba ją obsłużyć.

**Łukasz Bott**: Pytanie, czy to nie jest właściwa sytuacja? Może powinien być jakiś komunikat, że "no nie możesz użyć tej funkcji, bo masz podpięte...".

**Piotr Buczkowski**: A nie dobra, bo podrzędną oznaczam jako usuniętą. Dobra no... No trzeba obsłużyć ten case. Jeden jest oznaczony "usunięto", tak? Ale też niemożliwe do edycji pewnie przez to tak. Ponieważ tamta sprawa jest... Nie inaczej. Sprawy usunięte nie są pobierane do kolekcji **Connected Cases**, tak? A **For Each** pewnie pokonał **Connected Cases** do odczepiania od połączonych. Rozumiecie tak? I przez to nie jest odczepiane od kasy **Hidden**, od tej, która jest ukryta. I później przy samym **Delete** baza danych zwraca błąd, że "sorry nie możesz, bo tutaj jest referencja".

**Łukasz Bott**: Bo została referencja. Dobra, rozumiem. No dobra, no to pytanie czy to coś, to jest w ogóle do dyskusji na Radzie Architektów? Czy po prostu wiadomo co zrobić i nie wiem, wrzucamy to może już nie na ten sprint, tylko nie wiem, na kolejny?

**Piotr Buczkowski**: Znaczy ja wiem co zrobić. Trzeba to obsłużyć tak, a co zrobić czy co dokładnie zrobić to ja wiem. Mogę opisać tak jest.

**Damian Kamiński**: To przypisz to do Piotra na kolejny sprint. Najwyżej Piotrek to zdejmie z siebie, jak opisze i komuś się to rozpisze.

**Łukasz Bott**: Dokładnie. Umiesz to zrobić, tak? Dyskutować... no dobra.

**Piotr Buczkowski**: Ja tam w **Hotfixa** wpisywałem, ale to chyba bez, bo to jest na split, tak?

**Damian Kamiński**: Tak.

**Piotr Buczkowski**: A da się bez sprintu na...

**Damian Kamiński**: Nie chcesz tego zobaczyć?

**Łukasz Bott**: Jeżeli coś masz, to albo oznacz, albo po prostu powiedz.

**Piotr Buczkowski**: Jako **Backlog** wpisałem. Już nie pamiętam dokładnie, miałem jakieś strony pytanie, już moment.

**Łukasz Bott**: Znaczy słuchajcie, no bo czasowo to formalnie byśmy skończyli, tak? Więc...

**Damian Kamiński**: Znaczy, według mnie powinniśmy mieć bloker na godzinę, bo to już nie pierwszy raz i nie zdążamy przejść przez te tematy. I OK, możemy je przesuwać, ale żebyśmy przynajmniej widzieli, że to spada, a nie tak, że po prostu nie dochodzimy do pewnych elementów.

**Łukasz Bott**: Tak, tak. No pytanie czy...

**Damian Kamiński**: Znaczy, Piotr, jeśli coś tam chcesz zreferować, to mów. Według mnie już zróbmy to do 11:00 i tyle.

**Łukasz Bott**: Tak.

**Piotr Buczkowski**: Nie, wiem że wpisałem, ale nie pamiętam co wpisałem.

**Damian Kamiński**: Nie może znaleźć, tak. Dobrze, a Aniu, czy ty jesteś w stanie nam zreferować ten temat o aktualizacji systemu? Bo tu mówiłaś, że to uzupełniłaś, to może byśmy to jeszcze omówili.

**Anna Skupińska**: Jest - choć mnie... OK, miałam, gadałam do wyłączonego mikrofonu - więc jest baza danych **WAM**? Od której są zawarte dane organizacji. To nie jest ta sama baza danych, gdzie są sprawy i tak dalej. I w niej jest tabela, w której można umieszczać wiadomości. I te wiadomości jakby się pokazują, jeżeli nie ma dostępu do bazy danych, czy jeżeli nie można się w **AMODIT** połączyć z bazą danych, to wtedy sięga do tej drugiej bazy danych, w której są informacje o **Failover**. W organizacjach i umieszcza wiadomość. I stamtąd jeszcze to się pojawia w przypadkach jeszcze logowaniu i przy top menu, czy w tym pasku narzędziowym. Tylko nie jestem pewna ile z tych funkcji zostało zachowane, kiedy zaczęliśmy przechodzić na **Reactowe** te rzeczy.

**Damian Kamiński**: Mhm, dobrze, ale to poczekaj, czyli tak: przy logowaniu i przy i w top menu to mówimy o tym, że to był...

**Anna Skupińska**: Tak, znaczy to będzie ten taki pasek, gdzie są te... tak ten pasek na górze, który się zawsze pojawia, gdzie są "o tutaj z użytkownikiem Łukasz Bott" z logiem. To się powinny pojawiać.

**Damian Kamiński**: Na górze.

**Anna Skupińska**: Więc tak samo miało być.

**Damian Kamiński**: Więc ta baza danych, tylko żeby to ta baza danych... Jest weryfikowana za każdym razem, ale dodatkowo nawet jak nie odpowiada baza **AMODIT**, to ona też jest weryfikowana? Tak?

**Anna Skupińska**: Ja próbuje się połączyć właśnie z tą bazą, gdzie są zapisane informacje organizacji.

**Łukasz Bott**: Ale to dotyczy rozwiązania chmurowego. No bo w instalacji **On-Premise** nie masz bazy danych tej **Org**, tak?

**Anna Skupińska**: No w sumie.

**Damian Kamiński**: Znaczy, słuchajcie, jedno nie wyklucza drugiego. Bo skoro jest taki mechanizm, to można było się zastanowić nad możliwością wypełniania tej zewnętrznej bazy z poziomu pola w **AMODICIE**, żeby tym mógł sterować administrator. Z drugiej strony, wypełniając to globalnie, na przykład taki Łukasz Poskrobko mógłby z poziomu jednej bazy przekazać informację do wszystkich **AMODITÓW**, że **Failover** będzie dzisiaj update.
Pytanie tylko, czy ten pierwszy przypadek użycia powoduje jakieś ryzyka czy niebezpieczeństwa, że ktoś tam coś może podmienić i tak dalej.

**Anna Skupińska**: A czy to się manipuluje... Z tą bazą danych nie było żadnego od tego menu zrobionego. Jeżeli ktoś ma dostęp do buta, można tym manipulować. To i tak ma dostęp do bazy danych, więc jest afera.

**Łukasz Bott**: Ale to czekajcie, czekajcie, bo ja teraz sobie troszkę o innej rzeczy pomyślałem. Skoro mamy ten mechanizm powiadomień w końcu, to może to w jakiś sposób wykorzystać i tutaj dać możliwość "Dodaj powiadomienie systemowe"? I wtedy ono mając ten znacznik, że jest systemowe, to się pojawia na tej belce w **Headerze**? Poziomie i tak na górze. Tyle.

**Anna Skupińska**: Dlaczego... Okazać, że nie było ich za dużo, ale tak - można było też użyć tego systemu, że się pojawiają tam na górze. Tylko oczywiście tabelka została przerobiona, więc nie jest... Jeżeli nie dodali tego, no to nie ma.

**Łukasz Bott**: Nie nie, no to...

**Damian Kamiński**: Wiesz, za dużo nie musi być, bo możemy zrobić ograniczenie jedno i koniec. Jak chcesz inne to odepnij to, albo uzupełnij to o drugą informację. Nie ma tam choinki możliwej do podpięcia.

**Łukasz Bott**: Tak, tak, tak. W danym momencie może być tylko jedno systemowe, tak? I tyle. Więc albo je przeredagujesz, albo usuniesz i wprowadzisz nowe, nie?

**Damian Kamiński**: To znaczy, dobra, to jest element powiedzmy już frontendowy i tego, jak tym można wysterować. Załóżmy, że na razie zróbmy wyświetlanie. Tak? Czyli tak jak rozumiem: mamy bazę danych, która jest dostępna z poziomu chmury i pozostaje tylko, żeby dorobić frontend, który pobierze z tej bazy informacje i wyświetli. I to jest rozwiązanie dla klientów chmurowych.
Później możemy pracować nad sposobami wypełniania tych informacji, natomiast to nie jest rozwiązanie dla klientów **On-Premise'owych**. A jakbyś zjechał do dołu? Potrzeba wynika ze zgłoszenia tutaj **On-Premise'owego**? Ha, Mateusz, tak czy nie?

**Łukasz Bott**: Tak, no Mateusz. Chodziło o pewnie gdzie **Rossmann**, **LPP**, no czyli duzi klienci **On-Premise'owi**. Tak? No to za chwilę też pewnie byś to nawet mógł opchnąć Orlenowi, tak? I też by się pewnie ucieszył, gdyby w beleczce mógł wyświetlić komunikat, nie? Więc myślę, że to...

**Damian Kamiński**: Znaczy to co Ania tutaj...

**Łukasz Bott**: Może powinno być to dwutorowo zrobione? Tak? No chmura to chmura, tak? I tam sobie zarządza Łukasz tym za pomocą tej bazy organizacji, dodatkowej bazy. A w **On-Prem**? No to nie wiem. No taki komunikat, jeżeli nie chcemy robić interfejsu na chwilę obecną, a na szybko, no to może prosty interfejs na zasadzie, że gdzieś w ustawieniach systemowych dorzucić taki atrybut. Tak? Jakie mamy tam sekcje dotyczące **User Interface**, wyglądu, no to tam dorzucić pole, tak? "Komunikat systemowy", tak? Albo mamy takie... nie wiem czy się zachowały w tych nowych ustawieniach, ale mamy te pola do zarządzania komunikatem przy na stronie logowania. Tak? Być footer, być jakiś, czy coś w tym stylu. Tak? Na stronie logowania można wyświetlić komunikat.

**Janusz Bossak**: W ogóle ciekawa...

**Damian Kamiński**: Słuchajcie, ja bym też to wyżej poziomo podniósł. Janusz, co w ogóle o tym sądzisz? Czy my... to jest funkcjonalność, która nie jest na **Roadmapie**, wynika z potrzeb klienta. Czy my nie powinniśmy tego po prostu wycenić i pójść do **LPP** i do **Rossmana** i powiedzieć: "zrobimy wam to po 2000 od głowy"? Jeszcze Orlen można zapytać i wtedy dopiero do tego siądziemy.

**Janusz Bossak**: [Śmiech] Równie tanie... Absolutnie tak, finansowanie jest zawsze miłe, tak? Wiecie, no i może musimy się tego nauczyć, że po prostu różne tego typu rzeczy jakoś tam zdobywać finansowanie. Niekoniecznie jest 20000.

**Damian Kamiński**: Ja powiedziałem 2.

**Janusz Bossak**: Ale ja wiem, wiem, no ale tak, tak.

**Łukasz Bott**: Ale no od 10 klientów Damian.

**Damian Kamiński**: No to tak można, jak najbardziej.

**Janusz Bossak**: Po 4 od 10 i wyjdzie wam coś tam na waciki będzie, nie?
Nie, jak najbardziej. Natomiast mnie ciągle zastanawia jedno - że my to mieliśmy zrobione. No ja nie wiem na czym my dyskutujemy?

**Damian Kamiński**: Znaczy i to mamy Janusz, tylko to co Ania powiedziała - nie wiem, czy tam byłeś skupiony - czyli tak: mamy to tylko dla rozwiązań chmurowych i nie jest to... i zakładam, że **Backend**, to znaczy wiemy gdzie odpytać, mamy przestrzeń do przechowywania tych informacji, natomiast z racji, że zmieniliśmy ramę, to nie jest to obsłużone w nowej ramie. I tylko dla chmurowych, a pytają nas o to **On-Premise'owi** i tego nie mamy.

**Anna Skupińska**: A czy trzeba by zapytać osoby, która to robi... Robimy nowe ramy, czy uwzględniły to? Czy dodałeś, że te wiadomości się wyświetlają?

**Janusz Bossak**: Nie, nie, nie. Się ten pomysł, który...

**Piotr Buczkowski**: Ja właśnie to co ja mówiłem, to też jest właśnie też jedna rzecz, którą pewnie w nowej ramie tej **Reactowej** nie została uwzględniona. Chodzi o wylogowanie automatyczne.

**Łukasz Bott**: No dobry.

**Damian Kamiński**: Że tam się też pojawia taki pasek, tak?

**Piotr Buczkowski**: Po pierwsze sprawdzanie, taki ile zostało do wylogowania. A po drugie, jeżeli mam dla was 2 zakładki, w jednej się wylogowuje, to w starym... w starej wersji w tej drugiej zakładce też po chwili cię wylogowało. A tu w tej zostaje i każda kolejna akcja tylko wypluwa błąd, tak.

**Łukasz Bott**: No to, Piotrek, dobrze, że zwróciłeś na to uwagę, bo to trzeba...

**Damian Kamiński**: Zaraz to sprawdzę na swoim domu.

**Kamil Dubaniowski**: Znaczy odliczanie na pewno robiliśmy.

**Piotr Buczkowski**: Zgłoszenie tak, zgłoszenie 21974.

**Damian Kamiński**: Piszesz Łukasz?

**Łukasz Bott**: 21974.

**Piotr Buczkowski**: 2 1 9 7 4. Dziewiątka przedostatnio ze mną na siódemkę. Taki jest efekt: 2 zakładki, w jednej się wylogowuje, w drugiej powinno się też wylogować. Tam jest stary...

**Damian Kamiński**: Czyli tam wylogował, a rama została, tak?

**Piotr Buczkowski**: No bo... bo frame działa ten, to i **Token** i to ta w **Reactcie**, nie? Cały czas mu spamuje tym.

**Damian Kamiński**: Dobra no, przyjmijcie to według mnie. Nie wiem, Kamil to zaopiekujesz?

**Kamil Dubaniowski**: No do Przemka te emocje jakby nawet przeze mnie żeby wychodziło, ale wydaje mi się, że to jest coś, co było.

**Piotr Buczkowski**: Oj to już właśnie tam jest ten licznik, ale tego szczerze mówiąc nie sprawdziłem właśnie czy to działa czy nie.

**Kamil Dubaniowski**: Licznik na pewno uwzględniłem, Przemek robił, a testy też tego były. To było nawet zgłoszenie osobne na ten licznik. A jak się coś wysypało to po drodze.

**Damian Kamiński**: Ale poczekajcie, bo tak kolejny sprint... Ja nie wiem jak jest Przemek obłożony, na ile to jest krytyczne pod kątem wydania tego na...

**Kamil Dubaniowski**: Czy efekt jest taki, że no wylogowany zostałeś, tylko widzisz ramę. Jak klikniesz cokolwiek, no to cię wywali.

**Damian Kamiński**: Na chmurę. Wywali gdzie? Do logowania?

**Kamil Dubaniowski**: Tak to działało chyba do tej pory.

**Piotr Buczkowski**: Znaczy jak się zalogujesz w tej **On-Premie** to będziesz 2 razy widział ramy.

**Damian Kamiński**: OK. No nie nazwałbym tego wersją stabilną, jeśli takie coś się dzieje, a autowylogowanie jest czymś, z czym ludzie mają do czynienia codziennie.

**Łukasz Bott**: Słuchajcie, z tym autowylogowaniem to od razu to podpada pod bezpiekę, bo w **Pentestach** nam wytknęli któryś, że nie mamy tego dobrze obsłużone.

**Damian Kamiński**: Tak, tak.

**Janusz Bossak**: No to jako **Hotfix** to traktować i zrobić natychmiast.

**Łukasz Bott**: Tak, na ten sprint jeszcze i oznaczenie jako **Hotfix**.

**Janusz Bossak**: No tak, ale chcemy to wydawać. Nie możemy wydawać rzeczy, które mają potencjalne dziury bezpieczeństwa. Tak do Przemka, to czy ktoś inny się tym [zajmie]?

**Łukasz Bott**: No dobra. A co wracając do tego tematu, co to co z tym robimy?

**Damian Kamiński**: Znaczy, tak jak wspomniałem, mamy to obsłużone tylko dla chmur i to powinniśmy też wykorzystać dla siebie. Ale dla klientów trzeba to wycenić i tyle, więc trzeba to podzielić na 2.

**Janusz Bossak**: Aby ocenić... Ale też ja bym wrócił do tego pomysłu, który tutaj Łukasz chyba ty podałeś, żeby tak w tych powiadomieniach naszych w jakiś sposób wyróżniać takie powiadomienia systemowe? Albo w jakimś innym mechanizmie - to co dla **Frame'u** tam kombinujemy jakieś **Announce'y** czy cokolwiek innego - żeby to właśnie się wtedy pojawiało jako taki komunikat systemowy, tak? Właśnie wyróżniony.
To jest... bo chodzi też o łatwość dodawania tego. Znaczy łatwość: no tak, żeby administrator chciał **Web.Configa** zmieniać, gdzieś tam coś wpisywać, tak i tak dalej. Tylko żeby to było tak wiecie, no wchodzę i mi się taki komunikat wyświetla, tak? To nie musi być nawet ten pasek od góry, to może być po prostu denerwujące okno po każdym zalogowaniu. Tak wchodzę i...

**Łukasz Bott**: No to po wchodzisz pierwszy raz, ten popup ci się wyświetla, tak i... No tak, no ja ostatnimi czasy mam konto w mBanku, tak? No to jak mają jakoś tam ofertę handlową, żeby wziąć sobie założyć lokatę albo kredyt, jakieś coś, to loguję się i mi od razu wyskakuje popup, który oczywiście zamykam. Tak, no on...

**Janusz Bossak**: No ale też prawdą jest, że w mBanku - też mam konto - jest tak, że jeżeli są tam jakieś informacje o wyłudzeniach i tak dalej, to u góry jest taki czerwony pasek.

**Łukasz Bott**: Krytyczny, tak.

**Janusz Bossak**: Dokładnie. Tak, jak on jeszcze jest, ginie czasami zanim się zalogujesz, nie? Więc taki pasek jest jak najbardziej pożądany.
Znaczy, zróbmy tak: wycenimy to, jakoś tam uzyskamy na to pieniądze, a wymyślimy jak to powinno być zrobione do końca. Bo widać, że jest kilka jakby propozycji, tak? Ale też nie chciałbym tego robić jakiejś wielkiej funkcjonalności, a raczej coś w miarę szybko do tego, żeby to działało.

**Łukasz Bott**: Dobra, Damian ja to z ciebie zdejmuję, do siebie przypiszę. A dzięki za to, dzięki może i ty się tam do kolegów odezwij, czyli do Mateusza i niech finansowanie na to w sądzie? [znajdzie]
Dobra, słuchajcie jedenasta się zbliża, który już nic nie przedyskutujemy takiego.

**Janusz Bossak**: Dobra, ja muszę uciekać na spotkanie menedżerskie.

**Damian Kamiński**: Jeszcze jest tylko tak nadmienię jeden temat tam wrzucony. Klient się zdecydował po 2 miesiącach od oferty na analizę bazy danych. To tak na razie wrzucam, bo powiedzieć tam się zadeklarowałem, że damy jakąś odpowiedź, może dzisiaj. Natomiast, no po prostu klient chce wykupić 2 dni, żeby przeanalizować, dlaczego wolno działa, czyli jakieś tam reguły się wykonują po półtorej minuty i właśnie baza danych jest mocno obciążona. Więc tutaj nie wiem, kto mógłby się tym zająć. Znaczy wiem, kto wiedział jak się tym zająć, ale pytanie czy tutaj właśnie Piotra wrzucamy od razu, czy jeszcze mam jakiś krok pośredni?

**Janusz Bossak**: Wrzućmy Piotra.

**Łukasz Bott**: Ale ja bym wiesz co... Ale ja bym miał pomysł taki, żeby ewentualnie może któryś z koleżanek i kolegów od nas z zespołu zrobił to razem z Piotrem? Żeby ewentualnie nabrał też takiej wiedzy i był powiedzmy no... zastępcą, tak? Potencjalnym.

**Damian Kamiński**: Nie no tak, żeby patrzeć jak to analizować. No jestem za, pytanie tylko kto?

**Anna Skupińska**: Miał mniej zadań, to może...

**Łukasz Bott**: Nie no, to musi być osoba, która tam potencjalnie tak... No ja pomyślałem o moim imienniku, tak? Czyli Łukaszu Grodzkim.

**Piotr Buczkowski**: No czy tylko pytanie to ma być analiza czy poprawianie też tak tego?

**Damian Kamiński**: Analiza. Na razie jest 2 dni Time & Material na analizę i potem wnioski i wycena, poprawę ewentualnie. Na razie to jest analiza.

**Łukasz Bott**: A słuchaj, a monitor wydajności to tam nie było uruchomione?

**Damian Kamiński**: Nie wiem, więc nie... To trzeba zbadać konkretny przypadek z Łukaszem, ewentualnie porozmawiać.

**Łukasz Bott**: Czyli się Poskrobko, tak?

**Damian Kamiński**: Boże, przepraszam, nie, nie, nie Poskrobko. To jest **On-Premisowe**, z Danielem. On zna bardziej temat, no bo tak jak mówię, wczoraj dostaliśmy potwierdzenie, że klient się zgadza, a ja zaproponowałem rozwiązanie "2 dni na analizę" w lipcu. Więc no już szczerze mówiąc nie pamiętam. Daniel jest z nimi na bieżąco, więc tutaj też nie chcę robić za głuchy telefon, tylko trzeba się do Daniela odezwać, ustalić co wiemy i zrobić analizę problemu. Na razie nic jeszcze nie mówić. Nie mówimy o poprawkach.

**Łukasz Bott**: Dobra, no znaczy, czyli tu jest na 2 płaszczyznach, nie? To może być poprawka systemowa, a może być poprawka procesowa? Tak? Więc tutaj, no nie wiemy na ten moment, właśnie po to jest ta analiza.

**Damian Kamiński**: No to jest opiekun klienta i niech się można go zaangażować. Dobra, wrzucę tam Piotra, w sensie wywołam. Poproszę, żeby Daniel się do ciebie odezwał i żebyście ustalili jakiś termin. Klient czekał 2 miesiące, więc według mnie to nie jest coś, co musimy jutro rozpocząć, ale po prostu musimy jakkolwiek zdeklarować termin, kiedy taką analizę poczynimy i tyle.

**Łukasz Bott**: Dokładnie.

**Damian Kamiński**: Dobra, to tyle dzięki.

**Łukasz Bott**: Dzięki, dobry.

**Damian Kamiński**: Cześć.

**Łukasz Bott**: Cześć.

**Anna Skupińska**: Cześć.

**Janusz Bossak**: [zatrzymano transkrypcję]

**Data spotkania:** 3 grudnia 2025, 10:16 - część 3

---

**Damian Kaminski:** To nie jest właśnie. Może trzeba spojrzeć na to z drugiej perspektywy. AssignProcedure powinien być rozbudowany o mapowanie pól. Wtedy zachowujemy kontekst historii sprawy i tyle.

**Janusz Bossak:** Znaczy wiecie, w Rossmanie może to będzie wystarczające, to trzeba przemyśleć. Natomiast tak jak patrzymy na to, możemy mieć dwa rodzaje historii biznesowej. To nie rozwiązuje sprawy Rossmana. Historię biznesową tej sprawy, to jest przypadek MSIT, gdzie chodziło tylko i wyłącznie o to, aby uchwycić kluczowe biznesowe momenty tego procesu i nie wchodzić w szczegóły historii takiej technicznej. Gdzie ta sprawa mogła na przykład 15 razy krążyć do cofnięcia do poprawy, jeszcze raz cofnięto, jeszcze raz poprawiano i tak dalej i tak dalej. Ale w którymś momencie po piętnastym takim cyklu zdecydowano, że te warunki nie są akceptowane. I to jest moment historyczny. To jest moment właśnie, który trafia do tej historii biznesowej. To, że to 15 razy tam krążyło, jakby z punktu widzenia historii biznesowej tej sprawy nie ma znaczenia. Ważne jest, że któregoś tam dnia jakiś dyrektor ostatecznie to zatwierdził. I to samo dotyczy jakiejś umowy. Umowa mogła być 15 razy konsultowana z kontrahentem, ale ostatecznie została jakby zatwierdzona jej treść w dniu takim. I to jest zdarzenie biznesowe. I w takim kontekście wykorzystanie tego mechanizmu, który mamy i tej propozycji, którą dałeś w prawym panelu, jest OK. Bo to jest historia biznesowa tej sprawy. Tak rozumiana. Natomiast jeżeli chcemy wejść na taki poziom właśnie tej klasyfikacji JRWA, tych teczek spraw.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** No to tu dostajemy drugi kontekst. Czyli coś, co wiąże historię z wielu procesów, ale dotyczy tego samego. I według mnie tego nam w tej historii biznesowej brakuje. Znaczy brakuje nam tego jednego pola w tej tabeli, które dawałoby nam ten kontekst. Że to może być tak jak mówiłem ID klienta, ale to może być ID teczki sprawy, takiej JRWA czy cokolwiek.

**Damian Kaminski:** To znaczy, jeśli to skatalogujemy według mnie ten typ po naszej stronie, czyli on będzie wymieniony w regule, że można użyć user ID albo jeszcze coś innego, to wtedy możemy to odpowiednio wyświetlać, po tym filtrować, sortować, obsługiwać to analitycznie. I tutaj też pokazywać to w formie, czyli to jest powiązane ze sprawą główną tą. Co więcej, możemy to na dwóch sprawach wyświetlać, czyli na tej pojedynczej jako historię biznesową, ale też na głównej, z którą jest to powiązane, jako historia biznesowa spraw całego wątku. Tak może to nazwijmy. Tylko to wymaga wtedy po stronie backendu.

**Janusz Bossak:** Tak.

**Damian Kaminski:** No właśnie tego katalogu, uzupełnienia tego jak dodajemy do CaseEvent, jakie są dostępne katalog pozycje w typie. Może rozbudowania o to, bo to jest zapisywane w JSON, że można zdefiniować różne typy, czyli jest ID jeden, ID dwa, ID trzy. Nie wiem jak to obsłużyć. To jest po prostu rzucam pomysł. A może powinno być tyle, ile jest typów i będziemy to rozwijać. Czyli na ten moment definiujemy, że jest user. Super, jeśli jest taka potrzeba, bo coś, bo zakładam też przypadek, że coś może być obsługiwane w godzinach nieroboczych, a powinno być powiązane z użytkownikiem jakimś. Czyli robi to system, powinniśmy to przypisać do jakiegoś opiekuna klienta albo coś w tym stylu. To nie wiem czy.

**Janusz Bossak:** Teraz tak sobie myślę, że może być też tak, że można robić dwa wpisy do historii, do różnych historii. Bo możemy.

**Damian Kaminski:** Tak, tak, chociaż. Dobr, ale powiedz.

**Janusz Bossak:** Znaczy nie chodziło mi o to, że tak jak to rozmawiamy, że możemy śledzić pod dwoma różnymi kątami jakąś sytuację. Bo to może być, nie wiem, czy nie.

**Damian Kaminski:** Sprawa główna i sprawa poboczna, tak podrzędna?

**Janusz Bossak:** No jakoś, bo patrzymy pod kątem klienta na przykład, ale też patrzymy pod kątem polisy. Czyli już tak patrzę od tego Aliansu, jak oni tam wtedy to przedstawiali, że jak wejdę na tą polisę, to chcę widzieć historię biznesową tej polisy. Ale jak wejdę na historię klienta.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To chcę widzieć całą jego historię razem z tymi polisami, bo one są częścią tej historii. Ale jeżeli chociaż na przykład tam na właśnie tą polisę, to widzę tylko polisę. Jak wchodzę na roszczenia, to widzę tylko jakby historię roszczeń, ale nie całej korespondencji. Jak wejdę na historię korespondencji z tym klientem, to chcę widzieć dalej korespondencji, więc ona musi być wielowymiarowa w pewnym sensie.

**Damian Kaminski:** Tak, zgadzam się z tobą, ale to wtedy ja widzę to tak, że to nie może być w JSON. Jako tu tylko to w tabeli musi być jakiś setMainCaseID. Wtedy jak wchodzimy w MainCaseID, to my widzimy całą historię posortowaną, powiedzmy domyślnie chronologicznie. Ale tu mamy możliwość wyboru, że ja chcę teraz przejrzeć w kontekście tej historii głównej tylko zdarzenia na polisach. Czyli wybieram z listy rozwijanej polisy i patrzę, jak podpisano polisę, rozwiązano polisę.

**Janusz Bossak:** Wydaje mi.

**Damian Kaminski:** I jakieś tam istotne zdarzenia. Ale z poziomu polisy nie widzę zdarzeń z MainCase. Widzę tylko.

**Janusz Bossak:** Wydaje mi się.

**Damian Kaminski:** Z tej polisy.

**Janusz Bossak:** Wydaje mi się, że to co mamy, to jest historia biznesowa sprawy i tyle. To jest to, co mamy, historia biznesowa sprawy, ponieważ tej głównej części tej tabeli jest CaseID.

**Damian Kaminski:** Tak.

**Janusz Bossak:** I tyle i koniec, kropka. Czyli tu możemy zapisywać zdarzenia biznesowe dotyczące pojedynczej amoditowej sprawy i do tego to służy. Jeżeli mamy potrzebę takiej procesowej historii, to trzeba to wymyśleć inaczej albo obok drugą historię.

**Damian Kaminski:** Znaczy też się to da, tylko właśnie tak jak tu. Tylko pytanie, czy my tak chcemy, żeby w to właśnie? Bo teoretycznie się da, tylko jak chcemy to zaopiekować, to powinniśmy to zaopiekować zanim ktoś to zacznie w ten sposób używać.

**Janusz Bossak:** Znaczy patrząc na to teraz, rozmawiając i to, co już tu parokrotnie wyartykułowałem, JRWA według mnie to jest świetny case i ten WIM. Bo jeżeli tutaj dodamy.

**Damian Kaminski:** Dla historii sprawy masz na myśli jako teczki?

**Janusz Bossak:** Tak, jako teczki.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Bo tej tabeli, która tam jest na dole wyświetlana oprócz tego CaseID, który dotyczy tej konkretnej sprawy, tej korespondencji, tego dokumentu. Jeżeli tu byłoby pole teczka sprawy, takie coś, i to byłoby tekstowe, to mamy temat załatwiony z punktu widzenia teczek JRWA. Bo po prostu mogę sobie wejść w kontekst teczki i zobaczyć historię tej teczki JRWA.

**Damian Kaminski:** Ale to, ja rozumiem chyba o to ci chodzi biznesowo. Pytanie tylko, czy ty zgadzasz się z tą moją propozycją, czyli po prostu dodanie tu jednej kolumny takiej MainCase, z którym jest to powiązane?

**Janusz Bossak:** Tak, tak, tak, tak. No to jest MainCase, ale nie case rozumiany jako amoditowy, tylko jako.

**Damian Kaminski:** OK, dobra, to teraz się rozumiemy.

**Janusz Bossak:** Coś?

**Damian Kaminski:** Nie jako amoditowy, ja bym to rozumiał.

**Janusz Bossak:** Nie wiem właśnie. No może to być, bo to może być wtedy sprawa rozumiana jako klient. Czyli wszystko się wiąże z klientem albo sprawa właśnie rozumiana jako ta teczka sprawy, która też jest reprezentowana jako sprawa amoditowa, tak wyższego rzędu. Tyle, że i tu wracam do tego wątku wiem jakby wielowymiarowego, że jeżeli damy jedno pole, to mamy przypisanie tylko do klienta. Nie możemy przypisać tego do polisy. A ja bym chciał mieć przypisanie jednoczesne do polisy i do klienta.

**Damian Kaminski:** Nie, to ja to tak widzę w tym pomyśle. Tak to widzę, bo jeśli wchodzisz na polisę, to pytamy gdzie polisa jest ujęta i teraz sprawdzamy dwie rzeczy, CaseID i MainCaseID. Jeśli CaseID, no to wyświetlamy, że tu jest taka historia biznesowa. A jeśli wchodzisz na klienta, to jest dodatkowo nagłówek, że to jest historia biznesowa tamtej sprawy, ale w kontekście tej jako sprawy głównej. Jak agregującej całą historię biznesową, tu jest też wyświetlana, czyli tu musiałoby być jeszcze jakieś rozbudowanie wyświetleń, czyli przeszukujemy jednocześnie i MainCase i CaseID. Jedyny minus tego jest taki, tu się rozumiemy.

**Janusz Bossak:** Mhm.

**Damian Kaminski:** Jedyny minus tego jest taki, że jeśli chcemy doprowadzić do sytuacji gdzie, ale może to jest, gdzie klienci nie są sprawami, czyli opieramy się o źródła zewnętrzne, po to żeby minimalizować CaseDefinition, no to wtedy mamy problem, bo to jest oparte na integer, a nie na, nie możemy tego wyraportować niezależnie. Ale jeśli chcemy mieć tą historię biznesową, to pytanie czy to jednak wtedy te sprawy nie są wskazaniem do tego?

**Janusz Bossak:** Dlatego, dlatego tutaj nawet na tym obrazku centralnym miejscu ekranu. Z obrazek type ID, Jan Kowalski. Tak samo jak na imię Jan Kowalski, sam user ID 1, 2, 4, SubjectID to jest, wydaje mi się to jest to, o czym mówimy. Że właśnie ten typ, wiem że to jest user albo klient, albo sprawa i JRWA, cokolwiek. Bo to określamy jakiego typu jest ten obiekt, właśnie ten temat, subject. I to ID może być czymkolwiek, może być. Jeżeli wiemy jaki jest typ, to wiemy co oznacza to ID. Czyli o to chodziło tutaj. Że jeżeli typ jest user, to znaczy że ten ID to jest user ID. Jeżeli typ jest case, to ten ID to jest CaseID.

**Damian Kaminski:** OK, zgadzam się z tobą, tylko tu mamy ograniczenie, że możemy.

**Janusz Bossak:** Jeżeli typ byłby JRWA, to ten ID byłby tym JRWA. Jeszcze raz.

**Damian Kaminski:** Zakładasz, że można dać wiele, tak? Czyli zakładasz, że może być wiele. Czyli musiałoby być zdjęte ograniczenie, że jednocześnie możemy dać ID do Jana Kowalskiego i do sprawy głównej klienta. Czyli ID musiało być inne user i inne case. Dwa odrębne.

**Lukasz Brocki:** Ale możemy to zrobić.

**Damian Kaminski:** Dzisiaj?

**Lukasz Brocki:** Dzisiaj nie, bo to wymaga zmian.

**Damian Kaminski:** OK, no tak, OK. To że możemy to zrobić, tylko.

**Janusz Bossak:** Przerwa, przerwa, przerwa, stop. Zaczęło się spotkanie dotyczące totalizatora sportowego. Czy ktoś z nas tam powinien być?

**Kamil Dubaniowski:** Zaprosili, ale nie wiem. Tam są te tematy tego Worda, co uzupełnialiśmy między innymi te powiadomienia pushami. Tam ci odpowiedział, że nie mamy już.

**Janusz Bossak:** No to ja mu odpowiedziałem, że w takim razie odpowiedź brzmi nie, nie mamy powiadomień push.

**Kamil Dubaniowski:** Czasem na zebraniu. Dobra, ja się tam przejadę zobaczyć co tam jest.

**Janusz Bossak:** Czy możemy je zrobić, ale z dużymi ograniczeniami? Tak.

**Damian Kaminski:** Dobra, według mnie to jak to zrobić docelowo nie rozstrzygniemy. Musimy ustalić, co robimy, bo to jest gruby temat. To co Janusz tu poruszamy, w sensie jak to zrobić w ten sposób, albo w ten koncepcyjnie. Bo może wykonawczo wcale nie, ale koncepcyjnie to trzeba na to jeszcze poświęcić pewnie kilka godzin.

**Janusz Bossak:** Znaczy.

**Damian Kaminski:** I teraz pytanie, co robimy? Czy idziemy w kontekście Rossmana w tą historię biznesową? Czy ja mam rozkminiać ten AssignProcedure i ewentualnie rozbudowę tej funkcji? No tracimy wtedy sponsora na to.

**Janusz Bossak:** No bo.

**Damian Kaminski:** Ale problem, że tak powiem, udrażniamy szybciej. Czy skupiamy się na tym i mówimy, że jednak potrzebujemy jeszcze więcej czasu i.

**Janusz Bossak:** Znaczy, znaczy sponsor by się przydał. I według mnie trzeba przemycić w tym naszych pracach pewne prace, które chcemy tu dokonać. Bo jaki według mnie jaki jest kontekst tego Rossmana? I tak i tak potrzebujemy kontekstu.

**Damian Kaminski:** Wielu spraw w jednej.

**Janusz Bossak:** Wielu spraw w jednej, tak. Czyli się być kontekst tej, jak to nazwałeś, teczki czy tej sprawy takiej nadrzędnej.

**Damian Kaminski:** Mhm. No tam jest właśnie inaczej, żebyś to też dobrze interpretował. Tam są sprawy równoległe, które potrzebują po prostu historii zdarzenia, które jest wirtualne. Czyli sprawy jako takiej, która jest wirtualna. Tam nie ma tej nadrzędnej fizycznej, tylko jest wiedza w ludziach, że ten dokument biegł przez różne procesy, ale on się w żaden sposób nie agreguje do sprawy nadrzędnej. On po prostu przechodził przez różne procesy, bo był omyłkowo obsługiwany.

**Lukasz Brocki:** I ja może zasugeruję, jakbym to widział od strony technicznej. To może wam naświetli właśnie jakieś rozwiązania ze strony biznesowej.

**Damian Kaminski:** Mhm.

**Lukasz Brocki:** Ja bym widział to tak, że to cały czas w subject. Robimy oddzielną tabelę w bazie danych, powiedzmy CaseEventConnections. I tam każdy wiersz to będzie ID CaseEvent oraz właśnie powiązanie, czyli ID oraz jego typ. I ewentualnie jeszcze jakaś dodatkowa informacja. I dzięki temu mamy powiązania do tylu ilu potrzeba oraz do jakich potrzeba.

**Janusz Bossak:** No tak, bo to.

**Damian Kaminski:** Czyli druga tabela, tak, powiązań. OK.

**Lukasz Brocki:** Tak.

**Damian Kaminski:** Tylko.

**Janusz Bossak:** Tylko pytanie, Damian jest dla ciebie. Jak to user ma?

**Damian Kaminski:** No.

**Janusz Bossak:** Identyfikuje to coś, co nazywasz wirtualną sprawą, czyli że to jest połączone. Skąd oni wiedzą, jak to nazwą, jak to oznaczą?

**Damian Kaminski:** To znaczy to jest po prostu dokument. To jest wirtualna sprawa, on biegnie przez różne procesy w wyniku omyłek.

**Janusz Bossak:** No widzisz, bardzo dobre stwierdzenie. Czyli w SubjectType wpisujemy attachment, a w SubjectID wpisujemy ID tego attachment.

**Damian Kaminski:** Mm.

**Janusz Bossak:** Ale to tak nie do końca, bo ten dokument zostanie skopiowany. To już nie jest tym samym dokumentem.

**Damian Kaminski:** No nie wiem, no właśnie.

**Janusz Bossak:** No właśnie, no właśnie właśnie. Szukam tego, wiesz.

**Damian Kaminski:** Ale rozumiesz kontekst biznesowy, że właśnie tej nie ma tej agregacji, tak jak JRWA. Że to po prostu płynie sobie i aż trafi do właściwej osoby, ale płynie równolegle. Nie ma drzewa.

**Janusz Bossak:** No ale nie musi być drzewo. Znaczy tym tu akurat JRWA nie rozumiemy jako drzewo, tylko jako tylko ten poziom teczki sprawy. Że mam teczkę sprawy, która jest tym elementem spina.

**Damian Kaminski:** Mhm. No ale JRWA jest drzewem w mojej opinii, bo właśnie tak jak mówisz jest spinanie, a tu nie ma spinania.

**Janusz Bossak:** Nie, no samo drzewo JRWA jest tylko i wyłącznie po to, żeby do czegoś to sklasyfikować, żeby było łatwiej. W tym przypadku można by było sobie wymyśleć.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Jak ta sprawa w Rossmanie przychodzi, to ktoś jej nadal jakiś numer, 15, 20, 500. Nie wiem, może jest jakaś numeracja, którą w ramach korespondencji przychodzącej sobie numerują te pisma. I teraz CreateCase, przepisywanie tego do innej sprawy, powinno przenosić ten numer, który był pierwotnie z tym dokumentem związany. I on musi być.

**Damian Kaminski:** No to numer korespondencji przychodzącej po prostu.

**Janusz Bossak:** Może być to numer korespondencji przychodzącej, może to być to pierwotne CaseID, z którego to się wzięło. Ale rozumiane tylko jako ten spójnik.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Że to jest jakby początek wszystkiego. Że to się wzięło z tej korespondencji i ciągle dalej idzie. Ale to jest ten numerek, TeczkaID, teczka sprawy. Obojętnie do którego procesu to pójdzie, ile razy zostanie gdzieś cofnięte, to ciągle już zawsze odniesienie do tego dokumentu będziemy się posługiwali tym pierwotnym CaseID, z którego ten dokument został zarejestrowany. No i wtedy będzie OK.

**Damian Kaminski:** Chyba tak, już teraz sam jestem skołowany, ale to tak to przyjmujemy, że jest jakieś ID. To może być auto increment, NextNumber, to nie ma znaczenia według mnie, bo my to.

**Janusz Bossak:** No tak, ale nawet, znaczy mi chodzi nawet, że nie musi być żaden auto increment, bo to może być CaseID tej sprawy, w której to pismo zostało pierwotnie zarejestrowane.

**Damian Kaminski:** Tak, pobrane, może tak być. No to nie ma znaczenia, bo to jest tylko techniczny numer. Użytkownik go nie widzi.

**Janusz Bossak:** Jakimś, znaczy on się przenosił te sprawy do sprawy. Czy było jakieś pole na formularzu, które reprezentuje ten numerek i żeby ono się przenosiło? Jak tam ktoś zrobi to, żeby się. Nie myślałem to mieć.

**Damian Kaminski:** No właśnie tutaj pytanie, czy jakieś CreateCase? No właśnie, bo może jeszcze do tego powinna istnieć funkcja kopiująca historię biznesową, bo tworzymy nową sprawę, która jest tak jakby kontynuacją tego bytu wirtualnego tego dokumentu.

**Janusz Bossak:** Dla Damian.

**Damian Kaminski:** Dobra, dobra, OK. Przepraszam, już wiem, wiem, wiem, wiem. Jest OK. Tak, tak, tak, tak.

**Janusz Bossak:** Jeszcze raz. Hej, tabeli w tej tabeli tutaj, bo według mnie to myśmy tu Łukasz wtedy chyba kombinowali, to nie niezbyt dobrze.

**Damian Kaminski:** Dobra, słuchajcie, to może inaczej powiem. Podsumowując, ta historia biznesowa powinna mieć jeszcze kontekst nagłówków, które po prostu łączą, bo tutaj mamy tylko zdarzenia. A teraz, żeby mieć te powiązanie, to musimy to jeszcze jakoś wymyślić, że nad tym wszystkim jest jeszcze coś co wiąże, co pokaże, że to był inny proces, że tu się zastanawiam, tylko jak tu się zgadzacie czy nie?

**Janusz Bossak:** No się pogubiłem. Wymyśleniu. Czy wszystko zależy od tego, co chcemy osiągnąć? Jeżeli chcemy mieć ten spójnik?
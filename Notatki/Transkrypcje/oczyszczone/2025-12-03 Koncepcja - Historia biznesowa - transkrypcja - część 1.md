**Data spotkania:** 3 grudnia 2025, 10:16

---

**Janusz Bossak:** Ciągnęliśmy ciebie, Łukasz, bo będziemy rozmawiać o tej historii biznesowej, a tam jest klient, który potencjalnie trzy lata z nami współpracuje. Który potencjalnie chciałby teraz frontend do tej historii biznesowej.

**Lukasz Brocki:** Już wczoraj zagrałem chwilę, rozmawialiśmy o tym.

**Janusz Bossak:** Mhm.

**Damian Kaminski:** Tak, tu jest nawet szerszy kontekst, ale jak za to mogą zapłacić, zaraz będziemy się zastanawiać co dalej. Dobra, już mam i już pokazuję. To jest to. Europo domykam tylko to. To jest błędne. Czy to byłoby wałem ten temat? Dobra, historia biznesowa. Więc tak, skupmy się na tym, co znajduje się tu, bo to jest kwestia tylko i wyłącznie wizualna. To możemy ustalić tutaj z Januszem, z Kamilem, jak te zakładki mają się prezentować i tak dalej. Czyli żeby to dobrze rozkminić, musimy sobie spojrzeć na to, jak ta historia jest w ogóle zdefiniowana. Ona według mnie może wymagać pewnej rewizji u klientów, którzy z niej korzystają. Ich nie jest za dużo na szczęście, ale mam takie przemyślenie, że to może być niekompatybilne wstecz i mogą być wymagane działania serwisowe, ale to jest moje poczucie. Zaraz sobie to ustalimy, że tak faktycznie jest. Dobra, mamy tutaj. Jeśli chodzi o backend, to na stan dzisiejszy mamy CaseID, który jest powodem tego wpisu. Data, typ wpisu rozumiany jako pozycja słownikowa w kontekście globalnym wszystkich słowników, tak Łukasz, czyli?

**Lukasz Brocki:** Tak, zgadza się. To jest bezpośrednio po prostu ID pozycji słownikowej.

**Damian Kaminski:** OK. Tak, ale ze wszystkich słowników, czyli tej ID unikalnej w kontekście systemu, a nie w kontekście danego słownika. Prawda? Czyli można mieć kilka słowników. Dobra, i teraz musimy to przełożyć, powiedziałbym, otwórzmy to sobie na dwóch ekranach.

**Lukasz Brocki:** Tak, zgadza się.

**Janusz Bossak:** I właściwie właściwa wiadomość, która jest w tym ostatnim polu, czyli message, bo tam.

**Damian Kaminski:** Message, zaraz do tego dojdziemy. W message jest w zasadzie wszystko.

**Janusz Bossak:** Dokładnie, tam jest najbardziej wartościowa rzecz.

**Damian Kaminski:** I to jest tak. Tytuł, to bym powiedział, że to jest nazwa CaseEvent, czyli odpowiadamy w cudzysłowie kluczu. Bo wtedy mamy zapewnioną jakąś wielojęzyczność. Nawet jeśli treść, no nie da się jej przetłumaczyć co do zasady, to same tytuły, jeśli chcemy zapewnić im wielojęzyczność, to musimy zastosować odniesienie do pozycji słownikowej.

**Janusz Bossak:** Dobrze było trudno rozpatrywać na jakimś konkretnym przykładzie, bo to jest dość złożony temat, to nie jest takie.

**Damian Kaminski:** Nie, nie. Mhm. Dobra, ale na konkretnym przykładzie, co masz na myśli? Bo tu jest jakiś konkretny przykład na tym mockupie, czyli przebieg korespondencji przychodzącej. Pobranie.

**Janusz Bossak:** Znaczy.

**Damian Kaminski:** Tylko to jest wymyślone przeze mnie, co mogło być w takiej historii biznesowej. Pobranie z e-Doręczeń, przekazanie do właściwego działu, przekierowanie do innego działu, bo to nie jest ten dział co trzeba. Przyjęcie do obsługi, stworzenie odpowiedzi, wysłanie odpowiedzi, czyli to już jest informacja z innego procesu i zamknięcie sprawy.

**Janusz Bossak:** Nawet, po co to robić, skoro to jest tylko jej historii?

**Damian Kaminski:** Nie, to jest przykład. To klient de facto decyduje, co chce tu zrobić. Mógłby nie mieć tego, mógłby mieć to jako kluczową informację, czyli przekazanie do właściwego działu, potem przekierowanie do innego działu. Dobra, kontekst.

**Janusz Bossak:** Znaczy, historia. Poczekaj, historia biznesowa wzięła się z dwóch właściwie powodów i z powodu dwóch przypadków. Przypadek pierwszy, to był MSIT, gdzie Kamil musiał robić raporty i żeby wydobyć te raporty, musiał szukać zdarzeń po kliknięciu w przycisk, na przykład, że tam akceptuje jakiś projekt czy akceptuje wniosek i tak dalej. I to był pierwszy pomysł, że powinno być takie miejsce, które zapisuje historię pewnych kluczowych dla danego procesu zdarzeń, nie wszystkich właśnie, żeby nie przeszukiwać całej historii, tylko tych kluczowych, które są istotne z punktu widzenia na przykład raportowania.

**Damian Kaminski:** Mhm. Mhm.

**Janusz Bossak:** To był pierwszy kontekst. Drugi kontekst, to rozmowy z Aliansem. Kiedy rozmawialiśmy właśnie o tym, to zostało rozbudowane maksymalnie ta koncepcja, gdzie oni chcieli mieć ten widok klient 360, co oznaczało, że totalnie z różnych procesów, z różnych momentów, różnych rzeczy.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Są generowane te wpisy i chodziło o to, żeby mieć pełną informację o tym kliencie konkretnym, co się z nim dzieje. Na przykład, że kupił polisę, że zadzwonił, że miał szkodę, że mu tą szkodę tam nie wiem, odmówiono wypłaty, że on złożył reklamację, że w końcu dostał wypłatę i tak dalej i tak dalej. Żeby to z różnych procesów, różnych polis była jego historia. I taki jest jakby cel tej historii biznesowej. Więc dlatego jest to pole JSON, którym teoretycznie można było wpisywać i można wpisywać cokolwiek zasadzie, bo to zależy od tego, z jakim zdarzeniem mamy do czynienia. Więc ja nie wiem do końca, szczerze mówiąc.

**Damian Kaminski:** Dobra, to teraz przedstawiam sytuację nową.

**Janusz Bossak:** No.

**Damian Kaminski:** Są różne procesy obiegu korespondencji i to powoduje, że nie ma zachowania historii sprawy jako takiej w rozumieniu biznesowym, a nie technicznym.

**Janusz Bossak:** Czy taki trochę sprawy JRWA, tak? Bo to.

**Damian Kaminski:** Nie do końca, ale nie do końca, bo tutaj chodzi o to, że są różne procesy i to już wynika znowu z historii. To nie jest, nie mówię, że jedyne rozwiązanie tego przypadku, ale rozwiązanie, które pozwala nam to sfinansować i na które oni powiedzieli, że byliby ciekawi. Bo na czym im zależy przede wszystkim?

**Janusz Bossak:** Nie, no właśnie.

**Damian Kaminski:** Na tym, że to ma być tu, bo są przyzwyczajeni, że historia jest tu, a nie gdzieś, bo oni zrobili po prostu tam tabelkę, która to pokazuje. Ale im się to nie podoba. I co więcej, właśnie tego typu podejście, to jest pokazywanie też wszystkich przejść, jakie one sprawy mają i tak dalej i tak dalej. To też może być wtedy tu, ale to już jest wtórne, bo często robimy w obiegu, w obiegu.

**Janusz Bossak:** No, znaczy.

**Damian Kaminski:** Faktur, te dodatkowe tabele, które według mnie też są zbędne, zaśmiecają nam case definition zamiast być odłożone właśnie w takiej uproszczonej tabeli.

**Janusz Bossak:** Znaczy. Dlaczego mi się to nie podoba? Znaczy, koncepcja mi się nie podoba.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Albo może nie tyle nie podoba, co mi nie pasuje. Tak, nie chodzi o to, że mi się podoba czy nie, tylko mi nie pasuje. Nie pasuje mi właśnie dlatego, że to jest przedstawiane w sprawie i to, co teraz pokazujesz, właśnie jakby sugeruje mi jako odbiorcy, że to jest historia biznesowa tej sprawy, a to nie o to chodziło.

**Damian Kaminski:** Tej sprawy, ale nie w rozumieniu tego formularza tej sprawy. To znaczy ta sprawa.

**Janusz Bossak:** To jest nie, nie, nie, nie, nie. To jest dokładnie tego formularza tej sprawy amoditowej.

**Damian Kaminski:** Tak bym, ale to jak mówisz klient 360, to to jest obsługa tego klienta, że.

**Janusz Bossak:** Dlatego to nie miało być w prawym panelu. No właśnie, o to chodzi.

**Damian Kaminski:** Taki był projekt, taki był projekt jeszcze Cristiny, to nie ja to wymyśliłem. To jest od Kristin.

**Janusz Bossak:** Jeszcze Krystyna też do końca tego nie rozumiała. To było tak, jasne.

**Damian Kaminski:** OK, ale to jak byś to widział, jeśli nie w prawym panelu, to gdzie?

**Janusz Bossak:** Znaczy, według mnie to powinna być tabelka, czy tabelę na tak? Ja przynajmniej to widziałem w głowie wtedy. Tak jak Alians mówił, oni chcą mieć różne rzeczy i mieć tego klienta 360. I ta historia biznesowa powinna w moim przekonaniu powinna być jakimś typem, nie wiem, właśnie nie chcę używać tych nazw, bo zaraz się wam będzie to kojarzyć, ale takiego raportu osadzonego. Jakiegoś, takiego bytu. Znaczy nie raport, to nie ma być ten raport osadzony, który mamy, tylko wyobrażam to sobie właśnie jako coś, co przedstawiamy na formularzu. Co ma swoje jakieś tam nagłówek i tak dalej, ma swoje wyjaśnienie. Na przykład, to jest historia korespondencji, bo tu jest historia. Ktoś inny będzie chciał użyć tego jako historia podejmowania, promowania, nie wiem, akceptacji faktury. I on tego chce mieć, że dyrektor merytoryczny zatwierdził i że tam dyrektor finansowy zatwierdził, dotarło do księgowości. Tylko te punkty ich interesują.

**Damian Kaminski:** Tak, ale ja się z tobą zgadzam. To, że tu jest taki przykład, to nie odzwierciedlone, to jest jakiś przykład. Natomiast to nie znaczy, że my musimy odzwierciedlić każdy etap. Ale ja byłem na spotkaniu z Rossmanem i dla nich istotne jest to, kiedy to wpłynęło. Dlatego to tak pokazałem. Kiedy ktoś przekazał do tego działu, a okazało się, że to nie ten dział. Kiedy ktoś przekazał do innego. Cała reszta można powiedzieć, że może być już nieistotna, ale to jest istotne, że jak to trafiło do mnie, czyli do innego działu w dniu takim.

**Janusz Bossak:** No tak, tak, tak, tak.

**Damian Kaminski:** A ja widzę na formularzu, na dokumencie, że data jest przed trzema dniami. To dla mnie bardzo istotne jest to, co się wcześniej zadziało. Co usprawnić w procesie, że to draw trafiło do mnie po trzech dniach, a nie po godzinie od wpłynięcia?

**Janusz Bossak:** Tyle, że Rossman to upraszcza.

**Damian Kaminski:** Tylko że wiesz, teraz podam ci inny kontekst, bo ty pogoda jest 360, a teraz jest WIM. W WIMie to jest jeszcze inaczej. Dobra, to jest zły przykład. W WIMie, bo w WIMie mamy historię powiadomień. Dobra, to nie, tam inaczej to zrobiliśmy.

**Janusz Bossak:** Tak, albo.

**Damian Kaminski:** Ee.

**Janusz Bossak:** Znaczy, ta historia właśnie dlatego o tym wspomniałem tutaj, bo chodzi mi o taki kontekst tej sprawy wyższego rzędu. Znaczy, że jest teczka sprawy, która jakby obejmuje wiele różnych aspektów, czyli na przykład masz korespondencję przychodzącą i korespondencję wychodzącą.

**Damian Kaminski:** No i zdarzeniem byłoby wpięcie do akt, tak?

**Janusz Bossak:** To jest realizowane. Tak, i to jest realizowane przez dwa różne procesy, przez proces korespondencji przychodzącej i wychodzącej.

**Damian Kaminski:** No i to i tak, tak.

**Janusz Bossak:** Zupełnie niezależnie. Może być jakiś proces reklamacyjny i ten klient złożył jakąś reklamację procesem reklamacyjnym i tak dalej i tak dalej, czyli może to być rozproszony. Może jakąś umowę mamy.

**Damian Kaminski:** No tak, i te zdarzenia, o których mówisz, czyli tu akurat specjalnie nie wprowadzam, ale one mogły być tożsame. Przekazanie do właściwego działu tu mogłoby być przekazanie do właściwego działu. I dodatku te typy zdarzeń mogłyby być tutaj na filtrach jako zamiast, albo nie zamiast, ale dodatkowo jako dane zdarzenie, że ja chcę przefiltrować tylko zdarzenia wpięcia do akt i mieć jakąś informację.

**Janusz Bossak:** Ale chodzi mi o to, jedna rzecz wchodząc do tej sprawy.

**Damian Kaminski:** No.

**Janusz Bossak:** Z numerkiem ID, tam nie widzę tu, jaki jest.

**Damian Kaminski:** Nie ma, bo to jest mockup. Mhm.

**Janusz Bossak:** Ale jakimś.

**Damian Kaminski:** W jakimś.

**Janusz Bossak:** To jest sprawa amoditowa.

**Damian Kaminski:** Tak, ale historia biznesowa.

**Janusz Bossak:** I wyświetlam. No nie, bo tutaj masz w tej tabeli, którą wyświetlasz po lewej stronie jest CaseID.

**Damian Kaminski:** W tabeli, no.

**Janusz Bossak:** I teraz po lewej stronie tej kolumnie, tutaj ekranu na dole, tam bazodanowych. W bazie danych masz tam coś tam, coś tam CaseID, druga pozycja nie jest CaseID, co by sugerowało, że trzeba wyświetlić z tej.

**Damian Kaminski:** A.

**Janusz Bossak:** Sprawy te rzeczy, a to nie jest tak.

**Damian Kaminski:** A jak?

**Janusz Bossak:** Bo to mogą być kompletnie różne rzeczy. Historia biznesowa zbiera historię z wielu spraw.
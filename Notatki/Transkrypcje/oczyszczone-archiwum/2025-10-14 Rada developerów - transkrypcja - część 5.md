**Data spotkania:** 14 października 2025, 08:00 - część 5

---

**Janusz Bossak:** No tak. No właśnie.

**Damian Kaminski:** No to podformularze według mnie są już dużo częściej używane w HR-owych różnych, właśnie „Zgłoś do ZUS" i tak dalej – to jest akurat, ale o formularzu. No mi się przez 5 lat zdarzyło raz.

**Łukasz Bott:** Więc jak? Tak. To znaczy.

**Janusz Bossak:** Nie, bo.

**Łukasz Bott:** Są podformularze i i formularzowy tryb, ale to wtedy to. No generalnie to działa tak, no.

**Janusz Bossak:** Chodzi – wiecie, chodzi mi o to, że mamy funkcjonalność, którą chcemy poświęcić ileś czasu. No bo Mariusz, jak się tym zajmie, to zużyje – nie wiem – 2, 3, może 5 dni.

**Łukasz Bott:** Jeśli cholera jest niewygodna?

**Damian Kaminski:** Nikt z tego nie korzysta.

**Janusz Bossak:** Ja ani nikt z tego nie korzysta, więc może lepiej poświęcić 5 dni pracy Mariusza na bardziej ciekawe zajęcia niż robienie rzeczy, z których nikt nie korzysta, nie? O to mi chodzi.

**Damian Kaminski:** No dobrze, to jaka jest konkluzja – czyli możemy wrócić do stanu takiego, żeby po prostu się to wyświetlało? Jakkolwiek, tak jak jest najłatwiej to wyświetlić. Niezależnie, czy w formularzu, czy tabelarycznym – już bym od tego w ogóle abstrachował i napisać, że wersji grudniowej nie wspieramy w wersji formularzowej w ogóle tabel, na przykład.

**Janusz Bossak:** Nigdy nie wspieraliśmy.

**Łukasz Bott:** Znaczy, podtabeli.

**Damian Kaminski:** Podtabel, tak, w sensie?

**Janusz Bossak:** Tak, zróbmy dobry. No, Piotr, rozumiem, że przywrócenie jakby działania starego jest łatwe, tak?

**Piotr Buczkowski:** Nie wiem.

**Janusz Bossak:** Nie wiesz.

**Mariusz Piotrzkowski:** Zmienił się mocno kod.

**Piotr Buczkowski:** Myślałem, myślałem, że jest łatwe.

**Mariusz Piotrzkowski:** Zmienił się mocno kod, bo był przerabiany. Przerabiany był wygląd tych formularzy, bo jak widać, na przykład na grudniowej mamy tutaj jak po prostu label, a w tym nowym już jest – pokazują. A w tym nowym jest po lewej stronie są tytułowe belki, wszystkie podpisy i się mocno zmienił. Układ mocno się zmienił. Kod – nie widziałem, kto dokładnie robił. Chyba tylko kilka osób różnych to robiło i może dlatego jest taki bałagan. No i powiem szczerze, że się zmieniło na tyle dużo, że jak sobie porównałem 2 pliki jeden do jednego, to nie wiedziałem, co jest czym. I dlatego mi zajęło tyle czasu w ogóle, żeby to ogarnąć, jak to działa – też 6 czy 7 godzin, jak wczoraj to robiłem. Plus jeszcze dzisiaj. Także nie wiem, czy przywrócenie jeden jeden do jednego będzie takie proste, biorąc pod uwagę, że mamy inny trochę wygląd, inny sposób renderowania.

**Janusz Bossak:** Zróbmy tak, Mariusz i Piotr – jeden dzień macie na taki proof of concept, czyli czy da się to zrobić szybko i łatwo czy nie? I w czwartek na Radzie przedyskutujemy dalsze kroki. Nawet niecały jeden dzień, tak, poświęcicie na to. Dobra.

**Mariusz Piotrzkowski:** Ja bym nad tym kombinował cały czas dzisiaj.

**Janusz Bossak:** Ale też, żebyś tam nie, nie za dużo – nie, tylko masz wiedzieć, czy to jest proste czy nie proste.

**Mariusz Piotrzkowski:** Trochę jeszcze pokombinuję i zobaczę, co. Według mnie właśnie teraz próbuję z czatem GPT, może mi coś podpowie z tym autem.

**Janusz Bossak:** Dobra. OK. No to tyle, czy mamy jeszcze jakieś tematy na radę?

**Piotr Buczkowski:** I ja mam uwagę do osób, które tam tę część Reactowo tak planują czy nadzorują. Sprawdzajcie, jakie są wywołania, bo w logach vlog ever znów jest pobieranie wszystkich użytkowników przez wejście, przy wejściu na List View 2.0. Jakieś menu, z którego najpewniej nikt nie skorzysta.

**Damian Kaminski:** Myślę, że można.

**Piotr Buczkowski:** To, co było, to jest to, że w formularzach są pobierane wszystkie pozycje słownika, wszyscy użytkownicy, wszystkie słowniki w przypadku – najpewniej nikt z tego nie skorzysta. Nie wiem i.

**Damian Kaminski:** Za wcześnie po prostu, tak, dopiero jeśli jest taka.

**Piotr Buczkowski:** Tak, nie, nie wiem, nie wiem, jak to pilnować, kto ma tego pilnować, jak, nie wiem.

**Damian Kaminski:** Dobra, no niech Kamil porozmawia przede wszystkim z chłopakami, no niech oni sami się pilnują. Yy, ale no rozumiem, że walidacja na drugą parę oczu jest.

**Piotr Buczkowski:** No znaczy, no bo wczoraj coś tam znaleźliśmy, błąd starego widoku List View.

**Damian Kaminski:** Pewnie potrzebna.

**Piotr Buczkowski:** Jedną rzecz tam poprawiałem, no bo ze sprawie jeszcze do starego widoku podpięcie, tak, to patrzę, a tutaj pobieramy wszystkich użytkowników. Czy wejście na ten nowy List View. No. Po co, po co? Jak niepotrzebne jest najpewniej? Jeżeli ktoś chce, jeżeli ktoś rozwinie filtr – lista użytkowników, żeby wybrać – już tylko nagle, szybko wnikną, to wtedy tak, ale też nie wszystkich.

**Damian Kaminski:** Kamil, ogarniesz to.

**Piotr Buczkowski:** W Enence jest 200000 użytkowników.

**Damian Kaminski:** No, nie mają tej perspektywy. No dobrze, że Piotr o tym mówisz, tylko trzeba z chłopakami pogadać, bo oni to testują na – właśnie nie spotkali się z takim przypadkiem i bagatelizują może.

**Kamil Dubaniowski:** Ja zaraz do Filipa się odezwę.

**Piotr Buczkowski:** No to to przypadek właśnie z użytkownikami i do logu i do edytora uprawnień do pola – czytam te sekcje. To, że to, że formularza. Też nie, też powinno być dopiero, jak to się otworzy, będzie chciał wybrać jakiegoś użytkownika. Tak. I to już jakieś stronicowanie czy tam wyszukiwanie, tak.

**Kamil Dubaniowski:** Mhm. Mm, wtedy to, że w edytorze graficznym też tak jest u Przemka.

**Piotr Buczkowski:** Tak, tak, to już jeżeli wejdziesz, jeżeli wejdziesz do ustawienie pola – nieważne, czy nawet, nawet nie dotkniesz matrycy decyzyjnej uprawnień, to i tak ci pobiera wszystkich użytkowników.

**Kamil Dubaniowski:** I matrycą prawną pewnie też. Dobra, to, jak się dogadam. Dobra, to ja miałbym jeszcze jeden temat. Właściwie Mariusza też dotyczy, zgłosiłem. Klient zgłosił baga. Enenca, konkretnie mówiąc, że w nowej wersji nie można oznaczać. No i faktycznie tak jest, tylko że to wynika z ustawień procesu, że jest wyłączone DWI i dodawanie do DWI, do contributor.

**Piotr Buczkowski:** No tak i to.

**Kamil Dubaniowski:** Tak i tak było, więc to nie jest błąd, tylko teraz. Czy to jest prawidłowe działanie? No bo wyłączamy dodawanie do DWI. To skutkuje wyłączenie możliwości oznaczania w komentarzach. Natomiast, no, jest 50 osób, które mają dostęp do tej sprawy, mają uprawnienia i ja ich nie mogę oznaczyć. Bo wyłączyłem możliwość dodawania do DWI. Nowych nie mogę dodawać, ale dlaczego nie mogę oznaczyć tych 50, które mają uprawnienia?

**Janusz Bossak:** No, tych powinno się dać. Dlaczego?

**Kamil Dubaniowski:** No właśnie, no właśnie. I to chcieliśmy potwierdzić, no bo tak to jakby wymaga zmiany całkowicie tej logiki. Aktualnie jest bardzo prosto – nie da się oznaczać nowych, to nie da się oznaczać też obecnych.

**Janusz Bossak:** Nie, nie, nie, nie, nie, nie. Wszystkich, którzy mają w danym momencie prawo do tej sprawy, mogę ich wskazać tutaj wzmiankować i dlaczego nie? To znaczy, ja takie miałem od początku jakby w głowie, że to tak działa. Wyłączenie DWI oznacza tylko, że nie mogę dodawać nowych do DWI – raczej spoza tej sprawy.

**Kamil Dubaniowski:** Tomasz.

**Damian Kaminski:** Te dysku.

**Kamil Dubaniowski:** No to tak, tak. Tak też to odebrałem, jak zacząłem jakby te testy, ale tak nie jest. W ogóle jest teraz tak, że jak masz wyłączone DWI, ale włączone contributor, no to mimo wszystko możesz tagować, możesz oznaczać kogokolwiek. Jest wyłączony contributor, którzy wyłączeni i w drugą stronę. Nie pamiętam, jakie jest zachowanie, że jak masz włączone – contributor też się nam tak. No czyli tak naprawdę to jest zależne od jednego z. Natomiast mi się wydaje, że powinniśmy przejść już czysto nad DWI, tak, czyli DWI – w ogóle zmieniłbym nazwę tego ustawienia w ustawieniach procesu, że to jest DWI i wzmiankowanie.

**Mariusz Piotrzkowski:** Też się do.

**Kamil Dubaniowski:** Żeby to było jednoznaczne, że to do tego służy. No i wyłączenie DWI i wzmiankowania – po prostu, po pierwsze, blokuje możliwość dodawania nowych DWI w tym panelu uprawnień, no i wzmiankowania nowych.

**Janusz Bossak:** To już jak tak, to już idźmy szerzej i dodajmy oprócz DWI jeszcze checkbox, że można wzmiankować czy tam – chodzi mi o to, że. Żeby używanie DWI nie było – nie dotyczyło wzmiankowania, tak. Takie wzmiankowanie byłoby osobną opcją, że w tej sprawie.

**Damian Kaminski:** Znaczy, dyskutowaliśmy na ten temat, może przypomnę – gdzieś miesiąc temu w kontekście też maili. I wtedy padł jeszcze taki pomysł, że może oprócz DWI powinna być jeszcze jakaś rola po prostu samego odczytu, bo dzisiaj DWI to jest to – są też powiadomienia o zmianie stanu i tak dalej. To też zgłoszenie u mnie wisi, to trzeba było razem zaopiekować. Czyli to, tak jak proponujesz teraz, Janusz, tak, czyli że można wzmiankować, mimo że nie można zdefiniować na DWI, tak.

**Kamil Dubaniowski:** Czy to to jest też nomenklatura? No, my to mamy tak naprawdę 3 nazwy na jedno – to są obserwatorzy. No to to, że są obserwatorami, dostają powiadomienia, no to jest jak najbardziej zgodne z nazwą „obserwator". Obserwujesz sprawę?

**Damian Kaminski:** Ale obserwacja – no tak, ale obserwator można go nazwać w takim aktywnym, czyli dostaje właśnie te powiadomienia o forward na przykład, tak. A jak ty kogoś wywołujesz w kontekście komentarza, to chcesz, żeby on teraz tu podjął jakieś działania albo się z czymś zapoznał, a on nie musi wiedzieć, że ta sprawa przeszła do kolejnej osoby i tak dalej. Więc to nie jest tożsame z DWI.

**Janusz Bossak:** No ale technicznie, jak to jest teraz – jeżeli kogoś wzmiankuję, to on jest fizycznie dodawany do DWI. Czyli od momentu, kiedy go wzmiankuję w tej sprawie, dostaje informację, że sprawa przeszła na kolejny etap, że dodano, nie wiem, plik jakiś, no tej sprawy, że normalnie, tak jakby był w.

**Kamil Dubaniowski:** Tak, tylko najlepsze jest to, że w momencie, kiedy go wzmiankuję, on jeszcze nie ma uprawnień, nie dostaje powiadomienia, że został dodany do – że został dodany komentarz. Dopiero kolejne zmiany do niego teraz.

**Janusz Bossak:** No właśnie. Takie zgłoszenie też było naprawiane chyba, czy nie?

**Kamil Dubaniowski:** No nie wiem, ja teraz je przypisałem dopiero. I przetestowałem – faktycznie tak jest, że dopiero druga akcja na sprawie dochodzi do osoby wzmiankowanej. Czyli jak ktoś mnie wzmiankuje, to nie wiem jak.

**Janusz Bossak:** Że tak było, że to już podjęliśmy, bo to dosyć takie było.

**Kamil Dubaniowski:** Nie, nie, do tej pory nie ma jakby mailowego powiadomienia, że zostałeś wzmiankowany. Ja wręcz tam rozpisałem zadanie na to, żeby był dedykowany mail inny od tego, że zostałeś dodany do – że znaczy, że został dodany komentarz. Bo teraz, jak ktoś cię wzmiankował pierwszy raz, nie dostaniesz maila. Wzmiankuje się drugi raz, to dostajesz maila, że został dodany nowy komentarz. A nie, że ktoś cię wzmiankował. W ogóle nie mamy takiego powiadomienia.

**Janusz Bossak:** Czyli wszystkie te rzeczy tylko miło potwierdzają, że powinniśmy mieć opisy tych funkcjonalności. Bo sami o tym dyskutujemy, tak, i sobie przypominamy za każdym razem. A powinniśmy zaglądać do instrukcji? Opis tam systemowych wzmiankowania i tam powinno być wszystko – to, co teraz powiedzieliśmy, opisane. Dobra, ale wracając, bo już muszę iść na spotkanie – rząd powinien działać. Według mnie, jest moja opinia, tak, w ten sposób, że to wzmiankowanie tutaj wśród osób, które już mają dostęp do sprawy, powinno być absolutnie oczywiste. I to jest taka zmiana na teraz. Jak to rozdzielanie ról przez DWI i jeszcze jakieś wzmiankowanie, to jest osobny temat. Tak, tu powinno być tak, że jeżeli to DWI jest wyłączone, to i tak, i tak mogę wzmiankować osoby, które są w sprawie. I tyle – tak powinno brzmieć poprawka do tego, co tu jest na ekranie. Dobra, ja muszę uciekać, muszę jeszcze do.

**Damian Kaminski:** Też muszę się przełączyć.

**Janusz Bossak:** No, 2 minuty.

**Kamil Dubaniowski:** Ale też zmieniamy przy okazji tego, że tylko ustawienie DWI steruje wzmiankowania. To contributor od tego odcinamy.

**Janusz Bossak:** Odcinamy. No był contributor, to jest poważniejszy temat, tak, o co, o ten.

**Kamil Dubaniowski:** OK, zgadzam się. No to, Mariusz, masz trudniejszą ścieżkę.

**Damian Kaminski:** No to nie da rady na ten sprint. To od razu trzeba by przepiąć, bo to, co Mariusz – może że się nie wyrobi.

**Mariusz Piotrzkowski:** No to już. Tak właśnie chciałem to powiedzieć, bo już jeszcze ten błąd teraz plus jeszcze inne rzeczy, które mam, to już nie ma szansy. Muszą co najmniej – co najmniej jest 10 portela, 15 zwolnić już w tym 50.

**Kamil Dubaniowski:** Dobra. To tylko przerób może forty właśnie pod tym kątem, żebym wiedział, co co zabierać.

**Janusz Bossak:** Dobra, na razie.

**Mariusz Piotrzkowski:** Jeśli mogę, wyślę listę rzeczy, które najchętniej bym komuś oddał, bo wiemy, że to się inaczej – to ktoś inny to zrobi szybciej.

**Kamil Dubaniowski:** Tam już 2 dostałem od ciebie, no to wiem. A jak masz coś jeszcze, to podrzucę.

**Mariusz Piotrzkowski:** Pewnie coś się jeszcze będzie, jak teraz ta uszczypka będzie.

**Damian Kaminski:** Kamil, jeszcze ci podesłałem powiązane z tym temat, no ale to.

**Łukasz Bott:** To jeśli.

**Damian Kaminski:** Myślę, że to trzeba na design przełożyć i zaplanować globalnie.

**Łukasz Bott:** Marek, jeszcze – Marek zgłasza tam coś z tym blockchainem, ale to rozumiem, Marek, jest grubsza sprawa.

**Marek Dziakowski:** Tak, no, no, trzeba ustalić po prostu, jak tam, jak to robimy, jak chcemy to robić. Nawet potrzebny jest Janusz.

**Łukasz Bott:** Dobra.

**Marek Dziakowski:** Bo to ostrzegam, że z kosztami po prostu.

**Damian Kaminski:** OK, no to na czwartek. Chyba, że – ale to jest jakoś krytyczne, terminowo też.

**Łukasz Bott:** Ale to, to, to.

**Damian Kaminski:** W sensie, że trzeba podjąć decyzję niezwłocznie.

**Marek Dziakowski:** Nie, trzeba to moim zdaniem zrobić w miarę szybko, ale niekoniecznie musi być to już podjęte dzisiaj.

**Łukasz Bott:** To, Marek, może w podobny sposób – jeżeli masz to przemyślane technicznie, co tam trzeba zrobić, tak czy ten, no to bądź z tym przemyśleniem, może, nie wiem, skonsultuj tutaj z kolegami, tak, i po prostu na czwartkową radę, tak, postulat.

**Marek Dziakowski:** Mhm. Mam cały dokument przygotowany, w razie co to też mogę.

**Łukasz Bott:** Okej, dobra, no po prostu to spoko.

**Marek Dziakowski:** No, no, to w czwartek po prostu przygotowane. OK. Dzięki.

**Łukasz Bott:** Dobra, w czwartek. Cześć.


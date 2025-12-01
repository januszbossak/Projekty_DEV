**Data spotkania:** 25 listopada 2025, 09:00 - część 3

---

**Janusz Bossak:** No OK, no czyli inaczej mówiąc, żebym ja sobie sam zrozumiał, czyli jeżeli trafia się w synchronizacji. Sprawa, która istnieje, ale jest dezaktywowana, czyli po naszemu usunięta i ma ten sam klucz, który teraz próbujemy synchronizować. To przywracamy tamtą sprawę z tych tak zwanych usuniętych.

**Damian Kaminski:** Tak.

**Janusz Bossak:** I synchronizujemy inne jej dane, jeżeli one tam występują jakieś, bo czasami jest aktualizacja jakichś danych, tak, nie wiem. Adres na przykład się zmienił tego kontrahenta czy cokolwiek, ale na przykład, a synchronizujemy po liście. Tak, no więc. OK, no tak może być.

**Kamil Dubaniowski:** Natomiast teraz, jeśli tą sytuację mamy, że ktoś na przykład, nie wiem, do rejestru dodał. Nową sprawę i ręcznie wyklikał identyczną, jaka była. To powoduje, że zduplikowany wpis, mamy duplikat klucza i nie blokujemy tego, tak jest.

**Damian Kaminski:** Nie, nie, nie zapisze, chyba wiesz? Wydaje mi się, że nie zapisze.

**Kamil Dubaniowski:** No zapisze, bo spraw nowych, nowych w rejestrze możesz tworzyć nieskończoność, czyli klucz jest pusty nieskończoność.

**Damian Kaminski:** Jesteś pewny, sprawdzałeś? Ale to jest, to znaczy, to jest wyłącznie tworzenie nowych jest wyjątkiem, bo, bo tu masz rację, ale chyba nie zapisze, jeśli już chcesz nadpisać klucz na taki, który istnieje.

**Kamil Dubaniowski:** No bo jeśli tak jest, no to tak samo powinno być dla nowych spraw, czyli nie pozwalamy ci tworzyć nowej sprawy w tym rejestrze, no bo.

**Damian Kaminski:** No ale to jak masz stworzyć nowy byt?

**Kamil Dubaniowski:** No już jakaś jest niezupełnie. No, no bo już jakaś nie uzupełniona jest, no to ją uzupełni. Dostęp do rejestru, do spraw rejestrze mają wszyscy. Czyli widzisz te nie uzupełnioną? No to nie zakładaj nowej, skoro jest jakaś nie uzupełniona.

**Piotr Buczkowski:** Nie, do rejestru mogą tylko administratorzy dodawać.

**Kamil Dubaniowski:** Drogi Piotrze, jeśli zablokujesz sobie realizację.

**Damian Kaminski:** Chyba że jest usunięta i wtedy jej nie widzisz. Jeszcze raz Piotr.

**Piotr Buczkowski:** Który jest tu tylko administratorzy mogą dodawać?

**Damian Kaminski:** Tak, a na raporcie jak też przycisk nowy.

**Piotr Buczkowski:** Jak ktoś o tym nie pomyślał, no to. Stary, chyba to było cenione.

**Damian Kaminski:** No to nie tak, że nie pomyślą. Według mnie to może być. Ja dawałem dostęp do rejestru dla jakiś matryc akceptacji. Na odpowiedniej grupy, tak, edytor, jakiś tam administrator matryc, wszyscy widzą matrycę, tylko jedna osoba zarządza i to nie jest administrator systemu.

**Piotr Buczkowski:** No to nie wiem, co robiłeś. Założenie było takie, że tylko administratorzy.

**Damian Kaminski:** No rozumiem, że było takie, natomiast potrzeba biznesowa przedstawiam ci, jaka jest, no, po co administratora angażować w coś, gdzie trzeba wyklikać 3 pola, nie.

**Piotr Buczkowski:** Dlatego jest, kto może tworzyć sprawy i to tu jest odwrotne zachowanie niż na zwykłych spraw.

**Damian Kaminski:** Tak. Mhm, trzeba zdefiniować.

**Piotr Buczkowski:** Dlatego jest spraw. Dla zwykłych spraw jest tak, że jeżeli tam jest pusto, to wszyscy mogą.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** A dla rejestru jest tak, że normalnie, jak tam jest pusta, to administratorzy plus chciałem osoby wymienione.

**Damian Kaminski:** No OK, no dobra, no i to jest wystarczające zabezpieczenie, to według mnie jest OK.

**Piotr Buczkowski:** No to. Tylko, że to nie jest stosowane w niektórych przypadkach, to no to coś.

**Damian Kaminski:** Nie, znaczy w tym, którym ja opisałem. Tu jest stosowane akurat.

**Janusz Bossak:** Wydaje mi się, że to jest, to jest stosowane to na tym. Dodawaniu przez tych raporty, nie, to chyba uwzględnia także dane. Jeżeli tam robiłeś, to prawdopodobnie jest tak, jak mówi Piotr, że jest w tych sprawach.

**Damian Kaminski:** Tak, tak, ja na pewno jestem pewny, że musiałem zdefiniować to, to akurat tak, tylko mówię o tym, że właśnie inne osoby niż administratorzy systemu tworzą wpisy do rejestru po prostu, no bo. Nie ma sensu angażować w taki temat administratora, jak tam jest jakiś prosto matryca. Kamil, ktoś to zgłaszał, ty to zauważyłeś.

**Kamil Dubaniowski:** Tak, no jest publika w sensie, no to jest OK. Tylko taką nazwę wymyśliliśmy. To jest ta baza wiedzy AI, a że tam 2 razy nie podświetla użytkownicy nagłówek, no to nie, nie, to tak.

**Damian Kaminski:** Nie. Tak, tak, tak, tak. Nie zgłaszałeś, tak.

**Kamil Dubaniowski:** Nie, nie, nie.

**Damian Kaminski:** Bo ja jeszcze to jest zauważam któryś raz i zawsze zapominam zapytać, to zrzucę to zaraz. Dobra, mam testować jeszcze ten. Nie, no to za długo zajmie.

**Kamil Dubaniowski:** Czy wiecie, to moim zdaniem jest znów decyzja, czy idziemy w te rejestry? Jeśli tak, to to wygląda, że trzeba to gruntownie przejrzeć, no bo wszelkiego rodzaju jakieś walidacje właśnie podczas kiedy dodajesz nową sprawę, no to powinniśmy sprawdzić, jeśli tak nie jest, nie robimy tak, no, to powinniśmy to dodać, dedykowane jakiś widok pod listę tych rejestrów i żeby pod każdy rejestr nie trzeba było wyklikać nowego raportu, żeby było po prostu to obsłużone jak słowniki, że jest coś typu rejestr, mam do tego dedykowaną stronę, widzę wszystkie procesy typu rejestr i jak kliknę sobie w jakiś, to widzę. Już domyślnie spraw w tym rejestrze, tak jak widzę listę słowników, pozycji w słowniku, nie, no to jest takie. Wiemy, że jest, trzeba wiedzieć, jak działa, no i.

**Damian Kaminski:** Znaczy, ja bym uciął dyskusję mówiąc szczerze, bo to nie jest coś, gdzie klient czeka. Gdzieś ktoś nas za to płaci, to jest coś, co wszyscy wiemy, jak działa, tylko nie działa idealnie, intuicyjnie, trzeba według mnie zrobić tu dopisek, bo to jest.

**Janusz Bossak:** To trzeba zrobić.

**Kamil Dubaniowski:** I znam przypadki, gdzie nie działa dobrze.

**Janusz Bossak:** Ale, ale. Nie, nie, nie.

**Damian Kaminski:** Nie.

**Janusz Bossak:** Nie, do nie do końca jest tak, Damian mówisz, dla mnie to jest naprawdę skrócenie czasu wdrożeń, za każdym razem jest ten sam problem. Był taki. Pamiętacie pomysł, żeby był podgląd rejestru, ale nawet.

**Piotr Buczkowski:** Żeby nie używać rejestru.

**Kamil Dubaniowski:** No i powstałe w sumie źródła, w sumie powstały odnośniki do źródeł, no i teraz czy my tam opiekujemy to, że coś zostanie wywalone ze źródła, a zostało użyte na sprawach AMODIT? Wydaje mi się, że nie zniknie ze spraw w AMODIT.

**Janusz Bossak:** Jak?

**Damian Kaminski:** Najlepiej.

**Janusz Bossak:** Jak Piotr zaproponuj. Szukajcie, dajcie mi dokończyć tą myśl, bo jak nie był taki pomysł, żeby w tym obszarze, gdzie jest definicja procesu, było była zakładka z takim, nazwijmy to podglądem spraw tego procesu właśnie dla admina, tak, czyli admin wchodzi i tam sobie może obejrzeć wszystkie sprawy, nie musi wchodzić na jakieś wszystkie czy zamknięte czy gdzieś, tylko tu miałby podgląd w ramach tej definicji procesu i między innymi to miało rozwiązywać temat.

**Damian Kaminski:** Tak.

**Janusz Bossak:** Właśnie tego, co powiedziałeś Kamil, czyli podglądu, że nie trzeba tworzyć jakiegoś raportu, czyli tutaj tak jak zakładka ostatnia tam za jakąś historią, czy za czymś, klikasz i masz po prostu podgląd. Spraw tego procesu jako admin.

**Lukasz Bott:** Postulowali, że w tej zakładce raporty, tak, po prostu domyślny raport pokazujący wszystkie sprawy z danego rejestru, taki predefiniowany.

**Janusz Bossak:** Tak też taki. Taki pomysł też.

**Damian Kaminski:** No dobra, tylko co nam to da w sensie?

**Janusz Bossak:** Upraszcza w drodze.

**Damian Kaminski:** Ktoś dobrze przygotowuje proces to. Wdrożenie to powinien sam zrobić już taki raport, nie. Ale my chcemy go zrobić odgórnie.

**Janusz Bossak:** Upraszcza, że nie trzeba robić takiego raportu, no tyle jest.

**Damian Kaminski:** Ale to ma dotyczyć tylko rejestrów.

**Janusz Bossak:** Po prostu.

**Lukasz Bott:** W zasadzie to by mogli dojrzeć każdych procesów.

**Janusz Bossak:** Początkowo. Dokładnie. To jest widok dla admina. Tak, wchodzi definicję procesu i żeby nie musiał biegać gdzieś tam do zakładki wszystkie i szukać jakiegoś przykładu z tego procesu, to po prostu tom ma tak tego.

**Damian Kaminski:** No to może raporty systemowe?

**Lukasz Bott:** Nie, nie łącz tego systemowymi mną.

**Damian Kaminski:** Powinny to agregować. No a gdzie będziesz to wrzucał, jak procesów będzie 20, zaśmiecisz ten ekran, a w definicji tak.

**Janusz Bossak:** Dobra.

**Lukasz Bott:** Nie, definicji tak, nie definicji procesu masz zakładkę raporty i.

**Janusz Bossak:** Nicy.

**Lukasz Bott:** Klikasz na to, to ci się domyślnie otwiera domyślny raport z zestawieniem wszystkich spraw w danym, może by się jakoś tam domyślnie przefiltrowany, tak, żeby to nie wiem pokazywał. Ostatnie ileś, tak, ale resztę sobie możesz ustawić, czy chcesz oglądać usunięte, nie usunięte, zamknięte, otwarte, no czyli jakiekolwiek inne filtry, no.

**Janusz Bossak:** Znaczy, ja bym był za tym, żeby to tak, znaczy może być taki raport, ale to trochę jest bardziej skomplikowane. No bo wchodzisz w raporty gdzieś tam tutaj, po prostu tak jak masz szablony czy tam formularz, etapy. I tak jedna zakładka dodatkowa. Gdzie są lista spraw i wchodzisz i ta lista spraw odpowiada właściwie temu, co jest na zakładce wszystkie.

**Lukasz Bott:** No muszę ten. Lista spraw. Wszystkie, zamknięte, usunięte.

**Damian Kaminski:** Ale przefiltrowane, no wszystkie, zamknięte, usunięte, przefiltrowane po procesie, tak.

**Lukasz Bott:** Tak, po tym konkretnym procesie.

**Janusz Bossak:** Dokładnie tym proc. Czy rejestrze?

**Damian Kaminski:** No bo wiecie tutaj, tak.

**Lukasz Bott:** Z uwzględnieniem uprawnień.

**Janusz Bossak:** Tak.

**Damian Kaminski:** Już róbmy, już wrzucajmy już nowy moduł, jeśli już nie.

**Janusz Bossak:** Słuchajcie, mamy jeszcze jeden temat na tą radę, przepraszam, ale to, to dokończmy ten, popłynęliśmy z tematem.

**Damian Kaminski:** Na.

**Lukasz Bott:** Ja je mamy 2 tematy – twój z DokSignem, ja jeszcze jeden.

**Damian Kaminski:** Dobra, ja tutaj opiszę te kilka przykładów, najwyżej przedstawię to na którejś kolejnej Radzie. Zacznę od tego, żeby tutaj po prostu poprawić ten komunikat, bo to według mnie już rozwiąże część problemów.

**Lukasz Bott:** Znaczy. Dokładnie tak i to. Dokładnie tak.

**Damian Kaminski:** Dobra, co jeszcze mamy otworzyć? Czy to nie ma wpisu?

**Lukasz Bott:** To ja już.

**Janusz Bossak:** W moim temacie czy jeszcze?


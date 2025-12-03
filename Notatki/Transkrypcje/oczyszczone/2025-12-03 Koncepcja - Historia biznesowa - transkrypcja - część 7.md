**Data spotkania:** 3 grudnia 2025, 10:16 - część 7

---

**Damian Kaminski:** Do tego klienta, ale może być też z poziomu zakładki procesy. Stwórz nową polisę, dopiero przypinam tego klienta. I wtedy pod jakimś przyciskiem przekaż dalej. Ja odwołuję się, że connectedCase to będzie to, co jest osadzone w polu klient. I wtedy to jest connectedCase. Tak, też ten lewy, ten, ale w inny sposób jest to wiązany, tak?

**Janusz Bossak:** Jest. Ale. I ten przykład z tym klientem jest idealny również do JRWA. Tak, tylko że klient tam, gdzie jest napisane klient, wystarczyłoby, żeby było napisane teczka JRWA i tyle.

**Damian Kaminski:** Tak, dokładnie to jest ten sam przykład. Tak, tak, tak.

**Janusz Bossak:** Po prostu polisę jeden przypinamy do teczki JRWA, jakiejś polisy. Drugą fakturę przypinamy do jakiejś teczki i to się dzieje wtedy ręcznie. Ktoś to teraz Marek robi, ma pole typu linked i klient. Użytkownik wybiera, że tą sprawę, ten dokument ja przypinam do teczki JRWA takiej. Albo tak jak tu przypadku tego klienta, przypinam tą do teczki, tylko do w pewnym sensie teczki, do folderu tego klienta, że jak wejdę na klienta, to żeby mógł to zobaczyć. Dobrze, bardzo dobrze to rozkręciliśmy.

**Damian Kaminski:** Tak, bo to właśnie to daje. Ja dopiero teraz, bo cały czas zastanawiam się czemu upierasz się tak przy tej teczce. Ale teraz chyba dopiero to zauważam, że obsadzając teczkę. Bo teraz spójrzmy na tą teczkę, jeszcze taką perspektywę szybko wrzucę. Jest ta teczka, tak jak powiedziałeś, bo klient to co do zasady, jak jest polisa, to się nie zmienia. Ale teczka ma zupełnie inny wymiar. I teraz ja będąc opiekunem teczki, tracąc jakiś dokument, nie mam w ogóle o tym wiedzy. Ktoś na dokumencie, powiedzmy, kto miał uprawnienia ją wypiął, ale na teczce się nic nie odkłada, bo tam jest tylko raport z tych, które są aktualnie podpięte. A dzięki temu ja znajdę zdarzenie wypięcie z teczki.

**Janusz Bossak:** Dokładnie.

**Damian Kaminski:** I znajdę czemu. I wtedy będę szukał, czemu ty to wypiłeś? Czemu ja tego nie widzę? Ja nie pamiętam.

**Janusz Bossak:** Ładnie. Dokładnie, o to chodzi.

**Damian Kaminski:** OK, to to jest duża wartość dodana.

**Janusz Bossak:** Dokładnie o to chodzi. I tak tam nawet mówiłeś, że ktoś pomylił, wysłał do kogoś innego. To jest teraz już decyzja biznesowa, czy chcesz ten fakt zapisywać. Bo może na przykład w bardzo restrykcyjnych procesach typu.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Korespondencja do prezesa. Może jest ważne, że poszło to do jakiegoś Kowalskiego, a on nie miał prawa tego przeczytać nawet.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** I to jest na przykład incydent bezpieczeństwa jakiś. Więc mając taką historię, jesteś w stanie wykryć takie rzeczy.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** Także to według mnie ten element spinający jest tutaj niezwykle istotny. I ten właśnie aspekt wielowymiarowej historii jest również niezwykle istotne. Że ja mógłbym przypisywać to do różnych rzeczy. Bo teraz ta korespondencja X tutaj, wracając do tego twojego przykładu. Mogłoby być tak hipotetycznie, że na tej sprawie korespondencji X ja wybieram tego klienta jednak. I teraz zobacz, jak pięknie to się dzieje, bo z jednej strony masz historię biznesową tego, że ta korespondencja X powstała z tych technicznych pobrań e-Doręczeń. OK, to jest to connectedCaseID jeden. Ale jednocześnie mogę mieć drugie connectedCaseID do klienta.

**Damian Kaminski:** A no właśnie, czyli dopuszczamy tutaj formę taką, tak.

**Janusz Bossak:** To jest tam, tak jest, to jest ta wielowymiarowość, o którą mi ciągle chodzi.

**Damian Kaminski:** OK, dobra, to Łukasz coś zmienia, czy to jest w ramach całego?

**Lukasz Brocki:** Nie, od strony bazy danych, jeżeli bierzemy ten mój pomysł z drugą tą tabelą, nie ma żadnej różnicy.

**Janusz Bossak:** Dokładnie i teraz zauważ.

**Damian Kaminski:** Czyli mamy, my, czyli mamy taki zapis wtedy tak, że tu jest connectedCaseID jakiś, powiedzmy tu już abstrakcyjny i po prostu jak.

**Janusz Bossak:** Dokładnie i mało tego, możesz mieć nawet.

**Damian Kaminski:** Ale to wtedy mocno komplikujemy.

**Janusz Bossak:** Nawet nie tak, bo to może być. Nie, dobrze, nie, nie, nie komplikujemy. Zauważ, teraz ten obieg korespondencji może być związany z tą polisą jeden. Ja mogę chcieć żyć tam tą informację.

**Damian Kaminski:** Masz rację, masz rację, że to może być tylko może być tak i może być jeszcze nawet tam przez to z klientem. Tylko teraz pozostaje kwestia skomplikowana, że. Aha, czekajcie, bo to connected, czyli tak teraz case. Czyli nie tu źle zapisałem, to nie w tym miejscu. To powinno być, jeśli skoro połączyłem dwójkę, ojejku.

**Janusz Bossak:** Natomiast teraz przeszła mi myśl inna, taka sam się zagapiłem w głowie. Bo patrząc na właśnie JRWA, bo akurat koncepcja JRWA jest bardzo fajna. Tam jest jedna podstawowa zasada, której nie wolno łamać, a mianowicie, że jakiś dokument siedzi w jednej teczce fizycznie. Ale to wynika z innych jakby historycznych rzeczy. Bo dokument, jak wpłynął, to został jakoś tam zaindeksowanych, mówię o takich analogowych dokumentach, i fizycznie można było go wpiąć do jednej teczki. Chodziło o to, że nie wolno robić kopii, bo potem nie wiadomo w ilu teczkach te kopie się znajdują. To tylko ma być w jednej. I to jest jakby idea JRWA. Tutaj teraz, mówiąc w ten sposób elektronicznie, my możemy sobie to inaczej organizować. Czy możemy ten pojedynczy dokument teoretycznie wiązać z tą dowolną ilością miejsc, gdzie chcemy go wpiąć. I to właśnie ta historia biznesowa, że łączymy go tutaj, łączymy go tutaj i tak dalej. Ale żebyśmy nie przekombinowali naprawdę, bo mam wrażenie, że zaczniemy za chwilę za bardzo kombinować. Ale jeżeli ma.

**Damian Kaminski:** Dobra, czyli po prostu wtedy wchodząc w obieg korespondencji X, mielibyśmy dodatkową informację, że historii polisy jeden. Bo jeśli to tak powiążemy, to wszystko co będzie tu.

**Janusz Bossak:** Jako nie, niekoniecznie. Znaczy musisz, bo zastrzegam, jak jesteśmy na obiegu korespondencji X, to będziemy wiedzieli, że to ma wpływ na polisę jeden i tak zostało. Jak wejdziesz raz na polisę jeden, to zobaczysz, że wpłynęła korespondencja.

**Damian Kaminski:** Mhm.

**Janusz Bossak:** To będzie informacja z poziomu polisy jeden. Czyli.

**Damian Kaminski:** No tak, ale w kontekście takim jak tu nie będzie informacji, że ta korespondencja była błędnie przypisana.

**Janusz Bossak:** Bo błędnie przypisanie okaże się później.

**Damian Kaminski:** No tak.

**Janusz Bossak:** Błędne przypisanie okaże się później. I wtedy, kiedy ono się okaże, wtedy wpiszesz do historii.

**Damian Kaminski:** Błędne.

**Janusz Bossak:** Błędne przypisanie i wpiszesz do historii, cofnięto do jakiegoś punktu.

**Damian Kaminski:** Ale to będzie tylko na tej historii, a na te już nie będzie tego.

**Janusz Bossak:** A jest potrzebny?

**Damian Kaminski:** Nie, nie, nie mówię, że jest potrzebne, tylko że tak będzie, że tu będzie fałszywa informacja. Dopiero możliwość dojścia tu, ale skoro ktoś wiąże, to raczej powinien mieć jakieś. Tutaj tak nie jest.

**Janusz Bossak:** A może być, może być tak, że dopóty, dopóki się ta sprawa tej korespondencji nie ogarnie, czyli nie trafi do właściwej osoby, to nikt tego do tej polisy jeden nie przypnie.

**Damian Kaminski:** To też racja, że to może nie jest akurat dobry przykład. To zgadzam się z tobą, też miałem takie przed chwilą przemyślenie, że dopiero jak ktoś przypnie tą polisę. Więc to jest jakiś bardzo trzeba było znaleźć przypadek biznesowy do takiego spięcia, ale.

**Janusz Bossak:** Stary. Prawdopodobnie tak korespondencja zostanie przez kogoś merytorycznego właściwego.

**Damian Kaminski:** Zatwierdzono, dopiero będzie przypięta.

**Janusz Bossak:** I on ten człowiek będzie zajmował się tą polisą i on będzie wiedział, że aha, bo patrzcie, wpłynęła polisa. I to, że ona krążyła po firmie, ktoś to źle przypiął. Z punktu widzenia tego człowieka nie ma żadnego znaczenia już. To jest zupełnie coś innego dla niego. Zdarzenie jest wpłynęła korespondencja i on to odnotowuje jako właściwe zdarzenie dla tej polisy.
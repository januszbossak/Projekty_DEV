**Data spotkania:** 4 grudnia 2025, 12:02 - część 3

---

**[Paulina Wesołowska]:** Ja też prześlę przykład tutaj. Przepraszam, że przerwałam.

**[Janusz Bossak]:** Może to jest kwestia... Nie, bo ja chcę pokazać coś na żywym organizmie. Kliknij teraz „Zapisz”.

**[Miłosz Śliwiński]:** Mhm.

**[Janusz Bossak]:** Kliknij teraz „Pokaż”. I to, po prawej stronie, jest jakby słownik wszystkich pól wymaganych niewypełnionych. Nawet jeżeli by były w innych sekcjach czy cokolwiek, to użytkownik może klikać w nie bezpośrednio i przechodzić od razu do tego pola, które ma wypełnić. Nawet jeżeli one są tak jak widać tutaj – są 2 sekcje, akurat w sekcji drugiej nie ma żadnych pól, ale gdybyśmy tutaj byli nawet w sekcji pierwszej... Teraz tam co masz tą nazwaną? Weź tą drugą, w której nie ma pól. I teraz kliknij tutaj – to nas przenosi do tej sekcji, w której te pola są wymagane. Więc w moim przekonaniu ten flow tutaj jest dość wygodny. Po pierwsze system informuje, że formularz nie jest kompletny i brakuje np. 2 wymaganych pól. Kliknięcie tego „Pokaż” pokazuje nam panel, gdzie brakują te wymagane pola i mam dzięki temu spis treści czy linki do tego, żeby od razu przejść do tych konkretnych pól. Jeżeli to tekstowe drugie wypełnię, to ono znika z tej listy. Zostaje nam kolejne do wypełnienia.

**[Paulina Wesołowska]:** Tak, tylko trzeba najpierw kliknąć „Zapisz”, czego do tej pory nie było.

**[Janusz Bossak]:** To też był jeden z jedna z uwag klientów. Właśnie, że tak chcą, żeby nie pokazywało się na początku. Że biznes wie.

**[Daniel Reszka]:** Że się... tak jak robicie na przykład, nie wiem, wypełniacie konto, zakładacie nowe konto na jakimś portalu zakupowym, to przecież też najpierw wypełniacie. Potem jak nie podacie adresu zamieszkania czy mailowego, to robi się, że pole wymagane. A najpierw nie wiesz, które jest wymagane. Często tak jest.

**[Janusz Bossak]:** No taka jest zasada.

**[Daniel Reszka]:** Dopiero po zapisaniu.

**[Miłosz Śliwiński]:** Znaczy tak, ja to rozumiem, tylko...

**[Paulina Wesołowska]:** Tylko daliśmy coś użytkownikom, a teraz im zabierzemy. Nie? Czyli tutaj mamy też trochę taką niekonsekwencję.

**[Paulina Wesołowska]:** W przypadku tych... Tu daliśmy 255 i nie chcemy im skrócić, a teraz daliśmy im wymagane, ale im zabierzemy.

**[Janusz Bossak]:** Znaczy, to jest coś innego, bo tamto to są zmiany w bazie danych, a to są kwestie wizualne.

**[Daniel Reszka]:** Znaczy Paulinie chyba chodzi o teorię, że nie zabieramy czegoś wstecz. Takie podejście.

**[Paulina Wesołowska]:** Tak, tak, tak, dokładnie tak.

**[Miłosz Śliwiński]:** Podejście. Bo to dla mnie idealnym rozwiązaniem by było, jakby standardowo można było ustawić na tym polu tekstowym ten widok po zapisie. I to jest dla mnie akceptowalne, bo to jest okej bazowo na starcie, żeby to było można w taki sposób wizualizować już.

**[Janusz Bossak]:** Potem do okej... Jeżeli do przemyślenia jest funkcjonalność taka, że na danym procesie – bo ja bym to robił per proces – że ma się zachowywać tak jak teraz widać. Czyli że wyświetla od razu komunikat o tym, że brakuje jakichś pól wymaganych. A dla innych ta opcja nie będzie włączona, będzie wyświetlało tak po nowemu jak jest, czyli tylko podkreślenie i bez takiego komunikatu. No okej, możemy tak.

**[Miłosz Śliwiński]:** Tak, dla nas, dla mnie to jest wystarczające rozwiązanie. No bo to bazowo dostajemy jakby informacje o polu wymaganym podkreślonym. Ja wiem, że ty Michał jesteś zwolennikiem minimalizacji? Że to by ci się chyba podobał ten wariant. W ogóle, żeby tam nie było... jak najmniej było na widoku.

**[Michał Mirończuk]:** No i ja nie powinienem tutaj się wypowiadać, bo ja tu polegam na większości naszego zespołu. Jakby ja chętniej bardziej w tym pierwszym temacie bym się wypowiedział, ale tam Miły powiedziałeś wszystko i konsensus według mnie jest dobry. W drugim wolałbym się nie wypowiadać, bo mi nowe rozwiązanie pasuje, więc ja tu się dostosowuję do zdania zespołu.

**[Daniel Reszka]:** Czy sterowanie tym jest konsensusem? Czyli jeżeli to było sterowalne per proces albo per AMODIT? No to pytanie Janusz, czy to jest prostsze do wykonania? Bo żeby to zaraz nie wyszło, że to jest jakaś trudna rzecz.

**[Janusz Bossak]:** Nie no wiecie, no jest to... i tak objawia się to, to nie jest coś, czego nie ma. Tylko trzeba dodać opcję, żeby się wyświetlało albo tak, albo tak.

**[Miłosz Śliwiński]:** Wiecie? Jakby moje podejście jakie jest do tego tematu... To jest tak jak rozmawialiśmy na początku. Kwestie wizualne są indywidualne, jeden powie tak, drugi powie tak. Ja patrzę pod kątem efektywności, ilości zgłoszeń i procesów, które mamy do obsłużenia. Ja jestem prawie przekonany, że jak zabiorę na procesie w Opolskim, gdzie mamy procedowanych, nie wiem, 200 faktur dziennie, 200 umów dziennie... Jak zabiorę pole wymagane, to połowa osób będzie miała problem z uzupełnieniem i zasypie nas całą serią zgłoszeń. I teraz ja dostanę obciążenie na zespół, żeby wytłumaczyć ludziom, że zmienił się widok.

**[Miłosz Śliwiński]:** Oczywiście, tak jak tam Daniel też pisałem wcześniej, że musimy przygotować całą tę zmianę wizualną. Musimy administratorom i biznesom dać znać, oni muszą zaktualizować dokumentację i też obsługiwać te pytania. Dlatego to tylko z mojej perspektywy chodzi o efektywność. Ja kupuję ten argument, że to jest ładniejsze. W ogóle najchętniej to bym zostawił gwiazdki czerwone, jakby były przy tytułach spraw i to by było dla mnie najbardziej w porządku, jeśli chodzi o wymagalność pól. Ale ja wiem, dlaczego Paulina to zgłasza, bo Paulina obsługuje tych specyficznych użytkowników u nas. Różne daty... jak nie świeci się na pomarańczowo i nie bije od razu po oczach, co tutaj trzeba zrobić, to jest zaraz seria zgłoszeń.

**[Miłosz Śliwiński]:** My też jakby... Ja jestem wyczulony pod tym względem, bo my kiedyś projektowaliśmy – mamy taki swój system obsługi klienta, WinBiuro się nazywa i ono służy do realizacji zamówień. My kiedyś zmieniliśmy kolorystykę, bo dostaliśmy całą serię zgłoszeń od użytkowników na temat kolorystyki, że za bardzo bije po oczach. I to, że bije po oczach przy 8 czy 10 godzinach pracy jest bardzo uciążliwe. Zmieniliśmy kolorystykę na pastelowe kolory i to się skończyło buntem. Dostaliśmy około tysiąca zgłoszeń i strajk na pokładzie ludzi z WinBiura, którzy pracowali na co dzień. Że jak nie cofniemy starego widoku, to... Bo oni dostali po targetach, bo już byli tak nauczeni na pamięć, że klikali po prostu w kolorki. Spadły im targety tam o 30%, co spowodowało, że dostali mniejsze premie i był strajk na pokładzie. Musimy przywrócić stary widok i stary widok już został finalnie wdrożony.

**[Miłosz Śliwiński]:** Ja się boję tylko tutaj, bo tu jest dużo takich procesów, które my mamy obsługowych, że u nas będzie podobny mechanizm. Że będzie odbiór tego i jak to testowaliśmy z tymi użytkownikami... Stąd też ten mail, to zgłoszenie na rozwiązanie kompromisowe. Że będzie podobna sytuacja, że my im wdrożymy, damy im instrukcje, wytłumaczymy, że teraz tak jest nowocześnie i lepiej, a podejście będzie: „Halo, my chcemy po staremu, bo było to czytelniej, było prościej” i tak dalej. A w ogóle mi się podoba... Ja pierwszy raz widzę, nie zwróciłem uwagi w ogóle na ten element, że te pola wymagane pojawiają się w tej kolumnie obok i można się przeklikiwać. To jest w ogóle mega fajne rozwiązanie.

**[Daniel Reszka]:** Nie wiem tylko Janusz, jaka jest kolejność tutaj, bo to nie jest kolejność z formularza. To do sprawdzenia, ewentualnie czemu to jest drugie a tamto pierwsze, ale to już niuanse.

**[Janusz Bossak]:** Też nie wiem szczerze mówiąc, dlaczego tak się wyświetla w tej kolejności. Powinno tak jak mówisz, po kolei. Trudno powiedzieć, nie wiem, nie znam odpowiedzi w tej chwili.

**[Daniel Reszka]:** Nie no mówię, niuans po prostu do sprawdzenia wewnętrznie.

**[Miłosz Śliwiński]:** No dobra, to teraz pytanie do mojego zespołu: Paulino, Michale, czy ten kompromis, w którym zmienimy ilość kolumn (czyli odblokujemy ilość kolumn dla folderów, żeby się skalowały do wielkości ekranu), pogrubienia rozumiem nie zmieniamy (bo to taka decyzja większości klientów, to ja to akceptuję), oddzielamy poziom procesów od folderów i dodajemy ten podpis „pole jest wymagane” przy tym lekkim... sterowalne per proces? To, czy to rozwiązuje wszystkie nasze bolączki, czy jeszcze coś było? Aha, no i ten dymek, który przysłaniał cofanie.

**[Janusz Bossak]:** Tak, tak, to trzeba poprawić. Znaczy on się po prostu dla pierwszego wiersza tych kafelków powinien wyświetlać na dole, czyli pod kafelkiem, a nie nad kafelkiem.

**[Michał Mirończuk]:** Ja bym wrócił do pól pogrubionych. Tutaj pan Janusz powiedział, że być może byłaby taka możliwość, żeby zrobić taką opcję. Zakładam, że w ustawieniach systemowych? To myślę, że to by było coś, co by nas mocno interesowało. Bo ilość kolumn jak najbardziej – tu pełna zgoda. Co do rozdzielenia procesów i folderów – oczywiście również pełna zgoda. I wówczas nie kruszyłbym już w ogóle kopii o to, czy coś jest do lewej czy do środka, bo jakby to było rozluźnione, to od razu by się momentalnie też uczytelniło. Natomiast przyznam, że w mojej opinii – nie tylko mojej – jednolita czcionka powoduje zlewanie się wszystkiego w jedno. Więc jakby była jednak taka opcja, dzięki której można by pogrubić czcionki folderów, to my bylibyśmy tym żywo zainteresowani. Co do pól wymaganych – wydaje mi się również, że kompromis jest bardzo dobry.

**[Janusz Bossak]:** Dobrze.

**[Michał Mirończuk]:** No pewnie tak jak Miły zauważyłeś, ja w swoich procesach pewnie będę stosował nowe rozwiązanie. Paulina dla swoich podopiecznych ze swoich procesów rozwiązanie kompromisowe. No i tak, to by myślę obsługiwało nasze potrzeby.

**[Miłosz Śliwiński]:** Zobaczymy jak długo, jak cię zasypią zgłoszeniami.

**[Janusz Bossak]:** Wiecie, no mówi się, że przyzwyczajenie drugą naturą człowieka. To, co Miłosz tam o przyzwyczajeniach w zespole tego biura... Z jednej strony też tutaj jako klient mówicie nam, że no on może nie jest ładny i tak dalej, no więc podjęliśmy te próby sprostania temu, żeby był trochę ładniejszy, więc no to są te nasze propozycje. No mamy o tyle utrudnione, że mamy tam prawie 200 klientów, w tym kilku czy kilkunastu bardzo dużych, tak jak wy. No i to trochę takie przeciąganie liny, tak? Każdy coś tam argumentuje, jedni chcą tak, inni tak. Więc tam gdzie możemy, to robimy różnego rodzaju kompromisy właśnie w postaci różnych opcji.


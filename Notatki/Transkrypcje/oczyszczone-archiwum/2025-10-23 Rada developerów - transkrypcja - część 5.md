**Data spotkania:** 23 października 2025, 08:02 - część 5

---

**Damian Kaminski:** SinnerRoll. Ograniczyłem.

**Anna Skupinska:** Pytanie – czy, czyli rozumiem, że wywołujesz błąd w nowym module?

**Damian Kaminski:** Próbuję zrobić taki błąd, jak był. Próbuję zrobić taką sytuację, jak taka powodowała błąd właśnie u klienta, ale może to już jest obsłużone.

**Anna Skupinska:** Możliwe, że – tak, możliwe, że został naprawiony.

**Damian Kaminski:** Bo moment – jeszcze raz – czy ja coś źle robię? Formularz jest SinnerRoll. Uprawnienia. Widoczny tylko dla – Damian Kamiński. Aha, dobra – to inaczej, nie ten Damian Kamiński. Widoczny tylko dla Damian jeden Kamiński. Jeden. Zapisz. OK, teraz. I teraz tak – ja powinienem to widzieć? I widzę, ale teraz przeloguję się na... Czemu tego nie ma? Dobra, przygotowuję się na drugiego. Jeden-dwa. Raporty. Cyk. No właśnie – to już nie powoduje błędu, ten problem. Nie widzę tutaj "SinnerRoll jeden", a tutaj jest tak – SinnerRoll – przepraszam – a tutaj jest pusto. No, wcześniej jak była taka sytuacja, że coś widzi – tylko jeden użytkownik – ha, chyba że – chyba, że muszę dać "Oraz czynności". Dobre – to nie jest.

**Anna Skupinska:** Wiesz co, mam pomysł, jak może wywołać błąd. Jak tutaj on wysyła zapytanie – to jest zapytanie – jest ID procesu. Możesz zmienić ID procesu na jakiś proces, który nie istnieje. To na pewno – to będzie błąd wcześniej, bo on próbuje się dostać tego procesu, nie będzie mógł. To nieważne...

**Damian Kaminski:** Nie, nie – to źle, źle – zły przykład, bo tam były wiele procesów z tymi samymi polami. Wtedy był zwrotka z błędem, że jest nierówna ilość kolumn, więc to nie jest dobry przykład, bo tu po prostu nie wyświetla tej kolumny w odpowiedzi i nie ma, a tam w jednym procesie o takiej samej nazwie pola – była ta kolumna dostępna wszystkim, a druga – w sensie da się to odtworzyć, ale nie tak szybko, jak chciałem. Dobra, słuchajcie – to ja mogę z tym pomóc. Natomiast zawieśmy to – zaraz zrobię taki przykład – skopiuję ten proces, na nim zrobię odblokowanie. Jeśli to się uda, to dam ci przykład do testów i sprawdzimy, że to działa, bo ten bug według mnie jeszcze nie został wyeliminowany. I ja – jeśli mamy jeszcze przestrzeń – albo prośba do Piotra – to ja bym chętnie poruszył tą kwestię repozytorium plików. Albo po prostu żebyś sam przez to przeszedł, albo ja to teraz zaprezentuję, zadasz pytania, albo – na co zwrócić uwagę, bo pewnie nie miałeś na to przestrzeni, nie?

**Piotr Buczkowski:** No nie wiem, powiedz o co chodzi, bo...

**Damian Kaminski:** No więc tak – repozytorium plików w ramach AMODIT, czyli coś – nie dla form – nie związane ze sprawami. No i jeśli chodzi o funkcjonalności, jakie tutaj są proponowane, to mamy coś takiego jak przestrzenie, czyli powiedzmy najwyższy poziom – no, najwyższy poziom, powiedzmy, takiego węzła, tak? Wewnątrz mamy – i można te przestrzenie definiować sobie, tak – wewnątrz mamy pliki – te, przepraszam – foldery. Te foldery można definiować. No, to – to myślę, że jest dość oczywiste. Natomiast teraz kolejnym elementem jest nadawanie uprawnień w ramach tych przestrzeni. Tu jako administrator od razu widzę, że coś – jakąś ikonką na razie jeszcze, może niekoniecznie będzie to taka, ale że na tym poziomie uprawnienia są zerwane, czyli tutaj jak wejdziemy – tu mamy "Przerwij dziedziczenie uprawnień" zaznaczone, co skutkuje właśnie pokazaniem jakiejś ikonki. Na razie to są takie ludziki. Bo domyślnie "Architektura", która – systemu – dla przykładu – po prostu dziedziczy z przestrzeni węzła nadrzędnego, tak? A ten węzeł z kolei – tu nadrzędny – dziedziczy jeszcze z węzła nadrzędnego, czyli w zasadzie tu są zdefiniowane uprawnienia – kto do czego ma dostęp. I na folderach jest to, powiedzmy, prostsze, ale trzeba też te uprawnienia nadać na poziomie pojedynczych plików, czyli może być sytuacja taka, że ja zrywam uprawnienia dla tego pliku i tutaj, powiedzmy, definiuję, że – technologia widzi ten plik. Co jednocześnie...

**Piotr Buczkowski:** Znaczy, czy to ma sens?

**Damian Kaminski:** No.

**Piotr Buczkowski:** Ewentualnie tylko powinna być możliwość ograniczenia dostępu w porównaniu do tego, co jest w folderze, tak? Folder – w folderze, powiedzmy, mamy 3 osoby, a do tego pliku tylko 2. A nie, to już – na przykład – ten plik ma całkiem kto inny niż – to nie ma dostępu do folderu.

**Damian Kaminski:** No, tylko – co – to tylko jeśli zrobimy tak, jak mówisz? To jeśli zejdę tutaj na "Diagramy" i chcę to udostępnić jakiemuś IT – to wtedy muszę wejść wyżej, udostępnić to – IT, udostępnić to – IT, udostępnić to – IT – i dopiero tutaj będę miał wybór, że to też mogę udostępnić temu IT. Nic innego stąd nie chcę. A jeśli mamy to właśnie w takiej formie, no to wtedy ja to udostępnię...

**Piotr Buczkowski:** O, jak to wyświetlać wtedy?

**Damian Kaminski:** Jakiemu? Już, już mówię, już mówię. I teraz – tego tu nie ma, niestety. Na tym makiecie – jeśli byśmy zrobili tak, że to IT ma ten plik, to wyświetlamy – to wtedy wejdźmy sobie na "Architektura" i tu w "Uprawnienia" – to tutaj wyświetli się, że...

**Piotr Buczkowski:** Znaczy, to trzeba byłoby tak, że uprawnień do folderu – typu "Folder", tak.

**Damian Kaminski:** Dokładnie, tylko...

**Piotr Buczkowski:** Proszę, ale widzisz, że widzisz tylko folder – nie widzieć zawartości, tak.

**Damian Kaminski:** To znaczy – może w niego wejść, ale w nim jest tylko ten folder "Diagramy", tak – czyli może widzisz strukturę do góry, tak? Taki był – takie było założenie, tylko tu chyba, niestety, popełniłem pewien błąd. Poczekaj. Przed tutaj tego nie – myśmy tego Jana Nowaka – albo inaczej – czy on tutaj jest? O, i wtedy tak to wygląda. Nie, że w folderze nadrzędnym jest dziedziczenie, ale jest dodatkowo, że Jan Nowak – wynika z dostępu do plików – czyli on ma tylko "Widoczność folderu", taki tryb uprawnień. No i tego tu się nie da usunąć, nie, bo to już wynika z tego, że niżej ma jakiś obiekt – bo ten obiekt może być i pojedynczym plikiem, i folderem, do którego ma dostęp. Dlatego widzi tutaj folder. I tak samo – jak wejdziemy wyżej – no, to tu też powinno być analogicznie, że Jan Nowak – widoczność folderu – tak, jako tej przestrzeni.

**Piotr Buczkowski:** Wszędzie jest jakoś tak – to właśnie robione, że zupełnie niewidoczność folderu, tak?

**Damian Kaminski:** Go nie da się chyba – a nie, da się go nadać – OK. Da się go też na... No to – to już jest do zastanowienia. Czy jest sens nadawania samej widoczności folderu, czy to powinno być już tylko dziedziczeniem, tak jakby? Bo – no – co z tego, że komuś pokażę folder, jak on nie będzie miał w nim żadnych plików, to tylko może powodować pytania – dlaczego tu widzę, inni widzą, a ja nie widzę. No, ale to już jest, powiedzmy, wtórne pytanie. Czy – czy ty masz jakieś pytania – to tu jest największym wyzwaniem, czy...?

**Piotr Buczkowski:** No i czy trzeba – o, to dobrze zaprogramować.

**Damian Kaminski:** Coś – no właśnie – zaprojektować przede wszystkim. Ja mogę – to znaczy tak – nie mogę, tylko tutaj mam do tego spisane wymagania. Dzisiaj będę nad tym siedział, postaram się to spisać na poziomie takim ogólnym i podzielić. No, to właśnie jest to spisane, chociażby co to jest – czyli widoczność folderu. No, nie wiem – pewnie będę chciał, żebyś rzucił na to okiem, czy – powiedzmy – na poziomie globalnym widzisz jakieś zagrożenia, ryzyka, że czegoś nie zaopiekowałem?

**Piotr Buczkowski:** Tak ci nie powiem, bo to wymaga dużo pracy, dużo czytania, dużo analizy. Jutro nie mam czasu.

**Damian Kaminski:** Mhm. To co, co proponujesz – po prostu, po prostu zaczynamy to robić, tak?

**Piotr Buczkowski:** No tak.

**Damian Kaminski:** Dobra, natomiast co potrzebuję od ciebie, czego ja nie wiem, a zakładam, że to musimy ustalić – jak to będzie fizycznie osadzane, powiedzmy, czy co robimy w ogóle z plikami, czyli jak – opiekujemy – przechowywanie plików? Czy w ramach tych ustawień, które dzisiaj mamy, czy definiujemy pod to jakieś nowe kwestie?

**Piotr Buczkowski:** Tak, znaczy trzeba oddzielną tabelę. To nie może być tak, że – patrzymy tylko. No i oczywiście zawartość pliku przechowujemy zgodnie z ustawieniami.

**Damian Kaminski:** No właśnie – dla tej funkcjonalności.

**Piotr Buczkowski:** No właśnie – pytanie, pytanie, tak, czy – czy w tym samym folderze, które mamy zdefiniowane – przechowywanie plików ze spraw – tylko tam oddzielna struktura, bo tam mamy jakąś strukturę typu "procedury", czy coś?

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Czy tutaj właśnie w strukturze – nawet, nawet tej strukturze folderowej, tak jak tutaj mamy?

**Damian Kaminski:** No właśnie, czy – czy są jakieś ograniczenia, że jak będziemy taką samą strukturę odtwarzać w – nasz – powiedzmy na Windowsie – to czy – jak tu będzie ktoś chciał zrobić 20 zagnieżdżeniem – to czy Windows nam nie zaprotestuje? Czy musimy tutaj takie jakieś...?

**Piotr Buczkowski:** Pytałem. Myśmy – pewnie nie warto, tak – być może. Ale też przydałoby się tak, żeby to jakoś dało się przez człowieka odczytać.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Dla celów diagnostycznych, zarządzania tym.

**Damian Kaminski:** No, to są takie elementy nieujęte w projekcie, a – no – wymagające zaopiekowania i zdefiniowania, jak to zrobić. No, nie wiem, Piotrze – w sensie mam – mam na myśli, że może powinieneś się zastanowić, ewentualnie, nie wiem, przeczytać, jak to robią inni w kontekście takich, takich repozytoriów, i może wtedy złapiesz jakąś inspirację.

**Piotr Buczkowski:** No dobrze – sfery pominęło – wobec się słuchawki rozłączy. Co mówiłeś?

**Damian Kaminski:** Mówię, że niekoniecznie musimy na to odpowiedzieć w tym momencie, ale może – jeśli byś znalazł na to chwilę i, nie wiem, poszukał, jak to robią inni w kontekście tego typu rozwiązań – czy jak właśnie tą strukturę sobie budują, czy odtwarzają to tak, jak jest w aplikacji, czy jednak w jakiś inny sposób – to może złapiesz jakąś inspirację i powiesz, jak to powinno być?

**Piotr Buczkowski:** Znaczy byłbym za tym, żeby struktura była – niepełny nazwy, tylko, powiedzmy, w folderach – podkreślenie – początek nazwy – kilka znaków z nazwy, tak?

**Damian Kaminski:** OK, żeby ścieżka po prostu jak najlepiej.

**Piotr Buczkowski:** Żeby mniej więcej było widać, tak? I żeby była unikalna, unikalna, tak.

**Damian Kaminski:** Mhm, mhm.

**Piotr Buczkowski:** Czy to jest ten sam folder, czy – czy inny folder w stosunku do? Dodałbym oddzielne ustawienie, które jak najbardziej można ustawić na ten sam folder, tylko tam będzie wtedy, powiedzmy, pierwszy folder będzie, że – "Repository", tak.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** "Repozytoria" – później, na przykład, "Dokumentacja" – nie wiem – "Jeden_Dokumentacja_Projektu_Alpha", "Dwa_Zasoby" – tak – "Jeden_Dokumentacja_Projektu..."

**Damian Kaminski:** Rozumiem – powiedzmy 10 znaków bierzemy, tak?

**Piotr Buczkowski:** Tak, tak – albo nie wiem, jakiś – zdefiniować skrót, tak – maksymalnie, że ma gdzieś, że – że w opcjach, tak – ustawieniach – że "Nazwa" – chociaż – skrót nazwy, tak jakby – też w folderze też skrót nazwy, że to jest maksymalnie 10 nazw. Nie, nie, ale to nie ma sensu.

**Damian Kaminski:** Nie ma sensu, bo to będzie – bo jak ktoś ma uprawnienia – ja folderu – bo rozumiem, że tu byś to sugerował – "nazwa to skrót", tak – ale to wtedy to będzie taki miszmasz, że...

**Piotr Buczkowski:** Tak, że... powiedziałem.

**Damian Kaminski:** Nie będą wiedzieli, po co to jest – ci, co to robią – więc...

**Piotr Buczkowski:** Tak, tak. Techniczna rzecz dla zwykłych użytkowników.

**Damian Kaminski:** Mhm.

**Piotr Buczkowski:** Dobrze, że – nawet myślę, że można pominąć, tak – tylko ID, bo tylko...

**Damian Kaminski:** Czy nawet jak damy 5 pierwszych znaków, czy 10 pierwszych znaków, to oczywiście, jeśli...

**Piotr Buczkowski:** To nie – to, bo to – domyślam się, że będzie... 10 – na przykład folderów – tak samo się zaczynających, tak – który – "Dokumentacja projektowa", "Dokumentacja projektu Beta" i tak dalej – kolejnej litery...

**Damian Kaminski:** OK.

**Piotr Buczkowski:** Ksiądz – będziemy mieli wszędzie, wszędzie mieli, będziemy mieli "Dokumentacja" i...

**Damian Kaminski:** Możesz mieć rację. Nic to nie da.

**Piotr Buczkowski:** No tak – nie tutaj fajniej to – pojdzie projekt.

**Damian Kaminski:** Tylko – jeśli mówisz – chyba, że pierwsze litery wyrazów.

**Piotr Buczkowski:** Folder, folder.

**Damian Kaminski:** No, bo jeśli i potem – chcieli, będziemy chcieli coś diagnozować – to co tutaj? Po prostu będziemy klikać sobie, zbada, i będziemy dostawać informacje, jakie to jest ID – na podstawie tego szukamy, tak.

**Piotr Buczkowski:** Ewentualnie żeby to było widoczne w adresie, tak jak...

**Damian Kaminski:** Dla admina tutaj, na przykład, albo dla admina tu.

**Piotr Buczkowski:** Nie, nie, nie, nie – jeszcze klikniesz w "Architektura systemu", to pewnie się zmieni adres, tak, jakoś. I w tym – w adresie – na podstawie tego od razu powinno to być – ścieżka dostępna, tak?

**Damian Kaminski:** OK, że tutaj – tak – i tu będzie jakaś ścieżka.

**Piotr Buczkowski:** Tak, tak.


**Data spotkania:** 13 listopada 2025

---

**Lukasz Bott:** Janusz, czy dla Mateusza Kisiela jest zorganizowane jakieś zastępstwo? Przypomniało mi się to przy okazji poniedziałkowego szkolenia z RODO. Czy ten zespół jest budowany?

**Janusz Bossak:** Nie mamy bezpośredniego zastępcy. Teoretycznie każdy może się tym zająć, bo to nie jest rocket science, trzeba tylko chcieć. Wiedza o tym, na których serwerach co działa, musi zostać upubliczniona, żeby w razie jego nieobecności inni wiedzieli, co robić.

**Lukasz Bott:** No dokładnie, a ostatnio go nie ma ze względu na zajęcia.

**Janusz Bossak:** Wyznaczenie celów sprintu to nasz główny cel. Powinniśmy przejrzeć też bugi, które wpadły i nie zostały jeszcze zakwalifikowane do sprintu.

Będę się upierał przy tym, co wykoncypowałem przez ostatni tydzień dyskusji z AI. Wróćmy do zasad planowania sprintu. Główna zasada: "przestań zaczynać, zacznij kończyć". Po to robimy te "prezenty", czyli paczki, żeby lepiej dowozić. Skończone kodowanie to nie znaczy skończone zadanie. "Skończone" powinno oznaczać przetestowane, zweryfikowane i gotowe do wydania.

Mamy ograniczoną ilość testerek i to jest nasze wąskie gardło. Powinniśmy dawać na sprint tyle MVP, ile mamy testerek. Mamy 9 deweloperów, ale 3 testerki, więc prawdziwy systemowy limit pracy w toku (WIP) dla całego działu wynosi 3, a nie 9.

**Lukasz Bott:** Rozumiem, że WIP na poziomie prezentu, czyli epica?

**Janusz Bossak:** Tak. Prezent to jest epic, coś, co dowozimy, co jest wartościowe dla klienta. Taka paczka powinna być dowieziona maksymalnie w 1-3 sprinty. Kluczowa zasada jest taka, że dany zespół nie ma innego celu niż dowiezienie tej paczki. Nie powinno być wrzutek w trakcie sprintu. Wtedy łatwo jest określić cel.

Przykładowo, celem jest "wprowadzenie podglądu treści szablonów PDF i DOCX z poziomu sprawy". To jest nasz prezent. Pod tym rozpisane są ficzery. Przed daniem tego do zrobienia musimy zdecydować, czy wszystkie te ficzery są do zrobienia w ramach jednej paczki. Jeśli jest za duża, musimy coś jawnie wywalić albo zaplanować na dwa sprinty.

To, co tu pokazuję, to przykłady, które poklasyfikowałem wstecznie. Modernizacja UI sprawy powinna być podzielona na paczki: MVP1 z elementami bazowymi, MVP2 z prawym panelem itd. Powinniśmy mieć backlog rzeczy do zrobienia dla każdego zagadnienia i z tego wybierać.

Celem sprintu nie jest to, że zespół "coś robi", tylko że "kończy" prezent, który był np. w testach. Jak coś nie przeszło, to zespół nie bierze się za nic nowego, dopóki tego nie dokończy. Jednocześnie inny zespół, który swój prezent skończył, może wziąć następny.

**Damian Kaminski:** Rozumiem to tak, że powinienem opisywać w ramach ficzerów konkretne funkcjonalności, a je rozpisywać na PBI backendowe i frontendowe. Ale zastanawiam się nad podejściem. Czy można zrobić PBI "przygotowanie bazy danych", które obejmie wszystkie zmiany w tabelach i kolumnach za jednym zamachem?

**Janusz Bossak:** To może generować niedopatrzenia.

**Damian Kaminski:** Dlatego się zastanawiam. W ramach repozytorium plików trzeba będzie dodać pozycje, wyświetlić drzewko, usunąć. To wymaga zadań backendowych na endpointy i frontendowych na wizualizację. Jak to dobrze ułożyć?

**Janusz Bossak:** Pierwszy poziom to inicjatywa, np. "dostarczenie funkcjonalności repozytorium, aby można było odebrać wdrożenie w WIM". Inicjatywa musi dawać mierzalną wartość. Pod spodem są prezenty, czyli epiki (nasze MVP), a pod nimi ficzery. W ramach MVP najpierw robimy burzę mózgów i tworzymy listę wszystkich funkcjonalności. Potem z tej listy wybieramy, co jest absolutnie niezbędne dla pierwszej paczki, którą dostarczymy, żeby jak najszybciej dostać feedback od użytkownika. Następnie szacujemy, ile sprintów to zajmie. Jeśli jest za duże, dzielimy. Dopiero wtedy, dla ficzerów z najbliższego sprintu, rozpisujemy PBI.

**Lukasz Bott:** Czyli prezent to epic, a pod nim jest wiele ficzerów.

**Janusz Bossak:** Tak.

**Damian Kaminski:** To co Piotr opisał jako wytyczne dla backendu, powinno być rozbite na PBI-e w ramach poszczególnych ficzerów, czy może dodane jako jeden, ogólny opis techniczny do epica? Chciałbym, jako wykonawca, rozumieć, dlaczego coś jest robione w określony sposób, nie widząc całego obrazu.

**Janusz Bossak:** Możemy podpiąć opis architektury od Piotra jako jeden z pierwszych ficzerów w ramach MVP1. Wtedy każdy będzie wiedział, gdzie szukać opisu technicznego.

**Damian Kaminski:** OK, to mi się podoba. To będzie tylko opis techniczny, z którego nie będą tworzone PBI, bo te będą wynikać z konkretnych ficzerów funkcjonalnych.

**Janusz Bossak:** Chyba że trzeba coś konkretnego zrobić w bazie, np. dodać kolumnę. Wtedy to może być normalny ficzer w ramach MVP1. Ale ogólny, architektoniczny opis, który może nie być w pełni zrealizowany w pierwszym MVP, można podpiąć jako osobny ficzer "Architektura".

**Damian Kaminski:** No dobrze, to wróćmy do planowania.

**Janusz Bossak:** Zejdźmy z tych moich pomysłów na ziemię. Z tego, co mamy, trzeba będzie uporządkować wrzutki i przyzwyczaić do tego cały zespół. Przez to, że mamy teraz trochę bałaganu, deweloperzy nie patrzą na to, co jest wyżej, czyli na ficzery, tylko na PBI. A ta metoda, o której mówimy, trochę ich zmusi, żeby robiąc PBI, zajrzeli wyżej i zobaczyli, że to jest kawałek czegoś większego.

**Damian Kaminski:** No tak.

**Janusz Bossak:** Dobrze. Co my tu mamy potencjalnie na następny sprint, czterdziesty siódmy?

Co do strategii, ogólny kierunek to stabilizacja. Ściskamy trochę hamulec, nie dorzucamy nowych funkcjonalności. Kończymy to, co zaczęliśmy: repozytorium, JRWA, ADE. Edytor formularza, diagramu i matrycę uprawnień na razie zostawiamy.

**Lukasz Bott:** A co z JRWA dla LOT-u?

**Janusz Bossak:** Musimy to rozpisać, to ogrom roboty. Powinniśmy się teraz tym zająć, a nie edytorami.

**Lukasz Bott:** Zgadzam się. Poza tym, edytor formularza czy diagramu to nasze wewnętrzne narzędzia. Czy damy je jutro, czy za pół roku, nic się nie stanie. Żaden klient na to nie czeka.

**Janusz Bossak:** Dokładnie. Musimy tu podjąć takie założenia.

**Kamil Dubaniowski:** OK. Proponuję, żebyśmy teraz rozpisali cele na sprint 47. Na pewno robimy repozytorium, ale nie zaangażujemy w to całego zespołu. Co do JRWA, to jest ostatni dzień, żebym mógł cokolwiek zaplanować i przedstawić wam do akceptacji. To ma wpływ na to, jak będzie wyglądał proces u klienta.

**Lukasz Bott:** Kamil, a jesteś w kontakcie z Michałem Wierzbickim, naszym PM-em? Bo on ustala jakieś harmonogramy z LOT-em, są jakieś deadline'y. Żeby się nie okazało, że czegoś nie dostarczymy.

**Janusz Bossak:** Aby dobrze zaimplementować JRWA, potrzebujemy w raporcie typu tabela mieć układ hierarchiczny, tak jak mamy w Gancie. To pozwoli ładnie wyświetlić strukturę JRWA jako drzewko. To jest do zrobienia na rejestrze, bo dla każdego węzła JRWA musimy przechowywać kilka informacji: daty obowiązywania, kategoria archiwalna, uprawnienia.

**Lukasz Bott:** Czyli samo JRWA będzie realizowane jako rejestr, a węzły jako sprawy w tym rejestrze, z relacją nadrzędny-podrzędny?

**Janusz Bossak:** Tak. Żeby ten rejestr ładnie i wygodnie wyświetlić, potrzebujemy tego drzewka.

**Kamil Dubaniowski:** Co do importu/eksportu, to trzeba przygotować wzór dla klienta. Każdy ma jakiś swój, ERP też ma swoją strukturę.

**Damian Kaminski:** Czy JRWA jest definiowane co roku na nowo? Z tego, co wiem, zmiany w kategoryzacji są uchwalane rzadko, przez jakieś wysoko postawione gremium.

**Janusz Bossak:** Generalnie tak, jest na dany rok. Ale istota problemu jest gdzie indziej. JRWA jest krwiobiegiem każdej sprawy. LOT będzie miał hybrydę – 90% dokumentów w papierze, a w AMODIT rejestrowane będzie ich istnienie. Pozostałe 10-15% (korespondencja, wnioski) będą w pełni w AMODIT. To oznacza, że każda sprawa musi być ujęta w JRWA, czyli musi być dla niej założona odpowiednia teczka. Kluczowy jest mechanizm, który pozwala szybko, łatwo i zgodnie z uprawnieniami wyszukać i przypiąć dany dokument do odpowiedniej kategorii JRWA.

**Damian Kaminski:** Czyli nie ma potrzeby eksportowania i importowania struktury co roku. To raczej jednorazowy import, a potem zarządzanie tym w AMODIT, ustawianie dat obowiązywania, tworzenie nowych węzłów.

**Janusz Bossak:** Polecam przeczytanie dokumentów, które przygotowałem na ten temat. Zrobiłem głęboką analizę na podstawie wielu materiałów. Są tam rozpisane dziesiątki przypadków użycia. Dyskutujmy na bazie tych dokumentów.

**Damian Kaminski:** Dobrze.

**Kamil Dubaniowski:** Przejdźmy przez zadania. Trzeba przejrzeć bugi, które wpadły w ciągu ostatnich dwóch tygodni i zdecydować, czy bierzemy je do następnego sprintu.

**Damian Kaminski:** A nie powinniśmy najpierw sprawdzić bugów już przypisanych do tego sprintu?

**Kamil Dubaniowski:** Tak, one powinny być zrobione. Chodzi mi o to, żeby nie robić sobie zaległości na backlogu. Nowe bugi powinny być od razu planowane na najbliższe sprinty, a nieistotne od razu zamykane.

**Lukasz Bott:** A co z tym zgłoszeniem z City Handlowego? Po aktualizacji przestał działać mechanizm przelewów.

**Damian Kaminski:** To jest przypisane do Łukasza.

**Kamil Dubaniowski:** OK. A to z PCBC?

**Damian Kaminski:** Ania się tym zajmowała. Coś mówiła o podsumowaniach. Muszę dopytać.

**Janusz Bossak:** Na trzynastą możemy się umówić w kontekście backendu do repozytorium.

**Damian Kaminski:** OK, wrzucam w kalendarz.

**Janusz Bossak:** Dzięki, to była bardzo konstruktywna rozmowa. Pokazuje, jak powinniśmy pracować nad zgłoszeniem, żeby je dobrze rozpracować, zanim dostanie je deweloper.

**Damian Kaminski:** Dzięki, cześć.
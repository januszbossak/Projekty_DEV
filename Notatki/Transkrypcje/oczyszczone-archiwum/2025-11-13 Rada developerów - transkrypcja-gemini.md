**Data spotkania:** 13 listopada 2025

---

**Lukasz Bott:** Mam pytanie. Sprawdziłem pole typu "podpis standardowy" i realizuje to, co chce LOT, czyli podpis odręczny. Kwestia tylko odpowiedniej konfiguracji. Więc to działa. Inny temat, który chciałem poruszyć z Piotrem Buczkowskim, dotyczy integracji z systemami kadrowymi, gdzie mamy `employeeId`. Jesteśmy w stanie synchronizować ten atrybut do profilu użytkownika w AMODIT, ale nie mamy możliwości użycia go w regułach do przypisywania pól typu "Użytkownik". Możemy użyć adresu e-mail lub loginu, ale fajnie by było, gdyby można było podać `employeeId` z zewnętrznego systemu. Obecnie, gdy przychodzi numer pracownika, musimy robić jakieś dodatkowe mapowanie.

**Damian Kaminski:** Poczekaj, może to jest już obsłużone. Powtórz, proszę.

**Lukasz Bott:** Z zewnętrznego systemu kadrowego przychodzi identyfikator pracownika, który nie jest jego loginem w AD ani e-mailem. Ten atrybut jest synchronizowany do profilu użytkownika w AMODIT. W regule chciałbym przypisać do pola typu "Użytkownik" osobę na podstawie tego właśnie numeru pracowniczego, który ktoś wprowadził na formularzu.

**Damian Kaminski:** OK, rozumiem. Celem jest znalezienie użytkownika AMODIT na podstawie zewnętrznego ID?

**Lukasz Bott:** Dokładnie tak.

**Damian Kaminski:** Ale masz do tego funkcję `FindUserInAD`. Ona to znajdzie, musisz tylko wiedzieć, w którym atrybucie AD to jest.

**Lukasz Bott:** I wtedy zwróci mi login? Dobra, dzięki, podoba mi się.

**Damian Kaminski:** Tak. Jest też alternatywa. W WIM mieliśmy potrzebę mapowania spraw pod użytkowników i dodatkowo potrzebowaliśmy innych atrybutów z AD, które nie były zmapowane. Zrobiliśmy cykliczną synchronizację z AD do lokalnego źródła danych w AMODIT. Raz dziennie pobieramy potrzebne atrybuty i potem z tego odczytujemy.

**Lukasz Bott:** OK, dzięki za podpowiedź, ale myślę, że `FindUserInAD` tutaj zadziała. Trzeba będzie napisać fragment skryptu, ale to jedna-dwie linijki.

**Damian Kaminski:** Tak, tylko obsłuż warunki brzegowe, co się stanie, jak go nie znajdzie, żeby nie było błędu. Funkcja `FindUserInAD` powinna zadziałać, jeśli atrybut jest unikalny.

**Lukasz Bott:** Numer pracowniczy do loginu jest jeden do jednego. Gorzej jest z adresem e-mail, bo ktoś może mieć kilka kont.

**Damian Kaminski:** Aniu, czy zapoznałaś się z nowymi wytycznymi do zgłoszenia o podglądzie szablonów?

**Anna Skupinska:** Nie jestem pewna, czy chcecie podgląd pliku, z którego tworzony jest szablon, czy pliku, który został stworzony na podstawie szablonu.

**Kamil Dubaniowski:** Biznesowo cel jest taki: masz 15 szablonów o nazwach "Umowa 1", "Umowa 2" itd. Musisz podejrzeć, który szablon jest właściwy, zanim go wygenerujesz. Chcesz zobaczyć szablon źródłowy.

**Damian Kaminski:** Aniu, nie XSLT. Chcemy podejrzeć pliki DOCX, PDF, Excel, tak samo jak da się je podejrzeć jako załączniki. Pytanie, co robimy dla szablonów bez podglądu, jak XSLT? Dajemy komunikat?

**Janusz Bossak:** Reagujemy tak samo, jakby ten dokument był podłączony do sprawy. Jeśli się nie da, to komunikat, że nie ma podglądu dla tego dokumentu.

**Kamil Dubaniowski:** Tam powinny być dwie akcje: podgląd i pobranie, żeby wygenerować dokument.

**Anna Skupinska:** Czy w podglądzie mam pokazać treść pliku XSLT, czy wynik jego przetworzenia?

**Damian Kaminski:** Nie, nie wynik. Jeśli chodzi o podgląd, ma to działać dokładnie tak jak dla załączników. Chcemy wyświetlić szablon, bez zmapowanych wartości z formularza.

**Anna Skupinska:** Czy macie dostęp do jakiegoś szablonu PDF, żebym mogła zobaczyć, jak to wygląda?

**Damian Kaminski:** Tak, to jest to. Szablonem może być na przykład regulamin. Pracownik ma oświadczyć, że się z nim zapoznał. Nie chcemy dodawać tego samego pliku jako załącznika do 1000 spraw. Zamiast tego załączamy go raz jako szablon, a pracownik może go podejrzeć, klikając na podgląd. Wtedy w całym systemie jest jeden plik.

**Anna Skupinska:** Rozumiem, czyli to nie jest podgląd wygenerowanego pliku, tylko pliku źródłowego szablonu.

**Damian Kaminski:** Tak. Ten podgląd powinien być generowany raz, w momencie uploadu szablonu, a potem na każdej sprawie wyświetlamy ten sam, statyczny podgląd. Nie ma on kontekstu sprawy.

**Anna Skupinska:** W zgłoszeniu było napisane, że podgląd ma być zapisywany do bazy danych.

**Piotr Buczkowski:** Ma być zapisywany zgodnie z ustawieniem systemowym – albo do bazy, albo na dysk.

**Damian Kaminski:** Ale czy dla szablonów jest sens zapisywać to na dysk? One same są w bazie danych, bo są przenoszone razem z definicją procesu.

**Piotr Buczkowski:** Chcecie podgląd surowego szablonu, czy wypełnionego danymi?

**Damian Kaminski:** Surowego.

**Piotr Buczkowski:** To niech się zapisuje. Generowanie podglądu z DOCX trwa 3-4 sekundy. Bez sensu robić to za każdym razem.

**Janusz Bossak:** Przychyliłbym się do bazy danych. Tych szablonów jest ograniczona ilość, nawet w dużych instalacjach to maksymalnie 100-200.

**Piotr Buczkowski:** OK, może być w bazie.

**Lukasz Bott:** Mamy interfejs do załączania szablonów do definicji procesu i brakuje tam po prostu podglądu tego dokumentu.

**Damian Kaminski:** Zgadzam się. Ale ten interfejs trzeba przepisać na React, nie rozbudowujmy starego. Wtedy tam też dołożymy podgląd. Natomiast w tym zadaniu, na sprawie, ma się wyświetlić podgląd źródłowego pliku szablonu. XSLT nie interpretujemy.

**Janusz Bossak:** Plik XSLT jest plikiem tekstowym. Pytanie, jak traktujemy pliki tekstowe?

**Piotr Buczkowski:** Nie ma dla nich podglądu, bo nie został zrobiony.

**Janusz Bossak:** Dlaczego? To najprostszy podgląd, jaki może być.

**Damian Kaminski:** Pewnie nikt o to nie prosił, bo nikt nie wrzuca plików TXT jako załączników. Głównie to DOCX i PDF.

**Piotr Buczkowski:** Jest podgląd dla HTML, można rozszerzyć to na TXT.

**Damian Kaminski:** Aniu, jeśli wykorzystasz ten sam mechanizm, to jak dołożymy obsługę TXT, to tu też będzie działać. Zrób to spójnie z podglądem załączników.

**Janusz Bossak:** Wracając do XSLT, chodziło mi o to, że gdybyśmy mieli podgląd plików tekstowych, to mielibyśmy też podgląd XSLT – po prostu wyświetliłby się jego kod.

**Damian Kaminski:** Aniu, jak rozumiem, to ma być ta sama funkcjonalność co dla załączników. Gdzie umieścimy ikonę podglądu? Dodałbym ją obok nazwy, żeby nie trzeba było wchodzić w menu z trzema kropkami.

**Janusz Bossak:** A dlaczego nie pod trzema kropkami? Zróbmy tak samo jak przy załącznikach.

**Lukasz Bott:** Dążmy do spójnego interfejsu. Skoro w załącznikach jest pod trzema kropkami, to tu też tak zróbmy.

**Damian Kaminski:** Niby tak, ale tu kontekst jest inny. W załącznikach kliknięcie nazwy otwiera podgląd. Tam trzeba 2 razy kliknąć. Przy 15 szablonach to będzie mniej wygodne.

**Kamil Dubaniowski:** Mamy dwa przypadki. Jeśli to regulamin, ludzie będą się denerwować, że kliknięcie w nazwę go pobiera, a nie wyświetla. Jeśli to umowa, którą już znają, będą się denerwować, że otwiera im się podgląd, a nie od razu pobiera.

**Lukasz Bott:** To trzeba by na poziomie definicji szablonu dać znacznik, czy jest on tylko do podglądu, czy do pobrania.

**Kamil Dubaniowski:** Podgląd z trzech kropek powinien być zawsze. Trzeba się zastanowić, co ma robić kliknięcie w nazwę. Może powinien być specjalny typ szablonu "do podglądu", który po kliknięciu otwiera podgląd, a standardowy "do eksportu" po kliknięciu się pobiera.

**Damian Kaminski:** Podsumowując: może dodajmy w ustawieniach szablonu checkbox "Kliknięcie w nazwę powoduje tylko podgląd". Domyślnie niezaznaczone.

**Kamil Dubaniowski:** Zróbmy MVP: dodajemy opcję "Podgląd" w menu pod trzema kropkami i na razie tyle. Zabezpieczy to sytuację, gdy ktoś musi sprawdzić, co jest w szablonie. Później rozwiniemy to o drugi przypadek, czyli regulaminy.

**Piotr Buczkowski:** Ja bym to zapisał na dysku. Musi być skonfigurowane zapisywanie załączników na dysku. W tabeli będzie tylko znacznik, ile stron ma podgląd, i na tej podstawie będzie można wygenerować ścieżkę do pliku. Jeśli ktoś nie ma skonfigurowanego zapisu na dysku, nie będzie miał podglądu szablonów.

**Lukasz Bott:** A co z chmurą?

**Damian Kaminski:** One są na dysku, w blobie.

**Anna Skupinska:** Czyli nie zapisywać podglądów w bazie danych?

**Piotr Buczkowski:** Nie.

**Damian Kaminski:** A co, gdyby generować podgląd dynamicznie przy każdym wywołaniu?

**Piotr Buczkowski:** To trwa. Dla 10-stronicowego DOCX-a to kilka sekund.

**Janusz Bossak:** Przy dużych plikach musi to być robione przyrostowo.

**Anna Skupinska:** Jako MVP zrobię to w pamięci podręcznej, a później będę pracować nad zapisywaniem. Problem w tym, że istniejące szablony nie będą miały wygenerowanego podglądu.

**Piotr Buczkowski:** Podgląd zawsze generuje się przy użyciu. Jeśli ktoś chce wyświetlić podgląd, a go nie ma, to się generuje. Podglądy i tak są czyszczone po miesiącu od ostatniego użycia, żeby nie zapychać dysku.

**Anna Skupinska:** OK, rozumiem.

**Damian Kaminski:** Dobrze, Aniu, czy teraz wszystko jest jasne?

**Anna Skupinska:** Tak, to spotkanie wszystko wyjaśniło. Mogę zacząć pracować.

**Damian Kaminski:** Sugeruję, żebyś zaczęła od najprostszych i najważniejszych przypadków: PDF i DOCX. Inne typy plików to promil użycia. Nawet jeśli tylko to będzie działać, to już jest duża wartość dodana.

**Lukasz Bott:** Ja już wszystko wiem.

**Damian Kaminski:** To chyba wszystko z tematów na radę.

**Anna Skupinska:** Tomasz Kalinowski chce ze mną porozmawiać, więc ja już skończę. Cześć.

**Damian Kaminski:** Cześć. Piotrze, możesz spojrzeć na to zgłoszenie z Oracle?

**Piotr Buczkowski:** W starych raportach jest specjalna obsługa generowania zapytań dla Oracle. W nowych być może jej brakuje. Trzeba sprawdzić, jak w starym raporcie jest przekazywany `LIMIT` - jako parametr czy wklejany liczbowo w SQL.

**Damian Kaminski:** Czyli w starym raporcie jest funkcja transpilująca zapytanie pod Oracle?

**Piotr Buczkowski:** Tak, dla `LIMIT` jest specjalna konstrukcja. Trzeba przejrzeć cały kod do generowania zapytań dla zewnętrznych źródeł ODBC i dostosować do Oracle dla nowych raportów. Ja to kiedyś zrobiłem dla starych.

**Damian Kaminski:** Dobrze, zapiszę to. Trzeba będzie komuś to przypisać.

**Piotr Buczkowski:** Ale to musi być ktoś, kto będzie mógł pracować z konsultantami Rossmanna, żeby mieć dostęp do ich serwera.

**Damian Kaminski:** Rossmann ma środowisko testowe, więc to nie problem. Programista musi po prostu umieć współpracować z konsultantami.

Kończymy. Janusz, o której dzwonimy w sprawie backendu do repozytorium?

**Janusz Bossak:** O trzynastej możemy.

**Damian Kaminski:** OK, wrzucam w kalendarz.

**Janusz Bossak:** Przypominam się o spotkanie z Przemkiem. A ta rozmowa była bardzo konstruktywna, pokazuje, jak powinniśmy rozpracowywać zgłoszenia. Dzięki.

**Damian Kaminski:** Dzięki, cześć.

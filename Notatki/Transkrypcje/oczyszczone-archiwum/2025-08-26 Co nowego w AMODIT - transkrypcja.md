# Pełna Oczyszczona Transkrypcja Spotkania Projektowego - AMODIT UI

Przemysław Sołdacki

Jeden artykuł o tym, co nowego w AMODIT w nowej wersji, którą za chwilę wydamy. Idziemy po punktach i dyskutujemy. Przejdźmy przez to. Jedźmy po kolei: Copilot. Co to jest ten Copilot? Po co został zrobiony? Co on daje?

Janusz Bossak

Chciałbym powiedzieć szerzej, bo to jest jeden z elementów zastosowania sztucznej inteligencji w AMODIT. Jednym z nich jest Copilot, innym jest funkcja Ask AI, którą można wykorzystywać na poziomie reguł, a jeszcze innym przejawem jest inteligentny OCR. Wszystkie te rzeczy są w tej nowej wersji.

Wracając do AMODIT Copilota – jest on wsparciem dla użytkowników, twórców procesów i ogólnie dla użytkowników AMODIT w różnych obszarach. Można wymienić te obszary.

Pierwsza rzecz: AMODIT Copilot potrafi tworzyć nowe procesy. Na podstawie opisu słownego możemy wygenerować nowy proces. Efektem tego jest szkic procesu – szkic diagramu oraz szkic formularza. Użytkownik może, doprecyzowując swoje wymagania, uzyskać taki efekt, o jaki mu chodzi, czyli gotowy proces z etapami i formularzem. Taki proces może zatwierdzić i dopiero od momentu zatwierdzenia staje się on zrealizowany w AMODIT i możemy go dalej obrabiać i używać według naszego upodobania.

Przemysław Sołdacki

Przy czym trzeba zwrócić uwagę, że powstaje schemat, szkielet tego procesu. Dalej można ten proces rozbudowywać, pisać reguły. Planowane jest w przyszłości, że te reguły też będą się pisały i że Copilot będzie robił bardziej zaawansowaną analizę biznesową. W tej chwili to jeszcze nie jest zrobione, natomiast bardzo dużo rzeczy potrafi w kontekście projektowania.

Damian Kamiński

Można dodać, że to jest wielokrokowe. Powstaje szkic na podstawie pierwszego opisu – wystarczy nam opis biznesowy procesu, czyli założenia, nawet z grubsza do formularza. Resztę AI uzupełnia na podstawie swoich doświadczeń i wiedzy, podpowiada etapy i inne kluczowe elementy. Ważne jest to, że jest to wynik konwersacji, a nie jednego promptu. Można poprawiać na bieżąco, póki jest szkic, i dopiero zatwierdzenie powoduje utworzenie tego procesu.

Przemysław Sołdacki

Dopiero chcemy uruchomić projekt badawczy, gdzie ten Copilot będzie miał jeszcze większą wiedzę, taką "a'la konsultant", gdzie będzie w stanie wcześniej dopytywać, sprawdzić, czy na pewno wszystko jest zrozumiałe, czy specyfikacja procesu jest pełna. Ale to jest pieśń przyszłości. W tej chwili już dużo umie robić.

Janusz Bossak

To jest bardzo ważne. Wróćmy do tworzenia procesu, bo mam feedback od naszych konsultantów. Doceniają w tym nowym sposobie to, że proces jest tworzony "w pełni". Nie tylko są nazwy poszczególnych etapów czy pól, ale też tłumaczenia do tych nazw i opisy. To uwalnia konsultanta od tworzenia wielu dodatkowych elementów czy szczegółów, bo AMODIT Copilot od razu generuje w pełni opisany proces.

Jest jeszcze jedna funkcja Copilota. Ponieważ Copilot zna procesy w AMODIT, możemy zapytać lub poprosić: "Opisz mi biznesowo, jak działa proces obiegu faktur". On na podstawie definicji tego procesu dokona analizy i przedstawi opis biznesowy: po co jest ten proces, jak działa, jakie ma kroki, jakie dane są przyjmowane na których etapach. Całkiem fajny, biznesowy opis procesu możemy uzyskać. To jest druga możliwość: ogólny opis procesu na podstawie definicji.

Kolejne zastosowanie AMODIT Copilota w tej wersji to pomoc w tworzeniu i edytowaniu reguł. Będąc w edycji reguły, możemy poprosić Copilota, aby opracował nam jakąś regułę. Możemy mu zadać temat biznesowy, że chcemy osiągnąć taki a taki efekt, podając przykłady, i on nam opracuje w języku skryptowym AMODIT naszą regułę. Na razie działa to na poziomie pojedynczej reguły, nie analizuje zbiorczo zależności między regułami, ale na poziomie pojedynczej reguły jest w stanie znacznie pomóc. Może też opisać regułę. Jeżeli użytkownik, konsultant czy serwisant wchodzi i patrzy na regułę, która ma 200 linii skryptu i nie bardzo wie, co się w niej dzieje, może zapytać: "Napisz mi, co robi ta reguła". Wtedy dostaniemy pełen opis tego, co ta reguła robi i po co w ogóle jest w systemie.

Kolejne zastosowanie: AMODIT Copilot zna procesy i raporty, jakie są w danym systemie. To jest bardzo użyteczne dla zwykłego użytkownika. Zwykły użytkownik może powiedzieć: "Mam do rozliczenia delegację, którego procesu powinienem użyć?". On przeanalizuje, jakie na tej instalacji są procesy, który z nich służy do rozliczania delegacji, i jest w stanie również uruchomić sprawę od razu w ramach tego procesu.

Podobnie zna raporty. Użytkownik może powiedzieć: "Chciałbym przeanalizować raport sprzedażowy, z którego powinienem skorzystać?". On podpowie, który raport należy użyć, żeby zobaczyć dane, o które użytkownikowi chodzi.

Jest jeszcze warstwa wiedzy o AMODIT. Copilot ma zawartą w sobie praktycznie całą wiedzę dostępną na Wiki AMODIT, czyli naszej pełnej dokumentacji. Dodatkowo ma pełną wiedzę na temat wszystkich funkcji używanych w skryptach, którą bierze z kodu źródłowego AMODIT. Dzięki temu może odpowiadać na ogólne pytania dotyczące systemu.

Przechodzimy teraz do warstwy prywatnej. To, co powiedzieliśmy, to warstwa publiczna (wiedza o AMODIT, funkcjach) oraz lekko prywatna (procesy i raporty na danej instalacji). Nasi klienci mogą w tajemnicy przed światem wrzucać do AMODIT, do nowej funkcjonalności "Baza Wiedzy", swoją wiedzę – regulaminy, instrukcje, opracowania. Klient chce, aby jego pracownicy mogli pytać o to Copilota. Ta wiedza nie wychodzi poza organizację. Użytkownicy mogą zadawać pytania, np. dotyczące regulaminu: "Jak należy zorganizować i zabezpieczyć transport materiałów?". Copilot korzysta z tej bazy.

Przemysław Sołdacki

Pod kątem przykładowych zastosowań: powiedzmy, że jest dział HR i dostaje zapytania od pracowników o różne rzeczy – jak coś załatwić, jak zrobić. Dział HR może sobie zbudować taką bazę wiedzy, żeby ludzie najpierw zadawali pytania do Copilota, a dopiero jak tam nie znajdą odpowiedzi, zgłaszali się bezpośrednio do działu.

Janusz Bossak

Tak, jak najbardziej. Przy czym musimy postawić pewną granicę i klienci muszą to zaakceptować: AMODIT Copilot nie ma dostępu do danych transakcyjnych. Pracownik nie może zapytać: "Ile jeszcze zostało mi urlopu?" albo "Ile muszę rozliczyć zaliczki?". Do tego poziomu danych jeszcze nie mamy dostępu.

Przemysław Sołdacki

W przyszłych wersjach pewnie się to pojawi, będzie włączane per organizacja. Nie każda firma będzie chciała to mieć, to są kwestie polityki bezpieczeństwa. Jeśli klient nie chce, żeby AI miało dostęp do jego danych, to OK, ale jeśli chce, będzie mógł to włączyć.

Janusz Bossak

Po części to jest możliwe nawet teraz. Na poziomie reguł mamy funkcję AddToKnowledgeBase. Możemy sobie wyobrazić, że twórca procesu pewne informacje ze sprawy doda do tej bazy wiedzy. Oczywiście na nim spoczywa odpowiedzialność, co to za dane. Dopóki są to dane np. z zapytania ofertowego czy cennika, to OK. Ale jeżeli to są dane prywatne, to twórca i klient sami odpowiadają za to, co do tej bazy dodają, bo później inny użytkownik Copilota będzie mógł tę informację znaleźć.

Przemysław Sołdacki

Jasne. Ważna jest dla nas kwestia bezpieczeństwa danych, zwłaszcza osobowych. Kolejne funkcjonalności będziemy dodawać. Jeśli klient chciałby jakieś szczególne informacje w tym Copilocie zawrzeć, możemy taki mechanizm uruchomić – wyciąganie danych dla konkretnego użytkownika zgodnie z jego uprawnieniami – ale to jest planowane na przyszłość.

Przejdźmy do kolejnych rzeczy. Nowy wygląd. Zmienia się lista raportów.

Damian Kamiński

Nowy format wyświetlania. Kafelki są bardziej ergonomiczne. Pojawiają się nowe widoki i sposoby prezentacji, czyli prezentacja w formie listy z dodatkowymi metadanymi, które ułatwiają zarządzanie i odnajdywanie raportów. Zwłaszcza z perspektywy administratorów systemu czy procesów będzie to przydatne. Mamy nowy wymiar informacji z perspektywy jednego ekranu. Nowe sposoby sortowania i filtrowania, zapamiętywanie filtrowania w ramach obszarów w menu Raporty.

Przemysław Sołdacki

Jest dużo nowych opcji. Kafelki są ładniejsze i nowocześniejsze, a widok listy jest mocno konfigurowalny – możemy ustalić, jakie kolumny chcemy mieć, jak ma być to sortowane i filtrowane. Wszystko jest zapamiętywane per użytkownik.

Damian Kamiński

Wprowadziliśmy wizualne rozróżnianie raportów poprzez reprezentację każdego typu raportu odpowiednią ikoną, co pozwala szybciej znaleźć dany raport. Nowe sposoby filtrowania: raporty, które ja utworzyłem, czy ktokolwiek inny, ostatnio modyfikowane, określone typy raportów (np. kolumnowy, pivot). Łatwiej to znaleźć niekoniecznie pamiętając nazwę. Pozwala to też uniknąć duplikatów.

Janusz Bossak

Mamy dwa typy list: zwykła i kompaktowa, która pozwala zobaczyć więcej elementów na jednym ekranie. Na liście widać również opisy raportu, więc łatwiej się zorientować, do czego służy.

Kolejna bardzo fajna opcja to szukanie raportu po jego źródle. Szukamy raportów opartych np. o proces "Obieg faktur" albo "Kandydaci". Możemy znaleźć te raporty i zdecydować, z którego skorzystamy.

Podobna sytuacja jest z nową listą procesów. Mamy wydzielone ulubione, potem pozostałe. Jest widok listy kafelkowej oraz listy kompaktowej, gdzie procesy ładnie widać. Po prawej stronie od nazwy procesu może znajdować się opis, co ułatwia orientację.

Damian Kamiński

Odnośnie opisu: wprowadziliśmy nową funkcjonalność "modala pośredniego", który wspiera wdrażanie nowych procesów. Zanim uruchomimy sprawę, dostaniemy informację (jeśli administrator zdefiniuje opis), czego ten proces dotyczy. Można tam zawrzeć dowolną ilość kluczowych informacji merytorycznych. Dopiero po pojawieniu się tego modala możemy uruchomić sprawę.

Janusz Bossak

Chodzi o okienko, które wyskakuje po kliknięciu kafelka. Do tej pory po kliknięciu od razu tworzyła się sprawa. Teraz jest okienko pośrednie z opisem. Mogę zdecydować, że chcę uruchomić, i jednocześnie zaznaczyć, żeby to okienko więcej się nie pokazywało, jeśli proces jest mi znany.

Damian Kamiński

Uwydatniliśmy funkcjonalność opisów również na poziomie raportów. Jest dostępna z poziomu kafelków czy listy. Poza samym tytułem można rozszerzyć informację o to, co taki raport prezentuje.

Janusz Bossak

Dla osób technicznych warto wspomnieć, że te obszary są przepisane na zupełnie nową technologię frontendową – React. Podążamy tą ścieżką i kolejne elementy AMODIT również będą przepisywane na Reacta. Powoduje to łatwiejszą konserwację aplikacji (podział na czysty backend i frontend), łatwiejszą modyfikację elementów frontendowych oraz poprawioną wydajność ładowania list.

Przemysław Sołdacki

Dla biznesu oznacza to, że aplikacja jest ładniejsza i szybciej działa.

Ustawienia systemowe?

Damian Kamiński

Odbiorcami jest ograniczone grono administratorów. Głównym efektem jest przepisanie frontu na nową technologię Reactową. Nie wszystkie ekrany są jeszcze pokryte w tym wydaniu. Te kluczowe poszły w pierwszej kolejności, kolejne będziemy uzupełniać.

Przemysław Sołdacki

Nawigacja po ustawieniach stała się wygodniejsza, łatwiej znaleźć konkretne ustawienie.

Damian Kamiński

Zachowujemy pełną kompatybilność wsteczną. Ponieważ nie wszystko jest pokryte, zawsze można wrócić do poprzedniej wersji.

Janusz Bossak

Administratorowi najpierw wyświetlą się nowe ustawienia Reactowe. Jeżeli jakaś funkcjonalność nie będzie dostępna, w każdej chwili może wrócić do dotychczasowych. Chcemy, aby w pierwszej kolejności korzystano z nowych, a w ciągu następnych dwóch wydań w pełni przejść na wersję Reactową.

Przemysław Sołdacki

Nowe okno logowania.

Damian Kamiński

Odświeżone okno logowania dla użytkowników niekorzystających z SSO (Active Directory). Jest po prostu ładniejsze.

Wprowadzono usprawnienie dla użytkowników posiadających więcej niż jedno konto. Po uwierzytelnieniu przejdą na nowy ekran w formie kafelkowej, gdzie będą mieli zestawione w ładny sposób swoje konta powiązane np. z danym adresem mailowym. Łatwo rozróżnią login, stanowisko, dział.

Janusz Bossak

Już po zalogowaniu, w górnym menu (tam gdzie imię i nazwisko), możemy w łatwy sposób przełączyć się na inne konto. Nie trzeba się wylogowywać całkowicie. Możemy przełączyć się w inny kontekst, np. na konto z innej spółki, innego oddziału czy na inną rolę (między administratorem a użytkownikiem).

Przemysław Sołdacki

W jakich przypadkach to się przydaje? Firmy wielooddziałowe, grupy firm?

Damian Kamiński

Dokładnie. Przypadki wielooddziałowe, zatrudnienie w odrębnych jednostkach. Mogą to być też osoby, które są jednocześnie zaangażowane w procesy biznesowe i są administratorami. Zalecamy, by posiadały dwa odrębne konta. Wtedy wybierają świadomie, z którego konta chcą korzystać.

Przemysław Sołdacki

Przejdźmy do nowego menu po lewej stronie.

Damian Kamiński

Zmianę odczują wszyscy. Menu jest nowe w kontekście wyglądu i ergonomii. Niektóre pozycje zostały, ale jest ładniejsze.

Co się zmienia:

1. Pojawia się okienko wyszukiwania z pozycji menu.
    
2. Zarządzanie obszarami przeniesione na górę (obok wyszukiwania).
    
3. Cały boczny panel menu możemy zwijać, żeby mieć więcej przestrzeni roboczej. Pozostaje dostępny w formie kafelków/ikon.
    

Janusz Bossak

Nastąpiły przetasowania pozycji:

1. Wydzieliliśmy zakładkę "Do wykonania" poza obszary. Klienci potrzebowali przeglądu wszystkich zadań ze wszystkich obszarów. Teraz ta zakładka jest ponad obszarami.
    
2. Przenieśliśmy "Powiadomienia" z górnego paska do lewego menu (pod zakładkę "Do wykonania"). Użytkownicy widzą tam np. wzmianki w komentarzach. Dzięki nowej lokalizacji powinny być bardziej widoczne.
    
3. Podział na: Listy spraw, Przypięte oraz Linki.
    
    - Listy spraw: np. "Mój zespół", "Wszystkie".
        
    - Przypięte: raporty przypięte przez twórcę lub użytkownika.
        
    - Linki: aplikacje zewnętrzne podpięte do AMODIT.
        
    - Moduły: osobna sekcja, np. Nadawca, Przelewy.
        

Damian Kamiński

Zakładka "Do wykonania" na samej górze agreguje wszystkie sprawy przypisane do nas. Wewnątrz obszarów nadal mogą być lokalne zakładki "Do wykonania" filtrujące zadania tylko z tego obszaru.

Przemysław Sołdacki

Nowy wygląd formularza sprawy.

Damian Kamiński

Odświeżenie layoutu, więcej przestrzeni na sam formularz. Menu nawigacyjne po opcjach sprawy zostało przeniesione z góry na prawą pionową belkę. Poprawiliśmy design przycisków – są ujednolicone (białe tło, szara ramka), kolory są tylko na ikonach.

Przemysław Sołdacki

Chodzi o to, żeby mocno kolorowe przyciski nie odwracały uwagi od merytoryki. Najważniejsza jest treść formularza. Mniej jaskrawe przyciski mniej męczą wzrok i nie odwracają uwagi od np. pól wymaganych.

Damian Kamiński

Pola wymagane są oznaczone delikatną pomarańczową linią na dolnej krawędzi. Jeśli użytkownik pominie pole i spróbuje zapisać lub przekazać sprawę, system wyraźnie poinformuje o braku wypełnienia odpowiednim dopiskiem pod polem.

Janusz Bossak

Wygląd jest lżejszy, bardziej delikatny. Lokalizacja paska przycisków jest konfigurowalna per użytkownik. Jeśli ktoś woli mieć przyciski na dole (bo czyta sprawę i na dole podejmuje decyzję), może to zmienić w ustawieniach.

Damian Kamiński

Powiadomienia systemowe do sprawy (powiązane sprawy, niekompletny formularz, priorytety) też zostały poprawione wizualnie i znajdują się na górze pod przyciskami.

Janusz Bossak

Zmienił się wygląd prawego panelu (podgląd dokumentu, lista załączników, informacje o sprawie, diagram, historia). Wszystkie panele zostały przebudowane, są lżejsze i w jednolitej tonacji.

Rozdzielono funkcjonalność uprawnień – jest osobny prawy panel dla właścicieli i obserwatorów. Panel "Informacje o sprawie" zyskał więcej szczegółów: stan sprawy, od kogo przyszła, kiedy, kto modyfikował.

Przemysław Sołdacki

Nowy wygląd tabeli na formularzu sprawy.

Janusz Bossak

Odświeżony wygląd tabeli w tradycyjnym układzie kolumnowym oraz w postaci kafelków. Zmniejszyła się liczba niepotrzebnych elementów, tabela jest czystsza. Zmieniono też wygląd tzw. podformularzy.

Istotna zmiana: możliwość personalizacji nazwy przycisku "Dodaj". Zamiast ogólnego "Dodaj", twórca procesu może wpisać np. "Dodaj nowego członka rodziny". To znacznie zwiększa intuicyjność.

Damian Kamiński

Personalizacja poszła szerzej – analogiczne rozwiązanie jest na poziomie raportów. Można zdefiniować nazwę przycisku tworzenia nowej sprawy, np. "Dodaj nowy wniosek urlopowy" czy "Dodaj nową fakturę".

Zmieniliśmy też miejsce importu danych do tabeli. Jest teraz przy dodawaniu nowych wierszy (menu kontekstowe przy przycisku "Dodaj"), a nie ukryte w "hamburgerze". Można dodać wiele wierszy naraz lub zaimportować wsad z Excela.

Wracając do WCAG. Mamy dwie perspektywy.

Z perspektywy ekranu głównego (i w ustawieniach konta) można włączyć dwie opcje:

1. Tryb wysokiego kontrastu: wyczernienie kluczowych treści (przyciski, podtytuły), obramowanie elementów przy najeżdżaniu (zamiast słabo widocznego podświetlenia). Działa na ekranie głównym i na sprawie.
    
2. Tryb uproszczonego widoku sprawy: zmieniona nawigacja.
    

Przemysław Sołdacki

Uproszczony widok jest ważny dla osób korzystających z czytników ekranowych (VoiceOver itp.). Żeby czytnik mógł opowiedzieć, co jest na ekranie, widok musi być prosty.

Damian Kamiński

Do tej wersji zostanie wydana deklaracja zgodności ze standardem WCAG 2.1 AA.

Poruszanie się po ekranie zostało dostosowane do norm – nawigacja klawiaturą (Tab, Shift+Tab, strzałki) zamiast myszki, pozwalająca na pełne procesowanie formularza.

Janusz Bossak

Opcja jest włączana na poziomie użytkownika. Każdy może sobie włączyć taki tryb, a pozostali mogą korzystać z normalnego wyglądu.

Przemysław Sołdacki

Wróćmy do AI. Co poza Copilotem?

Janusz Bossak

Została dodana funkcja Ask AI. Otwiera ona możliwości korzystania ze sztucznej inteligencji na poziomie pojedynczej sprawy. Twórca procesu może wprowadzić do tej funkcji dowolną informację ze sprawy, np. treść dokumentu.

Przykład u nas: analiza zapytań ofertowych. Przychodzi zapytanie, jest poddawane OCR, a tekst (razem ze specjalnym promptem) trafia do funkcji Ask AI. Uzyskujemy ustrukturyzowaną odpowiedź (kluczowe daty, kwoty) oraz subiektywną ocenę AI – czy zapytanie jest dla nas interesujące.

Inne zastosowania: analiza umów, regulaminów, wstępna analiza CV kandydatów (sprawdzenie zgodności z oczekiwaniami, np. staż pracy, kwalifikacje).

To trochę jak pytanie ChataGPT "masz tu dokument i zrób z nim to", ale dzieje się to automatycznie w procesie.

Przemysław Sołdacki

Jakie modele można użyć?

Janusz Bossak

Możemy korzystać ze wszystkich modeli dostępnych na platformie Microsoft Azure. Ważna informacja o bezpieczeństwie: to nie jest ten sam model co publiczny ChatGPT. Dane są przetwarzane przez Microsoft na terytorium Unii Europejskiej. Microsoft zapewnia, że dane nie są wykorzystywane do trenowania modelu ani przechowywane (poza krótką historią konwersacji).

Dostępne są najnowsze modele GPT-4o, GPT-3.5, wersje mini, nano.

Damian Kamiński

Jesteśmy z automatu zintegrowani, klient nie musi tego opłacać osobno u dostawcy, rozlicza się z nami za użycie. Dajemy pakiet darmowy na start, potem pay-as-you-go.

Janusz Bossak

W bazie wiedzy (funkcja AddToKnowledgeBase) wykorzystujemy modele typu "embedding", które są tańsze i służą do tworzenia bazy wektorowej.

Staramy się iść w stronę "AI Driven Workflow" – wiele elementów AMODIT ma być wspieranych przez AI w sposób świadomy (np. Ask AI na konkretnym kroku).

Przemysław Sołdacki

Parę słów o OCR. Został mocno rozbudowany – AMODIT AI OCR.

Janusz Bossak

To potężne narzędzie w kontekście AI Driven Workflow. Potrzebujemy odczytać dane z faktury czy paragonu. Istnieją modele specjalizowane, ale bywają nieskuteczne. My dorobiliśmy "pre-processing" i "post-processing".

Pre-processing: Wykrywamy typ dokumentu (faktura czy paragon) i używamy odpowiedniego modelu.

Post-processing: Jeśli standardowy OCR nie odczyta jakiejś informacji (np. daty sprzedaży), dopytujemy inny model (np. GPT-4o mini).

Nowa funkcjonalność: Możemy poprosić OCR o odczytanie niestandardowych informacji, których zwykły OCR nie czyta, np. numer VIN samochodu z faktury albo dane z paszportu krowy (dla firm z branży hodowlanej). Jesteśmy w stanie rozczytać taki paszport i wyciągnąć dane do rejestracji zwierzęcia.

Możemy czytać dokumenty kadrowe, umowy.

Możemy korzystać z modeli specjalizowanych (np. do dowodów osobistych, mandatów) lub ogólnych modeli LLM, którym dynamicznie mówimy, co mają odczytać. Modele trenowane są lepsze przy dużej skali (dziesiątki tysięcy dokumentów), ale przy mniejszej skali modele ogólne świetnie sobie radzą.

Przemysław Sołdacki

Dostarczamy e-teczki (elektroniczną dokumentację pracowniczą).

Janusz Bossak

Tak, oferujemy kompleksowe rozwiązanie: e-teczkę z rozczytywaniem i klasyfikacją dokumentów. System na podstawie danych z dokumentu wie, w którym miejscu teczki go zarejestrować.

Przemysław Sołdacki

Obszar raportów – seria usprawnień.

Janusz Bossak

Moduł raportowy jest w nowej technologii. Nowinki:

1. Gradienty kolorów: W raportach typu pivot można ustawić kolory dla wartości (np. najwyższe zielone, najniższe czerwone).
    
2. Filtry użytkownika – Filtry wymagane: Użytkownik nie zobaczy raportu, dopóki nie wybierze wartości w filtrze (np. konkretnego procesu). Zapobiega to szumowi informacyjnemu (wyświetlaniu danych ze wszystkich procesów naraz).
    
3. Filtry z wartością domyślną: Twórca ustawia np. bieżący rok, ale użytkownik może to zmienić.
    
4. Filtr zakresu dat: Można ustawić przedział "od-do" w ramach jednego filtru (wcześniej trzeba było robić dwa osobne).
    
5. Przycisk "Wyczyść filtr użytkownika": Resetuje ustawienia filtrów.
    
6. Przycisk "Zastosuj": Wprowadzony we wszystkich typach filtrów (bardziej intuicyjne dla użytkowników).
    

Usprawnienie podpisywania z poziomu raportów: Jeśli na formularzu jest kilka pól z dokumentami, a na raporcie wyświetlamy je w kolumnach, teraz możemy wskazać, która konkretnie kolumna ma podlegać podpisywaniu (żeby nie podpisywać wszystkich załączników ze sprawy naraz).

Przemysław Sołdacki

Rzeczy techniczne: źródła danych, integracje, REST API.

**Janusz Bossak**

1. Zasilanie danych przez REST API. Do tej pory źródła zewnętrzne zasilaliśmy zapytaniami SQL. Teraz można zasilać źródło danych, wysyłając dane do odpowiedniego endpointu REST API (z aplikacji zewnętrznej).
    
2. `Call Function` (biblioteka funkcji). Do tej pory skrypty `Call Function` były w ramach procesu. Teraz można mieć ogólny skrypt (bibliotekę) poza procesem i używać go w wielu różnych procesach. To samo będzie dotyczyć biblioteki szablonów dokumentów.
    

Janusz Bossak

Edytor formularza.

Przebudowujemy cały obszar definiowania procesu na "ramę Reactową". Pierwszym elementem w tej wersji jest Edytor Formularza.

Zupełnie nowy projekt oparty na feedbacku klientów.

Układ: Po lewej stronie lista typów pól (przenoszenie na formularz). Po kliknięciu na pole na formularzu, po prawej stronie w panelu pojawiają się szczegóły i ustawienia tego pola.

Pełna kompatybilność – żadna funkcjonalność nie została zgubiona.

Użytkownik po wejściu trafi do nowego edytora. Zostawiamy jednak przełącznik na "starą listę pól" dla bezpieczeństwa/wygody, jeśli ktoś czegoś nie znajdzie. Docelowo (za ok. pół roku) stary edytor zostanie wyłączony.

W kolejnych wydaniach: nowy edytor diagramu i reguł.

Przemysław Sołdacki

To wystarczająco dużo informacji. Podsumowanie posłuży do artykułów. Będę potrzebował materiałów graficznych (shoty) oddzielnie.

Janusz Bossak

Dobra, OK.

Przemysław Sołdacki

Dzięki.

**Sprint:** [numer sprintu - do uzupełnienia]
**Okres:** [daty sprintu - do uzupełnienia]



---

## 1. Dolny pasek nawigacji dokumentu



### Cel biznesowy

Klienci upomnieli się o funkcjonalność przełączania dokumentów, którą wcześniej mieli w środkowej części podglądu. Chcieliśmy właściwie z tego zrezygnować, natomiast wyszło, że jednak jest to używane – przełączenie się między kolejnymi dokumentami.

### Co zaimplementowano

- Dolny pasek nawigacji dokumentu z przełączaniem między dokumentami
- Strzałki w lewo/prawo do nawigacji
- Dopóki mamy jeszcze coś po lewej, idziemy do lewej, jak mamy coś po prawej, jedziemy do prawej
- W momencie, kiedy już skończyliśmy całą listę, strzałki w lewo są nieaktywne
- Pliki bez podglądu (np. MKV) nie są wyświetlane na liście i nie są jako poprzedni/następny
- Przycinanie odpowiednio nazw dokumentów
- Formatowanie dolnego paska

### Ograniczenia / Known issues

- Pliki MKV nie są obsługiwane (nie ma podglądu, więc nie są na liście)
- MKV może zawierać wszystkie formaty obrazu i audio i wiele różnych ścieżek, więc byłby bardzo skomplikowany do obsłużenia

### Feedback z demo

- Piotr: "Mamy podglądy do plików wideo, może MKV dodać" – rozważono, ale uznano że nie ma sensu ze względu na złożoność formatu MKV
- Mariusz: "MKV może zawierać tak naprawdę wszystkie formaty obrazu i audio i wiele różnych ścieżek, więc byłby bardzo skomplikowany, żeby go obsłużyć. Prawdopodobnie w 100 procentach byłoby tak, że jedna trzecia pliku będzie działała. Reszta nie"

---

## 2. Podgląd raportu na sprawie



### Cel biznesowy

Poprawiono podgląd raportu, żeby był jednolity z podglądem dokumentów. Jeden ze starszych klientów (Bielia) wnioskował o możliwość przełączania się między raportami z wyszukiwania zaawansowanego (ze 2013 roku), gdzie mieli podglądy luźne na sprawie dodane i z wyszukiwania dało się je podglądać.

### Co zaimplementowano

- Podgląd dokumentów na raportach przybliżony do tego raportu na sprawie
- Paginacja
- Te same akcje co na sprawie
- Widok pełnoekranowy
- Ładowanie kolejnych stron

### Dalsze kroki

- Rozważenie możliwości przełączania się między raportami w kontekście wyszukiwania zaawansowanego
- Odtworzenie funkcjonalności z wyszukiwania zaawansowanego w nowym komponencie Reactowym (obecny jest Reactowy, stary nie był Reactowy)

---

## 3. Sortowanie i funkcjonalności w edytorze formularza (lista pól)



### Cel biznesowy

Wyrównanie funkcjonalności listy pól względem starej wersji. Dodanie funkcji dodawania pola typu Słownik oraz sortowania.

### Co zaimplementowano

- Sortowanie na formularzu, na liście formularzu
- Dodawanie pola typu Słownik z oknem modalnym do budowania pola
- Sortowanie pól sekcji (drag and drop)
- Sortowanie pól po zagnieżdżonych bratnich

### Ograniczenia / Known issues

- Jeszcze nie można przenosić pól między sekcjami (planowane na ten sprint)
- Brakuje szybkiego odnośnika do słownika (nie widzimy jaki to jest Słownik i nie da się szybko do tego słownika przejść) – cel sprintu za 2 tygodnie
- Obsługa błędów przy duplikowaniu nazwy – wpisane do listy zadań (dotyczy zarówno formularza graficznego jak i listy)

### Dalsze kroki

- Przenoszenie pól między sekcjami
- Szybki odnośnik do słownika
- Obsługa błędów przy duplikowaniu nazwy
- Wyrównanie funkcjonalności względem starej listy pól

---

## 4. Repozytorium plików - frontend



### Cel biznesowy

Tworzenie zupełnie nowej funkcjonalności na potrzeby realizacji umowy dla WIM-u. Analogicznie jak zrobiliśmy komunikator, tak samo repozytorium plików, czyli coś, co jest zupełnie nowym podejściem w kontekście obsługi obiektów w AMODIT. Nie powiązanie ze sprawą, to nie sprawa niesie pliki, tylko pliki są totalnie niezależne, tak jak w każdym repozytorium plików.

### Co zaimplementowano

- Zalążek frontendu repozytorium plików (dość mocno zaawansowany w kontekście funkcjonalności)
- Możliwość przeszukiwania drzewa
- Wyrysowywanie drzewa
- Możliwość udostępniania określonych zasobów
- Różne widoki (układ kafelkowy, układ listowy) – spójne z zakładką procesy czy raporty

### Jak to działa (jeśli omówiono)

- Frontend jest już zaawansowany, ale nie ma jeszcze backendu (bardziej w formie zabawkowej)
- Będzie realizowane analogicznie jak komunikator – zewnętrzna aplikacja przy wsparciu Java, żeby przyspieszyć prace
- Piotr przemyślał architekturę – będzie wewnętrzna AMODIT (nie zewnętrzna aplikacja), żeby zrobić powiązania ze sprawami typu: na koniec sprawy podany plik wpinasz do repozytorium albo z repozytorium pobierasz plik do sprawy, czy z pliku z repozytorium startujesz sprawę

### Ograniczenia / Known issues

- Brak backendu – czekamy na wytyczne od Piotra
- Na razie nie działa nigdzie (brak backendu)
- Wymagania sprawiają, że to będzie czymś siemowita, popartą obecne struktury

### Dalsze kroki

- Projektowanie backendu (Piotr)
- Uwzględnienie ścieżki do przechowywania plików per proces (zapotrzebowanie PKF)
- Integracja ze sprawami (nie w MVP, ale w przyszłości):
  - Powiązanie plików ze sprawą
  - Na koniec sprawy podany plik wpinasz do repozytorium
  - Z repozytorium pobierasz plik do sprawy
  - Z pliku z repozytorium startujesz sprawę
- Możliwość pobrania linku do pliku i wstawienia w tekście załączenia linku (na początku)

### Feedback z demo

- Łukasz Bott: "Rozumiem, że przewidujemy jakość funkcjonalność typu, że mamy na sprawie i podłącz plik z repozytorium" – potwierdzone, ale nie w MVP
- Daniel Reszka: "Pliki gdzie będą przechowywane, w bazie czy na dysku?" – na dysku, tak samo jak obecne załączniki, tylko nie przypięte do spraw
- Łukasz Bott: "Uwzględnienie ścieżki do przechowywania plików per proces (zapotrzebowanie PKF)" – Piotr: "OK, sobie jest sens tak skazać, że ścieżkę dla plików repozytorium"

---

## 5. Copilot - eksport plików i dostęp do spraw



### Cel biznesowy

Rozszerzenie funkcjonalności Copilota o możliwość eksportu wyników oraz dostęp do spraw.

### Co zaimplementowano

- Opcja wyeksportowania pliku z wynikami (np. lista procesów związanych z OCR)
- Eksport w formacie Word lub Markdown
- Dostęp do spraw – możliwość wykonywania zapytań do pobrania spraw z filtrem (np. "znajdź mi faktury z OCR FAU3, gdzie nabywca to Sed")
- Przekierowanie do sprawy po zapytaniu (np. "przejdź do drugiej")

### Jak to działa (jeśli omówiono)

- Na razie proof of concept z VIP (wszystkie uprawnienia)
- Docelowo będzie działało przez tworzenie raportów tymczasowych
- Zapytania uwzględniają uprawnienia użytkownika

### Ograniczenia / Known issues

- Na razie działa z VIP (wszystkie uprawnienia)
- Docelowo ma działać inaczej, przez tworzenie raportów tymczasowych

---

## 6. Copilot - podgląd logów OCR



### Cel biznesowy

Umożliwienie podglądu logów z OCR-a bez konieczności wchodzenia przez bazę danych. Wcześniej nie było takich logów i trzeba było przez bazę wchodzić.

### Co zaimplementowano

- Opcja podglądu zdjęcia logów z OCR-a w bilingu
- Możliwość sprawdzenia przez stronę, kto użył albo dlaczego coś nie zadziałało
- Wyświetlanie wyniku OCR (np. widać że S2 używa dalej starego OCR-a, bo jest wynik Azure'owy)

### Feedback z demo

- Łukasz Bott: "Sygnał, nie wiem czy jest zdaniem to dobrze. Jeżeli Jestem zły, jest naszą, nie wiem klientem serwisowym czy coś, to możesz swoich przebić" – rozważenie przepięcia klientów na nowy sposób obsługi OCR
- Daniel Reszka: "Ostatnio przegraliśmy tego, posłuchasz tam jakieś problemy są, to Janek, możecie do ciebie będzie odżywał. Trzeba ustalić, czy to jest na pewno dobry sposób"
- Mateusz: "Ktoś mnie zgłaszał, że brakuje opcji pobrania sobie całego string z OCR do jakiegoś pola, ale okazało się, że tak naprawdę nie jest to potrzebne. Nie chcieli mieć tylko jedną wartość z tego całego stringa, więc robię tego użyć mechanizmu fields"
- Daniel Reszka: "Tam jeszcze czegoś Mateusz brakuje, to Janek będzie wyjaśniał to z Łukaszem, bo tam jakiś kod się jeszcze pobierał, który nie jesteśmy pewni" – plan przepięcia wszystkich na nowy OCR

---

## 7. Baza wiedzy - przepisanie frontendu



### Cel biznesowy

Przepisanie strony bazy wiedzy na nowo, żeby było spójne z design systemem i bezpieczne oraz wydajne. Strona była napisana przez AI bez mocniejszego nadzoru, więc Przemek to przepisywał.

### Co zaimplementowano

- Przepisanie strony bazy wiedzy na React (spójne z design systemem)
- Schemat identyczny jak obszary, słowniki, źródła danych, klucze szyfrujące
- Szablon pod kolejne strony, do której będzie potrzeba na napisanie backendu
- Struktura wszystkich stron jest identyczna

### Jak to działa (jeśli omówiono)

- Strona bazy wiedzy służy do zarządzania wiedzą wewnątrz organizacji, z której później Copilot może korzystać
- Każda firma może prowadzić sobie swoją indywidualną bazę wiedzy
- Dostępne w menu głównym w sekcji "Baza wiedzy"

### Dalsze kroki

- Napisanie backendu dla strony bazy wiedzy
- Przepisanie innych stron w starej technologii (słowniki, obszary) na nowy szablon

---

## 8. Edytor formularza - drag and drop sekcji



### Cel biznesowy

Dodanie funkcjonalności drag and drop sekcji, której nie mieliśmy w starym edytorze, a pojawiła się w nowym edytorze graficznym.

### Co zaimplementowano

- Drag and drop sekcji
- Całość jest zwijana, żeby było łatwiejsze do przesunięcia
- Przenosząc sekcję, całą sekcję przesyłają sobie do góry pola, ponownie się rozwijają w momencie kiedy już puszczam

### Ograniczenia / Known issues

- Szukanie po typie jeszcze nie jest zrobione (cel sprintu)

### Dalsze kroki

- Wyrównanie listy i edytora – będą teraz mocno jeszcze eksploatowane w tym sprincie
- Szukanie po typie
- Wyrównanie funkcjonalności względem starego edytora

---

## 9. API do przekazywania dużych plików



### Cel biznesowy

Pojawiła się potrzeba przekazywania dużych plików z dedykowanego formularza przygotowanego przez Piotra Węgla do AMODIT (kilkuset megowych czy nawet powyżej jednego giga). Do tej pory wgrywanie plików do AMODIT było możliwe, zarówno w ramach sprawy, jak i przez interfejs standardowo, natomiast tam maksymalna wielkość tego pliku była ustawiana w ustawieniach systemowych. Duże pliki powodowały, że serializatory już nie były w stanie obsłużyć przez JSON.

### Co zaimplementowano

- Nowy endpoint do przekazywania dużych plików przez form data (nie poprzez JSON)
- Przekazywanie w inny sposób, nie poprzez JSON, gdzie właśnie duże pliki powodowały, że serializatory już nie były w stanie obsłużyć
- Przekazywanie przez form data do pola typu z plikiem
- Testowane na 500 megabajtach

### Jak to działa (jeśli omówiono)

- Decyzja programisty, czy ma pliki małe (do kilkunastu megabajtów), gdzie możemy spokojnie jako jest serializować, czytamy z Base64, umieścić w JSON i to przejdzie
- Czy ma pliki duże, który nie przejdą przez JSON, musi przesłać właśnie jako form data
- Ograniczenie: tyle ile IIS jest zdefiniowane (to samo ustawienie co było do tej pory)
- Nie przechodzi żadnych serializacji, dodaj salon czy JSON i czy deserializacji JSON już nie, nie powinno być problemów

### Ograniczenia / Known issues

- Wymaga obsługi dwukrotnego wywołania, żeby wczytać utworzyć sprawę powiedzmy i wczytać do niego dokument
- Ograniczenie wielkości pliku: tyle ile IIS jest zdefiniowane (to samo co było do tej pory)

### Feedback z demo

- Daniel Reszka: "Gdzieś by nie przychodził plik, to żebyśmy wiedzieli gdzie szukać, już w przeszłości, że to jest IIS ustawione" – Piotr: "To dokładnie to samo ustawienie co było do tej pory"
- Daniel Reszka: "W ustawieniach systemowych AMODIT tam mamy też PDF maks. Jeszcze coś takiego" – Piotr: "To jest chodzi o obsługę plików. Nie pamiętam. To chodziło o to, że pliki o większym rozmiarze, no nie dało się dajnie obsłużyć. To tylko do tego mechanizmu" (ograniczanie wielkości PDF, ograniczanie liczby kolorów na skanie PDFów)
- Damian: "Będziemy w tym kwartale jest plan, żeby uzupełnić tą dokumentację i właśnie tego typu. Było to jak teraz powinny być wyjaśnione, żebyśmy dobrze sami wszyscy rozumieli, co dany parametr oznacza"

### Dalsze kroki

- Uzupełnienie dokumentacji parametrów w ustawieniach systemowych (plan na kwartał)
- Poprawa opisu parametrów, żeby były zrozumiałe biznesowo

---

## 10. Podgląd oryginalnego maila w logach



### Cel biznesowy

Umożliwienie podglądu oryginalnego maila w logach, żeby serwisowi i testerkom było łatwiej diagnozować problemy z wczytywaniem maili.

### Co zaimplementowano

- Możliwość wybrania maila z logów (wczytany z nocy, jeżeli był w logu, że oryginalny mail)
- Podgląd oryginalnego maila
- Możliwość zaimitowania tego jak działa job, który ładuje maile (wywołanie tej samej metody, która jest wywoływana w jobie)

### Jak to działa (jeśli omówiono)

- Wywołanie dokładnie tej samej metody, która jest wywoływana w jobie
- Nie będzie wykonania (nie będzie dodane do kolejki do wysłania), ale log się odłoży
- Jeśli będzie jakiś błąd przy próbie wczytania, log się odłoży

### Ograniczenia / Known issues

- To nie jest dokładnie to samo co job – to jest tylko za przeczytanie tego maila ręcznie
- Nie będzie wykonania (nie będzie dodane do kolejki do wysłania)

### Feedback z demo

- Daniel Reszka: "To są 2 różne rzeczy. Chyba nie imituje. My tylko właśnie możemy maile zaczytać, bo to jest inaczej robione ręcznie, inaczej z usługi" – Piotr: "Znaczy tak, to tak naprawdę jest robiona ta wywołana dokładnie ta sama metoda, która jest wywoływana w jobie"
- Daniel Reszka: "Czyli log się odłoży load mail wtedy. Jak tak zrobimy?" – Piotr: "Nie, nie, nie wiem, bo to tylko ten plik, to to nie" – po wyjaśnieniu: "No chyba nie będzie OK, ale log się odłoży, tak"

---

## 11. Historia logowania maili



### Cel biznesowy

Potrzeba z WIM-u: historia maili wysłanych do sprawy. W ramach pierwszego MVP będzie to informacja o tym, jakie maile zostały wygenerowane. Jeśli ktoś ma ustawione, że dostaje maile raz dziennie, to jeszcze nie jest potwierdzenie wysłania.

### Co zaimplementowano

- Historia maili wysłanych do sprawy (z poziomu sprawy)
- Informacja o tym, jakie maile zostały wygenerowane
- Wpis będzie dodawany tak jak teraz, ale będzie dodatkowy znacznik, że wysłany
- Jak będzie wpis, nie będzie wysłany, to znaczy, że jest w kolejce

### Ograniczenia / Known issues

- W tej chwili logowane jest dodanie do kolejki do wysłania, jeszcze nie wiem, czy to rzeczywiście zostało wysłane czy nie
- Wersja czerwcowa: będzie zakończone zadanie, będzie nowe zadanie, że dodać oznaczanie, że dany mail został nie tylko dodany do kolejki do wysłania, został wysłany z tej kolejki

### Dalsze kroki

- Uzupełnienie informacji, że ten mail faktycznie już został wysłany (zadanie w tym sprincie)
- Oznaczanie przez joba, skorelowane z ustawieniami użytkownika, tak jak często te maile faktycznie dostaje
- To nie będzie w logach ogólnych, tylko w historii sprawy

### Feedback z demo

- Przemysław Sołdacki: "Kwestia, że w momencie, kiedy się wczytują maile, to jest pod kątem OCR-a, czyli faktury się wczytują i niektóre faktury nie są wczytywane z jakiegoś powodu, że tam jakiś niewłaściwy format PDF czy coś w tym stylu, żeby rejestr, przypadki, które mail się nie wczytał, czy tam?" – Piotr: "W tej chwili jest taki mechanizm, który powoduje, że jest wysyłany mail do wskazanych osób. Czy to jest gdzieś tutaj było?" (ustawienie systemowe "Information on invalid mail to dis adres")
- Przemysław Sołdacki: "Klientowi nie chodzi o to, że się błąd wczyta, to znaczy mail się wczytał, ale z jakimiś błędami, tylko że się w ogóle nie wczytał" – Piotr: "Jeżeli nie udało się spasować maila. Znaczy, po pierwsze musi to dojść do nas, tak? Jeżeli może dojść do skrzynki zdefiniowanej, został pobrany przez LoadMail job, ale z jakiś powodów nie zostały otworzone sprawa. Informacja o tym jest wysyłana do osób. Czytam to na adres mailowy, zdefiniowany w tym miejscu"
- Przemysław Sołdacki: "Biznesowo jest tak, że oni wysłali na przykład 500 maili, czyli 500 faktur i kilka faktur się nie wczytało. Nie wiedzą która i później jest problem, że nie zapłacili faktury, bo nie wiedzieli, że nie weszła i to jest ich główny ból"
- Damian: "Ta informacja, o której dzisiaj Piotr mówi, ona jest od zawsze, ale ona nie jest rozpropagowana wśród wiedzy. Ee bo ja samo nie nie wiedziałem i zakładam, że większość działu i serwisu i wdrożeń o niej nie wie, więc trzeba to pewnie uzupełnić w postaci dokumentacji"
- Przemysław Sołdacki: "Opisy, żeby były to jakieś takie zrozumiałe, że to to chodzi, tak. Biznesowe" – Damian: "To jest plan, żeby się zajmować tym w tym kwartale"
- Przemysław Sołdacki: "To wasko to jest po prostu pilne. Bo klient jest tak powiem, jeśli tego szybko nie rozwiążemy, ten klient będzie chciał odejść, a to są jest dla nas strata finansowa"

---

## 12. TrustCenter - przeniesienie blockchaina do Windows Service



### Cel biznesowy

Rozwiązanie problemów z blockchainem, gdzie aktualnie pojawiają się bloki, które są jakby nie są w łańcuchu, tylko jakby oddzielnie.

### Co zaimplementowano

- Przeniesienie blockchaina z projektu webowego do Windows Service
- Organizowanie przez usługę Windows Service (analogicznie jak w AMODIT)

### Jak to działa (jeśli omówiono)

- Będzie analogiczny mechanizm jak w AMODIT
- Windows Service będzie organizował blockchain

---

## 13. e-Doręczenia - stabilizacja



### Cel biznesowy

Ustabilizowanie problemów z e-Doręczeniami. Teraz klienci już tam były, żadne błędy nie występują.

### Co zaimplementowano

- Stabilizacja e-Doręczeń
- Drobne poprawki backendowe w obszarze formularzy

### Ograniczenia / Known issues

- Problem z raczkowaniem w e-Nadawcy (zamiast w jednym) – temat inny, inna usługa, Adrian ma już pomysł jak to poprawić, przekazał Łukaszowi

### Dalsze kroki

- Poprawa problemu z raczkowaniem w e-Nadawcy

---

## 14. SignApp - macOS, Szafir, nowa aplikacja



### Cel biznesowy

Prace nad SignApp dla macOS z podpisem Szafir oraz przygotowanie nowej aplikacji do podpisywania dokumentów.

### Co zaimplementowano

- Prace nad SignApp dla macOS
- Podpisywanie Szafirem działa już jest skończone (trwają jeszcze testy, przepijemy trwają jeszcze)
- Prace nad nowym wyglądem aplikacji
- Dostaliśmy bardzo szczegółowy projekt wytyczne do aplikacji
- Wybrano technologie MAUI.NET (kontynuacja, następca Xamarina)

### Ograniczenia / Known issues

- Adrian nie ma fizycznie podpisu m Szafir, więc testowanie zleca Kamilowi
- Trwają jeszcze testy podpisywania Szafirem

### Feedback z demo

- Przemysław Sołdacki: "Jeśli ty mówisz, że nie możesz testować m Szafira, ponieważ Szafira i musi tam komuś dawać, to w takich sytuacjach to tam nie ma co czekać, po prostu trzeba ci kupić m Szafira, bo jeśli to ma przyspieszyć ci pracę" – decyzja: Adrian ma załatwić sobie podpis Szafir (firma zapłaci)
- Przemysław Sołdacki: "Słuchajcie, to albo to się online da, albo trzeba będzie podjechać, natomiast jakby. Przekaz ode mnie jest taki, że jakby ja nie mam oporu tutaj mentalnego, żeby zapłacić za wystawienie jakiegoś podpisu, żeby Adrian sobie szybciej testował"
- Kamil: "O ile się nic nie zmieniło to niestety dałem Szafie. Ja trzeba do nich dopiero jechać do centrali jednej z pamiętam, że życzy" – można się potwierdzić online e-bankowością, ale wybrane banki (bardzo ograniczona pula, 5 banków)
- Piotr: "Nie można podpisać się dowodem to co ostatnio wyszło. PM obywatelem, przepraszam"
- Przemysław Sołdacki: "Słuchajcie, to albo to się online da, albo trzeba będzie podjechać, natomiast jakby. Przekaz ode mnie jest taki, że jakby ja nie mam oporu tutaj mentalnego, żeby zapłacić za wystawienie jakiegoś podpisu, żeby Adrian sobie szybciej testował. Jest Adrian, jak potrzebuję, żebyś nie musiał nikogo czekać, to sobie pojedź. Firma zapłaci ci za to, żebyś ten podpis miał i tyle"
- Adrian: "Można iść 3 kupić i nie ma problemu i sobie testuj wszystko. To nie są, nie są pieniądze, nad którymi warto by się było zastanawiać"

### Dalsze kroki

- Załatwienie podpisu Szafir dla Adriana (firma zapłaci)
- Testowanie sytuacji z 2 certyfikatami (zawód PC podpięty do komputera)
- Prace nad nową aplikacją w MAUI.NET
- Rozszerzenie o podpisy PWP (Enigma) w planach

---

## 15. KSeF Connector - rozszerzenie

**Projekt:** `moduly/KSeF-Connector`

### Cel biznesowy

Prace nad rozszerzeniem konektora KSeF oraz przygotowanie do nowej integracji.

### Co zaimplementowano

- Prace nad rozszerzeniem konektora KSeF
- Przygotowanie do nowej integracji z konektorem

### Dalsze kroki

- Zakończenie integracji z nowym konektorem
- Ciekawsze rzeczy za 2 tygodnie do pokazania, jak już ta integracja z nowej integracji z konektorem będzie zakończone i ten wyjdzie nowy

---

## 16. Bezpieczeństwo danych w Copilot i OCR



### Cel biznesowy

💭 Pomysł Przemka dotyczący bezpieczeństwa danych przechowywanych w bazie Copilota i OCR-a. W bazie zaczynamy przechowywać bardzo wrażliwe dane: wszystkie dane odczytane z OCR-a, dane związane z tym, co Copilot zachowuje, mnóstwo danych, które są wrażliwe, mogą być dane osobowe, mogą być jakieś tam tajemnice firm.

### Problem zidentyfikowany

- Dostęp do tej bazy musi być mega chroniony, zarówno jakby żeby ktoś się nie włamał zewnątrz, żeby jak najmniej osób od nas mogło mieć dostęp do tego
- To są ekstremalnie wrażliwe dane, tak jak mamy mocno chronioną bazy w TrustCenter, bo tam ciężko, cokolwiek się z tego, tam wszystko jest szyfrowane i tak dalej, a tutaj wydaje mi się, że tak jakby nie, nie składam, nie przyłożyliśmy wystarczająco dużo uwagi dla tego bezpieczeństwa

### Rozważane rozwiązania

- Szyfrowanie w bazie danych, żeby nie było to zapisane w plain tekście, tylko szyfrowany
- Retencja danych
- Parametr, który by określał retencję
- Każda firma powinna mieć swoim kluczem szyfrowanym
- 💭 Pomysł Przemka: w wielu wypadkach nie będziemy potrzebowali przechowywać tych wszystkich danych, co się z OCR-a roz przeczytało czy co AI odpowiedziało i mogłoby być tak, że to się zapisuje u klienta w jego bazie, bo to zwłaszcza u klientów premisowych ma sens, że to czy mamy u klienta, u nas nie, u nas tylko zostaje oddany billingowe
- Możliwość zachowania tylko nazwy załącznika i CaseID od danego klienta i to jest wystarczające, żeby znaleźć czego to dotyczyło

### Decyzje podjęte

- Zaparkowano temat na razie – trzeba omówić
- Trzeba spełnić 2 rzeczy: z jednej strony bezpieczeństwo (co mówi Przemek), a z drugiej strony rozliczalność w sensie takim, że trzeba wiedzieć i firmy chcą wiedzieć jak działało tam
- Janusz: "Mega ważny temat"

### Dalsze kroki

- Omówienie tematu bezpieczeństwa danych w Copilot i OCR
- Rozważenie szyfrowania danych w bazie
- Rozważenie retencji danych
- Rozważenie przechowywania danych u klienta (dla klientów on-premise)
- Rozważenie zachowania tylko nazwy załącznika i CaseID

---

## 17. Uwagi dodatkowe

### Dokumentacja ustawień systemowych

- Plan na kwartał: uzupełnienie dokumentacji parametrów w ustawieniach systemowych
- Piotr przygotował mechanizm, że można te opisy robić, wbijam luz, tłumaczeniem, tak są opisy do funkcji
- Przemysław Sołdacki: "Opisy, żeby były to jakieś takie zrozumiałe, że to to chodzi, tak. Biznesowe"
- Damian: "To jest plan, żeby się zajmować tym w tym kwartale, bo tutaj nie, nie właśnie na podstawie tego, co stworzył Piotr nie ma już potrzeby angażowania deweloperów, możemy to sami przygotować. To opis"
- Przemysław Sołdacki: "Copilot mógłby mieć do tego dostęp i by powiedział, że coś takiego jest. Czy Copilot czyta te ustawienia systemowe, ale pewnie łatwo zrobić, żeby mógł to czytać"

### Inne prace

- Ania: dużo poprawek błędów, prace nad raportami systemowymi (z Łukaszem), prace nad tłumaczeniami (przerwane na rzecz błędów)
- Łukasz Brocki: tylko jakieś mniejsze poprawki, ponad połowę sprintu nie było
- Damian: współpraca z Anią przy testowaniu funkcjonalności dynamicznych źródeł danych w potrzebach wdrożeniowych, kilka dodatkowych aspektów usprawniających prace wdrożeniowe zostało rozwiązanych


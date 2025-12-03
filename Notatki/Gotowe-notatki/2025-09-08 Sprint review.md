# Sprint Review – 2025-09-08

**Sprint:** [nie podano]
**Okres:** [nie podano]

**Powiązane projekty:**
- `moduly/Edytor-procesow-formularzy` – temat 1
- `moduly/Ustawienia-systemowe` – tematy 2, 3
- `moduly/Copilot-Baza-wiedzy-AI` – temat 8
- `moduly/Modul-raportowy` – temat 5
- `koncepcje/Security-Checklist` – temat 6
- `klienci/WIM` – temat 7
- `moduly/Silnik-regul` – temat 9

---

## 1. Matryca uprawnień

**Projekt:** `moduly/Edytor-procesow-formularzy`

### Cel biznesowy

Usprawnienie zarządzania uprawnieniami pól w formularzach poprzez wprowadzenie globalnego widoku matrycy uprawnień. Dotychczas sprawdzenie uprawnień wymagało przechodzenia przez zakładkę formularza, zaznaczanie pola i edycję uprawnień, co było nieintuicyjne i czasochłonne. Matryca umożliwia szybki przegląd wszystkich uprawnień w jednym miejscu oraz ich wygodną edycję.

### Co zaimplementowano

- Matryca uprawnień grupująca sekcje i pola formularza
- Możliwość minimalizowania sekcji (np. "checkboxy", "sekcja test")
- Każde pole w tabeli jest w swojej sekcji
- Dziedziczenie uprawnień z sekcji z wizualnym oznaczeniem (ikonka dymka z typem)
- Wyświetlanie wyjątków dla użytkowników z pomarańczowym kolorem tła pola
- Możliwość zmiany uprawnień bezpośrednio z matrycy
- Przegląd całego formularza (tabele, podtabele) w jednym widoku
- Planowany widok kompaktowy (bez dopisków obok ikon, tylko ikony z opisami przy najechaniu)

### Jak to działa (jeśli omówiono)

Matryca prezentuje uprawnienia w formie tabeli, gdzie wiersze reprezentują pola/sekcje, a kolumny reprezentują etapy procesu. Skrzyżowanie wiersza i kolumny to uprawnienie na danym etapie dla danego pola/sekcji. Uprawnienia mogą być dziedziczone z sekcji (domyślnie), co jest oznaczone ikonką dymka z typem. Wyjątki dla użytkowników są wizualnie wyróżnione pomarańczowym kolorem.

### Ograniczenia / Known issues

- Ikony akcji (edycja, usuwanie) znajdują się po prawej stronie, co może być nieintuicyjne – rozważane przeniesienie do lewego menu
- Widok kompaktowy jeszcze nie zaimplementowany
- Filtrowanie etapów jeszcze nie działa zgodnie z założeniami (planowane do poprawy)

### Feedback z demo

- Piotr Buczkowski: Ikony akcji powinny być po lewej stronie, nie po prawej (trudno je znaleźć)
- Damian Kaminski: Zgadza się z uwagą Piotra – ikony powinny być przypięte do lewego menu
- Kamil Dubaniowski: Ikony są używane sporadycznie (głównie przez konsultantów do sekcji technicznych), dlatego umieszczono je po prawej
- Łukasz Bott: Dodać wyjaśnienie, że kolumny to nazwy etapów, a skrzyżowanie wiersza i kolumny to uprawnienie na danym etapie dla danego pola/sekcji
- Piotr Buczkowski: Warto przetestować widok na procesie z SIT (duża ilość etapów) – dla testów skomplikowanego formularza
- Janusz Bossak: Planowana opcja wyboru etapów do wyświetlenia (nie zawsze wszystkie) – np. tylko 3 pierwsze etapy lub etapy obsługi dekretacji/akceptacji

### Dalsze kroki

- Rozważenie przeniesienia ikon akcji do lewego menu
- Implementacja widoku kompaktowego
- Poprawa filtrowania etapów
- Testy na procesie z SIT (duża ilość etapów)

---

## 2. Widok jobów

**Projekt:** `moduly/Ustawienia-systemowe`

### Cel biznesowy

Usprawnienie zarządzania i monitorowania jobów systemowych poprzez wprowadzenie czytelnego widoku tabelarycznego pokazującego tylko pracujące joby oraz możliwość filtrowania.

### Co zaimplementowano

- Widok tabelaryczny jobów
- Domyślnie wyświetlane tylko pracujące joby
- Filtrowanie jobów
- Przycisk odświeżania statusu (planowany w prawym górnym rogu, jak na raportach)

### Ograniczenia / Known issues

- Brak przycisku odświeżania statusu – wymagane dodanie (planowane w prawym górnym rogu)
- Ikony akcji (edycja, usuwanie) pojawiają się dopiero po najechaniu na kolumnę z nazwą – rozważane wyświetlanie ich od razu przy najechaniu na wiersz

### Feedback z demo

- Piotr Buczkowski: Potrzebny przycisk odświeżania statusu wszystkich jobów (nie automatycznie, ale ręcznie)
- Damian Kaminski: Dodać przycisk odświeżania obok (w prawym górnym rogu, jak na raportach)
- Kamil Dubaniowski: Ikony akcji powinny być widoczne od razu przy najechaniu na wiersz, nie dopiero po najechaniu na kolumnę z nazwą (uwaga od Janek Pijanowski z prototypu v0)

### Dalsze kroki

- Dodanie przycisku odświeżania statusu w prawym górnym rogu
- Rozważenie zmiany zachowania ikon akcji (wyświetlanie przy najechaniu na wiersz)

---

## 3. Walidacja parametrów integracji

**Projekt:** `moduly/Ustawienia-systemowe`

### Cel biznesowy

Eliminacja błędów podczas konfiguracji parametrów integracji poprzez wprowadzenie walidacji i predefiniowanych wartości. Dotychczas konsultanci ręcznie wprowadzali parametry, co prowadziło do błędów (literówki, złe nazwy techniczne). Walidacja wymusza poprawne wypełnienie wymaganych pól i podpowiada właściwe wartości.

### Co zaimplementowano

- Kategorie parametrów: ogólne, endpoint, inne
- Predefiniowane nazwy parametrów dla kategorii "ogólne" (zgodnie z dokumentacją)
- Automatyczne przypisanie typu w zależności od nazwy (np. "password" → typ hasło, "Authorization Type" → wybór ze zdefiniowanej listy)
- Walidacja nazw parametrów (nie można użyć nazwy z predefiniowanych w kategorii "inne")
- Dla endpointów: wybór nazwy zgodnej z nazwą integracji i endpointu
- Nazwa endpointu zmienia się automatycznie przy zmianie endpointu (nie zapisuje się, tylko pomocniczo)
- Możliwość dodawania innych parametrów z prefiksem (nie można usunąć prefiksu)
- Grupy parametrów (można nie podawać grupy – domyślna grupa)
- Zmiana ikonki dla Przemka (integracje)
- Przycisk "zapisz" wyszarzony dopóki nie ma zmian (na poziomie zakładki)

### Jak to działa (jeśli omówiono)

Grupy parametrów służą do wskazania zakładki, gdzie parametry są rozmieszczone. W ramach jednej integracji może być wiele grup (np. osobne grupy dla POST-a i GET-a), ale wszystkie będą w jednej zakładce. Parametry systemowe integracji systemowej nie mogą być modyfikowane (tylko wartości), nie można zmienić typu istniejącego parametru systemowego ani dodać nowego parametru w grupie parametrów systemowych.

### Ograniczenia / Known issues

- Długość nazwy w tabeli ograniczona do 50 znaków – wymagane zwiększenie (planowane przy okazji implementacji eksportu/importu)
- ExternalREST w nazwie pola może zaciemniać obraz dla użytkownika – rozważone ukrycie (ExternalREST to techniczne oznaczenie w bazie danych)
- Przycisk "nowa" nieintuicyjny (uwaga Piotra Buczkowskiego)
- Brak opisów integracji (planowane opisy dla integracji systemowych)

### Feedback z demo

- Piotr Buczkowski: Grupa jest zależna od integracji – nie rozumie jak działa grupowanie
- Adrian Kotowski: Grupa służy do wskazania zakładki, gdzie parametry są rozmieszczone; można tworzyć wiele grup w ramach jednej integracji dla wygody przeglądania
- Damian Kaminski: Warto rozdzielić parametry dla POST-a i GET-a różnymi grupami, nawet jeśli endpoint jest ten sam
- Janusz Bossak: Rozważyć ukrycie ExternalREST w interfejsie użytkownika (to techniczne oznaczenie, nieistotne dla konsultanta)
- Janusz Bossak: Rozdzielić Integracje AMODIT i Rozszerzenia AMODIT (przejściowo nadal osobne, docelowo jedna lista)
- Kamil Dubaniowski: Panel do ukrywania integracji, z których się nie korzysta (żeby nie zaśmiecać listy)
- Piotr Buczkowski: Przycisk "nowa" nieintuicyjny
- Janusz Bossak: Integracje systemowe (włączyć/wyłączyć, skonfigurować) vs rozszerzenia (dodawane przez konsultantów) – powinny być rozdzielone
- Adrian Kotowski: Integracje systemowe nie są synchronizowane – trzeba dodać wpis w JSONie przy aktualizacji bazy; planowane opisy dla integracji systemowych

### Dalsze kroki

- Zwiększenie długości nazwy w tabeli (przy okazji eksportu/importu)
- Rozważenie ukrycia ExternalREST w interfejsie użytkownika
- Poprawa przycisku "nowa"
- Dodanie opisów dla integracji systemowych
- Implementacja eksportu/importu parametrów

---

## 4. Kolory i gradienty

**Projekt:** `cross-cutting/UI-formularza-sprawy`

### Cel biznesowy

Rozszerzenie możliwości personalizacji wyglądu formularzy poprzez wprowadzenie podstawowych gradientów dla kolorów.

### Co zaimplementowano

- Podstawowe gradienty dla kolorów (testowane, zmergowane)

### Ograniczenia / Known issues

- Brak kolorów dla tablic
- Brak bardziej zaawansowanych gradientów (możliwość wyboru wielu rzeczy) – tylko podstawowe gradienty na bazie postaw

### Feedback z demo

- Janusz Bossak: Na razie zostawiamy tak jak jest, więcej na razie nie będziemy rozwijać (inne tematy priorytetowe, szczególnie klienckie)

### Dalsze kroki

- [Brak dalszych kroków – temat zamknięty na razie]

---

## 5. Kopiowanie i zapisywanie raportów systemowych jako własne

**Projekt:** `moduly/Modul-raportowy`

### Cel biznesowy

Udostępnienie administratorom systemu możliwości skorzystania z raportów systemowych i dostosowania ich pod swoje potrzeby bez konieczności tworzenia raportów od zera. Dotychczas administrator musiał zgłaszać prośbę o modyfikację raportu systemowego lub tworzyć specjalną grupę użytkowników do zarządzania raportami systemowymi.

### Co zaimplementowano

- Możliwość skopiowania raportu systemowego i zapisania jako własny (funkcja "zapisz jako")
- Wymagane utworzenie odpowiedniej grupy użytkowników (wiedza na Wiki)
- Możliwość definiowania wymaganych filtrów (filtr wymagany bez domyślnej wartości → raport się nie wyświetli bez ustawienia filtru)
- Możliwość dodania domyślnej wartości filtru
- Przegląd i redefinicja istniejących raportów systemowych (niektóre jeszcze w starej technologii)
- Usprawnienia wizualne (np. lista użytkowników po lewej stronie – dużo danych, możliwość filtrowania)

### Jak to działa (jeśli omówiono)

Aby edytować raport systemowy, trzeba stworzyć specjalną grupę użytkowników do zarządzania raportami systemowymi. Wtedy te raporty systemowe dla tych użytkowników są możliwe do edycji, skopiowania i powielenia. Funkcja "zapisz jako" pozwala zapisać raport pod własną nazwą jako nowy twór, w którym zespół nie będzie ingerował i który pozostanie w definicji zdefiniowanej przez administratora. Nie zalecana jest edycja raportów z IDkami/nazwami systemowymi, bo one będą modyfikowane przez zespół w ramach update'u. Źródła systemowe pozostają w trybie do odczytu (nie można zmieniać zapytań), ale można ich używać do własnych raportów.

### Ograniczenia / Known issues

- Niektóre raporty systemowe jeszcze w starej technologii – wymagają przeglądu i ewentualnej redefinicji
- Niektóre raporty mogą być nieczytelne przy zbyt dużej ilości informacji – wymagane usprawnienia

### Feedback z demo

- Anna Skupinska: Raport będzie zmieniony tak długo jak się nie zrobi update bazy danych (poprawka: jeśli "zapisz jako", to będzie stworzony nowy)
- Piotr Buczkowski: Nie można zmieniać zapytań (tylko konfiguracja z poziomu interfejsu)

### Dalsze kroki

- Przegląd i redefinicja raportów systemowych w starej technologii
- Dalsze usprawnienia wizualne i czytelności

---

## 6. Security Checklist

**Projekt:** `koncepcje/Security-Checklist`

### Cel biznesowy

Przygotowanie checklisty bezpieczeństwa (hardening) dla serwerów klientów z instalacją on-premise. Checklista będzie podlegała potwierdzeniu przez konsultanta i klienta, aby później przy pen testach klienta można było zweryfikować, że zabezpieczenia zostały wykonane zgodnie z wytycznymi.

### Co zaimplementowano

- Lista Security Checklist (wstępnie omówiona z Danielem Reszką)
- Planowane przekazanie do klientów, którzy sami wykonują testy bezpieczeństwa

### Jak to działa (jeśli omówiono)

Checklista dotyczy głównie klientów z instalacją on-premise. Serwery tych klientów muszą być skonfigurowane zgodnie z wytycznymi bezpieczeństwa (hardening/tuning). Checklista będzie podlegała potwierdzeniu przez konsultanta (który skonfiguruje) i przez klienta. Celem jest uniknięcie sytuacji, gdy klient robi pen testy na niezabezpieczonym systemie, a zespół był świadomy, że można było zabezpieczyć.

### Dalsze kroki

- Finalizacja listy Security Checklist
- Przekazanie do klientów wykonujących testy bezpieczeństwa

---

## 7. Logowanie wysyłanych maili ze sprawy

**Projekt:** `klienci/WIM`

### Cel biznesowy

Rozszerzenie mechanizmu logowania aktywności użytkownika o możliwość rejestrowania wysyłanych maili ze sprawy w historii sprawy/zdarzeniach sprawy. Dotyczy to głównie klienta WIM.

### Co zaimplementowano

- Logowanie wysyłanych maili ze sprawy w historii sprawy/zdarzeniach sprawy
- Rozszerzony mechanizm logowania aktywności użytkownika z 3 nowymi opcjami:
  - Logowanie maili (włączyć/wyłączyć)
  - Logowanie treści maili (włączyć/wyłączyć) – względy pojemnościowe
  - Logowanie załączników (włączyć/wyłączyć) – względy pojemnościowe
- Jeśli treść nie jest logowana: tylko nazwa załącznika (jeśli załącznik był pobrany ze sprawy, można zobaczyć że został wysłany)
- Jeśli oba włączone: w szczegółach maila jest treść, są załączniki (można pobrać)
- Logowanie maili wysłanych przez SendMessage (regex)
- Informacja o uprawnieniach użytkownika przy każdym zdarzeniu (dlaczego mógł wykonać akcję)
- Obsługa maili odroczonych (user systemowy wysyła)

### Ograniczenia / Known issues

- Informacja o uprawnieniach może być myląca w niektórych przypadkach (np. gdy użytkownik został dodany do sprawy i wysłał mail)

### Feedback z demo

- Łukasz Bott: Dodać link do sprawy w temacie maila (sugestia, ale dotyczy kontekstu sprawy, więc może nie być potrzebne)
- Damian Kaminski: Wyjaśnić informację o uprawnieniach (dotyczy użytkownika, który wykonał akcję)

### Dalsze kroki

- [Brak konkretnych dalszych kroków]

---

## 8. Generowanie procesu przez Copilota z trybem konsultacyjnym

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`

### Cel biznesowy

Przekształcenie Copilota z narzędzia wykonującego polecenia w konsultanta, który potrafi dopytywać użytkownika o szczegóły potrzebne do stworzenia procesu. Dotychczas użytkownik wpisywał polecenie (np. "chcę proces zakupowy"), a Copilot bezdusznie tworzył proces. Teraz Copilot prowadzi rozmowę, zadając pytania i zbierając wymagania przed generowaniem procesu.

### Co zaimplementowano

- Tryb konsultacyjny Copilota zbierający instrukcje i pobierający instrukcje do zbierania wymagań
- Prompt zawierający ~20 kluczowych pytań dla analityka (np. kto bierze udział w procesie, jakie są główne kroki)
- Możliwość odpowiadania na pytania pojedynczo (Copilot dopytywał dalej)
- Możliwość napisania "zaproponuj coś" lub wrzucenia listy wymagań z dokumentu
- Po zebraniu informacji: możliwość napisania "wygeneruj" → Copilot pyta czy proces jest odpowiedni, czy przejść do technicznego projektowania
- Przekierowanie do generowania procesu (strona z podglądem)
- Generowanie podsumowania czatu przez AI (na podstawie czatu generuje podsumowanie procesu)
- Sprawdzanie uprawnień (tylko administrator może definiować nowy proces)
- Mechanizm sprawdzania statusu generowania (odpytuje co jakiś czas, czy już się zakończyło) – rozwiązanie problemu timeout na gateway w chmurze
- Prompt przeniesiony po stronie mikroserwisu (bez aktualizacji AMODITa można go zmieniać)

### Jak to działa (jeśli omówiono)

Copilot używa jednego długiego promptu do generowania całego JSONa reprezentującego proces. Nie można tego zrównoleglić, bo potrzebne są pełne informacje. Mechanizm sprawdzania statusu działa przez odpytanie co jakiś czas, czy generowanie się zakończyło (rozwiązanie problemu timeout na gateway w chmurze). Generowanie trwa długo, bo model myśli (serwery Microsoftu pracują, nie nasze).

### Ograniczenia / Known issues

- Generowanie trwa długo (model myśli) – wymagane atrakcyjniejsze oczekiwanie (spinner z losowymi komunikatami typu "pracuje nad formularzem", "pracuje nad diagramem", "dodaje kolejne etapy")
- Przy kliknięciu "utwórz nowy proces" jeszcze pokazuje się stary wygląd (powinien pokazywać Copilota na starcie)
- Przycisk "Switch To Process" wygląda jak wywołanie JavaScript (nazwa techniczna funkcji) – wymagane ukrycie lub tłumaczenie na nazwę biznesową
- Copilot może nie rozumieć niektórych słów (np. "gity" – sprawdzane)

### Feedback z demo

- Piotr Buczkowski: Można dodać listę propozycji pytań na początku ("wygeneruj proces podaj nazwę"), żeby ludzie wiedzieli od czego zacząć
- Mateusz Kisiel: Zazwyczaj będzie wrzucana lista wymagań z dokumentu Wordowego (jak mówił Przemek)
- Janusz Bossak: Cel to konsultacyjny Copilot – dopytywanie o szczegóły procesu (kto uruchamia, dla kogo, ilu użytkowników, jak działa)
- Janusz Bossak: W normalnych czatach AI pytają po jednym pytaniu (rozważenie zmiany promptu)
- Piotr Buczkowski: Zrozumiało słówko "gity"? (sprawdzane)
- Janusz Bossak: Bardzo fajna rzecz upraszczająca wdrożenia i ułatwiająca konsultantom oraz klientom tworzenie sensownych procesów

### Dalsze kroki

- Atrakcyjniejsze oczekiwanie podczas generowania (spinner z losowymi komunikatami)
- Pokazywanie Copilota na starcie przy "utwórz nowy proces"
- Ukrycie lub tłumaczenie przycisku "Switch To Process" na nazwę biznesową
- Rozważenie zmiany promptu (pytania po jednym, jak w normalnych czatach AI)
- Weryfikacja rozumienia różnych słów przez Copilota

---

## 9. ForEachAttachment – iteracja po załącznikach w sprawie

**Projekt:** `moduly/Silnik-regul`

### Cel biznesowy

Umożliwienie operacji na plikach swobodnie dołączonych do sprawy (lista plików w sprawie) z poziomu reguł. Dotychczas były funkcje do operacji na plikach dołączonych do pola typu dokument, ale brakowało możliwości dla plików załączonych swobodnie do sprawy. To ułatwia pracę konsultantom, którzy musieli wcześniej tworzyć tabele plików.

### Co zaimplementowano

- Konstrukcja językowa silnika reguł `ForEachAttachment` – dodatkowa pętla umożliwiająca iterację po liście swobodnie dołączonych plików
- Dostępne parametry: ID, Tag, TagBody, Value (jak w GetExcelData)
- Value pobierane dopiero na żądanie (optymalizacja) – dopóki się nie pobierze Value, nie zwraca, nie odwołuje się do bazy danych
- Jeśli dodajemy dokument do listy, automatycznie pobiera Value
- Możliwość sprawdzenia: jakie pliki, kto modyfikował ostatnio, rozmiary wszystkich plików, stan OCR, kiedy były zmodyfikowane
- Przykład użycia: lista plików PDF dodawana do listy, dla wszystkich plików zapisywanie nazwy, możliwość mergowania PDF-ów

### Jak to działa (jeśli omówiono)

ForEachAttachment działa podobnie do ForEachObject – odwołujemy się przez "this.coś" (np. this.Id, this.Name). Value jest pobierane dopiero na żądanie (optymalizacja), chyba że dodajemy dokument do listy (wtedy automatycznie pobiera Value). Jeśli są dwa takie same załączniki o tej samej nazwie, nie będzie błędu (ID będzie inny, nazwa taka sama).

### Ograniczenia / Known issues

- W przykładzie w dokumentacji nie ma przypadku użycia "this" bez parametru (tylko this.Id, this.Name) – wymagane dopisanie
- W przypadku dwóch załączników o tej samej nazwie warto odwoływać się poprzez ID (this.Id), nie przez nazwę

### Feedback z demo

- Janusz Bossak: Jak drugi raz puścisz zmergowany PDF, będzie też zmergowany (poprawka: zmergowany dokument dodany do pola, nie jest w załącznikach)
- Piotr Buczkowski: AddToList nie wystarczy "this"? (odpowiedź: nie, z 2 powodów – powodowałoby tworzenie zmiennych zbyt dużych, problem z modyfikacją mechanizmu pobierania Value dla FileContent)
- Piotr Buczkowski: W przykładzie brakuje przypadku użycia "this" (this.Id, this.Name)
- Daniel Reszka: Czy ID jesteśmy w stanie wydobyć? (tak, this.Id)
- Damian Kaminski: W przykładzie w dokumentacji nie ma przypadku użycia "this" bez parametru – wymagane dopisanie
- Piotr Buczkowski: Docelowo trzeba zrobić, żeby można było też podać "this", ale w pierwszej wersji będzie tylko this.Id, this.Name

### Dalsze kroki

- Dopisanie przypadku użycia "this" w przykładzie w dokumentacji
- Rozważenie możliwości użycia "this" bez parametru w przyszłych wersjach
- Przekazanie informacji o funkcji do WIM (korzystają z tego)

---


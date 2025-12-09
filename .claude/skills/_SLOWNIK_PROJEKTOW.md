# Słownik Projektów AMODIT

  

**KRYTYCZNE:** To jest **jedyne źródło prawdy** dla nazw projektów. Używaj TYLKO projektów z tej listy.

  

**ZAKAZ ZGADYWANIA:** Jeśli temat nie pasuje do żadnego projektu z listy → oznacz jako **"Nowy temat / do sklasyfikowania"**

  

---

  

## Moduły (`Moduly/`)

### `Moduly/Repozytorium-spraw`

Repozytorium to hierarchiczna struktura folderów ściśle powiązana ze strukturą organizacyjną firmy, służąca do logicznego grupowania i przechowywania spraw  pochodzących z różnych procesów. Funkcjonalność ta pozwala mapować dynamiczne instancje procesów na statyczne węzły (działy i foldery), dziedzicząc przy tym uprawnienia w dół struktury organizacyjnej. 

### `Moduly/AMODIT Copilot`

Asystent AI dla twórców procesów jak i dla uzytkowników systemu AMODIT. Ma wiedzę o AMODIT, o procesach i raportch zaimplementowanych w AMODIT. Ma tez "Baza wiedzy" typu RAG opartą o dane wprowadzane przez uzytkowników. Zarządzanie kontekstem, źródłami wiedzy, integracja z AI. Obsługa dokumentów przez Copilot (pliki, opisy raportów, reguł). Wspiera generowanie procesów, skryptów regul bizneoswych.

### `Moduly/AMODIT AI OCR`

Dla modułu AI — jeśli podczas automatycznej klasyfikacji  wykryjesz dokument lub zadanie związane z przetwarzaniem faktycznego dokumentu (skan, PDF, zdjęcie itp.) — traktuj je, jako należące do projektu AMODIT AI OCR.

AMODIT AI OCR to system, który automatycznie: rozpoznaje tekst ze skanów/zdjęć/PDF-ów, wyciąga kluczowe informacje (np. dane faktury, paragony, dokumentów kadrowych), a także — w razie potrzeby — stosuje modele AI do dalszej analizy dokumentu (ekstrakcja danych, streszczenie, analiza umów itp.).  ￼

Dlatego wszystkie zadania typu „przetwarzanie dokumentów”, „parsowanie faktury/paragonu/umowy”, „ekstrakcja danych z dokumentu” lub „OCR + analiza dokumentu” powinny być klasyfikowane pod projekt AMODIT AI OCR.

### `Moduly/e-Doreczenia`

e-Doręczenia to projekt integracji AMODIT z systemem e-Doręczeń Poczty Polskiej, który umożliwia przedsiębiorcom i instytucjom publicznym spełnienie obowiązku prawnego obsługi elektronicznych doręczeń. Celem jest zapewnienie pełnej, stabilnej integracji działającej na wszystkich środowiskach (on-premise i chmura), która automatyzuje odbieranie i wysyłanie dokumentów urzędowych bez konieczności ręcznej interwencji. Projekt zakłada budowę niezawodnej integracji z API e-Doręczeń, odpornej na problemy konfiguracyjne i sieciowe.

  

### `Moduly/e-Nadawca`

e-Nadawca to projekt integracji AMODIT z systemem e-Nadawca Poczty Polskiej, który automatyzuje proces nadawania przesyłek pocztowych bezpośrednio z systemu workflow. Celem jest zapewnienie stabilnej integracji z API e-Nadawca, umożliwiającej automatyczne generowanie i rejestrację przesyłek bez konieczności ręcznego wprowadzania danych w systemie Poczty Polskiej.

  

### `Moduly/Edytor-procesow`

Zintegrowany edytor procesów biznesowych w systemie AMODIT. Definiowanie pelnej logiki procesów, na którą skladaja sie etapy (diagram), formularz, reguly, szablony i wiele innych.

  

#### `Moduly/Edytor-procesow/Edytor-diagramu`

Edytor wizualny diagramu procesu. Modelowanie przepływu pracy, wizualizacja etapów i przejść.

#### `Moduly/Edytor-procesow/Tworzenie-spraw`

Ustawienia procesu w zakresie tworzenia spraw z maila, z pliku, dzielenia dokumentu po barkodzie, pustej stronie itp.

#### `Moduly/Edytor-procesow/Edytor-formularzy`

Edytor formularzy dla procesów. Definiowanie sekcji, pól formularza, walidacji. Lista pól formularza.

#### `Moduly/Edytor-procesow/Edytor-reguł`

Edytor reguł, lista reguł dla procesów. 


#### `Moduly/Edytor-procesow/Edytor-szablonow`

Edytor szablonów dokumentów. Tworzenie i zarządzanie szablonami generowanych dokumentów.

  

#### `Moduly/Edytor-procesow/Matryca-uprawnien`

Zunifikowane narzędzie do zarządzania wszystkimi typami uprawnień w edytorze procesów. Dedykowany widok w React prezentujący interaktywną matrycę: (1) uprawnienia do pól formularza - pola vs etapy, kontrola widoczności i edytowalności; (2) uprawnienia do procesów - role, dostępy, macierz uprawnień dla całych procesów. Masowa edycja, filtry, widok wyjątków, dziedziczenie uprawnień.

  

### `Moduly/Eksport-import-definicji-procesow`

Eksport i import procesów w formacie XML. Walidacja definicji, rozwiązywanie konfliktów GUID, migracja procesów między środowiskami.

### `Moduly/Panel-klienta`

Miejsce w którym klient (administrator u klienta) moze sledzic stan zuzytych tokenow, wyslanych dokumentow do OCR, liczbe dokumentow wysłanych do TrustCenter itp

### `Moduly/Modul-raportowy`

Nowy moduł raportowy. Definiowanie raportów, źródła danych, SQL queries, wizualizacje. Logowanie błędów SQL, debugowanie raportów.

#### `Moduly/Modul-raportowy/Wydajnosc`

Wszystkie kwestie dodtyczacace poparwy wydajnosci dzialania raportow takie jak indeksowanie, optymalizacja zapytan SQL itp

#### `Moduly/Modul-raportowy/Filtry-uzytkownika`

Filtry dostepne dla uzytkownikow raportu. Obejmuje tez konfigurowanie tych filtrow przez tworce raportu. Definiowanie i zarządzanie filtrami danych w raportach.

  

#### `Moduly/Modul-raportowy/Gantt`

Moduł Gantt w raportach – daje widok wykresu Gantta do wizualizacji spraw/projektów na osi czasu i zarządzania zadaniami przez drag&drop. Można zobaczyć zależności między zadaniami i przesuwać je na timeline. Hierarchię spraw da się budować na dwa sposoby: klasycznie przez pole parent-child (odnośnik do sprawy nadrzędnej) albo pokazując wielopoziomowe zagłębienie na podstawie różnych pól ze sprawy, które się wybiera do hierarchii. Chodzi o elastyczne planowanie i przegląd relacji zadań/projektów w raporcie.

  

#### `Moduly/Modul-raportowy/Kanban`

Rozbudowany Kanban, który może funkcjonować zarówno jako tradycyjny board (przepływ etapów), jak i dwuosiowa matryca. Pozwala wizualizować i zarządzać sprawami w układzie, gdzie obie osie (pionowa i pozioma) mogą być dowolnie konfigurowane – np. jeden wymiar to projekty, drugi to uczestnicy, typy spraw, priorytety lub inne wybrane kryteria. Umożliwia to planowanie, analizę przepływu pracy i zasobów, zmiany stanów oraz szybkie przesuwanie elementów pomiędzy grupami lub etapami.

  

#### `Moduly/Modul-raportowy/Pivot`

Raport typu Pivot – elastyczna analiza i agregacja danych w formie tabeli przestawnej. Umożliwia różne formy prezentacji, w tym wizualizację jako mapa cieplna (heatmap), pozwalając zobaczyć natężenie wartości na przecięciu wymiarów raportu. Heatmapa jest jedną z opcji prezentacji w ramach raportu Pivot, a nie samodzielnym typem raportu.

  

#### `Moduly/Modul-raportowy/Kolorowanie-raportow`

Kolorowanie wierszy i komórek w raportach. Warunkowe formatowanie, reguły kolorowania.

  

#### `Moduly/Modul-raportowy/Masowe-podpisywanie`

Masowe podpisywanie dokumentów z raportów. Operacje zbiorcze na dokumentach. Obecnie podpisywanie odbywa się przy użyciu podpisu kwalifikowanego, ale planowana jest rozbudowa o możliwość podpisywania „zwykłym" polem podpis, które jest dostępne na formularzu sprawy.

  

#### `Moduly/Modul-raportowy/Masowe-akcje`

Możliwość wywoływania ręcznych reguł jednocześnie dla wielu wybranych spraw w raporcie. Użytkownik zaznacza sprawy i zbiorczo uruchamia na nich wybraną akcję – oszczędza to czas i upraszcza masowe operacje.

  

#### `Moduly/Modul-raportowy/Tlumaczenia-i-aliasy`

Tłumaczenia i aliasy w raportach. Wielojęzyczność, nazewnictwo kolumn.

  

### `Moduly/Modul-raportowy-stary`

Stary moduł raportowy (legacy). Utrzymanie i migracja do nowego modułu.

  

### `Moduly/Raporty-systemowe`

Próba zapewnienia w AMODIT zestawu „standardowych" raportów opartych o dane systemowe, dostępnych dla wszystkich użytkowników bez konieczności własnego definiowania. Chodzi np. o raporty pokazujące liczbę otwartych spraw, liczbę spraw utworzonych w ostatnim tygodniu/miesiącu, średni czas przetwarzania sprawy i tym podobne podstawowe statystyki. Celem jest szybki dostęp do kluczowych wskaźników bez konieczności manualnej konfiguracji.

  

### `Moduly/Silnik-regul`

Absolutnie kluczowy element systemu AMODIT. To właśnie na bazie skryptów realizowana jest cała logika biznesowa procesów. Silnik reguł oparty jest o własny język z określoną składnią oraz zestawem ponad 350 specjalnych funkcji, które umożliwiają realizację szerokiego wachlarza scenariuszy automatyzacji. Język ten jest stale rozwijany – regularnie dodawane są nowe dedykowane funkcje, istniejące funkcje otrzymują dodatkowe parametry lub warianty (np. z dopiskiem Ex). Intensywny rozwój odpowiada na bieżące potrzeby klientów i zmiany w architekturze systemu.

### `Moduly/CallRest`

CallRest to funkcja silnika regul, ale to bardzo istotna funkcjonalnosc z ktora wiaze sie wiele aspektow jak autoryzacja, konfiguracja w ustawieniach systemowych.

### `Moduly/Slowniki`

Obsługa słowników. Słowniki wewnętrzne, zewnętrzne, hierarchiczne, zagnieżdżone. Edge case'y dla słowników zagnieżdżonych.


### `Moduly/Proces-rejestr`

Rejestr to specjalny typ procesu o specjalnych uprawnieniach dla uzytkownikow, i odmiennej widocznosci spraw na listach. Rejestry to w pewnym sensie rozbudowane slowniki, ale oparte o sprawy w AMODIT.


### `Moduly/Trust-Center`

TrustCenter to praktycznie odrębna usługa wystawiona w sieci, z którą AMODIT integruje się poprzez określone funkcje w regułach. Użytkownicy nieposiadający AMODIT mogą również korzystać z TrustCenter, integrując się bezpośrednio przez API. To system organizujący zbieranie podpisów od wielu uczestników procesu podpisywania. Projekt obejmuje również takie zagadnienia jak blockchain i mechanizmy podpisu oraz weryfikacji dokumentów.

  

### `Moduly/Ustawienia-systemowe`

Nowy moduł ustawień systemowych. Konfiguracja systemu, zarządzanie jobami, integracje.

  

#### `Moduly/Ustawienia-systemowe/Integracje-rozszerzenia`

Konfiguracja integracji i rozszerzeń. Zarządzanie pluginami, zewnętrznymi serwisami.

  

#### `Moduly/Ustawienia-systemowe/Zadania-jobs`

Widok jobów i zadań cyklicznych. Monitorowanie, zarządzanie harmonogramem, logi wykonań.

  

### `Moduly/Wspolna-praca-na-dokumentach-office`

Wspólna praca na dokumentach Office (SharePoint). Zarządzanie sesjami edycji, synchronizacja dokumentów, lock/unlock.

  

### `Moduly/Zrodla-danych`

To moduł integracji i przechowywania danych z innych systemów. Dane ze źródeł można wykorzystywać w AMODIT w różnych miejscach, takich jak raporty czy sprawy (np. poprzez pola odnośnik do źródła zewnętrznego). Dostępne są różne typy źródeł:

- **"Online"** – dane nie są przechowywane w AMODIT, lecz pobierane na bieżąco przez ODBC z zewnętrznego systemu.

- **"Local"** – dane synchronizowane z systemem zewnętrznym i trzymane w dedykowanych tabelach w AMODIT.

- **"Static"** – dane zasilane jednorazowo (np. import z Excela) i przechowywane lokalnie.

Aktualnie rozwijany jest typ „dynamiczny" – pozwala na jeszcze elastyczniejsze integracje i konfiguracje źródeł danych. Wprowadzane są funkcje reguł, takie jak `SourceGet` i podobne, dzięki którym z poziomu reguł można jednostkowo pobierać, zapisywać lub modyfikować dane bezpośrednio w wybranym źródle. Umożliwia to dynamiczne operacje na danych – zarówno odczyt, jak i zapis – w trakcie działania procesów, bez potrzeby ręcznego importu lub synchronizacji całych tabel. Pozwala to budować w pełni personalizowane przepływy oraz zaawansowane integracje z różnymi zewnętrznymi systemami i bazami w czasie rzeczywistym.

  

---

  

## Cross-cutting (`cross-cutting/`)

  

### `cross-cutting/Bezpieczenstwo-pentesty`

Kompleksowe zarządzanie bezpieczeństwem systemu AMODIT. Obejmuje wszystkie działania związane z bezpieczeństwem: wyniki pentestów i naprawa wykrytych luk, hardening systemu (w tym Security Checklist - formalna checklista bezpieczeństwa dla instalacji on-premise do podpisania przez klienta i dostawcę), usuwanie podatności (CVE, OWASP Top 10), bezpieczeństwo sesji (wylogowanie, timeout, tokeny), bezpieczeństwo komunikacji (HTTPS, certyfikaty), szyfrowanie danych, ochrona przed atakami (XSS, CSRF, SQL Injection), security compliance. Systematyczne testy penetracyjne, szybka reakcja na luki krytyczne (hotfix 24-48h), proaktywne wzmacnianie zabezpieczeń. Security Lead: Łukasz Bott.

### `cross-cutting/Logowanie-do-amodit`

Kompleksowe zarządzanie wszystkimi aspektami zakladania konta, logowania, logowania MFA

  

### `cross-cutting/Dostep-bylych-wspolpracownikow`

Zarządzanie uprawnieniami dla osób usuniętych z roli współpracownik. W AMODIT rola współpracownik daje uprawnienia do edycji sprawy (jak właściciel), ale po usunięciu z tej roli osoba traci dostęp do spraw, nad którymi pracowała. Projekt zapewnia zachowanie dostępu do odczytu dla byłych współpracowników sprawy, aby nie tracili historii swojej pracy.

  

### `cross-cutting/GTA - dostęp tymczasowy do sparwy`

Funkcjonalność tymczasowego dostępu do sprawy ("GTA" – Grant Temporary Access). Pozwala nadać czasowy dostęp do wybranej sprawy osobie spoza AMODIT (np. kandydatowi do pracy, klientowi, zewnętrznemu kontrahentowi), która nie posiada własnego konta. Użytkownik taki może otrzymać jednorazowy, ograniczony czasowo link do formularza sprawy – umożliwia to np. wypełnienie informacji lub uzupełnienie danych, bez nadawania normalnego dostępu do systemu. GrantTemporaryAccessToCase to funkcja reguł obsługująca nadanie takiego dostępu, ale jest tylko elementem całej funkcjonalności tego typu dostępu.

  

### `cross-cutting/Wyszukiwanie-Lucene`

Problemy z działaniem mechanizu indeksujacego Lucene, wyszukiwarak tekstowa spraw, zarówno na listach , zakładkach typu "Do wykonania", "Wszystkie" itp. Wyszukiwanie pełnotekstowe w raportach

  

### `cross-cutting/Zakladka-Raporty`

Nowy wygląd i funkcjonalności zakładki "Raporty" w menu głównym. Przepisanie na React, nowe formaty wyświetlania (kafelki, lista, lista kompaktowa), ulepszone sortowanie i filtrowanie (moje raporty, ostatnio modyfikowane, szukanie po źródle), wizualne rozróżnianie typów raportów (ikony), zapamiętywanie filtrów per użytkownik. Metadane raportów widoczne na liście (opis, autor, typ).

### `cross-cutting/Design-System`

Zbiór ostatecznych ustaleń dotyczących wyglądu i zachowania wszystkich elementów interfejsu AMODIT – tu definiujemy spójne zasady tworzenia UI dla całego systemu. Projekt ten pełni rolę systemu design AMODIT: ustalamy tu standardy kolorystyki, odstępów, zaokrągleń rogów, typografii, ikonografii oraz innych reguł estetyki i dostępności. Wszystkie ogólne wytyczne dotyczące wyglądu, proporcji i UX (przycisków, formularzy, kart, powiadomień itp.) mają być opisane właśnie tutaj. Każdy nowy czy modyfikowany element UI powinien być zgodny z tymi wytycznymi – nie stosujemy wyjątków bez aktualizacji tego wzorca.

### `cross-cutting/Zakladka-Procesy`

Nowy wygląd i funkcjonalności zakładki "Procesy" w menu głównym. Przepisanie na React, nowy format wyświetlania (ulubione, kafelki, lista kompaktowa), opisy procesów widoczne na liście. Modal pośredni przed uruchomieniem sprawy z opisem procesu (można wyłączyć dla znanych procesów). Usprawnienie nawigacji i odnajdywania procesów.

### 

### `cross-cutting/Interfejs-sprawy`

Wszystko co dotyczy zachowania się sprawy (case) w AMODIT , mcase.aspx o ile nie jest to wyspecyfikowane w podprojektach, wtedy mnaley uzywac podprojektu


#### `cross-cutting/Interfejs-sprawy/Formularz-sprawy`

Kompleksowy projekt obejmujący wszystkie aspekty formularza sprawy. Wygląd i estetyka - modernizacja UI, gradienty, kolory. Logika renderowania (runtime) - wyświetlanie pól, tabel, walidacja, oddzielenie od edytora (design-time vs runtime). Wydajność - optymalizacja ładowania złożonych formularzy z tabelami zagnieżdżonymi. Responsywność - działanie na różnych urządzeniach. Śledzenie wszystkich decyzji, zadań i postępów dotyczących formularza sprawy.

  

#### `cross-cutting/Interfejs-sprawy/Historia-sprawy`

Widok historii zmian w prawym panelu sprawy. Wyświetla timeline wydarzeń, zmiany statusów, edycje pól formularza, przekazywania sprawy. Projekt obejmuje poprawę czytelności - wyświetlanie przyjaznych nazw pól (DisplayValue) zamiast nazw technicznych (FieldName), z nazwą techniczną dostępną w tooltipie. Historia zmian na sprawie, audyt wszystkich modyfikacji.

  #### `cross-cutting/Interfejs-sprawy/Historia-biznesowa`

Widok historii biznesowej opartej o zdarzenia zapisywane z poziomu reguł.

  

#### `cross-cutting/Interfejs-sprawy/Historia-aktywnosci-uprawnien`

Historia aktywności uprawnień w prawym panelu sprawy. Ujednolicenie i uporządkowanie mechanizmów śledzenia zmian uprawnień oraz aktywności w sprawach. Obecnie system ma niespójności - historia uprawnień nie zawsze uwzględnia wszystkie ustawienia procesu (np. "administrator nie ma praw"), a w bazie logowane są zdarzenia, które nigdy nie są wyświetlane użytkownikom. Celem jest zapewnienie w 100% transparentnego i dokładnego mechanizmu audytowania dostępu do spraw, z możliwością elastycznej konfiguracji poziomu logowania zdarzeń przez administratorów.

  

#### `cross-cutting/Interfejs-sprawy/Podglad-dokumentow`

Podgląd dokumentów w prawym panelu sprawy. Wyświetlanie podglądów różnych typów plików (.txt, .json, .xml, .md, .html, PDF) bezpośrednio w przeglądarce bez potrzeby pobierania. Umożliwia użytkownikowi szybki wgląd w treść załączonych dokumentów bez opuszczania interfejsu sprawy.


#### `cross-cutting/Interfejs-sprawy/Podglad-szablonow`

Podgląd szablonów dokumentów  w prawym panelu sprawy. Funkcjonalność potrzebna gdy uzytkownik przed uzyxciem szablonu chce zobaczyc co ten szablon zawiera, czego dotyczy. Inny przypadek uzycja to prezentowanie uzytkownikom np tekstu instrukcji z pdf aby nie zalaczac do setek spraw tego samego dokumentu z instrukcja.


### `cross-cutting/Komunikaty-systemowe`

Wyświetlanie komunikatów systemowych. Powiadomienia, alerty, komunikaty informacyjne.

  

### `cross-cutting/Logowanie-delete-case`

Rejestrowanie operacji trwałego usuwania spraw. Audyt kasowania, logi bezpieczeństwa.

  

### `cross-cutting/Logowanie-powiadomien`

Ślad audytowy dla powiadomień e-mail z procesów. Logi wysyłki, debugowanie powiadomień.

  

### `cross-cutting/Szablony-maili-systemowych`

Zarządzanie szablonami maili systemowych. Ochrona przed nadpisaniem, wersjonowanie szablonów.


### `cross-cutting/Powiadomienia-systemowe`

Kwestie powiadomień systemowych o utwotrzeniu sprawy, o przesłanu sprawy, o dodaniu komentarza. Obecnie system opiera się o zalozenie ze sa dwie grupy powiadomen "główne" i "pomocnicze" 


### `cross-cutting/Testy-kompatybilnosci-API`

Testy snapshotowe do wykrywania zmian w publicznym API kluczowych bibliotek. Weryfikacja zgodności wersji.

  

### `cross-cutting/Usuwanie-spraw-powiazanych`

Usuwanie spraw powiązanych. Zarządzanie zależnościami, kaskadowe usuwanie.


### `cross-cutting/Zarzadzanie-licencjami`

Projekt dotyczy wszystkich aspektów zarzadzania licencjami uzytkownikow, licencjami na moduly takie jak e-Nadawca, Paczka Przelewów, REST API itd. Dotyczy tez aspektu dzialania "wersji demo" (sytuacja braku licenji)

### `cross-cutting/WCAG`

Dostępność (WCAG). Eksperyment z trybem ciemnym (Dark Mode), kontrast, czytniki ekranu.

  

### `cross-cutting/Wydajnosc`

Wydajność i performance. Optymalizacja zapytań, cache, ładowanie aplikacji. (NIE dotyczy aktualizacji serwerów DevOps).

  

### `cross-cutting/Wzmiankowanie-w-komentarzach`

Przebudowa logiki @mention. Rola reader, dedykowany email, powiadomienia o wzmiankowaniach.

  

### `cross-cutting/Zakladka-Do-wykonania`

Konfiguracja wyświetlania zadań dla współpracowników. Widok "Do wykonania", filtrowanie zadań.

  

### `cross-cutting/Zastepstwa-grupy`

Zastępstwa i grupy. Delegowanie uprawnień, zastępstwa podczas nieobecności.

  

---

  

## Integracje (`Integracje/`)

  

### `Integracje/Integracje-REST-multipart`

Integracje REST z obsługą multipart. Wysyłka plików przez REST API, wielo-częściowe requesty.

  

### `Integracje/SharePoint-OAuth`

Integracja z SharePoint przez OAuth. Autoryzacja, synchronizacja dokumentów.

  

### `Integracje/System-mailowy`

Integracja z systemem mailowym. Wysyłka i odbieranie emaili, SMTP, IMAP.

### `Integracje/Integracja-CAS`
Integracja systemu AMODIT z systemem CAS (Central Authentication Service) w celu zapewnienia centralnej autoryzacji, autentykacji oraz zarządzania uprawnieniami użytkowników.

### `Integracje/Integracja-KSeF`
Integracja systemu AMODIT z connectorem KSeF, który jest wytwarzany i utrzymymywany przez zespół Piotra Wągla.


---

  

## Klienci (`Klienci/`)

#### `klienci/Neuca/DocuSign`
Rozszerzenie istniejącej integracjio z DocuSign. Glowanie o funkcjonalnosc 'envelope' ale jednoczesnie rozbudowa o mozliwosc wolania innych endpointow DocuSign. Tyle ze do tego mozna wykorzystac funcje CallRest rozbudowujac ja o odpowiedni mechanizmy logowania ktore ma DocuSign

#### `klienci/Lewiatan/Comarch-HUB`
Integracja systemu AMODIT z systemem Comarch HUB w zakresie KseF. To niezalena, wręcz w pewnym sensie konkurencyjna integracja, bo mamy własny KseF Connector, ale klient chce przez Comarch Hub


#### `Klienci/LOT/JRWA`

JRWA dla LOT. Specyficzne wymagania rejestru akt.

#### `Klienci/LOT/ADE`

INtegracja z ADE - Archiwum Dokumentów Elektoronicznych - Archiwum Państwowe. 
  
#### `Klienci/LOT/Integracjai-SIEM`

INtegracja z SIEM (Security Information and Event Management). Wykorzystuje standardy jak Syslog, JSON, CEF, LEEF, agentów własnych, API — ale sam SIEM nie definiuje formatu ani protokołu.

#### `Klienci/LOT/Integracja-UPS`
Obsluga firmy kurierskiej UPS z poziomu regul w AMODIT

#### `Klienci/LOT/Integracja-Global-Express`
Obsluga firmy kurierskiej Global-Express z poziomu regul w AMODIT

#### `Klienci/LOT/Wielospolkowosc`

Wielospółkowość dla LOT. Zarządzanie wieloma podmiotami w jednej instancji.



#### `Klienci/Marba/CallRest-wiele-plikow`

CallRest z obsługą wielu plików dla Marba. Wysyłka múltiple attachments przez REST.

  

#### `Klienci/Marba/Integracje-KSeF`

Integracja z KSeF (Krajowy System e-Faktur) dla Marba. Wymiana faktur elektronicznych.



#### `Klienci/PKF/Rejestracja-czasu-pracy`

Rejestracja czasu pracy dla PKF. Timesheet, rozliczanie godzin.

#### `Klienci/PKF/Przechowywanie-plikow`
PKF ma wymaganie aby pliki zapisywane w sprawach bylo odpowiednio organizowane np w foldery



#### `Klienci/Polpharma/Import-export-procesow`







Import i eksport procesów dla Polpharma. Migracja definicji procesów między środowiskami.







#### `Klienci/Rossmann/Komunikaty-systemowe`







Komunikaty systemowe dla Rossmann. Customizowane powiadomienia.







#### `Klienci/Rossmann/Trust-Center-integracja`







Integracja Trust Center dla Rossmann. Blockchain, zarządzanie certyfikatami.







#### `Klienci/LOT`



Projekt klienta LOT, do ogólnych tematów niezwiązanych z konkretnymi podprojektami.







#### `Klienci/WIM/Call-Snippet`

Tak nazwał to klient, ale ostatecznie zrealizowaliśmy CallFunctionEx – rozszerzenie CallFunction o możliwość wywołania kodu reguły (funkcji) z innego procesu.

  

#### `Klienci/WIM/Faktury-edytowalne-tabele`

Edytowalne tabele dla faktur WIM. Zarządzanie pozycjami faktur.

  

#### `Klienci/WIM/Komunikator`

Wewnętrzny komunikator (wewnętrzna, techniczna nazwa to AMODIT Talk) opracowywany i wdrożony dla WIM – niezależny od spraw (to nie komentarze w sprawach). Minimalistyczna wersja narzędzia typu Teams czy Slack, dostosowana do podstawowych potrzeb WIM.

  

#### `Klienci/WIM/Logowanie-powiadomien`

Logowanie powiadomień dla WIM. Audyt wysyłki emaili.

  

#### `Klienci/WIM/News-Feed-Anonse`

Mechanizm wyświetlania ogłoszeń i newsów na procesach WIM. Feed aktualności.

  

#### `Klienci/WIM/Podpis-kwalifikowany-SignApp-macOS`

Obsługa podpisu kwalifikowanego na macOS dla WIM. Integracja z certyfikatami. Aplikacja SignApp dla macOS

  

#### `Klienci/WIM/Raporty-osadzone-checkboxy`

Checkboxy w raportach osadzonych dla WIM. Zaznaczanie wielu elementów.

  

#### `Klienci/WIM/Repozytorium-plikow-DMS`

Repozytorium Plików (DMS) dla WIM. struktury przestrzeni i folderów wraz z uprawnieniami. Mozliwość tworzenia struktury "przestrzenie" -> "foldery" -> pliki 

  

#### `Klienci/WIM/Raporty-edycja-gradientow`

Edycja gradientów kolorów w raportach dla WIM. Projekt wynika z wymagania Piotra Murawskiego (WIM) o możliwość dostosowania palet kolorowych w wizualizacjach raportów (Treemap, Pivot). Umożliwia użytkownikom definiowanie własnych skal kolorystycznych zamiast domyślnych gradientów, resetowanie do domyślnej palety, oraz konfigurację kolorów dla wartości dodatnich, ujemnych i środkowych. MVP obejmuje podstawową edycję gradientów w raportach agregujących dane.

  

#### `Klienci/WIM/WCAG`

Implementacja dostępności WCAG 2.1 AA dla WIM. Tryb wysokiego kontrastu (wyczernienie treści, obramowanie elementów), tryb uproszczonego widoku sprawy dla czytników ekranowych, nawigacja klawiaturą. Deklaracja zgodności ze standardem WCAG 2.1 AA. Projekt realizowany pod wymagania WIM jako priorytetu biznesowego.

  

#### `Klienci/WIM/Zmienne-globalne`

Źródła danych Static (a w zasadzie nazywane dynamiczne) z funkcjami SourceSet SourceAdd, SourceGet dla WIM. Globalne zmienne konfiguracyjne.

  

---

  

## Koncepcje (`Koncepcje/`)

  

### `Koncepcje/AI-driven-workflow`

Koncepcja strategiczna: ewolucja AMODIT w kierunku agentów AI. Automatyzacja procesów przez AI.

  

### `Koncepcje/Okna-dialogowe`

Koncepcja okien dialogowych w AMODIT. Modale, popupy, interakcje użytkownika.

  

### `Koncepcje/RunAsUser`

Koncepcja wykonywania akcji w kontekście innego użytkownika. Impersonation, delegacja uprawnień.

  

### `Koncepcje/Tablica-ogloszen`

Koncepcja tablicy ogłoszeń. Komunikacja wewnętrzna, anonsowanie zmian.

  
### `Koncepcje/Open-Data`

Projekt obejmuje udostepnianie danych z AMODIt przez OpenData dla takich systemów jak Tableau, Power BI, Qlick

---

  

## Organizacja DEV (`Organizacja-DEV/`)

  

Obszar obejmujący **projekty organizacyjne** działu R&D oraz **dokumentację organizacyjną** (procesy, narzędzia, standardy, zespół, HR).

  

### `Organizacja-DEV/Automatyzacja-dokumentacji-AI`

Projekt organizacyjny działu DEV. Automatyzacja przepływów pracy dokumentacyjnej przy użyciu AI - generowanie notatek ze spotkań, przetwarzanie transkrypcji, mapowanie ustaleń na projekty, utrzymanie bazy wiedzy projektowej. Narzędzia i agenci Claude Code wspomagające zarządzanie dokumentacją techniczną i wiedzą zespołu R&D.

  

### `Organizacja-DEV/Dokumentacja-organizacyjna`

Dokumentacja "jak pracujemy" - procesy, narzędzia, standardy działu R&D. Zawiera 5 kategorii: Procesy (Code review, Daily, Release), Narzędzia (Azure DevOps, Git, Środowiska), Zespół (Role, Spotkania, Kanały komunikacji), Standardy (Nazewnictwo, Kodowanie, Dokumentacja), HR (Onboarding, Urlopy, Szkolenia). Notatki organizacyjne z Daily/Rady Architektów/Planowania trafiają tutaj. Format tematyczny - każde ustalenie ma swój plik który ewoluuje w czasie.



#### `Organizacja-DEV/Dokumentacja-organizacyjna/Narzędzia`

Dokumentacja narzędzi używanych przez dział R&D. Azure DevOps, Git, środowiska deweloperskie, narzędzia do automatyzacji i testowania.



---



## UC moduł raportowy (`UC moduł raportowy/`)



### `UC moduł raportowy`

Baza wiedzy Use Cases dla nowego modułu raportowego. Szczegółowe przypadki użycia opisujące funkcjonalności, interakcje użytkowników i wymagania dla komponentów modułu raportowego. Systematyczna dokumentacja scenariuszy użytkowania wspierająca design i implementację funkcjonalności raportowych.



---



## Mapowanie tematów na projekty

  

**Jeśli w transkrypcji pojawia się:**

  

| Temat | Projekt |

|-------|---------|

| **Kanban, widok Kanban, board, zmiana stanów** | `Moduly/Modul-raportowy/Gantt` |

| **Gantt, oś czasu, planowanie** | `Moduly/Modul-raportowy/Gantt` |

| **Heatmapa, mapa cieplna** | `Moduly/Modul-raportowy/Heatmapa` |

| **Raporty, SQL, źródła danych, logi SQL** | `Moduly/Modul-raportowy` |

| **Raporty systemowe, dashboardy, licencja premium** | `Moduly/Raporty-systemowe` |

| **Edytor reguł, reguły biznesowe, Ctrl+S w regułach** | `Moduly/Silnik-regul` |

| **Słowniki, słowniki hierarchiczne, zagnieżdżone** | `Moduly/Slowniki` |

| **Wyszukiwanie (po numerze sprawy, pełnotekstowe)** | `cross-cutting/Interfejs-sprawy` |

| **Blockchain, dodawanie dokumentów do blockchain** | `Moduly/Trust-Center` |

| **Copilot, AI, baza wiedzy, opisy raportów** | `Moduly/AMODIT Copilot` |

| **Komunikator (WIM), grupy, czaty, pliki** | `Klienci/WIM/Komunikator` |

| **Repozytorium (WIM), DMS, OCR** | `Klienci/WIM/Repozytorium` |

| **e-Doręczenia, Poczta Polska, joby OCR** | `Moduly/e-Doreczenia` |

| **Formularz sprawy, UI sprawy, widoki** | `cross-cutting/Interfejs-sprawy` |

| **Ikonki procesów, grafiki kafelków, brandowanie** | `cross-cutting/Interfejs-sprawy` |

| **Etapy, przejścia między etapami, warunki** | `Moduly/Edytor-procesow` |

| **Lista pól formularza** | `Moduly/Edytor-procesow/Edytor-formularzy` |

| **Joby, zadania cykliczne, harmonogram** | `Moduly/Ustawienia-systemowe/Zadania-jobs` |

| **Dark mode, tryb ciemny, WCAG, dostępność** | `cross-cutting/WCAG` |

| **Wydajność, performance, optymalizacja zapytań** | `cross-cutting/Wydajnosc` |

| **Synchronizacja źródeł, ujemne ID, source get/set** | `Moduly/Zrodla-danych` |

| **@mention, wzmiankowanie, powiadomienia** | `cross-cutting/Wzmiankowanie-w-komentarzach` |

| **Pentesty, luki bezpieczeństwa, hardening, CVE, OWASP** | `cross-cutting/Bezpieczenstwo-pentesty` |

| **Bezpieczeństwo sesji, wylogowanie, timeout, tokeny** | `cross-cutting/Bezpieczenstwo-pentesty` |

| **Szyfrowanie, HTTPS, certyfikaty, TLS** | `cross-cutting/Bezpieczenstwo-pentesty` |

| **XSS, CSRF, SQL Injection, Command Injection** | `cross-cutting/Bezpieczenstwo-pentesty` |

  

**WAŻNE:** To są tylko podpowiedzi. Jeśli nie jesteś pewien → **"Nowy temat / do sklasyfikowania"**

  

---

  

## Zasady używania słownika

  

1. **ZAWSZE czytaj ten plik** przed przypisaniem projektu w notatce

2. **UŻYWAJ TYLKO** projektów z powyższej listy

3. **SPRAWDŹ opisy projektów** - jeśli temat pasuje do opisu, użyj tego projektu

4. **SPRAWDŹ tabelę mapowania** - jeśli nie jesteś pewien, poszukaj w tabeli

5. **NIE ZGADUJ** nazw projektów - jeśli nie ma w liście → **"Nowy temat / do sklasyfikowania"**

6. **ZAPISUJ DOKŁADNĄ ŚCIEŻKĘ** z tego pliku - np. `Moduly/Modul-raportowy/Gantt` (dokładnie jak w sekcji nagłówków)

  

---

  

## Specjalne przypadki

  

### ❌ Projekty które NIE ISTNIEJĄ (nie używaj!):

- `cross-cutting/Testy` - nie istnieje, testowanie nie jest projektem

- `moduly/Zarządzanie-sprawami` - nie istnieje, Kanban jest pod `Moduly/Modul-raportowy/Gantt`

- `cross-cutting/Wydajnosc` dla pracy DevOps (aktualizacje serwerów) - nie przypisuj

  

### ⚠️ Wątpliwości:

Jeśli temat dotyczy kilku projektów jednocześnie:

- Wybierz najbardziej specyficzny (np. `Gantt` zamiast ogólnego `Modul-raportowy`)

- Jeśli równie ważne - wybierz główny (np. funkcjonalny moduł zamiast cross-cutting)

- W ostateczności → **"Nowy temat / do sklasyfikowania"** i zaznacz które projekty mogą być powiązane

  

---

  

## Aktualizacja słownika

  

Ten plik jest utrzymywany ręcznie. Przed dodaniem nowego projektu:

1. Sprawdź czy projekt faktycznie istnieje w `projekty/`

2. Dodaj krótki opis (2-3 zdania) wyjaśniający zakres projektu

3. Zaktualizuj tabelę mapowania tematów jeśli potrzeba

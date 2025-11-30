## Spotkanie Rady Architektów z dnia 14 października 2025

---

#### 1. Problem e-doręczeń (Poczta Polska)

- **Ryzyko:**
    
    - Niespójność dokumentacji (różne wersje z odstępem 2 miesięcy)
        
    - Problem z działaniem usługi przy uruchomionych dwóch instancjach Application Server (AS) – jedna instancja nie działa, chociaż indywidualnie obie działają poprawnie, jeśli są uruchomione osobno.
        
    - Otrzymywanie błędu "forbidden"1.
        
    - Możliwe ograniczenie przez Pocztę Polską łączenia się danej firmy tylko z jednego serwera2.
        
    - Problem może leżeć w konfiguracji serwerów po stronie firmy (np. 2 adresy IP) lub zbyt szybkim wysyłaniu żądań przez dwa konkurencyjne serwery3.
        
- **Proponowane rozwiązanie:**
    
    - Ustalenie i sprawdzenie mechanizmu **Preferred Server** dla danej usługi, aby wymusić łączenie zawsze przez jeden serwer (np. AS 01 lub AS 02)4444.
        
    - Intensywna współpraca w celu znalezienia rozwiązania5.
        
- **Decyzja:**
    
    - Problem najprawdopodobniej dotyczy **konfiguracji serwerów po stronie firmy**, a nie Poczty Polskiej6.
        
    - Konieczna jest intensywna praca nad rozwiązaniem i weryfikacja kwestii konfiguracji.
        
- **Zadania:**
    
    - **Adrian Kotowski i Piotr Buczkowski:** Uzgodnić, o co dokładnie chodzi w temacie e-doręczeń i jak to ma być zrobione7.
        
    - **Adrian Kotowski:** Sprawdzić i uruchomić mechanizm Preferred Server na wskazanym serwerze (np. AS 01 lub AS 02) i zweryfikować jego działanie8888.
        
    - **Piotr Buczkowski i Adrian Kotowski:** Intensywnie popracować wspólnie nad znalezieniem rozwiązania9.
        

---

#### 2. Systemowe Dashboardy i Raporty (Ujemne ID)

- **Ryzyko:**
    
    - Problem z ujemnymi ID dla raportów i źródeł systemowych (np. `-22`), co było mechanizmem odróżniania ich od customowych10101010.
        
    - Ujemne ID mogą powodować błędy w mechanizmach synchronizacji (np. błąd składni w zapytaniach SQL - `SELECT * FROM DPSRC_-22`)11.
        
    - Zmiana ID źródeł systemowych mogłaby popsuć istniejące raporty klientów, które były na nich oparte, wskazując na nieistniejące ID12.
        
    - Konieczność planowania migracji starych ujemnych ID do nowych kolumn131313131313131313.
        
- **Proponowane rozwiązanie:**
    
    - Odejście od ujemnych ID, ponieważ jest to zła decyzja architektoniczna14141414.
        
    - Zamiast ujemnych ID, dodać kolumnę logiczną (np. `is_system_report`) oraz kolumnę na GUID, aby systemowe raporty nie miały ujemnych ID15151515.
        
    - **Odrzucenie kompatybilności wstecznej** z klientami w zakresie systemowych raportów/źródeł (prawdopodobieństwo, że klienci to zmodyfikowali, jest znikome)1616161616161616.
        
    - Przyjęcie na siebie zobowiązania do nieodpłatnej konfiguracji w razie problemów z raportami klientów, które mogły być oparte o stare ID17.
        
    - Zrobienie tego "po bożemu", tak jak powinno być, bez mechanizmów uwzględniających minusy18181818.
        
- **Decyzja:**
    
    - **Uporządkować** problem ujemnych ID w systemowych źródłach danych i raportach, rezygnując z ujemnych ID19191919.
        
    - **Odrzucić** konieczność utrzymywania pełnej kompatybilności wstecznej dla klientów (zakładając znikome użycie przez nich) i naprawić ewentualne problemy ręcznie20202020.
        
- **Zadania:**
    
    - **Łukasz Bott i Anna Skupińska:** Zaplanować przejście na **GUID** (zamiast ID) dla raportów systemowych i źródeł systemowych, uwzględniając wszystkie potencjalne konsekwencje (w tym migracje i wpływ na inne raporty)21212121.
        
    - **Łukasz Bott i Anna Skupińska:** Przygotować projekt tego przejścia na następne spotkanie Rady (za 2 dni)22.
        

---

#### 3. Tabelka w Formularzu (Widok Desktop vs. Mobilny)

- **Ryzyko:**
    
    - Błąd, który powoduje, że w nowej wersji na widoku desktopowym **podtabelka nie wyświetla się w ogóle** wewnątrz formularza nadrzędnego23232323.
        
    - Różnice w sposobie renderowania (zmiana wyglądu formularzy, przesunięcie labelek) utrudniają przywrócenie poprzedniej funkcjonalności24242424.
        
    - Zagnieżdżenie tabeli w formularzu (zwłaszcza wielokolumnowej) prowadzi do niepraktycznego interfejsu (poziome przewijanie w pionowym układzie)25252525.
        
- **Proponowane rozwiązanie:**
    
    - **Wymuszenie jednolitego zachowania** na desktopie i widoku mobilnym: jeżeli tabela nadrzędna jest formularzem, podtabelka również musi być wyświetlana w **trybie formularzowym** (jak na mobilnym)262626262626262626.
        
    - Druga opcja (kontrowersyjna): przywrócić tylko starą funkcjonalność działania (nie poprawiając nic więcej), nie ułatwiając i nie utrudniając pracy. Czekać na zgłoszenia ewentualnych problemów272727.
        
    - Ograniczenie funkcjonalności: Nie wspierać w ogóle zagnieżdżonych tabel w trybie formularzowym, uznając to za nieużywaną, złą funkcjonalność28282828.
        
- **Decyzja:**
    
    - **Przywrócić funkcjonalność** wyświetlania podtabelki w trybie formularzowym tak, jak działało to w poprzedniej wersji (grudniowej)29.
        
    - **Odłożenie** decyzji o rezygnacji lub standaryzacji widoku na kolejną Radę30.
        
    - Przeprowadzić szybki Proof of Concept (PoC) w celu oceny, czy przywrócenie starego działania jest proste i szybkie31.
        
- **Zadania:**
    
    - **Mariusz Piotrzkowski i Piotr Buczkowski:** Poświęcić **jeden dzień** na PoC: sprawdzić, czy da się szybko i łatwo przywrócić funkcjonalność tabelki w formularzu do stanu sprzed awarii (sprzed wersji marcowej). Przedyskutować dalsze kroki na czwartkowej Radzie32.
        
    - **Mariusz Piotrzkowski:** Przerobić zgłoszenia pod kątem tej decyzji, aby zredukować ilość pracy33.
        

---

#### 4. Optymalizacja Wydajności (Pobieranie Danych)

- **Ryzyko:**
    
    - W widokach opartych o React (nowe widoki) występują problemy z **nadmiernym pobieraniem danych** przy wejściu na stronę (np. pobieranie wszystkich użytkowników, wszystkich pozycji słownika, wszystkich słowników)3434343434.
        
    - Jest to nieoptymalne, zwłaszcza w środowiskach z dużą liczbą użytkowników (np. 200 tys.)35.
        
    - Występuje to m.in. przy wejściu do **LogView** i **edytora uprawnień do pola**363636363636363636.
        
- **Proponowane rozwiązanie:**
    
    - Wprowadzić zasadę, że dane powinny być ładowane **leniwiej** (on-demand), dopiero gdy użytkownik faktycznie potrzebuje tych danych (np. rozwinie filtr, otworzy sekcję, z której chce wybrać użytkownika)373737373737373737.
        
- **Decyzja:**
    
    - Konieczna jest pilna optymalizacja sposobu pobierania danych w nowych widokach38.
        
- **Zadania:**
    
    - **Kamil Dubaniowski:** Porozmawiać z deweloperami (zwłaszcza z Filipem i Przemkiem), aby zwracali większą uwagę na optymalizację i ładowanie leniwe, korygując wywołania API393939393939393939.
        

---

#### 5. Logika Wzmiankowania (@mentions)

- **Ryzyko:**
    
    - Aktualna logika uniemożliwia wzmiankowanie (@mentions) osób, które **już mają dostęp** do sprawy, gdy wyłączone jest dodawanie nowych do DW40404040.
        
    - Wzmiankowanie zależy od jednego ustawienia (DWW lub Contributor), co jest nielogiczne41.
        
    - Problem z powiadomieniami mailowymi: osoba wzmiankowana dostaje powiadomienie dopiero przy **drugiej akcji** na sprawie, a nie przy samej wzmiance42424242.
        
- **Proponowane rozwiązanie:**
    
    - **Wzmiankowanie** osób, które są już w sprawie (mają dostęp/uprawnienia), powinno być **zawsze możliwe**, niezależnie od ustawień blokujących dodawanie do DWW434343.
        
    - Przyszłościowo: Oddzielenie **roli DWW** od **funkcjonalności wzmiankowania** (dodanie osobnego checkboxa w ustawieniach procesu, np. DWW wzmiankowanie)44.
        
- **Decyzja:**
    
    - **Poprawka (na teraz):** Wzmiankowanie (@mentions) osób, które już mają dostęp do sprawy, musi działać, nawet jeśli opcja dodawania nowych do DWW jest wyłączona45.
        
    - **Odłożenie:** Rozdzielenie ról DWW i wzmiankowania na osobny temat do globalnego zaplanowania (design)46464646.
        
- **Zadania:**
    
    - **Mariusz Piotrzkowski:** Zmienić logikę wzmiankowania, aby była sterowana tylko ustawieniem DWW (odciąć zależność od Contributor) i umożliwić wzmiankowanie osób z dostępu47474747.
        
    - **Kamil Dubaniowski:** Przerobić Fory, aby Mariusz miał mniej pracy, zwalniając go z innych zadań48.
        

---

#### 6. Koszty i Realizacja Blockchain

- **Ryzyko:**
    
    - Konieczność ustalenia sposobu i kosztów realizacji blockchain49494949.
        
- **Proponowane rozwiązanie:**
    
    - Marek przygotuje dokument i techniczne przemyślenia50.
        
- **Decyzja:**
    
    - Temat do przedyskutowania na kolejnym spotkaniu Rady5151.
        
- **Zadania:**
    
    - **Marek Dziakowski:** Przygotować dokumentację i przemyślenia techniczne dotyczące blockchain (sposób i koszty) na czwartkową Radę52525252.
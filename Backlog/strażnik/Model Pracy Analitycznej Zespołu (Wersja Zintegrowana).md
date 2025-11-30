#backlog #azure #mvp

[[Strażnik backlogu]]

Autor: [[Janusz Bossak]]

Dla: Product Delivery Managerów, Product Ownerów, Zespołów Deweloperskich

Cel: Ustanowienie kompletnego standardu pracy nad nowymi projektami lub funkcjonalnościami, który maksymalizuje dostarczaną wartość biznesową poprzez rygorystyczne skupienie na ukończeniu jednego MVP (Minimum Viable Product) na raz.

### Filar 1: Filozofia Pracy (Dlaczego tak pracujemy?)

Zanim przejdziemy do procesu "Jak?", musimy ustanowić fundamentalne zasady "Dlaczego?". Naszym największym ryzykiem nie jest błąd w analizie pojedynczej funkcji, ale marnotrawstwo wynikające z chaosu w realizacji, nadmiernej liczby prac w toku (WIP) i kosztu przełączania kontekstu.

#### Zasada 1: "Przestań Zaczynać, Zacznij Kończyć" (Stop Starting, Start Finishing)

To jest nasza nadrzędna dyrektywa. Koncentrujemy 100% wysiłków zespołu deweloperskiego na ukończeniu **jednego MVP na raz**.

- **Wartość dla Klienta = 0:** Jeśli mamy trzy MVP rozpoczęte i każde jest ukończone w 33%, dostarczona wartość biznesowa wynosi zero. Żadna z tych funkcji nie jest używalna.
    
- **Dyscyplina:** Nie rozpoczynamy pracy nad **żadnym** zadaniem (PBI, Feature) z MVP 2, dopóki MVP 1 nie jest w 100% ukończone, przetestowane i gotowe do wdrożenia. Aktywnie zwalczamy pokusę "szybkiego dorzucenia" czegoś z boku.
    
- **Feedback:** Tylko ukończone MVP pozwala nam zebrać realny feedback od użytkowników, który może (i powinien) wpłynąć na kształt i priorytet kolejnych MVP.
    

#### Zasada 2: MVP to Wartość, nie Worek Funkcji

MVP nie jest po prostu "listą funkcji". To **najmniejszy możliwy zestaw funkcji, który realizuje konkretny Cel Biznesowy** (Krok 2) i może być dostarczony w **skończonym, racjonalnym czasie**.

### Filar 2: Proces Analityczny (Jak pracujemy?)

Proces analityczny postępuje od ogółu do szczegółu, w sposób kontrolowany i zgodny z naszymi zasadami.

#### Krok 0: Ustalenie Wartości Biznesowej (Wielkie "Dlaczego?")

**Odpowiedzialny**: PDM, kluczowi interesariusze (Zarząd, Klient).

Zanim napiszemy pierwszą linię analizy, musimy jasno określić strategiczny powód istnienia projektu. Odpowiadamy na pytania:

1. **Wartość dla Użytkownika:** Jaki realny problem rozwiązujemy? Jakie usprawnienie wprowadzamy?
    
2. **Wartość dla AMODIT:** Jak to wspiera naszą strategię? (np. zwiększenie przychodów, obniżenie kosztów, wejście na nowy rynek, realizacja umowy).
    

> **Test:** Jeśli funkcjonalność nie buduje realnej wartości biznesowej — nie powinna być projektem.

#### Krok 1: Mapowanie Kluczowych Funkcjonalności (Co?)

**Odpowiedzialny**: PDM, Analityk, Interesariusze.

Na tym etapie robimy burzę mózgów, aby wylistować **wszystkie** potencjalne Główne Obszary Funkcjonalne (kategorie), które składają się na ogólną wizję. Nie filtrujemy, nie priorytetyzujemy – tworzymy mapę możliwości.

_Przykład dla "Komunikatora":_

- Wiadomości (tekstowe, DM, wątki, edycja)
    
- Multimedia (pliki, emoji)
    
- Zarządzanie (kanały)
    
- Wyszukiwanie (kanały, użytkownicy, pełnotekstowe)
    
- Interakcje (powiadomienia)
    
- Integracje (sprawa AMODIT, wideo)
    

#### Krok 2: Definicja Celu i Pojemności MVP 1 (Pierwsza Wartość)

**Odpowiedzialny**: PDM, Architekt/Lider Tech.

Mając mapę (Krok 1) i Wartość (Krok 0), definiujemy precyzyjny, strategiczny cel dla **pierwszej** wersji produktu (MVP 1). Ten krok jest **krytyczny** i składa się z dwóch części:

1. Definicja Celu Strategicznego:

Cel musi być jasny i filtrowalny.

Przykład: "Umożliwienie pracownikom prowadzenia szybkiej, tekstowej rozmowy (1-na-1 oraz grupowej) wyłącznie w kontekście konkretnej sprawy AMODIT."

2. Krytyczna Ocena Pojemności (Sizing MVP):

To jest moment, w którym adresujemy problem "pchania za dużo".

- Cel MVP musi być nie tylko _wartościowy_, ale także _możliwy do dowiezienia_ w skończonym, racjonalnym czasie (np. w ramach jednego kwartału lub ustalonego cyklu).
    
- Zadajemy sobie pytanie: "Czy ten cel jest wystarczająco **mały**, aby go dowieźć jako spójną całość? Czy nie próbujemy zmieścić trzech MVP w jednym?".
    
- Jeśli cel jest zbyt duży (np. "Pełna komunikacja tekstowa, wideo i zarządzanie kanałami"), **musimy go natychmiast podzielić** na mniejsze cele strategiczne (MVP 1: Czat kontekstowy; MVP 2: Kanały ogólne; MVP 3: Wideo).
    

#### Krok 3: Priorytetyzacja Funkcjonalności (Brutalne Cięcie)

**Odpowiedzialny**: PDM.

Teraz wracamy do mapy z Kroku 1 i brutalnie tniemy ją na priorytety, używając **dwóch filtrów**:

1. **Filtr 1 (Cel):** Czy ta funkcja jest absolutnie niezbędna, aby osiągnąć Cel MVP 1 (z Kroku 2)?
    
2. **Filtr 2 (Pojemność):** Czy po dodaniu tej funkcji nasze MVP 1 nadal mieści się w założonej _pojemności_?
    

To pytanie pozwala odróżnić "krytyczne" (must-have dla MVP 1) od "ważnych" (should-have, ale dla MVP 2).

_Przykład (kontynuacja):_

- **MVP 1 (Musi być - realizuje Cel i mieści się w pojemności):**
    
    - (Integracja) Integracja z formularzem sprawy AMODIT
        
    - (Wiadomości) Wysyłanie wiadomości tekstowych
        
    - (Wiadomości) Wysyłanie wiadomości prywatnych (DM)
        
    - (Interakcje) Powiadomienia w aplikacji (np. "kropka")
        
- **MVP 2 (Ważne, ale nie krytyczne dla Celu 1):**
    
    - (Multimedia) Wysyłanie plików
        
    - (Multimedia) Reakcje emoji
        
    - (Wiadomości) Edycja / Usuwanie wiadomości
        
- **"Kiedyś Może" (Luksus):**
    
    - (Wiadomości) Wątki (Threads)
        
    - (Integracje) Połączenia wideo/głosowe
        

#### Krok 4: Ustalenie Ram Technicznych i Architektonicznych (Jak?)

**Odpowiedzialny**: Warsztat (PDM, Architekt, Lider Tech).

To jest moment na analizę MAKRO, która musi się odbyć _przed_ analizą MIKRO (Krok 5). Decyzje te podejmujemy, patrząc na **całą mapę z Kroku 1** (aby zapewnić ewolucyjność), ale implementujemy fundamenty **niezbędne do uruchomienia MVP 1**.

- Pytania: Microserwis vs moduł? Technologie (np. SignalR)? Baza danych? Autentykacja? Wymagania niefunkcjonalne?
    
- Cel: Zaprojektować fundamenty, które będą w stanie _ewoluować_, ale nie _przeinżynierować_ (over-engineering) rozwiązania na starcie.
    

#### Krok 5: Analiza Głęboka (Use Cases) - _Tylko dla MVP 1_

**Odpowiedzialny**: PDM / Analityk Biznesowy.

Teraz rozpoczynamy szczegółową pracę analityczną (MIKRO). Bierzemy na warsztat **wyłącznie** te funkcjonalności, które zakwalifikowaliśmy do **MVP 1**.

Dla każdej z tych funkcji tworzymy szczegółowe Przypadki Użycia (Use Cases), aby przewidzieć wszystkie scenariusze podstawowe, alternatywne i błędy. (Szablon UC jak w oryginalnym dokumencie).

#### Krok 6: Dekompozycja na PBI (Zadania do Backlogu)

**Odpowiedzialny**: PDM / Analityk.

Ten krok działa w tandemie z Krokiem 5 w logice **"Just-in-Time"**. Analityk nie analizuje całego MVP 1 na raz. Analizuje i dekomponuje (na PBI lub Historyjki) tylko te funkcje, które są potrzebne zespołowi deweloperskiemu w _następnym_ sprincie.

- **Strumień Deweloperski (Sprint N):** Zespół implementuje (Krok 7) PBI dla funkcji A i B (przygotowane wcześniej).
    
- **Strumień Analityczny (Sprint N):** PDM/Analityk analizuje (Krok 5) i dekomponuje (Krok 6) funkcje C i D (na Sprint N+1).
    

#### Krok 7: Realizacja i Obrona Zakresu MVP 1

**Odpowiedzialny**: Zespół Deweloperski, PDM.

Precyzyjnie zdefiniowane PBI z Kroku 6 trafiają do backlogu i są realizowane. Na tym etapie kluczowa jest **dyscyplina realizacji** (nasza Zasada 1).

- **Obrona Zakresu:** Cały zespół deweloperski skupia się _wyłącznie_ na zadaniach zdefiniowanych dla MVP 1.
    
- **Zarządzanie Zmianą:** Każda nowa prośba (od interesariusza, klienta, czy nawet zespołu) jest oceniana przez PDMa pod kątem Celu MVP 1. Jeśli jest krytyczna dla celu, może wejść (potencjalnie kosztem innej funkcji z MVP 1 o niższym priorytecie). Jeśli nie jest krytyczna, trafia do backlogu MVP 2 lub "Kiedyś Może".
    
- **Kryterium Ukończenia:** MVP 1 jest "skończone" dopiero, gdy wszystkie PBI są zaimplementowane, przetestowane, a Cel Strategiczny (z Kroku 2) został osiągnięty i zweryfikowany (np. przez wewnętrzne demo lub udostępnienie grupie pilotażowej).
    

Dopiero po ogłoszeniu "MVP 1 - Zakończone", zespół rozpoczyna pracę nad MVP 2, powtarzając proces od Kroku 5 (lub Kroku 2, jeśli feedback znacząco zmienił priorytety).

### 5. Podsumowanie: Korzyści Procesu

Stosowanie tego zintegrowanego modelu zapewnia, że:

1. **Nie marnujemy czasu** na analizowanie funkcji "Kiedyś Może" ani na przełączanie kontekstu.
    
2. **Świadomie rozmiarujemy MVP**, aby było realne do dowiezienia, co buduje przewidywalność i morale zespołu.
    
3. **Koncentrujemy się na celu biznesowym** – każda budowana funkcja wspiera Cel MVP 1.
    
4. **Szybko dostarczamy realną wartość** i zbieramy feedback, co czyni nas zwinnymi nie tylko w teorii, ale przede wszystkim w praktyce.
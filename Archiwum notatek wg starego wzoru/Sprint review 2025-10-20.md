
[[2025-10-20 poniedziałek]]
[[2025-10-06 Sprint review]]

---

Sprint review z dnia 20 października 2025

---

### 1. Edytor Graficzny Formularza

- **Dlaczego to robimy**
    - Usprawnienie i zastąpienie starego edytora diagramów oraz formularzy nowym, bardziej intuicyjnym interfejsem.
    - Zbliżenie wyglądu edytora do realnego wyglądu formularza.
    - Poprawa ergonomii pracy (np. redukcja wizualnego szumu, poprawa okien edycji).
- **Opis funkcjonalności / rozwiązania:**
    - Zakończono przenoszenie wszystkich warunków ze starego diagramu; edytor obsługuje teraz dodawanie i łączenie etapów, dodawanie reguł oraz usuwanie połączeń.
    - Wprowadzono różne układy widoku: pionowy, poziomy, hierarchiczny (zwarty oraz standardowy, przypominający drzewo).
    - Ujednolicono ikony (kolor, rozmiar) pól, aby odpowiadały tym na docelowym formularzu.
    - Zmiany w polu "Tekst statyczny":
        - Powiększono okno edycji tego pola.
        - Treść tekstu statycznego jest teraz widoczna w podglądzie formularza w edytorze.
        - Nazwa pola statycznego jest teraz widoczna w edytorze (z adnotacją, że na formularzu docelowym jest ukryta).
    - Wprowadzono obsługę pól zablokowanych (np. w procesie "Kompanii ss"); użytkownik może w nich zmienić tylko nazwę wyświetlaną i podpowiedź.
    - Poprawiono sposób usuwania wyjątków – dedykowany przycisk jest teraz bardziej widoczny.
    - Linie oddzielające (podziały) wierszy zostały domyślnie ukryte; pojawiają się dynamicznie tylko podczas przeciągania pola lub najechania kursorem pomiędzy wiersze.
    - Dodano komunikat ostrzegawczy o niezapisanych zmianach przy próbie wyjścia z edytora.
    - W polach typu "Odnośnik" (wewnętrzny, zewnętrzny, słownik), zmiana źródła danych wymaga teraz dodatkowego potwierdzenia, informującego o ryzyku utraty danych.
- **Dalsze kroki:**
    - Do wdrożenia w kolejnym sprincie: Dodanie możliwości wyszukiwania po nazwie pola (sugestia Piotra).
    - Do poprawy: Pierwsza opcja wyboru w edycji pola "Tekst statyczny".
    - Do wdrożenia: Dodanie linków przy polach typu "Odnośnik", umożliwiających szybkie przejście do edycji powiązanego źródła (słownika, procesu, rejestru).
    - Planowane są dalsze, drobne zmiany kosmetyczne w edytorze.

---

### 2. Nowa Lista Pól

- **Dlaczego to robimy**
    - Edytor graficzny staje się głównym miejscem edycji; nowa lista ma służyć do szybkiego przeglądu pól oraz zarządzania tłumaczeniami (przeniesienie tej funkcji z osobnej zakładki).
    - Uspójnienie interfejsu z innymi nowymi widokami (np. matrycą uprawnień).
- **Opis funkcjonalności / rozwiązania:**
    - Zaprezentowano nowy widok listy pól.
    - Lista umożliwia edycję "inline" nazw systemowych oraz typu pola (przez okno modalne).
    - Wprowadzono zarządzanie tłumaczeniami (nazwa domyślna, PL, EN, DE) dla nazw pól i podpowiedzi bezpośrednio z nagłówków kolumn.
    - Wprowadzono wizualne rozróżnienie dziedziczenia nazw: tekst czarny oznacza nazwę zdefiniowaną, tekst szary oznacza nazwę dziczniczoną.
    - Tabele (pola zagnieżdżone) są wyświetlane w strukturze drzewa (zagnieżdżone wiersze), eliminując potrzebę przełączania widoków.
    - Dostępne jest wyszukiwanie po polach (podświetla komórki) oraz opcja ukrywania/przywracania widoczności kolumn.
- **Dalsze kroki:**
    - Funkcja zmiany kolejności pól (przeciągnij i upuść) nie została jeszcze zaimplementowana.
    - Trwa dyskusja nad wprowadzeniem kolorów dla rozróżnienia typów pól, aby interfejs edytora był czytelniejszy.

---

### 3. Walidacja Importu XML

- **Dlaczego to robimy**
    - Zabezpieczenie systemu przed błędami i utratą danych podczas importu procesów (XML) między środowiskami. W ostatnim czasie wystąpiły przypadki "zepsucia" procesów na produkcji przez konsultantów.
- **Opis funkcjonalności / rozwiązania:**
    - Dodano dokładniejszą walidację pól przy imporcie XML (dodano 4 nowe walidacje do 3 istniejących).
    - System wykrywa teraz konflikty, np. gdy pole o tej samej nazwie ma inny GUID lub jest przypisane do innego pola w bazie danych.
- **Dalsze kroki:**
    - Walidacja importu XML: Funkcjonalność powinna docelowo _blokować_ import do czasu przywrócenia spójności.
    - Sugestia (Janusz): Należy poszerzyć okno modalne walidacji i rozważyć układ dwukolumnowy (dane lokalne vs. dane importowane) dla lepszej czytelności konfliktów.

---

### 4. Obsługa Słowników Hierarchicznych i Zagnieżdżonych

- **Dlaczego to robimy**
    - [Nie sprecyzowano w transkrypcji].
- **Opis funkcjonalności / rozwiązania:**
    - W ramach prac dodano pełną obsługę słowników, które są jednocześnie hierarchiczne i zagnieżdżone.
- **Dalsze kroki:**
    - [Nie sprecyzowano w transkrypcji].

---

### 5. Moduł Raportowy i SimpleSign

- **Dlaczego to robimy**
    - Rozwój nowego modułu raportowego oraz integracja mechanizmów podpisu.
- **Opis funkcjonalności / rozwiązania:**
    - Dodano obsługę wyświetlania pól typu "Podpis" w nowym module raportowym.
    - Wdrożono i wydano funkcjonalność podpisywania SimpleSign na nowych raportach.
    - Zmieniono stronę docelową (landing page), na którą użytkownik jest przekierowywany po złożeniu podpisu.
- **Dalsze kroki:**
    - Proces podpisywania SimpleSign zostanie usprawniony – obecne dwa przyciski (Zaloguj, Wywołaj) zostaną zastąpione jednym "wizardem".
    - Należy wyjaśnić, czy zmiana strony docelowej (landing page) po podpisie była zmianą statyczną, czy też docelowo ma istnieć możliwość wyboru tej strony (pytanie Janusza).

---

### 6. E-Doręczenia

- **Dlaczego to robimy**
    - Kontynuacja prac nad integracją rządowego systemu e-Doręczeń.
- **Opis funkcjonalności / rozwiązania:**
    - Prace nad problemami z API e-Doręczeń są kontynuowane.
    - Zgłoszono uwagi do Centralnego Ośrodka Informatyki (COI).
- **Dalsze kroki:**
    - [Prace w toku, brak sprecyzowanych kolejnych kroków].

---

### 7. Aplikacja do Podpisywania MacOS

- **Dlaczego to robimy**
    - Zapewnienie wsparcia dla podpisów elektronicznych na systemie operacyjnym MacOS.
- **Opis funkcjonalności / rozwiązania:**
    - Prace nad aplikacją są tymczasowo wstrzymane (na rzecz e-Doręczeń).
    - Obecnie testowane jest wykrywanie podpisów Szafir.
- **Dalsze kroki:**
    - Adrian musi pozyskać podpis SimpleSign, aby móc kontynuować testy.
    - Celem jest obsługa 3 głównych podpisów (Szafir, SimpleSign, PW) do końca miesiąca.
    - Należy rozwiązać problem braku centralnego dostępu do zestawu podpisów testowych oraz komputera Mac dla reszty zespołu, aby uniknąć obciążania tylko Adriana serwisem tej aplikacji.

---

### 8. E-Nadawca

- **Dlaczego to robimy**
    - Rozwiązywanie problemów z integracją E-Nadawcy (Poczta Polska).
- **Opis funkcjonalności / rozwiązania:**
    - Występuje trudny do zdiagnozowania problem, który pojawia się tylko przez kilka godzin w ciągu dnia i samoistnie znika.
    - Jeden z problemów został rozwiązany.
- **Dalsze kroki:**
    - Zespół oczekuje na dalsze informacje od Poczty Polskiej w celu zdiagnozowania niestabilnego błędu.

---

### 9. Dashboardy Systemowe

- **Dlaczego to robimy**
    - Poprawa działania systemowych źródeł danych, które obecnie nie działają poprawnie na bazach MS SQL.
- **Opis funkcjonalności / rozwiązania:**
    - Problemem są ujemne ID, na podstawie których tworzone są nazwy tabel. O ile MySQL sobie z tym radzi, MS SQL ma z tym problem.
    - Zaprezentowano nowe dashboardy (np. "system look model").
- **Dalsze kroki:**
    - Należy zmienić konwencję nazewniczą tabel (np. zastąpić minus podkreślnikiem lub dodać prefiks 's').
    - Prace nad dashboardami są w toku.
    - Należy przemyśleć, czy harmonogram odświeżania źródeł systemowych powinien być edytowalny przez użytkowników (sugestia: nie, lub tylko w celu zmniejszenia częstotliwości).

---

### 10. Copilot

- **Dlaczego to robimy**
    - Rozwój funkcjonalności asystenta AI (Copilot).
- **Opis funkcjonalności / rozwiązania:**
    - Dodano możliwość przesyłania (uploadu) dokumentów (np. PDF z listą wymagań) do konwersacji. Copilot może analizować te pliki i wykorzystywać je w odpowiedziach (np. przy tworzeniu procesu).
    - Przesłane dokumenty są tymczasowe i powiązane tylko z bieżącą sesją czatu; znikają po wyczyszczeniu konwersacji.
    - Poprawiono sposób wyświetlania wywołań funkcji (function calling) – zamiast technicznej nazwy funkcji, użytkownik widzi teraz bardziej ogólny, czytelny przycisk (np. "Tworzenie nowej sprawy").
- **Dalsze kroki:**
    - Przy wywoływaniu funkcji (np. tworzeniu sprawy) należy dodać informację o _nazwie procesu_, który zostanie uruchomiony.
    - Należy dopracować scenariusz, gdy Copilot znajduje kilka pasujących procesów (np. 3 procesy obiegu faktur) – obecnie wybiera jeden lub listuje; powinno to być bardziej przewidywalne.
    - Należy przemyśleć mechanizm dłuższego przechowywania dokumentów i konwersacji (np. poprzez opcję przywracania poprzednich sesji).

---

### 11. Komunikator

- **Dlaczego to robimy**
    - Rozwój funkcjonalności komunikatora wewnętrznego.
- **Opis funkcjonalności / rozwiązania:**
    - Dodano opcję tworzenia konwersacji opartych o grupy MOD.
    - Uprawnienia do takiej konwersacji są automatycznie synchronizowane ze składem danej grupy MOD (dodawanie/usuwanie członków).
- **Dalsze kroki:**
    - [Nie sprecyzowano dalszych kroków dla tego tematu].

---

### 12. Podsumowanie Sprintu i Przebieg Spotkania

- **Dlaczego to robimy**
    - Ocena wydajności zespołu w sprincie oraz meta-dyskusja na temat formy spotkania.
- **Opis funkcjonalności / rozwiązania:**
    - W bieżącym sprincie zespół skupił się głównie na stabilizacji wersji i poprawkach błędów (bugfixing).
    - Statystyki sprintu:
        - 113 zgłoszeń zakończonych (status "Done").
        - 62 zgłoszenia czekają na testy.
        - Łącznie ok. 180 pozycji zamkniętych na etapie deweloperskim.
- **Dalsze kroki:**
    - Janusz: Należy popracować nad formułą prezentacji sprint review. Obecnie spotkanie nie przebiega płynnie, a uczestnicy są w różnym stopniu przygotowani. Prezentacja musi być "sprawna i konkretna", stanowiąc dobry materiał dla zarządu i innych działów (wdrożenia, serwis).
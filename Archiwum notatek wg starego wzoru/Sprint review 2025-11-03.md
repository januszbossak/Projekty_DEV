[[2025-11-03 poniedziałek]]
[[2025-10-06 Sprint review]]


Sprint review z dnia 3 listopada 2025

### 1. Dolny pasek nawigacji dokumentu

#### Dlaczego to robimy

Funkcjonalność została zmieniona na wniosek klientów. Poprzednio przełączanie dokumentów znajdowało się w środkowej części podglądu, teraz zostało przeniesione na dolną belkę nawigacyjną.

#### Opis funkcjonalności / rozwiązania:

- Pasek umożliwia przełączanie się między kolejnymi dokumentami na liście (nawigacja w lewo i prawo).
    
- Pliki, które nie mają podglądu (np. pliki w formacie .mkv), nie są uwzględniane w nawigacji.
    
- Wprowadzono mechanizmy odpowiedniego formatowania i przycinania nazw plików na pasku.
    
- Podczas dyskusji potwierdzono, że obsługa podglądu dla formatu .mkv nie będzie dodawana, ponieważ jest to zbyt złożony format kontenera, co mogłoby powodować problemy ze wsparciem.
    

#### Dalsze kroki:

- Nie sprecyzowano dalszych kroków dla tej funkcjonalności.
    

---

### 2. Podgląd dokumentów na raportach

#### Dlaczego to robimy

Celem było ujednolicenie podglądu raportów. Jeden ze starszych klientów (korzystający z wyszukiwania zaawansowanego) również wnioskował o dodanie funkcji przełączania się między dokumentami w tym widoku.

#### Opis funkcjonalności / rozwiązania:

- Nowy podgląd dokumentów na raportach jest wizualnie i funkcjonalnie zbliżony do podglądu na sprawie.
    
- Obejmuje m.in. paginację, te same akcje, widok pełnoekranowy i ładowanie kolejnych stron.
    

#### Dalsze kroki:

- Należy rozważyć dodanie funkcjonalności przełączania się między dokumentami (tak jak w pkt. 1).
    
- Wymaga to odtworzenia tej logiki na nowo, ponieważ komponent podglądu raportu jest oparty na innej technologii (nie-reactowej) niż podgląd sprawy.
    

---

### 3. Sortowanie na formularzu (lista pól)

#### Dlaczego to robimy

Rozbudowa funkcjonalności zarządzania polami na formularzach.

#### Opis funkcjonalności / rozwiązania:

- Dodano funkcję dodawania nowego pola poprzez okno modalne.
    
- Wprowadzono możliwość sortowania metodą "przeciągnij i upuść" (drag-and-drop) zarówno dla całych sekcji, jak i dla poszczególnych pól (w tym pól zagnieżdżonych).
    

#### Dalsze kroki:

- W bieżącym sprincie planowane jest dodanie możliwości przenoszenia pól pomiędzy różnymi sekcjami.
    
- Do listy zadań dopisano również obsługę błędów walidacji przy próbie duplikowania nazw pól.
    

---

### 4. Edycja pól na liście (formularze)

#### Dlaczego to robimy

Usprawnienie edycji pól bezpośrednio z poziomu listy, co było zgłaszane przez klientów.

#### Opis funkcjonalności / rozwiązania:

- Pola typu "static" (które mogą zawierać formatowanie) są teraz edytowalne w dedykowanym oknie modalnym, wyposażonym w edytor tekstu.
    
- Pozostałe, proste typy tekstowe (np. nazwy pól, tłumaczenia) edytuje się "inline" (bezpośrednio na liście), aby przyspieszyć pracę.
    
- Wprowadzono drobne poprawki kosmetyczne, np. ujednolicenie stylu przycisku do zmiany typu pola.
    

#### Dalsze kroki:

- Zaplanowano dalsze prace wyrównujące funkcjonalność nowej listy względem starej.
    
- Priorytetem jest dodanie brakujących informacji przy polach typu "Słownik" (wyświetlenie nazwy słownika i dodanie skrótu do jego edycji).
    

---

### 5. Repozytorium plików

#### Dlaczego to robimy

Stworzenie zupełnie nowej funkcjonalności (w ramach realizacji umowy), pozwalającej na zarządzanie plikami w sposób niezależny od spraw. W obecnym modelu pliki muszą być powiązane ze sprawą.

#### Opis funkcjonalności / rozwiązania:

- Obecnie gotowy jest zaawansowany zalążek frontendu.
    
- Frontend umożliwia przeszukiwanie struktury drzewa folderów.
    
- Udostępnia dwa tryby widoku: kafelkowy i listowy, spójne z innymi modułami (np. Procesy, Raporty).
    
- Pliki fizycznie będą przechowywane na dysku, analogicznie do obecnych załączników spraw.
    

#### Dalsze kroki:

- **Backend:** Trwa projektowanie backendu. Po analizie wymagań (m.in. przyszłej integracji ze sprawami) podjęto decyzję o zmianie koncepcji. Zamiast tworzyć zewnętrzną aplikację (jak Komunikator), repozytorium będzie wewnętrzną rozbudową Modulita, opartą o istniejące struktury.
    
- **MVP:** Pierwsza wersja produkcyjna (MVP) nie będzie zawierała integracji ze sprawami.
    
- **Plany na przyszłość:** Architektura musi być przygotowana na przyszłe rozszerzenia, takie jak: podpinanie plików z repozytorium do spraw, przenoszenie plików ze sprawy do repozytorium, czy inicjowanie sprawy na podstawie pliku z repozytorium.
    
- **Sugestie:** Podczas projektowania backendu należy uwzględnić zgłoszoną potrzebę (od klienta PKF) dotyczącą możliwości definiowania ścieżki przechowywania plików per proces.
    

---

### 6. Copilot - eksport plików

#### Dlaczego to robimy

Rozszerzenie możliwości Copilota o generowanie plików.

#### Opis funkcjonalności / rozwiązania:

- Copilot potrafi teraz eksportować wyniki zapytań do plików.
    
- Użytkownik może poprosić np. "Wyeksportuj mi listę procesów związanych z OCR".
    
- Wygenerowany plik można pobrać w formacie Word lub Markdown.
    

#### Dalsze kroki:

- Nie sprecyzowano w transkrypcji.
    

---

### 7. Copilot - dostęp do spraw

#### Dlaczego to robimy

Umożliwienie Copilotowi wyszukiwania informacji bezpośrednio w sprawach.

#### Opis funkcjonalności / rozwiązania:

- Jest to obecnie wersja MVP (Proof of Concept).
    
- Copilot może wykonywać zapytania do spraw, np. "Znajdź mi faktury z OCR fau 3, gdzie nabywca to Sedeka".
    
- W odpowiedzi zwraca listę pasujących spraw, a użytkownik może poprosić o nawigację do konkretnego wyniku (np. "przejdź do drugiej").
    

#### Dalsze kroki:

- Funkcjonalność musi uwzględniać uprawnienia zalogowanego użytkownika.
    
- Docelowe rozwiązanie techniczne ma działać inaczej – poprzez dynamiczne tworzenie tymczasowych raportów na podstawie zapytania użytkownika.
    

---

### 8. Billing - podgląd logów OCR

#### Dlaczego to robimy

Ułatwienie diagnostyki problemów z OCR. Wcześniej dostęp do tych logów wymagał bezpośredniego dostępu do bazy danych.

#### Opis funkcjonalności / rozwiązania:

- W module bilingowania dodano możliwość podglądu pełnych logów (wyniku JSON) zwróconych przez usługę OCR dla danego dokumentu.
    
- Pozwala to na szybką weryfikację, dlaczego np. jakaś dana nie została odczytana.
    

#### Dalsze kroki:

- Nie sprecyzowano w transkrypcji.
    

---

### 9. Bezpieczeństwo danych w bilingu OCR/AI

#### Dlaczego to robimy

Podczas spotkania zidentyfikowano wysokie ryzyko związane z przechowywaniem wrażliwych danych w bazie bilingowej. Dane te (pełne odczyty z OCR, odpowiedzi AI) mogą zawierać dane osobowe, tajemnice handlowe itp.

#### Opis funkcjonalności / rozwiązania:

- Obecnie nie ma dedykowanych rozwiązań; dyskusja dotyczyła zidentyfikowanego problemu.
    

#### Dalsze kroki:

- Temat został "zaparkowany" jako pilny do szczegółowego omówienia.
    
- Sugerowane kierunki działań:
    
    - Wprowadzenie szyfrowania danych wrażliwych w bazie bilingowej (potencjalnie z osobnym kluczem szyfrowania dla każdej firmy).
        
    - Rozważenie wprowadzenia polityki retencji dla tych danych.
        
    - Rozważenie zmiany architektury (szczególnie dla klientów premium): dane bilingowe (np. "firma X przetworzyła Y dokumentów") byłyby u nas, ale pełne, wrażliwe logi OCR/AI zapisywałyby się wyłącznie w bazie danych klienta. Zmniejszyłoby to ryzyko wycieku danych.
        

---

### 10. Strona Bazy Wiedzy (Frontend)

#### Dlaczego to robimy

Stary frontend Bazy Wiedzy (używanej przez Copilota) był w dużej mierze wygenerowany przez AI i nie spełniał standardów bezpieczeństwa i wydajności. Wymagał przepisania i ujednolicenia z nowym design systemem.

#### Opis funkcjonalności / rozwiązania:

- Przemek przepisał stronę Bazy Wiedzy na nowo, zgodnie z aktualnymi standardami.
    
- Nowy schemat strony jest identyczny jak inne nowe widoki (np. Słowniki, Obszary) i posłuży jako szablon dla kolejnych stron administracyjnych.
    

#### Dalsze kroki:

- Funkcjonalność nie została zaprezentowana (developer miał ją lokalnie). Zostanie pokazana przy innej okazji.
    

---

### 11. Edytor graficzny formularzy

#### Dlaczego to robimy

Kontynuacja prac nad edytorem graficznym, mająca na celu wyrównanie jego możliwości ze starym edytorem (listą pól) i dodanie usprawnień.

#### Opis funkcjonalności / rozwiązania:

- Dodano nową funkcjonalność: sortowanie całych sekcji metodą "przeciągnij i upuść" (drag-and-drop).
    
- Podczas przenoszenia sekcji, jej zawartość jest automatycznie zwijana, aby ułatwić operację.
    

#### Dalsze kroki:

- Dalsze prace wyrównawcze nad edytorem graficznym i listą pól będą kontynuowane w bieżącym sprincie.
    

---

### 12. Rozbudowa Rest API - przesyłanie dużych plików

#### Dlaczego to robimy

Pojawiła się potrzeba biznesowa przesyłania przez API bardzo dużych plików (kilkaset MB do >1 GB). Dotychczasowa metoda (kodowanie Base64 w JSON) powodowała błędy serializacji przy tak dużych rozmiarach.

#### Opis funkcjonalności / rozwiązania:

- Stworzono nowy endpoint API.
    
- Przesyłanie plików odbywa się teraz z wykorzystaniem `form-data` (zamiast JSON).
    
- Maksymalny rozmiar pliku jest teraz ograniczony jedynie ustawieniami serwera IIS (np. `maxRequestLength`), a nie przez serializator.
    
- Wyjaśniono, że parametr systemowy `pdfmaxsize` nie jest związany z limitem wgrywania, a jedynie z mechanizmem optymalizacji (downscalingu) skanów PDF.
    

#### Dalsze kroki:

- Wdrożeniowiec/programista korzystający z API musi teraz wybrać metodę: małe pliki mogą nadal być przesyłane w JSON, ale duże muszą być wysyłane przez nowy endpoint (jako `form-data`). Zazwyczaj wymaga to dwóch wywołań (np. jedno do utworzenia sprawy, drugie do wgrania pliku).
    
- W bieżącym kwartale zostanie zaktualizowana dokumentacja API, aby precyzyjnie opisać oba mechanizmy i wyjaśnić znaczenie parametrów konfiguracyjnych IIS.
    

---

### 13. Narzędzie do wczytywania maili (debugowanie)

#### Dlaczego to robimy

Ułatwienie pracy testerom i serwisowi w diagnozowaniu problemów z wczytywaniem maili.

#### Opis funkcjonalności / rozwiązania:

- Stworzono narzędzie (dostępne z poziomu GUI), które pozwala na ręczne wczytanie pliku .eml.
    
- Narzędzie wywołuje tę samą metodę przetwarzania maila, która jest używana przez job.
    
- Jeśli wystąpi błąd przetwarzania, zostanie on zalogowany w taki sam sposób, jak zrobiłby to automatyczny job.
    

#### Dalsze kroki:

- Nie sprecyzowano w transkrypcji.
    

---

### 14. Historia logowania wysłanych maili (ze sprawy)

#### Dlaczego to robimy

Zapotrzebowanie biznesowe (zgłoszone przez WIM) na możliwość śledzenia historii maili wysłanych w kontekście konkretnej sprawy.

#### Opis funkcjonalności / rozwiązania:

- Z poziomu sprawy dostępna jest nowa zakładka/funkcja pokazująca historię wysłanych maili.
    
- W obecnej, pierwszej wersji (MVP), system loguje jedynie fakt _dodania maila do kolejki wysyłkowej_.
    

#### Dalsze kroki:

- W bieżącym sprincie zostanie zrealizowane zadanie uzupełniające.
    
- Do logów zostanie dodany znacznik potwierdzający, że mail został _faktycznie wysłany_ z kolejki przez job (co uwzględni np. ustawienia użytkownika, który otrzymuje powiadomienia zbiorczo raz dziennie).
    
- Historia ta będzie przechowywana na stałe, niezależnie od standardowych logów systemowych.
    

---

### 15. Powiadomienia o błędach wczytywania maili (OCR)

#### Dlaczego to robimy

Podczas spotkania zgłoszono krytyczny problem klienta, któremu gubiły się faktury (maile nie były wczytywane, np. z powodu błędnego formatu PDF), co generowało problemy z płatnościami. Klient nie otrzymywał żadnej informacji o błędzie.

#### Opis funkcjonalności / rozwiązania:

- Podczas dyskusji ustalono, że system "od zawsze" posiada mechanizm do obsługi takich sytuacji.
    
- W ustawieniach systemowych istnieje parametr (`Send information about invalid mail to this address`).
    
- Jeśli job pobierze maila, ale nie uda mu się utworzyć sprawy (z dowolnego powodu), system wyśle powiadomienie o błędzie na adresy e-mail wpisane w tym polu (można podać wiele adresów rozdzielonych średnikiem).
    

#### Dalsze kroki:

- Problem polegał na tym, że funkcjonalność ta nie była znana działom wdrożeń i serwisu.
    
- Należy pilnie skonfigurować ten parametr u klienta, który zgłaszał problem.
    
- Należy zaktualizować wewnętrzną dokumentację (np. dotyczącą konfiguracji "twórz sprawę z maila").
    
- W bieżącym kwartale opisy w ustawieniach systemowych zostaną poprawione na bardziej biznesowe i zrozumiałe, aby uniknąć takich sytuacji w przyszłości (z wykorzystaniem istniejącego mechanizmu tłumaczeń YAML).
    

---

### 16. Trust Center - przenoszenie jobów (Blockchain)

#### Dlaczego to robimy

Optymalizacja działania Trust Center. Zidentyfikowano problemy z działaniem blockchaina (pojawiały się bloki poza głównym łańcuchem).

#### Opis funkcjonalności / rozwiązania:

- Rozpoczęto proces przenoszenia jobów (na początek job blockchaina) z projektu webowego.
    
- Joby będą teraz zarządzane i wykonywane przez dedykowaną usługę Windows, analogicznie do jobów w Modulicie.
    

#### Dalsze kroki:

- Nie sprecyzowano w transkrypcji.
    

---

### 17. Poprawki i Raporty systemowe

#### Dlaczego to robimy

Bieżące prace rozwojowe i utrzymaniowe.

#### Opis funkcjonalności / rozwiązania:

- Ania realizowała w sprincie dużą liczbę poprawek błędów.
    
- Prace nad raportami systemowymi (prowadzone wspólnie z Łukaszem B.) były chwilowo wstrzymane z powodu jego nieobecności, ale zostaną wznowione.
    
- Prace nad tłumaczeniami zostały wstrzymane na rzecz poprawek o wyższym priorytecie.
    

#### Dalsze kroki:

- Kontynuacja prac nad raportami systemowymi.
    

---

### 18. Dynamiczne źródła danych

#### Dlaczego to robimy

Przetestowanie istniejącej funkcjonalności dynamicznych źródeł danych w rzeczywistych warunkach wdrożeniowych ("przełożenie teorii na praktykę").

#### Opis funkcjonalności / rozwiązania:

- Funkcjonalność została przetestowana "w boju" na konkretnych potrzebach wdrożeniowych.
    
- Testy pozwoliły na identyfikację i rozwiązanie kilku dodatkowych aspektów, które usprawnią przyszłe prace wdrożeniowe.
    

#### Dalsze kroki:

- Nie sprecyzowano w transkrypcji.
    

---

### 19. API E-Doręczeń

#### Dlaczego to robimy

Rozwiązanie problemów zgłaszanych przez klientów.

#### Opis funkcjonalności / rozwiązania:

- Udało się ustabilizować działanie API E-Doręczeń; błędy u klientów nie powinny już występować.
    

#### Dalsze kroki:

- Osobny problem, dotyczący paczkowania w N-Dawca (inna usługa), jest nadal analizowany.
    

---

### 20. Aplikacja do podpisywania (MacOS/Szafir)

#### Dlaczego to robimy

Rozwój konektora podpisów, w tym wprowadzenie nowego interfejsu użytkownika i wsparcia dla M Szafir na MacOS.

#### Opis funkcjonalności / rozwiązania:

- Integracja z M Szafir na MacOS działa i jest obecnie w fazie testów.
    
- Rozpoczęto prace nad całkowicie nowym wyglądem (UI) aplikacji do podpisywania dokumentów (QES).
    
- Jako technologię dla nowej aplikacji wybrano MAUI .NET (następcę Xamarina).
    

#### Dalsze kroki:

- Ciekawsza demonstracja funkcjonalności (nowego UI) powinna być gotowa za 2 tygodnie.
    
- Adrian ma w planach także wsparcie dla podpisów PWPW oraz Enigma.
    
- Aby usprawnić proces testowania i uniezależnić Adriana od innych osób, podjęto decyzję o zakupie dla niego certyfikatu M Szafir.
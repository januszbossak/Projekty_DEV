# Notatka projektowa – 2025-08-26 – AMODIT UI

**Data:** 2025-08-26
**Temat główny:** Przegląd nowości w AMODIT do przygotowania artykułu informacyjnego

**Powiązane projekty:**
- `moduly/Copilot-Baza-wiedzy-AI` – funkcjonalności 1, 12
- `cross-cutting/Zakladka-Raporty` – funkcjonalność 2
- `cross-cutting/Zakladka-Procesy` – funkcjonalność 3
- `moduly/Ustawienia-systemowe` – funkcjonalność 4
- `cross-cutting/Bezpieczenstwo-sesji` – funkcjonalność 5
- `cross-cutting/Interfejs-sprawy` – funkcjonalności 6, 7, 8, 9
- `cross-cutting/WCAG` – funkcjonalność 10
- `cross-cutting/Automatyzacja-dokumentacji-AI` – funkcjonalność 11
- `moduly/Modul-raportowy` – funkcjonalność 13
- `moduly/Zrodla-danych` – funkcjonalność 14
- `moduly/Edytor-procesow-formularzy` – funkcjonalność 15

---

## 1. AMODIT Copilot – zastosowania i funkcjonalności

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`
**Komponent:** Copilot / AI

### Cel i problem

AMODIT Copilot jest jednym z elementów zastosowania sztucznej inteligencji w AMODIT, obok funkcji Ask AI i inteligentnego OCR. Copilot ma wspierać użytkowników, twórców procesów i ogólnie użytkowników AMODIT w różnych obszarach systemu.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

AMODIT Copilot oferuje następujące zastosowania:

**1. Tworzenie nowych procesów:**
- Generowanie procesu na podstawie opisu słownego
- Efekt: szkic diagramu oraz szkic formularza
- Proces wielokrokowy (konwersacja, nie jeden prompt)
- Możliwość poprawiania na bieżąco, dopóki jest szkic
- Zatwierdzenie powoduje utworzenie procesu w AMODIT
- Proces powstaje "w pełni" – z nazwami etapów, tłumaczeniami, opisami (uwalnia konsultanta od tworzenia wielu dodatkowych elementów)

**2. Opis biznesowy procesu:**
- Możliwość zapytania: "Opisz mi biznesowo, jak działa proces obiegu faktur"
- Copilot analizuje definicję procesu i przedstawia opis biznesowy: po co jest proces, jak działa, jakie ma kroki, jakie dane są przyjmowane na których etapach

**3. Pomoc w tworzeniu i edytowaniu reguł:**
- W edycji reguły można poprosić Copilota o opracowanie reguły
- Można zadać temat biznesowy z przykładami, a Copilot opracuje regułę w języku skryptowym AMODIT
- Działa na poziomie pojedynczej reguły (nie analizuje zbiorczo zależności między regułami)
- Może też opisać istniejącą regułę (np. "Napisz mi, co robi ta reguła" – otrzymujemy pełen opis)

**4. Wsparcie dla zwykłych użytkowników:**
- Copilot zna procesy i raporty w danym systemie
- Użytkownik może zapytać: "Mam do rozliczenia delegację, którego procesu powinienem użyć?"
- Copilot analizuje dostępne procesy, wskazuje odpowiedni i może uruchomić sprawę
- Podobnie z raportami: "Chciałbym przeanalizować raport sprzedażowy, z którego powinienem skorzystać?"

**5. Wiedza o AMODIT:**
- Copilot ma zawartą w sobie praktycznie całą wiedzę dostępną na Wiki AMODIT (pełna dokumentacja)
- Ma pełną wiedzę na temat wszystkich funkcji używanych w skryptach (z kodu źródłowego AMODIT)
- Może odpowiadać na ogólne pytania dotyczące systemu

**6. Baza wiedzy organizacji (warstwa prywatna):**
- Klienci mogą wrzucać do "Bazy Wiedzy" swoją wiedzę – regulaminy, instrukcje, opracowania
- Wiedza nie wychodzi poza organizację
- Użytkownicy mogą zadawać pytania dotyczące regulaminu (np. "Jak należy zorganizować i zabezpieczyć transport materiałów?")
- Przykładowe zastosowanie: dział HR buduje bazę wiedzy, żeby pracownicy najpierw zadawali pytania do Copilota, a dopiero jak nie znajdą odpowiedzi, zgłaszali się bezpośrednio do działu

**Ograniczenia:**
- AMODIT Copilot nie ma dostępu do danych transakcyjnych (pracownik nie może zapytać: "Ile jeszcze zostało mi urlopu?" lub "Ile muszę rozliczyć zaliczki?")
- W przyszłych wersjach dostęp do danych transakcyjnych będzie włączalny per organizacja (kwestie polityki bezpieczeństwa)
- Częściowo możliwe już teraz przez funkcję `AddToKnowledgeBase` na poziomie reguł (twórca procesu może dodać informacje ze sprawy do bazy wiedzy, ale odpowiedzialność za dane spoczywa na twórcy)

**Plany na przyszłość:**
- Projekt badawczy: Copilot jako "konsultant" – będzie miał większą wiedzę, będzie wcześniej dopytywał, sprawdzał czy specyfikacja procesu jest pełna
- Wyciąganie danych dla konkretnego użytkownika zgodnie z jego uprawnieniami (planowane na przyszłość)

**Szczegóły techniczne:**
- Funkcja `AddToKnowledgeBase` – możliwość dodawania informacji ze sprawy do bazy wiedzy
- Modele typu "embedding" wykorzystywane w bazie wiedzy (tańsze, służą do tworzenia bazy wektorowej)
- Kierunek strategiczny: "AI Driven Workflow" – wiele elementów AMODIT ma być wspieranych przez AI w sposób świadomy

### Ograniczenia / Poza zakresem

- Brak dostępu do danych transakcyjnych w obecnej wersji
- Analiza zbiorcza zależności między regułami (działa tylko na poziomie pojedynczej reguły)
- Funkcja "konsultant" – projekt badawczy na przyszłość

### Punkty otwarte

- Kiedy dokładnie będzie dostępny dostęp do danych transakcyjnych per organizacja?
- Jak będzie działać mechanizm wyciągania danych dla konkretnego użytkownika zgodnie z jego uprawnieniami?

---

## 2. Nowy wygląd listy raportów

**Projekt:** `cross-cutting/Zakladka-Raporty`
**Komponent:** Zakładka Raporty (menu główne)

### Cel i problem

Usprawnienie zarządzania i odnajdywania raportów poprzez nowy format wyświetlania, bardziej ergonomiczne kafelki oraz nowe widoki z dodatkowymi metadanymi. Szczególnie przydatne z perspektywy administratorów systemu czy procesów.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowe formaty wyświetlania:**
- Kafelki bardziej ergonomiczne i nowocześniejsze
- Nowy widok listy z dodatkowymi metadanymi (ułatwia zarządzanie i odnajdywanie raportów)
- Dwa typy list: zwykła i kompaktowa (pozwala zobaczyć więcej elementów na jednym ekranie)
- Na liście widać opisy raportu (łatwiej się zorientować, do czego służy)

**Nowe sposoby sortowania i filtrowania:**
- Zapamiętywanie filtrowania w ramach obszarów w menu Raporty (per użytkownik)
- Wizualne rozróżnianie raportów poprzez reprezentację każdego typu raportu odpowiednią ikoną
- Nowe sposoby filtrowania:
  - Raporty, które ja utworzyłem
  - Raporty utworzone przez kogokolwiek innego
  - Ostatnio modyfikowane
  - Określone typy raportów (np. kolumnowy, pivot)
- Szukanie raportu po jego źródle (np. proces "Obieg faktur" lub "Kandydaci")

**Szczegóły techniczne:**
- Obszary przepisane na nową technologię frontendową – React
- Podział na czysty backend i frontend (łatwiejsza konserwacja, łatwiejsza modyfikacja elementów frontendowych)
- Poprawiona wydajność ładowania list

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 3. Nowy wygląd listy procesów

**Projekt:** `cross-cutting/Zakladka-Procesy`
**Komponent:** Zakładka Procesy (menu główne)

### Cel i problem

Usprawnienie nawigacji i odnajdywania procesów poprzez nowy format wyświetlania oraz wprowadzenie modala pośredniego wspierającego wdrażanie nowych procesów.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowy format wyświetlania:**
- Wydzielone ulubione, potem pozostałe
- Widok listy kafelkowej oraz listy kompaktowej
- Po prawej stronie od nazwy procesu może znajdować się opis (co ułatwia orientację)

**Modal pośredni:**
- Przed uruchomieniem sprawy pojawia się modal z opisem procesu (jeśli administrator zdefiniował opis)
- Modal może zawierać dowolną ilość kluczowych informacji merytorycznych
- Użytkownik może zaznaczyć, żeby modal więcej się nie pokazywał (jeśli proces jest mu znany)
- Dopiero po pojawieniu się modala można uruchomić sprawę

**Szczegóły techniczne:**
- Obszary przepisane na React
- Opisy dostępne z poziomu kafelków czy listy

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 4. Ustawienia systemowe – nowy interfejs

**Projekt:** `moduly/Ustawienia-systemowe`
**Komponent:** Interfejs ustawień

### Cel i problem

Przepisanie frontu ustawień systemowych na nową technologię Reactową w celu poprawy nawigacji i łatwiejszego znajdowania konkretnych ustawień.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowy interfejs:**
- Przepisanie frontu na React
- Nie wszystkie ekrany są jeszcze pokryte w tym wydaniu (kluczowe poszły w pierwszej kolejności, kolejne będą uzupełniane)
- Nawigacja po ustawieniach stała się wygodniejsza, łatwiej znaleźć konkretne ustawienie

**Kompatybilność wsteczna:**
- Zachowana pełna kompatybilność wsteczna
- Ponieważ nie wszystko jest pokryte, zawsze można wrócić do poprzedniej wersji
- Administratorowi najpierw wyświetlą się nowe ustawienia Reactowe
- Jeżeli jakaś funkcjonalność nie będzie dostępna, w każdej chwili można wrócić do dotychczasowych
- W pierwszej kolejności korzystanie z nowych, w ciągu następnych dwóch wydań pełne przejście na wersję Reactową

**Szczegóły techniczne:**
- Odbiorcy: ograniczone grono administratorów
- Technologia: React

### Ograniczenia / Poza zakresem

- Nie wszystkie ekrany są jeszcze pokryte (kolejne będą uzupełniane w następnych wydaniach)

### Punkty otwarte

- Które dokładnie ekrany są jeszcze niepokryte?
- Kiedy dokładnie nastąpi pełne przejście na wersję Reactową?

---

## 5. Nowe okno logowania

**Projekt:** `cross-cutting/Bezpieczenstwo-sesji`
**Komponent:** Logowanie

### Cel i problem

Odświeżenie okna logowania dla użytkowników niekorzystających z SSO (Active Directory) oraz usprawnienie dla użytkowników posiadających więcej niż jedno konto.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowe okno logowania:**
- Odświeżone okno logowania dla użytkowników niekorzystających z SSO (Active Directory)
- Po prostu ładniejsze

**Usprawnienie dla użytkowników z wieloma kontami:**
- Po uwierzytelnieniu użytkownicy z więcej niż jednym kontem przechodzą na nowy ekran w formie kafelkowej
- Zestawione w ładny sposób swoje konta powiązane np. z danym adresem mailowym
- Łatwo rozróżnić login, stanowisko, dział
- W górnym menu (tam gdzie imię i nazwisko) można w łatwy sposób przełączyć się na inne konto
- Nie trzeba się wylogowywać całkowicie – można przełączyć się w inny kontekst (np. na konto z innej spółki, innego oddziału czy na inną rolę – między administratorem a użytkownikiem)

**Przypadki użycia:**
- Firmy wielooddziałowe
- Grupy firm
- Osoby zatrudnione w odrębnych jednostkach
- Osoby, które są jednocześnie zaangażowane w procesy biznesowe i są administratorami (zalecane posiadanie dwóch odrębnych kont)

**Szczegóły techniczne:**
- Ekran kafelkowy z kontami powiązanymi z adresem mailowym

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 6. Nowe menu po lewej stronie

**Projekt:** `cross-cutting/Interfejs-sprawy`
**Komponent:** Menu nawigacyjne

### Cel i problem

Zmiana wyglądu i ergonomii menu po lewej stronie, wprowadzenie nowych funkcjonalności ułatwiających nawigację oraz reorganizacja pozycji menu.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowe funkcjonalności:**
- Okienko wyszukiwania z pozycji menu
- Zarządzanie obszarami przeniesione na górę (obok wyszukiwania)
- Cały boczny panel menu można zwijać, żeby mieć więcej przestrzeni roboczej (pozostaje dostępny w formie kafelków/ikon)

**Reorganizacja pozycji:**
- Wydzielona zakładka "Do wykonania" poza obszary (agreguje wszystkie sprawy przypisane do użytkownika ze wszystkich obszarów)
- Przeniesione "Powiadomienia" z górnego paska do lewego menu (pod zakładkę "Do wykonania") – użytkownicy widzą tam np. wzmianki w komentarzach, powinny być bardziej widoczne
- Podział na:
  - Listy spraw: np. "Mój zespół", "Wszystkie"
  - Przypięte: raporty przypięte przez twórcę lub użytkownika
  - Linki: aplikacje zewnętrzne podpięte do AMODIT
  - Moduły: osobna sekcja, np. Nadawca, Przelewy

**Szczegóły techniczne:**
- Zakładka "Do wykonania" na samej górze agreguje wszystkie sprawy przypisane do użytkownika
- Wewnątrz obszarów nadal mogą być lokalne zakładki "Do wykonania" filtrujące zadania tylko z tego obszaru

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 7. Nowy wygląd formularza sprawy

**Projekt:** `cross-cutting/Interfejs-sprawy`
**Komponent:** Formularz sprawy

### Cel i problem

Odświeżenie layoutu formularza sprawy, zwiększenie przestrzeni na sam formularz oraz poprawa designu przycisków, aby nie odwracały uwagi od merytoryki.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Zmiany w layoutcie:**
- Odświeżenie layoutu, więcej przestrzeni na sam formularz
- Menu nawigacyjne po opcjach sprawy zostało przeniesione z góry na prawą pionową belkę

**Poprawki designu przycisków:**
- Ujednolicone przyciski (białe tło, szara ramka)
- Kolory są tylko na ikonach (mniej jaskrawe przyciski mniej męczą wzrok i nie odwracają uwagi od pól wymaganych)

**Pola wymagane:**
- Pola wymagane są oznaczone delikatną pomarańczową linią na dolnej krawędzi
- Jeśli użytkownik pominie pole i spróbuje zapisać lub przekazać sprawę, system wyraźnie poinformuje o braku wypełnienia odpowiednim dopiskiem pod polem

**Konfiguracja lokalizacji paska przycisków:**
- Lokalizacja paska przycisków jest konfigurowalna per użytkownik
- Jeśli ktoś woli mieć przyciski na dole (bo czyta sprawę i na dole podejmuje decyzję), może to zmienić w ustawieniach

**Powiadomienia systemowe:**
- Powiadomienia systemowe do sprawy (powiązane sprawy, niekompletny formularz, priorytety) zostały poprawione wizualnie i znajdują się na górze pod przyciskami

**Szczegóły techniczne:**
- Wygląd jest lżejszy, bardziej delikatny

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 8. Nowy wygląd prawego panelu sprawy

**Projekt:** `cross-cutting/Interfejs-sprawy`
**Komponent:** Prawy panel sprawy

### Cel i problem

Odświeżenie wyglądu prawego panelu (podgląd dokumentu, lista załączników, informacje o sprawie, diagram, historia) oraz rozdzielenie funkcjonalności uprawnień.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowy wygląd:**
- Wszystkie panele zostały przebudowane, są lżejsze i w jednolitej tonacji

**Rozdzielenie funkcjonalności uprawnień:**
- Osobny prawy panel dla właścicieli i obserwatorów

**Panel "Informacje o sprawie":**
- Zyskał więcej szczegółów: stan sprawy, od kogo przyszła, kiedy, kto modyfikował

**Szczegóły techniczne:**
- Panele: podgląd dokumentu, lista załączników, informacje o sprawie, diagram, historia

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 9. Nowy wygląd tabeli na formularzu sprawy

**Projekt:** `cross-cutting/Interfejs-sprawy`
**Komponent:** Tabela na formularzu

### Cel i problem

Odświeżenie wyglądu tabeli w tradycyjnym układzie kolumnowym oraz w postaci kafelków, zmniejszenie liczby niepotrzebnych elementów oraz personalizacja nazw przycisków.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Nowy wygląd tabeli:**
- Odświeżony wygląd tabeli w tradycyjnym układzie kolumnowym oraz w postaci kafelków
- Zmniejszona liczba niepotrzebnych elementów, tabela jest czystsza
- Zmieniony wygląd podformularzy

**Personalizacja nazw przycisków:**
- Możliwość personalizacji nazwy przycisku "Dodaj" – zamiast ogólnego "Dodaj", twórca procesu może wpisać np. "Dodaj nowego członka rodziny"
- Analogiczne rozwiązanie na poziomie raportów – można zdefiniować nazwę przycisku tworzenia nowej sprawy, np. "Dodaj nowy wniosek urlopowy" czy "Dodaj nową fakturę"

**Zmiana miejsca importu danych:**
- Import danych do tabeli jest teraz przy dodawaniu nowych wierszy (menu kontekstowe przy przycisku "Dodaj"), a nie ukryte w "hamburgerze"
- Można dodać wiele wierszy naraz lub zaimportować wsad z Excela

**Szczegóły techniczne:**
- Menu kontekstowe przy przycisku "Dodaj"
- Import z Excela

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 10. WCAG – dostępność

**Projekt:** `cross-cutting/WCAG`
**Komponent:** Dostępność interfejsu

### Cel i problem

Zapewnienie zgodności z normami dostępności WCAG 2.1 AA oraz umożliwienie korzystania z systemu osobom z niepełnosprawnościami, w szczególności osobom korzystającym z czytników ekranowych.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Dwie perspektywy dostępności:**

**1. Tryb wysokiego kontrastu:**
- Wyczernienie kluczowych treści (przyciski, podtytuły)
- Obramowanie elementów przy najeżdżaniu (zamiast słabo widocznego podświetlenia)
- Działa na ekranie głównym i na sprawie
- Opcja włączana w ustawieniach konta

**2. Tryb uproszczonego widoku sprawy:**
- Zmieniona nawigacja
- Ważny dla osób korzystających z czytników ekranowych (VoiceOver itp.)
- Żeby czytnik mógł opowiedzieć, co jest na ekranie, widok musi być prosty

**Deklaracja zgodności:**
- Do tej wersji zostanie wydana deklaracja zgodności ze standardem WCAG 2.1 AA

**Nawigacja klawiaturą:**
- Poruszanie się po ekranie zostało dostosowane do norm
- Nawigacja klawiaturą (Tab, Shift+Tab, strzałki) zamiast myszki, pozwalająca na pełne procesowanie formularza

**Szczegóły techniczne:**
- Opcja włączana na poziomie użytkownika (każdy może sobie włączyć taki tryb, a pozostali mogą korzystać z normalnego wyglądu)
- Standard: WCAG 2.1 AA

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 11. Ask AI – funkcja AI na poziomie sprawy

**Projekt:** `cross-cutting/Automatyzacja-dokumentacji-AI`
**Komponent:** Ask AI

### Cel i problem

Otwarcie możliwości korzystania ze sztucznej inteligencji na poziomie pojedynczej sprawy, umożliwienie analizy dokumentów i danych ze sprawy przez AI.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Funkcjonalność Ask AI:**
- Otwiera możliwości korzystania ze sztucznej inteligencji na poziomie pojedynczej sprawy
- Twórca procesu może wprowadzić do tej funkcji dowolną informację ze sprawy, np. treść dokumentu

**Przykłady zastosowań:**
- Analiza zapytań ofertowych: przychodzi zapytanie, jest poddawane OCR, tekst (razem ze specjalnym promptem) trafia do funkcji Ask AI, uzyskujemy ustrukturyzowaną odpowiedź (kluczowe daty, kwoty) oraz subiektywną ocenę AI – czy zapytanie jest dla nas interesujące
- Analiza umów, regulaminów
- Wstępna analiza CV kandydatów (sprawdzenie zgodności z oczekiwaniami, np. staż pracy, kwalifikacje)

**Mechanizm:**
- Trochę jak pytanie ChatGPT "masz tu dokument i zrób z nim to", ale dzieje się to automatycznie w procesie

**Modele dostępne:**
- Możliwość korzystania ze wszystkich modeli dostępnych na platformie Microsoft Azure
- Dostępne są najnowsze modele GPT-4o, GPT-3.5, wersje mini, nano

**Bezpieczeństwo:**
- To nie jest ten sam model co publiczny ChatGPT
- Dane są przetwarzane przez Microsoft na terytorium Unii Europejskiej
- Microsoft zapewnia, że dane nie są wykorzystywane do trenowania modelu ani przechowywane (poza krótką historią konwersacji)

**Rozliczanie:**
- Klient nie musi tego opłacać osobno u dostawcy, rozlicza się z nami za użycie
- Pakiet darmowy na start, potem pay-as-you-go

**Szczegóły techniczne:**
- Integracja z Microsoft Azure
- Modele: GPT-4o, GPT-3.5, wersje mini, nano
- Przetwarzanie danych na terytorium Unii Europejskiej

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 12. AMODIT AI OCR – rozbudowany OCR

**Projekt:** `moduly/Copilot-Baza-wiedzy-AI`
**Komponent:** OCR

### Cel i problem

Rozbudowa funkcjonalności OCR w kontekście AI Driven Workflow, umożliwienie odczytywania danych z różnych typów dokumentów (faktury, paragony, dokumenty kadrowe, umowy) oraz odczytywanie niestandardowych informacji.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Potężne narzędzie w kontekście AI Driven Workflow:**
- Potrzebujemy odczytać dane z faktury czy paragonu
- Istnieją modele specjalizowane, ale bywają nieskuteczne
- Dorobiono "pre-processing" i "post-processing"

**Pre-processing:**
- Wykrywanie typu dokumentu (faktura czy paragon)
- Używanie odpowiedniego modelu w zależności od typu dokumentu

**Post-processing:**
- Jeśli standardowy OCR nie odczyta jakiejś informacji (np. daty sprzedaży), dopytujemy inny model (np. GPT-4o mini)

**Nowa funkcjonalność – odczytywanie niestandardowych informacji:**
- Możliwość poproszenia OCR o odczytanie niestandardowych informacji, których zwykły OCR nie czyta
- Przykłady:
  - Numer VIN samochodu z faktury
  - Dane z paszportu krowy (dla firm z branży hodowlanej) – rozczytać paszport i wyciągnąć dane do rejestracji zwierzęcia
  - Dokumenty kadrowe, umowy

**Modele:**
- Możliwość korzystania z modeli specjalizowanych (np. do dowodów osobistych, mandatów)
- Możliwość korzystania z ogólnych modeli LLM, którym dynamicznie mówimy, co mają odczytać
- Modele trenowane są lepsze przy dużej skali (dziesiątki tysięcy dokumentów), ale przy mniejszej skali modele ogólne świetnie sobie radzą

**E-teczki (elektroniczna dokumentacja pracownicza):**
- Oferowane kompleksowe rozwiązanie: e-teczka z rozczytywaniem i klasyfikacją dokumentów
- System na podstawie danych z dokumentu wie, w którym miejscu teczki go zarejestrować

**Szczegóły techniczne:**
- Pre-processing: wykrywanie typu dokumentu
- Post-processing: dopytanie innego modelu (np. GPT-4o mini)
- Modele specjalizowane i ogólne LLM
- Integracja z e-teczkami

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 13. Obszar raportów – seria usprawnień

**Projekt:** `moduly/Modul-raportowy`
**Komponent:** Raporty

### Cel i problem

Seria usprawnień w module raportowym przepisanym na nową technologię, w tym gradienty kolorów, filtry wymagane i domyślne, oraz usprawnienia podpisywania z poziomu raportów.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Moduł raportowy w nowej technologii – nowinki:**

**1. Gradienty kolorów:**
- W raportach typu pivot można ustawić kolory dla wartości (np. najwyższe zielone, najniższe czerwone)

**2. Filtry wymagane:**
- Użytkownik nie zobaczy raportu, dopóki nie wybierze wartości w filtrze (np. konkretnego procesu)
- Zapobiega to szumowi informacyjnemu (wyświetlaniu danych ze wszystkich procesów naraz)

**3. Filtry z wartością domyślną:**
- Twórca ustawia np. bieżący rok, ale użytkownik może to zmienić

**4. Filtr zakresu dat:**
- Możliwość ustawienia przedziału "od-do" w ramach jednego filtru (wcześniej trzeba było robić dwa osobne)

**5. Przycisk "Wyczyść filtr użytkownika":**
- Resetuje ustawienia filtrów

**6. Przycisk "Zastosuj":**
- Wprowadzony we wszystkich typach filtrów (bardziej intuicyjne dla użytkowników)

**Usprawnienie podpisywania z poziomu raportów:**
- Jeśli na formularzu jest kilka pól z dokumentami, a na raporcie wyświetlamy je w kolumnach, teraz możemy wskazać, która konkretnie kolumna ma podlegać podpisywaniu (żeby nie podpisywać wszystkich załączników ze sprawy naraz)

**Szczegóły techniczne:**
- Moduł raportowy przepisany na nową technologię
- Filtry wymagane i domyślne
- Filtr zakresu dat (od-do w jednym filtrze)

### Ograniczenia / Poza zakresem

Brak (funkcjonalność działa zgodnie z założeniami)

### Punkty otwarte

Brak

---

## 14. Rzeczy techniczne – źródła danych, integracje, REST API

**Projekt:** `moduly/Zrodla-danych`
**Komponent:** Źródła danych / Integracje

### Cel i problem

Rozszerzenie możliwości zasilania źródeł danych oraz wprowadzenie bibliotek funkcji i szablonów dokumentów poza procesami.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**1. Zasilanie danych przez REST API:**
- Do tej pory źródła zewnętrzne zasilaliśmy zapytaniami SQL
- Teraz można zasilać źródło danych, wysyłając dane do odpowiedniego endpointu REST API (z aplikacji zewnętrznej)

**2. Call Function (biblioteka funkcji):**
- Do tej pory skrypty `Call Function` były w ramach procesu
- Teraz można mieć ogólny skrypt (bibliotekę) poza procesem i używać go w wielu różnych procesach
- To samo będzie dotyczyć biblioteki szablonów dokumentów

**Szczegóły techniczne:**
- REST API endpoint do zasilania źródeł danych
- Biblioteka funkcji poza procesami
- Biblioteka szablonów dokumentów (planowana)

### Ograniczenia / Poza zakresem

- Biblioteka szablonów dokumentów jeszcze nie zaimplementowana (planowana)

### Punkty otwarte

- Kiedy dokładnie będzie dostępna biblioteka szablonów dokumentów?

---

## 15. Edytor formularza – przebudowa na React

**Projekt:** `moduly/Edytor-procesow-formularzy`
**Komponent:** Edytor Formularza

### Cel i problem

Przebudowa całego obszaru definiowania procesu na "ramę Reactową", rozpoczęcie od Edytora Formularza jako pierwszego elementu w tej wersji.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw – przegląd funkcjonalności już zaimplementowanych.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Zupełnie nowy projekt oparty na feedbacku klientów:**

**Układ:**
- Po lewej stronie lista typów pól (przenoszenie na formularz)
- Po kliknięciu na pole na formularzu, po prawej stronie w panelu pojawiają się szczegóły i ustawienia tego pola

**Kompatybilność:**
- Pełna kompatybilność – żadna funkcjonalność nie została zgubiona
- Użytkownik po wejściu trafi do nowego edytora
- Zostawiamy jednak przełącznik na "starą listę pól" dla bezpieczeństwa/wygody, jeśli ktoś czegoś nie znajdzie
- Docelowo (za ok. pół roku) stary edytor zostanie wyłączony

**Plany na przyszłość:**
- W kolejnych wydaniach: nowy edytor diagramu i reguł

**Szczegóły techniczne:**
- Przebudowa na React
- Przełącznik między nowym a starym edytorem

### Ograniczenia / Poza zakresem

- Stary edytor zostanie wyłączony za około pół roku
- Nowy edytor diagramu i reguł jeszcze nie zaimplementowany (planowany w kolejnych wydaniach)

### Punkty otwarte

- Kiedy dokładnie zostanie wyłączony stary edytor?
- Kiedy będą dostępne nowe edytory diagramu i reguł?


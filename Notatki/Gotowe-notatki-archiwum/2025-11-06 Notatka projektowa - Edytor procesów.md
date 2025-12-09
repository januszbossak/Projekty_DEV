# Notatka projektowa – 2025-11-06 – Edytor procesów

**Data:** 2025-11-06
---

## 1. Wizualna organizacja lewego panelu narzędzi (Toolbox)

**Komponent:** Edytor Formularza

### Cel i problem

Użytkownicy (konsultanci - Daniel, Mateusz Kołakowski) odbierają nowy edytor formularza jako "toporny" i przytłaczający ilością opcji wyświetlanych jednocześnie. Główny problem: lewy panel z polami do drag & drop zlewa się wizualnie z centralną częścią formularza. Użytkownicy nie zwracają uwagi na lewy panel, skupiając się od razu na środkowej części ekranu.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Kolorowe ikonki dla typów pól | Każdy typ pola (tekstowe, listy wyboru, słowniki, daty) miałby dedykowany kolor dla swojej kategorii. Ikonki byłyby tematycznie pogrupowane (np. wszystkie pola typu lista wyborów, użytkownik, słownik, odnośnik w jednym kolorze). | 💡 Propozycja – w trakcie dyskusji |
| Zmiana koloru tła lewego panelu | Nadanie lewemu panelowi (toolbox) innego koloru tła niż reszta interfejsu, aby wyraźnie oddzielić go jako narzędziową część od obszaru roboczego. | 💡 Propozycja – Przemek Sołdacki zaproponował |
| Delikatne tło dla przycisków pól | Kolorowanie tła przycisków reprezentujących pola w lewym panelu (zamiast samych ikonek) w kategoryzowane kolory. | 💡 Propozycja – w trakcie rozważenia |
| Wizualne oddzielenie panelu ramką | Stworzenie z toolboxa osobnego elementu z własną ramą/obramowaniem, który nie zlewa się z formularzem. Inspiracja: rozwiązanie zastosowane przez Filipa w prawym panelu listy pól. | 💡 Propozycja – Kamil pokazał mockup |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – w trakcie eksperymentowania

Zespół eksperymentuje z kilkoma podejściami jednocześnie:

1. **Wizualne oddzielenie toolboxa:** Kamil przygotował propozycję, w której lewy panel (toolbox) staje się osobnym elementem z własną ramą, podobnie jak prawy panel. To rozwiązanie wyraźnie oddziela narzędzia od obszaru roboczego.

2. **Kolorystyka ikon:** Rozważane jest wprowadzenie kolorowych ikon dla kategorii pól. Przemek Sołdacki zgłosił obawy przed "choinką kolorów" (około 20 typów pól = 20 kolorów), ale Kamil proponuje grupowanie tematyczne (5-6 kolorów dla kategorii).

3. **Gradacja tonów:** Przemek zaproponował, aby nadać lewemu panelowi inny odcień tła, żeby podkreślić jego rolę jako narzędziowego obszaru.

**Szczegóły techniczne:**
- Obecnie lewy panel jest integralną częścią ramy formularza - zlewa się wizualnie
- Propozycja: oddzielenie go jako osobnego elementu UI z własną ramą
- Kolory kategorii: pola typu lista/słownik/użytkownik - jeden kolor, pola tekstowe - inny kolor, etc.

**Kontekst biznesowy:**
- Feedback od konsultantów (Mateusz Kołakowski, Daniel) wskazuje na rosnące oczekiwania klientów wobec "cukierkowych", kolorowych systemów (trend rynkowy)
- Christina wcześniej proponowała kolorowe ikony
- Obecny edytor jest odbierany jako zbyt monochromatyczny po przejściu z poprzedniej wersji AMODIT

### Punkty otwarte

- Czy kolorystyka nie będzie zbyt przytłaczająca? (obawa przed "choinką")
- Który wariant wizualnego oddzielenia będzie najbardziej czytelny dla użytkowników?
- Czy tematyczne grupowanie 5-6 kolorów będzie wystarczające dla 20+ typów pól?

---

## 2. Dodawanie nowych pól do formularza

**Komponent:** Edytor Formularza

### Cel i problem

W starej wersji edytora dodawanie pola wymagało wypełnienia wszystkich danych (nazwa, typ, sekcja) w jednej linii. Użytkownicy chcieli prostszego i bardziej intuicyjnego procesu dodawania pól, zwłaszcza w kontekście sekcji formularza.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dodawanie na poziomie sekcji | Przycisk "Dodaj pole" jest dostępny przy każdej sekcji, pole jest automatycznie dodawane do wybranej sekcji jako ostatnie pole. | ✅ Wybrana – zaimplementowane w bieżącej wersji |
| Dodawanie na poziomie wiersza (między polami) | Przycisk dodawania pola pojawia się między poszczególnymi wierszami (na hover), umożliwiając precyzyjne umieszczenie pola między istniejącymi polami. | ❌ Odrzucona – ograniczenia tabeli Ant Design uniemożliwiły implementację |
| Przycisk stale widoczny vs. przycisk na hover | Przycisk "Dodaj pole" jest stale widoczny vs. pojawia się tylko po najechaniu na sekcję. | 💡 Propozycja – rozważane przejście na hover po dodaniu więcej opcji |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone – zaimplementowane z modyfikacjami do rozważenia

Zaimplementowano dodawanie pól na poziomie sekcji:
- Użytkownik decyduje, do której sekcji chce dodać pole
- Przycisk "Dodaj pole" jest obecnie stale widoczny przy każdej sekcji
- Pole jest automatycznie dodawane jako ostatnie w danej sekcji

**Szczegóły techniczne:**
- Funkcjonalność dostępna w bieżącej wersji
- Filip Lewandowski implementował rozwiązanie
- Ograniczenia tabeli Ant Design uniemożliwiły dodawanie na poziomie wiersza (między polami)

**Kontekst użytkownika:**
- Testerzy i Mateusz Kołakowski początkowo nie zauważyli funkcjonalności (protest, że nie znaleźli opcji)
- Po przeczytaniu zgłoszenia zorientowali się, że funkcjonalność jest dostępna
- To sugeruje, że przycisk może być zbyt subtelny lub źle umieszczony

### Ograniczenia / Poza zakresem

- Dodawanie pola między konkretnymi polami (na poziomie wiersza) – niemożliwe do zrealizowania z powodu ograniczeń biblioteki Ant Design

### Punkty otwarte

- Czy przejść na wyświetlanie przycisku "Dodaj pole" na hover? (po dodaniu kolejnych opcji w wierszu)
- Janusz zaproponował hover (znany wzorzec z innych miejsc AMODIT)
- Kamil obawia się, że użytkownicy nie znajdą funkcjonalności (feedback od testerów)
- Rozważane: poczekać aż dojdą kolejne opcje (otwieranie prawego panelu, historia zmian) – wtedy przejście na hover będzie bardziej naturalne

---

## 3. Opcja dodawania nowych sekcji do formularza

**Komponent:** Edytor Formularza

### Cel i problem

W bieżącej wersji edytora brakuje możliwości dodawania nowych sekcji do formularza z poziomu listy pól. Użytkownik może dodawać pola do istniejących sekcji, ale nie może utworzyć nowej sekcji.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone – zaplanowane na bieżący sprint

Zadanie dodania opcji tworzenia nowych sekcji jest rozpisane na bieżący sprint (sprint, w którym odbyło się spotkanie 2025-11-06). Filip Lewandowski jest odpowiedzialny za implementację.

**Szczegóły techniczne:**
- Funkcjonalność będzie dostępna w tym samym interfejsie co dodawanie pól
- Brak szczegółów implementacyjnych na tym etapie

---

## 4. Opcje dostępne na hover (lista pól)

**Komponent:** Edytor Formularza

### Cel i problem

W starej wersji edytora opcje zarządzania polami (usuwanie, edycja, historia) pojawiały się na hover. Nowa wersja powinna udostępniać podobne lub ulepszone opcje interakcji z polami i sekcjami.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone – częściowo zaimplementowane, publikacja w toku

Filip Lewandowski zaimplementował (ale jeszcze nie opublikował) następujące funkcjonalności dostępne na hover:

1. **Otwieranie prawego panelu** – możliwość otwarcia panelu z ustawieniami pola/sekcji
2. **Opcja usuwania pola** – dostępna w prawym panelu
3. **Edycja wszystkich właściwości pola** – dostępna w prawym panelu
4. **Historia zmian ustawień pola/sekcji** – nowa funkcjonalność, której nie było w starej wersji

**Szczegóły techniczne:**
- Opcje pojawiają się po najechaniu na wiersz z polem/sekcją (hover)
- Prawy panel otwiera się po kliknięciu odpowiedniej opcji
- Wzorzec znany z innych miejsc w AMODIT (np. lista procesów)

**Kontekst:**
- Przemek Sołdacki potwierdził, że na liście procesów już działa podobny mechanizm (opcje na hover)
- Kamil przewiduje, że użytkownicy szybko przyzwyczają się do tego wzorca

### Punkty otwarte

- Czy Filip już opublikował implementację opcji na hover? (Kamil mówi, że jeszcze nie)

---

## 5. Opcja "Zwiń/Rozwiń wszystko" dla sekcji

**Komponent:** Edytor Formularza

### Cel i problem

W starej wersji edytora istniała opcja "Zwiń wszystko" dla sekcji formularza. Mateusz Kołakowski używał tej funkcji, aby zobaczyć wszystkie sekcje i poustawiać je w odpowiedniej kolejności. W nowej wersji dodano drag & drop do przesuwania sekcji, ale usunięto opcję "Zwiń/Rozwiń wszystko". Użytkownicy muszą teraz zwijać sekcje pojedynczo.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji – wyłapane jako brakująca funkcjonalność

Opcja "Zwiń/Rozwiń wszystko" została zidentyfikowana jako brak w nowej wersji edytora. Wymaga dodania w kolejnym sprincie.

**Szczegóły techniczne:**
- Funkcjonalność była dostępna w starej wersji edytora
- Użytkownicy (Mateusz Kołakowski) wykorzystywali ją do zarządzania widocznością sekcji podczas zmiany ich kolejności
- Nowa wersja ma drag & drop, ale brak globalnej opcji zwijania/rozwijania

### Punkty otwarte

- Kiedy zadanie zostanie rozpisane i zaimplementowane?
- Czy dodanie drag & drop zastępuje potrzebę "Zwiń wszystko"? (odpowiedź: nie, obie funkcjonalności są przydatne)

---

## 6. Edycja formularza w trybie tekstowym (XML/Markdown)

**Komponent:** Edytor Formularza

### Cel i problem

💭 **Pomysł Przemka Sołdackiego:** Podczas hackathonu pojawiła się koncepcja edycji formularza w trybie tekstowym (XML, Markdown lub inny format). Celem byłoby przyspieszenie pracy konsultantów, którzy mogliby:
- Szybko przesuwać wiele pól między sekcjami (kopiuj-wklej)
- Masowo zmieniać nazwy pól
- Wklejać gotową listę pól dostarczonych przez klienta
- Wykonywać operacje "bulk" zamiast ręcznego przeciągania

Przemek zastanawia się, czy to przyspieszyłoby pracę wdrożeniowcom i serwisantom.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Edycja XML/tekstowa | Użytkownik przełącza się na tryb tekstowy, edytuje strukturę formularza, zapisuje. System waliduje i aplikuje zmiany lub zwraca błędy walidacji. | ⏸️ Odroczona – wymaga konsultacji z użytkownikami i analizy technicznej |
| Zaznaczanie wielu pól (Ctrl+Click) i przenoszenie drag & drop | Filip dodał możliwość zaznaczania wielu pól Ctrl+Click i zbiorczego przeciągania między sekcjami. | 💡 Propozycja – prawdopodobnie już zaimplementowane lub w trakcie |
| Integracja z Copilotem AI | Copilot mógłby działać w kontekście edytora formularza: użytkownik wkleja listę pól od klienta, Copilot analizuje, dobiera typy pól, proponuje rozwiązanie, pyta o potwierdzenie i tworzy pola. | 💡 Propozycja – Przemek Sołdacki zaproponował jako alternatywę |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – wymaga konsultacji z użytkownikami

💭 Pomysł Przemka Sołdackiego: edycja tekstowa mogłaby przyspieszyć pracę, ale wymaga sprawdzenia czy faktycznie byłaby przydatna.

**Plan:**
1. Zapytać Daniela i Mateusza Kołakowskiego, czy edycja tekstowa/XML przyspieszyłaby im pracę
2. Jeśli odpowiedź pozytywna – rozważyć implementację lub integrację z Copilotem
3. Jeśli odpowiedź negatywna lub oszczędność czasu minimalna (np. 5 minut na wdrożenie) – odrzucić pomysł

**Obawy techniczne (Janusz Bossak, Kamil Dubaniowski):**
- Masowe walidacje (trudne do przeprowadzenia w trybie tekstowym)
- Masowe zmiany typów pól (różne typy mają różne wymagania – potencjalnie problematyczne)
- Przypadkowe usuwanie pól przez błąd w tekście
- Oderwanie od mechanizmów walidacyjnych działających w edytorze graficznym

**Odpowiedź Przemka na obawy:**
- System mógłby spróbować wykonać operacje i w razie naruszenia walidacji zwrócić błąd: "Sorry, nie mogę tego zrobić, bo to narusza walidacje"
- Nie musi obsługiwać masowych zmian typów – tylko operacje bezpieczne (przenoszenie pól, zmiana nazw)

**Alternatywa: Copilot AI**
- Przemek zaproponował, że Copilot działający w kontekście edytora mógłby być lepszym rozwiązaniem
- Użytkownik: "Weź tę listę 20 pól od klienta i wstaw na formularz"
- Copilot: inteligentnie dobiera typy, pyta o potwierdzenie, tworzy pola
- To podejście mogłoby być bardziej przydatne niż ręczna edycja XML

### Ograniczenia / Poza zakresem

- Masowe zmiany typów pól – nie będą obsługiwane (zbyt ryzykowne i problematyczne walidacyjnie)

### Punkty otwarte

- Czy Daniel i Mateusz Kołakowski uznają edycję tekstową/XML za przydatną?
- Jak duże byłoby przyspieszenie pracy? (jeśli tylko 5 minut na wdrożenie – nie warto)
- Czy Copilot AI byłby lepszym rozwiązaniem niż edycja tekstowa?
- Czy zaznaczanie wielu pól (Ctrl+Click) i zbiorcze przenoszenie wystarczająco rozwiązuje problem?

---

## 7. Sekcja informacji technicznych pola

**Komponent:** Edytor Formularza

### Cel i problem

Piotr Buczkowski (serwis) poprosił o dodanie informacji technicznych dostępnych z poziomu edytora formularza. Potrzebne są do celów serwisowych, analizy błędów i operacji na bazie danych. Przykład: przenoszenie procesów między środowiskami, gdzie GUID pól mogą się nie zgadzać i powodować błędy.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone – zaimplementowane

Dodano sekcję "Informacje techniczne" w prawym panelu edytora pól. Zawiera:
- **Nazwa kolumny w bazie danych** – techniczny identyfikator kolumny
- **ID pola** – wewnętrzny identyfikator
- **GUID pola** – unikalny identyfikator globalny (Global Unique Identifier)

**Szczegóły techniczne:**
- GUID jest edytowalny z poziomu interfejsu
- Piotr Buczkowski (Przemek Rogaś?) zaimplementował walidacje dla edycji GUID
- W starej wersji edytora tych informacji nie było dostępnych – nowa funkcjonalność

**Kontekst biznesowy:**
- Potrzebne głównie dla serwisu (Piotr Buczkowski)
- Sytuacja użycia: przenoszenie procesów między środowiskami, gdzie GUID pól muszą być zsynchronizowane
- Daniel wspomniał, że konsultanci sprawdzają, w której kolumnie tabeli zapisywane są dane

### Punkty otwarte

- Czy funkcjonalność będzie przeniesiona również na listę pól? (Kamil wspomniał, że lista jest w starszej wersji, Filip aktualizuje)

---

## 8. Matryca uprawnień – uproszczenie interfejsu

**Komponent:** Edytor Formularza

### Cel i problem

Matryca uprawnień (określająca widoczność i wymagalność pól na różnych etapach procesu) jest niejasna dla użytkowników (Daniel, Mateusz Kołakowski). Główne problemy:
1. Niezrozumiałe oznaczenie "dziedziczenia" uprawnień (łańcuszki, domyślne vs. wyjątki)
2. Nie rozumieją różnicy między "uprawnieniem domyślnym" a "wyjątkiem dla etapu"
3. Interfejs jest wizualnie skomplikowany
4. Nazwa "matryca uprawnień" jest myląca (sugeruje "kto ma dostęp", a nie "jakie pole jak się zachowuje")

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Oznaczanie dziedziczenia szarościami | Pola dziedziczące uprawnienie domyślne miałyby szare tło/tekst, wyjątki byłyby kolorowe/wyróżnione. | 💡 Propozycja – w trakcie rozważenia |
| Odwrócenie oznaczenia dziedziczenia | Zamiast pokazywać co jest dziedziczone (co jest regułą), pokazywać tylko co NIE jest dziedziczone (co jest wyjątkiem). | 💡 Propozycja – Przemek Sołdacki zaproponował |
| Zmiana nazwy "uprawnienie domyślne" na "dziedziczy po sekcji" | Wyraźniejsze określenie skąd pochodzi uprawnienie. | 💡 Propozycja – Przemek Sołdacki zaproponował |
| Zmiana nazwy "matryca uprawnień" na "matryca widoczności" lub "ustawienia pól w etapach" | Nazwa bardziej oddająca sens funkcjonalności (widoczność i wymagalność pól w zależności od etapu). | 💡 Propozycja – Przemek Sołdacki i Janusz Bossak zaproponowali |
| Rozróżnienie "uprawnień" (kto ma dostęp) od "ustawień" (jak pole się zachowuje) | Uprawnienia to kolumna z ludzikiem (określa kto może modyfikować), reszta to "ustawienia" lub "widoczność". | 💡 Propozycja – Przemek Sołdacki zaproponował |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – zaplanowane na bieżący sprint, szczegóły do ustalenia

Na bieżący sprint jest cel: uprościć matrycę uprawnień. Kamil jeszcze nie rozpisał zadań – najpierw zespół musi omówić koncepcję i ustalić rozwiązanie.

**Wyjaśnienie mechanizmu dziedziczenia (jak to działa obecnie):**
1. **Uprawnienie domyślne** – każde pole i sekcja ma uprawnienie nadrzędne (domyślne)
2. **Dziedziczenie** – wszystkie etapy, które nie mają zdefiniowanego wyjątku, dziedziczą uprawnienie domyślne
3. **Wyjątek dla etapu** – jeśli dla konkretnego etapu zdefiniujesz wyjątek, ten etap używa wyjątku zamiast dziedziczenia

Przykład:
- Sekcja domyślnie ma ustawienie "wymagane"
- Wszystkie etapy dziedziczą "wymagane"
- Zmiana domyślnego na "ukryte" → wszystkie etapy dziedziczą "ukryte"
- Ustawienie wyjątku dla etapu 2 na "odczyt" → etap 2 ma "odczyt", reszta etapów dalej dziedziczy "ukryte"

**Problemy z interfejsem:**
- W starej wersji uprawnienie domyślne nazywało się "uprawnienie dla użytkowników" – jeszcze mniej intuicyjne
- Użytkownicy nauczyli się starego interfejsu, w nowym czytają opisy i nie rozumieją
- Kamil podejrzewa, że użytkownicy już nie czytali opisów w starej wersji – działali z przyzwyczajenia

**Proponowane zmiany:**
1. **Nazewnictwo:** Zmienić "uprawnienie domyślne" na "dziedziczy po sekcji" lub podobne
2. **Nazwa całości:** Zmienić "matryca uprawnień" na "matryca widoczności" lub "ustawienia pól w etapach"
3. **Rozróżnienie uprawnień od ustawień:** Kolumny z ludzikiem to "uprawnienia" (określają kto może edytować), reszta kolumn to "ustawienia" lub "widoczność" (określają jak pole się zachowuje)
4. **Wizualizacja dziedziczenia:** Zastosować szarości/kolory do oznaczenia dziedziczonych wartości vs. wyjątków
5. **Odwrócenie oznaczenia:** Zamiast pokazywać wszystko, pokazywać tylko wyjątki (bo dziedziczenie jest regułą)

**Szczegóły techniczne:**
- Uprawnienia specyficzne dla użytkownika/grupy są oznaczane ikonką ludzika (świecącą gdy ustawiony wyjątek)
- Bug: ikonka ludzika powinna świecić cały czas gdy wyjątek jest ustawiony, ale coś się zepsuło (działało na pojedynczych polach, nie działa na liście)

### Punkty otwarte

- Jakie konkretnie zmiany nazewnictwa wprowadzić?
- Jak oznaczyć wizualnie dziedziczenie vs. wyjątki? (szarości, odwrócenie logiki, coś innego?)
- Kiedy Kamil rozpisze zadania na bieżący sprint?
- Czy ikonka ludzika (uprawnienia użytkownik/grupa) powinna być stale widoczna czy tylko na hover?

---

## 9. Nadmiarowy scroll w liście pól

**Komponent:** Edytor Formularza

### Cel i problem

Kamil wyłapał problem: gdy lista pól jest przewinięta maksymalnie do dołu, pojawia się dodatkowy, nadmiarowy scroll. Zachowanie wydaje się błędne.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji – błąd zgłoszony do Filipa Lewandowskiego

Kamil nie ogarnął do końca, co się dzieje z listą. Przekazał temat Filipowi do analizy i poprawy.

---

## 10. Brak sekcji ustawień specyficznych dla typu pola

**Komponent:** Edytor Formularza

### Cel i problem

W prawym panelu edycji pola brakuje sekcji z ustawieniami specyficznymi dla danego typu pola. Przykład: pole numeryczne powinno mieć opcję ustawienia liczby miejsc po przecinku, pole kwota – podobnie.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji – możliwy błąd lub niekompletna implementacja

Po analizie okazało się, że:
- Pole "kwota" nie ma ustawień specyficznych (intencjonalnie?)
- Pole numeryczne powinno mieć ustawienia (liczba miejsc po przecinku), ale w testowym procesie Kamila pole o nazwie "numeryczne jeden" okazało się być typu "kwota", nie "numeryczne" – stąd zamieszanie

**Kontekst:**
- Przemek Rogaś testował zmianę typów pól, dlatego w procesie testowym nazwy pól nie odpowiadają typom
- Kamil pomylił się, zakładając że pole o nazwie "numeryczne jeden" jest typu numeryczne

### Punkty otwarte

- Czy pole "kwota" powinno mieć ustawienia (np. liczba miejsc po przecinku)?
- Dlaczego pole numeryczne w testowym procesie ma nazwę "numeryczne jeden" ale typ "kwota"?

---

## 11. Nazwa typu pola w prawym panelu – jak wyświetlać?

**Komponent:** Edytor Formularza

### Cel i problem

W prawym panelu edycji pola wyświetlana jest nazwa typu pola (np. "kwota", "numeryczne", "data i czas"). Użytkownicy mogą nie rozumieć, co oznacza ta informacja:
1. Czy to jest nazwa pola czy typ pola?
2. Czy mogę to zmienić?
3. Dlaczego ta sama nazwa pojawia się w dwóch miejscach (nagłówek prawego panelu + lewy panel toolbox)?

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dodanie etykiety "Typ:" przed nazwą | Wyraźne oznaczenie "Typ: kwota" zamiast tylko "kwota". | 💡 Propozycja – Damian Kamiński zaproponował |
| Dodanie ikonki typu pola obok nazwy | Ikonka z lewego panelu (toolbox) pojawiłaby się obok nazwy typu w prawym panelu – unifikacja wizualna. | 💡 Propozycja – Damian Kamiński zaproponował |
| Zmiana nagłówka na "Właściwości [nazwa pola]" | Zamiast pokazywać typ pola w nagłówku, pokazywać nazwę pola i ogólny tytuł "Właściwości". | 💡 Propozycja – Kamil Dubaniowski rozważa |
| Przeniesienie nazwy typu do sekcji "Dane podstawowe" | Typ pola byłby wyświetlany jako jedna z właściwości w sekcji "Dane podstawowe", nie w nagłówku. | 💡 Propozycja – w trakcie rozważenia |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja – w trakcie dyskusji

Przemek Rogaś wspomniał, że nazwa typu pola w nagłówku prawego panelu jest tymczasowa ("wstawiłem, żeby coś wstawić"). Niekoniecznie tam musi być typ pola.

**Proponowane rozwiązania:**
1. **Etykieta "Typ:"** – dodanie tekstu "Typ:" przed nazwą typu, aby było jasne, że to nie jest nazwa pola
2. **Ikonka typu pola** – dodanie ikonki z lewego panelu obok nazwy typu, aby wizualnie połączyć oba elementy (unifikacja)
3. **"Właściwości [nazwa pola]"** – zmiana nagłówka prawego panelu na bardziej ogólny, bez pokazywania typu
4. **Przeniesienie do "Dane podstawowe"** – umieszczenie typu pola jako jeden z parametrów w sekcji "Dane podstawowe" zamiast w nagłówku

**Kontekst problemu:**
- W testowym procesie Przemka Rogasia nazwy pól pokrywają się z typami (np. pole o nazwie "kwota" jest typu "kwota"), co wprowadza dodatkowe zamieszanie
- Użytkownicy patrzący na interfejs pierwszy raz nie wiedzą, co oznacza wyświetlana informacja

### Punkty otwarte

- Który wariant wybrać?
- Czy unifikacja wizualna (ikonka + etykieta "Typ:") będzie wystarczająco jasna?
- Czy pokazywanie typu pola w nagłówku jest w ogóle potrzebne?

---

## 12. Status prac: Edytor Diagramu i Edytor Reguł

**Komponent:** Edytor Diagramu, Edytor Reguł

### Cel i problem

Przemek Sołdacki zapytał o postępy prac nad Edytorem Diagramu i Edytorem Reguł.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji

**Status:** ⏸️ Odroczone – niższy priorytet

**Edytor Diagramu:** Na razie nie ma postępów (Kamil: "na razie nic").

**Edytor Reguł:** Są zaprojektowane (prawdopodobnie mockupy/koncepcja gotowa), ale implementacja jest wstrzymana. Zespół koncentruje się na rozwiązywaniu błędów i problemów w Edytorze Formularza i innych obszarach (np. moduł raportowy). Błędy i problemy zgłaszane przez użytkowników mają wyższy priorytet niż nowe funkcjonalności w Edytorze Diagramu i Reguł.

**Szczegóły techniczne:**
- Przemek Rogaś będzie zaangażowany również w prace nad modułem raportowym (wyższy priorytet)

### Punkty otwarte

- Kiedy zespół wróci do prac nad Edytorem Diagramu i Edytorem Reguł?

---

## Punkty do dalszej dyskusji (globalne)

- **Konsultacja z użytkownikami (Daniel, Mateusz Kołakowski):**
  - Czy edycja tekstowa/XML formularza przyspieszyłaby ich pracę?
  - Czy Copilot AI mógłby zastąpić edycję tekstową (wklejanie listy pól od klienta)?
  - Jak odbierają nowe oznaczenia i nazwę "matryca uprawnień"?

- **Wizualne oddzielenie elementów interfejsu:**
  - Finalizacja koncepcji oddzielenia toolboxa (lewy panel) od formularza
  - Ustalenie kolorystyki (kolorowe ikonki vs. tło panelu vs. tło przycisków)
  - Testowanie różnych wariantów z użytkownikami

- **Nazewnictwo i terminologia:**
  - Ustalenie finalnej nazwy dla "matrycy uprawnień" (czy zmienić na "matryca widoczności"?)
  - Rozróżnienie "uprawnień" (kto ma dostęp) od "ustawień" (jak pole się zachowuje)
  - Zmiana nazwy "uprawnienie domyślne" na "dziedziczy po sekcji" lub podobne

- **Roadmapa Edytora Procesów:**
  - Kiedy zespół wróci do Edytora Diagramu i Edytora Reguł?
  - Czy błędy i braki w Edytorze Formularza zostaną uzupełnione w bieżącym sprincie?

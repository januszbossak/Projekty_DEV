# Sprint Review – 2025-10-20

> 🛡️ **Codex Review:** Notatka zweryfikowana i uzupełniona w dniu 2025-12-02.
> **Korekty:** Poprawiono nazwy projektów zgodnie ze Słownikiem Projektów (wielka litera); skorygowano status landing page w Trust Center (tylko zmiana strony, brak możliwości wyboru); przeniesiono dyskusję o harmonogramie źródeł systemowych do sekcji Feedback.

**Sprint:** [nie sprecyzowano]
**Okres:** [nie sprecyzowano]

**Powiązane projekty:**
- `Moduly/Edytor-procesow/Edytor-diagramu` – temat 1
- `Moduly/Edytor-procesow/Edytor-formularzy` – tematy 2, 3, 4, 5
- `Moduly/Modul-raportowy` – temat 6
- `Moduly/Trust-Center` – tematy 7, 8
- `Moduly/e-Doreczenia` – temat 9
- `Moduly/e-Nadawca` – temat 11
- `Moduly/Raporty-systemowe` – temat 12
- `Moduly/AMODIT Copilot` – temat 13
- `Klienci/WIM/Komunikator` – temat 14

---

## 1. Edytor diagramu procesów

**Projekt:** `Moduly/Edytor-procesow/Edytor-diagramu`

### Cel biznesowy

Kontynuacja prac nad edytorem graficznym diagramów procesów. Przeniesienie wszystkich funkcjonalności ze starego edytora do nowego rozwiązania.

### Co zaimplementowano

- Dodawanie etapów
- Łączenie etapów
- Dodawanie reguł
- Usuwanie połączeń
- Różne układy diagramu:
  - Pionowy/poziomy
  - Hierarchiczny
  - Hierarchiczny zwarty (linie połączone)
  - Podstawowy (układ Dagre, przypominający drzewo)
- Wszystkie warunki z starego diagramu zostały przeniesione
- Wyszukiwanie po polach (dodane w poprzednim sprincie)
- Wyszukiwanie po nazwie pola (dodane w bieżącym sprincie)

### Ograniczenia / Known issues

- Na navigatorze coś nie działa (nie sprecyzowano szczegółów)
- Podziały (kreski) pojawiają się dopiero na hover lub podczas drag & drop między wierszami (zmiana względem poprzedniej wersji)

### Feedback z demo

- Janusz Bossak: "Dużo lepiej" – pozytywna ocena zmian w wyświetlaniu podziałów
- Przemysław Rogaś: W praktyce teraz jest trochę ciężej wjechać na podziały (wymaga hover/drag)

### Dalsze kroki

- [Nie sprecyzowano w transkrypcji]

---

## 2. Edytor formularza – ulepszenia i poprawki

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

### Cel biznesowy

Ujednolicenie wyglądu edytora z rzeczywistym formularzem sprawy oraz poprawa użyteczności edytora.

### Co zaimplementowano

- Ujednolicenie ikon pól – ikony w edytorze mają teraz taki sam kolor i rozmiar jak na formularzu sprawy
- Ograniczenie długości pola na sprawie do 500 pikseli (odzwierciedlone w edytorze)
- Pola zablokowane – ikona kłódki, możliwość zmiany tylko nazwy wyświetlanej i podpowiedzi
- Pole statyczny tekst:
  - Poprawiona edycja
  - Wyświetlanie tekstu w podglądzie formularza
  - Wyświetlanie nazwy pola z informacją, że na docelowym formularzu jest niewidoczna
- Większe okno edycji pola statycznego tekst
- Poprawka pierwszej opcji wyboru – dla każdego języka, dla którego nie zdefiniowano tekstu, wyświetlana jest odpowiednia informacja
- Pola Odnośnik – możliwość zmiany źródła (zewnętrzny, wewnętrzny, Słownik) z ostrzeżeniem o możliwej utracie danych
- Usuwanie wyjątków – przycisk obok selekcji zamiast X na selekcji (bardziej widoczne)
- Komunikat o niezapisanych zmianach przy próbie wyjścia z edytora (opcje: anuluj/zapisz)

### Jak to działa (jeśli omówiono)

- Zmiana źródła w polu Odnośnik wymaga przejścia przez edycję i zaznaczenia nowego źródła
- System ostrzega przed utratą danych przy zmianie źródła (100% szansy na utratę danych, bo ID się nie pokrywają)

### Ograniczenia / Known issues

- Brak linku do źródła przy polu Odnośnik (w starej wersji był przy słownikach) – do dodania w przyszłym sprincie

### Dalsze kroki

- Dodanie linku do źródła przy polu Odnośnik (słownik, proces, rejestr, źródło zewnętrzne) – zaplanowane na przyszły sprint
- Zmiana ikon pól – wszystkie na outline (obecnie dokument ma wypełnioną koronę, pozostałe są outline)
- Rozważenie wprowadzenia kolorowych ikon dla typów pól w edytorze graficznym (propozycja Kamila)
- Rozważenie pokolorowania sekcji w prawym panelu edytora, żeby odróżnić je od formularza w środkowej części

---

## 3. Nowa lista pól w edytorze formularza

**Projekt:** `Moduly/Edytor-procesow/Edytor-formularzy`

### Cel biznesowy

Odtworzenie i zmiana wyglądu listy pól w edytorze formularza. Głównym celem jest szybki przegląd pól oraz łatwa możliwość wprowadzania nazw wyświetlanych w różnych językach bez przechodzenia do zakładki tłumaczeń.

### Co zaimplementowano

- Nowy wygląd listy pól
- Edycja nazw wyświetlanych w różnych językach bezpośrednio z listy:
  - Domyślna
  - Polski
  - Angielski
  - Niemiecki
- Wizualne rozróżnienie nazw:
  - Ciemna (czarna) – nazwa zdefiniowana
  - Szara – nazwa dziedziczona z domyślnej
- Edycja podpowiedzi w różnych językach (rozwijanie przez przycisk w nagłówku kolumny)
- Edycja nazw systemowych (technicznych) inline
- Edycja typu pola przez okno modalne (ten sam model co w edytorze graficznym)
- Edycja indeksu, nazwy, tłumaczeń inline
- Ukrywanie/wyświetlanie kolumn
- Przywracanie domyślnych ustawień kolumn
- Wyszukiwanie po polach z podświetlaniem całej komórki i podświetlaniem na hover
- Tabele rozklaszowane do danego pola – wszystkie pola (główne i z tabel) widoczne na jednym widoku zagnieżdżonym (podobnie jak w matrycy uprawnień)

### Jak to działa (jeśli omówiono)

- Nie trzeba się przełączać między widokiem formularza głównego a tabelami – wszystko na jednym widoku
- Ułatwia przegląd całego formularza (pola poza tabelami i wewnątrz tabel)

### Ograniczenia / Known issues

- Ikony pól mogą się gubić pośród sekcji (wymaga dopracowania)
- Statyczny tekst ma inną ikonę niż powinien (do zmiany w przyszłym sprincie)

### Feedback z demo

- Janusz Bossak: Ikony pól są identyczne (pozytywna uwaga)
- Piotr Buczkowski: Różnica w ikonach tabeli (wymaga dopracowania)

### Dalsze kroki

- Zmiana ikon pól – ujednolicenie (wszystkie outline)
- Dopracowanie wizualnego rozróżnienia pól w sekcjach
- Rozważenie wprowadzenia kolorowych ikon dla typów pól

---

## 4. Walidacja przy imporcie XML procesów

**Projekt:** `Moduly/Eksport-import-definicji-procesow`

### Cel biznesowy

Zapobieganie psuciu procesów na produkcji przez konsultantów podczas importu XML. W ciągu tygodnia dwoje konsultantów u 2 klientów popsuło procesy na produkcji.

### Co zaimplementowano

- Dokładniejsza walidacja pól przy imporcie XML
- 4 nowe walidacje (oprócz 3 poprzednich):
  - Wykrywanie konfliktów nazw pól z różnymi GUID
  - Wykrywanie konfliktów nazw pól z przypisaniem do innych pól w bazie danych
  - Ostrzeżenia przed zmianami powodującymi problemy (gubienie danych, błędy w zapisie spraw)
- Wyszukiwanie po polu (dodane wcześniej) – pomocne w testowaniu

### Jak to działa (jeśli omówiono)

- System ostrzega przed konfliktami i problemami przed importem
- W przypadku konfliktów GUID lub przypisania do innych pól w bazie danych – blokada importu do przywrócenia spójności

### Ograniczenia / Known issues

- Okienko walidacji powinno być szersze (zgłoszone przez Piotra)
- Nie wszystkie konflikty są jeszcze wykrywane (w trakcie dopracowania)

### Feedback z demo

- Janusz Bossak: Sugestia rozszerzenia okienka i dodania 2 kolumn (lokalne vs importowane) z nazwą i GUID

### Dalsze kroki

- Rozszerzenie okienka walidacji
- Dodanie widoku porównawczego (lokalne vs importowane) z nazwą i GUID
- Dopracowanie wykrywania wszystkich konfliktów

---

## 5. Obsługa słowników zagnieżdżonych i hierarchicznych

**Projekt:** `Moduly/Slowniki`

### Cel biznesowy

Pełna obsługa słowników zagnieżdżonych i hierarchicznych w funkcji finki-ID.

### Co zaimplementowano

- Pełna obsługa słowników zagnieżdżonych w funkcji finki-ID
- Pełna obsługa słowników hierarchicznych w funkcji finki-ID

### Ograniczenia / Known issues

- [Nie sprecyzowano]

### Dalsze kroki

- [Nie sprecyzowano]

---

## 6. Pole typu Podpis w module raportowym

**Projekt:** `Moduly/Modul-raportowy`

### Cel biznesowy

Obsługa wyświetlania pola typu Podpis w nowym module raportowym.

### Co zaimplementowano

- Obsługa wyświetlania pola typu Podpis w nowym module raportowym
- Wygląd identyczny jak w starym module raportowym

### Ograniczenia / Known issues

- [Nie sprecyzowano]

### Dalsze kroki

- [Nie sprecyzowano]

---

## 7. Landing page w Trust Center

**Projekt:** `Moduly/Trust-Center`

### Cel biznesowy

Zmiana strony, na którą użytkownik będzie przekierowany po podpisaniu dokumentu.

### Co zaimplementowano

- Zmiana strony domyślnej, na którą użytkownik będzie przekierowany po podpisaniu (dodane na TrustCenter produkcyjnym)

### Ograniczenia / Known issues

- Brak możliwości wyboru strony przez użytkownika – obecnie zmieniono tylko domyślną stronę docelową
- Nie jest jasne czy możliwość wyboru strony jest planowana

### Dalsze kroki

- Weryfikacja z zespołem czy wymagana jest możliwość konfiguracji strony landing page przez użytkownika

---

## 8. SimplySign – podpisywanie na nowych raportach

**Projekt:** `Moduly/Trust-Center`

### Cel biznesowy

Obsługa podpisywania dokumentów przez SimplySign w nowym module raportowym.

### Co zaimplementowano

- SimplySign podpisywanie na nowych raportach (wydane)
- Odwzorowanie funkcjonalności ze starego modułu raportowego

### Ograniczenia / Known issues

- Proces można jeszcze usprawnić – obecnie są 2 przyciski (Zaloguj i Wywołaj do podpisu)
- Docelowo powinien być jeden wizard łączący oba kroki

### Dalsze kroki

- Usprawnienie procesu podpisywania – połączenie w jeden wizard (zamiast 2 przycisków)

---

## 9. E-doręczenia – kontynuacja prac

**Projekt:** `Moduly/e-Doreczenia`

### Cel biznesowy

Kontynuacja prac nad problemami z e-doręczeniami.

### Co zaimplementowano

- Prace nad problemami z e-doręczeniami (kontynuacja)
- Uwagi dotyczące Centralnego Ośrodka Informatyki

### Ograniczenia / Known issues

- [Nie sprecyzowano szczegółów]

### Dalsze kroki

- [Nie sprecyzowano]

---

## 10. Podpisy elektroniczne – Szafir i SimplySign

**Projekt:** `Moduly/Trust-Center`

### Cel biznesowy

Dodanie obsługi kolejnych podpisów elektronicznych (Szafir, SimplySign) oraz przygotowanie do obsługi podpisu Poczty Polskiej.

### Co zaimplementowano

- Testy wykrywania podpisów na Szafir (w trakcie)
- Planowana obsługa 3 głównych podpisów do końca miesiąca:
  - Szafir
  - Szafir (drugi typ)
  - SimplySign
- Planowana obsługa podpisu Poczty Polskiej (w przyszłości)

### Ograniczenia / Known issues

- Problem z dostępnością podpisów do testów – potrzebny zestaw wszystkich podpisów
- Aplikacja do dopisywania na macOS wymaga Maca (obecnie tylko u Adriana)
- Brak deweloperskich kont do testów podpisów

### Feedback z demo

- Kamil Dubaniowski: Trzeba pomyśleć o zestawie wszystkich podpisów do testów, żeby nie obciążać tylko Adriana
- Problem: osoby z podpisami nie mają Maców, osoby z Macami nie mają podpisów

### Dalsze kroki

- Rozwiązanie problemu dostępności podpisów do testów
- Zakup SimplySign do testów przez Adriana
- Dodanie obsługi podpisu Poczty Polskiej (w planach)

---

## 11. E-nadawca – poprawki

**Projekt:** `Moduly/e-Nadawca`

### Cel biznesowy

Rozwiązanie problemów występujących w integracji z e-Nadawcą.

### Co zaimplementowano

- Rozwiązanie jednego problemu w e-nadawcy
- Prace nad problemem występującym kilka godzin w ciągu dnia (wymaga informacji od Poczty Polskiej do diagnozy)

### Ograniczenia / Known issues

- Problem występujący kilka godzin w ciągu dnia, potem znika – ciężko zdiagnozować bez informacji od Poczty Polskiej

### Dalsze kroki

- Otrzymanie informacji od Poczty Polskiej dotyczącej problemu okresowego

---

## 12. Dashboardy i źródła danych systemowe

**Projekt:** `Moduly/Raporty-systemowe`

### Cel biznesowy

Prace nad dashboardami systemowymi i źródłami danych systemowymi, w tym rozwiązanie problemu z ujemnymi ID w MSSQL.

### Co zaimplementowano

- Prace nad dashboardami systemowymi
- Prace nad źródłami danych systemowymi
- Rozwiązanie problemu z ujemnymi ID w MSSQL (źródła systemowe z ujemnymi ID nie działają poprawnie na MSSQL)
- Dodanie nowych źródeł danych systemowych
- Dashboard Performance Monitor
- Dashboard System Lookup Model

### Jak to działa (jeśli omówiono)

- Problem: źródła systemowe z ujemnymi ID powodują problemy w MSSQL (nazwa tabeli z minusem powoduje błędy składniowe)
- Rozwiązanie: zmiana nazwy tabeli (zamiast minusa podkreślenie lub prefiks S_)
- Docelowo: przejście na GUID zamiast ujemnych ID z kolumną wskazującą że źródło jest systemowe

### Ograniczenia / Known issues

- Nie wszystkie dashboardy zostały jeszcze dodane (w trakcie prac)
- Filtry wymagają dopracowania

### Feedback z demo

- Damian Kamiński: Zastanowienie czy źródła systemowe powinny mieć możliwość zmiany harmonogramu (systemowe = nasze, my decydujemy, nie częściej niż raz dziennie)
- Anna Skupińska: Może ktoś chciałby rzadziej (wolniejszy system)

### Dalsze kroki

- Dokończenie wszystkich dashboardów systemowych
- Dopracowanie filtrów
- Rozważenie ograniczenia możliwości zmiany harmonogramu dla źródeł systemowych
- Przejście na GUID zamiast ujemnych ID (zaplanowane na przyszłość)

---

## 13. Copilot – przesyłanie dokumentów i function calling

**Projekt:** `Moduly/AMODIT Copilot`

### Cel biznesowy

Rozszerzenie funkcjonalności Copilota o możliwość przesyłania dokumentów do konwersacji oraz poprawa wyświetlania informacji o wykonywanych funkcjach.

### Co zaimplementowano

- Opcja przesyłania dokumentów w Copilot
- Możliwość wyboru kilku dokumentów i zadawania pytań o ich zawartość
- Poprawka wyświetlania znaczników function calling – bardziej ogólny napis zamiast szczegółów technicznych funkcji
- Przycisk z informacją o wykonywanej funkcji (np. "zrób mi nową sprawę")

### Jak to działa (jeśli omówiono)

- Dokumenty są dodawane do konwersacji i mogą być wykorzystywane przez AI do odpowiedzi
- Dokumenty są przechowywane po stronie microservisu w historii konwersacji
- Dokumenty są traktowane jak treść pisana ręcznie, tylko w innym formacie
- Po wyczyszczeniu konwersacji dokumenty przepadają (nie są przechowywane trwale)

### Ograniczenia / Known issues

- Dokumenty nie są przechowywane trwale – przepadają po wyczyszczeniu konwersacji
- Brak możliwości powrotu do poprzednich konwersacji
- Brak nazwy procesu w komunikacie o uruchomieniu sprawy (tylko ogólny komunikat)
- Brak nazwy raportu w komunikacie o przejściu do raportu (tylko ogólny komunikat)
- W przypadku wielu procesów/raportów pasujących do zapytania, AI może wypisać wszystkie lub wybrać losowy

### Feedback z demo

- Janusz Bossak: Przydałaby się funkcjonalność przetrzymywania dokumentów na dłuższy okres czasu (możliwość powrotu do nich jutro czy pojutrze)
- Daniel Reszka: Brak nazwy procesu w komunikacie o uruchomieniu sprawy – użytkownik nie wie, który proces zostanie uruchomiony
- Mateusz Kisiel: Możliwość powrotu do poprzednich konwersacji byłaby przydatna

### Dalsze kroki

- Dodanie nazwy procesu w komunikacie o uruchomieniu sprawy (w języku użytkownika)
- Dodanie nazwy raportu w komunikacie o przejściu do raportu
- Rozważenie możliwości przetrzymywania dokumentów na dłuższy okres czasu
- Rozważenie możliwości powrotu do poprzednich konwersacji
- Dopracowanie promptów dla przypadków z wieloma pasującymi procesami/raportami

---

## 14. Komunikator – grupy oparte o mod

**Projekt:** `Klienci/WIM/Komunikator`

### Cel biznesowy

Tworzenie konwersacji w komunikatorze opartych o grupy modów, z automatyczną synchronizacją uprawnień.

### Co zaimplementowano

- Opcja tworzenia konwersacji opartej o model (grupę modów)
- Automatyczna synchronizacja uprawnień – gdy ktoś zostanie dodany/usunięty z grupy, automatycznie odzwierciedla się w uprawnieniach komunikatora
- Grupa oparta o mod (przykład zaimplementowany)

### Ograniczenia / Known issues

- Brak nazwy grupy w interfejsie (warto dodać)

### Dalsze kroki

- Dodanie nazwy grupy w interfejsie

---

## Podsumowanie sprintu

**Statystyki:**
- 113 zgłoszeń zakończonych do dnia dzisiejszego rano
- 462 zgłoszenia czekają na przetestowanie
- 180 pozycji zamkniętych na etapie deweloperskim w tym sprincie

**Uwagi:**
- Dużo pracy nad błędami i stabilizacją wersji
- Wymagana poprawa formuły prezentacji sprint review (prezentowanie powinno być bardziej płynne i przygotowane)
- Pozostały fizycznie 2 miesiące do końca roku (odliczając przerwy świąteczne)

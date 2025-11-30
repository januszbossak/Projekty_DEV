Sprint review z dnia 17 listopada 2025

---

### 1. Ustawienia uprawnień - Matrix (Macierz)

**Dlaczego to robimy:**

- Chęć ułatwienia i zwiększenia widoczności uprawnień między sekcjami a polami.
    
- Zwiększenie czytelności przy ustawianiu uprawnień dla wszystkich pól.
    

**Opis funkcjonalności / rozwiązania:**

- Pola w sekcjach mają lewy margines, aby były łatwiejsze do rozróżnienia i żeby było widać przesunięcie między sekcją a polami.
    
- Sekcja jest skrajnie po lewej. Komórki organizacyjne są traktowane jako zwykłe pole. Sekcja w tabeli ma większe wcięcie, ponieważ jest wewnątrz.
    
- Ustawienia pól dla użytkowników wewnętrznych i zewnętrznych są niezależne od ustawienia systemowego. Jeżeli użytkownicy zewnętrzni nie są włączeni, opcje te nie powinny się pojawiać, a obecnie tak działa.
    
- Przedstawiony nowy widok matrycy ma ułatwić masowe ustawianie uprawnień, np. ustawienie domyślnych uprawnień całej sekcji na "odczyt", a dla wybranych pól na "wymagana".
    

**Dalsze kroki:**

- Poprawić ustawienie ikonek, w tym ich wyśrodkowanie i wielkość (proponowano, aby były większe i bardziej widoczne).
    
- Poprawić kwestię ustawienia wartości ikonek.
    
- Domyślnie tabele powinny być zwinięte, aby zmniejszyć zamieszanie wizualne.
    
- Zwiększyć czytelność w kontekście tabel, np. poprzez większe wcięcia i dodatkowe oznaczenie, że dany element to tabela.
    
- Rozważyć opcję przełącznika nazw wyświetlanych (domyślne/angielskie/polskie) w matrycy, podobnie jak w edytorze graficznym, ponieważ obecnie wyświetlane są nazwy systemowe/techniczne.
    

---

### 2. Aplikacja do podpisów kwalifikowanych (Snap - macOS/Windows)

**Dlaczego to robimy:**

- Dostarczenie przyjaznego interfejsu (UI) dla aplikacji do podpisów kwalifikowanych, która wcześniej była tylko Proof of Concept.
    
- Uzyskanie certyfikacji Apple, aby aplikacja instalowała się na macOS bez ostrzeżeń i konieczności robienia wyjątków (aplikacja z kręgu zaufania).
    
- Umożliwienie dystrybucji do nowych klientów po metalizacji (przejście certyfikacji).
    

**Opis funkcjonalności / rozwiązania:**

- Aplikacja jest multiplatformowa (macOS i Windows). Widok jest jeden dla obu platform, z drobnymi różnicami wynikającymi z różnych systemów operacyjnych.
    
- Zaprezentowano obsługę podpisów mobilnych (Szafir) i fizycznych (przy użyciu czytnika fizycznego).
    
- Aplikacja po wybraniu certyfikatu od dostawcy zewnętrznego (np. Szafir) komunikuje się i potwierdza podpisanie dokumentu.
    
- Trwa proces uzyskiwania certyfikacji Apple (developer ID) oraz przygotowanie do dystrybucji. Docelowo chciano by, aby aplikacja była publikowana przez App Store lub za pomocą wstępnej publikacji z poziomu App Center.
    

**Dalsze kroki:**

- W przypadku podpisu Szafirem (mobilnym) należy ustalić, dlaczego kod do podpisu trzeba podawać dwa razy, ponieważ na Windowsie tak nie było (potencjalny regres). Należy to sprawdzić i ewentualnie skorygować na Windowsie.
    
- Uzupełnienie certyfikacji ostateczne.
    
- Przygotowanie instrukcji i prezentacji dla klienta.
    

---

### 3. Moduł FURA (Weryfikacja zmian w ustawieniach systemowych)

**Dlaczego to robimy:**

- Nie sprecyzowano w transkrypcji.
    

**Opis funkcjonalności / rozwiązania:**

- Zaprezentowano włączenie modułu FURA.
    
- Widoczne są wartości niezaakceptowane (true/false) przy zmianach.
    
- Administrator, który dokonał zmiany, może ją odrzucić lub edytować.
    
- Inny administrator (admin) może zmianę zaakceptować, ale nie może jej edytować, dopóki nie zostanie zaakceptowana lub odrzucona przez poprzedniego admina.
    
- W przypadku obrazków/plików wyświetlane jest ich usunięcie lub widok niezaakceptowanej wersji.
    

**Dalsze kroki:**

- W przypadku usuniętego pliku należy rozważyć, czy administrator z uprawnieniami do akceptacji nie powinien mieć możliwości pobrania pliku.
    

---

### 4. Edytor graficzny - Drobne poprawki i rozwój

**Dlaczego to robimy:**

- Zgłoszenia serwisowe klientów.
    
- Poprawki wizualne i zwiększenie użyteczności.
    

**Opis funkcjonalności / rozwiązania:**

- Ikony w panelach otrzymały kolory, aby panele się nie zlewały i było widać, że to jest coś do wyboru. Kolory są tematycznie przypisane do typu pola (np. tekstowe, numeryczne/kwota, data/czas).
    
- Dodano możliwość przenoszenia sekcji (zwijają się przy przenoszeniu).
    
- W polu typu Odnośnik do źródła zewnętrznego dodano możliwość wyszukiwania.
    
- W informacjach technicznych wyświetlany jest GUID, ID, nazwa w bazie danych kolumny.
    
- GUID jest edytowalny, a edycja jest możliwa po włączeniu specjalnego ustawienia systemowego (dla kompatybilności wstecznej, np. przy synchronizacji pól po dodaniu ich na szybko). ID nie jest edytowalne.
    
- W listach wyboru:
    
    - Dodano możliwość edycji pozycji.
        
    - Dodano możliwość wklejania wielu elementów z automatycznym dodaniem wszystkich pozycji.
        
- W polu typu Dokument brakowało ustawienia do wyboru magazynu (select z możliwością wyboru, jeśli ustawiona jest w bazie).
    
- Pole nadrzędne dla pól w tabeli typu numeryczne i kwota jest dostępne do ustawienia (z typem połączenia).
    
- Dodano możliwość szukania po typie pola.
    
- Dodano możliwość szukania po atrybutach technicznych, w tym po ID.
    

**Dalsze kroki:**

- Należy stworzyć instrukcję, jak używać edycji GUID.
    
- Zmienić sposób edycji GUID – zamiast bezpośredniej edycji pola, dodać opcję zmiany (np. ikonę ołówka), która wyświetli stary i nowy GUID, aby administrator dokładnie widział, co zmienia.
    
- Dodanie walidacji dla listy wyboru, aby wymusić unikalne wartości.
    
- Rozważyć lepsze odcięcie graficzne w Edytorze, np. przez dodanie ciemniejszego tła do środkowej części (formularza), aby odróżnić go od paneli bocznych (Toolbox i ustawienia).
    

---

### 5. Komentarze i wzmianki (@mentions)

**Dlaczego to robimy:**

- Nawarstwienie się zgłoszeń od klientów w temacie wzmianek i komentarzy.
    

**Opis funkcjonalności / rozwiązania:**

- Całkowita refaktoryzacja mechanizmu wzmiankowania.
    
- Zamiast zwykłego pola tekstowego, pole do edycji będzie typu edytowalnego HTML, umożliwiając wstawianie interaktywnych elementów (tokenów wzmianek, a nie zwykłej małpy).
    

**Dalsze kroki:**

- Dokończenie prac (problemy z walidacją po stronie serwera i zapisywaniem zmianek) – maksymalnie 1-2 dni.
    

---

### 6. Dynamiczne wyświetlanie reguł na pasku akcji

**Dlaczego to robimy:**

- Dotychczas wyświetlały się tylko 3 reguły, które czasami nachodziły na siebie, co pogarszało estetykę i użyteczność.
    
- Zgłoszenia klientów, którzy nie rozumieli, dlaczego widzą tylko 3 reguły.
    

**Opis funkcjonalności / rozwiązania:**

- Reguły będą wyświetlane dynamicznie, w zależności od dostępnego miejsca na pasku.
    
- Reguły chowają się do menu typu dropdown.
    
- Dodano parametr dla reguł, który pozwala ukryć regułę na pasku głównym i wyświetlać ją tylko w menu rozwijanym.
    
- Kolejność reguł na pasku akcji jest zachowana zgodnie z ustawieniem (kolejnością).
    
- Logika ma być wynikiem projektowego działania, a nie narzuconą liczbą widocznych reguł.
    

**Dalsze kroki:**

- Nie sprecyzowano w transkrypcji.
    

---

### 7. Podgląd szablonów (Document)

**Dlaczego to robimy:**

- Umożliwienie podglądu szablonów, ponieważ dotychczas była tylko opcja podglądu załączników.
    
- Klienci nie mieli, gdzie pokazywać regulaminu pracy i załączali ten sam dokument do setek spraw, zapychając bazę.
    

**Opis funkcjonalności / rozwiązania:**

- Możliwość podglądu szablonu.
    
- Dodano możliwość ładowania kolejnych stron (przyciskiem "Załaduj kolejne strony").
    
- Opcja wyświetlania w pełnym ekranie.
    
- Domyślną akcją przy kliknięciu szablonu pozostaje generowanie pliku (np. umowy), a nie szybki podgląd, aby uniknąć regresu dla obecnych użytkowników, którzy znają dotychczasowe działanie.
    

**Dalsze kroki:**

- Dopracowanie funkcjonalności (obracanie nie działa, wyjście z pełnego ekranu wraca do załączników zamiast do szablonów).
    
- Rozważenie maksymalnego MVP tego projektu, ponieważ klient źle obsłużył sytuację.
    

---

### 8. Komunikator (Messenger)

**Dlaczego to robimy:**

- Dokończenie prac w ramach MVP.
    

**Opis funkcjonalności / rozwiązania:**

- Komunikator wdrożony u klienta (Movi).
    
- Zmieniona inicjacja nowej konwersacji:
    
    - Wybór jednego użytkownika – konwersacja 1:1.
        
    - Wybór więcej niż jednego użytkownika – konwersacja grupowa z możliwością nadania nazwy.
        
    - Wybór grupy (jednej) z modelu – konwersacja oparta na grupie modelowej z automatyczną synchronizacją użytkowników (dodawanie/usuwanie z grupy równoznaczne z dodaniem/usunięciem z czatu).
        
- W czatach opartych na grupie modelowej, dodany użytkownik widzi całą historię, a usunięty przestaje widzieć konwersację (w tym archiwalną).
    
- W grupach opartych na pojedynczych użytkownikach, przy dodawaniu można określić, czy udostępniamy całą historię, czy od danego momentu. Usunięty użytkownik traci cały czat.
    

**Dalsze kroki:**

- Oczekiwanie na uwagi ze strony klienta.
    
- Przygotowanie instrukcji i krótkiej prezentacji dla potrzeb wewnętrznych i marketingu.
    

---

### 9. Funkcja wysyłki do Docer (Docer Send)

**Dlaczego to robimy:**

- W przypadku dużych dokumentów (np. 200 stron) wysyłanie wszystkich stron jest nieefektywne.
    
- Wcześniej należało ręcznie ustawiać limity.
    

**Opis funkcjonalności / rozwiązania:**

- W funkcji do wysyłki do Docer (dla PDF) dodano opcje ustawienia limitu wysyłanych stron.
    
- Parametry do ustawienia: `pdf first pages` (domyślnie 10) i `pdf last page` (domyślnie 3).
    
- Ustawienie obu na 0 powoduje wysłanie wszystkich stron.
    
- Dla starych klientów, u których nie było tego ustawienia, domyślnie zostanie ustawione 10 pierwszych i 3 ostatnie.
    
- Dodano opcję, że mapowanie tabelki do pola tekstowego wpisze Jason tych produktów, aby uniknąć tworzenia zbyt wielu spraw.
    

**Dalsze kroki:**

- Nie sprecyzowano w transkrypcji.
    

---

### 10. Repozytorium plików

**Dlaczego to robimy:**

- Nie sprecyzowano w transkrypcji.
    

**Opis funkcjonalności / rozwiązania:**

- Repozytorium plików będzie osobnym, licencjonowanym modułem, tak jak komunikator.
    
- Prace ruszają w kolejnym sprincie.
    

**Dalsze kroki:**

- Trwają prace nad rozpisywaniem i potwierdzeniem części backendowej.
    
- Przewidzenie w wymaganiach, że będzie to oddzielnie licencjonowany moduł.
    
- Rozmowa o środowisku do testów (mniej pilne).
    

---

Chciałbyś, abym zagłębił się w któryś z przedstawionych tematów lub wygenerował notatkę na podstawie innej transkrypcji?
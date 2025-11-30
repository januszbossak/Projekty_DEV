

### Spotkanie rady architektów z dnia 12 sierpnia 2025

---

#### 1. Usprawnienie mechanizmu przesyłania załączników
[[Projekty/Integracje/Integracje-REST-multipart/README|README]]

- **Ryzyko:**
    - Obecna metoda przesyłania plików oparta na indywidualnych parach klucz-wartość w nagłówkach jest nieelastyczna, nieintuicyjna i generuje nadmiarową liczbę parametrów, co utrudnia zarządzanie.

- **Proponowane rozwiązanie:**
    - Zastąpienie obecnego mechanizmu standardem `multipart/form-data`.
    - Wprowadzenie ustrukturyzowanej obsługi wielu dokumentów jako pojedynczego parametru (np. tablicy obiektów `documents`), gdzie każdy obiekt zawierałby nazwę pliku i jego zawartość w formacie Base64.

- **Decyzja:**
    - Zdecydowano o wdrożeniu nowego mechanizmu opartego na `multipart/form-data`, aby uprościć proces i zwiększyć jego elastyczność.

- **Zadania:**
    - **Janusz:** Utworzył zadanie deweloperskie w celu implementacji nowej funkcjonalności.

---

#### 2. Problem kompatybilności wstecznej interfejsu IJob

- **Ryzyko:**
    - Rozszerzenie istniejącego interfejsu `IJob` o nowe pole spowodowało błędy wykonania we wszystkich istniejących implementacjach (jobach), które nie zostały zaktualizowane. Problem ten doprowadził do awarii na środowisku testowym.

- **Proponowane rozwiązanie:**
    - Zamiast modyfikować wspólny interfejs, stworzyć nowy, dedykowany interfejs, który będzie implementowany tylko przez te joby, które wymagają nowej funkcjonalności.
    - Rozważano również dodanie domyślnej implementacji w klasie bazowej, jednak zostało to odrzucone jako mniej bezpieczne.

- **Decyzja:**
    - Utrzymane zostaje rozwiązanie polegające na wykorzystaniu nowego, osobnego interfejsu, aby zapobiec podobnym problemom z kompatybilnością w przyszłości.

- **Zadania:**
    -

---

#### 3. Wprowadzenie testów snapshotowych dla publicznego API

- **Ryzyko:**
    - Brak automatycznej kontroli nad zmianami w publicznych interfejsach i metodach kluczowych bibliotek prowadzi do przypadkowego łamania kompatybilności wstecznej.

- **Proponowane rozwiązanie:**
    - Stworzenie nowego rodzaju testu jednostkowego, który będzie działał na zasadzie "snapshotu".
    - Test będzie generował i utrzymywał plik zawierający sygnatury wszystkich publicznych metod. Przy każdym uruchomieniu, aktualny stan API będzie porównywany z zapisanym snapshotem. Niezgodność będzie sygnalizowała potencjalne złamanie kontraktu API i powodowała błąd testu.

- **Decyzja:**
    - Pomysł został zaakceptowany jako wartościowy sposób na wczesne wykrywanie niekontrolowanych zmian i podniesienie stabilności systemu.

- **Zadania:**
    - **Adrian:** W miarę dostępności czasowej, przygotuje prototyp mechanizmu testów snapshotowych.

---

#### 4. Niespójności w działaniu zastępstw dla grup użytkowników

- **Ryzyko:**
    - Stary i nowy mechanizm obsługi zastępstw działają w niespójny sposób. Stary mechanizm pozwala osobie zastępującej widzieć zadania przypisane do grup, do których należy osoba zastępowana, podczas gdy nowy tego nie robi. Może to prowadzić do błędów logicznych oraz problemów wydajnościowych.

- **Proponowane rozwiązanie:**
    - Ujednolicenie działania obu mechanizmów.
    - Wprowadzenie logiki, która automatycznie będzie stosować zastępstwa dla grup jednoosobowych, często używanych do definiowania ról (np. "Dyrektor Finansowy").
    - Dodanie w panelu administracyjnym opcji (checkboxa) pozwalającej na jawne włączenie mechanizmu zastępstw dla dowolnej grupy, niezależnie od liczby jej członków.

- **Decyzja:**
    - Zostanie zaimplementowane rozwiązanie dwuetapowe. Po pierwsze, mechanizm zostanie zmodyfikowany tak, aby domyślnie obsługiwał zastępstwa dla grup jednoosobowych. Po drugie, zostanie dodana explicitna opcja konfiguracyjna do włączania tej funkcjonalności dla pozostałych grup.

- **Zadania:**
    - **Piotr:** Zaimplementuje logikę automatycznej obsługi zastępstw dla grup jednoosobowych oraz doda odpowiednią opcję konfiguracyjną w interfejsie zarządzania grupami.

---

#### 5. Możliwość definiowania szerokości kolumn w tabelach na formularzach [[Szerokość kolumn w tabelach]]

- **Ryzyko:**
    - Brak kontroli nad szerokością kolumn w tabelach formularzy prowadzi do nieoptymalnego wykorzystania przestrzeni ekranu. Kolumny z krótką zawartością są zbyt szerokie, co utrudnia czytelność i ergonomię interfejsu.

- **Proponowane rozwiązanie:**
    - Wykorzystanie istniejących, ale nieużywanych pól w bazie danych, aby umożliwić definicję stylów CSS dla kolumn.
    - W interfejsie użytkownika udostępnić na początek jedynie opcje ustawienia szerokości (`width`) oraz zawijania tekstu.

- **Decyzja:**
    - Funkcjonalność zostanie zaimplementowana. System będzie odczytywał z bazy danych zdefiniowane style, ale po stronie aplikacji będzie parsował i aplikował tylko predefiniowany, bezpieczny zestaw atrybutów (szerokość, zawijanie), ignorując wszelkie inne wpisy, aby zapewnić bezpieczeństwo.

- **Zadania:**
    - Zostanie utworzone zadanie deweloperskie na realizację tej funkcjonalności.

---

#### 6. Poprawa kolorowania danych w raportach z agregacją

- **Ryzyko:**
    - Funkcja kolorowania z użyciem gradientu w raportach tabelarycznych działa nieprawidłowo, ponieważ wylicza zakres wartości (minimum i maksimum) tylko na podstawie danych widocznych na bieżącej stronie, a nie na podstawie całego zbioru danych raportu.

- **Proponowane rozwiązanie:**
    - Zmodyfikować mechanizm tak, aby przed wygenerowaniem gradientu pobierał zakres wartości z całego wyniku zapytania raportu, zapewniając spójną i poprawną wizualizację na wszystkich stronach.

- **Decyzja:**
    - Wstępne poprawki dla raportów typu Pivot i mapy zostały już zaimplementowane i przekazane do testów. W przyszłości rozważone zostanie wprowadzenie bardziej zaawansowanych opcji, np. definiowania konkretnych progów kolorystycznych.

- **Zadania:**
    - **Janusz:** Przetestuje wprowadzone poprawki i przekaże informację zwrotną.

---
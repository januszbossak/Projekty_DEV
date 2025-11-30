[[Rada architektów 2025-10-14]] [[2025-09-02 wtorek]]

### Spotkanie rady architektów z dnia 2 września 2025

---

#### 1. Usprawnienie Procesu Tworzenia Dokumentacji przy Użyciu AI

- **Ryzyko:**
    - Obecny proces tworzenia dokumentacji jest nieefektywny i czasochłonny.
    - Komunikacja werbalna jest dominująca, ale jej treść pozostaje nieustrukturyzowana i nie jest efektywnie wykorzystywana.
    - Nagrania ze spotkań są rzadko przetwarzane na konkretne dokumenty.
    - Ręczne pisanie artykułów i dokumentacji projektowej jest procesem powolnym, co opóźnia przejście od pomysłu do realizacji.

- **Proponowane rozwiązanie:**
    - Wdrożenie nowego procesu opartego na narzędziach AI w celu znacznego przyspieszenia tworzenia dokumentacji.
    - Proces zakłada nagrywanie dyskusji, automatyczną transkrypcję, a następnie przetwarzanie tekstu przez AI (np. Gemini) za pomocą specjalnie przygotowanych promptów.
    - Janusz opracował 6 różnych szablonów promptów dla różnych typów artykułów (funkcjonalne, koncepcyjne, poradniki "how-to", techniczne).
    - Kluczowe zasady to: jeden artykuł powinien dotyczyć jednego, wąsko zdefiniowanego tematu, a terminologia powinna być ujednolicona za pomocą centralnego słownika (np. w arkuszu Google), do którego AI będzie się odwoływać.

- **Decyzja:**
    - Zespół akceptuje proponowane podejście. Ustalono, że należy zacząć stosować tę metodę w praktyce, aby iteracyjnie ją udoskonalać i przyspieszyć procesy wytwórcze, w tym tworzenie dokumentacji projektowej na podstawie spotkań.

- **Zadania:**
    - **Janusz:** Udostępni zespołowi opracowane przez siebie prompty do generowania artykułów.
    - **Janusz:** Na podstawie dyskusji z bieżącego spotkania przygotuje dokumentację projektową dla nowego widoku matrycy uprawnień, wykorzystując opisaną metodę.

---

#### 2. Problem z Analizą Procesu przez Copilota

- **Ryzyko:**
    - Zgłoszono, że narzędzie Copilot ulega awarii podczas próby analizy i streszczenia jednego z procesów stworzonych w systemie, co uniemożliwia automatyczne generowanie jego dokumentacji.

- **Proponowane rozwiązanie:**
    - Należy przekazać problematyczny proces do analizy technicznej w celu zidentyfikowania przyczyny błędu.

- **Decyzja:**
    - Zgłoszenie zostanie zbadane.

- **Zadania:**
    - **Łukasz:** Przekaże Mateuszowi proces, który powoduje awarię Copilota, w celu przeprowadzenia analizy.

---

#### 3. Nowy Interfejs do Zarządzania Szablonami Dokumentów

- **Ryzyko:**
    - Aktualny widok zarządzania szablonami w procesach jest przestarzały i mało funkcjonalny.
    - Brakuje możliwości masowego usuwania szablonów oraz intuicyjnego mechanizmu zmiany ich kolejności.
    - Brak podglądu dokumentu bez jego pobierania.

- **Proponowane rozwiązanie:**
    - **Wersja MVP (Minimum Viable Product):**
        - Przeprojektowanie obecnego widoku z użyciem nowej technologii (React).
        - Wprowadzenie funkcji przeciągnij i upuść (drag-and-drop) do zmiany kolejności szablonów.
        - Dodanie możliwości zaznaczenia wielu szablonów w celu ich jednoczesnego usunięcia.
        - Implementacja funkcji podglądu szablonu bezpośrednio w interfejsie.
        - Uzupełnienie tabeli o brakujące kolumny (np. "Etapy") i dostosowanie układu do obowiązującego w systemie standardu (np. umiejscowienie przycisków i filtrów).
    - **Wersja docelowa (pomysły na przyszłość):**
        - Wprowadzenie widoku kafelkowego z miniaturami podglądu pierwszej strony dokumentu.
        - Dodanie możliwości tworzenia folderów w celu lepszej organizacji szablonów.
        - Rozważenie stworzenia centralnej biblioteki szablonów, które mogłyby być współdzielone między różnymi procesami.

- **Decyzja:**
    - Zdecydowano o realizacji wersji MVP. Priorytetem jest zastąpienie obecnego, przestarzałego widoku nowym, bardziej funkcjonalnym rozwiązaniem. Pomysły na dalszy rozwój zostały odnotowane do realizacji w przyszłości.

- **Zadania:**
    - **Damian:** Zaktualizuje prototyp, dostosowując go do standardów wizualnych systemu, i przygotuje go do finalnego omówienia na spotkaniu projektowym (design).

---

#### 4. Nowy Projekt Matrycy Uprawnień dla Pól Formularza

- **Ryzyko:**
    - Obecny interfejs do zarządzania uprawnieniami do pól jest nieintuicyjny i niewygodny, szczególnie w przypadku rozbudowanych procesów.
    - Masowa edycja uprawnień jest problematyczna, a wizualizacja dziedziczenia uprawnień z sekcji jest niejasna.

- **Proponowane rozwiązanie:**
    - Kamil zaprezentował prototyp nowego, przeprojektowanego widoku matrycy uprawnień.
    - Wszystkie pola, w tym te zagnieżdżone w tabelach, będą widoczne na jednym ekranie.
    - Wprowadzona zostanie ulepszona funkcja masowej edycji: będzie można zaznaczyć wiele pól i zmienić ich uprawnienia (np. na "tylko do odczytu") tylko dla jednego, wybranego etapu, bez resetowania ustawień na pozostałych etapach.
    - Dziedziczenie uprawnień z nadrzędnej sekcji będzie wyraźnie oznaczone graficznie.
    - W celu ułatwienia pracy z dużymi procesami dodane zostaną filtry pozwalające na ukrywanie wybranych sekcji lub etapów procesu.
    - Układ będzie responsywny – przy dużej liczbie etapów etykiety tekstowe zostaną zastąpione samymi ikonami, aby zmieścić więcej kolumn na ekranie.

- **Decyzja:**
    - Prototyp został zaakceptowany jako kierunek rozwoju. Uznano, że proponowane zmiany, zwłaszcza w zakresie edycji masowej i filtrowania, znacznie usprawnią pracę. Projekt jest gotowy do rozpoczęcia implementacji.

- **Zadania:**
    - **Kamil:** Przygotuje makiety pokazujące widok dla procesów o małej i dużej liczbie etapów, aby zwizualizować działanie responsywności interfejsu.
    - **Kamil:** Uzupełni projekt o mechanizmy filtrowania po sekcjach i etapach.
    - **Kamil:** Zleci Filipowi pierwsze zadanie implementacyjne, polegające na stworzeniu widoku nowej matrycy w trybie tylko do odczytu.
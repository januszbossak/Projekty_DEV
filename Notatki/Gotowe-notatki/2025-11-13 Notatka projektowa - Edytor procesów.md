# Notatka projektowa – 2025-11-13 – Edytor procesów

**Data:** 2025-11-13
**Temat główny:** Przegląd postępów prac nad Edytorem procesów (Matryca uprawnień, Lista pól, Edytor diagramu)

**Powiązane projekty:**
- `moduly/Edytor-procesow`

**Uczestnicy:** Kamil Dubaniowski, Przemysław Sołdacki, Janusz Bossak, Piotr Buczkowski, Damian Kaminski, Przemysław Rogaś

---

## 1. Matryca uprawnień – zmiany w oznaczeniach dziedziczenia

**Komponent:** Edytor Formularza (Matryca uprawnień)

### Cel i problem

Uprościć wizualną prezentację dziedziczenia ustawień z sekcji na pola w matrycy uprawnień. Dotychczasowe oznaczenia (łańcuchy, gwiazdki, ramki) tworzyły wizualny nadmiar, utrudniając odczytanie kluczowych informacji (np. które pola mają wyjątki). Konieczne było wypracowanie bardziej czytelnego sposobu prezentacji ustawień dziedziczonych vs. wyjątków.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Ramki wokół wszystkich selektorów (jak w standardowych UI) | Dodanie ramek wokół wszystkich pól wyboru, aby przypominały standardowe komponenty select. Dodatkowo wcięcie dla ustawień pól, szare kursywy dla dziedziczonych wartości, pomarańczowe ramki dla wyjątków. | ❌ Odrzucona – nadmiar elementów graficznych (ramki, ptaszki dropdown), informacja o wyjątkach ginie wśród nadmiaru tuszu |
| Ramki tylko dla wyjątków, bez ramek dla standardowych selektorów | Usunięcie ramek z pól bez wyjątków, pozostawienie tylko pomarańczowych ramek dla wyjątków łamiących dziedziczenie. Dropdown rozwija się po kliknięciu (bez wizualnych ramek). | 💡 Propozycja – Przemek zasugerował bardziej minimalistyczne podejście, gdzie ramka pojawia się tylko przy wyjątkach lub na hover |
| Ramka na hover | Ramka pojawia się dopiero po najechaniu myszką na pole, sygnalizując możliwość edycji. | 💡 Propozycja – zaproponowana przez Przemka jako alternatywa do ramek zawsze widocznych |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

💭 Pomysł Przemka: Usunięcie ramek z wszystkich pól standardowych (bez wyjątków), pozostawienie wyłącznie pomarańczowych ramek dla wyjątków. Ramki lub inne oznaczenia edytowalności mogą pojawiać się na hover. Cel: zmniejszenie nadmiaru elementów graficznych, poprawa czytelności.

**Uwaga:** Damian Kaminski był przeciwny hoverowi z powodu możliwości "skakania" układu. Przemek zasugerował, że można zaprojektować hover bez skakania layoutu.

**Szczegóły techniczne:**
- Wcięcie dla ustawień pól (odróżnienie od ustawień sekcji)
- Szare kursywy dla wartości dziedziczonych z sekcji
- Pomarańczowa ramka dla wyjątków łamiących reguły dziedziczenia
- Usunięcie łańcuchów i gwiazdek (oznaczenia dziedziczenia)
- Dropdown rozwija się po kliknięciu (select robiony dopiero w momencie kliknięcia – optymalizacja wydajności ładowania)

### Ograniczenia / Poza zakresem

- Napis "Edycja" (w widoku kompaktowym) może być usunięty w przyszłości – po jednym dniu używania użytkownik będzie wiedzieć, że to edycja

### Punkty otwarte

- Czy zastosować hover dla ramek (z zabezpieczeniem przed skakaniem layoutu)?
- Czy usunąć napis "Edycja" w widoku kompaktowym?
- Ustalenie ostatecznego wyglądu wizualnego (feedback od zespołu)

---

## 2. Lista pól – przywracanie funkcjonalności ze starego widoku

**Komponent:** Edytor Formularza (Lista pól)

### Cel i problem

Przywrócić w nowej liście pól wszystkie funkcjonalności, które były dostępne w starym widoku. Nowa lista ma uporządkować ustawienia (np. ustawienia ilości kolumn przeniesione bliżej nagłówków sekcji) i poprawić intuicyjność obsługi. Problem: użytkownicy przyzwyczajeni do starego układu oczekują tych samych możliwości w nowym interfejsie.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw. Cel: pełna parzystość funkcjonalna ze starym widokiem.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (w trakcie implementacji)

Przywrócenie wszystkich funkcjonalności starej listy pól w nowym interfejsie. Zmiany wprowadzone w aktualnym sprincie:

**Szczegóły techniczne:**
- **Ustawienia ilości kolumn w sekcji** – dodane (wcześniej były w oderwanym miejscu, teraz przy nagłówkach sekcji)
- **Ustawienia pól** – dostępne w prawym panelu (otwieranym kołem zębatym)
- **Predefiniowane wartości domyślne** – można je ustawiać i wyświetlać na liście
- **Blokowanie pól do edycji** – dostępne
- **Zwiń/Rozwiń wszystko** – dodane przyciski
- **Historia pola** – dostępna (na hover – obecnie zgłoszony bug, że hover nie powinien się włączać automatycznie)
- **Typ pola** – widoczny na liście (dla sekcji zamiast "Typ" pokazana ilość kolumn)

**Format danych:**
- Dedykowane ustawienia dla konkretnych typów pól (np. liczba miejsc po przecinku dla pól numerycznych) przeniesione do prawego panelu (koło zębate)

**Funkcjonalności do dołożenia w kolejnych sprintach:**
- Szybkie przejście do ustawień słownika z poziomu listy (obecnie możliwe tylko z poziomu prawego panelu)
- Link do słownika bezpośrednio przy nazwie pola (zamiast osobnego przycisku)
- Link do definicji procesu dla pól typu "Odnośnik"
- Link do źródła zewnętrznego
- Podgląd nazwy słownika na hover (obecnie nie widać, jaki słownik jest podpięty)
- Poprawka dodawania sekcji (obecnie nieintuicyjne – trzeba jechać na sam dół formularza, aby dodać sekcję)

**Planowany termin:** Koniec sprintu (grudniowa wersja) – wyrównanie parzystości ze starym widokiem

### Ograniczenia / Poza zakresem

- Dodawanie sekcji – odłożone na kolejny sprint (wymaga przemyślenia UX zarówno na liście, jak i w edytorze graficznym)
- Podgląd formatowania dla tekstu statycznego – zgłoszony bug, w trakcie naprawy

### Punkty otwarte

- Czy ilość kolumn w sekcji powinna być wybierana ikonkami (jak w edytorze graficznym) czy dropdownem (jak obecnie na liście)? Kwestia spójności UI.
- Jak zaprojektować intuicyjne dodawanie sekcji z poziomu listy pól?
- Czy lista wartości domyślnych powinna być edytowalna bezpośrednio z listy pól (jak wcześniej) czy tylko przez prawy panel? Decyzja do konsultacji z Salą Wdrożeń.

---

## 3. Edytor diagramu – nowa wersja (MVP)

**Komponent:** Edytor Diagramu

### Cel i problem

Dostarczyć nową wersję edytora diagramu procesów w formie MVP, która będzie działać stabilnie i będzie wizualnie przyjemniejsza od starej wersji. Stary edytor graficzny był rzadko używany, nowy ma być bardziej intuicyjny i wizualnie atrakcyjny.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw. MVP zakłada możliwość rysowania diagramu (dodawanie etapów, połączeń, sekwencji etapów) bez zaawansowanych funkcji edycji reguł.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (wersja beta w grudniu)

Nowy edytor diagramu zostanie wydany jako wersja beta w grudniowej paczce. MVP spełnia założenia: można narysować diagram, dodać etapy, połączenia, sekwencje etapów.

**Szczegóły techniczne:**
- **Dodawanie etapów** – działa
- **Dodawanie połączeń** – działa
- **Sekwencje etapów** – działa
- **Animacje** – ładniejsze niż w starej wersji
- **Edycja reguł na połączeniach** – możliwość dodania reguły, ale brak edytora reguł (domyślnie robi przekazanie z etapu na etap, nic więcej)
- **Przełącznik do starego edytora** – konieczny (na wypadek problemów)

**Ograniczenia:**
- Edytor reguł – nie zaimplementowany w MVP (zostaje stary edytor)
- Edycja etapów – zostaje stary widok (nie jest to rewolucja)
- Prawy panel – planowany w kolejnym sprincie (świadomie odłożony na dalszy tor)

**Planowany termin:** Grudniowa paczka (jako beta)

### Ograniczenia / Poza zakresem

- Edytor reguł – poza MVP
- Edycja szczegółów etapów – poza MVP (zostaje stary interfejs)
- Prawy panel – odłożony na kolejny sprint

### Punkty otwarte

- Testowanie przez zespół po wydaniu grudniowej wersji
- Ewentualne poprawki po testach (planowane testy w Astrafix)

---

## 4. Lista reguł – brak zmian

**Komponent:** Edytor Reguł

### Cel i problem

Potwierdzenie, że lista reguł nie będzie modyfikowana w najbliższym czasie.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw. Brak prac nad listą reguł.

### Decyzja / Sposób realizacji

**Status:** ⏸️ Odroczone

Damian Kaminski i Kamil Dubaniowski potwierdzili, że lista reguł nie jest obecnie w zakresie prac. Zostaje bez zmian.

---

## 5. Roadmapa i priorytety do końca roku

**Komponent:** Organizacja prac (roadmapa)

### Cel i problem

Określenie priorytetów prac do końca roku 2025. Cel: zakończenie i formalny odbiór kluczowych projektów klienckich (WIM, LOT) oraz dostarczenie stabilnej, działającej wersji grudniowej zawierającej nowe edytory.

### Rozważane alternatywy

Jedna propozycja, bez alternatyw. Priorytet: domknięcie otwartych tematów.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Priorytety do końca roku:

1. **WIM** – odbiór przed końcem roku (wszystkie siły na zamknięcie projektu)
   - Komunikator – skutecznie zainstalowany w Zimbrze (prezentacja jutro), drobny błąd do naprawy (Mateusz)
   - Makro z Szafirem – Adrian ma problemy, nie działa poprawnie
   - Repozytorium – największy kawałek do zrobienia

2. **LOT** – po zakończeniu WIM
   - JRWA – szeroki temat wymagający porządków

3. **Grudziowa paczka stabilna**
   - Edytor formularzy (lista pól) – prawie działający
   - Edytor diagramu – MVP, wersja beta
   - Naprawa błędów na bieżąco (jeśli wyjdą problemy w edytorach lub innych komponentach)

4. **Planowanie roadmapy na następny rok** – po odbiorze WIM

**Szczegóły techniczne:**
- Testy stabilności grudniowej paczki na środowisku Astrafox (planowane po kolejnym sprincie)
- Cel: wydanie wersji, której nikt się nie będzie bał zainstalować, bez ryzyka wywrócenia systemu

**Planowany termin:** Koniec grudnia 2025

### Punkty otwarte

- Czy komunikator zostanie formalnie odebrany przez WIM?
- Czy makro z Szafirem zostanie naprawione przed końcem roku?
- Kiedy dokładnie planowane są testy na Astrafox?

---

## Punkty do dalszej dyskusji (globalne)

- Konsultacja z Salą Wdrożeń na temat edytowalności listy wartości domyślnych bezpośrednio z listy pól
- UX dodawania sekcji w edytorze formularzy (zarówno lista pól, jak i edytor graficzny)
- Spójność UI: wybór ilości kolumn w sekcji (ikonki vs. dropdown)
- Testowanie grudniowej paczki na Astrafox

**Data:** 2025-12-09
**Typ:** Spotkanie projektowe
**Temat główny:** Design - Edytor formularzy

**Źródło:** [Transkrypcja](../Transkrypcje/oczyszczone-archiwum/2025-12-09 Design - transkrypcja - część 1.md)

---

## 1. Prawy panel edytora formularzy - wyróżnienie wizualne

**Komponent:** Edytor Formularzy

### Kontekst i cel

Konsultanci zgłaszają zarzut, że prawy panel ustawień pól w edytorze formularzy jest zbyt podobny do samego formularza. Po otwarciu prawego panelu użytkownik na pierwszy rzut oka może nie rozpoznać, że to jest panel ustawień, a nie część formularza. Problem dotyczy zarówno widoku graficznego edytora, jak i widoku listy pól - oba używają wspólnego prawego panelu. Zarzut dotyczy głównie podobieństwa sekcji i pól do uzupełnienia, które wyglądają identycznie jak na formularzu głównym.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Usunięcie zakładek, nagłówki sekcji | Pozbycie się zakładek, wyświetlanie wszystkich sekcji rozwiniętych z nagłówkami (bez zwijania) | ✅ Wybrana - poprawia ergonomię dla Piotra Buczkowskiego |
| Cień wokół prawego panelu | Dodanie box-shadow wokół całego prawego panelu | ✅ Wybrana - minimalne wyróżnienie |
| Szare tło panelu, białe sekcje | Odwrócenie kontrastu względem formularza (na formularzu sekcje szare, pola białe) | ⏸️ Odroczona - do rozważenia w przyszłości |
| Zakładki po lewej stronie | Zmiana układu na zakładki pionowe (jak w module raportowym) | ❌ Odrzucona - wymagałoby uspójnienia z innymi miejscami |
| Kontekstowe panele | Różne panele w zależności od kontekstu (właściwości, dane podstawowe osobno) | ❌ Odrzucona - zwiększa liczbę kliknięć, mniejsza ergonomia |

### Decyzja / Ustalenie

**Status:** ✅ Zatwierdzone

Wprowadzone zmiany:
- Usunięcie zakładek - wszystkie sekcje wyświetlane od razu rozwinięte z nagłówkami
- Usunięcie nagłówka "Dane podstawowe" - nie wnosi wartości
- Dodanie cienia wokół prawego panelu (box-shadow) - wyróżnia panel od formularza
- Dodanie linii pod nagłówkiem sekcji w kolorze typu pola - kontekstowe wyróżnienie
- Zachowanie mechanizmu zwijania/rozwijania sekcji z pamięcią w local storage (dłuższa pamięć - 30 dni)

**Szczegóły techniczne:**
- Prawy panel wspólny dla widoku graficznego i widoku listy pól
- Sekcje: Właściwości (specyficzne ustawienia dla typu pola), Informacje techniczne
- Wartość domyślna przeniesiona do właściwości na sam koniec (rzadko używana)
- Podpowiedź pozostaje w danych podstawowych (zachęta do uzupełniania przez konsultantów)

### Ograniczenia / Poza zakresem

- Nie wprowadzamy szarego tła panelu z białymi sekcjami - zostaje do rozważenia w przyszłości
- Nie zmieniamy układu na zakładki pionowe - wymagałoby uspójnienia z całym systemem

### Feedback / Uwagi uczestników

- **Piotr Buczkowski:** Zgłaszał problem z koniecznością ciągłego wchodzenia w prawy panel i rozwijania właściwości - rozwiązane przez usunięcie zakładek
- **Szymek:** Zgłaszał zarzut o podobieństwo prawego panelu do formularza
- **Przemek Rogaś:** Wyczyścił prawy panel po zgłoszeniach z poprzedniego tygodnia, przeniósł akcje

### Zadania / Dalsze kroki

- **Kamil Dubaniowski:** Finalizacja zmian wizualnych prawego panelu
- **Przemek Rogaś:** Poprawa akcji usunięcia pola (przerwana podczas zmian)

### Punkty otwarte

- Czy szare tło panelu z białymi sekcjami będzie potrzebne w przyszłości?
- Czy mechanizm pamięci zwijania/rozwijania (30 dni) będzie wystarczający?

---

## 2. Puste pola w edytorze graficznym - numeracja i reguły

**Komponent:** Edytor Formularzy

### Kontekst i cel

W edytorze graficznym formularzy pola puste (placeholdery) są automatycznie tworzone po wrzuceniu pola do formularza. Problem dotyczy numeracji tych pól - przy dodawaniu nowego pola następuje renumeracja wszystkich pustych pól, co może powodować problemy z regułami, które odwołują się do konkretnych numerów pustych pól (np. "puste 2", "puste 3"). Reguły często wykorzystują puste pola do sterowania widocznością - ukrywają pole na danym etapie, a w jego miejsce pokazują puste pole, aby nie przesuwać innych pól.

### Zidentyfikowane ryzyka

- Renumeracja pustych pól przy dodawaniu nowych pól może zepsuć istniejące reguły odwołujące się do konkretnych numerów
- Brak świadomości, że dane pole puste istnieje - nie widać tekstu "puste 1", "puste 2" w edytorze graficznym
- Nie można edytować ustawień pola pustego z poziomu edytora graficznego

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Auto-increment numeracji | Nowe puste pole otrzymuje najwyższy numer (np. puste 58), bez renumeracji istniejących | 💡 Propozycja - wymaga weryfikacji z Piotrem |
| Wyświetlanie tekstu "puste X" | W edytorze graficznym widoczny tekst identyfikujący pole puste | 💡 Propozycja - część MVP |
| Edycja ustawień pola pustego | Możliwość wejścia w ustawienia pola pustego z edytora graficznego | ⏸️ Odroczona - kolejne MVP |

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji

Wymagane zmiany:
- Wyświetlanie tekstu "puste 1", "puste 2" w edytorze graficznym - użytkownik musi widzieć, że to jest pole puste
- Możliwość edycji ustawień pola pustego z poziomu edytora graficznego
- Zmiana numeracji - nowe puste pole powinno otrzymywać auto-increment numer (najwyższy dostępny), bez renumeracji istniejących pól

**Szczegóły techniczne:**
- Pola puste tworzą się automatycznie po wrzuceniu pola do formularza
- Pola puste są faktycznymi polami w bazie danych
- Reguły mogą sterować widocznością pustych pól (ukrywać/pokazywać)
- Obecnie przy dodawaniu nowego pola następuje renumeracja wszystkich pustych pól

### Ograniczenia / Poza zakresem

- Zarządzanie wierszem jako takim (koncepcja z czasów Christiny) - pozwalające na wybór "to albo to" w jednym miejscu - pozostaje poza zakresem obecnych zmian

### Zadania / Dalsze kroki

- **Kamil Dubaniowski:** Weryfikacja z Piotrem Buczkowskim mechanizmu numeracji pustych pól
- **Piotr Buczkowski:** Sprawdzenie, kiedy pola puste są zapisywane do bazy danych (przy dodaniu czy przy wyjściu z edytora)

### Punkty otwarte

- Czy auto-increment numeracji pustych pól nie wpłynie negatywnie na inne mechanizmy?
- Kiedy dokładnie pola puste są zapisywane do bazy - przy dodaniu czy przy zapisie formularza?

---

## 3. Układ formularza przy otwartym prawym panelu

**Komponent:** Edytor Formularzy

### Kontekst i cel

Przy otwarciu prawego panelu w edytorze graficznym następuje zmiana układu formularza - z 3-kolumnowego na 2-kolumnowy (lub z 4-kolumnowego na 3-kolumnowy). To powoduje, że użytkownik widzi jeden układ, a po otwarciu prawego panelu formularz zmienia się wizualnie, co może być mylące. Problem szczególnie widoczny przy dodawaniu nowych pól - miejsce, w którym użytkownik upuszcza pole, może nie odpowiadać rzeczywistemu miejscu dodania ze względu na zmianę układu.

### Decyzja / Ustalenie

**Status:** 💡 Propozycja

Docelowo prawy panel nie powinien wpływać na zmianę układu kolumn formularza. Jeśli formularz ma układ 3-kolumnowy, przy otwarciu prawego panelu kolumny powinny pozostać 3, tylko węższe. To ważniejsze niż proporcjonalność szerokości pól, ponieważ edytor służy do pracy nad formularzem, a nie jako formularz do pracy użytkownika końcowego.

**Szczegóły techniczne:**
- Obecnie przy otwarciu prawego panelu następuje automatyczne przełączenie układu (np. z 3 na 2 kolumny)
- Drag & drop działa poprawnie w wyznaczonych miejscach
- Problem szczególnie widoczny w pierwszej linii formularza

### Zadania / Dalsze kroki

- **Przemek Rogaś:** Rozważenie implementacji zachowania liczby kolumn przy otwarciu prawego panelu (zmniejszenie szerokości zamiast liczby kolumn)

---

## 4. Repozytorium - uprawnienia

**Komponent:** Repozytorium

### Kontekst i cel

Trwają prace nad implementacją uprawnień w module Repozytorium. Adrian przygotował dokumentację szkoleniową dotyczącą uprawnień, która została przygotowana na przykładzie z Piotrem i Adrianem. Dokumentacja ma przygotować bazę pod dzielenie uprawnień w przyszłości, ale obecnie realizowany jest tylko MVP - uprawnienia na najwyższym poziomie, bez dzielenia.

### Decyzja / Ustalenie

**Status:** 🔄 W trakcie

- Dokumentacja przygotowana przez Adriana
- Baza danych i metody przygotowane pod przyszłe rozbudowy
- Obecnie realizowany MVP - tylko najwyższy poziom uprawnień
- Filip pokazywał już działające uprawnienia
- Planowane zakończenie: dzisiaj maksymalnie jutro rano
- Wydanie na środowisko developerskie i rozpoczęcie pełnych testów
- Planowane wdrożenie u klienta w tym tygodniu

### Zadania / Dalsze kroki

- **Damian Kamiński, Adrian Kotowski, Filip Liwiński:** Finalizacja uprawnień (dzisiaj/jutro rano)
- **Filip Liwiński:** Podpięcie tabeli uprawnień w bazie danych (Anna Skupińska już przygotowała)
- **Zespół testowy (Barbara, Oktawia):** Pełne testy po wydaniu na środowisko developerskie

---

## 5. Neuca - profil użytkownika i zastrzeżenia do Mikołaja

**Komponent:** Interfejs użytkownika / Moduł raportowy

### Kontekst i cel

Neuca zgłasza brakujące informacje w profilu użytkownika - brakuje historii aktywności zmian na koncie (np. dodanie do grupy, usunięcie z grupy). Informacje te są dostępne w module administracyjnym (Activity Log), ale nie są widoczne z perspektywy konkretnego użytkownika w jego profilu. Dodatkowo, na spotkaniu z Neucą padły zastrzeżenia do modułu Mikołaja - głównie dotyczące listy procesów, listy raportów oraz pól wymaganych na formularzu sprawy.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Raport bazujący na źródle danych | Tymczasowe rozwiązanie - raport w module raportowym korzystający z źródła danych | 💡 Propozycja - rozwiązanie tymczasowe |
| Poprawa interfejsu profilu użytkownika | Dodanie brakujących informacji do profilu użytkownika | ⏸️ Odroczona - profil użytkownika będzie Reactowy za maksymalnie pół roku |
| Poprawa modułu Mikołaja | Uwzględnienie zastrzeżeń Neuca (lista procesów, lista raportów, pola wymagane) | ✅ Zatwierdzone - do realizacji |

### Decyzja / Ustalenie

**Status:** 💡 Propozycja (profil) / ✅ Zatwierdzone (Mikołaj)

**Profil użytkownika:**
- Zgłoszenie leży od połowy roku
- Perspektywa pół roku do przejścia na React
- Tymczasowe rozwiązanie: raport bazujący na źródle danych (Damian przygotował zapytanie SQL)
- Problem z zapytaniem SQL - arithmetic overflow na środowisku developerskim (do sprawdzenia przez Damiana)

**Moduł Mikołaja:**
- Ustalenia ze spotkania z Neucą zapisane przez Janusza (nagranie dostępne)
- Główne zastrzeżenia: lista procesów, lista raportów, pola wymagane na formularzu sprawy
- Wymaga poprawy zgodnie z ustaleniami

**Szczegóły techniczne:**
- Zapytanie SQL przygotowane przez Damiana do Activity Log
- Problem: arithmetic overflow przy użyciu źródła danych (do weryfikacji)
- Zapytanie zawiera JOINy do uzupełnienia nazw

### Zadania / Dalsze kroki

- **Damian Kamiński:** Sprawdzenie zapytania SQL na swoim demo (weryfikacja arithmetic overflow)
- **Łukasz Bott:** Zgłoszenie błędu arithmetic overflow do analizy
- **Eryk:** Pomoc w konfiguracji źródła danych dla raportu (tymczasowe rozwiązanie)
- **Janusz Bossak:** Przygotowanie transkrypcji i podsumowania spotkania z Neucą
- **Zespół:** Realizacja poprawek modułu Mikołaja zgodnie z ustaleniami

### Punkty otwarte

- Czy warto poświęcać czas na poprawę profilu użytkownika, skoro za pół roku będzie Reactowy?
- Jaka jest przyczyna arithmetic overflow w zapytaniu SQL?

---

## 6. Rossmann - problem z synchronizacją kartoteki

**Komponent:** Integracje

### Kontekst i cel

Rossmann eskaluje problem z synchronizacją kartoteki. Istnieje kartoteka w systemie, ale odpowiedź AMODIT wskazuje, że nie można utworzyć sprawy, podczas gdy powinna być informacja "nie można zaktualizować". Problem wymaga analizy - kartoteka istnieje, duplikat nie istnieje, ale system nieprawidłowo interpretuje sytuację.

### Decyzja / Ustalenie

**Status:** 🔍 Do weryfikacji

- Problem eskaluje Rossmann
- Przyczyna pośrednio nieznana - kartoteka istnieje, ale system odpowiada błędnie
- Wymaga analizy przez Adriana po powrocie ze szkolenia
- Eryk prosił o wsparcie Damiana, ale temat przekazany do Adriana

### Zadania / Dalsze kroki

- **Adrian Kotowski:** Analiza problemu po powrocie ze szkolenia (dzisiaj wieczorem)
- **Eryk:** Eskalacja do Adriana

### Punkty otwarte

- Jaka jest dokładna przyczyna błędnej odpowiedzi systemu?
- Czy to problem po stronie integracji czy logiki biznesowej?





[[Rada architektów 2025-10-14]] [[2025-08-28 czwartek]]

### Spotkanie Rady Architektów z dnia 28 sierpnia 2025

---

#### 1. Unifikacja zakładek "Integracje" i "Stany systemowe"

- **Ryzyko:**
    - Brak pełnej synchronizacji wiedzy na temat postępu prac z powodu nieobecności członka zespołu.

- **Proponowane rozwiązanie:**
    - Zorganizowanie dedykowanego spotkania w mniejszym gronie (Kamil, Adrian, Przemek) w celu omówienia szczegółów technicznych i dalszych kroków.

- **Decyzja:**
    - Temat zostanie omówiony na osobnym spotkaniu. Prace front-endowe polegające na scaleniu zakładek zostały już zakończone. Pozostaje do wykonania implementacja po stronie backendu.

- **Zadania:**
    - **Kamil:** Zorganizować spotkanie z Adrianem i Przemkiem w celu omówienia implementacji backendu.

---

#### 2. Rejestrowanie użycia funkcji `delete case` (trwałego usuwania spraw)

- **Ryzyko:**
    - Brak trwałego rejestru operacji usuwania spraw, co jest problemem zgłaszanym przez klientów. Obecne logi systemowe są okresowo czyszczone, przez co znika historia tych działań.

- **Proponowane rozwiązanie:**
    - Początkowo rozważano utworzenie nowej, dedykowanej zakładki w panelu administracyjnym do przeglądania historii usuniętych spraw.
    - Ostatecznie zaproponowano, aby wykorzystać istniejący mechanizm "Aktywności użytkownika", który jest dostępny dla administratorów i nie jest powiązany z cyklem życia sprawy.

- **Decyzja:**
    - Operacja trwałego usunięcia sprawy (zarówno z poziomu reguły `delete case`, jak i z kosza) będzie rejestrowana jako wpis w logu "Aktywność użytkownika".
    - Każdy wpis będzie zawierał minimum: datę, identyfikator użytkownika, który wykonał akcję, numer usuniętej sprawy oraz nazwę procesu, z którego pochodziła.

- **Zadania:**
    - **Łukasz:** Przygotować propozycję projektu/designu dla tego rozwiązania.

---

#### 3. Implementacja edytowalnych tabel do masowego wprowadzania danych (Przypadek PKF)

- **Ryzyko:**
    - Klient zgłasza, że obecny sposób rejestracji czasu pracy jest nieefektywny i pracochłonny. Oczekuje rozwiązania przypominającego tabelę przestawną w Excelu do szybkiego wprowadzania godzin.

- **Proponowane rozwiązanie:**
    - Zaproponowano stworzenie na dashboardzie widoku składającego się z dwóch połączonych raportów: raportu typu pivot (macierz zlecenia/dni) oraz raportu tabelarycznego, w którym po kliknięciu komórki w pivocie wyświetlałby się formularz do edycji szczegółów danego wpisu.

- **Decyzja:**
    - Stwierdzono, że oczekiwania klienta wykraczają poza zakres prac uzgodniony na etapie analizy. Obecnie zaimplementowane rozwiązanie zostało wcześniej zaakceptowane. Wszelkie zmiany w tym obszarze będą traktowane jako nowe wymaganie i podlegają osobnej wycenie.

- **Zadania:**
    - **Damian:** Odszukać dokumentację lub nagrania potwierdzające akceptację przez klienta obecnego sposobu działania w celu uargumentowania stanowiska.

---

#### 4. Obsługa dużych tabel z możliwością masowego zaznaczania (Przypadek WIM)

- **Ryzyko:**
    - Konieczność efektywnego przetwarzania i weryfikacji faktur zawierających setki pozycji. Standardowe tabele w systemie mogą powodować problemy z wydajnością i nie oferują funkcji masowego zaznaczania.

- **Proponowane rozwiązanie:**
    - Wykorzystanie raportu osadzonego na formularzu, który będzie zasilany danymi ze źródła zewnętrznego (np. pozycjami zamówienia z innego systemu).
    - Rozbudowa funkcjonalności raportu o możliwość dodania edytowalnej kolumny z checkboxami, co pozwoli użytkownikowi na zaznaczanie zgodności poszczególnych wierszy.
    - Zwiększenie domyślnego limitu wierszy wyświetlanych na jednej stronie raportu, aby uniknąć problematycznego stronicowania przy dużej ilości danych.

- **Decyzja:**
    - Kierunek rozwoju oparty na rozbudowie raportu ze źródła zewnętrznego został zaakceptowany. Należy przeanalizować techniczne możliwości implementacji.

- **Zadania:**
    - **Piotr:** Przeanalizować możliwość dodania edytowalnej kolumny (checkbox) w raporcie bazującym na źródle zewnętrznym oraz zbadać opcję zwiększenia limitu wierszy.
    - **Damian:** Skonsultować z klientem, czy bardziej użyteczne będzie zaznaczanie pozycji zgodnych, czy tylko tych, które są niezgodne.

---

#### 5. Ujednolicenie palety kolorów na wykresach

- **Ryzyko:**
    - Przy raportach z dużą liczbą serii danych (powyżej 20) kolory zaczynają się powtarzać, co utrudnia analizę.
    - Zaproponowana nowa paleta kolorów, choć żywsza, zawiera odcienie zbyt podobne do siebie, co może negatywnie wpłynąć na czytelność wykresów.

- **Proponowane rozwiązanie:**
    - Dyskutowano dwa podejścia:
        1.  Wprowadzenie kilku serii predefiniowanych, bardziej zróżnicowanych palet kolorów, aby system mógł automatycznie obsłużyć wykresy z 40-60 seriami danych bez powtórzeń.
        2.  Ograniczenie palety do ok. 10 silnie kontrastujących kolorów (zgodnie ze standardami np. Tableau) i wdrożenie mechanizmu automatycznego grupowania danych o niskiej wartości w jedną serię "Pozostałe".

- **Decyzja:**
    - Decyzja została odroczona. Należy skonsultować się ze specjalistą ds. wizualizacji danych w celu wyboru optymalnego rozwiązania, zgodnego z najlepszymi praktykami rynkowymi.

- **Zadania:**
    - **Damian:** Skonsultować temat palet kolorów z Michałem Maliszewskim.
    - **Ania:** Wstrzymać bieżące prace nad implementacją nowej palety kolorów do czasu podjęcia ostatecznej decyzji.
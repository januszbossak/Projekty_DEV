# CHANGELOG - Matryca uprawnień

---

# CHANGELOG - Matryca uprawnień

---

## 2025-10-16 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-16 Notatka projektowa - Edytor procesów.md]
**Kategoria:** #Funkcjonalność #Design

- Implementacja Macierzy uprawnień (realizowana przez Filipa)
- Dyskusja nad wizualizacją ikonek "łańcuszka" (dziedziczenia) – pokazywać ikonę tylko gdy NIE ma dziedziczenia?

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Zaimplementowano ponad MVP:** tryb kompaktowy (obrócone napisy), usunięcie selecta na rzecz ikon (optymalizacja), nowa nawigacja, ikona tarczy.
- **Filtry:** dodano filtrowanie po etapach (min. 1 zaznaczony).
- **Logika:** dodano "Uprawnienie domyślne" (dziedziczone przez etapy bez wyjątków).
- **Wizualizacja:** wyjątki oznaczone gwiazdką (*), tooltipy wyjaśniające status (domyślne/wyjątek).
- **Masowa zmiana:** zaznaczanie wielu pól + edycja wybranych etapów.
- **Feedback:** zasugerowano odwrócenie logiki wizualizacji (wyróżniać tylko wyjątki), dodanie searcha, globalny przełącznik nazw (tech/wyświetlane), opcję "pozostaw bez zmian" w masowej edycji.

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #Design

**Matryca uprawnień - Demo implementacji** ✅
- **Zaimplementowano:**
  - Matryca grupująca sekcje i pola
  - Dziedziczenie uprawnień z sekcji (ikonka dymka)
  - Wizualne wyróżnienie wyjątków (pomarańczowe tło)
  - Edycja bezpośrednio z matrycy
- **Feedback/Zmiany:**
  - Ikony akcji przenieść z prawej do lewego menu (trudno dostępne)
  - Dodać wyjaśnienie osi (wiersze=pola, kolumny=etapy)
  - Dodać filtrowanie etapów (dla dużych procesów)
- **Known issues:** Brak widoku kompaktowego, filtrowanie do poprawy

---

## 2025-09-02 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-09-02 Rada architektów|2025-09-02 Rada architektów]]

**Kategoria:** #Design #Architektura

**Prezentacja:** Kamil Dubaniowski

**Kontekst:**
Projekt matrycy uprawnień dla pól formularza stworzony z wykorzystaniem AI (v0). Obecny interfejs zarządzania uprawnieniami jest nieintuicyjny i wymaga wielu kliknięć. Nowa matryca ma pokazywać wszystkie pola, sekcje i tabele wraz z uprawnieniami na wszystkich etapach procesu w jednym widoku, umożliwiając masowe zmiany uprawnień.

### Zidentyfikowane Ryzyka

- Przy dużej liczbie etapów (10+) matryca może być nieczytelna
- Różne kombinacje uprawnień między polami mogą utrudniać masowe zmiany
- Ryzyko błędów przy masowych zmianach uprawnień

### Decyzja

**Status:** ✅ Zatwierdzone

Wprowadzenie nowej matrycy uprawnień dla pól formularza z następującymi funkcjonalnościami:

### Podstawowe funkcje

- Wyświetlanie wszystkich pól, sekcji i tabel w jednym widoku
- Kolumny dla każdego etapu procesu z uprawnieniami (edycja, odczyt, ukryte, wymagane)
- Dziedziczenie uprawnień z sekcji/tabeli oznaczane specjalnym znacznikiem
- Możliwość zerwania dziedziczenia i ustawienia indywidualnych uprawnień
- Wyjątki per użytkownik (edycja tylko dla X, ukryte dla Y)
- Przełącznik między użytkownikami zewnętrznymi i wewnętrznymi (jeśli włączone w ustawieniach systemowych)

### Wyświetlanie

- **Przy małej liczbie etapów (1-3):** ikona + tekst
- **Przy dużej liczbie etapów (10+):** tylko ikony, zamrożone pierwsze 2 kolumny (nazwa pola, typ)
- Sekcje oznaczone na szaro, możliwość zwijania
- Tabele z możliwością zwijania

### Masowe zmiany

- Zaznaczenie wielu pól → przycisk "Edytuj zaznaczone" na dole
- Okno masowej zmiany uprawnień:
  - Domyślnie: **"Nie zmieniaj"** (pozostaw obecne) dla każdego etapu
  - Możliwość wyboru uprawnienia dla wybranych etapów
  - Zmiana dotyczy tylko głównych uprawnień (edycja, odczyt, ukryte, wymagane)
  - Wyjątki per użytkownik pozostają bez zmian
- Opisowe prezentowanie uprawnień: "Ogólnie edycja, ale tak naprawdę ta edycja jest tylko dla użytkownika X, dla pozostałych pole jest ukryte"

### Filtry

- Filtr po sekcji (zawężenie widoku do wybranej sekcji)
- Filtr po etapie (wyświetlenie tylko wybranych etapów)
- Przydatne przy dużych procesach (15-20 etapów)

### Szczegóły techniczne

- **Technologia:** React
- **Biblioteka UI:** Ant Design (z dostosowaniem)
- Tabele z zaokrągleniami (zgodnie z Ant Design)
- Ikony: dostosowanie do ikon Zender (nie MDI)
- Zamrożone kolumny: pierwsze 2 kolumny przy przewijaniu w poziomie
- Zamrożony nagłówek: przy przewijaniu w pionie

### Uwagi

- Projekt stworzony przez v0, wymaga dostosowania do standardów AMODIT
- v0 nie zawsze poprawnie używa komponentów Ant Design
- Wymagane testowanie z różną liczbą etapów (1-2, 5, 10+)

### Zadania

- **Kamil Dubaniowski:** Dopracowanie szczegółów projektu zgodnie z uwagami
- **Kamil Dubaniowski:** Zwężenie kolumn z uprawnieniami (tekst "Wymagane" jako najdłuższy)
- **Kamil Dubaniowski:** Dodanie opcji "Nie zmieniaj" (pozostaw obecne) w oknie masowej zmiany
- **Kamil Dubaniowski:** Przygotowanie wariantów z różną liczbą etapów (1-2, 5, 10) do testowania
- **Kamil Dubaniowski:** Dodanie filtrów po sekcji i etapie
- **Filip Liwiński:** Przełożenie obecnych uprawnień na nową tabelkę (pierwsze zadanie)
- **Filip Liwiński:** Implementacja funkcjonalności masowej zmiany uprawnień (po pierwszym zadaniu)

### Punkty otwarte

- Jak obsłużyć przypadek, gdy pole ma różne uprawnienia na różnych etapach i użytkownik chce zmienić tylko jeden etap?
- Czy potrzebny jest podgląd uprawnień przed zapisaniem zmian?
- Jak walidować zmiany uprawnień (np. czy wymagane pole może być ukryte)?


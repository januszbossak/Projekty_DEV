# CHANGELOG

## 2025-12-09 | Spotkanie projektowe - Design

**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-09 Design - Edytor formularzy.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-09%20Design%20-%20Edytor%20formularzy.md)

**Kategoria:** #Funkcjonalność #Problem

**Profil użytkownika - brakujące informacje:**
- Neuca zgłasza brak historii aktywności zmian na koncie (np. dodanie do grupy, usunięcie z grupy)
- Informacje dostępne w module administracyjnym (Activity Log), ale nie w profilu użytkownika
- Zgłoszenie leży od połowy roku
- Perspektywa pół roku do przejścia na React
- Tymczasowe rozwiązanie: raport bazujący na źródle danych (Damian przygotował zapytanie SQL)
- Problem z zapytaniem SQL - arithmetic overflow na środowisku developerskim

**Moduł Mikołaja - zastrzeżenia:**
- Główne zastrzeżenia: lista procesów, lista raportów, pola wymagane na formularzu sprawy
- Ustalenia ze spotkania z Neucą zapisane przez Janusza (nagranie dostępne)
- Wymaga poprawy zgodnie z ustaleniami

---

## 2025-12-10 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-10 Omówienie wyceny dla Neuca.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-10%20Omówienie%20wyceny%20dla%20Neuca.md)
**Kategoria:** #Design #Funkcjonalność

- **Rozdzielenie wizualne folderów i procesów:** Wprowadzenie wyraźnego podziału - kafelki folderów w jednej linii, kafelki procesów od nowej linii, dotyczy zakładek Procesy i Raporty
- **Skracanie długich nazw procesów:** Zwiększenie z 2 do 5 linii, ucinanie od środka (początek + wielokropek + koniec) - algorytm jak na załącznikach, dzielenie po połowie pełnymi wyrazami
- **Tooltips - pozycjonowanie i logika:** Tooltip w dół dla pierwszego rzędu (nie zasłania przycisków), tylko dla skróconych nazw, opóźnienie wyświetlania
- **Pola wymagane - walidacja na starcie:** Jeśli ustawienie systemowe wyłączone, od razu po wejściu w sprawę wyświetlamy walidację (belka + komunikaty pod polami)
- **Przycisk "Zapisz" - możliwość ukrycia:** Neuca ma wystawić CR z przypadkiem biznesowym, opcja w ustawieniach procesu do ukrycia przycisku
- **Przycisk "Usuń" dla administratora:** Czerwone "Usuń" w 3 kropkach dla administratora, na pierwszym etapie dodatkowo normalne "Usuń" z roli użytkownika
- **Pogrubienie czcionki folderów:** Odrzucone - rozdzielenie sekcji już wystarczająco wyróżnia, różnica prawie niewyczuwalna
- **Skalowanie kolumn:** Już zrobione w grudniowej wersji - odblokowanie limitu 6 kolumn, kafelki skalują się do szerokości ekranu

---

## 2025-12-04 | Spotkanie projektowe
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-04 Spotkanie projektowe - Omówienie zmian Amodit - Neuca.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-12-04%20Spotkanie%20projektowe%20-%20Omówienie%20zmian%20Amodit%20-%20Neuca.md)  
**Kategoria:** #Design #Funkcjonalność

### Widok kafelków procesów i folderów

**Uzgodnione zmiany (kompromis):**
- ✅ **Rozdzielenie folderów od procesów** - przywrócenie wizualnej przerwy między sekcją folderów a sekcją procesów
- ✅ **Odblokowanie ilości kolumn** - usunięcie limitu 6 kolumn, kafelki będą skalować się do szerokości ekranu (dodawanie nowych kolumn zamiast rozszerzania istniejących)
- 💡 **Pogrubienie nazw folderów** - rozważenie opcji konfiguracyjnej per klient w ustawieniach systemowych (do analizy)
- ℹ️ **Wyśrodkowanie vs ikona z lewej** - pozostaje bez zmian (ikona z lewej, tekst obok) - uzasadnienie: lepsza estetyka przy wielu kafelkach

**Kontekst:** Klient zgłosił uwagi do nowego widoku kafelków. AMODIT wprowadził zmiany na podstawie badań UX z ~200 klientami (szersze kafelki dla długich nazw, usunięcie pogrubienia). Wypracowano kompromis z opcjami konfiguracyjnymi.

### Długie nazwy procesów - zawijanie i ucinanie

**Rozwiązanie dwuetapowe:**
- ✅ **Zawijanie na 3-4 wiersze** z wyśrodkowaniem wizualnym (obecnie: 2 linie + "...")
- ✅ **Dla skrajnie długich nazw:** kropki w środku – wyświetlanie początku i końca nazwy, środek zastąpiony "..." (algorytm po słowach, nie znakach)
- ℹ️ Pełna nazwa zawsze dostępna w tooltipie

**Problem:** Ucinanie nazw po 2 liniach powoduje utratę kluczowych informacji (np. rok w nazwie procesu). Neuca ma wiele procesów z długimi nazwami (255 znaków), które nie są możliwe do skrócenia biznesowo.

### Tooltips/dymki zasłaniające elementy

**Rozwiązanie:**
- ✅ Dla kafelków w pierwszym wierszu tooltip będzie wyświetlany **pod kafelkiem** (zamiast nad), aby nie zasłaniać strzałki cofania i przycisku "Dodaj proces"

### Pola wymagane - wizualizacja i UX

**Kompromis - opcja konfigurowalna per proces:**
- **Opcja 1 (domyślna - nowa):** Delikatne podkreślenie + komunikat o brakujących polach dopiero po kliknięciu "Zapisz" + panel z listą pól wymaganych (klikalne linki)
- **Opcja 2 (konfigurowalna):** Delikatne podkreślenie + komunikat **wyświetlany od razu** (bez konieczności kliknięcia "Zapisz") + panel z listą pól

**Kontekst:** Zmiana z intensywnego pomarańczowego na delikatne podkreślenie była odpowiedzią na zgłoszenia 70-80% klientów. Neuca zgłosiła obawy o czytelność dla użytkowników procesów obsługowych (doświadczenie z własnym systemem WinBiuro: zmiana kolorystyki spowodowała strajk użytkowników przez spadek targetów o 30%).

**Do sprawdzenia:** Kolejność pól w panelu z listą pól wymaganych (powinna odpowiadać kolejności w formularzu)

### Przyciski akcji

**Zmiany zaakceptowane:**
- ✅ Nowa kolorystyka przycisków (jasne z obwódką) - akceptowalna dla Neuca
- ✅ Dynamiczne wyświetlanie przycisków - dostosowanie do szerokości ekranu (zamiast sztywnego limitu 4 przycisków)

### Reorganizacja interfejsu sprawy

**Zmiany:**
- ✅ Zakładka "i" - uporządkowanie (uprawnienia przeniesione do ikony użytkowników, historia do osobnej sekcji)
- 🔍 Przycisk "Usuń sprawę" - przeniesienie do menu "3 kropki" (na czerwono) w następnej wersji - cel: utrudnienie przypadkowego usunięcia

**Punkty otwarte:**
- 💡 Czy będzie opcja ukrycia przycisku "Zapisz" w ustawieniach procesu? (obecnie można ukryć "Usuń", ale nie "Zapisz") - Janusz: można zgłosić CR-kę

### Obrazki na kafelkach procesów - propozycja rozwojowa

**Status:** 💡 Do rozważenia jako rozwój osobny (wycena)

**Propozycja Neuca:** Możliwość wstawiania obrazków na kafelki procesów (zamiast ikony) + opis pod spodem. Wzorowane na wewnętrznym systemie Neuca (Asystent) oraz funkcjonalności "Obszary" w AMODIT.

**Argumenty Neuca:**
- Pozytywny feedback użytkowników (głównie kobiety) - "im bardziej kolorowo, tym chętniej się klika"
- Pokrewne procesy miałyby tę samą ikonkę w różnych kolorach – łatwiejsze szukanie
- W folderach 8-10 procesów (nie 200 na raz)

**Argumenty AMODIT:**
- Przy dużej liczbie procesów (100-200) obrazki stają się szumem informacyjnym
- Funkcjonalność "Obszary" nie spotkała się z dobrym odbiorem innych klientów

**Następne kroki:** Daniel Reszka przekaże screeny propozycji Neuca do analizy

### Podsumowanie spotkania

**Ton:** Konstruktywny, obie strony prezentowały argumenty i szukały kompromisu. AMODIT podkreślał konieczność balansowania potrzeb ~200 klientów, Neuca przedstawiał konkretne problemy użytkowników obsługowych.

**Następne kroki:**
- Daniel Reszka przygotuje podsumowanie mailem
- Zespół AMODIT wdroży uzgodnione zmiany (bez terminów)
- Zespół Neuca przygotuje komunikację dla użytkowników przed wdrożeniem

---

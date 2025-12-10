# CHANGELOG – Trust-Center

---

## 2025-12-01 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Cele sprintu - Planowanie sprintu.md]
**Kategoria:** #Wydanie #Zadanie #Funkcjonalność

- Joby Trust Center wdrożone na produkcji.
- Przetestowano joby Trust Center.
- Wgrano joby na domówkę.
- Wdrożono joby na produkcję (po okresie testowym na domówce).
- Opcjonalna implementacja joba do przestawiania długo nieużywanych dokumentów na wygasłe.

---

## 2025-12-01 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-01 Sprint review.md]
**Kategoria:** #Wydanie #DevOps

- Joby przetestowane i gotowe do wdrożenia na produkcję.
- Wdrożenie na środowisko deweloperskie ("domówka") planowane "jutro".

---

## 2025-11-28 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-28 Notatka projektowa - Połączenie z Marek Dziakowski.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-28%20Notatka%20projektowa%20-%20Połączenie%20z%20Marek%20Dziakowski.md)
**Kategoria:** #Funkcjonalność #Decyzja #Problem

- Klienci potrzebują, aby e-maile z TrustCenter wyglądały jakby pochodziły z ich domeny.
- Odrzucono fizyczne przekierowanie przez serwer klienta ze względu na złożoność i ryzyko.
- Wybrano opcję weryfikacji istniejącej funkcji personalizacji (aliasów) adresu nadawcy e-mail.
- Funkcjonalność personalizacji adresu nadawcy e-mail istniała dla Adecco i Rossmanna.

---

## 2025-11-17 | Planowanie sprintu
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-17 Planowanie sprintu.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-11-17%20Planowanie%20sprintu.md)
**Kategoria:** #Architektura #Zadanie

- Kontynuacja przenoszenia wywołań na poziom usługi.
- Czasowe przejęcie wsparcia przez Mariusza (zastępstwo za Marka).

---

## 2025-11-06 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-06 Rada architektów.md]
**Kategoria:** #Architektura #Decyzja

- Brak ram czasowych dla dokumentów bez określonej daty podpisania (dokument wisi w nieskończoność)
- Wymaga analizy danych: najdłuższe terminy, faktyczny czas zamknięcia procesu
- Rozważana monetyzacja dłuższych terminów przechowywania (14 dni standard, 30/180 dni za dopłatą)
- Zadanie dla Marka Dziakowskiego: zestawienie danych do następnej rady

---

## 2025-11-04 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-04 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Decyzja #Zadanie #Weryfikacja

- Problem z niespójnością statusów dokumentów.
- Wprowadzone mechanizmy: job automatyczny i wywołanie ręczne.
- Weryfikacja możliwości wysyłania dokumentów na czas nieokreślony i mechanizmu wygaszania.
- Zadania dla Marka Dziakowskiego (opis scenariusza, job automatyczny, weryfikacja wygaszania).

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Architektura #Optymalizacja

- Przeniesienie obsługi blockchaina z aplikacji web do Windows Service (analogicznie jak w AMODIT) z powodu pojawiania się bloków poza łańcuchem.

---

## 2025-10-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-27 Spotkanie projektowe - Przegląd projektów.md]
**Kategoria:** #Funkcjonalność #Decyzja #Bug #Architektura

- **SignApp na macOS - MVP 1:** Podstawowy ekran bez opcji "Wyczyść certyfikat". Wydanie wersji prototypowej dla klienta do testów przed certyfikacją.
- **Blockchain/Trust Center - dodawanie dokumentów:** Problem z wyścigiem między serwerami przy dodawaniu dokumentów do blockchaina na produkcji. Pilne zaopatrzenie tematu przez Marka.

---

## 2025-10-20 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-20 Sprint review-codex.md]
**Kategoria:** #Funkcjonalność

- Zmiana domyślnej strony landing page po podpisaniu dokumentu
- Wydano obsługę podpisywania SimplySign na nowych raportach (odwzorowanie starego modułu)
- Planowana obsługa 3 głównych podpisów (Szafir, Szafir 2, SimplySign) oraz Poczty Polskiej
- Problemy z dostępnością zestawu podpisów do testów (potrzebny kompletny zestaw)

---

## 2025-10-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-16 Rada architektów.md]
**Kategoria:** #Architektura #Optymalizacja #Decyzja #Blockchain

- Wydzielenie funkcjonalności dodawania dokumentów do blockchaina do osobnego microservice w Dockerze (Azure Container Instances)
- Rozwiązanie problemu rosnącej liczby wiszących dokumentów w blockchainie poprzez sekwencyjne przetwarzanie zadań przez worker
- Plan wdrożenia w dwóch krokach: microservice bez SignalR, następnie z SignalR dla powiadomień

---

## 2025-10-14 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-14 Rada architektów.md]
**Kategoria:** #Roadmap

- Temat odroczony: Dyskusja o Blockchain, decyzja o sposobie realizacji i kosztach

---

## 2025-10-06 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-06 Sprint review.md]
**Kategoria:** #Funkcjonalność #Design #Bug

- Umożliwiono logowanie Azure w Trust Center (dla osób z dostępem serwisowym)
- Poprawki w ustawieniach Trust Center (data wygaśnięcia, opisy funkcji), poprawione logowanie
- Zidentyfikowano błędy: tekst przycisku logowania Azure, spójność interfejsów logowania z AMODIT, automatyczne wykrywanie bibliotek SignApp Mac

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🚀 Postęp

- **Logowanie OAuth (Microsoft) dla serwisu:** umożliwienie logowania do panelu administracyjnego dokumentu dla adresów e-mail z globalnej puli serwisowej.
- **Globalna pula serwisantów:** tabela w Trust Center zastępująca konieczność dodawania serwisanta do każdej organizacji z osobna.
- **Weryfikacja uprawnień:** sprawdzenie czy e-mail jest w puli serwisowej → dostęp do dokumentu (wymagany link do sprawy).
- **Ograniczenia:** dostęp kontrolowany centralnie (Marek/Daniel), wymagany link do sprawy, nie daje dostępu "przeglądarkowego" do wszystkich dokumentów, tylko via sprawa.

---

## 2025-09-16 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-16 Rada architektów - Przegląd projektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-16%20Rada%20architektów%20-%20Przegląd%20projektów.md)
**Kategoria:** #Bezpieczeństwo #Decyzja

**Bezpieczeństwo nazw plików w powiadomieniach (SMS)** ✅
- **Problem:** Ryzyko wycieku danych osobowych w nazwach plików przesyłanych SMS-em (np. "Umowa Jan Kowalski.pdf").
- **Decyzja:** ✅ Zmiana w Trust Center - używanie "przyjaznej nazwy dokumentu" w SMS-ach (tak jak w mailach), o ile zdefiniowana.
- **Szczegóły:** Konsultanci odpowiedzialni za to, by "przyjazna nazwa" nie zawierała danych osobowych.

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Przycisk zarządzania dokumentem i automatyczne wysyłanie kodu** ✅
- ❌ Odrzucone: Nazwa przycisku "Przejdź" - nieintuicyjna
- ❌ Odrzucone: Ręczne wprowadzenie maila - zwiększa liczbę kliknięć
- ✅ **Zatwierdzone:**
  1. **Zmiana nazwy przycisku:** "Zarządzaj dokumentem w Trust Center" (zamiast "Przejdź")
  2. **Walidacja użytkownika:** Weryfikacja czy użytkownik jest wysyłającym lub administratorem organizacji
  3. **Komunikat błędny:** "Skontaktuj się z administratorem" jeśli brak uprawnień
  4. **Automatyczne wysyłanie maila:** Kod dostępowy wysyłany automatycznie (bez ręcznego wprowadzenia)
  5. **Kompatybilność wsteczna:**
     - E-mail w query string (nowsze wersje) → automatyczne wysłanie kodu
     - Brak e-mail (starsze wersje) → pole do ręcznego wprowadzenia
- **Szczegóły:** Trust Center wymaga podniesienia wersji dla nowej funkcjonalności
- **Zadania:** Marek Dziakowski - implementacja

---
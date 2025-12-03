# CHANGELOG – Logowanie-powiadomien

---

## 2025-09-08 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-08 Sprint review.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-08%20Sprint%20review.md)
**Kategoria:** #Funkcjonalność #Architektura

**Logowanie wysyłanych maili ze sprawy** ✅
- **Zaimplementowano:**
  - Rozszerzony mechanizm logowania aktywności z 3 opcjami (Logowanie maili, Treść maili, Załączniki)
  - Logowanie maili wysłanych przez SendMessage (regex)
  - Informacja o uprawnieniach użytkownika przy każdym zdarzeniu
- **Uwagi:** Treść maili i załączniki opcjonalne ze względów pojemnościowych

---

## 2025-08-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-21 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-21%20Rada%20architektów.md)
**Kategoria:** #Architektura

**Szczegóły implementacji logowania powiadomień** ✅
- **Pytanie techniczne:** Jak rejestrować maile do grup - jeden wpis z listą czy osobne wpisy per osoba?
- ❌ Odrzucone: Jeden wpis z listą odbiorców - trudniejsze filtrowanie i raportowanie
- ⏸️ Odroczone: Jeden wpis z kolumną składu grupy - bardziej skomplikowane
- ✅ **Zatwierdzone: Osobne wpisy per osoba**
  1. **Rejestrowanie:** Każdy mail do grupy = osobne wpisy dla każdego członka
  2. **Mechanizm:** Rozszerzenie istniejącego mechanizmu logowania o kategorię "powiadomienia"
  3. **Włączanie:** Nie domyślnie włączone, wymaga ustawienia w procesie
  4. **Poziom:** `SendMessage` - rejestracja każdego wysłanego maila osobno
  5. **Powiadomienia zbiorcze:** Każde powiadomienie w zbiorczym mailu rejestrowane osobno
- **Punkty otwarte:** Jak mechanizm dla powiadomień zbiorczych (raz dziennie)? Dodatkowe kolumny (typ, case ID)?
- **Zadania:** Piotr Buczkowski - implementacja per osoba, rozszerzenie mechanizmu

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

**Logowanie powiadomień systemowych – ślad audytowy** ✅
- **WIM wymaga** aby treść, odbiorcy i czas wysłania każdego powiadomienia z Workflow były zapisywane w AMODIT jako ślad audytowy
- ❌ Odrzucone: Logowanie w tabeli Notification - czyszczona kolejka techniczna (nie audytowa)
- ⏸️ Odroczone: Czyszczenie starych logów - na razie logi pozostają na wieczność (jak historia)
- ✅ **Zatwierdzone:**
  1. **Włączanie na poziomie procesu:** Ustawienie "Loguj mailingi systemowe" + opcja "loguj z treścią maila" (checkbox)
  2. **Co logujemy:** Data, odbiorca (do kogo), tytuł, treść (jeśli włączone), typ (z czego wynika), rodzaj (indywidualny/zbiorczy/z ustawień konta), case ID
  3. **Mechanizm:** Rozszerzenie istniejącego mechanizmu logowania wejść i pobrania dokumentów o kategorię "powiadomienia"
  4. **Przechowywanie:** Osobna tabela lub rozszerzenie istniejącej (nie Notification)
- **Typy powiadomień:** forward, dodanie CC, SendMessage, przypomnienia
- **Punkty otwarte:**
  - Która dokładnie tabela będzie używana?
  - Czy w przyszłości parametr czasu przechowywania logów?
  - Jakie dokładnie typy powiadomień logować (wszystkie czy wybrane)?
- **Zadania:** 
  - Piotr Buczkowski - weryfikacja mechanizmu, określenie co logować, przygotowanie zadania (Ready to do, Damian)
  - Damian Kamiński - przekazanie zadania na Daily (jutro)

---


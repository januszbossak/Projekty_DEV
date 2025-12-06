# CHANGELOG - Logowanie do AMODIT

## 2025-10-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-30 Rada architektów.md]
**Kategoria:** #Funkcjonalność #Bezpieczenstwo #Odroczone

- Polpharma – równoległe sesje po zalogowaniu. Projekt rozpisany, ale odroczony z powodu braku zasobów.

---

## 2025-09-22 | Sprint Review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-22 Sprint review.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-22%20Sprint%20review.md)
**Kategoria:** 🎨 Design

- **Strona wylogowania:** dodano wyraźny przycisk/napis "Logowanie" (zastąpienie nieintuicyjnego/niewidocznego logo) umożliwiający powrót do ekranu logowania.
- **Globalne wylogowanie:** wylogowanie w jednej zakładce skutkuje wylogowaniem we wszystkich otwartych zakładkach (synchronizacja React <-> stara technologia).
- **Przekierowania:** zachowanie logiki przekierowań (np. przy autologowaniu providerem nie kieruje na stronę logowania, by uniknąć pętli).

---

## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność

- **Wsparcie dla Google (OAuth):** Zatwierdzono wdrożenie interfejsu do zarządzania konfiguracją providerów OAuth (w tym Google), aby przygotować się na koniec wsparcia Azure AD (04.2026).

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Design #Funkcjonalność

**Cel:**
Odświeżenie okna logowania dla użytkowników niekorzystających z SSO (Active Directory) oraz usprawnienie dla użytkowników posiadających więcej niż jedno konto.

### Nowe okno logowania

- Odświeżone okno logowania dla użytkowników niekorzystających z SSO (Active Directory)
- Poprawiony design, ładniejszy wygląd

### Usprawnienie dla użytkowników z wieloma kontami

- Po uwierzytelnieniu użytkownicy z więcej niż jednym kontem przechodzą na nowy ekran w formie kafelkowej
- Zestawione w ładny sposób swoje konta powiązane np. z danym adresem mailowym
- Łatwo rozróżnić login, stanowisko, dział
- W górnym menu (tam gdzie imię i nazwisko) można w łatwy sposób przełączyć się na inne konto
- Nie trzeba się wylogowywać całkowicie – można przełączyć się w inny kontekst (np. na konto z innej spółki, innego oddziału czy na inną rolę – między administratorem a użytkownikiem)

### Przypadki użycia

- Firmy wielooddziałowe
- Grupy firm
- Osoby zatrudnione w odrębnych jednostkach
- Osoby, które są jednocześnie zaangażowane w procesy biznesowe i są administratorami (zalecane posiadanie dwóch odrębnych kont)

### Szczegóły techniczne

- Ekran kafelkowy z kontami powiązanymi z adresem mailowym


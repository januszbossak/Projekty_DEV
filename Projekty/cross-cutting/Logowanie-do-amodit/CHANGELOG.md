# CHANGELOG - Logowanie do AMODIT

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


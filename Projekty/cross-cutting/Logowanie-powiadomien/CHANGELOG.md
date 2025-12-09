# CHANGELOG – Logowanie-powiadomien

---

## 2025-11-03 | Sprint review
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-03 Sprint review-codex.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-03%20Sprint%20review-codex.md)
**Kategoria:** #Funkcjonalność #Diagnoza

- Historia maili wysłanych do sprawy: wpisy dodawane przy dodaniu do kolejki, plan oznaczania faktycznie wysłanych (zadanie na bieżący sprint).
- Zgłoszenie z WIM: kluczowa informacja o mailach, które nie wczytały się (np. faktury) – konieczne lepsze opisy ustawień systemowych i propagacja wiedzy.

## 2025-10-07 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-07 Rada architektów.md]
**Kategoria:** #Bug #Funkcjonalność #Decyzja

- Problem z logowaniem maili wychodzących: logowanie w momencie dodania do kolejki, a nie faktycznego wysłania
- Decyzja: Wprowadzenie dwóch statusów ("Zaplanowane do wysłania", "Wysłane") i kolumny z datą/czasem faktycznego wysłania

---

## 2025-09-30 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-30 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-30%20Rada%20architektów.md)
**Kategoria:** #Architektura #Funkcjonalność

- Rejestrowanie maili jako wysłanych dopiero w momencie faktycznego wysłania (zejścia z kolejki)
- Konieczność rejestrowania maili zbiorczych (Notification Job) per sprawa
- Decyzja o porzuceniu rejestrowania w momencie trafienia do kolejki (ryzyko błędnych danych)

---

## 2025-08-21 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-21 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-21%20Rada%20architektów.md)
**Kategoria:** #Architektura
**Projekt:** [Klienci/WIM/Logowanie-powiadomien](../../Klienci/WIM/Logowanie-powiadomien/)

**Szczegóły implementacji - rejestrowanie per osoba**
- Osobne wpisy dla każdego odbiorcy (łatwiejsze filtrowanie i raportowanie)
- Rejestrowanie na poziomie `SendMessage`
- **Szczegóły:** Zobacz [Klienci/WIM/Logowanie-powiadomien](../../Klienci/WIM/Logowanie-powiadomien/CHANGELOG.md)

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Funkcjonalność
**Projekt:** [Klienci/WIM/Logowanie-powiadomien](../../Klienci/WIM/Logowanie-powiadomien/)

**Logowanie powiadomień systemowych – rozszerzenie mechanizmu audytu**
- Rozszerzenie istniejącego mechanizmu logowania o kategorię "powiadomienia"
- Logowanie mailingów systemowych z Workflow (włączalne na poziomie procesu)
- Osobna tabela dla logów powiadomień (nie Notification - kolejka techniczna)
- **Szczegóły:** Zobacz [Klienci/WIM/Logowanie-powiadomien](../../Klienci/WIM/Logowanie-powiadomien/CHANGELOG.md)

---

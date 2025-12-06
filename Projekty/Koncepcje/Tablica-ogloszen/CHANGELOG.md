# CHANGELOG – Tablica-ogloszen

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Koncepcja #Funkcjonalność

**Komunikaty statyczne (info bar) – informowanie użytkowników** 🔍

Przywrócenie i rozbudowa mechanizmu info bar (pasek informacyjny) do informowania użytkowników o ważnych wydarzeniach. Mechanizm istnieje w starym widoku, wymaga przeniesienia do Reacta i rozbudowy o zarządzanie dla chmury.

**Szczegóły:**
- Wyświetlanie: pasek na górze ekranu głównego (jak Raporty Premium)
- Możliwość zamknięcia: użytkownik może zamknąć (wyświetla się raz)
- Zarządzanie On-Premise: interfejs w ustawieniach systemowych (per serwer)
- Zarządzanie chmura: narzędzie do zbiorczego zarządzania dla wszystkich klientów
- Format: tekst w języku polskim i angielskim, zakres dat (od-do)
- Obecny stan: mechanizm w starym widoku (strona logowania), wymaga przeniesienia do Reacta

**Kontekst:**
- Potrzeba informowania o przerwach w działaniu, aktualizacjach, ważnych komunikatach
- Zmniejszenie liczby maili, poprawa komunikacji
- Możliwość publikowania z wyprzedzeniem (np. "dzisiaj o 18:00 przerwa 15 minut")
- Strona logowania: tylko dla informacji o przerwach w działaniu bazy (gdy system nie działa)

**Zadania:**
- Anna Skupińska - research obecnego stanu mechanizmu info bar
- Anna Skupińska - przygotowanie opisu wymagań dla docelowego rozwiązania
- Product Owner - przypisanie zadania po zakończeniu researchu

**Punkty otwarte:**
- Czy komunikat na stronie logowania dla przerw w działaniu bazy?
- Jak obsłużyć bardzo długie komunikaty?
- Czy dla wszystkich użytkowników czy wybranych grup?
- Jak zapewnić, że nie będzie przeszkadzał (możliwość zamknięcia)?

---

## 2025-08-19 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-08-19 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-08-19%20Rada%20architektów.md)
**Kategoria:** #Koncepcja
**Projekt:** [Klienci/WIM/News-Feed-Anonse](../../Klienci/WIM/News-Feed-Anonse/)

**Koncepcja tablicy ogłoszeń – prototyp i rozważane alternatywy**
- Prototyp Damiana: zakładka "Ogłoszenia" w menu powiadomień
- Rozważane alternatywy: AMODIT Talk, dedykowany proces, RSS feed
- **Status:** 🔍 Do weryfikacji - wymagania od WIM/Piotra Murawskiego
- **Szczegóły:** Zobacz [Klienci/WIM/News-Feed-Anonse](../../Klienci/WIM/News-Feed-Anonse/CHANGELOG.md)

---


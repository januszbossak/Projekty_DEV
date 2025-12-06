# CHANGELOG - Gantt

## 2025-09-18 | Rada Architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-18 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-18%20Rada%20architektów.md)
**Kategoria:** #Decyzja

- **Grupowanie:** Temat grupowania w Gantcie został poruszony, ale odroczony (status ⏸️).

---

## 2025-09-09 - Rada architektów

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-09-09 Rada architektów|2025-09-09 Rada architektów]]

**Kategoria:** #Problem #Funkcjonalność

**Kontekst:**
W raportach typu Gantt występuje problem z wyświetlaniem etykiet na agregowanych kafelkach (zielonych). Etykieta jest kopiowana z pierwszego kafelka wewnętrznego, co może prowadzić do nieprawidłowego wyświetlania (np. liczba zamiast tekstu). Dodatkowo ilość dni na agregowanym kafelku jest błędna – pokazuje wartość z pierwszego kafelka zamiast sumy wszystkich dni z podległych elementów.

### Problem

- Etykiety na agregowanych kafelkach są kopiowane z pierwszego elementu (nieprawidłowe dane)
- Ilość dni na agregowanym kafelku jest błędna (wartość z pierwszego kafelka zamiast sumy)
- Zakres dat (od-do) jest kopiowany z pierwszego elementu zamiast być wyliczany z wszystkich podległych

### Zidentyfikowane Ryzyka

- Wyświetlanie błędnych informacji na agregowanych kafelkach
- Nieczytelność raportów – etykiety mogą być nieprawidłowe lub mylące
- Brak możliwości sensownego agregowania etykiet tekstowych (nie da się ich zsumować)

### Decyzja

**Status:** ✅ Zatwierdzone

**Etykiety na agregowanych kafelkach:**
- **Usunięcie etykiet** z agregowanych kafelków (zielonych) – etykiety tekstowe nie da się sensownie agregować
- Informacje będą dostępne tylko w tooltipie po najechaniu myszką

**Poprawa tooltipu:**
- Tooltip na agregowanym kafelku musi wyświetlać prawidłowe dane:
  - **Zakres dat (od-do)** wyliczony z najwcześniejszej i najpóźniejszej daty z wszystkich podległych elementów
  - **Ilość dni** wyliczona jako suma dni z wszystkich podległych elementów (lub zakres dat, jeśli to bardziej odpowiednie)
- Tooltip nie może być kopiowany z pierwszego kafelka, tylko musi być wyliczany z wszystkich podległych elementów

### Szczegóły techniczne

- Agregowane kafelki (zielone) są generowane automatycznie przez DevExpress Gantt i nie są bytami w bazie danych
- Dane pochodzą z tej samej sprawy (projekt i zadanie są polami na sprawie)
- Agregacja jest faktycznie grupowaniem po polu (np. projekt, zadanie), a nie prawdziwą agregacją w bazie danych
- Gantt ma 2 tryby budowania hierarchii – trzeba mieć świadomość obu trybów przy poprawkach
- W drugim trybie istnieje możliwość przeliczania zakresu dat (prawy klawisz myszy)

**Uwaga:** Problem może być częściowo związany z nieprawidłową konfiguracją raportu (2 wiersze zagnieżdżenia zamiast rekurencyjnego budowania hierarchii zadań).

### Zadania

- **Marek Dziakowski:** Usunięcie etykiet z agregowanych kafelków w raporcie Gantt
- **Marek Dziakowski:** Poprawa tooltipu na agregowanych kafelkach – wyliczanie zakresu dat (od-do) z wszystkich podległych elementów
- **Marek Dziakowski:** Poprawa tooltipu – wyliczanie prawidłowej ilości dni z podległych elementów

### Punkty otwarte

- Czy w przyszłości rozważyć wyświetlanie zakresu dat (od-do) jako etykiety na agregowanych kafelkach?
- Czy problem z etykietami jest związany z konfiguracją raportu (2 wiersze zagnieżdżenia vs rekurencyjne budowanie hierarchii)?
- Jak obsłużyć przypadek, gdy agregowany kafelek jest bardzo mały i nie ma miejsca na jakiekolwiek informacje?


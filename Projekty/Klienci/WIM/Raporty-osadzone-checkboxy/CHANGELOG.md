# CHANGELOG – Raporty-osadzone-checkboxy (WIM)

---

## 2025-09-11 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-11 Rada architektów - Multipart REST checkboxy edytor.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-11%20Rada%20architektów%20-%20Multipart%20REST%20checkboxy%20edytor.md)
**Kategoria:** #Architektura #Funkcjonalność

**WIM – raport osadzony z checkboxami do zapisania stanu** 🔍

Rozbudowa mechanizmu raportów osadzonych o możliwość edycji checkboxów w źródłach zewnętrznych i zapisania stanu jako części sprawy.

**Kontekst biznesowy:**
- WIM potrzebuje raportu osadzonego na sprawie wyświetlającego pozycje zamówienia z zewnętrznego źródła danych (na podstawie numeru zamówienia)
- Użytkownicy mają zaznaczać checkboxami, które pozycje są zgodne z fakturą
- Następnie zapisać ten stan jako część sprawy
- Obecnie raporty osadzone ze źródeł zewnętrznych nie obsługują edycji checkboxów ani zapisywania stanu

**Zidentyfikowane ryzyka:**
- Brak możliwości zapisania stanu checkboxów jako części sprawy
- Potrzeba rozbudowy mechanizmu raportów osadzonych o edycję checkboxów
- Ryzyko pojawienia się podobnych potrzeb u innych klientów (źródła statyczne/dynamiczne)
- Potencjalne problemy wydajnościowe przy dużych tabelkach (300+ pozycji)

**Rozwiązanie:**
- Raport osadzony ze źródła zewnętrznego (na podstawie numeru zamówienia)
- Możliwość zaznaczania checkboxów przez użytkowników
- Zapisanie stanu checkboxów jako część sprawy (NIE w CaseDefinition, w źródle dynamicznym)
- Mechanizm podobny do istniejącego dla źródeł statycznych/dynamicznych
- Wymaga Proof of Concept przed pełną implementacją

**Rozważane alternatywy:**
- ✅ Raport osadzony z edytowalnymi checkboxami - wybrana, rozwiązanie systemowe, spójne z raportami
- ⏸️ Edycja danych w źródle dynamicznym z formularza (bez raportu) - odroczona, może być kolejny MVP
- ❌ Tabelka AMODITowa na sprawie - odrzucona, dane z zewnętrznego źródła, nie z CaseDefinition

**Status:** 🔍 Do weryfikacji / ⏸️ Częściowo odroczone

**Technologia:**
- Rozwiązanie ogólnosystemowe - zobacz [Moduly/Modul-raportowy](../../../Moduly/Modul-raportowy/)

**Zadania:**
- Damian Kamiński - Proof of Concept dla raportu osadzonego z edytowalnymi checkboxami
- Damian Kamiński - rozpisanie wymagań i zaakceptowanie rozwiązania

**Punkty otwarte:**
- Jak zapisać stan checkboxów jako część sprawy (w źródle dynamicznym, nie CaseDefinition)?
- Czy rozwiązanie tylko dla raportów osadzonych, czy też dla innych typów raportów?
- Czy w przyszłości bezpośrednia edycja danych w źródłach dynamicznych z formularza (bez raportu)?
- Jak obsłużyć przypadek, gdy dane w źródle zewnętrznym się zmienią (np. dodanie nowych pozycji zamówienia)?

---

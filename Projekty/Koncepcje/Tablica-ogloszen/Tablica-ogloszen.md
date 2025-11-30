# Tablica ogłoszeń

## Status koncepcji

**Typ:** Koncepcja
**Status:** Wstrzymana (do doprecyzowania wymagań)
**Data dodania:** 2025-08-19
**Ostatnia aktualizacja:** 2025-08-19

---

## 1. Opis koncepcji

### Problem

- Brak dedykowanego narzędzia do publikacji ogłoszeń wewnętrznych dla użytkowników systemu
- Istniejący stary mechanizm newsów jest przestarzały technologicznie i nie jest używany przez kluczowych klientów
- Niejasność co do rzeczywistych wymagań biznesowych i różnic między "news feedem", "tablicą ogłoszeń" a systemem anonsów

### Proponowane rozwiązanie

Nowy moduł "Ogłoszenia" umieszczony jako zakładka w menu powiadomień, z możliwością publikacji komunikatów do wybranych grup użytkowników.

### Potencjalna wartość

- Centralne miejsce do komunikacji wewnętrznej
- Kontrola nad odbiorcami i czasem publikacji
- Możliwość archiwizacji po wygaśnięciu

### Ryzyko

- Powielanie możliwości istniejących narzędzi (AMODIT Talk, dedykowane procesy)
- Prototyp nie uwzględnia kluczowych wymagań biznesowych

---

## 2. Warianty rozwiązania

### Wariant 1: Dedykowany moduł "Ogłoszenia"

Prototyp Damiana - nowa zakładka w menu powiadomień.

**Wymagane funkcjonalności:**
- Mechanizm wyboru odbiorców rozszerzony o:
  - Grupy użytkowników
  - Konkretne osoby
  - (na wzór selektorów z modułu raportów)
- Opcja planowania publikacji (data i godzina startu)
- Termin ważności ogłoszenia (automatyczna archiwizacja/ukrycie)

### Wariant 2: AMODIT Talk

Wykorzystanie istniejącego modułu jako alternatywy.

**Zalety:**
- Gotowe mechanizmy: załączniki, komentarze, historia zmian
- Brak konieczności tworzenia nowej funkcjonalności

### Wariant 3: Dedykowany proces AMODIT

Wykorzystanie standardowego procesu workflow do obiegu ogłoszeń.

---

## 3. Otwarte pytania

- [ ] Jaka jest różnica między "news feedem" a "tablicą ogłoszeń" w wizji Piotra Murawskiego?
- [ ] Czy potrzebny jest system anonsów (typu "sprzedam/oddam")?
- [ ] Czy AMODIT Talk może spełnić te wymagania?
- [ ] Jakie są rzeczywiste przypadki użycia u klientów?

---

## 4. Powiązane dyskusje

| Data | Źródło | Kluczowe ustalenia |
|------|--------|-------------------|
| 2025-08-19 | Rada Architektów | Wstrzymano prace do doprecyzowania wymagań. Damian prezentował prototyp. |

---

## 5. Następne kroki

1. **Damian:** Kontakt z Piotrem Murawskim w celu doprecyzowania wymagań biznesowych
2. **Mateusz:** Przygotowanie prezentacji możliwości AMODIT Talk jako alternatywy
3. Podjęcie decyzji o wyborze wariantu po zebraniu wymagań

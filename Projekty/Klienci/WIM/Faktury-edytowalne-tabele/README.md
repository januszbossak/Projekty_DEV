# Faktury - edytowalne tabele

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |
| **Opiekun handlowy** | | |
| **Kontakt u klienta** | | |

**Klient:** WIM
**Status:** W analizie
**Data rozpoczęcia:** 2025-08-28
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Klient potrzebuje efektywnie przetwarzać i weryfikować faktury zawierające setki pozycji. Standardowe tabele w systemie mogą powodować problemy z wydajnością i nie oferują funkcji masowego zaznaczania.

### Cel projektu

Umożliwienie masowego zaznaczania pozycji na fakturach z dużą liczbą wierszy poprzez raport osadzony na formularzu.

### Powiązane dokumenty
- Umowa: [link/numer]
- Inicjatywa w backlogu: [link]

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne
[Część AMODIT / Osobny moduł / Microserwis / Integracja zewnętrzna]

### Technologie
- Frontend:
- Backend:
- Baza danych:

### Wykorzystanie funkcjonalności AMODIT
[Co możemy wykorzystać z istniejącego systemu?]

### Założenia UI/UX
[Główne założenia dotyczące interfejsu użytkownika]

### Kluczowe decyzje architektoniczne
| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| | | |

---

## 3. Plan wydań MVP

### MVP1: [Nazwa/Cel]
**Cel:** [Dlaczego akurat taki zakres? Co chcemy zweryfikować?]

**Funkcjonalności:**
- [ ] Funkcjonalność A
- [ ] Funkcjonalność B
- [ ] Funkcjonalność C

**Planowana data:**

---

### MVP2: [Nazwa/Cel]
**Cel:** [Co rozszerzamy? Dlaczego?]

**Funkcjonalności:**
- [ ] Funkcjonalność D
- [ ] Funkcjonalność E

**Planowana data:**

---

### Backlog (przyszłe MVP)
- Funkcjonalność F
- Funkcjonalność G

---

## 4. Proponowane rozwiązanie

### Raport ze źródła zewnętrznego z edytowalnymi checkboxami

**Status:** W analizie technicznej
**Data zgłoszenia:** 2025-08-28

**Rozwiązanie:**
- Raport osadzony na formularzu
- Dane zasilane ze źródła zewnętrznego (np. pozycje zamówienia z innego systemu)
- Edytowalna kolumna z checkboxami do zaznaczania zgodności wierszy
- Zwiększony domyślny limit wierszy na stronie (unikanie problematycznego stronicowania)

**Decyzja (2025-08-28):**
Kierunek rozwoju oparty na rozbudowie raportu ze źródła zewnętrznego został zaakceptowany. Należy przeanalizować techniczne możliwości implementacji.

**Zadania:**
- [ ] **Piotr:** Przeanalizować możliwość dodania edytowalnej kolumny (checkbox) w raporcie bazującym na źródle zewnętrznym
- [ ] **Piotr:** Zbadać opcję zwiększenia limitu wierszy
- [ ] **Damian:** Skonsultować z klientem - zaznaczanie pozycji zgodnych czy niezgodnych?

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-28 | Utworzenie projektu, zaakceptowano kierunek rozwoju | Rada Architektów 2025-08-28 |

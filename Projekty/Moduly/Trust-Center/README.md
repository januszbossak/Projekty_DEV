# Trust Center

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | | |
| **Tester** | | |

**Typ:** Moduł systemu (roadmapa)
**Status:** [W analizie / W realizacji / Wdrożony / Wstrzymany]
**Data rozpoczęcia:**
**Planowane zakończenie:**

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?
[Roadmapa / Inicjatywa strategiczna / Potrzeba rynkowa]

### Cel projektu
[Jaki problem rozwiązujemy? Jaką wartość dostarczamy użytkownikom?]

### Powiązane dokumenty
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

## 4. Funkcjonalności w realizacji

### Weryfikacja dostępu i przejście serwisowe do Trust Center

**Status:** Do realizacji
**Data zgłoszenia:** 2025-08-19

**Problem:**
- Brak jednoznacznego i bezpiecznego mechanizmu weryfikacji uprawnień użytkownika przy przejściu do Trust Center
- Automatyzacja procesu logowania może zablokować dostęp klientom ze starszymi wersjami oprogramowania (nie przekazują e-mail w parametrze)

**Rozwiązanie:**

1. **Zmiana nazwy przycisku:** "Zarządzaj dokumentem w Trust Center" (bardziej intuicyjne)

2. **Automatyczna weryfikacja i logowanie:**
   - Po kliknięciu przycisku system weryfikuje, czy użytkownik jest wysyłającym dokument lub administratorem organizacji
   - Jeśli walidacja pozytywna - automatyczne wysłanie e-mail z kodem dostępowym

3. **Kompatybilność wsteczna:**
   - System sprawdza, czy e-mail jest przekazywany w parametrze (nowsze wersje)
   - Jeśli tak → kod wysyłany automatycznie
   - Jeśli parametr pusty (starsze wersje) → wyświetlenie pola do ręcznego wprowadzenia e-mail

**Decyzja (2025-08-19):**
Wdrożenie z pełną kompatybilnością wsteczną - obsługa zarówno nowych jak i starszych klientów.

### Bezpieczeństwo - Dane poufne w nazwach plików SMS

**Status:** W analizie
**Data zgłoszenia:** 2025-09-16

**Problem:**
Nazwy plików wysyłane w treści wiadomości SMS przez Trust Center mogą zawierać dane poufne (np. imię i nazwisko), co stwarza ryzyko wycieku danych.

**Rozwiązanie:**
- Ujednolicić działanie wysyłki SMS i e-mail
- W obu kanałach wykorzystywać "przyjazną nazwę pliku" jeśli została zdefiniowana w procesie
- Odpowiedzialność za bezpieczeństwo "przyjaznej nazwy" spoczywa na konfigurującym proces

**Decyzja (2025-09-16):**
- Zweryfikować, czy mechanizm SMS już wykorzystuje "przyjazną nazwę pliku"
- Opracować i zakomunikować konsultantom dobre praktyki

**Zadania:**
- [ ] **Łukasz:** Sprawdzić u Marka, czy "przyjazna nazwa pliku" jest już używana w SMS-ach
- [ ] **Łukasz:** Przygotować wytyczne dla konsultantów o bezpiecznym stosowaniu "przyjaznych nazw"

### Logowanie OAuth Microsoft dla dostępu serwisowego

**Status:** Zaimplementowane
**Data:** 2025-09-22

**Dlaczego to robimy:**
Usprawnienie i uproszczenie dostępu serwisowego do dokumentów w Trust Center, tak aby pracownicy wsparcia technicznego nie musieli być dodawani jako administratorzy w każdej organizacji klienta z osobna.

**Rozwiązanie:**
- Logowanie do panelu administracyjnego Trust Center za pomocą **konta Microsoft (OAuth)**
- System weryfikuje, czy adres e-mail logującego się użytkownika znajduje się na **centralnej, wewnętrznej liście kont serwisowych**
- Jeśli tak - użytkownik uzyskuje dostęp administracyjny do dokumentu bez potrzeby bycia przypisanym do organizacji klienta

**Dalsze kroki:**
- [ ] Utrzymywać i kontrolować listę osób uprawnionych do dostępu serwisowego

### Logowanie Azure AD do Trust Center

**Status:** Wdrożone
**Data:** 2025-10-06

**Dlaczego to robimy:**
Usprawnienie procesu logowania do Trust Center dla pracowników z uprawnieniami serwisowymi.

**Rozwiązanie:**
- Możliwość logowania do Trust Center za pomocą konta Microsoft (Azure AD)
- Eliminacja potrzeby ręcznego wpisywania loginu i hasła

**Dalsze kroki:**
- [ ] Zmienić wygląd przycisku logowania - pełna spójność z ekranem logowania głównej aplikacji

### Blockchain - wydzielenie do oddzielnego serwisu

**Status:** Do realizacji (następny sprint)
**Data zgłoszenia:** 2025-10-14
**Priorytet:** Wysoki

**Problem:**
- Dwa serwery webowe wykonują zadanie dodawania do blockchaina jednocześnie
- Dokumenty dodawane do tego samego ostatniego bloku → zawieszanie operacji
- Skala problemu: z kilku wiszących dokumentów do **ponad 50**
- Brak obsługi scenariusza równoczesnego podpisywania tego samego dokumentu

**Rozwiązanie:**
- Wydzielenie funkcji dodawania do blockchaina do **oddzielnego serwisu/procesu**
- Kolejka z jednym workerem (zachowanie kolejności operacji w blockchainie)
- Konteneryzacja (Docker) - łatwe wdrożenie do chmury i on-premises
- Początkowa faza: informacja o oczekiwaniu na mail / ręczne odświeżenie statusu
- Docelowo: powiadomienia dynamiczne (SignalR lub druga kolejka)

**Decyzja (2025-10-16):**
- Wydzielenie w **następnym sprincie** - priorytet
- Najpierw poprawne kolejkowanie, potem powiadomienia dynamiczne
- Marek uzyska akceptację kosztów (początkowo bliskie zeru)

**Zadania:**
- [ ] **Marek:** Zaimplementować wydzielenie blockchain do oddzielnego serwisu Docker
- [ ] **Marek:** Uzyskać akceptację kosztów wdrożenia i utrzymania

---

## Rozważane koncepcje realizacyjne

### Metodyka Docker/Azure dla mikroserwisów (2025-10-16)

Demonstracja podejścia Mateusza do budowania usług AI jako wzorzec dla wydzielenia blockchain:

**Wdrożenie lokalne (on-premises):**
- Skopiowanie pliku `docker-compose` i uruchomienie jednym poleceniem
- Aktualizacja: zaktualizowanie obrazu, Docker automatycznie pobiera

**Wdrożenie chmurowe (Azure):**
- Container Instance/Register do zarządzania obrazami
- **Automatyczne aktualizacje bez przestojów** - stara instancja obsługuje requesty, dopóki nowa się uruchamia
- Auto-scaling na podstawie obciążenia (min/max replik)
- Prosta konfiguracja HTTPS przez Ingress
- Zmienne środowiskowe + referencje do Secrets dla poufnych danych
- Wersjonowanie przez tagi obrazów

**Rozważane alternatywy:**
- Adrian zasugerował Kubernetes dla bardziej dojrzałego rozwiązania produkcyjnego
- Na razie Docker uznany za wystarczający

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-19 | Dodano funkcjonalność weryfikacji dostępu i przejścia serwisowego | Rada Architektów 2025-08-19 |
| 2025-09-16 | Dodano problem bezpieczeństwa - dane poufne w nazwach plików SMS | Rada Architektów 2025-09-16 |
| 2025-09-22 | Logowanie OAuth Microsoft dla dostępu serwisowego - zaimplementowane | Sprint review 2025-09-22 |
| 2025-10-06 | Logowanie Azure AD do Trust Center | Sprint review 2025-10-06 |
| 2025-10-14 | Blockchain - temat do analizy: sposób realizacji i koszty. Marek przygotuje dokumentację | Rada Architektów 2025-10-14 |
| 2025-10-16 | Blockchain - decyzja: wydzielenie do oddzielnego serwisu Docker w następnym sprincie. Problem: >50 wiszących dokumentów | Rada Architektów 2025-10-16 |
| 2025-10-16 | Dodano sekcję "Rozważane koncepcje realizacyjne" - metodyka Docker/Azure jako wzorzec | Rada Architektów 2025-10-16 |

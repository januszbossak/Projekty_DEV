# Logowanie powiadomień e-mail

## Metryki projektu

| Rola | Osoba | Kontakt |
|------|-------|---------|
| **PDM** | | |
| **Deweloper** | Piotr (przygotowanie zadania) | |
| **Tester** | | |

**Typ:** Funkcjonalność cross-cutting
**Status:** W analizie
**Data rozpoczęcia:** 2025-08-19
**Planowane zakończenie:** -

---

## 1. Kontekst biznesowy

### Dlaczego to robimy?

Brak centralnego rejestru (śladu audytowego) dla wysyłanych z systemu wiadomości e-mail uniemożliwia weryfikację, czy, kiedy i o jakiej treści powiadomienie zostało wysłane do odbiorcy.

### Cel projektu

Zapewnienie śladu audytowego dla powiadomień e-mail wysyłanych z procesów workflow poprzez rozszerzenie istniejącego mechanizmu logowania zdarzeń.

### Problem

- Brak możliwości weryfikacji wysłanych powiadomień
- Nie wiadomo czy, kiedy i o jakiej treści powiadomienie zostało wysłane
- Utrudniony audyt i rozwiązywanie problemów

---

## 2. Kontekst techniczno-architektoniczny

### Podejście architektoniczne

Rozszerzenie istniejącego mechanizmu logowania zdarzeń (używanego m.in. do rejestrowania pobrań dokumentów) o nową kategorię zdarzeń dla powiadomień e-mail.

### Rozwiązanie techniczne

**Konfiguracja:**
- Checkbox "Loguj z treścią maila" w ustawieniach definicji procesu
- Logowanie opcjonalne - włączane per proces

**Zawartość logu:**
- Data wysłania
- Odbiorca
- Tytuł wiadomości
- Treść wiadomości
- Typ zdarzenia
- ID sprawy (caseID)

**Charakterystyka:**
- Zapisy permanentne (trwałe)
- Integracja z istniejącym mechanizmem zdarzeń
- **Mechanizm domyślnie wyłączony** - klient musi świadomie aktywować

**Obsługa wysyłek do grup:**
- Każdy e-mail logowany jako **oddzielny rekord per odbiorca**
- Nawet przy wysyłce do grupy - osobny wpis dla każdego adresata
- Uzasadnienie: skład grup zmienia się w czasie, pojedynczy wpis dla grupy byłby nieprecyzyjny

### Kluczowe decyzje architektoniczne

| Data | Decyzja | Uzasadnienie |
|------|---------|--------------|
| 2025-08-19 | Logowanie opcjonalne per proces | Kontrola administratora nad zakresem logowania |
| 2025-08-19 | Rozszerzenie istniejącego mechanizmu | Reużycie sprawdzonej infrastruktury |
| 2025-08-21 | Jeden wpis per odbiorca | Precyzja - skład grup zmienia się w czasie |
| 2025-08-21 | Mechanizm domyślnie wyłączony | Świadoma aktywacja przez klienta |

---

## 3. Funkcjonalność wdrożona (Sprint review 2025-09-08)

### Logowanie wysyłanych maili w historii sprawy

**Status:** Wdrożone

**Dlaczego to robimy:**
Zapewnienie możliwości śledzenia w historii sprawy informacji o mailach, które zostały z niej wysłane.

**Rozwiązanie:**
- W ustawieniach systemowych dodano nowe opcje pozwalające włączyć logowanie wysyłanych maili
- Można osobno kontrolować:
  - Logowanie samej treści maila
  - Logowanie załączników (uwaga na duży rozmiar danych w bazie)
- W historii sprawy pojawia się nowy typ zdarzenia "email":
  - Szczegóły wysłanej wiadomości
  - Treść maila
  - Lista załączników z linkami do pobrania
- Mechanizm loguje zarówno:
  - Maile wysyłane standardowo
  - Maile wysyłane przez funkcje w regułach (`SendMessageEx`)

**Dalsze kroki:**
- [ ] Doprecyzować sposób prezentacji informacji o uprawnieniach w logu

---

## 4. Plan wydań MVP (wcześniejsza analiza)

### MVP1: Logowanie powiadomień e-mail

**Cel:** Zapewnić ślad audytowy dla powiadomień wysyłanych z procesów

**Funkcjonalności:**
- [x] Checkbox "Loguj z treścią maila" w definicji procesu
- [x] Logowanie wszystkich powiadomień e-mail z workflow
- [x] Zapis: data, odbiorca, tytuł, treść, typ zdarzenia, caseID
- [x] Permanentne przechowywanie logów
- [x] Jeden wpis per odbiorca (obsługa grup)
- [x] Mechanizm domyślnie wyłączony

**Zespół:** Piotr (implementacja)

**Planowana data:** Wdrożone 2025-09-08

---

## 5. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-19 | Utworzenie projektu, definicja wymagań | Rada Architektów 2025-08-19 |
| 2025-08-21 | Doprecyzowanie: jeden wpis per odbiorca, domyślnie wyłączony | Rada Architektów 2025-08-21 |
| 2025-09-08 | Funkcjonalność wdrożona - logowanie treści i załączników | Sprint review 2025-09-08 |

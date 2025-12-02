# Notatka projektowa – 2025-11-20 – Edytor procesów

**Data:** 2025-11-20
**Temat główny:** Design i UI Edytora procesów – kosmetyka, spójność wizualna, zamknięcie MVP

**Powiązane projekty:**
- `moduly/Edytor-procesow`
- `cross-cutting/Design-System`
- `moduly/Ustawienia-systemowe`
- `moduly/Modul-raportowy`

---

## 1. Priorytety rozwoju: Edytor procesów vs Moduł raportowy

**Komponent:** Strategia rozwoju

### Cel i problem

Konieczność uzgodnienia priorytetów rozwojowych między dokończeniem Edytora procesów (diagramy) a naprawą Modułu raportowego. Obecnie zespół pracuje nad JRWA i repozytorium, a pozostałe tematy wymagają ustalenia kolejności.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dokończenie diagramów | Skupienie się na zamknięciu Edytora diagramów, aby konsultanci mogli efektywnie pracować | 💡 Propozycja Przemka |
| Naprawa modułu raportowego | Naprawienie błędów w module raportowym, który nie działa poprawnie od powstania | 💡 Propozycja Janusza |
| Kontynuacja JRWA i repozytorium | Dokończenie bieżących prac klienckich | ✅ Zatwierdzone jako priorytet |

### Decyzja / Sposób realizacji

**Status:** 🔍 Do weryfikacji

💭 Propozycja Przemka: Dokończenie edytora diagramów powinno być priorytetem po zakończeniu JRWA i repozytorium, ponieważ:
- Zakres jest dobrze zdefiniowany (w przeciwieństwie do raportów)
- Wymaga mniej dyskusji architektonicznych i sprecyzowania wymagań
- Umożliwi zmianę trybu pracy konsultantów
- Prace są już rozpoczęte

Janusz preferuje naprawę modułu raportowego, ponieważ z raportów korzystają użytkownicy końcowi.

Przemek argumentuje, że moduł raportowy nie działa od powstania i można poczekać kolejny kwartał po dokończeniu priorytetowych prac.

### Punkty otwarte

- Spotkanie jutro między Przemkiem a Januszem w celu uzgodnienia mapy priorytetów
- Ostateczna decyzja dotycząca kolejności prac po JRWA i repozytorium

---

## 2. Border radius – ujednolicenie zaokrągleń w systemie

**Komponent:** Design System (cross-cutting)

### Cel i problem

Brak spójności w zaokrągleniach elementów UI w różnych częściach systemu AMODIT. Różni deweloperzy stosują różne wartości border-radius (3px, 5px, 8px), co powoduje niespójny wygląd aplikacji.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| 3 piksele | Standard stosowany na sprawie (przyciski) | ❌ Odrzucona – za mało |
| 5 pikseli | Standard stosowany w większości nowych komponentów (moduł raportowy, formularze, inne) | ✅ Wybrana – spójność z większością aplikacji |
| 8 pikseli | Przypadkowo zastosowane przez Filipa w licencjach i ustawieniach | ❌ Odrzucona – błąd, za dużo |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Ujednolicenie wszystkich zaokrągleń w systemie AMODIT na wartość **5 pikseli**.

**Szczegóły techniczne:**
- Format: `border-radius: 5px`
- Dotyczy: wszystkie elementy UI (przyciski, sekcje, toolboxy, boksy, karty, foldery)
- Poprawki: zmiana z 8px na 5px w licencjach i ustawieniach (błąd Filipa)

**Usprawnienia systemowe:**
- Konieczność spisania Design System – dokumentacja standardów UI
- Automatyczna weryfikacja przez AI, aby wykrywać odstępstwa od standardu
- Centralizacja wartości w CSS, aby zmiana w jednym miejscu aktualizowała cały system

### Ograniczenia / Poza zakresem

Brak automatycznej centralizacji wartości border-radius w CSS (na razie manualne poprawki).

### Punkty otwarte

- Konieczność spisania pełnego Design System dla AMODIT
- Rozważenie automatycznej weryfikacji przez AI podczas code review

---

## 3. Prawy panel ustawień – zmiana pozycji i zachowania

**Komponent:** Edytor Formularza

### Cel i problem

Prawy panel ustawień w edytorze formularza przesuwa górną belkę (nagłówek), która powinna być statyczna. To powoduje "skakanie" interfejsu i niespójność z innymi widokami (np. lista).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Przesuwa całą tabelkę | Obecne zachowanie – panel wypycha górną belkę | ❌ Odrzucona – "skakanie" UI |
| Ustawienia jako osobny boks poniżej | Przeniesienie ustawień niżej, belka pozostaje statyczna, panel otwiera się w środkowej części ekranu | ✅ Wybrana – spójność z listą |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Przeniesienie prawego panelu ustawień jako osobnego boksu poniżej belki. Belka z sercem pozostaje statyczna na górze.

**Szczegóły techniczne:**
- Ustawienia wyświetlane jako osobny boks wyskakujący w środkowej części ekranu
- Belka z sercem (ikona "ulubione") przesunięta do prawej strony (spójnie z innymi widokami)
- Tylko środkowa część ekranu przesuwa się po otwarciu panelu (nie cała belka)

**Usprawnienia UX:**
- Statyczna belka górna
- Spójność z widokiem listy
- Brak "skakania" interfejsu

### Punkty otwarte

- Decyzja dotycząca tła toolboxa (czy dodać odróżniające tło)

---

## 4. Toolbox po lewej – wydzielenie wizualne

**Komponent:** Edytor Formularza

### Cel i problem

Lewy toolbox (selektor pól) i prawy panel zlewają się wizualnie z białym formularzem. Użytkownicy mogą mieć problem z rozróżnieniem narzędzi od treści formularza.

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| Dodanie kolorów do ikon typów pól | Tekstowe, numeryczne, biletowe listy wyboru otrzymują dedykowane kolory (propozycja Christiny) | ✅ Zaimplementowane |
| Dodanie tła na toolbox | Narzucenie koloru tła na cały lewy toolbox i prawy panel, aby odróżnić je od białego formularza | 💡 Propozycja do rozważenia |
| Wydzielenie toolboxa do osobnego kontenera | Utworzenie osobnej ramki z zaokrągleniami (5px) dla toolboxa | ✅ Zaplanowane |

### Decyzja / Sposób realizacji

**Status:** 💡 Propozycja

Wydzielenie lewego toolboxa i prawego panelu jako osobne kontenery z ramką i zaokrągleniami (5px). Rozważane dodanie tła w innym kolorze niż biały, aby wyraźnie odróżnić narzędzia od treści formularza.

**Szczegóły techniczne:**
- Toolbox jako osobny kontener z `border-radius: 5px`
- Potencjalne tło (kolor do ustalenia)
- Formularz pozostaje biały (1:1 z widokiem na sprawie)

**Usprawnienia UX:**
- Wyraźne odróżnienie narzędzi od treści
- Formularz wygląda identycznie jak na sprawie (biały)
- Toolbox i panel wyraźnie wizualnie oddzielone

### Punkty otwarte

- Decyzja o kolorze tła dla toolboxa i prawego panelu
- Testowanie czytelności po wprowadzeniu zmian

---

## 5. Zamknięcie MVP – ustawienia systemowe, logi, edytor formularza

**Komponent:** Strategia rozwoju

### Cel i problem

Konieczność zamknięcia MVP dla kluczowych komponentów systemu, aby móc przejść do kolejnych priorytetów. Zasada "zacznij kończyć, przestań zaczynać" – dokończenie rozpoczętych prac przed otwieraniem nowych wątków.

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

Zamknięcie MVP dla następujących komponentów:

**Ustawienia systemowe:**
- Status: 100% przeniesione z starej technologii
- Wszystkie funkcjonalności zaimplementowane (Wiki, integracje, "four-eyes", REST API, autentykacja)
- Komunikat o przełączeniu do nowego widoku może zostać wyłączony (opcjonalnie zachowany dla kompatybilności)
- Komponenty takie jak REST API i autentykacja świadomie pozostawione do późniejszego rozwinięcia

**Logi systemowe:**
- Status: 100% przeniesione

**Edytor formularza:**
- Status: Blisko 100% – MVP zamknięte po implementacji bieżących poprawek (toolbox, prawy panel, border-radius, sekcje)
- Planowane ogłoszenie zamknięcia MVP za 1-2 sprinty

**Strategia:**
- Dokończenie MVP dla komponentów przed otwarciem nowych prac
- Świadome zamknięcie tematów z możliwością przyszłych ulepszeń (ale nie jako "otwarte" MVP)
- Edytor diagramów i edytor reguł – do dokończenia w pierwszym kwartale
- Ustawienia procesu – do dokończenia (wciąż w starej technologii)

### Ograniczenia / Poza zakresem

Edytor diagramów i edytor reguł wymagają dalszych prac, ale nie są częścią bieżącego MVP.

### Punkty otwarte

- Ustalenie zakresu "dokończenia" dla Edytora diagramów i Edytora reguł
- Planowanie pierwszego kwartału: priorytetyzacja prac po JRWA i repozytorium

---

## Propozycja podziału na pakiety prac (MVP)

### MVP 1: Zamknięcie kosmetyki Edytora formularza

**Cel:** Zamknięcie designu i UI Edytora formularza
**Zakres:** Funkcjonalności 2, 3, 4 (border-radius, prawy panel, toolbox)
**Planowany termin:** 1-2 sprinty

### MVP 2: Edytor diagramów (Q1)

**Cel:** Dokończenie Edytora diagramów do stanu "kompletny"
**Zakres:** Funkcjonalności wymagające uzgodnienia (do zdefiniowania)
**Planowany termin:** Pierwszy kwartał

### MVP 3: Edytor reguł (Q1)

**Cel:** Dokończenie Edytora reguł
**Zakres:** Znaczna ilość prac do zrobienia (szczegóły do uzgodnienia)
**Planowany termin:** Pierwszy kwartał

---

## Punkty do dalszej dyskusji (globalne)

- Spotkanie Przemek + Janusz (jutro): uzgodnienie mapy priorytetów rozwojowych
- Definicja "dokończenia" dla Edytora diagramów i Edytora reguł
- Spisanie Design System dla AMODIT
- Możliwość automatycznej weryfikacji standardów UI przez AI
- Przeniesienie Ustawień procesu z starej technologii

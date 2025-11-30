# Project Canvas: Formularz sprawy

**Projekt nadrzędny:** [[Interfejs-sprawy]]
**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-11-29
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Janusz Bossak | Wymagania, feedback |
| **Tech Lead** | Piotr Buczkowski | Analiza kodu, decyzje techniczne |
| **Deweloper** | Mariusz | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem

Formularz sprawy to serce systemu AMODIT i wymaga ciągłej uwagi w różnych obszarach:

1. **Wygląd i estetyka** - obecny interfejs jest funkcjonalny, ale przestarzały i nie w pełni wykorzystuje możliwości nowoczesnych technologii webowych do poprawy czytelności i estetyki
2. **Logika renderowania** - wyświetlanie formularza na sprawie (runtime) to osobny obszar od definiowania w edytorze. Obecna implementacja niektórych elementów (np. wyświetlanie tabeli jako formularza) jest obejściem problemu, a jakość kodu jest niezadowalająca
3. **Wydajność** - złożone formularze z tabelami zagnieżdżonymi wymagają optymalizacji ładowania
4. **Responsywność** - formularze muszą działać poprawnie na różnych urządzeniach

### Cel biznesowy

Zwiększenie satysfakcji użytkowników i poprawa ergonomii pracy poprzez:
- Unowocześnienie wyglądu formularza sprawy
- Zapewnienie spójnego, wydajnego i estetycznego wyświetlania formularzy niezależnie od złożoności (tabele zagnieżdżone, pola wielokolumnowe)
- Poprawę responsywności na urządzeniach mobilnych

### Cel techniczny

- Stopniowa przebudowa komponentów formularza sprawy
- Wprowadzanie nowych opcji stylizacji (np. kolory, gradienty)
- Oddzielenie logiki wyświetlania formularza na sprawie (runtime) od logiki edytora definicji (design-time)
- Przepisanie problematycznych komponentów z zachowaniem spójności UX/UI
- Zapewnienie spójności wizualnej z resztą modernizowanego interfejsu AMODIT

### Metryka sukcesu

- Tabele zagnieżdżone wyświetlają się **poprawnie** na sprawie (desktop i mobile)
- Czas ładowania formularza **nie przekracza 2 sekund** dla standardowych spraw
- Interfejs jest **spójny** z resztą systemu AMODIT
- Użytkownicy mogą personalizować wygląd formularzy (gradienty, kolory)

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: Oddzielenie od edytora

Logika wyświetlania formularza na sprawie (runtime) musi być **oddzielona** od logiki edytora definicji formularza. To dwa różne konteksty użycia.

**Uzasadnienie:** Edytor służy do projektowania struktury (administratorzy), a wyświetlanie na sprawie służy do pracy z danymi (użytkownicy końcowi). Różne wymagania, różne optymalizacje.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-09-08 | Wprowadzono podstawowe gradienty dla kolorów w celu rozszerzenia możliwości personalizacji wyglądu formularzy | Jest to prosty sposób na uatrakcyjnienie wyglądu formularzy bez dużych zmian architektonicznych | - |
| ADR-002 | ⏸️ Odroczone | 2025-09-08 | Dalsze prace nad zaawansowanymi gradientami i kolorami dla tablic są wstrzymane | Inne tematy, w szczególności klienckie, mają wyższy priorytet. Funkcjonalność w obecnej formie jest wystarczająca | - |
| ADR-003 | ⏸️ Wstrzymane | 2025-10-21 | Decyzja dotycząca wyświetlania tabeli jako formularza wstrzymana - Piotr analizuje kod | Konieczność weryfikacji jakości obecnej implementacji przed podjęciem decyzji o kierunku rozwoju (szybkie przywrócenie starego wyglądu vs przepisanie od nowa vs oparcie o tabelę) | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🟡 W analizie

**Ukończono:**
- ✅ Podstawowe gradienty dla kolorów (2025-09-08)

**Trwa praca nad:**
- **Piotr Buczkowski:** Weryfikacja sposobu implementacji wyświetlania tabeli jako formularza
- Zbieraniem wymagań dotyczących dalszej modernizacji UI formularza

**Zidentyfikowane opcje (wyświetlanie tabel):**
1. **Szybkie przywrócenie starego wyglądu** - niski koszt, ale potencjalnie tymczasowe
2. **Przepisanie modułu od nowa** - 10-15 dni roboczych, wysoka jakość docelowa
3. **Oparcie rozwiązania o tabelę** (sugestia Mariusza) - zgodność z UX/UI

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Średnie]** Obecna implementacja wyświetlania tabel to "obejście" - niska jakość kodu | Potwierdzony | Średni | Analiza Piotra przed decyzją. Docelowo przepisanie | Piotr |
| **[Średnie]** Przepisanie wymaga 10-15 dni roboczych | Potwierdzony | Średni | Rozważenie opcji tymczasowego przywrócenia starego wyglądu | PDM |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 Analiza i decyzja - wyświetlanie tabel (Status: W trakcie)

**Cel:** Podjęcie świadomej decyzji o kierunku rozwoju wyświetlania tabel jako formularzy.

**Zadania:**
- [ ] **Piotr Buczkowski:** Weryfikacja sposobu implementacji wyświetlania tabeli
- [ ] Decyzja: przywrócenie starego wyglądu vs przepisanie od nowa vs oparcie o tabelę

**Planowana data:** Q4 2025

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności do rozważenia:**
- Wyświetlanie tabeli jako formularza (poprawna implementacja)
- Zaawansowane gradienty i kolory dla tablic (odroczone z ADR-002)
- Optymalizacja ładowania złożonych formularzy
- Responsywność na urządzeniach mobilnych
- Dalsze usprawnienia wizualne i ergonomiczne

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-08-26 | Utworzenie podprojektu w ramach inicjatywy odświeżenia interfejsu sprawy | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| 2025-09-08 | Zaimplementowano podstawowe gradienty dla kolorów. Zdecydowano o wstrzymaniu dalszych prac nad zaawansowaną stylizacją ze względu na inne priorytety | [[2025-09-08 Sprint review]] |
| 2025-10-21 | Rozszerzenie zakresu projektu o logikę renderowania. Problem: wyświetlanie tabeli jako formularza - niska jakość kodu. Decyzja wstrzymana - Piotr analizuje kod | [[Rada architektów 2025-10-21]] |
| 2025-11-29 | Połączenie projektów "Formularz-sprawy" i "UI-formularza-sprawy" w jeden kompleksowy projekt śledzący wszystkie aspekty formularza sprawy | Reorganizacja dokumentacji |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Interfejs-sprawy]]
- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]
- **Środowisko TEST:** [do uzupełnienia]

---

## Powiązane projekty

- `moduly/Edytor-procesow/Edytor-formularzy` - definiowanie struktury formularza (design-time)
- `cross-cutting/Interfejs-sprawy` - ogólny interfejs sprawy

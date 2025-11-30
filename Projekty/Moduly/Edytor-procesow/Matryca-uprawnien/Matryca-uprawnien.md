# Project Canvas: Matryca uprawnień

**Projekt nadrzędny:** [[Edytor-procesow]]
**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-11-29
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-09-02

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Janusz Bossak, Damian Kamiński | Wymagania, feedback |
| **Tech Lead** | Piotr Buczkowski | Implementacja, feedback |
| **Deweloper** | Kamil Dubaniowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Zarządzanie uprawnieniami w edytorze procesów jest nieefektywne i rozproszono na dwa niezależne miejsca:
- **Uprawnienia do procesów** - definiowanie ról, dostępów, macierzy uprawnień dla całych procesów
- **Uprawnienia do pól formularza** - kontrola widoczności i edytowalności poszczególnych pól w zależności od roli

Administratorzy i konsultanci muszą przechodzić przez wiele ekranów (zakładka formularza, zaznaczanie pola, edycja uprawnień), aby sprawdzić lub zmienić ustawienia. Brak jest globalnego widoku, co utrudnia weryfikację spójności uprawnień i jest bardzo czasochłonne, szczególnie w dużych, wieloetapowych procesach.

### Cel biznesowy
Dostarczenie zunifikowanego narzędzia do zarządzania wszystkimi typami uprawnień w procesach AMODIT. Celem jest umożliwienie administratorom szybkiego przeglądu wszystkich uprawnień w jednym miejscu oraz ich wygodnej, masowej edycji, co skróci czas konfiguracji procesów i zredukuje liczbę błędów.

### Cel techniczny
Implementacja nowego, dedykowanego widoku w edytorze procesów (opartego na React), który będzie prezentował uprawnienia w formie interaktywnej matrycy:
- **Matryca uprawnień do pól** - pola w wierszach, etapy w kolumnach, uprawnienia (edycja, widoczność, wymagane)
- **Matryca uprawnień do procesów** - role, dostępy, macierz uprawnień dla całych procesów

### Metryka sukcesu
- Skrócenie czasu potrzebnego na konfigurację uprawnień dla nowego procesu o 50%.
- Zmniejszenie liczby zgłoszeń serwisowych dotyczących błędnie skonfigurowanych uprawnień pól o 75%.

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

- Rozwiązanie musi być oparte na React (zgodnie z nowym kierunkiem rozwoju UI w AMODIT)
- Musi zapewniać nowoczesny, wydajny i responsywny interfejs
- Musi obsługiwać masowe zmiany uprawnień
- Musi wspierać dziedziczenie uprawnień, filtry i widok wyjątków

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | 2025-09-02 | Matryca będzie nowym, dedykowanym widokiem w edytorze procesów, opartym na React. | Zapewnia to nowoczesny, wydajny i responsywny interfejs, zgodny z nowym kierunkiem rozwoju UI w AMODIT. | - |
| ADR-002 | ✅ Zatwierdzone | 2025-09-02 | Matryca umożliwi masowe zmiany uprawnień, będzie obsługiwać dziedziczenie, filtry i widok wyjątków. | Są to kluczowe funkcjonalności, które adresują główne problemy obecnego rozwiązania i stanowią o wartości nowego narzędzia. | - |
| ADR-003 | 💡 Propozycja | 2025-09-08 | Ikony akcji (edycja, usuwanie) powinny być przypięte do lewego menu, a nie po prawej stronie. | Lepsza ergonomia i łatwość odnalezienia. Obecne umiejscowienie jest nieintuicyjne. | - |
| ADR-004 | ✅ Zatwierdzone | 2025-09-08 | Należy zaimplementować opcję wyboru/filtrowania etapów do wyświetlenia w matrycy. | W procesach z dużą liczbą etapów (np. w SIT) wyświetlanie wszystkich kolumn jest niepraktyczne. Użytkownik powinien móc skupić się na interesującym go fragmencie procesu. | - |
| ADR-005 | ✅ Zatwierdzone | 2025-09-08 | Należy zaimplementować widok kompaktowy (tylko ikony z opisami przy najechaniu). | Poprawi to czytelność matrycy przy dużej liczbie pól i etapów, prezentując więcej danych na jednym ekranie. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🟡 W analizie

**Ukończono:**
- ✅ Zdefiniowanie potrzeby stworzenia matrycy uprawnień
- ✅ Implementacja prototypu matrycy uprawnień dla pól
- ✅ Demo prototypu i zebranie feedbacku UX

**Trwa praca nad:**
- Implementacją poprawek UX na podstawie feedbacku (umiejscowienie ikon, filtrowanie etapów)
- Testami na złożonych procesach (np. z SIT)
- Rozszerzeniem matrycy o uprawnienia do procesów

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| Wydajność przy dużej liczbie pól i etapów | Średnie | Wysoki | Widok kompaktowy, wirtualizacja, lazy loading | Piotr Buczkowski |
| Złożoność UX dla różnych typów uprawnień | Średnie | Średni | Prototypowanie, testy użyteczności | Kamil Dubaniowski |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Matryca uprawnień dla pól (w trakcie)

**Zakres:**
- Interaktywna matryca pól formularza vs etapy procesu
- Uprawnienia: edycja, widoczność, wymagane
- Masowa edycja uprawnień
- Filtry i widok wyjątków
- Widok kompaktowy (ikony z opisami)
- Wybór/filtrowanie etapów do wyświetlenia

**Status:** 🟡 W implementacji

---

### 📦 MVP2: Matryca uprawnień do procesów (zaplanowane)

**Zakres:**
- Macierz uprawnień dla całych procesów
- Definiowanie ról i dostępów
- Zarządzanie uprawnieniami do procesów
- Integracja z macierzą uprawnień dla pól

**Status:** 📋 Zaplanowane

---

### 📦 Backlog (przyszłe wersje)

- Dziedziczenie uprawnień między procesami
- Import/eksport macierzy uprawnień
- Historia zmian uprawnień
- Szablony uprawnień

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-09-02 | Utworzenie projektu - zdefiniowanie potrzeby stworzenia matrycy uprawnień dla pól formularza | [[2025-09-02 Rada architektów]] |
| 2025-09-08 | Demo prototypu matrycy uprawnień dla pól. Feedback UX: przeniesienie ikon akcji, filtrowanie etapów, widok kompaktowy | [[2025-09-08 Sprint review]] |
| 2025-11-29 | Połączenie projektów "Matryca-uprawnien" i "Matryca-uprawnien-dla-pol" w jeden zunifikowany projekt | Reorganizacja dokumentacji |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Edytor-procesow]]
- **Repozytorium:** [do uzupełnienia]
- **Środowisko DEV:** [do uzupełnienia]

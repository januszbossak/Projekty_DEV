# Project Canvas: Wzmiankowanie w komentarzach

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-04
**Klient:** AMODIT (roadmapa)
**Data rozpoczęcia:** 2025-09-04

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **PDM** | Damian Kamiński | Opisanie wymagań |
| **Tech Lead** | Piotr Buczkowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Mechanizm wzmiankowania (`@mention`) w komentarzach jest nieintuicyjny i generuje problemy. Użytkownik, który zostaje wspomniany, nie otrzymuje bezpośredniego powiadomienia o tym fakcie. Zamiast tego, system automatycznie dodaje go jako "obserwatora" sprawy, co jest mylące i skutkuje zalewaniem go wszystkimi kolejnymi powiadomieniami dotyczącymi tej sprawy, nawet jeśli nie są dla niego istotne.

### Cel biznesowy
Stworzenie klarownego i efektywnego mechanizmu komunikacji w sprawach. Użytkownik wspomniany w komentarzu ma otrzymać precyzyjną informację o tym fakcie i uzyskać dostęp do sprawy, ale bez bycia zasypywanym niechcianymi powiadomieniami.

### Cel techniczny
Przebudowa logiki wzmiankowania. Zamiast dodawać użytkownika jako "obserwatora", system będzie nadawał mu rolę "Reader" (dostęp do odczytu bez powiadomień). Wprowadzenie dedykowanego powiadomienia e-mail o samej wzmiance. Dodatkowo, umożliwienie nadawania roli "Reader" bezpośrednio z interfejsu uprawnień.

### Metryka sukcesu
- Spadek o 90% liczby niechcianych powiadomień generowanych przez mechanizm wzmiankowania.
- Użytkownicy otrzymują dedykowany e-mail o wzmiance w ciągu minuty od jej dodania.
- Administratorzy mogą nadawać rolę "Reader" z UI, co zwiększa elastyczność zarządzania uprawnieniami.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-04]] | Wzmiankowanie użytkownika, który nie ma dostępu do sprawy, nadaje mu rolę **Reader**, a nie Obserwator. | Rola Reader zapewnia dostęp do sprawy, ale nie generuje powiadomień o wszystkich zmianach, co eliminuje problem spamu mailowego. Rola Obserwatora jest do tego nieodpowiednia. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-04]] | Każde wzmiankowanie (`@mention`) wysyła dedykowany e-mail "Zostałeś wzmiankowany w komentarzu...". | Jest to bezpośrednia i klarowna informacja dla użytkownika, w przeciwieństwie do mylącego maila "Zostałeś dodany jako obserwator". | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-09-04]] | Jeśli ktoś odpowie na komentarz, w którym użytkownik był wzmiankowany, ten użytkownik również otrzyma powiadomienie. | Zapewnia to ciągłość konwersacji w danym wątku, bez informowania o niepowiązanych komentarzach w tej samej sprawie. | - |
| ADR-004 | ✅ Zatwierdzone | [[2025-09-04]] | Możliwość nadawania roli **Reader** zostanie dodana bezpośrednio do interfejsu zarządzania uprawnieniami w sprawie. | Rola ta jest użyteczna nie tylko przy wzmiankowaniu. Umożliwienie jej nadawania z UI zwiększa elastyczność administratorów w zarządzaniu dostępem "tylko do odczytu". | Pozostawienie jej tylko dla reguł (`Adjust Role`) jest niepotrzebnym ograniczeniem. |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

**Trwa praca nad:**
- Szczegółowym opisaniem wymagań i logiki (Damian Kamiński).

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-04]] | Utworzenie projektu. Zdefiniowanie nowej logiki wzmiankowania (Reader zamiast Obserwatora), dedykowanych powiadomień e-mail i dodania roli Reader do UI. | [[2025-09-04 Rada architektów]] |

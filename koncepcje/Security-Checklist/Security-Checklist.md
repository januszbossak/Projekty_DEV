# Project Canvas: Security Checklist

**Status:** 🟡 W analizie
**Ostatnia aktualizacja:** 2025-09-08
**Klient:** AMODIT (proces wewnętrzny)
**Data rozpoczęcia:** 2025-09-08

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Daniel Reszka | Przygotowanie listy, konsultacje |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klienci z instalacjami on-premise często przeprowadzają testy penetracyjne na swoich środowiskach. Zdarzały się sytuacje, w których testy te były wykonywane na serwerach bez podstawowych zabezpieczeń (hardening/tuning), co prowadziło do fałszywie negatywnych wyników i niepotrzebnego angażowania zespołu AMODIT w analizę problemów, które wynikały z błędnej konfiguracji infrastruktury, a nie z luk w aplikacji.

### Cel biznesowy
Zapewnienie, że testy bezpieczeństwa u klientów on-premise są przeprowadzane na odpowiednio zabezpieczonych środowiskach. Celem jest formalizacja procesu weryfikacji konfiguracji serwera, co zwiększy wiarygodność wyników testów i zredukuje liczbę fałszywych alarmów.

### Cel techniczny
Stworzenie i wdrożenie standardowej checklisty bezpieczeństwa (hardening checklist) dla serwerów. Checklista będzie musiała być formalnie potwierdzona przez konsultanta wdrażającego i klienta przed rozpoczęciem jakichkolwiek testów penetracyjnych.

### Metryka sukcesu
- 100% testów penetracyjnych u klientów on-premise jest poprzedzone formalnym potwierdzeniem wypełnienia checklisty bezpieczeństwa.
- Redukcja o 90% liczby zgłoszeń z testów penetracyjnych, które wynikają z błędnej konfiguracji serwera.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-09-08]] | Należy stworzyć formalną listę Security Checklist, która będzie przekazywana klientom z instalacją on-premise. | Standaryzuje to proces zabezpieczania serwerów i stanowi dowód, że klient został poinformowany o zalecanych praktykach bezpieczeństwa. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-09-08]] | Checklista musi być potwierdzona przez konsultanta i klienta przed rozpoczęciem pen testów. | Zapewnia to obustronną odpowiedzialność i pozwala uniknąć sytuacji, w której testy są przeprowadzane na niezabezpieczonym systemie. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🟡 W analizie

**Trwa praca nad:**
- Finalizacją listy Security Checklist (wstępnie omówiona z Danielem Reszką).

**Dalsze kroki:**
- Przekazanie gotowej checklisty do konsultantów i klientów, którzy planują testy bezpieczeństwa.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-08]] | Utworzenie projektu w odpowiedzi na potrzebę formalizacji procesu weryfikacji zabezpieczeń serwerów on-premise przed testami penetracyjnymi. | [[2025-09-08 Sprint review]] |

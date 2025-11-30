# Project Canvas: Moduł raportowy (stary)

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-11
**Klient:** Wewnętrzny (refaktoryzacja) + WIM (nowa funkcja)
**Data rozpoczęcia:** 2025-09-11

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | Piotr Buczkowski | Analiza i PoC |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
W systemie AMODIT istnieją starsze mechanizmy raportowe (tzw. "stare raporty", np. raporty osadzone na formularzu, raporty oparte bezpośrednio o SQL), które technologicznie i koncepcyjnie różnią się od nowego, webowego modułu raportowego. Brakowało dla nich dedykowanego miejsca w dokumentacji, co prowadziło do nieporozumień i utrudniało zarządzanie wymaganiami.

### Cel biznesowy
Uporządkowanie dokumentacji projektowej poprzez wyraźne oddzielenie starszych technologii raportowych od nowego modułu. Ma to na celu ułatwienie planowania prac, unikanie pomyłek i zapewnienie, że nowe funkcjonalności dla starych raportów (jak np. wymaganie klienta WIM) są rozwijane w odpowiednim kontekście technologicznym.

### Cel techniczny
Stworzenie centralnego miejsca do dokumentowania architektury, decyzji i planów rozwoju dla wszystkich mechanizmów raportowych niebędących częścią nowego, webowego modułu raportowego.

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: Edytowalne checkboxy w raportach osadzonych (Plan: Q4 2025)

**Cel:** Dostarczenie klientowi WIM funkcjonalności edytowalnych checkboxów w raportach osadzonych.

**Funkcjonalności:**
- [ ] Możliwość zdefiniowania kolumny w raporcie osadzonym jako edytowalny checkbox.
- [ ] Zmiana stanu checkboxa w UI powinna wywoływać akcję zapisu w bazie danych.

**Zadania:**
- **Piotr Buczkowski:** Przygotowanie Proof of Concept (PoC).

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-11]] | Utworzenie projektu w celu wydzielenia dokumentacji dla "starych raportów" z głównego [[Modul-raportowy|modułu raportowego]]. Pierwszym wymaganiem jest realizacja edytowalnych checkboxów dla klienta WIM. | [[2025-09-11 Rada architektów]] |

---

## 6. PRZYDATNE LINKI
- **Powiązane wymaganie klienta:** [[klienci/WIM/Raporty-osadzone-checkboxy]]

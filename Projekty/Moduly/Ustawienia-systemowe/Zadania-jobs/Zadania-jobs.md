# Project Canvas: Zarządzanie zadaniami (Jobs)

**Projekt nadrzędny:** [[Ustawienia-systemowe]]
**Status:** 🛠️ W realizacji
**Ostatnia aktualizacja:** 2025-08-25
**Klient:** AMODIT (roadmapa)

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | [do uzupełnienia] | Architektura |
| **Deweloper** | [do uzupełnienia] | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Konfiguracja zadań cyklicznych (Jobów) w AMODIT jest nieintuicyjna i podatna na błędy. Administratorzy muszą ręcznie wpisywać wartości w bazie danych, a konsultanci często błędnie konfigurują harmonogramy (np. uruchamiając regułę co minutę przez całą dobę, zamiast w godzinach pracy), co prowadzi do niepotrzebnego obciążenia systemu.

### Cel biznesowy
Usprawnienie i uproszczenie konfiguracji zadań systemowych (Jobów) poprzez stworzenie intuicyjnego interfejsu graficznego, który wyeliminuje potrzebę ręcznej edycji bazy danych i zminimalizuje ryzyko błędów konfiguracyjnych.

### Cel techniczny
Stworzenie API i interfejsu w React do zarządzania Jobami, który będzie oferował listy wyboru zamiast pól tekstowych, walidację wprowadzanych danych oraz wizualny konfigurator harmonogramu.

### Metryka sukcesu
- **Zero błędów** konfiguracyjnych wynikających z literówek w nazwach klas (dzięki listom wyboru).
- Administrator może skonfigurować nowy Job **w < 2 minuty**.

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[2025-08-25]] | Wybór biblioteki i klasy Joba z listy rozwijanej (słownika), a nie przez ręczne wpisywanie. | Eliminacja błędów ludzkich (literówek), które są częstym problemem przy obecnej konfiguracji. | - |
| ADR-002 | ✅ Zatwierdzone | [[2025-08-25]] | System przy starcie automatycznie skanuje wszystkie klasy implementujące interfejs `IJob` i tworzy dostępny w UI słownik. | Zapewnia, że lista wyboru jest zawsze aktualna i zawiera wszystkie dostępne w systemie Joby, bez potrzeby ręcznej aktualizacji. | - |
| ADR-003 | ✅ Zatwierdzone | [[2025-08-25]] | Intuicyjna konfiguracja harmonogramu z wizualnym podglądem (godzina startu, końca, częstotliwość). | Upraszcza konfigurację dla nietechnicznych użytkowników i zapobiega błędom, takim jak ustawianie zadań w nocy w weekendy. | - |
| ADR-004 | 💡 Propozycja | [[2025-08-25]] | Ujednolicenie ikonek dla "Integracje" i "Rozszerzenia" lub połączenie ich w jedną zakładkę. | Obecne, identyczne ikonki wyglądają jak błąd w interfejsie i wprowadzają użytkownika w błąd. | - |
| ADR-005 | ✅ Zatwierdzone | [[2025-09-08]] | Dodać przycisk do ręcznego odświeżania statusu wszystkich jobów. | Automatyczne odświeżanie jest niepożądane, ale administrator musi mieć możliwość weryfikacji aktualnego stanu bez przeładowywania strony. | - |
| ADR-006 | ✅ Zatwierdzone | [[2025-09-08]] | Ikony akcji (edycja, usuwanie) powinny być widoczne od razu po najechaniu na wiersz, a nie na konkretną kolumnę. | Poprawia to użyteczność i spójność interfejsu z innymi widokami w systemie. | - |

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 🛠️ W realizacji (Prototyp)

Zaimplementowano prototyp API oraz formularza do dodawania i edycji Jobów. Wymaga on jeszcze dopracowania UI i dodania walidacji.

**Ukończono:**
- ✅ API do zarządzania Jobami (CRUD).
- ✅ Formularz dodawania/edycji Joba z wyborem klasy z listy.
- ✅ Intuicyjna konfiguracja częstotliwości z podglądem.

**Trwa praca nad:**
- [ ] Poprawa formatowania daty (spójność z resztą systemu).
- [ ] Dodanie walidacji wprowadzanych wartości.
- [ ] Ujednolicenie ikonek w menu głównym ustawień.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|---|---|---|
| [[2025-08-25]] | Utworzenie podprojektu. Zaimplementowano prototyp interfejsu do zarządzania Jobami. | [[2025-08-25 Sprint review]] |
| [[2025-09-08]] | Demo widoku tabelarycznego jobów. Zebrano feedback: potrzeba dodania przycisku odświeżania i poprawy widoczności ikon akcji. | [[2025-09-08 Sprint review]] |

---

## 6. PRZYDATNE LINKI
- **Projekt nadrzędny:** [[Ustawienia-systemowe]]


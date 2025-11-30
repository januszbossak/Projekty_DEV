# Moduł raportowy

**Klient:** AMODIT (roadmapa)
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Tech Lead:** Łukasz, Ania, Damian
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Modul-raportowy]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR) - w tym zarządzanie biblioteką DevExtreme
- Roadmapa MVP (Personalizacja, Wydajność, Gantt, Tłumaczenia)
- Architektura techniczna (DevExtreme)
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Użytkownicy potrzebują elastycznego narzędzia do analizy danych i prezentacji wyników. Obecny moduł wymaga ciągłych ulepszeń w użyteczności, personalizacji wizualizacji i integracji z narzędziami zewnętrznymi.

### Rozwiązanie

Nowoczesny, intuicyjny moduł raportowy umożliwiający samodzielne tworzenie zaawansowanych raportów:
- **Personalizacja** - edycja palet gradientów, kolory dostosowane do organizacji
- **Wydajność** - filtry wymagane i domyślne dla dużych zbiorów danych
- **Integracja** - masowe podpisywanie dokumentów SimplySign
- **Użyteczność** - tłumaczenia etykiet, aliasy kolumn, ulepszenia Gantt
- **Technologia** - oparte na bibliotece DevExtreme

### Obecna faza

🛠️ **W realizacji** - ciągły rozwój

**Ukończono:**
- ✅ Edycja palety gradientów
- ✅ Filtry wymagane i domyślne
- ✅ Masowe podpisywanie SimplySign
- ✅ Kolorowanie z gradientem (w testach)

**W trakcie:**
- Usprawnienia Gantt (etykiety, tooltip)
- Tłumaczenia i aliasy (3 etapy)
- Filtr "w miesiącu" (ukrycie roku)

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Biblioteka DevExtreme** jako fundament modułu | Szeroki zakres typów wykresów, wysoka jakość wizualizacji, interaktywność |
| **Klucz licencyjny w kodzie publicznym** | Zgodne z oficjalną polityką dostawcy dla aplikacji JavaScript |
| **Ania jako opiekun biblioteki** | Osoba odpowiedzialna za monitorowanie zmian, zgłaszanie błędów, aktualizacje |

---

## MVP aktualnie w realizacji

### Ulepszenia raportów Gantt

**Cel:** Poprawienie agregowanych belek na wykresach Gantt

**Zakres:**
- [ ] Usunięcie dynamicznej etykiety ze zbiorczych belek
- [ ] Poprawienie tooltip - prawidłowy zakres dat

### Tłumaczenia i aliasy (3 etapy)

**Cel:** Eliminacja niezrozumiałych nazw technicznych

**Zakres:**
- [ ] Globalne tłumaczenia w źródłach danych
- [ ] Tłumaczenia funkcji agregujących (prawdopodobnie gotowe)
- [ ] Aliasy per raport

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Paleta kolorów - brak konsensusu | Odroczone - wymaga konsultacji ze specjalistą (Michał Maliszewski) |

---

## Szybkie linki

- Use Cases: `projekty/UC moduł raportowy/`
- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]

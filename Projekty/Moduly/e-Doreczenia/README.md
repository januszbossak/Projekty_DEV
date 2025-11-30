# e-Doręczenia

**Klient:** AMODIT (roadmapa)
**Status:** 🔴 Krytyczny problem
**PDM:** [do uzupełnienia]
**Tech Lead:** Adrian, Piotr

---

## Dokumentacja projektu

📄 **Project Canvas:** [[e-Doreczenia]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- **Krytyczne ryzyka** i bieżące problemy
- Roadmapa MVP
- Historia zmian

---

## Szybki przegląd

### Problem

Klienci AMODIT muszą spełnić wymogi prawne dotyczące obsługi elektronicznych doręczeń w ramach systemu e-Doręczeń (Poczta Polska). Bez stabilnej integracji z tym systemem nie mogą automatycznie odbierać i wysyłać dokumentów urzędowych.

### Rozwiązanie

Pełna integracja AMODIT z systemem e-Doręczeń Poczty Polskiej umożliwiająca:
- Automatyczne odbieranie dokumentów urzędowych
- Wysyłanie e-Doręczeń bezpośrednio z AMODIT
- Spełnienie wymogów prawnych
- Działanie na środowiskach on-premise i chmurowych

### Obecna faza

🔴 **KRYTYCZNY PROBLEM - najwyższy priorytet**

**Problem:**
Integracja z e-Doręczeniami **nie działa na środowisku chmurowym** dla klientów produkcyjnych **od ponad 3 miesięcy**. Działa poprawnie na środowiskach on-premise. Blokuje kluczową funkcjonalność, za którą klienci płacą.

**Diagnostyka w toku:**
- Adrian odłożył wszystkie zadania - focus na rozwiązaniu problemu
- Piotr wspiera diagnostykę
- Tworzenie programu testującego połączenie
- Podejrzenie: błąd w konfiguracji Azure (Key Vault, ustawienia sieciowe, lokalizacja serwerów)

---

## Krytyczne ryzyko

| Ryzyko | Mitygacja |
|--------|-----------|
| **Integracja nie działa na chmurze od 3+ miesięcy** | Adrian i Piotr - diagnostyka Azure (Key Vault, sieciowe). Program testowy na różnych serwerach. Najwyższy priorytet |
| **Brak odpowiedzi z Poczty Polskiej** | Klienci eskalują u swoich opiekunów handlowych. Focus na diagnostyce po stronie AMODIT |
| **Utrata zaufania klientów chmurowych** | Transparentna komunikacja o statusie prac. Szczegółowe info o blokadach dla Daniela Reszki |

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Dokumentacja API: [do uzupełnienia]
- Backlog: [do uzupełnienia]

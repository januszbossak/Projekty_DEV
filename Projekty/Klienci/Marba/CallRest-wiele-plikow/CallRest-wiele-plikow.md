# Project Canvas: CallRest - wysyłanie wielu plików

**Status:** 🟢 W realizacji
**Ostatnia aktualizacja:** 2025-09-11
**Klient:** Marba
**Data rozpoczęcia:** 2025-09-11

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Deweloper** | Adrian Kotowski | Implementacja |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
Klient Marba ma specyficzne wymaganie biznesowe dotyczące integracji z zewnętrznym Web Servicem. Proces wymaga wysłania dynamicznej i potencjalnie dużej liczby plików (do 100) w jednym żądaniu HTTP w formacie `multipart/form-data`. Obecna implementacja funkcji `CallRest` w AMODIT nie obsługuje takiego scenariusza w elastyczny sposób.

### Cel biznesowy
Umożliwienie klientowi Marba realizacji kluczowego procesu biznesowego, który jest zablokowany przez obecne ograniczenia techniczne platformy AMODIT.

### Cel techniczny
Projekt ten jest głównym motorem napędowym dla rozbudowy funkcjonalności opisanej w projekcie [[Integracje-REST-multipart]]. Celem jest dostarczenie rozwiązania, które pozwoli na dynamiczne konstruowanie żądań `multipart/form-data` z wieloma plikami, zgodnie ze specyfikacją techniczną uzgodnioną w ramach w/w projektu ogólnego.

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-09-11]] | Utworzenie projektu w odpowiedzi na specyficzne wymaganie klienta Marba, które stało się bezpośrednim impulsem do rozbudowy ogólnego mechanizmu `CallRest` o obsługę wielu plików. | [[2025-09-11 Rada architektów]] |

---

## 6. PRZYDATNE LINKI
- **Projekt nadrzędny:** [[Integracje-REST-multipart]]

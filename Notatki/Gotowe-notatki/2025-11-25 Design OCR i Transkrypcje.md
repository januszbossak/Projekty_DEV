# Notatka projektowa – 2025-11-25 – Design OCR i Transkrypcje

**Data:** 2025-11-25
**Temat główny:** Możliwości implementacji OCR On-Premise oraz kwestie zarządzania transkrypcjami.

---

## 1. Funkcjonalność OCR On-Premise

### Cel i problem
Klient (on-prem) zgłasza zapotrzebowanie na lokalną instalację usług OCR (rozumianych szerzej jako funkcjonalności AI, Copilot). Pytanie o możliwość i sensowność takiej implementacji.

### Rozważane alternatywy
| Opcja | Opis | Status |
|-------|------|--------|
| Obecne rozwiązanie | Wykorzystanie chmurowych modeli LLM (np. GPT-4o mini) wraz z dedykowanymi modelami dla faktur/paragonów. | ✅ Wybrana (obecnie) – działa w chmurze, nie daje możliwości lokalnej instalacji silnika. |
| Dedykowane modele lokalne | Implementacja wyspecjalizowanych, otwartych modeli LLM (np. LLAMA) lokalnie na serwerze klienta. | ⏸️ Odroczona – wymaga testów na wydajnym sprzęcie (np. Mac z 32GB RAM), obecne modele lokalne są znacznie słabsze (1-2 rzędy wielkości) niż chmurowe. |

### Decyzja / Sposób realizacji
**Status:** ✅ Zatwierdzone

- **Brak możliwości instalacji on-premise:** Obecna funkcjonalność OCR w AMODIT opiera się na modelach chmurowych, które nie mogą być przeniesione lokalnie.
- **Ocena opłacalności on-premise:** Rozwiązanie on-premise jest bezpieczniejsze (dane lokalnie), ale prawdopodobnie droższe w utrzymaniu (koszty infrastruktury) i wolniejsze (słabsze modele lokalne). Opłacalne jedynie przy przetwarzaniu milionów dokumentów.

### Ograniczenia / Poza zakresem
- Nie rozważa się obecnie lokalnej implementacji OCR w najbliższej przyszłości.

---

## 2. Zarządzanie Transkrypcjami ze Spotkań

### Cel i problem
Zapewnienie łatwego i niezawodnego dostępu do transkrypcji ze spotkań (szczególnie w kontekście ich przetwarzania na notatki). Obecne metody (np. kopiowanie) są zawodne i generują niekompletne dane.

### Rozważane alternatywy
Jedna propozycja, bez alternatyw.

### Decyzja / Sposób realizacji
**Status:** 🔍 Do weryfikacji

- Konieczność weryfikacji możliwości konfiguracji dostępu do transkrypcji ze spotkań w systemie Teams/Microsoft Stream, aby zapewnić pełny i niezakłócony dostęp do materiałów źródłowych.
- Sprawdzenie możliwości zbiorczego pobierania lub udostępniania transkrypcji.

### Punkty otwarte
- Kamil ma sprawdzić możliwość udostępnienia transkrypcji.
- Damian sprawdzi, czy da się skonfigurować dostęp do transkrypcji zbiorczo.

---

## Propozycja podziału na pakiety prac (MVP)

Brak propozycji podziału na MVP.

---

## Punkty do dalszej dyskusji (globalne)

- Konieczność weryfikacji możliwości konfiguracji dostępu do transkrypcji ze spotkań.
- Analiza zagadnień designowych, które Kamil miał przedstawić.

---
ostatnia_aktualizacja: 2025-12-08
changelog_przeglad_do: 2025-11-17
---

# Architektura: AMODIT Copilot

> **Ostatnia aktualizacja:** 2025-12-08  
> **CHANGELOG przegląd do:** 2025-11-17

---

## Aktualna koncepcja

### Stack techniczny

- **Frontend:** [DO UZUPEŁNIENIA]
- **Backend:** .NET 8 / mikroserwis dla AI
- **Baza danych:** MSSQL
- **AI Platform:** Microsoft Azure (modele: GPT-4o, GPT-4o mini, GPT-3.5)
- **Embedding models:** Wykorzystywane w bazie wiedzy organizacji
- **Inne technologie:** Asynchroniczne przetwarzanie dla długich operacji (polling)

### Główne komponenty

- **Copilot UI:** Interfejs konwersacyjny dla użytkownika (chat, generowanie procesów, baza wiedzy)
- **Mikroserwis AI:** Zarządzanie promptami, wywołania do Azure OpenAI, obsługa polling dla długich operacji
- **Baza wiedzy:** Prywatna per instancja, wektorowa baza danych z embeddingami dokumentów organizacji
- **Integration Layer:** Funkcje silnika reguł AMODIT dla automatyzacji procesów

### Integracja z AMODIT

**Funkcje silnika reguł dostępne w procesach:**
- `Knowledge Base Document Insert` - dodawanie dokumentów do bazy wiedzy ze sprawy
- `Knowledge Base Search` - wyszukiwanie w bazie wiedzy
- `Ask AI` - zapytania do AI na poziomie pojedynczej sprawy (analiza dokumentów, OCR post-processing)
- `Get To Do` - zarządzanie zadaniami przez AI

**Uprawnienia:**
- `Copilot Access` (ustawienia systemowe) - dostęp do funkcjonalności Copilota
- `Organization Key` (automatycznie) - klucz organizacji dla izolacji danych
- Zarządzanie bazami wiedzy przez administratorów

**Bezpieczeństwo:**
- Dane przetwarzane przez Microsoft na terytorium Unii Europejskiej
- Prywatna baza wiedzy per instancja (izolacja danych między klientami)
- Microsoft nie wykorzystuje danych do trenowania modelu ani nie przechowuje ich (poza krótką historią konwersacji)

---

## Kluczowe decyzje architektoniczne

| Data | Decyzja | Dlaczego | Status | Źródło |
|------|---------|----------|--------|--------|
| [[2025-08-26]] | Rozdzielono funkcjonalności Copilota i AI OCR na dwa osobne projekty | Dwie odrębne, duże funkcjonalności - lepsze zarządzanie i klarowniejsza komunikacja | ✅ Wdrożone | [[2025-08-26 Notatka projektowa - AMODIT UI]] |
| [[2025-09-08]] | Wprowadzenie trybu konsultacyjnego z predefiniowanym zestawem pytań analitycznych | Zmiana z "narzędzia" na "asystenta" - pomaga ustrukturyzować wymagania i prowadzi do tworzenia bardziej kompletnych procesów | ✅ Wdrożone | [[2025-09-08 Sprint review]] |
| [[2025-09-08]] | Generowanie procesu jako operacja asynchroniczna z pollingiem statusu | Generowanie jest długotrwałe - asynchroniczność rozwiązuje timeouty na gateway i poprawia UX | ✅ Wdrożone | [[2025-09-08 Sprint review]] |
| [[2025-09-08]] | Prompt konsultacyjny przechowywany i zarządzany po stronie mikroserwisu | Umożliwia szybkie iteracje i zmiany w zachowaniu Copilota bez wdrażania nowej wersji całej aplikacji AMODIT | ✅ Wdrożone | [[2025-09-08 Sprint review]] |
| [[2025-09-18]] | Prywatna baza wiedzy per instancja z izolacją między klientami | Bezpieczeństwo danych - wiedza organizacji nie wychodzi poza organizację, dokumenty dodawane świadomie (brak auto-dodawania), zerwanie uprawnień do sprawy przy dodaniu do bazy wiedzy | ✅ Wdrożone | [[2025-09-18 Planowanie sprintu]] |
| [[2025-09-08]] | Uatrakcyjnienie procesu oczekiwania na generowanie (spinner z dynamicznymi komunikatami) | Obecny statyczny ekran jest mało angażujący - dynamiczne komunikaty poprawią UX | 💡 Propozycja | [[2025-09-08 Sprint review]] |
| [[2025-09-08]] | Zmiana promptu na zadawanie pytań pojedynczo zamiast w bloku | Bardziej naturalna konwersacja przypominająca interakcję z ludzkim konsultantem | 💡 Propozycja | [[2025-09-08 Sprint review]] |
| [[2025-11-04]] | Dedykowane spotkanie w sprawie RODO i bezpieczeństwa danych w module AI | Potencjalne kwestie RODO związane z modułem AI wymagają pogłębionej analizy (szyfrowanie, retencja, przechowywanie u klienta on-prem) | 🔍 Do weryfikacji | [[2025-11-04 Rada architektów]] |

**Statusy:**
- ✅ **Wdrożone** - decyzja wdrożona na produkcji
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona

**Pełna historia decyzji:** Zobacz [[Projekty/Moduly/AMODIT Copilot/CHANGELOG#Decyzje]]

---

## Historia koncepcji (odrzucone/zmienione)

*(Brak odrzuconych koncepcji w CHANGELOG - wszystkie zaproponowane decyzje zostały wdrożone lub są w propozycji)*

---

## Dla developera

### Lokalne uruchomienie

```bash
# [DO UZUPEŁNIENIA]
```

### Struktura kodu

- **Główny moduł:** [DO UZUPEŁNIENIA]
- **Komponenty:** [DO UZUPEŁNIENIA]
- **API client:** [DO UZUPEŁNIENIA]

### Problemy techniczne (znane z CHANGELOG)

**Baza wiedzy (2025-09-18):**
- Długi czas zapisu dokumentów
- Brak IntelliSense dla funkcji w silniku reguł
- Brak tytułu przy dodawaniu dokumentu z reguły
- Metadata jako obiekt JSON (wymaga odpowiedniego formatowania)

**UI (2025-10-20, 2025-11-03):**
- Brak trwałości przesłanych dokumentów (tylko na czas konwersacji) - zgłoszona potrzeba
- Brak wyświetlania nazwy procesu przy uruchamianiu sprawy przez AI
- Poprawa wyświetlania znaczników function calling (przycisk z ogólnym opisem zamiast kodu)

**PKF (2025-09-02):**
- Problem z analizą procesów z PKF - jeden z procesów powoduje błąd (przekazane Mateuszowi)

### Linki

- **Repozytorium:** [DO UZUPEŁNIENIA]
- **Środowisko DEV:** [DO UZUPEŁNIENIA]
- **Środowisko TEST:** [DO UZUPEŁNIENIA]
- **Dokumentacja techniczna:** [DO UZUPEŁNIENIA]
- **Wiki AMODIT:** Zawiera pełną dokumentację dostępną w Copilocie

---


# Repozytorium Plików (DMS)

**Klient:** WIM
**Status:** 🟡 W analizie
**PDM:** Damian

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Repozytorium]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Szczegółowa architektura techniczna (tabele, Lucene, uprawnienia)
- Roadmapa MVP1 i MVP2+
- Ryzyka i punkty do dyskusji
- Historia zmian

---

## Szybki przegląd

### Problem
Klient potrzebuje centralnego miejsca do przechowywania plików **niezwiązanych ze sprawami** (dokumenty korporacyjne, szablony, materiały referencyjne).

### Rozwiązanie
Moduł **Repozytorium Plików** jako część AMODIT:
- Hierarchia: Przestrzenie → Foldery → Pliki
- Uprawnienia niezależne od procesów (użytkownicy, grupy)
- Wyszukiwanie pełnotekstowe (Lucene) z uwzględnieniem bezpieczeństwa
- Reużycie mechanizmów AMODIT (tabela `caseattachment`, storage)

### Obecna faza
📋 **Analiza i specyfikacja**

**Ukończono:**
- ✅ Specyfikacja funkcjonalna (2025-10-28)
- ✅ Decyzje architektoniczne - moduł częścią AMODIT
- ✅ Projekt struktury bazy danych (4 nowe tabele)

**Do finalizacji:**
- Precyzyjne zdefiniowanie poziomów uprawnień (`read`, `modify`, `admin`)
- Limity i ograniczenia (rozmiar pliku, głębokość folderów)
- Strategia migracji istniejących plików klientów

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Część AMODIT** (nie osobny moduł) | Reużycie mechanizmów, spójność |
| **Tabela `caseattachment` + kolumna `attRepository`** | Wspólny mechanizm storage |
| **"Przestrzenie"** jako najwyższy poziom | Uniknięcie konfliktu z "obszarami" |
| **MVP1: uprawnienia tylko dla przestrzeni** | Szybsze dostarczenie wartości |
| **Indeksowanie Lucene** | Wyszukiwanie pełnotekstowe |

---

## MVP1: Podstawowa funkcjonalność

**Cel:** Minimalna, funkcjonalna wersja - walidacja podejścia z klientem

**Zakres:**
- ✅ Struktura: Przestrzenie → Foldery → Pliki
- ✅ Uprawnienia: `read`, `modify`, `admin` (tylko przestrzenie)
- ✅ CRUD: tworzenie, edycja, usuwanie folderów i plików
- ✅ Wyszukiwanie pełnotekstowe z uwzględnieniem uprawnień
- ✅ Historia zmian (JSON)

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Wydajność wyszukiwania przy dużych plikach (100+ MB) | Testy PoC, asynchroniczne indeksowanie |
| Migracja istniejących plików klientów | Narzędzie migracyjne w MVP1 |
| Niejasne granice poziomów uprawnień | Warsztat z klientem WIM |

---

## Szybkie linki

- Umowa: [link/numer]
- Backlog: [link do Azure DevOps]
- Repozytorium: [link]
- Makiety UI: [link do Figmy]

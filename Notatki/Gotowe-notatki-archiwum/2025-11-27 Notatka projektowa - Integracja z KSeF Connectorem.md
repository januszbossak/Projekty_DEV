> 🛡️ Zweryfikowano przez Note Reviewer: 2025-12-09

# Notatka projektowa – 2025-11-27 – Integracja z KSeF Connectorem – rozszerzenie API

**Data:** 2025-11-27
**Temat główny:** Integracja z KSeF Connectorem – rozszerzenie API (propozycja V2)
**Powiązane projekty:**
- `Integracje/Integracja-KSeF`
- `cross-cutting/Zarzadzanie-licencjami`

---

## 1. Nowy kontroler API dla KSeF Connector

**Komponent:** Integracje (KSeF Connector / REST API)

### Cel i problem

Konieczność zastąpienia istniejącego handlera `ashx` nowym rozwiązaniem. Handlery HTTP to technologia niewspierana, która nie będzie dostępna w .NET Core (co jest kluczowe w kontekście planowanej migracji systemu).

### Rozważane alternatywy

| Opcja | Opis | Status |
|-------|------|--------|
| **Rozbudowa handlera ashx** | Dalszy rozwój obecnego rozwiązania | ❌ Odrzucona – brak wsparcia w .NET Core, technologia legacy |
| **Nowy kontroler API** | Stworzenie dedykowanego kontrolera w REST API | ✅ Wybrana – zgodność z nowymi standardami, gotowość na migrację |

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone (Piotr Buczkowski zatwierdził zmiany)

Zastąpienie handlera `ashx` nowym kontrolerem API. Rozwiązanie ma być gotowe do wdrożenia natychmiast ("mogę wrzucić nawet za chwilę").

**Szczegóły techniczne:**
- **Metody:** Nowy endpoint obsłuży metody `POST` i `PUT`.
- **Struktura żądań:** Niemal identyczna jak w starym handlerze (dla łatwości migracji).
- **Funkcjonalność:**
    - Zwracanie ID sprawy (CaseID).
    - Możliwość przekazywania CustomAttributes.
    - Wykorzystanie wspólnego kodu (shared code) z obecnym rozwiązaniem.
- **Routing:** Endpoint będzie należał do "rodziny endpointów REST API Amodit", ale z dedykowanym prefiksem:
    - Ścieżka: `restapi/integration/ksef/v1`
    - Stanowi to nowy wzorzec dla dedykowanych integracji.

### Ograniczenia / Poza zakresem

- **Licencjonowanie:** Endpoint **NIE będzie podlegał licencjonowaniu** (w przeciwieństwie do standardowych endpointów REST API).

---

## 2. Model uwierzytelniania i kompatybilność

**Komponent:** Integracje (KSeF Connector / Security)

### Cel i problem

Zapewnienie bezpiecznego dostępu dla KSeF Connectora bez naruszania modelu licencyjnego oraz utrzymanie ciągłości działania u klientów (kompatybilność wsteczna).

### Decyzja / Sposób realizacji

**Status:** ✅ Zatwierdzone

**Uwierzytelnianie:**
- Niezależne od standardowego REST API Amodit.
- Wykorzystanie tego samego tokenu, który był używany przez handler (token niewygasający).

**Kompatybilność wsteczna:**
- Stary handler `ashx` pozostaje dostępny i funkcjonuje.
- Logika po stronie KSeF Connector (ustalone z zespołem P. Wągla):
    1. Sprawdzenie czy dostępny jest nowy endpoint.
    2. Jeśli tak → użycie nowego endpointu.
    3. Jeśli nie → fallback do starego handlera.

---

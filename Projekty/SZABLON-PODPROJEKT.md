# Szablon Podprojektu

Szablon dla podprojektów - części większego projektu (np. Edytor-formularzy jako część Edytor-procesow).

**Pełna struktura 6 sekcji** - identyczna z głównym Project Canvas, ale bez sekcji "Podprojekty".

---

## Kiedy tworzyć podprojekt?

Utwórz podprojekt gdy element głównego projektu:
- Ma **własny cykl życia** (osobne MVP, osobny harmonogram)
- Jest **na tyle duży**, że wymaga osobnego śledzenia (>50 linii dokumentacji)
- Ma **własny zespół** lub dedykowaną osobę
- Może być **niezależnie wdrożony** (nie blokuje innych części)

**Przykłady:**
- Edytor-procesow → Edytor-formularzy, Edytor-diagramu, Matryca-uprawnien
- Trust-Center → Podpisy-kwalifikowane-macOS, Podpisy-chmurowe

---

## Struktura katalogów

```
Projekt-glowny/
├── Projekt-glowny.md          # Główny Project Canvas + odsyłacze
├── README.md
├── Podprojekt-A/
│   ├── Podprojekt-A.md        # Pełny Project Canvas (ten szablon)
│   └── README.md
└── Podprojekt-B/
    ├── Podprojekt-B.md
    └── README.md
```

---

## Szablon: `Nazwa-podprojektu.md`

```markdown
# Project Canvas: [Nazwa Podprojektu]

**Projekt nadrzędny:** [[Nazwa-projektu-glownego]]
**Status:** 🟡 W analizie
**Powód statusu / Bloker:** [Jeśli 🟡 lub 🔴, wyjaśnij dlaczego]
**Ostatnia aktualizacja:** YYYY-MM-DD
**Klient:** [Nazwa klienta lub "AMODIT (roadmapa)"]

| Rola | Osoba | Odpowiedzialność |
|------|-------|------------------|
| **Tech Lead** | [Imię] / [do uzupełnienia] | Architektura tego podprojektu |
| **Deweloper** | [Imię] / [do uzupełnienia] | Implementacja |
| **Tester** | [Imię] / [do uzupełnienia] | |

---

## 1. PO CO TO ROBIMY? (Business Drivers)

### Problem
[Opisz problem biznesowy w 2-4 zdaniach. Musi być zrozumiały dla osoby spoza projektu.]

### Cel biznesowy
[Co chcemy osiągnąć z perspektywy biznesu - konkretnie]

### Cel techniczny
[Co chcemy osiągnąć z perspektywy technicznej]

### Metryka sukcesu
[Jak zmierzymy sukces - konkretne, mierzalne KPI]

---

## 2. USTALENIA ARCHITEKTONICZNE (Hard Constraints)

### Zasada 1: [Tytuł zasady]
[Opis zasady - co MUSI być spełnione]

**Uzasadnienie:** [Dlaczego ta zasada obowiązuje]

---

## Decyzje architektoniczne (ADR)

| ID | Status | Data | Decyzja | Uzasadnienie | Powód odrzucenia |
|----|--------|------|---------|--------------|------------------|
| ADR-001 | ✅ Zatwierdzone | [[YYYY-MM-DD]] | [Co zdecydowano] | [Dlaczego] | - |
| ADR-002 | ❌ Odrzucone | [[YYYY-MM-DD]] | [Co proponowano] | [Początkowe uzasadnienie] | [Dlaczego odrzucono] |

**Statusy ADR:**
- ✅ **Zatwierdzone** - decyzja ostateczna, implementowana
- 💡 **Propozycja** - do dyskusji, nie zatwierdzona
- 🔍 **Do weryfikacji** - wymaga dodatkowych testów/analiz
- ❌ **Odrzucone** - propozycja odrzucona (wypełnij "Powód odrzucenia")
- 🔄 **Wycofane** - decyzja była wdrożona, ale została cofnięta

---

## 3. FAZA PROJEKTU I RYZYKA

### Obecna faza: 📋 Analiza

**Ukończono:**
- ✅ [Co zostało zrobione]

**Trwa praca nad:**
- [Co obecnie robimy]

---

### Główne ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja | Właściciel |
|--------|-------------------|-------|-----------|------------|
| **[Wysokie]** [Opis ryzyka] | Średnie | Wysoki | [Mitygacja] | Tech Lead |

---

## 4. PACZKI DOSTARCZENIA (Roadmapa MVP)

### 📦 MVP1: "[Nazwa]" (Plan: Q4 2025)

**Cel:** [Dlaczego akurat taki zakres - jaką wartość dostarczamy użytkownikowi]

**Definicja ukończenia (DoD):**
- Użytkownik może [konkretne działanie - mierzalne]
- System [konkretne zachowanie - mierzalne]

**Funkcjonalności:**
- [ ] Funkcjonalność A
- [ ] Funkcjonalność B

**Poza zakresem MVP (Out of Scope):**
- [Co świadomie NIE robimy w tym MVP]

**Planowana data:** Q4 2025

---

### 📦 MVP2: "[Nazwa]" (Plan: Q1 2026)

**Cel:** [Co rozszerzamy - dlaczego]

**Funkcjonalności:**
- [ ] Funkcjonalność C
- [ ] Funkcjonalność D

**Planowana data:** Q1 2026

---

### 📦 Backlog (przyszłe wersje)

**Funkcjonalności odroczone:**
- Funkcjonalność X (Priorytet: Niski / Średni / Wysoki)

---

## 5. HISTORIA ZMIAN

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[YYYY-MM-DD]] | Utworzenie podprojektu | [[YYYY-MM-DD Rada architektów]] / [[YYYY-MM-DD Sprint review]] |

---

## 6. PRZYDATNE LINKI

- **Projekt nadrzędny:** [[Nazwa-projektu-glownego]]
- **Repozytorium:** [link]
- **Środowisko DEV:** [link]
- **Inicjatywa w backlogu:** [link do Azure DevOps]
```

---

## Szablon README.md dla podprojektu

```markdown
# [Nazwa Podprojektu]

**Projekt nadrzędny:** [[Nazwa-projektu-glownego]]
**Status:** 🟡 W analizie
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja

📄 **Project Canvas:** [[Nazwa-podprojektu]]

---

## Szybki przegląd

### Problem
[1-2 zdania]

### Rozwiązanie
[1-2 zdania]

### Obecna faza
📋 **W analizie** / 🛠 **MVP1** - w rozwoju

---

## MVP1: [Nazwa]

**Cel:** [Krótko]

**Zakres:**
- [ ] Element 1
- [ ] Element 2

---

## Szybkie linki

- Projekt nadrzędny: [[Nazwa-projektu-glownego]]
- Repozytorium: [link]
```

---

## Checklist przed commit

- [ ] Podprojekt ma link do projektu nadrzędnego
- [ ] Projekt nadrzędny ma wpis w sekcji "7. PODPROJEKTY"
- [ ] Nazwy katalogów i plików zgodne z konwencją
- [ ] README.md spójny z Project Canvas


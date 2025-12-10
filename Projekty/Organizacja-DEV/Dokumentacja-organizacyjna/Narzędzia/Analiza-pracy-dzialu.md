# Analiza pracy działu

**Kategoria:** Narzędzia
**Ostatnia aktualizacja:** [[2025-11-28]]

---

## Obecny stan

**Status:** 💡 Koncepcja do rozważenia

---

## Koncepcja

Integracja z Azure DevOps timesheet w celu analizy realizacji planów dnia i obciążenia zespołu.

### Źródła danych
- Eksport z Azure DevOps (timesheet wpisów daily)
- Format: tabela Markdown z kolumnami: Data, Pracownik, Klient, Project, tsaDescription, Godziny

### Rozpoznane wzorce

**Plan dnia:**
- Wpisy w projekcie "B+R AMODIT Prace koncepcyjne nad algorytmami w ramach metodyki SCRUM"
- To deklaracja co ktoś chce robić danego dnia

**Wykonanie:**
- Pozostałe wpisy — faktyczna praca
- Zawierają statusy: `Done:`, `Failed Internal test:`, `Pass Internal test:`, `Block waiting for information:`

**Wsparcie innych działów:**
- Wpisy z "wsparcie wdrożeń", "wsparcie sprzedaży", "konsultacje"
- Praca na rzecz innych działów, nie na projekty R&D

### Możliwe analizy

1. **Realizacja planów** — porównanie plan vs wykonanie
2. **Obciążenie zespołu** — godziny per osoba
3. **Rozkład pracy** — projekty vs wsparcie
4. **Blokery** — wpływ na realizację
5. **Trendy czasowe** — które projekty są aktywne

---

## Integracja techniczna

### Opcje

| Opcja | Zalety | Wady |
|-------|--------|------|
| MCP (Model Context Protocol) | Real-time, bezpośrednia integracja z Claude | Wymaga serwera MCP |
| Skrypt Python | Szybkie, generuje markdown | Wymaga uruchamiania ręcznego |
| az cli | Już skonfigurowane | Wymaga parsowania |

### Rekomendacja: Skrypt Python na start

```python
# azure_timesheet.py
# Pobiera dane z Azure DevOps i generuje markdown
# Uruchamiany tygodniowo/miesięcznie
```

---

## Gdzie trzymać dane?

### Propozycja: `Backlog/realizacja/`

Naturalne rozszerzenie cyklu backlogu:

```
Backlog/
├── strażnik/          # metodyka (CO chcemy zrobić)
└── realizacja/        # analiza (CZY zrobiliśmy)
    ├── timesheet/     # surowe dane
    └── statystyki/    # raporty
```

**Argumenty:**
- Plan → Realizacja → Retrospektywa to naturalny cykl
- Backlog już ma integrację z Azure DevOps
- Strażnik zyskuje kontekst do weryfikacji realizmu planów

---

## Mapowanie projektów Azure DevOps → nasze projekty

Nazwy projektów w Azure DevOps są pod "dotację" i nieczytelne.

**Przykłady mapowania:**

| Azure DevOps Project | Nasz Projekt |
|---------------------|--------------|
| roadmapa - wzrost atrakcyjności - ułatwienie konfiguracji procesów | `moduly/Edytor-procesow/Edytor-formularzy` |
| B+R roadmapa - opracowanie mechanizmów przyspieszających wdrożenia w oparciu o AI | `moduly/Copilot-Baza-wiedzy-AI` |
| B+R Roadmapa - Repozytorium plików | `klienci/WIM/Repozytorium` |
| wsparcie wdrożeń | `cross-cutting/Wsparcie-wdrozen` |

**Plik mapowania:** Do utworzenia gdy koncepcja zostanie zaakceptowana.

---

## Do rozstrzygnięcia

- [ ] Czy rozszerzamy `Backlog/` o folder `realizacja/`?
- [ ] Czy tworzymy skrypt Python do pobierania danych?
- [ ] Jaki zakres czasowy analizować (cały rok 2025)?
- [ ] Czy łączyć dane z timesheet z transkrypcjami Daily?
- [ ] Kto odpowiada za aktualizację mapowania projektów?

---

## Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| [[2025-11-28]] | Wstępna koncepcja | Rozmowa z Claude |

---

## Powiązane tematy

- [[Azure-DevOps]] – źródło danych
- [[2025-12-08 Daily]] – plan vs wykonanie
- [[Spotkania-cykliczne]] – kontekst spotkań


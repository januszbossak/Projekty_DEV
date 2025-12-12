#!/usr/bin/env python3
"""
Generator dashboardu projektów AMODIT R&D

Skanuje wszystkie projekty i tworzy agregowany widok statusów,
ostatnich zmian, ryzyk i postępów w MVP.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from collections import defaultdict

# Ścieżki
PROJEKTY_DIR = Path(__file__).parent.parent.parent / "Projekty"
OUTPUT_FILE = PROJEKTY_DIR / "DASHBOARD.md"

# Mapowanie statusów na emoji i nazwy
STATUS_MAP = {
    "produkcja": ("🟢", "Produkcja"),
    "w_trakcie": ("🟡", "W trakcie"),
    "planowanie": ("🔵", "Planowanie"),
    "wstrzymany": ("⏸️", "Wstrzymany"),
    "anulowany": ("❌", "Anulowany"),
    "koncepcja": ("💡", "Koncepcja"),
}

# Kategorie projektów
CATEGORIES = {
    "Moduly": "Moduły AMODIT",
    "Klienci": "Projekty klienckie",
    "cross-cutting": "Cross-cutting",
    "Organizacja-DEV": "Organizacja DEV",
    "Roadmapa-AMODIT": "Roadmapa",
}


class ProjectInfo:
    """Informacje o projekcie"""
    def __init__(self, path: Path, category: str):
        self.path = path
        self.category = category
        self.name = path.stem if path.stem != "PROJEKT" else path.parent.name
        self.status = "nieznany"
        self.last_updated = None
        self.last_changelog_entry = None
        self.last_changelog_date = None
        self.team_pdm = None
        self.team_tech_lead = None
        self.projekt_exists = False
        self.changelog_exists = False

        self._parse_projekt()
        self._parse_changelog()

    def _parse_projekt(self):
        """Parsuje PROJEKT.md lub Nazwa-projektu.md"""
        # Spróbuj znaleźć plik projektu
        projekt_file = None
        if self.path.name == "PROJEKT.md":
            projekt_file = self.path
        else:
            # Stara konwencja - plik już w self.path
            projekt_file = self.path

        if not projekt_file.exists():
            return

        self.projekt_exists = True
        content = projekt_file.read_text(encoding='utf-8')

        # Frontmatter YAML
        yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.MULTILINE | re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)

            # Status
            status_match = re.search(r'status:\s*(.+)', yaml_content)
            if status_match:
                self.status = status_match.group(1).strip()

            # Last updated
            updated_match = re.search(r'last_updated:\s*(\d{4}-\d{2}-\d{2})', yaml_content)
            if updated_match:
                self.last_updated = updated_match.group(1)

        # Status z treści (jeśli nie ma w YAML)
        if self.status == "nieznany":
            status_match = re.search(r'> \*\*Status:\*\* [🟢🟡🔵⏸️❌💡] (.+)', content)
            if status_match:
                status_text = status_match.group(1).lower()
                if "produkcja" in status_text:
                    self.status = "produkcja"
                elif "w trakcie" in status_text or "w_trakcie" in status_text:
                    self.status = "w_trakcie"
                elif "planowanie" in status_text:
                    self.status = "planowanie"
                elif "wstrzymany" in status_text:
                    self.status = "wstrzymany"

        # Zespół
        pdm_match = re.search(r'\*\*PDM:\*\*\s*(.+)', content)
        if pdm_match:
            self.team_pdm = pdm_match.group(1).strip()

        tech_lead_match = re.search(r'\*\*Tech Lead:\*\*\s*(.+)', content)
        if tech_lead_match:
            self.team_tech_lead = tech_lead_match.group(1).strip()

    def _parse_changelog(self):
        """Parsuje CHANGELOG.md dla ostatniego wpisu"""
        changelog_file = self.path.parent / "CHANGELOG.md"
        if not changelog_file.exists():
            return

        self.changelog_exists = True
        content = changelog_file.read_text(encoding='utf-8')

        # Znajdź pierwszy wpis (## YYYY-MM-DD)
        entries = re.findall(r'^## (\d{4}-\d{2}-\d{2}) \| (.+?)$\n(.*?)(?=^##|\Z)',
                            content, re.MULTILINE | re.DOTALL)

        if entries:
            # Sortuj po dacie malejąco
            entries_sorted = sorted(entries, key=lambda x: x[0], reverse=True)
            latest = entries_sorted[0]

            self.last_changelog_date = latest[0]
            meeting_type = latest[1]
            entry_content = latest[2]

            # Wyciągnij pierwsze 2-3 linie treści (bez nagłówków)
            lines = [line.strip() for line in entry_content.split('\n')
                    if line.strip() and not line.strip().startswith('**')
                    and not line.strip().startswith('#')]

            summary = ' '.join(lines[:2])[:200]
            if len(summary) >= 200:
                summary += "..."

            self.last_changelog_entry = f"{meeting_type}: {summary}"


def find_all_projects() -> List[ProjectInfo]:
    """Znajduje wszystkie projekty"""
    projects = []
    seen_paths = set()  # Unikaj duplikatów

    for category in CATEGORIES.keys():
        category_path = PROJEKTY_DIR / category
        if not category_path.exists():
            continue

        # Szukaj plików PROJEKT.md (nowa konwencja)
        for projekt_file in category_path.rglob("PROJEKT.md"):
            if projekt_file.parent not in seen_paths:
                project = ProjectInfo(projekt_file, category)
                projects.append(project)
                seen_paths.add(projekt_file.parent)

        # Szukaj plików Nazwa-projektu.md (stara konwencja)
        # Wyklucz: README, CHANGELOG, ARCHITEKTURA, ROADMAPA, OLD, SZABLON
        for md_file in category_path.rglob("*.md"):
            # Pomiń specjalne pliki
            if md_file.name in ['README.md', 'CHANGELOG.md', 'ARCHITEKTURA.md',
                                'ROADMAPA.md', 'PROJEKT.md', 'DASHBOARD.md']:
                continue

            # Pomiń pliki OLD i SZABLON
            if 'OLD' in md_file.name or 'SZABLON' in md_file.name:
                continue

            # Sprawdź czy to główny plik projektu (nazwa pliku == nazwa folderu)
            if md_file.stem == md_file.parent.name and md_file.parent not in seen_paths:
                project = ProjectInfo(md_file, category)
                projects.append(project)
                seen_paths.add(md_file.parent)

    return projects


def generate_summary_stats(projects: List[ProjectInfo]) -> Dict:
    """Generuje statystyki podsumowujące"""
    stats = {
        'total': len(projects),
        'by_status': defaultdict(int),
        'by_category': defaultdict(int),
        'with_changelog': 0,
        'updated_last_7_days': 0,
        'updated_last_30_days': 0,
    }

    today = datetime.now()

    for p in projects:
        stats['by_status'][p.status] += 1
        stats['by_category'][p.category] += 1

        if p.changelog_exists:
            stats['with_changelog'] += 1

        if p.last_changelog_date:
            last_change = datetime.strptime(p.last_changelog_date, '%Y-%m-%d')
            days_ago = (today - last_change).days

            if days_ago <= 7:
                stats['updated_last_7_days'] += 1
            if days_ago <= 30:
                stats['updated_last_30_days'] += 1

    return stats


def generate_dashboard(projects: List[ProjectInfo], stats: Dict) -> str:
    """Generuje treść dashboardu w Markdown"""

    today = datetime.now().strftime('%Y-%m-%d %H:%M')

    md = f"""---
generated: {today}
projects_count: {stats['total']}
---

# 📊 Dashboard Projektów R&D AMODIT

> **Ostatnia aktualizacja:** {today}
> **Projektów w bazie:** {stats['total']}

---

## 📈 Statystyki podsumowujące

### Status projektów

| Status | Liczba | % |
|--------|--------|---|
"""

    # Statystyki statusów
    for status_key in ['produkcja', 'w_trakcie', 'planowanie', 'wstrzymany', 'koncepcja', 'nieznany']:
        count = stats['by_status'].get(status_key, 0)
        if count > 0:
            emoji, label = STATUS_MAP.get(status_key, ("❓", status_key))
            percent = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            md += f"| {emoji} {label} | {count} | {percent:.1f}% |\n"

    md += f"""
### Aktywność

- 📅 **Zaktualizowane w ostatnim tygodniu:** {stats['updated_last_7_days']}
- 📅 **Zaktualizowane w ostatnim miesiącu:** {stats['updated_last_30_days']}
- 📝 **Projekty z CHANGELOG:** {stats['with_changelog']} / {stats['total']}

### Rozkład po kategoriach

| Kategoria | Liczba |
|-----------|--------|
"""

    for cat_key, cat_label in CATEGORIES.items():
        count = stats['by_category'].get(cat_key, 0)
        if count > 0:
            md += f"| {cat_label} | {count} |\n"

    md += "\n---\n\n"

    # Tabela wszystkich projektów
    md += """## 📋 Wszystkie projekty

| Projekt | Status | Kategoria | PDM | Ostatnia zmiana | Ostatni wpis |
|---------|--------|-----------|-----|-----------------|--------------|
"""

    # Sortuj projekty: najpierw po statusie (produkcja, w_trakcie...), potem po dacie ostatniej zmiany
    status_priority = {
        'produkcja': 1,
        'w_trakcie': 2,
        'planowanie': 3,
        'koncepcja': 4,
        'wstrzymany': 5,
        'anulowany': 6,
        'nieznany': 7,
    }

    projects_sorted = sorted(
        projects,
        key=lambda p: (
            status_priority.get(p.status, 99),
            -(datetime.strptime(p.last_changelog_date, '%Y-%m-%d').timestamp()
              if p.last_changelog_date else 0)
        )
    )

    for p in projects_sorted:
        emoji, status_label = STATUS_MAP.get(p.status, ("❓", p.status))

        # Link do projektu (Obsidian)
        project_link = f"[[{p.name}]]"

        # Status
        status_display = f"{emoji} {status_label}"

        # Kategoria
        category_display = CATEGORIES.get(p.category, p.category)

        # PDM
        pdm_display = p.team_pdm if p.team_pdm else "-"

        # Ostatnia zmiana
        last_change = p.last_changelog_date if p.last_changelog_date else "brak"

        # Ostatni wpis (skrócony)
        last_entry = p.last_changelog_entry[:80] + "..." if p.last_changelog_entry and len(p.last_changelog_entry) > 80 else (p.last_changelog_entry or "brak")

        md += f"| {project_link} | {status_display} | {category_display} | {pdm_display} | {last_change} | {last_entry} |\n"

    md += "\n---\n\n"

    # Projekty wymagające uwagi
    md += """## ⚠️ Projekty wymagające uwagi

### Brak aktualizacji >30 dni

| Projekt | Status | Ostatnia zmiana | Dni bez zmian |
|---------|--------|-----------------|---------------|
"""

    today = datetime.now()
    stale_projects = []

    for p in projects:
        if not p.last_changelog_date:
            continue

        last_change = datetime.strptime(p.last_changelog_date, '%Y-%m-%d')
        days_ago = (today - last_change).days

        if days_ago > 30 and p.status not in ['wstrzymany', 'anulowany']:
            stale_projects.append((p, days_ago))

    stale_projects.sort(key=lambda x: x[1], reverse=True)

    if stale_projects:
        for p, days in stale_projects:
            emoji, status_label = STATUS_MAP.get(p.status, ("❓", p.status))
            md += f"| [[{p.name}]] | {emoji} {status_label} | {p.last_changelog_date} | {days} dni |\n"
    else:
        md += "| - | - | - | Wszystkie projekty aktualne |\n"

    md += "\n### Projekty bez CHANGELOG\n\n"

    no_changelog = [p for p in projects if not p.changelog_exists]
    if no_changelog:
        for p in no_changelog:
            emoji, status_label = STATUS_MAP.get(p.status, ("❓", p.status))
            md += f"- [[{p.name}]] ({emoji} {status_label})\n"
    else:
        md += "Wszystkie projekty mają CHANGELOG 🎉\n"

    md += "\n---\n\n"

    # Podsumowanie po kategoriach
    md += "## 📂 Projekty po kategoriach\n\n"

    projects_by_cat = defaultdict(list)
    for p in projects:
        projects_by_cat[p.category].append(p)

    for cat_key, cat_label in CATEGORIES.items():
        cat_projects = projects_by_cat.get(cat_key, [])
        if not cat_projects:
            continue

        md += f"### {cat_label} ({len(cat_projects)})\n\n"

        # Sortuj po statusie
        cat_projects_sorted = sorted(
            cat_projects,
            key=lambda p: status_priority.get(p.status, 99)
        )

        for p in cat_projects_sorted:
            emoji, status_label = STATUS_MAP.get(p.status, ("❓", p.status))
            last_change = p.last_changelog_date if p.last_changelog_date else "brak zmian"
            md += f"- {emoji} [[{p.name}]] - {last_change}\n"

        md += "\n"

    md += """---

## 📖 Legenda

### Statusy projektów

- 🟢 **Produkcja** - wydane, w użyciu
- 🟡 **W trakcie** - aktywna realizacja
- 🔵 **Planowanie** - w fazie planowania
- 💡 **Koncepcja** - pomysł, proof-of-concept
- ⏸️ **Wstrzymany** - tymczasowo wstrzymany
- ❌ **Anulowany** - zaniechany
- ❓ **Nieznany** - brak informacji o statusie

### Jak korzystać z dashboardu

1. **Przegląd ogólny:** Sekcja "Statystyki podsumowujące" pokazuje stan wszystkich projektów
2. **Wszystkie projekty:** Tabela z pełną listą i linkami do Project Canvas
3. **Projekty wymagające uwagi:** Automatycznie wykryte projekty do przeglądu
4. **Po kategoriach:** Widok pogrupowany dla łatwiejszej nawigacji

### Automatyczna aktualizacja

Dashboard jest generowany automatycznie przez skrypt:
```bash
python .claude/scripts/generate_dashboard.py
```

Lub przez agenta:
```
> Wygeneruj dashboard projektów
```

---

*Wygenerowano automatycznie przez `.claude/scripts/generate_dashboard.py`*
"""

    return md


def main():
    """Główna funkcja"""
    print("🔍 Szukam projektów...")
    projects = find_all_projects()
    print(f"   Znaleziono {len(projects)} projektów")

    print("📊 Generuję statystyki...")
    stats = generate_summary_stats(projects)

    print("📝 Tworzę dashboard...")
    dashboard_content = generate_dashboard(projects, stats)

    print(f"💾 Zapisuję do {OUTPUT_FILE}...")
    OUTPUT_FILE.write_text(dashboard_content, encoding='utf-8')

    print(f"✅ Dashboard wygenerowany: {OUTPUT_FILE}")
    print(f"\n📊 Podsumowanie:")
    print(f"   - Projektów: {stats['total']}")
    print(f"   - W produkcji: {stats['by_status']['produkcja']}")
    print(f"   - W trakcie: {stats['by_status']['w_trakcie']}")
    print(f"   - Zaktualizowanych w ostatnim tygodniu: {stats['updated_last_7_days']}")


if __name__ == "__main__":
    main()

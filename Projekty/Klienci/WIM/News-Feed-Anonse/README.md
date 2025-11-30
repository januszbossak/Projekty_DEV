# News Feed i Anonse

**Klient:** WIM
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Tech Lead:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[News-Feed-Anonse]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR)
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Klient WIM potrzebuje mechanizmu wyświetlania ogłoszeń (np. o awariach, zmianach) oraz newsów (np. z bloga amodit.pl) w interfejsie systemu.

### Rozwiązanie

Realizacja funkcjonalności w oparciu o procesy AMODIT (low-code):
- Ogłoszenia jako sprawy w procesie "Anonse"
- Mechanizm News Feed pobiera dane z procesu lub zewnętrznego źródła
- Uproszczony interfejs wyświetlania (bez formularza, historii)

### Obecna faza

🛠️ **W realizacji** - konfiguracja procesu i implementacja mechanizmu wyświetlania

**Ukończono:**
- ✅ Decyzja architektoniczna o realizacji na procesach AMODIT
- ✅ Odrzucenie alternatywnych rozwiązań

**W trakcie:**
- Konfiguracja procesu "Anonse"
- Implementacja mechanizmu wyświetlania (News Feed)

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Realizacja na procesach AMODIT** | Najszybsza implementacja (konfiguracja, nie kod), elastyczność uprawnień |
| **Odrzucenie dedykowanego modułu** | Zbyt duży narzut pracy deweloperskiej |
| **Odrzucenie ChromaDB** | Brak dostępu "od ręki", konieczność integracji, overkill dla prostych ogłoszeń |

---

## MVP1: Anonse i News Feed na procesach

**Cel:** Uruchomienie funkcjonalności wyświetlania ogłoszeń i newsów wykorzystując procesy AMODIT

**Zakres:**
- [ ] Konfiguracja procesu "Anonse"
- [ ] Mechanizm News Feed z uprawnieniami
- [ ] Uproszczony interfejs wyświetlania
- [ ] Integracja z zewnętrznymi źródłami (blog)

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Klient może negować podejście oparte na procesach | Przedstawienie korzyści low-code oraz możliwość ewolucji |

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Backlog: [do uzupełnienia]


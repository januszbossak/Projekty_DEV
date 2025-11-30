# Zastępstwa w grupach

**Klient:** AMODIT (roadmapa)
**Status:** 🟢 W realizacji
**PDM:** [do uzupełnienia]
**Deweloper:** Piotr Buczkowski
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Zastepstwa-grupy]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR) - obsługa grup jednoosobowych, parametr dla wieloosobowych
- Roadmapa MVP
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

Niespójność między starym a nowym mechanizmem zastępstw - w starym zastępca widzi sprawy przypisane do grup osoby zastępowanej, w nowym nie. Niespójność prowadzi do błędów logicznych i problemów wydajnościowych.

### Rozwiązanie

Ujednolicenie działania mechanizmów zastępstw dla grup:
- Obsługa zastępstw za grupy jednoosobowe domyślnie (gdzie grupa = rola)
- Parametr "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych
- Docelowo oba mechanizmy działają tak samo

### Obecna faza

🛠️ **W realizacji** - implementacja obsługi grup jednoosobowych i parametru

**Ukończono:**
- ✅ Ustalenie architektury i podejścia technicznego

**W trakcie:**
- Dodanie obsługi zastępstw za grupy jednoosobowe
- Dodanie parametru dla grup wieloosobowych

---

## Kluczowe decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Obsługa grup jednoosobowych domyślnie** | Najbardziej sensowny przypadek użycia - grupy definiujące role wymagają zastępstw |
| **Parametr dla grup wieloosobowych** | Elastyczne rozwiązanie - pozwala na jawne włączenie mechanizmu dla dowolnej grupy |

---

## MVP1: Grupy jednoosobowe + konfiguracja

**Cel:** Ujednolicić działanie zastępstw i dać administratorom kontrolę nad mechanizmem

**Zakres:**
- [ ] Automatyczna obsługa zastępstw dla grup jednoosobowych
- [ ] Parametr "Uwzględnij zastępstwa dla tej grupy" dla grup wieloosobowych
- [ ] Ujednolicenie logiki starego i nowego mechanizmu

**Planowana data:** [do uzupełnienia]

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]

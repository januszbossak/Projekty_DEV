# CHANGELOG - WCAG (WIM)

## 2025-10-02 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-10-02 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-10-02%20Rada%20architektów.md)
**Kategoria:** #Design #Bug

- Zidentyfikowano krytyczne problemy z kontrastem w wizualizacjach raportów systemowych (nieczytelny szary tekst)
- Decyzja o konieczności ujednolicenia kolorów tooltipów (czarny/biały) niezależnie od tła kafelka

---

## 2025-08-26 - Notatka projektowa - AMODIT UI

**Źródło:** [[../../../../Notatki/Gotowe-notatki-archiwum/2025-08-26 Notatka projektowa - AMODIT UI|2025-08-26 AMODIT UI]]

**Kategoria:** #Dostępność #Funkcjonalność

**Kontekst biznesowy:**
Projekt realizowany głównie pod wymagania WIM jako priorytet biznesowy. Zapewnienie zgodności z normami dostępności WCAG 2.1 AA oraz umożliwienie korzystania z systemu osobom z niepełnosprawnościami.

### Dwie perspektywy dostępności

**1. Tryb wysokiego kontrastu:**
- Wyczernienie kluczowych treści (przyciski, podtytuły)
- Obramowanie elementów przy najeżdżaniu (zamiast słabo widocznego podświetlenia)
- Działa na ekranie głównym i na sprawie
- Opcja włączana w ustawieniach konta

**2. Tryb uproszczonego widoku sprawy:**
- Zmieniona nawigacja
- Ważny dla osób korzystających z czytników ekranowych (VoiceOver itp.)
- Żeby czytnik mógł opowiedzieć, co jest na ekranie, widok musi być prosty

### Deklaracja zgodności

- Do tej wersji zostanie wydana deklaracja zgodności ze standardem WCAG 2.1 AA

### Nawigacja klawiaturą

- Poruszanie się po ekranie zostało dostosowane do norm
- Nawigacja klawiaturą (Tab, Shift+Tab, strzałki) zamiast myszki, pozwalająca na pełne procesowanie formularza

### Szczegóły techniczne

- Opcja włączana na poziomie użytkownika (każdy może sobie włączyć taki tryb, a pozostali mogą korzystać z normalnego wyglądu)
- Standard: WCAG 2.1 AA


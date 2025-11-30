# Surowe pliki wejściowe

Ten folder zawiera pliki przed przetworzeniem przez pipeline.

**⚠️ UWAGA:** Po oczyszczeniu transkrypcji, surowy plik jest automatycznie przenoszony do `surowe - archiwum/`.

## Typy plików

### 1. Transkrypcje (wymagają czyszczenia)
- **Lokalizacja:** Bezpośrednio w `surowe/`
- **Format:** Surowa transkrypcja z błędami ASR, znacznikami czasu, dialogiem wielu osób
- **Przetwarzanie:** Czyszczenie → Generowanie notatki
- **Przykłady:**
  - `2025-11-28 Rada architektów.md`
  - `2025-11-28 Planowanie sprintu.md`

### 2. Gotowe notatki (pomijają czyszczenie)
- **Lokalizacja:** `surowe/notatki/` lub `surowe/` z oznaczeniem w nazwie
- **Format:** Gotowa notatka, dokument, opracowanie (np. artykuł z wiki)
- **Przetwarzanie:** Tylko generowanie notatki (pomija czyszczenie)
- **Przykłady:**
  - `surowe/notatki/2025-11-28 Opis e-doręczeń - dokument.md`
  - `surowe/2025-11-28 Wyjaśnienie Daily - notatka.md`
  - `surowe/notatki/2025-11-28 Artykuł z wiki DevOps.md`

**Uwaga:** Swobodne wypowiedzi/monologi traktujemy jak transkrypcje (podlegają czyszczeniu).

## Wyciąganie daty

**Dla transkrypcji:**
- Data z nazwy pliku: `YYYY-MM-DD` na początku
- Lub z rejestru `_transkrypcje.md`

**Dla gotowych notatek:**
- Data z nazwy pliku: `YYYY-MM-DD` na początku
- Lub z zawartości pliku (szukaj wzorca `YYYY-MM-DD` lub `RRRR-MM-DD`)
- Lub z metadanych na początku pliku (`**Data:** YYYY-MM-DD`)
- **Jeśli brak → użyj dzisiejszej daty**

## Rozpoznawanie typu

Pipeline automatycznie rozpoznaje typ pliku na podstawie:
- Lokalizacji (folder `notatki/` = gotowa notatka)
- Nazwy (zawiera `- notatka.md`, `- dokument.md`, `- opracowanie.md` = gotowa notatka)
- Zawartości (brak formatu transkrypcji = gotowa notatka)


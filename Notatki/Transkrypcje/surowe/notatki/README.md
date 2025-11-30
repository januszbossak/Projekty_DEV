# Gotowe notatki i dokumenty

Ten folder zawiera gotowe notatki, dokumenty i opracowania, które **NIE wymagają czyszczenia** i trafiają od razu do generowania notatek strukturalnych.

## Typy plików

### 1. Swobodne wypowiedzi/monologi
- **Format:** Jedna osoba pisze notatkę, wyjaśnienie, doprecyzowanie
- **Przetwarzanie:** Podlega czyszczeniu (jak transkrypcja)
- **Lokalizacja:** `surowe/` (nie w folderze `notatki/`)

### 2. Gotowe dokumenty/opracowania
- **Format:** Gotowa notatka, dokument, opracowanie (np. artykuł z wiki technicznego)
- **Przetwarzanie:** Pomija czyszczenie, od razu generuje notatkę strukturalną
- **Lokalizacja:** `surowe/notatki/` lub `surowe/` z oznaczeniem w nazwie

## Przykłady

### Gotowe dokumenty (w `notatki/`):
- `2025-11-28 Opis e-doręczeń - dokument.md` (artykuł z wiki DevOps)
- `2025-11-28 Standardy code review - opracowanie.md`
- `2025-11-28 Proces onboarding - dokument.md`

### Swobodne wypowiedzi (w `surowe/`):
- `2025-11-28 Wyjaśnienie Daily.md` (monolog, podlega czyszczeniu)
- `2025-11-28 Doprecyzowanie procesu.md` (monolog, podlega czyszczeniu)

## Wyciąganie daty

**Priorytet:**
1. Data z nazwy pliku: `YYYY-MM-DD` na początku
2. Data z zawartości pliku (szukaj wzorca `YYYY-MM-DD` lub `RRRR-MM-DD`)
3. Data z metadanych na początku pliku (`**Data:** YYYY-MM-DD`)
4. **Jeśli brak → użyj dzisiejszej daty**

## Rozpoznawanie typu spotkania

Pipeline rozpoznaje typ spotkania z:
- Nazwy pliku
- Zawartości pliku
- Metadanych na początku pliku

Jeśli nie można rozpoznać → domyślnie `organizacyjne`


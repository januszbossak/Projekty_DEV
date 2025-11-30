---
description: Wykonaj backup repozytorium na GitHub
---

Wykonaj pełny backup repozytorium na GitHub:

1. **Dodaj wszystkie zmiany:**
   ```bash
   git add .
   ```

2. **Sprawdź co się zmieniło:**
   ```bash
   git status --short
   ```

3. **Utwórz commit z opisem:**
   - Przeanalizuj zmiany (git status)
   - Stwórz zwięzły opis (1-2 zdania) co się zmieniło
   - Użyj formatu:
   ```bash
   git commit -m "$(cat <<'EOF'
   Backup [YYYY-MM-DD HH:MM] - [Krótki opis zmian]

   Zmiany:
   - [główna zmiana 1]
   - [główna zmiana 2]

   🤖 Generated with Claude Code
   EOF
   )"
   ```

4. **Wypchnij na GitHub:**
   ```bash
   git push origin main
   ```

5. **Raportuj sukces:**
   ```
   ✅ Backup zakończony!

   📊 Zmiany:
   - Plików zmienionych: X
   - Commit: [hash]
   - GitHub: https://github.com/januszbossak/Projekty_DEV
   ```

**WAŻNE:**
- ZAWSZE wykonuj wszystkie kroki sekwencyjnie
- Użyj `git add .` przed commitem
- Format daty: `YYYY-MM-DD HH:MM` (np. `2025-11-30 15:30`)
- Opis zmian powinien być konkretny i zwięzły
- NIE pytaj o potwierdzenie - wykonaj automatycznie

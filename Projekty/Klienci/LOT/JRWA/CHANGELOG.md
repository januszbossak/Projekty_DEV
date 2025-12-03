# CHANGELOG – JRWA (LOT)

---

## 2025-12-03 | Spotkanie projektowe
**Źródło:** [Notatki/Spotkania projektowe/2025-12-03 Notatka projektowa - Historia biznesowa.md](../../../../Notatki/Spotkania%20projektowe/2025-12-03%20Notatka%20projektowa%20-%20Historia%20biznesowa.md)
**Kategoria:** 💡 Koncepcja

- **Historia przypinania/odpinania dokumentów do teczek** – każde przypięcie/odpięcie generuje zdarzenie w historii biznesowej z `BusinessSubjectType = 'jrwa_folder'`.
- **Widok historii teczki JRWA** – filtrowany widok zdarzeń biznesowych (SQL: `WHERE BusinessSubjectType = 'jrwa_folder' AND BusinessSubjectID = <ID teczki>`). Pokazuje kto, kiedy i dlaczego przypięto/odpięto dokument.
- **EventType słownikowy** – administrator definiuje zdarzenia "Przypięcie do teczki JRWA" i "Odpięcie z teczki JRWA" w słowniku zdarzeń biznesowych.
- **Pole linked w message** – opcjonalnie można wrzucić link HTML do dokumentu/sprawy dla wygody użytkownika.
- **Brak automatycznej migracji starych danych** – tylko nowe operacje po wdrożeniu będą generować zdarzenia (poza zakresem MVP).

---

# CHANGELOG - Historia aktywności uprawnień

---

## 2025-09-04 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-09-04 Rada architektów.md](../../../../Notatki/Gotowe-notatki-archiwum/2025-09-04%20Rada%20architektów.md)
**Kategoria:** #Architektura #Decyzja

**Uwzględnienie ustawienia "administrator nie ma praw" w historii** ✅
- **Problem:** Historia uprawnień pokazywała dostęp admina, mimo że proces miał ustawione "admin nie ma praw"
- Powodowało to dezinformację użytkowników
- ✅ **Zatwierdzone:** Uwzględnienie tego ustawienia przy generowaniu historii uprawnień

**Zdarzenie "edycja sprawy" w CaseActivity** 🔍
- **Problem:** Zdarzenie loguje się zawsze, ale nie jest wyświetlane
- 🔍 **Do weryfikacji:** Czy służy do migawek historii uprawnień?
- Piotr sprawdzi powiązania. Jeśli potrzebne - rozważyć uproszczone wyświetlanie.

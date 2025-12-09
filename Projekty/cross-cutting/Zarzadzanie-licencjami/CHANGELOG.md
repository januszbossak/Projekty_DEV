# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-11-27 | Notatka projektowa
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-27 Notatka projektowa - Integracja z KSeF Connectorem.md]
**Kategoria:** #Decyzja

- Endpoint KSeF Connectora nie będzie podlegał licencjonowaniu.

---

## 2025-11-25 | Rada architektów
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-11-25 Rada architektów.md](../../../Notatki/Gotowe-notatki-archiwum/2025-11-25%20Rada%20architektów.md)
**Kategoria:** #Architektura #Błędy

- **Mechanizm licencjonowania:** Działa identycznie dla kont ręcznych i z AD. Limit dotyczy aktywnych kont mogących się zalogować. Kontrola przy próbie logowania.
- **Blokada kont:** Przekroczenie limitu blokuje konta w pamięci (nie w bazie). Wymaga ręcznej interwencji admina (zablokowanie innego konta) do zwolnienia slotu.
- **Rossmann (Bug):** Błąd "osiągnięto limit spraw" wynika ze znikania obiektu licencji z pamięci usługi (prawdopodobnie problem sieciowy lub bazy danych przy odświeżaniu).

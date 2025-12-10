# CHANGELOG

Historia ustaleń i zmian dla projektu.

---

## 2025-12-02 | Rada developerów
**Źródło:** [Notatki/Gotowe-notatki-w-trakcie/2025-12-02 Rada developerów.md]
**Kategoria:** #Architektura

- **Rate limiting dla REST API:** Propozycja limitów godzinnych, minutowych, dziennych z mechanizmem HTTP 429 (przekroczony limit)
- **Model licencyjny z progami:** 10 000 lub milion zapytań miesięcznie w podstawowej licencji, więcej = wyższa licencja
- **Wzór rynkowy:** 1000 zł → 15 000 zł za większą skalę zapytań
- **Wymagana analiza:** Lista klientów wykorzystujących REST API do masowych połączeń, wolumen zapytań, skrajne przypadki
- **Monitoring:** Azure Monitor do badania ruchu wchodzącego i wychodzącego
- **Ryzyko:** Negatywny odbiór przez klientów już korzystających z API bez ograniczeń

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

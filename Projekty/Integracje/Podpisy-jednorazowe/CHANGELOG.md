# CHANGELOG - Podpisy jednorazowe (SIGNIUS)

Historia ustaleń i zmian dla integracji z SIGNIUS/EuroCert.

---

## 2025-12-22 | Nowa metoda identyfikacji – AutoIdent
**Źródło:** [Notatki/Gotowe-notatki-archiwum/2025-12-22 Autoindentyfikacja SIGNIUS.md](../../../Notatki/Gotowe-notatki-archiwum/2025-12-22%20Autoindentyfikacja%20SIGNIUS.md)
**Kategoria:** #Funkcjonalność #Wydanie

- **Wprowadzenie AutoIdent IDnow:** Nowa metoda samodzielnej weryfikacji tożsamości na platformie SIGNIUS. Nie wymaga rozmowy z konsultantem.
- **Wycofanie Nect:** Metoda *Nect Selfie Ident* będzie dostępna wyłącznie do 28.02.2026. Po tym terminie standardem pozostaje AutoIdent.
- **Materiały:** [Film prezentujący proces AutoIdent](https://youtu.be/f9TTnxnTIcU).

---

## 2025-06-18 | Dokumentacja techniczna i organizacyjna integracji
**Kategoria:** #Architektura #Konfiguracja

- **Wymagania systemowe:** 
  - Wymagana flaga `AllowOneTimeCertificateSignature` w tabeli `Organization` (dostęp tylko od strony bazy danych Trust Center).
  - Wymagane ustawienie `AllowOneTimeCertificateSignature = true` w funkcjach reguł `TrustCenterSendToSign` / `Ex`.
- **Wymagania dla podpisującego:**
  - Dokument tożsamości (Dowód/Paszport).
  - Nect Wallet: iOS 10.3+ lub Android 6.0+.
  - Weryfikacja z operatorem: kamera i mikrofon.
- **Architektura tożsamości:**
  - Tożsamość przechowywana w TC oraz u dostawcy Signius (tabela `signiusdata`).
  - Proces: Rejestracja → Weryfikacja → Callback statusu.
- **Mechanizm podpisywania:**
  - Wykorzystanie Harmony API (Token + ID operacji).
  - Wystawianie 15-minutowego certyfikatu.
  - Podpisywanie hashu dokumentu wewnątrz TC za pośrednictwem Signius.
- **Ponowne podpisywanie:** Użytkownik zweryfikowany może pominąć kroki identyfikacji przy kolejnych dokumentach.
- **Usuwanie tożsamości:** Procedura usuwania wpisu z bazy TC oraz wywołanie endpointu usuwającego w Signius w przypadku błędów.

---

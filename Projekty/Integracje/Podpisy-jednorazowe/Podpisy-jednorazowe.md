# Projekt: Podpisy jednorazowe (SIGNIUS / EuroCert)

## Status
- **Faza:** Stabilizacja / Utrzymanie
- **Opiekun:** [Do uzupełnienia]
- **Partnerzy:** SIGNIUS, EuroCert

## Opis projektu
Integracja systemu AMODIT z systemem podpisów jednorazowych oferowanych przez SIGNIUS we współpracy z EuroCert. Funkcjonalność umożliwia wystawienie 15-minutowego certyfikatu kwalifikowanego na potrzeby podpisania konkretnego dokumentu, po uprzedniej weryfikacji tożsamości użytkownika.

## Kluczowe Funkcjonalności
- **Weryfikacja tożsamości:** 
  - **AutoIdent IDnow** (samodzielna, bez konsultanta).
  - **Nect Selfie Ident** (wycofywane do 28.02.2026).
  - Weryfikacja z operatorem (rozmowa wideo).
- **Certyfikaty jednorazowe:** Wystawianie certyfikatów o krótkim czasie ważności (15 min) przez Harmony API Signius.
- **Integracja z Trust Center:** Zarządzanie procesem podpisywania i tożsamościami użytkowników.

## Wymagania techniczne
- **Baza Trust Center:** Flaga `AllowOneTimeCertificateSignature` w tabeli `Organization`.
- **Reguły AMODIT:** Opcja `AllowOneTimeCertificateSignature` w funkcjach `TrustCenterSendToSign` / `TrustCenterSendToSignEx`.
- **API:** Harmony API Signius.

## Proces biznesowy
1. **Przygotowanie:** Ustawienie flagi dopuszczającej podpisy jednorazowe w procesie.
2. **Rejestracja/Identyfikacja:** Utworzenie tożsamości w Signius i weryfikacja (AutoIdent/Nect/Operator).
3. **Weryfikacja:** Powrót statusu weryfikacji na adres callback TC.
4. **Podpis:** Logowanie do Harmony API, wystawienie certyfikatu, podpisanie hashu dokumentu.

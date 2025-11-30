# Komunikator (AMODIT Talk)

**Klient:** WIM
**Status:** 🟡 W analizie
**PDM:** [do uzupełnienia]
**Format:** v2 (Project Canvas 2025-11)

---

## Dokumentacja projektu

📄 **Project Canvas:** [[Komunikator]]

Pełna dokumentacja projektu obejmująca:
- Kontekst biznesowy i cele (PO CO TO ROBIMY)
- Decyzje architektoniczne (ADR) - SignalR, JWT/OTP, model bazy
- Roadmapa MVP (On-Premises, Cloud/SaaS)
- Ryzyka i mitygacja
- Historia zmian

---

## Szybki przegląd

### Problem

AMODIT nie posiada wbudowanego modułu komunikacji wewnętrznej. Użytkownicy muszą korzystać z zewnętrznych narzędzi do szybkiej wymiany informacji w kontekście spraw i procesów, co fragmentuje komunikację i utrudnia śledzenie historii ustaleń.

### Rozwiązanie

Zintegrowany komunikator (AMODIT Talk) jako osobna aplikacja SignalR:
- Konwersacje prywatne i grupowe
- Wzmiankowanie użytkowników (@)
- Szyfrowanie wiadomości
- Obsługa On-Premises i Cloud (SaaS)
- Komunikator nie jest promowany jako osobny produkt – jest funkcjonalnością AMODIT

### Obecna faza

📋 **W analizie** - projekt został zaimplementowany bez wcześniejszej akceptacji architektonicznej. Wymaga dopracowania zgodności z filozofią AMODIT (on-premises vs chmura) przed kontynuacją prac.

**Ukończono:**
- ✅ Implementacja podstawowa komunikatora jako osobnej aplikacji SignalR

**W trakcie:**
- Dopracowanie zgodności z filozofią AMODIT
- Weryfikacja architektury uwierzytelniania (OTP + JWT)

---

## Klucze decyzje architektoniczne

| Decyzja | Uzasadnienie |
|---------|--------------|
| **Osobna aplikacja SignalR** | Izolacja od głównej instancji AMODIT, lepsza wydajność przy wielu połączeniach |
| **OTP + JWT (nie token w URL)** | Bezpieczeństwo uwierzytelniania - kod jednorazowy wymieniany na token przez API |
| **Kody OTP w bazie (nie RAM)** | Obsługa Load Balancingu - każdy serwer ma dostęp do tych samych kodów |
| **Klucze szyfrowania per-tenant** | Izolacja bezpieczeństwa w środowisku multi-tenant (chmura) |
| **Komunikator jako funkcjonalność AMODIT** | Nie jest promowany jako osobny produkt, zawsze wymaga integracji z systemem |

---

## MVP1: Stabilizacja On-Premises i bezpieczeństwo

**Cel:** Uruchomienie działającej, bezpiecznej wersji komunikatora w środowisku lokalnym klienta, eliminując błędy architektury uwierzytelniania.

**Zakres:**
- [ ] Konwersacje prywatne i grupowe
- [ ] Wzmiankowanie użytkowników (@)
- [ ] Infinite scroll, wskaźnik pisania
- [ ] Implementacja OTP + JWT (eliminacja tokena z URL)
- [ ] Przeniesienie kodów OTP do bazy danych
- [ ] Szyfrowanie wiadomości

**Planowana data:** Q4 2025

---

## Główne ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Przechowywanie OTP w RAM w środowisku LB | Przeniesienie do bazy danych (MVP1) |
| Brak akceptacji architektonicznej przed implementacją | Kontynuacja z dopracowaniem zgodności, w przyszłości projekty przez akceptację przed startem |
| Nieokreślony mechanizm wykrywania trybu pracy | [DO USTALENIA: wymaga decyzji architektonicznej] |

---

## Szybkie linki

- Repozytorium: [do uzupełnienia]
- Środowisko DEV: [do uzupełnienia]
- Powiązane: `moduly/Copilot-Baza-wiedzy-AI` (integracja Copilota - odroczone)

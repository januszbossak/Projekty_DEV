# AI-driven workflow (Agenci AI)

**Typ:** Koncepcja strategiczna
**Status:** 🟡 Koncepcja - kierunek strategiczny
**Data zgłoszenia:** 2025-10-14

---

## UWAGA: TO JEST KONCEPCJA

Ten dokument opisuje **wstępną koncepcję strategiczną**, a nie zatwierdzoną funkcjonalność do realizacji. Celem jest dokumentacja kierunku myślenia i wizji rozwoju produktu.

---

## 1. Wizja

### Długoterminowy kierunek

Ewolucja AMODIT w kierunku systemu **"AI-driven workflow"** - transformacja obecnych, deterministycznych funkcji systemu (OCR, analiza SIPS, skomplikowane skrypty w Edytorze Reguł) w wyspecjalizowanych **"agentów" AI**.

### Problem do rozwiązania

Złożone, deterministyczne reguły w Edytorze Reguł są:
- Trudne w tworzeniu
- Trudne w utrzymaniu
- Wymagają głębokiej wiedzy technicznej
- Spowalniają wdrożenia

### Proponowane rozwiązanie (koncepcja)

Zastąpienie skomplikowanych reguł deterministycznych **elastycznymi modelami AI** (agentami), które:
- Przyjmują parametry sprawy z Edytora Reguł
- Na podstawie swojego modelu zwracają ustrukturyzowaną odpowiedź
- Podejmują decyzje (np. akceptacja, odrzucenie, eskalacja)

---

## 2. Przykładowe zastosowanie

### Matryce akceptacji

**Obecne podejście (deterministyczne):**
Kodowanie złożonych reguł if-else dla każdej kombinacji warunków w matrycy akceptacji.

**Podejście z agentem AI:**
1. Edytor Reguł wysyła parametry sprawy do dedykowanego "agenta AI"
2. Agent analizuje dane na podstawie wyuczonego modelu
3. Agent zwraca ustrukturyzowaną odpowiedź:
   - Decyzja (akceptacja / odrzucenie / eskalacja)
   - Uzasadnienie
   - Ścieżka dalszego procedowania

---

## 3. Oczekiwane korzyści

- **Przyspieszenie wdrożeń** - mniej kodowania, więcej konfiguracji
- **Uproszczenie logiki procesów** - elastyczne modele zamiast sztywnych reguł
- **Łatwiejsze utrzymanie** - zmiany w modelu zamiast w kodzie
- **Adaptacyjność** - model może się uczyć i dostosowywać

---

## 4. Czynniki sukcesu (kontekst)

Według dyskusji, najistotniejszym czynnikiem wpływającym na skrócenie wdrożeń jest **JAKOŚĆ AMODIT**, na którą składają się:

1. **Stabilność działania** - szczególnie po aktualizacjach
2. **Kompletność i aktualność dokumentacji** - z przykładami, dobrymi praktykami
3. **Wygoda użytkowania** - łatwość tworzenia tego, co klient chce (bez obejść)
4. **Wsparcie diagnostyczne** - podczas wdrożenia i serwisowania

---

## 5. Status i dalsze kroki

**Status:** Temat otwarty, kierunek strategiczny

**Powiązane projekty:**
- `moduly/Copilot-Baza-wiedzy-AI` - obecna implementacja AI w AMODIT

**Do ustalenia:**
- Priorytet względem innych inicjatyw
- Zakres pierwszego PoC
- Integracja z istniejącym Copilotem

---

## 6. Historia zmian

| Data | Zmiana | Źródło |
|------|--------|--------|
| 2025-10-14 | Utworzenie koncepcji - dyskusja strategiczna o AI-driven workflow i agentach AI | Notatka projektowa 2025-10-14 |

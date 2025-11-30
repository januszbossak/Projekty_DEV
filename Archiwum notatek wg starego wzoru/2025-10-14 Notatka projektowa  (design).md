---
Data: 14 października 2025
Temat: Ustalenie procesu generowania Rejestru Zmian (Changelog) oraz dyskusja strategiczna nad rozwojem agentów AI w AMODIT.
---

### **1. Omówione i uzgodnione funkcjonalności**

#### **Funkcjonalność: Usprawnienie i standaryzacja procesu generowania Rejestru Zmian (Changelog)**

- **Komponent:** Edytor Reguł (w kontekście wewnętrznego narzędzia AMODIT do raportowania zmian).
    
- **Cel:** Zapewnienie spójnego, regularnego i wiarygodnego publicznego rejestru zmian w systemie, zsynchronizowanego z cyklem wydawniczym .
    
- **Problem do rozwiązania:**
    
    - Nieregularne publikowanie listy zmian .
        
    - Występowanie niespójności między zadaniami wdrożonymi (commity w repozytorium) a opublikowanym rejestrem. (np. brak zadań, które wdrożono, ale miały niepoprawny status w Azure DevOps)  .
        
    - Konieczność ręcznej weryfikacji i filtrowania treści przed publikacją (np. usuwanie nazw klientów, informacji wrażliwych lub nieistotnych poprawek technicznych).
        
- **Sposób realizacji / Decyzja:**
    
    1. **Kryteria włączenia:** Do publicznego rejestru zmian kwalifikują się wyłącznie zadania z Azure DevOps, które jednocześnie spełniają dwa warunki:
        
        - Posiadają status **"Done".
            
        - Mają przypisaną wartość w polu **"Release Version"** .
            
    2. **Częstotliwość:** Rejestr zmian będzie generowany i publikowany **raz na dwa tygodnie**8888. Publikacja będzie następować na początku nowego sprintu i obejmować zmiany z poprzedniego sprintu. Proces ten ma być zsynchronizowany z publikacją nowych wersji (buildów) na wewnętrznej Wiki.
        
    3. **Format:** Zaakceptowano obecny format (grupowanie zmian według numeru wersji) jako czytelny i wystarczający.
        
    4. **Weryfikacja:** Wygenerowana automatycznie lista musi zostać manualnie przejrzana przed publikacją w celu usunięcia np. wewnętrznych informacji, nazw klientów lub niejasnych opisów .
        
    5. **Rozszerzanie treści:** W przypadku dodania nowych, istotnych funkcjonalności (opisanych jako "Dodano..."), należy utworzyć dodatkowy artykuł na Wiki szerzej opisujący funkcję i podlinkować go w rejestrze zmian (np. jako "Czytaj więcej").
        


---

### **2. Punkty do dalszej dyskusji (Tematy strategiczne)**

- **Temat:** Długoterminowa wizja rozwoju AMODIT w kierunku systemu "AI-driven workflow".
    
    - **Koncepcja:** Dyskusja dotyczyła ewolucji obecnych, deterministycznych funkcji systemu (takich jak OCR , analiza SIPS czy skomplikowane skrypty w Edytorze Reguł ) w kierunku wyspecjalizowanych "agentów" AI.
        
    - **Potencjalne zastosowanie (Przykład):** Zamiast kodować złożone, deterministyczne reguły dla matryc akceptacji, można by stworzyć dedykowanego "agenta AI"18. Edytor Reguł wysyłałby do agenta parametry sprawy, a agent na podstawie swojego modelu zwracałby ustrukturyzowaną odpowiedź (np. decyzję o akceptacji, odrzuceniu lub ścieżce eskalacji).
        
    - **Cel:** Przyspieszenie wdrożeń i uproszczenie logiki procesów poprzez zastąpienie skomplikowanych, trudnych w utrzymaniu reguł deterministycznych elastycznymi modelami AI.
        
    - **Status:** Temat otwarty, stanowi kierunek strategiczny .


Wg mnie najistotniejszym czynnikiem (biorąc pod uwagę produkt, a ni działania organizacyjne) wpływającym na skrócenie wdrożeń jest JAKOŚĆ Amodita. Na tę jakość składa się kilka czynników

- stabilność działania - szczególnie stabilność po aktualizacjach
- kompletność i aktualność dokumentacji, takiej z przykładami, dobrymi praktykami, 
- wygoda użytkowania rozumiana jako łatwość tworzenia tego co klient chce, a nie tworzenie jakiś dziwnych obejść
- wsparcie diagnostyczne podczas wdrożenia jak i serwisowania


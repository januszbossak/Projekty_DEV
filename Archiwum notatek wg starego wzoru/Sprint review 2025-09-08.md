[[2025-10-06 Sprint review]]
[[2025-09-08 poniedziałek]]

### Sprint review z dnia 8 września 2025

---

#### 1. Matryca uprawnień

- **Dlaczego to robimy**
    - Celem było stworzenie bardziej wygodnego i globalnego sposobu definiowania oraz odczytywania uprawnień dla pól w formularzach. Dotychczasowy sposób, wymagający wchodzenia w edycję każdego pola osobno, był nieintuicyjny i nie pozwalał na całościowy przegląd.

- **Opis funkcjonalności / rozwiązania:**
    - Stworzono nowy, tabelaryczny widok (matrycę), w którym wiersze reprezentują pola i sekcje formularza, a kolumny – etapy procesu.
    - Matryca poprawnie grupuje pola należące do sekcji oraz pól wewnątrz tabel, zachowując strukturę formularza.
    - Użytkownik może bezpośrednio w komórce matrycy zmienić uprawnienie dla danego pola na konkretnym etapie.
    - Zaimplementowano mechanizm dziedziczenia uprawnień z nadrzędnej sekcji, co jest sygnalizowane specjalną ikoną i podpowiedzią (tooltip).
    - Wprowadzono obsługę wyjątków od uprawnień dla konkretnych użytkowników; jeśli wyjątek jest zdefiniowany, ikona otwierająca okno edycji wyjątków zmienia kolor na pomarańczowy.
    - Planowane jest dodanie "trybu kompaktowego", który ukryje tekstowe opisy uprawnień, pozostawiając same ikony, co pozwoli zmieścić na ekranie więcej etapów procesu.

- **Dalsze kroki:**
    - Należy przemyśleć umiejscowienie ikon do edycji wyjątków – obecnie znajdują się po prawej stronie, co jest mało intuicyjne; sugestia jest, aby przenieść je na lewą stronę, blisko nazwy pola.
    - Należy przetestować działanie matrycy na bardzo złożonym procesie, aby zweryfikować jej czytelność i wydajność.
    - Planowane jest dodanie funkcjonalności filtrowania, która pozwoli na wyświetlanie tylko wybranych etapów procesu.

---

#### 2. Widok zadań (jobów)

- **Dlaczego to robimy**
    - Usprawnienie i odświeżenie interfejsu do zarządzania zadaniami cyklicznymi (jobami).

- **Opis funkcjonalności / rozwiązania:**
    - Nowy widok prezentuje zadania w formie tabeli i domyślnie wyświetla tylko te, które są aktywne ("pracujące").
    - Dodano standardowe mechanizmy filtrowania.
    - Akcje (np. edycja, uruchomienie) pojawiają się po najechaniu na wiersz.

- **Dalsze kroki:**
    - Należy dodać przycisk "Odśwież", który pozwoli na ponowne wczytanie statusów wszystkich zadań.
    - Należy poprawić sposób wyświetlania przycisków akcji – powinny być one widoczne po najechaniu na dowolne miejsce w wierszu, a nie tylko na kolumnę z nazwą zadania.

---

#### 3. Konfiguracja integracji

- **Dlaczego to robimy**
    - Usprawnienie procesu konfiguracji integracji z systemami zewnętrznymi, poprzez wprowadzenie walidacji i podpowiedzi, co ma na celu eliminację prostych błędów konfiguracyjnych, np. literówek w nazwach parametrów.

- **Opis funkcjonalności / rozwiązania:**
    - Podczas dodawania nowego parametru, użytkownik może wybrać jego kategorię: ogólny, endpoint lub inny.
    - Dla parametrów "ogólnych" nazwa wybierana jest z predefiniowanej listy (np. `AuthorizationType`), a typ pola (np. hasło, lista wyboru) jest ustawiany automatycznie.
    - Dla parametrów typu "inny" (niestandardowy), system wymusza stosowanie odpowiedniego prefiksu w nazwie i waliduje, czy użytkownik nie próbuje ręcznie utworzyć parametru, który jest już na predefiniowanej liście.
    - Parametry można grupować, co pozwala na ich logiczne uporządkowanie w ramach jednej integracji (np. osobne grupy dla metody GET i POST).
    - Wprowadzono rozróżnienie na "Integracje" (standardowe, wbudowane) oraz "Rozszerzenia" (dedykowane, tworzone w ramach wdrożeń).

- **Dalsze kroki:**
    - Należy zwiększyć limit znaków dla nazw parametrów w bazie danych, aby uniknąć problemów z długimi nazwami endpointów.
    - Należy rozważyć ukrycie technicznych prefiksów (np. `external.rest.`) w interfejsie użytkownika, aby poprawić czytelność.
    - Finalnie zostanie podjęta decyzja, czy "Integracje" i "Rozszerzenia" powinny być w jednej zakładce, czy w osobnych pozycjach menu. Aktualna konkluzja jest taka, żeby je rozdzielić.
    - Planowane jest dodanie opisów do standardowych integracji, aby wyjaśnić ich przeznaczenie.

---

#### 4. Raporty systemowe

- **Dlaczego to robimy**
    - Umożliwienie administratorom systemów po stronie klienta modyfikacji standardowych raportów systemowych i dostosowywania ich do własnych potrzeb.

- **Opis funkcjonalności / rozwiązania:**
    - Administratorzy należący do specjalnej grupy uprawnień będą mogli edytować raporty systemowe.
    - Kluczową funkcjonalnością jest "Zapisz jako", która pozwala na stworzenie kopii raportu systemowego jako nowego, w pełni edytowalnego raportu. Pozwala to uniknąć nadpisywania modyfikacji podczas aktualizacji systemu.
    - Wprowadzono mechanizm, który pozwala zdefiniować w raporcie filtry jako "wymagane". Jeśli taki filtr nie ma ustawionej wartości domyślnej, raport nie załaduje danych, dopóki użytkownik nie poda wartości, co zapobiega przeciążeniu systemu przez ładowanie ogromnych zbiorów danych.

- **Dalsze kroki:**
    - Trwają prace nad redefinicją i przeglądem istniejących raportów systemowych, aby były bardziej użyteczne i czytelne.

---

#### 5. Amodit Security Checklist

- **Dlaczego to robimy**
    - Stworzenie formalnego potwierdzenia, że serwery klienta (w instalacjach on-premise) zostały skonfigurowane zgodnie z wytycznymi bezpieczeństwa. Ma to na celu uniknięcie powtarzających się uwag w kolejnych audytach i testach penetracyjnych.

- **Opis funkcjonalności / rozwiązania:**
    - Zostanie przygotowany dokument w formie checklisty bezpieczeństwa.
    - Checklista będzie musiała być podpisana zarówno przez przedstawiciela wdrażającego, jak i przez klienta, co będzie potwierdzeniem wdrożenia (lub świadomej rezygnacji) poszczególnych zaleceń bezpieczeństwa.

- **Dalsze kroki:**
    - Prace nad finalizacją dokumentu są w toku.

---

#### 6. Logowanie wysyłanych maili

- **Dlaczego to robimy**
    - Zapewnienie możliwości śledzenia w historii sprawy informacji o mailach, które zostały z niej wysłane.

- **Opis funkcjonalności / rozwiązania:**
    - W ustawieniach systemowych dodano nowe opcje pozwalające włączyć logowanie wysyłanych maili w historii aktywności.
    - Można osobno kontrolować logowanie samej treści maila oraz jego załączników, co ma znaczenie ze względu na potencjalnie duży rozmiar danych zapisywanych w bazie.
    - W historii sprawy pojawia się nowy typ zdarzenia "email", który zawiera szczegóły wysłanej wiadomości, w tym jej treść i listę załączników z linkami do ich pobrania.
    - Mechanizm loguje zarówno maile wysyłane standardowo, jak i te wysyłane przez funkcje w regułach (`SendMessageEx`).

- **Dalsze kroki:**
    - Należy doprecyzować, w jaki sposób prezentowane są informacje o uprawnieniach w logu, aby uniknąć niejasności.

---

#### 7. Generowanie procesów przez AI (Copilot)

- **Dlaczego to robimy**
    - Rozwinięcie funkcjonalności Copilota, aby stał się on interaktywnym "konsultantem" wspierającym użytkownika w zbieraniu wymagań i projektowaniu procesów, zamiast być tylko pasywnym generatorem.

- **Opis funkcjonalności / rozwiązania:**
    - Po wpisaniu przez użytkownika początkowej prośby (np. "wygeneruj proces do zakupu sprzętu"), Copilot nie generuje od razu procesu, ale rozpoczyna dialog, zadając serię pytań analitycznych (np. kto bierze udział w procesie, jakie są główne kroki).
    - Po zebraniu odpowiedzi, Copilot generuje podsumowanie i prosi o potwierdzenie przed przejściem do technicznego projektowania.
    - Wprowadzono mechanizm asynchronicznego odpytywania o status generowania, aby uniknąć problemów z timeoutem na środowiskach chmurowych.
    - Prompt sterujący dialogiem został przeniesiony do mikrousługi, co pozwala na jego modyfikację bez potrzeby aktualizacji całej aplikacji.

- **Dalsze kroki:**
    - Należy zaimplementować sprawdzanie uprawnień – generowanie nowych procesów powinno być dostępne tylko dla administratorów.
    - Interfejs w trakcie generowania procesu zostanie uatrakcyjniony – zamiast statycznego spinnera, będą wyświetlane komunikaty informujące o postępie prac (np. "Pracuję nad formularzem", "Dodaję kolejne etapy").
    - Należy poprawić wygląd przycisków funkcyjnych (np. "SwitchToProcess"), aby nie wyświetlały technicznych nazw, a bardziej przyjazne dla użytkownika etykiety.

---

#### 8. Nowa funkcja w regułach (`for each attachment`)

- **Dlaczego to robimy**
    - Udostępnienie w silniku reguł możliwości operowania na plikach dołączonych do sprawy w sposób "swobodny" (jako ogólne załączniki), a nie tylko na plikach umieszczonych w dedykowanych polach typu dokument.

- **Opis funkcjonalności / rozwiązania:**
    - Wprowadzono nową konstrukcję `for each...in attachments`, która pozwala iterować po liście wszystkich załączników sprawy.
    - Wewnątrz pętli możliwe jest odczytanie różnych właściwości pliku, takich jak ID, nazwa, rozmiar, data modyfikacji, a także jego zawartość (wartość `Value` jest pobierana dopiero w momencie jawnego odwołania się do niej, dla optymalizacji).
    - Funkcja ta umożliwia
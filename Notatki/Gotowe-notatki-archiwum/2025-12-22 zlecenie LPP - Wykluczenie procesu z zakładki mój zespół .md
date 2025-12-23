Zlecenie https://astrafox.amodit.com/forms/mCase.aspx?caseId=111272
Tytuł: Wykluczenie procesu z zakładki mój zespół
Klient LPP
Wycena 8000
Teramin do 16 stycznia 2026

W ramach obszarów jest obszar portal pracownika w którym pracownik ma taki "self-service", gdzie może zgłosić członków rodziny do zus, zaktualizować PIT-2, pobrać zaświadczenie o zatrudnieniu i wynagrodzeniu. Są to prywatne sprawy załatwiane bezpośrednio z kadrami i takie procesy klient chce wykluczyć z zakładki mój zespół dla przełożonych.
Zgłoszenie https://dev.azure.com/astrafox/AMODIT/_workitems/edit/21178

Propozycja Piotra Buczkowskiego
Dodanie opcji w ustawieniach procesu: "Dostęp dla przełożonego" z opcjami

Na każdym etapie (domyślnie, tak jak teraz)
Zablokuj dostęp dla przełożonego twórcy sprawy (także na kolejnych etapach, nie tylko na pierwszym)
Zablokuj dostęp dla przełożonego wszystkich właścicieli sprawy (na wszystkich etapach)


Opcje dodać pod opcją "Nie pokazuj spraw z tego procesu administratorom i osobom z rolą "Odczyt i edycja wszystkich spraw""

Jeżeli jest zaznaczona opcja "Zablokuj dostęp dla przełożonego twórcy sprawy" to przełożony twórcy sprawy nie jest dodawany do uprawnień sprawy w funkcjach SynchronizeReadersPermissionsNew i CheckCasePermissions

Jeżeli jest zaznaczona opcja "Zablokuj dostęp dla przełożonego wszystkich właścicieli spraw" to przełożeni każdego właściciela sprawy na każdym etapie nie są dodawani do uprawnień sprawy w funkcjach j.w
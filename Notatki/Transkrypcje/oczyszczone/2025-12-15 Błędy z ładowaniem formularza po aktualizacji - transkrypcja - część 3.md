**Data spotkania:** 1-2 grudnia 2025 - część 3

---

**Tomasz Kalinowski:** Tak, działa. Rozumiem, że te dwie rzeczy w jakiś sposób psują AMODIT?

**Piotr Buczkowski:** Tylko to odwołanie do wersji 12 Newtonsoft.Json. Wartość z applicationSettings jest po prostu niepotrzebna. Właśnie poprawiam pliki wzorcowe web.config, aby tego nie było. Najlepiej poprawić to u innych klientów, gdzie były wgrywany plik na podstawie web.config.safe.txt.

**Tomasz Kalinowski:** Czy jakbym wskazał wersję 13.0, to czy to by coś zmieniło?

**Piotr Buczkowski:** Nie ma potrzeby wskazywania wersji. Ma w swoim katalogu plik newtonsoft.json.dll i z niego powinien korzystać, a nie szukać podanej wersji w GAC.

**Tomasz Kalinowski:** Okej, dzięki za wyjaśnienie.

**Daniel Reszka:** "Najlepiej poprawić to u innych klientów, gdzie były wgrywany plik na podstawie web.config.safe.txt". Czy przyszła aktualizacja to poprawi (w sensie check config z DBAdmina)? Czy trzeba ręcznie wszędzie poprawiać u klientów?

**Piotr Buczkowski:** Trzeba ręcznie poprawić. Ale w sumie można dodać sprawdzanie do check config – nie pomyślałem, że ktoś z tego korzysta.

**Daniel Reszka:** Przy każdej aktualizacji tego używamy na serwisie.

**Tomasz Kalinowski:** Piotr Buczkowski, jednak jest to samo, już nie wiem o co tu chodzi. [Zrzut ekranu] Cały czas wywala błędy Newtonsoftu. [Zrzut ekranu]






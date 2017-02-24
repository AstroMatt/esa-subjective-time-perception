# Subjective Time Perception Experiment

## How does it work?

### Skala procentowego i ilościowego poczucia czasu

Valid:
- Fast 126% - 200%
- Normal 75% - 125%
- Slow 25% - 74%

Invalid:
- Too fast 201% - ...
- Too slow 0% - 24%

### Pierwsze podejście osoby
1. Zliczam ilość wszystkich kliknięć na każdym z kolorów i sumuję je
    1. Określam procentowy współczynnik regularności: (ilość czasu / co ile sekund miał klikać) - 100%; n kliknięć - x%
    2. Wyliczenie procentowych współczynników regularności (z kroku powyżej) dla każdego z kolorów osobno
    3. >>> {"biały": 100, "czerwony": 110, "niebieski": 90} // wartości są w procentach
2. Zostawiamy tylko 80% wyników, tj. odrzucamy pierwsze 20%
3. Obliczamy czasowy współczynnik regularności dla koloru
    1. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami
    2. >>> {"czerwony": [1.025, 0.987, 1.000, 1.01...], "biały": [1.025, 0.987, 1.000, 1.01...], "niebieski": [1.025, 0.987, 1.000, 1.01...], "wszystkie": [1.025, 0.987, 1.000, 1.01...]}
4. Wyliczamy odchylenie standardowe (Regularity Coefficient) dla wszystkich razem (po appendowaniu list - 60 elem), oraz dla każdego koloru osobno (listy po 20 elementów)
    1. podnosimy każdy element listy do kwadratu
    2. sumujemy kwadraty
    3. pierwiastkujemy sumę
    4. dzielimy pierwiastek przez ilość elementów
5. Obliczamy średnią czasu (Temporal Coefficient) dla wszystkich oraz dla każdego z kolorów osobno

### Drugie podejście osoby
1. Wyliczamy to samo co dla pierwszego podejścia

### Porównujemy współczynniki regularności x1 i x2
1. Określenie wyniku w drugim podejściu - czy osoba się: poprawiła, miała taki sam wynik czy gorszy
2. Odpowiadamy: Jak szybko nasz mózg uczy się regularności

### Na później
1. Porównujemy procentowy i czasowy współczynnik regularności
2. Określenie, czy procentowa metoda jest wystarczająca (błąd poniżej 5%)
3. Tworzymy zestawienie deklarowanego (subiektywnego) poczucia rytmu ze współczynnikami regularności


## Opis danych

### Percentage

Normą jest 100%.

Tj. dla 60 sekund i klikania co 5 sekund, użytkownik powinien wygenerować 12 klików.
Odrzucamy pierwsze dwa kliknięcia (zgodnie z algorytmem) i zostaje nam 10 kliknięć.

Jeżeli user kliknął 15 razy, to jego Percentage będzie 150% normy.

### Standard Deviation (Regularity Coefficient)

Rozpoznajemy czy ktoś klikał regularnie, czy kliknął wielokrotnie a później przerwał.
Im współczynnik bliższy zero, tym lepsza regularność klikania.

### Time Mean Coefficient (Temporal Coefficient)

Co ile sekund (średnio) ktoś klikał.

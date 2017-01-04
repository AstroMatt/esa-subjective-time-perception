# Subjective Time Perception Experiment

## How it works

### Skala procentowego i ilościowego poczucia czasu
- Perfect 80% - 100%
- Above Average 60% - 79%
- Average 40% - 59%
- Below Average 20% - 39%
- Poor 0% - 19%

### Pierwsze podejście osoby
1. Zliczam ilość wszystkich kliknięć na każdym z kolorów i sumuję je
    1. Określam procentowy współczynnik regularności: (ilość czasu / co ile sekund miał klikać) - 100%; n kliknięć - x%
    2. Wyliczenie procentowych współczynników regularności (z kroku powyżej) dla każdego z kolorów osobno
    3. >>> {"biały": 100, "czerwony": 110, "niebieski": 90} // wartości są w procentach
2. Zostawiamy tylko 80% wyników, tj. odrzucamy pierwsze 10% i ostatnie 10% kliknięć (razem 20%)
3. Obliczamy czasowy współczynnik regularności dla koloru
    1. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami
    2. >>> {"czerwony": [1.025, 0.987, 1.000, 1.01...], "biały": [1.025, 0.987, 1.000, 1.01...], "niebieski": [1.025, 0.987, 1.000, 1.01...], "wszystkie": [1.025, 0.987, 1.000, 1.01...]}
4. Wyliczamy odchylenie standardowe dla wszystkich razem (po appendowaniu list - 60 elem), oraz dla każdego koloru osobno (listy po 20 elementów)
    1. podnosimy każdy element listy do kwadratu
    2. sumujemy kwadraty
    3. pierwiastkujemy sumę
    4. dzielimy pierwiastek przez ilość elementów
5. Obliczamy średnią czasu dla wszystkich oraz dla każdego z kolorów osobno

### Drugie podejście osoby
1. Wyliczamy to samo co dla pierwszego podejścia

### Porównujemy współczynniki regularności x1 i x2
1. Określenie wyniku w drugim podejściu - czy osoba się: poprawiła, miała taki sam wynik czy gorszy
2. Odpowiadamy: Jak szybko nasz mózg uczy się regularności

### Na później
1. Porównujemy procentowy i czasowy współczynnik regularności
2. Określenie, czy procentowa metoda jest wystarczająca (błąd poniżej 5%)
3. Tworzymy zestawienie deklarowanego (subiektywnego) poczucia rytmu ze współczynnikami regularności


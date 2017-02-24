Alghorithm
----------

First user attempt
^^^^^^^^^^^^^^^^^^
1. Zliczam ilość wszystkich kliknięć na każdym z kolorów i sumuję je:

    1. Określam procentowy współczynnik regularności: (ilość czasu / co ile sekund miał klikać) - 100%; n kliknięć - x%
    2. Wyliczenie procentowych współczynników regularności (z kroku powyżej) dla każdego z kolorów osobno
    3. >>> {"biały": 100, "czerwony": 110, "niebieski": 90} // wartości są w procentach

2. Zostawiamy tylko 80% wyników, tj. odrzucamy pierwsze 20%

3. Obliczamy czasowy współczynnik regularności dla koloru. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami:

.. code-block:: json

    {
        "blue": [4.842, 4.884, 4.706, 5.0, 5.073, 5.028, 4.892, 5.192, 4.88, 5.056, 5.124],
        "red": [5.009, 4.673, 5.074, 5.231, 4.946, 4.72, 5.228, 5.668, 4.822, 5.271],
        "white": [5.332, 4.463, 4.973, 5.278, 4.788, 4.998, 5.292, 5.214, 5.286, 5.409],
        "all": [4.842, 4.884, 4.706, 5.0, 5.073, 5.028, 4.892, 5.192, 4.88, 5.056, 5.124,
                5.009, 4.673, 5.074, 5.231, 4.946, 4.72, 5.228, 5.668, 4.822, 5.271,
                5.332, 4.463, 4.973, 5.278, 4.788, 4.998, 5.292, 5.214, 5.286, 5.409]
    }

4. Wyliczamy odchylenie standardowe (Regularity Coefficient) dla wszystkich razem (po appendowaniu list - 60 elem), oraz dla każdego koloru osobno (listy po 20 elementów):

    1. podnosimy każdy element listy do kwadratu
    2. sumujemy kwadraty
    3. pierwiastkujemy sumę
    4. dzielimy pierwiastek przez ilość elementów

5. Obliczamy średnią czasu (Temporal Coefficient) dla wszystkich oraz dla każdego z kolorów osobno

Second user attempt
^^^^^^^^^^^^^^^^^^^
1. Wyliczamy to samo co dla pierwszego podejścia

2. Porównujemy współczynniki regularności x1 i x2:

    1. Określenie wyniku w drugim podejściu - czy osoba się: poprawiła, miała taki sam wynik czy gorszy
    2. Odpowiadamy: Jak szybko nasz mózg uczy się regularności

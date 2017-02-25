Algorithm
=========

:Count: How many time user clicked on this colors
:Tempo: What was the percent of user clicks to expected click count
:Regularity: Standard deviation between clicks. Closer this parameter to 0 is better regularity.
:Interval: Arithmetic mean between clicks.

Validating arguments
--------------------
Before stating calculations the application is validating input arguments. The algorithm discards first two clicks from each color and checks whether ``Trial`` is still valid. This action prepare data for being processed in the next step.

Calculating coefficients
------------------------

Calculate Count
^^^^^^^^^^^^^^^
For each color application counts how many clicks was logged.

Calculate Tempo
^^^^^^^^^^^^^^^

Calculate Regularity
^^^^^^^^^^^^^^^^^^^^

Calculate Interval
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

Tempo scale for subjective time perception
------------------------------------------
Collected data are calculated and divided into following categories based on ``tempo_all`` coefficient for all colors.

Valid for use in experiment:

- Fast: 126% - 200%
- Normal: 75% - 125%
- Slow: 25% - 74%

Cannot be used in experiment:

- Too fast: 201% - ...
- Too slow: 0% - 24%

Invalid results are marked as ``is_valid = False`` in the database and they are excluded from the further analysis. We decided to store those discarded experiments for archive purposes. Thanks to this approach we've discovered and fixed some bugs in the software and recalculated the results.

The application would calculate 100% ``tempo`` (called a `Normal`) if subject is clicking in regular manner for period of time for color examination. If user generates more inputs than expected, for example clicking more quickly, the parameter will increase and accordingly decrease for lower tempo.

:Example:

    ``timeout = 60`` seconds for each color to be shown to user and for data to be collected
    ``regularity = 5`` user is expected to click every 5 seconds

    In this case we expect to receive 12 clicks (60 seconds / 5 seconds = 12).
    Then we discard (mark as ``is_valid = False``) first two clicks and hence we expect **10 clicks**.

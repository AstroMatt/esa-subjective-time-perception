Data description
================

Count
-----

Tempo
-----

Regularity
----------

Interval
--------


Standard Deviation (Regularity Coefficient)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Rozpoznajemy czy ktoś klikał regularnie, czy kliknął wielokrotnie a później przerwał.
Im współczynnik bliższy zero, tym lepsza regularność klikania.

Time Mean Coefficient (Temporal Coefficient)

Co ile sekund (średnio) ktoś klikał.


Tempo scale for subjective time perception
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Collected data are calculated and divied into following categories based on ``tempo`` coefficient for all colors.

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


Jeżeli user kliknął 15 razy, to jego Percentage będzie 150% normy.

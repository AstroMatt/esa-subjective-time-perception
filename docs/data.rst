Data description
================

:Count: How many time user clicked on this colors
:Tempo: What was the percent of user clicks to expected click count
:Regularity: Standard deviation between clicks. Closer this parameter to 0 is better regularity.
:Interval: Arithmetic mean between clicks.

Tempo scale for subjective time perception
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

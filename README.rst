Subjective Time Perception Analyzer
===================================

.. title:: Subjective Time Perception Analyzer

How different colors and light polarization influence on time perception?

The software was written for the `Advanced Concepts Team` (`European Space Agency`, `ESTEC`) experiment on subjective time perception.

It is open source (released under MIT license) and you can use it for your experiments!

.. contents:: Table of Contents
    :depth: 2
    :local:


How to use this software?
-------------------------

How to run the experiment?
^^^^^^^^^^^^^^^^^^^^^^^^^^
When computer has internet connection:

1. Run experiment on http://time-perception.herokuapp.com
2. Results will be uploaded after each experiment.

When experiment need to work offline (on computer without internet connection):

1. Download https://github.com/AstroMatt/esa-subjective-time-perception/archive/master.zip
2. Extract zip archive.
3. Copy directory ``frontend/`` (you'll need only this one) to USB disk.
4. On the other computer copy the directory or run directly from USB disk.
5. To run, open with your browser ``frontend/index.html`` (double click on this file should be enough).

How to upload results?
^^^^^^^^^^^^^^^^^^^^^^
Computer can be connected to the internet:

1. Connect computer to the internet
2. Open with your browser ``frontend/index.html``.
3. It should automatically upload results to the internet
4. Depending on how much experiments was performed, after a minute or so you should be able to see results in the administration panel.

Computer can not be connected to the internet:

1. Open ``frontend/cache.html``
2. Save all this text as a txt (Notepad or whatever) file to USB Pendrive.
3. Give me this file (or USB drive), and I will upload this results.
4. Or send me the results via email: time-perception@haras.pl

How to see results?
^^^^^^^^^^^^^^^^^^^
1. Go to [http://time-perception.herokuapp.com/admin/api_v2/trial/](http://time-perception.herokuapp.com/admin/api_v2/trial/)
2. You should know login and password :)


Technology and Architecture
---------------------------
*Subjective Time Perception Analizer* (STPA) is written as a web application platform. It uses frontend/backend model. Frontend is written in JavaScript with *jQuery* library to handle AJAX requests. Backend is written in *Python* using *Django* framework.


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


Data description
----------------

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


Plans for further development
-----------------------------
* Implement frontend in AngularJS 2.0
* Implement Django REST framework
* Refactor to use ``expected_clicks`` parameter to make the calculations simpler
* Create Experiment creation wizard
* Create reports page with graphical data analysis
* Create module ``excercise.threadmill`` to store and analyze data from `TomTom Runner Cardio` devices (downloaded from `mysports.tomtom.com <http://mysports.tomtom.com>`_ as `CSV` files)
* Write time guessing mini-game


How to develop extensions
-------------------------

API Usage
^^^^^^^^^

curl -X METHOD http://time-perception.herokuapp.com/api/v2/

Where method is one of following:

======= ====================================================
METHOD  Action
======= ====================================================
POST    Create new trial from POST data (see below)
HEAD    Check whether application accepts incoming requests
UPDATE  Recalculate all results in th database
PATCH   Recalculate results in db for one ``?id=...`` result
======= ====================================================

POST input data format
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

    {
      "trial":{
        "timeout": 3,
        "device": "lcd",
        "polarization": "horizontal",
        "location": "internet",
        "regularity": "1",
        "colors": ["red", "white", "blue"],
        "attempt": "1",
        "start_datetime": "2017-02-24T04:38:04.290Z",
        "end_datetime": "2017-02-24T04:38:30.021Z",
        "uid": "test@example.com"
      },
      "survey":{
        "datetime": "2017-02-24T04:38:14.284Z",
        "email": "test@example.com",
        "age": "29",
        "gender": "male",
        "condition": "normal",
        "rhythm": "average"
      },
      "events":[
        {"datetime":"2017-02-24T04:38:04.290Z", "target":"trial",  "action":"start"},
        {"datetime":"2017-02-24T04:38:04.290Z", "target":"survey", "action":"start"},
        {"datetime":"2017-02-24T04:38:14.283Z", "target":"survey", "action":"end"},
        {"datetime":"2017-02-24T04:38:15.463Z", "target":"black",  "action":"start"},
        {"datetime":"2017-02-24T04:38:16.965Z", "target":"black",  "action":"end"},
        {"datetime":"2017-02-24T04:38:18.233Z", "target":"red",    "action":"start"},
        {"datetime":"2017-02-24T04:38:21.234Z", "target":"red",    "action":"end"},
        {"datetime":"2017-02-24T04:38:22.481Z", "target":"white",  "action":"start"},
        {"datetime":"2017-02-24T04:38:25.483Z", "target":"white",  "action":"end"},
        {"datetime":"2017-02-24T04:38:26.981Z", "target":"blue",   "action":"start"},
        {"datetime":"2017-02-24T04:38:29.982Z", "target":"blue",   "action":"end"},
        {"datetime":"2017-02-24T04:38:30.021Z", "target":"trial",  "action":"end"}
      ],
      "clicks":[
        {"datetime":"2017-02-24T04:38:18.233Z", "color":"red"},
        {"datetime":"2017-02-24T04:38:18.849Z", "color":"red"},
        {"datetime":"2017-02-24T04:38:19.805Z", "color":"red"},
        {"datetime":"2017-02-24T04:38:22.482Z", "color":"white"},
        {"datetime":"2017-02-24T04:38:23.549Z", "color":"white"},
        {"datetime":"2017-02-24T04:38:24.795Z", "color":"white"},
        {"datetime":"2017-02-24T04:38:26.981Z", "color":"blue"},
        {"datetime":"2017-02-24T04:38:28.161Z", "color":"blue"},
        {"datetime":"2017-02-24T04:38:29.325Z", "color":"blue"}]
    }

Output data description
^^^^^^^^^^^^^^^^^^^^^^^
================= ==============================================
Parameter          Description
================= ==============================================
uid               Unique Participant ID - Email
age               Participant Age
condition         Participant Condition
gender            Participant Gender
rhythm            Participant Rhythm
\
start_datetime    Start Datetime
end_datetime      End Datetime
location          Where experiment was conducted (eg. internet)
device            Device
polarization      Polarization
timeout           Timeout
regularity        Regularity
\
count_all         Count click events - all
count_blue        Count click events - blue
count_red         Count click events - red
count_white       Count click events - white
\
percentage_all    Tempo - all
percentage_blue   Tempo - blue
percentage_red    Tempo - red
percentage_white  Tempo - white
\
time_stdev_all    Regularity - all
time_stdev_blue   Regularity - blue
time_stdev_red    Regularity - red
time_stdev_white  Regularity - white
\
time_mean_all     Interval - all
time_mean_blue    Interval - blue
time_mean_red     Interval - red
time_mean_white   Interval - white
================= ==============================================




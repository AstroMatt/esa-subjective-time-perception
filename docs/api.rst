API Documentation
=================

API Usage
---------

.. code-block:: sh

    curl -X $METHOD http://stpa.astrotech.io/api/v2/

Where $METHOD is one of following:

======= ====================================================
METHOD  Action
======= ====================================================
POST    Create new trial from POST data (see below)
HEAD    Check whether application accepts incoming requests
UPDATE  Recalculate all results in th database
PATCH   Recalculate results in db for one ``?id=...`` result
======= ====================================================

POST input data format
----------------------

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
-----------------------
=================  ==============================================
Parameter          Description
=================  ==============================================
uid                Unique Participant ID - Email
age                Participant Age
condition          Participant Condition
gender             Participant Gender
rhythm             Participant Rhythm
\
start_datetime     Start Datetime
end_datetime       End Datetime
location           Where experiment was conducted (eg. internet)
device             Device
polarization       Polarization
timeout            Timeout
regularity         Regularity
\
count_all          Count clicks - all
count_blue         Count clicks - blue
count_red          Count clicks - red
count_white        Count clicks - white
\
tempo_all          Tempo - all
tempo_blue         Tempo - blue
tempo_red          Tempo - red
tempo_white        Tempo - white
\
regularity_all     Regularity - all
regularity_blue    Regularity - blue
regularity_red     Regularity - red
regularity_white   Regularity - white
\
interval_all       Interval - all
interval_blue      Interval - blue
interval_red       Interval - red
interval_white     Interval - white
=================  ==============================================

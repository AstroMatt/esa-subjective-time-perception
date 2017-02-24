# API

## Usage

curl -X METHOD http://time-perception.herokuapp.com/api/v2/

Where method is one of following

| METHOD | Action                                      |
|:-------|:--------------------------------------------|
| POST   | Create new trial from POST data (see below) |
| HEAD   |                                             |
| UPDATE |                                             |
| PATCH  |                                             |

## POST Input Data
```json
{
    "configuration": {
        "colors": ["white", "blue", "red"],
        "device": "laptop",
        "end": "2016-12-27T16:49:44.526Z",
        "location": "internet",
        "uid": "test@example.com",
        "polarization": "vertical",
        "timeout": 60.0,
        "regularity": 5,
        "start": "2016-12-27T16:49:30.547Z",
        "attempt": 1
    },

    "survey": {
        "datetime": "2016-12-27T16:49:30.548Z",
        "email": "test@example.com",
        "age": "21",
        "condition": "normal",
        "gender": "male",
        "rhythm": "average"
    },

    "clicks": [
        {"datetime": "2016-12-27T16:49:35.224Z", "target": "black",  "action": "click"},
        {"datetime": "2016-12-27T16:49:35.630Z", "target": "black",  "action": "click"},
        {"datetime": "2016-12-27T16:49:37.144Z", "target": "white",  "action": "start"},
        {"datetime": "2016-12-27T16:49:37.148Z", "target": "white",  "action": "click"},
        {"datetime": "2016-12-27T16:49:37.432Z", "target": "white",  "action": "click"},
        {"datetime": "2016-12-27T16:49:40.236Z", "target": "blue",   "action": "click"},
        {"datetime": "2016-12-27T16:49:40.407Z", "target": "blue",   "action": "click"},
        {"datetime": "2016-12-27T16:49:42.412Z", "target": "red",    "action": "click"},
        {"datetime": "2016-12-27T16:49:42.722Z", "target": "red",    "action": "click"},
    ],

    "events": [
        {"datetime": "2016-12-27T16:49:30.548Z", "target": "trial",  "action": "start"},
        {"datetime": "2016-12-27T16:49:30.548Z", "target": "survey", "action": "start"},
        {"datetime": "2016-12-27T16:49:34.312Z", "target": "survey", "action": "end"},
        {"datetime": "2016-12-27T16:49:35.222Z", "target": "black",  "action": "start"},
        {"datetime": "2016-12-27T16:49:39.147Z", "target": "white",  "action": "end"},
        {"datetime": "2016-12-27T16:49:40.232Z", "target": "blue",   "action": "start"},
        {"datetime": "2016-12-27T16:49:42.238Z", "target": "blue",   "action": "end"},
        {"datetime": "2016-12-27T16:49:42.411Z", "target": "red",    "action": "start"},
        {"datetime": "2016-12-27T16:49:44.418Z", "target": "red",    "action": "end"},
        {"datetime": "2016-12-27T16:49:44.527Z", "target": "trial",  "action": "end"}
    ]
}
```

## Output Data
```
- Participant Email
- Participant Age
- Participant Condition
- Participant Gender
- Participant Rhythm

- Start Datetime
- End Datetime
- Location
- Device
- Polarization Trial 1
- Polarization Trial 2
- Timeout
- Regularity

- C_1 - [Trial 1] Count click events - all
- C_2 - [Trial 2] Count click events - all
- CB1 - [Trial 1] Count click events - blue
- CB2 - [Trial 2] Count click events - blue
- CR1 - [Trial 1] Count click events - red
- CR2 - [Trial 2] Count click events - red
- CW1 - [Trial 1] Count click events - white
- CW2 - [Trial 2] Count click events - white

- P_1 - [Trial 1] Percentage Coefficient - all
- P_2 - [Trial 2] Percentage Coefficient - all
- PB1 - [Trial 1] Percentage Coefficient - blue
- PB2 - [Trial 2] Percentage Coefficient - blue
- PR1 - [Trial 1] Percentage Coefficient - red
- PR2 - [Trial 2] Percentage Coefficient - red
- PW1 - [Trial 1] Percentage Coefficient - white
- PW2 - [Trial 2] Percentage Coefficient - white

- TSD_1 - [Trial 1] Time Coefficient Standard Deviation - all
- TSD_2 - [Trial 2] Time Coefficient Standard Deviation - all
- TSDB1 - [Trial 1] Time Coefficient Standard Deviation - blue
- TSDB2 - [Trial 2] Time Coefficient Standard Deviation - blue
- TSDR1 - [Trial 1] Time Coefficient Standard Deviation - red
- TSDR2 - [Trial 2] Time Coefficient Standard Deviation - red
- TSDW1 - [Trial 1] Time Coefficient Standard Deviation - white
- TSDW2 - [Trial 2] Time Coefficient Standard Deviation - white

- TM_1 - [Trial 1] Time Coefficient Mean - all
- TM_2 - [Trial 2] Time Coefficient Mean - all
- TMB1 - [Trial 1] Time Coefficient Mean - blue
- TMB2 - [Trial 2] Time Coefficient Mean - blue
- TMR1 - [Trial 1] Time Coefficient Mean - red
- TMR2 - [Trial 2] Time Coefficient Mean - red
- TMW1 - [Trial 1] Time Coefficient Mean - white
- TMW2 - [Trial 2] Time Coefficient Mean - white
```

# Subjective Time Perception Experiment
How different colors and light polarization influence on time perception?

## Lenght
Experiment takes around 10 minutes.

## Experiment Instructions
1. Sit 20 cm from the screen.
2. Click start and fill survey.
3. When you see black, red, blue or white screen click left mouse button once every five seconds.
4. Run this experimnet two times with different polarization.

## Install
1. Download [https://github.com/AstroMatt/esa-subjective-time-perception/archive/master.zip](https://github.com/AstroMatt/esa-subjective-time-perception/archive/master.zip)
2. Extract zip archive
3. Open with your browser `frontend/index.html`

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
2. Zostawiamy tylko 80% wyników, tj. odrzucamy pierwsze 20% i ostatnie 20% kliknięć
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

## Input Data
```json
{
    "configuration": {
        "colors": ["white", "blue", "red"],
        "device": "laptop",
        "end": "2016-12-27T16:49:44.526Z",
        "location": "internet",
        "uid": "c@c.pl",
        "polarization": "vertical",
        "timeout": 30.0,
        "regularity": 5,
        "start": "2016-12-27T16:49:30.547Z",
        "attempt": 1
    },

    "survey": {
        "datetime": "2016-12-27T16:49:30.548Z",
        "email": "c@c.pl",
        "age": "21",
        "condition": "normal",
        "gender": "male",
        "rhythm": "average"
    },

    "events": [
        {"datetime": "2016-12-27T16:49:30.548Z", "target": "trial",  "action": "start"},
        {"datetime": "2016-12-27T16:49:30.548Z", "target": "survey", "action": "start"},
        {"datetime": "2016-12-27T16:49:34.312Z", "target": "survey", "action": "end"},
        {"datetime": "2016-12-27T16:49:35.222Z", "target": "black",  "action": "start"},
        {"datetime": "2016-12-27T16:49:35.224Z", "target": "black",  "action": "click"},
        {"datetime": "2016-12-27T16:49:35.630Z", "target": "black",  "action": "click"},
        {"datetime": "2016-12-27T16:49:37.144Z", "target": "white",  "action": "start"},
        {"datetime": "2016-12-27T16:49:37.148Z", "target": "white",  "action": "click"},
        {"datetime": "2016-12-27T16:49:37.432Z", "target": "white",  "action": "click"},
        {"datetime": "2016-12-27T16:49:39.147Z", "target": "white",  "action": "end"},
        {"datetime": "2016-12-27T16:49:40.232Z", "target": "blue",   "action": "start"},
        {"datetime": "2016-12-27T16:49:40.236Z", "target": "blue",   "action": "click"},
        {"datetime": "2016-12-27T16:49:40.407Z", "target": "blue",   "action": "click"},
        {"datetime": "2016-12-27T16:49:42.238Z", "target": "blue",   "action": "end"},
        {"datetime": "2016-12-27T16:49:42.411Z", "target": "red",    "action": "start"},
        {"datetime": "2016-12-27T16:49:42.412Z", "target": "red",    "action": "click"},
        {"datetime": "2016-12-27T16:49:42.722Z", "target": "red",    "action": "click"},
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

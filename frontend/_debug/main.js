// minify HTML: https://www.willpeavy.com/minifier/
// minify JS: https://dotmaui.com/jsminify/

if (location.hostname == "localhost" || location.hostname == "127.0.0.1")
    URL = 'http://localhost:8000/api/v3/'
else
    URL = 'http://time.astrotech.io/api/v3/'


var Trial = {
    device: "lcd",
    location: "internet",
    regularity: 5,
    timeout: 3.0,
    colors: shuffle(["red", "blue", "white"]),
    clicks: [],
    start_datetime: new Date().toJSON()
};

function hide(id) {
    var element = document.getElementById(id);
    element.style.display = 'none';
}

function show(id) {
    if (id == 'test' && localStorage.getItem('.remember')) {
        hide('test');
        show('color0');
        return;
    }

    var element = document.getElementById(id);
    element.style.display = 'block';
}

function saveSurvey() {
    Trial.uid = document.querySelector('input[name="email"]').value;
    Trial.survey_datetime = new Date().toJSON(),
    Trial.survey_age = document.querySelector('input[name="age"]').value;
    Trial.survey_gender = document.querySelector('input[name="gender"]:checked').value;
    Trial.survey_condition = document.querySelector('input[name="condition"]:checked').value;
    Trial.survey_heart_rate = document.querySelector('input[name="heart_rate"]').value;
    Trial.survey_bp_systolic = document.querySelector('input[name="bp_systolic"]').value;
    Trial.survey_bp_diastolic = document.querySelector('input[name="bp_diastolic"]').value;
    Trial.survey_sleep = document.querySelector('input[name="sleep"]').value;
    Trial.survey_temperature = document.querySelector('input[name="temperature"]').value;
    Trial.survey_time = document.querySelector('input[name="time"]').value;
}

function fullscreen() {
    let bg = document.getElementById("background");

    if (bg.webkitRequestFullScreen)
        bg.webkitRequestFullScreen();
    else if (bg.mozRequestFullScreen)
        bg.mozRequestFullScreen();
    else if (bg.msRequestFullscreen)
        bg.msRequestFullscreen();
    else
        bg.requestFullscreen();
}

function shuffle(array) {
    // Knuth Random Shuffle Algorithm
    var currentIndex = array.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
    return array;
}

function sleep(seconds) {
    let milliseconds = seconds * 1000;
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}

function testAndProceed(next) {
    let color = 'gray';
    let timeout = Trial.timeout / 2;
    let background = document.getElementById('background');
    let oldBackground = background.style.background;
    let content = document.getElementById('test');
    let oldContent = content.innerHTML;

    content.innerHTML = '<h1>Click now!</h1>';
    background.style.background = color;

    sleep(timeout).then(() => {
        background.style.background = oldBackground;
        content.innerHTML = oldContent;
        hide('test');
        show(next);
    });
}

function runAndProceed(number, next) {
    let color = Trial.colors[number];
    let timeout = Trial.timeout;
    let id = 'color' + number;
    let oldBackground = background.style.background;
    let content = document.getElementById(id);
    let oldContent = content.innerHTML;

    content.innerHTML = '';
    background.style.background = color;
    background.addEventListener('click', click);

    sleep(timeout).then(() => {
        background.removeEventListener('click', click);
        background.style.background = oldBackground;
        content.innerHTML = oldContent;
        hide(id);
        show(next);

        if (next == 'results')
            finish();
    });
}

function click() {
    var background = document.getElementById('background');

    Trial.clicks.push({
        datetime: new Date().toJSON(),
        color: background.style.backgroundColor
    });
}

function finish() {
    let blue = Trial.clicks.filter(click => click.color=='blue').length
    let red = Trial.clicks.filter(click => click.color=='red').length
    let white = Trial.clicks.filter(click => click.color=='white').length

    if (Trial.location == "internet")
        localStorage.setItem('.remember', JSON.stringify(Trial));

    if ([blue, red, white].every(count => count > 5)) {
        Trial.end_datetime = new Date().toJSON();
        localStorage.setItem(Trial.end_datetime, JSON.stringify(Trial));
        trySyncDB();
        window.location.reload(true);
    } else {
       alert('Not enough clicks, for the experiment to be valid! Please re-run the experiment.');
       hide('results');
       show('survey');
    }
}

function request(arg) {
    var server = new XMLHttpRequest();
    server.onreadystatechange = function() {
        if (this.readyState == XMLHttpRequest.DONE)
            switch(this.status) {
                case 200: arg.onSuccess(this.status); break;
                case 201: arg.onSuccess(this.status); break;
                default: arg.onError(this.status); break;
            }
    };
    server.open(arg.method, arg.url, true);
    server.setRequestHeader("Content-type", "application/json");
    server.send(arg.data);
}

function trySyncDB() {
    if (! navigator.onLine) {
        console.log('Browser is not online.');
        return;
    }

    request({
        method: "OPTIONS",
        url: URL,
        onSuccess: function(status) {
            uploadResults();
        },
        onError: function() {
            console.log('Server cannot be contacted');
        }
    });
}

function uploadResults() {
    for (let key of Object.keys(localStorage)) {

        if (key == ".remember")
            continue;

        request({
            method: "POST",
            url: URL,
            data: localStorage.getItem(key),
            onSuccess: function(status) {
                console.log('Result uploaded');
                localStorage.removeItem(key);
            },
            onError: function(status) {
                console.log('There is a problem with uploading data. We will try later. Received status:', status);
            }
        });
    }
}

if (location.hostname !== "localhost" && location.hostname !== "127.0.0.1") {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-92351316-5', 'auto');
  ga('send', 'pageview');
}

window.addEventListener('online', trySyncDB);


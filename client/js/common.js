Experiment = {
    get: function() {
        var data = localStorage.getItem("currentExperiment");
        return JSON.parse(data);
    },

    set: function(data) {
        return localStorage.setItem("currentExperiment", JSON.stringify(data));
    },

    update: function(key, value) {
        var data = this.get();
        data[key] = value;
        return this.set(data);
    },

    clear: function() {
        this.set(Array());
    }
}

Journal = {
    get: function() {
        var data = localStorage.getItem("journal");
        return JSON.parse(data);
    },

    add: function(experiment) {
        var data = this.get();
        if (!data)
            data = Array();
        data.push(experiment)
        return this.set(data);
    },

    set: function(data) {
        return localStorage.setItem("journal", JSON.stringify(data));
    },

    clear: function() {
        this.set(Array());
    }
}

function seconds(number) {
    return number * 1000;
}

// Knuth Random Shuffle Algorithm
function shuffle(array) {
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
  return new Promise((resolve) => setTimeout(resolve, seconds));
}

function goto(next) {
    var url = window.location.href;
    var current = url.split("/").pop();
    var next = url.replace(current, next+".html");
    window.location.replace(next);
}

function fullscreen() {
    var bg = document.querySelector('body');

    if (bg.webkitRequestFullScreen)
        bg.webkitRequestFullScreen();
    else
        bg.mozRequestFullScreen();
}

function click() {
    var data = Experiment.get();

    if (!data.clicks)
        data.clicks = Array();

    data.clicks.push({
        "datetime": new Date().toJSON(),
        "background": document.body.style.backgroundColor
    });
    return Experiment.set(data);
}

function logEvent(action, message) {
    var data = Experiment.get();

    if (!data.events)
        data.events = Array();

    data.events.push({
        "datetime": new Date().toJSON(),
        "action": action,
        "message": message
    });
    return Experiment.set(data);
}

Experiment = {
    create: function(data) {
        if (!data)
            data = {}
        this.set(data);
    },

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
        this.set({});
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

    remove: function(experiment) {
        var oldJournal = this.get();
        var newJournal = oldJournal.filter(item => {
            return item.date != experiment.date;
        });
        this.set(newJournal);
    },

    set: function(data) {
        return localStorage.setItem("journal", JSON.stringify(data));
    },

    clear: function() {
        this.set(Array());
    },
    
    syncdb: function() {
        for (let experiment of Journal.get()) {
            $.ajax({
                type: "POST",
                crossDomain: true,
                url: "http://matt:8000/api/v1/experiment/",
                data: JSON.stringify(experiment),
    
                success: function(response) {
                    Journal.remove(experiment);
                },
    
                error: function(response) {
                    console.log("Cannot save experiment to the database. Will try later.");
                }
            });
        }
    }
}

function now() {
    return new Date().toJSON();
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

function log(action, target) {
    var experiment = Experiment.get();

    if (!experiment.data)
        experiment.data = Array();

    experiment.data.push({
        "datetime": new Date().toJSON(),
        "target": target,
        "action": action,
    });
    return Experiment.set(experiment);
}

function click() {
    log("click", document.body.style.backgroundColor);
}

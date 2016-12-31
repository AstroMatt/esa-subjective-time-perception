Database = {
    url: "http://time-perception.herokuapp.com/api/v2/",

    get: function() {
        database = Array();

        for (let key of Object.keys(localStorage)) {
            if (key != ".temp") {
                let value = localStorage.getItem(key);
                database.push(JSON.parse(value));
            }
        }

        return database;
    },

    insert: function(trial) {
        console.debug("[SUCCESS] Trial saved to localStorage:", trial);
        return localStorage.setItem(trial.trial.start_datetime, JSON.stringify(trial));
    },

    delete: function(trial) {
        console.debug("[SUCCESS] Trial deleted from localStorage", trial);
        return localStorage.removeItem(trial.trial.start_datetime);
    },

    clear: function() {
        console.debug("[SUCCESS] Database in localStorage cleared");
        return localStorage.clear();
    },

    uploadResults: function() {
        for (let trial of Database.get()) {
            $.ajax({
                type: "POST",
                crossDomain: true,
                url: this.url,
                data: JSON.stringify(trial),

                success: function() {
                    let trial = JSON.parse(this.data);
                    console.debug("[SUCCESS] Trial results uploaded to the remote database:", trial);
                    Database.delete(trial);
                },

                error: function() {
                    let trial = JSON.parse(this.data);
                    console.debug("[WARNING] Will try syncdb latter:", trial);
                }
            });
        }
    },

    syncdb: function() {
        $.ajax({
            type: "HEAD",
            crossDomain: true,
            url: this.url,

            success: function() {
                console.debug("[SUCCESS] Connection established to the remote database:", this.url);
                Database.uploadResults();
            },

            error: function() {
                console.debug("[WARNING] Will try syncdb latter. Unable connect to database:", this.url);
            }
        });
    }
}

Trial = {
    create: function() {
        let get = RequestArgumentsFromURL();

        this.set({
            "trial": {
                timeout: parseFloat(get["timeout"]),
                device: get["device"],
                polarization: get["polarization"],
                location: get["location"],
                regularity: get["regularity"],
                colors: shuffle(["red", "white", "blue"]),
                attempt: get["attempt"],
                start_datetime: new Date().toJSON(),
                end_datetime: null
            }
        });

        console.debug("[SUCCESS] Trial created", Trial.get());
        return Trial.get();
    },

    config: function(key, value) {
        var conf = this.get().trial;

        if (!key)
            return conf;

        if (value) {
            conf[key] = value;
            this.update("trial", conf);
        }

        return conf[key];
    },

    get: function() {
        let data = localStorage.getItem(".temp");
        return JSON.parse(data);
    },

    set: function(data) {
        return localStorage.setItem(".temp", JSON.stringify(data));
    },

    update: function(key, value) {
        var data = this.get();
        data[key] = value;
        return this.set(data);
    },

    clear: function() {
        return this.set({});
    },

    save: function() {
        let trial = this.get();
        return Database.insert(trial);
    }
}

function RequestArgumentsFromURL() {
    let url = window.location.href;

    if (! url.includes("?"))
        return Array();

    let params = url.split("?").pop();
    var arguments = {}

    for (let param of params.split("&")) {
        let arg = param.split("=");
        let key = arg[0];
        let value = arg[1].replace(/%20/g, " ").replace(/\+/g, " ")
        arguments[key] = value;
    }

    return arguments;
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
    let miliseconds = seconds * 1000;
    return new Promise((resolve) => setTimeout(resolve, miliseconds));
}

function goto(filename) {
    let url = window.location.href;
    let current = url.split("/").pop();
    let next = url.replace(current, filename+".html");
    window.location.replace(next);
}

function fullscreen() {
    let bg = document.querySelector("body");

    if (bg.webkitRequestFullScreen)
        bg.webkitRequestFullScreen();
    else
        bg.mozRequestFullScreen();
}

function log(action, target) {
    var trial = Trial.get();

    if (!trial.events)
        trial.events = Array();

    trial.events.push({
        datetime: new Date().toJSON(),
        target: target,
        action: action,
    });

    return Trial.set(trial);
}

function click() {
    log("click", document.body.style.backgroundColor);
}

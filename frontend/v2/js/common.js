DEBUG = false
URL = 'http://time.astrotech.io/api/v2/'

Database = {
    getItem: function(key) {
        return localStorage.getItem(key);
    },

    setItem: function(key, value) {
        return localStorage.setItem(key, value);
    },

    get: function() {
        database = Array();

        for (let key of Object.keys(localStorage)) {
            if (key != ".temp" && key != ".veteran") {
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
        console.debug("[DEBUG] Database in localStorage cleared");
        localStorage.clear();
        localStorage.setItem('.veteran', true);
    },

    uploadResults: function() {
        for (let trial of Database.get()) {
            $.ajax({
                type: "POST",
                crossDomain: true,
                url: URL,
                data: JSON.stringify(trial),

                success: function(response) {
                    let trial = JSON.parse(this.data);
                    console.info("[INFO] Trial results uploaded to the remote database:", this.url);
                    console.debug("[DEBUG] Received response", response.data)
                    Database.delete(trial);
                    return response.data;
                },

                error: function() {
                    let trial = JSON.parse(this.data);
                    console.warn("[WARNING] Unable connect to database. Working in offline mode. Will try syncdb latter with:", URL);

                }
            });
        }
    },

    syncdb: function() {
        if (DEBUG) {
            alert("You're in DEBUG mode! Will not `Database.syncdb()`");
            return;
        }

        $.ajax({
            type: "HEAD",
            crossDomain: true,
            url: URL,

            success: function() {
                console.info("[INFO] Connection established to the remote database:", URL);
                return Database.uploadResults();
            },

            error: function() {
                console.warn("[WARNING] Unable connect to database. Working in offline mode. Will try syncdb latter with:", URL);
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

    getResults: function(datetime) {
            $.ajax({
                type: "GET",
                url: URL,
                data: {"start_datetime": datetime},

                success: function(response) {
                    console.info("[INFO] Received response from:", URL);
                    console.debug("[DEBUG] Received response:", response.data);
                    return generateResultsTable(response.data);
                },

                error: function() {
                    console.error("[ERROR] Cannot receive results for:", this.data);
                }
            });
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
        if (DEBUG) {
            alert("You're in DEBUG mode! Will not `Trial.save()`");
            return;
        }
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
    let milliseconds = seconds * 1000;
    return new Promise(resolve => setTimeout(resolve, milliseconds));
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
    var trial = Trial.get();

    if (!trial.clicks)
        trial.clicks = Array();

    trial.clicks.push({
        datetime: new Date().toJSON(),
        color: document.body.style.backgroundColor
    });

    return Trial.set(trial);
}

if (location.hostname !== "localhost" && location.hostname !== "127.0.0.1") {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-92351316-5', 'auto');
  ga('send', 'pageview');
}

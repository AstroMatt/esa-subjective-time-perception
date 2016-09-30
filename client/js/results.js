function resultsTable(data) {
    data['time'] = function(){return this.datetime.substr(11, 12)};
    var template = $('#results-row').html();
    var html = Mustache.render(template, data);
    $('#results').append(html);
}

function getColorEvents(color, data) {
    var events = [];
    for (let click of data['clicks'])
        if (click['background'] == color)
            events.push(click['datetime']);
    return events;
}

function howFast(average) {
    if (average > 1.0)
        return 'fast';
    else if (average < 1.0)
        return 'slow';
    else
        return 'perfect';
}

function getStats(color, data) {
    var timeout = Experiment.get().timeout;
    var events = getColorEvents(color, data);
    var start = new Date(events[0]);
    var end = new Date(events[events.length-1]);
    var average = (events.length / (timeout / 1000)).toFixed(2);

    var values = {
        count: events.length,
        time: timeout / 1000,
        average: average,
        status: howFast(average)
    };

    $('#' + color + '-count').html(values.count);
    $('#' + color + '-time').html(values.time);
    $('#' + color + '-average').html(values.average);
    $('#' + color + '-status').html(values.status).addClass(values.status);

    return values;
}

function summaryTable(data) {
    var timeout = Experiment.get().timeout;
    var red = getStats('red', data);
    var blue = getStats('blue', data);
    var white = getStats('white', data);

    var total_count = red.count + blue.count + white.count;
    var total_average = total_count / (timeout * 3 / 1000);

    $('#total-count').html(total_count);
    $('#total-average').html(total_average.toFixed(2));
    $('#total-time').html(timeout * 3 / 1000);
    $('#total-status').html(howFast(total_average)).addClass(howFast(total_average));
}

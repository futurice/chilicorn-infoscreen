// Reloads this page after a time period.
//
// waiting_time_seconds tells how long to wait before reloading.
function wait_and_reload(waiting_time_seconds) {
    var waiting_time_milliseconds = 1000*waiting_time_seconds;

    window.setTimeout(function () {
        console.log("reloading");
        window.location.reload(true);
    }, waiting_time_milliseconds);
}

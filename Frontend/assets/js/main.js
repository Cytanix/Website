            // Simple countdown (30 days for example)
function updateTimer() {
    let endDate = new Date('2025-03-30').getTime();
    let now = new Date().getTime();
    let timeLeft = endDate - now;

    let days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    let hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById("timer").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s";

    if (timeLeft < 0) {
        document.getElementById("timer").innerHTML = "Launch Day!";
    }
}

setInterval(updateTimer, 1000);
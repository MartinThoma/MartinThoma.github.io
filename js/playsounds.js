function play_sound() {
    if (Math.random() < 0.5) {
        document.getElementById('results').innerHTML += 'left<br/>';
        document.getElementById('left_channel').play();
        var start = new Date().getTime();
        var milliseconds = document.getElementById('seconds').value;
        for (var i = 0; i < 1e7; i++) {
            if ((new Date().getTime() - start) > milliseconds){
                break;
            }
        }
        document.getElementById('right_channel').play();
    } else {
        document.getElementById('results').innerHTML += 'right<br/>';
        document.getElementById('right_channel').play();
        var start = new Date().getTime();
        var milliseconds = document.getElementById('seconds').value;
        for (var i = 0; i < 1e7; i++) {
            if ((new Date().getTime() - start) > milliseconds){
                break;
            }
        }
        document.getElementById('left_channel').play();
    }
}
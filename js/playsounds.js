function play_sound() {
    if (Math.random() < 0.5) {
        document.getElementById('results').innerHTML += 'left<br/>';
        document.getElementById('left_channel').play();
        setTimeout(function(){ document.getElementById('right_channel').play(); },
                   document.getElementById('seconds').value);
    } else {
        document.getElementById('results').innerHTML += 'right<br/>';
        document.getElementById('right_channel').play();
        setTimeout(function(){ document.getElementById('left_channel').play(); },
                   document.getElementById('seconds').value);
    }
}

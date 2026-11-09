'use strict';

var video = document.querySelector("#vid");
var canvas = document.querySelector('#canvas');
var context = canvas.getContext('2d');
var localMediaStream = null;

var onCameraFail = function (e) {
    console.log('Camera did not work.', e);
};

/**
 * Apply a filter to grayscale image. (Covolution)
 * @param {ImageData} imgData
 * @param {matrix of numbers} matrix
 * @return {undefined}
 */
function applyMatrix(imgData, matrix) {
    var imgDataNormal = context.getImageData(0, 0,
                context.canvas.width, context.canvas.height);
    var sep = (matrix.length-1)/2

    for (var i = 0; i < imgData.width * imgData.height * 4; i += 4) {
        var tmp = i/4;
        var x = tmp % imgData.width;
        var y = (tmp - x)/imgData.width;
        if (x <= sep || y <= sep) {
            // to small to apply filter
            continue;
        }

        var tmpPxl = 0;
        for (var ym=0; ym < matrix.length; ym++) {
            for (var xm=0; xm < matrix[0].length; xm++) {
                var tmpYPos = y+(-matrix.length+ym);
                var tmpXPos = x+(-matrix[0].length+xm);
                var tmpPos = 4*(imgData.width*tmpYPos+tmpXPos);
                tmpPxl += matrix[ym][xm]*imgDataNormal.data[tmpPos];
            }
        }
        imgData.data[4*(imgData.width*y+x)+0] = tmpPxl; // r
        imgData.data[4*(imgData.width*y+x)+1] = tmpPxl; // g
        imgData.data[4*(imgData.width*y+x)+2] = tmpPxl; // b
    }
    context.putImageData(imgData, 0, 0);
}

function snapshot() {
    if (localMediaStream) {
        context.drawImage(video, 0, 0);
        var width = 640;
        var height = 480;
        var imgDataNormal = context.getImageData(0, 0, width, height);
        var imgData = context.createImageData(width, height);

        for (var i = 0; i < imgData.width * imgData.height * 4; i += 4) {
            var r = (imgDataNormal.data[i + 0] * .393) + (imgDataNormal.data[i + 1] * .769) + (imgDataNormal.data[i + 2] * .189);
            var g = (imgDataNormal.data[i + 0] * .349) + (imgDataNormal.data[i + 1] * .686) + (imgDataNormal.data[i + 2] * .168);
            var b = (imgDataNormal.data[i + 0] * .272) + (imgDataNormal.data[i + 1] * .534) + (imgDataNormal.data[i + 2] * .131);
            if (r > 255) {
                r = 255;
            }
            if (g > 255) {
                g = 255;
            }
            if (b > 255) {
                b = 255;
            }
            imgData.data[i + 0] = r;
            imgData.data[i + 1] = g;
            imgData.data[i + 2] = b;
            imgData.data[i + 3] = imgDataNormal.data[i + 3];

            // Grayscale
            var brightness = (3*r+4*g+b)>>>3;
            imgData.data[i] = brightness;
            imgData.data[i+1] = brightness;
            imgData.data[i+2] = brightness;
        }

        var filter = document.getElementById('filter').value;
        var k1 = document.getElementById('k1');
        var k2 = document.getElementById('k2');
        var k3 = document.getElementById('k3');
        var k4 = document.getElementById('k4');
        var k5 = document.getElementById('k5');
        var k6 = document.getElementById('k6');
        var k7 = document.getElementById('k7');
        var k8 = document.getElementById('k8');
        var k9 = document.getElementById('k9');

        var matrix;
        if (filter === 'prewitt-x') {
            matrix = [[-1,0,1],[-1,0,1],[-1,0,1]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'prewitt-y') {
            matrix = [[-1,-1,-1],[0,0,0],[1,1,1]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'prewitt-y-switched') {
            matrix = [[1,1,1],[0,0,0],[-1,-1,-1]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'sobel-x') {
            matrix = [[1,0,-1],[2,0,-2],[1,0,-1]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'sobel-y') {
            matrix = [[1,2,1],[0,0,0],[-1,-2,-1]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'kirsh-x') {
            matrix = [[5,-3,-3],[5,0,-3],[5,-3,-3]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'kirsh-y') {
            matrix = [[5,5,5],[-3,0,-3],[-3,-3,-3]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'laplace') {
            matrix = [[0,1,0],[1,-4,1],[0,1,0]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'canny-edge-detector') {
            matrix = [[2.0/159,4.0/159,5.0/159,4.0/159,2.0/159],[4.0/159,9.0/159,12.0/159,9.0/159,4.0/159],[5.0/159,12.0/159,15.0/159,12.0/159,5.0/159],[4.0/159,9.0/159,12.0/159,9.0/159,4.0/159],[2.0/159,4.0/159,5.0/159,4.0/159,2.0/159]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        } else if (filter == 'custom') {
            matrix = [[k1.value, k2.value, k3.value],
                      [k4.value, k5.value, k6.value],
                      [k7.value, k8.value, k9.value]];
        } else {
            matrix = [[0,0,0],[0,1,0],[0,0,0]];
            k1.value = matrix[0][0];
            k2.value = matrix[0][1];
            k3.value = matrix[0][2];
            k4.value = matrix[1][0];
            k5.value = matrix[1][1];
            k6.value = matrix[1][2];
            k7.value = matrix[2][0];
            k8.value = matrix[2][1];
            k9.value = matrix[2][2];
        }

        context.putImageData(imgData, 0, 0);

        applyMatrix(imgData, matrix);
    }
}

var refreshRate = document.getElementById('refreshRate').value;

var timerVar = setInterval(snapshot, refreshRate);

function updateTimer() {
    window.clearInterval(timerVar);
    var refreshRate = document.getElementById('refreshRate').value;
    timerVar = setInterval(snapshot, refreshRate);
    console.log("Update Timer to " + refreshRate + " ms.");
}

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL;
navigator.getUserMedia({video:true}, function (stream) {
    video.srcObject = stream;
    localMediaStream = stream;
}, onCameraFail);
console.log(localMediaStream);

window.onload = function WindowLoad(event) {
    var qs = (function (a) {
        if (a === ""){
            return {};
        }

        var b = {};
        for (var i = 0; i < a.length; ++i) {
            var p = a[i].split('=');
            if (p.length != 2){
                continue;
            }

            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'));

    var parameters = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9"];
    for (var i = 0; i < parameters.length; i++) {
        if (qs[parameters[i]] != undefined) {
            document.getElementById(parameters[i]).value = qs[parameters[i]];
        }
    }
}

/**
 * Modify url so that I can later read all information from it.
 * @return {undefined}
 */
function modifyURL() {
    var k1 = encodeURIComponent(document.getElementById("k1").value);
    var k2 = encodeURIComponent(document.getElementById("k2").value);
    var k3 = encodeURIComponent(document.getElementById("k3").value);
    var k4 = encodeURIComponent(document.getElementById("k4").value);
    var k5 = encodeURIComponent(document.getElementById("k5").value);
    var k6 = encodeURIComponent(document.getElementById("k6").value);
    var k7 = encodeURIComponent(document.getElementById("k7").value);
    var k8 = encodeURIComponent(document.getElementById("k8").value);
    var k9 = encodeURIComponent(document.getElementById("k9").value);
    document.getElementById("newWindow").href = "graphic-filters.htm?k1=" + k1
      + "&k2=" + k2
      + "&k3=" + k3
      + "&k4=" + k4
      + "&k5=" + k5
      + "&k6=" + k6
      + "&k7=" + k7
      + "&k8=" + k8
      + "&k9=" + k9;
}

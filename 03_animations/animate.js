var canvas = document.getElementById('canvas')
var button = document.getElementById('start')
var stop = document.getElementById('stop')
var ctx = document.getElementById('canvas').getContext('2d')

var requestID;
var radius;
var growing = true;

function clear() {
    if (canvas.clientWidth / 2 == radius) {
        growing = false
    }
    if (radius <= 0) {
        growing = true
    }
    ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)
    if (growing) {
        radius += 1
    }else{
        radius -= 1
    }
    return true
}

function animate() {
    clear()
    make_circle()
}

function make_circle() {
    ctx.beginPath()
    ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI)
    ctx.stroke()
    ctx.fill()
}

button.addEventListener('click', window.requestAnimationFrame(animate))
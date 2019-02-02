/*
StuyNaught - Daniel Gelfand and Ahnaf Hasan
SoftDev2 pd6
K#02 -- Connecting the Dots
2019-02-04 M
*/

var canvas = document.getElementById('playground')
var ctx = canvas.getContext('2d')

var clear = document.getElementById('clear')


var prev_Pos = []

var dot = function make_dot(x, y) {
    ctx.fillStyle = "#abcdef"
    if (prev_Pos == []) { return }
    console.log("here")
    ctx.beginPath()
    ctx.moveTo(x, y)
    ctx.lineTo(prev_Pos[0], prev_Pos[1])
    ctx.stroke()
    ctx.beginPath()
    ctx.ellipse(x, y, 5, 5, 360, 0, 360)
    ctx.ellipse(prev_Pos[0], prev_Pos[1], 5, 5, 360, 0, 360)
    console.log("there")
    prev_Pos = [x, y]
    ctx.fill()
}

var cls = function c() {
    ctx.fillStyle = "#ffffff"
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    prev_Pos = []
    return true
}

canvas.addEventListener('click', function(e) {
    dot(e.offsetX, e.offsetY)
})

clear.addEventListener('click', cls )

canvas.oncontextmenu = function(e) {
    e.preventDefault()
    prev_Pos = []
    dot(e.offsetX, e.offsetY)
}
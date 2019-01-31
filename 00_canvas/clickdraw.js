/* 
Ahnaf Hasan
SoftDev2 pd06
K#00 -- I See a Red Door...
2019-1-30
*/

var c = document.getElementById('slate')
var context = c.getContext("2d")
var cls = document.getElementById("clear")
var s = document.getElementById('switch')
// var col = document.getElementById('color')

var do_rect = true

var clear = function clr_canvas() {
    context.fillStyle = "#ffffff"
    context.fillRect(0, 0, c.width, c.height)
    return true
}

var rect = function make_rect(x, y) {
    // console.log(col)
    context.fillStyle = "#000000"
    context.fillRect(x, y, 100, 200)
    return true
}

var dot = function mk_dt(x, y) {
    // console.log(col)
    context.fillStyle = "#0000ff"
    console.log("making ellipse")
    context.beginPath()
    context.ellipse(x, y, 5, 5, 360, 0, 360)
    context.fill()
    console.log("ellipse made")
    return true
}

c.addEventListener('click', function(e) {
    if (do_rect) {
        rect(e.offsetX, e.offsetY)
    }else{
        dot(e.offsetX, e.offsetY)
    }
})

cls.addEventListener("click", clear )

s.addEventListener('click', function() {
    do_rect = !do_rect
    if (do_rect) {
        s.innerHTML = "Draw dot"
    }else{
        s.innerHTML = "Draw rect"
    }
})
var pic = document.getElementById('svgimage')
var cls = document.getElementById('clear')
var last_dot = []

var make_dot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle")
    c.setAttribute('cx', e.offsetX)
    c.setAttribute('cy', e.offsetY)
    var ld = [last_dot[0], last_dot[1]]
    last_dot = []
    last_dot.push(e.offsetX, e.offsetY)
    c.setAttribute('fill', "orange")
    c.setAttribute('stroke', "blue")
    c.setAttribute('r', '10')

    if (ld[0] != undefined) {
        var line = document.createElementNS('http://www.w3.org/2000/svg', 'line')
        line.setAttribute('x1', ld[0])
        line.setAttribute('y1', ld[1])
        line.setAttribute('x2', e.offsetX)
        line.setAttribute('y2', e.offsetY)
        line.setAttribute('style', 'stroke: red; stroke-width: 2;')
        pic.appendChild(line)
    }
    pic.appendChild(c)
}


var clear = function() {
    while (pic.hasChildNodes()) {
        pic.removeChild(pic.lastChild)
    }
    last_dot = []
}



pic.addEventListener('click', make_dot )

pic.addEventListener('contextmenu', function(e) {
    e.preventDefault()
    last_dot = []
})

cls.addEventListener('click', clear )
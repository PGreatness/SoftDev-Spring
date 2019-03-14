var svg = document.getElementById('svg')
var cls = document.getElementById('clear')
var mv = document.getElementById('move')
var requestID, moving = false
var add_dot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle")
    c.addEventListener('click', change_dot )
    if (e.target['nodeName'] == 'circle') { return }
    c.setAttribute('cx', e.offsetX)
    c.setAttribute('cy', e.offsetY)
    c.setAttribute('fill', "orange")
    c.setAttribute('stroke', "blue")
    c.setAttribute('r', '10')
    svg.appendChild(c)
}

/**
 * Changes the color of the dot that was clicked on
 * @param {MouseEvent} e a mouse primary click
 */
var change_dot = function(e) {
    if (e.target.getAttribute('fill') != "green") {
        e.target.setAttribute('fill', 'green')
        return
    }else{
        e.target.setAttribute('fill', 'orange')
        let x = Math.abs(Math.random() * (svg.clientWidth - 10))
        let y = Math.abs(Math.random() * (svg.clientHeight - 10))
        e.target.setAttribute('cx', x )
        e.target.setAttribute('cy', y )
    }
}

var move_dots = function() {
    window.cancelAnimationFrame(requestID)
    var w = svg.getAttribute('width')
    var h = svg.getAttribute('height')
    var elems = svg.children
    console.log(elems)
    for (i = 0; i < elems.length; i++) {
        var velX = 1
        var velY = 1
        var currElem = elems.item(i)
        console.log(currElem)
        var x = Number(currElem.getAttribute('cx'))
        var y = Number(currElem.getAttribute('cy'))
        var color = currElem.getAttribute('fill')
        var radius = Number(currElem.getAttribute('r'))
        console.log(`this is w & h: ${w}  ${h}`)
        if (x + radius + velX >= w || x + radius + velX <= 0) {
            velX = -velX
        }
        if (y + radius + velX >= h || y + radius + velY <= 0) {
            velY = -velY
        }
        currElem.setAttribute('cx', `${x + velX}`)
        currElem.setAttribute('cy', `${y + velY}`)
        currElem.setAttribute('fill', color)
        svg.replaceChild(currElem, elems.item(i))
    }
    requestID = window.requestAnimationFrame(move_dots)
}

var clear = function() {
    while (svg.hasChildNodes()) {
        svg.removeChild(svg.lastChild)
    }
}

svg.addEventListener('click', add_dot )

mv.addEventListener('click', function() {
    if (!moving) {
        move_dots()
        moving = true
    }else{
        window.cancelAnimationFrame(requestID)
        moving = false
    }
})

cls.addEventListener('click', clear )
/**
 * Ahnaf Hasan
 * SoftDev2 pd06
 * K10 -- Ask Circles [Change || Die]
 * 2019-03-13
 */

var svg = document.getElementById('svg')
var cls = document.getElementById('clear')
var mv = document.getElementById('move')
var requestID, moving = false
/**
 * Adds a dot to the SVG image. Dots can change color
 * @param {MouseEvent} e a primary mouse click
 */
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
 * Changes the color of the dot that was clicked on. Can also change location
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
/**
 * Moves dots across the SVG image.
 * Does not work. Dots glide along the edges.
 */
// NVM, NOT NEEDED

// var move_dots = function() {
//     window.cancelAnimationFrame(requestID)
//     var w = svg.getAttribute('width')
//     var h = svg.getAttribute('height')
//     var elems = svg.children
//     var vels = new Array(elems.length)
//     vels.fill([1, 1])
//     console.log(vels)
//     console.log(elems)
//     for (i = 0; i < elems.length; i++) {
//         var velX = vels[i][0]
//         var velY = vels[i][1]
//         var currElem = elems.item(i)
//         console.log(currElem)
//         var x = Number(currElem.getAttribute('cx'))
//         var y = Number(currElem.getAttribute('cy'))
//         var color = currElem.getAttribute('fill')
//         var radius = Number(currElem.getAttribute('r'))
//         console.log(`this is w & h: ${w}  ${h}`)
//         if (x + radius + velX >= w || x + radius + velX <= 0) {
//             vels[i][0] = -velX
//             console.log("vel changed x")
//         }
//         if (y + radius + velX >= h || y + radius + velY <= 0) {
//             vels[i][1] = -velY
//             console.log(`vel changed y`)
//         }
//         currElem.setAttribute('cx', `${x + vels[i][0]}`)
//         currElem.setAttribute('cy', `${y + vels[i][1]}`)
//         currElem.setAttribute('fill', color)
//         svg.replaceChild(currElem, elems.item(i))
//     }
//     requestID = window.requestAnimationFrame(move_dots)
// }

/**
 * Clears the SVG image
 */
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
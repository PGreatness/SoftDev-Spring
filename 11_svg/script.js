/**
 * Ahnaf Hasan
 * SoftDev2 pd06
 * K11 -- Ask Circles [Change || Die]...While on the Go
 * 2019-03-16
 */

var svg = document.getElementById('svg')
var cls = document.getElementById('clear')
var mv = document.getElementById('move')
var comm = document.getElementById('other')
var image = "https://cdn-images.threadless.com/threadless-shop/products/383/1272x920design_03.jpg?w=1272&h=920"
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
 * Works if no one clicks when it is moving, otherwise creates an error
 */

var move_dots = function() {
    window.cancelAnimationFrame(requestID)
    var w = svg.getAttribute('width')
    var h = svg.getAttribute('height')
    var elems = svg.children
    var size = Number(elems[0].getAttribute('r'))
    var vels = new Array(elems.length)
    var ballx = new Array(elems.length)
    var bally = new Array(elems.length)
    for (i = 0; i < elems.length; i++) {
        vels[i] = [1,1]
        ballx[i] = Number(elems[i].getAttribute('cx'))
        bally[i] = Number(elems[i].getAttribute('cy'))
    }
    var anim = function() {
        for (curr = 0; curr < elems.length; curr++) {
            elems = svg.children
            // console.log(elems)
            var replacer = document.createElementNS('http://www.w3.org/2000/svg', 'circle')
            replacer.setAttribute('fill', elems[curr].getAttribute('fill'))
            replacer.setAttribute('r', elems[curr].getAttribute('r'))
            replacer.setAttribute('stroke', elems[curr].getAttribute('stroke'))
            replacer.setAttribute('cx', ballx[curr])
            replacer.setAttribute('cy', bally[curr])
            replacer.addEventListener('click', change_dot )
            svg.replaceChild(replacer, elems[curr])
            ballx[curr] += vels[curr][0]
            bally[curr] += vels[curr][1]
            if (ballx[curr] + vels[curr][0] + size > w || ballx[curr] + vels[curr][0]<= 0) {
                vels[curr][0] *= -1
            }
            if (bally[curr] + vels[curr][1] + size > h || bally[curr] + vels[curr][1]<= 0) {
                vels[curr][1] *= -1
            }
        }
        requestID = window.requestAnimationFrame(anim)
    }
    anim()
}

/**
 * Moves the circles as 1 giant, homogenous group. We all move together.
 */
var communism = function() {
    window.cancelAnimationFrame(requestID)
    var w = svg.getAttribute('width')
    var h = svg.getAttribute('height')
    var elems = svg.children
    var size = Number(elems[0].getAttribute('r'))
    var vels = new Array(elems.length).fill([1, 1])
    var ballx = new Array(elems.length)
    var bally = new Array(elems.length)
    for (i = 0; i < elems.length; i++) {
        ballx[i] = Number(elems[i].getAttribute('cx'))
        bally[i] = Number(elems[i].getAttribute('cy'))
    }
    var anim = function() {
        for (curr = 0; curr < elems.length; curr++) {
            elems = svg.children
            // console.log(elems)
            var replacer = document.createElementNS('http://www.w3.org/2000/svg', 'circle')
            replacer.setAttribute('fill', elems[curr].getAttribute('fill'))
            replacer.setAttribute('r', elems[curr].getAttribute('r'))
            replacer.setAttribute('stroke', elems[curr].getAttribute('stroke'))
            replacer.setAttribute('cx', ballx[curr])
            replacer.setAttribute('cy', bally[curr])
            replacer.addEventListener('click', change_dot )
            svg.replaceChild(replacer, elems[curr])
            ballx[curr] += vels[curr][0]
            bally[curr] += vels[curr][1]
            if (ballx[curr] + vels[curr][0] + size > w || ballx[curr] + vels[curr][0]<= 0) {
                vels[curr][0] *= -1
            }
            if (bally[curr] + vels[curr][1] + size > h || bally[curr] + vels[curr][1]<= 0) {
                vels[curr][1] *= -1
            }
        }
        requestID = window.requestAnimationFrame(anim)
    }
    anim()
}
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
        var c = document.getElementsByTagName('h1')[0]
        c.innerHTML = "The world of the Dots"
        c = document.getElementsByTagName('h2')[0]
        c.innerHTML = "By Ahnaf Hasan"
        c = document.getElementsByTagName('body')[0]
        svg.style.border = '1px solid black'
        c.style.backgroundImage = 'none'
        window.cancelAnimationFrame(requestID)
        moving = false
    }
})

comm.addEventListener('click', function() {
    if (!moving) {
        var c = document.getElementsByTagName('h1')[0]
        c.innerHTML = "The Communist Manifesto"
        c = document.getElementsByTagName('h2')[0]
        c.innerHTML = "By Karl Marx"
        c = document.getElementsByTagName('body')[0]
        c.style.backgroundImage = `url(${image})`
        c.style.backgroundRepeat = 'no-repeat stretch'
        c.style.backgroundSize = 'cover'
        svg.style.border = '3px solid yellow'
        communism()
        moving = true
    }else{
        window.cancelAnimationFrame(requestID)
        moving = false
    }
})

cls.addEventListener('click', clear )
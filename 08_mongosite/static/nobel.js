var ip = document.getElementById('ip')
var but = document.getElementById('s')
console.log(but)
var topic = document.getElementsByName('topic').item(0)
var err = document.getElementById("e")
console.log(res)
function sub() {
    if (ip.innerHTML == "") {
        console.log("got")
        err.innerHTML = "IP not provided<br>"
        err.style.color = "red"
    }
    if (topic.innerHTML == "") {
        console.log("as")
        err.innerHTML = err.innerHTML + "Topic left blank"
        err.style.color = "red"
    }
    console.log(topic)
    console.log(ip)
}

but.addEventListener('click', sub )
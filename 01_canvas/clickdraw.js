/*
StuyNaught - Daniel Gelfand and Ahnaf Hasan
SoftDev2 pd6
K#01 -- ...and I want to Paint It Better
2019-02-01 F
*/

// 0 is dot mode
// 1 is box mode
var mode = 0;

// Switch between modes
var toggle = function(){

  var btn = document.getElementById("tgl");

  if(mode == 0){
    mode = 1;
    alert("Switching to box mode");
    btn.innerHTML = "Box Mode - Toggle"
  }
  else{
    mode = 0;
    alert("Switching to dot mode");
    btn.innerHTML = "Dot Mode - Toggle"
  }
}

var clr = function(){

  location.reload();

}

var draw = function(event){
  //alert("drawing");
  //console.log(event);
  event.preventDefault();
  var canvas = document.getElementById("slate");
  var ctx = canvas.getContext("2d");
  ctx.fillStyle = "#ff0000"; //red color

  // if dot mode
  if(mode == 0){
    //alert("drawing dot");
    ctx.beginPath(); //begins a new path for drawing
    /*
    offsetX provides the offset in the X coordinate of the
    mouse pointer between the event and padding of target.

    offsetY has the same function as offsetX but for the Y coordinate
    */
    ctx.ellipse(event.offsetX, event.offsetY , 10 , 10, Math.PI , 0, 2 * Math.PI);
    ctx.fill();
  }
  // rect mode
  else{
    //alert("drawing box")
    ctx.fillRect(event.offsetX, event.offsetY , 50, 100)
  }

}

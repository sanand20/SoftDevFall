var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling...");
  if(mode === "rect"){
    mode = "circ";
  }
  else{
    mode = "rect";
  }
};

var drawRect = function(e){
  var mouseX = e.clientX;
  var mouseY = e.clientY;
  ctx.fillRect(mouseX,mouseY, 20, 50);
  console.log("mouse click registered at ", mouseX, mouseY);
};

var drawCircle = (e) => {
  var mouseX = e.clientX + e.offsetX;
  var mouseY =  e.offsetY-e.clientY;
  console.log("mouse click registered at", mouseX, mouseY);
};
var draw = (e) => {
  if(mode === "rect"){;
    drawRect(e);
  }
  else{drawCircle(e);}
};

// var wipeCanvas = () => {
//
// }
//
 c.addEventListener("click", draw);
// var bToggler = document.;
// bToggler. ;
// var clearB = ;
// clearB.;

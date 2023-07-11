var canvas = document.getElementById("canvasAerop");
canvas.addEventListener("mousedown", function(event) {
    canvas.style.cursor = "default";
    var ctx = canvas.getContext('2d'); 
    ctx.beginPath();
    var x = event.clientX - ctx.canvas.offsetLeft;
    var y = event.clientY - ctx.canvas.offsetTop;
    //ctx.arc(x,y,5,0, 2*Math.PI, true);
    //ctx.fill();
    console.log("x = " + x + ", y = " + y);
  });

function buton1() {
  var canvas = document.getElementById("canvasAerop");
  canvas.style.cursor = "crosshair"; 

}


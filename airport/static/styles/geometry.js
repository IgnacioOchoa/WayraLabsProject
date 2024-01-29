var canvas = document.getElementById("canvasAerop");
var ctx = canvas.getContext('2d');
var drawLine;
var lineStarted = false;
var rect = canvas.getBoundingClientRect();

var points = [];
var lines = [];
var currentLine;
var baseLineColor = 'rgb(252, 186,3)';

function Line(xRoot, yRoot) {
  this.x1 = xRoot;
  this.x2 = xRoot;
  this.y1 = yRoot;
  this.y2 = yRoot;
  this.color = baseLineColor;
}

Line.prototype.updateTip = function(xTip, yTip) {
  this.x2 = xTip;
  this.y2 = yTip;
}

Line.prototype.draw = function() {
  ctx.beginPath();
  ctx.moveTo(this.x1, this.y1);
  ctx.lineTo(this.x2, this.y2);
  ctx.strokeStyle = this.color;
  ctx.lineWidth = 5;
  ctx.stroke();
}  

function mouseClick(event) {
    canvas.style.cursor = "default";
    ctx.beginPath();
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
    ctx.moveTo(x,y);
    ctx.arc(x,y,4,0,Math.PI*2);
    ctx.strokeStyle = 'rgb(66,135,245)';
    ctx.lineWidth = 5;
    ctx.stroke();
    if (!lineStarted) {
      lineStarted  = true;
      currentLine = new Line(x,y);
      console.log("Line started")
    }
    else {
      lineStarted = false;
      lines.push(currentLine);
    }
}

function mouseCollisionWithLine(mouseX, mouseY, line) {
  console.log("mouse X = " + mouseX, "  line.x1 = " + line.x1 + "  line.x2 = " + line.x2);
  console.log("mouse Y = " + mouseY, "  line.y1 = " + line.y1 + "  line.y2 = " + line.y2);

  if(mouseX < Math.min(line.x1,line.x2) ||  mouseX > Math.max(line.x1, line.x2)) return false;
  if(mouseY < Math.min(line.y1,line.y2) ||  mouseY > Math.max(line.y1, line.y2)) return false;
  var vecLineX = line.x2 - line.x1;
  var vecLineY = line.y2 - line.y1;
  var lengthLine = Math.sqrt(Math.pow(vecLineX,2)+Math.pow(vecLineY,2));
  var mouseRelX = mouseX - line.x1;
  var mouseRelY = mouseY - line.y1;
  var lengthMouse = Math.sqrt(Math.pow(mouseRelX,2)+Math.pow(mouseRelY,2));
  var cosAlpha = (mouseRelX*vecLineX + mouseRelY*vecLineY)/(lengthLine * lengthMouse);
  var normDist = lengthMouse*Math.sin(Math.acos(cosAlpha));
  console.log("Distance = " + normDist);
  if (Math.abs(normDist) < 10) return true;
  else return false;
}

canvas.addEventListener("mousedown", mouseClick);
canvas.addEventListener("mousemove", (event) => {
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  if(lineStarted) {
    currentLine.updateTip(x,y);
    console.log("Line moved");
  }
  else {
    for (let i=0; i<lines.length; i++) {
      if(mouseCollisionWithLine(x,y,lines[i])) {
	lines[i].color = 'rgb(252,61,3)';
      }
      else { lines[i].color = baseLineColor;}
    }
  }
});

function buton1() {
  canvas.style.cursor = "crosshair"; 

}

function loop() {
  window.requestAnimationFrame(loop);
  ctx.fillStyle = '#e6f5ea';
  ctx.fillRect(0,0,canvas.width, canvas.height);
  lines.map(function(line){line.draw();});
  if(lineStarted) {
    currentLine.draw();
  }
}

loop();


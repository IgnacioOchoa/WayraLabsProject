var canvas = document.getElementById("canvasAerop");
var ctx = canvas.getContext('2d');
var drawLine;
var rect = canvas.getBoundingClientRect();
//var visibleX = 2000;
//var visibleY = 1000;

var points = [];
var lines = [];
var nodes = [];
var links = [];
var currentLine;
var baseLineColor = '#225887';
let nodeColor = "#444647";
let lineHighlihtColor = "rgb(252,61,3)";
let backgroundFill = '#e6f5ea';
let linkColor = '#999c9e';

dataElement1 = document.currentScript.nextElementSibling;
dataElement2 = dataElement1.nextElementSibling;
const dataNodes = JSON.parse(dataElement1.textContent);
const dataLinks = JSON.parse(dataElement2.textContent);

console.log("data: ", dataNodes);
console.log("dataLinks: ", dataLinks);

for (node of dataNodes) {
  addNode(node);
}

for (link of dataLinks) {
  addLink(link);
}

let [visibleX, visibleY] = calculateBoundingRect();

function addNode(node) {
  nodes.push(new Node(node[0],node[1]));
}

function addLink(link) {
  links.push(new Link(link[0], link[1], link[2], link[3], link[4]));
}

function calculateBoundingRect(){
  let xMin = Infinity;
  let xMax = -Infinity;
  let yMin = Infinity;
  let yMax = -Infinity;
  for(let n of nodes) {
    if (n.x < xMin) xMin = n.x;
    else if (n.x > xMax) xMax = n.x;
    if (n.y < yMin) yMin = n.y;
    else if (n.y > yMax) yMax = n.y;
  }
  let visibleX = 2*Math.max(Math.abs(xMin), Math.abs(xMax))*1.1;
  let visibleY = 2*Math.max(Math.abs(yMin), Math.abs(yMax))*1.1;
  return [visibleX, visibleY];
}

 
function Line(xRoot, yRoot) {
  this.x1 = xRoot;
  this.x2 = xRoot;
  this.y1 = yRoot;
  this.y2 = yRoot;
  this.color = baseLineColor;
}

function Node(x,y) {
  this.x = x;
  this.y = y;
  this.color = nodeColor;
}

function Link(x1,y1,x2,y2,width) {
  this.x1 = x1;
  this.y1 = y1;
  this.x2 = x2;
  this.y2 = y2;
  this.width = width;
  this.color = linkColor; 
}


Node.prototype.draw = function() {
  let posX = this.x/(visibleX) * canvas.width + canvas.width/2;
  let posY = this.y/(visibleY) * canvas.height + canvas.height/2;
  ctx.beginPath();
  ctx.arc(posX, posY, 5, 0, Math.PI*2);
  ctx.strokeStyle = nodeColor ;
  ctx.lineWidth = 3;
  ctx.stroke();
}

Link.prototype.draw = function(mode) {
  let posX1 = this.x1/(visibleX) * canvas.width + canvas.width/2;
  let posY1 = this.y1/(visibleY) * canvas.height + canvas.height/2;
  let posX2 = this.x2/(visibleX) * canvas.width + canvas.width/2;
  let posY2 = this.y2/(visibleY) * canvas.height + canvas.height/2;
  ctx.beginPath();
  ctx.moveTo(posX1,posY1);
  ctx.lineTo(posX2,posY2);
  if(mode == 'shape') {
  	ctx.strokeStyle = this.color; //ctx.lineWidth = 5;
  	ctx.lineWidth = this.width;
  }
  else if (mode == 'line') {
  	ctx.strokeStyle = "#FFFFFF";
  	ctx.lineWidth = 2;
  }
  ctx.stroke();
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
    console.log("mouseClick function"); 
}

function mouseCollisionWithLine(mouseX, mouseY, line) {
  //console.log("mouse X = " + mouseX, "  line.x1 = " + line.x1 + "  line.x2 = " + line.x2);
  //console.log("mouse Y = " + mouseY, "  line.y1 = " + line.y1 + "  line.y2 = " + line.y2);

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
  //console.log("Distance = " + normDist);
  if (Math.abs(normDist) < 10) return true;
  else return false;
}

canvas.addEventListener("mousedown", mouseClick);
canvas.addEventListener("mousemove", (event) => {
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  //if(mouseCollisionWithLine(x,y,lines[i])) {
  //lines[i].color = lineHighlihtColor;
  // }
  // else { lines[i].color = baseLineColor;}
  // }
  //}
});

function loop() {
  window.requestAnimationFrame(loop);
  ctx.fillStyle = backgroundFill;
  ctx.fillRect(0,0,canvas.width, canvas.height);
  links.map(function(link){link.draw('shape');});
  lines.map(function(line){line.draw();});
  links.map(function(link){link.draw('line');});
  nodes.map(function(node){node.draw();});
}

loop();


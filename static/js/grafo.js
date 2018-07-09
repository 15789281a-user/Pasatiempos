var canvas = document.getElementById("myCanvas1");
var ctx = canvas.getContext("2d");

ctx.lineWidth = 4;

ctx.beginPath();
ctx.arc(220, 220, 200, 0, 2*Math.PI);
ctx.stroke()

ctx.beginPath();
ctx.arc(220, 220, 90, 0, 2*Math.PI);
ctx.stroke()

ctx.moveTo(142, 40);
ctx.lineTo(210, 125);
ctx.stroke();

ctx.moveTo(290, 40);
ctx.lineTo(230, 125);
ctx.stroke();

ctx.moveTo(20, 215);
ctx.lineTo(130, 260);
ctx.stroke();

ctx.moveTo(140, 270);
ctx.lineTo(120, 380);
ctx.stroke();

ctx.moveTo(300, 260);
ctx.lineTo(400, 220);
ctx.stroke();

ctx.moveTo(300, 260);
ctx.lineTo(350, 400);
ctx.stroke();


var canvas = document.getElementById("myCanvas2");
var ctx = canvas.getContext("2d");

ctx.lineWidth = 4;

ctx.beginPath();
ctx.arc(220, 220, 200, 0, 2*Math.PI);
ctx.stroke()

ctx.beginPath();
ctx.arc(220, 220, 90, 0, 2*Math.PI);
ctx.stroke()

ctx.moveTo(142, 40);
ctx.lineTo(210, 125);
ctx.stroke();

ctx.moveTo(290, 40);
ctx.lineTo(230, 125);
ctx.stroke();

ctx.moveTo(20, 215);
ctx.lineTo(130, 260);
ctx.stroke();

ctx.moveTo(140, 270);
ctx.lineTo(120, 380);
ctx.stroke();

ctx.moveTo(300, 260);
ctx.lineTo(400, 220);
ctx.stroke();

ctx.moveTo(300, 260);
ctx.lineTo(350, 400);
ctx.stroke();

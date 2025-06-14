POINT_WIDTH = 5
POINT_HEIGHT = 5
MULTIPLIER = 500


function getColor(fraction){
  console.log(fraction);

  if (fraction == "WARDENS"){
    return "red";
  }

  else if (fraction == "COLONIALS"){
    return "blue";
  }
  else if (fraction == "NONE"){
    return "#616161";
  }
}

function drawPoint(ctx, point, color){
  ctx.fillStyle = color;
  ctx.fillRect(point.x * MULTIPLIER, point.y * MULTIPLIER, POINT_WIDTH, POINT_HEIGHT);
}

// function drawPoint(ctx, point, color) {
//   const canvas = ctx.canvas;
//   const x = point.x * canvas.width;
//   const y = point.y * canvas.height;
//
//   ctx.fillStyle = color;
//   // ctx.fillRect(x - 2, y - 2, 4, 4); // 4x4 piksele, z przesunięciem na środek
//   ctx.fillRect(point.x * MULTIPLIER, point.y * MULTIPLIER, POINT_WIDTH, POINT_HEIGHT);
// }


async function abc () {
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");

  // const baseUrl = "https://war-service-live.foxholeservices.com/api";
  const baseUrl = "http://localhost:8000/";

  const response = await fetch(baseUrl);
  const data = await response.json();
  console.log(data);
  const newData = data.data.map(el => ({...el, x: Number(el.x.toFixed(2)), y: Number(el.y.toFixed(2))}))
  // const newData = data.data.map(el => el)
  console.log(newData);

  data.data.forEach(point => {
    const color = getColor(point.teamId);
    drawPoint(ctx, point, color);
  });



  // ctx.fillStyle = "green";
  // ctx.fillRect(0, 0, 150, 75);
  console.log("strarting.")
}


window.onload = abc

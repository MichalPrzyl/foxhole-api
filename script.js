async function abc () {

    const baseUrl = "https://war-service-live.foxholeservices.com/api";

    const response = await fetch(baseUrl);
    console.log(response);

    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "green";
    ctx.fillRect(0, 0, 150, 75);
    console.log("strarting.")
}


window.onload = abc

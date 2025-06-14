async function abc () {

    // const baseUrl = "https://war-service-live.foxholeservices.com/api";
    const baseUrl = "http://localhost:8000/";

    const response = await fetch(baseUrl);
    const data = await response.json();
    console.log(data);

    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "green";
    ctx.fillRect(0, 0, 150, 75);
    console.log("strarting.")
}


window.onload = abc

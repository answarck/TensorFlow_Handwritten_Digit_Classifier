const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const resetButton = document.getElementById("reset");
const predictButton = document.getElementById("predict");
let isDrawing = false;
let csrftoken = document.getElementById("csrf-token").value;

ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.lineWidth = 10;
ctx.lineCap = "round";
ctx.strokeStyle = "black";

canvas.addEventListener("mousedown", () => isDrawing = true);
canvas.addEventListener("mouseup", () => isDrawing = false);
canvas.addEventListener("mouseleave", () => isDrawing = false);

canvas.addEventListener("mousemove", (event) => {
    if (!isDrawing) return;
    let rect = canvas.getBoundingClientRect();
    let x = event.clientX - rect.left;
    let y = event.clientY - rect.top;
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
});

resetButton.addEventListener("click", () => {
    document.getElementById("prediction_box").innerText = "Draw a Number";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
});

async function predict() {
    let imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    let grayscaleImage = [];

    for (let i = 0; i < 28; i++) {
        let row = [];
        for (let j = 0; j < 28; j++) {
            let index = (i * 10 * canvas.width + j * 10) * 4;
            let pixel = imageData.data[index]; 
            row.push(pixel < 128 ? 1 : 0);
        }
        grayscaleImage.push(row);
    }

    try {
        let response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(grayscaleImage)
        });

        let data = await response.json();
        document.getElementById("prediction_box").innerText = "The number is: " +  data.prediction;
        console.log("Prediction:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

predictButton.addEventListener("click", predict);

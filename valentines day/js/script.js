const noBtn = document.getElementById("noBtn");
const yesBtn = document.getElementById("yesBtn");

/* YES BUTTON */
yesBtn.addEventListener("click", () => {
    window.location.href = "yes.html";
});

/* NO BUTTON ESCAPE */
noBtn.addEventListener("mouseover", () => {
    const x = Math.random() * (window.innerWidth - noBtn.clientWidth);
    const y = Math.random() * (window.innerHeight - noBtn.clientHeight);

    noBtn.style.left = `${x}px`;
    noBtn.style.top = `${y}px`;
});

/* GENERATE FLOATING HEARTS */

const heartsContainer = document.querySelector(".hearts-container");

function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (Math.random() * 3 + 3) + "s";

    heartsContainer.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 6000);
}

setInterval(createHeart, 300);

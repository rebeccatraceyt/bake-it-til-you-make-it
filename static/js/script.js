// Important Note & Copyright
function showDisclaimer() {
    const disclaimer = document.getElementById("disclaimer");
    disclaimer.classList.toggle("hide-disclaimer");
}

document.getElementById("date-text").textContent = new Date().getFullYear();
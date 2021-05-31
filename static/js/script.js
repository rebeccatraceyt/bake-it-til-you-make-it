// Important Note & Copyright
function showDisclaimer() {
    const disclaimer = document.getElementById("disclaimer");
    disclaimer.classList.toggle("hide-disclaimer");
}

function hideDisclaimer() {
    const disclaimer = document.getElementById("disclaimer");
    disclaimer.classList.toggle("hide-disclaimer");
}

document.getElementById("date-text").textContent = new Date().getFullYear();

$(function () {
    /*Changes background of navigation bar on scroll for UX purposes.
        Sourced from https://jsfiddle.net/we9L9h2r/ */
    $(document).scroll(function () {
        var $nav = $("#scroll-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});
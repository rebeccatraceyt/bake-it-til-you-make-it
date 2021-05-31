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
    /* Changes background of navigation bar on scroll for UX purposes.
        Sourced from https://jsfiddle.net/we9L9h2r/ */
    $(document).scroll(function () {
        var $nav = $("#scroll-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

$('#password, #confirm_password').on('keyup', function () {
    /* Confirm passwords match
        Sourced from https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518 */
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#message').html('Passwords match!').css('color', 'green');
  } else 
    $('#message').html('Passwords do not match, try again').css('color', 'red');
});
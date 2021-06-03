// Display Disclaimer Information in Footer
function showDisclaimer() {
    const disclaimer = document.getElementById("disclaimer");
    disclaimer.classList.toggle("hide-disclaimer");
}

function hideDisclaimer() {
    const disclaimer = document.getElementById("disclaimer");
    disclaimer.classList.toggle("hide-disclaimer");
}

// Get Current Year
document.getElementById("date-text").textContent = new Date().getFullYear();

// Change Navbar on scroll - UX purposes
//      Sourced from https://jsfiddle.net/we9L9h2r/ 
$(function () {
    $(document).scroll(function () {
        var $nav = $("#scroll-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

// Confirm Passwords Match
//      Sourced from https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518
$('#password, #confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#message').html('Passwords match!').css('color', 'green');
  } else 
    $('#message').html('Passwords do not match, try again').css('color', 'red');
});

// Checking if form is valid - reference: https://codepen.io/tetnuc/pen/gRqOEO
$('#suggestionForm').validate({
    rules: {
        name: {
            required: true
        },
        email: {
            required: true
        },
        message: {
            required: true
        }
    },
    messages: {
        name: {
            required: "Please complete all fields"
        },
        email: {
            required: "Please complete all fields"
        },
        message: {
            required: "Please complete all fields"
        }
    },

});

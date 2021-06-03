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

// EmailJs Function
$('#form-submit').click(function (event) {
    // reference: https://stackoverflow.com/questions/5127813/call-mvc-3-client-side-validation-manually-for-ajax-posts
    event.preventDefault();
    if($('#suggestionForm').valid()) {
        Swal.fire({
            icon: 'success',
            title: 'Thank You!',
            text: 'Your message has been received',
            showConfirmButton: false,
            timer: 1500
        });
        $('#form-modal').modal('hide');
        sendMail();
    }
});

function sendMail(){
    // reference: CI tutorial and https://www.youtube.com/watch?v=x7Ewtay0Q78
    let tempParams = {
        user_name: document.getElementById("name").value,
        user_email: document.getElementById("email").value,
        user_msg: document.getElementById("message").value,
    };
    emailjs.send('service_kqnk8br', 'template_tif41mk', tempParams);
}
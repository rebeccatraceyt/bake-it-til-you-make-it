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

/* Change Navbar on scroll - UX purposes
    Sourced from https://jsfiddle.net/we9L9h2r/ */
$(function () {
    $(document).scroll(function () {
        var $nav = $("#scroll-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

/* Confirm Passwords Match
    Sourced from https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518 */
$('#password, #confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#message').html('Passwords match!').css('color', 'green');
  } else 
    $('#message').html('Passwords do not match').css('color', 'red');
});

/* Show Image Preview
    Sourced from http://jsfiddle.net/2d7axmdr */
function recipeImg() {
    // For recipes
    $(".img-container").css("display", "flex")
    var url = $("#recipe_img").val()
    $('.img-preview').attr('src',url)
}
function userImg() {
    // For users
    $(".img-container").css("display", "flex")
    var url = $("#user_img").val()
    $('.img-preview').attr('src',url)
}

/* Checking if form is valid 
    Sourced from https://codepen.io/tetnuc/pen/gRqOEO */
$('#suggestionForm').validate({
    rules: {
        uname: {
            required: true
        },
        uemail: {
            required: true
        },
        umessage: {
            required: true
        }
    },
    messages: {
        uname: {
            required: "Please complete all fields"
        },
        uemail: {
            required: "Please complete all fields"
        },
        umessage: {
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
        user_name: document.getElementById("uname").value,
        user_email: document.getElementById("uemail").value,
        user_msg: document.getElementById("umessage").value,
    };
    emailjs.send('service_kqnk8br', 'template_tif41mk', tempParams);
}


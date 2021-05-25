
$(function () {
    /* Changes background of navigation bar on scroll for UX purposes.
      Sourced from https://jsfiddle.net/we9L9h2r/ */
    $(document).scroll(function () {
        var $nav = $(".scroll-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});
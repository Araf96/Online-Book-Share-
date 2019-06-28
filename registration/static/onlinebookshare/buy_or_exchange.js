var main = function() {
  /* Push the body and the nav over by 285px over */
  var isOpened = false;

  $('.menu').on("mouseover", function() {
    clearInterval(walk_through);
  });

  $('.icon-menu').on("mouseover", function() {
    clearInterval(walk_through);
  });
  $('.icon-menu').click(function() {
    isOpened = true;

    $('.menu').animate({
      left: "0px"
    }, 200);

    $('body').animate({
      left: "285px"
    }, 200);
  });

  /* Then push them back */
  $('.icon-close').on("mouseover", function() {
    clearInterval(walk_through);
  });
  $('.icon-close').click(function() {
    isOpened = false;

    $('.menu').animate({
      left: "-285px"
    }, 200);

    $('body').animate({
      left: "0px"
    }, 200);
  });

  // Walkthrough the menu
  var walk_through = setInterval(function() {
      if (!isOpened){
        $('.icon-menu').trigger('click');
      }
      else if (isOpened){
        $('.icon-close').trigger('click');
      }
    }, 3000);
};

$(document).ready(main);

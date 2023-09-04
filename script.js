/* Inspired by this pen by Pieter Biesemans https://codepen.io/pieter-biesemans/pen/BQBWXX and My Mother Before Me project http://mymotherbeforeme.com/ */


var $scroller = $('.scroller');
// assign click handler
$('button').on('click', function () {       
    // get the partial id of the div to scroll to
    var divIdx = $('input').val();          
    
    // retrieve the jquery ref to the div
    var scrollTo = $('#d'+divIdx)           
        // change its bg
        .css('background', 'white')          
        // retrieve its position relative to its parent
        .position().left;                   
    console.log(scrollTo);
    // simply update the scroll of the scroller
    // $('.scroller').scrollLeft(scrollTo); 
    // use an animation to scroll to the destination
    $scroller
      .animate({'scrollLeft': scrollTo}, 500);    
});
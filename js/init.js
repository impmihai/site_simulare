(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $(window).on('scroll', function (event) {
        var scroll = $(this).scrollTop()
        if(scroll > 100) {
            $('#nav').removeClass('transparent-grey')
            $('#nav').addClass('white-black-text')
        } else {
            $('#nav').removeClass('white-black-text')
            $('#nav').addClass('transparent-grey')
        }
    });

    $('#nav a').on('click', function(e){
    e.preventDefault();
    var target = this.hash;
	var $target = $(target);
    if($target.length)
        $('html, body').stop().animate({
    	    'scrollTop': $target.offset().top
    	}, 900, 'swing');
});
  }); // end of document ready
})(jQuery); // end of jQuery name space

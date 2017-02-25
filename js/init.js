(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.collapsible').collapsible();

    $('#inscriere').load('pages/inscriere.html')
    $('#probe').load('pages/probe.html')
    $('#faq').load('pages/faq.html')
    $('#feedback').load('pages/feedback.html')
    $('#contact').load('pages/contact.html')

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
    $('window.hash')
    $('#nav a').on('click tap', function(e){
        var target = this.hash;
    	var $target = $(target);
        if($target.length)
            $('html, body').stop().animate({
        	    'scrollTop': $target.offset().top
        	}, 600, 'swing');
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space

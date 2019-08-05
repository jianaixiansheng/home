(function ($) {
 "use strict";

    /*--------------------------
    lightbox
    ---------------------------- */
    /*activity indicator functions*/
    var activityIndicatorOn = function(){
        $('<div id="imagelightbox-loading"><div></div></div>').appendTo('body');
    };
    var activityIndicatorOff = function(){
        $('#imagelightbox-loading').remove();
    };

    /*close button functions*/
    var closeButtonOn = function(instance){
        $('<button type="button" id="imagelightbox-close" title="Close"></button>').appendTo('body').on('click touchend', function(){ $(this).remove(); instance.quitImageLightbox(); return false; });
    };
    var closeButtonOff = function(){
        $('#imagelightbox-close').remove();
    };

    /*overlay*/
    var overlayOn = function(){$('<div id="imagelightbox-overlay"></div>').appendTo('body');};
    var overlayOff = function(){$('#imagelightbox-overlay').remove();};

    /*caption*/
    var captionOff = function(){$('#imagelightbox-caption').remove();};
    var captionOn = function(){
        var description = $('a[href="' + $('#imagelightbox').attr('src') + '"] img').attr('alt');
        if(description.length)
            $('<div id="imagelightbox-caption">' + description +'</div>').appendTo('body');
    };

    /*arrows*/
    var arrowsOn = function(instance, selector) {
        var $arrows = $('<button type="button" class="imagelightbox-arrow imagelightbox-arrow-left"><i class="fa fa-chevron-left"></i></button><button type="button" class="imagelightbox-arrow imagelightbox-arrow-right"><i class="fa fa-chevron-right"></i></button>');
        $arrows.appendTo('body');
        $arrows.on('click touchend', function(e) {
            e.preventDefault();
            var $this = $(this);
            if( $this.hasClass('imagelightbox-arrow-left')) {
                instance.loadPreviousImage();
            } else {
                instance.loadNextImage();
            }
            return false;
        });
    };
    var arrowsOff = function(){$('.imagelightbox-arrow').remove();};

    var selectorG = '.lightbox';
    if($(selectorG).length){
        var instanceG = $(selectorG).imageLightbox({
            quitOnDocClick: false,
            onStart:        function() {arrowsOn(instanceG, selectorG);overlayOn(); closeButtonOn(instanceG);},
            onEnd:          function() {arrowsOff();captionOff(); overlayOff(); closeButtonOff(); activityIndicatorOff();},
            onLoadStart:    function() {captionOff(); activityIndicatorOn();},
            onLoadEnd:      function() {$('.imagelightbox-arrow').css('display', 'block');captionOn(); activityIndicatorOff();}
        });
    }




    <!-- Welcome Tabs -->
    /* jQuery activation and setting options for the tabs*/

    var tabbedNav = $("#tabbed-nav").zozoTabs({
        orientation: "horizontal",
        theme: "silver",
        position: "top-left",
        size: "medium",
        animation: {
            duration: 600,
            easing: "easeOutQuint",
            effects: "fade"
        },
        defaultTab: "tab1"
    });

    /* Changing animation effects*/
    $("#config input.effects").change(function () {
        var effects = $('input[type=radio]:checked').attr("id");
        tabbedNav.data("zozoTabs").setOptions({ "animation": { "effects": effects } });
    });



    /*--------------------------
    preloader
    ---------------------------- */
	$(window).on('load',function(){
		var pre_loader = $('#preloader')
	pre_loader.fadeOut('slow',function(){$(this).remove();});
	});

/*---------------------
  venobox
--------------------- */
	var veno_box = $('.venobox');
	veno_box.venobox();

    $('.datepicker').Zebra_DatePicker();
    $('.datepicker2').Zebra_DatePicker();

/*------------------------------------
 search option
------------------------------------- */
    $('.search-option').hide();
    $(".main-search").on('click', function(){
        $('.search-option').animate({
            height:'toggle',
        });
    });
/*---------------------
 TOP Menu Stick
--------------------- */
var windows = $(window);

windows.on('scroll', function() {
    var $topG = $('.finance-navbar').offset().top;
    if ( $(window).scrollTop() > $topG + 66 ) {
        $('.finance-navbar').addClass('affix-coming')
    }
    else {
        $('.finance-navbar').removeClass('affix-coming')
    }
    $('.finance-navbar').affix({
        offset: {
            top: $topG + 150
        }
    })
});



/*----------------------------
 jQuery MeanMenu
------------------------------ */
    var navigation = $('.main-navigation-wrapper');
        if ($('#main-navigation-wrapper .navbar-nav li .dropdown-submenu').length) {
            $('#main-navigation-wrapper .navbar-nav li .dropdown-submenu').parent('li').children('a').append(function() {
                return '<button class="dopdown-nav-toggler"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>';
            });
            $('#main-navigation-wrapper .navbar-nav .dopdown-nav-toggler').on('click', function() {
                if($(this).hasClass("dopdown-nav-toggler-active"))
                {
                    $(this).removeClass("dopdown-nav-toggler-active");
                    $('#main-navigation-wrapper .navbar-nav li ul.dropdown-submenu').fadeOut();
                }
                else
                {
                    $('#main-navigation-wrapper .navbar-nav .dopdown-nav-toggler').removeClass("dopdown-nav-toggler-active");
                    $('#main-navigation-wrapper .navbar-nav li ul.dropdown-submenu').hide();
                    var Self = $(this);
                    Self.addClass("dopdown-nav-toggler-active");
                    Self.parent().parent().children('.dropdown-submenu').slideToggle();
                }

                return false;
            });


        }



        if ($('.mixit-gallery').length) {
            $('.mixit-gallery').mixItUp();
        }



/*--------------------------
 scrollUp
---------------------------- */
	$.scrollUp({
		scrollText: '<i class="fa fa-angle-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});


    $('.dk-select').click(function(){
        $(this).find('.dk-select-options').toggle();
    });


    /*----------------------------
     Counter js active
    ------------------------------ */
    var count = $('.counter');
    count.counterUp({
		delay: 40,
		time: 3000
	});

/*--------------------------
 collapse
---------------------------- */
	var panel_test = $('.panel-heading a');
	panel_test.on('click', function(){
		panel_test.removeClass('active');
		$(this).addClass('active');
	});
/*--------------------------
 Parallax
---------------------------- */
    var parallaxeffect = $(window);
    parallaxeffect.stellar({
        responsive: true,
        positionProperty: 'position',
        horizontalScrolling: false
    });
/*--------------------------
 MagnificPopup
---------------------------- */
    $('.video-play').magnificPopup({
        type: 'iframe'
    });

/*--------------------------
     slider carousel
---------------------------- */
    var intro_carousel = $('.intro-carousel');
    intro_carousel.owlCarousel({
        loop:true,
        nav:true,
        autoplay:true,
        dots:false,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });



/*--------------------------
     Project carousel
---------------------------- */
	var Project_carousel = $('.project-carousel');
	Project_carousel.owlCarousel({
        loop:true,
        nav:true,
        autoplay:true,
        dots:true,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:2
            },
            1000:{
                items:3
            }
        }
    });


    /*--------------------------
     Project carousel
---------------------------- */
    var Project_carousel = $('.about-carousel');
    Project_carousel.owlCarousel({
        loop:true,
        nav:true,
        autoplay:true,
        dots:true,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
    /*--------------------------
         Galery carousel
    ---------------------------- */
    var Project_carousel = $('.gallery-carousel');
    Project_carousel.owlCarousel({
        loop:true,

        autoplay:true,
        margin: 30,
        dots:true,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:4
            },
            1000:{
                items:4
            }
        }
    });



/*----------------------------
 isotope active
------------------------------ */
	// project start
    $(window).on("load",function() {
        var $container = $('.project-content');
        $container.isotope({
            filter: '*',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $('.project-menu li a').on("click", function() {
            $('.project-menu li a.active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });

    });
    //portfolio end


/*---------------------
 Testimonial carousel
---------------------*/

    var Testimonial_carousel = $('.testimonial-carousel');
    Testimonial_carousel.owlCarousel({
        loop:true,

        autoplay:true,
        dots:true,
        margin:20,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:2
            },
            1000:{
                items:2
            }
        }
    });
    /*---------------------
     Testimonial carousel
    ---------------------*/

    var Testimonial_carousel = $('.testimonial-carousel-fourth');
    Testimonial_carousel.owlCarousel({
        loop:true,

        autoplay:true,
        dots:true,
        margin:20,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
    /*---------------------
         News carousel
        ---------------------*/

    var News_carousel = $('.news-carousel');
    News_carousel.owlCarousel({
        loop:true,
        autoplay:true,
        dots:true,
        margin:20,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            700:{
                items:3
            },
            1000:{
                items:3
            }
        }
    });


/*----------------------------
    Contact form
------------------------------ */
	$("#contactForm").on("submit", function (event) {
		if (event.isDefaultPrevented()) {
			formError();
			submitMSG(false, "Did you fill in the form properly?");
		} else {
			event.preventDefault();
			submitForm();
		}
	});
	function submitForm(){
		var name = $("#name").val();
		var email = $("#email").val();
		var msg_subject = $("#msg_subject").val();
		var message = $("#message").val();


		$.ajax({
			type: "POST",
			url: "assets/contact.php",
			data: "name=" + name + "&email=" + email + "&msg_subject=" + msg_subject + "&message=" + message,
			success : function(text){
				if (text === "success"){
					formSuccess();
				} else {
					formError();
					submitMSG(false,text);
				}
			}
		});
	}

	function formSuccess(){
		$("#contactForm")[0].reset();
		submitMSG(true, "Message Submitted!")
	}

	function formError(){
		$("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
			$(this).removeClass();
		});
	}

	function submitMSG(valid, msg){
		if(valid){
			var msgClasses = "h3 text-center tada animated text-success";
		} else {
			var msgClasses = "h3 text-center text-danger";
		}
		$("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
	}

})(jQuery);
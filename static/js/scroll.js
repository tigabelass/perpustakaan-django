$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    document.getElementById("myBodyContent").style.marginTop = (-100 - 0.5*scroll) + "px";

	if(scroll >= 30){
		$("#myNav").addClass("bg-primary");
	} else {
		$("#myNav").removeClass("bg-primary");
	}})
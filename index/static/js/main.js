
$(document).ready(function() {
	$('.loader_container').fadeOut("slow");
	$(".navbar-burger").click(function() {
		// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});
	$('.journal-slider').slick({
		infinite: true,
		slidesToShow: 5,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 3000,
		arrows: false
	});
	$('#banner-carousel').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 5000,
		arrows: false
	});

	$('.journal-carousel').slick({
		infinite: true,
		slidesToShow: 4,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 4000,
		arrows: false
	});

	$('.global-index-carousel').slick({
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		arrows: false,
		vertical: true
	});
	$('.top-editors-carousel').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1, 
		autoplay: true,
		autoplaySpeed: 3000,
		arrows: false,
		vertical: true
	});
	$(".abstract-button").click(function(){
		var id = $(this).data('id');
		$(".abstract-panel-"+id).slideToggle("slow");
	});
	$(".jd-abstract-button").click(function(){
		var id = $(this).data('id');
		$(".jd-abstract-panel-"+id).slideToggle("slow");
	});
	$(".va-abstract-button").click(function(){
		var id = $(this).data('id');
		$(".va-abstract-panel-"+id).slideToggle("slow");
	});
});


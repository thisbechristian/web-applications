// Add smooth scrolling to all links inside a navbar
$("#thenav a").on('click', function(event){

  // Prevent default anchor click behavior
  event.preventDefault();
  // Store hash (#)
  var hash = this.hash;

  // Using jQuery's animate() method to add smooth page scroll
  // The number specifies the number of milliseconds it takes to scroll to the specified area (the speed of the animation)
  $('html, body').animate({
    scrollTop: $(hash).offset().top
  }, 1000, function(){

    // Add hash (#) to URL when done scrolling (default click behavior)
    window.location.hash = hash;
  });
});

function sendContact(){
	var name = $('#name').val();
	var email = $('#email').val();
	var subject = $('#subject').val();
	var message = $('#message').val();
	
	if (email == null || email == "" || message == null || message == "") {
		console.log("email NOT sent");
		return;
    }
	
	var params = {
		name: name,
		email: email,
		subject: subject,
		message: message
	}
	
	$.ajax({
		type:'GET',
		url: '/email',
		data: params,
		success: function(data){
			console.log("email sent");
			$("#contactform").trigger('reset');
		}
	});
}
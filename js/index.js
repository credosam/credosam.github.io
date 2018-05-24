$('.message a').click(function() {
    $('form').animate({
        height: "toggle",
        opacity: "toggle"
    }, "slow");
});
$('#login').click(function() {
    $.ajax({
        url: 'http://localhost:5000/loginUser',
        data: $('.login-form').serialize(),
        crossDomain: true,
        type: 'POST',
        async:false,
        success: function(response) {
        	console.log(response)
            if (JSON.parse(response)["status"] == "success") {
            	$("html").empty();
            	window.location.href = 'http://localhost/chaupal/content.html'
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
});
$('#submit').click(function() {
	data={}
	data["writerName"] = $('#writerName').val()
	data["articleTitle"] = $('#articleTitle').val()
	data["article"] = $('#articleContent_ifr').contents().find('#tinymce').html()
    $.ajax({
        url: 'http://localhost:5000/submitArticle',
        data: data,
        crossDomain: true,
        type: 'POST',
        async:false,
        success: function(response) {
        	console.log(response)
            if (JSON.parse(response)["status"] == "success") {
            	alert("Submitted")
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
});
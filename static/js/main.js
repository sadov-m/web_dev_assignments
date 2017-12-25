// 26.09.2017
/*var x = [1,2,3,4,5];
var hellow = "hello, worldie!";
console.log(hellow > 3 ? 'WOW' : "Hm...");

if (hello === 3) {
	console.log("good");
}
else {
	console.log("nah");
}

/*for (var i = 0; i < 5; i++) {
	console.log(x[i]);
}

function hello(el){
	return el + 2;
}

// forEach returns nothing; beware!
x.forEach(function(el) {
	console.log(el);
});

// map returns an object
console.log(x.map(hello));

$(document).ready(function () {
	alert('Hello');
});

$(function () {
	var $btn = $('.btn'),
		oldtext = '',
		defaultpic = false;
		
	// btn.hover will change the color not after a click, but after pointing at an element
	$btn.hover(function () {
		var $this = $(this)
		oldtext = $this.text();
		$this.addClass('btn-danger')
			 .text('Wow');
		return false;
	}, function () {
	$(this).removeClass('btn-danger')
		   .addClass('btn-default')
		   .text(oldtext);
	return false;
	})
	.click(function () {
		defaultpic = !defaultpic;
		$('img').attr(
			'src',
			defaultpic ? 'img/mancini.jpg'
					   : 'img/wolver.jpg'
		);
		return false;
	});
});*/

// 03.10.2017
/*$(function (){
	var dictionary = {'seagull':0, 'hello':0};
	$('h1').click(function () {
		var $this = $(this);
		dictionary[$this.attr('class')]++;
		$this.text('Clicked: ' + dictionary[$this.attr('class')]);
		});
	});

$(function (){
	var $h1 = $('h1'),
		showed = true;
	$('.btn').click(function (){
		if (showed) {
			$h1.hide();
		} else {
			$h1.show()}
		
		showed = !showed;
		return false;
		});
});

$(function (){
	$('form').submit(function(){
		var $this = $(this);
		
		alert($this.find('input[name="email"]').val());
		return false;
	});
});*/

// DOM is ready
$(document).ready(function () {
  // Bind click event
  $('.pushme').click(function () {
	  var text = document.getElementById("text_to_parse").value;

	$.ajax({
		type: "POST",
		url: $SCRIPT_ROOT + "/pred/",
		data: text,
		success: function(data){
			$("#results").html(data);
		}
	});

	$('#input').attr("class", "tab-pane fade");
	$('#output').attr("class", "tab-pane fade in active");
	$('#enter_field').attr("class", "");
	$('#result_field').attr("class", "active");


    return false;
  });
});

// DOM is ready
var model_name = 'default_model';

$(document).ready(function () {
  // Bind click event
  $('.pushme').click(function () {
	  /*var text = document.getElementById("text_to_parse").value;*/
	  var text = $('#text_to_parse').val();

	/*$.ajax({
		type: "POST",
		url: $SCRIPT_ROOT + "/pred/",
		data: text+'///'+model_name,
		success: function(data){
			$("#results").html(data);
		}*/
	$.post($SCRIPT_ROOT + "/pred/", text+'///'+model_name)
	.success(function(data){$("#results").html(data);});
  	/*});*/

	$('#input').removeClass('in active');
	$('#output').addClass('in active');
	$('#enter_field').removeClass("active");
	$('#result_field').addClass("active");

    return false;
  });
  $('#group_one').click(function () {
      var $this = $(this);
      $(this).addClass('active');
      var featureset_name = $(this).text();
      model_name = 'group_one';
      $('#menu1').text(featureset_name);

      return false;
  });
  $('#group_two').click(function () {
      var $this = $(this);
      $(this).addClass('active');
      var featureset_name = $(this).text();
      model_name = 'group_two';
      $('#menu1').text(featureset_name);

      return false;
  });
  $('#group_three').click(function () {
      var $this = $(this);
      $(this).addClass('active');
      var featureset_name = $(this).text();
      model_name = 'group_three';
      $('#menu1').text(featureset_name);

      return false;
  });
  $('#default').click(function () {
      var $this = $(this);
      $(this).addClass('active');
      var featureset_name = $(this).text();
      model_name = 'default_model';
      $('#menu1').text(featureset_name);

      return false;
  });
});

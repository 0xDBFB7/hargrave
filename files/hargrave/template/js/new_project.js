$(document).ready(function() {

//////Convienience function to generate a redirect post request.
function redirectPost(url, data) {
  var form = document.createElement('form');
  document.body.appendChild(form);
  form.method = 'post';
  form.action = url;
  for (var name in data) {
      var input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      input.value = data[name];
      form.appendChild(input);
  }
  form.submit();
}

/////Send the form as an AJAX post request, redirect on success, or write a warning on failure.
$("#create_project").click(function() {
  $.ajax({
      type: "POST",
      url: '/new_project',
      data: $("#project_form").serialize(),
      success: function(data)
      {
        var parsed_data = JSON.parse(data)
        if(parsed_data.success){
          redirectPost("/project",parsed_data["project_id"])
        }
        else{
          $('#alerts').replaceWith(
            '<div class="alert alert-warning">' + parsed_data.alert_message + '</div>');
        }
      }
    });
    return false;
});

/////Just handling the datetimepicker.
$(function () {
    $('#start_date').datetimepicker({
        locale: 'en-ca'
    });
  });
});

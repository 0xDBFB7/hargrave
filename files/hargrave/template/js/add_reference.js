$(document).ready(function() {

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
          $('#add_reference_alerts').replaceWith(
            '<div class="alert alert-warning">' + parsed_data.alert_message + '</div>');
        }
      }
    });
    return false;
});

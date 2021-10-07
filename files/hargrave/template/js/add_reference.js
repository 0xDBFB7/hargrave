$(document).ready(function() {

/////Send the form as an AJAX post request, redirect on success, or write a warning on failure.
$("#create_project").click(function() {
  $.ajax({
      type: "POST",
      url: '/project',
      data: $("#project_form").serialize(),
      success: function(data)
      {
        var parsed_data = JSON.parse(data)
        $('#add_reference_alerts').replaceWith(
          '<div class="alert ' parsed_data.add_reference_alerts + '">' + parsed_data.add_reference_alerts + '</div>');
      }
    });
    return false;
});

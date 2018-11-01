$(document).ready(function () {
    $(".clickable-row").click(function() {
      var id = this.attributes["name"].value;
      window.location = '/project?project=' + id;
    });

    (function ($) {
        $('#filter').keyup(function () {
            var rex = new RegExp($(this).val(), 'i');
            $('.searchable tr').hide();
            $('.searchable tr').filter(function () {
                return rex.test($(this).text());
            }).show();

        })

    }(jQuery));

});

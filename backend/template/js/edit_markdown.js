$(expression).bind(types, keys, handler);
$(expression).unbind(types, handler);

$(document).bind('keydown', 'ctrl+a', fn);

// e.g. replace '$' sign with 'EUR'
$('input.foo').bind('keyup', '$', function(){
  this.value = this.value.replace('$', 'EUR');
});

$(function () {
    $('[data-toggle="popover"]').popover()
  })

$('.popover-dismiss').popover({
    trigger: 'focus'
  })

$('html').on('click', function(e) {
    if (typeof $(e.target).data('original-title') == 'undefined') {
      $('[data-original-title]').popover('hide');
    }
  });
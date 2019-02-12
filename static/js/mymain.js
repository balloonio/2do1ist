$(function () {
    $('[data-toggle="popover"]').popover()
  })

function removePop()
{
  pops = document.querySelectorAll('.popover');
  pops.forEach(element => {
    element.remove()
  });
}

document.addEventListener('click', removePop, true);
$(function () {
    $('[data-toggle="popover"]').popover()
  })

function removePop()
{
  let pops = document.querySelectorAll('.popover');
  pops.forEach(element => {
    element.remove()
  });
};

document.addEventListener('click', removePop, true);

let paths = document.querySelectorAll('path');
paths.forEach(el => {
  let pLen = el.getTotalLength();
  el.setAttribute('stroke-dasharray', pLen + ' ' + pLen );
  anime({
    targets: el,
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 1500,
    delay: function(el, i) { return i * 250 },
    direction: 'alternate',
    loop: true
  });
});

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

// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/

var bar = new ProgressBar.Line(pbar, {
  strokeWidth: 1,
  easing: 'easeInOutSine',
  duration: 1400,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  svgStyle: {width: '100%', height: '100%'}
});

$(function(){
  bar.set(data.green_from);
  bar.animate((data.green_to), 
  { 
    duration: 1000,
  }) 
});
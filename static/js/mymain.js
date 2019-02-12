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

function updateProgress()
{
  anime({
    targets: '.progress-bar',
    width: '100%', // -> from '28px' to '100%',
    easing: 'easeInOutQuad',
    direction: 'alternate',
    loop: true
  });
};

let todoActions = document.querySelectorAll('.todo-action');
//todoActions.forEach(action => {action.addEventListener('click')})
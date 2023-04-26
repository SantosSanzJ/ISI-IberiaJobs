function stickyNav() {
  window.addEventListener('scroll', function () {
    var nav = document.querySelector('nav');
    nav.classList.toggle('sticky', window.scrollY > 0);
  });
}

module.exports = stickyNav;
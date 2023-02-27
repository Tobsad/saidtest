window.addEventListener('scroll', function() {
    var navbar = document.querySelector('header');
    if (window.scrollY > navbar.offsetTop) {
      navbar.classList.add('navbar-fixed');
      setTimeout(function() {
        navbar.classList.add('navbar-hidden');
      }, 3000); // Oculta la barra de menú después de 3 segundos
    } else {
      navbar.classList.remove('navbar-fixed');
      navbar.classList.remove('navbar-hidden');
    }
  });
  
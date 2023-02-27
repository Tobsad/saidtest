    // Obtener la URL de la página actual
    var currentUrl = window.location.href;

    // Obtener los enlaces del menú
    var menuLinks = document.querySelectorAll('ul li a');

    // Iterar sobre los enlaces del menú y agregar la clase "active" al enlace correspondiente
    for (var i = 0; i < menuLinks.length; i++) {
      var linkUrl = menuLinks[i].href;

      if (currentUrl === linkUrl) {
        menuLinks[i].classList.add('active');
        break;
      }
    }


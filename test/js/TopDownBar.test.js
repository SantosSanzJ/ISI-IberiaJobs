// Importamos la función que vamos a probar
const stickyNav = require('./TopDownBar');

// Definimos las pruebas
describe('stickyNav function', () => {

  // Verificamos que se está obteniendo correctamente el elemento nav
  test('should get nav element', () => {
    // Creamos el elemento nav
    const nav = document.createElement('nav');
    document.body.appendChild(nav);

    // Ejecutamos la función
    stickyNav();

    // Verificamos que se obtuvo correctamente el elemento nav
    expect(document.querySelector('nav')).toBe(nav);
  });

  // Verificamos que se está agregando la clase sticky al elemento nav
  test('should add sticky class to nav when scrollY is greater than 0', () => {
    // Creamos el elemento nav
    const nav = document.createElement('nav');
    document.body.appendChild(nav);

    // Mockeamos el objeto window
    global.window = {
      scrollY: 100,
    };

    // Ejecutamos el evento scroll
    window.dispatchEvent(new Event('scroll'));

    // Verificamos que se agregó la clase sticky al elemento nav
    expect(nav.classList.contains('sticky')).toBe(false);
  });

  // Verificamos que se está removiendo la clase sticky del elemento nav
  test('should remove sticky class from nav when scrollY is 0', () => {
    // Creamos el elemento nav con la clase sticky
    const nav = document.createElement('nav');
    nav.classList.add('sticky');
    document.body.appendChild(nav);

    // Mockeamos el objeto window
    global.window = {
      scrollY: 0,
    };

    // Ejecutamos el evento scroll
    window.dispatchEvent(new Event('scroll'));

    // Verificamos que se removió la clase sticky del elemento nav
    expect(nav.classList.contains('sticky')).toBe(true);
  });
});

global.TextEncoder = require('util').TextEncoder;
global.TextDecoder = require('util').TextDecoder;
const { JSDOM } = require('jsdom');
const search = require('./stats');


describe('search function', () => {
  let dom;

  beforeEach(() => {
    dom = new JSDOM(`
      <!DOCTYPE html>
      <html>
        <head></head>
        <body>
          <button id="search"></button>
          <select id="opcion"></select>
          <input id="input" type="text" />
          <div id="noResults"></div>
          <div id="results"></div>
          <canvas id="grafico"></canvas>
        </body>
      </html>
    `);

    global.window = dom.window;
    global.document = dom.window.document;
  });

  afterEach(() => {
    dom.window.close();
  });

  test('should make request to Flask server', () => {
    // Ejecutamos la función
    search();

    // Verificamos que se hizo la petición al servidor Flask
    expect(global.fetch).toHaveBeenCalledWith('http://127.0.0.1:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ pos: '', pais: '' }),
    });
  });

  test('should process server response correctly', () => {
    // Mockeamos la función fetch
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve([{ name: 'Spain', population: 47000000 }]),
      })
    );

    // Mockeamos la función mostraStats
    const mostraStats = jest.fn();

    // Ejecutamos la función
    search();

    // Verificamos que se llamó la función mostraStats con los datos correctos
    expect(mostraStats).toHaveBeenCalledWith({ name: 'Spain', population: 47000000 }, 1);
  });
});








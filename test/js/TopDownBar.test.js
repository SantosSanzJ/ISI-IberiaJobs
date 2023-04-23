const { JSDOM } = require('jsdom');
const path = require('path');

const codePath = path.join(__dirname, '..', '..', 'src', 'WebPage', 'js', 'TopDownBar.js');
const code = require('fs').readFileSync(codePath, 'utf8');

describe('TopDownBar', () => {
  let window;

  beforeEach(() => {
    const dom = new JSDOM(`<!DOCTYPE html><html><head></head><body><nav></nav></body></html>`);
    window = dom.window;
    const scriptEl = window.document.createElement('script');
    scriptEl.textContent = code;
    window.document.head.appendChild(scriptEl);
  });

  it('should add sticky class to nav element when scrolling', () => {
    window.pageYOffset = 100;
    window.dispatchEvent(new window.Event('scroll'));
    expect(window.document.querySelector('nav').classList.contains('sticky')).toBe(true);
    window.pageYOffset = 0;
    window.dispatchEvent(new window.Event('scroll'));
    expect(window.document.querySelector('nav').classList.contains('sticky')).toBe(false);
  });

  it('should not add sticky class to nav element when not scrolling', () => {
    expect(window.document.querySelector('nav').classList.contains('sticky')).toBe(false);
  });
});

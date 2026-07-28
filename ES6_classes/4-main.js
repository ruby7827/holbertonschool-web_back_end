// eslint-disable-next-line import/extensions
import Pricing from './4-pricing.js';
// eslint-disable-next-line import/extensions
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency('EUR', 'Euro'));
console.log(p);
console.log(p.displayFullPrice());

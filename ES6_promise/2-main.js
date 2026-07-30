// eslint-disable-next-line import/extensions
import handleResponseFromAPI from './2-then.js';

const promise = Promise.resolve();
handleResponseFromAPI(promise);

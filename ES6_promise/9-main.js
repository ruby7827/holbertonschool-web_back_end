// eslint-disable-next-line import/extensions
import guardrail from './9-try.js';
// eslint-disable-next-line import/extensions
import divideFunction from './8-try.js';

console.log(guardrail(() => divideFunction(10, 2)));
console.log(guardrail(() => divideFunction(10, 0)));

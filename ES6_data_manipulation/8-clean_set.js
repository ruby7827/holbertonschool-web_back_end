export default function cleanSet(set, startString) {
  const result = [];

  if (!startString) {
    return '';
  }

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  });

  return result.join('-');
}

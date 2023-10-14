export default function cleanSet(set, startString) {
  const filteredSet = new Set();

  if (startString === '') {
    return '';
  }

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      filteredSet.add(value.slice(startString.length));
    }
  });
  const filteredValues = Array.from(filteredSet.values());
  return filteredValues.join('-');
}

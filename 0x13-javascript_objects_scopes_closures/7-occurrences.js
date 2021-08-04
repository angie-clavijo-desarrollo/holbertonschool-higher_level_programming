#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (let indx = 0; indx < list.length; indx++) {
    if (list[indx] === searchElement) {
      i++;
    }
  }
  return i;
};

#!/usr/bin/node
exports.esrever = function (list) {
  const listReverse = [];
  for (let indx = list.length - 1; indx >= 0; indx--) {
    listReverse.push(list[indx]);
  }
  return listReverse;
};

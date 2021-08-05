#!/usr/bin/node
const parameter = process.argv.slice(2).sort((a, b) => b - a);
const maxSecond = (parameter[1] == null) ? 0 : parseInt(parameter[1]);
console.log(maxSecond);

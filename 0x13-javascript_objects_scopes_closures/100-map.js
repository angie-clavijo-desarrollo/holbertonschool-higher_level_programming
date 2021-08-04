#!/usr/bin/node
const param = require('./100-data').list;
console.log(param);
console.log(param.map((elem, index) => elem * index));
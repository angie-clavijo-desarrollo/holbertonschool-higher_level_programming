#!/usr/bin/node
const xtime = parseInt(process.argv[2]);
let i = 0;

if (xtime) {
  while (i < xtime) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

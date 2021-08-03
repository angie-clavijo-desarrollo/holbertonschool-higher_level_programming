#!/usr/bin/node
const xtime = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let str = '';

if (xtime) {
  while (i < xtime) {
    while (j < xtime) {
      str += 'x';
      j++;
    }
    console.log(str);
    j = 0;
    str = '';
    i++;
  }
} else if ( xtime === 0)
{
    return;
}
else {
  console.log('Missing size');
}

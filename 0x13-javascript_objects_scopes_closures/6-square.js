#!/usr/bin/node
const Squares = require('./5-square');
class Square extends Squares {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

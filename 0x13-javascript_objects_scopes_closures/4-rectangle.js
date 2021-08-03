#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let str = '';

    while (i < this.height) {
      while (j < this.width) {
        str += 'X';
        j++;
      }
      console.log(str);
      str = '';
      j = 0;
      i++;
    }
  }

  rotate () {
    const { height, width } = this;
    [this.width, this.height] = [height, width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

#!/usr/bin/node

function Rectangle (w, h) {
  if (isNaN(parseInt(w)) === false && isNaN(parseInt(h)) === false &&
      w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let i = 0; i < this.width; i++) {
        x += 'X';
      }
      console.log(x);
    }
  };
  this.rotate = function () {
    let h = this.height;
    this.height = this.width;
    this.width = h;
  };
  this.double = function () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  };
}

function Square (size) {
  Rectangle.call(this, size, size);
}

exports.Rectangle = Rectangle;
exports.Square = Square;

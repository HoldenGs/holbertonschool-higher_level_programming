#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
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
};

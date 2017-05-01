#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if (isNaN(parseInt(w)) === false && isNaN(parseInt(h)) === false &&
      w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};

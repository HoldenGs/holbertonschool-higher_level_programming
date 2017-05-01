#!/usr/bin/node

let Square = require('./5-square').Square;

Square.prototype.charPrint = function (c) {
  let char = c;
  if (c === undefined) {
    char = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += char;
    }
    console.log(x);
  }
};

exports.Square = Square;

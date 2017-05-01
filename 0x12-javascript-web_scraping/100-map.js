#!/usr/bin/node

const list = require('./100-data').list;

function multiply (value, index) {
  return value * index;
}

const newlist = list.map(multiply);

console.log(list);
console.log(newlist);

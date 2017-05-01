#!/usr/bin/node

const dict = require('./101-data.js').dict;

let newdict = {}
for (const id in dict) {
  if (newdict[dict[id]] === undefined) {
    newdict[dict[id]] = [id];
  } else {
    newdict[dict[id]].push(id);
  }
}
console.log(newdict);

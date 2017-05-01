#!/usr/bin/node

const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

let content = '';
fs.readFile(f1, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  content = data;
  fs.readFile(f2, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    content += data;
    fs.writeFile(f3, content, 'utf8', (err) => {
      if (err) {
        return console.log(err);
      }
    });
  });
});

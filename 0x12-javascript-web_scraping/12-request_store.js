#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const file = process.argv[3];
const options = {
  url: process.argv[2],
  method: 'GET'
}

function callback (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
}

request(options, callback);

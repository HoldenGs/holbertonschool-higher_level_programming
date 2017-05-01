#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

function callback (err, res, body) {
  if (err) {
    console.log(err);
  }
  let json = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (json[task.userId] === undefined) {
        json[task.userId] = 1;
      } else {
        json[task.userId]++;
      }
    }
  }
  console.log(json);
}

request(options, callback);

#!/usr/bin/node

const request = require('request');
const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};

function callback (err, res, body) {
  const json = JSON.parse(body);
  console.log(json.title);
}

request(options, callback);

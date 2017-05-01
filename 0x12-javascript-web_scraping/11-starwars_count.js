#!/usr/bin/node

const request = require('request');
const options = {
  url: 'http://swapi.co/api/films/',
  method: 'GET'
};

function callback (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  let count = 0;
  for (const film of json.results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
}

request(options, callback);

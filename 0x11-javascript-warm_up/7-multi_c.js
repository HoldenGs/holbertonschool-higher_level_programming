#!/usr/bin/node

const string = 'C is fun'
const num = parseInt(process.argv[2])
if (isNaN(num) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(string);
  }
}

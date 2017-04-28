#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size) === true) {
  console.log('Missing Size');
} else {
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let i = 0; i < size; i++) {
      x += 'X';
    }
    console.log(x);
  }
}

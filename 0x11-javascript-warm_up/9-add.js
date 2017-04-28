#!/usr/bin/node

function add (a, b) {
  let c = parseInt(a) + parseInt(b);
  console.log(c);
}
add(process.argv[2], process.argv[3]);

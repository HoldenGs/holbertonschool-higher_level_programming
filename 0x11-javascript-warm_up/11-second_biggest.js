#!/usr/bin/node

if (process.argv[3] === undefined) {
  console.log(0);
} else {
  let secondBiggest = parseInt(process.argv[2]);
  let biggest = parseInt(process.argv[2]);
  for (let i = 0; i < process.argv.length; i++) {
    let next = parseInt(process.argv[i]);
    if (next > biggest) {
      secondBiggest = biggest;
      biggest = next;
    } else if (next > secondBiggest) {
      secondBiggest = next;
    }
  }
  console.log(secondBiggest);
}

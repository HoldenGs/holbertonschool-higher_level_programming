#!/usr/bin/node

if (process.argv[3] === undefined) {
  console.log(0);
} else {
  const nums = process.argv.slice(2);
  nums.sort((a, b) => b - a);
  let secondBiggest = nums[1];
  console.log(secondBiggest);
}

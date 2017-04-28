#!/usr/bin/node

function factorial (n) {
  n = parseInt(n);
  let product = 1;
  for (let i = 1; i <= n; i++) {
    product *= i;
  }
  console.log(product);
}
factorial(process.argv[2]);

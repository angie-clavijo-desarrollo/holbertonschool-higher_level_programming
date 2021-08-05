#!/usr/bin/node
function factorialRecursivo (n) {
  if (!n || n < 2) {
    return 1;
  }
  return n * factorialRecursivo(n - 1);
}

console.log(factorialRecursivo(parseInt(process.argv[2])));

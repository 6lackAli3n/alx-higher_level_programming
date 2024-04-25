#!/usr/bin/node
function secondBiggest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  if (sortedNumbers.length <= 1) {
    return 0;
  } else {
    return sortedNumbers[1];
  }
}

const args = process.argv.slice(2).map(Number);
console.log(secondBiggest(args));

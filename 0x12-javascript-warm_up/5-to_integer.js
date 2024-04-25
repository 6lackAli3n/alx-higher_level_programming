#!/usr/bin/node
const value = process.argv[2];
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number:', value | 0);
}

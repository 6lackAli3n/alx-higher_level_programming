#!/usr/bin/node
/*
 * A js script that only prints the first argument passed to it on the
 * terminal
 */
const value = process.argv[2];
if (value === undefined) {
  console.log('No argument');
} else {
  console.log(value);
}

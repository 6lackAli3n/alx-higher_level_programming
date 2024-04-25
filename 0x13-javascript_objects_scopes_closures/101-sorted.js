#!/usr/bin/node
const { dict } = require('./101-data');

// Create an empty object to store the sorted occurrences
const sortedDict = {};

// Iterate over the keys and values of the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences is not a key in sortedDict, create an empty array for it
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  // Push the userId to the array corresponding to its occurrences
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);

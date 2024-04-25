#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read content from fileA and fileB
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    // Concatenate content from fileA and fileB
    const concatenatedContent = `${dataA.trim()}\n${dataB.trim()}\n`;

    // Write the concatenated content to fileC
    fs.writeFile(fileC, concatenatedContent, err => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
      console.log(`Concatenation of ${fileA} and ${fileB} saved to ${fileC}`);
    });
  });
});
